/**
 * Newsletter subscribe endpoint for build-your-house.com.
 *
 * POST /subscribe  { email, source?, website? }
 *   - `website` is a honeypot: real users never fill it, bots do.
 *   - Stores into D1 (subscribers table), idempotent on email.
 *
 * Export the list anytime with:
 *   wrangler d1 execute buildyourhouse-newsletter --remote \
 *     --command "SELECT * FROM subscribers ORDER BY created_at"
 */

const ALLOWED_ORIGINS = new Set([
  'https://build-your-house.com',
  'http://localhost:4000',
]);

const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const MAX_EMAIL_LENGTH = 254;

function corsHeaders(origin) {
  return {
    'Access-Control-Allow-Origin': ALLOWED_ORIGINS.has(origin) ? origin : 'https://build-your-house.com',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '86400',
  };
}

function json(body, status, origin) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { 'Content-Type': 'application/json', ...corsHeaders(origin) },
  });
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin');
    const url = new URL(request.url);

    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders(origin) });
    }

    if (request.method !== 'POST' || url.pathname !== '/subscribe') {
      return json({ error: 'not found' }, 404, origin);
    }

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

    try {
      await env.DB.prepare(
        'INSERT INTO subscribers (email, source, created_at) VALUES (?1, ?2, ?3) ON CONFLICT(email) DO NOTHING'
      )
        .bind(email, source, new Date().toISOString())
        .run();
    } catch (err) {
      console.error('subscribe insert failed:', err);
      return json({ error: 'storage error' }, 500, origin);
    }

    return json({ ok: true }, 200, origin);
  },
};
