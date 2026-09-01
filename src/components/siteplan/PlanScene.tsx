/**
 * The drawing itself — property line, setbacks, elements, dimensions.
 *
 * One component renders both the editor canvas and the printed sheet. That
 * is deliberate: what is seen is what prints, down to the tick marks, and a
 * symbol can never drift between the two. The only differences are the
 * `mode` flag (interaction and hover chrome are screen-only) and the
 * viewBox the caller sets.
 */

import {
  closestPoints,
  edgeDimension,
  formatFeet,
  type Pt,
} from '@/lib/siteplan/geometry';
import { liveRows } from '@/lib/siteplan/check';
import type { CheckResult, EdgeName, Plan, PlanElement } from '@/lib/siteplan/types';
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
  /** Below the drag breakpoint the inspector lists the four property-line
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
}: Props) {
  const lot = plan.lot;
  if (!lot) return null;

  const tu = textU ?? u;
  const byId = new Map(plan.elements.map((e) => [e.id, e]));
  const dims: Dim[] = [];

  // ---- Lot dimensions, north and west edges (§2.2 step 2)
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

  // ---- Every rule measuring under 1.5x its minimum, selection-independent
  const live = liveRows(result);
  live.forEach((row, i) => {
    const dim = dimForRow(row.fromId, row.toId, row.edge, byId, lot);
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

  // ---- The selected element's four distances to the property lines
  const sel = selectedId ? byId.get(selectedId) : null;
  if (sel && mode === 'screen' && showSelectionDims) {
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
  }

  // ---- Setback crossings the OWNER entered — their own visual language
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

  return (
    <>
      {/* Property line: solid heavy, the drawing's outer boundary. */}
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
      <Setbacks plan={plan} />

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
    </>
  );
}

function dimForRow(
  fromId: string | undefined,
  toId: string | undefined,
  edge: EdgeName | undefined,
  byId: Map<string, PlanElement>,
  lot: { w: number; d: number }
): [Pt, Pt] | null {
  const from = fromId ? byId.get(fromId) : null;
  if (!from) return null;
  if (edge) return edgeDimension(from, lot, edge);
  const to = toId ? byId.get(toId) : null;
  if (!to) return null;
  return closestPoints(from, to);
}

/**
 * Long-dash lines inset from the lot edges. Drawn as four separate lines,
 * not one inset rectangle, because front, side and rear can differ and a
 * blank one must simply not appear.
 */
function Setbacks({ plan }: { plan: Plan }) {
  const lot = plan.lot!;
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
