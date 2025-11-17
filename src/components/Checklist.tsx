'use client';

import React, { useState, useEffect } from 'react';
import styles from '@/styles/components/Checklist.module.css';

interface ChecklistProps {
  title?: string;
  items: string[];
  storageKey?: string;
}

export default function Checklist({ title, items, storageKey }: ChecklistProps) {
  const [checked, setChecked] = useState<Set<number>>(new Set());

  // Load from localStorage on mount
  useEffect(() => {
    if (storageKey && typeof window !== 'undefined') {
      const saved = localStorage.getItem(storageKey);
      if (saved) {
        try {
          const savedSet = new Set<number>(JSON.parse(saved));
          setChecked(savedSet);
        } catch (e) {
          console.error('Failed to load checklist state:', e);
        }
      }
    }
  }, [storageKey]);

  // Save to localStorage when changed
  useEffect(() => {
    if (storageKey && typeof window !== 'undefined') {
      localStorage.setItem(storageKey, JSON.stringify(Array.from(checked)));
    }
  }, [checked, storageKey]);

  const toggleItem = (index: number) => {
    setChecked(prev => {
      const newSet = new Set(prev);
      if (newSet.has(index)) {
        newSet.delete(index);
      } else {
        newSet.add(index);
      }
      return newSet;
    });
  };

  return (
    <div className={styles.checklist}>
      {title && <h3 className={styles.title}>{title}</h3>}
      <div className={styles.items}>
        {items.map((item, index) => (
          <div key={index} className={styles.item}>
            <button
              className={`${styles.checkbox} ${checked.has(index) ? styles.checked : ''}`}
              onClick={() => toggleItem(index)}
              aria-label={checked.has(index) ? `Uncheck ${item}` : `Check ${item}`}
              type="button"
            >
              {checked.has(index) && <span className={styles.checkmark}>✓</span>}
            </button>
            <label
              className={`${styles.label} ${checked.has(index) ? styles.labelChecked : ''}`}
              onClick={() => toggleItem(index)}
            >
              {item}
            </label>
          </div>
        ))}
      </div>
    </div>
  );
}
