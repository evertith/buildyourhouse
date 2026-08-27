#!/usr/bin/env python3
"""WA.2 Permit Application Checklist — Washington Edition.

Every Washington claim was read out of the RCW/WAC text at app.leg.wa.gov in
August 2026 and is cited on-page.

Verified sources:
  RCW 19.27.031(1)      state building code in effect in ALL counties and
                        cities; the model codes adopted (note: UPC, not IPC)
  RCW 19.27.060(1)(a)   a local amendment affecting single-family residential
                        is ineffective unless SBCC-approved
  RCW 19.27.095(1),(2)  vesting on a complete application; required contents
  RCW 19.27.097(1)      evidence of an adequate water supply; the WRIA lists;
                        "an application for a water right shall not be
                        sufficient proof"
  RCW 90.44.050         5,000 gpd permit-exempt domestic baseline
  RCW 90.94.020(5)(f)   3,000 gpd + $500 fee, WRIAs 1/11/22/23/49/55/59
  RCW 90.94.030         950 gpd + $500 fee + on-site stormwater, WRIAs
                        7/8/9/10/12/13/14/15
  RCW 18.08.410(5)      anyone may do the design work for a residential
                        building of up to four dwelling units, any size
  RCW 36.70B.070        28 days to a completeness determination; deemed
                        complete on day 29
  RCW 36.70B.080        65/100/170-day decision clocks; 10%/20% fee refund
  WAC 51-51-003         2021 IRC adopted; electrical sent to ch. 296-46B WAC
                        or the local jurisdiction's electrical code
  WAC 51-51-0313        R313.2 one- and two-family sprinklers NOT adopted
  WAC 51-51-0332        radon: Appendix F in zone 1 counties AND in any house
                        using the R408.3 unvented crawl space method
  WAC 51-11R-30100      Table R301.1 — all 39 counties are 4C or 5B
  WAC 51-11R-40213      Table R402.1.3 — one column for the whole state
  WAC 51-11R-40240      R402.4.1.3.1 — 4.0 ACH50, testing mandatory
  WAC 51-11R-40320      R403.3.5/.6 — duct test and the leakage thresholds
  WAC 51-11R-40350      R403.6.2 — ventilation airflow must be verified
  WAC 51-11R-40620      R406.3 — credits by dwelling size; the drawings must
                        show the options chosen
  WAC 246-272A-0200     septic permit from the local health officer
  WAC 246-272A-0250     when a resident owner may install their own system

Deliberately hedged: septic and critical-areas review are local; the kit names
the rule and the office and leaves the local threshold blank.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

import design as d
import kit as k

S = k.S
CW = k.CW

FORM_ID = "WA.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Application"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Everything a Washington owner-builder gathers, verifies, and files — "
    "with the state-level gates that stop an application cold, and the clocks "
    "the State puts on your reviewer once it is complete.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- gates
flow += k.h2_tight("THE FOUR GATES SET BY STATE LAW")
flow.append(k.body(
    "Most of what your city or county asks for is local. These four are not — "
    "they are conditions Washington law puts on your application, and no "
    "local office can waive them. Clear these before you worry about "
    "anything else."))

flow.append(k.bullet(
    "<b>1. Proof of water.</b> Every applicant for a building permit for a "
    "building needing potable water must \"<i>provide evidence of an adequate "
    "water supply for the intended use of the building</i>.\" In 15 named "
    "water resource inventory areas the proof is defined by rule and comes "
    "with a fee and a withdrawal cap. (RCW 19.27.097(1))"))
flow.append(k.bullet(
    "<b>2. A complete application — which is worth more than an early "
    "one.</b> Completeness is what freezes the rules in your favor and what "
    "starts your reviewer's clock. The statute lists what the application "
    "must contain. (RCW 19.27.095(1), (2); RCW 36.70B.070)"))
flow.append(k.bullet(
    "<b>3. Energy credits shown on the drawings.</b> \"<i>The drawings "
    "included with the building permit application shall identify which "
    "options have been selected and the point value of each option</i>\" — a "
    "submission requirement written into the energy code itself. "
    "(WAC 51-11R-40620, § R406.3)"))
flow.append(k.bullet(
    "<b>4. Your electrical permit is not on this application.</b> The "
    "residential code sends electrical work to a different rule book: "
    "\"<i>Electrical Code is regulated by chapter 296-46B WAC or Electrical "
    "Code as adopted by the local jurisdiction.</i>\" See <b>WA.3</b> and "
    "<b>WA.4</b>. (WAC 51-51-003)"))

flow.append(Spacer(1, 6))
flow.append(k.callout("File complete, not fast — RCW 19.27.095(1)", [
    Paragraph("\"<i>A valid and fully complete building permit application "
              "for a structure, that is permitted under the zoning or other "
              "land use control ordinances in effect on the date of the "
              "application shall be considered under the building permit "
              "ordinance in effect at the time of application, and the zoning "
              "or other land use control ordinances in effect on the date of "
              "application.</i>\"", S["body"]),
    Paragraph("This is Washington's vesting rule, and it is a real "
              "protection: a code change, a fee increase, or a new zoning "
              "overlay that lands after your complete application does not "
              "reach your project. It attaches to <b>completeness</b>, not to "
              "the date you first walked in. An incomplete application buys "
              "you nothing.", S["body"]),
]))

# ---------------------------------------------------------------- A
flow += k.h2_tight("A. SITE AND PROJECT VERIFICATION")
flow += k.check_table("A1: Before anything else", [
    "Confirmed which office issues your building permit — city or town if you "
    "are inside the limits, otherwise the county (see WA.4)",
    "Confirmed separately who issues your <b>electrical</b> permit — L&amp;I, "
    "or a city or county running its own electrical program",
    ("Parcel number and site address confirmed",
     [("Parcel #:", 0.55), ("Address:", 0.45)]),
    "Deed recorded in your name — the contractor-registration exemption you "
    "are relying on is an <i>own property</i> exemption",
    ("Zoning, permitted use, and setbacks confirmed in writing",
     [("Front:", 0.25), ("Side:", 0.25), ("Rear:", 0.25), ("Other:", 0.25)]),
    "Critical areas and shoreline jurisdiction checked — wetlands, streams, "
    "steep slopes, geologic hazard, floodplain, and any shoreline designation "
    "under chapter 90.58 RCW. This is the most common cause of a long "
    "Washington permit",
    "Easements, rights-of-way, recorded restrictions, and any HOA or covenant "
    "approval identified — covenants are private, and nobody checks them for "
    "you",
], notes_header="Notes / who confirmed")

# ---------------------------------------------------------------- B
flow += k.h2_tight("B. THE APPLICATION PACKAGE")
flow.append(k.body(
    "For any construction project costing more than <b>$5,000</b>, RCW "
    "19.27.095(2) fixes a minimum content list for the application: the legal "
    "description or tax parcel number and the street address; the property "
    "owner's name, address and phone; <b>the prime contractor's business "
    "name, address, phone and current state contractor registration "
    "number</b>; and either the lender administering interim construction "
    "financing or the firm that issued a payment bond. Those details are then "
    "printed on the permit itself and on the inspection record card posted at "
    "the site."))

flow.append(k.callout(
    "The line that stops owner-builders: \"prime contractor's … registration "
    "number\"", [
        Paragraph("You are exempt from contractor registration on your own "
                  "property, so you have no number to write. This is normal "
                  "and every Washington permit counter has seen it — they "
                  "will have you identify yourself as the owner-builder, and "
                  "many use an owner-builder acknowledgment form for exactly "
                  "this. Ask which form they want <i>before</i> you file, and "
                  "do not leave the box blank without asking.", S["body"]),
        Paragraph("Separately, RCW 19.27.095(5): if the lender or "
                  "payment-bond information is not yet available, you say so, "
                  "the application \"<i>shall be processed forthwith</i>,\" "
                  "and it \"<i>shall not cause the application to be deemed "
                  "incomplete for the purposes of vesting</i>.\"", S["body"]),
    ]))
flow.append(Spacer(1, 6))

flow += k.check_table("B1: Forms and proofs", [
    "Building permit application, completed and signed",
    "Owner-builder acknowledgment / exemption form as your jurisdiction words "
    "it — ask for it by name",
    ("Evidence of adequate water supply attached (see section C)",
     [("Form of evidence:", 1.0)]),
    ("Estimated construction cost stated — this usually sets your fee",
     [("Stated cost: $", 1.0)]),
    "Lender or payment-bond details supplied, or their absence stated in "
    "writing",
    "Separate trade permits identified: plumbing and mechanical from your "
    "building department; <b>electrical from L&amp;I or the local electrical "
    "program</b>",
], notes_header="Notes")

flow += k.check_table("B2: Plans and supporting drawings", [
    "Complete plan sets in the number and format your jurisdiction requires "
    "(most Washington jurisdictions now take digital submission)",
    "Site plan showing property lines, setbacks, building footprint, "
    "driveway, well and septic areas including the <b>reserve area</b>, "
    "critical areas and their buffers, and easements",
    "Foundation plan, floor plans, elevations, wall sections, framing plan",
    ("Energy credit options and their point values shown on the drawings — "
     "required by § R406.3, not optional", [("Credits shown:", 1.0)]),
    ("Local Table R301.2 design criteria obtained and used — ground snow "
     "load, wind, seismic design category, frost depth",
     [("Snow:", 0.25), ("Wind:", 0.25), ("SDC:", 0.25), ("Frost:", 0.25)]),
    "Engineered details where the code needs them — lateral bracing and "
    "hold-downs in the higher seismic categories, trusses, long spans, "
    "retaining walls, steep-slope foundations",
], notes_header="Notes")

flow.append(k.callout("You are allowed to draw your own house", [
    Paragraph("Washington's architect practice act does not reach houses. "
              "RCW 18.08.410 says the chapter shall not prevent \"<i>any "
              "person from doing design work including preparing "
              "construction contract documents and administration of the "
              "construction contract for the erection, enlargement, repair, "
              "or alteration of a structure or any appurtenance to a "
              "structure <b>regardless of size</b>, if the structure is to be "
              "used for a residential building of up to and including four "
              "dwelling units</i>.\"", S["body"]),
    Paragraph("So no architect's stamp is required by the licensing statute, "
              "at any square footage. That is <b>not</b> the same as saying "
              "no engineering is required: where the building code calls for "
              "calculations — and much of western Washington sits in a "
              "seismic design category that does — you still need them. The "
              "distinction is license versus code.", S["body"]),
]))

# ---------------------------------------------------------------- C
flow += k.h2_tight("C. WATER — THE GATE MOST OWNER-BUILDERS TRIP OVER")
flow.append(k.body(
    "If your house needs potable water, you cannot get a building permit "
    "without proving you will have it. Acceptable evidence is \"<i>a water "
    "right permit from the department of ecology, a letter from an approved "
    "water purveyor stating the ability to provide water, or another form "
    "sufficient to verify the existence of an adequate water supply</i>.\" "
    "And one sentence that has cost people a building season: \"<i>An "
    "application for a water right shall not be sufficient proof of an "
    "adequate water supply.</i>\""))

flow.append(k.callout(
    "\"Washington lets you drill a well for 5,000 gallons a day\" — not where "
    "most people build", [
        Paragraph("The often-quoted figure is real: RCW 90.44.050 exempts "
                  "from permitting a groundwater withdrawal \"<i>for single "
                  "or group domestic uses in an amount not exceeding five "
                  "thousand gallons a day</i>,\" plus watering a lawn or "
                  "non-commercial garden up to half an acre. That is the "
                  "statewide baseline.", S["body"]),
        Paragraph("But in <b>15 water resource inventory areas</b> the 2018 "
                  "streamflow-restoration law replaced it. In WRIAs 7 "
                  "(Snohomish), 8 (Cedar-Sammamish), 9 (Duwamish-Green), 10 "
                  "(Puyallup-White), 12 (Chambers-Clover), 13 (Deschutes), 14 "
                  "(Kennedy-Goldsborough) and 15 (Kitsap), a new "
                  "permit-exempt domestic connection is capped at <b>950 "
                  "gallons per day</b> — indoor use for a household, and "
                  "little else — with a <b>$500 fee</b> paid to the "
                  "permitting authority and a requirement to manage "
                  "stormwater on site. In WRIAs 1 (Nooksack), 11 (Nisqually), "
                  "22 (Lower Chehalis), 23 (Upper Chehalis), 49 (Okanogan), "
                  "55 (Little Spokane) and 59 (Colville), the cap is "
                  "<b>3,000 gallons per day</b>, again with the $500 fee. "
                  "That first list is the Puget Sound population — if your "
                  "lot is in one of those basins and your plan assumed 5,000 "
                  "gallons a day and no fee, both halves of the plan are "
                  "wrong.", S["body"]),
    ]))
flow.append(k.cite(
    "RCW 19.27.097(1)(a)–(d); RCW 90.44.050; RCW 90.94.020(5)(f) and "
    "RCW 90.94.030(3). Both caps apply \"<i>until rules have been adopted "
    "that specify otherwise</i>\" — Ecology has been adopting basin rules "
    "since, so <b>confirm the current figure for your WRIA with Ecology or "
    "your permit counter</b>. Additional rules apply in WRIAs 3 and 4 (Skagit) "
    "under chapter 173-503 WAC following <i>Swinomish Indian Tribal Community "
    "v. Department of Ecology</i>, and in WRIAs 37, 38 and 39 (Yakima) where "
    "adjudicated rights govern. Find your WRIA on Ecology's water resources "
    "map at <b>ecology.wa.gov</b>."))

flow += k.check_table("C1: Water supply", [
    ("Water resource inventory area (WRIA) for your parcel identified",
     [("WRIA #:", 0.5), ("Name:", 0.5)]),
    "Determined which applies: public water purveyor, permit-exempt well, or "
    "an existing water right",
    ("If public water: written letter from the purveyor stating ability to "
     "serve obtained", [("Purveyor:", 0.6), ("Date:", 0.4)]),
    "If a well: confirmed whether your WRIA carries a reduced withdrawal cap, "
    "a $500 fee, and a restriction recorded against title — and budgeted all "
    "three",
    "Well driller licensed under chapter 18.104 RCW, and the well report "
    "understood to be part of your permit evidence",
], notes_header="Notes")

# ---------------------------------------------------------------- D
flow += k.h2_tight("D. SEPTIC — YOUR LOCAL HEALTH JURISDICTION, NOT THE "
                   "BUILDING OFFICE")
flow.append(k.body(
    "On-site sewage is permitted and inspected by your <b>local health "
    "officer</b> under a statewide Department of Health rule, on a separate "
    "track and a separate timeline from your building permit. Except for a "
    "minor repair, \"<i>a person proposing the installation … of an OSS, "
    "shall submit an application and obtain a permit from the local health "
    "officer prior to beginning construction</i>.\" The application must "
    "carry the soil and site evaluation, a dimensioned site plan showing both "
    "the initial and the <b>reserve</b> area, and a detailed design bearing "
    "the <b>name, signature and stamp of the designer</b>."))
flow.append(k.body(
    "Two timing facts worth planning around: the local health officer must "
    "<b>respond to an application within 30 days</b>, and the permit's "
    "expiration date \"<i>may not exceed five years from the date of permit "
    "issuance</i>.\" Start the soil evaluation before anything else on this "
    "list — it is the item most likely to change what you can build, or "
    "whether you can build at all."))

flow.append(k.callout("You may be allowed to install it yourself — ask", [
    Paragraph("\"<i>Only installers may construct OSS</i>,\" with one "
              "exception: \"<i>The local health officer <b>may allow</b> the "
              "resident owner of a single-family residence to install the OSS "
              "for that single-family residence</i>\" — except where the "
              "primary and reserve areas are within <b>200 feet of marine "
              "water</b>, within <b>100 feet of surface water</b>, or the "
              "permit meets the Table X standards of WAC 246-272A-0280.",
              S["body"]),
    Paragraph("Note <i>may allow</i>. This is a discretion your health "
              "officer exercises, not a right you hold, and the water "
              "setbacks rule out a great many Puget Sound lots. If you get "
              "permission, the rule then binds you the same way it binds a "
              "professional: follow the approved design, keep it on site, "
              "change nothing without the designer's and the health "
              "officer's prior authorization, be <b>on site at all times "
              "during excavation and construction</b>, and <b>do not cover "
              "the system until the health officer has approved covering "
              "it</b>.", S["body"]),
]))
flow.append(k.cite(
    "WAC 246-272A-0200(2), (4)(a), (4)(f) and WAC 246-272A-0250(1)–(3), "
    "chapter 246-272A WAC (On-site Sewage Systems), read at app.leg.wa.gov "
    "August 2026. The 30-day response duty traces to RCW 70.05.074. "
    "<b>Application forms, fees, and any additional local rules are set by "
    "your local health jurisdiction</b> under WAC 246-272A-0013 — confirm "
    "them there, not here."))

flow += k.check_table("D1: On-site sewage", [
    "Local health jurisdiction for your county identified (see WA.4) — it is "
    "often not the same agency as your building department",
    ("Soil and site evaluation completed", [("By:", 0.6), ("Date:", 0.4)]),
    ("Design prepared and stamped by a licensed designer, or written "
     "permission to prepare your own confirmed with the health officer",
     [("Designer:", 1.0)]),
    "Initial <b>and reserve</b> areas shown on the site plan and consistent "
    "with the house footprint, driveway and well",
    ("Septic permit issued", [("Permit #:", 0.5), ("Expires:", 0.5)]),
    "If installing it yourself: written permission from the health officer, "
    "and the marine/surface water setbacks confirmed not to apply",
    "Pre-cover inspection scheduled, and any operational permit or ongoing "
    "monitoring requirement understood",
], notes_header="Notes")

# ---------------------------------------------------------------- E
flow += k.h2_tight("E. CODE EDITIONS AND ENERGY COMPLIANCE")
flow.append(k.body(
    "Washington's building code is not optional anywhere: \"<i>Except as "
    "otherwise provided in this chapter, there shall be in effect in <b>all "
    "counties and cities</b> the state building code</i>.\" The residential "
    "stack in force is the <b>2021</b> International Residential Code as "
    "adopted and amended by chapter 51-51 WAC, with the energy code in "
    "chapter 51-11R WAC and plumbing in chapter 51-56 WAC. Note that "
    "Washington adopts the <b>Uniform Plumbing Code</b>, not the "
    "International Plumbing Code — buy the right book."))
flow.append(k.cite(
    "RCW 19.27.031(1); WAC 51-51-003, which adopts the 2021 IRC \"<i>provided "
    "that chapters 11 and 25 through 43 of this code are not adopted</i>\" and "
    "sends energy, plumbing and electrical to their own chapters. Washington "
    "runs a three-year adoption cycle (RCW 19.27.031(3)); confirm the edition "
    "your jurisdiction is enforcing before you draw. Verified August 2026."))

flow.append(k.callout("Three things Washington did to the residential code", [
    Paragraph("<b>No sprinkler mandate for your house.</b> The IRC's "
              "one- and two-family sprinkler section is struck: \"<i>R313.2 "
              "One- and two-family dwellings automatic sprinkler systems. "
              "This section is not adopted.</i>\" Townhouse units do require "
              "them — except in townhouse buildings of no more than four "
              "units. (WAC 51-51-0313)", S["body"]),
    Paragraph("<b>Radon control is broader than the map.</b> Appendix F "
              "applies in the high radon potential (zone 1) counties named in "
              "the code's own Table AF101(1) — <i>and</i> \"<i>to all "
              "buildings constructed using the provisions of Section R408.3 "
              "Unvented crawl space compliance method</i>.\" Choose a "
              "conditioned crawl space anywhere in Washington and you have "
              "opted into radon control. (WAC 51-51-0332)", S["body"]),
    Paragraph("<b>Your local design criteria are genuinely local.</b> "
              "\"<i>Additional criteria shall be established by the local "
              "jurisdiction and set forth in Table R301.2.</i>\" Snow load, "
              "wind, seismic design category and frost depth come from your "
              "building department, not from a statewide table. Get them in "
              "writing before you engineer anything. (WAC 51-51-0301)",
              S["body"]),
]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>The energy code is where Washington earns its reputation — and where "
    "the prescriptive table is simpler than you expect.</b> All 39 counties "
    "sit in just two climate zones, <b>4C</b> (marine, west of the Cascades) "
    "or <b>5B</b> (dry, east) — there is no zone 6 in the code's Washington "
    "table. And the prescriptive envelope table has a <b>single column</b>, "
    "headed \"Climate Zone 5 and Marine 4,\" so the numbers are the same "
    "whether you build in Bellingham or Walla Walla."))

env_rows = [
    [k.cellp("Fenestration <i>U</i>-factor"), k.cellp("0.30"),
     k.cellp("0.32 permitted above 4,000 ft elevation (note j)")],
    [k.cellp("Skylight <i>U</i>-factor"), k.cellp("0.50"), k.cellp("")],
    [k.cellp("Ceiling"), k.cellp("R-60"),
     k.cellp("R-38 permitted for single rafter- or joist-vaulted ceilings "
             "where the full depth extends over the top plate (note e)")],
    [k.cellp("Wood frame wall"), k.cellp("R-20+5 or R-13+10"),
     k.cellp("First figure is cavity, second is continuous insulation "
             "(note i)")],
    [k.cellp("Floor"), k.cellp("R-30"), k.cellp("")],
    [k.cellp("Below-grade wall"), k.cellp("R-10/15/21 int + 5TB"),
     k.cellp("R-5 thermal break between floor slab and basement wall "
             "(note c)")],
    [k.cellp("Slab"), k.cellp("R-10, 4 ft"),
     k.cellp("R-10 continuous required under heated slabs (note d)")],
]
flow.append(k.ref_table(
    "WSEC-R Table R402.1.3 — prescriptive minimums, the whole state",
    [k.cellp("Component", bold=True), k.cellp("Requirement", bold=True),
     k.cellp("What the footnote adds", bold=True)],
    env_rows, [1.7 * inch, 1.5 * inch, CW - 3.2 * inch]))
flow.append(k.cite(
    "WAC 51-11R-40213, Table R402.1.3, as amended effective March 15, 2024 "
    "(WSR 24-03-084). <i>R</i>-values are minimums and <i>U</i>-factors are "
    "maximums. This is the prescriptive path only — R405 total building "
    "performance and R407 certified passive house are separate routes with "
    "different paperwork. County climate zones are in WAC 51-11R-30100, "
    "Table R301.1; geography will mislead you, so look yours up rather than "
    "guessing — <b>Skamania is 5B</b> despite sitting on the west side."))

flow.append(k.body(
    "<b>Then the credits.</b> On top of the envelope, every dwelling unit "
    "must \"<i>comply with sufficient options … so as to achieve the "
    "following minimum number of credits</i>\": <b>5.0</b> for a small "
    "dwelling unit (under 1,500 sq ft of conditioned floor area with less "
    "than 300 sq ft of fenestration), <b>8.0</b> for a medium dwelling unit "
    "(everything not otherwise listed), and <b>9.0</b> for a large dwelling "
    "unit (over 5,000 sq ft of conditioned floor area). This is the "
    "requirement that drives heat pumps, heat pump water heaters and better "
    "envelopes into Washington houses, and it is the one to design around "
    "early — the options you pick change your mechanical system, not just "
    "your insulation."))
flow.append(k.cite("WAC 51-11R-40620, § R406.3."))

flow.append(k.callout("Washington makes you pass three tests, not one", [
    Paragraph("<b>1 — Blower door, and there is no visual alternative.</b> "
              "\"<i>The building or dwelling unit shall be tested for air "
              "leakage.</i>\" The limit: \"<i>The maximum air leakage rate "
              "for any dwelling unit <b>under any compliance path</b> shall "
              "not exceed 4.0 air changes per hour</i>,\" at 50 Pa. A signed "
              "written report, with the verified location and a time stamp, "
              "goes to you and to the code official. (§ R402.4.1.2, "
              "§ R402.4.1.3.1)", S["body"]),
    Paragraph("<b>2 — Duct leakage.</b> \"<i>Ducts shall be leak tested.</i>\" "
              "Rough-in: 4.0 cfm per 100 sq ft of conditioned floor area at "
              "25 Pa, or 3.0 if the air handler is not yet installed. "
              "Post-construction: 4.0 cfm per 100 sq ft. Ducts and air "
              "handlers entirely inside the thermal envelope: 8.0 cfm per 100 "
              "sq ft — and <b>ducts in a crawl space do not qualify</b> for "
              "that allowance. (§ R403.3.5, § R403.3.6)", S["body"]),
    Paragraph("<b>3 — Ventilation airflow, the one people forget.</b> "
              "\"<i>Mechanical ventilation systems shall be tested and "
              "verified to provide the minimum ventilation flow rates "
              "required</i>,\" with a signed written report to the code "
              "official. Whole-house mechanical ventilation is required in "
              "the first place. (§ R403.6, § R403.6.2)", S["body"]),
]))
flow.append(k.cite(
    "WAC 51-11R-40240, WAC 51-11R-40320 and WAC 51-11R-40350 — the 2021 "
    "Washington State Energy Code, Residential, effective March 15, 2024. "
    "Book the testing agency early; in rural counties there are few of them "
    "and they set your schedule, not the other way round."))

flow += k.check_table("E1: Energy code", [
    ("Compliance path chosen — prescriptive, total building performance "
     "(R405), or certified passive house (R407)", [("Path:", 1.0)]),
    ("Climate zone for your county looked up in Table R301.1",
     [("Climate zone:", 1.0)]),
    ("Dwelling size category and required credits determined; options chosen "
     "and <b>printed on the drawings with their point values</b>",
     [("Size:", 0.5), ("Credits:", 0.5)]),
    "Insulation, window U-factor and air-sealing details shown on the plans",
    ("All three tests booked — blower door (4.0 ACH50), duct leakage, "
     "ventilation airflow", [("Tester:", 0.6), ("Booked:", 0.4)]),
], notes_header="Notes")

# ---------------------------------------------------------------- F
flow += k.h2_tight("F. WHAT THE STATE GUARANTEES YOU")
flow.append(k.body(
    "Washington gives an applicant more leverage than most states, and almost "
    "none of it is volunteered at the counter. These apply to jurisdictions "
    "planning under the Growth Management Act, which covers most of the "
    "state's population — ask whether yours does."))

flow.append(k.bullet(
    "<b>28 days to tell you whether you are complete.</b> The local "
    "government must give you a written determination that the application is "
    "procedurally complete or say exactly what is missing. If they say "
    "nothing, \"<i>an application shall be deemed procedurally complete on "
    "the 29th day</i>.\" (RCW 36.70B.070(1), (4)(a))"))
flow.append(k.bullet(
    "<b>Then a decision clock.</b> From the determination of completeness: "
    "<b>65 days</b> for a permit needing no public notice, <b>100 days</b> "
    "with notice, <b>170 days</b> with notice and a hearing. Time spent "
    "waiting on <i>you</i> does not count. (RCW 36.70B.080(1)(d), (g))"))
flow.append(k.bullet(
    "<b>Your money back if they miss it.</b> \"<i>When permit time periods … "
    "are not met, a portion of the permit fee must be refunded</i>\" — "
    "<b>10%</b> if the overrun is within 20% of the original period, "
    "<b>20%</b> beyond that. A jurisdiction may instead collect only 80% of "
    "the fee up front and bill the rest if it hits its dates. (RCW "
    "36.70B.080(1)(l))"))
flow.append(k.bullet(
    "<b>Local residential amendments need State approval.</b> \"<i>No "
    "amendment to a code enumerated in RCW 19.27.031 … that affects "
    "single-family or multifamily residential buildings shall be effective "
    "unless the amendment is approved by the building code council.</i>\" If "
    "you are told a local rule requires something the State code does not, "
    "you may ask whether the Council approved it. (RCW 19.27.060(1)(a))"))
flow.append(k.cite(
    "The refund provision does not apply to a jurisdiction that has "
    "implemented at least three of the process options in RCW 36.70B.160(1) — "
    "ask which applies to yours. Excluded from the clock: time waiting on "
    "requested information, an applicant-requested suspension, environmental "
    "impact statement preparation, and appeal periods (RCW 36.70B.080(1)(g)). "
    "Verified August 2026."))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Application filed:", 0.5),
                         ("Determined complete:", 0.5)]))
flow.append(d.FillInRow([("Decision due:", 0.5), ("Permit #:", 0.5)]))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 4))
flow.append(k.sources_table([
    ("State building code is in effect in all counties and cities; the "
     "adopted model codes include the Uniform Plumbing Code",
     "RCW 19.27.031(1)"),
    ("A local amendment affecting single-family residential is ineffective "
     "unless approved by the State Building Code Council",
     "RCW 19.27.060(1)(a)"),
    ("A complete application vests to the ordinances in effect on the "
     "application date", "RCW 19.27.095(1)"),
    ("Application contents over $5,000, including the prime contractor's "
     "registration number; missing lender/bond data does not break vesting",
     "RCW 19.27.095(2), (5)"),
    ("Evidence of an adequate water supply required; a water right "
     "application is not sufficient proof; the WRIA lists",
     "RCW 19.27.097(1)"),
    ("Permit-exempt domestic groundwater baseline of 5,000 gallons per day",
     "RCW 90.44.050"),
    ("Reduced caps and a $500 fee: 3,000 gpd in WRIAs 1, 11, 22, 23, 49, 55, "
     "59; 950 gpd plus on-site stormwater in WRIAs 7, 8, 9, 10, 12, 13, 14, "
     "15", "RCW 90.94.020(5)(f); 90.94.030(3)"),
    ("Anyone may do the design work for a residential building of up to four "
     "dwelling units, regardless of size", "RCW 18.08.410(5)"),
    ("28 days to a completeness determination, deemed complete on day 29; "
     "then 65/100/170-day decision clocks and the 10%/20% fee refund",
     "RCW 36.70B.070(1), (4)(a); 36.70B.080(1)(d), (l)"),
    ("2021 IRC adopted; electrical regulated by chapter 296-46B WAC or the "
     "local jurisdiction's electrical code", "WAC 51-51-003"),
    ("One- and two-family sprinkler section not adopted; radon Appendix F in "
     "zone 1 counties and in any unvented crawl space house",
     "WAC 51-51-0313; 51-51-0332"),
    ("Local jurisdiction sets Table R301.2 design criteria; all 39 counties "
     "are climate zone 4C or 5B, and one prescriptive envelope column covers "
     "the whole state",
     "WAC 51-51-0301; 51-11R-30100; 51-11R-40213"),
    ("Three mandatory tests: air leakage at 4.0 ACH50 under any compliance "
     "path, duct leakage, and verified ventilation airflow",
     "WAC 51-11R-40240; -40320; -40350"),
    ("Energy credits: 5.0 small, 8.0 medium, 9.0 large; options shown on the "
     "drawings", "WAC 51-11R-40620"),
    ("Septic permit from the local health officer before construction; 30-day "
     "response; permit not to exceed five years", "WAC 246-272A-0200"),
    ("Resident owner may be allowed to install their own system, with water "
     "setback exclusions", "WAC 246-272A-0250"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "wa-permit-kit",
                       "WA.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
