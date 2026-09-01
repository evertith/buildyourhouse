/**
 * Site Plan Studio — engineering scale for the printed sheet.
 *
 * On screen the drawing is fit-to-viewport and the scale is whatever the
 * window is. On paper it has to be a scale a reviewer can put an engineer's
 * rule against, printed in the title block AND drawn as a graphic bar — so
 * the sheet still measures correctly after someone photocopies it at 94%.
 */

import { lotBox } from './geometry';
import type { Lot } from './types';

/** Feet to the inch, the standard engineer's-scale ladder and its decades. */
const LADDER = [10, 20, 30, 40, 50, 60, 100, 200, 300, 400, 500, 600, 1000];

/**
 * The largest drawing (smallest feet-per-inch) that fits the lot inside the
 * drawing window. Returns feet per inch.
 */
export function pickScale(
  lotW: number,
  lotD: number,
  windowInW: number,
  windowInH: number
): number {
  for (const s of LADDER) {
    if (lotW / s <= windowInW && lotD / s <= windowInH) return s;
  }
  return LADDER[LADDER.length - 1];
}

/**
 * The same pick for a lot of either shape: a polygon is scaled by what it
 * spans, not by two dimensions it does not have. Sheet and screen both go
 * through here so the printed scale can never disagree with the drawing.
 */
export function pickScaleForLot(
  lot: Lot,
  windowInW: number,
  windowInH: number
): number {
  const box = lotBox(lot);
  return pickScale(box.w, box.d, windowInW, windowInH);
}

/** "1\" = 30'" — the title-block form. */
export function formatScale(feetPerInch: number): string {
  return `1" = ${feetPerInch}'`;
}

const INTERVALS = [5, 10, 20, 25, 50, 100, 200, 250, 500, 1000];

export interface BarScale {
  /** Feet per division. */
  interval: number;
  /** Number of divisions. */
  divisions: number;
  /** Total feet the bar spans. */
  totalFeet: number;
  /** Tick labels, including the leading 0. */
  ticks: number[];
}

/**
 * A bar of five divisions, sized so the whole bar lands between about 1.4in
 * and 2.6in at the chosen scale — long enough to measure against, short
 * enough to sit under the drawing window.
 */
export function barScale(feetPerInch: number, maxInches = 2.6): BarScale {
  const divisions = 5;
  let interval = INTERVALS[0];
  for (const candidate of INTERVALS) {
    const inches = (candidate * divisions) / feetPerInch;
    if (inches <= maxInches) interval = candidate;
    else break;
  }
  const ticks: number[] = [];
  for (let i = 0; i <= divisions; i++) ticks.push(interval * i);
  return {
    interval,
    divisions,
    totalFeet: interval * divisions,
    ticks,
  };
}
