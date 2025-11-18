'use client';

import React from 'react';
import styles from '@/styles/components/Section.module.css';

interface SectionProps {
  title?: string;
  subtitle?: string;
  children: React.ReactNode;
  variant?: 'default' | 'highlighted';
  spacing?: 'default' | 'large';
  background?: 'default' | 'warm';
}

export default function Section({
  title,
  subtitle,
  children,
  variant = 'default',
  spacing = 'default',
  background = 'default'
}: SectionProps) {
  const sectionClasses = [
    styles.section,
    styles[variant],
    spacing === 'large' ? styles.spacingLarge : '',
    background === 'warm' ? styles.backgroundWarm : ''
  ].filter(Boolean).join(' ');

  return (
    <section className={sectionClasses}>
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
