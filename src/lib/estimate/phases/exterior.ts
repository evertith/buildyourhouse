import { RATES } from '../prices.ts';
import { allowance, line } from '../types.ts';
import type { PhaseFn } from './shared.ts';
import { n } from './shared.ts';

/**
 * Exterior finish: siding on the net wall area, trim at corners, openings,
 * and the band, soffit and fascia on the eaves and rakes, gutters on the
 * eaves. Finish-sensitive: standard is fiber-cement lap; the multiplier
 * takes basic to vinyl territory and premium toward board-and-batten or
 * masonry accents.
 */
export const exterior: PhaseFn = (g) => {
  const op = g.openings.value;
  const roof = g.roof.value;
  const h = g.wallHeightFt.value;
  const stories = g.stories.value;

  const netWall = g.extWallAreaSf.value - op.windowAreaSf - op.extDoors * 20 - op.garageDoors * 112;
  const siding = Math.ceil(netWall * 1.1);
  const trimLf = Math.ceil(op.windows * 14 + op.extDoors * 17 + 4 * h * stories + g.perimeterLf.value);
  const soffitSf = Math.ceil((roof.eaveLf + roof.rakeLf) * 1.5);
  const fasciaLf = Math.ceil(roof.eaveLf + roof.rakeLf);
  const gutterLf = Math.ceil(roof.eaveLf + 4 * 12);

  return {
    id: 'exterior',
    name: 'Exterior finish',
    note: 'Siding, trim, soffit and fascia, gutters',
    lines: [
      line('siding', 'Fiber-cement lap siding', siding, RATES.sidingSf, `${n(netWall)} sq ft of wall after openings, 10% waste, nails included`),
      line('trim', 'Trim and corner boards', trimLf, RATES.trimLf, 'Window and door casing, corners, band board'),
      line('soffit', 'Soffit', soffitSf, RATES.soffitSf, '18-in vented soffit on eaves and rakes'),
      line('fascia', 'Fascia', fasciaLf, RATES.fasciaLf, 'Wrapped or composite fascia'),
      line('gutters', 'Gutters and downspouts', gutterLf, RATES.gutterLf, 'Aluminum, four downspouts'),
      allowance('sundries', 'Caulk, paint, flashing tape', RATES.exteriorSundries),
    ],
  };
};
