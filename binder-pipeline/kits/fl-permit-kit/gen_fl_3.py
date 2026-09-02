#!/usr/bin/env python3
"""FL.3 Inspection Sequence.

Structured around the three GATES that stop a Florida job, rather than as a
flat list of inspections. Each gate is a document held by an office that is
not the building department, and each one has stopped somebody's build:

  1. The Notice of Commencement, recorded at the clerk of the circuit court.
     s. 713.135(1)(e)1., Fla. Stat. bars the building department (or a private
     provider) from performing or approving inspections until a copy is filed.
  2. The septic construction permit, which by s. 381.0065(4), Fla. Stat. must
     exist BEFORE the building permit issues — and whose final installation
     approval is a statutory precondition to occupancy.
  3. The blower door test and the termite certificate, which are performed by
     third parties and land at the certificate of occupancy.

The inspection list itself is FBC Building 110.3, which is a codified
statewide minimum rather than a local option — worth saying plainly, because
in most states in this series the inspection list IS local.
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

FORM_ID = "FL.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "On the Job"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "The document that has to be recorded before anyone will "
                 "inspect you, the inspections themselves, and a log.")
flow.append(k.disclaimer())

# --------------------------------------------------------------- the gate
flow += k.h2("THE DOCUMENT THAT GATES YOUR FIRST INSPECTION")
flow.append(k.body(
    "Florida's <b>Notice of Commencement</b> is the single most common way an "
    "owner-builder's job stops dead in its second month. It is not a building "
    "department form. You record it with the <b>clerk of the circuit court</b> "
    "in the county where the property sits, and then you give a copy to the "
    "building department."))
flow.append(k.body(
    "Get the sequence wrong and the consequence is immediate: "
    "“In the absence of the filing of a copy of the notice of "
    "commencement, the issuing authority or a private provider performing "
    "inspection services <b>may not perform or approve subsequent "
    "inspections</b> until the applicant files… such copy with the "
    "issuing authority” (s. 713.135(1)(e)1., Fla. Stat.)."))
rows = [
    [k.cellp("<b>Record it before you start work</b>"),
     k.cellp("The owner, “before actually commencing to improve any "
             "real property,… shall record a notice of commencement.” "
             "Recording is a precondition of starting, not of permitting."),
     k.cellp("713.13(1)(a)")],
    [k.cellp("<b>But not too early</b>"),
     k.cellp("“If the improvement described in the notice of "
             "commencement is not actually commenced within <b>90&nbsp;days</b> "
             "after the recording thereof, such notice is void and of no "
             "further effect.” Record it, then start."),
     k.cellp("713.13(2)")],
    [k.cellp("<b>Post a copy at the site</b>"),
     k.cellp("Post either a certified copy or a notarized statement that it "
             "has been filed for recording, along with a copy. This is a "
             "standing obligation, not a one-time act."),
     k.cellp("713.13(1)(a)")],
    [k.cellp("<b>File a copy with the building department</b>"),
     k.cellp("Required <b>before the first inspection</b> where the direct "
             "contract is <b>greater than $5,000</b> — which a house always "
             "is."),
     k.cellp("713.135(1)(e)")],
    [k.cellp("<b>You sign it, personally</b>"),
     k.cellp("“The owner must sign the notice of commencement and no "
             "one else may be permitted to sign in his or her stead.” It "
             "is sworn — the statutory form carries a notary block, and "
             "Florida allows online notarization."),
     k.cellp("713.13(1)(g), (1)(d)")],
    [k.cellp("<b>It expires in a year</b>"),
     k.cellp("Effective for <b>1&nbsp;year from recording</b> unless the notice "
             "states a longer period. If your build will run longer, say so "
             "in the notice or amend it before it lapses."),
     k.cellp("713.13(6), (5)(a)")],
]
flow.append(k.ref_table(
    "Notice of Commencement — the six things to get right",
    [k.cellp("", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.85 * inch, CW - 3.10 * inch, 1.25 * inch]))
flow.append(k.cite(
    "Sections 713.13 and 713.135, Fla. Stat. (2026). The recording threshold "
    "itself sits elsewhere: an improvement with a direct contract price of "
    "$2,500 or less is exempt (s. 713.02(5)), and s. 713.135(1) does not "
    "apply to a contract to repair or replace an existing heating or "
    "air-conditioning system under $15,000."))

flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "Why letting it lapse costs money, not just time", [
        Paragraph("The statutory form carries this warning in capitals, and "
                  "it is the whole point of the document: "
                  "“ANY PAYMENTS MADE BY THE OWNER AFTER THE EXPIRATION "
                  "OF THE NOTICE OF COMMENCEMENT ARE CONSIDERED IMPROPER "
                  "PAYMENTS UNDER CHAPTER 713… AND CAN RESULT IN YOUR "
                  "PAYING TWICE FOR IMPROVEMENTS TO YOUR PROPERTY.”",
                  S["body"]),
        Paragraph("Owner-builder jobs run long. A notice recorded at the "
                  "footing on a build that takes fifteen months expires with "
                  "the trim still going in — and every payment you make after "
                  "that date loses its protection. <b>Put the expiry date in "
                  "your calendar the day you record it</b>, and amend the "
                  "notice to extend the period before it runs out. An "
                  "amendment may extend the effective period, but changing "
                  "contractors requires a new notice.", S["body"]),
        Paragraph("One thing the building department may <b>not</b> do: "
                  "require the notice as a condition of issuing your permit. "
                  "The statute says so expressly (s. 713.135(1)(f), (1)(e)4.). "
                  "The permit can issue first; the notice gates the "
                  "inspections.", S["body"]),
    ]))

# ------------------------------------------------------------ the septic gate
flow += k.h2("THE GATE BEFORE THE PERMIT, AND THE GATE BEFORE YOU MOVE IN")
flow.append(k.body(
    "If your lot is on septic, one statute governs both ends of your "
    "project, and it is not in the building code. Section 381.0065(4), Fla. "
    "Stat. provides that a local government"))
flow.append(k.callout(
    "Section 381.0065(4), Fla. Stat.", [
        Paragraph("“…may not issue a building or plumbing permit for "
                  "any building that requires the use of an onsite sewage "
                  "treatment and disposal system <b>unless the owner or "
                  "builder has received a construction permit for such system "
                  "from the department</b>. A building or structure may not "
                  "be occupied and a municipality, political subdivision, or "
                  "any state or federal agency may not authorize occupancy "
                  "<b>until the department approves the final installation</b> "
                  "of the onsite sewage treatment and disposal system.”",
                  S["body"]),
    ]))
flow.append(Spacer(1, 2))
flow.append(k.body(
    "Read that twice if you are on septic. Your septic <b>construction "
    "permit</b> is a prerequisite to your <b>building permit</b> — so the "
    "septic application is the first thing you file, not something you get to "
    "later. And the septic <b>final installation approval</b> is a "
    "prerequisite to occupancy, independent of your certificate of occupancy. "
    "Two separate approvals from an agency that is not your building "
    "department. FL.4 explains which agency that is in your county, because "
    "in 2026 the answer is genuinely split."))

# -------------------------------------------------------------- inspections
flow += k.h2("THE REQUIRED INSPECTIONS")
flow.append(k.body(
    "Unlike most states in this series, Florida's inspection list is "
    "<b>codified statewide</b> in the building code rather than left to local "
    "option. FBC Building 110.3 sets the minimum for a one- or two-family "
    "dwelling. Your building department will add trade inspections and may "
    "add more; it may not require fewer."))
rows = [
    [k.cellp("<b>1</b>"), k.cellp("<b>Foundation</b>"),
     k.cellp("After trenches are excavated and forms erected. Covers "
             "stem-wall, monolithic slab-on-grade, piling and pile caps, "
             "footers and grade beams. <b>In a flood hazard area the "
             "elevation certification must be submitted upon placement of "
             "the lowest floor, before any further vertical "
             "construction.</b>")],
    [k.cellp("<b>2</b>"), k.cellp("<b>Underground trades</b>"),
     k.cellp("Plumbing and electrical below slab, before cover. Your "
             "building department schedules these against the trade permits "
             "rather than the 110.3 list.")],
    [k.cellp("<b>3</b>"), k.cellp("<b>Sheathing</b>"),
     k.cellp("Roof and wall sheathing, <b>sheathing fasteners</b>, and roof "
             "and wall dry-in. This is the nailing inspection — in a "
             "hurricane state it is the one inspectors fail people on, and "
             "it can be taken as part of dry-in or separately.")],
    [k.cellp("<b>4</b>"), k.cellp("<b>Framing</b>"),
     k.cellp("Window and door framing, vertical cells and columns, lintels "
             "and tie beams, trusses, bracing and connectors, draft stopping "
             "and fire blocking, energy insulation, and a rough-opening "
             "dimension tolerance check.")],
    [k.cellp("<b>5</b>"), k.cellp("<b>Rough trade inspections</b>"),
     k.cellp("Electrical, plumbing and mechanical rough-in before cover, "
             "under their own permits.")],
    [k.cellp("<b>6</b>"), k.cellp("<b>Roofing</b>"),
     k.cellp("Dry-in, insulation, roof coverings and flashing.")],
    [k.cellp("<b>7</b>"), k.cellp("<b>Exterior wall coverings</b>"),
     k.cellp("Wall coverings and veneers, and soffit coverings.")],
    [k.cellp("<b>8</b>"),
     k.cellp("<b>Impact-resistant coverings and systems</b>"),
     k.cellp("Where shutters or impact glazing are installed, the building "
             "official schedules inspections to confirm the system on the "
             "plans was actually installed, and installed per the "
             "manufacturer's instructions <b>and the product approval</b>. "
             "This is where your FL numbers get checked against reality.")],
    [k.cellp("<b>9</b>"), k.cellp("<b>Final</b>"),
     k.cellp("Building complete and ready for occupancy, plus final trade "
             "inspections. <b>In a flood hazard area a final certification of "
             "the lowest floor elevation must be submitted as part of the "
             "final inspection</b> — a second elevation document, not the "
             "same one you filed at the foundation.")],
]
flow.append(k.ref_table(
    "FBC Building 110.3 — statewide minimum inspections",
    [k.cellp("", bold=True), k.cellp("Inspection", bold=True),
     k.cellp("What it covers", bold=True)],
    rows, [0.42 * inch, 1.85 * inch, CW - 2.27 * inch]))
flow.append(k.cite(
    "FBC Building 110.3, 8th Edition (2023). Threshold-building special "
    "inspections do not reach a house: a “threshold building” is "
    "one greater than three stories or 50&nbsp;feet, or an assembly occupancy over "
    "5,000&nbsp;square feet with more than 500 occupants (s. 553.71(12), Fla. "
    "Stat.)."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "One approved inspection every 180&nbsp;days keeps the permit alive", [
        Paragraph("A permit becomes invalid if work is not commenced within "
                  "6&nbsp;months, or if work is suspended or abandoned for "
                  "6&nbsp;months. The definition that saves a slow owner-builder "
                  "build is this one: “Work shall be considered to be in "
                  "active progress when the permit has received an "
                  "<b>approved inspection within 180&nbsp;days</b>.” "
                  "(FBC Building 105.4.1, 105.4.1.3.) If you are going to be "
                  "away from the job for a season, schedule an inspection you "
                  "can pass before you go.", S["body"]),
    ]))

# ------------------------------------------------------------ before the CO
flow += k.h2("THE THREE THINGS THAT ARRIVE FROM SOMEBODY ELSE")
flow.append(k.body(
    "Three sign-offs at the end of a Florida build are produced by people who "
    "do not work for the building department, and each has its own lead time. "
    "Line them up early."))
flow.append(k.bullet(
    "<b>The termite Certificate of Compliance.</b> A licensed pest control "
    "company must issue a certificate to the building department stating "
    "that “The building has received a complete treatment for the "
    "prevention of subterranean termites.” If you use soil treatment, "
    "the initial application inside the foundation perimeter happens "
    "<i>after</i> excavation, backfill and compaction — and any soil "
    "disturbed after treatment has to be retreated. (FBC Residential "
    "R318.1.)"))
flow.append(k.bullet(
    "<b>The blower door test.</b> Mandatory before your certificate of "
    "occupancy, to a maximum of <b>7&nbsp;air changes per hour at 50&nbsp;pascals</b>, "
    "run after every penetration of the thermal envelope is sealed. You may "
    "not perform or self-certify it — it takes an energy auditor or rater, a "
    "Class A or B air-conditioning or mechanical contractor, or a third party "
    "approved by the code official. Below 3&nbsp;ACH50 the code then requires "
    "whole-house mechanical ventilation. (FBC Energy Conservation "
    "R402.4.1.2.)"))
flow.append(k.bullet(
    "<b>Septic final installation approval.</b> Occupancy may not be "
    "authorized until the department approves the final installation "
    "(s. 381.0065(4), Fla. Stat.). This is separate from your building "
    "final, and it comes from a different office."))

# ---------------------------------------------------------------- the log
flow += k.h2_tight("INSPECTION LOG", reserve=2.0)
flow += k.check_table(
    "Record every inspection as it happens",
    [("Notice of Commencement recorded", [("Book/Page:", 0.5),
                                          ("Expires:", 0.5)]),
     ("Copy of NOC filed with building department", [("Filed:", 1.0)]),
     ("Septic construction permit in hand (before building permit)",
      [("Permit no.:", 1.0)]),
     ("Foundation", [("Inspector:", 0.6), ("Result:", 0.4)]),
     ("Elevation certification at lowest floor (flood hazard area only)",
      [("Submitted:", 1.0)]),
     ("Underground plumbing / electrical", [("Inspector:", 0.6),
                                            ("Result:", 0.4)]),
     ("Sheathing and fasteners / dry-in", [("Inspector:", 0.6),
                                           ("Result:", 0.4)]),
     ("Framing", [("Inspector:", 0.6), ("Result:", 0.4)]),
     ("Electrical rough-in", [("Inspector:", 0.6), ("Result:", 0.4)]),
     ("Plumbing rough-in", [("Inspector:", 0.6), ("Result:", 0.4)]),
     ("Mechanical rough-in", [("Inspector:", 0.6), ("Result:", 0.4)]),
     ("Roofing", [("Inspector:", 0.6), ("Result:", 0.4)]),
     ("Exterior wall coverings", [("Inspector:", 0.6), ("Result:", 0.4)]),
     ("Impact-resistant coverings verified against product approval",
      [("Inspector:", 0.6), ("Result:", 0.4)]),
     ("Insulation", [("Inspector:", 0.6), ("Result:", 0.4)]),
     ("Termite Certificate of Compliance filed", [("Company:", 0.6),
                                                  ("Date:", 0.4)]),
     ("Blower door test passed", [("ACH50:", 0.4), ("Tested by:", 0.6)]),
     ("Septic final installation approval", [("Approved:", 1.0)]),
     ("Final building inspection", [("Inspector:", 0.6), ("Result:", 0.4)]),
     ("Final elevation certification (flood hazard area only)",
      [("Submitted:", 1.0)]),
     ("Certificate of occupancy issued", [("Date:", 1.0)]),
     ],
    notes_header="Notes")

# ----------------------------------------------------------------- sources
flow += k.h2_tight("SOURCES", reserve=2.0)
flow.append(k.sources_table([
    ("The owner must record a notice of commencement before commencing to "
     "improve the property, and post a certified copy or notarized statement "
     "at the site", "s. 713.13(1)(a)"),
    ("A notice is void if the improvement is not commenced within 90&nbsp;days of "
     "recording", "s. 713.13(2)"),
    ("The owner must sign the notice personally; the statutory form is sworn "
     "before a notary", "s. 713.13(1)(d), (1)(g)"),
    ("The notice is effective for 1&nbsp;year from recording unless it states "
     "otherwise, and may be amended to extend that period",
     "s. 713.13(6), (5)(a)"),
    ("Payments made after the notice expires are improper payments and can "
     "result in paying twice", "s. 713.13(1)(c) and the statutory form"),
    ("A copy must be filed with the issuing authority before the first "
     "inspection where the direct contract exceeds $5,000, and inspections "
     "may not be performed or approved until it is",
     "s. 713.135(1)(e), (1)(e)1."),
    ("Recording may not be required as a condition of applying for or "
     "issuing a building permit", "s. 713.135(1)(e)4., (1)(f)"),
    ("Improvements with a direct contract price of $2,500 or less are exempt; "
     "s. 713.135(1) does not reach an HVAC repair or replacement contract "
     "under $15,000", "ss. 713.02(5), 713.135(1)(f)"),
    ("No building or plumbing permit may issue without a septic construction "
     "permit, and occupancy may not be authorized until final installation is "
     "approved", "s. 381.0065(4)"),
    ("The statewide minimum inspection list, the flood elevation "
     "certifications at lowest floor and at final, and the impact-resistant "
     "covering inspection", "FBC Building 110.3"),
    ("A permit stays in active progress with an approved inspection within "
     "180&nbsp;days", "FBC Building 105.4.1, 105.4.1.3"),
    ("Threshold buildings are over three stories or 50&nbsp;feet, so the special "
     "inspector regime does not reach a house", "s. 553.71(12)"),
    ("Termite protection and the licensed pest control company's Certificate "
     "of Compliance", "FBC Residential R318.1"),
    ("Maximum 7&nbsp;ACH50, who may perform the test, and mechanical ventilation "
     "below 3&nbsp;ACH50", "FBC Energy Conservation R402.4.1.2"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "fl-permit-kit",
                       "FL.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
