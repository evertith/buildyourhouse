import React from 'react';
import { amazonProductUrl, amazonSearchUrl } from '@/lib/affiliate';

interface AmazonLinkProps {
  /** Direct product link by ASIN. Takes precedence over `search`. */
  asin?: string;
  /** Tagged search link (preferred for evergreen content). Falls back to the link text. */
  search?: string;
  children: React.ReactNode;
}

/**
 * Inline, properly-tagged Amazon affiliate link.
 * rel="sponsored nofollow" satisfies both Google's paid-link policy and
 * Amazon's requirement that affiliate links are disclosed/marked.
 */
export default function AmazonLink({ asin, search, children }: AmazonLinkProps) {
  const text = typeof children === 'string' ? children : (search ?? '');
  const href = asin ? amazonProductUrl(asin) : amazonSearchUrl(search ?? text);
  return (
    <a href={href} target="_blank" rel="sponsored nofollow noopener noreferrer">
      {children}
    </a>
  );
}
