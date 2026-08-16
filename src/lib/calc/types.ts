/**
 * Shared result contract for the trade calculators (src/lib/calc/*).
 *
 * Every engine is a pure function from typed inputs to a CalcResult. The
 * framework components (src/components/calc/*) render any CalcResult, so
 * engines stay free of presentation concerns and pages stay free of math.
 *
 * Quantities are the headline; costs are honest LOW–HIGH material ranges
 * (never a single fake-precise number) and exclude labor unless a line
 * says otherwise.
 */

export interface CalcLine {
  id: string;
  /** What to buy — "Wall studs", "Ready-mix concrete". */
  label: string;
  qty: number;
  /** Purchase unit — "studs", "sheets", "yd³", "bundles". */
  unit: string;
  /** Spec detail — '2×4 precut, 16" OC, corners and openings included'. */
  detail?: string;
  costLow?: number;
  costHigh?: number;
}

export interface CalcResult {
  /** The one number the visitor came for. */
  hero: {
    qty: number;
    unit: string;
    label: string;
    detail?: string;
    /**
     * How to format the hero: 'qty' (default) renders formatQty + unit,
     * 'currency' renders as dollars, 'duration' renders like qty (unit
     * carries "months"/"weeks"). Lets planning worksheets (W-01…W-04)
     * share the sheet without faking a material quantity.
     */
    kind?: 'qty' | 'currency' | 'duration';
  };
  lines: CalcLine[];
  /**
   * Total material cost range across lines. Optional: worksheets whose
   * hero IS the dollar figure (or whose output is a schedule) omit it and
   * the sheet skips the cost dimension line.
   */
  costLow?: number;
  costHigh?: number;
  /**
   * Run-specific assumption notes ("Includes 10% waste", "Excludes labor").
   * The page's static methodology section covers the full math; these are
   * the short flags that belong next to the numbers.
   */
  notes: string[];
}

/** Sum line cost ranges into result totals. */
export function totalCosts(lines: CalcLine[]): { costLow: number; costHigh: number } {
  return {
    costLow: Math.round(lines.reduce((s, l) => s + (l.costLow ?? 0), 0)),
    costHigh: Math.round(lines.reduce((s, l) => s + (l.costHigh ?? 0), 0)),
  };
}

/** Clamp helper — HTML min/max are bypassable, engines must self-defend. */
export function clamp(value: number, min: number, max: number): number {
  if (!Number.isFinite(value)) return min;
  return Math.min(max, Math.max(min, value));
}
