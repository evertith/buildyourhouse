import { CalcLine, CalcResult, clamp, totalCosts } from './types';

/**
 * Interior paint takeoff — wall/ceiling/trim gallons and primer.
 *
 * Coverage: 350 sq ft per gallon per coat on smooth drywall (the number on
 * every can; textured surfaces run 25% lower and the page says so).
 *
 * Modes:
 * - 'room': perimeter × height minus 21 sq ft per door and 15 per window.
 * - 'house': paintable wall area ≈ 2.7 × floor area (industry heuristic
 *   for whole-interior repaints of typical layouts).
 *
 * Trim: ≈ 0.5 gal per room-equivalent (≈ every 150 sq ft of floor) per
 * coat, bought in quarts/gallons of enamel.
 *
 * 2026 prices: quality interior latex $38–$65/gal; PVA drywall primer
 * $18–$28/gal; trim enamel $45–$70/gal.
 */

export interface PaintInputs {
  mode: 'room' | 'house';
  // room mode
  roomLengthFt: number;
  roomWidthFt: number;
  ceilingHeightFt: number;
  doors: number;
  windows: number;
  // house mode
  floorAreaSqFt: number;
  // both
  coats: 1 | 2;
  includeCeilings: boolean;
  includeTrim: boolean;
  newDrywall: boolean; // primer required
}

const COVERAGE = 350; // sq ft per gallon per coat
const WALL_PAINT_PRICE: [number, number] = [38, 65];
const PRIMER_PRICE: [number, number] = [18, 28];
const TRIM_PAINT_PRICE: [number, number] = [45, 70];

export function calculatePaint(raw: PaintInputs): CalcResult {
  let wallArea: number;
  let ceilingArea: number;
  let floorEquivalent: number;
  let areaDetail: string;

  if (raw.mode === 'room') {
    const l = clamp(raw.roomLengthFt, 3, 100);
    const w = clamp(raw.roomWidthFt, 3, 100);
    const h = clamp(raw.ceilingHeightFt, 7, 20);
    const doors = clamp(raw.doors, 0, 20);
    const windows = clamp(raw.windows, 0, 40);
    wallArea = Math.max(0, 2 * (l + w) * h - doors * 21 - windows * 15);
    ceilingArea = raw.includeCeilings ? l * w : 0;
    floorEquivalent = l * w;
    areaDetail = `${Math.round(wallArea)} sq ft of wall after ${doors} door${doors === 1 ? '' : 's'} and ${windows} window${windows === 1 ? '' : 's'}`;
  } else {
    const floor = clamp(raw.floorAreaSqFt, 100, 20000);
    wallArea = floor * 2.7;
    ceilingArea = raw.includeCeilings ? floor : 0;
    floorEquivalent = floor;
    areaDetail = `${Math.round(wallArea).toLocaleString('en-US')} sq ft paintable wall (2.7 × floor area)`;
  }

  const wallGallons = Math.ceil((wallArea * raw.coats) / COVERAGE);
  const ceilingGallons = ceilingArea > 0 ? Math.ceil((ceilingArea * raw.coats) / COVERAGE) : 0;
  const primerGallons = raw.newDrywall
    ? Math.ceil((wallArea + ceilingArea) / (COVERAGE * 0.85)) // primer spreads slightly worse on bare board
    : 0;
  const trimGallons = raw.includeTrim
    ? Math.max(1, Math.round(((floorEquivalent / 150) * 0.5 * raw.coats) * 2) / 2)
    : 0;

  const lines: CalcLine[] = [
    {
      id: 'wall-paint',
      label: 'Wall paint',
      qty: wallGallons,
      unit: 'gallons',
      detail: `${raw.coats} coat${raw.coats === 1 ? '' : 's'} at 350 sq ft/gal`,
      costLow: Math.round(wallGallons * WALL_PAINT_PRICE[0]),
      costHigh: Math.round(wallGallons * WALL_PAINT_PRICE[1]),
    },
  ];

  if (ceilingGallons > 0) {
    lines.push({
      id: 'ceiling-paint',
      label: 'Ceiling paint',
      qty: ceilingGallons,
      unit: 'gallons',
      detail: `Flat ceiling white, ${raw.coats} coat${raw.coats === 1 ? '' : 's'}`,
      costLow: Math.round(ceilingGallons * WALL_PAINT_PRICE[0]),
      costHigh: Math.round(ceilingGallons * WALL_PAINT_PRICE[1]),
    });
  }
  if (primerGallons > 0) {
    lines.push({
      id: 'primer',
      label: 'Drywall primer',
      qty: primerGallons,
      unit: 'gallons',
      detail: 'PVA primer, one coat on new board — non-negotiable on fresh drywall',
      costLow: Math.round(primerGallons * PRIMER_PRICE[0]),
      costHigh: Math.round(primerGallons * PRIMER_PRICE[1]),
    });
  }
  if (trimGallons > 0) {
    lines.push({
      id: 'trim',
      label: 'Trim enamel',
      qty: trimGallons,
      unit: 'gallons',
      detail: 'Semi-gloss for doors, casing, and base',
      costLow: Math.round(trimGallons * TRIM_PAINT_PRICE[0]),
      costHigh: Math.round(trimGallons * TRIM_PAINT_PRICE[1]),
    });
  }

  const totals = totalCosts(lines);
  const totalGallons = wallGallons + ceilingGallons + primerGallons + trimGallons;

  return {
    hero: {
      qty: totalGallons,
      unit: 'gallons',
      label: 'Total paint & primer',
      detail: areaDetail,
    },
    lines,
    ...totals,
    notes: [
      'Coverage assumes smooth drywall — textured walls drink ~25% more.',
      'Two coats is the honest default for color changes and new drywall.',
      'Material cost only. Brushes, rollers, tape, and drop cloths add $50–$150 for a first-time setup.',
    ],
  };
}
