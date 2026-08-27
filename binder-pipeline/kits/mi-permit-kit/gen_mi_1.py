#!/usr/bin/env python3
"""MI.1 Owner-Builder Exemption Walkthrough.

Every Michigan claim in this document was read out of the primary source in
August 2026 and is cited on-page. Where the statute is silent or enforcing
agencies differ, the document says so and gives the verification step.

Verified sources:
  MCL 339.2401(a)(iii)  a person erecting for their OWN use and occupancy is
                        outside the definition of "residential builder"
  MCL 339.2403(b)       express exemption: owner of property, structure for
                        the owner's own use and occupancy
  MCL 339.2403(f)       the $600 aggregate-contract exemption + anti-splitting
  MCL 339.601(1),(4),(6) unlicensed practice; the residential-builder-specific
                        penalties that OVERRIDE the general $500/90-day one
  MCL 339.2412(1),(3),(4) no suit to collect, no lien, $5,000-$25,000 civil fine
  MCL 125.1510(1),(2),(3),(4) permit application; the verified affidavit is
                        about the PLANS; the written-instrument rule; the
                        8-point boldface section 23a warning
  MCL 125.1523a         conspiring to circumvent licensing = civil violation,
                        $100-$500
  MCL 339.2012(1)(c),(1)(d),(2)  architect/engineer seal exemptions and the
                        DEFINITION of "calculated floor area" (habitable only)
  MCL 339.5737(3)(g)    homeowner ELECTRICAL exemption (2016 PA 407). The old
                        MCL 338.883 was REPEALED eff. 4 Apr 2017 — do not cite
  MCL 339.5733(1),(2)   a qualifying local electrical ordinance displaces
                        article 7, and 737(3)(g) is NOT in the protected list
  MCL 339.6107(2)(d)    homeowner PLUMBING exemption — note there is NO
                        occupancy condition in the text; do not add one
  MCL 339.5819          homeowner MECHANICAL exemption — reaches only "a
                        heating or refrigerating system," and DOES require a
                        sworn affirmation of ownership/occupancy on the
                        permit application
  MCL 339.6125, 339.5811  local licensing barred for plumbing and mechanical
                        (the asymmetry with electrical is the trap)

Deliberately NOT claimed: that Michigan imposes a not-for-sale window, an
occupancy period, an owner-present-at-inspection rule, or a workers'
compensation proof requirement on an owner-builder. None appears in the
Occupational Code, Act 230, or 2016 PA 407 (all 154 sections searched).
Note the one real affidavit: MCL 339.5819 for mechanical. The BUILDING permit
affidavit under MCL 125.1510(1) is about the plans, not occupancy.
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

FORM_ID = "MI.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "Exemption & Qualification"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "How Michigan's owner-builder exemption actually works — the two statutes "
    "that create it, the three separate trade exemptions stacked on top of "
    "it, and the conditions that take them away.")

flow.append(k.disclaimer(
    "Statute text was read at legislature.mi.gov in August 2026; statutes "
    "change."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION")
flow.append(k.body(
    "Michigan requires a state <b>Residential Builder</b> license to build "
    "houses for other people. Building your own is not that. The Occupational "
    "Code excludes you twice over: you fall outside the <i>definition</i> of "
    "a residential builder in the first place, and there is a separate "
    "express exemption saying the licensing article does not apply to you. "
    "Neither one carries a dollar threshold, a square-footage limit, a "
    "holding period, or a state affidavit."))
flow.append(k.cite(
    "MCL 339.2401(a)(iii) and MCL 339.2403(b), Occupational Code, 1980 PA "
    "299, Article 24. Read at legislature.mi.gov, August 2026."))

rows = [
    [k.cellp("Is there a project-cost threshold?"),
     k.cellp("<b>No.</b> Michigan's license requirement is not keyed to "
             "project value the way many states' are. You may build a "
             "$1,000,000 house for yourself unlicensed")],
    [k.cellp("Must you own the land?"),
     k.cellp("Yes — the exemption is written for \"an owner of property,\" "
             "with reference to a structure <i>on the property</i>")],
    [k.cellp("Must you live in it?"),
     k.cellp("Yes — \"for the owner's own use <b>and</b> occupancy.\" Both "
             "words do work. A structure you will not occupy is not covered")],
    [k.cellp("For how long?"),
     k.cellp("<b>The statute sets no period.</b> There is no 12-month rule, "
             "no not-for-sale window, and no waiting period in Michigan law "
             "— see the section below before you rely on that")],
    [k.cellp("What do you sign?"),
     k.cellp("An affidavit verifying that your <i>plans and "
             "specifications</i> are true and complete — not an occupancy "
             "affidavit. (MCL 125.1510(1))")],
    [k.cellp("Can you do your own wiring, plumbing and HVAC?"),
     k.cellp("Yes — but under <b>three further exemptions</b>, each with its "
             "own test. Qualifying as an owner-builder does not qualify you "
             "for any of them")],
]
flow.append(k.ref_table(
    "The exemption at a glance",
    [k.cellp("Question", bold=True), k.cellp("Michigan's answer", bold=True)],
    rows, [2.7 * inch, CW - 2.7 * inch]))

# ---------------------------------------------------------------- the exemption
flow += k.h2_tight("THE EXEMPTION ITSELF — TWO STATUTES, NOT ONE")
flow.append(k.body(
    "Most guides quote one of these and miss the other. They do different "
    "jobs, and having both is why the Michigan owner-builder right is so "
    "hard to argue with."))

flow.append(k.callout("The two provisions — belt and braces", [
    Paragraph("<b>(1) You are not a residential builder to begin with.</b> "
              "The definition reaches \"<i>a person that erects a "
              "residential structure <b>except for the person's own use and "
              "occupancy on the person's property</b></i>.\" Build for "
              "yourself, on your own land, and the definition simply does "
              "not describe you. (MCL 339.2401(a)(iii))", S["body"]),
    Paragraph("<b>(2) And the article expressly does not apply to you.</b> "
              "\"<i>Notwithstanding article 6, a person may engage in the "
              "business of or act in the capacity of a residential builder "
              "… without a license under this article, if the person is … "
              "<b>an owner of property, with reference to a structure on the "
              "property for the owner's own use and occupancy</b></i>.\" "
              "(MCL 339.2403(b))", S["body"]),
]))
flow.append(Spacer(1, 8))
flow.append(k.body(
    "Read the operative words closely. <b>Owner of property</b> — the "
    "exemption belongs to the person who owns the land, so get the deed "
    "recorded in your name before you apply. <b>On the property</b> — it is "
    "the structure on land you own, not any structure anywhere. And <b>own "
    "use and occupancy</b> — a conjunction, not a synonym pair. A building "
    "you will use but not occupy, or own but not occupy, is outside it."))

flow.append(k.callout(
    "What Michigan does NOT impose — and what to do with that", [
        Paragraph("The Occupational Code sets <b>no holding period</b>, no "
                  "\"not offered for sale within X months\" clause, and no "
                  "presumption that you lacked intent if you move out. "
                  "Guides that print a one-year or two-year Michigan window "
                  "are importing another state's rule. Michigan's test is "
                  "your <b>intent at the time you build</b>: was this "
                  "structure for your own use and occupancy?", S["body"]),
        Paragraph("That cuts both ways: there is no safe-harbor date you can "
                  "wait out either. Sell a house you never meant to live in "
                  "and you needed the license at month zero — time does not "
                  "cure it. Build the home you actually mean to live in, keep "
                  "evidence that you meant it, and the absence of a deadline "
                  "works entirely in your favor.", S["body"]),
    ]))
flow.append(k.cite(
    "Verified by reading MCL 339.2401, 339.2403 and 339.2412 in full at "
    "legislature.mi.gov in August 2026. If a future amendment adds a period, "
    "it will appear in those sections."))

# ---------------------------------------------------------------- what you sign
flow += k.h2_tight("WHAT YOU ACTUALLY SIGN — MCL 125.1510")
flow.append(k.body(
    "The <b>building</b> permit application carries no homeowner affidavit. "
    "What the law requires is that every application — yours, a builder's, "
    "anyone's — carry \"<i>a detailed statement in writing, <b>verified by "
    "affidavit of the individual making it</b>, of the specifications for "
    "the building or structure, and full and complete copies of the plans "
    "drawn to scale</i>.\" You are swearing that your <b>drawings and "
    "specifications are accurate</b>, not that you promise to live there. "
    "Nothing in the Construction Code Act asks a homeowner to attest to "
    "occupancy or to not selling."))
flow.append(k.body(
    "<b>The mechanical permit is the exception, and it is statutory.</b> To "
    "install your own heating or refrigerating system you must, \"<i>in his "
    "or her application for a permit,</i>\" affirm \"<i>that he or she is or "
    "will become the owner and occupant of the dwelling</i>\" and that you "
    "will install the equipment yourself. That is a real occupancy "
    "attestation, on that one application, under MCL 339.5819 — see the "
    "trade section below."))
flow.append(k.body(
    "Separately, many enforcing agencies hand owner-builders their own local "
    "\"homeowner affidavit\" or \"homeowner permit\" form with additional "
    "promises on it. Those are <b>local instruments</b> adopted under MCL "
    "125.1508b(11), and they vary. Read whatever you are handed before you "
    "sign it, because its terms are not set by the State and are not "
    "reproduced anywhere in this kit."))

flow.append(k.callout(
    "The warning printed above your signature — and what it means for hiring",
    [
        Paragraph("Michigan requires this sentence on every building permit "
                  "application, in 8-point boldface, immediately above where "
                  "you sign: \"<i>Section 23a of the state construction code "
                  "act of 1972, 1972 PA 230, MCL 125.1523a, prohibits a "
                  "person from conspiring to circumvent the licensing "
                  "requirements of this state relating to persons who are to "
                  "perform work on a residential building or a residential "
                  "structure. Violators of section 23a are subjected to "
                  "civil fines.</i>\" (MCL 125.1510(4))", S["body"]),
        Paragraph("That is the provision behind the rule you will hear at "
                  "the counter as \"<b>a licensed contractor may not work "
                  "under your homeowner permit.</b>\" The mechanism is in "
                  "MCL 125.1510(2)–(3): a person is not recognized as your "
                  "builder or agent unless a written contract, power of "
                  "attorney or letter of authorization is <b>filed with the "
                  "enforcing agency</b> setting out their license number and "
                  "expiry; and anyone licensed — or required to be licensed "
                  "— who applies for a permit for residential work must give "
                  "their license number, workers' compensation carrier, "
                  "employer identification number and unemployment agency "
                  "number on the application.", S["body"]),
        Paragraph("So the honest version is not \"you may never hire "
                  "anyone.\" It is: <b>the person who does the work is "
                  "supposed to be the person on the permit.</b> The Bureau "
                  "states it plainly for the mechanical trade — \"<i>a "
                  "homeowner must secure a permit for work they are "
                  "performing at their residence, and mechanical contractors "
                  "are responsible for permits on work they are performing "
                  "on behalf of an owner</i>\" — and the same logic runs "
                  "through all four disciplines. Pull your own permits for "
                  "the work you genuinely do yourself, and have each "
                  "licensed contractor you hire pull their own under their "
                  "own license. Using your homeowner permit as a wrapper so "
                  "an unlicensed crew can work under it is precisely what "
                  "section 23a names.", S["body"]),
    ]))
flow.append(k.cite(
    "MCL 125.1510(1), (2), (3), (4) and MCL 125.1523a, Stille-DeRossett-Hale "
    "Single State Construction Code Act, 1972 PA 230. The boldface warning "
    "above is reproduced verbatim on the Bureau of Construction Codes' own "
    "Building Permit Application, form BCC-324 (04/2024), page 4."))

# ---------------------------------------------------------------- trade work
flow += k.h2_tight("DOING YOUR OWN ELECTRICAL, PLUMBING, AND MECHANICAL WORK")
flow.append(k.body(
    "This is where Michigan is genuinely better than most licensing states — "
    "and where owner-builders get sloppy. The builder exemption and the "
    "three trade exemptions are <b>four different rules</b>. Qualifying for "
    "one does not qualify you for the others, and the trade exemptions are "
    "narrower than the builder one in ways that matter."))

trade_rows = [
    [k.cellp("<b>Electrical</b>"),
     k.cellp("No license for \"<i>any installation, alteration, or repair of "
             "electrical equipment by a homeowner in a <b>single family home "
             "and accompanying outbuildings</b> owned and occupied<b>, or to "
             "be occupied</b>, by <b>the individual who is performing</b></i>\" "
             "the work. The widest of the three — and \"or to be occupied\" "
             "expressly covers a house you have not moved into yet."),
     k.cellp("MCL 339.5737(3)(g)")],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp("A license is not required for \"<i>the installation by a "
             "homeowner of <b>his or her own plumbing, building sewer, or "
             "private sewer</b> in his or her single-family dwelling <b>if a "
             "permit is secured</b></i>.\" Note what is <i>absent</i>: no "
             "occupancy condition at all. The permit is written into the "
             "exemption itself."),
     k.cellp("MCL 339.6107(2)(d)")],
    [k.cellp("<b>Mechanical</b>"),
     k.cellp("Much narrower than assumed — only \"<i>a <b>heating or "
             "refrigerating system</b></i>,\" not mechanical work generally. "
             "Own and occupy (or be about to), install it <b>personally</b>, "
             "<b>affirm both on the permit application</b>, and get an "
             "inspection once it is running. Refrigerant is separately "
             "<b>federal</b>: EPA Section 608 to open a circuit."),
     k.cellp("MCL 339.5819; 40 C.F.R. 82-F")],
]
flow.append(k.ref_table(
    "Trade by trade — what each statute actually says",
    [k.cellp("Trade", bold=True), k.cellp("What the exemption requires", bold=True),
     k.cellp("Authority", bold=True)],
    # 0.95in split "Mechanical" mid-word at 9.5pt bold.
    trade_rows, [1.15 * inch, CW - 1.15 * inch - 1.4 * inch, 1.4 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>Do not flatten these into one rule.</b> They differ on <b>scope</b> "
    "(mechanical reaches only a heating or refrigerating system), on "
    "<b>occupancy</b> (electrical and mechanical require it, plumbing does "
    "not mention it), and on <b>paperwork</b> (only mechanical demands a "
    "sworn affirmation). All three run to <b>the individual doing the "
    "work</b>, and all three exempt you from the <b>license</b> only — never "
    "from the permit."))

flow.append(k.callout(
    "The trap: your electrical exemption can be switched off locally", [
        Paragraph("The three trade exemptions are not equally durable, and "
                  "no competing Michigan guide says so. Article 7 "
                  "\"<i>does not apply in the jurisdiction of a municipality "
                  "that adopts or has adopted an ordinance</i>\" meeting four "
                  "tests — standards at least as stringent, substantially "
                  "similar enforcement, comparable penalties, and inspection "
                  "of electrical wiring. (MCL 339.5733(1))", S["body"]),
        Paragraph("The statute then lists the classes such an ordinance may "
                  "<i>not</i> require a license for — section 737(3)<b>(c), "
                  "(d), (e), or (f)</b>. The homeowner exemption is "
                  "<b>737(3)(g)</b>, conspicuously absent from that protected "
                  "list. So a municipality running its own qualifying "
                  "electrical ordinance can lawfully require a licensed "
                  "electrician even on your own home. Plumbing and mechanical "
                  "are the opposite — local licensing is barred outright "
                  "(MCL 339.6125(1); MCL 339.5811). <b>Ask before you buy "
                  "wire.</b>", S["body"]),
    ]))

flow.append(k.callout("A permit is still required for every trade", [
    Paragraph("Being exempt from a <b>license</b> is not being exempt from a "
              "<b>permit</b>. Michigan requires separate permits for "
              "building, electrical, mechanical and plumbing work, and the "
              "Bureau states the rule for each trade flatly: electrical — "
              "\"<i>a person shall not equip a building with electrical "
              "conductors or equipment … without receiving a permit</i>\"; "
              "plumbing — \"<i>plumbing work shall not be started until a "
              "permit for such work has been issued</i>\"; mechanical — "
              "\"<i>except for replacement of minor parts, mechanical work "
              "shall not be started until a permit for such work has been "
              "issued</i>.\" Doing your own work without pulling those "
              "permits is the single most expensive mistake in this kit, "
              "because the remedy is opening up finished work.", S["body"]),
    Paragraph("And in Michigan there is a second sting: those four permits "
              "may not all come from the same office. See <b>MI.4</b>.",
              S["body"]),
]))
flow.append(k.cite(
    "All three exemptions are quoted from the <b>skilled trades regulation "
    "act, 2016 PA 407</b>: electrical, MCL 339.5737(3)(g), with the permit "
    "requirement at MCL 339.5731(1) and the local-ordinance override at "
    "MCL 339.5733; plumbing, MCL 339.6107(2)(d), with MCL 339.6125(2) "
    "authorizing the homeowner to hold the permit and MCL 339.6125(1) "
    "barring local licensing; mechanical, MCL 339.5819, with MCL 339.5811 "
    "barring local licensing. <b>Watch the citation you are given "
    "elsewhere:</b> the old Electrical Administrative Act (MCL 338.881–"
    "338.892), the State Plumbing Act (MCL 338.3511–338.3569) and the Forbes "
    "Mechanical Contractors Act (MCL 338.971–338.988) were all <b>repealed "
    "effective April 4, 2017</b> by that same act. Guides still citing "
    "MCL 338.883 for the homeowner electrical exemption are quoting dead "
    "law. Verified August 2026."))

# ---------------------------------------------------------------- small jobs
flow += k.h2_tight("THE $600 RULE — AND WHY IT IS NOT YOUR EXEMPTION")
flow.append(k.body(
    "Michigan also exempts work \"<i>if the aggregate contract price … is "
    "less than $600.00</i>,\" and you will see this quoted as though it were "
    "a threshold below which anyone may work on your house. Read the second "
    "sentence: it \"<i>does not apply if the work of a construction is only "
    "a part of a larger or major operation … or in which a division of the "
    "operation is made in contracts of amounts less than $600.00, <b>to "
    "evade this act</b></i>.\" You cannot slice a house into $599 pieces. "
    "Your exemption is MCL 339.2403(b); do not rely on this one. "
    "(MCL 339.2403(f))"))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS BEFORE YOU APPLY")
flow.append(k.body(
    "Every line below is a condition Michigan law imposes or a fact the "
    "permit counter will ask you to prove. Work down it with a pen. If you "
    "cannot check a box, resolve it before you file — not after."))

flow += k.check_table("Step 1 — Ownership and intent", [
    ("Land is recorded in your name as of the permit application date — the "
     "exemption belongs to \"an owner of property\"",
     [("Deed/liber-page:", 0.55), ("Parcel ID:", 0.45)]),
    "You intend the finished structure for your <b>own use and occupancy</b> "
    "— not as a rental, spec house, flip, or a building you will use but not "
    "live in",
    "You can show what you intended if asked: a construction loan in your "
    "name, a homestead/principal-residence exemption filing, an address "
    "change, a signed contract to sell your current home",
    "No purchase, lease, or listing agreement for the property exists or is "
    "contemplated",
    ("If your plan involves selling or renting the finished house at all, "
     "you have the enforcing agency's written position before applying",
     [("Date requested:", 0.5), ("Response:", 0.5)]),
], notes_header="Notes / evidence")

flow += k.check_table("Step 2 — The four exemptions you are relying on", [
    "<b>Builder:</b> confirmed you meet MCL 339.2403(b) — owner of the "
    "property, structure for your own use and occupancy",
    "<b>Electrical:</b> single-family home (plus outbuildings), you own it "
    "and occupy or will occupy it, and <b>you personally</b> will do the "
    "wiring",
    "<b>Electrical, local override:</b> asked your municipality whether it "
    "runs its own electrical ordinance under MCL 339.5733 — if it does, your "
    "homeowner exemption may not apply there",
    "<b>Plumbing:</b> you will install your own plumbing, building sewer, or "
    "private sewer in your single-family dwelling, and a permit is secured",
    "<b>Mechanical:</b> it is a <b>heating or refrigerating system</b>, you "
    "own and will occupy the dwelling, you will install it personally, and "
    "you are ready to affirm both on the permit application",
    "<b>Mechanical, federal:</b> you hold EPA Section 608 certification if "
    "you will open a refrigerant circuit",
    "For any trade you will <b>not</b> do yourself, the licensed contractor "
    "you hire will pull that permit under their own license",
    ("Each contractor's license verified with LARA before they start",
     [("Verified on:", 1.0)]),
], notes_header="Notes / evidence")

flow.append(k.body(
    "<b>Step 3 — the paperwork itself</b> (the four permit applications, the "
    "five environmental approvals, plan sets, and everything your enforcing "
    "agency adds on top) is worked in <b>MI.2 Permit Application "
    "Checklist</b>, and each document is described in <b>MI.5 Forms &amp; "
    "Documents Index</b>."))

# ---------------------------------------------------------------- losing it
flow += k.h2_tight("WHAT TAKES THE EXEMPTION AWAY — AND WHAT IT COSTS")
flow.append(k.bullet(
    "<b>Building something you never intended to occupy</b> — a spec house, "
    "a rental, an investment flip. This is the whole test."))
flow.append(k.bullet(
    "<b>Not owning the land</b> the structure sits on."))
flow.append(k.bullet(
    "<b>Letting an unlicensed person work under your permit</b> — the "
    "section 23a conspiracy provision."))
flow.append(k.bullet(
    "<b>Doing a trade yourself when the trade exemption does not fit</b> — "
    "for example wiring a duplex, or having someone else do the wiring on "
    "your homeowner electrical permit."))
flow.append(Spacer(1, 4))
flow.append(k.body(
    "The consequences Michigan law actually names, in ascending order. "
    "<b>Conspiring to circumvent licensing</b> is a civil violation carrying "
    "a fine of \"<i>not less than $100.00 or more than $500.00</i>,\" "
    "enforceable by the county prosecutor or the Attorney General "
    "(MCL 125.1523a). An unlicensed residential builder <b>cannot sue to "
    "collect</b> — no action \"<i>for the collection of compensation for the "
    "performance of an act or contract for which a license is required</i>\" "
    "without alleging and proving licensure — and <b>cannot record a "
    "construction lien</b> (MCL 339.2412(1), (3))."))

flow.append(k.callout(
    "The penalty figure nearly every Michigan summary gets wrong", [
        Paragraph("You will read that unlicensed residential building in "
                  "Michigan is a misdemeanor carrying \"up to $500 or 90 "
                  "days.\" Those are the numbers in MCL 339.601(4) — the "
                  "<b>general</b> penalty for practicing any occupation the "
                  "Occupational Code regulates.", S["body"]),
        Paragraph("Residential builders were carved out of it. MCL "
                  "339.601(6) begins \"<i><b>Notwithstanding subsections (4) "
                  "and (5)</b></i>\" and sets its own scale: a first offense "
                  "is a misdemeanor punishable by a fine of \"<i>not less "
                  "than $5,000.00 or more than $25,000.00, or imprisonment "
                  "for not more than 1 year, or both</i>\"; a second offense "
                  "raises the prison term to two years; and an offense "
                  "\"<i>that causes death or serious injury</i>\" is a "
                  "<b>felony</b> with up to four years. A separate civil "
                  "action by a prosecutor or the Attorney General carries "
                  "$5,000 to $25,000 on top (MCL 339.2412(4)).", S["body"]),
        Paragraph("None of this touches a genuine owner-builder — you are "
                  "exempt, so there is no offense. It matters because it "
                  "shows how seriously Michigan treats the line.", S["body"]),
    ]))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("The exemption twice over: a person erecting for their own use and "
     "occupancy on their own property is outside the definition, and is "
     "also expressly exempted",
     "MCL 339.2401(a)(iii); 339.2403(b)"),
    ("No project-cost threshold, holding period or not-for-sale window in "
     "the article; the $600 exemption is for small standalone jobs and "
     "cannot be split to evade the act",
     "MCL 339.2401–2412; 339.2403(f)"),
    ("The affidavit verifies the plans and specifications; an agent or "
     "builder is not recognized without a filed written instrument; licensed "
     "residential applicants must give license, workers' comp, EIN and UIA "
     "numbers", "MCL 125.1510(1)–(3)"),
    ("The 8-point boldface section 23a warning above the signature, and the "
     "civil violation it names: $100–$500",
     "MCL 125.1510(4); 125.1523a"),
    ("Unlicensed residential building: $5,000–$25,000 and up to 1 year "
     "(first offense), felony if death or serious injury results — not the "
     "general $500 / 90-day penalty", "MCL 339.601(4), (6)"),
    ("Unlicensed builder cannot sue to collect and cannot lien; prosecutor "
     "or Attorney General may seek $5,000–$25,000",
     "MCL 339.2412(1), (3), (4)"),
    ("Homeowner electrical exemption — and that a qualifying local ordinance "
     "can switch it off. The old MCL 338.883 was repealed effective April 4, "
     "2017", "MCL 339.5737(3)(g); 339.5733"),
    ("Homeowner plumbing exemption — no occupancy condition — and mechanical, "
     "heating or refrigerating system only, with a sworn affirmation on the "
     "application; local licensing barred for both",
     "MCL 339.6107(2)(d); 339.5819"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "mi-permit-kit",
                       "MI.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
