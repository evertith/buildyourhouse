import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import PaintCalc from '@/components/calc/PaintCalc';
import { CalcHero, CalcSection, AssumptionsTable, CalcFAQ, RelatedCalcs } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';
import { generateFAQSchema, schemaToScriptTag } from '@/lib/schema';

export const metadata: Metadata = {
  alternates: { canonical: '/calculators/paint' },
  title: 'Paint Calculator — Gallons for Walls, Ceilings & Trim',
  description:
    'How much paint do I need? Enter room size or floor area and get gallons for walls, ceilings, primer, and trim — coverage math shown, plus a printable takeoff.',
};

const FAQS = [
  {
    question: 'How much paint for a 12×12 room?',
    answer:
      'A 12 × 12 room with 8-ft ceilings has 384 sq ft of wall — 2 × (12 + 12) × 8. Deduct 21 sq ft for the door and 15 for each of two windows and you are down to about 333 sq ft. Two coats means covering 666 sq ft, and at 350 sq ft per gallon that rounds up to 2 gallons of wall paint. Painting the 144 sq ft ceiling too adds one more gallon for two coats.',
  },
  {
    question: 'How many square feet does a gallon of paint cover?',
    answer:
      'The number on every can — and the one this calculator uses — is 350 sq ft per gallon per coat on smooth drywall. Textured surfaces run about 25% lower, so on knockdown or orange peel figure closer to 260 sq ft per gallon. Primer spreads about 15% worse on bare board than paint does on a sealed wall, roughly 300 sq ft per gallon.',
  },
  {
    question: 'Do I really need primer on new drywall?',
    answer:
      'Yes — on fresh drywall it is non-negotiable. Unprimed board flashes the joints through the finish: paper face and joint compound absorb paint at different rates, so every seam and screw head reads as a dull or shiny stripe under the topcoat, no matter how many coats you roll. One coat of PVA drywall primer ($18–$28 a gallon) seals the whole surface to one porosity, and your finish coats behave the same everywhere.',
  },
  {
    question: 'One coat or two?',
    answer:
      'Two coats is the honest default for color changes and new drywall — one coat of even premium paint rarely hides a color shift, and primer is not a finish coat. The one-coat case is a refresh in the same color and sheen on walls already in good shape. When in doubt, buy for two: an unopened gallon can go back to the store, but a Saturday spent re-rolling a streaky wall cannot.',
  },
  {
    question: 'How much does it cost to paint a house interior yourself?',
    answer:
      'Materials are what this takeoff prices: quality interior latex runs $38–$65 a gallon as of August 2026, primer $18–$28, and trim enamel $45–$70. Add $50–$150 for a first-time setup of brushes, rollers, tape, and drop cloths. Hiring it out typically runs $2–$6 per square foot of floor area — the gap is labor, and painting is the finish trade where owner-builder labor most reliably substitutes for a pro, if you accept that prep and cutting-in take longer than the rolling.',
  },
];

const faqSchema = generateFAQSchema(FAQS);

export default function PaintPage() {
  return (
    <div className={s.calcPage}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      <CalcHero
        title="Paint Calculator"
        sub="Gallons for walls, ceilings, primer, and trim — one room or the whole house, with the coverage math shown, not hidden."
        cells={[
          { k: 'Sheet', v: 'TO-05' },
          { k: 'Returns', v: 'Gallons' },
          { k: 'Coverage', v: '350 ft²/gal' },
          { k: 'Coats', v: '1–2' },
        ]}
      />

      <div className={s.sheetWrap}>
        <PaintCalc />
      </div>

      <div className={s.content}>
        <CalcSection label="Methodology" title="How this takeoff is figured" meta="SHEET TO-05">
          <div className={s.prose}>
            <p>
              <strong>Wall area, one room.</strong> Perimeter times height: 2 × (length + width) ×
              ceiling height, then 21 sq ft deducted per door and 15 per window. A 12 × 12 room
              with 8-ft ceilings, one door, and two windows nets about 333 sq ft of paintable wall.
            </p>
            <p>
              <strong>Wall area, whole house.</strong> Paintable wall area is estimated at 2.7 ×
              floor area — the industry heuristic for whole-interior repaints of typical layouts.
              It bakes in interior partitions (painted on both sides) less the openings, closets,
              and tile you will not paint.
            </p>
            <p>
              <strong>Gallons.</strong> Area × coats ÷ 350 sq ft per gallon, rounded up to whole
              cans. That 350 is the coverage printed on the can and holds on smooth drywall —
              textured walls drink roughly 25% more.
            </p>
            <p>
              <strong>Primer.</strong> New drywall gets one coat of PVA primer over every wall and
              ceiling. Primer spreads about 15% worse on bare board than paint on a sealed
              surface — figure roughly 300 sq ft per gallon instead of 350.
            </p>
            <p>
              <strong>Trim.</strong> Enamel for doors, casing, and base is estimated at about half
              a gallon per 150 sq ft of floor per coat, rounded to the nearest half gallon with a
              one-gallon minimum — trim is cut-in work, and coverage per gallon matters less than
              having enough to finish every side of every door.
            </p>
            <p>
              <strong>What&apos;s not here.</strong> Exterior paint, cabinet finishing, wallpaper, and
              labor. If you are still hanging board, run the{' '}
              <a href="/calculators/drywall">drywall calculator</a> first — its square footage is
              the same one this sheet paints.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Assumptions" title="Coverage, deductions, and prices" meta="ADJUST ABOVE">
          <AssumptionsTable
            rows={[
              { label: 'Coverage', value: '350 sq ft/gal per coat' },
              { label: 'Textured surfaces', value: '~25% more paint' },
              { label: 'Door deduction', value: '21 sq ft each' },
              { label: 'Window deduction', value: '15 sq ft each' },
              { label: 'Whole-house wall area', value: '2.7 × floor area' },
              { label: 'Primer coverage', value: '~300 sq ft/gal on bare board' },
              { label: 'Trim enamel', value: '0.5 gal per 150 sq ft floor' },
              { label: 'Wall paint', value: '$38–$65/gal, Aug 2026' },
            ]}
          />
        </CalcSection>

        <CalcSection label="Questions" title="Owner-builders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS.map((f) => ({ question: f.question, answer: f.answer }))} />
        </CalcSection>

        <RelatedCalcs slug="paint" />

        <div className={`${s.block} ${s.blockLast} no-print`}>
          <BinderCTA
            context="calc-paint"
            lead="The binder's finish-phase section holds the room-by-room paint checklists and punch-list sheets this takeoff feeds — the paperwork that gets the last 10% of the build actually finished. 367 pages, organized the way a GC runs a build."
          />
        </div>
      </div>
    </div>
  );
}
