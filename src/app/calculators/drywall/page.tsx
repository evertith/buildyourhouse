import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import DrywallCalc from '@/components/calc/DrywallCalc';
import { CalcHero, CalcSection, AssumptionsTable, CalcFAQ, RelatedCalcs } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';
import { generateFAQSchema, schemaToScriptTag } from '@/lib/schema';

export const metadata: Metadata = {
  alternates: { canonical: '/calculators/drywall' },
  title: 'Drywall Calculator — Sheets, Mud, Tape & Screws',
  description:
    'How many sheets of drywall do I need? Enter a room or your whole-house square footage and get sheet, mud, tape, and screw counts — plus a printable takeoff.',
};

const FAQS = [
  {
    question: 'How many sheets of drywall for a 2,000 sq ft house?',
    answer:
      'About 255 sheets of 4×8. The math: 2,000 sq ft of floor × 3.7 (the walls-plus-ceilings heuristic for stick-built layouts) is 7,400 sq ft of board; divide by 32 sq ft per sheet and add 10% cut waste and you land at 255. With 4×12 sheets it is about 170. Room count, ceiling height, and layout swing the real number, so run rooms individually before ordering.',
  },
  {
    question: 'How much joint compound per sheet of drywall?',
    answer:
      'Standard finishing rules run about 140 lb of all-purpose compound per 1,000 sq ft of board — roughly 4.5 lb per 4×8 sheet, or one 4.5-gallon (61.5-lb) bucket per 450 sq ft, which is about fourteen 4×8 sheets. That covers embedding the tape plus two finish coats. Heavy texture, skim coats, and beginner technique all push it up, so have the next bucket on hand before you run dry mid-coat.',
  },
  {
    question: 'Should I use 4×8 or 4×12 sheets?',
    answer:
      'Per square foot they cost about the same — $12–$18 for a 4×8 (32 sq ft) versus $17–$26 for a 4×12 (48 sq ft), August 2026 national ranges. The 4×12 wins on finishing: a 12-ft sheet runs the full length of most walls, eliminating butt joints, the hardest seams to hide. The 4×8 wins on handling: a 1/2" 4×12 weighs close to 80 lb, wants two people, and will not turn the corner into tight halls and stairwells. Crews hang 4×12 wherever it fits; solo owner-builders mostly live with 4×8.',
  },
  {
    question: 'How many screws per sheet of drywall?',
    answer:
      'Figure about one screw per square foot of board: roughly 32 for a 4×8 sheet and 48 for a 4×12. Codes typically call for screws every 12 inches on ceilings and every 16 inches on walls, and on 16"-on-center framing that averages out to about one per square foot. A 1-lb box holds around 200 #6 × 1¼" coarse-thread screws, so plan one box per 200 sq ft of board — about six 4×8 sheets.',
  },
  {
    question: 'How much does it cost to drywall a house?',
    answer:
      'For a 2,000 sq ft house, materials from this calculator run roughly $3,600–$5,400 — about 255 4×8 sheets plus compound, tape, and screws at August 2026 national prices. That is not the number a drywall contractor quotes: hung, taped, and finished typically runs $1.50–$3.50 per square foot of board, which is $11,000–$26,000 on the same 7,400 sq ft of board. The gap is labor — finishing is a skill trade, and a bad finish shows through every coat of paint.',
  },
];

const faqSchema = generateFAQSchema(FAQS);

export default function DrywallPage() {
  return (
    <div className={s.calcPage}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      <CalcHero
        title="Drywall Calculator"
        sub="Sheets, joint compound, tape, and screws from your square footage — with the math shown, not hidden."
        cells={[
          { k: 'Sheet', v: 'TO-02' },
          { k: 'Returns', v: 'Quantities' },
          { k: 'Scope', v: 'Board + finishing' },
          { k: 'Waste', v: 'Included' },
        ]}
      />

      <div className={s.sheetWrap}>
        <DrywallCalc />
      </div>

      <div className={s.content}>
        <CalcSection label="Methodology" title="How this takeoff is figured" meta="SHEET TO-02">
          <div className={s.prose}>
            <p>
              <strong>One room.</strong> Wall board is perimeter × ceiling height, minus a 10%
              allowance for door, window, and closet openings. Including the ceiling adds
              length × width. This is a real takeoff — measured from your room, accurate enough
              to order from.
            </p>
            <p>
              <strong>Whole house.</strong> Finished board area ≈ 3.7 × floor area. Interior
              partitions carry board on both faces, exterior walls on one, and every ceiling gets
              covered — stack that up over a typical stick-built layout and estimators land
              between 3.5 and 4.0 sq ft of drywall per square foot of floor. This calculator uses
              3.7, the midpoint. Treat house mode as a planning number and run rooms individually
              before ordering.
            </p>
            <p>
              <strong>Sheets.</strong> Board area divided by 32 sq ft (4×8) or 48 sq ft (4×12),
              plus 10% cut waste. Every window cutout and closet jog turns part of a sheet into
              scrap; 10% is the standard carry.
            </p>
            <p>
              <strong>Finishing consumables.</strong> One 4.5-gal bucket of all-purpose compound
              per 450 sq ft of board (about 140 lb per 1,000 sq ft), one 500-ft roll of paper tape
              per 1,350 sq ft (about 370 ft of seams per 1,000 sq ft), and roughly one screw per
              square foot — bought as 1-lb boxes of about 200 #6 × 1¼&quot; coarse screws.
            </p>
            <p>
              <strong>On the job.</strong> Hang ceilings before walls, so the wall sheets support
              the ceiling edges. Use 5/8&quot; board on garage ceilings where your code requires it —
              check before ordering that area as 1/2&quot;.
            </p>
            <p>
              <strong>What&apos;s not here.</strong> Labor, corner bead, texture, and primer. When the
              finish coats are sanded, the <a href="/calculators/paint">paint calculator</a> picks
              up from this same square footage.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Assumptions" title="Waste, coverage, and multipliers" meta="ADJUST ABOVE">
          <AssumptionsTable
            rows={[
              { label: 'House mode multiplier', value: '3.7 × floor area' },
              { label: 'Openings allowance (room)', value: '10% of wall area' },
              { label: 'Cut waste', value: '10%' },
              { label: 'Joint compound', value: '1 bucket per 450 sq ft' },
              { label: 'Joint tape', value: '1 × 500-ft roll per 1,350 sq ft' },
              { label: 'Screws', value: '≈ 1 per sq ft of board' },
              { label: 'Prices', value: 'National range, Aug 2026' },
            ]}
          />
        </CalcSection>

        <CalcSection label="Questions" title="Owner-builders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS.map((f) => ({ question: f.question, answer: f.answer }))} />
        </CalcSection>

        <RelatedCalcs slug="drywall" />

        <div className={`${s.block} ${s.blockLast} no-print`}>
          <BinderCTA
            context="calc-drywall"
            lead="Drywall doesn't go up until framing, electrical, plumbing, and mechanical rough-ins pass inspection — the binder's inspection logs track those sign-offs, and its materials sheets hold the takeoff you just ran. 367 pages of job-site paperwork, organized the way a GC runs a build."
          />
        </div>
      </div>
    </div>
  );
}
