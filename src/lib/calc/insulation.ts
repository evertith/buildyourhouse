import { CalcLine, CalcResult, clamp, totalCosts } from './types';

/**
 * Insulation takeoff — wall batts and attic coverage.
 *
 * Batt coverage per bag (typical manufacturer bag charts, rounded —
 * exact coverage varies by brand and width):
 * - R-13 (2×4 wall): ~106 sq ft/bag
 * - R-15 (2×4 wall, high density): ~68 sq ft/bag
 * - R-19 (2×6 wall): ~87 sq ft/bag
 * - R-21 (2×6 wall, high density): ~68 sq ft/bag
 * Blown-in attic (fiberglass, e.g. AttiCat-class): R-38 ≈ 1 bag per
 * 40 sq ft; R-49 ≈ 1 bag per 31 sq ft. Machine rental is usually free
 * with a ~10-bag purchase.
 *
 * Wall area from footprint: perimeter × wall height × stories, minus a
 * 15% openings allowance.
 *
 * 2026 prices: R-13 bag $55–$75, R-15 $60–$85, R-19 $60–$85, R-21
 * $70–$95, blown-in bag $38–$52.
 */

export interface InsulationInputs {
  scope: 'walls' | 'attic' | 'both';
  // walls
  wallInput: 'footprint' | 'area';
  lengthFt: number;
  widthFt: number;
  stories: 1 | 2 | 3;
  wallHeightFt: 8 | 9 | 10;
  wallAreaSqFt: number;
  wallR: 'r13' | 'r15' | 'r19' | 'r21';
  // attic
  atticAreaSqFt: number;
  atticR: 'r38' | 'r49';
}

const BATT_META: Record<
  InsulationInputs['wallR'],
  { label: string; coverage: number; price: [number, number] }
> = {
  r13: { label: 'R-13 batts (2×4 walls)', coverage: 106, price: [55, 75] },
  r15: { label: 'R-15 batts (2×4 walls)', coverage: 68, price: [60, 85] },
  r19: { label: 'R-19 batts (2×6 walls)', coverage: 87, price: [60, 85] },
  r21: { label: 'R-21 batts (2×6 walls)', coverage: 68, price: [70, 95] },
};

const BLOWN_META: Record<
  InsulationInputs['atticR'],
  { label: string; sqFtPerBag: number; price: [number, number] }
> = {
  r38: { label: 'Blown-in fiberglass to R-38', sqFtPerBag: 40, price: [38, 52] },
  r49: { label: 'Blown-in fiberglass to R-49', sqFtPerBag: 31, price: [38, 52] },
};

export function calculateInsulation(raw: InsulationInputs): CalcResult {
  const lines: CalcLine[] = [];
  let wallArea = 0;
  let atticArea = 0;

  if (raw.scope !== 'attic') {
    if (raw.wallInput === 'footprint') {
      const l = clamp(raw.lengthFt, 8, 300);
      const w = clamp(raw.widthFt, 8, 300);
      const stories = clamp(raw.stories, 1, 3);
      wallArea = 2 * (l + w) * raw.wallHeightFt * stories * 0.85; // 15% openings
    } else {
      wallArea = clamp(raw.wallAreaSqFt, 50, 30000);
    }
    const meta = BATT_META[raw.wallR];
    const bags = Math.ceil((wallArea / meta.coverage) * 1.05);
    lines.push({
      id: 'wall-batts',
      label: meta.label,
      qty: bags,
      unit: 'bags',
      detail: `${Math.round(wallArea).toLocaleString('en-US')} sq ft of wall cavity, 5% cut allowance — check the bag chart for your exact brand`,
      costLow: Math.round(bags * meta.price[0]),
      costHigh: Math.round(bags * meta.price[1]),
    });
  }

  if (raw.scope !== 'walls') {
    atticArea = clamp(raw.atticAreaSqFt, 100, 20000);
    const meta = BLOWN_META[raw.atticR];
    const bags = Math.ceil(atticArea / meta.sqFtPerBag);
    lines.push({
      id: 'attic-blown',
      label: meta.label,
      qty: bags,
      unit: 'bags',
      detail: `${atticArea.toLocaleString('en-US')} sq ft attic — blower rental typically free with ~10+ bags`,
      costLow: Math.round(bags * meta.price[0]),
      costHigh: Math.round(bags * meta.price[1]),
    });
  }

  const totals = totalCosts(lines);
  const totalBags = lines.reduce((s, l) => s + l.qty, 0);

  const heroDetail =
    raw.scope === 'both'
      ? `${Math.round(wallArea).toLocaleString('en-US')} sq ft walls + ${atticArea.toLocaleString('en-US')} sq ft attic`
      : raw.scope === 'walls'
        ? `${Math.round(wallArea).toLocaleString('en-US')} sq ft of wall cavity`
        : `${atticArea.toLocaleString('en-US')} sq ft of attic`;

  return {
    hero: {
      qty: totalBags,
      unit: 'bags',
      label: 'Insulation to buy',
      detail: heroDetail,
    },
    lines,
    ...totals,
    notes: [
      'R-value requirements come from your climate zone and local code — the guide below has the map.',
      'Never compress batts to fit; a squashed R-19 performs like R-13.',
      'Material cost only. Air-sealing (caulk, foam) before insulating is the highest-ROI hour on the job.',
    ],
  };
}
