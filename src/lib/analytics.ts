/**
 * Thin wrapper over the gtag.js queue loaded in layout.tsx (G-75MNQ8RDT7).
 * Safe to call anywhere: no-ops on the server and when gtag is blocked
 * (ad blockers strip the script, so window.gtag may never exist).
 */

declare global {
  interface Window {
    gtag?: (...args: unknown[]) => void;
  }
}

export function trackEvent(
  name: string,
  params?: Record<string, string | number | boolean | undefined>
): void {
  if (typeof window === 'undefined' || typeof window.gtag !== 'function') return;
  window.gtag('event', name, params);
}
