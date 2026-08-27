#!/usr/bin/env python3
"""CA.4 Where to File Directory.

California has a statewide building code but no statewide permit counter.
B&P 7031.5 addresses the permit application to "each county or city"; H&S 19825
to "every city, county, or city and county"; Ed Code 17620(b) likewise. So the
issuing authority is the CITY if the parcel is inside city limits and the
COUNTY if it is unincorporated.

This document gives the structure and the finding instructions; the owner-
builder fills in the local specifics.

Deliberately prints agency WEBSITES and lookup routes rather than phone numbers
— direct-dial numbers at city and county offices change often enough that a
printed number is a liability, and every block has a rule to write down the
number you confirmed.

Every domain named here was resolved in August 2026. cslb.ca.gov,
fire.ca.gov, osfm.fire.ca.gov and bof.fire.ca.gov serve but refuse automated
requests, so this document prints the domain and the navigation path rather
than a deep link — deep links into those sites rot fastest anyway.
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

FORM_ID = "CA.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The offices a California owner-builder deals with, how to find each one "
    "for your parcel, and a page to write down what you confirmed.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- who issues
flow += k.h2_tight("WHO ISSUES YOUR PERMIT DEPENDS ON WHERE YOUR LOT IS")
flow.append(k.body(
    "The building code is statewide; permits are not issued by the State. "
    "Every statute that touches the permit addresses it to local government — "
    "B&amp;P § 7031.5 to \"<i>each county or city</i>,\" Health &amp; Safety "
    "Code § 19825 to \"<i>every city, county, or city and county</i>,\" "
    "Education Code § 17620(b) to \"<i>a city or county</i>.\" In practice: if "
    "your parcel sits <b>inside the limits of an incorporated city</b>, the "
    "city issues. If it is in the <b>unincorporated county</b>, the county "
    "does. Some small cities contract their building services back to the "
    "county, so the counter you stand at may not be the one you expect."))

flow.append(k.callout_long("Settle this first — it decides everything else", [
    Paragraph("Before you gather a single document, confirm <b>which "
              "jurisdiction issues your permit</b>. There is no single "
              "statewide parcel viewer, but there is a fast official check: "
              "the tax-rate lookup at <b>maps.cdtfa.ca.gov</b> takes a street "
              "address and tells you whether it sits in an incorporated city "
              "or in the unincorporated county. Confirm it against your county "
              "assessor's parcel viewer, which is definitive because the "
              "assessor assigns the APN — then call that building department "
              "and confirm it out loud. Filing with the wrong office costs you "
              "weeks, and in California weeks are expensive.", S["body"]),
    Paragraph("Ask the same call two more questions: <b>which Title 24 "
              "edition</b> they are currently enforcing, and whether they have "
              "<b>local amendments</b> on file. Both answers change what you "
              "draw.", S["body"]),
]))
flow.append(Spacer(1, 8))

# ---------------------------------------------------------------- how to find
flow += k.h2_tight("HOW TO FIND EACH OFFICE")
find_rows = [
    [k.cellp("<b>Building department</b><br/>(permits, plan review, "
             "inspection scheduling)"),
     k.cellp("Search \"<i>[your city] CA building department</i>\" or "
             "\"<i>[your county] CA building and safety</i>.\" Most California "
             "jurisdictions run an online permit portal; ask which one and "
             "register before you file.")],
    [k.cellp("<b>Planning / zoning</b><br/>(setbacks, use, zoning clearance)"),
     k.cellp("Usually a separate department from building, and usually the "
             "first stop — many jurisdictions require a planning clearance "
             "before building will accept your application at all.")],
    [k.cellp("<b>Environmental health</b><br/>(septic, private wells)"),
     k.cellp("Search \"<i>[your county] environmental health septic</i>.\" "
             "This is a <b>county</b> function even if your parcel is inside a "
             "city. Ask whether the county runs an approved LAMP under the "
             "State Water Board's OWTS Policy — the Board publishes a LAMP "
             "contact list at waterboards.ca.gov. Wells are permitted "
             "locally too: the Department of Water Resources sets the "
             "standards but issues nothing, and keeps a county-by-county list "
             "of permitting agencies at <b>water.ca.gov</b>.")],
    [k.cellp("<b>Fire authority</b><br/>(access, water supply, WUI, "
             "sprinklers)"),
     k.cellp("Could be a city fire department, a county fire department, an "
             "independent fire protection district, or CAL FIRE in the State "
             "Responsibility Area. Ask your building department which one "
             "reviews your project, and whether they or the fire authority "
             "inspect the sprinkler system. Check your parcel's zone and "
             "responsibility area on the official viewer linked from "
             "<b>osfm.fire.ca.gov</b>, not on a listing.")],
    [k.cellp("<b>School district</b><br/>(the fee certification that gates "
             "your permit)"),
     k.cellp("Find the district whose boundary contains the parcel — the "
             "county office of education can tell you, and it is not always "
             "the nearest school. Ask for the current per-square-foot rate and "
             "what they need to issue the certificate.")],
    [k.cellp("<b>Public works</b><br/>(driveway, encroachment, grading, "
             "address)"),
     k.cellp("Establish who <b>maintains the road</b> you will connect to: "
             "city, county, or the State. A connection onto a state highway is "
             "a Caltrans encroachment permit (dot.ca.gov). Your <b>Regional "
             "Water Quality Control Board</b> — one of nine, found from "
             "waterboards.ca.gov — decides whether your land disturbance needs "
             "the Construction General Permit, enrolled at "
             "smarts.waterboards.ca.gov.")],
]
flow.append(k.ref_table(
    "Finding the right office for your parcel",
    [k.cellp("Office", bold=True), k.cellp("How to find it", bold=True)],
    find_rows, [2.15 * inch, CW - 2.15 * inch]))

flow.append(k.cite(
    "<b>Sources</b> (verified August 2026; statutes at "
    "<b>leginfo.legislature.ca.gov</b>). Permit-issuing authority is local: "
    "B&amp;P § 7031.5; H&amp;S § 19825(a); Education Code § 17620(b); and "
    "H&amp;S § 17960 — \"<i>The building department of every city or county "
    "shall enforce within its jurisdiction all the provisions published in the "
    "State Building Standards Code</i>.\" School district certification gates "
    "the building permit, or the final inspection and certificate of occupancy "
    "where the district elected the Government Code § 66007(a) alternative — "
    "§ 17620(c). Local amendments are filed with the Building Standards "
    "Commission, fire district findings with HCD — CRC § 1.1.8.1. Every domain "
    "in this document resolved in August 2026; navigate from the domain, not "
    "a printed deep link."))

# ---------------------------------------------------------------- directory
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT")
flow.append(k.body(
    "Confirm each entry by telephone rather than copying it from a search "
    "result, and write down the date and the name of the person you spoke to "
    "— in a California permitting office a name is worth more than a "
    "number."))


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
    ("PLANNING / ZONING", "setbacks, zoning clearance, address assignment"),
    ("COUNTY ENVIRONMENTAL HEALTH", "septic and private well"),
    ("FIRE AUTHORITY", "access, water supply, WUI construction, sprinklers"),
    ("SCHOOL DISTRICT", "fee certification — gates your permit or your CO"),
    ("PUBLIC WORKS / ENCROACHMENT", "driveway, grading, road connection"),
    ("ELECTRIC UTILITY / WATER / SEWER", "temporary power, permanent service, "
     "connection and will-serve"),
    ("ENERGY CONSULTANT / ECC-RATER", "Title 24 compliance and verification"),
]:
    flow += office_block(label, sub)

# ---------------------------------------------------------------- state level
flow += k.h2_tight("STATE-LEVEL CONTACTS")
flow.append(k.body(
    "These are stable and worth knowing. Phone numbers are left for you to "
    "confirm — a wrong number printed in a kit is worse than no number."))

state_rows = [
    [k.cellp("<b>Contractors State License Board</b> (CSLB)"),
     k.cellp("Verify the license of every contractor you hire, in the right "
             "classification, before work starts and again before final "
             "payment. Also publishes owner-builder guidance and takes "
             "reports of unlicensed activity."),
     k.cellp("cslb.ca.gov")],
    [k.cellp("<b>California Building Standards Commission</b>"),
     k.cellp("Publishes Title 24 and its effective dates, and is where cities "
             "and counties must <b>file</b> their local amendments (CRC "
             "§ 1.1.8.1). It publishes a <b>searchable ordinance list per code "
             "cycle</b> — search your city or county by name to see what it "
             "amended."),
     k.cellp("dgs.ca.gov/BSC")],
    [k.cellp("<b>Dept of Housing and Community Development</b> (HCD)"),
     k.cellp("Adopts the residential building standards you are built to, and "
             "runs the factory-built and manufactured housing programs. Fire "
             "district amendment findings are filed here."),
     k.cellp("hcd.ca.gov")],
    [k.cellp("<b>California Energy Commission</b>"),
     k.cellp("The Energy Code, approved compliance software, and the CF1R / "
             "CF2R / CF3R compliance documents. Since January 2026 the "
             "verification program is the <b>Energy Code Compliance "
             "Program</b> — ask for an <b>ECC-Rater</b>, not a HERS rater."),
     k.cellp("energy.ca.gov")],
    [k.cellp("<b>State Water Resources Control Board</b>"),
     k.cellp("The OWTS Policy that governs septic, and the list of local "
             "agencies running approved LAMPs. Also the Construction General "
             "Permit for stormwater, enrolled through SMARTS."),
     k.cellp("waterboards.ca.gov<br/>smarts.waterboards.ca.gov")],
    [k.cellp("<b>CAL FIRE</b> and the <b>Office of the State Fire "
             "Marshal</b>"),
     k.cellp("Fire hazard severity zone maps — check your parcel here, not on "
             "a listing — defensible space guidance, and the listings of "
             "building products approved for wildland-urban interface use."),
     k.cellp("fire.ca.gov<br/>osfm.fire.ca.gov")],
    [k.cellp("<b>Board of Forestry and Fire Protection</b>"),
     k.cellp("Writes the defensible space regulations. It <b>adopted</b> the "
             "Zone 0 ember-resistant rules on 19 August 2026, effective on "
             "filing — expected around September 2026. Confirm current status "
             "here before you finalize a site plan."),
     k.cellp("bof.fire.ca.gov")],
    [k.cellp("<b>Coastal Commission</b> · <b>Caltrans</b> · "
             "<b>Dept of Water Resources</b>"),
     k.cellp("A Coastal Development Permit is a separate approval on its own "
             "timeline in the Coastal Zone. Caltrans issues the encroachment "
             "permit if your driveway meets a state highway. DWR sets well "
             "standards and lists the county agencies that permit wells."),
     k.cellp("coastal.ca.gov<br/>dot.ca.gov<br/>water.ca.gov")],
]
flow.append(k.ref_table(
    "State agencies and what each is actually for",
    [k.cellp("Agency", bold=True),
     k.cellp("Why you would contact them", bold=True),
     k.cellp("Website", bold=True)],
    state_rows, [1.78 * inch, CW - 1.78 * inch - 1.68 * inch, 1.68 * inch]))



if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ca-permit-kit",
                       "CA.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
