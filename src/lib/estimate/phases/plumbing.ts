import { RATES } from '../prices.ts';
import { allowance, line } from '../types.ts';
import type { PhaseFn } from './shared.ts';

/**
 * Plumbing, rough-in and finish. Fixtures count three per bath (including
 * half baths' two), two in the kitchen, two in the laundry, two hose bibs;
 * rough-in is priced per fixture (PEX supply, PVC drain-waste-vent, valves)
 * plus the service lines from the house to the tap or well. Finish is
 * toilets, tubs and showers, faucets, the kitchen sink, the water heater.
 */
export const plumbing: PhaseFn = (g) => {
  const rooms = g.rooms.value;
  const bathsCeil = Math.ceil(rooms.baths);
  const fullBaths = Math.floor(rooms.baths);
  const fixtures = Math.round(rooms.baths * 3) + rooms.kitchens * 2 + 2 + 2;

  return {
    id: 'plumbing',
    name: 'Plumbing',
    note: `${rooms.baths} baths, kitchen, laundry; rough-in and finish`,
    licensed: true,
    lines: [
      line('rough', 'Rough-in, per fixture', fixtures, RATES.roughPerFixture, 'PEX supply, PVC drain-waste-vent, shutoffs, manifold'),
      allowance('service', 'Water and sewer lines to the house', RATES.serviceLines, 'From the meter or well and the sewer tap or septic'),
      line('heater', 'Water heater', 1, RATES.waterHeater, '50-gallon electric or gas'),
      line('toilets', 'Toilets', bathsCeil, RATES.toilet),
      line('tubs', 'Tubs and showers', fullBaths, RATES.tubShower, 'One tub-shower unit, the rest showers, valves included'),
      line('faucets', 'Lavatory faucets and drains', bathsCeil, RATES.faucet),
      line('sink', 'Kitchen sink and faucet', rooms.kitchens, RATES.kitchenSink),
      line('bibs', 'Hose bibs', 2, RATES.hoseBib),
      line('laundry', 'Laundry box', 1, RATES.laundryBox),
      allowance('sundries', 'Supply lines, traps, ice-maker and dishwasher kits', RATES.plumbingSundries),
    ],
  };
};
