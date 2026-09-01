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

import type { EdgeName, Lot, PlanElement, Pt, RectLot } from './types';

// `Pt` is declared in types.ts so that `Lot` can hold one without the two
// modules importing each other. Re-exported here because every drawing
// component already reaches for it from geometry.
export type { Pt };

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
  lot: RectLot
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
  lot: RectLot
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
  lot: RectLot,
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

// ---------------------------------------------------------------------------
// POLYGON LOTS (v1.5)
//
// A rectangle is a polygon with four corners, so everything below works for
// both — but the rect path keeps its own named-edge routines above, because
// "35 ft off the north line" is what a rectangular plot plan says and losing
// the compass name to a generic "nearest boundary" would be a downgrade.
// ---------------------------------------------------------------------------

/** The lot boundary as a clockwise ring, first point NOT repeated. */
export function lotRing(lot: Lot): Pt[] {
  if (lot.kind === 'poly') return lot.pts;
  return [
    { x: 0, y: 0 },
    { x: lot.w, y: 0 },
    { x: lot.w, y: lot.d },
    { x: 0, y: lot.d },
  ];
}

export interface LotBox {
  minX: number;
  minY: number;
  maxX: number;
  maxY: number;
  /** East-west span, feet. */
  w: number;
  /** North-south span, feet. */
  d: number;
  cx: number;
  cy: number;
}

/**
 * The lot's bounding box. Every fit-to-view decision in the tool runs through
 * this — the canvas viewBox, the printed sheet's scale, the aspect the canvas
 * takes — so a notched parcel is framed by what it actually spans rather than
 * by two numbers it no longer has.
 */
export function lotBox(lot: Lot): LotBox {
  if (lot.kind === 'rect') {
    return {
      minX: 0,
      minY: 0,
      maxX: lot.w,
      maxY: lot.d,
      w: lot.w,
      d: lot.d,
      cx: lot.w / 2,
      cy: lot.d / 2,
    };
  }
  const xs = lot.pts.map((p) => p.x);
  const ys = lot.pts.map((p) => p.y);
  const minX = Math.min(...xs);
  const maxX = Math.max(...xs);
  const minY = Math.min(...ys);
  const maxY = Math.max(...ys);
  return {
    minX,
    minY,
    maxX,
    maxY,
    w: maxX - minX,
    d: maxY - minY,
    cx: (minX + maxX) / 2,
    cy: (minY + maxY) / 2,
  };
}

/**
 * Twice the signed shoelace area. POSITIVE IS CLOCKWISE, because the world is
 * y-down: (0,0) → (10,0) → (10,10) → (0,10) reads clockwise on screen and
 * sums positive. Getting this backwards would flip every outward normal and
 * print the side lengths inside the lot.
 */
export function signedArea2(poly: Pt[]): number {
  let sum = 0;
  for (let i = 0; i < poly.length; i++) {
    const a = poly[i];
    const b = poly[(i + 1) % poly.length];
    sum += a.x * b.y - b.x * a.y;
  }
  return sum;
}

/** Enclosed area in square feet, winding-independent. */
export function polygonArea(poly: Pt[]): number {
  return Math.abs(signedArea2(poly)) / 2;
}

export function lotArea(lot: Lot): number {
  return lot.kind === 'rect' ? lot.w * lot.d : polygonArea(lot.pts);
}

/** Reverses a counter-clockwise ring. Deed calls run either way round. */
export function ensureClockwise(poly: Pt[]): Pt[] {
  return signedArea2(poly) < 0 ? [...poly].reverse() : poly;
}

/** Closest point on a segment to p, and how far away it is. */
function segmentClosest(p: Pt, a: Pt, b: Pt): { at: Pt; feet: number } {
  const vx = b.x - a.x;
  const vy = b.y - a.y;
  const len2 = vx * vx + vy * vy;
  let t = len2 < EPS ? 0 : ((p.x - a.x) * vx + (p.y - a.y) * vy) / len2;
  t = t < 0 ? 0 : t > 1 ? 1 : t;
  const at = { x: a.x + t * vx, y: a.y + t * vy };
  return { at, feet: Math.hypot(p.x - at.x, p.y - at.y) };
}

/** Nearest point on a ring to p, with the index of the segment it lands on. */
export function pointToRing(
  p: Pt,
  ring: Pt[]
): { feet: number; at: Pt; index: number } {
  let best = { feet: Infinity, at: p, index: 0 };
  for (let i = 0; i < ring.length; i++) {
    const c = segmentClosest(p, ring[i], ring[(i + 1) % ring.length]);
    if (c.feet < best.feet) best = { feet: c.feet, at: c.at, index: i };
  }
  return best;
}

/**
 * Shortest distance from a shape to a ring's BOUNDARY, with the two ends of
 * that line.
 *
 * Deliberately not `polyDistance`: that returns 0 for containment, which is
 * the right answer for two elements overlapping and the wrong one for a house
 * inside its own lot. The house is some distance from the property line, and
 * that distance is the entire question a setback asks.
 *
 * Both directions are swept — shape vertices against ring segments AND ring
 * vertices against shape segments — because on a notched parcel the closest
 * approach is often the notch's corner poking at the middle of a wall, which
 * a vertex-only sweep from the shape would miss entirely.
 */
export function boundaryClosest(
  shape: Pt[],
  ring: Pt[]
): { feet: number; a: Pt; b: Pt; index: number } {
  let best = { feet: Infinity, a: shape[0], b: ring[0], index: 0 };
  for (const p of shape) {
    for (let i = 0; i < ring.length; i++) {
      const c = segmentClosest(p, ring[i], ring[(i + 1) % ring.length]);
      if (c.feet < best.feet) best = { feet: c.feet, a: p, b: c.at, index: i };
    }
  }
  for (let i = 0; i < ring.length; i++) {
    const v = ring[i];
    for (let j = 0; j < shape.length; j++) {
      const c = segmentClosest(v, shape[j], shape[(j + 1) % shape.length]);
      // The ring vertex sits on segments i-1 and i; credit it to i.
      if (c.feet < best.feet) best = { feet: c.feet, a: c.at, b: v, index: i };
    }
  }
  return best;
}

/** Pulls a shape in toward its own center by `by` feet. */
function shrink(shape: Pt[], by: number): Pt[] {
  const cx = shape.reduce((s, p) => s + p.x, 0) / shape.length;
  const cy = shape.reduce((s, p) => s + p.y, 0) / shape.length;
  return shape.map((p) => {
    const dx = p.x - cx;
    const dy = p.y - cy;
    const len = Math.hypot(dx, dy);
    if (len <= by) return { x: cx, y: cy };
    const k = 1 - by / len;
    return { x: cx + dx * k, y: cy + dy * k };
  });
}

/**
 * True when any part of the element is off the parcel.
 *
 * Three tests, and a notched parcel needs all three. Corners outside the lot
 * is the ordinary case. A boundary corner inside the element is the notch
 * biting a chunk out of a house. The third is the one that surprised the
 * tests: a notch narrower than the house slices straight through it, in one
 * wall and out the other, so no corner of the house leaves the parcel and no
 * corner of the parcel enters the house — and the middle of the house is on
 * the neighbor's land regardless.
 *
 * The crossing test runs against a slightly shrunken element so that a
 * building drawn deliberately ON the property line is touching, not crossing.
 */
export function elementOutside(el: PlanElement, lot: Lot): boolean {
  const ring = lotRing(lot);
  const shape = corners(el);
  if (shape.some((p) => !pointInPoly(p, ring))) return true;
  if (ring.some((v) => pointInPoly(v, shape))) return true;
  const inner = shrink(shape, 0.02);
  for (let i = 0; i < inner.length; i++) {
    const a1 = inner[i];
    const a2 = inner[(i + 1) % inner.length];
    for (let j = 0; j < ring.length; j++) {
      if (segmentsIntersect(a1, a2, ring[j], ring[(j + 1) % ring.length])) {
        return true;
      }
    }
  }
  return false;
}

/**
 * How far the worst part of an element reaches past the property line, and
 * the line to draw for it.
 *
 * Corners alone are not enough — the deepest overhang of a house sliced by a
 * narrow notch is in the middle of the house, not at any corner — so the
 * footprint is sampled on a grid in the element's OWN frame, which keeps it
 * correct under rotation and collapses harmlessly for the well (a point) and
 * the water edge (a line). Only reached once an element is known to be
 * outside, so the ordinary drag pays nothing for it.
 */
function overshoot(el: PlanElement, ring: Pt[]): { feet: number; a: Pt; b: Pt; index: number } {
  const a = rad(el.rot);
  const cos = Math.cos(a);
  const sin = Math.sin(a);
  const N = 8;
  let worst = { feet: -1, a: { x: el.x, y: el.y }, b: { x: el.x, y: el.y }, index: 0 };
  for (let i = 0; i <= N; i++) {
    for (let j = 0; j <= N; j++) {
      const lx = el.w * (i / N - 0.5);
      const ly = el.d * (j / N - 0.5);
      const p = {
        x: el.x + lx * cos - ly * sin,
        y: el.y + lx * sin + ly * cos,
      };
      if (pointInPoly(p, ring)) continue;
      const r = pointToRing(p, ring);
      if (r.feet > worst.feet) worst = { feet: r.feet, a: p, b: r.at, index: r.index };
    }
  }
  if (worst.feet < 0) {
    // Nothing sampled outside, yet the element is known to cross: the strip
    // off the parcel is thinner than the sample spacing. Report it as a
    // crossing of no measurable depth rather than inventing a number.
    const c = boundaryClosest(corners(el), ring);
    return { feet: 0, a: c.a, b: c.b, index: c.index };
  }
  return worst;
}

export interface BoundaryMeasure {
  /** Feet to the nearest property line. NEGATIVE means the element crosses it. */
  feet: number;
  /** The two ends of the dimension line. */
  a: Pt;
  b: Pt;
  /** Named edge on a rectangular lot; null on a polygon. */
  edge: EdgeName | null;
  /** Index into the polygon ring of the segment measured to. */
  segment: number;
}

/**
 * Distance from an element to the nearest property line, whatever shape the
 * lot is. The rectangular path is the old named-edge maths untouched, so
 * every number a rect plan printed before prints identically now.
 *
 * When the element crosses the line the sign flips and the magnitude becomes
 * how far PAST the line its worst corner reaches — not the near-zero distance
 * from the crossing shape to the boundary it is sitting on. "Two feet onto
 * the neighbor" is the useful sentence; "0.0 ft from the line" is not.
 */
export function nearestBoundary(el: PlanElement, lot: Lot): BoundaryMeasure {
  if (lot.kind === 'rect') {
    const { edge, feet } = nearestEdge(el, lot);
    const [a, b] = edgeDimension(el, lot, edge);
    const RECT_SEG: Record<EdgeName, number> = { north: 0, east: 1, south: 2, west: 3 };
    return { feet, a, b, edge, segment: RECT_SEG[edge] };
  }

  const ring = lot.pts;
  if (elementOutside(el, lot)) {
    const o = overshoot(el, ring);
    return { feet: -o.feet, a: o.a, b: o.b, edge: null, segment: o.index };
  }
  const c = boundaryClosest(corners(el), ring);
  return { feet: c.feet, a: c.a, b: c.b, edge: null, segment: c.index };
}

/**
 * The unit vector pointing OUT of the lot, square to segment `i`. Side-length
 * labels sit along this so they print outside the boundary the way a plat
 * prints them, and never over the house.
 */
export function outwardNormal(ring: Pt[], i: number): Pt {
  const a = ring[i];
  const b = ring[(i + 1) % ring.length];
  const dx = b.x - a.x;
  const dy = b.y - a.y;
  const len = Math.hypot(dx, dy) || 1;
  // Clockwise winding in a y-down world puts the interior to the segment's
  // left, so the outward side is (dy, -dx).
  return { x: dy / len, y: -dx / len };
}

/** Length of each side, in ring order. */
export function sideLengths(ring: Pt[]): number[] {
  return ring.map((a, i) => {
    const b = ring[(i + 1) % ring.length];
    return Math.hypot(b.x - a.x, b.y - a.y);
  });
}

/**
 * True when two non-adjacent sides cross. Reported as a warning and never as
 * a block: an owner mid-entry has a self-crossing boundary for as long as it
 * takes them to place the next corner, and refusing to draw it would make the
 * tool feel broken at exactly the moment they need to see what they typed.
 */
export function selfIntersects(poly: Pt[]): boolean {
  const n = poly.length;
  if (n < 4) return false;
  for (let i = 0; i < n; i++) {
    for (let j = i + 1; j < n; j++) {
      // Adjacent sides share a vertex; the wrap-around pair does too.
      if (j === i + 1 || (i === 0 && j === n - 1)) continue;
      if (
        segmentsIntersect(
          poly[i],
          poly[(i + 1) % n],
          poly[j],
          poly[(j + 1) % n]
        )
      ) {
        return true;
      }
    }
  }
  return false;
}

/**
 * A point well inside the lot to drop a new element at: the sample point
 * furthest from any boundary. A notched or L-shaped parcel's bounding-box
 * center is routinely outside the parcel, and dropping a house on the
 * neighbor's land the moment someone clicks "House" would be a bad first
 * impression of a tool whose whole job is that distinction.
 */
export function innerPoint(lot: Lot): Pt {
  if (lot.kind === 'rect') return { x: lot.w / 2, y: lot.d / 2 };
  const box = lotBox(lot);
  const ring = lot.pts;
  const center = { x: box.cx, y: box.cy };
  let best = pointInPoly(center, ring)
    ? { p: center, d: pointToRing(center, ring).feet }
    : { p: center, d: -1 };
  const N = 16;
  for (let i = 1; i < N; i++) {
    for (let j = 1; j < N; j++) {
      const p = {
        x: box.minX + (box.w * i) / N,
        y: box.minY + (box.d * j) / N,
      };
      if (!pointInPoly(p, ring)) continue;
      const d = pointToRing(p, ring).feet;
      if (d > best.d) best = { p, d };
    }
  }
  return best.p;
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
