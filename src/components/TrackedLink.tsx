'use client';

import React from 'react';
import { trackEvent } from '@/lib/analytics';

interface TrackedLinkProps extends React.AnchorHTMLAttributes<HTMLAnchorElement> {
  eventName: string;
  eventParams?: Record<string, string | number | boolean | undefined>;
}

/**
 * Anchor that fires a GA4 event on click. Use for outbound conversion links
 * on server-component pages (e.g. the Stripe checkout link on /shop).
 */
export default function TrackedLink({ eventName, eventParams, onClick, children, ...anchor }: TrackedLinkProps) {
  return (
    <a
      {...anchor}
      onClick={(e) => {
        trackEvent(eventName, eventParams);
        onClick?.(e);
      }}
    >
      {children}
    </a>
  );
}
