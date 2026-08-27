/**
 * State Permit Kit registry — one entry per state, the single source of
 * truth for the shop's kit line. Drives the permit-kits hub (shipped +
 * coming), the templated kit product pages, state-guide CTAs, and the
 * sitemap. A kit ships by flipping status to 'shipped' and filling
 * checkoutUrl + hook (payment link provisioned via the downloads worker's
 * provision-products, which stamps metadata.sku).
 *
 * Production runs in demand-ranked phases of four (phase field); the
 * 50-state program started Aug 2026 from the NC prototype.
 */

export interface StateKit {
  /** Product slug and SKU: '<code>-permit-kit' (e.g. 'nc-permit-kit'). */
  slug: string;
  state: string;
  /** Lowercase postal code — matches binder-pipeline/kits/<code>-permit-kit/. */
  code: string;
  /** State-guide route: /permitting/state-guides/<guideSlug>. */
  guideSlug: string;
  status: 'shipped' | 'coming';
  /** Stripe payment link — required once shipped. */
  checkoutUrl?: string;
  /** One-line hook: the state-specific traps the kit documents. */
  hook?: string;
  /** Planned production phase (1–12), set by demand ranking. */
  phase?: number;
}

const K = (
  state: string,
  code: string,
  guideSlug: string,
  rest: Partial<StateKit> = {}
): StateKit => ({
  slug: `${code}-permit-kit`,
  state,
  code,
  guideSlug,
  status: 'coming',
  ...rest,
});

export const STATE_KITS: StateKit[] = [
  K('Alabama', 'al', 'alabama', { phase: 5 }),
  K('Alaska', 'ak', 'alaska', {
    status: 'shipped',
    checkoutUrl: 'https://buy.stripe.com/7sYeVd5W7dB543qdV1fAc0d',
    hook: 'The exemption paragraph almost everyone cites is the remodel one, a state plumbing inspector arrives where no building department exists, and the code that actually binds your house comes through the mortgage — with the building official employed by the lender.',
  }),
  K('Arizona', 'az', 'arizona', { phase: 11 }),
  K('Arkansas', 'ar', 'arkansas', { phase: 3 }),
  K('California', 'ca', 'california', {
    status: 'shipped',
    checkoutUrl: 'https://buy.stripe.com/dRmbJ1ckvgNhfM85ovfAc09',
    hook: 'Sprinklers in every new home, the 2023 NEC, the declaration that is stricter than § 7044, and 52 hours that makes a helper your employee.',
  }),
  K('Colorado', 'co', 'colorado', {
    status: 'shipped',
    checkoutUrl: 'https://buy.stripe.com/aFa00jbgr2WrgQceZ5fAc08',
    hook: 'Two permit systems over one house: a local building permit that may not exist, state electrical and plumbing permits that always do, and the inspection condition that quietly voids the homeowner electrical exemption.',
  }),
  K('Connecticut', 'ct', 'connecticut', { phase: 10 }),
  K('Delaware', 'de', 'delaware', { phase: 12 }),
  K('Florida', 'fl', 'florida', { phase: 3 }),
  K('Georgia', 'ga', 'georgia', {
    status: 'shipped',
    checkoutUrl: 'https://buy.stripe.com/7sYeVd5W7gNhdE0eZ5fAc04',
    hook: 'The one-sale-per-24-months exemption trap, mandatory codes even in no-permit counties, and the two required performance tests.',
  }),
  K('Hawaii', 'hi', 'hawaii', { phase: 9 }),
  K('Idaho', 'id', 'idaho', { phase: 6 }),
  K('Illinois', 'il', 'illinois', { phase: 10 }),
  K('Indiana', 'in', 'indiana', { phase: 7 }),
  K('Iowa', 'ia', 'iowa', { phase: 4 }),
  K('Kansas', 'ks', 'kansas', { phase: 10 }),
  K('Kentucky', 'ky', 'kentucky', { phase: 2 }),
  K('Louisiana', 'la', 'louisiana', { phase: 3 }),
  K('Maine', 'me', 'maine', { phase: 8 }),
  K('Maryland', 'md', 'maryland', { phase: 9 }),
  K('Massachusetts', 'ma', 'massachusetts', { phase: 9 }),
  K('Michigan', 'mi', 'michigan', {
    status: 'shipped',
    checkoutUrl: 'https://buy.stripe.com/fZu5kD84f1SneI46szfAc0a',
    hook: 'The four permits that may come from four different governments, the 3,500 sq ft rule measured in habitable space only, and the court order that froze Michigan on the 2015 code.',
  }),
  K('Minnesota', 'mn', 'minnesota', { phase: 4 }),
  K('Mississippi', 'ms', 'mississippi', {
    status: 'shipped',
    checkoutUrl: 'https://buy.stripe.com/eVqaEXacn7cHdE03gnfAc0c',
    hook: 'The 120-day window in 2014 that decided whether any code binds your parcel, the coastal wind mandate that also had an opt-out, the zero-dollar trade-license rule, and the septic approval that locks your water meter.',
  }),
  K('Missouri', 'mo', 'missouri', { phase: 9 }),
  K('Montana', 'mt', 'montana', {
    status: 'shipped',
    checkoutUrl: 'https://buy.stripe.com/cNi7sL84f1SnarO2cjfAc0b',
    hook: 'The building code that does not apply to your house, the electrical permit that applies anyway and is enforced at the power meter, the contractor statute that was repealed on January 1 2026, and the sanitation law that bars you from even erecting the building.',
  }),
  K('Nebraska', 'ne', 'nebraska', { phase: 12 }),
  K('Nevada', 'nv', 'nevada', { phase: 5 }),
  K('New Hampshire', 'nh', 'new-hampshire', { phase: 7 }),
  K('New Jersey', 'nj', 'new-jersey', { phase: 8 }),
  K('New Mexico', 'nm', 'new-mexico', { phase: 6 }),
  K('New York', 'ny', 'new-york', { phase: 5 }),
  K('North Carolina', 'nc', 'north-carolina', {
    status: 'shipped',
    checkoutUrl: 'https://buy.stripe.com/7sYaEX3NZ40vgQc2cjfAc01',
    hook: 'The owner exemption affidavit, the $40K lien-agent threshold, septic gating the permit, and the personally-present inspection rule.',
  }),
  K('North Dakota', 'nd', 'north-dakota', { phase: 11 }),
  K('Ohio', 'oh', 'ohio', { phase: 6 }),
  K('Oklahoma', 'ok', 'oklahoma', { phase: 4 }),
  K('Oregon', 'or', 'oregon', { phase: 7 }),
  K('Pennsylvania', 'pa', 'pennsylvania', { phase: 8 }),
  K('Rhode Island', 'ri', 'rhode-island', { phase: 10 }),
  K('South Carolina', 'sc', 'south-carolina', { phase: 4 }),
  K('South Dakota', 'sd', 'south-dakota', { phase: 11 }),
  K('Tennessee', 'tn', 'tennessee', { phase: 11 }),
  K('Texas', 'tx', 'texas', {
    status: 'shipped',
    checkoutUrl: 'https://buy.stripe.com/aFaeVd4S3dB5dE004bfAc06',
    hook: 'No state license or permit — and the traps that replace them: trade licensing, TCEQ septic, the energy code that applies anyway, coastal windstorm.',
  }),
  K('Utah', 'ut', 'utah', { phase: 7 }),
  K('Vermont', 'vt', 'vermont', { phase: 8 }),
  K('Virginia', 'va', 'virginia', {
    status: 'shipped',
    checkoutUrl: 'https://buy.stripe.com/9B64gz84f2WrarOg39fAc05',
    hook: 'The § 54.1-1101 exemption, the lien agent that protects you, VDH septic shot clocks, and the VDOT driveway permit almost nobody expects.',
  }),
  K('Washington', 'wa', 'washington', {
    status: 'shipped',
    checkoutUrl: 'https://buy.stripe.com/fZu6oHesD7cH9nKcQXfAc07',
    hook: 'The electrical permit that comes from the State instead of your county, the 950-gallon well cap that replaced the 5,000-gallon one, and the three energy tests with no visual alternative.',
  }),
  K('West Virginia', 'wv', 'west-virginia', { phase: 5 }),
  K('Wisconsin', 'wi', 'wisconsin', { phase: 3 }),
  K('Wyoming', 'wy', 'wyoming', { phase: 6 }),
];

export const shippedKits = () => STATE_KITS.filter((k) => k.status === 'shipped');
export const comingKits = () => STATE_KITS.filter((k) => k.status === 'coming');
export const kitBySlug = (slug: string) => STATE_KITS.find((k) => k.slug === slug);
export const kitByGuideSlug = (guideSlug: string) =>
  STATE_KITS.find((k) => k.guideSlug === guideSlug);
