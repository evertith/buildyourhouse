'use client';

import { useState } from 'react';
import s from '@/styles/Estimate.module.css';
import { checkoutPlanRead, PLAN_READ_PRICE } from '@/lib/planRead';
import type { PlanReadView } from '@/lib/planRead';

interface Props {
  view: PlanReadView | null;
  /** The token in the URL named no read. */
  missing: boolean;
  cancelled: boolean;
  error: string | null;
  onAttachAnother: () => void;
}

/**
 * The strip under the title while a read is unpaid, queued, running, or
 * over without a result. The ready state has no strip: the ledger itself
 * is the result.
 */
export default function ReadingStatus({ view, missing, cancelled, error, onAttachAnother }: Props) {
  const [busy, setBusy] = useState(false);
  const [payError, setPayError] = useState<string | null>(null);

  const pay = async () => {
    if (!view || busy) return;
    setBusy(true);
    setPayError(null);
    try {
      const res = await checkoutPlanRead(view.token);
      if (res.checkout_url) {
        window.location.href = res.checkout_url;
        return;
      }
      window.location.reload();
    } catch (err) {
      setPayError((err as Error).message);
      setBusy(false);
    }
  };

  if (missing) {
    return (
      <div className={`${s.status} no-print`} role="status">
        <p className={s.statusTitle}>That plan read was not found.</p>
        <p className={s.statusBody}>
          The link may be incomplete. Look it up with the email you paid with at{' '}
          <a href="/shop/recover">the order recovery page</a>, or attach the set again below.
        </p>
      </div>
    );
  }

  if (!view) {
    if (error) {
      return (
        <div className={`${s.status} no-print`} role="status">
          <p className={s.statusTitle}>Checking on your plans…</p>
          <p className={s.statusBody}>{error}</p>
        </div>
      );
    }
    return (
      <div className={`${s.status} no-print`} role="status">
        <p className={s.statusTitle}>Checking on your plans…</p>
      </div>
    );
  }

  const name = view.plan.name || 'your plan set';
  const sheets = view.plan.pageCount ? `, ${view.plan.pageCount} sheets` : '';

  if (view.status === 'setup') {
    return (
      <div className={`${s.status} no-print`} role="status">
        <p className={s.statusTitle}>
          {cancelled ? 'Checkout was cancelled.' : 'Your plans are attached but the read is not paid for.'}
        </p>
        <p className={s.statusBody}>
          {name}
          {sheets} is uploaded and your answers are kept. Pay the ${PLAN_READ_PRICE} and the read starts; the
          free estimate below is unchanged until then.
        </p>
        <div className={s.statusActions}>
          <button type="button" className={s.btn} style={{ marginTop: 0 }} onClick={pay} disabled={busy}>
            {busy ? 'Opening checkout…' : `Pay $${PLAN_READ_PRICE} and start the read`}
          </button>
          <button type="button" className={s.tb} onClick={onAttachAnother}>
            Attach a different set
          </button>
        </div>
        {payError && (
          <p className={s.panelError} role="alert">
            {payError}
          </p>
        )}
      </div>
    );
  }

  if (view.status === 'queued' || view.status === 'reading') {
    const running = view.progress.find((p) => p.status === 'running');
    const done = view.progress.filter((p) => p.status === 'done').length;
    const total = view.progress.length;
    const step = running ? `${running.label}${running.detail ? `: ${running.detail}` : ''}` : view.status === 'queued' ? 'Waiting for the reader' : 'Reading';
    return (
      <div className={`${s.status} no-print`} role="status" aria-live="polite">
        <p className={s.statusTitle}>
          <span className={s.pulse} aria-hidden="true" />
          Reading {name}
          {sheets}.
        </p>
        <p className={s.statusBody}>
          {step}
          {total ? ` (${done} of ${total} steps done)` : ''}. Usually within a few hours, often faster. The
          ledger below is still the free estimate; it re-draws itself when the read is done, and the link
          goes to {view.emailHint || 'your email'} as well, so you can close this tab.
        </p>
        {total > 0 && (
          <ol className={s.steps}>
            {view.progress.map((p) => (
              <li key={p.key} className={`${s.step} ${s[`step_${p.status}`] ?? ''}`}>
                {p.label}
              </li>
            ))}
          </ol>
        )}
      </div>
    );
  }

  if (view.status === 'unsupported' || view.status === 'refunded') {
    return (
      <div className={`${s.status} no-print`} role="status">
        <p className={s.statusTitle}>We could not read {name}.</p>
        <p className={s.statusBody}>
          {view.reason || 'The set did not carry enough to measure from.'}{' '}
          {view.refunded
            ? `The $${PLAN_READ_PRICE} has been refunded to your card; it shows up in a few business days.`
            : 'Nothing was charged for the read.'}{' '}
          The free estimate below is unchanged. If you have the architect&apos;s PDF rather than a scan, or
          the full set with the floor plans and the roof plan, attach that one.
        </p>
        <div className={s.statusActions}>
          <button type="button" className={`${s.btn} ${s.btnGhost}`} style={{ marginTop: 0 }} onClick={onAttachAnother}>
            Attach a different set
          </button>
        </div>
      </div>
    );
  }

  return null;
}
