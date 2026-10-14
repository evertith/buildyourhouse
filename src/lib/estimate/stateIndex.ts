/**
 * Per-state planning index for the whole-house estimate. North Carolina is
 * 1.00 because that is where the site's own builds were priced; every other
 * state is relative to it.
 *
 * `materials` scales every material line and `labor` every labor line.
 * They are seeded from published regional construction cost factors
 * (city cost indexes, Census construction cost by division) and rounded to
 * two places: a planning index, not a quote. Materials move a little by
 * region (freight, concrete haul distance); labor moves a lot.
 *
 * `climate` scales HVAC tonnage (cooling-dominated states need more
 * capacity per square foot; mild coastal climates less).
 *
 * `permitBase` and `tapFee` are the parts of the soft-cost phase that vary
 * most by state: the flat part of a residential building permit, and the
 * water and sewer tap or impact fees a municipality charges on a new house.
 * On a rural lot with no utilities, a well and septic replace the tap fee
 * and usually cost more; the page says so.
 */

import type { Range } from './types.ts';

export interface StateFactors {
  code: string;
  name: string;
  materials: number;
  labor: number;
  climate: number;
  permitBase: Range;
  tapFee: Range;
}

export const DEFAULT_STATE = 'NC';

const S = (
  code: string,
  name: string,
  materials: number,
  labor: number,
  climate: number,
  permitBase: [number, number],
  tapFee: [number, number]
): StateFactors => ({
  code,
  name,
  materials,
  labor,
  climate,
  permitBase: { low: permitBase[0], high: permitBase[1] },
  tapFee: { low: tapFee[0], high: tapFee[1] },
});

export const STATES: readonly StateFactors[] = [
  S('AL', 'Alabama', 0.97, 0.88, 1.15, [500, 1100], [2500, 6000]),
  S('AK', 'Alaska', 1.22, 1.3, 1.05, [700, 1500], [4000, 9000]),
  S('AZ', 'Arizona', 1.0, 0.98, 1.2, [700, 1500], [5000, 12000]),
  S('AR', 'Arkansas', 0.96, 0.85, 1.1, [450, 1000], [2500, 6000]),
  S('CA', 'California', 1.12, 1.45, 0.9, [1500, 3500], [15000, 40000]),
  S('CO', 'Colorado', 1.03, 1.08, 0.9, [900, 1900], [8000, 20000]),
  S('CT', 'Connecticut', 1.06, 1.3, 1.0, [900, 2000], [5000, 12000]),
  S('DE', 'Delaware', 1.03, 1.18, 1.0, [700, 1500], [4000, 9000]),
  S('FL', 'Florida', 1.01, 0.98, 1.2, [800, 1800], [6000, 15000]),
  S('GA', 'Georgia', 0.98, 0.93, 1.15, [600, 1300], [3500, 9000]),
  S('HI', 'Hawaii', 1.3, 1.4, 0.85, [1200, 2600], [8000, 20000]),
  S('ID', 'Idaho', 1.02, 0.98, 0.95, [700, 1500], [4000, 10000]),
  S('IL', 'Illinois', 1.03, 1.28, 1.0, [800, 1800], [4000, 10000]),
  S('IN', 'Indiana', 0.99, 1.0, 1.0, [500, 1200], [3000, 7000]),
  S('IA', 'Iowa', 0.99, 1.02, 1.0, [500, 1100], [3000, 7000]),
  S('KS', 'Kansas', 0.98, 0.95, 1.05, [500, 1100], [3000, 7000]),
  S('KY', 'Kentucky', 0.98, 0.95, 1.0, [500, 1100], [3000, 7000]),
  S('LA', 'Louisiana', 0.98, 0.9, 1.2, [550, 1200], [3000, 7000]),
  S('ME', 'Maine', 1.03, 1.05, 1.05, [600, 1300], [3000, 7000]),
  S('MD', 'Maryland', 1.04, 1.15, 1.0, [900, 2000], [8000, 18000]),
  S('MA', 'Massachusetts', 1.08, 1.38, 1.0, [1000, 2200], [5000, 12000]),
  S('MI', 'Michigan', 1.0, 1.08, 1.0, [600, 1300], [3500, 8000]),
  S('MN', 'Minnesota', 1.02, 1.18, 1.05, [700, 1500], [4000, 10000]),
  S('MS', 'Mississippi', 0.96, 0.84, 1.15, [450, 1000], [2500, 6000]),
  S('MO', 'Missouri', 0.99, 1.02, 1.05, [500, 1100], [3000, 7000]),
  S('MT', 'Montana', 1.03, 1.0, 1.0, [600, 1300], [3500, 8000]),
  S('NE', 'Nebraska', 0.99, 0.98, 1.05, [500, 1100], [3000, 7000]),
  S('NV', 'Nevada', 1.03, 1.12, 1.15, [800, 1800], [6000, 15000]),
  S('NH', 'New Hampshire', 1.04, 1.1, 1.05, [700, 1500], [3500, 8000]),
  S('NJ', 'New Jersey', 1.07, 1.38, 1.0, [1000, 2400], [6000, 15000]),
  S('NM', 'New Mexico', 0.99, 0.92, 1.0, [600, 1300], [4000, 9000]),
  S('NY', 'New York', 1.08, 1.4, 1.0, [900, 2200], [5000, 14000]),
  S('NC', 'North Carolina', 1.0, 1.0, 1.0, [600, 1400], [3000, 7000]),
  S('ND', 'North Dakota', 1.02, 1.0, 1.05, [500, 1100], [3000, 7000]),
  S('OH', 'Ohio', 1.0, 1.02, 1.0, [600, 1300], [3500, 8000]),
  S('OK', 'Oklahoma', 0.97, 0.88, 1.1, [500, 1100], [2500, 6000]),
  S('OR', 'Oregon', 1.05, 1.18, 0.9, [1000, 2200], [10000, 25000]),
  S('PA', 'Pennsylvania', 1.03, 1.15, 1.0, [700, 1500], [4000, 10000]),
  S('RI', 'Rhode Island', 1.06, 1.25, 1.0, [800, 1800], [4000, 10000]),
  S('SC', 'South Carolina', 0.98, 0.92, 1.15, [600, 1300], [3500, 9000]),
  S('SD', 'South Dakota', 1.0, 0.95, 1.05, [500, 1100], [3000, 7000]),
  S('TN', 'Tennessee', 0.98, 0.92, 1.05, [550, 1200], [3000, 8000]),
  S('TX', 'Texas', 0.99, 0.92, 1.2, [700, 1500], [4000, 10000]),
  S('UT', 'Utah', 1.02, 1.02, 0.95, [800, 1700], [6000, 14000]),
  S('VT', 'Vermont', 1.04, 1.05, 1.05, [600, 1300], [3000, 7000]),
  S('VA', 'Virginia', 1.01, 1.03, 1.0, [700, 1500], [5000, 14000]),
  S('WA', 'Washington', 1.07, 1.25, 0.9, [1000, 2200], [10000, 25000]),
  S('WV', 'West Virginia', 0.99, 0.98, 1.0, [500, 1100], [3000, 7000]),
  S('WI', 'Wisconsin', 1.01, 1.08, 1.05, [600, 1300], [3500, 8000]),
  S('WY', 'Wyoming', 1.03, 0.98, 1.0, [600, 1300], [3500, 8000]),
];

const BY_CODE: Record<string, StateFactors> = Object.fromEntries(STATES.map((s) => [s.code, s]));

export function isStateCode(code: string): boolean {
  return Object.prototype.hasOwnProperty.call(BY_CODE, code.toUpperCase());
}

/** Factors for a state code; unknown codes fall back to the default state. */
export function stateFactors(code: string): StateFactors {
  return BY_CODE[code.toUpperCase()] ?? BY_CODE[DEFAULT_STATE];
}

/** Codes in name order, for a select. */
export const STATE_CODES: readonly string[] = [...STATES]
  .sort((a, b) => a.name.localeCompare(b.name))
  .map((s) => s.code);
