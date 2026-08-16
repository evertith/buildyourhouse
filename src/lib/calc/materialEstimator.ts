import { CalcLine, CalcResult, clamp, totalCosts } from './types';

/**
 * Whole-house material estimator — planning-level quantities and cost for
 * the structural shell (concrete, framing lumber, drywall, roofing,
 * flooring, insulation) from finished square footage and finish level.
 *
 * This is the rule-of-thumb sheet, not a takeoff: it derives a footprint
 * and wall areas from square footage rather than from a plan, so the
 * trade sheets (TO-01…TO-06) beat it once you have real dimensions.
 *
 * Geometry, all derived from finished area ÷ stories = footprint:
 * - Slab: footprint × 4" thick. Footing: 16" wide × 12" deep around the
 *   perimeter of an equal-area square (4√area).
 * - Walls: the footprint is treated as a 1.5:1 rectangle for wall length;
 *   exterior wall area = perimeter × wall height × stories. Interior
 *   partitions run 1 linear foot per 4 sq ft of floor, per story.
 * - Roof: footprint × 1.1 (gable) / 1.3 (hip or mixed) / 1.5 (cut-up with
 *   multiple valleys). The multiplier absorbs pitch, overhang, and waste
 *   together — the roofing sheet (TO-03) separates them properly.
 *
 * Board feet are built up per system and land near the 6–7 bf per finished
 * sq ft rule of thumb for light wood framing: walls 0.6 bf/sq ft of wall
 * surface, exterior sheathing 0.5, floor joists 1.4 and subfloor 0.75 per
 * sq ft of framed floor, roof framing plus sheathing 1.5 per sq ft of roof,
 * then 15% waste on the total.
 *
 * Prices are point rates by finish level with a symmetric band around each
 * (concrete ±20%, lumber ±25%, drywall ±15%, roofing ±20%, flooring ±25%,
 * insulation ±20%), so the headline total sits at the center of the range
 * the sheet shows. Materials only — no labor, and no windows, doors,
 * cabinets, appliances, MEP, or exterior finishes.
 */

export type RoofComplexity = 'simple' | 'moderate' | 'complex';
export type FinishLevel = 'basic' | 'standard' | 'premium';

export interface MaterialEstimatorInputs {
  homeSizeSqFt: number;
  stories: 1 | 2 | 3;
  roofComplexity: RoofComplexity;
  wallHeightFt: 8 | 9 | 10;
  finishLevel: FinishLevel;
}

export interface MaterialEstimatorResult extends CalcResult {
  foundationAreaSqFt: number;
  exteriorWallAreaSqFt: number;
  interiorWallAreaSqFt: number;
  roofAreaSqFt: number;
}

/** Delivered ready-mix, national average — the ±20% band is the $120–$180/yd³ spread. */
const CONCRETE_YD_PRICE = 150;

const LUMBER_BF_PRICE: Record<FinishLevel, number> = {
  basic: 0.85,
  standard: 1.1,
  premium: 1.5,
};
const DRYWALL_SHEET_PRICE: Record<FinishLevel, number> = {
  basic: 12,
  standard: 15,
  premium: 22,
};
const ROOFING_SQUARE_PRICE: Record<FinishLevel, number> = {
  basic: 250,
  standard: 350,
  premium: 500,
};
const FLOORING_SF_PRICE: Record<FinishLevel, number> = {
  basic: 3,
  standard: 5,
  premium: 8,
};
const INSULATION_SF_PRICE: Record<FinishLevel, number> = {
  basic: 1.25,
  standard: 1.75,
  premium: 2.5,
};

const ROOF_MULTIPLIER: Record<RoofComplexity, number> = {
  simple: 1.1,
  moderate: 1.3,
  complex: 1.5,
};

const ROOF_LABEL: Record<RoofComplexity, string> = {
  simple: 'simple gable',
  moderate: 'hip or mixed',
  complex: 'cut-up with valleys',
};

const FINISH_LABEL: Record<FinishLevel, string> = {
  basic: 'basic',
  standard: 'standard',
  premium: 'premium',
};

/**
 * Symmetric low/high band around a point price. Symmetry is load-bearing:
 * it keeps the summed range centered on the headline total.
 */
function band(cost: number, spread: number): { costLow: number; costHigh: number } {
  return {
    costLow: Math.round(cost * (1 - spread)),
    costHigh: Math.round(cost * (1 + spread)),
  };
}

export function calculateMaterialEstimator(raw: MaterialEstimatorInputs): MaterialEstimatorResult {
  const homeSize = clamp(raw.homeSizeSqFt, 100, 25000);
  const stories = clamp(raw.stories, 1, 3) as 1 | 2 | 3;
  const wallHeight = raw.wallHeightFt;
  const { roofComplexity, finishLevel } = raw;

  const foundationArea = homeSize / stories;

  // Foundation: 4" slab over the footprint plus a 16" × 12" continuous
  // footing around the perimeter of an equal-area square.
  const slabCubicFeet = foundationArea * (4 / 12);
  const perimeterEstimate = 4 * Math.sqrt(foundationArea);
  const footingCubicFeet = perimeterEstimate * (16 / 12) * (12 / 12);
  const concreteYards = (slabCubicFeet + footingCubicFeet) / 27;
  const concreteCost = concreteYards * CONCRETE_YD_PRICE;

  // Wall geometry from a 1.5:1 rectangle of the same footprint area.
  const width = Math.sqrt(foundationArea / 1.5);
  const length = foundationArea / width;
  const perimeter = 2 * (width + length);

  const exteriorWallArea = perimeter * wallHeight * stories;
  const interiorWallLinearFeetPerFloor = foundationArea / 4;
  const interiorWallArea = interiorWallLinearFeetPerFloor * wallHeight * stories;

  const roofArea = foundationArea * ROOF_MULTIPLIER[roofComplexity];

  // Framing lumber, board feet by system.
  const wallStudsBoardFeet = (exteriorWallArea + interiorWallArea) * 0.6;
  const wallSheathingBoardFeet = exteriorWallArea * 0.5;
  const floorJoistsBoardFeet = foundationArea * stories * 1.4;
  const subfloorBoardFeet = foundationArea * stories * 0.75;
  const roofBoardFeet = roofArea * 1.5;
  const totalBoardFeet =
    (wallStudsBoardFeet +
      wallSheathingBoardFeet +
      floorJoistsBoardFeet +
      subfloorBoardFeet +
      roofBoardFeet) *
    1.15;
  const lumberCost = totalBoardFeet * LUMBER_BF_PRICE[finishLevel];

  // Drywall: both faces of every partition plus every ceiling.
  const drywallArea = interiorWallArea * 2 + homeSize;
  const drywallSheets = Math.ceil(drywallArea / 32);
  const drywallCost = drywallSheets * DRYWALL_SHEET_PRICE[finishLevel];

  const roofSquares = roofArea / 100;
  const roofingCost = roofSquares * ROOFING_SQUARE_PRICE[finishLevel];

  const flooringArea = homeSize;
  const flooringCost = flooringArea * FLOORING_SF_PRICE[finishLevel];

  const insulationArea = exteriorWallArea + homeSize;
  const insulationCost = insulationArea * INSULATION_SF_PRICE[finishLevel];

  const lines: CalcLine[] = [
    {
      id: 'concrete',
      label: 'Ready-mix concrete',
      qty: Math.round(concreteYards * 10) / 10,
      unit: 'yd³',
      detail: `4" slab over ${Math.round(foundationArea).toLocaleString('en-US')} sq ft plus a 16" × 12" continuous footing — no rebar, vapor barrier, or under-slab foam`,
      ...band(concreteCost, 0.2),
    },
    {
      id: 'lumber',
      label: 'Framing lumber',
      qty: Math.round(totalBoardFeet),
      unit: 'bf',
      detail: 'Studs, plates, wall sheathing, floor joists, subfloor, roof framing and deck — 15% waste included',
      ...band(lumberCost, 0.25),
    },
    {
      id: 'drywall',
      label: 'Drywall',
      qty: drywallSheets,
      unit: 'sheets',
      detail: '4×8 sheets — both faces of every partition plus all ceilings, before tape and compound',
      ...band(drywallCost, 0.15),
    },
    {
      id: 'roofing',
      label: 'Roofing',
      qty: Math.round(roofSquares * 10) / 10,
      unit: 'squares',
      detail: `Shingles and underlayment for a ${ROOF_LABEL[roofComplexity]} roof — footprint × ${ROOF_MULTIPLIER[roofComplexity]}`,
      ...band(roofingCost, 0.2),
    },
    {
      id: 'flooring',
      label: 'Finish flooring',
      qty: flooringArea,
      unit: 'ft²',
      detail: `Finished floor area at the ${FINISH_LABEL[finishLevel]} grade — material only, no underlayment or installation`,
      ...band(flooringCost, 0.25),
    },
    {
      id: 'insulation',
      label: 'Insulation',
      qty: Math.round(insulationArea),
      unit: 'ft²',
      detail: 'Exterior wall area plus finished floor area, covering ceilings and floor systems',
      ...band(insulationCost, 0.2),
    },
  ];

  const totals = totalCosts(lines);

  // Headline total from the unrounded point costs — the center of the band.
  const totalCost = Math.round(
    concreteCost + lumberCost + drywallCost + roofingCost + flooringCost + insulationCost
  );

  return {
    hero: {
      qty: totalCost,
      unit: 'estimate',
      label: 'Estimated materials',
      kind: 'currency',
      detail: `Structural shell for ${homeSize.toLocaleString('en-US')} sq ft over ${stories} ${stories === 1 ? 'story' : 'stories'}, ${FINISH_LABEL[finishLevel]} finish — the center of the range below`,
    },
    lines,
    ...totals,
    notes: [
      'Planning-level quantities derived from square footage — not a takeoff from your plans.',
      'Shell only: no windows, doors, cabinets, appliances, HVAC, electrical, plumbing, or exterior finishes.',
      'Material cost only. No labor, delivery, fasteners, or dumpsters.',
    ],
    foundationAreaSqFt: Math.round(foundationArea),
    exteriorWallAreaSqFt: Math.round(exteriorWallArea),
    interiorWallAreaSqFt: Math.round(interiorWallArea),
    roofAreaSqFt: Math.round(roofArea),
  };
}
