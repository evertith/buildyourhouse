/**
 * Editorial lender directory for /financing.
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
    states: 'AZ · CA · CO · FL · GA · MI · NC · SC · TX',
    notes:
      'Owner-builder construction loans are their entire business — no general contractor or project supervisor required. Advertises 12-month terms up to $700K, unlimited draws with no draw fees, and land equity counting toward the down payment. Says construction loans are not available in every state it is licensed in, so confirm your state before you plan around it.',
  },
  {
    id: 'normandy',
    name: 'Normandy Corporation',
    kind: 'Owner-builder specialist',
    url: 'https://normandy.com/self-build-owner-build-loans/',
    states: 'CA · CT · DE · FL · IA · MA · MI · NC · NJ · NY · OR · RI · VA · WA',
    notes:
      'Licensed mortgage banker with a dedicated self-build / owner-build program for borrowers acting as their own GC — no site supervisor and no general contractor on the payroll. Advertises up to 90% loan-to-cost on conforming amounts, with jumbo programs up to 80%. The state list above is their owner-occupied footprint; they lend in more states for non-owner-occupied projects.',
  },
  {
    id: 'farm-credit-virginias',
    name: 'Farm Credit of the Virginias',
    kind: 'Regional lender',
    url: 'https://www.farmcreditofvirginias.com/loans/construction-loans/',
    states: 'VA · WV',
    notes:
      'One of the few Farm Credit associations that puts owner-builders in writing — its construction page advertises allowances for owner and self-builds, with customer-managed builds carrying extra documentation and credit requirements. Interest-only during construction with scheduled draws and inspections, across a 96-county rural service area.',
  },
  {
    id: 'timberland-bank',
    name: 'Timberland Bank',
    kind: 'Regional lender',
    url: 'https://www.timberlandbank.com/lending/personal/construction-loan',
    states: 'WA',
    notes:
      'Washington community bank that advertises a named Owner-Builder program — "whether you hire a contractor or choose to build your own home" — with the owner-builder actively managing the project alongside a local lender. Advertises two-step construction financing at a maximum 80% loan-to-value, a 12-month construction term, interest-only payments during construction, and loan servicing kept in house.',
  },
  {
    id: 'olympia-federal',
    name: 'Olympia Federal Savings',
    kind: 'Regional lender',
    url: 'https://www.olyfed.com/home/construction/',
    states: 'WA (South Sound)',
    notes:
      'South Sound mutual savings bank that advertises taking either kind of project — "whether you’re going to do it yourself or work with a builder". Advertises all-in-one construction-to-permanent financing closed up front so there is no refinance at completion, no risk-based pricing, and human underwriting rather than automated. Read the fine print on leverage: the advertised 95% loan-to-cost applies to owner-occupied homes built with a licensed contractor.',
  },
  {
    id: 'greenstone',
    name: 'GreenStone Farm Credit Services',
    kind: 'Regional lender',
    url: 'https://www.greenstonefcs.com/loans/home-land-loans/home-construction-loans/',
    states: 'MI · northeast WI',
    notes:
      'Farm Credit cooperative that says it plainly: "You can use a licensed builder, do it yourself, or opt for a combination of both." Advertises a one-time close with interest-only payments during the build rolling straight into the end mortgage, direct-deposit draws, and as little as 5% down with PMI. Builder’s risk insurance is required and the budget has to be adequate.',
  },
  {
    id: 'kalamazoo-county-state-bank',
    name: 'Kalamazoo County State Bank',
    kind: 'Regional lender',
    url: 'https://kcsbank.com/construction-loan/',
    states: 'MI (southwest)',
    notes:
      'Southwest Michigan community bank that lists "Self-Contracting Builds" as a construction loan use case and describes itself as one of the few banks financing owner-builders. Advertises letting you work with a builder, do some of the work yourself, or self-contract the entire project — including sweat equity on trades like drywall, electrical, plumbing, flooring and trim.',
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

export const LENDERS_VERIFIED = 'September 2026';
