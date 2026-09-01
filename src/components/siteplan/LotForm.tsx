'use client';

/**
 * The empty state (§2.2 step 1). Nothing can be placed without a lot, so the
 * canvas area starts as two number fields plus the state selector — one
 * decision, and no empty toolbox to puzzle over.
 *
 * v1.5 adds one more door without moving the first: the rectangle stays the
 * default and the fast path, and a single toggle opens polygon entry for the
 * parcels that are not rectangles. Real parcels are notched, angled and
 * metes-and-bounds at every size — a cul-de-sac lot with a well on it is as
 * likely to be odd-shaped as a hundred acres — so the door has to be here,
 * not buried behind a note telling people to draw the boundary by hand.
 */

import { FormEvent, useState } from 'react';
import s from '@/styles/SitePlanStudio.module.css';
import { acres, lotError } from '@/lib/siteplan/defaults';
import { SITEPLAN_RULES } from '@/lib/siteplan/rules';
import type { EdgeName, Lot, Pt } from '@/lib/siteplan/types';
import { EDGE_LABEL } from '@/lib/siteplan/types';
import LotShapeEditor from './LotShapeEditor';

interface Props {
  stateCode: string;
  /** The lot being edited, or null on a first visit. */
  lot: Lot | null;
  onStateChange: (code: string) => void;
  onSubmit: (w: number, d: number, frontEdge: EdgeName) => void;
  onSubmitPoly: (pts: Pt[]) => void;
  /** Only offered when there is already a lot to go back to. */
  onCancel?: () => void;
}

const STATES = [...SITEPLAN_RULES].sort((a, b) => a.state.localeCompare(b.state));

export default function LotForm({
  stateCode,
  lot,
  onStateChange,
  onSubmit,
  onSubmitPoly,
  onCancel,
}: Props) {
  const [w, setW] = useState(lot?.kind === 'rect' ? String(lot.w) : '150');
  const [d, setD] = useState(lot?.kind === 'rect' ? String(lot.d) : '200');
  const [front, setFront] = useState<EdgeName>('north');
  const [error, setError] = useState<string | null>(null);
  const [poly, setPoly] = useState(lot?.kind === 'poly');

  const wNum = Number(w);
  const dNum = Number(d);
  const valid = !lotError(wNum, dNum);

  const submit = (e: FormEvent) => {
    e.preventDefault();
    const err = lotError(wNum, dNum);
    if (err) {
      setError(err);
      return;
    }
    setError(null);
    onSubmit(wNum, dNum, front);
  };

  return (
    <div className={`${s.lotForm} ${poly ? s.lotFormWide : ''}`}>
      <p className={s.lotFormLabel}>Start with your lot</p>
      <h3 className={s.lotFormTitle}>
        {poly ? 'Where does the boundary run?' : 'How big is the parcel?'}
      </h3>
      <p className={s.lotFormLead}>
        {poly
          ? 'Click the corners as they actually run, or type the bearing and distance calls straight off your deed. Nothing you enter leaves your browser.'
          : 'Two dimensions in feet from your deed, plat or county parcel viewer. You can change them later, and nothing you enter leaves your browser.'}
      </p>

      <label className={s.shapeToggle}>
        <input
          type="checkbox"
          className={s.shapeToggleBox}
          checked={poly}
          data-testid="poly-toggle"
          onChange={(e) => {
            setPoly(e.target.checked);
            setError(null);
          }}
        />
        <span>
          <strong>This lot isn&apos;t rectangular.</strong> Draw the boundary
          corner by corner, or enter it from the deed.
        </span>
      </label>

      {poly ? (
        <>
          <LotShapeEditor
            initial={lot?.kind === 'poly' ? lot.pts : null}
            onSubmit={onSubmitPoly}
            onCancel={() => (onCancel ? onCancel() : setPoly(false))}
          />
          <div className={s.lotRow}>
            <label className={s.field}>
              <span className={s.fieldLabel}>State</span>
              <span className={s.selectBox}>
                <select
                  className={s.selectInput}
                  value={stateCode}
                  onChange={(e) => onStateChange(e.target.value)}
                >
                  <option value="">No state — just measure</option>
                  {STATES.map((st) => (
                    <option key={st.code} value={st.code}>
                      {st.state}
                    </option>
                  ))}
                </select>
              </span>
              <span className={s.fieldHint}>
                Optional. Pick one and the tool checks your layout against what
                that state publishes.
              </span>
            </label>
            <p className={s.fieldHint}>
              <strong>The road.</strong> A polygon has no north or west side to
              pick from a list, so mark the frontage by clicking that boundary
              side on the plan once the lot is drawn.
            </p>
          </div>
        </>
      ) : (
        <form onSubmit={submit}>
          <div className={s.lotFields}>
            <label className={s.field}>
              <span className={s.fieldLabel}>Width (east–west)</span>
              <span className={s.fieldBox}>
                <input
                  className={s.fieldInput}
                  type="number"
                  inputMode="decimal"
                  min={10}
                  max={5280}
                  value={w}
                  onChange={(e) => setW(e.target.value)}
                />
                <span className={s.fieldUnit}>ft</span>
              </span>
            </label>
            <span className={s.lotTimes} aria-hidden="true">
              ×
            </span>
            <label className={s.field}>
              <span className={s.fieldLabel}>Depth (north–south)</span>
              <span className={s.fieldBox}>
                <input
                  className={s.fieldInput}
                  type="number"
                  inputMode="decimal"
                  min={10}
                  max={5280}
                  value={d}
                  onChange={(e) => setD(e.target.value)}
                />
                <span className={s.fieldUnit}>ft</span>
              </span>
            </label>
          </div>

          {valid && (
            <p className={s.lotAcres}>
              {(wNum * dNum).toLocaleString()} sq ft ·{' '}
              {acres({ kind: 'rect', w: wNum, d: dNum }).toFixed(2)} acres
            </p>
          )}

          <div className={s.lotRow}>
            <label className={s.field}>
              <span className={s.fieldLabel}>Which edge is the road on?</span>
              <span className={s.selectBox}>
                <select
                  className={s.selectInput}
                  value={front}
                  onChange={(e) => setFront(e.target.value as EdgeName)}
                >
                  {(['north', 'east', 'south', 'west'] as EdgeName[]).map((e) => (
                    <option key={e} value={e}>
                      {EDGE_LABEL[e]}
                    </option>
                  ))}
                </select>
              </span>
              <span className={s.fieldHint}>
                Front, side and rear setbacks are measured from this.
              </span>
            </label>

            <label className={s.field}>
              <span className={s.fieldLabel}>State</span>
              <span className={s.selectBox}>
                <select
                  className={s.selectInput}
                  value={stateCode}
                  onChange={(e) => onStateChange(e.target.value)}
                >
                  <option value="">No state — just measure</option>
                  {STATES.map((st) => (
                    <option key={st.code} value={st.code}>
                      {st.state}
                    </option>
                  ))}
                </select>
              </span>
              <span className={s.fieldHint}>
                Optional. Pick one and the tool checks your layout against what
                that state publishes.
              </span>
            </label>
          </div>

          {error && (
            <p className={s.fieldError} role="alert">
              {error}
            </p>
          )}

          <div className={s.shapeActions}>
            <button type="submit" className={s.primaryBtn}>
              Start drawing
            </button>
            {onCancel && (
              <button type="button" className={s.ghostBtn} onClick={onCancel}>
                Cancel
              </button>
            )}
          </div>
        </form>
      )}
    </div>
  );
}
