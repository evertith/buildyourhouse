'use client';

import React from 'react';
import styles from '@/styles/components/CalloutBox.module.css';

type CalloutType = 'tip' | 'warning' | 'critical' | 'info' | 'success';

interface CalloutBoxProps {
  type: CalloutType;
  title?: string;
  children: React.ReactNode;
}

// Line-icon markers (replace emoji) — drawn to match the site's icon system.
const ICONS: Record<CalloutType, React.ReactNode> = {
  info: (
    <>
      <circle cx="12" cy="12" r="9" />
      <path d="M12 11.5v4.5" />
      <path d="M12 8h.01" />
    </>
  ),
  tip: (
    <>
      <path d="M9 18h6" />
      <path d="M10 21h4" />
      <path d="M12 3a6 6 0 0 0-3.6 10.8c.5.4.9 1 1 1.7l.1.5h5l.1-.5c.1-.7.5-1.3 1-1.7A6 6 0 0 0 12 3Z" />
    </>
  ),
  warning: (
    <>
      <path d="M12 3 22 20H2L12 3Z" />
      <path d="M12 10v4" />
      <path d="M12 17h.01" />
    </>
  ),
  critical: (
    <>
      <path d="M8.5 3h7L21 8.5v7L15.5 21h-7L3 15.5v-7L8.5 3Z" />
      <path d="M12 8v5" />
      <path d="M12 16h.01" />
    </>
  ),
  success: (
    <>
      <circle cx="12" cy="12" r="9" />
      <path d="m8 12 3 3 5-6" />
    </>
  ),
};

const defaultTitles: Record<CalloutType, string> = {
  tip: 'Pro Tip',
  warning: 'Warning',
  critical: 'Critical',
  info: 'Important',
  success: 'Success',
};

export default function CalloutBox({ type, title, children }: CalloutBoxProps) {
  return (
    <div className={`${styles.callout} ${styles[type]}`}>
      <div className={styles.title}>
        <svg
          className={styles.icon}
          viewBox="0 0 24 24"
          fill="none"
          stroke="currentColor"
          strokeWidth="1.6"
          strokeLinecap="round"
          strokeLinejoin="round"
          aria-hidden="true"
        >
          {ICONS[type]}
        </svg>
        {title || defaultTitles[type]}
      </div>
      <div className={styles.content}>{children}</div>
    </div>
  );
}
