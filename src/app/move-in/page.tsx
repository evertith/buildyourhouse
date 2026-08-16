import Link from 'next/link';
import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import h from '@/styles/CalcHub.module.css';
import { CalcSection } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';

export const metadata: Metadata = {
  alternates: { canonical: '/move-in' },
  title: 'Move-In — Punch List, Certificate of Occupancy & Loan Conversion',
  description:
    'The last phase of an owner-built home: finishing the punch list, earning your certificate of occupancy, converting the construction loan to a mortgage, and moving in.',
};

/** Sheet index for the move-in section, in the order the steps actually happen. */
const SHEETS: { no: string; href: string; title: string; desc: string; out: string }[] = [
  {
    no: 'MI-01',
    href: '/move-in/punch-list',
    title: 'Punch List',
    desc: 'The room-by-room walkthrough method, the items inspectors reliably catch, and how to get subs back on site to fix their own work.',
    out: '1–2 weeks',
  },
  {
    no: 'MI-02',
    href: '/move-in/certificate-of-occupancy',
    title: 'Certificate of Occupancy',
    desc: 'What the final inspection requires, the hold-ups that stall a CO, and how to get signed off without a second visit.',
    out: '1–3 days',
  },
  {
    no: 'MI-03',
    href: '/move-in/loan-conversion',
    title: 'Loan Conversion',
    desc: 'Turning the construction loan into a permanent mortgage — appraisal requirements, rate locks, timeline, and the costs to expect.',
    out: '2–4 weeks',
  },
  {
    no: 'MI-04',
    href: '/move-in/moving-in',
    title: 'Moving In',
    desc: 'Utility setup, safety checks, warranty registrations, and the first-week checklist for the house you just built.',
    out: '1 week',
  },
];

export default function MoveInHub() {
  return (
    <div className={s.calcPage}>
      <section className={`${s.hero} bp-band bp-grid no-print`}>
        <span className={`${s.crop} ${s.tl}`} />
        <span className={`${s.crop} ${s.tr}`} />
        <div className={`${s.heroInner} ${s.heroInnerFlat}`}>
          <p className={`bp-eyebrow ${s.eyebrow}`}>Section 07 — Move-In</p>
          <h1 className={s.heroTitle}>From punch list to front door key</h1>
          <p className={s.heroSub}>
            The last four steps of an owner-built house: finish the details, earn the certificate of
            occupancy, convert the loan, and move in.
          </p>
          <div className={s.dimstrip}>
            <div className={s.dimcell}>
              <span className={s.k}>Sheets</span>
              <span className={s.v}>04</span>
            </div>
            <div className={s.dimcell}>
              <span className={s.k}>Stage</span>
              <span className={s.v}>Move-in</span>
            </div>
            <div className={s.dimcell}>
              <span className={s.k}>Comes after</span>
              <span className={s.v}>Finish work</span>
            </div>
            <div className={s.dimcell}>
              <span className={s.k}>Cost</span>
              <span className={s.v}>Free</span>
            </div>
          </div>
        </div>
      </section>

      <div className={s.content}>
        <CalcSection label="Move-in sheets" title="The last four steps" meta="MI-01 — MI-04">
          <div className={s.prose}>
            <p>
              The final stretch of an owner-built house is detail work and paperwork rather than
              construction, and it is where tired builders lose weeks. Four steps stand between a
              finished house and your keys &mdash; they run roughly in this order, though the loan
              paperwork can start while the punch list is still open.
            </p>
          </div>

          <div>
            {SHEETS.map((sheet) => (
              <Link key={sheet.href} href={sheet.href} className={h.idxRow}>
                <span className={h.idxNo}>{sheet.no}</span>
                <span>
                  <span className={h.idxTitle}>{sheet.title}</span>
                  <span className={h.idxDesc}>{sheet.desc}</span>
                </span>
                <span className={h.idxOut}>{sheet.out}</span>
                <span className={h.idxGo} aria-hidden="true">
                  →
                </span>
              </Link>
            ))}
          </div>
        </CalcSection>

        <div className={`${s.block} ${s.blockLast}`}>
          <BinderCTA
            context="move-in-hub"
            lead="Punch lists, final inspection sign-offs, warranty registrations, and closeout paperwork — the binder carries the forms for this last stretch alongside the 367 pages that got you here."
          />
        </div>
      </div>
    </div>
  );
}
