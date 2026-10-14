/**
 * StudTally → Geometry: the measured rung.
 *
 * The partner API returns a flat summary of what the plan read found. Every
 * field it carries becomes a measured Geometry field with its sheet
 * reference; every field it lacks falls back to the derived rule for a
 * house of the measured size, so a partial read still produces a complete
 * ledger and each row's basis tag tells the truth. Decimals arrive as
 * strings (StudTally serializes every quantity that way).
 */

import { deriveGeometry, FOUNDATION_LABEL, HEATED_SF_MAX, HEATED_SF_MIN } from './geometry.ts';
import type { Foundation, Geometry, Profile, Roof, RoofComplexity, Sourced, Stories, WallHeight } from './geometry.ts';
import { clamp } from './types.ts';

export interface MeasuredOpenings {
  windows?: number | string;
  window_area_sf?: number | string;
  ext_doors?: number | string;
  garage_doors?: number | string;
}

export interface MeasuredRooms {
  count?: number | string;
  baths?: number | string;
  kitchens?: number | string;
  bedrooms?: number | string;
}

export interface MeasuredRoof {
  plane_area_sf?: number | string;
  pitch?: number | string;
  ridge_lf?: number | string;
  hip_valley_lf?: number | string;
  eave_lf?: number | string;
  framing?: string;
}

/** The geometry summary from StudTally's partner API (docs/10 §6.4 there). */
export interface MeasuredPayload {
  plan_id: string;
  name?: string;
  sheets_total?: number;
  sheets_read?: number;
  heated_sf?: number | string;
  stories?: number | string;
  footprint_sf?: number | string;
  perimeter_lf?: number | string;
  footprint?: { width_ft?: number | string; depth_ft?: number | string };
  wall_height_ft?: number | string;
  ext_wall_lf?: number | string;
  int_wall_lf?: number | string;
  ext_wall_area_sf?: number | string;
  openings?: MeasuredOpenings;
  rooms?: MeasuredRooms;
  roof?: MeasuredRoof;
  foundation?: string;
  framed_floor_sf?: number | string;
  unheated_sf?: number | string;
  garage_sf?: number | string;
  porches?: { count?: number | string; posts?: number | string };
  refs?: Record<string, string>;
  assumed?: string[];
  extraction_version?: number;
  pipeline_version?: string;
  read_at?: string;
}

/** One line of the rail's "measured from your plans" list. */
export interface MeasuredFact {
  text: string;
  ref?: string;
  /** The buyer answered this at attach time; there is no sheet behind it. */
  you?: boolean;
}

const num = (v: unknown): number | undefined => {
  if (v === null || v === undefined || v === '') return undefined;
  const n = typeof v === 'number' ? v : Number(v);
  return Number.isFinite(n) ? n : undefined;
};

/** More exterior doors than this on one house is a mis-tagged read, not a house. */
const EXT_DOORS_SANE_MAX = 8;

const FOUNDATION_FROM_STUDTALLY: Record<string, Foundation> = {
  slab: 'slab',
  raised_crawl: 'crawl',
  crawl: 'crawl',
  basement: 'basement',
};

function roofComplexity(roof: MeasuredRoof | undefined): RoofComplexity | undefined {
  if (!roof) return undefined;
  const hv = num(roof.hip_valley_lf);
  const ridge = num(roof.ridge_lf);
  if (hv === undefined) return undefined;
  if (hv === 0) return 'gable';
  if (ridge !== undefined && ridge > 0 && hv > 1.2 * ridge) return 'cutup';
  return 'hip';
}

/**
 * The profile a plan read implies, with the visitor's finish and state kept.
 * Used to derive the fallback geometry and to keep the chips honest.
 */
export function measuredProfile(payload: MeasuredPayload, base: Profile): Profile {
  const heated = num(payload.heated_sf);
  const stories = num(payload.stories);
  const wall = num(payload.wall_height_ft);
  const foundation = payload.foundation ? FOUNDATION_FROM_STUDTALLY[payload.foundation] : undefined;
  const roof = roofComplexity(payload.roof);
  return {
    heatedSf: heated !== undefined ? Math.round(clamp(heated, HEATED_SF_MIN, HEATED_SF_MAX)) : base.heatedSf,
    stories: stories !== undefined ? (clamp(Math.round(stories), 1, 3) as Stories) : base.stories,
    finish: base.finish,
    foundation: foundation ?? base.foundation,
    state: base.state,
    roof: roof ?? base.roof,
    wallHeightFt: wall !== undefined ? (clamp(Math.round(wall), 8, 10) as WallHeight) : base.wallHeightFt,
  };
}

/** Build the measured geometry: payload fields where present, derived rules elsewhere. */
export function measuredGeometry(payload: MeasuredPayload, base: Profile): Geometry {
  const profile = measuredProfile(payload, base);
  const d = deriveGeometry(profile);
  const refs = payload.refs ?? {};
  const m = <T>(value: T, key: string): Sourced<T> => ({ value, source: 'measured', ref: refs[key] });
  const fallbacks: string[] = [];
  const take = <T>(key: string, value: T | undefined, derived: Sourced<T>, label: string): Sourced<T> => {
    if (value === undefined) {
      fallbacks.push(label);
      return derived;
    }
    return m(value, key);
  };

  const heatedSf = take('heated_sf', num(payload.heated_sf), d.heatedSf, 'Heated area');
  const stories = take(
    'stories',
    num(payload.stories) !== undefined ? profile.stories : undefined,
    d.stories,
    'Stories'
  );

  const fpW = num(payload.footprint?.width_ft);
  const fpD = num(payload.footprint?.depth_ft);
  const footprintSf = take('footprint_sf', num(payload.footprint_sf) ?? (fpW && fpD ? fpW * fpD : undefined), d.footprintSf, 'Footprint');
  const perimeterLf = take('footprint_sf', num(payload.perimeter_lf) ?? (fpW && fpD ? 2 * (fpW + fpD) : undefined), d.perimeterLf, 'Perimeter');
  const sides: Sourced<{ longFt: number; shortFt: number }> =
    fpW && fpD ? m({ longFt: Math.max(fpW, fpD), shortFt: Math.min(fpW, fpD) }, 'footprint_sf') : d.sides;

  const wallHeightFt = take('wall_height_ft', num(payload.wall_height_ft), d.wallHeightFt, 'Wall height');
  const extWallLf = take('ext_wall_lf', num(payload.ext_wall_lf), d.extWallLf, 'Exterior wall length');
  const intWallLf = take('int_wall_lf', num(payload.int_wall_lf), d.intWallLf, 'Interior wall length');
  const extWallAreaSf: Sourced<number> =
    num(payload.ext_wall_area_sf) !== undefined
      ? m(num(payload.ext_wall_area_sf) as number, 'ext_wall_lf')
      : extWallLf.source === 'measured'
        ? m(extWallLf.value * wallHeightFt.value, 'ext_wall_lf')
        : d.extWallAreaSf;

  const o = payload.openings;
  const extraAssumed: string[] = [];
  let extDoors = num(o?.ext_doors);
  if (extDoors !== undefined && extDoors > EXT_DOORS_SANE_MAX) {
    // A read that tags most doors "exterior" would price a dozen entry doors; a house
    // carries a handful. Price the derived count and say so.
    extraAssumed.push(
      `Exterior doors: the read counted ${extDoors}, more than a house carries, so ${d.openings.value.extDoors} are priced; the review at StudTally settles which doors are exterior.`
    );
    extDoors = undefined;
  }
  const openings: Sourced<Geometry['openings']['value']> = o
    ? m(
        {
          windows: num(o.windows) ?? d.openings.value.windows,
          windowAreaSf: num(o.window_area_sf) ?? (num(o.windows) ?? d.openings.value.windows) * 15,
          extDoors: extDoors ?? d.openings.value.extDoors,
          garageDoors: num(o.garage_doors) ?? d.openings.value.garageDoors,
        },
        'openings'
      )
    : (fallbacks.push('Windows and doors'), d.openings);

  const r = payload.rooms;
  const rooms: Sourced<Geometry['rooms']['value']> = r
    ? m(
        {
          count: num(r.count) ?? d.rooms.value.count,
          baths: num(r.baths) ?? d.rooms.value.baths,
          kitchens: num(r.kitchens) ?? d.rooms.value.kitchens,
          bedrooms: num(r.bedrooms) ?? d.rooms.value.bedrooms,
        },
        'rooms'
      )
    : (fallbacks.push('Rooms'), d.rooms);

  const pr = payload.roof;
  const complexity = roofComplexity(pr) ?? d.roof.value.complexity;
  const roof: Sourced<Roof> = pr
    ? m(
        {
          planeAreaSf: num(pr.plane_area_sf) ?? d.roof.value.planeAreaSf,
          pitch: num(pr.pitch) ?? d.roof.value.pitch,
          ridgeLf: num(pr.ridge_lf) ?? d.roof.value.ridgeLf,
          hipValleyLf: num(pr.hip_valley_lf) ?? d.roof.value.hipValleyLf,
          eaveLf: num(pr.eave_lf) ?? d.roof.value.eaveLf,
          rakeLf: complexity === 'gable' ? d.roof.value.rakeLf : 0,
          framing: pr.framing === 'stick' || pr.framing === 'truss' ? pr.framing : d.roof.value.framing,
          complexity,
        },
        'roof'
      )
    : (fallbacks.push('Roof'), d.roof);

  const foundationValue = payload.foundation ? FOUNDATION_FROM_STUDTALLY[payload.foundation] : undefined;
  const foundation = take('foundation', foundationValue, d.foundation, 'Foundation type');

  const framedFloorSf = take('framed_floor_sf', num(payload.framed_floor_sf), d.framedFloorSf, 'Framed floor area');

  // No garage door on a measured plan means no garage, whatever the size rule says.
  const garageMeasured = num(payload.garage_sf);
  const garageSf: Sourced<number> =
    garageMeasured !== undefined
      ? m(garageMeasured, 'unheated_sf')
      : openings.source === 'measured' && openings.value.garageDoors === 0
        ? { value: 0, source: 'derived' }
        : d.garageSf;
  const unheatedSf = take('unheated_sf', num(payload.unheated_sf), garageSf.value === d.garageSf.value ? d.unheatedSf : { value: garageSf.value + 120, source: 'derived' }, 'Unheated area');

  const p = payload.porches;
  const porches: Sourced<Geometry['porches']['value']> = p
    ? m({ count: num(p.count) ?? d.porches.value.count, posts: num(p.posts) ?? d.porches.value.posts }, 'porches')
    : (fallbacks.push('Porches'), d.porches);

  const assumed = [
    ...(payload.assumed ?? []),
    ...extraAssumed,
    ...fallbacks.map((f) => `${f}: not read from the plans, so derived from the measured size by the free estimate's rule.`),
  ];

  return {
    heatedSf,
    stories,
    footprintSf,
    perimeterLf,
    sides,
    wallHeightFt,
    extWallLf,
    intWallLf,
    extWallAreaSf,
    openings,
    rooms,
    roof,
    foundation,
    framedFloorSf,
    unheatedSf,
    garageSf,
    porches,
    assumed,
  };
}

/** "2589-S_Thompson_-_Final_Set_09_23_21" → "2589-S Thompson - Final Set 09 23 21". */
export function humanizePlanName(name: string): string {
  return name.replace(/[_]+/g, ' ').replace(/\s+/g, ' ').trim();
}

/** The title a read gets: the plan's name when it reads as one, else a plain phrase. */
export function planTitle(name: string | undefined): string {
  const clean = name ? humanizePlanName(name) : '';
  return clean && clean.length <= 28 ? `${clean}, costed.` : 'Your plans, costed.';
}

const fmt = (n: number, digits = 0) =>
  n.toLocaleString('en-US', { maximumFractionDigits: digits, minimumFractionDigits: 0 });

function feetInches(ft: number): string {
  const whole = Math.floor(ft);
  const inches = Math.round((ft - whole) * 12);
  if (inches === 12) return `${whole + 1} ft`;
  return inches ? `${whole} ft ${inches} in` : `${whole} ft`;
}

/** The facts list for the rail: what was read, each with its sheet. */
export function measuredFacts(g: Geometry): MeasuredFact[] {
  const facts: MeasuredFact[] = [];
  if (g.heatedSf.source === 'measured') {
    facts.push({
      text: `${fmt(g.heatedSf.value)} sq ft heated, ${g.stories.value === 1 ? 'one story' : `${g.stories.value} stories`}`,
      ref: g.heatedSf.ref,
    });
  }
  if (g.sides.source === 'measured') {
    facts.push({ text: `Footprint ${feetInches(g.sides.value.longFt)} by ${feetInches(g.sides.value.shortFt)}`, ref: g.sides.ref });
  } else if (g.footprintSf.source === 'measured') {
    facts.push({ text: `Footprint ${fmt(g.footprintSf.value)} sq ft`, ref: g.footprintSf.ref });
  }
  if (g.extWallLf.source === 'measured') {
    facts.push({
      text: `Exterior walls, ${fmt(g.extWallLf.value)} lf${g.wallHeightFt.source === 'measured' ? ` at ${fmt(g.wallHeightFt.value, 1)} ft` : ''}`,
      ref: g.extWallLf.ref,
    });
  }
  if (g.openings.source === 'measured') {
    const o = g.openings.value;
    facts.push({
      text: `${fmt(o.windows)} windows, ${fmt(o.extDoors)} exterior doors${o.garageDoors ? `, ${fmt(o.garageDoors)} garage` : ''}`,
      ref: g.openings.ref,
    });
  }
  if (g.roof.source === 'measured') {
    const r = g.roof.value;
    facts.push({
      text: `Roof, ${fmt(r.planeAreaSf / 100)} squares at ${fmt(r.pitch, 1)} in 12${r.framing !== 'unknown' ? `, ${r.framing === 'stick' ? 'stick framed' : 'trussed'}` : ''}`,
      ref: g.roof.ref,
    });
  }
  if (g.rooms.source === 'measured') {
    const r = g.rooms.value;
    facts.push({ text: `${fmt(r.count)} rooms, ${fmt(r.baths, 1)} baths, ${fmt(r.bedrooms)} bedrooms`, ref: g.rooms.ref });
  }
  if (g.foundation.source === 'measured') {
    facts.push({
      text: `${FOUNDATION_LABEL[g.foundation.value][0].toUpperCase()}${FOUNDATION_LABEL[g.foundation.value].slice(1)} foundation`,
      ref: g.foundation.ref,
      you: !g.foundation.ref,
    });
  }
  return facts;
}

/** "A-2" → "sheet A-2", "3" → "sheet 3"; a ref that already says "sheet" is left alone. */
export function sheetLabel(ref: string): string {
  return /^sheet\b/i.test(ref.trim()) ? ref.trim() : `sheet ${ref.trim()}`;
}

/** True when the geometry came from a plan read rather than the profile. */
export function isMeasured(g: Geometry): boolean {
  return Object.values(g).some((v) => typeof v === 'object' && v !== null && 'source' in v && v.source === 'measured');
}
