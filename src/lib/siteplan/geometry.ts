/**
 * Site Plan Studio — the maths.
 *
 * Everything here is pure and unit-tested (test/geometry.test.ts). It is the
 * one file where a silent error would print a wrong number on a permit
 * application, so it is written for exactness on the awkward cases rather
 * than for brevity: rotated rectangles, overlapping shapes, degenerate
 * shapes (the well is a point, the water edge is a line), and elements that
 * cross the property line.
 */

import type { EdgeName, Lot, PlanElement } from './types';

export interface Pt {
  x: number;
  y: number;
}

const EPS = 1e-9;

/** Degrees to radians. */
const rad = (deg: number) => (deg * Math.PI) / 180;

/**
 * The four corners of an element after rotation about its center, clockwise
 * from the local north-west. A zero-width or zero-depth element still returns
 * four points — two coincident pairs for a line, four for a point — which is
 * what lets one distance routine serve rectangles, lines and points.
 */
export function corners(el: Pick<PlanElement, 'x' | 'y' | 'w' | 'd' | 'rot'>): Pt[] {
  const hw = el.w / 2;
  const hd = el.d / 2;
  const a = rad(el.rot);
  const cos = Math.cos(a);
  const sin = Math.sin(a);
  const local: Pt[] = [
    { x: -hw, y: -hd },
    { x: hw, y: -hd },
    { x: hw, y: hd },
    { x: -hw, y: hd },
  ];
  return local.map((p) => ({
    x: el.x + p.x * cos - p.y * sin,
    y: el.y + p.x * sin + p.y * cos,
  }));
}

/** Shortest distance from a point to a line segment. Exact when a === b. */
export function pointSegmentDistance(p: Pt, a: Pt, b: Pt): number {
  const vx = b.x - a.x;
  const vy = b.y - a.y;
  const len2 = vx * vx + vy * vy;
  if (len2 < EPS) return Math.hypot(p.x - a.x, p.y - a.y);
  let t = ((p.x - a.x) * vx + (p.y - a.y) * vy) / len2;
  t = t < 0 ? 0 : t > 1 ? 1 : t;
  return Math.hypot(p.x - (a.x + t * vx), p.y - (a.y + t * vy));
}

/** Even-odd ray cast. A point exactly on the boundary may return either way. */
export function pointInPoly(p: Pt, poly: Pt[]): boolean {
  let inside = false;
  for (let i = 0, j = poly.length - 1; i < poly.length; j = i++) {
    const a = poly[i];
    const b = poly[j];
    if (a.y > p.y !== b.y > p.y) {
      const xAt = ((b.x - a.x) * (p.y - a.y)) / (b.y - a.y) + a.x;
      if (p.x < xAt) inside = !inside;
    }
  }
  return inside;
}

const cross = (o: Pt, a: Pt, b: Pt) =>
  (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);

/** True when segments p1p2 and p3p4 touch or cross. */
export function segmentsIntersect(p1: Pt, p2: Pt, p3: Pt, p4: Pt): boolean {
  const d1 = cross(p3, p4, p1);
  const d2 = cross(p3, p4, p2);
  const d3 = cross(p1, p2, p3);
  const d4 = cross(p1, p2, p4);
  if (((d1 > 0 && d2 < 0) || (d1 < 0 && d2 > 0)) &&
      ((d3 > 0 && d4 < 0) || (d3 < 0 && d4 > 0))) {
    return true;
  }
  // Collinear touching: fall back to a zero point-to-segment distance.
  if (Math.abs(d1) < EPS && pointSegmentDistance(p1, p3, p4) < EPS) return true;
  if (Math.abs(d2) < EPS && pointSegmentDistance(p2, p3, p4) < EPS) return true;
  if (Math.abs(d3) < EPS && pointSegmentDistance(p3, p1, p2) < EPS) return true;
  if (Math.abs(d4) < EPS && pointSegmentDistance(p4, p1, p2) < EPS) return true;
  return false;
}

/** The polygon's edges as ordered point pairs. */
function edges(poly: Pt[]): [Pt, Pt][] {
  const out: [Pt, Pt][] = [];
  for (let i = 0; i < poly.length; i++) {
    out.push([poly[i], poly[(i + 1) % poly.length]]);
  }
  return out;
}

/**
 * Minimum distance between two convex polygons, `0` when they overlap.
 *
 * Deliberately NOT a separating-axis test. SAT needs a non-degenerate
 * polygon to produce axes, and two of this tool's elements are degenerate by
 * design — the well is a point, the water edge is a line. Containment plus
 * edge-intersection plus a vertex-to-edge sweep is the same answer, holds up
 * on those shapes, and does not care whether the input is convex.
 */
export function polyDistance(a: Pt[], b: Pt[]): number {
  for (const p of a) if (pointInPoly(p, b)) return 0;
  for (const p of b) if (pointInPoly(p, a)) return 0;
  const ea = edges(a);
  const eb = edges(b);
  for (const [a1, a2] of ea) {
    for (const [b1, b2] of eb) {
      if (segmentsIntersect(a1, a2, b1, b2)) return 0;
    }
  }
  let min = Infinity;
  for (const p of a) {
    for (const [b1, b2] of eb) {
      const d = pointSegmentDistance(p, b1, b2);
      if (d < min) min = d;
    }
  }
  for (const p of b) {
    for (const [a1, a2] of ea) {
      const d = pointSegmentDistance(p, a1, a2);
      if (d < min) min = d;
    }
  }
  return min;
}

/** Distance between two placed elements, nearest edge to nearest edge. */
export function elementDistance(a: PlanElement, b: PlanElement): number {
  return polyDistance(corners(a), corners(b));
}

/**
 * Distance from an element to each property line.
 *
 * NEGATIVE MEANS THE ELEMENT CROSSES THAT LINE — its own warning, and one
 * that outranks every separation conflict, because a septic tank 8 ft from
 * the well is a design problem and a septic tank on the neighbor's land is
 * a different kind of problem entirely.
 */
export function distanceToLotEdges(
  el: PlanElement,
  lot: Lot
): Record<EdgeName, number> {
  const pts = corners(el);
  return {
    north: Math.min(...pts.map((p) => p.y)),
    south: Math.min(...pts.map((p) => lot.d - p.y)),
    west: Math.min(...pts.map((p) => p.x)),
    east: Math.min(...pts.map((p) => lot.w - p.x)),
  };
}

/** Distance to the nearest property line, whichever it is. */
export function nearestEdge(
  el: PlanElement,
  lot: Lot
): { edge: EdgeName; feet: number } {
  const d = distanceToLotEdges(el, lot);
  let edge: EdgeName = 'north';
  let feet = d.north;
  (['east', 'south', 'west'] as EdgeName[]).forEach((e) => {
    if (d[e] < feet) {
      feet = d[e];
      edge = e;
    }
  });
  return { edge, feet };
}

/**
 * The two ends of the dimension line from an element to one property line:
 * from the element's nearest corner, perpendicular to that edge. This is how
 * a setback is dimensioned on a real plan — square to the line, off the
 * closest point of the building.
 */
export function edgeDimension(
  el: PlanElement,
  lot: Lot,
  edge: EdgeName
): [Pt, Pt] {
  const pts = corners(el);
  if (edge === 'north') {
    const p = pts.reduce((a, b) => (b.y < a.y ? b : a));
    return [p, { x: p.x, y: 0 }];
  }
  if (edge === 'south') {
    const p = pts.reduce((a, b) => (b.y > a.y ? b : a));
    return [p, { x: p.x, y: lot.d }];
  }
  if (edge === 'west') {
    const p = pts.reduce((a, b) => (b.x < a.x ? b : a));
    return [p, { x: 0, y: p.y }];
  }
  const p = pts.reduce((a, b) => (b.x > a.x ? b : a));
  return [p, { x: lot.w, y: p.y }];
}

/** Axis-aligned bounds of an element after rotation. */
export function bounds(el: PlanElement) {
  const pts = corners(el);
  return {
    minX: Math.min(...pts.map((p) => p.x)),
    maxX: Math.max(...pts.map((p) => p.x)),
    minY: Math.min(...pts.map((p) => p.y)),
    maxY: Math.max(...pts.map((p) => p.y)),
  };
}

/** Midpoint of the shortest line between two elements — where a label sits. */
export function closestPoints(a: PlanElement, b: PlanElement): [Pt, Pt] {
  const pa = corners(a);
  const pb = corners(b);
  let best: [Pt, Pt] = [pa[0], pb[0]];
  let min = Infinity;
  const consider = (p: Pt, s1: Pt, s2: Pt, flip: boolean) => {
    const vx = s2.x - s1.x;
    const vy = s2.y - s1.y;
    const len2 = vx * vx + vy * vy;
    let t = len2 < EPS ? 0 : ((p.x - s1.x) * vx + (p.y - s1.y) * vy) / len2;
    t = t < 0 ? 0 : t > 1 ? 1 : t;
    const q = { x: s1.x + t * vx, y: s1.y + t * vy };
    const d = Math.hypot(p.x - q.x, p.y - q.y);
    if (d < min) {
      min = d;
      best = flip ? [q, p] : [p, q];
    }
  };
  for (const p of pa) for (const [b1, b2] of edges(pb)) consider(p, b1, b2, false);
  for (const p of pb) for (const [a1, a2] of edges(pa)) consider(p, a1, a2, true);
  return best;
}

/**
 * Decimal feet as drafting notation: 28.5 → 28'-6". Inches round to the
 * nearest inch and a remainder under half an inch prints as -0", because a
 * plot plan measured to the sixteenth is claiming a precision nobody has.
 */
export function formatFeet(n: number): string {
  const neg = n < 0;
  const abs = Math.abs(n);
  let ft = Math.floor(abs + 1e-9);
  let inches = Math.round((abs - ft) * 12);
  if (inches >= 12) {
    ft += 1;
    inches = 0;
  }
  return `${neg ? '−' : ''}${ft}'-${inches}"`;
}

/** Compact form for tight table cells: 78 ft, 78.5 ft. */
export function formatFeetShort(n: number): string {
  const r = Math.round(n * 10) / 10;
  return `${Number.isInteger(r) ? r : r.toFixed(1)} ft`;
}

/** Snap to the nearest foot unless the pointer is held with Alt. */
export function snapFoot(n: number, free: boolean): number {
  return free ? Math.round(n * 100) / 100 : Math.round(n);
}

/** Clamp with no assumption about argument order. */
export function clamp(n: number, lo: number, hi: number): number {
  return n < lo ? lo : n > hi ? hi : n;
}
