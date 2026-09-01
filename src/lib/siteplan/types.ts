/**
 * Site Plan Studio — the plan document.
 *
 * WORLD COORDINATES. Everything in this module is feet, measured from the
 * lot's north-west corner: +x runs east (right), +y runs south (down). That
 * matches SVG's own y-down axis, so nothing has to be flipped between the
 * model and the drawing, and it matches how a plot plan is dimensioned —
 * "35 ft off the north line, 22 ft off the west line".
 *
 * North on the DRAWING is not north on the GROUND: the drawing always stays
 * screen-up and `north` rotates the north arrow instead (§3.2). A lot that
 * sits at 40 degrees to true north is drawn square and the arrow leans.
 */

/**
 * The six placeable elements plus `waterEdge`.
 *
 * `waterEdge` is a two-point line — a pond bank, stream or lake shore. It is
 * here because half the verified separations in the corpus (Alaska's 100 ft
 * under 18 AAC 72.520(b), Montana's under ARM 17.36.323 Table 2) are measured
 * to surface water, and without something to measure to they would be
 * unenforceable text. It is stored as a rectangle of zero depth so that drag,
 * rotate and the distance code all treat it like any other element.
 */
export type ElementKind =
  | 'house'
  | 'structure'
  | 'well'
  | 'septicTank'
  | 'drainfield'
  | 'driveway'
  | 'waterEdge';

export const ELEMENT_KINDS: ElementKind[] = [
  'house',
  'well',
  'septicTank',
  'drainfield',
  'driveway',
  'structure',
  'waterEdge',
];

/** Singular display name, sentence case — used in prose and dimension labels. */
export const KIND_LABEL: Record<ElementKind, string> = {
  house: 'House',
  structure: 'Structure',
  well: 'Well',
  septicTank: 'Septic tank',
  drainfield: 'Drainfield',
  driveway: 'Driveway',
  waterEdge: 'Water edge',
};

/**
 * One placed element.
 *
 * `w` and `d` are the footprint along the element's OWN axes before rotation.
 * A well is a point (w = d = 0); a water edge is a line (d = 0, w = its
 * length). Both fall out of the same rectangle maths — see geometry.ts, which
 * is written to stay exact on degenerate shapes.
 */
export interface PlanElement {
  id: string;
  kind: ElementKind;
  /** Center, feet east of the west property line. */
  x: number;
  /** Center, feet south of the north property line. */
  y: number;
  /** Extent along the element's local x axis, feet. */
  w: number;
  /** Extent along the element's local y axis, feet. 0 for well and waterEdge. */
  d: number;
  /** Rotation about the center, degrees clockwise. */
  rot: number;
}

/** A point in world feet. Lives here so `Lot` can hold one without geometry.ts
    and types.ts importing each other; geometry.ts re-exports it. */
export interface Pt {
  x: number;
  y: number;
}

/** The common case, and still the default path: a rectangle from two numbers. */
export interface RectLot {
  kind: 'rect';
  /** East-west, feet. */
  w: number;
  /** North-south, feet. */
  d: number;
}

/**
 * A boundary as it actually runs (v1.5).
 *
 * `pts` are world feet, CLOCKWISE, and the first point is NOT repeated at the
 * end — the ring closes implicitly. Clockwise is enforced on entry
 * (`ensureClockwise`) so the outward normal used for side labels is the same
 * for a boundary someone clicked and a boundary read off a deed, which may
 * call its courses in either direction.
 *
 * There are no curves. A curved call is entered as one or more straight
 * meander segments, which is also how a creek or a lake edge is carried on a
 * plat — see the V1.5 addendum in the spec.
 */
export interface PolyLot {
  kind: 'poly';
  pts: Pt[];
}

export type Lot = RectLot | PolyLot;

export type EdgeName = 'north' | 'east' | 'south' | 'west';

export const EDGE_LABEL: Record<EdgeName, string> = {
  north: 'North line',
  east: 'East line',
  south: 'South line',
  west: 'West line',
};

/**
 * Zoning setbacks, as the OWNER entered them (§2.6). The rules module cannot
 * supply these honestly — they are county and city, and vary parcel to
 * parcel — so they are asked for, drawn as the user's own check, and never
 * presented as a state requirement.
 */
export interface Setbacks {
  front: number | null;
  side: number | null;
  rear: number | null;
}

/**
 * Which lot edge the street is on. Front/rear/side are meaningless without
 * it, and assuming "front = north" would silently draw a wrong setback on
 * every parcel whose driveway comes in from the south.
 */
export interface TitleFields {
  project: string;
  owner: string;
  address: string;
  parcel: string;
  /** Free-text irregular-lot note; prints on the sheet (§11 Q1 ruling). */
  irregular: string;
}

export const EMPTY_TITLE: TitleFields = {
  project: '',
  owner: '',
  address: '',
  parcel: '',
  irregular: '',
};

export interface Plan {
  lot: Lot | null;
  /** Lowercase postal code, matching StateSiteplanRules.code. '' = none. */
  stateCode: string;
  elements: PlanElement[];
  selectedId: string | null;
  setbacks: Setbacks;
  frontEdge: EdgeName;
  /**
   * Which boundary side the street is on, in POLYGON mode: an index into
   * `lot.pts` naming the segment that runs from `pts[i]` to `pts[i+1]`.
   * `null` means unmarked, and an unmarked frontage is why a driveway
   * crossing the boundary raises nothing in poly mode — the tool cannot tell
   * a legitimate approach from a mistake without being told where the road is.
   */
  frontSegment: number | null;
  /** North arrow bearing, 0–359 degrees clockwise from up. */
  north: number;
  title: TitleFields;
}

export const EMPTY_PLAN: Plan = {
  lot: null,
  stateCode: '',
  elements: [],
  selectedId: null,
  setbacks: { front: null, side: null, rear: null },
  frontEdge: 'north',
  frontSegment: null,
  north: 0,
  title: EMPTY_TITLE,
};

/**
 * How much authority the tool may claim for the selected state (Amendment A).
 * Three treatments, never blended — the whole trust position of the page
 * rests on an unverified number never wearing a verified number's clothes.
 *
 * - `none`     no state chosen. Measure everything, claim nothing.
 * - `rules`    verified state that publishes at least one binding distance.
 * - `local`    verified state whose finding is that NO statewide minimum
 *              exists. Chip stays VERIFIED; the sourced negative is the
 *              content; nothing is measured against a default.
 * - `hedged`   unverified state. Typical values, daggered and italic, dashed
 *              dimension lines, and nothing is ever called a violation.
 */
export type Treatment = 'none' | 'rules' | 'local' | 'hedged';

export type RowStatus =
  /** Measured and clear. */
  | 'ok'
  /** Measured, short of a binding minimum. Only ever in treatment `rules`. */
  | 'violation'
  /** Measured, short of a typical value. The hedged-state equivalent. */
  | 'watch'
  /** The rule applies but the elements it measures are not both placed. */
  | 'unplaced';

/** One row of the separations schedule — on screen and on the sheet. */
export interface MeasureRow {
  /** Stable id: the CoreSeparations key. Also the analytics guard key. */
  id: string;
  label: string;
  requiredFeet: number | null;
  measuredFeet: number | null;
  status: RowStatus;
  citation: string | null;
  note?: string;
  /** True when the requirement is a typical value, not this state's rule. */
  hedged: boolean;
  /** True for pure-geometry dimensions carrying no requirement at all. */
  geometric?: boolean;
  /** Element ids to draw the dimension line between. */
  fromId?: string;
  toId?: string;
  /** Named lot edge the rule measured to. Rectangular lots only. */
  edge?: EdgeName;
  /**
   * The rule measured to the nearest point on a polygon boundary, which has
   * no edge name. `fromId` plus this flag is enough to redraw the dimension.
   */
  boundary?: boolean;
}

/** An element wholly or partly outside the lot. Outranks every separation. */
export interface BoundaryWarning {
  id: string;
  elementId: string;
  label: string;
  /** How far past the line, feet (always positive). */
  overFeet: number;
  /** Null on a polygon lot: the boundary it crossed has no compass name. */
  edge: EdgeName | null;
}

/** A building crossing a setback the OWNER entered. Never a state rule. */
export interface SetbackWarning {
  id: string;
  elementId: string;
  label: string;
  edge: EdgeName;
  requiredFeet: number;
  measuredFeet: number;
}

/** A sourced statement with no number to measure. */
export interface NoteRow {
  id: string;
  label: string;
  text: string;
  citation?: string | null;
  /** Conditional provisions (Amendment B) print with their own framing. */
  conditional?: boolean;
  feet?: number | null;
}

export interface CheckResult {
  treatment: Treatment;
  rows: MeasureRow[];
  boundary: BoundaryWarning[];
  setbacks: SetbackWarning[];
  notes: NoteRow[];
}
