/**
 * Protected downloads + order admin for build-your-house.com.
 *
 * Public routes (multi-SKU: see PRODUCTS registry below):
 *   GET  /download?session_id=cs_...  Verify the Stripe Checkout session is paid,
 *                                     resolve its SKU, stream that product's ZIP
 *                                     from R2, log delivery to D1.
 *   GET  /order-info?session_id=...   Session-gated product name/kind for the
 *                                     success page.
 *   POST /recover { email, website }  Self-service recovery: all paid sessions for
 *                                     an email, each with its product + URL.
 *                                     Rate-limited per IP; `website` is a honeypot.
 *   GET  /print-assets/<token>/interior.pdf
 *   GET  /print-assets/<token>/cover.pdf
 *                                     Token-gated print-ready PDFs. Lulu fetches the
 *                                     source files by URL when normalising a print job.
 *
 * Webhook:
 *   POST /stripe-webhook              Stripe checkout.session.completed → send the buyer
 *                                     their download link via Resend (dedupe on session_id).
 *                                     For the printed binder it also places the Lulu print
 *                                     job (dedupe on print_jobs.session_id).
 *                                     Non-2xx responses make Stripe retry for up to 3 days.
 *
 * Admin routes (Authorization: Bearer <ADMIN_KEY>):
 *   GET  /admin                       Dashboard UI (static HTML; data calls need the key).
 *   GET  /admin/api/orders            All checkout sessions + refund/dispute status +
 *                                     per-order download counts from D1.
 *   GET  /admin/api/diagnostics       Health: R2 objects present, D1 reachable,
 *                                     payment-link redirect + promo-code config.
 *   GET  /admin/api/print-jobs        D1 print jobs joined with live Lulu status/tracking.
 *   POST /admin/api/test-lulu-job     Print-pipeline pre-flight: Lulu auth + pod package +
 *                                     page count + source-file reachability, priced via
 *                                     cost calculation. Never creates a print job.
 *   POST /admin/api/fix-payment-link  Enable promotion codes and ensure the payment link
 *                                     redirects to /shop/success?session_id={CHECKOUT_SESSION_ID}.
 *
 * Secrets: STRIPE_SECRET_KEY, ADMIN_KEY, RESEND_API_KEY, STRIPE_WEBHOOK_SECRET,
 * PRINT_ASSET_TOKEN, LULU_CLIENT_KEY, LULU_CLIENT_SECRET (set via `wrangler secret put`).
 * Bindings: DOWNLOADS_BUCKET (R2), DB (D1 — see schema.sql).
 */

import { ADMIN_HTML } from './admin.js';

const SITE_ORIGIN = 'https://build-your-house.com';
const WORKER_ORIGIN = 'https://buildyourhouse-downloads.azerothcorner.workers.dev';
const SUCCESS_PATH = '/shop/success';
const SESSION_TTL_MS = 24 * 60 * 60 * 1000;
const RECOVERY_MAX_PER_HOUR = 5;

// ---------------------------------------------------------------- print-on-demand

const LULU_API = 'https://api.lulu.com';
const LULU_TOKEN_URL =
  'https://api.lulu.com/auth/realms/glasstree/protocol/openid-connect/token';

/** Letter, B&W standard, coil bound, 60# white stock, matte cover. */
const POD_PACKAGE_ID = '0850X1100BWSTDCO060UW444MXX';

/**
 * The print-ready artifacts in R2, built by
 * binder-pipeline/print-edition/build_print_edition.py.
 *
 * PRINT_PAGE_COUNT and the md5 sums describe the objects currently at these
 * keys. Rebuild the PDFs and all three must be updated together — Lulu verifies
 * source_md5sum and rejects the job on a mismatch. That failure is deliberate:
 * it is loud, it happens at job creation, and it beats printing stale bytes.
 */
const PRINT_ASSETS = {
  interior: { r2Key: 'print/interior.pdf', md5: '179f61220210fae5da4ad56dd994e889' },
  cover: { r2Key: 'print/cover.pdf', md5: '3757650d0b1f456a6729161b723d0330' },
};
const PRINT_PAGE_COUNT = 396;
// GROUND_HD: tracked home-delivery ground, $8.64 over MAIL at Aug 2026 rates —
// keeps the customer email's 7-10 business day promise honest and adds tracking.
const PRINT_SHIPPING_LEVEL = 'GROUND_HD';
const PRINT_CONTACT_EMAIL = 'seth@build-your-house.com';
// Lulu requires a phone number on every address; Stripe only collects one if the
// payment link asks for it, so fall back to a number carriers will accept.
const PRINT_PHONE_FALLBACK = '9999999999';

/**
 * Product registry — one entry per SKU. `kind: 'download'` streams r2Key on
 * /download; `kind: 'ship'` is a physical product (printed binder) that ALSO
 * grants the digital download (r2Key) and triggers an owner notification with
 * the shipping address on purchase. Stripe objects are provisioned/aligned by
 * POST /admin/api/provision-products, which stamps metadata.sku on the
 * Product and Payment Link so sessions resolve back to a SKU.
 */
const PRODUCTS = {
  'job-site-binder': {
    sku: 'job-site-binder',
    kind: 'download',
    name: 'Owner-Builder Job Site Binder System',
    amount: 9700,
    r2Key: 'owner-builder-job-site-binder.zip',
    // Pre-registry Stripe objects — seeded so legacy sessions resolve.
    stripeProductId: 'prod_U0FsQiF5sLoIJ9',
    paymentLinkUrl: 'https://buy.stripe.com/5kQ28racn54z0ReeZ5fAc00',
    description:
      '367 pages of owner-builder contracts, checklists, forms, and trackers across ' +
      '8 sections — 57 print-ready PDFs plus editable Word contracts and Excel ' +
      'budget workbooks. Second Edition, revised 2026. Instant download.',
    emailSubject: 'Your Owner-Builder Job Site Binder — download inside',
    emailBlurb:
      'The ZIP contains 367 pages of printable PDFs, plus editable Word contracts and ' +
      'Excel budget spreadsheets. Open the "HOW TO USE THIS BINDER" guide first — it ' +
      'walks you through printing and assembling the binder.',
  },
  'nc-permit-kit': {
    sku: 'nc-permit-kit',
    kind: 'download',
    name: 'North Carolina Owner-Builder Permit Kit',
    amount: 3400,
    r2Key: 'nc-permit-kit.zip',
    description:
      'North Carolina owner-builder permitting, start to finish: the GC-license ' +
      'exemption walkthrough, NC permit application checklist, inspection sequence, ' +
      'where-to-file directory, and forms index. Print-ready PDFs, instant download.',
    emailSubject: 'Your North Carolina Permit Kit — download inside',
    emailBlurb:
      'The ZIP contains the NC owner-builder exemption walkthrough, permit application ' +
      'checklist, inspection sequence, where-to-file directory, and forms index — ' +
      'print-ready PDFs with the statute citations on the page.',
  },
  'sub-hiring-pack': {
    sku: 'sub-hiring-pack',
    kind: 'download',
    name: 'Subcontractor Hiring Pack',
    amount: 2900,
    r2Key: 'sub-hiring-pack.zip',
    description:
      'Hire subs like a GC: interview scorecard, reference check script, the hiring ' +
      'walkthrough, plus the subcontractor agreement, change order form, lien waivers, ' +
      'and payment draw schedule — print-ready PDFs and editable Word versions.',
    emailSubject: 'Your Subcontractor Hiring Pack — download inside',
    emailBlurb:
      'The ZIP contains the interview scorecard, reference check script, and hiring ' +
      'walkthrough, plus the subcontractor agreement, change order form, lien waivers, ' +
      'and draw schedule — with editable Word versions of the contract documents.',
  },
  'printed-binder': {
    sku: 'printed-binder',
    kind: 'ship',
    name: 'Owner-Builder Job Site Binder — Printed & Shipped',
    amount: 14900,
    r2Key: 'owner-builder-job-site-binder.zip', // printed buyers get digital too
    description:
      'The complete 367-page Second Edition binder, professionally printed and ' +
      'coil-bound so it lies flat on the job site, shipped to your door — plus the ' +
      'full digital download immediately while it ships. US shipping included.',
    emailSubject: 'Order confirmed — your printed Job Site Binder',
    emailBlurb: null,
  },
};

const DEFAULT_SKU = 'job-site-binder';

function productForSku(sku) {
  return PRODUCTS[sku] || PRODUCTS[DEFAULT_SKU];
}

/** Map a (possibly expanded) Stripe product reference to a SKU. */
function skuFromStripeProduct(productRef) {
  if (!productRef) return null;
  if (typeof productRef === 'object') {
    if (productRef.metadata?.sku && PRODUCTS[productRef.metadata.sku]) {
      return productRef.metadata.sku;
    }
    productRef = productRef.id;
  }
  for (const def of Object.values(PRODUCTS)) {
    if (def.stripeProductId && def.stripeProductId === productRef) return def.sku;
  }
  return null;
}

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

// Per-isolate Lulu access token: { token, expires }. Client-credentials tokens
// last an hour, so this saves an auth round-trip on every print-job call.
let luluAuth = null;

async function luluAccessToken(env) {
  if (luluAuth && Date.now() < luluAuth.expires) return luluAuth.token;
  const body = new URLSearchParams();
  body.set('grant_type', 'client_credentials');
  body.set('client_id', env.LULU_CLIENT_KEY);
  body.set('client_secret', env.LULU_CLIENT_SECRET);
  const res = await fetch(LULU_TOKEN_URL, {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body,
  });
  const data = await res.json();
  if (!res.ok) {
    throw new Error(data?.error_description || data?.error || `Lulu auth error ${res.status}`);
  }
  // Renew a minute early so a token can never expire mid-request.
  luluAuth = { token: data.access_token, expires: Date.now() + (data.expires_in - 60) * 1000 };
  return luluAuth.token;
}

/** Minimal Lulu Print API client (no SDK — mirrors the Stripe helper above). */
async function lulu(env, path, { method = 'GET', body } = {}) {
  const token = await luluAccessToken(env);
  const res = await fetch(`${LULU_API}${path}`, {
    method,
    headers: {
      Authorization: `Bearer ${token}`,
      Accept: 'application/json',
      ...(body ? { 'Content-Type': 'application/json' } : {}),
    },
    body: body ? JSON.stringify(body) : undefined,
  });
  const text = await res.text();
  let data = null;
  try {
    data = text ? JSON.parse(text) : null;
  } catch {
    // Lulu fronts its API with Cloudflare, which serves HTML on some errors.
  }
  if (!res.ok) {
    throw new Error(`Lulu ${method} ${path} → ${res.status}: ${text.slice(0, 600)}`);
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

/** Returns { paid, email, sku, session } for a checkout session, caching paid results. */
async function verifyStripeSession(sessionId, env) {
  const cached = verifiedSessions.get(sessionId);
  if (cached && Date.now() - cached.at < SESSION_TTL_MS) {
    return { paid: true, email: cached.email, sku: cached.sku, session: null };
  }
  let session;
  try {
    session = await stripe(
      env,
      `/checkout/sessions/${encodeURIComponent(sessionId)}?expand[]=line_items.data.price.product`
    );
  } catch {
    return { paid: false, email: null, sku: null, session: null };
  }
  const paid = isPaidStatus(session.payment_status);
  const email = session.customer_details?.email || null;
  const sku =
    skuFromStripeProduct(session.line_items?.data?.[0]?.price?.product) || DEFAULT_SKU;
  if (paid) {
    verifiedSessions.set(sessionId, { at: Date.now(), email, sku });
  }
  return { paid, email, sku, session };
}

async function logDownload(env, { sessionId, email, sku, request }) {
  try {
    await env.DB.prepare(
      'INSERT INTO downloads (session_id, email, ip, user_agent, created_at, sku) VALUES (?1, ?2, ?3, ?4, ?5, ?6)'
    )
      .bind(
        sessionId,
        email,
        request.headers.get('CF-Connecting-IP'),
        (request.headers.get('User-Agent') || '').slice(0, 500),
        new Date().toISOString(),
        sku
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

  const { paid, email, sku } = await verifyStripeSession(sessionId, env);
  if (!paid) {
    return new Response('Payment not verified. Please complete your purchase first.', { status: 403 });
  }

  const product = productForSku(sku);
  const object = await env.DOWNLOADS_BUCKET.get(product.r2Key);
  if (!object) {
    console.error(`R2 object missing: ${product.r2Key} (sku ${product.sku})`);
    return new Response(
      'Download temporarily unavailable — please email us with your receipt and we will send the file directly.',
      { status: 500 }
    );
  }

  ctx.waitUntil(logDownload(env, { sessionId, email, sku: product.sku, request }));

  return new Response(object.body, {
    headers: {
      ...corsHeaders(origin),
      'Content-Type': 'application/zip',
      'Content-Disposition': `attachment; filename="${product.r2Key}"`,
      'Content-Length': object.size.toString(),
      'Cache-Control': 'no-store',
    },
  });
}

/** Public, session-gated order info for the success page (name/kind per SKU). */
async function handleOrderInfo(request, env, origin) {
  const sessionId = new URL(request.url).searchParams.get('session_id');
  if (!sessionId || !sessionId.startsWith('cs_')) {
    return json({ error: 'missing or invalid session_id' }, 400, origin);
  }
  const { paid, sku } = await verifyStripeSession(sessionId, env);
  if (!paid) {
    return json({ paid: false }, 200, origin);
  }
  const product = productForSku(sku);
  return json(
    {
      paid: true,
      product: { sku: product.sku, name: product.name, kind: product.kind },
    },
    200,
    origin
  );
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

  let paidSessions = [];
  try {
    const params = new URLSearchParams({ limit: '100' });
    params.set('customer_details[email]', email);
    const res = await stripe(env, `/checkout/sessions?${params}`);
    paidSessions = res.data.filter(
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
      .bind(email, ip, paidSessions.length ? 1 : 0, new Date().toISOString())
      .run()
      .catch((err) => console.error('recovery log insert failed:', err))
  );

  if (paidSessions.length === 0) {
    return json({ found: false }, 200, origin);
  }

  // Resolve each paid session to its product (one line-items call per session,
  // capped — a customer with several purchases gets one entry per product).
  const orders = [];
  for (const s of paidSessions.slice(0, 5)) {
    let sku = DEFAULT_SKU;
    try {
      const items = await stripe(
        env,
        `/checkout/sessions/${encodeURIComponent(s.id)}/line_items?expand[]=data.price.product`
      );
      sku = skuFromStripeProduct(items?.data?.[0]?.price?.product) || DEFAULT_SKU;
    } catch (err) {
      console.error('recovery line-items lookup failed:', err);
    }
    const product = productForSku(sku);
    orders.push({
      product: product.name,
      sku: product.sku,
      kind: product.kind,
      url: successUrl(s.id),
      purchased: new Date(s.created * 1000).toISOString().slice(0, 10),
    });
  }

  // `url` kept for backward compatibility with the current recover page.
  return json({ found: true, url: orders[0].url, orders }, 200, origin);
}

function timingSafeEqualStr(a, b) {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

function printAssetUrl(env, name) {
  return `${WORKER_ORIGIN}/print-assets/${env.PRINT_ASSET_TOKEN}/${name}.pdf`;
}

/**
 * Unguessable source files for Lulu, which fetches the interior and cover by URL
 * while normalising a print job (so they cannot be behind the admin key). The
 * shared secret sits in the path; anything else 404s, making the route
 * indistinguishable from one that was never registered.
 */
async function handlePrintAsset(env, token, name) {
  const asset = PRINT_ASSETS[name];
  if (!asset || !env.PRINT_ASSET_TOKEN || !timingSafeEqualStr(token, env.PRINT_ASSET_TOKEN)) {
    return new Response('Not Found', { status: 404 });
  }
  const object = await env.DOWNLOADS_BUCKET.get(asset.r2Key);
  if (!object) {
    console.error(`R2 print asset missing: ${asset.r2Key}`);
    return new Response('Not Found', { status: 404 });
  }
  return new Response(object.body, {
    headers: {
      'Content-Type': 'application/pdf',
      'Content-Length': object.size.toString(),
      'Content-Disposition': `inline; filename="${name}.pdf"`,
      'Cache-Control': 'no-store',
    },
  });
}

/** Map a Stripe Checkout session's shipping details onto Lulu's address shape. */
function luluShippingAddress(session) {
  const ship =
    session.shipping_details || session.collected_information?.shipping_details || null;
  const addr = ship?.address || {};
  return {
    name: ship?.name || session.customer_details?.name || '',
    street1: addr.line1 || '',
    ...(addr.line2 ? { street2: addr.line2 } : {}),
    city: addr.city || '',
    state_code: addr.state || '',
    postcode: addr.postal_code || '',
    country_code: addr.country || 'US',
    phone_number: session.customer_details?.phone || PRINT_PHONE_FALLBACK,
  };
}

/**
 * Persist a placed print job. The book is already ordered by the time this
 * runs, so a D1 failure must never surface as a Lulu failure — it is logged and
 * returned as a warning rather than thrown.
 */
async function recordPrintJob(env, sessionId, job) {
  try {
    await env.DB.prepare(
      'INSERT OR IGNORE INTO print_jobs (session_id, lulu_job_id, status, created_at) VALUES (?1, ?2, ?3, ?4)'
    )
      .bind(sessionId, String(job.id), job.status?.name || 'CREATED', new Date().toISOString())
      .run();
    return null;
  } catch (err) {
    console.error(`print_jobs insert failed (Lulu job ${job.id} IS placed):`, err);
    return `print_jobs row could not be written: ${err.message}`;
  }
}

/**
 * Place the Lulu print job for a paid session, at most once ever. Every
 * duplicate here is a real book on a real card, so there are two guards.
 *
 * print_jobs.session_id (the primary key) is written immediately after Lulu
 * accepts the job, so a Stripe webhook retry — which happens whenever any later
 * step in the handler throws — finds the row and returns. If that write is the
 * thing that failed, Lulu itself is the fallback: line items carry the session
 * id as external_id, so asking Lulu answers "have I already ordered this?"
 * even when our own bookkeeping lost the answer.
 */
async function ensureLuluPrintJob(env, { session }) {
  const row = await env.DB.prepare(
    'SELECT lulu_job_id, status, created_at FROM print_jobs WHERE session_id = ?1'
  )
    .bind(session.id)
    .first();
  if (row) return { job: null, existing: row };

  const prior = await lulu(env, `/print-jobs/?external_id=${encodeURIComponent(session.id)}`);
  if (prior?.count > 0) {
    const found = prior.results[0];
    await recordPrintJob(env, session.id, found);
    return {
      job: null,
      existing: { lulu_job_id: String(found.id), status: found.status?.name || null },
    };
  }

  const job = await lulu(env, '/print-jobs/', {
    method: 'POST',
    body: {
      contact_email: PRINT_CONTACT_EMAIL,
      external_id: session.id,
      shipping_level: PRINT_SHIPPING_LEVEL,
      shipping_address: luluShippingAddress(session),
      line_items: [
        {
          title: 'Owner-Builder Job Site Binder',
          quantity: 1,
          external_id: session.id,
          // Lulu reads the page count off the interior PDF itself; the field is
          // read-only on this endpoint (page_count is only an input to the cost
          // calculator). PRINT_PAGE_COUNT is what the file must contain.
          printable_normalization: {
            pod_package_id: POD_PACKAGE_ID,
            interior: {
              source_url: printAssetUrl(env, 'interior'),
              source_md5sum: PRINT_ASSETS.interior.md5,
            },
            cover: {
              source_url: printAssetUrl(env, 'cover'),
              source_md5sum: PRINT_ASSETS.cover.md5,
            },
          },
        },
      ],
    },
  });

  return { job, existing: null, warning: await recordPrintJob(env, session.id, job) };
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

async function sendResendEmail(env, { to, subject, text, html }) {
  const res = await fetch('https://api.resend.com/emails', {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${env.RESEND_API_KEY}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      from: 'Seth at Build Your House <seth@build-your-house.com>',
      to: [to],
      reply_to: 'seth@build-your-house.com',
      subject,
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

/** Send the product-delivery email via Resend. Returns the Resend message id. */
async function sendFulfillmentEmail(env, { email, name, sessionId, product }) {
  const link = successUrl(sessionId);
  const first = (name || '').trim().split(/\s+/)[0] || '';
  const greeting = first ? `Hi ${first},` : 'Hi,';

  if (product.kind === 'ship') {
    const text = `${greeting}

Thanks for ordering the printed Owner-Builder Job Site Binder! Your order is confirmed and heads to the printer next — expect it at your door in about 7-10 business days.

While it ships, the complete digital version is yours right now:
${link}

Lose this email later? Recover your download anytime at https://build-your-house.com/shop/recover using this email address.

Any trouble at all, just reply and I'll help directly.

Seth
Build Your House
https://build-your-house.com
`;
    const html = `<p>${greeting}</p>
<p>Thanks for ordering the printed Owner-Builder Job Site Binder! Your order is confirmed and heads to the printer next — expect it at your door in about 7&ndash;10 business days.</p>
<p>While it ships, the complete digital version is yours right now:</p>
<p><a href="${link}"><strong>Open your download page</strong></a></p>
<p>Lose this email later? Recover your download anytime at <a href="https://build-your-house.com/shop/recover">build-your-house.com/shop/recover</a> using this email address.</p>
<p>Any trouble at all, just reply and I&rsquo;ll help directly.</p>
<p>Seth<br>Build Your House<br><a href="https://build-your-house.com">build-your-house.com</a></p>`;
    return sendResendEmail(env, { to: email, subject: product.emailSubject, text, html });
  }

  const text = `${greeting}

Thanks for buying the ${product.name}! This email is your product delivery — keep it so you can always get back to your files.

Your download page:
${link}

${product.emailBlurb}

Lose this email later? Recover your download anytime at https://build-your-house.com/shop/recover using this email address.

Any trouble at all, just reply and I'll help directly.

Seth
Build Your House
https://build-your-house.com
`;

  const html = `<p>${greeting}</p>
<p>Thanks for buying the ${product.name}! This email is your product delivery — keep it so you can always get back to your files.</p>
<p><a href="${link}"><strong>Open your download page</strong></a></p>
<p>${product.emailBlurb}</p>
<p>Lose this email later? Recover your download anytime at <a href="https://build-your-house.com/shop/recover">build-your-house.com/shop/recover</a> using this email address.</p>
<p>Any trouble at all, just reply and I&rsquo;ll help directly.</p>
<p>Seth<br>Build Your House<br><a href="https://build-your-house.com">build-your-house.com</a></p>`;

  return sendResendEmail(env, { to: email, subject: product.emailSubject, text, html });
}

function shipToLines(session) {
  const ship =
    session.shipping_details || session.collected_information?.shipping_details || null;
  const addr = ship?.address || {};
  return [
    ship?.name || session.customer_details?.name || '(no name)',
    addr.line1,
    addr.line2,
    `${addr.city || ''}, ${addr.state || ''} ${addr.postal_code || ''}`,
    addr.country,
  ].filter(Boolean);
}

function ownerEmail(env, { subject, text }) {
  return sendResendEmail(env, {
    to: PRINT_CONTACT_EMAIL,
    subject,
    text,
    html: `<pre style="font-family:monospace">${text.replace(/</g, '&lt;')}</pre>`,
  });
}

/** Receipt for an automated print job: Lulu has it, nothing to do. */
async function sendPrintJobNotification(env, { session, product, job, warning }) {
  const text = `Printed binder order — Lulu job #${job.id} created. No action needed.

Product: ${product.name} ($${(session.amount_total / 100).toFixed(2)})
Customer: ${session.customer_details?.email || '(no email)'}
Session: ${session.id}
Lulu status: ${job.status?.name || 'CREATED'}
${warning ? `\nWARNING: ${warning}\nThe book IS ordered — this only affects /admin/api/print-jobs.\n` : ''}
SHIP TO:
${shipToLines(session).join('\n')}

Lulu prints and ships this automatically. Track it at https://www.lulu.com
(or GET /admin/api/print-jobs for live status and the tracking number once it
leaves the printer). The customer already has digital access via their
download page.
`;
  await ownerEmail(env, {
    subject: `Lulu job #${job.id} created — printed binder for ${
      session.customer_details?.name || session.customer_details?.email
    }`,
    text,
  });
}

/**
 * Fallback when Lulu refused the job. The order is paid and the customer has
 * been promised a book, so this is the manual runbook.
 */
async function sendShipNotification(env, { session, product, error }) {
  const ship =
    session.shipping_details || session.collected_information?.shipping_details || null;

  const text = `Printed binder order — ACTION NEEDED. The automated Lulu job failed.

Product: ${product.name} ($${(session.amount_total / 100).toFixed(2)})
Customer: ${session.customer_details?.email || '(no email)'}
Session: ${session.id}

LULU ERROR:
${error ? String(error.message || error).slice(0, 800) : '(none recorded)'}

SHIP TO:
${shipToLines(session).join('\n')}

RUNBOOK:
1. Retry from the Lulu dashboard (https://www.lulu.com): ${PRINT_PAGE_COUNT}-page
   coil-bound Letter B&W book, pod package ${POD_PACKAGE_ID}. The print-ready
   files are in R2 at ${PRINT_ASSETS.interior.r2Key} and ${PRINT_ASSETS.cover.r2Key}
   (rebuild with binder-pipeline/print-edition/build_print_edition.py).
2. Ship to the address above; keep the tracking number.
3. Reply to the customer's fulfillment email thread with tracking.
Customer already has digital access via their download page.
`;

  await ownerEmail(env, {
    subject: `ACTION: Lulu job failed, print & ship manually — ${
      ship?.name || session.customer_details?.email
    }`,
    text,
  });
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

  // The webhook payload has no line items — resolve the SKU with one retrieve.
  const { sku } = await verifyStripeSession(session.id, env);
  const product = productForSku(sku);

  // Throwing here → 500 → Stripe retries the webhook, so a transient Resend
  // outage still results in the customer getting their email.
  const resendId = await sendFulfillmentEmail(env, {
    email,
    name: session.customer_details?.name,
    sessionId: session.id,
    product,
  });

  if (product.kind === 'ship') {
    let job = null;
    let warning = null;
    let luluError = null;
    try {
      ({ job, warning } = await ensureLuluPrintJob(env, { session }));
    } catch (err) {
      luluError = err;
      console.error('Lulu print job creation failed:', err);
    }
    try {
      if (luluError) {
        await sendShipNotification(env, { session, product, error: luluError });
      } else if (job) {
        await sendPrintJobNotification(env, { session, product, job, warning });
      }
      // A null job with no error means a retry found the job already placed;
      // it was announced the first time round, so stay quiet.
    } catch (err) {
      // The customer email is the critical path; the owner notification also
      // lands via the admin orders view, so log rather than force a retry
      // (which would re-send the customer email).
      console.error('ship notification failed:', err);
    }
  }

  await env.DB.prepare(
    'INSERT INTO fulfillment_emails (session_id, email, resend_id, created_at) VALUES (?1, ?2, ?3, ?4)'
  )
    .bind(session.id, email, resendId, new Date().toISOString())
    .run();

  return new Response('sent', { status: 200 });
}

async function findPaymentLink(env) {
  const res = await stripe(env, '/payment_links?limit=100');
  return res.data.find((l) => l.url === PRODUCTS[DEFAULT_SKU].paymentLinkUrl) || null;
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
  // The print artifacts are not attached to a SKU but a missing one silently
  // breaks every $149 order, so they get the same presence check.
  const uniqueKeys = [
    ...new Set([
      ...Object.values(PRODUCTS).map((p) => p.r2Key).filter(Boolean),
      ...Object.values(PRINT_ASSETS).map((a) => a.r2Key),
    ]),
  ];
  const [d1Check, links, account, ...r2Heads] = await Promise.all([
    env.DB.prepare('SELECT COUNT(*) AS count FROM downloads').first().catch(() => null),
    stripe(env, '/payment_links?limit=100').catch((err) => {
      linksError = err.message;
      return null;
    }),
    stripe(env, '/account').catch((err) => {
      accountError = err.message;
      return null;
    }),
    ...uniqueKeys.map((k) => env.DOWNLOADS_BUCKET.head(k).catch(() => null)),
  ]);

  const r2 = uniqueKeys.map((key, i) => {
    const head = r2Heads[i];
    return head
      ? { ok: true, key, size: head.size, uploaded: head.uploaded }
      : { ok: false, key, error: 'object missing from bucket' };
  });

  const link = links?.data?.find((l) => l.url === PRODUCTS[DEFAULT_SKU].paymentLinkUrl) || null;
  const report = paymentLinkReport(link);
  if (linksError) report.error = linksError;

  // Per-SKU payment-link overview via metadata stamped by provision-products.
  const skuLinks = {};
  if (links) {
    for (const l of links.data) {
      if (l.metadata?.sku && PRODUCTS[l.metadata.sku]) {
        skuLinks[l.metadata.sku] = { id: l.id, url: l.url, active: l.active };
      }
    }
  }

  return json(
    {
      stripe_account: account
        ? { id: account.id, name: account.settings?.dashboard?.display_name || null }
        : { error: accountError || 'account lookup failed' },
      r2,
      d1: d1Check ? { ok: true, total_downloads: d1Check.count } : { ok: false },
      payment_link: report,
      products: Object.fromEntries(
        Object.values(PRODUCTS).map((p) => [
          p.sku,
          {
            kind: p.kind,
            amount: p.amount,
            r2_ok: p.r2Key ? r2.find((x) => x.key === p.r2Key)?.ok || false : null,
            payment_link: skuLinks[p.sku] || (p.paymentLinkUrl ? { url: p.paymentLinkUrl } : null),
          },
        ])
      ),
    },
    200
  );
}

/** D1 print jobs, each joined with its live status and tracking from Lulu. */
async function handlePrintJobs(env) {
  const { results } = await env.DB.prepare(
    'SELECT session_id, lulu_job_id, status, created_at FROM print_jobs ORDER BY created_at DESC LIMIT 50'
  ).all();

  const jobs = await Promise.all(
    results.map(async (row) => {
      try {
        const live = await lulu(env, `/print-jobs/${encodeURIComponent(row.lulu_job_id)}/`);
        const item = live.line_items?.[0] || {};
        return {
          ...row,
          lulu_status: live.status?.name || null,
          lulu_message: live.status?.message || null,
          total_cost: live.costs?.total_cost_incl_tax || null,
          tracking_id: item.tracking_id || null,
          tracking_urls: item.tracking_urls || [],
          estimated_shipping_dates: live.estimated_shipping_dates || null,
        };
      } catch (err) {
        return { ...row, lulu_status: null, error: err.message };
      }
    })
  );

  return json({ jobs }, 200);
}

/**
 * Pre-flight for the print pipeline. Proves, from inside the worker, that the
 * Lulu credentials work, that the pod package and page count price correctly,
 * and that Lulu will be able to fetch both source files from the URLs we hand
 * it — then prices the job with a cost calculation.
 *
 * This endpoint has no code path that creates a print job. A real job prints a
 * real book and charges a real card, so ordering one stays a deliberate act.
 */
async function handleTestLuluJob(request, env) {
  let payload = {};
  try {
    payload = await request.json();
  } catch {
    // Body is optional.
  }
  if (payload.dry === false) {
    return json(
      { error: 'this endpoint only runs cost calculations; it cannot create a print job' },
      400
    );
  }

  const address = payload.shipping_address || {
    name: 'Test Buyer',
    street1: '123 W Martin St',
    city: 'Raleigh',
    state_code: 'NC',
    postcode: '27601',
    country_code: 'US',
    phone_number: PRINT_PHONE_FALLBACK,
  };

  // Check the bytes Lulu will hash. Fetching our own public URL from in here is
  // not an option — Cloudflare rejects a Worker subrequest to its own hostname
  // with error 1042 — so verify R2's stored md5 against the sum we hand Lulu,
  // which is the same equality Lulu enforces when it downloads the file.
  const assets = {};
  for (const [name, asset] of Object.entries(PRINT_ASSETS)) {
    const head = await env.DOWNLOADS_BUCKET.head(asset.r2Key).catch(() => null);
    const stored = head?.checksums?.md5;
    const actual = stored
      ? [...new Uint8Array(stored)].map((b) => b.toString(16).padStart(2, '0')).join('')
      : null;
    assets[name] = {
      r2_key: asset.r2Key,
      present: !!head,
      size: head?.size ?? null,
      declared_md5: asset.md5,
      r2_md5: actual,
      md5_ok: actual === asset.md5,
      source_url: printAssetUrl(env, name),
    };
  }

  const cost = await lulu(env, '/print-job-cost-calculations/', {
    method: 'POST',
    body: {
      line_items: [
        { page_count: PRINT_PAGE_COUNT, pod_package_id: POD_PACKAGE_ID, quantity: 1 },
      ],
      shipping_address: address,
      shipping_option: PRINT_SHIPPING_LEVEL,
    },
  });

  const retail = PRODUCTS['printed-binder'].amount / 100;
  return json(
    {
      dry: true,
      note: 'cost calculation only — no print job was created',
      pod_package_id: POD_PACKAGE_ID,
      page_count: PRINT_PAGE_COUNT,
      shipping_level: PRINT_SHIPPING_LEVEL,
      assets,
      retail_price: retail,
      landed_cost: cost.total_cost_incl_tax,
      gross_margin: (retail - Number(cost.total_cost_incl_tax)).toFixed(2),
      cost,
    },
    200
  );
}

/** Sync the flagship binder Product's checkout description from the registry. */
async function handleSyncProduct(env) {
  const def = PRODUCTS[DEFAULT_SKU];
  const link = await findPaymentLink(env);
  if (!link) {
    return json({ error: `no payment link matching ${def.paymentLinkUrl}` }, 404);
  }
  const items = await stripe(env, `/payment_links/${link.id}/line_items`);
  const productId = items?.data?.[0]?.price?.product;
  if (!productId) {
    return json({ error: 'no product on payment link line items' }, 404);
  }
  const before = await stripe(env, `/products/${productId}`);
  const body = new URLSearchParams();
  body.set('description', def.description);
  const after = await stripe(env, `/products/${productId}`, { method: 'POST', body });
  return json(
    { id: productId, name: after.name, before: before.description, after: after.description },
    200
  );
}

/**
 * Idempotently create/align Stripe objects for every SKU in the registry:
 * Product (metadata.sku + description), Price (unit amount), Payment Link
 * (metadata.sku, promo codes allowed, success redirect, shipping collection
 * for ship SKUs). Safe to re-run; reports what exists vs. what was created.
 */
async function handleProvisionProducts(env) {
  const [linksRes, productsRes] = await Promise.all([
    stripe(env, '/payment_links?limit=100'),
    stripe(env, '/products?limit=100&active=true'),
  ]);
  const results = {};

  for (const def of Object.values(PRODUCTS)) {
    const out = { actions: [] };

    // ---- Product: by metadata.sku, seeded id, or create.
    let product =
      productsRes.data.find((p) => p.metadata?.sku === def.sku) ||
      (def.stripeProductId ? productsRes.data.find((p) => p.id === def.stripeProductId) : null);
    if (!product && def.stripeProductId) {
      product = await stripe(env, `/products/${def.stripeProductId}`).catch(() => null);
    }
    if (!product) {
      const body = new URLSearchParams();
      body.set('name', def.name);
      body.set('description', def.description);
      body.set('metadata[sku]', def.sku);
      product = await stripe(env, '/products', { method: 'POST', body });
      out.actions.push('created product');
    } else if (product.metadata?.sku !== def.sku) {
      const body = new URLSearchParams();
      body.set('metadata[sku]', def.sku);
      product = await stripe(env, `/products/${product.id}`, { method: 'POST', body });
      out.actions.push('stamped metadata.sku');
    }
    out.product_id = product.id;

    // ---- Price: an active recurring-free price at the right amount.
    const pricesRes = await stripe(env, `/prices?product=${product.id}&active=true&limit=100`);
    let price = pricesRes.data.find(
      (p) => p.unit_amount === def.amount && p.currency === 'usd' && !p.recurring
    );
    if (!price) {
      const body = new URLSearchParams();
      body.set('product', product.id);
      body.set('currency', 'usd');
      body.set('unit_amount', String(def.amount));
      price = await stripe(env, '/prices', { method: 'POST', body });
      out.actions.push('created price');
    }
    out.price_id = price.id;

    // ---- Payment link: by metadata.sku or the seeded URL, else create.
    let link =
      linksRes.data.find((l) => l.metadata?.sku === def.sku) ||
      (def.paymentLinkUrl ? linksRes.data.find((l) => l.url === def.paymentLinkUrl) : null);
    if (!link) {
      const body = new URLSearchParams();
      body.set('line_items[0][price]', price.id);
      body.set('line_items[0][quantity]', '1');
      body.set('allow_promotion_codes', 'true');
      body.set('metadata[sku]', def.sku);
      body.set('after_completion[type]', 'redirect');
      body.set(
        'after_completion[redirect][url]',
        `${SITE_ORIGIN}${SUCCESS_PATH}?session_id={CHECKOUT_SESSION_ID}`
      );
      if (def.kind === 'ship') {
        body.set('shipping_address_collection[allowed_countries][0]', 'US');
      }
      link = await stripe(env, '/payment_links', { method: 'POST', body });
      out.actions.push('created payment link');
    } else if (link.metadata?.sku !== def.sku) {
      const body = new URLSearchParams();
      body.set('metadata[sku]', def.sku);
      link = await stripe(env, `/payment_links/${link.id}`, { method: 'POST', body });
      out.actions.push('stamped link metadata.sku');
    }
    out.payment_link = link.url;
    out.link_active = link.active;
    if (out.actions.length === 0) out.actions.push('already provisioned');
    results[def.sku] = out;
  }

  return json({ results }, 200);
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
      download_url: `${WORKER_ORIGIN}/download?session_id=${encodeURIComponent(s.id)}`,
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

      if (request.method === 'GET' && url.pathname === '/order-info') {
        return await handleOrderInfo(request, env, origin);
      }

      if (request.method === 'POST' && url.pathname === '/recover') {
        return await handleRecover(request, env, ctx, origin);
      }

      const printAsset = url.pathname.match(/^\/print-assets\/([^/]+)\/(interior|cover)\.pdf$/);
      if (request.method === 'GET' && printAsset) {
        return await handlePrintAsset(env, printAsset[1], printAsset[2]);
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
        if (request.method === 'GET' && url.pathname === '/admin/api/print-jobs') {
          return await handlePrintJobs(env);
        }
        if (request.method === 'POST' && url.pathname === '/admin/api/test-lulu-job') {
          return await handleTestLuluJob(request, env);
        }
        if (request.method === 'POST' && url.pathname === '/admin/api/fix-payment-link') {
          return await handleFixPaymentLink(env);
        }
        if (request.method === 'POST' && url.pathname === '/admin/api/sync-product') {
          return await handleSyncProduct(env);
        }
        if (request.method === 'POST' && url.pathname === '/admin/api/provision-products') {
          return await handleProvisionProducts(env);
        }
      }

      return new Response('Not Found', { status: 404 });
    } catch (err) {
      console.error('unhandled error:', err);
      return json({ error: 'internal error' }, 500, origin);
    }
  },
};
