#!/usr/bin/env python3
"""MS.4 Where to File Directory.

Mississippi's hardest question is not what the rules are. It is whether any
building code binds your parcel at all — and that was settled by a resolution
entered on a board's minutes in 2006 or 2014, in windows that are now closed.

This document is the kit's differentiator. No competing guide tells a reader
that the adopted code is a filed public record they can demand to see, or that
the opt-out resolutions are findable in the same minute books. Both facts come
straight out of the enabling statutes:

  § 19-5-9    county codes bind ONLY the unincorporated areas of the county,
              and the adopted code is "certified to by the president and clerk
              of the board of supervisors and shall be filed as a permanent
              record in the office of the clerk"
  § 21-19-25  municipal codes are adopted by ordinance, "certified to by the
              mayor and clerk of the municipality, and shall be filed as a
              permanent record in the office of the clerk," with published
              notice; and are not in force for one month after passage unless
              the ordinance says otherwise
  SB 2378 (2014) § 1(3)   the 120-day statewide opt-out, "upon resolution duly
              adopted and entered upon its minutes"
  § 17-2-1 (2006 HB 1406) § 1(4)  the coastal 60-day opt-out, same mechanism

Deliberately prints agency WEBSITES and lookup routes rather than phone
numbers — direct-dial numbers at county and municipal offices change often
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

FORM_ID = "MS.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Before you can ask where to file, you have to answer a question most "
    "states never pose: does any building code bind this parcel? Here is how "
    "to find out, from public records you are entitled to see.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- the problem
flow += k.h2_tight("THE QUESTION MISSISSIPPI MAKES YOU ANSWER FIRST")
flow.append(k.body(
    "In most states the building code is a given and the only question is "
    "which office administers it. In Mississippi the code itself is "
    "contingent. Your parcel sits in exactly one of three situations, and "
    "which one it is determines everything else in this kit."))

sit_rows = [
    [k.cellp("<b>A — Inside a city or town<br/>that adopted a code</b>"),
     k.cellp("The municipality issues your permits and inspects. Its "
             "ordinance governs, and it may be stricter than anything the "
             "state requires. Municipal codes reach the whole area inside the "
             "corporate limits.")],
    [k.cellp("<b>B — Unincorporated county<br/>that adopted a code</b>"),
     k.cellp("The county issues and inspects. Note the limit in § 19-5-9: a "
             "county's codes \"<i>shall apply <b>only to the unincorporated "
             "areas</b> of the county</i>.\" A county code never governs "
             "inside a town's limits.")],
    [k.cellp("<b>C — No code adopted,<br/>or opted out</b>"),
     k.cellp("No building permit, no plan review, no inspector. This is legal "
             "and it is common. It does <b>not</b> mean nothing applies — see "
             "the second half of this document, and MS.2.")],
]
flow.append(k.ref_table(
    "The three situations",
    [k.cellp("Where your parcel sits", bold=True),
     k.cellp("What it means for you", bold=True)],
    sit_rows, [2.0 * inch, CW - 2.0 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout_long(
    "Why nobody can tell you the answer from your county's name", [
        Paragraph("Mississippi ran <b>two opt-out windows</b>, and both are "
                  "long closed. The statewide construction code law took "
                  "effect <b>August 1, 2014</b>, and gave every county and "
                  "every municipality within it 120 days to walk away: "
                  "\"<i>Within one hundred twenty (120) days after the "
                  "provisions of this section go into effect, the board of "
                  "supervisors of a county and/or the governing authorities "
                  "of any municipality within a county, <b>upon resolution "
                  "duly adopted and entered upon its minutes</b>, may choose "
                  "not to be subject to the code requirements imposed under "
                  "this section.</i>\" That window shut at the end of "
                  "November 2014 and has never reopened.", S["body"]),
        Paragraph("The coastal mandate had its own, earlier window. The 2006 "
                  "law that put Jackson, Harrison, Hancock, Stone and Pearl "
                  "River counties under emergency wind and flood requirements "
                  "gave those same counties and their municipalities <b>sixty "
                  "days</b> to opt out by resolution, in identical language. "
                  "So even on the coast, \"mandatory\" is a claim to check "
                  "rather than assume.", S["body"]),
        Paragraph("<b>This is why a neighbor, a builder, or a search result "
                  "cannot answer it for you.</b> The decision was a vote in a "
                  "room a decade ago, recorded in a minute book, and it "
                  "varies between a county and the towns inside it. The good "
                  "news is that a vote entered on the minutes is a public "
                  "record — and so is the code itself. You can go and look.",
                  S["body"]),
    ]))
flow.append(k.cite(
    "Senate Bill 2378, 2014 Regular Session, Section 1(3), effective August "
    "1, 2014, codified in Miss. Code Ann. Title 17, Chapter 2 — read as "
    "enrolled at billstatus.ls.state.ms.us. <b>The State confirms the "
    "deadline in its own words:</b> the State Fire Marshal's office states "
    "that \"<i>under Senate Bill 2378 of 2014, all counties and "
    "municipalities must enact uniform building codes unless they opt out "
    "prior to Nov. 30, 2014</i>\" (mid.ms.gov → State Fire Marshal → "
    "Mississippi Uniform Building Codes). Coastal window: House Bill 1406, "
    "2006 Regular Session, Section 1(4), now Miss. Code Ann. § 17-2-1. County "
    "limitation: § 19-5-9. Verified August 2026."))

# ---------------------------------------------------------------- how to find out
flow += k.h2_tight("HOW TO ESTABLISH IT — IN FOUR CALLS AND ONE VISIT")
flow.append(k.body(
    "Work these in order. Stop as soon as you get a clear written answer, and "
    "write it on the next page. The whole exercise is usually done in a "
    "morning, and it is the highest-value morning of your project."))

flow.append(k.checklist([
    "<b>Settle whether you are inside a municipality at all.</b> A rural "
    "mailing address often carries a nearby town's post office name while the "
    "parcel itself is in the unincorporated county. The <b>county tax "
    "assessor</b> settles it from the parcel number, and will tell you free.",
    "<b>If you are inside a town or city:</b> ask the <b>municipal clerk</b> "
    "whether the municipality has adopted a building code, and under which "
    "ordinance. Section 21-19-25 requires the adopted code to be "
    "\"<i>certified to by the mayor and clerk of the municipality</i>\" and "
    "\"<i>filed as a permanent record in the office of the clerk</i>.\" Ask "
    "to see the filed copy.",
    "<b>If you are in the unincorporated county:</b> ask the <b>chancery "
    "clerk</b>, who keeps the board of supervisors' minutes, the same "
    "question. Section 19-5-9 requires a county's adopted code to be "
    "\"<i>certified to by the president and clerk of the board of "
    "supervisors</i>\" and \"<i>filed as a permanent record in the office of "
    "the clerk</i>.\"",
    "<b>Ask the specific question nobody thinks to ask:</b> \"Did this board "
    "adopt a resolution opting out of the State Uniform Construction Code "
    "in 2014?\" — and, in the five coastal counties, \"or out of the wind and "
    "flood requirements in 2006?\" Both were required to be entered on the "
    "minutes, so both are findable.",
    "<b>Get it in writing.</b> An email from the clerk or the building "
    "official saying \"no building permit is required for a single-family "
    "dwelling at parcel #____\" is worth keeping for the rest of the "
    "building's life. Your lender, your insurer, and the person who buys the "
    "house from you in twenty years will all eventually ask.",
    "<b>If a code IS enforced, ask which edition.</b> The statute lets a "
    "jurisdiction adopt \"<i>one (1) of the last three (3) adopted "
    "editions</i>\" — so neighboring counties can lawfully be on different "
    "editions of the IRC at the same time. There is no single Mississippi "
    "answer to look up.",
    "<b>Do not expect the State to have a list.</b> The Insurance "
    "Department's Fire Marshal page on uniform building codes is a form for "
    "jurisdictions to <i>self-report</i> their code policy. There is no "
    "published roster of who opted out. Your county's own minute book is the "
    "record that governs.",
]))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "The body that sets the statewide minimum has not set one", [
        Paragraph("Both the statute and the 2014 act speak of codes "
                  "\"<i>as adopted and amended by the Mississippi Building "
                  "Codes Council</i>.\" The Council is real and its statute "
                  "is unrepealed — but its authority is written as "
                  "<b>discretionary</b>, and a search of the Insurance "
                  "Department's adopted regulations, where a Council code "
                  "would have to be filed, turns up no building-codes-council "
                  "chapter, no residential code, and no adopted IRC edition "
                  "at all.", S["body"]),
        Paragraph("Practically, that means <b>there is no statewide "
                  "residential code edition to look up, and no statewide "
                  "electrical or energy code for a site-built house.</b> Both "
                  "reach your project only through whichever edition of the "
                  "IRC your own county or city adopted — which is the "
                  "question this document keeps sending you back to. If you "
                  "are told \"Mississippi is on the such-and-such IRC,\" ask "
                  "the speaker which instrument adopted it.", S["body"]),
    ]))
flow.append(k.cite(
    "Miss. Code Ann. § 17-2-3(5) — the Council \"shall adopt by reference and "
    "amend only one (1) of the last three (3) editions … as <b>discretionary "
    "statewide minimum codes</b>.\" The absence of any adopted code was "
    "established by enumerating the Mississippi Insurance Department's "
    "adopted regulations, including all sixteen chapters of the State Fire "
    "Marshal's Part 7, in August 2026. Note separately that the Fire Marshal "
    "<i>has</i> adopted the 2024 International Fire Code and International "
    "Building Code as of July 1, 2024, and that the state's modular-home rule "
    "adopts 2024 editions including the IRC and the National Electrical Code "
    "— <b>neither reaches a site-built one- or two-family dwelling</b>, and "
    "both are frequently misreported as a statewide residential adoption."))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "Two things that are true even where a code IS enforced", [
        Paragraph("<b>Residential fire sprinklers are not required by the "
                  "state.</b> The statewide law adopts the IRC \"<i>with the "
                  "exception of those provisions that require the "
                  "installation of a multipurpose residential fire protection "
                  "sprinkler system or any other fire sprinkler protection "
                  "system in a new or existing one- or two-family "
                  "dwelling</i>,\" and the Building Codes Council is "
                  "separately barred from imposing one. <b>But your county or "
                  "city still may</b> — the same section preserves their "
                  "power to \"<i>adopt, modify and enforce codes …, including "
                  "the adoption of codes which require the installation of "
                  "fire protection sprinkler systems in any structure</i>.\" "
                  "Ask; do not assume.", S["body"]),
        Paragraph("<b>A county code stops at the town line.</b> If your "
                  "parcel is inside a municipality, the county's code does "
                  "not reach it, and the municipality's does — even if the "
                  "county's is stricter, and even if the town has no building "
                  "department of its own.", S["body"]),
    ]))
flow.append(k.cite(
    "Sprinkler carve-out: SB 2378 (2014) § 1(1)(b). Council bar and the "
    "preserved local power: Miss. Code Ann. § 17-2-3(7), as amended by 2011 "
    "HB 1385. Edition choice: SB 2378 (2014) § 1(1)(a)–(b) and § 17-2-3(5). "
    "County limit: § 19-5-9."))

# ---------------------------------------------------------------- the other offices
flow += k.h2_tight("THE OFFICES THAT DO NOT CARE WHETHER YOU HAVE A CODE")
flow.append(k.body(
    "This is the half of the directory that matters most in no-code "
    "Mississippi, and the half that guides skip. A building-code opt-out is "
    "an opt-out of <b>the building code</b>. It is not an opt-out of public "
    "health law, of flood-insurance rules, of highway access rules, or of "
    "your utility's connection requirements. Each of these is a separate "
    "authority under a separate statute, and each can stop your project."))

off_rows = [
    [k.cellp("<b>County health department</b><br/>(septic / onsite "
             "wastewater)"),
     k.cellp("Administered through the <b>Mississippi State Department of "
             "Health</b> — msdh.ms.gov — usually at the county health "
             "department. On any parcel without a public sewer this is the "
             "approval to secure <b>first</b>, because it can determine where "
             "on the lot the house may sit, and in a no-code county it is "
             "commonly the only site inspection your build will ever "
             "receive.")],
    [k.cellp("<b>Floodplain administrator</b>"),
     k.cellp("If your community takes part in the National Flood Insurance "
             "Program it administers a floodplain ordinance, and the "
             "construction-code exemptions in state law are expressly written "
             "not to touch it — \"<i>the provisions of this section shall not "
             "apply to any floodplain management ordinances or regulations "
             "necessary for eligibility for the National Flood Insurance "
             "Program</i>.\" Ask the county or city who holds this role.")],
    [k.cellp("<b>E-911 addressing</b>"),
     k.cellp("A new parcel usually needs an address assigned before a utility "
             "will set a meter or a lender will close. Normally run by the "
             "county — ask the chancery clerk or the county administrator who "
             "handles addressing.")],
    [k.cellp("<b>County road department<br/>or MDOT</b>"),
     k.cellp("A new driveway tying into a county road needs the county's "
             "permission; a tie-in to a numbered <b>state</b> highway is "
             "MDOT's — mdot.ms.gov. Settle this before you grade, because the "
             "culvert size and apron location are theirs to specify, not "
             "yours.")],
    [k.cellp("<b>Electric utility</b>"),
     k.cellp("Your power supplier — an investor-owned utility or one of "
             "Mississippi's electric cooperatives — sets its own conditions "
             "for temporary construction power and for setting the permanent "
             "meter, and those conditions apply whether or not a code does. "
             "<b>Ask early what release or inspection they require</b>; in a "
             "county with no electrical inspector this is the question that "
             "most often surprises owner-builders.")],
    [k.cellp("<b>Water association<br/>or rural water district</b>"),
     k.cellp("Much of rural Mississippi is served by member-owned water "
             "associations rather than a municipal system. Membership, tap "
             "fees and meter-set lead times are set by the association and "
             "are worth asking about months ahead.")],
    [k.cellp("<b>Zoning office</b>"),
     k.cellp("Zoning is separate from building code, and a county or city "
             "with no building code may still have zoning — setbacks, minimum "
             "lot size, permitted uses. Ask specifically; the answer is often "
             "different from the building-code answer.")],
]
flow.append(k.ref_table(
    "Authorities that apply regardless of your building-code status",
    [k.cellp("Office", bold=True), k.cellp("Why it can stop you", bold=True)],
    off_rows, [1.95 * inch, CW - 1.95 * inch]))
flow.append(k.cite(
    "The floodplain quotation is Miss. Code Ann. § 17-2-7(5), repeated at "
    "§ 17-2-9(6) — the exemptions from the state construction code are "
    "expressly written not to reach NFIP floodplain ordinances. Confirm which "
    "of the offices above apply to your parcel; several will not."))

# ---------------------------------------------------------------- directory
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT")
flow.append(k.body(
    "Start with the code-status question, because every line under it depends "
    "on the answer. Confirm each entry with the office itself rather than "
    "copying it from a search result, and note the name of the person you "
    "spoke to — in a county office, a name is worth more than a number."))

flow.append(Paragraph(
    "<b>CODE STATUS</b> — <font size=9.5>the answer that governs everything "
    "else</font>", S["body"]))
flow.append(d.FillInRow([("Parcel is in (city / unincorporated county):", 1.0)]))
flow.append(d.FillInRow([("Building code enforced?  YES / NO:", 0.5),
                         ("Confirmed by:", 0.5)]))
# Three fields left "In writing?" a 33pt rule — too short to write on. Two
# fields give both a usable run.
flow.append(d.FillInRow([("Code and edition enforced:", 0.6),
                         ("Confirmed in writing on:", 0.4)]))
flow.append(Spacer(1, 8))


def office_block(label, sub):
    """One office: department, then portal plus who and when confirmed."""
    return [
        Paragraph(f"<b>{label}</b> — <font size=9.5>{sub}</font>", S["body"]),
        d.FillInRow([("Office / department:", 0.62), ("Phone:", 0.38)]),
        d.FillInRow([("Website / address:", 0.40), ("Spoke with:", 0.32),
                     ("Confirmed:", 0.28)]),
        Spacer(1, 4),
    ]


for label, sub in [
    ("BUILDING PERMIT OFFICE", "municipal or county — or write NONE"),
    ("CHANCERY CLERK", "board minutes, filed county code, opt-out resolution"),
    ("MUNICIPAL CLERK", "ordinances and the filed municipal code"),
    ("COUNTY HEALTH DEPARTMENT", "septic permit and soil evaluation"),
    ("FLOODPLAIN ADMINISTRATOR", "flood zone, elevation, NFIP status"),
    ("E-911 ADDRESSING", "address assignment for the new dwelling"),
    ("ROAD DEPARTMENT / MDOT", "driveway tie-in and culvert"),
    ("ELECTRIC UTILITY", "temporary power, permanent meter, what they require"),
    ("WATER ASSOCIATION / UTILITY", "membership, tap, meter lead time"),
    ("ZONING OFFICE", "setbacks, lot size, permitted use — if any"),
]:
    flow += office_block(label, sub)

# ---------------------------------------------------------------- state level
flow += k.h2_tight("STATE-LEVEL CONTACTS")
flow.append(k.body(
    "These are stable and worth knowing. Phone numbers are left for you to "
    "confirm — a wrong number printed in a kit is worse than no number."))

state_rows = [
    [k.cellp("<b>Mississippi State Board of Contractors</b>"),
     k.cellp("Licenses residential builders, remodelers, construction "
             "managers and the electrical, plumbing, mechanical and HVAC "
             "trades. This is where you <b>verify the license of every trade "
             "contractor you hire</b> — required no matter how small the job "
             "is."),
     k.cellp("msboc.us")],
    [k.cellp("<b>Mississippi State Department of Health</b>"),
     k.cellp("Onsite wastewater (septic) permitting and the certification of "
             "installers and evaluators; county health departments deliver "
             "the service locally."),
     k.cellp("msdh.ms.gov")],
    [k.cellp("<b>Mississippi Department of Environmental Quality</b>"),
     k.cellp("Water wells and water-supply matters, and construction "
             "stormwater permitting on larger disturbances."),
     k.cellp("mdeq.ms.gov")],
    [k.cellp("<b>Mississippi Emergency Management Agency</b>"),
     k.cellp("State coordination for the National Flood Insurance Program — "
             "the route to community flood-map information when your local "
             "office cannot help."),
     k.cellp("msema.org")],
    [k.cellp("<b>Mississippi Department of Transportation</b>"),
     k.cellp("Access and driveway permits where your property fronts a "
             "numbered state highway."),
     k.cellp("mdot.ms.gov")],
    [k.cellp("<b>Mississippi Legislature</b>"),
     k.cellp("The statutes themselves, free: Title 73 Chapter 59 "
             "(residential builders), Title 17 Chapter 2 (building codes), "
             "§ 19-5-9 and § 21-19-25 (county and municipal adoption). The "
             "site also carries every enacted bill, which is how the dates in "
             "this kit were checked."),
     k.cellp("legislature.ms.gov")],
]
flow.append(k.ref_table(
    "State agencies and what each is actually for",
    [k.cellp("Agency", bold=True),
     k.cellp("Why you would contact them", bold=True),
     k.cellp("Website", bold=True)],
    # 1.25in split "legislature.ms.gov" mid-word at 9.5pt.
    state_rows, [1.75 * inch, CW - 1.75 * inch - 1.5 * inch, 1.5 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026). Statewide code and its 120-day "
    "opt-out: SB 2378, 2014 Regular Session, § 1, effective August 1, 2014. "
    "Coastal counties and their 60-day opt-out: HB 1406, 2006 Regular "
    "Session, § 1, codified at Miss. Code Ann. § 17-2-1. Council editions and "
    "the sprinkler bar: § 17-2-3(5), (7), as amended by HB 1385, 2011 Regular "
    "Session. County adoption, the unincorporated-areas limit, and filing "
    "with the clerk: § 19-5-9. Municipal adoption, filing and notice: "
    "§ 21-19-25. NFIP floodplain ordinances unaffected by the code "
    "exemptions: § 17-2-7(5); § 17-2-9(6). Enacted bill text was read at "
    "billstatus.ls.state.ms.us."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ms-permit-kit",
                       "MS.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
