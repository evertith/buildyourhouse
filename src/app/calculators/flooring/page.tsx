import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import FlooringCalc from '@/components/calc/FlooringCalc';
import { CalcHero, CalcSection, AssumptionsTable, CalcFAQ, RelatedCalcs } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';
import { generateFAQSchema, schemaToScriptTag } from '@/lib/schema';

export const metadata: Metadata = {
  alternates: { canonical: '/calculators/flooring' },
  title: 'Flooring Calculator — Square Feet, Waste & Box Counts',
  description:
    'How much flooring do I need? Enter square footage and get order quantities with honest waste (8–15%), box counts, and underlayment — plus a printable takeoff.',
};

const FAQS = [
  {
    question: 'How much extra flooring should I order?',
    answer:
      'For a straight lay, order 8% extra for click-together planks — LVP, laminate, engineered hardwood — and 10% extra for solid hardwood, tile, and carpet. A diagonal or herringbone layout adds 5 points on top, so plan on 13–15%. Ordering short costs more than the waste does: flooring is made in dye lots, and a box bought three weeks later often does not quite match the floor already down.',
  },
  {
    question: 'How many boxes of flooring do I need for 1,000 sq ft?',
    answer:
      'For LVP: 1,000 sq ft plus 8% waste is 1,080 sq ft to order. At the typical 23 sq ft per box, 1,080 ÷ 23 rounds up to 47 boxes. Laminate boxes run about 20 sq ft (54 boxes for the same floor), engineered and solid hardwood about 22, and tile about 15. Always divide your with-waste square footage by the coverage printed on the carton you are actually buying, then round up.',
  },
  {
    question: 'Do I need underlayment under LVP?',
    answer:
      'Floating floors — click-lock LVP, laminate, and engineered hardwood — get a foam or felt underlayment for sound and moisture control, sold in 100 sq ft rolls. But many LVP lines now ship with an attached pad, and doubling up under those voids most warranties, so skip the rolls. Tile never uses this kind of underlayment (it sets in thinset over a proper substrate), and carpet cushion is the separate pad already counted in the carpet + pad line.',
  },
  {
    question: 'How is carpet sold?',
    answer:
      'Carpet comes off 12-ft-wide rolls and is priced by the square yard — 9 sq ft. This calculator converts your with-waste square footage to square yards and rounds up. The 10% waste factor covers seam and roll-width loss: a 13-ft-wide room still consumes a full 12-ft width plus a seamed strip. Have the installer map seams away from traffic lanes and windows before you place the order.',
  },
  {
    question: 'What does flooring cost per square foot?',
    answer:
      'Materials only, August 2026 national ranges: laminate $1.50–$4, LVP $2–$5, ceramic tile $2–$6, carpet with pad $3–$7, engineered hardwood $4–$8, and solid hardwood $5–$10 per sq ft. Installed prices you see advertised bundle labor on top of that, and labor varies widely by market and subfloor condition — this calculator prices the material order only, so get install quotes separately.',
  },
];

const faqSchema = generateFAQSchema(FAQS);

export default function FlooringPage() {
  return (
    <div className={s.calcPage}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      <CalcHero
        title="Flooring Calculator"
        sub="Square footage with honest waste, box counts, and underlayment from your floor area — with the math shown, not hidden."
        cells={[
          { k: 'Sheet', v: 'TO-06' },
          { k: 'Returns', v: 'Sq ft + boxes' },
          { k: 'Waste', v: '8–15%' },
          { k: 'Basis', v: 'By material' },
        ]}
      />

      <div className={s.sheetWrap}>
        <FlooringCalc />
      </div>

      <div className={s.content}>
        <CalcSection label="Methodology" title="How this takeoff is figured" meta="SHEET TO-06">
          <div className={s.prose}>
            <p>
              <strong>Waste.</strong> Click-together planks — LVP, laminate, engineered
              hardwood — get 8% cut waste on a straight lay. Solid hardwood, tile, and carpet get
              10%. A diagonal or herringbone layout adds 5 points on top of either — the classic
              reason DIY orders come up short.
            </p>
            <p>
              <strong>Boxes.</strong> Order square footage divided by typical retail box coverage,
              rounded up: 23 sq ft per box for LVP, 20 for laminate, 22 for engineered and solid
              hardwood, 15 for tile. Coverage varies by product line, so check the carton you are
              buying before you place the order.
            </p>
            <p>
              <strong>Carpet.</strong> Sold by the square yard from 12-ft rolls, so the sheet
              converts your with-waste footage to square yards (÷ 9) and rounds up. The waste
              factor covers seams and roll-width loss — plan seam locations before ordering.
            </p>
            <p>
              <strong>Underlayment.</strong> Floating plank floors get foam or felt rolls at
              100 sq ft each — floor area ÷ 100, rounded up. Skipped when your planks have an
              attached pad, and never added for tile or carpet.
            </p>
            <p>
              <strong>Tile setting.</strong> One 50-lb bag of thinset per ~50 sq ft with a
              1/4&quot; × 3/8&quot; trowel. Grout, backer board, and leveler are separate line
              items sized from your tile and substrate.
            </p>
            <p>
              <strong>What&apos;s not here.</strong> Transitions, stair nosing, and baseboard.
              Keep one unopened box for future repairs — flooring is made in dye lots, and a
              match ordered later is a gamble. Wood and laminate need 48–72 hours acclimating on
              site before install. The <a href="/calculators/paint">paint calculator</a> covers
              the walls above this floor.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Assumptions" title="Waste, coverage, and rolls" meta="ADJUST ABOVE">
          <AssumptionsTable
            rows={[
              { label: 'Waste — LVP, laminate, engineered', value: '8%' },
              { label: 'Waste — hardwood, tile, carpet', value: '10%' },
              { label: 'Diagonal / herringbone', value: '+5 points' },
              { label: 'Box coverage — LVP', value: '23 sq ft' },
              { label: 'Box coverage — laminate', value: '20 sq ft' },
              { label: 'Box coverage — hardwood', value: '22 sq ft' },
              { label: 'Box coverage — tile', value: '15 sq ft' },
              { label: 'Carpet', value: '12-ft roll, sold by sq yd' },
              { label: 'Underlayment roll', value: '100 sq ft' },
              { label: 'Thinset', value: '1 bag per ~50 sq ft' },
              { label: 'Prices', value: 'National range, Aug 2026' },
            ]}
          />
        </CalcSection>

        <CalcSection label="Questions" title="Owner-builders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS.map((f) => ({ question: f.question, answer: f.answer }))} />
        </CalcSection>

        <RelatedCalcs slug="flooring" />

        <div className={`${s.block} ${s.blockLast} no-print`}>
          <BinderCTA
            context="calc-flooring"
            lead="The binder's finish-phase section holds your flooring order logs and delivery tracking sheets — where this takeoff turns into orders and the orders get checked at the curb. 367 pages of job-site paperwork, organized the way a GC runs a build."
          />
        </div>
      </div>
    </div>
  );
}
