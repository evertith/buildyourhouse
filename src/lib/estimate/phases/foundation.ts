import { RATES } from '../prices.ts';
import { allowance, line, ceilTo } from '../types.ts';
import type { Line } from '../types.ts';
import type { PhaseFn } from './shared.ts';
import { n } from './shared.ts';

/**
 * Foundation by type.
 * - Slab: 4-in monolithic slab over the house and garage with a 20 × 12 in
 *   turned-down footing on the perimeter, mesh in the slab, rebar in the
 *   footing, vapor barrier, 4 in of gravel.
 * - Crawl: 24 × 12 in continuous footing, 3-ft block stem wall, piers every
 *   200 sq ft, PT sill, vents, vapor barrier on the ground, garage on its
 *   own slab.
 * - Basement: 8-ft poured walls, 8 in thick, on 24 × 12 in footings, 4-in
 *   slab, waterproofed and drained, garage on its own slab.
 * Concrete carries a 10% order factor; short-loading a pour is the classic
 * expensive mistake.
 */
export const foundation: PhaseFn = (g) => {
  const footprint = g.footprintSf.value;
  const perimeter = g.perimeterLf.value;
  const garage = g.garageSf.value;
  const kind = g.foundation.value;
  const lines: Line[] = [];

  const garageSlabLines = (): Line[] => {
    if (!garage) return [];
    const cuFt = garage * (4 / 12) + 44 * (20 / 12);
    const yd = ceilTo((cuFt / 27) * 1.1, 0.5);
    return [
      line('garage-slab', 'Garage slab', yd, RATES.readyMixYd, `4 in over ${n(garage)} sq ft with a turned-down edge`),
    ];
  };

  if (kind === 'slab') {
    const slabArea = footprint + garage;
    const slabPerimeter = perimeter + (garage ? 44 : 0);
    const cuFt = slabArea * (4 / 12) + slabPerimeter * (20 / 12);
    const yd = ceilTo((cuFt / 27) * 1.1, 0.5);
    const rebar = Math.ceil(((2 * slabPerimeter) / 20) * 1.05);
    const mesh = Math.ceil((slabArea / 50) * 1.1);
    const vapor = Math.ceil(slabArea * 1.15);
    const gravelTons = Math.ceil(((slabArea * (4 / 12)) / 27) * 1.4);
    lines.push(
      line('concrete', 'Ready-mix concrete', yd, RATES.readyMixYd, `4-in slab over ${n(slabArea)} sq ft plus a 20 × 12 in turned-down footing, 10% order factor`),
      line('rebar', 'Rebar, #4 × 20 ft', rebar, RATES.rebarStick, 'Two runs in the footing, 5% lap'),
      line('mesh', 'Welded wire mesh', mesh, RATES.meshSheet, '5 × 10 sheets in the slab, one-square overlap'),
      line('vapor', 'Vapor barrier', vapor, RATES.vaporSf, '6-mil poly under the slab, 15% for laps'),
      line('gravel', 'Gravel base', gravelTons, RATES.gravelTon, '4 in of compacted stone under the slab'),
      allowance('sundries', 'Anchor bolts, forms, edge foam', RATES.slabSundries)
    );
  } else if (kind === 'crawl') {
    const piers = Math.ceil(footprint / 200);
    const cuFt = perimeter * 2 + piers * 4;
    const yd = ceilTo((cuFt / 27) * 1.1, 0.5);
    const blocks = Math.ceil(3 * perimeter * 1.125 * 1.05);
    const rebar = Math.ceil(((2.5 * perimeter) / 20) * 1.05);
    const vents = Math.ceil(footprint / 150);
    lines.push(
      line('concrete', 'Ready-mix concrete, footings', yd, RATES.readyMixYd, `24 × 12 in continuous footing on ${n(perimeter)} lf plus ${piers} pier pads, 10% order factor`),
      line('block', 'CMU block, stem wall', blocks, RATES.cmuBlock, '8-in block, 3 ft high, mortar and grout included'),
      line('piers', 'Interior piers', piers, RATES.pier, 'Block piers on pads, one per 200 sq ft'),
      line('rebar', 'Rebar, #4 × 20 ft', rebar, RATES.rebarStick, 'Footing runs and vertical dowels'),
      line('sill', 'Pressure-treated sill, 2 × 8', Math.ceil(perimeter * 1.05), RATES.ptSillLf, 'On the stem wall under the floor framing'),
      line('vapor', 'Vapor barrier', Math.ceil(footprint * 1.15), RATES.vaporSf, '6-mil poly on the crawl floor'),
      line('vents', 'Foundation vents', vents, RATES.foundationVent),
      allowance('sundries', 'Anchor bolts, forms, termite shield', RATES.slabSundries),
      ...garageSlabLines()
    );
  } else {
    const wallCuFt = perimeter * 8 * (8 / 12);
    const footingCuFt = perimeter * 2;
    const slabCuFt = footprint * (4 / 12);
    const yd = ceilTo(((wallCuFt + footingCuFt + slabCuFt) / 27) * 1.1, 0.5);
    const rebar = Math.ceil(((6 * perimeter) / 20) * 1.05);
    const mesh = Math.ceil((footprint / 50) * 1.1);
    const gravelTons = Math.ceil(((perimeter * 2 + footprint * (4 / 12)) / 27) * 1.4);
    lines.push(
      line('concrete', 'Ready-mix concrete', yd, RATES.readyMixYd, `8-ft walls 8 in thick on ${n(perimeter)} lf of 24 × 12 in footing, plus a 4-in slab, 10% order factor`),
      line('rebar', 'Rebar, #4 × 20 ft', rebar, RATES.rebarStick, 'Footing runs, wall mats, dowels'),
      line('mesh', 'Welded wire mesh', mesh, RATES.meshSheet, 'In the basement slab'),
      line('waterproof', 'Waterproofing', Math.ceil(perimeter * 8), RATES.waterproofSf, 'Membrane on the outside of the walls'),
      line('drain', 'Drain tile', Math.ceil(perimeter * 1.05), RATES.drainTileLf, 'Perforated pipe at the footing, to daylight or a sump'),
      line('vapor', 'Vapor barrier', Math.ceil(footprint * 1.15), RATES.vaporSf, '6-mil poly under the slab'),
      line('gravel', 'Gravel', gravelTons, RATES.gravelTon, 'Footing drain bed and slab base'),
      allowance('sundries', 'Anchor bolts, form rental, window wells', { low: 1600, high: 3000, unit: 'allowance' }),
      ...garageSlabLines()
    );
  }

  return {
    id: 'foundation',
    name: 'Foundation',
    note:
      kind === 'slab'
        ? 'Monolithic slab with turned-down footings, mesh, vapor barrier, gravel'
        : kind === 'crawl'
          ? 'Crawl space: footings, block stem wall, piers, sill, vents'
          : 'Full basement: footings, poured walls, slab, waterproofing, drain',
    lines,
  };
};
