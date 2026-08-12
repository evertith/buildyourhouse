import { CalcLine, CalcResult, clamp, totalCosts } from './types';

/**
 * Flooring takeoff — square footage with waste, boxes, and underlayment.
 *
 * Waste factors (straight lay): plank materials 8%, tile 10%, carpet 10%
 * (seam/roll-width waste). Diagonal or herringbone layouts add 5 points —
 * the classic reason DIY orders come up short.
 *
 * Box coverage defaults (typical 2026 retail): LVP 23 sq ft, laminate
 * 20 sq ft, hardwood 22 sq ft, tile 15 sq ft. Carpet sells by the sq yd
 * from 12-ft rolls.
 *
 * 2026 material prices per sq ft: LVP $2–$5, laminate $1.50–$4, engineered
 * hardwood $4–$8, solid hardwood $5–$10, ceramic tile $2–$6, carpet+pad
 * $3–$7.
 */

export type FlooringMaterial = 'lvp' | 'laminate' | 'engineered' | 'hardwood' | 'tile' | 'carpet';

export interface FlooringInputs {
  areaSqFt: number;
  material: FlooringMaterial;
  layout: 'straight' | 'diagonal';
  needsUnderlayment: boolean;
}

const MATERIAL_META: Record<
  FlooringMaterial,
  { label: string; boxCoverage: number | null; waste: number; price: [number, number]; detail: string }
> = {
  lvp: { label: 'Luxury vinyl plank', boxCoverage: 23, waste: 0.08, price: [2, 5], detail: 'Click-lock LVP, ~23 sq ft per box' },
  laminate: { label: 'Laminate', boxCoverage: 20, waste: 0.08, price: [1.5, 4], detail: 'AC4 laminate, ~20 sq ft per box' },
  engineered: { label: 'Engineered hardwood', boxCoverage: 22, waste: 0.08, price: [4, 8], detail: '~22 sq ft per box' },
  hardwood: { label: 'Solid hardwood', boxCoverage: 22, waste: 0.1, price: [5, 10], detail: '3/4" solid, ~22 sq ft per bundle' },
  tile: { label: 'Tile', boxCoverage: 15, waste: 0.1, price: [2, 6], detail: 'Ceramic/porcelain, ~15 sq ft per box' },
  carpet: { label: 'Carpet + pad', boxCoverage: null, waste: 0.1, price: [3, 7], detail: 'From 12-ft roll, seams planned' },
};

const UNDERLAYMENT_ROLL = { coverage: 100, price: [45, 70] as [number, number] };
// Tile setting materials per 50 sq ft: one bag thinset ($15–$25) + grout share.
const THINSET_PER_BAG_SQFT = 50;
const THINSET_PRICE: [number, number] = [15, 25];

export function calculateFlooring(raw: FlooringInputs): CalcResult {
  const area = clamp(raw.areaSqFt, 20, 20000);
  const meta = MATERIAL_META[raw.material];
  const waste = meta.waste + (raw.layout === 'diagonal' ? 0.05 : 0);
  const orderSqFt = Math.ceil(area * (1 + waste));

  const lines: CalcLine[] = [];

  if (meta.boxCoverage) {
    const boxes = Math.ceil(orderSqFt / meta.boxCoverage);
    lines.push({
      id: 'flooring',
      label: meta.label,
      qty: boxes,
      unit: 'boxes',
      detail: `${orderSqFt.toLocaleString('en-US')} sq ft incl. ${Math.round(waste * 100)}% waste — ${meta.detail}`,
      costLow: Math.round(orderSqFt * meta.price[0]),
      costHigh: Math.round(orderSqFt * meta.price[1]),
    });
  } else {
    const sqYds = Math.ceil(orderSqFt / 9);
    lines.push({
      id: 'flooring',
      label: meta.label,
      qty: sqYds,
      unit: 'sq yd',
      detail: `${orderSqFt.toLocaleString('en-US')} sq ft incl. ${Math.round(waste * 100)}% seam waste — ${meta.detail}`,
      costLow: Math.round(orderSqFt * meta.price[0]),
      costHigh: Math.round(orderSqFt * meta.price[1]),
    });
  }

  if (raw.needsUnderlayment && (raw.material === 'lvp' || raw.material === 'laminate' || raw.material === 'engineered')) {
    const rolls = Math.ceil(area / UNDERLAYMENT_ROLL.coverage);
    lines.push({
      id: 'underlayment',
      label: 'Underlayment',
      qty: rolls,
      unit: 'rolls',
      detail: 'Foam/felt roll, 100 sq ft — skip if planks have attached pad',
      costLow: Math.round(rolls * UNDERLAYMENT_ROLL.price[0]),
      costHigh: Math.round(rolls * UNDERLAYMENT_ROLL.price[1]),
    });
  }

  if (raw.material === 'tile') {
    const thinsetBags = Math.ceil(area / THINSET_PER_BAG_SQFT);
    lines.push({
      id: 'thinset',
      label: 'Thinset mortar',
      qty: thinsetBags,
      unit: 'bags',
      detail: '50-lb bag per ~50 sq ft with a 1/4" × 3/8" trowel; grout separate',
      costLow: Math.round(thinsetBags * THINSET_PRICE[0]),
      costHigh: Math.round(thinsetBags * THINSET_PRICE[1]),
    });
  }

  const totals = totalCosts(lines);

  return {
    hero: {
      qty: orderSqFt,
      unit: 'sq ft',
      label: 'Flooring to order',
      detail: `${area.toLocaleString('en-US')} sq ft measured + ${Math.round(waste * 100)}% waste (${raw.layout} lay)`,
    },
    lines,
    ...totals,
    notes: [
      'Keep one unopened box for future repairs — dye lots vary.',
      'Transitions, stair nosing, and baseboard are separate line items.',
      'Material cost only. Acclimate wood and laminate on site 48–72 hours before install.',
    ],
  };
}
