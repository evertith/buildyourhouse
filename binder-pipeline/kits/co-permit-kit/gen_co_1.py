#!/usr/bin/env python3
"""CO.1 The Owner-Builder's Legal Position in Colorado.

Every Colorado claim in this document was read out of the official Colorado
Revised Statutes 2026 PDFs published by the Office of Legislative Legal
Services (olls.info/crs, linked from leg.colorado.gov) in August 2026, and is
cited on-page. Where the statute is silent or jurisdictions differ, the
document says so and gives the verification step.

Verified sources:
  30-28-201(1)          county commissioners "authorized to" adopt a building
                        code; agricultural shelter may be excepted
  30-28-205(1)          "After the adoption of the building code" a permit is
                        required — the duty is contingent on adoption
  30-28-205(3)          plans must bear an architect's or engineer's seal
                        unless exempted by 12-120-403
  31-15-601             municipal building and fire regulation powers
  12-120-403(1)(a)      one- to four-family dwellings exempt from the
                        architect-licensing requirement — draw your own plans
  12-115-109(1)         electrician license required
  12-115-116(2)         homeowner electrical exemption, VERBATIM — conditioned
                        on the work being inspected. THE KIT'S HEADLINE TRAP
  12-115-116(4)         the broader sale/lease/rental exclusion
  12-115-116(6)(a),(c)  maintenance/repair of existing facilities: no license,
                        no inspection, no fee — and what the term means
  12-115-120(1)(a)(I)   state permit unless a qualifying local building dept
  12-115-120(1)(b),(c)  utility may not serve without proof of final approval
  12-115-120(2)(a),(b)  new construction inspected by a state inspector;
                        permit BEFORE work begins; 3-working-day inspection
  12-115-120(6)         permits valid 12 months; up to 3 years if shown at
                        application; 6-month extension
  12-115-120(8)         a local government may start/stop its program only as
                        of July 1, with notice by October 1 prior
  12-115-120(11)(c)     "qualified applicant" includes a homeowner working on
                        the homeowner's home
  12-115-107(2)(a)(I)   board adopts NEC by rule; locals may be more stringent
  12-115-121(2)(a)      local electrical inspection fee cap mechanism
  12-155-118(2)         homeowner plumbing exemption, VERBATIM — no inspection
                        condition; exclusion reaches "licensing" only
  12-155-120(1)(a)      state plumbing AND GAS PIPING permit; different
                        carve-out test from electrical
  12-155-120(1)(c)(I)   permit before work; (11)(c) homeowner qualified
  12-155-103(2)         "gas piping" defined
  12-155-106(1),(2),(5) Colorado plumbing code is a statewide minimum; locals
                        may amend upward; Colorado fuel gas code
  12-20-407(1)(a)       unlicensed electrical or plumbing practice is a
                        class 2 misdemeanor

Still deliberately hedged: the adopted NEC and Colorado plumbing code editions
(board rule, not statute — the kit reads 3 CCR 710-1 and
3 CCR 720-1 for the adopted editions); the absence of a state
GC or HVAC license, printed as an as-of-2026 absence; and every jurisdiction's
owner-builder permit policy, which the buyer confirms in writing.
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

FORM_ID = "CO.1"
FORM_TITLE = "The Owner-Builder's Legal Position in Colorado"
TOPIC = "Legal Position"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What Colorado actually requires of a person building their own house — "
    "the licenses that do not exist, the two state trade permits that do, and "
    "the one condition hidden inside the homeowner electrical exemption.")

flow.append(k.disclaimer(
    "Statute text was read from the official Colorado Revised Statutes 2026 "
    "at leg.colorado.gov in August 2026; statutes change."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION")
flow.append(k.body(
    "Colorado has <b>no statewide general contractor license</b> and <b>no "
    "statewide residential building code</b>. You do not apply to the State "
    "for permission to build your own house — there is no state affidavit, "
    "no exemption to claim, no board that reviews you. Whether a building "
    "permit exists at all is a decision your county or city made, or never "
    "made. <b>But two things are statewide, and they are the two things "
    "owner-builders most want to do themselves:</b> electrical work and "
    "plumbing work each require a state license, each carries a homeowner "
    "exemption — and <b>each installation requires a permit and an "
    "inspection regardless of who does the work</b>. Where your local "
    "government does not run its own qualifying program, that permit comes "
    "from a state board and a state inspector drives out to your site."))
flow.append(k.cite(
    "Absence of a state GC license: Title 12 of the Colorado Revised "
    "Statutes 2026 licenses electricians (article 115) and plumbers (article "
    "155) but contains no general-contractor, home-builder, or "
    "residential-construction article — checked August 2026. Building code "
    "adoption: C.R.S. 30-28-201(1), 30-28-205(1); 31-15-601."))

# ---------------------------------------------------------------- the absence
flow += k.h2_tight("THE ABSENCE — AND ITS EXACT SHAPE")
flow.append(k.body(
    "Two absences, and they are not the same absence. <b>No state contractor "
    "license:</b> Title 12 of the Colorado Revised Statutes — the "
    "professions and occupations title — licenses electricians and plumbers "
    "and says nothing about general contractors or home builders. "
    "<b>No statewide residential building code:</b> the county statute is "
    "permissive, not mandatory. \"<i>A board of county commissioners is "
    "authorized to adopt ordinances and a building code … in all or part of "
    "the county, and not embraced within the limits of any incorporated city "
    "or town</i>\" (30-28-201(1)) — and the enforcement section makes the "
    "permit duty conditional: \"<i>After the adoption of the building code, "
    "it shall be unlawful to erect, construct, reconstruct, alter, or remodel "
    "any structure, dwelling, or building in the designated area … without "
    "first obtaining a building permit from the county building "
    "inspector</i>\" (30-28-205(1)). No adoption, no permit requirement."))
flow.append(k.body(
    "Municipalities get their powers from 31-15-601, and home-rule cities "
    "under article XX of the Colorado Constitution set their own. The "
    "practical result is what makes Colorado different from almost every "
    "other state: <b>your neighbor across a county line may be under a "
    "completely different code — or under none.</b>"))

flow.append(k.callout("Print-date warning — say it the careful way", [
    Paragraph("The accurate sentences are: \"<b>As of August 2026 no "
              "Colorado state agency issues a general contractor or home "
              "builder license</b>,\" and \"<b>Colorado adopts no statewide "
              "residential building code.</b>\" Neither means \"no rules\" "
              "or \"no permits\" — two trades are licensed statewide and "
              "their permits are required statewide. Nor are these timeless: "
              "legislatures create licenses, and Colorado has legislated "
              "repeatedly here since 2022. Verify at leg.colorado.gov.",
              S["body"]),
]))
flow.append(k.cite(
    "C.R.S. 30-28-201(1), 30-28-205(1), 31-15-601; Colo. Const. art. XX. "
    "Absence of a GC or HVAC licensing article verified by reading the "
    "article list of Title 12, Colorado Revised Statutes 2026, August 2026. "
    "One statutory exception worth knowing: county building codes may except "
    "\"<i>buildings or structures used for the sole purpose of providing "
    "shelter for agricultural implements, farm products, livestock, or "
    "poultry</i>\" (30-28-201(1), 30-28-205(1)) — a barn is not a house."))

# ---------------------------------------------------------------- electrical
flow += k.h2_tight("ELECTRICAL — C.R.S. ARTICLE 115 (STATE ELECTRICAL BOARD)")
flow.append(k.body(
    "The licensing rule is flat (12-115-109(1)). The homeowner carve-out is "
    "in 12-115-116(2), and the whole document turns on reading it slowly:"))
flow.append(Paragraph("C.R.S. 12-115-116(2), in full", S["h3"]))
flow.append(k.body(
    "\"<i>Nothing in this article 115 shall be construed to require any "
    "individual to hold a license before doing electrical work on his or her "
    "own property or residence <b>if all such electrical work, except for "
    "maintenance or repair of existing facilities, is inspected as provided "
    "in this article 115</b>; if, however, the property or residence is "
    "intended for sale or resale by a person engaged in the business of "
    "constructing or remodeling the facilities or structures or is rental "
    "property that is occupied or is to be occupied by tenants for lodging, "
    "either transient or permanent, or is generally open to the public, the "
    "owner shall be responsible for, and the property shall be subject to, "
    "all of the provisions of this article 115 pertaining to inspection and "
    "licensing, unless specifically exempted therein.</i>\""))
flow.append(Spacer(1, 6))

flow.append(k.callout(
    "THE TRAP — the exemption is conditioned on the inspection", [
        Paragraph("The load-bearing word is <b>\"if\"</b>. Colorado does not "
                  "give a homeowner an unconditional right to do their own "
                  "wiring; it gives a right that exists <b>only if all the "
                  "work is inspected</b>. Skip the permit and the "
                  "inspection and you have not merely missed an inspection "
                  "— <b>the exemption you were relying on never applied to "
                  "the work</b>, which leaves unlicensed electrical work "
                  "behind your drywall. Practicing the profession of an "
                  "electrician without an active license is a <b>class 2 "
                  "misdemeanor</b> (12-115-123; 12-20-407(1)(a)(V)(B)).",
                  S["body"]),
    ]))
flow.append(Spacer(1, 4))
flow.append(k.body(
    "Compare the plumbing exemption three articles later, below: it contains "
    "no inspection condition at all. Two near-identical sentences in the same "
    "title, and only one of them puts your license exemption at risk if you "
    "skip an inspection. This asymmetry appears in no general owner-builder "
    "guide we have seen — and it is the single most important sentence in "
    "this kit."))
flow.append(Spacer(1, 6))

flow.append(Paragraph("What takes the exemption away entirely", S["h3"]))
flow.append(k.body(
    "Two exclusions, the second broader. Under 12-115-116(2) the exemption is "
    "lost if the property is \"<i>intended for sale or resale by a person "
    "engaged in the business of constructing or remodeling</i>,\" is rental "
    "property occupied or to be occupied by tenants, or is open to the "
    "public. Under 12-115-116(4) — no \"in the business\" qualifier — "
    "property \"<i>developed for sale, lease, or rental</i>\" is subject to "
    "the whole article. <b>Read together, the safe rule is: build it to live "
    "in, not to sell or rent.</b>"))
flow.append(k.body(
    "What the exemption does <b>not</b> require is worth saying too: the "
    "statute says \"<i>his or her own property or residence</i>.\" There is "
    "<b>no occupancy condition</b> in the text — no requirement that you "
    "already live there, which would be impossible for a house under "
    "construction. Guides that print \"a home you own and live in\" are "
    "adding words the statute does not contain. Your local building "
    "department may impose its own occupancy condition on the building "
    "permit; that is a separate, local question. And one genuine free pass: "
    "\"<i>maintenance or repair of existing facilities</i>\" on your own "
    "property needs no license, no board inspection, and no fee "
    "(12-115-116(6)(a)) — defined narrowly as replacing components \"<i>with "
    "new components that serve the same purpose</i>\" (12-115-116(6)(c)). "
    "Building a new house is not maintenance or repair."))

flow.append(Paragraph("The permit: who issues it, and when you buy it",
                      S["h3"]))
flow.append(k.body(
    "\"<i>An individual required to have electrical inspection under this "
    "article 115 shall apply to the board for an electrical permit … "
    "<b>except where an incorporated town or city, county, city and county, "
    "or qualified state institution of higher education has a building "
    "department that meets the minimum standards of this article 115 and "
    "that processes applications for building permits and inspections, in "
    "which case the individual shall apply to the building department</b></i>"
    "\" (12-115-120(1)(a)(I)). For new construction, the owner \"<i>shall "
    "have the electrical portion of the installation … inspected by a state "
    "electrical inspector</i>\" except in a jurisdiction \"<i>having its own "
    "electrical code and inspection program equal to the minimum standards</i>"
    "\" of the article (12-115-120(2)(a)). Timing is not negotiable: "
    "\"<i>Prior to the commencement of any electrical installation, the "
    "person making the installation, who must be a qualified applicant, "
    "shall apply for a permit and pay the required permit fee</i>\" "
    "(12-115-120(2)(b)). The state inspector must inspect within "
    "<b>three working days</b> of receiving the inspection application."))
flow.append(k.body(
    "And you may buy it yourself: \"<i>qualified applicant</i>\" expressly "
    "includes \"<b><i>a homeowner performing work on the homeowner's "
    "home</i></b>\" (12-115-120(11)(c)), added in 2022 and effective "
    "January 1, 2023. Applying when you are <b>not</b> a qualified applicant "
    "is itself a violation (12-115-122(1)(q)), so a friend or an "
    "unregistered helper cannot pull it for you."))

flow.append(k.callout("The enforcement mechanism nobody expects — your meter",
                      [
    Paragraph("Colorado does not chase you; it waits at the meter. On final "
              "inspection and approval the board notifies the utility, and "
              "\"<b><i>A utility shall not provide service to any person "
              "required to have electrical inspection under this article 115 "
              "without proof of final approval</i></b>\" (12-115-120(1)(b), "
              "(c)). The only exceptions are situations the board or local "
              "authority declares an emergency, for a maximum of seven days, "
              "and approved tiny-home connections. However quiet your county "
              "is about building permits, <b>an unapproved house does not "
              "get permanent power</b>.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>Permits expire.</b> Board permits run twelve months; the board may "
    "issue one for up to three years if you demonstrate <b>at the time of "
    "application</b> that the work is substantial, or extend six months for "
    "extenuating circumstances notified before expiry (12-115-120(6)(a)). "
    "Ask for the long permit when you apply — an owner-build routinely "
    "outruns twelve months, and once a permit expires you must buy a new one "
    "before any inspection can happen (12-115-120(6)(b))."))
flow.append(k.body(
    "<b>The code is a floor, not a ceiling — and it just moved.</b> The "
    "board adopts electrical standards by rule, \"<i>governed when "
    "appropriate by the standards in the most current edition of the "
    "national electrical code</i>\" (12-115-107(2)(a)(I)), so the adopted "
    "edition lives in board rule, not in the statute. As of this printing "
    "the rule incorporates \"<i>the National Fire Protection Association "
    "standard number 70, hereafter known as the National Electrical Code, "
    "<b>2026 Edition</b></i>,\" and states \"<i>The effective date shall be "
    "<b>August 1, 2026</b></i>\" (3 CCR 710-1, Rule 1.5(A)). If you are "
    "reading a guide, a course, or an inspector's handout written before "
    "mid-2026, it is on the previous edition. The same statute preserves "
    "local authority to enforce standards \"<i>more stringent than the "
    "minimum standards adopted by the board</i>,\" so confirm both: the "
    "board's current rule, and your jurisdiction's amendments."))
flow.append(k.cite(
    "C.R.S. 12-115-109(1), 12-115-116(2), (4), (6)(a), (6)(c), "
    "12-115-120(1)(a)(I), (1)(b), (1)(c), (2)(a), (2)(b), (6), (11)(c), "
    "12-115-122(1)(q), 12-115-123, 12-115-107(2)(a)(I); 12-20-407(1)(a). "
    "Board rules at 3 CCR 710-1, sos.state.co.us/CCR. All read August 2026."))

# ---------------------------------------------------------------- plumbing
flow += k.h2_tight("PLUMBING AND GAS PIPING — C.R.S. ARTICLE 155 "
                   "(STATE PLUMBING BOARD)")
flow.append(k.body(
    "Same shape, three differences that matter. The exemption, verbatim: \"<i>Nothing in this article 155 requires an individual to "
    "hold a license to perform plumbing work on the individual's own "
    "property or residence … except that, if such property or residence is "
    "intended for sale or resale by a person engaged in the business of "
    "constructing or remodeling the facilities or structures or is rental "
    "property that is occupied or is to be occupied by tenants … or is a "
    "commercial or industrial building, the owner is responsible for and the "
    "property is subject to the provisions of this article 155 pertaining to "
    "<b>licensing</b></i>\" (12-155-118(2))."))

diff_rows = [
    [k.cellp("<b>No inspection condition</b>"),
     k.cellp("The plumbing exemption is not conditioned on the work being "
             "inspected. The permit and inspection duty in 12-155-120 still "
             "applies to the work — but skipping it does not retroactively "
             "dissolve your license exemption the way 12-115-116(2) does. "
             "Do not read this as permission to skip: unlicensed plumbing "
             "is also a class 2 misdemeanor (12-20-407(1)(a)(IV)).")],
    [k.cellp("<b>It covers gas piping</b>"),
     k.cellp("\"<i>Any plumbing <b>or gas piping</b> installation in any new "
             "construction</i>\" needs the permit and the inspection "
             "(12-155-120(1)(a)). \"Gas piping\" means \"<i>any arrangement "
             "of piping used to convey fuel gas, supplied by one meter</i>\" "
             "(12-155-103(2)) — so the propane runs in a mountain house sit "
             "inside the state plumbing permit. The board adopts a separate "
             "<b>Colorado fuel gas code</b> for it (12-155-106(5)).")],
    [k.cellp("<b>A different local carve-out test</b>"),
     k.cellp("Electrical defers to a local building department that "
             "\"<i>meets the minimum standards</i>\" and processes building "
             "permits. Plumbing defers only \"<i>where the local entity … "
             "conducts inspections and issues plumbing permits</i>\" "
             "(12-155-120(1)(a)). Different tests, so <b>a jurisdiction can "
             "run one program and not the other</b> — which is why CO.0 "
             "makes you ask the two questions separately.")],
]
flow.append(k.ref_table(
    "Three ways plumbing is not a copy of electrical",
    [k.cellp("Difference", bold=True), k.cellp("What the statute says",
                                               bold=True)],
    diff_rows, [1.6 * inch, CW - 1.6 * inch]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "Everything else runs parallel: permit before the work "
    "(12-155-120(1)(c)(I)); inspection within three working days; permits "
    "valid twelve months with the same extension routes (12-155-120(3)(a)); "
    "and \"<i>qualified applicant</i>\" again expressly includes \"<i>a "
    "homeowner performing work on the homeowner's home</i>\" "
    "(12-155-120(11)(c))."))
flow.append(k.body(
    "The Colorado plumbing code is a statewide minimum by design: the board "
    "\"<i>shall establish a Colorado plumbing code … [that] must represent "
    "the minimum standards for installation, alteration, and repair of "
    "plumbing equipment and systems <b>throughout the state</b></i>\" "
    "(12-155-106(1)), and \"<i>Local governments are permitted to amend the "
    "code for their jurisdictions as long as the amendments are at least "
    "equal to the minimum requirements</i>\" (12-155-106(2)). What the board "
    "has actually adopted sits in <b>3 CCR 720-1</b>: the <b>Colorado "
    "Plumbing Code</b> is built on named chapters of the <b>2021 "
    "International Plumbing Code</b> and the 2021 IRC, and the <b>Colorado "
    "Fuel Gas Code</b> on the <b>2021 International Fuel Gas Code</b> and "
    "the IRC — in each case \"<i>with certain additions, revisions, and "
    "deletions</i>,\" and expressly not including later editions."))
flow.append(k.body(
    "<b>Note the five-year gap.</b> As of August 2026 Colorado's statewide "
    "electrical minimum is the 2026 NEC while its plumbing and fuel-gas "
    "minimums are built on 2021 model codes — you will wire to a code edition "
    "that took effect this year and plumb to one five years older, on the "
    "same house, under two different boards. Check each rule yourself at "
    "sos.state.co.us/CCR before you rely on either date."))
flow.append(k.cite(
    "C.R.S. 12-155-118(2), 12-155-120(1)(a), (1)(c)(I), (3)(a), (11)(c), "
    "12-155-103(2), 12-155-106(1), (2), (5); 12-20-407(1)(a)(IV). Adopted "
    "codes read from 3 CCR 720-1 (State Plumbing Board Rules and "
    "Regulations) and 3 CCR 710-1 (State Electrical Board Rules and "
    "Regulations) at sos.state.co.us/CCR, August 2026."))

# ---------------------------------------------------------------- both trades
flow.append(Spacer(1, 4))
flow.append(k.callout("The rule that covers both trades", [
    Paragraph("Being exempt from a <b>license</b> is never being exempt from "
              "a <b>permit</b>. Both articles require a permit before work "
              "begins and an inspection after, on every new-construction "
              "installation, no matter who does the work — and both name you, "
              "the homeowner, as a person entitled to buy that permit. The "
              "exemption saves you from needing a licensed tradesperson. It "
              "does not save you from the paperwork — and on the electrical "
              "side, the paperwork is what keeps the exemption alive.",
              S["body"]),
]))

# ---------------------------------------------------------------- plans
flow += k.h2_tight("YOUR PLANS — YOU MAY DRAW THEM YOURSELF")
flow.append(k.body(
    "A useful thing Colorado gives you, and few owner-builders know it. The "
    "architects' practice act does not reach houses: \"<i>Nothing in this "
    "part 4 shall prevent any person … from preparing plans and "
    "specifications for, designing, planning, or administering the "
    "construction contracts for construction … of … <b>One-, two-, three-, "
    "and four-family dwellings, including accessory buildings commonly "
    "associated with those dwellings</b></i>\" (12-120-403(1)(a)). The "
    "county statute that otherwise demands a seal defers to it: plans must "
    "bear the seal of a Colorado-licensed architect or engineer "
    "\"<i>unless the preparation of plans and specification is exempted by "
    "section 12-120-403</i>\" (30-28-205(3))."))
flow.append(k.body(
    "The limit is local and real: 12-120-403(2) preserves every county's and "
    "municipality's power to adopt building codes, and across the Front "
    "Range's expansive soils and the high country's snow loads departments "
    "routinely require an <b>engineered foundation design, a soils report</b>, "
    "and sealed structural calculations. That is a code requirement on the "
    "structure, not a licensing requirement on the draftsman. Ask exactly "
    "which sheets need a seal before you draw."))
flow.append(k.cite(
    "C.R.S. 12-120-403(1)(a), (2); 30-28-205(3). Read August 2026. Which "
    "sheets your jurisdiction requires sealed is a local fact — confirm it."))

# ---------------------------------------------------------------- other trades
# ---------------------------------------------------------------- local practice
flow += k.h2_tight("THE LOCAL LAYER — TWO VERIFIED EXAMPLES OF HOW FAR IT "
                   "VARIES")
flow.append(k.body(
    "State law is the floor. Whichever local government permits your parcel "
    "sets its own owner-builder terms on top of it, and Colorado's differ "
    "more than almost any other state's. Two verified examples:"))

ob_rows = [
    [k.cellp("<b>Denver</b><br/>City &amp; County"),
     k.cellp("Single-family only — not ADUs, townhomes, condos, or duplexes, "
             "\"<i>even for the unit where you live</i>.\" \"<i>You must be "
             "the legal owner and resident</i>\"; permits \"<i>cannot be "
             "issued to trusts, LLCs, or corporations</i>.\" An <b>exam</b> is "
             "required before doing electrical, plumbing, or mechanical work "
             "(a state license may substitute). \"<i>You must occupy the home "
             "for at least one year after work is complete</i>,\" and may "
             "build a new home as a homeowner only \"<i>once every five "
             "years</i>.\"")],
    [k.cellp("<b>Pikes Peak</b><br/>Regional Building Dept."),
     k.cellp("\"<i>As a homeowner you may obtain a permit only if you are "
             "performing the work on your primary residence, which you own "
             "and reside in. You cannot perform work on a rental property you "
             "own nor a home you do not reside in.</i>\" And the line worth "
             "memorizing: \"<i><b>It is illegal for a homeowner to obtain a "
             "permit for a contractor hired to do the work for you.</b></i>\" "
             "Build without a permit and a Certificate of Alleged "
             "Non-compliance is filed with the county clerk, <b>placing a "
             "lien against the property</b>.")],
]
flow.append(k.ref_table(
    "Same state, same statutes — two very different counters",
    [k.cellp("Jurisdiction", bold=True),
     k.cellp("What its own pages say", bold=True)],
    ob_rows, [1.35 * inch, CW - 1.35 * inch]))
flow.append(Spacer(1, 6))
flow.append(k.callout("Four questions, one email", [
    Paragraph("Neither set of terms above is in any statute — both are local "
              "policy, and yours will differ again. Before you count on doing "
              "anything yourself, ask your permit office: <b>(1)</b> must an "
              "owner-builder register as a contractor? <b>(2)</b> is there an "
              "owner-builder affidavit or agreement, and what does signing it "
              "commit you to — ownership, occupancy, a period you may not "
              "sell, an exam? <b>(3)</b> which trades will you let me permit "
              "personally? <b>(4)</b> which code editions and local "
              "amendments? A dated written answer from the office that will "
              "issue your permit outranks anything printed in any guide, "
              "including this one.", S["body"]),
]))
flow.append(k.cite(
    "Denver CPD, \"Applying for Permits as a Homeowner\" (denvergov.org); "
    "Pikes Peak Regional Building Department, Homeowner Permits (pprbd.org). "
    "Both read August 2026; local policy changes without notice."))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("POSITION CHECKLIST — SETTLE THESE BEFORE YOU PLAN THE "
                   "WORK")
flow.append(k.body(
    "Every line is a decision this document has shown to be yours to make — "
    "and most of them change the budget. Work down it with a pen."))

flow += k.check_table("Step 1 — Who permits your parcel", [
    ("Confirmed whether the parcel is inside a municipality or in "
     "unincorporated county, and which government permits it",
     [("Jurisdiction:", 1.0)]),
    ("Confirmed whether that jurisdiction has adopted a building code, and "
     "which edition, with the local amendment list in hand",
     [("Edition:", 0.5), ("Amendments:", 0.5)]),
    ("ELECTRICAL: asked whether the jurisdiction issues electrical permits "
     "and inspects, or whether the State Electrical Board does",
     [("Issued by:", 1.0)]),
    ("PLUMBING &amp; GAS: asked the same question separately — the statutory "
     "test is different and the answer can differ",
     [("Issued by:", 1.0)]),
    "Asked whether an owner-builder must register as a contractor, and "
    "whether an owner-builder affidavit is required — and what signing it "
    "commits you to",
    ("Written answers filed with this kit",
     [("Who answered:", 0.6), ("Date:", 0.4)]),
], notes_header="Notes / who answered")

flow += k.check_table("Step 2 — Trade-by-trade decisions", [
    "ELECTRICAL: decided between a licensed electrician and the homeowner "
    "exemption — and understood that relying on the exemption REQUIRES the "
    "work to be inspected (12-115-116(2))",
    ("If hiring: license verified at dora.colorado.gov, and the firm "
     "confirmed as a registered electrical contractor",
     [("License #:", 0.55), ("Verified:", 0.45)]),
    "PLUMBING &amp; GAS: decided between a licensed plumber and the "
    "homeowner exemption — and confirmed the gas piping is inside the "
    "plumbing permit, not the HVAC scope",
    "Confirmed the house is being built to occupy, not to sell or rent — "
    "the exclusions in 12-115-116(2) and (4) end the exemption either way",
    ("Permit term planned: asked for a permit longer than twelve months AT "
     "APPLICATION if the build will run long (12-115-120(6)(a))",
     [("Term granted:", 1.0)]),
    ("Utility's new-service requirements confirmed — no permanent power "
     "without proof of final electrical approval (12-115-120(1)(c))",
     [("Utility:", 1.0)]),
], notes_header="Notes")

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("No state GC or HVAC license as of August 2026; Title 12 licenses "
     "electricians and plumbers only", "C.R.S. Title 12 article list"),
    ("Counties are AUTHORIZED to adopt a building code — not required; the "
     "permit duty exists only after adoption; agricultural shelter may be "
     "excepted", "C.R.S. 30-28-201(1), 30-28-205(1)"),
    ("Electrician license required", "C.R.S. 12-115-109(1)"),
    ("Homeowner electrical exemption is conditioned on the work being "
     "inspected", "C.R.S. 12-115-116(2)"),
    ("Sale, lease, or rental development removes the exemption; "
     "maintenance/repair of existing facilities needs no license, "
     "inspection, or fee", "C.R.S. 12-115-116(2), (4), (6)"),
    ("State electrical permit unless a qualifying local building department "
     "issues it; permit and fee BEFORE work begins; inspection within three "
     "working days", "C.R.S. 12-115-120(1)(a)(I), (2)(a), (2)(b)"),
    ("A homeowner working on their own home is a \"qualified applicant\" for "
     "both permits", "C.R.S. 12-115-120(11)(c); 12-155-120(11)(c)"),
    ("No utility service without proof of final electrical approval",
     "C.R.S. 12-115-120(1)(b), (1)(c)"),
    ("Statewide electrical minimum is the 2026 NEC, effective August 1, 2026", "3 CCR 710-1, Rule 1.5(A)"),
    ("Homeowner plumbing exemption carries NO inspection condition; "
     "unlicensed practice in either trade is a class 2 misdemeanor",
     "C.R.S. 12-155-118(2); 12-20-407(1)(a)"),
    ("State plumbing permit covers GAS PIPING; different local carve-out "
     "test", "C.R.S. 12-155-120(1)(a); 12-155-103(2)"),
    ("Local owner-builder terms vary far beyond the statutes",
     "denvergov.org; pprbd.org"),
    ("One- to four-family dwellings are exempt from the architect-licensing "
     "requirement", "C.R.S. 12-120-403(1)(a); 30-28-205(3)"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "co-permit-kit",
                       "CO.1-owner-builder-legal-position.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
