/**
 * Labor for each phase, as a ratio of that phase's material cost.
 *
 * The ratios are calibrated so that the default house (2,000 sq ft, one
 * story, slab, standard finish, North Carolina) lands where 2026
 * subcontractor quotes land: framing crews at roughly $9–12 per square
 * foot, drywall hang-and-finish near twice the board cost, electricians
 * and plumbers well above their material. Labor is a range, scaled from
 * the material range by the same ratio, then by the state labor index.
 *
 * Hours convert the labor figure to time at a blended crew rate, so the
 * Do-it-myself switch can say what the visitor is signing up for.
 */

import type { PhaseId, Range } from './types.ts';
import { scaleRange, mid } from './types.ts';

export const LABOR_RATIO: Record<PhaseId, number> = {
  soft: 0,
  site: 1.5,
  foundation: 0.9,
  framing: 1.1,
  roofing: 0.9,
  openings: 0.3,
  exterior: 0.9,
  plumbing: 1.3,
  electrical: 1.5,
  hvac: 0.7,
  insulation: 0.55,
  drywallPaint: 1.9,
  interior: 0.55,
  final: 0.35,
};

/** Blended crew rate, dollars per hour, used only to express labor as hours. */
export const HOURLY_RATE: Record<PhaseId, number> = {
  soft: 45,
  site: 45,
  foundation: 45,
  framing: 45,
  roofing: 45,
  openings: 45,
  exterior: 45,
  plumbing: 65,
  electrical: 65,
  hvac: 65,
  insulation: 45,
  drywallPaint: 45,
  interior: 45,
  final: 45,
};

/** Phases the ledger starts with Do it myself selected. */
export const DIY_DEFAULT: readonly PhaseId[] = ['insulation', 'interior', 'final'];

/** Phases some states reserve for a licensed trade; the row carries a hint. */
export const LICENSED_PHASES: ReadonlySet<PhaseId> = new Set<PhaseId>([
  'plumbing',
  'electrical',
  'hvac',
]);

export function laborFor(
  id: PhaseId,
  materials: Range,
  laborIndex: number
): { labor: Range; hours: number } {
  const labor = scaleRange(materials, LABOR_RATIO[id] * laborIndex);
  const hours = mid(labor) / (HOURLY_RATE[id] * laborIndex);
  return { labor, hours };
}
