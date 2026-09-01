'use client';

/**
 * Left rail: the palette, the lot summary, the owner's setbacks, and the
 * north dial.
 *
 * Clicking a tool DROPS the element immediately (§2.2 step 3) rather than
 * arming a click-to-place cursor — one fewer mode, nothing to explain, and
 * it works from the keyboard.
 */

import s from '@/styles/SitePlanStudio.module.css';
import { acres, KIND_HINT } from '@/lib/siteplan/defaults';
import type { EdgeName, ElementKind, Plan, Setbacks } from '@/lib/siteplan/types';
import { EDGE_LABEL, ELEMENT_KINDS, KIND_LABEL } from '@/lib/siteplan/types';

interface Props {
  plan: Plan;
  onAdd: (kind: ElementKind) => void;
  onEditLot: () => void;
  onSetback: (key: keyof Setbacks, value: number | null) => void;
  onFrontEdge: (edge: EdgeName) => void;
  onNorth: (deg: number) => void;
}

/** Miniature of each symbol, so the palette reads as a legend. */
function ToolGlyph({ kind }: { kind: ElementKind }) {
  const ink = 'var(--text-heading)';
  return (
    <svg viewBox="0 0 22 16" className={s.toolGlyph} aria-hidden="true">
      {kind === 'house' && (
        <rect x="2" y="3" width="18" height="10" fill="none" stroke={ink} strokeWidth="1.8" />
      )}
      {kind === 'structure' && (
        <rect x="4" y="3" width="14" height="10" fill="none" stroke={ink} strokeWidth="1.1" />
      )}
      {kind === 'well' && (
        <>
          <circle cx="11" cy="8" r="4.2" fill="none" stroke={ink} strokeWidth="1.3" />
          <line x1="4.5" y1="8" x2="17.5" y2="8" stroke={ink} strokeWidth="1" />
          <line x1="11" y1="1.5" x2="11" y2="14.5" stroke={ink} strokeWidth="1" />
        </>
      )}
      {kind === 'septicTank' && (
        <>
          <rect x="3" y="4" width="16" height="8" fill="none" stroke={ink} strokeWidth="1.3" />
          <rect x="5" y="6" width="12" height="4" fill="none" stroke={ink} strokeWidth="0.9" />
        </>
      )}
      {kind === 'drainfield' && (
        <>
          <rect x="2" y="3" width="18" height="10" fill="none" stroke={ink} strokeWidth="1.2" />
          <line x1="3.5" y1="6.5" x2="18.5" y2="6.5" stroke={ink} strokeWidth="0.9" strokeDasharray="3 2" />
          <line x1="3.5" y1="9.5" x2="18.5" y2="9.5" stroke={ink} strokeWidth="0.9" strokeDasharray="3 2" />
        </>
      )}
      {kind === 'driveway' && (
        <>
          <line x1="4" y1="2" x2="4" y2="14" stroke={ink} strokeWidth="1.2" />
          <line x1="18" y1="2" x2="18" y2="14" stroke={ink} strokeWidth="1.2" />
          <circle cx="9" cy="5" r="0.8" fill={ink} opacity="0.5" />
          <circle cx="13" cy="8" r="0.8" fill={ink} opacity="0.5" />
          <circle cx="9" cy="11" r="0.8" fill={ink} opacity="0.5" />
        </>
      )}
      {kind === 'waterEdge' && (
        <>
          <line x1="2" y1="9" x2="20" y2="9" stroke="#4a6b80" strokeWidth="1.8" />
          <path d="M4 9 q2 -2.5 4 0 M12 9 q2 -2.5 4 0" fill="none" stroke="#4a6b80" strokeWidth="1" />
        </>
      )}
    </svg>
  );
}

function SetbackField({
  label,
  value,
  onChange,
}: {
  label: string;
  value: number | null;
  onChange: (v: number | null) => void;
}) {
  return (
    <label className={s.sbField}>
      <span className={s.sbLabel}>{label}</span>
      <span className={s.sbBox}>
        <input
          className={s.sbInput}
          type="number"
          inputMode="decimal"
          min={0}
          max={999}
          placeholder="—"
          value={value === null ? '' : value}
          onChange={(e) => {
            const v = e.target.value.trim();
            onChange(v === '' ? null : Number(v));
          }}
        />
        <span className={s.sbUnit}>ft</span>
      </span>
    </label>
  );
}

/** North rotates, the drawing stays screen-up — how a real plan handles it. */
function NorthDial({ deg, onChange }: { deg: number; onChange: (d: number) => void }) {
  const r = 26;
  const a = ((deg - 90) * Math.PI) / 180;
  return (
    <div className={s.northRow}>
      <svg
        viewBox="-34 -34 68 68"
        className={s.northDial}
        role="img"
        aria-label={`North arrow at ${deg} degrees`}
      >
        <circle cx="0" cy="0" r={r + 4} fill="var(--bg-primary)" stroke="var(--hairline)" strokeWidth="1" />
        {Array.from({ length: 12 }, (_, i) => {
          const t = (i * 30 * Math.PI) / 180;
          return (
            <line
              key={i}
              x1={Math.cos(t) * (r - 1)}
              y1={Math.sin(t) * (r - 1)}
              x2={Math.cos(t) * (r + 2.5)}
              y2={Math.sin(t) * (r + 2.5)}
              stroke="var(--hairline-strong)"
              strokeWidth="1"
            />
          );
        })}
        <line
          x1={-Math.cos(a) * (r - 6)}
          y1={-Math.sin(a) * (r - 6)}
          x2={Math.cos(a) * (r - 6)}
          y2={Math.sin(a) * (r - 6)}
          stroke="var(--accent-primary)"
          strokeWidth="1.6"
        />
        <polygon
          points={`${Math.cos(a) * r},${Math.sin(a) * r} ${Math.cos(a + 2.5) * 7},${Math.sin(a + 2.5) * 7} ${Math.cos(a - 2.5) * 7},${Math.sin(a - 2.5) * 7}`}
          fill="var(--accent-primary)"
        />
        <text
          x={Math.cos(a) * (r - 13)}
          y={Math.sin(a) * (r - 13)}
          textAnchor="middle"
          dominantBaseline="central"
          fontFamily="var(--font-mono)"
          fontSize="10"
          fill="var(--text-secondary)"
        >
          N
        </text>
      </svg>
      <label className={s.sbField}>
        <span className={s.sbLabel}>North</span>
        <span className={s.sbBox}>
          <input
            className={s.sbInput}
            type="number"
            min={0}
            max={359}
            step={15}
            value={deg}
            onChange={(e) => {
              const v = Number(e.target.value);
              onChange(Number.isFinite(v) ? ((Math.round(v) % 360) + 360) % 360 : 0);
            }}
          />
          <span className={s.sbUnit}>°</span>
        </span>
      </label>
    </div>
  );
}

export default function Toolbox({
  plan,
  onAdd,
  onEditLot,
  onSetback,
  onFrontEdge,
  onNorth,
}: Props) {
  const lot = plan.lot!;
  return (
    <div className={s.toolbox}>
      <section className={s.rail}>
        <p className={s.railLabel}>Place</p>
        <div className={s.palette}>
          {ELEMENT_KINDS.map((kind) => (
            <button
              key={kind}
              type="button"
              className={s.tool}
              onClick={() => onAdd(kind)}
              title={KIND_HINT[kind]}
            >
              <ToolGlyph kind={kind} />
              <span className={s.toolName}>{KIND_LABEL[kind]}</span>
            </button>
          ))}
        </div>
        <p className={s.railHint}>
          Adds it to the middle of the lot — then drag it where it goes.
        </p>
      </section>

      <section className={s.rail}>
        <p className={s.railLabel}>Lot</p>
        <p className={s.lotSummary}>
          {lot.w} × {lot.d} ft
          <span className={s.lotSummarySub}>{acres(lot).toFixed(2)} acres</span>
        </p>
        <button type="button" className={s.ghostBtn} onClick={onEditLot}>
          Edit lot
        </button>
        <label className={s.sbField}>
          <span className={s.sbLabel}>Road is on the</span>
          <span className={s.selectBox}>
            <select
              className={s.selectInput}
              value={plan.frontEdge}
              onChange={(e) => onFrontEdge(e.target.value as EdgeName)}
            >
              {(['north', 'east', 'south', 'west'] as EdgeName[]).map((e) => (
                <option key={e} value={e}>
                  {EDGE_LABEL[e]}
                </option>
              ))}
            </select>
          </span>
        </label>
      </section>

      <section className={s.rail}>
        <p className={s.railLabel}>Setbacks</p>
        <div className={s.sbGrid}>
          <SetbackField
            label="Front"
            value={plan.setbacks.front}
            onChange={(v) => onSetback('front', v)}
          />
          <SetbackField
            label="Side"
            value={plan.setbacks.side}
            onChange={(v) => onSetback('side', v)}
          />
          <SetbackField
            label="Rear"
            value={plan.setbacks.rear}
            onChange={(v) => onSetback('rear', v)}
          />
        </div>
        <p className={s.railHint}>
          Yours, not the state&apos;s. Zoning setbacks are county and city and
          vary parcel to parcel, so the tool asks rather than guessing. Get them
          in writing from the planning counter.
        </p>
      </section>

      <section className={s.rail}>
        <p className={s.railLabel}>Orientation</p>
        <NorthDial deg={plan.north} onChange={onNorth} />
        <p className={s.railHint}>
          The drawing stays square to the page and the arrow turns — which is
          how a plan handles a lot that is not square to north.
        </p>
      </section>
    </div>
  );
}
