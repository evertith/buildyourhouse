#!/usr/bin/env python3
"""ID.3 Inspection Sequence & Clocks.

Every Idaho claim in this document was read against its primary source in
September 2026 and is cited on-page.

The organizing idea: Idaho gives the permit holder more statutory clocks than
almost any state in this line — a completeness clock, a 48-business-hour
inspection clock with a self-help remedy on all four tracks, and a refund for
an unexplained failure — and gives the BUILDING inspection sequence to nobody.
No Idaho statute enumerates the residential building inspections; the trade
ladders are in rule. The document prints what is in a rule, prints the model
code's list as the local default with a write-in, and puts the clocks first.

Verified sources:
  § 39-4117(1)-(4)      permit-process document; 10 business days to notice an
                        incomplete residential application; 10 per resubmission;
                        completeness is not approval; extension only in writing
  § 39-4113(2), (6)     the 30-day plan-review clock is for public works and
                        schools ONLY (verified limit)
  § 39-4116(6)          laws in effect at application govern the permit
  § 39-4118             48 business hours → third-party inspector, refund; 10%
                        refund if no failure reason within 3 business days;
                        inspector qualification (2025 ch. 221, eff. 1 Jul 2025)
  § 54-1004A, § 54-2626A, § 54-5020A   the same rule on the electrical,
                        plumbing and HVAC tracks (2026 ch. 232, eff. 1 Jul 2026)
  § 39-4108             ICC certification; residential-certified inspectors
  § 39-4119             live virtual re-inspections
  § 39-4107(2), § 39-4120   the Board hears appeals for buildings within the
                        DIVISION's jurisdiction only (verified limit)
  § 54-1004             correction notice must specify violations and a period
  § 54-1005(3); IDAPA 24.39.10.200.04   utility lock; contractor-only temp power
  IDAPA 24.39.10.500.01.a.i   nothing concealed until approved for cover
  IDAPA 24.39.20.500.03   plumbing: groundwork → rough-in → final tags
  IDAPA 24.39.70.500.03   HVAC: work-in-progress → final tags
  § 54-5020(1)          HVAC: notify DOPL at least 1 day before, Sundays and
                        holidays excluded; reinspection at actual cost
  § 54-5017(4)          HVAC no-permit: double, then triple fee
  DOPL plumbing and HVAC pages   inspection codes; eTRAKiT next-day requests
                        until 7 p.m.; "this permit application is not an
                        inspection request"
  IDAPA 58.01.03.011.03, .011.05   septic: 48 hours' notice; no wastewater
                        before final and as-built
  § 42-238(11)          driller's report within 30 days

DELIBERATELY NOT CLAIMED, and why:
  - A statewide residential building inspection list. None exists in statute
    or rule; IRC R109 as adopted governs, and Part I is locally amendable.
  - Any appeal route for a trade inspector's correction notice. The trade
    chapters provide board appeals of civil penalties only; the document says
    ask the supervisor in writing and cites nothing.
  - A permit life for the building permit. Not in the Act; IRC R105.5 as
    adopted (180 days to commence) is locally amendable.
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
sec = k.sec
NB = k.NB
CITE = k.CITE_COL

FORM_ID = "ID.3"
FORM_TITLE = "Inspection Sequence & Clocks"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Four inspection tracks over one Idaho house, the clocks the statute puts "
    "on every one of them, and the one that starts before the footings.")

flow.append(k.disclaimer(
    "The trade inspection ladders below are the state rules'. A city or county "
    "running its own program sets its own; an enforcing jurisdiction's "
    "building inspections follow IRC R109 as its ordinance adopted it. Ask, "
    "and write the answer on the log at the end."))
flow.append(Spacer(1, 10))

# ------------------------------------------------- who inspects what
flow += k.h2_tight("WHAT YOU GET DEPENDS ON WHETHER ANYONE ADOPTED A CODE",
                   reserve=2.0)
flow.append(k.body(
    "ID.1 settled whether your city or county enforces a building code. Here "
    "is what each answer means once the concrete moves. <b>Read across the "
    "trade columns.</b> They are the same in both rows, and that is the point "
    "Idaho owner-builders most often miss."))
rows = [
    [k.cellp("<b>Enforcing jurisdiction</b>"),
     k.cellp("The local building department, on IRC R109 as adopted and "
             "amended by its ordinance, ending in a certificate of "
             "occupancy under R110"),
     k.cellp("<b>DOPL</b> — separate permits, separate inspectors, separate "
             "tags — unless the city or county runs its own program for "
             "that trade")],
    [k.cellp("<b>No building code adopted</b>"),
     k.cellp("<b>Nobody.</b> No building permit, no footing or framing "
             "inspection, no certificate of occupancy. Nobody offers a "
             "voluntary one either — DOPL issues no residential permit"),
     k.cellp("<b>DOPL. Still required.</b> Electrical, plumbing and HVAC "
             "permits and inspections do not depend on the Building Code "
             "Act at all")],
]
flow.append(k.ref_table(
    "Two answers, four tracks",
    [k.cellp("Your status", bold=True),
     k.cellp("Who inspects the BUILDING", bold=True),
     k.cellp("Who inspects the TRADES", bold=True)],
    rows, [1.45 * inch, (CW - 1.45 * inch) * 0.5, (CW - 1.45 * inch) * 0.5]))
flow.append(k.cite(
    f"Building: Idaho Code Title 39, Chapter 41 ({sec('39-4111')}, "
    f"{sec('39-4116')}). Electrical, plumbing and HVAC: Title 54, Chapters "
    f"10, 26 and 50 ({sec('54-1005')}, {sec('54-2620')}, {sec('54-5016')}). "
    f"Septic and the well are a fifth and sixth track — the health district "
    f"and IDWR — and come at the end of this document."))

# ------------------------------------------------- temp power
flow += k.h2_tight("THE FIRST DECISION — TEMPORARY POWER, THREE WAYS",
                   reserve=2.4)
flow.append(k.body(
    f"Your power supplier \"shall not connect with or energize any electrical "
    f"installation … unless an inspection has been conducted and resulted as "
    f"'passed'\" ({sec('54-1005(3)')}); the only exception is a connection "
    f"\"after the purchase of an electrical permit by a licensed electrical "
    f"contractor,\" which the rule confines to preserving life or property "
    f"and \"temporary service for construction\" — \"at the request of a "
    f"licensed electrical contractor\" (IDAPA 24.39.10.200.04). On a "
    f"homeowner permit that door is shut. Decide before the footings:"))
rows = [
    [k.cellp("<b>A</b>", center=True),
     k.cellp("<b>A licensed electrical contractor pulls the permit for the "
             "temporary service</b>"),
     k.cellp("The utility energizes on the contractor's request before "
             "inspection; the contractor \"assumes full responsibility.\" "
             "Your homeowner permit covers the house wiring separately")],
    [k.cellp("<b>B</b>", center=True),
     k.cellp("<b>You build the temporary service on your homeowner "
             "permit</b>"),
     k.cellp("Request the inspection; the utility may set the meter only "
             "after it passes. The 48-business-hour clock below applies. "
             "Nothing may be concealed before approval for cover")],
    [k.cellp("<b>C</b>", center=True),
     k.cellp("<b>Generator until the permanent service passes</b>"),
     k.cellp("No utility involvement until the final. Note (4): nobody but "
             "a power supplier may energize an installation before a permit "
             "is bought — buy the permit first either way")],
]
flow.append(k.ref_table(
    "Three ways to get power on site",
    [k.cellp("", bold=True, center=True), k.cellp("Option", bold=True),
     k.cellp("How it works", bold=True)],
    rows, [0.35 * inch, 2.3 * inch, CW - 2.65 * inch]))

# ------------------------------------------------- clocks
flow += k.h2_tight("THE CLOCKS THE STATUTE GIVES YOU", reserve=2.4)
flow.append(k.body(
    "Idaho wrote three of these in 2025 and 2026, and they are the most "
    "useful pages in this kit if an office goes quiet on you."))
rows = [
    [k.cellp("<b>Completeness — 10 business days</b>"),
     k.cellp("If a residential building permit application \"is deemed "
             "incomplete, the local government shall, <b>within ten (10) "
             "business days</b> of receipt … provide written notice to the "
             "applicant specifying any missing information.\" Each "
             "resubmission gets another 10 business days for a written "
             "completeness determination — which \"shall not constitute "
             "approval\" but sends the application to formal plan review"),
     k.cellp(f"{sec('39-4117(2)')}, (3)")],
    [k.cellp("<b>Extension only in writing</b>"),
     k.cellp("The clock moves only if you \"agree in writing to an "
             "extension,\" and first \"a local government shall provide "
             "written notice to an applicant explaining that an extension is "
             "needed\""),
     k.cellp(sec("39-4117(4)"))],
    [k.cellp("<b>Plan review — no clock for a house</b>"),
     k.cellp("The 30-calendar-day initial-review deadline in the Act applies "
             "to \"public works\" and public school plans only. There is no "
             "statutory plan-review deadline for a private residence"),
     k.cellp(f"{sec('39-4113(2)')}, (6)")],
    [k.cellp("<b>Which law governs</b>"),
     k.cellp("\"Permits shall be governed by the laws in effect at the time "
             "the permit application is received\""),
     k.cellp(sec("39-4116(6)"))],
    [k.cellp("<b>Failure with no reason — 10% back</b>"),
     k.cellp("If an inspector fails the work and \"fails to, within three (3) "
             "business days, provide the permit holder or his agent with a "
             "reason for the failure,\" the jurisdiction \"shall refund ten "
             "percent (10%)\" of the inspection fee. Same rule on all four "
             "tracks"),
     k.cellp(f"{sec('39-4118(2)')}; {sec('54-1004A(2)')}; "
             f"{sec('54-2626A(2)')}; {sec('54-5020A(2)')}")],
]
flow.append(k.ref_table(
    "Deadlines the office owes you",
    [k.cellp("Clock", bold=True), k.cellp("What the statute says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.7 * inch, CW - 1.7 * inch - CITE, CITE]))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "The 48-business-hour rule — one sentence, four statutes, and a self-help "
    "remedy", [
        Paragraph("\"If an inspection requested by a permit holder <b>is not "
                  "performed within forty-eight (48) business hours</b>, such "
                  "permit holder shall be authorized to <b>hire a third-party "
                  "inspector</b> to perform such inspection. The permit "
                  "holder or third-party inspector shall notify the division "
                  "or local government that such inspection is being "
                  "completed by a third-party inspector. The permit holder "
                  "shall provide a copy of the results of the completed "
                  "inspection to the division or local government. A permit "
                  "holder who obtains a third-party inspection under this "
                  "section <b>shall be refunded any fee</b>, or portion "
                  "thereof, that the permit holder paid … for such "
                  "inspection.\"", S["body"]),
        Paragraph(f"The text is identical in {sec('39-4118(1)')} (building, "
                  f"effective 1&#160;July 2025) and in {sec('54-1004A(1)')} "
                  f"(electrical), {sec('54-2626A(1)')} (plumbing) and "
                  f"{sec('54-5020A(1)')} (HVAC), all effective 1&#160;July "
                  f"2026. The third-party inspector must hold the same "
                  f"credential as the state's: ICC certification for "
                  f"building ({sec('39-4108')}), and the electrical, plumbing "
                  f"and HVAC qualifications the trade chapters set for their "
                  f"own inspectors. <b>Log the date and time of every "
                  f"request</b> — the log at the end has the column — because "
                  f"the clock runs from the request.", S["body"]),
    ]))

# ------------------------------------------------- trade ladders
flow += k.h2_tight("THE TRADE LADDERS, AS THE RULES FIX THEM", reserve=2.4)
flow.append(k.body(
    "Each DOPL inspection ends in a <b>tag</b> attached to the work. The tags "
    "are the record; keep them on until the final."))
rows = [
    [k.cellp("<b>Plumbing</b>"),
     k.cellp("<b>Groundwork</b> — \"for groundwork to be covered, with "
             "acceptance by the inspector,\" tag \"preferably to a vertical "
             "riser\" → <b>rough-in</b> — \"prior to covering or "
             "concealing\" → <b>final</b> — \"when the plumbing as "
             "specified on the permit is complete\""),
     k.cellp("IDAPA 24.39.20.500.03")],
    [k.cellp("<b>HVAC</b>"),
     k.cellp("<b>Work-in-progress</b> — \"following inspection of "
             "groundwork, rough-in work, or any portion of the installation "
             "that is to be covered or otherwise concealed\" → <b>final</b>. "
             "A \"Notice of Correction\" tag means a reinspection and a "
             "reinspection fee. Notify DOPL \"at least one (1) day prior to "
             "the desired inspection, Sundays and holidays excluded\""),
     k.cellp(f"IDAPA 24.39.70.500.03; {sec('54-5020(1)')}")],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("<b>Cover</b> — \"No wiring or equipment may be concealed in "
             "any manner from access or sight until the work has been "
             "inspected and approved for cover\" → <b>final</b>, which is "
             "what unlocks the meter. A correction notice \"shall clearly "
             "indicate any and all violations to be corrected and specify a "
             "definite period of time\""),
     k.cellp(f"IDAPA 24.39.10.500.01.a.i; {sec('54-1005(3)')}; "
             f"{sec('54-1004')}")],
]
flow.append(k.ref_table(
    "Three ladders, three rules",
    [k.cellp("Track", bold=True), k.cellp("The rungs, quoted", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.0 * inch, CW - 1.0 * inch - CITE, CITE]))
flow.append(k.cite(
    "<b>Booking.</b> Every DOPL form says it in capitals: \"THIS PERMIT "
    "APPLICATION IS NOT AN INSPECTION REQUEST.\" Requests go through DOPL's "
    "eTRAKiT portal, linked from each trade's permit page — \"requests for a "
    "next day inspection can be made until 7 p.m. MST\" — or the inspection "
    "phone line using the code for the inspection type: plumbing "
    "<b>203</b> groundwork, <b>201</b> rough-in, <b>204</b> final; HVAC "
    "<b>701</b> rough-in, <b>713</b> gas pressure, <b>704</b> final. The "
    "assigned inspector and his inspection days for your city are on DOPL's "
    "Inspector List with Schedules (ID.4). Post the orange Job Identification "
    "Sticker where the inspector will see it. Combined permits: a DOPL "
    "plumbing or HVAC permit that \"includes any part of an electrical "
    f"installation\" satisfies the electrical chapter if the fees are paid "
    f"({sec('54-1016(4)')}; {sec('54-5016(2)')})."))

# ------------------------------------------------- building
flow += k.h2_tight("THE BUILDING INSPECTIONS — IRC R109 AS YOUR ORDINANCE "
                   "ADOPTED IT", reserve=2.2)
flow.append(k.body(
    "No Idaho statute or rule enumerates the residential building inspections. "
    "In an enforcing jurisdiction, IRC R109 governs as the local ordinance "
    "adopted it — and Part I, where R109 lives, is one of the parts a local "
    f"government may amend by ordinance ({sec('39-4116(4)(c)(i)')}). The "
    f"model code's list is the default: foundation; plumbing, mechanical and "
    f"electrical rough (where the local program does them); floodplain "
    f"elevation where applicable; frame and masonry; final. <b>Ask for the "
    f"jurisdiction's own list</b> — the {sec('39-4117(1)')} process document "
    f"should carry it — and expect it to be longer."))
rows = [
    [k.cellp("<b>Who may inspect</b>"),
     k.cellp("State and local building inspectors hold ICC certification; "
             "one with only the residential certification \"may only inspect "
             "structures regulated by the International Residential Code\""),
     k.cellp(sec("39-4108"))],
    [k.cellp("<b>Virtual re-inspections</b>"),
     k.cellp("Allowed \"at their discretion\" after an in-person inspection; "
             "the address must be verified on camera; not for structural "
             "inspections on buildings of three stories or more"),
     k.cellp(sec("39-4119"))],
    [k.cellp("<b>Certificate of occupancy</b>"),
     k.cellp("IRC R110 as adopted, locally amendable. Where no building code "
             "is enforced, none exists and none can be requested — plan for "
             "a lender or insurer to ask, and keep every trade tag and the "
             "septic as-built instead"),
     k.cellp("—")],
    [k.cellp("<b>Appeals</b>"),
     k.cellp("Local: the IRC R112 board of appeals as the ordinance adopted "
             "it. The state Building Code Board hears appeals only for "
             "buildings \"within the jurisdiction of the division\" — not a "
             "house in an enforcing county. Trade correction notices: the "
             "chapters give the boards appeals of civil penalties only; ask "
             "the inspector's area supervisor in writing"),
     k.cellp(f"{sec('39-4107(2)')}; {sec('39-4120')}")],
]
flow.append(k.ref_table(
    "Around the building inspections",
    [k.cellp("", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.45 * inch, CW - 1.45 * inch - CITE, CITE]))

# ------------------------------------------------- septic and well
flow += k.h2_tight("SEPTIC AND WELL — THE OTHER TWO TRACKS", reserve=2.0)
rows = [
    [k.cellp("<b>Septic — site and test holes</b>"),
     k.cellp("\"If an inspection requires preparation, such as test hole "
             "excavation or partial construction of the system, the "
             "applicant or permittee must notify the Director at least "
             "<b>forty-eight (48) hours</b> in advance, excluding weekends "
             "and holidays\""),
     k.cellp("IDAPA 58.01.03.011.03")],
    [k.cellp("<b>Septic — final</b>"),
     k.cellp("\"No system may receive wastewater until the Director conducts "
             "a final installation inspection and completes as-built "
             "drawings\"; the as-built comes to you within 30 days. The "
             "permittee must uncover anything covered before inspection on "
             "request"),
     k.cellp("IDAPA 58.01.03.011.05, .011.02")],
    [k.cellp("<b>Well — driller's report</b>"),
     k.cellp("The driller keeps a daily log at the well site and files the "
             "report with IDWR \"within thirty (30) days following the "
             "completion of the well\""),
     k.cellp(sec("42-238(11)"))],
]
flow.append(k.ref_table(
    "Health district and IDWR",
    [k.cellp("", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.6 * inch, CW - 1.6 * inch - CITE, CITE]))

# ------------------------------------------------- log
# 2.6in: the log's first row carries a bold lead, a wrapped line and two
# field lines, so title + header + first row run ~2.3in; at 2.0in the heading
# sat alone at the foot of the page with the table on the next.
flow += k.h2_tight("INSPECTION LOG — RECORD EVERY REQUEST AND EVERY TAG",
                   reserve=2.6)
flow += k.check_table(
    "Every visit, whoever required it — the \"Requested\" date starts the "
    "48-business-hour clock",
    [
        ("<b>Septic site / test-hole inspection</b> — 48 hours' notice.",
         [("Requested", 0.34), ("Done", 0.33), ("Result", 0.33)]),
        ("<b>Temporary service</b> — option A, B or C above, and the date "
         "the meter was set.", [("Option", 0.3), ("Inspected", 0.35),
                                ("Meter set", 0.35)]),
        ("<b>Foundation / footing</b> — local, if a building code is "
         "enforced.", [("Requested", 0.34), ("Done", 0.33), ("Result", 0.33)]),
        ("<b>Plumbing groundwork</b> — DOPL code 203, before cover.",
         [("Requested", 0.34), ("Done", 0.33), ("Tag", 0.33)]),
        ("<b>HVAC work-in-progress</b> — anything to be concealed.",
         [("Requested", 0.34), ("Done", 0.33), ("Tag", 0.33)]),
        ("<b>Plumbing rough-in</b> — code 201, before concealment.",
         [("Requested", 0.34), ("Done", 0.33), ("Tag", 0.33)]),
        ("<b>Electrical cover</b> — nothing concealed until approved.",
         [("Requested", 0.34), ("Done", 0.33), ("Result", 0.33)]),
        ("<b>Frame</b> — local, if enforced. Envelope method: visual "
         "inspection items field-verified, or blower door booked.",
         [("Requested", 0.34), ("Done", 0.33), ("Result", 0.33)]),
        ("<b>Gas pressure test</b> — HVAC code 713; 20 psig for 20 minutes.",
         [("Requested", 0.34), ("Done", 0.33), ("Tag", 0.33)]),
        ("<b>Electrical final</b> — unlocks the meter.",
         [("Requested", 0.34), ("Done", 0.33), ("Result", 0.33)]),
        ("<b>Plumbing final</b> — code 204. <b>HVAC final</b> — code 704.",
         [("Plumbing tag", 0.5), ("HVAC tag", 0.5)]),
        ("<b>Septic final</b> and as-built received — no wastewater before "
         "this.", [("Done", 0.5), ("As-built received", 0.5)]),
        ("<b>Building final and certificate of occupancy</b>, if issued "
         "where I am building.", [("Final", 0.5), ("CO number", 0.5)]),
        ("Any inspection my jurisdiction requires that is not on this list — "
         "ask, and write it here:", [("Inspection", 0.5), ("Date", 0.5)]),
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "id-permit-kit",
                       "ID.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
