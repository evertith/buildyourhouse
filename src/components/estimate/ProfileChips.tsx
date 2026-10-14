'use client';

import { useState } from 'react';
import s from '@/styles/Estimate.module.css';
import type { Foundation, Profile, RoofComplexity, Stories, WallHeight } from '@/lib/estimate/geometry';
import { HEATED_SF_MAX, HEATED_SF_MIN } from '@/lib/estimate/geometry';
import type { Finish } from '@/lib/estimate/prices';
import { STATES } from '@/lib/estimate/stateIndex';

interface Props {
  profile: Profile;
  onChange: (patch: Partial<Profile>) => void;
}

const STATE_OPTIONS = [...STATES].sort((a, b) => a.name.localeCompare(b.name));

/**
 * The input chips. Every change recomputes the ledger at once; the square
 * footage field keeps its own text so a visitor can type "25" on the way to
 * "2500" without the estimate jumping to the minimum.
 */
export default function ProfileChips({ profile, onChange }: Props) {
  const [sqftText, setSqftText] = useState(String(profile.heatedSf));
  const [syncedSqft, setSyncedSqft] = useState(profile.heatedSf);
  const [more, setMore] = useState(profile.roof !== 'hip' || profile.wallHeightFt !== 9);

  // The profile can change from outside (URL hydration): adopt the new value
  // during render rather than in an effect.
  if (profile.heatedSf !== syncedSqft) {
    setSyncedSqft(profile.heatedSf);
    setSqftText(String(profile.heatedSf));
  }

  const commitSqft = (raw: string) => {
    const n = Number(raw);
    if (Number.isFinite(n) && n >= HEATED_SF_MIN && n <= HEATED_SF_MAX) {
      onChange({ heatedSf: Math.round(n) });
    }
  };

  const blurSqft = () => {
    const n = Number(sqftText);
    if (!Number.isFinite(n) || n <= 0) {
      setSqftText(String(profile.heatedSf));
      return;
    }
    const clamped = Math.min(HEATED_SF_MAX, Math.max(HEATED_SF_MIN, Math.round(n)));
    setSqftText(String(clamped));
    if (clamped !== profile.heatedSf) onChange({ heatedSf: clamped });
  };

  return (
    <div className={`${s.chips} no-print`}>
      <label className={s.chip}>
        <span className={s.chipLabel}>Finished area</span>
        <input
          className={s.chipInput}
          type="number"
          inputMode="numeric"
          min={HEATED_SF_MIN}
          max={HEATED_SF_MAX}
          step={50}
          value={sqftText}
          onChange={(e) => {
            setSqftText(e.target.value);
            commitSqft(e.target.value);
          }}
          onBlur={blurSqft}
          aria-label="Finished square feet"
        />
        <span className={s.chipUnit}>sq ft</span>
      </label>

      <label className={s.chip}>
        <span className={s.chipLabel}>Stories</span>
        <select
          className={s.chipSelect}
          value={profile.stories}
          onChange={(e) => onChange({ stories: Number(e.target.value) as Stories })}
        >
          <option value={1}>1</option>
          <option value={2}>2</option>
          <option value={3}>3</option>
        </select>
      </label>

      <label className={s.chip}>
        <span className={s.chipLabel}>Finish</span>
        <select
          className={s.chipSelect}
          value={profile.finish}
          onChange={(e) => onChange({ finish: e.target.value as Finish })}
        >
          <option value="basic">Basic</option>
          <option value="standard">Standard</option>
          <option value="premium">Premium</option>
        </select>
      </label>

      <label className={s.chip}>
        <span className={s.chipLabel}>Foundation</span>
        <select
          className={s.chipSelect}
          value={profile.foundation}
          onChange={(e) => onChange({ foundation: e.target.value as Foundation })}
        >
          <option value="slab">Slab</option>
          <option value="crawl">Crawl space</option>
          <option value="basement">Basement</option>
        </select>
      </label>

      <label className={s.chip}>
        <span className={s.chipLabel}>State</span>
        <select
          className={s.chipSelect}
          value={profile.state}
          onChange={(e) => onChange({ state: e.target.value })}
        >
          {STATE_OPTIONS.map((st) => (
            <option key={st.code} value={st.code}>
              {st.name}
            </option>
          ))}
        </select>
      </label>

      {more ? (
        <>
          <label className={s.chip}>
            <span className={s.chipLabel}>Roof</span>
            <select
              className={s.chipSelect}
              value={profile.roof}
              onChange={(e) => onChange({ roof: e.target.value as RoofComplexity })}
            >
              <option value="gable">Simple gable</option>
              <option value="hip">Hip or mixed</option>
              <option value="cutup">Cut-up, valleys</option>
            </select>
          </label>
          <label className={s.chip}>
            <span className={s.chipLabel}>Walls</span>
            <select
              className={s.chipSelect}
              value={profile.wallHeightFt}
              onChange={(e) => onChange({ wallHeightFt: Number(e.target.value) as WallHeight })}
            >
              <option value={8}>8 ft</option>
              <option value={9}>9 ft</option>
              <option value={10}>10 ft</option>
            </select>
          </label>
        </>
      ) : (
        <button type="button" className={s.chipMore} onClick={() => setMore(true)} aria-expanded={false}>
          Roof and wall height
        </button>
      )}
    </div>
  );
}
