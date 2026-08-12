import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import ConcreteCalc from '@/components/calc/ConcreteCalc';
import { CalcHero, CalcSection, AssumptionsTable, CalcFAQ, RelatedCalcs } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';
import { generateFAQSchema, schemaToScriptTag } from '@/lib/schema';

export const metadata: Metadata = {
  alternates: { canonical: '/calculators/concrete-slab' },
  title: 'Concrete Calculator — Slab Yards, Bags & Rebar',
  description:
    'How much concrete do I need for a slab? Enter dimensions and thickness for yards to order, bag counts, and mesh or rebar — with a printable takeoff sheet.',
};

const FAQS = [
  {
    question: 'How many yards of concrete for a 24×24 slab?',
    answer:
      'At 4" thick, 24 × 24 ft is 576 sq ft × 4/12 = 192 cubic feet. A thickened edge adds a 12 × 12" footing around the 96-ft perimeter — 96 more cubic feet — for 288 total, or 10.7 cubic yards placed. Add the 10% order margin and round up to the quarter yard, and you order 11.75 yd³. Skip the thickened edge and the same slab orders at 8 yards even.',
  },
  {
    question: 'Should I use bags or ready-mix concrete?',
    answer:
      'An 80-lb bag yields 0.60 cubic feet, so a single cubic yard is 45 bags — mixed one batch at a time. Bags stop making sense around 2 yards (90+ bags); past that, mixing time alone risks cold joints between batches. Ready-mix runs $155–$195 per yard delivered (August 2026), though loads under about 4 yards usually carry a short-load fee. The sheet shows the bagged alternative in the notes so you can compare both ways.',
  },
  {
    question: 'How thick should a garage slab be?',
    answer:
      '4 inches is the typical garage slab for cars and light trucks. Go 5 or 6 inches if the slab will carry heavy trucks, an RV, or a vehicle lift. Your code office and your soil have the final say — expansive or poorly compacted soil can demand more thickness or reinforcement regardless of what parks on it, so confirm with the permit desk before you form.',
  },
  {
    question: 'Do I need rebar or wire mesh in a slab?',
    answer:
      'For a residential slab on grade, reinforcement is crack control, not structure — it holds cracks tight rather than preventing them. Mesh or rebar both work if placed mid-slab on chairs, not left on the ground to be pulled up during the pour. Choose rebar (figured here as #4 both ways at 24" on-center) when the slab carries point loads like a lift post or heavy racking. Plain or fiber mix with neither is also common for sheds — ask your inspector what local practice expects.',
  },
  {
    question: 'What is a short-load fee?',
    answer:
      'A ready-mix truck carries about 10 yards, and the plant pays for the truck and driver whether it hauls 10 or 2. Loads under roughly 4 cubic yards usually carry a short-load fee to cover the trip; the exact charge varies by plant, so ask when you order. If your pour lands just under the cutoff, it can be cheaper to add a footing or pad to the same pour, or split a truck with a neighbor.',
  },
];

const faqSchema = generateFAQSchema(FAQS);

export default function ConcreteSlabPage() {
  return (
    <div className={s.calcPage}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      <CalcHero
        title="Concrete Slab Calculator"
        sub="Cubic yards to order, the bagged alternative, and reinforcement from your slab dimensions — with the math shown, not hidden."
        cells={[
          { k: 'Sheet', v: 'TO-03' },
          { k: 'Returns', v: 'Yards + bags' },
          { k: 'Scope', v: 'Slabs & garages' },
          { k: 'Margin', v: '+10%' },
        ]}
      />

      <div className={s.sheetWrap}>
        <ConcreteCalc />
      </div>

      <div className={s.content}>
        <CalcSection label="Methodology" title="How this takeoff is figured" meta="SHEET TO-03">
          <div className={s.prose}>
            <p>
              <strong>Slab volume.</strong> Length × width × (thickness ÷ 12) gives cubic feet;
              divide by 27 for cubic yards. A 24 × 24 ft slab at 4&quot; is 192 cubic feet — about
              7.1 yards before margin.
            </p>
            <p>
              <strong>Thickened edge.</strong> The standard monolithic detail for garages and
              sheds: a 12&quot; wide × 12&quot; deep footing around the perimeter, poured in the
              same shot as the slab. On that 24 × 24, the 96-ft perimeter adds 96 cubic feet —
              roughly 3.5 yards more.
            </p>
            <p>
              <strong>Order margin.</strong> The order quantity carries 10% on top of the placed
              volume and rounds up to the quarter yard. Short-loading a pour is the expensive
              mistake: if the truck comes up a half yard short, you either pay a second delivery —
              with its own short-load fee — or cold-joint the slab while you wait. Finishing crews
              would rather waste half a yard than stop a pour, and so should you.
            </p>
            <p>
              <strong>Bags vs. ready-mix.</strong> An 80-lb bag yields 0.60 cubic feet, and the
              bagged alternative appears in the notes under the schedule so you can compare. Bags
              stop making sense above roughly 2 yd³ — that is 90-plus bags to haul, mix, and place
              before the first batch stiffens.
            </p>
            <p>
              <strong>Under and in the slab.</strong> Every run includes 6-mil poly vapor barrier
              at the slab footprint plus 15% for laps and turnups. Mesh is figured as 5×10 flat
              sheets with a one-square overlap (10%); rebar as #4 both ways at 24&quot; on-center
              with a 5% lap allowance.
            </p>
            <p>
              <strong>What&apos;s not here.</strong> Forms, gravel base, labor, and pump or
              finishing costs. This sheet sizes slabs, garages, and outbuildings — house
              foundations need engineered footings from your plans, not a calculator. The{' '}
              <a href="/build-phases/foundation">foundation phase guide</a> covers what happens
              before and after the pour.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Assumptions" title="Volume, margin, and materials" meta="ADJUST ABOVE">
          <AssumptionsTable
            rows={[
              { label: 'Slab volume', value: 'L × W × t/12 ÷ 27' },
              { label: 'Thickened edge', value: '12 × 12" × perimeter' },
              { label: 'Order margin', value: '+10%, rounded up to ¼ yd' },
              { label: '80-lb bag yield', value: '0.60 cu ft' },
              { label: 'Vapor barrier', value: '6-mil poly + 15% laps' },
              { label: 'Wire mesh', value: '5×10 sheets + 10% overlap' },
              { label: 'Rebar', value: '#4 both ways, 24" OC + 5%' },
              { label: 'Ready-mix price', value: '$155–$195/yd, Aug 2026' },
              { label: 'Short loads', value: 'Fee under ~4 yd³ — ask the plant' },
            ]}
          />
        </CalcSection>

        <CalcSection label="Questions" title="Owner-builders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS.map((f) => ({ question: f.question, answer: f.answer }))} />
        </CalcSection>

        <RelatedCalcs slug="concrete-slab" />

        <div className={`${s.block} ${s.blockLast} no-print`}>
          <BinderCTA
            context="calc-concrete-slab"
            lead="The binder's foundation section holds the pre-pour checklist, pour-day sheets, and delivery logs — the paperwork this takeoff feeds. 367 pages of job-site paperwork, organized the way a GC runs a build."
          />
        </div>
      </div>
    </div>
  );
}
