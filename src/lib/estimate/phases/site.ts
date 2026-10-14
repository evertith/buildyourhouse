import { RATES } from '../prices.ts';
import { allowance, line } from '../types.ts';
import type { PhaseFn } from './shared.ts';
import { n } from './shared.ts';

/**
 * Site work: clearing, rough grade, driveway base, erosion control, and
 * temporary power. Clearing and grading are equipment and labor, so the
 * material side is small and the labor ratio is the highest on the ledger.
 */
export const site: PhaseFn = (g) => {
  const perimeter = g.perimeterLf.value;

  // 100-ft gravel drive, 12 ft wide, 8 in deep; 1.4 tons per cubic yard.
  const driveCuYd = (100 * 12 * (8 / 12)) / 27;
  const gravelTons = Math.ceil(driveCuYd * 1.4);

  // Silt fence around the disturbed area, about 2.5× the house perimeter.
  const siltLf = Math.ceil(perimeter * 2.5);

  return {
    id: 'site',
    name: 'Site work',
    note: 'Clearing, rough grade, driveway base, erosion control, temporary power',
    lines: [
      allowance(
        'fill',
        'Fill and topsoil',
        RATES.fillTopsoil,
        `Rough grade over ${n(g.footprintSf.value)} sq ft of footprint plus the drive and yard`
      ),
      line(
        'gravel',
        'Gravel driveway base',
        gravelTons,
        RATES.gravelTon,
        '100-ft drive, 12 ft wide, 8 in of crusher run'
      ),
      line(
        'silt',
        'Silt fence',
        siltLf,
        RATES.siltFenceLf,
        'Around the disturbed area, stakes included'
      ),
      allowance(
        'entrance',
        'Construction entrance',
        RATES.constructionEntrance,
        'Stone pad at the drive so trucks do not track mud onto the road'
      ),
      line('power', 'Temporary power pole and meter', 1, RATES.tempPower, 'Rented pole, meter base, GFCI outlets'),
    ],
  };
};
