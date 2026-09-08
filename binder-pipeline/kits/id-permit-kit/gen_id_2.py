#!/usr/bin/env python3
"""ID.2 Permit Application Checklist.

Every Idaho claim in this document was read against its primary source in
September 2026 and is cited on-page.

The organizing idea: the code that binds the house is uniform statewide and
mostly set by rule; the one part handed to the county by name is IRC R301
design criteria (snow, frost, wind, seismic). So the document prints every
statewide number it can cite, prints the county's numbers as write-in lines,
and never guesses at a snow load.

Verified sources:
  § 39-4109(1)(b), (3), (4)   IRC edition by Board rule; no amendment more
                        restrictive than ICC; effective 1 January after adoption
  IDAPA 24.39.30.600.03   2018 IRC Parts I, II, III, IX with amendments
                        (7-1-24): R105.2 pools 4 ft, flag poles; R302.6 garage
                        5/8 Type X; R302.13 deleted; R303.4 whole-house
                        ventilation; R313.2 deleted; Table R403.1; R403.1.1;
                        R602.10 APA SR-102 alternate
  IDAPA 24.39.30.600.06   Idaho Table R402.1.2 and R402.1.4 (zones 5, 6);
                        R402.4.1.2 Visual Inspection exception; R402.6 log homes
  § 39-9701(1), (2)     2018 IECC pinned by statute from 1 July 2022; preemption
  § 54-1001             2023 NEC adopted by the Legislature (2023 ch. 244,
                        H0337, effective 1 July 2023)
  IDAPA 24.39.10.600.01   the Idaho amendments (4-4-25) — AFCI bedrooms only,
                        GFCI deletions, SPD and emergency disconnect permissive
  IDAPA 24.39.10.500.01.a.i, .500.02.a, .500.04, .500.06   cover rule; fees
  IDAPA 24.39.20.500.02.a, .500.01.c, .600.21, .600.26   plumbing fees; expiry;
                        42-inch water-service cover; softener loop
  IDAPA 24.39.70.500.02.a, .500.01.c   HVAC fees; expiry
  DOPL Homeowner HVAC Permit fee schedule (rev. 8/17/2022)   Manual S, J & D
                        review $25 on a new dwelling
  DOPL Plumbing FAQ     "2017 Idaho State Plumbing Code (ISPC) based on the
                        2015 Uniform Plumbing Code"
  IDAPA 24.39.30.500.03   DOPL Table 1-A applies to DOPL-issued permits only
  HBUS minutes 17 Feb 2026; Admin. Bulletin Oct 2025 p. 358   Docket
                        24-3930-2502 (2024 I-Codes) rejected
  DOPL bld-statutes-and-rules page   "not currently engaged in rulemaking for
                        2026–2027"
  IDAPA 58.01.03.005.01, .005.08, .006.08.b, .007.08.a, .007.09, .007.18,
  .008.01.a, .008.01.d, .008.02.b-c, .011.03, .011.05   septic
  IDAPA 58.01.14.110    minimum septic fees; districts may differ
  § 42-235, § 42-238(2), (3), (11); § 42-111; § 42-227(1), (4)   wells
  IDAPA 37.03.09.025.01.d, .025.04, .036.03   well separations, casing, 10 ft

DELIBERATELY NOT CLAIMED, and why:
  - Any ground snow load, frost depth or seismic design category. All are IRC
    R301.2 design criteria that § 39-4116(4)(c)(iii) hands to the local
    jurisdiction; no statewide table exists in the Act or the rule.
  - Any local building-permit fee. Every enforcing jurisdiction sets its own by
    ordinance; DOPL's Table 1-A is not a default for a house.
  - The Board's adoption date of the 2018 IRC. Not retrieved; the mechanism
    (1 January after adoption) is printed instead.
  - Processing-time estimates. The only clocks in statute are in ID.3.
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
sec = k.sec
NB = k.NB
CITE = k.CITE_COL

FORM_ID = "ID.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "What to Gather"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The code editions actually in force, the numbers Idaho set itself, the "
    "numbers your county sets, and the fees as the rules write them.")

flow.append(k.disclaimer(
    "Every fee here is a state rule figure or a figure printed on DOPL's own "
    "form, with its date. Local building-permit fees are not printed because "
    "each enforcing city and county sets its own — ask for the fee ordinance "
    "with the permit-process document."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- editions
flow += k.h2_tight("THE CODE EDITIONS ACTUALLY IN FORCE", reserve=2.2)
flow.append(k.body(
    "Two of these are set by statute and can only move by a bill. The rest are "
    "set by Board rule — and Idaho's rules face legislative review, which is "
    "how the last update died. See the box after the table."))
rows = [
    [k.cellp("<b>Residential building</b>"),
     k.cellp("<b>2018 International Residential Code, Parts I, II, III and "
             "IX</b>, with Idaho amendments. Parts IV–VIII (energy, "
             "mechanical, fuel gas, plumbing, electrical) are excluded by "
             "statute and covered by the codes below. ICC sells it as the "
             "\"2020 Idaho Residential Code\" — same 2018 base"),
     k.cellp(f"IDAPA 24.39.30.600.03; {sec('39-4109(1)(b)')}")],
    [k.cellp("<b>Energy</b>"),
     k.cellp("<b>2018 IECC</b> with Idaho amendments, <b>fixed by statute</b> "
             "from 1&#160;July 2022 and preempting every local government"),
     k.cellp(f"{sec('39-9701(1)')}; IDAPA 24.39.30.600.06")],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("<b>2023 National Electrical Code</b>, \"hereby adopted by the "
             "Idaho legislature\" (effective 1&#160;July 2023) — and "
             "<b>amended downward</b> by the Electrical Board. See the "
             "trap below"),
     k.cellp(f"{sec('54-1001')}; IDAPA 24.39.10.600")],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp("<b>2015 Uniform Plumbing Code</b> with Idaho amendments — "
             "DOPL calls it the \"2017 Idaho State Plumbing Code (ISPC) "
             "based on the 2015 Uniform Plumbing Code.\" Not the IPC"),
     k.cellp(f"IDAPA 24.39.20.600; {sec('54-2601')}")],
    [k.cellp("<b>Mechanical, fuel gas</b>"),
     k.cellp("<b>2018 International Mechanical Code</b>, <b>2018 "
             "International Fuel Gas Code</b>, and 2018 IRC Parts V and VI"),
     k.cellp(f"IDAPA 24.39.70.600; {sec('54-5001')}")],
    [k.cellp("<b>Fire sprinklers</b>"),
     k.cellp("<b>Not required</b> in one- and two-family dwellings — by "
             "statute, binding on every local government; R313.2 deleted "
             "from the Idaho code"),
     k.cellp(f"{sec('39-4116(3)')}; IDAPA 24.39.30.600.03.j")],
]
flow.append(k.ref_table(
    "What binds a house in Idaho, September 2026",
    [k.cellp("Trade", bold=True), k.cellp("Code and edition", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.35 * inch, CW - 1.35 * inch - CITE, CITE]))
flow.append(k.cite(
    f"<b>How an edition changes.</b> The IRC and IBC editions are whatever the "
    f"Idaho Building Code Board adopts by rule; \"any edition of the building "
    f"codes adopted by the board will take effect on January 1 of the year "
    f"following its adoption\" ({sec('39-4109(4)')}). The <b>energy</b> code "
    f"edition is in the statute itself ({sec('39-9701(1)')}), as is the "
    f"<b>NEC</b> edition ({sec('54-1001')}); only a bill moves either. And "
    f"a ceiling on every residential amendment: none \"shall be made by the "
    f"Idaho building code board that provide for standards that are more "
    f"restrictive than those published by the International Code Council\" "
    f"({sec('39-4109(3)')}). Every Idaho residential amendment loosens or "
    f"clarifies; none tightens."))

flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "The 2024 update was rejected — and nothing is scheduled to replace it", [
        Paragraph("DOPL proposed the 2024 I-Codes in Docket 24-3930-2502 "
                  "(Idaho Administrative Bulletin, 1&#160;October 2025, "
                  "p.&#160;358). On <b>17&#160;February 2026</b> the House "
                  "Business Committee's minutes record: \"MOTION: Rep. "
                  "Thompson made a motion to <b>reject Docket No. "
                  "24-3930-2502</b> due to the many concerns and questions "
                  "regarding the proposed changes in addition to the "
                  "incorporation by reference of the international code. "
                  "Speaking to the motion, Rep. Crane (13) expressed his "
                  "support of the motion, noting the need to create an Idaho "
                  "Building Code.\" A substitute motion to hold the docket "
                  "failed; the motion to reject \"carried by voice vote.\"",
                  S["body"]),
        Paragraph("DOPL's Building statutes-and-rules page, September 2026: "
                  "\"These boards are not currently engaged in rulemaking for "
                  "2026–2027. Existing rules remain in effect.\" So the "
                  "<b>2018 IRC, IBC and IECC remain in force</b>, the rule "
                  "paragraphs carry 7-1-24 dates, and no successor edition "
                  "has a date. The committee's minuted questions — whole-house "
                  "ventilation, sealing of registers, garage heat detectors, "
                  "\"blower door test frequency\" — are a preview of the next "
                  "fight. Confirm the edition printed on your permit.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- NEC trap
flow += k.h2_tight("THE ELECTRICAL TRAP — A 2023 NEC AMENDED DOWNWARD",
                   reserve=2.4)
flow.append(k.body(
    "A reader wiring to the national 2023 book will install AFCI on every "
    "circuit, a whole-house surge device and an outdoor emergency disconnect "
    "that Idaho does not require. A reader on a stale 2017 or 2020 book will "
    "miss Idaho's own island-receptacle rule. Either way, the table matters. "
    "All rows are IDAPA 24.39.10.600.01, effective 4&#160;April 2025."))
rows = [
    [k.cellp("<b>210.12(B) — AFCI</b>"),
     k.cellp("\"Shall apply in full. Exception: In one- and two-family "
             "dwelling units, Arc-Fault Circuit-Interrupter Protection shall "
             "only apply to all branch circuits and outlets supplying "
             "<b>bedrooms</b>. All other locations in such units are "
             "exempt\""),
     k.cellp("<b>AFCI = bedrooms only</b>")],
    [k.cellp("<b>210.8(A) — GFCI, general</b>"),
     k.cellp("\"Delete reference to 250-volt receptacles\"; (5) replaced with "
             "\"Unfinished areas of basements\"; (7) food-prep areas "
             "<b>deleted</b>; (8) sinks confined to areas other than "
             "kitchens; (11) laundry areas <b>deleted</b>. (6) Kitchens is "
             "<i>not</i> amended"),
     k.cellp("Kitchen receptacles stay GFCI; laundry, wet bar, finished "
             "basement and 250-V do not")],
    [k.cellp("<b>210.8(D), 422.5(A)(7) — appliances</b>"),
     k.cellp("In dwelling units, list items (7) dishwashers, (8) ranges, (9) "
             "wall ovens, (10) cooktops, (11) clothes dryers, (12) microwaves "
             "<b>deleted</b>"),
     k.cellp("No appliance-specific GFCI")],
    [k.cellp("<b>210.8(F) — outdoor outlets</b>"),
     k.cellp("List items (1) garages at or below grade and (2) accessory "
             "buildings <b>deleted</b>"),
     k.cellp("Garage and outbuilding outdoor outlets drop out")],
    [k.cellp("<b>215.18, 225.42, 230.67 — surge</b>"),
     k.cellp("For dwelling units a surge protection device \"shall be "
             "<b>permitted</b>\"; the requiring list item deleted"),
     k.cellp("<b>SPD not required</b>")],
    [k.cellp("<b>225.41, 230.85 — emergency disconnect</b>"),
     k.cellp("For one- and two-family dwellings \"shall be <b>permitted</b>\"; "
             "230.85(C) deleted"),
     k.cellp("<b>Outdoor emergency disconnect not required</b>")],
    [k.cellp("<b>210.52(C) — islands</b>"),
     k.cellp("New item (4): island and peninsula receptacles, \"if "
             "installed,\" may be mounted not more than 12&#160;in below the "
             "countertop, not where the overhang exceeds 6&#160;in"),
     k.cellp("Island receptacles optional; below-counter allowed")],
    [k.cellp("<b>210.52(E)(3) — decks</b>"),
     k.cellp("Balconies, decks and porches of <b>20&#160;sq&#160;ft or "
             "more</b> accessible from inside need one receptacle, not more "
             "than 6½&#160;ft above the surface"),
     k.cellp("Small decks exempt")],
    [k.cellp("<b>314.27(C) — fan boxes</b>"),
     k.cellp("Second paragraph deleted"),
     k.cellp("No fan-rated box required at every habitable-room ceiling "
             "outlet")],
    [k.cellp("<b>334.15(C) — NM cable</b>"),
     k.cellp("May be secured to the bottom edge of joists in crawl spaces "
             "not over 4.5&#160;ft high"),
     k.cellp("Crawl-space wiring eased")],
]
flow.append(k.ref_table(
    "Idaho amendments to the 2023 NEC that change a house",
    [k.cellp("Section", bold=True), k.cellp("Idaho action", bold=True),
     k.cellp("Effect", bold=True)],
    rows, [1.55 * inch, (CW - 1.55 * inch) * 0.6, (CW - 1.55 * inch) * 0.4]))
flow.append(k.cite(
    "Rules of the Idaho Electrical Board, IDAPA 24.39.10, at "
    "adminrules.idaho.gov. Also in the same chapter: \"No wiring or equipment "
    "may be concealed in any manner from access or sight until the work has "
    "been inspected and approved for cover by the electrical inspector\" "
    "(500.01.a.i), and \"all electrical permits shall be purchased before "
    "work is commenced\" (500.01.a). Off-grid: rapid-shutdown relief for "
    "buildings 1,000&#160;ft or more from utility lines and for detached "
    "PV-only structures (690.12 as amended); lead-acid battery systems need "
    "no ESS listing (706.5). <b>Where a city or county runs its own electrical "
    "program, the Idaho electrical code is still the standard by "
    f"statute</b> ({sec('54-1001B(1)(a)')})."))

# ---------------------------------------------------------------- energy
flow += k.h2_tight("THE ENERGY CODE — PINNED BY STATUTE, PREEMPTING EVERY COUNTY",
                   reserve=2.4)
flow.append(k.body(
    f"\"On and after July 1, 2022, the Idaho state energy code shall be the "
    f"2018 international energy conservation code, as amended … by the Idaho "
    f"building code board and approved by the legislature\" "
    f"({sec('39-9701(1)')}). And the preemption: \"The provisions of this "
    f"chapter <b>preempt, eliminate, and prohibit</b> any cities, counties … "
    f"or any other local governmental entities of any kind from adopting "
    f"energy code or energy-related requirements … that differ from or are "
    f"more extensive than the requirements of the Idaho energy conservation "
    f"code\" ({sec('39-9701(2)')}) — applying to local codes adopted "
    f"\"prior to, on, or after July 1, 2022\" ((3)). <b>Nobody may add to "
    f"this table.</b> Idaho deleted the model code's Zone 5 and Zone 6 rows "
    f"and wrote its own:"))
rows = [
    [k.cellp("Fenestration U-factor"), k.cellp("<b>0.32</b>", center=True),
     k.cellp("<b>0.30</b>", center=True)],
    [k.cellp("Skylight U-factor"), k.cellp("0.55", center=True),
     k.cellp("0.55", center=True)],
    [k.cellp("Glazed fenestration SHGC"), k.cellp("NR", center=True),
     k.cellp("NR", center=True)],
    [k.cellp("<b>Ceiling</b>"), k.cellp("<b>R-38</b>", center=True),
     k.cellp("<b>R-49</b>", center=True)],
    [k.cellp("<b>Wood-frame wall</b>"), k.cellp("<b>R-20, or 13+5</b>", center=True),
     k.cellp("<b>R-22, or 13+5</b>", center=True)],
    [k.cellp("Mass wall"), k.cellp("13/17", center=True),
     k.cellp("15/20", center=True)],
    [k.cellp("Floor"), k.cellp("R-30", center=True),
     k.cellp("R-30", center=True)],
    [k.cellp("Basement wall"), k.cellp("15/19", center=True),
     k.cellp("15/19", center=True)],
    [k.cellp("Slab R-value and depth"), k.cellp("R-10, 2&#160;ft", center=True),
     k.cellp("R-10, 4&#160;ft", center=True)],
    [k.cellp("Crawl-space wall"), k.cellp("15/19", center=True),
     k.cellp("15/19", center=True)],
]
flow.append(k.ref_table(
    "Idaho Table R402.1.2 — insulation and fenestration by component "
    "(IDAPA 24.39.30.600.06.b)",
    [k.cellp("Component", bold=True),
     k.cellp("Climate Zone 5", bold=True, center=True),
     k.cellp("Climate Zone 6", bold=True, center=True)],
    rows, [CW - 3.2 * inch, 1.6 * inch, 1.6 * inch]))
flow.append(k.cite(
    "Equivalent U-factors, Idaho Table R402.1.4 (600.06.d): Zone 5 ceiling "
    "0.030, frame wall 0.060, floor 0.033; Zone 6 ceiling 0.026, frame wall "
    "0.057. Every Idaho county is Zone 5 or Zone 6 under IECC Table R301.1 — "
    "look yours up in the model code, not in an Idaho amendment. Note the "
    "Zone 6 wall row: <b>R-22 or 13+5</b>, against the model code's 20+5 or "
    "13+10 — a reduction, as the statute requires. Guides printing R-49 "
    "ceilings in Zone 5, R-38 floors, U-0.30 windows in Zone 5, or an "
    "\"R-20+5\" wall option are printing the model code, not Idaho's."))

flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "No blower door unless you choose one — and one ventilation rule you "
    "cannot skip", [
        Paragraph("Idaho adds an exception to R402.4.1.2: \"<b>Visual "
                  "Inspection.</b> The Permit Holder will determine <b>at the "
                  "time of permit application</b> the method of determining "
                  "building envelope tightness. A visual inspection shall be "
                  "considered acceptable in lieu of testing when the items "
                  "listed in Table R402.4.1.1, applicable to the method of "
                  "construction, are field verified\" (600.06.e). The choice "
                  "is yours and it is made on the application. If you choose "
                  "testing, the unamended 2018 figure of 3 air changes per "
                  "hour at 50 pascals applies.", S["body"]),
        Paragraph("The other direction: Idaho replaced R303.4 so that "
                  "\"Dwelling units <b>shall be provided with whole-house "
                  "mechanical ventilation</b> in accordance with Section "
                  "M1505.4\" (600.03.h) — mandatory, not tied to an "
                  "air-leakage threshold. Design the ventilation system in; "
                  "an exhaust fan on a timer is the usual minimum.", S["body"]),
        Paragraph("Log homes have their own Table R402.6 (600.06.f–g): an "
                  "8-inch minimum average log with R-49 ceiling and R-30 "
                  "floor in both zones, or a 5-inch log with high-efficiency "
                  "equipment. REScheck and R405 simulated performance remain "
                  "available as alternatives.", S["body"]),
    ]))

# ---------------------------------------------------------------- county numbers
flow += k.h2_tight("WHAT THE COUNTY SETS — AND THE NUMBERS IDAHO WROTE ITSELF",
                   reserve=2.4)
flow.append(k.body(
    f"The Act lets a local government amend, by ordinance, IRC \"Section R301, "
    f"Design Criteria\" ({sec('39-4116(4)(c)(iii)')}). That is the section "
    f"that carries ground snow load, frost depth, wind speed, seismic design "
    f"category, weathering and flood hazard. <b>No statewide value for any of "
    f"them exists in the Act or in IDAPA 24.39.30</b> — a guide that prints "
    f"a snow-load table by county is printing something no Idaho rule "
    f"contains. Ask the building official for the adopted values, or for the "
    f"site-specific study the ordinance requires, and write them here:"))
flow += k.check_table(
    "My jurisdiction's R301 design criteria, as told to me",
    [
        ("Ground snow load, and whether a site-specific study is required:",
         [("psf", 0.3), ("Study?", 0.3), ("Who told me", 0.4)]),
        ("Frost depth for footings:", [("Inches", 0.3), ("Who told me", 0.7)]),
        ("Seismic design category and ultimate design wind speed:",
         [("SDC", 0.3), ("Wind mph", 0.3), ("Who told me", 0.4)]),
        ("In a mapped flood hazard area?", [("Yes / No", 0.4), ("Source", 0.6)]),
    ])
flow.append(k.body(
    "<b>What Idaho did write into the residential code</b>, uniform statewide "
    "unless your county has run the good-cause hearing:"))
rows = [
    [k.cellp("<b>Footings</b>"),
     k.cellp("Idaho Table R403.1 replaces the model tables: 1-story "
             "light-frame footing width <b>12&#160;in</b> at every soil "
             "value; 2-story 15&#160;in at 1,500&#160;psf, 12&#160;in from "
             "2,000&#160;psf up; spread footings <b>at least 6&#160;in "
             "thick</b>"),
     k.cellp("600.03.n–p")],
    [k.cellp("<b>Garage separation</b>"),
     k.cellp("Table R302.6 replaced: <b>⅝-in Type X</b> gypsum on the garage "
             "side for the residence, attics, habitable rooms above and the "
             "supporting structure"),
     k.cellp("600.03.f")],
    [k.cellp("<b>Floor membrane</b>"),
     k.cellp("R302.13 (fire protection of floors) <b>deleted</b> — no "
             "gypsum membrane under I-joists"),
     k.cellp("600.03.g")],
    [k.cellp("<b>Wall bracing</b>"),
     k.cellp("R602.10, or R602.12 where applicable, \"or the most current "
             "edition of APA System Report SR-102 as an alternate method\""),
     k.cellp("600.03.q")],
    [k.cellp("<b>Windborne debris</b>"),
     k.cellp("R301.2.1.2 protection of openings — deleted"),
     k.cellp("600.03.d")],
    [k.cellp("<b>Permit exemptions</b>"),
     k.cellp("R105.2 kept, with pools exempt to <b>4&#160;ft</b> deep (not "
             "24&#160;in) and \"11. Flag poles\" added. Part I is locally "
             "amendable — confirm"),
     k.cellp("600.03.b–c")],
    [k.cellp("<b>Water service depth</b>"),
     k.cellp("The one statewide burial number: \"The cover must be not less "
             "than <b>forty-two (42) inches</b> below grade\" — a plumbing "
             "rule, not a frost depth"),
     k.cellp("IDAPA 24.39.20.600.21")],
    [k.cellp("<b>Softener loop</b>"),
     k.cellp("Every new one- or two-family residence \"built slab on grade "
             "or that will have a finished basement at the time of final "
             "inspection must have a pre-plumbed water softener loop\": one "
             "hot soft, one cold soft and one cold hard line at the kitchen "
             "sink; irrigation hose bibbs on hard water"),
     k.cellp("IDAPA 24.39.20.600.26")],
]
flow.append(k.ref_table(
    "Idaho's own numbers — IDAPA 24.39.30.600.03 unless noted",
    [k.cellp("Subject", bold=True), k.cellp("Idaho text", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.4 * inch, CW - 1.4 * inch - CITE, CITE]))
flow.append(k.cite(
    "Other plumbing amendments a house hits (IDAPA 24.39.20.600): "
    "underground drainage and vent piping at least 2&#160;in (600.30); "
    "building sewer 4&#160;in from the connection to inside the foundation "
    "(600.39); air admittance valves allowed only on island sinks in new "
    "residential construction, never in attics, crawl spaces or bathroom "
    "groups (600.46); sidewall venting expressly acceptable on cabins and log "
    "homes (600.44.a); no water-hammer arrestors required residentially "
    "(600.23). Mechanical (IDAPA 24.39.70.600.03): gas piping test at "
    "20&#160;psig for 20 minutes; dryer duct supported every 4&#160;ft with "
    "no protruding fasteners."))

# ---------------------------------------------------------------- fees
flow += k.h2_tight("THE TRADE PERMIT FEES, AS THE RULES SET THEM", reserve=2.4)
flow.append(k.body(
    "These are DOPL's fees and apply wherever DOPL issues the permit. A city "
    "or county running its own program sets its own. Electrical and plumbing "
    "use the same ladder, measured on <b>living space</b> — which the "
    "plumbing worksheet defines to include an unfinished basement."))
rows = [
    [k.cellp("Up to 1,500&#160;sq&#160;ft of living space"),
     k.cellp("$130", center=True), k.cellp("$130", center=True)],
    [k.cellp("1,501 to 2,500&#160;sq&#160;ft"),
     k.cellp("$195", center=True), k.cellp("$195", center=True)],
    [k.cellp("2,501 to 3,500&#160;sq&#160;ft"),
     k.cellp("$260", center=True), k.cellp("$260", center=True)],
    [k.cellp("3,501 to 4,500&#160;sq&#160;ft"),
     k.cellp("$325", center=True), k.cellp("$325", center=True)],
    [k.cellp("Over 4,500&#160;sq&#160;ft"),
     k.cellp("$325 + $65 per additional 1,000&#160;sq&#160;ft or part",
             center=True),
     k.cellp("$325 + $65 per additional 1,000&#160;sq&#160;ft or part",
             center=True)],
    [k.cellp("Includes"),
     k.cellp("\"associated buildings with wiring being constructed on each "
             "property\"", center=True),
     k.cellp("\"all buildings with plumbing systems being constructed on "
             "each property\"", center=True)],
]
flow.append(k.ref_table(
    "New one-family dwelling — electrical (IDAPA 24.39.10.500.02.a.i) and "
    "plumbing (IDAPA 24.39.20.500.02.a)",
    [k.cellp("Living space", bold=True),
     k.cellp("Electrical", bold=True, center=True),
     k.cellp("Plumbing", bold=True, center=True)],
    rows, [CW - 3.6 * inch, 1.8 * inch, 1.8 * inch]))

flow.append(Spacer(1, 2))
rows = [
    [k.cellp("Base permit"), k.cellp("<b>$100</b>", center=True)],
    [k.cellp("Furnace, heat pump, air conditioner, boiler, mini-split, "
             "free-standing solid-fuel stove, gas fireplace or similar "
             "appliance, including its ducts, vents and flues"),
     k.cellp("$30 first, $15 each additional", center=True)],
    [k.cellp("Exhaust or ventilation duct — dryer, range hood, bath fan and "
             "similar"),
     k.cellp("$15 first, $5 each additional", center=True)],
    [k.cellp("Fuel gas piping"), k.cellp("$5 per appliance outlet", center=True)],
    [k.cellp("Hydronic system"), k.cellp("$5 per zone", center=True)],
    [k.cellp("<b>Manual S, J and D review</b> — \"required when installing "
             "the primary heating and/or cooling system in a NEW single or "
             "two-family dwelling\""),
     k.cellp("<b>$25</b> — on the DOPL homeowner form, not in the rule "
             "table", center=True)],
]
flow.append(k.ref_table(
    "Residential HVAC (IDAPA 24.39.70.500.02.a; DOPL Homeowner HVAC fee "
    "schedule rev. 8/17/2022)",
    [k.cellp("Item", bold=True), k.cellp("Fee", bold=True, center=True)],
    rows, [CW - 2.4 * inch, 2.4 * inch]))
flow.append(Spacer(1, 4))
flow.append(k.callout(
    "A worked example, so the arithmetic is not a surprise", [
        Paragraph("A <b>2,200&#160;sq&#160;ft</b> house with a gas furnace "
                  "and an air conditioner, four exhaust ducts (dryer, range "
                  "hood, two bath fans) and three gas outlets. Electrical "
                  "<b>$195</b>. Plumbing <b>$195</b>. HVAC: $100 base + $30 "
                  "furnace + $15 A/C + $15 first duct + $15 for three more + "
                  "$15 gas outlets + $25 Manual J/S/D review = <b>$215</b>. "
                  "<b>$605 in state trade permits</b> — with the electrical "
                  "one including the shop, and the plumbing one including "
                  "every building with plumbing on the lot. Bring the load, "
                  "equipment-selection and duct calculations to the HVAC "
                  "permit; the review line is on the form.", S["body"]),
    ]))
flow.append(k.cite(
    "<b>Around the fees.</b> Every trade permit expires <b>365 days</b> from "
    "purchase (plumbing and HVAC: or last inspection); renewal for one year is "
    "$65 (24.39.10.500.01.c; 24.39.20.500.01.c; 24.39.70.500.01.c). "
    "Reinspection for work not ready, bad directions or an uncorrected notice: "
    "$65 (24.39.10.500.04). Plan check: $65 per hour (24.39.10.500.06). An "
    "extra $65 \"may be assessed if the location is not clearly given\" — the "
    "forms say so. HVAC without a permit: <b>double fee</b>, triple on a "
    f"repeat within 12 months ({sec('54-5017(4)')}). DOPL's FAQ: an "
    "Enforcement Permit for work done without one costs \"double the original "
    "amount.\""))

# ---------------------------------------------------------------- building fee
flow += k.h2_tight("THE BUILDING PERMIT FEE — LOCAL, AND WHY DOPL'S TABLE IS NOT "
                   "YOURS", reserve=2.0)
flow.append(k.body(
    "DOPL publishes a building fee table — Table 1-A in IDAPA 24.39.30.500.03, "
    "$695.63 for the first $100,000 of valuation plus $3.92 per additional "
    "$1,000, with plan review at $100 per hour between 40% and 65% of the "
    "permit fee. <b>It applies only to permits DOPL issues</b> — state "
    "buildings, public schools, modular units. It is not a default for a "
    "house, because there is no default: where a county has adopted a "
    "building code its fee ordinance governs, and where it has not there is "
    "no building permit and no fee. Ask for the fee ordinance together with "
    f"the {sec('39-4117(1)')} permit-process document, and write the answer "
    f"on the record at the end of this document."))

# ---------------------------------------------------------------- septic
flow += k.h2_tight("THE SEPTIC PACKAGE, IN ORDER", reserve=1.8)
flow.append(k.body(
    "DEQ writes the rules (IDAPA 58.01.03, rewritten effective "
    "1&#160;July 2025); Idaho's seven public health districts issue the "
    "permits and do the inspections under a memorandum of understanding with "
    "DEQ. The permit constrains where the house can sit, so it comes before "
    "the footprint is fixed."))
rows = [
    [k.cellp("<b>1</b>", center=True), k.cellp("<b>Site evaluation</b>"),
     k.cellp("A standard drainfield site \"will not exceed twenty percent "
             "(20%)\" slope (008.01.a); \"an acceptable site must be large "
             "enough to construct <b>two (2) complete drainfields</b>,\" each "
             "sized for 100% of the design flow (008.02.c). Test-hole "
             "inspections need <b>48 hours'</b> notice, weekends and "
             "holidays excluded (011.03)")],
    [k.cellp("<b>2</b>", center=True), k.cellp("<b>Installation permit</b>"),
     k.cellp("\"No person may … install any individual or subsurface sewage "
             "disposal system … unless there is a valid installation "
             "permit\" (005.01). Valid <b>two years</b> from issue unless "
             "the permit says otherwise (005.08)")],
    [k.cellp("<b>3</b>", center=True), k.cellp("<b>Who installs</b>"),
     k.cellp("A registered installer — except \"<b>owners installing their "
             "own standard or basic alternative system</b> as described in "
             "the TGM\" need no installer's permit (006.08.b). Complex "
             "systems need a registered complex installer")],
    [k.cellp("<b>4</b>", center=True), k.cellp("<b>Final and as-built</b>"),
     k.cellp("\"<b>No system may receive wastewater</b> until the Director "
             "conducts a final installation inspection and completes "
             "as-built drawings\"; you get the as-built within 30 days "
             "(011.05)")],
]
flow.append(k.ref_table(
    "IDAPA 58.01.03 — the sequence",
    [k.cellp("", bold=True, center=True), k.cellp("Step", bold=True),
     k.cellp("What the rule says", bold=True)],
    rows, [0.35 * inch, 1.45 * inch, CW - 1.8 * inch]))
flow.append(k.cite(
    "<b>Fees</b> (IDAPA 58.01.14.110, minimums — \"designees may adopt "
    "different fees\" and must publish them online): basic or complex system "
    "permit <b>$400</b>; tank only $300; renewal $40. <b>Sizing</b> "
    "(58.01.03.007.09, .007.08.a, .008.02.b): design flow 250&#160;gpd for a "
    "3-bedroom house, ±50&#160;gpd per bedroom; minimum tank <b>1,000 "
    "gallons</b>, +250 per bedroom over four; absorption area = flow ÷ "
    "1.0 / 0.5 / 0.2 gal per sq&#160;ft per day for soil groups A / B / C. "
    "A 3-bedroom house on group B soil: 500&#160;sq&#160;ft of trench "
    "bottom, twice over for the reserve area."))
rows = [
    [k.cellp("<b>Drainfield</b> to a well or other domestic supply"),
     k.cellp("<b>100&#160;ft</b>", center=True), k.cellp("008.01.d")],
    [k.cellp("<b>Drainfield</b> to permanent surface water, soil A / B / C"),
     k.cellp("200 / 125 / 100&#160;ft", center=True), k.cellp("008.01.d")],
    [k.cellp("<b>Drainfield</b> to a basement foundation; to crawl space or "
             "slab"),
     k.cellp("<b>20&#160;ft</b>; 10&#160;ft", center=True),
     k.cellp("008.01.d")],
    [k.cellp("<b>Drainfield</b> or <b>tank</b> to the property line"),
     k.cellp("5&#160;ft", center=True), k.cellp("008.01.d; 007.18")],
    [k.cellp("<b>Septic tank</b> to a private well"),
     k.cellp("<b>50&#160;ft</b>", center=True), k.cellp("007.18")],
    [k.cellp("<b>Septic tank</b> to a dwelling or building"),
     k.cellp("5&#160;ft", center=True), k.cellp("007.18")],
    [k.cellp("<b>Well</b> to any permanent building; to the property line"),
     k.cellp("10&#160;ft; 5&#160;ft", center=True),
     k.cellp("IDAPA 37.03.09.025.01.d")],
]
flow.append(k.ref_table(
    "Separation distances — statewide minimums the health district may "
    "increase",
    [k.cellp("Between", bold=True),
     k.cellp("Minimum", bold=True, center=True),
     k.cellp("IDAPA 58.01.03 unless noted", bold=True)],
    rows, [CW - 1.45 * inch - CITE, 1.45 * inch, CITE]))

# ---------------------------------------------------------------- well
flow += k.h2_tight("IF YOU ARE ON A WELL", reserve=2.0)
rows = [
    [k.cellp("<b>You may not drill it yourself</b>"),
     k.cellp(f"\"It shall be unlawful for any person to drill a well in "
             f"Idaho … without first complying with the provisions of this "
             f"chapter,\" and \"person\" means \"<b>any individual who drills "
             f"or abandons any well for himself or another</b>\" "
             f"({sec('42-238(2)')}, (3)). IDWR: \"All wells must be "
             f"constructed by a well driller with a valid license from "
             f"IDWR\"")],
    [k.cellp("<b>Drilling permit before drilling</b>"),
     k.cellp(f"\"Prior to beginning construction of any well … the driller "
             f"or well owner shall obtain a permit\" — <b>$75</b> for a "
             f"domestic well ({sec('42-235')}). IDWR's rules provide a "
             f"\"Start Card\" — \"an expedited drilling permit process for "
             f"the construction of cold water, single-family residential "
             f"wells\" (IDAPA 37.03.09.010.49)")],
    [k.cellp("<b>No water right needed — usually</b>"),
     k.cellp(f"A domestic well — up to 13,000 gallons per day including "
             f"irrigation of up to half an acre ({sec('42-111(1)')}) — "
             f"needs no water-right permit ({sec('42-227(1)')}). <b>Except</b> "
             f"in a subdivision whose application was filed on or after "
             f"1&#160;July 2025 inside a moratorium, critical ground water "
             f"or ground water management area: there a permit is required "
             f"for anything beyond in-home use and livestock "
             f"({sec('42-227(4)')})")],
    [k.cellp("<b>Driller's report, after</b>"),
     k.cellp(f"Filed with IDWR \"within thirty (30) days following the "
             f"completion of the well\" ({sec('42-238(11)')}). Get a copy — "
             f"it is the well's only record, and IDWR's well-log search "
             f"holds it")],
    [k.cellp("<b>Siting and casing</b>"),
     k.cellp("Casing at least <b>12&#160;in</b> above finished grade "
             "(IDAPA 37.03.09.025.04); afterwards \"the well owner must not "
             "construct or allow construction of any permanent building, "
             "except for buildings to house a well or plumbing apparatus … "
             "closer than <b>ten (10) feet</b>\" (036.03)")],
]
flow.append(k.ref_table(
    "The well sequence",
    [k.cellp("", bold=True), k.cellp("What the statute and rule require",
                                     bold=True)],
    rows, [1.85 * inch, CW - 1.85 * inch]))

# ---------------------------------------------------------------- record
flow += k.h2_tight("PERMIT RECORD — FILL THIS IN AS EACH ONE ISSUES",
                   reserve=1.6)
flow += k.check_table(
    "Every approval on this build",
    [
        ("<b>Septic installation permit</b> from health district No. ___, "
         "or written confirmation of public sewer:",
         [("Number", 0.4), ("Issued", 0.3), ("Expires", 0.3)]),
        ("<b>Septic final inspection</b> passed and as-built received:",
         [("Date", 0.5), ("As-built received", 0.5)]),
        ("<b>IDWR drilling permit</b> and the driller's license number:",
         [("Permit", 0.5), ("Driller license", 0.5)]),
        ("<b>Well driller's report</b> received — due within 30&#160;days:",
         [("Date", 0.5), ("Well tag / log no.", 0.5)]),
        ("<b>Building permit</b>, if one exists where I am building, the "
         "code edition printed on it, and the certificate of occupancy at "
         "the end:",
         [("Number", 0.3), ("Edition", 0.25), ("Expires", 0.2),
          ("CO no.", 0.25)]),
        ("<b>Electrical and plumbing permits</b> — DOPL or local:",
         [("Elec. no.", 0.25), ("Issued", 0.25), ("Plb. no.", 0.25),
          ("Issued", 0.25)]),
        ("<b>HVAC permit</b> — and Manual J/S/D submitted:",
         [("Number", 0.4), ("Issued", 0.3), ("J/S/D in?", 0.3)]),
        ("<b>Envelope method chosen on the application</b> — visual "
         "inspection or blower-door test:", [("Method", 1.0)]),
        ("<b>Zoning approval</b>, <b>floodplain determination</b> and "
         "<b>911 address</b> — all local, all independent of the building "
         "code:",
         [("Zoning ref.", 0.34), ("Flood: in / out", 0.33),
          ("Address", 0.33)]),
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "id-permit-kit",
                       "ID.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
