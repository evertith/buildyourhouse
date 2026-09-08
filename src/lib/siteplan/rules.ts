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
 * Only the shipped kit states in VERIFIED_STATES carry verified data. Every
 * other state falls back to DEFAULTS and must be presented to the user as
 * unverified.
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
 * Commonly-cited practice, for the states with no kit yet.
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
      'Most shipped states set no well-to-surface-water rule; where one exists ' +
      '(Louisiana 50 ft, Ohio 25 ft, South Carolina 50 ft, Wisconsin 25 ft) it lives on that state’s own entry. ' +
      'The 100 ft surface-water setbacks the defaults do carry are measured ' +
      'from the wastewater system, not the well. No number is offered here rather than ' +
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
 * The shipped kit states. Anything absent here is absent from the corpus.
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
    code: 'ar',
    state: 'Arkansas',
    guideSlug: 'arkansas',
    verified: true,
    verifiedDate: 'September 2026',
    separations: {
      wellToSeptic: {
        feet: 100,
        citation: '§ 6.2.3, ADH Rules Pertaining to Onsite Wastewater Systems (eff. Sept. 5, 2024)',
        note:
          'Tank and absorption field carry the same numbers — the rule ' +
          'measures to "facilities used for the collection, treatment, and ' +
          'renovation of wastewater." The well-side rule (17 CAR ' +
          '§ 11-502(c)) also sets 100 ft in clay and loam soils and directs ' +
          'doubling in highly pervious gravel formations — in karst country ' +
          'treat 200 ft as the working number.',
      },
      wellToDrainfield: {
        feet: 100,
        citation: '§ 6.2.3, ADH Rules Pertaining to Onsite Wastewater Systems',
        note: 'Same provision as the tank; Arkansas does not distinguish components.',
      },
      wellToPropertyLine: unknown(
        'No general number exists — ADH sets 50 ft to the lot line only for ' +
          'subdivision lot-sizing (§ 5.2); outside that context none was found.'
      ),
      septicToPropertyLine: {
        feet: 10,
        citation: '§ 6.2.7, ADH Rules Pertaining to Onsite Wastewater Systems',
        note: 'From all property lines. These distances are floors — "greater distances shall be required where local conditions demand" (§ 6.1).',
      },
      septicToBuilding: {
        feet: 10,
        citation: '§ 6.2.6, ADH Rules Pertaining to Onsite Wastewater Systems',
        note: 'From any dwelling or building.',
      },
      septicToSurfaceWater: {
        feet: 100,
        citation: '§ 6.2.4, ADH Rules Pertaining to Onsite Wastewater Systems',
        note:
          'To the high-water mark of any stream or lake. Rises to 300 ft ' +
          'within a quarter mile of a public water supply intake (§ 6.2.1); ' +
          'a pond on your own property gets 50 ft (§ 6.2.5).',
      },
      wellToSurfaceWater: unknown(NO_STATE_RULE),
    },
    extraSeparations: [
      {
        label: 'Septic to any sinkhole',
        feet: 100,
        citation: '§ 6.2.9, ADH Rules Pertaining to Onsite Wastewater Systems',
      },
      {
        label: 'Septic to any water service line',
        feet: 10,
        citation: '§ 6.2.8, ADH Rules Pertaining to Onsite Wastewater Systems',
      },
      {
        label: 'Septic to a pond on adjacent property, in the pond watershed',
        feet: 100,
        citation: '§ 6.2.5, ADH Rules Pertaining to Onsite Wastewater Systems',
      },
      {
        label: 'Field line to property line under the 10-acre exemption',
        feet: 200,
        citation: 'Ark. Code Ann. § 14-236-104(c)',
        note:
          'A condition of the exemption from ADH permitting on tracts of ten ' +
          'acres or larger — not a general setback. The exemption lives only ' +
          'in the statute and is absent from the 2024 rule, so cite the ' +
          'statute; county staff may not know it.',
      },
    ],
    setbacksNote:
      'Building setbacks are city zoning where a permit system exists at ' +
      'all — most Arkansas counties never created a building permit. The ' +
      'septic permit is the rural builder’s one real gate.',
    negativeFindings: [
      'No statewide number exists for swimming pools, basements beyond the ' +
        'generic 10 ft building distance, slopes, or wet-weather ditches — ' +
        'and no minimum lot size: a soil suitability test substitutes ' +
        '(§ 4.2).',
      'A homeowner may install their own system (§ 14-236-102(b)(2)) — the ' +
        'design must still come from a Designated Representative — and may ' +
        'drill their own well (§ 17-50-108(b)). No well permit exists; a ' +
        'construction report is due within 90 days.',
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
    code: 'fl',
    state: 'Florida',
    guideSlug: 'florida',
    verified: true,
    verifiedDate: 'September 2026',
    separations: {
      wellToSeptic: {
        feet: 75,
        citation: 'Rule 62-6.005(1)(a), F.A.C.',
        note:
          'From a private potable well or multi-family water well to the ' +
          'system. The rule does not distinguish the tank from the ' +
          'drainfield — the distance runs to the system as a whole.',
      },
      wellToDrainfield: {
        feet: 75,
        citation: 'Rule 62-6.005(1)(a), F.A.C.',
        note:
          'Same provision as the tank — Florida measures to the onsite ' +
          'sewage treatment and disposal system without distinguishing ' +
          'components.',
      },
      wellToPropertyLine: unknown(
        'Not set in the septic chapter, and the private-well construction ' +
          'rule carries no property-line number in the shipped research — ' +
          'your water management district and county set well siting.'
      ),
      septicToPropertyLine: {
        feet: 5,
        citation: 'Rule 62-6.005(2), F.A.C.',
        note:
          'Except where the line abuts a utility easement with no ' +
          'underground utilities, or a recorded shared-system easement.',
      },
      septicToBuilding: {
        feet: 5,
        citation: 'Rule 62-6.005(2), F.A.C.',
        note:
          'From building foundations including pilings, mobile home walls ' +
          'and pool walls. Sidewalks, decks and patios are not subject to ' +
          'the 5 ft setback, but a drainfield may not be installed beneath ' +
          'them.',
      },
      septicToSurfaceWater: {
        feet: 75,
        citation: 'Rule 62-6.005(3), F.A.C.',
        note:
          'Lateral, to permanent or tidally influenced surface water ' +
          'bodies. A normally dry ditch, swale or retention area gets 15 ft ' +
          'to its design high-water line instead.',
      },
      wellToSurfaceWater: unknown(NO_STATE_RULE),
    },
    extraSeparations: [
      {
        label: 'Septic to a public drinking water well (system ≤2,000 gal/day)',
        feet: 100,
        citation: 'Rule 62-6.005(1)(b), F.A.C.',
        note: 'Rises to 200 ft where the well serves a facility over 2,000 gal/day (62-6.005(1)(c)).',
      },
      {
        label: 'Septic to a non-potable water well',
        feet: 50,
        citation: 'Rule 62-6.005(1)(d), F.A.C.',
      },
      {
        label: 'Septic to potable water lines',
        feet: 10,
        citation: 'Rule 62-6.005(2)(b), F.A.C.',
        note: 'A sealed sleeve alternative exists; water lines within 24 inches of the system are restricted either way.',
      },
      {
        label: 'Septic to a dry ditch, swale or retention area',
        feet: 15,
        citation: 'Rule 62-6.005(1)(f), F.A.C.',
        note: 'To the design high-water line, where water stands less than 72 hours after rainfall.',
      },
    ],
    setbacksNote:
      'Building setbacks are county and municipal zoning. The septic chapter ' +
      'itself is under active rulemaking — core rules were amended 8 June ' +
      '2026 — so confirm the current text at flrules.org before you dig.',
    negativeFindings: [
      'The 75 ft surface-water setback is uniform — no larger coastal or ' +
        'tidal number exists in Rule 62-6.005; tidal and nontidal bodies get ' +
        'the same distance.',
      'Where you file is split mid-transfer: DEP permits directly in 17 ' +
        'counties (the Panhandle plus Marion); the other 50 still file with ' +
        'the county health department (ch. 2020-150, Laws of Florida).',
      'A lot served by a private well needs at least a half acre — 21,780 ' +
        'square feet — under Rule 62-6.005(7)(a).',
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
    code: 'la',
    state: 'Louisiana',
    guideSlug: 'louisiana',
    verified: true,
    verifiedDate: 'September 2026',
    separations: {
      wellToSeptic: {
        feet: 50,
        citation: 'LAC 51:XII.327.A.2',
        note: 'The Sanitary Code table row "Septic tanks — 50," for any water well.',
      },
      wellToDrainfield: {
        feet: 50,
        citation: 'LAC 51:XII.327.A.2 and footnote 2',
        note:
          'The table prints 100 ft to absorption fields, and footnote 2 ' +
          'reduces it to 50 ft for a PRIVATE water well — the single ' +
          'most-misreported number in Louisiana. A public water supply well ' +
          'keeps the full 100 ft.',
      },
      wellToPropertyLine: unknown(NO_STATE_RULE),
      septicToPropertyLine: {
        feet: 10,
        citation: 'LAC 51:XIII.719.I',
        note:
          'Absorption trenches at least 10 ft from any property line — and ' +
          'sand filter beds, effluent reduction fields and rock plant ' +
          'filters carry the same 10 ft. The TANK itself has no stated ' +
          'minimum: LDH prints "No minimum stated."',
      },
      septicToBuilding: {
        feet: 10,
        citation: 'LAC 51:XIII.719.I',
        note: 'Absorption trenches at least 10 ft from any dwelling.',
      },
      septicToSurfaceWater: unknown(
        'No statewide septic-to-surface-water minimum was found — the ' +
          'well side carries 50 ft to a canal, ditch, stream, pond or lake ' +
          'instead. Your parish sanitarian sets siting on wet ground.'
      ),
      wellToSurfaceWater: {
        feet: 50,
        citation: 'LAC 51:XII.327.A.2; LAC 56:I.315.A',
        note:
          'To a drainage canal, ditch or stream — measured from the highest ' +
          'water level of the last ten years, and the well agency’s own ' +
          'table adds ponds and lakes.',
      },
    },
    extraSeparations: [
      {
        label: 'Water well to the land-side toe of a levee',
        feet: 250,
        citation: 'LAC 56:I.317.A; R.S. 38:225(6)',
        note: 'Within 1,500 ft of a state or federal flood-control levee, levee board permission is required first (LAC 56:I.317.B).',
      },
      {
        label: 'Water well to another water well',
        feet: 25,
        citation: 'LAC 51:XII.327.A.2',
      },
      {
        label: 'Underground potable water line to absorption trenches or any effluent reduction option',
        feet: 25,
        citation: 'LAC 51:XIV.613.G',
        note: 'Ten feet to the septic tank or a mechanical plant (LAC 51:XIV.613.H).',
      },
      {
        label: 'Absorption trench to the adjacent trench, centerline',
        feet: 6,
        citation: 'LAC 51:XIII.719.I',
      },
    ],
    setbacksNote:
      'Building setbacks are parish and municipal zoning. Whether your soil ' +
      'takes a conventional field or forces a mechanical plant is the state ' +
      'health officer’s determination — and it changes which septic rules ' +
      'and which installer rules apply to you.',
    negativeFindings: [
      'The distances are split across four separate rule sets — LAC 51:XII ' +
        '(wells), 51:XIII (sewage), 51:XIV (water lines) and 56:I (the well ' +
        'agency) — which is why third-party summaries reading one part ' +
        'produce an incomplete table.',
      'Several published figures are advisory "should" language, not ' +
        'requirements — including the ATU-to-property-line distance. The ' +
        'numbers above are the mandatory ones.',
      'Hand-drawn site plans are explicitly accepted by LDH; the property ' +
        'plat behind them needs a surveyor’s seal or a Clerk of Court ' +
        '"true copy" designation — the second option costs far less.',
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
  {
    code: 'wi',
    state: 'Wisconsin',
    guideSlug: 'wisconsin',
    verified: true,
    verifiedDate: 'September 2026',
    separations: {
      wellToSeptic: {
        feet: 25,
        citation: 's. NR 812.08 Table A, Wis. Adm. Code',
        note:
          'Well to a septic or holding tank. Table A as amended by CR ' +
          '25-013, effective 1 March 2026 — cite the current table; older ' +
          'references abound.',
      },
      wellToDrainfield: {
        feet: 50,
        citation: 's. NR 812.08 Table A, Wis. Adm. Code',
        note: 'Well to a POWTS dispersal component — drainfield or mound.',
      },
      wellToPropertyLine: unknown(NO_STATE_RULE),
      septicToPropertyLine: unknown(
        'POWTS component setbacks live in SPS 383.43 Table 383.43-1, and ' +
          'determining POWTS setbacks is itself a regulated act reserved to ' +
          'licensed credential-holders (SPS 385.10(2)) — your master ' +
          'plumber or POWTS designer produces that plan.'
      ),
      septicToBuilding: unknown(
        'Set in SPS 383.43 Table 383.43-1 — the POWTS plan your licensed ' +
          'designer prepares carries it; the sanitary permit application ' +
          'cannot be completed without one.'
      ),
      septicToSurfaceWater: unknown(
        'Set POWTS-side in SPS 383.43, and county shoreland zoning under ' +
          'NR 115 separately controls structures near water — the county ' +
          'sanitary office answers both.'
      ),
      wellToSurfaceWater: {
        feet: 25,
        citation: 's. NR 812.08 Table A, Wis. Adm. Code',
        note:
          'Well to a shoreline. The pond-shoreline distance does not apply ' +
          'to synthetically lined decorative yard ponds on residential lots.',
      },
    },
    extraSeparations: [
      {
        label: 'Vertical: dispersal component above groundwater and bedrock',
        feet: 2,
        citation: 'SPS 383.44(3)(a), Wis. Adm. Code',
        note:
          '24 inches minimum. The 36-inch figure is the pre-2000 rule and ' +
          'the code says so itself — printing 3 feet would be wrong.',
      },
      {
        label: 'Well to a building sewer',
        feet: 8,
        citation: 's. NR 812.08 Table A, Wis. Adm. Code',
      },
    ],
    setbacksNote:
      'Building setbacks are local zoning plus shoreland and floodplain ' +
      'overlays the county administers (NR 115 puts structures 75 ft from ' +
      'the ordinary high-water mark, with a 35 ft floor where an existing ' +
      'development pattern allows). On unsewered land the sanitary permit ' +
      'must exist before the building permit can issue (s. 145.195(1)).',
    negativeFindings: [
      'You may drill your own well (s. 280.15(4); NR 812.10(1)(a)) after ' +
        'the mandatory pre-drilling notification (s. 281.34(3)(a)) — but ' +
        'you may NOT install your own septic: the sanitary permit ' +
        'application requires a licensed master plumber or MPRS (SPS ' +
        '383.21(2)(c)4.).',
      'A drainfield setback "does not apply if the component has been ' +
        'abandoned in accordance with s. SPS 383.33" (Table A footnote) — ' +
        'properly abandoning an old system can rescue a tight lot.',
      'No municipality may require your building-permit plans to be ' +
        'stamped by an architect or engineer for a UDC dwelling (SPS ' +
        '320.09(6)(c)) — the strongest owner-drawn-plan language of any ' +
        'state in this corpus.',
    ],
  },
  {
    code: 'pa',
    state: 'Pennsylvania',
    guideSlug: 'pennsylvania',
    verified: true,
    verifiedDate: 'September 2026',
    separations: {
      // 25 Pa. Code § 73.13 keeps three tables: treatment tanks (b), the
      // absorption-area perimeter (c), and spray fields (d). The absorption
      // area is the governing one for a conventional system, so its numbers
      // lead; the tank's smaller distances ride in notes.
      wellToSeptic: {
        feet: 50,
        citation: '25 Pa. Code § 73.13(b)',
        note:
          'Treatment tank to an individual water supply or suction line. ' +
          'The absorption area needs 100 ft — that larger circle usually ' +
          'controls the layout.',
      },
      wellToDrainfield: {
        feet: 100,
        citation: '25 Pa. Code § 73.13(c)',
        note:
          'Measured from the perimeter of the aggregate to an individual ' +
          'water supply or its suction line. § 73.13(a): these are minimums ' +
          'and "if conditions warrant, greater isolation distances may be ' +
          'required" — the Sewage Enforcement Officer decides.',
      },
      wellToPropertyLine: unknown(
        'Pennsylvania has no statewide private well construction standard — ' +
          'no state well permit and no state well-to-line distance. Some ' +
          'counties and municipalities regulate wells; ask yours.'
      ),
      septicToPropertyLine: {
        feet: 10,
        citation: '25 Pa. Code § 73.13(c)',
        note:
          'Absorption area to a property line, easement, or right-of-way. ' +
          'Same 10 ft for the treatment tank (§ 73.13(b)).',
      },
      septicToBuilding: {
        feet: 10,
        citation: '25 Pa. Code § 73.13(c)',
        note:
          'Absorption area to occupied buildings, swimming pools, and ' +
          'driveways alike.',
      },
      septicToSurfaceWater: {
        feet: 50,
        citation: '25 Pa. Code § 73.13(c)',
        note:
          'Absorption area to streams, watercourses, lakes, ponds, or other ' +
          'surface water; the treatment tank itself needs 25 ft. One gloss ' +
          'the chapter states outright: "wetlands are not surface waters" ' +
          'for these rules — do not apply this buffer to a mapped wetland.',
      },
      wellToSurfaceWater: unknown(
        'No statewide well construction standard exists, so no state number ' +
          'for a well near surface water.'
      ),
    },
    extraSeparations: [
      {
        label: 'Absorption area to mine subsidence areas, bore holes, or sinkholes',
        feet: 100,
        citation: '25 Pa. Code § 73.13(c)',
      },
      {
        label: 'Absorption area to another active on-lot system',
        feet: 5,
        citation: '25 Pa. Code § 73.13(c)',
      },
      {
        label: 'Absorption area to a surface drainageway or a slope over 25%',
        feet: 10,
        citation: '25 Pa. Code § 73.13(c)',
      },
      {
        label: 'Absorption area to a cistern used as a water supply',
        feet: 25,
        citation: '25 Pa. Code § 73.13(c)',
      },
    ],
    setbacksNote:
      'Building setbacks from lot lines are municipal zoning — roughly ' +
      '2,560 municipalities, no statewide value, so the write-in lines are ' +
      'the answer there. The septic permit comes from your municipality’s ' +
      'Sewage Enforcement Officer on a DEP form, and § 73.12 carries hard ' +
      'disqualifiers worth knowing before you sketch: slope over 25%, a ' +
      'mapped floodway (or 50 ft from the top of the stream bank where ' +
      'unmapped), rock outcrops in the absorption area, and sinkhole ' +
      'depressions in limestone country. Fill is unusable until it has ' +
      'been in place four years.',
    negativeFindings: [
      'Pennsylvania issues no state permit for a private residential ' +
        'water well and sets no statewide construction standard — the ' +
        'driller’s contract and any county rules are the only controls.',
      'Perc faster than 3.0 min/inch is Unsuitable (§ 73.16) — very fast ' +
        'ground fails, not just slow ground. Design flow is 400 gpd ' +
        'through three bedrooms plus 100 gpd per bedroom beyond.',
    ],
  },
  {
    code: 'oh',
    state: 'Ohio',
    guideSlug: 'ohio',
    verified: true,
    verifiedDate: 'September 2026',
    separations: {
      // Ohio groups its septic setbacks into two numbers (OAC
      // 3701-29-06(G)(3)) instead of a row-per-feature table; the well side
      // is a genuine 34-row table at OAC 3701-28-07(J). The two chapters
      // agree at the boundary: 50 ft between a live well and any part of
      // the system, stated from both sides.
      wellToSeptic: {
        feet: 50,
        citation: 'OAC 3701-29-06(G)(3)(c); OAC 3701-28-07(J) Table 1',
        note:
          'To any component of the system — tank, lines, or field; Ohio ' +
          'does not distinguish. The 50 ft applies to a live well. A ' +
          'properly sealed (abandoned) well needs only 10 ft — the ' +
          'asymmetry that rescues some small lots.',
      },
      wellToDrainfield: {
        feet: 50,
        citation: 'OAC 3701-29-06(G)(3)(c); OAC 3701-28-07(J) Table 1',
        note:
          'Same provision as the tank. The well must also clear the ' +
          'required replacement area (OAC 3701-29-06(G)(2)) — see the ' +
          'note below the tables.',
      },
      wellToPropertyLine: {
        feet: 10,
        citation: 'OAC 3701-28-07(J) Table 1',
        note: 'Lot lines and easements alike.',
      },
      septicToPropertyLine: {
        feet: 10,
        citation: 'OAC 3701-29-06(G)(3)(a)',
        note:
          'All system components to a property line or right-of-way ' +
          'boundary. Every Ohio number is a statewide floor the local ' +
          'health district may raise (OAC 3701-29-22).',
      },
      septicToBuilding: {
        feet: 10,
        citation: 'OAC 3701-29-06(G)(3)(a)',
        note: 'Any building or other structure, driveways and hardscape too.',
      },
      septicToSurfaceWater: {
        feet: 50,
        citation: 'OAC 3701-29-06(G)(3)(b)',
        note:
          'Absorption field to a lake, river, perennial stream, wetland, ' +
          'or impoundment. An intermittent stream or swale needs only ' +
          '10 ft from any component (G)(3)(a) — the field-vs-tank and ' +
          'perennial-vs-intermittent distinctions both matter here.',
      },
      wellToSurfaceWater: {
        feet: 25,
        citation: 'OAC 3701-28-07(J) Table 1',
        note: 'Permanent bodies of water — streams, lakes, ponds.',
      },
    },
    extraSeparations: [
      {
        label: 'Well to a leaching pit, drywell, or leaching privy not properly abandoned',
        feet: 100,
        citation: 'OAC 3701-28-07(J) Table 1',
      },
      {
        label: 'Well to a fuel or chemical tank under 1,100 gallons',
        feet: 50,
        citation: 'OAC 3701-28-07(J) Table 1',
      },
      {
        label: 'Well to a propane or natural gas heating tank',
        feet: 20,
        citation: 'OAC 3701-28-07(J) Table 1',
      },
      {
        label: 'Well to a dwelling foundation (10 ft) or deck edge (5 ft)',
        feet: 10,
        citation: 'OAC 3701-28-07(D)',
      },
      {
        label: 'Septic to a geothermal vertical loop (horizontal closed loops need 10 ft)',
        feet: 50,
        citation: 'OAC 3701-29-06(G)(3)(c)',
      },
    ],
    setbacksNote:
      'The rule that actually kills Ohio lots is not a setback: every new ' +
      'system needs a second, fully compliant replacement area meeting ' +
      'every distance above (OAC 3701-29-06(G)(1)), and the well must ' +
      'clear both areas (G)(2). Sketch the reserve area before falling in ' +
      'love with a site plan. Floodways, wetlands, and any public well’s ' +
      'sanitary isolation radius are prohibited outright (G)(H). Building ' +
      'setbacks from lot lines are local zoning — and in much of rural ' +
      'Ohio the health district is the only office that will ever review ' +
      'this drawing, because no residential building department is ' +
      'certified there.',
    negativeFindings: [
      'No statewide minimum lot size exists — but every separation is a ' +
        'floor the local health district may raise (OAC 3701-29-22), so ' +
        'confirm the local rules before staking anything.',
      'You cannot perform your own soil evaluation (certified soil ' +
        'scientist or equivalent required), and there is no blanket ' +
        'homeowner exemption for installing your own system — the ' +
        'fee/bond waiver in OAC 3701-29-03(H) applies to a registered ' +
        'installer working on their own home, so registration comes ' +
        'first. Drilling your own well is allowed only after registering ' +
        'with the Department of Health.',
    ],
  },
  {
    code: 'tn',
    state: 'Tennessee',
    guideSlug: 'tennessee',
    verified: true,
    verifiedDate: 'September 2026',
    separations: {
      // One table governs statewide: Rule 0400-48-01-.11(1). It measures
      // tank and disposal field in separate columns; where they differ the
      // field number leads and the tank rides in the note.
      wellToSeptic: {
        feet: 50,
        citation: 'Rule 0400-48-01-.11(1), "Water Supply" row',
        note:
          'The rule keeps one undifferentiated "Water Supply" row — it ' +
          'does not separate private wells from public lines. The well ' +
          'chapter states the same 50 ft from its side twice over ' +
          '(0400-45-09 Table A and .15(2)(j), which makes the driller ' +
          'confirm it on the completion report).',
      },
      wellToDrainfield: {
        feet: 50,
        citation: 'Rule 0400-48-01-.11(1), "Water Supply" row',
        note:
          'Same 50 ft as the tank. Beware a 25 ft figure floating around ' +
          'the well chapter — that is for closed-loop geothermal ' +
          'boreholes (Rule 0400-45-09-.17), not water wells.',
      },
      wellToPropertyLine: {
        feet: 10,
        citation: 'Rule 0400-45-09-.10(2)(d)',
        note:
          'Graduated, not flat: under 10 ft prohibited; 10–25 ft allowed ' +
          'only with 35 ft of cased-and-grouted construction; 25 ft or ' +
          'more is the normal case. Treat 25 ft as the planning number.',
      },
      septicToPropertyLine: {
        feet: 10,
        citation: 'Rule 0400-48-01-.11(1)',
        note: 'Tank and disposal field alike; same 10 ft to easements.',
      },
      septicToBuilding: {
        feet: 10,
        citation: 'Rule 0400-48-01-.11(1), "Dwellings" row',
        note: 'Disposal field 10 ft; the tank itself needs only 5 ft.',
      },
      septicToSurfaceWater: {
        feet: 25,
        citation: 'Rule 0400-48-01-.11(1), starred row',
        note:
          'Disposal field 25 ft, tank 15 ft — to streams, sinkholes, ' +
          'gullies, drainageways, and cut banks alike. The starred row is ' +
          'adjustable in BOTH directions by the Commissioner after a soil ' +
          'consultant’s investigation, so treat it as a default, not a ' +
          'hard line.',
      },
      wellToSurfaceWater: unknown(
        'No number found in either the septic or the well chapter — the ' +
          'well rules control contamination sources, not surface water ' +
          'distances.'
      ),
    },
    extraSeparations: [
      {
        label: 'Disposal field to water lines (tank the same)',
        feet: 10,
        citation: 'Rule 0400-48-01-.11(1)',
      },
      {
        label: 'Septic tank to dosing tank',
        feet: 5,
        citation: 'Rule 0400-48-01-.11(1)',
      },
      {
        label: 'House-to-tank sewer connection to the disposal field',
        feet: 10,
        citation: 'Rule 0400-48-01-.11(1)',
      },
    ],
    setbacksNote:
      'Tennessee sizes lots before it sets distances: 20,000 sq ft ' +
      'minimum on public water and 25,000 sq ft on a private well ' +
      '(0400-48-01-.09), and every system needs a 100% duplicate reserve ' +
      'area — sketch the reserve before committing to a layout, and if ' +
      'you are planning an LDGP system the reserve must be sized as if a ' +
      'conventional system were going in it. Slope over 30% is ' +
      'rebuttable, over 50% is a hard stop. Building setbacks from lot ' +
      'lines are local zoning; the septic permit is TDEC’s (form ' +
      'CN-0971), not the county health department’s, except in the nine ' +
      'contract counties.',
    negativeFindings: [
      'No numeric rule exists for driveways, springs, cisterns, or ' +
        'embankments as horizontal setbacks — those are handled as ' +
        'excluded areas (0400-48-01-.04(4)(b), which also names caves) ' +
        'or construction specs, so do not invent numbers for them.',
      'Draining stormwater into a sinkhole can create a regulated Class ' +
        'V injection well (TDEC UIC chapter 0400-45-06: an "improved ' +
        'sinkhole" is an injection well requiring authorization). Keep ' +
        'roof and driveway runoff away from karst features entirely.',
      'You may not drill your own well — Tennessee licenses well ' +
        'drillers, and TDEC states that even licensed GCs, electricians, ' +
        'and plumbers may not install or maintain wells or well pumps ' +
        'without a TDEC license.',
    ],
  },
  {
    code: 'sc',
    state: 'South Carolina',
    guideSlug: 'south-carolina',
    verified: true,
    verifiedDate: 'September 2026',
    separations: {
      // R.61-56 § 200.6(1) measures from any part of the system (solid
      // pipes excluded); R.61-71 § E.1 measures from the well. The two
      // regulations agree at the boundary: 75 ft both directions.
      wellToSeptic: {
        feet: 75,
        citation: 'R.61-56 § 200.6(1)(b); R.61-71 § E.1.c',
        note:
          'Private well — both regulations state the same 75 ft from ' +
          'their own side. A public well needs 100 ft (§ 200.6(1)(c)).',
      },
      wellToDrainfield: {
        feet: 75,
        citation: 'R.61-56 § 200.6(1)(b)',
        note:
          'Same provision — the rule measures to any part of the system, ' +
          'tank and field alike.',
      },
      wellToPropertyLine: {
        feet: 5,
        citation: 'R.61-71 § E.1.k',
        note: 'Same 5 ft to a building. The Department may require more ' +
          'for certain well types over fractured rock or shallow ' +
          'limestone (§ E.2).',
      },
      septicToPropertyLine: {
        feet: 5,
        citation: 'R.61-56 § 200.6(1)(k)',
        note:
          'The floor. Alternative-system appendices escalate it: four ' +
          'standards carry 75 ft on contiguous lots in subdivisions ' +
          'approved after the standard took effect, and Appendix P ' +
          '(elevated systems) carries an unconditional 50 ft from the ' +
          'retaining wall. Fill-cap systems measure from where the fill ' +
          'taper meets natural grade — roughly 15–20 ft beyond the ' +
          'trench per side.',
      },
      septicToBuilding: {
        feet: 5,
        citation: 'R.61-56 § 200.6(1)(a)',
        note:
          'Basements change it: 25 ft upslope, 15 ft on the sides — and ' +
          '25 ft on the sides where foundation drains sit at or below ' +
          'trench bottom (§ 200.6(1)(i)). The system also may not be ' +
          'placed under a driveway or parking area at all.',
      },
      septicToSurfaceWater: {
        feet: 75,
        citation: 'R.61-56 § 200.6(1)(d)',
        note:
          'To mean high water or the critical area line. Eight ' +
          'alternative-system appendices raise this to 125 ft — and ' +
          '"environmentally sensitive waters" includes lakes over 40 ' +
          'acres statewide, so a lakefront lot needing a fill-cap or ' +
          'mounded system gets the 125 ft line, not 75.',
      },
      wellToSurfaceWater: {
        feet: 50,
        citation: 'R.61-71 § E.1.b',
        note: 'Lake, stream, or other surface-water body.',
      },
    },
    extraSeparations: [
      {
        label: 'Septic to a public well',
        feet: 100,
        citation: 'R.61-56 § 200.6(1)(c)',
      },
      {
        label: 'Septic to a drainage ditch or stormwater detention pond (max water elevation)',
        feet: 25,
        citation: 'R.61-56 § 200.6(1)(f)',
      },
      {
        label: 'Septic to an inground pool',
        feet: 15,
        citation: 'R.61-56 § 200.6(1)(h)',
      },
      {
        label: 'Well to a sewer line',
        feet: 20,
        citation: 'R.61-71 § E.1.a',
      },
      {
        label: 'Septic to an upslope curtain drain (downslope needs 25 ft)',
        feet: 10,
        citation: 'R.61-56 § 200.6(1)(e)',
      },
    ],
    setbacksNote:
      'Enforcement is mandatory statewide (§ 6-9-10), so unlike the ' +
      'no-inspector states this drawing will be reviewed. Every new ' +
      'system needs a repair area of 50% of the original system’s size ' +
      '(§ 200.7). The trap on small lots is the alternative-system ' +
      'escalation: shallow water tables push you into fill-cap and ' +
      'mounded standards whose setbacks are measured from the fill ' +
      'taper and rise to 125 ft from water — a mounded system can ' +
      'consume a small lot’s buildable area outright. Building setbacks ' +
      'from lot lines are local zoning; wind and seismic design values ' +
      'cannot be printed by county because § 6-9-105(C) forbids drawing ' +
      'climatological boundaries on political lines — get both from ' +
      'your building official in writing.',
    negativeFindings: [
      'You may drill your own well — R.61-44 defines a well driller to ' +
        'include owners building wells on their own property for ' +
        'personal use, exempt from licensing and bonding. File the ' +
        'Notice of Intent ($70 residential): the agency must answer ' +
        'within 48 hours excluding weekends, or coverage is deemed ' +
        'approved.',
      'Vertical criteria decide lots as often as setbacks: 36 in to the ' +
        'zone of saturation below natural grade, 6 in below the deepest ' +
        'point of effluent application, and 12 in to rock ' +
        '(§§ 200.4–200.5).',
      'Since July 2024 septic and wells are SCDES (des.sc.gov) — DHEC ' +
        'no longer exists and scdhec.gov serves nothing, though many ' +
        'county pages still link to it.',
    ],
  },
  {
    code: 'id',
    state: 'Idaho',
    guideSlug: 'idaho',
    verified: true,
    verifiedDate: 'September 2026',
    separations: {
      // Three tables, read from both sides. DEQ's septic rules keep one for
      // the drainfield (IDAPA 58.01.03.008.01.d, by soil group A/B/C) and
      // one for the tank (58.01.03.007.18); IDWR's well construction
      // standards keep a third measured from the well (37.03.09.025.01.d).
      // They agree at the boundary — 50 ft to a tank, 100 ft to a
      // drainfield — and the drainfield column governs a conventional
      // system, so it leads and the tank rides in notes. Every number is a
      // statewide minimum the health district may raise: 58.01.03.001.02
      // lets the higher standard prevail, and the well rule says districts
      // set "additional siting and separation distance requirements."
      wellToSeptic: {
        feet: 50,
        citation: 'IDAPA 58.01.03.007.18; IDAPA 37.03.09.025.01.d',
        note:
          'Septic tank to a well, spring, or suction line that is not a ' +
          'public water supply (a public one needs 100 ft). The well rule ' +
          'states the same 50 ft from its side. The drainfield needs ' +
          '100 ft — that larger circle usually controls the layout.',
      },
      wellToDrainfield: {
        feet: 100,
        citation: 'IDAPA 58.01.03.008.01.d; IDAPA 37.03.09.025.01.d',
        note:
          'Drainfield to all wells and other domestic water supplies, the ' +
          'same in every soil group; the well rule states the same 100 ft ' +
          'from its side, and the well owner must keep the distance up ' +
          'after the well is in (37.03.09.036.04).',
      },
      wellToPropertyLine: {
        feet: 5,
        citation: 'IDAPA 37.03.09.025.01.d',
        note:
          'A sanitation number from the well construction standards, not ' +
          'a zoning setback — your county or city zoning may keep the ' +
          'well farther from the line.',
      },
      septicToPropertyLine: {
        feet: 5,
        citation: 'IDAPA 58.01.03.008.01.d; IDAPA 58.01.03.007.18',
        note:
          'Drainfield and septic tank alike, in every soil group. Like the ' +
          'well figure this is a sanitation minimum, not the zoning ' +
          'setback for the house.',
      },
      septicToBuilding: {
        feet: 10,
        citation: 'IDAPA 58.01.03.008.01.d',
        note:
          'Drainfield to a building foundation on a crawl space or slab. ' +
          'It becomes 20 ft the moment the foundation is a basement — ' +
          'sketch to 20 ft if the house will have one. The tank needs ' +
          '5 ft to a dwelling foundation or building (58.01.03.007.18).',
      },
      septicToSurfaceWater: {
        feet: 200,
        citation: 'IDAPA 58.01.03.008.01.d',
        note:
          'Drainfield to permanent or intermittent surface water other ' +
          'than canals and ditches, in Group A soils (coarse to fine sand, ' +
          'loamy sand). Group B (very fine sand, sandy loam, loam, silt ' +
          'loam, silt) needs 125 ft and Group C (clay loam, sandy clay ' +
          'loam, silty clay loam) 100 ft. The soil group comes from the ' +
          'district\'s test hole, so the largest figure is drawn until ' +
          'you have it. The tank needs 50 ft (58.01.03.007.18).',
      },
      wellToSurfaceWater: {
        feet: 50,
        citation: 'IDAPA 37.03.09.025.01.d',
        note:
          'Well to permanent (over 6 months) or intermittent (over 2 ' +
          'months) surface water; 25 ft to canals, ditches, laterals, and ' +
          'temporary surface water.',
      },
    },
    extraSeparations: [
      {
        label: 'Drainfield to a basement foundation (crawl space or slab needs 10 ft; tank 5 ft)',
        feet: 20,
        citation: 'IDAPA 58.01.03.008.01.d',
      },
      {
        label: 'Drainfield to temporary surface water or an irrigation canal or ditch (tank needs 25 ft)',
        feet: 50,
        citation: 'IDAPA 58.01.03.008.01.d',
      },
      {
        label: 'Drainfield to a water distribution line that is not double-encased (10 ft double-encased; tank 10 ft to a private line, 25 ft to a public one)',
        feet: 25,
        citation: 'IDAPA 58.01.03.008.01.d',
      },
      {
        label: 'Drainfield to a downslope cut or scarp with an impermeable layer above its base, Group A soil (50 ft in Groups B and C; 50/25/25 ft where the layer is below the base; tank 10 ft)',
        feet: 75,
        citation: 'IDAPA 58.01.03.008.01.d',
      },
      {
        label: 'Undisturbed earth between drainfield trenches, and between the tank and the nearest trench',
        feet: 6,
        citation: 'IDAPA 58.01.03.008.03',
      },
      {
        label: 'Vertical: drainfield bottom above an impermeable layer, every soil group',
        feet: 4,
        citation: 'IDAPA 58.01.03.008.01.c',
      },
      {
        label: 'Vertical: drainfield bottom above normal high groundwater or fractured bedrock, Group A soil (4 ft in Group B, 3 ft in Group C; 1 ft above seasonal high groundwater)',
        feet: 6,
        citation: 'IDAPA 58.01.03.008.01.c',
      },
      {
        label: 'Vertical: seasonal high water level below the top of the septic tank',
        feet: 2,
        citation: 'IDAPA 58.01.03.007.18',
      },
      {
        label: 'Well to a permanent building other than a well or plumbing house — and nobody may build closer once the well exists',
        feet: 10,
        citation: 'IDAPA 37.03.09.025.01.d; 37.03.09.036.03',
      },
      {
        label: 'Well to another existing well under separate ownership (50 ft to a public water supply well)',
        feet: 25,
        citation: 'IDAPA 37.03.09.025.01.d',
      },
      {
        label: 'Well to an effluent pipe or a gravity sewer main (pressurized main 100 ft; pressure-tested single-residence sewer line 25 ft)',
        feet: 50,
        citation: 'IDAPA 37.03.09.025.01.d',
      },
      {
        label: 'Well to an above-ground chemical storage tank',
        feet: 20,
        citation: 'IDAPA 37.03.09.025.01.d',
      },
    ],
    setbacksNote:
      'Every number above is a statewide minimum, not the answer: where a ' +
      'local ordinance is stricter the higher standard prevails ' +
      '(IDAPA 58.01.03.001.02), and each of the seven health districts ' +
      'may set "additional siting and separation distance requirements" ' +
      '(37.03.09.025.01.d) — get the district\'s septic checklist before ' +
      'you sketch. Sketch two drainfields: an acceptable site "must be ' +
      'large enough to construct two (2) complete drainfields," each ' +
      'sized for the full design flow (58.01.03.008.02.c), and the ' +
      'replacement area stays vacant, free of vehicles and of any soil ' +
      'modification (004.06). Hard disqualifiers: a standard drainfield ' +
      'site "will not exceed twenty percent (20%)" slope (008.01.a), an ' +
      'absorption bed cannot sit on a slope over 8% (008.09.b), gravel, ' +
      'sandy clay, silty clay, clay, shrink-swell clays, organic mucks and ' +
      'hardpan are unsuitable soils (008.01.b), and the permit may be ' +
      'denied where public or central sewer is "reasonably accessible" ' +
      '(005.05.c). Building setbacks from lot lines are zoning under the ' +
      'Local Land Use Planning Act — 44 counties and about 200 cities, no ' +
      'statewide value — and frost depth, ground snow load, wind and ' +
      'seismic are the county\'s to set by name (IRC R301 Design ' +
      'Criteria, § 39-4116(4)(c)(iii)); no state table exists. The one ' +
      'statewide depth figure is the 42-inch cover on the water service ' +
      'line (IDAPA 24.39.20.600.21), a plumbing rule for the utility ' +
      'trench, not a frost depth. Get all four from your building ' +
      'official in writing.',
    negativeFindings: [
      'You may install your own standard or basic alternative septic ' +
        'system — the installer\'s registration is not required for ' +
        '"owners installing their own standard or basic alternative ' +
        'system" (58.01.03.006.08.b), though the installation permit ' +
        'still is (005.01) and a complex system needs a registered ' +
        'complex installer. You may NOT drill your own well: § 42-238(3) ' +
        'defines a person to include "any individual who drills or ' +
        'abandons any well for himself or another," and the $75 IDWR ' +
        'drilling permit (§ 42-235) comes before any drilling.',
      'Design flow is 250 gpd for three bedrooms, plus or minus 50 gpd ' +
        'per bedroom (58.01.03.007.09). The tank is 1,000 gal minimum, ' +
        'plus 250 gal for each bedroom over four (007.08.a). Drainfield ' +
        'area is design flow divided by an application rate of 1.0, 0.5, ' +
        'or 0.2 gal per sq ft per day for soil Groups A, B and C ' +
        '(008.02.b) — 500 sq ft of trench bottom for three bedrooms on ' +
        'Group B, twice over for the replacement area. Laterals run ' +
        '100 ft at most, trenches 1–6 ft wide and 2–4 ft deep under at ' +
        'least 12 in of cover, and a system tops out at 1,500 sq ft of ' +
        'trench (008.03).',
      'The septic permit runs through the health district: a test-hole ' +
        'or site inspection on 48 hours\' notice, then a final with an ' +
        'as-built before any wastewater enters the system ' +
        '(58.01.03.011.03, .05). The driller files the well report with ' +
        'IDWR within 30 days (§ 42-238(11)), and the casing must stand at ' +
        'least 12 in above finished grade (37.03.09.025.04).',
      'None of the above is a building setback or a design-criteria ' +
        'value, and in a county with no building ordinance no building ' +
        'permit is issued at all (§ 39-4111) — the health-district septic ' +
        'permit and the IDWR drilling permit are then the only land ' +
        'approvals that exist.',
    ],
  },
  {
    code: 'ne',
    state: 'Nebraska',
    guideSlug: 'nebraska',
    verified: true,
    verifiedDate: 'September 2026',
    separations: {
      // Two tables, read from both sides. NDEE Title 124 ch. 2 Table 2.1
      // (effective 27 June 2022) keeps tank / absorption / lagoon columns;
      // the absorption column governs a conventional system, so it leads
      // and the tank rides in notes. DWEE Title 134 ch. 4 Chart 1
      // (effective 28 June 2026, superseding Title 178 ch. 12) measures
      // from the well and agrees at the boundary: 50 ft to a tank, 100 ft
      // to a lateral field. Every number is a state floor a delegated
      // local program may raise (Title 124 ch. 2 § 014; Title 134 ch. 4
      // § 001).
      wellToSeptic: {
        feet: 50,
        citation: 'Title 124 ch. 2 Table 2.1; Title 134 ch. 4 Chart 1',
        note:
          'Septic tank to a private drinking-water well. Chart 1 states ' +
          'the same 50 ft from the well side ("Any septic tank"). The ' +
          'absorption system needs 100 ft — that larger circle usually ' +
          'controls the layout. A public community well needs 500 ft ' +
          'from either.',
      },
      wellToDrainfield: {
        feet: 100,
        citation: 'Title 124 ch. 2 Table 2.1; Title 134 ch. 4 Chart 1',
        note:
          'Absorption system to a private well; Chart 1 states the same ' +
          '100 ft from the well side ("Any septic lateral field"). Chart 2 ' +
          'lets a driller close to 50–100 ft only where Chart 1 cannot be ' +
          'met, with prior written DWEE approval and full-length bentonite ' +
          'grout — a variance, not a planning number.',
      },
      wellToPropertyLine: unknown(
        'Title 134 ch. 4 Chart 1 has no property-line row — a verified ' +
          'absence. The only ownership-based distances (600 ft to an ' +
          'irrigation well, 1,000 ft to an industrial or community well ' +
          'under different ownership) apply only to drilling irrigation ' +
          'and industrial wells.'
      ),
      septicToPropertyLine: {
        feet: 5,
        citation: 'Title 124 ch. 2 Table 2.1',
        note:
          'Tank and absorption system alike; a lagoon needs 50 ft. The ' +
          'same 5 ft applies to a driveway, parking area, sidewalk, or ' +
          'other impermeable surface.',
      },
      septicToBuilding: {
        feet: 10,
        citation: 'Title 124 ch. 2 Table 2.1',
        note:
          'Absorption system to a Class 2 foundation — the house higher in ' +
          'elevation than the system, the default case. It becomes 30 ft ' +
          'the moment any part of the basement, footing, or slab living ' +
          'quarters sits LOWER than the system (Class 1); a slab that is ' +
          'not living quarters (Class 3) stays at 10 ft. The tank needs ' +
          '10 ft (Class 2) or 15 ft (Class 1); a lagoon needs 100 ft.',
      },
      septicToSurfaceWater: {
        feet: 50,
        citation: 'Title 124 ch. 2 Table 2.1',
        note: 'Tank, absorption system, and lagoon all 50 ft.',
      },
      wellToSurfaceWater: unknown(
        'Title 134 ch. 4 Chart 1 has no surface-water row — a verified ' +
          'absence. The nearest rules are 10 ft to any storm water way and ' +
          '10 ft to any depression that could retain stagnant water.'
      ),
    },
    extraSeparations: [
      {
        label: 'Absorption area to a pressure water main, service line, or suction line (tank needs 10 ft)',
        feet: 25,
        citation: 'Title 124 ch. 2 Table 2.1',
      },
      {
        label: 'Absorption area to a driveway, parking area, sidewalk, or impermeable surface (reserve area too)',
        feet: 5,
        citation: 'Title 124 ch. 2 Table 2.1; GTS220000 § III.K.12',
      },
      {
        label: 'Absorption area to a neighbour’s Class 2 foundation (40 ft if theirs sits lower, Class 1)',
        feet: 30,
        citation: 'Title 124 ch. 2 Table 2.1',
      },
      {
        label: 'Septic to a horizontal closed-loop geothermal well (tank and field alike)',
        feet: 25,
        citation: 'Title 124 ch. 2 Table 2.1',
      },
      {
        label: 'Well to a pressurized or non-watertight sanitary sewer line (watertight sanitary or storm sewer needs 10 ft)',
        feet: 50,
        citation: 'Title 134 ch. 4 Chart 1',
      },
      {
        label: 'Well to a wastewater lagoon, privy, cesspool, or subsurface disposal system',
        feet: 100,
        citation: 'Title 134 ch. 4 Chart 1',
      },
      {
        label: 'Well to an animal-waste structure or feeding-operation holding pens',
        feet: 100,
        citation: 'Title 134 ch. 4 Chart 1',
      },
      {
        label: 'Well to a storm water way, frost-proof hydrant, or well pit',
        feet: 10,
        citation: 'Title 134 ch. 4 Chart 1',
      },
      {
        label: 'Vertical: trench or bed bottom above seasonal high groundwater or a barrier layer',
        feet: 4,
        citation: 'GTS220000 § III.C, § III.K.1',
      },
      {
        label: 'Undisturbed soil between trenches, and tank to nearest trench, on slopes under 10% (6 ft at 10–20%, 10 ft over 20%)',
        feet: 4,
        citation: 'GTS220000 § III.K.9',
      },
    ],
    setbacksNote:
      'Every number above is a state floor: Title 124 ch. 2 § 014 and ' +
      'Title 134 ch. 4 § 001 both let local requirements be stricter, and ' +
      'the delegated programs (Lincoln-Lancaster, Douglas, Sarpy and others ' +
      'under § 81-15,248(3)) may be — treat their counter as the ceiling, ' +
      'not this table. Sketch the reserve area first: it is mandatory and ' +
      'carries every setback (ch. 2 § 008), and once the system is in, ' +
      'nobody may build a foundation, well, water line, surface-water ' +
      'feature, or property line inside a Table 2.1 distance without a PE ' +
      'letter (§ 011). GTS220000 disqualifiers: a system in fill is ' +
      'prohibited except sand fill or where the bottom 12 in of trench ' +
      'sits in undisturbed native soil; slope over 3% needs drop-box or ' +
      'pressure distribution unless every trench bottom is at one ' +
      'elevation; a gravity trench runs 150 ft at most. Building setbacks ' +
      'from lot lines are county zoning (§ 23-114(2)(c)) or city zoning ' +
      'with no statewide value, and frost depth, snow load, and wind speed ' +
      'are filled in locally on IRC Table R301.2 — no state table exists, ' +
      'and the "42 inches" often quoted for Omaha is unverified. Get all ' +
      'four from your building official in writing.',
    ownerDrawnAccepted:
      'The septic drawing is not yours to file. General-permit coverage ' +
      '(GTS220000 § II.A) requires "an appropriately scaled drawing of the ' +
      'onsite wastewater treatment system" submitted with the registration ' +
      'and a certification signed by the PE, REHS, or certified installer ' +
      'who supervised the work — and § 81-15,248(1) puts that professional ' +
      'on site for the siting and layout, so draft here, then hand it ' +
      'over. For a well variance you file the map yourself: "a scaled map ' +
      'showing the location of the well in relation to property lines, ' +
      'structures, utilities, and contamination sources," at least 10 days ' +
      'before drilling (Title 134 ch. 4 § 012.01). The building-permit ' +
      'site plan is local, where a program exists at all.',
    negativeFindings: [
      'You may drill your own well on land you own and use as your place ' +
        'of abode (§ 46-1233(2)) and register it yourself within 60 days ' +
        '(§ 46-602(1)) — but you may NOT install your own septic system: a ' +
        'certified installer, PE, or REHS must be physically present and ' +
        'supervising (§ 81-15,248(1); Title 124 ch. 9 § 004).',
      'Perc faster than 5 min/inch fails without a 12-inch loamy-sand ' +
        'liner, and slower than 60 min/inch is off the general permit ' +
        '(GTS220000 § III.J). Design flow is 100 gpd plus 100 gpd per ' +
        'bedroom — 400 gpd for three bedrooms (Table 1). A three-bedroom ' +
        'tank is 1,000 gal, 1,250 with a grinder pump or a tub over 50 ' +
        'gal, 1,500 with both (Table 3); its trench bottom area runs from ' +
        '495 sq ft at 5–10 min/inch to 1,050 sq ft at 50–60 (Table 5).',
      'The house-to-drainfield distance triples — 10 ft to 30 ft — when ' +
        'any part of the basement or footing sits lower than the system ' +
        '(Title 124 Table 2.1, Class 1).',
      'Title 134 ch. 4 (2026) has no well-to-property-line rule; the ' +
        '600/1,000 ft rows apply only to irrigation and industrial wells. ' +
        'Anything citing Title 178 ch. 12 for well distances is stale — it ' +
        'was superseded 28 June 2026.',
    ],
  },
  {
    code: 'az',
    state: 'Arizona',
    guideSlug: 'arizona',
    verified: true,
    verifiedDate: 'September 2026',
    separations: {
      // Two rulebooks, read from both sides. ADEQ's onsite table, A.A.C.
      // R18-9-A312(C) Table 1 (text current through the 19 June 2023
      // amendment, 29 A.A.R. 1023), measures from the whole facility —
      // tank, disposal works and, in the table's own words, "Including
      // Reserve Area" — and is administered by the county agency ADEQ has
      // delegated under § 49-107. ADWR's well construction rule
      // R12-15-818 measures from the well and agrees at the boundary:
      // 100 ft to any septic tank system or sewage disposal area. Every
      // number is a regulatory minimum: A312(C)(3) lets the agency set "a
      // more stringent setback on a site- or area-specific basis."
      wellToSeptic: {
        feet: 100,
        citation: 'A.A.C. R18-9-A312(C), Table 1; A.A.C. R12-15-818',
        note:
          'Septic tank to a public or private water supply well. ADWR ' +
          'states the same 100 ft from the well side: "no well shall be ' +
          'drilled within 100 feet of any septic tank system, sewage ' +
          'disposal area," waivable only in writing by the ADWR Director. ' +
          'The disposal works and their reserve area need the same 100 ft.',
      },
      wellToDrainfield: {
        feet: 100,
        citation: 'A.A.C. R18-9-A312(C), Table 1; A.A.C. R12-15-818',
        note:
          'Disposal works to a public or private water supply well, and ' +
          'the reserve area counts: the table\'s setbacks apply to the ' +
          'facility "Including Reserve Area." The well rule\'s "sewage ' +
          'disposal area" states the same 100 ft from its side, and it is ' +
          'the same 100 ft a neighbor must promise in the property-line ' +
          'waiver below.',
      },
      wellToPropertyLine: unknown(
        'No well-to-property-line distance exists in A.R.S. Title 45 or ' +
          '12 A.A.C. 15 Article 8 — a verified absence. R12-15-818 fixes ' +
          '100 ft to septic systems and contamination sources only; the ' +
          'property line is reached indirectly, through ADEQ\'s 50 ft ' +
          'septic-to-line rule where the neighbor has no well.'
      ),
      septicToPropertyLine: {
        feet: 50,
        citation: 'A.A.C. R18-9-A312(C), Table 1',
        note:
          'Tank, disposal works and reserve area alike, to a property ' +
          'line shared with any adjoining lot "not served by a common ' +
          'drinking water system or an existing water well" — the ' +
          'undeveloped rural neighbor who could still drill. All other ' +
          'property lines need 5 ft. The 50 ft drops "to a minimum of ' +
          '5 feet" only where the affected neighbors agree, in a recorded ' +
          'document, to keep any new well at least 100 ft from the system ' +
          'and its reserve, and the agency approves; the larger figure is ' +
          'drawn until that document is on record.',
      },
      septicToBuilding: {
        feet: 10,
        citation: 'A.A.C. R18-9-A312(C), Table 1',
        note:
          'Tank, disposal works and reserve area to a building, and ' +
          '"building" reaches further than the house: it "Includes ' +
          'porches, decks (including pool decks), and steps (covered or ' +
          'uncovered), breezeways, roofed patios, carports, covered walks, ' +
          'and similar structures." A swimming pool excavation needs 5 ft.',
      },
      septicToSurfaceWater: {
        feet: 100,
        citation: 'A.A.C. R18-9-A312(C), Table 1',
        note:
          'To a perennial or intermittent stream, measured "from the high ' +
          'water line of the peak streamflow from a 10-year, 24-hour ' +
          'rainfall event," and the same 100 ft to a lake, reservoir, or ' +
          'canal (a canal "from the edge of the canal"). A drinking water ' +
          'intake from a surface water source needs 200 ft; a wash or ' +
          'drainage easement draining more than 20 acres needs 50 ft.',
      },
      wellToSurfaceWater: unknown(
        'No well-to-surface-water distance in the shipped research. ' +
          'R12-15-818 (Well Location) lists septic tank systems, sewage ' +
          'disposal areas, landfills, hazardous waste facilities and ' +
          'petroleum storage — not surface water — and R12-15-821 lets ' +
          'the Director require a greater distance from any potential ' +
          'source of contamination.'
      ),
    },
    extraSeparations: [
      {
        label: 'Septic (reserve area included) to earth fissures',
        feet: 100,
        citation: 'A.A.C. R18-9-A312(C), Table 1',
      },
      {
        label: 'Septic to a wash or drainage easement with a drainage area over 20 acres, from the natural channel bank or easement boundary (25 ft with erosion protection the floodplain administrator approves)',
        feet: 50,
        citation: 'A.A.C. R18-9-A312(C), Table 1',
      },
      {
        label: 'Septic to a drinking water intake from a surface water source',
        feet: 200,
        citation: 'A.A.C. R18-9-A312(C), Table 1',
      },
      {
        label: 'Septic to a water main or branch water line (domestic service line, including a domestic water holding tank, 5 ft)',
        feet: 10,
        citation: 'A.A.C. R18-9-A312(C), Table 1',
      },
      {
        label: 'Trench, bed, chamber or gravelless trench to a downslope or cut bank over 15%, culvert or ditch, to the closest point of daylighting (50 ft with a limiting subsurface condition; treatment works 10 ft; drip lines 3 ft)',
        feet: 20,
        citation: 'A.A.C. R18-9-A312(C), Table 1',
      },
      {
        label: 'Septic to a driveway, to the nearest edge of the excavation (a reinforced tank may sit under a driveway; disposal works may not)',
        feet: 5,
        citation: 'A.A.C. R18-9-A312(C), Table 1',
      },
      {
        label: 'Septic to a swimming pool excavation, and to any easement other than a drainage easement',
        feet: 5,
        citation: 'A.A.C. R18-9-A312(C), Table 1',
      },
      {
        label: 'Between trenches: twice the effective depth or 5 ft, whichever is greater',
        feet: 5,
        citation: 'A.A.C. R18-9-E302(C)(2)(c)',
      },
      {
        label: 'Vertical: trench or chamber to the seasonal high water table at a soil absorption rate of 0.63–1.20 gal/day/sq ft (5 ft at 0.20–0.63; a seepage pit 60 ft; outside 0.20–1.20 "Not allowed for septic tank effluent")',
        feet: 10,
        citation: 'A.A.C. R18-9-A312(E)(1)',
      },
    ],
    setbacksNote:
      'Every number above is a regulatory minimum, not an approval: the ' +
      'table applies unless the Department "Establishes a more stringent ' +
      'setback on a site- or area-specific basis" (R18-9-A312(C)(3)), and ' +
      'the delegated county agency that issues the permit under § 49-107 ' +
      'may do exactly that — get its setback sheet before you sketch. Every ' +
      'setback is measured to the facility "Including Reserve Area," so ' +
      'sketch the reserve first: for a dwelling it is "a reserve area of ' +
      '100 percent of the primary area, excluding the footprint of the ' +
      'treatment works" (A312(D)(4)(a)), waived only for a lot in a ' +
      'subdivision approved before 1974 that keeps its original ' +
      'configuration. Arizona names no disqualifiers; it names "limiting ' +
      'conditions," and any one of them takes away the standard ' +
      'septic-tank design (E302(A)(1)) and pushes you to an alternative ' +
      'system with a designer of record. Surface (A310(C)(2)): slope ' +
      '"greater than 15 percent at the intended location," a setback in ' +
      'the table not met, adverse surface drainage, a 100-year flood ' +
      'hazard zone on the property that may affect the system, "An ' +
      'outcropping of rock that cannot be excavated," or fill in the ' +
      'intended location. Subsurface, within 12 ft of grade (A310(D)(2)): ' +
      'a soil absorption rate above 1.20 or below 0.20 gal/day/sq ft, less ' +
      'vertical separation than A312(E)(1), seasonal saturation, an ' +
      'impervious layer, "Soil with more than 50 percent rock fragments," ' +
      'or open fractures, karst, or cobbles. Before any of it, ask whether ' +
      'a sewer stub reaches the lot line: R18-9-A309(A)(5) requires ' +
      'connection where "A sewer service line extension is available at ' +
      'the property boundary" and the connection fee is not more than ' +
      '$6,000 and the building sewer not more than $3,000 (the rule\'s ' +
      'thresholds, not fees), or where a county, municipal, or sanitary ' +
      'district ordinance says so. Building setbacks from lot lines are ' +
      'zoning — county under A.R.S. Title 11, Ch. 6, Art. 1 and municipal ' +
      'under § 9-462.01 — with no statewide value. Frost depth, ground ' +
      'snow load, wind, seismic and flood are the locally adopted IRC ' +
      'Table R301.2 as amended; no state table exists. Even the code ' +
      'edition is local: Arizona has no statewide residential code, only ' +
      'adoption by reference under § 11-861 (counties) and § 9-802 ' +
      '(cities), the unincorporated spread runs from the 2003 IRC (Graham ' +
      'County) to the 2024 IRC, and Greenlee County has adopted no ' +
      'building code at all. Get all of it from your building official in ' +
      'writing, with the adopting ordinance number.',
    ownerDrawnAccepted:
      'Two drawings, and you file both. For a domestic well on a parcel of ' +
      'five acres or less, § 45-596(F) puts "a well site plan of the ' +
      'property" in your own notice of intention to drill — the notice ' +
      '"shall be signed by the owner or lessee of the property" ' +
      '(R12-15-809) — showing the assessor\'s parcel number, the proposed ' +
      'well, any septic tank or sewer system on the property or "within ' +
      'one hundred feet of the proposed well site," and the county health ' +
      'authority\'s written approval. For a conventional septic system the ' +
      'Discharge Authorization turns on the applicant\'s own site plan: it ' +
      'must accurately reflect "the final location and configuration of ' +
      'the components of the treatment and disposal works" ' +
      '(R18-9-A309(C)(1)(a)), with changes made during construction ' +
      'recorded on it (A301(D)(1)(e)), and no installer license number is ' +
      'asked for. What you cannot draw is the soils: the site ' +
      'investigation behind the numbers belongs to an Arizona-registered ' +
      'engineer, geologist, or sanitarian, or a holder of a ' +
      'Department-recognized training certificate (A310(H)). The ' +
      'building-permit site plan is local; in a county it is at least "a ' +
      'sketch of the proposed construction containing sufficient ' +
      'information for the enforcement of the zoning ordinance" ' +
      '(§ 11-815(B)).',
    mustShow: [
      'For a domestic well on five acres or less, the county assessor\'s parcel identification number (§ 45-596(F))',
      'The proposed well location, and any septic tank or sewer system on the property or within 100 ft of the proposed well site (§ 45-596(F))',
      'Written approval by the county health authority that controls septic installation (§ 45-596(F))',
      'The final location and configuration of every treatment and disposal component, reserve area included (R18-9-A309(C)(1)(a); A312(C))',
    ],
    negativeFindings: [
      'You may install your own conventional septic system: for a facility ' +
        'permitted entirely under R18-9-E302, the Discharge Authorization ' +
        'turns on an accurate site plan and a certified tank ' +
        'watertightness test (A309(C)(1)) — no installer license number ' +
        'is required — and § 32-1121(A)(5) lets an owner "do the work ' +
        'themselves." An alternative system (anything under E303 to E323) ' +
        'is different: A309(C)(2) requires "The name of the installation ' +
        'contractor and the Registrar of Contractor\'s license number" and ' +
        'a Certificate of Completion from the designer of record, who must ' +
        'verify the installation before backfill. In both cases the site ' +
        'investigation is a licensed act (A310(H)): an owner-builder ' +
        'cannot self-certify the percolation test, and it takes at least ' +
        'two test locations in the primary area and one in the reserve ' +
        '(A310(E)(1), (F)(1)(a)).',
      'You may drill your own exempt well on your own land, but only ' +
        'under a single well license (§ 45-595(D)) — no fee, yet ' +
        'R12-15-807 makes it an examination, offered at least six times a ' +
        'year with a 70 percent passing grade, good for one well at one ' +
        'location for one year. Anyone else is a licensed well driller ' +
        '(§ 45-595(A)). Either way the notice of intention to drill comes ' +
        'first (§ 45-454(G), § 45-596): $150, or $100 for a domestic well ' +
        'of 35 gpm or less outside an active management area or ' +
        'irrigation nonexpansion area (§ 45-596(L)); the drilling card ' +
        'arrives within 15 days and must be at the well site before ' +
        'drilling starts (§ 45-596(D); R12-15-810(A)); the well must be ' +
        'completed within one year (§ 45-596(E)). The driller reports ' +
        'within 30 days and the owner files a completion report within ' +
        '30 days of pump installation (§ 45-600). Casing is steel or ' +
        'thermoplastic and stands at least 1 ft above ground, over a ' +
        'surface seal of at least 20 ft of steel casing and cement grout ' +
        'placed in one continuous application (R12-15-811(A)(1), ' +
        '(B)(1)); the Director may require a longer seal or a greater ' +
        'distance from a contamination source (R12-15-821).',
      'Inside an active management area established on or before 1 July ' +
        '1994, no exempt well may be drilled "if any part of the land is ' +
        'within one hundred feet of the operating water distribution ' +
        'system of a municipal provider with an assured water supply ' +
        'designation" (§ 45-454(C)) — a 100 ft rule that runs from the ' +
        'utility\'s mains, not from your septic. Exemptions exist on ' +
        'request where service is refused within 30 days, connecting ' +
        'costs more than the well, an easement is refused, or a ' +
        'no-service agreement is signed (§ 45-454(D)); one exempt well ' +
        'per use per site is the AMA rule (§ 45-454(I)). An exempt well ' +
        'is one pumping at most 35 gallons per minute (§ 45-454(B)).',
      'Sizing is by bedrooms AND fixture count (R18-9-A314(A)(4)(a)). ' +
        'Three bedrooms with 21 fixture units or fewer is 450 gpd and a ' +
        '1,000 gal tank; over 21 it is 600 gpd and 1,250 gal; the minimum ' +
        'tank on any dwelling is 1,000 gal. A 1.6 gpf water closet counts ' +
        '3 units, a tub, clothes washer, dishwasher, or kitchen sink 2, a ' +
        'lavatory 1 — two full baths, a kitchen, laundry and a utility ' +
        'sink already sit near the 21-unit line. Absorption area is design ' +
        'flow divided by the soil absorption rate (A312(D)(1)); at a 10 ' +
        'min/in percolation rate the trench SAR is 0.63, so 450 ÷ 0.63 is ' +
        'about 714 sq ft, then the same again in reserve. Faster than 1 ' +
        'min/in or slower than 120 needs a site-specific SAR; between ' +
        'listed values use the slower rate (A312(D)(2)). A trench runs ' +
        '100 ft at most with a 12–36 in bottom, and nothing may be paved ' +
        'over a disposal works (E302(C)(2)(c), (C)(1)(h)).',
      'The septic permit is a two-step Aquifer Protection Permit: no ' +
        'construction "until the Director issues a Construction ' +
        'Authorization," construction complete within two years, then a ' +
        'Request for Discharge Authorization, which the agency may inspect ' +
        'before the Discharge Authorization issues — miss the two years ' +
        'and the Notice of Intent expires (R18-9-A301(D)). ADEQ\'s own ' +
        'Notice of Intent form (DWS 402, April 2025) states its clock ' +
        'under R18-1-525 as 73 business days overall, 42 administrative ' +
        'plus 31 substantive, with each A312(G) alternative-setback ' +
        'request adding eight; a delegated county\'s clock is the ' +
        'county\'s own, and a county residential-lot permit sits outside ' +
        'the statutory time-frame rules altogether (§ 11-1605(M)(2)).',
      'Title 45 and 12 A.A.C. 15 Article 8 set no well-to-property-line ' +
        'distance; the line is reached only through ADEQ\'s 50 ft ' +
        'septic-to-line rule where the neighbor has no well. And none of ' +
        'the above is a building setback or a design-criteria value: ' +
        'every county must issue a building permit for construction over ' +
        '$1,000 (§ 11-321(A)), but whether that permit carries a building ' +
        'code — plan review and inspections — is the county\'s choice ' +
        'under § 11-861(A), and in Greenlee County it carries none.',
    ],
  },
  {
    code: 'ny',
    state: 'New York',
    guideSlug: 'new-york',
    verified: true,
    verifiedDate: 'September 2026',
    separations: {
      // New York State outside New York City, which keeps its own codes
      // (Executive Law § 383(1)(c)). Two Health Department tables, read
      // from both sides. 10 NYCRR Appendix 75-A Table 2 (§ 75-A.4(b),
      // effective 16 March 2016) measures from each wastewater component —
      // house sewer, tank, distribution box, absorption field, seepage pit
      // — to a well, surface water, the dwelling and the property line;
      // Appendix 5-B Table 1 (effective 23 November 2005) measures from
      // the well. They agree at the boundary — 50 ft to a tank, 100 ft to
      // an absorption field, 150 ft to a seepage pit, 200 ft where the
      // field drains toward the well — and the absorption-field row
      // governs a conventional system, so it leads and the tank rides in
      // notes. Both appendices are inside the Uniform Code by reference
      // ([NY] P2602.1.2 for 75-A, [NY] P2602.1.1 for 5-B), so the code
      // official enforces them and the county health department, or the
      // DOH district office where the county has no full-service health
      // department, approves; a deviation is a "specific waiver" only
      // that office can grant (DOH Fact Sheet #6).
      wellToSeptic: {
        feet: 50,
        citation: 'App. 75-A Table 2; App. 5-B Table 1',
        note:
          'Septic tank or watertight treatment unit to a well or suction ' +
          'line; Table 1 states the same 50 ft from the well side ("Septic ' +
          'tank, aerobic unit, watertight effluent line to distribution ' +
          'box"). The absorption field needs 100 ft — that larger circle ' +
          'usually controls the layout. Every well distance in both tables ' +
          'grows by 50% where aquifer water enters the well less than ' +
          '50 ft below grade (Table 2 note g), so 75 ft for a shallow well.',
      },
      wellToDrainfield: {
        feet: 100,
        citation: 'App. 75-A Table 2; App. 5-B Table 1',
        note:
          'Absorption field to a well or suction line, and the well rule ' +
          'states the same 100 ft from its side ("Absorption field or ' +
          'bed"). It becomes 150 ft for a shallow well (aquifer water ' +
          'entering less than 50 ft below grade, note g) and 200 ft where ' +
          'the system sits upgrade and in the direct path of surface-water ' +
          'drainage to the well (note a) — sketch to the larger figure ' +
          'until the well depth and the drainage direction are known. A ' +
          'seepage pit needs 150 ft; a raised, mound, or sand-filter ' +
          'system the same 100 ft. Where the system involves fill, measure ' +
          'from the toe of the fill slope (note c).',
      },
      wellToPropertyLine: unknown(
        'App. 5-B Table 1 has no property-line row and no dwelling row — ' +
          'a verified absence. The well is placed by contamination ' +
          'sources, not lot lines: "A well shall be located upgradient of ' +
          'any potential or known source of contamination unless property ' +
          'boundaries, site topography, location of structures and ' +
          'accessibility require a different location" (§ 5-B.2(c)). On ' +
          'Long Island the Nassau and Suffolk sanitary codes govern house ' +
          'wells and were not read for this entry.'
      ),
      septicToPropertyLine: {
        feet: 10,
        citation: 'App. 75-A Table 2',
        note:
          'Absorption field, septic tank, distribution box, house sewer ' +
          'and seepage pit alike — every row of Table 2 is 10 ft to the ' +
          'property line. Measured from the edge of the 50% reserve area ' +
          'too (note d), and from the toe of the fill slope on a raised ' +
          'or mound system (note c).',
      },
      septicToBuilding: {
        feet: 20,
        citation: 'App. 75-A Table 2',
        note:
          'Absorption field to the dwelling; the distribution box, seepage ' +
          'pit, and raised or mound system need the same 20 ft. The septic ' +
          'tank and the effluent line to the distribution box need 10 ft, ' +
          'the house sewer 3 ft. Measured from the edge of the reserve ' +
          'area as well (note d).',
      },
      septicToSurfaceWater: {
        feet: 100,
        citation: 'App. 75-A Table 2',
        note:
          'Absorption field to a stream, lake or watercourse, measured to ' +
          'the mean high water mark (note b), or to a wetland — wetlands ' +
          'count as surface water here. The distribution box, seepage pit, ' +
          'and raised or mound system need the same 100 ft; the septic ' +
          'tank and effluent line 50 ft; the house sewer 25 ft. A sand ' +
          'filter built watertight may close to 50 ft (note f).',
      },
      wellToSurfaceWater: {
        feet: 25,
        citation: 'App. 5-B Table 1',
        note:
          'Well to a stream, lake, watercourse, drainage ditch, or ' +
          'wetland, from the well side; 37.5 ft for a shallow well (the ' +
          '50% increase where aquifer water enters less than 50 ft below ' +
          'grade). The well may not sit "in a direct line of flow" from ' +
          'any listed contaminant source, "nor in any contaminant plume."',
      },
    },
    extraSeparations: [
      {
        label: 'Absorption field to a well when the system is upgrade and in the direct path of surface-water drainage to the well (Table 1 states the same 200 ft from the well side, and for a field in coarse gravel)',
        feet: 200,
        citation: 'App. 75-A Table 2 note a; App. 5-B Table 1',
      },
      {
        label: 'Absorption field to a well where aquifer water enters the well less than 50 ft below grade — every well distance in both tables grows 50%',
        feet: 150,
        citation: 'App. 75-A Table 2 note g; App. 5-B Table 1',
      },
      {
        label: 'Seepage pit to a well or suction line (Table 1 states the same 150 ft from the well side)',
        feet: 150,
        citation: 'App. 75-A Table 2; App. 5-B Table 1',
      },
      {
        label: 'Distribution box to a well or suction line, and to surface water (20 ft to the dwelling, 10 ft to the property line)',
        feet: 100,
        citation: 'App. 75-A Table 2',
      },
      {
        label: 'House sewer with watertight joints to a well (25 ft if cast iron; 25 ft to surface water, 3 ft to the dwelling, 10 ft to the property line)',
        feet: 50,
        citation: 'App. 75-A Table 2',
      },
      {
        label: 'Closest part of the wastewater treatment system to any water service line',
        feet: 10,
        citation: 'App. 75-A Table 2 note e',
      },
      {
        label: 'Well to a cesspool, or to land application or pile storage of manure, septage, or municipal sludge',
        feet: 200,
        citation: 'App. 5-B Table 1',
      },
      {
        label: 'Well to a fertilizer or pesticide mixing area, a seepage pit, or a single-walled underground chemical or petroleum tank (300 ft to an unprotected salt or chemical storage site or a landfill)',
        feet: 150,
        citation: 'App. 5-B Table 1',
      },
      {
        label: 'Well to non-watertight septic components, an unlined sand filter, a privy pit, stormwater recharge from paved areas, a cemetery, or a barnyard, silo, or animal pen — and to "all known sources of contamination not shown"',
        feet: 100,
        citation: 'App. 5-B Table 1',
      },
      {
        label: 'Well to a sanitary or combined sewer, a watertight privy vault, or a clear-water recharge basin',
        feet: 50,
        citation: 'App. 5-B Table 1',
      },
      {
        label: 'Separate subsurface discharge for water-softener backwash, to wells or watercourses (backwash goes into the septic system only where such a discharge is unavailable)',
        feet: 250,
        citation: 'App. 75-A § 75-A.3(a)',
      },
      {
        label: 'Vertical: useable soil above rock, unsuitable soil, and high seasonal groundwater for a conventional absorption field',
        feet: 4,
        citation: 'App. 75-A § 75-A.4(a)(2)',
      },
      {
        label: 'Vertical: highest groundwater level below the proposed trench bottom (at least one test hole 6 ft deep)',
        feet: 2,
        citation: 'App. 75-A § 75-A.4(c)(2)',
      },
    ],
    setbacksNote:
      'This entry is New York State outside New York City, which keeps its ' +
      'own construction codes (Executive Law § 383(1)(c)). Every number ' +
      'above is the Health Department standard the code official enforces ' +
      'through the Uniform Code ([NY] P2602.1.1, P2602.1.2), and the ' +
      'county health department — or the DOH district office where the ' +
      'county has no full-service health department — is the approver: ' +
      '"specific waivers" from the standards "can only be granted by the ' +
      'local health department" (DOH Fact Sheet #6), a local well-driller ' +
      'law stands if it is "at least as comprehensive" (ECL § 15-1525(6)), ' +
      'and on Long Island the Nassau and Suffolk sanitary codes govern ' +
      'house wells and no Long Island sanitary-code number was read for ' +
      'this entry — get the county\'s own sheet before you sketch. Sketch ' +
      'the reserve area: "An additional useable area of 50 percent shall ' +
      'be set aside for future expansion or replacement whenever ' +
      'possible" (§ 75-A.4(a)(5)), and every Table 2 distance is measured ' +
      'from its edge as well (note d). Two regional overlays add setbacks ' +
      'the state table does not, and apply only inside their boundary. ' +
      'Inside the Adirondack Park, Executive Law § 806 keeps every on-site ' +
      'sewage drainage field or seepage pit 100 ft from the mean ' +
      'high-water mark in all land use areas, and the principal building ' +
      '50 ft (hamlet, moderate intensity), 75 ft (low intensity, rural ' +
      'use), or 100 ft (resource management) back from it; a single-family ' +
      'dwelling in a Resource Management area, or close to forest preserve ' +
      'or a state or federal highway, is a class B regional project that ' +
      'may need an Agency permit before undertaking (§§ 809(2)(a), 810(2)). ' +
      'Inside the New York City watershed (10 NYCRR Part 128 — the parcel ' +
      'test is DEP\'s watershed map, not the county) the septic plans need ' +
      'NYC DEP approval and no part of a new absorption field may lie ' +
      'within 100 ft of a watercourse or wetland or 300 ft of a reservoir, ' +
      'reservoir stem, or controlled lake (§ 128-3.8(a)(1), (5)). Building ' +
      'setbacks from lot lines are zoning, which the Uniform Code leaves to ' +
      'each city, town, and village (Executive Law § 379(3)) — no ' +
      'statewide value. Frost depth, wind speed, and ground snow load are ' +
      'the authority having jurisdiction\'s to fill in on Table R301.2 ' +
      '([NY] R301.2 notes b, d, o); no state frost table exists, and the ' +
      'snow load is the parcel\'s, the larger of Figures R301.2(3) and ' +
      'R301.2(4) plus 2 psf for every 100 ft of elevation above 1,000 ft, ' +
      'with anything over 70 psf pushed to engineered design ' +
      '([NY] R301.2.3; Figure R301.2(4) Note 1). Where the Department of ' +
      'State is the enforcing agency you supply those criteria yourself, ' +
      'and if the town never set them a licensed architect or engineer ' +
      'establishes them (19 NYCRR § 1202.12). Get all of it from your ' +
      'code enforcement official in writing.',
    ownerDrawnAccepted:
      'The septic drawing is not yours to file: plans "shall be prepared ' +
      'directly by or under the supervision of a design professional" ' +
      '(10 NYCRR § 75.5(b)), so draft here, then hand it over. The ' +
      'building-permit site plan has a statewide floor, and it starts with ' +
      'a surveyor: 19 NYCRR § 1203.3(a)(3) requires "a site plan, drawn to ' +
      'scale and drawn in accordance with an accurate boundary survey," so ' +
      'a sketch from the deed alone does not meet the rule. Whether the ' +
      'house plans themselves need a stamp is the 1,500 sq ft line: a ' +
      'residence of more than 1,500 sq ft gross, not counting garage, ' +
      'carport, porches, cellar, or uninhabitable basement or attic, needs ' +
      'an architect\'s or engineer\'s seal statewide (Education Law ' +
      '§§ 7307(5), 7209(7)(b)); at or under it the state does not require ' +
      'one, but the local code enforcement program may ([NY] R106.6). The ' +
      'well plan is the driller\'s: only a DEC-registered driller may ' +
      'install a private well ([NY] P2602.1.1), and the driller files the ' +
      'completion report with DEC and "shall provide a copy … to the water ' +
      'well owner" (ECL § 15-1525(3)).',
    mustShow: [
      'The size and location of new construction and existing structures and appurtenances on the site, drawn to scale in accordance with an accurate boundary survey (19 NYCRR § 1203.3(a)(3))',
      'Distances from lot lines (19 NYCRR § 1203.3(a)(3))',
      'The established street grades and the proposed finished grades (19 NYCRR § 1203.3(a)(3))',
      'As applicable, flood hazard areas, floodways, and design flood elevations (19 NYCRR § 1203.3(a)(3))',
      'On the application, the tax map number and street address (19 NYCRR § 1203.3(a)(2))',
    ],
    negativeFindings: [
      'You may NOT drill your own well: "Individual water supplies (private ' +
        'wells) shall be installed by a well driller registered with the ' +
        'Department of Environmental Conservation" ([NY] P2602.1.1). The ' +
        'Environmental Conservation Law itself reaches only "the business ' +
        'of water well drilling" (ECL § 15-1525(1)), which is why some ' +
        'guides say an owner may drill; the Uniform Code closes that door ' +
        'for a house. The driller\'s on-site supervisor must have passed ' +
        'the NGWA exam (§ 15-1525(5)), and on Long Island a DEC well ' +
        'permit under ECL § 15-1527 is needed only above 45 gallons a ' +
        'minute — ordinary house wells sit below it. You may NOT design ' +
        'your own septic system: plans "shall be prepared directly by or ' +
        'under the supervision of a design professional" (10 NYCRR ' +
        '§ 75.5(b)). Installing a conventional system is not restricted by ' +
        'the state rule, but an alternative system needs the health ' +
        'department\'s prior approval, a design professional supervising ' +
        'construction, and a post-construction certification (§ 75.5(c)).',
      'Design flow is "a minimum daily flow of 110 gallons per day per ' +
        'bedroom" for new construction (§ 75-A.3(b), Table 1) — 330 gpd ' +
        'for three bedrooms. The tank is 1,000 gal for one to three ' +
        'bedrooms, 1,250 for four, 1,500 for five, 1,750 for six, then ' +
        '250 gal and seven square feet of liquid surface for each ' +
        'additional bedroom; "A garbage grinder shall be considered ' +
        'equivalent to an additional bedroom," and so shall an expansion ' +
        'attic (§ 75-A.6(a)(1), Table 3). Set aside a 50% reserve area ' +
        '"whenever possible" (§ 75-A.4(a)(5)).',
      'Site disqualifiers (§ 75-A.4(a)): "Areas lower than the 10 year ' +
        'flood level are unacceptable for on-site systems. Slopes greater ' +
        'than 15% are also unacceptable"; a conventional absorption field ' +
        'needs "at least four feet of useable soil available above rock, ' +
        'unsuitable soil, and high seasonal groundwater"; and soils ' +
        'percolating faster than one minute per inch "are not suitable" ' +
        'unless the site is modified by blending. The highest groundwater ' +
        'level must be at least two feet below the proposed trench ' +
        'bottom, from at least one test hole six feet deep ' +
        '(§ 75-A.4(c)(2)).',
      'App. 5-B Table 1 carries no well-to-property-line and no ' +
        'well-to-dwelling distance — verified absences, not gaps. The well ' +
        'is placed by contamination sources and the rule that it be ' +
        'upgradient of them (§ 5-B.2(c)). Wetlands count as surface water ' +
        'in both tables.',
      'None of the above is a building setback or a design-criteria ' +
        'value. Lot-line setbacks are local zoning (Executive Law ' +
        '§ 379(3)); frost depth and ground snow load are filled in by the ' +
        'authority having jurisdiction on Table R301.2, and any inch or ' +
        'psf figure quoted for a county is a local custom, not a state ' +
        'rule.',
    ],
  },
];

const VERIFIED_BY_CODE = new Map(VERIFIED_STATES.map((s) => [s.code, s]));

/**
 * All 50 states. Those with shipped kits carry verified data; the rest are
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
