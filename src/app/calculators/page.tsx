import Link from 'next/link';
import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import h from '@/styles/CalcHub.module.css';
import { CalcHero, CalcSection } from '@/components/calc/sections';
import { CALCULATORS } from '@/lib/calc/registry';
import BinderCTA from '@/components/BinderCTA';

export const metadata: Metadata = {
  alternates: { canonical: '/calculators' },
  title: 'Free Construction Calculators — Framing, Drywall, Concrete & More',
  description:
    'Eleven free calculators for owner-builders: framing lumber, drywall, concrete, roofing, paint, flooring, insulation, plus cost, timeline, and budget worksheets. Formulas shown, no signup.',
};

/** Output summaries for the index rows ("studs · plates · sheathing"). */
const OUTPUTS: Record<string, string> = {
  'framing-lumber': 'studs · plates · sheathing',
  drywall: 'sheets · mud · tape',
  'concrete-slab': 'yards · bags · rebar',
  roofing: 'squares · bundles · underlay',
  paint: 'gallons · primer · trim',
  flooring: 'sq ft · boxes · underlay',
  insulation: 'batt bags · blown-in bags',
};

const WORKSHEETS = [
  {
    no: 'W-01',
    href: '/feasibility/cost-savings-calculator',
    title: 'Cost Savings Calculator',
    desc: 'Gut-check whether owner-building pencils out: the GC fee you avoid, honestly separated from the value of your own hours.',
    out: 'savings · GC fee',
  },
  {
    no: 'W-02',
    href: '/calculators/material-estimator',
    title: 'Whole-House Material Estimator',
    desc: 'Planning-level quantities for the entire build — concrete through insulation — from square footage and finish level.',
    out: 'all majors · total cost',
  },
  {
    no: 'W-03',
    href: '/calculators/timeline-estimator',
    title: 'Timeline Estimator',
    desc: 'A realistic build schedule from your hours per week, DIY share, and experience — phase by phase.',
    out: 'months · phases',
  },
  {
    no: 'W-04',
    href: '/calculators/budget-tracker',
    title: 'Budget Tracker',
    desc: 'Budget vs. actual by phase, with contingency burn — so overruns surface early instead of at the end.',
    out: 'variance · contingency',
  },
];

export default function CalculatorsPage() {
  return (
    <div className={s.calcPage}>
      <CalcHero
        flat
        title="Owner-Builder Calculators"
        sub="Takeoff sheets for the materials that dominate your budget — quantities first, cost ranges second, every formula shown."
        cells={[
          { k: 'Sheets', v: '11 tools' },
          { k: 'Signup', v: 'None' },
          { k: 'Formulas', v: 'Shown' },
          { k: 'Output', v: 'Print-ready' },
        ]}
      />

      <div className={s.content}>
        <CalcSection
          label="Takeoff sheets"
          title="One sheet per trade"
          meta="TO-01 — TO-07"
        >
          <div>
            {CALCULATORS.map((c) => (
              <Link key={c.slug} href={`/calculators/${c.slug}`} className={h.idxRow}>
                <span className={h.idxNo}>{c.sheetNo}</span>
                <span>
                  <span className={h.idxTitle}>{c.name}</span>
                  <span className={h.idxDesc}>{c.blurb}</span>
                </span>
                <span className={h.idxOut}>{OUTPUTS[c.slug]}</span>
                <span className={h.idxGo} aria-hidden="true">→</span>
              </Link>
            ))}
          </div>
        </CalcSection>

        <CalcSection
          label="Planning worksheets"
          title="The whole-build numbers"
          meta="W-01 — W-04"
        >
          <div>
            {WORKSHEETS.map((w) => (
              <Link key={w.href} href={w.href} className={h.idxRow}>
                <span className={h.idxNo}>{w.no}</span>
                <span>
                  <span className={h.idxTitle}>{w.title}</span>
                  <span className={h.idxDesc}>{w.desc}</span>
                </span>
                <span className={h.idxOut}>{w.out}</span>
                <span className={h.idxGo} aria-hidden="true">→</span>
              </Link>
            ))}
          </div>
        </CalcSection>

        <div className={`${s.block} ${s.blockLast}`}>
          <BinderCTA
            context="calculators-hub"
            lead="Every takeoff these sheets produce has a home in the binder: materials logs, quote comparisons, delivery tracking, and inspection checklists — 367 pages of the paperwork that runs a build."
          />
        </div>
      </div>
    </div>
  );
}
