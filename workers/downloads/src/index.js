/**
 * Protected downloads + order admin for build-your-house.com.
 *
 * Public routes:
 *   GET  /download?session_id=cs_...  Verify the Stripe Checkout session is paid,
 *                                     stream the binder ZIP from R2, log delivery to D1.
 *   POST /recover { email, website }  Self-service recovery: look up a paid session by
 *                                     purchase email and return the success-page URL.
 *                                     Rate-limited per IP; `website` is a honeypot.
 *
 * Webhook:
 *   POST /stripe-webhook              Stripe checkout.session.completed → send the buyer
 *                                     their download link via Resend (dedupe on session_id).
 *                                     Non-2xx responses make Stripe retry for up to 3 days.
 *
 * Admin routes (Authorization: Bearer <ADMIN_KEY>):
 *   GET  /admin                       Dashboard UI (static HTML; data calls need the key).
 *   GET  /admin/api/orders            All checkout sessions + refund/dispute status +
 *                                     per-order download counts from D1.
 *   GET  /admin/api/diagnostics       Health: R2 object present, D1 reachable,
 *                                     payment-link redirect + promo-code config.
 *   POST /admin/api/fix-payment-link  Enable promotion codes and ensure the payment link
 *                                     redirects to /shop/success?session_id={CHECKOUT_SESSION_ID}.
 *
 * Secrets: STRIPE_SECRET_KEY, ADMIN_KEY, RESEND_API_KEY, STRIPE_WEBHOOK_SECRET
 * (set via `wrangler secret put`).
 * Bindings: DOWNLOADS_BUCKET (R2), DB (D1 — see schema.sql).
 */

import { ADMIN_HTML } from './admin.js';

const R2_OBJECT_KEY = 'owner-builder-job-site-binder.zip';
const SITE_ORIGIN = 'https://build-your-house.com';
const SUCCESS_PATH = '/shop/success';
const PAYMENT_LINK_URL = 'https://buy.stripe.com/5kQ28racn54z0ReeZ5fAc00';
const SESSION_TTL_MS = 24 * 60 * 60 * 1000;
const RECOVERY_MAX_PER_HOUR = 5;

// Per-isolate cache of sessions already verified as paid (avoids a Stripe
// round-trip on repeat downloads). Value: { at, email }.
const verifiedSessions = new Map();

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

/**
 * A session is fulfillable when Stripe collected payment OR nothing was owed —
 * a 100%-off promotion code produces payment_status 'no_payment_required'.
 */
function isPaidStatus(status) {
  return status === 'paid' || status === 'no_payment_required';
}

function successUrl(sessionId) {
  return `${SITE_ORIGIN}${SUCCESS_PATH}?session_id=${encodeURIComponent(sessionId)}`;
}

function corsHeaders(origin) {
  const headers = {
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
  };
  if (origin === SITE_ORIGIN || origin?.endsWith('.build-your-house.com') || origin === 'http://localhost:4000') {
    headers['Access-Control-Allow-Origin'] = origin;
  }
  return headers;
}

function json(body, status, origin) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', ...corsHeaders(origin) },
  });
}

/** Minimal Stripe REST client (no SDK — keeps the worker dependency-free). */
async function stripe(env, path, { method = 'GET', body } = {}) {
  const res = await fetch(`https://api.stripe.com/v1${path}`, {
    method,
    headers: {
      Authorization: `Bearer ${env.STRIPE_SECRET_KEY}`,
      ...(body ? { 'Content-Type': 'application/x-www-form-urlencoded' } : {}),
    },
    body,
  });
  const data = await res.json();
  if (!res.ok) {
    throw new Error(data?.error?.message || `Stripe API error ${res.status}`);
  }
  return data;
}

async function isAuthorized(request, env) {
  if (!env.ADMIN_KEY) return false;
  const key = (request.headers.get('Authorization') || '').replace(/^Bearer\s+/i, '');
  if (!key) return false;
  // Compare SHA-256 digests so the comparison is constant-time.
  const enc = new TextEncoder();
  const [a, b] = await Promise.all([
    crypto.subtle.digest('SHA-256', enc.encode(key)),
    crypto.subtle.digest('SHA-256', enc.encode(env.ADMIN_KEY)),
  ]);
  const ua = new Uint8Array(a);
  const ub = new Uint8Array(b);
  let diff = 0;
  for (let i = 0; i < ua.length; i++) diff |= ua[i] ^ ub[i];
  return diff === 0;
}

/** Returns { paid, email } for a checkout session, caching paid results. */
async function verifyStripeSession(sessionId, env) {
  const cached = verifiedSessions.get(sessionId);
  if (cached && Date.now() - cached.at < SESSION_TTL_MS) {
    return { paid: true, email: cached.email };
  }
  let session;
  try {
    session = await stripe(env, `/checkout/sessions/${encodeURIComponent(sessionId)}`);
  } catch {
    return { paid: false, email: null };
  }
  const paid = isPaidStatus(session.payment_status);
  const email = session.customer_details?.email || null;
  if (paid) {
    verifiedSessions.set(sessionId, { at: Date.now(), email });
  }
  return { paid, email };
}

async function logDownload(env, { sessionId, email, request }) {
  try {
    await env.DB.prepare(
      'INSERT INTO downloads (session_id, email, ip, user_agent, created_at) VALUES (?1, ?2, ?3, ?4, ?5)'
    )
      .bind(
        sessionId,
        email,
        request.headers.get('CF-Connecting-IP'),
        (request.headers.get('User-Agent') || '').slice(0, 500),
        new Date().toISOString()
      )
      .run();
  } catch (err) {
    // Never block a paying customer's download on logging problems.
    console.error('download log insert failed:', err);
  }
}

async function handleDownload(request, env, ctx, origin) {
  const sessionId = new URL(request.url).searchParams.get('session_id');
  if (!sessionId || !sessionId.startsWith('cs_')) {
    return new Response('Missing or invalid session_id', { status: 400 });
  }

  const { paid, email } = await verifyStripeSession(sessionId, env);
  if (!paid) {
    return new Response('Payment not verified. Please complete your purchase first.', { status: 403 });
  }

  const object = await env.DOWNLOADS_BUCKET.get(R2_OBJECT_KEY);
  if (!object) {
    console.error(`R2 object missing: ${R2_OBJECT_KEY}`);
    return new Response(
      'Download temporarily unavailable — please email us with your receipt and we will send the file directly.',
      { status: 500 }
    );
  }

  ctx.waitUntil(logDownload(env, { sessionId, email, request }));

  return new Response(object.body, {
    headers: {
      ...corsHeaders(origin),
      'Content-Type': 'application/zip',
      'Content-Disposition': `attachment; filename="${R2_OBJECT_KEY}"`,
      'Content-Length': object.size.toString(),
      'Cache-Control': 'no-store',
    },
  });
}

async function handleRecover(request, env, ctx, origin) {
  let payload;
  try {
    payload = await request.json();
  } catch {
    return json({ error: 'invalid JSON' }, 400, origin);
  }

  // Honeypot filled → bot. Pretend nothing was found.
  if (typeof payload.website === 'string' && payload.website.trim() !== '') {
    return json({ found: false }, 200, origin);
  }

  const email = typeof payload.email === 'string' ? payload.email.trim().toLowerCase() : '';
  if (!email || email.length > 254 || !EMAIL_RE.test(email)) {
    return json({ error: 'invalid email' }, 400, origin);
  }

  const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
  const hourAgo = new Date(Date.now() - 60 * 60 * 1000).toISOString();
  try {
    const { count } = await env.DB.prepare(
      'SELECT COUNT(*) AS count FROM recovery_requests WHERE ip = ?1 AND created_at > ?2'
    )
      .bind(ip, hourAgo)
      .first();
    if (count >= RECOVERY_MAX_PER_HOUR) {
      return json({ error: 'too many attempts — try again in an hour' }, 429, origin);
    }
  } catch (err) {
    console.error('recovery rate-limit query failed:', err);
  }

  let found = null;
  try {
    const params = new URLSearchParams({ limit: '100' });
    params.set('customer_details[email]', email);
    const res = await stripe(env, `/checkout/sessions?${params}`);
    found = res.data.find(
      (s) => isPaidStatus(s.payment_status) && s.customer_details?.email?.toLowerCase() === email
    );
  } catch (err) {
    console.error('recovery Stripe lookup failed:', err);
    return json({ error: 'lookup failed — please try again' }, 500, origin);
  }

  ctx.waitUntil(
    env.DB.prepare(
      'INSERT INTO recovery_requests (email, ip, found, created_at) VALUES (?1, ?2, ?3, ?4)'
    )
      .bind(email, ip, found ? 1 : 0, new Date().toISOString())
      .run()
      .catch((err) => console.error('recovery log insert failed:', err))
  );

  if (!found) {
    return json({ found: false }, 200, origin);
  }
  return json({ found: true, url: successUrl(found.id) }, 200, origin);
}

function timingSafeEqualStr(a, b) {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

/** Verify a Stripe-Signature header against the raw request body. */
async function verifyStripeSignature(header, body, secret, toleranceSec = 300) {
  const parsed = { t: null, v1: [] };
  for (const part of (header || '').split(',')) {
    const eq = part.indexOf('=');
    if (eq === -1) continue;
    const k = part.slice(0, eq).trim();
    const v = part.slice(eq + 1).trim();
    if (k === 't') parsed.t = v;
    else if (k === 'v1') parsed.v1.push(v);
  }
  if (!parsed.t || parsed.v1.length === 0) return false;
  const age = Math.abs(Date.now() / 1000 - Number(parsed.t));
  if (!Number.isFinite(age) || age > toleranceSec) return false;

  const enc = new TextEncoder();
  const key = await crypto.subtle.importKey(
    'raw',
    enc.encode(secret),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign']
  );
  const mac = await crypto.subtle.sign('HMAC', key, enc.encode(`${parsed.t}.${body}`));
  const expected = [...new Uint8Array(mac)].map((b) => b.toString(16).padStart(2, '0')).join('');
  return parsed.v1.some((sig) => timingSafeEqualStr(sig, expected));
}

/** Send the product-delivery email via Resend. Returns the Resend message id. */
async function sendFulfillmentEmail(env, { email, name, sessionId }) {
  const link = successUrl(sessionId);
  const first = (name || '').trim().split(/\s+/)[0] || '';
  const greeting = first ? `Hi ${first},` : 'Hi,';

  const text = `${greeting}

Thanks for buying the Owner-Builder Job Site Binder! This email is your product delivery — keep it so you can always get back to your files.

Your download page:
${link}

The ZIP contains 367 pages of printable PDFs, plus editable Word contracts and Excel budget spreadsheets. Open the "HOW TO USE THIS BINDER" guide first — it walks you through printing and assembling the binder.

Lose this email later? Recover your download anytime at https://build-your-house.com/shop/recover using this email address.

Any trouble at all, just reply and I'll help directly.

Seth
Build Your House
https://build-your-house.com
`;

  const html = `<p>${greeting}</p>
<p>Thanks for buying the Owner-Builder Job Site Binder! This email is your product delivery — keep it so you can always get back to your files.</p>
<p><a href="${link}"><strong>Open your download page</strong></a></p>
<p>The ZIP contains 367 pages of printable PDFs, plus editable Word contracts and Excel budget spreadsheets. Open the &ldquo;HOW TO USE THIS BINDER&rdquo; guide first — it walks you through printing and assembling the binder.</p>
<p>Lose this email later? Recover your download anytime at <a href="https://build-your-house.com/shop/recover">build-your-house.com/shop/recover</a> using this email address.</p>
<p>Any trouble at all, just reply and I&rsquo;ll help directly.</p>
<p>Seth<br>Build Your House<br><a href="https://build-your-house.com">build-your-house.com</a></p>`;

  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.RESEND_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      from: 'Seth at Build Your House <seth@build-your-house.com>',
      to: [email],
      reply_to: 'seth@build-your-house.com',
      subject: 'Your Owner-Builder Job Site Binder — download inside',
      text,
      html,
    }),
  });
  const data = await res.json();
  if (!res.ok) {
    throw new Error(data?.message || `Resend error ${res.status}`);
  }
  return data.id || null;
}

async function handleStripeWebhook(request, env) {
  const body = await request.text();
  const ok = await verifyStripeSignature(
    request.headers.get('Stripe-Signature'),
    body,
    env.STRIPE_WEBHOOK_SECRET
  );
  if (!ok) {
    return new Response('invalid signature', { status: 400 });
  }

  const event = JSON.parse(body);
  if (
    event.type !== 'checkout.session.completed' &&
    event.type !== 'checkout.session.async_payment_succeeded'
  ) {
    return new Response('ignored', { status: 200 });
  }

  const session = event.data.object;
  if (!isPaidStatus(session.payment_status)) {
    // Async payment methods complete later; the async_payment_succeeded event covers those.
    return new Response('not paid yet', { status: 200 });
  }
  const email = session.customer_details?.email;
  if (!email) {
    return new Response('no email on session', { status: 200 });
  }

  const existing = await env.DB.prepare('SELECT id FROM fulfillment_emails WHERE session_id = ?1')
    .bind(session.id)
    .first();
  if (existing) {
    return new Response('already sent', { status: 200 });
  }

  // Throwing here → 500 → Stripe retries the webhook, so a transient Resend
  // outage still results in the customer getting their email.
  const resendId = await sendFulfillmentEmail(env, {
    email,
    name: session.customer_details?.name,
    sessionId: session.id,
  });
  await env.DB.prepare(
    'INSERT INTO fulfillment_emails (session_id, email, resend_id, created_at) VALUES (?1, ?2, ?3, ?4)'
  )
    .bind(session.id, email, resendId, new Date().toISOString())
    .run();

  return new Response('sent', { status: 200 });
}

async function findPaymentLink(env) {
  const res = await stripe(env, '/payment_links?limit=100');
  return res.data.find((l) => l.url === PAYMENT_LINK_URL) || null;
}

function paymentLinkReport(link) {
  if (!link) return { found: false };
  const redirect = link.after_completion?.redirect?.url || null;
  return {
    found: true,
    id: link.id,
    active: link.active,
    allow_promotion_codes: link.allow_promotion_codes,
    after_completion_type: link.after_completion?.type || null,
    redirect_url: redirect,
    redirect_ok:
      !!redirect &&
      redirect.startsWith(`${SITE_ORIGIN}${SUCCESS_PATH}`) &&
      redirect.includes('{CHECKOUT_SESSION_ID}'),
  };
}

async function handleDiagnostics(env) {
  let linksError = null;
  let accountError = null;
  const [r2Head, d1Check, links, account] = await Promise.all([
    env.DOWNLOADS_BUCKET.head(R2_OBJECT_KEY).catch(() => null),
    env.DB.prepare('SELECT COUNT(*) AS count FROM downloads').first().catch(() => null),
    stripe(env, '/payment_links?limit=100').catch((err) => {
      linksError = err.message;
      return null;
    }),
    stripe(env, '/account').catch((err) => {
      accountError = err.message;
      return null;
    }),
  ]);

  const link = links?.data?.find((l) => l.url === PAYMENT_LINK_URL) || null;
  const report = paymentLinkReport(link);
  if (linksError) report.error = linksError;
  if (!report.found && links) {
    // Surface what the key CAN see so an account/link mismatch is obvious.
    report.expected_url = PAYMENT_LINK_URL;
    report.available = links.data.map((l) => ({ id: l.id, url: l.url, active: l.active }));
  }

  return json(
    {
      stripe_account: account
        ? { id: account.id, name: account.settings?.dashboard?.display_name || null }
        : { error: accountError || 'account lookup failed' },
      r2: r2Head
        ? { ok: true, key: R2_OBJECT_KEY, size: r2Head.size, uploaded: r2Head.uploaded }
        : { ok: false, key: R2_OBJECT_KEY, error: 'object missing from bucket' },
      d1: d1Check ? { ok: true, total_downloads: d1Check.count } : { ok: false },
      payment_link: report,
    },
    200
  );
}

// Checkout-page description for the Stripe Product behind the payment link.
// POST /admin/api/sync-product pushes it; edit here, redeploy, re-run.
const PRODUCT_DESCRIPTION =
  '367 pages of owner-builder contracts, checklists, forms, and trackers across ' +
  '8 sections — 57 print-ready PDFs plus editable Word contracts and Excel ' +
  'budget workbooks. Second Edition, revised 2026. Instant download.';

async function handleSyncProduct(env) {
  const link = await findPaymentLink(env);
  if (!link) {
    return json({ error: `no payment link matching ${PAYMENT_LINK_URL}` }, 404);
  }
  const items = await stripe(env, `/payment_links/${link.id}/line_items`);
  const productId = items?.data?.[0]?.price?.product;
  if (!productId) {
    return json({ error: 'no product on payment link line items' }, 404);
  }
  const before = await stripe(env, `/products/${productId}`);
  const body = new URLSearchParams();
  body.set('description', PRODUCT_DESCRIPTION);
  const after = await stripe(env, `/products/${productId}`, { method: 'POST', body });
  return json(
    { id: productId, name: after.name, before: before.description, after: after.description },
    200
  );
}

async function handleFixPaymentLink(env) {
  const link = await findPaymentLink(env);
  if (!link) {
    return json({ error: `no payment link matching ${PAYMENT_LINK_URL}` }, 404);
  }

  const before = paymentLinkReport(link);
  const body = new URLSearchParams();
  body.set('allow_promotion_codes', 'true');
  if (!before.redirect_ok) {
    body.set('after_completion[type]', 'redirect');
    body.set(
      'after_completion[redirect][url]',
      `${SITE_ORIGIN}${SUCCESS_PATH}?session_id={CHECKOUT_SESSION_ID}`
    );
  }

  const updated = await stripe(env, `/payment_links/${link.id}`, { method: 'POST', body });
  return json({ before, after: paymentLinkReport(updated) }, 200);
}

async function handleOrders(env) {
  // Pull every checkout session (paid and abandoned), newest first.
  const sessions = [];
  let startingAfter = null;
  for (let page = 0; page < 5; page++) {
    const params = new URLSearchParams({ limit: '100' });
    params.append('expand[]', 'data.payment_intent.latest_charge');
    if (startingAfter) params.set('starting_after', startingAfter);
    const res = await stripe(env, `/checkout/sessions?${params}`);
    sessions.push(...res.data);
    if (!res.has_more || res.data.length === 0) break;
    startingAfter = res.data[res.data.length - 1].id;
  }

  // Per-session download + fulfillment-email stats from D1.
  const stats = new Map();
  const emails = new Map();
  try {
    const { results } = await env.DB.prepare(
      'SELECT session_id, COUNT(*) AS n, MAX(created_at) AS last FROM downloads GROUP BY session_id'
    ).all();
    for (const row of results) stats.set(row.session_id, row);
    const sent = await env.DB.prepare(
      'SELECT session_id, created_at FROM fulfillment_emails'
    ).all();
    for (const row of sent.results) emails.set(row.session_id, row.created_at);
  } catch (err) {
    console.error('download stats query failed:', err);
  }

  const orders = sessions.map((s) => {
    const charge = s.payment_intent?.latest_charge || null;
    const dl = stats.get(s.id);
    return {
      session_id: s.id,
      created: s.created,
      email: s.customer_details?.email || null,
      name: s.customer_details?.name || null,
      amount_total: s.amount_total,
      currency: s.currency,
      payment_status: s.payment_status,
      session_status: s.status,
      discount: s.total_details?.amount_discount || 0,
      refunded: charge?.refunded || false,
      amount_refunded: charge?.amount_refunded || 0,
      disputed: charge?.disputed || false,
      payment_intent_id:
        typeof s.payment_intent === 'string' ? s.payment_intent : s.payment_intent?.id || null,
      receipt_url: charge?.receipt_url || null,
      downloads: dl ? dl.n : 0,
      last_download: dl ? dl.last : null,
      emailed_at: emails.get(s.id) || null,
      success_url: successUrl(s.id),
      download_url: `https://buildyourhouse-downloads.azerothcorner.workers.dev/download?session_id=${encodeURIComponent(s.id)}`,
    };
  });

  return json({ orders }, 200);
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const origin = request.headers.get('Origin');

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders(origin) });
    }

    try {
      if (request.method === 'GET' && url.pathname === '/download') {
        return await handleDownload(request, env, ctx, origin);
      }

      if (request.method === 'POST' && url.pathname === '/recover') {
        return await handleRecover(request, env, ctx, origin);
      }

      if (request.method === 'POST' && url.pathname === '/stripe-webhook') {
        return await handleStripeWebhook(request, env);
      }

      if (request.method === 'GET' && url.pathname === '/admin') {
        return new Response(ADMIN_HTML, {
          headers: { 'Content-Type': 'text/html;charset=UTF-8', 'Cache-Control': 'no-store' },
        });
      }

      if (url.pathname.startsWith('/admin/api/')) {
        if (!(await isAuthorized(request, env))) {
          return json({ error: 'unauthorized' }, 401);
        }
        if (request.method === 'GET' && url.pathname === '/admin/api/orders') {
          return await handleOrders(env);
        }
        if (request.method === 'GET' && url.pathname === '/admin/api/diagnostics') {
          return await handleDiagnostics(env);
        }
        if (request.method === 'POST' && url.pathname === '/admin/api/fix-payment-link') {
          return await handleFixPaymentLink(env);
        }
        if (request.method === 'POST' && url.pathname === '/admin/api/sync-product') {
          return await handleSyncProduct(env);
        }
      }

      return new Response('Not Found', { status: 404 });
    } catch (err) {
      console.error('unhandled error:', err);
      return json({ error: 'internal error' }, 500, origin);
    }
  },
};
