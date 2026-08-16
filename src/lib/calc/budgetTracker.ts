import { CalcLine, CalcResult } from './types';
import { formatCurrency } from './format';

/**
 * Budget-vs-actual worksheet (W-04): what each phase was supposed to cost,
 * what it actually cost, and how much of the contingency the difference has
 * eaten. Unlike the trade takeoffs this is a ledger — the visitor supplies
 * every number and the engine only does the arithmetic.
 *
 * Math is the legacy calculateBudgetTracker() unchanged, including its sign
 * convention: variance = planned − actual, so POSITIVE IS UNDER BUDGET.
 * (The UI never shows a raw signed figure; it shows the magnitude with an
 * "over"/"under" word, so the convention stays internal.)
 *
 * Conventions:
 * - A phase is "on track" while it is within ±5% of its planned number;
 *   past that it counts as over or under. Same band decides the overall
 *   status, applied to the total.
 * - The contingency reserve is a percentage of the PLANNED total, and only
 *   an overrun draws it down — running under budget does not top it back up
 *   beyond the original reserve.
 */

export interface BudgetCategoryInput {
  id: string;
  label: string;
  /** Budgeted for this phase. */
  planned: number;
  /** Spent so far on this phase. */
  actual: number;
}

export interface BudgetTrackerInputs {
  categories: BudgetCategoryInput[];
  /** Reserve as a % of the planned total. Defaults to 15. */
  contingencyPct?: number;
}

export type BudgetStatus = 'under' | 'on-track' | 'over';

export interface BudgetCategoryAnalysis extends BudgetCategoryInput {
  /** planned − actual: positive means the phase came in under. */
  variance: number;
  variancePct: number;
  status: BudgetStatus;
}

export interface BudgetTrackerResult extends CalcResult {
  totalPlanned: number;
  totalActual: number;
  totalVariance: number;
  variancePct: number;
  contingencyAmount: number;
  contingencyRemaining: number;
  categories: BudgetCategoryAnalysis[];
  overallStatus: BudgetStatus;
  /** Phases with money logged against them. */
  startedCount: number;
  /**
   * Variance across the phases that have actually spent money. Mid-build
   * this is the number that matters: the whole-plan variance is dominated
   * by work nobody has paid for yet.
   */
  varianceToDate: number;
  /** Run-specific advice — rendered next to the inputs. */
  flags: string[];
}

/** The legacy tracker's starting phases and budgets — a ~$250k plan. */
export const DEFAULT_BUDGET_CATEGORIES: BudgetCategoryInput[] = [
  { id: 'site-foundation', label: 'Site Prep & Foundation', planned: 45000, actual: 0 },
  { id: 'framing-exterior', label: 'Framing & Exterior', planned: 65000, actual: 0 },
  { id: 'rough-ins', label: 'Rough-Ins (MEP)', planned: 40000, actual: 0 },
  { id: 'insulation-drywall', label: 'Insulation & Drywall', planned: 25000, actual: 0 },
  { id: 'interior-finishes', label: 'Interior Finishes', planned: 50000, actual: 0 },
  { id: 'final-landscaping', label: 'Final & Landscaping', planned: 25000, actual: 0 },
];

export const DEFAULT_CONTINGENCY_PCT = 15;

/** Money fields are user-typed; never let a stray value poison the ledger. */
function money(value: number): number {
  return Number.isFinite(value) && value > 0 ? value : 0;
}

export function calculateBudgetTracker(raw: BudgetTrackerInputs): BudgetTrackerResult {
  const contingencyPct = Math.max(0, raw.contingencyPct ?? DEFAULT_CONTINGENCY_PCT);
  const inputs = raw.categories.map((c) => ({
    ...c,
    planned: money(c.planned),
    actual: money(c.actual),
  }));

  const totalPlanned = inputs.reduce((sum, c) => sum + c.planned, 0);
  const totalActual = inputs.reduce((sum, c) => sum + c.actual, 0);
  const totalVariance = totalPlanned - totalActual;
  // Guard against divide-by-zero (nothing budgeted) → "NaN%".
  const variancePct = totalPlanned > 0 ? (totalVariance / totalPlanned) * 100 : 0;

  const contingencyAmount = totalPlanned * (contingencyPct / 100);
  const contingencyRemaining = contingencyAmount - Math.max(0, -totalVariance);

  const categories: BudgetCategoryAnalysis[] = inputs.map((c) => {
    const variance = c.planned - c.actual;
    const pct = c.planned > 0 ? (variance / c.planned) * 100 : 0;
    let status: BudgetStatus;
    if (variance > c.planned * 0.05) status = 'under';
    else if (variance < -c.planned * 0.05) status = 'over';
    else status = 'on-track';
    return { ...c, variance, variancePct: pct, status };
  });

  let overallStatus: BudgetStatus;
  if (variancePct > 5) overallStatus = 'under';
  else if (variancePct < -5) overallStatus = 'over';
  else overallStatus = 'on-track';

  const startedCount = categories.filter((c) => c.actual > 0).length;
  const started = startedCount > 0;
  const allStarted = startedCount === categories.length && categories.length > 0;
  const varianceToDate = categories
    .filter((c) => c.actual > 0)
    .reduce((sum, c) => sum + c.variance, 0);

  const lines: CalcLine[] = categories.map((c) => ({
    id: c.id,
    label: c.label,
    // A phase nobody has spent on is not "under budget" — it is unspent.
    qty: Math.abs(c.variance),
    unit: c.actual === 0 ? 'unspent' : directionWord(c.variance),
    detail: categoryDetail(c),
  }));

  lines.push({
    id: 'contingency',
    label: 'Contingency reserve',
    qty: Math.abs(Math.round(contingencyRemaining)),
    unit: contingencyRemaining < 0 ? 'overdrawn' : 'unspent',
    detail: `${contingencyPct}% of the ${formatCurrency(totalPlanned)} plan = ${formatCurrency(
      contingencyAmount
    )}; overruns come out of this first`,
  });

  return {
    hero: started
      ? spendingHero({
          totalVariance,
          variancePct,
          totalPlanned,
          totalActual,
          contingencyRemaining,
          allStarted,
          startedCount,
          phaseCount: categories.length,
          varianceToDate,
        })
      : emptyHero(totalPlanned),
    lines,
    notes: [
      'Your numbers, your arithmetic — nothing here is estimated for you.',
      'A phase counts as on track while it is within 5% of plan.',
      'Contingency is a share of the planned total and only an overrun draws it down.',
    ],
    totalPlanned,
    totalActual,
    totalVariance,
    variancePct,
    contingencyAmount,
    contingencyRemaining,
    categories,
    overallStatus,
    startedCount,
    varianceToDate,
    flags: started
      ? buildFlags(categories, overallStatus, contingencyAmount, contingencyRemaining, allStarted, startedCount)
      : ['Nothing logged yet — enter what each phase has actually cost as the invoices land.'],
  };
}

/** "over budget" / "under budget" / "on budget", for the schedule column. */
function directionWord(variance: number): string {
  if (variance > 0) return 'under budget';
  if (variance < 0) return 'over budget';
  return 'on budget';
}

function categoryDetail(c: BudgetCategoryAnalysis): string {
  const base = `Planned ${formatCurrency(c.planned)} · spent ${formatCurrency(c.actual)}`;
  if (c.actual === 0) return `${base} — nothing logged yet`;
  if (c.status === 'on-track') return `${base} — within 5% of plan`;
  if (c.planned === 0) return `${base} — no budget was set for this phase`;
  return `${base} — ${Math.abs(c.variancePct).toFixed(1)}% ${c.variance < 0 ? 'over' : 'under'}`;
}

/**
 * Nothing spent yet: showing "$250,000 under budget" would be true and
 * useless, so the hero carries the plan total until the first dollar is
 * logged. Arithmetic is untouched either way.
 */
function emptyHero(totalPlanned: number): CalcResult['hero'] {
  return {
    qty: totalPlanned,
    unit: 'planned',
    label: 'Planned total — nothing logged yet',
    kind: 'currency',
    detail: 'Enter what each phase has actually cost to see variance and contingency burn.',
  };
}

interface HeroContext {
  totalVariance: number;
  variancePct: number;
  totalPlanned: number;
  totalActual: number;
  contingencyRemaining: number;
  allStarted: boolean;
  startedCount: number;
  phaseCount: number;
  varianceToDate: number;
}

/**
 * Mid-build, most of the whole-plan variance is work nobody has paid for
 * yet, so calling it "under budget" is the false comfort this page warns
 * about. Until every phase has costs logged, the headline says what the
 * figure actually is — plan left unspent — and the detail carries the
 * variance on the work that has been paid for.
 */
function spendingHero(c: HeroContext): CalcResult['hero'] {
  const spent = `${formatCurrency(c.totalActual)} spent against ${formatCurrency(c.totalPlanned)} planned`;
  const reserve = `${formatCurrency(c.contingencyRemaining)} of contingency left`;
  const logged = `${c.startedCount} of ${c.phaseCount} phases have costs logged`;
  const toDate =
    c.varianceToDate === 0
      ? `on plan so far (${logged})`
      : `${formatCurrency(Math.abs(c.varianceToDate))} ${c.varianceToDate < 0 ? 'over' : 'under'} on the work paid for (${logged})`;

  if (!c.allStarted && c.totalVariance >= 0) {
    return {
      qty: c.totalVariance,
      unit: 'unspent',
      label: 'Unspent in the plan',
      kind: 'currency',
      detail: `${spent} — ${toDate}, ${reserve}`,
    };
  }

  const word = directionWord(c.totalVariance);
  return {
    qty: Math.abs(c.totalVariance),
    unit: word,
    label: `${word.charAt(0).toUpperCase()}${word.slice(1)} vs. plan`,
    kind: 'currency',
    detail: c.allStarted
      ? `${spent} — ${Math.abs(c.variancePct).toFixed(1)}% ${c.totalVariance < 0 ? 'over' : 'under'}, ${reserve}`
      : `${spent} — ${toDate}, ${reserve}`,
  };
}

/**
 * Same trigger conditions as the legacy recommendations, in the same order;
 * the wording is the site's, not the old placeholder copy.
 */
function buildFlags(
  categories: BudgetCategoryAnalysis[],
  overallStatus: BudgetStatus,
  contingencyAmount: number,
  contingencyRemaining: number,
  allStarted: boolean,
  startedCount: number
): string[] {
  const flags: string[] = [];
  const over = categories.filter((c) => c.status === 'over');

  if (over.length > 0) {
    flags.push(
      `${over.length} ${over.length === 1 ? 'phase is' : 'phases are'} over budget — ${
        allStarted
          ? 'with every phase underway, the difference has to come out of scope or funding.'
          : 'take the difference out of the phases you have not started yet.'
      }`
    );
  }
  if (contingencyRemaining < contingencyAmount * 0.3) {
    flags.push(
      contingencyRemaining < 0
        ? 'The contingency reserve is spent and then some. Every further overrun comes straight out of your pocket.'
        : 'Contingency is down to its last third. Cut scope now, while the cuts are still cheap.'
    );
  }
  if (overallStatus === 'over' && contingencyRemaining < 0) {
    flags.push('Over budget with the reserve gone. Re-plan the rest of the build before the next phase starts.');
  }
  if (overallStatus === 'under') {
    // Same trigger as the legacy tracker, but partway through a build the
    // under-plan figure is mostly unbought work, so say so.
    flags.push(
      allStarted
        ? 'Running under budget. Hold the difference until finishes are priced — that is where it usually goes.'
        : `Only ${startedCount} of ${categories.length} phases have costs logged, so most of the under-plan figure is work you have not paid for yet.`
    );
  }
  if (categories.some((c) => Math.abs(c.variancePct) > 15)) {
    flags.push('At least one phase is more than 15% off plan. Check the estimate, not just the spending.');
  }
  return flags;
}
