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
  const gcFeeSavings = inputs.estimatedCost * (inputs.gcFeePercentage / 100);
  const laborValueSavings = inputs.laborHours * inputs.hourlyWage;
  const totalSavings = gcFeeSavings + laborValueSavings;
  const percentageSaved = (totalSavings / inputs.estimatedCost) * 100;

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
  const concreteYards = (foundationArea * 0.33) / 27 + (foundationArea * 0.5 / 27); // slab + footings
  const concreteCost = concreteYards * 150; // $150/cubic yard

  // Framing lumber
  const wallArea = (foundationArea * 2 * Math.sqrt(foundationArea / Math.PI)) * wallHeight * stories;
  const roofMultiplier = roofComplexity === 'simple' ? 1.1 : roofComplexity === 'moderate' ? 1.3 : 1.5;
  const roofArea = foundationArea * roofMultiplier;

  const totalBoardFeet = (wallArea / 8) * 1.5 + (roofArea / 2) * 2 + (homeSize * 2); // walls + roof + floor joists
  const lumberCost = totalBoardFeet * (finishLevel === 'basic' ? 0.85 : finishLevel === 'standard' ? 1.10 : 1.50);

  // Drywall (interior walls + ceilings)
  const drywallArea = wallArea * 0.7 + homeSize; // 70% of wall area is interior + all ceilings
  const drywallSheets = Math.ceil(drywallArea / 32); // 4x8 sheets
  const drywallCost = drywallSheets * (finishLevel === 'basic' ? 12 : finishLevel === 'standard' ? 15 : 22);

  // Roofing
  const roofSquares = roofArea / 100;
  const roofingCost = roofSquares * (finishLevel === 'basic' ? 250 : finishLevel === 'standard' ? 350 : 500);

  // Flooring
  const flooringArea = homeSize;
  const flooringCost = flooringArea * (finishLevel === 'basic' ? 3 : finishLevel === 'standard' ? 5 : 8);

  // Insulation
  const insulationArea = wallArea + homeSize; // walls + ceiling
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
  const { homeSize, hoursPerWeek, diyPercentage, experienceLevel, helpers } = inputs;

  // Base hours for complete DIY build
  let baseHours = homeSize * 15; // 15 hours per square foot is realistic for DIY

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

  // Phase breakdown
  const phases = [
    {
      name: 'Planning & Permitting',
      weeks: Math.ceil(totalWeeks * 0.15),
      description: 'Design finalization, permit applications, site prep planning'
    },
    {
      name: 'Foundation',
      weeks: Math.ceil(totalWeeks * 0.12),
      description: 'Excavation, footings, foundation walls, waterproofing'
    },
    {
      name: 'Framing',
      weeks: Math.ceil(totalWeeks * 0.20),
      description: 'Floor system, wall framing, roof framing, sheathing'
    },
    {
      name: 'Rough-Ins',
      weeks: Math.ceil(totalWeeks * 0.18),
      description: 'Electrical, plumbing, HVAC rough-in work'
    },
    {
      name: 'Insulation & Drywall',
      weeks: Math.ceil(totalWeeks * 0.12),
      description: 'Insulation installation, drywall hanging, taping, mudding'
    },
    {
      name: 'Interior Finishes',
      weeks: Math.ceil(totalWeeks * 0.15),
      description: 'Trim, doors, cabinets, flooring, painting'
    },
    {
      name: 'Final & Exterior',
      weeks: Math.ceil(totalWeeks * 0.08),
      description: 'Exterior finishes, landscaping, final inspections, punch list'
    }
  ];

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
  const variancePercentage = (totalVariance / totalBudgeted) * 100;

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
