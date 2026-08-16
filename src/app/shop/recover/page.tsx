'use client';

import { useState, FormEvent } from 'react';
import { trackEvent } from '@/lib/analytics';
import styles from '../transaction.module.css';

const WORKER_BASE_URL = 'https://buildyourhouse-downloads.azerothcorner.workers.dev';

export default function RecoverPage() {
  const [email, setEmail] = useState('');
  const [honeypot, setHoneypot] = useState('');
  const [status, setStatus] = useState<'idle' | 'loading' | 'found' | 'notfound' | 'error'>('idle');
  const [message, setMessage] = useState('');
  const [downloadPageUrl, setDownloadPageUrl] = useState('');

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const trimmed = email.trim();
    if (!trimmed || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(trimmed)) {
      setStatus('error');
      setMessage('Please enter a valid email address.');
      return;
    }

    setStatus('loading');
    setMessage('');

    try {
      const res = await fetch(`${WORKER_BASE_URL}/recover`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: trimmed, website: honeypot }),
      });
      if (res.status === 429) {
        setStatus('error');
        setMessage('Too many attempts. Please wait an hour and try again.');
        return;
      }
      if (!res.ok) {
        throw new Error(`recover failed: ${res.status}`);
      }
      const data = await res.json();
      if (data.found && data.url) {
        setStatus('found');
        setDownloadPageUrl(data.url);
        trackEvent('download_recovered', { item_name: 'job_site_binder' });
      } else {
        setStatus('notfound');
      }
    } catch {
      setStatus('error');
      setMessage('Something went wrong. Please try again in a moment.');
    }
  };

  return (
    <div className={styles.page}>
      <section className={`${styles.hero} bp-band bp-grid`}>
        <span className={`${styles.crop} ${styles.tl}`} />
        <span className={`${styles.crop} ${styles.tr}`} />
        <span className={`${styles.crop} ${styles.bl}`} />
        <span className={`${styles.crop} ${styles.br}`} />
        <div className={styles.heroInner}>
          <div className={styles.heroBody}>
            <div className={`${styles.eyebrow} bp-eyebrow`}>Download recovery</div>
            <h1 className={styles.heroTitle}>Recover your download</h1>
            <p className={styles.heroSub}>
              Bought from the shop but lost the download page?
            </p>
            <p className={styles.heroCopy}>
              Enter the email address you used at checkout and we’ll find your order. Your
              files don’t expire, so there is nothing to re-buy.
            </p>
          </div>
        </div>
      </section>

      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.panel}>
            <div className={styles.panelNo}>
              <span>Order lookup</span>
              <span>Purchase email</span>
            </div>

            {status !== 'found' && (
              <form className={styles.form} onSubmit={handleSubmit}>
                {/* Honeypot — hidden from real users, bots auto-fill it */}
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
                <label className={styles.label} htmlFor="recover-email">
                  Purchase email address
                </label>
                <div className={styles.field}>
                  <input
                    id="recover-email"
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="you@example.com"
                    disabled={status === 'loading'}
                    className={styles.input}
                  />
                  <button
                    type="submit"
                    className={`${styles.btnPrimary} ${styles.submit}`}
                    disabled={status === 'loading'}
                  >
                    {status === 'loading' ? 'Searching…' : 'Find My Order'}
                  </button>
                </div>
                <p className={styles.formNote}>
                  Matched against the address on your Stripe receipt
                </p>
              </form>
            )}

            {status === 'found' && (
              <div className={styles.found}>
                <p className={styles.foundLine}>
                  <span className={styles.tick} aria-hidden="true">
                    &#10003;
                  </span>
                  Order found. Your download page is ready.
                </p>
                <a
                  href={downloadPageUrl}
                  className={`${styles.btnPrimary} ${styles.btnBig}`}
                >
                  Go to Your Download Page
                </a>
              </div>
            )}

            {status === 'notfound' && (
              <p className={styles.stateNote} role="status">
                We couldn&apos;t find a completed purchase under that email. Double-check
                the address you used at checkout (it&apos;s on your Stripe receipt). Still
                stuck? Email us at{' '}
                <a href="mailto:info@build-your-house.com">info@build-your-house.com</a>{' '}
                with your receipt and we&apos;ll sort it out.
              </p>
            )}

            {status === 'error' && message && (
              <p className={styles.stateErr} role="alert">
                {message}
              </p>
            )}
          </div>
        </div>
      </section>
    </div>
  );
}
