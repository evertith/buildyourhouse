'use client';

import { FormEvent, useId, useRef, useState } from 'react';
import s from '@/styles/Estimate.module.css';
import { trackEvent } from '@/lib/analytics';
import {
  createPlanRead,
  formatMb,
  PLAN_PDF_MAX_BYTES,
  PLAN_PDF_MAX_SHEETS,
  PLAN_READ_PRICE,
} from '@/lib/planRead';
import type { FloorFraming, Foundation, RoofFraming } from '@/lib/planRead';
import { CALCULATOR_SLUG } from './exports';

interface Props {
  /** serializeProfile(...).toString(): finish, state and the switches travel with the read. */
  profileQuery: string;
  onClose: () => void;
}

/**
 * Attach plans: the PDF, the three questions the drawings rarely settle, and
 * the email the results link goes to. Submitting streams the file to the
 * Worker and sends the browser to Stripe. The size limit is stated before
 * the picker and an oversize file is refused here with its size named.
 */
export default function AttachPanel({ profileQuery, onClose }: Props) {
  const [file, setFile] = useState<File | null>(null);
  const [email, setEmail] = useState('');
  const [foundation, setFoundation] = useState<Foundation>('from_plan');
  const [floor, setFloor] = useState<FloorFraming>('from_plan');
  const [roof, setRoof] = useState<RoofFraming>('from_plan');
  const [error, setError] = useState<string | null>(null);
  const [busy, setBusy] = useState(false);
  const [dragging, setDragging] = useState(false);
  const inputRef = useRef<HTMLInputElement | null>(null);
  const id = useId();

  const pick = (f: File | null | undefined) => {
    setError(null);
    if (!f) return;
    const isPdf = f.type === 'application/pdf' || /\.pdf$/i.test(f.name);
    if (!isPdf) {
      setFile(null);
      setError('That is not a PDF. Export the plan set as one PDF and attach that.');
      return;
    }
    if (f.size > PLAN_PDF_MAX_BYTES) {
      setFile(null);
      setError(`That file is ${formatMb(f.size)}. The limit is 100 MB: export at a lower raster resolution, or send only the architectural sheets.`);
      return;
    }
    setFile(f);
  };

  const submit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (busy) return;
    if (!file) {
      setError('Attach the plan set first.');
      return;
    }
    setBusy(true);
    setError(null);
    try {
      const res = await createPlanRead(file, {
        email: email.trim(),
        foundation,
        floorFraming: floor,
        roofFraming: roof,
        profile: profileQuery,
      });
      trackEvent('begin_checkout', {
        calculator: CALCULATOR_SLUG,
        currency: 'USD',
        value: PLAN_READ_PRICE,
        items: [{ item_id: 'plan-read', item_name: 'Measured Whole-House Estimate', price: PLAN_READ_PRICE, quantity: 1 }],
      });
      window.location.href = res.checkout_url;
    } catch (err) {
      setError((err as Error).message || 'The upload did not go through. Try again in a minute.');
      setBusy(false);
    }
  };

  return (
    <form className={`${s.panel} no-print`} onSubmit={submit} aria-labelledby={`${id}-title`}>
      <div className={s.panelHead}>
        <div>
          <p id={`${id}-title`} className={s.panelTitle}>
            Attach your plans, ${PLAN_READ_PRICE}
          </p>
          <p className={s.panelLede}>
            StudTally reads the set and this ledger is re-drawn from your drawings: the footprint,
            every wall, window and door, the roof as drawn, with the sheet beside each number. Usually
            back within a few hours. Refunded if the set cannot be read.
          </p>
        </div>
        <button type="button" className={s.tb} onClick={onClose}>
          Close
        </button>
      </div>

      <div
        className={`${s.drop} ${dragging ? s.dropActive : ''} ${file ? s.dropHas : ''}`}
        onDragOver={(e) => {
          e.preventDefault();
          setDragging(true);
        }}
        onDragLeave={() => setDragging(false)}
        onDrop={(e) => {
          e.preventDefault();
          setDragging(false);
          pick(e.dataTransfer.files?.[0]);
        }}
      >
        <input
          ref={inputRef}
          id={`${id}-file`}
          type="file"
          accept="application/pdf,.pdf"
          className="visually-hidden"
          onChange={(e) => pick(e.target.files?.[0])}
        />
        {file ? (
          <>
            <p className={s.dropName}>{file.name}</p>
            <p className={s.dropMeta}>{formatMb(file.size)}</p>
            <button type="button" className={s.tb} onClick={() => inputRef.current?.click()}>
              Choose a different file
            </button>
          </>
        ) : (
          <>
            <label htmlFor={`${id}-file`} className={`${s.btn} ${s.btnGhost}`} style={{ marginTop: 0 }}>
              Choose the plan set
            </label>
            <p className={s.dropMeta}>
              or drop it here. One PDF up to 100 MB, up to {PLAN_PDF_MAX_SHEETS} sheets. Plans, elevations,
              sections and schedules are what get read.
            </p>
          </>
        )}
      </div>

      <div className={s.qs}>
        <label className={s.q}>
          <span className={s.qLabel}>Foundation</span>
          <select className={s.qSelect} value={foundation} onChange={(e) => setFoundation(e.target.value as Foundation)}>
            <option value="from_plan">Read it from the plan</option>
            <option value="slab">Slab on grade</option>
            <option value="raised_crawl">Crawl space</option>
            <option value="basement">Basement</option>
          </select>
        </label>
        <label className={s.q}>
          <span className={s.qLabel}>Floor framing</span>
          <select className={s.qSelect} value={floor} onChange={(e) => setFloor(e.target.value as FloorFraming)}>
            <option value="from_plan">Read it from the plan</option>
            <option value="lumber">Dimensional lumber joists</option>
            <option value="i_joist">I-joists by the supplier</option>
            <option value="floor_truss">Floor trusses by the supplier</option>
          </select>
        </label>
        <label className={s.q}>
          <span className={s.qLabel}>Roof framing</span>
          <select className={s.qSelect} value={roof} onChange={(e) => setRoof(e.target.value as RoofFraming)}>
            <option value="from_plan">Read it from the plan</option>
            <option value="stick">Stick framed, rafters</option>
            <option value="truss">Trusses by the supplier</option>
          </select>
        </label>
        <label className={s.q}>
          <span className={s.qLabel}>Email for the results link</span>
          <input
            type="email"
            required
            className={s.qInput}
            placeholder="you@example.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            autoComplete="email"
          />
        </label>
      </div>

      {error && (
        <p className={s.panelError} role="alert">
          {error}
        </p>
      )}

      <div className={s.panelFoot}>
        <button type="submit" className={s.btn} style={{ marginTop: 0 }} disabled={busy}>
          {busy ? 'Uploading…' : `Pay $${PLAN_READ_PRICE} and read my plans`}
        </button>
        <p className={s.cardFine} style={{ margin: 0 }}>
          {busy
            ? 'A large set can take a minute to upload. Stripe opens next.'
            : 'Checkout is on Stripe. Your finish, state, and switches stay as set.'}
        </p>
      </div>
    </form>
  );
}
