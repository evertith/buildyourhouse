#!/usr/bin/env python3
"""GA.4 Where to File Directory.

Georgia has statewide codes but no statewide permit counter: permits and
inspections are a power each city or county chooses to exercise (O.C.G.A.
§ 8-2-26(a)), and some exercise none of it. This document gives the
structure and the finding instructions; the owner-builder fills in the local
specifics.

Sources verified August 2026:
  O.C.G.A. § 8-2-26(a)   local-option enforcement; § 8-2-25(a) codes bind
                         statewide regardless
  State agency functions and domains — checked live August 2026:
    dca.georgia.gov (construction codes), sos.ga.gov (State Licensing Board
    for Residential and Commercial General Contractors; ch. 43-14 trade
    division boards), dph.georgia.gov/environmental-health/onsite-sewage,
    epd.georgia.gov (E&S, NPDES, floodplain, wells), gaswcc.georgia.gov,
    dot.ga.gov (District Area Offices), gefa.georgia.gov
  High-volume jurisdiction DOMAINS verified live August 2026; department
    names verified only where taken from the site's own URL structure —
    the rest are marked with an asterisk on the page.
  O.C.G.A. § 44-14-361.5(b)  the Notice of Commencement files with the clerk
                         of superior court

Deliberately prints agency WEBSITES and lookup routes rather than phone
numbers — direct-dial numbers change often enough that a printed number is a
liability; every block has a rule to write the number you confirmed.

Still deliberately hedged: several county department names (marked * — the
domain is the verified key); which counties enforce permits at all (no
official roster — first call decides); O.C.G.A. mirror currency (March 28,
2024).
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

FORM_ID = "GA.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The offices a Georgia owner-builder deals with, how to find each one "
    "for your parcel, and a page to write down what you confirmed.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- who issues
flow += k.h2_tight("WHO ISSUES YOUR PERMIT DEPENDS ON WHERE YOUR LOT IS")
flow.append(k.body(
    "The codes are statewide; the counter is not. Permitting is a power "
    "granted to \"<i>the governing body of any municipality or county "
    "adopting any state minimum standard code</i>\" (§ 8-2-26(a)). "
    "Inside city limits the city usually issues (some contract back to "
    "the county); in the unincorporated county, the county issues "
    "<b>where a building department exists at all</b> — and where none "
    "does, there is no permit to pull, though the codes still bind your "
    "work (§ 8-2-25(a); see GA.2 and GA.3)."))

flow.append(k.callout("Settle this first — it decides everything else", [
    Paragraph("Before you gather a single document, confirm three "
              "things: whether your parcel is <b>inside a "
              "municipality</b>, <b>which government</b> (if any) issues "
              "building permits for it, and <b>who runs the "
              "inspections</b>. Call the county with your parcel ID and "
              "ask directly — in Georgia this one call can change the "
              "entire path.", S["body"]),
]))
flow.append(Spacer(1, 8))

# ---------------------------------------------------------------- how to find
flow += k.h2_tight("HOW TO FIND EACH OFFICE")
find_rows = [
    [k.cellp("<b>Building / permitting department</b><br/>(permits, plan "
             "review, inspections)"),
     k.cellp("Search \"<i>[your county] GA building permit</i>\" and stay "
             "on the government's own domain. Metro departments run "
             "online portals — ask which one and register before you "
             "file.")],
    [k.cellp("<b>Planning / zoning</b><br/>(setbacks, use, zoning "
             "verification)"),
     k.cellp("Often a separate department, sometimes the same counter. "
             "Ask the permit office who confirms zoning and setbacks for "
             "your parcel.")],
    [k.cellp("<b>County health department — environmental health</b><br/>"
             "(septic, wells)"),
     k.cellp("Search \"<i>[your county] GA environmental health "
             "septic</i>.\" Every county has one — this track exists even "
             "where no building department does.")],
    [k.cellp("<b>GDOT District Area Office</b><br/>(driveway onto a state "
             "route)"),
     k.cellp("Residential driveway applications go to the Area Office "
             "for your county — via dot.ga.gov. First confirm the road "
             "is actually a state route.")],
    [k.cellp("<b>Erosion &amp; sedimentation / land disturbance</b>"),
     k.cellp("Your certified Local Issuing Authority — usually the county "
             "or city; the EPD district office where none exists. Ask the "
             "permit office which applies.")],
    [k.cellp("<b>Clerk of superior court</b><br/>(Notice of Commencement)"),
     k.cellp("Files in the project's county within 15 days of commencing "
             "work (§ 44-14-361.5(b)). Ask whether your clerk publishes "
             "a fill-in form — contents list in GA.2 and GA.5.")],
]
flow.append(k.ref_table(
    "Finding the right office for your parcel",
    [k.cellp("Office", bold=True), k.cellp("How to find it", bold=True)],
    find_rows, [2.05 * inch, CW - 2.05 * inch]))

flow.append(k.cite(
    "Local-option enforcement: O.C.G.A. § 8-2-26(a); codes statewide "
    "regardless: § 8-2-25(a); Notice of Commencement venue: "
    "§ 44-14-361.5(b). Verified August 2026."))

# ---------------------------------------------------------------- directory
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT")
flow.append(k.body(
    "Confirm each entry by phone rather than copying it from a search "
    "result, and write the date and the name of the person you spoke to "
    "— in a county office, a name is worth more than a number."))


def office_block(label, sub):
    """One office: department and phone, then portal plus who/when confirmed."""
    return [
        Paragraph(f"<b>{label}</b> — <font size=9.5>{sub}</font>", S["body"]),
        d.FillInRow([("Office / department:", 0.62), ("Phone:", 0.38)]),
        d.FillInRow([("Portal / address:", 0.44), ("Spoke with:", 0.34),
                     ("Confirmed:", 0.22)]),
        Spacer(1, 4),
    ]


for label, sub in [
    ("BUILDING / PERMITTING DEPARTMENT",
     "issues the permit; schedules inspections — or confirms none exists"),
    ("PLANNING / ZONING", "setbacks, zoning verification, address assignment"),
    ("COUNTY HEALTH — ENVIRONMENTAL HEALTH", "septic permit and final; wells"),
    ("GDOT DISTRICT AREA OFFICE", "driveway access onto a state route"),
    ("LOCAL ISSUING AUTHORITY — E&amp;S", "land disturbance, if not exempt"),
    ("CLERK OF SUPERIOR COURT", "Notice of Commencement filing"),
    ("UTILITIES — POWER / WATER / SEWER",
     "construction power, permanent service, taps — or N/A if well/septic"),
]:
    flow += office_block(label, sub)

# ---------------------------------------------------------------- state level
flow += k.h2_tight("STATE-LEVEL CONTACTS")
flow.append(k.body(
    "These are stable and worth knowing; phone numbers are left for you "
    "to confirm. (One more: the Georgia Environmental Finance Authority, "
    "gefa.georgia.gov, is the state energy office — programs, not code. "
    "Code questions go to DCA.)"))

state_rows = [
    [k.cellp("<b>Dept. of Community Affairs (DCA)</b><br/>Construction "
             "Codes &amp; Industrialized Buildings"),
     k.cellp("Publishes the state minimum codes and the Georgia "
             "Amendments. Code questions: codes@dca.ga.gov."),
     k.cellp("dca.georgia.gov")],
    [k.cellp("<b>State Licensing Board for Residential and Commercial "
             "General Contractors</b> (Secretary of State)"),
     k.cellp("Licensing and owner-exemption questions; verify every "
             "contractor you hire. Older handouts say \"Residential and "
             "General Contractors\" — SB 503 (2024) renamed it; same "
             "board."),
     k.cellp("sos.ga.gov")],
    [k.cellp("<b>Trade division boards</b> (Secretary of State, O.C.G.A. "
             "ch. 43-14)"),
     k.cellp("Electrical, plumbing, conditioned air, low-voltage, and "
             "utility licenses — verify every trade sub. The boards "
             "license people; they do not inspect houses."),
     k.cellp("sos.ga.gov")],
    [k.cellp("<b>Dept. of Public Health</b><br/>Environmental Health — "
             "On-Site Sewage"),
     k.cellp("The state septic rules your county health department "
             "administers, and links to each county office."),
     k.cellp("dph.georgia.gov")],
    [k.cellp("<b>Environmental Protection Division (EPD)</b><br/>"
             "Watershed Protection Branch"),
     k.cellp("E&amp;S oversight, NPDES construction stormwater "
             "(GAR100001 family, NOI forms), floodplain coordination, "
             "water well standards. E&amp;S plan standards live with the "
             "Soil &amp; Water Conservation Commission "
             "(gaswcc.georgia.gov)."),
     k.cellp("epd.georgia.gov")],
    [k.cellp("<b>Georgia DOT</b> — District Area Offices"),
     k.cellp("Driveway and encroachment permits on state routes, via "
             "the Area Office for your county."),
     k.cellp("dot.ga.gov")],
]
flow.append(k.ref_table(
    "State agencies and what each is actually for (domains checked live, "
    "August 2026)",
    [k.cellp("Agency", bold=True),
     k.cellp("Why you would contact them", bold=True),
     k.cellp("Website", bold=True)],
    state_rows, [1.95 * inch, CW - 1.95 * inch - 1.3 * inch, 1.3 * inch]))

# ---------------------------------------------------------------- high volume
flow += k.h2_tight("HIGH-VOLUME JURISDICTIONS")
flow.append(k.body(
    "Domains verified live in August 2026 — treat the domain as the "
    "reliable key and search it for \"building permit.\""))

hv_rows = [
    [k.cellp("Gwinnett County"),
     k.cellp("Dept. of Planning &amp; Development — Building Services"),
     k.cellp("gwinnettcounty.com")],
    [k.cellp("Fulton County (unincorp.)"),
     k.cellp("Public Works — Planning, Zoning &amp; Permitting"),
     k.cellp("fultoncountyga.gov")],
    [k.cellp("Cobb County"),
     k.cellp("Community Development Agency — Building &amp; Development"),
     k.cellp("cobbcounty.gov")],
    [k.cellp("Cherokee County"),
     k.cellp("Development Services Center"),
     k.cellp("cherokeega.com")],
    [k.cellp("Forsyth County"),
     k.cellp("Planning &amp; Community Development *"),
     k.cellp("forsythco.com")],
    [k.cellp("Paulding County"),
     k.cellp("Community Development *"),
     k.cellp("paulding.gov")],
    [k.cellp("Henry County"),
     k.cellp("Building &amp; Development Services *"),
     k.cellp("henrycountyga.gov")],
    [k.cellp("Hall County"),
     k.cellp("Building Inspections / Development Services *"),
     k.cellp("hallcounty.org")],
    [k.cellp("City of Atlanta"),
     k.cellp("Dept. of City Planning — Office of Buildings *"),
     k.cellp("atlantaga.gov")],
    [k.cellp("Chatham County (unincorp.)"),
     k.cellp("Building Safety &amp; Regulatory Services *"),
     k.cellp("chathamcountyga.gov")],
    [k.cellp("City of Savannah"),
     k.cellp("Development Services *"),
     k.cellp("savannahga.gov")],
]
flow.append(k.ref_table(
    "Metro Atlanta and Savannah permitting offices",
    [k.cellp("Jurisdiction", bold=True),
     k.cellp("Department (* = confirm name when you call)", bold=True),
     k.cellp("Domain", bold=True)],
    hv_rows, [1.6 * inch, CW - 1.6 * inch - 1.6 * inch, 1.6 * inch]))

flow.append(Spacer(1, 4))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026): local-option permitting — "
    "O.C.G.A. § 8-2-26(a); statewide codes — § 8-2-25(a); Notice of "
    "Commencement venue — § 44-14-361.5(b). All domains checked live "
    "against the agencies' own sites; names marked * are customary, "
    "not verified titles."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ga-permit-kit",
                       "GA.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
