import { Env, AuthenticatedRequest } from '../index.ts';
import { generateId } from '../lib/auth.ts';
import { getRelevantContent, formatContentForPrompt, STATE_DISPLAY_NAMES } from '../lib/content-map.ts';

function json(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}

interface Build {
  id: string;
  name: string;
  state: string;
  county: string | null;
  phase: string;
  square_footage: number | null;
  stories: number | null;
  foundation_type: string | null;
  build_approach: string;
  budget_range: string | null;
  timeline_goal: string | null;
  has_land: number;
  has_plans: number;
  has_permit: number;
  has_loan: number;
  notes: string | null;
}

interface Memory {
  fact: string;
  category: string;
  created_at: string;
}

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

const PLAN_LIMITS: Record<string, number> = {
  free: 5,
  starter: 50,
  pro: 200,
};

export async function handleChat(request: Request, env: Env, auth: AuthenticatedRequest, path: string): Promise<Response> {
  if (path === '/chat' && request.method === 'POST') {
    return chat(request, env, auth);
  }
  return json({ error: 'Not Found' }, 404);
}

async function chat(request: Request, env: Env, auth: AuthenticatedRequest): Promise<Response> {
  const body = await request.json() as {
    build_id: string;
    conversation_id?: string;
    message: string;
  };

  if (!body.build_id || !body.message) {
    return json({ error: 'build_id and message are required' }, 400);
  }

  // Check user's plan and query limits
  const user = await env.DB.prepare(
    'SELECT plan, queries_used_this_month, queries_reset_at, subscription_status FROM users WHERE id = ?'
  ).bind(auth.userId).first<{
    plan: string;
    queries_used_this_month: number;
    queries_reset_at: string;
    subscription_status: string;
  }>();

  if (!user) return json({ error: 'User not found' }, 404);

  // Reset monthly counter if needed
  const resetAt = new Date(user.queries_reset_at);
  const now = new Date();
  if (now.getMonth() !== resetAt.getMonth() || now.getFullYear() !== resetAt.getFullYear()) {
    await env.DB.prepare(
      'UPDATE users SET queries_used_this_month = 0, queries_reset_at = ? WHERE id = ?'
    ).bind(now.toISOString(), auth.userId).run();
    user.queries_used_this_month = 0;
  }

  // Check limits
  const limit = PLAN_LIMITS[user.plan] || PLAN_LIMITS.free;
  if (user.plan !== 'free' && user.subscription_status !== 'active') {
    // Paid plan but subscription lapsed — fall back to free limits
    const freeLimit = PLAN_LIMITS.free;
    if (user.queries_used_this_month >= freeLimit) {
      return json({ error: 'Query limit reached. Please renew your subscription.', limit_reached: true }, 429);
    }
  } else if (user.queries_used_this_month >= limit) {
    return json({ error: 'Monthly query limit reached.', limit_reached: true, plan: user.plan, limit }, 429);
  }

  // Get the build
  const build = await env.DB.prepare(
    'SELECT * FROM builds WHERE id = ? AND user_id = ?'
  ).bind(body.build_id, auth.userId).first<Build>();

  if (!build) return json({ error: 'Build not found' }, 404);

  // Get memories for this build
  const memoriesResult = await env.DB.prepare(
    'SELECT fact, category, created_at FROM memories WHERE build_id = ? ORDER BY created_at DESC LIMIT 30'
  ).bind(build.id).all<Memory>();
  const memories = memoriesResult.results;

  // Get or create conversation
  let conversationId = body.conversation_id;
  let previousMessages: Message[] = [];

  if (conversationId) {
    const convo = await env.DB.prepare(
      'SELECT messages FROM conversations WHERE id = ? AND build_id = ?'
    ).bind(conversationId, build.id).first<{ messages: string }>();

    if (convo) {
      previousMessages = JSON.parse(convo.messages);
    }
  } else {
    conversationId = generateId();
  }

  // Get relevant content based on phase, state, and query
  const relevantContent = getRelevantContent(build.phase, build.state, body.message);
  const contentText = formatContentForPrompt(relevantContent);

  // Build the system prompt
  const systemPrompt = buildSystemPrompt(build, memories, contentText);

  // Build messages array for Claude
  const claudeMessages = [
    ...previousMessages.map(m => ({ role: m.role as 'user' | 'assistant', content: m.content })),
    { role: 'user' as const, content: body.message },
  ];

  // Call Claude API (streaming)
  const claudeResponse = await fetch('https://api.anthropic.com/v1/messages', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-api-key': env.ANTHROPIC_API_KEY,
      'anthropic-version': '2023-06-01',
    },
    body: JSON.stringify({
      model: 'claude-sonnet-4-20250514',
      max_tokens: 2048,
      system: systemPrompt,
      messages: claudeMessages,
      stream: true,
    }),
  });

  if (!claudeResponse.ok) {
    const err = await claudeResponse.text();
    console.error('Claude API error:', err);
    return json({ error: 'AI service error' }, 502);
  }

  // Stream the response back, collecting the full response for storage
  const { readable, writable } = new TransformStream();
  const writer = writable.getWriter();
  const encoder = new TextEncoder();

  // Process the stream in the background
  const fullResponseParts: string[] = [];

  (async () => {
    try {
      const reader = claudeResponse.body!.getReader();
      const decoder = new TextDecoder();
      let buffer = '';

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;

        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split('\n');
        buffer = lines.pop() || '';

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            const data = line.slice(6);
            if (data === '[DONE]') continue;

            try {
              const event = JSON.parse(data);
              if (event.type === 'content_block_delta' && event.delta?.text) {
                fullResponseParts.push(event.delta.text);
                await writer.write(encoder.encode(`data: ${JSON.stringify({ text: event.delta.text })}\n\n`));
              }
            } catch {
              // Skip malformed events
            }
          }
        }
      }

      // Send done event
      await writer.write(encoder.encode(`data: ${JSON.stringify({ done: true, conversation_id: conversationId })}\n\n`));

      // Save conversation and update query count
      const fullResponse = fullResponseParts.join('');
      const updatedMessages: Message[] = [
        ...previousMessages,
        { role: 'user', content: body.message },
        { role: 'assistant', content: fullResponse },
      ];

      const title = previousMessages.length === 0
        ? body.message.slice(0, 100)
        : undefined;

      const nowStr = new Date().toISOString();

      if (body.conversation_id) {
        // Update existing conversation
        await env.DB.prepare(
          'UPDATE conversations SET messages = ?, updated_at = ? WHERE id = ?'
        ).bind(JSON.stringify(updatedMessages), nowStr, conversationId).run();
      } else {
        // Create new conversation
        await env.DB.prepare(
          'INSERT INTO conversations (id, build_id, title, messages, created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?)'
        ).bind(conversationId, build.id, title, JSON.stringify(updatedMessages), nowStr, nowStr).run();
      }

      // Increment query count
      await env.DB.prepare(
        'UPDATE users SET queries_used_this_month = queries_used_this_month + 1 WHERE id = ?'
      ).bind(auth.userId).run();

      // Extract memories in the background using Haiku (cheap)
      await extractMemories(env, build.id, conversationId!, body.message, fullResponse);

    } catch (err) {
      console.error('Stream processing error:', err);
      await writer.write(encoder.encode(`data: ${JSON.stringify({ error: 'Stream error' })}\n\n`));
    } finally {
      await writer.close();
    }
  })();

  return new Response(readable, {
    headers: {
      'Content-Type': 'text/event-stream',
      'Cache-Control': 'no-cache',
      'Connection': 'keep-alive',
    },
  });
}

function buildSystemPrompt(build: Build, memories: Memory[], contentText: string): string {
  const stateName = STATE_DISPLAY_NAMES[build.state] || build.state;
  const location = build.county ? `${build.county}, ${stateName}` : stateName;

  let prompt = `You are a retired general contractor with 15+ years of experience, serving as a personal construction advisor for an owner-builder. You are knowledgeable, patient, and practical. You give specific, actionable advice — not vague generalities.

IMPORTANT RULES:
- Always give answers specific to their location (${location}) when relevant — building codes, permit requirements, climate considerations, and local practices.
- Reference specific code sections (IRC, IBC, NEC, UPC) when discussing code requirements.
- When you're unsure about a local requirement, say so and recommend they verify with their building department.
- Use plain language but don't dumb things down. These are motivated adults making a major investment.
- If they describe a problem, ask clarifying questions before giving advice — just like a real GC would.
- When discussing costs, give realistic ranges for their area if possible.
- Proactively warn about common mistakes relevant to their current phase.

PROJECT DETAILS:
- Location: ${location}
- Current Phase: ${build.phase}`;

  if (build.square_footage) prompt += `\n- Square Footage: ${build.square_footage} sq ft`;
  if (build.stories) prompt += `\n- Stories: ${build.stories}`;
  if (build.foundation_type) prompt += `\n- Foundation: ${build.foundation_type}`;
  if (build.build_approach) prompt += `\n- Build Approach: ${build.build_approach === 'diy' ? 'Mostly DIY' : build.build_approach === 'subs' ? 'Mostly hiring subs' : 'Mix of DIY and hiring subs'}`;
  if (build.budget_range) prompt += `\n- Budget: ${build.budget_range}`;
  if (build.timeline_goal) prompt += `\n- Timeline Goal: ${build.timeline_goal}`;

  prompt += `\n- Has Land: ${build.has_land ? 'Yes' : 'Not yet'}`;
  prompt += `\n- Has Plans: ${build.has_plans ? 'Yes' : 'Not yet'}`;
  prompt += `\n- Has Permit: ${build.has_permit ? 'Yes' : 'Not yet'}`;
  prompt += `\n- Has Loan: ${build.has_loan ? 'Yes' : 'Not yet'}`;

  if (build.notes) prompt += `\n- Notes: ${build.notes}`;

  if (memories.length > 0) {
    prompt += `\n\nWHAT YOU KNOW FROM PREVIOUS CONVERSATIONS:`;
    for (const m of memories) {
      prompt += `\n- [${m.category}] ${m.fact}`;
    }
  }

  if (contentText) {
    prompt += `\n\nRELEVANT REFERENCE MATERIAL FROM BUILD-YOUR-HOUSE.COM:
${contentText}

Use this reference material to inform your answers. You can reference specific guides by mentioning "check out our guide on [topic]" with the path.`;
  }

  return prompt;
}

async function extractMemories(env: Env, buildId: string, conversationId: string, userMessage: string, assistantResponse: string): Promise<void> {
  try {
    const extractionPrompt = `Analyze this conversation exchange between an owner-builder and their construction advisor. Extract any NEW FACTS about the owner-builder's project that would be useful to remember for future conversations.

USER MESSAGE:
${userMessage}

ADVISOR RESPONSE:
${assistantResponse}

Extract facts as a JSON array. Each fact should have:
- "fact": A concise statement of the fact (e.g., "Foundation inspection passed on March 15")
- "category": One of: progress, decision, issue, preference, contractor, timeline, budget, code

Only include facts that are SPECIFIC to this person's build — not general construction knowledge. If there are no new project-specific facts, return an empty array.

Return ONLY valid JSON, no other text. Example:
[{"fact": "Chose slab foundation over crawl space", "category": "decision"}]`;

    const response = await fetch('https://api.anthropic.com/v1/messages', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01',
      },
      body: JSON.stringify({
        model: 'claude-haiku-4-5-20251001',
        max_tokens: 512,
        messages: [{ role: 'user', content: extractionPrompt }],
      }),
    });

    if (!response.ok) return;

    const result = await response.json() as { content: Array<{ text: string }> };
    const text = result.content[0]?.text || '[]';

    let facts: Array<{ fact: string; category: string }>;
    try {
      facts = JSON.parse(text);
    } catch {
      // Try to extract JSON from the response
      const match = text.match(/\[[\s\S]*\]/);
      if (match) {
        facts = JSON.parse(match[0]);
      } else {
        return;
      }
    }

    if (!Array.isArray(facts) || facts.length === 0) return;

    // Insert memories
    for (const fact of facts.slice(0, 5)) { // Max 5 facts per exchange
      if (fact.fact && fact.category) {
        const id = generateId();
        await env.DB.prepare(
          'INSERT INTO memories (id, build_id, fact, category, source_conversation_id, created_at) VALUES (?, ?, ?, ?, ?, ?)'
        ).bind(id, buildId, fact.fact, fact.category, conversationId, new Date().toISOString()).run();
      }
    }
  } catch (err) {
    console.error('Memory extraction error:', err);
    // Non-fatal — don't break the chat flow
  }
}
