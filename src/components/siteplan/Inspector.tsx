'use client';

/**
 * Right rail: the selected element's numbers, and every distance from it.
 *
 * Numeric first (§2.2 step 5) — on a permit drawing people want a right
 * angle, not a feeling. Below 768px this is also the ONLY way to move an
 * element (§5): position is edited as distance from the west and north
 * lines, which is how a surveyor would enter it anyway, because a 466 ft lot
 * at 390px is under a pixel per foot and a drag that feels bad is worse than
 * no drag at all.
 */

import s from '@/styles/SitePlanStudio.module.css';
import {
  distanceToLotEdges,
  elementDistance,
  formatFeet,
} from '@/lib/siteplan/geometry';
import type { EdgeName, Plan, PlanElement } from '@/lib/siteplan/types';
import { EDGE_LABEL, KIND_LABEL } from '@/lib/siteplan/types';

interface Props {
  plan: Plan;
  selected: PlanElement | null;
  onResize: (id: string, w: number, d: number) => void;
  onRotate: (id: string, rot: number) => void;
  onSetEdgeDistance: (id: string, edge: EdgeName, feet: number) => void;
  onDelete: (id: string) => void;
  onHoverElement: (id: string | null) => void;
  /** True on desktop, where dragging is the primary way to place. */
  draggable: boolean;
}

function NumField({
  label,
  value,
  unit = 'ft',
  min,
  max,
  step,
  onChange,
}: {
  label: string;
  value: number;
  unit?: string;
  min?: number;
  max?: number;
  step?: number;
  onChange: (v: number) => void;
}) {
  return (
    <label className={s.sbField}>
      <span className={s.sbLabel}>{label}</span>
      <span className={s.sbBox}>
        <input
          className={s.sbInput}
          type="number"
          inputMode="decimal"
          min={min}
          max={max}
          step={step}
          value={Number.isFinite(value) ? Math.round(value * 10) / 10 : 0}
          onChange={(e) => {
            const v = Number(e.target.value);
            if (Number.isFinite(v)) onChange(v);
          }}
        />
        <span className={s.sbUnit}>{unit}</span>
      </span>
    </label>
  );
}

export default function Inspector({
  plan,
  selected,
  onResize,
  onRotate,
  onSetEdgeDistance,
  onDelete,
  onHoverElement,
  draggable,
}: Props) {
  const lot = plan.lot!;

  if (!selected) {
    return (
      <div className={s.inspector}>
        <p className={s.railLabel}>Element</p>
        <p className={s.inspectorEmpty}>
          {plan.elements.length === 0
            ? 'Place something from the toolbox and it will show its dimensions here.'
            : draggable
              ? 'Click an element on the plan to edit its size, angle and distances.'
              : 'Tap an element on the plan to edit its position and size.'}
        </p>
      </div>
    );
  }

  const edges = distanceToLotEdges(selected, lot);
  const others = plan.elements.filter((e) => e.id !== selected.id);
  const isPoint = selected.kind === 'well';
  const isLine = selected.kind === 'waterEdge';

  return (
    <div className={s.inspector}>
      <div className={s.inspectorHead}>
        <p className={s.railLabel}>{KIND_LABEL[selected.kind]}</p>
        <button
          type="button"
          className={s.deleteBtn}
          onClick={() => onDelete(selected.id)}
        >
          Delete
        </button>
      </div>

      {!isPoint && (
        <div className={s.sbGrid}>
          <NumField
            label={isLine ? 'Length' : 'Width'}
            value={selected.w}
            min={1}
            max={5280}
            onChange={(v) => onResize(selected.id, Math.max(1, v), selected.d)}
          />
          {!isLine && (
            <NumField
              label="Depth"
              value={selected.d}
              min={1}
              max={5280}
              onChange={(v) => onResize(selected.id, selected.w, Math.max(1, v))}
            />
          )}
        </div>
      )}

      {!isPoint && (
        <>
          <NumField
            label="Rotate"
            unit="°"
            value={selected.rot}
            min={0}
            max={359}
            step={15}
            onChange={(v) => onRotate(selected.id, ((Math.round(v) % 360) + 360) % 360)}
          />
          <div className={s.rotRow}>
            {[0, 90, 180, 270].map((deg) => (
              <button
                key={deg}
                type="button"
                className={`${s.rotBtn} ${selected.rot === deg ? s.rotBtnOn : ''}`}
                onClick={() => onRotate(selected.id, deg)}
              >
                {deg}°
              </button>
            ))}
          </div>
        </>
      )}

      <p className={s.railLabel}>Position</p>
      <div className={s.sbGrid}>
        <NumField
          label="From west line"
          value={edges.west}
          onChange={(v) => onSetEdgeDistance(selected.id, 'west', v)}
        />
        <NumField
          label="From north line"
          value={edges.north}
          onChange={(v) => onSetEdgeDistance(selected.id, 'north', v)}
        />
      </div>

      <p className={s.railLabel}>Distances</p>
      <ul className={s.distList}>
        {(['north', 'east', 'south', 'west'] as EdgeName[]).map((edge) => (
          <li key={edge} className={s.distRow}>
            <span className={s.distKey}>{EDGE_LABEL[edge]}</span>
            <span className={s.distLeader} />
            <span
              className={`${s.distVal} ${edges[edge] < 0 ? s.distValBad : ''}`}
            >
              {edges[edge] < 0
                ? `${formatFeet(Math.abs(edges[edge]))} over`
                : formatFeet(edges[edge])}
            </span>
          </li>
        ))}
        {others.map((o) => (
          <li
            key={o.id}
            className={s.distRow}
            onMouseEnter={() => onHoverElement(o.id)}
            onMouseLeave={() => onHoverElement(null)}
          >
            <span className={s.distKey}>{KIND_LABEL[o.kind]}</span>
            <span className={s.distLeader} />
            <span className={s.distVal}>
              {formatFeet(elementDistance(selected, o))}
            </span>
          </li>
        ))}
      </ul>
    </div>
  );
}
