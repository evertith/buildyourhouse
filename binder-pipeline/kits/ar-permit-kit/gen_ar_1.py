#!/usr/bin/env python3
"""AR.1 Owner-Builder Exemption Walkthrough.

Every Arkansas claim in this document was read out of its primary source in
September 2026 and is cited on-page. Where the statute is silent, or the answer
depends on a local ordinance, the document says so and gives the verification
step rather than guessing.

Verified sources:
  Ark. Code Ann. § 17-25-513(1)  the owner-builder exemption, capped at one
                       residence per CALENDAR YEAR
  Ark. Code Ann. § 17-25-513(2),(3),(4),(5),(6)  the other residential
                       exemptions, including the $2,000 line and its
                       anti-splitting rule
  17 CAR § 295-101(6)  "Own residence" DEFINED — and the fourth branch, "a
                       residence constructed for the occupancy of the person who
                       owns the property", is what makes the exemption work for
                       a house you do not live in yet
  Ark. Code Ann. § 17-25-502(2)  "residential building contractor" expressly
                       includes one who "assumes charge in a supervisory
                       capacity or otherwise manages the construction" — so the
                       exemption covers acting as your own GC, not just swinging
                       your own hammer
  Ark. Code Ann. § 17-25-502(3)  "single family residence" runs up to FOUR units
  Ark. Code Ann. § 17-25-505(c)  unlicensed contracting is a Class A
                       misdemeanor, each day a separate offense
  Ark. Code Ann. § 17-25-101(a)(1),(c)  the $50,000 commercial threshold, and
                       its express exclusion of single-family residences
  Ark. Code Ann. § 14-56-202  cities MAY require a building permit
  Ark. Code Ann. § 14-14-802(b)  county general services power; "building codes"
                       is NOT among the enumerated services
  Ark. Code Ann. § 14-17-207(a),(f)  county planning ordinances are "zoning,
                       subdivision, setback, or entry control" — building code
                       again absent
  Ark. Code Ann. § 14-17-212  a county SHALL NOT regulate residential building
                       design elements (Acts 2019 No. 446)
  Ark. Code Ann. § 17-28-102(b) + § 17-28-101(9)  electrical homeowner
                       exemption, and the narrow "primary residence" definition
  Ark. Code Ann. § 17-28-305(b)(2),(c)  a city may demand a competency
                       demonstration; electrical permitting is local option
  Ark. Code Ann. § 17-38-302(1)  plumbing homeowner exemption — "owned AND
                       OCCUPIED", and expressly subject to local ordinance
  Ark. Code Ann. § 17-33-102(b)(1),(d)  HVACR homeowner exemption — limited to
                       an "EXISTING building or structure"
  Ark. Code Ann. § 14-236-102(b)(2)  the homeowner "retaining all rights to
                       install and repair his system"
  Ark. Code Ann. § 17-50-108(b)  a person may construct a well on their own land
                       without a license
  Ark. Code Ann. § 18-44-115  the Notice to Owner, and the lien that fails
                       without it

DELIBERATELY NOT CLAIMED, and why:
  - That Arkansas imposes a holding period, a not-for-sale window, or a resale
    clawback on an owner-builder. No such provision exists in § 17-25-513 or in
    17 CAR pt. 295. Several web guides imply one; they are wrong.
  - That an owner-builder affidavit must be filed. None exists at state level.
  - That owner-supplied materials fall outside the $2,000 test. The carve-out at
    § 17-25-101(d)(2) sits in the COMMERCIAL chapter, which excludes
    single-family residences. Reading it across is unresolved.
  - That a sub hired directly by an exempt owner-builder is sheltered by
    § 17-25-513(4). On the face of the text it is not — (4) shelters subs of a
    LICENSED contractor. The document tells the reader to verify each sub's own
    license instead of resolving the question.
  - Any statement that a particular county requires no building permit. That is
    a per-county fact and the document gives the method, not the answer.
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

FORM_ID = "AR.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "Exemption & Qualification"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What Arkansas actually lets you do yourself — and the one question about "
    "your own parcel that changes the shape of the entire build.")

flow.append(k.disclaimer(
    "Statute and rule text was read at arkleg.state.ar.us, "
    "codeofarrules.arkansas.gov and the licensing boards' own published "
    "statute books in September 2026; all of them change."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION", reserve=2.0)
flow.append(k.body(
    "Arkansas <b>does</b> license residential builders — and then exempts you "
    "from that license, in one sentence, for the house you are building for "
    "yourself. The exemption is real, it is short, and it has exactly one "
    "condition attached to it."))
flow.append(k.body(
    "So the interesting question in Arkansas is not <i>may I build it</i>. It "
    "is <b>who, if anyone, is going to inspect it</b> — and then, separately "
    "and much more dangerously, <b>which of the trade exemptions actually "
    "reaches a house that nobody lives in yet.</b> Those are three different "
    "tests written by three different boards, and they do not agree."))

rows = [
    [k.cellp("Do you need a license to build your own house?"),
     k.cellp(f"<b>No.</b> A person acting as a residential building contractor "
             f"in the construction of their own residence is exempt "
             f"({sec('17-25-513(1)')}) — <b>unless they build more than one "
             f"residence in a calendar year</b>")],
    [k.cellp("Does the exemption cover hiring subs, or only your own hands?"),
     k.cellp("<b>Both.</b> The exempt role expressly includes one who "
             f"\"assumes charge in a supervisory capacity or otherwise manages "
             f"the construction\" ({sec('17-25-502(2)')}). You may act as your "
             f"own general contractor")],
    [k.cellp("Is there a project-cost threshold?"),
     k.cellp(f"A separate exemption covers work of <b>$2,000 or less</b> "
             f"({sec('17-25-513(3)')}), and it may not be split into smaller "
             f"contracts. You do not need it — the owner-builder exemption has "
             f"<b>no dollar limit at all</b>")],
    [k.cellp("Must you own the land? Must you live in it?"),
     k.cellp("You must own it. Occupancy is where the traps are: the "
             "<b>building</b> exemption reaches a house built <i>for</i> your "
             "occupancy, but <b>each trade exemption sets its own test</b> and "
             "two of them say \"occupied\". See the trade section")],
    [k.cellp("How long must you keep it?"),
     k.cellp("<b>The statutes set no period.</b> No holding period, no "
             "not-for-sale window, no resale clawback anywhere in the "
             "residential subchapter or its rules")],
    [k.cellp("Is there a form to file?"),
     k.cellp("<b>No.</b> The exemption is self-executing — there is no "
             "state owner-builder affidavit and no exemption form. Your city "
             "may still want one")],
    [k.cellp("Do you need a building permit?"),
     k.cellp("<b>Only if your city — or, far more rarely, your county — "
             "created one.</b> This is the sentence the rest of the kit turns "
             "on. Read the next section before anything else")],
    [k.cellp("Does the building code apply either way?"),
     k.cellp("<b>Yes. Always.</b> The Arkansas Fire Prevention Code is adopted "
             "statewide and reaches one- and two-family dwellings by its own "
             "scope. Only the enforcement is optional")],
]
flow.append(k.ref_table(
    "The Arkansas position at a glance",
    [k.cellp("Question", bold=True), k.cellp("Arkansas's answer", bold=True)],
    rows, [2.45 * inch, CW - 2.45 * inch]))
flow.append(k.cite(
    "Residential licensing: Ark. Code Ann. Title 17, Chapter 25, Subchapter 5, "
    "administered by the Residential Contractors Committee of the Arkansas "
    "Contractors Licensing Board. The Board is now housed in the Arkansas "
    "Department of Labor and Licensing; the old aclb.arkansas.gov address "
    "redirects there."))

# ---------------------------------------------------------------- the exemption
flow += k.h2_tight("THE EXEMPTION, IN FULL", reserve=2.4)
flow.append(k.body(
    "Here is the whole of it. Arkansas puts the owner-builder exemption in the "
    "first two paragraphs of its residential exemptions section, and they are "
    "two different exemptions doing two different jobs."))
flow.append(k.callout_long(
    f"Ark. Code Ann. {sec('17-25-513')} — Exemptions", [
        Paragraph("\"The following shall be exempted from the licensing "
                  "requirements of this subchapter:", S["body"]),
        Paragraph("<b>(1) A person who acts as a residential building "
                  "contractor in the construction of his or her residence "
                  "unless he or she builds more than one (1) residence during "
                  "any calendar year;</b>", S["body"]),
        Paragraph("<b>(2) The owner of a single family residence acting as his "
                  "or her own home improvement contractor on his or her own "
                  "property;</b>\"", S["body"]),
        Paragraph("<b>(1) is the one you want when you are building a new "
                  "house.</b> (2) covers remodeling a home you already own, "
                  "and — worth noticing — it carries <i>no</i> annual cap in "
                  "its text at all.", S["body"]),
    ]))
flow.append(k.cite(
    "Quoted from the Arkansas Contractors Licensing Board's own publication, "
    "<i>Arkansas Residential Contractors Licensing Law — Statutes and Rules of "
    "the Residential Contractors Committee</i>, revised April 2026, page 8."))

flow.append(Spacer(1, 4))
flow.append(k.body(
    f"<b>\"Own residence\" is not left to common sense — it is defined by "
    f"rule</b>, and the definition is wider than the phrase sounds. This is "
    f"the single most useful sentence in Arkansas owner-builder law, because "
    f"without its last clause the exemption would be circular for anyone "
    f"building a house they do not live in yet:"))
flow.append(k.callout(
    "17 CAR § 295-101(6) — the definition that makes it work", [
        Paragraph("\"'Own residence', as found in Arkansas Code "
                  f"{sec('17-25-509(c)')} and {sec('17-25-513')}, means the "
                  "personal residence, the principal place of abode, the "
                  "domicile, <b>or a residence constructed for the occupancy "
                  "of the person who owns the property</b>.\"", S["body"]),
    ]))
flow.append(k.cite(
    "Read in the official Code of Arkansas Rules at "
    "codeofarrules.arkansas.gov, Title 17, and confirmed against the Board's "
    "own April 2026 publication. \"Ownership\" is separately defined at 17 CAR "
    f"{sec('295-101(1)')} as the \"sole and exclusive right to sell or convey "
    f"property.\""))

flow += k.h2_tight("THE ONE CONDITION — AND FOUR THINGS ARKANSAS NEVER SAYS",
                   reserve=2.0)
flow.append(k.body(
    "The cap is a <b>calendar year</b>, not a rolling twelve months, and it "
    "counts residences <i>built</i>, not lots owned. Build one house for "
    "yourself this year and you are inside the exemption. Start a second in "
    "the same calendar year and you have lost it for both."))
rows = [
    [k.cellp("<b>A holding period</b>"),
     k.cellp("Nothing in the subchapter or its rules requires you to keep the "
             "house for any length of time")],
    [k.cellp("<b>A \"not for sale or lease\" clause</b>"),
     k.cellp("There is none. The rule's test is that the residence was "
             "<i>constructed for the occupancy of</i> the owner — a test about "
             "purpose at the time of building, not a resale ban")],
    [k.cellp("<b>An affidavit or exemption form</b>"),
     k.cellp("No state owner-builder affidavit exists. The Board publishes "
             "license applications, bonds and complaint forms — nothing for an "
             "exempt owner")],
    [k.cellp("<b>A dollar threshold on the owner-builder exemption</b>"),
     k.cellp(f"The $2,000 figure is a <i>different</i> exemption "
             f"({sec('17-25-513(3)')}) for small jobs. Your own house is "
             f"exempt at any value")],
]
flow.append(k.ref_table(
    "Conditions people expect to find in Arkansas law, and do not",
    [k.cellp("Commonly assumed", bold=True),
     k.cellp("What the text actually shows", bold=True)],
    rows, [2.05 * inch, CW - 2.05 * inch]))
flow.append(k.cite(
    "These are negative findings. They were established by reading "
    f"{sec('17-25-513')} and the whole of 17 CAR pt. 295 in September 2026 and "
    f"finding no such provision — not by inference from silence elsewhere. If "
    f"a guide tells you Arkansas has a one-year no-sale rule, ask it for the "
    f"section number."))

# ---------------------------------------------------------------- the big one
flow += k.h2_tight("THE QUESTION THAT DECIDES YOUR BUILD", reserve=2.0)
flow.append(k.body(
    "Arkansas adopts <b>one</b> building code for the whole state and forbids "
    "your city or county from adopting a different one. What it never does is "
    "require anybody to enforce that code on a house. Three separate texts "
    "make the point, and they all use the same permissive verb."))
rows = [
    [k.cellp("<b>The code itself</b>"),
     k.cellp("Local governments \"shall only adopt and enforce the provisions "
             "of the Arkansas Fire Prevention Code, 2021 Edition… the only "
             "foundation document available for modification by local "
             "jurisdictions <b>should they choose to adopt</b> more stringent "
             "provisions\""),
     k.cellp("AFPC Vol. I<br/>§ 101.2.2")],
    [k.cellp("<b>Cities</b>"),
     k.cellp("A city of the first class <b>may</b> \"Provide that a house or "
             "structure not be erected within the city limits <b>except upon a "
             "permit</b>\"; second-class cities and incorporated towns "
             "<b>may</b> \"Enforce building and safety codes\""),
     k.cellp(sec("14-56-202"))],
    [k.cellp("<b>Counties</b>"),
     k.cellp("A county <b>may</b> \"provide through ordinance for the "
             "establishment of any service…\" — and <b>\"building codes\" is "
             "not among the services the statute lists.</b> The county "
             "planning subchapter enumerates \"zoning, subdivision, setback, "
             "or entry control ordinances\" — building code again absent"),
     k.cellp(f"{sec('14-14-802(b)')}<br/>{sec('14-17-207(a)')}")],
]
flow.append(k.ref_table(
    "Every verb is \"may\"",
    [k.cellp("Who", bold=True), k.cellp("What the text says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [0.95 * inch, CW - 2.25 * inch, 1.3 * inch]))
flow.append(k.cite(
    "The Arkansas Fire Prevention Code, 2021 Edition took effect 1 January "
    "2023 and is a state rule (015.01.22 Ark. Code R. 005). Its residential "
    "volume — Volume III — is the 2021 International Residential Code with "
    "Arkansas amendments, and by its own scope it applies to \"detached one- "
    "and two-family dwellings and townhouses not more than three stories above "
    "grade plane in height\" (§ R101.2)."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Why there is no state backstop for a house", [
        Paragraph("The building permit in the code is addressed to a "
                  "<b>building official</b> — and the Arkansas Fire Prevention "
                  "Code defines that as \"any governmental official having "
                  "authority to enforce that aspect of the Code.\" If your city "
                  "or county never created the office, there is nobody to "
                  "apply to and no permit to obtain.", S["body"]),
        Paragraph("The State Fire Marshal does not fill the gap. The only "
                  "inspection duty the statute makes <b>mandatory</b> is for "
                  "\"places of public assembly, including factories or "
                  "industrial plants normally employing ten (10) or more "
                  f"persons\" ({sec('20-22-1012(b)(1)')}). General inspection "
                  f"power is \"<i>may</i>\" ({sec('20-22-1012(a)(1)')}), and "
                  f"the Marshal's remit is aimed at \"factories, asylums, "
                  f"hospitals, churches, schools, halls, theaters, and all "
                  f"other places in which numbers of people work, live, or "
                  f"congregate\" ({sec('20-22-1010(b)(5)')}).", S["body"]),
        Paragraph("<b>So the code governs your house and, in much of rural "
                  "Arkansas, no building official will ever look at it.</b> "
                  "The standard still applies to you. So does the liability, "
                  "and so does every lender, insurer and buyer who later asks "
                  "what it was built to.", S["body"]),
    ]))

flow.append(Spacer(1, 4))
flow.append(k.body(
    f"<b>One protection worth knowing about while you are asking.</b> Since "
    f"2019 a county \"shall not regulate residential building design "
    f"elements\" ({sec('14-17-212')}, Acts 2019 No. 446) — defined to include "
    f"exterior color and cladding type, roof style and pitch, ornamentation, "
    f"window and door placement, the number and type of rooms, interior "
    f"layout, and <b>minimum square footage</b>. Building and safety code "
    f"requirements and National Flood Insurance Program conditions are carved "
    f"out of the ban. A parallel section, {sec('14-56-204')}, applies to "
    f"cities. If a county tells you your house is too small or the roof is the "
    f"wrong pitch, that section is the one to read."))

# ---------------------------------------------------------------- the trades
flow += k.h2_tight("THE THREE TRADE EXEMPTIONS ARE THREE DIFFERENT TESTS",
                   reserve=2.0)
flow.append(k.body(
    "This is the part of Arkansas law that catches careful people out. All "
    "three trades have a homeowner exemption. <b>All three are worded "
    "differently, and the differences decide whether the exemption reaches a "
    "house that is still under construction.</b> Read the verbs."))
rows = [
    [k.cellp("<b>Electrical</b><br/>" + sec("17-28-102(b)")),
     k.cellp("\"Nothing in this chapter shall be construed to require an "
             "individual to hold a license before doing electrical work on "
             "<b>his or her primary residence</b> except as otherwise required "
             "by state law, rules, regulations, or <b>local ordinances</b>.\""),
     k.cellp("\"Primary residence\" is defined as \"an <b>unattached "
             "single-family dwelling used as</b> the person's primary place of "
             f"residence\" ({sec('17-28-101(9)')}). Present tense. Its "
             f"application to a house not yet occupied is not addressed")],
    [k.cellp("<b>Plumbing</b><br/>" + sec("17-38-302(1)")),
     k.cellp("\"The licensing provisions of this chapter shall not apply to: "
             "(1) Plumbing work done by a property owner in a building "
             "<b>owned and occupied</b> by him or her as his or her home "
             "<b>except when the license is required by local ordinance</b>\""),
     k.cellp("\"Owned <b>and</b> occupied\", with no rule extending it to a "
             "residence merely built <i>for</i> future occupancy. On a literal "
             "reading a house under construction is not yet occupied")],
    [k.cellp("<b>HVACR</b><br/>" + sec("17-33-102(b)(1)")),
     k.cellp("\"This chapter shall not apply to a person who: (1) Performs "
             "HVACR work in an <b>existing building or structure</b> owned and "
             "occupied by him or her as his or her home\""),
     k.cellp("<b>The narrowest of the three.</b> \"Existing building or "
             "structure\" does not, on its face, reach new construction at "
             "all")],
]
flow.append(k.ref_table(
    "Same idea, three different tests",
    [k.cellp("Trade", bold=True), k.cellp("The exemption", bold=True),
     k.cellp("What the wording does to it", bold=True)],
    # 1.35in, not 1.15: "§ 17-33-102(b)(1)" measures 83.8pt and a 1.15in column
    # leaves only 72.8pt inside the padding, which broke the citation between
    # "(b)" and "(1)" on its own line.
    rows, [1.35 * inch, (CW - 1.35 * inch) * 0.52,
           (CW - 1.35 * inch) * 0.48]))
flow.append(k.cite(
    "Electrical is licensed by the Board of Electrical Examiners and HVACR by "
    "the HVACR Licensing Board, both within the Arkansas Department of Labor "
    "and Licensing. <b>Plumbing is not</b> — plumbers and natural gas fitters "
    "are licensed by the Arkansas Department of Health through the Committee "
    "of Plumbing Examiners. Quotations read from each board's own published "
    "statute book, September 2026."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "What to do with that — the honest version", [
        Paragraph("We are not going to tell you these exemptions certainly do "
                  "or certainly do not cover your unoccupied new build. The "
                  "texts are genuinely unresolved on the point and no Arkansas "
                  "case or board rule settles it. What we can tell you is what "
                  "the words are, which is more than any other guide will give "
                  "you, and what the consequences of guessing wrong are.",
                  S["body"]),
        Paragraph("<b>Ask the board, in writing, before you start the work</b> "
                  "— and ask about your specific situation: a new dwelling, "
                  "not yet occupied, that you own and intend to live in. Write "
                  "the answer and the date on the line at the end of this "
                  "document.", S["body"]),
        Paragraph("<b>Three things are true whichever way the answer falls.</b> "
                  "Even when exempt from the <i>license</i>, an HVACR exempt "
                  "person \"is required to conform to rules on the performance "
                  "of HVACR work as well as obtaining local permits and "
                  f"inspections as may be required by local ordinance\" "
                  f"({sec('17-33-102(d)')}). The electrical exemption is "
                  f"expressly subordinate to local ordinances, and a city or "
                  f"county \"may by ordinance require a person, before doing "
                  f"electrical work on his or her primary residence, to "
                  f"demonstrate a technical competency\" "
                  f"({sec('17-28-305(b)(2)')}). And the plumbing exemption "
                  f"carries its own \"except when the license is required by "
                  f"local ordinance\" in the same sentence.", S["body"]),
    ]))

flow.append(Spacer(1, 4))
flow.append(k.body(
    "<b>The septic system and the well go the other way.</b> Both are governed "
    "by statutes that say plainly you may do your own — which, after three "
    "trade exemptions written in riddles, is a relief."))
rows = [
    [k.cellp("<b>Septic</b>"),
     k.cellp("The statute directs registration of installers \"<b>with the "
             "individual homeowner retaining all rights to install and repair "
             "his system</b> in accordance with the provisions of this "
             "chapter.\" \"Installer\" is defined as one who works \"for "
             "compensation… <b>for others</b>\""),
     k.cellp(f"{sec('14-236-102(b)(2)')}<br/>{sec('14-236-103(6)')}")],
    [k.cellp("<b>Well</b>"),
     k.cellp("\"Nothing in this chapter… shall prevent a person who has not "
             "obtained a license… from constructing, altering, or repairing a "
             "water well or installing or repairing a pump or pumping "
             "equipment <b>for use by him or her on his or her own land</b>\""),
     k.cellp(sec("17-50-108(b)"))],
]
flow.append(k.ref_table(
    "Two places Arkansas says yes without hedging",
    [k.cellp("", bold=True), k.cellp("What the statute says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [0.75 * inch, CW - 2.15 * inch, 1.4 * inch]))
flow.append(k.body(
    "<b>Both come with a limit that matters more than the permission.</b> You "
    "may install your own septic system, but you may <b>not design it</b> — "
    "Part I of the permit application \"shall be completed by a Designated "
    "Representative\" (Rules Pertaining to Onsite Wastewater Systems, § 4.10.1), "
    "and the permit itself is still required. You may drill your own well, but "
    "the exemption is from the <i>license</i> only: \"No person shall "
    "construct, repair, or abandon… any water well without complying with the "
    f"provisions of this chapter and the rules\" ({sec('17-50-107(a)')}). "
    "Casing, grouting, sealing, disinfection and separation distances all still "
    "bind you. AR.2 carries the numbers."))
flow.append(k.closing_note(
    "Onsite wastewater rule text is from the Arkansas State Board of Health's "
    "<i>Rules Pertaining to Onsite Wastewater Systems</i>, effective 5 "
    "September 2024 — note the current title drops the older \"and "
    "Regulations\". Well rules are 17 CAR Part 11, Arkansas Water Well "
    "Construction Rules. <b>The Commission on Water Well Construction no "
    "longer exists:</b> Act 691 of 2023 abolished it and transferred "
    "everything to the Arkansas Natural Resources Commission in the Department "
    "of Agriculture. Guides still naming the old commission are working from "
    "stale sources."))

# ---------------------------------------------------------------- hiring subs
flow += k.h2_tight("HIRING SUBCONTRACTORS — THE EXEMPTION IS YOURS, NOT THEIRS",
                   reserve=2.0)
flow.append(k.body(
    "Your exemption covers <i>you</i> managing the job. It does not travel to "
    "the people you hire. Arkansas shelters a subcontractor in two ways, and "
    "an owner-builder fits neither of them cleanly:"))
flow.append(k.bullet(
    f"{sec('17-25-513(4)')} exempts \"a subcontractor <b>of a contractor "
    f"licensed by the Residential Contractors Committee</b>.\" You are exempt, "
    f"not licensed — so on the face of the text this paragraph does not reach "
    f"a sub you hire directly."))
flow.append(k.bullet(
    f"{sec('17-25-513(5)')} exempts anyone \"licensed as a contractor by "
    f"another licensing agency, board, or commission of the State of Arkansas "
    f"if the contractor is performing work within the scope of the license "
    f"held.\" <b>This is the one that matters.</b> It is how your electrician, "
    f"plumber and HVACR contractor qualify — because each holds a state "
    f"license from their own board."))
flow.append(k.body(
    f"The practical rule that falls out of this is simple, and it is the same "
    f"rule whether or not the fine print is ever resolved: <b>hire licensed "
    f"trades and verify each license yourself before work starts.</b> A "
    f"residential trade sub working directly for you on more than $2,000 needs "
    f"to be licensed by somebody — and the person who finds out otherwise, "
    f"late, is you. Unlicensed contracting is a Class A misdemeanor with "
    f"\"each day in violation… to constitute a separate offense\" "
    f"({sec('17-25-505(c)')})."))
flow.append(k.callout(
    "Before you hire anyone, and before you pay anyone", [
        Paragraph("<b>Verify the license.</b> The Contractors Licensing Board "
                  "publishes a Find A Licensed Contractor lookup, and the "
                  "Department of Labor and Licensing publishes rosters for "
                  "electricians and HVACR. Plumbers are looked up separately "
                  "through the Department of Health. AR.4 lists all of them.",
                  S["body"]),
        Paragraph("<b>Get the Notice to Owner, and keep it.</b> On residential "
                  "property of four or fewer&#160;units, no lien may be acquired "
                  "unless the owner received the notice set out in Ark. Code "
                  f"Ann. {sec('18-44-115')} — and \"no lien may be claimed by "
                  f"any subcontractor, laborer, material supplier, or other "
                  f"lien claimant unless the owner… has received at least one "
                  f"(1) copy of the notice.\" It is the residential "
                  f"contractor's duty to give it \"before the commencement of "
                  f"work.\" That notice protects <i>you</i>: without it, the "
                  f"lien fails.", S["body"]),
    ]))

# ---------------------------------------------------------------- scope
flow += k.h2_tight("TWO DEFINITIONS THAT CATCH PEOPLE", reserve=1.8)
rows = [
    [k.cellp(f"<b>\"Single family residence\"<br/>{sec('17-25-502(3)')}</b>"),
     k.cellp("\"any project consisting of at least one (1) but <b>no more than "
             "four (4)&#160;units</b> of new construction for residential "
             "occupancy.\" A duplex, triplex or fourplex is still "
             "<i>residential</i> in Arkansas — it does not become a commercial "
             "job")],
    [k.cellp(f"<b>The $50,000 figure<br/>{sec('17-25-101')}</b>"),
     k.cellp("It is the <b>commercial</b> threshold, and that chapter's own "
             "definition excludes houses: \"except single-family residences… "
             "It is the intention of this definition to include all "
             "improvements, demolition, or structures, <b>excepting only "
             "single-family residences</b>.\" If a guide applies $50,000 to "
             "your house, it has the wrong subchapter")],
]
flow.append(k.ref_table(
    "Read these before you assume which rules you are under",
    [k.cellp("Term", bold=True), k.cellp("What it actually means", bold=True)],
    rows, [1.85 * inch, CW - 1.85 * inch]))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS WITH A PEN",
                   reserve=1.6)
flow += k.check_table(
    "Confirm each of these before you break ground",
    [
        "I own the parcel outright, or hold the sole and exclusive right to "
        "sell or convey it (17 CAR § 295-101(1)).",
        "This house is being constructed for my own occupancy — the test in "
        "17 CAR § 295-101(6).",
        "I have not started, and will not start, a second residence in this "
        "same calendar year (§ 17-25-513(1)).",
        ("I asked my CITY whether it requires a building permit, and who "
         "issues it. Answer:", [("Office", 0.5), ("Answer", 0.5)]),
        ("I asked my COUNTY the same question. Answer:",
         [("Office", 0.5), ("Answer", 0.5)]),
        ("I confirmed whether the parcel sits inside a city's planning area "
         "or extraterritorial jurisdiction — a county mailing address does "
         "not settle this. Answer:", [("Confirmed with", 1.0)]),
        ("I asked the Board of Electrical Examiners, in writing, whether the "
         "§ 17-28-102(b) homeowner exemption reaches my unoccupied new "
         "dwelling. Answer:", [("Date", 0.4), ("Answer", 0.6)]),
        ("I asked the Department of Health the same about the § 17-38-302(1) "
         "plumbing exemption. Answer:", [("Date", 0.4), ("Answer", 0.6)]),
        ("I asked the HVACR Licensing Board the same about § 17-33-102(b)(1), "
         "which on its face covers only existing buildings. Answer:",
         [("Date", 0.4), ("Answer", 0.6)]),
        ("I checked whether my city requires a technical competency "
         "demonstration before I do my own electrical work "
         "(§ 17-28-305(b)(2)). Answer:", [("Answer", 1.0)]),
        "I have a Designated Representative engaged for the septic design — "
        "I cannot design it myself (Onsite Wastewater Rules § 4.10.1).",
        "Every subcontractor I intend to hire holds a current license from "
        "their own Arkansas board, and I have verified each one myself.",
        ("I received the § 18-44-115 Notice to Owner before work started, and "
         "filed it with this kit. Date:", [("Date received", 1.0)]),
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ar-permit-kit",
                       "AR.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
