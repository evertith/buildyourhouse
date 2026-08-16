import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import CostSavingsCalc from '@/components/calc/CostSavingsCalc';
import { CalcHero, CalcSection, AssumptionsTable, CalcFAQ, RelatedCalcs } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';
import { generateFAQSchema, schemaToScriptTag } from '@/lib/schema';

export const metadata: Metadata = {
  alternates: { canonical: '/feasibility/cost-savings-calculator' },
  title: 'Owner-Builder Savings Calculator — How Much Will You Save?',
  description:
    'How much do you save building your own house? Enter your budget and a GC fee percentage to see the cash you keep, your cost per square foot, and the honest value of your own hours.',
};

const FAQS = [
  {
    question: 'How much do you actually save by being your own general contractor?',
    answer:
      'The cash you keep is the builder’s fee, and that is typically 10–20% of the contract price. On a $300,000 build at 14%, that is $42,000 — real money, and it is the number this worksheet leads with. What it is not is the 30–40% figure you see quoted online. Those numbers get there by adding the value of your own labor to the fee you avoided, which double-counts work the budget was already paying for.',
  },
  {
    question: 'Should I count my own labor as savings?',
    answer:
      'No — not as cash. Your construction budget already includes what subcontractors charge to do that work. If you frame the walls yourself, you do not pay the framer, so the savings show up as a smaller budget, not as a separate pile of money on top of the GC fee. Counting both is the single most common way owner-builder savings estimates get inflated. That is why this sheet lists the value of your hours on its own line, marked "not cash": it is real value you are contributing, but it is sweat equity, not a check you get to keep.',
  },
  {
    question: 'What does a general contractor’s fee actually pay for?',
    answer:
      'Coordinating and scheduling every subcontractor, ordering materials so they land before the crew does, walking inspections, catching bad work before it gets covered up, carrying the liability, and eating the cost when something has to be redone. Their sub relationships also mean their calls get returned first. When you keep the fee, you take on every one of those jobs — and the trades you have never met price your one-off job accordingly.',
  },
  {
    question: 'What costs go up when you owner-build?',
    answer:
      'Financing is usually the big one: fewer lenders write owner-builder construction loans, and the ones that do often want more down or charge a higher rate. Then builder’s-risk insurance you buy yourself instead of riding on a GC’s policy, re-work from mistakes a builder would not have made, tool and equipment rental, and schedule drag — every extra month is another month of construction-loan interest and, often, rent or a mortgage somewhere else. Budget a contingency that assumes you will make expensive mistakes, because you will make some.',
  },
  {
    question: 'How many hours does owner-building take?',
    answer:
      'Most owner-builders put in 400–1,000 hours across a 12–18 month build, even when they hire out nearly all the labor. That is evenings and weekends: bid packages, material orders, inspection scheduling, site visits, and the phone calls that never stop. This sheet divides the fee you keep by those hours so you can see what your time is earning — at $42,000 over 500 hours it is $84 an hour, which is the honest way to compare it against overtime at your day job.',
  },
  {
    question: 'Do owner-builders really get contractor pricing on materials?',
    answer:
      'Partly. Lumberyards and supply houses will open an account and quote you off list once they see a real project and a real permit, and that pricing beats big-box retail on lumber, trusses, windows, and doors. What you will not get is the volume tier a builder putting up thirty houses a year is on. Plan on landing between retail and builder pricing, and get three quotes on every package over a few thousand dollars.',
  },
];

const faqSchema = generateFAQSchema(FAQS);

export default function CostSavingsCalculatorPage() {
  return (
    <div className={s.calcPage}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      <CalcHero
        title="Owner-Builder Cost Savings Calculator"
        sub="What you actually keep by acting as your own GC — the builder’s fee you avoid, held apart from the value of your own hours instead of quietly added to it."
        cells={[
          { k: 'Sheet', v: 'W-01' },
          { k: 'Returns', v: 'Cash saved' },
          { k: 'Basis', v: 'Fee % of contract' },
          { k: 'Excludes', v: 'Sweat equity' },
        ]}
      />

      <div className={s.sheetWrap}>
        <CostSavingsCalc />
      </div>

      <div className={s.content}>
        <CalcSection label="Methodology" title="How this worksheet is figured" meta="SHEET W-01">
          <div className={s.prose}>
            <p>
              <strong>Cash saved.</strong> Contract price × fee percentage. The build cost you
              enter is the all-in number a general contractor would quote you — their fee
              included — and the percentage is that fee&apos;s share of it. Keep the fee and your
              cost is the contract less the fee; the subs and suppliers still get paid exactly
              what they were going to get paid.
            </p>
            <p>
              <strong>Why your labor is not added in.</strong> Your budget already carries
              subcontractor labor. Doing the work yourself removes that line from the budget — it
              does not create a second pot of savings sitting next to the fee. Adding both is how
              a 14% saving gets advertised as 40%. The value of your hours is on the sheet, on its
              own line, marked as not cash, because it is worth knowing what you are contributing
              even though you cannot spend it.
            </p>
            <p>
              <strong>Fee kept, per hour you work.</strong> The fee you avoid divided by the hours
              you put in. This is the number to argue with: if it comes out below what you earn at
              work, and you would otherwise be earning it, the math is telling you something.
            </p>
            <p>
              <strong>Cost per square foot.</strong> Your cost after the fee, divided by finished
              square footage — the figure you can hold up against what people in your county are
              actually paying. The with-a-GC number sits beside it for comparison.
            </p>
            <p>
              <strong>What is not modeled.</strong> Builder&apos;s-risk insurance, permit and impact
              fees, construction-loan interest, tool rental, and re-work. Those are covered under
              the reality check below, and the{' '}
              <a href="/calculators/material-estimator">whole-house material estimator</a> and{' '}
              <a href="/calculators/budget-tracker">budget tracker</a> are where the real numbers
              go once you have quotes.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Assumptions" title="What this sheet takes as given" meta="ADJUST ABOVE">
          <AssumptionsTable
            rows={[
              { label: 'Cash saved', value: 'Fee % × contract price' },
              { label: 'Your cost', value: 'Contract price − fee' },
              { label: 'Sweat equity', value: 'Hours × your hourly value' },
              { label: 'Sweat equity in the headline', value: 'Excluded' },
              { label: 'Fee percentage cap', value: '30%' },
              { label: 'Full-time week', value: '40 hours' },
              { label: 'Added owner-builder costs', value: 'Not modeled' },
            ]}
          />
        </CalcSection>

        <CalcSection label="The fee" title="What you are keeping, and what it bought" meta="15–20% TYPICAL">
          <div className={s.prose}>
            <p>
              <strong>General contractor fees.</strong> Most GCs charge 15–20% of total
              construction cost. On a $300,000 home that is $45,000–$60,000. Manage the project
              yourself and you keep it — which is the whole financial case for owner-building, and
              it is a good one.
            </p>
            <p>
              <strong>What that fee does for you.</strong> Coordinating subcontractors, holding the
              schedule together, walking inspections, ordering materials on time, and overseeing
              quality. Every one of those becomes your job. The fee is not free money sitting on
              the table; it is payment for work that still has to happen.
            </p>
            <p>
              <strong>Your labor has value too.</strong> Whether you frame walls, run trim, or
              paint, you are doing work that costs $30–$75 an hour to hire out. Most owner-builders
              contribute 400–1,000 hours. That is real value — it just shows up as a smaller budget
              rather than as cash in your pocket, which is why this sheet keeps it on a separate
              line.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Beyond the fee" title="The savings that do not show up in the headline" meta="HONEST VERDICTS">
          <div className={s.prose}>
            <p>
              Owner-builders pick up smaller savings all over the job. They are real, but they vary
              enough that this sheet will not put a number on them for you — here is the honest
              verdict on each.
            </p>
          </div>
          <AssumptionsTable
            rows={[
              { label: 'Contractor pricing on materials', value: 'Partly — supply houses, not big boxes' },
              { label: 'Markup on subcontractor bids', value: 'Avoided' },
              { label: 'Cost decisions made in real time', value: 'Yours to make, or to blow' },
              { label: 'Finish work GCs sub out', value: 'Sweat equity, not cash' },
              { label: 'Communication overhead', value: 'Gone — you are the overhead' },
            ]}
          />
        </CalcSection>

        <CalcSection label="Reality check" title="What the savings will cost you" meta="READ THIS TWICE">
          <div className={s.prose}>
            <p>
              <strong>Time investment.</strong> Plan on 12–18 months from permit to move-in. Your
              evenings and weekends go into managing the project even if you hire out most of the
              labor — and the hours are not optional or reschedulable when an inspector or a
              concrete truck is involved.
            </p>
            <p>
              <strong>Learning curve.</strong> You will need to learn building codes, inspection
              requirements, and construction sequencing. Budget time and money for mistakes and
              re-work; sequencing errors are the expensive kind, because they get discovered after
              something is covered up.
            </p>
            <p>
              <strong>Stress factor.</strong> Managing a build is stressful in a way that is hard
              to price. Every decision, every delay, and every dollar is yours. Ask anyone who has
              done it what the last two months were like.
            </p>
            <p>
              <strong>Opportunity cost.</strong> Consider what else those 400–1,000 hours could
              have gone to. The value of your labor depends entirely on what you are giving up to
              spend it here — which is exactly what the &ldquo;value of your time&rdquo; field is
              asking you to be honest about.
            </p>
            <p>
              None of that makes owner-building a bad decision. It makes it a job. Take the{' '}
              <a href="/feasibility/is-it-right-for-you">feasibility assessment</a> for a
              straight answer on whether it fits your situation, and the{' '}
              <a href="/start-here">complete roadmap</a> for what the sequence actually looks like.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Questions" title="Owner-builders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS.map((f) => ({ question: f.question, answer: f.answer }))} />
        </CalcSection>

        <RelatedCalcs slug="cost-savings-calculator" />

        <div className={`${s.block} ${s.blockLast} no-print`}>
          <BinderCTA
            context="cost-savings-calculator"
            lead="Owner-builders keep those savings by staying organized — the Job Site Binder is the management system that makes it stick: contracts, checklists, inspection forms, and budget trackers across 367 print-ready pages."
          />
        </div>
      </div>
    </div>
  );
}
