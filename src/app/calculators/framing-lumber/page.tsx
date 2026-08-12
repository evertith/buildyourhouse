import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import FramingCalc from '@/components/calc/FramingCalc';
import { CalcHero, CalcSection, AssumptionsTable, CalcFAQ, RelatedCalcs } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';
import { generateFAQSchema, schemaToScriptTag } from '@/lib/schema';

export const metadata: Metadata = {
  alternates: { canonical: '/calculators/framing-lumber' },
  title: 'Framing Lumber Calculator — Studs, Plates & Sheathing Counts',
  description:
    'How many studs to frame a house? Enter your footprint and get stud counts, plate boards, headers, and OSB sheets — with the formulas shown, plus a printable takeoff.',
};

const FAQS = [
  {
    question: 'How many studs do I need per linear foot of wall?',
    answer:
      'At 16" on-center spacing, estimators use one stud per linear foot of wall. The pure spacing math gives 0.75 per foot, but corners, T-intersections, king and jack studs at openings, and blocking eat the difference — one per foot is the shortcut that comes out right on real jobs. At 24" on-center, use 0.75 per foot.',
  },
  {
    question: 'How much lumber does it take to frame a 2,000 sq ft house?',
    answer:
      'For a single-story 2,000 sq ft footprint (say 50 × 40 ft), this calculator lands around 680 studs plus roughly 135 plate boards and 60–70 sheets of OSB for the walls. Floor joists, beams, and roof framing are on top of that — wall framing is typically only about a third of total framing lumber.',
  },
  {
    question: 'Should I frame at 16" or 24" on-center?',
    answer:
      'Most single-family walls are framed 16" on-center with 2×4s. 24" on-center ("advanced framing") saves roughly a quarter of the studs and lets more insulation into the wall, but nearly all codes require 2×6 studs at that spacing for structural walls, and drywall needs to be 5/8" or attached with care to avoid waviness. If you are not sure, 16" is the safe default your inspector sees every day.',
  },
  {
    question: 'What is a precut stud, and why is it 92⅝ inches?',
    answer:
      'A precut stud is cut at the mill so that stud + one bottom plate + two top plates lands exactly at a standard ceiling height: 92⅝" gives you an 8-ft wall after drywall. You pay less than for a 96" board and skip a cut on every stud. For 9-ft walls buy 104⅝", for 10-ft walls 116⅝".',
  },
  {
    question: 'How much does it cost to frame a house?',
    answer:
      'This calculator prices wall-framing materials only — studs, plates, headers, and sheathing — using August 2026 national big-box ranges. Framing labor typically runs $6–$12 per square foot on top of materials if you hire it out, and lumber prices swing hard by region and season, so treat the range here as a starting point and get quotes from a local lumberyard, not just the big boxes.',
  },
];

const faqSchema = generateFAQSchema(FAQS);

export default function FramingLumberPage() {
  return (
    <div className={s.calcPage}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      <CalcHero
        title="Framing Lumber Calculator"
        sub="Studs, plates, headers, and sheathing from your wall dimensions — with the math shown, not hidden."
        cells={[
          { k: 'Sheet', v: 'TO-01' },
          { k: 'Returns', v: 'Quantities' },
          { k: 'Scope', v: 'Wall framing' },
          { k: 'Waste', v: 'Included' },
        ]}
      />

      <div className={s.sheetWrap}>
        <FramingCalc />
      </div>

      <div className={s.content}>
        <CalcSection label="Methodology" title="How this takeoff is figured" meta="SHEET TO-01">
          <div className={s.prose}>
            <p>
              <strong>Studs.</strong> Wall length in feet × 1 stud (16&quot; on-center) or × 0.75
              (24&quot; on-center). That multiplier is the standard estimating shortcut: nominal
              spacing alone would undercount, because every corner, channel, opening, and run of
              blocking adds sticks. Interior partitions are estimated at 1 linear foot of wall per
              4 sq ft of floor — a typical stick-built layout — and framed with 2×4s regardless of
              exterior wall size.
            </p>
            <p>
              <strong>Plates.</strong> Every wall gets a single bottom plate and a doubled top
              plate — three runs of plate stock — bought as 16-ft boards with 5% cut waste.
            </p>
            <p>
              <strong>Headers.</strong> One door or window per ~120 sq ft of floor is a typical
              opening density; each opening carries one 8-ft 2×10 (a doubled header for a 3-ft
              opening). Wide openings and garage doors need engineered headers — size those from
              your plans, not a calculator.
            </p>
            <p>
              <strong>Sheathing.</strong> Exterior wall area (perimeter × wall height × stories)
              divided into 4×8 sheets of 7/16&quot; OSB, plus 10% for cuts and gable-end waste.
            </p>
            <p>
              <strong>What&apos;s not here.</strong> Floor joists, beams, roof framing, fasteners, and
              house wrap. Wall framing is usually about a third of a house&apos;s total framing
              package — the <a href="/calculators/material-estimator">whole-house material estimator</a> covers
              the rest at the planning level.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Assumptions" title="Waste, spacing, and coverage" meta="ADJUST ABOVE">
          <AssumptionsTable
            rows={[
              { label: 'Stud count, 16" OC', value: '1.0 per lf of wall' },
              { label: 'Stud count, 24" OC', value: '0.75 per lf of wall' },
              { label: 'Interior partitions', value: '1 lf per 4 sq ft floor' },
              { label: 'Plate runs', value: '3 × wall length + 5%' },
              { label: 'Openings', value: '1 per 120 sq ft floor' },
              { label: 'Sheathing waste', value: '10%' },
              { label: 'Prices', value: 'National range, Aug 2026' },
            ]}
          />
        </CalcSection>

        <CalcSection label="Questions" title="Owner-builders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS.map((f) => ({ question: f.question, answer: f.answer }))} />
        </CalcSection>

        <RelatedCalcs slug="framing-lumber" />

        <div className={`${s.block} ${s.blockLast} no-print`}>
          <BinderCTA
            context="calc-framing-lumber"
            lead="The binder's materials section holds your takeoffs, quotes, and delivery logs — the sheets this calculator fills in. 367 pages of job-site paperwork, organized the way a GC runs a build."
          />
        </div>
      </div>
    </div>
  );
}
