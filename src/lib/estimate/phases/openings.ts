import { RATES } from '../prices.ts';
import { line } from '../types.ts';
import type { Line } from '../types.ts';
import type { PhaseFn } from './shared.ts';

/**
 * Windows and exterior doors. Finish-sensitive: the standard rates are
 * vinyl double-hung windows, a fiberglass entry door with sidelights, a
 * sliding patio door, a steel back door, and an insulated steel garage
 * door with an opener; the finish multiplier moves all of them.
 */
export const openings: PhaseFn = (g) => {
  const op = g.openings.value;
  const otherDoors = Math.max(0, op.extDoors - 2);
  const lines: Line[] = [
    line('windows', 'Windows', op.windows, RATES.window, `Vinyl double-hung, about ${Math.round(op.windowAreaSf / op.windows)} sq ft each`),
    line('entry', 'Entry door with sidelights', 1, RATES.entryDoor, 'Prehung fiberglass, lockset included'),
    line('patio', 'Patio door', 1, RATES.patioDoor, '6-ft sliding or French'),
  ];
  if (otherDoors > 0) {
    lines.push(line('ext-doors', 'Other exterior doors', otherDoors, RATES.extDoor, 'Prehung steel, back and garage entry'));
  }
  if (op.garageDoors > 0) {
    lines.push(line('garage-door', 'Garage door and opener', op.garageDoors, RATES.garageDoor, '16 × 7 ft insulated steel'));
  }
  return {
    id: 'openings',
    name: 'Windows and exterior doors',
    note: `${op.windows} windows, ${op.extDoors} exterior doors${op.garageDoors ? ', garage door' : ''}`,
    lines,
  };
};
