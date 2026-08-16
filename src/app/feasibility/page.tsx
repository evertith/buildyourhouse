import Link from 'next/link';
import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import h from '@/styles/CalcHub.module.css';
import { CalcSection } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';

export const metadata: Metadata = {
  alternates: { canonical: '/feasibility' },
  title: 'Owner-Builder Feasibility — Should You Build Your Own House?',
  description:
    'Four checks before you commit: an honest self-assessment, a realistic savings estimate, the true time commitment, and what your state allows owner-builders to do.',
};

/** Sheet index for the feasibility section, in the order they should be run. */
const SHEETS: { no: string; href: string; title: string; desc: string; out: string }[] = [
  {
    no: 'FS-01',
    href: '/feasibility/is-it-right-for-you',
    title: 'Is Owner-Building Right for You?',
    desc: 'An honest self-assessment from a retired GC — the financial, skill, and temperament questions that decide whether you should do this at all.',
    out: 'self-assessment',
  },
  {
    no: 'FS-02',
    href: '/feasibility/cost-savings-calculator',
    title: 'Cost Savings Calculator',
    desc: 'Put a number on it. Factors in typical GC markup, the value of your own labor, and material costs to estimate what you would actually keep.',
    out: 'savings estimate',
  },
  {
    no: 'FS-03',
    href: '/feasibility/time-commitment',
    title: 'Time Commitment',
    desc: 'Realistic weekly hours and total duration, phase by phase, from someone who has actually run the schedule instead of guessing at it.',
    out: '12–18 months',
  },
  {
    no: 'FS-04',
    href: '/feasibility/state-by-state-rules',
    title: 'Owner-Builder Laws by State',
    desc: 'What your state actually lets you do — permit access, licensing thresholds, insurance requirements, and how soon you can sell.',
    out: 'state rules',
  },
];

export default function FeasibilityHub() {
  return (
    <div className={s.calcPage}>
      <section className={`${s.hero} bp-band bp-grid no-print`}>
        <span className={`${s.crop} ${s.tl}`} />
        <span className={`${s.crop} ${s.tr}`} />
        <div className={`${s.heroInner} ${s.heroInnerFlat}`}>
          <p className={`bp-eyebrow ${s.eyebrow}`}>Section 01 — Feasibility</p>
          <h1 className={s.heroTitle}>Should you build it yourself?</h1>
          <p className={s.heroSub}>
            Four honest checks &mdash; temperament, money, time, and your state&rsquo;s law &mdash;
            before you commit a dollar to an owner-built house.
          </p>
          <div className={s.dimstrip}>
            <div className={s.dimcell}>
              <span className={s.k}>Sheets</span>
              <span className={s.v}>04</span>
            </div>
            <div className={s.dimcell}>
              <span className={s.k}>Stage</span>
              <span className={s.v}>Week 1–2</span>
            </div>
            <div className={s.dimcell}>
              <span className={s.k}>Comes before</span>
              <span className={s.v}>Planning</span>
            </div>
            <div className={s.dimcell}>
              <span className={s.k}>Cost</span>
              <span className={s.v}>Free</span>
            </div>
          </div>
        </div>
      </section>

      <div className={s.content}>
        <CalcSection
          label="Feasibility checks"
          title="Four questions to answer first"
          meta="FS-01 — FS-04"
        >
          <div className={s.prose}>
            <p>
              Owner-building saves real money, but not for everyone and not in every state. These
              four checks are the ones worth running before you spend anything &mdash; a weekend
              here is what keeps a bad fit from costing you a year.
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
            context="feasibility-hub"
            lead="Decided you're doing this? The paperwork half of the job is already built: 367 print-ready pages of checklists, contracts, inspection forms, and tracking sheets, organized the way a GC organizes a build."
          />
        </div>
      </div>
    </div>
  );
}
