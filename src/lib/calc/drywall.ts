import { CalcLine, CalcResult, clamp, totalCosts } from './types';

/**
 * Drywall takeoff — sheets, joint compound, tape, and screws.
 *
 * Two modes:
 * - 'room': exact takeoff from room dimensions. Wall area = perimeter ×
 *   height, ceiling optional, minus a 10% openings allowance (doors,
 *   windows, closets openings).
 * - 'house': whole-house heuristic. Finished drywall area ≈ 3.7 × floor
 *   area for typical stick-built layouts (interior partitions have two
 *   faces, exterior walls one interior face, plus ceilings). The classic
 *   estimator range is 3.5–4.0; 3.7 is the midpoint.
 *
 * Consumables per 1,000 sq ft of board (standard finishing rules):
 * - Joint compound: ~140 lb ≈ 2.3 buckets of 4.5-gal (61.5 lb) all-purpose.
 *   We carry 1 bucket per 450 sq ft.
 * - Tape: ~370 ft → one 500-ft roll per 1,350 sq ft.
 * - Screws: ~1 per sq ft → one 1-lb box (~200 screws of #6 1¼") per
 *   200 sq ft.
 *
 * 2026 price ranges: 1/2" 4×8 $12–$18, 4×12 $17–$26; compound bucket
 * $17–$24; tape roll $5–$9; screws $7–$10/lb.
 */

export interface DrywallInputs {
  mode: 'room' | 'house';
  // room mode
  roomLengthFt: number;
  roomWidthFt: number;
  ceilingHeightFt: number;
  includeCeiling: boolean;
  // house mode
  floorAreaSqFt: number;
  // both
  sheetSize: '4x8' | '4x12';
}

const SHEET_AREA: Record<'4x8' | '4x12', number> = { '4x8': 32, '4x12': 48 };
const SHEET_PRICE: Record<'4x8' | '4x12', [number, number]> = {
  '4x8': [12, 18],
  '4x12': [17, 26],
};
const MUD_BUCKET_PRICE: [number, number] = [17, 24];
const TAPE_ROLL_PRICE: [number, number] = [5, 9];
const SCREW_BOX_PRICE: [number, number] = [7, 10];

export function calculateDrywall(raw: DrywallInputs): CalcResult {
  let area: number;
  let areaDetail: string;

  if (raw.mode === 'room') {
    const l = clamp(raw.roomLengthFt, 3, 100);
    const w = clamp(raw.roomWidthFt, 3, 100);
    const h = clamp(raw.ceilingHeightFt, 7, 20);
    const wallArea = 2 * (l + w) * h * 0.9; // 10% openings allowance
    const ceilingArea = raw.includeCeiling ? l * w : 0;
    area = wallArea + ceilingArea;
    areaDetail = `${Math.round(wallArea)} sq ft walls${raw.includeCeiling ? ` + ${Math.round(ceilingArea)} sq ft ceiling` : ''}`;
  } else {
    const floor = clamp(raw.floorAreaSqFt, 100, 20000);
    area = floor * 3.7;
    areaDetail = `${Math.round(floor).toLocaleString('en-US')} sq ft floor × 3.7 (walls + ceilings heuristic)`;
  }

  const sheetArea = SHEET_AREA[raw.sheetSize];
  const sheets = Math.ceil((area / sheetArea) * 1.1); // 10% cut waste
  const mudBuckets = Math.max(1, Math.ceil(area / 450));
  const tapeRolls = Math.max(1, Math.ceil(area / 1350));
  const screwBoxes = Math.max(1, Math.ceil(area / 200));

  const sheetPrice = SHEET_PRICE[raw.sheetSize];
  const lines: CalcLine[] = [
    {
      id: 'sheets',
      label: 'Drywall sheets',
      qty: sheets,
      unit: 'sheets',
      detail: `1/2" × ${raw.sheetSize === '4x8' ? '4×8' : '4×12'} — 10% cut waste included`,
      costLow: Math.round(sheets * sheetPrice[0]),
      costHigh: Math.round(sheets * sheetPrice[1]),
    },
    {
      id: 'mud',
      label: 'Joint compound',
      qty: mudBuckets,
      unit: 'buckets',
      detail: '4.5-gal all-purpose — one bucket finishes ≈ 450 sq ft of board',
      costLow: Math.round(mudBuckets * MUD_BUCKET_PRICE[0]),
      costHigh: Math.round(mudBuckets * MUD_BUCKET_PRICE[1]),
    },
    {
      id: 'tape',
      label: 'Joint tape',
      qty: tapeRolls,
      unit: 'rolls',
      detail: '500-ft paper roll — ≈ 370 ft of seams per 1,000 sq ft',
      costLow: Math.round(tapeRolls * TAPE_ROLL_PRICE[0]),
      costHigh: Math.round(tapeRolls * TAPE_ROLL_PRICE[1]),
    },
    {
      id: 'screws',
      label: 'Drywall screws',
      qty: screwBoxes,
      unit: 'lb boxes',
      detail: '#6 × 1¼" coarse — roughly one screw per square foot of board',
      costLow: Math.round(screwBoxes * SCREW_BOX_PRICE[0]),
      costHigh: Math.round(screwBoxes * SCREW_BOX_PRICE[1]),
    },
  ];

  const totals = totalCosts(lines);

  return {
    hero: {
      qty: sheets,
      unit: 'sheets',
      label: 'Drywall sheets',
      detail: areaDetail,
    },
    lines,
    ...totals,
    notes: [
      raw.mode === 'room'
        ? 'Room walls carry a 10% openings allowance for doors and windows.'
        : 'Whole-house mode is a planning heuristic — run rooms individually before ordering.',
      'Hang ceilings before walls; use 5/8" board on garage ceilings where code requires it.',
      'Material cost only. No labor, corner bead, or texture.',
    ],
  };
}
