import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import RoofingCalc from '@/components/calc/RoofingCalc';
import { CalcHero, CalcSection, AssumptionsTable, CalcFAQ, RelatedCalcs } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';
import { generateFAQSchema, schemaToScriptTag } from '@/lib/schema';

export const metadata: Metadata = {
  alternates: { canonical: '/calculators/roofing' },
  title: 'Roofing Calculator — Squares, Bundles & Underlayment',
  description:
    'How many squares is my roof? Enter footprint and pitch for shingle bundles, underlayment, starter, and cap — with the pitch math shown and a printable takeoff.',
};

const FAQS = [
  {
    question: 'How many squares is a 2,000 sq ft house roof?',
    answer:
      'It depends on the footprint, not the living area. A 40 × 30 ft single-story at 6/12 pitch with 1-ft overhangs works out to a 42 × 32 plan (1,344 sq ft), times a 1.118 pitch factor, plus 10% gable waste — about 16.6 squares to order. A 2,000 sq ft single-story (50 × 40 footprint) at the same settings runs about 26.9 squares, but a 2,000 sq ft two-story has roughly a 1,000 sq ft footprint, so two stories roughly halve the roof.',
  },
  {
    question: 'How many bundles of shingles per square?',
    answer:
      'Three. Architectural shingles are packaged so three bundles cover one square (100 sq ft of roof), and that is what this calculator uses, rounded up to whole bundles on the waste-added area — so a 16.6-square order comes to 50 bundles. Some heavyweight and specialty shingles run four or five bundles per square; check the wrapper before you order.',
  },
  {
    question: 'What does roof pitch do to material quantities?',
    answer:
      'Flat plan area gets multiplied by √(1 + (rise/12)²) to become sloped surface. At 4/12 the factor is 1.054 — barely more than flat. At 6/12 it is 1.118, at 8/12 it is 1.202, and at 12/12 it reaches 1.414 — the same footprint needs about 34% more shingles at 12/12 than at 4/12. Pitch hits labor even harder: above about 7/12, most crews charge steep-roof rates.',
  },
  {
    question: 'How much waste should I add for a hip roof?',
    answer:
      '15% — this calculator uses 15% for hips against 10% for a simple gable. Every hip is a long diagonal cut line where shingle ends get trimmed off and thrown away, and hips also consume more cap: the math here figures roughly 1.6× the house length in ridge-and-hip cap for a hip roof versus a single gable ridge. For a cut-up roof with multiple hips, valleys, and dormers, use the 20% setting.',
  },
  {
    question: "What's not in this estimate?",
    answer:
      'Ice & water shield — required by code at eaves and valleys in cold climates, with one roll covering about 65 lf of eave — plus flashing, pipe boots, vents, labor, and tear-off disposal. Those depend on your climate, your code, and what is on the roof now, so price them from your plans and a roof-top look, not a footprint.',
  },
];

const faqSchema = generateFAQSchema(FAQS);

export default function RoofingPage() {
  return (
    <div className={s.calcPage}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      <CalcHero
        title="Roofing Calculator"
        sub="Squares, shingle bundles, underlayment, starter, and cap from your footprint and pitch — with the math shown, not hidden."
        cells={[
          { k: 'Sheet', v: 'TO-04' },
          { k: 'Returns', v: 'Squares + bundles' },
          { k: 'Basis', v: 'Pitch factored' },
          { k: 'Waste', v: '10–20%' },
        ]}
      />

      <div className={s.sheetWrap}>
        <RoofingCalc />
      </div>

      <div className={s.content}>
        <CalcSection label="Methodology" title="How this takeoff is figured" meta="SHEET TO-04">
          <div className={s.prose}>
            <p>
              <strong>Roof area.</strong> Plan area is the footprint plus overhang on all four
              sides: (length + 2 × overhang) × (width + 2 × overhang). That flat area is then
              multiplied by the pitch factor √(1 + (rise/12)²) to become sloped surface —
              4/12 → 1.054, 6/12 → 1.118, 8/12 → 1.202, 12/12 → 1.414.
            </p>
            <p>
              <strong>Waste.</strong> A simple gable gets 10%, hips and valleys 15%, and a cut-up
              roof 20% — every hip, valley, and dormer is a cut line that throws away shingle
              ends. Shingles and nails are figured on the waste-added area; underlayment gets its
              own 10% for laps instead.
            </p>
            <p>
              <strong>Shingles and underlayment.</strong> Architectural shingles at 3 bundles per
              square, rounded up to whole bundles. Synthetic underlayment comes in 10-square
              rolls, sized to the roof area plus 10% for laps.
            </p>
            <p>
              <strong>Starter, cap, and drip edge.</strong> Starter strip runs the eaves and
              rakes — approximated with the plan perimeter, at 105 lf per bundle, with 5% added
              on hip roofs where every edge is an eave. Ridge and hip cap covers ~33 lf per
              bundle: a gable needs cap roughly the house length, hips multiply that by 1.6, and
              a cut-up roof by 2.1. Drip edge is the full perimeter plus 5% laps, in 10-ft
              aluminum sticks.
            </p>
            <p>
              <strong>Nails.</strong> 2.5 lb of 1¼&quot; coil roofing nails per square — about 320
              nails.
            </p>
            <p>
              <strong>L-shaped houses.</strong> The math assumes a rectangle. For an L or T, run
              each wing through the calculator separately and add the takeoffs — the ridge and
              valley lines will differ, which is also why the waste setting matters more on those
              roofs.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Assumptions" title="Coverage, waste, and pricing" meta="ADJUST ABOVE">
          <AssumptionsTable
            rows={[
              { label: 'Pitch factor', value: '√(1 + (rise/12)²)' },
              { label: 'Waste', value: 'Gable 10% · hips 15% · cut-up 20%' },
              { label: 'Shingle coverage', value: '3 bundles per square' },
              { label: 'Underlayment roll', value: '10 squares, +10% laps' },
              { label: 'Starter strip', value: '105 lf per bundle' },
              { label: 'Ridge & hip cap', value: '~33 lf per bundle' },
              { label: 'Coil nails', value: '2.5 lb per square' },
              { label: 'Shingle bundle', value: '$34–$48, Aug 2026' },
            ]}
          />
        </CalcSection>

        <CalcSection label="Questions" title="Owner-builders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS.map((f) => ({ question: f.question, answer: f.answer }))} />
        </CalcSection>

        <RelatedCalcs slug="roofing" />

        <div className={`${s.block} ${s.blockLast} no-print`}>
          <BinderCTA
            context="calc-roofing"
            lead="The binder's roofing section holds the inspection checklist and delivery logs this takeoff feeds — bundle counts against the delivery, dry-in and final walk on the checklist. 367 pages of job-site paperwork, organized the way a GC runs a build."
          />
        </div>
      </div>
    </div>
  );
}
