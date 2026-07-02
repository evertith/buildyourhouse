'use client';

import { Suspense, useEffect } from 'react';
import { useSearchParams } from 'next/navigation';
import Section from '@/components/Section';
import { trackEvent } from '@/lib/analytics';

const WORKER_BASE_URL = 'https://buildyourhouse-downloads.azerothcorner.workers.dev';

function downloadUrl(sessionId: string) {
  return `${WORKER_BASE_URL}/download?session_id=${encodeURIComponent(sessionId)}`;
}

function SuccessContent() {
  const searchParams = useSearchParams();
  const sessionId = searchParams.get('session_id');

  // GA4 purchase, deduped per Stripe session so reloads/back-navigation
  // don't double-count the sale.
  useEffect(() => {
    if (!sessionId) return;
    const dedupeKey = `purchase_tracked_${sessionId}`;
    try {
      if (sessionStorage.getItem(dedupeKey)) return;
      sessionStorage.setItem(dedupeKey, '1');
    } catch {
      // Storage unavailable (private mode) — still track; worst case is a rare double-count.
    }
    trackEvent('purchase', {
      transaction_id: sessionId,
      currency: 'USD',
      value: 97,
      item_name: 'job_site_binder',
    });
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
            Your Owner-Builder Job Site Binder System is ready to download.
            You&apos;ll also receive a receipt from Stripe at the email you provided.
          </p>

          <a
            href={downloadUrl(sessionId)}
            className="button button-large"
            style={{
              fontSize: 'var(--text-xl)',
              padding: 'var(--space-6) var(--space-12)',
            }}
            onClick={() => trackEvent('binder_download', { item_name: 'job_site_binder' })}
          >
            Download Your Binder System (ZIP)
          </a>

          <p style={{
            marginTop: 'var(--space-3)',
            fontSize: 'var(--text-sm)',
            color: 'var(--text-secondary)',
          }}>
            3.4 MB &bull; ZIP file containing PDFs, Word docs, and Excel spreadsheets
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
            <h3>Read the START HERE Guide</h3>
            <p>
              Open the &ldquo;START HERE&rdquo; PDF first. It walks you through
              how to assemble your binder step by step.
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
