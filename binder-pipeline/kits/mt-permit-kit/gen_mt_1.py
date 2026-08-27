#!/usr/bin/env python3
"""MT.1 The Owner-Builder Exemption Walkthrough — Montana.

Every Montana claim in this document was read out of the Montana Code
Annotated on the Legislature's own server at mca.legmt.gov in August 2026, and
is cited on-page. Where the statute is silent or jurisdictions differ, the
document says so and gives the verification step.

Verified sources:
  37-45-101             NEW chapter purpose: regulation of construction
                        contractors (effective January 1, 2026)
  37-45-102(1)(a),(b)   "construction contractor" defined — (1)(b) reaches an
                        owner working on their OWN property who employs members
                        of more than one trade on a single job
  37-45-104(8),(12),(13),(16),(18),(20),(24)  the exemptions, redesignated from
                        39-9-211; (13) is the owner-builder exemption and its
                        anti-flip condition with the 12-month escape
  37-45-201(1)          construction contractor LICENSE required; the
                        application must show workers'-comp compliance
  37-45-202             engaging a LICENSED contractor shields you from
                        employer liability for workers' comp, UI, and wages
  37-45-203(1)          application fee set by the department — no figure in
                        statute, so the kit prints none
  37-45-301(1)(d)       hiring an independent contractor without an ICEC
  50-60-102(1)(a),(2)   the state building code "does not apply to" residential
                        buildings of fewer than five dwelling units unless the
                        local legislative body adopts it; the state "may not
                        enforce" it for them
  50-60-102(5)          the ENERGY provisions apply anyway
  50-60-802(1)          builder self-certification, in writing, to the owner
  50-60-205(1)          no local code adopted => state code applies, state
                        enforces
  50-60-301(2)(a)       locals may NOT be more stringent — a ceiling, not a
                        floor
  50-60-302(1)          a local government may not enforce without certification
  50-60-203(5)(a)       no residential fire-sprinkler mandate may be included
  37-68-103(3)(a),(b)   homeowner electrical exemption — LICENSE only; grid-tied
                        generator work excluded. Contrast (2) and (7)(a), which
                        say "licensing and inspection"
  50-60-604, -605, -607 electrical permit, the power-supplier bar, and the
                        misdemeanor
  50-60-506(4)          homeowner plumbing exemption — reaches the PERMIT
  37-69-102(1)(a),(h)   the narrower plumbing LICENSE exemption, and the
                        private-water-supply pump exemption

DEAD CITATIONS — do not reintroduce. MCA Title 39, chapter 9 (Contractor
Registration) was repealed and renumbered effective January 1, 2026 by Ch. 481
and Ch. 644, Laws of 2025. 39-9-101, -102, -103, -201, -204, -206, -207 and
-401 are repealed; 39-9-205 was renumbered 37-45-205 and 39-9-211 redesignated
37-45-104. Every Montana owner-builder guide we checked, including our own
earlier one, still cites the dead chapter.

Still deliberately hedged: the adopted code editions (ARM Title 24, chapter
301, not statute); the department's contractor license fee (set by rule);
whether your particular local government has adopted the code for residential
buildings; and every local owner-builder policy.
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

FORM_ID = "MT.1"
FORM_TITLE = "The Owner-Builder Exemption Walkthrough"
TOPIC = "Your Legal Position"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What Montana actually requires of a person building their own house — the "
    "contractor license that appeared in 2026, the building code that may not "
    "apply, and the three duties that survive the exemption anyway.")

flow.append(k.disclaimer(
    "Statute text was read from the Montana Code Annotated at mca.legmt.gov in "
    "August 2026; statutes change, and Montana changed this area of law "
    "effective January 1, 2026."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION")
flow.append(k.body(
    "Montana licenses no <b>residential general contractor</b> in the sense "
    "most states mean — there is no exam, no experience requirement, and no "
    "trade competency test for the person building a house. What Montana has "
    "instead, as of <b>January 1, 2026</b>, is a <b>construction contractor "
    "license</b> aimed at insurance compliance, and it carries an owner "
    "exemption you almost certainly qualify for. The <b>state building "
    "code</b> very likely does not apply to your house at all: by statute it "
    "\"<i>does not apply to … residential buildings containing less than five "
    "dwelling units</i>\" unless your local legislative body has adopted it, "
    "and the state \"<i>may not enforce</i>\" it for those buildings. "
    "<b>But three duties survive that exemption</b>, and they are the three "
    "nobody tells you about: an <b>electrical permit</b> your power supplier "
    "is forbidden to connect you without, an <b>energy code</b> you certify in "
    "writing yourself, and the entire body of water, wastewater, and land-use "
    "law that chapter 60 never touched."))
flow.append(k.cite(
    "37-45-201(1), 37-45-104(13); 50-60-102(1)(a), (2), (5); 50-60-604, "
    "50-60-605; 50-60-802(1), MCA. Read August 2026."))

# ---------------------------------------------------------------- dead cites
flow.append(k.callout(
    "Before you read anything else about Montana contractors — check the date",
    [
        Paragraph("On <b>January 1, 2026</b> Montana repealed and renumbered "
                  "its entire contractor statute. <b>MCA Title 39, chapter 9 "
                  "— \"Contractor Registration\" — is dead law.</b> Sections "
                  "39-9-101, -102, -103, -201, -204, -206, -207 and -401 were "
                  "repealed (Ch. 481 and Ch. 644, Laws of 2025); 39-9-205 was "
                  "renumbered <b>37-45-205</b> and the exemptions at 39-9-211 "
                  "were redesignated <b>37-45-104</b>. The live chapter is "
                  "<b>MCA Title 37, chapter 45 — Construction Contractors</b>. "
                  "Nearly every Montana owner-builder guide, article, and "
                  "forum answer still cites the repealed chapter, and several "
                  "still describe the credential as a registration rather than "
                  "a license. If what you are reading cites Title 39 chapter "
                  "9, it was written for a Montana that no longer exists.",
                  S["body"]),
    ]))
flow.append(Spacer(1, 6))

# ---------------------------------------------------------------- contractor
flow += k.h2_tight("THE CONSTRUCTION CONTRACTOR LICENSE — MCA TITLE 37, "
                   "CHAPTER 45")
flow.append(k.body(
    "The rule is flat: \"<i>An individual or business entity may not engage in "
    "business as a construction contractor <b>without a current license from "
    "the department</b></i>\" (37-45-201(1)). What the application asks for "
    "tells you what the license is really for — a Social Security number, "
    "\"<i>proof of compliance with workers' compensation laws</i>,\" an "
    "employer identification number, and the names of the partners, officers, "
    "or members. There is <b>no examination and no competency requirement in "
    "the statute</b>. This is an insurance and accountability credential "
    "wearing the word \"license.\""))
flow.append(k.body(
    "That word is new. Until January 1, 2026 the same credential was called a "
    "<b>registration</b> and lived in the labor title; the 2025 Legislature "
    "moved it into the professions and occupations title and restated its "
    "purpose as protecting \"<i>the public health, safety, and welfare of the "
    "public through the regulation of construction contractors</i>\" "
    "(37-45-101). Parts of the chapter still say \"registered\" and "
    "\"register\" where the new sections say \"license\" — both words appear "
    "in the same chapter today. Do not read anything into which one a "
    "particular subsection uses."))

flow.append(Paragraph("The definition reaches further than you expect",
                      S["h3"]))
flow.append(k.body(
    "Most people read the first half of the definition, see the words "
    "\"<i>for another</i>,\" and stop — a contractor is someone who builds for "
    "someone else. But there is a second half, and it is about <b>your own "
    "property</b>. A \"construction contractor\" is a person who:"))
flow.append(k.body(
    "\"<i>(a) <b>in the pursuit of an independent business</b>, offers to "
    "undertake, undertakes, or submits a bid to construct, alter, repair, add "
    "to, subtract from, improve, move, wreck, or demolish <b>for another</b> a "
    "building … <b>or</b> (b) in order to do work similar to that described in "
    "subsection (1)(a) <b>on the construction contractor's property, employs "
    "members of more than one trade on a single job or under a single building "
    "permit</b>, except as otherwise provided</i>\" (37-45-102(1))."))
flow.append(Spacer(1, 4))
flow.append(k.callout("What (1)(b) means for you, in plain terms", [
    Paragraph("Subsection (1)(b) is the one that reaches owner-builders. If "
              "you <b>employ</b> members of <b>more than one trade</b> on a "
              "single job on your own property, the definition catches you — "
              "and then you need the exemption below to get back out. The "
              "load-bearing word is <b>employs</b>: engaging separate "
              "independent businesses under their own licenses is not the same "
              "thing as employing tradespeople. This is exactly the "
              "distinction that decides your workers'-compensation exposure "
              "too, which is why the two questions are really one question. "
              "See the hiring rules below and MT.2.", S["body"]),
]))
flow.append(Spacer(1, 6))

flow.append(Paragraph("The owner exemption, in full", S["h3"]))
flow.append(k.body(
    "Twenty-four exemptions sit at 37-45-104 — the section formerly numbered "
    "39-9-211. The one that matters is <b>(13)</b>, and it is unusually "
    "generous. The chapter does not apply:"))
flow.append(k.body(
    "\"<i>(13) to <b>an owner working on the owner's property, whether "
    "occupied by the owner or not</b>, but this exemption does not apply to an "
    "owner who is otherwise covered by this chapter who constructs an "
    "improvement on the owner's property <b>with the intention and for the "
    "purpose of promptly selling the improved property</b>, unless the owner "
    "has <b>continuously occupied the property as the owner's primary "
    "residence for at least the last 12 months</b></i>.\""))
flow.append(Spacer(1, 4))

ex_rows = [
    [k.cellp("<b>No occupancy requirement</b>"),
     k.cellp("The statute says \"<i>whether occupied by the owner or not</i>.\" "
             "Montana does not ask you to live in the house — which would be "
             "impossible for one under construction — and does not ask you to "
             "promise to. Guides that print \"a home you own and live in\" are "
             "adding words the statute does not contain.")],
    [k.cellp("<b>One condition: the flip</b>"),
     k.cellp("The exemption drops away if you build \"<i>with the intention "
             "and for the purpose of promptly selling</i>.\" It is a test of "
             "purpose at the time you build, not a ban on ever selling. And it "
             "has its own escape: an owner who has <b>continuously occupied "
             "the property as a primary residence for at least the last 12 "
             "months</b> keeps the exemption even then.")],
    [k.cellp("<b>Hiring one licensed contractor</b>"),
     k.cellp("Exemption (12) covers \"<i>an owner who contracts for work to be "
             "performed by a registered construction contractor</i>\" — with "
             "the same anti-flip proviso. So the ordinary owner-builder "
             "pattern, hiring licensed trades and running the job yourself, "
             "sits inside two exemptions at once.")],
    [k.cellp("<b>The small-job line</b>"),
     k.cellp("Exemption (8) covers work \"<i>of a casual, minor, or "
             "inconsequential nature</i>\" whose aggregate contract price for "
             "labor, materials, and all other items is <b>less than $2,500 a "
             "job</b> — but expressly <b>not</b> where the work \"<i>is only a "
             "part of a larger or major operation</i>\" or is split into "
             "sub-$2,500 contracts \"<i>for the purpose of evasion</i>.\" "
             "Nobody builds a house under this exemption.")],
    [k.cellp("<b>Trades you hire</b>"),
     k.cellp("A Montana-licensed <b>electrician or plumber operating within "
             "the scope of the license</b> is exempt from this chapter "
             "entirely (16), as is a licensed <b>water well contractor</b> "
             "doing water well work (20) and a Montana-licensed architect or "
             "engineer acting solely in a professional capacity (15).")],
    [k.cellp("<b>Solo trades</b>"),
     k.cellp("\"<i>An independent contractor who has no employees</i>\" is "
             "exempt (24) — though the statute lets one \"<i>voluntarily elect "
             "to register</i>.\" A great many Montana subcontractors are "
             "one-person businesses, so expect this to come up, and see the "
             "certificate discussed below.")],
]
flow.append(k.ref_table(
    "Reading 37-45-104 as an owner-builder",
    [k.cellp("The point", bold=True),
     k.cellp("What the statute says", bold=True)],
    ex_rows, [1.6 * inch, CW - 1.6 * inch]))
flow.append(k.cite(
    "37-45-101, 37-45-102(1), 37-45-104(8), (12), (13), (15), (16), (20), "
    "(24), 37-45-201(1), 37-45-203(1), MCA (chapter effective January 1, "
    "2026; 37-45-104 redesignated from 39-9-211 by Sec. 20, Ch. 644, L. "
    "2025). The department sets the license application fee by rule "
    "(37-45-203(1)); no figure appears in statute, so none is printed here."))

# ---------------------------------------------------------------- hiring
flow += k.h2_tight("IF YOU HIRE ANYONE — THE SHIELD, AND HOW YOU LOSE IT")
flow.append(k.body(
    "This is the most valuable paragraph in the document for anyone paying "
    "for labor. Montana gives you a statutory shield, and it is switched on by "
    "one fact: whether the person you engaged holds a license."))
flow.append(k.callout_long(
    "The workers'-compensation shield — 37-45-202", [
        Paragraph("\"<i>A person who, pursuant to an oral or written contract, "
                  "<b>engages a construction contractor who is licensed under "
                  "this chapter on the date of the contract is not liable as "
                  "an employer for workers' compensation coverage under "
                  "39-71-405, for unemployment insurance coverage, or for "
                  "wages and fringe benefits</b></i>\" for that contractor, "
                  "that contractor's employees, or a subsequent subcontractor "
                  "and its employees (37-45-202).", S["body"]),
        Paragraph("Read the trigger: <b>licensed on the date of the "
                  "contract</b>. Not licensed last year, not \"applying,\" not "
                  "licensed by the time the work happens. If the crew framing "
                  "your house is working for someone who was unlicensed the "
                  "day you shook hands, the shield never attached — and an "
                  "injury on your site becomes a question about whether "
                  "<b>you</b> were the employer. That is not a theoretical "
                  "risk; it is the reason this statute exists. Verify the "
                  "license, on the day you sign, and keep the printout.",
                  S["body"]),
        Paragraph("The parallel rule for one-person businesses is the "
                  "<b>independent contractor exemption certificate</b> under "
                  "39-71-417. The new chapter makes it unprofessional conduct "
                  "for a licensee to hire or classify someone as an "
                  "independent contractor who lacks a required certificate, or "
                  "whose certificate the department has suspended, revoked, or "
                  "denied (37-45-301(1)(d)). Ask every solo trade for the "
                  "certificate and file a copy.", S["body"]),
    ]))
flow.append(k.cite(
    "37-45-202, 37-45-301(1)(d), MCA; 39-71-405, 39-71-417, MCA. Read August "
    "2026. Whether any particular arrangement makes you an employer is a "
    "fact-specific question — this is the statutory rule, not advice about "
    "your job."))

# ---------------------------------------------------------------- code
flow += k.h2_tight("THE BUILDING CODE THAT PROBABLY DOES NOT APPLY TO YOUR "
                   "HOUSE")
flow.append(k.body(
    "Montana writes one statewide building code, adopted by rule by the "
    "Department of Labor &amp; Industry (50-60-203). Then the applicability "
    "section takes your house back out of it. The state building code "
    "\"<i><b>does not apply to</b> … residential buildings containing less "
    "than five dwelling units or their attached-to structures, any farm or "
    "ranch building of any size, and any private garage or private storage "
    "structure of any size used only for the owner's own use, located within a "
    "county, city, or town, <b>unless the local legislative body by ordinance "
    "or resolution makes the state building code applicable to these "
    "structures</b></i>\" (50-60-102(1)(a)). And the state's hands are tied: "
    "\"<i>the state <b>may not enforce</b> the state building code under "
    "50-60-205 for the buildings … referred to in subsection (1)</i>\" "
    "(50-60-102(2))."))
flow.append(k.callout("Say this precisely — it is not what most guides say", [
    Paragraph("The common phrasing is \"the code still applies, there is just "
              "nobody to inspect it.\" <b>That is not what the statute "
              "says.</b> It says the code <b>does not apply</b> — a "
              "scope limit, not an enforcement gap — unless your county, "
              "city, or town has affirmatively adopted it for these "
              "structures. Which cuts both ways. It means no building "
              "official can cite you under a code that does not reach your "
              "house. It also means <b>no code compliance is presumed</b>, and "
              "when a lender, insurer, appraiser, or buyer asks what your "
              "house was built to, the honest answer is whatever you can "
              "document — which is why MT.3 exists.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "Two consequences worth knowing. <b>Where a local government has adopted "
    "nothing</b>, \"<i>the state building code applies within the county, "
    "city, or town and the state will enforce the code in these areas</i>\" "
    "(50-60-205(1)) — for everything the 50-60-102(1) exemption did not carve "
    "out. Your house is carved out; a five-unit apartment building on the same "
    "street is not. <b>And a local government cannot enforce a code at all "
    "unless the department has certified its program</b> (50-60-302(1)), with "
    "inspectors who are themselves state-licensed journeymen in the craft they "
    "inspect or certified by an approved national body (50-60-302(1)(c))."))

flow.append(Paragraph("The rule that surprises people from other states",
                      S["h3"]))
flow.append(k.body(
    "In most of the country a state building code is a <b>floor</b>: cities "
    "may add to it, and famously do. Montana wrote the opposite. \"<i>Except "
    "as provided in subsection (2)(b), a county, city, or town <b>may not "
    "adopt or enforce a building code that is more stringent than the building "
    "code adopted by the department</b> or as required by state law</i>\" "
    "(50-60-301(2)(a)). The single exception is <b>voluntary</b>: a local "
    "government may adopt incentive-based energy standards that exceed the "
    "state's, and \"<i>New construction is not required to meet local "
    "standards that exceed state energy conservation standards unless the "
    "building contractor elects to receive a local incentive</i>\" "
    "(50-60-301(2)(b))."))
flow.append(k.body(
    "So the amendment-hunting that dominates permitting in Colorado, "
    "California, or Washington is largely absent here — <b>within the building "
    "code</b>. What varies locally is everything the building code is not: "
    "zoning, subdivision, floodplain, driveway access, addressing, fire "
    "district requirements, and the fee schedule. Those are the questions to "
    "spend your phone calls on."))
flow.append(k.body(
    "One more absence worth having in writing, because it comes up in every "
    "conversation about cost: the department <b>may not include in the state "
    "building code</b> \"<i>a requirement for the installation of a fire "
    "sprinkler system in a single-family dwelling or a residential building "
    "that contains no more than two dwelling units</i>\" (50-60-203(5)(a)), "
    "nor a requirement that buildings be built with solar or electric-vehicle "
    "wiring or equipment (50-60-203(5)(b))."))
flow.append(k.cite(
    "50-60-102(1)(a), (2); 50-60-203(5)(a), (5)(b); 50-60-205(1); "
    "50-60-301(2)(a), (2)(b); 50-60-302(1), (1)(c), MCA. Read August 2026. "
    "Whether YOUR local legislative body has adopted the code for residential "
    "buildings is the first question in MT.4, and the only one that changes "
    "everything else."))

# ---------------------------------------------------------------- electrical
flow += k.h2_tight("ELECTRICAL — THE EXEMPTION THAT IS NARROWER THAN IT LOOKS")
flow.append(k.body(
    "Here is the sentence every Montana owner-builder has read: \"<i>this "
    "chapter does not require an individual to hold a license to perform "
    "electrical work on the individual's own property or residence if the "
    "property or residence is maintained for the individual's own use</i>\" "
    "(37-68-103(3)(a)). It is real, and it is generous — no single-family "
    "limit, no occupancy requirement, no not-for-sale clause. Now read what it "
    "does <b>not</b> say, by comparing it with its neighbors in the very same "
    "section."))

cmp_rows = [
    [k.cellp("<b>37-68-103(2)</b><br/>maintenance electricians"),
     k.cellp("\"The <b><i>licensing or inspection</i></b> provisions of this "
             "chapter do not apply …\"")],
    [k.cellp("<b>37-68-103(7)(a)</b><br/>apprentices"),
     k.cellp("\"The <b><i>licensing and inspection</i></b> provisions of this "
             "chapter do not apply …\"")],
    [k.cellp("<b>37-68-103(3)(a)</b><br/><b>you, the homeowner</b>"),
     k.cellp("\"this chapter <b><i>does not require an individual to hold a "
             "license</i></b> …\" — <b>the word \"inspection\" is absent, and "
             "so is the word \"permit\"</b>")],
]
flow.append(k.ref_table(
    "Three exemptions, one section, two different scopes",
    [k.cellp("Subsection", bold=True),
     k.cellp("What it exempts you from", bold=True)],
    cmp_rows, [1.85 * inch, CW - 1.85 * inch]))
flow.append(Spacer(1, 6))

flow.append(k.callout_long(
    "THE TRAP — a license exemption is not a permit exemption", [
        Paragraph("The Legislature knew how to exempt someone from inspection: "
                  "it did so twice in the same section, in plain words. For "
                  "the homeowner it wrote something narrower. <b>You are "
                  "excused from holding an electrician's license. You are not "
                  "excused from the permit or the inspection.</b>", S["body"]),
        Paragraph("And it could not have been otherwise, because the permit "
                  "does not live in that chapter at all. The electrical permit "
                  "duty is in a different title: the department \"<i>or an "
                  "authorized representative or a county, city, or town "
                  "certified to perform an inspection pursuant to 50-60-302 "
                  "shall inspect electrical installations, issue electrical "
                  "permits for these installations, and establish and charge a "
                  "reasonable and uniform fee</i>\" (50-60-604). An exemption "
                  "written in Title 37 cannot waive a duty written in Title "
                  "50. Whenever you meet a Montana exemption, ask which title "
                  "it lives in.", S["body"]),
        Paragraph("Note also what the electrical part does <b>not</b> exempt. "
                  "Part 6 has its own exceptions list at 50-60-602 — utility "
                  "signal and traffic equipment, refineries, mines, low-voltage "
                  "signal and fiber — and <b>nothing in it about residential "
                  "buildings of fewer than five dwelling units</b>. The "
                  "carve-out that took your house out of the building code "
                  "never reached the electrical part.", S["body"]),
    ]))
flow.append(Spacer(1, 6))

flow.append(Paragraph("How Montana enforces it: at the meter", S["h3"]))
flow.append(k.body(
    "Montana does not send anyone looking for you. It waits at the point where "
    "you need something. \"<i>Except for temporary connections that the "
    "department of labor and industry may authorize by rule for a period not "
    "exceeding <b>14 days</b> without a preconnection inspection, <b>power "
    "suppliers may not connect with or energize an electrical installation "
    "under this part unless the owner or a licensed electrical contractor has "
    "delivered to the power supplier an electrical permit covering the "
    "installation</b></i>\" (50-60-605). The statute defines power suppliers "
    "broadly — \"<i>Individuals, firms, cooperatives, corporations, or "
    "municipalities selling electricity</i>\" — so your rural electric "
    "cooperative is bound by it exactly as an investor-owned utility is. Note "
    "the words \"<b>the owner or</b>\": you may deliver the permit yourself."))
flow.append(k.body(
    "And going around it is a crime, not a fee. \"<i>Any person … other than a "
    "power supplier, that energizes an electrical installation under this part "
    "for which an electrical permit has not been issued … is guilty of a "
    "<b>misdemeanor</b></i>\" (50-60-607). However quiet your county is about "
    "building permits, this is the gate: <b>no electrical permit, no permanent "
    "power.</b>"))

flow.append(k.callout("The one thing you may not do yourself — grid-tied", [
    Paragraph("The homeowner exemption has exactly one written carve-out, and "
              "it is aimed squarely at the modern rural build: \"<i>Subsection "
              "(3)(a) <b>does not include an exemption for an individual who "
              "is performing electrical work on a grid-tied generator</b> "
              "located at the individual's own property or residence</i>\" "
              "(37-68-103(3)(b)). If your plans include a grid-tied solar "
              "array, a grid-tied wind turbine, or an interconnected standby "
              "generator, that work needs a <b>licensed electrician</b> even "
              "though the rest of the house does not. Off-grid systems with no "
              "utility interconnection are not what this subsection describes "
              "— but if there is any chance you will interconnect later, price "
              "the licensed work now.", S["body"]),
]))
flow.append(Paragraph("The condition the statute does not mention", S["h3"]))
flow.append(k.body(
    "The licensing exemption in 37-68-103(3)(a) has no not-for-sale clause. "
    "The <b>permit</b> rule does. <b>ARM 24.301.431(3)</b> defines who may "
    "hold an electrical permit and includes owners doing electrical work on "
    "their own residence, farm, or ranch property \"<i>maintained for their "
    "personal, private use</i>\" — adding that the property \"<i>shall not be "
    "built on speculation of resale or intended as rental property</i>.\" So "
    "the practical rule for both trades is the same, and it comes from the "
    "rules rather than the code: <b>you may permit your own work on the home "
    "you will actually live in, and not on one you are building to sell or "
    "rent</b>. A spec or rental build needs a licensed electrician and a "
    "licensed plumber. The plumbing rule is worded slightly tighter still, "
    "reaching \"<i>the dwelling in which they will reside</i>\" "
    "(ARM 24.301.361(3))."))
flow.append(k.callout_long("The rule that ends \"my buddy is going to help "
                           "me wire it\"", [
    Paragraph("This is the single most commonly broken rule in Montana "
              "owner-building, and almost nobody knows it exists. Under "
              "<b>ARM 24.301.431(8)</b>, <b>no person other than the "
              "permittee</b> — or, where the permittee is an electrical "
              "contractor, that contractor's licensed employees — may perform "
              "<b>any</b> work under the permit.", S["body"]),
    Paragraph("Read that against the homeowner permit. You pulled it as the "
              "owner doing your own work. That means <b>you</b> do the work: "
              "not your brother-in-law who wires for a living, not a friend "
              "who is between jobs, not a neighbor helping for a weekend. If "
              "someone else is going to put hands on it, the lawful routes "
              "are a licensed electrician pulling their own permit, or that "
              "person working as a licensed electrical contractor's employee "
              "under the contractor's permit. And remember the inspector is "
              "<b>required</b> to demand proof of licensure from anyone on "
              "site who appears involved with the installation "
              "(50-60-604) — so this is checked in practice, not just on "
              "paper.", S["body"]),
]))
flow.append(Spacer(1, 4))
flow.append(k.callout("\"No permit\" has never meant \"no requirements\"", [
    Paragraph("If you want one rule that settles the argument, it is this "
              "one. Montana's electrical amendments require smoke alarms and "
              "carbon monoxide alarms to be installed per the adopted "
              "building and residential codes <b>\"<i>regardless of whether "
              "or not the building or structure is exempt by 50-60-102, "
              "MCA</i>\"</b> (ARM 24.301.411(1)(d)). The rule reaches out "
              "specifically to name the exemption that took your house out of "
              "the building code — and applies anyway. Whatever else you "
              "conclude about building without a permit, the life-safety "
              "requirements did not go away with the inspector.", S["body"]),
]))
flow.append(k.cite(
    "37-68-103(2), (3)(a), (3)(b), (7)(a), MCA; 50-60-602, 50-60-604, "
    "50-60-605, 50-60-607, MCA. Permit-holder conditions and the alarm "
    "requirement: ARM 24.301.431(3) and ARM 24.301.411(1)(d), read August "
    "2026 — the department reproduces 24.301.431 in its own Electrical "
    "Information Pamphlet, which it labels unofficial guidance, so read the "
    "rule itself before you rely on it. The adopted National Electrical Code "
    "edition is likewise set by rule, not statute (50-60-603(2))."))

# ---------------------------------------------------------------- plumbing
flow += k.h2_tight("PLUMBING — THE MIRROR IMAGE, AND A CONDITION THAT HIDES "
                   "IN THE RULES")
flow.append(k.body(
    "Everything above runs the other way for plumbing, and this is where "
    "reading the statute instead of the summary pays for the kit. Montana "
    "gives the homeowner <b>two different plumbing exemptions, in two "
    "different titles, with two different conditions</b>. You need both, and "
    "they do not match."))

pl_rows = [
    [k.cellp("<b>The PERMIT</b><br/>50-60-506(4)"),
     k.cellp("\"<i>This part does not prohibit <b>the owner of residential "
             "property</b> from making an installation for all sanitary "
             "plumbing and potable water supply piping <b>without a permit</b> "
             "if <b>the owner personally does the work</b></i>.\""),
     k.cellp("Two conditions only <i>in the statute</i>: you own residential "
             "property, and you personally do the work. No single-family "
             "limit, no occupancy condition. <b>But see the callout below</b> "
             "— the administrative rule adds a spec-and-rental condition the "
             "statute does not contain.")],
    [k.cellp("<b>The LICENSE</b><br/>37-69-102(1)(a)"),
     k.cellp("Licensure is not required \"<i>when <b>an owner of a "
             "single-family residence used exclusively for the owner's "
             "personal use</b> installs all sanitary plumbing and potable "
             "water supply piping</i>.\""),
     k.cellp("Narrower: it must be a <b>single-family residence</b> and it "
             "must be \"<i>used exclusively for the owner's personal "
             "use</i>.\" This is the condition people are half-remembering "
             "when they describe the permit rule.")],
]
flow.append(k.ref_table(
    "Two plumbing exemptions — take the narrower of the two conditions",
    [k.cellp("Exempts you from", bold=True),
     k.cellp("The words", bold=True),
     k.cellp("What it actually requires", bold=True)],
    pl_rows, [1.38 * inch, (CW - 1.38 * inch) * 0.52,
              (CW - 1.38 * inch) * 0.48]))
flow.append(Spacer(1, 6))

flow.append(k.callout_long(
    "The spec-and-rental condition — real, but not where you would look for "
    "it", [
        Paragraph("You will read, on state web pages and in every guide that "
                  "copied them, that a homeowner may skip the plumbing permit "
                  "only if the residence \"is for the owner's personal use and "
                  "<b>not built on speculation of resale or intended as a "
                  "rental property</b>.\" That sentence is <b>not in "
                  "50-60-506(4)</b>, which imposes only ownership of "
                  "residential property and personal performance of the work, "
                  "and it is <b>not in 37-69-102(1)(a)</b>, which imposes a "
                  "single-family residence used exclusively for the owner's "
                  "personal use. So is the agency making it up? <b>No — and "
                  "this is the lesson.</b>", S["body"]),
        Paragraph("The condition lives in the <b>administrative rule</b>. "
                  "<b>ARM 24.301.361(3)</b> provides that permits may not be "
                  "issued to anyone other than a Montana-licensed master "
                  "plumber to install plumbing \"<i>in a residence that is "
                  "built on speculation of sale or rent and is not the owner's "
                  "primary residence in which they will reside</i>,\" and "
                  "<b>ARM 24.301.431(3)</b> does the same job on the "
                  "electrical side, limiting owner permits to the owner's own "
                  "residence, farm, or ranch \"<i>maintained for their "
                  "personal, private use</i>,\" not \"<i>built on speculation "
                  "of resale or intended as rental property</i>.\" An "
                  "administrative rule is binding law. The agency was "
                  "summarizing the rule, not the statute.", S["body"]),
        Paragraph("<b>Why this matters far beyond plumbing.</b> Montana keeps "
                  "an unusual amount of what actually governs your house in "
                  "the Administrative Rules rather than the code: the adopted "
                  "code editions, the state's amendments to them, the permit "
                  "fees, the inspection procedure, and — as here — real "
                  "conditions on the exemptions. <b>Reading only the statute "
                  "will mislead you in Montana.</b> When someone tells you "
                  "what Montana requires, ask whether the answer is in the "
                  "MCA or the ARM, and go read that one. The habit is worth "
                  "more than any single fact in this kit — and it is the same "
                  "habit that catches the dead Title 39 citations on page 2.",
                  S["body"]),
    ]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "Three more plumbing carve-outs worth knowing on a rural build. No license "
    "is required \"<i>in the case of a private water supply, [for the] "
    "installation of the pump, waterline, or pressure tank, regardless of "
    "whether the pump, waterline, or pressure tank is located inside or "
    "outside the structure being served</i>\" (37-69-102(1)(h)) — so your well "
    "pump and pressure tank are yours to install. Plumbing \"<i>on farms "
    "having their own individual water supply or sewage disposal system</i>\" "
    "is outside the state plumbing part altogether (50-60-503), and outside "
    "the plumbing chapter for farms and ranches not connected to public water "
    "or sewer (37-69-102(1)(c), (2)). And no state plumbing permit is required "
    "\"<i>whenever the installation occurs in an area governed by a county, "
    "city, or town and where there is in effect a county, city, or town "
    "building code that covers plumbing installations and that provides "
    "inspection procedures</i>\" (50-60-506(3)) — in a certified jurisdiction "
    "the permit is local, not absent."))
flow.append(k.cite(
    "50-60-503, 50-60-506(1), (2), (3), (4), MCA; 37-69-102(1)(a), (1)(c), "
    "(1)(h), (2), MCA. Read August 2026. The adopted plumbing code edition is "
    "set by rule in ARM Title 24, chapter 301 — confirm it at rules.mt.gov."))

# ---------------------------------------------------------------- energy
flow += k.h2_tight("THE ENERGY CODE — THE ONE YOU SIGN YOURSELF")
flow.append(k.body(
    "This is the duty that surprises everyone, because it sits three "
    "subsections below the exemption that people stop reading at. The same "
    "section that takes your house out of the state building code puts part of "
    "it back: \"<i>for purposes of promoting the energy efficiency of home "
    "design and operation, <b>the provisions of the state building code "
    "relating to energy conservation … apply to residential buildings</b></i>,"
    "\" excepting only farm and ranch buildings and private garages or storage "
    "structures used only for the owner's own use (50-60-102(5)(a))."))
flow.append(k.body(
    "Then it says who enforces it. For a residential building of fewer than "
    "five dwelling units not otherwise subject to the state building code — "
    "your house — the energy provisions are enforceable \"<i><b>through the "
    "builder self-certification program provided for in 50-60-802</b></i>\" "
    "(50-60-102(5)(b)(ii)). And 50-60-802(1) says what that means: \"<i>a "
    "person who begins construction on a residential building in Montana after "
    "October 1, 1993, <b>shall certify in writing to the building owner at the "
    "conclusion of construction that the residential building has been "
    "constructed in compliance with the energy-efficient construction "
    "standards</b></i>\" adopted under 50-60-203(1)."))
flow.append(k.callout("You are the builder and you are the owner", [
    Paragraph("Read those two roles again. The person who begins construction "
              "certifies, in writing, to the building owner. As an "
              "owner-builder you are both — so the statute has you certify to "
              "yourself, on paper, at the end of the job. It sounds like a "
              "formality until you need it: this document is the <b>only</b> "
              "code-compliance record many rural Montana houses will ever "
              "have, and it is the first thing a lender's appraiser, an "
              "insurer, or a future buyer's inspector will ask for. Write it, "
              "date it, sign it, and keep it with the house. MT.5 says what "
              "belongs in it.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "Which edition of the energy code you are certifying to is set by rule, "
    "not by statute, and the department may adopt national codes by reference "
    "\"<i>in whole or in part</i>\" and \"<i>may adopt rules more stringent "
    "than those contained in national codes</i>\" (50-60-203(2)) — Montana has "
    "historically amended what it adopts. Read the current adoption in ARM "
    "Title 24, chapter 301 at <b>rules.mt.gov</b> and write the edition and "
    "its effective date into the checklist below before you order insulation "
    "or windows."))
flow.append(k.body(
    "There is a <b>second</b> energy document, and it is physical. Under "
    "50-60-803 and <b>ARM 24.301.162</b> the builder completes a signed and "
    "dated <b>permanent label</b> — a self-adhesive card roughly four inches "
    "by six — listing the insulation R-values, window U-factor, heating and "
    "cooling equipment efficiencies, and water heater efficiency, and "
    "<b>permanently attaches it to the interior of the electrical panel</b>. "
    "That is where an appraiser or a home inspector will look for it in "
    "fifteen years, and it costs nothing to do at the time."))
flow.append(k.cite(
    "50-60-102(5)(a), (5)(b)(i), (5)(b)(ii); 50-60-203(1), (2); 50-60-802(1), "
    "(2); 50-60-803, MCA; ARM 24.301.162. Read August 2026. Subsection "
    "50-60-802(2) adds a parallel certification where a local government with "
    "a code enforcement program has adopted voluntary energy standards that "
    "the building meets or exceeds."))

# ---------------------------------------------------------------- penalties
flow += k.h2_tight("WHAT ACTUALLY HAPPENS IF YOU GET IT WRONG")
flow.append(k.body(
    "Montana rebuilt its enforcement machinery in 2023 and most published "
    "answers are out of date. The old trade-specific criminal penalties were "
    "<b>repealed</b>: 37-68-322 (electricians) and 37-69-324 (plumbers) both "
    "went away by Sec. 11, Ch. 366, L. 2023. Unlicensed practice in any Title "
    "37 profession now runs through one consolidated section."))
pen_rows = [
    [k.cellp("<b>Unlicensed practice</b><br/>any Title 37 trade"),
     k.cellp("The department \"<i>may issue a cease and desist order</i>\" on "
             "credible evidence that a person is acting \"<i>without the "
             "license required</i>\" (37-1-109(1)). Then: a penalty of "
             "<b>not more than $1,000 a day</b> for each day the order is "
             "violated (37-1-109(3)); an action for injunction, with costs of "
             "investigation and attorney fees (37-1-109(4)(a), (b)); and "
             "anyone who \"<i>knowingly or purposely violates</i>\" the "
             "injunction \"<i>is guilty of a <b>felony</b></i>\" "
             "(37-1-109(4)(c)). Note the shape: nothing bites until an order "
             "issues, and then it escalates fast.")],
    [k.cellp("<b>Plumbing without a permit<br/>or a license</b>"),
     k.cellp("The Title 37 penalty was repealed but its <b>Title 50 twin "
             "survived</b> — a divergence worth knowing. Under <b>50-60-515</b> "
             "a person who works in the field of plumbing in violation of the "
             "part \"<i>is guilty of a <b>misdemeanor</b></i>\" and shall be "
             "fined \"<i>not less than $10 and not more than $100 for each "
             "separate offense</i>,\" expressly excepting the work covered by "
             "37-69-102 and 50-60-503. And starting plumbing work without a "
             "required permit costs <b>double the permit fee</b> "
             "(50-60-509).")],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("Energizing an installation with no electrical permit is a "
             "<b>misdemeanor</b> (50-60-607), and knowing violation of the "
             "state electrical code is a misdemeanor as well (50-60-110).")],
    [k.cellp("<b>Hiring an unlicensed<br/>plumber</b>"),
     k.cellp("Montana expressly does <b>not</b> penalize you for it: the "
             "chapter \"<i>may not be construed as imposing a penalty on any "
             "unlicensed person for hiring or contracting with an unlicensed "
             "person to do work in the field of plumbing</i>\" (37-69-103; "
             "twin at 50-60-502). The exposure falls on the person doing the "
             "work — but read the workers'-compensation section above before "
             "you take comfort in that.")],
]
flow.append(k.ref_table(
    "The live penalties, after the 2023 consolidation",
    [k.cellp("Situation", bold=True), k.cellp("What the law provides",
                                              bold=True)],
    pen_rows, [1.55 * inch, CW - 1.55 * inch]))
flow.append(Spacer(1, 6))
flow.append(k.callout("Two trades Montana does not license at all", [
    Paragraph("Worth knowing before you price the job. Montana licenses "
              "electricians (Title 37, ch. 68), plumbers (ch. 69), water well "
              "contractors (ch. 43), construction blasters (ch. 72), and "
              "elevator work (ch. 73) — and <b>nothing else in the building "
              "trades</b>. There is <b>no HVAC or mechanical contractor "
              "license</b>: chapter 70, \"Heating, Ventilation, Air "
              "Conditioning,\" appears in the code as <b>(Repealed)</b>, its "
              "sections struck by Sec. 195, Ch. 575, L. 1981, and no "
              "replacement was ever enacted. There is <b>no gas fitter "
              "license</b> either — fuel gas is handled as a code, not a "
              "trade. Both kinds of work still need permits and inspection "
              "where a permit applies; neither needs a licensed installer.",
              S["body"]),
]))
flow.append(k.cite(
    "37-1-109(1), (3), (4)(a)–(c), MCA; 50-60-110, 50-60-509, 50-60-515, "
    "50-60-607, MCA; 37-69-103; 50-60-502, MCA. Repeals: 37-68-322 and "
    "37-69-324, Sec. 11, Ch. 366, L. 2023. Absence of HVAC licensing: MCA "
    "Title 37, chapter 70 is captioned \"(Repealed)\" and 37-70-101, -201, "
    "and -301 each read \"Repealed. Sec. 195, Ch. 575, L. 1981.\" Read August "
    "2026."))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("POSITION CHECKLIST — SETTLE THESE BEFORE YOU PLAN THE "
                   "WORK")
flow.append(k.body(
    "Every line is a decision this document has shown to be yours to make, and "
    "most of them change the budget. Work down it with a pen."))

flow += k.check_table("Step 1 — Which Montana are you building in", [
    ("Confirmed whether the parcel is inside a city or town, or in "
     "unincorporated county — and which local legislative body governs it",
     [("Jurisdiction:", 1.0)]),
    ("Asked that body, in writing, whether it has adopted the state building "
     "code for residential buildings of fewer than five dwelling units "
     "(50-60-102(1)(a)), and whether its enforcement program is certified "
     "under 50-60-302", [("Adopted?", 0.5), ("Certified?", 0.5)]),
    ("ELECTRICAL: asked who issues the electrical permit for this parcel — the "
     "Department of Labor &amp; Industry, or a certified local program "
     "(50-60-604)", [("Issued by:", 1.0)]),
    ("PLUMBING: asked whether a local building code covering plumbing with "
     "inspection procedures is in effect here, which removes the state permit "
     "(50-60-506(3))", [("Answer:", 1.0)]),
    ("Written answers, with the name of who gave them, filed with this kit",
     [("Who answered:", 0.6), ("Date:", 0.4)]),
], notes_header="Notes / who answered")

flow += k.check_table("Step 2 — Your own position under Title 37, chapter 45", [
    "Confirmed you are building on property you own, and that you are NOT "
    "building it with the intention and for the purpose of promptly selling — "
    "the only condition on the owner exemption (37-45-104(13))",
    "Read 37-45-102(1)(b) and decided how you will engage trades: as separate "
    "licensed businesses, or as people you employ. The answer decides both "
    "your licensing position and your workers'-comp exposure",
    ("For every contractor engaged: license verified under Title 37, chapter "
     "45 ON THE DATE OF THE CONTRACT, and the printout filed — this is what "
     "switches on the 37-45-202 shield",
     [("Verified for:", 0.6), ("Date:", 0.4)]),
    ("For every one-person trade: independent contractor exemption certificate "
     "obtained and filed (39-71-417)", [("Filed for:", 1.0)]),
    "Workers' compensation position settled in writing with your insurance "
    "agent before any paid labor sets foot on the site",
], notes_header="Notes")

flow += k.check_table("Step 3 — Trade-by-trade decisions", [
    "ELECTRICAL: decided between a licensed electrician and the homeowner "
    "exemption — and understood that the exemption reaches the LICENSE only, "
    "not the permit or the inspection (37-68-103(3)(a); 50-60-604)",
    ("Electrical permit obtained, and the power supplier's requirements "
     "confirmed — no permanent connection without the permit delivered to them "
     "(50-60-605); energizing without one is a misdemeanor (50-60-607)",
     [("Permit #:", 0.5), ("Supplier:", 0.5)]),
    "GRID-TIED: confirmed whether any solar, wind, or standby generator will "
    "interconnect with the utility — that work is NOT covered by the homeowner "
    "exemption and needs a licensed electrician (37-68-103(3)(b))",
    "PLUMBING: confirmed you personally will do the work if you are relying on "
    "50-60-506(4), and that the house meets the narrower license condition in "
    "37-69-102(1)(a) — single-family, used exclusively for your personal use",
    ("ENERGY: the adopted energy code edition and effective date read from ARM "
     "Title 24, chapter 301 and written down — you will certify to it at the "
     "end (50-60-802(1))", [("Edition:", 0.55), ("Effective:", 0.45)]),
], notes_header="Notes")

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("MCA Title 39, chapter 9 (Contractor Registration) repealed and "
     "renumbered effective January 1, 2026; the live chapter is Title 37, "
     "chapter 45", "Ch. 481 and Ch. 644, L. 2025; MCA 37-45-104 history line"),
    ("A construction contractor license is required; the application shows "
     "workers'-comp compliance, not competency", "37-45-201(1), MCA"),
    ("\"Construction contractor\" reaches an owner who employs members of more "
     "than one trade on their own property", "37-45-102(1)(b), MCA"),
    ("Owner working on the owner's property is exempt, occupied or not; the "
     "only condition is intent to promptly sell, with a 12-month "
     "primary-residence escape", "37-45-104(13), MCA"),
    ("Engaging a contractor licensed on the date of the contract shields you "
     "from employer liability for workers' comp, UI, and wages",
     "37-45-202, MCA"),
    ("The state building code does not apply to residential buildings of fewer "
     "than five dwelling units unless the local legislative body adopts it; "
     "the state may not enforce it for them", "50-60-102(1)(a), (2), MCA"),
    ("A local government may NOT adopt or enforce a building code more "
     "stringent than the state's", "50-60-301(2)(a), MCA"),
    ("No residential fire-sprinkler mandate may be included in the state "
     "building code", "50-60-203(5)(a), MCA"),
    ("The homeowner electrical exemption reaches the LICENSE only — compare "
     "the \"licensing and inspection\" wording in the same section",
     "37-68-103(3)(a), (2), (7)(a), MCA"),
    ("Grid-tied generator work on your own property is NOT exempt",
     "37-68-103(3)(b), MCA"),
    ("Electrical permits and inspections; no power supplier may energize "
     "without the permit; energizing without one is a misdemeanor",
     "50-60-604, -605, -607, MCA"),
    ("The homeowner plumbing exemption reaches the PERMIT; the license "
     "exemption is narrower and differently worded",
     "50-60-506(4); 37-69-102(1)(a), MCA"),
    ("Owner permits for both trades are limited to the owner's own residence, "
     "not one built on speculation of sale or rent — a condition in the RULES, "
     "not the statutes", "ARM 24.301.361(3);<br/>ARM 24.301.431(3)"),
    ("Smoke and carbon monoxide alarms are required regardless of the "
     "50-60-102 exemption", "ARM 24.301.411(1)(d)"),
    ("The energy code applies to residential buildings anyway, enforced by "
     "builder self-certification in writing to the owner",
     "50-60-102(5); 50-60-802(1), MCA"),
    ("A permanent energy label is attached inside the electrical panel",
     "50-60-803, MCA; ARM 24.301.162"),
    ("Unlicensed practice: cease and desist, then up to $1,000 a day, then "
     "injunction, then a felony for knowingly violating it", "37-1-109, MCA"),
    ("Unlicensed plumbing is a misdemeanor, $10 to $100 per offense; starting "
     "without a required permit doubles the fee", "50-60-515; 50-60-509, MCA"),
    ("Montana licenses no HVAC/mechanical contractor and no gas fitter — "
     "chapter 70 was repealed in 1981",
     "MCA Title 37, ch. 70<br/>(Repealed)"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "mt-permit-kit",
                       "MT.1-owner-builder-exemption-walkthrough.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
