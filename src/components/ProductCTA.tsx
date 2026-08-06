import TrackedLink from '@/components/TrackedLink';
import styles from '@/styles/ProductCTA.module.css';

interface ProductCTAProps {
  /** Product page this CTA sends the reader to (e.g. "/shop/nc-permit-kit"). */
  href: string;
  /** Product name — the heading of the aside. */
  title: string;
  /** Why the reader of *this* page wants it, in their terms. */
  lead: string;
  /** Whole dollars. Rendered on the button. */
  price: number;
  /** Where this CTA is placed, for GA4 attribution (e.g. "vetting-and-interviewing"). */
  context: string;
  /** Product SKU, for GA4 attribution. */
  sku: string;
  /** Overrides the "From the shop" kicker. */
  kicker?: string;
  /** Overrides the default button label. */
  cta?: string;
}

/**
 * Contextual cross-sell for the smaller shop SKUs — the NC Permit Kit and the
 * Subcontractor Hiring Pack. Same placement rule as {@link BinderCTA}: put it
 * where the reader is already dealing with the paperwork the product solves.
 * Reach for BinderCTA instead when the whole $97 system is the right answer.
 */
export default function ProductCTA({
  href,
  title,
  lead,
  price,
  context,
  sku,
  kicker,
  cta,
}: ProductCTAProps) {
  return (
    <aside className={styles.productCta}>
      <p className={styles.kicker}>{kicker ?? 'From the shop'}</p>
      <h3 className={styles.title}>{title}</h3>
      <p className={styles.copy}>{lead}</p>
      <TrackedLink
        eventName="shop_cta_click"
        eventParams={{ location: 'product_cta', context, item_name: sku }}
        href={href}
        className={styles.button}
      >
        {cta ?? 'See what’s inside'} — ${price}
      </TrackedLink>
    </aside>
  );
}
