'use client';

/**
 * The SVG canvas: viewBox in world feet, zoom, pan, and every pointer
 * interaction.
 *
 * Pointer handlers live on the SVG ROOT rather than on each shape (§4.2).
 * A shape records which element was grabbed and the offset within it;
 * the root converts client coordinates to world coordinates and moves it.
 * `setPointerCapture` keeps the drag alive when the cursor leaves the shape,
 * and mouse, pen and touch all behave the same for free.
 */

import { useCallback, useEffect, useRef, useState } from 'react';
import s from '@/styles/SitePlanStudio.module.css';
import { clamp, lotBox, snapFoot } from '@/lib/siteplan/geometry';
import type { CheckResult, Plan } from '@/lib/siteplan/types';
import PlanScene from './PlanScene';

interface Props {
  plan: Plan;
  result: CheckResult;
  activeRowId: string | null;
  hoverElementId: string | null;
  onRowHover: (id: string | null) => void;
  onSelect: (id: string | null) => void;
  onMove: (id: string, x: number, y: number) => void;
  onRotate: (id: string, rot: number) => void;
  onNudge: (dx: number, dy: number) => void;
  onDelete: () => void;
  /** Polygon mode: clicking a boundary side marks it as the road frontage. */
  onSegmentClick?: (index: number) => void;
  /** False below 768px: numeric editing replaces dragging (§5). */
  draggable: boolean;
}

const MIN_ZOOM = 0.5;
const MAX_ZOOM = 4;

type Drag =
  | { kind: 'element'; id: string; offX: number; offY: number }
  | { kind: 'rotate'; id: string; cx: number; cy: number }
  | {
      kind: 'pan';
      startClientX: number;
      startClientY: number;
      cx: number;
      cy: number;
      pxPerWorld: number;
    }
  | null;

export default function PlanCanvas({
  plan,
  result,
  activeRowId,
  hoverElementId,
  onRowHover,
  onSelect,
  onMove,
  onRotate,
  onNudge,
  onDelete,
  onSegmentClick,
  draggable,
}: Props) {
  const svgRef = useRef<SVGSVGElement | null>(null);
  const wrapRef = useRef<HTMLDivElement | null>(null);
  const dragRef = useRef<Drag>(null);
  // A pan that travelled ends in a click on whatever was under the pointer.
  // Without this the frontage side under a dragged-across boundary would be
  // marked every time somebody panned the drawing.
  const pannedRef = useRef(false);
  const [zoom, setZoom] = useState(1);
  const [center, setCenter] = useState<{ x: number; y: number } | null>(null);
  const [box, setBox] = useState({ w: 800, h: 560 });

  const lot = plan.lot;

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

  // A new lot resets zoom and pan. That is done by REMOUNTING from the
  // parent (a key on the lot dimensions) rather than by an effect that
  // resets state, so there is no render where a 40 ft lot is showing a
  // 400 ft pan.

  const toWorld = useCallback((clientX: number, clientY: number) => {
    const svg = svgRef.current;
    if (!svg) return { x: 0, y: 0 };
    const ctm = svg.getScreenCTM();
    if (!ctm) return { x: 0, y: 0 };
    const pt = new DOMPoint(clientX, clientY).matrixTransform(ctm.inverse());
    return { x: pt.x, y: pt.y };
  }, []);

  if (!lot) return null;

  // Room OUTSIDE the property line for the lot dimension lines and their
  // labels, measured off the BOUNDING BOX so a notched parcel is framed by
  // what it actually spans. On a rectangle the framing is deliberately
  // asymmetric: both dimension lines run along the north and west edges, so
  // the default view is nudged south-east to give them the margin rather
  // than splitting it evenly and clipping the labels. A polygon labels every
  // side, so it is centerd and given the margin all round.
  const span = lotBox(lot);
  const fitW = span.w * 1.38;
  const fitH = span.d * 1.38;
  const vw = fitW / zoom;
  const vh = fitH / zoom;
  const bias = lot.kind === 'rect' ? 0.04 : 0;
  const cx = center?.x ?? span.cx + span.w * bias;
  const cy = center?.y ?? span.cy + span.d * bias;
  const viewBox = `${cx - vw / 2} ${cy - vh / 2} ${vw} ${vh}`;
  // preserveAspectRatio="meet" fits the viewBox inside the box, so the
  // effective scale is whichever axis is tighter.
  const pxPerWorld = Math.min(box.w / vw, box.h / vh);
  const u = pxPerWorld > 0 ? 1 / pxPerWorld : 1;
  // Constant-size labels swamp a small canvas — a 12px label on a 300px-wide
  // drawing is a quarter of the lot. Text shrinks with the box; symbols do not.
  const textScale = Math.max(0.62, Math.min(1, box.w / 620));
  // The canvas takes the lot's own proportions so a deep parcel is not
  // letterboxed into a strip down the middle of a landscape box. Clamped
  // either side so an extreme lot cannot make a canvas nobody can use.
  const aspect = Math.max(0.72, Math.min(1.9, span.w / span.d));

  const onElementPointerDown = (e: React.PointerEvent, id: string) => {
    if (!draggable) {
      onSelect(id);
      return;
    }
    e.stopPropagation();
    const el = plan.elements.find((x) => x.id === id);
    if (!el) return;
    const w = toWorld(e.clientX, e.clientY);
    dragRef.current = { kind: 'element', id, offX: w.x - el.x, offY: w.y - el.y };
    svgRef.current?.setPointerCapture(e.pointerId);
    onSelect(id);
  };

  const onRotateDown = (e: React.PointerEvent, id: string) => {
    e.stopPropagation();
    const el = plan.elements.find((x) => x.id === id);
    if (!el) return;
    dragRef.current = { kind: 'rotate', id, cx: el.x, cy: el.y };
    svgRef.current?.setPointerCapture(e.pointerId);
  };

  const onBackgroundPointerDown = (e: React.PointerEvent) => {
    onSelect(null);
    // Native text-selection during a fast drag paints ghost highlights.
    e.preventDefault();
    // Pan deltas are measured in SCREEN pixels against a scale frozen here.
    // Converting each move through the live CTM feeds the viewBox's own
    // motion back into the delta and the pan oscillates toward the pointer
    // instead of tracking it.
    pannedRef.current = false;
    dragRef.current = {
      kind: 'pan',
      startClientX: e.clientX,
      startClientY: e.clientY,
      cx,
      cy,
      pxPerWorld,
    };
    svgRef.current?.setPointerCapture(e.pointerId);
  };

  const onPointerMove = (e: React.PointerEvent) => {
    const drag = dragRef.current;
    if (!drag) return;
    const w = toWorld(e.clientX, e.clientY);

    if (drag.kind === 'element') {
      const free = e.altKey;
      onMove(
        drag.id,
        snapFoot(w.x - drag.offX, free),
        snapFoot(w.y - drag.offY, free)
      );
      return;
    }
    if (drag.kind === 'rotate') {
      const deg = (Math.atan2(w.y - drag.cy, w.x - drag.cx) * 180) / Math.PI + 90;
      const norm = ((deg % 360) + 360) % 360;
      onRotate(drag.id, e.altKey ? Math.round(norm) : Math.round(norm / 15) * 15);
      return;
    }
    // Pan: hold the world point that was grabbed under the pointer, using
    // the drag-start scale so the viewBox's motion never feeds back.
    if (
      Math.abs(e.clientX - drag.startClientX) > 4 ||
      Math.abs(e.clientY - drag.startClientY) > 4
    ) {
      pannedRef.current = true;
    }
    setCenter({
      x: drag.cx - (e.clientX - drag.startClientX) / drag.pxPerWorld,
      y: drag.cy - (e.clientY - drag.startClientY) / drag.pxPerWorld,
    });
  };

  const endDrag = (e: React.PointerEvent) => {
    if (!dragRef.current) return;
    dragRef.current = null;
    try {
      svgRef.current?.releasePointerCapture(e.pointerId);
    } catch {
      // The pointer was already released; nothing to undo.
    }
  };

  const onKeyDown = (e: React.KeyboardEvent) => {
    if (!plan.selectedId) return;
    const step = e.shiftKey ? 10 : 1;
    const map: Record<string, [number, number]> = {
      ArrowLeft: [-step, 0],
      ArrowRight: [step, 0],
      ArrowUp: [0, -step],
      ArrowDown: [0, step],
    };
    if (map[e.key]) {
      e.preventDefault();
      onNudge(map[e.key][0], map[e.key][1]);
      return;
    }
    if (e.key === 'Delete' || e.key === 'Backspace') {
      e.preventDefault();
      onDelete();
    }
  };

  return (
    <div className={s.canvasWrap}>
      <div
        className={s.canvasBox}
        ref={wrapRef}
        style={{ aspectRatio: `${aspect}` }}
      >
        <svg
          ref={svgRef}
          className={s.canvas}
          viewBox={viewBox}
          preserveAspectRatio="xMidYMid meet"
          role="application"
          aria-label="Site plan drawing"
          tabIndex={0}
          onKeyDown={onKeyDown}
          onPointerDown={onBackgroundPointerDown}
          onPointerMove={onPointerMove}
          onPointerUp={endDrag}
          onPointerCancel={endDrag}
        >
          <PlanScene
            plan={plan}
            result={result}
            u={u}
            textU={u * textScale}
            mode="screen"
            showSelectionDims={draggable}
            interactive
            selectedId={plan.selectedId}
            hoverElementId={hoverElementId}
            activeRowId={activeRowId}
            onElementPointerDown={onElementPointerDown}
            onRotateDown={draggable ? onRotateDown : undefined}
            onRowHover={onRowHover}
            onSegmentClick={
              onSegmentClick
                ? (i) => {
                    if (pannedRef.current) return;
                    onSegmentClick(i);
                  }
                : undefined
            }
          />
        </svg>
      </div>

      <div className={`${s.zoomBar} no-print`}>
        <button
          type="button"
          className={s.zoomBtn}
          onClick={() => setZoom((z) => clamp(Math.round((z - 0.25) * 100) / 100, MIN_ZOOM, MAX_ZOOM))}
          aria-label="Zoom out"
        >
          −
        </button>
        <input
          type="range"
          className={s.zoomRange}
          min={MIN_ZOOM}
          max={MAX_ZOOM}
          step={0.05}
          value={zoom}
          onChange={(e) => setZoom(Number(e.target.value))}
          aria-label="Zoom"
        />
        <button
          type="button"
          className={s.zoomBtn}
          onClick={() => setZoom((z) => clamp(Math.round((z + 0.25) * 100) / 100, MIN_ZOOM, MAX_ZOOM))}
          aria-label="Zoom in"
        >
          +
        </button>
        <button
          type="button"
          className={s.zoomFit}
          onClick={() => {
            setZoom(1);
            setCenter(null);
          }}
        >
          Fit
        </button>
        <span className={s.zoomPct}>{Math.round(zoom * 100)}%</span>
        <span className={s.zoomHint}>
          {draggable
            ? 'Drag to move · Alt for free placement · arrows nudge 1 ft'
            : 'Tap an element, then edit its position below'}
          {onSegmentClick ? ' · click a boundary side to mark the road' : ''}
        </span>
      </div>
    </div>
  );
}
