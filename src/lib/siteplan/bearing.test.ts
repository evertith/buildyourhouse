/**
 * Bearing and closure tests. Run directly, no build step:
 *
 *   node --test --experimental-strip-types src/lib/siteplan/bearing.test.ts
 *
 * The parser is the piece most likely to be wrong in a way nobody notices:
 * a quadrant read into the wrong quadrant still draws a plausible-looking
 * parcel, just not the owner's. So every accepted format is asserted against
 * a known azimuth, the y-down sign convention is pinned in both axes, and a
 * real five-call boundary is walked and checked for closure.
 */

import test from 'node:test';
import assert from 'node:assert/strict';

import {
  callVector,
  canCloseGap,
  closeGap,
  closure,
  formatAzimuth,
  formatBearing,
  normalizeAzimuth,
  parseBearing,
  ringFromTraverse,
  traverse,
} from './bearing.ts';
import { ensureClockwise, polygonArea, signedArea2 } from './geometry.ts';

const near = (a: number, b: number, tol = 1e-9, msg?: string) =>
  assert.ok(Math.abs(a - b) < tol, msg ?? `${a} !== ${b} (tol ${tol})`);

const az = (s: string): number => {
  const p = parseBearing(s);
  assert.ok(p, `failed to parse ${JSON.stringify(s)}`);
  return p!.azimuth;
};

// ------------------------------------------------------------ quadrant forms

test('parseBearing: the four quadrants', () => {
  near(az('N 42 E'), 42);
  near(az('S 42 E'), 138);
  near(az('S 42 W'), 222);
  near(az('N 42 W'), 318);
});

test('parseBearing: degrees, minutes and seconds', () => {
  near(az('N 42°15\' E'), 42.25);
  near(az('N 42°15\'30" E'), 42 + 15 / 60 + 30 / 3600);
  near(az('N 42 15 30 E'), 42 + 15 / 60 + 30 / 3600);
  near(az('N42-15-30E'), 42 + 15 / 60 + 30 / 3600);
  near(az('n42-15-30e'), 42 + 15 / 60 + 30 / 3600);
});

test('parseBearing: whitespace and punctuation are optional', () => {
  near(az('N42.5E'), 42.5);
  near(az('  S   7   W  '), 187);
  near(az('S7W'), 187);
  near(az('N 42°15’ E'), 42.25, 1e-9, 'a curly apostrophe is still a minute mark');
});

test('parseBearing: minutes and seconds carry into the quadrant maths', () => {
  // A south-west call: 180 + the angle, minutes included.
  near(az('S 12°30\' W'), 192.5);
  // A north-west call subtracts from 360.
  near(az('N 12°30\' W'), 347.5);
});

test('parseBearing: zero and ninety are exact', () => {
  near(az('S 0°00\'00" E'), 180);
  near(az('N 0 E'), 0);
  near(az('N 90 E'), 90);
  near(az('S 90 W'), 270);
});

test('parseBearing: spelled-out quadrants', () => {
  near(az('North 42 East'), 42);
  near(az('south 7 west'), 187);
});

// ------------------------------------------------------------- azimuth forms

test('parseBearing: azimuth', () => {
  near(az('azimuth 132.5'), 132.5);
  near(az('az 132.5'), 132.5);
  near(az('132.5'), 132.5);
  near(az('132.5°'), 132.5);
  near(az('az 132-30'), 132.5, 1e-9, 'azimuth accepts DMS too');
  near(az('bearing 5'), 5);
});

test('parseBearing: azimuth wraps at 360', () => {
  near(az('360'), 0);
  near(az('az 359.9'), 359.9);
});

// ------------------------------------------------------------ cardinal forms

test('parseBearing: cardinals', () => {
  near(az('due north'), 0);
  near(az('N'), 0);
  near(az('east'), 90);
  near(az('due W'), 270);
});

// -------------------------------------------------------------- what fails

test('parseBearing: rejects what it cannot resolve', () => {
  assert.equal(parseBearing(''), null);
  assert.equal(parseBearing('   '), null);
  assert.equal(parseBearing('northeasterly'), null);
  assert.equal(parseBearing('N E'), null, 'no angle');
  assert.equal(parseBearing('N 42 X'), null, 'not a quadrant');
  assert.equal(parseBearing('N 95 E'), null, 'over 90 in a quadrant');
  assert.equal(parseBearing('N 42°75\' E'), null, 'minutes over 59');
  assert.equal(parseBearing('az 400'), null, 'over 360');
  assert.equal(parseBearing('to the point of beginning'), null);
});

// -------------------------------------------------------------- round trips

test('formatBearing: quadrant round trip', () => {
  for (const a of [42, 42.25, 137.75, 222.5, 318.125, 1.5, 358.5]) {
    near(az(formatBearing(a)), a, 1e-9, `round trip failed at ${a}`);
  }
});

test('formatBearing: whole-second round trip', () => {
  for (const secs of [0, 1, 30, 59, 3599, 12345, 300000]) {
    const a = normalizeAzimuth(secs / 3600);
    near(az(formatBearing(a)), a, 1e-9, `round trip failed at ${a}`);
  }
});

test('formatBearing: prints the deed idiom', () => {
  assert.equal(formatBearing(42.25), `N 42°15' E`);
  assert.equal(formatBearing(42), 'N 42° E');
  assert.equal(formatBearing(138), 'S 42° E');
  assert.equal(formatBearing(222), 'S 42° W');
  assert.equal(formatBearing(318), 'N 42° W');
  assert.equal(formatBearing(0), 'DUE N');
  assert.equal(formatBearing(90), 'DUE E');
  assert.equal(formatBearing(180), 'DUE S');
  assert.equal(formatBearing(270), 'DUE W');
});

test('formatAzimuth: its own idiom, and it parses back', () => {
  assert.equal(formatAzimuth(132.5), `AZ 132°30'`);
  near(az(formatAzimuth(132.5)), 132.5);
});

// ------------------------------------------------------------- the walk

test('callVector: the world is y-down, so north is negative y', () => {
  const n = callVector(0, 100);
  near(n.x, 0, 1e-9);
  near(n.y, -100, 1e-9, 'due north walks UP the drawing');
  const e = callVector(90, 100);
  near(e.x, 100, 1e-9);
  near(e.y, 0, 1e-9);
  const s = callVector(180, 100);
  near(s.y, 100, 1e-9);
  const w = callVector(270, 100);
  near(w.x, -100, 1e-9);
});

test('callVector: a 45 degree call splits the distance', () => {
  const v = callVector(45, Math.SQRT2 * 100);
  near(v.x, 100, 1e-9);
  near(v.y, -100, 1e-9);
});

test('traverse: four cardinal calls close a square exactly', () => {
  const pts = traverse({ x: 0, y: 0 }, [
    { azimuth: 90, distance: 100 },
    { azimuth: 180, distance: 100 },
    { azimuth: 270, distance: 100 },
    { azimuth: 0, distance: 100 },
  ]);
  assert.equal(pts.length, 5);
  const c = closure(pts);
  near(c.feet, 0, 1e-9);
  near(c.perimeter, 400, 1e-9);
  const ring = ringFromTraverse(pts);
  assert.equal(ring.length, 4, 'the closing point is dropped');
  near(polygonArea(ring), 10000, 1e-9);
});

test('traverse: a deed that omits its closing call keeps its last corner', () => {
  // Three sides of the same square: the ring closes on the implied fourth.
  const pts = traverse({ x: 0, y: 0 }, [
    { azimuth: 90, distance: 100 },
    { azimuth: 180, distance: 100 },
    { azimuth: 270, distance: 100 },
  ]);
  const ring = ringFromTraverse(pts);
  assert.equal(ring.length, 4);
  near(polygonArea(ring), 10000, 1e-9);
  near(closure(pts).feet, 100, 1e-9);
  assert.equal(canCloseGap(pts), false, 'a whole missing side is not a rounding gap');
});

test('closure: reports the gap as a vector back to the start', () => {
  const pts = traverse({ x: 0, y: 0 }, [
    { azimuth: 90, distance: 100 },
    { azimuth: 180, distance: 100 },
    { azimuth: 270, distance: 97 },
    { azimuth: 0, distance: 100 },
  ]);
  const c = closure(pts);
  near(c.feet, 3, 1e-9, 'three feet short on one call ends three feet out');
  near(c.dx, -3, 1e-9);
  near(c.dy, 0, 1e-9);
  assert.equal(canCloseGap(pts), true);
});

test('closeGap: moves the last point onto the point of beginning', () => {
  const pts = traverse({ x: 0, y: 0 }, [
    { azimuth: 90, distance: 100 },
    { azimuth: 180, distance: 100 },
    { azimuth: 270, distance: 97 },
    { azimuth: 0, distance: 100 },
  ]);
  const fixed = closeGap(pts);
  near(closure(fixed).feet, 0, 1e-9);
  // Only the last point moved.
  for (let i = 0; i < pts.length - 1; i++) {
    near(fixed[i].x, pts[i].x, 1e-9);
    near(fixed[i].y, pts[i].y, 1e-9);
  }
  assert.equal(ringFromTraverse(fixed).length, 4);
});

test('canCloseGap: a closed boundary has no gap to close', () => {
  const pts = traverse({ x: 0, y: 0 }, [
    { azimuth: 90, distance: 100 },
    { azimuth: 180, distance: 100 },
    { azimuth: 270, distance: 100 },
    { azimuth: 0, distance: 100 },
  ]);
  assert.equal(canCloseGap(pts), false);
});

// -------------------------------------------- a real five-call parcel

test('a five-call deed parses, walks and closes', () => {
  // Written the way a plat prints it, mixing the accepted formats.
  const deed: [string, number][] = [
    ['N 90°00\' E', 300],
    ['S 18°26\'06" E', 158.114],
    ['S 90 W', 250],
    ['az 315', 70.711],
    ['N 26°33\'54" W', 111.803],
  ];
  const calls = deed.map(([b, distance]) => {
    const p = parseBearing(b);
    assert.ok(p, `failed to parse ${b}`);
    return { azimuth: p!.azimuth, distance };
  });
  near(calls[0].azimuth, 90);
  near(calls[1].azimuth, 180 - (18 + 26 / 60 + 6 / 3600));
  near(calls[3].azimuth, 315);

  const pts = traverse({ x: 0, y: 0 }, calls);
  assert.equal(pts.length, 6);
  const c = closure(pts);
  assert.ok(c.feet < 0.01, `a good deed closes tight, got ${c.feet}`);
  near(c.perimeter, 890.628, 1e-3);

  const ring = ringFromTraverse(pts);
  assert.equal(ring.length, 5, 'five calls, five corners');
  // (0,0) (300,0) (350,150) (100,150) (50,100) — 42,500 sq ft, just under an acre.
  near(polygonArea(ring), 42500, 0.2);
  assert.ok(signedArea2(ring) > 0, 'a deed walked clockwise stores as drawn');
});

test('a counter-clockwise deed is turned clockwise for the lot', () => {
  // The same square walked the other way round.
  const ccw = ringFromTraverse(
    traverse({ x: 0, y: 0 }, [
      { azimuth: 180, distance: 100 },
      { azimuth: 90, distance: 100 },
      { azimuth: 0, distance: 100 },
      { azimuth: 270, distance: 100 },
    ])
  );
  assert.ok(signedArea2(ccw) < 0, 'walked counter-clockwise');
  const cw = ensureClockwise(ccw);
  assert.ok(signedArea2(cw) > 0, 'stored clockwise');
  near(polygonArea(cw), 10000, 1e-9);
});
