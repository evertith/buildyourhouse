#!/usr/bin/env python3
"""LA.1 Owner-Builder Exemption Walkthrough.

The document the whole kit turns on. Louisiana's owner-builder position is
governed by THREE separate chapters of law that nobody assembles in one place:

  - contractor licensing, R.S. 37:2150 et seq. (LSLBC) — the exemption and the
    affidavit;
  - plumbing and gas fitting, R.S. 37:1361 et seq. (State Plumbing Board) — a
    different chapter that R.S. 37:2157 does not reach, where the homeowner
    allowance is a DEFINITIONAL exclusion rather than an exemption;
  - individual sewage, LAC 51:XIII (state health officer) — self-install
    allowed except for a mechanical plant.

Two widely-printed Louisiana facts are wrong and are corrected on page 2: the
exemption statute everyone cites (R.S. 37:2170) was repealed by Acts 2022,
No. 195, and the licensing threshold is $50,000, not $75,000.
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

FORM_ID = "LA.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "The Exemption"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "What Louisiana actually lets you do on your own house — "
                 "under three different chapters of law, only one of which "
                 "most guides have read.")
flow.append(k.disclaimer())

# ------------------------------------------------------------------ short
flow += k.h2("THE SHORT VERSION")
flow.append(k.body(
    "Louisiana is one of the few states that <b>names the owner-builder in "
    "its statute</b> instead of leaving you to argue you fall outside a "
    "definition. The exemption is real, it is written down, and — this is the "
    "part that matters most — it is written in <i>management</i> verbs. You "
    "may <b>hire and direct subcontractors</b> on your own house. You are not "
    "limited to work you perform with your own hands."))
flow.append(k.body(
    "It comes with one condition and one piece of paper. The condition is a "
    "frequency cap: <b>one residence per year</b>, and the year runs from the "
    "date your certificate of occupancy issues. The paper is an <b>affidavit "
    "of exemption</b> on a form the state licensing board provides, which you "
    "hand to your local permit office <i>before</i> the permit issues."))
flow.append(k.body(
    "What that exemption does <b>not</b> do is release you from anything "
    "else. The building code still binds your house, the permit is still "
    "required, and two trades are governed by a different chapter of law "
    "entirely — one the contractor exemption does not touch. This document "
    "walks all three."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Two things almost every Louisiana guide still prints, and both are wrong",
    [
        Paragraph(
            "<b>1. The statute number.</b> Nearly every article, forum post "
            "and older guide cites <b>La. R.S. 37:2170</b> as the "
            "owner-builder exemption. That section, and R.S.&nbsp;37:2171 "
            "with it, was <b>repealed by Acts 2022, No.&nbsp;195</b>. Quoting "
            "a repealed section to a permit clerk is the fastest way to lose "
            "an argument you should win. The exemption now lives at "
            "<b>R.S.&nbsp;37:2157(A)(13)</b>.", S["body"]),
        Paragraph(
            "<b>2. The dollar threshold.</b> The figure in wide circulation "
            "is <b>$75,000</b>. The current statute says <b>fifty thousand "
            "dollars</b> — R.S.&nbsp;37:2150.1(19)(a) and (4)(a)(ii). "
            "Louisiana rewrote this chapter three times in four years (Acts "
            "2022, No.&nbsp;195; Acts 2024, No.&nbsp;178; Acts 2025, "
            "No.&nbsp;422), which is why so much of what is published about "
            "it describes law that is no longer in force.", S["body"]),
        Paragraph(
            "Neither correction changes what you may do. Both change whether "
            "you can prove it.", S["body"]),
    ]))
flow.append(k.cite(
    "Sources: La. R.S. 37:2157(A)(13); repeal of R.S. 37:2170 and 37:2171 by "
    "Acts 2022, No. 195, §2; La. R.S. 37:2150.1(4)(a)(ii) and (19)(a). Read "
    "at legis.la.gov, September 2026."))

# ------------------------------------------------------------------ verbatim
flow += k.h2("THE EXEMPTION, WORD FOR WORD")
flow.append(k.body(
    "This is the entire provision. It is worth carrying to the permit counter "
    "on paper, because the sentence that gets you the permit is the last "
    "one."))
flow.append(k.callout_long(
    "La. R.S. 37:2157(A)(13) — Exemptions",
    [
        Paragraph(
            "&ldquo;A. The provisions of this Part shall not apply to any of "
            "the following: … <b>(13) Owners of property who supervise, "
            "superintend, oversee, direct, or in any manner assume charge of "
            "the construction, alteration, repair, improvement, movement, "
            "demolition, putting up, tearing down, or maintenance of their "
            "personal residences, if the homeowner does not build more than "
            "one residence per year. The one-year period shall commence on "
            "the date of issuance of the certificate of occupancy. However, "
            "an owner of property may build more than one single-family "
            "dwelling in a one-year period if the construction of an "
            "additional residence occurs as a result of a change in the legal "
            "marital status of the owner or change in the employment status "
            "of the owner whereby the owner must relocate to another "
            "employment location, which is located in excess of fifty miles "
            "from his personal residence. An affidavit of exemption shall be "
            "provided to obtain the building permit on a form provided by the "
            "board.</b>&rdquo;", S["body"]),
    ]))
flow.append(k.cite(
    "La. R.S. 37:2157(A)(13), quoted in full. &ldquo;The board&rdquo; is the "
    "State Licensing Board for Contractors — R.S. 37:2150.1(1)."))

flow.append(Spacer(1, 6))
rows = [
    [k.cellp("Act as your own general contractor and hire licensed subs"),
     k.cellp("<b>Yes</b>"),
     k.cellp("The verbs are &ldquo;supervise, superintend, oversee, direct, "
             "or in any manner assume charge&rdquo; — management, not manual "
             "labor. Where the Legislature wanted hands-on work it said so, "
             "in the same section: (A)(15)(a) exempts an owner who "
             "&ldquo;physically performs&rdquo; home improvement work. Those "
             "words are absent from (13).")],
    [k.cellp("Do the work yourself"),
     k.cellp("<b>Yes</b>"),
     k.cellp("Nothing in (13) requires you to hire anyone. Trades governed by "
             "other chapters are covered further down this document.")],
    [k.cellp("Build a house to sell or rent"),
     k.cellp("<b>No</b>"),
     k.cellp("The exemption is for &ldquo;their personal residences.&rdquo; "
             "That phrase is the qualifying condition — see the note on "
             "selling, below.")],
    [k.cellp("Build more than one home in a year"),
     k.cellp("<b>No</b>, with two exceptions"),
     k.cellp("A change in your legal marital status, or a change in "
             "employment that forces you to relocate more than "
             "<b>fifty&nbsp;miles</b> from your personal residence.")],
    [k.cellp("Skip the building permit"),
     k.cellp("<b>No</b>"),
     k.cellp("The affidavit exists <i>to obtain</i> the permit. It is a "
             "precondition, not a substitute.")],
    [k.cellp("Skip the code, or the inspections"),
     k.cellp("<b>No</b>"),
     k.cellp("R.S. 37:2157(B): the exemptions section &ldquo;shall not be "
             "construed to waive local and state health and life safety code "
             "requirements.&rdquo;")],
]
flow.append(k.ref_table(
    "What R.S. 37:2157(A)(13) does and does not let you do",
    [k.cellp("", bold=True), k.cellp("", bold=True),
     k.cellp("Why", bold=True)],
    rows, [2.05 * inch, 1.05 * inch, CW - 3.10 * inch]))

# ------------------------------------------------------------------ clock
flow += k.h2_tight("THE ONE-HOME-A-YEAR CLOCK", reserve=2.0)
flow.append(k.body(
    "Read the clock carefully, because it does not start where people assume. "
    "The statute says the one-year period <b>&ldquo;shall commence on the "
    "date of issuance of the certificate of occupancy.&rdquo;</b> Not the "
    "permit date, not the day you broke ground, not the day you moved in. If "
    "you are contemplating a second build, that single sentence is the one "
    "that decides whether you are still exempt."))
rows = [
    [k.cellp("What starts the year"),
     k.cellp("The <b>date the certificate of occupancy issues</b> on the "
             "first residence.")],
    [k.cellp("What does not start it"),
     k.cellp("Permit issuance, start of construction, or occupancy in fact. "
             "The statute names one event.")],
    [k.cellp("Exception 1"),
     k.cellp("A change in the owner's <b>legal marital status</b>.")],
    [k.cellp("Exception 2"),
     k.cellp("A change in the owner's <b>employment status</b> requiring "
             "relocation to a work location more than "
             "<b>fifty&nbsp;miles</b> from the personal residence.")],
    [k.cellp("What the exceptions permit"),
     k.cellp("Building <b>more than one single-family dwelling</b> inside the "
             "one-year window. Keep the documentation that proves the "
             "triggering change.")],
]
flow.append(k.ref_table(
    "The frequency cap in R.S. 37:2157(A)(13)",
    [k.cellp("", bold=True), k.cellp("", bold=True)],
    rows, [2.05 * inch, CW - 2.05 * inch]))

# ------------------------------------------------------------------ affidavit
flow += k.h2_tight("THE AFFIDAVIT OF EXEMPTION", reserve=2.0)
flow.append(k.body(
    "Two separate statutes require this document, and between them they "
    "answer every practical question about it. The first is the last sentence "
    "of the exemption itself. The second puts the duty on the permit office, "
    "which is why the clerk will ask for it whether or not you bring it up."))
flow.append(k.callout_long(
    "La. R.S. 37:2160(C) — the duty on the permit office",
    [
        Paragraph(
            "&ldquo;<b>The local building permit official shall require any "
            "applicant claiming an exemption for residential construction "
            "activities to execute an affidavit attesting to the claimed "
            "exemption. Such affidavit shall be executed on a form provided "
            "by the board and submitted to the local building permit official "
            "prior to the issuance of a permit.</b>&rdquo;", S["body"]),
    ]))
rows = [
    [k.cellp("What it is actually called"),
     k.cellp("<b>Affidavit Claiming Exemption from Licensure</b> — that is "
             "the title printed on the LSLBC form. The statute calls it an "
             "&ldquo;affidavit of exemption,&rdquo; so both names are in "
             "circulation for one document.")],
    [k.cellp("Where to get it"),
     k.cellp("The forms page at <b>lslbc.gov</b>. The version current when "
             "this kit was verified is stamped <b>Revised 8/1/2025</b>; check "
             "for a newer revision before you sign.")],
    [k.cellp("Do not confuse it with"),
     k.cellp("The <b>Church Owner/Builder Affidavit</b>, which sits on the "
             "same forms page and implements a different exemption "
             "(R.S. 37:2157(A)(3)). Confusingly, the words &ldquo;Owner/"
             "Builder&rdquo; appear in the <i>church</i> form's title and not "
             "in the homeowner one.")],
    [k.cellp("Who receives the signed affidavit"),
     k.cellp("Your <b>local building permit official</b> — the parish or "
             "municipal permit office. <b>Not</b> the LSLBC. This is the "
             "detail most often reported backwards.")],
    [k.cellp("When"),
     k.cellp("<b>Prior to the issuance of a permit.</b> It is a condition of "
             "getting the permit, not a filing you catch up on.")],
    [k.cellp("Notarized?"),
     k.cellp("<b>Yes.</b> The form closes with &ldquo;Sworn to and subscribed "
             "before me&rdquo; and carries signature blocks for the homeowner "
             "and the notary. Do not sign it before you are in front of "
             "one.")],
    [k.cellp("How it is structured"),
     k.cellp("A header block and <b>eleven separate statements, each "
             "requiring your initials</b>. They are not boilerplate — read "
             "the four summarized below before you initial anything.")],
    [k.cellp("Is a parish's own form acceptable?"),
     k.cellp("The LSLBC form states that it is &ldquo;the only document "
             "authorized by the Louisiana State Licensing Board for "
             "Contractors pursuant to La. R.S. 37:2160(C) to claim exemption "
             "from licensure.&rdquo; Bring the state form even if your office "
             "hands you something else.")],
]
flow.append(k.ref_table(
    "The affidavit, in practical terms",
    [k.cellp("", bold=True), k.cellp("", bold=True)],
    rows, [2.05 * inch, CW - 2.05 * inch]))
flow.append(k.cite(
    "Sources: La. R.S. 37:2157(A)(13), final sentence; La. R.S. 37:2160(C); "
    "the LSLBC <i>Affidavit Claiming Exemption from Licensure</i> (revision "
    "of 1 August 2025), read in full at lslbc.gov, September 2026."))

flow += k.h2_tight("Four of the eleven statements you will be initialing",
                   reserve=2.0)
flow.append(k.body(
    "The affidavit is where Louisiana quietly loads several obligations onto "
    "you that appear nowhere in the exemption statute. These four change how "
    "you should run the job."))
rows = [
    [k.cellp("<b>Primary residence after the CO</b>"),
     k.cellp("You attest you are claiming the exemption to act as general "
             "contractor and that you will maintain the house as your "
             "<b>primary residence</b> after the certificate of occupancy. "
             "That is the resale question answered on the form itself, even "
             "though the statute is silent.")],
    [k.cellp("<b>Written contracts with every sub</b>"),
     k.cellp("You acknowledge R.S. 37:2159(A) and (B): written contracts with "
             "each licensed subcontractor, and <b>no work begins before all "
             "parties have signed</b>. Budget time for this; it is not "
             "advice, it is an attestation.")],
    [k.cellp("<b>The exemption does not cover your subs</b>"),
     k.cellp("You attest that your exemption does not extend to "
             "subcontractors who require licensure. See the section below — "
             "this catches people.")],
    [k.cellp("<b>Direct, onsite supervision — by you</b>"),
     k.cellp("You accept sole legal and financial responsibility, agree to "
             "give <b>direct onsite supervision</b>, and agree not to hire an "
             "unlicensed person as your contractor, construction manager or "
             "supervisor. An absentee owner-builder is not what this "
             "exemption contemplates.")],
]
flow.append(k.ref_table(
    "From the LSLBC affidavit's initialed statements",
    [k.cellp("", bold=True), k.cellp("What you are agreeing to", bold=True)],
    rows, [2.05 * inch, CW - 2.05 * inch]))
flow.append(k.callout(
    "Sign it carefully — the form says so itself", [
        Paragraph(
            "The affidavit's eleventh statement has you acknowledge "
            "<b>La. R.S.&nbsp;14:133</b>: submitting false information to a "
            "public agency is a <b>felony</b>, punishable by up to five&nbsp;years "
            "in prison and a fine of up to $5,000. It also records your right "
            "to consult an attorney before signing. Neither of those is on "
            "the form by accident.", S["body"]),
    ]))

flow += k.h2_tight("WHY YOUR PERMIT CLERK CARES SO MUCH ABOUT THIS FORM",
                   reserve=2.0)
flow.append(k.body(
    "Owner-builders often read the permit counter's insistence on the "
    "affidavit as bureaucratic caution. It is not. The statute puts the "
    "prohibition on the <i>clerk</i>, not on you."))
flow.append(k.callout_long(
    "La. R.S. 37:2160(B) — the rule the permit office is following",
    [
        Paragraph(
            "&ldquo;<b>A local building department shall not issue a building "
            "permit to any person who does not hold an active license in the "
            "appropriate classification for the scope of work for which the "
            "permit is issued.</b> Nothing in this Section shall prohibit a "
            "local building department from issuing a permit for work that "
            "does not require a license pursuant to this Chapter.&rdquo;",
            S["body"]),
        Paragraph(
            "The first sentence forbids the office from putting your name on "
            "a permit. The second sentence is the door: a permit may issue "
            "for work that does not require a license — and an owner exempt "
            "under (A)(13) is doing exactly that. <b>The affidavit is how you "
            "prove you are through that door.</b> It is not paperwork you can "
            "backfill; without it the clerk is barred from issuing.",
            S["body"]),
    ]))
flow.append(k.body(
    "There is a second reason the offices are careful. Under "
    "R.S.&nbsp;37:2160(A) the board's staff may inspect each local permit "
    "official's list of issued permits <b>every month</b> to check that "
    "nobody is working as a contractor without a license, and permitting "
    "authorities must hand over unredacted permit documents on request. Your "
    "affidavit is what makes your name on that list defensible."))

flow += k.h2_tight("YOUR SUBCONTRACTORS DO NOT RIDE ON YOUR EXEMPTION",
                   reserve=2.0)
flow.append(k.body(
    "This is the single most expensive misreading available in Louisiana, and "
    "it comes from a paragraph that looks helpful until you read who it "
    "applies to."))
flow.append(k.callout_long(
    "La. R.S. 37:2157(A)(17) — read who it covers",
    [
        Paragraph(
            "&ldquo;(17) Any person performing work as a subcontractor "
            "<b>for a residential construction license holder</b>, except for "
            "electrical, mechanical, plumbing, mold remediation, asbestos, or "
            "hazardous materials scopes of work.&rdquo;", S["body"]),
        Paragraph(
            "It exempts subs only when they are working <i>for a license "
            "holder</i>. An exempt owner-builder is not a license holder — "
            "you are exempt <i>from</i> licensure, which is the opposite "
            "thing. And electrical, mechanical and plumbing are carved out of "
            "the paragraph in any event. The board's own affidavit says the "
            "same in plainer words: your exemption does not apply to any "
            "subcontractor who is subject to licensure.", S["body"]),
        Paragraph(
            "<b>Plan on every sub meeting its own threshold and holding its "
            "own license.</b> Verify each one in the board's searchable "
            "database before the work starts, and keep a printout with the "
            "signed contract.", S["body"]),
    ]))
flow.append(k.cite(
    "The reading above follows the plain text of R.S. 37:2157(A)(17) and is "
    "corroborated by the board's own affidavit. No Louisiana case or board "
    "rule construing the paragraph against an exempt owner was found, so "
    "treat it as the safe reading rather than a settled holding — which is "
    "how you should be treating it anyway."))

# ------------------------------------------------------------------ resale
flow += k.h2_tight("SELLING LATER: WHAT THE STATUTE DOES AND DOES NOT SAY",
                   reserve=2.0)
flow.append(k.body(
    "This is worth getting exactly right, because Louisiana law contains both "
    "answers and they sit in the same section."))
flow.append(k.body(
    "<b>R.S.&nbsp;37:2157(A)(13) contains no holding period and no anti-resale "
    "clause.</b> It does not say you may not sell within any number of years. "
    "Its qualifying words are &ldquo;their personal residences&rdquo; and its "
    "only limit is the one-per-year cap. That is an unusual and genuinely "
    "favorable position compared with most states."))
flow.append(k.body(
    "But the phrase that people remember — &ldquo;will not be for sale or "
    "rent&rdquo; — <i>does</i> exist in Louisiana law. It is in a different "
    "paragraph, <b>R.S.&nbsp;37:2157(A)(2)</b>, the general owner exemption, "
    "which also requires that access to the property be controlled &ldquo;so "
    "that only employees and nonpublic invitees are allowed access.&rdquo; "
    "That condition is unworkable on an ordinary house lot, which is exactly "
    "why (A)(13) exists separately. Do not let the two be conflated — by a "
    "guide, or by a counter clerk reading the wrong paragraph."))
flow.append(k.body(
    "The honest practical position: build it as your residence and be able to "
    "show that is what you did. A house sold immediately on completion "
    "invites the argument that you were building &ldquo;for sale … by "
    "another,&rdquo; which is the opening words of the <i>residential "
    "contractor</i> definition at R.S.&nbsp;37:2150.1(19)(a). Keep your "
    "homestead exemption filing, your utility accounts and your change of "
    "address."))

# ------------------------------------------------------------------ threshold
flow += k.h2_tight("THE $50,000 THRESHOLD, AND WHAT COUNTS TOWARD IT",
                   reserve=2.0)
flow.append(k.body(
    "You do not need this number if the exemption applies to you — the "
    "exemption is not threshold-dependent. You need it for two other reasons: "
    "to know when a person you are <i>hiring</i> must hold a license, and "
    "because Louisiana defines project value in a way that surprises "
    "owner-builders."))
flow.append(k.callout_long(
    "La. R.S. 37:2150.1(3) — how project value is measured",
    [
        Paragraph(
            "&ldquo;&lsquo;Contract&rsquo; means an agreement to perform a "
            "scope of work that is regulated by this Chapter. <b>The project "
            "value includes the entire cost of the labor, materials, rentals, "
            "and all direct and indirect project expenses. The cost of "
            "materials, rentals, and direct and indirect expenses shall be "
            "included regardless of who pays the costs or if they are "
            "donated.</b>&rdquo;", S["body"]),
        Paragraph(
            "Read the last sentence twice. <b>Owner-supplied materials "
            "count. Donated materials count.</b> You cannot bring a job under "
            "a threshold by buying the materials yourself and hiring out only "
            "the labor — the statute closes that door expressly. What the "
            "statute does <i>not</i> do is assign a dollar value to your own "
            "unpaid hours, and this kit prints no figure for that because "
            "none exists in the law.", S["body"]),
    ]))
rows = [
    [k.cellp("New residential structure"), k.cellp("<b>$50,000</b>"),
     k.cellp("R.S. 37:2150.1(4)(a)(ii), (19)(a)")],
    [k.cellp("Improvements or repairs to an existing residence"),
     k.cellp("<b>$7,500</b>"), k.cellp("R.S. 37:2150.1(4)(a)(iii)")],
    [k.cellp("Home improvement"), k.cellp("<b>$7,500</b>"),
     k.cellp("R.S. 37:2150.1(10), (11), (19)(b)(i)")],
    [k.cellp("Electrical contractor"), k.cellp("<b>$10,000</b>"),
     k.cellp("R.S. 37:2150.1(6)")],
    [k.cellp("Mechanical contractor (HVAC)"), k.cellp("<b>$10,000</b>"),
     k.cellp("R.S. 37:2150.1(13)")],
    [k.cellp("Plumbing contractor"), k.cellp("<b>$10,000</b>"),
     k.cellp("R.S. 37:2150.1(16)")],
]
flow.append(k.ref_table(
    "LSLBC project-value thresholds that matter on a house",
    [k.cellp("Scope", bold=True), k.cellp("Threshold", bold=True),
     k.cellp("Citation", bold=True)],
    rows, [CW - 3.05 * inch, 1.05 * inch, 2.0 * inch]))
flow.append(k.cite(
    "The <b>$7,500</b> home-improvement tier is a renovation rule, not a "
    "new-construction rule: &ldquo;home improvement&rdquo; is defined at "
    "R.S. 37:2150.1(10) as work on a <i>preexisting</i> residential "
    "structure, and R.S. 37:2150.1(11) bars a home improvement contractor "
    "from footings, foundations, outside walls, skeleton, bearing columns, "
    "load-bearing interior walls, floor slabs and roofing. It is the number "
    "that matters after your house exists."))

# ------------------------------------------------------------------ trades
flow += k.h2("THE THREE CHAPTERS — TRADE BY TRADE")
flow.append(k.body(
    "Here is the structural point no Louisiana guide makes, and it is the "
    "reason so much published advice about doing your own trade work in this "
    "state is muddled. Your position is set by <b>three different bodies of "
    "law</b>, and the contractor exemption you just read reaches only the "
    "first of them."))
rows = [
    [k.cellp("<b>1.</b> Contractor licensing"),
     k.cellp("R.S. 37:2150 et seq.<br/>State Licensing Board for "
             "Contractors"),
     k.cellp("General building, electrical, mechanical and plumbing "
             "<i>contractor</i> licenses. <b>R.S. 37:2157(A)(13) exempts you "
             "from this Part</b> on your personal residence.")],
    [k.cellp("<b>2.</b> Plumbing and gas fitting"),
     k.cellp("R.S. 37:1361 et seq.<br/>State Plumbing Board of Louisiana"),
     k.cellp("Licenses the <i>individual</i> — residential plumber limited, "
             "journeyman, master, gas fitter. <b>R.S. 37:2157 does not reach "
             "this chapter at all.</b> Your allowance here comes from a "
             "different mechanism entirely — see below.")],
    [k.cellp("<b>3.</b> Individual sewage systems"),
     k.cellp("LAC 51:XIII<br/>State health officer (LDH)"),
     k.cellp("Installer licensing for septic systems, with an express "
             "homeowner carve-out that has one important limit.")],
]
flow.append(k.ref_table(
    "Three separate chapters govern one house",
    [k.cellp("", bold=True), k.cellp("Where it lives", bold=True),
     k.cellp("What it does to you", bold=True)],
    rows, [1.55 * inch, 1.85 * inch, CW - 3.40 * inch]))

flow += k.h2_tight("Electrical and HVAC", reserve=1.8)
flow.append(k.body(
    "Louisiana licenses electrical and mechanical <b>contractors</b> through "
    "the LSLBC, both at a <b>$10,000</b> project value "
    "(R.S.&nbsp;37:2150.1(6) and (13)). Both are inside the same Part that "
    "R.S.&nbsp;37:2157(A)(13) switches off for an owner building their "
    "personal residence."))
flow.append(k.body(
    "Note what the definition actually captures: an electrical contractor is "
    "a person who &ldquo;undertakes to, attempts to, or submits a price or "
    "bid or offers to&rdquo; do the work. It is a description of someone "
    "<i>selling</i> the work. A homeowner wiring their own house is not "
    "bidding it to anyone."))
flow.append(k.body(
    "Now the fact that makes Louisiana different from almost every state "
    "around it: <b>there is no Louisiana journeyman or master electrician "
    "license.</b> There is no state board of electrical examiners. The state "
    "licenses the electrical <i>contractor</i> — the business selling the "
    "work — and stops there. Credentialing the individual electrician is left "
    "to municipalities, and it is optional even for them."))
flow.append(k.callout_long(
    "La. R.S. 33:4782 — where individual electrician licensing actually lives",
    [
        Paragraph(
            "&ldquo;<b>All municipalities, except New Orleans, may enact "
            "ordinances for the purpose of regulating persons pursuing or "
            "engaged in the business of installing wires or apparatus to "
            "convey electric current for light, heat, or power.</b> … The "
            "municipalities may in their discretion vest the board with full "
            "power, control, and regulation of the business. <b>The power or "
            "final inspection of any of the work shall be vested solely in "
            "the city electrician.</b>&rdquo;", S["body"]),
        Paragraph(
            "Note the verbs — &ldquo;may enact,&rdquo; &ldquo;in their "
            "discretion.&rdquo; This is a grant of optional authority to "
            "towns, not a statewide scheme, and New Orleans is expressly "
            "carved out of it and runs its own. So the honest answer to "
            "&ldquo;do I need an electrician's license in Louisiana?&rdquo; "
            "is: <b>the state does not issue one, and whether your town does "
            "is a question only your town can answer.</b>", S["body"]),
    ]))
flow.append(k.body(
    "So ask your permit office two questions, in these words, and write both "
    "answers on the line in LA.4: <b>does this jurisdiction license or "
    "register individual electricians</b>, and <b>may a homeowner pull the "
    "electrical permit on their own residence here?</b> Louisiana's uniform "
    "code law preempts local <i>construction codes</i>; it does not abolish "
    "local licensing ordinances, so this genuinely varies."))

flow += k.h2_tight("Plumbing — a different chapter, and a different mechanism",
                   reserve=2.2)
flow.append(k.body(
    "You will read that Louisiana &ldquo;allows a homeowner to do their own "
    "plumbing.&rdquo; That is broadly true and almost always explained "
    "wrongly. There is <b>no homeowner exemption</b> in the plumbing "
    "licensing sections: R.S.&nbsp;37:1367(A) and (B) say flatly that no "
    "natural person shall do the work of a residential plumber limited, "
    "journeyman or master plumber without the board's license, and they name "
    "no owner."))
flow.append(k.body(
    "The allowance is in the <b>definitions</b> instead, and it is stronger "
    "for being there. Work on your own home is not exempted from "
    "&ldquo;plumbing&rdquo; — it is excluded from the meaning of the word, so "
    "the license requirement never attaches in the first place."))
flow.append(k.callout_long(
    "La. R.S. 37:1377(D) — what &ldquo;plumbing&rdquo; does not include",
    [
        Paragraph(
            "&ldquo;For purposes of this Chapter the definition of plumbing "
            "given above will not include: … <b>(8) Work done by an "
            "individual on his own personal residence.</b>&rdquo;", S["body"]),
        Paragraph(
            "Two neighbors in the same list are worth knowing. "
            "<b>(2) Drilling of water wells</b> is also outside "
            "&ldquo;plumbing&rdquo; — a well driller is regulated elsewhere, "
            "not by the plumbing board. And <b>(9)</b>, the owner exclusion "
            "for <i>maintenance</i> work on property generally, says such "
            "work &ldquo;shall specifically not include construction or "
            "installation.&rdquo; Paragraph (8) carries no such limit — which "
            "is the difference between your own residence and a rental you "
            "own.", S["body"]),
    ]))
flow.append(k.body(
    "Gas fitting has its own, separate homeowner allowance, and this one is "
    "written as a true exemption: R.S.&nbsp;37:1367(J)(2) — &ldquo;The "
    "provisions of this Subsection shall not apply to work performed by "
    "persons on their own residences.&rdquo; It attaches only to the gas "
    "fitter subsection."))
flow.append(k.callout(
    "The reach of the plumbing chapter is geographic — check whether it "
    "covers your site", [
        Paragraph(
            "R.S.&nbsp;37:1375 limits where the whole plumbing chapter "
            "applies: to &ldquo;all cities, towns, villages, communities and "
            "public sewerage and/or water districts in the State of "
            "Louisiana,&rdquo; and to &ldquo;all areas within "
            "<b>one&nbsp;mile</b> of the boundary of any city or sewer or "
            "water district … and all areas within one&nbsp;mile of the "
            "community, sewerage or water facilities of the areas referred to "
            "above.&rdquo; The section dates from 1964 and 1968 and the word "
            "&ldquo;communities&rdquo; is not defined in it. Do not conclude "
            "on your own that your parcel is outside the chapter's reach — "
            "ask the State Plumbing Board, and get the answer in writing "
            "before you rely on it.", S["body"]),
    ]))

flow += k.h2_tight("Septic — you may install your own, with one exception "
                   "that catches many Louisiana lots", reserve=2.2)
flow.append(k.body(
    "The rule is unusually clear, and the exception inside it is the part "
    "worth planning around."))
flow.append(k.callout_long(
    "LAC 51:XIII.705.A — installer licensing",
    [
        Paragraph(
            "&ldquo;A person who wishes to engage in the business of "
            "installing or providing maintenance of individual sewerage "
            "systems shall obtain … a license for such activity prior to "
            "making any such installations or providing maintenance. "
            "<b>Such a license shall not be required, however, for an "
            "individual wishing to install an individual sewerage system, "
            "other than an individual mechanical plant, for his own private, "
            "personal use. Individual mechanical plants shall be installed and "
            "maintenance provided by licensed individual sewerage system "
            "installers and/or maintenance providers only.</b>&rdquo;",
            S["body"]),
    ]))
flow.append(k.body(
    "So: a conventional septic tank and absorption field, an oxidation pond "
    "or a sand filter you may install yourself. An <b>individual mechanical "
    "plant</b> — the aerobic treatment unit Louisiana uses heavily wherever "
    "soils and water tables defeat a conventional field — must be installed "
    "and maintained by a licensed installer. On a great many Louisiana lots "
    "that is not a free choice, and the smaller lot sizes the Sanitary Code "
    "allows are themselves conditioned on using a mechanical plant. LA.2 "
    "covers the lot-size rule."))
flow.append(k.body(
    "The license exemption is <b>not</b> a permit exemption. LAC "
    "51:XIII.705.B makes the installer and the property owner both "
    "responsible for the permit and plan-approval sections, and the permit is "
    "issued by the state health officer in two stages. Expect an on-site "
    "inspection: the rule's final-approval path runs through either an "
    "inspection by the state health officer's representative <i>or</i> a "
    "&ldquo;Certification by Installer&rdquo; form signed by a licensed "
    "installer — and if you installed it yourself, you are not one."))

# ------------------------------------------------------------------ penalty
flow += k.h2_tight("IF YOU GET IT WRONG", reserve=2.0)
flow.append(k.body(
    "Contracting without a license is a criminal offense in Louisiana, and "
    "the fine is a daily one. This is not printed to alarm you — the "
    "exemption is straightforward to qualify for — but because the daily "
    "multiplier is the part people do not expect."))
flow.append(k.callout_long(
    "La. R.S. 37:2163(C) — penalties",
    [
        Paragraph(
            "&ldquo;<b>(1) Anyone found to be in violation of this Section "
            "shall be guilty of a misdemeanor and, upon conviction, shall be "
            "fined a sum not to exceed five hundred dollars per day of "
            "violation, or three months in prison, or both.</b> (2) "
            "Notwithstanding any action taken by the board, any person who "
            "does not possess a license from the board and violates any of "
            "the provisions of this Section, and causes harm or damage to "
            "another in excess of three hundred dollars, upon conviction, "
            "shall be fined not less than five hundred dollars nor more than "
            "five thousand dollars, or imprisoned, with or without hard "
            "labor, for not less than six&nbsp;months nor more than five&nbsp;years, or "
            "both.&rdquo;", S["body"]),
    ]))
flow.append(k.cite(
    "La. R.S. 37:2163(C). Prosecution is by the district attorney where the "
    "violation occurs — R.S. 37:2163(D)."))

# ------------------------------------------------------------------ checklist
flow += k.h2_tight("DO YOU QUALIFY? WORK THIS BEFORE YOU FILE", reserve=2.0)
flow.append(k.checklist([
    "I own the property, and the structure will be <b>my personal "
    "residence</b> — not a house built to sell or to rent.",
    "I have not obtained a certificate of occupancy on another residence "
    "I built within the last year — or one of the two statutory exceptions "
    "applies and I can document it.",
    "I have the LSLBC <b>Affidavit Claiming Exemption from Licensure</b> — "
    "not the church form — and I have checked lslbc.gov for a revision newer "
    "than the one I am holding.",
    "I have read all eleven initialed statements, and I have a notary lined "
    "up. I am not signing it in advance.",
    "I have a <b>written contract</b> ready for every licensed subcontractor, "
    "and I know no work may start until all parties sign (R.S. 37:2159).",
    "I know my exemption does <b>not</b> cover my subcontractors, and I have "
    "verified each one in the board's license database.",
    "I know whether my site is in the <b>unincorporated parish</b> or inside "
    "a municipality, because that decides who receives the affidavit.",
    "Any electrical or mechanical work I hire out over <b>$10,000</b> will go "
    "to an LSLBC-licensed contractor, and I have verified the license.",
    "Any plumbing I do not perform myself will be done by a State Plumbing "
    "Board licensee.",
    "I have asked my permit office, in plain words, whether a homeowner may "
    "pull the electrical permit here — and written the answer down.",
    "If I am on septic: I know whether my site needs a mechanical plant, "
    "because that decides whether I may install it myself.",
    "I understand the exemption releases me from the contractor license "
    "only — not from the permit, the code, or the inspections.",
]))

# ------------------------------------------------------------------ sources
flow.append(Spacer(1, 8))
flow.append(k.sources_table([
    ("The owner-builder exemption, and the affidavit requirement",
     "La. R.S. 37:2157(A)(13)"),
    ("The permit office must require the affidavit before issuing",
     "La. R.S. 37:2160(C)"),
    ("A permit office may not issue to an unlicensed person, except for work "
     "requiring no license", "La. R.S. 37:2160(B)"),
    ("The board may inspect local permit lists monthly",
     "La. R.S. 37:2160(A)"),
    ("Written contracts with subcontractors before work begins",
     "La. R.S. 37:2159(A), (B)"),
    ("The subcontractor exemption reaches only subs of a license holder",
     "La. R.S. 37:2157(A)(17)"),
    ("Form title, revision date, notarization, and the eleven statements",
     "LSLBC, Affidavit Claiming Exemption from Licensure, rev. 1 Aug 2025"),
    ("False information to a public agency is a felony",
     "La. R.S. 14:133, as recited on the affidavit"),
    ("No statewide electrician license; municipal option, New Orleans "
     "excepted", "La. R.S. 33:4782"),
    ("The exemption waives no health or life safety code requirement",
     "La. R.S. 37:2157(B)"),
    ("The &ldquo;not for sale or rent&rdquo; condition is in the general "
     "owner exemption, not the homeowner one",
     "La. R.S. 37:2157(A)(2)"),
    ("&ldquo;Physically performs&rdquo; appears in the home improvement "
     "exemption, not in (A)(13)", "La. R.S. 37:2157(A)(15)(a)"),
    ("R.S. 37:2170 and 37:2171 were repealed", "Acts 2022, No. 195, §2"),
    ("Residential contractor definition and the $50,000 threshold",
     "La. R.S. 37:2150.1(19)(a), (4)(a)(ii)"),
    ("Project value includes owner-supplied and donated materials",
     "La. R.S. 37:2150.1(3)"),
    ("Electrical, mechanical and plumbing contractor thresholds",
     "La. R.S. 37:2150.1(6), (13), (16)"),
    ("&ldquo;The board&rdquo; means the State Licensing Board for Contractors",
     "La. R.S. 37:2150.1(1)"),
    ("Penalty for unlicensed contracting, per day of violation",
     "La. R.S. 37:2163(C), (D)"),
    ("Plumbing licenses are required of the individual, with no owner "
     "carve-out in the licensing section", "La. R.S. 37:1367(A), (B)"),
    ("Work on your own personal residence is outside the definition of "
     "&ldquo;plumbing&rdquo;", "La. R.S. 37:1377(D)(8)"),
    ("Gas fitting on your own residence is expressly exempt",
     "La. R.S. 37:1367(J)(2)"),
    ("Geographic reach of the plumbing chapter", "La. R.S. 37:1375"),
    ("Homeowner may install their own sewerage system, except a mechanical "
     "plant", "LAC 51:XIII.705.A"),
    ("Owner remains responsible for the sewage permit and approved plans",
     "LAC 51:XIII.705.B"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "la-permit-kit",
                       "LA.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
