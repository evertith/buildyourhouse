'use client';

import { useState, FormEvent } from 'react';
import styles from '@/styles/EmailCapture.module.css';
import { trackEvent } from '@/lib/analytics';

// Cloudflare Worker (workers/newsletter) backed by D1. Export the list with:
// wrangler d1 execute buildyourhouse-newsletter --remote --command "SELECT * FROM subscribers"
const NEWSLETTER_ENDPOINT =
  process.env.NEXT_PUBLIC_NEWSLETTER_ENDPOINT ??
  'https://buildyourhouse-newsletter.azerothcorner.workers.dev/subscribe';

interface EmailCaptureProps {
  title?: string;
  description?: string;
  buttonText?: string;
  placeholderText?: string;
  onSubmit?: (email: string) => Promise<void>;
}

export default function EmailCapture({
  title = "Join Our Newsletter",
  description = "Get expert tips on building your own house delivered to your inbox.",
  buttonText = "Subscribe",
  placeholderText = "Enter your email",
  onSubmit
}: EmailCaptureProps) {
  const [email, setEmail] = useState('');
  const [honeypot, setHoneypot] = useState('');
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');
  const [message, setMessage] = useState('');

  const validateEmail = (email: string): boolean => {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    if (!email) {
      setStatus('error');
      setMessage('Please enter an email address');
      return;
    }

    if (!validateEmail(email)) {
      setStatus('error');
      setMessage('Please enter a valid email address');
      return;
    }

    setStatus('loading');
    setMessage('');

    try {
      if (onSubmit) {
        await onSubmit(email);
      } else {
        const response = await fetch(NEWSLETTER_ENDPOINT, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            email,
            source: window.location.pathname,
            website: honeypot,
          }),
        });
        if (!response.ok) {
          throw new Error(`subscribe failed: ${response.status}`);
        }
      }

      setStatus('success');
      setMessage('Thank you for subscribing!');
      setEmail('');

      // GA4 recommended lead-gen event; mark as a key event in GA4 admin.
      trackEvent('generate_lead', { method: 'newsletter_form' });

      // Reset success message after 5 seconds
      setTimeout(() => {
        setStatus('idle');
        setMessage('');
      }, 5000);
    } catch (error) {
      setStatus('error');
      setMessage('Something went wrong. Please try again.');
      console.error('Email submission error:', error);
    }
  };

  return (
    <div className={styles.emailCapture}>
      <div className={styles.content}>
        <h2 className={styles.title}>{title}</h2>
        <p className={styles.description}>{description}</p>

        <form onSubmit={handleSubmit} className={styles.form}>
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
          <div className={styles.inputWrapper}>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder={placeholderText}
              className={`${styles.input} ${status === 'error' ? styles.inputError : ''}`}
              disabled={status === 'loading'}
              aria-label="Email address"
              aria-invalid={status === 'error'}
              aria-describedby={message ? 'email-message' : undefined}
            />
            <button
              type="submit"
              className={styles.button}
              disabled={status === 'loading'}
            >
              {status === 'loading' ? 'Subscribing...' : buttonText}
            </button>
          </div>

          {message && (
            <p
              id="email-message"
              className={`${styles.message} ${
                status === 'success' ? styles.messageSuccess : styles.messageError
              }`}
              role={status === 'error' ? 'alert' : 'status'}
            >
              {message}
            </p>
          )}
        </form>

        <p className={styles.privacy}>
          We respect your privacy. Unsubscribe at any time.
        </p>
      </div>
    </div>
  );
}
