'use client';

import s from '@/styles/Estimate.module.css';
import type { PhaseRow } from '@/lib/estimate/estimate';
import type { PhaseId } from '@/lib/estimate/types';
import { hoursApprox, money100, pct } from './format';

interface Props {
  row: PhaseRow;
  /** The largest phase share on the ledger; that phase fills its track. */
  maxShare: number;
  open: boolean;
  onToggleOpen: (id: PhaseId) => void;
  onChoice: (id: PhaseId, diy: boolean) => void;
  /** Plans attached: tag derived rows too, so the two bases read side by side. */
  showBasis?: boolean;
}

const mid = (r: { low: number; high: number }) => (r.low + r.high) / 2;

/**
 * One phase: name and note, the share-of-cost bar on the same scale as the
 * rail's split bar, the cash this phase costs, and the who-does-it switch.
 * The name opens the lines. Orange appears only on an owner's own hours.
 */
export default function LedgerRow({ row, maxShare, open, onToggleOpen, onChoice, showBasis = false }: Props) {
  const mat = mid(row.materials);
  const lab = mid(row.labor);
  const total = mat + lab;
  const cash = mat + (row.diy ? 0 : lab);
  const matPct = total > 0 ? pct(mat / total) : '100';
  const labPct = total > 0 ? pct(lab / total) : '0';
  const hasLines = row.lines.length > 0;
  const panelId = `phase-${row.id}-lines`;

  return (
    <div className={s.row}>
      <div className={s.cName}>
        {hasLines ? (
          <button
            type="button"
            className={s.name}
            aria-expanded={open}
            aria-controls={panelId}
            onClick={() => onToggleOpen(row.id)}
          >
            <svg width="10" height="12" viewBox="0 0 10 12" aria-hidden="true">
              <path d="M1 1l7 5-7 5z" fill="currentColor" />
            </svg>
            <span>{row.name}</span>
            {row.basis === 'measured' ? (
              <span className={`${s.tag} ${s.tagM}`}>measured</span>
            ) : showBasis && !row.soft ? (
              <span className={`${s.tag} ${s.tagD}`}>derived</span>
            ) : null}
          </button>
        ) : (
          <p className={s.name} style={{ paddingLeft: 20, cursor: 'default' }}>
            <span>{row.name}</span>
            {showBasis && !row.soft && <span className={`${s.tag} ${s.tagD}`}>derived</span>}
          </p>
        )}
        <p className={s.note}>{row.note}</p>
        {row.licensed && (
          <p className={s.hint}>
            Some states reserve this work for a licensed trade.{' '}
            <a href="/permitting/state-guides">Check your state guide.</a>
          </p>
        )}
      </div>

      <div className={`${s.bar} ${s.cBar}`} aria-hidden="true">
        <div className={s.barFill} style={{ width: `${pct(maxShare > 0 ? row.share / maxShare : 0)}%` }}>
          <span className={s.barMat} style={{ width: `${matPct}%` }} />
          {lab > 0 && (
            <span className={row.diy ? s.barOwn : s.barLab} style={{ width: `${labPct}%` }} />
          )}
        </div>
      </div>

      <div className={`${s.cost} ${s.cCost}`}>
        {money100(cash)}
        {row.diy && <span className={s.costHours}>plus about {hoursApprox(row.hours)} hours of yours</span>}
      </div>

      <div className={s.cSeg}>
        {row.soft ? (
          <span className={s.paidNotBuilt}>Paid, not built</span>
        ) : (
          <div className={s.seg} role="group" aria-label={`Who does ${row.name.toLowerCase()}`}>
            <button type="button" aria-pressed={!row.diy} onClick={() => onChoice(row.id, false)}>
              Hire it
            </button>
            <button type="button" aria-pressed={row.diy} onClick={() => onChoice(row.id, true)}>
              Do it myself
            </button>
          </div>
        )}
      </div>

      {open && hasLines && (
        <div className={s.lines} id={panelId}>
          {row.lines.map((l) => (
            <div key={l.id} className={s.ln}>
              <span>
                <span className={s.lnName}>
                  {l.label}
                  {l.unit !== 'allowance' && (
                    <>
                      {', '}
                      {formatQty(l.qty)} {l.unit}
                    </>
                  )}
                </span>
                {l.detail && <span className={s.lnSub}>{l.detail}</span>}
              </span>
              <span className={s.v}>{money100((l.costLow + l.costHigh) / 2)}</span>
            </div>
          ))}
          <div className={`${s.ln} ${s.lnFoot}`}>
            <span>Materials</span>
            <span className={s.v}>{money100(mat)}</span>
          </div>
          {!row.soft && (
            <div className={s.ln}>
              <span style={{ color: 'var(--muted)' }}>
                Labor, about {hoursApprox(row.hours)} hours
                {row.diy ? ', yours' : ''}
              </span>
              <span className={s.v}>{row.diy ? 'your time' : money100(lab)}</span>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

function formatQty(q: number): string {
  return new Intl.NumberFormat('en-US', { maximumFractionDigits: 1 }).format(q);
}
