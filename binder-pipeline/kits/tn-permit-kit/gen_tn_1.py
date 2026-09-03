#!/usr/bin/env python3
"""TN.1 Owner-Builder Exemption Walkthrough.

Every Tennessee claim in this document was read against its primary source in
September 2026 and is cited on-page.

CITATION POLICY FOR THIS DOCUMENT — read before editing.
Tennessee does not publish its own code in machine-readable form; the official
Tennessee Code Unannotated sits behind a LexisNexis session wall. The statutory
language quoted here was therefore taken from published Tennessee appellate
opinions that quote it verbatim, and every headline number is independently
corroborated by 2024-2026 agency documents (the Board's rules revised 18 November
2025, the State Fire Marshal's rules revised 25 February 2024, and the SFMO's
current FAQs).

The practical consequence: the SUBSTANCE is solid, but subdivision numbering has
demonstrably drifted — the same exemption is cited as § 62-6-103(2)(A),
§ 62-6-103(a)(2)(A) and § 62-6-103(a)(2)(A & B) across different opinions. So this
document cites the statute at SECTION level and quotes the sentence, rather than
printing a pinpoint subdivision that may be stale. Do not "improve" this by
adding subdivision letters without checking Lexis.

Verified sources:
  Tenn. Code Ann. § 62-6-102   "contractor" defined; $25,000; reaches anyone who
                       "undertakes to, attempts to or submits a price or bid or
                       offers to" construct — the license is needed to BID
  Tenn. Code Ann. § 62-6-102   "prime contractor" is "one who contracts directly
                       with the owner" — the hinge of this whole document
  Tenn. Code Ann. § 62-6-103   the owner exemption, and the two-year REBUTTABLE
                       PRESUMPTION of intent to resell
  Tenn. Code Ann. § 62-6-120   Class A misdemeanor, and the carve-out protecting
                       an owner who engages an unlicensed contractor to build
                       their own residence
  Rule 0680-01-.22     "Individual use shall mean use by persons other than the
                       general public"
  Rule 0680-01-.26     exemption does not reach resale, lease, rent
  Rule 0680-01-.24(1)  the four fields a sub must furnish: name, classification,
                       monetary limit, expiration date
  Rule 0680-01-.13(1)  monetary limit is 10x net worth or 10x working capital
  Rule 0680-01-.13(8)  limits may not be combined to bid a project
  Rule 0680-01-.27(3)  a licensed contractor may not pull a permit for a job an
                       unlicensed contractor is running
  Rule 0680-06-.02(1)  general liability floors by monetary limit
  Rule 0780-02-23-.05(3)  one property owner's permit per TWENTY-FOUR months
  Rule 0780-02-23-.01(i)  "property owner's permit" defined — one family dwelling
                       "in which the owner intends to live upon completion"
  Rule 0780-02-01-.05(2)(a)  homeowner electrical permit; TWELVE months; family
                       only; no unlicensed helpers
  Tenn. Code Ann. § 66-11-146  the owner-occupied lien shield — and the
                       subsection that takes it away when the owner is the prime
  Tenn. Code Ann. § 66-11-143  Notice of Completion; TEN days on 1-4 family;
                       void if recorded before completion

DELIBERATELY NOT CLAIMED, and why:
  - That a homeowner may do their own HVAC/mechanical work. No homeowner
    exemption text was found for mechanical at all, and no below-$25,000 state
    HVAC credential appears to exist. The document says what IS known and sends
    the reader to their codes office.
  - Any statement about the Notice of Nonpayment (§ 66-11-145) applying to a
    house. As enacted in 2007 that section EXCLUDES one- to four-family
    residential, which is the opposite of what most secondary sources say. The
    conflict is unresolved, so the document prints neither version.
  - That unlicensed contractors cannot lien in Tennessee. That claim appears in
    a demand letter quoted by a court, not in a holding, and the statutory text
    carries no licensure condition.
  - "In the county of residence" as an element of the exemption. It appears in
    the permit's own important-notices text but has no statutory support found.
  - The $2,500 out-of-state threshold's statutory basis. It is on the Board's
    own affidavit form, so it is real, but no TCA section was located.
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
CITE = k.CITE_COL

FORM_ID = "TN.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "Exemption & Qualification"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What Tennessee lets you do yourself — and the moment you become a prime "
    "contractor without anyone telling you.")

flow.append(k.disclaimer(
    "Tennessee's official code sits behind a subscription viewer, so the "
    "statutory sentences quoted here were read from published Tennessee "
    "appellate opinions that quote them verbatim, and every number was "
    "confirmed against the agencies' own 2024-2026 rules and guidance. Cite "
    "the section, quote the sentence, and check subdivision numbering before "
    "you rely on a pinpoint."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION", reserve=2.0)
flow.append(k.body(
    "Tennessee licenses contractors at <b>$25,000</b> and then exempts you, in "
    "one sentence, for the house you are building for yourself. The exemption "
    "is real and it is not stingy — there is no dollar cap on your own home."))
flow.append(k.body(
    "What catches people is not the exemption. It is <b>what your exemption "
    "does to everybody you hire.</b> The moment you act as your own general "
    "contractor, every trade is contracting <i>directly with the owner</i> — "
    "and Tennessee calls that a <b>prime contractor</b>."))
rows = [
    [k.cellp("Do you need a license to build your own house?"),
     k.cellp(f"<b>No.</b> A person who owns property and constructs a single "
             f"residence on it \"for individual use, and not for resale, lease, "
             f"rent or other similar purpose\" is exempt "
             f"(Tenn. Code Ann. {sec('62-6-103')})")],
    [k.cellp("Is there a dollar limit on the exemption?"),
     k.cellp("<b>None.</b> The $25,000 threshold is what makes someone a "
             "<i>contractor</i>. Your own home is exempt at any value")],
    [k.cellp("Is there a frequency limit?"),
     k.cellp("<b>Yes — two years, and it bites twice.</b> The statute creates a "
             "rebuttable presumption of intent to resell; the state permit rule "
             "makes it a hard bar. See the next section but one")],
    [k.cellp("Must you intend to live in it?"),
     k.cellp("<b>Yes.</b> The state permit rule defines a property owner's "
             "permit as one for a dwelling \"in which the owner intends to live "
             "upon completion\" (rule 0780-02-23-.01(i))")],
    [k.cellp("Does the exemption cover hiring subs?"),
     k.cellp("<b>Yes — you may act as your own general contractor.</b> But it "
             "is <i>your</i> exemption. It does not travel to anyone you hire")],
    [k.cellp("So what changes for the people you hire?"),
     k.cellp("<b>Everything.</b> They bid directly to you, which makes each of "
             "them a prime contractor — and a prime needs a license at "
             "<b>$25,000</b>, whatever the trade")],
    [k.cellp("Is there a form to sign?"),
     k.cellp("No <i>Board</i> form exists. The affidavit is built into the "
             "building permit application, and you sign it there")],
    [k.cellp("Can you do your own electrical and plumbing?"),
     k.cellp("<b>Electrical yes, on a homeowner permit — one per twelve "
             "months.</b> Plumbing yes, per the state's own exemption list. "
             "Mechanical is genuinely unclear; see the trades section")],
]
flow.append(k.ref_table(
    "The Tennessee position at a glance",
    [k.cellp("Question", bold=True), k.cellp("Tennessee's answer", bold=True)],
    rows, [2.35 * inch, CW - 2.35 * inch]))
flow.append(k.cite(
    "Contractors are licensed by the Board for Licensing Contractors within the "
    "Department of Commerce and Insurance. Its rules are chapter 0680-01, "
    "revised 18&#160;November 2025. The residential building permit rules are "
    "the State Fire Marshal's chapter 0780-02-23, revised 25&#160;February 2024."))

# ---------------------------------------------------------------- status first
flow += k.h2_tight("FIRST — FIND OUT WHICH TENNESSEE YOU ARE BUILDING IN",
                   reserve=2.0)
flow.append(k.body(
    "Before any of the rest of this matters, settle one thing: <b>who, if "
    "anyone, enforces a residential building code on your parcel.</b> Unlike "
    "most states, Tennessee publishes the answer for every jurisdiction."))
flow.append(k.callout_long(
    "The five-minute lookup", [
        Paragraph("<b>1. Open the State Fire Marshal's jurisdictions table</b> "
                  "at <i>tn.gov/commerce/fire/residential-permits/"
                  "jurisdictions-inspectors.html</i>. It lists all 95 counties "
                  "and 378 municipalities and carries its own currency date.",
                  S["body"]),
        Paragraph("<b>2. Look up your CITY first.</b> If your parcel is inside "
                  "any city limits, that city's row governs — not the county's. "
                  "A county's opt-out reaches only the unincorporated area.",
                  S["body"]),
        Paragraph("<b>3. Read the status.</b> <b>EXEMPT</b> means the local "
                  "government runs its own building department and its own "
                  "code. <b>SRBP</b> means the state enforces and you buy the "
                  "permit at core.tn.gov. <b>OPT OUT</b> means no residential "
                  "building code is enforced there at all.", S["body"]),
        Paragraph("<b>4. Do not assume it is permanent.</b> An opt-out "
                  "resolution expires 180&#160;days after that legislative "
                  "body's next election unless the new body passes it again. "
                  "Check the list again before you file, not just before you "
                  "buy the land.", S["body"]),
        Paragraph("<b>5. Get it in writing and date it.</b> Email is fine. "
                  "Write it on the directory page in TN.4. In three years, when "
                  "an appraiser asks why there is no permit on file, that email "
                  "is your answer.", S["body"]),
    ]))
flow.append(k.cite(
    "When this kit was assembled the table read \"accurate as of 8/21/2026\" "
    "and broke down as <b>50 counties EXEMPT, 37 OPT OUT and 8 SRBP</b>. "
    "<b>One warning:</b> the State Fire Marshal publishes the state-enforced "
    "county list in two places and in September 2026 they disagreed — the "
    "dated jurisdictions table listed eight counties, the apply-for-a-permit "
    "page listed seven and omitted Campbell County. TN.4 sets out both. If the "
    "two disagree when you read them, ask the office rather than picking one."))

# ---------------------------------------------------------------- the exemption
flow += k.h2_tight("THE EXEMPTION, IN FULL", reserve=2.4)
flow.append(k.callout_long(
    f"Tenn. Code Ann. {sec('62-6-103')} — the owner exemption", [
        Paragraph("\"[N]otwithstanding subdivision (a)(1), <b>any person, firm "
                  "or church that owns property and constructs on the property "
                  "single residences, farm buildings or other buildings for "
                  "individual use, and not for resale, lease, rent or other "
                  "similar purpose, is exempt from the requirements of this "
                  "part.</b>\"", S["body"]),
        Paragraph("The Board's own rule adds the definition that decides "
                  "arguments: \"Any person, business or church that owns "
                  "property and constructs single residences or buildings for "
                  "their individual use shall not need a contractor's license. "
                  "<b>Individual use shall mean use by persons other than the "
                  "general public.</b>\" (rule 0680-01-.22)", S["body"]),
        Paragraph("And a second rule closes the obvious loophole: \"This "
                  "exemption <b>does not apply to construction pertaining to "
                  "resale, lease, rent or other similar purpose</b>. The "
                  "exemption does not apply to persons constructing buildings "
                  "for a business-type purpose that cater to and depend upon "
                  "usage by members of the general public.\" (rule "
                  "0680-01-.26)", S["body"]),
    ]))
flow.append(k.cite(
    "Board rules read from the Secretary of State's official chapter 0680-01, "
    "revision of 18&#160;November 2025, at publications.tnsosfiles.com. The "
    "statutory sentence is quoted verbatim in published Tennessee appellate "
    "decisions and is restated in materially identical terms by the State Fire "
    "Marshal's current guidance."))

# ---------------------------------------------------------------- two-year rule
flow += k.h2_tight("THE TWO-YEAR RULE IS ACTUALLY TWO DIFFERENT RULES",
                   reserve=2.2)
flow.append(k.body(
    "Nearly every guide tells you Tennessee allows \"one house every two "
    "years.\" That is true at the permit counter and <b>not quite true in the "
    "statute</b> — and the difference decides what happens if you build two."))
rows = [
    [k.cellp("<b>In the statute</b><br/>" + sec("62-6-103")),
     k.cellp("A <b>rebuttable presumption</b>. There is a \"rebuttable "
             "presumption that the person or firm intends to construct for the "
             "purpose of resale, lease, rent or any other similar purpose "
             "<b>if more than one (1) application is made for a permit</b> to "
             "construct a single residence <b>or if more than one (1) single "
             "residence is constructed within a period of two (2) years</b>\""),
     k.cellp("You are not barred. The burden shifts to <b>you</b> to prove "
             "individual use — which means you are arguing it, possibly in "
             "court. Note it can be triggered by <b>applications</b>, not just "
             "finished houses")],
    [k.cellp("<b>At the permit counter</b><br/>rule 0780-02-23-.05(3)"),
     k.cellp("A <b>hard bar</b>. \"Pursuant to T.C.A. " + sec("62-6-103") +
             ", <b>an individual may obtain only one (1) property owner's "
             "permit within a twenty-four (24) month period.</b>\""),
     k.cellp("No presumption, no argument. In a state-enforced jurisdiction "
             "the system will simply not issue you a second one")],
]
flow.append(k.ref_table(
    "Same two years, two different mechanisms",
    [k.cellp("Where", bold=True), k.cellp("What it says", bold=True),
     k.cellp("What it means for you", bold=True)],
    rows, [1.5 * inch, (CW - 1.5 * inch) * 0.55, (CW - 1.5 * inch) * 0.45]))
flow.append(k.cite(
    "The permit rule is the <b>state</b> program's. In an EXEMPT jurisdiction "
    "the local government's own homeowner-permit rules apply and they differ — "
    "ask yours. The statutory presumption applies everywhere, whoever issues "
    "the permit."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "Changing your mind mid-build is the version nobody warns you about", [
        Paragraph("The exemption turns on what the house is <i>for</i>, and "
                  "Tennessee courts have measured that continuously rather than "
                  "at the start. A contractor is unlicensed for these purposes "
                  "if they do not hold a valid license <b>throughout the entire "
                  "time contracting services are performed</b>. Applied to an "
                  "owner-builder who decides part-way through to sell, the "
                  "Court of Appeals has observed that at least as to the period "
                  "after the owner knew he was going to sell, he was acting in "
                  "violation of the licensing law.", S["body"]),
        Paragraph("<b>So the decision to sell is not a decision you get to make "
                  "at the end.</b> If your plans genuinely change, stop and "
                  "take advice before you list it — and note that the state "
                  "permit rule requires a <b>new permit</b> the moment you stop "
                  "acting as the owner-builder and hire a contractor to finish.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- the prime trap
flow += k.h2_tight("THE TRAP — YOUR EXEMPTION MAKES EVERYONE ELSE A PRIME",
                   reserve=2.2)
flow.append(k.body(
    "This is the most valuable page in this document, and it is the thing "
    "Tennessee owner-builders most often get wrong. It follows from two "
    "definitions that are three sentences apart."))
flow.append(k.bullet(
    f"A <b>prime contractor</b> is \"one who contracts <b>directly with the "
    f"owner</b>\" (Tenn. Code Ann. {sec('62-6-102')})."))
flow.append(k.bullet(
    f"A <b>contractor</b> needs a license for any undertaking \"for which the "
    f"total cost is twenty-five thousand dollars ($25,000) or more\" — and the "
    f"definition reaches anyone who \"undertakes to, attempts to or <b>submits "
    f"a price or bid or offers to</b>\" do the work (Tenn. Code Ann. "
    f"{sec('62-6-102')})."))
flow.append(k.body(
    "Under a licensed general contractor, a framing or excavation sub is "
    "bidding to the <i>contractor</i>, and most trades need no state license at "
    "all. <b>When you are the general contractor, every one of them is bidding "
    "to the owner.</b> The Department of Commerce and Insurance says it in one "
    "line in its own licensing booklet:"))
flow.append(k.callout(
    "From the state's own contractor licensing booklet", [
        Paragraph("\"Subcontractors: A contractor's license is NOT required for "
                  "all subcontractors, those bidding directly to a contractor "
                  "and not the owner, for projects such as: painting, "
                  "excavation, landscaping, etc., unless, the subcontractors "
                  "are performing mechanical, plumbing, HVAC, electrical or "
                  "roofing over $25,000; and masonry if over $100,000… "
                  "<b>Note: Bidding to a homeowner acting as their own GC makes "
                  "you a &quot;Prime&quot;.</b>\"", S["body"]),
    ]))
flow.append(k.body(
    "<b>The practical rule that falls out of it:</b> any single trade contract "
    "on your job worth $25,000 or more needs a licensed contractor — including "
    "trades that would need no license under a professional builder. And the "
    "license must be held <b>before they bid</b>, not before they start: the "
    "Board's unlawful-bidding rule says an unlicensed bidder \"shall [not] be "
    "awarded any contract for the project… or [be] permitted to participate in "
    "any re-bidding of the project\" (rule 0680-01-.18)."))
rows = [
    [k.cellp("<b>Electrical, plumbing, mechanical / HVAC, roofing</b>"),
     k.cellp("$25,000 or more", center=True),
     k.cellp("Named as \"contractors\" in the statute itself")],
    [k.cellp("<b>Masonry</b>"), k.cellp("$100,000 or more", center=True),
     k.cellp("Materials and labor, per Board rule 0680-01-.24(1)")],
    [k.cellp("<b>Any other trade bidding to you</b> — framing, concrete, "
             "excavation, drywall, painting"),
     k.cellp("$25,000 or more", center=True),
     k.cellp("Because they are contracting directly with the owner, which "
             "makes them a prime")],
]
flow.append(k.ref_table(
    "When the person you hire needs a state license",
    [k.cellp("Trade", bold=True),
     k.cellp("Threshold", bold=True, center=True),
     k.cellp("Why", bold=True)],
    rows, [2.05 * inch, 1.2 * inch, CW - 3.25 * inch]))
flow.append(k.cite(
    "The cost is measured all-in. Board rule 0680-01-.13(8): no contractor may "
    "engage or offer to engage in any project \"of which the cost (<b>including "
    "all material and labor furnished by or through another source other than "
    "the owner</b>) would exceed the monetary limitation placed on his "
    "license.\" <b>And you cannot borrow someone else's license:</b> rule "
    "0680-01-.27(3) makes it misconduct for a licensed contractor to pull a "
    "permit \"for a job in which an unlicensed contractor is acting as the "
    "general contractor.\""))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "One piece of good news, and it is a real protection", [
        Paragraph("Contracting without a license is a Class A misdemeanor in "
                  f"Tennessee (Tenn. Code Ann. {sec('62-6-120')}). But the "
                  f"penalty provision carries an express carve-out for you: the "
                  f"penalties \"<b>shall not apply to a person who engages a "
                  f"contractor without a license for the purpose of "
                  f"constructing a residence for the use of that person.</b>\"",
                  S["body"]),
        Paragraph("So an owner who unwittingly hires an unlicensed builder for "
                  "their own home is not the one committing the offense. <b>The "
                  "unlicensed contractor still is</b> — and you are still the "
                  "one with an unlicensed contractor on your house, no "
                  "meaningful recourse, and a builder whose recovery against "
                  "you is capped at \"actual documented expenses.\" Verify the "
                  "license anyway.", S["body"]),
    ]))

# ---------------------------------------------------------------- trades
flow += k.h2_tight("WHAT YOU MAY DO WITH YOUR OWN HANDS", reserve=2.2)
rows = [
    [k.cellp("<b>Electrical</b>"),
     k.cellp("<b>Yes</b>, on a <b>residential property owner's electrical "
             "permit</b>. \"Any person may perform electrical work (for which "
             "an inspection is required) upon his/her own residence provided "
             "he/she first applies for and obtains\" one"),
     k.cellp("<b>Only one per 12&#160;months</b> — a different clock from the "
             "24-month building permit. Extends to you and <b>immediate "
             "family only</b>, and \"shall not authorize assistance by any "
             "other person not duly licensed\"")],
    [k.cellp("<b>Plumbing</b><br/>(incl. gas piping)"),
     k.cellp("<b>Yes.</b> The state's Limited Licensed Plumber application "
             "lists \"<b>Homeowner may perform plumbing on their own "
             f"residence</b>\" among the exemptions under {sec('62-6-406')}"),
     k.cellp("This is a <i>state</i> exemption. A city or county may still "
             "require a licensed plumber to pull the permit — the state's own "
             "guidance says the trade license is \"NOT exempt from local "
             "licensing, permit and inspection requirements\"")],
    [k.cellp("<b>Mechanical / HVAC</b>"),
     k.cellp("<b>Genuinely unclear, and we are not going to pretend "
             "otherwise.</b> No homeowner exemption text for mechanical work "
             "was found, and Tennessee appears to issue no below-$25,000 HVAC "
             "credential at all"),
     k.cellp("What <i>is</i> certain: HVAC at $25,000+ needs a licensed "
             "mechanical contractor; the <b>electrical</b> portion falls under "
             "the electrical rules and the <b>gas piping</b> under the plumbing "
             "rules. <b>Ask your codes office and write the answer down</b>")],
]
flow.append(k.ref_table(
    "Three trades, three different levels of certainty",
    [k.cellp("Trade", bold=True), k.cellp("May you do it yourself?", bold=True),
     k.cellp("The condition that matters", bold=True)],
    rows, [1.15 * inch, (CW - 1.15 * inch) * 0.48,
           (CW - 1.15 * inch) * 0.52]))
flow.append(k.cite(
    "Electrical quoted from rule 0780-02-01-.05(2)(a), revised 14&#160;July "
    "2025. Plumbing from the Department of Commerce and Insurance's own Limited "
    "Licensed Plumber application. <b>On mechanical we are reporting a genuine "
    "gap rather than filling it:</b> the Board licenses contractors, Limited "
    "Licensed Electricians and Limited Licensed Plumbers, and nothing else — "
    "which implies HVAC under $25,000 needs no state license, but no rule says "
    "so affirmatively and no homeowner exemption for mechanical work exists in "
    "the text. A guide that gives you a confident answer here is guessing."))

# ---------------------------------------------------------------- verifying
flow += k.h2_tight("VERIFYING A SUB — FOUR FIELDS, AND A NUMBER THAT TELLS YOU "
                   "MORE THAN IT LOOKS", reserve=2.0)
flow.append(k.body(
    "The Board tells you exactly what to check, because it is what a "
    "subcontractor is legally obliged to hand over: \"It is the subcontractor's "
    "responsibility to furnish evidence to the prime contractor of an active "
    "license with the appropriate <b>name, classification, monetary limit, and "
    "expiration date</b>, regardless of how the bid is transmitted\" (rule "
    "0680-01-.24(1)). You are the prime. That evidence is owed to you."))
rows = [
    [k.cellp("<b>Name</b>"),
     k.cellp("Must be the exact name they are licensed under. Rule "
             "0680-01-.25(1): \"Contracting in a name different than that in "
             "which an individual or entity is licensed by this Board is "
             "considered a violation.\" A license in a company name and an "
             "invoice in a personal name is a real problem, not a formality")],
    [k.cellp("<b>Classification</b>"),
     k.cellp("<b>BC-A</b> is residential building construction, up to four "
             "units and three stories. <b>BC-A/r</b> is Limited Residential, "
             "capped at $125,000. <b>CE</b> is electrical, <b>CMC</b> "
             "mechanical (which covers HVAC, refrigeration and gas piping)")],
    [k.cellp("<b>Monetary limit</b>"),
     k.cellp("<b>Read this one carefully — see below.</b> Limits from "
             "different classifications <b>may not be combined</b> to bid a "
             "project, and only a 10% tolerance is allowed (none at all for "
             "BC-A/r)")],
    [k.cellp("<b>Expiration date</b>"),
     k.cellp("The license must be valid <b>throughout</b> the work, not merely "
             "on the day it was signed")],
]
flow.append(k.ref_table(
    "What to check, at verify.tn.gov",
    [k.cellp("Field", bold=True), k.cellp("What it tells you", bold=True)],
    rows, [1.35 * inch, CW - 1.35 * inch]))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "The monetary limit is a free credit check, and almost nobody uses it", [
        Paragraph("Tennessee sets a contractor's monetary limit at <b>the "
                  "lesser of ten times net worth or ten times working "
                  "capital</b> (rule 0680-01-.13(1)). Read that backwards: a "
                  "builder carrying a <b>$150,000</b> limit has a "
                  "Board-reviewed file showing roughly <b>$15,000</b> of net "
                  "worth or working capital. That is the single most useful "
                  "financial fact you can obtain about a builder, for nothing, "
                  "in about a minute.", S["body"]),
        Paragraph("<b>One caveat that weakens the inference for newer "
                  "licenses.</b> From 1&#160;July 2026 the Board allows a "
                  "surety bond of at least 50% of the requested monetary limit "
                  "as an alternative to a CPA-reviewed or audited financial "
                  "statement. So a recent license may be bond-backed rather "
                  "than balance-sheet-backed. Ask which.", S["body"]),
        Paragraph("<b>And check the insurance separately.</b> The Board's own "
                  "floor for general liability is only <b>$100,000</b> for any "
                  "contractor with a monetary limit up to $500,000 (rule "
                  "0680-06-.02(1)). That is nowhere near enough cover for a "
                  "custom home. Ask for a certificate showing more.", S["body"]),
    ]))
flow.append(k.cite(
    "Verification is at <b>verify.tn.gov</b>, which is the Department's public "
    "license search. <b>It is not the same system as core.tn.gov</b>, which is "
    "where permits are bought — the two are widely confused. The Board also "
    "publishes a separate tool to verify a Qualifying Agent, which matters "
    "because the license belongs to the business while the person who passed "
    "the examination is the qualifying agent."))

# ---------------------------------------------------------------- workers comp
flow += k.h2_tight("WORKERS' COMPENSATION — WHERE OWNER-BUILDERS GET HURT",
                   reserve=2.0)
flow.append(k.body(
    "Tennessee treats construction differently from every other industry. Most "
    "businesses need workers' compensation cover at five employees. <b>In "
    "construction it starts at one</b>, and the Bureau of Workers' Compensation "
    "says so plainly: businesses in the construction industry \"are required to "
    "have workers' compensation coverage for everyone including the business "
    "owners. Other businesses need insurance if there are five or more "
    "employees.\""))
flow.append(k.body(
    "Tennessee also runs a public <b>Exemption Registry</b> where a genuine "
    "construction business owner can register an exemption for themselves. For "
    "an owner-builder that registry is a <b>verification tool, not a "
    "shield</b>:"))
flow.append(k.bullet(
    "A one-person trade contractor who tells you they are exempt <b>should be "
    "on it</b>, and it is publicly searchable. If they are not listed, the "
    "claim is empty."))
flow.append(k.bullet(
    "The registry exempts <b>the owner of the business only</b>. In the "
    "Bureau's own words: \"Exempt owners are still required to have insurance "
    "coverage for all of their employees, <b>even if they have only one "
    "employee</b>.\""))
flow.append(k.bullet(
    "A registry filing can be <b>disregarded</b> where the person is not really "
    "a business owner. Tennessee's workers' compensation court has rejected an "
    "exemption where \"the only 'assets' of any purported business are [the "
    "worker's] tools, likely of minimal value and customarily in all "
    "construction workers' possession,\" holding the filing was an attempt to "
    "avoid the Act. That is precisely the person an owner-builder hires."))
flow.append(k.callout(
    "The honest position on whether you become the employer", [
        Paragraph("Tennessee courts have held that <b>an owner does not become "
                  "a \"contractor\" merely by assuming general-contractor "
                  "responsibilities</b> on their own build, and the licensing "
                  "definition reaches only work done \"for a fixed price, fee, "
                  "commission, or gain of whatever nature\" — which cuts "
                  "against treating an owner-builder as a statutory employer. "
                  "<b>But no Tennessee decision squarely resolves it</b>, and "
                  "the closest case on the facts — an uninsured owner-builder "
                  "whose hired job-runner's worker fell — was fought for years "
                  "on other grounds and still left the owner carrying a share "
                  "of the fault.", S["body"]),
        Paragraph("<b>So: collect a certificate of workers' compensation "
                  "insurance from every trade, naming you as certificate "
                  "holder — or a Registry exemption printout plus written "
                  "confirmation that they have no employees and will bring none "
                  "on site. Then check the Registry yourself.</b> This is the "
                  "cheapest risk you will ever retire on a build.", S["body"]),
    ]))

# ---------------------------------------------------------------- liens
flow += k.h2_tight("THE LIEN SHIELD YOU GIVE UP BY BEING YOUR OWN GC",
                   reserve=2.2)
flow.append(k.body(
    "Tennessee protects homeowners from subcontractor liens unusually well — "
    "and the protection is written so that <b>becoming your own general "
    "contractor switches it off.</b> Both halves are in the same section."))
rows = [
    [k.cellp("<b>If you hire a prime contractor</b>"),
     k.cellp("On contracts to improve owner-occupied residential property, \"a "
             "lien or right of lien upon such property <b>shall exist only in "
             "favor of a prime contractor</b>.\" Your builder's unpaid subs and "
             "suppliers <b>cannot</b> lien your home")],
    [k.cellp("<b>If you ARE the prime contractor</b>"),
     k.cellp("\"When the owner of residential real property and the prime "
             "contractor are one and the same person… a lien or right of lien "
             "upon such property shall exist only in favor of the prime "
             "contractor <b>and remote contractors in contractual privity with "
             "the prime contractor</b>.\" Your own trades and suppliers "
             "<b>can</b> lien")],
]
flow.append(k.ref_table(
    f"Tenn. Code Ann. {sec('66-11-146')} — the same section, both ways",
    [k.cellp("Your role", bold=True), k.cellp("Who can lien your house",
                                              bold=True)],
    rows, [1.85 * inch, CW - 1.85 * inch]))
flow.append(k.body(
    "<b>The escape hatch is payment, and it is absolute:</b> \"No lien in "
    "favor of the remote contractor shall exist on such real property "
    "<b>from and after the date the prime contractor pays the remote "
    "contractor</b> for work or labor performed or materials, services, "
    "equipment, or machinery furnished by that remote contractor.\" Pay a trade "
    "in full and their lien right on your home is extinguished. <b>Get a lien "
    "waiver at every payment and keep them together.</b> One layer of "
    "protection does survive: someone your trade hires is not in privity with "
    "you, and the section gives them no lien."))
flow.append(Spacer(1, 4))
flow.append(k.callout(
    "The Notice of Completion — a ten-day clock you control", [
        Paragraph(f"Recording a <b>Notice of Completion</b> with the register "
                  f"of deeds when the house is finished cuts every unrecorded "
                  f"claimant's window to <b>ten days</b> on a one- to "
                  f"four-family residence, against thirty for everything else "
                  f"(Tenn. Code Ann. {sec('66-11-143')}). It is one of the few "
                  f"levers an owner holds rather than waits on.", S["body"]),
        Paragraph("<b>Two conditions.</b> Record it <i>after</i> completion — "
                  "\"[a]ny notice of completion recorded as herein provided "
                  "<b>before</b> the completion of the improvement or the "
                  "demolition is void and of no effect whatsoever.\" And serve "
                  "a copy as the section requires; the duty to serve the prime "
                  "contractor falls away where you are the prime.", S["body"]),
    ]))
flow.append(k.cite(
    "Lien text quoted from the 2007 Public Chapter that rewrote the chapter, "
    "read at publications.tnsosfiles.com, and the section architecture is "
    "confirmed as live by a 2024 Court of Appeals decision citing the 2022 "
    "code. <b>We have deliberately not printed anything about the Notice of "
    "Nonpayment.</b> As enacted, that section <i>excludes</i> one- to "
    "four-family residential — the opposite of what many secondary sources say "
    "— and we could not resolve the conflict. Ask a Tennessee construction "
    "lawyer rather than trusting either version."))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS WITH A PEN",
                   reserve=1.6)
flow += k.check_table(
    "Confirm each of these before you break ground",
    [
        ("I looked up my jurisdiction's status on the State Fire Marshal's "
         "table — my CITY first, then the county. Status and date read:",
         [("Status", 0.5), ("Date", 0.5)]),
        "I am the record owner of the parcel, and I intend to live in this "
        "house when it is finished.",
        "I am not building it for resale, lease or rent — and I understand "
        "that changing my mind mid-build does not preserve the exemption for "
        "the part already built.",
        "I have not applied for or been issued another owner-builder permit "
        "within the past 24&#160;months, and will not apply for a second within "
        "this two-year window.",
        ("I understand that every trade bidding to me is a PRIME contractor, "
         "and I have identified which contracts will reach $25,000 "
         "($100,000 for masonry). Those trades are:", [("Trades", 1.0)]),
        # Merged from two rows into one. As two, the table ran to within an
        # inch of the foot of the page and threw the closing note onto a sheet
        # of its own — a whole page for four lines of text.
        ("For every one of those, I checked name, classification, monetary "
         "limit and expiration date at verify.tn.gov — and confirmed no bid "
         "exceeds that limit, which cannot be combined across classifications. "
         "Date checked:", [("Date", 1.0)]),
        ("I collected a workers' compensation certificate naming me as "
         "certificate holder, OR a Registry exemption printout plus written "
         "confirmation of no employees, from every trade. Outstanding:",
         [("Still needed from", 1.0)]),
        ("I asked my codes office whether I may perform my own mechanical and "
         "HVAC work, because the state rules do not answer it. Answer:",
         [("Answer", 0.6), ("Who told me", 0.4)]),
        "If I am doing my own wiring, I have applied for a residential "
        "property owner's electrical permit — and I know it is one per 12 "
        "months, covers only me and immediate family, and allows no unlicensed "
        "helpers.",
        "I am collecting a signed lien waiver at every payment to every trade, "
        "because as my own prime contractor my trades can lien this house.",
        ("I know where my register of deeds is, and I will record a Notice of "
         "Completion after — never before — completion. Office:",
         [("Register of deeds", 1.0)]),
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "tn-permit-kit",
                       "TN.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
