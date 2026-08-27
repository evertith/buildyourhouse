#!/usr/bin/env python3
"""KY.4 Where to File Directory.

Kentucky's hard question is not which code applies — one mandatory code applies
everywhere — but whether anyone will inspect your house at all, and if so who.

The counts printed in this document were derived by the author from the
Department of Housing, Buildings and Construction's own per-county inspector
sheets at dhbc.ky.gov (HOW DO I? -> Contact an Inspector), all of which were
downloaded and tallied on 27 August 2026: 119 sheets published for Kentucky's
120 counties (Gallatin has none); 25 sheets print "None" for Local Building
Inspector, 6 leave the field empty and 10 carry no such line at all, so 41 of
the 119 show no local building inspector. Several of the remaining 78 name an
inspector for a city only, so 78 overstates county-wide coverage.

Deliberately prints agency WEBSITES and lookup routes rather than phone
numbers — the county sheets carry direct-dial and cell numbers for named
individuals, which change constantly, and a stale number printed in a kit is
worse than none. Every block has a rule to write down what you confirmed.
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

FORM_ID = "KY.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Kentucky's hardest question is not what the rules are — it is whether "
    "anyone will inspect your house, and who. This document answers it and "
    "gives you a page to write down what you confirmed.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- the problem
flow += k.h2_tight("ONE CODE, AND UP TO SIX DIFFERENT ANSWERS")
flow.append(k.body(
    "The Kentucky Residential Code is the same in all 120 counties. Who "
    "enforces it is not. On a single parcel you can be dealing with a county "
    "building inspector, a city building inspector, a <b>state</b> plumbing "
    "inspector out of Frankfort, a state or local HVAC inspector, a certified "
    "electrical inspector arranged through your county judge/executive, and a "
    "health department environmentalist — and in much of the state, no "
    "building inspector at all."))

lvl_rows = [
    [k.cellp("<b>Building</b>"),
     k.cellp("<b>Local, or nobody.</b> Only if your city or county passed an "
             "ordinance requiring permits and inspections for single-family "
             "dwellings. The State is barred from filling the gap. "
             "(KRS 198B.060(1), (4)(b))")],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp("<b>State by default.</b> The permit comes from the Department of "
             "Housing, Buildings and Construction. A local government that has "
             "been authorized may issue instead, and its permit \"<i>shall be "
             "deemed a permit issued by the department</i>\" — but the "
             "department keeps concurrent jurisdiction. (KRS 318.134(1)(a); "
             "318.140(1))")],
    [k.cellp("<b>HVAC</b>"),
     k.cellp("<b>State, or a local program that already existed in 2007.</b> "
             "No local government may start a new HVAC permitting or "
             "inspection program — the door closed on January 1, 2007. "
             "(KRS 198B.6671(1); 198B.6673(2), (4))")],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("<b>A certified electrical inspector</b> — employed by, or "
             "contracted with, the local government, or a state inspector. "
             "Your power company cannot connect you permanently without their "
             "final certificate of approval. (KRS 198B.060(11))")],
    [k.cellp("<b>Septic</b>"),
     k.cellp("<b>Your county health department</b>, under the Cabinet for "
             "Health and Family Services. Its permit must accompany your "
             "state plumbing application. (KRS 318.134(2))")],
    [k.cellp("<b>Zoning</b>"),
     k.cellp("<b>City or county planning</b> — an entirely separate question "
             "from building permits, and not answered by any of the above. "
             "Many Kentucky counties have zoning but no building permits")],
]
flow.append(k.ref_table(
    "Six questions, six possible offices",
    [k.cellp("Permit or approval", bold=True),
     k.cellp("Who handles it", bold=True)],
    lvl_rows, [1.15 * inch, CW - 1.15 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout_long(
    "The mistake this document exists to prevent", [
        Paragraph("Owner-builders arriving in Kentucky from a state with "
                  "universal permitting assume that somebody, somewhere, will "
                  "tell them what to do. In much of Kentucky nobody will — and "
                  "the reason is statutory, not administrative. Permits, "
                  "inspections and certificates of occupancy are not mandatory "
                  "for a single-family residence unless the local government "
                  "passed an ordinance, and the department \"<i>shall not "
                  "preempt or assert jurisdiction for the enforcement of the "
                  "code on single-family dwellings</i>.\"", S["body"]),
        Paragraph("<b>Working through the Department's own county inspector "
                  "sheets — all 119 of them — 25 print \"None\" for Local "
                  "Building Inspector, 6 carry the heading with nothing after "
                  "it, and 10 have no such line at all. That is 41 of 119, "
                  "about one county in three.</b> The 25 word it in a way that "
                  "says everything: \"<i>None / For Commercial construction "
                  "Contact Dept. Housing, Buildings Construction for building "
                  "permits</i>.\" The State will handle a warehouse there. For "
                  "your house, there is nobody.", S["body"]),
        Paragraph("<b>And the other 78 overstate the coverage.</b> Several "
                  "name an inspector for a city only — the sheets say things "
                  "like \"City Limits ONLY\" or \"(No County Building "
                  "Inspector)\" — so a named inspector on your county's sheet "
                  "does not mean the whole county is covered. If your parcel "
                  "is outside the city limits, ask again.", S["body"]),
        Paragraph("<b>Treat all of this as a measure of how common the gap is, "
                  "not as a lookup.</b> The sheets are a contact list of "
                  "inspectors, not a register of ordinances: a city inside one "
                  "of those counties may still require permits, and a county "
                  "with a named inspector may still not require them for "
                  "houses. Only your own city and county can tell you which "
                  "side of the line your parcel is on — which is why the first "
                  "checklist in KY.1 is two phone calls.", S["body"]),
    ]))

# ---------------------------------------------------------------- the sheets
flow += k.h2_tight("THE COUNTY INSPECTOR SHEET — KENTUCKY'S BEST-KEPT SECRET")
flow.append(k.body(
    "The Department publishes a <b>one-page PDF for every county</b> naming "
    "the actual people who inspect there: your state electrical inspector, "
    "your plumbing inspector and the hours they keep, the HVAC inspector, the "
    "health department environmentalist who handles your septic, and whether a "
    "local building inspector exists at all. It is free, it is current, and "
    "almost nobody outside the trade knows it exists."))
flow.append(k.body(
    "Find it at <b>dhbc.ky.gov</b> → <b>HOW DO I?</b> → <b>Contact an "
    "Inspector</b>, then click your county."))

flow.append(k.checklist([
    "Open <b>your county's sheet</b> and read the <b>Local Building "
    "Inspector</b> line first. If it says <i>None</i>, or the line is not "
    "there at all, your county has no local building inspector — go back to "
    "KY.1 and confirm with your city and county whether any permit ordinance "
    "applies to you.",
    "Write down the <b>Plumbing Inspector</b> and — this is the useful part — "
    "the <b>office hours and office address</b> printed underneath. In most "
    "counties that address is the <b>county health department</b>, which is "
    "also where your septic permit comes from. Two of your approvals live in "
    "the same building.",
    "Write down the <b>State Electrical Inspector</b>. Every published sheet "
    "names one. Where the sheet says \"<i>Local Electrical Inspector: contact "
    "the County Judge Executive's office or City office where work is to be "
    "performed</i>,\" that is the real answer for most of rural Kentucky — "
    "start with the judge/executive's office.",
    "Write down the <b>HVAC Inspector</b> and the <b>Health Dept. "
    "Environmentalist</b>.",
    "Check the <b>\"Updated\" date</b> in the bottom corner. Most sheets were "
    "revised in 2026, but some are older — if yours is, confirm the names "
    "before you rely on them.",
    "<b>Building in Gallatin County?</b> There is no published sheet for it. "
    "Contact the Department directly and write the answers below.",
]))
flow.append(Spacer(1, 6))
flow.append(k.cite(
    "Department of Housing, Buildings and Construction county inspector "
    "sheets, dhbc.ky.gov → Contact an Inspector, all downloaded and tallied "
    "27 August 2026: <b>119 sheets published for 120 counties</b> — Gallatin "
    "has none. Of the 119, <b>25 print \"None\"</b> for Local Building "
    "Inspector, <b>6 leave the field empty</b> and <b>10 carry no such line</b> "
    "— 41 in total — while 78 name someone, several of them for a city only. "
    "117 sheets carry an update stamp: 70 revised in 2026, 41 in 2025, 6 in "
    "2024. The classification of the agency's wording is the author's; sheet "
    "formats vary, and some counties combine roles."))

# ---------------------------------------------------------------- other offices
flow += k.h2_tight("THE OFFICES THE COUNTY SHEET DOES NOT COVER")
flow.append(k.body(
    "The sheet settles the inspectors. It says nothing about the approvals "
    "that are not inspections — and on a rural Kentucky parcel those are "
    "usually the ones that take the longest."))

find_rows = [
    [k.cellp("<b>Zoning and planning</b><br/>(use, setbacks, lot size, "
             "subdivision)"),
     k.cellp("Your <b>city or county planning commission</b>, or the county "
             "judge/executive's office where there is no commission. Entirely "
             "separate from building permits — a county with no building "
             "permit may still have zoning, and a county with zoning may have "
             "no building permit. Ask for setbacks in writing before you "
             "draw.")],
    [k.cellp("<b>911 address assignment</b>"),
     k.cellp("Usually the <b>county 911 or emergency services office</b>, "
             "sometimes the property valuation administrator. You will need "
             "an address before the utilities will set an account, so do this "
             "early rather than late.")],
    [k.cellp("<b>Driveway / entrance permit</b>"),
     k.cellp("If you tie in to a <b>state-maintained route</b>, the Kentucky "
             "Transportation Cabinet's district office issues the encroachment "
             "or entrance permit — <b>transportation.ky.gov</b>. If the road "
             "is county-maintained, it is the county road department. Confirm "
             "which authority owns your road before assuming.")],
    [k.cellp("<b>Floodplain</b>"),
     k.cellp("Kentucky administers floodplain construction at the "
             "<b>state</b> level through the Energy and Environment Cabinet's "
             "Division of Water — <b>eec.ky.gov</b>. This can apply even where "
             "your county has no building permit and no local floodplain "
             "ordinance, so check your parcel against the flood maps before "
             "you buy, not after.")],
    [k.cellp("<b>Septic and private well</b>"),
     k.cellp("Your <b>county health department</b>, under the Cabinet for "
             "Health and Family Services — <b>chfs.ky.gov</b>. The "
             "environmentalist named on your county inspector sheet is the "
             "person. Start here first: the septic permit gates the state "
             "plumbing permit by statute.")],
    [k.cellp("<b>Electric utility</b>"),
     k.cellp("Your rural electric cooperative or investor-owned utility. They "
             "need the certified electrical inspector's <b>final certificate "
             "of approval</b> before permanent service, and they set their own "
             "requirements for the service point, meter base and pole. Ask for "
             "their construction requirements in writing at the start.")],
    [k.cellp("<b>Water district</b>"),
     k.cellp("If you are on public water rather than a well, the water "
             "district cannot give you permanent service until the plumbing is "
             "approved (KRS 318.165). Tap fees are theirs and are often the "
             "largest single permit-related cost on the job.")],
]
flow.append(k.ref_table(
    "Finding the right office for your parcel",
    [k.cellp("Office", bold=True), k.cellp("How to find it", bold=True)],
    find_rows, [1.95 * inch, CW - 1.95 * inch]))

# ---------------------------------------------------------------- directory
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT")
flow.append(k.body(
    "Start with the question that governs everything else, then work down. "
    "Confirm each answer with the office itself rather than copying it from a "
    "search result, and note the name of the person you spoke to — in a county "
    "office a name is worth more than a number."))

# pack_fields rather than a hand-split FillInRow: at a fixed 0.62/0.38 split the
# long "Does your CITY require…" label ran into the next label's rule.
flow.append(Paragraph(
    "<b>THE QUESTION THAT GOVERNS EVERYTHING ELSE</b> — "
    "<font size=9.5>does a building permit exist where you are building?</font>",
    S["body"]))
flow += k.pack_fields([("City requires a building permit? (Y/N):", 0),
                       ("Confirmed with:", 0)], CW)
flow += k.pack_fields([("County requires one? (Y/N):", 0),
                       ("Confirmed with:", 0)], CW)
flow.append(Spacer(1, 8))


def office_block(label, sub):
    """One office: its label glued to its two write-in rows.

    KeepTogether because platypus will otherwise leave the bold label alone at
    the foot of a page with its rules overleaf — which happened to CERTIFIED
    ELECTRICAL INSPECTOR, and reads as a heading with nothing under it.
    """
    from reportlab.platypus import KeepTogether
    return [KeepTogether([
        Paragraph(f"<b>{label}</b> — <font size=9.5>{sub}</font>", S["body"]),
        d.FillInRow([("Office / person:", 0.62), ("Phone:", 0.38)]),
        d.FillInRow([("Portal / address:", 0.44), ("Spoke with:", 0.34),
                     ("Confirmed:", 0.22)]),
    ]), Spacer(1, 4)]


for label, sub in [
    ("BUILDING PERMIT", "city or county — or write NONE REQUIRED"),
    ("STATE PLUMBING INSPECTOR", "name, office hours and office address from "
     "your county sheet"),
    ("HVAC INSPECTOR", "state, or a local program predating 2007"),
    ("CERTIFIED ELECTRICAL INSPECTOR", "the final certificate of approval your "
     "power company needs"),
    ("HEALTH DEPARTMENT", "septic permit and the environmentalist's name"),
    ("ZONING / PLANNING", "setbacks, use, lot requirements"),
    ("911 ADDRESSING", "you need the address before the utilities will set an "
     "account"),
    ("ROAD / DRIVEWAY PERMIT", "Transportation Cabinet district, or county "
     "road department"),
    ("ELECTRIC UTILITY", "temporary construction power and permanent service"),
    ("WATER &amp; SEWER", "public connection and tap fees — or N/A if well and "
     "septic"),
]:
    flow += office_block(label, sub)

# ---------------------------------------------------------------- state level
flow += k.h2_tight("STATE-LEVEL CONTACTS")
flow.append(k.body(
    "These are stable and worth knowing. Phone numbers are left for you to "
    "write in — a wrong number printed in a kit is worse than no number."))

state_rows = [
    [k.cellp("<b>Department of Housing, Buildings and Construction</b>"),
     k.cellp("Publishes the county inspector sheets and the currently-adopted "
             "code list; issues the state plumbing and HVAC permits; licenses "
             "electricians, plumbers and HVAC contractors and certifies "
             "electrical and building inspectors. Also where you verify that a "
             "contractor you are hiring actually holds the license they claim."),
     k.cellp("dhbc.ky.gov")],
    [k.cellp("<b>Kentucky General Assembly</b>"),
     k.cellp("The statutes and regulations themselves, free and current: KRS "
             "Chapter 198B (building code), 227A (electrical), 318 (plumbing), "
             "and KAR Title 815 (Housing, Buildings and Construction)."),
     k.cellp("apps.legislature.ky.gov")],
    [k.cellp("<b>Cabinet for Health and Family Services</b>"),
     k.cellp("On-site sewage disposal — the septic permit that must accompany "
             "your state plumbing application — administered through your "
             "county health department."),
     k.cellp("chfs.ky.gov")],
    [k.cellp("<b>Energy and Environment Cabinet</b>"),
     k.cellp("Division of Water: floodplain construction, stream crossings, "
             "water well driller certification and construction stormwater "
             "permits."),
     k.cellp("eec.ky.gov")],
    [k.cellp("<b>Kentucky Transportation Cabinet</b>"),
     k.cellp("Entrance and encroachment permits where a driveway meets a "
             "state-maintained route. Work through the district office that "
             "covers your county."),
     k.cellp("transportation.ky.gov")],
]
flow.append(k.ref_table(
    "State agencies and what each is actually for",
    [k.cellp("Agency", bold=True),
     k.cellp("Why you would contact them", bold=True),
     k.cellp("Website", bold=True)],
    # 1.55in split "apps.legislature.ky.gov" mid-word at 9.5pt.
    state_rows, [1.62 * inch, CW - 1.62 * inch - 1.72 * inch, 1.72 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026). Local option and the bar on state "
    "preemption for single-family dwellings — KRS 198B.060(1), (4)(b), (8), "
    "(13); 815 KAR 7:125 Section 2(2)(a). State plumbing permit and local "
    "authorization — KRS 318.134(1)(a); 318.140(1). Septic permit accompanying "
    "the plumbing application — KRS 318.134(2). HVAC permit, and the bar on "
    "new local HVAC programs after January 1, 2007 — KRS 198B.6671(1); "
    "198B.6673(2), (4). Certified electrical inspector and permanent service — "
    "KRS 198B.060(11). No permanent water until the plumbing is approved — "
    "KRS 318.165. County inspector sheets — dhbc.ky.gov, downloaded 27 August "
    "2026. All four agency websites above returned a live page on that date."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ky-permit-kit",
                       "KY.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
