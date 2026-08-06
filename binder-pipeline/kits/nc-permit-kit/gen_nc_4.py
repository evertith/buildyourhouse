#!/usr/bin/env python3
"""NC.4 Where to File Directory.

North Carolina has a statewide building code but no statewide permit counter:
G.S. 160D-1110 and G.S. 87-14 both address the permit application to "any
incorporated city, town, or county." This document gives the structure and the
finding instructions; the owner-builder fills in the local specifics.

Deliberately prints agency WEBSITES and lookup routes rather than phone
numbers — direct-dial numbers at county offices change often enough that a
printed number is a liability, and every block has a rule to write the number
you confirmed.
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

FORM_ID = "NC.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The offices a North Carolina owner-builder deals with, how to find each "
    "one for your parcel, and a page to write down what you confirmed.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- who issues
flow += k.h2_tight("WHO ISSUES YOUR PERMIT DEPENDS ON WHERE YOUR LOT IS")
flow.append(k.body(
    "The building code is statewide; permits are not issued by the State. "
    "Both G.S. 87-14 and G.S. 160D-1110 send the application to \"<i>the "
    "building inspector or other authority of any incorporated city, town, "
    "or county</i>.\" Inside a municipality's limits the city or town usually "
    "issues; in the unincorporated county, the county does — but some towns "
    "contract inspections back to the county."))

flow.append(k.callout("Settle this first — it decides everything else", [
    Paragraph("Before you gather a single document, confirm <b>which "
              "jurisdiction issues your permit</b> and whether your parcel is "
              "inside city limits or in the unincorporated county. Call the "
              "county inspections department with your parcel identification "
              "number (PIN) and ask them directly. Filing with the wrong "
              "office costs you weeks.", S["body"]),
]))
flow.append(Spacer(1, 8))

# ---------------------------------------------------------------- how to find
flow += k.h2_tight("HOW TO FIND EACH OFFICE")
find_rows = [
    [k.cellp("<b>Building inspections</b><br/>(permits, plan review, "
             "inspection scheduling)"),
     k.cellp("Search \"<i>[your county] NC building inspections</i>\" or "
             "\"<i>[your town] NC permits</i>.\" Most NC jurisdictions run an "
             "online permit portal; ask which one and register before you "
             "file.")],
    [k.cellp("<b>Planning / zoning</b><br/>(setbacks, use, zoning "
             "verification)"),
     k.cellp("Often a separate department from inspections, sometimes the "
             "same counter. Ask inspections who confirms zoning and setbacks "
             "for your parcel — you will need that before plan review.")],
    [k.cellp("<b>County health department</b><br/>(septic, private wells)"),
     k.cellp("Search \"<i>[your county] NC environmental health</i>.\" On-"
             "site wastewater and private drinking water wells are handled "
             "by the local health department, not the building inspector.")],
    [k.cellp("<b>NCDOT District Engineer</b><br/>(driveway connection to a "
             "state-maintained road)"),
     k.cellp("NCDOT runs <b>14 highway divisions</b> with a county lookup at "
             "<b>ncdot.gov → Divisions → Highways</b>; your driveway is "
             "handled by the District Engineer within that division. A "
             "permit is normally <i>not</i> required for a single residence "
             "— call anyway, they arrange the driveway pipe. First confirm "
             "your road is state-maintained at all.")],
    [k.cellp("<b>Erosion &amp; sedimentation control</b>"),
     k.cellp("If you will disturb more than one acre, this is either NC DEQ's "
             "land resources program or a delegated local program. Ask your "
             "inspections department which applies in your county — they "
             "cannot issue your building permit without an approved plan.")],
]
flow.append(k.ref_table(
    "Finding the right office for your parcel",
    [k.cellp("Office", bold=True), k.cellp("How to find it", bold=True)],
    find_rows, [2.05 * inch, CW - 2.05 * inch]))

flow.append(k.cite(
    "Permit-issuing authority: N.C.G.S. § 160D-1110(a) and § 87-14(a). "
    "Erosion control plan required before a building permit may issue for "
    "land-disturbing activity: § 160D-1110(e). Verified August 2026."))

# ---------------------------------------------------------------- directory
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT")
flow.append(k.body(
    "Confirm each entry by phone rather than copying it from a search "
    "result, and write the date you confirmed it. Note the name of the "
    "person you spoke to — in a county office, having a name is worth more "
    "than having a number."))


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
    ("BUILDING INSPECTIONS", "issues the permit; schedules inspections"),
    ("PLANNING / ZONING", "setbacks, zoning verification, address assignment"),
    ("COUNTY HEALTH — ENVIRONMENTAL HEALTH", "septic and private well"),
    ("NCDOT DISTRICT OFFICE", "driveway access to a state-maintained road"),
    ("EROSION &amp; SEDIMENTATION CONTROL", "if disturbing over one acre"),
    ("ELECTRIC UTILITY", "temporary construction power and permanent service"),
    ("WATER &amp; SEWER", "public connection, tap fees — or N/A if well/septic"),
    ("LIEN AGENT", "required at $40,000 or more — see NC.5"),
]:
    flow += office_block(label, sub)

# ---------------------------------------------------------------- state level
flow += k.h2_tight("STATE-LEVEL CONTACTS")
flow.append(k.body(
    "These are stable and worth knowing. Phone numbers are left for you to "
    "confirm — a wrong number printed in a kit is worse than no number."))

state_rows = [
    [k.cellp("<b>NC Licensing Board for General Contractors</b>"),
     k.cellp("Verify that any contractor you hire at $40,000 or more is "
             "licensed. This is also the body that receives your owner "
             "exemption affidavit and verifies your claim."),
     k.cellp("nclbgc.org")],
    [k.cellp("<b>NC Office of State Fire Marshal</b><br/>Code enforcement / "
             "engineering"),
     k.cellp("Publishes the North Carolina State Building Code and issues "
             "code interpretations. The place to settle a code dispute your "
             "inspector cannot."),
     k.cellp("ncosfm.gov")],
    [k.cellp("<b>NC General Assembly</b>"),
     k.cellp("The General Statutes themselves — Chapter 87 (contractor "
             "licensing), Chapter 160D (development regulation, permits, "
             "inspections), Chapter 44A (liens)."),
     k.cellp("ncleg.gov")],
    [k.cellp("<b>NC Department of Insurance</b>"),
     k.cellp("Maintains the list of registered lien agents you must choose "
             "from (G.S. 44A-11.1(b), § 58-26-45)."),
     k.cellp("ncdoi.gov")],
]
flow.append(k.ref_table(
    "State agencies and what each is actually for",
    [k.cellp("Agency", bold=True), k.cellp("Why you would contact them", bold=True),
     k.cellp("Website", bold=True)],
    state_rows, [1.95 * inch, CW - 1.95 * inch - 1.15 * inch, 1.15 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026, all at ncleg.gov): permits issued "
    "by city, town, or county — § 160D-1110(a), § 87-14(a). Erosion control "
    "plan required before the building permit — § 160D-1110(e). Lien agent "
    "registry — § 44A-11.1(b), § 58-26-45. Affidavit forwarded to the "
    "Licensing Board — § 87-14(a)(1)."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "nc-permit-kit",
                       "NC.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
