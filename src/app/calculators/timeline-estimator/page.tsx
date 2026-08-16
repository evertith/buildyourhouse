import type { Metadata } from 'next';
import s from '@/styles/CalcSheet.module.css';
import TimelineCalc from '@/components/calc/TimelineCalc';
import { CalcHero, CalcSection, AssumptionsTable, CalcFAQ, RelatedCalcs } from '@/components/calc/sections';
import BinderCTA from '@/components/BinderCTA';
import { generateFAQSchema, schemaToScriptTag } from '@/lib/schema';

export const metadata: Metadata = {
  alternates: { canonical: '/calculators/timeline-estimator' },
  title: 'Free Build Timeline Calculator — How Long Will Your House Take?',
  description:
    'Estimate your owner-builder timeline based on house size, experience level, and DIY percentage. Phase-by-phase schedule with realistic durations.',
};

const FAQS = [
  {
    question: 'How long does it take to build a house yourself?',
    answer:
      'Professional builders finish a house in 4–6 months. Owner-builders should plan on 12–24 months, depending on how many hours a week they can hold and how much of the work they keep. That gap is not failure — it is what happens when you are learning the job while doing it, working evenings and weekends, and waiting on subs who have other customers.',
  },
  {
    question: 'How many hours does it take to build a house?',
    answer:
      'This worksheet uses 1.75 personal hours per square foot for a complete DIY build, so a 2,000 sq ft house is roughly 3,500 hands-on hours before adjustments. A first-time builder multiplies that by 1.4; somebody with several projects behind them multiplies by 0.8. If you sub out half the work, only half of those hours land on your calendar.',
  },
  {
    question: 'Can I build a house while working a full-time job?',
    answer:
      'Yes, and most owner-builders do — but do the arithmetic before you commit. Twenty hours a week is two full days, half of a full-time pace, and it turns a 3,500-hour build into roughly 88 weeks of your own time at a 50% DIY share. Ten hours a week doubles everything. The number that matters is not the hours you can work in a good week, it is the hours you can still work in month fourteen.',
  },
  {
    question: 'How much longer does a first-time builder take?',
    answer:
      'Add 30–40%. You will spend time learning, making mistakes, and doing some things twice. The upside is that skills compound: you will be far faster at the end than at the beginning, which is why hiring out early framing and doing your own finish work often beats the reverse.',
  },
  {
    question: 'Why do owner-builder schedules slip?',
    answer:
      'Rarely because a task took longer than planned. It is permit review that runs 4–12 weeks, subs who need 4–6 weeks of lead time, failed inspections that add a week apiece, weather that shuts down concrete and framing, and momentum lost to a vacation or a busy stretch at work. This worksheet counts working time only — every one of those delays lands on top of the number it gives you.',
  },
  {
    question: 'Do helpers really cut the schedule in half?',
    answer:
      'No. Each consistent helper is counted here as 60% more output, not 100%, because somebody has to plan the work, answer questions, and redo what gets done wrong. Two helpers get you to roughly 45% of the solo hours, not 33%. Occasional weekend volunteers are worth less than that — count only the people who actually show up week after week.',
  },
];

const faqSchema = generateFAQSchema(FAQS);

export default function TimelineEstimatorPage() {
  return (
    <div className={s.calcPage}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      <CalcHero
        title="Build Timeline Estimator"
        sub="How long the build actually takes from your hours per week, DIY share, and experience — phase by phase, so you can plan your life around it."
        cells={[
          { k: 'Sheet', v: 'W-03' },
          { k: 'Returns', v: 'Schedule' },
          { k: 'Scope', v: 'Whole build' },
          { k: 'Basis', v: 'Your hours' },
        ]}
      />

      <div className={s.sheetWrap}>
        <TimelineCalc />
      </div>

      <div className={s.content}>
        <CalcSection label="Methodology" title="How this schedule is figured" meta="SHEET W-03">
          <div className={s.prose}>
            <p>
              <strong>Hours first, calendar second.</strong> The worksheet starts with 1.75 personal
              hours per square foot for a complete DIY build — about 3,500 hours on a 2,000 sq ft
              house. That figure lines up with the Census reality for owner-built homes, which take
              roughly 15 months against 4–6 for a builder, and with what owner-builders report once
              they add up their own logs.
            </p>
            <p>
              <strong>Experience.</strong> A first build multiplies the hours by 1.4, some
              experience by 1.0, and several projects behind you by 0.8. This is the single largest
              adjustment in the sheet, and it is the one people argue with most. The time does not go
              into the work itself; it goes into figuring out the work, buying the wrong thing, and
              doing part of it twice.
            </p>
            <p>
              <strong>Helpers.</strong> Each consistent helper divides the hours by an extra 0.6, so
              one helper leaves you at 1/1.6 of the solo hours rather than half. Somebody still has
              to plan, supervise, and fix. Count only the people who show up week after week — the
              friend who helps one Saturday does not change your schedule.
            </p>
            <p>
              <strong>DIY share.</strong> Only the share you keep runs on your clock. Work you sub
              out still has to be scheduled, inspected, and paid for, but it happens on the sub’s
              time, so it does not consume the hours you have available each week.
            </p>
            <p>
              <strong>Calendar.</strong> Your hours divided by the hours you work per week gives
              weeks; weeks divided by 4.33 gives months. The seven phases split that total by fixed
              shares — 15% planning and permitting, 12% foundation, 20% framing, 18% rough-ins, 12%
              insulation and drywall, 15% interior finishes, 8% final and exterior — distributed so
              the phases add up to exactly the total rather than each rounding up on its own.
            </p>
            <p>
              <strong>What is not in the number.</strong> Weather, permit review, sub lead times,
              failed inspections, material backorders, and the weeks life takes back. Those are
              additive, and on most owner-builder projects they are the difference between the
              estimate and the move-in date. Build the buffer yourself; the worksheet will not do it
              for you.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Assumptions" title="Rates, multipliers, and phase shares" meta="ADJUST ABOVE">
          <AssumptionsTable
            rows={[
              { label: 'Base labor', value: '1.75 hrs per sq ft' },
              { label: 'Beginner', value: '× 1.4' },
              { label: 'Some experience', value: '× 1.0' },
              { label: 'Multiple projects', value: '× 0.8' },
              { label: 'Each helper', value: '÷ (1 + 0.6 per helper)' },
              { label: 'Months', value: 'weeks ÷ 4.33' },
              { label: 'Planning & permitting', value: '15% of schedule' },
              { label: 'Foundation', value: '12%' },
              { label: 'Framing', value: '20%' },
              { label: 'Rough-ins', value: '18%' },
              { label: 'Insulation & drywall', value: '12%' },
              { label: 'Interior finishes', value: '15%' },
              { label: 'Final & exterior', value: '8%' },
            ]}
          />
        </CalcSection>

        <CalcSection label="Context" title="Understanding build timelines">
          <div className={s.prose}>
            <p>
              <strong>Realistic expectations.</strong> Professional builders typically complete a
              home in 4–6 months. Owner-builders should plan for 12–24 months depending on their
              schedule and DIY percentage. This is not failure — it is reality when you are learning
              while building. Most owner-builders underestimate timelines by 30–50%. It always takes
              longer than you think, especially working evenings and weekends.
            </p>
            <p>
              <strong>Hours per week matter more than anything else.</strong> If you can dedicate 20
              hours per week — two full days — you are working at 50% of a full-time pace. At 10
              hours per week everything takes twice as long. Weather, life events, and burnout
              reduce effective hours further. Few owner-builders hold their planned pace for the
              entire project; plan on 60–70% of your estimated hours.
            </p>
            <p>
              <strong>Experience level.</strong> Beginners should add 30–40% to timelines. You will
              spend time learning, making mistakes, and doing things twice. Intermediate builders
              with some construction experience work at near-professional pace on familiar tasks.
              The upside is that skills compound — you will be much faster at the end than the
              beginning, which is an argument for doing finish work yourself after hiring out early
              framing.
            </p>
            <p>
              <strong>Subcontractor delays.</strong> Even hiring out only half the work, you will
              face scheduling delays. Good subs are busy and may have 2–4 week lead times. Weather
              delays, failed inspections, and material shortages add weeks. Book subcontractors 4–6
              weeks in advance, get on their schedule early, confirm the week before, and have
              backup plans.
            </p>
            <p>
              <strong>Critical path items.</strong> Some tasks must happen in sequence: foundation
              before framing, framing before roofing, rough-ins before drywall. You cannot compress
              these. Focus your DIY effort on parallel tasks — site cleanup, painting, trim — that
              do not hold up critical work. Hiring out the critical path (foundation, framing,
              roofing) maintains momentum; do finish work yourself when you have more flexibility.
            </p>
            <p>
              <strong>Seasonal factors.</strong> Building through winter adds 2–4 weeks in most
              climates. Concrete will not cure below freezing, subs will not work in heavy rain, and
              you will hate framing in snow. The best sequence is to start in spring, get dried in
              by fall, and finish the interior through winter — that minimizes weather delays.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Phases" title="What actually happens in each phase">
          <div className={s.prose}>
            <p>
              <strong>Planning &amp; permitting — 15%.</strong> Finalizing plans, applying for
              permits, ordering materials, setting up accounts. Permit approval alone takes 4–12
              weeks in most jurisdictions. Start this early, while you are still in feasibility.
            </p>
            <p>
              <strong>Foundation — 12%.</strong> Excavation, footings, foundation walls,
              waterproofing, backfill. Weather dependent, and most owner-builders hire it out
              entirely. Budget 2–4 weeks for a simple slab, 4–6 weeks for a full basement.
            </p>
            <p>
              <strong>Framing — 20%.</strong> Floor system, wall framing, roof framing, sheathing,
              windows and doors. The most exciting phase and the one that demands the most skill.
              Professional crews take 2–4 weeks; DIY crews take 6–12.
            </p>
            <p>
              <strong>Rough-ins — 18%.</strong> Electrical, plumbing, and HVAC rough-in work. Most
              owner-builders hire licensed subs here, and scheduling three trades in sequence takes
              coordination. Budget 3–6 weeks plus inspection time.
            </p>
            <p>
              <strong>Insulation &amp; drywall — 12%.</strong> Insulation, hanging, taping, mudding,
              sanding. Many owner-builders do their own insulation and hire the drywall — good
              finishing takes skill that does not come quickly. Budget 2–4 weeks for a typical home.
            </p>
            <p>
              <strong>Interior finishes — 15%.</strong> Trim, doors, cabinets, flooring, painting,
              countertops. This is where owner-builders save the most money doing the work
              themselves. Plan for it to take longer than expected; details matter and they are slow.
            </p>
            <p>
              <strong>Final &amp; exterior — 8%.</strong> Exterior finishes, landscaping, final
              inspections, punch list. The last 10% takes as long as you think the last 50% will
              take. Budget extra for the punch list, which does not end when you think it will.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Strategy" title="Keeping the schedule from slipping">
          <div className={s.prose}>
            <p>
              <strong>Build your schedule backwards.</strong> Start from your move-in date and work
              back, then add 30% buffer. If you must be in by next fall, you need to start
              foundation work this spring — not this summer.
            </p>
            <p>
              <strong>Track actual against estimated.</strong> After each phase, compare the time it
              took to the time you planned. If framing ran 50% long, adjust every remaining estimate
              up by the same factor. Do not keep assuming you will make up time later; nobody ever
              does.
            </p>
            <p>
              <strong>Protect your momentum.</strong> The biggest timeline killer is stopping. Once
              momentum is gone — a vacation, a work project, an illness — restarting is hard. Keep
              at least minimal weekly progress even through busy periods.
            </p>
            <p>
              <strong>Book subs early.</strong> Get on subcontractor schedules 4–6 weeks ahead,
              confirm weekly, and have backups identified. A single sub delay cascades into months
              of lost time when it pushes you past the next weather window.
            </p>
            <p>
              <strong>Batch similar tasks.</strong> Do all the framing at once, all the electrical at
              once, all the painting at once. Switching tasks costs setup, cleanup, and mental
              context every time.
            </p>
            <p>
              <strong>Plan for life.</strong> Work demands, family obligations, holidays, burnout —
              build them into the timeline. A sustainable pace beats heroic sprints followed by
              multi-week collapses.
            </p>
          </div>
        </CalcSection>

        <CalcSection label="Questions" title="Owner-builders ask" meta="FAQ" noPrint>
          <CalcFAQ items={FAQS.map((f) => ({ question: f.question, answer: f.answer }))} />
        </CalcSection>

        <RelatedCalcs slug="timeline-estimator" />

        <div className={`${s.block} ${s.blockLast} no-print`}>
          <BinderCTA
            context="timeline-estimator"
            lead="Turn your estimate into a working schedule — the Job Site Binder's Master Project Timeline tracks every phase from permits to punch list, alongside 367 print-ready pages of checklists and logs."
          />
        </div>
      </div>
    </div>
  );
}
