#!/usr/bin/env python3
"""MS.1 Owner-Builder Exemption Walkthrough.

Every Mississippi claim in this document was read out of the primary source in
August 2026 and is cited on-page. Statute text was read in the State Board of
Contractors' own published booklet, "Residential Builders Law 2022," which
reproduces Title 73, Chapter 59 verbatim (msboc.us -> Laws), cross-checked
against the enacted bills at billstatus.ls.state.ms.us.

Verified sources:
  § 73-59-1(b),(c)   "residential builder" = builds FOR SALE for another, or
                     for compensation for another over $50,000 and not more
                     than three floors; "remodeler" = improvements over
                     $10,000. Building your own is neither.
  § 73-59-1(h)       "construction manager" excludes the OWNER by name, and
                     reaches a CM even where the owner holds the permit
  § 73-59-3(1)(d)    subcontractors of ANY TIER doing electrical, plumbing,
                     mechanical and/or HVAC must be licensed "no matter the
                     dollar amount" — this is the trap. The $10,000 figure
                     printed by nearly every guide is the REMODELER threshold
                     in § 73-59-1(c), not a trade threshold.
  § 73-59-9(1),(2),(3) misdemeanor $100-$5,000 and/or 30-60 days; unlicensed
                     party may not sue to enforce the contract; board may
                     issue a citation and stop work
  § 73-59-15(1)(b)   the owner-builder exemption — own residence, own GC. No
                     cost cap, no sale condition inside (b) itself
  § 73-59-15(1)(c)   the relative exemption — consanguinity or direct affinity
  § 73-59-15(1)(d)   the owner-supervising exemption — carries its own
                     not-for-sale condition and is NOT subject to (2)
  § 73-59-15(1)(g)   TWO residences a year where no building permit is
                     required — the no-code-county exemption
  § 73-59-15(2)      the cap and the rebuttable presumption. Reads "within a
                     period of one (1) year" — a ROLLING twelve months, not a
                     calendar year. Applies to (1)(b) and (c) only.
  § 73-59-17         the building official SHALL refuse a permit absent
                     evidence of license OR exemption, and shall report
  § 73-59-18         Dept of Revenue permit under § 27-65-27 — expressly not
                     required of "a person building ... his or her own
                     residence"

Deliberately NOT claimed: that Mississippi caps the owner-builder exemption by
project cost (it does not — the $50,000 figure defines who is a residential
builder building for OTHERS); that the trade-license threshold is $10,000 (it
is zero); that the cap runs on a calendar year (the statute says a period of
one year); that a homeowner may never do their own electrical work (Chapter 59
does not reach the owner — but a local ordinance may, which is a local
question this document sends the reader to ask).
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

FORM_ID = "MS.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "Exemption & Qualification"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "How Mississippi's owner-builder exemption actually works — the four "
    "separate exemptions in one statute, the twelve-month limit that is not a "
    "calendar year, and the zero-dollar rule that applies to everyone you "
    "hire.")

flow.append(k.disclaimer(
    "Statute text was read in the State Board of Contractors' published "
    "Residential Builders Law booklet and against the enacted bills at "
    "billstatus.ls.state.ms.us in August 2026; statutes change."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION")
flow.append(k.body(
    "Mississippi requires a State Board of Contractors license to build "
    "houses for other people. Building your own is not that, and the "
    "Residential Builders Law says so in one plain sentence: the chapter "
    "\"<i>shall not apply to … any person who undertakes construction or "
    "improvement on his own residence, or who acts as his own general "
    "contractor in the performance of construction or improvement on his own "
    "residence</i>.\" No dollar cap, no square-footage limit, no state "
    "affidavit form, no holding period."))
flow.append(k.cite(
    "Miss. Code Ann. § 73-59-15(1)(b), Residential Builders and Remodelers, "
    "Title 73, Chapter 59. Read in the State Board of Contractors' "
    "<i>Residential Builders Law</i> booklet, August 2026."))

rows = [
    [k.cellp("Is there a project-cost threshold on <i>me</i>?"),
     k.cellp("<b>No.</b> The $50,000 figure everyone quotes defines who is a "
             "<b>residential builder</b> — someone building for <i>another "
             "person</i> for compensation. It is not a ceiling on your own "
             "house. You may build a $900,000 home for yourself unlicensed")],
    [k.cellp("Must you own the land?"),
     k.cellp("The exemption is written around \"<b>his own residence</b>.\" "
             "Have the deed recorded in your name before you apply — the "
             "permit office is required to see evidence that you are exempt")],
    [k.cellp("Must you live in it?"),
     k.cellp("Paragraph (b) says \"own residence,\" and the separate "
             "paragraph (d) exemption adds \"<b>will not be for sale, rent, "
             "public use or public assembly</b>.\" Build the home you mean to "
             "live in and both are satisfied")],
    [k.cellp("How many can you build?"),
     k.cellp("<b>One in any twelve months</b> — and the statute says \"within "
             "a period of one (1) year,\" which is a rolling window, "
             "<b>not</b> a calendar year. See the section below; this is the "
             "most misquoted line in Mississippi owner-building")],
    [k.cellp("What do you file?"),
     k.cellp("No state form exists. The <b>building official</b> is the one "
             "under a duty — they must refuse your permit unless you furnish "
             "evidence you are licensed <i>or exempt</i>. What counts as "
             "evidence is set locally (§ 73-59-17)")],
    [k.cellp("Can you hire subs?"),
     k.cellp("Yes — and here is the sting. <b>Your exemption is yours "
             "alone.</b> For electrical, plumbing, mechanical and HVAC, "
             "anyone you hire must hold a state license <b>no matter how "
             "small the job is</b>. Not $10,000. Zero")],
]
flow.append(k.ref_table(
    "The exemption at a glance",
    [k.cellp("Question", bold=True), k.cellp("Mississippi's answer", bold=True)],
    rows, [2.5 * inch, CW - 2.5 * inch]))

# ---------------------------------------------------------------- four exemptions
flow += k.h2_tight("FOUR EXEMPTIONS IN ONE SECTION — AND THEY ARE NOT THE SAME")
flow.append(k.body(
    "Section 73-59-15 lists seven exemptions. <b>Four of them can apply to an "
    "owner-builder</b>, they carry different conditions, and only two of them "
    "are capped at one house a year. Most guides quote one and miss the rest, "
    "which is how readers end up believing Mississippi is stricter than it "
    "is."))

ex_rows = [
    [k.cellp("<b>(1)(b)</b><br/>Your own residence"),
     k.cellp("\"<i>Any person who undertakes construction or improvement on "
             "his own residence, or who acts as his own general contractor "
             "…</i>\" <b>This is your exemption.</b> No cost cap and no "
             "not-for-sale wording inside the paragraph itself"),
     k.cellp("Capped by (2): <b>one a year</b>")],
    [k.cellp("<b>(1)(c)</b><br/>For a relative"),
     k.cellp("Building, or acting as GC, where the owner is \"<i>related to "
             "such person by consanguinity or direct affinity</i>\" and the "
             "property \"<i>will not be for sale, rent, public use or public "
             "assembly</i>.\" Covers building for a parent or child who will "
             "live there"),
     k.cellp("Capped by (2): <b>one a year</b>")],
    [k.cellp("<b>(1)(d)</b><br/>Owner in charge"),
     k.cellp("\"<i>The owners of property who supervise, superintend, "
             "oversee, direct or in any manner assume charge of the "
             "construction … on such property for use by such owner and which "
             "will not be for sale, rent, public use or public assembly</i>\""),
     k.cellp("<b>Not</b> capped by (2)")],
    [k.cellp("<b>(1)(g)</b><br/>No-permit county"),
     k.cellp("\"<i>Any person who constructs two (2) single residences or "
             "less within a period of one (1) year <b>in any county or "
             "municipality which does not require a building permit</b> or "
             "any local certification …, provided that the person is not "
             "building the residences for sale</i>\""),
     k.cellp("<b>Two</b> a year")],
]
flow.append(k.ref_table(
    "The four that can cover an owner-builder",
    [k.cellp("Exemption", bold=True),
     k.cellp("What the statute actually says", bold=True),
     k.cellp("Limit", bold=True)],
    ex_rows, [1.35 * inch, CW - 1.35 * inch - 1.25 * inch, 1.25 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "Read (1)(d) and (1)(g) before you assume you are capped at one", [
        Paragraph("Subsection (2) — the one-a-year cap — names only "
                  "\"<i>a person specified in subsection (1)(b) or (c)</i>.\" "
                  "<b>Paragraph (d) is not in that list.</b> An owner who "
                  "assumes charge of construction on their own property, for "
                  "their own use, not for sale or rent, is exempt under (d) "
                  "and subsection (2) does not reach them by its terms.",
                  S["body"]),
        Paragraph("And paragraph (g) runs the other way: in a county or "
                  "municipality that <b>does not require a building "
                  "permit</b>, anyone building not-for-sale gets <b>two</b> "
                  "residences in a year, not one. Mississippi wrote a "
                  "no-permit-jurisdiction exemption directly into its "
                  "licensing law — which tells you how normal no-code "
                  "counties are here.", S["body"]),
        Paragraph("None of this is permission to run a building business out "
                  "of the exemptions. If you are building one home to live "
                  "in, rely on (1)(b), stay inside the twelve months, and "
                  "treat (d) and (g) as the belt to that pair of braces.",
                  S["body"]),
    ]))
flow.append(k.cite(
    "Miss. Code Ann. § 73-59-15(1)(b), (c), (d), (g) and § 73-59-15(2), "
    "quoted verbatim. Verified August 2026."))

# ---------------------------------------------------------------- the year rule
flow += k.h2_tight("THE ONE-A-YEAR RULE — AND WHY \"CALENDAR YEAR\" IS WRONG")
flow.append(k.body(
    "This is the single most misquoted sentence in Mississippi owner-"
    "building, and getting it wrong costs you a build season. The statute "
    "reads: \"<i>A person specified in subsection (1)(b) or (c) shall not "
    "make more than one (1) application for a permit to construct a single "
    "residence or shall not construct more than one (1) single residences "
    "<b>within a period of one (1) year</b>.</i>\""))

flow.append(k.callout(
    "A rolling twelve months, not January to December", [
        Paragraph("\"<b>Within a period of one (1) year</b>\" is a rolling "
                  "window measured from your last permit application or "
                  "completed residence. It is not the calendar. Guides that "
                  "print \"one dwelling per calendar year\" are describing a "
                  "rule Mississippi did not write, and the difference is "
                  "real: under a calendar-year reading you could pull a "
                  "permit in December and another in January. Under the words "
                  "actually in the statute, that is two applications inside "
                  "one year and the presumption attaches.", S["body"]),
        Paragraph("The second sentence supplies the machinery: \"<i>There "
                  "shall be a <b>rebuttable presumption</b> that such person "
                  "intends to construct for the purpose of sale, lease, rent "
                  "or any similar purpose if more than one (1) application is "
                  "made for a permit to construct a single residence or if "
                  "more than one (1) single residences is constructed within "
                  "a period of one (1) year.</i>\" Being presumed to build "
                  "for sale drops you into the definition of a "
                  "<b>residential builder</b> in § 73-59-1(b) — someone who "
                  "\"constructs a building or structure <b>for sale</b> for "
                  "use by another as a residence\" — and that person needs a "
                  "license.", S["body"]),
        Paragraph("<b>Rebuttable</b> is the operative word. It is a "
                  "presumption, not a bar: you are entitled to show the "
                  "second house was genuinely for your own use, or for a "
                  "relative under (1)(c). Keep the evidence that proves it — "
                  "a homestead exemption filing, a construction loan in your "
                  "name, a change of address, utility accounts.", S["body"]),
    ]))
flow.append(k.cite(
    "Miss. Code Ann. § 73-59-15(2); definition of \"residential builder\" at "
    "§ 73-59-1(b). Verified August 2026."))

# ---------------------------------------------------------------- what you show
flow += k.h2_tight("WHAT YOU HAVE TO SHOW THE PERMIT COUNTER")
flow.append(k.body(
    "There is no statewide owner-builder affidavit in Mississippi. What there "
    "is, is a duty running the other way — <b>on the building official, not "
    "on you</b>. The clerk at the counter is required by statute to ask."))
flow.append(k.callout(
    "The building official must refuse a permit unless you prove one of two things",
    [
        Paragraph("\"<i>The building official, or other authority charged "
                  "with the duty of issuing building or similar permits, of "
                  "any municipality or county, <b>shall refuse to issue a "
                  "permit</b> for any undertaking which would classify the "
                  "applicant as a residential builder or remodeler under this "
                  "chapter <b>unless the applicant has furnished evidence "
                  "that he is either licensed as required by this chapter or "
                  "exempt from the requirements of this chapter</b>.</i>\"",
                  S["body"]),
        Paragraph("So you will be asked to prove your exemption, and the "
                  "statute does not say what proof looks like — that is set "
                  "locally. In practice the counter wants a <b>recorded deed "
                  "in your name</b> and a signed statement that the home is "
                  "for your own use. Some offices have their own homeowner "
                  "affidavit; some will ask you to sign the permit "
                  "application itself. Ask which, before you drive there, and "
                  "write the answer into MS.4.", S["body"]),
        Paragraph("The same section obliges the official to \"<i>report to "
                  "the board the name and address of any person who, in his "
                  "opinion, has violated this chapter</i>.\" The counter is "
                  "not adversarial — but it is a reporting channel to the "
                  "Board, which is a good reason to be straightforwardly "
                  "accurate about what you are building and why.", S["body"]),
    ]))
flow.append(k.cite(
    "Miss. Code Ann. § 73-59-17, quoted verbatim. Separately, § 73-59-18 "
    "requires residential <i>contractors</i> to hold a Department of Revenue "
    "permit under § 27-65-27 before obtaining a building permit — and says in "
    "terms that \"<i>a residential contractor is not a person building, "
    "repairing or renovating his or her own residence</i>,\" so it does not "
    "reach you."))

# ---------------------------------------------------------------- the trap
flow += k.h2_tight("THE ZERO-DOLLAR RULE — WHAT EVERY GUIDE GETS WRONG")
flow.append(k.body(
    "Search for Mississippi trade licensing and you will be told, over and "
    "over, that residential electrical, plumbing and HVAC work needs a state "
    "license \"<b>when the job exceeds $10,000</b>.\" That is wrong, and it "
    "is wrong in the direction that gets owner-builders in trouble."))

flow.append(k.callout_long(
    "Where the $10,000 figure really comes from — and what the statute says", [
        Paragraph("<b>$10,000 is the REMODELER threshold.</b> Section "
                  "73-59-1(c) defines a \"remodeler\" as someone who, for "
                  "compensation, undertakes \"<i>the construction, or "
                  "superintending of the construction, of improvements to an "
                  "existing residence when the total cost of the improvements "
                  "exceeds Ten Thousand Dollars ($10,000.00)</i>.\" It is a "
                  "threshold about <b>remodeling someone else's house</b>. It "
                  "has nothing to do with the trades.", S["body"]),
        Paragraph("<b>The trades have no threshold at all.</b> Section "
                  "73-59-3(1) lists who must be licensed by the Board, and "
                  "paragraph (d) reaches \"<i>any subcontractor, <b>of any "
                  "tier</b>, performing the following work or within the "
                  "following trade, on any residential construction or "
                  "residential improvement project, <b>no matter the dollar "
                  "amount of the construction or improvements</b>: (i) "
                  "Electrical; (ii) Plumbing; (iii) Mechanical; and/or (iv) "
                  "Heating, ventilation and/or air conditioning</i>.\"",
                  S["body"]),
        Paragraph("Read \"no matter the dollar amount\" literally, because it "
                  "is meant literally. The electrician who sets your "
                  "temporary power pole for $700 needs a state license. So "
                  "does the plumber who ties in a single fixture, and the "
                  "HVAC contractor who hangs one condenser. And \"of any "
                  "tier\" closes the other door: it is not enough that the "
                  "company you hired is licensed if they push the work down "
                  "to an unlicensed crew.", S["body"]),
        Paragraph("<b>Your exemption does not travel to them.</b> Section "
                  "73-59-15 exempts <i>you</i>, the person building your own "
                  "residence. It does not exempt the people you pay. Verify "
                  "every trade contractor's license with the Board before "
                  "they start — the Board publishes a license search at "
                  "<b>msboc.us</b> — and write the verification date into the "
                  "checklist below.", S["body"]),
    ]))
flow.append(k.cite(
    "Miss. Code Ann. § 73-59-3(1)(d) and § 73-59-1(c), quoted verbatim from "
    "the State Board of Contractors' <i>Residential Builders Law</i> booklet "
    "(msboc.us → Laws), August 2026."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "And the one you would never guess: hiring a \"construction manager\"", [
        Paragraph("If you bring in a consultant to run your build for you — "
                  "someone who is not a licensed builder but who takes a fee "
                  "to manage the job — <b>they need a license too.</b> "
                  "Section 73-59-3(1)(c) licenses anyone \"<i>acting in the "
                  "capacity as a construction manager through a contract or "
                  "an agreement with the owner of the property being improved "
                  "or constructed upon</i>.\"", S["body"]),
        Paragraph("And the definition anticipates exactly your situation. A "
                  "construction manager is \"<i>any person or entity, "
                  "<b>other than a residential builder, remodeler or "
                  "owner</b>, who has a contract or agreement with the owner "
                  "of the property …, <b>no matter if that owner himself is "
                  "the general contractor or a holder of a building "
                  "permit</b></i>.\" You are excluded by name — the owner is "
                  "never their own construction manager. But the person you "
                  "hire to stand in your shoes is not excluded.", S["body"]),
    ]))
flow.append(k.cite(
    "Miss. Code Ann. § 73-59-3(1)(c); definition at § 73-59-1(h)."))

# ---------------------------------------------------------------- own trade work
flow += k.h2_tight("DOING YOUR OWN ELECTRICAL, PLUMBING AND HVAC")
flow.append(k.body(
    "Chapter 59 does not reach you here, and it is worth being precise about "
    "why. The trade licensing requirement in § 73-59-3(1)(d) is written for "
    "\"<b>any subcontractor, of any tier</b>\" — you are not a subcontractor "
    "of anyone on your own house. And § 73-59-15(1)(b) says the "
    "<b>chapter</b> — all of it, including § 73-59-3 — \"shall not apply\" to "
    "a person undertaking construction on their own residence. <b>The State "
    "of Mississippi does not require you to be a licensed electrician to wire "
    "your own home.</b>"))
flow.append(k.callout(
    "But the state is not the only government involved", [
        Paragraph("Counties and municipalities have independent statutory "
                  "authority to adopt building, plumbing, electrical, gas and "
                  "sanitary codes — counties under Miss. Code Ann. § 19-5-9 "
                  "(and only for the <b>unincorporated</b> areas of the "
                  "county), municipalities under § 21-19-25. A local code can "
                  "carry its own rules about who may pull a trade permit and "
                  "who may do the work, and some Mississippi jurisdictions do "
                  "restrict homeowner electrical, gas and mechanical work on "
                  "life-safety grounds even on an owner-occupied home.",
                  S["body"]),
        Paragraph("This kit will not tell you that your city allows it, "
                  "because that is not a statewide fact and anyone who tells "
                  "you otherwise is guessing. <b>Ask before you buy wire</b>, "
                  "get the answer from the office that issues the permit, and "
                  "record it in MS.4. If no local code has been adopted on "
                  "your parcel at all — which is common in Mississippi — then "
                  "there is no local rule to break, and your own competence "
                  "is the only thing standing between you and a house fire. "
                  "Build to the code anyway.", S["body"]),
    ]))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS BEFORE YOU APPLY")
flow.append(k.body(
    "Every line below is a condition Mississippi law imposes or a fact the "
    "permit counter is required to ask you about. Work down it with a pen. If "
    "you cannot check a box, resolve it before you file — not after."))

flow += k.check_table("Step 1 — Ownership and intent", [
    ("Deed recorded in your name before the permit application date — the "
     "exemption is written around \"his own residence\"",
     [("Recorded:", 0.5), ("Parcel ID:", 0.5)]),
    "You intend the finished home for your <b>own use</b> — not as a rental, "
    "spec house, or flip. Paragraph (1)(d) puts it as \"will not be for sale, "
    "rent, public use or public assembly\"",
    ("No other residence permit applied for, and no other residence "
     "completed, in the previous twelve months — a <b>rolling</b> year, not "
     "the calendar (§ 73-59-15(2))",
     [("Last permit date:", 1.0)]),
    "You can evidence your intent if the Board ever asks: homestead "
    "exemption filing, construction loan in your name, address change, "
    "utility accounts in your name",
    ("You have asked the permit office what it accepts as \"evidence … that "
     "he is … exempt\" under § 73-59-17, and have that item ready",
     [("Asked on:", 0.45), ("They accept:", 0.55)]),
], notes_header="Notes / evidence")

flow += k.check_table("Step 2 — Everyone you are paying", [
    "<b>Electrical:</b> contractor holds a current State Board of Contractors "
    "license — required <b>no matter the dollar amount</b>",
    "<b>Plumbing:</b> contractor licensed — same zero-dollar rule",
    "<b>Mechanical / HVAC:</b> contractor licensed — same zero-dollar rule",
    "<b>Any tier below them:</b> you have asked each trade contractor whether "
    "they will subcontract any part of the work, and to whom — § 73-59-3(1)(d) "
    "reaches subcontractors \"of any tier\"",
    ("Every license verified at msboc.us before work started — not after",
     [("Verified on:", 1.0)]),
    "If you have engaged anyone to <b>manage</b> the build for a fee, they "
    "hold a license as a construction manager (§ 73-59-3(1)(c))",
    "Any general trades contractor building for you (rather than with you) "
    "over $50,000 holds a residential builder license",
], notes_header="License # / verified")

flow.append(k.body(
    "<b>Step 3 — the paperwork itself</b> (whether a building permit exists "
    "on your parcel at all, the septic and flood approvals that apply even "
    "where it does not, and everything your county adds on top) is worked in "
    "<b>MS.2 Permit Application Checklist</b>, and each document is described "
    "in <b>MS.5 Forms &amp; Documents Index</b>."))

# ---------------------------------------------------------------- losing it
flow += k.h2_tight("WHAT TAKES THE EXEMPTION AWAY — AND WHAT IT COSTS")
flow.append(k.bullet(
    "<b>Building something you never intended to occupy</b> — a spec house, a "
    "rental, a flip. Intent to build for sale is the whole test."))
flow.append(k.bullet(
    "<b>A second residence inside twelve rolling months</b>, which raises the "
    "rebuttable presumption that the purpose was sale."))
flow.append(k.bullet(
    "<b>Not owning the property</b> the residence sits on."))
flow.append(Spacer(1, 4))
flow.append(k.body(
    "If you fall outside every exemption, Mississippi's consequences are "
    "specific. Undertaking residential construction without a required "
    "license is a <b>misdemeanor</b>, and on conviction carries a fine of "
    "\"<i>not less than One Hundred Dollars ($100.00) and not more than Five "
    "Thousand Dollars ($5,000.00) or … imprison[ment] for not less than "
    "thirty (30) nor more than sixty (60) days in the county jail, or "
    "both</i>.\" The Board may separately \"<i>issue a citation and may stop "
    "work</i>.\""))
flow.append(k.callout(
    "The civil consequence that actually bites", [
        Paragraph("An unlicensed party who needed a license \"<i>may not "
                  "bring any action, either at law or in equity, to enforce "
                  "any contract for residential building or remodeling or to "
                  "enforce a sales contract</i>,\" and may recover only "
                  "\"<i>actual documented expenses for labor, materials or "
                  "both … but only for those expenses which can be shown by "
                  "<b>clear and convincing evidence</b></i>.\"", S["body"]),
        Paragraph("Note which way this points for you. It is the <b>unlicensed "
                  "contractor</b> who loses the right to sue — so a trade "
                  "contractor working on your house without the license "
                  "§ 73-59-3(1)(d) requires cannot enforce their contract "
                  "against you, and no profit is recoverable, only documented "
                  "cost proved to a heightened standard. That is a reason to "
                  "hire licensed trades, not a reason to hire unlicensed ones: "
                  "a contractor with nothing to lose in court is a contractor "
                  "with no incentive to finish.", S["body"]),
        Paragraph("None of this touches a genuine owner-builder. You are "
                  "exempt, so there is no offense. It matters because it "
                  "shows where Mississippi draws the line, and how sharp the "
                  "edge is on the other side of it.", S["body"]),
    ]))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("The owner-builder exemption: the chapter does not apply to a person "
     "building, or acting as their own general contractor on, their own "
     "residence — with no cost cap", "§ 73-59-15(1)(b)"),
    ("The relative exemption (consanguinity or direct affinity, not for sale "
     "or rent); the owner-in-charge exemption; and the two-residence "
     "exemption in a jurisdiction that requires no building permit",
     "§ 73-59-15(1)(c), (d), (g)"),
    ("One permit application or one residence \"within a period of one (1) "
     "year\" — a rolling twelve months — and the rebuttable presumption of "
     "building for sale. Applies to (1)(b) and (c) only", "§ 73-59-15(2)"),
    ("\"Residential builder\" means building for sale for another, or for "
     "compensation for another over $50,000 and not more than three floors; "
     "\"remodeler\" is improvements over $10,000", "§ 73-59-1(b), (c)"),
    ("Electrical, plumbing, mechanical and HVAC subcontractors of any tier "
     "must be licensed \"no matter the dollar amount\" — there is no $10,000 "
     "trade threshold", "§ 73-59-3(1)(d)"),
    ("A construction manager engaged by the owner must be licensed, and the "
     "definition excludes the owner by name",
     "§ 73-59-3(1)(c); § 73-59-1(h)"),
    ("The building official shall refuse a permit unless furnished evidence "
     "of license or exemption, and shall report suspected violations",
     "§ 73-59-17"),
    ("A person building his or her own residence is not a \"residential "
     "contractor\" and so needs no Department of Revenue permit",
     "§ 73-59-18; § 27-65-27"),
    ("Misdemeanor, $100–$5,000 and/or 30–60 days; no action to enforce the "
     "contract, and recovery limited to documented expenses proved by clear "
     "and convincing evidence; Board may cite and stop work",
     "§ 73-59-9(1), (2), (3)"),
    ("County codes may be adopted only for the unincorporated areas of the "
     "county; municipalities adopt by ordinance",
     "§ 19-5-9; § 21-19-25"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ms-permit-kit",
                       "MS.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
