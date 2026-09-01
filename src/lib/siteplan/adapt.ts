/**
 * Site Plan Studio — the adapter between `rules.ts` and the drawing.
 *
 * `rules.ts` is a transcription of the shipped kit corpus and is frozen: its
 * citations are verbatim-verified and nothing here may edit, widen or
 * "helpfully" fill one of its nulls. This file only says which drawn
 * elements each of the seven named separations measures between, so the
 * geometry has something to point at.
 *
 * THE TWO RULES THIS FILE ENFORCES
 *
 * 1. A rule with `feet: null` can never produce a violation. It is a
 *    finding — usually the most useful thing the tool can tell a builder —
 *    and it surfaces as a note carrying the corpus's own words.
 * 2. `extraSeparations` never reaches the conflict engine (Amendment B).
 *    Those figures are conditions of narrow provisions — Texas's 100 ft is
 *    the condition of the 10-acre OSSF permitting exemption, Washington's
 *    100/200 ft bar owner self-installation — and drawing one as a setback
 *    every lot must meet is exactly the error class this site exists to fix.
 */

import {
  DEFAULT_SEPARATIONS,
  type CoreSeparations,
  type SeparationRule,
  type StateSiteplanRules,
} from './rules';
import { BUILDING_KINDS, SEPTIC_KINDS } from './defaults';
import type { ElementKind, Treatment } from './types';

export type SeparationKey = keyof CoreSeparations;

export const SEPARATION_KEYS: SeparationKey[] = [
  'wellToSeptic',
  'wellToDrainfield',
  'wellToPropertyLine',
  'septicToPropertyLine',
  'septicToBuilding',
  'septicToSurfaceWater',
  'wellToSurfaceWater',
];

/**
 * One separation, resolved onto the elements the user can draw.
 * `to: 'propertyLine'` measures against the lot edges rather than a pair.
 */
export interface AdaptedRule {
  key: SeparationKey;
  label: string;
  from: ElementKind[];
  to: ElementKind[] | 'propertyLine';
  feet: number | null;
  citation: string | null;
  note?: string;
}

const LABEL: Record<SeparationKey, string> = {
  wellToSeptic: 'Well → septic tank',
  wellToDrainfield: 'Well → drainfield',
  wellToPropertyLine: 'Well → property line',
  septicToPropertyLine: 'Septic → property line',
  septicToBuilding: 'Septic → building',
  septicToSurfaceWater: 'Septic → surface water',
  wellToSurfaceWater: 'Well → surface water',
};

/**
 * Does a property-line rule cover the drainfield as well as the tank?
 *
 * The corpus writes these against the wastewater system as a whole — ARM
 * 17.36.323 Table 2's 10 ft is a table row for the system, not for the tank
 * alone — so BOTH are measured and the worse of the two is reported. The
 * exception is a note that narrows the rule to sealed components or names
 * the tank on its own; Montana's own well-to-tank row does exactly that, so
 * the phrase has to be honoured rather than assumed away.
 */
function narrowsToTank(note?: string): boolean {
  if (!note) return false;
  const n = note.toLowerCase();
  return (
    n.includes('sealed component') ||
    n.includes('tank only') ||
    n.includes('septic tank only')
  );
}

function septicSideFor(rule: SeparationRule): ElementKind[] {
  return narrowsToTank(rule.note) ? ['septicTank'] : [...SEPTIC_KINDS];
}

/**
 * The seven separations as element pairs. Order is the order they print.
 *
 * `wellToSeptic` measures the tank alone and `wellToDrainfield` the field
 * alone, because the corpus states them as separate rows with separate
 * numbers — Montana's are 50 ft and 100 ft, and collapsing them would print
 * the wrong one against the wrong element.
 */
export function adaptSeparations(sep: CoreSeparations): AdaptedRule[] {
  return [
    {
      key: 'wellToSeptic',
      label: LABEL.wellToSeptic,
      from: ['well'],
      to: ['septicTank'],
      ...pick(sep.wellToSeptic),
    },
    {
      key: 'wellToDrainfield',
      label: LABEL.wellToDrainfield,
      from: ['well'],
      to: ['drainfield'],
      ...pick(sep.wellToDrainfield),
    },
    {
      key: 'wellToPropertyLine',
      label: LABEL.wellToPropertyLine,
      from: ['well'],
      to: 'propertyLine',
      ...pick(sep.wellToPropertyLine),
    },
    {
      key: 'septicToPropertyLine',
      label: LABEL.septicToPropertyLine,
      from: septicSideFor(sep.septicToPropertyLine),
      to: 'propertyLine',
      ...pick(sep.septicToPropertyLine),
    },
    {
      key: 'septicToBuilding',
      label: LABEL.septicToBuilding,
      from: septicSideFor(sep.septicToBuilding),
      to: [...BUILDING_KINDS],
      ...pick(sep.septicToBuilding),
    },
    {
      key: 'septicToSurfaceWater',
      label: LABEL.septicToSurfaceWater,
      from: septicSideFor(sep.septicToSurfaceWater),
      to: ['waterEdge'],
      ...pick(sep.septicToSurfaceWater),
    },
    {
      key: 'wellToSurfaceWater',
      label: LABEL.wellToSurfaceWater,
      from: ['well'],
      to: ['waterEdge'],
      ...pick(sep.wellToSurfaceWater),
    },
  ];
}

function pick(r: SeparationRule) {
  return { feet: r.feet, citation: r.citation, note: r.note };
}

/** True when the state publishes at least one binding distance. */
export function hasBindingRule(sep: CoreSeparations): boolean {
  return SEPARATION_KEYS.some((k) => sep[k].feet !== null);
}

/**
 * Which of the three display treatments applies (Amendment A).
 *
 * The case that forced the third treatment: most verified states have all
 * seven separations null, because the finding IS that no statewide minimum
 * exists. Michigan's dossier says so in as many words. Falling those back to
 * daggered typical values would replace a sourced, useful negative with a
 * number that is wrong for Michigan — so a verified state never borrows a
 * default, and only unverified states are hedged.
 */
export function treatmentFor(
  rules: StateSiteplanRules | null,
  stateCode: string
): Treatment {
  if (!stateCode || !rules) return 'none';
  if (!rules.verified) return 'hedged';
  return hasBindingRule(rules.separations) ? 'rules' : 'local';
}

/**
 * The separations to measure against, given the treatment. A hedged state
 * borrows DEFAULT_SEPARATIONS; every other treatment uses the state's own
 * data, nulls and all.
 */
export function separationsFor(
  rules: StateSiteplanRules | null,
  treatment: Treatment
): CoreSeparations | null {
  if (treatment === 'none') return null;
  if (treatment === 'hedged') return DEFAULT_SEPARATIONS();
  return rules ? rules.separations : null;
}

/**
 * The distinct sourced negatives behind a state's null separations.
 *
 * Most local-rule states repeat one finding across all seven keys (Michigan
 * has one, California one, Alaska four distinct ones), so they are deduped
 * by text and labelled with every separation they cover. That turns seven
 * identical paragraphs into one paragraph that says what it governs.
 */
export function groupedNegatives(
  sep: CoreSeparations
): { text: string; keys: SeparationKey[]; label: string }[] {
  const byText = new Map<string, SeparationKey[]>();
  for (const key of SEPARATION_KEYS) {
    const rule = sep[key];
    if (rule.feet !== null) continue;
    const text = rule.note ?? 'No distance is stated for this separation.';
    const list = byText.get(text);
    if (list) list.push(key);
    else byText.set(text, [key]);
  }
  return [...byText.entries()].map(([text, keys]) => ({
    text,
    keys,
    label:
      keys.length === SEPARATION_KEYS.length
        ? 'All seven separations'
        : keys.map((k) => LABEL[k]).join(' · '),
  }));
}

export const SEPARATION_LABEL = LABEL;
