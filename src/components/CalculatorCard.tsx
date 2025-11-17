'use client';

import React from 'react';
import styles from '@/styles/components/CalculatorCard.module.css';

interface CalculatorCardProps {
  title: string;
  description?: string;
  children: React.ReactNode;
}

export default function CalculatorCard({ title, description, children }: CalculatorCardProps) {
  return (
    <div className={styles.card}>
      <div className={styles.header}>
        <h3 className={styles.title}>{title}</h3>
        {description && <p className={styles.description}>{description}</p>}
      </div>
      <div className={styles.content}>
        {children}
      </div>
    </div>
  );
}
