'use client';

import s from '@/styles/Estimate.module.css';
import type { Geometry, Profile } from '@/lib/estimate/geometry';
import { measuredFacts, sheetLabel } from '@/lib/estimate/measured';
import type { Finish } from '@/lib/estimate/prices';
import { STATES } from '@/lib/estimate/stateIndex';

interface Props {
  geometry: Geometry;
  profile: Profile;
  onChange: (patch: Partial<Profile>) => void;
}

const STATE_OPTIONS = [...STATES].sort((a, b) => a.name.localeCompare(b.name));

/**
 * The title-block facts once the plans are read: what was measured with its
 * sheet, and the two inputs that are still the visitor's (finish and state).
 * Square footage, stories, foundation, roof and wall height are no longer
 * chips; the drawings settled them.
 */
export default function MeasuredChips({ geometry, profile, onChange }: Props) {
  const facts = measuredFacts(geometry).slice(0, 4);
  return (
    <div className={`${s.chips} no-print`}>
      {facts.map((f) => (
        <span key={f.text} className={s.fact}>
          {f.text}
          {f.ref ? (
            <span className={`${s.tag} ${s.tagM}`}>{sheetLabel(f.ref)}</span>
          ) : f.you ? (
            <span className={`${s.tag} ${s.tagD}`}>you</span>
          ) : null}
        </span>
      ))}
      <label className={s.chip}>
        <span className={s.chipLabel}>Finish</span>
        <select className={s.chipSelect} value={profile.finish} onChange={(e) => onChange({ finish: e.target.value as Finish })}>
          <option value="basic">Basic</option>
          <option value="standard">Standard</option>
          <option value="premium">Premium</option>
        </select>
        <span className={`${s.tag} ${s.tagD}`}>you</span>
      </label>
      <label className={s.chip}>
        <span className={s.chipLabel}>State</span>
        <select className={s.chipSelect} value={profile.state} onChange={(e) => onChange({ state: e.target.value })}>
          {STATE_OPTIONS.map((st) => (
            <option key={st.code} value={st.code}>
              {st.name}
            </option>
          ))}
        </select>
        <span className={`${s.tag} ${s.tagD}`}>you</span>
      </label>
    </div>
  );
}
