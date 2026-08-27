#!/usr/bin/env python3
"""MI.4 Where to File Directory.

Michigan has a single statewide construction code and no single permit
counter. Building, electrical, mechanical and plumbing are each assigned
SEPARATELY to a state, county or local enforcing agency, unit of government by
unit of government, and the assignment changes after every Construction Code
Commission meeting.

The counts printed in this document were derived by the author from the
Bureau of Construction Codes' Statewide Jurisdiction List, revision 8/21/2026,
read 27 August 2026: 1,824 units of government across all 83 counties, of
which 252 have at least one discipline assigned to a different agency than the
others. Per-discipline state counts: building 59, electrical 184, mechanical
241, plumbing 264.

Deliberately prints agency WEBSITES and lookup routes rather than phone
numbers — direct-dial numbers at county and township offices change often
enough that a printed number is a liability, and every block has a rule to
write the number you confirmed.
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

FORM_ID = "MI.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Michigan's hardest question is not what the rules are — it is who "
    "enforces them on your parcel. This document answers it, per trade, and "
    "gives you a page to write down what you confirmed.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- the problem
flow += k.h2_tight("ONE CODE, THREE POSSIBLE ENFORCERS, FOUR SEPARATE ANSWERS")
flow.append(k.body(
    "Michigan's construction code is a single statewide code. Its "
    "<b>administration</b> is not. Every unit of government in the state — "
    "every township, city and village — is listed against <b>four "
    "disciplines</b>: building, electrical, mechanical and plumbing. Each of "
    "the four is separately assigned to one of three levels."))

lvl_rows = [
    [k.cellp("<b>LOCAL</b>"),
     k.cellp("That city, township or village runs its own program and issues "
             "that permit itself.")],
    [k.cellp("<b>COUNTY</b>"),
     k.cellp("That unit of government receives code enforcement services "
             "from a county enforcing agency — so you file with the county, "
             "not the township.")],
    [k.cellp("<b>STATE</b>"),
     k.cellp("The Bureau of Construction Codes is responsible for code "
             "enforcement there. You file with the State of Michigan in "
             "Lansing, and a state inspector drives to your site.")],
]
flow.append(k.ref_table(
    "The three levels, in the Bureau's own words",
    [k.cellp("If the list says", bold=True),
     k.cellp("What it means", bold=True)],
    lvl_rows, [1.2 * inch, CW - 1.2 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "The mistake this document exists to prevent", [
        Paragraph("Because the four disciplines are assigned separately, "
                  "<b>your building permit and your plumbing permit may come "
                  "from different governments.</b> That is not a rare edge "
                  "case. Working through the Bureau's own list for all 1,824 "
                  "units of government in Michigan, <b>252 of them — about "
                  "one in seven — have at least one discipline assigned to a "
                  "different agency than the others.</b>", S["body"]),
        Paragraph("The pattern is lopsided in a way that matters to you. The "
                  "State is the <b>building</b> enforcing agency for only 59 "
                  "units of government, but the <b>plumbing</b> enforcing "
                  "agency for 264 and the <b>mechanical</b> enforcing agency "
                  "for 241. So the common rural case is not \"the state does "
                  "everything\" — it is a county building department that "
                  "will happily take your building permit, and a state "
                  "plumbing inspector out of Lansing who has never heard of "
                  "your project. Check all four before you file any of them.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- the list
flow += k.h2_tight("THE STATEWIDE JURISDICTION LIST — HOW TO USE IT")
flow.append(k.body(
    "The Bureau publishes the answer for every unit of government in "
    "Michigan in one PDF, free. It is the single most useful document in "
    "Michigan owner-building and almost nobody outside the trade knows it "
    "exists. Find it at <b>michigan.gov/lara</b> → Bureau of Construction "
    "Codes, where it is linked from every permit information page, or search "
    "\"<i>Michigan Statewide Jurisdiction List</i>.\""))

flow.append(k.checklist([
    "Find the <b>county</b> your parcel is in — the list is ordered by "
    "county, then by unit of government within it.",
    "Find your exact <b>unit of government</b>: the township, city or "
    "village your parcel sits in. This is not always the mailing address on "
    "your deed — a rural address often carries a nearby city's post office "
    "name while the parcel is in a township.",
    "Read <b>all four columns</b> across that one row — BLDG, ELEC, MECH, "
    "PLBG — and write each answer into the directory on the next page.",
    "Check for a <b>date under any column</b>. The list prints the effective "
    "date of a change directly below the level of jurisdiction, so a recent "
    "handover is visible on the row itself.",
    "Check for an <b>asterisk</b>. An asterisk means the Bureau is "
    "temporarily assisting a local agency; the detail is spelled out at the "
    "end of the list under \"Assistance to Local Enforcing Agency.\"",
]))
flow.append(Spacer(1, 6))

flow.append(k.callout("It changes — and it changed this year", [
    Paragraph("The Bureau updates the list \"<i>after every Construction "
              "Code Commission meeting to show changes; i.e. units of "
              "government which have newly assumed responsibility or those "
              "who have returned responsibility to the state or county "
              "level.</i>\" This is not a static reference.", S["body"]),
    Paragraph("A live example from the current revision: <b>every unit of "
              "government in Luce County — the county itself, the Village of "
              "Newberry, and its townships — moved to STATE enforcement for "
              "all four disciplines effective 01/01/2026.</b> An "
              "owner-builder there who relied on a two-year-old answer, or "
              "on what a neighbor did, would file with an office that no "
              "longer handles it. <b>Download the list the week you file, "
              "not the year you start planning.</b>", S["body"]),
]))
flow.append(k.cite(
    "Bureau of Construction Codes, <i>Statewide Jurisdiction List</i>, "
    "revision 8/21/2026, read 27 August 2026. Quotations are from the "
    "explanatory page at the front of that document. The counts in this "
    "document (1,824 units of government across 83 counties; 252 with a "
    "split assignment; state-enforced counts of 59 building, 184 electrical, "
    "241 mechanical, 264 plumbing) were derived by tallying that revision of "
    "the list and will drift as units of government change level — treat "
    "them as a picture of how common the problem is, not as a lookup. Your "
    "row is the only one that governs."))

# ---------------------------------------------------------------- other offices
flow += k.h2_tight("THE OFFICES THE JURISDICTION LIST DOES NOT COVER")
flow.append(k.body(
    "The list settles the four construction permits. It says nothing about "
    "the five environmental approvals in MI.2, and those are assigned by "
    "entirely different statutes — so they can land on a fifth and sixth "
    "office again."))

find_rows = [
    [k.cellp("<b>Zoning</b><br/>(use, setbacks, height, lot coverage)"),
     k.cellp("Always your <b>township, city or village</b> — never the "
             "State, and not preempted by the construction code. Search "
             "\"<i>[your township] MI zoning</i>.\" Ask for the setbacks in "
             "writing before you draw.")],
    [k.cellp("<b>County or district health department</b><br/>(septic, "
             "private well)"),
     k.cellp("Some Michigan counties have their own health department; many "
             "share a multi-county <b>district</b> health department. Search "
             "\"<i>[your county] MI health department environmental "
             "health</i>\" and confirm which body serves your county.")],
    [k.cellp("<b>Soil erosion (Part 91)</b>"),
     k.cellp("The <b>county</b> enforces throughout the county unless your "
             "municipality has adopted its own department-approved "
             "ordinance, which may be stricter. Ask the county first; they "
             "will tell you if your municipality has taken it over.")],
    [k.cellp("<b>County road commission</b><br/>(driveway / road tie-in)"),
     k.cellp("Michigan county road commissions are separate bodies from the "
             "county government and issue their own driveway permits. If you "
             "connect to a state trunkline (an I-, US- or M- numbered route) "
             "it is <b>MDOT</b> instead — michigan.gov/mdot.")],
    [k.cellp("<b>Fire district</b>"),
     k.cellp("Your local fire authority signs the fire district line on the "
             "permit application. On a rural parcel expect questions about "
             "access width, turnaround and water supply.")],
    [k.cellp("<b>EGLE</b><br/>(wetlands, inland lakes and streams, "
             "floodplain, shoreline)"),
     k.cellp("The Department of Environment, Great Lakes, and Energy — "
             "michigan.gov/egle — permits work in regulated wetlands, near "
             "inland lakes and streams, in floodplains, and on high-risk "
             "erosion and critical dune areas. If any part of your parcel is "
             "wet or near water, ask <i>before</i> you design the driveway.")],
]
flow.append(k.ref_table(
    "Finding the right office for your parcel",
    [k.cellp("Office", bold=True), k.cellp("How to find it", bold=True)],
    find_rows, [2.05 * inch, CW - 2.05 * inch]))

# ---------------------------------------------------------------- directory
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT")
flow.append(k.body(
    "Start with the four construction permits, because in Michigan they are "
    "four separate answers. Write the <b>level</b> you read off the "
    "Statewide Jurisdiction List (LOCAL, COUNTY or STATE) and then the "
    "office that level actually means for your parcel. Confirm each by phone "
    "rather than copying it from a search result, and note the name of the "
    "person you spoke to — in a township office, a name is worth more than a "
    "number."))


def permit_block(label, sub):
    """One of the four construction permits: level, office, portal."""
    return [
        Paragraph(f"<b>{label}</b> — <font size=9.5>{sub}</font>", S["body"]),
        d.FillInRow([("Level (LOCAL / COUNTY / STATE):", 0.5),
                     ("Office:", 0.5)]),
        d.FillInRow([("Portal / address:", 0.42), ("Spoke with:", 0.34),
                     ("Confirmed:", 0.24)]),
        Spacer(1, 4),
    ]


for label, sub in [
    ("BUILDING PERMIT", "plan review, footings through final, the CO"),
    ("ELECTRICAL PERMIT", "service, rough-in, final — often a different "
     "agency than building"),
    ("MECHANICAL PERMIT", "heating, ductwork, fuel gas"),
    ("PLUMBING PERMIT", "water, waste, vent, building sewer"),
]:
    flow += permit_block(label, sub)

flow.append(Spacer(1, 4))


def office_block(label, sub):
    """One supporting office: department and phone, then portal plus who/when."""
    return [
        Paragraph(f"<b>{label}</b> — <font size=9.5>{sub}</font>", S["body"]),
        d.FillInRow([("Office / department:", 0.62), ("Phone:", 0.38)]),
        d.FillInRow([("Portal / address:", 0.44), ("Spoke with:", 0.34),
                     ("Confirmed:", 0.22)]),
        Spacer(1, 4),
    ]


for label, sub in [
    ("ZONING", "township / city / village — setbacks, use, address assignment"),
    ("HEALTH DEPARTMENT", "septic and private well — county or district"),
    ("SOIL EROSION (PART 91)", "county, unless your municipality has assumed it"),
    ("COUNTY ROAD COMMISSION", "driveway permit — or MDOT on a state trunkline"),
    ("FIRE DISTRICT", "access, turnaround, water supply"),
    ("ELECTRIC UTILITY", "temporary construction power and permanent service"),
    ("WATER &amp; SEWER", "public connection, tap fees — or N/A if well/septic"),
]:
    flow += office_block(label, sub)

# ---------------------------------------------------------------- state level
flow += k.h2_tight("STATE-LEVEL CONTACTS")
flow.append(k.body(
    "These are stable and worth knowing. Phone numbers are left for you to "
    "confirm — a wrong number printed in a kit is worse than no number."))

state_rows = [
    [k.cellp("<b>LARA Bureau of Construction Codes</b>"),
     k.cellp("Publishes the Statewide Jurisdiction List and the code rules; "
             "issues permits and inspects wherever the list says STATE; "
             "licenses residential builders and the skilled trades. Also "
             "where you verify that a contractor you are hiring is actually "
             "licensed."),
     k.cellp("michigan.gov/bcc")],
    [k.cellp("<b>Michigan Construction Code Commission</b>"),
     k.cellp("Hears construction code appeals, and is the body whose "
             "meetings trigger each revision of the Statewide Jurisdiction "
             "List. Reached through the Bureau."),
     k.cellp("michigan.gov/bcc")],
    [k.cellp("<b>Michigan Legislature</b>"),
     k.cellp("The statutes themselves, free and current: the Occupational "
             "Code (1980 PA 299, Article 24 — residential builders), the "
             "Stille-DeRossett-Hale Act (1972 PA 230 — permits, enforcing "
             "agencies), and NREPA Part 91 (1994 PA 451 — soil erosion)."),
     k.cellp("legislature.mi.gov")],
    [k.cellp("<b>EGLE</b>"),
     k.cellp("Wetlands, inland lakes and streams, floodplain, high-risk "
             "erosion and critical dune permits; the state radon program."),
     k.cellp("michigan.gov/egle")],
]
flow.append(k.ref_table(
    "State agencies and what each is actually for",
    [k.cellp("Agency", bold=True), k.cellp("Why you would contact them", bold=True),
     k.cellp("Website", bold=True)],
    # 1.25in split "legislature.mi.gov" and "michigan.gov/bcc" mid-word.
    state_rows, [1.65 * inch, CW - 1.65 * inch - 1.55 * inch, 1.55 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026). The three jurisdiction levels "
    "and the update cadence: Bureau of Construction Codes, <i>Statewide "
    "Jurisdiction List</i>, explanatory page, rev. 8/21/2026. Application "
    "goes to \"the appropriate enforcing agency\": MCL 125.1510(1), and the "
    "Bureau's own instruction on form BCC-324 (04/2024) — \"<i>A permit "
    "application must be submitted to the appropriate enforcing agency based "
    "upon these lists.</i>\" Soil erosion is enforced by the county "
    "throughout the county unless a municipality has an approved ordinance: "
    "MCL 324.9105(1), 324.9106. Statutes at legislature.mi.gov."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "mi-permit-kit",
                       "MI.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
