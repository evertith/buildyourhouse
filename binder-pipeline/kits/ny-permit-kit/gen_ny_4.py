#!/usr/bin/env python3
"""NY.4 Where to File Directory.

Every web address in this document was confirmed to resolve in September 2026.
No phone numbers appear anywhere in this kit — they go stale faster than
anything else on a printed page, and every office below can be reached from its
own site.

The organizing idea: New York does NOT publish which government issues the
permit for a given parcel. DOS says only that it enforces "in the place of only
a limited number of local governments," and no list was retrievable. So this
document is a method — one question to one clerk, in the statutory order — and
then the offices that exist whichever rung answers: the county health
department that approves septic and wells, the two regional overlays that
reach one house, and the county license laws that mostly exclude a new home.

Verified sources:
  Exec. Law § 381(2), § 372(11)   the ladder; village before town
  19 NYCRR Part 1202             where DOS is the permit office
  10 NYCRR § 75.5; App. 75-A; App. 5-B; DOH Fact Sheet #6
  2025 RCNYS [NY] P2602.1.1, P2602.1.2
  ECL § 15-1525(6), § 15-1527    local well-driller laws; Long Island 45 gpm
  Exec. Law §§ 806, 809, 810     Adirondack Park shoreline and permits
  10 NYCRR § 128-3.8             NYC watershed septic
  Suffolk § 563-16; Nassau Admin. Code § 21-11.1; Putnam Ch. 135 § 135-3(C);
  Westchester § 863.312, .313    county home-improvement laws
  Exec. Law § 379(3)             zoning stays local
  19 NYCRR § 1203.3(a)(2), (3)   tax map number; site plan per boundary survey
  2025 RCNYS [NY] R306.1         shaded X and B zones

DELIBERATELY NOT PRINTED:
  - A list of municipalities where the county or DOS is the permit office.
    Not retrievable; the verification step is printed instead.
  - Any Long Island county sanitary-code number for wells or septic. Not read.
  - Rockland County's Chapter 286 definitions. Text not retrievable; the
    reader is told to obtain the current chapter from the county.
  - Any fee, anywhere.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

import kit as k

S = k.S
CW = k.CW
sec = k.sec
NB = k.NB
CITE = k.CITE_COL

FORM_ID = "NY.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "How to identify your permit office on the ladder, who approves the "
    "septic system and the well, the two overlays that reach one house, and "
    "the county license laws that do — and do not — reach a new home.")

flow.append(k.disclaimer(
    "Every web address here was checked in September 2026. No phone numbers "
    "appear anywhere in this kit."))
flow.append(Spacer(1, 10))

# ------------------------------------------------------------ the method
flow += k.h2_tight("NO LIST EXISTS — HERE IS THE ONE QUESTION THAT REPLACES IT",
                   2.2)
flow.append(k.body(
    "Most states leave you ringing round to find out whether anybody permits "
    "your parcel. New York settles <i>whether</i> — somebody always does — "
    "and leaves you to find out <i>who</i>. The Department of State enforces "
    "the code “in the place of only a limited number of local governments,” "
    "and publishes no list of them; counties run enforcement for many towns "
    "by agreement, and publish no list either. The statute fixes the order "
    "of the question, so ask it in that order."))
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp("<b>Village, then town, then city</b>"),
     k.cellp("Inside an incorporated village the <b>village</b> is your "
             "local government; a town is the local government only "
             "“outside the area of any incorporated village” "
             f"({sec('372(11)')}). Ask the clerk: does the municipality run a "
             "code enforcement program under 19 NYCRR Part 1203, and who is "
             "the code enforcement officer?")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("<b>The county</b>"),
     k.cellp("If the local government enacted a local law declining to "
             "enforce, or contracted the job to the county, the county's "
             "code office issues the permit. Ask the same clerk which county "
             "office; then confirm with that office directly.")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("<b>The Department of State</b>"),
     k.cellp("If neither local government nor county enforces, DOS does, "
             "under Part 1202, through the Division of Building Standards "
             "and Codes' regional office for your county. The regional "
             "offices are listed at <b>dos.ny.gov/building-standards-and-"
             "codes</b>.")],
]
flow.append(k.ref_table(
    f"The ladder, in the order Executive Law {sec('381(2)')} fixes it",
    [k.cellp("", bold=True, center=True), k.cellp("Rung", bold=True),
     k.cellp("Who to ask, and what", bold=True)],
    rows, [0.35 * inch, 1.6 * inch, CW - 1.95 * inch]))
flow.append(k.cite(
    "Get the answer in writing and date it. If the clerk's answer is “we use "
    "a company for that,” ask whether the company acts <i>for the "
    "municipality</i> under a contract — in which case you are on rung 1 and "
    "the permit still issues from the town — or whether the town has "
    "declined enforcement altogether. The two sound alike on the phone and "
    "are different offices, different fee schedules and different local "
    "laws."))

# ------------------------------------------------------------ DOS as AHJ
flow += k.h2_tight("IF THE DEPARTMENT OF STATE IS YOUR PERMIT OFFICE", 2.0)
flow.append(k.body(
    "19 NYCRR Part 1202 is the procedure “in the circumstances in which the "
    "Secretary of State, through the Department of State (the department), "
    "will administer and enforce the Uniform Code and Energy Code in the "
    "place and stead of a local government or county” "
    f"({sec('1202.1(a)')}). Four things change; a fifth — the eight "
    "permit exemptions apply by rule rather than by local choice "
    f"({sec('1202.3(b)')}) — is in NY.5."))
rows = [
    [k.cellp("The permit comes from Albany"),
     k.cellp("“No person shall commence any work for which a building permit "
             "is required without first having obtained a building permit "
             "<b>from the department</b>.”"),
     k.cellp("19 NYCRR<br/>" + sec("1202.3(a)"))],
    [k.cellp("Two signatures"),
     k.cellp("The application “shall be signed by the owner of the building "
             "or structure <b>and the owner of the real property</b>, if "
             "different.”"),
     k.cellp("19 NYCRR<br/>" + sec("1202.3(c)"))],
    [k.cellp("You supply the design criteria"),
     k.cellp("“The owner shall be responsible for providing the department "
             "with the climatic and geographic design criteria” — snow, "
             "wind, seismic, frost, termite, winter design temperature, ice "
             "barrier, air freezing index, mean annual temperature — “as "
             "established by the city, town, or village.” If the town never "
             "set them, a licensed architect or engineer establishes them."),
     k.cellp("19 NYCRR<br/>" + sec("1202.12(a)") + ", (b)")],
    [k.cellp("Third-party fees are yours"),
     k.cellp("DOS may contract inspections to a third party, and “the owner "
             "shall pay the associated fee prescribed by this Part, including "
             "but not limited to the fee associated with the third-party "
             "services.” The displaced town “shall not charge or collect "
             "fees.”"),
     k.cellp("19 NYCRR<br/>" + sec("1202.1(c)") + ";<br/>Exec. Law<br/>"
             + sec("381(5)(a)"))],
]
flow.append(k.ref_table(
    "Part 1202 — what is different when DOS is the office",
    [k.cellp("Change", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - CITE, CITE]))

# ------------------------------------------------------------ health
flow += k.h2_tight("SEPTIC AND WELLS — THE COUNTY HEALTH DEPARTMENT", 2.2)
flow.append(k.body(
    "The code official enforces both — [NY] P2602.1.2 pulls the Health "
    "Department's Appendix 75-A into the Uniform Code for septic, and "
    "[NY] P2602.1.1 pulls Appendix 5-B in for wells — but the <b>approver</b> "
    "is the local health department: the county health department, or in the "
    "counties without a full-service one, the State Health Department's "
    "district office. DOH Fact Sheet #6, written for code officials: "
    "“Approvals for deviations (e.g., ‘specific waivers’) from the standards "
    "can only be granted by the local health department (LHD i.e., county "
    "health department or NYS District Office) having jurisdiction.”"))
rows = [
    [k.cellp("<b>Which office</b>"),
     k.cellp("DOH publishes the county environmental health programs at "
             "<b>health.ny.gov/environmental/water/drinking/ctyadd1.htm</b> "
             "and its district offices at <b>…/distphn.htm</b>. Find your "
             "county on the first page; if it is not there, use the second.")],
    [k.cellp("<b>Septic</b>"),
     k.cellp("Plans “shall be prepared directly by or under the supervision "
             f"of a design professional” (10 NYCRR {sec('75.5(b)')}) to "
             "Appendix 75-A, and go to the health department for approval. "
             "An <b>alternative</b> system needs prior review and approval, "
             "a design professional supervising construction, and a "
             f"post-construction certification ({sec('75.5(c)')}). NY.2 has "
             "the distances and sizes.")],
    [k.cellp("<b>Well</b>"),
     k.cellp("Drilled only by a DEC-registered driller ([NY] P2602.1.1). "
             "Check registration at <b>appfactory.dec.ny.gov/WaterWell/"
             "Contractor_Search</b>. A local well-driller licensing law is "
             "not preempted if it is “at least as comprehensive” "
             f"(ECL {sec('15-1525(6)')}), so ask the county whether it has "
             "one.")],
    [k.cellp("<b>Long Island</b>"),
     k.cellp("A DEC well permit under ECL " + sec("15-1527") + " is needed in "
             "Nassau or Suffolk only where pumping capacity exceeds "
             "<b>45&#160;gallons a minute</b> — an ordinary house well is "
             "below it. The Nassau and Suffolk county sanitary codes govern "
             "house wells and septic instead; <b>they were not read for this "
             "kit</b>. Go to the county health department first.")],
    [k.cellp("<b>Inside the NYC watershed</b>"),
     k.cellp("New York City's Department of Environmental Protection must "
             "also approve — see the next section.")],
]
flow.append(k.ref_table(
    "Who approves what, on the health side",
    [k.cellp("", bold=True), k.cellp("Where to go", bold=True)],
    rows, [1.45 * inch, CW - 1.45 * inch]))

# ------------------------------------------------------------- overlays
flow += k.h2_tight("TWO OVERLAYS THAT REACH ONE HOUSE — CHECK THE MAP FIRST",
                   2.4)
flow.append(k.body(
    "Both are gated on geography and neither is part of the Uniform Code. If "
    "your parcel is inside either, it adds an approval and changes the septic "
    "setbacks. If it is not, skip this section."))
flow.append(k.callout_long(
    "The Adirondack Park — Executive Law Article 27", [
        Paragraph("<b>Shoreline setbacks apply everywhere in the Park</b>, "
                  "whether or not the Agency permits your project. Minimum "
                  "setback of a principal building from the mean high-water "
                  "mark: <b>50&#160;ft</b> in hamlet and moderate-intensity "
                  "areas, <b>75&#160;ft</b> in low-intensity and rural-use "
                  "areas, <b>100&#160;ft</b> in resource-management areas "
                  f"({sec('806(1)(a)(2)')}). “The minimum setback of any "
                  "on-site sewage drainage field or seepage pit shall be "
                  "<b>one hundred feet</b> from the mean high-water mark in "
                  f"all land use areas” ({sec('806(1)(b)')}). Lot-width and "
                  "tree-cutting rules sit alongside.", S["body"]),
        Paragraph("<b>When you need an Agency permit.</b> A single-family "
                  "dwelling in a <b>Resource Management</b> area is a class B "
                  f"regional project ({sec('810(2)(d)(1)')}); so is one within "
                  "one-eighth mile of wilderness, primitive or canoe forest "
                  "preserve, or within 150&#160;ft (Rural Use) or 300&#160;ft "
                  "(Resource Management) of a state or federal highway "
                  f"({sec('810(2)(c)(17)')}, (d)(9)). A class B project in a "
                  "land use area without an Agency-approved local program "
                  f"needs an Agency permit before undertaking ({sec('809(2)(a)')}). "
                  "A single-family dwelling is a “minor project” — deemed "
                  "complete on receipt, decided within <b>45&#160;days</b> "
                  f"({sec('809(1)')}). Start at <b>apa.ny.gov/permitting/"
                  "laws.html</b>.", S["body"]),
    ]))
flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "The New York City watershed — 10 NYCRR Part 128", [
        Paragraph("In the watershed towns of Delaware, Greene, Schoharie, "
                  "Sullivan and Ulster counties west of the Hudson, and "
                  "Putnam, Westchester and Dutchess east of it, “the design, "
                  "treatment, construction, maintenance and operation of new "
                  "subsurface sewage treatment systems, and the plans "
                  "therefor, require the review and approval of the "
                  "Department” — New York City's Department of Environmental "
                  f"Protection ({sec('128-3.8(a)(1)')}). No part of a new "
                  "absorption field may be “within the limiting distance of "
                  "<b>100&#160;feet</b> of a watercourse or wetland or "
                  "<b>300&#160;feet</b> of a reservoir, reservoir stem or "
                  f"controlled lake” ({sec('128-3.8(a)(5)')}).", S["body"]),
        Paragraph("The parcel test is DEP's watershed map, reached from "
                  "<b>nyc.gov/site/dep/environment/regulations.page</b>. "
                  "Being in one of those counties does not put you in the "
                  "watershed; being on the map does.", S["body"]),
    ]))

# -------------------------------------------------------- county licenses
flow += k.h2_tight("COUNTY HOME-IMPROVEMENT LICENSE LAWS — WHICH REACH A "
                   "NEW HOUSE", 2.4)
flow.append(k.body(
    "No state license exists, but five downstate counties license "
    "home-improvement contractors, and a builder or trade you hire may need "
    "one. The county laws were read; here is what each says about a new "
    "house. <b>None of the five reaches the owner working on their own "
    "house</b> — Putnam says so expressly, and the others define the "
    "licensee as a person conducting a home-improvement <i>business</i>."))
rows = [
    [k.cellp("<b>Suffolk</b>"),
     k.cellp("“Home improvement contracting” “shall not include <b>the "
             "construction of a new home</b> or work done by a contractor in "
             "compliance with a guaranty of completion on new residential "
             "property.” Electrical and plumbing are licensed separately "
             "under §&#160;563-126."),
     k.cellp("Suffolk County Code<br/>" + sec("563-16"))],
    [k.cellp("<b>Nassau</b>"),
     k.cellp("“‘Home Improvement’ shall not include (a) <b>the construction "
             "of a new home building</b> or work done by a contractor in "
             "compliance with a guarantee of completion of a new building "
             "project.”"),
     k.cellp("Nassau Admin. Code<br/>" + sec("21-11.1(3)"))],
    [k.cellp("<b>Putnam</b>"),
     k.cellp("The chapter does not apply to “the sale or construction of a "
             "new home <b>other than a custom home</b>,” nor to “<b>work "
             "performed upon a residence by the owner</b>,” nor to plumbing "
             "(Chapter 190) or electrical (Chapter 145), which the county "
             "licenses separately. So a builder erecting a custom home on "
             "your lot <b>does</b> need the Putnam license."),
     k.cellp("Putnam County Code<br/>" + sec("135-3(C)"))],
    [k.cellp("<b>Westchester</b>"),
     k.cellp("“Home improvement” means “repair, replacement, remodeling, "
             "installation, construction, alteration, conversion, "
             "modernization made to, in or upon a private residence,” and no "
             "person may engage in the business unless licensed. <b>There is "
             "no express new-home exclusion.</b> Confirm with the county's "
             "Consumer Protection department whether a contractor building a "
             "new house on an owner's lot must hold the license."),
     k.cellp("Laws of Westchester County<br/>" + sec("863.312") + ", .313")],
    [k.cellp("<b>Rockland</b>"),
     k.cellp("Rockland licenses home-improvement contractors under Chapter "
             "286 of the county code. <b>The chapter text could not be "
             "retrieved for this kit</b> and nothing is asserted about its "
             "new-home treatment. Obtain the current chapter from the county "
             "before hiring."),
     k.cellp("Rockland County Code<br/>Ch. 286 — not verified")],
]
flow.append(k.ref_table(
    "Five county laws, and what each says about a new house",
    [k.cellp("County", bold=True), k.cellp("What the law says", bold=True),
     k.cellp("Instrument", bold=True)],
    # 1.2in, not 1.0in: "Westchester" in bold measures ~62pt at 9.5pt and a
    # 1.0in column leaves 62pt inside its padding, so it split as "Westchest /
    # er" — which check.py caught as a line opening with a two-letter fragment.
    rows, [1.2 * inch, CW - 1.2 * inch - 1.85 * inch, 1.85 * inch]))
flow.append(k.cite(
    "Read from the counties' own hosted texts in September 2026: Suffolk's "
    "Consumer Affairs PDF of §&#160;563, Nassau's local-law text, Putnam's "
    "Chapter 135 PDF, and Westchester's license application, which "
    "reproduces §&#160;863.312. A contractor building your whole house is "
    "separately bound by General Business Law Article 36-A statewide — "
    "NY.2."))

# ------------------------------------------------------------- regardless
flow += k.h2_tight("THE OFFICES THAT EXIST WHATEVER YOUR RUNG", 2.4)
flow.append(k.body(
    "The real risk is not missing an office — it is doing them in the wrong "
    "order, because three of them constrain what goes on the application "
    "and two constrain where the house can physically sit."))
rows = [
    [k.cellp("<b>1</b>", center=True), k.cellp("<b>Your rung</b>"),
     k.cellp("The clerk, in the statutory order above. Before anything else.")],
    [k.cellp("<b>2</b>", center=True), k.cellp("<b>Tax map number</b>"),
     k.cellp("From the assessor. The application must carry “the tax map "
             f"number and the street address” ({sec('1203.3(a)(2)(ii)')}), "
             "and so must the certificate of occupancy.")],
    [k.cellp("<b>3</b>", center=True), k.cellp("<b>Boundary survey</b>"),
     k.cellp("A licensed surveyor. The site plan must be “drawn in "
             "accordance with an accurate boundary survey” "
             f"({sec('1203.3(a)(3)(viii)')}). Order it early; the septic "
             "design and the zoning setbacks are drawn on it.")],
    [k.cellp("<b>4</b>", center=True), k.cellp("<b>County health department</b>"),
     k.cellp("Septic design approval and the well. <b>Constrains the house "
             "position</b> — do it before you fix the footprint.")],
    [k.cellp("<b>5</b>", center=True), k.cellp("<b>APA or NYC DEP</b>"),
     k.cellp("Only if the map puts you inside the Park or the watershed. "
             "Both change the septic setbacks.")],
    [k.cellp("<b>6</b>", center=True), k.cellp("<b>Zoning</b>"),
     k.cellp("Local, always — setbacks, height, lot coverage are matters "
             "“as to which the uniform fire prevention and building code "
             f"does not provide” (Exec. Law {sec('379(3)')}). Ask whether "
             "zoning approval must precede the building permit.")],
    [k.cellp("<b>7</b>", center=True), k.cellp("<b>Floodplain administrator</b>"),
     k.cellp("Pull the FIRM at <b>msc.fema.gov</b>. In New York, "
             "flood-resistant construction applies in <b>shaded X and B "
             "zones</b> as well as A and V ([NY] R306.1).")],
    [k.cellp("<b>8</b>", center=True), k.cellp("<b>Workers' Compensation Board</b>"),
     k.cellp("Form CE-200 as a homeowner at <b>businessexpress.ny.gov</b>, or "
             "carrier forms C-105.2 and DB-120.1. Job-specific. NY.1.")],
    [k.cellp("<b>9</b>", center=True), k.cellp("<b>Electrical inspection agency</b>"),
     k.cellp("From your office's approved list — nobody else's. Named on the "
             "statement of special inspections. Then the driveway permit "
             "from whichever road authority owns the road you touch, and "
             "811 before any excavation.")],
]
flow.append(k.ref_table(
    "The sequence, whatever your rung",
    [k.cellp("", bold=True, center=True), k.cellp("Step", bold=True),
     k.cellp("Which office, and why the order", bold=True)],
    rows, [0.35 * inch, 1.85 * inch, CW - 2.2 * inch]))

# --------------------------------------------------------------- addresses
flow += k.h2_tight("STATE-LEVEL ADDRESSES", 2.0)
flow.append(k.body(
    "All confirmed to resolve in September 2026. Two of them sit behind a "
    "browser check that refuses automated readers; a person with a browser "
    "gets through."))
rows = [
    [k.cellp("<b>Code editions and the all-electric status line</b>"),
     k.cellp("dos.ny.gov/notice-adoption")],
    [k.cellp("<b>DOS regional offices; the Division's home</b>"),
     k.cellp("dos.ny.gov/building-standards-and-codes")],
    [k.cellp("<b>Model local law most towns copied</b>"),
     k.cellp("dos.ny.gov/model-local-laws")],
    [k.cellp("<b>Appeals and variances (Part 1205)</b>"),
     k.cellp("dos.ny.gov/code/variances")],
    [k.cellp("<b>Complaint about a code official</b>"),
     k.cellp("dos.ny.gov/code/complaints")],
    [k.cellp("<b>Form CE-200</b>"),
     k.cellp("businessexpress.ny.gov — search “CE-200”; overview at "
             "wcb.ny.gov/content/ebiz/wc_db_exemptions/"
             "requestExemptionOverview.jsp")],
    [k.cellp("<b>The 2025 codes, free</b>"),
     k.cellp("codes.iccsafe.org/content/NYSRC2025P1 (residential); "
             "codes.iccsafe.org/content/NYSECC2025P1 (energy)")],
    [k.cellp("<b>County health departments</b>"),
     k.cellp("health.ny.gov/environmental/water/drinking/ctyadd1.htm; "
             "district offices at …/distphn.htm")],
    [k.cellp("<b>Appendix 75-A and 5-B</b>"),
     k.cellp("health.ny.gov/regulations/nycrr/title_10/part_75/"
             "appendix_75-a.htm; …/part_5/appendix_5b.htm")],
    [k.cellp("<b>DEC registered well drillers</b>"),
     k.cellp("appfactory.dec.ny.gov/WaterWell/Contractor_Search")],
    [k.cellp("<b>Adirondack Park Agency</b>"),
     k.cellp("apa.ny.gov/permitting/laws.html")],
    [k.cellp("<b>NYC watershed map and rules</b>"),
     k.cellp("nyc.gov/site/dep/environment/regulations.page")],
    [k.cellp("<b>The all-electric docket</b>"),
     k.cellp("courtlistener.com/docket/71197226/mulhern-gas-co-inc-v-mosley/")],
    [k.cellp("<b>Statutes</b>"),
     k.cellp("nysenate.gov/legislation/laws/EXC/A18 — Article 18; swap the "
             "code and section for any law cited here")],
]
# 1.55in label column. The label is sized by the LONGEST address in the right
# column, not by how the labels look: the widest single token here is the
# Appendix 75-A path at ~300pt at 9.5pt, and the WCB overview path at ~330pt.
# CW - 1.55in leaves 392pt, so neither wraps mid-token. Labels may wrap.
flow.append(k.ref_table(
    "Verified September 2026",
    [k.cellp("What you need", bold=True), k.cellp("Where", bold=True)],
    rows, [1.55 * inch, CW - 1.55 * inch]))
flow.append(k.cite(
    "<b>One warning when you look something up.</b> The official NYCRR on "
    "Westlaw (govt.westlaw.com/nycrr) was still showing the <b>2020</b> "
    "Residential Code for Part 1220 nine months after the 2025 rule took "
    "effect. For Parts 1219–1229 and 1240, read the Department of State's own "
    "rule-text PDFs, linked from the Notice of Adoption page."))

# ---------------------------------------------------------------- write-in
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT", 1.6)
flow += k.check_table(
    "Every office that touches this build, confirmed and dated",
    [
        ("Village / town / city, and whether it runs a Part 1203 program:",
         [("Municipality", 0.6), ("Runs program?", 0.4)]),
        ("My rung (1 local, 2 county, 3 DOS) and the office that issues the "
         "permit:", [("Rung", 0.25), ("Office", 0.75)]),
        ("Code enforcement officer by name, and the date I confirmed it:",
         [("Officer", 0.6), ("Date", 0.4)]),
        ("County health department or DOH district office for septic and "
         "well; tax map number from the assessor:",
         [("Office", 0.6), ("Tax map no.", 0.4)]),
        ("Inside the Adirondack Park? Inside the NYC watershed? (map "
         "checked, date):", [("Park", 0.3), ("Watershed", 0.3), ("Date", 0.4)]),
        ("Zoning office, and whether zoning approval precedes the building "
         "permit:", [("Office", 0.6), ("Precedes?", 0.4)]),
        ("Floodplain administrator; FIRM zone (including shaded X):",
         [("Office", 0.6), ("Zone", 0.4)]),
        ("County home-improvement license law, if any, and whether it "
         "reaches my builder:", [("Law", 0.5), ("Reaches builder?", 0.5)]),
        ("Electric utility, and what it needs before setting a meter "
         "(usually the agency's electrical certificate); road authority for "
         "the driveway:",
         [("Utility", 0.5), ("Road authority", 0.5)]),
        "I called 811 before any excavation.",
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ny-permit-kit",
                       "NY.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
