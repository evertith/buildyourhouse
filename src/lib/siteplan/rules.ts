/**
 * Site Plan Studio — per-state siting rules.
 *
 * Extracted from the shipped permit-kit corpus (binder-pipeline/kits/research
 * dossiers, the kit generators, and the state guides). This module is a
 * transcription of that research, not new research: every number carrying
 * `verified: true` also carries the citation the kit prints for it.
 *
 * THE RULE THIS FILE EXISTS TO ENFORCE: a null `feet` means the corpus does not
 * support a number, and the tool must say so rather than draw a circle. Nulls
 * here are deliberate and are not defects to be "filled in" — filling one in
 * without a citation from a shipped kit breaks the accuracy standard the whole
 * product line rests on. Reach for DEFAULTS only as an explicitly-labelled
 * fallback; it is common practice, not law, and it is wrong somewhere.
 *
 * Only the 12 shipped kit states carry verified data. The other 38 fall back to
 * DEFAULTS and must be presented to the user as unverified.
 */

import { STATE_KITS } from '@/lib/kits';

/** One separation distance, as the corpus states it. */
export interface SeparationRule {
  /** Distance in feet. Null when the corpus states no number for this state. */
  feet: number | null;
  /** The citation exactly as the kit prints it. Null whenever feet is null. */
  citation: string | null;
  /** The hedge, the negative finding, or the local-variation caveat. */
  note?: string;
}

/**
 * The seven separations the studio draws. Every state defines all seven; ones
 * the corpus does not support are present with feet: null and a note.
 */
export interface CoreSeparations {
  wellToSeptic: SeparationRule;
  wellToDrainfield: SeparationRule;
  wellToPropertyLine: SeparationRule;
  septicToPropertyLine: SeparationRule;
  septicToBuilding: SeparationRule;
  septicToSurfaceWater: SeparationRule;
  wellToSurfaceWater: SeparationRule;
}

/** A separation outside the core seven (vertical, slope, tank-to-field, …). */
export interface LabelledSeparation extends SeparationRule {
  label: string;
}

export interface StateSiteplanRules {
  /** Lowercase postal code, matching StateKit.code. */
  code: string;
  state: string;
  /** State-guide route segment: /permitting/state-guides/<guideSlug>. */
  guideSlug: string;
  /** True only where the shipped-kit corpus backs the data below. */
  verified: boolean;
  /** When the kit last verified the research, e.g. 'August 2026'. */
  verifiedDate?: string;
  separations: CoreSeparations;
  /** Extra separations the corpus states — vertical, slope, tank-to-field. */
  extraSeparations?: LabelledSeparation[];
  /** The building-setback position: local zoning unless a state rule exists. */
  setbacksNote: string;
  /** Who accepts an owner-drawn plan vs requires a survey, with citation. */
  ownerDrawnAccepted?: string;
  /** Plot-plan contents, where a kit checklist enumerates them. */
  mustShow?: string[];
  /**
   * Verified absences — where the corpus was read and found NO rule. These are
   * findings, not gaps: they tell a builder the state floor is thinner than
   * they assume, and they are the reason a local check still matters.
   */
  negativeFindings?: string[];
}

/** Attached to every DEFAULTS number. Common practice is not law. */
export const COMMON_PRACTICE_NOTE =
  'Common practice, not a verified rule for this state — your local health ' +
  'department sets the real number. Confirm before siting anything.';

/** The honest position on building setbacks nearly everywhere. */
export const LOCAL_ZONING_SETBACKS =
  'Building setbacks are set by local zoning (county or municipal), not by ' +
  'the state. Get them in writing from the planning counter before you site ' +
  'the house.';

/** Builds a "corpus states no number" rule. */
const unknown = (note: string): SeparationRule => ({
  feet: null,
  citation: null,
  note,
});

const NO_STATE_RULE = 'No state-level distance found in the shipped research; ' +
  'this is set locally.';

/**
 * Why a state has no number, in that state's own terms. Each of these is a
 * finding from the kit research, not a placeholder — the reason the number is
 * missing is usually the most useful thing the tool can tell a builder.
 */
const LOCAL_OWTS =
  'No statewide separation table. Septic runs through the State Water Board\'s ' +
  'OWTS Policy (adopted 18 April 2023), implemented locally — most counties ' +
  'through a Local Agency Management Program approved by the Regional Water ' +
  'Quality Control Board. Your LAMP sets the distance.';

const CO_LOCAL =
  'Set by your local board of health, which Colorado requires to adopt its own ' +
  'detailed onsite-wastewater rules (C.R.S. 25-10-104(2)). The state sets a ' +
  'floor the county cannot go below, not a number you can design to.';

const GA_DPH =
  'Well and septic setbacks come from DPH Rule 511-3-1 and the DPH manual, ' +
  'administered county by county. The kit names the authority but prints no ' +
  'distance, so none is carried here.';

const KY_REG =
  'Setbacks live in 902 KAR 10:085, but the kit prints no distance from it — ' +
  'the site evaluation by the local health department produces the number for ' +
  'your specific site.';

const MI_NONE =
  'There is no statewide figure to carry. Michigan has no statewide septic ' +
  'code, and the research pass instruction is explicit: print none. Your ' +
  'district health department is the only source.';

const MS_LOCAL =
  'The kit routes onsite wastewater to the Department\'s Division of On-site ' +
  'Wastewater and prints no separation distance.';

const TX_LOCAL =
  'Set by the local authorized agent (usually the county) under 30 TAC Ch. ' +
  '285, following the site evaluation. No statewide distance is printed.';

const VA_LOCAL =
  'Set through the VDH construction permit process (12VAC5-610) at the local ' +
  'health department. The kit prints no statewide separation distance.';

/**
 * Commonly-cited practice, for the 38 states with no kit yet.
 *
 * Every number here is drawn from the corpus's own values rather than outside
 * research, and each carries where it came from. Two fields are deliberately
 * null: the corpus establishes no common figure for them, and inventing one to
 * fill the shape of the table is exactly the failure this module exists to
 * prevent. A null default renders as "ask your health department", which is the
 * true answer.
 *
 * verified is false and every populated entry carries COMMON_PRACTICE_NOTE.
 * These are a starting point for a conversation with a health department, never
 * the answer.
 */
export const DEFAULT_SEPARATIONS = (): CoreSeparations => ({
  wellToSeptic: {
    feet: 100,
    citation: null,
    note:
      COMMON_PRACTICE_NOTE +
      ' The most corroborated number in the corpus: Alaska fixes it by statute ' +
      '(18 AAC 72.100(a)(1)) and Montana reaches the same 100 ft to a ' +
      'drainfield (ARM 17.36.323, Table 2).',
  },
  wellToDrainfield: {
    feet: 100,
    citation: null,
    note:
      COMMON_PRACTICE_NOTE +
      ' Same basis as well-to-tank: 18 AAC 72.100(a)(1) and ARM 17.36.323, ' +
      'Table 2 both put the drainfield at 100 ft.',
  },
  wellToPropertyLine: {
    feet: null,
    citation: null,
    note:
      'No common figure is established anywhere in the shipped research. The ' +
      'only in-corpus number is an uncited 10 ft in the North Carolina state ' +
      'guide, which is too thin to generalise from. Ask your health ' +
      'department.',
  },
  septicToPropertyLine: {
    feet: 10,
    citation: null,
    note:
      COMMON_PRACTICE_NOTE +
      ' Alaska DEC\'s installation manual footnotes 10 ft as a "Recommended ' +
      'minimum horizontal separation distance" — guidance, not law — and ' +
      'Montana makes 10 ft binding (ARM 17.36.323, Table 2).',
  },
  septicToBuilding: {
    feet: 10,
    citation: null,
    note:
      COMMON_PRACTICE_NOTE +
      ' From the same Alaska DEC manual footnote, where it is explicitly a ' +
      'recommendation. Alaska imposes no state foundation setback at all.',
  },
  septicToSurfaceWater: {
    feet: 100,
    citation: null,
    note:
      COMMON_PRACTICE_NOTE +
      ' Alaska (18 AAC 72.520(b)) and Montana (ARM 17.36.323, Table 2) both ' +
      'set 100 ft. Washington\'s similar-looking 100 ft is NOT a setback — it ' +
      'is a threshold that bars owner self-installation — so it does not ' +
      'corroborate this number.',
  },
  wellToSurfaceWater: {
    feet: null,
    citation: null,
    note:
      'The corpus states no well-to-surface-water rule for any shipped state — ' +
      'the 100 ft surface-water setbacks it does carry are measured from the ' +
      'wastewater system, not the well. No number is offered here rather than ' +
      'a guessed one.',
  },
});

export const DEFAULTS: StateSiteplanRules = {
  code: 'default',
  state: 'Default (no kit yet)',
  guideSlug: '',
  verified: false,
  separations: DEFAULT_SEPARATIONS(),
  setbacksNote: LOCAL_ZONING_SETBACKS,
};

/**
 * The 12 shipped kit states. Anything absent here is absent from the corpus.
 */
const VERIFIED_STATES: StateSiteplanRules[] = [
  {
    code: 'ak',
    state: 'Alaska',
    guideSlug: 'alaska',
    verified: true,
    verifiedDate: 'August 2026',
    separations: {
      wellToSeptic: {
        feet: 100,
        citation: '18 AAC 72.100(a)(1)',
        note:
          'Private well to septic tank, absorption field, sewer line, holding ' +
          'tank, pit privy or "other potential source of contamination," ' +
          'measured nearest edge to nearest edge. A well serving a public ' +
          'system needs 200 ft (18 AAC 80.020 Table A).',
      },
      wellToDrainfield: {
        feet: 100,
        citation: '18 AAC 72.100(a)(1)',
        note: 'Same rule as the tank — the absorption field is named in it.',
      },
      wellToPropertyLine: unknown(NO_STATE_RULE),
      septicToPropertyLine: {
        feet: null,
        citation: null,
        note:
          'No state setback exists. 18 AAC 72.520 was read in full and ' +
          'contains none; DEC\'s installation manual lists 10 ft and footnotes ' +
          'it "Recommended minimum horizontal separation distance" — guidance, ' +
          'not law. Inside the Municipality of Anchorage 10 ft IS mandatory ' +
          '(AMC 15.65.210B.1).',
      },
      septicToBuilding: {
        feet: null,
        citation: null,
        note:
          'No state foundation setback exists — same finding as the property ' +
          'line. DEC recommends 10 ft; Anchorage makes 10 ft mandatory ' +
          '(AMC 15.65.210B.1).',
      },
      septicToSurfaceWater: {
        feet: 100,
        citation: '18 AAC 72.520(b); 72.990(91)',
        note:
          'To the high water level of a lake, river, stream, spring or slough ' +
          '— and "slough" is defined to include a swamp, bog or marsh, which ' +
          'on an Alaska parcel is often most of it.',
      },
      wellToSurfaceWater: unknown(
        'Not stated separately; the 100 ft surface-water rule in 18 AAC ' +
          '72.520(b) is written against the wastewater system, not the well.'
      ),
    },
    extraSeparations: [
      {
        label: 'Vertical to annual high water table',
        feet: 4,
        citation: '18 AAC 72.520(d)(1)',
        note: 'From the bottom of the distribution media down.',
      },
      {
        label: 'Vertical to an impermeable horizon',
        feet: 6,
        citation: '18 AAC 72.520(d)(2)',
        note:
          'Bedrock, clay, permafrost, or soils percolating slower than 120 ' +
          'minutes per inch.',
      },
      {
        label: 'Absorption field to a steep slope',
        feet: 50,
        citation: '18 AAC 72.520(c)',
        note:
          'To a slope steeper than 25 percent with a vertical drop over 10 ft, ' +
          'natural or man-made.',
      },
      {
        label: 'Septic tank to absorption field',
        feet: 5,
        citation: '18 AAC 72.520(f)',
      },
      {
        label: 'Well to private sewer line, building sump or fuel tank',
        feet: 25,
        citation: '18 AAC 72.100(a)(2), (4)',
      },
    ],
    setbacksNote:
      'Building setbacks are local. Most of Alaska has no building department ' +
      'at all, and the boroughs that do set their own — Kenai Peninsula ' +
      'Borough sets building setbacks at KPB 20.30 while issuing no building ' +
      'permit. Confirm with the borough or city that actually has jurisdiction.',
    ownerDrawnAccepted:
      'Split, and the split is sharp. The Municipality of Anchorage requires a ' +
      'surveyed plot plan plus stamped structural calculations for a new home ' +
      '(AMC 23.05.010). The City of Wasilla expressly lets an owner draw their ' +
      'own site plan for a single-family dwelling or duplex ' +
      '(WMC 16.90.020.B). Elsewhere the kit\'s standing advice is that a ' +
      'surveyed plot plan is needed where the jurisdiction requires one, ' +
      'because a sketch is commonly rejected.',
    mustShow: [
      'The building envelope',
      'The wastewater system and its reserve area',
      'The well',
      'The driveway',
      'Every structure on the parcel (where a building department reviews it)',
    ],
    negativeFindings: [
      'No state property-line setback for a septic system — 18 AAC 72.520 was ' +
        'read in full and contains none.',
      'No state foundation setback for a septic system, same source.',
      'No state permit is required to drill a private domestic well; 18 AAC 80 ' +
        'applies to public systems only (80.005(b)).',
      'The widely-quoted 18 AAC 72.020 setback section is REPEALED (rewrite ' +
        'effective 1 October 2023). Anything citing it is stale.',
    ],
  },
  {
    code: 'mt',
    state: 'Montana',
    guideSlug: 'montana',
    verified: true,
    verifiedDate: 'August 2026',
    separations: {
      wellToSeptic: {
        feet: 50,
        citation: 'ARM 17.36.323, Table 2',
        note:
          'The corpus states this as well to "sealed components," which is how ' +
          'the table describes the tank and sealed lines.',
      },
      wellToDrainfield: {
        feet: 100,
        citation: 'ARM 17.36.323, Table 2',
        note:
          'Drinking water well to a drainfield or soil absorption system, and ' +
          'the same 100 ft from a mixing zone to a drinking water well. A ' +
          'smaller well isolation zone is possible only if the department ' +
          'approves one.',
      },
      wellToPropertyLine: unknown(
        'Not stated as a setback. Related but different: the 100 ft well ' +
          'isolation zone (76-4-102(27)) must itself lie inside the ' +
          'subdivision boundary or be secured by easement for parcels created ' +
          'after 1 October 2021 (76-4-104(7)(i)) — on a small lot this, not ' +
          'the house, is the binding constraint.'
      ),
      septicToPropertyLine: {
        feet: 10,
        citation: 'ARM 17.36.323, Table 2',
        note: 'An easement may satisfy it.',
      },
      septicToBuilding: unknown(NO_STATE_RULE),
      septicToSurfaceWater: {
        feet: 100,
        citation: 'ARM 17.36.323, Table 2',
        note: 'Surface water and springs to a drainfield.',
      },
      wellToSurfaceWater: unknown(NO_STATE_RULE),
    },
    extraSeparations: [
      {
        label: 'Natural soil above a limiting layer',
        feet: 4,
        citation: 'ARM 17.36.320(4)',
        note:
          'Six feet on slopes over 15 percent. This is the number that quietly ' +
          'decides whether a lot works.',
      },
      {
        label: 'Sewage lagoon to a well',
        feet: 1000,
        citation: 'ARM 17.36.323, Table 2',
      },
      {
        label: 'Well isolation zone radius',
        feet: 100,
        citation: '76-4-102(27), MCA',
      },
    ],
    setbacksNote:
      'Building setbacks are local zoning. What IS statewide is that county ' +
      'septic rules must be "no less stringent" than the state minimums ' +
      '(ARM 17.36.911(2); MCA 50-2-116(1)(j)) — so the separations above are a ' +
      'floor your county can raise but never lower.',
    negativeFindings: [
      'No state septic-installer licensing rule and no state pre-backfill ' +
        'inspection rule were found — both remain local.',
      'A COSA is not the septic permit: a drainfield permit is still required ' +
        'by the local health department.',
    ],
  },
  {
    code: 'nc',
    state: 'North Carolina',
    guideSlug: 'north-carolina',
    verified: true,
    verifiedDate: 'August 2026',
    separations: {
      // The NC kit deliberately prints no separation numbers: it routes every
      // distance to the county health department under 15A NCAC 18E. The older
      // state guide does print a table, but without citations, so none of it
      // can be marked verified here. See the report note on this conflict.
      wellToSeptic: unknown(
        'The NC kit routes this to county health (15A NCAC 18E) rather than ' +
          'printing a number. The state guide\'s table says 100 ft but cites ' +
          'nothing, so it is not carried here as verified.'
      ),
      wellToDrainfield: unknown(
        'Not separately stated; permitted by the county health department ' +
          'under 15A NCAC 18E.'
      ),
      wellToPropertyLine: unknown(
        'The state guide\'s table says 10 ft but cites nothing. Not carried as ' +
          'verified.'
      ),
      septicToPropertyLine: unknown(
        'The state guide says "Varies by system size (10-50 feet)" without a ' +
          'citation — a hedge, not a number. County health sets it.'
      ),
      septicToBuilding: unknown(NO_STATE_RULE),
      septicToSurfaceWater: unknown(NO_STATE_RULE),
      wellToSurfaceWater: unknown(NO_STATE_RULE),
    },
    setbacksNote:
      'Building setbacks are local zoning — the kit\'s instruction is to get ' +
      'required setbacks confirmed in writing. On-site wastewater and private ' +
      'wells run through the county health department on a separate track and ' +
      'a different timeline from the building permit.',
    mustShow: [
      'Property lines',
      'Setbacks',
      'The building footprint',
      'The driveway',
      'Well and septic locations',
      'Any easements',
      'System type and drainfield location',
    ],
    negativeFindings: [
      'The septic permit sequence gates the building permit: Improvement ' +
        'Permit, then Construction Authorization, then Operation Permit ' +
        '(15A NCAC 18E, § .0204(f)).',
      'A well construction permit is required BEFORE drilling, and the ' +
        'Certificate of Completion before the well may be placed in service ' +
        '(15A NCAC 02C .0300).',
    ],
  },
  {
    code: 'wa',
    state: 'Washington',
    guideSlug: 'washington',
    verified: true,
    verifiedDate: 'August 2026',
    separations: {
      // Washington's onsite rules run through the local health jurisdiction
      // (WAC 246-272A-0013 lets it add its own). The state rule carries no
      // separation table, so all seven are null by finding, not by omission.
      wellToSeptic: unknown(NO_STATE_RULE),
      wellToDrainfield: unknown(NO_STATE_RULE),
      wellToPropertyLine: unknown(NO_STATE_RULE),
      septicToPropertyLine: unknown(NO_STATE_RULE),
      septicToBuilding: unknown(NO_STATE_RULE),
      septicToSurfaceWater: unknown(
        'No state setback. Do not mistake the 100 ft surface-water figure in ' +
          'WAC 246-272A-0250(2) for one — it bars the owner from installing ' +
          'the system themselves, it does not bar the system from being there.'
      ),
      wellToSurfaceWater: unknown(NO_STATE_RULE),
    },
    extraSeparations: [
      {
        label: 'Owner self-installation barred — within this of marine water',
        feet: 200,
        citation: 'WAC 246-272A-0250(1)–(2)',
        note:
          'Subsection (2)(a). Not a siting setback. The health officer "may ' +
          'allow" a resident ' +
          'owner to install their own system, except where the primary and ' +
          'reserve areas fall within this distance. It rules out a great many ' +
          'Puget Sound lots.',
      },
      {
        label: 'Owner self-installation barred — within this of surface water',
        feet: 100,
        citation: 'WAC 246-272A-0250(1)–(2)',
        note:
          'Subsection (2)(b). Not a siting setback — the same ' +
          'self-installation exclusion.',
      },
    ],
    setbacksNote:
      'Building setbacks are local zoning, and in Washington they come with a ' +
      'second question that catches people: ask the planning counter whether ' +
      'any critical area or its buffer touches the parcel, because those ' +
      'buffers move the buildable envelope more than the setbacks do.',
    ownerDrawnAccepted:
      'For the septic side, no — the design must bear "the name, signature and ' +
      'stamp of the designer" and the application must carry a dimensioned ' +
      'site plan showing both the initial and the reserve area ' +
      '(WAC 246-272A-0200). The building-permit site plan is the local ' +
      'jurisdiction\'s call.',
    mustShow: [
      'Property lines',
      'Setbacks',
      'The building footprint',
      'The driveway',
      'Well and septic areas, including the reserve area',
      'Critical areas and their buffers',
      'Easements',
    ],
    negativeFindings: [
      'The state onsite rule carries no separation-distance table; local ' +
        'health jurisdictions may add their own rules under ' +
        'WAC 246-272A-0013, and forms and fees are theirs.',
      'Owner installation is discretionary, not a right — the rule reads "may ' +
        'allow" (WAC 246-272A-0250(2)).',
      'You may cover the installation only after the local health officer has ' +
        'approved it (WAC 246-272A-0250(3)(g)).',
    ],
  },
  {
    code: 'ca',
    state: 'California',
    guideSlug: 'california',
    verified: true,
    verifiedDate: 'August 2026',
    separations: {
      // Septic runs through the State Water Board's OWTS Policy, implemented
      // locally through a LAMP. No statewide separation table reached print.
      wellToSeptic: unknown(LOCAL_OWTS),
      wellToDrainfield: unknown(LOCAL_OWTS),
      wellToPropertyLine: unknown(LOCAL_OWTS),
      septicToPropertyLine: unknown(LOCAL_OWTS),
      septicToBuilding: unknown(LOCAL_OWTS),
      septicToSurfaceWater: unknown(LOCAL_OWTS),
      wellToSurfaceWater: unknown(LOCAL_OWTS),
    },
    extraSeparations: [
      {
        label: 'Defensible space around the structure',
        feet: 100,
        citation: 'PRC § 4291; Gov. Code § 51182',
        note:
          '"Maintain defensible space of 100 feet from each side and from the ' +
          'front and rear of the structure, but not beyond the property line." ' +
          'PRC § 4291 applies in the State Responsibility Area; Gov. Code ' +
          '§ 51182 in a locally designated Very High Fire Hazard Severity ' +
          'Zone. Both amended by Stats. 2025, Ch. 731 (AB 1455), effective ' +
          '13 October 2025. This one genuinely shapes where the house can go.',
      },
      {
        label: 'More intense fuel reduction zone',
        feet: 30,
        citation: 'PRC § 4291; Gov. Code § 51182',
        note: 'Applies between 5 and 30 feet around the structure.',
      },
      {
        label: 'Ember-resistant zone ("Zone 0")',
        feet: 5,
        citation: 'PRC § 4291(g)(1)',
        note:
          'NOT yet in force for new structures. The statute says the ' +
          'requirement "shall not take effect for new structures until the ' +
          'board updates the regulations." Whether the Board of Forestry has ' +
          'done so was the open question at the kit\'s August 2026 pass — ' +
          'treat as pending and confirm, do not design to it as settled law.',
      },
    ],
    setbacksNote:
      'Building setbacks are local zoning. The distance that actually moves a ' +
      'California house is the defensible-space envelope above, not the ' +
      'zoning setback — and note it stops at the property line, so a small ' +
      'lot cannot satisfy it by pushing the house across the boundary.',
    negativeFindings: [
      'You may NOT drill your own well. Water Code § 13750.5 requires a C-57 ' +
        'Water Well Contractor\'s License with no owner exception — a sharp ' +
        'contrast with § 7044, which lets you wire and plumb your own house.',
      'Before constructing in the zone, the owner must obtain a certification ' +
        'from the local building official that the structure as proposed ' +
        'complies with applicable standards, and give it to the ' +
        'course-of-construction insurer on request (PRC § 4291(a)(5); ' +
        'Gov. Code § 51182(a)(5)).',
    ],
  },
  {
    code: 'co',
    state: 'Colorado',
    guideSlug: 'colorado',
    verified: true,
    verifiedDate: 'August 2026',
    separations: {
      wellToSeptic: unknown(CO_LOCAL),
      wellToDrainfield: unknown(CO_LOCAL),
      wellToPropertyLine: unknown(CO_LOCAL),
      septicToPropertyLine: unknown(CO_LOCAL),
      septicToBuilding: unknown(CO_LOCAL),
      septicToSurfaceWater: unknown(CO_LOCAL),
      wellToSurfaceWater: unknown(CO_LOCAL),
    },
    setbacksNote:
      'Building setbacks are local zoning, and the kit adds a Colorado-specific ' +
      'question: confirm any wildland-urban interface overlay at the same time, ' +
      'because it changes what you build as well as where.',
    ownerDrawnAccepted:
      'You may draw your own plans. C.R.S. 12-120-403(1)(a) puts "One-, two-, ' +
      'three-, and four-family dwellings, including accessory buildings ' +
      'commonly associated with those dwellings" outside the architects\' ' +
      'practice act. Whether the building department accepts an unsurveyed ' +
      'site plan is still a local question.',
    mustShow: [
      'Property lines',
      'Setbacks',
      'The building footprint',
      'The driveway',
      'Easements',
      'Well and septic locations with their separation distances',
    ],
    negativeFindings: [
      'Colorado sets a statutory floor and pushes the detail down: "Every ' +
        'local board of health in the state shall develop and adopt detailed ' +
        'rules" for onsite wastewater (C.R.S. 25-10-104(2)), and local rules ' +
        'must be "no less stringent" (25-10-104(4)).',
      'Whether you may install your own septic is a local question the statute ' +
        'does not answer — 25-10-109(1) says a local board "may" license ' +
        'systems contractors, which is permissive.',
      'Reg. 43 (5 CCR 1002-43) is commonly cited for OWTS minimums but was NOT ' +
        'independently verified in the kit\'s research pass; the kit cites the ' +
        'statute instead. Verify the CCR series number before relying on it.',
    ],
  },
  {
    code: 'ga',
    state: 'Georgia',
    guideSlug: 'georgia',
    verified: true,
    verifiedDate: 'August 2026',
    separations: {
      wellToSeptic: unknown(GA_DPH),
      wellToDrainfield: unknown(GA_DPH),
      wellToPropertyLine: unknown(GA_DPH),
      septicToPropertyLine: unknown(GA_DPH),
      septicToBuilding: unknown(GA_DPH),
      septicToSurfaceWater: unknown(GA_DPH),
      wellToSurfaceWater: unknown(GA_DPH),
    },
    setbacksNote: LOCAL_ZONING_SETBACKS,
    mustShow: [
      'Property lines',
      'Setbacks',
      'The building footprint',
      'System and drainfield location',
    ],
    negativeFindings: [
      'The septic gate is on site work, not on the building permit: no ' +
        '"physical development of a lot" where a septic system will be used ' +
        'until the county issues the construction permit.',
      'You may drill your own well if the property is your primary residence, ' +
        'but not on property you own and are developing for resale ' +
        '(O.C.G.A. § 12-5-131.1(a)).',
      'No statewide domestic-well permit was found; county requirements vary.',
      'Stream buffers bind even inside the single-family erosion-control ' +
        'exemption (§ 12-7-6(b) minimum standards), but the kit deliberately ' +
        'prints no buffer or proximity distance because it could not verify ' +
        'the exact statutory text. Read § 12-7-17 in full and ask your local ' +
        'issuing authority before relying on the exemption near any stream ' +
        'or lake.',
    ],
  },
  {
    code: 'ky',
    state: 'Kentucky',
    guideSlug: 'kentucky',
    verified: true,
    verifiedDate: 'August 2026',
    separations: {
      wellToSeptic: unknown(KY_REG),
      wellToDrainfield: unknown(KY_REG),
      wellToPropertyLine: unknown(KY_REG),
      septicToPropertyLine: unknown(KY_REG),
      septicToBuilding: unknown(KY_REG),
      septicToSurfaceWater: unknown(KY_REG),
      wellToSurfaceWater: unknown(KY_REG),
    },
    setbacksNote:
      'Building setbacks are local zoning, and Kentucky\'s own instruction is ' +
      'blunt: get setbacks in writing BEFORE you draw. Many Kentucky ' +
      'jurisdictions require zoning approval while issuing no building permit ' +
      'at all, so the zoning counter may be the only setback authority you ' +
      'ever meet.',
    negativeFindings: [
      'A homeowner MAY install their own septic system (902 KAR 10:110 §2(4)), ' +
        'but all work must be personally performed by the homeowner except ' +
        'excavation and backfill by a named certified installer — and no one ' +
        'may hold more than one homeowner permit in any five-year period.',
      'A homeowner may NOT drill their own well. KRS 223.405 requires a ' +
        'certified driller and there is no homeowner exemption.',
      'The septic permit gates both the plumbing permit (KRS 318.134(2)) and ' +
        'the electricity: an electrical inspector may not issue certificates ' +
        'of approval without a notice of release from the health department ' +
        '(KRS 211.350(8)).',
      'It is not a perc test — "percolation" appears zero times in ' +
        '902 KAR 10:085. Ratings come from soil morphology to 42 inches.',
      'Do not cite 902 KAR 10:060, 10:090, 10:100 or 10:130 — inactive or ' +
        'repealed, though web guides still quote 10:060 for fees.',
    ],
  },
  {
    code: 'mi',
    state: 'Michigan',
    guideSlug: 'michigan',
    verified: true,
    verifiedDate: 'August 2026',
    separations: {
      wellToSeptic: unknown(MI_NONE),
      wellToDrainfield: unknown(MI_NONE),
      wellToPropertyLine: unknown(MI_NONE),
      septicToPropertyLine: unknown(MI_NONE),
      septicToBuilding: unknown(MI_NONE),
      septicToSurfaceWater: unknown(MI_NONE),
      wellToSurfaceWater: unknown(MI_NONE),
    },
    extraSeparations: [
      {
        label: 'Soil-erosion permit trigger — from the water\'s edge',
        feet: 500,
        citation: 'R 323.1704(1)',
        note:
          'Not a septic setback, but the one distance that reliably changes a ' +
          'Michigan site plan: an earth change "within 500 feet of the ' +
          'water\'s edge of a lake or stream" needs a soil-erosion permit ' +
          'regardless of acreage (the other trigger being one acre). Measured ' +
          'to the water\'s edge — not the shoreline, not the ordinary ' +
          'high-water mark. No building permit may issue until that permit ' +
          'has been obtained.',
      },
    ],
    setbacksNote:
      'Building setbacks are local zoning — township, city or village, and in ' +
      'Michigan zoning is never preempted. Septic and wells run through the ' +
      'county or multi-county district health department.',
    mustShow: [
      'The dimensions of the proposed building or structure',
      'The location of the proposed building or structure',
      'Other buildings or structures on the same premises',
      'The drainfield and reserve area',
    ],
    negativeFindings: [
      'THE BIG ONE: no statewide septic setback, fee, percolation procedure or ' +
        'drainfield sizing figure exists. The research pass instruction is ' +
        'explicit — print none. Any number a Michigan builder is given comes ' +
        'from their district health department.',
      'Michigan regulates outhouses statewide (MCL 333.12771, R 325.421 et ' +
        'seq.) while not regulating septic systems statewide.',
      'You may drill your own well on property you own or lease for your own ' +
        'use, subject to the permit and the rules; well permitting is ' +
        'delegated to local health departments, which issue the construction ' +
        'permit BEFORE drilling.',
      'There is no statewide septic-permit-before-building-permit sequencing ' +
        'rule; the Part 91 soil-erosion link to the building permit ' +
        '(R 323.1711(2)) is verified, but there is no septic equivalent.',
    ],
  },
  {
    code: 'ms',
    state: 'Mississippi',
    guideSlug: 'mississippi',
    verified: true,
    verifiedDate: 'August 2026',
    separations: {
      wellToSeptic: unknown(MS_LOCAL),
      wellToDrainfield: unknown(MS_LOCAL),
      wellToPropertyLine: unknown(MS_LOCAL),
      septicToPropertyLine: unknown(MS_LOCAL),
      septicToBuilding: unknown(MS_LOCAL),
      septicToSurfaceWater: unknown(MS_LOCAL),
      wellToSurfaceWater: unknown(MS_LOCAL),
    },
    setbacksNote: LOCAL_ZONING_SETBACKS,
    mustShow: [
      'The legal description of the property',
      'The buildings and improvements',
      'The septic system location',
    ],
    negativeFindings: [
      'Mississippi well permitting specifics were NOT verified to primary text ' +
        'in the kit\'s research pass — the kit names the agency (MDEQ) and ' +
        'makes no threshold claim. Whether a household well needs a permit is ' +
        'an open question in the corpus.',
      'The sealed-plans threshold for one- and two-family dwellings is not ' +
        'verified as a statewide rule; the kit asks the reader to confirm ' +
        'locally.',
    ],
  },
  {
    code: 'tx',
    state: 'Texas',
    guideSlug: 'texas',
    verified: true,
    verifiedDate: 'August 2026',
    separations: {
      wellToSeptic: unknown(TX_LOCAL),
      wellToDrainfield: unknown(TX_LOCAL),
      wellToPropertyLine: unknown(TX_LOCAL),
      septicToPropertyLine: unknown(
        'No general state setback. There IS a 100 ft figure in Health & Safety ' +
          'Code § 366.052, but it is the condition of the 10-acre permitting ' +
          'exemption rather than a setback every Texas lot must meet — see ' +
          'extraSeparations. Drawing it for an ordinary lot would be wrong.'
      ),
      septicToBuilding: unknown(TX_LOCAL),
      septicToSurfaceWater: unknown(TX_LOCAL),
      wellToSurfaceWater: unknown(TX_LOCAL),
    },
    extraSeparations: [
      {
        label:
          'Field line to property line — condition of the 10-acre permit ' +
          'exemption ONLY',
        feet: 100,
        citation: 'Health & Safety Code § 366.052(a), (b)',
        note:
          'The permitting sections do not apply to a system serving "a single ' +
          'residence that is located on a land tract that is 10 acres or ' +
          'larger in which the field line or sewage disposal line is not ' +
          'closer than 100 feet of the property line," with effluent retained ' +
          'on-site, no nuisance and no groundwater pollution. Meet all of it ' +
          'and you are exempt from the permit; miss any of it and the ordinary ' +
          'county process applies. Not a universal setback.',
      },
    ],
    setbacksNote:
      'Building setbacks are municipal. Texas has no statewide residential ' +
      'building code enforcement outside municipalities, so on unincorporated ' +
      'land the binding site constraints are usually the septic permit, the ' +
      'floodplain permit and the driveway permit rather than zoning.',
    mustShow: [
      'Property lines',
      'Setbacks',
      'The building footprint',
      'The driveway',
      'Easements',
      'Drainage',
    ],
    negativeFindings: [
      'The OSSF permit functions as the de facto building permit on ' +
        'unincorporated land (Health & Safety Code § 366.051).',
      'A landowner MAY drill their own well: the licensing definition excludes ' +
        'a person who "drills, bores, cores, or constructs a water well on the ' +
        'person\'s own property for the person\'s own use" ' +
        '(Occupations Code § 1901.001(15)(A)). Groundwater conservation ' +
        'districts commonly require registration or a permit anyway, even for ' +
        'exempt domestic wells.',
    ],
  },
  {
    code: 'va',
    state: 'Virginia',
    guideSlug: 'virginia',
    verified: true,
    verifiedDate: 'August 2026',
    separations: {
      wellToSeptic: unknown(VA_LOCAL),
      wellToDrainfield: unknown(VA_LOCAL),
      wellToPropertyLine: unknown(VA_LOCAL),
      septicToPropertyLine: unknown(VA_LOCAL),
      septicToBuilding: unknown(VA_LOCAL),
      septicToSurfaceWater: unknown(VA_LOCAL),
      wellToSurfaceWater: unknown(VA_LOCAL),
    },
    setbacksNote: LOCAL_ZONING_SETBACKS,
    mustShow: [
      'Property lines',
      'Setbacks',
      'The building footprint',
      'System type and drainfield location',
    ],
    negativeFindings: [
      'No septic construction without a written VDH permit ' +
        '(12VAC5-610-240), and the construction permit is null and void once ' +
        '18 months elapse from issuance (12VAC5-610-300(A)).',
      'A permit is required before constructing, altering, or deepening a ' +
        'private well; the owner or agent applies at the local health ' +
        'department.',
    ],
  },
];

const VERIFIED_BY_CODE = new Map(VERIFIED_STATES.map((s) => [s.code, s]));

/**
 * All 50 states. The 12 with shipped kits carry verified data; the other 38 are
 * generated from the kit registry and carry DEFAULTS, so adding a state means
 * adding one entry to VERIFIED_STATES rather than editing a list of 50.
 */
export const SITEPLAN_RULES: StateSiteplanRules[] = STATE_KITS.map(
  (kit) =>
    VERIFIED_BY_CODE.get(kit.code) ?? {
      code: kit.code,
      state: kit.state,
      guideSlug: kit.guideSlug,
      verified: false,
      separations: DEFAULT_SEPARATIONS(),
      setbacksNote: LOCAL_ZONING_SETBACKS,
    }
);

const RULES_BY_CODE = new Map(SITEPLAN_RULES.map((s) => [s.code, s]));

/**
 * Rules for a state by lowercase postal code. Unknown codes fall back to
 * DEFAULTS — check `verified` before presenting any number as authoritative.
 */
export function getStateRules(code: string): StateSiteplanRules {
  return RULES_BY_CODE.get(code.toLowerCase()) ?? DEFAULTS;
}

/** True when this specific distance is backed by a citation in the corpus. */
export function isRuleVerified(rule: SeparationRule): boolean {
  return rule.feet !== null && rule.citation !== null;
}

/** The states whose data came from a shipped kit. */
export const VERIFIED_STATE_CODES: string[] = VERIFIED_STATES.map((s) => s.code);
