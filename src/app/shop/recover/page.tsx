'use client';

import { useState, FormEvent } from 'react';
import Section from '@/components/Section';
import { trackEvent } from '@/lib/analytics';

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
    <div className="content-container">
      <Section spacing="large">
        <div style={{ textAlign: 'center', maxWidth: '600px', margin: '0 auto' }}>
          <h1 style={{ fontSize: 'var(--text-3xl)', marginBottom: 'var(--space-4)' }}>
            Recover Your Download
          </h1>
          <p style={{
            fontSize: 'var(--text-lg)',
            color: 'var(--text-secondary)',
            marginBottom: 'var(--space-8)',
            lineHeight: 'var(--leading-relaxed)',
          }}>
            Bought the Owner-Builder Job Site Binder but lost the download page?
            Enter the email address you used at checkout and we&apos;ll find your order.
          </p>

          {status !== 'found' && (
            <form onSubmit={handleSubmit}>
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
              <div style={{
                display: 'flex',
                gap: 'var(--space-3)',
                justifyContent: 'center',
                flexWrap: 'wrap',
              }}>
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="you@example.com"
                  disabled={status === 'loading'}
                  aria-label="Purchase email address"
                  style={{
                    fontSize: 'var(--text-base)',
                    padding: 'var(--space-3) var(--space-4)',
                    border: '1px solid var(--border, #ccc)',
                    borderRadius: 'var(--radius-md, 8px)',
                    minWidth: '260px',
                  }}
                />
                <button
                  type="submit"
                  className="button"
                  disabled={status === 'loading'}
                  style={{ padding: 'var(--space-3) var(--space-8)' }}
                >
                  {status === 'loading' ? 'Searching…' : 'Find My Order'}
                </button>
              </div>
            </form>
          )}

          {status === 'found' && (
            <div>
              <p style={{
                fontSize: 'var(--text-lg)',
                marginBottom: 'var(--space-6)',
              }}>
                &#10003; Order found! Your download page is ready.
              </p>
              <a
                href={downloadPageUrl}
                className="button button-large"
                style={{
                  fontSize: 'var(--text-xl)',
                  padding: 'var(--space-5) var(--space-10)',
                }}
              >
                Go to Your Download Page
              </a>
            </div>
          )}

          {status === 'notfound' && (
            <p style={{
              marginTop: 'var(--space-6)',
              fontSize: 'var(--text-base)',
              color: 'var(--text-secondary)',
            }} role="status">
              We couldn&apos;t find a completed purchase under that email. Double-check
              the address you used at checkout (it&apos;s on your Stripe receipt). Still
              stuck? Email us at{' '}
              <a href="mailto:info@build-your-house.com">info@build-your-house.com</a>{' '}
              with your receipt and we&apos;ll sort it out.
            </p>
          )}

          {status === 'error' && message && (
            <p style={{
              marginTop: 'var(--space-6)',
              fontSize: 'var(--text-base)',
              color: 'var(--danger, #b91c1c)',
            }} role="alert">
              {message}
            </p>
          )}
        </div>
      </Section>
    </div>
  );
}
