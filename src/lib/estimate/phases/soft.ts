import { BUILDERS_RISK_SHARE, PERMIT_PER_SF, RATES } from '../prices.ts';
import { allowance } from '../types.ts';
import type { Geometry } from '../geometry.ts';
import type { PhaseContext, PhaseSpec } from './shared.ts';
import { n } from './shared.ts';

/**
 * Before you break ground: the money that is paid, not built. Permit and
 * plan review, survey, the water and sewer tap (or impact fees), a year of
 * builder's risk insurance, and the plans. The permit base and the tap fee
 * come from the state table; builder's risk is a share of the hard cost,
 * so this phase runs after the others.
 */
export function soft(g: Geometry, ctx: PhaseContext, hardCostMid: number): PhaseSpec {
  const heated = g.heatedSf.value;
  const st = ctx.state;
  const perSf = PERMIT_PER_SF * heated;
  const risk = hardCostMid * BUILDERS_RISK_SHARE;
  const plans =
    ctx.finish === 'premium' ? RATES.plansPremium : ctx.finish === 'basic' ? RATES.plansBasic : RATES.plansStandard;

  return {
    id: 'soft',
    name: 'Before you break ground',
    note: 'Permit and plan review, survey, tap or impact fees, builder’s risk, plans',
    soft: true,
    lines: [
      allowance(
        'permit',
        'Building permit',
        { low: st.permitBase.low + perSf, high: st.permitBase.high + perSf, unit: 'allowance' },
        `${st.name} base plus $${PERMIT_PER_SF.toFixed(2)} per heated sq ft (${n(heated)} sq ft)`
      ),
      allowance('review', 'Plan review and inspections', RATES.planReview),
      allowance('survey', 'Survey and site plan', RATES.survey, 'Boundary and stake-out'),
      allowance(
        'tap',
        'Water and sewer tap or impact fees',
        { ...st.tapFee, unit: 'allowance' },
        'Municipal connection; a well and septic on a rural lot usually cost more'
      ),
      allowance(
        'risk',
        'Builder’s risk insurance, 12 months',
        { low: risk * 0.8, high: risk * 1.2, unit: 'allowance' },
        'About half a percent of the hard cost'
      ),
      allowance(
        'plans',
        ctx.finish === 'premium' ? 'Custom plans, stamped' : 'Stock plans, stamped and modified',
        plans
      ),
    ],
  };
}
