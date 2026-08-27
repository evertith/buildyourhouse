#!/usr/bin/env python3
"""CA.5 Forms & Documents Index.

Sources verified August 2026:
  H&S 19825(a)     the statutory permit application: Owner-Builder Declaration,
                   Workers' Compensation Declaration, construction lender block
  H&S 19825(b)     Authorization of Agent to Act on Property Owner's Behalf
  B&P 7031.5       the exemption statement; $500 civil penalty
  Lab 3800(a)      comp declaration under penalty of perjury
  Civ 8172         construction lending agency block on the application
  Ed Code 17620    school district fee certification gates permit or CO
  2025 CRC R309.2  automatic sprinklers in all one- and two-family dwellings
  2025 CRC R109    the inspection set; R109.1.5.2 -> CBC Ch. 17 special
                   inspections; R109.1.6.2 the CALGreen O&M manual at final
  2025 CRC R110    certificate of occupancy; R110.3 temporary CO
  PRC 4291(a)(5) / Gov 51182(a)(5)  the pre-construction certification and the
                   final inspection report your insurer may ask for
  Wat 13750.5      C-57 license to drill a well
  SWRCB            OWTS Policy and LAMPs; Construction General Permit / SMARTS

Form names and numbers are local; the obligations behind them are not. Where a
document's name varies by jurisdiction the row says what it does rather than
naming a form number this kit cannot verify for all 58 counties.
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

FORM_ID = "CA.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document a California owner-builder meets — what each one is, when "
    "it is needed, and which office it comes from.")

flow.append(k.disclaimer(
    "Form names and numbers are local; the obligations behind them are not."))
flow.append(Spacer(1, 8))

DOCS = [
    ("Building permit application",
     "The main application — and in California a <b>statutory form</b>: "
     "§ 19825 requires every city and county to use one \"in substantially the "
     "same form.\" Carries the declarations below. <b>When:</b> after zoning, "
     "school fees, septic and fire review are lined up.",
     "City building department if inside city limits; county if "
     "unincorporated"),
    ("Owner-Builder Declaration",
     "Part of that application, signed <b>under penalty of perjury</b>. You "
     "check the basis for your exemption and acknowledge the limits on "
     "selling. Bring identification — the agency must verify you are the owner "
     "on title. <b>When:</b> at application. See CA.1 before you sign it.",
     "On the permit application (H&amp;S § 19825; B&amp;P § 7031.5)"),
    ("Notice to Property Owner",
     "A <b>second</b> signed document, on your building department's own "
     "letterhead: the \"Owner's Acknowledgment and Verification of "
     "Information,\" twelve statements you read and <b>initial one at a "
     "time</b>, covering liability for unlicensed workers, when you become an "
     "employer, building to sell, and latent defects after you sell. "
     "<b>When:</b> ask for it before application day. No permit issues without "
     "it, and an agent may not sign it without prior approval.",
     "Your building department (H&amp;S § 19825(c))"),
    ("Workers' Compensation Declaration",
     "Also under penalty of perjury, on the same application: you self-insure, "
     "you carry a policy, or you certify you will not employ anyone so as to "
     "become subject to the comp laws. <b>Revisit it</b> the day you first pay "
     "a helper.",
     "On the permit application (Lab. § 3800(a))"),
    ("Authorization of Agent",
     "If anyone other than you signs the Owner-Builder Declaration, the owner "
     "must complete this and return it to the agency <b>before the permit "
     "issues</b>. California does allow an agent — but on a form, in advance.",
     "Owner completes; returned to the issuing agency (H&amp;S § 19825(b))"),
    ("Construction lending agency block",
     "The application must give space to name your construction lender, or to "
     "note that there is none.",
     "On the permit application (Civil Code § 8172)"),
    ("School district fee certificate",
     "Certification that the school facilities fee has been paid, or does not "
     "apply. <b>Your building permit cannot issue without it</b> — or, where "
     "the district elected otherwise, your final inspection and certificate of "
     "occupancy cannot. <b>When:</b> start early; the rate is per square foot "
     "and the district sets it.",
     "The school district whose boundary contains the parcel "
     "(Ed. Code § 17620)"),
    ("Title 24 energy compliance documents",
     "<b>CF1R</b> Certificate of Compliance with the application, <b>CF2R</b> "
     "Certificate of Installation from whoever installed each measure, and "
     "<b>CF3R</b> Certificate of Verification from the rater. On a "
     "wood-framed dwelling of two stories or fewer you may sign the CF1R "
     "yourself; the CF3R you may not.",
     "Your energy consultant; CF3R verification by an independent "
     "<b>ECC-Rater</b> (not a HERS rater — the program changed in 2026)"),
    ("Fire sprinkler plans",
     "Design for the automatic sprinkler system <b>every new California "
     "dwelling requires</b>, to NFPA 13D or CRC § R309.3. Affects your water "
     "service, pressure, and on a well your tank and pump. <b>When:</b> at "
     "design, not after plan check.",
     "A C-16 fire protection contractor; reviewed by the building department "
     "or the fire authority"),
    ("Septic permit",
     "Issued under the State Water Board's OWTS Policy, in most counties "
     "through an approved Local Agency Management Program. Preceded by a site "
     "and soil evaluation, which is what actually decides whether your land "
     "can carry a system and what it costs. <b>When:</b> first — before you "
     "design, ideally before you buy.",
     "County environmental health under its LAMP; the Regional Water Board "
     "where none applies"),
    ("Well permit and well completion report",
     "Permit before drilling; the completion report is filed by the driller "
     "afterwards. The driller must hold a <b>C-57 Water Well Contractor's "
     "License</b> — there is no owner exception for drilling, unlike the "
     "electrical and plumbing work you may self-perform.",
     "County environmental health; driller must be C-57 licensed "
     "(Water Code § 13750.5)"),
    ("Grading permit and geotechnical report",
     "Triggered by the volume or the slope of your earthwork, on thresholds "
     "your jurisdiction sets. A soils or geotechnical report is commonly "
     "required on sloped or filled sites and drives your foundation design.",
     "Building department or public works; report from a licensed engineer"),
    ("Construction General Permit enrollment",
     "If your land disturbance brings you under the statewide stormwater "
     "permit, you enroll through the State Water Board's SMARTS system and "
     "receive a WDID number — <b>before</b> ground disturbance. Confirm "
     "coverage with your Regional Water Board.",
     "State Water Resources Control Board, through its SMARTS system"),
    ("Encroachment / driveway permit",
     "Required to connect your driveway to a public road. Which agency issues "
     "it depends on who maintains the road — city, county, or Caltrans for a "
     "state highway.",
     "City or county public works; Caltrans if a state highway"),
    ("WUI pre-construction certification",
     "In a fire hazard zone, <b>before</b> construction the owner must obtain "
     "a certification from the building official that the dwelling as proposed "
     "complies with applicable building standards, and provide it on request "
     "to the course-of-construction insurer. Ask for it by name.",
     "Your building official (PRC § 4291(a)(5); Gov. § 51182(a)(5))"),
    ("Special inspection reports",
     "Where your approved plans carry a special inspection schedule — common "
     "on engineered work in California's seismic design categories — an "
     "approved special inspector reports directly to the building official. "
     "You pay for it.",
     "An approved agency; see California Building Code Chapter 17"),
    ("Operation and maintenance manual",
     "A CALGreen requirement that catches people at the very end: at the time "
     "of final inspection a manual \"shall be placed in the building.\" "
     "<b>When:</b> collect appliance and equipment documentation from your "
     "first delivery, not the week of your final.",
     "You assemble it (CRC § R109.1.6.2; CALGreen Ch. 4, Div. 4.4)"),
    ("Certificate of occupancy",
     "Issued after the final inspection when the building official finds no "
     "violations. The building may not be used or occupied until it issues. "
     "It records <b>the code edition your permit was issued under</b> and "
     "<b>whether a sprinkler system was required</b> — keep it.",
     "Building department, at the end (CRC § R110)"),
    ("Final inspection report for your insurer",
     "In a fire hazard zone, on completion the owner must obtain from the "
     "building official a copy of the final inspection report demonstrating "
     "compliance, and provide it on request to the property insurer. File it "
     "with your insurance papers. A <b>temporary</b> certificate of occupancy "
     "may also be issued before the whole work is complete, for a period the "
     "building official sets (CRC § R110.3).",
     "Your building official (PRC § 4291(a)(5); Gov. § 51182(a)(5))"),
]

rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in DOCS]
flow.append(k.ref_table(
    "Documents a California owner-builder will encounter",
    [k.cellp("Document", bold=True),
     k.cellp("What it is and when you need it", bold=True),
     k.cellp("Where it comes from", bold=True)],
    rows, [1.4 * inch, CW - 1.4 * inch - 1.75 * inch, 1.75 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026; statutes at "
    "leginfo.legislature.ca.gov). The permit application, Owner-Builder "
    "Declaration, Workers' Compensation Declaration and agent authorization "
    "are set out in the text of Health &amp; Safety Code § 19825(a) and (b); "
    "the underlying duty to state the basis of exemption, with a civil penalty "
    "of not more than $500, is B&amp;P § 7031.5; the comp declaration is "
    "required by Labor Code § 3800(a); the construction lender block by Civil "
    "Code § 8172. School district certification gates the permit under "
    "Education Code § 17620(b), or the final inspection and certificate of "
    "occupancy under § 17620(c). Automatic sprinklers in every one- and "
    "two-family dwelling: 2025 California Residential Code § R309.2 — "
    "renumbered from § R313.2 in the previous edition. Inspections, the "
    "operation and maintenance manual, and the certificate of occupancy: "
    "§ R109, § R109.1.6.2 and § R110. Special inspections: California Building "
    "Code Chapter 17. Wildfire certification and final report: Public "
    "Resources Code § 4291(a)(5) and Government Code § 51182(a)(5), both as "
    "amended by AB 1455 (Stats. 2025, Ch. 731). Well drilling license: Water "
    "Code § 13750.5. Septic and stormwater: State Water Resources Control "
    "Board OWTS Policy and Construction General Permit. <b>This kit prints no "
    "fee figures</b> — school fees, permit fees, septic and grading fees are "
    "all set locally or adjusted periodically, and a stale number is worse "
    "than none."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ca-permit-kit",
                       "CA.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
