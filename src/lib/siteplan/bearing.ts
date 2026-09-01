/**
 * Site Plan Studio — metes and bounds.
 *
 * Owners do not hold their boundary as a list of coordinates. They hold it as
 * the calls printed on their deed or plat: a bearing and a distance per side,
 * walked turtle-style from the point of beginning. This module reads those
 * calls in the forms they are actually written in, walks them, and reports
 * whether the walk came back to where it started.
 *
 * BEARINGS ACCEPTED
 *   quadrant   N 42°15' E · N42-15-30E · S 7 W · N 42 15 30 E · S 0°00'00" E
 *   azimuth    azimuth 132.5 · az 132-30 · 132.5° · 132.5
 *   cardinal   due north · north · N
 *
 * Everything resolves to an AZIMUTH: degrees clockwise from north, 0 ≤ a < 360.
 * The world is +x east and +y SOUTH (types.ts), so a call of azimuth `a` and
 * length `L` steps (L·sin a, −L·cos a) — the minus is the whole difference
 * between a boundary that closes and one that is mirrored about the east-west
 * axis, which is exactly the bug that would ship silently.
 */

import type { Pt } from './types';

export interface ParsedBearing {
  /** Degrees clockwise from north, 0 ≤ azimuth < 360. */
  azimuth: number;
  /** Canonical form for display: "N 42°15' E", "DUE E", "AZ 132°30'". */
  label: string;
}

const NUM = /\d+(?:\.\d+)?/g;

const CARDINAL: Record<string, number> = {
  n: 0,
  north: 0,
  e: 90,
  east: 90,
  s: 180,
  south: 180,
  w: 270,
  west: 270,
};

/** Degrees, minutes, seconds → decimal degrees. Missing parts are zero. */
function dms(parts: number[]): number | null {
  const [deg = 0, min = 0, sec = 0] = parts;
  if (min >= 60 || sec >= 60) return null;
  return deg + min / 60 + sec / 3600;
}

export function normalizeAzimuth(a: number): number {
  return ((a % 360) + 360) % 360;
}

/**
 * Reads one bearing. Returns null on anything it cannot resolve — a row that
 * will not parse must stay visibly unparsed rather than quietly become north.
 */
export function parseBearing(raw: string): ParsedBearing | null {
  const text = String(raw ?? '')
    .trim()
    .toLowerCase()
    // Spelled-out quadrants are common on older deeds ("North 42 East").
    .replace(/\bnorth\b/g, 'n')
    .replace(/\bsouth\b/g, 's')
    .replace(/\beast\b/g, 'e')
    .replace(/\bwest\b/g, 'w')
    .replace(/\.$/, '')
    // Degree, minute and second marks are separators, not data. So are the
    // hyphens in N42-15-30E and the commas some plats use.
    .replace(/[°*]/g, ' ')
    .replace(/["“”']/g, ' ')
    .replace(/[-–—,]/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  if (!text) return null;

  // ---- cardinal: "due north", "north", "n"
  const bare = text.replace(/^due\s+/, '').trim();
  if (CARDINAL[bare] !== undefined) {
    const az = CARDINAL[bare];
    return { azimuth: az, label: formatBearing(az) };
  }

  // ---- azimuth: an explicit prefix, or a number standing on its own
  const azMatch = /^(?:az|azimuth|bearing)\b(.*)$/.exec(text);
  const azBody = azMatch ? azMatch[1] : /^[\d.\s]+$/.test(text) ? text : null;
  if (azBody !== null) {
    const parts = (azBody.match(NUM) ?? []).map(Number);
    if (!parts.length) return null;
    const deg = dms(parts);
    if (deg === null || deg > 360) return null;
    const azimuth = normalizeAzimuth(deg);
    return { azimuth, label: formatAzimuth(azimuth) };
  }

  // ---- quadrant: a leading N or S, a trailing E or W, an angle between
  const q = /^([ns])\s*(.*?)\s*([ew])$/.exec(text);
  if (!q) return null;
  const parts = (q[2].match(NUM) ?? []).map(Number);
  if (!parts.length) return null;
  const angle = dms(parts);
  if (angle === null || angle > 90) return null;

  const north = q[1] === 'n';
  const east = q[3] === 'e';
  const azimuth = normalizeAzimuth(
    north ? (east ? angle : -angle) : east ? 180 - angle : 180 + angle
  );
  return { azimuth, label: formatBearing(azimuth) };
}

/** Decimal degrees as D°MM'SS", dropping empty minutes and seconds. */
function formatDms(deg: number): string {
  let d = Math.floor(deg + 1e-9);
  let rem = (deg - d) * 60;
  let m = Math.floor(rem + 1e-9);
  let s = Math.round((rem - m) * 60 * 100) / 100;
  if (s >= 60) {
    s -= 60;
    m += 1;
  }
  if (m >= 60) {
    m -= 60;
    d += 1;
  }
  if (m === 0 && s === 0) return `${d}°`;
  const mm = String(m).padStart(2, '0');
  if (s === 0) return `${d}°${mm}'`;
  const ss = (s < 10 ? '0' : '') + (Number.isInteger(s) ? s : s.toFixed(2));
  return `${d}°${mm}'${ss}"`;
}

/** Azimuth back to the quadrant form a deed prints. */
export function formatBearing(azimuth: number): string {
  const a = normalizeAzimuth(azimuth);
  // A quadrant bearing cannot express a cardinal direction without claiming a
  // quadrant it is not in, so the cardinals say so plainly.
  if (Math.abs(a) < 1e-9) return 'DUE N';
  if (Math.abs(a - 90) < 1e-9) return 'DUE E';
  if (Math.abs(a - 180) < 1e-9) return 'DUE S';
  if (Math.abs(a - 270) < 1e-9) return 'DUE W';
  if (a < 90) return `N ${formatDms(a)} E`;
  if (a < 180) return `S ${formatDms(180 - a)} E`;
  if (a < 270) return `S ${formatDms(a - 180)} W`;
  return `N ${formatDms(360 - a)} W`;
}

export function formatAzimuth(azimuth: number): string {
  return `AZ ${formatDms(normalizeAzimuth(azimuth))}`;
}

/** One step of the walk: where a call of this bearing and length lands. */
export function callVector(azimuth: number, distance: number): Pt {
  const a = (normalizeAzimuth(azimuth) * Math.PI) / 180;
  return { x: distance * Math.sin(a), y: -distance * Math.cos(a) };
}

export interface ResolvedCall {
  azimuth: number;
  distance: number;
}

/**
 * Walks the calls from `start`, returning the point of beginning followed by
 * one point per call — n calls give n+1 points. The last point is where the
 * deed's own arithmetic says the walk ended, which is not necessarily where
 * it started; see `closure`.
 */
export function traverse(start: Pt, calls: ResolvedCall[]): Pt[] {
  const pts: Pt[] = [{ ...start }];
  let cur = start;
  for (const c of calls) {
    const v = callVector(c.azimuth, c.distance);
    cur = { x: cur.x + v.x, y: cur.y + v.y };
    pts.push(cur);
  }
  return pts;
}

export interface Closure {
  /** How far the walk ended from where it began, feet. */
  feet: number;
  /** The gap as a vector, last point → point of beginning. */
  dx: number;
  dy: number;
  /** Sum of the call lengths, feet. */
  perimeter: number;
}

export function closure(pts: Pt[]): Closure {
  if (pts.length < 2) return { feet: 0, dx: 0, dy: 0, perimeter: 0 };
  const first = pts[0];
  const last = pts[pts.length - 1];
  let perimeter = 0;
  for (let i = 1; i < pts.length; i++) {
    perimeter += Math.hypot(pts[i].x - pts[i - 1].x, pts[i].y - pts[i - 1].y);
  }
  const dx = first.x - last.x;
  const dy = first.y - last.y;
  return { feet: Math.hypot(dx, dy), dx, dy, perimeter };
}

/**
 * Whether closing the gap is a correction rather than a demolition.
 *
 * A deed transcribed with a typo in one distance misses closure by a few
 * feet, and nudging the last corner fixes it. A deed whose final "thence to
 * the point of beginning" call was simply not typed misses by the length of
 * a whole side — and nudging the last corner there would collapse a real
 * corner onto the start and silently destroy the shape. So the offer is only
 * made when the gap is small against the perimeter.
 */
export function canCloseGap(pts: Pt[]): boolean {
  const c = closure(pts);
  if (c.feet < 1e-9) return false;
  return c.feet <= Math.max(3, c.perimeter * 0.02);
}

/** Moves the last point onto the point of beginning, so the walk closes exactly. */
export function closeGap(pts: Pt[]): Pt[] {
  if (pts.length < 2) return pts;
  const { dx, dy } = closure(pts);
  const out = pts.map((p) => ({ ...p }));
  const last = out[out.length - 1];
  out[out.length - 1] = { x: last.x + dx, y: last.y + dy };
  return out;
}

/**
 * The traverse as a lot ring: first point not repeated.
 *
 * A deed that includes its closing call ends on the point of beginning, and
 * that duplicate point is dropped. A deed that omits it — "thence to the
 * point of beginning" with no bearing given — ends on a real corner, which is
 * kept, and the ring closes with the straight line the deed implied.
 */
export function ringFromTraverse(pts: Pt[]): Pt[] {
  if (pts.length < 2) return pts;
  const first = pts[0];
  const last = pts[pts.length - 1];
  return Math.hypot(first.x - last.x, first.y - last.y) < 0.5
    ? pts.slice(0, -1)
    : pts;
}
