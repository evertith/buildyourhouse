import Link from 'next/link';
import ImpressionSentinel from '@/components/ImpressionSentinel';
import TrackedLink from '@/components/TrackedLink';
import styles from '@/styles/DecisionFork.module.css';

/** Where the hiring-a-builder track lives. One place to change when the state guides for hiring exist. */
export const HIRING_TRACK_HREF = '/hiring-a-builder';

interface Props {
  /** Two-letter state code. */
  code: string;
  /** Display name — "Nebraska". */
  state: string;
}

/**
 * The one-line fork under every Quick Answer. Most readers give a guide one
 * screen; this is the screen. A reader who has just decided against
 * owner-building gets a door instead of a dead end, and the click is the
 * demand signal for the hiring-a-builder track.
 */
export default function DecisionFork({ code, state }: Props) {
  return (
    <p className={`${styles.fork} no-print`}>
      <ImpressionSentinel placement="decision-fork" params={{ state: code }} />
      <span className={styles.branch}>
        <span className={styles.k}>Building it yourself?</span> Keep reading.
      </span>
      <span className={styles.branch}>
        <span className={styles.k}>Hiring a builder in {state}?</span>{' '}
        <TrackedLink
          href={`${HIRING_TRACK_HREF}?state=${code}`}
          eventName="fork_hire_click"
          eventParams={{ state: code }}
          className={styles.link}
        >
          Start here instead →
        </TrackedLink>
      </span>
      <Link href="/permitting/state-guides" className={styles.all}>
        All 50 states
      </Link>
    </p>
  );
}
