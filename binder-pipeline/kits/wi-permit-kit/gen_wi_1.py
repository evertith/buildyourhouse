#!/usr/bin/env python3
"""WI.1 Owner-Builder Exemption Walkthrough.

Every Wisconsin claim in this document was read out of the primary source in
September 2026 and is cited on-page. Where the statute is silent or the answer
depends on a local ordinance, the document says so and gives the verification
step.

Verified sources:
  101.61(1),(3)        "dwelling" excludes a primitive rural hunting cabin, and
                       the cabin definition is GRANDFATHERED — the structure
                       must trace to one built before 31 Dec 1997
  101.615              the subchapter reaches dwellings begun on/after
                       1 Dec 1978; SPS 320.03 gives 1 Jun 1980 for chs. 320,
                       321, 323, 324, 325 and 1 Dec 1978 for ch. 322
  101.65(1c)           a nonconforming municipal ordinance is unenforceable,
                       and an owner may WAIVE a contract term requiring
                       compliance with one
  101.65(1m)           no permit to a person "required to be certified" — the
                       exempt owner is not such a person
  101.65(1r)           the cautionary statement EVERY owner applicant signs
  101.65(2)            municipalities SHALL contract with the department for
                       inspection services they do not perform
  101.651(1),(2m),(3)  the 2,500-population rule and the department as residual
                       enforcer — s. 101.651(3)(b) is the no-gap clause
  101.654(1)(a),(b)    the certification duty and the whole of the owner
                       exemption: "resides or will reside"
  101.654(1m),(2),(3)  what a certified contractor must carry — the bond or
                       $250,000 policy the owner-builder does NOT have
  101.66(1)            the code duty falls on "every builder, designer, and
                       OWNER" by name
  101.66(1m)           owner-milled lumber, the s. 36.25(48) grading
                       certificate and its 5-year recency rule
  101.66(3)            $25-$500 per violation, each day a separate offense
  101.862(1)-(4)       the electrical license rule and the owner exemption —
                       "owns and occupies", present tense
  101.178(2),(3),(5)   HVAC registration is mandatory, certification VOLUNTARY,
                       and local HVAC licensing is pre-empted
  145.06(1),(2),(4)    the plumbing license rule, the ban on license-lending,
                       and the owner exemption — "one-family building" only
  145.01(10)(a)2       POWTS work IS "plumbing" by definition
  145.04(2)            no local licensing of a state-licensed person
  102.04(1)(b)         the 3-employee and $500-quarter worker's comp triggers
  102.07(8)(b)         the NINE-part independent contractor test, conjunctive
  SPS 305.31, 305.315  the two dwelling contractor credentials
  SPS 305.70(1)(b)2    the HVAC owner exemption — "resides or will reside"
  SPS 320.09(9)(a)7    the master plumber's name and license number go ON the
                       permit at issuance — the practical answer on plumbing
  SPS 383.21(2)(c)4    the sanitary permit names the master plumber; there is
                       no owner-installer track for septic

Deliberately NOT claimed: that Wisconsin imposes a holding period, a
not-for-sale window, or an owner-occupancy period after completion. The
licensing research read s. 101.654, SPS 305.31 and SPS 305.315 in full and no
such condition exists. The only "2 years" in s. 101.654 is the continuing
education cycle for CERTIFIED contractors — it is not an owner rule.
Deliberately NOT claimed: that the electrical and plumbing owner exemptions do
or do not reach new construction. Both are written in the present tense and
neither says "new construction". The document prints the four texts side by
side, prints the drafting contrast, and sends the reader to the AHJ.
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

FORM_ID = "WI.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "Exemption & Qualification"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What Wisconsin actually lets you do yourself — and the four separate "
    "trade rules that are not the same rule.")

flow.append(k.disclaimer(
    "Statute and code text was read at docs.legis.wisconsin.gov in September "
    "2026; both change."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION")
flow.append(k.body(
    "<b>Wisconsin has no state general contractor or home builder license.</b> "
    "What it has instead is a credential attached to the <i>permit</i>: with "
    "narrow exceptions, nobody may obtain a building permit for a one- or "
    "two-family dwelling without a certificate of financial responsibility "
    "from the department. That is not a competency test. It is proof of a "
    "bond or a liability policy, worker's compensation cover, and a "
    "twelve-hour business course."))
flow.append(k.body(
    "And then Wisconsin exempts you from it in a single sentence, in words "
    "that were written with a house that does not exist yet firmly in mind."))

rows = [
    [k.cellp("Do you need a state license to build your own house?"),
     k.cellp("<b>No.</b> Wisconsin licenses no residential general contractor. "
             "The credential that normally gates the permit — the dwelling "
             "contractor certification — is expressly lifted for an owner who "
             "resides or will reside in the dwelling")],
    [k.cellp("Is there a project-cost threshold?"),
     k.cellp("<b>No.</b> The duty tracks the permit, not the project value. "
             "s. 101.654(1)(a) says “no person may obtain a building "
             "permit”, full stop")],
    [k.cellp("Must you live in it? For how long afterward?"),
     k.cellp("<b>You must reside or intend to reside in it. There is no "
             "period.</b> No holding period, no not-for-sale window, no "
             "minimum occupancy — none appears in s. 101.654, s. SPS 305.31 "
             "or s. SPS 305.315")],
    [k.cellp("Do you need a building permit?"),
     k.cellp("<b>Yes, everywhere.</b> Wisconsin has no permit-free town for a "
             "new dwelling. If nobody local enforces, the department does — "
             "see the enforcement section below")],
    [k.cellp("Does the code apply to you?"),
     k.cellp("<b>Yes, and it names you.</b> “Every builder, designer, and "
             "<b>owner</b> shall use building materials, methods, and "
             "equipment which are in conformance with the one- and 2-family "
             "dwelling code” (s. 101.66(1))")],
    [k.cellp("Can you do your own trade work?"),
     k.cellp("<b>Four different answers.</b> Heating: clearly yes. Electrical "
             "and plumbing: the exemptions are written in the present tense "
             "and a new house has no occupant. Septic: no. See the trade "
             "section — this is the heart of the document")],
]
flow.append(k.ref_table(
    "The Wisconsin position at a glance",
    [k.cellp("Question", bold=True), k.cellp("Wisconsin's answer", bold=True)],
    rows, [2.45 * inch, CW - 2.45 * inch]))
flow.append(k.cite(
    "Wis. Stat. ss. 101.654, 101.66(1); Wis. Admin. Code ss. SPS 305.31, "
    "305.315. The absence of a residential builder license is a negative — it "
    "was checked by reading the licensing provisions of Wis. Stat. ch. 101 "
    "subch. II and ch. SPS 305 in September 2026, and none creates one. "
    "Municipal business registration is a separate, genuinely local question."))

# ---------------------------------------------------------------- the exemption
flow += k.h2_tight("THE EXEMPTION, IN FULL")
flow.append(k.body(
    "Wisconsin's owner-builder exemption is one sentence long. Here it is, and "
    "here is the duty it lifts you out of."))

flow.append(k.callout_long("The rule, and the exception", [
    Paragraph("<b>The duty.</b> “<i>Subject to par. (b), no person may obtain "
              "a building permit unless the person annually obtains from the "
              "department a certificate of financial responsibility showing "
              "that the person is in compliance with sub. (2), completes the "
              "continuing education requirements described under sub. (1m), "
              "and furnishes to the issuer of the permit proof of completion "
              "of those continuing education requirements.</i>” "
              "(Wis. Stat. s. 101.654(1)(a))", S["body"]),
    Paragraph("<b>The exemption.</b> “<i><b>Paragraph (a) does not apply to an "
              "owner of a dwelling who resides or will reside in the dwelling "
              "and who applies for a building permit to perform work on that "
              "dwelling.</b></i>” (Wis. Stat. s. 101.654(1)(b))", S["body"]),
    Paragraph("<b>Read the tense.</b> “<i>resides <b>or will reside</b></i>” — "
              "the legislature wrote the future tense on purpose, and it is "
              "what makes this exemption work for a house that is not built "
              "yet. Hold on to that phrase; two of the four trade exemptions "
              "later in this document do <i>not</i> contain it, and the "
              "difference matters.", S["body"]),
    Paragraph("<b>And the code repeats it.</b> “<i>Section 101.654 (1) (b), "
              "Stats., exempts an owner of a dwelling who resides or will "
              "reside in the dwelling and who applies for a building permit to "
              "perform work on the dwelling from obtaining a dwelling "
              "contractor financial responsibility certification.</i>” "
              "(Note to s. SPS 305.31)", S["body"]),
]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>What the sentence does not say is as important as what it says.</b> "
    "The full text of s. 101.654 and of both administrative rules was read in "
    "September 2026. There is <b>no holding period</b>, no bar on selling or "
    "renting afterward, no “principal residence” test, no limit of one "
    "dwelling per owner per period, no dollar cap, and <b>no affidavit</b>. "
    "Several states impose a one- or two-year not-for-sale window on their "
    "owner-builder exemptions. Wisconsin does not."))
flow.append(k.callout(
    "Where the “two years” you may have read comes from", [
        Paragraph("There <i>is</i> a two-year cycle in s. 101.654 — but it is "
                  "the continuing education a <b>certified contractor</b> must "
                  "complete: “<i>Completion every 2 years of at least 12 hours "
                  "of continuing education relevant to the professional area "
                  "of expertise of the person seeking to obtain a building "
                  "permit</i>” (s. 101.654(1m)(b)1.). That is a rule for "
                  "people who hold the credential, not a holding period for "
                  "people exempt from it. If a source tells you Wisconsin "
                  "makes an owner-builder keep the house for two years, it has "
                  "borrowed this number from the wrong subsection.",
                  S["body"]),
    ]))

flow += k.h2_tight("WHAT THE EXEMPTION LIFTS — AND WHAT IT LEAVES BEHIND")
rows = [
    [k.cellp("<b>Dwelling contractor certification</b> — the bond or liability "
             "policy, worker's comp and unemployment proof"),
     k.cellp("<b>LIFTED</b>", center=True),
     k.cellp("s. 101.654(1)(b); s. SPS 305.31(1)")],
    [k.cellp("<b>Dwelling contractor qualifier</b> — the 12-hour course and "
             "its continuing education"),
     k.cellp("<b>LIFTED</b>", center=True),
     k.cellp("The exception clause sits in the stem of s. SPS 305.31(1), so it "
             "reaches both par. (a) and par. (b)")],
    [k.cellp("<b>The building permit itself</b>"),
     k.cellp("<b>STILL REQUIRED</b>", center=True),
     k.cellp("s. SPS 320.08(1) — before any on-site construction, "
             "“including excavation for a structure”")],
    [k.cellp("<b>The code</b>"),
     k.cellp("<b>STILL APPLIES</b>", center=True),
     k.cellp("s. 101.66(1) names the owner personally")],
    [k.cellp("<b>Every inspection</b>"),
     k.cellp("<b>STILL REQUIRED</b>", center=True),
     k.cellp("s. SPS 320.10; see WI.3")],
    [k.cellp("<b>The cautionary statement</b>"),
     k.cellp("<b>YOU STILL SIGN IT</b>", center=True),
     k.cellp("s. 101.65(1r) reaches every owner who applies for a permit")],
    [k.cellp("<b>The county sanitary permit</b>, if you are not on a sewer"),
     k.cellp("<b>STILL REQUIRED — FIRST</b>", center=True),
     k.cellp("s. 145.195(1); s. SPS 320.09(9)(c)")],
]
flow.append(k.ref_table(
    "The exemption is a credential exemption and nothing more",
    [k.cellp("Requirement", bold=True), k.cellp("For an owner-builder",
                                                bold=True),
     k.cellp("Authority", bold=True)],
    rows, [CW - 3.3 * inch, 1.35 * inch, 1.95 * inch]))

flow.append(Spacer(1, 4))
flow.append(k.body(
    "One consequence is worth stating plainly, because it is the real cost of "
    "the exemption. A certified dwelling contractor has had to show the "
    "department either “<i>a bond … of not less than $5,000</i>” or "
    "“<i>a policy of general liability insurance … in the amount of at least "
    "$250,000 per occurrence</i>” (s. 101.654(2)(a)1. and 2.). When you take "
    "the exemption, <b>nothing stands behind your work but you</b>. That is "
    "the trade the statute is offering, and it is a reasonable one — but carry "
    "your own liability cover anyway."))
flow.append(k.closing_note(
    "Certification requirements: Wis. Stat. s. 101.654(1)(a), (1m), (2), "
    "(2m), (3); Wis. Admin. Code ss. SPS 305.31, 305.315. The exemption: "
    "s. 101.654(1)(b). Read at docs.legis.wisconsin.gov, September 2026."))

# ---------------------------------------------------------------- who inspects
flow += k.h2_tight("THERE IS NO PERMIT-FREE TOWN IN WISCONSIN")
flow.append(k.body(
    "If you have built in Montana, Kentucky or Mississippi, unlearn the "
    "instinct. Those states leave real gaps where no building official ever "
    "appears. <b>Wisconsin closes the gap by statute.</b>"))
flow.append(k.callout_long("The no-gap clause", [
    Paragraph("A city, village or town may take up enforcement by ordinance "
              "(s. 101.65(1)(a)). A municipality of <b>2,500 or fewer</b> "
              "people may instead pass a resolution asking the county to do it "
              "(s. 101.651(1) and (2m)(a)). And if it does neither: "
              "“<i><b>The department shall provide inspection services and "
              "shall enforce this subchapter throughout any municipality that "
              "does not exercise jurisdiction under sub. (2m) and that has not "
              "adopted a resolution under sub. (2m) (a).</b></i>” "
              "(s. 101.651(3)(b))", S["body"]),
    Paragraph("Larger municipalities that do not inspect are caught too — they "
              "“<i>shall contract with the department for those inspection "
              "services which the municipality does not perform</i>” "
              "(s. 101.65(2)). Between those two subsections, every parcel in "
              "Wisconsin has an enforcing authority.", S["body"]),
    Paragraph("<b>What this means on the ground.</b> In a "
              "department-jurisdiction municipality you do not go to a town "
              "hall. You obtain the permit from a <b>private registered UDC "
              "inspection agency</b>, and “<i>a person who obtains a Wisconsin "
              "uniform building permit from a registered UDC inspection agency "
              "shall retain the same agency to conduct the inspections</i>” "
              "(s. SPS 320.08(1) and (2)). You cannot change agencies "
              "mid-build, so choose deliberately.", S["body"]),
]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "There is one true carve-out from the code, and it is narrower than the "
    "folklore. A <b>primitive rural hunting cabin</b> is excluded from the "
    "definition of “dwelling” and a municipality “<i>may not exercise "
    "jurisdiction over</i>” one (ss. 101.61(1), 101.65(1g); "
    "s. SPS 320.05(12)). But read the definition before you rely on it."))
flow.append(k.callout(
    "The hunting-cabin exemption is grandfathered, not available", [
        Paragraph("“<i>‘Primitive rural hunting cabin’ means a structure that "
                  "satisfies <b>all</b> of the following: (a) The structure is "
                  "not used as a home or residence. (b) The structure is used "
                  "principally for recreational hunting activity. (c) The "
                  "structure does not exceed 2 stories in height. (d) The "
                  "structure satisfies any of the following: <b>1. The "
                  "structure was constructed before December 31, 1997.</b> "
                  "2. The structure results from alterations made to a "
                  "structure described in subd. 1. 3. The structure replaces a "
                  "structure described in subd. 1.</i>” "
                  "(Wis. Stat. s. 101.61(3))", S["body"]),
        Paragraph("Paragraph (d) is the whole story: the structure must trace "
                  "back to a building that existed before 1998. <b>You cannot "
                  "build a new one.</b> And paragraph (a) closes the other "
                  "door — the moment it is used as a home, it is not a hunting "
                  "cabin and the code applies.", S["body"]),
    ]))
flow.append(k.closing_note(
    "Enforcement: Wis. Stat. ss. 101.65(1)(a), (2), 101.651(1), (2m), (3)(b); "
    "Wis. Admin. Code ss. SPS 320.06(1), 320.08(1), (2). Hunting cabins: "
    "ss. 101.61(1), (3), 101.65(1g); s. SPS 320.05(12), created by CR 21-047, "
    "Register May 2022 No. 797, eff. 1 June 2022."))

# ---------------------------------------------------------------- trades
flow += k.h2_tight("THE FOUR TRADES ARE FOUR DIFFERENT RULES")
flow.append(k.body(
    "This is the section to read twice. Wisconsin writes a separate owner "
    "exemption for each trade, in four separate places, and <b>they are not "
    "worded the same way</b>. Two of them look forward to a house you will "
    "live in. Two of them are written in the present tense, and a house under "
    "construction has nobody living in it."))

rows = [
    [k.cellp("<b>Building / carpentry</b><br/>The dwelling contractor "
             "credential"),
     k.cellp("“an owner of a dwelling who <b>resides or will reside</b> in "
             "the dwelling”"),
     k.cellp("<b>Yes</b><br/>expressly", center=True),
     k.cellp("s. 101.654(1)(b)")],
    [k.cellp("<b>Heating, ventilating, air conditioning</b><br/>HVAC "
             "contractor registration"),
     k.cellp("“a dwelling owned by the person … and in which the person … "
             "<b>resides or will reside</b>”"),
     k.cellp("<b>Yes</b><br/>expressly", center=True),
     k.cellp("s. SPS 305.70(1)(b)2.")],
    [k.cellp("<b>Electrical</b><br/>Electrician license or registration"),
     k.cellp("“premises that the property owner <b>owns and occupies</b> as a "
             "residence”"),
     k.cellp("<b>Not on its<br/>face</b>", center=True),
     k.cellp("s. 101.862(4)(a)")],
    [k.cellp("<b>Plumbing</b><br/>Plumber license"),
     k.cellp("“in a <b>one-family building owned and occupied</b> by him or "
             "her as his or her home or farm building”"),
     k.cellp("<b>Not on its<br/>face</b>", center=True),
     k.cellp("s. 145.06(4)(a)")],
]
flow.append(k.ref_table(
    "The tense trap — the same idea written four different ways",
    [k.cellp("Trade", bold=True), k.cellp("The words the exemption uses",
                                          bold=True),
     k.cellp("Reaches a house<br/>nobody lives in yet?", bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.45 * inch, CW - 4.05 * inch, 1.15 * inch, 1.45 * inch]))
flow.append(k.cite(
    "Each of the four texts was read separately at its own source in September "
    "2026. The asymmetry is in the drafting, not in this summary: the "
    "legislature used forward-looking words in two places and present-tense "
    "words in the other two."))

flow.append(Spacer(1, 6))
flow.append(k.callout_long("What to do about the two present-tense trades", [
    Paragraph("Neither s. 101.862(4)(a) nor s. 145.06(4)(a) contains the "
              "phrase “new construction”. What they contain is the present "
              "tense — “owns <b>and occupies</b>”, “owned <b>and "
              "occupied</b>” — and a house you are still framing has no "
              "occupant. Anyone who tells you the answer is obviously yes, or "
              "obviously no, is reading past the words.", S["body"]),
    Paragraph("<b>On plumbing, however, the code settles the practical "
              "question from a completely different direction.</b> The permit "
              "itself has a field for it: “<i>the name and license number of "
              "the Wisconsin master plumber responsible for the installation "
              "of plumbing shall be entered on the permit by the issuing "
              "entity at the time of issuance</i>” (s. SPS 320.09(9)(a)7.). "
              "Whatever s. 145.06(4)(a) means, a Wisconsin master plumber's "
              "name goes on your building permit when it issues. Plan for a "
              "licensed plumber and ask your inspector how they handle the "
              "field.", S["body"]),
    Paragraph("<b>And note the plumbing exemption is narrower still.</b> It "
              "reaches a “<b>one-family</b> building”. The dwelling contractor "
              "exemption covers one- <i>and</i> two-family dwellings; the "
              "plumbing exemption does not. If you are building a duplex, the "
              "plumbing exemption is unavailable to you on its own terms.",
              S["body"]),
    Paragraph("<b>Both can also be switched off locally.</b> The electrical "
              "exemption applies “<i>unless a license or registration issued "
              "by the department is required by local ordinance</i>” and the "
              "plumbing one “<i>except where such license is required by local "
              "ordinance</i>”. Nothing lets a local ordinance <i>widen</i> "
              "either exemption — only narrow it. Ask.", S["body"]),
]))

flow += k.h2_tight("HEATING IS THE FRIENDLY TRADE — WITH ONE FEDERAL CATCH",
                   reserve=2.0)
flow.append(k.body(
    "HVAC is where Wisconsin is most generous, and the reasons are worth "
    "knowing. The mandatory state credential is a <b>registration</b>, not a "
    "license, and it carries no examination — s. 101.178(2) requires anyone "
    "“<i>engaged in the business of</i>” HVAC work to register, while the "
    "<b>examination-based certification is voluntary by the express words of "
    "the statute</b>: the department “<i>shall promulgate rules for a "
    "<b>voluntary</b> program</i>” (s. 101.178(3)(a))."))
flow.append(k.body(
    "The owner exemption then uses the good wording: no registration is needed "
    "“<i>to install or service heating, ventilating, air conditioning, or "
    "refrigeration equipment within a dwelling owned by the person … and in "
    "which the person … <b>resides or will reside</b></i>” "
    "(s. SPS 305.70(1)(b)2.). And the same rule adds that no HVAC registration "
    "is needed “<i>for electrical or plumbing work associated with the "
    "installation or servicing of the HVAC equipment</i>” "
    "(s. SPS 305.70(1)(b)3.) — though that lifts only the HVAC credential, not "
    "the electrical or plumbing ones."))
flow.append(k.callout(
    "The catch is federal, not Wisconsin", [
        Paragraph("Printed as a Note to s. SPS 305.70: “<i>Pursuant to federal "
                  "regulations individuals who install or service HVAC "
                  "equipment involving ozone-depleting refrigerants are "
                  "required to hold a Type I, II, III, or Universal technician "
                  "certification issued in accordance with section 608 of the "
                  "federal Clean Air Act and title 40 CFR part 82, subpart "
                  "F.</i>”", S["body"]),
        Paragraph("So: set your own furnace, run your own ductwork, and hang "
                  "your own line set — but the person who <b>charges the "
                  "refrigerant</b> on a split system or heat pump needs an EPA "
                  "608 card. A Wisconsin exemption is not a federal exemption. "
                  "Most owner-builders install everything and hire the "
                  "start-up.", S["body"]),
    ]))
flow.append(k.body(
    "One more oddity in your favor: HVAC is the <b>only</b> trade where "
    "Wisconsin pre-empts local licensing. “<i>A political subdivision may not "
    "require a person to obtain certification, licensure or other approval by "
    "the political subdivision in order to engage in the business of "
    "installing or servicing heating, ventilating or air conditioning "
    "equipment in the political subdivision unless the political subdivision "
    "required that approval before November 1, 1993</i>” (s. 101.178(3)(d)). "
    "Compare electrical and plumbing, where the state exemption is expressly "
    "<i>subject</i> to local ordinance. A permit is still required before "
    "installation begins (s. SPS 305.70(4))."))

flow += k.h2_tight("SEPTIC IS A HARD NO", reserve=2.0)
flow.append(k.body(
    "Of everything in this document, this is the one to accept rather than "
    "argue with. <b>A Wisconsin homeowner may not install their own private "
    "onsite wastewater treatment system.</b>"))
flow.append(k.body(
    "The reasoning runs through three provisions. First, POWTS work <i>is</i> "
    "plumbing by statutory definition — plumbing includes “<i>the "
    "construction, connection, installation, service, or repair of any drain "
    "or wastewater piping system … <b>including private on-site wastewater "
    "treatment systems</b></i>” (s. 145.01(10)(a)2.). Second, the homeowner "
    "plumbing exemption reaches work “<i>in a one-family <b>building</b></i>” "
    "— and a treatment tank and dispersal cell are not in the building. "
    "Third, and decisively, the sanitary permit application cannot be "
    "completed without naming somebody else: it must be accompanied by "
    "“<i>documentation that the master plumber or the master "
    "plumber-restricted service who is to be responsible for the "
    "installation</i>” (s. SPS 383.21(2)(c)4.), and that same person is the "
    "one who must call for the inspection and “<i>provide the necessary "
    "equipment and properly licensed personnel</i>” for it "
    "(s. SPS 383.26(2)(b), (d))."))
flow.append(k.body(
    "The compliant and completely ordinary path is to act as your own general "
    "contractor and hire a Master Plumber or Master Plumber-Restricted Service "
    "for the septic. Counties cannot add a license of their own on top: "
    "“<i>No city, village, town, town sanitary district, county … may require "
    "the licensing of any person licensed or registered under this "
    "chapter</i>” (s. 145.04(2))."))
flow.append(k.closing_note(
    "Trades: Wis. Stat. ss. 101.178(2), (3)(a), (3)(d), 101.862(1)-(4), "
    "145.01(10)(a)2., 145.04(2), 145.06(1), (2), (4); Wis. Admin. Code "
    "ss. SPS 305.70(1), (4), 320.09(9)(a)7., 383.21(2)(c)4., 383.26(2). "
    "Read at docs.legis.wisconsin.gov, September 2026."))

# ---------------------------------------------------------------- cautionary
flow += k.h2_tight("THE STATEMENT YOU WILL BE ASKED TO SIGN")
flow.append(k.body(
    "There is no owner-builder affidavit in Wisconsin. There <i>is</i> a "
    "mandatory signed statement, and it is about something else entirely — the "
    "people you hire. Your municipality has no discretion here; the statute "
    "says it “<i>shall require</i>” it of every owner who applies for a "
    "building permit."))
flow.append(k.callout_long("Wis. Stat. s. 101.65(1r), in full", [
    Paragraph("“<i>Shall require an owner who applies for a building permit to "
              "sign a statement advising the owner that if the owner hires a "
              "contractor to perform work under the building permit and the "
              "contractor is not bonded or insured as required under "
              "s. 101.654 (2) (a), the following consequences might "
              "occur:</i>”", S["body"]),
    Paragraph("“<i>(a) The owner may be held liable for any bodily injury to "
              "or death of others or for any damage to the property of others "
              "that arises out of the work performed under the building permit "
              "or that is caused by any negligence by the contractor that "
              "occurs in connection with the work performed under the building "
              "permit.</i>”", S["body"]),
    Paragraph("“<i>(b) The owner may not be able to collect from the "
              "contractor damages for any loss sustained by the owner because "
              "of a violation by the contractor of the one- and 2-family "
              "dwelling code or an ordinance enacted under sub. (1) (a), "
              "because of any bodily injury to or death of others or damage to "
              "the property of others that arises out of the work performed "
              "under the building permit or because of any bodily injury to or "
              "death of others or damage to the property of others that is "
              "caused by any negligence by the contractor that occurs in "
              "connection with the work performed under the building "
              "permit.</i>”", S["body"]),
    Paragraph("<b>Treat this as an instruction, not a formality.</b> It is the "
              "state telling you, in writing, that an uninsured "
              "subcontractor's negligence can land on you and that you may "
              "have no recovery against them. Before any sub starts, ask for "
              "their dwelling contractor certification and their certificate "
              "of insurance, and verify the credential yourself through the "
              "department's public license search.", S["body"]),
]))

# ---------------------------------------------------------------- hiring help
flow += k.h2_tight("IF YOU HIRE HELP, TWO NUMBERS DECIDE YOUR EXPOSURE")
flow.append(k.body(
    "Worker's compensation is where owner-builders most often discover they "
    "have become an employer without meaning to. Wisconsin sets two triggers, "
    "and they bite at different moments."))
rows = [
    [k.cellp("<b>Three or more employees</b>, at any time, in any trades or "
             "locations"),
     k.cellp("You become subject “<i>on the day on which the person employs 3 "
             "or more such employees</i>” — <b>immediately</b>")],
    [k.cellp("<b>Fewer than three</b>, but you have paid wages of <b>$500 or "
             "more in any calendar quarter</b>"),
     k.cellp("You become subject “<i>on the 10th day of the month next "
             "succeeding such quarter</i>” — a short grace period, then it "
             "attaches")],
]
flow.append(k.ref_table(
    "Wis. Stat. s. 101.654(2)(b) and the two triggers in s. 102.04(1)(b)",
    [k.cellp("Trigger", bold=True), k.cellp("When it attaches", bold=True)],
    rows, [CW * 0.46, CW * 0.54]))
flow.append(k.cite(
    "Wis. Stat. s. 102.04(1)(b)1. and 2. Farming has its own threshold at "
    "s. 102.04(1)(c) — six or more employees on any 20 days in a calendar "
    "year. If either trigger is met, s. 102.28(2)(a) requires you to insure. "
    "Whether a person building their own home is engaged in a “trade, "
    "business, profession or occupation” at all is a genuine question under "
    "s. 102.07(4)(a)2., and s. 102.07(4)(b) narrows the escape — confirm your "
    "position with the Department of Workforce Development before you hire, "
    "rather than assuming either answer."))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "The companion trap is that calling somebody a subcontractor does not make "
    "them one. Wisconsin's test has <b>nine conditions and every one must be "
    "met</b> — the statute says an independent contractor is not your employee "
    "only if they “<i>meet all of the following conditions</i>”."))
flow.append(k.checklist([
    "Maintains a separate business with his or her own office, equipment, "
    "materials and other facilities",
    "Holds or has applied for a federal employer identification number, or has "
    "filed business or self-employment income tax returns based on that work "
    "in the previous year",
    "Operates under contracts to perform specific services or work for "
    "specific amounts of money and under which the independent contractor "
    "controls the means of performing the work",
    "Incurs the main expenses related to the service or work performed under "
    "contract",
    "Is responsible for the satisfactory completion of the work and is liable "
    "for a failure to complete it",
    "Receives compensation on a commission or per job or competitive bid "
    "basis and not on any other basis",
    "May realize a profit or suffer a loss under contracts to perform the work",
    "Has continuing or recurring business liabilities or obligations",
    "The success or failure of the business depends on the relationship of "
    "business receipts to expenditures",
]))
flow.append(k.cite(
    "Wis. Stat. s. 102.07(8)(b)1. to 9., quoted in substance; read the full "
    "text before relying on it. Because the test is conjunctive, paying "
    "somebody by the hour, with your tools, on your schedule fails conditions "
    "1, 3, 4 and 6 at the same time — and a person who fails the test is your "
    "employee for worker's compensation purposes, whatever the paperwork says."))

# ---------------------------------------------------------------- lumber
flow += k.h2_tight("IF YOU ARE MILLING YOUR OWN LUMBER", reserve=2.0)
flow.append(k.body(
    "Wisconsin is one of the few states with an express route for ungraded "
    "dimension lumber in a house, and it is written for exactly the person "
    "reading this kit. Load-bearing dimension lumber normally has to be tested "
    "and approved — unless the lumber “<i>has been milled at the request of "
    "the person owning the lumber for use in the construction of the dwelling, "
    "and the dwelling will be inhabited by the person owning the lumber</i>”, "
    "or the miller “<i>sells the lumber directly to a person who will inhabit "
    "the dwelling</i>” (s. 101.66(1m)(a)1. and 2.)."))
flow.append(k.body(
    "Three conditions come with it. The lumber “<i>shall be milled so that it "
    "meets or exceeds the requirements of the one- and 2-family dwelling "
    "code</i>” and the miller must give you a <b>written certification</b> "
    "that it does (s. 101.66(1m)(b)). The miller must hold a current "
    "<b>certificate of accomplishment</b> from the lumber grading training "
    "program under s. 36.25(48), received “<i>within the 5 years before "
    "providing the written certification</i>”, with a copy attached "
    "(s. 101.66(1m)(bn)). And the inspector keeps the last word: they may "
    "“<i>authorize the use of the lumber, reject the use of the lumber, or "
    "authorize its use subject to more restrictive construction requirements, "
    "including requirements as to size, spacing, length of spans, and "
    "design</i>” (s. 101.66(1m)(c))."))
flow.append(k.callout(
    "Ask before you fell a tree", [
        Paragraph("The inspector's discretion under s. 101.66(1m)(c) is real "
                  "and it is exercised after the lumber exists. Take your "
                  "miller's certificate and your span table to the inspector "
                  "<b>before</b> the logging starts, and get the answer in "
                  "writing. A rejection at framing inspection is an expensive "
                  "way to learn that your spans needed to be shorter.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS BEFORE YOU START",
                   reserve=2.0)
flow.append(k.body(
    "Nothing here is filed with the state. It is the set of questions that "
    "decides whether the rest of this kit sequences correctly for your parcel."))
flow.append(k.checklist([
    "<b>I will reside in this dwelling.</b> That is the whole test in "
    "s. 101.654(1)(b), and “will reside” is enough — the house does not have "
    "to exist yet",
    "<b>I have identified which of the four enforcement models covers my "
    "parcel</b> — my municipality, a contracted agency, my county, or a "
    "private registered UDC inspection agency under state jurisdiction "
    "(WI.4 shows you how to find out)",
    "<b>If state jurisdiction applies, I have chosen my registered UDC "
    "inspection agency deliberately</b>, knowing I am locked to it for every "
    "inspection (s. SPS 320.08(2))",
    "<b>I know whether my parcel is sewered.</b> If it is not, the county "
    "sanitary permit comes before the building permit by statute",
    "<b>I have a Master Plumber or Master Plumber-Restricted Service lined up "
    "for the septic</b>, because I may not install it myself",
    "<b>I have asked my inspector, in writing, how they treat owner electrical "
    "and owner plumbing on new construction</b> — and I have their answer "
    "before I buy materials",
    "<b>I have checked whether a local ordinance requires a license anyway</b> "
    "for electrical or plumbing, which both state exemptions expressly allow",
    "<b>I understand I will sign the cautionary statement</b>, and I will "
    "verify each subcontractor's dwelling contractor certification and "
    "insurance before they start",
    "<b>I have counted my helpers against the worker's compensation "
    "triggers</b> — three employees at any time, or $500 in wages in a "
    "calendar quarter",
    "<b>I am carrying my own liability cover</b>, because the exemption means "
    "no bond and no $250,000 policy stands behind this build",
]))
flow.append(k.cite(
    "Nothing on this list is a Wisconsin filing requirement. It is a working "
    "checklist assembled from the provisions cited throughout this document."))

flow.append(Spacer(1, 4))
flow.append(k.ref_table(
    "Sources — every Wisconsin claim in this document (verified September 2026)",
    [k.cellp("What this document states", bold=True),
     k.cellp("Authority", bold=True)],
    [[k.cellp("No state builder license; the permit credential and its owner "
              "exemption"), k.cellp("Wis. Stat. s. 101.654(1)(a), (1)(b)")],
     [k.cellp("No holding period or resale restriction"),
      k.cellp("Negative finding — full text of s. 101.654, ss. SPS 305.31, "
              "305.315")],
     [k.cellp("Both dwelling contractor credentials fall away for the owner"),
      k.cellp("s. SPS 305.31(1) stem, and its Note")],
     [k.cellp("The code binds the owner personally"),
      k.cellp("Wis. Stat. s. 101.66(1)")],
     [k.cellp("Penalty: $25 to $500, each day a separate offense"),
      k.cellp("Wis. Stat. s. 101.66(3)")],
     [k.cellp("No permit-free town; the department is the residual enforcer"),
      k.cellp("Wis. Stat. ss. 101.65(2), 101.651(3)(b)")],
     [k.cellp("Permit before any excavation; same agency for inspections"),
      k.cellp("ss. SPS 320.08(1), 320.08(2)")],
     [k.cellp("Hunting cabin exemption is grandfathered to pre-1998"),
      k.cellp("Wis. Stat. s. 101.61(3)(d)")],
     [k.cellp("The four trade exemptions and their differing wording"),
      k.cellp("ss. 101.654(1)(b), 101.862(4)(a), 145.06(4)(a); "
              "s. SPS 305.70(1)(b)2.")],
     [k.cellp("Master plumber named on the permit at issuance"),
      k.cellp("s. SPS 320.09(9)(a)7.")],
     [k.cellp("Owner may not install a POWTS"),
      k.cellp("Wis. Stat. s. 145.01(10)(a)2.; ss. SPS 383.21(2)(c)4., "
              "383.26(2)(b), (d)")],
     [k.cellp("HVAC registration mandatory, certification voluntary, local "
              "licensing pre-empted"),
      k.cellp("Wis. Stat. s. 101.178(2), (3)(a), (3)(d)")],
     [k.cellp("EPA section 608 for refrigerant work"),
      k.cellp("Note to s. SPS 305.70")],
     [k.cellp("The cautionary statement"),
      k.cellp("Wis. Stat. s. 101.65(1r)")],
     [k.cellp("Worker's compensation triggers"),
      k.cellp("Wis. Stat. s. 102.04(1)(b); duty to insure s. 102.28(2)(a)")],
     [k.cellp("Nine-part independent contractor test, all required"),
      k.cellp("Wis. Stat. s. 102.07(8)(b)")],
     [k.cellp("Owner-milled lumber and the grading certificate"),
      k.cellp("Wis. Stat. s. 101.66(1m)(a), (b), (bn), (c)")]],
    [CW - 2.5 * inch, 2.5 * inch]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "wi-permit-kit",
                       "WI.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
