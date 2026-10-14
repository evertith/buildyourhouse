/**
 * The one shared geometry object.
 *
 * A profile (square footage, stories, finish, foundation, state, roof) derives
 * a synthetic Geometry with the rules below; a StudTally plan read produces a
 * measured one. Every phase module downstream is identical: it never knows
 * which it got, and every field says where it came from.
 */

import type { Source } from './types.ts';
import { clamp, roundTo } from './types.ts';
import type { Finish } from './prices.ts';

export interface Sourced<T> {
  value: T;
  source: Source;
  /** Sheet reference for a measured value: "A-2". */
  ref?: string;
}

export type Stories = 1 | 2 | 3;
export type Foundation = 'slab' | 'crawl' | 'basement';
export type RoofComplexity = 'gable' | 'hip' | 'cutup';
export type WallHeight = 8 | 9 | 10;

export interface Profile {
  heatedSf: number;
  stories: Stories;
  finish: Finish;
  foundation: Foundation;
  /** Two-letter state code. */
  state: string;
  roof: RoofComplexity;
  wallHeightFt: WallHeight;
}

export const PROFILE_DEFAULTS: Profile = {
  heatedSf: 2000,
  stories: 1,
  finish: 'standard',
  foundation: 'slab',
  state: 'NC',
  roof: 'hip',
  wallHeightFt: 9,
};

export const HEATED_SF_MIN = 500;
export const HEATED_SF_MAX = 10000;

export interface Openings {
  windows: number;
  windowAreaSf: number;
  extDoors: number;
  garageDoors: number;
}

export interface Rooms {
  count: number;
  baths: number;
  kitchens: number;
  bedrooms: number;
}

export interface Roof {
  /** Plan (horizontal) area under the roof, including overhangs. */
  planeAreaSf: number;
  /** Rise in 12. */
  pitch: number;
  ridgeLf: number;
  hipValleyLf: number;
  eaveLf: number;
  rakeLf: number;
  framing: 'stick' | 'truss' | 'unknown';
  complexity: RoofComplexity;
}

export interface Porches {
  count: number;
  posts: number;
}

export interface Geometry {
  heatedSf: Sourced<number>;
  stories: Sourced<Stories>;
  footprintSf: Sourced<number>;
  perimeterLf: Sourced<number>;
  /** Long and short sides of the equivalent rectangle. */
  sides: Sourced<{ longFt: number; shortFt: number }>;
  wallHeightFt: Sourced<number>;
  /** Sum of exterior walls, all stories, garage walls included. */
  extWallLf: Sourced<number>;
  intWallLf: Sourced<number>;
  /** Gross exterior wall area before openings. */
  extWallAreaSf: Sourced<number>;
  openings: Sourced<Openings>;
  rooms: Sourced<Rooms>;
  roof: Sourced<Roof>;
  foundation: Sourced<Foundation>;
  /** Framed (wood) floor area: raised first floors plus every upper floor. */
  framedFloorSf: Sourced<number>;
  /** Under roof but not heated: garage, porches. */
  unheatedSf: Sourced<number>;
  garageSf: Sourced<number>;
  porches: Sourced<Porches>;
  /** Plain-language list of what was assumed. */
  assumed: string[];
}

const derived = <T>(value: T): Sourced<T> => ({ value, source: 'derived' });
const user = <T>(value: T): Sourced<T> => ({ value, source: 'user' });

export const ROOF_LABEL: Record<RoofComplexity, string> = {
  gable: 'simple gable',
  hip: 'hip or mixed',
  cutup: 'cut-up with valleys',
};

export const FOUNDATION_LABEL: Record<Foundation, string> = {
  slab: 'slab',
  crawl: 'crawl space',
  basement: 'basement',
};

/** A square-footage profile becomes a full geometry by rules stated on the page. */
export function deriveGeometry(raw: Profile): Geometry {
  const heatedSf = roundTo(clamp(raw.heatedSf, HEATED_SF_MIN, HEATED_SF_MAX));
  const stories = clamp(raw.stories, 1, 3) as Stories;
  const wallHeightFt = raw.wallHeightFt;

  // Footprint = heated ÷ stories, treated as a 1.5:1 rectangle for walls.
  const footprintSf = heatedSf / stories;
  const shortFt = Math.sqrt(footprintSf / 1.5);
  const longFt = footprintSf / shortFt;
  const perimeterLf = 2 * (shortFt + longFt);

  // Openings and rooms by density rules.
  const windows = Math.max(4, Math.round(heatedSf / 110));
  const windowAreaSf = windows * 15;
  const extDoors = 3;
  const garageDoors = heatedSf >= 1400 ? 1 : 0;
  const garageSf = garageDoors ? 440 : 0;
  const porchSf = 120;
  const porches: Porches = { count: 1, posts: 4 };
  const unheatedSf = garageSf + porchSf;

  const roomCount = Math.max(4, Math.round(heatedSf / 170));
  const baths = heatedSf < 1800 ? 2 : heatedSf <= 2600 ? 2.5 : 3;
  const bedrooms = clamp(Math.round(heatedSf / 650), 2, 5);

  // Walls. The garage adds three exterior walls of its own (one is shared).
  const garageWallLf = garageDoors ? 60 : 0;
  const extWallLf = perimeterLf * stories + garageWallLf;
  const intWallLf = heatedSf / 4;
  const extWallAreaSf = extWallLf * wallHeightFt;

  // Roof: plan area under roof, 1-ft overhangs, pitch 6:12.
  const underRoofSf = footprintSf + garageSf + porchSf;
  const planeAreaSf = underRoofSf * 1.08;
  const roofPerimeterLf = perimeterLf * 1.1 + (garageDoors ? 44 : 0);
  const roof: Roof = {
    planeAreaSf,
    pitch: 6,
    ridgeLf: longFt + (garageDoors ? 11 : 0),
    hipValleyLf:
      raw.roof === 'gable' ? 0 : raw.roof === 'hip' ? 1.2 * shortFt : 2.4 * shortFt,
    eaveLf: raw.roof === 'gable' ? roofPerimeterLf * 0.55 : roofPerimeterLf,
    rakeLf: raw.roof === 'gable' ? roofPerimeterLf * 0.45 * 1.12 : 0,
    framing: 'truss',
    complexity: raw.roof,
  };

  // Floors: a slab carries the first floor on concrete; every upper floor is framed.
  const raisedFirst = raw.foundation === 'slab' ? 0 : footprintSf;
  const framedFloorSf = raisedFirst + (stories - 1) * footprintSf;

  const assumed = [
    `Footprint of ${fmt(footprintSf)} sq ft (heated area ÷ ${stories === 1 ? 'one story' : `${stories} stories`}), as a 1.5:1 rectangle about ${fmt(longFt)} by ${fmt(shortFt)} ft.`,
    `${wallHeightFt}-ft walls; interior partitions at 1 linear foot per 4 sq ft of floor (${fmt(intWallLf)} lf).`,
    `${windows} windows at 15 sq ft each (one per 110 sq ft), ${extDoors} exterior doors${garageDoors ? ', a two-car garage with one 16-ft door' : ', no garage'}.`,
    `${roomCount} rooms, ${baths} baths, ${bedrooms} bedrooms, one kitchen, one laundry.`,
    `${ROOF_LABEL[raw.roof][0].toUpperCase()}${ROOF_LABEL[raw.roof].slice(1)} roof at 6:12 with 1-ft overhangs, trussed.`,
    raw.foundation === 'slab'
      ? 'Monolithic slab with turned-down footings under the house and garage.'
      : raw.foundation === 'crawl'
        ? 'Crawl space: continuous footing, 3-ft block stem wall, piers every 200 sq ft, framed first floor.'
        : 'Full basement: 8-ft poured walls on footings, slab floor, waterproofed and drained, framed first floor.',
    'One front porch, 120 sq ft, on four posts.',
  ];

  return {
    heatedSf: user(heatedSf),
    stories: user(stories),
    footprintSf: derived(footprintSf),
    perimeterLf: derived(perimeterLf),
    sides: derived({ longFt, shortFt }),
    wallHeightFt: user(wallHeightFt),
    extWallLf: derived(extWallLf),
    intWallLf: derived(intWallLf),
    extWallAreaSf: derived(extWallAreaSf),
    openings: derived({ windows, windowAreaSf, extDoors, garageDoors }),
    rooms: derived({ count: roomCount, baths, kitchens: 1, bedrooms }),
    roof: derived(roof),
    foundation: user(raw.foundation),
    framedFloorSf: derived(framedFloorSf),
    unheatedSf: derived(unheatedSf),
    garageSf: derived(garageSf),
    porches: derived(porches),
    assumed,
  };
}

function fmt(n: number): string {
  return Math.round(n).toLocaleString('en-US');
}
