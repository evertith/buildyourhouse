/**
 * Geometry tests. Run directly, no build step and nothing wired into CI:
 *
 *   node --test --experimental-strip-types src/lib/siteplan/geometry.test.ts
 *
 * These cover the cases that ship wrong silently: a rotated rectangle's
 * corners, overlap returning exactly zero, point-to-segment (the water edge
 * and the well both depend on it), and the negative lot-edge distance that
 * means "outside the property line".
 */

import test from 'node:test';
import assert from 'node:assert/strict';

import {
  bounds,
  closestPoints,
  corners,
  distanceToLotEdges,
  elementDistance,
  formatFeet,
  formatFeetShort,
  nearestEdge,
  pointInPoly,
  pointSegmentDistance,
  polyDistance,
  segmentsIntersect,
  snapFoot,
} from './geometry.ts';
import type { PlanElement } from './types.ts';

const near = (a: number, b: number, tol = 1e-6, msg?: string) =>
  assert.ok(Math.abs(a - b) < tol, msg ?? `${a} !== ${b} (tol ${tol})`);

const el = (o: Partial<PlanElement>): PlanElement => ({
  id: 'x',
  kind: 'house',
  x: 0,
  y: 0,
  w: 10,
  d: 10,
  rot: 0,
  ...o,
});

// ---------------------------------------------------------------- corners

test('corners: unrotated rectangle', () => {
  const c = corners(el({ x: 50, y: 40, w: 40, d: 28, rot: 0 }));
  assert.deepEqual(
    c.map((p) => [p.x, p.y]),
    [
      [30, 26],
      [70, 26],
      [70, 54],
      [30, 54],
    ]
  );
});

test('corners: 90 degrees swaps the footprint', () => {
  const c = corners(el({ x: 0, y: 0, w: 40, d: 20, rot: 90 }));
  const b = bounds(el({ x: 0, y: 0, w: 40, d: 20, rot: 90 }));
  near(b.maxX - b.minX, 20, 1e-9, 'width becomes depth');
  near(b.maxY - b.minY, 40, 1e-9, 'depth becomes width');
  // Clockwise in a y-down world: the local NW corner lands top-right.
  near(c[0].x, 10);
  near(c[0].y, -20);
});

test('corners: 45 degrees puts a corner on the diagonal', () => {
  const c = corners(el({ x: 0, y: 0, w: 10, d: 10, rot: 45 }));
  const half = Math.sqrt(50); // half-diagonal of a 10x10
  near(Math.hypot(c[0].x, c[0].y), half);
  // Every corner keeps its distance from the center under rotation.
  for (const p of c) near(Math.hypot(p.x, p.y), half);
});

test('corners: rotation is about the center, not the origin', () => {
  const c = corners(el({ x: 100, y: 200, w: 10, d: 4, rot: 37 }));
  const cx = c.reduce((s, p) => s + p.x, 0) / 4;
  const cy = c.reduce((s, p) => s + p.y, 0) / 4;
  near(cx, 100, 1e-9);
  near(cy, 200, 1e-9);
});

test('corners: a well is four coincident points', () => {
  const c = corners(el({ kind: 'well', x: 12, y: 34, w: 0, d: 0, rot: 0 }));
  for (const p of c) {
    near(p.x, 12);
    near(p.y, 34);
  }
});

test('corners: a water edge is a line of the right length', () => {
  const c = corners(el({ kind: 'waterEdge', x: 0, y: 0, w: 120, d: 0, rot: 0 }));
  near(Math.hypot(c[1].x - c[0].x, c[1].y - c[0].y), 120);
  near(Math.hypot(c[2].x - c[1].x, c[2].y - c[1].y), 0);
});

// ------------------------------------------------------- point to segment

test('pointSegmentDistance: perpendicular foot inside the segment', () => {
  near(pointSegmentDistance({ x: 5, y: 3 }, { x: 0, y: 0 }, { x: 10, y: 0 }), 3);
});

test('pointSegmentDistance: clamps past the ends', () => {
  near(pointSegmentDistance({ x: -4, y: 0 }, { x: 0, y: 0 }, { x: 10, y: 0 }), 4);
  near(pointSegmentDistance({ x: 14, y: 0 }, { x: 0, y: 0 }, { x: 10, y: 0 }), 4);
  near(pointSegmentDistance({ x: 13, y: 4 }, { x: 0, y: 0 }, { x: 10, y: 0 }), 5);
});

test('pointSegmentDistance: degenerate segment is a point', () => {
  near(pointSegmentDistance({ x: 3, y: 4 }, { x: 0, y: 0 }, { x: 0, y: 0 }), 5);
});

test('pointSegmentDistance: on the segment is zero', () => {
  near(pointSegmentDistance({ x: 5, y: 0 }, { x: 0, y: 0 }, { x: 10, y: 0 }), 0);
});

// ----------------------------------------------------------- polyDistance

test('polyDistance: axis-aligned gap', () => {
  const a = corners(el({ x: 0, y: 0, w: 10, d: 10 }));
  const b = corners(el({ x: 30, y: 0, w: 10, d: 10 }));
  near(polyDistance(a, b), 20);
});

test('polyDistance: diagonal corner-to-corner gap', () => {
  const a = corners(el({ x: 0, y: 0, w: 10, d: 10 }));
  const b = corners(el({ x: 20, y: 20, w: 10, d: 10 }));
  near(polyDistance(a, b), Math.hypot(10, 10));
});

test('polyDistance: overlap is exactly zero', () => {
  const a = corners(el({ x: 0, y: 0, w: 20, d: 20 }));
  const b = corners(el({ x: 5, y: 5, w: 20, d: 20 }));
  assert.equal(polyDistance(a, b), 0);
});

test('polyDistance: full containment is zero', () => {
  const outer = corners(el({ x: 0, y: 0, w: 100, d: 100 }));
  const inner = corners(el({ x: 0, y: 0, w: 4, d: 4 }));
  assert.equal(polyDistance(outer, inner), 0);
  assert.equal(polyDistance(inner, outer), 0);
});

test('polyDistance: crossed rectangles with no vertex inside either', () => {
  // A plus sign: neither shape has a corner inside the other, but they overlap.
  const across = corners(el({ x: 0, y: 0, w: 100, d: 10 }));
  const down = corners(el({ x: 0, y: 0, w: 10, d: 100 }));
  assert.equal(polyDistance(across, down), 0);
});

test('polyDistance: touching edges is zero', () => {
  const a = corners(el({ x: 0, y: 0, w: 10, d: 10 }));
  const b = corners(el({ x: 10, y: 0, w: 10, d: 10 }));
  near(polyDistance(a, b), 0);
});

test('polyDistance: a point inside a rectangle is zero', () => {
  const house = corners(el({ x: 0, y: 0, w: 40, d: 28 }));
  const well = corners(el({ kind: 'well', x: 5, y: 5, w: 0, d: 0 }));
  assert.equal(polyDistance(house, well), 0, 'a well inside the house is not 5 ft away');
});

test('polyDistance: rotated rectangle measures from the true corner', () => {
  // A 10x10 turned 45 degrees has its corner sqrt(50) from the center, so
  // the gap to a wall at x = 50 is 50 - sqrt(50), not 50 - 5.
  const a = corners(el({ x: 0, y: 0, w: 10, d: 10, rot: 45 }));
  const wall = corners(el({ x: 60, y: 0, w: 20, d: 200 }));
  near(polyDistance(a, wall), 50 - Math.sqrt(50), 1e-9);
});

test('polyDistance: rotation reduces a face-to-face gap', () => {
  const square = el({ x: 0, y: 0, w: 20, d: 20 });
  const wall = el({ x: 60, y: 0, w: 10, d: 400 });
  const flat = elementDistance(square, wall);
  const turned = elementDistance({ ...square, rot: 45 }, wall);
  near(flat, 45);
  assert.ok(turned < flat, 'a 45-degree square reaches further toward the wall');
  near(turned, 55 - Math.sqrt(200), 1e-9);
});

test('polyDistance: symmetric', () => {
  const a = corners(el({ x: 3, y: 7, w: 14, d: 9, rot: 22 }));
  const b = corners(el({ x: 80, y: 40, w: 20, d: 5, rot: -14 }));
  near(polyDistance(a, b), polyDistance(b, a), 1e-9);
});

test('polyDistance: well to water edge is point to segment', () => {
  const well = corners(el({ kind: 'well', x: 50, y: 10, w: 0, d: 0 }));
  const water = corners(el({ kind: 'waterEdge', x: 50, y: 90, w: 200, d: 0 }));
  near(polyDistance(well, water), 80);
  // Off the end of the line, the distance runs to the endpoint.
  const shortWater = corners(el({ kind: 'waterEdge', x: 200, y: 10, w: 40, d: 0 }));
  near(polyDistance(well, shortWater), 130);
});

// -------------------------------------------------------- point-in-polygon

test('pointInPoly: inside, outside, and a rotated shape', () => {
  const sq = corners(el({ x: 0, y: 0, w: 10, d: 10 }));
  assert.equal(pointInPoly({ x: 0, y: 0 }, sq), true);
  assert.equal(pointInPoly({ x: 9, y: 0 }, sq), false);
  const turned = corners(el({ x: 0, y: 0, w: 10, d: 10, rot: 45 }));
  assert.equal(pointInPoly({ x: 0, y: 0 }, turned), true);
  // (4.9, 4.9) is inside the axis-aligned square but outside the turned one.
  assert.equal(pointInPoly({ x: 4.9, y: 4.9 }, sq), true);
  assert.equal(pointInPoly({ x: 4.9, y: 4.9 }, turned), false);
});

test('segmentsIntersect: crossing, parallel, and collinear touching', () => {
  assert.equal(
    segmentsIntersect({ x: 0, y: 0 }, { x: 10, y: 10 }, { x: 0, y: 10 }, { x: 10, y: 0 }),
    true
  );
  assert.equal(
    segmentsIntersect({ x: 0, y: 0 }, { x: 10, y: 0 }, { x: 0, y: 5 }, { x: 10, y: 5 }),
    false
  );
  assert.equal(
    segmentsIntersect({ x: 0, y: 0 }, { x: 10, y: 0 }, { x: 10, y: 0 }, { x: 20, y: 0 }),
    true
  );
});

// ------------------------------------------------------- lot edge distance

test('distanceToLotEdges: four distances from a centered house', () => {
  const lot = { w: 150, d: 200 };
  const d = distanceToLotEdges(el({ x: 75, y: 100, w: 40, d: 28 }), lot);
  near(d.west, 55);
  near(d.east, 55);
  near(d.north, 86);
  near(d.south, 86);
});

test('distanceToLotEdges: negative means over the property line', () => {
  const lot = { w: 150, d: 200 };
  const d = distanceToLotEdges(el({ x: 10, y: 100, w: 40, d: 28 }), lot);
  near(d.west, -10, 1e-9, 'the west wall is 10 ft onto the neighbor');
  assert.ok(d.west < 0);
  // Measured from the NEAREST corner (x = 30), not from the center.
  near(d.east, 120);
});

test('distanceToLotEdges: a rotated house reaches further than its half-width', () => {
  const lot = { w: 200, d: 200 };
  const flat = distanceToLotEdges(el({ x: 100, y: 100, w: 40, d: 28 }), lot);
  const turned = distanceToLotEdges(el({ x: 100, y: 100, w: 40, d: 28, rot: 30 }), lot);
  near(flat.west, 80);
  assert.ok(turned.west < flat.west);
  // Half-diagonal projection: 20cos30 + 14sin30 = 24.32
  near(turned.west, 100 - (20 * Math.cos(Math.PI / 6) + 14 * Math.sin(Math.PI / 6)), 1e-9);
});

test('distanceToLotEdges: a well is a point on all four edges', () => {
  const d = distanceToLotEdges(el({ kind: 'well', x: 30, y: 40, w: 0, d: 0 }), {
    w: 150,
    d: 200,
  });
  near(d.west, 30);
  near(d.east, 120);
  near(d.north, 40);
  near(d.south, 160);
});

test('nearestEdge: picks the smallest, including a negative one', () => {
  const lot = { w: 150, d: 200 };
  assert.equal(nearestEdge(el({ x: 20, y: 100, w: 10, d: 10 }), lot).edge, 'west');
  assert.equal(nearestEdge(el({ x: 75, y: 6, w: 10, d: 10 }), lot).edge, 'north');
  const over = nearestEdge(el({ x: 75, y: 198, w: 10, d: 10 }), lot);
  assert.equal(over.edge, 'south');
  assert.ok(over.feet < 0);
});

// ----------------------------------------------------------- closestPoints

test('closestPoints: the shortest line lands on both shapes', () => {
  const a = el({ x: 0, y: 0, w: 10, d: 10 });
  const b = el({ x: 40, y: 0, w: 10, d: 10 });
  const [p, q] = closestPoints(a, b);
  near(p.x, 5);
  near(q.x, 35);
  near(Math.hypot(q.x - p.x, q.y - p.y), elementDistance(a, b), 1e-9);
});

// ------------------------------------------------------------- formatFeet

test('formatFeet: drafting notation', () => {
  assert.equal(formatFeet(28), `28'-0"`);
  assert.equal(formatFeet(28.5), `28'-6"`);
  assert.equal(formatFeet(0), `0'-0"`);
  assert.equal(formatFeet(0.25), `0'-3"`);
  assert.equal(formatFeet(100.02), `100'-0"`, 'a remainder under an inch drops');
  assert.equal(formatFeet(27.99), `28'-0"`, 'rounds up rather than printing 11 inches');
  assert.equal(formatFeet(-10.5), `−10'-6"`);
});

test('formatFeetShort: one decimal, no trailing zero', () => {
  assert.equal(formatFeetShort(78), '78 ft');
  assert.equal(formatFeetShort(78.46), '78.5 ft');
  assert.equal(formatFeetShort(78.04), '78 ft');
});

test('snapFoot: whole feet unless free placement', () => {
  assert.equal(snapFoot(12.4, false), 12);
  assert.equal(snapFoot(12.6, false), 13);
  assert.equal(snapFoot(12.437, true), 12.44);
});
