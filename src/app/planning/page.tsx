import Link from 'next/link';
import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import h from '@/styles/CalcHub.module.css';
import { CalcSection } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';

export const metadata: Metadata = {
  alternates: { canonical: '/planning' },
  title: 'Planning an Owner-Built Home — Land, Loans, Plans, Budget & Schedule',
  description:
    'The five planning decisions that set up an owner-built house: securing land, getting construction financing, choosing house plans, building a real budget, and drafting the schedule.',
};

/** Sheet index for the planning section, in the order they should be worked. */
const SHEETS: { no: string; href: string; title: string; desc: string; out: string }[] = [
  {
    no: 'PL-01',
    href: '/planning/secure-land',
    title: 'Securing Land',
    desc: 'Finding and evaluating a buildable lot — zoning verification, utility access, soil testing, and the due diligence that prevents expensive surprises.',
    out: '2–6 months',
  },
  {
    no: 'PL-02',
    href: '/planning/financing',
    title: 'Construction Financing',
    desc: 'How construction loans work for owner-builders: lender requirements, down payments, draw schedules, and the alternatives when banks say no.',
    out: '4–12 weeks',
  },
  {
    no: 'PL-03',
    href: '/planning/house-plans',
    title: 'House Plans',
    desc: 'Stock plans versus custom design, what modifications really cost, and exactly which drawings your permit office will require.',
    out: '4–16 weeks',
  },
  {
    no: 'PL-04',
    href: '/planning/budget',
    title: 'Construction Budget',
    desc: 'Cost breakdowns by phase, how much contingency to carry, and the tracking that keeps a 20% overrun from sneaking up on you.',
    out: '2–4 weeks',
  },
  {
    no: 'PL-05',
    href: '/planning/timeline',
    title: 'Project Timeline',
    desc: 'Phase durations, scheduling dependencies, and the buffer strategy that keeps a realistic build schedule from quietly slipping.',
    out: '1–2 weeks',
  },
];

export default function PlanningHub() {
  return (
    <div className={s.calcPage}>
      <section className={`${s.hero} bp-band bp-grid no-print`}>
        <span className={`${s.crop} ${s.tl}`} />
        <span className={`${s.crop} ${s.tr}`} />
        <div className={`${s.heroInner} ${s.heroInnerFlat}`}>
          <p className={`bp-eyebrow ${s.eyebrow}`}>Section 02 — Planning</p>
          <h1 className={s.heroTitle}>Plan the build before you break ground</h1>
          <p className={s.heroSub}>
            Land, financing, drawings, budget, schedule &mdash; the five decisions that set the
            ceiling on everything that comes after them.
          </p>
          <div className={s.dimstrip}>
            <div className={s.dimcell}>
              <span className={s.k}>Sheets</span>
              <span className={s.v}>05</span>
            </div>
            <div className={s.dimcell}>
              <span className={s.k}>Stage</span>
              <span className={s.v}>Month 1–3</span>
            </div>
            <div className={s.dimcell}>
              <span className={s.k}>Comes before</span>
              <span className={s.v}>Permitting</span>
            </div>
            <div className={s.dimcell}>
              <span className={s.k}>Cost</span>
              <span className={s.v}>Free</span>
            </div>
          </div>
        </div>
      </section>

      <div className={s.content}>
        <CalcSection label="Planning sheets" title="Five decisions, in order" meta="PL-01 — PL-05">
          <div className={s.prose}>
            <p>
              Planning is the cheapest place in the whole project to make a mistake. Every decision
              below is close to free to change now and expensive to change once the footings are
              poured &mdash; and each one feeds the next, so work them roughly in this order.
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
            context="planning-hub"
            lead="The budget, schedule, and quote comparisons you build here need somewhere to live once the job starts. The Job Site Binder is 367 print-ready pages of exactly that paperwork, organized the way a GC organizes a job."
          />
        </div>
      </div>
    </div>
  );
}
