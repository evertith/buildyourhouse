'use client';

/**
 * Polygon lot entry (v1.5) — two ways in, one boundary out.
 *
 * DRAW IT. Click the corners in order, click the first corner again to close.
 * Then every corner is a handle: drag it, delete it, or add one at a side's
 * midpoint. Snapped to the foot.
 *
 * ENTER IT FROM YOUR DEED. Bearing and distance per row, exactly as the deed
 * prints them, walked turtle-style from the point of beginning. This is how
 * owners actually hold their boundary — the deed is in the drawer, the plat
 * is stapled to it, and no free tool reads either. The running closure error
 * is the thing a surveyor checks first, so it is on screen the whole time.
 *
 * The world window is FIXED at a chosen extent rather than fitted to the
 * points as they are placed. A view that refits itself between clicks moves
 * the ground under the cursor, and placing the fourth corner of a boundary
 * that just rescaled is guesswork.
 */

import { useEffect, useRef, useState } from 'react';
import s from '@/styles/SitePlanStudio.module.css';
import {
  canCloseGap,
  closeGap,
  closure,
  formatBearing,
  parseBearing,
  ringFromTraverse,
  traverse,
} from '@/lib/siteplan/bearing';
import {
  ensureClockwise,
  formatFeetShort,
  lotBox,
  polygonArea,
  selfIntersects,
  sideLengths,
} from '@/lib/siteplan/geometry';
import { polyError } from '@/lib/siteplan/defaults';
import type { Pt } from '@/lib/siteplan/types';

interface Props {
  /** The boundary being edited, or null when starting from nothing. */
  initial: Pt[] | null;
  onSubmit: (pts: Pt[]) => void;
  onCancel: () => void;
}

type Mode = 'draw' | 'deed';

interface CallRow {
  bearing: string;
  distance: string;
}

const EXTENTS = [200, 400, 800, 1600, 3200];
const BLANK_ROWS = 4;
const emptyRow = (): CallRow => ({ bearing: '', distance: '' });

/** Grid spacing in feet for a given world extent, so lines stay readable. */
function gridStep(extent: number): number {
  return extent / 8;
}

export default function LotShapeEditor({ initial, onSubmit, onCancel }: Props) {
  const [mode, setMode] = useState<Mode>('draw');
  const [pts, setPts] = useState<Pt[]>(initial ?? []);
  const [closed, setClosed] = useState<boolean>(!!initial && initial.length >= 3);
  const [rows, setRows] = useState<CallRow[]>(() =>
    Array.from({ length: BLANK_ROWS }, emptyRow)
  );
  const [gapClosed, setGapClosed] = useState(false);
  const [extent, setExtent] = useState(400);
  const [error, setError] = useState<string | null>(null);
  const [box, setBox] = useState({ w: 620, h: 620 });
  const [drawCenter] = useState<Pt>(() => {
    if (!initial?.length) return { x: 0, y: 0 };
    const b = lotBox({ kind: 'poly', pts: initial });
    return { x: b.cx, y: b.cy };
  });

  const svgRef = useRef<SVGSVGElement | null>(null);
  const wrapRef = useRef<HTMLDivElement | null>(null);
  const dragRef = useRef<{ index: number; moved: boolean } | null>(null);
  const downRef = useRef<{ cx: number; cy: number; world: Pt } | null>(null);

  useEffect(() => {
    const node = wrapRef.current;
    if (!node || typeof ResizeObserver === 'undefined') return;
    const ro = new ResizeObserver(([entry]) => {
      const r = entry.contentRect;
      if (r.width > 0 && r.height > 0) setBox({ w: r.width, h: r.height });
    });
    ro.observe(node);
    return () => ro.disconnect();
  }, []);

  // ---- The deed traverse, and the boundary it produces.
  const parsed = rows.map((r) => {
    const b = r.bearing.trim() ? parseBearing(r.bearing) : null;
    const dist = Number(r.distance);
    const ok = !!b && Number.isFinite(dist) && dist > 0;
    return { row: r, bearing: b, distance: dist, ok };
  });
  const calls = parsed
    .filter((p) => p.ok)
    .map((p) => ({ azimuth: p.bearing!.azimuth, distance: p.distance }));

  const walk = calls.length ? traverse({ x: 0, y: 0 }, calls) : [];
  const gap = walk.length ? closure(walk) : null;
  const deedRing =
    walk.length < 3 ? [] : ringFromTraverse(gapClosed ? closeGap(walk) : walk);

  // ---- Whichever mode is active supplies the shape everything else reads.
  const shape = mode === 'draw' ? pts : deedRing;
  const shapeClosed = mode === 'draw' ? closed : deedRing.length >= 3;
  const area = shape.length >= 3 ? polygonArea(shape) : 0;
  const crossing = shape.length >= 4 && selfIntersects(shape);
  const sides = shapeClosed ? sideLengths(shape) : [];

  // The view center is fixed for the whole session in draw mode. A window
  // that recenters itself between clicks moves the ground under the cursor,
  // and the fourth corner of a boundary that just shifted is guesswork. Deed
  // mode has no clicking to protect, so it frames what was typed.
  const viewCenter =
    mode === 'deed' && shape.length >= 2
      ? (() => {
          const b = lotBox({ kind: 'poly', pts: shape });
          return { x: b.cx, y: b.cy };
        })()
      : drawCenter;

  // The window has to hold whatever is being drawn; a deed for a 21-acre
  // strip is entered before anyone thinks about the extent control.
  const needed = shape.length
    ? Math.max(
        ...shape.map((p) =>
          Math.max(Math.abs(p.x - viewCenter.x), Math.abs(p.y - viewCenter.y))
        )
      ) * 2.2
    : 0;
  const view = Math.max(extent, EXTENTS.find((e) => e >= needed) ?? needed);
  const half = view / 2;
  const viewBox = `${viewCenter.x - half} ${viewCenter.y - half} ${view} ${view}`;
  const u = view / Math.max(1, Math.min(box.w, box.h));
  const step = gridStep(view);

  const toWorld = (clientX: number, clientY: number): Pt => {
    const svg = svgRef.current;
    if (!svg) return { x: 0, y: 0 };
    const ctm = svg.getScreenCTM();
    if (!ctm) return { x: 0, y: 0 };
    const p = new DOMPoint(clientX, clientY).matrixTransform(ctm.inverse());
    return { x: p.x, y: p.y };
  };

  const snap = (p: Pt): Pt => ({ x: Math.round(p.x), y: Math.round(p.y) });

  const hitVertex = (w: Pt): number => {
    // Kept clear of the delete cross, which sits 17u out on the same ray:
    // overlapping targets would delete corners people meant to drag.
    const r = 9 * u;
    for (let i = 0; i < pts.length; i++) {
      if (Math.hypot(pts[i].x - w.x, pts[i].y - w.y) <= r) return i;
    }
    return -1;
  };

  const hitDelete = (w: Pt): number => {
    if (!closed || pts.length <= 3) return -1;
    const r = 6.5 * u;
    for (let i = 0; i < pts.length; i++) {
      const c = deleteAt(pts, i, u);
      if (Math.hypot(c.x - w.x, c.y - w.y) <= r) return i;
    }
    return -1;
  };

  const hitMidpoint = (w: Pt): number => {
    if (!closed) return -1;
    const r = 9 * u;
    for (let i = 0; i < pts.length; i++) {
      const a = pts[i];
      const b = pts[(i + 1) % pts.length];
      const m = { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
      if (Math.hypot(m.x - w.x, m.y - w.y) <= r) return i;
    }
    return -1;
  };

  const onPointerDown = (e: React.PointerEvent) => {
    if (mode !== 'draw') return;
    e.preventDefault();
    const w = toWorld(e.clientX, e.clientY);

    const del = hitDelete(w);
    if (del >= 0) {
      setPts((ps) => ps.filter((_, i) => i !== del));
      return;
    }

    const v = hitVertex(w);
    if (v >= 0) {
      // Clicking the first corner is how a boundary closes.
      if (!closed && v === 0 && pts.length >= 3) {
        setClosed(true);
        return;
      }
      if (closed) {
        dragRef.current = { index: v, moved: false };
        svgRef.current?.setPointerCapture(e.pointerId);
        return;
      }
      // Mid-entry, on a corner that is not the first: swallow it rather than
      // stacking a second corner on top of one already placed.
      return;
    }

    const mid = hitMidpoint(w);
    if (mid >= 0) {
      const a = pts[mid];
      const b = pts[(mid + 1) % pts.length];
      const m = snap({ x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 });
      setPts((ps) => [...ps.slice(0, mid + 1), m, ...ps.slice(mid + 1)]);
      dragRef.current = { index: mid + 1, moved: false };
      svgRef.current?.setPointerCapture(e.pointerId);
      return;
    }

    downRef.current = { cx: e.clientX, cy: e.clientY, world: w };
  };

  const onPointerMove = (e: React.PointerEvent) => {
    const drag = dragRef.current;
    if (!drag) return;
    drag.moved = true;
    const w = snap(toWorld(e.clientX, e.clientY));
    setPts((ps) => ps.map((p, i) => (i === drag.index ? w : p)));
  };

  const onPointerUp = (e: React.PointerEvent) => {
    if (dragRef.current) {
      dragRef.current = null;
      try {
        svgRef.current?.releasePointerCapture(e.pointerId);
      } catch {
        // Already released.
      }
      return;
    }
    const down = downRef.current;
    downRef.current = null;
    if (!down || closed) return;
    // A click, not the tail of a drag.
    if (Math.hypot(e.clientX - down.cx, e.clientY - down.cy) > 4) return;
    setPts((ps) => [...ps, snap(down.world)]);
    setError(null);
  };

  const setRow = (i: number, patch: Partial<CallRow>) => {
    setRows((rs) => rs.map((r, j) => (j === i ? { ...r, ...patch } : r)));
    setGapClosed(false);
  };

  const submit = () => {
    const ring = ensureClockwise(shape);
    const err = polyError(ring);
    if (err) {
      setError(err);
      return;
    }
    // A boundary created from nothing is moved to the origin, so the drawing
    // sits in the same first-quadrant world every other plan uses. An EDIT
    // keeps its coordinates: shifting them would slide the lot out from under
    // the house, well and septic already placed on it.
    if (initial) {
      onSubmit(ring);
      return;
    }
    const b = lotBox({ kind: 'poly', pts: ring });
    onSubmit(ring.map((p) => ({ x: p.x - b.minX, y: p.y - b.minY })));
  };

  const useDeedCorners = () => {
    setPts(ensureClockwise(deedRing));
    setClosed(true);
    setMode('draw');
  };

  const canSubmit = shapeClosed && shape.length >= 3 && !polyError(shape);

  return (
    <div className={s.shapeEditor}>
      <div className={s.shapeTabs} role="tablist" aria-label="How to enter the boundary">
        <button
          type="button"
          role="tab"
          aria-selected={mode === 'draw'}
          className={`${s.shapeTab} ${mode === 'draw' ? s.shapeTabOn : ''}`}
          onClick={() => setMode('draw')}
        >
          Click the corners
        </button>
        <button
          type="button"
          role="tab"
          aria-selected={mode === 'deed'}
          className={`${s.shapeTab} ${mode === 'deed' ? s.shapeTabOn : ''}`}
          onClick={() => setMode('deed')}
        >
          Enter it from your deed
        </button>
      </div>

      <div className={s.shapeBody}>
        <div className={s.shapeCanvasCol}>
          <div className={s.shapeCanvasBox} ref={wrapRef}>
            <svg
              ref={svgRef}
              className={s.shapeCanvas}
              viewBox={viewBox}
              preserveAspectRatio="xMidYMid meet"
              role="application"
              aria-label="Lot boundary"
              data-testid="shape-canvas"
              onPointerDown={onPointerDown}
              onPointerMove={onPointerMove}
              onPointerUp={onPointerUp}
              onPointerCancel={onPointerUp}
            >
              <Grid center={viewCenter} view={view} step={step} u={u} />

              {shape.length > 0 && (
                <path
                  d={pathFor(shape, shapeClosed)}
                  fill={shapeClosed ? 'rgba(16, 44, 66, 0.05)' : 'none'}
                  stroke="var(--text-heading)"
                  strokeWidth={2.2}
                  strokeLinejoin="round"
                  vectorEffect="non-scaling-stroke"
                />
              )}

              {shapeClosed &&
                sides.map((len, i) => (
                  <SideLabel key={i} ring={shape} i={i} feet={len} u={u} />
                ))}

              {mode === 'draw' &&
                closed &&
                pts.map((p, i) => {
                  const b = pts[(i + 1) % pts.length];
                  const m = { x: (p.x + b.x) / 2, y: (p.y + b.y) / 2 };
                  return (
                    <g key={`mid-${i}`} pointerEvents="none">
                      <circle
                        cx={m.x}
                        cy={m.y}
                        r={5.5 * u}
                        fill="var(--bg-primary)"
                        stroke="var(--hairline-strong)"
                        strokeWidth={1}
                        vectorEffect="non-scaling-stroke"
                      />
                      <path
                        d={`M ${m.x - 2.6 * u} ${m.y} h ${5.2 * u} M ${m.x} ${m.y - 2.6 * u} v ${5.2 * u}`}
                        stroke="var(--text-secondary)"
                        strokeWidth={1.1}
                        vectorEffect="non-scaling-stroke"
                      />
                    </g>
                  );
                })}

              {mode === 'draw' &&
                pts.map((p, i) => (
                  <g key={`v-${i}`} pointerEvents="none">
                    <circle
                      cx={p.x}
                      cy={p.y}
                      r={(i === 0 && !closed ? 8 : 6) * u}
                      fill={i === 0 && !closed ? 'var(--accent-primary)' : 'var(--bg-primary)'}
                      stroke="var(--accent-primary)"
                      strokeWidth={1.6}
                      vectorEffect="non-scaling-stroke"
                    />
                    {closed && pts.length > 3 && (
                      <g>
                        <circle
                          cx={deleteAt(pts, i, u).x}
                          cy={deleteAt(pts, i, u).y}
                          r={6 * u}
                          fill="var(--bg-primary)"
                          stroke="var(--accent-critical)"
                          strokeWidth={1.2}
                          vectorEffect="non-scaling-stroke"
                        />
                        <path
                          d={`M ${deleteAt(pts, i, u).x - 2.2 * u} ${deleteAt(pts, i, u).y - 2.2 * u} l ${4.4 * u} ${4.4 * u} M ${deleteAt(pts, i, u).x + 2.2 * u} ${deleteAt(pts, i, u).y - 2.2 * u} l ${-4.4 * u} ${4.4 * u}`}
                          stroke="var(--accent-critical)"
                          strokeWidth={1.3}
                          vectorEffect="non-scaling-stroke"
                        />
                      </g>
                    )}
                  </g>
                ))}

              {/* The point of beginning, and where the walk actually ended. */}
              {mode === 'deed' && walk.length > 1 && gap && gap.feet > 0.05 && !gapClosed && (
                <g pointerEvents="none">
                  <line
                    x1={walk[walk.length - 1].x}
                    y1={walk[walk.length - 1].y}
                    x2={walk[0].x}
                    y2={walk[0].y}
                    stroke="var(--accent-critical)"
                    strokeWidth={1.4}
                    strokeDasharray="6 4"
                    vectorEffect="non-scaling-stroke"
                  />
                  <circle
                    cx={walk[walk.length - 1].x}
                    cy={walk[walk.length - 1].y}
                    r={5 * u}
                    fill="none"
                    stroke="var(--accent-critical)"
                    strokeWidth={1.4}
                    vectorEffect="non-scaling-stroke"
                  />
                </g>
              )}
            </svg>
          </div>

          <div className={s.shapeMeta}>
            <span className={s.shapeStat} data-testid="shape-corners">
              {shape.length} corners
            </span>
            {area > 0 && (
              <span className={s.shapeStat} data-testid="shape-area">
                {Math.round(area).toLocaleString()} sq ft · {(area / 43560).toFixed(2)} acres
              </span>
            )}
            <span className={s.shapeSpacer} />
            <label className={s.shapeExtent}>
              <span>View</span>
              <span className={s.selectBox}>
                <select
                  className={s.selectInput}
                  value={String(view)}
                  onChange={(e) => setExtent(Number(e.target.value))}
                >
                  {EXTENTS.map((e) => (
                    <option key={e} value={e}>
                      {e} ft
                    </option>
                  ))}
                </select>
              </span>
            </label>
          </div>

          {crossing && (
            <p className={s.shapeWarn} role="status">
              Boundary crosses itself — check your corners.
            </p>
          )}
        </div>

        <div className={s.shapeSideCol}>
          {mode === 'draw' ? (
            <div className={s.shapePanel}>
              <p className={s.railLabel}>Click the corners</p>
              <ol className={s.shapeSteps}>
                <li>
                  Click each corner of your lot in order, going round the
                  boundary one way.
                </li>
                <li>
                  Click the first corner again — the filled one — to close the
                  shape.
                </li>
                <li>
                  Then drag any corner to move it, click the <strong>+</strong>{' '}
                  on a side to add one, or the <strong>×</strong> to remove one.
                </li>
              </ol>
              <p className={s.railHint}>
                Corners snap to the foot. Exact numbers are easier off a deed —
                the other tab reads bearings and distances straight off it.
              </p>
              <div className={s.shapeBtnRow}>
                {!closed && pts.length >= 3 && (
                  <button
                    type="button"
                    className={s.ghostBtn}
                    onClick={() => setClosed(true)}
                  >
                    Close boundary
                  </button>
                )}
                {pts.length > 0 && (
                  <button
                    type="button"
                    className={s.ghostBtn}
                    onClick={() => {
                      setPts([]);
                      setClosed(false);
                      setError(null);
                    }}
                  >
                    Clear corners
                  </button>
                )}
              </div>
            </div>
          ) : (
            <div className={s.shapePanel}>
              <p className={s.railLabel}>Bearing and distance</p>
              <p className={s.railHint}>
                One row per call, in the order your deed lists them, starting
                at the point of beginning. Write the bearing however the deed
                writes it — <code>N 42°15&apos; E</code>, <code>N42-15-30E</code>,{' '}
                <code>S 7 W</code> or <code>azimuth 132.5</code> all read.
              </p>

              <div className={s.callTable}>
                <div className={s.callHead}>
                  <span>#</span>
                  <span>Bearing</span>
                  <span>Distance</span>
                  <span />
                </div>
                {rows.map((r, i) => {
                  const p = parsed[i];
                  const bad = r.bearing.trim() !== '' && !p.bearing;
                  return (
                    <div key={i} className={s.callRow}>
                      <span className={s.callNo}>{i + 1}</span>
                      <span className={`${s.callBox} ${bad ? s.callBoxBad : ''}`}>
                        <input
                          className={s.callInput}
                          type="text"
                          inputMode="text"
                          placeholder="N 42°15' E"
                          aria-label={`Call ${i + 1} bearing`}
                          data-testid={`call-bearing-${i}`}
                          value={r.bearing}
                          onChange={(e) => setRow(i, { bearing: e.target.value })}
                        />
                      </span>
                      <span className={s.callBox}>
                        <input
                          className={s.callInput}
                          type="number"
                          inputMode="decimal"
                          min={0}
                          step="0.01"
                          placeholder="150"
                          aria-label={`Call ${i + 1} distance in feet`}
                          data-testid={`call-distance-${i}`}
                          value={r.distance}
                          onChange={(e) => setRow(i, { distance: e.target.value })}
                        />
                        <span className={s.callUnit}>ft</span>
                      </span>
                      <button
                        type="button"
                        className={s.callDrop}
                        aria-label={`Remove call ${i + 1}`}
                        onClick={() =>
                          setRows((rs) =>
                            rs.length > 1 ? rs.filter((_, j) => j !== i) : [emptyRow()]
                          )
                        }
                      >
                        ×
                      </button>
                      <span className={s.callRead}>
                        {p.bearing
                          ? formatBearing(p.bearing.azimuth)
                          : bad
                            ? 'not read'
                            : ''}
                      </span>
                    </div>
                  );
                })}
              </div>

              <div className={s.shapeBtnRow}>
                <button
                  type="button"
                  className={s.ghostBtn}
                  onClick={() => setRows((rs) => [...rs, emptyRow()])}
                >
                  Add a call
                </button>
                {deedRing.length >= 3 && (
                  <button type="button" className={s.ghostBtn} onClick={useDeedCorners}>
                    Adjust corners by hand
                  </button>
                )}
              </div>

              {gap && calls.length >= 2 && (
                <div className={s.closureBox} data-testid="closure">
                  {gapClosed ? (
                    <>
                      <p className={s.closureOk}>
                        Gap closed — the last corner was moved onto the point of
                        beginning.
                      </p>
                      <button
                        type="button"
                        className={s.linkBtn}
                        onClick={() => setGapClosed(false)}
                      >
                        Undo
                      </button>
                    </>
                  ) : gap.feet < 0.05 ? (
                    <p className={s.closureOk}>
                      Boundary closes on the point of beginning.
                    </p>
                  ) : (
                    <>
                      <p className={s.closureBad}>
                        Boundary ends {formatFeetShort(gap.feet)} from where it
                        started.
                      </p>
                      {canCloseGap(walk) ? (
                        <button
                          type="button"
                          className={s.ghostBtn}
                          onClick={() => setGapClosed(true)}
                        >
                          Close the gap
                        </button>
                      ) : (
                        <p className={s.closureNote}>
                          That is most of a side — check for a call you have not
                          typed yet. Left as it is, the boundary closes with a
                          straight line back to the start.
                        </p>
                      )}
                    </>
                  )}
                </div>
              )}
            </div>
          )}
        </div>
      </div>

      {error && (
        <p className={s.fieldError} role="alert">
          {error}
        </p>
      )}

      <div className={s.shapeActions}>
        <button
          type="button"
          className={s.primaryBtn}
          onClick={submit}
          disabled={!canSubmit}
          data-testid="use-boundary"
        >
          Use this boundary
        </button>
        <button type="button" className={s.ghostBtn} onClick={onCancel}>
          Cancel
        </button>
      </div>
    </div>
  );
}

/** Where the little delete cross sits for corner `i` — outside the boundary. */
function deleteAt(pts: Pt[], i: number, u: number): Pt {
  const n = pts.length;
  const prev = pts[(i - 1 + n) % n];
  const next = pts[(i + 1) % n];
  const p = pts[i];
  // Away from both neighbors is away from the lot at a convex corner, and
  // is at least never on top of the boundary at a reflex one.
  const dx = 2 * p.x - prev.x - next.x;
  const dy = 2 * p.y - prev.y - next.y;
  const len = Math.hypot(dx, dy) || 1;
  return { x: p.x + (dx / len) * 17 * u, y: p.y + (dy / len) * 17 * u };
}

function pathFor(pts: Pt[], closed: boolean): string {
  if (!pts.length) return '';
  const d = pts.map((p, i) => `${i === 0 ? 'M' : 'L'} ${p.x} ${p.y}`).join(' ');
  return closed ? `${d} Z` : d;
}

function Grid({
  center,
  view,
  step,
  u,
}: {
  center: Pt;
  view: number;
  step: number;
  u: number;
}) {
  const half = view / 2;
  const x0 = Math.ceil((center.x - half) / step) * step;
  const y0 = Math.ceil((center.y - half) / step) * step;
  const lines: React.ReactElement[] = [];
  for (let v = y0; v <= center.y + half; v += step) {
    lines.push(
      <line
        key={`h${v}`}
        x1={center.x - half}
        y1={v}
        x2={center.x + half}
        y2={v}
        stroke="var(--hairline)"
        strokeWidth={1}
        vectorEffect="non-scaling-stroke"
      />
    );
  }
  for (let v = x0; v <= center.x + half; v += step) {
    lines.push(
      <line
        key={`v${v}`}
        x1={v}
        y1={center.y - half}
        x2={v}
        y2={center.y + half}
        stroke="var(--hairline)"
        strokeWidth={1}
        vectorEffect="non-scaling-stroke"
      />
    );
  }
  return (
    <g pointerEvents="none">
      <rect
        x={center.x - half}
        y={center.y - half}
        width={view}
        height={view}
        fill="var(--bg-secondary)"
      />
      {lines}
      <text
        x={center.x - half + 8 * u}
        y={center.y - half + 16 * u}
        fontFamily="var(--font-mono)"
        fontSize={11 * u}
        fill="var(--text-secondary)"
      >
        {Math.round(step)} ft grid
      </text>
    </g>
  );
}

/**
 * The side length, printed along its own side and outside the boundary —
 * the plat idiom. Text is flipped on sides running right-to-left so no label
 * prints upside down.
 */
function SideLabel({
  ring,
  i,
  feet,
  u,
}: {
  ring: Pt[];
  i: number;
  feet: number;
  u: number;
}) {
  const a = ring[i];
  const b = ring[(i + 1) % ring.length];
  const mid = { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
  const len = Math.hypot(b.x - a.x, b.y - a.y);
  if (len < 1e-6 || len / u < 26) return null;
  // The label always sits on the outward side of its own side; turning the
  // text by half a turn on right-to-left sides only stops it reading upside
  // down, and does not move it.
  const raw = (Math.atan2(b.y - a.y, b.x - a.x) * 180) / Math.PI;
  const deg = raw > 90 || raw < -90 ? raw + 180 : raw;
  const nx = (b.y - a.y) / len;
  const ny = -(b.x - a.x) / len;
  const off = 11 * u;
  return (
    <text
      x={mid.x + nx * off}
      y={mid.y + ny * off}
      transform={`rotate(${deg} ${mid.x + nx * off} ${mid.y + ny * off})`}
      textAnchor="middle"
      dominantBaseline="central"
      fontFamily="var(--font-mono)"
      fontSize={10.5 * u}
      fill="var(--text-secondary)"
      pointerEvents="none"
    >
      {formatFeetShort(feet)}
    </text>
  );
}
