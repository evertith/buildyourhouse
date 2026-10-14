/**
 * Shared shapes for the whole-house estimate engine (src/lib/estimate).
 *
 * Every phase module is a pure function from a Geometry to a PhaseResult.
 * Costs are honest low–high ranges, never a single fake-precise number; the
 * ledger prints rounded mids and the rail prints the range under them.
 *
 * Relative imports inside this folder carry the `.ts` extension so the
 * tests run with `node --test --experimental-strip-types` and no build step
 * (same convention as src/lib/siteplan).
 */

export interface Range {
  low: number;
  high: number;
}

export interface Money {
  low: number;
  mid: number;
  high: number;
}

/** A unit rate: dollars per `unit`, national, as of PRICES_AS_OF. */
export interface Rate {
  low: number;
  high: number;
  unit: string;
}

/** Where a number came from: the profile rules, a plan read, or the visitor. */
export type Source = 'derived' | 'measured' | 'user';

export type PhaseId =
  | 'soft'
  | 'site'
  | 'foundation'
  | 'framing'
  | 'roofing'
  | 'openings'
  | 'exterior'
  | 'plumbing'
  | 'electrical'
  | 'hvac'
  | 'insulation'
  | 'drywallPaint'
  | 'interior'
  | 'final';

export const PHASE_ORDER: readonly PhaseId[] = [
  'soft',
  'site',
  'foundation',
  'framing',
  'roofing',
  'openings',
  'exterior',
  'plumbing',
  'electrical',
  'hvac',
  'insulation',
  'drywallPaint',
  'interior',
  'final',
];

export interface Line {
  id: string;
  /** What to buy: "Ready-mix concrete". */
  label: string;
  qty: number;
  /** Purchase unit: "yd³", "sheets", "allowance". */
  unit: string;
  /** Spec detail under the row. */
  detail?: string;
  costLow: number;
  costHigh: number;
  /** Sheet reference for a measured line: "A-2". */
  ref?: string;
}

export interface PhaseResult {
  id: PhaseId;
  name: string;
  /** One line under the name: what the phase covers. */
  note: string;
  lines: Line[];
  /** Material cost range, after the state index and finish multiplier. */
  materials: Range;
  /** Labor cost range if hired, after the state labor index. */
  labor: Range;
  /** Hours of work the labor figure represents. */
  hours: number;
  /** Whether the numbers were derived from the profile or measured from plans. */
  basis: Source;
  /** Soft costs are paid, not built: no Hire it / Do it myself switch. */
  soft?: boolean;
  /** Some states require a licensed trade for this phase. */
  licensed?: boolean;
}

export function sumLines(lines: Line[]): Range {
  return {
    low: lines.reduce((s, l) => s + l.costLow, 0),
    high: lines.reduce((s, l) => s + l.costHigh, 0),
  };
}

export function mid(r: Range): number {
  return (r.low + r.high) / 2;
}

export function money(r: Range): Money {
  return { low: r.low, mid: mid(r), high: r.high };
}

export function addRange(a: Range, b: Range): Range {
  return { low: a.low + b.low, high: a.high + b.high };
}

export function scaleRange(r: Range, k: number): Range {
  return { low: r.low * k, high: r.high * k };
}

/** A priced line: qty × rate. */
export function line(
  id: string,
  label: string,
  qty: number,
  rate: Rate,
  detail?: string,
  ref?: string
): Line {
  return {
    id,
    label,
    qty,
    unit: rate.unit,
    detail,
    costLow: qty * rate.low,
    costHigh: qty * rate.high,
    ref,
  };
}

/** A lump allowance with its own low–high band. */
export function allowance(id: string, label: string, r: Rate, detail?: string, ref?: string): Line {
  return { id, label, qty: 1, unit: 'allowance', detail, costLow: r.low, costHigh: r.high, ref };
}

/** Symmetric band around a point cost, so sums stay centered on the mid. */
export function band(cost: number, spread: number): Range {
  return { low: cost * (1 - spread), high: cost * (1 + spread) };
}

export function clamp(value: number, min: number, max: number): number {
  if (!Number.isFinite(value)) return min;
  return Math.min(max, Math.max(min, value));
}

/** Round to the nearest `step` (default 1). */
export function roundTo(value: number, step = 1): number {
  return Math.round(value / step) * step;
}

export function ceilTo(value: number, step = 1): number {
  return Math.ceil(value / step - 1e-9) * step;
}
