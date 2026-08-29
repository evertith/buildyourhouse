import Link from 'next/link';
import styles from '@/styles/PlanningTools.module.css';

/**
 * "Plan your build" link module for the state guides — routes readers (and
 * link equity) from the permitting cluster into the calculators and planning
 * pages, which otherwise get no inbound links from the site's highest-traffic
 * section.
 */
export default function PlanningTools() {
  return (
    <aside className={styles.planningTools}>
      <h3 className={styles.title}>Plan Your Build</h3>
      <p className={styles.copy}>
        Permits sorted? Put numbers to the rest of the project with our free planning tools:
      </p>
      <ul className={styles.links}>
        <li>
          <Link href="/feasibility/cost-savings-calculator">
            Cost savings calculator — what acting as your own GC saves
          </Link>
        </li>
        <li>
          <Link href="/calculators/budget-tracker">
            Budget tracker — line-item costs with a contingency built in
          </Link>
        </li>
        <li>
          <Link href="/calculators/timeline-estimator">
            Timeline estimator — how long your build will realistically take
          </Link>
        </li>
        <li>
          <Link href="/planning/budget">Setting a realistic construction budget</Link>
        </li>
        <li>
          <Link href="/financing">Construction financing for owner-builders</Link>
        </li>
      </ul>
    </aside>
  );
}
