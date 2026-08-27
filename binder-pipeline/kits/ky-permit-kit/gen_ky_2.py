#!/usr/bin/env python3
"""KY.2 Permit Application Checklist.

The centerpiece of this document is the code-edition section. Kentucky is on
the 2023 NEC, but not all of it: the Department delayed several articles under
the 2018 Kentucky Residential Code, three of those delays expired on 15 July
2026, and the 2023 NEC's expanded GFCI requirements REMAIN delayed and are not
yet enforceable. Both halves of that are verified from the Department's own
notice, and both are wrong or missing in every competing Kentucky summary.

Fee figures come from the regulations themselves — 815 KAR 20:050 Section 4 and
815 KAR 8:070 Section 4 — which is why they can be printed at all. Local
building permit fees are NOT printed: they are set by each local government
under KRS 198B.060(18) and there is no statewide schedule.

Verified sources:
  KRS 318.134(2)       the septic permit must accompany the plumbing
                       application — the sequence is statutory
  KRS 198B.060(10)     workers' compensation / unemployment insurance affidavit
  KRS 198B.060(18)     local and department fees "designed to fully cover, but
                       shall not exceed, the cost of the service performed"
  815 KAR 7:125 §2,§3  2015 IRC + 2018 Kentucky Residential Code, 3rd Edition
  815 KAR 20:050 §4-§6 plumbing permit fees, inspections included, expiry
  815 KAR 8:070 §4     HVAC permit fees
  HBC, "Codes Currently Adopted by Kentucky"  the full adopted-code list
  HBC, "July 15, 2026 NEC Update"             the NEC delays, both halves
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

FORM_ID = "KY.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Application"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What to gather, in the order Kentucky actually requires it — starting "
    "with the one approval that gates another by statute.")

flow.append(k.disclaimer(
    "Fees quoted below are the ones published in regulation. Local building "
    "permit fees are set by each local government and are not."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- sequence
flow += k.h2_tight("THE ONE SEQUENCE KENTUCKY FIXES IN STATUTE")
flow.append(k.body(
    "Most permit ordering is convention. This one is law. Your application for "
    "the state plumbing permit must carry \"<i>plans and specifications of the "
    "proposed plumbing installation, location, and construction of the water "
    "supply system to be used</i>\" — and then: \"<i>If an on-site sewage "
    "disposal system that does not have a surface discharge is proposed, <b>a "
    "valid on-site sewage disposal permit issued by the Cabinet for Health and "
    "Family Services or its designated agent shall accompany the "
    "application</b></i>.\""))
flow.append(k.body(
    "In plain terms: <b>on a septic site, no septic permit means no state "
    "plumbing permit</b> — and no state plumbing permit eventually means no "
    "permanent water supply, because a utility or water district may not "
    "provide one until the interior plumbing has been installed and approved. "
    "The health department is therefore the first call on a rural Kentucky "
    "build, not the last."))
flow.append(k.cite("KRS 318.134(2); KRS 318.165."))

flow.append(k.callout_long("The septic permit, and the clock Kentucky puts on it", [
    Paragraph("What you are applying for is a <b>construction permit</b> for "
              "an on-site sewage disposal system, on the Cabinet's form "
              "<b>DFS-307</b>. There is no separate \"operation permit\" for a "
              "house — after installation there is an inspection, before "
              "backfill. It runs through your <b>local health department</b>, "
              "and the environmentalist named on your county inspector sheet "
              "(see KY.4) is the person to call.", S["body"]),
    Paragraph("<b>You get a statutory shot clock, and almost nobody uses "
              "it.</b> \"<i>Site evaluations shall be completed by the local "
              "health department <b>within fifteen (15) working days</b> of "
              "receipt of the application. If further information is required, "
              "the local health department shall promptly notify the applicant "
              "and shall have an additional <b>ten (10) working days</b> after "
              "that submittal of additional information in which to evaluate "
              "and issue or deny the permit.</i>\" (KRS 211.350(3)) Date your "
              "application and keep the copy.", S["body"]),
    Paragraph("<b>It is not a perc test.</b> Kentucky rates the site on soil "
              "morphology from borings or backhoe pits — suitable, "
              "provisionally suitable or unsuitable — and the word "
              "\"percolation\" does not appear in the regulation at all. The "
              "permit expires <b>one year</b> from issuance unless extended. "
              "Fees are hybrid: a <b>$50</b> state permit fee set in "
              "regulation, plus whatever your local board of health charges "
              "for the site evaluation and the permit.", S["body"]),
    Paragraph("<b>And you may install it yourself.</b> Permits normally issue "
              "only to certified installers, but they \"<i>may be issued to "
              "homeowners</i>\" if you apply before starting, do the work in "
              "compliance with the regulations, and — the catch — \"<i>all "
              "work is personally performed by the homeowner, except that "
              "necessary excavation and backfilling work may be performed by a "
              "certified installer <b>if notification of intent is made at the "
              "time of application</b></i>\" with that installer named on the "
              "form. And: \"<i>No person shall be issued more than one (1) "
              "homeowner permit to construct or alter an on-site sewage "
              "disposal system in any five (5) year period</i>,\" repairs "
              "excepted. That is a <b>third</b> five-year ration, separate "
              "from the plumbing and HVAC ones in KY.1.", S["body"]),
]))
flow.append(k.cite(
    "902 KAR 10:085 Section 2(1)(g), (i) and Section 9(1); 902 KAR 10:110 "
    "Sections 1(8), 2(3), 2(4) and 3; KRS 211.350(3), (5). Note the homeowner "
    "definition excludes anyone \"<i>who is a builder or contractor who "
    "engages in a business of constructing or rehabilitating residential "
    "structures for sale or resale</i>.\" Local fees vary widely and a "
    "homeowner-install permit is not always the cheaper option — at least one "
    "district health department charges more for it than for a "
    "certified-installer permit. Ask yours for its fee schedule."))

flow += k.check_table("A1: Before anything else", [
    ("Confirmed whether a building permit is required at all — city and "
     "county, both asked (KY.1, Step 1)",
     [("City:", 0.5), ("County:", 0.5)]),
    ("Health department contacted and the on-site sewage <b>site evaluation</b> "
     "requested",
     [("Date requested:", 0.5), ("Evaluator:", 0.5)]),
    ("On-site sewage disposal permit <b>issued and in hand</b> — you cannot "
     "file the plumbing application without it",
     [("Permit no.:", 0.55), ("Date:", 0.45)]),
    ("Confirmed whether you are on public water or a private well, and what "
     "each requires of you",
     [("Answer:", 1.0)]),
    ("Parcel checked against the flood maps, and the Division of Water asked "
     "if any part is in a floodplain",
     [("Result:", 1.0)]),
    ("911 address assigned — the utilities will want it before they open an "
     "account", [("Address:", 0.7), ("Date:", 0.3)]),
    ("Zoning and setbacks confirmed in writing, whether or not a building "
     "permit is required", [("Confirmed by:", 0.6), ("Date:", 0.4)]),
    ("Driveway or entrance permit — Transportation Cabinet district on a "
     "state-maintained route, county road department otherwise",
     [("Authority:", 0.6), ("Date:", 0.4)]),
], notes_header="Notes / who confirmed")

# ---------------------------------------------------------------- package
# reserve=2.6: this heading has no body text under it, so the default 1.5in let
# it print with only the B1 table's title band's worth of room left and stranded
# it alone at the foot of the page.
flow += k.h2_tight("THE APPLICATION PACKAGE", reserve=2.6)

flow += k.check_table("B1: State plumbing permit", [
    "Application made <b>before the work begins</b> — the regulation requires "
    "it, and a permit cannot be issued retroactively",
    "<b>Homeowner affidavit</b> filed with the application, stating you will "
    "abide by 815 KAR Chapter 20",
    "Plans and specifications of the plumbing installation, and of the "
    "location and construction of the water supply system",
    "Valid on-site sewage disposal permit attached, if you are on septic",
    ("Asked the Division of Plumbing whether your house requires a "
     "<b>plan submission</b> or will be handled by field inspection — the "
     "regulation's plan-review section and its enabling statute do not line up "
     "cleanly for a single-family house, so get the answer in writing",
     [("Answer:", 0.7), ("From:", 0.3)]),
    ("Fixture count worked out — the fee is driven by it",
     [("Fixtures / openings:", 0.55), ("Water heaters:", 0.45)]),
], notes_header="Notes")

flow += k.check_table("B2: State HVAC permit", [
    "Applied on the <b>Homeowner One &amp; Two Family Dwellings</b> form, "
    "before any HVAC work starts",
    "<b>Affidavit</b> to abide by the regulation",
    "<b>Proof of adequate sizing</b> of the system to be installed — a load "
    "calculation, not a rule of thumb",
    "<b>A complete design plan of all related duct and piping</b> — the most "
    "paperwork any of the three trade permits asks for",
    ("Five-year check: no homeowner HVAC construction permit issued to you "
     "within the last five years", [("Last one (date or none):", 1.0)]),
], notes_header="Notes")

flow += k.check_table("B3: Electrical", [
    "Identified the <b>certified electrical inspector</b> who will issue your "
    "final certificate of approval — without it your power company cannot "
    "connect permanent service",
    "Confirmed whether they are a local inspector or the state inspector named "
    "on your county sheet, and how they want inspections requested",
    "Confirmed the inspector holds at least the <b>one- and two-family</b> "
    "certification class",
    ("Arranged <b>temporary construction power</b> — expressly not blocked by "
     "the permanent-service rule", [("Utility:", 0.6), ("Date:", 0.4)]),
], notes_header="Notes")

flow += k.check_table("B4: If a local building permit IS required", [
    "Local application form, plans and site plan to that jurisdiction's "
    "requirements — these are local instruments and they vary",
    "<b>Workers' compensation and unemployment insurance affidavit</b> — "
    "required by statute before any Kentucky building department may issue a "
    "permit (see below)",
    ("Certificate of insurance collected from every subcontractor before they "
     "start", [("Filed where:", 1.0)]),
    ("Local fee schedule obtained in writing so you can budget",
     [("Fee basis:", 0.6), ("Amount:", 0.4)]),
], notes_header="Notes")

# ---------------------------------------------------------------- affidavit
flow += k.h2_tight("THE WORKERS' COMPENSATION AFFIDAVIT")
flow.append(k.body(
    "No Kentucky building department may issue any permit \"<i>unless the "
    "person shall assure, <b>by affidavit</b>, that all contractors and "
    "subcontractors employed, or that will be employed, on activity covered by "
    "the permit shall be in compliance with Kentucky requirements for workers' "
    "compensation insurance … and unemployment insurance</i>.\" You are "
    "swearing to something about other people's insurance, and the penalty for "
    "getting it wrong is uncapped in the direction that matters: a fine \"<i>not "
    "to exceed four thousand dollars ($4,000) <b>or an amount equal to the sum "
    "of all uninsured and unsatisfied claims</b> … <b>whichever is "
    "greater</b></i>,\" enforced by the county attorney."))
flow.append(k.body(
    "Collect a certificate of insurance from every subcontractor, keep it, and "
    "re-check the expiry date against your schedule. This is the cheapest line "
    "item in the whole build and the one with the largest tail."))
flow.append(k.cite("KRS 198B.060(10)(a), (b), (c)."))

# ---------------------------------------------------------------- codes
flow += k.h2_tight("CODE EDITIONS — AND THE PART OF THE NEC KENTUCKY HAS NOT "
                   "SWITCHED ON")
flow.append(k.body(
    "Kentucky's adopted editions are older than most national tables suggest, "
    "and the electrical picture is genuinely unusual. Build to the wrong "
    "edition and you will be told about it at rough-in."))

code_rows = [
    [k.cellp("<b>Residential</b>"),
     k.cellp("<b>2018 Kentucky Residential Code, Third Edition (August "
             "2024)</b>, based on the <b>2015 International Residential "
             "Code</b>. The Kentucky amendments supersede any conflicting IRC "
             "provision."),
     k.cellp("815 KAR 7:125 §2(1), §3; effective 3 Dec 2024")],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("<b>2023 National Electrical Code (NFPA 70)</b> — but with "
             "Kentucky delays still in force. See the box below before you buy "
             "devices."),
     k.cellp("HBC adopted-codes list; HBC NEC notice")],
    [k.cellp("<b>Energy</b>"),
     k.cellp("<b>2009 IECC</b> for residential buildings. (The 2012 IECC "
             "applies to commercial only.) This is among the more lenient "
             "residential energy codes still in force anywhere — treat it as a "
             "floor, not a target."),
     k.cellp("HBC adopted-codes list")],
    [k.cellp("<b>Mechanical</b>"),
     k.cellp("<b>2015 International Mechanical Code.</b>"),
     k.cellp("HBC adopted-codes list")],
    [k.cellp("<b>Fuel gas</b>"),
     k.cellp("<b>NFPA 54, National Fuel Gas Code</b> — <i>not</i> the "
             "International Fuel Gas Code, which Kentucky does not adopt at "
             "all. <b>Ask your inspector which edition:</b> the Department's "
             "adopted-codes list says 2012, while the Residential Code's own "
             "referenced-standards chapter says 2009. Confirm before you buy a "
             "reference book."),
     k.cellp("HBC adopted-codes list; KRC Ch. 24 and Ch. 44")],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp("<b>Kentucky's own State Plumbing Code</b>, 815 KAR Chapter 20. "
             "Kentucky adopts neither the IPC nor the UPC — the plumbing rules "
             "are a Kentucky instrument, and the statute folds them into the "
             "Uniform State Building Code."),
     k.cellp("815 KAR Chapter 20; KRS 198B.050(2)")],
]
flow.append(k.ref_table(
    "What is actually in force in Kentucky",
    [k.cellp("Discipline", bold=True), k.cellp("Edition", bold=True),
     k.cellp("Authority", bold=True)],
    code_rows, [1.05 * inch, CW - 1.05 * inch - 1.75 * inch, 1.75 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout_long(
    "The NEC trap — half of it expired six weeks ago, and half of it has not",
    [
        Paragraph("Kentucky is on the <b>2023 NEC</b>, but the Department "
                  "delayed enforcement of several of its articles under the "
                  "2018 Kentucky Residential Code. Anyone quoting \"Kentucky "
                  "is on the 2023 NEC\" without the delays, or quoting the "
                  "delays without their dates, will send you wrong in one "
                  "direction or the other.", S["body"]),
        Paragraph("<b>Now enforceable — the delay expired 15 July 2026.</b> "
                  "<b>210.52(C)</b> receptacle locations for islands, "
                  "peninsulas, wall spaces, countertops and work surfaces; "
                  "<b>230.67</b> surge protection for services supplying "
                  "dwelling units; and <b>314.27(C)</b> outlet boxes for "
                  "ceiling-suspended paddle fans. If you read a guide written "
                  "before that date saying these do not apply yet, it is now "
                  "out of date.", S["body"]),
        Paragraph("<b>Still delayed, and NOT yet enforceable.</b> The "
                  "Department's own words: \"<i>The following GFCI "
                  "requirements in the 2023 NEC under the 2018 Kentucky "
                  "Residential Code <b>remain delayed and are not yet "
                  "enforceable</b></i>\" — <b>210.8(A)</b>, GFCI protection "
                  "for receptacles over 125 volts, and <b>210.8(D)(8), (9), "
                  "(10) and (11)</b>, GFCI protection for specified branch "
                  "circuits and outlets. This is the half that changes what "
                  "you actually install, and it is the half every summary "
                  "leaves out.", S["body"]),
        Paragraph("<b>The paddle-fan box clarification.</b> The Department "
                  "issued it because inspectors and builders were reading "
                  "314.27(C) too widely: it \"<i>does not require every "
                  "ceiling outlet box to be listed for ceiling fan support. "
                  "The requirement applies only to outlet boxes installed in "
                  "the <b>habitable rooms</b> of dwelling units where a "
                  "ceiling-suspended (paddle) fan could reasonably be "
                  "installed in the future.</i>\"", S["body"]),
        Paragraph("<b>And there is a grandfather clause worth knowing.</b> "
                  "\"<i>If a project has gone through a building code plan "
                  "review and the approval from the review was before July 15, "
                  "2026, or <b>the electrical permit was issued before July "
                  "15, 2026</b>, then the work under the scope of the "
                  "electrical permit would not be required to follow the "
                  "requirements that will begin mandatory enforcement on July "
                  "15, 2026.</i>\" If your project straddles that date, the "
                  "date on your paperwork decides which rules you build to — "
                  "so find it and keep it.", S["body"]),
    ]))
flow.append(k.cite(
    "Department of Housing, Buildings and Construction, <i>July 15, 2026 NEC "
    "Update</i>, and <i>Codes Currently Adopted by Kentucky</i>, both read at "
    "dhbc.ky.gov on 27 August 2026. Code editions: 815 KAR 7:125, effective "
    "3 December 2024. <b>Confirm the current position before you wire.</b> The "
    "Department established a <b>2026 NEC Task Force</b> on 18 March 2026 to "
    "review the 2026 edition against the currently adopted 2023 NEC and "
    "recommend adoption; as of August 2026 no adoption date had been "
    "announced. The delays live in the code document and in Department "
    "notices, not in the regulation text, so the notice page at dhbc.ky.gov is "
    "the thing to re-read."))

flow += k.check_table("D1: Code and energy", [
    ("Confirmed with your electrical inspector which NEC articles they are "
     "enforcing today, and noted the date you asked",
     [("Inspector:", 0.55), ("Date asked:", 0.45)]),
    "Understood that <b>210.8(A)</b> and <b>210.8(D)(8)–(11)</b> GFCI "
    "provisions remain delayed — do not assume 2023 NEC GFCI coverage applies",
    ("If your permit or plan approval predates 15 July 2026, kept the dated "
     "paperwork that proves it", [("Permit date:", 1.0)]),
    "Energy compliance worked to the <b>2009 IECC</b> as the minimum, with a "
    "decision recorded on where you will exceed it",
    "Fuel gas checked against <b>NFPA 54</b> (not the IFGC), and plumbing "
    "against <b>815 KAR Chapter 20</b> (not the IPC or UPC)",
], notes_header="Notes")

# ---------------------------------------------------------------- fees
flow += k.h2_tight("FEES — THE ONES KENTUCKY PUBLISHES")
flow.append(k.body(
    "Two of your three state permits have fees fixed in regulation, so they "
    "can be budgeted exactly. The local building permit cannot: each local "
    "government sets its own, and the only statutory constraint is that fees "
    "\"<i>shall be designed to fully cover, but shall not exceed, the cost of "
    "the service performed</i>.\" That is why Kentucky building permit fees "
    "are low by national standards — and why this kit prints a blank for "
    "yours rather than a guess."))

fee_rows = [
    [k.cellp("<b>State plumbing permit</b><br/>one- and two-family"),
     k.cellp("<b>$50 base, plus $14</b> for each plumbing fixture, appliance "
             "or opening left for one; each domestic water heater; and each "
             "separately metered water or sewer service beyond the first. A "
             "single water heater on its own is <b>$50</b> flat."),
     k.cellp("815 KAR 20:050 §4")],
    [k.cellp("<b>Plumbing inspections</b>"),
     k.cellp("<b>Five inspections are included</b> at no additional cost. "
             "Each additional inspection is <b>$50</b>, payable before the "
             "final — but additional inspection fees do not apply at all if "
             "your permit cost exceeded <b>$250</b>."),
     k.cellp("815 KAR 20:050 §5")],
    [k.cellp("<b>State HVAC permit</b>"),
     k.cellp("<b>$105 for the first system, plus $50</b> for each additional "
             "system. Homeowner permits are charged at the same rate as "
             "one- and two-family permits."),
     k.cellp("815 KAR 8:070 §4(1)")],
    [k.cellp("<b>Electrical inspection</b>"),
     k.cellp("Set by the inspector or the local government behind them — not "
             "fixed statewide. Ask when you book."),
     k.cellp("KRS 198B.060(11), (18)")],
    [k.cellp("<b>Local building permit</b>"),
     k.cellp("Set by each local government, at cost. Commonly per square foot "
             "or valuation-based. <b>Get yours in writing.</b>"),
     k.cellp("KRS 198B.060(18)")],
    [k.cellp("<b>Septic permit</b>"),
     k.cellp("Your county health department — ask the environmentalist named "
             "on your county inspector sheet."),
     k.cellp("Local health department")],
]
flow.append(k.ref_table(
    "Published fees, and the ones you have to ask for",
    [k.cellp("Permit", bold=True), k.cellp("Fee", bold=True),
     k.cellp("Authority", bold=True)],
    fee_rows, [1.35 * inch, CW - 1.35 * inch - 1.45 * inch, 1.45 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout("The plumbing permit has a clock on it", [
    Paragraph("A plumbing permit \"<i>shall expire one (1) year after the date "
              "of issuance unless construction is ongoing, in which case the "
              "permit shall remain effective until the completion of the "
              "planned plumbing inspection</i>,\" and it \"<i>shall expire and "
              "become void if the plumbing work ceases on the project for a "
              "period exceeding twelve (12) months</i>.\"", S["body"]),
    Paragraph("For an owner-builder working weekends this is the likeliest "
              "administrative failure in the kit: a winter of interior work "
              "with no plumbing activity looks identical to abandonment. "
              "<b>If a long gap is coming, call an inspection you can pass "
              "before it starts.</b> Five are included.", S["body"]),
]))
flow.append(k.cite("815 KAR 20:050 §6(1), (2); §5(1)."))

flow.append(Spacer(1, 6))
flow.append(d.FillInRow([("Total permit budget:", 0.5),
                         ("Confirmed on:", 0.5)]))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 6))
flow.append(k.sources_table([
    ("The on-site sewage permit must accompany the state plumbing permit "
     "application", "KRS 318.134(2)"),
    ("No permanent water supply until the interior plumbing is installed and "
     "approved", "KRS 318.165"),
    ("Workers' compensation and unemployment affidavit required before any "
     "permit issues; $4,000 or the sum of all uninsured claims, whichever is "
     "greater", "KRS 198B.060(10)"),
    ("2015 IRC plus the 2018 Kentucky Residential Code, Third Edition "
     "(August 2024), effective 3 December 2024", "815 KAR 7:125 §2(1), §3"),
    ("2023 NEC in force; 210.52(C), 230.67 and 314.27(C) enforceable from "
     "15 July 2026; 210.8(A) and 210.8(D)(8)–(11) remain delayed",
     "HBC, July 15 2026 NEC Update"),
    ("2009 IECC residential, 2015 IMC, NFPA 54 for fuel gas rather than the "
     "IFGC, and Kentucky's own plumbing code rather than the IPC or UPC",
     "HBC adopted-codes list; KRS 198B.050(2)"),
    ("On-site sewage: a construction permit on form DFS-307, issued only to a "
     "certified installer or to a homeowner, after a site evaluation the "
     "health department must complete in 15 working days",
     "902 KAR 10:085 §2; 10:110 §2, §3; KRS 211.350(3)"),
    ("A homeowner may install their own system, must do the work personally "
     "except excavation and backfill, and may hold only one such permit in "
     "five years", "902 KAR 10:110 §2(4)"),
    ("A state floodplain permit is required to place a building in a "
     "floodplain, regardless of any local ordinance", "KRS 151.250(2)"),
    ("Plumbing permit fees, five inspections included, and the one-year "
     "expiry", "815 KAR 20:050 §4, §5, §6"),
    ("HVAC permit fee of $105 for the first system plus $50 each additional",
     "815 KAR 8:070 §4(1)"),
    ("Local and department fees must cover but not exceed the cost of the "
     "service", "KRS 198B.060(18)"),
]))
flow.append(k.cite(k.STATUTE_NOTE))

# ---------------------------------------------------------------- the record
# KY.3 logs the inspections; nothing logged the permits themselves, and the
# plumbing permit's one-year clock makes the expiry column load-bearing.
flow += k.h2_tight("PERMIT RECORD — FILL THIS IN AS EACH ONE ISSUES")
flow.append(k.body(
    "Keep this with the plan set. The <b>expires</b> column matters more in "
    "Kentucky than most places: the state plumbing permit runs out one year "
    "from issuance unless construction is ongoing, and a local building permit "
    "carries whatever expiry that jurisdiction sets — ask, and write it here."))

rec_header = [k.cellp("Permit", bold=True), k.cellp("Number", bold=True),
              k.cellp("Issued", bold=True), k.cellp("Fee paid", bold=True),
              k.cellp("Expires", bold=True), k.cellp("Issuing office", bold=True)]
rec_names = [
    "On-site sewage (septic)", "State plumbing", "State HVAC",
    "Electrical inspection", "Local building (or N/A)", "Driveway / entrance",
    "Floodplain (or N/A)", "",
]
rec_rows = [[k.cellp(n) if n else "", "", "", "", "", ""] for n in rec_names]
rec_w = [1.55 * inch, 0.90 * inch, 0.72 * inch, 0.72 * inch, 0.72 * inch]
rec_w.append(CW - sum(rec_w))
flow.append(d.titled_table(
    "Permit record", rec_header, rec_rows, rec_w, S,
    row_heights=[30] * len(rec_rows)))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ky-permit-kit",
                       "KY.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
