/**
 * Editorial lender directory for /planning/financing.
 *
 * Facts verified against the lenders' public pages in August 2026 — state
 * footprints and terms change, so entries describe what each lender
 * ADVERTISES and the page tells readers to verify. Nobody here pays us
 * today; if a sponsorship ever exists it runs through FEATURED_LENDER
 * below and renders with a visible "Sponsored" label (and rel="sponsored").
 *
 * RESPA note (see lender-outreach/target-lenders.md): keep placements
 * flat-fee advertising or compliance-approved lead-gen; never present a
 * listing as an endorsement in exchange for per-closing fees.
 */

export interface LenderEntry {
  id: string;
  name: string;
  kind: 'Owner-builder specialist' | 'Regional lender';
  url: string;
  /** Display string, hedged to what the lender advertises. */
  states: string;
  /** What they advertise, in our words — no endorsement. */
  notes: string;
}

export const LENDERS: LenderEntry[] = [
  {
    id: 'owner-builder-loans',
    name: 'Owner Builder Loans, LLC',
    kind: 'Owner-builder specialist',
    url: 'https://www.ownerbuilderloans.com/',
    states: 'AZ · CA · CO · FL · GA · MI · SC · TX',
    notes:
      'Owner-builder construction loans are their entire business — no general contractor or project supervisor required. Advertises 12-month terms up to $700K, unlimited draws with no draw fees, and land equity counting toward the down payment.',
  },
  {
    id: 'normandy',
    name: 'Normandy Corporation',
    kind: 'Owner-builder specialist',
    url: 'https://normandy.com/self-build-owner-build-loans/',
    states: 'NC · CA · MI · NJ · NY · WA and others',
    notes:
      'Licensed mortgage banker with a dedicated self-build / owner-build program for borrowers acting as their own GC. Advertises up to 90% loan-to-cost on conforming amounts, with jumbo programs above that.',
  },
  {
    id: 'agsouth',
    name: 'AgSouth Farm Credit',
    kind: 'Regional lender',
    url: 'https://agsouthfc.com/',
    states: 'GA · SC · parts of NC',
    notes:
      'Farm Credit cooperative doing construction-to-permanent lending on rural and country property — a strong fit for owner-builders outside city limits, where many national lenders won’t go.',
  },
  {
    id: 'cfsbank',
    name: 'cfsbank',
    kind: 'Regional lender',
    url: 'https://www.cfsbank.bank/',
    states: 'PA',
    notes:
      'Community bank with a purpose-built Owner Builder Mortgage that can count lot equity — and in some cases sweat equity — toward the down payment.',
  },
];

/**
 * Sponsored placement config — the on-site half of a signed lender deal.
 * null = no deal = the slot renders nothing. When a deal closes, fill this
 * in and the slot renders with a visible "Sponsored" label.
 */
export interface FeaturedLender {
  name: string;
  url: string;
  states: string;
  pitch: string; // one honest sentence, approved by the lender
}

export const FEATURED_LENDER: FeaturedLender | null = null;

export const LENDERS_VERIFIED = 'August 2026';
