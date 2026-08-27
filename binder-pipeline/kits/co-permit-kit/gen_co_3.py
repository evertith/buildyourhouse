#!/usr/bin/env python3
"""CO.3 Inspection Sequence — Colorado.

Colorado's inspection problem is not the ladder; it is that up to four
separate authorities inspect one house and none of them coordinates with the
others. This document names them, works the state process in operational
detail (because that is the one nobody explains), and gives a log for each.

Sources verified August 2026:
  C.R.S. 12-115-120(2)(b)     state inspector must inspect within three
                              working days of receiving the application
  C.R.S. 12-115-120(3)(a)     certificate of approval on a pass
  C.R.S. 12-115-120(3)(b)     written notice of disapproval with reasons;
                              service may be ordered discontinued if
                              hazardous; appeal to the board, heard within
                              seven days; reinspection fee after correction
  C.R.S. 12-115-120(4)        notice of disapproval posted at the site and
                              filed with the board
  C.R.S. 12-115-120(1)(b),(c) board notifies the utility on final approval;
                              utility may not serve without proof of it
  C.R.S. 12-155-120(1)(b),(2) the plumbing twin: three working days,
                              certificate of approval, disapproval process
  C.R.S. 25-10-106(1)(h)      OWTS final inspection after completion but
                              BEFORE the system is placed in use
  dpo.colorado.gov/ElectricalPlumbingPermits  do not call the Division for
                              scheduling — contact your inspector; inspector
                              contact lists and inspection maps published;
                              board policy on who must be present for
                              inspection of OCCUPIED dwelling units; remote
                              video inspection waiver for occupied residential
  Colorado building-department single family/duplex plan review checklists —
                              adopted codes, design criteria, the engineered
                              soils report and foundation, and multi-agency
                              project approval routing
  2021 IECC R401.3 as locally adopted — the permanent energy certificate

Still deliberately hedged: the local ladder itself is labeled TYPICAL, because
no Colorado statute enumerates residential inspections and each jurisdiction's
permit card governs; and the Pueblo design criteria are printed as one
jurisdiction's published figures, never as statewide values. The Pueblo
Regional Building Department was succeeded on January 1, 2026 and is no longer
cited as a live office anywhere in this kit.
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

FORM_ID = "CO.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The up-to-four authorities that inspect one Colorado house, how the "
    "state electrical and plumbing inspections actually work, and a log for "
    "every one of them.")

flow.append(k.disclaimer(
    "Where a local building permit exists, its permit card lists the "
    "inspections your job requires and it governs. The state trade "
    "inspections are additional to it, not part of it."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- who inspects
flow += k.h2_tight("FOUR INSPECTORS, ONE HOUSE, NO COORDINATION")
flow.append(k.body(
    "In a state with a single building department, one office schedules "
    "everything and one final closes the job. In Colorado your house can be "
    "inspected by four authorities under three statutes, and <b>none will "
    "tell the others what happened</b>. Nobody is managing your sequence. "
    "You are."))

who_rows = [
    [k.cellp("<b>Local building inspector</b>"),
     k.cellp("Footings through final, under whichever code edition your "
             "jurisdiction adopted — if it adopted one. Issues the "
             "certificate of occupancy where one exists."),
     k.cellp("Your county or municipality")],
    [k.cellp("<b>Electrical inspector</b>"),
     k.cellp("Rough and final electrical against the National Electrical "
             "Code as adopted by the State Electrical Board. A <b>state</b> "
             "inspector unless your jurisdiction runs its own qualifying "
             "program."),
     k.cellp("State Electrical Board, or your local program")],
    [k.cellp("<b>Plumbing / gas inspector</b>"),
     k.cellp("Plumbing and <b>fuel gas piping</b> against the Colorado "
             "Plumbing and Fuel Gas Codes. Decided separately from "
             "electrical — a jurisdiction may run one and not the other."),
     k.cellp("State Plumbing Board, or your local program")],
    [k.cellp("<b>Public health (OWTS)</b>"),
     k.cellp("Site evaluation before the permit, and a final inspection of "
             "the installed system \"<i>before the system is placed in "
             "use</i>\" (25-10-106(1)(h))."),
     k.cellp("Your local public health agency")],
]
flow.append(k.ref_table(
    "Who can inspect your house, and under whose authority",
    [k.cellp("Inspector", bold=True), k.cellp("What they look at", bold=True),
     k.cellp("Whose office", bold=True)],
    who_rows, [1.5 * inch, CW - 1.5 * inch - 1.65 * inch, 1.65 * inch]))
flow.append(k.cite(
    "C.R.S. 12-115-120(2)(a); 12-155-120(1)(a); 25-10-106(1)(h); "
    "30-28-205(1). A fifth party inspects in practice but not by law: your "
    "lender's draw inspector. Treat their checklist as a floor, not a code."))

# ---------------------------------------------------------------- state process
flow += k.h2_tight("HOW A STATE INSPECTION ACTUALLY WORKS")
flow.append(k.body(
    "Getting this wrong costs weeks. The Division sells the permit; it does "
    "<b>not</b> schedule the inspection. Its instruction is blunt: \"<i>Do "
    "not contact the Division offices regarding inspection requests or "
    "scheduling. You must contact your inspector for scheduling "
    "information.</i>\" It publishes an inspection map and inspector contact "
    "list for each trade — find yours when you buy the permit, not the day "
    "you need them."))

proc_rows = [
    [k.cellp("<b>The clock</b>"),
     k.cellp("A state inspector \"<i>shall inspect … <b>within three working "
             "days after the receipt of the application for "
             "inspection</b></i>\" — same words in both statutes "
             "(12-115-120(2)(b); 12-155-120(1)(b)). A real entitlement; hold "
             "them to it and plan your cover-up around it.")],
    [k.cellp("<b>If it passes</b>"),
     k.cellp("The inspector \"<i>shall issue a certificate of approval</i>\" "
             "(12-115-120(3)(a); 12-155-120(2)(a)). Keep every one — they "
             "evidence that the work was inspected, which on the electrical "
             "side keeps your homeowner exemption alive.")],
    [k.cellp("<b>If it fails</b>"),
     k.cellp("Written notice of disapproval <b>with the reasons</b>, a copy "
             "posted at the installation site and filed with the board "
             "(12-115-120(3)(b), (4)). If the installation is hazardous the "
             "inspector may order electrical service discontinued until it "
             "is made safe. After correcting, you \"<i>shall apply for "
             "reinspection in the same manner as for the original inspection "
             "and pay the required reinspection fee</i>.\"")],
    [k.cellp("<b>Who must be there</b>"),
     k.cellp("Board policy requires the contractor, or an <b>adult homeowner "
             "or the homeowner's representative</b>, to be present for the "
             "inspection <b>of occupied dwelling units</b>. A house under "
             "construction is not occupied — but confirm, and expect to meet "
             "them on a rural parcel they have never visited.")],
]
flow.append(k.ref_table(
    "The state process, start to finish",
    [k.cellp("Stage", bold=True), k.cellp("What the rule is", bold=True)],
    proc_rows, [1.35 * inch, CW - 1.35 * inch]))
flow.append(Spacer(1, 6))

flow.append(k.callout("The finish line is the meter, not the final", [
    Paragraph("On final inspection and approval \"<i>notice shall be issued "
              "by the board to the utility</i>,\" and \"<b><i>A utility shall "
              "not provide service to any person required to have electrical "
              "inspection under this article 115 without proof of final "
              "approval</i></b>\" (12-115-120(1)(b), (c)). Emergencies get "
              "at most seven days. Whatever else is or is not required where "
              "you are building, this is the gate: <b>no approved electrical "
              "final, no permanent power</b>. Schedule your electrical final "
              "with the utility's connection date in mind, not after it.",
              S["body"]),
]))

# ---------------------------------------------------------------- ladder
flow += k.h2_tight("THE TYPICAL LADDER — AND WHERE THE STATE SLOTS IN")
flow.append(k.body(
    "No Colorado statute enumerates residential inspections; your "
    "jurisdiction's adopted code and permit card do. The order below is the "
    "<b>typical</b> shape an IRC-based code produces, annotated with which "
    "authority owns each rung when the state runs the trades. Verify names "
    "and count against your own permit card."))

seq = [
    ("1. Footing / setback", "LOCAL",
     "Forms and steel in place before concrete; setbacks verified against "
     "the approved site plan."),
    ("2. Foundation wall / damproofing", "LOCAL",
     "Before backfill. On expansive soils this is where the engineered "
     "foundation design gets checked against what was actually built."),
    ("3. Underground plumbing, then slab", "STATE or local, then LOCAL",
     "Under-slab drain, waste, and vent pressure-tested and inspected, then "
     "the slab inspected before the pour. Buy the plumbing permit long "
     "before this."),
    ("5. Rough electrical", "STATE or local",
     "Wiring complete and open. Book early: the three-working-day clock "
     "starts when the inspector receives your request."),
    ("6. Rough plumbing and gas piping", "STATE or local",
     "Often two separate permits and, in practice, two separate "
     "inspections. Fuel gas is its own code and its own application."),
    ("7. Rough mechanical / framing", "LOCAL",
     "Called only after the trade rough-ins pass — which means after the "
     "STATE inspections, on a schedule the local inspector does not "
     "control."),
    ("8. Insulation, air sealing, drywall", "LOCAL",
     "Against the adopted energy code; any blower-door or duct-leakage test "
     "lands here. Some jurisdictions also inspect drywall fastening before "
     "tape."),
    ("10. Trade finals", "STATE or local",
     "Electrical and plumbing/gas each final out and issue their own "
     "certificate of approval. The electrical final triggers the utility "
     "notice."),
    ("11. OWTS final", "PUBLIC HEALTH",
     "After installation, before the system is placed in use "
     "(25-10-106(1)(h))."),
    ("12. Building final / CO", "LOCAL",
     "Where a local building permit exists. Expect to hand over the trade "
     "certificates, the OWTS approval, and the address."),
]
rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in seq]
flow.append(k.ref_table(
    "Typical order — your permit card governs; authority varies by "
    "jurisdiction",
    [k.cellp("Inspection", bold=True), k.cellp("Whose", bold=True),
     k.cellp("What must be complete", bold=True)],
    rows, [1.85 * inch, 1.0 * inch, CW - 2.85 * inch]))
flow.append(Spacer(1, 6))

flow.append(k.callout("The sequencing trap this creates", [
    Paragraph("The rough electrical and rough plumbing rungs are usually the "
              "state's; framing is your local inspector's, and it cannot "
              "happen until they have passed. So framing sits behind a queue "
              "you do not control, at an office your building department has "
              "no relationship with. <b>Book the state rough inspections as "
              "early as the work allows</b>, get the certificates in hand, "
              "and bring copies to framing. Every week lost here is lost "
              "twice, because the trades cannot close up until framing "
              "passes.", S["body"]),
]))

# ---------------------------------------------------------------- what done means
flow += k.h2_tight("WHAT \"FINISHED\" MEANS WHERE YOU ARE BUILDING")
flow.append(k.body(
    "If your jurisdiction issues a certificate of occupancy, that is the "
    "finish line and it will want the trade certificates first. If it has no "
    "building code there is no CO, and the documents below are what a lender, "
    "insurer, or future buyer will ask for instead. Collect them either way."))
flow.append(k.checklist([
    "<b>Certificate of approval — electrical</b>, from the state or local "
    "inspector. On the electrical side this is also what evidences that the "
    "work was inspected, the condition your homeowner exemption depends on "
    "(12-115-116(2)).",
    "<b>Certificate of approval — plumbing, and gas piping if separate</b> — "
    "plus the <b>utility's final approval and permanent meter set</b>, which "
    "the board's notice to the utility releases (12-115-120(1)(b), (c)).",
    "<b>OWTS final inspection and any as-built</b> your public health agency "
    "requires — the system may not be used before it passes — and the "
    "<b>well permit, well construction report, and pump installation "
    "report</b> as filed with the Division of Water Resources.",
    "<b>The energy certificate posted in the house.</b> Under the 2021 IECC "
    "as adopted by Colorado jurisdictions, a permanent certificate of "
    "insulation R-values, window U-factors, and equipment efficiencies is "
    "completed by the builder and posted near the furnace or another "
    "approved interior location. As owner-builder, you are the builder.",
    "<b>Certificate of occupancy</b>, if your jurisdiction issues one.",
]))

# ---------------------------------------------------------------- logs
flow += k.h2_tight("INSPECTION LOG")
log_header = [k.cellp("Inspection", bold=True),
              k.cellp("Authority", bold=True),
              k.cellp("Called", bold=True),
              k.cellp("Held", bold=True),
              k.cellp("Result", bold=True),
              k.cellp("Corrections required / notes", bold=True)]
log_names = [
    "Footing / setback", "Foundation wall", "Underground plumbing / slab",
    "Rough electrical", "Rough plumbing / gas",
    "Rough mechanical / framing", "Insulation / air sealing / drywall",
    "Final — electrical", "Final — plumbing / gas", "OWTS final",
    "Final — building / CO", "",
]
log_rows = [[k.cellp(n) if n else "", "", "", "", "", ""] for n in log_names]
widths = [1.55 * inch, 0.92 * inch, 0.62 * inch, 0.62 * inch, 0.62 * inch]
widths.append(CW - sum(widths))
flow.append(d.titled_table(
    "Record every inspection as it happens — nobody else keeps this record",
    log_header, log_rows, widths, S,
    row_heights=[30] * len(log_rows)))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Electrical inspector:", 0.34),
                         ("Plumbing inspector:", 0.33),
                         ("Building inspector:", 0.33)]))
flow.append(d.FillInRow([("Utility released:", 0.34),
                         ("OWTS accepted:", 0.33),
                         ("CO issued:", 0.33)]))

flow.append(Spacer(1, 10))
flow.append(k.sources_table([
    ("State inspector must inspect within three working days of the "
     "application", "C.R.S. 12-115-120(2)(b); 12-155-120(1)(b)"),
    ("Certificate of approval issued on a passing inspection",
     "C.R.S. 12-115-120(3)(a); 12-155-120(2)(a)"),
    ("Written notice of disapproval with reasons; posted at the site; "
     "reinspection fee; appeal heard within seven days",
     "C.R.S. 12-115-120(3)(b), (4); 12-155-120(2)(b)"),
    ("Board notifies the utility; no service without proof of final "
     "approval", "C.R.S. 12-115-120(1)(b), (1)(c)"),
    ("OWTS final inspection before the system is placed in use",
     "C.R.S. 25-10-106(1)(h)"),
    ("Do not call the Division to schedule — contact your inspector; "
     "inspector lists and maps published; presence policy for occupied "
     "dwellings; remote video waiver",
     "DPO permits page,<br/>dpo.colorado.gov"),
    ("Engineered soils report and stamped foundation plans; published "
     "design criteria; multi-agency project approval routing",
     "Colorado building-department checklists (see CO.2)"),
    ("Permanent energy certificate posted at the furnace or approved "
     "interior location", "2021 IECC R401.3, as locally adopted"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "co-permit-kit",
                       "CO.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
