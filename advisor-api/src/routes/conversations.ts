import { Env, AuthenticatedRequest } from '../index.ts';

function json(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}

export async function handleConversations(request: Request, env: Env, auth: AuthenticatedRequest, path: string): Promise<Response> {
  // GET /conversations?build_id=xxx — list conversations for a build
  if (path === '/conversations' && request.method === 'GET') {
    return listConversations(request, env, auth);
  }

  // GET /conversations/:id — get a specific conversation
  const convoMatch = path.match(/^\/conversations\/([a-f0-9]+)$/);
  if (convoMatch && request.method === 'GET') {
    return getConversation(env, auth, convoMatch[1]);
  }

  // DELETE /conversations/:id
  if (convoMatch && request.method === 'DELETE') {
    return deleteConversation(env, auth, convoMatch[1]);
  }

  return json({ error: 'Not Found' }, 404);
}

async function listConversations(request: Request, env: Env, auth: AuthenticatedRequest): Promise<Response> {
  const url = new URL(request.url);
  const buildId = url.searchParams.get('build_id');

  if (!buildId) {
    return json({ error: 'build_id is required' }, 400);
  }

  // Verify the build belongs to this user
  const build = await env.DB.prepare(
    'SELECT id FROM builds WHERE id = ? AND user_id = ?'
  ).bind(buildId, auth.userId).first();

  if (!build) return json({ error: 'Build not found' }, 404);

  const conversations = await env.DB.prepare(
    'SELECT id, title, summary, created_at, updated_at FROM conversations WHERE build_id = ? ORDER BY updated_at DESC LIMIT 50'
  ).bind(buildId).all();

  return json({ conversations: conversations.results });
}

async function getConversation(env: Env, auth: AuthenticatedRequest, conversationId: string): Promise<Response> {
  const conversation = await env.DB.prepare(`
    SELECT c.* FROM conversations c
    JOIN builds b ON c.build_id = b.id
    WHERE c.id = ? AND b.user_id = ?
  `).bind(conversationId, auth.userId).first();

  if (!conversation) return json({ error: 'Conversation not found' }, 404);

  return json({ conversation });
}

async function deleteConversation(env: Env, auth: AuthenticatedRequest, conversationId: string): Promise<Response> {
  const result = await env.DB.prepare(`
    DELETE FROM conversations WHERE id = ? AND build_id IN (
      SELECT id FROM builds WHERE user_id = ?
    )
  `).bind(conversationId, auth.userId).run();

  if (!result.meta.changes) return json({ error: 'Conversation not found' }, 404);
  return json({ success: true });
}
