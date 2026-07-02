import TrackedLink from '@/components/TrackedLink';
import styles from '@/styles/BinderCTA.module.css';

interface BinderCTAProps {
  /** Where this CTA is placed, for GA4 attribution (e.g. "permitting-hub"). */
  context: string;
  /** Optional lead-in tailored to the surrounding page. */
  lead?: string;
}

/**
 * Contextual cross-sell for the $97 Job Site Binder. Place on pages where the
 * reader is dealing with the paperwork the product solves (permits,
 * inspections, subs, checklists).
 */
export default function BinderCTA({ context, lead }: BinderCTAProps) {
  return (
    <aside className={styles.binderCta}>
      <p className={styles.kicker}>From the shop</p>
      <h3 className={styles.title}>The Owner-Builder Job Site Binder System</h3>
      <p className={styles.copy}>
        {lead ??
          'Every checklist, contract, inspection form, and tracking sheet for your build — 229 pages of print-ready templates, organized the way a GC organizes a job.'}
      </p>
      <TrackedLink
        eventName="shop_cta_click"
        eventParams={{ location: 'binder_cta', context }}
        href="/shop"
        className={styles.button}
      >
        See what&apos;s inside — $97
      </TrackedLink>
    </aside>
  );
}
