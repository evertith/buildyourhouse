import { CalcLine, CalcResult, clamp, totalCosts } from './types';

/**
 * Wall-framing lumber takeoff: studs, plates, headers allowance, and
 * exterior sheathing for a rectangular footprint. Scope is WALLS ONLY —
 * floor systems and roof framing are separate trades (and the whole-house
 * material estimator covers them at the rule-of-thumb level).
 *
 * Estimating conventions used (each stated on the page):
 * - Studs: one stud per linear foot of wall at 16" OC. The nominal spacing
 *   yields 0.75/lf; the industry shortcut of 1.0/lf absorbs corners,
 *   T-intersections, jack/king studs at openings, and blocking. At 24" OC
 *   the same logic lands at 0.75/lf.
 * - Plates: three runs (single bottom + double top) of plate stock per
 *   wall, bought as 16 ft lengths with 5% cut waste.
 * - Interior walls: 1 linear foot per 4 sq ft of floor area — the same
 *   heuristic the whole-house estimator uses, typical of stick-built
 *   single-family layouts.
 * - Sheathing: 4×8 OSB on exterior wall area with 10% waste.
 *
 * 2026 material price ranges (big-box, national): precut SPF 2×4 stud
 * $3.20–$4.80, 2×4×16 plate stock $8.50–$13, 2×6 ≈ 1.55× the 2×4 price,
 * 7/16" OSB $16–$28/sheet. Regional swing is the reason for ranges.
 */

export interface FramingInputs {
  lengthFt: number;
  widthFt: number;
  stories: 1 | 2 | 3;
  wallHeightFt: 8 | 9 | 10;
  studSpacing: 16 | 24;
  studSize: '2x4' | '2x6';
  includeInterior: boolean;
}

export interface FramingResult extends CalcResult {
  exteriorWallLf: number;
  interiorWallLf: number;
  sheathingArea: number;
}

const STUD_PRICE: Record<'2x4' | '2x6', [number, number]> = {
  '2x4': [3.2, 4.8],
  '2x6': [5.0, 7.4],
};
const PLATE_16FT_PRICE: Record<'2x4' | '2x6', [number, number]> = {
  '2x4': [8.5, 13.0],
  '2x6': [13.0, 20.0],
};
const OSB_SHEET_PRICE: [number, number] = [16, 28];
// One opening (door or window) per ~120 sq ft of floor is a typical
// single-family density; each opening needs header stock ≈ 6 lf of doubled
// 2×10 (~10 bf). Priced via 2x10x8 boards.
const HEADER_BOARD_PRICE: [number, number] = [9, 14];

export function calculateFraming(raw: FramingInputs): FramingResult {
  const lengthFt = clamp(raw.lengthFt, 8, 300);
  const widthFt = clamp(raw.widthFt, 8, 300);
  const stories = clamp(raw.stories, 1, 3) as 1 | 2 | 3;
  const wallHeightFt = raw.wallHeightFt;
  const studsPerLf = raw.studSpacing === 16 ? 1.0 : 0.75;

  const footprint = lengthFt * widthFt;
  const perimeter = 2 * (lengthFt + widthFt);

  const exteriorWallLf = perimeter * stories;
  const interiorWallLf = raw.includeInterior ? (footprint * stories) / 4 : 0;
  const totalWallLf = exteriorWallLf + interiorWallLf;

  // Studs — taller walls need longer studs but not more of them; count is
  // driven by wall length. Interior partitions framed 2×4 regardless of
  // exterior stud size.
  const exteriorStuds = Math.ceil(exteriorWallLf * studsPerLf);
  const interiorStuds = Math.ceil(interiorWallLf * studsPerLf);

  // Plates: 3 runs × wall lf, in 16-ft sticks, +5% cut waste.
  const plateLf = totalWallLf * 3 * 1.05;
  const plateBoards = Math.ceil(plateLf / 16);

  // Headers: one opening per ~120 sq ft, one 8-ft board of 2×10 each
  // (doubled header for a 3-ft opening ≈ 6.5 lf).
  const openings = Math.max(4, Math.round((footprint * stories) / 120));
  const headerBoards = openings;

  // Sheathing: exterior wall surface only, 4×8 sheets, 10% waste.
  const sheathingArea = perimeter * wallHeightFt * stories;
  const sheathingSheets = Math.ceil((sheathingArea / 32) * 1.1);

  const studPrice = STUD_PRICE[raw.studSize];
  const platePrice = PLATE_16FT_PRICE[raw.studSize];

  const lines: CalcLine[] = [
    {
      id: 'exterior-studs',
      label: 'Exterior wall studs',
      qty: exteriorStuds,
      unit: 'studs',
      detail: `${raw.studSize === '2x4' ? '2×4' : '2×6'} × ${wallHeightFt === 8 ? '92⅝" precut' : wallHeightFt === 9 ? '104⅝" precut' : '116⅝" precut'}, ${raw.studSpacing}" OC — corners, openings, and blocking included`,
      costLow: Math.round(exteriorStuds * studPrice[0]),
      costHigh: Math.round(exteriorStuds * studPrice[1]),
    },
    ...(interiorStuds > 0
      ? [
          {
            id: 'interior-studs',
            label: 'Interior partition studs',
            qty: interiorStuds,
            unit: 'studs',
            detail: `2×4 precut, ${raw.studSpacing}" OC`,
            costLow: Math.round(interiorStuds * STUD_PRICE['2x4'][0]),
            costHigh: Math.round(interiorStuds * STUD_PRICE['2x4'][1]),
          },
        ]
      : []),
    {
      id: 'plates',
      label: 'Plate stock',
      qty: plateBoards,
      unit: 'boards',
      detail: `${raw.studSize === '2x4' ? '2×4' : '2×6'} × 16 ft — single bottom plate, doubled top plate, 5% cut waste`,
      costLow: Math.round(plateBoards * platePrice[0]),
      costHigh: Math.round(plateBoards * platePrice[1]),
    },
    {
      id: 'headers',
      label: 'Header stock',
      qty: headerBoards,
      unit: 'boards',
      detail: '2×10 × 8 ft — one doubled header per door/window opening (1 per ~120 sq ft)',
      costLow: Math.round(headerBoards * HEADER_BOARD_PRICE[0]),
      costHigh: Math.round(headerBoards * HEADER_BOARD_PRICE[1]),
    },
    {
      id: 'sheathing',
      label: 'Wall sheathing',
      qty: sheathingSheets,
      unit: 'sheets',
      detail: '7/16" OSB, 4×8 — exterior walls, 10% waste',
      costLow: Math.round(sheathingSheets * OSB_SHEET_PRICE[0]),
      costHigh: Math.round(sheathingSheets * OSB_SHEET_PRICE[1]),
    },
  ];

  const totals = totalCosts(lines);
  const totalStuds = exteriorStuds + interiorStuds;

  return {
    hero: {
      qty: totalStuds,
      unit: 'studs',
      label: 'Total studs',
      detail: `${formatWallLf(totalWallLf)} lf of wall at ${raw.studSpacing}" on-center`,
    },
    lines,
    ...totals,
    notes: [
      'Wall framing only — floor joists, beams, and roof framing are separate takeoffs.',
      'Stud counts use the 1-per-lf (16" OC) estimating shortcut, which absorbs corners, jacks, kings, and blocking.',
      'Material cost only. No labor, fasteners, or delivery.',
    ],
    exteriorWallLf: Math.round(exteriorWallLf),
    interiorWallLf: Math.round(interiorWallLf),
    sheathingArea: Math.round(sheathingArea),
  };
}

function formatWallLf(lf: number): string {
  return new Intl.NumberFormat('en-US', { maximumFractionDigits: 0 }).format(lf);
}
