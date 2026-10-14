/**
 * runEstimate: profile or geometry → the whole-house estimate.
 *
 * Each hard phase turns the geometry into national material lines; the
 * runner scales them by the state materials index and, for the
 * finish-sensitive phases, the finish multiplier; labor follows from the
 * material range by the phase ratio and the state labor index. Soft costs
 * run last because builder's risk is a share of the hard cost. Totals are
 * low / mid / high; the ledger prints rounded mids and the rail the range.
 */

import { deriveGeometry } from './geometry.ts';
import type { Geometry, Profile } from './geometry.ts';
import { CONTINGENCY_SHARE, FINISH_MULTIPLIER, FINISH_PHASES, PRICES_AS_OF } from './prices.ts';
import type { Finish } from './prices.ts';
import { DIY_DEFAULT, LICENSED_PHASES, laborFor } from './labor.ts';
import { stateFactors } from './stateIndex.ts';
import type { StateFactors } from './stateIndex.ts';
import { PHASE_ORDER, addRange, mid, money, scaleRange, sumLines } from './types.ts';
import type { Line, Money, PhaseId, PhaseResult, Range } from './types.ts';
import type { PhaseContext, PhaseFn, PhaseSpec } from './phases/shared.ts';
import { site } from './phases/site.ts';
import { foundation } from './phases/foundation.ts';
import { framing } from './phases/framing.ts';
import { roofing } from './phases/roofing.ts';
import { openings } from './phases/openings.ts';
import { exterior } from './phases/exterior.ts';
import { plumbing } from './phases/plumbing.ts';
import { electrical } from './phases/electrical.ts';
import { hvac } from './phases/hvac.ts';
import { insulation } from './phases/insulation.ts';
import { drywallPaint } from './phases/drywallPaint.ts';
import { interior } from './phases/interior.ts';
import { final } from './phases/final.ts';
import { soft } from './phases/soft.ts';

const HARD_PHASES: Record<Exclude<PhaseId, 'soft'>, PhaseFn> = {
  site,
  foundation,
  framing,
  roofing,
  openings,
  exterior,
  plumbing,
  electrical,
  hvac,
  insulation,
  drywallPaint,
  interior,
  final,
};

export interface EstimateChoices {
  /** Phases the owner does themselves. Defaults to DIY_DEFAULT. */
  diy?: readonly PhaseId[];
}

export interface PhaseRow extends PhaseResult {
  /** Owner does this phase: labor becomes hours instead of cash. */
  diy: boolean;
  /** Materials plus labor, whoever does it. */
  total: Range;
  /** Share of the all-hired total (mid), 0–1, for the bars. */
  share: number;
}

export interface Totals {
  materials: Money;
  hiredLabor: Money;
  ownLabor: Money;
  soft: Money;
  /** Materials, soft costs, and hired labor: what leaves the account. */
  cash: Money;
  /** Every phase hired. */
  allHired: Money;
  contingency: Money;
  /** Cash to build per heated square foot. */
  perSqFt: Money;
  /** Hours of the owner's own work. */
  hours: number;
  nDiy: number;
}

export interface Estimate {
  geometry: Geometry;
  finish: Finish;
  state: StateFactors;
  phases: PhaseRow[];
  totals: Totals;
  asOf: string;
  diy: PhaseId[];
}

export function isProfile(x: Profile | Geometry): x is Profile {
  return typeof (x as Profile).heatedSf === 'number';
}

/** Run the estimate. Pass a profile for the free rung or a geometry for a measured one. */
export function runEstimate(
  input: Profile | Geometry,
  finish: Finish,
  stateCode: string,
  choices: EstimateChoices = {}
): Estimate {
  const geometry = isProfile(input) ? deriveGeometry(input) : input;
  const state = stateFactors(stateCode);
  const ctx: PhaseContext = { finish, state };
  const diy = new Set<PhaseId>(choices.diy ?? DIY_DEFAULT);
  diy.delete('soft');

  const hard = (Object.keys(HARD_PHASES) as Array<Exclude<PhaseId, 'soft'>>).map((id) =>
    finishPhase(HARD_PHASES[id](geometry, ctx), ctx, geometry)
  );
  const hardCostMid = hard.reduce((s, p) => s + mid(p.materials) + mid(p.labor), 0);
  const softPhase = finishPhase(soft(geometry, ctx, hardCostMid), ctx, geometry, false);

  const ordered = PHASE_ORDER.map((id) =>
    id === 'soft' ? softPhase : (hard.find((p) => p.id === id) as PhaseResult)
  );

  const allHiredRange = ordered.reduce(
    (s, p) => addRange(s, addRange(p.materials, p.labor)),
    { low: 0, high: 0 }
  );
  const allHiredMid = mid(allHiredRange);

  const phases: PhaseRow[] = ordered.map((p) => {
    const isDiy = !p.soft && diy.has(p.id);
    const total = addRange(p.materials, p.labor);
    return { ...p, diy: isDiy, total, share: allHiredMid > 0 ? mid(total) / allHiredMid : 0 };
  });

  const zero: Range = { low: 0, high: 0 };
  const materials = phases.filter((p) => !p.soft).reduce((s, p) => addRange(s, p.materials), zero);
  const softRange = softPhase.materials;
  const hiredLabor = phases.filter((p) => !p.soft && !p.diy).reduce((s, p) => addRange(s, p.labor), zero);
  const ownLabor = phases.filter((p) => p.diy).reduce((s, p) => addRange(s, p.labor), zero);
  const cash = addRange(addRange(materials, softRange), hiredLabor);
  const hours = phases.filter((p) => p.diy).reduce((s, p) => s + p.hours, 0);
  const heated = geometry.heatedSf.value;

  const totals: Totals = {
    materials: money(materials),
    hiredLabor: money(hiredLabor),
    ownLabor: money(ownLabor),
    soft: money(softRange),
    cash: money(cash),
    allHired: money(allHiredRange),
    contingency: money(scaleRange(cash, CONTINGENCY_SHARE)),
    perSqFt: money(scaleRange(cash, 1 / heated)),
    hours,
    nDiy: phases.filter((p) => p.diy).length,
  };

  return {
    geometry,
    finish,
    state,
    phases,
    totals,
    asOf: PRICES_AS_OF,
    diy: phases.filter((p) => p.diy).map((p) => p.id),
  };
}

/** Apply the state index and finish multiplier to a phase's lines, then labor. */
function finishPhase(spec: PhaseSpec, ctx: PhaseContext, g: Geometry, scale = true): PhaseResult {
  const k = scale
    ? ctx.state.materials * (FINISH_PHASES.has(spec.id) ? FINISH_MULTIPLIER[ctx.finish] : 1)
    : 1;
  const lines: Line[] = spec.lines.map((l) => ({ ...l, costLow: l.costLow * k, costHigh: l.costHigh * k }));
  const materials = sumLines(lines);
  const { labor, hours } = spec.soft
    ? { labor: { low: 0, high: 0 }, hours: 0 }
    : laborFor(spec.id, materials, ctx.state.labor);
  const basis = phaseBasis(spec.id, g);
  return {
    id: spec.id,
    name: spec.name,
    note: spec.note,
    lines,
    materials,
    labor,
    hours,
    basis,
    soft: spec.soft,
    licensed: spec.licensed || LICENSED_PHASES.has(spec.id),
  };
}

/** A phase is measured when the geometry fields it leans on were measured. */
function phaseBasis(id: PhaseId, g: Geometry): PhaseResult['basis'] {
  const fields: Partial<Record<PhaseId, Array<{ source: string }>>> = {
    foundation: [g.footprintSf, g.perimeterLf, g.foundation],
    framing: [g.extWallLf, g.intWallLf, g.roof],
    roofing: [g.roof],
    openings: [g.openings],
    exterior: [g.extWallAreaSf, g.openings],
    plumbing: [g.rooms],
    insulation: [g.extWallAreaSf, g.footprintSf],
    drywallPaint: [g.intWallLf, g.extWallLf],
    interior: [g.rooms, g.intWallLf],
  };
  const f = fields[id];
  if (!f) return 'derived';
  return f.every((s) => s.source === 'measured') ? 'measured' : 'derived';
}
