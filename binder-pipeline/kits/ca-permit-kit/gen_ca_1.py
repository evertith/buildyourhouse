#!/usr/bin/env python3
"""CA.1 Owner-Builder Exemption Walkthrough.

Every California claim in this document was read out of the statute text at
leginfo.legislature.ca.gov in August 2026 and is cited on-page. Where the
statute is silent or jurisdictions differ, the document says so and gives the
verification step.

Verified sources (with the amendment line each page prints):
  B&P 7044      the four owner-builder exemptions; the two sale presumptions
                (Stats. 2016, Ch. 714 — SB 944)
  B&P 7048      minor-work exemption: <$1,000, no permit, not part of a larger
                job, solo, no advertising. SUBSTANCE is AB 2622 (Stats. 2024,
                Ch. 240), eff. Jan 1 2025 — it did the $500->$1,000, the
                no-permit condition and the (c)(2) no-employees condition, and
                has no sunset. The later line, Stats. 2025 Ch. 67 (AB 1170),
                is the annual maintenance-of-the-codes bill and moved a comma.
                Corroborated by 7027.2 — AB 2622's other section, untouched by
                AB 1170 — which still reads "(Amended by Stats. 2024, Ch. 240,
                Sec. 1. (AB 2622) Effective January 1, 2025.)"
  B&P 7044.01   ANY licensed contractor, contractors' association, labor
                organization, affected consumer, DA or the AG may seek an
                injunction against a non-exempt owner-builder, need not prove
                irreparable injury, and gets attorney's fees if it prevails —
                as does a prevailing defendant (Stats. 2009, Ch. 307 — SB 821)
  H&S 19825(c)  THE MANDATORY DISCLOSURE. "Notice to Property Owner" +
                "Owner's Acknowledgment and Verification of Information",
                12 initialed items, on the ISSUER's letterhead. "A permit
                shall not be issued unless the property owner complies with
                this section." (Stats. 2010, Ch. 697 — SB 189)
  Evid 606/620  what "presumption affecting the burden of proof" and
                "conclusive presumption" actually mean
  B&P 7031      unlicensed person cannot sue for payment; owner may recover
                ALL compensation paid (Stats. 2020, Ch. 312 — SB 1474)
  B&P 7031.5    permit applicant must state the basis of the exemption;
                $500 civil penalty. NOTE: 7031.5 does NOT itself say "under
                penalty of perjury" — that comes from H&S 19825.
  B&P 7028      unlicensed contracting is a misdemeanor; (h) the person who
                hired them is a victim of crime
  B&P 7026      "contractor" includes demolition and site clearing
  B&P 7057      GC needs two unrelated trades; may not contract fire
                protection or C-57 well drilling without the classification
  H&S 19825     THE STATUTORY PERMIT APPLICATION — every city and county must
                use "substantially the same form." Contains the Owner-Builder
                Declaration, the Workers' Compensation Declaration, and the
                agent authorization in (b).
  Lab 3700      every employer shall secure compensation — no minimum
                employee count in California
  Lab 3351(d)   residential employee (Stats. 2023, Ch. 133 — AB 1766)
  Lab 3352(a)(8) the exclusion: under 52 hours OR wages not more than $100 in
                the 90 days before injury. EITHER, not both.
  Lab 3352(a)(1) parent, spouse or child excluded
  Lab 3706      no coverage => employee sues at law, no exclusive remedy
  Lab 3800      permit applicant signs the comp declaration under penalty of
                perjury, per H&S 19825
  Civ 8172      construction lender block on the permit application

Deliberately hedged: whether a construction helper on a NEW build is a
"residential employee" within Lab 3351(d) at all (the carve-out is written for
household employees), and whether a given jurisdiction limits owner
self-performed electrical work.
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

FORM_ID = "CA.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "Exemption & Qualification"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "How California's owner-builder exemption actually works — which of the "
    "four exemptions you are claiming, the declaration you sign under penalty "
    "of perjury, and the sentence in it that is stricter than the statute "
    "everyone quotes.")

flow.append(k.disclaimer(
    "Statute text was read at leginfo.legislature.ca.gov in August 2026; "
    "every section page prints its own amendment history."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION")
flow.append(k.body(
    "California does not have a dollar threshold above which you need a "
    "general contractor. It has something simpler and stricter: "
    "<b>contracting at all requires a license</b>, and \"contractor\" is "
    "defined broadly enough to cover almost any construction work done for "
    "someone else. The Contractors State License Law then carves owners out "
    "of it. If you own the property and are not building to sell, § 7044 "
    "means the licensing chapter simply <i>does not apply to you</i> — at any "
    "project cost."))
flow.append(k.cite(
    "B&amp;P § 7026 (\"contractor\" is synonymous with \"builder\" and reaches "
    "anyone who undertakes to construct, alter, improve, move, wreck or "
    "demolish a structure \"or to do any part thereof\"); § 7044 (the owner "
    "exemptions); § 7028 (unlicensed contracting is a misdemeanor). Note that "
    "the licensing question and the <i>permit</i> question are different: "
    "being exempt from a license never exempts you from a permit."))


# ---------------------------------------------------------------- four exemptions
flow += k.h2_tight("IT IS FOUR EXEMPTIONS, NOT ONE — B&amp;P § 7044(a)")
flow.append(k.body(
    "This is the single most useful thing to understand before you go to the "
    "counter. Section 7044(a) contains <b>four separate exemptions</b> with "
    "<b>different conditions</b>. Guides that describe \"the § 7044 owner-"
    "builder exemption\" as one rule blur conditions from one branch into "
    "another — which is where the phantom \"you must live there a year "
    "first\" rule comes from. Find your branch, then read only its "
    "conditions."))

ex_rows = [
    [k.cellp("<b>(a)(1)</b><br/>You do the work"),
     k.cellp("An owner who builds or improves a structure on their property, "
             "provided <b>both</b>: (A) \"<i>None of the improvements are "
             "intended or offered for sale</i>,\" and (B) the owner "
             "\"<i>personally performs all of the work</i>\" or any work not "
             "performed by the owner is done by \"<i>the owner's employees "
             "with wages as their sole compensation</i>.\" "
             "<b>No cap on structures.</b>"),
     k.cellp("The main new-build branch. Note (B): a helper paid in a profit "
             "share, in trade, or in beer is not an employee on wages — and "
             "the moment you do have employees, see workers' comp below.")],
    [k.cellp("<b>(a)(2)</b><br/>Licensed subs do the work"),
     k.cellp("An owner who builds or improves on their property, provided "
             "<b>both</b>: (A) the owner \"<i>directly contracts with "
             "licensees who are duly licensed to contract for the work of the "
             "respective trades</i>,\" and (B) for single-family residential "
             "structures, <b>no more than four</b> are intended or offered "
             "for sale in a calendar year — \"<i>This subparagraph shall not "
             "apply if the owner contracts with a general contractor for the "
             "construction.</i>\""),
     k.cellp("The four-structure cap lives <b>only here</b>, and switches off "
             "entirely when a licensed GC is used. Summaries routinely report "
             "the cap without either qualification.")],
    [k.cellp("<b>(a)(3)</b><br/>Improving your own home"),
     k.cellp("A homeowner improving their principal place of residence, "
             "provided <b>all</b>: (A) the work is performed prior to sale; "
             "(B) the homeowner \"<i>has actually resided in the residence "
             "for the 12 months prior to completion of the work</i>\"; and "
             "(C) they have not used this exemption \"<i>on more than two "
             "structures more than once during any three-year period</i>.\""),
     k.cellp("A <b>remodel</b> branch. This — not new construction — is where "
             "the 12-month residency requirement lives. If you are building "
             "from scratch on raw land, this branch is not yours.")],
    [k.cellp("<b>(a)(4)</b><br/>Self-help housing"),
     k.cellp("A nonprofit corporation assisting an owner-builder in a mutual "
             "self-help housing program, as those terms are defined in Health "
             "&amp; Safety Code § 50692(a) and § 50078."),
     k.cellp("Narrow. Relevant if you are building through an organized "
             "self-help program rather than alone.")],
]
flow.append(k.ref_table(
    "The four exemptions in B&amp;P § 7044(a) — find yours before you sign",
    [k.cellp("Branch", bold=True), k.cellp("What the statute requires", bold=True),
     k.cellp("What it means for you", bold=True)],
    ex_rows, [1.15 * inch, CW - 1.15 * inch - 1.85 * inch, 1.85 * inch]))
flow.append(k.cite(
    "B&amp;P § 7044(a)(1)–(4), quoted from the section text at "
    "leginfo.legislature.ca.gov. Current text amended by Stats. 2016, "
    "Ch. 714, Sec. 1 (SB 944), effective January 1, 2017 — verified still "
    "current August 2026."))

flow.append(k.callout_long("Can you mix branches — some work yourself, some subbed?", [
    Paragraph("Read strictly, (a)(1) and (a)(2) are alternatives, and most "
              "owner-builders do both: self-perform some trades and hire "
              "licensed subs for the rest. The statutory permit application "
              "settles the practical question — the Owner-Builder Declaration "
              "in Health &amp; Safety Code § 19825 gives you a box that reads "
              "\"<i>I, as owner of the property, or my employees with wages "
              "as their sole compensation, will do (_) all of or (_) portions "
              "of the work</i>.\" The form California requires every "
              "jurisdiction to use therefore contemplates you doing "
              "<b>portions</b> of the work. Anyone you hire for the rest must "
              "be licensed for their trade.", S["body"]),
]))

# ---------------------------------------------------------------- declaration
flow += k.h2_tight("WHAT YOU SIGN — THE DECLARATION IS STATEWIDE, H&amp;S § 19825")
flow.append(k.body(
    "California does something no other state in this series does: it prints "
    "<b>the permit application itself in the statute</b>. Health and Safety "
    "Code § 19825 requires every city and county that issues building permits "
    "to use an application \"<i>in substantially the same form set forth "
    "under this subdivision</i>.\" So the declaration you sign in Siskiyou "
    "County and the one you sign in San Diego say materially the same thing, "
    "whatever the letterhead looks like."))
flow.append(k.body(
    "The statutory form runs in this order: <b>Building Project "
    "Identification</b> · <b>Licensed Contractor's Declaration</b> · "
    "<b>Owner-Builder Declaration</b> · <b>Workers' Compensation "
    "Declaration</b> · <b>Declaration Regarding Construction Lending "
    "Agency</b> (Civil Code § 8172) · a closing certification block. You will "
    "complete the third, fourth and fifth."))

flow.append(k.body(
    "<b>Two procedural requirements in § 19825 that catch people out.</b> "
    "First, the agency must \"<i>require any individual who executes the "
    "Owner-Builder Declaration to present documentation sufficient to "
    "identify the property owner and, as necessary, verify the signature of "
    "the property owner</i>\" — bring photo identification and something "
    "showing you on title. Second, if anyone other than the owner signs, "
    "§ 19825(b) requires an <b>Authorization of Agent to Act on Property "
    "Owner's Behalf</b>, completed by the owner and returned to the agency "
    "<i>before</i> the permit issues. Unlike some states, California does "
    "provide a statutory route for an agent — but it is a form, in advance, "
    "not a phone call on the day."))

flow.append(k.body(
    "The Owner-Builder Declaration itself is affirmed <b>under penalty of "
    "perjury</b> and offers three checkboxes: you (or your employees on "
    "wages) will do all or portions of the work and the structure is not "
    "intended or offered for sale; or you are exclusively contracting with "
    "licensed contractors; or you claim some other stated basis for "
    "exemption. Then comes the sentence below."))

flow.append(k.callout_long(
    "The sentence in the declaration that is stricter than § 7044", [
        Paragraph("\"<i>By my signature below I acknowledge that, except for "
                  "my personal residence in which I must have resided for at "
                  "least one year prior to completion of the improvements "
                  "covered by this permit, I cannot legally sell a structure "
                  "that I have built as an owner-builder if it has not been "
                  "constructed in its entirety by licensed contractors.</i>\"",
                  S["body"]),
        Paragraph("Every guide to California owner-building explains "
                  "§ 7044(b): sell within a year and there is a "
                  "<i>rebuttable presumption</i> you built for sale. True. "
                  "But the sworn statement you actually sign is worded as a "
                  "<b>flat prohibition</b>, its escape hatch runs "
                  "<b>backwards</b> — residence for a year <i>before</i> "
                  "completion, not a year of holding afterwards — and it "
                  "bites on exactly the structure that was not "
                  "\"constructed in its entirety by licensed contractors,\" "
                  "which is the § 7044(a)(1) owner-builder who did the work "
                  "himself.", S["body"]),
        Paragraph("Do not try to resolve that tension yourself at the "
                  "counter. If there is any chance you will need to sell "
                  "inside a year, get your building department's and, if the "
                  "money is real, a California construction lawyer's position "
                  "<b>in writing before you sign</b>. The declaration is the "
                  "document a prosecutor or a civil plaintiff will put in "
                  "front of you, not the statutory summary you read online.",
                  S["body"]),
    ]))
flow.append(k.cite(
    "Health &amp; Safety Code § 19825(a), Owner-Builder Declaration, and "
    "§ 19825(b) for the agent authorization; B&amp;P § 7031.5 for the "
    "underlying duty. Note that § 7031.5 itself does <b>not</b> use the words "
    "\"under penalty of perjury\" — it requires \"<i>a statement which he has "
    "prepared and signed</i>\" giving the basis for the alleged exemption, "
    "and sets a <b>civil penalty of not more than $500</b> for violating it. "
    "The oath comes from the § 19825 form text."))

# ------------------------------------------------- the second signed document
flow += k.h2_tight("THE SECOND DOCUMENT — THE 12 THINGS YOU INITIAL, § 19825(c)")
flow.append(k.body(
    "The Declaration is not the only thing you sign. Subdivision (c) of the "
    "same statute requires a <b>second</b> document — and it is the one that "
    "actually stops your permit."))
flow.append(k.callout_long(
    "\"A permit shall not be issued unless the property owner complies\"", [
        Paragraph("\"<i>When the Owner-Builder Declaration required under "
                  "subdivision (a) is executed, a <b>Notice to Property "
                  "Owner</b> also shall be executed by the property owner in "
                  "substantially the same form set forth under this section. "
                  "The Notice to Property Owner shall appear on the official "
                  "letterhead of the issuer … [and] shall be completed and "
                  "signed by the property owner and <b>returned prior to "
                  "issuance of the permit</b>. An agent of the owner shall not "
                  "execute this notice unless the property owner obtains the "
                  "prior approval of the permitting authority. <b>A permit "
                  "shall not be issued unless the property owner complies with "
                  "this section.</b></i>\"", S["body"]),
        Paragraph("Under that cover letter sits the <b>Owner's Acknowledgment "
                  "and Verification of Information</b>: twelve statements you "
                  "must <b>read and initial one at a time</b>, then sign and "
                  "return. Note the letterhead requirement — this is why the "
                  "form looks different in every California jurisdiction and "
                  "has no statewide form number. It is not a Contractors State "
                  "License Board publication; it is your building "
                  "department's.", S["body"]),
    ]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "Four of the twelve are worth reading before you meet them at the "
    "counter, because they are admissions you are making about your own "
    "exposure:"))
flow.append(k.bullet(
    "<b>Item 1 — unlicensed workers.</b> \"<i>I, as an Owner-Builder, may be "
    "held liable and subject to serious financial risk for any injuries "
    "sustained by an unlicensed person and his or her employees while working "
    "on my property. <b>My homeowner's insurance may not provide coverage for "
    "those injuries.</b></i>\""))
flow.append(k.bullet(
    "<b>Item 5 — when you become an employer.</b> \"<i>if I employ or "
    "otherwise engage any persons, other than California licensed "
    "Contractors, and the total value of my construction is at least <b>five "
    "hundred dollars ($500)</b>, including labor and materials, I may be "
    "considered an 'employer' under state and federal law.</i>\" Read that "
    "figure carefully: the form still says $500, and it is measuring "
    "something different from § 7048's $1,000 — becoming an <i>employer</i>, "
    "not qualifying for a licensing exemption."))
flow.append(k.bullet(
    "<b>Item 7 — building to sell.</b> \"<i>an Owner-Builder who builds "
    "single-family residential structures cannot legally build them with the "
    "intent to offer them for sale, unless all work is performed by licensed "
    "subcontractors and the number of structures does not exceed four within "
    "any calendar year, or all of the work is performed under contract with a "
    "licensed general building Contractor.</i>\" That is § 7044(a)(2) restated "
    "as something you personally acknowledge."))
flow.append(k.bullet(
    "<b>Item 8 — after you sell.</b> \"<i>if I sell the property for which "
    "this permit is issued, I may be held liable for any financial or "
    "personal injuries sustained by any subsequent owner(s) that result from "
    "any <b>latent construction defects</b> in the workmanship or "
    "materials.</i>\""))
flow.append(k.cite(
    "Health &amp; Safety Code § 19825(c) and the form text set out in that "
    "section (amended by Stats. 2010, Ch. 697, Sec. 39 — SB 189). Ask your "
    "building department to send you this form <b>before</b> the day you "
    "apply; § 19825(c) lets them provide it by mail, electronically, or at the "
    "counter, and reading twelve liability acknowledgments while a queue forms "
    "behind you is not when you want to meet them for the first time."))

# ---------------------------------------------------------------- sale rule
flow += k.h2_tight("THE SALE RULE — B&amp;P § 7044(b), AND THE PART NOBODY PRINTS")
flow.append(k.body(
    "Section 7044(b) sets two presumptions, and almost every summary reports "
    "only the first."))

flow.append(k.callout_long("Two presumptions, not one", [
    Paragraph("<b>(b)(1) — rebuttable.</b> \"<i>Except as provided in "
              "paragraph (2), proof of the sale or offering for sale of a "
              "structure by or for the owner-builder within one year after "
              "completion of the structure constitutes a rebuttable "
              "presumption affecting the burden of proof that the structure "
              "was undertaken for purposes of sale.</i>\"", S["body"]),
    Paragraph("<b>(b)(2) — conclusive.</b> \"<i>Proof of the sale or offering "
              "for sale of five or more structures by the owner-builder "
              "within one year after completion constitutes a conclusive "
              "presumption that the structures were undertaken for purposes "
              "of sale.</i>\"", S["body"]),
    Paragraph("Both phrases are terms of art, and the Evidence Code defines "
              "them. A \"<b>presumption affecting the burden of proof</b>\" "
              "operates \"<i>to impose upon the party against whom it operates "
              "the burden of proof as to the <b>nonexistence</b> of the "
              "presumed fact</i>\" (Evid. Code § 606) — so you must "
              "affirmatively prove a negative: that you did <i>not</i> build "
              "for sale. A <b>conclusive</b> presumption (Evid. Code § 620) "
              "admits no contrary evidence at all. At five structures the "
              "question is closed against you as a matter of law.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "Three details worth holding on to. The trigger is <b>sale or offering "
    "for sale</b> — putting the house on the market inside the year is "
    "enough, even if it does not sell. The clock runs from <b>completion</b>, "
    "which the section does not define. And a rebuttable presumption is not a "
    "finding of guilt: it shifts the burden onto you to show you did not "
    "build for sale. That is survivable with good records — a mortgage in "
    "your name, utilities, voter registration, a genuine reason for the move "
    "— and miserable without them."))
flow.append(k.cite(
    "B&amp;P § 7044(b)(1), (b)(2); Evidence Code § 606, § 620. <b>And note who "
    "can come after you.</b> Under B&amp;P § 7044.01 \"<i>any licensed "
    "contractor or association of contractors, labor organization, consumer "
    "affected by the violation, district attorney, or the Attorney General "
    "shall be entitled to seek injunctive relief</i>\" against an owner-builder "
    "who is neither licensed nor exempt — the plaintiff \"<i>shall not be "
    "required to prove irreparable injury</i>\" and recovers attorney's fees "
    "if it prevails. A prevailing defendant recovers fees too. This is a "
    "private enforcement channel, not just a regulator's, and a competing "
    "licensed builder who thinks you are building to sell can use it."))

# ---------------------------------------------------------------- who you pay
flow += k.h2_tight("WHO YOU MAY PAY — AND WHAT HAPPENS IF YOU PAY THE WRONG PERSON")
flow.append(k.body(
    "Your exemption covers <b>you</b>. It does nothing for the people you "
    "hire. Anyone you pay to perform work that requires a license must hold "
    "one for their trade, and the only small-job relief is § 7048 — which is "
    "narrower than its headline number suggests."))

flow.append(k.callout_long("§ 7048 has four conditions, not one", [
    Paragraph("The exemption applies only where the aggregate contract price "
              "for <b>labor, materials, and all other items is less than "
              "$1,000</b> — <b>and</b> \"<i>the work or operation does not "
              "require a building permit</i>\" (§ 7048(a)); <b>and</b> the "
              "work is not \"<i>only a part of a larger or major "
              "operation</i>,\" nor split into sub-$1,000 contracts to evade "
              "the chapter (§ 7048(b)); <b>and</b> the person does not "
              "advertise or hold themselves out as a contractor, and does not "
              "\"<i>employ another person to perform, or assist in "
              "performing, the work</i>\" (§ 7048(c)).", S["body"]),
    Paragraph("On a permitted house build, condition two is usually fatal on "
              "its own: your project requires a building permit, so § 7048 "
              "does not reach work that forms part of it. Treat § 7048 as "
              "covering the odd unpermitted errand, not your trades.",
              S["body"]),
]))
flow.append(k.cite(
    "B&amp;P § 7048. The substance is <b>AB 2622 (Stats. 2024, Ch. 240), "
    "effective January 1, 2025</b> — it raised the threshold from $500 to "
    "$1,000 and added both the \"no building permit\" condition and the "
    "no-employees condition in (c)(2). The section carries a later line, "
    "Stats. 2025, Ch. 67 (AB 1170), but that is the Legislature's annual "
    "maintenance-of-the-codes bill and its only change here was moving a "
    "comma. <b>Cite AB 2622 for the rule.</b> AB 2622 has no sunset."))

flow.append(k.body(
    "<b>If you do pay an unlicensed person, the law is on your side — "
    "expensively.</b> Under § 7031(a) an unlicensed contractor cannot sue you "
    "for payment at all, \"<i>regardless of the merits of the cause of "
    "action</i>.\" Under § 7031(b) you \"<i>may bring an action … to recover "
    "all compensation paid to the unlicensed contractor</i>\" — all of it, "
    "not the overpayment. Any security interest they took to secure payment "
    "is unenforceable (§ 7031(c)). And § 7028(h) makes you, the person who "
    "hired them, \"<i>a victim of crime … eligible … for restitution for "
    "economic losses, regardless of whether he or she had knowledge that the "
    "person was unlicensed</i>.\""))
flow.append(k.body(
    "That is a remedy, not a plan — recovering from someone unlicensed and "
    "possibly unfindable is its own project, and meanwhile their injuries are "
    "your problem. <b>Check every license before work starts and again before "
    "final payment</b> — see CA.4."))
flow.append(k.cite(
    "B&amp;P § 7031(a), (b), (c) (Stats. 2020, Ch. 312 — SB 1474); § 7028(h). "
    "Unlicensed contracting is a misdemeanor under § 7028(b): first "
    "conviction up to <b>$5,000</b> or six months in county jail or both; on "
    "a second the court must impose the greater of 20% of the contract price "
    "or $5,000, plus not less than 90 days (§ 7028(c))."))

# ---------------------------------------------------------------- workers comp
flow += k.h2_tight("WORKERS' COMPENSATION — CALIFORNIA HAS NO FREE PASS")
flow.append(k.body(
    "Many states only require workers' compensation once you employ three or "
    "more people. <b>California has no such threshold.</b> Labor Code § 3700 "
    "says \"<i>every employer except the state shall secure the payment of "
    "compensation</i>.\" One employee is enough. This is the exposure that "
    "turns a § 7044(a)(1) build — the branch that expressly contemplates "
    "\"the owner's employees\" — into a real risk."))

flow.append(k.callout_long(
    "The number that matters is 52 hours — and it is an OR", [
        Paragraph("A person doing work around a residence is an employee "
                  "under Labor Code § 3351(d). Section 3352(a)(8) then "
                  "excludes such a person if, during \"<i>the 90 calendar "
                  "days immediately preceding the date of injury</i>,\" the "
                  "employment \"comes within <b>either</b> of the following "
                  "descriptions\": (A) \"<i>The employment was, or was "
                  "contracted to be, for less than 52 hours</i>\"; or (B) "
                  "\"<i>The employment was, or was contracted to be, for "
                  "wages of not more than one hundred dollars ($100)</i>.\"",
                  S["body"]),
        Paragraph("Because it is <b>either</b>, the practical line is the "
                  "<b>52 hours</b>: a helper who works 52 hours or more in "
                  "the preceding 90 days is not excluded, whatever they were "
                  "paid. On a house build, 52 hours is a week and a half. "
                  "Three exactness points, because this sentence is misquoted "
                  "constantly: (A) is \"<b>less than</b> 52 hours\" — strict — "
                  "while (B) is \"<b>not more than</b> $100\" — inclusive; the "
                  "window is the 90 days before the <b>injury</b>, not the "
                  "length of the job; and \"<i>or was contracted to be</i>\" "
                  "counts what you agreed to, however few hours were actually "
                  "worked. Separately, § 3352(a)(1) excludes a § 3351(d) "
                  "person employed by <b>your parent, spouse, or child</b>.",
                  S["body"]),
        Paragraph("<b>And do not lean on this exclusion too hard — it may not "
                  "reach your job at all.</b> Section 3352(a)(8) excludes only "
                  "\"<i>a person described in subdivision (d) of Section "
                  "3351</i>,\" and § 3351(d) describes someone whose duties "
                  "are \"<i>incidental to the ownership, maintenance, or use "
                  "of the dwelling</i>\" or \"<i>personal and not in the "
                  "course of the trade, business, profession, or occupation of "
                  "the owner</i>.\" That language was written for housekeepers "
                  "and gardeners. If a framer or an electrician on a new build "
                  "is <b>not</b> a § 3351(d) residential employee, then the "
                  "52-hour exclusion never applies to them <b>at any number of "
                  "hours</b> — they are a plain § 3351 employee from the first "
                  "hour.", S["body"]),
        Paragraph("This kit will not tell you which way that falls, because "
                  "the statute does not resolve it and it turns on case law. "
                  "But \"I only had him for twenty hours, so I do not need "
                  "cover\" is the single most common owner-builder assumption "
                  "in California and it rests on a reading the text does not "
                  "clearly support. <b>If you are paying anyone directly, "
                  "price a policy, and get an attorney's view before you rely "
                  "on the exclusion.</b>", S["body"]),
    ]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>What going without costs.</b> The statutory permit application prints "
    "the warning in capitals: failure to secure coverage \"<i>SHALL SUBJECT "
    "AN EMPLOYER TO CRIMINAL PENALTIES AND CIVIL FINES UP TO ONE HUNDRED "
    "THOUSAND DOLLARS ($100,000), IN ADDITION TO THE COST OF COMPENSATION, "
    "DAMAGES AS PROVIDED FOR IN SECTION 3706 OF THE LABOR CODE, INTEREST, AND "
    "ATTORNEY'S FEES.</i>\" Section 3706 is the sharp end: if you have not "
    "secured coverage, an injured worker \"<i>may bring an action at law "
    "against such employer for damages, as if this division did not "
    "apply</i>\" — you lose the exclusive-remedy protection that caps a comp "
    "claim, and face an ordinary personal-injury suit with no ceiling."))
flow.append(k.body(
    "At the permit counter you will sign one of three options in the Workers' "
    "Compensation Declaration, under penalty of perjury: you self-insure; you "
    "carry a policy (carrier, number, expiry); or you \"<i>shall not employ "
    "any person in any manner so as to become subject to the workers' "
    "compensation laws of California</i>\" and will comply forthwith if that "
    "changes. Sign the third only if it is true, and revisit it the day you "
    "first hand someone cash."))
flow.append(k.cite(
    "Lab. Code § 3700 (duty to secure — no minimum employee count); "
    "§ 3351(d) (Stats. 2023, Ch. 133 — AB 1766); § 3352(a)(1), (a)(8); "
    "§ 3706 (loss of exclusive remedy); § 3800(a) (the city or county "
    "\"<i>shall require that each applicant for the permit sign a declaration "
    "under penalty of perjury verifying workers' compensation coverage or "
    "exemption from coverage, as required by Section 19825 of the Health and "
    "Safety Code</i>\"). The $100,000 warning text is quoted from the "
    "§ 19825 form itself."))

# ---------------------------------------------------------------- trade work
flow += k.h2_tight("DOING YOUR OWN ELECTRICAL, PLUMBING, AND MECHANICAL WORK")
flow.append(k.body(
    "California handles this more simply than most states. There is no "
    "separate owner exemption to qualify for trade by trade: the C-10 "
    "electrical, C-36 plumbing and C-20 mechanical classifications are "
    "classifications of <b>contractor's license</b>, and § 7044 exempts you "
    "from the licensing chapter as a whole. The classifications govern the "
    "people you hire."))
flow.append(k.callout_long("Three things that are still true", [
    Paragraph("<b>Every trade still needs a permit and an inspection.</b> "
              "Being exempt from a license is not being exempt from a permit. "
              "The remedy for skipping one is opening up finished work.",
              S["body"]),
    Paragraph("<b>Some jurisdictions restrict owner self-performed work "
              "anyway</b> — most often the main service, gas piping, or "
              "anything the utility must energize. That is local policy, not "
              "a § 7044 question. Ask your building department which trades "
              "they will let an owner-builder self-perform before you plan "
              "the work.", S["body"]),
    Paragraph("<b>Two jobs you cannot take on at all</b>: fire sprinklers and "
              "water well drilling. Section 7057(c) bars even a licensed "
              "general building contractor from contracting for a fire "
              "protection system or C-57 well drilling without that "
              "classification, and Water Code § 13750.5 gives owners no "
              "drilling exception. Both come from their own specialist.",
              S["body"]),
]))
flow.append(k.cite(
    "B&amp;P § 7057(a), (c); § 7026.12 and § 7026.13 (fire protection); Water "
    "Code § 13750.5 (C-57 well drilling). Handling refrigerant is a separate "
    "<b>federal</b> matter: EPA Section 608 technician certification is "
    "required to open a refrigerant circuit, and refrigerant may not be sold "
    "to uncertified persons (40 C.F.R. Part 82, Subpart F)."))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS BEFORE YOU APPLY")
flow.append(k.body(
    "Every line below is a condition a statute imposes or a fact the permit "
    "counter will ask you to prove. Work down it with a pen. If you cannot "
    "check a box, resolve it before you file — not after."))

flow += k.check_table("Step 1 — Ownership, intent, and your branch", [
    ("Title is recorded in your name as of the permit application date",
     [("APN:", 0.5), ("Recorded:", 0.5)]),
    ("Identified <b>which § 7044(a) branch</b> you are claiming — (1) own "
     "work, (2) licensed subs, or (3) principal-residence remodel",
     [("Branch claimed:", 1.0)]),
    "The improvements are not intended or offered for sale — no listing, "
    "purchase option or marketing exists or is contemplated — and you can "
    "hold the finished house unsold and unlisted for at least 12 months after "
    "completion",
    ("If a sale inside a year is even possible, you have your building "
     "department's written position before signing",
     [("Date requested:", 0.5), ("Response:", 0.5)]),
], notes_header="Notes / evidence")

flow += k.check_table("Step 2 — The people you will pay", [
    "Every contractor you will hire holds a current CSLB license in the "
    "right classification for their trade",
    ("Each license checked at the CSLB lookup — record the number and the "
     "date you checked", [("License #:", 0.5), ("Checked:", 0.5)]),
    "You are not relying on § 7048 to pay anyone for permitted work — it "
    "does not reach work that requires a building permit",
    "Anyone helping you who is not a licensed contractor is your employee on "
    "wages, or your parent, spouse or child",
    ("Workers' compensation decided: policy in place, or the no-employee "
     "declaration is genuinely true", [("Carrier / N/A:", 0.6), ("Policy:", 0.4)]),
    "You understand 52 hours in any 90 days makes a residential helper a "
    "covered employee, whatever they were paid",
], notes_header="Notes / evidence")

flow += k.check_table("Step 3 — At the counter", [
    "Photo identification and proof you are the owner on title, ready to "
    "present as § 19825 requires — and, if anyone else will sign for you, the "
    "Authorization of Agent completed and returned <b>before</b> issuance",
    ("<b>Notice to Property Owner</b> requested from your building department, "
     "all twelve items read and initialed, signed and returned — no permit "
     "issues without it (§ 19825(c))",
     [("Requested:", 0.5), ("Returned:", 0.5)]),
    ("You have read the Owner-Builder Declaration's closing acknowledgment — "
     "the sentence about not selling — and accept it. Construction lender "
     "named, or noted as none", [("Lender / none:", 1.0)]),
], notes_header="Notes")

flow.append(k.body(
    "<b>The rest of the paperwork</b> — plans, Title 24 compliance "
    "documentation, septic and well, fire-zone construction, grading and "
    "school fees — is worked in <b>CA.2 Permit Application Checklist</b>, and "
    "every document is described in <b>CA.5 Forms &amp; Documents Index</b>."))

# ---------------------------------------------------------------- losing it
flow += k.h2_tight("WHAT TAKES THE EXEMPTION AWAY")
flow.append(k.bullet(
    "Building something you intend to sell — the condition in § 7044(a)(1)(A) "
    "is about <b>intent at the time</b>, not only about what happens later."))
flow.append(k.bullet(
    "Selling or <b>offering for sale</b> within one year of completion, which "
    "raises the rebuttable presumption; five or more structures makes it "
    "conclusive."))
flow.append(k.bullet(
    "Not owning the property, or paying helpers as anything other than "
    "employees on wages if you are relying on § 7044(a)(1)(B)."))
flow.append(k.bullet(
    "Using the (a)(3) remodel branch without having actually resided in the "
    "home for the 12 months before the work is complete."))
flow.append(Spacer(1, 4))
flow.append(k.body(
    "Consequences the statutes actually name: a <b>$500 civil penalty</b> for "
    "a false or missing exemption statement on the application (§ 7031.5); "
    "<b>perjury</b> exposure on the declaration itself (H&amp;S § 19825); "
    "unlicensed contracting as a <b>misdemeanor</b> carrying up to $5,000 and "
    "six months on a first conviction (§ 7028(b)); and — if you employed "
    "anyone without coverage — <b>civil fines up to $100,000</b> and an "
    "uncapped tort suit by the injured worker (Lab. § 3706)."))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("No project-cost threshold; contracting for another requires a license",
     "B&amp;P § 7026, § 7028"),
    ("Four separate owner exemptions with different conditions",
     "B&amp;P § 7044(a)(1)–(4)"),
    ("Own-work branch: nothing intended or offered for sale; helpers must be "
     "employees on wages. The four-structure cap applies only to the "
     "licensed-sub branch, and the 12-month residency test only to the remodel "
     "branch", "B&amp;P § 7044(a)(1)–(a)(3)"),
    ("Sale or offering within one year — rebuttable presumption; five or more "
     "structures — conclusive", "B&amp;P § 7044(b)(1), (b)(2)"),
    ("Permit applicant must state the basis of exemption ($500 civil penalty); "
     "the application, Owner-Builder Declaration and agent authorization are "
     "fixed statewide", "B&amp;P § 7031.5; H&amp;S § 19825"),
    ("A second signed document — the Notice to Property Owner and its twelve "
     "initialed acknowledgments — gates the permit",
     "H&amp;S § 19825(c)"),
    ("Injunction by any licensed contractor, association, union, consumer, DA "
     "or the AG, with attorney's fees and no need to prove irreparable injury",
     "B&amp;P § 7044.01"),
    ("Minor-work exemption: under $1,000, no permit, not part of a larger "
     "job, solo, no advertising", "B&amp;P § 7048(a)–(c)"),
    ("Unlicensed contractor cannot sue for payment; owner may recover all "
     "compensation paid; the hirer is a crime victim",
     "B&amp;P § 7031(a), (b); § 7028(h)"),
    ("A GC may not contract fire protection or C-57 well drilling without "
     "the classification", "B&amp;P § 7057(c)"),
    ("Every employer shall secure compensation — no minimum employee count; "
     "no coverage means the worker sues at law with no exclusive remedy",
     "Lab. § 3700, § 3706"),
    ("Residential employee excluded only under 52 hours OR $100 in the "
     "preceding 90 days; parent, spouse or child excluded",
     "Lab. § 3351(d); § 3352(a)(1), (a)(8)"),
    ("Comp declaration under penalty of perjury; construction lender named",
     "Lab. § 3800(a); Civ. § 8172"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ca-permit-kit",
                       "CA.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
