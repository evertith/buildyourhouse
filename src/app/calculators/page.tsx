import Link from 'next/link';
import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import h from '@/styles/CalcHub.module.css';
import { CalcHero, CalcSection } from '@/components/calc/sections';
import { CALCULATORS, calcHref } from '@/lib/calc/registry';
import BinderCTA from '@/components/BinderCTA';

export const metadata: Metadata = {
  alternates: { canonical: '/calculators' },
  title: 'Free Construction Calculators — Framing, Drywall, Concrete & More',
  description:
    'Eleven free calculators for owner-builders: framing lumber, drywall, concrete, roofing, paint, flooring, insulation, plus cost, timeline, and budget worksheets — and a site plan drawing tool. Formulas shown, no signup.',
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
  'cost-savings-calculator': 'savings · GC fee',
  'material-estimator': 'all majors · total cost',
  'timeline-estimator': 'months · phases',
  'budget-tracker': 'variance · contingency',
};

const TAKEOFFS = CALCULATORS.filter((c) => (c.kind ?? 'takeoff') === 'takeoff');
const WORKSHEETS = CALCULATORS.filter((c) => c.kind === 'worksheet');

export default function CalculatorsPage() {
  return (
    <div className={s.calcPage}>
      <CalcHero
        flat
        title="Owner-Builder Calculators"
        sub="Takeoff sheets for the materials that dominate your budget — quantities first, cost ranges second, every formula shown."
        cells={[
          { k: 'Sheets', v: '12 tools' },
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
            {TAKEOFFS.map((c) => (
              <Link key={c.slug} href={calcHref(c)} className={h.idxRow}>
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
              <Link key={w.slug} href={calcHref(w)} className={h.idxRow}>
                <span className={h.idxNo}>{w.sheetNo}</span>
                <span>
                  <span className={h.idxTitle}>{w.name}</span>
                  <span className={h.idxDesc}>{w.blurb}</span>
                </span>
                <span className={h.idxOut}>{OUTPUTS[w.slug]}</span>
                <span className={h.idxGo} aria-hidden="true">→</span>
              </Link>
            ))}
          </div>
        </CalcSection>

        <CalcSection
          label="Drawing sheets"
          title="Draw it, don't just count it"
          meta="SP-01"
        >
          <div>
            <Link href="/site-plan-studio" className={h.idxRow}>
              <span className={h.idxNo}>SP-01</span>
              <span>
                <span className={h.idxTitle}>Site Plan Studio</span>
                <span className={h.idxDesc}>
                  Draw your lot, house, well, septic and driveway to scale,
                  check your state&rsquo;s separation distances, and print a
                  letter-size plot plan for the permit application.
                </span>
              </span>
              <span className={h.idxOut}>plot plan &middot; to scale</span>
              <span className={h.idxGo} aria-hidden="true">&rarr;</span>
            </Link>
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
