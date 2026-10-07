/**
 * Lender sponsorship — the on-site half of a signed deal, per state.
 *
 * Flat-fee advertising only (RESPA posture, see lenders.ts): a sponsor buys
 * placement, never per-lead or per-closing compensation, and the placement
 * is labeled Sponsored wherever it renders (rel="sponsored"). A sponsor must
 * meet the same inclusion standard as the editorial directory — its own
 * site must state that it accepts owner-builders — and its pitch is one
 * honest sentence approved by both sides.
 *
 * Empty map = no deals = the state module shows the editorial list and the
 * house ad that points lenders at the rate card.
 */

export interface StateSponsor {
  /** Matches a LENDERS id when the sponsor is also listed editorially. */
  lenderId?: string;
  name: string;
  url: string;
  /** One honest sentence, approved by the lender. */
  pitch: string;
  /** ISO date the placement started — shown nowhere, kept for the ledger. */
  since: string;
}

/** Keyed by two-letter state code. */
export const SPONSORS: Record<string, StateSponsor> = {};

export const SPONSOR_PAGE = '/financing/sponsor';
export const SPONSOR_CONTACT_EMAIL = 'info@build-your-house.com';

/** Rate card, USD per month. Founding rate is locked for 12 months for the first ten state sponsors. */
export const STATE_SPONSOR_PRICE = 149;
export const STATE_SPONSOR_FOUNDING_PRICE = 99;
export const STATE_SPONSOR_FOUNDING_SEATS = 10;
export const NATIONAL_SPONSOR_PRICE = 349;
export const SPONSOR_MIN_MONTHS = 3;

export function sponsorForState(code: string): StateSponsor | null {
  return SPONSORS[code.toUpperCase()] ?? null;
}

/**
 * Consented borrower introduction — the one exception to "we don't route form
 * submissions": a borrower from the match form agrees in writing to be
 * introduced to a named lender, and that lender pays a flat fee. One lender,
 * never resold, same fee whether or not a loan closes, refund if the borrower
 * declines. Sold from /financing/lead (noindex; Seth sends the link).
 */
export const LEAD_PRICE = 149;
export const LEAD_SKU = 'financing-lead';
export const LEAD_PAGE = '/financing/lead';
/** Stripe Payment Link for LEAD_SKU, created by the downloads worker's provision-products. */
export const LEAD_CHECKOUT_URL = 'https://buy.stripe.com/bJeaEXgAL54z6by3gnfAc0r';
