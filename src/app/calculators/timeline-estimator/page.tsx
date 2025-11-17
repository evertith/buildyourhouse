import TimelineEstimatorCalculator from '@/components/TimelineEstimatorCalculator';
import type { Metadata } from 'next';
import styles from '../../feasibility/cost-savings-calculator/calculator-page.module.css';

export const metadata: Metadata = {
  title: 'Build Timeline Estimator - Calculate Your Owner-Builder Timeline',
  description: 'Estimate how long it will take to build your home based on your schedule, experience level, and DIY percentage. Get realistic phase-by-phase timelines.',
};

export default function TimelineEstimatorPage() {
  return (
    <div className={styles.page}>
      <div className={styles.container}>
        <header className={styles.header}>
          <h1>Build Timeline Estimator</h1>
          <p className={styles.subtitle}>
            Get a realistic estimate of how long your owner-builder project will take from permit
            to move-in. This calculator factors in your available time, experience level, DIY percentage,
            and provides a phase-by-phase breakdown so you can plan your life accordingly.
          </p>
        </header>

        <TimelineEstimatorCalculator />

        <section className={styles.info}>
          <h2>Understanding Build Timelines</h2>

          <div className={styles.infoGrid}>
            <div className={styles.infoCard}>
              <h3>Realistic Expectations</h3>
              <p>
                Professional builders typically complete a home in 4-6 months. Owner-builders should
                plan for 12-24 months depending on their schedule and DIY percentage. This isn't failure -
                it's reality when you're learning while building.
              </p>
              <p>
                <strong>Key insight:</strong> Most owner-builders underestimate timelines by 30-50%.
                It always takes longer than you think, especially when working evenings and weekends.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Hours Per Week Matter</h3>
              <p>
                If you can dedicate 20 hours per week (two full days), you're working at 50% of a
                full-time pace. At 10 hours per week, everything takes twice as long. Weather, life
                events, and burnout further reduce effective hours.
              </p>
              <p>
                <strong>Reality check:</strong> Few owner-builders maintain their planned pace for
                the entire project. Plan for 60-70% of your estimated hours.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Experience Level Impact</h3>
              <p>
                Beginners should add 30-40% to timelines. You'll spend time learning, making mistakes,
                and doing things twice. Intermediate builders with some construction experience can
                work at near-professional pace on familiar tasks.
              </p>
              <p>
                <strong>The upside:</strong> Skills compound. You'll be much faster at the end than
                the beginning. Consider doing finish work yourself after hiring out early framing.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Subcontractor Delays</h3>
              <p>
                Even when hiring out 50% of work, you'll face scheduling delays. Good subs are busy
                and may have 2-4 week lead times. Weather delays, failed inspections, and material
                shortages add weeks to the schedule.
              </p>
              <p>
                <strong>Pro tip:</strong> Book subcontractors 4-6 weeks in advance. Get on their
                schedule early, confirm the week before, and have backup plans.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Critical Path Items</h3>
              <p>
                Some tasks must happen in sequence: foundation before framing, framing before roofing,
                rough-ins before drywall. You can't compress these. Focus your DIY efforts on parallel
                tasks (site cleanup, painting, trim) that don't hold up critical work.
              </p>
              <p>
                <strong>Strategy:</strong> Hire out critical path items (foundation, framing, roofing)
                to maintain momentum. Do finish work yourself when you have more flexibility.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Seasonal Factors</h3>
              <p>
                Building through winter adds 2-4 weeks in most climates. Concrete won't cure below
                freezing, subs won't work in heavy rain, and you'll hate framing in snow. Plan
                weatherproof work (interior finishes) for winter months.
              </p>
              <p>
                <strong>Best timeline:</strong> Start in spring, get dried-in by fall, finish
                interior through winter. This minimizes weather delays.
              </p>
            </div>
          </div>
        </section>

        <section className={styles.reality}>
          <h2>Phase-by-Phase Realities</h2>
          <p>
            Here's what actually happens during each phase, based on hundreds of owner-builder projects:
          </p>

          <div className={styles.considerations}>
            <div className={styles.consideration}>
              <h4>Planning & Permitting</h4>
              <p>
                15% of timeline. Finalizing plans, applying for permits, ordering materials, setting up
                accounts. Permit approval alone takes 4-12 weeks in most jurisdictions. Start this early
                while still in feasibility.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Foundation</h4>
              <p>
                12% of timeline. Excavation, footings, foundation walls, waterproofing, backfill.
                Weather dependent. Most owner-builders hire this out entirely. Budget 2-4 weeks for
                a simple slab, 4-6 weeks for a full basement.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Framing</h4>
              <p>
                20% of timeline. Floor system, wall framing, roof framing, sheathing, windows/doors.
                This is the most exciting phase but requires the most skill. Professional crews take
                2-4 weeks. DIY crews: 6-12 weeks.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Rough-Ins</h4>
              <p>
                18% of timeline. Electrical, plumbing, HVAC rough-in work. Most owner-builders hire
                licensed subs for this. Scheduling three different trades takes coordination. Budget
                3-6 weeks plus inspection time.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Insulation & Drywall</h4>
              <p>
                12% of timeline. Insulation, drywall hanging, taping, mudding, sanding. Many owner-builders
                do their own insulation but hire drywall. Good drywall finishing takes skill. Budget
                2-4 weeks for a typical home.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Interior Finishes</h4>
              <p>
                15% of timeline. Trim, doors, cabinets, flooring, painting, countertops. This is where
                owner-builders can save the most money doing it themselves. Plan for this to take longer
                than expected - details matter.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Final & Exterior</h4>
              <p>
                8% of timeline. Exterior finishes, landscaping, final inspections, punch list items.
                The last 10% takes as long as you think the last 50% will take. Budget extra time for
                the endless punch list.
              </p>
            </div>
          </div>
        </section>

        <section className={styles.reality} style={{ backgroundColor: 'var(--color-bg-light)', marginTop: '3rem' }}>
          <h2>Timeline Management Strategies</h2>
          <p>
            After managing hundreds of builds, here's how to keep your project on track:
          </p>

          <div className={styles.considerations}>
            <div className={styles.consideration}>
              <h4>Build Your Schedule Backwards</h4>
              <p>
                Start with your move-in date and work backwards. Add 30% buffer time. If you absolutely
                must be in by next fall, you need to start foundation work this spring - not summer.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Track Actual vs. Estimated</h4>
              <p>
                After each phase, compare actual time to estimated. If framing took 50% longer than
                planned, adjust all remaining estimates up. Don't keep assuming you'll "make up time later."
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Protect Your Momentum</h4>
              <p>
                The biggest timeline killer is stopping. Once you lose momentum (vacation, work project,
                illness), it's hard to restart. Try to maintain at least minimal weekly progress even during
                busy periods.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Book Subs Early</h4>
              <p>
                Get on subcontractor schedules 4-6 weeks in advance. Confirm weekly. Have backup subs
                identified. A single sub delay can cascade into months of lost time.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Batch Similar Tasks</h4>
              <p>
                Do all framing at once, all electrical at once, all painting at once. Switching between
                tasks costs time in setup, cleanup, and mental context switching. Batching is more efficient.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Plan for Life</h4>
              <p>
                You'll have work demands, family obligations, holidays, and burnout. Build these into
                your timeline. A sustainable pace beats heroic sprints followed by multi-week breaks.
              </p>
            </div>
          </div>
        </section>

        <section className={styles.nextSteps}>
          <h2>Next Steps</h2>
          <p>Now that you understand the timeline, explore other planning tools.</p>
          <div className={styles.ctaButtons}>
            <a href="/calculators/material-estimator" className={styles.primaryButton}>
              Estimate Materials
            </a>
            <a href="/calculators/budget-tracker" className={styles.secondaryButton}>
              Track Your Budget
            </a>
          </div>
        </section>
      </div>
    </div>
  );
}
