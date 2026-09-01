'use client';

/**
 * The tear-off stub (§6): emails the owner their measured distances, their
 * conflicts and the citations, as text they can forward to a health
 * department. It sits BELOW the sheet and AFTER the print button — the
 * value-delivered-first position `EstimateCapture` uses — and it never gates
 * the print or the SVG download.
 *
 * It posts to the newsletter worker's /siteplan route, which subscribes the
 * address and sends the measurements immediately. Nothing here promises a
 * future artifact — the deliverable is the email, and it goes out now.
 *
 * The worker prints the `rows` label/value pairs verbatim and frames the
 * whole email off the `verified` boolean, so both are built to survive the
 * trip: a typical value stays worded as typical, and `verified` is read
 * straight off rules.ts rather than inferred from the display treatment.
 */

import { FormEvent, useState } from 'react';
import s from '@/styles/SitePlanStudio.module.css';
import { trackEvent } from '@/lib/analytics';
import { formatFeet } from '@/lib/siteplan/geometry';
import { measureAllPairs, sheetRows } from '@/lib/siteplan/check';
import type { StateSiteplanRules } from '@/lib/siteplan/rules';
import type { CheckResult, Plan } from '@/lib/siteplan/types';
import { EDGE_LABEL, KIND_LABEL } from '@/lib/siteplan/types';

const WORKER_BASE =
  process.env.NEXT_PUBLIC_NEWSLETTER_WORKER_BASE ??
  'https://buildyourhouse-newsletter.azerothcorner.workers.dev';

const CAPTURE_PATH = '/siteplan';

interface Props {
  plan: Plan;
  result: CheckResult;
  rules: StateSiteplanRules | null;
}

/** The measurements as label/value pairs — the shape the worker prints. */
export function capturePayloadRows(plan: Plan, result: CheckResult) {
  const rows: { label: string; value: string }[] = [];

  for (const b of result.boundary) {
    rows.push({
      label: `${b.label} — outside the property line`,
      value: `crosses the ${EDGE_LABEL[b.edge].toLowerCase()} by ${formatFeet(b.overFeet)}`,
    });
  }
  for (const w of result.setbacks) {
    rows.push({
      label: `${w.label} — your ${EDGE_LABEL[w.edge].toLowerCase()} setback`,
      value: `${formatFeet(w.measuredFeet)} — inside the ${w.requiredFeet}' setback you entered`,
    });
  }
  for (const r of sheetRows(result)) {
    // The worker prints label/value pairs verbatim, so the measurement, the
    // requirement and the citation all have to live in the value string —
    // and the hedged wording has to survive the trip, because an unverified
    // number must not read as a requirement in an inbox either.
    const req = r.hedged
      ? `${r.requiredFeet}' typical, not verified`
      : `${r.status === 'violation' ? 'needs' : 'meets'} ${r.requiredFeet}'`;
    const cite = r.citation ? ` · ${r.citation}` : '';
    rows.push({
      label: r.label,
      value: `${formatFeet(r.measuredFeet ?? 0)} — ${req}${cite}`.slice(0, 140),
    });
  }
  // No rule rows happens constantly — it is every verified state whose
  // finding is that no statewide minimum exists, and every visitor who has
  // not picked a state. Send the measurements anyway: they are the thing a
  // health department will ask for, and they are true without any rule.
  if (!rows.length && plan.lot) {
    for (const m of measureAllPairs(plan)) {
      rows.push({
        label: m.label,
        value: `${formatFeet(m.feet)} — no state rule found; your health department sets this`.slice(0, 140),
      });
    }
  }
  // Last resort: too little drawn to measure a pair, so send the positions.
  if (!rows.length && plan.lot) {
    for (const el of plan.elements) {
      rows.push({
        label: KIND_LABEL[el.kind],
        value: `${Math.round(el.x)} ft east and ${Math.round(el.y)} ft south of the north-west corner`,
      });
    }
  }
  return rows.slice(0, 20);
}

export default function SheetCapture({ plan, result, rules }: Props) {
  const [email, setEmail] = useState('');
  const [honeypot, setHoneypot] = useState('');
  const [status, setStatus] = useState<'idle' | 'loading' | 'success' | 'error'>('idle');

  const rows = capturePayloadRows(plan, result);

  const submit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    if (status === 'loading') return;
    setStatus('loading');
    const notes = result.notes
      .filter((n) => n.id.startsWith('null-') || n.conditional)
      .slice(0, 8)
      .map((n) =>
        `${n.label}${n.feet != null ? ` (${n.feet} ft)` : ''}: ${n.text}${
          n.citation ? ` — ${n.citation}` : ''
        }`.slice(0, 300)
      );
    try {
      const res = await fetch(`${WORKER_BASE}${CAPTURE_PATH}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email,
          website: honeypot,
          sourcePath: window.location.pathname,
          state: plan.stateCode,
          stateName: rules?.state ?? 'No state selected',
          // Straight from rules.ts, never inferred: this boolean drives the
          // verified-vs-typical framing of the email the owner receives, so a
          // wrong value here would put a hedged number in an inbox with a
          // verified sentence around it.
          verified: rules?.verified ?? false,
          lot: plan.lot ? `${plan.lot.w} × ${plan.lot.d} ft` : 'as drawn',
          rows,
          notes,
        }),
      });
      if (!res.ok) throw new Error(`siteplan send failed: ${res.status}`);
      const data = (await res.json()) as { ok?: boolean };
      if (data.ok !== true) throw new Error('siteplan send rejected');
      setStatus('success');
      trackEvent('generate_lead', { method: 'siteplan_capture' });
    } catch {
      setStatus('error');
    }
  };

  return (
    <div className={`${s.capture} no-print`}>
      <div>
        <p className={s.captureHead}>Your measurements, in your inbox</p>
        <p className={s.captureSub}>
          Every distance on this sheet, with the requirement and the statute
          citation beside it, sent now — so you have the source when you call
          the health department. You&apos;ll also get the owner-builder
          newsletter; unsubscribe in one click.
        </p>
      </div>
      {status === 'success' ? (
        <p className={s.captureDone} role="status">
          Sent. Give it a few minutes, and check spam if it isn&apos;t there.
        </p>
      ) : (
        <form className={s.captureForm} onSubmit={submit}>
          <input
            type="text"
            name="website"
            value={honeypot}
            onChange={(e) => setHoneypot(e.target.value)}
            style={{ position: 'absolute', left: '-9999px', height: 0, width: 0, opacity: 0 }}
            tabIndex={-1}
            autoComplete="off"
            aria-hidden="true"
          />
          <input
            type="email"
            required
            placeholder="you@example.com"
            aria-label="Email address"
            className={s.captureInput}
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            disabled={status === 'loading'}
          />
          <button type="submit" className={s.captureBtn} disabled={status === 'loading'}>
            {status === 'loading' ? 'Sending…' : 'Email me my measurements'}
          </button>
        </form>
      )}
      {status === 'error' ? (
        <p className={`${s.captureFine} ${s.fieldError}`} role="alert">
          That didn&apos;t send. Try again in a minute.
        </p>
      ) : (
        <p className={s.captureFine}>
          No spam. One email with your numbers, then the occasional newsletter.
        </p>
      )}
    </div>
  );
}
