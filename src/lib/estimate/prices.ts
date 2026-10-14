/**
 * Unit rates for the whole-house estimate: national, material only, as of
 * PRICES_AS_OF. Every rate is a low–high band; regional swing and the
 * contractor-vs-retail spread are the reason for ranges. The state index
 * (stateIndex.ts) scales these; the finish multiplier moves only the
 * finish-sensitive phases.
 *
 * Refresh ritual, quarterly: edit this file, run the tests (the FAQ numbers
 * and the assumptions table are generated from the default run, so they
 * follow), and update PRICES_AS_OF.
 *
 * Where a trade sheet under src/lib/calc prices the same item, the rate
 * here matches it (framing studs and plates, OSB, ready-mix, shingles,
 * drywall consumables, paint, batts), so the two never disagree.
 */

import type { PhaseId, Rate } from './types.ts';

export const PRICES_AS_OF = 'October 2026';

export type Finish = 'basic' | 'standard' | 'premium';

export const FINISH_MULTIPLIER: Record<Finish, number> = {
  basic: 0.85,
  standard: 1,
  premium: 1.3,
};

/** Phases whose materials move with the finish level. */
export const FINISH_PHASES: ReadonlySet<PhaseId> = new Set<PhaseId>([
  'openings',
  'exterior',
  'drywallPaint',
  'interior',
]);

export const FINISH_LABEL: Record<Finish, string> = {
  basic: 'Basic',
  standard: 'Standard',
  premium: 'Premium',
};

const r = (low: number, high: number, unit: string): Rate => ({ low, high, unit });

export const RATES = {
  // Site work
  fillTopsoil: r(1200, 2500, 'allowance'),
  gravelTon: r(35, 55, 'tons'),
  siltFenceLf: r(1.5, 2.5, 'lf'),
  constructionEntrance: r(400, 700, 'allowance'),
  tempPower: r(900, 1500, 'each'),

  // Foundation
  readyMixYd: r(155, 195, 'yd³'),
  rebarStick: r(9, 16, 'sticks'),
  meshSheet: r(9, 14, 'sheets'),
  vaporSf: r(0.06, 0.12, 'sq ft'),
  slabSundries: r(800, 1500, 'allowance'),
  cmuBlock: r(3.1, 5.0, 'blocks'),
  pier: r(90, 140, 'piers'),
  ptSillLf: r(1.6, 2.4, 'lf'),
  foundationVent: r(20, 35, 'vents'),
  waterproofSf: r(1.0, 2.0, 'sq ft'),
  drainTileLf: r(2.0, 4.0, 'lf'),
  rigidFoamSf: r(1.2, 1.8, 'sq ft'),

  // Framing
  stud2x6: r(5.0, 7.4, 'studs'),
  stud2x4: r(3.2, 4.8, 'studs'),
  plate2x6: r(13, 20, 'boards'),
  plate2x4: r(8.5, 13, 'boards'),
  headerBoard: r(9, 14, 'boards'),
  garageHeader: r(150, 250, 'each'),
  osbSheet: r(16, 28, 'sheets'),
  houseWrapRoll: r(150, 220, 'rolls'),
  joist2x10: r(28, 40, 'boards'),
  subfloorSheet: r(38, 55, 'sheets'),
  girderPerSf: r(0.9, 1.6, 'sq ft'),
  truss: r(110, 170, 'trusses'),
  porchPost: r(60, 90, 'posts'),
  porchBeam: r(300, 500, 'allowance'),

  // Roofing
  shingleBundle: r(34, 48, 'bundles'),
  underlaymentRoll: r(85, 140, 'rolls'),
  iceWaterRoll: r(90, 130, 'rolls'),
  starterBundle: r(28, 42, 'bundles'),
  ridgeCapBundle: r(45, 65, 'bundles'),
  dripStick: r(9, 15, 'sticks'),
  ridgeVent: r(12, 20, 'sticks'),
  flashingBoots: r(150, 300, 'allowance'),
  nailLb: r(3.5, 5, 'lb'),

  // Windows and exterior doors (standard finish; the multiplier moves these)
  window: r(380, 560, 'windows'),
  entryDoor: r(1400, 2400, 'each'),
  patioDoor: r(1200, 1900, 'each'),
  extDoor: r(350, 600, 'doors'),
  garageDoor: r(1900, 3200, 'each'),

  // Exterior finish
  sidingSf: r(2.2, 3.6, 'sq ft'),
  trimLf: r(1.8, 3.0, 'lf'),
  soffitSf: r(2.5, 4.0, 'sq ft'),
  fasciaLf: r(2.0, 3.5, 'lf'),
  gutterLf: r(4, 7, 'lf'),
  exteriorSundries: r(400, 900, 'allowance'),

  // Plumbing
  roughPerFixture: r(220, 380, 'fixtures'),
  serviceLines: r(500, 900, 'allowance'),
  waterHeater: r(900, 1600, 'each'),
  toilet: r(180, 320, 'each'),
  tubShower: r(450, 900, 'each'),
  faucet: r(90, 180, 'each'),
  kitchenSink: r(220, 400, 'each'),
  hoseBib: r(40, 70, 'each'),
  laundryBox: r(60, 110, 'each'),
  plumbingSundries: r(200, 400, 'allowance'),

  // Electrical
  service200A: r(900, 1500, 'each'),
  wiringPerSf: r(1.6, 2.4, 'sq ft'),
  devicesPerRoom: r(55, 90, 'rooms'),
  smokeCo: r(35, 60, 'each'),
  fixturesPerRoom: r(90, 180, 'rooms'),
  exteriorLights: r(200, 450, 'allowance'),

  // HVAC
  heatPumpTon: r(1700, 2500, 'tons'),
  ductPerSf: r(1.0, 1.6, 'sq ft'),
  thermostat: r(120, 250, 'each'),
  bathFan: r(90, 160, 'each'),
  hvacSundries: r(350, 600, 'allowance'),

  // Insulation
  battBagR19: r(60, 85, 'bags'),
  blownBagR49: r(38, 52, 'bags'),
  airSealing: r(250, 500, 'allowance'),

  // Drywall and paint
  drywallSheet: r(12, 18, 'sheets'),
  mudBucket: r(17, 24, 'buckets'),
  tapeRoll: r(5, 9, 'rolls'),
  screwBox: r(7, 10, 'lb boxes'),
  cornerBead: r(4, 7, 'sticks'),
  wallPaintGal: r(38, 65, 'gallons'),
  primerGal: r(18, 28, 'gallons'),
  trimPaintGal: r(45, 70, 'gallons'),
  paintSundries: r(150, 350, 'allowance'),

  // Interior finish
  intDoor: r(205, 365, 'doors'),
  baseLf: r(1.2, 2.2, 'lf'),
  casingLf: r(1.4, 2.4, 'lf'),
  shelvingPerBedroom: r(120, 220, 'bedrooms'),
  flooringSf: r(3.5, 6.0, 'sq ft'),
  underlaymentSf: r(0.35, 0.6, 'sq ft'),
  kitchenCabinets: r(6000, 11000, 'kitchens'),
  vanity: r(450, 900, 'each'),
  counterSf: r(45, 85, 'sq ft'),
  tileSf: r(2.5, 5.5, 'sq ft'),
  tileSetSf: r(0.8, 1.4, 'sq ft'),
  showerGlass: r(600, 1100, 'each'),
  bathAccessories: r(150, 300, 'baths'),

  // Final and move-in
  appliances: r(4500, 7500, 'allowance'),
  flatworkSundriesSf: r(0.7, 1.2, 'sq ft'),
  seedStraw: r(800, 1500, 'allowance'),
  shrubs: r(600, 1500, 'allowance'),
  finalClean: r(300, 600, 'allowance'),
  dumpster: r(450, 650, 'each'),
  oddsAndEnds: r(300, 700, 'allowance'),

  // Before you break ground
  planReview: r(300, 700, 'allowance'),
  survey: r(800, 1500, 'allowance'),
  plansBasic: r(900, 2000, 'allowance'),
  plansStandard: r(1500, 3000, 'allowance'),
  plansPremium: r(7000, 14000, 'allowance'),
} as const satisfies Record<string, Rate>;

/** Building permit: a state base (stateIndex.ts) plus this per heated square foot. */
export const PERMIT_PER_SF = 0.35;

/** Builder's risk insurance, 12 months, as a share of hard cost. */
export const BUILDERS_RISK_SHARE = 0.005;

/** Contingency the rail shows on top of cash to build. */
export const CONTINGENCY_SHARE = 0.1;
