'use client';

import React from 'react';
import styles from '@/styles/components/CalloutBox.module.css';

interface CalloutBoxProps {
  type: 'tip' | 'warning' | 'critical' | 'info' | 'success';
  title?: string;
  children: React.ReactNode;
}

const iconMap = {
  tip: '💡',
  warning: '⚠️',
  critical: '🚨',
  info: 'ℹ️',
  success: '✅',
};

const defaultTitles = {
  tip: 'Pro Tip',
  warning: 'Warning',
  critical: 'Critical',
  info: 'Important Information',
  success: 'Success',
};

export default function CalloutBox({ type, title, children }: CalloutBoxProps) {
  const icon = iconMap[type];
  const displayTitle = title || defaultTitles[type];

  return (
    <div className={`${styles.callout} ${styles[type]}`}>
      <div className={styles.title}>
        <span className={styles.icon}>{icon}</span>
        {displayTitle}
      </div>
      <div className={styles.content}>
        {children}
      </div>
    </div>
  );
}
