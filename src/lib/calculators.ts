// Cost Savings Calculator
export interface CostSavingsInputs {
  homeSize: number; // square feet
  estimatedCost: number; // total cost estimate
  gcFeePercentage: number; // typically 15-20%
  laborHours: number; // hours you'll work yourself
  hourlyWage: number; // value of your time
}

export interface CostSavingsResults {
  gcFeeSavings: number;
  laborValueSavings: number;
  totalSavings: number;
  percentageSaved: number;
}

export function calculateCostSavings(inputs: CostSavingsInputs): CostSavingsResults {
  // Guard and clamp inputs (HTML min/max are bypassable).
  const estimatedCost = Math.max(0, inputs.estimatedCost || 0);
  const gcFeePercentage = Math.min(30, Math.max(0, inputs.gcFeePercentage || 0));
  const laborHours = Math.max(0, inputs.laborHours || 0);
  const hourlyWage = Math.max(0, inputs.hourlyWage || 0);

  // Cash savings = the GC fee you avoid by managing the project yourself.
  const gcFeeSavings = estimatedCost * (gcFeePercentage / 100);

  // Imputed value of your own time. This is NOT cash savings: estimatedCost
  // already includes subcontractor labor, so adding this would double-count.
  const laborValueSavings = laborHours * hourlyWage;

  // Headline cash savings is the GC fee only — no labor value added in.
  const totalSavings = gcFeeSavings;

  // Honest headline percentage: equals the GC fee percentage you avoid.
  // Return 0 when estimatedCost is missing/zero to avoid Infinity/NaN.
  const percentageSaved = estimatedCost > 0 ? (gcFeeSavings / estimatedCost) * 100 : 0;

  return {
    gcFeeSavings,
    laborValueSavings,
    totalSavings,
    percentageSaved
  };
}

// Material Estimator Calculator
export interface MaterialEstimatorInputs {
  homeSize: number; // square feet
  stories: number; // 1, 2, or 3
  roofComplexity: 'simple' | 'moderate' | 'complex'; // gable, hip, multiple valleys
  wallHeight: number; // feet (typically 8, 9, or 10)
  finishLevel: 'basic' | 'standard' | 'premium';
}

export interface MaterialEstimatorResults {
  concrete: {
    cubicYards: number;
    cost: number;
  };
  lumber: {
    boardFeet: number;
    cost: number;
  };
  drywall: {
    sheets: number;
    cost: number;
  };
  roofing: {
    squares: number;
    cost: number;
  };
  flooring: {
    squareFeet: number;
    cost: number;
  };
  insulation: {
    squareFeet: number;
    cost: number;
  };
  totalCost: number;
}

export function calculateMaterialEstimate(inputs: MaterialEstimatorInputs): MaterialEstimatorResults {
  const { homeSize, stories, roofComplexity, wallHeight, finishLevel } = inputs;

  // Foundation concrete (4" slab + footings)
  const foundationArea = homeSize / stories;
  // Slab: 4 inches thick = 0.33 feet; Footings: assume 16" wide x 12" deep around perimeter
  const slabCubicFeet = foundationArea * (4 / 12); // 4 inches = 0.33 feet
  const perimeterEstimate = 4 * Math.sqrt(foundationArea); // Assume square-ish house
  const footingCubicFeet = perimeterEstimate * (16 / 12) * (12 / 12); // 16" wide x 12" deep
  const concreteYards = (slabCubicFeet + footingCubicFeet) / 27; // Convert cubic feet to cubic yards
  const concreteCost = concreteYards * 150; // $150/cubic yard

  // Framing lumber
  // Calculate perimeter for a rectangular house (assume aspect ratio of 1.5:1)
  const width = Math.sqrt(foundationArea / 1.5);
  const length = foundationArea / width;
  const perimeter = 2 * (width + length);

  // Exterior walls
  const exteriorWallArea = perimeter * wallHeight * stories;

  // Interior walls (assume 1 linear foot of interior wall per 4 sq ft of floor
  // space). Computed per floor from the footprint, then scaled by stories so
  // partitions on upper floors are counted (the old code keyed this off total
  // homeSize and silently dropped the per-story repetition for studs/drywall).
  const interiorWallLinearFeetPerFloor = foundationArea / 4;
  const interiorWallAreaPerFloor = interiorWallLinearFeetPerFloor * wallHeight;
  const interiorWallArea = interiorWallAreaPerFloor * stories;

  const totalWallArea = exteriorWallArea + interiorWallArea;

  // Roof area with complexity multiplier
  const roofMultiplier = roofComplexity === 'simple' ? 1.1 : roofComplexity === 'moderate' ? 1.3 : 1.5;
  const roofArea = foundationArea * roofMultiplier;

  // Board feet calculation (calibrated to land ~6-7 bf per finished sq ft,
  // the standard rule of thumb for light wood framing):
  // - Wall studs: 2x4/2x6 at 16" OC plus top/bottom plates = ~0.6 bf per sq ft
  //   of wall surface
  // - Wall sheathing: 1/2" OSB/plywood = ~0.5 bf per sq ft of wall area (exterior only)
  // - Floor joists: 2x10 at 16" OC = ~1.4 bf per sq ft of framed floor
  // - Subfloor: 3/4" T&G plywood = ~0.75 bf per sq ft of framed floor
  // - Roof: rafters/trusses + sheathing = ~1.5 bf per sq ft of roof

  // Wall studs for ALL walls (exterior + interior). Both wall areas already
  // account for every story, so studs scale with wall area directly.
  const wallStudsBoardFeet = (exteriorWallArea + interiorWallArea) * 0.6;

  // Wall sheathing for exterior walls only
  const wallSheathingBoardFeet = exteriorWallArea * 0.5;

  // Floor system. A multi-story home has an elevated structural floor between
  // each level (stories - 1 inter-floor decks) plus the ground floor, all
  // framed at the per-floor footprint (foundationArea).
  const framedFloors = stories; // ground floor + each upper floor's deck
  const floorJoistsBoardFeet = foundationArea * framedFloors * 1.4;
  const subfloorBoardFeet = foundationArea * framedFloors * 0.75;

  // Roof system (already includes sheathing)
  const roofBoardFeet = roofArea * 1.5;

  const totalBoardFeet = (wallStudsBoardFeet + wallSheathingBoardFeet + floorJoistsBoardFeet + subfloorBoardFeet + roofBoardFeet) * 1.15; // Add 15% waste
  const lumberCost = totalBoardFeet * (finishLevel === 'basic' ? 0.85 : finishLevel === 'standard' ? 1.10 : 1.50);

  // Drywall: both faces of every interior partition (interiorWallArea already
  // spans all stories) plus every floor's ceiling (homeSize is total area).
  const drywallArea = (interiorWallArea * 2) + homeSize;
  const drywallSheets = Math.ceil(drywallArea / 32); // 4x8 sheets = 32 sq ft
  const drywallCost = drywallSheets * (finishLevel === 'basic' ? 12 : finishLevel === 'standard' ? 15 : 22);

  // Roofing
  const roofSquares = roofArea / 100;
  const roofingCost = roofSquares * (finishLevel === 'basic' ? 250 : finishLevel === 'standard' ? 350 : 500);

  // Flooring
  const flooringArea = homeSize;
  const flooringCost = flooringArea * (finishLevel === 'basic' ? 3 : finishLevel === 'standard' ? 5 : 8);

  // Insulation (exterior walls + ceiling)
  const insulationArea = exteriorWallArea + homeSize; // Only exterior walls + ceiling
  const insulationCost = insulationArea * (finishLevel === 'basic' ? 1.25 : finishLevel === 'standard' ? 1.75 : 2.50);

  return {
    concrete: {
      cubicYards: Math.round(concreteYards * 10) / 10,
      cost: Math.round(concreteCost)
    },
    lumber: {
      boardFeet: Math.round(totalBoardFeet),
      cost: Math.round(lumberCost)
    },
    drywall: {
      sheets: drywallSheets,
      cost: Math.round(drywallCost)
    },
    roofing: {
      squares: Math.round(roofSquares * 10) / 10,
      cost: Math.round(roofingCost)
    },
    flooring: {
      squareFeet: flooringArea,
      cost: Math.round(flooringCost)
    },
    insulation: {
      squareFeet: Math.round(insulationArea),
      cost: Math.round(insulationCost)
    },
    totalCost: Math.round(concreteCost + lumberCost + drywallCost + roofingCost + flooringCost + insulationCost)
  };
}

// Timeline Estimator Calculator
export interface TimelineEstimatorInputs {
  homeSize: number; // square feet
  hoursPerWeek: number; // hours you can dedicate
  diyPercentage: number; // 0-100, how much you'll do yourself vs hire out
  experienceLevel: 'beginner' | 'intermediate' | 'experienced';
  helpers: number; // number of regular helpers
}

export interface TimelineEstimatorResults {
  totalMonths: number;
  totalWeeks: number;
  phases: {
    name: string;
    weeks: number;
    description: string;
  }[];
  totalHours: number;
  warningFactors: string[];
}

export function calculateTimelineEstimate(inputs: TimelineEstimatorInputs): TimelineEstimatorResults {
  // Clamp/floor inputs (HTML min/max are bypassable).
  const homeSize = Math.max(0, inputs.homeSize || 0);
  // Guard against divide-by-zero: 0 hours/week would yield Infinity months.
  const hoursPerWeek = Math.max(1, inputs.hoursPerWeek || 0);
  const diyPercentage = Math.min(100, Math.max(0, inputs.diyPercentage || 0));
  const experienceLevel = inputs.experienceLevel;
  const helpers = Math.max(0, inputs.helpers || 0);

  // Base hours for a complete DIY build.
  // ~1.75 personal hours per square foot lands a 2,000 sq ft home near
  // 3,500 hrs of hands-on labor — in line with the site's time-commitment
  // page (500-2,000+ hrs of pure management, more once you swing a hammer)
  // and the ~15-month Census reality for owner-built homes.
  let baseHours = homeSize * 1.75;

  // Adjust for experience
  const expMultiplier = experienceLevel === 'beginner' ? 1.4 : experienceLevel === 'intermediate' ? 1.0 : 0.8;
  baseHours *= expMultiplier;

  // Adjust for helpers (each helper adds 60% efficiency)
  const helperMultiplier = 1 / (1 + (helpers * 0.6));
  baseHours *= helperMultiplier;

  // Actual hours you'll work based on DIY percentage
  const yourHours = baseHours * (diyPercentage / 100);

  // Calculate timeline
  const totalWeeks = Math.ceil(yourHours / hoursPerWeek);
  const totalMonths = Math.round(totalWeeks / 4.33 * 10) / 10;

  // Phase breakdown. Fractions sum to 1.0; distribute the integer weeks with a
  // largest-remainder method so the phases add up to exactly totalWeeks (plain
  // Math.ceil on each fraction overshot the total).
  const phaseTemplates = [
    {
      name: 'Planning & Permitting',
      fraction: 0.15,
      description: 'Design finalization, permit applications, site prep planning'
    },
    {
      name: 'Foundation',
      fraction: 0.12,
      description: 'Excavation, footings, foundation walls, waterproofing'
    },
    {
      name: 'Framing',
      fraction: 0.20,
      description: 'Floor system, wall framing, roof framing, sheathing'
    },
    {
      name: 'Rough-Ins',
      fraction: 0.18,
      description: 'Electrical, plumbing, HVAC rough-in work'
    },
    {
      name: 'Insulation & Drywall',
      fraction: 0.12,
      description: 'Insulation installation, drywall hanging, taping, mudding'
    },
    {
      name: 'Interior Finishes',
      fraction: 0.15,
      description: 'Trim, doors, cabinets, flooring, painting'
    },
    {
      name: 'Final & Exterior',
      fraction: 0.08,
      description: 'Exterior finishes, landscaping, final inspections, punch list'
    }
  ];

  const rawWeeks = phaseTemplates.map(p => totalWeeks * p.fraction);
  const floored = rawWeeks.map(w => Math.floor(w));
  let remainder = totalWeeks - floored.reduce((sum, w) => sum + w, 0);
  // Hand out the leftover weeks to the phases with the largest fractional parts.
  const order = rawWeeks
    .map((w, i) => ({ i, frac: w - Math.floor(w) }))
    .sort((a, b) => b.frac - a.frac);
  for (let k = 0; k < order.length && remainder > 0; k++) {
    floored[order[k].i] += 1;
    remainder--;
  }

  const phases = phaseTemplates.map((p, i) => ({
    name: p.name,
    weeks: floored[i],
    description: p.description
  }));

  // Warning factors
  const warnings: string[] = [];
  if (hoursPerWeek < 15) warnings.push('Low weekly hours may extend timeline significantly');
  if (experienceLevel === 'beginner' && diyPercentage > 50) warnings.push('High DIY % with beginner experience adds risk');
  if (homeSize > 2500 && hoursPerWeek < 20) warnings.push('Large home with limited time = long project');
  if (diyPercentage > 70) warnings.push('Very high DIY % requires strong commitment and skills');

  return {
    totalMonths,
    totalWeeks,
    phases,
    totalHours: Math.round(yourHours),
    warningFactors: warnings
  };
}

// Budget Tracker Calculator
export interface BudgetPhase {
  name: string;
  budgeted: number;
  actual: number;
}

export interface BudgetTrackerInputs {
  phases: BudgetPhase[];
  contingency: number; // percentage (typically 10-20%)
}

export interface BudgetTrackerResults {
  totalBudgeted: number;
  totalActual: number;
  totalVariance: number;
  variancePercentage: number;
  contingencyAmount: number;
  contingencyRemaining: number;
  phaseAnalysis: {
    name: string;
    budgeted: number;
    actual: number;
    variance: number;
    variancePercentage: number;
    status: 'under' | 'on-track' | 'over';
  }[];
  overallStatus: 'under' | 'on-track' | 'over';
  recommendations: string[];
}

export function calculateBudgetTracker(inputs: BudgetTrackerInputs): BudgetTrackerResults {
  const { phases, contingency } = inputs;

  const totalBudgeted = phases.reduce((sum, p) => sum + p.budgeted, 0);
  const totalActual = phases.reduce((sum, p) => sum + p.actual, 0);
  const totalVariance = totalBudgeted - totalActual;
  // Guard against divide-by-zero (no budget entered) → "NaN%"/"-Infinity%".
  const variancePercentage = totalBudgeted > 0 ? (totalVariance / totalBudgeted) * 100 : 0;

  const contingencyAmount = totalBudgeted * (contingency / 100);
  const contingencyRemaining = contingencyAmount - Math.max(0, -totalVariance);

  const phaseAnalysis = phases.map(phase => {
    const variance = phase.budgeted - phase.actual;
    const varPercent = phase.budgeted > 0 ? (variance / phase.budgeted) * 100 : 0;

    let status: 'under' | 'on-track' | 'over';
    if (variance > phase.budgeted * 0.05) status = 'under';
    else if (variance < -phase.budgeted * 0.05) status = 'over';
    else status = 'on-track';

    return {
      name: phase.name,
      budgeted: phase.budgeted,
      actual: phase.actual,
      variance,
      variancePercentage: varPercent,
      status
    };
  });

  let overallStatus: 'under' | 'on-track' | 'over';
  if (variancePercentage > 5) overallStatus = 'under';
  else if (variancePercentage < -5) overallStatus = 'over';
  else overallStatus = 'on-track';

  // Generate recommendations
  const recommendations: string[] = [];
  const overBudgetPhases = phaseAnalysis.filter(p => p.status === 'over');

  if (overBudgetPhases.length > 0) {
    recommendations.push(`${overBudgetPhases.length} phase(s) over budget - review and adjust remaining phases`);
  }

  if (contingencyRemaining < contingencyAmount * 0.3) {
    recommendations.push('Contingency running low - consider cost-cutting measures');
  }

  if (overallStatus === 'over' && contingencyRemaining < 0) {
    recommendations.push('ALERT: Over budget and contingency depleted - immediate action needed');
  }

  if (overallStatus === 'under') {
    recommendations.push('Under budget - consider upgrades or keep as savings');
  }

  const highVariancePhases = phaseAnalysis.filter(p => Math.abs(p.variancePercentage) > 15);
  if (highVariancePhases.length > 0) {
    recommendations.push('Some phases show high variance - review estimating accuracy');
  }

  return {
    totalBudgeted,
    totalActual,
    totalVariance,
    variancePercentage,
    contingencyAmount,
    contingencyRemaining,
    phaseAnalysis,
    overallStatus,
    recommendations
  };
}
