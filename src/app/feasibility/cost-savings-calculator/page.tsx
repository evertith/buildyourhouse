import CostSavingsCalculator from '@/components/CostSavingsCalculator';
import type { Metadata } from 'next';
import styles from './calculator-page.module.css';

export const metadata: Metadata = {
  title: 'Cost Savings Calculator - Calculate Your Owner-Builder Savings',
  description: 'Calculate exactly how much money you can save by building your own home. Factor in GC fees, your labor value, and get a realistic estimate.',
};

export default function CostSavingsCalculatorPage() {
  return (
    <div className={styles.page}>
      <div className={styles.container}>
        <header className={styles.header}>
          <h1>Owner-Builder Cost Savings Calculator</h1>
          <p className={styles.subtitle}>
            Discover exactly how much you can save by acting as your own general contractor.
            This calculator factors in typical GC fees, the value of your labor, and gives you
            a realistic estimate of your potential savings.
          </p>
        </header>

        <CostSavingsCalculator />

        <section className={styles.info}>
          <h2>Understanding Your Savings</h2>

          <div className={styles.infoGrid}>
            <div className={styles.infoCard}>
              <h3>General Contractor Fees</h3>
              <p>
                Most general contractors charge 15-20% of the total construction cost. On a
                $300,000 home, that's $45,000-$60,000. By managing the project yourself,
                you keep this money.
              </p>
              <p>
                <strong>What GCs do for this fee:</strong> Coordinate subcontractors, manage
                schedules, handle inspections, order materials, and oversee quality. You'll
                be doing all of this yourself.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Your Labor Value</h3>
              <p>
                The "sweat equity" you put in has real value. Whether you frame walls, install
                trim, or paint, you're doing work that would otherwise cost $30-75/hour to
                hire out.
              </p>
              <p>
                <strong>Typical owner-builder hours:</strong> Most owner-builders contribute
                400-1,000 hours of labor. Even at conservative hourly rates, this adds up to
                significant savings.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Hidden Savings</h3>
              <p>
                Beyond direct savings, owner-builders often save by:
              </p>
              <ul>
                <li>Getting contractor pricing on materials</li>
                <li>Avoiding markup on subcontractor bids</li>
                <li>Making cost-effective decisions in real-time</li>
                <li>Doing finish work that GCs often subcontract</li>
                <li>Eliminating communication overhead</li>
              </ul>
            </div>
          </div>
        </section>

        <section className={styles.reality}>
          <h2>The Reality Check</h2>
          <p>
            While the savings are real, it's important to understand what you're taking on:
          </p>

          <div className={styles.considerations}>
            <div className={styles.consideration}>
              <h4>Time Investment</h4>
              <p>
                Plan for 12-18 months from permit to move-in. You'll spend evenings and
                weekends managing the project, even if you hire most of the labor.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Learning Curve</h4>
              <p>
                You'll need to learn building codes, inspection requirements, and construction
                sequencing. Budget time for mistakes and re-work.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Stress Factor</h4>
              <p>
                Managing a home build is stressful. You're responsible for every decision,
                every delay, and every dollar spent.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Opportunity Cost</h4>
              <p>
                Consider what else you could do with those 400-1,000 hours. The "value" of
                your labor depends on what you're giving up.
              </p>
            </div>
          </div>
        </section>

        <section className={styles.nextSteps}>
          <h2>Next Steps</h2>
          <p>Now that you know your potential savings, it's time to assess if owner-building is right for you.</p>
          <div className={styles.ctaButtons}>
            <a href="/feasibility/is-it-right-for-you" className={styles.primaryButton}>
              Take the Feasibility Assessment
            </a>
            <a href="/start-here" className={styles.secondaryButton}>
              See the Complete Roadmap
            </a>
          </div>
        </section>
      </div>
    </div>
  );
}
