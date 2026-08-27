#!/usr/bin/env python3
"""KY.3 Inspection Sequence.

Kentucky has no single statutory list of residential inspections, and for a
structural reason rather than an accidental one: the building inspections may
not exist at all on your parcel, while the three trade approvals always do. The
sequence printed here is therefore split into "the ones that always happen" and
"the ones that happen only if your jurisdiction requires them," and every step
without a citation is flagged as common practice rather than law.

Verified sources:
  KRS 198B.6672(3)   HVAC inspection: scheduled at least ONE business day in
                     advance and completed within THREE business days
  KRS 198B.6677      inspector shall refuse approval; right to a KRS 13B hearing
  KRS 198B.062       approved construction documents are mandatory and an
                     on-site inspector may not order changes contrary to them
  KRS 198B.070(3)    local appeals board: hearing within 15 days, 10 days'
                     notice by certified mail, decision within 5 working days
  KRS 198B.060(9)    applying for a permit is deemed consent to inspection
  KRS 198B.060(11)   the electrical final certificate of approval and permanent
                     electric service
  KRS 198B.060(13)   no certificate of occupancy required for a single-family
                     dwelling absent a local program
  KRS 198B.130       attorney's fees added if no certificate of occupancy
  KRS 318.165        no permanent water supply until the plumbing is approved
  815 KAR 20:050 §5  five plumbing inspections included in the permit fee
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

FORM_ID = "KY.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The order inspections happen in, which ones happen no matter where you "
    "build, and the clocks Kentucky law runs against the inspector.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- why
flow += k.h2_tight("WHY KENTUCKY HAS NO SINGLE LIST OF INSPECTIONS")
flow.append(k.body(
    "In most states you can print one inspection sequence and it will be "
    "broadly right everywhere. In Kentucky you cannot, because the building "
    "inspections and the trade inspections come from different places and only "
    "one set is guaranteed."))
flow.append(k.body(
    "<b>The trade inspections always happen.</b> Plumbing, HVAC and electrical "
    "are governed by statewide instruments that do not care whether your "
    "county has a building ordinance. <b>The building inspections happen only "
    "if your jurisdiction requires them</b> — and in roughly a third of "
    "Kentucky counties there is no local building inspector on the state's own "
    "list at all. Work out which column you are in before you plan the "
    "schedule."))

# ---------------------------------------------------------------- always
flow += k.h2_tight("THE APPROVALS THAT HAPPEN WHEREVER YOU BUILD")
always = [
    ("Plumbing — underground / rough",
     "Under-slab and in-wall water, waste and vent piping, under test, before "
     "it is covered. Your permit includes <b>five inspections at no additional "
     "cost</b>, so use them rather than saving them.",
     "815 KAR 20:050 §5(1)"),
    ("Plumbing — final",
     "Fixtures set and the system complete. This is the approval a water "
     "utility or water district needs before it may give you <b>permanent "
     "water</b>.",
     "KRS 318.165"),
    ("HVAC — installation",
     "The initial heating, ventilation or air conditioning system. The "
     "inspection \"<i>shall be scheduled with the property owner … at least "
     "one (1) business day in advance and shall be completed within three (3) "
     "business days of the scheduled inspection.</i>\"",
     "KRS 198B.6672(3)"),
    ("Electrical — rough and final",
     "Arranged through the certified electrical inspector for your county. "
     "The <b>final certificate of approval</b> is the document your power "
     "company needs before it may connect <b>permanent electric service</b>.",
     "KRS 198B.060(11)"),
]
rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in always]
flow.append(k.ref_table(
    "Always required — whatever your county does about building permits",
    [k.cellp("Inspection", bold=True),
     k.cellp("What it covers", bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - 1.35 * inch, 1.35 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout("The two signatures the whole schedule hangs on", [
    Paragraph("Whatever else happens, your house does not become habitable "
              "until two people sign. A <b>certified electrical inspector</b> "
              "issues the final certificate of approval — and \"<i>after a "
              "certified electrical inspector has been provided for by the "
              "local government or the department, no utility shall initiate "
              "permanent electrical service to any new building</i>\" without "
              "it. (That opening condition is met in practice: all 119 "
              "published county sheets name a state electrical inspector.) And "
              "the plumbing is inspected and approved, without which \"<i>no "
              "permanent water supply shall be provided to any building by any "
              "public utility or water district</i>.\"", S["body"]),
    Paragraph("On a septic site there is a step in front of the electrical "
              "one. A certified electrical inspector may not issue a "
              "certificate for temporary or permanent wiring without a "
              "<b>notice of release</b> from the local health department — the "
              "initial release on your septic site-evaluation application, the "
              "final release on approval of the sewage disposal plan. So the "
              "health department gates your construction power too, unless "
              "your county has adopted the Uniform State Building Code and "
              "enforces on-site sewage permitting. (KRS 211.350(8))",
              S["body"]),
    Paragraph("Sequence the build around those two. Temporary construction "
              "power is expressly not blocked — \"<i>nothing in this section "
              "shall prohibit the supply or use of necessary electrical "
              "services during the construction and testing process</i>\" — so "
              "arrange it early and separately. (KRS 198B.060(11); "
              "KRS 318.165)", S["body"]),
]))

# ---------------------------------------------------------------- maybe
flow += k.h2_tight("THE BUILDING INSPECTIONS — IF YOUR JURISDICTION REQUIRES THEM")
flow.append(k.body(
    "Where a local ordinance applies, the sequence below is the one Kentucky "
    "building departments commonly call for a new house. It is a <b>working "
    "sequence, not a statutory list</b> — Kentucky does not fix one in "
    "statute for single-family dwellings. Confirm yours against your permit "
    "card at the first inspection and write in anything your jurisdiction "
    "adds."))
seq = [
    ("1. Footing", "Trenches excavated to depth, forms and reinforcing in "
     "place, before concrete."),
    ("2. Foundation / waterproofing", "After the walls are poured or laid and "
     "damp-proofing is applied — before backfill. Backfilling early is the "
     "commonest way to lose this one."),
    ("3. Under-slab", "Under-slab plumbing and any under-slab electrical, "
     "plus the vapor retarder and fill, before the slab is poured."),
    ("4. Rough-ins", "Plumbing, electrical and HVAC rough-in. In Kentucky "
     "these are frequently <b>different inspectors from different "
     "governments</b> than the building inspector — book them separately and "
     "early."),
    ("5. Framing", "After the roof is on and all framing, firestopping and "
     "bracing are in place. Most jurisdictions want the rough-ins approved "
     "first; ask yours whether it is a requirement or a preference."),
    ("6. Insulation", "After framing is approved and before any wall or "
     "ceiling covering, to the 2009 IECC as adopted."),
    ("7. Finals", "Each trade takes its own final. The building final is the "
     "one that releases the certificate of occupancy where one is issued."),
]
rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b)] for a, b in seq]
flow.append(k.ref_table(
    "Working residential sequence where a local ordinance applies",
    [k.cellp("Inspection", bold=True),
     k.cellp("What must be complete", bold=True)],
    rows, [1.75 * inch, CW - 1.75 * inch]))
flow.append(k.cite(
    "Steps above carry no citation because Kentucky prescribes no statutory "
    "inspection sequence for a single-family dwelling — these are common "
    "practice, and your jurisdiction's card governs. Energy provisions: 2009 "
    "IECC for residential buildings, per the Department's currently-adopted "
    "code list."))

# ---------------------------------------------------------------- rights
flow += k.h2_tight("THE CLOCKS AND RIGHTS KENTUCKY GIVES YOU")
flow.append(k.body(
    "Kentucky hands owner-builders several genuine rights that almost nobody "
    "invokes, mostly because they are scattered across three chapters."))
flow.append(k.bullet(
    "<b>Your HVAC inspection runs on a statutory clock.</b> It \"<i>shall be "
    "scheduled with the property owner or owners or their agent or agents "
    "<b>at least one (1) business day in advance</b> and shall be <b>completed "
    "within three (3) business days</b> of the scheduled inspection</i>.\" "
    "This is the only hard inspection deadline in the Kentucky residential "
    "scheme — hold them to it. (KRS 198B.6672(3))"))
flow.append(k.bullet(
    "<b>Five plumbing inspections are already paid for.</b> \"<i>A person with "
    "a plumbing permit shall be entitled to five (5) plumbing inspections at "
    "no additional cost.</i>\" Additional ones are $50 each — unless your "
    "permit cost more than $250, in which case they are free too. "
    "(815 KAR 20:050 §5)"))
flow.append(k.bullet(
    "<b>An inspector may not overrule your approved drawings.</b> \"<i>All "
    "buildings shall be constructed according to the construction documents "
    "approved by the building official … <b>No on-site inspector shall order "
    "changes in the construction of a building which are contrary to the "
    "approved construction documents.</b></i>\" If an inspector disagrees with "
    "the approved plans, the statute tells them to refer it back to the "
    "building official — not to direct you on site. (KRS 198B.062)"))
flow.append(k.bullet(
    "<b>A fast appeal, with dates attached.</b> Where a local appeals board "
    "exists it must convene a hearing \"<i>within fifteen (15) days of "
    "receipt</i>\" of your appeal, notify all parties by certified mail "
    "\"<i>no later than ten (10) days prior</i>,\" and \"<i>render a decision "
    "within five (5) working days after the hearing</i>.\" Its decision can "
    "then be appealed to the Department. (KRS 198B.070(3), (4))"))
flow.append(k.bullet(
    "<b>An HVAC refusal is appealable too</b> — an applicant aggrieved by an "
    "action of an inspector or the Department \"<i>may request a hearing in "
    "accordance with KRS Chapter 13B</i>.\" (KRS 198B.6677(2))"))

flow.append(Spacer(1, 6))
flow.append(k.callout("What Kentucky does NOT promise you", [
    Paragraph("There is <b>no statutory deadline</b> for a building, plumbing "
              "or electrical inspector to attend after you request an "
              "inspection — the three-business-day rule reaches HVAC only. "
              "There is no statutory permit-decision clock for a single-family "
              "dwelling either. Ask each office what to expect, write it into "
              "KY.4, and book further ahead than feels necessary.", S["body"]),
    Paragraph("And note what applying costs you: an applicant \"<i>by the act "
              "of applying for the permit, shall be deemed to have consented "
              "to inspection … during construction and upon the completion of "
              "construction</i>.\" Refusing an inspection has consequences of "
              "its own — for HVAC the inspector \"<i>shall refuse to approve "
              "the work</i>\" and continued use of the system can be "
              "prohibited outright. (KRS 198B.060(9); KRS 198B.6677(1))",
              S["body"]),
]))

# ---------------------------------------------------------------- CO
flow += k.h2_tight("THE CERTIFICATE AT THE END — OPTIONAL, AND WORTH HAVING")
flow.append(k.body(
    "Where a local government has established jurisdiction, no building may be "
    "occupied until the building official issues a <b>certificate of "
    "occupancy</b>. Where it has not, nothing \"<i>shall be construed to "
    "require a certificate of occupancy to be issued for any single-family "
    "dwelling</i>.\" So for much of Kentucky the certificate is genuinely "
    "optional."))
flow.append(k.body(
    "<b>Get one anyway if you can.</b> Kentucky attaches a specific financial "
    "consequence to not having one. Anyone damaged by a violation of the code "
    "may sue whoever committed it — within one year of discovering the damage, "
    "and in no event more than ten years after first occupation or the "
    "settlement date. The award may include damages and the cost of "
    "litigation, and \"<i><b>if a certificate of occupancy was not issued, "
    "then an award may also include reasonable attorney's fees</b></i>.\" A "
    "certificate you were never required to obtain is the cheapest liability "
    "insurance available to a Kentucky owner-builder."))
flow.append(k.body(
    "If your jurisdiction issues one, note that any approved change to the "
    "construction \"<i>shall be recorded with the construction documents "
    "before the certificate of occupancy shall be issued</i>\" — so keep your "
    "change records with the plan set rather than loose."))
flow.append(k.cite("KRS 198B.060(13); KRS 198B.130(1), (2); KRS 198B.062."))

# ---------------------------------------------------------------- the log
flow += k.h2_tight("INSPECTION LOG — RECORD EVERY ONE")
flow.append(k.body(
    "Fill this in as it happens, not from memory, and note <b>which office</b> "
    "each inspection came from — in Kentucky that is genuinely not the same "
    "one each time. If no building inspector ever attends your site, this page "
    "and your photographs are the only record that the work was done to code. "
    "Take the photographs regardless."))

log_header = [k.cellp("Inspection", bold=True),
              k.cellp("Office", bold=True),
              k.cellp("Called", bold=True),
              k.cellp("Held", bold=True),
              k.cellp("Result", bold=True),
              k.cellp("Corrections required / notes", bold=True)]
log_names = [
    "Footing", "Foundation", "Under-slab", "Plumbing rough",
    "Electrical rough", "HVAC installation", "Framing", "Insulation",
    "Plumbing final", "Electrical final certificate", "HVAC final",
    "Building final", "",
]
log_rows = [[k.cellp(n) if n else "", "", "", "", "", ""] for n in log_names]
# "Result" must not wrap: 0.6in clipped it to "Resul / t" at 9.5pt bold.
widths = [1.30 * inch, 0.66 * inch, 0.64 * inch, 0.60 * inch, 0.76 * inch]
widths.append(CW - sum(widths))
flow.append(d.titled_table(
    "Inspection log", log_header, log_rows, widths, S,
    row_heights=[30] * len(log_rows)))

flow.append(Spacer(1, 8))
flow += k.pack_fields([("Electrical final certificate of approval issued:", 0),
                       ("Permanent power set:", 0)], CW)
flow += k.pack_fields([("Plumbing final approved:", 0),
                       ("Permanent water set:", 0)], CW)
flow += k.pack_fields([("Certificate of occupancy issued (or N/A):", 0),
                       ("Number:", 0)], CW)

flow.append(Spacer(1, 8))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026; statutes and regulations at "
    "apps.legislature.ky.gov). HVAC inspection scheduling and completion — "
    "KRS 198B.6672(3). Refusal to approve, and the right to a hearing — "
    "KRS 198B.6677. Deemed consent to inspection — KRS 198B.060(9). Permanent "
    "electric service and the certified electrical inspector — "
    "KRS 198B.060(11). Permanent water supply — KRS 318.165. Five plumbing "
    "inspections included — 815 KAR 20:050 Section 5(1). Approved construction "
    "documents and on-site inspectors — KRS 198B.062. Appeal clocks — "
    "KRS 198B.070(3), (4). Certificate of occupancy not required for a "
    "single-family dwelling absent a local program — KRS 198B.060(13). Private "
    "action and attorney's fees — KRS 198B.130. Steps without a citation are "
    "common practice, not law — confirm them locally."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ky-permit-kit",
                       "KY.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
