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
