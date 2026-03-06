import { Env } from '../index.ts';
import { hashPassword, verifyPassword, createToken, generateId } from '../lib/auth.ts';

function json(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}

export async function handleAuth(request: Request, env: Env, path: string): Promise<Response> {
  if (path === '/auth/signup' && request.method === 'POST') {
    return signup(request, env);
  }
  if (path === '/auth/login' && request.method === 'POST') {
    return login(request, env);
  }
  return json({ error: 'Not Found' }, 404);
}

async function signup(request: Request, env: Env): Promise<Response> {
  const body = await request.json() as { email?: string; password?: string; name?: string };

  if (!body.email || !body.password) {
    return json({ error: 'Email and password are required' }, 400);
  }

  const email = body.email.toLowerCase().trim();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    return json({ error: 'Invalid email address' }, 400);
  }

  if (body.password.length < 8) {
    return json({ error: 'Password must be at least 8 characters' }, 400);
  }

  // Check if email already exists
  const existing = await env.DB.prepare('SELECT id FROM users WHERE email = ?').bind(email).first();
  if (existing) {
    return json({ error: 'An account with this email already exists' }, 409);
  }

  const id = generateId();
  const passwordHash = await hashPassword(body.password);
  const now = new Date().toISOString();

  await env.DB.prepare(
    'INSERT INTO users (id, email, password_hash, name, queries_reset_at, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)'
  ).bind(id, email, passwordHash, body.name || null, now, now, now).run();

  const token = await createToken(id, email, env.JWT_SECRET);

  return json({ token, user: { id, email, name: body.name || null, plan: 'free', subscription_status: 'none' } }, 201);
}

async function login(request: Request, env: Env): Promise<Response> {
  const body = await request.json() as { email?: string; password?: string };

  if (!body.email || !body.password) {
    return json({ error: 'Email and password are required' }, 400);
  }

  const email = body.email.toLowerCase().trim();

  const user = await env.DB.prepare(
    'SELECT id, email, password_hash, name, plan, subscription_status FROM users WHERE email = ?'
  ).bind(email).first<{
    id: string;
    email: string;
    password_hash: string;
    name: string | null;
    plan: string;
    subscription_status: string;
  }>();

  if (!user) {
    return json({ error: 'Invalid email or password' }, 401);
  }

  const validPassword = await verifyPassword(body.password, user.password_hash);
  if (!validPassword) {
    return json({ error: 'Invalid email or password' }, 401);
  }

  const token = await createToken(user.id, user.email, env.JWT_SECRET);

  return json({
    token,
    user: {
      id: user.id,
      email: user.email,
      name: user.name,
      plan: user.plan,
      subscription_status: user.subscription_status,
    },
  });
}
