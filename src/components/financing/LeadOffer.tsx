'use client';

import { Suspense } from 'react';
import { useSearchParams } from 'next/navigation';
import TrackedLink from '@/components/TrackedLink';
import f from '@/styles/Financing.module.css';
import btn from '@/app/shop/product.module.css';
import { LEAD_CHECKOUT_URL, LEAD_PRICE } from '@/lib/financing/sponsors';

/** Same vocabulary as the match form and the newsletter worker's LEAD_LABELS. */
const LABELS: Record<string, Record<string, string>> = {
  timeline: { '0-6': 'Within 6 months', '6-12': '6–12 months', '12-18': '12–18 months', '18plus': '18+ months' },
  credit: { '740plus': '740+', '700-739': '700–739', '660-699': '660–699', 'below-660': 'Below 660', unsure: 'Not sure' },
  land: { own: 'Owns the land', 'under-contract': 'Land under contract', looking: 'Still looking for land' },
  budget: { 'under-200k': 'Under $200K', '200-400k': '$200–400K', '400-700k': '$400–700K', 'over-700k': '$700K+' },
};

function clean(v: string | null, re: RegExp, max: number) {
  return (v || '').replace(re, '').slice(0, max);
}

/**
 * The anonymized borrower card plus the pay button. Everything shown here comes
 * from the URL Seth sends (?ref=FL-3&state=TX&timeline=6-12&credit=740plus&land=own&budget=over-700k)
 * so one static page serves every introduction. Nothing identifying is ever in the URL.
 */
function LeadOfferInner() {
  const q = useSearchParams();
  const ref = clean(q.get('ref'), /[^A-Za-z0-9_-]/g, 40);
  const state = clean(q.get('state'), /[^A-Za-z]/g, 2).toUpperCase();
  const pick = (key: keyof typeof LABELS) => LABELS[key][q.get(key) || ''] || '';
  const rows = [
    { k: 'Reference', v: ref || '—', note: 'quote this in any email' },
    { k: 'State', v: state || '—', note: 'where the house will be built' },
    { k: 'Timeline', v: pick('timeline') || '—', note: 'when they expect to break ground' },
    { k: 'Credit', v: pick('credit') || '—', note: 'self-reported band' },
    { k: 'Land', v: pick('land') || '—', note: 'as of the form date' },
    { k: 'Budget', v: pick('budget') || '—', note: 'construction cost, their estimate' },
  ];
  const payHref = ref
    ? `${LEAD_CHECKOUT_URL}?client_reference_id=${encodeURIComponent(ref)}`
    : LEAD_CHECKOUT_URL;

  return (
    <>
      <div className={f.statGrid}>
        {rows.map((r) => (
          <div key={r.k} className={f.stat}>
            <span className={f.statK}>{r.k}</span>
            <span className={f.statV}>{r.v}</span>
            <span className={f.statNote}>{r.note}</span>
          </div>
        ))}
      </div>
      <p>
        <TrackedLink
          href={payHref}
          eventName="lead_purchase_click"
          eventParams={{ lead_ref: ref || 'none', state: state || 'none' }}
          className={btn.btnPrimary}
        >
          Pay ${LEAD_PRICE} and request the introduction →
        </TrackedLink>
      </p>
      <p className={f.fine}>
        Stripe checkout, card or bank. The reference number travels with the payment so the
        right borrower is attached to it. Prefer an invoice? Reply to the email you received and
        we send one through Stripe, due on receipt.
      </p>
    </>
  );
}

export default function LeadOffer() {
  return (
    <Suspense fallback={<div className={f.statGrid} aria-hidden="true" />}>
      <LeadOfferInner />
    </Suspense>
  );
}
