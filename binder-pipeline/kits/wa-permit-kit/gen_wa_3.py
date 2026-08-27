#!/usr/bin/env python3
"""WA.3 Inspection Sequence — Washington.

Sources verified August 2026 (app.leg.wa.gov):
  RCW 19.28.101(1)   L&I inspects electrical work; no subdivision of
                     government may adopt these provisions by ordinance
                     except cities and towns under RCW 19.28.010(3)
  RCW 19.28.101(2)   48-hour inspection commitment; the 24-hour written
                     request remedy that lets the utility connect
  RCW 19.28.101(3)   15 days to correct after notice; power may be cut
  RCW 19.28.101(4)   nothing may be concealed before approval
  RCW 19.28.101(5)   L&I approval required before the utility connects
  RCW 19.28.010(3),(4) the city/town electrical program option
  WAC 51-51-003      2021 IRC adopted; electrical sent elsewhere
  WAC 51-11R-40240   blower door mandatory, 4.0 ACH50
  WAC 51-11R-40320   duct test and thresholds
  WAC 51-11R-40350   ventilation airflow must be verified
  WAC 246-272A-0250(3)(g)  cover the septic system only after the local
                     health officer approves

Deliberately NOT printed: IRC Chapter 1 subsection numbers for the building
inspections. Washington adopts the model text rather than rewriting it into
the WAC, so the enumerated list is ICC's copyrighted text rather than a
Washington rule this kit can quote and verify line by line — and the list that
governs YOUR job is the one printed on your permit card. The sequence below is
the common Washington residential order, with the agency named for each call.
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

FORM_ID = "WA.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The order Washington inspections happen in, which agency you call for "
    "each one, the three tests you have to pass, and a log to record every "
    "result as you go.")

flow.append(k.disclaimer(
    "Your permit card lists the inspections your job requires — it governs."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- who calls
flow += k.h2_tight("YOU WILL BE CALLING TWO DIFFERENT AGENCIES")
flow.append(k.body(
    "This is the single thing that catches owner-builders in Washington, and "
    "it is not difficulty — it is a phone book problem. Your <b>building, "
    "plumbing and mechanical</b> inspections come from the city or county "
    "that issued your building permit. Your <b>electrical</b> inspections "
    "almost certainly do not."))
flow.append(k.body(
    "The residential code hands electrical work straight out of the building "
    "department: \"<i>Electrical Code is regulated by chapter 296-46B WAC or "
    "Electrical Code as adopted by the local jurisdiction.</i>\" Chapter "
    "296-46B WAC is the Department of Labor &amp; Industries' rule book. The "
    "statute behind it is blunter still — L&amp;I's director \"<i>shall cause "
    "an inspector to inspect all wiring, appliances, devices, and equipment "
    "to which this chapter applies</i>,\" and \"<i>nothing contained in this "
    "chapter may be construed as providing any authority for any subdivision "
    "of government to adopt by ordinance any provisions contained or provided "
    "for in this chapter except those pertaining to cities and towns</i>.\""))

flow.append(k.callout("Cities and towns, not counties", [
    Paragraph("The local-electrical-program option belongs to "
              "<b>incorporated cities and towns</b>. A city or town may enact "
              "and enforce its own electrical ordinance to an equal, higher "
              "or better standard, and where it does, its inspectors must "
              "meet the same qualifications as state electrical inspectors. "
              "Counties have no such power under this chapter.", S["body"]),
    Paragraph("So: if your lot is in unincorporated county, your electrical "
              "permit and inspections come from <b>L&amp;I</b>. If you are "
              "inside city limits, ask the city whether it runs its own "
              "electrical program — several of the larger ones do. Settle "
              "this before you pull any permit; it decides who you call for "
              "the rest of the job. (RCW 19.28.010(3), (4); RCW "
              "19.28.101(1))", S["body"]),
]))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "Two rights on the electrical side you are unlikely to be told about", [
        Paragraph("<b>A 48-hour commitment.</b> \"<i>Upon request, electrical "
                  "inspections will be made by the department within "
                  "forty-eight hours, excluding holidays, Saturdays, and "
                  "Sundays.</i>\"", S["body"]),
        Paragraph("<b>And a remedy if they miss it.</b> \"<i>If, upon "
                  "<b>written</b> request, the electrical inspector fails to "
                  "make an electrical inspection within twenty-four hours, "
                  "the serving utility may immediately connect electrical "
                  "power to the installation if the necessary electrical work "
                  "permit is displayed.</i>\" Note the word <i>written</i> — "
                  "a phone call does not start this clock. If you are waiting "
                  "on temporary power, put the request in writing and keep "
                  "the copy. (RCW 19.28.101(2))", S["body"]),
    ]))

# ---------------------------------------------------------------- the sequence
flow += k.h2_tight("THE SEQUENCE — AND WHO YOU CALL FOR EACH")
flow.append(k.body(
    "The order below is the common Washington residential sequence. The exact "
    "list for your job, and how your department bundles the trades, is "
    "printed on your permit card — that is the list that governs. What is "
    "<b>not</b> negotiable is the agency column, and the rule that nothing "
    "gets covered before it is approved."))

seq = [
    ("1. Temporary power",
     "Service pole or temporary service for construction. Requires an "
     "electrical work permit, and the utility may not connect until the "
     "installation is approved.",
     "L&amp;I or city"),
    ("2. Footing / setback",
     "Trenches excavated, forms and reinforcing steel in place, before any "
     "concrete is placed. Many jurisdictions verify setbacks at this visit — "
     "have your site plan on site.",
     "City / county"),
    ("3. Foundation and under-slab",
     "Foundation walls, damp-proofing and drainage; and everything the slab "
     "will bury — under-slab plumbing, vapor retarder, any under-slab "
     "conduit. Radon rough-in is inspected here where it applies.",
     "City / county"),
    ("4. Under-floor / crawl space",
     "Piers, girders, sill anchorage, grade clearances and ground cover in a "
     "crawl space. If you have chosen an unvented crawl space, this is where "
     "the radon provisions you opted into show up.",
     "City / county"),
    ("5. Shear wall / nailing",
     "Called separately in much of western Washington because of the seismic "
     "design category: hold-downs, anchor bolts, shear panel edge nailing and "
     "the continuous load path, before anything covers them.",
     "City / county"),
    ("6. Electrical rough-in (cover)",
     "All wiring in place before it is concealed. This is a separate call to "
     "a separate agency and it is the one most likely to be forgotten — "
     "nothing may be covered until the electrical inspector approves it.",
     "L&amp;I or city"),
    ("7. Plumbing and mechanical rough-in",
     "Water, waste and vent piping under test, gas piping, duct runs and "
     "combustion air, before concealment.",
     "City / county"),
    ("8. Framing",
     "After roof cover, with framing, blocking, bracing and firestopping "
     "complete and all rough-ins approved. Commonly the visit where the "
     "building inspector checks that every other rough-in has signed off.",
     "City / county"),
    ("9. Insulation and air sealing",
     "Insulation and air barrier in place, before wall and ceiling covering. "
     "The energy code's installation criteria are inspected here.",
     "City / county"),
    ("10. Duct leakage test",
     "Rough-in or post-construction, by the tester — see the thresholds "
     "below. A signed written report goes to the code official.",
     "Third-party tester"),
    ("11. Septic pre-cover",
     "The system may not be backfilled until the local health officer has "
     "given approval to cover. Different agency again.",
     "Local health"),
    ("12. Blower door and ventilation verification",
     "Both mandatory, both after the envelope is closed. Signed written "
     "reports to the code official.",
     "Third-party tester"),
    ("13. Final electrical",
     "Required before the utility will connect permanent power.",
     "L&amp;I or city"),
    ("14. Final plumbing, mechanical, and building",
     "The building final is the one that releases the certificate of "
     "occupancy.",
     "City / county"),
]
rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in seq]
flow.append(k.ref_table(
    "Common Washington residential sequence — and the agency for each call",
    [k.cellp("Inspection", bold=True),
     k.cellp("What must be complete / what is verified", bold=True),
     k.cellp("Who", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - 1.15 * inch, 1.15 * inch]))
flow.append(k.cite(
    "The agency split is statutory: WAC 51-51-003; RCW 19.28.101(1), (5); "
    "RCW 19.28.010(3), (4). The septic cover approval is WAC "
    "246-272A-0250(3)(g). The three tests are WAC 51-11R-40240, "
    "WAC 51-11R-40320 and WAC 51-11R-40350. The <b>order and bundling</b> of "
    "the building-side calls is set by your jurisdiction under the "
    "administrative provisions of the adopted International Residential Code "
    "— this kit prints the common sequence rather than model-code subsection "
    "numbers, because your permit card is the list that binds you. Verified "
    "August 2026."))

# ---------------------------------------------------------------- the tests
flow += k.h2_tight("THE THREE TESTS — BOOK THEM EARLY")
flow.append(k.body(
    "Washington does not offer a visual alternative to any of these. All "
    "three produce a signed written report that goes to the code official, "
    "and in rural counties there are few testers, so they set your schedule "
    "rather than the other way round."))

test_rows = [
    [k.cellp("<b>Envelope air leakage</b><br/>(blower door)"),
     k.cellp("\"<i>The building or dwelling unit shall be tested for air "
             "leakage.</i>\" Maximum <b>4.0 air changes per hour</b> at 50 Pa "
             "for any dwelling unit <b>under any compliance path</b>. The "
             "report must carry a verified location and time stamp and be "
             "signed by the testing agency."),
     k.cellp("§ R402.4.1.2<br/>§ R402.4.1.3.1")],
    [k.cellp("<b>Duct leakage</b>"),
     k.cellp("Rough-in: <b>4.0 cfm per 100 sq ft</b> of conditioned floor "
             "area at 25 Pa — or 3.0 if the air handler is not yet "
             "installed. Post-construction: 4.0 cfm per 100 sq ft. Ducts and "
             "air handlers entirely inside the thermal envelope: 8.0 — but "
             "<b>ducts in a crawl space do not qualify</b>."),
     k.cellp("§ R403.3.5<br/>§ R403.3.6")],
    [k.cellp("<b>Ventilation airflow</b>"),
     k.cellp("\"<i>Mechanical ventilation systems shall be tested and "
             "verified to provide the minimum ventilation flow rates "
             "required.</i>\" The one owner-builders forget, because it does "
             "not feel like a test. Ducted range hoods of 6 inches or larger "
             "with no more than one elbow are excepted."),
     k.cellp("§ R403.6.2")],
]
flow.append(k.ref_table(
    "Mandatory performance tests, 2021 Washington State Energy Code",
    [k.cellp("Test", bold=True), k.cellp("What it requires", bold=True),
     k.cellp("Section", bold=True)],
    test_rows, [1.45 * inch, CW - 1.45 * inch - 1.2 * inch, 1.2 * inch]))

# ---------------------------------------------------------------- wrong
flow += k.h2_tight("WHEN AN INSPECTION GOES WRONG")
wrong = [
    [k.cellp("<b>You failed a building inspection</b>"),
     k.cellp("Get the written correction notice, fix exactly what it names, "
             "and re-call. Re-inspection fees and how soon you may re-call "
             "are local — ask at your first inspection so it is not a "
             "surprise at your fifth."),
     k.cellp("local")],
    [k.cellp("<b>You failed an electrical inspection</b>"),
     k.cellp("A different regime. Where an installation is not in accordance "
             "with the chapter or is dangerous, you are notified and \"<i>shall "
             "within fifteen days, or such further reasonable time as may "
             "upon request be granted</i>,\" make the repairs. The inspector "
             "may order electrical service disconnected, and reconnecting "
             "without approval is unlawful."),
     k.cellp("RCW 19.28.101(3)")],
    [k.cellp("<b>You covered something early</b>"),
     k.cellp("\"<i>No electrical wiring or equipment subject to this chapter "
             "may be concealed until it has been approved by the inspector "
             "making the inspection.</i>\" At inspection it must be "
             "sufficiently accessible for the inspector to test it. Expect to "
             "open it up. The same principle applies to your septic system "
             "and to every building-side rough-in."),
     k.cellp("RCW 19.28.101(4)")],
    [k.cellp("<b>The utility will not connect you</b>"),
     k.cellp("You must obtain inspection and approval from L&amp;I "
             "\"<i>before requesting the electric utility to connect</i>.\" "
             "The utility connects on the certified permit. If an inspection "
             "is overdue, use the written-request route in RCW 19.28.101(2)."),
     k.cellp("RCW 19.28.101(5)")],
]
flow.append(k.ref_table(
    "Failures, concealment, and power",
    [k.cellp("Situation", bold=True), k.cellp("What applies", bold=True),
     k.cellp("Authority", bold=True)],
    wrong, [1.6 * inch, CW - 1.6 * inch - 1.25 * inch, 1.25 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>At the end</b>, the building department issues the certificate of "
    "occupancy under the administrative provisions of the adopted "
    "International Residential Code. Ask yours early what it wants in hand "
    "before it will issue — commonly every trade final including the "
    "electrical one, the energy test reports, and the septic operational "
    "approval. Do not plan a move-in date around an assumption here."))

# ---------------------------------------------------------------- the log
flow += k.h2_tight("INSPECTION LOG — RECORD EVERY ONE")
flow.append(k.body(
    "Fill this in as it happens, not from memory. Note <b>which agency</b> "
    "you called as well as the result — on a Washington job that is the "
    "detail you will want six months later. If a result is ever disputed, "
    "this page and your photographs are the record you have."))

log_header = [k.cellp("Inspection", bold=True),
              k.cellp("Agency", bold=True),
              k.cellp("Called", bold=True),
              k.cellp("Held", bold=True),
              k.cellp("Result", bold=True),
              k.cellp("Corrections required / notes", bold=True)]
log_names = [
    "Temporary power", "Footing / setback", "Foundation / under-slab",
    "Under-floor / crawl", "Shear wall / nailing", "Electrical rough-in",
    "Plumbing rough-in", "Mechanical rough-in", "Framing",
    "Insulation / air sealing", "Duct leakage test", "Septic pre-cover",
    "Blower door", "Ventilation verification", "Final electrical",
    "Final plumbing", "Final mechanical", "Final building", "", "",
]
log_rows = [[k.cellp(n) if n else "", "", "", "", "", ""] for n in log_names]
widths = [1.3 * inch, 0.82 * inch, 0.66 * inch, 0.66 * inch, 0.62 * inch]
widths.append(CW - sum(widths))
flow.append(d.titled_table(
    "Inspection log", log_header, log_rows, widths, S,
    row_heights=[28] * len(log_rows)))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Certificate of occupancy issued:", 0.55),
                         ("Number:", 0.45)]))

flow.append(Spacer(1, 8))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026 at app.leg.wa.gov). Electrical is "
    "inspected by L&amp;I and no subdivision of government may legislate in "
    "the field except cities and towns — RCW 19.28.101(1) with RCW "
    "19.28.010(3), (4). The 48-hour inspection commitment and the 24-hour "
    "written-request remedy — RCW 19.28.101(2). Fifteen days to correct after "
    "notice, and disconnection powers — RCW 19.28.101(3). Nothing concealed "
    "before approval, and accessibility at inspection — RCW 19.28.101(4). No "
    "utility connection before approval — RCW 19.28.101(5). The residential "
    "code sends electrical to chapter 296-46B WAC or the local jurisdiction's "
    "electrical code — WAC 51-51-003. Blower door, duct and ventilation "
    "testing — WAC 51-11R-40240, 51-11R-40320, 51-11R-40350 (2021 Washington "
    "State Energy Code, Residential, effective March 15, 2024). Septic may "
    "not be covered before the local health officer approves — WAC "
    "246-272A-0250(3)(g)."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "wa-permit-kit",
                       "WA.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
