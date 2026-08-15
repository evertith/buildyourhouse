import TrackedLink from '@/components/TrackedLink';
import styles from '@/styles/PromoBanner.module.css';

/**
 * Site-wide announcement bar for The House Year (our home-maintenance app).
 * Sits above the sticky header, so it scrolls away once the reader dives in.
 */
export default function PromoBanner() {
  return (
    <TrackedLink
      href="https://www.thehouseyear.com"
      target="_blank"
      rel="noopener"
      eventName="cross_promo_click"
      eventParams={{ destination: 'thehouseyear', location: 'top_banner' }}
      className={`${styles.banner} no-print`}
    >
      <span className={styles.chip}>New</span>
      <span className={styles.name}>The House Year</span>
      <span className={styles.tag}> — a licensed contractor&apos;s plan for your specific house</span>
      <span className={styles.arrow} aria-hidden="true"> ↗</span>
    </TrackedLink>
  );
}
