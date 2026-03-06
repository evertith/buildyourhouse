import { Env, AuthenticatedRequest } from '../index.ts';

function json(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}

export async function handleAccount(request: Request, env: Env, auth: AuthenticatedRequest, path: string): Promise<Response> {
  if (path === '/account' && request.method === 'GET') {
    return getAccount(env, auth);
  }

  if (path === '/account/usage' && request.method === 'GET') {
    return getUsage(env, auth);
  }

  if (path === '/account/subscribe' && request.method === 'POST') {
    return createCheckoutSession(request, env, auth);
  }

  if (path === '/account/portal' && request.method === 'POST') {
    return createPortalSession(env, auth);
  }

  return json({ error: 'Not Found' }, 404);
}

async function getAccount(env: Env, auth: AuthenticatedRequest): Promise<Response> {
  const user = await env.DB.prepare(
    'SELECT id, email, name, plan, subscription_status, queries_used_this_month, created_at FROM users WHERE id = ?'
  ).bind(auth.userId).first();

  if (!user) return json({ error: 'User not found' }, 404);

  return json({ user });
}

async function getUsage(env: Env, auth: AuthenticatedRequest): Promise<Response> {
  const user = await env.DB.prepare(
    'SELECT plan, subscription_status, queries_used_this_month, queries_reset_at FROM users WHERE id = ?'
  ).bind(auth.userId).first<{
    plan: string;
    subscription_status: string;
    queries_used_this_month: number;
    queries_reset_at: string;
  }>();

  if (!user) return json({ error: 'User not found' }, 404);

  const limits: Record<string, number> = { free: 5, starter: 50, pro: 200 };
  const limit = limits[user.plan] || limits.free;

  return json({
    plan: user.plan,
    subscription_status: user.subscription_status,
    queries_used: user.queries_used_this_month,
    queries_limit: limit,
    resets_at: user.queries_reset_at,
  });
}

async function createCheckoutSession(request: Request, env: Env, auth: AuthenticatedRequest): Promise<Response> {
  const body = await request.json() as { plan?: string };
  const plan = body.plan || 'starter';

  const priceIds: Record<string, string> = {
    starter: 'price_1T83lYK5ZC8FJBSWJevJJY0c',
    pro: 'price_1T83lIK5ZC8FJBSWir164tqI',
  };

  const priceId = priceIds[plan];
  if (!priceId) return json({ error: 'Invalid plan' }, 400);

  const user = await env.DB.prepare(
    'SELECT email, stripe_customer_id FROM users WHERE id = ?'
  ).bind(auth.userId).first<{ email: string; stripe_customer_id: string | null }>();

  if (!user) return json({ error: 'User not found' }, 404);

  // Create or reuse Stripe customer
  let customerId = user.stripe_customer_id;
  if (!customerId) {
    const customerRes = await fetch('https://api.stripe.com/v1/customers', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${env.STRIPE_SECRET_KEY}`,
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: `email=${encodeURIComponent(user.email)}&metadata[user_id]=${auth.userId}`,
    });
    const customer = await customerRes.json() as { id: string };
    customerId = customer.id;

    await env.DB.prepare(
      'UPDATE users SET stripe_customer_id = ? WHERE id = ?'
    ).bind(customerId, auth.userId).run();
  }

  // Create checkout session
  const params = new URLSearchParams({
    'customer': customerId,
    'mode': 'subscription',
    'line_items[0][price]': priceId,
    'line_items[0][quantity]': '1',
    'success_url': 'https://build-your-house.com/advisor/chat?subscribed=true',
    'cancel_url': 'https://build-your-house.com/advisor/account',
    'metadata[user_id]': auth.userId,
    'metadata[plan]': plan,
  });

  const sessionRes = await fetch('https://api.stripe.com/v1/checkout/sessions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${env.STRIPE_SECRET_KEY}`,
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: params.toString(),
  });

  const session = await sessionRes.json() as { url: string };
  return json({ url: session.url });
}

async function createPortalSession(env: Env, auth: AuthenticatedRequest): Promise<Response> {
  const user = await env.DB.prepare(
    'SELECT stripe_customer_id FROM users WHERE id = ?'
  ).bind(auth.userId).first<{ stripe_customer_id: string | null }>();

  if (!user?.stripe_customer_id) {
    return json({ error: 'No active subscription' }, 400);
  }

  const params = new URLSearchParams({
    'customer': user.stripe_customer_id,
    'return_url': 'https://build-your-house.com/advisor/account',
  });

  const res = await fetch('https://api.stripe.com/v1/billing_portal/sessions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${env.STRIPE_SECRET_KEY}`,
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: params.toString(),
  });

  const session = await res.json() as { url: string };
  return json({ url: session.url });
}
