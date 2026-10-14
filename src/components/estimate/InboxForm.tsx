'use client';

import { FormEvent, useState } from 'react';
import s from '@/styles/Estimate.module.css';
import { trackEvent } from '@/lib/analytics';
import type { Estimate } from '@/lib/estimate/estimate';
import type { Profile } from '@/lib/estimate/geometry';
import { CALCULATOR_NAME, CALCULATOR_SLUG, phaseRows, profileRows, splitRows } from './exports';
import { money, money100 } from './format';

const WORKER_BASE =
  process.env.NEXT_PUBLIC_NEWSLETTER_WORKER_BASE ??
  'https://buildyourhouse-newsletter.azerothcorner.workers.dev';

interface Props {
  estimate: Estimate;
  profile: Profile;
  onSent: () => void;
}

/**
 * Send to inbox: the newsletter Worker's /estimate endpoint mails the ledger
 * and subscribes the address. Results are never gated; the ask comes after
 * the number is on the page. generate_lead fires only on confirmed success.
 */
export default function InboxForm({ estimate, profile, onSent }: Props) {
  const [email, setEmail] = useState('');
  const [honeypot, setHoneypot] = useState('');
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');

  const submit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (status === 'loading') return;
    setStatus('loading');
    const t = estimate.totals;
    try {
      const res = await fetch(`${WORKER_BASE}/estimate`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email,
          website: honeypot,
          sourcePath: window.location.pathname + window.location.search,
          calculator: CALCULATOR_SLUG,
          calculatorName: CALCULATOR_NAME,
          hero: `${money100(t.cash.mid)} cash to build`,
          inputs: profileRows(profile, estimate),
          lines: [...phaseRows(estimate), ...splitRows(estimate)],
          linesLabel: 'Phases',
          cost: `${money100(t.cash.low)} – ${money100(t.cash.high)}, about ${money(t.perSqFt.mid)} per sq ft`,
          costLabel: 'Likely range',
        }),
      });
      if (!res.ok) throw new Error(`estimate send failed: ${res.status}`);
      setStatus('success');
      trackEvent('generate_lead', { method: 'estimate_inbox', calculator: CALCULATOR_SLUG });
      onSent();
    } catch {
      setStatus('error');
    }
  };

  if (status === 'success') {
    return (
      <p className={s.inboxDone} role="status">
        Sent. Give it a few minutes, and check spam if it is not there.
      </p>
    );
  }

  return (
    <form className={s.inboxForm} onSubmit={submit}>
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
        className={s.inboxInput}
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        disabled={status === 'loading'}
      />
      <button type="submit" className={`${s.btn} ${s.btnGhost}`} style={{ marginTop: 0 }} disabled={status === 'loading'}>
        {status === 'loading' ? 'Sending…' : 'Send the ledger'}
      </button>
      {status === 'error' ? (
        <p className={s.inboxError} role="alert">
          That did not send. Try again in a minute.
        </p>
      ) : (
        <p className={s.cardFine}>
          One email with your numbers, then the occasional owner-builder letter. Unsubscribe in one click.
        </p>
      )}
    </form>
  );
}
