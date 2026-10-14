'use client';

import s from '@/styles/Estimate.module.css';
import type { Estimate } from '@/lib/estimate/estimate';
import { money100, plural } from './format';

/** Phone only: the total pinned to the top while the ledger scrolls. */
export default function StickyStrip({ estimate }: { estimate: Estimate }) {
  const t = estimate.totals;
  return (
    <div className={`${s.strip} no-print`} aria-hidden="true">
      <span>
        <span className={s.stripLabel}>Cash to build</span>
        <span className={s.stripCash}>{money100(t.cash.mid)}</span>
      </span>
      <span className={s.stripMeta}>
        {t.nDiy} {plural(t.nDiy, 'phase', 'phases')} yourself
      </span>
    </div>
  );
}
