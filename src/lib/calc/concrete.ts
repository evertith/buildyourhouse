import { CalcLine, CalcResult, clamp, totalCosts } from './types';

/**
 * Concrete slab takeoff — volume in cubic yards, ready-mix vs. bagged
 * comparison, reinforcement, and vapor barrier.
 *
 * Math:
 * - Slab volume = L × W × (thickness / 12) cubic feet → ÷ 27 for yards.
 * - Optional perimeter footings (thickened edge): width × depth × perimeter.
 * - Order factor: +10% — short-loading a pour is the classic expensive
 *   mistake; finishing crews would rather waste half a yard than cold-joint
 *   a slab.
 * - Bags: an 80-lb bag yields 0.60 cu ft, 60-lb yields 0.45. Bags stop
 *   making sense above roughly 2 yards (90+ bags); the UI surfaces both and
 *   lets the visitor see why.
 *
 * 2026 price ranges: ready-mix $155–$195/yd delivered (short-load fees
 * extra below ~4 yd); 80-lb bag $5.50–$8; 6-mil vapor barrier ~$0.06–0.12
 * /sq ft; WWM sheet (5×10) $9–$14; #4 rebar 20-ft stick $9–$16.
 */

export interface ConcreteInputs {
  lengthFt: number;
  widthFt: number;
  thicknessIn: 4 | 5 | 6;
  thickenedEdge: boolean;
  reinforcement: 'none' | 'mesh' | 'rebar';
}

const READY_MIX_PER_YD: [number, number] = [155, 195];
const BAG_80_PRICE: [number, number] = [5.5, 8];
const VAPOR_PER_SQFT: [number, number] = [0.06, 0.12];
const MESH_SHEET_PRICE: [number, number] = [9, 14]; // 5×10 sheet = 50 sq ft
const REBAR_STICK_PRICE: [number, number] = [9, 16]; // #4 × 20 ft

export function calculateConcrete(raw: ConcreteInputs): CalcResult {
  const l = clamp(raw.lengthFt, 2, 300);
  const w = clamp(raw.widthFt, 2, 300);
  const area = l * w;
  const perimeter = 2 * (l + w);

  const slabCuFt = area * (raw.thicknessIn / 12);
  // Thickened edge: 12" wide × 12" deep beyond slab thickness, around the
  // perimeter — the standard monolithic-slab detail for garages and sheds.
  const edgeCuFt = raw.thickenedEdge ? perimeter * 1 * 1 : 0;
  const totalCuFt = slabCuFt + edgeCuFt;

  const orderYards = Math.ceil(((totalCuFt / 27) * 1.1) * 4) / 4; // +10%, round up to ¼ yd
  const bags80 = Math.ceil((totalCuFt * 1.1) / 0.6);

  const lines: CalcLine[] = [
    {
      id: 'ready-mix',
      label: 'Ready-mix concrete',
      qty: orderYards,
      unit: 'yd³',
      detail: `Order quantity incl. 10% — ${Math.round(totalCuFt)} cu ft placed${raw.thickenedEdge ? ' (slab + thickened edge)' : ''}`,
      costLow: Math.round(orderYards * READY_MIX_PER_YD[0]),
      costHigh: Math.round(orderYards * READY_MIX_PER_YD[1]),
    },
    {
      id: 'vapor',
      label: 'Vapor barrier',
      qty: Math.ceil(area * 1.15),
      unit: 'sq ft',
      detail: '6-mil poly under slab, 15% for laps and turnups',
      costLow: Math.round(area * 1.15 * VAPOR_PER_SQFT[0]),
      costHigh: Math.round(area * 1.15 * VAPOR_PER_SQFT[1]),
    },
  ];

  if (raw.reinforcement === 'mesh') {
    const sheets = Math.ceil((area / 50) * 1.1);
    lines.push({
      id: 'mesh',
      label: 'Welded wire mesh',
      qty: sheets,
      unit: 'sheets',
      detail: '5×10 ft flat sheets, one-square overlap (10%)',
      costLow: Math.round(sheets * MESH_SHEET_PRICE[0]),
      costHigh: Math.round(sheets * MESH_SHEET_PRICE[1]),
    });
  } else if (raw.reinforcement === 'rebar') {
    // #4 bar both ways at 24" OC.
    const runsL = Math.floor(w / 2) + 1;
    const runsW = Math.floor(l / 2) + 1;
    const barLf = runsL * l + runsW * w;
    const sticks = Math.ceil((barLf / 20) * 1.05);
    lines.push({
      id: 'rebar',
      label: 'Rebar',
      qty: sticks,
      unit: 'sticks',
      detail: `#4 × 20 ft — both ways at 24" OC (${Math.round(barLf)} lf), 5% lap allowance`,
      costLow: Math.round(sticks * REBAR_STICK_PRICE[0]),
      costHigh: Math.round(sticks * REBAR_STICK_PRICE[1]),
    });
  }

  const totals = totalCosts(lines);

  return {
    hero: {
      qty: orderYards,
      unit: 'yd³',
      label: 'Concrete to order',
      detail: `${l} × ${w} ft at ${raw.thicknessIn}" thick${raw.thickenedEdge ? ' with thickened edge' : ''}`,
    },
    lines,
    ...totals,
    notes: [
      `Bagged alternative: ${bags80.toLocaleString('en-US')} × 80-lb bags ($${Math.round(bags80 * BAG_80_PRICE[0]).toLocaleString('en-US')}–$${Math.round(bags80 * BAG_80_PRICE[1]).toLocaleString('en-US')}) — practical only under ~2 yd³.`,
      'Loads under ~4 yd³ usually carry a short-load fee; ask the plant.',
      'Excludes forms, gravel base, labor, and pump/finishing. House foundations need engineered footings — this is for slabs, garages, and outbuildings.',
    ],
  };
}
