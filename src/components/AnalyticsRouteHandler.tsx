"use client";

import { usePathname } from "next/navigation";
import { useEffect, useRef } from "react";

/**
 * Fires a GA4 page_view on client-side route changes. The gtag('config', ...)
 * call in layout.tsx only covers the initial document load; without this,
 * every next/link navigation on the site goes uncounted.
 */
export default function AnalyticsRouteHandler() {
  const pathname = usePathname();
  const isInitialLoad = useRef(true);

  useEffect(() => {
    // The initial page_view is sent by gtag('config') — skip it here to avoid double-counting.
    if (isInitialLoad.current) {
      isInitialLoad.current = false;
      return;
    }
    if (typeof window.gtag !== "function") return;
    window.gtag("event", "page_view", {
      page_path: pathname,
      page_location: window.location.href,
      page_title: document.title,
    });
  }, [pathname]);

  return null;
}
