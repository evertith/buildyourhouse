'use client';

import { useState, FormEvent } from 'react';
import styles from '@/styles/SampleCapture.module.css';
import { trackEvent } from '@/lib/analytics';

// Same Cloudflare Worker (workers/newsletter, D1-backed) that EmailCapture posts to.
const NEWSLETTER_ENDPOINT =
  process.env.NEXT_PUBLIC_NEWSLETTER_ENDPOINT ??
  'https://buildyourhouse-newsletter.azerothcorner.workers.dev/subscribe';

const SAMPLE_PDF = '/binder-sample.pdf';

/**
 * Email gate on the free 19-page binder sample. On success it swaps to the
 * download link in place — the reader never leaves the trust section.
 */
export default function SampleCapture() {
  const [email, setEmail] = useState('');
  const [honeypot, setHoneypot] = useState('');
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');
  const [message, setMessage] = useState('');

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      setStatus('error');
      setMessage('Enter a valid email address and the sample opens right here.');
      return;
    }

    setStatus('loading');
    setMessage('');

    try {
      const response = await fetch(NEWSLETTER_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email,
          source: '/shop-sample',
          website: honeypot,
        }),
      });
      if (!response.ok) {
        throw new Error(`subscribe failed: ${response.status}`);
      }

      setStatus('success');
      setEmail('');
      trackEvent('generate_lead', { method: 'sample_pages' });
    } catch (error) {
      setStatus('error');
      setMessage('That did not go through. Try again, or email us and we will send the sample.');
      console.error('Sample capture error:', error);
    }
  };

  if (status === 'success') {
    return (
      <div className={styles.done}>
        <p className={styles.doneLabel}>Sample ready — 19 pages</p>
        <p className={styles.doneCopy}>
          Opens as a PDF. A copy is on its way to your inbox as well.
        </p>
        <a className={styles.button} href={SAMPLE_PDF} target="_blank" rel="noopener">
          Open the sample PDF
        </a>
      </div>
    );
  }

  return (
    <>
      <form onSubmit={handleSubmit} className={styles.form}>
        <input
          type="text"
          name="website"
          value={honeypot}
          onChange={(e) => setHoneypot(e.target.value)}
          className={styles.hp}
          tabIndex={-1}
          autoComplete="off"
          aria-hidden="true"
        />
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="you@example.com"
          className={styles.input}
          disabled={status === 'loading'}
          aria-label="Email address"
          aria-invalid={status === 'error'}
          aria-describedby={message ? 'sample-message' : undefined}
        />
        <button type="submit" className={styles.button} disabled={status === 'loading'}>
          {status === 'loading' ? 'Sending…' : 'Send me the 19 pages'}
        </button>
      </form>

      {message && (
        <p id="sample-message" className={styles.message} role="alert">
          {message}
        </p>
      )}

      <p className={styles.privacy}>
        One email, then the occasional build guide. Unsubscribe any time.
      </p>
    </>
  );
}
