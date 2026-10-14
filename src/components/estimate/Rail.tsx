'use client';

import s from '@/styles/Estimate.module.css';
import TrackedLink from '@/components/TrackedLink';
import type { Estimate } from '@/lib/estimate/estimate';
import type { Profile } from '@/lib/estimate/geometry';
import { STUDTALLY_PRICE, studTallyUrl } from '@/lib/studtally';
import InboxForm from './InboxForm';
import { hoursApprox, money, money100, pct, plural } from './format';

export type ExportKind = 'copy' | 'print' | 'csv' | 'email';

interface Props {
  estimate: Estimate;
  profile: Profile;
  copied: boolean;
  onExport: (kind: ExportKind) => void;
}

/**
 * The sticky rail: cash to build with the split bar and contingency, the
 * tools, the inbox form, and the plans card. The split bar is on the same
 * scale as the ledger bars (share of every trade hired), so the eye can
 * carry a phase's bar up to the total.
 */
export default function Rail({ estimate, profile, copied, onExport }: Props) {
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

      <div className={`${s.card} ${s.cardGhost} no-print`}>
        <p className={s.cardTitleSm}>Send this ledger to your inbox</p>
        <p className={s.cardFine}>
          Your profile, every phase, and the split, as one email, so you still have it at the lumberyard.
        </p>
        <InboxForm estimate={estimate} profile={profile} onSent={() => onExport('email')} />
      </div>

      <div className={`${s.card} ${s.cardGhost} no-print`}>
        <p className={s.cardTitle}>Have your plans?</p>
        <p className={s.cardBody}>
          StudTally reads a residential plan set and returns the framing list the yard keys in: every
          stud, plate, header, sheet, and hanger, counted per wall and reviewed by a person. Framing
          only; the other thirteen phases stay estimates. ${STUDTALLY_PRICE}, usually under an hour.
        </p>
        <TrackedLink
          href={studTallyUrl('material-estimator')}
          target="_blank"
          rel="noopener"
          className={`${s.btn} ${s.btnGhost}`}
          eventName="studtally_click"
          eventParams={{ calculator: 'material-estimator', location: 'estimator-rail' }}
        >
          Upload plans at StudTally
        </TrackedLink>
        <p className={s.cardFine}>From the people behind this site.</p>
      </div>
    </>
  );
}
