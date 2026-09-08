#!/usr/bin/env python3
"""AZ.3 Inspection Sequence & Clocks.

Every Arizona claim in this document was read against its primary source in
September 2026 and is cited on-page.

The organizing idea: Arizona's permit clocks live in the "regulatory bill of
rights" articles, and the county version carves every residential-lot permit
out. So a CITY house permit carries posted time frames, one comprehensive
request for corrections, a 15-working-day denial notice, an automatic refund
and a bar on mid-build plan changes — and a COUNTY house permit carries none
of it. The only county clock is inspections "at the earliest reasonable
time." The document prints the asymmetry first, then the septic and well
clocks that are the same everywhere, then a log.

Verified sources:
  § 9-831(3); § 11-1601(4)   "license" includes a permit
  § 11-1605(M)(2)       the county carve-out — every residential-lot license
  § 9-835(A)–(O)        the city clock, rule by rule
  § 9-834(D), (E)       no waiver solicitation; private civil action
  § 9-470.01(A)–(H)     15 working days → third-party review, cities ≥ 30,000;
                        the clock starts after construction documents are
                        approved
  § 11-1604; § 11-1606; § 11-1609   what still applies in a county
  § 11-862(A)           the five-member advisory board
  § 11-863(B), (C)      inspections "at the earliest reasonable time"; fees
  § 9-833(N)(2)         inspection-rights statute excludes scheduled inspections
  § 9-467(A); § 11-321(G)   the CO as a reporting event
  § 32-1121(A)(5)       the CO or completion starts the one-year clock
  Graham County FAQ; Cochise OBA Secs. 5, 12, 15, 16; Coconino AMMP page;
  Greenlee County Engineer letter   local sequences and what issues no CO
  A.A.C. R18-9-A301(D); A316   septic authorizations; transfer inspection
  § 45-596(D), (E); § 45-600   drilling card, one-year completion, reports

DELIBERATELY NOT CLAIMED, and why:
  - Any review time in days for a COUNTY permit. § 11-1605(M)(2) removes the
    statute; a number would invent a right that does not exist.
  - A statewide inspection list. None exists; IRC R109 as locally adopted.
  - A permit life or fee. Local; the only verified life is Cochise's 36 months.
  - What any utility requires before setting a meter. Not fetched.
  - § 9-833 as an inspection right. Its (N)(2) excludes inspections you
    schedule.
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
ars = k.ars
aac = k.aac
NB = k.NB
CITE = k.CITE_COL

FORM_ID = "AZ.3"
FORM_TITLE = "Inspection Sequence & Clocks"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The clocks that run against a city permit counter and not a county "
    "one, the two authorizations on the septic system, the certificate of "
    "occupancy you may never get, and a log.")

flow.append(k.disclaimer(
    "No Arizona statute names a residential building inspection; the "
    "sequence is IRC R109 as your ordinance adopted it. What the statutes do "
    "fix — and fix differently for a city and a county — is how long the "
    "counter may take and what happens when it takes longer. Read your "
    "column."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- asymmetry
flow += k.h2_tight("THE CITY/COUNTY ASYMMETRY — READ YOUR COLUMN", reserve=2.4)
flow.append(k.body(
    f"Both the city and the county \"regulatory bill of rights\" articles "
    f"define \"license\" to include \"the whole or part of any … permit, "
    f"certificate, approval, registration, charter or similar form of "
    f"permission required by law\" ({ars('9-831(3)')}; {sec('11-1601(4)')}). "
    f"Then the county version takes the house back out:"))
flow.append(k.callout(
    f"Arizona Revised Statutes {sec('11-1605(M)')}, verbatim", [
        Paragraph("\"This section does not apply to a license that is either: "
                  "1. Issued within seven working days after receipt of the "
                  "initial application or a permit that expires within "
                  "twenty-one working days after issuance. <b>2. Necessary "
                  "for the construction or development of a residential lot, "
                  "including swimming pools, hardscape and property walls, "
                  "subdivisions or master planned community.</b>\"",
                  S["body"]),
        Paragraph(f"The city version exempts only the seven-day and "
                  f"twenty-one-day permits ({sec('9-835(O)')}). So every "
                  f"clock, the one-request rule, the refund and the "
                  f"mid-build bar below apply to a <b>city</b> house permit, "
                  f"and none of them applies to a <b>county</b> one. Any "
                  f"table that shows counties reviewing faster than cities "
                  f"has this backwards.", S["body"]),
    ]))
flow.append(Spacer(1, 4))
rows = [
    [k.cellp("<b>Review time frame</b>"),
     k.cellp("Posted on the city's website — an overall time frame, split "
             "into administrative completeness and substantive review "
             "(§&#160;9-835(A), (B))"),
     k.cellp("<b>None.</b> Ask in writing under §&#160;11-1609 what the "
             "county's practice is, knowing it is not enforceable by "
             "refund")],
    [k.cellp("<b>Corrections</b>"),
     k.cellp("\"one comprehensive written or electronic request for "
             "corrections\" ((G))"),
     k.cellp("As many as the county wants")],
    [k.cellp("<b>Denial</b>"),
     k.cellp("Not for a residential application unless the city notified "
             "you within 15 working days of submission that it may be "
             "denied for \"excessive substantive deficiencies\" ((G))"),
     k.cellp("No statutory limit")],
    [k.cellp("<b>Refund</b>"),
     k.cellp("Automatic if the city exceeds its time frame or its one "
             "request ((K))"),
     k.cellp("None")],
    [k.cellp("<b>Mid-build plan changes</b>"),
     k.cellp("Barred while you build to the approved plan ((N))"),
     k.cellp("No statutory bar")],
    [k.cellp("<b>Inspections</b>"),
     k.cellp("IRC R109 as adopted; no statutory clock"),
     k.cellp("\"at the earliest reasonable time\" (§&#160;11-863(B)) — the "
             "only county clock on a house")],
    [k.cellp("<b>What both owe you</b>"),
     k.cellp("The counter handout; no unauthorized conditions; a written "
             "clarification within 30 days (§§&#160;9-834, 9-836, 9-839)"),
     k.cellp("The same three (§§&#160;11-1604, 11-1606, 11-1609)")],
]
flow.append(k.ref_table(
    "One house, two regimes",
    [k.cellp("", bold=True), k.cellp("City permit", bold=True),
     k.cellp("County permit", bold=True)],
    rows, [1.45 * inch, (CW - 1.45 * inch) * 0.55, (CW - 1.45 * inch) * 0.45]))
flow.append(k.cite(
    "If speed matters and you have a choice of lots, this table is the "
    "reason to prefer one inside city limits. If you are in a county, the "
    "§&#160;11-1609 letter — a written answer within thirty days — is the "
    "only clock you can start yourself, and AZ.5 has the template."))

# ---------------------------------------------------------------- city clock
flow += k.h2_tight("THE CITY CLOCK — A.R.S. § 9-835, RULE BY RULE", reserve=2.4)
rows = [
    [k.cellp("<b>Posted time frames</b>"),
     k.cellp("A city \"shall have in place an overall time frame during which "
             "the municipality will either grant or deny each type of "
             "license,\" stating separately \"the administrative "
             "completeness review time frame and the substantive review "
             "time frame,\" posted on its website"),
     k.cellp(f"{ars('9-835(A)')}, (B)")],
    [k.cellp("<b>Completeness</b>"),
     k.cellp("Notice of completeness or of \"a comprehensive list of the "
             "specific deficiencies\" within the completeness time frame; "
             "if none issues, \"the application is deemed administratively "
             "complete.\" The clock suspends until the missing information "
             "arrives"),
     k.cellp(f"{sec('9-835(D)')}–(F)")],
    [k.cellp("<b>One request for corrections</b>"),
     k.cellp("\"During the substantive review time frame, a municipality "
             "may make one comprehensive written or electronic request for "
             "corrections,\" amendable once to add missed legal "
             "requirements \"and the legal authority for the "
             "requirements\"; supplemental requests \"limited to issues "
             "previously identified.\" \"Within ten working days after a "
             "request by the applicant, the municipality shall meet or "
             "discuss with the applicant the request for corrections\""),
     k.cellp(sec("9-835(G)"))],
    [k.cellp("<b>The residential no-denial rule</b>"),
     k.cellp("\"a municipality may not deny a residential license "
             "application that is necessary for land development or "
             "building construction unless the municipality considers the "
             "application withdrawn or the municipality has notified the "
             "applicant and the property owner within fifteen working days "
             "after the submission of the application that the application "
             "may be subject to denial because of excessive substantive "
             "deficiencies\""),
     k.cellp(sec("9-835(G)"))],
    [k.cellp("<b>Extension; denial contents</b>"),
     k.cellp("Extension only by mutual written agreement, not more than "
             "50% of the overall time frame. A denial must state its "
             "statutory, ordinance or code justification, the appeal route "
             "with the number of working days to protest, and the "
             "resubmittal fee"),
     k.cellp(f"{sec('9-835(I)')}, (J)")],
    [k.cellp("<b>The automatic refund</b>"),
     k.cellp("If a city \"makes more than one comprehensive … request for "
             "corrections and one supplemental … request … to a license "
             "application necessary for residential building construction … "
             "or does not issue … within the overall time frame,\" it "
             "\"shall refund to the applicant all fees charged for "
             "reviewing and acting on the application.\" It \"shall not "
             "require an applicant to submit an application for a "
             "refund,\" must pay within thirty working days, and the "
             "refund \"may not be waived by an applicant\""),
     k.cellp(sec("9-835(K)"))],
    [k.cellp("<b>Resubmittal fees</b>"),
     k.cellp("After a denial, nothing beyond \"the cost of processing the "
             "resubmitted revisions or corrections\"; after a withdrawal, "
             "not more than 50% of the original unrefunded fee"),
     k.cellp(f"{sec('9-835(L)')}, (M)")],
    [k.cellp("<b>No mid-build changes</b>"),
     k.cellp("A city \"may not modify, rescind or request any subsequent "
             "modifications or revisions to an approved plan or permit for "
             "residential land development or residential building "
             "construction during construction if the construction is done "
             "in accordance with the approved plan or permit\" — unless a "
             "field condition unknown at review, your own request, or a "
             "code noncompliance the city had not already ruled on"),
     k.cellp(sec("9-835(N)"))],
    [k.cellp("<b>Waiver; enforcement</b>"),
     k.cellp("\"A municipality shall not request or initiate discussions "
             "with a person about waiving that person's rights.\" Private "
             "civil action; the court \"may award reasonable attorney fees, "
             "damages and all fees associated with the license "
             "application\""),
     k.cellp(f"{ars('9-834(D)')}, (E)")],
]
flow.append(k.ref_table(
    "What a city permit counter owes you, and what it costs the city to miss",
    [k.cellp("Rule", bold=True), k.cellp("The text", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - CITE, CITE]))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    f"{ars('9-470.01')} — fifteen working days, then a third-party reviewer "
    f"(cities of 30,000 or more)", [
        Paragraph("\"If a municipality with a population of thirty thousand "
                  "persons or more does not approve, conditionally approve "
                  "or respond with required additions or revisions to an "
                  "application for a single-family residential building "
                  "permit <b>within fifteen working days after the date the "
                  "application is submitted</b>, any required review of the "
                  "application may be performed by a qualified third party "
                  "selected by the municipality … A municipality shall "
                  "maintain a list of at least three third-party "
                  "reviewers.\" The city \"may not request or require an "
                  "applicant to waive a deadline\" ((C)); you may appeal any "
                  "decision ((D)); you pay the third party's fees to the "
                  "city ((F)); hillside ordinances and federal floodplain "
                  "reviews are outside it ((G)); the building official's "
                  "power to withhold a certificate of occupancy is untouched "
                  "((H)).", S["body"]),
        Paragraph("<b>The catch, verbatim:</b> \"The time frame prescribed by "
                  "this subsection does not begin until the applicant has "
                  "satisfied the following requirements: 1. The municipality "
                  "has approved construction documents for the dwelling to "
                  "be constructed. 2. The municipality has approved vertical "
                  "construction activities to begin … on the individual "
                  "lot.\" Read with the definition in (I), the fifteen days "
                  "for a one-off custom house appear to attach to the steps "
                  "<i>after</i> the construction documents are approved — "
                  "permit issuance — not to the plan review itself. That is "
                  "this kit's reading, not the statute's words; confirm it "
                  "with your city in writing before you count on a "
                  "fifteen-day plan review.", S["body"]),
    ]))

# ---------------------------------------------------------------- county
flow += k.h2_tight("WHAT A COUNTY STILL OWES YOU", reserve=2.2)
rows = [
    [k.cellp("<b>No unauthorized conditions</b>"),
     k.cellp("A county \"shall not base a licensing decision in whole or in "
             "part on a licensing requirement or condition that is not "
             "specifically authorized by statute, rule, ordinance or "
             "code,\" and prints the section on every application"),
     k.cellp(f"{ars('11-1604(A)')}, (H)")],
    [k.cellp("<b>The handout</b>"),
     k.cellp("At application: the list of steps, the time frames, a contact, "
             "the website, and notice of the clarification right"),
     k.cellp(ars("11-1606"))],
    [k.cellp("<b>Clarification in 30 days</b>"),
     k.cellp("A written request — name, address, the provision, the facts, "
             "your proposed interpretation, whether it is pending on an "
             "application — draws \"a written explanation of its "
             "interpretation or application\" within thirty days"),
     k.cellp(ars("11-1609"))],
    [k.cellp("<b>Inspections</b>"),
     k.cellp("County inspection rules \"shall require that such inspections "
             "be made at the earliest reasonable time.\" Fees: "
             "\"reasonable\" — no state schedule"),
     k.cellp(f"{ars('11-863(B)')}, (C)")],
    [k.cellp("<b>Alternatives and interpretations</b>"),
     k.cellp("Every county code \"shall contain a provision for an advisory "
             "board consisting of at least five members\" — an architect, "
             "an engineer, a licensed general contractor, a member of the "
             "public and a tradesperson — \"to determine the suitability of "
             "alternative materials and construction and to permit "
             "interpretations.\" In a city, every denial must name the "
             "appeal route (§&#160;9-835(J)(2))"),
     k.cellp(ars("11-862(A)"))],
]
flow.append(k.ref_table(
    "The county rules that survive the carve-out",
    [k.cellp("", bold=True), k.cellp("The statute", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.55 * inch, CW - 1.55 * inch - CITE, CITE]))

# ---------------------------------------------------------------- inspections
flow += k.h2_tight("THE BUILDING INSPECTIONS — IRC R109 AS YOUR ORDINANCE "
                   "ADOPTED IT", reserve=2.2)
flow.append(k.body(
    f"Nothing in Title 9 or Title 11 names an inspection. The sequence is "
    f"the model code's — foundation, rough plumbing, mechanical and "
    f"electrical, frame, final — as amended locally, and the local lists "
    f"read for this kit look like it: Graham County's is setback, footing, "
    f"framing, rough electrical, mechanical and plumbing, drywall and final. "
    f"Cochise Option 1 requires \"only limited Building Code inspections "
    f"dealing with the trade areas of Mechanical, Electrical, Plumbing and "
    f"Fire Prevention,\" requested \"at least twenty-four (24) hours in "
    f"advance\" (OBA Secs. 5, 15). <b>Ask for the jurisdiction's own "
    f"list</b> — the §&#160;9-836 / §&#160;11-1606 handout should carry it "
    f"— and write it on the log."))
flow.append(k.body(
    f"<b>The inspection-rights statute does not cover the inspections you "
    f"book.</b> {ars('9-833')} \"Does not apply to a municipal inspection "
    f"that is requested and scheduled by the regulated person\" ((N)(2)) — "
    f"which every routine building inspection is. This kit does not cite it "
    f"as a right."))
flow.append(k.callout(
    "Where nobody inspects the wiring — ask the utility before you frame", [
        Paragraph("In Greenlee County the engineer's letter says the county "
                  "\"does not inspect construction.\" Under Cochise Option 2 "
                  "there are \"no building code inspections.\" Coconino's "
                  "AMMP page says the program yields no utility \"green "
                  "tag.\" What APS, SRP, TEP, UniSource or your cooperative "
                  "requires before it will set a meter on an uninspected "
                  "house is in that utility's own service-requirements "
                  "manual, which this kit did not read. <b>Get the "
                  "utility's clearance rule in writing before framing</b>, "
                  "and write it on the record in AZ.2. The Cochise amendment "
                  "is candid about the alternative: no dwelling built under "
                  "it \"shall be required to be connected to a source of "
                  "electrical power, or wired\" (Sec. 21).", S["body"]),
    ]))

# ---------------------------------------------------------------- CO
flow += k.h2_tight("THE CERTIFICATE OF OCCUPANCY — AND THE THREE PLACES IT "
                   "NEVER COMES", reserve=2.2)
flow.append(k.body(
    f"No Arizona statute requires a certificate of occupancy for a "
    f"single-family dwelling; the requirement is the locally adopted IRC "
    f"R110 as amended. State law mentions the CO twice: as a reporting event "
    f"to the assessor and the Department of Revenue ({ars('9-467(A)')}; "
    f"{sec('11-321(G)')}), and as one of the two starts of the one-year "
    f"no-sale clock — \"completion or issuance of a certificate of "
    f"occupancy\" ({sec('32-1121(A)(5)')}). Greenlee County issues none. "
    f"Cochise Option 2 yields none and Option 1 a \"conditioned\" one (OBA "
    f"Sec. 16). The Coconino AMMP yields none. <b>In those programs it "
    f"cannot be obtained later</b>, a lender or buyer will ask for it, and "
    f"the only start date for the one-year clock is \"completion\" — so "
    f"write down the day the house was finished, with a photograph, and "
    f"keep every inspection record you do have."))

# ---------------------------------------------------------------- septic/well clocks
flow += k.h2_tight("SEPTIC AND WELL — THE CLOCKS THAT ARE THE SAME EVERYWHERE",
                   reserve=2.4)
rows = [
    [k.cellp("<b>Construction Authorization</b>"),
     k.cellp("No construction before it issues; \"A person shall complete "
             "construction within two years of receiving a Construction "
             "Authorization\" or the Notice of Intent expires. Changes that "
             "still conform need no re-approval but go on the site plan"),
     k.cellp(aac("R18-9-A301(D)"))],
    [k.cellp("<b>Discharge Authorization</b>"),
     k.cellp("On the Request for Discharge Authorization, with the final "
             "site plan and the tank watertightness certification; the "
             "county \"may inspect the facility before issuing.\" Book the "
             "before-backfill inspection with the county — do not cover a "
             "trench on your own schedule"),
     k.cellp(f"{aac('R18-9-A301(D)')}; A309(C)")],
    [k.cellp("<b>ADEQ's posted review clock</b>"),
     k.cellp("On the Notice of Intent form itself: 42 business days "
             "administrative + 31 substantive = 73 overall for a single "
             "4.02 permit; each alternative-setback request \"adds eight "
             "business days.\" A delegated county's clock is the county's — "
             "and a county residential permit sits outside "
             "§&#160;11-1605"),
     k.cellp("ADEQ DWS 402, rev. April 2025 (R18-1-525)")],
    [k.cellp("<b>Transfer inspection — if you sell</b>"),
     k.cellp("\"Within six months before the date of property transfer, the "
             "person who is transferring a property served by an on-site "
             "wastewater treatment facility shall retain an inspector to "
             "perform a transfer of ownership inspection\" — an "
             "ADEQ-qualified engineer, sanitarian, septage hauler, "
             "ROC-licensed septic contractor or certified operator. The "
             "tank must have been pumped unless the facility \"was put into "
             "service within 12 months before\"; no inspection if it was "
             "never put into service. The buyer files a Notice of Transfer "
             "within 15 calendar days"),
     k.cellp(aac("R18-9-A316"))],
    [k.cellp("<b>Well — drilling card</b>"),
     k.cellp("Within 15 days of a complete notice ADWR mails the drilling "
             "card to the driller; \"The well shall be completed within one "
             "year after the date of the notice\""),
     k.cellp(f"{ars('45-596(D)')}, (E)")],
    [k.cellp("<b>Well — reports</b>"),
     k.cellp("The driller's report within 30 days of completion; <b>your</b> "
             "completion report within 30 days after the pump is installed"),
     k.cellp(ars("45-600"))],
]
flow.append(k.ref_table(
    "ADEQ, your delegated county, and ADWR",
    [k.cellp("", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - CITE, CITE]))
flow.append(k.cite(
    "<b>Permit life is local.</b> The only verified figure in the state is "
    "Cochise's: 36 months, one 12-month extension on written request with "
    "substantial progress (OBA Sec. 12). Ask for yours and write it on the "
    "AZ.2 record. An owner-builder who sells inside the one-year window is "
    "selling a house with a septic system under a year old, and "
    "R18-9-A316(C)(2)(a) is written for exactly that case."))

# ---------------------------------------------------------------- log
# 2.6in: the log's first row carries a bold lead, a wrapped line and a field
# line, so title + header + first row run ~2.3in.
flow += k.h2_tight("INSPECTION LOG — RECORD EVERY REQUEST AND EVERY VISIT",
                   reserve=3.0)
# Field labels are kept to "Asked / Done / Result" and the task column
# widened (date 0.9in, notes 1.8in) so the three rules pack on ONE line —
# "Requested / Done / Result" wrapped to two and cost the log a page.
flow += k.check_table(
    "Every visit, whoever required it — and the date you asked, which is the "
    "only clock a county recognizes",
    [
        ("<b>Septic site investigation</b> — by the registered engineer, "
         "geologist, sanitarian or certified investigator (name):",
         [("Investigator", 0.5), ("Done", 0.25), ("Report", 0.25)]),
        ("<b>Zoning setback, then footing / foundation</b> — the "
         "§ 11-815(B) sketch on file; footing if a code is enforced on my "
         "permit.", [("Asked", 0.34), ("Done", 0.33), ("Result", 0.33)]),
        ("<b>Septic before backfill</b> — the county's inspection; tank "
         "watertightness certified.",
         [("Asked", 0.34), ("Done", 0.33), ("Result", 0.33)]),
        ("<b>Rough plumbing, mechanical, electrical</b> — Cochise Option 1 "
         "inspects these only; 24 hours' notice.",
         [("Asked", 0.34), ("Done", 0.33), ("Result", 0.33)]),
        ("<b>Frame</b>, then <b>drywall / insulation</b> where the local "
         "list has it — and the energy method my ordinance requires, if "
         "any.", [("Asked", 0.34), ("Done", 0.33), ("Result", 0.33)]),
        ("<b>Utility clearance</b> — what the power company needed, and the "
         "date the meter was set.",
         [("Requirement", 0.5), ("Meter set", 0.5)]),
        ("<b>Septic Discharge Authorization</b> received — no discharge "
         "before this.", [("Asked", 0.5), ("DA issued", 0.5)]),
        ("<b>Well</b> — drilling card at the site; completion; driller's "
         "report; my completion report within 30 days of the pump.",
         [("Card", 0.25), ("Done", 0.25), ("Driller's rpt", 0.25),
          ("Mine", 0.25)]),
        ("<b>Final</b>, and the <b>certificate of occupancy</b> if one "
         "issues where I am building — or the dated, photographed record "
         "of completion if none will.",
         [("Final", 0.34), ("CO no.", 0.33), ("Completion", 0.33)]),
        ("Any inspection my jurisdiction requires that is not on this list "
         "— ask, and write it here:", [("Inspection", 0.5), ("Date", 0.5)]),
    ], date_w=0.9, notes_w=1.8)
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "az-permit-kit",
                       "AZ.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
