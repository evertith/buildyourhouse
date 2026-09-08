#!/usr/bin/env python3
"""NY.1 Who Enforces Your House.

Every other state's document 1 in this series walks an owner-builder
exemption: the paragraph that lets you act as your own contractor, and the
conditions attached to it. New York has no such paragraph, because it has no
state contractor license to be exempt FROM. The Department of State's own FAQ
says licensing "is not handled by this Division," and Executive Law Article 18
contains no licensing provision at all.

So the document that earns its place here answers the three questions New York
actually poses, which no other state in the program poses in the same form:

  1. WHICH GOVERNMENT ISSUES MY PERMIT. Executive Law § 381(2) runs enforcement
     down a ladder — town/village/city → county → Department of State — and
     the code never lapses on any rung (§§ 371(2)(c), 379(3), 383(1)).
  2. THE PERMIT GATE. General Municipal Law § 125 and Workers' Compensation
     Law § 57: no permit without carrier forms C-105.2 and DB-120.1, or an
     affidavit of no employees — Form CE-200, "Apply as a Homeowner,"
     job-specific per permit. No other state's owner-builder page has this.
  3. THE ALL-ELECTRIC CLOCK. Executive Law § 378(19) and 19 NYCRR Subpart
     1229-2, suspended by a stipulation whose 120-day clock started when the
     Second Circuit's mandate issued on 2 September 2026.

Every New York claim in this document was read against its primary source in
September 2026 and is cited on-page.

Verified sources:
  Exec. Law § 371(2)(c), § 383(1)  the code is in force everywhere; supersedes
                                   inconsistent local law
  Exec. Law § 379(1)–(3)           no municipality may make the code more or
                                   less restrictive; Code Council approval for
                                   more-restrictive local standards; zoning
                                   stays local
  Exec. Law § 383(1)(c)            the NYC carve-out
  Exec. Law § 381(2)               the ladder, verbatim; § 372(11) "local
                                   government" excludes a county
  Exec. Law § 381(1)               minimum standards; no periodic inspection of
                                   owner-occupied one- and two-family dwellings
  Exec. Law § 382(2)               $1,000/day, names "any owner, builder"
  19 NYCRR Part 1202               where DOS is the permit office
  19 NYCRR Part 1203               the floor every local program must meet
  GML § 125; WCL § 57(1)           the permit gate, verbatim
  WCB BIZ-ContractREQs-fs-1-v12    C-105.2, U-26.3, DB-120.1; ACORD not
                                   acceptable; CE-200 via Business Express
  WCB-Exemption-Instr-1-v3         "Apply as a Homeowner"; job-specific
  Labor Law § 240(1)               "contract for but do not direct or control"
  19 NYCRR § 1219.2(a); § 1220.2   2025 RCNYS adopted; effective 31 Dec 2025
  2025 RCNYS Ch. 34 header         NEC 2023 basis; [NY] E3401.2.1
  Exec. Law § 378(19)              the all-electric statute
  19 NYCRR § 1229-2.4(a)(1)        "substantially complete building permit
                                   application"
  Mulhern Gas v. Mosley, Dkt. 75   Stipulation and Order, 18 Nov 2025, ¶¶ 2, 4
  2d Cir. 25-2041 docket           rehearing denied 26 Aug 2026; mandate 2 Sep
                                   2026

DELIBERATELY NOT CLAIMED, and why:
  - A list of municipalities where DOS or the county is the permit office.
    DOS says only "a limited number"; no list was retrievable. The document
    prints the verification step instead.
  - Whether a homeowner paying day labor becomes an "employer" under WCL § 2.
    A legal question the Board's homeowner path does not answer; the document
    says so and sends the reader to the Board or a lawyer.
  - Any "October 28, 2026" all-electric date. Secondary-source arithmetic
    from the decision date; the stipulation counts from the MANDATE.
  - Which code edition governs a permit applied for before 31 December 2025.
    No grandfathering rule exists in Part 1203 or the Notice of Adoption.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

import kit as k

S = k.S
CW = k.CW
sec = k.sec
NB = k.NB
CITE = k.CITE_COL

FORM_ID = "NY.1"
FORM_TITLE = "Who Enforces Your House"
TOPIC = "Who Enforces"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Which of three governments issues your permit, the workers' compensation "
    "form that gates it, and the court-set date that decides whether you may "
    "run a gas line.")
flow.append(k.disclaimer())

flow.append(k.body(
    "Start with the sentence that settles the question most guides spend a "
    "page hedging. It is state policy to “<b>insure that the uniform code be "
    "in full force and effect in every area of the state</b>” (Executive Law "
    f"{sec('371(2)(c)')}), and the code “shall supersede any other provision "
    "of a general, special or local law, ordinance, administrative code, rule "
    f"or regulation inconsistent or in conflict therewith” ({sec('383(1)')}). "
    "There is no rural exception, no acreage exception and no county that "
    "has escaped it. Outside New York City, the 2025 Uniform Code is the code "
    "your house must meet."))
flow.append(k.body(
    "What varies is <b>who administers it on your lot</b>. New York is often "
    "described as having towns that “opted out” of the code. The word appears "
    "nowhere in the statute: a local government may decline to <i>enforce</i>, "
    "and the job then passes to the county, and from the county to the "
    "Department of State. Nobody is ever left without a permit office. What "
    "changes is which office, which fee, which local law and which inspector."))
flow.append(k.callout(
    "The error this document exists to correct", [
        Paragraph("There is no owner-builder exemption in New York, and "
                  "guides that promise you one are describing another state. "
                  "New York issues no contractor license, so there is nothing "
                  "to be exempt from. What New York has instead — and what "
                  "no owner-builder page prints — is a <b>permit gate about "
                  "employees, not licenses</b>: General Municipal Law "
                  f"{sec('125')}. That section, the enforcement ladder, and "
                  "the all-electric clock are the three things this document "
                  "is about.", S["body"]),
    ]))

# ------------------------------------------------------------- the ladder
# 1.5in, not 2.2: the intro callout ends ~1.9in from the foot of page 1, and
# the full reserve threw this heading and its three-line lead to page 2 while
# the § 381(2) box (whose title band is glued to its first paragraph) would
# have moved anyway. The heading plus its lead fit in 1.5in; the box follows
# on page 2 either way.
flow += k.h2_tight("FIRST: WHICH GOVERNMENT ISSUES YOUR PERMIT", 1.5)
flow.append(k.body(
    "Executive Law " + sec("381(2)") + " is the section that does the work. "
    "It is long, and it is worth reading in the statute's own words because "
    "every guide paraphrases it into something it does not say."))
flow.append(k.callout_long(
    f"Executive Law {sec('381(2)')} — who administers and enforces", [
        Paragraph("“Except as may be provided in regulations of the secretary "
                  "pursuant to subdivision one of this section, <b>every local "
                  "government shall administer and enforce</b> the uniform "
                  "fire prevention and building code and the state energy "
                  "conservation construction code on and after the first day "
                  "of January, nineteen hundred eighty-four, provided, "
                  "however, that a local government may enact a local law "
                  "prior to the first day of July in any year providing that "
                  "it will not enforce such codes on and after the first day "
                  "of January next succeeding.", S["body"]),
        Paragraph("In such event <b>the county</b> in which said local "
                  "government is situated shall administer and enforce such "
                  "codes within such local government … unless the county "
                  "shall have enacted a local law providing that it will not "
                  "enforce such codes within that county. In such event "
                  "<b>the secretary</b> in the place and stead of the local "
                  "government shall, directly or by contract, administer and "
                  "enforce the uniform code and the state energy conservation "
                  "construction code. … Local governments or counties may "
                  "charge fees to defray the costs of administration and "
                  "enforcement.”", S["body"]),
    ]))
flow.append(k.cite(
    f"“Local government” is defined at {sec('372(11)')} as “a village, town "
    "(outside the area of any incorporated village) or city.” <b>A county is "
    "not a local government under Article 18</b> — it is the first fallback. "
    "The same subdivision lets two or more local governments run a joint "
    "program under General Municipal Law Article 5-G, and lets a local "
    "government contract with its county, which is why several counties run "
    "enforcement for many of their towns by agreement."))

rows = [
    [k.cellp("<b>1</b>"), k.cellp("Your town, village or city"),
     k.cellp("The default. The local government runs a code enforcement "
             "program under its own local law, which must meet the Part 1203 "
             "floor. You apply at the town, village or city hall; the fee is "
             "set by that legislative body's resolution. Inside an "
             "incorporated village, the <b>village</b> is your local "
             "government, not the town around it.")],
    [k.cellp("<b>2</b>"), k.cellp("Your county"),
     k.cellp("Where the local government enacted a local law declining to "
             "enforce — or contracted the job to the county under "
             f"{sec('381(2)')}. The county's code office issues the permit and "
             "sends the inspector. The local government “shall not administer "
             "and enforce the uniform code, and shall not charge or collect "
             f"fees” ({sec('381(5)(a)')}).")],
    [k.cellp("<b>3</b>"), k.cellp("The Department of State"),
     k.cellp("Where the county also declined, or where DOS has taken a program "
             "over. 19 NYCRR Part 1202 governs: the permit issues “from the "
             f"department” ({sec('1202.3(a)')}), the application is signed by "
             "the building owner <b>and the landowner</b> if different, "
             "<b>you</b> supply the snow, wind, frost and seismic design "
             f"criteria ({sec('1202.12')}), and you pay any third-party "
             "inspection fee. DOS says it holds this role for “only a limited "
             "number of local governments.” NY.4 has the detail.")],
]
flow.append(k.ref_table(
    f"The three rungs — Executive Law {sec('381(2)')}",
    [k.cellp("", bold=True), k.cellp("Permit office", bold=True),
     k.cellp("What it means for you", bold=True)],
    rows, [0.4 * inch, 1.75 * inch, CW - 2.15 * inch]))
flow.append(Spacer(1, 6))

flow.append(k.body(
    "<b>No list of which rung applies where was retrievable when this kit "
    "was assembled</b>, and this kit does not guess. The answer is one "
    "question to one clerk, and it is the most valuable question you will "
    "ask all year."))
flow += k.check_table(
    "Find your rung — do these in order", [
        "Identify whether the parcel is inside an incorporated village. If it "
        "is, the village is your local government; if not, the town (or the "
        "city).",
        "Ask that local government's clerk: “Does the municipality have a "
        "code enforcement program under 19 NYCRR Part 1203, and who is the "
        "code enforcement officer?” If yes, you are on rung 1.",
        "If the clerk says the town does not enforce, ask whether the "
        "<b>county</b> administers the Uniform Code there, and which county "
        "office. If yes, rung 2.",
        "If neither, the Department of State is your permit office under "
        "Part 1202. Start at the DOS regional office for your county — "
        "NY.4 has the address.",
        "Ask whichever office answers for a copy of its <b>code enforcement "
        "local law</b> and its current <b>fee schedule</b>. Part 1203 sets no "
        "fee and no review clock; the local law does.",
        "Get the answer in writing, date it, and write it on the directory "
        "page in NY.4. The office that issues the permit is the office whose "
        "inspector signs your certificate of occupancy.",
    ], notes_header="Confirmed with / notes")

flow.append(k.body(
    "<b>Why the rung changes the process but not the house.</b> No "
    "municipality “shall have the power to supersede, void, repeal or make "
    "more or less restrictive any provisions of this article” (Executive Law "
    f"{sec('379(3)')}); a stricter local construction standard exists only "
    "where the State Fire Prevention and Building Code Council has approved "
    f"it ({sec('379(1)')}–(2)), and a building official may not “waive, vary, "
    "modify, or otherwise alter” any provision ([NY] R104.2.2). What stays "
    "local is everything “as to which the uniform fire prevention and "
    "building code does not provide” — zoning, fees, the optional exemption "
    "list, and trade licensing."))

# --------------------------------------------------------------- licensing
flow += k.h2_tight("WHAT NOBODY CAN ASK YOU FOR: A CONTRACTOR LICENSE", 2.0)
flow.append(k.body(
    "New York issues no general contractor, electrician or plumber license "
    "at state level — not to you, and not to the people you hire. The "
    "Division of Building Standards and Codes states it on its own FAQ page: "
    "“<b>Issues regarding local laws, zoning, and licensing of contractors "
    "or electricians are not handled by this Division.</b>” Executive Law "
    "Article 18 contains no licensing provision. There is no owner-builder "
    "exemption in New York because there is nothing to be exempt from."))
flow.append(k.body(
    "Two things follow. <b>Whether you may do your own wiring or plumbing is "
    "a local licensing question</b>, decided by the municipality under "
    f"{sec('379(3)')}; there is no statewide registry, so ask the clerk and "
    "the county consumer-affairs office whether a local electrician, plumber "
    "or home-improvement license law exists (NY.4 sets out the five county "
    "laws that were read). And <b>a manufactured home is a different "
    "path</b> — 19 NYCRR Part 1210 certifies installers, and an owner-occupant "
    "“may apply for certification as the installer” (DOS FAQ) — which this "
    "kit does not cover."))

# --------------------------------------------------------------- the gate
# 1.0in: this heading has a two-line lead and is then followed by the GML
# § 125 box, whose title band is glued to its first paragraph and moves as a
# unit whenever it does not fit. A 2.4in reserve moved heading, lead and box
# together and left 1.4in blank; the heading and lead fit in an inch.
flow += k.h2_tight("THE PERMIT GATE: GENERAL MUNICIPAL LAW § 125", 1.0)
flow.append(k.body(
    "This is the page no other New York owner-builder guide has, so here is "
    "the statute itself, verbatim and complete."))
flow.append(k.callout_long(
    f"General Municipal Law {sec('125')} — building permits; workers' "
    "compensation", [
        Paragraph("“No city, town or village shall issue a building permit "
                  "without obtaining from the permit applicant either:", S["body"]),
        Paragraph("1. proof duly subscribed that workers' compensation "
                  "insurance and disability benefits coverage issued by an "
                  "insurance carrier in a form satisfactory to the chair of "
                  "the workers' compensation board as provided for in section "
                  "fifty-seven of the workers' compensation law is effective; "
                  "or", S["body"]),
        Paragraph("2. <b>an affidavit that such permit applicant has not "
                  "engaged an employer or any employees</b> as those terms "
                  "are defined in section two of the workers' compensation "
                  "law to perform work relating to such building permit.”",
                  S["body"]),
    ]))
flow.append(k.cite(
    f"Workers' Compensation Law {sec('57(1)')} reaches the same result from "
    "the other side: the head of any state or municipal office “authorized or "
    "required by law to issue any permit for or in connection with any work "
    "involving the employment of employees in a hazardous employment … shall "
    "not issue such permit unless proof duly subscribed by an insurance "
    "carrier is produced in a form satisfactory to the chair, that "
    "compensation for all employees has been secured.” Note who the statute "
    f"binds: {sec('125')} names cities, towns and villages; {sec('57')} names "
    "every permit-issuing office, which is how the requirement follows your "
    "permit up the ladder to a county or to DOS."))

flow.append(Spacer(1, 4))
flow.append(k.body(
    "So the section gives an owner-builder exactly two doors, and the "
    "Workers' Compensation Board publishes the form behind each."))
rows = [
    [k.cellp("<b>Door 1 — you carry a policy</b>"),
     k.cellp("Your carrier sends the permit office <b>Form C-105.2</b>, "
             "Certificate of Workers' Compensation Insurance (the State "
             "Insurance Fund uses its own <b>Form U-26.3</b>), and "
             "<b>Form DB-120.1</b>, the disability and Paid Family Leave "
             "certificate. The Board cannot issue either to you directly, "
             "and the name and federal ID on the form must exactly match the "
             "applicant. “<b>ACORD forms are not acceptable</b> proof of New "
             "York State workers' compensation coverage under WCL §&#160;57.”"),
     ],
    [k.cellp("<b>Door 2 — you have no employees</b>"),
     k.cellp("You obtain a <b>Certificate of Attestation of Exemption, Form "
             "CE-200</b>, through New York Business Express at "
             "<b>businessexpress.ny.gov</b>. A NY.gov Business account is "
             "required. Under How to Apply, the Board's instruction sheet "
             "says: “Select <b>Apply as a Homeowner</b> (applies to those "
             "obtaining permits to work on their residence).” Print it, sign "
             "it, submit it with the application. The certificate carries a "
             "number the permit office can validate online."),
     ],
]
flow.append(k.ref_table(
    "The two doors, and the Board's forms for each",
    [k.cellp("Door", bold=True), k.cellp("What you file", bold=True)],
    rows, [1.7 * inch, CW - 1.7 * inch]))
flow.append(k.cite(
    "Forms from the Board's own sheet “Requirements for businesses applying "
    "for government permits, licenses, or contracts” (BIZ-ContractREQs-fs-1) "
    "and its CE-200 instruction sheet (WCB-Exemption-Instr-1). <b>The rule "
    "that bites:</b> “Certificates for building permits are <b>job-specific</b> "
    "and a separate certificate will be required for each building permit.” "
    "A CE-200 for the house does not cover a later permit for the garage, "
    "and it “CAN NOT be used to show another business or that business's "
    "insurance carrier that coverage is not required.”"))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "The question the form does not answer for you", [
        # Two paragraphs, not one. callout_long glues its title band to the
        # first body paragraph, so a ten-line opener made the smallest chunk
        # that could start the box ~1.9in and threw the whole box to the next
        # page behind a 1.4in gap. Split at the natural seam, the box can
        # open at the foot of a page with its title and four lines.
        Paragraph("The CE-200 attests that you have “not engaged an employer "
                  "or any employees.” An owner who hires <b>insured "
                  "subcontractors</b> is not thereby the employer of the "
                  "subs' workers — collect each trade's C-105.2 and DB-120.1 "
                  "naming you as certificate holder, and check them.",
                  S["body"]),
        Paragraph("An owner who hires individuals by the hour to swing "
                  "hammers <b>may be</b> an employer under Workers' "
                  f"Compensation Law {sec('2')}. That is a legal question "
                  "this kit does not resolve; the Board or a lawyer does. "
                  "What this kit will say: do not sign an attestation you are "
                  "not sure is true, because the permit rests on it.",
                  S["body"]),
        Paragraph("<b>The Scaffold Law has a homeowner exception, and it "
                  "turns on the same behavior.</b> Labor Law "
                  f"{sec('240(1)')} imposes its elevation-hazard duty on "
                  "“all contractors and owners and their agents, <b>except "
                  "owners of one and two-family dwellings who contract for "
                  "but do not direct or control the work</b>.” An "
                  "owner-builder who hires trades and stays out of the means "
                  "and methods is inside the exception; one who supervises "
                  "the framing crew from the deck may not be. The statutory "
                  "phrase is printed here; the case law on “direct or "
                  "control” is not summarized.", S["body"]),
    ]))

# ----------------------------------------------------------- code editions
# 1.2in: the seven-line lead under this heading splits cleanly, and the
# editions table that follows carries its own title and header.
flow += k.h2_tight("THE CODE YOU ARE BUILDING TO — 2025, SINCE 31 DECEMBER 2025",
                   1.2)
flow.append(k.body(
    "The 2025 Uniform Code (19 NYCRR Parts 1219–1229) and the 2025 Energy "
    "Code (Part 1240) were adopted 5&#160;December 2025 and took effect "
    "<b>31&#160;December 2025</b>; the option to build to the 2020 edition "
    "closed that day ([NY] R102.6). The eight code books are each "
    "“(publication date: July 2025), published by the International Code "
    f"Council” ({sec('1219.2(a)')}) — “based on the 2024 International Code "
    "Council books with New York modifications,” in DOS's words."))
# Prose, not a three-row table. The table version measured 2.6in and, with
# its own title and header, could not start in the space its lead left on
# the page — it moved whole and left 1.1in blank. The same three facts read
# fine in five lines.
flow.append(k.body(
    "Three books bind a house. The <b>2025 Residential Code of New York "
    "State</b> (RCNYS) covers detached one- and two-family dwellings and "
    "townhouses not more than three stories above grade plane; an applicant "
    f"may elect the Building Code instead for the whole building ({sec('1220.2(a)')}, "
    "(d)). Its Electrical Part, Chapters 34–43, “is based on the <b>2023 "
    "National Electrical Code</b> (NFPA 70—2023),” and anything not covered "
    "“shall comply with the applicable provisions of NFPA 70” (Chapter 34 "
    "header; E3401.2) — <b>the edition does not vary by town</b>. And the "
    "<b>2025 Energy Conservation Construction Code</b> (ECCCNYS), Residential "
    f"Provisions ({sec('1240.4(a)')}), carries New York's own insulation, "
    "window and air-leakage values — NY.2 prints them."))
flow.append(k.cite(
    "<b>The code is the regulation, not the book</b> (DOS bulletin 2026-1: "
    "“The regulations must be examined prior to reviewing the "
    "publications”). Any RCNYS section printed with a <b>[NY]</b> tag is a "
    "New York amendment. <b>No grandfathering rule was found</b> for a permit "
    "applied for before 31&#160;December 2025 — if yours was in review on "
    "that date, ask the office which edition it is reviewing against."))

# ----------------------------------------------------------- all-electric
flow += k.h2_tight("THE ALL-ELECTRIC PROVISION — A DATED STATUS BOX", 2.4)
flow.append(k.body(
    "Executive Law " + sec("378(19)(a)") + " directs that the Uniform Code "
    "“shall prohibit the installation of fossil-fuel equipment and building "
    "systems, in any new building not more than seven stories in height … "
    "on or after December thirty-first, two thousand twenty-five.” The rule "
    "that implements it is 19 NYCRR Subpart 1229-2 (and " + sec("1240.6") +
    " in the Energy Code). Both are <b>suspended by a federal court order</b> "
    "as this kit goes to print, and the suspension has a clock. Read the box; "
    "then check the date before you file."))
flow.append(k.callout_long(
    "Status on 3 September 2026 — check before you file", [
        Paragraph("<b>The trigger is the application date, not the "
                  "occupancy date.</b> The prohibition reaches buildings “for "
                  "which a <b>substantially complete building permit "
                  "application</b> for the initial construction of such "
                  "building is submitted on or after” the effective date "
                  f"(19 NYCRR {sec('1229-2.4(a)(1)')}). A substantially "
                  "complete application is one with enough information under "
                  "the stricter of your office's program or Part 1203 “such "
                  "that the authority having jurisdiction can examine the "
                  f"application” ({sec('1229-2.3(20)')}). A complete "
                  "application in before the suspension lifts is outside the "
                  "prohibition, whenever the house is built.", S["body"]),
        Paragraph("<b>The suspension.</b> In <i>Mulhern Gas Co. v. Mosley</i> "
                  "(N.D.N.Y. 1:23-cv-01267), a Stipulation and Order signed "
                  "<b>18&#160;November 2025</b> (Dkt. 75) provides that the "
                  "effective date of Subpart 1229-2 and §&#160;1240.6 “is "
                  "hereby suspended, pending final disposition of the "
                  "Plaintiffs' appeal in the Second Circuit and the "
                  "disposition of any petition for a writ of certiorari” "
                  "(¶&#160;2), and that “if no writ of certiorari is timely "
                  "sought, this suspension shall terminate automatically "
                  "<b>120&#160;days after the issuance of the mandate</b> of "
                  "the Second Circuit” (¶&#160;4).", S["body"]),
        Paragraph("<b>The clock.</b> The Second Circuit affirmed on "
                  "<b>30&#160;June 2026</b>. Rehearing en banc was denied "
                  "<b>26&#160;August 2026</b>. The mandate issued "
                  "<b>2&#160;September 2026</b> (docket 25-2041). One hundred "
                  "and twenty days from the mandate is <b>31&#160;December "
                  "2026</b>. A petition for certiorari is due about "
                  "<b>24&#160;November 2026</b>; if one is filed, the "
                  "suspension continues to the 120th day after its denial, or "
                  "after a Supreme Court judgment. <b>The widely reported "
                  "date of 28&#160;October 2026 is wrong</b> — it counts from "
                  "the decision, and the stipulation counts from the "
                  "mandate.", S["body"]),
        Paragraph("<b>DOS's own status line</b>, on its Notice of Adoption "
                  "page (“Update on Recent Court Ruling – July 2, 2026”): the "
                  "provisions “continue to be suspended by Court Order and "
                  "are neither effective nor enforceable.” <b>Before you "
                  "file, read that page and the docket.</b> If the "
                  "suspension has ended, a substantially complete application "
                  "submitted that day is inside the prohibition.", S["body"]),
    ]))
flow.append(k.cite(
    "What the rule does <i>not</i> exempt, if it takes effect: "
    f"{sec('1229-2.5')} lists manufactured homes, agricultural buildings, "
    "emergency and standby power, and a grid-infeasibility exemption on “a "
    "written determination, issued by local utility … indicating that new or "
    "expanded electric service cannot be reasonably provided.” <b>Nothing in "
    "Subpart 1229-2 exempts a single-family house, a wood stove, a propane "
    "range, or a generator used for anything but emergency or standby "
    "power.</b> Equipment is “fossil-fuel equipment” if it “uses fossil-fuel "
    f"for combustion” (Exec. Law {sec('378(19)(g)(i)')})."))

# -------------------------------------------------------------- electrical
# 1.3in: the all-electric cite above ends ~1.7in from the foot, and at 1.6 the
# reserve still fired once the h2's own 14pt spaceBefore was counted. The
# paragraph under this heading is twelve lines and splits cleanly.
flow += k.h2_tight("ELECTRICAL — THE INSPECTOR YOUR OFFICE HAS APPROVED", 1.3)
flow.append(k.body(
    "The code book says new electrical work “shall be inspected by the "
    "building official” (E3403.2). The rule above the book is more specific: "
    "electrical inspections are <b>special inspections</b>, and an office "
    "“shall not accept or rely upon a special inspection unless the person "
    "performing such special inspection (i) is a qualified person employed "
    "or retained by <b>an agency that has been approved by the authority "
    "having jurisdiction</b>” (19 NYCRR " + sec("1203.2(e)(4)") + "). Most "
    "building departments employ no electrical inspector and accept "
    "certificates from third-party agencies they have approved; there is no "
    "state list. NY.3 walks the track — and the 30-day order-to-remedy clock, "
    "the $1,000-a-day penalty that names “any owner, builder,” and your Part "
    "1205 appeal to a regional board of review, decided in 60 days. The one "
    "instruction that belongs here: <b>get your office's approved-agency "
    "list before you buy wire.</b>"))
flow.append(k.callout(
    "The sentence in the code that no other state has", [
        Paragraph("<b>[NY] E3401.2.1 Owner-occupied one-family dwellings.</b> "
                  "“Owner-occupied one-family dwellings and accessory "
                  "structures <b>shall not be required to be provided with "
                  "electrical power, wiring, devices and equipment</b>, "
                  "unless expressly required by statute, local law, ordinance, "
                  "or other regulations. If an on-site electrical power system "
                  "is installed or used, all electrical wiring, devices and "
                  "equipment in such system shall comply with Part "
                  "VIII—Electrical of this code.”", S["body"]),
        Paragraph("An owner-occupied off-grid house is lawful under the "
                  "Uniform Code; a rented one is not. Nothing similar exists "
                  "for plumbing. Check the local law — the section defers to "
                  "it — before you rely on this.", S["body"]),
    ]))

# ------------------------------------------------------------- write-ins
flow += k.h2_tight("WRITE DOWN WHAT YOU CONFIRMED", 1.6)
flow.append(k.body(
    "Everything above is statewide. These answers are yours alone, and every "
    "later document in this kit depends on them."))
flow += k.check_table(
    "Your enforcement picture", [
        ("Town / village / city, and county",
         [("Municipality", 0.5), ("County", 0.5)]),
        ("Which rung issues my permit (1 local, 2 county, 3 DOS), and who "
         "told me", [("Rung", 0.3), ("Confirmed by", 0.7)]),
        ("The code enforcement office and officer by name",
         [("Office", 0.5), ("Officer", 0.5)]),
        ("Which door I am using under GML §&#160;125 — CE-200 as a homeowner, "
         "or carrier forms C-105.2 and DB-120.1:",
         [("Door", 0.35), ("CE-200 number", 0.65)]),
        ("Does the municipality or county license electricians, plumbers or "
         "home-improvement contractors? Which?", [("Answer", 1.0)]),
        ("The electrical inspection agency the office has approved, and "
         "whether the office will accept a homeowner's own wiring:",
         [("Agency", 0.6), ("Own wiring?", 0.4)]),
        ("All-electric status on the day I file — suspended or in effect — "
         "and the source I read it from:", [("Status", 0.4), ("Source", 0.6)]),
    ], notes_header="Notes")

# --------------------------------------------------------------- sources
flow.append(Spacer(1, 4))
flow.append(k.sources_table([
    ("The Uniform Code is in force in every area of the state; New York City "
     "keeps its own code",
     "Exec. Law §§ 371(2)(c), 383(1), 383(1)(c)"),
    ("The enforcement ladder: local government → county → DOS",
     "Exec. Law § 381(2); § 372(11)"),
    ("Where DOS is the permit office: owner and landowner sign; owner "
     "supplies design criteria; third-party fees; the displaced town may "
     "not charge",
     "19 NYCRR §§ 1202.1(c), 1202.3, 1202.12; Exec. Law § 381(5)(a)"),
    ("No municipality may make the code more or less restrictive; zoning "
     "and licensing stay local; no official may waive a provision; "
     "licensing is not a DOS matter",
     "Exec. Law § 379(1)–(3); 2025 RCNYS [NY] R104.2.2; DOS Division FAQ"),
    ("No permit without carrier proof or an affidavit of no employees",
     "GML § 125; WCL § 57(1)"),
    ("C-105.2, U-26.3, DB-120.1; ACORD not acceptable; CE-200 via Business "
     "Express; homeowner path; job-specific; Scaffold Law homeowner exception",
     "WCB BIZ-ContractREQs-fs-1; WCB-Exemption-Instr-1; WCB CE-200 pages; "
     "Labor Law § 240(1)"),
    ("2025 codes adopted 5 Dec 2025, effective 31 Dec 2025; 2024 I-Code "
     "basis; Electrical Part NEC 2023-based",
     "19 NYCRR § 1219.2(a); DOS 2026-1; 2025 RCNYS Ch. 34 header"),
    ("All-electric statute and rule; the application-date trigger",
     "Exec. Law § 378(19); 19 NYCRR §§ 1229-2.3(20), 1229-2.4(a)(1), 1229-2.5"),
    ("Suspension; 120 days from the mandate",
     "Mulhern Gas v. Mosley, N.D.N.Y. Dkt. 75 ¶¶ 2, 4"),
    ("Affirmed 30 Jun 2026; rehearing denied 26 Aug 2026; mandate 2 Sep 2026",
     "2d Cir. No. 25-2041 docket"),
    ("Electrical inspections are special inspections; approved agency only",
     "19 NYCRR § 1203.2(e)(4); 2025 RCNYS E3403.2"),
    ("Owner-occupied one-family dwellings need no electrical system",
     "2025 RCNYS [NY] E3401.2.1"),
]))
flow.append(Spacer(1, 6))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ny-permit-kit",
                       "NY.1-who-enforces-your-house.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
