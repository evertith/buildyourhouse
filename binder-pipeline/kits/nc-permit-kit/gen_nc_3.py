#!/usr/bin/env python3
"""NC.3 Inspection Sequence — NC.

Sources verified August 2026:
  G.S. 160D-1113  inspections of work in progress; owner-builder must be present
  G.S. 160D-1112  changes require written approval before they are built
  G.S. 160D-1114  stop order appeal to the State Fire Marshal within five days
  G.S. 160D-1116  final inspection, certificate of compliance, TCO, penalty
  G.S. 160D-1104  inspector duties and the applicant protections in (b)–(e)
  2018 NC Administrative Code and Policies § 107 — the eight enumerated
    inspections, 107.1.1 through 107.1.8, to which NC Residential Code § R109
    defers. An earlier edition numbered framing and rough-in in the opposite
    order; the descriptive text is stable, only those two numbers swapped.
  Code edition currently in effect: 2018 (ncosfm.gov, Codes Current and Past).

Note: there is NO numeric statutory deadline for an inspector to respond to a
request — G.S. 160D-1104(b) says only "in a timely manner." The 15-business-day
clock that people misremember applies to residential PLAN REVIEW under
G.S. 160D-1110(b), and lives in NC.2.
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

FORM_ID = "NC.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The order North Carolina inspections happen in, what each inspector is "
    "actually looking at, and a log to record every result as you go.")

flow.append(k.disclaimer(
    "Your permit card lists the inspections your job requires — it governs."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- who sets it
flow += k.h2_tight("WHAT THE STATE SETS AND WHAT YOUR COUNTY SETS")
flow.append(k.body(
    "The <b>definitions</b> below are statewide. They come from Section 107 "
    "of the North Carolina Administrative Code and Policies, part of the "
    "State Building Code, and they say what condition the work must be in "
    "before each inspection can be called. The <b>list of inspections your "
    "particular job needs</b>, and the order your department calls them in, "
    "is local — it is printed on your permit card. Where the two differ, "
    "your permit card and your inspector govern."))
flow.append(k.body(
    "The statute itself does not enumerate inspections. G.S. 160D-1113 "
    "simply directs local inspectors to \"<i>make as many inspections "
    "thereof as may be necessary to satisfy them that the work is being done "
    "according to the provisions of any applicable State and local laws and "
    "of the terms of the permit</i>.\" That is why counties vary in how they "
    "bundle framing with rough-in, or insulation with framing."))

flow.append(k.callout(
    "You must be there — every time", [
        Paragraph("\"<i>If a building permit has been obtained by an owner "
                  "exempt from licensure under G.S. 87-1(b)(2), no inspection "
                  "shall be conducted without the owner being present, unless "
                  "the plans for the building were drawn and sealed by an "
                  "architect licensed pursuant to Chapter 83A.</i>\" "
                  "(G.S. 160D-1113)", S["body"]),
        Paragraph("This is a command on the inspector, not a suggestion to "
                  "you. Note it says <b>architect</b> — not engineer. Plan "
                  "your work weeks around it.", S["body"]),
    ]))
flow.append(k.cite(
    "N.C.G.S. § 160D-1113; 2018 North Carolina Administrative Code and "
    "Policies § 107. The 2018 edition of the State Building Code is the "
    "edition in effect (NC Office of State Fire Marshal, Codes — Current and "
    "Past, verified August 2026). The 2024 edition has been adopted but its "
    "effective date remains deferred; it may be used as an alternative method "
    "on request. Confirm the edition your county is enforcing before you "
    "submit plans."))

# ---------------------------------------------------------------- the sequence
flow += k.h2_tight("THE SEQUENCE — WHAT MUST BE COMPLETE BEFORE YOU CALL")
seq = [
    ("1. Footing",
     "Trenches excavated, all grade stakes installed, all reinforcing steel "
     "and supports in place and tied, and all necessary forms and bulkheads "
     "in place and braced — <b>before any concrete is placed</b>.",
     "§ 107.1.1"),
    ("2. Under-slab",
     "After all materials and equipment that the concrete slab will conceal "
     "are complete — under-slab plumbing, electrical, vapor barrier, fill. "
     "Certain unheated garage slabs, sidewalks and driveways are excepted for "
     "one- and two-family dwellings.",
     "§ 107.1.2"),
    ("3. Foundation / crawl space",
     "After all foundation supports are installed. In a crawl space this is "
     "where piers, girders, sill anchorage, and grade clearances are looked "
     "at.",
     "§ 107.1.3"),
    ("4. Building framing",
     "After roof framing (excluding permanent roof coverings), wall, ceiling "
     "and floor framing is complete with appropriate blocking, bracing and "
     "firestopping in place. Pipes, chimneys and vents, roof and chimney "
     "flashing, insulation baffles, and any lintels bolted to the framing "
     "must be visible.",
     "§ 107.1.4"),
    ("5. Rough-in (electrical, plumbing, mechanical)",
     "When all building framing and every part of the electrical, plumbing, "
     "fire protection or heating-ventilation-cooling system that will be "
     "hidden from view has been placed — but <b>before any wall or ceiling "
     "finish or any insulation</b> is installed. Many NC counties call "
     "framing and rough-in together; some call each trade separately.",
     "§ 107.1.5"),
    ("6. Insulation",
     "After an approved framing and rough-in inspection, and after the "
     "permanent roof covering is installed, with all insulation and vapor "
     "retarders in place — before any wall or ceiling covering is applied.",
     "§ 107.1.6"),
    ("7. Fire protection",
     "Wherever material is used for fire protection purposes. You must notify "
     "the department once the material is in place; it may not be concealed "
     "until inspected and approved.",
     "§ 107.1.7"),
    ("8. Final — each trade",
     "After completion of the work authorized under each technical code. "
     "Building, electrical, plumbing and mechanical each get their own final. "
     "The building final is the one that releases the certificate.",
     "§ 107.1.8"),
]
rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in seq]
flow.append(k.ref_table(
    "Standard North Carolina residential inspection sequence",
    [k.cellp("Inspection", bold=True),
     k.cellp("What must be complete / what is verified", bold=True),
     k.cellp("Code", bold=True)],
    rows, [1.55 * inch, CW - 1.55 * inch - 1.0 * inch, 1.0 * inch]))
flow.append(k.cite(
    "Definitions quoted from the 2018 North Carolina Administrative Code and "
    "Policies § 107 (Inspections), whose § 107.1 directs that \"<i>the "
    "inspection department shall perform the following inspections</i>\" and "
    "then names these eight. The NC Residential Code's own § R109 simply "
    "points there. Note that an earlier edition numbered framing and "
    "rough-in in the opposite order — the descriptive text is stable, the "
    "two subsection numbers swapped. Verified August 2026."))

flow += k.h2_tight("WHAT AN INSPECTOR MAY AND MAY NOT DO")
flow.append(k.body(
    "G.S. 160D-1104 gives you more leverage than most owner-builders "
    "realise. Worth knowing before your first difficult inspection:"))
flow.append(k.bullet(
    "The inspector \"<i>shall conduct all inspections requested by the "
    "permit holder for each scheduled inspection</i>,\" and must tell you "
    "where the work fails. They are <b>prohibited from requiring "
    "affidavits</b> attesting to compliance in lieu of actually inspecting "
    "Residential Code work. (§ 160D-1104(c))"))
flow.append(k.bullet(
    "On a re-inspection, new violations found on items <b>already "
    "approved</b> may not delay a temporary CO, and <b>no re-inspection fee "
    "may be charged</b> for those items. (§ 160D-1104(d))"))
flow.append(k.bullet(
    "Cancel more than one business day ahead and they may not charge you a "
    "fee or fail the inspection. (§ 160D-1104(d2))"))
flow.append(k.bullet(
    "Every department must run an <b>informal internal review</b> of "
    "inspection decisions, starting with the inspector's supervisor — whose "
    "name, phone and email must be provided with your permit. Use it before "
    "you escalate. (§ 160D-1104(e))"))
flow.append(k.bullet(
    "Counties cannot invent extra <b>routine</b> inspections beyond the "
    "State Building Code list without Residential Code Council approval — "
    "though they may still inspect for unforeseen or unique circumstances. "
    "(§ 160D-1104(d))"))
flow.append(k.cite(
    "One thing the statutes do <b>not</b> give you: a deadline. There is no "
    "numeric statutory turnaround for an inspection request — G.S. "
    "160D-1104(b) requires only \"<i>the making of any necessary inspections "
    "in a timely manner</i>.\" Any 24- or 48-hour figure you have heard is "
    "local practice. The hard clock in North Carolina law applies to "
    "residential <i>plan review</i>, not inspections (§ 160D-1110(b)) — see "
    "NC.2."))

# ---------------------------------------------------------------- certificate
flow += k.h2_tight("THE CERTIFICATE AT THE END")
flow.append(k.body(
    "\"<i>At the conclusion of all work done under a building permit, the "
    "appropriate inspector shall make a final inspection, and, if the "
    "completed work complies with all applicable State and local laws and "
    "with the terms of the permit, the inspector shall issue a certificate "
    "of compliance.</i>\" North Carolina's statutory name is <b>certificate "
    "of compliance</b>; most counties and every lender will call it the "
    "certificate of occupancy."))
flow.append(k.body(
    "A <b>temporary certificate of occupancy</b> may be issued for a stated "
    "period if the inspector finds the building may safely be occupied before "
    "final completion. Moving in before either one issues is a <b>Class 1 "
    "misdemeanor</b> — the most serious penalty named anywhere in this kit."))
flow.append(k.cite("N.C.G.S. § 160D-1116(a), (b), (c)."))

# ---------------------------------------------------------------- when it goes wrong
flow += k.h2_tight("WHEN AN INSPECTION GOES WRONG")
wrong = [
    [k.cellp("<b>You failed</b>"),
     k.cellp("Get the written correction notice, fix exactly what it names, "
             "and re-call. Re-inspection fees and how soon you may re-call "
             "are local — ask at your first inspection so it is not a "
             "surprise at your third."),
     k.cellp("local")],
    [k.cellp("<b>You need to change something</b>"),
     k.cellp("Get written approval <i>before</i> you build it. No change or "
             "deviation from the approved application, plans or permit may be "
             "made until the inspection department specifically approves it "
             "in writing, unless the Code clearly permits it."),
     k.cellp("§ 160D-1112")],
    [k.cellp("<b>You got a stop order</b>"),
     k.cellp("You may appeal a stop order alleging a Building Code violation "
             "to the State Fire Marshal <b>within five days</b>, in writing, "
             "copying the local inspector. No further work may proceed in "
             "violation of the order while the appeal is pending."),
     k.cellp("§ 160D-1114")],
    [k.cellp("<b>Your permit went stale</b>"),
     k.cellp("A permit expires six months after issuance if work has not "
             "commenced, and expires immediately if work is discontinued for "
             "12 months after commencement. Local ordinance may set a shorter "
             "commencement window."),
     k.cellp("§ 160D-1111")],
]
flow.append(k.ref_table(
    "Failures, changes, stop orders, and expiry",
    [k.cellp("Situation", bold=True), k.cellp("What to do", bold=True),
     k.cellp("Authority", bold=True)],
    wrong, [1.45 * inch, CW - 1.45 * inch - 1.2 * inch, 1.2 * inch]))
flow.append(k.cite(
    "Guides that say a North Carolina permit \"is valid for 18 months\" are "
    "describing a local practice, not the statute — § 160D-1111 sets six "
    "months to commence and 12 months of inactivity thereafter."))

# ---------------------------------------------------------------- the log
flow += k.h2_tight("INSPECTION LOG — RECORD EVERY ONE")
flow.append(k.body(
    "Fill this in as it happens, not from memory. If a result is ever "
    "disputed, or a later inspector questions earlier work, this page and "
    "your photos are the record you have."))

log_header = [k.cellp("Inspection", bold=True),
              k.cellp("Called", bold=True),
              k.cellp("Held", bold=True),
              k.cellp("Result", bold=True),
              k.cellp("Inspector", bold=True),
              k.cellp("Corrections required / notes", bold=True)]
log_names = [
    "Footing", "Under-slab", "Foundation / crawl", "Framing",
    "Electrical rough-in", "Plumbing rough-in", "Mechanical rough-in",
    "Insulation", "Fire protection", "Final — electrical",
    "Final — plumbing", "Final — mechanical", "Final — building",
    "", "", "",
]
log_rows = [[k.cellp(n) if n else "", "", "", "", "", ""] for n in log_names]
widths = [1.25 * inch, 0.72 * inch, 0.72 * inch, 0.62 * inch, 1.05 * inch]
widths.append(CW - sum(widths))
flow.append(d.titled_table(
    "Inspection log", log_header, log_rows, widths, S,
    row_heights=[30] * len(log_rows)))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Certificate of compliance issued:", 0.55),
                         ("Number:", 0.45)]))

flow.append(Spacer(1, 8))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026, General Statutes at ncleg.gov). "
    "Inspections of work in progress, and the owner-present rule with its "
    "architect-sealed exception — § 160D-1113. Inspector duties and "
    "applicant protections: all requested inspections conducted and no "
    "affidavits in lieu — § 160D-1104(c); no re-inspection fee or TCO delay "
    "for newly-noted items already approved, and the limit on locally-added "
    "routine inspections — § 160D-1104(d); no fee if cancelled over one "
    "business day ahead — § 160D-1104(d2); informal internal review — "
    "§ 160D-1104(e); \"timely manner\" and no numeric deadline — "
    "§ 160D-1104(b). Changes need written approval — § 160D-1112. Stop-order "
    "appeal within five days — § 160D-1114. Permit expiry — § 160D-1111. "
    "Final inspection, certificate of compliance, temporary CO and the "
    "Class 1 occupancy penalty — § 160D-1116. The eight required inspections "
    "and their definitions — 2018 NC Administrative Code and Policies "
    "§ 107.1.1–.1.8, to which NC Residential Code § R109 defers. The 2018 "
    "State Building Code is the edition in effect — ncosfm.gov, Codes "
    "Current and Past."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "nc-permit-kit",
                       "NC.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
