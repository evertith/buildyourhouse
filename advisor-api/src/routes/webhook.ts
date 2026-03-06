import { Env } from '../index.ts';

function json(data: unknown, status = 200): Response {
  return new Response(JSON.stringify(data), {
    status,
    headers: { 'Content-Type': 'application/json' },
  });
}

export async function handleWebhook(request: Request, env: Env): Promise<Response> {
  const signature = request.headers.get('stripe-signature');
  if (!signature) return json({ error: 'Missing signature' }, 400);

  // For Cloudflare Workers, we verify the webhook signature manually
  const body = await request.text();

  // Parse the signature header
  const sigParts = signature.split(',').reduce((acc, part) => {
    const [key, value] = part.split('=');
    acc[key.trim()] = value;
    return acc;
  }, {} as Record<string, string>);

  const timestamp = sigParts['t'];
  const expectedSig = sigParts['v1'];

  if (!timestamp || !expectedSig) {
    return json({ error: 'Invalid signature format' }, 400);
  }

  // Verify signature
  const payload = `${timestamp}.${body}`;
  const key = await crypto.subtle.importKey(
    'raw',
    new TextEncoder().encode(env.STRIPE_WEBHOOK_SECRET),
    { name: 'HMAC', hash: 'SHA-256' },
    false,
    ['sign']
  );
  const sig = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(payload));
  const computedSig = Array.from(new Uint8Array(sig)).map(b => b.toString(16).padStart(2, '0')).join('');

  if (computedSig !== expectedSig) {
    return json({ error: 'Invalid signature' }, 400);
  }

  // Verify timestamp is within 5 minutes
  const eventTime = parseInt(timestamp) * 1000;
  if (Math.abs(Date.now() - eventTime) > 300000) {
    return json({ error: 'Timestamp too old' }, 400);
  }

  const event = JSON.parse(body) as { type: string; data: { object: Record<string, unknown> } };

  switch (event.type) {
    case 'checkout.session.completed': {
      const session = event.data.object as {
        metadata?: { user_id?: string; plan?: string };
        subscription?: string;
      };
      const userId = session.metadata?.user_id;
      const plan = session.metadata?.plan || 'starter';
      const subscriptionId = session.subscription as string;

      if (userId && subscriptionId) {
        await env.DB.prepare(
          'UPDATE users SET plan = ?, subscription_status = ?, subscription_id = ?, updated_at = ? WHERE id = ?'
        ).bind(plan, 'active', subscriptionId, new Date().toISOString(), userId).run();
      }
      break;
    }

    case 'customer.subscription.updated': {
      const sub = event.data.object as {
        id: string;
        status: string;
      };
      await env.DB.prepare(
        'UPDATE users SET subscription_status = ?, updated_at = ? WHERE subscription_id = ?'
      ).bind(sub.status, new Date().toISOString(), sub.id).run();
      break;
    }

    case 'customer.subscription.deleted': {
      const sub = event.data.object as { id: string };
      await env.DB.prepare(
        'UPDATE users SET subscription_status = ?, plan = ?, updated_at = ? WHERE subscription_id = ?'
      ).bind('canceled', 'free', new Date().toISOString(), sub.id).run();
      break;
    }
  }

  return json({ received: true });
}
