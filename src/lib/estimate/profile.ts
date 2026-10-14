/**
 * The profile in the URL, so an estimate is shareable and the state pages
 * can pre-set it: ?sqft=2000&stories=1&finish=standard&found=slab&state=NC
 * &roof=hip&height=9&diy=insulation,interior,final
 *
 * Absent keys fall back to the defaults; `diy=none` means every phase
 * hired. Parsing is forgiving (a bad value is the default, never an error).
 */

import { HEATED_SF_MAX, HEATED_SF_MIN, PROFILE_DEFAULTS } from './geometry.ts';
import type { Foundation, Profile, RoofComplexity, Stories, WallHeight } from './geometry.ts';
import { DIY_DEFAULT } from './labor.ts';
import type { Finish } from './prices.ts';
import { DEFAULT_STATE, isStateCode } from './stateIndex.ts';
import { PHASE_ORDER } from './types.ts';
import type { PhaseId } from './types.ts';
import { clamp, roundTo } from './types.ts';

export interface ProfileState {
  profile: Profile;
  diy: PhaseId[];
}

const FINISHES: Finish[] = ['basic', 'standard', 'premium'];
const FOUNDATIONS: Foundation[] = ['slab', 'crawl', 'basement'];
const ROOFS: RoofComplexity[] = ['gable', 'hip', 'cutup'];

function pick<T extends string>(raw: string | null, allowed: readonly T[], fallback: T): T {
  return raw && (allowed as readonly string[]).includes(raw) ? (raw as T) : fallback;
}

export function parseProfile(params: URLSearchParams): ProfileState {
  const d = PROFILE_DEFAULTS;
  const sqftRaw = Number(params.get('sqft'));
  const heatedSf = Number.isFinite(sqftRaw) && sqftRaw > 0
    ? roundTo(clamp(sqftRaw, HEATED_SF_MIN, HEATED_SF_MAX))
    : d.heatedSf;
  const storiesRaw = Number(params.get('stories'));
  const stories = ([1, 2, 3] as const).includes(storiesRaw as Stories) ? (storiesRaw as Stories) : d.stories;
  const heightRaw = Number(params.get('height'));
  const wallHeightFt = ([8, 9, 10] as const).includes(heightRaw as WallHeight)
    ? (heightRaw as WallHeight)
    : d.wallHeightFt;
  const stateRaw = (params.get('state') ?? '').toUpperCase();
  const state = isStateCode(stateRaw) ? stateRaw : DEFAULT_STATE;

  const diyRaw = params.get('diy');
  let diy: PhaseId[];
  if (diyRaw === null) diy = [...DIY_DEFAULT];
  else if (diyRaw === 'none' || diyRaw === '') diy = [];
  else {
    const ids = diyRaw.split(',');
    diy = PHASE_ORDER.filter((id) => id !== 'soft' && ids.includes(id));
  }

  return {
    profile: {
      heatedSf,
      stories,
      finish: pick(params.get('finish'), FINISHES, d.finish),
      foundation: pick(params.get('found'), FOUNDATIONS, d.foundation),
      state,
      roof: pick(params.get('roof'), ROOFS, d.roof),
      wallHeightFt,
    },
    diy,
  };
}

/** Only the keys that differ from the defaults, so a default estimate has a clean URL. */
export function serializeProfile({ profile: p, diy }: ProfileState): URLSearchParams {
  const d = PROFILE_DEFAULTS;
  const q = new URLSearchParams();
  if (p.heatedSf !== d.heatedSf) q.set('sqft', String(p.heatedSf));
  if (p.stories !== d.stories) q.set('stories', String(p.stories));
  if (p.finish !== d.finish) q.set('finish', p.finish);
  if (p.foundation !== d.foundation) q.set('found', p.foundation);
  if (p.state !== d.state) q.set('state', p.state);
  if (p.roof !== d.roof) q.set('roof', p.roof);
  if (p.wallHeightFt !== d.wallHeightFt) q.set('height', String(p.wallHeightFt));
  const diySorted = PHASE_ORDER.filter((id) => diy.includes(id));
  const defaultSorted = PHASE_ORDER.filter((id) => DIY_DEFAULT.includes(id));
  if (diySorted.join(',') !== defaultSorted.join(',')) {
    q.set('diy', diySorted.length ? diySorted.join(',') : 'none');
  }
  return q;
}
