'use client';

/**
 * The tear-off stub (design spec §6): emails the visitor their takeoff via
 * the newsletter worker's /estimate endpoint, which also subscribes them.
 * Results are never gated; the ask comes after full value is delivered.
 * Fires generate_lead only on confirmed success.
 */

import { FormEvent, useState } from 'react';
import s from '@/styles/CalcSheet.module.css';
import { trackEvent } from '@/lib/analytics';

const WORKER_BASE =
  process.env.NEXT_PUBLIC_NEWSLETTER_WORKER_BASE ??
  'https://buildyourhouse-newsletter.azerothcorner.workers.dev';

export interface EstimatePayload {
  calculator: string; // slug
  calculatorName: string;
  hero: string; // "89 sheets"
  inputs: { label: string; value: string }[];
  lines: { label: string; value: string }[];
  cost: string; // "$1,240 – $1,690"
}

export default function EstimateCapture({ payload }: { payload: EstimatePayload }) {
  const [email, setEmail] = useState('');
  const [honeypot, setHoneypot] = useState('');
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');

  const submit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (status === 'loading') return;
    setStatus('loading');
    try {
      const res = await fetch(`${WORKER_BASE}/estimate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email,
          website: honeypot,
          sourcePath: window.location.pathname,
          ...payload,
        }),
      });
      if (!res.ok) throw new Error(`estimate send failed: ${res.status}`);
      setStatus('success');
      trackEvent('generate_lead', {
        method: 'calculator_estimate',
        calculator: payload.calculator,
      });
    } catch {
      setStatus('error');
    }
  };

  return (
    <div className={`${s.tearoff} no-print`}>
      <div>
        <p className={s.tearoffHead}>Send this takeoff to your inbox</p>
        <p className={s.tearoffSub}>
          The quantities above, with your inputs, as one email — so you still
          have them when you&apos;re pricing at the lumberyard. You&apos;ll also get our
          owner-builder newsletter; unsubscribe any time.
        </p>
      </div>
      {status === 'success' ? (
        <p className={s.tearoffDone} role="status">
          Sent. Give it a few minutes, and check spam if it&apos;s not there.
        </p>
      ) : (
        <form className={s.tearoffForm} onSubmit={submit}>
          {/* Honeypot — hidden from real users, bots auto-fill it */}
          <input
            type="text"
            name="website"
            value={honeypot}
            onChange={(e) => setHoneypot(e.target.value)}
            style={{ position: 'absolute', left: '-9999px', height: 0, width: 0, opacity: 0 }}
            tabIndex={-1}
            autoComplete="off"
            aria-hidden="true"
          />
          <input
            type="email"
            required
            placeholder="you@example.com"
            aria-label="Email address"
            className={s.tearoffInput}
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            disabled={status === 'loading'}
          />
          <button type="submit" className={s.tearoffBtn} disabled={status === 'loading'}>
            {status === 'loading' ? 'Sending…' : 'Email my estimate'}
          </button>
        </form>
      )}
      {status === 'error' ? (
        <p className={`${s.tearoffFine} ${s.fieldError}`} role="alert">
          That didn&apos;t send. Try again in a minute.
        </p>
      ) : (
        <p className={s.tearoffFine}>
          No spam. One email with your numbers, then the occasional newsletter.
          Unsubscribe in one click.
        </p>
      )}
    </div>
  );
}
