'use client';

import React from 'react';
import styles from '@/styles/components/ProductPick.module.css';
import { amazonProductUrl, amazonSearchUrl } from '@/lib/affiliate';
import { trackEvent } from '@/lib/analytics';

interface ProductPickProps {
  /** Product name shown as the headline link. */
  name: string;
  /** Direct product link by ASIN. Takes precedence over `search`. */
  asin?: string;
  /** Search query for an evergreen tagged link. Falls back to `name`. */
  search?: string;
  /** Small eyebrow label, e.g. "Power Tools — buy first". */
  category?: string;
  /** The "why we recommend it" copy. */
  children?: React.ReactNode;
}

/**
 * Contextual product recommendation card for MDX content.
 * Intentionally shows NO price — the Amazon Operating Agreement forbids
 * displaying prices not pulled live via the Product Advertising API.
 */
export default function ProductPick({ name, asin, search, category, children }: ProductPickProps) {
  const href = asin ? amazonProductUrl(asin) : amazonSearchUrl(search ?? name);
  const rel = 'sponsored nofollow noopener noreferrer';
  const handleClick = () =>
    trackEvent('affiliate_click', {
      destination: 'amazon',
      component: 'product_pick',
      product: asin ?? search ?? name,
    });
  return (
    <div className={styles.pick}>
      {category && <span className={styles.eyebrow}>{category}</span>}
      <a className={styles.name} href={href} target="_blank" rel={rel} onClick={handleClick}>
        {name}
      </a>
      {children && <div className={styles.why}>{children}</div>}
      <div className={styles.footerRow}>
        <a className={styles.cta} href={href} target="_blank" rel={rel} onClick={handleClick}>
          Check price on Amazon →
        </a>
        <span className={styles.disclosure}>Affiliate link — we may earn a commission</span>
      </div>
    </div>
  );
}
