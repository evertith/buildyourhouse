import Link from 'next/link';
import { STATE_KITS } from '@/lib/kits';
import { KIT_PRICE } from '@/lib/kit-content';
import styles from '@/styles/StatePlate.module.css';

interface StatePlateProps {
  /**
   * What a state with no kit yet does when clicked. 'anchor' links it to
   * `comingHref` (the hub's request form); 'inert' renders it unclickable,
   * for surfaces where 46 links to the same anchor would be noise.
   */
  coming?: 'anchor' | 'inert';
  comingHref?: string;
}

/**
 * Sorted by postal code, not by state name: the code is the only thing a cell
 * shows, so it has to be the sort key or the grid reads as unsorted. (The kit
 * index on the hub shows full state names and is ordered by those instead.)
 * Fixed order, never grouped by status — the plate is a lookup table, so a
 * state has to stay where the reader last found it.
 */
const cellOrder = [...STATE_KITS].sort((a, b) => a.code.localeCompare(b.code));

/**
 * The coverage plate: all 50 states as a fixed grid of postal codes, issued
 * kits filled in.
 *
 * Reads straight from STATE_KITS, so the only thing that changes as a state
 * ships is that its cell fills. At 4 issued the plate reads as a program
 * that has started; at 50 it reads as one that finished.
 */
export default function StatePlate({
  coming = 'anchor',
  comingHref = '#request',
}: StatePlateProps) {
  return (
    <div className={styles.plate}>
      {cellOrder.map((k) => {
        const code = k.code.toUpperCase();

        if (k.status === 'shipped') {
          return (
            <Link
              key={k.slug}
              href={`/shop/${k.slug}`}
              className={`${styles.cell} ${styles.issued}`}
              aria-label={`${k.state} permit kit, $${KIT_PRICE}`}
            >
              <span className={styles.code}>{code}</span>
              <span className={styles.tick}>${KIT_PRICE}</span>
            </Link>
          );
        }

        const inner = (
          <>
            <span className={styles.code}>{code}</span>
            <span className={styles.tick} aria-hidden="true">
              &mdash;
            </span>
            <span className="visually-hidden">{k.state} — in production</span>
          </>
        );

        return coming === 'anchor' ? (
          <a key={k.slug} href={comingHref} className={`${styles.cell} ${styles.pending}`}>
            {inner}
          </a>
        ) : (
          <span key={k.slug} className={`${styles.cell} ${styles.pending}`}>
            {inner}
          </span>
        );
      })}
    </div>
  );
}
