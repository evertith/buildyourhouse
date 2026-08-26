import TrackedLink from '@/components/TrackedLink';
import styles from '@/styles/PromoBanner.module.css';

/**
 * The House Year banner — sticky ad slot pinned under the header on every
 * page. Live-HTML version of the 2026-08-26 creative (plain download
 * message, no offer code): wheel mark, one-line pitch, Download Now.
 * Fraunces comes from the site's self-hosted next/font setup.
 */

/* Official 12-segment year wheel from the brand creative */
function Wheel({ className }: { className?: string }) {
  return (
    <svg className={className} viewBox="0 0 148 148" aria-hidden="true">
      <path d="M 76.6 0.0 A 74 74 0 0 1 108.7 8.7 L 95.6 33.4 A 46 46 0 0 0 75.6 28.0 Z" fill="#C9A25E" />
      <path d="M 113.2 11.2 A 74 74 0 0 1 136.8 34.8 L 113.0 49.6 A 46 46 0 0 0 98.4 35.0 Z" fill="#FDFBF6" />
      <path d="M 139.3 39.3 A 74 74 0 0 1 148.0 71.4 L 120.0 72.4 A 46 46 0 0 0 114.6 52.4 Z" fill="#FDFBF6" />
      <path d="M 148.0 76.6 A 74 74 0 0 1 139.3 108.7 L 114.6 95.6 A 46 46 0 0 0 120.0 75.6 Z" fill="#FDFBF6" />
      <path d="M 136.8 113.2 A 74 74 0 0 1 113.2 136.8 L 98.4 113.0 A 46 46 0 0 0 113.0 98.4 Z" fill="#FDFBF6" />
      <path d="M 108.7 139.3 A 74 74 0 0 1 76.6 148.0 L 75.6 120.0 A 46 46 0 0 0 95.6 114.6 Z" fill="#FDFBF6" />
      <path d="M 71.4 148.0 A 74 74 0 0 1 39.3 139.3 L 52.4 114.6 A 46 46 0 0 0 72.4 120.0 Z" fill="#FDFBF6" />
      <path d="M 34.8 136.8 A 74 74 0 0 1 11.2 113.2 L 35.0 98.4 A 46 46 0 0 0 49.6 113.0 Z" fill="#FDFBF6" />
      <path d="M 8.7 108.7 A 74 74 0 0 1 0.0 76.6 L 28.0 75.6 A 46 46 0 0 0 33.4 95.6 Z" fill="#FDFBF6" />
      <path d="M 0.0 71.4 A 74 74 0 0 1 8.7 39.3 L 33.4 52.4 A 46 46 0 0 0 28.0 72.4 Z" fill="#FDFBF6" />
      <path d="M 11.2 34.8 A 74 74 0 0 1 34.8 11.2 L 49.6 35.0 A 46 46 0 0 0 35.0 49.6 Z" fill="#FDFBF6" />
      <path d="M 39.3 8.7 A 74 74 0 0 1 71.4 0.0 L 72.4 28.0 A 46 46 0 0 0 52.4 33.4 Z" fill="#FDFBF6" />
    </svg>
  );
}

export default function PromoBanner() {
  return (
    <div className={`${styles.slot} no-print`}>
      <TrackedLink
        href="https://www.thehouseyear.com/?utm_source=buildyourhouse&utm_medium=banner&utm_campaign=download"
        target="_blank"
        rel="noopener"
        eventName="cross_promo_click"
        eventParams={{ destination: 'thehouseyear', location: 'leaderboard' }}
        className={styles.banner}
        aria-label="The House Year — keep up with your house's yearly maintenance. Download now."
      >
        <span className={styles.lead}>
          <Wheel className={styles.wheel} />
          <span className={styles.titles}>
            <span className={styles.kicker}>The House Year</span>
            <span className={styles.headline}>
              Keep up with your house&rsquo;s yearly maintenance.
            </span>
          </span>
        </span>
        <span className={styles.button}>Download Now</span>
      </TrackedLink>
    </div>
  );
}
