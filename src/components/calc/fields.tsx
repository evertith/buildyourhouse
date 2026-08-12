'use client';

/**
 * Input primitives for the takeoff-sheet calculators (design spec §4.1–4.3).
 *
 * NumberField keeps a local string draft so partial input ("12.", "") never
 * poisons the engine: the last valid number is what the parent holds, and
 * the schedule keeps rendering from it while the field shows an inline
 * error (spec §5.5 — never NaN, never a blank results panel).
 */

import { ReactNode, useId, useState } from 'react';
import s from '@/styles/CalcSheet.module.css';

interface NumberFieldProps {
  label: string;
  unit: string;
  value: number;
  onChange: (value: number) => void;
  hint?: string;
  min?: number;
  step?: number | 'any';
}

export function NumberField({ label, unit, value, onChange, hint, min = 0, step = 'any' }: NumberFieldProps) {
  const id = useId();
  const [draft, setDraft] = useState<string | null>(null);
  const [invalid, setInvalid] = useState(false);

  const shown = draft ?? String(value);

  const handle = (raw: string) => {
    setDraft(raw);
    const parsed = Number(raw);
    if (raw.trim() === '' || !Number.isFinite(parsed) || parsed < 0) {
      setInvalid(true);
      return;
    }
    setInvalid(false);
    onChange(parsed);
  };

  return (
    <div className={`${s.field} ${invalid ? s.fieldInvalid : ''}`}>
      <label className={s.fieldLabel} htmlFor={id}>{label}</label>
      <div className={s.fieldBox}>
        <input
          id={id}
          className={s.fieldInput}
          type="number"
          inputMode="decimal"
          min={min}
          step={step}
          value={shown}
          onChange={(e) => handle(e.target.value)}
          onBlur={() => { if (!invalid) setDraft(null); }}
        />
        <span className={s.fieldUnit} aria-hidden="true">{unit}</span>
      </div>
      {invalid ? (
        <span className={s.fieldError}>Enter a number</span>
      ) : hint ? (
        <span className={s.fieldHint}>{hint}</span>
      ) : null}
    </div>
  );
}

interface DimPairProps {
  label: string;
  lengthValue: number;
  widthValue: number;
  onLength: (v: number) => void;
  onWidth: (v: number) => void;
  unit?: string;
  hint?: string;
}

export function DimPair({ label, lengthValue, widthValue, onLength, onWidth, unit = 'ft', hint }: DimPairProps) {
  const labelId = useId();
  return (
    <div className={s.field}>
      <span className={s.fieldLabel} id={labelId}>{label}</span>
      <div className={s.dimPair} role="group" aria-labelledby={labelId}>
        <DimInput ariaLabel={`Length in ${unit === 'ft' ? 'feet' : unit}`} unit={unit} value={lengthValue} onChange={onLength} />
        <span className={s.dimTimes} aria-hidden="true">×</span>
        <DimInput ariaLabel={`Width in ${unit === 'ft' ? 'feet' : unit}`} unit={unit} value={widthValue} onChange={onWidth} />
      </div>
      {hint && <span className={s.fieldHint}>{hint}</span>}
    </div>
  );
}

function DimInput({ ariaLabel, unit, value, onChange }: { ariaLabel: string; unit: string; value: number; onChange: (v: number) => void }) {
  const [draft, setDraft] = useState<string | null>(null);
  const [invalid, setInvalid] = useState(false);
  return (
    <div className={`${s.fieldBox} ${invalid ? s.fieldInvalid : ''}`}>
      <input
        className={s.fieldInput}
        type="number"
        inputMode="decimal"
        min={0}
        step="any"
        aria-label={ariaLabel}
        aria-invalid={invalid || undefined}
        value={draft ?? String(value)}
        onChange={(e) => {
          const raw = e.target.value;
          setDraft(raw);
          const parsed = Number(raw);
          if (raw.trim() === '' || !Number.isFinite(parsed) || parsed < 0) {
            setInvalid(true);
            return;
          }
          setInvalid(false);
          onChange(parsed);
        }}
        onBlur={() => { if (!invalid) setDraft(null); }}
      />
      <span className={s.fieldUnit} aria-hidden="true">{unit}</span>
    </div>
  );
}

interface SegOption<T extends string | number> {
  value: T;
  label: ReactNode;
}

interface SegProps<T extends string | number> {
  label: string;
  options: SegOption<T>[];
  value: T;
  onChange: (v: T) => void;
  hint?: string;
}

export function Seg<T extends string | number>({ label, options, value, onChange, hint }: SegProps<T>) {
  const labelId = useId();
  const name = useId();
  return (
    <div className={s.field}>
      <span className={s.fieldLabel} id={labelId}>{label}</span>
      <div className={s.seg} role="radiogroup" aria-labelledby={labelId}>
        {options.map((o) => (
          <label key={String(o.value)} className={`${s.segOpt} ${value === o.value ? s.segOn : ''}`}>
            <input
              type="radio"
              name={name}
              value={String(o.value)}
              checked={value === o.value}
              onChange={() => onChange(o.value)}
              className="visually-hidden"
            />
            {o.label}
          </label>
        ))}
      </div>
      {hint && <span className={s.fieldHint}>{hint}</span>}
    </div>
  );
}

interface SelectFieldProps<T extends string> {
  label: string;
  options: { value: T; label: string }[];
  value: T;
  onChange: (v: T) => void;
  hint?: string;
}

export function SelectField<T extends string>({ label, options, value, onChange, hint }: SelectFieldProps<T>) {
  const id = useId();
  return (
    <div className={s.field}>
      <label className={s.fieldLabel} htmlFor={id}>{label}</label>
      <div className={s.selectBox}>
        <select
          id={id}
          className={s.selectInput}
          value={value}
          onChange={(e) => onChange(e.target.value as T)}
        >
          {options.map((o) => (
            <option key={o.value} value={o.value}>{o.label}</option>
          ))}
        </select>
      </div>
      {hint && <span className={s.fieldHint}>{hint}</span>}
    </div>
  );
}
