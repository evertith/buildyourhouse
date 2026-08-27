#!/usr/bin/env python3
"""CO.2 Permit Application Checklist — Colorado, two tracks plus the land.

Colorado's application problem is not "what goes in the packet" but "how many
packets, to how many offices, in what order." This document runs the land
approvals first — because in Colorado the well permit can decide whether the
house is buildable at all — then the local building permit, then the state
trade permits.

Sources verified August 2026 (see the on-page sources table):
  C.R.S. 37-92-602(1)(b)      exempt well: 15 gpm cap; household, fire, stock,
                              one acre of lawn/garden; not more than three
                              single-family dwellings
  C.R.S. 37-92-602(3)(b)(II)(A)  THE 35-ACRE LINE, verbatim — under 35 acres
                              the presumption runs only for a well used
                              "solely for ordinary household purposes inside a
                              single-family dwelling" and NOT for irrigation
  C.R.S. 37-92-602(1)(a)      designated groundwater basins are outside the
                              article entirely — their own rules apply
  C.R.S. 37-92-602(3)(a)(II)  statutory application fees
  C.R.S. 37-92-602(3)(b)(III) subdivision wells: cumulative effect counted
  dwr.colorado.gov            "review of complete applications may take up to
                              49 days"; applications by email, fees online
  C.R.S. 25-10-104(1),(2),(4) statewide OWTS minimums; EVERY local board of
                              health must adopt rules, no less stringent
  C.R.S. 25-10-106(1)(a)-(h)  what the local rules must cover: application,
                              site inspection, required studies, determination
                              by an environmental health specialist or PE,
                              permit issuance, and a FINAL INSPECTION before
                              the system is placed in use
  C.R.S. 25-10-109(1)         systems-contractor licensing is a LOCAL option —
                              so "can I install my own septic?" is a local
                              question the statute does not answer
  C.R.S. 25-10-110            local agencies hold primary enforcement
  C.R.S. 30-28-205(1),(3)     county permit after code adoption; seal unless
                              12-120-403 exempts
  C.R.S. 12-120-403(1)(a)     you may draw your own house plans
  C.R.S. 30-28-211(3),(3.5)   the energy-code trigger: adopting or UPDATING a
                              building code pulls in an energy code; the
                              July 1 2023 / July 1 2026 tiers; the rural-county
                              carve-out at (3.5)(c)
  C.R.S. 31-15-602(3),(3.5)   the municipal parallel — with NO rural carve-out
  C.R.S. 12-115-120(2)(b)     electrical permit and fee BEFORE work commences
  C.R.S. 12-155-120(1)(c)(I)  plumbing/gas permit and fee BEFORE work
  dpo.colorado.gov/ElectricalPlumbingPermits  what the state permit system
                              asks for; separate permit per detached structure;
                              the published local-jurisdiction lists

Still deliberately hedged: every local packet (each building department
publishes its own submittal list); whether your parcel can get a well permit
at all; whether your local board of health lets a homeowner install their own
OWTS; and all fees other than the two set in statute.
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

FORM_ID = "CO.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Application"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The land approvals that gate a Colorado build, the local building permit "
    "if one exists, and the state electrical and plumbing permits that exist "
    "either way — in the order you have to work them.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

flow += k.h2_tight("THE ORDER MATTERS MORE THAN THE PAPERWORK")
flow.append(k.body(
    "In most states you start at the building department. In Colorado you "
    "start at the water, because the answer can be \"this parcel cannot have "
    "a house on it.\" DWR's own page warns that \"<i>review of complete "
    "applications may take up to <b>49 days</b></i>\" — before a driller is "
    "scheduled. Septic runs on its own clock through local public health, "
    "needs a site evaluation before the permit, and cannot be used until a "
    "final inspection passes. Both commonly have to be resolved before a "
    "building department will issue anything, and neither depends on whether "
    "your county has a building code at all. So: <b>1. Water</b> — well "
    "permit or tap commitment. <b>2. Wastewater</b> — OWTS permit or sewer "
    "tap. <b>3. Access and address.</b> <b>4. The permits</b> — local "
    "building permit if one is required, and the state trade permits, which "
    "are required either way. Items 1 to 3 are the long poles; item 4 is "
    "where everyone starts."))
flow.append(Spacer(1, 4))

# ================================================================ WATER
flow += k.h2_tight("1. WATER — THE PERMIT THAT DECIDES WHETHER YOU CAN BUILD")
flow.append(k.body(
    "Colorado water law is prior-appropriation law: a well is a water right, "
    "not a utility connection. Small residential wells escape adjudication as "
    "\"exempt\" wells — inside limits narrower than most land buyers assume, "
    "and the limits turn on acreage."))

flow.append(k.callout(
    "The 35-acre line — the single most expensive thing to learn late", [
        Paragraph("Under C.R.S. 37-92-602(3)(b)(II)(A) the state engineer "
                  "presumes no injury to other water rights — which is what "
                  "lets the permit issue — where the well is <b>\"<i>the only "
                  "well on a residential site, which well will be used solely "
                  "for ordinary household purposes inside a single-family "
                  "dwelling and will not be used for irrigation</i>\"</b>, "
                  "<b>or</b> is \"<i>the only well on a tract of land of "
                  "<b>thirty-five acres or more</b></i>\" used for the fuller "
                  "list of purposes, <b>or</b> is the only well on a "
                  "qualifying cluster-development lot.", S["body"]),
        Paragraph("Read plainly: on a parcel <b>under 35 acres</b> a new "
                  "exempt well is typically <b>household use inside the house "
                  "only — no lawn, no garden irrigation, no livestock</b>. At "
                  "<b>35 acres or more</b> you can get the wider permit: "
                  "household use for up to three dwellings, fire protection, "
                  "watering poultry and livestock, and irrigation of up to "
                  "one acre of gardens and lawns — all capped at <b>fifteen "
                  "gallons per minute</b> (37-92-602(1)(b)). People buy "
                  "five-acre parcels planning an orchard and find out "
                  "afterwards. Read the permit's allowed-uses page before you "
                  "close on land.", S["body"]),
    ]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>Two further gates.</b> <i>Designated groundwater basins</i> are "
    "carved out of the exempt-well article altogether (37-92-602(1)(a)) and "
    "run under their own Ground Water Commission rules — much of eastern "
    "Colorado sits in one, and a new small-capacity permit there is a "
    "different application with different odds. And in a <i>subdivision</i> "
    "approved on or after June 1, 1972 whose water-supply plan the state "
    "engineer never recommended for approval, \"<i>the cumulative effect of "
    "all such wells in the subdivision shall be considered in determining "
    "material injury</i>\" (37-92-602(3)(b)(III)) — meaning your neighbors' "
    "wells count against yours. Neither of these is a reason to give up; both "
    "are reasons to ask DWR before you buy."))

flow += k.check_table("W1: Water supply", [
    ("Determined the water source: exempt well / augmented well / municipal "
     "or district tap / cistern with hauled water",
     [("Source:", 1.0)]),
    ("Parcel acreage confirmed against the 35-acre line, and the allowed "
     "uses you will actually get written down",
     [("Acres:", 0.5), ("Uses allowed:", 0.5)]),
    "Checked whether the parcel sits in a Designated Basin or the Denver "
    "Basin (different rules and forms), or in a subdivision whose "
    "water-supply plan was never recommended for approval "
    "(cumulative-effect review) — dwr.colorado.gov, Well Permitting",
    ("Well permit application filed with DWR — allow up to 49 days for "
     "review of a complete application",
     [("Filed:", 0.5), ("Permit #:", 0.5)]),
    ("If a tap instead: written will-serve and the tap fee in writing. If a "
     "well: licensed well construction contractor engaged, with construction "
     "and pump records to be filed with DWR", [("Driller / provider:", 1.0)]),
    "Electrical permit for the well pump wiring planned — the state "
    "publishes a \"Requirements for Well Wiring\" handout and a separate "
    "Well Water Installer permit type",
], notes_header="Notes / who confirmed")
flow.append(k.cite(
    "C.R.S. 37-92-602(1)(a), (1)(b), (3)(a)(II), (3)(b)(II)(A), "
    "(3)(b)(III); dwr.colorado.gov Well Permitting (49-day review; "
    "applications by email with fees paid online; Beginner's Guide to Well "
    "Permits). The statutory application fees are one hundred dollars under "
    "subsection (3)(b) and sixty dollars under (3)(c) "
    "(37-92-602(3)(a)(II)) — confirm against DWR's current fee schedule "
    "before you send payment. Read August 2026."))

# ================================================================ WASTEWATER
flow += k.h2_tight("2. WASTEWATER — A LOCAL PERMIT UNDER A STATE FLOOR")
flow.append(k.body(
    "On-site wastewater treatment systems follow the same floor-and-ceiling "
    "shape as the trade codes. The Water Quality Control Commission sets "
    "statewide minimum standards, and then \"<i>Every local board of health "
    "in the state <b>shall</b> develop and adopt detailed rules for on-site "
    "wastewater treatment systems within its area of jurisdiction</i>\" "
    "(25-10-104(2)) — rules that must comply with the state minimums and, "
    "where adopted later, be \"<i>no less stringent</i>\" (25-10-104(4)). "
    "Enforcement sits locally: \"<i>The primary responsibility for the "
    "enforcement of this article … lies with local public health agencies and "
    "local boards of health</i>\" (25-10-110). So your septic office is the "
    "county or district public health agency, not the building department and "
    "not the state."))
flow.append(k.body(
    "Statute tells you what the local process must contain — useful, because "
    "it is the same everywhere even when the forms differ. Local rules must "
    "provide for a written application; \"<i>review of the application and "
    "inspection of the proposed site</i>\"; the studies and reports the "
    "agency may require, which is where soil profile and percolation work "
    "lives; a determination by \"<i>an environmental health specialist or a "
    "professional engineer</i>\"; issuance by the health officer; and a "
    "\"<i>final inspection … <b>but before the system is placed in "
    "use</b></i>\" (25-10-106(1)(a)–(h))."))
flow.append(k.callout("\"Can I install my own septic?\" — a local question",
                      [
    Paragraph("The state statute does not answer it. Licensing of systems "
              "contractors is permissive and local: \"<i>The local board of "
              "health <b>may</b> adopt rules that provide for the licensing "
              "of systems contractors</i>\" (25-10-109(1)). Some Colorado "
              "public health agencies license installers and allow a "
              "homeowner to install on their own property; others require a "
              "licensed installer for any system. Ask your local public "
              "health agency, in writing, before you price the job either "
              "way.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow += k.check_table("W2: Wastewater", [
    ("Local public health agency identified — the septic permit office for "
     "your county or health district", [("Agency:", 1.0)]),
    ("Site evaluation and soil work completed by whoever the agency accepts "
     "(environmental health specialist or professional engineer)",
     [("By:", 0.6), ("Date:", 0.4)]),
    ("OWTS permit issued BEFORE construction of the system",
     [("Permit #:", 0.5), ("Date:", 0.5)]),
    "Asked whether the agency allows a homeowner to install their own system "
    "(25-10-109(1) leaves it to the local board of health), and scheduled the "
    "final inspection — the system may not be used until it passes "
    "(25-10-106(1)(h))",
    "If sewer instead: written will-serve from the sanitation district and "
    "the tap fee quoted in writing",
], notes_header="Notes")

# ================================================================ ACCESS
flow += k.h2_tight("3. ACCESS AND ADDRESS — SMALL PERMITS THAT BLOCK BIG ONES")
flow.append(k.body(
    "Two approvals that are trivial to obtain and expensive to discover late, "
    "because other applications ask for their output. An <b>assigned "
    "address</b> is what the state permit system, the utility, and the "
    "emergency-services database key on — you cannot buy a state electrical "
    "permit without a job-site address and directions to it. A <b>driveway or "
    "access permit</b> comes from whoever owns the road: the county road "
    "department for a county road, the municipality for a city street, and "
    "the Colorado Department of Transportation where a driveway meets a state "
    "highway. Ask early which one owns your frontage; on a rural parcel the "
    "answer is not always obvious from the map."))
flow += k.check_table("W3: Access, address, and the rest of the land", [
    ("Address assigned by the county or municipal addressing authority",
     [("Address:", 1.0)]),
    ("Driveway / access permit obtained from the road authority — county, "
     "municipality, or CDOT for a state highway",
     [("Authority:", 0.55), ("Permit #:", 0.45)]),
    "Zoning, setbacks, and any overlay confirmed in writing — wildland-urban "
    "interface, ridgeline, historic, or scenic — plus the floodplain status "
    "of every part of the site, and the local floodplain development permit "
    "if any of it is in a mapped hazard area",
    "Easements, covenants, and any HOA architectural review identified — "
    "private restrictions bind you even where no public code does — and fire "
    "district requirements asked about directly: access width and turnaround, "
    "water supply or storage, and any sprinkler requirement",
], notes_header="Notes")

# ================================================================ TRACK A
flow += k.h2_tight("4A. THE LOCAL BUILDING PERMIT — IF YOUR JURISDICTION "
                   "REQUIRES ONE")
flow.append(k.body(
    "There is no statewide submittal list, because there is no statewide "
    "code. Your building department publishes its own, and that list governs. "
    "What follows is the shape common to Colorado departments, with the two "
    "items Colorado adds to the usual set: <b>a soils report and an "
    "engineered foundation</b>, which the expansive clays of the Front Range "
    "and the snow loads of the high country make near-universal, and "
    "<b>energy-code compliance</b> under whichever edition the trigger below "
    "landed your jurisdiction on."))
flow.append(k.callout("Good news you can use: draw your own plans", [
    Paragraph("The architects' practice act does not reach houses — \"<i>One-, "
              "two-, three-, and four-family dwellings, including accessory "
              "buildings commonly associated with those dwellings</i>\" are "
              "outside it (C.R.S. 12-120-403(1)(a)) — and the county statute "
              "requiring a professional seal defers to that exemption "
              "(30-28-205(3)). You may prepare and submit your own drawings. "
              "What your department can still require is <b>engineering</b> "
              "on the structure: a soils report, a foundation designed by a "
              "Colorado professional engineer, and stamped structural "
              "calculations for the snow load. Ask exactly which sheets need "
              "a seal before you draw, not after.", S["body"]),
]))
flow.append(Spacer(1, 6))

flow.append(Paragraph("The energy code your jurisdiction landed on",
                      S["h3"]))
flow.append(k.body(
    "Widely misreported, so here is the actual trigger. A county or "
    "municipality that has building codes, or adopts them after July 1, 2022, "
    "must also adopt and enforce an energy code (30-28-211(3); 31-15-602(3)). "
    "Then: one that <b>updates any building code</b> on or after July 1, 2023 "
    "and before July 1, 2026 must adopt an energy code at least equivalent to "
    "the <b>2021 IECC plus the model electric ready and solar ready code</b>; "
    "one that updates <b>on or after July 1, 2026</b> must reach the <b>model "
    "low energy and carbon code</b> developed by the Energy Code Board "
    "(30-28-211(3.5)(a), (b); 31-15-602(3.5)). Two things guides miss: the "
    "duty is triggered by <b>updating a code, not by a calendar deadline</b> "
    "— a jurisdiction that never updates never moves — and it reaches only "
    "jurisdictions that have building codes at all. A <b>rural county</b> "
    "(population under 30,000) that applied for and was not awarded an "
    "energy-code grant may instead adopt one of the three most recent IECC "
    "editions (30-28-211(3.5)(c)); municipalities get no such relief. And "
    "adopting the wildfire resiliency code alone does not trigger the duty "
    "(30-28-211(3.5)(g))."))
flow.append(Spacer(1, 4))

flow += k.check_table("A1: Before you file", [
    ("Confirmed the jurisdiction requires a building permit at all, and got "
     "the adopted code editions and the local amendment list",
     [("Editions:", 1.0)]),
    ("Submittal checklist obtained from the department — their list governs, "
     "not this one — and the energy-code path settled",
     [("Energy code:", 0.5), ("Path:", 0.5)]),
    "Owner-builder question answered in writing: may you pull the permit, "
    "is an affidavit required, and must you register as a contractor",
    "Water and wastewater approvals in hand — most departments will not "
    "issue without them",
], notes_header="Notes / who confirmed")

flow += k.check_table("A2: The application package", [
    "Site plan: property lines, setbacks, building footprint, driveway, "
    "easements, well and septic locations with their separation distances, "
    "and drainage",
    "Floor plans, elevations, wall sections, and window and door schedule — "
    "yours to draw (12-120-403(1)(a))",
    "Energy compliance documentation for the adopted energy code",
    "Colorado Wildfire Resiliency Code compliance if the parcel is in a "
    "designated wildland-urban interface area — structure hardening (Class 1 "
    "or Class 2) and the site and defensible-space requirements",
    ("Soils / geotechnical report, and a foundation design by a Colorado "
     "professional engineer if required", [("Engineer:", 1.0)]),
    ("Structural design for the site's snow load — confirm the ground snow "
     "load figure your department uses, in writing",
     [("Ground snow load:", 1.0)]),
    "Application form completed, and copies of the well permit, OWTS permit, "
    "driveway permit, and address assignment attached",
    ("Filed, fee paid, and the plan-review clock noted",
     [("Filed:", 0.5), ("Permit #:", 0.5)]),
], notes_header="Notes")

# ================================================================ TRACK B
flow += k.h2_tight("4B. THE STATE TRADE PERMITS — THESE EXIST EITHER WAY")
flow.append(k.body(
    "Whether or not a building permit exists for your house, the electrical "
    "and plumbing installations need permits, and they must be bought "
    "<b>before the work starts</b>: \"<i>Prior to the commencement of any "
    "electrical installation … shall apply for a permit and pay the required "
    "permit fee</i>\" (12-115-120(2)(b)), and the same words for plumbing and "
    "gas piping at 12-155-120(1)(c)(I). If your jurisdiction runs its own "
    "program you buy them there. Otherwise you buy them from the state, "
    "online, and the Division publishes exactly what it will ask you for."))

info_rows = [
    [k.cellp("<b>Every permit</b>"),
     k.cellp("The job-site address; <b>directions to the job site including "
             "the nearest cross streets</b>; a valid credit card. Permits "
             "bought through the online system are \"<i>processed "
             "immediately upon payment</i>\"; a hard-copy application "
             "\"<i>may be delayed up to 7 business days</i>.\"")],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("Square footage of the living space to be wired; the <b>name of "
             "the power supplier</b>; and the cost of materials and labor "
             "for the work.")],
    [k.cellp("<b>Plumbing (residential)</b>"),
     k.cellp("A <b>fixture count</b> — traps, water hammer arrestors, "
             "backflow preventers, water heaters, fuel gas outlets, and fuel "
             "gas pressure regulators. Count these off your own plans before "
             "you sit down to apply.")],
    [k.cellp("<b>Gas piping</b>"),
     k.cellp("A <b>separate application</b> from the plumbing permit — the "
             "Division publishes a Gas Piping Permit Application of its own, "
             "and the Colorado Fuel Gas Code is a separate adopted code.")],
    [k.cellp("<b>Each detached structure</b>"),
     k.cellp("\"<i>A separate permit is required for each detached structure "
             "on the same property.</i>\" Garage, shop, barn, studio — each "
             "one is its own permit, clearly named or numbered. Budget for "
             "them.")],
]
flow.append(k.ref_table(
    "What the state permit system asks for (dpo.colorado.gov, August 2026)",
    [k.cellp("Permit", bold=True),
     k.cellp("What you need in front of you", bold=True)],
    info_rows, [1.5 * inch, CW - 1.5 * inch]))
flow.append(Spacer(1, 6))

flow.append(k.callout("If you hire it out, do NOT buy the permit", [
    Paragraph("The Division's own notice to homeowners is explicit: if you "
              "are hiring an electrical or plumbing contractor, \"<i>your "
              "contractor is responsible for obtaining the required "
              "permit(s)</i>\" and as the homeowner \"<i>you should not "
              "continue with the permit application process</i>.\" Buying the "
              "permit yourself and then having someone else do the work is "
              "not a shortcut — it is the arrangement the statute treats as a "
              "violation, and it can leave the work uninsured as well as "
              "unlawful. Buy the permit only for work you will actually "
              "perform yourself.", S["body"]),
]))
flow.append(Spacer(1, 6))

flow += k.check_table("B1: State (or local) trade permits", [
    ("Confirmed who issues for ELECTRICAL, and separately for PLUMBING and "
     "GAS PIPING — the Division publishes both lists (CO.4)",
     [("Electrical:", 0.5), ("Plumbing:", 0.5)]),
    ("Electrical permit purchased BEFORE any wiring begins "
     "(12-115-120(2)(b))", [("Permit #:", 0.5), ("Date:", 0.5)]),
    ("Plumbing permit purchased BEFORE any plumbing begins "
     "(12-155-120(1)(c)(I))", [("Permit #:", 0.5), ("Date:", 0.5)]),
    ("Gas piping permit purchased separately if there is fuel gas or propane "
     "on the job — and a separate permit for every detached structure, each "
     "named or numbered on its own application",
     [("Permit #:", 0.5), ("Date:", 0.5)]),
    ("Permit term: asked for longer than twelve months at application if the "
     "build will run long (12-115-120(6)(a); 12-155-120(3)(a)); and the two "
     "Homeowner's Guides downloaded from the Division",
     [("Term:", 1.0)]),
], notes_header="Notes")

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 10))
flow.append(k.sources_table([
    ("Exempt well: 15 gpm cap; household, fire, stock, one acre of "
     "lawn/garden; max three dwellings", "C.R.S. 37-92-602(1)(b)"),
    ("DWR review of a complete well permit application may take up to 49 "
     "days", "dwr.colorado.gov, Well Permitting"),
    ("The 35-acre line: under it, household use inside the dwelling only, "
     "no irrigation", "C.R.S. 37-92-602(3)(b)(II)(A)"),
    ("Designated basins sit outside the exempt-well article; subdivision "
     "wells are judged on cumulative effect",
     "C.R.S. 37-92-602(1)(a), (3)(b)(III)"),
    ("Statewide OWTS minimums; every local board of health must adopt rules "
     "no less stringent; local rules must cover application, site "
     "inspection, studies, specialist or PE determination, permit, and a "
     "final inspection before use; homeowner installation is a local "
     "question", "C.R.S. 25-10-104, 25-10-106(1)(a)–(h), 25-10-109(1)"),
    ("Energy code triggered by ADOPTING OR UPDATING a building code; the "
     "2023 and 2026 tiers; the municipal twin",
     "C.R.S. 30-28-211(3), (3.5); 31-15-602(3), (3.5)"),
    ("Rural-county carve-out (population under 30,000, grant not awarded); "
     "the wildfire resiliency code alone does not trigger the energy-code "
     "duty", "C.R.S. 30-28-211(3.5)(c), (g)"),
    ("Electrical, plumbing, and gas piping permits and fees before work "
     "commences", "C.R.S. 12-115-120(2)(b); 12-155-120(1)(c)(I)"),
    ("What the state permit system asks for; separate permit per detached "
     "structure; contractor buys the permit when you hire out",
     "DPO permits page,<br/>dpo.colorado.gov"),
    ("2025 Colorado Wildfire Resiliency Code applies in designated "
     "wildland-urban interface areas", "DFPC, dfpc.colorado.gov"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "co-permit-kit",
                       "CO.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
