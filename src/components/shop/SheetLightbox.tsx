'use client';

import { useEffect, useRef, useState } from 'react';
import { trackEvent } from '@/lib/analytics';
import styles from '@/app/shop/product.module.css';

interface SheetLightboxProps {
  /** Stripe checkout link for this kit, so the moment of conviction has a buy button. */
  checkoutUrl: string;
  /** Kit slug for event attribution (nc-permit-kit). */
  slug: string;
  /** GA4 location prefix for this kit (nck, gak, …). */
  ev: string;
  price: number;
}

interface Open {
  src: string;
  alt: string;
  caption: string;
}

/**
 * Tap any page image on a kit page to read it at full size. The product page
 * shows three real pages per kit, but at thumbnail width the citations are
 * illegible — and the citations are the product. One listener on the page
 * (every <img data-sheet> opens here), a native <dialog>, no library.
 */
export default function SheetLightbox({ checkoutUrl, slug, ev, price }: SheetLightboxProps) {
  const ref = useRef<HTMLDialogElement>(null);
  const [open, setOpen] = useState<Open | null>(null);

  useEffect(() => {
    function onClick(e: MouseEvent) {
      const img = (e.target as HTMLElement | null)?.closest<HTMLImageElement>('img[data-sheet]');
      if (!img) return;
      e.preventDefault();
      const caption = img.dataset.caption || img.alt || '';
      setOpen({ src: img.currentSrc || img.src, alt: img.alt, caption });
      trackEvent('sheet_zoom', { item_name: slug, location: `${ev}_${img.dataset.sheet}` });
    }
    document.addEventListener('click', onClick);
    return () => document.removeEventListener('click', onClick);
  }, [slug, ev]);

  useEffect(() => {
    const d = ref.current;
    if (!d) return;
    if (open && !d.open) d.showModal();
    if (!open && d.open) d.close();
  }, [open]);

  return (
    <dialog
      ref={ref}
      className={styles.lightbox}
      aria-label={open?.caption || 'Kit page'}
      onClose={() => setOpen(null)}
      onClick={(e) => {
        // Backdrop click closes; clicks inside the figure do not.
        if (e.target === e.currentTarget) setOpen(null);
      }}
    >
      {open && (
        <div className={styles.lightboxInner}>
          <img src={open.src} alt={open.alt} width={700} height={906} className={styles.lightboxImg} />
          <div className={styles.lightboxBar}>
            <span className={styles.lightboxCap}>{open.caption}</span>
            <a
              href={checkoutUrl}
              className={styles.btnPrimary}
              onClick={() =>
                trackEvent('begin_checkout', {
                  currency: 'USD',
                  value: price,
                  item_name: slug,
                  location: `${ev}_lightbox`,
                })
              }
            >
              Get the kit — ${price}
            </a>
            <button type="button" className={styles.lightboxClose} onClick={() => setOpen(null)} aria-label="Close">
              ×
            </button>
          </div>
        </div>
      )}
    </dialog>
  );
}
