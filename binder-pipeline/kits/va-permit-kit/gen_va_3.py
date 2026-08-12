#!/usr/bin/env python3
"""VA.3 Inspection Sequence — Virginia.

Sources verified August 2026:
  USBC § 113.1 (13VAC5-63-130)  work "shall not be deemed in compliance
                                until approved"
  USBC § 113.3                  the statewide minimum inspection list, seven
                                items, quoted verbatim on-page
  USBC § 113.6                  defects corrected and reinspected before any
                                work conceals them; written approval or
                                written notice
  USBC § 113.7                  building official may accept third-party
                                inspection reports under a written policy
  § 36-105(B)                   fees (including any reinspection fee) are
                                levied locally
  USBC § 116.1 / 116.1.1 (13VAC5-63-160)  certificate of occupancy before
                                occupancy; temporary CO on request
  § 54.1-1101(B)                exemption users must obtain a CO before
                                conveying to a buyer (see VA.1)
  13VAC5-63-264                 blower-door and duct-test reports that land
                                at final (see VA.2)

Note: unlike some states, Virginia's dossier surfaced NO statute requiring
the owner-builder to be personally present at inspections — so this
document imposes none. Being there anyway is good practice.

Still deliberately hedged: the "two working days" third-party inspection
trigger sometimes attributed to § 113.7 (not verified verbatim — not
printed); the five-working-day CO issuance timing (printed as a labeled
paraphrase of § 116, with a confirm step); and reinspection fees, which are
a local fee-schedule question with no statewide rule to print.
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

FORM_ID = "VA.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The inspections Virginia's building code requires, in order — what "
    "each one checks, what happens when one fails, and a log to record "
    "every result as you go.")

flow.append(k.disclaimer(
    "The USBC sets the minimum inspection list; your building department "
    "schedules them and may inspect more — its instructions govern."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- who sets it
flow += k.h2_tight("WHAT THE STATE SETS AND WHAT YOUR LOCALITY SETS")
flow.append(k.body(
    "The list below is statewide: USBC § 113.3 names the minimum "
    "inspections every Virginia building department must perform on your "
    "house, and this document quotes each one verbatim. How they are "
    "scheduled, whether trades are called together or separately, and "
    "anything your department adds on top is local practice. The "
    "governing principle sits in § 113.1: \"<i>any building or structure "
    "may be inspected at any time before completion and shall not be "
    "deemed in compliance until approved</i>.\" Nothing counts until it "
    "is inspected and approved — so never cover work that has not been."))
flow.append(k.cite(
    "USBC § 113.1, § 113.3 (13VAC5-63-130). Verified August 2026."))

flow.append(k.callout(
    "No owner-present rule — but be there anyway", [
        Paragraph("Some states forbid inspecting an owner-builder's job "
                  "without the owner on site. Virginia's statutes and the "
                  "USBC sections this kit verified impose no such "
                  "requirement — so this document does not invent one. "
                  "Attend every inspection you can regardless: the "
                  "ten-minute conversation with the inspector at footing "
                  "is the cheapest education you will get all build.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- the sequence
flow += k.h2_tight("THE SEQUENCE — THE SEVEN REQUIRED INSPECTIONS, VERBATIM")
seq = [
    ("1. Footing",
     "\"<i>Inspection of footing excavations and reinforcement material "
     "for concrete footings prior to the placement of concrete.</i>\" "
     "Trenches open, rebar placed and supported — and no concrete until "
     "the approval is in hand.",
     "§ 113.3(1)"),
    ("2. Foundation",
     "\"<i>Inspection of foundation systems during phases of construction "
     "necessary to ensure compliance with this code.</i>\" Walls, "
     "waterproofing, anchorage — your department decides which phases it "
     "looks at; ask when you pull the permit.",
     "§ 113.3(2)"),
    ("3. Pre-concrete",
     "\"<i>Inspection of preparatory work prior to the placement of "
     "concrete.</i>\" Slabs and flatwork: everything the pour will bury — "
     "under-slab plumbing and electrical, vapor barrier, fill — complete "
     "first.",
     "§ 113.3(3)"),
    ("4. Framing",
     "\"<i>Inspection of structural members and fasteners prior to "
     "concealment.</i>\" The framing inspection: structure complete, "
     "connections visible, nothing covered.",
     "§ 113.3(4)"),
    ("5. Trade rough-ins",
     "\"<i>Inspection of electrical, mechanical and plumbing materials, "
     "equipment, and systems prior to concealment.</i>\" Everything that "
     "will hide inside walls, floors and ceilings — before insulation, "
     "before drywall. Localities differ on whether trades are called "
     "together or separately.",
     "§ 113.3(5)"),
    ("6. Energy",
     "\"<i>Inspection of energy conservation material prior to "
     "concealment.</i>\" Virginia gives energy its own concealment "
     "inspection — insulation, air barrier and sealing details, checked "
     "before any wall or ceiling covering goes on.",
     "§ 113.3(6)"),
    ("7. Final",
     "\"<i>Final inspection.</i>\" The whole house, complete. This is "
     "where the paper lands too: the blower-door result and the signed "
     "duct-test report go to the code official (see VA.2, section E).",
     "§ 113.3(7)"),
]
rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in seq]
flow.append(k.ref_table(
    "The statewide minimum inspection list — USBC § 113.3",
    [k.cellp("Inspection", bold=True),
     k.cellp("The code's words, and what they mean on site", bold=True),
     k.cellp("Code", bold=True)],
    rows, [1.35 * inch, CW - 1.35 * inch - 0.95 * inch, 0.95 * inch]))
flow.append(k.cite(
    "All seven quoted from USBC § 113.3 (13VAC5-63-130), verified August "
    "2026. The list is the statewide minimum — your department may "
    "inspect \"at any time before completion\" under § 113.1 and may "
    "look at more than the minimum."))

# ---------------------------------------------------------------- failures
flow += k.h2_tight("WHEN AN INSPECTION FAILS — AND WHO ELSE CAN INSPECT")
flow.append(k.body(
    "<b>Defects must be fixed before they disappear.</b> Under USBC "
    "§ 113.6, defective work must be corrected and reinspected "
    "\"<i>before any work proceeds that would conceal such defects</i>\" "
    "— and the official gives you written approval, or a written notice "
    "of defects. Keep every one of those papers with this log. Whether "
    "your locality charges for a failed reinspection is a local "
    "fee-schedule question: fees are levied locally — \"<i>fees may be "
    "levied by the local governing body in order to defray the cost of "
    "such enforcement and appeals</i>\" (§ 36-105(B)) — and there is no "
    "statewide reinspection fee rule, so <b>get the fee schedule when "
    "your permit issues</b>."))
flow.append(k.body(
    "<b>Third-party inspections exist, on the official's terms.</b> "
    "\"<i>The building official may accept reports of inspections and "
    "tests from individuals or inspection agencies approved in "
    "accordance with the building official's written policy required by "
    "Section 113.7.1.</i>\" (§ 113.7) If your department is slow to "
    "schedule, ask whether it has such a policy and which agencies it "
    "has approved. This kit prints no deadline that forces the option "
    "open — the timing trigger sometimes quoted for § 113.7 was not "
    "verified, so do not rely on one."))
flow.append(k.cite(
    "USBC § 113.6, § 113.7 (13VAC5-63-130); § 36-105(B). Verified "
    "August 2026."))

# ---------------------------------------------------------------- certificate
flow += k.h2_tight("THE CERTIFICATE AT THE END — USBC § 116")
flow.append(k.body(
    "\"<i>Prior to occupancy or change of occupancy of a building or "
    "structure, a certificate of occupancy shall be obtained in "
    "accordance with this section.</i>\" (§ 116.1) You do not move in — "
    "not a mattress, not a toothbrush — before it issues. If part of the "
    "house is genuinely done and safe, there is a statutory bridge: "
    "\"<i>Upon the request of a permit holder, a temporary certificate "
    "of occupancy may be issued before the completion of the work "
    "covered by a permit</i>,\" where the portion occupied is safe "
    "(§ 116.1.1)."))
flow.append(k.body(
    "On timing: Section 116 directs the building official to issue the "
    "certificate within five working days after the approved final "
    "inspection once compliance is verified — <b>that sentence is a "
    "paraphrase of the section, not quoted text</b>; confirm the timing "
    "with your building department rather than planning your move around "
    "it. And remember the string from VA.1: an owner who built under the "
    "§ 54.1-1101(A)(7) exemption must obtain the CO <b>before conveying "
    "the property to a buyer</b>, absent the buyer's written waiver "
    "(§ 54.1-1101(B))."))
flow.append(k.cite(
    "USBC § 116.1, § 116.1.1 (13VAC5-63-160); § 54.1-1101(B). Verified "
    "August 2026."))

# ---------------------------------------------------------------- the log
flow += k.h2_tight("INSPECTION LOG — RECORD EVERY ONE")
flow.append(k.body(
    "Fill this in as it happens, not from memory. If a result is ever "
    "disputed, or a later inspector questions earlier work, this page "
    "and your photos are the record you have. Rows are provided for the "
    "trades called separately and for the two energy tests — cross out "
    "what your department does not use."))

log_header = [k.cellp("Inspection", bold=True),
              k.cellp("Called", bold=True),
              k.cellp("Held", bold=True),
              k.cellp("Result", bold=True),
              k.cellp("Inspector", bold=True),
              k.cellp("Corrections required / notes", bold=True)]
log_names = [
    "Footing", "Foundation", "Pre-concrete / slab", "Framing",
    "Electrical rough-in", "Plumbing rough-in", "Mechanical rough-in",
    "Energy / insulation", "Blower-door test", "Duct leakage test",
    "Final — building",
    "", "", "",
]
log_rows = [[k.cellp(n) if n else "", "", "", "", "", ""] for n in log_names]
widths = [1.25 * inch, 0.72 * inch, 0.72 * inch, 0.62 * inch, 1.05 * inch]
widths.append(CW - sum(widths))
flow.append(d.titled_table(
    "Inspection log", log_header, log_rows, widths, S,
    row_heights=[30] * len(log_rows)))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Certificate of occupancy issued:", 0.55),
                         ("Number:", 0.45)]))

flow.append(Spacer(1, 8))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026; USBC sections at "
    "law.lis.virginia.gov/admincode, title 13, agency 5, chapter 63). "
    "Nothing deemed in compliance until approved — § 113.1. The seven "
    "minimum inspections, quoted verbatim — § 113.3. Defects corrected "
    "and reinspected before concealment; written approval or notice — "
    "§ 113.6. Third-party reports under the official's written policy — "
    "§ 113.7. Fees, including any reinspection fee, are local — "
    "§ 36-105(B). Certificate of occupancy before occupancy, and the "
    "temporary CO — § 116.1, § 116.1.1; the five-working-day issuance "
    "timing is a paraphrase of § 116 — confirm it locally. CO before "
    "conveying to a buyer — § 54.1-1101(B). Blower-door and duct-test "
    "reports — 13VAC5-63-264, covered in VA.2."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "va-permit-kit",
                       "VA.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
