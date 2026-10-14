'use client';

import { useState } from 'react';
import s from '@/styles/Estimate.module.css';
import TrackedLink from '@/components/TrackedLink';
import type { Estimate } from '@/lib/estimate/estimate';
import type { Geometry, Profile } from '@/lib/estimate/geometry';
import { humanizePlanName, measuredFacts, sheetLabel } from '@/lib/estimate/measured';
import { PLAN_READ_PRICE } from '@/lib/planRead';
import type { PlanReadView } from '@/lib/planRead';
import { STUDTALLY_PRICE, studTallyUrl } from '@/lib/studtally';
import InboxForm from './InboxForm';
import { hoursApprox, money, money100, pct, plural } from './format';

export type ExportKind = 'copy' | 'print' | 'csv' | 'email';

interface Props {
  estimate: Estimate;
  profile: Profile;
  copied: boolean;
  onExport: (kind: ExportKind) => void;
  /** The plan read this page follows, if any. */
  view: PlanReadView | null;
  /** The measured geometry once the read is ready. */
  measured: Geometry | null;
  planName?: string;
  onAttach: () => void;
}

/**
 * The sticky rail: cash to build with the split bar and contingency, the
 * tools, the inbox form, and the plans card. The split bar is on the same
 * scale as the ledger bars (share of every trade hired), so the eye can
 * carry a phase's bar up to the total. The plans card is the attach offer
 * in the free state, a one-line status while a read is in flight, and the
 * measured-facts card plus the framing-list upgrade once it is done.
 */
export default function Rail({ estimate, profile, copied, onExport, view, measured, planName, onAttach }: Props) {
  const t = estimate.totals;
  const all = t.allHired.mid || 1;
  const matShare = (t.materials.mid + t.soft.mid) / all;
  const hiredShare = t.hiredLabor.mid / all;
  const ownShare = t.ownLabor.mid / all;

  return (
    <>
      <div className={s.card}>
        <p className={s.cardLabel}>Cash to build, before contingency</p>
        <div className={s.cash}>{money100(t.cash.mid)}</div>
        <p className={s.cashMeta}>
          Likely {money100(t.cash.low)} to {money100(t.cash.high)}, about {money(t.perSqFt.mid)} per square foot.
          Every trade hired: {money100(t.allHired.mid)}.
        </p>
        <div
          className={s.split}
          role="img"
          aria-label={`Materials and soft costs ${money100(t.materials.mid + t.soft.mid)}, hired labor ${money100(t.hiredLabor.mid)}, your own hours worth ${money100(t.ownLabor.mid)}`}
        >
          <span className={s.barMat} style={{ width: `${pct(matShare)}%` }} />
          <span className={s.barLab} style={{ width: `${pct(hiredShare)}%` }} />
          <span className={s.barOwn} style={{ width: `${pct(ownShare)}%` }} />
        </div>
        <div className={s.legend}>
          <span className={s.legendRow}>
            <span>
              <span className={s.swatch} style={{ background: 'var(--paper)' }} />
              Materials and soft costs
            </span>
            <strong>{money100(t.materials.mid + t.soft.mid)}</strong>
          </span>
          <span className={s.legendRow}>
            <span>
              <span className={s.swatch} style={{ background: 'var(--grey)' }} />
              Hired labor
            </span>
            <strong>{money100(t.hiredLabor.mid)}</strong>
          </span>
          <span className={s.legendRow}>
            <span>
              <span className={s.swatch} style={{ background: 'var(--orange)' }} />
              Your hours, about {hoursApprox(t.hours)}
            </span>
            <strong>{money100(t.ownLabor.mid)}</strong>
          </span>
        </div>
        <p className={s.contingency}>
          Carry a 10% contingency on top: <strong>{money100(t.contingency.mid)}</strong>. {t.nDiy}{' '}
          {plural(t.nDiy, 'phase', 'phases')} yourself.
        </p>
        <div className={`${s.tools} no-print`} style={{ marginTop: 18 }}>
          <button type="button" className={s.tb} onClick={() => onExport('copy')}>
            {copied ? 'Copied' : 'Copy'}
          </button>
          <button type="button" className={s.tb} onClick={() => onExport('print')}>
            Print
          </button>
          <button type="button" className={s.tb} onClick={() => onExport('csv')}>
            Download CSV
          </button>
        </div>
      </div>

      {measured ? (
        <>
          <MeasuredCard geometry={measured} estimate={estimate} view={view} planName={planName} />
          <UpgradeCard view={view} />
        </>
      ) : view ? (
        <StatusCard view={view} />
      ) : (
        <div className={`${s.card} ${s.cardGhost} no-print`}>
          <p className={s.cardTitle}>Have your plans?</p>
          <p className={s.cardBody}>
            Attach the plan set as a PDF and every row is measured from your drawings: the footprint, every
            wall and window, the roof as drawn, with the sheet it came from beside each number. Usually back
            within a few hours. Refunded if the set cannot be read.
          </p>
          <button type="button" className={s.btn} onClick={onAttach}>
            Attach plans, ${PLAN_READ_PRICE}
          </button>
          <p className={s.cardFine}>
            Read by StudTally, from the people behind this site. When you order framing, the ${PLAN_READ_PRICE}{' '}
            comes off StudTally&apos;s ${STUDTALLY_PRICE} framing list.
          </p>
        </div>
      )}

      <div className={`${s.card} ${s.cardGhost} no-print`}>
        <p className={s.cardTitleSm}>Send this ledger to your inbox</p>
        <p className={s.cardFine}>
          Your {measured ? 'plans, ' : 'profile, '}every phase, and the split, as one email, so you still have it at the lumberyard.
        </p>
        <InboxForm estimate={estimate} profile={profile} planName={planName} onSent={() => onExport('email')} />
      </div>
    </>
  );
}

function StatusCard({ view }: { view: PlanReadView }) {
  const name = view.plan.name || 'your plan set';
  const line =
    view.status === 'setup'
      ? `${name} is attached. Pay the $${PLAN_READ_PRICE} above and the read starts.`
      : view.status === 'queued' || view.status === 'reading'
        ? `${name} is being read. The ledger re-draws itself when it is done.`
        : `${name} could not be read${view.refunded ? '; refunded' : ''}. The free estimate stands.`;
  return (
    <div className={`${s.card} ${s.cardGhost} no-print`}>
      <p className={s.cardTitleSm}>Plans attached</p>
      <p className={s.cardFine}>{line}</p>
    </div>
  );
}

function MeasuredCard({
  geometry,
  estimate,
  view,
  planName,
}: {
  geometry: Geometry;
  estimate: Estimate;
  view: PlanReadView | null;
  planName?: string;
}) {
  const facts = measuredFacts(geometry);
  const nMeasured = estimate.phases.filter((p) => p.basis === 'measured').length;
  const nTotal = estimate.phases.length;
  const g = view?.geometry;
  const sheets = g?.sheets_read && g?.sheets_total ? `${g.sheets_read} of ${g.sheets_total} sheets read` : null;
  return (
    <div className={s.card}>
      <p className={s.cardTitleSm}>Measured from your plans</p>
      <p className={s.cardFine} style={{ marginTop: 4 }}>
        {planName ? humanizePlanName(planName) : 'Plan set'}
        {sheets ? `, ${sheets}` : ''}
      </p>
      <ul className={s.facts}>
        {facts.map((f) => (
          <li key={f.text} className={s.factRow}>
            <span>{f.text}</span>
            {f.ref ? (
              <span className={`${s.tag} ${s.tagM}`}>{sheetLabel(f.ref)}</span>
            ) : f.you ? (
              <span className={`${s.tag} ${s.tagD}`}>you</span>
            ) : null}
          </li>
        ))}
      </ul>
      <p className={s.cardFine}>
        {nMeasured} of {nTotal} phases measured, {nTotal - nMeasured} derived from area.
      </p>
      {geometry.assumed.length > 0 && (
        <details className="more">
          <summary>What was assumed</summary>
          <ul className={s.assumedList}>
            {geometry.assumed.map((a) => (
              <li key={a}>{a}</li>
            ))}
          </ul>
        </details>
      )}
    </div>
  );
}

function UpgradeCard({ view }: { view: PlanReadView | null }) {
  const [copied, setCopied] = useState(false);
  const code = view?.upgrade?.code ?? null;
  const expires = view?.upgrade?.expiresAt ? new Date(view.upgrade.expiresAt) : null;
  const copy = async () => {
    if (!code) return;
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      window.setTimeout(() => setCopied(false), 1500);
    } catch {
      // Clipboard unavailable: the code is on screen.
    }
  };
  return (
    <div className={`${s.card} ${s.cardGhost} no-print`}>
      <p className={s.cardTitle}>Framing list, ${STUDTALLY_PRICE}, ${PLAN_READ_PRICE} back</p>
      <p className={s.cardBody}>
        Every stud, plate, header, sheet and hanger, counted per wall and reviewed by a person. Framing only:
        the other thirteen phases stay estimates.
      </p>
      {code ? (
        <>
          <div className={s.code}>
            <span>{code}</span>
            <button type="button" className={s.tb} onClick={copy}>
              {copied ? 'Copied' : 'Copy'}
            </button>
          </div>
          <p className={s.cardFine}>
            Enter it at StudTally&apos;s checkout and ${PLAN_READ_PRICE} comes off the ${STUDTALLY_PRICE}.
            {expires && !Number.isNaN(expires.getTime())
              ? ` Good until ${expires.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })}.`
              : ''}
          </p>
        </>
      ) : (
        <p className={s.cardFine}>
          Your ${PLAN_READ_PRICE} credit code is in the email that said this estimate was ready; reply to it if it is missing.
        </p>
      )}
      <TrackedLink
        href={studTallyUrl('measured-estimate')}
        target="_blank"
        rel="noopener"
        className={`${s.btn} ${s.btnGhost}`}
        eventName="studtally_upgrade_click"
        eventParams={{ calculator: 'material-estimator', location: 'estimator-rail-measured' }}
      >
        Open at StudTally
      </TrackedLink>
    </div>
  );
}
