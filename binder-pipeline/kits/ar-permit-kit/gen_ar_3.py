#!/usr/bin/env python3
"""AR.3 Inspection Sequence.

Split into the approvals that happen wherever you build and the building
inspections that happen only where a local government created a permit office.

Verified sources:
  Ark. Code Ann. § 17-38-204(b),(c),(f)(1)  plumbing permits and inspections are
              MANDATORY wherever a water, sewer or gas utility system exists —
              "shall establish" — and the Department of Health may take "immediate
              charge and entire control" where no local inspector was provided
  Ark. Code Ann. § 17-28-305(a),(c),(d)     electrical permitting is LOCAL
              OPTION ("may"); an electrical inspector must hold a state license;
              a city may not re-examine a state-licensed electrician
  17 CAR § 210-1101(a)  a state electrical inspector may require concealed work
              to be EXPOSED, including removing sheetrock, where the work was
              not subject to city inspection and there is evidence of serious
              violations
  AFPC Vol. III § R109.1.1 to R109.1.6  the required inspections — VERIFIED
              UNAMENDED by Arkansas, so this is the list a local program follows
  AFPC Vol. III § R110  certificate of occupancy, also unamended
  Onsite Wastewater Rules § 4.7, § 4.10.2, § 4.10.3  24 hours' notice, the
              installation inspection and its 5-day paperwork, and the Permit
              for Operation without which the system may not be used
  17 CAR § 11-401  well construction report within 90 days, with longitude and
              latitude; § 11-403 a copy to the customer on demand

DELIBERATELY NOT CLAIMED:
  - That a utility will or will not connect without an inspection. That is a
    utility business practice, varies by co-op, and no state primary source
    establishes it. The document tells the reader to ask their provider and
    gives them a line to write the answer on.
  - Any statutory inspection clock. Arkansas sets no re-inspection deadline for
    residential building inspections that could be verified.
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

FORM_ID = "AR.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The order things get looked at — and who does the looking when your "
    "county has no building department.")

flow.append(k.disclaimer(
    "The inspection list below is the one the Arkansas residential code sets "
    "out; whether anyone performs it depends on your jurisdiction."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- why
flow += k.h2_tight("WHY ARKANSAS HAS NO SINGLE LIST OF INSPECTIONS",
                   reserve=1.6)
flow.append(k.body(
    "Every other document in this kit turns on the same fact, and inspections "
    "are where it bites hardest. Arkansas has <b>one</b> residential code and "
    "<b>three</b> different possible answers to \"who inspects this?\" — and "
    "which one you get depends on the line your parcel sits on."))
rows = [
    [k.cellp("<b>Inside a city that permits</b>"),
     k.cellp("The full set. Building, trades, and a certificate of occupancy — "
             "the sequence in the middle of this document")],
    [k.cellp("<b>A county with a building department</b>"),
     k.cellp("The same sequence, run by the county. A minority of Arkansas "
             "counties; do not assume yours is one")],
    [k.cellp("<b>Most unincorporated Arkansas</b>"),
     k.cellp("<b>No building inspection at all.</b> But the septic "
             "inspections still happen, the plumbing inspection may be "
             "mandatory, and the electric utility still has to be satisfied "
             "before it energizes anything")],
]
flow.append(k.ref_table(
    "Three answers to one question",
    [k.cellp("Where you are", bold=True),
     k.cellp("Who inspects", bold=True)],
    rows, [2.15 * inch, CW - 2.15 * inch]))

# ---------------------------------------------------------------- always
# 2.6in, not 1.8: this heading is followed by a two-line lead paragraph before
# its table, and at 1.8 the heading kept the first line of that paragraph and
# nothing else at the foot of page 1.
flow += k.h2_tight("THE APPROVALS THAT HAPPEN WHEREVER YOU BUILD",
                   reserve=2.6)
flow.append(k.body(
    "These are not building inspections and they are not optional. Work them "
    "in this order."))
flow += k.check_table(
    "The ones that do not depend on your county",
    [
        ("<b>Septic — notify before you start.</b> The Authorized Agent must "
         "be notified <b>at least 24&#160;hours</b> before work begins on the "
         "system (Onsite Wastewater Rules § 4.7).",
         [("Date notified", 1.0)]),
        ("<b>Septic — installation inspection (Part II).</b> Performed by the "
         "Environmental Health Specialist, or by the Designated "
         "Representative with the Authorized Agent's approval. Documentation "
         "reaches the local health unit within <b>5 days</b> (§ 4.10.2).",
         [("Date", 0.45), ("Inspector", 0.55)]),
        ("<b>Septic — Permit for Operation (Part III).</b> \"The system shall "
         "not be used until the Permit for Operation is issued\" (§ 4.10.3). "
         "Until this exists you do not have a legal toilet.",
         [("Issued", 1.0)]),
        ("<b>Plumbing inspection</b> — mandatory wherever a water, sewer or "
         "gas utility system exists. See the section below.",
         [("Date", 0.45), ("Result", 0.55)]),
        ("<b>Well construction report</b> — due within <b>90 days</b> of "
         "completion, must carry the well's longitude and latitude, and a "
         "copy must be provided to you on demand (17 CAR § 11-401, § 11-403). "
         "<b>Demand it.</b> It is your only record of depth, casing and "
         "static level.", [("Date filed", 1.0)]),
        ("<b>Floodplain</b> — if you are in a flood hazard area, the code "
         "requires an inspection when the lowest floor is placed and before "
         "further vertical construction (AFPC Vol. III § R109.1.3), and your "
         "local floodplain administrator will have its own requirements.",
         [("Date", 0.45), ("Office", 0.55)]),
    ])

# ---------------------------------------------------------------- plumbing
flow += k.h2_tight("THE PLUMBING INSPECTION — THE MANDATORY ONE", reserve=2.0)
flow.append(k.body(
    "This is the part of Arkansas law most likely to catch out someone who has "
    "read that rural Arkansas is unregulated. Plumbing is the one trade where "
    "the statute uses <b>shall</b>."))
flow.append(k.callout_long(
    f"Ark. Code Ann. {sec('17-38-204')}", [
        Paragraph("\"(b) A plumbing installation shall not be: (1) Installed "
                  "in any building within this state except in accordance "
                  "with or exceeding the minimum requirements of the "
                  "department; or (2) <b>Started without the prescribed "
                  "licenses, permits, and acceptable plan review of plumbing "
                  "plans and specifications when required.</b>", S["body"]),
        Paragraph("(c) A city, town, sewerage district, water district, sewer "
                  "association, water association, utility gas system, or "
                  "county having a system of either water, sewerage, or gas "
                  "utility, or a combination of utilities, <b>shall establish "
                  "a system of permits and inspections</b> to assure that the "
                  "public health and safety is protected.\"", S["body"]),
        Paragraph("And where such a utility system exists but nobody was "
                  "appointed to inspect, the Department of Health \"<b>may "
                  "take immediate charge and entire control of the plumbing "
                  "inspection program</b>\" (§ 17-38-204(f)(1)). The "
                  "Department publishes which counties its own state plumbing "
                  "inspectors cover.", S["body"]),
    ]))
flow.append(k.body(
    "Read that against the electrical statute in the next section and the "
    "asymmetry is stark. <b>The trigger is the utility system, not the city "
    "limit.</b> A rural water association serving your parcel is enough to "
    "pull the mandatory-permit language into play — so the question to ask is "
    "not \"am I in a city?\" but \"who supplies my water, sewer or gas, and do "
    "they run a plumbing permit and inspection program?\""))
flow += k.check_table(
    "Settle this before the plumber starts",
    [
        ("Who supplies water to this parcel — a city, a rural water "
         "association, or my own well?", [("Answer", 1.0)]),
        ("Does that body run a plumbing permit and inspection program? If it "
         "has a utility system, the statute says it shall.",
         [("Answer", 1.0)]),
        ("If nobody local inspects, does a state plumbing inspector cover this "
         "county?", [("Answer", 1.0)]),
        ("The plumbing code applies statewide regardless — confirm the plumber "
         "holds a current Department of Health license.",
         [("License no.", 0.55), ("Verified", 0.45)]),
    ])

# ---------------------------------------------------------------- electrical
flow += k.h2_tight("THE ELECTRICAL QUESTION — OPTIONAL, WITH A STING",
                   reserve=2.0)
flow.append(k.body(
    f"Electrical permitting is local option: \"Any city or county <b>may</b> "
    f"establish by ordinance, rules, and regulations a system of permits and "
    f"inspections for the installation, repair, and maintenance of electrical "
    f"facilities and electrical work\" ({sec('17-28-305(c)')}). Where no city "
    f"or county opted in, there is no electrical permit to pull."))
flow.append(k.body(
    "Two things follow that people get wrong in opposite directions."))
flow.append(k.bullet(
    "<b>The code still applies.</b> The 2026 National Electrical Code is the "
    "adopted statewide standard for the performance of electrical work (17 CAR "
    "§ 210-401). No permit does not mean no rules — it means nobody is "
    "checking on a schedule."))
flow.append(k.bullet(
    "<b>And Arkansas kept a way to check anyway.</b> A state electrical "
    "inspector \"may require electrical work to be exposed for inspection, "
    "<b>including the removal of sheetrock</b>\" where the work was not "
    "subject to inspection by a city and there is evidence of serious "
    "violations (17 CAR § 210-1101(a)). It is not a routine inspection "
    "program — but it is a real power, and it lands after your walls are "
    "closed."))
flow.append(k.callout(
    "The inspector you will actually meet is your electric utility", [
        Paragraph("In an area with no local electrical permit program, the "
                  "practical gate on your build is the utility or co-op that "
                  "energizes the service. What it requires before it connects "
                  "— an inspection, a licensed electrician's certification, a "
                  "particular meter base — is a <b>business practice of that "
                  "utility</b>, not a state rule, and it varies from one "
                  "co-op to the next. We are not going to guess yours. Ask "
                  "them early, in writing, because the answer determines when "
                  "you can close walls.", S["body"]),
    ]))
flow += k.check_table(
    "Ask your electric provider before you rough anything in",
    [
        ("Which utility or co-op serves this parcel?", [("Name", 1.0)]),
        ("What does it require before it will energize permanent service?",
         [("Answer", 1.0)]),
        ("Does it require inspection by a state-licensed electrical "
         "inspector? If so, who?", [("Answer", 1.0)]),
        ("Temporary construction power — what is needed, and when to apply",
         [("Answer", 1.0)]),
        ("Service entrance specification — meter base, mast height, location",
         [("Answer", 1.0)]),
    ])
flow.append(k.cite(
    f"One protection worth knowing: a state-licensed electrician \"shall not "
    f"be subject to examination or licensing by any city or county in order to "
    f"perform electrical work\" ({sec('17-28-305(a)')}), and whoever does "
    f"inspect must themselves hold a state inspector license "
    f"({sec('17-28-305(d)')}). A city can require a permit; it cannot make "
    f"your electrician re-qualify locally."))

# ---------------------------------------------------------------- building
flow += k.h2_tight("THE BUILDING INSPECTIONS — IF SOMEBODY REQUIRES THEM",
                   reserve=2.0)
flow.append(k.body(
    "Where a permit program exists, this is the sequence, and it is worth "
    "knowing that Arkansas did <b>not</b> amend it. The list below is the "
    "Arkansas residential code's own, so a local program is working from "
    "exactly these headings."))
rows = [
    [k.cellp("<b>1</b>", center=True), k.cellp("<b>Foundation</b>"),
     k.cellp("\"after poles or piers are set or trenches or basement areas are "
             "excavated\" — before you pour"),
     k.cellp("R109.1.1")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("<b>Plumbing, mechanical, gas and electrical rough</b>"),
     k.cellp("\"prior to covering or concealment\". Note the code groups all "
             "four; in Arkansas they may be inspected by different offices, or "
             "by nobody"),
     k.cellp("R109.1.2")],
    [k.cellp("<b>3</b>", center=True), k.cellp("<b>Floodplain</b>"),
     k.cellp("In flood hazard areas, \"upon placement of the lowest floor… "
             "prior to further vertical construction\""),
     k.cellp("R109.1.3")],
    [k.cellp("<b>4</b>", center=True), k.cellp("<b>Frame and masonry</b>"),
     k.cellp("\"after the roof, masonry, framing… are in place\" — the "
             "inspection everything else waits on"),
     k.cellp("R109.1.4")],
    [k.cellp("<b>5</b>", center=True), k.cellp("<b>Any other inspection</b>"),
     k.cellp("\"The building official shall have the authority to make or "
             "require any other inspections to ascertain compliance\""),
     k.cellp("R109.1.5")],
    [k.cellp("<b>6</b>", center=True), k.cellp("<b>Final</b>"),
     k.cellp("\"after the permitted work is complete and <b>prior to "
             "occupancy</b>\""),
     k.cellp("R109.1.6")],
]
flow.append(k.ref_table(
    "Arkansas Fire Prevention Code, Volume III — required inspections",
    [k.cellp("#", bold=True, center=True), k.cellp("Inspection", bold=True),
     k.cellp("What the code says", bold=True), k.cellp("Cite", bold=True)],
    rows, [0.35 * inch, 1.85 * inch, CW - 3.15 * inch, 0.95 * inch]))
flow.append(k.cite(
    "AFPC Volume III, § R109.1.1 to § R109.1.6, read September 2026 and "
    "confirmed carrying no Arkansas amendment. The certificate of occupancy "
    "provision at § R110 is likewise unamended. A local program may add "
    "inspections under R109.1.5 — insulation and sheathing are the usual "
    "additions — so ask for the office's own list at the counter."))

# ---------------------------------------------------------------- nobody
flow += k.h2_tight("WHEN NOBODY IS REQUIRED TO INSPECT YOU", reserve=2.0)
flow.append(k.body(
    "This is the situation most buyers of this kit are actually in, and it "
    "deserves a straight answer rather than a warning label. Nothing legally "
    "obliges you to have the framing looked at. Several things make it a bad "
    "idea to skip."))
flow.append(k.bullet(
    "<b>The code still applies to the house.</b> The Arkansas Fire Prevention "
    "Code is adopted statewide and its residential volume reaches your "
    "dwelling by its own scope. What is missing is the inspection, not the "
    "standard — and not your liability for falling short of it."))
flow.append(k.bullet(
    "<b>You will be asked what it was built to.</b> Appraisers, insurers, "
    "mortgage underwriters and eventually a buyer all ask. A build with no "
    "permit, no inspection record and no photographs is worth arguing about; a "
    "build with a documented inspection log is not."))
flow.append(k.bullet(
    "<b>Hire the inspections you are not required to have.</b> A private "
    "third-party inspection at foundation, rough-in and frame costs a small "
    "fraction of what opening a finished wall costs. In northeast Arkansas — "
    "the New Madrid seismic country — and anywhere with the state's expansive "
    "clay, an engineered foundation is money spent on physics, which does not "
    "care whether anyone issued a permit."))
flow.append(k.bullet(
    "<b>Photograph everything before it is covered.</b> Trenches open, "
    "reinforcement placed, every rough-in run, insulation before drywall. Date "
    "them. This log plus that photo set is the record you will wish you had."))

# ---------------------------------------------------------------- log
flow += k.h2_tight("INSPECTION LOG — RECORD EVERY ONE", reserve=1.6)
flow += k.check_table(
    "Whether or not anybody required it",
    [
        ("Septic — 24-hour notice given", [("Date", 1.0)]),
        ("Septic — installation inspection (Part II)",
         [("Date", 0.45), ("By", 0.55)]),
        ("Septic — Permit for Operation (Part III)", [("Date", 1.0)]),
        ("Foundation / footing", [("Date", 0.45), ("By", 0.55)]),
        ("Foundation — engineer's observation, if used",
         [("Date", 0.45), ("By", 0.55)]),
        ("Floodplain — lowest floor elevation", [("Date", 0.45), ("By", 0.55)]),
        ("Plumbing rough-in", [("Date", 0.45), ("By", 0.55)]),
        ("Electrical rough-in", [("Date", 0.45), ("By", 0.55)]),
        ("Mechanical and gas rough-in", [("Date", 0.45), ("By", 0.55)]),
        ("Frame and masonry", [("Date", 0.45), ("By", 0.55)]),
        ("Insulation, before drywall", [("Date", 0.45), ("By", 0.55)]),
        ("Electric utility — service energized",
         [("Date", 0.45), ("By", 0.55)]),
        ("Final plumbing", [("Date", 0.45), ("By", 0.55)]),
        ("Final electrical", [("Date", 0.45), ("By", 0.55)]),
        ("Final mechanical", [("Date", 0.45), ("By", 0.55)]),
        ("Final building", [("Date", 0.45), ("By", 0.55)]),
        ("Certificate of occupancy, if issued here", [("Date", 1.0)]),
    ],
    notes_header="Result / notes")
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ar-permit-kit",
                       "AR.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
