/**
 * Plans attached: the $20 measured estimate on the cost-to-build page.
 *
 * The browser streams a PDF to POST /plan-read with the setup answers and the
 * buyer's email in headers; the Worker streams it on to StudTally's partner
 * API (never buffering it), records a plan_reads row keyed by a random
 * 128-bit token, creates the Stripe Checkout Session, and hands back the
 * checkout URL. Payment lands by webhook or by the page's verify call,
 * whichever is first; both call fulfillPaidSession, which tells StudTally the
 * read is paid (that queues the job) and emails "we're reading your plans".
 *
 * While the job runs, GET /plan-read/:token polls StudTally (the page every
 * 5 s, the cron sweep every 5 min for closed tabs). When StudTally reports the
 * set read, the geometry summary is stored on the row and the ready email
 * goes out; the page then renders the measured ledger from it. A set StudTally
 * cannot read is refunded here through Stripe, the row is marked, the buyer
 * gets the reason, and the owner gets an alert.
 *
 * The token is the only credential for a result, like a share link. The row
 * never stores plan bytes; the geometry outlives StudTally's 90-day purge.
 */

export const PLAN_READ_SKU = 'plan-read';

const ESTIMATOR_PATH = '/calculators/material-estimator';
const MAX_PDF_BYTES = 100 * 1024 * 1024;
const MAX_PAGES = 40;
const CREATE_MAX_PER_HOUR = 5;
/** The page polls every 5 s; StudTally is asked at most this often per read. */
const POLL_MIN_INTERVAL_MS = 4000;
/** The cron sweep stops following a read after this long. */
const SWEEP_WINDOW_DAYS = 7;
const SWEEP_BATCH = 25;

const ANSWERS = {
  foundation: ['from_plan', 'slab', 'raised_crawl', 'basement'],
  floor_framing: ['from_plan', 'lumber', 'i_joist', 'floor_truss'],
  roof_framing: ['from_plan', 'stick', 'truss'],
};

const ACTIVE = new Set(['queued', 'reading']);

// ---------------------------------------------------------------- helpers

function nowIso() {
  return new Date().toISOString();
}

function newToken() {
  const b = new Uint8Array(16);
  crypto.getRandomValues(b);
  return [...b].map((x) => x.toString(16).padStart(2, '0')).join('');
}

function decodeHeader(value) {
  if (!value) return '';
  try {
    return decodeURIComponent(value);
  } catch {
    return value;
  }
}

function mb(bytes) {
  return (bytes / (1024 * 1024)).toFixed(bytes >= 10 * 1024 * 1024 ? 0 : 1);
}

function readUrl(deps, token) {
  return `${deps.SITE_ORIGIN}${ESTIMATOR_PATH}?read=${encodeURIComponent(token)}`;
}

function maskEmail(email) {
  if (!email) return '';
  const [user, domain] = email.split('@');
  if (!domain) return '***';
  return `${user.slice(0, 1)}***@${domain}`;
}

function parseJson(text, fallback) {
  if (!text) return fallback;
  try {
    return JSON.parse(text);
  } catch {
    return fallback;
  }
}

function studtallyBase(env) {
  return (env.STUDTALLY_API_URL || 'https://api.studtally.com').replace(/\/$/, '');
}

/** Minimal partner-API client. Throws an Error with .status and .detail on non-2xx. */
async function studtally(env, path, { method = 'GET', headers = {}, body, rawBody } = {}) {
  if (!env.STUDTALLY_PARTNER_KEY) {
    throw new Error('STUDTALLY_PARTNER_KEY is not set');
  }
  const res = await fetch(`${studtallyBase(env)}${path}`, {
    method,
    headers: {
      'X-Partner-Key': env.STUDTALLY_PARTNER_KEY,
      ...(body ? { 'Content-Type': 'application/json' } : {}),
      ...headers,
    },
    body: body ? JSON.stringify(body) : rawBody,
  });
  const text = await res.text();
  const data = parseJson(text, null);
  if (!res.ok) {
    const err = new Error(
      (data && typeof data.detail === 'string' && data.detail) || `StudTally ${method} ${path} → ${res.status}`
    );
    err.status = res.status;
    err.detail = data && typeof data.detail === 'string' ? data.detail : null;
    throw err;
  }
  return data;
}

async function getRow(env, token) {
  return env.DB.prepare('SELECT * FROM plan_reads WHERE token = ?1').bind(token).first();
}

async function rowBySession(env, sessionId) {
  return env.DB.prepare('SELECT * FROM plan_reads WHERE session_id = ?1').bind(sessionId).first();
}

/** The shape the page reads. Never the full email: the token is a share link. */
function publicView(row, extra = {}) {
  return {
    token: row.token,
    status: row.status,
    plan: { name: row.plan_name, pageCount: row.page_count },
    emailHint: maskEmail(row.email),
    progress: parseJson(row.progress_json, []),
    geometry: row.status === 'ready' ? parseJson(row.geometry_json, null) : null,
    reason: row.unsupported_reason || null,
    refunded: row.status === 'refunded',
    upgrade: row.upgrade_code ? { code: row.upgrade_code, expiresAt: row.upgrade_expires_at || null } : null,
    profile: row.profile_json || '',
    createdAt: row.created_at,
    readyAt: row.ready_at || null,
    ...extra,
  };
}

// ---------------------------------------------------------------- Stripe

let planReadPriceCache = null;

/** The active $20 price for the plan-read product, found by metadata.sku and cached per isolate. */
async function planReadPriceId(env, deps) {
  if (env.PLAN_READ_PRICE_ID) return env.PLAN_READ_PRICE_ID;
  if (planReadPriceCache) return planReadPriceCache;
  const products = await deps.stripe(env, '/products?limit=100&active=true');
  const product = products.data.find((p) => p.metadata?.sku === PLAN_READ_SKU);
  if (!product) {
    throw new Error('plan-read product is not provisioned in Stripe (run /admin/api/provision-products)');
  }
  const prices = await deps.stripe(env, `/prices?product=${product.id}&active=true&limit=20`);
  const price = prices.data.find((p) => p.currency === 'usd' && !p.recurring && p.unit_amount === deps.PLAN_READ_AMOUNT);
  if (!price) {
    throw new Error('plan-read price is not provisioned in Stripe (run /admin/api/provision-products)');
  }
  planReadPriceCache = price.id;
  return price.id;
}

async function createCheckoutSession(env, deps, { token, planId, email }) {
  const price = await planReadPriceId(env, deps);
  const url = readUrl(deps, token);
  const body = new URLSearchParams();
  body.set('mode', 'payment');
  body.set('line_items[0][price]', price);
  body.set('line_items[0][quantity]', '1');
  body.set('success_url', `${url}&session_id={CHECKOUT_SESSION_ID}`);
  body.set('cancel_url', `${url}&cancelled=1`);
  body.set('customer_email', email);
  body.set('client_reference_id', token);
  body.set('metadata[app]', 'buildyourhouse');
  body.set('metadata[sku]', PLAN_READ_SKU);
  body.set('metadata[token]', token);
  body.set('metadata[plan_id]', planId);
  body.set('payment_intent_data[description]', 'Measured whole-house estimate, build-your-house.com');
  body.set('payment_intent_data[metadata][app]', 'buildyourhouse');
  body.set('payment_intent_data[metadata][sku]', PLAN_READ_SKU);
  body.set('payment_intent_data[metadata][token]', token);
  body.set('allow_promotion_codes', 'true');
  body.set('consent_collection[promotions]', 'auto');
  return deps.stripe(env, '/checkout/sessions', { method: 'POST', body });
}

// ---------------------------------------------------------------- emails

function emailFooter() {
  return `Questions? Reply to this email.

Seth
Build Your House
https://build-your-house.com
`;
}

function htmlFooter() {
  return `<p>Questions? Reply to this email.</p>
<p>Seth<br>Build Your House<br><a href="https://build-your-house.com">build-your-house.com</a></p>`;
}

async function sendStartedEmail(env, deps, row) {
  const link = readUrl(deps, row.token);
  const text = `Hi,

Payment received. We're reading ${row.plan_name || 'your plan set'} now (${row.page_count || '?'} sheets).

What happens next:

1. StudTally reads the set: the footprint, every wall, window and door, the roof as drawn, and the rooms, with the sheet each number came from.

2. Your estimate page re-draws itself from those measurements. Usually within a few hours, often faster. Keep this link; it is your results page:
${link}

3. You get a second email when it is ready.

If the set turns out to be something we cannot read (a scan with no dimensions, a sketch, a set with only elevations), the $20 is refunded automatically and the email says why.

${emailFooter()}`;
  const html = `<p>Hi,</p>
<p>Payment received. We&rsquo;re reading <strong>${escapeHtml(row.plan_name || 'your plan set')}</strong> now (${row.page_count || '?'} sheets).</p>
<p><strong>What happens next:</strong></p>
<ol>
<li>StudTally reads the set: the footprint, every wall, window and door, the roof as drawn, and the rooms, with the sheet each number came from.</li>
<li>Your estimate page re-draws itself from those measurements. Usually within a few hours, often faster. Keep this link; it is your results page:<br><a href="${link}"><strong>Open your estimate</strong></a></li>
<li>You get a second email when it is ready.</li>
</ol>
<p>If the set turns out to be something we cannot read (a scan with no dimensions, a sketch, a set with only elevations), the $20 is refunded automatically and the email says why.</p>
${htmlFooter()}`;
  return deps.sendResendEmail(env, { to: row.email, subject: "We're reading your plans", text, html });
}

function upgradeParagraphText(row) {
  if (!row.upgrade_code) return '';
  return `
When you are ready to order framing, the $20 comes off StudTally's $79 framing list: every stud, plate, header, sheet and hanger, counted per wall and reviewed by a person. Framing only; the other thirteen phases stay estimates. Enter this code at StudTally's checkout: ${row.upgrade_code}
https://studtally.com/?utm_source=build-your-house.com&utm_medium=email&utm_campaign=plan-takeoff&utm_content=measured-estimate
`;
}

function upgradeParagraphHtml(row) {
  if (!row.upgrade_code) return '';
  return `<p>When you are ready to order framing, the $20 comes off StudTally&rsquo;s $79 framing list: every stud, plate, header, sheet and hanger, counted per wall and reviewed by a person. Framing only; the other thirteen phases stay estimates. Enter this code at <a href="https://studtally.com/?utm_source=build-your-house.com&amp;utm_medium=email&amp;utm_campaign=plan-takeoff&amp;utm_content=measured-estimate">StudTally&rsquo;s checkout</a>: <strong>${escapeHtml(row.upgrade_code)}</strong></p>`;
}

async function sendReadyEmail(env, deps, row) {
  const link = readUrl(deps, row.token);
  const g = parseJson(row.geometry_json, {}) || {};
  const facts = [];
  if (g.heated_sf) facts.push(`${Number(g.heated_sf).toLocaleString('en-US')} sq ft heated`);
  if (g.sheets_read && g.sheets_total) facts.push(`${g.sheets_read} of ${g.sheets_total} sheets read`);
  if (g.ext_wall_lf) facts.push(`${Math.round(Number(g.ext_wall_lf)).toLocaleString('en-US')} lf of exterior wall`);
  const factLine = facts.length ? `What was read: ${facts.join(', ')}.` : '';
  const text = `Hi,

Your measured estimate is ready. Every phase the plans could settle is now priced from your drawings, with the sheet it came from beside each number; the rest stays derived from the measured size and says so.
${factLine}

Open it here (the link is yours to keep and share):
${link}
${upgradeParagraphText(row)}
${emailFooter()}`;
  const html = `<p>Hi,</p>
<p>Your measured estimate is ready. Every phase the plans could settle is now priced from your drawings, with the sheet it came from beside each number; the rest stays derived from the measured size and says so.</p>
${factLine ? `<p>${escapeHtml(factLine)}</p>` : ''}
<p><a href="${link}"><strong>Open your measured estimate</strong></a><br>The link is yours to keep and share.</p>
${upgradeParagraphHtml(row)}
${htmlFooter()}`;
  return deps.sendResendEmail(env, { to: row.email, subject: 'Your measured estimate is ready', text, html });
}

async function sendUnsupportedEmail(env, deps, row) {
  const link = `${deps.SITE_ORIGIN}${ESTIMATOR_PATH}`;
  const refundLine = row.status === 'refunded'
    ? 'The $20 has been refunded to your card; it shows up in a few business days.'
    : 'Nothing was charged for the read.';
  const text = `Hi,

We could not read ${row.plan_name || 'your plan set'}. ${row.unsupported_reason || 'The set did not carry enough to measure from.'}

${refundLine}

The free estimate from your square footage is still here:
${link}

If you have a different version of the plans (the architect's PDF rather than a scan, or the full set with the floor plans and the roof plan), attach that one and we will read it.

${emailFooter()}`;
  const html = `<p>Hi,</p>
<p>We could not read <strong>${escapeHtml(row.plan_name || 'your plan set')}</strong>. ${escapeHtml(row.unsupported_reason || 'The set did not carry enough to measure from.')}</p>
<p>${refundLine}</p>
<p>The free estimate from your square footage is still here: <a href="${link}">${link}</a></p>
<p>If you have a different version of the plans (the architect&rsquo;s PDF rather than a scan, or the full set with the floor plans and the roof plan), attach that one and we will read it.</p>
${htmlFooter()}`;
  return deps.sendResendEmail(env, { to: row.email, subject: "We couldn't read your plans", text, html });
}

function escapeHtml(s) {
  return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// ---------------------------------------------------------------- create

export async function handleCreate(request, env, ctx, origin, deps) {
  const h = (name) => request.headers.get(name);
  const email = decodeHeader(h('X-Plan-Email')).trim().toLowerCase();
  if (!email || email.length > 254 || !deps.EMAIL_RE.test(email)) {
    return deps.json({ error: 'Enter a valid email address; the results link goes there.' }, 400, origin);
  }
  const ctype = (h('Content-Type') || '').split(';')[0].trim().toLowerCase();
  if (ctype !== 'application/pdf') {
    return deps.json({ error: 'Attach the plan set as a PDF.' }, 415, origin);
  }
  const length = Number(h('Content-Length'));
  if (!Number.isFinite(length) || length <= 0) {
    return deps.json({ error: 'The upload was empty.' }, 411, origin);
  }
  if (length > MAX_PDF_BYTES) {
    return deps.json({ error: `That file is ${mb(length)} MB. The limit is 100 MB.` }, 413, origin);
  }
  const answers = {};
  for (const [key, header] of [
    ['foundation', 'X-Plan-Foundation'],
    ['floor_framing', 'X-Plan-Floor'],
    ['roof_framing', 'X-Plan-Roof'],
  ]) {
    const v = (h(header) || 'from_plan').trim();
    if (!ANSWERS[key].includes(v)) {
      return deps.json({ error: `Unknown answer for ${key.replace('_', ' ')}.` }, 400, origin);
    }
    answers[key] = v;
  }
  const name = (decodeHeader(h('X-Plan-Name')) || 'Plan set').replace(/\.pdf$/i, '').trim().slice(0, 120) || 'Plan set';
  const profile = (h('X-Plan-Profile') || '').slice(0, 300);

  const ip = request.headers.get('CF-Connecting-IP') || 'unknown';
  const hourAgo = new Date(Date.now() - 60 * 60 * 1000).toISOString();
  try {
    const { count } = await env.DB.prepare(
      'SELECT COUNT(*) AS count FROM plan_reads WHERE ip = ?1 AND created_at > ?2'
    )
      .bind(ip, hourAgo)
      .first();
    if (count >= CREATE_MAX_PER_HOUR) {
      return deps.json({ error: 'Too many uploads from this connection. Try again in an hour.' }, 429, origin);
    }
  } catch (err) {
    console.error('plan_reads rate-limit query failed:', err);
  }

  const token = newToken();
  let plan;
  try {
    plan = await studtally(env, '/api/partner/plans', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/pdf',
        'Content-Length': String(length),
        'X-Plan-Name': encodeURIComponent(name),
        'X-Contact-Email': encodeURIComponent(email),
        'X-Partner-Ref': token,
        'X-Foundation': answers.foundation,
        'X-Floor-Framing': answers.floor_framing,
        'X-Roof-Framing': answers.roof_framing,
      },
      rawBody: request.body,
    });
  } catch (err) {
    if (err.status === 413 || err.status === 415 || err.status === 422) {
      return deps.json({ error: err.detail || err.message }, err.status, origin);
    }
    console.error('plan upload to StudTally failed:', err);
    return deps.json({ error: 'The plans could not be uploaded right now. Try again in a minute.' }, 502, origin);
  }
  if (plan.page_count > MAX_PAGES) {
    return deps.json({ error: `This set has ${plan.page_count} sheets; the limit is ${MAX_PAGES}.` }, 413, origin);
  }

  const now = nowIso();
  await env.DB.prepare(
    `INSERT INTO plan_reads (token, plan_id, email, status, plan_name, page_count, profile_json, answers_json, ip, created_at, updated_at)
     VALUES (?1, ?2, ?3, 'setup', ?4, ?5, ?6, ?7, ?8, ?9, ?9)`
  )
    .bind(token, plan.plan_id, email, name, plan.page_count, profile, JSON.stringify(answers), ip, now)
    .run();

  let session;
  try {
    session = await createCheckoutSession(env, deps, { token, planId: plan.plan_id, email });
  } catch (err) {
    console.error('plan-read checkout session failed:', err);
    return deps.json({ error: 'Checkout could not be started. Try again in a minute.' }, 502, origin);
  }
  await env.DB.prepare('UPDATE plan_reads SET session_id = ?2, updated_at = ?3 WHERE token = ?1')
    .bind(token, session.id, nowIso())
    .run();

  return deps.json({ token, checkout_url: session.url, page_count: plan.page_count }, 201, origin);
}

// ---------------------------------------------------------------- payment

/**
 * Mark a paid Checkout Session's read as started: tell StudTally (which
 * queues the job and mints the upgrade code), move the row to queued, and
 * email the buyer once. Idempotent: the conditional UPDATE decides who sends
 * the email when the webhook and the verify call race.
 */
export async function fulfillPaidSession(env, deps, session) {
  const token = session.metadata?.token || session.client_reference_id || null;
  let row = token ? await getRow(env, token) : null;
  if (!row) row = await rowBySession(env, session.id);
  if (!row) return { row: null, started: false };
  if (row.status !== 'setup') return { row, started: false };

  const intent =
    typeof session.payment_intent === 'string' ? session.payment_intent : session.payment_intent?.id || null;
  const paid = await studtally(env, `/api/partner/plans/${encodeURIComponent(row.plan_id)}/paid`, {
    method: 'POST',
    body: {
      stripe_session_id: session.id,
      stripe_payment_intent_id: intent,
      amount_cents: session.amount_total ?? 0,
      currency: session.currency || 'usd',
      email: session.customer_details?.email || row.email,
      receipt_url: null,
    },
  });

  const now = nowIso();
  const res = await env.DB.prepare(
    `UPDATE plan_reads
       SET status = 'queued', session_id = ?2, payment_intent_id = ?3, amount_cents = ?4,
           upgrade_code = ?5, upgrade_expires_at = ?6, paid_at = ?7, updated_at = ?7
     WHERE token = ?1 AND status = 'setup'`
  )
    .bind(
      row.token,
      session.id,
      intent,
      session.amount_total ?? 0,
      paid?.upgrade_code || null,
      paid?.upgrade_expires_at || null,
      now
    )
    .run();
  const started = (res.meta?.changes ?? 0) === 1;
  row = await getRow(env, row.token);
  if (started) {
    try {
      await sendStartedEmail(env, deps, row);
    } catch (err) {
      console.error('plan-read started email failed:', err);
    }
  }
  return { row, started };
}

// ---------------------------------------------------------------- progress

/** Ask StudTally where a read stands and move the row along. Returns the fresh row. */
export async function refreshRow(env, deps, row, { force = false } = {}) {
  if (!ACTIVE.has(row.status)) return row;
  if (!force && row.last_polled_at && Date.now() - Date.parse(row.last_polled_at) < POLL_MIN_INTERVAL_MS) {
    return row;
  }
  let plan;
  try {
    plan = await studtally(env, `/api/partner/plans/${encodeURIComponent(row.plan_id)}`);
  } catch (err) {
    console.error('plan-read status poll failed:', err);
    return row;
  }
  const now = nowIso();
  const progress = JSON.stringify(plan.progress || []);
  const st = plan.status;

  if (st === 'review' || st === 'complete') {
    let geometry;
    try {
      geometry = await studtally(env, `/api/partner/plans/${encodeURIComponent(row.plan_id)}/geometry`);
    } catch (err) {
      if (err.status === 409) {
        await env.DB.prepare(
          "UPDATE plan_reads SET progress_json = ?2, last_polled_at = ?3, updated_at = ?3 WHERE token = ?1"
        )
          .bind(row.token, progress, now)
          .run();
        return getRow(env, row.token);
      }
      console.error('plan-read geometry fetch failed:', err);
      return row;
    }
    const res = await env.DB.prepare(
      `UPDATE plan_reads
         SET status = 'ready', geometry_json = ?2, progress_json = ?3,
             upgrade_code = COALESCE(?4, upgrade_code), upgrade_expires_at = COALESCE(?5, upgrade_expires_at),
             ready_at = ?6, last_polled_at = ?6, updated_at = ?6
       WHERE token = ?1 AND status IN ('queued', 'reading')`
    )
      .bind(row.token, JSON.stringify(geometry), progress, plan.upgrade_code || null, plan.upgrade_expires_at || null, now)
      .run();
    const fresh = await getRow(env, row.token);
    if ((res.meta?.changes ?? 0) === 1) {
      try {
        await sendReadyEmail(env, deps, fresh);
      } catch (err) {
        console.error('plan-read ready email failed:', err);
      }
    }
    return fresh;
  }

  if (st === 'unsupported' || st === 'failed') {
    const reason =
      plan.unsupported_reason ||
      (st === 'failed'
        ? 'The read failed partway through the set.'
        : 'The set did not carry enough to measure from.');
    let refunded = false;
    let refundError = null;
    if (row.payment_intent_id) {
      try {
        const body = new URLSearchParams();
        body.set('payment_intent', row.payment_intent_id);
        body.set('reason', 'requested_by_customer');
        body.set('metadata[token]', row.token);
        body.set('metadata[app]', 'buildyourhouse');
        await deps.stripe(env, '/refunds', { method: 'POST', body });
        refunded = true;
      } catch (err) {
        refundError = err.message;
        console.error('plan-read refund failed:', err);
      }
    }
    const newStatus = refunded ? 'refunded' : 'unsupported';
    const res = await env.DB.prepare(
      `UPDATE plan_reads
         SET status = ?2, unsupported_reason = ?3, refund_error = ?4, progress_json = ?5,
             last_polled_at = ?6, updated_at = ?6
       WHERE token = ?1 AND status IN ('queued', 'reading')`
    )
      .bind(row.token, newStatus, reason, refundError, progress, now)
      .run();
    const fresh = await getRow(env, row.token);
    if ((res.meta?.changes ?? 0) === 1) {
      if (refunded) {
        try {
          await studtally(env, `/api/partner/plans/${encodeURIComponent(row.plan_id)}/refund-notice`, {
            method: 'POST',
            body: { stripe_payment_intent_id: row.payment_intent_id },
          });
        } catch (err) {
          console.error('plan-read refund notice failed:', err);
        }
      }
      try {
        await sendUnsupportedEmail(env, deps, fresh);
      } catch (err) {
        console.error('plan-read unsupported email failed:', err);
      }
      try {
        await deps.ownerEmail(env, {
          subject: `Plan read ${st}${refunded ? ', refunded' : refundError ? ', REFUND FAILED' : ', nothing to refund'}: ${fresh.plan_name}`,
          text: `A $20 plan read ended ${st}.

Token: ${fresh.token}
StudTally plan: ${fresh.plan_id}
Buyer: ${fresh.email}
Reason: ${reason}
Payment intent: ${fresh.payment_intent_id || '(none: comped or unpaid)'}
Refund: ${refunded ? 'issued through Stripe' : refundError ? `FAILED: ${refundError} (refund by hand in the Stripe dashboard)` : 'not needed'}
Results page: ${readUrl(deps, fresh.token)}
`,
        });
      } catch (err) {
        console.error('plan-read owner alert failed:', err);
      }
    }
    return fresh;
  }

  // queued | processing (| setup, if StudTally never queued it: keep waiting, the sweep retries)
  const newStatus = st === 'processing' ? 'reading' : 'queued';
  await env.DB.prepare(
    `UPDATE plan_reads SET status = ?2, progress_json = ?3, last_polled_at = ?4, updated_at = ?4
     WHERE token = ?1 AND status IN ('queued', 'reading')`
  )
    .bind(row.token, newStatus, progress, now)
    .run();
  return getRow(env, row.token);
}

export async function handleStatus(request, env, ctx, origin, deps, token) {
  let row = await getRow(env, token);
  if (!row) return deps.json({ error: 'not found' }, 404, origin);
  if (ACTIVE.has(row.status)) row = await refreshRow(env, deps, row);
  return deps.json(publicView(row), 200, origin);
}

export async function handleVerify(request, env, ctx, origin, deps, token) {
  let payload;
  try {
    payload = await request.json();
  } catch {
    return deps.json({ error: 'invalid JSON' }, 400, origin);
  }
  const sessionId = typeof payload.session_id === 'string' ? payload.session_id : '';
  if (!sessionId.startsWith('cs_')) return deps.json({ error: 'missing session_id' }, 400, origin);
  let row = await getRow(env, token);
  if (!row) return deps.json({ error: 'not found' }, 404, origin);

  let started = false;
  if (row.status === 'setup') {
    let session;
    try {
      session = await deps.stripe(env, `/checkout/sessions/${encodeURIComponent(sessionId)}`);
    } catch (err) {
      console.error('plan-read verify retrieve failed:', err);
      return deps.json({ error: 'Stripe could not be reached. The page will keep checking.' }, 502, origin);
    }
    const belongs = session.metadata?.token === token || session.client_reference_id === token;
    if (!belongs) return deps.json({ error: 'That checkout does not belong to this read.' }, 404, origin);
    if (deps.isPaidStatus(session.payment_status)) {
      ({ row, started } = await fulfillPaidSession(env, deps, session));
    }
  }
  if (ACTIVE.has(row.status)) row = await refreshRow(env, deps, row);
  return deps.json(publicView(row, { justPaid: started, amountCents: row.amount_cents ?? null }), 200, origin);
}

/** After a cancelled checkout: the open session's URL again, or a fresh session. */
export async function handleCheckout(request, env, ctx, origin, deps, token) {
  const row = await getRow(env, token);
  if (!row) return deps.json({ error: 'not found' }, 404, origin);
  if (row.status !== 'setup') return deps.json({ error: 'This read is already paid for.' }, 409, origin);
  if (row.session_id) {
    try {
      const cs = await deps.stripe(env, `/checkout/sessions/${encodeURIComponent(row.session_id)}`);
      if (cs.status === 'open' && cs.url) return deps.json({ checkout_url: cs.url }, 200, origin);
      if (deps.isPaidStatus(cs.payment_status)) {
        const { row: fresh } = await fulfillPaidSession(env, deps, cs);
        return deps.json(publicView(fresh), 200, origin);
      }
    } catch (err) {
      console.error('plan-read checkout lookup failed:', err);
    }
  }
  let session;
  try {
    session = await createCheckoutSession(env, deps, { token, planId: row.plan_id, email: row.email });
  } catch (err) {
    console.error('plan-read checkout session failed:', err);
    return deps.json({ error: 'Checkout could not be started. Try again in a minute.' }, 502, origin);
  }
  await env.DB.prepare('UPDATE plan_reads SET session_id = ?2, updated_at = ?3 WHERE token = ?1')
    .bind(token, session.id, nowIso())
    .run();
  return deps.json({ checkout_url: session.url }, 200, origin);
}

// ---------------------------------------------------------------- sweep and recovery

/** Cron: follow every active read so a closed tab still gets its email and its refund. */
export async function sweep(env, deps) {
  const since = new Date(Date.now() - SWEEP_WINDOW_DAYS * 24 * 60 * 60 * 1000).toISOString();
  const { results } = await env.DB.prepare(
    `SELECT * FROM plan_reads WHERE status IN ('queued', 'reading') AND created_at > ?1
     ORDER BY created_at ASC LIMIT ?2`
  )
    .bind(since, SWEEP_BATCH)
    .all();
  for (const row of results) {
    try {
      await refreshRow(env, deps, row, { force: true });
    } catch (err) {
      console.error(`plan-read sweep failed for ${row.token}:`, err);
    }
  }
  return results.length;
}

/** Recovery entries for an email: every read that got past checkout. */
export async function recoverRows(env, deps, email) {
  try {
    const { results } = await env.DB.prepare(
      `SELECT token, plan_name, status, created_at FROM plan_reads
       WHERE email = ?1 AND status <> 'setup' ORDER BY created_at DESC LIMIT 5`
    )
      .bind(email)
      .all();
    return results.map((r) => ({
      product: `Measured estimate: ${r.plan_name || 'plan set'}`,
      sku: PLAN_READ_SKU,
      kind: 'service',
      status: r.status,
      url: readUrl(deps, r.token),
      purchased: String(r.created_at).slice(0, 10),
    }));
  } catch (err) {
    console.error('plan_reads recovery query failed:', err);
    return [];
  }
}
