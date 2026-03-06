import { Env, AuthenticatedRequest } from '../index.ts';
import { generateId } from '../lib/auth.ts';

function json(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}

export async function handleBuilds(request: Request, env: Env, auth: AuthenticatedRequest, path: string): Promise<Response> {
  // GET /builds — list user's builds
  if (path === '/builds' && request.method === 'GET') {
    return listBuilds(env, auth);
  }

  // POST /builds — create a new build
  if (path === '/builds' && request.method === 'POST') {
    return createBuild(request, env, auth);
  }

  // Match /builds/:id
  const buildMatch = path.match(/^\/builds\/([a-f0-9]+)$/);
  if (buildMatch) {
    const buildId = buildMatch[1];
    if (request.method === 'GET') return getBuild(env, auth, buildId);
    if (request.method === 'PUT') return updateBuild(request, env, auth, buildId);
    if (request.method === 'DELETE') return deleteBuild(env, auth, buildId);
  }

  return json({ error: 'Not Found' }, 404);
}

async function listBuilds(env: Env, auth: AuthenticatedRequest): Promise<Response> {
  const builds = await env.DB.prepare(
    'SELECT * FROM builds WHERE user_id = ? ORDER BY updated_at DESC'
  ).bind(auth.userId).all();

  return json({ builds: builds.results });
}

async function createBuild(request: Request, env: Env, auth: AuthenticatedRequest): Promise<Response> {
  const body = await request.json() as Record<string, unknown>;

  if (!body.state) {
    return json({ error: 'State is required' }, 400);
  }

  const id = generateId();
  const now = new Date().toISOString();

  await env.DB.prepare(`
    INSERT INTO builds (id, user_id, name, state, county, phase, square_footage, stories, foundation_type, build_approach, budget_range, timeline_goal, has_land, has_plans, has_permit, has_loan, notes, created_at, updated_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
  `).bind(
    id,
    auth.userId,
    (body.name as string) || 'My Build',
    body.state as string,
    (body.county as string) || null,
    (body.phase as string) || 'researching',
    (body.square_footage as number) || null,
    (body.stories as number) || 1,
    (body.foundation_type as string) || null,
    (body.build_approach as string) || 'mix',
    (body.budget_range as string) || null,
    (body.timeline_goal as string) || null,
    body.has_land ? 1 : 0,
    body.has_plans ? 1 : 0,
    body.has_permit ? 1 : 0,
    body.has_loan ? 1 : 0,
    (body.notes as string) || null,
    now,
    now,
  ).run();

  const build = await env.DB.prepare('SELECT * FROM builds WHERE id = ?').bind(id).first();
  return json({ build }, 201);
}

async function getBuild(env: Env, auth: AuthenticatedRequest, buildId: string): Promise<Response> {
  const build = await env.DB.prepare(
    'SELECT * FROM builds WHERE id = ? AND user_id = ?'
  ).bind(buildId, auth.userId).first();

  if (!build) return json({ error: 'Build not found' }, 404);
  return json({ build });
}

async function updateBuild(request: Request, env: Env, auth: AuthenticatedRequest, buildId: string): Promise<Response> {
  const existing = await env.DB.prepare(
    'SELECT id FROM builds WHERE id = ? AND user_id = ?'
  ).bind(buildId, auth.userId).first();

  if (!existing) return json({ error: 'Build not found' }, 404);

  const body = await request.json() as Record<string, unknown>;
  const now = new Date().toISOString();

  // Build dynamic update query
  const fields: string[] = [];
  const values: unknown[] = [];

  const allowedFields = ['name', 'state', 'county', 'phase', 'square_footage', 'stories', 'foundation_type', 'build_approach', 'budget_range', 'timeline_goal', 'has_land', 'has_plans', 'has_permit', 'has_loan', 'notes'];

  for (const field of allowedFields) {
    if (field in body) {
      fields.push(`${field} = ?`);
      const val = body[field];
      // Convert booleans to integers for SQLite
      if (field.startsWith('has_')) {
        values.push(val ? 1 : 0);
      } else {
        values.push(val);
      }
    }
  }

  if (fields.length === 0) {
    return json({ error: 'No fields to update' }, 400);
  }

  fields.push('updated_at = ?');
  values.push(now);
  values.push(buildId);
  values.push(auth.userId);

  await env.DB.prepare(
    `UPDATE builds SET ${fields.join(', ')} WHERE id = ? AND user_id = ?`
  ).bind(...values).run();

  const build = await env.DB.prepare('SELECT * FROM builds WHERE id = ?').bind(buildId).first();
  return json({ build });
}

async function deleteBuild(env: Env, auth: AuthenticatedRequest, buildId: string): Promise<Response> {
  const result = await env.DB.prepare(
    'DELETE FROM builds WHERE id = ? AND user_id = ?'
  ).bind(buildId, auth.userId).run();

  if (!result.meta.changes) return json({ error: 'Build not found' }, 404);
  return json({ success: true });
}
