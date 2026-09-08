#!/usr/bin/env python3
"""NY.5 Forms & Documents Index.

Every document an owner-builder will meet in New York, named as the agency
names it, with what it is, when it happens and where it comes from.

Two negative sections carry real weight here. "What may need no permit" is
printed with its condition — the exemptions are the permit office's to adopt,
not the state's to grant — and "What New York does not require" exists because
owner-builders arriving from other states routinely budget for radon piping
and residential sprinklers, neither of which the Uniform Code demands on a
two-story house.

Verified sources:
  GML § 125; WCL § 57                the permit gate
  WCB BIZ-ContractREQs-fs-1-v12      C-105.2, U-26.3, DB-120.1, SI-12, DB-155;
                                     ACORD not acceptable
  WCB-Exemption-Instr-1-v3           CE-200 via Business Express; homeowner path
  19 NYCRR § 1203.3(a)(2)(iv), (a)(3)(vii)  statement of special inspections;
                                     energy compliance statement
  19 NYCRR § 1203.3(d)(2)(ii), (iv)  final report of special inspections;
                                     written test results
  2025 ECCCNYS [NY] R402.5.1.2; R401.3
  10 NYCRR § 75.5(b), (c)            design professional; alternative systems
  ECL § 15-1525(3)                   well completion report; copy to owner
  19 NYCRR § 1203.3(d)(1), (4)       CO; temporary CO
  2025 RCNYS [NY] R115; Exec. Law § 378(5-c)  solid-fuel certificate
  Exec. Law § 378(5-b)               smoke-alarm affidavit at conveyance
  19 NYCRR § 1205.4                  the Part 1205 petition
  Exec. Law § 809                    APA permit
  10 NYCRR § 128-3.8                 DEP approval
  19 NYCRR § 1203.3(a)(1); § 1202.3(b)  the eight exemption categories
  2025 RCNYS [NY] R101.2.1, R309.2, E3401.2.1; Exec. Law § 381(1)
  2025 RCNYS [NY] P2602.1.1; ECL § 15-1525(1)

DELIBERATELY NOT CLAIMED:
  - Any local form name. Those vary by municipality and are unverifiable in
    bulk; the document gives write-in lines instead.
  - A form number for the Part 1205 petition or the DOS complaint. Both are
    "a form prescribed by the department"; the document points at the page.
  - The Part 1205 fee amount. Not retrieved.
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

FORM_ID = "NY.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Forms & Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document you will meet, named as the agency names it — and the "
    "things New York never asks you for.")

flow.append(k.disclaimer(
    "Form numbers were read from the agencies' own current forms and rules in "
    "September 2026. Where no form number is published, this document says so "
    "rather than inventing one."))
flow.append(Spacer(1, 10))

# ----------------------------------------------------------- with the app
flow += k.h2_tight("WITH THE APPLICATION", 2.2)
rows = [
    [k.cellp("<b>Form CE-200</b><br/>Certificate of Attestation of Exemption"),
     k.cellp("Your affidavit under GML §&#160;125 that you have “not engaged an "
             "employer or any employees.” Applied for online as a "
             "<b>homeowner</b>; a NY.gov Business account is required; "
             "<b>job-specific</b> — one per building permit. Print, sign, "
             "submit with the application."),
     k.cellp("businessexpress.ny.gov")],
    [k.cellp("<b>Form C-105.2</b> and <b>DB-120.1</b>"),
     k.cellp("The alternative door: carrier-issued certificates of workers' "
             "compensation and of disability and Paid Family Leave coverage, "
             "sent by the carrier to the permit office. The State Insurance "
             "Fund's version of the first is <b>U-26.3</b>; self-insurers "
             "use SI-12 and DB-155. “<b>ACORD forms are not acceptable</b>.” "
             "Also what you collect from every trade you hire."),
     k.cellp("Your carrier")],
    [k.cellp("<b>Statement of special inspections</b>"),
     k.cellp("Required “where applicable” in the application. Names the "
             "electrical inspection agency your office has approved, and any "
             "other special inspector."),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(a)(2)(iv)"))],
    [k.cellp("<b>Written statement of Energy Code compliance</b>"),
     k.cellp("Part of the construction documents: which path (prescriptive "
             "with the R408 package, R405 performance, or R406 ERI) and the "
             "values. Software output from a compliance tool is the usual "
             "form; the rule does not prescribe one."),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(a)(3)(vii)"))],
    [k.cellp("<b>Stamped construction documents</b>"),
     k.cellp("Above 1,500&#160;sq&#160;ft gross, drawings sealed and signed by "
             "a New York-licensed architect or engineer, showing the "
             "registration expiration date and, for a firm, its Certificate "
             "of Authorization number."),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(a)(3)(ix)"))],
    [k.cellp("<b>Site plan on a boundary survey</b>"),
     k.cellp("Drawn to scale, “drawn in accordance with an accurate boundary "
             "survey,” with distances to lot lines, street and finished "
             "grades, and flood hazard areas."),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(a)(3)(viii)"))],
    [k.cellp("<b>Appendix 75-A septic design</b>"),
     k.cellp("Prepared by or under a design professional and submitted to "
             "the county health department or DOH district office for "
             "approval. An alternative system needs prior approval and a "
             "post-construction certification from the design professional."),
     k.cellp("10 NYCRR<br/>" + sec("75.5(b)") + ", (c)")],
    [k.cellp("<b>APA permit application</b> or <b>DEP approval</b>"),
     k.cellp("Only inside the Adirondack Park (single-family dwelling in a "
             "resource management area, or near forest preserve or a state "
             "highway) or the NYC watershed (any new subsurface system). "
             "NY.4."),
     k.cellp("Exec. Law<br/>" + sec("809") + ";<br/>10 NYCRR<br/>"
             + sec("128-3.8"))],
]
flow.append(k.ref_table(
    "What goes in before the permit issues",
    [k.cellp("Document", bold=True), k.cellp("What it is", bold=True),
     k.cellp("Source", bold=True)],
    rows, [1.75 * inch, CW - 1.75 * inch - 1.5 * inch, 1.5 * inch]))

# ----------------------------------------------------- during and after
flow += k.h2_tight("DURING CONSTRUCTION AND AFTER", 2.2)
rows = [
    [k.cellp("<b>The permit itself</b>"),
     k.cellp("Carries a specific expiration date; must be “visibly displayed "
             "at the worksite”; one set of stamped approved documents stays "
             "on site. No state form number — each office prints its own."),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(a)(4)") + "–(8)")],
    [k.cellp("<b>Electrical rough-in and final certificates</b>"),
     k.cellp("Issued by the approved agency. The final certificate is the "
             "“final report of special inspections” the office must hold "
             "before the CO. Deliver it to the office."),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(d)(2)(ii)"))],
    [k.cellp("<b>Air-leakage test report</b>"),
     k.cellp("The tester's written blower-door result, “provided to the "
             "building official.” A CO precondition. Limit 3.0 ACH in Zones "
             "4–5, 2.5 in Zone 6."),
     k.cellp("2025 ECCCNYS<br/>[NY] R402.5.1.2;<br/>19 NYCRR<br/>"
             + sec("1203.3(d)(2)(iv)"))],
    [k.cellp("<b>Energy certificate (posted)</b>"),
     k.cellp("Permanent, at the furnace or utility room: R-values, U-factors, "
             "test results, equipment efficiencies, the code edition and "
             "the compliance path."),
     k.cellp("2025 ECCCNYS<br/>R401.3")],
    [k.cellp("<b>Water well completion report</b>"),
     k.cellp("Filed with DEC by the registered driller; “the water well "
             "driller shall provide a copy of such completion report to the "
             "water well owner.” <b>Get the copy</b> — it is the well's only "
             "record."),
     k.cellp("ECL<br/>" + sec("15-1525(3)"))],
    [k.cellp("<b>Solid-fuel certificate of compliance</b>"),
     k.cellp("Separate permit, inspection and certificate for any wood "
             "stove, chimney or flue <b>before it is operated</b>."),
     k.cellp("2025 RCNYS<br/>[NY] R115")],
    [k.cellp("<b>Certificate of occupancy</b>"),
     k.cellp("The only lawful permission to occupy. Carries the permit "
             "number, address and tax map number, use classification and any "
             "special conditions. A <b>temporary CO</b> is available before "
             "completion, for a specified period, once the house is safe to "
             "occupy with alarms operational and egress complete."),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(d)(1)") + ", (3), (4)")],
    [k.cellp("<b>Part 1205 petition</b>"),
     k.cellp("Appeal of a code official's order, determination or inaction, "
             "or a variance from the code — on a DOS-prescribed form with a "
             "fee, decided in 60 days. Start at dos.ny.gov/code/variances."),
     k.cellp("19 NYCRR<br/>" + sec("1205.4"))],
]
flow.append(k.ref_table(
    "What is created while you build, and what you keep",
    [k.cellp("Document", bold=True), k.cellp("What it is", bold=True),
     k.cellp("Source", bold=True)],
    rows, [1.75 * inch, CW - 1.75 * inch - 1.5 * inch, 1.5 * inch]))

# ---------------------------------------------------------------- local docs
flow += k.h2_tight("THE LOCAL DOCUMENTS — WRITE IN WHAT YOURS CALLS THEM", 1.8)
flow.append(k.body(
    "Each permit office prints its own paperwork under its own names, and "
    "there is no statewide vocabulary for it. These are the ones that exist "
    "nearly everywhere."))
flow += k.check_table(
    "What my office calls each document",
    [
        ("<b>Building permit application</b> — and whether a homeowner "
         "version exists:", [("Called", 0.6), ("Homeowner form?", 0.4)]),
        ("<b>Zoning or site plan approval</b>, if separate:",
         [("Called", 0.6), ("Issued by", 0.4)]),
        ("<b>Driveway permit</b>:", [("Called", 0.6), ("Road authority", 0.4)]),
        ("<b>Floodplain development permit</b>, if in a mapped hazard area "
         "(including shaded X):", [("Called", 0.6), ("Administrator", 0.4)]),
        ("<b>Local electrical or plumbing license</b>, if the municipality "
         "or county issues one:", [("Called", 0.6), ("Issued by", 0.4)]),
    ])

# --------------------------------------------------------------- no permit
flow += k.h2_tight("WHAT MAY NEED NO PERMIT — ONLY IF YOUR OFFICE SAYS SO",
                   2.0)
flow.append(k.body(
    "Part 1203 lets a permit office exempt eight categories. It does not "
    "require it to, and a town may demand a permit for a 100&#160;sq&#160;ft "
    "shed. Where the Department of State is the office, the same eight are "
    f"exempt by rule ({sec('1202.3(b)')}). The ones that touch a house:"))
rows = [
    [k.cellp("<b>Accessory sheds</b>"),
     k.cellp("One-story detached structures accessory to a one- or "
             "two-family dwelling, “used for tool and storage sheds, "
             "playhouses, or similar uses, provided the gross floor area does "
             "not exceed <b>144&#160;square feet</b>.”")],
    [k.cellp("<b>Window awnings</b>"),
     k.cellp("On a one- or two-family dwelling.")],
    [k.cellp("<b>Finish work</b>"),
     k.cellp("“Painting, wallpapering, tiling, carpeting, or other similar "
             "finish work.”")],
    [k.cellp("<b>Portable appliances</b>"),
     k.cellp("“Installation of listed portable electrical, plumbing, "
             "heating, ventilation, or cooling equipment or appliances.”")],
    [k.cellp("<b>Like-for-like replacement</b>"),
     k.cellp("Replacement of equipment with the same kind in the same "
             "place.")],
    [k.cellp("<b>Non-structural repairs</b>"),
     k.cellp("Repairs that do not affect the structural system, the means "
             "of egress or the fire protection system.")],
]
flow.append(k.ref_table(
    f"The optional exemptions — 19 NYCRR {sec('1203.3(a)(1)')}",
    [k.cellp("What", bold=True), k.cellp("The rule's wording", bold=True)],
    rows, [1.8 * inch, CW - 1.8 * inch]))
flow.append(k.cite(
    "The rule closes with the sentence that matters: “An exemption from the "
    "requirement to obtain a building permit <b>shall not be deemed an "
    "authorization for work to be performed in violation</b> of either or "
    "both of the Codes.” Ask your office which of the eight its local law "
    "adopted; the DOS model local law includes all eight, but a town may "
    "have struck any of them."))

# --------------------------------------------------------------- never
flow += k.h2_tight("WHAT NEW YORK DOES NOT REQUIRE", 2.0)
flow.append(k.body(
    "Worth knowing because owner-builders arriving from other states "
    "routinely budget for these. Under the Uniform Code, none of them is "
    "required on an ordinary house."))
flow.append(k.bullet(
    "<b>Radon-resistant construction.</b> Appendix BE is “included for "
    "informational purposes” — not adopted ([NY] R101.2.1). A municipality "
    "cannot simply adopt it; a more-restrictive standard needs Code Council "
    f"approval (Exec. Law {sec('379')})."))
flow.append(k.bullet(
    "<b>Residential sprinklers below three stories.</b> Required in one- and "
    "two-family dwellings only at “three stories above grade plane” "
    "([NY] R309.2) — but count a walk-out basement carefully."))
flow.append(k.bullet(
    "<b>A state contractor license, or an owner-builder affidavit.</b> "
    "Neither exists. The only state affidavit is the CE-200, and it is about "
    "employees."))
flow.append(k.bullet(
    "<b>An electrical system at all</b>, in an owner-occupied one-family "
    "dwelling — “unless expressly required by statute, local law, ordinance, "
    "or other regulations” ([NY] E3401.2.1). Check the local law."))
flow.append(k.bullet(
    "<b>Periodic inspection of your house once you live in it.</b> No rule "
    "may require “regular, periodic inspections of … owner-occupied one and "
    f"two-family dwellings” (Exec. Law {sec('381(1)')})."))
flow.append(k.bullet(
    "<b>A statewide frost depth, snow load or fee.</b> The first two are the "
    "office's to write into Table R301.2; the third is its legislative "
    "body's to set by resolution."))
flow.append(k.cite(
    "<b>Each of these is the Uniform Code's answer.</b> A local law may add "
    "to the process — a zoning condition, a local license — but may not add "
    "to the construction standard without the Code Council's approval, and "
    "DOS keeps the list of standards it has approved."))

# --------------------------------------------------------------- may not
flow += k.h2_tight("THE TWO THINGS YOU MAY NOT DO YOURSELF", 1.8)
flow.append(k.body(
    "New York is quiet about owner-performed work — it licenses nothing at "
    "state level, so the only limits are local. Two exceptions are written "
    "into the code by reference, and both are on the health side."))
flow.append(k.callout(
    "You may not drill the well, and you may not design the septic system", [
        Paragraph("<b>The well.</b> “Individual water supplies (private wells) "
                  "<b>shall be installed by a well driller registered with the "
                  "Department of Environmental Conservation</b> and be in "
                  "compliance with the provisions of Appendix 5-B” "
                  "([NY] P2602.1.1). The Environmental Conservation Law itself "
                  "only regulates “the business of water well drilling” "
                  f"(ECL {sec('15-1525(1)')}), which is why some guides say an "
                  "owner may drill their own; the Uniform Code closes that "
                  "door for a house. Verify the driller at DEC's registered "
                  "contractor search, and get your copy of the completion "
                  "report.", S["body"]),
        Paragraph("<b>The septic design.</b> “Plans for the design of "
                  "individual onsite wastewater treatment systems <b>shall be "
                  "prepared directly by or under the supervision of a design "
                  f"professional</b>” (10 NYCRR {sec('75.5(b)')}). Installing "
                  "it is not restricted by the state rule — but the health "
                  "department inspects before cover, and an alternative system "
                  "must be built under the design professional's supervision "
                  f"({sec('75.5(c)')}).", S["body"]),
    ]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ny-permit-kit",
                       "NY.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
