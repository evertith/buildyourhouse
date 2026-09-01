# Site Plan Studio — design & architecture spec

**Status:** proposal, for team-lead review before any code is written.
**Sheet series:** SP-01 (new series alongside TO-\* takeoffs and W-\* worksheets).
**Depends on:** `src/lib/siteplan/rules.ts` (owned by another agent — contract assumed in §9).

A free, client-side plot-plan editor. The owner-builder enters lot dimensions, places
a house, well, septic tank, drainfield and driveway, sees live distances to everything
that matters, and prints a to-scale letter-size plot plan they can actually hand to a
rural building department.

---

## 1. Route, page composition, and what it targets

### 1.1 Route: `/site-plan-studio` (top-level)

Recommended over `/calculators/site-plan-studio`, for one decisive reason and two supporting ones:

- **The growth path is child pages.** v2 wants `/site-plan-studio/alaska` etc. ("site plan
  requirements Alaska", "Alaska septic setback distances") — 50 pages that inherit the tool's
  relevance. Under the calculators cluster those become `/calculators/site-plan-studio/alaska`,
  which is three levels deep and semantically wrong.
- It is not a calculator. The cluster's promise is "enter numbers, get quantities". A drawing
  tool sitting in that index dilutes both.
- `/financing` set the precedent: a tool that is its own destination gets its own top-level route.

**The SEO cost of a fresh top-level path is real** (the site is authority-limited — 47/139
indexed as of the last check), so pay it down with internal links rather than URL nesting:

| Where | Link |
| --- | --- |
| `/calculators` hub | new third section, "Drawing sheets", one row: SP-01 |
| `/resources` | tools list |
| Footer "Resources" column | new row beside Calculators / Templates |
| Every state guide | in the permit-application / septic section |
| Every kit product page | "the kit lists your state's site-plan requirements; draw the plan here" |
| `/permitting` | in the application-package section |

**No new nav item.** The nav is at 10 items and Financing landed there recently; an 11th
breaks the header at the tablet breakpoint and pushes the Shop CTA around. Site Plan Studio
reaches users through the calculators hub and the state guides, which is where the intent is.

Register in `src/app/sitemap.ts` at priority 0.8, `changeFrequency: 'monthly'`.

### 1.2 Query set

Primary: **"site plan for building permit"** — informational with tool intent, and the page
is the answer rather than an article about the answer.

| Slot | Text |
| --- | --- |
| `<title>` | `Site Plan Studio — Draw a Site Plan for Your Building Permit` |
| H1 | **Draw a Site Plan for Your Building Permit** |
| Eyebrow | `SP-01 · Site Plan Studio` |
| Description | `Draw your lot, house, well, septic and driveway to scale, check the separations your state requires, and print a letter-size plot plan for your permit application. Free, no signup.` |

The tool name goes in the eyebrow and the H1 carries the query — exactly the `FinancingHero`
pattern (`FIN-01 · Financing` / "Construction Loans for Owner-Builders"). Naming the H1
"Site Plan Studio" would spend the site's strongest heading on a brand term nobody searches.

Secondary queries, each owned by an H2 in the content band: *how to draw a site plan for a
permit* · *plot plan template* · *what to include on a site plan* · *site plan vs plot plan*.

### 1.3 Page composition

```
  ┌─ bp-band + bp-grid hero ─────────────────────────────┐
  │ SP-01 · SITE PLAN STUDIO                             │
  │ Draw a Site Plan for Your Building Permit            │
  │ lead paragraph                                       │
  │ [Lot ▸ 4-cell dimstrip: Cost Free / Signup None /    │
  │  Output Print-ready / Scale To scale]                │
  └──────────────────────────────────────────────────────┘
    THE EDITOR                      ← the whole point, above the fold on desktop
    ─ How jurisdictions treat owner-drawn plans   (H2 ×4, SEO body)
    ─ What a building department looks for        (10-item checklist)
    ─ When you need a surveyor instead            (5 triggers)
    ─ FAQ (7 items → FAQPage schema)
    ─ Kit cross-link band (state kits, $34) + BinderCTA
```

The editor sits immediately under the hero. Do not lead with prose — the tool is the
differentiator and burying it below 800 words of copy is the standard mistake.

---

## 2. Editor: SVG, and why

**SVG, not `<canvas>`.**

- The export must be vector — a plot plan printed from a rasterised canvas looks like a fax,
  and this sheet has to sit beside the $97 binder's pages without embarrassment.
- Hit-testing is free: pointer events land on the shape's DOM node. No manual geometry for
  picking, only for measuring.
- The Blueprint language *is* line work — hairline strokes, hatches, dimension ticks. That is
  SVG's native vocabulary and it inherits the CSS custom properties directly.
- Real DOM nodes take `role`, `aria-label` and `tabIndex`, so keyboard and screen-reader
  support is achievable rather than aspirational.
- Zero dependencies.

Canvas wins at thousands of primitives or freehand drawing. This scene has fewer than thirty
shapes. There is no case for it.

### 2.1 Desktop layout (≥1024px)

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│ SP-01 · SITE PLAN         State [Alaska ▾]  ⚠ 1     [Reset]  [Preview sheet ▸]  │  toolbar 56px
├────────────────┬──────────────────────────────────────────────┬─────────────────┤
│  TOOLBOX       │              CANVAS  (SVG, fit-to-lot)       │   INSPECTOR     │
│  208px         │                    1fr                       │   304px         │
│                │                                              │                 │
│ PLACE          │   ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐    │ HOUSE           │
│  ▭ House       │   │        ├──── 150'-0" ────┤          │    │ ─────────────── │
│  ⊕ Well        │   │   ┌ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┐     │    │ Width   40   ft │
│  ▤ Septic tank │   │   │ setback 25'                │     │    │ Depth   28   ft │
│  ▨ Drainfield  │   │   │    ┌──────────┐            │     │    │ Rotate  0    °  │
│  ═ Driveway    │   │ │ │    │  HOUSE   │      ⊕     │ │   │    │  [0] [90] [180] │
│  ▭ Structure   │   │ │ │    │  40×28   │     WELL   │ │   │    │                 │
│                │  200'│    └──────────┘            │ │   │    │ DISTANCES       │
│ ─────────────  │   │ │ │  ▨▨▨▨▨▨▨                  │ │   │    │ North line  35' │
│ LOT            │   │ │ │  drainfield               │ │   │    │ West line   22' │
│ 150 × 200 ft   │   │   └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘     │    │ Well        62' │
│ [Edit lot]     │   │                                     │    │ Drainfield  78' │
│                │   └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘    │                 │
│ SETBACKS       │                                              │ ⚠ CONFLICTS  1  │
│ Front 25 ft    │        ⊖ ──────●────── ⊕   fit  100%         │ ─────────────── │
│ Side  10 ft    │                                              │ Well → drain-   │
│ Rear  15 ft    │                                              │ field is 78 ft, │
│                │                                              │ needs 100 ft.   │
│ NORTH   ↑ 0°   │                                              │ 18 AAC 72.020   │
│ [dial] [ 0  °] │                                              │ ✓ VERIFIED      │
└────────────────┴──────────────────────────────────────────────┴─────────────────┘
```

Grid: `208px minmax(0,1fr) 304px`. The `minmax(0,…)` on the middle track is load-bearing —
without it the SVG's intrinsic width pushes the grid wider than the viewport.

### 2.2 Input flow

1. **Empty state is the lot form.** Nothing can be placed without a lot, so the canvas area
   renders two number fields (width × depth, feet) plus the state selector and a
   "Start drawing" button. One decision, no empty toolbox to puzzle over.
2. **Lot renders**, fit to the viewport, with a dimension line on the north and west edges and
   dashed setback lines if setbacks have been entered.
3. **Toolbox unlocks.** Clicking an element *drops it immediately* at a free position
   (centre-biased, offset from anything already placed) rather than arming a click-to-place
   cursor. Fewer modes, nothing to explain, and it works from the keyboard.
4. **Drag to position.** Snap to 1 ft. Hold <kbd>Alt</kbd> for free placement. Arrow keys nudge
   the selected element 1 ft, <kbd>Shift</kbd>+arrow 10 ft.
5. **Rotate** from the inspector: a numeric field plus `0 / 90 / 180 / 270` buttons, and a
   drag handle at the shape's top-right. Numeric first — on a permit drawing people want a
   right angle, not a feeling.

Default sizes on drop (`defaults.ts`): house 40×28 ft, structure 24×24, septic tank 8×5,
drainfield 60×20, driveway 12 ft wide × to the nearest lot edge, well = point with a 1 ft
symbol radius.

### 2.3 Dimension lines

Rendered in the `bp-dimline` idiom, translated to SVG: 1px stroke in `--hairline-strong`,
45° end ticks (drafting convention, not arrowheads), label in JetBrains Mono 10px sitting on a
`--bg-primary` plate so it stays readable over hatching.

What is shown, and why not everything — twelve elements produce 66 pairs and the drawing
becomes spaghetti:

- **Always:** the selected element's four distances to the property lines.
- **Always, selection-independent:** any pair that a rule governs *and* that measures under
  1.5× the required minimum. Those are the ones about to become a problem.
- **On hover:** hovering a distance row in the inspector highlights its dimension line in
  `--accent-primary`, and vice versa.

Violating dimensions turn `--accent-critical` and append the requirement:
`78'-0" (100' req.)`. In a hedged state (§2.5) the same line is **dashed** and reads
`78'-0" (100' typical)`.

### 2.4 Notation and units

Input: decimal feet (`28.5`). Display: `28'-6"` — feet-and-inches, standard drafting notation,
with inches dropped when the remainder is under an inch (`28'-0"`). One helper,
`formatFeet(n)`, in `geometry.ts`; used identically on screen and on the sheet.

### 2.5 State selector — the trust moment

Three states, three visual treatments. **The tool must never render an unverified number in
the same style as a verified one.**

**Verified state.** Chip: `✓ VERIFIED · AUG 2026` in `--accent-secondary` (sage). Distances
solid. Conflicts are stated as conflicts: *"Well → drainfield is 78 ft, needs 100 ft.
18 AAC 72.020."* Citation shown inline and printed on the sheet.

**Hedged state.** Chip: `† UNVERIFIED · TYPICAL VALUES` in `--accent-warning` (amber), plus a
persistent band above the canvas:

> We have not verified Wyoming's separation distances. The figures below are typical of what
> states require and are here so you can sanity-check your layout — they are **not** Wyoming's
> rule. Confirm with your county health department before you dig.

And the numbers themselves are downgraded, not just the banner: values print in italic with a
superscript dagger, dimension lines are dashed, and **nothing is ever called a violation**.
The heading is "Check these", the verb is "may need", and the requirement column says
"typical", never "required". The margin table on the sheet carries the same dagger and the
same footnote. Banner-only hedging gets ignored the moment someone starts dragging; changing
the mark itself does not.

**No state selected.** The tool draws and measures and flags nothing. Measuring is useful
without any legal claim attached, and this is the honest default before a state is chosen.

`ownerDrawnAccepted` from the rules module surfaces here too, as a one-line note under the
selector: *"Alaska: owner-drawn plans are generally accepted for rural residential permits;
DEC septic approval may require an engineer's drawing."*

### 2.6 Setbacks are the user's, not the state's

Zoning setbacks are county and city, not state, and vary parcel to parcel — the rules module
cannot supply them honestly. So the toolbox asks for front / side / rear (blank by default),
draws them as long-dash lines inset from the lot edges, and flags a building crossing one as
a **user-entered check**, visually distinct from a state rule and captioned *"setback as you
entered it — confirm with your zoning ordinance"*. This is the single most useful thing on a
residential site plan; guessing it would be the fastest way to get someone's permit rejected
with our sheet in their hand.

### 2.7 Scale and zoom

- **Screen:** `viewBox` in world feet, fit to the lot with a 10% margin. Zoom slider
  0.5×–4× plus a `fit` button; pan by dragging empty canvas. A five-acre lot is ~466 ft across,
  where 1 ft is under a pixel — placing a well 10 ft off a line needs magnification.
- **Export:** pick the largest standard engineering scale from
  `1"=10', 20', 30', 40', 50', 60', 100'` that fits the lot inside the drawing window.
  Print it in the title block **and** draw a graphic bar scale, so the sheet survives being
  photocopied at 94%.

---

## 3. The export sheet

### 3.1 Format: print-to-PDF primary, SVG download secondary

**Recommend both, print first.** Print CSS is zero-dependency, gives a true-vector PDF through
the browser's own Save-as-PDF, and the codebase already has the `no-print` convention plus a
global print block. The SVG download is ~30 lines (serialise, Blob, anchor) and worth
including for the user who wants to edit it — but it is not the hand-off format, because
nobody at a rural permit counter opens a `.svg`.

**Do not add jsPDF or svg2pdf.** A dependency to reproduce what <kbd>Cmd</kbd>+<kbd>P</kbd>
already does perfectly is a bad trade on a static-export site.

Portrait, fixed, letter. A 6.0" × 6.4" drawing window fits any lot at some standard scale in
either proportion, and a fixed orientation is one print stylesheet instead of two. Landscape
goes to v2.

### 3.2 Sheet layout

```
┌───────────────────────────────────────────────────────────────┐  8.5" × 11"
│ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ 4pt orange rule (--accent-primary) ▬▬▬▬▬▬▬▬▬▬ │
│                                                               │
│  SITE PLAN                                          ┌───────┐ │
│  Owner-prepared plot plan                           │   N   │ │
│  ───────────────────────────────────────────────────│   ↑   │ │
│                                                     └───────┘ │
│  ┌──────────────────────────────────┐  ┌────────────────────┐ │
│  │                                  │  │ SEPARATIONS        │ │
│  │        DRAWING WINDOW            │  │ ALASKA             │ │
│  │          6.0" × 6.4"             │  ├────────────────────┤ │
│  │                                  │  │ Well → septic tank │ │
│  │   ┌ ─ ─ ─ setback ─ ─ ─ ─ ┐      │  │ req 50'   act 62'  │ │
│  │   │  ┌────────┐           │      │  │ ✓  18 AAC 80.015   │ │
│  │   │  │ HOUSE  │      ⊕    │      │  ├────────────────────┤ │
│  │   │  └────────┘     WELL  │      │  │ Well → drainfield  │ │
│  │   │   ▨▨▨▨▨▨              │      │  │ req 100'  act 78'  │ │
│  │   └ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ┘      │  │ ✗  18 AAC 72.020   │ │
│  │        ├─── 150'-0" ───┤         │  ├────────────────────┤ │
│  └──────────────────────────────────┘  │ Sources verified   │ │
│    0   30   60   90  120  150 ft       │ August 2026        │ │
│    ├────┼────┼────┼────┼────┤          └────────────────────┘ │
│                                                               │
│  LEGEND  ▭ house  ⊕ well  ▤ tank  ▨ drainfield  ═ drive       │
│  ─────────────────────────────────────────────────────────    │
│  ┌───────────────────────────────────┐ ┌────────────────────┐ │
│  │ PROJECT  ________________________ │ │ OWNER-PREPARED     │ │
│  │ OWNER    ________________________ │ │ This plot plan was │ │
│  │ ADDRESS  ________________________ │ │ prepared by the    │ │
│  │ PARCEL   ________________________ │ │ property owner …   │ │
│  ├──────────┬───────────┬────────────┤ │ Not a boundary     │ │
│  │ SCALE    │ DATE      │ SHEET      │ │ survey.            │ │
│  │ 1"=30'   │ 2026-08-31│   SP-01    │ │ build-your-house   │ │
│  └──────────┴───────────┴────────────┘ └────────────────────┘ │
└───────────────────────────────────────────────────────────────┘
```

**Title block write-ins.** PROJECT / OWNER / SITE ADDRESS / PARCEL (APN) print as the typed
value if entered, otherwise as a ruled blank line for a pen — the binder's print-and-fill
convention, and it means the sheet is usable before the user knows their APN.

**North arrow.** User sets north rotation, 0–359°, snapping to 15°, via a dial plus a numeric
field. The drawing stays screen-up and the arrow rotates — which is how a real plan handles a
lot that is not square to north.

**Symbols** (also the on-screen vocabulary, so the legend teaches the editor):
house = heavy solid outline · structure = medium solid · well = circle with cross-hairs ⊕ ·
septic tank = double-line rectangle · drainfield = rectangle with dashed lateral lines ·
driveway = two parallel lines with stipple · setback = long-dash · property line = solid heavy.

**Separation table.** One row per rule that applies to elements *actually placed* — no well on
the plan means no well rules printed. Columns: pair · required · measured · status · citation.
Footer line: `Sources verified August 2026` for a verified state; for a hedged state the whole
table is daggered and the footer reads `† Typical values — Wyoming's requirements were not
verified. Confirm with your county health department.`

### 3.3 Print mechanics

```css
@page { size: letter portrait; margin: 0.5in; }
@media print {
  body > *:not(.sheetRoot) { display: none !important; }
  .sheetRoot { width: 7.5in; height: 10in; }
  * { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
}
```

The on-screen preview renders the identical component at the same aspect inside a modal, so
what is seen is what prints. Above the print button, one line of instruction, because browser
defaults will otherwise stamp a URL across the title block:

> In the print dialogue: set Margins to *Default*, turn *Headers and footers* off, and choose
> Save as PDF.

---

## 4. Component architecture

```
src/app/site-plan-studio/page.tsx          server — metadata, FAQ schema, hero, content, FAQ
src/components/siteplan/
  SitePlanStudio.tsx      'use client' root: reducer, layout, hydration, analytics guards
  LotForm.tsx             empty state: width × depth + state selector
  Toolbox.tsx             palette, lot summary, setback inputs, north dial
  PlanCanvas.tsx          the SVG scene, viewBox/zoom/pan, pointer handling
  ElementShape.tsx        one element: symbol, selection chrome, rotate handle
  DimensionLine.tsx       SVG dim line — ticks, label plate, violation/hedged styling
  Inspector.tsx           selected element fields + distance list
  ConflictList.tsx        violation rows: measured, required, citation, verification chip
  StateSelect.tsx         picker + verified/hedged banner + ownerDrawn note
  ExportSheet.tsx         the letter sheet (preview + print target)
  TitleBlock.tsx          write-in fields, scale/date/sheet cells, north arrow
  SheetCapture.tsx        email hook (§6)
src/lib/siteplan/
  types.ts                ElementKind, PlanElement, Plan, Violation
  geometry.ts             corners(), polyDistance(), distanceToLotEdges(), formatFeet()
  check.ts                Plan × rules → Violation[]
  scale.ts                engineering-scale picker, bar-scale ticks
  storage.ts              versioned localStorage load/save
  defaults.ts             per-kind default dimensions
  rules.ts                ← other agent
src/styles/
  SitePlanStudio.module.css
  ExportSheet.module.css
```

### 4.1 State: `useReducer`, no library

The whole plan is one small object and the mutations are about ten named actions
(`SET_LOT`, `ADD_ELEMENT`, `MOVE_ELEMENT`, `RESIZE_ELEMENT`, `ROTATE_ELEMENT`, `SELECT`,
`DELETE_ELEMENT`, `SET_STATE`, `SET_SETBACKS`, `SET_NORTH`, `SET_TITLE_FIELD`, `HYDRATE`,
`RESET`). Adding zustand for one page contradicts a codebase with no state library.

**Violations are derived, never stored:**
`const violations = useMemo(() => check(plan, rulesFor(plan.stateCode)), [plan])`.
Storing them creates two sources of truth that drift the first time a drag is interrupted.

### 4.2 Dragging

Pointer handlers on the SVG **root**, not per shape. `onPointerDown` on a shape records the
element id and the grab offset in world coordinates; `onPointerMove` on the root converts
client coords to world coords and dispatches `MOVE_ELEMENT`; `setPointerCapture` keeps the
drag alive when the cursor leaves the shape. One handler set, and mouse, pen and touch behave
identically for free.

### 4.3 Geometry (`geometry.ts`) — the one fiddly file

Rectangles rotate, so element-to-element distance is minimum distance between two convex
polygons:

- `corners(el)` → four points after rotation about the centre.
- `polyDistance(a, b)` → `0` when they overlap (separating-axis test), otherwise the minimum
  over every point-to-segment pair.
- The well is a point: `polyDistance(point, poly) − symbolRadius`.
- `distanceToLotEdges(el, lot)` → four numbers, minimum over corners per edge; **negative
  means the element crosses the property line**, which is its own warning ("outside the
  property line") and outranks every separation conflict in the list.

About 120 lines, and it earns a small unit test — a rotated rectangle's corner distance is
exactly the kind of thing that silently ships wrong.

### 4.4 Persistence

`localStorage['byh.siteplan.v1']`, debounced 400 ms, version-keyed so a schema change is
discarded rather than crashing on parse. **Hydrate in `useEffect`, never during render** — the
page is statically exported and the first paint must match the server output. On restore, show
one line: *"Restored the plan you were drawing · Start over"*.

### 4.5 v1 scope / v2 backlog

**v1:** rectangular lot · house, well, septic tank, drainfield, driveway, generic structure ·
drag, rotate, numeric edit, delete · user-entered setbacks · live dimensions · state
separation checks with verified/hedged treatment · export sheet (print + SVG download) ·
localStorage · email hook · analytics.

**v2:** polygon and irregular lots · easements and rights-of-way · contours, slope, drainage
arrows · multiple buildings with per-building setbacks · existing vs proposed distinction ·
utility runs · well protection-radius circles · landscape sheet · PNG export ·
`/site-plan-studio/[state]` landing pages · parcel import from county GIS.

---

## 5. Mobile (390px)

**Recommendation: numeric editing, not read-only, and not drag.**

- Below 1024px the three-column grid collapses to a single column: canvas, then inspector,
  then toolbox.
- Below 768px, **dragging is disabled** and the inspector's numeric fields become the editing
  surface. Position is edited as "distance from west line / distance from north line" number
  inputs — which is how a surveyor would enter it anyway.
- The lot form, state selector, conflict list, sheet preview and print all work fully.
- One line above the canvas: *"Drawing is easier on a larger screen — your plan is saved on
  this device."*

Why not full drag on a phone: a 466 ft lot at 390px is under one pixel per foot. Precise
placement is not achievable, and shipping a drag that feels bad is worse than not shipping
one. Why not read-only: a page ranking for a query that half its traffic reads on a phone
cannot answer with "come back on a laptop" and expect anything but a bounce.

**No horizontal overflow at 390 — the hard requirement.** Mechanics:

- The SVG carries `width: 100%` and no fixed width; `viewBox` does all scaling, so it can
  never overflow.
- The **sheet preview is the one risk** — it is 7.5in wide by definition. Wrap it in a
  dedicated `overflow-x: auto` container so it scrolls inside itself; the body never scrolls
  sideways.
- Toolbar chips and the toolbox palette wrap rather than scroll.
- The separations table on screen gets `overflow-x: auto` on its own wrapper.
- Sweep at 390 and 1280 before merge.

---

## 6. Email capture

**Placement:** below the sheet preview and *after* the print button — the value-delivered-first
position `EstimateCapture` uses inside `CalcSheet`. It never gates the print, and never gates
the SVG download.

**v1 implementation:** `POST {WORKER_BASE}/subscribe` with
`{ email, source: '/site-plan-studio', website: honeypot }`. That endpoint exists, is
idempotent, and sends the standard welcome. Zero worker work.

**Copy — and a caution.** The state site-plan checklist PDF does not exist yet, so the button
must not promise it as a delivery. Honest framing at launch:

> **Get the site-plan checklist for your state**
> We're building a one-page checklist per state — what your department wants on the sheet, and
> who to ring. You'll get yours the day it's ready, plus the owner-builder newsletter.
> Unsubscribe in one click.

**Better v1.1, and cheap:** add a `/siteplan` route to the newsletter worker modelled exactly
on `/estimate` — it emails the user their measured distances, their conflict list and the
citations as text, immediately. That is a real deliverable today, needs no new artifact, and
it converts far better than a promise. Recommend shipping `/subscribe` on day one and the
`/siteplan` route as a fast follow.

Fire `generate_lead` with `{ method: 'siteplan_capture' }` only on confirmed success, matching
`EstimateCapture`.

---

## 7. Analytics

`trackEvent` from `src/lib/analytics.ts`. Names stay snake_case and namespaced `siteplan_*`;
`generate_lead` is reused so existing lead reporting keeps working.

| Event | Params | When |
| --- | --- | --- |
| `siteplan_start` | `lot_w`, `lot_d`, `state` | lot submitted — once per session |
| `siteplan_state_select` | `state`, `verified` | state chosen |
| `siteplan_element_add` | `kind` | each element placed |
| `siteplan_violation_shown` | `rule`, `state`, `verified` | **once per rule id per session** |
| `siteplan_export` | `method` (`print`\|`svg`), `state`, `elements`, `conflicts` | export |
| `siteplan_restore` | `elements` | hydrated from localStorage |
| `generate_lead` | `method: 'siteplan_capture'` | capture succeeds |

Two things matter here:

- **`siteplan_violation_shown` must be guarded by a `useRef` set of already-fired rule ids**,
  the way `CalcSheet` guards `calculator_use`. Unguarded, a single drag emits hundreds of
  events and the GA4 property is ruined for the month.
- **`siteplan_state_select` is the most valuable datum on the page.** It ranks demand for
  states by name, which tells you which entries in `rules.ts` to verify next and — more
  usefully — which permit kits to build next. Mark `siteplan_export` as a GA4 key event.

---

## 8. Risk and liability copy

Three tiers, all in the kits' `verifyNote` voice: name the mechanism, name who decides, and
point at the printed source rather than asking to be believed.

**(a) In the editor, under the state selector, always visible:**

> Distances are measured from what you draw. Whether your department accepts an owner-drawn
> plan — and what it must show — is decided at the counter, not here.

**(b) On the export sheet, the disclaimer block:**

> **Owner-prepared.** This plot plan was prepared by the property owner using a free drawing
> tool — not by a licensed surveyor or engineer. Dimensions are as entered by the owner and
> have not been field-verified against a recorded survey. Separation distances are checked
> against [State] requirements as published by [authority], [date]. Requirements change, and
> the office reviewing this application decides what applies to this parcel.
> **This is not a boundary survey.**

**(c) In the page content, the fuller statement:**

> This tool draws a plan and measures it. It does not survey your land, and it does not tell
> you your permit will be approved. The separations it checks are the ones states publish for
> wells, septic tanks and drainfields; setbacks are set by your county or city zoning
> ordinance and vary parcel to parcel, so the tool asks you for them rather than guessing.
> Every rule it checks prints its citation on the sheet, so you can hand a reviewer the source
> rather than our word for it.

For a hedged state, (b) swaps to: *"Separation distances shown are typical values. [State]'s
requirements were not verified for this tool. Confirm every distance with [authority] before
construction."* — and the table daggers stay.

---

## 9. Contract assumed of `rules.ts`

Coded against this shape. If the data agent's module differs, only `check.ts` and
`StateSelect.tsx` adapt — nothing else touches it.

```ts
export type ElementKind =
  | 'house' | 'well' | 'septicTank' | 'drainfield' | 'driveway' | 'structure';

export interface SeparationRule {
  id: string;              // 'well-drainfield'
  from: ElementKind;
  to: ElementKind | 'propertyLine';
  minFeet: number;
  label: string;           // 'Well to drainfield'
  citation: string;        // '18 AAC 72.020(a)'
  sourceUrl?: string;
}

export interface StateSiteplanRules {
  code: string;            // 'ak'
  state: string;           // 'Alaska'
  verified: boolean;
  verifiedDate?: string;   // 'August 2026'
  authority: string;       // 'Alaska DEC, Division of Water'
  ownerDrawnAccepted: 'yes' | 'varies' | 'no' | 'unknown';
  ownerDrawnNote: string;
  separations: SeparationRule[];
  notes?: string[];
}

export const SITEPLAN_RULES: Record<string, StateSiteplanRules>;
```

`verified: false` drives every hedged treatment in §2.5 and §3.2. There is no third flag and
no per-rule override — one boolean per state, so the visual downgrade can never be applied
half-way.

---

## 10. Build order

1. `types.ts`, `geometry.ts` (+ test), `defaults.ts` — the maths, in isolation.
2. `SitePlanStudio.tsx` reducer + `LotForm` + `PlanCanvas` rendering a static lot.
3. Element placement, drag, selection, `Inspector` numeric editing.
4. `DimensionLine` + `check.ts` + `ConflictList`.
5. `StateSelect` and the full verified/hedged treatment.
6. `ExportSheet`, `TitleBlock`, `scale.ts`, print CSS.
7. `storage.ts`, `SheetCapture`, analytics.
8. Page shell: hero, content bands, FAQ, schema, sitemap, hub and guide cross-links.
9. 390 / 1280 sweep; print a real sheet on paper and look at it.

---

## 11. Open questions — TEAM LEAD RULINGS (Aug 31 2026)

**Q1 polygon lots: DEFERRED to v2, as recommended.** v1 ships the free-text
irregular-lot note that prints on the sheet ("Lot is irregular; see attached
plat.").

**Q2 capture promise: build the `/siteplan` worker route IN v1** (modeled on
`/estimate` — emails the user their distances, conflicts, and citations
immediately). It's a real deliverable today; the checklist-promise wording is
dropped entirely. Capture copy: "Email me my measurements and citations" +
newsletter opt-in framing.

**Q3 orientation: fixed portrait for v1**, landscape to v2.

**AMENDMENT A — the verified-but-local display state (forced by the corpus
extractions).** The binary verified/hedged treatment misses what the data
actually says: for most verified states the corpus's finding is "no statewide
separation minimum EXISTS — the county health department sets it" (Michigan's
dossier literally instructs 'print none'; CO/KY/GA/MS/VA similar). A verified
state with zero binding separations must NOT fall back to daggered typical
values — it renders its own third treatment: chip stays `✓ VERIFIED`, the
rules panel and sheet table show the sourced negative ("Michigan sets no
statewide separation distance; your county health department does — ask in
writing before you site anything. MCL/R-cite.") and nothing is measured
against defaults. Typical-value daggered defaults apply ONLY to unverified
(hedged) states.

**AMENDMENT B — conditional rules never become violation rows.** Several
extracted figures are conditions of narrow provisions, not blanket minimums:
TX's 100 ft field-line-to-property-line is a condition of the 10-acre OSSF
permitting exemption (§ 366.052); WA's 100/200 ft surface/marine-water
figures are owner-self-install eligibility conditions (WAC 246-272A-0250(2)),
not siting rules. These go in `StateSiteplanRules.notes` (printed on the
sheet in the notes area with their precise framing), NEVER in `separations[]`
— only genuinely binding statewide minimums (e.g. Montana's ARM 17.36.323
Table 2 set, Alaska's separations) may drive the conflict engine. Misframing
a conditional figure as a requirement is exactly the error class this site
exists to fix.

**AMENDMENT C — the illustrative citations in §3.2's sheet mock are
placeholders** (the "18 AAC 80.015" example is actually the boiler chapter —
18 AAC 72 is wastewater). Builders must take every citation from `rules.ts`
verbatim and never from this spec.

### (original questions, for the record)

1. **Polygon lots — recommend deferring, and it is the biggest call here.** An editable
   polygon needs vertex handles, insert/delete, self-intersection guards, and mitred setback
   offsetting, which is more work than the rest of the editor combined. Cheap v1 substitute: a
   free-text note field that prints on the sheet — *"Lot is irregular; see attached plat."*
   Anyone with a genuinely irregular parcel already has a plat to staple to the application.
2. **The checklist promise in the capture block.** Either build the per-state checklist first,
   or ship the "you'll get it when it's ready" wording — which is a real commitment to honour.
   The `/siteplan` worker route (§6) sidesteps the question entirely and is the better answer
   if there is appetite for a small worker change.
3. **Sheet orientation.** Fixed portrait keeps it to one stylesheet. If wide rural lots turn
   out to be the norm, landscape moves from v2 to v1 and the print CSS doubles.

---

## 12. V1.5 — polygon lots (shipped)

**Status:** built and verified, September 2026. This section un-defers §11 Q1 at
**reduced scope** and records what was deliberately left out. §11's other rulings and
Amendments A–C are unchanged and still binding.

### 12.1 What shipped

**The lot is a discriminated union.** `Plan.lot` is now
`{ kind: 'rect'; w; d } | { kind: 'poly'; pts: Pt[] }` — world feet, clockwise, first
point not repeated. The rectangle stays the default and the fast path; §11 Q1's original
recommendation was right that the polygon is more work than the rest of the editor, and the
answer was to keep the rectangle's code path intact rather than generalise everything onto
a polygon that most users do not have.

**Two ways in.** A single toggle in the lot form — *"This lot isn't rectangular"* — opens
`LotShapeEditor`, which offers:

- **Click the corners.** Click in sequence, click the first corner to close, then drag any
  corner, insert one at a side's midpoint, or delete one. Snapped to the foot. The world
  window is fixed at a chosen extent rather than fitted to the points as they land: a view
  that refits itself between clicks moves the ground under the cursor.
- **Enter it from your deed.** Bearing and distance per row, walked turtle-style from the
  point of beginning. `bearing.ts` reads quadrant bearings (`N 42°15' E`, `N42-15-30E`,
  `S 7 W`, spelled-out `North 42 East`), azimuths (`azimuth 132.5`, `az 132-30`, bare
  numbers) and cardinals (`due north`). Running closure error is on screen the whole time.

**Closure, and the guard on it.** The closure readout is the thing a surveyor checks first,
so it is never hidden. "Close the gap" moves the last corner onto the point of beginning —
but it is **only offered when the gap is under max(3 ft, 2% of perimeter)**. A deed whose
final "thence to the point of beginning" call was never typed misses closure by the length
of a whole side, and nudging the last corner there would collapse a real corner onto the
start and silently destroy the shape. That case gets an explanation instead.

**Measurement.** `nearestBoundary(el, lot)` is the single entry point for
element-to-property-line distance. On a rectangle it is the v1 named-edge maths untouched,
so every number a rect plan printed before prints identically. On a polygon it sweeps
**both** directions — element vertices against boundary segments and boundary vertices
against element edges — because on a notched parcel the closest approach is routinely the
notch corner facing the middle of a wall, which a one-directional sweep misses by feet.

**Boundary crossing** is three tests, and a notched parcel needs all three: a corner off
the parcel, a boundary corner inside the element, and — the one the tests caught — a notch
narrower than the house slicing in one wall and out the other, where no vertex of either
shape is inside the other. Overshoot depth is sampled on a grid in the element's own frame,
because the deepest overhang of a sliced house is in its middle, not at any corner.

**Drawing.** Every side carries its length in the plat idiom — a mono label along the
segment, outside the boundary, skipped on sides too short to hold one at the current scale
rather than overprinted. The marked road frontage is drawn heavy with an offset dashed
right-of-way line and a `ROAD` caption.

### 12.2 Scope cuts — deliberate, and why

- **No setback offsets.** Setback lines remain rectangle-only. Front, side and rear are
  named against four squared-off edges; a mitered inward offset of an eight-sided boundary
  is a different piece of geometry, and a confidently wrong setback line on a permit sheet
  is worse than none. The toolbox says exactly that in one line and shows nearest-boundary
  distances instead. This upholds the original §11 ruling that mitered polygon offsets stay
  cut.
- **No easements or rights-of-way.** Still v2. The lot note prints on the sheet and is the
  place for one today.
- **No curves.** There are no arcs, chords or radii. A curved call is entered as one or more
  straight **meander segments** — which is also how a creek or a lake edge is carried on a
  plat, so the motivating "21-acre strip whose north boundary is a creek" is expressible
  today at whatever fidelity the owner wants to click.
- **No self-intersection solver.** A crossing boundary warns (*"boundary crosses itself —
  check your corners"*) and still draws. An owner mid-entry has a self-crossing boundary for
  as long as it takes to place the next corner, and refusing to draw it would make the tool
  feel broken exactly when they need to see what they typed.
- **Road frontage is marked, not inferred.** A polygon has no north edge to pick from a
  list, so the owner clicks the side. **Unmarked frontage silences driveway boundary
  crossings entirely** rather than crying wolf on every parcel whose owner has not found the
  control yet.
- **Position editing on a polygon is x/y**, not "distance from the west line" — there is no
  west line. This matters because below 768px the inspector is the only way to move anything
  (§5), so the fields could not simply be dropped.

### 12.3 Storage

`byh.siteplan.v1` → **`byh.siteplan.v2`**, with a real migration rather than the discard a
version bump normally implies: v1 is read once, its `{ w, d }` becomes
`{ kind: 'rect', w, d }`, the plan is rewritten under the new key and the old key removed.
The absent `kind` **is** the version marker, so no separate migration flag can drift from
the data. `clearPlan` removes both keys, or "start over" would resurrect a v1 record that
had never been loaded.

### 12.4 Frozen, still

`rules.ts` was not touched. No citation, distance or note moved. Amendment B still holds:
`extraSeparations` never reaches the conflict engine, on any lot shape.

### 12.5 v2 backlog, revised

Easements and rights-of-way · true curves (arc calls with radius and chord) · mitered
setback offsets for polygons · contours, slope and drainage · multiple buildings with
per-building setbacks · existing vs proposed · utility runs · well protection-radius circles
· landscape sheet · PNG export · `/site-plan-studio/[state]` landing pages · parcel import
from county GIS (which would make hand entry the fallback rather than the primary path).
