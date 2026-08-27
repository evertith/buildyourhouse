#!/usr/bin/env python3
"""MI.3 Inspection Sequence — Michigan.

Sources verified August 2026:
  MCL 125.1511(1)  permit granted or denied within 10 business days, 15 for an
                   unusually complicated building; failure = deemed DENIAL,
                   which is what opens the appeal
  MCL 125.1512(1)  enforcing agency shall periodically inspect
  MCL 125.1512(2)  deemed consent; 8 a.m.-6 p.m. business days; nobody else
                   may accompany the inspector without the owner's consent
  MCL 125.1512(3)  notice to show cause BEFORE a stop order; 1 full working day
  MCL 125.1513     certificate of USE AND OCCUPANCY; temporary certificate;
                   5 business days to issue after written application; 12
                   hours' notice of the final inspection
  R 408.30509      MI amendment of IRC R109.1.4 — framing is inspected AFTER
                   the plumbing, mechanical and electrical rough inspections
                   are APPROVED. This is the Michigan ordering trap.
  R 408.30509a     MI amendment of IRC R109.4 — correction notice must cite
                   chapter and section IN WRITING; nothing covered until
                   authorized
  R 408.30510      MI amendment of IRC R110.1/.2/.3 — the seven things the
                   certificate must contain, including the CODE EDITION
  R 408.30500      the MRC adopts the 2015 IRC and expressly EXCLUDES section
                   R109.1 — so the IRC's own list of required inspections is
                   not Michigan law; the Act and your permit card govern
  BCC-324 (04/2024) state practice: 2 business days to respond, 5 business
                   days to perform; the 180-day inspection closure clock

Note: because R109.1 is excluded, this kit does NOT present a statutory list
of required inspections. It presents the sequence as commonly called, flags
the one ordering rule Michigan does fix by rule, and says plainly that the
permit card governs.
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

FORM_ID = "MI.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The order Michigan inspections happen in, the one sequencing rule the "
    "State fixes by rule, the clocks that run in your favor, and a log to "
    "record every result as you go.")

flow.append(k.disclaimer(
    "Your permit card lists the inspections your job requires — it governs."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- who sets it
flow += k.h2_tight("WHY MICHIGAN HAS NO STATUTORY LIST OF INSPECTIONS")
flow.append(k.body(
    "Most states adopt the International Residential Code's section R109.1, "
    "which enumerates the inspections a house must have. <b>Michigan "
    "deliberately does not.</b> The rule that adopts the code lists the "
    "sections of the 2015 IRC that are <i>excluded</i> from the Michigan "
    "Residential Code, and <b>R109.1 is on that exclusion list</b> — along "
    "with the IRC's own permit, fee, appeal, violation and stop-work "
    "provisions, all of which the Stille-DeRossett-Hale Act supplies "
    "instead."))
flow.append(k.body(
    "The statute that replaces it is deliberately open: \"<i>An enforcing "
    "agency shall <b>periodically inspect</b> all construction undertaken "
    "pursuant to a building permit issued by it to insure that the "
    "construction is performed in accordance with conditions of the building "
    "permit.</i>\" Which inspections <i>your</i> job needs, and what they "
    "are called, comes from your enforcing agency and is printed on your "
    "permit card."))
flow.append(k.cite(
    "R 408.30500 (Part 5, Michigan Residential Code) adopts the 2015 IRC "
    "\"<i>except for Sections … R 109.1 …</i>\"; MCL 125.1512(1). Rules read "
    "at ars.apps.lara.state.mi.us, statutes at legislature.mi.gov, August "
    "2026."))

flow.append(k.callout(
    "The one ordering rule Michigan DOES fix — and it surprises people", [
        Paragraph("Michigan keeps IRC section R109.1.4 and rewrites it: "
                  "\"<i>Inspection of framing construction shall be made "
                  "after the roof, all framing, firestopping, draftstopping, "
                  "and bracing are in place <b>and after the plumbing, "
                  "mechanical, and electrical rough inspections are "
                  "approved</b>.</i>\"", S["body"]),
        Paragraph("That inverts what owner-builders usually expect. In "
                  "Michigan the <b>framing inspection comes last of the "
                  "four</b>, not first, and not bundled with them: the three "
                  "rough-ins must be not merely called but <b>approved</b> "
                  "first. Schedule framing early because the frame is what "
                  "is finished, and you fail on sequence alone.", S["body"]),
        Paragraph("This is where MI.4 comes back to bite: if your plumbing "
                  "permit is a state permit and your building permit a "
                  "county permit, your framing inspection is gated on an "
                  "approval from a different government.", S["body"]),
    ]))
flow.append(k.cite("R 408.30509, amending IRC § R109.1.4."))

# ---------------------------------------------------------------- the sequence
flow += k.h2_tight("THE SEQUENCE — WHAT MUST BE COMPLETE BEFORE YOU CALL")
flow.append(k.body(
    "The order below is the one Michigan enforcing agencies commonly call "
    "for a new house on a basement, arranged to respect the framing rule "
    "above. It is a working sequence, not a statutory list — confirm yours "
    "against your permit card at your first inspection, and write in "
    "anything your agency adds."))
seq = [
    ("1. Footing",
     "Trenches excavated to depth, forms and any reinforcing in place, before "
     "concrete. Remember Michigan's footing depth is <b>42 inches below "
     "actual grade</b>, and the building official may modify it for soil, "
     "groundwater, frost, snow or exposure.",
     "R403.1.4 as amended"),
    ("2. Foundation / damp-proofing",
     "After the walls are poured or laid and damp-proofing or waterproofing "
     "is applied — before backfill. Backfilling early is the most common way "
     "to lose this one.",
     "local"),
    ("3. Underground / under-slab",
     "Under-slab plumbing and any under-slab electrical, plus vapor "
     "retarder and fill, before the slab is poured.",
     "local"),
    ("4. Plumbing rough-in",
     "Water, waste and vent piping complete and under test. <b>Must be "
     "approved before framing.</b>",
     "R109.1.4"),
    ("5. Mechanical rough-in",
     "Ductwork, fuel gas piping, venting and equipment set. <b>Must be "
     "approved before framing.</b>",
     "R109.1.4"),
    ("6. Electrical rough-in",
     "Boxes, cable, panel and grounding electrode system in. <b>Must be "
     "approved before framing.</b> Note Michigan's own amendment: flexible "
     "metal conduit and liquid-tight flexible metal conduit are <b>not "
     "permitted as an equipment grounding conductor</b>.",
     "R109.1.4; E3908.8.1–.2"),
    ("7. Framing and masonry",
     "After the roof, all framing, firestopping, draftstopping and bracing "
     "are in place <i>and</i> the three rough-ins are approved. Masonry is "
     "inspected after base course flashing and the water-resistive barrier "
     "are installed and the masonry is complete.",
     "R109.1.4 as amended"),
    ("8. Insulation and vapor retarder",
     "After framing is approved, before any wall or ceiling covering. "
     "Michigan requires a Class I or II vapor retarder on the interior side "
     "of frame walls in zones 5, 6, 7 and 8, with stated exceptions.",
     "R601.3 as amended"),
    ("9. Finals — each trade",
     "Electrical, plumbing, mechanical and building each get their own "
     "final. The building final is the one that releases the certificate.",
     "MCL 125.1513"),
]
rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in seq]
flow.append(k.ref_table(
    "Working Michigan residential inspection sequence",
    [k.cellp("Inspection", bold=True),
     k.cellp("What must be complete / what is verified", bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.35 * inch, CW - 1.35 * inch - 1.25 * inch, 1.25 * inch]))
flow.append(k.cite(
    "Framing and masonry: R 408.30509 amending IRC § R109.1.4. Footing "
    "depth: R 408.30522 amending § R403.1.4 — \"<i>All exterior footings and "
    "foundation systems shall extend 42 inches below actual grade</i>,\" with "
    "an exception letting the building official modify the depth on evidence "
    "of freezing degree days, soil type, ground water, snow depth, exposure, "
    "or other identified conditions. Vapor retarders: R 408.30522a amending "
    "§ R601.3. Equipment grounding: R 408.30536 amending §§ E3908.8.1 and "
    "E3908.8.2. Certificate: MCL 125.1513. Steps without a citation are "
    "common practice, not law — confirm them locally."))

# ---------------------------------------------------------------- rights
flow += k.h2_tight("THE CLOCKS AND RIGHTS MICHIGAN GIVES YOU")
flow.append(k.body(
    "Michigan's construction code act is unusually generous with deadlines "
    "that run against the enforcing agency. Owner-builders almost never "
    "invoke them, mostly because they do not know they exist."))
flow.append(k.bullet(
    "<b>A decision on your permit in 10 business days</b> — 15 \"<i>in case "
    "of an unusually complicated building or structure</i>.\" And the "
    "remedy is the useful part: \"<i>Failure by an enforcing agency to "
    "grant, in whole or in part, or deny an application within these periods "
    "of time shall be <b>deemed a denial</b> of the application for purposes "
    "of authorizing the institution of an appeal to the appropriate board of "
    "appeals.</i>\" Silence is not limbo — it is a denial you can appeal. "
    "(MCL 125.1511(1))"))
flow.append(k.bullet(
    "<b>Inspections happen in working hours.</b> \"<i>An inspection shall be "
    "made between 8 a.m. and 6 p.m. on business days, or when construction "
    "is actually being undertaken</i>,\" except on probable cause of "
    "immediate danger or with your permission. (MCL 125.1512(2))"))
flow.append(k.bullet(
    "<b>Nobody tags along without your say-so.</b> \"<i>A person other than "
    "the owner, his agent, architect, engineer or builder shall not accompany "
    "an inspector … unless his presence is necessary for the enforcement of "
    "this act … or except with the consent of an owner.</i>\" "
    "(MCL 125.1512(2))"))
flow.append(k.bullet(
    "<b>A written correction notice that cites the code.</b> On a failure "
    "the building official must \"<i>notify the permit holder or agent … "
    "wherein portion of the construction fails to comply,</i>\" and \"<i>the "
    "notification shall include specific reference to the code chapter and "
    "section numbers in violation <b>in writing</b>.</i>\" You are entitled "
    "to know which section you failed, on paper. Ask for it every time. "
    "(R 408.30509a)"))
flow.append(k.bullet(
    "<b>A chance to be heard before a stop order.</b> The agency must first "
    "give written notice of the violation \"<i>and to appear and show cause "
    "why the construction should not be stopped</i>.\" Only if you fail to "
    "appear and show good cause <b>within 1 full working day</b> after the "
    "notice is delivered does the stop order get posted. (MCL 125.1512(3))"))
flow.append(k.bullet(
    "<b>12 hours' notice of your final inspection.</b> \"<i>The enforcing "
    "agency shall give the owner … at least 12 hours' notice of the time of "
    "any final inspection.</i>\" (MCL 125.1513)"))

flow.append(Spacer(1, 6))
flow.append(k.callout("What the State does NOT promise you", [
    Paragraph("There is <b>no statutory deadline</b> for an inspector to "
              "turn up after you request an inspection. Where the State is "
              "your enforcing agency it publishes a practice — \"<i>the "
              "inspector will respond to an inspection request within two "
              "(2) business days to schedule the inspection. Inspections are "
              "typically performed within five (5) business days subject to "
              "the inspection schedule</i>\" — but that is a service "
              "standard on the State's own form, not a right, and it does "
              "not bind a county or local agency at all. Ask yours what to "
              "expect and write it into MI.4.", S["body"]),
]))

# ---------------------------------------------------------------- expiry
flow += k.h2_tight("THE 180-DAY CLOCK RUNS ON INSPECTIONS, NOT ON EFFORT")
flow.append(k.body(
    "A permit \"<i>remains valid as long as work is progressing, and "
    "inspections are requested and conducted</i>,\" and becomes invalid if "
    "work is not commenced within 180 days of issuance or is suspended or "
    "abandoned for 180 days. Then the sentence the State prints in capitals: "
    "\"<i>A PERMIT WILL BE CLOSED WHEN NO INSPECTIONS ARE REQUESTED AND "
    "CONDUCTED WITHIN 180 DAYS OF THE DATE OF ISSUANCE OR THE DATE OF A "
    "PREVIOUS INSPECTION.</i>\""))
flow.append(k.body(
    "For a Michigan owner-builder this is the single most likely "
    "administrative failure, because the shape of a Michigan build season "
    "produces exactly the gap the rule punishes: an autumn inspection, a "
    "winter of interior work nobody inspects, and a spring phone call "
    "explaining that the permit closed in February. <b>If a long gap is "
    "coming, call an inspection you can pass before it starts.</b> Where the "
    "State issued the permit, re-opening costs $75.00 and closed permits are "
    "not refundable."))
flow.append(k.cite(
    "Bureau of Construction Codes Building Permit Application, form BCC-324 "
    "(04/2024), page 3, \"Expiration of Permit\"; BCC Fee Schedule effective "
    "April 1, 2024. A local enforcing agency sets its own expiry practice — "
    "ask, and write it down."))

# ---------------------------------------------------------------- certificate
flow += k.h2_tight("THE CERTIFICATE AT THE END")
flow.append(k.body(
    "Michigan's statutory name is the <b>certificate of use and "
    "occupancy</b>. \"<i>A building or structure hereafter constructed shall "
    "not be used or occupied in whole or in part until a certificate of use "
    "and occupancy has been issued by the appropriate enforcing agency.</i>\" "
    "Once you are entitled to it, the agency \"<i>shall issue a certificate "
    "of use and occupancy <b>within 5 business days</b> after receipt of a "
    "written application therefor</i>\" and payment of its fee — so put the "
    "application in writing, and date your copy."))
flow.append(k.body(
    "A <b>temporary</b> certificate may be issued on request for part of the "
    "building before all the work is finished, if that part can be occupied "
    "safely. Michigan's code rule also fixes what the certificate must say: "
    "the permit number, the address, the portion covered, a statement that "
    "it was inspected for compliance, the building official's name, any "
    "special stipulations — and <b>the edition of the code under which the "
    "permit was issued</b>. That last item is worth keeping: given how "
    "Michigan's residential code edition has moved, your certificate is the "
    "record of which one your house was built to."))
flow.append(k.cite("MCL 125.1513; R 408.30510 amending §§ R110.1–R110.3."))

# ---------------------------------------------------------------- the log
flow += k.h2_tight("INSPECTION LOG — RECORD EVERY ONE")
flow.append(k.body(
    "Fill this in as it happens, not from memory. Note <b>which agency</b> "
    "each inspection came from — in Michigan that is genuinely not always "
    "the same one. If a result is ever disputed, or a later inspector "
    "questions earlier work, this page and your photographs are the record "
    "you have."))

log_header = [k.cellp("Inspection", bold=True),
              k.cellp("Agency", bold=True),
              k.cellp("Called", bold=True),
              k.cellp("Held", bold=True),
              k.cellp("Result", bold=True),
              k.cellp("Corrections required / notes", bold=True)]
log_names = [
    "Footing", "Foundation / damp-proof", "Under-slab", "Plumbing rough",
    "Mechanical rough", "Electrical rough", "Framing / masonry",
    "Insulation / vapor retarder", "Final — electrical", "Final — plumbing",
    "Final — mechanical", "Final — building",
    "",
]
log_rows = [[k.cellp(n) if n else "", "", "", "", "", ""] for n in log_names]
# "Result" must not wrap: 0.6in clipped it to "Resul / t" at 9.5pt bold.
widths = [1.22 * inch, 0.70 * inch, 0.64 * inch, 0.60 * inch, 0.76 * inch]
widths.append(CW - sum(widths))
flow.append(d.titled_table(
    "Inspection log", log_header, log_rows, widths, S,
    row_heights=[30] * len(log_rows)))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Certificate of use and occupancy issued:", 0.55),
                         ("Number:", 0.45)]))

flow.append(Spacer(1, 8))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026; statutes at legislature.mi.gov, "
    "rules at ars.apps.lara.state.mi.us). Permit decision in 10 or 15 "
    "business days, and deemed denial — MCL 125.1511(1). Periodic "
    "inspection, deemed consent, the 8 a.m.–6 p.m. window, and who may "
    "accompany an inspector — MCL 125.1512(1), (2). Show-cause notice before "
    "a stop order — MCL 125.1512(3). Certificate of use and occupancy, "
    "temporary certificate, 5 business days to issue, 12 hours' notice of "
    "the final — MCL 125.1513. Framing after approved rough-ins — "
    "R 408.30509. Written correction notice citing chapter and section — "
    "R 408.30509a. Certificate contents — R 408.30510. The 2015 IRC adopted "
    "excluding § R109.1 — R 408.30500."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "mi-permit-kit",
                       "MI.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
