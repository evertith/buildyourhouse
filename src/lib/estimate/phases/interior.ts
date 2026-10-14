import { RATES } from '../prices.ts';
import { line } from '../types.ts';
import type { PhaseFn } from './shared.ts';
import { n } from './shared.ts';

/**
 * Interior finish: doors, trim, flooring, cabinets, countertops, tile,
 * bath accessories. Finish-sensitive, and the largest material phase in
 * most houses. Flooring follows the flooring sheet's 8% straight-lay waste
 * (src/lib/calc/flooring.ts) at a blended plank-and-tile rate.
 */
export const interior: PhaseFn = (g) => {
  const rooms = g.rooms.value;
  const op = g.openings.value;
  const heated = g.heatedSf.value;
  const intDoors = Math.max(6, rooms.count - 2);
  // Base runs the finished wall perimeter: the paint sheet's 2.7 × floor of
  // wall area at the wall height, less a 3-ft door opening per door.
  const baseLf = Math.ceil((heated * 2.7) / 9 - intDoors * 3);
  const casingLf = Math.ceil(intDoors * 17 + op.windows * 14);
  const floorSf = Math.ceil(heated * 1.08);
  const bathsCeil = Math.ceil(rooms.baths);
  const fullBaths = Math.floor(rooms.baths);
  const counterSf = rooms.kitchens * 55 + bathsCeil * 12;
  const tileSf = fullBaths * 90;

  return {
    id: 'interior',
    name: 'Interior finish',
    note: 'Doors, trim, flooring, cabinets, countertops, tile, bath accessories',
    lines: [
      line('doors', 'Interior doors and hardware', intDoors, RATES.intDoor, 'Prehung, hinges and knobs included'),
      line('base', 'Baseboard', baseLf, RATES.baseLf, `${n(baseLf)} lf, primed MDF or pine`),
      line('casing', 'Door and window casing', casingLf, RATES.casingLf),
      line('shelving', 'Closet shelving', rooms.bedrooms, RATES.shelvingPerBedroom, 'Per bedroom, plus the linen and pantry'),
      line('flooring', 'Flooring', floorSf, RATES.flooringSf, `${n(heated)} sq ft at 8% waste: plank in living areas, tile in baths, carpet in bedrooms`),
      line('underlayment', 'Flooring underlayment', floorSf, RATES.underlaymentSf),
      line('cabinets', 'Kitchen cabinets', rooms.kitchens, RATES.kitchenCabinets, 'Stock or semi-custom, uppers and lowers, pantry'),
      line('vanities', 'Bath vanities', bathsCeil, RATES.vanity, 'With tops and sinks'),
      line('counters', 'Countertops', counterSf, RATES.counterSf, `${counterSf} sq ft of quartz or granite, kitchen and baths`),
      line('tile', 'Tile', tileSf, RATES.tileSf, `${tileSf} sq ft: shower walls and bath floors`),
      line('tile-set', 'Backer board, thinset, grout', tileSf, RATES.tileSetSf),
      line('glass', 'Shower glass', fullBaths, RATES.showerGlass, 'Framed or semi-frameless doors'),
      line('accessories', 'Mirrors, bars, hooks, paper holders', bathsCeil, RATES.bathAccessories, 'Per bath'),
    ],
  };
};
