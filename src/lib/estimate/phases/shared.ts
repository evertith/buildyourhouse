/**
 * What every phase module receives and returns. The runner (estimate.ts)
 * applies the state index, the finish multiplier, and labor; a phase only
 * turns geometry into priced lines at national rates.
 */

import type { Geometry } from '../geometry.ts';
import type { Finish } from '../prices.ts';
import type { StateFactors } from '../stateIndex.ts';
import type { Line, PhaseId } from '../types.ts';

export interface PhaseContext {
  finish: Finish;
  state: StateFactors;
}

export interface PhaseSpec {
  id: PhaseId;
  name: string;
  note: string;
  lines: Line[];
  soft?: boolean;
  licensed?: boolean;
}

export type PhaseFn = (g: Geometry, ctx: PhaseContext) => PhaseSpec;

/** Pitch factor: sloped area per plan area for a rise in 12. */
export function pitchFactor(pitch: number): number {
  return Math.sqrt(1 + Math.pow(pitch / 12, 2));
}

export function n(value: number): string {
  return Math.round(value).toLocaleString('en-US');
}
