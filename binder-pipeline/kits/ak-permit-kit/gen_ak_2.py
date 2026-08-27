#!/usr/bin/env python3
"""AK.2 Permit Application Checklist — Alaska.

The organizing problem: in most states this document is "what to put in the
envelope." In Alaska there is frequently no envelope, so the document has to
answer a different question first — what is required of the BUILDING when
nothing is required of the PAPERWORK.

Verified sources for the statewide floor:
  AS 18.70.095(a)      "Smoke detection devices shall be installed and
                       maintained in ALL DWELLING UNITS IN THE STATE" — in a
                       manner approved by the state fire marshal. This is in
                       the STATUTE, so it survives the fact that the fire
                       marshal's REGULATION (13 AAC 50.020) excludes detached
                       1-, 2- and 3-family dwellings and that AS 18.70.080(a)(2)
                       limits the regulatory power to 4+ dwelling units.
                       THE KIT'S HEADLINE TRAP.
  AS 18.70.095(d)(3)   "qualifying dwelling unit" for CO alarms — combustion
                       appliance, attached garage/carport, or adjacent parking
  13 AAC 50.030(b)     NFPA 72-2019 + IBC 907.2.11; battery-only permitted
                       ONLY in buildings built before 1/1/1989 or buildings
                       without commercial power — so a new house on the grid
                       needs hard-wired interconnected alarms
  AS 18.70.100(a)      class B misdemeanor; each 10 days a separate offense
  AS 18.70.100(c)      CO-detector violations are a "violation," not a
                       misdemeanor — do not flatten these two
  8 AAC 70.025(a)      2020 NEC is the state minimum electrical code
  8 AAC 63.010(a)(1)   2018 UPC "to be followed throughout the state"
  AS 18.60.735         under 2,500 population, exempt from the plumbing code
  AS 18.60.705(b)      lead limits — >8.0% in pipe/fittings, >0.2% in solder
                       or flux — prohibited in a residential facility
                       providing water for human consumption
  AS 18.60.200(b)      boiler installation notice. RESOLVED AFTER FIRST DRAFT
                       — an earlier draft printed this as an open question.
                       DOLWD's own Notification of New Boiler Installation
                       scopes the duty to "any commercial or residential (six
                       families) site," so a detached house files nothing. The
                       narrowing is the AGENCY'S, not the statute's; the kit
                       says so.

SEPTIC (Step 2), verified from 18 AAC 72 as rewritten eff. 10/1/2023 and
amended 8/13/2025 — NOTE 72.020, .025 and .035 now read "Repealed," which is
itself printed as a citation trap:
  18 AAC 72.400        may not install a conventional system unless certified
                       under .405 or approved under .410
  18 AAC 72.511(a)-(c) three no-plan-approval routes: certified installer;
                       engineer-designed to 2,500 gpd; APPROVED HOMEOWNER
  18 AAC 72.410; .954(c)  homeowner course + $275; one system per year
  18 AAC 72.511(d)(4)  permafrost / high groundwater knocks you out entirely
  18 AAC 72.100(a)(1)  100 ft well to septic; 72.520(b) 100 ft surface water
                       ("slough" includes swamp, bog or marsh — 72.990(91));
                       72.520(d) 4 ft water table / 6 ft bedrock-permafrost;
                       72.520(c) 50 ft from a >25% slope
  NEGATIVE FINDING     72.520 contains NO property-line or foundation setback.
                       DEC guidance recommends 10 ft; only Anchorage makes it
                       mandatory (AMC 15.65.210B.1). Printed as a negative.
  18 AAC 72.530        150 gpd/bedroom; 1,000 gal tank to 3 bedrooms +250/bdrm;
                       frost cover 2/3/4 ft by region
  18 AAC 72.550        24-hr notification; Documentation of Construction in 90
                       days with 8 photos + $115 (72.955); 72.560 after-the-
                       fact registration needs an engineer-sealed report
  18 AAC 72.225/.240   "Approval to Construct"; certification of construction
  Wells                no state permit (18 AAC 80.005(b) is public systems);
                       11 AAC 93.140(a) well log MANDATORY within 45 days on
                       "a person who constructs the well"; 11 AAC 93.035(b)
                       water-right thresholds; 93.040(d)(1) 500 gpd standard

FINANCING (Step 4) — the chapter that replaced a generic "ask your lender":
  AS 18.56.300(a),(b)  AHFC may not lend on housing begun after 6/30/1992
                       without FIVE named inspections
  AS 46.11.040; 18.56.096(c)  energy standards, construction begun after
                       12/31/1991 — a DIFFERENT date, six months apart
  15 AAC 150.035(a)    2018 IRC + Alaska amendments, expressly for units NOT
                       in a municipality with an approved building code
  15 AAC 155.010       BEES = 2018 IECC + Alaska amendments; 5 Star; 4 ACH50
  AS 18.56.096(a)(3)   owner-builders excepted from the contractor condition
  PUR-101 / PUR-102    rater-only energy certification; recorded inspection
                       summary carrying the Exempt Builder's Certification
  HUD ML 2020-36       permit+CO, or three inspections by an ICC-certified
                       inspector, or three by an architect/structural engineer.
                       The 10-year warranty and 90% LTV were ELIMINATED — do
                       not print them.

Deliberately NOT claimed: any DEC fee, distance or sizing figure not read in
the regulation text; AHFC market share; the 5 Star floor sourced to 15 AAC
155.030(a)(1) (which still reads "four-star plus"); AS 18.56.300(e)(3) for the
code edition (its text still names the Uniform Building Code).
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

FORM_ID = "AK.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "What to Gather"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What to assemble on both Alaska paths — the one where a government "
    "reviews your house, and the far commoner one where none does and the "
    "requirements arrive from somewhere else entirely.")

flow.append(k.disclaimer(
    "Work AK.4 first. Which half of this document applies to you depends on "
    "whether your parcel has a building authority at all."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- two paths
flow += k.h2_tight("TWO PATHS, AND EVERYONE WALKS PART OF BOTH")
flow.append(k.body(
    "Alaska owner-builders divide into two groups, and the division is not "
    "the one people expect. It is not \"regulated\" versus \"unregulated.\" "
    "It is <b>whether a single office assembles the requirements for you</b>. "
    "Where a building department exists, it hands you a list. Where none "
    "does, the requirements do not disappear — they scatter across a state "
    "agency, a federal one, a borough platting office, a utility, and your "
    "lender, and <b>nobody assembles them for you</b>. That is what the rest "
    "of this document is."))

path_rows = [
    [k.cellp("<b>A building department reviews your house</b>"),
     k.cellp("Anchorage, Juneau, Sitka, and a number of cities. You will get "
             "a plan review, a permit, a printed inspection card, and a "
             "certificate of occupancy at the end. Work <b>Steps 1–5</b> "
             "below, then hand the department its own application on top.")],
    [k.cellp("<b>No building department reviews your house</b>"),
     k.cellp("Most of Alaska by land area, and much of it by population — "
             "including large, growing, road-connected communities. There is "
             "no application to file for the dwelling itself. Work "
             "<b>Steps 1–4</b>, and treat <b>Step 2</b> and the statewide "
             "floor below as the requirements they are.")],
]
flow.append(k.ref_table(
    "Which half of this document is yours",
    [k.cellp("Your situation", bold=True),
     k.cellp("What it means for this checklist", bold=True)],
    path_rows, [2.05 * inch, CW - 2.05 * inch]))

# ---------------------------------------------------------------- the floor
flow += k.h2_tight("THE STATEWIDE FLOOR — WHAT BINDS YOU WITHOUT A PERMIT")
flow.append(k.body(
    "These apply to a house in the unorganized borough with no permit, no "
    "plan review and no inspector, exactly as they apply to a house in "
    "Anchorage. None of them is enforced by a building department, which is "
    "why they are so often missed."))

floor_rows = [
    [k.cellp("<b>Smoke and carbon monoxide alarms</b>"),
     k.cellp("Required by statute in <b>every dwelling unit in the state</b>. "
             "See the box below — this one is a criminal statute and it is "
             "the requirement Alaska owner-builders most often do not know "
             "exists."),
     k.cellp("AS 18.70.095; 13 AAC 50.030(b)")],
    [k.cellp("<b>The 2020 National Electrical Code</b>"),
     k.cellp("\"<i>Constitutes the minimum electrical code for the "
             "state.</i>\" Your homeowner exclusion is from the license, not "
             "the code (AK.1). Nobody inspects a single-family house, and "
             "knowing violation is still a misdemeanor."),
     k.cellp("8 AAC 70.025(a); AS 08.40.180")],
    [k.cellp("<b>The 2018 Uniform Plumbing Code</b>"),
     k.cellp("Adopted \"<i>as the minimum plumbing standards to be followed "
             "throughout the state</i>.\" In a community of <b>2,500 or "
             "more</b> it is also inspected by the State; below that the "
             "community is exempt from the chapter."),
     k.cellp("8 AAC 63.010(a)(1); AS 18.60.735")],
    [k.cellp("<b>Lead limits in the water system</b>"),
     k.cellp("Pipe or fittings containing more than <b>8.0 percent</b> lead, "
             "and solder or flux containing more than <b>0.2 percent</b>, are "
             "prohibited in plumbing \"<i>of a residential ... facility that "
             "provides water for human consumption</i>.\" Buy accordingly."),
     k.cellp("AS 18.60.705(b)")],
    [k.cellp("<b>Onsite wastewater</b>"),
     k.cellp("Regulated statewide by the Department of Environmental "
             "Conservation under <b>18 AAC 72</b>, or by the local program "
             "where DEC has delegated it. On most rural parcels this is the "
             "<i>only</i> approval you will need — and the one with the "
             "longest lead time. Step 2."),
     k.cellp("18 AAC 72")],
]
flow.append(k.ref_table(
    "Applies whether or not anyone issues you a permit",
    [k.cellp("Requirement", bold=True),
     k.cellp("What it actually is", bold=True),
     k.cellp("Authority", bold=True)],
    floor_rows, [1.5 * inch, CW - 1.5 * inch - 1.45 * inch, 1.45 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout_long(
    "The requirement that follows you into the empty quarter", [
        Paragraph("Alaska's fire and building regulation is capped by "
                  "statute: the Department of Public Safety may set standards "
                  "for \"<i>buildings used for residential purposes "
                  "containing <b>four or more dwelling units</b></i>\" "
                  "(AS 18.70.080(a)(2)), and the code it adopts excludes "
                  "\"<i>Detached one-, two-, and three-family dwellings</i>\" "
                  "in terms (13 AAC 50.020). Your house is outside the whole "
                  "apparatus. Which is why almost nobody notices the "
                  "sentence sitting fifteen sections away, in the statute "
                  "itself rather than in the regulation:", S["body"]),
        Paragraph("\"<i><b>Smoke detection devices shall be installed and "
                  "maintained in all dwelling units in the state</b>, and "
                  "carbon monoxide detection devices shall be installed and "
                  "maintained in all qualifying dwelling units in the state. "
                  "The smoke detection devices must be of a type and shall be "
                  "installed in a manner approved by the state fire "
                  "marshal.</i>\" (AS 18.70.095(a))", S["body"]),
        Paragraph("<b>All dwelling units in the state.</b> No unit-count "
                  "threshold, no population threshold, no exemption for "
                  "parcels without a building department. And the manner is "
                  "not left to you: the regulation requires compliance with "
                  "<b>NFPA 72-2019</b> and installation \"<i>at a minimum ... "
                  "in accordance with IBC Section 907.2.11</i>,\" then adds "
                  "the sentence that decides what you buy — \"<i>Smoke "
                  "detectors may be <b>solely battery operated</b> when "
                  "installed in <b>existing buildings built before January 1, "
                  "1989</b> or in <b>buildings without commercial "
                  "power</b>.</i>\" A new house on the grid is neither. "
                  "(13 AAC 50.030(b))", S["body"]),
        Paragraph("A <b>qualifying</b> dwelling unit, for the carbon monoxide "
                  "alarms, is one that \"<i>contains or is serviced by a "
                  "carbon-based-fueled appliance or device that produces "
                  "by-products of combustion</i>,\" or \"<i>has an attached "
                  "garage or carport</i>,\" or \"<i>is adjacent to a parking "
                  "space</i>.\" In Alaska that is very nearly every house "
                  "ever built. (AS 18.70.095(d)(3))", S["body"]),
        Paragraph("<b>It is enforced as a crime.</b> A violation of "
                  "AS 18.70.010 — 18.70.100 or a regulation adopted under "
                  "them is a <b>class B misdemeanor</b>, and \"<i>when not "
                  "otherwise specified, each <b>10 days</b> that the "
                  "violation or noncompliance continues is a separate "
                  "offense</i>\" — with the carbon monoxide provision "
                  "carved down to a non-criminal violation. So the one "
                  "construction requirement that reaches every dwelling in "
                  "Alaska is also the only one carrying a criminal penalty, "
                  "and it costs about a hundred dollars to satisfy. "
                  "(AS 18.70.100(a), (c))", S["body"]),
    ]))
flow.append(k.cite(
    "AS 18.70.080(a)(2), AS 18.70.095(a), (d)(3), AS 18.70.100(a), (c); "
    "13 AAC 50.020 (2021 IBC, Section 101.2 Exception 1) and 13 AAC "
    "50.030(b). Read at akleg.gov, August 2026. Hard-wired interconnected "
    "alarms are the practical consequence of IBC 907.2.11 for a new dwelling "
    "with commercial power — confirm the placement schedule against NFPA 72 "
    "and the state fire marshal's guidance before rough-in, because this is "
    "cheap at rough-in and expensive afterwards."))

flow.append(Spacer(1, 4))
flow += k.check_table("Statewide floor — confirm each before you close a wall", [
    "Smoke alarms specified <b>hard-wired and interconnected</b> (battery-only "
    "is permitted only in pre-1989 buildings or buildings without commercial "
    "power) and located per NFPA 72-2019 / IBC 907.2.11",
    "Carbon monoxide alarms specified — your house almost certainly qualifies "
    "if it has any combustion appliance, an attached garage or carport, or an "
    "adjacent parking space",
    "Wiring specified and bought to the <b>2020 NEC</b>",
    ("Plumbing specified to the <b>2018 UPC</b>, and you have established "
     "whether your community is at or above 2,500 population",
     [("Community pop.:", 0.5), ("State inspection? Y/N:", 0.5)]),
    "Pipe, fittings, solder and flux confirmed lead-free to the statutory "
    "limits before purchase",
    "If you are installing a hydronic boiler, you have read the note below — "
    "the state installation notice is scoped to commercial sites and "
    "residential sites of six families or more, so a detached house is "
    "outside it",
], notes_header="Notes / evidence")
flow.append(k.callout(
    "The boiler notice that does not reach a house — and the reason to know "
    "why", [
        Paragraph("Read AS 18.60.200(b) alone and you would file a notice: "
                  "\"<i>A person who installs a boiler or unfired pressure "
                  "vessel <b>shall notify</b> the Department of Labor and "
                  "Workforce Development of the installation, using a form "
                  "provided by the department.</i>\" No residential limit "
                  "appears in it, and AS 18.60.210(b)(2) exempts residential "
                  "heating boilers only from the separate "
                  "periodic-certificate sections.", S["body"]),
        Paragraph("<b>The department's own form settles it the other way.</b> "
                  "Its Notification of New Boiler Installation states that "
                  "the information must be submitted \"<i>within 30 days of "
                  "installation at any commercial or residential (six "
                  "families) site in the State of Alaska</i>.\" A detached "
                  "single-family house is outside that scope, and no notice "
                  "is called for.", S["body"]),
        Paragraph("Worth knowing that the narrowing is <b>the agency's, not "
                  "the statute's</b>. If you install something unusual — a "
                  "pressure vessel, a large system, anything serving more "
                  "than one dwelling — the statutory words are broad enough "
                  "to ask about, and one call is cheaper than a wrong "
                  "assumption.", S["body"]),
    ]))

# ---------------------------------------------------------------- step 1
flow += k.h2_tight("STEP 1 — THE LAND, BEFORE ANYTHING ELSE")
flow.append(k.body(
    "Alaska's expensive mistakes are made at this stage, and none of them is "
    "a paperwork mistake. Two of these — the geotechnical investigation and "
    "the wetlands determination — are the difference between a house and a "
    "loss, and neither is required by any Alaska permit."))

flow += k.check_table("Step 1 — Site and title", [
    ("Deed recorded, parcel number confirmed, and the legal description "
     "matches what you are building on",
     [("Parcel ID:", 0.5), ("Recorded:", 0.5)]),
    ("<b>Geotechnical investigation ordered</b> — non-negotiable on any site "
     "with possible permafrost, on a slope, or on fine-grained soils. Nothing "
     "in Alaska law requires this and nothing else will save you from it",
     [("Firm:", 0.5), ("Report date:", 0.5)]),
    ("Survey and plot plan showing the building envelope, the wastewater "
     "system and its reserve area, the well, and the driveway — drawn "
     "together, because they compete for the same ground",
     [("Surveyor:", 0.5), ("Date:", 0.5)]),
    ("<b>Wetlands determination.</b> Alaska holds an enormous share of the "
     "nation's wetlands and a Section 404 permit from the U.S. Army Corps of "
     "Engineers, Alaska District, is a real gate on a real number of parcels. "
     "Ask before you design the driveway, not after you have cut it",
     [("Requested:", 0.5), ("Outcome:", 0.5)]),
    ("<b>Floodplain status.</b> Where your community participates in the "
     "National Flood Insurance Program a floodplain development permit is "
     "required in a mapped special flood hazard area <i>even with no "
     "building code</i>, and riverine and ice-jam flooding are ordinary "
     "Alaska risks",
     [("In SFHA? Y/N:", 0.34), ("Permit needed:", 0.33), ("From:", 0.33)]),
    ("Access and driveway approval — Alaska DOT&amp;PF for a state-maintained "
     "road, the borough or city for theirs, or a recorded easement and a road "
     "association where the road is private",
     [("Authority:", 0.5), ("Permit / easement:", 0.5)]),
    ("Physical address assigned by the borough or city addressing office. "
     "Utilities, deliveries and emergency services all need it, and it is "
     "usually free and slow",
     [("Address:", 0.6), ("Assigned:", 0.4)]),
    ("Zoning or land use confirmed — setbacks, height, accessory buildings, "
     "and any waterfront or habitat setback. This exists in many Alaska "
     "boroughs that have <i>no</i> building code at all",
     [("Setbacks F/S/R:", 0.6), ("Confirmed by:", 0.4)]),
], notes_header="Notes / who confirmed")

# ---------------------------------------------------------------- step 2
flow += k.h2_tight("STEP 2 — WASTEWATER AND WATER: THE LONG POLE")
flow.append(k.body(
    "On a parcel with no building department this is normally the <b>only "
    "mandatory approval you will obtain</b>, and it is also the one with the "
    "longest lead time, because it depends on soil work that the ground has "
    "to be thawed to do. Start it a season ahead of everything else."))
flow.append(k.body(
    "Onsite wastewater is regulated statewide by the Department of "
    "Environmental Conservation under <b>18 AAC 72</b>. In several parts of "
    "Alaska the program is run locally instead — the Municipality of "
    "Anchorage's on-site water and wastewater program is the largest — and "
    "where it is, the local rules are the ones that apply and they are "
    "commonly stricter. Establish which office regulates your parcel before "
    "you pay anyone for a soils test, and write the answer into AK.4."))

flow.append(k.callout(
    "Before you read a word of Alaska septic advice — check the section number",
    [
        Paragraph("<b>18 AAC 72 was rewritten effective October 1, 2023 and "
                  "amended again on August 13, 2025.</b> Three of the "
                  "sections every older guide relies on now read, in the "
                  "code itself, \"<i>Repealed</i>\" — <b>18 AAC 72.020</b> "
                  "(separation distances), <b>72.025</b> (holding tanks) and "
                  "<b>72.035</b> (conventional onsite systems).", S["body"]),
        Paragraph("If a website, a realtor or a contractor quotes you "
                  "18 AAC 72.020 for a setback, they are quoting a section "
                  "that no longer exists. The live sections for a house are "
                  "<b>18 AAC 72.501 — 72.560</b> for a conventional system, "
                  "<b>72.601 — 72.660</b> for an alternative one, and "
                  "<b>72.100</b> for the distances around a private well.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- three routes
flow.append(Spacer(1, 8))
flow.append(k.body(
    "<b>You may not simply dig it yourself.</b> 18 AAC 72.400 provides that "
    "\"<i>a person may not construct, install, or modify any part of a "
    "conventional onsite wastewater system unless that person is certified "
    "under 18 AAC 72.405 or approved under 18 AAC 72.410</i>.\" But two of "
    "the three routes past that bar are open to an owner-builder, and one of "
    "them is <b>you, personally, after a DEC course</b> — which is far more "
    "permissive than most states and almost nobody knows it exists."))

route_rows = [
    [k.cellp("<b>Approved homeowner</b><br/>"
             "<font size=9>18 AAC 72.511(c); 72.410</font>"),
     k.cellp("<b>You install it yourself.</b> Complete DEC's training course, "
             "apply, and pay the <b>$275</b> homeowner training fee. The "
             "approval covers your own owner-occupied residence and "
             "authorizes <b>one system within a one-year period</b>. You must "
             "still have the soils properly classified — see below."),
     k.cellp("<b>$275</b><br/>training fee")],
    [k.cellp("<b>Certified installer</b><br/>"
             "<font size=9>18 AAC 72.511(a); 72.405</font>"),
     k.cellp("A contractor with DEC certification installs it. No prior DEC "
             "approval needed for a single private residence at not more than "
             "<b>1,500 gallons per day</b> of design flow."),
     k.cellp("Their fee")],
    [k.cellp("<b>Engineer design</b><br/>"
             "<font size=9>18 AAC 72.511(b)</font>"),
     k.cellp("Up to <b>2,500&nbsp;gpd</b> with no prior approval \"<i>if the "
             "system is installed by a person whose work is completed "
             "according to a registered engineer's design and the engineer "
             "inspects construction</i>.\" Required outright for alternative "
             "systems, holding tanks, waivers, and any site needing plan "
             "approval."),
     k.cellp("Engineer's fee")],
]
flow.append(k.ref_table(
    "Three routes to a legal septic system — none of them needs a permit",
    [k.cellp("Route", bold=True), k.cellp("What it involves", bold=True),
     k.cellp("Cost", bold=True)],
    route_rows, [1.5 * inch, CW - 1.5 * inch - 0.95 * inch, 0.95 * inch]))
flow.append(k.cite(
    "18 AAC 72.400; 72.511(a), (b), (c); 72.410(a), (b); 72.954(c) — "
    "\"<i>a training fee of $275</i>.\" Even on the homeowner route the "
    "soils must be classified by <b>a registered engineer or a soils "
    "laboratory</b> — 72.511(c)(2) requires either a sieve analysis of a "
    "collected sample or an engineer's on-site visual classification with a "
    "percolation test. A percolation test is mandatory in silty soils (SM, "
    "GM, ML) and unnecessary in clean sands (72.530(f)(3) note a)."))

# ---------------------------------------------------------------- the numbers
flow += k.h2_tight("THE NUMBERS ALASKA FIXES STATEWIDE")
flow.append(k.body(
    "These apply to every conventional system in the state, including one "
    "you install yourself with no permit and no inspector. They are worth "
    "knowing <b>before you buy a lot</b>, because a parcel that cannot hold "
    "them is a parcel you cannot build on."))

sep_rows = [
    [k.cellp("<b>100 feet</b>"),
     k.cellp("Between a <b>private well</b> and a septic tank, absorption "
             "field, sewer line, holding tank, pit privy, or \"<i>other "
             "potential source of contamination</i>,\" measured nearest edge "
             "to nearest edge. (A well serving a <i>public</i> system needs "
             "200 feet — 18 AAC 80.020 Table A.)"),
     k.cellp("18 AAC 72.100(a)(1)")],
    [k.cellp("<b>100 feet</b>"),
     k.cellp("Between a septic tank, absorption field, lift station or sewer "
             "manhole and the high water level of a <b>lake, river, stream, "
             "spring or slough</b>. Read \"slough\" broadly — the definitions "
             "section includes <b>a swamp, bog, or marsh</b>, which on an "
             "Alaska parcel is often most of it."),
     k.cellp("18 AAC 72.520(b); 72.990(91)")],
    [k.cellp("<b>4 feet</b>"),
     k.cellp("Vertical, from the bottom of the distribution media down to "
             "the <b>annual high water table</b>."),
     k.cellp("18 AAC 72.520(d)(1)")],
    [k.cellp("<b>6 feet</b>"),
     k.cellp("Vertical, down to an <b>impermeable horizon</b> — bedrock, "
             "clay, <b>permafrost</b>, or soils percolating slower than 120 "
             "minutes per inch."),
     k.cellp("18 AAC 72.520(d)(2)")],
    [k.cellp("<b>50 feet</b>"),
     k.cellp("Horizontal, between any part of the absorption field and a "
             "slope steeper than 25 percent with a vertical drop over 10 "
             "feet, natural or man-made."),
     k.cellp("18 AAC 72.520(c)")],
]
flow.append(k.ref_table(
    "Separation distances — statewide, mandatory",
    [k.cellp("Distance", bold=True), k.cellp("From what, to what", bold=True),
     k.cellp("Authority", bold=True)],
    sep_rows, [0.9 * inch, CW - 0.9 * inch - 1.45 * inch, 1.45 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "And the setback Alaska does NOT have — which is worth as much as the "
    "ones it does", [
        Paragraph("There is <b>no state property-line setback and no state "
                  "foundation setback</b> for a septic system. 18 AAC 72.520 "
                  "was read in full and contains neither. DEC's installation "
                  "manual lists 10 feet to a lot line and 10 feet to a "
                  "foundation, and footnotes both as a "
                  "\"<i>Recommended minimum horizontal separation "
                  "distance</i>\" — guidance, not law.", S["body"]),
        Paragraph("Inside the <b>Municipality of Anchorage</b> those same 10 "
                  "feet <i>are</i> mandatory, along with a 20-foot setback "
                  "from smaller slope breaks and seasonal groundwater "
                  "adjustment factors, under AMC 15.65.210. That is the "
                  "shape of the whole Alaska problem in one paragraph: the "
                  "state floor is thinner than people assume, and a "
                  "delegated local program can be markedly thicker. Build to "
                  "the recommended 10 feet anyway — it costs nothing at "
                  "layout and it protects your resale.", S["body"]),
    ]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>Sizing.</b> Design flow is <b>150 gallons per day for each "
    "bedroom</b> (18 AAC 72.530(b)(1)). Minimum septic tank for a house of "
    "up to three bedrooms is <b>1,000 gallons</b>, plus <b>250 gallons for "
    "each bedroom over three</b> (72.530(e)(2)). Absorption field area comes "
    "off a table keyed to percolation rate and soil class, taking whichever "
    "is more conservative (72.530(f)(3)). <b>In clean gravels a two-foot "
    "sand liner is mandatory</b> unless the percolation rate is slow enough "
    "to stand on its own — ground that drains too fast fails for the "
    "opposite reason to ground that drains too slowly, and people are "
    "surprised by it (72.530(f)(3)). And the cover over the field is a "
    "climate figure: <b>2 feet</b> of soil in southwest Alaska, <b>3 feet</b> "
    "in Southeast and the coast south and east of Valdez, and <b>4 feet</b> "
    "in \"<i>all remaining areas of the state</i>\" (72.530(c)) — approved "
    "insulation may substitute for up to two of those feet, but never below "
    "two feet of actual soil."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Permafrost does not just complicate the system — it disqualifies the "
    "easy route", [
        Paragraph("Every no-plan-approval route above is conditioned on "
                  "18 AAC 72.511(d), and subsection (d)(4) is the cliff. An "
                  "exempt system \"<i>may not be located in an area (A) "
                  "<b>known or suspected to contain permafrost</b>; (B) where "
                  "other conventional onsite wastewater systems have been "
                  "known to perform poorly; (C) where the groundwater table "
                  "is within four feet of the ground surface or the soil "
                  "conditions are overly moist or wet at any time of the "
                  "year</i>.\"", S["body"]),
        Paragraph("Note the standard: <b>suspected</b>, not proven. If your "
                  "ground is under suspicion you are out of the homeowner "
                  "and certified-installer routes entirely, into engineer "
                  "design and DEC plan approval — and 18 AAC 72.265(6) then "
                  "requires <b>a laboratory soil-moisture profile analysis</b> "
                  "showing the soils are adequately drained <i>and</i> "
                  "<b>a geotechnical study</b> showing the area \"<i>will "
                  "remain stable under the proposed design</i>.\"",
                  S["body"]),
        Paragraph("This is the strongest argument in the kit for buying the "
                  "geotechnical report early. In permafrost country it is not "
                  "only your foundation that depends on it — it decides "
                  "whether your septic system costs three thousand dollars or "
                  "thirty, and it decides it before you have spent anything "
                  "else.", S["body"]),
    ]))

# ---------------------------------------------------------------- what you file
flow += k.h2_tight("WHAT YOU FILE, AND WHEN")
flow.append(k.body(
    "There are two entirely different paper trails and they are commonly "
    "confused. Establish which one you are on before you dig."))

file_rows = [
    [k.cellp("<b>No plan approval needed</b><br/>"
             "<font size=9>the ordinary house</font>"),
     k.cellp("<b>Before:</b> notify DEC \"<i>at least one day before "
             "beginning construction</i>,\" on the department's form "
             "(72.550(a)).<br/><b>After:</b> within <b>90 days</b>, register "
             "the system with a completed <b>Documentation of "
             "Construction</b> — signed or sealed, plus <b>photographs of "
             "eight specified stages</b> of the installation, plus the "
             "<b>$115</b> registration fee (72.550(c); 72.955(a))."),
     k.cellp("<b>$115</b>")],
    [k.cellp("<b>Plan approval needed</b><br/>"
             "<font size=9>alternative systems, permafrost, waivers</font>"),
     k.cellp("<b>Before:</b> an <b>Approval to Construct</b> — that is the "
             "regulation's own name for it. DEC acts within <b>30 days</b> of "
             "a complete submittal, and the approval is void if the work is "
             "not finished within <b>2 years</b> (72.225).<br/><b>After:</b> "
             "within <b>60 days</b>, a <b>certification of construction</b> "
             "signed by the owner, each contractor and the observing "
             "engineer, plus record drawings (72.240(c))."),
     k.cellp("<b>$655</b><br/><font size=9>plan review,<br/>to 1,500 "
             "gpd</font>")],
]
flow.append(k.ref_table(
    "Two paper trails — find out which is yours before you dig",
    [k.cellp("Path", bold=True), k.cellp("What you file", bold=True),
     k.cellp("Fee", bold=True)],
    file_rows, [1.45 * inch, CW - 1.45 * inch - 0.95 * inch, 0.95 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "Photograph the open trench, or you cannot register the system", [
        Paragraph("Of everything in this kit, this is the instruction most "
                  "likely to save you money and the easiest to miss. The "
                  "90-day Documentation of Construction requires "
                  "<b>photographs of eight specified stages</b> — and the "
                  "ones that matter are the stages that exist for a few "
                  "hours: <b>the open excavation of the absorption field</b>, "
                  "and <b>the field with its media and pipe in place just "
                  "before backfill</b>. Once the machine has covered it, the "
                  "photograph cannot be taken and the registration cannot be "
                  "completed on the ordinary route.", S["body"]),
        Paragraph("Put a phone in someone's hand before the excavator "
                  "arrives. Shoot more than you think you need — the tank "
                  "with its inlet and outlet, the cleanouts, the fabric, the "
                  "standpipes, the finished grade. It costs nothing and it "
                  "is the difference between a $115 filing and an "
                  "engineer's report on a buried system.", S["body"]),
    ]))
flow.append(Spacer(1, 6))
flow.append(k.callout(
    "The ninety days is the cheapest deadline in this kit", [
        Paragraph("Miss the 90-day registration and the fix is not a late "
                  "fee. It is an <b>after-the-fact registration</b> under "
                  "18 AAC 72.560, which requires an <b>engineer-sealed "
                  "adequacy report</b> on a system that is already buried. "
                  "The same paperwork that costs <b>$115</b> and an "
                  "afternoon on time costs an engineer's site visit and "
                  "report later — and you will need it, because DEC keeps "
                  "the record and any future buyer or lender can pull it for "
                  "a $25 retrieval fee (72.955(b), (c)).", S["body"]),
    ]))
flow.append(Spacer(1, 6))
flow.append(d.FillInRow([("Route (homeowner / installer / engineer):", 0.58),
                         ("DEC notified:", 0.42)]))
flow.append(d.FillInRow([("Documentation of Construction filed:", 0.5),
                         ("Registration no. / date:", 0.5)]))

flow += k.check_table("Step 2 — Wastewater", [
    ("Established which office regulates onsite wastewater for your parcel — "
     "DEC, or a delegated program such as the Municipality of Anchorage's "
     "On-Site Water and Wastewater Section",
     [("Office:", 0.6), ("Confirmed:", 0.4)]),
    ("Route chosen and, if you are installing it yourself, DEC's homeowner "
     "training course completed and the $275 approval in hand <b>before</b> "
     "you start — it authorizes one system in a one-year period",
     [("Approved:", 0.5), ("Expires:", 0.5)]),
    ("Soils classified by a registered engineer or a soils laboratory, and a "
     "percolation test done where the soil class requires one",
     [("By:", 0.5), ("Date:", 0.5)]),
    ("Seasonal high water table established from monitoring between <b>June 1 "
     "and September 30</b>, or by another method the reviewer accepts — a "
     "winter reading does not establish it",
     [("Method:", 0.6), ("Result:", 0.4)]),
    "Site checked against the statewide separations above — 100 feet to the "
    "well, 100 feet to any lake, stream, spring, swamp, bog or marsh, 4 feet "
    "to the water table, 6 feet to bedrock or permafrost, 50 feet from a "
    "steep slope",
    "Permafrost ruled in or out. If suspected, you are on the engineer and "
    "plan-approval route and need a soil-moisture profile and a geotechnical "
    "study",
    ("DEC notified at least one day before construction begins",
     [("Notified:", 1.0)]),
    ("<b>Documentation of Construction filed within 90 days</b>, with the "
     "eight required photographs and the $115 fee — or the engineer's "
     "certification of construction within 60 days on the plan-approval route",
     [("Filed:", 0.5), ("Copy kept:", 0.5)]),
    "Reserve area protected from traffic and stockpiling for the whole build",
    ("If a holding tank or a pit privy is your plan, you have confirmed the "
     "conditions in writing — a privy needs no DEC approval but must meet "
     "18 AAC 72.030; a holding tank is an alternative system and needs an "
     "engineer", [("Confirmed:", 1.0)]),
], notes_header="Notes / who confirmed")

# ---------------------------------------------------------------- water
flow += k.h2_tight("STEP 2b — THE WELL, AND THE ONE FILING THAT IS MANDATORY")
flow.append(k.body(
    "<b>Alaska requires no state permit to drill a private domestic well.</b> "
    "The drinking water regulations, 18 AAC 80, apply to <i>public</i> water "
    "systems; a single-family well is a \"private water system\" and sits "
    "outside them, and DEC's own guidance for private systems says in terms "
    "that \"<i>application of these BMPs is voluntary</i>.\" Do not let "
    "anyone tell you the construction standards are mandatory — with one "
    "real exception, below."))
flow.append(k.bullet(
    "<b>The separations are mandatory.</b> The 100-foot distances in "
    "18 AAC 72.100(a) bind your well whether or not anyone permits it, and "
    "there is a 25-foot distance to a private sewer line, a building sump, "
    "and a fuel tank or line."))
flow.append(k.bullet(
    "<b>The construction method is effectively mandatory.</b> 18 AAC "
    "72.100(c): a person who drills or operates a private well \"<i>must use "
    "a method equivalent to well protection or source water protection "
    "contained in 18 AAC 80 or the publicly identified approved best "
    "management practice</i>.\" So the standards arrive by cross-reference "
    "even though the permit does not."))
flow.append(k.bullet(
    "<b>The well log is mandatory, and it is on whoever drills.</b> "
    "11 AAC 93.140(a): \"<i>the water well contractor <b>or a person who "
    "constructs the well</b> shall file a report within <b>45 days</b> after "
    "completion with <b>both the property owner and the department</b></i>.\" "
    "Filed with the Department of Natural Resources through its Well Log "
    "Tracking System. Drill it yourself and the duty is yours. <b>Get your "
    "copy at the time, then search the tracking system a couple of months "
    "later and confirm the filing actually landed</b> — your lender and your "
    "buyer will both want it, and a driller who never filed is a problem you "
    "want to find now rather than at closing."))
flow.append(k.bullet(
    "<b>A water right is usually not needed.</b> An application is required "
    "before consuming more than 5,000 gallons in a single day, or regularly "
    "using more than 500 gallons per day for more than 10 days a year "
    "(11 AAC 93.035(b)). DNR's standard quantity for a fully plumbed "
    "single-family home is <b>500 gallons per day</b> (11 AAC 93.040(d)(1)) "
    "— an ordinary house sits at or below the line. A water right is "
    "optional priority protection, not a permit to drill."))
flow.append(Spacer(1, 4))
flow.append(k.callout(
    "Test for arsenic, whatever anyone tells you about permits", [
        Paragraph("No Alaska statute requires a private well to be tested. "
                  "DEC recommends a baseline for <b>total coliform, nitrate "
                  "and arsenic</b> after the well is disinfected and "
                  "flushed, against 0 per 100 mL, 10 mg/L and 0.010 mg/L. "
                  "The arsenic line is not theoretical here: the State "
                  "Section of Epidemiology has documented private wells in "
                  "the Fairbanks area at up to <b>960 parts per billion</b>, "
                  "roughly a hundred times the drinking-water standard, and "
                  "reports that arsenic in private wells \"<i>is a known "
                  "problem in some communities</i>\" there.", S["body"]),
        Paragraph("Carbon filters and water softeners do <b>not</b> remove "
                  "arsenic. Reverse osmosis does. Test before you plumb, not "
                  "after — and inside the Municipality of Anchorage you will "
                  "be tested at resale anyway, for coliform, arsenic and "
                  "nitrate together.", S["body"]),
    ]))
flow.append(k.cite(
    "18 AAC 80.005(b) and 18 AAC 80.1990 (private water system definition); "
    "DEC, <i>Best Management Practices for Private Drinking Water "
    "Systems</i>; 18 AAC 72.100(a), (c); 11 AAC 93.140(a); 11 AAC 93.035(b); "
    "11 AAC 93.040(d)(1); Alaska Section of Epidemiology, <i>Bulletin</i> "
    "2016-14. Note the Municipality of Anchorage is different on both counts "
    "— a new well there needs a municipal permit under <b>AMC 15.55</b>, and a "
    "septic design there must always be sealed by a registered civil "
    "engineer (AMC 15.65.050D.3). Confirm the current subsection with the "
    "On-Site Water and Wastewater Section; sources differ on it."))

# ---------------------------------------------------------------- step 3
flow += k.h2_tight("STEP 3 — THE BUILDING ITSELF")
flow.append(k.body(
    "Nothing in this step is required by an Alaska permit unless a local "
    "department issues you one. Every item is here because the building "
    "needs it, or because somebody who is going to lend against, insure or "
    "buy the house will ask for it later."))

flow += k.check_table("Step 3 — Design and construction documents", [
    ("Structural design appropriate to your seismic and snow loading, by an "
     "engineer registered in Alaska. Alaska is the most seismically active "
     "part of the United States and roof snow loads vary sharply with "
     "elevation over short distances",
     [("Engineer:", 0.5), ("Sealed:", 0.5)]),
    ("Foundation design matched to the geotechnical report — and if that "
     "report identifies ice-rich permafrost, a foundation type chosen to keep "
     "the ground frozen rather than to resist settlement",
     [("Type:", 0.6), ("Basis:", 0.4)]),
    "Full plan set and specifications, kept as a record even where nobody "
    "reviews them — you will need them for the appraisal, the insurance "
    "binder and the eventual sale",
    ("Energy design fixed early: envelope, air barrier detail and a balanced "
     "ventilation strategy chosen together. In this climate an airtight house "
     "without balanced ventilation is a moisture failure waiting to happen",
     [("Ventilation:", 0.5), ("Design by:", 0.5)]),
    ("If any part of the build is financed, the lender's construction "
     "standard obtained <b>in writing before you draw</b> — see Step 4",
     [("Standard:", 0.6), ("Received:", 0.4)]),
    "Materials ordered against the season, not the schedule: long-lead items "
    "and anything shipped by barge or air ordered over the winter",
], notes_header="Notes / evidence")

# ---------------------------------------------------------------- step 4
flow += k.h2_tight("STEP 4 — THE CODE THAT ARRIVES THROUGH THE MORTGAGE")
flow.append(k.body(
    "This step has no equivalent in a Lower 48 permit kit, and for a "
    "financed Alaska owner-builder it is the most consequential page in the "
    "whole product. Alaska has no building code for houses — <b>and it "
    "enforces one anyway, through loan eligibility instead of a permit "
    "counter.</b>"))
flow.append(k.body(
    "Be precise about what this is, because the popular version of it is "
    "wrong. It is not \"your lender's rules.\" It is <b>state law</b>. The "
    "Alaska Housing Finance Corporation is a public corporation of the "
    "state, and two statutes bar it from lending on a house that was not "
    "built to a standard the state sets. The enforcement mechanism is the "
    "mortgage; the standard is statutory."))

flow.append(k.callout_long(
    "The two statutes, and the two dates they turn on", [
        Paragraph("<b>Inspections.</b> AS 18.56.300(a): the corporation "
                  "\"<i>may not make or purchase a housing loan for "
                  "residential housing the construction of which begins "
                  "<b>after June 30, 1992</b></i>\" unless it is inspected — "
                  "and subsection (b) names the stages: \"<i>(1) plan "
                  "approval; (2) completion of footings and foundations; (3) "
                  "completion of electrical installation, plumbing, and "
                  "framing; (4) completion of installation of insulation; "
                  "(5) final approval</i>.\" Five inspections, in statute.",
                  S["body"]),
        Paragraph("<b>Energy.</b> AS 46.11.040: \"<i>State financial "
                  "assistance may not be approved or granted for the "
                  "construction of or purchase of a loan for a residential "
                  "building if construction of the building began "
                  "<b>after December 31, 1991</b>, unless … the building is "
                  "in compliance with thermal and lighting energy "
                  "standards</i>,\" with a parallel bar on AHFC itself at "
                  "AS 18.56.096(c). Those standards are the <b>Building "
                  "Energy Efficiency Standard</b> — BEES.", S["body"]),
        Paragraph("<b>Two different dates, six months apart.</b> The energy "
                  "duty attaches to construction begun after 31 December "
                  "1991; the inspection duty to construction begun after 30 "
                  "June 1992. They are separate obligations from separate "
                  "statutes and nothing lets you satisfy one by satisfying "
                  "the other.", S["body"]),
    ]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>Which code?</b> 15 AAC 150.035(a) adopts the <b>2018 International "
    "Residential Code with Alaska-specific amendments</b> as \"<i>the "
    "residential building code for buildings used for residential purposes "
    "containing four or fewer dwelling units</i>\" — and, in the sentence "
    "that matters most to this kit's reader, applies it \"<i>to a "
    "residential unit that is <b>not located within a municipality that has "
    "an approved municipal building code</b></i>.\" It is drafted precisely "
    "for the ungoverned parcel. BEES itself is the <b>2018 IECC plus ASHRAE "
    "62.2-2016 plus Alaska amendments</b>, adopted at 15 AAC 155.010 and "
    "applying to buildings whose construction began on or after 1 January "
    "2019, with a minimum <b>5 Star</b> energy rating and a maximum "
    "<b>4&nbsp;ACH50</b> air leakage rate."))

flow.append(k.callout(
    "Read the amendment that gives this chapter its shape", [
        Paragraph("AHFC's amendments to the IRC <b>delete Chapter 1, Part 2 "
                  "— Administration and Enforcement</b>: the permit system, "
                  "the inspection card, the certificate of occupancy, the "
                  "whole apparatus by which a building department normally "
                  "operates a code. What replaces it is a recorded "
                  "certificate. And the BEES amendment document defines its "
                  "own enforcer in terms — \"<i>CODE OFFICIAL. The officer "
                  "or other designated duly authorized representative of "
                  "AHFC</i>.\"", S["body"]),
        Paragraph("<b>The financier is the building official.</b> That is "
                  "the single sentence this chapter exists to deliver.",
                  S["body"]),
    ]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>What proves it.</b> Two forms, and you should know their numbers "
    "before you start. <b>PUR-101</b> is the BEES certification, completed "
    "only by an AHFC-authorized energy rater using the state's AkWarm "
    "modeling software — you cannot self-certify it. <b>PUR-102</b> is the "
    "Summary of Building Inspections, signed stage by stage by an authorized "
    "inspector and then <b>recorded</b>; AHFC states that recording it "
    "\"<i>is the only means of tracking compliance with the law</i>.\" A "
    "certificate of occupancy from an <b>approved municipality</b> "
    "substitutes for the PUR-102 — which is why the list of approved "
    "municipalities matters enormously, and why it is not the list you would "
    "guess: <b>Wasilla and the Mat-Su Borough outside Palmer city are not on "
    "it.</b>"))

flow.append(k.callout_long(
    "The part that reaches you even if you never borrow a dollar", [
        Paragraph("Suppose you pay cash, skip the inspections, and build a "
                  "sound house. Nothing happens — until you sell. Your buyer "
                  "wants an AHFC-backed loan, and AHFC may not purchase a "
                  "loan on a house built after June 1992 that was never "
                  "inspected. <b>The obligation was yours; the consequence "
                  "lands on your buyer, which means it lands on your "
                  "price.</b>", S["body"]),
        Paragraph("The remedy exists and it is ugly: a <b>destructive "
                  "inspection</b>, accepted case by case — holes cut in "
                  "finished sheetrock, an engineer and an inspector engaged, "
                  "a notarized certification recorded after the fact. "
                  "Compare that with five inspections scheduled while the "
                  "walls are open.", S["body"]),
        Paragraph("So the honest framing is not \"comply if you are "
                  "borrowing.\" It is: <b>the five inspections are the "
                  "cheapest resale insurance available to an Alaska "
                  "owner-builder</b>, and they are cheapest on the day the "
                  "stage is open. If you are building outside an approved "
                  "municipality, this is the decision to make before "
                  "footings, not after drywall.", S["body"]),
    ]))
flow.append(k.cite(
    "AS 18.56.300(a), (b); AS 46.11.040; AS 18.56.096(c); 15 AAC 150.035(a); "
    "15 AAC 155.010; AHFC <i>New Construction Inspection Guidelines</i> and "
    "the Building Energy Efficiency Standard pages at <b>ahfc.us</b>, read "
    "August 2026. 15 AAC 150.040(b) allows a loan where the borrower "
    "\"<i>agrees, in writing, to bring the building into compliance … within "
    "one year</i>.\" <b>Do not cite AS 18.56.300(e)(3) for the code "
    "edition</b> — its text still names the old Uniform Building Code; the "
    "regulation controls. The 5 Star floor comes from the adopted "
    "amendments and AHFC's own published standard, not from 15 AAC "
    "155.030(a)(1), which still reads \"four-star plus.\""))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>Owner-builders are expressly accommodated, and it is written into "
    "the statute.</b> AS 18.56.096(a)(3) requires the work to be done by a "
    "registered contractor — then excepts work that \"<i>(A) has been "
    "totally or substantially performed by the borrower; (B) has been "
    "performed by a borrower who acts as the contractor …; or (C) has been "
    "performed in an area designated by the corporation as exempt … because "
    "of the unavailability of registered contractors</i>.\" The PUR-102 "
    "itself carries an <b>Exempt Builder's Certification</b> on which you "
    "certify that you qualify under AS 08.18.161 and, if you are an "
    "owner-builder under paragraph (11), \"<i>that I have not built a single "
    "family building, duplex, triplex, fourplex or commercial building "
    "within the prior two years</i>.\" <b>The two-year rule in AK.1 follows "
    "you onto the mortgage paperwork.</b> You skip the contractor "
    "credential; you do not skip the inspections or BEES."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "If your loan is federal rather than state — FHA's answer to the same "
    "problem", [
        Paragraph("HUD faced the identical question and answered it in "
                  "Mortgagee Letter 2020-36. For proposed new construction "
                  "the file needs \"<i>copies of the building permit (or "
                  "equivalent) and CO (or equivalent); <b>or</b> three "
                  "inspections (footing, framing and final) performed by the "
                  "local authority with jurisdiction over the Property or an "
                  "ICC certified RCI or CI …; <b>or</b> in the absence of "
                  "such ICC certified RCI or CI … three inspections … "
                  "performed by a disinterested third-party, who is a "
                  "registered architect or a structural engineer</i>.\" HUD's "
                  "own note on the change: it is \"<i>particularly relevant "
                  "in jurisdictions where building permits are not "
                  "issued</i>.\"", S["body"]),
        Paragraph("<b>Two things you will still be told that are no longer "
                  "true:</b> the ten-year insured protection plan option and "
                  "the 90 percent loan-to-value cap that went with it were "
                  "<b>eliminated</b>. Anyone offering you a ten-year warranty "
                  "as the FHA workaround is working from a superseded "
                  "handbook.", S["body"]),
    ]))

flow.append(Spacer(1, 6))

flow += k.check_table("Step 4 — Financing, inspections and the standard they impose", [
    ("Established whether your parcel is inside an <b>AHFC-approved "
     "municipality</b> — if it is, a certificate of occupancy substitutes for "
     "the inspection summary; if it is not, you must arrange the inspections "
     "yourself", [("Approved municipality? Y / N:", 0.6), ("Confirmed:", 0.4)]),
    ("<b>Five inspections scheduled before footings</b> — plan approval; "
     "footings and foundations; electrical, plumbing and framing; insulation; "
     "final. Each one is cheap while the stage is open and expensive "
     "afterwards", [("Inspector:", 0.6), ("Booked:", 0.4)]),
    ("AHFC-authorized inspector identified and available in your area — in a "
     "community with no ICC-licensed inspector, ask about the video and "
     "photograph allowance and get the approval <b>in writing in advance</b>",
     [("Name:", 0.6), ("Confirmed:", 0.4)]),
    ("Energy rater booked and the <b>PUR-101</b> path understood — only an "
     "AHFC-authorized rater can complete it, and raters are scarce off the "
     "road system", [("Rater:", 0.5), ("Booked:", 0.5)]),
    ("<b>PUR-102 recorded</b> at the end, not merely completed — recording is "
     "how compliance is tracked", [("Recorded:", 0.5), ("Book/page:", 0.5)]),
    ("Designed to BEES from the start — 2018 IECC with Alaska amendments, "
     "minimum 5 Star rating, maximum 4&nbsp;ACH50. Retrofitting an envelope to a "
     "rating is not possible after drywall",
     [("Target rating:", 0.5), ("Modeled by:", 0.5)]),
    ("If you are borrowing federally rather than from AHFC, the lender's "
     "inspection route confirmed in writing — permit and CO, three "
     "inspections by an ICC-certified inspector, or three by an architect or "
     "structural engineer", [("Route:", 0.6), ("Confirmed:", 0.4)]),
    ("Builder's risk insurance bound before materials arrive on site, and the "
     "carrier's requirements for an owner-built dwelling understood",
     [("Carrier:", 0.5), ("Bound:", 0.5)]),
    ("Homeowner's policy pre-qualified — ask now what the carrier will want "
     "at completion where no certificate of occupancy exists",
     [("Carrier:", 0.5), ("What they want:", 0.5)]),
    ("Workers' compensation in place if you will pay anyone as an employee "
     "rather than engaging a registered contractor",
     [("Policy:", 0.6), ("Effective:", 0.4)]),
], notes_header="Notes / who confirmed")

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "The money that flows the other way — and reaches a cash build", [
        Paragraph("Two AHFC programs pay you for going past the floor, and "
                  "one of them does not require an AHFC loan at all. The "
                  "<b>New Home Construction Rebate</b> is <b>$10,000</b>, "
                  "first-come until the funds are gone, for reaching "
                  "<b>5 Star Plus</b> — a notch above the BEES minimum, so "
                  "keep the two figures distinct — with the foundation "
                  "inspected on or after 2 January 2025. <b>AHFC financing "
                  "is not required</b>, which makes it a second reason for a "
                  "cash builder to run the inspections.", S["body"]),
        Paragraph("The <b>Energy Efficiency Interest Rate Reduction</b> cuts "
                  "the rate on the first <b>$250,000</b> of an AHFC loan — "
                  "roughly a quarter to a half point depending on the rating "
                  "and whether natural gas is available. Both are "
                  "first-come and both change; confirm current terms at "
                  "ahfc.us while you are still designing, because both are "
                  "keyed to decisions you make before footings.", S["body"]),
    ]))
flow.append(k.cite(
    "AS 18.56.096(a)(3); 15 AAC 155.020 (the only two BEES exemptions); "
    "AHFC PUR-101 and PUR-102 and the <i>New Construction Inspection "
    "Guidelines</i>; AHFC rebate and interest-rate-reduction program pages, "
    "read August 2026 — <b>both are funding-dependent, so confirm before "
    "relying on either</b>. HUD Mortgagee Letter 2020-36, amending Handbook "
    "4000.1 II.A.8.i, mandatory for case numbers assigned on or after 4 "
    "January 2021; new construction there also needs HUD forms 92541, 92544 "
    "(a <b>one</b>-year warranty) and 92051."))

# ---------------------------------------------------------------- step 5
flow += k.h2_tight("STEP 5 — ONLY IF A BUILDING DEPARTMENT ISSUES YOUR PERMIT")
flow.append(k.body(
    "Where a borough or city does review your house, its own application "
    "governs and its requirements are additional to everything above. The "
    "items below are the ones that most often send an Alaska applicant back "
    "to the counter."))

flow += k.check_table("Step 5 — The local application", [
    ("Adopted code editions confirmed <i>for that jurisdiction</i> — they are "
     "local adoptions and they differ from each other and from the state "
     "minimums",
     [("Building:", 0.34), ("Electrical:", 0.33), ("Plumbing:", 0.33)]),
    "Plan sets in the number and scale the department requires, including a "
    "site plan showing every structure on the parcel",
    "Structural calculations, sealed where that jurisdiction requires them — "
    "several Alaska jurisdictions require them for an ordinary house because "
    "of seismic design category",
    "Surveyed plot plan where required — a sketch is commonly rejected",
    ("Energy compliance documentation in the form that jurisdiction accepts",
     [("Form:", 0.6), ("Method:", 0.4)]),
    "Wastewater approval attached — most departments will not issue a "
    "building permit without it",
    ("Separate trade permit applications identified, and who pulls each one "
     "settled before you file",
     [("Electrical by:", 0.5), ("Plumbing by:", 0.5)]),
    ("Fees, and the permit expiry rule for that jurisdiction, written down. "
     "Expiry clocks run on inspections, and an Alaska winter is exactly the "
     "gap that trips them",
     [("Fee:", 0.34), ("Expires:", 0.33), ("Renewal:", 0.33)]),
], notes_header="Notes / who confirmed")

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 10))
flow.append(k.sources_table([
    ("Smoke alarms in all dwelling units in the state, and CO alarms in all "
     "qualifying units, installed as the fire marshal approves",
     "AS 18.70.095(a), (d)(3)"),
    ("NFPA 72-2019 and IBC 907.2.11; battery-only alarms permitted only in "
     "pre-1989 buildings or buildings without commercial power",
     "13 AAC 50.030(b)"),
    ("Enforced as a class B misdemeanor with each 10 days a separate "
     "offense; the carbon monoxide provision is a non-criminal violation",
     "AS 18.70.100(a), (c)"),
    ("The Fire Marshal's authority reaches residential buildings of four or "
     "more dwelling units, and the adopted code excludes detached one-, two- "
     "and three-family dwellings", "AS 18.70.080(a)(2);\n13 AAC 50.020"),
    ("2020 NEC is the state minimum electrical code; 2018 UPC is the minimum "
     "plumbing standard throughout the state",
     "8 AAC 70.025(a); 8 AAC 63.010(a)(1)"),
    ("Communities under 2,500 population are exempt from the state plumbing "
     "chapter", "AS 18.60.735"),
    ("Lead limits of 8.0 percent in pipe and fittings and 0.2 percent in "
     "solder or flux in a residential facility providing water for human "
     "consumption", "AS 18.60.705(b)"),
    ("Onsite wastewater is regulated statewide by the Department of "
     "Environmental Conservation, or by a delegated local program",
     "18 AAC 72"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ak-permit-kit",
                       "AK.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
