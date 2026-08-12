#!/usr/bin/env python3
"""VA.4 Where to File Directory.

Virginia has one statewide building code and no statewide permit counter:
§ 36-98 makes the USBC supersede all local building codes, and § 36-105
makes every locality's own building department responsible for enforcing
it. This document gives the structure and the finding instructions; the
owner-builder fills in the local specifics.

Deliberately prints agency WEBSITES and lookup routes rather than phone
numbers — direct-dial numbers at local offices change often enough that a
printed number is a liability, and every block has a rule to write the
number you confirmed.

Sources verified August 2026:
  § 36-98        the USBC supersedes local building codes
  § 36-105       local enforcement is mandatory; localities without a
                 department must contract the function
  Agency pages   DHCD, DPOR, VDH, DEQ, VDOT — roles and URLs confirmed on
                 each official site
  Locality sites the ten-locality table's department names and domains
                 confirmed on each official site, August 2026

Still deliberately hedged: the ten-locality table is presented as "ten of
Virginia's busiest permit counters," not a ranking (Census Building Permits
Survey confirms Loudoun and Chesterfield at the top tier; the rest are
large issuers by population and reputation); and Stafford County's
parent-department naming, which is inconsistent on its own site — the
table prints the function and the domain.
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

FORM_ID = "VA.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The offices a Virginia owner-builder deals with, how to find each one "
    "for your parcel, and a page to write down what you confirmed.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- who issues
flow += k.h2_tight("ONE CODE, LOCAL COUNTERS")
flow.append(k.body(
    "The code is statewide and exclusive: the USBC \"<i>shall supersede "
    "the building codes and regulations of the counties, municipalities "
    "and other political subdivisions and state agencies</i>\" (§ 36-98). "
    "But the State issues no permits — \"<i>enforcement of the provisions "
    "of the Building Code for construction and rehabilitation shall be "
    "the responsibility of the local building department</i>\" (§ 36-105), "
    "and a locality without one must contract the function to another "
    "jurisdiction or agency. So your permit counter is your county's, "
    "city's, or town's building department — same code everywhere, "
    "different forms, fees, and portals at every counter."))

flow.append(k.callout("Settle this first — it decides everything else", [
    Paragraph("Before you gather a single document, confirm <b>which "
              "locality issues your permit</b> — county, city, or town. "
              "Not every locality runs its own building department: "
              "§ 36-105 lets one contract the function to another "
              "jurisdiction, so a town lot may actually file with the "
              "county. Call the building department you believe covers "
              "your parcel, give them the parcel ID, and ask directly. "
              "Filing with the wrong office costs you weeks.", S["body"]),
]))
flow.append(Spacer(1, 8))

# ---------------------------------------------------------------- how to find
flow += k.h2_tight("HOW TO FIND EACH OFFICE")
find_rows = [
    [k.cellp("<b>Building department</b><br/>(permits, plan review, "
             "inspection scheduling)"),
     k.cellp("Search \"<i>[your locality] Virginia building permit</i>\" "
             "and stay on the .gov result. Many localities run an online "
             "permit portal; ask which one and register before you "
             "file.")],
    [k.cellp("<b>Planning / zoning</b><br/>(setbacks, use, floodplain)"),
     k.cellp("Often a separate department from the building office, "
             "sometimes the same counter. Ask the building department who "
             "confirms zoning and setbacks for your parcel — and who the "
             "<b>floodplain administrator</b> is, if your parcel touches "
             "a mapped floodplain.")],
    [k.cellp("<b>Local health department</b><br/>(septic, private wells)"),
     k.cellp("Search \"<i>[your locality] health department environmental "
             "health</i>.\" Onsite sewage and private wells are VDH "
             "programs filed at the <b>local</b> health department — not "
             "the building office (see VA.2, section C).")],
    [k.cellp("<b>VDOT district land use permits</b><br/>(driveway entrance "
             "on a state-maintained road)"),
     k.cellp("Unless you are in a city, a town that maintains its "
             "streets, or Henrico or Arlington, assume your road is "
             "VDOT's. Start at vdot.virginia.gov → Land Use Permits, "
             "which routes you to the district office for your locality; "
             "online filing is available.")],
    [k.cellp("<b>Erosion &amp; stormwater (VESMP)</b>"),
     k.cellp("The local VESMP authority issues your land-disturbance "
             "approval and holds the agreement-in-lieu-of-a-plan form. "
             "Ask the building department which office runs "
             "erosion/stormwater for your locality — no land-disturbing "
             "activity may begin before its approval.")],
]
flow.append(k.ref_table(
    "Finding the right office for your parcel",
    [k.cellp("Office", bold=True), k.cellp("How to find it", bold=True)],
    find_rows, [2.05 * inch, CW - 2.05 * inch]))

flow.append(k.cite(
    "One statewide code, locally enforced: § 36-98; § 36-105. Septic and "
    "wells via local health departments: 12VAC5-610-250; 12VAC5-630-230. "
    "Land-disturbance approval before any disturbance: § 62.1-44.15:34(A). "
    "VDOT entrance permits issued by district staff: 24VAC30-73-20(C). "
    "Verified August 2026."))

# ---------------------------------------------------------------- directory
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT")
flow.append(k.body(
    "Confirm each entry by phone rather than copying it from a search "
    "result, and write the date you confirmed it. Note the name of the "
    "person you spoke to — in a local office, having a name is worth "
    "more than having a number."))


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
    ("BUILDING DEPARTMENT", "issues the permit; schedules inspections"),
    ("PLANNING / ZONING", "setbacks, zoning verification, floodplain"),
    ("LOCAL HEALTH DEPARTMENT", "septic and private well (VDH programs)"),
    ("VDOT DISTRICT — LAND USE PERMITS", "driveway entrance on a "
     "state-maintained road"),
    ("EROSION &amp; STORMWATER (VESMP)", "land-disturbance approval; "
     "agreement in lieu of a plan"),
    ("ELECTRIC UTILITY", "temporary construction power and permanent "
     "service"),
    ("WATER &amp; SEWER", "public connection, tap fees — or N/A if "
     "well/septic"),
    ("MECHANICS' LIEN AGENT", "your option, and a smart one — see VA.2 "
     "and VA.5"),
]:
    flow += office_block(label, sub)

# ---------------------------------------------------------------- state level
flow += k.h2_tight("STATE-LEVEL CONTACTS")
flow.append(k.body(
    "These are stable and worth knowing. Phone numbers are left for you "
    "to confirm — a wrong number printed in a kit is worse than no "
    "number."))

state_rows = [
    [k.cellp("<b>DHCD — State Building Codes Office</b>"),
     k.cellp("Writes the USBC and issues code interpretations — the place "
             "to settle a code question your building official cannot "
             "(sbco@dhcd.virginia.gov)."),
     k.cellp("dhcd.virginia.gov<br/>→ codes")],
    [k.cellp("<b>DPOR — Board for Contractors</b>"),
     k.cellp("Contractor and tradesman licensing. Verify every "
             "subcontractor's license here before you sign — License "
             "Lookup is on the front page."),
     k.cellp("dpor.virginia.gov")],
    [k.cellp("<b>VDH — Onsite Sewage &amp; Water Services</b>"),
     k.cellp("The septic and private-well program. Applications file at "
             "your local health department; the state page holds the "
             "forms and the program rules."),
     k.cellp("vdh.virginia.gov")],
    [k.cellp("<b>DEQ</b>"),
     k.cellp("Oversees the local erosion/stormwater (VESMP) programs and "
             "runs the construction general permit for larger "
             "disturbances."),
     k.cellp("deq.virginia.gov")],
    [k.cellp("<b>VDOT — Land Use Permits</b>"),
     k.cellp("Entrance permits on state-maintained roads, issued by "
             "district staff. The land-use-permits page routes you to "
             "your district and the LUP forms."),
     k.cellp("vdot.virginia.gov")],
]
flow.append(k.ref_table(
    "State agencies and what each is actually for",
    [k.cellp("Agency", bold=True),
     k.cellp("Why you would contact them", bold=True),
     k.cellp("Website", bold=True)],
    state_rows, [1.95 * inch, CW - 1.95 * inch - 1.45 * inch, 1.45 * inch]))

# ---------------------------------------------------------------- localities
flow += k.h2_tight("TEN OF VIRGINIA'S BUSIEST PERMIT COUNTERS")
flow.append(k.body(
    "If your lot is in one of these, here is the department and the "
    "official domain — go to the domain and search the department name "
    "rather than trusting an ad-cluttered search result. This is a list "
    "of large issuers, not a ranking. If your locality is not here, the "
    "search patterns above find it in two minutes."))

loc_rows = [
    [k.cellp("Loudoun County"),
     k.cellp("Department of Building and Development"),
     k.cellp("loudoun.gov")],
    [k.cellp("Chesterfield County"),
     k.cellp("Department of Building Inspection"),
     k.cellp("chesterfield.gov")],
    [k.cellp("Prince William County"),
     k.cellp("Development Services — Building Development Division"),
     k.cellp("pwcva.gov")],
    [k.cellp("Fairfax County"),
     k.cellp("Land Development Services (LDS)"),
     k.cellp("fairfaxcounty.gov<br/>/landdevelopment")],
    [k.cellp("Henrico County"),
     k.cellp("Department of Building Construction and Inspections"),
     k.cellp("henrico.gov")],
    [k.cellp("City of Virginia Beach"),
     k.cellp("Planning &amp; Community Development — Permits &amp; "
             "Inspections"),
     k.cellp("planning.virginiabeach.gov")],
    [k.cellp("City of Chesapeake"),
     k.cellp("Department of Development &amp; Permits"),
     k.cellp("cityofchesapeake.net")],
    [k.cellp("City of Suffolk"),
     k.cellp("Planning &amp; Community Development"),
     k.cellp("suffolkva.us")],
    [k.cellp("Spotsylvania County"),
     k.cellp("Building Department (Community Development)"),
     k.cellp("spotsylvania.va.us")],
    [k.cellp("Stafford County"),
     k.cellp("Building Permits &amp; Inspections"),
     k.cellp("staffordcountyva.gov")],
]
flow.append(k.ref_table(
    "Department names and domains confirmed on each official site, "
    "August 2026",
    [k.cellp("Jurisdiction", bold=True),
     k.cellp("Building department", bold=True),
     k.cellp("Official domain", bold=True)],
    loc_rows, [1.7 * inch, CW - 1.7 * inch - 2.1 * inch, 2.1 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026): the USBC supersedes local "
    "codes — § 36-98; local enforcement is mandatory, and localities "
    "without a department contract it — § 36-105; both at "
    "law.lis.virginia.gov. Agency roles and URLs confirmed on each "
    "agency's own site. Locality department names and domains confirmed "
    "on each official site; Census Building Permits Survey data put "
    "Loudoun and Chesterfield at the top tier of 2024 issuers — the "
    "table is otherwise unranked. Note for driveway purposes: Henrico "
    "and Arlington counties maintain their own road systems, so an "
    "entrance there is a county matter, not VDOT's."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "va-permit-kit",
                       "VA.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
