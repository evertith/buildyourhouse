/**
 * Site Plan Studio — the conflict engine.
 *
 * Pure: a plan plus a state's rules in, a schedule of measured rows and
 * findings out. Violations are derived on every render and never stored
 * (§4.1) — storing them creates a second source of truth that drifts the
 * first time a drag is interrupted.
 *
 * What can and cannot become a violation:
 *   · a binding statewide minimum in a VERIFIED state          → violation
 *   · a typical value in an unverified state                   → watch, never violation
 *   · a rule with `feet: null`                                 → note, never measured
 *   · anything in `extraSeparations`                           → note, never measured
 *   · a setback the OWNER typed                                → its own kind of check
 *   · an element over the property line                        → outranks all of it
 */

import { DEFAULT_SEPARATIONS } from './rules';
import {
  adaptSeparations,
  groupedNegatives,
  separationsFor,
  treatmentFor,
  type AdaptedRule,
} from './adapt';
import { distanceToLotEdges, elementDistance, nearestEdge } from './geometry';
import type { StateSiteplanRules } from './rules';
import type {
  BoundaryWarning,
  CheckResult,
  EdgeName,
  MeasureRow,
  NoteRow,
  Plan,
  PlanElement,
  SetbackWarning,
} from './types';
import { EDGE_LABEL, KIND_LABEL } from './types';

/** The dimension line shows any governed pair measuring under this ratio. */
export const WATCH_RATIO = 1.5;

const OPPOSITE: Record<EdgeName, EdgeName> = {
  north: 'south',
  south: 'north',
  east: 'west',
  west: 'east',
};

function pickBy(els: PlanElement[], kinds: readonly string[]): PlanElement[] {
  return els.filter((e) => kinds.includes(e.kind));
}

function measureRule(rule: AdaptedRule, plan: Plan, hedged: boolean): MeasureRow {
  const base = {
    id: rule.key,
    label: rule.label,
    requiredFeet: rule.feet,
    citation: rule.citation,
    note: rule.note,
    hedged,
  };
  const from = pickBy(plan.elements, rule.from);

  if (rule.to === 'propertyLine') {
    if (!from.length || !plan.lot) {
      return { ...base, measuredFeet: null, status: 'unplaced' };
    }
    let worst: { el: PlanElement; edge: EdgeName; feet: number } | null = null;
    for (const el of from) {
      const n = nearestEdge(el, plan.lot);
      if (!worst || n.feet < worst.feet) worst = { el, edge: n.edge, feet: n.feet };
    }
    const w = worst!;
    return {
      ...base,
      measuredFeet: w.feet,
      status: statusFor(w.feet, rule.feet, hedged),
      fromId: w.el.id,
      edge: w.edge,
    };
  }

  const to = pickBy(plan.elements, rule.to);
  if (!from.length || !to.length) {
    return { ...base, measuredFeet: null, status: 'unplaced' };
  }
  let worst: { a: PlanElement; b: PlanElement; feet: number } | null = null;
  for (const a of from) {
    for (const b of to) {
      if (a.id === b.id) continue;
      const feet = elementDistance(a, b);
      if (!worst || feet < worst.feet) worst = { a, b, feet };
    }
  }
  const w = worst!;
  return {
    ...base,
    measuredFeet: w.feet,
    status: statusFor(w.feet, rule.feet, hedged),
    fromId: w.a.id,
    toId: w.b.id,
  };
}

function statusFor(
  measured: number,
  required: number | null,
  hedged: boolean
): MeasureRow['status'] {
  if (required === null) return 'ok';
  if (measured >= required) return 'ok';
  return hedged ? 'watch' : 'violation';
}

/** Elements that may legitimately leave the lot, so they are not flagged. */
function boundaryExempt(el: PlanElement, edge: EdgeName, frontEdge: EdgeName): boolean {
  // A stream or shoreline runs across the parcel and out the other side.
  if (el.kind === 'waterEdge') return true;
  // A driveway meets the road, so crossing the street line is the point.
  if (el.kind === 'driveway' && edge === frontEdge) return true;
  return false;
}

function boundaryWarnings(plan: Plan): BoundaryWarning[] {
  if (!plan.lot) return [];
  const out: BoundaryWarning[] = [];
  for (const el of plan.elements) {
    const d = distanceToLotEdges(el, plan.lot);
    let worst: { edge: EdgeName; feet: number } | null = null;
    (Object.keys(d) as EdgeName[]).forEach((edge) => {
      if (d[edge] >= -0.01) return;
      if (boundaryExempt(el, edge, plan.frontEdge)) return;
      if (!worst || d[edge] < worst.feet) worst = { edge, feet: d[edge] };
    });
    if (worst) {
      const w = worst as { edge: EdgeName; feet: number };
      out.push({
        id: `outside-${el.id}`,
        elementId: el.id,
        label: KIND_LABEL[el.kind],
        overFeet: Math.abs(w.feet),
        edge: w.edge,
      });
    }
  }
  return out;
}

/** Which of the three entered setbacks governs a given edge. */
function setbackForEdge(plan: Plan, edge: EdgeName): number | null {
  if (edge === plan.frontEdge) return plan.setbacks.front;
  if (edge === OPPOSITE[plan.frontEdge]) return plan.setbacks.rear;
  return plan.setbacks.side;
}

function setbackWarnings(plan: Plan): SetbackWarning[] {
  if (!plan.lot) return [];
  const out: SetbackWarning[] = [];
  for (const el of plan.elements) {
    if (el.kind !== 'house' && el.kind !== 'structure') continue;
    const d = distanceToLotEdges(el, plan.lot);
    (Object.keys(d) as EdgeName[]).forEach((edge) => {
      const req = setbackForEdge(plan, edge);
      if (req === null || !Number.isFinite(req) || req <= 0) return;
      if (d[edge] >= req - 0.01) return;
      out.push({
        id: `setback-${el.id}-${edge}`,
        elementId: el.id,
        label: KIND_LABEL[el.kind],
        edge,
        requiredFeet: req,
        measuredFeet: d[edge],
      });
    });
  }
  return out;
}

/**
 * Findings with no number to measure: the sourced negatives behind a state's
 * null separations, then its conditional provisions, then the kit's own
 * negative findings.
 */
function noteRows(rules: StateSiteplanRules | null, sepSource: ReturnType<typeof separationsFor>): NoteRow[] {
  const out: NoteRow[] = [];
  if (sepSource) {
    for (const g of groupedNegatives(sepSource)) {
      out.push({ id: `null-${g.keys.join('-')}`, label: g.label, text: g.text });
    }
  }
  if (rules?.extraSeparations) {
    rules.extraSeparations.forEach((x, i) => {
      out.push({
        id: `extra-${i}`,
        label: x.label,
        text: x.note ?? '',
        citation: x.citation,
        conditional: true,
        feet: x.feet,
      });
    });
  }
  if (rules?.negativeFindings) {
    rules.negativeFindings.forEach((t, i) => {
      out.push({ id: `finding-${i}`, label: 'Finding', text: t });
    });
  }
  return out;
}

export function check(plan: Plan, rules: StateSiteplanRules | null): CheckResult {
  const treatment = treatmentFor(rules, plan.stateCode);
  const sep = separationsFor(rules, treatment);
  const hedged = treatment === 'hedged';

  const rows: MeasureRow[] =
    sep === null
      ? []
      : adaptSeparations(sep)
          .filter((r) => r.feet !== null)
          .map((r) => measureRule(r, plan, hedged));

  return {
    treatment,
    rows,
    boundary: boundaryWarnings(plan),
    setbacks: setbackWarnings(plan),
    notes: treatment === 'none' ? [] : noteRows(rules, sep),
  };
}

/** Rows that measured short — violations in a verified state, watches in a hedged one. */
export function shortRows(result: CheckResult): MeasureRow[] {
  return result.rows.filter((r) => r.status === 'violation' || r.status === 'watch');
}

/** Rows worth drawing a dimension line for without a selection (§2.3). */
export function liveRows(result: CheckResult): MeasureRow[] {
  return result.rows.filter(
    (r) =>
      r.measuredFeet !== null &&
      r.requiredFeet !== null &&
      r.measuredFeet < r.requiredFeet * WATCH_RATIO
  );
}

/**
 * The seven separations measured on geometry alone, ignoring whether any
 * state governs them.
 *
 * This exists for the ten verified states whose finding is that NO statewide
 * minimum exists. They produce no rule rows at all, and the useful thing to
 * hand those owners is still the measurements — "your well is 78 ft from your
 * drainfield; your county health department sets the number" is a phone call
 * they can make. Pairing comes from the same adapter the engine uses, so the
 * two can never disagree about what measures against what.
 */
export function measureAllPairs(
  plan: Plan
): { label: string; feet: number }[] {
  const out: { label: string; feet: number }[] = [];
  for (const rule of adaptSeparations(DEFAULT_SEPARATIONS())) {
    const from = pickBy(plan.elements, rule.from);
    if (!from.length) continue;

    if (rule.to === 'propertyLine') {
      if (!plan.lot) continue;
      let worst = Infinity;
      for (const el of from) worst = Math.min(worst, nearestEdge(el, plan.lot).feet);
      if (Number.isFinite(worst)) out.push({ label: rule.label, feet: worst });
      continue;
    }

    const to = pickBy(plan.elements, rule.to);
    if (!to.length) continue;
    let worst = Infinity;
    for (const a of from) {
      for (const b of to) {
        if (a.id !== b.id) worst = Math.min(worst, elementDistance(a, b));
      }
    }
    if (Number.isFinite(worst)) out.push({ label: rule.label, feet: worst });
  }
  return out;
}

/** Rows the sheet prints: the rule applies to elements actually placed. */
export function sheetRows(result: CheckResult): MeasureRow[] {
  return result.rows.filter((r) => r.status !== 'unplaced');
}

export { EDGE_LABEL };
