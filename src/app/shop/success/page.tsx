'use client';

import { Suspense, useEffect, useState } from 'react';
import { useSearchParams } from 'next/navigation';
import Section from '@/components/Section';
import { trackEvent } from '@/lib/analytics';

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
      <div className="content-container">
        <Section spacing="large">
          <div style={{ textAlign: 'center', maxWidth: '600px', margin: '0 auto' }}>
            <h1 style={{ fontSize: 'var(--text-3xl)', marginBottom: 'var(--space-6)' }}>
              Looking for Your Download?
            </h1>
            <p style={{
              fontSize: 'var(--text-lg)',
              color: 'var(--text-secondary)',
              marginBottom: 'var(--space-8)',
              lineHeight: 'var(--leading-relaxed)',
            }}>
              If you already purchased the Job Site Binder System, check your email for
              the receipt from Stripe — it contains your order confirmation.
            </p>
            <a
              href="/shop"
              className="button button-large"
              style={{
                fontSize: 'var(--text-lg)',
                padding: 'var(--space-4) var(--space-10)',
              }}
            >
              Go to Shop
            </a>
          </div>
        </Section>
      </div>
    );
  }

  return (
    <div className="content-container">
      <Section spacing="large">
        <div style={{ textAlign: 'center', maxWidth: '700px', margin: '0 auto' }}>
          <div style={{ fontSize: 'var(--text-4xl)', marginBottom: 'var(--space-4)' }}>
            &#10003;
          </div>
          <h1 style={{
            fontSize: 'var(--text-3xl)',
            marginBottom: 'var(--space-4)',
            lineHeight: 'var(--leading-tight)',
          }}>
            Thank You for Your Purchase!
          </h1>
          <p style={{
            fontSize: 'var(--text-lg)',
            color: 'var(--text-secondary)',
            marginBottom: 'var(--space-10)',
            lineHeight: 'var(--leading-relaxed)',
          }}>
            {product?.kind === 'ship'
              ? 'Your printed binder is headed to production — and your digital copy is ready to download right now.'
              : `Your ${product?.name ?? 'purchase'} is ready to download.`}{' '}
            You&apos;ll also receive a receipt from Stripe at the email you provided.
          </p>

          <a
            href={downloadUrl(sessionId)}
            className="button button-large"
            style={{
              fontSize: 'var(--text-xl)',
              padding: 'var(--space-6) var(--space-12)',
            }}
            onClick={() =>
              trackEvent('binder_download', {
                item_name: product?.sku ?? 'unknown',
              })
            }
          >
            Download Your Files (ZIP)
          </a>

          <p style={{
            marginTop: 'var(--space-3)',
            fontSize: 'var(--text-sm)',
            color: 'var(--text-secondary)',
          }}>
            ZIP file with print-ready PDFs{product?.sku === 'sub-hiring-pack'
              ? ' plus editable Word contract documents'
              : product?.sku === 'job-site-binder' || product?.sku === 'printed-binder'
                ? ', editable Word contracts, and Excel budget workbooks'
                : ''}
          </p>

          <p style={{
            marginTop: 'var(--space-2)',
            fontSize: 'var(--text-sm)',
            color: 'var(--text-secondary)',
          }}>
            Save the file somewhere safe. If you ever lose it, you can recover
            your download at{' '}
            <a href="/shop/recover">build-your-house.com/shop/recover</a> with
            your purchase email.
          </p>
        </div>
      </Section>

      <Section title="What to Do Next" spacing="large" background="warm">
        <div className="how-it-works-grid">
          <div className="step-card">
            <div className="step-number">1</div>
            <h3>Download & Unzip</h3>
            <p>
              Save the ZIP file to your computer and extract it.
              You&apos;ll find organized folders for each binder section.
            </p>
          </div>

          <div className="step-card">
            <div className="step-number">2</div>
            <h3>Read the How-to-Use Guide</h3>
            <p>
              Open &ldquo;HOW TO USE THIS BINDER&rdquo; first. It walks you
              through how to assemble your binder step by step.
            </p>
          </div>

          <div className="step-card">
            <div className="step-number">3</div>
            <h3>Print & Assemble</h3>
            <p>
              Print at home or take to an office supply store.
              Use a 3-ring binder with tab dividers for each section.
            </p>
          </div>

          <div className="step-card">
            <div className="step-number">4</div>
            <h3>Build With Confidence</h3>
            <p>
              Take your binder to the job site. Everything you need
              is organized and ready — no phone required.
            </p>
          </div>
        </div>
      </Section>
    </div>
  );
}

export default function SuccessPage() {
  return (
    <Suspense fallback={
      <div className="content-container">
        <Section spacing="large">
          <div style={{ textAlign: 'center' }}>
            <p style={{ fontSize: 'var(--text-lg)', color: 'var(--text-secondary)' }}>
              Loading...
            </p>
          </div>
        </Section>
      </div>
    }>
      <SuccessContent />
    </Suspense>
  );
}
