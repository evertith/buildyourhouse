#!/usr/bin/env python3
"""TX.4 Where to File Directory — Texas.

Texas has no statewide permit counter: the building-permit statutes are all
municipal (Local Gov't Code Ch. 214) and the county statutes deny permit
power over houses (Ch. 233). So the directory question is not "where is the
office" but "which of three legal positions is my lot in" — city limits,
ETJ, or unincorporated — and then which city, county, and state offices own
each piece.

Sources verified August 2026:
  Loc. Gov't Code §§ 42.101–.105  ETJ; SB 2038 release petitions; HB 2512
                              (2025) narrowed applicability
  Agency domains from each agency's own navigation: tdlr.texas.gov,
  tsbpe.texas.gov, tceq.texas.gov, tdi.texas.gov/wind,
  comptroller.texas.gov/programs/seco, esl.tamu.edu, txdot.gov
  Jurisdiction domains from each jurisdiction's own pages:
  houstonpermittingcenter.org, sa.gov, fortworthtexas.gov,
  austintexas.gov, dallascityhall.com, mctx.org, comalcounty.gov,
  hayscountytx.gov, epcounty.com
  Parker County (parkercountytx.com) and Hood County (co.hood.tx.us)
  domains are printed with a hedge: their individual offices were not
  verified — confirm the issuing office.

Deliberately prints agency WEBSITES and lookup routes rather than phone
numbers — direct-dial numbers change often enough that a printed number is
a liability, and every block has a rule to write the number you confirmed.

Still deliberately hedged: how each city publishes its limits/ETJ maps
(you confirm with the city and county in writing), the Parker and Hood
County offices, and every county-variable office in the fill-in section.
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

FORM_ID = "TX.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "How to pin down which track your lot is on, the state agencies and "
    "big-jurisdiction offices a Texas owner-builder deals with, and a page "
    "to write down what you confirmed.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- track
flow += k.h2_tight("SETTLE YOUR TRACK FIRST — CITY LIMITS, ETJ, OR "
                   "UNINCORPORATED")
flow.append(k.body(
    "Every requirement in this kit branches on where the lot sits, and "
    "there are three positions, not two. <b>Inside city limits</b>: the "
    "city permits and inspects — Track A. <b>Unincorporated county</b>: "
    "no building permit, five separate approvals — Track B. <b>The "
    "extraterritorial jurisdiction (ETJ)</b> is the ring outside the "
    "limits where the city is not your permit office but can still reach "
    "you — most commonly through platting. If you are in an ETJ, work "
    "Track B and ask the city in writing which of its regulations it "
    "applies there."))
flow.append(k.callout("Get it in writing, from both sides", [
    Paragraph("Ask the city's planning/permitting department AND the "
              "county: \"Is this parcel inside the city limits, inside "
              "the ETJ, or unincorporated — and who issues residential "
              "permits for it?\" Cities annex, ETJs move, and online maps "
              "lag. A written answer with a date is the first page of "
              "your project file. Filing with the wrong office — or "
              "assuming no office exists — costs weeks either way.",
              S["body"]),
]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>ETJ release:</b> since SB 2038 (2023), landowners in most ETJ "
    "areas may petition for release from the city's ETJ (Local Gov't Code "
    "§ 42.102) — and if the city sits on a valid petition, \"<i>the area "
    "is released by operation of law</i>\" (§ 42.105(d)). 2025's HB 2512 "
    "narrowed which areas qualify (§ 42.101), so check the exclusions "
    "before you plan around a release."))
flow.append(k.cite(
    "Loc. Gov't Code §§ 42.101, 42.102, 42.105(d), read August 2026."))

# ---------------------------------------------------------------- state agencies
flow += k.h2_tight("STATE AGENCIES — WHO OWNS WHICH PIECE")
state_rows = [
    [k.cellp("<b>TDLR</b><br/>Licensing &amp; Regulation"),
     k.cellp("Electricians (licensing and the homeowner-exemption page), "
             "HVAC contractors, water well drillers and pump installers. "
             "Also the agency whose program list proves no GC license "
             "exists."),
     k.cellp("tdlr.texas.gov")],
    [k.cellp("<b>TSBPE</b><br/>Plumbing Examiners"),
     k.cellp("Plumbing licensing statewide — still a standalone board "
             "through at least September 1, 2033 (Occ. Code § 1301.003). "
             "The place to confirm the homestead exemption for your "
             "situation, and the current plumbing-code edition."),
     k.cellp("tsbpe.texas.gov")],
    [k.cellp("<b>TCEQ</b><br/>Environmental Quality"),
     k.cellp("The OSSF (septic) program: rules, the authorized-agent "
             "county lookup map, Form 0235 where TCEQ itself permits, and "
             "licensing of installers and site evaluators. Also a route "
             "to groundwater-district maps (with the Texas Water "
             "Development Board's viewers)."),
     k.cellp("tceq.texas.gov")],
    [k.cellp("<b>TDI — Windstorm</b><br/>Dept. of Insurance"),
     k.cellp("Coastal catastrophe-area list, the WPI-1 filing, "
             "inspections, and the WPI-8 certificate search."),
     k.cellp("tdi.texas.gov/wind")],
    [k.cellp("<b>SECO</b><br/>State Energy Conservation Office"),
     k.cellp("The statewide energy-code status page (single-family) and "
             "the adoption process — check it before you rely on the 2015 "
             "edition staying current."),
     k.cellp("comptroller.texas.gov/<br/>programs/seco")],
    [k.cellp("<b>Energy Systems Laboratory</b><br/>Texas A&amp;M"),
     k.cellp("The \"laboratory\" in Health &amp; Safety Code § 388.004: "
             "publishes the builder self-certification form for "
             "unincorporated areas and the IC3 tools."),
     k.cellp("esl.tamu.edu")],
    [k.cellp("<b>TxDOT</b>"),
     k.cellp("District and area offices take Form 1058 driveway "
             "applications for access to state-system highways, FM roads "
             "included."),
     k.cellp("txdot.gov")],
]
flow.append(k.ref_table(
    "State agencies and what each is actually for",
    [k.cellp("Agency", bold=True),
     k.cellp("Why you would contact them", bold=True),
     k.cellp("Website", bold=True)],
    state_rows, [1.7 * inch, CW - 1.7 * inch - 1.5 * inch, 1.5 * inch]))
flow.append(k.cite(
    "Domains from each agency's own site navigation, read August 2026. "
    "This kit prints no phone numbers anywhere — numbers rot; write the "
    "one you confirmed in the directory below."))

# ---------------------------------------------------------------- jurisdictions
flow += k.h2_tight("HIGH-VOLUME JURISDICTIONS — OFFICIAL DOMAINS")
jur_rows = [
    [k.cellp("<b>Houston</b>"),
     k.cellp("Houston Permitting Center (Houston Public Works) — "
             "iPermits/ProjectDox"),
     k.cellp("houstonpermittingcenter.org")],
    [k.cellp("<b>San Antonio</b>"),
     k.cellp("Development Services Department — BuildSA portal; forms at "
             "docsonline.sanantonio.gov"),
     k.cellp("sa.gov")],
    [k.cellp("<b>Fort Worth</b>"),
     k.cellp("Development Services Department — Accela Citizen Access"),
     k.cellp("fortworthtexas.gov")],
    [k.cellp("<b>Austin</b>"),
     k.cellp("Development Services Department"),
     k.cellp("austintexas.gov")],
    [k.cellp("<b>Dallas</b>"),
     k.cellp("Development Services / Permitting &amp; Inspections — "
             "DallasNow online permitting (launched May 2025)"),
     k.cellp("dallascityhall.com")],
    [k.cellp("<b>Montgomery County</b>"),
     k.cellp("Environmental Health / Permitting — septic and development "
             "permits; no residential building permit (the county's own "
             "FAQ says so)"),
     k.cellp("mctx.org")],
    [k.cellp("<b>Comal County</b>"),
     k.cellp("County Engineer's Office — OSSF, floodplain, driveway, and "
             "911 address: the county's four standard permits, one "
             "office"),
     k.cellp("comalcounty.gov")],
    [k.cellp("<b>Hays County</b>"),
     k.cellp("Development Services — all development plus OSSF in "
             "unincorporated areas, via MyGovernmentOnline"),
     k.cellp("hayscountytx.gov")],
    [k.cellp("<b>El Paso County</b>"),
     k.cellp("Public Works — the verified worked example of a Subchapter "
             "F residential inspection program (since January 1, 2013)"),
     k.cellp("epcounty.com")],
    [k.cellp("<b>Parker County</b>"),
     k.cellp("Domain only — septic/floodplain/development offices exist "
             "but were not individually verified; confirm the issuing "
             "office"),
     k.cellp("parkercountytx.com")],
    [k.cellp("<b>Hood County</b>"),
     k.cellp("Domain only — same hedge as Parker: confirm the issuing "
             "office"),
     k.cellp("co.hood.tx.us")],
]
flow.append(k.ref_table(
    "Offices and official domains (verified August 2026 except as hedged)",
    [k.cellp("Jurisdiction", bold=True), k.cellp("Office", bold=True),
     k.cellp("Domain", bold=True)],
    jur_rows, [1.5 * inch, CW - 1.5 * inch - 1.8 * inch, 1.8 * inch]))

# ---------------------------------------------------------------- search patterns
flow += k.h2_tight("SEARCH PATTERNS FOR EVERYONE ELSE")
find_rows = [
    [k.cellp("<b>City permit office</b>"),
     k.cellp("Search \"<i>[your city] TX residential building permit</i>\" "
             "and land only on the .gov / official domain. Ask which "
             "portal they use and register before you file.")],
    [k.cellp("<b>OSSF authorized agent</b>"),
     k.cellp("TCEQ's authorized-agent lookup map (tceq.texas.gov, OSSF "
             "program pages) tells you whether your county, another local "
             "government, or TCEQ itself permits your septic system.")],
    [k.cellp("<b>County floodplain administrator</b>"),
     k.cellp("Search \"<i>[your county] TX floodplain administrator</i>\" "
             "— often inside the county engineer's or development "
             "services office. Every NFIP county has one.")],
    [k.cellp("<b>Groundwater conservation district</b>"),
     k.cellp("Most of Texas is districted. Use the district maps "
             "published by TCEQ and the Texas Water Development Board, "
             "then call the district BEFORE drilling — even an exempt "
             "domestic well commonly needs district registration and "
             "spacing clearance.")],
    [k.cellp("<b>TxDOT district / area office</b>"),
     k.cellp("txdot.gov → Districts; the local area office takes the Form "
             "1058 driveway application for state-system roads.")],
    [k.cellp("<b>Electric utility, new-construction desk</b>"),
     k.cellp("Whoever serves the lot — co-op or IOU — ask for the "
             "new-construction / builder services desk and their "
             "meter-loop inspection requirements before you wire "
             "(see TX.3).")],
]
flow.append(k.ref_table(
    "Finding the right office for your parcel",
    [k.cellp("Office", bold=True), k.cellp("How to find it", bold=True)],
    find_rows, [2.05 * inch, CW - 2.05 * inch]))

# ---------------------------------------------------------------- directory
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT")
flow.append(k.body(
    "Confirm each entry by phone rather than copying it from a search "
    "result, and write the date you confirmed it. Note the name of the "
    "person you spoke to — in a county office, having a name is worth "
    "more than having a number."))


def office_block(label, sub):
    """One office: department and phone, then portal plus who/when
    confirmed."""
    return [
        Paragraph(f"<b>{label}</b> — <font size=9.5>{sub}</font>", S["body"]),
        d.FillInRow([("Office / department:", 0.62), ("Phone:", 0.38)]),
        d.FillInRow([("Portal / address:", 0.44), ("Spoke with:", 0.34),
                     ("Confirmed:", 0.22)]),
        Spacer(1, 4),
    ]


for label, sub in [
    ("CITY PERMITS / PLANNING", "Track A permits; or the ETJ answer in "
     "writing"),
    ("COUNTY DEVELOPMENT / ENGINEER", "floodplain, driveway/culvert, "
     "development permits, Subchapter F question"),
    ("OSSF AUTHORIZED AGENT", "septic permit and inspections"),
    ("GROUNDWATER DISTRICT", "well registration/permit and spacing — "
     "before drilling"),
    ("TxDOT AREA OFFICE", "Form 1058 driveway permit, if on a state road"),
    ("TDI WINDSTORM / ENGINEER", "coastal only — WPI-1 and phase "
     "inspections"),
    ("ELECTRIC UTILITY", "temporary power; meter-loop release "
     "requirements"),
    ("PRIVATE CODE-CERTIFIED INSPECTOR", "your Track B quality gate and "
     "energy-code route"),
]:
    flow += office_block(label, sub)

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026): ETJ release — Loc. Gov't Code "
    "§§ 42.101, 42.102, 42.105(d). Agency and jurisdiction domains — each "
    "organization's own site, as tabled above; Parker and Hood County "
    "rows are domain-only and hedged. Statutes at "
    "statutes.capitol.texas.gov."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "tx-permit-kit",
                       "TX.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
