import { CalcLine, CalcResult } from './types';

/**
 * Owner-builder schedule worksheet (W-03): how long the build takes given
 * the hours you can actually put in, how much of the work you keep, and how
 * fast you move at your experience level.
 *
 * The engine is the legacy calculateTimelineEstimate() math, moved here
 * unchanged — same inputs produce the same months, weeks, hours, and phase
 * durations. The clamps below are deliberately the legacy expressions
 * (`Math.max(0, x || 0)`) rather than the shared clamp() helper: clamp()
 * needs an upper bound, and inventing one would change results for large
 * inputs the old tool accepted.
 *
 * Estimating conventions (each stated on the page):
 * - 1.75 personal hours per square foot for a complete DIY build. A 2,000
 *   sq ft house lands near 3,500 hands-on hours, which lines up with the
 *   site's time-commitment page and the ~15-month Census figure for
 *   owner-built homes.
 * - Experience multiplier: beginner 1.4×, intermediate 1.0×, experienced
 *   0.8× — the learning curve is real and it is the largest single factor.
 * - Helpers: each consistent helper divides the hours by an extra 0.6, so
 *   one helper is 1/1.6 of the solo hours, not half.
 * - Only your DIY share of the work is on your clock; the rest runs on the
 *   subs' schedule in parallel.
 * - Calendar: weeks = your hours ÷ hours you work per week; months =
 *   weeks ÷ 4.33.
 */

export interface TimelineInputs {
  /** Finished square footage. */
  homeSizeSqFt: number;
  /** Hours you can put on the job in a typical week. */
  hoursPerWeek: number;
  /** 0–100: share of the work you keep instead of subbing out. */
  diyPercentage: number;
  experienceLevel: 'beginner' | 'intermediate' | 'experienced';
  /** Consistent helpers — friends and family who actually show up. */
  helpers: number;
}

export interface TimelinePhase {
  id: string;
  name: string;
  weeks: number;
  description: string;
}

export interface TimelineResult extends CalcResult {
  totalMonths: number;
  totalWeeks: number;
  /** Your personal hours on the job, rounded. */
  totalHours: number;
  phases: TimelinePhase[];
  /** Run-specific reality checks — rendered next to the inputs. */
  warnings: string[];
}

const EXPERIENCE_MULTIPLIER: Record<TimelineInputs['experienceLevel'], number> = {
  beginner: 1.4,
  intermediate: 1.0,
  experienced: 0.8,
};

/** Fractions sum to 1.0 — see distributeWeeks() for how they become integers. */
const PHASE_TEMPLATES: { id: string; name: string; fraction: number; description: string }[] = [
  {
    id: 'planning-permitting',
    name: 'Planning & Permitting',
    fraction: 0.15,
    description: 'Design finalization, permit applications, site prep planning',
  },
  {
    id: 'foundation',
    name: 'Foundation',
    fraction: 0.12,
    description: 'Excavation, footings, foundation walls, waterproofing',
  },
  {
    id: 'framing',
    name: 'Framing',
    fraction: 0.2,
    description: 'Floor system, wall framing, roof framing, sheathing',
  },
  {
    id: 'rough-ins',
    name: 'Rough-Ins',
    fraction: 0.18,
    description: 'Electrical, plumbing, HVAC rough-in work',
  },
  {
    id: 'insulation-drywall',
    name: 'Insulation & Drywall',
    fraction: 0.12,
    description: 'Insulation installation, drywall hanging, taping, mudding',
  },
  {
    id: 'interior-finishes',
    name: 'Interior Finishes',
    fraction: 0.15,
    description: 'Trim, doors, cabinets, flooring, painting',
  },
  {
    id: 'final-exterior',
    name: 'Final & Exterior',
    fraction: 0.08,
    description: 'Exterior finishes, landscaping, final inspections, punch list',
  },
];

export function calculateTimeline(raw: TimelineInputs): TimelineResult {
  const homeSizeSqFt = Math.max(0, raw.homeSizeSqFt || 0);
  // Guard against divide-by-zero: 0 hours/week would yield Infinity months.
  const hoursPerWeek = Math.max(1, raw.hoursPerWeek || 0);
  const diyPercentage = Math.min(100, Math.max(0, raw.diyPercentage || 0));
  const helpers = Math.max(0, raw.helpers || 0);

  let baseHours = homeSizeSqFt * 1.75;
  baseHours *= EXPERIENCE_MULTIPLIER[raw.experienceLevel] ?? 0.8;
  baseHours *= 1 / (1 + helpers * 0.6);

  const yourHours = baseHours * (diyPercentage / 100);

  const totalWeeks = Math.ceil(yourHours / hoursPerWeek);
  const totalMonths = Math.round((totalWeeks / 4.33) * 10) / 10;

  const weeks = distributeWeeks(totalWeeks);
  const phases: TimelinePhase[] = PHASE_TEMPLATES.map((p, i) => ({
    id: p.id,
    name: p.name,
    weeks: weeks[i],
    description: p.description,
  }));

  const totalHours = Math.round(yourHours);

  const warnings: string[] = [];
  if (hoursPerWeek < 15) warnings.push('Low weekly hours may extend timeline significantly');
  if (raw.experienceLevel === 'beginner' && diyPercentage > 50)
    warnings.push('High DIY % with beginner experience adds risk');
  if (homeSizeSqFt > 2500 && hoursPerWeek < 20)
    warnings.push('Large home with limited time = long project');
  if (diyPercentage > 70) warnings.push('Very high DIY % requires strong commitment and skills');

  const lines: CalcLine[] = phases.map((p) => ({
    id: p.id,
    label: p.name,
    qty: p.weeks,
    unit: 'weeks',
    detail: p.description,
  }));

  const fullTimeShare = Math.round((hoursPerWeek / 40) * 100);

  return {
    hero: {
      qty: totalMonths,
      unit: 'months',
      label: 'Permits to move-in',
      kind: 'duration',
      detail: `${formatHours(totalHours)} of your own hours at ${hoursPerWeek} hrs/week (${fullTimeShare}% of a full-time job) — about ${totalWeeks} weeks on the calendar`,
    },
    lines,
    notes: [
      'Your hours only — work you sub out runs on the subs’ schedule, not your clock.',
      'No allowance for weather, permit waits, failed inspections, or life. Add buffer.',
      'Phases are shown in sequence; on a real job some of them overlap.',
    ],
    totalMonths,
    totalWeeks,
    totalHours,
    phases,
    warnings,
  };
}

/**
 * Split the calendar into phases by fraction. Largest-remainder, so the
 * phases add up to exactly totalWeeks — rounding each fraction on its own
 * overshoots the total.
 */
function distributeWeeks(totalWeeks: number): number[] {
  const rawWeeks = PHASE_TEMPLATES.map((p) => totalWeeks * p.fraction);
  const floored = rawWeeks.map((w) => Math.floor(w));
  let remainder = totalWeeks - floored.reduce((sum, w) => sum + w, 0);
  const order = rawWeeks
    .map((w, i) => ({ i, frac: w - Math.floor(w) }))
    .sort((a, b) => b.frac - a.frac);
  for (let k = 0; k < order.length && remainder > 0; k++) {
    floored[order[k].i] += 1;
    remainder--;
  }
  return floored;
}

function formatHours(hours: number): string {
  return `${new Intl.NumberFormat('en-US', { maximumFractionDigits: 0 }).format(hours)} hrs`;
}
