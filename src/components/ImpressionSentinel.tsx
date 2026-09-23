'use client';

import { useEffect, useRef } from 'react';
import { trackEvent } from '@/lib/analytics';

interface Props {
  /** Placement id — 'kit-cta', 'code-alerts', 'state-lenders', 'lender-line', 'decision-fork', 'estimate-capture'. */
  placement: string;
  params?: Record<string, string | number | boolean | undefined>;
}

/** gtag.js is injected after hydration, so an element visible at load can intersect before analytics exists. Wait for it, bounded. */
function whenGtagReady(cb: () => void, tries = 40): void {
  if (typeof window !== 'undefined' && typeof window.gtag === 'function') return cb();
  if (tries <= 0) return;
  window.setTimeout(() => whenGtagReady(cb, tries - 1), 250);
}

/**
 * Fires one `placement_impression` event per page view when the PARENT
 * element is at least half visible (or fully visible, for elements taller
 * than the viewport). Drop it inside any block whose visibility matters
 * (a CTA, a capture, a sponsored slot) and the report stops guessing about
 * scroll depth. Renders nothing.
 */
export default function ImpressionSentinel({ placement, params }: Props) {
  const ref = useRef<HTMLSpanElement>(null);
  const paramsRef = useRef(params);
  paramsRef.current = params;

  useEffect(() => {
    const target = ref.current?.parentElement;
    if (!target || typeof IntersectionObserver === 'undefined') return;
    let fired = false;
    const io = new IntersectionObserver(
      (entries) => {
        if (fired) return;
        const hit = entries.some((e) => {
          if (!e.isIntersecting) return false;
          // Tall blocks (the lender module) can never reach 50% of their own
          // height inside a short viewport; count them once they fill it.
          const fillsViewport = e.intersectionRect.height >= (e.rootBounds?.height ?? Infinity) * 0.6;
          return e.intersectionRatio >= 0.5 || fillsViewport;
        });
        if (!hit) return;
        fired = true;
        io.disconnect();
        whenGtagReady(() => trackEvent('placement_impression', { placement, ...paramsRef.current }));
      },
      { threshold: [0, 0.25, 0.5, 0.75, 1] }
    );
    io.observe(target);
    return () => io.disconnect();
  }, [placement]);

  return <span ref={ref} hidden aria-hidden="true" />;
}
