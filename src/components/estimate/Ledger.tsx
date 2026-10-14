'use client';

import s from '@/styles/Estimate.module.css';
import type { Estimate } from '@/lib/estimate/estimate';
import type { PhaseId } from '@/lib/estimate/types';
import LedgerRow from './LedgerRow';
import { money100 } from './format';

interface Props {
  estimate: Estimate;
  openId: PhaseId | null;
  onToggleOpen: (id: PhaseId) => void;
  onChoice: (id: PhaseId, diy: boolean) => void;
}

/** The phase rows, the cash-to-build footer, and the fine print. */
export default function Ledger({ estimate, openId, onToggleOpen, onChoice }: Props) {
  const t = estimate.totals;
  const maxShare = Math.max(...estimate.phases.map((p) => p.share));
  return (
    <div id="ledger">
      <div className={s.hd} aria-hidden="true">
        <span>Phase</span>
        <span>Share of the cost</span>
        <span className={s.hdRight}>Cost</span>
        <span>Who does it</span>
      </div>

      {estimate.phases.map((row) => (
        <LedgerRow
          key={row.id}
          row={row}
          maxShare={maxShare}
          open={openId === row.id}
          onToggleOpen={onToggleOpen}
          onChoice={onChoice}
        />
      ))}

      <div className={s.ledgerFoot}>
        <span className={s.ledgerFootLabel}>Cash to build</span>
        <span className={s.ledgerFootCash}>{money100(t.cash.mid)}</span>
      </div>
      <p className={s.finePrint}>
        Quantities are derived from your square footage and a typical footprint; the sheet below the
        ledger says how. Prices are national ranges for {estimate.asOf}, scaled to{' '}
        {estimate.state.name}. An estimate, not a quote; order after a takeoff from your plans.
      </p>
    </div>
  );
}
