'use client';

/**
 * The trust moment (§2.5, Amendment A).
 *
 * THREE treatments, and the tool must never render an unverified number in
 * the same style as a verified one:
 *
 *   rules   verified, and the state publishes binding distances. Solid
 *           values, conflicts stated as conflicts, citation inline.
 *   local   verified, and the finding IS that no statewide minimum exists.
 *           The chip still says VERIFIED, because the negative is sourced —
 *           and no default is borrowed to fill the hole.
 *   hedged  not verified. Typical values, daggered and italic, and nothing
 *           is ever called a violation.
 */

import s from '@/styles/SitePlanStudio.module.css';
import { SITEPLAN_RULES, type StateSiteplanRules } from '@/lib/siteplan/rules';
import type { Treatment } from '@/lib/siteplan/types';

interface Props {
  stateCode: string;
  rules: StateSiteplanRules | null;
  treatment: Treatment;
  onChange: (code: string) => void;
  compact?: boolean;
}

const STATES = [...SITEPLAN_RULES].sort((a, b) => a.state.localeCompare(b.state));

export function VerificationChip({
  treatment,
  rules,
}: {
  treatment: Treatment;
  rules: StateSiteplanRules | null;
}) {
  if (treatment === 'none') {
    return <span className={`${s.chip} ${s.chipNone}`}>No state selected</span>;
  }
  if (treatment === 'hedged') {
    return (
      <span className={`${s.chip} ${s.chipHedged}`}>
        † Unverified · typical values
      </span>
    );
  }
  return (
    <span className={`${s.chip} ${s.chipVerified}`}>
      ✓ Verified{rules?.verifiedDate ? ` · ${rules.verifiedDate}` : ''}
    </span>
  );
}

export default function StateSelect({
  stateCode,
  rules,
  treatment,
  onChange,
  compact,
}: Props) {
  const name = rules?.state ?? 'this state';

  return (
    <div className={s.stateBlock}>
      <div className={s.stateRow}>
        <label className={s.stateLabel} htmlFor="sp-state">
          State
        </label>
        <span className={s.selectBox}>
          <select
            id="sp-state"
            className={s.selectInput}
            value={stateCode}
            onChange={(e) => onChange(e.target.value)}
          >
            <option value="">No state — just measure</option>
            {STATES.map((st) => (
              <option key={st.code} value={st.code}>
                {st.state}
              </option>
            ))}
          </select>
        </span>
        <VerificationChip treatment={treatment} rules={rules} />
      </div>

      {treatment === 'hedged' && (
        <div className={`${s.band} ${s.bandHedged}`} role="note">
          <p>
            We have not verified {name}&apos;s separation distances. The figures
            below are typical of what states require and are here so you can
            sanity-check your layout — they are <strong>not</strong> {name}&apos;s
            rule. Confirm with your county health department before you dig.
          </p>
        </div>
      )}

      {treatment === 'local' && (
        <div className={`${s.band} ${s.bandLocal}`} role="note">
          <p>
            Verified, and the finding is a negative: {name} publishes no
            statewide separation distance to measure against. Your county or
            district health department sets it. What the research found, and
            where it looked, is below — nothing here is measured against a
            default.
          </p>
        </div>
      )}

      {!compact && rules?.ownerDrawnAccepted && (
        <p className={s.ownerDrawn}>
          <span className={s.ownerDrawnKey}>Owner-drawn plans in {name}</span>
          {rules.ownerDrawnAccepted}
        </p>
      )}

      <p className={s.counterNote}>
        Distances are measured from what you draw. Whether your department
        accepts an owner-drawn plan — and what it must show — is decided at
        the counter, not here.
      </p>
    </div>
  );
}
