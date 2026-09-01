/**
 * Site Plan Studio — what an element looks like the moment it is dropped.
 *
 * Clicking a tool places the element immediately rather than arming a
 * click-to-place cursor (§2.2): one fewer mode, nothing to explain, and it
 * works from the keyboard. That only holds if the drop lands somewhere
 * sensible, which is what `placeElement` below is for.
 */

import {
  bounds,
  clamp,
  innerPoint,
  lotArea,
  lotBox,
  polygonArea,
  selfIntersects,
} from './geometry';
import type { EdgeName, ElementKind, Lot, PlanElement, Pt } from './types';

/** Footprint in feet on drop, before the user resizes anything. */
export const DEFAULT_SIZE: Record<ElementKind, { w: number; d: number }> = {
  house: { w: 40, d: 28 },
  structure: { w: 24, d: 24 },
  septicTank: { w: 8, d: 5 },
  drainfield: { w: 60, d: 20 },
  driveway: { w: 12, d: 50 },
  // A point. Measured from its center — the ⊕ symbol is drawn at a fixed
  // size on paper, not at a size in feet, so there is no world-space radius
  // to subtract and a printed distance matches what a ruler on the sheet says.
  well: { w: 0, d: 0 },
  // A line. Length is overwritten in placeElement to suit the lot.
  waterEdge: { w: 120, d: 0 },
};

/** One-line explanation shown under the tool in the palette. */
export const KIND_HINT: Record<ElementKind, string> = {
  house: 'The building footprint — the outline of the walls at grade.',
  structure: 'A garage, shop, barn or shed. Add one per building.',
  well: 'The well head. Every separation the states publish measures from it.',
  septicTank: 'The tank itself, not the field.',
  drainfield: 'The absorption field. Draw the reserve area as a second one.',
  driveway: 'From the road to the house — departments look for it.',
  waterEdge: 'A pond bank, stream or lake shore. Surface-water rules measure to it.',
};

/** Elements that behave as a building for separation purposes. */
export const BUILDING_KINDS: ElementKind[] = ['house', 'structure'];

/** Elements that are part of the wastewater system. */
export const SEPTIC_KINDS: ElementKind[] = ['septicTank', 'drainfield'];

let seq = 0;

/** Ids only need to be unique inside one plan, and stable across a save. */
export function newId(kind: ElementKind): string {
  seq += 1;
  return `${kind}-${seq.toString(36)}${Math.random().toString(36).slice(2, 6)}`;
}

/** Restores the counter after a hydrate so new ids cannot collide. */
export function bumpSeq(n: number): void {
  seq = Math.max(seq, n);
}

const overlaps = (a: PlanElement, b: PlanElement, pad: number): boolean => {
  const ba = bounds(a);
  const bb = bounds(b);
  return (
    ba.minX - pad < bb.maxX &&
    ba.maxX + pad > bb.minX &&
    ba.minY - pad < bb.maxY &&
    ba.maxY + pad > bb.minY
  );
};

/** Offsets tried in order, feet — center first, then a widening spiral. */
const RING: [number, number][] = [
  [0, 0],
  [0, -0.22],
  [0.26, 0],
  [0, 0.22],
  [-0.26, 0],
  [0.26, -0.22],
  [-0.26, 0.22],
  [0.26, 0.22],
  [-0.26, -0.22],
  [0, -0.38],
  [0.4, 0],
  [0, 0.38],
  [-0.4, 0],
];

/**
 * Drops an element at a free position: center-biased, offset from anything
 * already placed, and never hanging outside the lot.
 */
export function placeElement(
  kind: ElementKind,
  lot: Lot,
  existing: PlanElement[],
  frontEdge: EdgeName,
  frontSegment: number | null = null
): PlanElement {
  const size = { ...DEFAULT_SIZE[kind] };

  if (lot.kind === 'poly') return placeOnPolygon(kind, lot.pts, existing, frontSegment, size);

  if (kind === 'driveway') {
    // Runs in from the street edge, so it reads as an approach rather than a
    // slab floating in the yard.
    const along = frontEdge === 'north' || frontEdge === 'south';
    const run = clamp(along ? lot.d * 0.45 : lot.w * 0.45, 20, 90);
    size.d = run;
    const el: PlanElement = {
      id: newId(kind),
      kind,
      x: lot.w / 2,
      y: lot.d / 2,
      w: size.w,
      d: size.d,
      rot: along ? 0 : 90,
    };
    if (frontEdge === 'north') el.y = run / 2;
    else if (frontEdge === 'south') el.y = lot.d - run / 2;
    else if (frontEdge === 'west') el.x = run / 2;
    else el.x = lot.w - run / 2;
    return el;
  }

  if (kind === 'waterEdge') {
    // A first guess along the back of the lot; it exists to be dragged to
    // where the water actually is.
    const len = clamp(lot.w * 0.7, 20, lot.w);
    return {
      id: newId(kind),
      kind,
      x: lot.w / 2,
      y: lot.d * 0.85,
      w: len,
      d: 0,
      rot: 0,
    };
  }

  const pad = 6;
  for (const [fx, fy] of RING) {
    const el: PlanElement = {
      id: newId(kind),
      kind,
      x: clamp(lot.w / 2 + fx * lot.w, size.w / 2 + 2, lot.w - size.w / 2 - 2),
      y: clamp(lot.d / 2 + fy * lot.d, size.d / 2 + 2, lot.d - size.d / 2 - 2),
      w: size.w,
      d: size.d,
      rot: 0,
    };
    if (!existing.some((e) => overlaps(el, e, pad))) return el;
  }
  // Every candidate was occupied — drop it at the center and let the user
  // drag. Refusing to place would be worse than a stack.
  return {
    id: newId(kind),
    kind,
    x: lot.w / 2,
    y: lot.d / 2,
    w: size.w,
    d: size.d,
    rot: 0,
  };
}

/**
 * Dropping onto a polygon.
 *
 * The bounding-box center of a notched or L-shaped parcel is routinely off
 * the parcel, so the drop point is the sample furthest from any boundary
 * (`innerPoint`) and the search ring is scaled to the box around it. A
 * driveway starts at the middle of the marked road frontage and runs inward
 * square to it, which is what an approach looks like on a plat.
 */
function placeOnPolygon(
  kind: ElementKind,
  pts: Pt[],
  existing: PlanElement[],
  frontSegment: number | null,
  size: { w: number; d: number }
): PlanElement {
  const lot: Lot = { kind: 'poly', pts };
  const box = lotBox(lot);
  const home = innerPoint(lot);

  if (kind === 'driveway' && frontSegment !== null && pts[frontSegment]) {
    const a = pts[frontSegment];
    const b = pts[(frontSegment + 1) % pts.length];
    const mid = { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
    const dx = b.x - a.x;
    const dy = b.y - a.y;
    const len = Math.hypot(dx, dy) || 1;
    // Inward is the outward normal reversed; clockwise winding puts the land
    // on the segment's left.
    const inx = -dy / len;
    const iny = dx / len;
    const run = clamp(Math.min(box.w, box.d) * 0.45, 20, 90);
    return {
      id: newId(kind),
      kind,
      x: mid.x + inx * (run / 2),
      y: mid.y + iny * (run / 2),
      w: size.w,
      d: run,
      // The run is drawn down the element's own y axis, so the rotation is
      // the inward direction's bearing off south.
      rot: (Math.atan2(inx, iny) * 180) / Math.PI,
    };
  }

  if (kind === 'waterEdge') {
    return {
      id: newId(kind),
      kind,
      x: home.x,
      y: home.y,
      w: clamp(box.w * 0.6, 20, box.w),
      d: 0,
      rot: 0,
    };
  }

  const pad = 6;
  for (const [fx, fy] of RING) {
    const el: PlanElement = {
      id: newId(kind),
      kind,
      x: home.x + fx * box.w,
      y: home.y + fy * box.d,
      w: size.w,
      d: size.d,
      rot: 0,
    };
    if (!existing.some((e) => overlaps(el, e, pad))) return el;
  }
  return { id: newId(kind), kind, x: home.x, y: home.y, w: size.w, d: size.d, rot: 0 };
}

/** Lots outside this range are almost always a typo (feet, not acres). */
export const LOT_MIN = 10;
export const LOT_MAX = 5280;

export function lotError(w: number, d: number): string | null {
  if (!Number.isFinite(w) || !Number.isFinite(d) || w <= 0 || d <= 0) {
    return 'Enter both dimensions in feet.';
  }
  if (w < LOT_MIN || d < LOT_MIN) {
    return `Both dimensions need to be at least ${LOT_MIN} ft.`;
  }
  if (w > LOT_MAX || d > LOT_MAX) {
    return 'That is over a mile on a side — enter feet, not acres.';
  }
  return null;
}

/** Acres, for the lot summary. 43,560 sq ft to the acre. */
export function acres(lot: Lot): number {
  return lotArea(lot) / 43560;
}

/** Fewest corners worth calling a boundary, and the most worth drawing. */
export const POLY_MIN_PTS = 3;
export const POLY_MAX_PTS = 60;

/**
 * What stops a polygon boundary being accepted — and what merely warns.
 *
 * Only three things block: too few corners to enclose anything, an area small
 * enough to be a mis-keyed unit, and a span past the rectangular lot's own
 * ceiling. A self-crossing boundary does NOT block (see `selfIntersects`):
 * it is reported and drawn, because an owner who has mistyped one call needs
 * to see the crossing to find it.
 */
export function polyError(pts: Pt[]): string | null {
  if (pts.length < POLY_MIN_PTS) {
    return 'A boundary needs at least three corners.';
  }
  if (pts.length > POLY_MAX_PTS) {
    return `That is over ${POLY_MAX_PTS} corners — simplify the meander segments.`;
  }
  if (pts.some((p) => !Number.isFinite(p.x) || !Number.isFinite(p.y))) {
    return 'One of the corners is not a number.';
  }
  const box = lotBox({ kind: 'poly', pts });
  if (box.w > LOT_MAX || box.d > LOT_MAX) {
    return 'That is over a mile across — check the units on your distances.';
  }
  if (polygonArea(pts) < LOT_MIN * LOT_MIN) {
    return 'That encloses almost no area — check the corners.';
  }
  return null;
}

/** Non-blocking: the boundary is drawable but a call is probably mistyped. */
export function polyWarning(pts: Pt[]): string | null {
  return pts.length >= 4 && selfIntersects(pts)
    ? 'Boundary crosses itself — check your corners.'
    : null;
}
