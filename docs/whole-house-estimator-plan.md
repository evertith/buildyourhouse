# Whole-House Estimator v2 — Implementation Plan

**Status:** M1 done 2026-10-14 (StudTally on Railway). M2 built 2026-10-14 in the working tree, lint, typecheck, engine tests, and the static build pass; not yet committed or pushed. Written 2026-10-13.
**Design:** Direction D on the canvas, https://claude.ai/artifact/8zMPvCzBY9iZH92DGy4Hwq (row 4: free estimate and plans-attached, desktop and phone).
**Companion:** `~/Repositories/studtally/docs/10-railway-and-partner-api.md` (hosting move, Claude API auth, partner API).
**Route:** stays `/calculators/material-estimator`. It is the site's most-cited page; the URL, canonical, and inbound links do not move.

## 0. Decisions this plan assumes

| Decision | Choice |
|---|---|
| Product ladder | Free profile estimate → $20 measured estimate (StudTally reads the plans, no review step) → $79 reviewed framing order list at studtally.com. The profile estimate is free. The $20 is credited toward the $79 if the buyer goes on to the framing list: a single-use $20-off code StudTally issues per paid read (v1), applied automatically on the claim-flow session (v2). Every place the $79 appears says what it buys: the framing material list (lumber, sheathing, hardware, by wall), not a whole-house list; a buyer arriving from a 14-phase estimate will assume otherwise unless told. |
| Upload limit | 100 MB per PDF, stated in the attach panel before the file picker and in the FAQ. The account stays on the Workers Free plan, whose request-body cap is the ceiling everywhere. |
| Labor | In. Every phase has a Hire it / Do it myself switch. The total splits into materials, hired labor, and your own hours. |
| Regional pricing | Yes. A per-state materials and labor index drives the numbers; 50 state landing pages ship in M4. |
| Sequencing | M1 StudTally on Railway → M2 free estimator → M3 the $20 rung → M4 state pages. The $20 rung never ships while the StudTally backend is on the Mac. |
| Design | Direction D: A's ledger page, C's sticky rail and sheet-reference chips, B's colors. Navy `#102C42`, paper `#F4EFE4`, orange `#EE8A4B` only for your-hours and the one call to action, Instrument Serif + Instrument Sans. |
| Vision model | `claude-opus-5` stays in production. `claude-opus-5-5` is evaluated on the golden set first (cheaper, same context); see the StudTally doc. |

## 1. Milestones

| M | Deliverable | Depends on | Effort |
|---|---|---|---|
| M1 | StudTally API + worker on Railway, vision on a service-account API key, Mac tunnel retired. Started 2026-10-13: project, services, variables, first deploys, trial DB restore, custom domain registered; Done 2026-10-14: R2 token, storage sync, Anthropic key (30-day, expires 2026-11-13), smoke test, final DB restore, DNS switch, Mac agents stopped, web app redeployed with the 100 MB copy. Remaining: watch for a day and the first real paid job (StudTally `docs/10` §5 step 7) | nothing | 1–2 days |
| M2 | Free whole-house estimator live at the existing URL, old W-02 engine retired. Built 2026-10-14: `src/lib/estimate/` (geometry, prices, 50-state index, labor, 14 phases, runner, URL profile, default run, 11 node tests), `src/components/estimate/` (Direction D page), `materialEstimator.ts` and `MaterialEstimatorCalc.tsx` deleted, registry, hub, and home copy updated, newsletter Worker `/estimate` widened to 24 rows with custom headings and deployed. Awaiting commit and push (CF Pages deploys from main). | nothing (parallel with M1) | 5–7 days |
| M3 | Plans-attached rung live: upload, $20 checkout, reading status, measured ledger, emails, refunds | M1, M2 | 4–6 days |
| M4 | 50 state pages from the same engine, hub and sitemap updated, launch content | M2 | 2–3 days |

Effort is working days of focused build with Claude Code, not calendar time.

## 2. Workstream W2 — the engine (`src/lib/estimate/`)

The architectural move is one shared geometry object. A profile derives a synthetic one; a StudTally read produces a real one; every downstream phase is identical.

### 2.1 Files

```
src/lib/estimate/
  geometry.ts        Geometry type, Sourced<T>, deriveGeometry(profile), geometryFromStudTally(payload)
  prices.ts          unit rates {low, high, unit}, asOf, finish multipliers
  stateIndex.ts      { [code]: { materials, labor } } for 50 states, NC = 1.00
  labor.ts           per-phase labor ratios, blended hourly rates, DIY defaults, hours
  phases/
    soft.ts site.ts foundation.ts framing.ts roofing.ts openings.ts exterior.ts
    plumbing.ts electrical.ts hvac.ts insulation.ts drywallPaint.ts interior.ts final.ts
  estimate.ts        runEstimate(profile | geometry, choices) → Estimate
  format.ts          reuse src/lib/calc/format.ts
  __tests__/         golden values, properties, snapshots
```

The seven trade sheets under `src/lib/calc/` keep their length-by-width inputs and their pages. Phase modules share formulas with them at the function level (import `framing.ts` helpers where they fit), never at the component level. `src/lib/calc/materialEstimator.ts` is deleted once the new page ships.

### 2.2 Geometry

```ts
type Source = 'derived' | 'measured' | 'user';
interface Sourced<T> { value: T; source: Source; ref?: string }   // ref: "A-2"

interface Geometry {
  heatedSf: Sourced<number>;
  stories: Sourced<1 | 2 | 3>;
  footprintSf: Sourced<number>;
  perimeterLf: Sourced<number>;
  wallHeightFt: Sourced<number>;                 // typical
  extWallLf: Sourced<number>;                    // sum of exterior walls, all stories
  intWallLf: Sourced<number>;
  extWallAreaSf: Sourced<number>;                // gross, before openings
  openings: Sourced<{ windows: number; windowAreaSf: number; extDoors: number; garageDoors: number }>;
  rooms: Sourced<{ count: number; baths: number; kitchens: number; bedrooms: number }>;
  roof: Sourced<{ planeAreaSf: number; pitch: number; ridgeLf: number; hipValleyLf: number; eaveLf: number; framing: 'stick' | 'truss' | 'unknown' }>;
  foundation: Sourced<'slab' | 'crawl' | 'basement'>;
  framedFloorSf: Sourced<number>;                // raised floors only
  unheatedSf: Sourced<number>;                   // garage, porches under roof
  porches: Sourced<{ count: number; posts: number }>;
  assumed: string[];                             // plain-language list of what was assumed
}
```

### 2.3 Profile → Geometry (free rung)

Inputs: heated sq ft, stories, finish level, foundation, state, roof complexity (gable / hip / cut-up, kept from today's sheet as an advanced option, default hip). Rules carry over from `materialEstimator.ts` so the free numbers do not jump at launch:

- footprint = heated ÷ stories; perimeter from a 1.5:1 rectangle of that area
- interior partitions 1 lf per 4 sq ft of floor per story; wall height 9 ft default (8 / 10 selectable)
- openings: 1 window per 110 sq ft heated (15 sq ft each), 3 exterior doors, 1 garage door when heated ≥ 1,400
- rooms: count = heated ÷ 170; baths = 2 below 1,800, 2.5 to 2,600, 3 above; 1 kitchen
- roof plane area = footprint × 1.1 / 1.3 / 1.5 by complexity; pitch 6:12; eave lf = perimeter × 1.1; ridge = long side; hips and valleys = 0 / 1.2 × short side / 2.4 × short side
- framed floor = footprint for crawl and basement, 0 for slab; unheated = 440 sq ft garage when a garage door is present
- every field `source: 'derived'`; `assumed` lists the rules in words

### 2.4 StudTally → Geometry (measured rung)

The partner endpoint returns a flat JSON built from the `Extraction` model (fields: `footprint`, `walls`, `openings`, `rooms`, `areas`, `roof`, `floor_system`, `porches`, `wall_heights`, `scope`, `flags`). Mapping:

| Geometry field | StudTally source | ref |
|---|---|---|
| heatedSf | `areas.heated_sf`, else `footprint.area_sf × stories` | areas-table sheet |
| stories | `scope.stories` | scope sheet |
| footprintSf, perimeterLf | `footprint.area_sf`, `footprint.perimeter_ft` | floor-plan sheet |
| wallHeightFt | `wall_heights.typical_ft` | elevation/section sheet |
| extWallLf, intWallLf | `exterior_wall_lf()`, `interior_wall_lf()` | floor-plan sheet |
| extWallAreaSf | Σ exterior wall `length_ft × height_ft` | |
| openings | `openings` by `kind` and `exterior`; window area from width × height | schedule or floor-plan sheet |
| rooms | `rooms` by name match (bath, kitchen, bed) | floor-plan sheet |
| roof | Σ `roof.planes` (`plan_area_sf × pitch factor`, `ridge_lf`, `hip_lf + valley_lf`), `roof.pitch`, `roof.framing` | roof-plan sheet |
| foundation | `scope.foundation`, else the setup answer | |
| framedFloorSf | `floor_system.area_sf` | foundation sheet |
| unheatedSf | `areas.unheated_total_sf` | |
| porches | `porches` count and posts | |
| assumed | the partner payload's `assumed[]` (auto-resolved flags and defaults) | |

Fields the payload lacks fall back to the derived rule for that field, with `source: 'derived'`, so a partial read still produces a complete ledger and the chips tell the truth row by row.

### 2.5 Phase engines

Each module is `(g: Geometry, p: Prices, idx: StateIndex, finish: Finish) → PhaseResult { id, name, note, lines: Line[], materials: {low, high}, labor: {low, high}, basis: Source }`. Lines keep today's `CalcLine` shape (`label, qty, unit, detail, costLow, costHigh`) plus `ref?` for the sheet chip.

| Phase | Materials formula sketch | Reuses |
|---|---|---|
| Before you break ground | permit = state base + $0.35/sq ft; plan review; survey flat; tap/impact fee band by state; builder's risk = 0.5% of hard cost; plans allowance by stock/custom | |
| Site work | clearing and grade per footprint sq ft; driveway base 60 lf × width; silt fence per perimeter; temp power flat | |
| Foundation | slab: 4" slab over footprint + 16"×12" footing on perimeter → yd³; crawl: CMU 3 ft × perimeter, piers per 200 sq ft, PT sill per perimeter; basement: 8 ft × 8" walls on perimeter + slab | `concrete.ts` |
| Framing | per-wall studs (ext lf, int lf, corners, openings), plates lf × 3, headers per opening, sheathing by ext wall area, subfloor by framed floor, trusses = eave ÷ 2 ft or rafters by plane area, waste by category | `framing.ts` |
| Roofing | squares = plane area ÷ 100 × pitch waste; underlayment; ice-and-water per eave lf; drip edge per eave + rake; ridge vent per ridge lf | `roofing.ts` |
| Windows and exterior doors | windows × unit by finish; ext doors; garage door | |
| Exterior finish | siding = ext wall area − opening area; trim lf per corner and opening; soffit/fascia per eave; gutters per eave | |
| Plumbing | fixtures = baths × 3 + kitchen 2 + laundry 2; rough per fixture; DWV per footprint; water heater | |
| Electrical | service flat; rough per heated sq ft; devices per room; fixture allowance per room | |
| HVAC | tons = heated ÷ 600 (state climate factor); duct per heated sq ft; bath fans per bath | |
| Insulation | wall batts by ext wall area; attic by ceiling area; crawl floor when crawl | `insulation.ts` |
| Drywall and paint | both faces of partitions + ceilings → sheets; mud/tape; primer + 2 coats | `drywall.ts`, `paint.ts` |
| Interior finish | doors = rooms − 2; trim lf = int wall lf × 2 + perimeter; flooring = heated by finish; cabinets by kitchen + baths; counters; tile by baths | `flooring.ts` |
| Final and move-in | appliances by finish; drive and walks sq ft; landscaping allowance; clean + dumpster | |

Contingency is not a phase; the rail shows 10% of cash as a separate line.

### 2.6 Prices and the state index

`prices.ts` holds every unit rate as `{ low, high, unit }` with `asOf: '2026-10'` and finish multipliers (basic 0.85, standard 1, premium 1.3) applied only to finish-sensitive phases (openings, exterior, drywall and paint, interior). Rates are national; the page prints the as-of date. Refresh is a quarterly ritual: edit the file, regenerate the FAQ numbers, snapshot tests update.

`stateIndex.ts` carries `{ materials, labor }` per state with NC = 1.00, seeded from published regional construction cost factors and labeled a planning index. Materials index applies to every materials line; labor index to every labor line. Later this can move to Worker KV for updates without a deploy; not in scope now.

### 2.7 Labor

Per phase: `labor = materials.mid × ratio × idx.labor`, ratios in `labor.ts` (site 1.5, foundation 0.85, framing 0.7, roofing 0.8, openings 0.25, exterior 0.8, plumbing 1.3, electrical 1.5, HVAC 0.75, insulation 0.55, drywall and paint 1.6, interior 0.5, final 0.35). Hours = labor ÷ blended rate per phase (default $45; plumbing, electrical, HVAC at $65). DIY defaults: insulation, interior finish, final. Plumbing, electrical, and HVAC rows carry a hint that some states require a licensed trade, linking to the state guide.

### 2.8 Totals

`Estimate.totals = { materials, hiredLabor, ownLabor, soft, cash, allHired, contingency, perSqFt, hours, nDiy }`, each dollar figure `{ low, mid, high }`. The ledger shows rounded mids; the rail shows the likely range under the headline; the FAQ cites mids.

### 2.9 Tests

- Golden values per phase for the 2,000 sq ft, one-story, slab, standard, NC default (hand-checked once, then snapshotted).
- Properties: every total is monotonic in heated sq ft; no line has qty ≤ 0; DIY never raises cash; the measured Thompson fixture (`fixtures/thompson-geometry.json`, from the partner endpoint) produces the same ledger on every run.
- The free default must land within 10% of today's W-02 shell total for the shell phases, so the FAQ's cited numbers move deliberately, not accidentally.

## 3. Workstream W3 — the page

### 3.1 Files

```
src/app/calculators/material-estimator/page.tsx      server shell: metadata, FAQ schema, static sections
src/components/estimate/
  Estimator.tsx            client: state, URL sync, engine call, layout grid
  ProfileChips.tsx         the input chips (free state) / plan facts (measured state)
  Ledger.tsx LedgerRow.tsx the phase rows, bars, who-does-it switch, expanded lines
  Rail.tsx                 cash to build, split bar, contingency, plans card / measured card / upgrade card
  StickyStrip.tsx          phone-only pinned total
  AttachPanel.tsx          upload + three setup questions + email → checkout
  ReadingStatus.tsx        polling strip ("Reading sheet 4 of 12")
src/styles/Estimate.module.css
```

Fonts: `Instrument_Serif` and `Instrument_Sans` from `next/font/google`, loaded in the page and scoped by CSS variables on the page root, so the rest of the site keeps Fraunces and Hanken Grotesk.

### 3.2 Anatomy (Direction D)

Desktop: site header; title block (serif H1 "Your house, costed." + profile chips, or "{Plan name}, costed." + facts with sheet tags); a two-column grid: the ledger (phase rows: name + note, share-of-cost bar drawn to the same scale as the rail's bar, cost, Hire it / Do it myself) and a sticky right rail (cash to build, split bar and legend, contingency, then the plans card or the measured card plus the upgrade card). Below the ledger: cash-to-build footer row and fine print. Phone (container ≤ 900 px): rail first, then ledger; the sticky strip pins the total; rows collapse to name + cost with bar and switch beneath; the attach panel is full width and appears after the first estimate, never before it.

### 3.3 Page states

`free` → `attaching` (panel open) → `checkout` (redirect to Stripe) → `reading` (polling) → `measured`, or `unsupported` (refunded, message, back to free). State comes from the URL: `?read=<token>` selects a plan read; `&session_id=` triggers verify once; profile fields live in the query (`sqft, stories, finish, found, state, roof, diy=insul,int,final`) so an estimate is shareable and the state pages can pre-set it. `localStorage` remembers the last profile for convenience only.

### 3.4 Interactions

- Chips and switches recompute instantly; the live region announces the new total, debounced, never per keystroke (keep the pattern from `CalcSheet.tsx`).
- Row name toggles its lines; one row open at a time; framing open by default.
- The split bar's own-hours segment and the DIY-row bar segments are the only orange.
- Copy, Print (print stylesheet: ledger and rail only), Download CSV (client-side blob), Send to inbox (the newsletter Worker's `/estimate` endpoint, payload extended with phases and the split).

### 3.5 Analytics (GA4 via `trackEvent`)

`estimate_use` (once per session, with profile), `estimate_toggle` (phase, choice), `estimate_export` (copy | print | csv | email), `plan_read_open` (panel), `begin_checkout` (value 20), `plan_read_verified`, `plan_read_ready`, `studtally_upgrade_click`, and `purchase` on the measured page's first load after verify, deduped per session id like `/shop/success`.

### 3.6 SEO and content

- Title "Cost to Build a House Calculator: Every Phase, Materials and Labor". Description names the DIY switch and the state index.
- Methodology section rewritten phase by phase with the formulas in words; assumptions table generated from `prices.ts` and the profile so it cannot drift; "what this leaves out" shrinks to land, financing, and furniture.
- FAQ answers cite numbers produced by the engine's default run; a test fails if they drift.
- FAQ gains "What does the $79 at StudTally buy?": the framing list only (every stud, plate, header, sheet, and hanger, counted per wall and reviewed), with the other 13 phases staying estimates; and "How big can the plan PDF be?": 100 MB and 40 sheets.
- Keep the field notes and the binder cross-sell. Registry entry stays `material-estimator` (`kind: 'worksheet'`); the hub row copy and the home page's A-06 blurb update. `plan-takeoff` (PT-01) stays as StudTally's front door; `PLAN_TAKEOFF_SLUGS` loses `material-estimator` because the page now carries the flow itself.
- Sitemap: unchanged for this route; M4 adds the state pages.

### 3.6a What M2 built, and where it departs from the sketch

- The ledger bars are scaled so the largest phase fills its track and the others are proportional to it. Drawn at share-of-grand (the canvas's scale) the biggest phase was 17% of the track and the small ones were slivers; the rail's split bar still shows the whole-house split.
- A row's cost cell shows the cash for that phase given the switch (materials only when Do it myself, with "plus about N hours of yours" beneath), so the rows sum to the footer's cash to build. The canvas showed materials plus labor on every row.
- Drywall, paint, and baseboard follow the drywall and paint sheets' heuristics (3.7× and 2.7× floor area) rather than the framing rule's partitions, which doubled board and base; stud counts keep the framing sheet's rule so the two pages agree.
- The free rail's plans card is the StudTally $79 framing-list cross-sell with the §4.5 copy rule, since the $20 attach flow is M3; `PLAN_TAKEOFF_SLUGS` already dropped `material-estimator` because this page carries the card itself.
- The page measures the sticky site header and promo banner on mount and sets `--est-top`, so the phone strip and the rail pin just below them.
- Roof complexity and wall height sit behind a "Roof and wall height" chip; the five main chips match the canvas.
- Default run: $316k every trade hired ($158/sq ft, likely $239k–$392k), $288k with the three default DIY phases. The old W-02 shell-materials subset lands about 10% above the old sheet (foundation concrete, framing, drywall, roofing, flooring, insulation), inside the §2.9 bound.
- Engine tests run with `node --test --experimental-strip-types src/lib/estimate/__tests__/estimate.test.ts`.

### 3.7 Accessibility and performance

Real buttons and labels, 44 px targets, visible focus, `prefers-reduced-motion` respected, 4.5:1 on navy for every text color (`#A9B6C2` muted passes; never lighter). The engine runs in under a millisecond; no debounce on compute, only on announcements and analytics.

## 4. Workstream W4 — plans attached ($20)

### 4.1 Sequence

1. Visitor opens the attach panel: PDF (≤ 100 MB, ≤ 40 sheets; the panel says "PDF up to 100 MB" before the picker, and an oversize file is refused in the browser with its size named), three setup questions (foundation, floor framing, roof framing, each defaulting to "read it from the plan"), email.
2. Browser → BYH downloads Worker `POST /plan-read` (multipart). The Worker validates the PDF header and size, forwards the file to StudTally `POST /api/partner/plans`, receives `{ plan_id, page_count }`, writes a `plan_reads` row with a random 128-bit `token`, creates a Stripe Checkout Session for the `plan-read` price, and returns `{ token, checkout_url }`.
3. Stripe Checkout (account branding). Success URL `/calculators/material-estimator?read=<token>&session_id={CHECKOUT_SESSION_ID}`; cancel URL `?read=<token>&cancelled=1` reopens the panel with the answers intact.
4. The page calls `POST /plan-read/<token>/verify { session_id }`; the Worker asks Stripe, then calls StudTally `POST /api/partner/plans/{id}/paid`, which records the payment and queues the job. Independently the Stripe webhook does the same (first one wins, both idempotent) and sends the "We're reading your plans" email with the results link.
5. The page polls `GET /plan-read/<token>` every 5 s, showing StudTally's progress steps. Jobs take seconds without vision and a few minutes with it; the copy promises "usually within a few hours" and the email covers a closed tab.
6. When StudTally reports `review` or `complete`, the Worker fetches `GET /api/partner/plans/{id}/geometry`, stores the JSON on the `plan_reads` row, emails "Your measured estimate is ready", and the page renders the measured ledger from it. Results outlive StudTally's 90-day purge because the geometry lives in D1.
7. `unsupported`: the Worker refunds the payment intent through Stripe, marks the row, emails the reason, and the page returns to the free state with the message.

### 4.2 Where it lives

Extend `workers/downloads` rather than add a Worker: it already has the Stripe client, signature verification, Resend, D1, the admin dashboard, rate limiting, and the CORS allowlist. New routes `POST /plan-read`, `POST /plan-read/:token/verify`, `GET /plan-read/:token`; new D1 table:

```sql
CREATE TABLE plan_reads (
  token TEXT PRIMARY KEY, plan_id TEXT NOT NULL, email TEXT NOT NULL,
  status TEXT NOT NULL,              -- setup | queued | reading | ready | unsupported | refunded
  session_id TEXT UNIQUE, payment_intent_id TEXT,
  profile_json TEXT, geometry_json TEXT, unsupported_reason TEXT,
  upgrade_code TEXT, upgrade_expires_at TEXT,   -- StudTally's single-use $20-off code for this read
  created_at TEXT NOT NULL, updated_at TEXT NOT NULL
);
```

Secrets: `STUDTALLY_PARTNER_KEY`, `STUDTALLY_API_URL` (`https://api.studtally.com`). The account stays on the Workers Free plan, so 100 MB is the request-body ceiling; the browser checks `file.size` before sending, and the Worker answers 413 with the limit named for anything that slips past.

### 4.3 Stripe

`PRODUCTS['plan-read'] = { sku: 'plan-read', kind: 'service', name: 'Measured Whole-House Estimate', amount: 2000, checkout: 'session' }`. `handleProvisionProducts` creates the product and price and skips the payment link for `checkout: 'session'`; the Worker resolves the price by `metadata.sku` at session time (cached per isolate). Sessions carry `metadata.app = 'buildyourhouse'`, `metadata.sku`, `metadata.plan_id`, `metadata.token`, `client_reference_id = token`, `customer_email`. `isForeignSession` already lets these through; StudTally's webhook answers "not ours" until `/paid` has created its payments row, after which both sides reconcile idempotently. `handleStripeWebhook` gains a `kind === 'service'` branch. `/recover` lists plan reads for an email alongside downloads.

### 4.4 Emails (Resend, from the Worker)

Reading started (link, what happens next, refund promise), estimate ready (link, the headline number, the buyer's $20-off code with one sentence on what the $79 framing list is and is not), could not read (reason, refunded). Subscribe the buyer to the newsletter with `purchased: true` exactly as the shop does.

### 4.5 Upgrade to the framing list

v1: when `/paid` succeeds, StudTally creates a single-use $20-off promotion code for that read (§6.2 of the StudTally doc) and returns it; the Worker stores it on the `plan_reads` row (`upgrade_code`). The ready email and the rail's upgrade card show it with a `utm_content=measured-estimate` link to studtally.com through the existing referral helper in `src/lib/studtally.ts`; the buyer enters the code at StudTally's checkout, which already accepts promotion codes. The code expires with the plan set's 90-day purge window.

Copy rule for the upgrade card, the email, and the FAQ: the card is titled "Framing list, $79, $20 back" and its body says "Every stud, plate, header, sheet and hanger, counted per wall and reviewed by a person. Framing only: the other 13 phases stay estimates." Never "material list" on its own.

v2 (after M3 proves demand): a claim link that attaches the partner plan to the buyer's StudTally workspace on sign-in with the same email, so the $79 flow starts from the job already read instead of a second upload, with the code applied to that session automatically.

### 4.6 Security

Partner key compared constant-time on StudTally; tokens are the only credential for results, like share links; the attach endpoint is rate-limited per IP with the recovery pattern; PDF header and size checked before forwarding; StudTally keeps its own 100 MB / 40-sheet / encrypted-PDF rejections; no plan bytes are stored on the BYH side.

## 5. Workstream W1 — StudTally on Railway and the Claude API

Summary here, runbook in the StudTally doc. Two Railway services from one repo and Dockerfile (`api`: migrations then uvicorn; `worker`: `studtally-worker`), Railway Postgres, R2 for storage (`STORAGE_BACKEND=r2`), `STUDTALLY_VISION=api` with a service-account API key scoped to a StudTally workspace, `api.studtally.com` repointed from the tunnel to the Railway domain so the web Worker, the Stripe webhook URL, and `API_URL` do not change. Rollback is the DNS record.

## 6. Workstream W5 — state pages (M4)

`src/app/calculators/cost-to-build-a-house/[state]/page.tsx` with `generateStaticParams` from `STATE_KITS` (slug = `guideSlug`). Each page is the estimator with `state` pre-set and locked in the H1 ("Cost to build a house in North Carolina"), a state-specific intro (index, permit note, licensed-trade note), the per-state lender module, and the permit-kit cross-sell. Canonical to itself; the hub and `sitemap.ts` list all 50; the state guides link to their page.

## 7. Rollout and measurement

- M2 ships behind the same URL with a one-week watch on `estimate_use`, scroll depth, and the FAQ-driven queries in Search Console; the old page's impressions should hold or rise.
- M3 ships with billing on from day one and Seth's own plan sets as the smoke test. Success metric for the first month: ten paid reads, zero unrefunded unsupported jobs, median time to ready under one hour.
- M4 pages are judged by the state guides' own pattern: impressions by week three.

## 8. Risks

| Risk | Mitigation |
|---|---|
| Measured numbers disagree with the free numbers for the same house by a wide margin | Run both on Thompson in tests; the deltas are the content of the "what changed" line, not a bug, but anything over 2× on a phase gets explained in the note |
| Partial reads (text-free scans, odd sets) | Per-field fallback to derived with honest chips; `unsupported` refunds automatically |
| Plan sets over 100 MB | The panel states the limit up front and the refusal names the file's size; the FAQ suggests exporting the PDF at a lower raster resolution or sending only the architectural sheets |
| Buyer expects the $79 to be a whole-house material list | The copy rule in §4.5; `studtally_upgrade_click` is watched against StudTally refunds in the first month |
| Price table staleness | As-of date on the page; quarterly refresh ritual; FAQ test |
| Worker cold starts on Railway | Services run continuously; the API health check reports `worker_seen_at` |
| Licensed-trade rules differ by state | Hint on the three MEP rows links to the state guide; never a blocker |

## 9. Open items for Seth

Settled 2026-10-13: the account stays on the Workers Free plan and users are told 100 MB is the maximum upload. The profile estimate is free, the plan scan is $20, and the $20 is credited toward the $79 framing list as a single-use code per read, expiring with the 90-day purge window; the upgrade copy always says the $79 buys the framing list, not the whole house.

Still open; neither blocks M1 or M2, and the plan defaults to the first choice in each:

1. Default contingency: 10% as planned, or 15% to match the budget tracker's default.
2. Whether the state index should also move the soft-cost bands (permits and tap fees vary more than materials do).
