import { handleAuth } from './routes/auth.ts';
import { handleBuilds } from './routes/builds.ts';
import { handleChat } from './routes/chat.ts';
import { handleConversations } from './routes/conversations.ts';
import { handleWebhook } from './routes/webhook.ts';
import { handleAccount } from './routes/account.ts';
import { verifyToken } from './lib/auth.ts';

export interface Env {
  DB: D1Database;
  ANTHROPIC_API_KEY: string;
  STRIPE_SECRET_KEY: string;
  JWT_SECRET: string;
  STRIPE_WEBHOOK_SECRET: string;
}

export interface AuthenticatedRequest {
  userId: string;
}

const ALLOWED_ORIGINS = [
  'https://build-your-house.com',
  'http://localhost:3000',
];

function corsHeaders(origin: string | null): Record<string, string> {
  const headers: Record<string, string> = {
    'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type, Authorization',
    'Access-Control-Allow-Credentials': 'true',
  };
  if (origin && (ALLOWED_ORIGINS.includes(origin) || origin.endsWith('.build-your-house.com'))) {
    headers['Access-Control-Allow-Origin'] = origin;
  }
  return headers;
}

function jsonResponse(data: unknown, status = 200, origin: string | null = null): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: {
      'Content-Type': 'application/json',
      ...corsHeaders(origin),
    },
  });
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const origin = request.headers.get('Origin');
    const path = url.pathname;

    // CORS preflight
    if (request.method === 'OPTIONS') {
      return new Response(null, { status: 204, headers: corsHeaders(origin) });
    }

    try {
      // Public routes (no auth required)
      if (path.startsWith('/auth/')) {
        const response = await handleAuth(request, env, path);
        return addCors(response, origin);
      }

      // Stripe webhook (uses its own auth via signature)
      if (path === '/webhook/stripe' && request.method === 'POST') {
        const response = await handleWebhook(request, env);
        return addCors(response, origin);
      }

      // Protected routes (auth required)
      const authHeader = request.headers.get('Authorization');
      if (!authHeader || !authHeader.startsWith('Bearer ')) {
        return jsonResponse({ error: 'Unauthorized' }, 401, origin);
      }

      const token = authHeader.slice(7);
      const payload = await verifyToken(token, env.JWT_SECRET);
      if (!payload) {
        return jsonResponse({ error: 'Invalid or expired token' }, 401, origin);
      }

      const auth: AuthenticatedRequest = { userId: payload.sub };

      // Route to handlers
      if (path.startsWith('/builds')) {
        const response = await handleBuilds(request, env, auth, path);
        return addCors(response, origin);
      }

      if (path.startsWith('/chat')) {
        const response = await handleChat(request, env, auth, path);
        // Chat might return streaming response, add CORS differently
        return addCors(response, origin);
      }

      if (path.startsWith('/conversations')) {
        const response = await handleConversations(request, env, auth, path);
        return addCors(response, origin);
      }

      if (path.startsWith('/account')) {
        const response = await handleAccount(request, env, auth, path);
        return addCors(response, origin);
      }

      return jsonResponse({ error: 'Not Found' }, 404, origin);
    } catch (err) {
      console.error('Unhandled error:', err);
      return jsonResponse({ error: 'Internal Server Error' }, 500, origin);
    }
  },
};

function addCors(response: Response, origin: string | null): Response {
  const newHeaders = new Headers(response.headers);
  const cors = corsHeaders(origin);
  for (const [key, value] of Object.entries(cors)) {
    newHeaders.set(key, value);
  }
  return new Response(response.body, {
    status: response.status,
    statusText: response.statusText,
    headers: newHeaders,
  });
}
