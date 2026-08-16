import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import MaterialEstimatorCalc from '@/components/calc/MaterialEstimatorCalc';
import { CalcHero, CalcSection, AssumptionsTable, CalcFAQ, RelatedCalcs } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';
import { generateFAQSchema, schemaToScriptTag } from '@/lib/schema';

export const metadata: Metadata = {
  alternates: { canonical: '/calculators/material-estimator' },
  title: 'Building Material Cost Calculator — Whole-House Estimator',
  description:
    'How much do materials cost to build a house? Estimate lumber, concrete, drywall, roofing, flooring, and insulation quantities and costs from your square footage — free, no signup.',
};

const FAQS = [
  {
    question: 'How much do materials cost to build a house?',
    answer:
      'For a 2,000 sq ft single-story home with a hip roof and standard finishes, this calculator lands near $50,000 in shell materials — about $25 a square foot — with a realistic range of roughly $39,000 to $61,000 depending on where you buy and when. That covers concrete, framing lumber, drywall, roofing, flooring, and insulation only. Windows, doors, cabinets, appliances, HVAC, electrical, plumbing, and exterior finishes are all on top of it, and they typically add more than the shell costs.',
  },
  {
    question: 'What percentage of a build budget is materials?',
    answer:
      'Materials usually run 40–50% of hard construction cost on a conventionally built house, with labor taking most of the rest. That is exactly why owner-building pencils out for some people: you cannot negotiate lumber down 30%, but you can replace a general contractor fee and some subcontracted labor with your own hours. Materials are the part of the budget you can plan precisely — labor is the part you can trade for time.',
  },
  {
    question: 'How many board feet of lumber does a 2,000 sq ft house need?',
    answer:
      'About 14,000 board feet for a single-story 2,000 sq ft home with 8 ft walls — roughly 7 board feet per finished square foot, which is the standard rule of thumb for light wood framing. That total covers wall studs and plates, exterior sheathing, floor joists, subfloor, and roof framing with its deck, plus 15% waste. The same 2,000 sq ft built as a two-story comes in lower — around 6.3 board feet per square foot — because the roof and floor system cover half the area even though the walls get taller.',
  },
  {
    question: 'Does this estimate include labor?',
    answer:
      'No. Every number here is material cost delivered to your site — no labor, no equipment rental, no dumpsters, no fasteners. If you are subbing out the work, a rough planning check is to expect labor to roughly match or exceed material cost on the shell trades, more on finish work. The savings side of that trade is what the cost savings worksheet walks through.',
  },
  {
    question: 'Why is my lumberyard quote different from this estimate?',
    answer:
      'Three reasons, in order of size. Lumber prices swing 50–100% with market conditions, so a quote from a different quarter is a different number. Regional pricing varies widely — concrete, in particular, is priced by how far the truck drives. And a contractor account at a real lumberyard usually beats big-box retail by 10–20%, which is the single easiest discount an owner-builder can pick up. Use this estimate to size your budget and to sanity-check quotes, not to replace them.',
  },
  {
    question: 'How accurate is a square-footage material estimate?',
    answer:
      'Close enough to budget with, not close enough to order from. This sheet derives a footprint and wall areas from your square footage rather than from your plans, so an unusual shape, a walk-out basement, or a lot of glass will move the numbers. Once you have real dimensions, run the trade sheets — framing lumber, concrete slab, drywall, roofing, flooring, insulation — which take actual measurements and give you order quantities.',
  },
];

const faqSchema = generateFAQSchema(FAQS);

export default function MaterialEstimatorPage() {
  return (
    <div className={s.calcPage}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      <CalcHero
        title="Building Material Cost Calculator"
        sub="Whole-house material quantities and cost from your square footage — concrete through insulation, with every rate and multiplier shown."
        cells={[
          { k: 'Sheet', v: 'W-02' },
          { k: 'Returns', v: 'Cost + quantities' },
          { k: 'Scope', v: 'Structural shell' },
          { k: 'Basis', v: 'Sq ft + finish' },
        ]}
      />

      <div className={s.sheetWrap}>
        <MaterialEstimatorCalc />
      </div>

      <div className={s.content}>
        <CalcSection label="Methodology" title="How the estimate is figured" meta="SHEET W-02">
          <div className={s.prose}>
            <p>
              Everything starts from one division: finished square footage ÷ stories = footprint.
              A 2,000 sq ft two-story sits on a 1,000 sq ft slab, so it roofs exactly half the area
              of the same house built on one level and pours about 45% less concrete — footings
              shrink with the perimeter, not with the area. That is why stories move the total as
              much as they do.
            </p>
            <p>
              <strong>Concrete and foundation.</strong> A 4&quot; slab over the footprint plus a
              16&quot; wide × 12&quot; deep continuous footing around the perimeter of an equal-area
              square, converted to cubic yards and priced at $150 per yard delivered. Rebar, vapor
              barrier, and under-slab insulation are <em>not</em> in that number — budget another
              15–20% for them. For a real pour with your actual dimensions and thickness, use the{' '}
              <a href="/calculators/concrete-slab">concrete slab calculator</a>.
            </p>
            <p>
              <strong>Framing lumber.</strong> The footprint is treated as a 1.5:1 rectangle to get
              wall length. Board feet are built up per system — 0.6 bf per sq ft of wall surface for
              studs and plates, 0.5 for exterior sheathing, 1.4 for floor joists and 0.75 for
              subfloor per sq ft of framed floor, 1.5 per sq ft of roof for rafters or trusses plus
              the deck — then 15% waste on the total. That lands near 7 board feet per finished
              square foot, the standard rule of thumb. Lumber prices can swing 50–100% on market
              conditions, so get current quotes from more than one supplier and consider locking a
              price in when the market is in your favor. Stud-by-stud counts for walls come from
              the <a href="/calculators/framing-lumber">framing lumber calculator</a>.
            </p>
            <p>
              <strong>Drywall.</strong> Interior partitions are estimated at 1 linear foot per 4 sq
              ft of floor, per story. Board area is both faces of every partition plus every
              ceiling, divided into 4×8 sheets (32 sq ft each). Joint compound, tape, corner bead,
              and screws are separate — the <a href="/calculators/drywall">drywall calculator</a>{' '}
              works those out. Finish level moves the sheet price because premium builds run
              5/8&quot; board on ceilings and add moisture-resistant or sound-rated sheets.
            </p>
            <p>
              <strong>Roofing.</strong> Roof area is the footprint times a complexity multiplier —
              1.1 for a simple gable, 1.3 for hip or mixed, 1.5 for a cut-up roof with multiple
              valleys — which absorbs pitch, overhang, and cutting waste in one factor. That area is
              divided into squares (100 sq ft) and priced for shingles and underlayment. Ridge vent,
              drip edge, flashing, and ice-and-water shield add another 15–25% on top of shingle
              cost; the <a href="/calculators/roofing">roofing calculator</a> separates pitch from
              waste and counts those accessories.
            </p>
            <p>
              <strong>Flooring.</strong> Finished square footage at a per-foot material rate: basic
              is laminate or sheet vinyl, standard is mid-grade hardwood or tile, premium is
              high-end hardwood or natural stone. Material only — professional installation
              typically adds $2–$8 per square foot depending on what you picked. Room-by-room
              quantities with waste are in the{' '}
              <a href="/calculators/flooring">flooring calculator</a>.
            </p>
            <p>
              <strong>Insulation.</strong> Exterior wall area plus finished floor area, the second
              term standing in for ceilings and floor systems. Rates rise with finish level because
              higher-end builds carry higher R-values and more spray foam. Do not cut this line to
              save money — energy payback is usually 3–7 years and it drives how the house feels
              every day. Cavity-by-cavity quantities are in the{' '}
              <a href="/calculators/insulation">insulation calculator</a>.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Assumptions" title="Rates, waste, and multipliers" meta="ADJUST ABOVE">
          <AssumptionsTable
            rows={[
              { label: 'Footprint', value: 'Finished area ÷ stories' },
              { label: 'Footprint shape', value: '1.5:1 rectangle' },
              { label: 'Slab thickness', value: '4 in' },
              { label: 'Footing', value: '16 in × 12 in continuous' },
              { label: 'Concrete price', value: '$150 / yd³ delivered' },
              { label: 'Interior partitions', value: '1 lf per 4 sq ft floor, per story' },
              { label: 'Framing waste', value: '15%' },
              { label: 'Lumber price', value: '$0.85 – $1.50 / bf by finish' },
              { label: 'Drywall sheet', value: '4 × 8 (32 sq ft)' },
              { label: 'Roof area', value: '1.1 – 1.5 × footprint' },
              { label: 'Roofing price', value: '$250 – $500 / square by finish' },
              { label: 'Flooring price', value: '$3 – $8 / sq ft by finish' },
              { label: 'Insulation price', value: '$1.25 – $2.50 / sq ft by finish' },
              { label: 'Prices', value: 'National range, Aug 2026' },
            ]}
          />
        </CalcSection>

        <CalcSection label="Scope" title="What this estimate leaves out">
          <div className={s.prose}>
            <p>
              This sheet prices the structural shell. A complete material budget carries a second
              list that is often larger than the first — these are planning ranges for a typical
              single-family home, and they are the line items that surprise first-time builders
              most. Track them against your actual spend in the{' '}
              <a href="/calculators/budget-tracker">budget tracker</a>.
            </p>
          </div>
          <AssumptionsTable
            rows={[
              { label: 'Windows, doors & hardware', value: '$15,000 – $40,000' },
              { label: 'HVAC, electrical & plumbing', value: '$30,000 – $60,000' },
              { label: 'Cabinets & countertops', value: '$8,000 – $30,000' },
              { label: 'Appliances & fixtures', value: '$15,000 – $35,000' },
              { label: 'Siding, trim, paint & gutters', value: '$8,000 – $25,000' },
              { label: 'Site work, utilities & drive', value: '$15,000 – $40,000' },
            ]}
          />
        </CalcSection>

        <CalcSection label="Field notes" title="Ordering materials without losing money">
          <div className={s.prose}>
            <p>
              <strong>Order 10–15% extra on anything you cut.</strong> Waste, mistakes, and future
              repairs all come out of the same pile. It matters most for materials that get
              discontinued — flooring, tile, siding — where a matching board three years from now is
              worth more than the storage space it took.
            </p>
            <p>
              <strong>Open contractor accounts.</strong> Set up accounts at real lumberyards and
              suppliers rather than buying retail. Better pricing (usually 10–20% off), delivery
              scheduling, and access to contractor-grade material that the big boxes do not stock.
              This is the largest discount available to an owner-builder for the least effort.
            </p>
            <p>
              <strong>Time orders to the schedule, not the budget.</strong> Bring material in 1–2
              weeks before you need it. Buying everything up front invites theft, weather damage,
              and ties up cash you will want later. The exception is lumber: if the market is low
              and you have dry covered storage, locking a price in is defensible. Sequence your
              orders against your{' '}
              <a href="/calculators/timeline-estimator">build timeline</a> and the{' '}
              <a href="/build-phases/framing">framing phase</a> in particular, since that is where
              the biggest single delivery lands.
            </p>
            <p>
              <strong>Inspect every delivery before you sign.</strong> Count it, look for damage,
              check that it is what you ordered. Getting credit after the driver pulls away is a
              different and much worse conversation.
            </p>
            <p>
              <strong>Store it like it cost you money.</strong> Wet lumber warps, wet drywall is
              scrap, and moisture-damaged material causes problems that surface a year later. Tarps
              on, material up off the dirt, stacked flat.
            </p>
            <p>
              <strong>Keep every receipt.</strong> Track each purchase against the phase it belongs
              to. You will need it for budget tracking, for warranty claims, and occasionally for an
              inspector who wants to see a product spec.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Questions" title="Owner-builders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS.map((f) => ({ question: f.question, answer: f.answer }))} />
        </CalcSection>

        <RelatedCalcs slug="material-estimator" />

        <div className={`${s.block} ${s.blockLast} no-print`}>
          <BinderCTA
            context="material-estimator"
            lead="Estimating materials is planning-phase work — and it's exactly what the Job Site Binder's Excel calculators do with live formulas: concrete, drywall, paint, and roofing, plus 367 print-ready pages of checklists and logs for when the build starts."
          />
        </div>
      </div>
    </div>
  );
}
