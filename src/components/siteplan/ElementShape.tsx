/**
 * One placed element, drawn in the sheet's symbol vocabulary (§3.2) — the
 * same symbols on screen and on paper, so the printed legend teaches the
 * editor rather than describing a second drawing.
 *
 *   house       heavy solid outline
 *   structure   medium solid
 *   well        circle with cross-hairs
 *   septic tank double-line rectangle
 *   drainfield  rectangle with dashed laterals
 *   driveway    two parallel lines with stipple
 *   water edge  solid blue-grey line with wave ticks
 *
 * Symbols that represent a point or a line (well, water edge) are sized in
 * CSS pixels via `u`, not in feet: at 1" = 100' a 1 ft circle is a hundredth
 * of an inch and invisible. That is also why distances are measured from the
 * well's center — there is no world-space radius to subtract, so the number
 * on the sheet is the number a ruler on the sheet gives back.
 */

import { corners } from '@/lib/siteplan/geometry';
import type { PlanElement } from '@/lib/siteplan/types';
import { KIND_LABEL } from '@/lib/siteplan/types';

interface Props {
  el: PlanElement;
  selected?: boolean;
  hovered?: boolean;
  /** World units per CSS pixel. */
  u: number;
  /** World units per text pixel. Defaults to `u`. */
  tu?: number;
  mode: 'screen' | 'sheet';
  onPointerDown?: (e: React.PointerEvent, id: string) => void;
  onRotateDown?: (e: React.PointerEvent, id: string) => void;
  interactive?: boolean;
}

const INK = 'var(--text-heading)';
const WATER = '#4a6b80';

export default function ElementShape({
  el,
  selected,
  hovered,
  u,
  tu,
  mode,
  onPointerDown,
  onRotateDown,
  interactive,
}: Props) {
  const x = el.x - el.w / 2;
  const y = el.y - el.d / 2;
  const spin = `rotate(${el.rot} ${el.x} ${el.y})`;
  const t = tu ?? u;
  const wPx = el.w / u;
  const dPx = el.d / u;
  const showLabel = mode === 'sheet' ? wPx > 46 && dPx > 22 : wPx > 54 && dPx > 26;
  const fs = 9.5 * t;
  const name = KIND_LABEL[el.kind].toUpperCase();

  const grab = onPointerDown
    ? (e: React.PointerEvent) => onPointerDown(e, el.id)
    : undefined;

  const body = (() => {
    switch (el.kind) {
      case 'well':
        return <Well el={el} u={u} />;
      case 'waterEdge':
        return <WaterEdge el={el} u={u} />;
      case 'septicTank':
        return (
          <>
            <rect
              x={x}
              y={y}
              width={el.w}
              height={el.d}
              fill="var(--bg-primary)"
              stroke={INK}
              strokeWidth={1.4}
              vectorEffect="non-scaling-stroke"
            />
            <rect
              x={x + 1.2 * u}
              y={y + 1.2 * u}
              width={Math.max(0, el.w - 2.4 * u)}
              height={Math.max(0, el.d - 2.4 * u)}
              fill="none"
              stroke={INK}
              strokeWidth={1}
              vectorEffect="non-scaling-stroke"
            />
          </>
        );
      case 'drainfield':
        return <Drainfield el={el} />;
      case 'driveway':
        return <Driveway el={el} u={u} />;
      case 'structure':
        return (
          <rect
            x={x}
            y={y}
            width={el.w}
            height={el.d}
            fill="rgba(16, 44, 66, 0.045)"
            stroke={INK}
            strokeWidth={1.3}
            vectorEffect="non-scaling-stroke"
          />
        );
      default:
        return (
          <rect
            x={x}
            y={y}
            width={el.w}
            height={el.d}
            fill="rgba(16, 44, 66, 0.07)"
            stroke={INK}
            strokeWidth={2.1}
            vectorEffect="non-scaling-stroke"
          />
        );
    }
  })();

  // Point and line elements need a fat invisible target; rectangles are
  // their own target once they carry a fill.
  const hit =
    el.kind === 'well' ? (
      <circle cx={el.x} cy={el.y} r={11 * u} fill="transparent" />
    ) : el.kind === 'waterEdge' ? (
      <rect
        x={x}
        y={el.y - 8 * u}
        width={el.w}
        height={16 * u}
        fill="transparent"
      />
    ) : null;

  return (
    <g
      transform={spin}
      onPointerDown={interactive ? grab : undefined}
      style={interactive ? { cursor: 'move', touchAction: 'none' } : undefined}
      role={interactive ? 'button' : undefined}
      tabIndex={interactive ? 0 : undefined}
      aria-label={
        interactive
          ? `${KIND_LABEL[el.kind]}, ${Math.round(el.x)} feet east and ${Math.round(
              el.y
            )} feet south of the north-west corner`
          : undefined
      }
    >
      {body}
      {hit}
      {showLabel && (
        /* On a plate: the drainfield's dashed laterals and the driveway's
           stipple run straight through unplated text and make it unreadable. */
        <g
          pointerEvents="none"
          transform={`rotate(${-el.rot} ${el.x} ${el.y})`}
        >
          <rect
            x={el.x - (name.length * fs * 0.68) / 2 - 2 * t}
            y={el.y - fs * 0.78}
            width={name.length * fs * 0.68 + 4 * t}
            height={fs * 1.56}
            fill="var(--bg-primary)"
          />
          <text
            x={el.x}
            y={el.y}
            textAnchor="middle"
            dominantBaseline="central"
            fontFamily="var(--font-mono)"
            fontSize={fs}
            letterSpacing={0.08 * fs}
            fill="var(--text-secondary)"
          >
            {name}
          </text>
        </g>
      )}
      {el.kind === 'well' && mode === 'sheet' && (
        <text
          x={el.x + 13 * t}
          y={el.y}
          dominantBaseline="central"
          fontFamily="var(--font-mono)"
          fontSize={fs}
          letterSpacing={0.08 * fs}
          fill="var(--text-secondary)"
          pointerEvents="none"
        >
          WELL
        </text>
      )}
      {selected && mode === 'screen' && (
        <Selection el={el} u={u} onRotateDown={onRotateDown} />
      )}
      {hovered && !selected && mode === 'screen' && (
        <rect
          x={x - 2 * u}
          y={y - 2 * u}
          width={el.w + 4 * u}
          height={el.d + 4 * u}
          fill="none"
          stroke="var(--accent-primary)"
          strokeWidth={1}
          strokeOpacity={0.55}
          vectorEffect="non-scaling-stroke"
          pointerEvents="none"
        />
      )}
    </g>
  );
}

function Well({ el, u }: { el: PlanElement; u: number }) {
  const r = 6.5 * u;
  const arm = 10 * u;
  return (
    <>
      <circle
        cx={el.x}
        cy={el.y}
        r={r}
        fill="var(--bg-primary)"
        stroke={INK}
        strokeWidth={1.5}
        vectorEffect="non-scaling-stroke"
      />
      <line
        x1={el.x - arm}
        y1={el.y}
        x2={el.x + arm}
        y2={el.y}
        stroke={INK}
        strokeWidth={1.1}
        vectorEffect="non-scaling-stroke"
      />
      <line
        x1={el.x}
        y1={el.y - arm}
        x2={el.x}
        y2={el.y + arm}
        stroke={INK}
        strokeWidth={1.1}
        vectorEffect="non-scaling-stroke"
      />
    </>
  );
}

/** Ticks alternate sides of the line, the map convention for a bank. */
function WaterEdge({ el, u }: { el: PlanElement; u: number }) {
  const half = el.w / 2;
  const step = Math.max(el.w / 9, 8 * u);
  const ticks: React.ReactElement[] = [];
  for (let t = -half + step / 2, i = 0; t < half; t += step, i++) {
    ticks.push(
      <path
        key={i}
        d={`M ${el.x + t} ${el.y} q ${step * 0.25} ${-4 * u} ${step * 0.5} 0`}
        fill="none"
        stroke={WATER}
        strokeWidth={1}
        vectorEffect="non-scaling-stroke"
      />
    );
  }
  return (
    <>
      <line
        x1={el.x - half}
        y1={el.y}
        x2={el.x + half}
        y2={el.y}
        stroke={WATER}
        strokeWidth={2}
        vectorEffect="non-scaling-stroke"
      />
      {ticks}
    </>
  );
}

function Drainfield({ el }: { el: PlanElement }) {
  const x = el.x - el.w / 2;
  const y = el.y - el.d / 2;
  const laterals = 4;
  const gap = el.d / (laterals + 1);
  return (
    <>
      <rect
        x={x}
        y={y}
        width={el.w}
        height={el.d}
        fill="var(--bg-primary)"
        stroke={INK}
        strokeWidth={1.3}
        vectorEffect="non-scaling-stroke"
      />
      {Array.from({ length: laterals }, (_, i) => (
        <line
          key={i}
          x1={x + el.w * 0.05}
          y1={y + gap * (i + 1)}
          x2={x + el.w * 0.95}
          y2={y + gap * (i + 1)}
          stroke={INK}
          strokeWidth={1}
          strokeDasharray="6 4"
          strokeOpacity={0.75}
          vectorEffect="non-scaling-stroke"
        />
      ))}
    </>
  );
}

/** Two parallel lines with stipple — no end caps, so it reads as a run. */
function Driveway({ el, u }: { el: PlanElement; u: number }) {
  const x = el.x - el.w / 2;
  const y = el.y - el.d / 2;
  const dots: React.ReactElement[] = [];
  const stepY = Math.max(el.d / 12, 7 * u);
  const stepX = Math.max(el.w / 3, 5 * u);
  for (let dy = stepY / 2; dy < el.d; dy += stepY) {
    for (let dx = stepX / 2; dx < el.w; dx += stepX) {
      dots.push(
        <circle
          key={`${dx}-${dy}`}
          cx={x + dx}
          cy={y + dy}
          r={0.9 * u}
          fill="var(--text-secondary)"
          fillOpacity={0.5}
        />
      );
    }
  }
  return (
    <>
      <rect x={x} y={y} width={el.w} height={el.d} fill="rgba(35, 32, 25, 0.03)" />
      <line
        x1={x}
        y1={y}
        x2={x}
        y2={y + el.d}
        stroke={INK}
        strokeWidth={1.2}
        vectorEffect="non-scaling-stroke"
      />
      <line
        x1={x + el.w}
        y1={y}
        x2={x + el.w}
        y2={y + el.d}
        stroke={INK}
        strokeWidth={1.2}
        vectorEffect="non-scaling-stroke"
      />
      {dots}
    </>
  );
}

function Selection({
  el,
  u,
  onRotateDown,
}: {
  el: PlanElement;
  u: number;
  onRotateDown?: (e: React.PointerEvent, id: string) => void;
}) {
  const pad = 3 * u;
  const x = el.x - el.w / 2 - pad;
  const y = el.y - el.d / 2 - pad;
  const w = el.w + pad * 2;
  const h = el.d + pad * 2;
  const handle = 3.5 * u;
  const pts = corners({ ...el, rot: 0, w: el.w + pad * 2, d: el.d + pad * 2 });
  return (
    <g pointerEvents="none">
      <rect
        x={x}
        y={y}
        width={w}
        height={h}
        fill="none"
        stroke="var(--accent-primary)"
        strokeWidth={1.25}
        strokeDasharray="4 3"
        vectorEffect="non-scaling-stroke"
      />
      {pts.map((p, i) => (
        <rect
          key={i}
          x={p.x - handle}
          y={p.y - handle}
          width={handle * 2}
          height={handle * 2}
          fill="var(--bg-primary)"
          stroke="var(--accent-primary)"
          strokeWidth={1.25}
          vectorEffect="non-scaling-stroke"
        />
      ))}
      {onRotateDown && (
        <g
          pointerEvents="auto"
          style={{ cursor: 'grab', touchAction: 'none' }}
          onPointerDown={(e) => onRotateDown(e, el.id)}
        >
          <line
            x1={x + w}
            y1={y}
            x2={x + w + 14 * u}
            y2={y - 14 * u}
            stroke="var(--accent-primary)"
            strokeWidth={1.1}
            vectorEffect="non-scaling-stroke"
          />
          <circle
            cx={x + w + 14 * u}
            cy={y - 14 * u}
            r={6 * u}
            fill="var(--bg-primary)"
            stroke="var(--accent-primary)"
            strokeWidth={1.4}
            vectorEffect="non-scaling-stroke"
          />
          <path
            d={`M ${x + w + 11 * u} ${y - 14 * u} a ${3 * u} ${3 * u} 0 1 1 ${1.6 * u} ${2.2 * u}`}
            fill="none"
            stroke="var(--accent-primary)"
            strokeWidth={1.1}
            vectorEffect="non-scaling-stroke"
          />
        </g>
      )}
    </g>
  );
}
