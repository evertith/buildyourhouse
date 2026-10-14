import { RATES } from '../prices.ts';
import { allowance, line, ceilTo } from '../types.ts';
import type { PhaseFn } from './shared.ts';

/**
 * Final and move-in: appliances, the concrete drive and walks, seed and
 * shrubs, the last clean and the dumpsters, the odds and ends every build
 * ends with. Flatwork is 720 sq ft of drive and 150 sq ft of walks at 4 in.
 */
export const final: PhaseFn = () => {
  const flatworkSf = 720 + 150;
  const flatworkYd = ceilTo(((flatworkSf * (4 / 12)) / 27) * 1.1, 0.5);

  return {
    id: 'final',
    name: 'Final and move-in',
    note: 'Appliances, landscaping, concrete driveway and walks, cleanup',
    lines: [
      allowance('appliances', 'Appliance package', RATES.appliances, 'Range, refrigerator, dishwasher, microwave, washer, dryer'),
      line('flatwork', 'Concrete drive and walks', flatworkYd, RATES.readyMixYd, `${flatworkSf} sq ft at 4 in, 10% order factor`),
      line('flatwork-sundries', 'Mesh, forms, gravel for flatwork', flatworkSf, RATES.flatworkSundriesSf),
      allowance('seed', 'Seed, straw, and topsoil', RATES.seedStraw, 'Disturbed area around the house and drive'),
      allowance('shrubs', 'Foundation shrubs and mulch', RATES.shrubs),
      allowance('clean', 'Final clean', RATES.finalClean),
      line('dumpsters', 'Dumpsters', 3, RATES.dumpster, '20-yard, one per phase group'),
      allowance('odds', 'Mailbox, house numbers, odds and ends', RATES.oddsAndEnds),
    ],
  };
};
