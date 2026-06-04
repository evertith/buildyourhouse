// Amazon Associates configuration + link builders.
//
// SINGLE SOURCE OF TRUTH for the tracking tag. Confirmed in Associates Central →
// "Manage Your Tracking IDs" on 2026-06-04: Amazon truncated the "BuildYourHouse"
// store ID to "buildyourho00-20". To override without a code change, set
// NEXT_PUBLIC_AMAZON_TAG. A wrong tag = links work but earn $0.
export const AMAZON_ASSOCIATE_TAG =
  process.env.NEXT_PUBLIC_AMAZON_TAG ?? 'buildyourho00-20';

// Required disclosure (Amazon Operating Agreement). Rendered site-wide in the footer.
export const AMAZON_DISCLOSURE =
  'As an Amazon Associate, Build-Your-House.com earns from qualifying purchases.';

const AMAZON_DOMAIN = 'https://www.amazon.com';

/** Direct product link by ASIN, with the associate tag appended. */
export function amazonProductUrl(asin: string): string {
  return `${AMAZON_DOMAIN}/dp/${encodeURIComponent(asin)}?tag=${AMAZON_ASSOCIATE_TAG}`;
}

/**
 * Tagged search link. Preferred for evergreen content: it never 404s when a
 * product goes out of stock, and still attributes whatever the reader buys in
 * that session to your tag.
 */
export function amazonSearchUrl(query: string): string {
  return `${AMAZON_DOMAIN}/s?k=${encodeURIComponent(query)}&tag=${AMAZON_ASSOCIATE_TAG}`;
}
