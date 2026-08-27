#!/usr/bin/env python3
"""MI.5 Forms & Documents Index.

Sources verified August 2026:
  MCL 125.1510(1)   application, verified affidavit of the specifications,
                    plans to scale, site plan, owner in fee
  MCL 125.1510(2)   the written instrument that must be FILED before anyone is
                    recognized as your agent, attorney, architect, engineer or
                    builder — with their license number and expiry
  MCL 125.1510(4)   the section 23a warning above the signature
  MCL 125.1510(7),(8) ordinary repairs; agricultural buildings
  MCL 125.1513      certificate of use and occupancy; temporary certificate
  MCL 324.9112(5)   the SESC transfer notice a seller must give a buyer
  MCL 339.2012(1)(d) the 3,500 sq ft calculated-floor-area seal threshold
  R 408.30505       work exempt from permit — 200 sq ft accessory structures,
                    7 ft fences, 4 ft retaining walls, and the rest
  BCC form numbers, all Rev. 04/24: BCC-324 building, BCC-339 electrical,
                    BCC-9 mechanical, BCC-327 plumbing
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

FORM_ID = "MI.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document a Michigan owner-builder meets — what each one is, when "
    "it is needed, and which office it comes from.")

flow.append(k.disclaimer(
    "Form names and numbers below are the State's. If a county or local "
    "agency issues your permit, its forms will differ — the obligations "
    "behind them will not."))
flow.append(Spacer(1, 8))

DOCS = [
    ("Statewide Jurisdiction List",
     "Not a form — the <b>lookup</b> that tells you which agency issues each "
     "of your four permits, discipline by discipline, for your exact unit of "
     "government. <b>When:</b> before you fill in anything else, and again "
     "the week you file. Free.",
     "LARA Bureau of Construction Codes — michigan.gov/bcc"),
    ("Building permit application",
     "The main application. Carries the section 23a licensing warning above "
     "your signature, the five environmental control approvals, and the "
     "sealed-plans statement. <b>When:</b> after zoning, health department "
     "and soil erosion are lined up.",
     "Your enforcing agency. State form: <b>BCC-324</b> (Rev. 04/24)"),
    ("Electrical permit application",
     "Separate permit, separately priced per circuit, service size and "
     "fixture count. A homeowner may obtain it for a single-family home and "
     "accompanying outbuildings they own and will occupy — if they do the "
     "work themselves.",
     "Possibly a different agency. State form: <b>BCC-339</b>"),
    ("Mechanical permit application",
     "Separate permit. An owner of a single-family dwelling who occupies or "
     "will occupy it may perform the work without a license — but not "
     "without this.",
     "Possibly a different agency. State form: <b>BCC-9</b>"),
    ("Plumbing permit application",
     "Separate permit, covering the building sewer and private sewer as well "
     "as the house plumbing — which matters on a septic site.",
     "Possibly a different agency. State form: <b>BCC-327</b>"),
    ("Construction documents and site plan",
     "\"<i>Full and complete copies of the plans drawn to scale</i>,\" plus a "
     "site plan showing dimensions and the location of the proposed building "
     "<i>and every other structure on the premises</i>. Two sets is the "
     "State's requirement. <b>When:</b> with the application.",
     "You or your designer"),
    ("Verified affidavit of the specifications",
     "Michigan's statutory affidavit is <b>about your plans</b>, not about "
     "your occupancy: you swear the specifications and plans \"<i>are true "
     "and complete and contain a correct description of the building or "
     "structure, lot or parcel, and proposed work</i>.\" It is printed on "
     "the application itself.",
     "Part of the permit application"),
    ("Sealed plans — only over the threshold",
     "An architect's or engineer's seal is <b>not</b> required for a one- or "
     "two-family dwelling under <b>3,500 square feet of calculated floor "
     "area</b> — and \"calculated floor area\" counts habitable space only, "
     "excluding basements, garages, attics, bathrooms, closets, hallways and "
     "utility rooms. Do the arithmetic before you pay for a seal. See MI.2.",
     "A licensed architect or professional engineer, if you need one at all"),
    ("Local homeowner affidavit / homeowner permit form",
     "Many enforcing agencies add their own acknowledgement that you are "
     "acting as your own builder and accept the responsibility a licensed "
     "contractor would. <b>This is a local instrument, not a state one</b> — "
     "its terms vary, so read it before signing.",
     "Your enforcing agency, if it uses one"),
    ("Written instrument designating a builder or agent",
     "If anyone else will apply or act for you, they are <b>not recognized</b> "
     "until a construction contract, power of attorney or letter of "
     "authorization is filed with the enforcing agency — stating their "
     "license number and its expiry date.",
     "Filed with the enforcing agency"),
    ("Zoning approval",
     "Use, setbacks, height, lot coverage, accessory buildings. Never "
     "preempted by the construction code and never handled by the State. "
     "<b>When:</b> before you draw, not after.",
     "Township, city or village"),
    ("Fire district approval",
     "One of the five approval lines on the permit application. On a rural "
     "parcel expect access width, turnaround and water supply questions.",
     "Local fire authority"),
    ("Septic permit",
     "Michigan regulates on-site wastewater through <b>local health "
     "departments</b>, and the rules genuinely differ between them. Start "
     "the soil evaluation as early in the year as the ground allows — this "
     "is the longest pole on a rural build. <b>When:</b> first.",
     "County or multi-county <b>district</b> health department"),
    ("Well permit and water test",
     "Required before a private well is drilled, with water testing after "
     "completion. Confirm with your health department who draws the sample "
     "and who pays for it.",
     "County or district health department"),
    ("Soil erosion and sedimentation control permit (Part 91)",
     "Required for a regulated earth change. The <b>county</b> enforces "
     "throughout the county unless your municipality has adopted its own "
     "department-approved ordinance, which may be <b>stricter</b>. Ask for "
     "the trigger that applies to your parcel. <b>When:</b> before any earth "
     "is moved.",
     "County enforcing agency, or your municipality if it has assumed it"),
    ("SESC transfer notice",
     "If you <b>buy</b> a parcel already under a soil erosion permit, the "
     "permit, its conditions <i>and responsibility for existing violations</i> "
     "transfer to you — and the seller must give you signed written notice on "
     "a state-developed form, filed with the enforcing agency before the "
     "transfer. Ask for it.",
     "The seller, on a form from the enforcing agency"),
    ("Floodplain determination",
     "The fifth approval line. Required where the parcel sits in a mapped "
     "special flood hazard area; EGLE permits development in a regulated "
     "floodplain.",
     "Enforcing agency; EGLE for a floodplain permit"),
    ("Driveway / road tie-in permit",
     "Michigan county road commissions are separate bodies from county "
     "government and issue their own driveway permits. If you connect to a "
     "state trunkline — an I-, US- or M- numbered route — it is MDOT "
     "instead.",
     "County road commission, or MDOT on a trunkline"),
    ("Certificate of use and occupancy",
     "Michigan's statutory name for what everyone calls the CO. The building "
     "\"<i>shall not be used or occupied in whole or in part</i>\" until it "
     "issues, and the agency must issue it within <b>5 business days</b> of a "
     "written application once you are entitled to it. It records the code "
     "edition your permit was issued under — keep it.",
     "Enforcing agency, at the end. $50 on the state schedule"),
    ("Temporary certificate of use and occupancy",
     "May be issued on request for part of the building before all the work "
     "is complete, if that part can be occupied safely.",
     "Enforcing agency, on written request"),
]

rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in DOCS]
flow.append(k.ref_table(
    "Documents a Michigan owner-builder will encounter",
    [k.cellp("Document", bold=True),
     k.cellp("What it is and when you need it", bold=True),
     k.cellp("Where it comes from", bold=True)],
    rows, [1.45 * inch, CW - 1.45 * inch - 1.7 * inch, 1.7 * inch]))

flow.append(Spacer(1, 8))
flow += k.h2_tight("WHAT NEEDS NO PERMIT AT ALL")
flow.append(k.body(
    "Michigan's code rule lists the work that is exempt from a permit. The "
    "exemption is from the <b>permit</b> only — \"<i>exemption from the "
    "permit requirements of the code shall not be deemed to grant "
    "authorization for any work to be done in any manner in violation of the "
    "provisions of the code or any other laws or ordinances</i>.\" The ones "
    "that matter on a house build:"))
flow.append(k.bullet(
    "<b>One-story detached accessory structures</b> up to <b>200 square "
    "feet</b> of floor area."))
flow.append(k.bullet(
    "<b>Fences</b> not more than <b>7 feet</b> high, and <b>retaining "
    "walls</b> not more than <b>4 feet</b> from the bottom of the footing to "
    "the top of the wall, unless supporting a surcharge."))
flow.append(k.bullet(
    "<b>Sidewalks and driveways</b> not more than 30 inches above adjacent "
    "grade, not over a basement or story below, and not part of an "
    "accessible route."))
flow.append(k.bullet(
    "<b>Detached decks, porches and patios</b> up to 200 square feet, no "
    "more than 30 inches above grade, not attached to and not within 36 "
    "inches of the dwelling, and not serving any ingress or egress door."))
flow.append(k.bullet(
    "Painting, papering, tiling, carpeting, cabinets, counter tops and "
    "similar finish work; playground equipment; and a prefabricated "
    "above-ground pool under 24 inches deep and 5,000 gallons."))
flow.append(Spacer(1, 4))
flow.append(k.body(
    "Two statutory exemptions sit outside the code rule as well. <b>No "
    "building permit is required for ordinary repairs</b>, and none is "
    "required for \"<i>a building incidental to the use for agricultural "
    "purposes of the land on which the building is located if the building "
    "is not used in the business of retail trade</i>.\" That agricultural "
    "exemption is real and frequently misused — it turns on the <b>use of "
    "the land</b>, not on what the building looks like, and it does not "
    "exempt you from zoning. Ask before you rely on it."))
flow.append(k.cite(
    "R 408.30505, amending IRC § R105.2 (Part 5, Michigan Residential Code); "
    "MCL 125.1510(7), (8). Zoning is separate from the construction code and "
    "is not waived by any of these exemptions."))

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026; statutes at legislature.mi.gov, "
    "rules at ars.apps.lara.state.mi.us, forms at michigan.gov/bcc). "
    "Application contents, the verified affidavit of the specifications, and "
    "the site plan — MCL 125.1510(1). The written instrument required before "
    "an agent or builder is recognized, with license number and expiry — "
    "MCL 125.1510(2). The section 23a warning above the signature — MCL "
    "125.1510(4). Ordinary repairs and agricultural buildings — MCL "
    "125.1510(7), (8). Certificate of use and occupancy, the 5-business-day "
    "issue clock, and the temporary certificate — MCL 125.1513. Soil erosion "
    "permit transfer and the notice to the buyer — MCL 324.9112(3)–(5); "
    "county and municipal enforcement — MCL 324.9105(1), 324.9106. The 3,500 "
    "square foot calculated-floor-area seal threshold and its definition — "
    "MCL 339.2012(1)(d), (2). Work exempt from permit — R 408.30505. State "
    "form numbers and fees — BCC-324, BCC-339, BCC-9 and BCC-327, all Rev. "
    "04/24, and the BCC Fee Schedule effective April 1, 2024."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "mi-permit-kit",
                       "MI.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
