import { RATES } from '../prices.ts';
import { allowance, line, sumLines } from '../types.ts';
import type { Line } from '../types.ts';
import type { PhaseFn } from './shared.ts';
import { n, pitchFactor } from './shared.ts';

/**
 * Framing: walls, floor system, roof, sheathing, house wrap.
 * Conventions match the framing lumber sheet (src/lib/calc/framing.ts):
 * one stud per linear foot of wall at 16 in on center (the shortcut that
 * absorbs corners, jacks, kings, and blocking), three runs of plate in
 * 16-ft sticks with 5% cut waste, one header per opening, 4 × 8 OSB with
 * 10% waste. Exterior walls are 2 × 6, partitions 2 × 4.
 */
const STUD_LENGTH_FACTOR: Record<number, number> = { 8: 1, 9: 1.12, 10: 1.25 };
const TRUSS_FACTOR = { gable: 1, hip: 1.1, cutup: 1.25 } as const;

export const framing: PhaseFn = (g) => {
  const h = g.wallHeightFt.value;
  const lenFactor = STUD_LENGTH_FACTOR[h] ?? 1;
  const extLf = g.extWallLf.value;
  const intLf = g.intWallLf.value;
  const op = g.openings.value;
  const rooms = g.rooms.value;
  const roof = g.roof.value;
  const framedFloor = g.framedFloorSf.value;
  const studLabel = h === 8 ? '92⅝ in precut' : h === 9 ? '104⅝ in precut' : '116⅝ in precut';

  const extStuds = Math.ceil(extLf);
  const intStuds = Math.ceil(intLf);
  const extPlates = Math.ceil((extLf * 3 * 1.05) / 16);
  const intPlates = Math.ceil((intLf * 3 * 1.05) / 16);
  const intDoors = Math.max(6, rooms.count - 2);
  const headers = op.windows + op.extDoors + intDoors;
  const wallSheets = Math.ceil((g.extWallAreaSf.value / 32) * 1.1);
  const wrapRolls = Math.ceil((g.extWallAreaSf.value / 1000) * 1.1);

  const lines: Line[] = [
    line('ext-studs', 'Exterior wall studs, 2 × 6', extStuds, scaled(RATES.stud2x6, lenFactor), `${studLabel}, 16 in on center, ${n(extLf)} lf of wall`),
    line('int-studs', 'Partition studs, 2 × 4', intStuds, scaled(RATES.stud2x4, lenFactor), `${studLabel}, 16 in on center, ${n(intLf)} lf of wall`),
    line('ext-plates', 'Plate stock, 2 × 6 × 16 ft', extPlates, RATES.plate2x6, 'Single bottom, doubled top, 5% cut waste'),
    line('int-plates', 'Plate stock, 2 × 4 × 16 ft', intPlates, RATES.plate2x4, 'Single bottom, doubled top, 5% cut waste'),
    line('headers', 'Header stock, 2 × 10 × 8 ft', headers, RATES.headerBoard, `One doubled header per opening: ${op.windows} windows, ${op.extDoors} exterior doors, ${intDoors} interior doors`),
  ];
  if (op.garageDoors) {
    lines.push(line('garage-header', 'Garage door header, LVL', op.garageDoors, RATES.garageHeader, '16-ft opening'));
  }
  lines.push(
    line('wall-sheathing', 'Wall sheathing, 7/16 in OSB', wallSheets, RATES.osbSheet, `${n(g.extWallAreaSf.value)} sq ft of exterior wall, 10% waste`),
    line('wrap', 'House wrap', wrapRolls, RATES.houseWrapRoll, '10 × 100 ft rolls, tape included')
  );

  if (framedFloor > 0) {
    const joistLf = framedFloor * 0.75 * 1.1;
    const joists = Math.ceil(joistLf / 16);
    const subfloor = Math.ceil((framedFloor / 32) * 1.1);
    lines.push(
      line('joists', 'Floor joists, 2 × 10 × 16 ft', joists, RATES.joist2x10, `${n(framedFloor)} sq ft of framed floor at 16 in on center, rim and blocking included`),
      line('subfloor', 'Subfloor, ¾ in T&G OSB', subfloor, RATES.subfloorSheet, '10% waste'),
      line('girders', 'Girders, beams, hangers', Math.round(framedFloor), RATES.girderPerSf, 'Built-up or LVL girders on 10-ft bays, joist hangers, posts')
    );
  }

  const trussSpan = g.sides.value.shortFt + 2;
  const trusses = Math.ceil((roof.planeAreaSf / (2 * trussSpan)) * TRUSS_FACTOR[roof.complexity]);
  const slopedSf = roof.planeAreaSf * pitchFactor(roof.pitch);
  const roofSheets = Math.ceil((slopedSf / 32) * 1.1);
  lines.push(
    line('trusses', 'Roof trusses', trusses, RATES.truss, `${roof.pitch}:12, about ${n(trussSpan)} ft span, 2 ft on center${roof.complexity !== 'gable' ? ', hip and jack sets' : ''}`),
    line('roof-sheathing', 'Roof sheathing, 7/16 in OSB', roofSheets, RATES.osbSheet, `${n(slopedSf)} sq ft of roof deck, 10% waste`)
  );

  if (g.porches.value.count > 0) {
    lines.push(
      line('porch-posts', 'Porch posts, 6 × 6 PT', g.porches.value.posts, RATES.porchPost),
      allowance('porch-beam', 'Porch beam and roof framing', RATES.porchBeam)
    );
  }
  if (g.stories.value > 1) {
    lines.push(allowance('stairs', 'Stair stringers and framing', { low: 400, high: 700, unit: 'allowance' }));
  }

  const lumber = sumLines(lines);
  lines.push(
    {
      id: 'blocking',
      label: 'Blocking, backing, treated plates, sub-fascia',
      qty: 1,
      unit: 'allowance',
      detail: '6% of the lumber above: fire blocking, drywall backing, PT bottom plates on the slab, gable and eave framing',
      costLow: lumber.low * 0.06,
      costHigh: lumber.high * 0.06,
    },
    {
      id: 'fasteners',
      label: 'Nails, hangers, strapping, bracing',
      qty: 1,
      unit: 'allowance',
      detail: '8% of the lumber above: framing nails, hurricane ties, let-in bracing, temporary bracing',
      costLow: lumber.low * 0.08,
      costHigh: lumber.high * 0.08,
    }
  );

  return {
    id: 'framing',
    name: 'Framing',
    note: 'Walls, floor and roof framing, sheathing, house wrap, headers',
    lines,
  };
};

function scaled(rate: { low: number; high: number; unit: string }, k: number) {
  return { low: rate.low * k, high: rate.high * k, unit: rate.unit };
}
