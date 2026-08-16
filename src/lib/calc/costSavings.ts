import { CalcLine, CalcResult } from './types';

/**
 * Owner-builder savings worksheet (W-01): what you actually keep by acting
 * as your own general contractor, and what it costs you in hours.
 *
 * The one honest thing this worksheet does that most savings calculators
 * don't: it refuses to add the value of your own labor to the cash savings.
 * The construction budget already carries subcontractor labor, so counting
 * your hours as "savings" double-counts the same work and inflates the
 * headline by tens of thousands. Sweat equity is shown on its own line,
 * clearly marked as not cash.
 *
 * Conventions (each stated on the page):
 * - The build cost you enter is the ALL-IN price a GC would quote — their
 *   fee included — and the fee percentage is a share of that contract
 *   price. That is how percentage-of-contract bids are written, and it is
 *   what makes "your cost = contract − fee" the right subtraction.
 * - Fee percentage is capped at 30%. Above that, a bid is not a builder's
 *   fee; it is a developer's margin, and the comparison stops meaning
 *   anything.
 * - Nothing here models the costs owner-building adds back: builder's-risk
 *   insurance, permit runs, re-work, or a construction loan priced without
 *   a licensed GC on the file. Those are covered in the page's prose.
 *
 * Math parity: gcFeeSavings, laborValueSavings, totalSavings, and
 * percentageSaved reproduce calculateCostSavings() in src/lib/calculators.ts
 * exactly, including its clamping. Everything else on this sheet is derived
 * for display from those four numbers.
 */

export interface CostSavingsInputs {
  /** Finished square footage — context only; drives the per-sq-ft lines. */
  homeSize: number;
  /** All-in build cost with a GC, their fee included. */
  estimatedCost: number;
  /** Builder's fee as a percentage of the contract price. */
  gcFeePercentage: number;
  /** Hours you will personally put into the build. */
  laborHours: number;
  /** What an hour of your time is worth. */
  hourlyWage: number;
}

export interface CostSavingsResult extends CalcResult {
  /** Clamped contract price — what the GC column is worth. */
  contractPrice: number;
  gcFeeSavings: number;
  laborValueSavings: number;
  totalSavings: number;
  percentageSaved: number;
  netProjectCost: number;
  fullTimeWeeks: number;
  costPerSqFt: number;
  netCostPerSqFt: number;
  returnPerHour: number;
}

export function calculateCostSavings(raw: CostSavingsInputs): CostSavingsResult {
  // Clamps are lifted verbatim from the legacy engine — HTML min/max are
  // bypassable, and `|| 0` also absorbs NaN from a cleared field.
  const estimatedCost = Math.max(0, raw.estimatedCost || 0);
  const gcFeePercentage = Math.min(30, Math.max(0, raw.gcFeePercentage || 0));
  const laborHours = Math.max(0, raw.laborHours || 0);
  const hourlyWage = Math.max(0, raw.hourlyWage || 0);
  const homeSize = Math.max(0, raw.homeSize || 0);

  // Cash savings = the fee you avoid by managing the project yourself.
  const gcFeeSavings = estimatedCost * (gcFeePercentage / 100);

  // Imputed value of your own time. NOT cash savings — see the header note.
  const laborValueSavings = laborHours * hourlyWage;

  // Headline is the fee only. No labor value folded in.
  const totalSavings = gcFeeSavings;

  // Equals the fee percentage whenever there is a cost to take it from;
  // 0 rather than NaN when the budget field is empty.
  const percentageSaved = estimatedCost > 0 ? (gcFeeSavings / estimatedCost) * 100 : 0;

  // Derived for display only.
  const netProjectCost = estimatedCost - gcFeeSavings;
  const fullTimeWeeks = laborHours / 40;
  const costPerSqFt = homeSize > 0 ? estimatedCost / homeSize : 0;
  const netCostPerSqFt = homeSize > 0 ? netProjectCost / homeSize : 0;
  // What the fee you kept works out to per hour you put in. The most
  // decision-useful number here: compare it to your own hourly rate.
  const returnPerHour = laborHours > 0 ? gcFeeSavings / laborHours : 0;

  const lines: CalcLine[] = [
    {
      id: 'gc-contract',
      label: 'Same build with a GC',
      qty: Math.round(estimatedCost),
      unit: 'USD',
      detail: 'All-in contract price you entered, builder’s fee included',
    },
    {
      id: 'gc-fee',
      label: 'Builder’s fee you avoid',
      qty: Math.round(gcFeeSavings),
      unit: 'USD',
      detail: `${formatNum(gcFeePercentage)}% of the contract price`,
    },
    {
      id: 'net-cost',
      label: 'Your cost, managing it yourself',
      qty: Math.round(netProjectCost),
      unit: 'USD',
      detail: 'Contract price less the fee — subs and materials still get paid',
    },
    ...(homeSize > 0
      ? [
          {
            id: 'cost-per-sqft',
            label: 'Your cost per square foot',
            qty: Math.round(netCostPerSqFt),
            unit: 'USD/sq ft',
            detail: `vs. ${formatNum(Math.round(costPerSqFt))} per sq ft with a GC`,
          },
        ]
      : []),
    {
      id: 'hours',
      label: 'Hours you put in',
      qty: Math.round(laborHours),
      unit: 'hours',
      detail: 'Management time plus whatever you swing a hammer on',
    },
    {
      id: 'weeks',
      label: 'At 40 hours a week, that is',
      qty: round1(fullTimeWeeks),
      unit: 'weeks',
      detail: 'Full-time equivalent — most owner-builders spread it over evenings and weekends',
    },
    {
      id: 'sweat-equity',
      label: 'Value of your hours (not cash)',
      qty: Math.round(laborValueSavings),
      unit: 'USD',
      detail: 'Sweat equity you contribute — deliberately excluded from the headline',
    },
    {
      id: 'return-per-hour',
      label: 'Fee kept, per hour you work',
      qty: Math.round(returnPerHour),
      unit: 'USD/hr',
      detail: 'The fee you avoid, spread across your hours — compare it to your own rate',
    },
  ];

  return {
    hero: {
      qty: Math.round(totalSavings),
      unit: 'saved',
      label: 'Cash saved vs. hiring a GC',
      kind: 'currency',
      detail: heroDetail({
        percentageSaved,
        estimatedCost,
        homeSize,
        netCostPerSqFt,
        costPerSqFt,
      }),
    },
    lines,
    // No cost dimension line: the hero IS the dollar figure, and the sheet's
    // cost band is labelled for material pricing, which this sheet has none of.
    notes: [
      'Cash savings is the builder’s fee only. The value of your own hours is listed separately — adding it in would double-count labor the budget already carries.',
      'Assumes the fee is quoted as a percentage of the total contract price, and that you can buy materials and sub labor at the same prices a GC would.',
      'Excludes what owner-building adds back: builder’s-risk insurance, permit runs, re-work, and financing that may price differently without a licensed GC.',
      'Estimate only — not financial advice.',
    ],
    contractPrice: estimatedCost,
    gcFeeSavings,
    laborValueSavings,
    totalSavings,
    percentageSaved,
    netProjectCost,
    fullTimeWeeks,
    costPerSqFt,
    netCostPerSqFt,
    returnPerHour,
  };
}

function heroDetail({
  percentageSaved,
  estimatedCost,
  homeSize,
  netCostPerSqFt,
  costPerSqFt,
}: {
  percentageSaved: number;
  estimatedCost: number;
  homeSize: number;
  netCostPerSqFt: number;
  costPerSqFt: number;
}): string {
  const base = `${formatNum(round1(percentageSaved))}% of a ${formatUsd(estimatedCost)} contract price.`;
  if (homeSize <= 0 || estimatedCost <= 0) return base;
  return `${base} That is ${formatUsd(netCostPerSqFt)} per sq ft instead of ${formatUsd(costPerSqFt)}.`;
}

function formatNum(value: number): string {
  return new Intl.NumberFormat('en-US', { maximumFractionDigits: 2 }).format(value);
}

function formatUsd(value: number): string {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    maximumFractionDigits: 0,
  }).format(value);
}

function round1(value: number): number {
  return Math.round(value * 10) / 10;
}
