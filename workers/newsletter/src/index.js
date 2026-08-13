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
 *   POST /estimate     { email, website?, calculator, calculatorName, hero,
 *                        cost, inputs[], lines[], sourcePath? }
 *     The calculator tear-off: subscribes like /subscribe (welcome email
 *     suppressed — the takeoff email IS the transactional email) and sends
 *     the visitor their takeoff. Every string is length-capped, URL-stripped,
 *     and HTML-escaped so the endpoint can't be used to relay attacker
 *     content; calculator slug must match the known-slug pattern.
 *     Rate-limited per IP (per-isolate).
 *   POST /financing-lead  { name, email, phone, state, timeline, creditBand,
 *                           landStatus, budgetBand?, notes?, website?, sourcePath? }
 *     Owner-builder lender-match intake (the qualified-lead product).
 *     All enum fields validated against whitelists; free text is capped and
 *     URL-stripped. Stores into financing_leads (D1), emails Seth the lead,
 *     and subscribes the address (disclosed on the form). Honeypot +
 *     per-IP rate limit.
 *   GET  /unsubscribe?e=<email>&t=<hmac>
 *     HMAC-signed one-click unsubscribe (link included in every email we
 *     send from here). Marks D1 + Resend contact unsubscribed and shows a
 *     small confirmation page.
 *
 * POST /subscribe also accepts (used by the downloads worker on purchases):
 *   quiet: true      — store/sync only, send no onboarding email
 *   purchased: true  — stamp purchased_at (exits the drip sequence)
 *   insert: false    — only update an existing row, never create one
 *                      (buyers who didn't tick the consent box are marked
 *                      purchased if already subscribed, but never added)
 *
 * DRIP SEQUENCE: a daily cron (see wrangler.jsonc triggers) sends one
 * follow-up per branch at day 3 — '/shop-sample' signups get the sample
 * follow-up; everyone else gets the permit-mistakes email (with an NC kit
 * variant when the source is the NC state guide). Suppressed for
 * unsubscribed or purchased subscribers; sends are recorded in
 * sequence_sends so each step fires at most once per address.
 *
 * Admin (Authorization: Bearer <ADMIN_KEY> — same key as the downloads worker):
 *   GET  /admin/api/subscribers            JSON: counts by source + sequence
 *                                          sends + all rows
 *   GET  /admin/api/subscribers?format=csv CSV download
 *   POST /admin/api/run-sequence           Run the drip pass now (same code
 *                                          path as the cron; idempotent)
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
const WORKER_ORIGIN = 'https://buildyourhouse-newsletter.azerothcorner.workers.dev/';
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

Start with these: 19 real sample pages from the Owner-Builder Job Site Binder — the full foundation checklist and the complete span tables, free:
${SITE}/binder-sample.pdf

And if you're just getting started, this is the page I'd read first:
${SITE}/start-here

Questions about your build? Just reply — I read these.

Seth
Build Your House
${SITE}
${f.text}`,
    html: `<p>Hi,</p>
<p>Thanks for subscribing to Build Your House. Here's what to expect: an occasional email when there's something genuinely useful for an owner-builder — new guides, tools, or hard-won lessons. No filler, no daily drip.</p>
<p>Start with these: <a href="${SITE}/binder-sample.pdf"><strong>19 real sample pages from the Owner-Builder Job Site Binder</strong></a> — the full foundation checklist and the complete span tables, free.</p>
<p>And if you're just getting started, this is the page I'd read first: <a href="${SITE}/start-here">the owner-builder roadmap</a>.</p>
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

// ---------------------------------------------------------------- estimate

const CALC_SLUG_RE = /^[a-z0-9-]{2,40}$/;
const ESTIMATE_MAX_PER_HOUR = 5;
// Per-isolate rate limit — resets on isolate recycle, which is fine: the
// goal is stopping dumb loops, not determined adversaries (the payload is
// fully sanitized regardless).
const estimateHits = new Map(); // ip -> [timestamps]

function estimateRateLimited(ip) {
  const now = Date.now();
  const hourAgo = now - 60 * 60 * 1000;
  const hits = (estimateHits.get(ip) || []).filter((t) => t > hourAgo);
  if (hits.length >= ESTIMATE_MAX_PER_HOUR) return true;
  hits.push(now);
  estimateHits.set(ip, hits);
  return false;
}

function escapeHtml(s) {
  return s
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;');
}

/** Cap length, collapse whitespace, and strip anything URL-shaped. */
function cleanText(value, max) {
  if (typeof value !== 'string') return '';
  return value
    .replace(/https?:\/\/\S+/gi, '')
    .replace(/www\.\S+/gi, '')
    .replace(/\s+/g, ' ')
    .trim()
    .slice(0, max);
}

function cleanRows(raw, maxRows) {
  if (!Array.isArray(raw)) return [];
  return raw.slice(0, maxRows).map((r) => ({
    label: cleanText(r?.label, 60),
    value: cleanText(r?.value, 140),
  })).filter((r) => r.label && r.value);
}

function estimateEmail(unsubUrl, d) {
  const f = emailFooter(unsubUrl);
  const calcUrl = `${SITE}/calculators/${d.calculator}`;
  const inputsText = d.inputs.map((r) => `  ${r.label}: ${r.value}`).join('\n');
  const linesText = d.lines.map((r) => `  ${r.label}: ${r.value}`).join('\n');
  const rowsHtml = (rows) =>
    rows
      .map(
        (r) =>
          `<tr><td style="padding:4px 16px 4px 0;color:#56503f;white-space:nowrap">${escapeHtml(r.label)}</td><td style="padding:4px 0;color:#232019"><strong>${escapeHtml(r.value)}</strong></td></tr>`
      )
      .join('');
  return {
    subject: `Your ${d.calculatorName.toLowerCase()} takeoff — ${d.hero}`,
    text: `Hi,

Here's the takeoff you ran at build-your-house.com — your numbers, kept where you can find them.

${d.calculatorName}: ${d.hero}

Your inputs:
${inputsText}

Materials:
${linesText}

Estimated material cost: ${d.cost}

Estimate only — quantities come from the assumptions shown on the calculator page. Order after a takeoff from your actual plans, and get local prices.

Re-run it any time: ${calcUrl}

When you start ordering, the Job Site Binder's materials section is built for exactly this — takeoffs, quotes, and delivery logs on paper that survives the truck: ${SITE}/shop

Questions about your build? Just reply — I read these.

Seth
Build Your House
${SITE}
${f.text}`,
    html: `<p>Hi,</p>
<p>Here's the takeoff you ran at <a href="${calcUrl}">build-your-house.com</a> — your numbers, kept where you can find them.</p>
<p style="font-size:18px"><strong>${escapeHtml(d.calculatorName)}: ${escapeHtml(d.hero)}</strong></p>
<p style="margin-bottom:4px;color:#56503f;font-size:13px;text-transform:uppercase;letter-spacing:0.08em">Your inputs</p>
<table style="border-collapse:collapse;font-size:14px">${rowsHtml(d.inputs)}</table>
<p style="margin:16px 0 4px;color:#56503f;font-size:13px;text-transform:uppercase;letter-spacing:0.08em">Materials</p>
<table style="border-collapse:collapse;font-size:14px">${rowsHtml(d.lines)}</table>
<p style="margin-top:16px"><strong>Estimated material cost: ${escapeHtml(d.cost)}</strong></p>
<p style="color:#56503f;font-size:13px">Estimate only — quantities come from the assumptions shown on the calculator page. Order after a takeoff from your actual plans, and get local prices.</p>
<p><a href="${calcUrl}">Re-run it any time</a>.</p>
<p>When you start ordering, the <a href="${SITE}/shop">Job Site Binder</a>'s materials section is built for exactly this — takeoffs, quotes, and delivery logs on paper that survives the truck.</p>
<p>Questions about your build? Just reply — I read these.</p>
<p>Seth<br>Build Your House<br><a href="${SITE}">build-your-house.com</a></p>
${f.html}`,
  };
}

async function handleEstimate(request, env, ctx, origin) {
  let payload;
  try {
    payload = await request.json();
  } catch {
    return json({ error: 'invalid JSON' }, 400, origin);
  }

  // Honeypot filled → bot. Pretend success, store and send nothing.
  if (typeof payload.website === 'string' && payload.website.trim() !== '') {
    return json({ ok: true }, 200, origin);
  }

  const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
  if (estimateRateLimited(ip)) {
    return json({ error: 'too many requests' }, 429, origin);
  }

  const email = typeof payload.email === 'string' ? payload.email.trim().toLowerCase() : '';
  if (!email || email.length > MAX_EMAIL_LENGTH || !EMAIL_RE.test(email)) {
    return json({ error: 'invalid email' }, 400, origin);
  }

  const calculator = typeof payload.calculator === 'string' ? payload.calculator : '';
  if (!CALC_SLUG_RE.test(calculator)) {
    return json({ error: 'invalid calculator' }, 400, origin);
  }

  const data = {
    calculator,
    calculatorName: cleanText(payload.calculatorName, 60) || 'Calculator',
    hero: cleanText(payload.hero, 60),
    cost: cleanText(payload.cost, 60),
    inputs: cleanRows(payload.inputs, 12),
    lines: cleanRows(payload.lines, 12),
  };
  if (!data.hero || !data.lines.length) {
    return json({ error: 'invalid takeoff' }, 400, origin);
  }

  const source = cleanText(payload.sourcePath, 200) || `/calculators/${calculator}`;
  const now = new Date().toISOString();

  // Same storage semantics as /subscribe; the takeoff email replaces the
  // welcome for new signups (one email, not two).
  try {
    const existing = await env.DB.prepare(
      'SELECT unsubscribed_at FROM subscribers WHERE email = ?1'
    ).bind(email).first();
    if (!existing) {
      await env.DB.prepare(
        'INSERT INTO subscribers (email, source, created_at) VALUES (?1, ?2, ?3)'
      ).bind(email, source, now).run();
    } else if (existing.unsubscribed_at) {
      await env.DB.prepare(
        'UPDATE subscribers SET unsubscribed_at = NULL WHERE email = ?1'
      ).bind(email).run();
    }
  } catch (err) {
    console.error('estimate upsert failed:', err);
    return json({ error: 'storage error' }, 500, origin);
  }

  ctx.waitUntil((async () => {
    try {
      await upsertContact(env, email, false);
    } catch (err) {
      console.error('resend contact sync failed:', err);
    }
    try {
      const unsubUrl = await unsubscribeUrl(env, request.url, email);
      const msg = estimateEmail(unsubUrl, data);
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
    } catch (err) {
      console.error('estimate email failed:', err);
    }
  })());

  return json({ ok: true }, 200, origin);
}

// ---------------------------------------------------------------- financing leads

const LEAD_NOTIFY_TO = 'seth@build-your-house.com';
const LEAD_MAX_PER_HOUR = 3;
const leadHits = new Map(); // ip -> [timestamps]

function leadRateLimited(ip) {
  const now = Date.now();
  const hourAgo = now - 60 * 60 * 1000;
  const hits = (leadHits.get(ip) || []).filter((t) => t > hourAgo);
  if (hits.length >= LEAD_MAX_PER_HOUR) return true;
  hits.push(now);
  leadHits.set(ip, hits);
  return false;
}

const US_STATES = new Set([
  'AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN',
  'IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH',
  'NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT',
  'VT','VA','WA','WV','WI','WY',
]);
const LEAD_TIMELINES = new Set(['0-6', '6-12', '12-18', '18plus']);
const LEAD_CREDIT_BANDS = new Set(['740plus', '700-739', '660-699', 'below-660', 'unsure']);
const LEAD_LAND_STATUS = new Set(['own', 'under-contract', 'looking']);
const LEAD_BUDGET_BANDS = new Set(['under-200k', '200-400k', '400-700k', 'over-700k', '']);

const LEAD_LABELS = {
  timeline: { '0-6': '0–6 months', '6-12': '6–12 months', '12-18': '12–18 months', '18plus': '18+ months' },
  credit: { '740plus': '740+', '700-739': '700–739', '660-699': '660–699', 'below-660': 'Below 660', unsure: 'Not sure' },
  land: { own: 'Owns land', 'under-contract': 'Land under contract', looking: 'Still looking for land' },
  budget: { 'under-200k': 'Under $200K', '200-400k': '$200–400K', '400-700k': '$400–700K', 'over-700k': '$700K+' },
};

async function handleFinancingLead(request, env, ctx, origin) {
  let p;
  try {
    p = await request.json();
  } catch {
    return json({ error: 'invalid JSON' }, 400, origin);
  }

  // Honeypot filled → bot. Pretend success, store nothing.
  if (typeof p.website === 'string' && p.website.trim() !== '') {
    return json({ ok: true }, 200, origin);
  }

  const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
  if (leadRateLimited(ip)) {
    return json({ error: 'too many requests' }, 429, origin);
  }

  const email = typeof p.email === 'string' ? p.email.trim().toLowerCase() : '';
  const name = cleanText(p.name, 80);
  const phoneDigits = typeof p.phone === 'string' ? p.phone.replace(/[^\d]/g, '') : '';
  const state = typeof p.state === 'string' ? p.state.trim().toUpperCase() : '';
  const timeline = typeof p.timeline === 'string' ? p.timeline : '';
  const creditBand = typeof p.creditBand === 'string' ? p.creditBand : '';
  const landStatus = typeof p.landStatus === 'string' ? p.landStatus : '';
  const budgetBand = typeof p.budgetBand === 'string' ? p.budgetBand : '';
  const notes = cleanText(p.notes, 500);
  const source = cleanText(p.sourcePath, 200) || '/planning/financing';

  if (!email || email.length > MAX_EMAIL_LENGTH || !EMAIL_RE.test(email)) {
    return json({ error: 'invalid email' }, 400, origin);
  }
  if (!name) return json({ error: 'invalid name' }, 400, origin);
  if (phoneDigits.length < 10 || phoneDigits.length > 15) {
    return json({ error: 'invalid phone' }, 400, origin);
  }
  if (!US_STATES.has(state)) return json({ error: 'invalid state' }, 400, origin);
  if (!LEAD_TIMELINES.has(timeline)) return json({ error: 'invalid timeline' }, 400, origin);
  if (!LEAD_CREDIT_BANDS.has(creditBand)) return json({ error: 'invalid credit band' }, 400, origin);
  if (!LEAD_LAND_STATUS.has(landStatus)) return json({ error: 'invalid land status' }, 400, origin);
  if (!LEAD_BUDGET_BANDS.has(budgetBand)) return json({ error: 'invalid budget band' }, 400, origin);

  const now = new Date().toISOString();
  try {
    await env.DB.prepare(
      `INSERT INTO financing_leads
         (created_at, name, email, phone, state, timeline, credit_band, land_status, budget_band, notes, source)
       VALUES (?1, ?2, ?3, ?4, ?5, ?6, ?7, ?8, ?9, ?10, ?11)`
    ).bind(now, name, email, phoneDigits, state, timeline, creditBand, landStatus, budgetBand || null, notes || null, source).run();
  } catch (err) {
    console.error('financing lead insert failed:', err);
    return json({ error: 'storage error' }, 500, origin);
  }

  ctx.waitUntil((async () => {
    // Notify Seth — leads are actionable immediately, deal or no deal.
    try {
      const rows = [
        ['Name', name],
        ['Email', email],
        ['Phone', phoneDigits],
        ['State', state],
        ['Timeline', LEAD_LABELS.timeline[timeline]],
        ['Credit', LEAD_LABELS.credit[creditBand]],
        ['Land', LEAD_LABELS.land[landStatus]],
        ['Budget', budgetBand ? LEAD_LABELS.budget[budgetBand] : '—'],
        ['Notes', notes || '—'],
        ['Source', source],
      ];
      await resend(env, '/emails', {
        method: 'POST',
        body: {
          from: FROM,
          to: [LEAD_NOTIFY_TO],
          reply_to: email,
          subject: `Financing lead: ${state} · ${LEAD_LABELS.timeline[timeline]} · ${LEAD_LABELS.credit[creditBand]}`,
          text: rows.map(([k, v]) => `${k}: ${v}`).join('\n'),
          html: `<table style="border-collapse:collapse;font-size:14px">${rows
            .map(([k, v]) => `<tr><td style="padding:4px 16px 4px 0;color:#56503f">${escapeHtml(k)}</td><td style="padding:4px 0"><strong>${escapeHtml(String(v))}</strong></td></tr>`)
            .join('')}</table>
            <p style="color:#56503f;font-size:12px">Reply-to is the lead. financing_leads row created ${now}.</p>`,
        },
      });
    } catch (err) {
      console.error('lead notify failed:', err);
    }
    // Newsletter add (disclosed on the form). No welcome email — the form's
    // confirmation copy is the acknowledgment; first touch should be Seth's.
    try {
      const existing = await env.DB.prepare(
        'SELECT unsubscribed_at FROM subscribers WHERE email = ?1'
      ).bind(email).first();
      if (!existing) {
        await env.DB.prepare(
          'INSERT INTO subscribers (email, source, created_at) VALUES (?1, ?2, ?3)'
        ).bind(email, source, now).run();
      } else if (existing.unsubscribed_at) {
        await env.DB.prepare(
          'UPDATE subscribers SET unsubscribed_at = NULL WHERE email = ?1'
        ).bind(email).run();
      }
      await upsertContact(env, email, false);
    } catch (err) {
      console.error('lead subscriber sync failed:', err);
    }
  })());

  return json({ ok: true }, 200, origin);
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
  const quiet = payload.quiet === true;
  const purchased = payload.purchased === true;
  const allowInsert = payload.insert !== false;
  const now = new Date().toISOString();

  let isNew = false;
  let wasUnsubscribed = false;
  try {
    const existing = await env.DB.prepare(
      'SELECT unsubscribed_at FROM subscribers WHERE email = ?1'
    ).bind(email).first();
    if (!existing) {
      if (!allowInsert) {
        // Purchase without list consent from a non-subscriber: nothing to do.
        return json({ ok: true }, 200, origin);
      }
      isNew = true;
      await env.DB.prepare(
        'INSERT INTO subscribers (email, source, created_at, purchased_at) VALUES (?1, ?2, ?3, ?4)'
      ).bind(email, source, now, purchased ? now : null).run();
    } else {
      if (existing.unsubscribed_at && allowInsert) {
        wasUnsubscribed = true;
        await env.DB.prepare(
          'UPDATE subscribers SET unsubscribed_at = NULL WHERE email = ?1'
        ).bind(email).run();
      }
      if (purchased) {
        await env.DB.prepare(
          'UPDATE subscribers SET purchased_at = COALESCE(purchased_at, ?1) WHERE email = ?2'
        ).bind(now, email).run();
      }
    }
  } catch (err) {
    console.error('subscribe upsert failed:', err);
    return json({ error: 'storage error' }, 500, origin);
  }

  // Post-storage work never blocks the response (or the user's success state).
  ctx.waitUntil((async () => {
    if (allowInsert) {
      try {
        await upsertContact(env, email, false);
      } catch (err) {
        console.error('resend contact sync failed:', err);
      }
    }
    // Sample requests always deliver the PDF (even to an existing subscriber —
    // they asked for it). The welcome goes only to genuinely new signups.
    // `quiet` (purchase-driven syncs) sends nothing: the buyer already has a
    // fulfillment email in their inbox.
    if (!quiet && (source === '/shop-sample' || isNew || wasUnsubscribed)) {
      try {
        await sendOnboardEmail(env, request.url, email, source);
      } catch (err) {
        console.error('onboard email failed:', err);
      }
    }
  })());

  return json({ ok: true }, 200, origin);
}

// ---------------------------------------------------------------- drip sequence

const SEQUENCE_MIN_AGE_DAYS = 3;
// Never mail signups older than this on a step's first rollout — protects
// against blasting a backlog if a new step ships months from now.
const SEQUENCE_MAX_AGE_DAYS = 21;

function sequenceStepFor(sub) {
  const source = sub.source || '';
  if (source.startsWith('/purchase')) return null;
  if (source === '/shop-sample') return 'sample-d3';
  return 'planning-d3';
}

function sampleD3Email(unsubUrl) {
  const f = emailFooter(unsubUrl);
  const text = `Hi,

A few days ago you grabbed 19 sample pages from the Owner-Builder Job Site Binder. Honest question: did they earn a spot in your truck?

If they did, the full binder is the other 348 pages — every phase from foundation to punch list as working checklists and logs, plus editable Word contracts and auto-calculating Excel budget workbooks. $97, instant download:
${SITE}/shop

Rather skip the office-store printing run? The coil-bound printed edition ships to your door for $149, digital included:
${SITE}/shop

Either way — what are you building, and where are you in it? Reply and tell me. I read every one of these, and it shapes what I build next.

Seth
Build Your House
${SITE}
${f.text}`;
  const html = `<p>Hi,</p>
<p>A few days ago you grabbed 19 sample pages from the Owner-Builder Job Site Binder. Honest question: <strong>did they earn a spot in your truck?</strong></p>
<p>If they did, the full binder is the other 348 pages — every phase from foundation to punch list as working checklists and logs, plus editable Word contracts and auto-calculating Excel budget workbooks. $97, instant download: <a href="${SITE}/shop">build-your-house.com/shop</a>.</p>
<p>Rather skip the office-store printing run? The <a href="${SITE}/shop#printed">coil-bound printed edition</a> ships to your door for $149, digital included.</p>
<p>Either way — what are you building, and where are you in it? Reply and tell me. I read every one of these, and it shapes what I build next.</p>
<p>Seth<br>Build Your House<br><a href="${SITE}">build-your-house.com</a></p>
${f.html}`;
  return { subject: 'Did the sample pages earn a spot in your truck?', text, html };
}

function planningD3Email(unsubUrl, source) {
  const f = emailFooter(unsubUrl);
  const nc = (source || '').includes('north-carolina');
  const ncText = nc
    ? `

Since you found us through the North Carolina guide: the NC Permit Kit is those rules as working checklists — the owner exemption walkthrough, the application checklist, and the inspection sequence, with the statute citations printed on each page. $34:
${SITE}/shop/nc-permit-kit`
    : `

Your state's specifics are in the free state guides:
${SITE}/permitting/state-guides`;
  const ncHtml = nc
    ? `<p>Since you found us through the North Carolina guide: the <a href="${SITE}/shop/nc-permit-kit"><strong>NC Permit Kit</strong></a> is those rules as working checklists — the owner exemption walkthrough, the application checklist, and the inspection sequence, with the statute citations printed on each page. $34.</p>`
    : `<p>Your state's specifics are in the free <a href="${SITE}/permitting/state-guides">state guides</a>.</p>`;

  const text = `Hi,

Three permit mistakes that cost owner-builders real money — all three avoidable for the price of doing things in the right order:

1. Applying for the building permit before the approvals that gate it. Septic and well sign-offs often have to exist BEFORE the building department will issue — in some states that's statute, not county habit. Find out what your permit is waiting on before you file.

2. Treating pre-permit designations as afterthoughts. Some states require things like a designated lien agent before you first contract with anyone — the fee is small, but fixing a missed designation mid-build is not.

3. Scheduling inspections by the calendar instead of the sequence. One failed inspection cascades: trades idle, reinspection queues, concrete trucks rescheduled. Walk each checklist with a pen before you call the inspector.${ncText}

Which county are you building in? Permitting is local, and the quirks are where the money hides — reply and tell me yours, and I'll point you at what I know.

Seth
Build Your House
${SITE}
${f.text}`;
  const html = `<p>Hi,</p>
<p>Three permit mistakes that cost owner-builders real money — all three avoidable for the price of doing things in the right order:</p>
<p><strong>1. Applying for the building permit before the approvals that gate it.</strong> Septic and well sign-offs often have to exist <em>before</em> the building department will issue — in some states that's statute, not county habit. Find out what your permit is waiting on before you file.</p>
<p><strong>2. Treating pre-permit designations as afterthoughts.</strong> Some states require things like a designated lien agent before you first contract with anyone — the fee is small, but fixing a missed designation mid-build is not.</p>
<p><strong>3. Scheduling inspections by the calendar instead of the sequence.</strong> One failed inspection cascades: trades idle, reinspection queues, concrete trucks rescheduled. Walk each checklist with a pen before you call the inspector.</p>
${ncHtml}
<p>Which county are you building in? Permitting is local, and the quirks are where the money hides — reply and tell me yours, and I'll point you at what I know.</p>
<p>Seth<br>Build Your House<br><a href="${SITE}">build-your-house.com</a></p>
${f.html}`;
  return { subject: 'Three permit mistakes that cost owner-builders real money', text, html };
}

/**
 * Daily owner digest: last-24h list activity (signups, drip sends,
 * unsubscribes, sequence exits via purchase). Sends nothing on quiet days.
 * The 24h window tiles against the daily cron; second-level jitter at the
 * edges is acceptable for a human FYI email.
 */
async function runDigest(env) {
  const since = new Date(Date.now() - 24 * 3600 * 1000).toISOString();

  const [signups, sends, unsubs, purchases] = await Promise.all([
    env.DB.prepare(
      'SELECT email, source, created_at FROM subscribers WHERE created_at > ?1 ORDER BY created_at'
    ).bind(since).all(),
    env.DB.prepare(
      'SELECT email, step, sent_at FROM sequence_sends WHERE sent_at > ?1 ORDER BY sent_at'
    ).bind(since).all(),
    env.DB.prepare(
      'SELECT email, unsubscribed_at FROM subscribers WHERE unsubscribed_at > ?1'
    ).bind(since).all(),
    env.DB.prepare(
      'SELECT email, purchased_at FROM subscribers WHERE purchased_at > ?1'
    ).bind(since).all(),
  ]);

  const nSign = signups.results.length;
  const nSend = sends.results.length;
  const nUnsub = unsubs.results.length;
  const nBuy = purchases.results.length;
  if (nSign + nSend + nUnsub + nBuy === 0) {
    return { sent: false, reason: 'no activity in the last 24h' };
  }

  const lines = [];
  if (nSign) {
    lines.push(`NEW SIGNUPS (${nSign})`);
    for (const r of signups.results) {
      lines.push(`  ${r.email}  ·  ${r.source || '(no source)'}  ·  ${r.created_at.slice(0, 16)}Z`);
    }
    lines.push('');
  }
  if (nSend) {
    lines.push(`DRIP EMAILS SENT (${nSend})`);
    for (const r of sends.results) {
      lines.push(`  ${r.email}  ·  ${r.step}  ·  ${r.sent_at.slice(0, 16)}Z`);
    }
    lines.push('');
  }
  if (nBuy) {
    lines.push(`LEFT THE SEQUENCE AFTER PURCHASING (${nBuy})`);
    for (const r of purchases.results) {
      lines.push(`  ${r.email}`);
    }
    lines.push('');
  }
  if (nUnsub) {
    lines.push(`UNSUBSCRIBED (${nUnsub})`);
    for (const r of unsubs.results) {
      lines.push(`  ${r.email}`);
    }
    lines.push('');
  }
  lines.push(`Full list: admin API /admin/api/subscribers · replies to drip emails land at ${REPLY_TO}`);

  const summaryBits = [];
  if (nSign) summaryBits.push(`${nSign} signup${nSign > 1 ? 's' : ''}`);
  if (nSend) summaryBits.push(`${nSend} drip send${nSend > 1 ? 's' : ''}`);
  if (nBuy) summaryBits.push(`${nBuy} purchase exit${nBuy > 1 ? 's' : ''}`);
  if (nUnsub) summaryBits.push(`${nUnsub} unsubscribe${nUnsub > 1 ? 's' : ''}`);

  const text = lines.join('\n');
  await resend(env, '/emails', {
    method: 'POST',
    body: {
      from: FROM,
      to: [REPLY_TO],
      subject: `List digest — ${summaryBits.join(', ')}`,
      text,
      html: `<pre style="font-family:monospace;font-size:13px">${text
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')}</pre>`,
    },
  });
  return { sent: true, signups: nSign, sends: nSend, purchases: nBuy, unsubscribes: nUnsub };
}

/** One drip pass: idempotent, safe to run from cron or the admin endpoint. */
async function runSequence(env, workerOrigin) {
  const now = Date.now();
  const minCutoff = new Date(now - SEQUENCE_MIN_AGE_DAYS * 86400 * 1000).toISOString();
  const maxCutoff = new Date(now - SEQUENCE_MAX_AGE_DAYS * 86400 * 1000).toISOString();

  const { results } = await env.DB.prepare(
    `SELECT email, source FROM subscribers
     WHERE unsubscribed_at IS NULL AND purchased_at IS NULL
       AND created_at <= ?1 AND created_at > ?2`
  ).bind(minCutoff, maxCutoff).all();

  const report = { eligible: results.length, sent: [], skipped: 0, errors: [] };
  for (const sub of results) {
    const step = sequenceStepFor(sub);
    if (!step) {
      report.skipped++;
      continue;
    }
    const already = await env.DB.prepare(
      'SELECT 1 AS x FROM sequence_sends WHERE email = ?1 AND step = ?2'
    ).bind(sub.email, step).first();
    if (already) {
      report.skipped++;
      continue;
    }
    try {
      const unsubUrl = await unsubscribeUrl(env, workerOrigin, sub.email);
      const msg = step === 'sample-d3'
        ? sampleD3Email(unsubUrl)
        : planningD3Email(unsubUrl, sub.source);
      await resend(env, '/emails', {
        method: 'POST',
        body: {
          from: FROM,
          to: [sub.email],
          reply_to: REPLY_TO,
          subject: msg.subject,
          text: msg.text,
          html: msg.html,
        },
      });
      await env.DB.prepare(
        'INSERT INTO sequence_sends (email, step, sent_at) VALUES (?1, ?2, ?3)'
      ).bind(sub.email, step, new Date().toISOString()).run();
      report.sent.push({ email: sub.email, step });
    } catch (err) {
      console.error(`sequence send failed (${sub.email}, ${step}):`, err);
      report.errors.push({ email: sub.email, step, error: String(err.message || err) });
    }
  }
  return report;
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
    'SELECT email, source, created_at, unsubscribed_at, purchased_at FROM subscribers ORDER BY created_at DESC'
  ).all();

  if (url.searchParams.get('format') === 'csv') {
    const esc = (v) => (v == null ? '' : `"${String(v).replace(/"/g, '""')}"`);
    const csv = ['email,source,created_at,unsubscribed_at,purchased_at']
      .concat(results.map((r) => [r.email, r.source, r.created_at, r.unsubscribed_at, r.purchased_at].map(esc).join(',')))
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

  const sequence = {};
  try {
    const sends = await env.DB.prepare(
      'SELECT step, COUNT(*) AS n FROM sequence_sends GROUP BY step'
    ).all();
    for (const row of sends.results) sequence[row.step] = row.n;
  } catch (err) {
    console.error('sequence summary failed:', err);
  }

  return json(
    {
      total: results.length,
      active,
      unsubscribed: results.length - active,
      bySource,
      sequence,
      subscribers: results,
    },
    200,
    origin
  );
}

async function handleAdminFinancingLeads(request, env, origin) {
  const url = new URL(request.url);
  const { results } = await env.DB.prepare(
    'SELECT * FROM financing_leads ORDER BY created_at DESC'
  ).all();

  if (url.searchParams.get('format') === 'csv') {
    const cols = ['id', 'created_at', 'name', 'email', 'phone', 'state', 'timeline', 'credit_band', 'land_status', 'budget_band', 'notes', 'source', 'status', 'sent_to'];
    const esc = (v) => (v == null ? '' : `"${String(v).replace(/"/g, '""')}"`);
    const csv = [cols.join(',')]
      .concat(results.map((r) => cols.map((c) => esc(r[c])).join(',')))
      .join('\n');
    return new Response(csv, {
      headers: {
        'Content-Type': 'text/csv',
        'Content-Disposition': 'attachment; filename="financing-leads.csv"',
        ...corsHeaders(origin),
      },
    });
  }

  const byState = {};
  for (const r of results) byState[r.state] = (byState[r.state] || 0) + 1;
  return json({ total: results.length, byState, leads: results }, 200, origin);
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
      if (request.method === 'POST' && url.pathname === '/estimate') {
        return await handleEstimate(request, env, ctx, origin);
      }
      if (request.method === 'POST' && url.pathname === '/financing-lead') {
        return await handleFinancingLead(request, env, ctx, origin);
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
      if (url.pathname === '/admin/api/financing-leads') {
        if (!(await isAuthorized(request, env))) {
          return json({ error: 'unauthorized' }, 401, origin);
        }
        return await handleAdminFinancingLeads(request, env, origin);
      }
      if (request.method === 'POST' && url.pathname === '/admin/api/run-sequence') {
        if (!(await isAuthorized(request, env))) {
          return json({ error: 'unauthorized' }, 401, origin);
        }
        const report = await runSequence(env, WORKER_ORIGIN);
        return json(report, 200, origin);
      }
      if (request.method === 'POST' && url.pathname === '/admin/api/run-digest') {
        if (!(await isAuthorized(request, env))) {
          return json({ error: 'unauthorized' }, 401, origin);
        }
        return json(await runDigest(env), 200, origin);
      }
      return json({ error: 'not found' }, 404, origin);
    } catch (err) {
      console.error('unhandled error:', err);
      return json({ error: 'internal error' }, 500, origin);
    }
  },

  /** Daily drip pass + owner digest — see wrangler.jsonc triggers. */
  async scheduled(event, env, ctx) {
    ctx.waitUntil(
      (async () => {
        // Sequence first so today's sends appear in today's digest.
        try {
          const r = await runSequence(env, WORKER_ORIGIN);
          console.log('sequence run:', JSON.stringify(r));
        } catch (err) {
          console.error('sequence run failed:', err);
        }
        try {
          const d = await runDigest(env);
          console.log('digest:', JSON.stringify(d));
        } catch (err) {
          console.error('digest failed:', err);
        }
      })()
    );
  },
};
