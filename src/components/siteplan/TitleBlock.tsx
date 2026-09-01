'use client';

/**
 * The sheet's title block, north box, and the owner-prepared disclaimer.
 *
 * Write-ins print as the typed value if entered and as a ruled blank line
 * for a pen if not — the binder's print-and-fill convention, and it means
 * the sheet is usable before the owner knows their APN. That is why these
 * are inputs with a bottom rule rather than text: one component covers both
 * states with no toggle.
 */

import s from '@/styles/ExportSheet.module.css';
import type { StateSiteplanRules } from '@/lib/siteplan/rules';
import type { TitleFields, Treatment } from '@/lib/siteplan/types';

interface Props {
  title: TitleFields;
  onChange: (key: keyof TitleFields, value: string) => void;
  scaleLabel: string;
  date: string;
  rules: StateSiteplanRules | null;
  treatment: Treatment;
}

function WriteIn({
  label,
  value,
  onChange,
}: {
  label: string;
  value: string;
  onChange: (v: string) => void;
}) {
  return (
    <label className={s.writeIn}>
      <span className={s.writeInKey}>{label}</span>
      <input
        className={s.writeInField}
        type="text"
        value={value}
        maxLength={60}
        onChange={(e) => onChange(e.target.value)}
      />
    </label>
  );
}

export function NorthBox({ deg }: { deg: number }) {
  const a = ((deg - 90) * Math.PI) / 180;
  const r = 15;
  return (
    <div className={s.northBox}>
      <svg viewBox="-22 -22 44 44" className={s.northSvg} aria-label={`North, ${deg} degrees`}>
        <circle cx="0" cy="0" r="20" fill="none" stroke="var(--hairline)" strokeWidth="0.7" />
        <line
          x1={-Math.cos(a) * (r - 3)}
          y1={-Math.sin(a) * (r - 3)}
          x2={Math.cos(a) * (r - 3)}
          y2={Math.sin(a) * (r - 3)}
          stroke="var(--text-heading)"
          strokeWidth="1"
        />
        <polygon
          points={`${Math.cos(a) * r},${Math.sin(a) * r} ${Math.cos(a + 2.6) * 5.5},${Math.sin(a + 2.6) * 5.5} ${Math.cos(a - 2.6) * 5.5},${Math.sin(a - 2.6) * 5.5}`}
          fill="var(--text-heading)"
        />
      </svg>
      <span className={s.northKey}>N</span>
    </div>
  );
}

/**
 * The liability block (§8b). It names the mechanism, names who decides, and
 * points at the printed citations rather than asking to be believed. A
 * hedged state gets the "typical values, not verified" wording instead.
 */
export function Disclaimer({
  rules,
  treatment,
}: {
  rules: StateSiteplanRules | null;
  treatment: Treatment;
}) {
  const name = rules?.state;
  return (
    <div className={s.disclaimer}>
      <p className={s.disclaimerHead}>Owner-prepared</p>
      <p className={s.disclaimerBody}>
        This plot plan was prepared by the property owner using a free drawing
        tool — not by a licensed surveyor or engineer. Dimensions are as entered
        by the owner and have not been field-verified against a recorded survey.{' '}
        {treatment === 'rules' && name ? (
          <>
            Separation distances are checked against {name} requirements as
            published, {rules?.verifiedDate ?? 'August 2026'}; each citation is
            printed in the schedule.
          </>
        ) : treatment === 'local' && name ? (
          <>
            {name} publishes no statewide separation distance; the notes below
            record what the research found and who sets the number.
          </>
        ) : treatment === 'hedged' && name ? (
          <>
            Separation distances shown are typical values. {name}&apos;s
            requirements were not verified for this tool. Confirm every distance
            with your county health department before construction.
          </>
        ) : (
          <>No state was selected, so no separation requirement was checked.</>
        )}{' '}
        Requirements change, and the office reviewing this application decides
        what applies to this parcel. <strong>This is not a boundary survey.</strong>
      </p>
      <p className={s.disclaimerMark}>build-your-house.com/site-plan-studio</p>
    </div>
  );
}

export default function TitleBlock({
  title,
  onChange,
  scaleLabel,
  date,
  rules,
  treatment,
}: Props) {
  return (
    <div className={s.titleGrid}>
      <div className={s.titleFields}>
        <WriteIn
          label="Project"
          value={title.project}
          onChange={(v) => onChange('project', v)}
        />
        <WriteIn label="Owner" value={title.owner} onChange={(v) => onChange('owner', v)} />
        <WriteIn
          label="Address"
          value={title.address}
          onChange={(v) => onChange('address', v)}
        />
        <WriteIn
          label="Parcel (APN)"
          value={title.parcel}
          onChange={(v) => onChange('parcel', v)}
        />
        <div className={s.titleCells}>
          <div className={s.titleCell}>
            <span className={s.titleCellKey}>Scale</span>
            <span className={s.titleCellVal}>{scaleLabel}</span>
          </div>
          <div className={s.titleCell}>
            <span className={s.titleCellKey}>Date</span>
            <span className={s.titleCellVal}>{date}</span>
          </div>
          <div className={s.titleCell}>
            <span className={s.titleCellKey}>Sheet</span>
            <span className={s.titleCellVal}>SP-01</span>
          </div>
        </div>
      </div>
      <Disclaimer rules={rules} treatment={treatment} />
    </div>
  );
}
