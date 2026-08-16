/**
 * Server-renderable scaffolding for calculator pages: hero band, content
 * sections, assumptions table, FAQ, related sheets (design spec §3.1, §7).
 */

import Link from 'next/link';
import { ReactNode } from 'react';
import s from '@/styles/CalcSheet.module.css';
import { calcHref, relatedCalcsFor } from '@/lib/calc/registry';

interface CalcHeroProps {
  title: string;
  sub: string;
  cells: { k: string; v: string }[]; // exactly 4
  /** Hub variant — no sheet overlaps the band below. */
  flat?: boolean;
}

export function CalcHero({ title, sub, cells, flat }: CalcHeroProps) {
  return (
    <section className={`${s.hero} bp-band bp-grid no-print`}>
      <span className={`${s.crop} ${s.tl}`} />
      <span className={`${s.crop} ${s.tr}`} />
      <div className={`${s.heroInner} ${flat ? s.heroInnerFlat : ''}`}>
        <p className={`bp-eyebrow ${s.eyebrow}`}>Free tool</p>
        <h1 className={s.heroTitle}>{title}</h1>
        <p className={s.heroSub}>{sub}</p>
        <div className={s.dimstrip}>
          {cells.map((c) => (
            <div key={c.k} className={s.dimcell}>
              <span className={s.k}>{c.k}</span>
              <span className={s.v}>{c.v}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

interface CalcSectionProps {
  label: string;
  title: string;
  meta?: string;
  children: ReactNode;
  last?: boolean;
  noPrint?: boolean;
}

export function CalcSection({ label, title, meta, children, last, noPrint }: CalcSectionProps) {
  return (
    <section className={`${s.block} ${last ? s.blockLast : ''} ${noPrint ? 'no-print' : ''}`}>
      <div className={s.secHead}>
        <div>
          <p className={s.secLabel}>{label}</p>
          <h2 className={s.secTitle}>{title}</h2>
        </div>
        {meta && <p className={s.secMeta}>{meta}</p>}
      </div>
      {children}
    </section>
  );
}

/** Leader-line table for assumptions ("Waste factor …… 10%"). */
export function AssumptionsTable({ rows }: { rows: { label: string; value: string }[] }) {
  return (
    <div className={s.assumptions}>
      <ul className={s.schedule}>
        {rows.map((r) => (
          <li key={r.label} className={s.schedLine}>
            <span className={s.schedKey}>{r.label}</span>
            <span className={s.schedLeader} />
            <span className={s.schedVal}>{r.value}</span>
          </li>
        ))}
      </ul>
    </div>
  );
}

export interface FAQItem {
  question: string;
  answer: ReactNode;
}

export function CalcFAQ({ items }: { items: FAQItem[] }) {
  return (
    <div className={s.faqList}>
      {items.map((f) => (
        <div key={f.question} className={s.faqItem}>
          <h3 className={s.faqQ}>{f.question}</h3>
          <p className={s.faqA}>{f.answer}</p>
        </div>
      ))}
    </div>
  );
}

/** Strip of exactly three adjacent trade calculators (spec §7). */
export function RelatedCalcs({ slug }: { slug: string }) {
  const related = relatedCalcsFor(slug).slice(0, 3);
  if (!related.length) return null;
  return (
    <div className={`${s.related} no-print`}>
      <span className={s.relatedLabel}>Related sheets</span>
      <div className={s.relatedGrid}>
        {related.map((c) => (
          <Link key={c.slug} href={calcHref(c)} className={s.relatedCell}>
            <span className={s.relatedNo}>{c.sheetNo}</span>
            <span className={s.relatedName}>{c.name}</span>
          </Link>
        ))}
      </div>
    </div>
  );
}
