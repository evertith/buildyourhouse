import { RATES } from '../prices.ts';
import { allowance, line, clamp, roundTo } from '../types.ts';
import type { PhaseFn } from './shared.ts';
import { n } from './shared.ts';

/**
 * HVAC: a heat pump sized at one ton per 600 heated square feet, moved by
 * the state's climate factor and rounded to the half ton; ductwork per
 * heated square foot; thermostat (two with an upper floor); bath fans.
 */
export const hvac: PhaseFn = (g, ctx) => {
  const heated = g.heatedSf.value;
  const tons = clamp(roundTo((heated / 600) * ctx.state.climate, 0.5), 1.5, 7);
  const thermostats = g.stories.value > 1 ? 2 : 1;
  const fans = Math.ceil(g.rooms.value.baths);

  return {
    id: 'hvac',
    name: 'HVAC',
    note: `${tons}-ton heat pump, ductwork, thermostat, bath fans`,
    licensed: true,
    lines: [
      line('heat-pump', 'Heat pump and air handler', tons, RATES.heatPumpTon, `${tons} tons for ${n(heated)} sq ft in ${ctx.state.name}`),
      line('duct', 'Ductwork, boots, registers', Math.round(heated), RATES.ductPerSf, 'Flex and trunk duct per heated square foot'),
      line('thermostat', thermostats > 1 ? 'Thermostats, zoned' : 'Thermostat', thermostats, RATES.thermostat),
      line('fans', 'Bath exhaust fans', fans, RATES.bathFan, 'Ducted to the outside'),
      allowance('sundries', 'Line set, pad, disconnect, condensate', RATES.hvacSundries),
    ],
  };
};
