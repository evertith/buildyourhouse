import { RATES } from '../prices.ts';
import { allowance, line } from '../types.ts';
import type { PhaseFn } from './shared.ts';
import { n } from './shared.ts';

/**
 * Drywall and paint, by the drywall and paint sheets' rules
 * (src/lib/calc/drywall.ts, paint.ts): finished wall area is 2.7 × floor
 * area (both faces of partitions plus the inside of exterior walls, after
 * openings), ceilings are the floor area plus the garage, so board lands
 * at the classic 3.7 × floor; 4 × 8 sheets with 10% waste; a bucket of
 * compound per 450 sq ft, a roll of tape per 1,350, a pound of screws per
 * 200. Primer and two coats at 350 sq ft per gallon; trim enamel per room.
 * Finish-sensitive: premium runs ⅝-in board, level-5 finish, better paint.
 */
export const drywallPaint: PhaseFn = (g) => {
  const heated = g.heatedSf.value;
  const wallArea = heated * 2.7 * (g.wallHeightFt.value / 9);
  const ceilingArea = heated + g.garageSf.value;
  const boardArea = wallArea + ceilingArea;

  const sheets = Math.ceil((boardArea / 32) * 1.1);
  const mud = Math.max(1, Math.ceil(boardArea / 450));
  const tape = Math.max(1, Math.ceil(boardArea / 1350));
  const screws = Math.max(1, Math.ceil(boardArea / 200));
  const bead = Math.ceil(g.rooms.value.count * 2.5);

  const wallGallons = Math.ceil((wallArea * 2) / 350);
  const ceilingGallons = Math.ceil((heated * 2) / 350);
  const primer = Math.ceil(boardArea / (350 * 0.85));
  const trim = Math.max(1, Math.round((heated / 150) * 0.5 * 2 * 2) / 2);

  return {
    id: 'drywallPaint',
    name: 'Drywall and paint',
    note: 'Hang, finish, prime, two coats throughout',
    lines: [
      line('board', 'Drywall, ½ in × 4 × 8', sheets, RATES.drywallSheet, `${n(boardArea)} sq ft of walls and ceilings, 10% waste`),
      line('mud', 'Joint compound', mud, RATES.mudBucket, '4.5-gal all-purpose, one per 450 sq ft of board'),
      line('tape', 'Joint tape', tape, RATES.tapeRoll, '500-ft rolls'),
      line('screws', 'Drywall screws', screws, RATES.screwBox, '#6 × 1¼ in, a pound per 200 sq ft'),
      line('bead', 'Corner bead', bead, RATES.cornerBead, '8-ft sticks'),
      line('primer', 'Drywall primer', primer, RATES.primerGal, 'PVA, one coat on new board'),
      line('wall-paint', 'Wall paint', wallGallons, RATES.wallPaintGal, `Two coats on ${n(wallArea)} sq ft at 350 sq ft per gallon`),
      line('ceiling-paint', 'Ceiling paint', ceilingGallons, RATES.wallPaintGal, 'Flat white, two coats'),
      line('trim-paint', 'Trim enamel', trim, RATES.trimPaintGal, 'Semi-gloss on doors, casing, and base'),
      allowance('sundries', 'Masking, rollers, sanding, texture', RATES.paintSundries),
    ],
  };
};
