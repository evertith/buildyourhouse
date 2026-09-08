#!/usr/bin/env python3
"""NY.3 Inspection Sequence.

Every New York claim in this document was read against its primary source in
September 2026 and is cited on-page.

The organizing idea: 19 NYCRR Part 1203 fixes the FLOOR of inspections that
every code enforcement program in the state must provide — eleven elements,
which is already more than Pennsylvania's five — and the local law may add to
it. Two of those elements are performed by people you hire rather than by the
office: the electrical inspection is a "special inspection" that the office
may accept only from an agency it has approved, and the energy air-leakage
test is a written report from a tester. Both are certificate-of-occupancy
preconditions, so the owner-builder who does not manage them does not get a
CO.

The second half of the document is the part New York does better than most
states: a fixed 30-day order-to-remedy clock, a penalty section that names
"any owner, builder," and a statutory appeal from any code official's order —
or inaction — to a DOS regional board of review that must decide in 60 days.

Verified sources:
  19 NYCRR § 1203.3(b)(1)     the eleven inspection elements, verbatim; remote
                              inspections at the AHJ's discretion
  19 NYCRR § 1203.3(b)(2),(3) work stays exposed; notify when ready; a failed
                              inspection must cite "the specific code provision"
  19 NYCRR § 1203.2(e)        contracted-out enforcement — permit still issues
                              from the municipality
  19 NYCRR § 1203.2(e)(4)     electrical is a special inspection; approved
                              agency only
  2025 RCNYS E3403.2          new electrical work inspected
  2025 ECCCNYS [NY] R402.5.1.1, .2, .3; R401.3
  19 NYCRR § 1203.3(c)        stop work orders
  19 NYCRR § 1203.5(c)–(f)    order to remedy: 30 days; service; begin now
  Exec. Law § 382(1)–(3)      appearance tickets; $1,000/day; removal
  2025 RCNYS [NY] R112.1      appeal of any order, determination or inaction
  19 NYCRR § 1205.3(a)(2), § 1205.4(b), (e)  the regional board of review;
                              60 days
  2025 RCNYS [NY] R104.2.2    no local official may waive or vary
  19 NYCRR § 1203.3(d)(1)–(5) the certificate of occupancy
  2025 RCNYS [NY] R109.1, R109.3, R110.1
  Exec. Law § 378(5-b)        smoke-alarm affidavit at conveyance
  Exec. Law § 381(1)          no periodic inspection of owner-occupied dwellings

DELIBERATELY NOT CLAIMED, and why:
  - Any inspector response time. No provision of Part 1203 obliges the office
    to attend within any number of days (verified absence).
  - Any CO-issuance clock. None exists (verified absence).
  - The Part 1205 fee amount. The fee schedule was not retrieved; the
    document says a fee applies and points at DOS.
  - A list of approved electrical inspection agencies. None exists at state
    level; approval is per office under § 1203.2(e)(4).
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
CITE = k.CITE_COL

FORM_ID = "NY.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The eleven inspection elements the state rule requires, the two that "
    "come from people you hire, the 30-day clock on an order to remedy, the "
    "appeal you have, and the certificate of occupancy.")

flow.append(k.disclaimer(
    "Part 1203 is the floor. Your office's local law may add inspections and "
    "fixes its own scheduling practice; no state rule says how quickly an "
    "inspector must come."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- floor
flow += k.h2_tight("THE FLOOR — ELEVEN ELEMENTS, IN EVERY PROGRAM", 2.4)
flow.append(k.body(
    "Every code enforcement program — town, county or Department of State — "
    "must provide for at least these. This is the whole of the list, quoted, "
    "with the rule's own qualifier: “where applicable.”"))
flow.append(k.callout_long(
    f"19 NYCRR {sec('1203.3(b)(1)')} — inspections “shall include but not "
    "be limited to the following elements of the construction process”", [
        Paragraph("“(i) <b>worksite prior to the issuance of a permit</b>; "
                  "(ii) <b>footing and foundation</b>; (iii) <b>preparation "
                  "for concrete slab</b>; (iv) <b>framing</b>; (v) structural, "
                  "<b>electrical</b>, plumbing, mechanical, fire-protection, "
                  "and other similar service systems of the building; "
                  "(vi) fire resistant construction; (vii) fire resistant "
                  "penetrations; (viii) <b>solid fuel-burning heating "
                  "appliances, chimneys, flues, or gas vents</b>;", S["body"]),
        Paragraph("(ix) inspections required to demonstrate <b>Energy Code "
                  "compliance</b>, including but not limited to insulation, "
                  "fenestration, <b>air leakage</b>, system controls, "
                  "mechanical equipment size, and, where required, minimum "
                  "fan efficiencies, programmable thermostats, energy "
                  "recovery, whole-house ventilation, plumbing heat traps, "
                  "high-performance lighting, and controls; (x) installation, "
                  "connection, and assembly of factory manufactured buildings "
                  "and manufactured homes; and (xi) <b>a final inspection "
                  "after all work authorized by the building permit has been "
                  "completed</b>.”", S["body"]),
    ]))
flow.append(k.cite(
    "Rule text adopted 29&#160;December 2021, effective 30&#160;December 2022, "
    "read from the Department of State's own PDF. The same paragraph allows "
    "<b>remote inspections</b> “when, at the discretion of the authority "
    "having jurisdiction, the remote inspection can be performed to the same "
    "level and quality as an in-person inspection.” Note element (i): a "
    "<b>site visit before the permit issues</b>, which most states do not "
    "have — do not be surprised when the officer wants to walk the lot "
    "before signing. Your office's list will usually be longer than eleven; "
    "ask for it and write the extras on the log at the end."))

flow.append(Spacer(1, 4))
rows = [
    [k.cellp("<b>Keep it open</b>"),
     k.cellp("Work “shall remain accessible and exposed until inspected and "
             "accepted by the authority having jurisdiction.” Close a wall "
             "before the framing visit and you open it again."),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(b)(2)") + ";<br/>[NY] R109.1")],
    [k.cellp("<b>You call it in</b>"),
     k.cellp("The permit holder must “notify the authority having "
             "jurisdiction when construction work is ready for inspection.” "
             "Nobody comes unbidden."),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(b)(2)") + ";<br/>[NY] R109.3")],
    [k.cellp("<b>A failure must cite the section</b>"),
     k.cellp("After each inspection the office “shall note the work … to be "
             "satisfactory as completed, or the building permit holder shall "
             "be notified as to the manner in which the work fails to comply "
             "… <b>including a citation to the specific code provision or "
             "provisions that have not been met</b>.” Non-compliant work stays "
             "exposed until re-inspected. If you are failed without a "
             "section number, ask for one — the rule entitles you to it."),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(b)(3)"))],
]
flow.append(k.ref_table(
    "Your duties and the inspector's",
    [k.cellp("", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - CITE, CITE]))
flow.append(k.cite(
    "<b>How fast must they come? No state rule says.</b> Part 1203 sets no "
    "response time; the local law or the office's practice governs. If the "
    "answer is a long wait, the Part 1205 appeal below reaches “the failure "
    "… to make an order or determination within a reasonable amount of "
    "time.”"))

# ------------------------------------------------------------ electrical
flow += k.h2_tight("ELECTRICAL — A SPECIAL INSPECTION ON THE AGENCY'S "
                   "CERTIFICATES", 2.0)
flow.append(k.body(
    "The code book says new electrical work “shall be inspected by the "
    "building official” (2025 RCNYS E3403.2). The rule sitting above the "
    "book decides who that is in practice, and it is the New York trap."))
flow.append(k.callout_long(
    f"19 NYCRR {sec('1203.2(e)(4)')} — special inspections", [
        Paragraph("“‘Special inspections’ (as defined in the Uniform Code), "
                  "including but not limited to, <b>electrical inspections</b>, "
                  "elevator inspections, welding inspections, and smoke "
                  "control system inspections are not considered to be "
                  "building safety inspector enforcement activities or code "
                  "enforcement official enforcement activities … However, an "
                  "authority having jurisdiction <b>shall not accept or rely "
                  "upon a special inspection unless the person performing "
                  "such special inspection (i) is a qualified person employed "
                  "or retained by an agency that has been approved by the "
                  "authority having jurisdiction and (ii) has been approved by "
                  "the authority having jurisdiction</b> as having the "
                  "competence necessary to inspect a particular type of "
                  "construction requiring such special inspection.”",
                  S["body"]),
        Paragraph("<b>What it means on the ground.</b> Most New York building "
                  "departments employ no electrical inspector. They accept "
                  "rough-in and final certificates from third-party electrical "
                  "inspection agencies — but only from agencies <b>they</b> "
                  "have approved, and there is no state list. You cannot pick "
                  "any inspector. The certificate of occupancy then waits on "
                  "the office having “received and reviewed … a <b>final "
                  "report of special inspections</b>” "
                  f"(19 NYCRR {sec('1203.3(d)(2)(ii)')}). The agency's final "
                  "certificate is that report; make sure it reaches the "
                  "office, not just your file. It is the one part of a New "
                  "York inspection you engage and pay directly — an office "
                  "may contract its other inspections to a private firm "
                  f"({sec('1203.2(e)')}), but the permit still issues from "
                  "the municipality.", S["body"]),
    ]))
flow.append(Spacer(1, 4))
flow += k.check_table(
    "The electrical track — the four documents that must exist", [
        ("Approved-agency list obtained from the office, and the agency I "
         "engaged:", [("Agency", 1.0)]),
        ("<b>Rough-in certificate</b> issued, before any wiring is covered:",
         [("Date", 0.5), ("Certificate no.", 0.5)]),
        ("<b>Final certificate</b> issued, after fixtures and the service "
         "are complete:", [("Date", 0.5), ("Certificate no.", 0.5)]),
        ("Final report of special inspections <b>delivered to the permit "
         "office</b> — confirmed received:", [("Date", 0.5), ("By whom", 0.5)]),
    ])

# ---------------------------------------------------------------- energy
# The three headings below carry 1.3–1.4in reserves rather than the 2.0–2.4
# the rest of the kit uses. Each is followed by a three- or four-line lead
# and then a table or box whose first chunk is 1.2–1.5in tall, so a 2in
# reserve threw heading, lead and table to the next page together and left
# 1.5–1.9in blank at the foot of three consecutive pages — a whole page of
# whitespace across the document. The smaller reserve keeps heading and lead
# together (reportlab's orphan control guarantees at least two lines of the
# lead) and lets the table move on its own.
flow += k.h2_tight("ENERGY — THE INSPECTION, THE TEST AND THE WRITTEN RESULT",
                   1.4)
flow.append(k.body(
    "Element (ix) above is not one visit. The insulation is inspected before "
    "the wall closes, the blower door happens when the envelope is complete, "
    "and the written test result is a document the certificate of occupancy "
    "depends on."))
rows = [
    [k.cellp("<b>Insulation, open-wall</b>"),
     k.cellp("Components installed per Table R402.5.1.1; “where required by "
             "the building official, an approved third party shall inspect "
             "all components,” with “an open wall visual inspection.” No more "
             "than 2% of the insulated area may contain gaps, voids or "
             "compression. <b>Do not hang drywall before this is signed "
             "off.</b>"),
     k.cellp("2025 ECCCNYS<br/>[NY] R402.5.1.1")],
    [k.cellp("<b>The blower door, and its report</b>"),
     k.cellp("Mandatory. “The building or each dwelling unit … shall be "
             "tested for air leakage … Where required by the building "
             "official, testing shall be conducted by an approved third "
             "party. <b>A written report … shall be … provided to the "
             "building official.</b>” Limit <b>3.0 ACH</b> in Zones 4–5, "
             "<b>2.5 ACH</b> in Zone 6 (NY.2 has your county's zone). No CO "
             "until the office has “received and reviewed each written "
             "statement of the results of tests performed to show compliance "
             "with the Energy Code” — get the report to the office the day "
             "you get it."),
     k.cellp("2025 ECCCNYS<br/>[NY] R402.5.1.2, .3;<br/>19 NYCRR<br/>"
             + sec("1203.3(d)(2)(iv)"))],
    [k.cellp("<b>The posted certificate</b>"),
     k.cellp("A permanent certificate at the furnace or utility room listing "
             "R-values, U-factors, the blower-door and any duct-test results, "
             "equipment efficiencies, and “the code edition under which the "
             "structure was permitted, the compliance path used.” The final "
             "inspector will look for it."),
     k.cellp("2025 ECCCNYS<br/>R401.3")],
]
flow.append(k.ref_table(
    "Three energy items, in the order they happen",
    [k.cellp("Item", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - CITE, CITE]))

# ------------------------------------------------------------ enforcement
flow += k.h2_tight("STOP WORK, ORDER TO REMEDY, AND THE $1,000-A-DAY CLOCK",
                   1.4)
flow.append(k.body(
    "New York fixes the one enforcement clock most states leave open, and "
    "names the owner in the penalty section."))
rows = [
    [k.cellp("<b>Stop work order</b>"),
     k.cellp("Issued for work “contrary to provisions of either or both of "
             "the Codes, is being conducted in a dangerous or unsafe manner, "
             "is being performed without obtaining a required building "
             "permit, or when a building permit has been issued in error.” "
             "It “shall state the reason for its issuance and the conditions "
             "which must be satisfied before work will be allowed to "
             "resume.”"),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(c)"))],
    [k.cellp("<b>Order to remedy — 30&#160;days</b>"),
     k.cellp("“The time within which a person or entity served with an order "
             "to remedy is required to comply with such order to remedy is "
             "hereby fixed at <b>30&#160;days</b> following the date of such "
             "order.” Served personally or by certified or registered mail "
             "within five days of the order; a mailed order is deemed served "
             "on the mailing date. The office may require corrective action "
             "to <b>begin</b> immediately, or vacating or barricading while "
             "it proceeds."),
     k.cellp("19 NYCRR<br/>" + sec("1203.5(c)") + ", (e), (f)")],
    [k.cellp("<b>The penalty</b>"),
     k.cellp("Failing to comply with an order to remedy, or knowingly "
             "violating the Uniform Code as “any <b>owner, builder</b>, "
             "architect, tenant, contractor, subcontractor, construction "
             "superintendent or their agents or any other person taking part "
             "or assisting in the construction of any building,” is "
             "“punishable by a fine of not more than <b>one thousand dollars "
             "per day of violation</b>, or imprisonment not exceeding one "
             "year, or both.” A court “may order the removal of the building "
             "or an abatement of the condition.” The office may also issue "
             "appearance tickets."),
     k.cellp("Exec. Law<br/>" + sec("382(1)") + "–(3)")],
]
flow.append(k.ref_table(
    "The three pieces of paper, and what each one starts",
    [k.cellp("", bold=True), k.cellp("What the rule says", bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - CITE, CITE]))
flow.append(k.cite(
    "The 30-day figure is the time the Executive Law says must be “stated "
    f"in the order” ({sec('382(2)')}); Part 1203 fixes it statewide so no "
    "office can shorten it. Missing the 30 days is what converts a "
    "correctable violation into the per-day exposure — <b>if you cannot "
    "finish in 30 days, ask in writing for more time before day 30, not "
    "after</b>."))

# ------------------------------------------------------------- appeals
flow += k.h2_tight("THE APPEAL YOU HAVE — A REGIONAL BOARD OF REVIEW, "
                   "DECIDED IN 60 DAYS", 1.3)
flow.append(k.body(
    "This is the page Pennsylvania's opt-out towns do not have. New York "
    "gives every permit applicant a statutory forum above the code official, "
    "and the code book says so in its own administrative chapter."))
flow.append(k.callout_long(
    "The right, and the procedure", [
        Paragraph("<b>2025 RCNYS [NY] R112.1:</b> “An appeal of any order or "
                  "determination, <b>or the failure within a reasonable time "
                  "to make an order or determination</b>, of an administrative "
                  "official charged to enforce or purporting to enforce the "
                  "Uniform Code may be made in accordance with the provisions "
                  "of Part 1205.”", S["body"]),
        Paragraph(f"<b>19 NYCRR {sec('1205.3(a)(2)')}:</b> “Each regional "
                  "board of review shall have the power to hear and decide "
                  "appeals. An appeal may be of any order or determination, "
                  "relating directly to the provisions of the Uniform Code, "
                  "of an administrative official authorized to enforce the "
                  "Uniform Code, or the failure of an administrative official "
                  "to make such an order or determination within a reasonable "
                  "amount of time.” Remedies include “sustaining, reversing, "
                  "or modifying” the order, or “directing that any orders, "
                  "determinations, permits, or authorizations be issued.”",
                  S["body"]),
        Paragraph(f"<b>How:</b> “Any person aggrieved may petition the "
                  "regional board of review for an appeal” "
                  f"({sec('1205.4(b)')}), on a Department of State form with "
                  f"the fee set by {sec('1205.6')} (amount not printed here — "
                  "start at <b>dos.ny.gov/code/variances</b>). <b>When:</b> "
                  "“Petitions shall be decided within <b>60&#160;days</b> of "
                  "completeness unless a longer period is required for good "
                  f"cause shown” ({sec('1205.4(e)')}). DOS's 2026 guide "
                  "describes six regional boards of five members each — an "
                  "architect, an engineer, a code-enforcement background, a "
                  "fire background, and a businessperson or lawyer.",
                  S["body"]),
    ]))
flow.append(k.cite(
    "<b>Two things Part 1205 is not.</b> It is not a way to get a local "
    "official to bend the code: a building official may not “waive, vary, "
    "modify, or otherwise alter” any provision ([NY] R104.2.2), and a "
    "<b>variance</b> from the code itself is a separate Part 1205 petition to "
    f"DOS, also on a 60-day clock (Exec. Law {sec('381(1)(f)')}). And it is "
    "not the place for a complaint about an official's <i>conduct</i> rather "
    "than a decision — that goes to DOS on its code enforcement official "
    "complaint form at <b>dos.ny.gov/code/complaints</b>."))

# --------------------------------------------------------------- the CO
flow += k.h2_tight("THE CERTIFICATE OF OCCUPANCY", 2.2)
flow.append(k.body(
    "Permission to occupy “shall be granted only by issuance of a certificate "
    f"of occupancy or a certificate of compliance” (19 NYCRR "
    f"{sec('1203.3(d)(1)')}), and the code says the same: no occupancy "
    "without a CO where the local program requires one ([NY] R110.1). The "
    "rule then lists what the office must hold before it may sign — and "
    "<b>two of the five come from people you hired</b>, which is why an "
    "owner-builder's CO most often stalls on paperwork rather than on the "
    "house."))
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp("Inspected the work and found it in compliance with the codes."),
     k.cellp(sec("1203.3(d)(2)(i)"))],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("Where applicable, received and reviewed each written statement "
             "of structural observations and the <b>final report of special "
             "inspections</b> — your electrical agency's final certificate."),
     k.cellp(sec("1203.3(d)(2)(ii)"))],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("Where applicable, received and reviewed the <b>flood hazard "
             "certifications</b> — an elevation certificate if you built in "
             "a flood zone, which in New York includes shaded X."),
     k.cellp(sec("1203.3(d)(2)(iii)"))],
    [k.cellp("<b>4</b>", center=True),
     k.cellp("Where applicable, received and reviewed each <b>written "
             "statement of Energy Code test results</b> — the blower-door "
             "report."),
     k.cellp(sec("1203.3(d)(2)(iv)"))],
    [k.cellp("<b>5</b>", center=True),
     k.cellp("Where applicable, verified the seals and data plates on any "
             "factory-built component or manufactured home."),
     k.cellp(sec("1203.3(d)(2)(v)"))],
]
flow.append(k.ref_table(
    "Five things the office must have before the CO — 19 NYCRR "
    + sec("1203.3(d)(2)"),
    [k.cellp("", bold=True, center=True), k.cellp("Precondition", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [0.35 * inch, CW - 0.35 * inch - CITE, CITE]))
flow.append(Spacer(1, 6))
flow.append(k.callout_long(
    "What the CO says, the temporary CO, and after", [
        Paragraph("<b>Contents</b> " + f"({sec('1203.3(d)(3)')}): the permit "
                  "number and date, the address and <b>tax map number</b>, "
                  "the portion covered, the use and occupancy classification, "
                  "construction type, “any special conditions imposed in "
                  "connection with the issuance of the building permit,” the "
                  "signature and the issue date. Keep it with the deed.",
                  S["body"]),
        Paragraph("<b>Temporary CO</b> " + f"({sec('1203.3(d)(4)')}): allowed "
                  "before completion, “limited to a specified period of "
                  "time,” and only once the structure “may be occupied "
                  "safely,” the fire, smoke, CO and heat detection is "
                  "“installed and operational,” and “all required means of "
                  "egress … have been provided.” A CO issued in error is "
                  "suspended or revoked if the deficiency is not corrected "
                  f"within a specified period ({sec('1203.3(d)(5)')}). <b>No "
                  "rule sets a number of days for issuing a CO.</b>",
                  S["body"]),
        Paragraph("<b>Afterwards:</b> no rule may require “regular, periodic "
                  "inspections of … owner-occupied one and two-family "
                  f"dwellings” (Exec. Law {sec('381(1)')}), and when you sell, "
                  "an affidavit of smoke-alarm compliance is delivered at "
                  "conveyance, with the buyer having ten days to object "
                  f"(Exec. Law {sec('378(5-b)')}).", S["body"]),
    ]))

# ------------------------------------------------------------------ log
flow += k.h2_tight("INSPECTION LOG — RECORD EVERY ONE", 1.6)
flow += k.check_table(
    "Every visit, whoever performed it",
    [
        ("<b>Pre-permit worksite</b> visit, element (i).",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Footing and foundation</b> — forms and steel before concrete, "
         "at the frost depth in the office's Table R301.2; walls, "
         "damp-proofing and drainage before backfill.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Slab preparation</b> — base, vapor retarder, slab insulation "
         "(R-10ci, 4&#160;ft), before the pour.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Electrical rough-in</b> — the approved agency's certificate.",
         [("Date", 0.34), ("Agency", 0.33), ("Cert. no.", 0.33)]),
        ("<b>Plumbing and mechanical rough-in</b>, before concealment.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Framing</b> — with braced walls per the approved drawings, "
         "fire-resistant construction and penetrations, and the chimney or "
         "flue if any.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Insulation, open-wall</b> — before drywall.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Solid-fuel appliance</b> — separate permit and certificate of "
         "compliance before it is operated ([NY] R115).",
         [("Date", 0.34), ("Inspector", 0.33), ("Cert.", 0.33)]),
        ("<b>Blower door</b> — written report delivered to the office. "
         "Limit 3.0 ACH (Zones 4–5) or 2.5 ACH (Zone 6).",
         [("Date", 0.34), ("Result ACH", 0.33), ("Report sent", 0.33)]),
        ("<b>Electrical final</b> — the agency's final certificate, delivered "
         "to the office as the final report of special inspections.",
         [("Date", 0.34), ("Agency", 0.33), ("Cert. no.", 0.33)]),
        ("<b>Final building inspection</b> — after all permitted work is "
         "complete; R401.3 certificate posted.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Certificate of occupancy</b> issued.",
         [("Date", 0.5), ("Number", 0.5)]),
        ("Any inspection my office requires that is not on this list — ask, "
         "and write it here:", [("Inspection", 0.5), ("Date", 0.5)]),
    ])

# --------------------------------------------------------------- sources
flow.append(k.sources_table([
    ("The eleven inspection elements; remote inspections",
     "19 NYCRR § 1203.3(b)(1)"),
    ("Work stays exposed; permit holder notifies; failure must cite the "
     "section", "19 NYCRR § 1203.3(b)(2), (3); 2025 RCNYS [NY] R109.1, R109.3"),
    ("Electrical inspections are special inspections; approved agency only; "
     "contracted enforcement acts for the office",
     "19 NYCRR § 1203.2(e), (e)(4); 2025 RCNYS E3403.2"),
    ("Insulation inspection; mandatory air-leakage test; written report; "
     "posted certificate", "2025 ECCCNYS [NY] R402.5.1.1–.3; R401.3"),
    ("Stop work orders; order to remedy: 30 days; service; begin immediately",
     "19 NYCRR §§ 1203.3(c), 1203.5(c), (e), (f)"),
    ("$1,000 per day; “any owner, builder”; removal or abatement",
     "Exec. Law § 382(1)–(3)"),
    ("Appeal of any order, determination or inaction; petition with fee; "
     "decided within 60 days",
     "2025 RCNYS [NY] R112.1; 19 NYCRR §§ 1205.3(a)(2), 1205.4(b), (e), "
     "1205.6"),
    ("No local official may waive or vary; variances go to DOS",
     "2025 RCNYS [NY] R104.2.2; Exec. Law § 381(1)(f)"),
    ("Occupancy only by CO; five preconditions; contents; temporary CO; "
     "revocation", "19 NYCRR § 1203.3(d)(1)–(5); 2025 RCNYS [NY] R110.1"),
    ("No periodic inspection of owner-occupied dwellings; smoke-alarm "
     "affidavit at conveyance", "Exec. Law §§ 381(1), 378(5-b)"),
]))
flow.append(Spacer(1, 6))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ny-permit-kit",
                       "NY.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
