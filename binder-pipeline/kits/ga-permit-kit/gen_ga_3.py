#!/usr/bin/env python3
"""GA.3 Inspection Sequence — Georgia.

Sources verified August 2026:
  2026 Georgia Amendments to the 2024 IRC — Chapter 1 "Scope and
    Administration" deleted without substitution; kept in the code only as a
    reference and guide for local governments' own administrative procedures.
    That is why Georgia has no statewide inspection list.
  O.C.G.A. § 8-2-26(a)(4)  permits and inspections are a local-option power
  O.C.G.A. § 8-2-25(a)     the eight mandatory codes bind statewide regardless
  O.C.G.A. § 43-41-17(h)   owner-builder work must conform to the codes and
                           any local permitting/inspection requirements
  O.C.G.A. § 8-2-26(g)     private professional providers (verified in
                           substance)
  GA IECC R402.4.1.2       signed DET blower-door report "provided to the
                           code official"; R403.3.3 duct test at rough-in or
                           post-construction
  DPH Rule 511-3-1-.03(4)  no backfill or use of a septic system before the
                           county's final inspection and written approval;
                           (4)(b) later site changes void the approval

Still deliberately hedged: the inspection ladder is a MODEL (IRC R109 as
guide + universal Georgia practice), printed with blanks for the county's
actual required-inspection list, because Chapter 1 is deleted and no
statewide list exists; CO issuance and occupancy timing are local; who
inspects and reinspection fees are per-jurisdiction (worksheet blanks);
lender/insurer verification in no-inspection counties is practical guidance,
not statute; § 8-2-26(g) procedural terms not quoted.
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

FORM_ID = "GA.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The inspection ladder for a Georgia dwelling, the two energy-test "
    "gates, what changes in a county that inspects nothing — and a log to "
    "record every result as you go.")

flow.append(k.disclaimer(
    "Georgia deletes the IRC's administration chapter, so your county's "
    "required-inspection list governs — get it in writing and staple it "
    "here."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- who sets it
flow += k.h2_tight("WHY THERE IS NO STATEWIDE INSPECTION LIST")
flow.append(k.body(
    "The 2026 Georgia Amendments to the 2024 IRC do something structural: "
    "\"<i>Delete Chapter 1 'Scope and Administration' without substitution. "
    "Chapter 1 to remain in the Code as a reference and guide for local "
    "governments to use in the development of their own Administrative "
    "Procedures.</i>\" Permit administration, inspection scheduling, and "
    "certificate-of-occupancy issuance are therefore governed by <b>each "
    "local government's own administrative ordinance</b> — the IRC's "
    "inspection section (R109) survives only as a model."))
flow.append(k.body(
    "Pair that with § 8-2-26(a)(4) — permits and inspections are a power a "
    "county <b>may</b> exercise — and the practical rule follows: the "
    "sequence below is the shape nearly every enforcing Georgia "
    "jurisdiction uses, but the binding list is the one your county hands "
    "you with the permit. Ask for it by name: \"your required inspections "
    "list for a new single-family dwelling.\""))
flow.append(k.cite(
    "2026 Georgia Amendments to the 2024 IRC (DCA packet, read directly); "
    "O.C.G.A. § 8-2-26(a)(4). Verified August 2026."))

# ---------------------------------------------------------------- the sequence
flow += k.h2_tight("THE MODEL SEQUENCE — WHAT IS TYPICALLY COMPLETE BEFORE EACH CALL")
flow.append(k.body(
    "A model, not a statute — built on IRC § R109 as the guide Georgia "
    "kept it for, and on universal Georgia practice. Note the trade "
    "inspections: because Georgia deletes the IRC's plumbing, electrical, "
    "and energy parts, trade work is inspected against the <b>state IPC, "
    "the 2023 NEC, and the IMC/IFGC</b> — commonly as separate trade "
    "inspections, not one bundled visit."))

seq = [
    ("1. Footing / foundation",
     "Trenches excavated, forms and reinforcing in place — before any "
     "concrete is placed. On a septic lot, the health-department "
     "construction permit must already be in hand before this stage of "
     "lot development (GA.2, section C)."),
    ("2. Under-slab plumbing",
     "Everything the slab will conceal — under-slab plumbing, sleeves, "
     "vapor barrier, fill — complete and visible before the pour."),
    ("3. Rough plumbing",
     "All plumbing that walls and ceilings will hide, in place and under "
     "test — inspected to the state IPC."),
    ("4. Rough electrical",
     "All wiring, boxes, and service that will be concealed — inspected "
     "to the 2023 NEC."),
    ("5. Rough mechanical / gas",
     "Ductwork, equipment connections, vents, and gas piping that will be "
     "concealed — inspected to the IMC and IFGC. If you will claim the "
     "duct-test exception, the ducts must sit entirely inside the thermal "
     "envelope — make that visible now."),
    ("6. Framing",
     "Roof, wall, ceiling, and floor framing complete with blocking, "
     "bracing, and firestopping; rough-ins approved; penetrations "
     "flashed. Usually called after the trades pass."),
    ("7. Insulation",
     "Insulation and air-sealing in place — before wall or ceiling "
     "coverings. Your blower-door number is being decided here."),
    ("8. Energy testing (DET)",
     "Duct leakage test at rough-in or post-construction (unless "
     "excepted); blower door before final. Both by a certified DET "
     "verifier, both reported in writing — see the gate below."),
    ("9. Trade finals",
     "Plumbing, electrical, and mechanical each complete and working."),
    ("10. Building final / CO",
     "Everything done, site graded, septic final approval issued. The "
     "certificate of occupancy follows under your county's own "
     "administrative procedures."),
]
rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b)] for a, b in seq]
flow.append(k.ref_table(
    "Model Georgia residential inspection ladder (confirm against your "
    "county's list)",
    [k.cellp("Inspection", bold=True),
     k.cellp("What is typically complete / what is looked at", bold=True)],
    rows, [1.7 * inch, CW - 1.7 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>Your county's actual list</b> — copy it from the permit card or "
    "the department's handout, including anything it adds (site, "
    "erosion, temporary power) or bundles:"))
extra_rows = [[k.cellp(""), ""] for _ in range(4)]
flow.append(d.titled_table(
    "County-required inspections not shown above",
    [k.cellp("Inspection", bold=True), k.cellp("When it is called", bold=True)],
    extra_rows, [2.6 * inch, CW - 2.6 * inch], S,
    row_heights=[26] * len(extra_rows)))
flow.append(k.cite(
    "Model sequence: IRC § R109 as guide plus universal Georgia practice — "
    "printed as a model because the 2026 Georgia Amendments delete IRC "
    "Chapter 1 and no statewide list exists. Trade codes: 2026 GA "
    "Amendments (IRC Parts IV, VII, VIII deleted). Verified August 2026."))

# ---------------------------------------------------------------- energy gate
flow += k.h2_tight("THE ENERGY TESTS ARE GATES, NOT SUGGESTIONS")
flow.append(k.callout("The DET reports are part of passing final", [
    Paragraph("The blower-door rule does not stop at the number: \"<i>A "
              "written report of the results of the test shall be signed "
              "by the party conducting the test and provided to the code "
              "official</i>\" (GA IECC § R402.4.1.2) — and the test must "
              "come back <b>under 5 ACH50</b>, conducted by a certified "
              "DET verifier. The duct test (§ R403.3.3) runs at rough-in "
              "or post-construction, at <b>6 cfm25 per 100 sq ft</b> or "
              "better, unless ducts and air handlers sit entirely inside "
              "the envelope. In an enforcing county, no report means no "
              "final. Exactly when the CO issues is your county's "
              "administrative call — but book the verifier before "
              "drywall, not the week you want to move in.", S["body"]),
]))
flow.append(k.cite(
    "GA amendments to the 2015 IECC, § R402.4.1.2 and §§ R403.3.3–.3.4 "
    "(DCA amendment PDFs, read directly). CO timing is local — Chapter 1 "
    "deleted. Verified August 2026."))

# ---------------------------------------------------------------- septic final
flow += k.h2_tight("THE SEPTIC FINAL — DO NOT BACKFILL")
flow.append(k.body(
    "The county health department has its own final, and it comes before "
    "the trench is closed: \"<i>No person may backfill or use an on-site "
    "sewage management system until a final inspection has been made by "
    "the County Board of Health</i>\" and written approval issued (DPH "
    "Rule 511-3-1-.03(4)). And the approval is not permanent armor: later "
    "site changes that adversely affect the system — regrading, "
    "driveways, additions over the drainfield — render it void "
    "(Rule -.03(4)(b)). Your building final and CO will wait on this "
    "in any county that checks."))
flow.append(k.cite(
    "DPH Rule 511-3-1-.03(4), (4)(b) — official DPH rules PDF, read "
    "directly. Verified August 2026."))

# ---------------------------------------------------------------- no-inspection
flow += k.h2_tight("IF YOUR COUNTY INSPECTS NOTHING")
flow.append(k.body(
    "Some Georgia counties run no building department and call no "
    "inspections. Your legal duty does not shrink: the eight state "
    "minimum codes apply statewide with no local adoption (§ 8-2-25(a)), "
    "and your own exemption is conditioned on the work conforming to "
    "them (§ 43-41-17(h)). What disappears is the free referee — so "
    "build your own verification:"))
flow.append(k.bullet(
    "<b>Your lender and insurer will check anyway.</b> Construction "
    "loans draw against progress inspections, and insurers and future "
    "buyers' lenders ask for evidence the house met code. That is "
    "practical reality, not statute — but it is the enforcement you "
    "will actually feel."))
flow.append(k.bullet(
    "<b>Hire the inspection you were not given.</b> Georgia law "
    "contemplates private professional providers for plan review and "
    "inspection (§ 8-2-26(g)); even outside that mechanism, a private "
    "inspector working the ladder above at the same hold points is "
    "cheap against the cost of concealed defects."))
flow.append(k.bullet(
    "<b>The DET tests still happen.</b> The energy code and its testing "
    "rules are among the statewide-mandatory eight. Keep both signed "
    "reports even with no code official asking — they are the proof "
    "that outlives you selling the house."))
flow.append(k.bullet(
    "<b>The septic track never goes away.</b> County health "
    "departments permit and finally inspect septic in every county — "
    "that gate is DPH rule, not local option."))
flow.append(k.cite(
    "O.C.G.A. § 8-2-25(a); § 43-41-17(h); § 8-2-26(g) (procedural terms "
    "not printed — read the subsection before invoking it); DPH Rule "
    "511-3-1. Lender and insurer practice is guidance, not law. "
    "Verified August 2026."))

# ---------------------------------------------------------------- who inspects
flow += k.h2_tight("WHO ACTUALLY INSPECTS — AND WHAT A RE-CALL COSTS")
flow.append(k.body(
    "The state trade boards license electricians, plumbers, and "
    "conditioned-air contractors — <b>they do not inspect houses</b>. "
    "Trade work is checked by your local inspector (or a private "
    "professional provider), against the state trade codes. Reinspection "
    "fees, re-call windows, and scheduling are per-jurisdiction — ask at "
    "your first inspection so your third holds no surprises:"))
flow.append(Spacer(1, 4))
flow.append(d.FillInRow([("How to schedule (portal/phone):", 0.62),
                         ("Notice required:", 0.38)]))
flow.append(d.FillInRow([("Reinspection fee:", 0.4),
                         ("Re-call wait:", 0.3),
                         ("Cutoff time:", 0.3)]))

# ---------------------------------------------------------------- CO
flow += k.h2_tight("THE CERTIFICATE AT THE END — AND WHY YOU KEEP IT")
flow.append(k.body(
    "With IRC Chapter 1 deleted, when and how the certificate of "
    "occupancy issues is set by your county's administrative procedures "
    "— including whether you may occupy anything before it. Get that "
    "answer locally. Then file the CO somewhere permanent, twice over: "
    "it closes your permit file, and under § 43-41-17(h) it is the "
    "<b>start of the 24-month clock</b> that decides whether a future "
    "sale of this house poisons your next owner-built project. The date "
    "on this piece of paper is the one that counts."))
flow.append(k.cite(
    "CO administration local per the Chapter 1 deletion (2026 GA "
    "Amendments); 24-month clock from the CO date — O.C.G.A. "
    "§ 43-41-17(h). Verified August 2026."))

# ---------------------------------------------------------------- the log
flow += k.h2_tight("INSPECTION LOG — RECORD EVERY ONE")
flow.append(k.body(
    "Fill this in as it happens, not from memory. In a lightly-enforced "
    "county this log and your photos may be the only inspection record "
    "the house ever has — which makes it more valuable, not less."))

log_header = [k.cellp("Inspection", bold=True),
              k.cellp("Called", bold=True),
              k.cellp("Held", bold=True),
              k.cellp("Result", bold=True),
              k.cellp("Inspector", bold=True),
              k.cellp("Corrections required / notes", bold=True)]
log_names = [
    "Footing / foundation", "Under-slab plumbing", "Rough plumbing",
    "Rough electrical", "Rough mechanical / gas", "Framing", "Insulation",
    "Duct leakage test (DET)", "Blower door test (DET)", "Septic final",
    "Final — plumbing", "Final — electrical", "Final — mechanical",
    "Final — building", "", "",
]
log_rows = [[k.cellp(n) if n else "", "", "", "", "", ""] for n in log_names]
widths = [1.45 * inch, 0.72 * inch, 0.72 * inch, 0.62 * inch, 1.0 * inch]
widths.append(CW - sum(widths))
flow.append(d.titled_table(
    "Inspection log", log_header, log_rows, widths, S,
    row_heights=[30] * len(log_rows)))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Certificate of occupancy issued:", 0.55),
                         ("Number:", 0.45)]))

flow.append(Spacer(1, 8))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026). IRC Chapter 1 deleted without "
    "substitution, kept only as a guide for local administrative "
    "procedures — 2026 Georgia Amendments to the 2024 IRC (DCA packet, "
    "read directly). Permits and inspections as a local power — O.C.G.A. "
    "§ 8-2-26(a)(4); the eight mandatory codes statewide — § 8-2-25(a); "
    "owner-builder duty to conform — § 43-41-17(h); private professional "
    "providers — § 8-2-26(g). Blower-door test, DET verifier, and the "
    "signed report to the code official — GA IECC § R402.4.1.2; duct "
    "test and its inside-the-envelope exception — §§ R403.3.3–.3.4. "
    "Septic final inspection before backfill or use; approval voided by "
    "adverse site changes — DPH Rule 511-3-1-.03(4), (4)(b). The ladder "
    "itself is a model (IRC § R109 as guide plus universal Georgia "
    "practice) — your county's list governs."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ga-permit-kit",
                       "GA.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
