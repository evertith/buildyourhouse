import { RATES } from '../prices.ts';
import { allowance, line } from '../types.ts';
import type { PhaseFn } from './shared.ts';
import { n, pitchFactor } from './shared.ts';

/**
 * Roofing, by the roofing sheet's conventions (src/lib/calc/roofing.ts):
 * sloped area = plan area × pitch factor; waste 10 / 15 / 20% by cut-up;
 * three bundles per square; synthetic underlayment in 10-square rolls;
 * ice-and-water on the eaves (and valleys on a cut-up roof); starter on
 * eaves and rakes; cap on ridges and hips; drip edge the whole perimeter;
 * ridge vent; 2.5 lb of nails per square.
 */
const WASTE = { gable: 0.1, hip: 0.15, cutup: 0.2 } as const;

export const roofing: PhaseFn = (g) => {
  const roof = g.roof.value;
  const sloped = roof.planeAreaSf * pitchFactor(roof.pitch);
  const waste = WASTE[roof.complexity];
  const order = sloped * (1 + waste);
  const squares = order / 100;

  const bundles = Math.ceil(squares * 3);
  const underlayment = Math.ceil((sloped / 1000) * 1.1);
  const iceWaterLf = roof.eaveLf + (roof.complexity === 'cutup' ? roof.hipValleyLf / 2 : 0);
  const iceWater = Math.ceil(iceWaterLf / 65);
  const starter = Math.ceil((roof.eaveLf + roof.rakeLf) / 105);
  const cap = Math.ceil((roof.ridgeLf + roof.hipValleyLf) / 33);
  const drip = Math.ceil(((roof.eaveLf + roof.rakeLf) * 1.05) / 10);
  const vent = Math.ceil(roof.ridgeLf / 4);
  const nails = Math.ceil(squares * 2.5);

  return {
    id: 'roofing',
    name: 'Roofing',
    note: 'Architectural shingles, underlayment, ice and water, flashing, ridge vent',
    lines: [
      line('shingles', 'Architectural shingles', bundles, RATES.shingleBundle, `${squares.toFixed(1)} squares at ${roof.pitch}:12 with ${Math.round(waste * 100)}% waste, 3 bundles per square`),
      line('underlayment', 'Synthetic underlayment', underlayment, RATES.underlaymentRoll, `${n(sloped)} sq ft of deck, 10-square rolls, 10% for laps`),
      line('ice-water', 'Ice and water shield', iceWater, RATES.iceWaterRoll, `${n(iceWaterLf)} lf of eaves${roof.complexity === 'cutup' ? ' and valleys' : ''}, 65 lf per roll`),
      line('starter', 'Starter strip', starter, RATES.starterBundle, `${n(roof.eaveLf + roof.rakeLf)} lf of eaves and rakes`),
      line('cap', 'Ridge and hip cap', cap, RATES.ridgeCapBundle, `${n(roof.ridgeLf + roof.hipValleyLf)} lf, 33 lf per bundle`),
      line('drip', 'Drip edge', drip, RATES.dripStick, '10-ft aluminum, full perimeter, 5% laps'),
      line('vent', 'Ridge vent', vent, RATES.ridgeVent, `${n(roof.ridgeLf)} lf of ridge, 4-ft sticks`),
      allowance('flashing', 'Flashing and pipe boots', RATES.flashingBoots, 'Step, wall, and vent flashing'),
      line('nails', 'Roofing nails', nails, RATES.nailLb, '1¼ in coil, 2.5 lb per square'),
    ],
  };
};
