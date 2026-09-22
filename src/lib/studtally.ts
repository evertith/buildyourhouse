/**
 * StudTally — the plan-set takeoff service from the people behind this site.
 * The free calculators here estimate from square footage or field
 * measurements; StudTally reads an uploaded residential plan set and returns
 * the framing list with every quantity traced to the sheet it came from.
 *
 * One place for the URL, the price, and the UTM convention so every link on
 * the site attributes the same way on the StudTally side.
 */

export const STUDTALLY_URL = 'https://studtally.com/';

/** Per-job price as printed on studtally.com (September 2026). */
export const STUDTALLY_PRICE = 79;

/** Outbound link with attribution. `content` names the placement (calculator slug or page). */
export function studTallyUrl(content: string): string {
  const u = new URL(STUDTALLY_URL);
  u.searchParams.set('utm_source', 'build-your-house.com');
  u.searchParams.set('utm_medium', 'referral');
  u.searchParams.set('utm_campaign', 'plan-takeoff');
  u.searchParams.set('utm_content', content);
  return u.toString();
}

/** Calculators whose results sheet offers the StudTally step. Framing-adjacent only — the offer must match the page. */
export const PLAN_TAKEOFF_SLUGS = new Set(['material-estimator', 'framing-lumber']);
