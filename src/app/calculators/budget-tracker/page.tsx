import BinderCTA from '@/components/BinderCTA';
import BudgetTrackerCalculator from '@/components/BudgetTrackerCalculator';
import type { Metadata } from 'next';
import styles from '../../feasibility/cost-savings-calculator/calculator-page.module.css';

export const metadata: Metadata = {
  alternates: { canonical: '/calculators/budget-tracker' },
  title: 'Free Construction Budget Tracker — Budgeted vs. Actual Costs',
  description: 'Track your owner-builder budget in real time. Compare budgeted vs. actual costs by phase, spot overruns early, and stay on track.',
};

export default function BudgetTrackerPage() {
  return (
    <div className={styles.page}>
      <div className={styles.container}>
        <header className={styles.header}>
          <h1>Build Budget Tracker</h1>
          <p className={styles.subtitle}>
            Stay on top of your construction costs with real-time budget tracking. Compare your
            budgeted amounts to actual spending by phase, monitor your contingency reserve, and get
            actionable recommendations when variances occur. Knowledge is power when managing a six-figure project.
          </p>
        </header>

        <BudgetTrackerCalculator />

        <section className={styles.info}>
          <h2>Why Budget Tracking Matters</h2>

          <div className={styles.infoGrid}>
            <div className={styles.infoCard}>
              <h3>Early Warning System</h3>
              <p>
                The worst thing that can happen is discovering you're over budget when you're 80% done.
                Tracking budget vs. actual costs by phase gives you early warning when costs are trending
                high, allowing you to adjust before it's too late.
              </p>
              <p>
                <strong>Real example:</strong> If your foundation came in 15% over budget, you know
                immediately to cut costs on finishes or increase your loan amount - not at the end when
                you can't afford cabinets.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Variance Analysis</h3>
              <p>
                Understanding where and why you're over or under budget helps you make better decisions
                going forward. Was framing over budget because of lumber price increases? Poor estimating?
                Scope creep? Each cause requires a different response.
              </p>
              <p>
                <strong>Key insight:</strong> Small overruns on early phases compound. A 10% overrun
                on foundation, framing, and rough-ins leaves you 30% over budget before you reach finishes.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Contingency Management</h3>
              <p>
                Your contingency reserve (typically 10-20% of budget) is your safety net. Tracking how
                much contingency you've used versus how much project remains helps you gauge risk and
                make strategic decisions.
              </p>
              <p>
                <strong>Rule of thumb:</strong> If you've used more than 50% of contingency by the
                50% completion mark, you're likely headed for budget trouble. Time to make cuts.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Scope Control</h3>
              <p>
                Budget tracking forces discipline around scope changes. When you see real numbers,
                it's easier to say no to that expensive upgrade. Every "small" change shows up as
                variance, making the cumulative impact visible.
              </p>
              <p>
                <strong>Owner-builder trap:</strong> DIY builders often add features mid-build
                ("while we're at it"). These "small" upgrades can blow your budget without tracking.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Cash Flow Planning</h3>
              <p>
                Knowing your actual vs. budgeted spend helps you plan when you'll need cash. If you're
                consistently under budget, you can delay draws. If over budget, you need to arrange
                additional funding before you run out.
              </p>
              <p>
                <strong>Critical timing:</strong> Running out of cash mid-project is catastrophic.
                Track spending to ensure you have funds when needed for each phase.
              </p>
            </div>

            <div className={styles.infoCard}>
              <h3>Post-Project Learning</h3>
              <p>
                Detailed budget tracking creates a record of what your home actually cost to build.
                This is valuable for insurance, future sales, additions, or helping other owner-builders
                plan their projects.
              </p>
              <p>
                <strong>Tax benefit:</strong> Detailed cost records help establish your cost basis
                for capital gains calculations if you ever sell.
              </p>
            </div>
          </div>
        </section>

        <section className={styles.reality}>
          <h2>Common Budget Challenges</h2>
          <p>
            Based on 15+ years of managing construction budgets, here are the issues that derail
            owner-builder budgets:
          </p>

          <div className={styles.considerations}>
            <div className={styles.consideration}>
              <h4>Optimistic Initial Budgets</h4>
              <p>
                Most owner-builders start with unrealistic budgets. They use best-case pricing, forget
                entire categories (site work, permits, landscaping), and underestimate finish costs.
                Build contingency and pad estimates by 10-15%.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Scope Creep</h4>
              <p>
                "While we're at it" is the most expensive phrase in construction. Adding a window here,
                upgrading a fixture there - these add up to thousands. Track every change as variance
                to see the cumulative impact.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Material Price Volatility</h4>
              <p>
                Lumber, concrete, and steel prices swing 30-100% in a year. Your budget from six months
                ago may be worthless. Update material estimates based on current quotes before each phase.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Forgotten Costs</h4>
              <p>
                Permits, impact fees, utility connections, temporary power, dumpsters, tool rental,
                insurance - the "soft costs" add up to 8-15% of hard costs but are often forgotten in
                initial budgets.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Rework & Mistakes</h4>
              <p>
                First-time builders make mistakes. Failed inspections require rework. Changed minds
                require demolition and reinstallation. Budget 5-10% for learning curve costs.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Finish Fever</h4>
              <p>
                As the house takes shape, people get excited and upgrade finishes. Premium countertops,
                better tile, upgraded fixtures - finish costs often exceed budget by 20-40%. Set limits
                early and stick to them.
              </p>
            </div>
          </div>
        </section>

        <section className={styles.reality} style={{ backgroundColor: 'var(--color-bg-light)', marginTop: '3rem' }}>
          <h2>Budget Management Best Practices</h2>
          <p>
            Here's how successful owner-builders manage their budgets:
          </p>

          <div className={styles.considerations}>
            <div className={styles.consideration}>
              <h4>Update Weekly</h4>
              <p>
                Review and update your budget tracker every week. Enter all expenditures, get quotes
                for upcoming work, and adjust estimates for remaining phases. Weekly updates catch
                problems early when you can still fix them.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Track Everything</h4>
              <p>
                Every receipt, every payment, every material purchase - track it all. Use a dedicated
                credit card or checking account for the build. This makes tracking easier and separates
                construction costs from personal spending.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Get Three Quotes</h4>
              <p>
                For any subcontracted work over $5,000, get three quotes. This validates your budget
                estimates and ensures you're getting fair pricing. Always compare apples to apples -
                same scope, same materials.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Front-Load Contingency</h4>
              <p>
                Use contingency strategically on foundation and framing - getting these right matters
                most. Don't "save" contingency for finishes. If you get to finishes under budget, you
                can upgrade. If over budget, you can downgrade finishes easier than fixing foundation.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Communicate with Lender</h4>
              <p>
                If using construction financing, keep your lender updated on budget status. If you see
                overruns coming, discuss additional funding options early. Last-minute funding requests
                are expensive and often declined.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Build a Cash Reserve</h4>
              <p>
                Beyond your contingency, maintain a personal cash reserve (5-10% of budget) for timing
                gaps in construction financing or unexpected personal emergencies during the build.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Set Phase Gates</h4>
              <p>
                Before starting each new phase, review budget status. If you're over budget, identify
                cuts in the next phase before committing to work. It's easier to cut costs you haven't
                spent than to claw back money.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>Track Labor Separately</h4>
              <p>
                Separately track what you pay subcontractors vs. what you save doing work yourself.
                This validates your cost savings calculator estimates and helps you decide which tasks
                to DIY vs. hire out.
              </p>
            </div>
          </div>
        </section>

        <section className={styles.reality} style={{ backgroundColor: '#fff3cd', marginTop: '3rem' }}>
          <h2>When You're Over Budget</h2>
          <p>
            If your tracker shows you're headed over budget, here are your options in order of preference:
          </p>

          <div className={styles.considerations}>
            <div className={styles.consideration}>
              <h4>1. Use Contingency Reserve</h4>
              <p>
                This is what contingency is for. If you're 5-10% over on a phase, use contingency to
                cover it but make cuts elsewhere to replenish the reserve.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>2. Downgrade Finishes</h4>
              <p>
                The easiest cuts are finishes you haven't purchased yet. Switch from hardwood to luxury
                vinyl, granite to laminate, or custom cabinets to stock. You can always upgrade later.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>3. Do More Yourself</h4>
              <p>
                Increase your DIY percentage on upcoming phases. Paint, trim, flooring, and landscaping
                are all DIY-friendly and can save 30-50% over hiring out.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>4. Reduce Scope</h4>
              <p>
                Eliminate nice-to-have features. Skip the deck, finish the basement later, reduce
                landscaping scope, or eliminate the garage. Reduce scope before cutting quality on
                structural items.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>5. Defer Work</h4>
              <p>
                Complete the home to certificate of occupancy standards, then finish non-essential
                items after move-in. Fencing, landscaping, garage, and basement can wait.
              </p>
            </div>

            <div className={styles.consideration}>
              <h4>6. Increase Funding</h4>
              <p>
                As a last resort, request additional construction financing, take a personal loan,
                or use savings. This is expensive and should only be used for essential structural
                items you can't defer or downgrade.
              </p>
            </div>
          </div>
        </section>

        <BinderCTA
          context="budget-tracker"
          lead="Ready to track a real budget? The Job Site Binder includes an auto-calculating Excel budget workbook — 21 cost categories with live variance and subtotal formulas — plus the printed tracking sheets for the job site."
        />

        <section className={styles.nextSteps}>
          <h2>Next Steps</h2>
          <p>Continue planning your owner-builder project with our other calculators.</p>
          <div className={styles.ctaButtons}>
            <a href="/calculators/material-estimator" className={styles.primaryButton}>
              Estimate Materials
            </a>
            <a href="/calculators/timeline-estimator" className={styles.secondaryButton}>
              Estimate Timeline
            </a>
          </div>
        </section>
      </div>
    </div>
  );
}
