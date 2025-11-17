'use client';

import { useState, FormEvent } from 'react';
import styles from '@/styles/EmailCapture.module.css';

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
        // Placeholder for email service integration
        // TODO: Integrate with Mailchimp, ConvertKit, or other email service
        await new Promise(resolve => setTimeout(resolve, 1000));

        // For now, just log to console
        console.log('Email submitted:', email);
      }

      setStatus('success');
      setMessage('Thank you for subscribing!');
      setEmail('');

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
