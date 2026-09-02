#!/usr/bin/env python3
"""WI.3 Inspection Sequence.

Verified sources:
  SPS 320.10(1)        every inspection by an inspector certified under
                       ch. SPS 305 holding the credential for that inspection
  SPS 320.10(2)(b)     the applicant requests; construction may not pass the
                       point of inspection; and the TWO-BUSINESS-DAY release
  SPS 320.10(3)(b)-(i) the complete list of inspection types, verbatim
  SPS 320.10(3)(f)     the five rough categories, and the right to take them
                       as one inspection or individually
  SPS 320.10(3)(h)     no occupancy before a final that finds no critical
                       violations — and the FIVE-BUSINESS-DAY release
  SPS 320.10(4)        notice of compliance or noncompliance posted at the job
                       site
  SPS 320.08(2)        you are locked to the agency that issued your permit
  SPS 383.26(2)(a),(e) no POWTS component covered before inspection — and the
                       next-workday release
  SPS 383.45(2),(3),(4)  frozen soil, snow cover and the quarter-inch wire test
  SPS 320.02(2)(a)     occupancy may not be restricted for any reason other
                       than noncompliance with this code

Deliberately NOT printed: a re-inspection fee. s. SPS 320.10(3)(f)4. permits a
separate fee for each individual rough inspection but sets no amount, and fees
are municipal under Wis. Stat. s. 101.65(1)(c).
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

FORM_ID = "WI.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections & Occupancy"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every inspection the code names, the three clocks that let you keep "
    "working, and a log to fill in as each one passes.")

flow.append(k.disclaimer(
    "Your municipality or inspection agency may schedule additional visits by "
    "ordinance. The list below is the state minimum that applies everywhere."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- clocks
flow += k.h2_tight("THE THREE CLOCKS")
flow.append(k.body(
    "These are the most valuable numbers in this document, and most "
    "owner-builders never learn them. Wisconsin does not leave you waiting "
    "indefinitely for an inspector. It gives you a release in every "
    "direction — one to keep building, one to move in, and one on the "
    "septic."))
flow.append(k.callout_long("All three releases, in the code's own words", [
    Paragraph("<b>To keep building — two business days.</b> The general rule "
              "is that “<i>construction may not proceed beyond the point of "
              "inspection until the inspection has been completed</i>”. But: "
              "“<i><b>Construction may proceed if the inspection has not taken "
              "place by the end of the second business day following the day "
              "of notification</b> or as otherwise agreed between the "
              "applicant and the municipality or authorized UDC inspection "
              "agency.</i>” (s. SPS 320.10(2)(b)2. and 3.)", S["body"]),
    Paragraph("<b>To move in — five business days.</b> “<i>the dwelling may "
              "not be occupied until a final inspection has been made that "
              "finds no critical violations of this code that could reasonably "
              "be expected to affect the health or safety of a person using "
              "the dwelling.</i>” But: “<i><b>Occupancy may proceed in "
              "accordance with local ordinances if the inspection has not been "
              "completed by the end of the fifth business day following the "
              "day of notification</b> or as otherwise agreed between the "
              "applicant and the department or municipality.</i>” "
              "(s. SPS 320.10(3)(h)1. and 2.)", S["body"]),
    Paragraph("<b>And for the septic — the next workday.</b> “<i>If an "
              "inspection is not made by the end of the next workday, "
              "excluding Saturdays, Sundays and holidays, after the requested "
              "inspection day, the master plumber or the master "
              "plumber-restricted service may proceed with the installation of "
              "the POWTS, including backfilling and covering.</i>” "
              "(s. SPS 383.26(2)(e))", S["body"]),
    Paragraph("<b>How to actually use these.</b> Each clock runs from the day "
              "you gave <i>notification</i>, so the notification is the thing "
              "to document. Request in writing or by a method that leaves a "
              "record, note the date and time on the log at the back of this "
              "document, and photograph the work before you cover it. A clock "
              "you cannot prove you started is a clock you do not have.",
              S["body"]),
]))

# ---------------------------------------------------------------- who
flow += k.h2_tight("WHO INSPECTS, AND WHY YOU CANNOT SHOP", reserve=1.8)
flow.append(k.body(
    "Every inspection “<i>shall be performed by an inspector certified in "
    "accordance with ch. SPS 305 who holds the respective credential for the "
    "inspection performed</i>” (s. SPS 320.10(1)). One person may hold several "
    "credentials, which is why a single inspector often covers construction, "
    "electrical, plumbing and HVAC on a rural job — but each credential is "
    "separate and each must be held."))
flow.append(k.body(
    "If you are in a municipality where the department has jurisdiction, "
    "remember the lock-in from WI.1: “<i>A person who obtains a Wisconsin "
    "uniform building permit from a registered UDC inspection agency shall "
    "retain the same agency to conduct the inspections for the project</i>” "
    "(s. SPS 320.08(2)). Choose the agency before you file, not after your "
    "first disagreement."))

# ---------------------------------------------------------------- the list
flow += k.h2_tight("THE INSPECTIONS, IN ORDER", reserve=2.2)
flow.append(k.body(
    "Section SPS 320.10(3) names eight inspection types. Here they are in "
    "build order, with what the code actually says about each."))
rows = [
    [k.cellp("<b>Erosion control</b>"),
     k.cellp("Performed “<i>concurrently with all other required construction "
             "inspections</i>”, and the delegated authority may add more. So "
             "it is not one visit — your control measures have to be right "
             "every time somebody comes out")],
    [k.cellp("<b>Foundation excavation</b>"),
     k.cellp("“<i>after the placement of any forms or required reinforcement "
             "and prior to the placement of the permanent foundation "
             "material</i>”. If drain tile is required — by the inspector or "
             "by groundwater in the hole — “<i>the presence and location of "
             "bleeders used to connect the interior and exterior drain "
             "tile</i>” is inspected at the same time")],
    [k.cellp("<b>Foundation reinforcement</b>"),
     k.cellp("“<i>The placement of reinforcement shall be inspected where the "
             "reinforcement is required for code compliance</i>”")],
    [k.cellp("<b>Foundation</b>"),
     k.cellp("“<i>after completion</i>” — and where dampproofing, exterior "
             "insulation or drain tile are required, <b>before "
             "backfilling</b>. Do not backfill on a promise")],
    [k.cellp("<b>Rough</b> — five categories"),
     k.cellp("“<i>after the rough work is constructed but before it is "
             "concealed</i>”, for: <b>a.</b> the basement floor area; "
             "<b>b.</b> general construction, including framing; <b>c.</b> "
             "rough electrical; <b>d.</b> rough plumbing; <b>e.</b> rough "
             "heating, ventilating and air conditioning")],
    [k.cellp("<b>Insulation</b>"),
     k.cellp("“<i>of the insulation and vapor retarders after they are "
             "installed but before they are concealed</i>” — so this is "
             "before drywall, and it covers the vapor retarder too")],
    [k.cellp("<b>Final</b>"),
     k.cellp("The occupancy gate. See the five-business-day release above")],
    [k.cellp("<b>Installation</b>"),
     k.cellp("Only if you are setting a manufactured or modular home")],
]
flow.append(k.ref_table(
    "Wis. Admin. Code s. SPS 320.10(3)(b) to (i)",
    [k.cellp("Inspection", bold=True), k.cellp("What the code requires",
                                               bold=True)],
    rows, [1.85 * inch, CW - 1.85 * inch]))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "You choose how the rough inspections are packaged", [
        Paragraph("“<i>All categories of work for rough inspections may be "
                  "completed before the notice for inspection is given, "
                  "provided the work has not been covered.</i>” and "
                  "“<i>The applicant may request one rough inspection or "
                  "individual rough inspections.</i>” "
                  "(s. SPS 320.10(3)(f)2. and 3.)", S["body"]),
        Paragraph("That is a real scheduling decision. One combined rough "
                  "means one visit and usually one fee — the code allows "
                  "“<i>a separate fee … for each individual inspection</i>” "
                  "(subd. 4.) — but it also means every trade has to be "
                  "finished and correct on the same day, and one failure can "
                  "hold up the others. Individual roughs cost more and let "
                  "each trade clear on its own schedule. On a "
                  "self-performed build where you are doing the work in "
                  "sequence anyway, individual roughs are usually the calmer "
                  "choice.", S["body"]),
    ]))

# ---------------------------------------------------------------- septic
flow += k.h2_tight("THE SEPTIC INSPECTION IS A SEPARATE TRACK", reserve=2.0)
flow.append(k.body(
    "Your POWTS is inspected by the county under a different chapter, by a "
    "certified POWTS inspector, and it is the master plumber — not you — who "
    "calls it in. “<i>The master plumber or the master plumber-restricted "
    "service responsible for the installation of a POWTS … shall notify the "
    "governmental unit when the work will be or is ready for inspection</i>” "
    "and “<i>shall provide the necessary equipment and properly licensed "
    "personnel required for the inspection</i>” "
    "(s. SPS 383.26(2)(b) and (d))."))
flow.append(k.body(
    "The rule against covering work is stricter here than on the building "
    "side: “<i>no part of a POWTS component may be covered nor any POWTS "
    "component put into service until the governmental unit or the department "
    "has had an opportunity to inspect the system</i>” "
    "(s. SPS 383.26(2)(a)) — with the next-workday release quoted earlier."))
flow.append(k.callout(
    "Weather can stop the septic install outright", [
        Paragraph("Three conditions in s. SPS 383.45 will send the crew home, "
                  "and they matter for scheduling a Wisconsin build season:",
                  S["body"]),
        Paragraph("<b>Frozen soil.</b> Components consisting in part of in "
                  "situ soil “<i>may not be installed if the soil is frozen at "
                  "or below the infiltrative surface of the component</i>”. "
                  "<b>Snow.</b> “<i>Snow cover shall be removed before "
                  "excavating or installing.</i>” <b>Moisture.</b> “<i>If the "
                  "soil at the infiltrative surface can be rolled into a "
                  "¼-inch wire, the installation may not proceed.</i>”",
                  S["body"]),
        Paragraph("The wire test is the one that surprises people — it is a "
                  "wet-soil test, not a cold one, and it can stop work in a "
                  "rainy June as easily as a frozen November.", S["body"]),
    ]))

# ---------------------------------------------------------------- results
flow += k.h2_tight("HOW RESULTS ARE COMMUNICATED", reserve=1.8)
flow.append(k.body(
    "“<i>Notice of compliance or noncompliance with this code shall be written "
    "on the building permit or another readily visible means and posted at the "
    "job site</i>”, or delivered electronically if you and the inspector both "
    "agree (s. SPS 320.10(4)(a)1.). On a finding of noncompliance the "
    "authority “<i>shall also notify the applicant of record and the owner, in "
    "writing, of the violations to be corrected</i>” (subd. 2.). As an "
    "owner-builder you are both, so you should receive it twice over — and if "
    "you get a verbal correction only, ask for it in writing."))
flow.append(k.body(
    "One protection worth knowing at the end of the job: your municipality may "
    "not invent occupancy conditions. “<i>A municipality may not adopt an "
    "ordinance on any subject falling within the scope of this code including "
    "establishing restrictions on the occupancy of dwellings for any reason "
    "other than noncompliance with the provisions of this code</i>” "
    "(s. SPS 320.02(2)(a)). Occupancy turns on the final inspection finding no "
    "critical code violations — not on landscaping, not on a driveway being "
    "paved, not on a final grade certificate, unless some other body of law "
    "requires it."))

# ---------------------------------------------------------------- log
flow += k.h2_tight("INSPECTION LOG", reserve=2.0)
flow.append(k.body(
    "Record the date you gave notification as well as the date of the visit. "
    "The notification date is what starts the two-business-day and "
    "five-business-day clocks, and it is the only one you control."))
flow += k.check_table(
    "Building inspections — s. SPS 320.10(3)",
    [("Foundation excavation (and bleeders, if drain tile required)",
      [("Notified", 0.5), ("Result", 0.5)]),
     ("Foundation reinforcement",
      [("Notified", 0.5), ("Result", 0.5)]),
     ("Foundation — before backfill",
      [("Notified", 0.5), ("Result", 0.5)]),
     ("Rough — basement floor area",
      [("Notified", 0.5), ("Result", 0.5)]),
     ("Rough — general construction and framing",
      [("Notified", 0.5), ("Result", 0.5)]),
     ("Rough — electrical",
      [("Notified", 0.5), ("Result", 0.5)]),
     ("Rough — plumbing",
      [("Notified", 0.5), ("Result", 0.5)]),
     ("Rough — heating, ventilating and air conditioning",
      [("Notified", 0.5), ("Result", 0.5)]),
     ("Insulation and vapor retarders — before concealment",
      [("Notified", 0.5), ("Result", 0.5)]),
     ("Final — the occupancy gate",
      [("Notified", 0.5), ("Result", 0.5)]),
     ("Installation (manufactured or modular home only)",
      [("Notified", 0.5), ("Result", 0.5)])],
    notes_header="Inspector")

flow += k.check_table(
    "Septic and water — the county and DNR track",
    [("POWTS inspection before any component is covered",
      [("Notified", 0.5), ("Result", 0.5)]),
     ("Well construction report filed by the driller",
      [("Driller", 0.5), ("Date", 0.5)]),
     ("Coliform and nitrate samples collected",
      [("Date", 0.5), ("Result", 0.5)])],
    notes_header="Office")

flow.append(Spacer(1, 4))
flow.append(k.ref_table(
    "Sources — every Wisconsin claim in this document (verified September 2026)",
    [k.cellp("What this document states", bold=True),
     k.cellp("Authority", bold=True)],
    [[k.cellp("Certified inspector holding the credential for that "
              "inspection"), k.cellp("s. SPS 320.10(1)")],
     [k.cellp("Applicant requests; no work past the point of inspection"),
      k.cellp("s. SPS 320.10(2)(b)1., 2.")],
     [k.cellp("Two business days, then construction may proceed"),
      k.cellp("s. SPS 320.10(2)(b)3.")],
     [k.cellp("The eight inspection types and what each covers"),
      k.cellp("s. SPS 320.10(3)(b) to (i)")],
     [k.cellp("One rough inspection or individual roughs, applicant's choice"),
      k.cellp("s. SPS 320.10(3)(f)2., 3.")],
     [k.cellp("No occupancy before a final finding no critical violations"),
      k.cellp("s. SPS 320.10(3)(h)1.")],
     [k.cellp("Five business days, then occupancy may proceed"),
      k.cellp("s. SPS 320.10(3)(h)2.")],
     [k.cellp("Notice posted at the job site; written notice of violations"),
      k.cellp("s. SPS 320.10(4)(a)1., 2.")],
     [k.cellp("Occupancy may not be restricted for non-code reasons"),
      k.cellp("s. SPS 320.02(2)(a)")],
     [k.cellp("Locked to the agency that issued the permit"),
      k.cellp("s. SPS 320.08(2)")],
     [k.cellp("No POWTS component covered before inspection; next-workday "
              "release"), k.cellp("s. SPS 383.26(2)(a), (e)")],
     [k.cellp("The master plumber calls in the POWTS inspection"),
      k.cellp("s. SPS 383.26(2)(b), (d)")],
     [k.cellp("Frozen soil, snow cover and the quarter-inch wire test"),
      k.cellp("s. SPS 383.45(2), (3), (4)")]],
    [CW - 2.35 * inch, 2.35 * inch]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "wi-permit-kit",
                       "WI.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
