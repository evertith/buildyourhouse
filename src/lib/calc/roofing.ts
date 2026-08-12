import { CalcLine, CalcResult, clamp, totalCosts } from './types';

/**
 * Roofing takeoff — squares, shingle bundles, underlayment, starter,
 * ridge cap, drip edge, and nails, from footprint + pitch.
 *
 * Math:
 * - Plan area = (L + 2 × overhang) × (W + 2 × overhang).
 * - Pitch factor = √(1 + (rise/12)²) — 4/12 → 1.054 … 12/12 → 1.414.
 * - Waste by cut-up factor: gable 10%, hips/valleys 15%, complex 20%.
 * - 3 bundles per square (architectural), synthetic underlayment 10
 *   squares/roll, starter 105 lf/bundle on eaves+rakes, ridge cap ≈ house
 *   length + 25% per complexity step (hips add cap), coil nails ≈ 2.5 lb
 *   per square (~320 nails).
 *
 * 2026 prices: architectural bundle $34–$48; synthetic underlayment roll
 * $85–$140; starter bundle $28–$42; ridge cap bundle (~33 lf) $45–$65;
 * drip edge 10-ft stick $9–$15; coil nails $3.5–$5/lb.
 */

export interface RoofingInputs {
  lengthFt: number;
  widthFt: number;
  pitch: 4 | 5 | 6 | 7 | 8 | 9 | 10 | 12;
  overhangFt: 0 | 1 | 2;
  complexity: 'gable' | 'hips' | 'complex';
}

const BUNDLE_PRICE: [number, number] = [34, 48];
const UNDERLAYMENT_ROLL_PRICE: [number, number] = [85, 140];
const STARTER_BUNDLE_PRICE: [number, number] = [28, 42];
const RIDGE_BUNDLE_PRICE: [number, number] = [45, 65];
const DRIP_STICK_PRICE: [number, number] = [9, 15];
const NAIL_LB_PRICE: [number, number] = [3.5, 5];

const WASTE: Record<RoofingInputs['complexity'], number> = {
  gable: 0.1,
  hips: 0.15,
  complex: 0.2,
};

export function calculateRoofing(raw: RoofingInputs): CalcResult {
  const l = clamp(raw.lengthFt, 10, 300);
  const w = clamp(raw.widthFt, 10, 300);
  const o = raw.overhangFt;

  const planL = l + 2 * o;
  const planW = w + 2 * o;
  const planArea = planL * planW;
  const pitchFactor = Math.sqrt(1 + Math.pow(raw.pitch / 12, 2));
  const roofArea = planArea * pitchFactor;
  const wasteFactor = 1 + WASTE[raw.complexity];
  const orderArea = roofArea * wasteFactor;

  const squares = Math.ceil(orderArea / 100 * 10) / 10;
  const bundles = Math.ceil((orderArea / 100) * 3);
  const underlaymentRolls = Math.ceil(roofArea / 100 / 10 * 1.1);

  // Eaves + rakes need starter. Gable: 2 eaves + 4 rakes; hip roofs are all
  // eaves. Approximate with the plan perimeter either way.
  const starterLf = 2 * (planL + planW) * (raw.complexity === 'gable' ? 1 : 1.05);
  const starterBundles = Math.ceil(starterLf / 105);

  // Ridge + hip cap: gable ridge ≈ house length; hips add diagonal cap runs.
  const capLf =
    raw.complexity === 'gable' ? planL : raw.complexity === 'hips' ? planL * 1.6 : planL * 2.1;
  const ridgeBundles = Math.ceil(capLf / 33);

  const dripSticks = Math.ceil((2 * (planL + planW) * 1.05) / 10);
  const nailLbs = Math.ceil((orderArea / 100) * 2.5);

  const lines: CalcLine[] = [
    {
      id: 'shingles',
      label: 'Architectural shingles',
      qty: bundles,
      unit: 'bundles',
      detail: `${squares.toFixed(1)} squares incl. ${Math.round(WASTE[raw.complexity] * 100)}% waste — 3 bundles per square`,
      costLow: Math.round(bundles * BUNDLE_PRICE[0]),
      costHigh: Math.round(bundles * BUNDLE_PRICE[1]),
    },
    {
      id: 'underlayment',
      label: 'Synthetic underlayment',
      qty: underlaymentRolls,
      unit: 'rolls',
      detail: '10-square rolls, 10% for laps',
      costLow: Math.round(underlaymentRolls * UNDERLAYMENT_ROLL_PRICE[0]),
      costHigh: Math.round(underlaymentRolls * UNDERLAYMENT_ROLL_PRICE[1]),
    },
    {
      id: 'starter',
      label: 'Starter strip',
      qty: starterBundles,
      unit: 'bundles',
      detail: `${Math.round(starterLf)} lf of eaves and rakes — 105 lf per bundle`,
      costLow: Math.round(starterBundles * STARTER_BUNDLE_PRICE[0]),
      costHigh: Math.round(starterBundles * STARTER_BUNDLE_PRICE[1]),
    },
    {
      id: 'ridge',
      label: 'Ridge & hip cap',
      qty: ridgeBundles,
      unit: 'bundles',
      detail: `${Math.round(capLf)} lf of ridge${raw.complexity !== 'gable' ? ' and hips' : ''} — ~33 lf per bundle`,
      costLow: Math.round(ridgeBundles * RIDGE_BUNDLE_PRICE[0]),
      costHigh: Math.round(ridgeBundles * RIDGE_BUNDLE_PRICE[1]),
    },
    {
      id: 'drip',
      label: 'Drip edge',
      qty: dripSticks,
      unit: 'sticks',
      detail: '10-ft aluminum, full perimeter + 5% laps',
      costLow: Math.round(dripSticks * DRIP_STICK_PRICE[0]),
      costHigh: Math.round(dripSticks * DRIP_STICK_PRICE[1]),
    },
    {
      id: 'nails',
      label: 'Roofing nails',
      qty: nailLbs,
      unit: 'lb',
      detail: '1¼" coil — ≈ 2.5 lb per square',
      costLow: Math.round(nailLbs * NAIL_LB_PRICE[0]),
      costHigh: Math.round(nailLbs * NAIL_LB_PRICE[1]),
    },
  ];

  const totals = totalCosts(lines);

  return {
    hero: {
      qty: squares,
      unit: 'squares',
      label: 'Roof area to order',
      detail: `${Math.round(roofArea).toLocaleString('en-US')} sq ft actual at ${raw.pitch}/12 pitch, ${Math.round(WASTE[raw.complexity] * 100)}% waste added`,
    },
    lines,
    ...totals,
    notes: [
      'Assumes a rectangular footprint measured at the walls; L-shapes: run each wing separately and add.',
      'Ice & water shield (code-required in cold climates at eaves/valleys) not included — one roll covers ~65 lf of eave.',
      'Material cost only. No labor, flashing, vents, or tear-off disposal.',
    ],
  };
}
