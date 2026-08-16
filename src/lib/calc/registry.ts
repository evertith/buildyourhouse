/**
 * Calculator registry — one entry per trade calculator. Drives the
 * /calculators hub, related-calculator cross-links, and the sitemap.
 * Page copy (FAQ, methodology prose) lives in each page, not here.
 */

export interface CalcMeta {
  slug: string;
  /** Sheet number in the drafting-set conceit — stable, ordered. */
  sheetNo: string;
  name: string;
  /** Hub card + related-calc one-liner. */
  blurb: string;
  /** What the hero number is, for hub cards ("studs", "yd³"). */
  heroUnit: string;
  relatedGuide: { href: string; label: string };
  relatedCalcs: string[];
  /** Trade takeoff (TO-*) or planning worksheet (W-*). Default 'takeoff'. */
  kind?: 'takeoff' | 'worksheet';
  /** Route override for entries outside /calculators/<slug>. */
  href?: string;
}

/** Canonical route for a calculator. */
export function calcHref(meta: CalcMeta): string {
  return meta.href ?? `/calculators/${meta.slug}`;
}

export const CALCULATORS: CalcMeta[] = [
  {
    slug: 'framing-lumber',
    sheetNo: 'TO-01',
    name: 'Framing Lumber Calculator',
    blurb: 'Studs, plates, headers, and sheathing for every wall in the house.',
    heroUnit: 'studs',
    relatedGuide: { href: '/build-phases/framing', label: 'Framing phase guide' },
    relatedCalcs: ['drywall', 'insulation', 'roofing'],
  },
  {
    slug: 'drywall',
    sheetNo: 'TO-02',
    name: 'Drywall Calculator',
    blurb: 'Sheets, mud, tape, and screws — by room or for the whole house.',
    heroUnit: 'sheets',
    relatedGuide: { href: '/build-phases/drywall', label: 'Drywall phase guide' },
    relatedCalcs: ['paint', 'framing-lumber', 'insulation'],
  },
  {
    slug: 'concrete-slab',
    sheetNo: 'TO-03',
    name: 'Concrete Slab Calculator',
    blurb: 'Cubic yards, bag counts, rebar or mesh — sized so the truck isn’t short.',
    heroUnit: 'yd³',
    relatedGuide: { href: '/build-phases/foundation', label: 'Foundation phase guide' },
    relatedCalcs: ['framing-lumber', 'roofing', 'flooring'],
  },
  {
    slug: 'roofing',
    sheetNo: 'TO-04',
    name: 'Roofing Calculator',
    blurb: 'Squares, bundles, underlayment, and cap from footprint and pitch.',
    heroUnit: 'squares',
    relatedGuide: { href: '/build-phases/roofing', label: 'Roofing phase guide' },
    relatedCalcs: ['framing-lumber', 'insulation', 'concrete-slab'],
  },
  {
    slug: 'paint',
    sheetNo: 'TO-05',
    name: 'Paint Calculator',
    blurb: 'Gallons of paint and primer by room or whole house, coats included.',
    heroUnit: 'gallons',
    relatedGuide: { href: '/build-phases/painting', label: 'Painting phase guide' },
    relatedCalcs: ['drywall', 'flooring', 'insulation'],
  },
  {
    slug: 'flooring',
    sheetNo: 'TO-06',
    name: 'Flooring Calculator',
    blurb: 'Square footage with honest waste factors, box counts, underlayment.',
    heroUnit: 'sq ft',
    relatedGuide: { href: '/build-phases/flooring', label: 'Flooring phase guide' },
    relatedCalcs: ['paint', 'drywall', 'concrete-slab'],
  },
  {
    slug: 'insulation',
    sheetNo: 'TO-07',
    name: 'Insulation Calculator',
    blurb: 'Batt bags for walls, blown-in bags for the attic, by R-value.',
    heroUnit: 'bags',
    relatedGuide: { href: '/build-phases/insulation', label: 'Insulation phase guide' },
    relatedCalcs: ['drywall', 'framing-lumber', 'roofing'],
  },
  // Planning worksheets (W-01 … W-04) — whole-build numbers, same chassis.
  {
    slug: 'cost-savings-calculator',
    sheetNo: 'W-01',
    name: 'Cost Savings Calculator',
    blurb: 'Gut-check whether owner-building pencils out: the GC fee you avoid, honestly separated from the value of your own hours.',
    heroUnit: 'saved',
    kind: 'worksheet',
    href: '/feasibility/cost-savings-calculator',
    relatedGuide: { href: '/start-here', label: 'Start-here roadmap' },
    relatedCalcs: ['material-estimator', 'budget-tracker', 'timeline-estimator'],
  },
  {
    slug: 'material-estimator',
    sheetNo: 'W-02',
    name: 'Whole-House Material Estimator',
    blurb: 'Planning-level quantities for the entire build — concrete through insulation — from square footage and finish level.',
    heroUnit: 'estimate',
    kind: 'worksheet',
    relatedGuide: { href: '/planning/creating-budget', label: 'Budget planning guide' },
    relatedCalcs: ['framing-lumber', 'concrete-slab', 'cost-savings-calculator'],
  },
  {
    slug: 'timeline-estimator',
    sheetNo: 'W-03',
    name: 'Timeline Estimator',
    blurb: 'A realistic build schedule from your hours per week, DIY share, and experience — phase by phase.',
    heroUnit: 'months',
    kind: 'worksheet',
    relatedGuide: { href: '/timing-and-scheduling/realistic-timeline', label: 'Realistic timeline guide' },
    relatedCalcs: ['budget-tracker', 'cost-savings-calculator', 'material-estimator'],
  },
  {
    slug: 'budget-tracker',
    sheetNo: 'W-04',
    name: 'Budget Tracker',
    blurb: 'Budget vs. actual by phase, with contingency burn — so overruns surface early instead of at the end.',
    heroUnit: 'variance',
    kind: 'worksheet',
    relatedGuide: { href: '/planning/creating-budget', label: 'Budget planning guide' },
    relatedCalcs: ['material-estimator', 'timeline-estimator', 'cost-savings-calculator'],
  },
];

export function calcBySlug(slug: string): CalcMeta | undefined {
  return CALCULATORS.find((c) => c.slug === slug);
}

export function relatedCalcsFor(slug: string): CalcMeta[] {
  const meta = calcBySlug(slug);
  if (!meta) return [];
  return meta.relatedCalcs
    .map((s) => calcBySlug(s))
    .filter((c): c is CalcMeta => Boolean(c));
}
