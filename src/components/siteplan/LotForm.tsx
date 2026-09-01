'use client';

/**
 * The empty state (§2.2 step 1). Nothing can be placed without a lot, so the
 * canvas area starts as two number fields plus the state selector — one
 * decision, and no empty toolbox to puzzle over.
 */

import { FormEvent, useState } from 'react';
import s from '@/styles/SitePlanStudio.module.css';
import { acres, lotError } from '@/lib/siteplan/defaults';
import { SITEPLAN_RULES } from '@/lib/siteplan/rules';
import type { EdgeName } from '@/lib/siteplan/types';
import { EDGE_LABEL } from '@/lib/siteplan/types';

interface Props {
  stateCode: string;
  onStateChange: (code: string) => void;
  onSubmit: (w: number, d: number, frontEdge: EdgeName) => void;
}

const STATES = [...SITEPLAN_RULES].sort((a, b) => a.state.localeCompare(b.state));

export default function LotForm({ stateCode, onStateChange, onSubmit }: Props) {
  const [w, setW] = useState('150');
  const [d, setD] = useState('200');
  const [front, setFront] = useState<EdgeName>('north');
  const [error, setError] = useState<string | null>(null);

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
    <form className={s.lotForm} onSubmit={submit}>
      <p className={s.lotFormLabel}>Start with your lot</p>
      <h3 className={s.lotFormTitle}>How big is the parcel?</h3>
      <p className={s.lotFormLead}>
        Two dimensions in feet from your deed, plat or county parcel viewer. You
        can change them later, and nothing you enter leaves your browser.
      </p>

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
          {acres({ w: wNum, d: dNum }).toFixed(2)} acres
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
            Optional. Pick one and the tool checks your layout against what that
            state publishes.
          </span>
        </label>
      </div>

      {error && (
        <p className={s.fieldError} role="alert">
          {error}
        </p>
      )}

      <button type="submit" className={s.primaryBtn}>
        Start drawing
      </button>
    </form>
  );
}
