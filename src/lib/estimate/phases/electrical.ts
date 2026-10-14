import { RATES } from '../prices.ts';
import { allowance, line } from '../types.ts';
import type { PhaseFn } from './shared.ts';
import { n } from './shared.ts';

/**
 * Electrical: 200-amp service, rough-in priced per heated square foot
 * (wire, boxes, breakers), devices and plates per room, smoke and CO
 * detectors, a fixture allowance per room, exterior lights.
 */
export const electrical: PhaseFn = (g) => {
  const heated = g.heatedSf.value;
  const rooms = g.rooms.value;
  const detectors = rooms.bedrooms + g.stories.value + 1;

  return {
    id: 'electrical',
    name: 'Electrical',
    note: '200A service, rough-in, devices, fixtures, smoke detectors',
    licensed: true,
    lines: [
      line('service', '200A panel and service entrance', 1, RATES.service200A, 'Panel, meter base, service cable, grounding'),
      line('wiring', 'Rough-in wire, boxes, breakers', Math.round(heated), RATES.wiringPerSf, `Per heated square foot, ${n(heated)} sq ft`),
      line('devices', 'Switches, receptacles, plates', rooms.count, RATES.devicesPerRoom, `${rooms.count} rooms, GFCI and AFCI where required`),
      line('detectors', 'Smoke and CO detectors', detectors, RATES.smokeCo, 'Interconnected, one per bedroom and floor'),
      line('fixtures', 'Light fixtures and fans', rooms.count, RATES.fixturesPerRoom, 'Allowance per room'),
      allowance('exterior', 'Exterior lights and outlets', RATES.exteriorLights),
    ],
  };
};
