'use client';

import { Suspense, useEffect, useState } from 'react';
import { useSearchParams } from 'next/navigation';
import { trackEvent } from '@/lib/analytics';
import styles from '../transaction.module.css';

const WORKER_BASE_URL = 'https://buildyourhouse-downloads.azerothcorner.workers.dev';

function downloadUrl(sessionId: string) {
  return `${WORKER_BASE_URL}/download?session_id=${encodeURIComponent(sessionId)}`;
}

interface OrderProduct {
  sku: string;
  name: string;
  kind: 'download' | 'ship';
  amountCents?: number;
}

// Fallback prices for sessions served by a worker build that predates
// amountCents in /order-info. Keep in sync with workers/downloads PRODUCTS.
const SKU_PRICES: Record<string, number> = {
  'job-site-binder': 97,
  'nc-permit-kit': 34,
  'ga-permit-kit': 34,
  'va-permit-kit': 34,
  'tx-permit-kit': 34,
  'sub-hiring-pack': 29,
  'printed-binder': 149,
};

// Worded to hold for every SKU in the shop, not just the binder — the same
// page confirms a $29 pack and a $149 printed edition.
const STEPS: { no: string; title: string; copy: string }[] = [
  {
    no: 'Step 01',
    title: 'Download & unzip',
    copy: 'Save the ZIP file to your computer and extract it. You’ll find the documents organized into folders.',
  },
  {
    no: 'Step 02',
    title: 'Read the how-to-use guide',
    copy: 'Open the how-to-use document first. It walks you through what’s in the download and the order to work through it.',
  },
  {
    no: 'Step 03',
    title: 'Print & assemble',
    copy: 'Print at home or take the PDFs to an office supply store. A 3-ring binder with tab dividers keeps each section findable.',
  },
  {
    no: 'Step 04',
    title: 'Build with confidence',
    copy: 'Take the paper to the job site. Everything you need is organized and ready — no phone required.',
  },
];

function CropMarks() {
  return (
    <>
      <span className={`${styles.crop} ${styles.tl}`} />
      <span className={`${styles.crop} ${styles.tr}`} />
      <span className={`${styles.crop} ${styles.bl}`} />
      <span className={`${styles.crop} ${styles.br}`} />
    </>
  );
}

function SuccessContent() {
  const searchParams = useSearchParams();
  const sessionId = searchParams.get('session_id');
  const [product, setProduct] = useState<OrderProduct | null>(null);

  // Resolve the session to its actual SKU before tracking, so the GA4
  // purchase carries the real product and price (not a hardcoded one) and
  // never fires for unpaid/bogus session ids. Deduped per Stripe session so
  // reloads/back-navigation don't double-count the sale.
  useEffect(() => {
    if (!sessionId) return;
    let cancelled = false;
    (async () => {
      let info: { paid?: boolean; product?: OrderProduct };
      try {
        const res = await fetch(
          `${WORKER_BASE_URL}/order-info?session_id=${encodeURIComponent(sessionId)}`
        );
        if (!res.ok) return;
        info = await res.json();
      } catch {
        return; // Worker unreachable — skip tracking rather than fabricate a sale.
      }
      if (cancelled || !info.paid || !info.product) return;
      setProduct(info.product);

      const dedupeKey = `purchase_tracked_${sessionId}`;
      try {
        if (sessionStorage.getItem(dedupeKey)) return;
        sessionStorage.setItem(dedupeKey, '1');
      } catch {
        // Storage unavailable (private mode) — still track; worst case is a rare double-count.
      }
      const value =
        info.product.amountCents != null
          ? info.product.amountCents / 100
          : SKU_PRICES[info.product.sku] ?? 0;
      trackEvent('purchase', {
        transaction_id: sessionId,
        currency: 'USD',
        value,
        items: [
          {
            item_id: info.product.sku,
            item_name: info.product.name,
            price: value,
            quantity: 1,
          },
        ],
      });
    })();
    return () => {
      cancelled = true;
    };
  }, [sessionId]);

  if (!sessionId) {
    return (
      <div className={styles.page}>
        <section className={`${styles.hero} bp-band bp-grid`}>
          <CropMarks />
          <div className={styles.heroInner}>
            <div className={styles.heroBody}>
              <div className={`${styles.eyebrow} bp-eyebrow`}>No order on this link</div>
              <h1 className={styles.heroTitle}>Looking for your download?</h1>
              <p className={styles.heroSub}>
                This page needs an order attached to it, and there isn’t one.
              </p>
              <p className={styles.heroCopy}>
                If you already bought from the shop, check your email for the receipt from
                Stripe — it confirms your order. To get your files again, look the order up
                with the email address you paid with.
              </p>
              <div className={styles.heroCtas}>
                <a href="/shop/recover" className={styles.btnPrimary}>
                  Recover my download
                </a>
                <a href="/shop" className={styles.btnGhost}>
                  Go to the shop
                </a>
              </div>
            </div>
          </div>
        </section>
      </div>
    );
  }

  return (
    <div className={styles.page}>
      {/* ---------- CONFIRMATION + DOWNLOAD ---------- */}
      <section className={`${styles.hero} bp-band bp-grid`}>
        <CropMarks />
        <div className={styles.heroInner}>
          <div className={styles.heroBody}>
            <div className={`${styles.eyebrow} bp-eyebrow`}>Payment received</div>
            <h1 className={styles.heroTitle}>Thank you for your purchase.</h1>
            <p className={styles.heroSub}>
              {product?.kind === 'ship'
                ? 'Your printed binder is headed to production — and your digital copy is ready to download right now.'
                : `Your ${product?.name ?? 'purchase'} is ready to download.`}
            </p>
            <p className={styles.heroCopy}>
              You’ll also receive a receipt from Stripe at the email you provided.
            </p>

            <div className={styles.receipt}>
              <div className={styles.rcell}>
                <span className={styles.k}>Product</span>
                <span className={`${styles.v} ${styles.vName}`}>
                  {product?.name ?? 'Your purchase'}
                </span>
              </div>
              <div className={styles.rcell}>
                <span className={styles.k}>Access</span>
                <span className={styles.v}>Lifetime</span>
              </div>
              <div className={styles.rcell}>
                <span className={styles.k}>Order ref</span>
                <span className={`${styles.v} ${styles.vMono}`}>
                  {sessionId.slice(-8).toUpperCase()}
                </span>
              </div>
            </div>

            <div className={styles.heroCtas}>
              <a
                href={downloadUrl(sessionId)}
                className={`${styles.btnPrimary} ${styles.btnBig}`}
                onClick={() =>
                  trackEvent('binder_download', {
                    item_name: product?.sku ?? 'unknown',
                  })
                }
              >
                Download your files (ZIP)
              </a>
            </div>

            <p className={styles.heroFine}>
              ZIP file with print-ready PDFs{product?.sku === 'sub-hiring-pack'
                ? ' plus editable Word contract documents'
                : product?.sku === 'job-site-binder' || product?.sku === 'printed-binder'
                  ? ', editable Word contracts, and Excel budget workbooks'
                  : ''}
            </p>
          </div>
        </div>
      </section>

      {/* ---------- WHAT TO DO NEXT ---------- */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>What to do next</div>
              <h2 className={styles.secTitle}>From download to job site</h2>
            </div>
            <div className={styles.secMeta}>
              Print at home
              <br />
              or at a copy shop
            </div>
          </div>

          <div className={styles.steps}>
            {STEPS.map((s) => (
              <div key={s.no} className={styles.step}>
                <span className={styles.stepNo}>{s.no}</span>
                <h3 className={styles.stepTitle}>{s.title}</h3>
                <p className={styles.stepCopy}>{s.copy}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ---------- KEEP THE FILE ---------- */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.panel}>
            <div className={styles.panelNo}>
              <span>Keep this</span>
              <span>Lifetime access</span>
            </div>
            <h2 className={styles.panelTitle}>Save the file somewhere safe</h2>
            <p className={styles.panelCopy}>
              Your download doesn’t expire. If you ever lose the ZIP — new computer, wiped
              downloads folder, deleted email — you can recover it any time with the email
              address you used at checkout.
            </p>
            <a className={styles.panelLink} href="/shop/recover">
              Recover a download <span aria-hidden="true">→</span>
            </a>
          </div>
        </div>
      </section>
    </div>
  );
}

export default function SuccessPage() {
  return (
    <Suspense
      fallback={
        <div className={styles.page}>
          <section className={`${styles.hero} bp-band bp-grid`}>
            <CropMarks />
            <div className={styles.heroInner}>
              <div className={styles.heroBody}>
                <div className={`${styles.eyebrow} bp-eyebrow`}>Payment received</div>
                <h1 className={styles.heroTitle}>Thank you for your purchase.</h1>
                <p className={styles.loading}>Loading your order…</p>
              </div>
            </div>
          </section>
        </div>
      }
    >
      <SuccessContent />
    </Suspense>
  );
}
