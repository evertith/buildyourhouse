/**
 * Site Plan Studio — versioned localStorage.
 *
 * The key carries the schema version, so a future shape change discards the
 * old plan rather than crashing on it. Hydration happens in an effect, never
 * during render (§4.4) — the page is statically exported and the first paint
 * has to match the server output or React tears the tree down.
 */

import { EMPTY_PLAN, type Plan, type PlanElement } from './types';
import { ELEMENT_KINDS } from './types';
import { bumpSeq } from './defaults';

export const STORAGE_KEY = 'byh.siteplan.v1';

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

/** Returns null when there is nothing valid to restore. */
export function loadPlan(): Plan | null {
  if (typeof window === 'undefined') return null;
  let raw: string | null = null;
  try {
    raw = window.localStorage.getItem(STORAGE_KEY);
  } catch {
    return null; // Private mode, or storage disabled.
  }
  if (!raw) return null;
  try {
    const p = JSON.parse(raw) as Record<string, unknown>;
    const lotRaw = p.lot as Record<string, unknown> | null | undefined;
    const lot =
      lotRaw && typeof lotRaw === 'object'
        ? { w: num(lotRaw.w, 0), d: num(lotRaw.d, 0) }
        : null;
    if (!lot || lot.w <= 0 || lot.d <= 0) return null;

    const elements = Array.isArray(p.elements)
      ? (p.elements.map(parseElement).filter(Boolean) as PlanElement[])
      : [];
    // Keep generated ids from colliding with restored ones.
    bumpSeq(elements.length + 1);

    const sb = (p.setbacks ?? {}) as Record<string, unknown>;
    const t = (p.title ?? {}) as Record<string, unknown>;
    const front = str(p.frontEdge, 8);

    return {
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
      north: num(p.north, 0),
      title: {
        project: str(t.project),
        owner: str(t.owner),
        address: str(t.address),
        parcel: str(t.parcel),
        irregular: str(t.irregular, 240),
      },
    };
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
  } catch {
    // Nothing to do.
  }
}
