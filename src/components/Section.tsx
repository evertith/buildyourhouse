'use client';

import React from 'react';
import styles from '@/styles/components/Section.module.css';

interface SectionProps {
  title?: string;
  subtitle?: string;
  children: React.ReactNode;
  variant?: 'default' | 'highlighted';
}

export default function Section({ title, subtitle, children, variant = 'default' }: SectionProps) {
  return (
    <section className={`${styles.section} ${styles[variant]}`}>
      {(title || subtitle) && (
        <div className={styles.header}>
          {title && <h2 className={styles.title}>{title}</h2>}
          {subtitle && <p className={styles.subtitle}>{subtitle}</p>}
        </div>
      )}
      <div className={styles.content}>
        {children}
      </div>
    </section>
  );
}
