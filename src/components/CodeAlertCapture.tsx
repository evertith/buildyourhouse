'use client';

/**
 * Code Change Alerts — the revision watch as a subscriber promise.
 *
 * Sits on every state guide. The pitch is the one thing only this site can
 * honestly offer: we track each state's code transitions for the kit
 * program's revision watch anyway, so "email me when this state's rules
 * change" costs nothing to keep and is state-specific in a way no generic
 * newsletter is. Subscribers self-label by state via sourcePath +
 * '#code-alerts', so a transition broadcast filters the list by guide path.
 */

import { FormEvent, useState } from 'react';
import s from '@/styles/CodeAlertCapture.module.css';
import { trackEvent } from '@/lib/analytics';

const NEWSLETTER_ENDPOINT =
  process.env.NEXT_PUBLIC_NEWSLETTER_ENDPOINT ??
  'https://buildyourhouse-newsletter.azerothcorner.workers.dev/subscribe';

export default function CodeAlertCapture({ state }: { state: string }) {
  const [email, setEmail] = useState('');
  const [honeypot, setHoneypot] = useState('');
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');

  const submit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (status === 'loading') return;
    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      setStatus('error');
      return;
    }
    setStatus('loading');
    try {
      const res = await fetch(NEWSLETTER_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email,
          website: honeypot,
          source: `${window.location.pathname}#code-alerts`,
        }),
      });
      if (!res.ok) throw new Error(String(res.status));
      setStatus('success');
      trackEvent('generate_lead', { method: 'code_alert' });
    } catch {
      setStatus('error');
    }
  };

  return (
    <aside className={s.band} aria-label={`${state} code change alerts`}>
      <div className={s.copy}>
        <p className={s.kicker}>Revision watch · {state}</p>
        <p className={s.head}>Codes change. This page changes with them.</p>
        <p className={s.sub}>
          When {state} adopts a new edition or rewrites a rule on this page, we
          verify it against the primary source, update the guide, and email
          everyone who asked to know. That&rsquo;s the whole promise — no
          drip campaigns, just the change.
        </p>
      </div>
      {status === 'success' ? (
        <p className={s.done} role="status">
          Watching {state} for you. We&rsquo;ll email when the rules move.
        </p>
      ) : (
        <form className={s.form} onSubmit={submit}>
          <input
            type="text"
            name="website"
            value={honeypot}
            onChange={(e) => setHoneypot(e.target.value)}
            className={s.hp}
            tabIndex={-1}
            autoComplete="off"
            aria-hidden="true"
          />
          <input
            type="email"
            required
            placeholder="you@example.com"
            aria-label="Email address for code change alerts"
            className={s.input}
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            disabled={status === 'loading'}
          />
          <button type="submit" className={s.btn} disabled={status === 'loading'}>
            {status === 'loading' ? 'Adding…' : 'Watch this state'}
          </button>
          {status === 'error' && (
            <p className={s.err} role="alert">
              That didn&rsquo;t send — check the address and try again.
            </p>
          )}
        </form>
      )}
    </aside>
  );
}
