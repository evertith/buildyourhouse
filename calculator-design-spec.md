# Calculator Framework — Design Specification

**Status:** Implementation-ready. Follow verbatim.
**Scope:** Seven calculator pages (`framing-lumber`, `drywall`, `concrete-slab`, `roofing`, `paint`, `flooring`, `insulation`) + redesigned `/calculators` hub.
**Author:** Design pass, August 2026.

---

## 0. Design concept — "The Takeoff Sheet"

A general contractor prices a job by doing a **takeoff**: walking the drawings,
measuring, and writing quantities line by line on a takeoff sheet. That's
exactly what these calculators do for the visitor — so each calculator IS a
takeoff sheet from a drawing set.

Concretely:

- Every calculator page is one **sheet in a drawing set**, numbered like a
  drafting index: `TO-01 FRAMING`, `TO-02 DRYWALL` … The hub is the set's
  **sheet index**.
- The calculator instrument is a bordered **paper sheet laid on the desk**: it
  overlaps the navy hero band the way the shop's product sheets sit on navy,
  casting the same shadow (`.sheet` treatment from shop.module.css).
- Inputs are the **field measurements** (left column). Results are the
  **materials schedule** (right column): mono label, dotted leader, serif
  value — the same `.priceRow` leader language the shop uses for its price.
- The cost range renders as a **dimension line** (ticks + rule), not a chart.
  The component breakdown renders as **hatched takeoff bars** — drafting
  hatching, not chart-library bars.
- The email capture is the sheet's **tear-off stub** — dashed rule, plain
  honest copy.

Everything is built from existing tokens and the existing blueprint
primitives (`bp-band`, `bp-grid`, `bp-eyebrow`, `bp-dimline`,
`bp-mono-label`, `bp-sheet-no`). No new hex values except three derived
rgba/hatch tints documented in §4.4 and §4.5.

**What this is not:** a SaaS widget. No rounded-2xl cards, no gradient
buttons, no chart library, no dark mode. Square corners, hairlines, mono
labels, warm paper. Navy is an accent band, never the default surface.

---

## 1. Page anatomy

### 1.1 Calculator page — desktop (≥900px)

```
┌────────────────────────────────────────────────────────────────────┐
│ NAVY BAND (bp-band bp-grid, crop marks, 5px orange bottom rule)    │
│  ┌ eyebrow: FREE TOOL — mono, orange, trailing hairline ┐          │
│  H1 (serif display): Drywall Calculator                           │
│  Sub (serif italic): Sheets, mud, tape, and screws for your        │
│    square footage — with the math shown.                           │
│  ┌──────────── dimension strip (4 cells) ─────────────────┐        │
│  │ SHEET TO-02 │ OUTPUT: QTYS │ BASIS: 4×8–4×12 │ WASTE 10% │      │
│  └─────────────────────────────────────────────────────────┘      │
└────────────────────────────────────────────────────────────────────┘
        ┌───────────────────────────────────────────────────┐
        │ ▼ THE SHEET (overlaps band by 56px, .sheet shadow) │
        │ ┌───────────────────────────────────────────────┐ │
        │ │ TO-02 · DRYWALL TAKEOFF     [COPY] [PRINT]    │ │  sheet header
        │ ├────────────────────┬──────────────────────────┤ │
        │ │ FIELD MEASUREMENTS │ MATERIALS SCHEDULE       │ │
        │ │  (inputs, 1fr)     │  (results, 1.15fr)       │ │
        │ │  label             │  ┌ hero qty: 89 sheets ┐ │ │
        │ │  [ 1,800 |ft²]     │  schedule lines w/       │ │
        │ │  segmented 4×8 4×12│  dotted leaders          │ │
        │ │  select, stepper   │  cost dimension line     │ │
        │ │                    │  hatched breakdown bars  │ │
        │ │                    │  fine-print disclaimer   │ │
        │ ├────────────────────┴──────────────────────────┤ │
        │ │ ✂ TEAR-OFF: Send this takeoff to your inbox   │ │  capture
        │ └───────────────────────────────────────────────┘ │
        └───────────────────────────────────────────────────┘
│ CONTENT (width-content):                                           │
│   secHead: HOW IT'S FIGURED  · right meta: SHEET TO-02             │
│   methodology prose + formula table                                │
│   secHead: ASSUMPTIONS & WASTE                                     │
│   assumptions leader-table                                         │
│   secHead: QUESTIONS · FAQ rows (shop .faqItem pattern)            │
│   RELATED SHEETS strip (ladder-style row of other calculators)     │
│   CROSS-SELL spec-card (moreCard pattern; binder or kit)           │
└────────────────────────────────────────────────────────────────────┘
```

Input panel and results panel are both **static** (no sticky results on
desktop): both columns fit one viewport for every calculator (≤6 inputs), so
sticking buys nothing and risks overlap bugs. Sticky behavior is a
mobile-only concern (§1.2).

### 1.2 Calculator page — mobile (<900px)

```
┌──────────────────────────┐
│ NAVY BAND (compact)      │
│  eyebrow / H1 / sub      │
│  dimension strip 2×2     │
└──────────────────────────┘
  ┌────────────────────┐
  │ SHEET (overlap 32px)│
  │ header row          │
  │ FIELD MEASUREMENTS  │
  │ (inputs stacked)    │
  │─────────────────────│
  │ MATERIALS SCHEDULE  │
  │ (results stacked)   │
  │─────────────────────│
  │ tear-off capture    │
  └────────────────────┘
  content sections …
┌──────────────────────────┐
│ STICKY BAR (bottom, navy)│  ← visible only while the schedule
│ 89 SHEETS · VIEW TAKEOFF │    is out of the viewport
└──────────────────────────┘
```

### 1.3 Hub page anatomy — `/calculators`

```
┌ NAVY BAND: eyebrow "DRAWING SET · FREE TOOLS", H1 "Owner-Builder
│  Calculators", italic sub, dimension strip (7 SHEETS · NO SIGNUP ·
│  FORMULAS SHOWN · PRINT-READY) ┘
│
│ secHead: TAKEOFF SHEETS · meta "TO-01 — TO-07"
│ index rows (one per calculator):
│   TO-01 | Framing & Lumber Calculator | studs, plates,      | →
│         | one-line desc               | sheathing, headers  |
│ … seven rows, hairline-separated, hover = paper fill + orange inset
│
│ secHead: PLANNING WORKSHEETS · meta "W-01 — W-04"
│ same row treatment for cost-savings, material cost (umbrella),
│ timeline, budget tracker
│
│ EmailCapture (existing footer component appears site-wide; no extra
│ capture on hub) + BinderCTA spec-card at bottom
```

---

## 2. File plan

- `src/styles/CalcSheet.module.css` — every component below (single shared
  module; class names below are its exports).
- `src/styles/CalcHub.module.css` — hub-only styles (§8).
- Global addition to `src/styles/globals.css` (allowed, ~10 lines): print
  rules hiding site chrome (§5.6).

---

## 3. The sheet scaffold

### 3.1 Page wrapper + hero (`calcPage`, `hero`, …)

DOM (JSX shape):

```jsx
<div className={s.calcPage}>
  <section className={`${s.hero} bp-band bp-grid`}>
    <span className={`${s.crop} ${s.tl}`} /><span className={`${s.crop} ${s.tr}`} />
    <div className={s.heroInner}>
      <p className={`bp-eyebrow ${s.eyebrow}`}>Free tool</p>
      <h1 className={s.heroTitle}>Drywall Calculator</h1>
      <p className={s.heroSub}>Sheets, mud, tape, and screws for your square
        footage — with the math shown, not hidden.</p>
      <div className={s.dimstrip}>
        <div className={s.dimcell}><span className={s.k}>Sheet</span><span className={s.v}>TO-02</span></div>
        <div className={s.dimcell}><span className={s.k}>Returns</span><span className={s.v}>Quantities</span></div>
        <div className={s.dimcell}><span className={s.k}>Basis</span><span className={s.v}>4×8–4×12</span></div>
        <div className={s.dimcell}><span className={s.k}>Waste</span><span className={s.v}>Adjustable</span></div>
      </div>
    </div>
  </section>
  <div className={s.sheetWrap}>{/* …CalcSheet… */}</div>
  <div className={s.content}>{/* …methodology, FAQ, related, cross-sell… */}</div>
</div>
```

Notes: only TWO crop marks (top corners) — the hero is shorter than the
shop's; bottom crops would crowd the overlapping sheet. The dimension strip's
`v` values are words or sheet numbers, small (not the shop's 32px price
numerals — see CSS).

```css
/* ---------- PAGE + HERO ---------- */
.calcPage { background: var(--bg-primary); }

.hero {
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  position: relative;
  border-bottom: 5px solid var(--accent-primary);
}
.hero::before {
  -webkit-mask-image: radial-gradient(ellipse 95% 90% at 50% 30%, #000 55%, transparent 100%);
  mask-image: radial-gradient(ellipse 95% 90% at 50% 30%, #000 55%, transparent 100%);
}
.heroInner {
  position: relative;
  z-index: 1;
  max-width: var(--width-full);
  margin: 0 auto;
  /* extra bottom padding = sheet overlap depth + breathing room */
  padding: var(--space-8) var(--container-padding-mobile) calc(var(--space-8) + 56px);
}
.eyebrow {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: var(--space-2);
}
.eyebrow::after {
  content: "";
  height: 1px;
  width: 90px;
  background: rgba(246, 241, 228, 0.25);
}
.heroTitle {
  font-family: var(--font-display);
  font-weight: 600;
  font-size: clamp(34px, 4.4vw, 52px);
  line-height: 1.02;
  letter-spacing: -0.022em;
  color: var(--cream);
  margin: 0 0 var(--space-2);
}
.heroSub {
  font-family: var(--font-display);
  font-style: italic;
  font-weight: 500;
  font-size: clamp(18px, 1.9vw, 21px);
  line-height: 1.4;
  color: rgba(246, 241, 228, 0.86);
  max-width: 560px;
  margin: 0;
}
.dimstrip {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  border-top: 1px solid rgba(246, 241, 228, 0.2);
  border-bottom: 1px solid rgba(246, 241, 228, 0.2);
  margin-top: var(--space-5);
  max-width: 720px;
}
.dimcell {
  padding: 12px 0 12px var(--space-2);
  border-left: 1px solid rgba(246, 241, 228, 0.14);
}
.dimcell:first-child { border-left: none; padding-left: 0; }
.k {
  display: block;
  font-family: var(--font-mono);
  font-size: 10.5px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: rgba(246, 241, 228, 0.6);
  margin-bottom: 6px;
}
.v {
  display: block;
  font-family: var(--font-mono);
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--cream);
  line-height: 1.3;
}
.crop { position: absolute; width: 16px; height: 16px; z-index: 2; }
.tl { top: 18px; left: 18px; border-top: 1px solid rgba(246,241,228,0.45); border-left: 1px solid rgba(246,241,228,0.45); }
.tr { top: 18px; right: 18px; border-top: 1px solid rgba(246,241,228,0.45); border-right: 1px solid rgba(246,241,228,0.45); }

/* ---------- SHEET WRAP (the overlap move) ---------- */
.sheetWrap {
  position: relative;
  z-index: 2;
  max-width: var(--width-full);
  margin: -56px auto 0;
  padding: 0 var(--container-padding-mobile);
}
.content {
  max-width: var(--width-full);
  margin: 0 auto;
  padding: 0 var(--container-padding-mobile);
}

@media (min-width: 768px) {
  .heroInner, .sheetWrap, .content {
    padding-left: var(--container-padding-tablet);
    padding-right: var(--container-padding-tablet);
  }
}
@media (min-width: 1024px) {
  .heroInner, .sheetWrap, .content {
    padding-left: var(--container-padding-desktop);
    padding-right: var(--container-padding-desktop);
  }
}
@media (max-width: 900px) {
  .heroInner { padding-bottom: calc(var(--space-7) + 32px); }
  .sheetWrap { margin-top: -32px; }
  .dimstrip { grid-template-columns: repeat(2, 1fr); }
  .dimcell:nth-child(odd) { border-left: none; padding-left: 0; }
  .dimcell:nth-child(n + 3) { border-top: 1px solid rgba(246, 241, 228, 0.14); }
}
```

### 3.2 The sheet itself (`sheet`, `sheetHead`, `sheetBody`)

DOM:

```jsx
<div className={s.sheet}>
  <div className={s.sheetHead}>
    <span className={s.sheetNo}>TO-02 · Drywall takeoff</span>
    <span className={s.sheetTools}>
      <button type="button" className={s.toolBtn}>Copy takeoff</button>
      <button type="button" className={s.toolBtn}>Print</button>
    </span>
  </div>
  <div className={s.sheetBody}>
    <div className={s.inputsCol}>{/* §4.1–4.3 */}</div>
    <div className={s.resultsCol} >{/* §4.4–4.6 */}</div>
  </div>
  <div className={s.tearoff}>{/* §6 EstimateCapture */}</div>
</div>
```

```css
/* ---------- SHEET ---------- */
.sheet {
  background: var(--bg-primary);
  border: 1px solid var(--hairline-strong);
  border-radius: 0;
  box-shadow:
    0 1px 2px rgba(35, 32, 25, 0.1),
    0 14px 30px rgba(16, 44, 66, 0.13); /* same lift as shop .sheet */
}
.sheetHead {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-2);
  padding: 14px var(--space-4);
  border-bottom: 1px solid var(--hairline);
}
.sheetNo {
  font-family: var(--font-mono);
  font-size: 11.5px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent-primary);
}
.sheetTools { display: flex; gap: var(--space-2); }
.toolBtn {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text-secondary);
  background: transparent;
  border: 1px solid var(--hairline-strong);
  border-radius: 0;
  padding: 8px 12px;
  cursor: pointer;
  transition: border-color 0.15s ease, color 0.15s ease;
}
.toolBtn:hover { border-color: var(--accent-primary); color: var(--accent-primary); }
.sheetBody {
  display: grid;
  grid-template-columns: 1fr 1.15fr;
  gap: 0;
}
.inputsCol {
  padding: var(--space-5) var(--space-4) var(--space-5) var(--space-4);
  border-right: 1px solid var(--hairline);
}
.resultsCol {
  padding: var(--space-5) var(--space-4);
  background: var(--bg-secondary); /* schedule column is the deeper paper */
}
.colLabel {
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--text-secondary);
  margin: 0 0 var(--space-4);
  display: flex;
  align-items: center;
  gap: 12px;
}
.colLabel::after { content: ""; height: 1px; flex: 1; background: var(--hairline); }

@media (max-width: 900px) {
  .sheetBody { grid-template-columns: 1fr; }
  .inputsCol { border-right: none; border-bottom: 1px solid var(--hairline); }
  .inputsCol, .resultsCol { padding: var(--space-4) var(--space-3); }
  .sheetHead { padding: 12px var(--space-3); }
  .toolBtn { display: none; }           /* copy/print are desktop affordances */
  .toolBtnPrintMobile { display: none; } /* no exceptions — keep mobile clean */
}
```

Both columns open with `<p className={s.colLabel}>Field measurements</p>` /
`<p className={s.colLabel}>Materials schedule</p>`.

---

## 4. Fields & results components

### 4.1 Number field with unit (`field`, `fieldInput`, `fieldUnit`)

DOM:

```jsx
<div className={s.field}>
  <label className={s.fieldLabel} htmlFor="dw-area">Floor area</label>
  <div className={s.fieldBox}>
    <input id="dw-area" className={s.fieldInput} type="number"
           inputMode="decimal" min={0} step="any" value={…} onChange={…} />
    <span className={s.fieldUnit} aria-hidden="true">ft²</span>
  </div>
  <span className={s.fieldHint}>Total finished floor area, all stories</span>
</div>
```

```css
/* ---------- FIELDS ---------- */
.field { margin-bottom: var(--space-4); }
.fieldLabel {
  display: block;
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--text-heading);
  margin-bottom: 8px;
}
.fieldBox {
  display: flex;
  align-items: stretch;
  background: #fff;                      /* white stock, like .sheet paper */
  border: 1px solid var(--hairline-strong);
  border-radius: 0;
  transition: border-color 0.15s ease;
}
.fieldBox:focus-within { border-color: var(--accent-primary); }
.fieldInput {
  flex: 1;
  min-width: 0;
  border: none;
  background: transparent;
  padding: 12px 4px 12px 14px;
  font-family: var(--font-mono);
  font-size: 17px;
  font-variant-numeric: tabular-nums;
  color: var(--text-heading);
  text-align: right;
  min-height: 44px;
}
.fieldInput:focus { outline: none; } /* focus ring carried by .fieldBox border */
.fieldInput::-webkit-outer-spin-button,
.fieldInput::-webkit-inner-spin-button { -webkit-appearance: none; margin: 0; }
.fieldInput[type='number'] { -moz-appearance: textfield; appearance: textfield; }
.fieldUnit {
  display: flex;
  align-items: center;
  padding: 0 14px 0 8px;
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-secondary);
  border-left: 1px dotted var(--hairline-strong);
  margin-left: 8px;
}
.fieldHint {
  display: block;
  margin-top: 6px;
  font-size: 13.5px;
  line-height: 1.45;
  color: var(--text-secondary);
}
.fieldInvalid .fieldBox { border-color: var(--accent-critical); }
.fieldError {
  display: block;
  margin-top: 6px;
  font-size: 13.5px;
  color: var(--accent-critical);
}
```

The global `*:focus` outline (2px accent) is suppressed on the inner input
and expressed by the box border on `:focus-within` — one ring, drafting-crisp.

### 4.2 Dimension pair (`dimPair`)

For length × width inputs (concrete slab, rooms):

```jsx
<div className={s.field}>
  <span className={s.fieldLabel} id="slab-dims-label">Slab dimensions</span>
  <div className={s.dimPair} role="group" aria-labelledby="slab-dims-label">
    <div className={s.fieldBox}>
      <input aria-label="Length in feet" className={s.fieldInput} … />
      <span className={s.fieldUnit} aria-hidden="true">ft</span>
    </div>
    <span className={s.dimTimes} aria-hidden="true">×</span>
    <div className={s.fieldBox}>
      <input aria-label="Width in feet" className={s.fieldInput} … />
      <span className={s.fieldUnit} aria-hidden="true">ft</span>
    </div>
  </div>
</div>
```

```css
.dimPair {
  display: grid;
  grid-template-columns: 1fr auto 1fr;
  align-items: center;
  gap: 10px;
}
.dimTimes {
  font-family: var(--font-mono);
  font-size: 15px;
  color: var(--text-secondary);
}
```

### 4.3 Segmented control (`seg`) and select (`selectBox`)

Segmented — for 2–4 discrete options (stud spacing, sheet size, coats).
Radios under the hood:

```jsx
<div className={s.field}>
  <span className={s.fieldLabel} id="dw-size-label">Sheet size</span>
  <div className={s.seg} role="radiogroup" aria-labelledby="dw-size-label">
    {options.map(o => (
      <label key={o.value} className={`${s.segOpt} ${value === o.value ? s.segOn : ''}`}>
        <input type="radio" name="dw-size" value={o.value}
               checked={value === o.value} onChange={…}
               className="visually-hidden" />
        {o.label}
      </label>
    ))}
  </div>
</div>
```

```css
.seg {
  display: flex;
  border: 1px solid var(--hairline-strong);
  background: #fff;
}
.segOpt {
  flex: 1;
  min-height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 10px;
  font-family: var(--font-mono);
  font-size: 12.5px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--text-secondary);
  border-left: 1px solid var(--hairline);
  cursor: pointer;
  transition: background 0.15s ease, color 0.15s ease;
  text-align: center;
}
.segOpt:first-child { border-left: none; }
.segOpt:hover { background: var(--bg-secondary); }
.segOn, .segOn:hover {
  background: var(--navy);
  color: var(--cream);
}
.segOpt:focus-within {
  outline: 2px solid var(--accent-primary);
  outline-offset: -2px;
}

/* Native select, dressed as a field */
.selectBox {
  position: relative;
  background: #fff;
  border: 1px solid var(--hairline-strong);
}
.selectBox:focus-within { border-color: var(--accent-primary); }
.selectInput {
  width: 100%;
  border: none;
  background: transparent;
  padding: 12px 38px 12px 14px;
  font-family: var(--font-mono);
  font-size: 14px;
  color: var(--text-heading);
  min-height: 44px;
  appearance: none;
  cursor: pointer;
}
.selectInput:focus { outline: none; }
.selectBox::after {
  content: "";
  position: absolute;
  right: 14px;
  top: 50%;
  width: 7px;
  height: 7px;
  border-right: 1.5px solid var(--text-secondary);
  border-bottom: 1.5px solid var(--text-secondary);
  transform: translateY(-70%) rotate(45deg);
  pointer-events: none;
}
```

Choosing between them: **segmented** when all options fit one row at 320px
wide (≤4 short labels); **select** otherwise. Never both for the same kind of
choice across two calculators — consistency per input type (stud spacing is
always segmented; region/quality tiers always select).

### 4.4 Materials schedule (`heroQty`, `schedule`)

The results column. Hero quantity first — the number the visitor came for —
then the schedule lines.

```jsx
<div aria-hidden="true">{/* visual layer; announcements via §5.4 */}
  <p className={s.colLabel}>Materials schedule</p>
  <div className={s.heroQty}>
    <span className={s.heroQtyVal}>89</span>
    <span className={s.heroQtyUnit}>4×8 sheets</span>
  </div>
  <ul className={s.schedule}>
    <li className={s.schedLine}>
      <span className={s.schedKey}>Joint compound</span>
      <span className={s.schedLeader} />
      <span className={s.schedVal}>11 buckets</span>
    </li>
    …
  </ul>
</div>
```

```css
/* ---------- SCHEDULE ---------- */
.heroQty {
  display: flex;
  align-items: baseline;
  gap: 14px;
  padding-bottom: var(--space-3);
  margin-bottom: var(--space-3);
  border-bottom: 1px solid var(--hairline-strong);
}
.heroQtyVal {
  font-family: var(--font-display);
  font-size: clamp(44px, 5vw, 60px);
  font-weight: 600;
  line-height: 1;
  letter-spacing: -0.025em;
  color: var(--accent-primary);
  font-variant-numeric: tabular-nums;
}
.heroQtyUnit {
  font-family: var(--font-mono);
  font-size: 12.5px;
  font-weight: 500;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--text-heading);
}
.schedule { list-style: none; margin: 0 0 var(--space-4); padding: 0; }
.schedLine {
  display: flex;
  align-items: baseline;
  gap: 10px;
  padding: 9px 0;
  margin: 0;
}
.schedKey {
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-secondary);
  flex-shrink: 0;
}
.schedLeader {
  flex: 1;
  min-width: 24px;
  border-bottom: 1px dotted var(--hairline-strong);
  transform: translateY(-4px);
}
.schedVal {
  font-family: var(--font-display);
  font-size: 18px;
  font-weight: 600;
  color: var(--text-heading);
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}
```

### 4.5 Cost dimension line (`costDim`)

Cost is secondary to quantities and rendered as a **dimension line**: tick,
rule, filled span, rule, tick — low and high labels at the ends.

```jsx
<div className={s.costDim}>
  <p className={s.costDimLabel}>Estimated material cost
    <span className={s.costDimNote}>national range</span></p>
  <div className={s.costDimBar} role="img"
       aria-label="Estimated material cost between $1,240 and $1,690">
    <span className={s.costLow}>$1,240</span>
    <span className={s.costTrack}><span className={s.costSpan} /></span>
    <span className={s.costHigh}>$1,690</span>
  </div>
</div>
```

```css
/* ---------- COST DIMENSION LINE ---------- */
.costDim {
  border-top: 1px solid var(--hairline);
  padding-top: var(--space-3);
  margin-bottom: var(--space-3);
}
.costDimLabel {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: var(--space-2);
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--text-heading);
  margin: 0 0 12px;
}
.costDimNote {
  font-size: 10.5px;
  letter-spacing: 0.1em;
  color: var(--text-secondary);
}
.costDimBar { display: flex; align-items: center; gap: 12px; }
.costLow, .costHigh {
  font-family: var(--font-display);
  font-size: 20px;
  font-weight: 600;
  color: var(--text-heading);
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}
.costTrack {
  position: relative;
  flex: 1;
  height: 12px;
}
/* end ticks */
.costTrack::before, .costTrack::after {
  content: "";
  position: absolute;
  top: 0;
  width: 1px;
  height: 12px;
  background: var(--hairline-strong);
}
.costTrack::before { left: 0; }
.costTrack::after { right: 0; }
/* the dimension rule */
.costSpan {
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  height: 3px;
  transform: translateY(-50%);
  background: var(--accent-primary);
}
```

(The span always runs tick-to-tick — the two figures ARE the range; no fake
precision about where "your" number falls.)

### 4.6 Hatched breakdown bars (`bars`)

Only for calculators whose result has meaningful components (framing-lumber:
studs/plates/sheathing/headers; roofing: shingles/underlayment/starter;
paint: walls/ceiling/trim). Skip it when there's one dominant quantity
(drywall, concrete, flooring, insulation) — a chart with one bar is noise.

Hatch tints are derived from existing palette colors (navy `#102c42`,
accent `#c75a22`) at fixed alphas — the only "new" color values in this
system, and they're derivations, not additions:

```jsx
<div className={s.bars}>
  <p className={s.barsLabel}>Where the board feet go</p>
  {rows.map((r, i) => (
    <div key={r.key} className={s.barRow}>
      <span className={s.barKey}>{r.label}</span>
      <span className={s.barTrack}>
        <span className={`${s.barFill} ${i === 0 ? s.barFillLead : ''}`}
              style={{ width: `${r.pct}%` }} />
      </span>
      <span className={s.barVal}>{r.valueLabel}</span>
    </div>
  ))}
</div>
```

```css
/* ---------- HATCHED TAKEOFF BARS ---------- */
.bars {
  border-top: 1px solid var(--hairline);
  padding-top: var(--space-3);
  margin-bottom: var(--space-3);
}
.barsLabel {
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 500;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--text-heading);
  margin: 0 0 12px;
}
.barRow {
  display: grid;
  grid-template-columns: minmax(92px, 130px) 1fr minmax(72px, auto);
  gap: 12px;
  align-items: center;
  padding: 7px 0;
}
.barKey {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--text-secondary);
}
.barTrack {
  display: block;
  height: 16px;
  background: #fff;
  border: 1px solid var(--hairline);
}
.barFill {
  display: block;
  height: 100%;
  min-width: 2px;
  border-right: 1px solid var(--hairline-strong);
  /* drafting hatch: navy section lines on transparent */
  background: repeating-linear-gradient(
    -45deg,
    rgba(16, 44, 66, 0.5) 0 2px,
    transparent 2px 7px
  );
  transition: width 0.25s ease;
}
/* the largest component gets the accent hatch */
.barFillLead {
  background: repeating-linear-gradient(
    -45deg,
    rgba(199, 90, 34, 0.65) 0 2px,
    transparent 2px 7px
  );
}
.barVal {
  font-family: var(--font-display);
  font-size: 15px;
  font-weight: 600;
  color: var(--text-heading);
  text-align: right;
  font-variant-numeric: tabular-nums;
  white-space: nowrap;
}
@media (prefers-reduced-motion: reduce) {
  .barFill { transition: none; }
}
```

### 4.7 Fine print + assumptions block

Inside the results column, after cost/bars:

```css
.finePrint {
  font-size: 13px;
  line-height: 1.5;
  color: var(--text-secondary);
  border-top: 1px dotted var(--hairline-strong);
  padding-top: var(--space-2);
  margin: 0;
}
```

Copy (every calculator, verbatim pattern): *"Estimate only. Quantities
assume [one-line basis]; order after a takeoff from your actual plans.
Prices are national ranges, [Month Year] — get local quotes."*

The full **AssumptionsBlock** lives in the content area (§7) as leader-lines
reusing `schedule`/`schedLine` classes inside a bordered box:

```css
.assumptions {
  border: 1px solid var(--hairline-strong);
  background: var(--bg-secondary);
  padding: var(--space-4);
  max-width: 720px;
}
.assumptions .schedVal { font-size: 16px; }
```

---

## 5. Interaction spec

1. **Live updates, no Calculate button.** Engines are pure functions;
   recompute synchronously on every controlled-input change. Default values
   pre-fill every calculator so the schedule is never empty on load.
2. **No number tick animation.** A takeoff is penciled in, not slot-machined.
   Ticking numbers draw the eye to the animation instead of the answer, fight
   `tabular-nums` alignment, and cost reduced-motion handling for zero
   information gain. The only motion: 250ms width ease on breakdown bars and
   a 180ms `background-color` fade on `.resultsCol` (from `#fff` flash back
   to `var(--bg-secondary)`) — both disabled under `prefers-reduced-motion`.
3. **Debounce policy.** Computation: none (instant). Announcements (§5.4)
   and `calculator_use` tracking: 600ms after last change. Track
   `calculator_use` once per calculator per page load (first valid change),
   params `{ calculator: '<slug>' }`.
4. **Screen reader etiquette.** The visual results layer is `aria-hidden`.
   One visually-hidden `<div role="status" aria-live="polite">` receives a
   debounced one-sentence summary: *"Takeoff updated: 89 sheets, 11 buckets
   joint compound, cost $1,240 to $1,690."* Never announce per keystroke;
   never announce on initial load.
5. **Invalid input.** Clamp silently at compute time (engines guard), but
   when a field is empty or non-numeric show `.fieldInvalid` + `.fieldError`
   ("Enter a number") and hold the last valid schedule — never NaN, never a
   blank results panel. Zero is a valid input everywhere it's physically
   meaningful.
6. **Print.** `.toolBtn` Print calls `window.print()`. Global print CSS (add
   to `globals.css`):

```css
@media print {
  header, footer, nav { display: none !important; }
  .no-print { display: none !important; }
}
```

   Calculator template puts `no-print` on: hero band, tear-off capture,
   FAQ/related/cross-sell sections, sticky bar. Module print rules:

```css
@media print {
  .sheet { box-shadow: none; border-color: #000; }
  .resultsCol { background: #fff; }
  .sheetTools { display: none; }
  .printMeta { display: block !important; }
}
.printMeta {
  display: none;
  font-family: var(--font-mono);
  font-size: 10px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-secondary);
  padding: 10px var(--space-4);
  border-top: 1px solid var(--hairline);
}
```

   `.printMeta` content: *"Printed from build-your-house.com/calculators/drywall — estimate only."*
7. **Copy takeoff.** Copies a plain-text schedule (inputs + quantities +
   cost range + URL) via `navigator.clipboard`. Button label flips to
   "Copied" for 1.5s (text swap, no animation). Fire `calculator_copy`
   event `{ calculator }`.
8. **Sticky mobile bar** (`<900px` only): fixed bottom navy bar showing the
   hero quantity + "View takeoff →" anchor to `#takeoff` (id on
   `.resultsCol`, `scroll-margin-top: 96px`). Hidden while `.resultsCol` is
   in the viewport (IntersectionObserver; if JS-less, bar simply shows —
   harmless). Respect `env(safe-area-inset-bottom)`.

```css
.stickyBar {
  position: fixed;
  left: 0; right: 0; bottom: 0;
  z-index: 40;
  display: none;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-2);
  background: var(--navy);
  color: var(--cream);
  padding: 12px var(--container-padding-mobile);
  padding-bottom: calc(12px + env(safe-area-inset-bottom));
  border-top: 3px solid var(--accent-primary);
}
.stickyBarQty {
  font-family: var(--font-mono);
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}
.stickyBarLink {
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--cream);
  text-decoration: none;
  border: 1px solid rgba(246, 241, 228, 0.35);
  padding: 9px 14px;
  white-space: nowrap;
}
@media (max-width: 900px) {
  .stickyBar { display: flex; }
  .stickyBarHidden { display: none; }
}
```

---

## 6. Email capture — the tear-off stub

Placement: bottom of the sheet, full width, **after** results — the visitor
has already gotten full value; the ask is to keep it. Dashed top rule = the
perforation. No modal, no scroll-triggered popup, no gating: the numbers are
never held hostage.

DOM:

```jsx
<div className={`${s.tearoff} no-print`}>
  <div className={s.tearoffCopy}>
    <p className={s.tearoffHead}>Send this takeoff to your inbox</p>
    <p className={s.tearoffSub}>
      The quantities above, with your inputs, as one email — so you still
      have them when you're pricing at the lumberyard. You'll also get our
      owner-builder newsletter; unsubscribe any time.
    </p>
  </div>
  <form className={s.tearoffForm}>{/* honeypot input, visually-hidden */}
    <input type="email" required placeholder="you@example.com"
           aria-label="Email address" className={s.tearoffInput} />
    <button type="submit" className={s.tearoffBtn}>Email my estimate</button>
  </form>
  <p className={s.tearoffFine}>No spam. One email with your numbers, then the
    occasional newsletter. Unsubscribe in one click.</p>
</div>
```

States: submitting → button text "Sending…" disabled; success → replace form
with `<p className={s.tearoffDone}>Sent. Give it a few minutes, and check
spam if it's not there.</p>`; error → inline `.fieldError` text ("That
didn't send. Try again in a minute."). Fire `generate_lead`
`{ method: 'calculator_estimate', calculator }` on success only.

```css
/* ---------- TEAR-OFF CAPTURE ---------- */
.tearoff {
  border-top: 1px dashed var(--hairline-strong);
  padding: var(--space-5) var(--space-4);
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  gap: var(--space-2) var(--space-6);
  align-items: center;
}
.tearoffHead {
  font-family: var(--font-display);
  font-size: 22px;
  font-weight: 600;
  letter-spacing: -0.01em;
  color: var(--text-heading);
  margin: 0 0 8px;
}
.tearoffSub {
  font-size: 15px;
  line-height: 1.55;
  color: var(--text-secondary);
  margin: 0;
  max-width: none;
}
.tearoffForm { display: flex; gap: 10px; }
.tearoffInput {
  flex: 1;
  min-width: 0;
  background: #fff;
  border: 1px solid var(--hairline-strong);
  border-radius: 0;
  padding: 0 14px;
  min-height: 48px;
  font-family: var(--font-body);
  font-size: 15px;
  color: var(--text-heading);
}
.tearoffInput:focus {
  outline: none;
  border-color: var(--accent-primary);
}
.tearoffBtn {
  font-family: var(--font-mono);
  font-size: 12.5px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  font-weight: 500;
  background: var(--accent-primary);
  color: var(--cream);
  border: 1px solid var(--accent-primary);
  border-radius: 0;
  padding: 0 20px;
  min-height: 48px;
  cursor: pointer;
  transition: background 0.18s ease;
  white-space: nowrap;
}
.tearoffBtn:hover { background: var(--button-primary-hover); }
.tearoffBtn:disabled { opacity: 0.6; cursor: default; }
.tearoffFine {
  grid-column: 1 / -1;
  font-size: 12.5px;
  color: var(--text-secondary);
  margin: 0;
  max-width: none;
}
.tearoffDone {
  font-size: 15px;
  color: var(--text-heading);
  margin: 0;
}
@media (max-width: 900px) {
  .tearoff { grid-template-columns: 1fr; padding: var(--space-4) var(--space-3); }
  .tearoffForm { flex-direction: column; }
  .tearoffBtn { min-height: 48px; padding: 12px 20px; }
}
```

---

## 7. Content area components

All content sections use the shop's section scaffold, re-declared in the
module (secHead/secLabel/secTitle/secMeta — copy the shop values verbatim):

```css
.block { padding: var(--space-10) 0 0; }
.secHead {
  display: flex;
  align-items: flex-end;
  justify-content: space-between;
  gap: var(--space-3);
  border-bottom: 1px solid var(--hairline);
  padding-bottom: var(--space-3);
  margin-bottom: var(--space-5);
}
.secLabel {
  font-family: var(--font-mono);
  font-size: 13px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent-primary);
  margin-bottom: 8px;
}
.secTitle {
  font-family: var(--font-display);
  font-weight: 600;
  font-size: clamp(26px, 3vw, 38px);
  letter-spacing: -0.02em;
  line-height: 1.05;
  margin: 0;
}
.secMeta {
  font-family: var(--font-mono);
  font-size: 11.5px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--text-secondary);
  text-align: right;
  line-height: 1.7;
  white-space: nowrap;
}
.prose { max-width: 720px; }
.prose p { font-size: 16.5px; line-height: 1.65; color: var(--text-secondary); }
.prose strong { color: var(--text-heading); }
@media (max-width: 900px) { .secMeta { display: none; } }
```

Section order and right-meta values (every calculator page):

| # | secLabel | secTitle | secMeta |
|---|----------|----------|---------|
| 1 | Methodology | How this takeoff is figured | SHEET TO-0n |
| 2 | Assumptions | Waste, spacing, and coverage | ADJUST ABOVE |
| 3 | Questions | Owner-builders ask | FAQ |

**Methodology** shows the actual formulas in prose + a two-column leader
table (reuse `.assumptions`). This is a differentiator — every competitor
hides the math; we print it. FAQ reuses shop's `faqItem/faqQ/faqA` values
verbatim (copy into module).

**RelatedCalcs** — a ladder-strip (shop `.ladder` pattern) after FAQ:

```css
.related {
  border: 1px solid var(--hairline);
  background: var(--bg-secondary);
  display: grid;
  grid-template-columns: auto 1fr;
  margin-top: var(--space-10);
}
.relatedLabel {
  font-family: var(--font-mono);
  font-size: 10.5px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--accent-primary);
  writing-mode: vertical-rl;
  transform: rotate(180deg);
  text-align: center;
  padding: 14px 10px;
  border-right: 1px solid var(--hairline);
}
.relatedGrid { display: grid; grid-template-columns: repeat(3, 1fr); }
.relatedCell {
  display: block;
  padding: 14px 16px;
  border-right: 1px solid var(--hairline);
  text-decoration: none;
  transition: background 0.15s ease;
}
.relatedCell:last-child { border-right: none; }
.relatedCell:hover { background: var(--bg-primary); text-decoration: none; }
.relatedNo {
  display: block;
  font-family: var(--font-mono);
  font-size: 10.5px;
  letter-spacing: 0.12em;
  color: var(--accent-primary);
  margin-bottom: 4px;
}
.relatedName {
  display: block;
  font-family: var(--font-display);
  font-weight: 600;
  font-size: 15.5px;
  line-height: 1.25;
  color: var(--text-heading);
}
@media (max-width: 900px) {
  .related { grid-template-columns: 1fr; }
  .relatedLabel {
    writing-mode: horizontal-tb;
    transform: none;
    border-right: none;
    border-bottom: 1px solid var(--hairline);
    padding: 10px 16px;
    text-align: left;
  }
  .relatedGrid { grid-template-columns: 1fr; }
  .relatedCell { border-right: none; border-bottom: 1px solid var(--hairline); }
  .relatedCell:last-child { border-bottom: none; }
}
```

Show exactly **three** related sheets per page (the most adjacent trades),
not all six — a strip, not a sitemap.

**CrossSell** — reuse the existing `<BinderCTA>` component as-is (it already
has GA4 attribution) but pass a calculator-specific `lead` tying the tool to
the product, e.g. framing page: *"The binder's materials section holds your
takeoffs, quotes, and delivery logs — the sheets this calculator fills in."*
On concrete/roofing pages where a state kit is more relevant, keep BinderCTA
anyway (kits are state-specific; the binder is universal). Placement: last
element before the footer.

---

## 8. Hub page — the sheet index (`CalcHub.module.css`)

Hero: same band recipe as §3.1 (compact, two crop marks, dimension strip
cells: `7 SHEETS / NO SIGNUP / FORMULAS SHOWN / PRINT-READY`), title
"Owner-Builder Calculators", sub: *"Takeoff sheets for the materials that
dominate your budget — quantities first, cost ranges second, every formula
shown."* No sheet overlap on the hub (nothing to overlap); hero bottom
padding normal (`var(--space-8)`).

Index rows:

```jsx
<Link href="/calculators/framing-lumber" className={h.idxRow}>
  <span className={h.idxNo}>TO-01</span>
  <span className={h.idxMain}>
    <span className={h.idxTitle}>Framing &amp; Lumber Calculator</span>
    <span className={h.idxDesc}>Studs, plates, headers, and sheathing from
      your wall dimensions — in board feet and stick counts.</span>
  </span>
  <span className={h.idxOut}>studs · plates · sheathing</span>
  <span className={h.idxGo} aria-hidden="true">→</span>
</Link>
```

```css
.idxRow {
  display: grid;
  grid-template-columns: 80px 1fr 220px 40px;
  gap: var(--space-3);
  align-items: center;
  padding: var(--space-4) var(--space-2);
  border-top: 1px solid var(--hairline);
  text-decoration: none;
  transition: background 0.15s ease, box-shadow 0.15s ease;
}
.idxRow:last-of-type { border-bottom: 1px solid var(--hairline); }
.idxRow:hover {
  background: var(--bg-secondary);
  box-shadow: inset 3px 0 0 var(--accent-primary);
  text-decoration: none;
}
.idxNo {
  font-family: var(--font-mono);
  font-size: 12px;
  letter-spacing: 0.12em;
  color: var(--accent-primary);
}
.idxTitle {
  display: block;
  font-family: var(--font-display);
  font-size: 21px;
  font-weight: 600;
  line-height: 1.2;
  letter-spacing: -0.01em;
  color: var(--text-heading);
  margin-bottom: 5px;
}
.idxDesc {
  display: block;
  font-size: 14.5px;
  line-height: 1.5;
  color: var(--text-secondary);
}
.idxOut {
  font-family: var(--font-mono);
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-secondary);
  text-align: right;
  line-height: 1.6;
}
.idxGo {
  font-family: var(--font-mono);
  font-size: 16px;
  color: var(--accent-primary);
  text-align: right;
}
@media (max-width: 900px) {
  .idxRow { grid-template-columns: 56px 1fr 24px; }
  .idxOut { display: none; }
}
```

Two groups with the §7 secHead scaffold: **Takeoff sheets** (`TO-01…TO-07`)
and **Planning worksheets** (`W-01` Cost Savings, `W-02` Material Cost
[umbrella estimator], `W-03` Timeline, `W-04` Budget Tracker). Sheet number
assignments are permanent:

TO-01 framing-lumber · TO-02 drywall · TO-03 concrete-slab · TO-04 roofing ·
TO-05 paint · TO-06 flooring · TO-07 insulation.

---

## 9. Responsive & accessibility

- **Breakpoints used:** 1024 (container padding step), 900 (sheet columns
  stack, secMeta hides, related stacks, sticky bar appears), 600/480
  inherit global type scale only. Match shop exactly; no new breakpoints.
- **Touch targets:** every input, segment, select, button ≥44px tall;
  sticky-bar link ≥40px with padding.
- **Labels:** every input has a visible `<label>` (`for`/`id`) or
  `aria-label` (dimension pair members). Segmented = radiogroup with
  visually-hidden radios (keyboard: arrow keys native).
- **Live results:** visual panel `aria-hidden="true"`; debounced summary in
  a single `role="status"` node (§5.4). Cost bar is `role="img"` with the
  full sentence in `aria-label`.
- **Contrast rules:**
  - Cream `#f6f1e4` on navy `#102c42` ≈ 12:1 — free use.
  - Orange `--accent-primary #c75a22` on paper `#f2ecdf` ≈ 4.0:1 — **large
    text only** (heroQtyVal, idxGo arrows, ≥19px semibold). For small mono
    labels that are decorative/duplicated (sheetNo, secLabel, idxNo,
    relatedNo) it matches existing shop precedent and is acceptable; for
    any small orange text that is the ONLY affordance (links), use
    `var(--link-color)` `#b44e1a` instead.
  - `--text-secondary #56503f` on `--bg-secondary #e9e0ce` ≈ 6.4:1 — fine.
- **Reduced motion:** bars width transition, resultsCol flash, and toolBtn
  transitions all wrapped in `prefers-reduced-motion: reduce` overrides
  (shown in CSS above where they exist).
- **No layout shift:** results panel pre-filled from defaults at first
  paint (server-rendered markup carries default-input results, since
  engines are pure and defaults are static).

---

## 10. Voice reference for page copy

- Never "instantly discover" / "unlock" / "supercharge". Say what it does:
  "Sheets, mud, tape, and screws for your square footage."
- Every number claim carries its basis: "assumes 16″ o.c. studs" not
  "industry-standard assumptions".
- The disclaimer is one honest sentence, not a legal wall (§4.7).
- CTA verbs are literal: "Email my estimate", "Print", "Copy takeoff",
  "See what's inside — $97".

*End of spec.*
