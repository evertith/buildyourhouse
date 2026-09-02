#!/usr/bin/env python3
"""WI.2 Permit Application Checklist.

Everything here was read out of the primary source in September 2026 and is
cited on-page.

Verified sources:
  145.195(1)           no building permit on an unsewered parcel until the
                       septic permits are obtained — the statute that reorders
                       a rural Wisconsin build
  145.19(1g),(6),(7),(8)  the sanitary permit runs to the OWNER, the $25
                       groundwater fee, the 2-year term, transferability
  SPS 383.21(3)(c)     30 days for the county to determine a sanitary permit
  SPS 385.10(1),(2)    who may do a soil evaluation and a site evaluation —
                       a closed list that does not include the owner
  SPS 385.20(2)(b)     three soil profile evaluations, at least one a soil pit
  SPS 385.40(3)(a)     the site report contents, verbatim
  SPS 320.08(1),(2)    permit before any excavation; locked to your agency
  SPS 320.09(1),(4)    application form and two sets of plans
  SPS 320.09(5)(a)     the three-item site plan — the complete statewide list
  SPS 320.09(6)(c)     a municipality MAY NOT require an architect or engineer
                       seal, except under SPS 321.33 (floodplain)
  SPS 320.09(6)(d)     name the initial downstream receiving water
  SPS 320.09(9)(a)5,7  24-month expiry; master plumber named on the permit
  SPS 320.09(9)(b)     the footing-and-foundation permit to start construction
  SPS 320.09(9)(c)     conformance with SPS 383.25(2) before the permit issues
  SPS 320.09(9)(d)     post the permit; the uniform building permit seal
  SPS 320.09(11)       TEN BUSINESS DAYS to approve or deny
  SPS 302.34(1)        the $30 state seal fee
  SPS 316.007(1)(a)    NFPA 70 National Electrical Code 2023 — CR 26-016,
                       Register June 2026 No. 846, EFFECTIVE 1 SEPTEMBER 2026
  SPS 316.003(6)       additions and alterations comply with the chapter as it
                       stands at the time of permit application
  SPS 320.24 tables    what the UDC actually adopts by reference — and NFPA 70
                       is NOT among them; electrical comes through ch. SPS 316
  SPS 321.02           live loads, wind load, and the roof-load zone map
  Figure 321.02        Zone 1 = 40&nbsp;psf, Zone 2 = 30&nbsp;psf
  SPS 321.16(1),(2)    48&nbsp;inches or below frost penetration, whichever deeper
  SPS 322.31(1)(b)     the ENERGY zones — and they are numbered the opposite
                       way from the roof-load zones
  Tables 322.31-1,-3   the prescriptive envelope and the 90% AFUE furnace rule
  101.653(2)(b)        erosion control: more restrictive practices above 12%
                       slope
  SPS 321.125          erosion control for one- and 2-family dwellings

Deliberately NOT printed: any municipal permit fee. s. 101.65(1)(c) lets each
municipality set its own by ordinance and there is no statewide figure. Also
not printed: a snow load for any named county. Figure 321.02 is a map with the
zone boundary drawn across county lines; reading a county off it would be
guessing. The two legend values are printed and the reader is sent to the
inspector or the truss supplier.
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

FORM_ID = "WI.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Applications & Code Editions"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What to gather, in the order Wisconsin makes you gather it — and every "
    "code edition actually in force as of September 2026.")

flow.append(k.disclaimer(
    "Code editions change, and one of them changed this month. Confirm the "
    "electrical edition your permit falls under before you buy devices."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- order
flow += k.h2_tight("THE ORDER, AND WHY IT IS NOT THE ORDER YOU EXPECT")
flow.append(k.body(
    "On a sewered lot, the building permit is the first thing you apply for. "
    "On an unsewered lot — which is most rural Wisconsin — it is close to the "
    "<i>last</i>. Two provisions put the county septic approval in front of "
    "your building permit, and neither is discretionary."))
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp("<b>Soil and site evaluation</b> by a certified soil tester"),
     k.cellp("Three soil profile evaluations minimum, at least one dug as a "
             "full soil pit. You may not do this yourself")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("<b>POWTS design and plans</b>, sealed by a registered designer "
             "or signed by the master plumber who will install it"),
     k.cellp("s. SPS 383.22(2)(c) — again, no owner-prepared option")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("<b>County sanitary permit</b>"),
     k.cellp("The county has <b>30 days</b> to decide once it has all the "
             "information and fees")],
    [k.cellp("<b>4</b>", center=True),
     k.cellp("<b>Zoning / land use, shoreland, floodplain, driveway "
             "access</b>"),
     k.cellp("Local prerequisites; the building permit cannot issue until "
             "they are complete")],
    [k.cellp("<b>5</b>", center=True),
     k.cellp("<b>Wisconsin uniform building permit</b> — with erosion control"),
     k.cellp("<b>10 business days</b> to approve or deny once the file is "
             "complete")],
    [k.cellp("<b>6</b>", center=True),
     k.cellp("<b>Well</b> — drilled any time before you need water; no "
             "routine state permit"),
     k.cellp("But the separation distances in WI.4 constrain where the house "
             "and septic can go, so lay all three out together first")],
]
flow.append(k.ref_table(
    "The sequence on an unsewered parcel",
    [k.cellp("", bold=True), k.cellp("Step", bold=True),
     k.cellp("The part people miss", bold=True)],
    rows, [0.32 * inch, 2.35 * inch, CW - 2.67 * inch]))

flow.append(Spacer(1, 4))
flow.append(k.callout_long("The two sentences that set the order", [
    Paragraph("<b>From the statute.</b> “<i>No county, city, town or village "
              "may issue a building permit for construction of any structure "
              "requiring connection to a private on-site wastewater treatment "
              "system unless a private on-site wastewater treatment system "
              "satisfying all applicable regulations already exists to serve "
              "the proposed structure <b>or all permits necessary to install a "
              "private on-site wastewater treatment system have been "
              "obtained</b>.</i>” (Wis. Stat. s. 145.195(1))", S["body"]),
    Paragraph("<b>From the code, on the building side.</b> “<i>Pursuant to "
              "s. 145.195, Stats., if the proposed construction requires "
              "connection to a private onsite wastewater treatment system, a "
              "Wisconsin uniform building permit may not be issued unless "
              "conformance with s. SPS 383.25(2) has first been "
              "determined.</i>” (s. SPS 320.09(9)(c))", S["body"]),
    Paragraph("<b>The practical consequence.</b> The soil tester is the "
              "critical path on a rural Wisconsin build, not the building "
              "inspector — and soil work has a season. POWTS components may "
              "not be installed “<i>if the soil is frozen at or below the "
              "infiltrative surface</i>”, snow cover must be removed before "
              "excavating, and if the soil “<i>can be rolled into a ¼-inch "
              "wire, the installation may not proceed</i>” "
              "(s. SPS 383.45(2), (3), (4)). Book the soil tester early in the "
              "year.", S["body"]),
]))

# ---------------------------------------------------------------- septic pack
flow += k.h2_tight("THE SANITARY PERMIT PACKAGE", reserve=2.0)
flow.append(k.checklist([
    "<b>Certified soil tester engaged.</b> A soil evaluation “<i>shall be "
    "performed by an individual who is a certified soil tester</i>” "
    "(s. SPS 385.10(1)), and since 1974 no person may even construct soil "
    "bore holes without that certificate (Wis. Stat. s. 145.045(1))",
    "<b>At least three soil profile evaluations</b>, and for a house — well "
    "under 1,000&nbsp;gallons per day — “<i>at least one soil profile evaluation "
    "excavation per treatment or dispersal site shall be constructed as a soil "
    "pit</i>” (s. SPS 385.20(2)(b)1.a. and b.). A soil boring “<i>may not be "
    "created by means of a power auger</i>” (s. SPS 385.20(3)(b)2.)",
    "<b>Soil and site evaluation report</b> on the department's format, every "
    "page signed with the soil tester's identification number and the date "
    "(s. SPS 385.40(2))",
    "<b>POWTS plans</b> either sealed by a registered architect, engineer, "
    "designer of plumbing systems or designer of POWTS, <i>or</i> signed with "
    "license number by the master plumber responsible for installing it "
    "(s. SPS 383.22(2)(c))",
    "<b>Master Plumber or Master Plumber-Restricted Service named</b> — the "
    "application must carry “<i>documentation that the master plumber or the "
    "master plumber-restricted service who is to be responsible for the "
    "installation</i>” (s. SPS 383.21(2)(c)4.)",
    "<b>Sanitary permit application</b> filed with the county — “<i>the "
    "appropriate governmental unit where the POWTS is located or will be "
    "located</i>” (s. SPS 383.21(2)(b)1.). The permit runs to <b>you</b>, the "
    "property owner, not to the installer (Wis. Stat. s. 145.19(1g))",
    "<b>$25 groundwater fee</b> — this one is statewide and fixed by statute "
    "(Wis. Stat. s. 145.19(6)). The base permit fee is set by your county and "
    "is not printed here",
    "<b>Management plan</b> submitted with the design — it is part of the plan "
    "submittal, and it sets your servicing intervals (s. SPS 383.54(1)(b))",
]))
flow.append(k.cite(
    "Term and transfer: a sanitary permit “<i>is valid for 2 years from the "
    "date of issue and renewable for similar periods</i>” and “<i>shall remain "
    "valid to the end of the established period, notwithstanding any change in "
    "the state plumbing code</i>” (Wis. Stat. s. 145.19(7)) — so an issued "
    "permit locks its rules, though a renewal is judged against current rules "
    "(s. SPS 383.21(6)(b)). It may be transferred to a subsequent owner of the "
    "land, who must obtain a new copy from the issuing agent "
    "(s. 145.19(8)). Determination deadline: 30 days after the county has all "
    "required information and fees (s. SPS 383.21(3)(c))."))

# ---------------------------------------------------------------- building
flow += k.h2_tight("THE BUILDING PERMIT PACKAGE", reserve=2.0)
flow.append(k.body(
    "Wisconsin's plan submittal is unusually short, and one sentence in it is "
    "worth real money to an owner-builder."))
flow.append(k.checklist([
    "<b>Wisconsin uniform building permit application</b>, on the form from "
    "the department, the municipality or your UDC inspection agency. "
    "“<i>No application shall be accepted that does not contain all the "
    "information requested on the form</i>” (s. SPS 320.09(1))",
    "<b>At least two sets of plans</b> (s. SPS 320.09(4)), “<i>legible and "
    "drawn to scale or dimensioned</i>” (s. SPS 320.09(5))",
    "<b>Site plan</b> showing the three items listed in the next section",
    "<b>The name of the initial downstream receiving water of the state</b> "
    "from the dwelling, for erosion and sediment control purposes "
    "(s. SPS 320.09(6)(d)) — look it up before you sit down to fill the form",
    "<b>Erosion and sediment control measures</b> shown on the site plan to "
    "comply with s. SPS 321.125",
    "<b>Energy compliance</b> — either the prescriptive table or a UA "
    "calculation; if you use REScheck it must be “<i>a version approved by the "
    "department</i>” (s. SPS 322.31(2)(b))",
    "<b>Sanitary permit already issued</b>, if you are not on a sewer",
    "<b>Every other local prerequisite complete</b> — the permit “<i>shall not "
    "be issued … prior to the receipt of all completed forms, fees, plans, and "
    "documents required to process the application and completion of other "
    "local prerequisite permitting requirements</i>” (s. SPS 320.09(2)(a)4.)",
    "<b>The cautionary statement signed</b> (Wis. Stat. s. 101.65(1r); see "
    "WI.1)",
]))

flow.append(Spacer(1, 4))
flow.append(k.callout_long("Three rights on the building permit worth knowing",
                           [
    Paragraph("<b>1. Nobody can make you buy a stamp.</b> “<i><b>Except as "
              "required under s. SPS 321.33, a municipality exercising "
              "jurisdiction may not require plans or calculations to be "
              "stamped or sealed by an architect or engineer.</b></i>” "
              "(s. SPS 320.09(6)(c)) The one exception is floodplain "
              "construction — and even there, only specific items need a seal, "
              "notably the certification of the actual elevation of the lowest "
              "structural member by “<i>a registered land surveyor, architect "
              "or engineer</i>” (s. SPS 321.33(3)). On an ordinary house on "
              "ordinary ground, your own drawings are enough.", S["body"]),
    Paragraph("<b>2. There is a shot clock.</b> “<i>Action to approve or deny "
              "a uniform building permit application shall be completed within "
              "<b>10 business days</b> of receipt of all forms, fees, plans "
              "and documents required to process the application, and "
              "completion of other local prerequisite permitting "
              "requirements.</i>” (s. SPS 320.09(11))", S["body"]),
    Paragraph("<b>3. You can start the hole before the full permit.</b> "
              "“<i>Construction may begin on footings and foundations prior to "
              "the issuance of the Wisconsin uniform building permit where a "
              "permit to start construction is obtained.</i>” It takes a plot "
              "plan, complete footing and foundation information including "
              "exterior grading, and a fee — and “<i>the issuance of a permit "
              "to start construction shall not influence the approval or "
              "denial of the Wisconsin uniform building permit "
              "application.</i>” (s. SPS 320.09(9)(b)) In a short Wisconsin "
              "build season this is worth weeks.", S["body"]),
]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "Three more things happen at issuance. The <b>state seal</b> is affixed to "
    "the posted permit or the application, with the seal number on both, and "
    "the permit must be “<i>posted in a conspicuous place at the dwelling "
    "site</i>” (s. SPS 320.09(9)(d)). The seal costs <b>$30.00</b> per new "
    "dwelling, paid to the department by whoever issues your permit "
    "(s. SPS 302.34(1)) — your municipality may bill a slightly higher line to "
    "cover handling. And “<i>the name and license number of the Wisconsin "
    "master plumber responsible for the installation of plumbing shall be "
    "entered on the permit by the issuing entity at the time of issuance</i>” "
    "(s. SPS 320.09(9)(a)7.)."))
flow.append(k.callout(
    "The clock that runs against you", [
        Paragraph("“<i>The permit shall expire <b>24 months</b> after issuance "
                  "if the dwelling exterior has not been completed.</i>” "
                  "(s. SPS 320.09(9)(a)5.) Note the trigger is the "
                  "<i>exterior</i>, not the whole house — get the shell closed "
                  "in. Two years is generous for a full-time build and tight "
                  "for a weekends-and-evenings one, which is what most "
                  "owner-builders are actually doing.", S["body"]),
    ]))
flow.append(k.closing_note(
    "Building permit package: Wis. Admin. Code ss. SPS 320.08(1), 320.09(1), "
    "(2)(a)4., (4), (5), (6)(c), (6)(d), (9)(a)5., (9)(a)7., (9)(b), (9)(c), "
    "(9)(d), (11), 302.34(1), 321.33(3), 322.31(2)(b). Chapter SPS 320 as "
    "published, Register August 2026 No. 848."))

# ---------------------------------------------------------------- site plan
flow += k.h2_tight("WHAT THE SITE PLAN MUST SHOW — THE COMPLETE LIST",
                   reserve=2.0)
flow.append(k.body(
    "This is the entire statewide requirement. Three items, quoted in full."))
flow.append(k.callout_long("Wis. Admin. Code s. SPS 320.09(5)(a)", [
    Paragraph("“<i><b>(a) Site plan.</b> The site plan shall show all of the "
              "following:</i>”", S["body"]),
    Paragraph("“<i>1. The location of the dwelling and any other buildings, "
              "<b>wells</b>, surface waters and <b>dispersal systems</b> on "
              "the site with respect to <b>property lines</b> and surface "
              "waters adjacent to the site.</i>”", S["body"]),
    Paragraph("“<i>2. The areas of <b>land-disturbing construction "
              "activity</b> and the location of all <b>erosion and sediment "
              "control measures</b> to be employed in order to comply with "
              "s. SPS 321.125.</i>”", S["body"]),
    Paragraph("“<i>3. The <b>pre-construction ground surface slope and "
              "direction of runoff flow</b> within the proposed areas of land "
              "disturbance.</i>”", S["body"]),
    Paragraph("<b>Two things are notable.</b> The well and the septic "
              "dispersal system are already required on the building-permit "
              "site plan — so draw all three together from the start. And "
              "there is <b>no specified scale</b>: “to scale <i>or "
              "dimensioned</i>” is the whole requirement. Anyone who tells you "
              "Wisconsin demands 1&nbsp;inch = 100&nbsp;feet on this drawing is adding a "
              "rule the code does not contain.", S["body"]),
]))
flow.append(k.cite(
    "The sanitary-permit site plan is a different document with a different "
    "rule — see WI.4. Unlike this one, it may not be drawn by the owner: "
    "s. SPS 385.10(2) restricts site evaluation, including determining "
    "“<i>land slope or setback distances to topographic or other site "
    "features</i>”, to a closed list of credentialed people that does not "
    "include the property owner."))

# ---------------------------------------------------------------- editions
flow += k.h2_tight("WHAT CODE IS ACTUALLY IN FORCE", reserve=2.0)
flow.append(k.body(
    "The Uniform Dwelling Code is <b>Wisconsin's own code</b>, not an adoption "
    "of the International Residential Code. It is six chapters, and two of "
    "them are pointers to other chapters — which is why guides so often name "
    "the wrong one."))
rows = [
    [k.cellp("<b>SPS 320</b>"), k.cellp("Administration — permits, plans, "
                                        "inspections, adopted standards"),
     k.cellp("Register August 2026 No. 848")],
    [k.cellp("<b>SPS 321</b>"), k.cellp("Construction — structure, frost, "
                                        "loads, stairs, egress, floodplains"),
     k.cellp("Register November 2024 No. 827")],
    [k.cellp("<b>SPS 322</b>"), k.cellp("Energy conservation — Wisconsin's own "
                                        "prescriptive tables"),
     k.cellp("Register November 2024 No. 827")],
    [k.cellp("<b>SPS 323</b>"), k.cellp("Heating, ventilating and air "
                                        "conditioning"),
     k.cellp("—")],
    [k.cellp("<b>SPS 324</b>"), k.cellp("Electrical — <b>a pointer</b>, to "
                                        "ch. SPS 316"),
     k.cellp("—")],
    [k.cellp("<b>SPS 325</b>"), k.cellp("Plumbing — <b>a pointer</b>, to "
                                        "chs. SPS 381 to 387"),
     k.cellp("—")],
]
flow.append(k.ref_table(
    "The six UDC chapters (“the code” = chs. SPS 320 to 325, s. SPS 320.07(16))",
    [k.cellp("Chapter", bold=True), k.cellp("What it covers", bold=True),
     k.cellp("As published", bold=True)],
    rows, [0.95 * inch, CW - 3.15 * inch, 2.2 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout_long(
    "⚠ THE ELECTRICAL CODE CHANGED ON 1 SEPTEMBER 2026", [
        Paragraph("Almost every Wisconsin guide in circulation says the state "
                  "is on the <b>2017</b> National Electrical Code. That was "
                  "true until the first of this month. It is not true now.",
                  S["body"]),
        Paragraph("“<i>The following standard is incorporated by reference "
                  "into this chapter … NFPA 70 National Electrical Code, "
                  "(NEC) – <b>2023</b>, including all Temporary Interim "
                  "Amendments and Errata prior to January 1, 2025.</i>” "
                  "(s. SPS 316.007(1)(a))", S["body"]),
        Paragraph("The amendment is <b>CR 26-016, Register June 2026 No. 846, "
                  "effective 1 September 2026</b>. Six NEC editions of change "
                  "arrived at once — the 2017 book to the 2023 book — so "
                  "expect differences in receptacle placement, GFCI and AFCI "
                  "scope, service disconnects and surge protection. Do not "
                  "wire from a 2017-vintage cheat sheet.", S["body"]),
        Paragraph("<b>Which edition applies to you is a timing question.</b> "
                  "For additions and alterations the chapter is explicit: they "
                  "“<i>shall comply with all provisions of this chapter at the "
                  "time of permit application or, if no permit is required, "
                  "the beginning of the project</i>” (s. SPS 316.003(6)). For "
                  "new construction the chapter applies to “<i>all new "
                  "installations</i>” (s. SPS 316.003(1)). If your permit "
                  "application went in before 1 September, <b>ask your "
                  "electrical inspector in writing which edition your job is "
                  "being held to</b> and write the answer on this page.",
                  S["body"]),
    ]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "Two related points people get wrong. First, the <b>UDC itself does not "
    "adopt the NEC</b> — NFPA 70 appears nowhere in the adoption tables at "
    "s. SPS 320.24. Electrical reaches your house through ch. SPS 316, and "
    "local electrical ordinances must “<i>strictly conform</i>” to the state "
    "code (Wis. Stat. s. 101.86(1)(a)). Second, <b>SPS 322 is not an IECC "
    "adoption.</b> Wisconsin writes its own envelope table; the only IECC "
    "reference on the page is a note that “<i>the IECC 2009 version of "
    "REScheck meets the thermal envelope requirements of this code</i>.” "
    "Saying Wisconsin “adopts the 2009 IECC” overstates what the chapter "
    "does."))
rows = [
    [k.cellp("<b>SEI/ASCE 32-01</b>"),
     k.cellp("Design and Construction of Frost-Protected Shallow Foundations "
             "— the alternative to a 48-inch footing")],
    [k.cellp("<b>ANSI/AWC NDS-2015</b>"),
     k.cellp("National Design Specification for Wood Construction")],
    [k.cellp("<b>ANSI/AWC PWF-2007</b>"),
     k.cellp("Permanent Wood Foundation Design Specification")],
    [k.cellp("<b>ANSI/TPI 1-2007</b>"),
     k.cellp("National Design Standard for Metal Plate Connected Wood Truss "
             "Construction")],
    [k.cellp("<b>NFPA 54 / ANSI Z223.1 2015</b>"),
     k.cellp("National Fuel Gas Code — Wisconsin uses this rather than the "
             "IFGC")],
    [k.cellp("<b>NFPA 13D 2013</b>"),
     k.cellp("Sprinklers in one- and two-family dwellings — adopted as a "
             "<i>standard</i>; the UDC does not require sprinklers in a "
             "house")],
    [k.cellp("<b>ICC 400-2012</b>"),
     k.cellp("Design and Construction of Log Structures — if you are building "
             "a log home, this is your standard")],
    [k.cellp("<b>ACI 318-14, 332-14</b>"),
     k.cellp("Structural and residential concrete")],
]
flow.append(k.ref_table(
    "Standards the UDC adopts by reference (s. SPS 320.24, Tables 320.24-1 to "
    "320.24-13)",
    [k.cellp("Standard", bold=True), k.cellp("What it governs", bold=True)],
    rows, [2.0 * inch, CW - 2.0 * inch]))
flow.append(k.cite(
    "Selected from the adoption tables as published, Register August 2026 "
    "No. 848; the full tables also cover ASTM materials, ASHRAE handbooks, "
    "SMACNA duct standards, NAIMA and NIST references. An alternate standard "
    "“<i>equivalent to or more stringent than</i>” an adopted one may be used "
    "with department approval, and the department has <b>40 business days</b> "
    "to determine such an application (s. SPS 320.24(3))."))

# ---------------------------------------------------------------- zones
flow += k.h2_tight("THE TWO ZONE MAPS THAT RUN IN OPPOSITE DIRECTIONS",
                   reserve=2.2)
flow.append(k.body(
    "Wisconsin publishes two “Zone 1 / Zone 2” maps in the Uniform Dwelling "
    "Code. One sets your roof load. The other sets your insulation. <b>They "
    "are numbered the opposite way round.</b> Carry a zone number from one "
    "table to the other and you get both answers wrong, in opposite "
    "directions — under-framing a northern roof while under-insulating a "
    "northern wall."))
rows = [
    [k.cellp("<b>Zone 1</b>"),
     k.cellp("the <b>NORTH</b> — roof load <b>40&nbsp;psf</b>"),
     k.cellp("<b>everything else</b> — the southern and central counties")],
    [k.cellp("<b>Zone 2</b>"),
     k.cellp("the <b>SOUTH</b> — roof load <b>30&nbsp;psf</b>"),
     k.cellp("the <b>15 northern counties</b> named below")],
]
flow.append(k.ref_table(
    "Same words, opposite meanings",
    [k.cellp("", bold=True),
     k.cellp("Roof / snow load — Figure 321.02", bold=True),
     k.cellp("Energy — s. SPS 322.31(1)(b)", bold=True)],
    rows, [0.75 * inch, (CW - 0.75 * inch) / 2, (CW - 0.75 * inch) / 2]))
flow.append(k.cite(
    "Figure 321.02, “Zone Map for Roof Loads”, prints the legend "
    "“Zone 1 — 40 P.S.F. / Zone 2 — 30 P.S.F.” with Zone 1 covering the "
    "northern part of the state. Section SPS 322.31(1)(b) reads: “<i>In Tables "
    "322.31-1 and 322.31-2, zone 2 consists of the following 15 northern "
    "counties: Ashland, Bayfield, Burnett, Douglas, Florence, Forest, Iron, "
    "Langlade, Lincoln, Oneida, Price, Sawyer, Taylor, Vilas and Washburn. "
    "Zone 1 consists of all other counties not included in zone 2.</i>” Both "
    "chapters as published, Register November 2024 No. 827."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "Worked example, so this sticks", [
        Paragraph("A house in <b>Vilas County</b> is roof-load <b>Zone 1 "
                  "(40&nbsp;psf)</b> and energy <b>Zone 2 (R-21 walls, R-38 "
                  "floors)</b>. A house in <b>Dane County</b> is roof-load "
                  "<b>Zone 2 (30&nbsp;psf)</b> and energy <b>Zone 1 (R-20 walls, "
                  "R-30 floors)</b>. The zone number flips; the severity does "
                  "not. North is always the harder number in both tables — it "
                  "is only the <i>label</i> that reverses.", S["body"]),
        Paragraph("Do not read a snow load off the map for your county from "
                  "this kit. The zone boundary is drawn across county lines "
                  "and there is a separate dashed line near the Door "
                  "peninsula. Have your inspector or your truss supplier "
                  "confirm the zone for the parcel, and write it on your "
                  "permit record.", S["body"]),
    ]))

# ---------------------------------------------------------------- energy
flow += k.h2_tight("THE ENERGY TABLE, IN FULL", reserve=2.2)
rows = [
    [k.cellp("Fenestration U-factor"), k.cellp("0.35", center=True),
     k.cellp("0.35", center=True)],
    [k.cellp("Skylight U-factor"), k.cellp("0.60", center=True),
     k.cellp("0.60", center=True)],
    [k.cellp("Ceiling R-value"), k.cellp("49", center=True),
     k.cellp("49", center=True)],
    [k.cellp("Wood frame wall R-value"), k.cellp("20 or 13+5", center=True),
     k.cellp("21", center=True)],
    [k.cellp("Mass wall R-value"), k.cellp("15/19", center=True),
     k.cellp("19/21", center=True)],
    [k.cellp("Floor R-value"), k.cellp("30", center=True),
     k.cellp("38", center=True)],
    [k.cellp("Basement wall R-value"), k.cellp("15/19", center=True),
     k.cellp("15/19", center=True)],
    [k.cellp("Crawl space wall R-value"), k.cellp("10/13", center=True),
     k.cellp("10/13", center=True)],
    [k.cellp("Heated slab R-value"), k.cellp("10/15", center=True),
     k.cellp("10/15", center=True)],
    [k.cellp("Unheated slab R-value"), k.cellp("10", center=True),
     k.cellp("10", center=True)],
]
flow.append(k.ref_table(
    "Table 322.31-1 — Insulation and Fenestration Requirements by Component",
    [k.cellp("Component", bold=True),
     k.cellp("Zone 1 — most of the state", bold=True),
     k.cellp("Zone 2 — the 15 northern counties", bold=True)],
    rows, [CW - 4.0 * inch, 2.0 * inch, 2.0 * inch]))
flow.append(k.cite(
    "R-values are minimums, U-factors are maximums. “15/19” means R-15 "
    "continuous insulated sheathing on the interior or exterior of the home "
    "<i>or</i> R-19 cavity insulation at the interior of the basement wall, "
    "and may also be met with R-13 cavity plus R-5 continuous. “10/13” follows "
    "the same pattern. “13+5” means R-13 cavity plus R-5 insulated sheathing. "
    "R-20 and R-21 “<i>may be compressed into a 2X6 cavity</i>”. The floor "
    "value may instead be “<i>insulation sufficient to fill the framing cavity "
    "with a minimum of R-19</i>”. Heated-slab insulation must extend downward "
    "48&nbsp;inches, or to the bottom of the slab and then horizontally for a total "
    "of 48&nbsp;inches. Table and footnotes as published, Register November 2024 "
    "No. 827."))

flow.append(Spacer(1, 4))
flow.append(k.body(
    "There is a second way to comply. If the whole-dwelling envelope UA is at "
    "or below the UA you would get from the equivalent U-factors in Table "
    "322.31-2 over the same areas, you comply — calculated by a method "
    "“<i>consistent with the ASHRAE Handbook of Fundamentals</i>” and "
    "including “<i>the thermal bridging effects of framing materials</i>” "
    "(s. SPS 322.31(2)(a)). That is the trade-off path REScheck automates."))

rows = [
    [k.cellp("Natural gas and propane furnace"),
     k.cellp("<b>90% AFUE</b>", center=True)],
    [k.cellp("Natural gas and propane hot water boilers"),
     k.cellp("<b>90% AFUE</b>", center=True)],
    [k.cellp("Oil-fired furnaces"), k.cellp("<b>83% AFUE</b>", center=True)],
    [k.cellp("Oil-fired hot water boilers"),
     k.cellp("<b>84% AFUE</b>", center=True)],
]
flow.append(k.ref_table(
    "Table 322.31-3 — Warm Air Furnaces and Boilers, Minimum Efficiency",
    [k.cellp("Equipment type", bold=True),
     k.cellp("Minimum efficiency", bold=True)],
    rows, [CW - 2.2 * inch, 2.2 * inch]))
flow.append(k.cite(
    "Test procedures: DOE 10 CFR Part 430 or ANSI Z21.47 for gas and propane "
    "furnaces, DOE 10 CFR Part 430 for gas and propane hot water boilers and "
    "oil-fired hot water boilers, DOE 10 CFR Part 430 or UL 727 for oil-fired "
    "furnaces. There is a trade-off: in new construction a unit meeting only "
    "the federal standard may be installed “<i>if the dwelling thermal "
    "envelope requirements of Table 322.31-4 are met</i>” "
    "(s. SPS 322.31(3)(b)). Check that table with your inspector before "
    "counting on it — it is not reproduced here."))

# ---------------------------------------------------------------- structure
flow += k.h2_tight("STRUCTURAL MINIMUMS YOU WILL DESIGN TO", reserve=2.2)
flow.append(k.callout_long("Frost depth — s. SPS 321.16", [
    Paragraph("“<i>Footings and foundations, <b>including those for landings "
              "and stoops</b>, shall be placed below the frost penetration "
              "level <b>or at least 48&nbsp;inches below adjacent grade, whichever "
              "is deeper</b>, except as allowed under sub. (2).</i>” "
              "and “<i>Footings may not be placed on frozen material.</i>” "
              "(s. SPS 321.16(1))", S["body"]),
    Paragraph("Read the “whichever is deeper” carefully — <b>48&nbsp;inches is a "
              "floor, not a target</b>. In the north the measured frost "
              "penetration governs and it is deeper. And note that landings "
              "and stoops are expressly caught, which is where owner-builders "
              "most often get written up.", S["body"]),
    Paragraph("Three exceptions exist (s. SPS 321.16(2)): a frost-protected "
              "shallow foundation designed to <b>SEI/ASCE 32-01</b>; the "
              "portion of a footing directly under a window areaway; and "
              "bearing <b>directly on bedrock</b> less than 48&nbsp;inches down, "
              "provided the rock is cleaned of all earth, clay in crevices is "
              "removed to the frost penetration level or 1.5 times the crevice "
              "width, whichever is less, and water is prevented from "
              "collecting along the foundation.", S["body"]),
]))

flow.append(Spacer(1, 6))
rows = [
    [k.cellp("Floors"), k.cellp("40", center=True)],
    [k.cellp("Garage floors"), k.cellp("50", center=True)],
    [k.cellp("Exterior balconies, decks, porches"), k.cellp("40", center=True)],
    [k.cellp("Ceilings (with storage)"), k.cellp("20", center=True)],
    [k.cellp("Ceilings (without storage)"), k.cellp("5", center=True)],
]
flow.append(k.ref_table(
    "Table 321.02-1 — Live Load (pounds per square foot)",
    [k.cellp("Component", bold=True),
     k.cellp("Live load (psf)", bold=True)],
    rows, [CW - 2.0 * inch, 2.0 * inch]))
flow.append(k.cite(
    "Wind: a dwelling shall withstand “<i>either a horizontal and uplift "
    "pressure of 20 pounds per square foot acting over the surface area or the "
    "wind loads determined in accordance with ASCE 7-05</i>” "
    "(s. SPS 321.02(1)(c)), with a Note that ASCE 7-05 “<i>allows for "
    "substantial reduction from 20&nbsp;psf</i>”. Snow: roofs “<i>shall be designed "
    "and constructed to support the minimum snow loads listed on the zone "
    "map</i>” (s. SPS 321.02(1)(b)2.) — see the zone warning above."))

# ---------------------------------------------------------------- erosion
flow += k.h2_tight("EROSION CONTROL", reserve=1.8)
flow.append(k.body(
    "Erosion control is not a separate adventure in Wisconsin — it rides on "
    "the building permit, and the same authority that issues one handles the "
    "other. What it does have is a specific slope trigger written into the "
    "statute: the rules “<i>shall require the use of more restrictive or "
    "additional practices on an area with a slope that is greater than "
    "<b>12&nbsp;percent</b></i>” (Wis. Stat. s. 101.653(2)(b)). Your site plan has "
    "to show the pre-construction slope anyway, so measure it early."))
flow.append(k.checklist([
    "Land-disturbing areas and control measures shown on the site plan "
    "(s. SPS 320.09(5)(a)2.)",
    "Pre-construction ground surface slope and direction of runoff flow shown "
    "(s. SPS 320.09(5)(a)3.) — and check whether any of it exceeds 12&nbsp;percent",
    "The initial downstream receiving water of the state identified "
    "(s. SPS 320.09(6)(d))",
    "If you will disturb <b>one acre or more</b>, ask your county or the "
    "Department of Natural Resources about a construction site stormwater "
    "permit — that is a separate DNR program, not part of your building "
    "permit",
    "Ask whether your municipality has imposed erosion requirements more "
    "stringent than the code, which s. SPS 320.02(2)(e)1. permits when "
    "directed by a federal EPA order or a DNR rule under s. NR 151.004",
]))

# ---------------------------------------------------------------- record
flow += k.h2_tight("PERMIT RECORD — FILL THIS IN AS EACH ONE ISSUES",
                   reserve=2.0)
flow += k.check_table(
    "Every approval this build needs",
    [("Soil and site evaluation — certified soil tester",
      [("Tester / cert. no.", 0.5), ("Report date", 0.5)]),
     ("County sanitary permit — POWTS",
      [("Permit no.", 0.5), ("Expires", 0.5)]),
     ("Master plumber engaged for the POWTS",
      [("Name", 0.6), ("License no.", 0.4)]),
     ("Zoning / land use permit",
      [("Office", 0.6), ("Permit no.", 0.4)]),
     ("Shoreland or floodplain approval, if applicable",
      [("Office", 0.6), ("Ref.", 0.4)]),
     ("Driveway / access permit",
      [("Authority", 0.6), ("Permit no.", 0.4)]),
     ("Address assigned (rural 911 addressing)",
      [("Address", 1.0)]),
     ("Wisconsin uniform building permit",
      [("Permit no.", 0.5), ("Seal no.", 0.5)]),
     ("Enforcing authority / UDC inspection agency",
      [("Name", 1.0)]),
     ("Erosion control approval",
      [("Ref.", 0.5), ("Slope over 12%?", 0.5)]),
     ("Electrical code edition my permit is held to",
      [("2017 or 2023 NEC", 0.6), ("Confirmed by", 0.4)]),
     ("Roof-load zone and energy zone for this parcel",
      [("Roof zone", 0.5), ("Energy zone", 0.5)]),
     ("Well construction report filed by the driller",
      [("Driller", 0.6), ("Date", 0.4)]),
     ("Water sample results — coliform and nitrate",
      [("Date", 0.5), ("Result", 0.5)])],
    notes_header="Notes")

flow.append(Spacer(1, 4))
flow.append(k.ref_table(
    "Sources — every Wisconsin claim in this document (verified September 2026)",
    [k.cellp("What this document states", bold=True),
     k.cellp("Authority", bold=True)],
    [[k.cellp("Sanitary permit before the building permit"),
      k.cellp("Wis. Stat. s. 145.195(1); s. SPS 320.09(9)(c)")],
     [k.cellp("$25 groundwater fee; 2-year term; transferable"),
      k.cellp("Wis. Stat. s. 145.19(6), (7), (8)")],
     [k.cellp("County has 30 days to decide the sanitary permit"),
      k.cellp("s. SPS 383.21(3)(c)")],
     [k.cellp("Soil evaluation by a certified soil tester; three "
              "evaluations, one a pit"),
      k.cellp("ss. SPS 385.10(1), 385.20(2)(b); Wis. Stat. s. 145.045(1)")],
     [k.cellp("Two sets of plans; the three-item site plan"),
      k.cellp("s. SPS 320.09(4), (5)(a)")],
     [k.cellp("No architect or engineer seal may be required"),
      k.cellp("s. SPS 320.09(6)(c); exception s. SPS 321.33")],
     [k.cellp("Ten business days to approve or deny"),
      k.cellp("s. SPS 320.09(11)")],
     [k.cellp("Footing and foundation permit to start construction"),
      k.cellp("s. SPS 320.09(9)(b)")],
     [k.cellp("Permit expires at 24 months if the exterior is not complete"),
      k.cellp("s. SPS 320.09(9)(a)5.")],
     [k.cellp("$30 state seal per new dwelling"),
      k.cellp("s. SPS 302.34(1)")],
     [k.cellp("2023 National Electrical Code, effective 1 September 2026"),
      k.cellp("s. SPS 316.007(1)(a); CR 26-016, Register June 2026 No. 846")],
     [k.cellp("The UDC does not itself adopt the NEC"),
      k.cellp("Negative finding — Tables 320.24-1 to 320.24-13")],
     [k.cellp("Roof-load zones 40 and 30&nbsp;psf; energy zones inverted"),
      k.cellp("Figure 321.02; s. SPS 322.31(1)(b)")],
     [k.cellp("The prescriptive envelope table and its footnotes"),
      k.cellp("Table 322.31-1")],
     [k.cellp("90% AFUE gas furnaces and boilers"),
      k.cellp("Table 322.31-3")],
     [k.cellp("48&nbsp;inches or below frost penetration, whichever is deeper"),
      k.cellp("s. SPS 321.16(1)(a)")],
     [k.cellp("Live loads; 20&nbsp;psf wind alternative"),
      k.cellp("Table 321.02-1; s. SPS 321.02(1)(c)")],
     [k.cellp("Erosion control: more restrictive above 12&nbsp;percent slope"),
      k.cellp("Wis. Stat. s. 101.653(2)(b)")]],
    [CW - 2.65 * inch, 2.65 * inch]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "wi-permit-kit",
                       "WI.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
