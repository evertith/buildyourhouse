/**
 * The default run: 2,000 sq ft, one story, slab, standard finish, North
 * Carolina, with insulation, interior finish, and the final phase done by
 * the owner. The page's FAQ answers, methodology prose, and assumptions
 * table read their numbers from here, so a price refresh moves every cited
 * figure together and nothing drifts.
 */

import { PROFILE_DEFAULTS } from './geometry.ts';
import { DIY_DEFAULT } from './labor.ts';
import { runEstimate } from './estimate.ts';
import type { Estimate, PhaseRow } from './estimate.ts';
import type { PhaseId } from './types.ts';

export const DEFAULT_ESTIMATE: Estimate = runEstimate(
  PROFILE_DEFAULTS,
  PROFILE_DEFAULTS.finish,
  PROFILE_DEFAULTS.state,
  { diy: DIY_DEFAULT }
);

/** The same house with every phase hired, for "every trade hired" figures. */
export const DEFAULT_ALL_HIRED: Estimate = runEstimate(
  PROFILE_DEFAULTS,
  PROFILE_DEFAULTS.finish,
  PROFILE_DEFAULTS.state,
  { diy: [] }
);

export function defaultPhase(id: PhaseId): PhaseRow {
  const p = DEFAULT_ESTIMATE.phases.find((x) => x.id === id);
  if (!p) throw new Error(`no phase ${id}`);
  return p;
}

/** "$52,000": a mid rounded to the nearest thousand for prose. */
export function roundK(n: number): string {
  const k = Math.round(n / 1000) * 1000;
  return `$${k.toLocaleString('en-US')}`;
}

/** "$186": a per-square-foot figure for prose. */
export function roundDollar(n: number): string {
  return `$${Math.round(n).toLocaleString('en-US')}`;
}
