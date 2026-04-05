'use client';

import { useState, FormEvent } from 'react';
import styles from '@/styles/EmailCapture.module.css';

const SUBSCRIBE_API_URL = process.env.NEXT_PUBLIC_SUBSCRIBE_API_URL || '';

interface EmailCaptureProps {
  title?: string;
  description?: string;
  buttonText?: string;
  placeholderText?: string;
  source?: string;
  onSubmit?: (email: string) => Promise<void>;
}

export default function EmailCapture({
  title = "Get the Free Owner-Builder Permit Checklist",
  description = "The same checklist I used on every custom home build. Plus weekly tips from a retired GC.",
  buttonText = "Send Me the Checklist",
  placeholderText = "Enter your email",
  source = "website",
  onSubmit
}: EmailCaptureProps) {
  const [email, setEmail] = useState('');
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
      } else if (SUBSCRIBE_API_URL) {
        const res = await fetch(SUBSCRIBE_API_URL, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ email, source }),
        });

        if (!res.ok) {
          const data = await res.json().catch(() => ({}));
          throw new Error(data.error || 'Subscription failed');
        }
      } else {
        // Fallback: log and simulate success when no API is configured
        console.log('Email submitted (no API configured):', email);
        await new Promise(resolve => setTimeout(resolve, 500));
      }

      setStatus('success');
      setMessage('Check your inbox! We sent you the permit checklist.');
      setEmail('');

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
          We respect your privacy. Unsubscribe at any time. No spam, ever.
        </p>
      </div>
    </div>
  );
}
