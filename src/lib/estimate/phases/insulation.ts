import { RATES } from '../prices.ts';
import { allowance, line } from '../types.ts';
import type { Line } from '../types.ts';
import type { PhaseFn } from './shared.ts';
import { n } from './shared.ts';

/**
 * Insulation, by the insulation sheet's bag charts (src/lib/calc/insulation.ts):
 * R-19 batts in the 2 × 6 walls at 87 sq ft per bag, blown fiberglass to
 * R-49 in the attic at 31 sq ft per bag, R-19 batts under a crawl-space
 * floor, rigid foam on basement walls, and an air-sealing allowance.
 */
export const insulation: PhaseFn = (g) => {
  const op = g.openings.value;
  const wallCavity = g.extWallAreaSf.value - op.windowAreaSf - op.extDoors * 20 - op.garageDoors * 112;
  const wallBags = Math.ceil((wallCavity / 87) * 1.05);
  const ceiling = g.footprintSf.value;
  const atticBags = Math.ceil(ceiling / 31);
  const kind = g.foundation.value;

  const lines: Line[] = [
    line('walls', 'R-19 wall batts', wallBags, RATES.battBagR19, `${n(wallCavity)} sq ft of wall cavity, 5% cut allowance`),
    line('attic', 'Blown attic insulation to R-49', atticBags, RATES.blownBagR49, `${n(ceiling)} sq ft of ceiling, blower rental usually free with the bags`),
  ];
  if (kind === 'crawl') {
    const floorBags = Math.ceil((g.footprintSf.value / 87) * 1.05);
    lines.push(line('floor', 'R-19 floor batts', floorBags, RATES.battBagR19, 'Under the crawl-space floor, between joists'));
  }
  if (kind === 'basement') {
    const wallSf = Math.ceil(g.perimeterLf.value * 8);
    lines.push(line('basement', 'Rigid foam, basement walls', wallSf, RATES.rigidFoamSf, '2-in XPS on the inside of the walls'));
  }
  lines.push(allowance('sealing', 'Air sealing foam and caulk', RATES.airSealing, 'Top plates, penetrations, rim joist'));

  return {
    id: 'insulation',
    name: 'Insulation',
    note:
      kind === 'crawl'
        ? 'Wall batts, blown attic, crawl-space floor, air sealing'
        : kind === 'basement'
          ? 'Wall batts, blown attic, basement walls, air sealing'
          : 'Wall batts, blown attic, air sealing',
    lines,
  };
};
