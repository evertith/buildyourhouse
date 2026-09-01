/**
 * Site Plan Studio — versioned localStorage.
 *
 * The key carries the schema version, so a future shape change discards the
 * old plan rather than crashing on it. Hydration happens in an effect, never
 * during render (§4.4) — the page is statically exported and the first paint
 * has to match the server output or React tears the tree down.
 */

import { EMPTY_PLAN, type Lot, type Plan, type PlanElement, type Pt } from './types';
import { ELEMENT_KINDS } from './types';
import { bumpSeq } from './defaults';
import { ensureClockwise } from './geometry';

export const STORAGE_KEY = 'byh.siteplan.v2';

/**
 * v1 stored the lot as a bare `{ w, d }`. v1.5 made it a discriminated union,
 * so the key moved — and rather than discarding the plan the way a version
 * bump normally would, v1 is read once, converted to `{ kind: 'rect', … }`,
 * written under the new key and deleted. Somebody has a half-finished plot
 * plan in this browser and losing it to a refactor would be unforgivable.
 */
export const LEGACY_KEY = 'byh.siteplan.v1';

const num = (v: unknown, fallback: number): number =>
  typeof v === 'number' && Number.isFinite(v) ? v : fallback;

const str = (v: unknown, max = 120): string =>
  typeof v === 'string' ? v.slice(0, max) : '';

function parseElement(raw: unknown): PlanElement | null {
  if (!raw || typeof raw !== 'object') return null;
  const r = raw as Record<string, unknown>;
  if (typeof r.id !== 'string' || typeof r.kind !== 'string') return null;
  if (!ELEMENT_KINDS.includes(r.kind as PlanElement['kind'])) return null;
  return {
    id: r.id.slice(0, 40),
    kind: r.kind as PlanElement['kind'],
    x: num(r.x, 0),
    y: num(r.y, 0),
    w: num(r.w, 0),
    d: num(r.d, 0),
    rot: num(r.rot, 0),
  };
}

const nullableNum = (v: unknown): number | null =>
  typeof v === 'number' && Number.isFinite(v) ? v : null;

/**
 * Reads a stored lot in either schema.
 *
 * A v1 record has `{ w, d }` and no `kind`; a v2 record has `kind`. The
 * absent `kind` IS the version marker, so no separate migration flag has to
 * be kept in sync with the data.
 */
function parseLot(raw: unknown): Lot | null {
  if (!raw || typeof raw !== 'object') return null;
  const r = raw as Record<string, unknown>;

  if (r.kind === 'poly') {
    if (!Array.isArray(r.pts)) return null;
    const pts: Pt[] = [];
    for (const q of r.pts.slice(0, 200)) {
      if (!q || typeof q !== 'object') return null;
      const o = q as Record<string, unknown>;
      if (typeof o.x !== 'number' || typeof o.y !== 'number') return null;
      if (!Number.isFinite(o.x) || !Number.isFinite(o.y)) return null;
      pts.push({ x: o.x, y: o.y });
    }
    if (pts.length < 3) return null;
    return { kind: 'poly', pts: ensureClockwise(pts) };
  }

  // v1's shape, and v2's rectangle: the same two numbers either way.
  const w = num(r.w, 0);
  const d = num(r.d, 0);
  if (w <= 0 || d <= 0) return null;
  return { kind: 'rect', w, d };
}

/** Returns null when there is nothing valid to restore. */
export function loadPlan(): Plan | null {
  if (typeof window === 'undefined') return null;
  let raw: string | null = null;
  let migrated = false;
  try {
    raw = window.localStorage.getItem(STORAGE_KEY);
    if (!raw) {
      raw = window.localStorage.getItem(LEGACY_KEY);
      migrated = raw !== null;
    }
  } catch {
    return null; // Private mode, or storage disabled.
  }
  if (!raw) return null;
  try {
    const p = JSON.parse(raw) as Record<string, unknown>;
    const lot = parseLot(p.lot);
    if (!lot) return null;

    const elements = Array.isArray(p.elements)
      ? (p.elements.map(parseElement).filter(Boolean) as PlanElement[])
      : [];
    // Keep generated ids from colliding with restored ones.
    bumpSeq(elements.length + 1);

    const sb = (p.setbacks ?? {}) as Record<string, unknown>;
    const t = (p.title ?? {}) as Record<string, unknown>;
    const front = str(p.frontEdge, 8);
    const seg = p.frontSegment;
    const frontSegment =
      lot.kind === 'poly' &&
      typeof seg === 'number' &&
      Number.isInteger(seg) &&
      seg >= 0 &&
      seg < lot.pts.length
        ? seg
        : null;

    const plan: Plan = {
      ...EMPTY_PLAN,
      lot,
      stateCode: str(p.stateCode, 4).toLowerCase(),
      elements,
      selectedId: null,
      setbacks: {
        front: nullableNum(sb.front),
        side: nullableNum(sb.side),
        rear: nullableNum(sb.rear),
      },
      frontEdge:
        front === 'north' || front === 'east' || front === 'south' || front === 'west'
          ? front
          : 'north',
      frontSegment,
      north: num(p.north, 0),
      title: {
        project: str(t.project),
        owner: str(t.owner),
        address: str(t.address),
        parcel: str(t.parcel),
        irregular: str(t.irregular, 240),
      },
    };

    // Rewrite under the new key and drop the old one, so the conversion runs
    // once rather than on every load for the rest of this browser's life.
    if (migrated) {
      savePlan(plan);
      try {
        window.localStorage.removeItem(LEGACY_KEY);
      } catch {
        // The plan is already safe under the new key.
      }
    }
    return plan;
  } catch {
    return null;
  }
}

export function savePlan(plan: Plan): void {
  if (typeof window === 'undefined') return;
  try {
    // selectedId is view state, not document state — it does not persist.
    const { selectedId: _drop, ...doc } = plan;
    void _drop;
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(doc));
  } catch {
    // Quota or private mode. The tool still works; it just will not resume.
  }
}

export function clearPlan(): void {
  if (typeof window === 'undefined') return;
  try {
    window.localStorage.removeItem(STORAGE_KEY);
    // A v1 record that has never been loaded is still sitting there; "start
    // over" has to mean it, or the next visit resurrects the old plan.
    window.localStorage.removeItem(LEGACY_KEY);
  } catch {
    // Nothing to do.
  }
}
