/**
 * Newsletter system for build-your-house.com.
 *
 * Public routes:
 *   POST /subscribe    { email, source?, website? }
 *     `website` is a honeypot: real users never fill it, bots do.
 *     Stores into D1 (source of truth), syncs the contact into the Resend
 *     audience, and sends a transactional email via Resend:
 *       source '/shop-sample' → delivers the 19-page sample PDF link
 *       anything else         → short welcome note
 *     Idempotent on email; a resubscribe clears unsubscribed_at and
 *     reactivates the Resend contact, but never re-sends the welcome.
 *   GET  /unsubscribe?e=<email>&t=<hmac>
 *     HMAC-signed one-click unsubscribe (link included in every email we
 *     send from here). Marks D1 + Resend contact unsubscribed and shows a
 *     small confirmation page.
 *
 * Admin (Authorization: Bearer <ADMIN_KEY> — same key as the downloads worker):
 *   GET /admin/api/subscribers            JSON: counts by source + all rows
 *   GET /admin/api/subscribers?format=csv CSV download
 *
 * SENDING A NEWSLETTER: compose a Broadcast in the Resend dashboard against
 * the "Build Your House Newsletter" audience and include
 * {{{RESEND_UNSUBSCRIBE_URL}}} in the footer. Resend handles broadcast
 * unsubscribes/suppression on its side; D1 keeps the acquisition log.
 *
 * Secrets (wrangler secret put): RESEND_API_KEY, UNSUB_SECRET, ADMIN_KEY.
 * Vars: RESEND_AUDIENCE_ID. Bindings: DB (D1 — see schema.sql).
 */

const ALLOWED_ORIGINS = new Set([
  'https://build-your-house.com',
  'http://localhost:4000',
]);

const SITE = 'https://build-your-house.com';
const FROM = 'Seth at Build Your House <seth@build-your-house.com>';
const REPLY_TO = 'seth@build-your-house.com';
const SAMPLE_URL = `${SITE}/binder-sample.pdf`;

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const MAX_EMAIL_LENGTH = 254;

function corsHeaders(origin) {
  return {
    'Access-Control-Allow-Origin': ALLOWED_ORIGINS.has(origin) ? origin : 'https://build-your-house.com',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Access-Control-Max-Age': '86400',
  };
}

function json(body, status, origin) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', ...corsHeaders(origin) },
  });
}

// ---------------------------------------------------------------- crypto

async function hmacHex(secret, message) {
  const enc = new TextEncoder();
  const key = await crypto.subtle.importKey(
    'raw', enc.encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']
  );
  const sig = await crypto.subtle.sign('HMAC', key, enc.encode(message));
  return [...new Uint8Array(sig)].map((b) => b.toString(16).padStart(2, '0')).join('');
}

async function constantTimeEqual(a, b) {
  const enc = new TextEncoder();
  const [da, db] = await Promise.all([
    crypto.subtle.digest('SHA-256', enc.encode(a)),
    crypto.subtle.digest('SHA-256', enc.encode(b)),
  ]);
  const ua = new Uint8Array(da);
  const ub = new Uint8Array(db);
  let diff = 0;
  for (let i = 0; i < ua.length; i++) diff |= ua[i] ^ ub[i];
  return diff === 0;
}

async function unsubscribeUrl(env, requestUrl, email) {
  const token = await hmacHex(env.UNSUB_SECRET, email);
  const base = new URL(requestUrl).origin;
  return `${base}/unsubscribe?e=${encodeURIComponent(email)}&t=${token}`;
}

// ---------------------------------------------------------------- resend

async function resend(env, path, { method = 'GET', body } = {}) {
  const res = await fetch(`https://api.resend.com${path}`, {
    method,
    headers: {
      Authorization: `Bearer ${env.RESEND_API_KEY}`,
      ...(body ? { 'Content-Type': 'application/json' } : {}),
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const data = await res.json().catch(() => ({}));
  if (!res.ok) {
    throw new Error(data?.message || `Resend API error ${res.status}`);
  }
  return data;
}

async function upsertContact(env, email, unsubscribed) {
  // Create, and on "already exists" fall through to PATCHing the flag.
  try {
    await resend(env, `/audiences/${env.RESEND_AUDIENCE_ID}/contacts`, {
      method: 'POST',
      body: { email, unsubscribed },
    });
  } catch {
    await resend(env, `/audiences/${env.RESEND_AUDIENCE_ID}/contacts/${encodeURIComponent(email)}`, {
      method: 'PATCH',
      body: { unsubscribed },
    });
  }
}

// ---------------------------------------------------------------- emails

function emailFooter(unsubUrl) {
  return {
    text: `\n—\nYou're getting this because you signed up at build-your-house.com. Unsubscribe: ${unsubUrl}`,
    html: `<p style="color:#888;font-size:12px;margin-top:28px">You're getting this because you signed up at <a href="${SITE}">build-your-house.com</a>. <a href="${unsubUrl}">Unsubscribe</a>.</p>`,
  };
}

function sampleEmail(unsubUrl) {
  const f = emailFooter(unsubUrl);
  return {
    subject: 'Your 19 sample pages from the Job Site Binder',
    text: `Hi,

Here are your sample pages — 19 real pages straight out of the Owner-Builder Job Site Binder: the full 1.5 Foundation Checklist and the complete 8.2 Span Tables, same typesetting as the binder itself.

Download the sample (PDF):
${SAMPLE_URL}

Print them, take them outside, write on them. If they earn a spot in your truck, the full binder is 367 pages across 8 sections — plus editable Word contracts and Excel budget workbooks:
${SITE}/shop

Questions about your build? Just reply — I read these.

Seth
Build Your House
${SITE}
${f.text}`,
    html: `<p>Hi,</p>
<p>Here are your sample pages — <strong>19 real pages</strong> straight out of the Owner-Builder Job Site Binder: the full 1.5 Foundation Checklist and the complete 8.2 Span Tables, same typesetting as the binder itself.</p>
<p><a href="${SAMPLE_URL}"><strong>Download the sample (PDF)</strong></a></p>
<p>Print them, take them outside, write on them. If they earn a spot in your truck, the full binder is 367 pages across 8 sections — plus editable Word contracts and Excel budget workbooks: <a href="${SITE}/shop">build-your-house.com/shop</a>.</p>
<p>Questions about your build? Just reply — I read these.</p>
<p>Seth<br>Build Your House<br><a href="${SITE}">build-your-house.com</a></p>
${f.html}`,
  };
}

function welcomeEmail(unsubUrl) {
  const f = emailFooter(unsubUrl);
  return {
    subject: 'Welcome — owner-builder guides, straight talk, no filler',
    text: `Hi,

Thanks for subscribing to Build Your House. Here's what to expect: an occasional email when there's something genuinely useful for an owner-builder — new guides, tools, or hard-won lessons. No filler, no daily drip.

If you're just getting started, this is the page I'd read first:
${SITE}/start-here

Questions about your build? Just reply — I read these.

Seth
Build Your House
${SITE}
${f.text}`,
    html: `<p>Hi,</p>
<p>Thanks for subscribing to Build Your House. Here's what to expect: an occasional email when there's something genuinely useful for an owner-builder — new guides, tools, or hard-won lessons. No filler, no daily drip.</p>
<p>If you're just getting started, this is the page I'd read first: <a href="${SITE}/start-here">the owner-builder roadmap</a>.</p>
<p>Questions about your build? Just reply — I read these.</p>
<p>Seth<br>Build Your House<br><a href="${SITE}">build-your-house.com</a></p>
${f.html}`,
  };
}

async function sendOnboardEmail(env, requestUrl, email, source) {
  const unsubUrl = await unsubscribeUrl(env, requestUrl, email);
  const msg = source === '/shop-sample' ? sampleEmail(unsubUrl) : welcomeEmail(unsubUrl);
  await resend(env, '/emails', {
    method: 'POST',
    body: {
      from: FROM,
      to: [email],
      reply_to: REPLY_TO,
      subject: msg.subject,
      text: msg.text,
      html: msg.html,
    },
  });
}

// ---------------------------------------------------------------- handlers

async function handleSubscribe(request, env, ctx, origin) {
  let payload;
  try {
    payload = await request.json();
  } catch {
    return json({ error: 'invalid JSON' }, 400, origin);
  }

  // Honeypot filled → almost certainly a bot. Pretend success, store nothing.
  if (typeof payload.website === 'string' && payload.website.trim() !== '') {
    return json({ ok: true }, 200, origin);
  }

  const email = typeof payload.email === 'string' ? payload.email.trim().toLowerCase() : '';
  if (!email || email.length > MAX_EMAIL_LENGTH || !EMAIL_RE.test(email)) {
    return json({ error: 'invalid email' }, 400, origin);
  }

  const source = typeof payload.source === 'string' ? payload.source.slice(0, 200) : null;
  const now = new Date().toISOString();

  let isNew = false;
  let wasUnsubscribed = false;
  try {
    const existing = await env.DB.prepare(
      'SELECT unsubscribed_at FROM subscribers WHERE email = ?1'
    ).bind(email).first();
    if (!existing) {
      isNew = true;
      await env.DB.prepare(
        'INSERT INTO subscribers (email, source, created_at) VALUES (?1, ?2, ?3)'
      ).bind(email, source, now).run();
    } else if (existing.unsubscribed_at) {
      wasUnsubscribed = true;
      await env.DB.prepare(
        'UPDATE subscribers SET unsubscribed_at = NULL WHERE email = ?1'
      ).bind(email).run();
    }
  } catch (err) {
    console.error('subscribe upsert failed:', err);
    return json({ error: 'storage error' }, 500, origin);
  }

  // Post-storage work never blocks the response (or the user's success state).
  ctx.waitUntil((async () => {
    try {
      await upsertContact(env, email, false);
    } catch (err) {
      console.error('resend contact sync failed:', err);
    }
    // Sample requests always deliver the PDF (even to an existing subscriber —
    // they asked for it). The welcome goes only to genuinely new signups.
    if (source === '/shop-sample' || isNew || wasUnsubscribed) {
      try {
        await sendOnboardEmail(env, request.url, email, source);
      } catch (err) {
        console.error('onboard email failed:', err);
      }
    }
  })());

  return json({ ok: true }, 200, origin);
}

async function handleUnsubscribe(request, env) {
  const url = new URL(request.url);
  const email = (url.searchParams.get('e') || '').trim().toLowerCase();
  const token = url.searchParams.get('t') || '';
  const page = (title, body) =>
    new Response(
      `<!doctype html><meta name="viewport" content="width=device-width,initial-scale=1"><body style="font-family:system-ui,sans-serif;max-width:480px;margin:80px auto;padding:0 20px;color:#232019"><h2 style="margin-bottom:8px">${title}</h2><p style="color:#555;line-height:1.5">${body}</p><p style="margin-top:32px"><a href="${SITE}" style="color:#c75a22">build-your-house.com</a></p></body>`,
      { headers: { 'Content-Type': 'text/html; charset=utf-8' } }
    );

  if (!email || !EMAIL_RE.test(email) || !token) {
    return page('That link doesn’t look right', 'The unsubscribe link is missing part of its address. Use the link from the bottom of the email, or reply to any email and I’ll remove you by hand.');
  }
  const expected = await hmacHex(env.UNSUB_SECRET, email);
  if (!(await constantTimeEqual(token, expected))) {
    return page('That link doesn’t look right', 'The unsubscribe link didn’t verify. Use the link from the bottom of the email, or reply to any email and I’ll remove you by hand.');
  }

  try {
    await env.DB.prepare(
      'UPDATE subscribers SET unsubscribed_at = ?1 WHERE email = ?2 AND unsubscribed_at IS NULL'
    ).bind(new Date().toISOString(), email).run();
  } catch (err) {
    console.error('unsubscribe update failed:', err);
  }
  try {
    await upsertContact(env, email, true);
  } catch (err) {
    console.error('resend unsubscribe sync failed:', err);
  }

  return page('You’re unsubscribed', `${email} won’t get any more emails from Build Your House. Changed your mind? Any signup form on the site will re-subscribe you.`);
}

async function isAuthorized(request, env) {
  if (!env.ADMIN_KEY) return false;
  const key = (request.headers.get('Authorization') || '').replace(/^Bearer\s+/i, '');
  if (!key) return false;
  return constantTimeEqual(key, env.ADMIN_KEY);
}

async function handleAdminSubscribers(request, env, origin) {
  const url = new URL(request.url);
  const { results } = await env.DB.prepare(
    'SELECT email, source, created_at, unsubscribed_at FROM subscribers ORDER BY created_at DESC'
  ).all();

  if (url.searchParams.get('format') === 'csv') {
    const esc = (v) => (v == null ? '' : `"${String(v).replace(/"/g, '""')}"`);
    const csv = ['email,source,created_at,unsubscribed_at']
      .concat(results.map((r) => [r.email, r.source, r.created_at, r.unsubscribed_at].map(esc).join(',')))
      .join('\n');
    return new Response(csv, {
      headers: {
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename="subscribers.csv"',
        ...corsHeaders(origin),
      },
    });
  }

  const bySource = {};
  let active = 0;
  for (const r of results) {
    const s = r.source || '(none)';
    bySource[s] = (bySource[s] || 0) + 1;
    if (!r.unsubscribed_at) active++;
  }
  return json(
    { total: results.length, active, unsubscribed: results.length - active, bySource, subscribers: results },
    200,
    origin
  );
}

export default {
  async fetch(request, env, ctx) {
    const origin = request.headers.get('Origin');
    const url = new URL(request.url);

    try {
      if (request.method === 'OPTIONS') {
        return new Response(null, { status: 204, headers: corsHeaders(origin) });
      }
      if (request.method === 'POST' && url.pathname === '/subscribe') {
        return await handleSubscribe(request, env, ctx, origin);
      }
      if (request.method === 'GET' && url.pathname === '/unsubscribe') {
        return await handleUnsubscribe(request, env);
      }
      if (url.pathname === '/admin/api/subscribers') {
        if (!(await isAuthorized(request, env))) {
          return json({ error: 'unauthorized' }, 401, origin);
        }
        return await handleAdminSubscribers(request, env, origin);
      }
      return json({ error: 'not found' }, 404, origin);
    } catch (err) {
      console.error('unhandled error:', err);
      return json({ error: 'internal error' }, 500, origin);
    }
  },
};
