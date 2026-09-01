/**
 * The drawing itself — property line, setbacks, elements, dimensions.
 *
 * One component renders both the editor canvas and the printed sheet. That
 * is deliberate: what is seen is what prints, down to the tick marks, and a
 * symbol can never drift between the two. The only differences are the
 * `mode` flag (interaction and hover chrome are screen-only) and the
 * viewBox the caller sets.
 *
 * v1.5: the boundary is a rectangle or a polygon. A polygon carries its
 * length on EVERY side — the plat idiom, and the thing that makes an
 * owner-drawn sheet read as a real plot plan rather than a sketch — in place
 * of the two dimension lines a rectangle gets on its north and west edges.
 */

import {
  closestPoints,
  edgeDimension,
  formatFeet,
  formatFeetShort,
  lotRing,
  nearestBoundary,
  sideLengths,
  type Pt,
} from '@/lib/siteplan/geometry';
import { geometryRows, liveRows } from '@/lib/siteplan/check';
import type {
  CheckResult,
  EdgeName,
  Lot,
  Plan,
  PlanElement,
  RectLot,
} from '@/lib/siteplan/types';
import ElementShape from './ElementShape';
import DimensionLine, { type DimTone } from './DimensionLine';

interface Props {
  plan: Plan;
  result: CheckResult;
  /** World units per CSS pixel — sizes every symbol and label. */
  u: number;
  /** World units per text pixel. Defaults to `u`; a narrow canvas passes a
      smaller value so labels stay proportionate to the drawing. */
  textU?: number;
  /** Below the drag breakpoint the inspector lists the property-line
      distances numerically, so drawing them too only clutters a small canvas. */
  showSelectionDims?: boolean;
  mode: 'screen' | 'sheet';
  selectedId?: string | null;
  hoverElementId?: string | null;
  /** Row id hovered in the inspector; its dimension line goes accent (§2.3). */
  activeRowId?: string | null;
  interactive?: boolean;
  onElementPointerDown?: (e: React.PointerEvent, id: string) => void;
  onRotateDown?: (e: React.PointerEvent, id: string) => void;
  onRowHover?: (id: string | null) => void;
  /** Polygon mode: clicking a boundary side marks it as the road frontage. */
  onSegmentClick?: (index: number) => void;
}

interface Dim {
  key: string;
  a: Pt;
  b: Pt;
  label: string;
  tone: DimTone;
  dashed?: boolean;
  shift?: number;
  rowId?: string;
}

const OPPOSITE: Record<EdgeName, EdgeName> = {
  north: 'south',
  south: 'north',
  east: 'west',
  west: 'east',
};

export default function PlanScene({
  plan,
  result,
  u,
  textU,
  mode,
  showSelectionDims = true,
  selectedId,
  hoverElementId,
  activeRowId,
  interactive,
  onElementPointerDown,
  onRotateDown,
  onRowHover,
  onSegmentClick,
}: Props) {
  const lot = plan.lot;
  if (!lot) return null;

  const tu = textU ?? u;
  const byId = new Map(plan.elements.map((e) => [e.id, e]));
  const ring = lotRing(lot);
  const dims: Dim[] = [];

  // ---- Lot dimensions. A rectangle takes its two dimension lines on the
  // north and west edges (§2.2 step 2); a polygon takes a length on every
  // side instead, drawn below by SideLabels.
  if (lot.kind === 'rect') {
    const off = 20 * u;
    dims.push({
      key: 'lot-w',
      a: { x: 0, y: -off },
      b: { x: lot.w, y: -off },
      label: formatFeet(lot.w),
      tone: 'normal',
    });
    dims.push({
      key: 'lot-d',
      a: { x: -off, y: 0 },
      b: { x: -off, y: lot.d },
      label: formatFeet(lot.d),
      tone: 'normal',
    });
  }

  // ---- Every rule measuring under 1.5x its minimum, selection-independent
  const live = liveRows(result);
  live.forEach((row, i) => {
    const dim = dimForRow(row.fromId, row.toId, row.edge, row.boundary, byId, lot);
    if (!dim) return;
    const short = row.status === 'violation' || row.status === 'watch';
    const req = row.requiredFeet;
    const suffix =
      short && req !== null
        ? row.hedged
          ? ` (${req}' typical)`
          : ` (${req}' req.)`
        : '';
    dims.push({
      key: `row-${row.id}`,
      rowId: row.id,
      a: dim[0],
      b: dim[1],
      label: `${formatFeet(row.measuredFeet ?? 0)}${suffix}`,
      tone:
        activeRowId === row.id
          ? 'active'
          : row.status === 'violation'
            ? 'violation'
            : row.status === 'watch'
              ? 'watch'
              : 'normal',
      dashed: row.hedged,
      // Alternate above and below the midpoint: these lines often converge
      // on the same well, and stacked labels hide each other.
      shift: [0, -0.16, 0.16, -0.3, 0.3][i % 5],
    });
  });

  // ---- The sheet always carries the classic plot-plan set: dwelling to the
  // property lines, well↔septic pairs, septic↔dwelling — measured, no
  // requirement, whatever the state publishes. Rule rows already drawn win.
  if (mode === 'sheet') {
    geometryRows(plan, result.rows).forEach((row, i) => {
      const dim = dimForRow(row.fromId, row.toId, row.edge, row.boundary, byId, lot);
      if (!dim) return;
      dims.push({
        key: `geo-${row.id}`,
        a: dim[0],
        b: dim[1],
        label: formatFeet(row.measuredFeet ?? 0),
        tone: 'normal',
        shift: [0, -0.16, 0.16, -0.3, 0.3][(live.length + i) % 5],
      });
    });
  }

  // ---- The selected element's distance to the property line. Four named
  // distances on a rectangle; one, to the nearest side, on a polygon —
  // because "north line" means nothing on an eight-sided boundary and
  // "side 6" would mean less.
  const sel = selectedId ? byId.get(selectedId) : null;
  if (sel && mode === 'screen' && showSelectionDims) {
    if (lot.kind === 'rect') {
      (['north', 'east', 'south', 'west'] as EdgeName[]).forEach((edge) => {
        const [a, b] = edgeDimension(sel, lot, edge);
        const feet = Math.hypot(b.x - a.x, b.y - a.y);
        const outside =
          (edge === 'north' && a.y < 0) ||
          (edge === 'south' && a.y > lot.d) ||
          (edge === 'west' && a.x < 0) ||
          (edge === 'east' && a.x > lot.w);
        dims.push({
          key: `sel-${edge}`,
          a,
          b,
          label: formatFeet(feet),
          tone: outside ? 'violation' : 'normal',
        });
      });
    } else {
      const n = nearestBoundary(sel, lot);
      dims.push({
        key: 'sel-boundary',
        a: n.a,
        b: n.b,
        label: formatFeet(Math.abs(n.feet)),
        tone: n.feet < 0 ? 'violation' : 'normal',
      });
    }
  }

  // ---- The selected element's distances to its related elements, so the
  // well↔septic line is live under the cursor while dragging — whatever the
  // state's rules say. Pairs the rule engine already draws are skipped.
  if (sel && mode === 'screen' && showSelectionDims) {
    const RELATED: Partial<Record<PlanElement['kind'], PlanElement['kind'][]>> = {
      well: ['septicTank', 'drainfield', 'house'],
      septicTank: ['well', 'house'],
      drainfield: ['well', 'house'],
      house: ['well', 'septicTank', 'drainfield'],
    };
    const kinds = RELATED[sel.kind] ?? [];
    const drawnPairs = new Set(
      live
        .filter((r) => r.fromId && r.toId)
        .map((r) => [r.fromId, r.toId].sort().join(':'))
    );
    plan.elements
      .filter((e) => e.id !== sel.id && kinds.includes(e.kind))
      .forEach((other, j) => {
        if (drawnPairs.has([sel.id, other.id].sort().join(':'))) return;
        const [a, b] = closestPoints(sel, other);
        const feet = Math.hypot(b.x - a.x, b.y - a.y);
        dims.push({
          key: `rel-${other.id}`,
          a,
          b,
          label: formatFeet(feet),
          tone: 'normal',
          shift: [0, -0.16, 0.16][j % 3],
        });
      });
  }

  // ---- Setback crossings the OWNER entered — their own visual language.
  // Rectangles only; `check` produces none for a polygon.
  if (lot.kind === 'rect') {
    for (const w of result.setbacks) {
      const el = byId.get(w.elementId);
      if (!el) continue;
      const [a, b] = edgeDimension(el, lot, w.edge);
      dims.push({
        key: `sb-${w.id}`,
        a,
        b,
        label: `${formatFeet(w.measuredFeet)} (${w.requiredFeet}' setback)`,
        tone: 'setback',
        dashed: true,
      });
    }
  }

  return (
    <>
      {/* Property line: solid heavy, the drawing's outer boundary. */}
      {lot.kind === 'rect' ? (
        <rect
          x={0}
          y={0}
          width={lot.w}
          height={lot.d}
          fill="none"
          stroke="var(--text-heading)"
          strokeWidth={2.4}
          vectorEffect="non-scaling-stroke"
        />
      ) : (
        <path
          d={`${ring.map((p, i) => `${i === 0 ? 'M' : 'L'} ${p.x} ${p.y}`).join(' ')} Z`}
          fill="none"
          stroke="var(--text-heading)"
          strokeWidth={2.4}
          strokeLinejoin="round"
          vectorEffect="non-scaling-stroke"
        />
      )}

      {lot.kind === 'poly' && (
        <Frontage ring={ring} index={plan.frontSegment} u={u} tu={tu} />
      )}

      {lot.kind === 'rect' && <Setbacks lot={lot} plan={plan} />}

      {lot.kind === 'poly' && <SideLabels ring={ring} u={u} tu={tu} />}

      {plan.elements.map((el) => (
        <ElementShape
          key={el.id}
          el={el}
          u={u}
          tu={tu}
          mode={mode}
          selected={selectedId === el.id}
          hovered={hoverElementId === el.id}
          interactive={interactive}
          onPointerDown={onElementPointerDown}
          onRotateDown={onRotateDown}
        />
      ))}

      {dims.map((d) => (
        <DimensionLine
          key={d.key}
          a={d.a}
          b={d.b}
          label={d.label}
          tone={d.tone}
          dashed={d.dashed}
          u={u}
          tu={tu}
          shift={d.shift}
          onEnter={d.rowId && onRowHover ? () => onRowHover(d.rowId!) : undefined}
          onLeave={d.rowId && onRowHover ? () => onRowHover(null) : undefined}
        />
      ))}

      {/* Fat invisible pick targets, drawn LAST so they sit above the
          elements — marking the road frontage has to work even where the
          driveway already covers that side. */}
      {onSegmentClick && lot.kind === 'poly' && (
        <g>
          {ring.map((a, i) => {
            const b = ring[(i + 1) % ring.length];
            return (
              <line
                key={`pick-${i}`}
                x1={a.x}
                y1={a.y}
                x2={b.x}
                y2={b.y}
                stroke="transparent"
                strokeWidth={11 * u}
                style={{ cursor: 'pointer' }}
                onClick={() => onSegmentClick(i)}
              >
                <title>
                  {plan.frontSegment === i
                    ? 'Road frontage — click to clear'
                    : 'Mark this side as the road frontage'}
                </title>
              </line>
            );
          })}
        </g>
      )}
    </>
  );
}

function dimForRow(
  fromId: string | undefined,
  toId: string | undefined,
  edge: EdgeName | undefined,
  boundary: boolean | undefined,
  byId: Map<string, PlanElement>,
  lot: Lot
): [Pt, Pt] | null {
  const from = fromId ? byId.get(fromId) : null;
  if (!from) return null;
  if (edge && lot.kind === 'rect') return edgeDimension(from, lot, edge);
  if (boundary) {
    const n = nearestBoundary(from, lot);
    return [n.a, n.b];
  }
  const to = toId ? byId.get(toId) : null;
  if (!to) return null;
  return closestPoints(from, to);
}

/**
 * A length on every side, printed outside the boundary along the side it
 * measures. This is required plot-plan content — a reviewer reads the
 * boundary off these — and it is what makes the sheet look like a plat
 * rather than a shape someone drew.
 *
 * Sides too short to hold their own label at the current scale are skipped
 * rather than overprinted; the sheet's separations table still carries the
 * distances that matter, and an unreadable smear of overlapping numbers
 * would cost more than the missing label.
 */
function SideLabels({ ring, u, tu }: { ring: Pt[]; u: number; tu: number }) {
  const lengths = sideLengths(ring);
  const fs = 9.5 * tu;
  return (
    <g pointerEvents="none">
      {lengths.map((len, i) => {
        const a = ring[i];
        const b = ring[(i + 1) % ring.length];
        const label = formatFeetShort(len);
        // Needs room for the text along its own side, or it is left off.
        if (len / u < label.length * 6.4) return null;
        const mid = { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
        const nx = (b.y - a.y) / len;
        const ny = -(b.x - a.x) / len;
        // Clear of the frontage right-of-way dash at 5u, and inside the ROAD
        // caption at 26tu, so the three never stack on one side.
        const px = mid.x + nx * 12 * tu;
        const py = mid.y + ny * 12 * tu;
        const raw = (Math.atan2(b.y - a.y, b.x - a.x) * 180) / Math.PI;
        const deg = raw > 90 || raw < -90 ? raw + 180 : raw;
        return (
          <g key={`side-${i}`} transform={`rotate(${deg} ${px} ${py})`}>
            <rect
              x={px - (label.length * fs * 0.6) / 2 - 2 * tu}
              y={py - fs * 0.72}
              width={label.length * fs * 0.6 + 4 * tu}
              height={fs * 1.44}
              fill="var(--bg-primary)"
            />
            <text
              x={px}
              y={py}
              textAnchor="middle"
              dominantBaseline="central"
              fontFamily="var(--font-mono)"
              fontSize={fs}
              fill="var(--text-secondary)"
            >
              {label}
            </text>
          </g>
        );
      })}
    </g>
  );
}

/**
 * The marked road frontage: the side drawn heavy with a thin line offset
 * outside it, which is how a right-of-way is shown on a plat, and labeled
 * so the sheet says which side the road is on without a legend entry.
 */
function Frontage({
  ring,
  index,
  u,
  tu,
}: {
  ring: Pt[];
  index: number | null;
  u: number;
  tu: number;
}) {
  if (index === null || !ring[index]) return null;
  const a = ring[index];
  const b = ring[(index + 1) % ring.length];
  const len = Math.hypot(b.x - a.x, b.y - a.y);
  if (len < 1e-6) return null;
  const nx = (b.y - a.y) / len;
  const ny = -(b.x - a.x) / len;
  const off = 5 * u;
  const mid = { x: (a.x + b.x) / 2, y: (a.y + b.y) / 2 };
  const raw = (Math.atan2(b.y - a.y, b.x - a.x) * 180) / Math.PI;
  const deg = raw > 90 || raw < -90 ? raw + 180 : raw;
  const lx = mid.x + nx * 26 * tu;
  const ly = mid.y + ny * 26 * tu;
  return (
    <g pointerEvents="none">
      <line
        x1={a.x}
        y1={a.y}
        x2={b.x}
        y2={b.y}
        stroke="var(--text-heading)"
        strokeWidth={4}
        vectorEffect="non-scaling-stroke"
      />
      <line
        x1={a.x + nx * off}
        y1={a.y + ny * off}
        x2={b.x + nx * off}
        y2={b.y + ny * off}
        stroke="var(--text-secondary)"
        strokeWidth={1}
        strokeDasharray="10 5"
        vectorEffect="non-scaling-stroke"
      />
      {len / u > 90 && (
        <text
          x={lx}
          y={ly}
          transform={`rotate(${deg} ${lx} ${ly})`}
          textAnchor="middle"
          dominantBaseline="central"
          fontFamily="var(--font-mono)"
          fontSize={9 * tu}
          letterSpacing={0.14 * 9 * tu}
          fill="var(--text-secondary)"
        >
          ROAD
        </text>
      )}
    </g>
  );
}

/**
 * Long-dash lines inset from the lot edges. Drawn as four separate lines,
 * not one inset rectangle, because front, side and rear can differ and a
 * blank one must simply not appear.
 *
 * Rectangles only. A mitered inward offset of an eight-sided boundary is a
 * different piece of geometry, and a wrong setback line drawn confidently on
 * a permit sheet is worse than no setback line at all — so polygon mode says
 * so in the toolbox and measures the nearest boundary instead.
 */
function Setbacks({ lot, plan }: { lot: RectLot; plan: Plan }) {
  const { front, side, rear } = plan.setbacks;
  const lines: { key: string; x1: number; y1: number; x2: number; y2: number }[] = [];

  const push = (edge: EdgeName, v: number | null) => {
    if (v === null || !Number.isFinite(v) || v <= 0) return;
    if (edge === 'north') lines.push({ key: edge, x1: 0, y1: v, x2: lot.w, y2: v });
    if (edge === 'south')
      lines.push({ key: edge, x1: 0, y1: lot.d - v, x2: lot.w, y2: lot.d - v });
    if (edge === 'west') lines.push({ key: edge, x1: v, y1: 0, x2: v, y2: lot.d });
    if (edge === 'east')
      lines.push({ key: edge, x1: lot.w - v, y1: 0, x2: lot.w - v, y2: lot.d });
  };

  push(plan.frontEdge, front);
  push(OPPOSITE[plan.frontEdge], rear);
  const sides = (['north', 'east', 'south', 'west'] as EdgeName[]).filter(
    (e) => e !== plan.frontEdge && e !== OPPOSITE[plan.frontEdge]
  );
  sides.forEach((e) => push(e, side));

  return (
    <>
      {lines.map((l) => (
        <line
          key={l.key}
          x1={l.x1}
          y1={l.y1}
          x2={l.x2}
          y2={l.y2}
          stroke="var(--accent-info)"
          strokeWidth={1.15}
          strokeDasharray="12 6"
          strokeOpacity={0.8}
          vectorEffect="non-scaling-stroke"
        />
      ))}
    </>
  );
}
