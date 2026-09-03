#!/usr/bin/env python3
"""SC.1 Owner-Builder Exemption Walkthrough.

South Carolina's exemption is short, generous, and hung on three obligations
that live outside the statute's main sentence:

  1. § 40-59-260(C) — you must PERSONALLY APPEAR and sign the permit
     application, and the agency must hand you a disclosure statement whose
     wording the statute itself prints.
  2. § 40-59-260(E) — after the house exists you must file a notice at the
     REGISTER OF DEEDS saying you built it as an unlicensed builder. "Failure
     to do so revokes the statutory exemption." No fine, no notice period, no
     cure: the exemption you already relied on stops having been yours.
  3. § 40-59-260(A)(1) and (F) — the exemption lets you do the work yourself
     or with your own employees, and otherwise only with LICENSED contractors
     or REGISTERED entities. It never authorizes hiring an unlicensed person.

The document is built around those three, and then around the number nearly
every guide omits: the residential specialty threshold is $500, not $5,000.
$5,000 is the residential BUILDER threshold; $10,000 is the Chapter 11
general/mechanical threshold, raised from $5,000 by 2023 Act No. 69. Three
numbers, two chapters, two boards.
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
NB = k.NB
sec = k.sec

FORM_ID = "SC.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "The Exemption"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "The statute, the disclosure you sign at the counter, the "
                 "notice you file afterwards, and the three thresholds that "
                 "decide who you may pay.")
flow.append(k.disclaimer())

# ------------------------------------------------ the sentence that matters
flow += k.h2("THE EXEMPTION, IN ONE SENTENCE")
flow.append(k.body(
    "South Carolina licenses residential builders through the <b>Residential "
    "Builders Commission</b>, and the exemption that lets you build your own "
    "house without one is a single subsection. It opens by removing the "
    "entire chapter from you rather than by granting you a permission:"))
flow.append(k.body(
    "“This chapter does not apply to an owner of residential property who "
    "improves the property or who builds or improves structures or "
    "appurtenances on the property if: (1)&#160;the owner does the work himself, "
    "with his own employees, or with licensed contractors or registered "
    "entities or individuals; (2)&#160;the structure, group of structures, or "
    "appurtenances, including the improvements, are intended for the owner's "
    "sole occupancy or occupancy by the owner's family and are not intended "
    "for sale or rent; and (3)&#160;the general public does not have access to "
    "this structure.”"))
flow.append(k.cite(
    f"S.C. Code Ann. {sec('40-59-260')}(A). Note the cite. Some published "
    f"guides put the owner-builder exemption at {sec('40-59-30')}; that "
    f"section is <i>License requirement; enforcement of contracts; "
    f"restraining orders</i> and contains no exemption at all. "
    f"{sec('40-59-20')} is the definitions section."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "There is no square-footage cap and no permit counter", [
        Paragraph("South Carolina does not limit how big the house is, and it "
                  "does not limit you to one house every so many years. Read "
                  f"{sec('40-59-260')} and {sec('40-11-360')}(5) end to end "
                  "and there is no number of that kind anywhere in either. "
                  "What limits you instead is the character of the project: "
                  "sole occupancy by you or your family, not for sale or "
                  "rent, and no public access. If a guide gives you a square "
                  "footage or a one-per-year rule for South Carolina, it has "
                  "borrowed it from another state.", S["body"]),
    ]))

# ------------------------------------------------------------ two chapters
flow += k.h2_tight("TWO BOARDS, TWO EXEMPTIONS, ONE TWO-YEAR RULE",
                   reserve=2.2)
flow.append(k.body(
    "South Carolina regulates construction through two boards, both housed at "
    "the Department of Labor, Licensing and Regulation, and <b>each has its "
    "own owner exemption.</b> For a house on your own lot the Residential "
    "Builders Commission is the one that governs; the other exists so that "
    "nothing falls between them."))
rows = [
    [k.cellp("<b>Which statute</b>"),
     k.cellp(f"Title 40, <b>Chapter 59</b> — {sec('40-59-260')}"),
     k.cellp(f"Title 40, <b>Chapter 11</b> — {sec('40-11-360')}(5)")],
    [k.cellp("<b>Which board</b>"),
     k.cellp("Residential Builders Commission"),
     k.cellp("Contractor's Licensing Board")],
    [k.cellp("<b>What it covers</b>"),
     k.cellp("A residential building not over three floors in height and not "
             "more than sixteen units in any single apartment building "
             f"({sec('40-59-20')}(6))"),
     k.cellp("General and mechanical contracting — commercial work, and "
             "residential work outside the Commission's scope")],
    [k.cellp("<b>Credential threshold</b>"),
     k.cellp("Cost of the undertaking <b>exceeds&#160;$5,000</b> for a "
             "residential builder; <b>exceeds&#160;$500</b> for a residential "
             "specialty contractor"),
     k.cellp("Total cost of construction <b>greater than&#160;$10,000</b> for "
             f"general or for mechanical contracting ({sec('40-11-30')})")],
    [k.cellp("<b>The two-year rule</b>"),
     k.cellp("Selling, renting, or <i>offering</i> either within two years is "
             "prima facie evidence you built to sell — <b>unless otherwise "
             "approved by the commission</b>"),
     k.cellp("The same words, and the same two years — but <b>without</b> the "
             "commission-approval escape")],
    [k.cellp("<b>Who may do the work</b>"),
     k.cellp("You, your own employees, or licensed contractors and registered "
             "entities or individuals"),
     k.cellp("You, your own employees, or licensed contractors")],
]
flow.append(k.ref_table(
    "The residential exemption and its Chapter 11 twin",
    [k.cellp("", bold=True),
     k.cellp("Residential Builders Commission", bold=True),
     k.cellp("Contractor's Licensing Board", bold=True)],
    rows, [1.30 * inch, (CW - 1.30 * inch) / 2, (CW - 1.30 * inch) / 2]))
flow.append(k.cite(
    f"S.C. Code Ann. {sec('40-59-20')}, {sec('40-59-260')}, "
    f"{sec('40-11-30')}, {sec('40-11-360')}. The Chapter 11 threshold was "
    f"<b>raised from $5,000 to $10,000</b> by 2023 Act No.&#160;69, "
    f"{sec('3')}, effective 19&#160;May&#160;2023 — a source quoting $5,000 "
    f"for general contracting is pre-2023. {sec('40-59-270')} settles which "
    f"board owns you: “The commission is the exclusive licensing and "
    f"registration entity for persons who engage solely in residential "
    f"building and in residential specialty contracting.”"))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "One Chapter 11 rule that binds you even when you are exempt", [
        Paragraph(f"Section&#160;40-11-300(A) makes it unlawful “for an "
                  "<b>owner</b>, a construction manager, a prime contractor, "
                  "or another entity with contracting or hiring authority on "
                  "a construction project to divide work into portions so as "
                  "to avoid the financial or other requirements of this "
                  "chapter,” and says “The total cost of construction must be "
                  "used to determine the appropriate license group for a "
                  "project.” Splitting one $60,000 scope into six $9,000 "
                  "contracts to keep everyone under the Chapter 11 threshold "
                  "is the thing this sentence exists to forbid, and it names "
                  "the owner first.", S["body"]),
    ]))

# ---------------------------------------------------- the three conditions
flow += k.h2("THE THREE CONDITIONS, AND WHERE PEOPLE TRIP")
flow.append(k.bullet(
    "<b>You must be “an owner of residential property.”</b> The statute does "
    "not define owner and does not literally say the deed must be in your "
    "name — but the county forms operationalize it that way. Charleston "
    "County's affidavit asks you to print the “Name of Owner on the Deed.” If "
    "the lot is held by an LLC you control, raise it with the permit office "
    "<i>before</i> you file rather than at the counter."))
flow.append(k.bullet(
    "<b>Sole occupancy by you or your family, and not for sale or rent.</b> "
    "This is a statement about intent at the time you build, which is why the "
    "two-year rule exists to test it after the fact."))
flow.append(k.bullet(
    "<b>The general public may not have access to the structure.</b> The "
    "quiet condition. A house is fine; a house with a shopfront, a public "
    "studio, or a rentable event space in it is not obviously fine. If any "
    "part of your building is meant for customers, ask before you design "
    "around the exemption."))
flow.append(k.bullet(
    "<b>Condition (1) is a list of three labor sources, not a general "
    "permission.</b> You may do the work yourself, use your own employees, or "
    "use licensed contractors and registered entities or individuals. There "
    "is no fourth option. The exemption is about <i>your</i> license to "
    "build; it never becomes a license for the person you pay."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "The sentence that closes the “call him an employee” loophole", [
        Paragraph(f"Section&#160;40-59-260(B) ends: “This section does "
                  "not exempt a person who is employed by the owner and who "
                  "acts in the capacity of a builder or a specialty "
                  "contractor of any kind.” Putting an unlicensed builder on "
                  "your payroll does not import your exemption into him. And "
                  f"{sec('40-59-260')}(F) says it again from the other "
                  "direction: “Nothing in this chapter may be construed to "
                  "authorize an owner of a residential building or structure "
                  "to hire a person or entity that is not licensed or "
                  "registered in accordance with this chapter.”", S["body"]),
        Paragraph("Do not import the rule that applies to licensed builders. "
                  f"Section&#160;40-11-270(E) lets a <i>licensee</i> "
                  "“utilize the services of unlicensed subcontractors… "
                  "provided, the licensee provides supervision.” That "
                  "allowance runs to license holders. You are not one — you "
                  "are exempt from needing one, which is a different thing.",
                  S["body"]),
    ]))

# ----------------------------------------------------------- two-year rule
flow += k.h2("THE TWO-YEAR RULE: WHAT ACTUALLY TRIGGERS IT")
flow.append(k.body(
    "“In an action brought under this chapter, proof of the sale or rent or "
    "the offering for sale or rent of the structure by the owner-builder "
    "within two years after completion or issuance of a certificate or "
    "occupancy is prima facie evidence that the project was undertaken for "
    "the purpose of sale or rent, unless otherwise approved by the "
    "commission, and is subject to the penalties provided in this chapter.”"))
flow.append(k.cite(
    f"S.C. Code Ann. {sec('40-59-260')}(B), quoted exactly — “a certificate "
    f"or occupancy” is the Code's own wording."))
rows = [
    [k.cellp("<b>Offering counts</b>"),
     k.cellp("The clause reads “the sale or rent <b>or the offering for sale "
             "or rent</b>.” Listing the house inside the window is enough. "
             "You do not have to close.")],
    [k.cellp("<b>Renting counts, and “rent” is broad</b>"),
     k.cellp("“‘Sale’ or ‘rent’ includes an arrangement by which an owner "
             "receives compensation in money, provisions, chattel, <b>or "
             "labor</b> from the occupancy.” Letting someone live in the "
             "house in exchange for work on it is renting it.")],
    [k.cellp("<b>Two clocks, not one</b>"),
     k.cellp("The window runs “within two years after <b>completion or "
             "issuance of a certificate</b> of occupancy.” Those are usually "
             "different dates and the statute does not say which controls. "
             "Assume the earlier one starts it and the later one ends it.")],
    [k.cellp("<b>It is evidence, not a verdict</b>"),
     k.cellp("“Prima facie evidence” shifts the burden onto you; it does not "
             "decide the case. And the subsection carries an express escape: "
             "<b>“unless otherwise approved by the commission.”</b>")],
    [k.cellp("<b>The Chapter 11 twin has no escape</b>"),
     k.cellp(f"{sec('40-11-360')}(5) states the same two-year presumption in "
             "almost identical words and simply omits the "
             "commission-approval clause.")],
]
flow.append(k.ref_table(
    "Five things the two-year sentence actually says",
    [k.cellp("", bold=True), k.cellp("What it means for you", bold=True)],
    rows, [1.75 * inch, CW - 1.75 * inch]))
flow.append(k.cite(
    "The commission-approval route is real but undocumented: no published "
    "procedure, form or fee for it appears in the statute or in the "
    "Commission's regulations. If you can foresee a reason you may have to "
    "sell inside two years — a job transfer, a health change — raise it with "
    "the Residential Builders Commission in writing early, and keep the "
    "answer. Do not assume approval is routine."))

# -------------------------------------------------------- the disclosure
flow += k.h2("THE DISCLOSURE STATEMENT YOU WILL SIGN")
flow.append(k.body(
    "Two things happen at the counter, and the statute makes them conditions "
    "of the exemption rather than courtesies. First: <b>“To qualify for "
    "exemption under this section, an owner must personally appear and sign "
    "the building permit application.”</b> Not your designer, not your "
    "spouse with a power of attorney, not a scanned signature. Second: the "
    "local permitting agency “shall provide the person with a disclosure "
    "statement, provided by the department, in substantially the following "
    f"form” — and then {sec('40-59-260')}(C) prints the form. Here it is, "
    "word for word."))
flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "Disclosure Statement — the statutory text", [
        Paragraph("“State law requires residential construction to be done by "
                  "licensed residential builders and specialty contractors. "
                  "You have applied for a permit under an exemption to that "
                  "law. The exemption allows you, as the owner of your "
                  "property, to act as your own builder even though you do "
                  "not have a license.", S["body"]),
        Paragraph("You must supervise the construction yourself. You may "
                  "build or improve a one-family or two-family residence. The "
                  "building must be for your own use and occupancy. It may "
                  "not be built for sale or rent. If you sell or rent a "
                  "building you have built yourself within two years after "
                  "the construction is complete, the law will presume that "
                  "you built it for sale or rent, which is a violation of "
                  "this exemption.", S["body"]),
        Paragraph("You may not hire an unlicensed person as your residential "
                  "builder or specialty contractor. It is your responsibility "
                  "to make sure that people employed by you have licenses "
                  "required by state law and by county or municipal licensing "
                  "ordinances. Your construction must comply with all "
                  "applicable laws, ordinances, building codes, and zoning "
                  "regulations.”", S["body"]),
    ]))
flow.append(Spacer(1, 3))
flow.append(k.callout(
    "Two limits that appear only in the disclosure", [
        Paragraph("Read the two texts side by side and the disclosure is "
                  f"<i>narrower</i> than the statute it summarizes. "
                  f"Subsection (A) exempts an owner improving “the structure, "
                  f"group of structures, or appurtenances.” The disclosure "
                  f"says “You may build or improve a <b>one-family or "
                  f"two-family residence</b>.” Subsection (A) says nothing "
                  f"about supervision. The disclosure says “You must "
                  f"<b>supervise the construction yourself</b>.” Neither "
                  f"limit is reconciled anywhere in {sec('40-59-260')}, and "
                  f"the disclosure is the document you sign.", S["body"]),
        Paragraph("Counties may reword it — the statute only requires "
                  "“substantially the following form.” Charleston County's "
                  "version adds “direct, on-site supervision,” a bar on "
                  "delegating supervision to an unlicensed contractor, and a "
                  "carve-out stating that homeowners cannot pull permits for "
                  "work on a manufactured home. Ask your own office for its "
                  "form and read what you are actually signing.", S["body"]),
    ]))

# ------------------------------------------------- the register of deeds
flow += k.h2("THE NOTICE THAT KEEPS YOUR EXEMPTION ALIVE")
flow.append(k.body(
    "This is the obligation South Carolina owner-builders miss, and it is the "
    "only one in the statute with a self-executing penalty:"))
flow.append(k.body(
    "“If a residential building or structure has been constructed by an owner "
    "under the exemption provided for in this section, the owner of the "
    "residential building or structure <b>must promptly file as a matter of "
    "public record a notice with the register of deeds, indexed under the "
    "owner's name in the grantor's index</b>, stating that the residential "
    "building or structure was constructed by the owner as an unlicensed "
    "builder. <b>Failure to do so revokes the statutory exemption.</b>”"))
flow.append(k.cite(f"S.C. Code Ann. {sec('40-59-260')}(E)."))
flow.append(k.body(
    "There is no fine and no notice period. The consequence is that the "
    "exemption you built the house under stops applying — which puts you, "
    "retrospectively, in the position of someone who did residential building "
    f"without a license. {sec('40-59-30')}(A) makes that a misdemeanor "
    "carrying a fine of not less than $500 and not more than $10,000, or "
    "imprisonment of not less than thirty days, or both."))
flow.append(k.body(
    "Two practical notes. The statute says <b>“promptly”</b> and gives no day "
    f"count. And you should not have to hunt for the paperwork: "
    f"{sec('40-59-260')}(D) obliges the permitting agency, “At the time an "
    f"owner personally appears and signs the building permit application,” to "
    f"“provide the owner with all forms necessary to comply with subsection "
    f"(E).” <b>Ask for those forms while you are standing there.</b> Some "
    f"counties fold the whole thing into permit issuance — Charleston "
    f"County's notice is executed and recorded as a condition of approving "
    f"the permit application, which turns a post-construction filing into a "
    f"pre-permit one. Ask yours which way it runs, and write the answer "
    f"down."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "What the notice does to a future sale", [
        Paragraph("The notice is indexed in the <b>grantor's index</b> under "
                  "your name, which is exactly where a buyer's title search "
                  "looks. That is the point of it: the public record will say "
                  "the house was built by an unlicensed builder. Plan for a "
                  "buyer to ask about it, and keep your permit card, "
                  "inspection results and certificate of occupancy together "
                  "as the answer.", S["body"]),
    ]))

# ------------------------------------------------------ who you may pay
flow += k.h2_tight("WHO YOU MAY PAY: THREE THRESHOLDS", reserve=2.2)
flow.append(k.body(
    "Every guide to South Carolina prints $5,000. It is the right number for "
    "exactly one question. Here are all three, in the order you will meet "
    "them on a job site."))
rows = [
    [k.cellp("<b>$500</b>", center=True),
     k.cellp("<b>Residential specialty contractor</b>"),
     k.cellp("A person doing specialized trade work “when the undertakings "
             "<b>exceed five hundred dollars</b>” needs a specialty license "
             "or registration. This is the number that decides whether your "
             "tile setter, drywall hanger, mason or painter is legal. Raised "
             "from $200 by 2022 Act No.&#160;186."),
     k.cellp(f"{sec('40-59-20')}(7)")],
    [k.cellp("<b>$5,000</b>", center=True),
     k.cellp("<b>Residential builder</b>"),
     k.cellp("Someone who “constructs, superintends, or offers to construct "
             "or superintend” the work needs a builder license “when the cost "
             "of the undertaking <b>exceeds five thousand dollars</b>.” This "
             "is the license <i>you</i> are exempt from."),
     k.cellp(f"{sec('40-59-20')}(6)")],
    [k.cellp("<b>$10,000</b>", center=True),
     k.cellp("<b>General or mechanical contractor</b>"),
     k.cellp("Chapter 11 licensure bites when the total cost of construction "
             "is “<b>greater than ten thousand dollars</b>” for general or "
             "for mechanical contracting. Mechanical includes commercial "
             "electrical and plumbing."),
     k.cellp(f"{sec('40-11-30')}")],
]
flow.append(k.ref_table(
    "Three thresholds, two chapters",
    [k.cellp("Over", bold=True), k.cellp("Triggers", bold=True),
     k.cellp("What the statute says", bold=True), k.cellp("Cite", bold=True)],
    rows, [0.92 * inch, 1.50 * inch, CW - 3.57 * inch, 1.15 * inch]))
flow.append(k.cite(
    "A second $5,000 exists and is a different rule: a licensed residential "
    "specialty contractor whose undertaking for a property owner exceeds "
    "$5,000 must carry a surety bond approved by the Commission "
    f"({sec('40-59-240')}(D), and Regulation 106-2 sets it at not less than "
    f"$10,000). Bonds run $15,000 for a residential builder, $10,000 for a "
    f"specialty licensee and $5,000 for a specialty registrant."))

# --------------------------------------------------------- the trades
flow += k.h2_tight("WHICH TRADES NEED WHICH CREDENTIAL", reserve=2.2)
flow.append(k.body(
    "South Carolina splits residential trades into <b>licenses</b>, which "
    "require passing an examination, and <b>registrations</b>, which do not. "
    "Three trades are licensed. Everything else on the list is registered. "
    "Both are issued by the Residential Builders Commission, so both are "
    "checkable in one place."))
rows = [
    [k.cellp("<b>License, by examination</b>"),
     k.cellp("Plumbers · Electricians · Heating and air conditioning "
             "installers and repairers"),
     k.cellp("Examination required since 1&#160;July&#160;2004. The "
             "residential HVAC classification is capped by regulation at "
             "<b>five tons cooling and 175,000&#160;BTU/HR heating per "
             "unit</b> — a bigger unit is Chapter 11 work.")],
    [k.cellp("<b>Registration, no examination</b>"),
     k.cellp("Masons · Carpenters · Roofers · Dry wall installers · "
             "Insulation installers · Floor covering installers · Vinyl and "
             "aluminum siding installers · Stucco installers · Painters and "
             "wall paperers · Solar panel installers"),
     k.cellp("Registration still means a credential on file, a bond, and a "
             "credit report. “Masons” is the classification that covers "
             "<b>poured-in-place concrete foundations, footings and "
             "reinforced slabs</b> — your footing sub is a mason here, not a "
             "carpenter.")],
]
flow.append(k.ref_table(
    "Residential specialty classifications",
    [k.cellp("", bold=True), k.cellp("Trades", bold=True),
     k.cellp("What to know", bold=True)],
    rows, [1.45 * inch, 2.35 * inch, CW - 3.80 * inch]))
flow.append(k.cite(
    f"S.C. Code Ann. {sec('40-59-20')}(7) and S.C. Code of Regulations "
    f"106-1 and 106-2. Two limits worth knowing before you build a schedule: "
    f"a specialty contractor “is not authorized to construct additions to "
    f"residential buildings or structures without supervision by a "
    f"residential builder,” and is “prohibited from undertaking work outside "
    f"the scope of his license or registration, including employing, hiring, "
    f"and contracting or subcontracting with others to perform such work on "
    f"his behalf” — so your tile setter may not sub out your drywall. A "
    f"registrant may hold no more than <b>three</b> classifications "
    f"({sec('40-59-240')}(A)); wanting a fourth means sitting the builder "
    f"examination."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "Doing your own wiring and plumbing: a county question, not a state one",
    [
        Paragraph(f"Section&#160;40-59-260(A) removes Chapter 59 from “an "
                  "owner… who improves the property… if the owner does the "
                  "work himself.” On its face that includes the specialty "
                  "license requirement, so the state licensing statute does "
                  "not stand between you and your own wiring.", S["body"]),
        Paragraph("What it does not remove is the permit, the code or the "
                  "inspection — the disclosure you sign says so in terms. And "
                  "the practical gate is local: your building department "
                  "decides what it will issue a homeowner trade permit for, "
                  "and your utility decides what it will connect. Charleston "
                  "County, for one, publishes a carve-out barring homeowners "
                  "from pulling permits for work on a manufactured home. "
                  "<b>Ask your office before you plan a schedule around "
                  "owner-performed trade work, and write the answer on "
                  "SC.4.</b>", S["body"]),
    ]))

# ---------------------------------------------------- hiring protections
flow += k.h2("IF YOU HIRE ANYONE: FOUR PROTECTIONS AND ONE DEADLINE")
flow.append(k.body(
    "Checking a license is usually framed as a duty. In South Carolina it is "
    "also leverage, because the statutes attach real consequences to the "
    "unlicensed that work in your favor as the owner."))
rows = [
    [k.cellp("<b>An unlicensed sub cannot lien you, and cannot sue you</b>"),
     k.cellp("“Notwithstanding Section 29-5-10, or another provision of law, "
             "a person or firm who first has not procured a license or "
             "registered with the commission and is required to do so by law "
             "<b>may not file a mechanics' lien or bring an action at law or "
             "in equity to enforce the provisions of a contract</b> for "
             "residential building or residential specialty contracting.”"),
     k.cellp(f"{sec('40-59-30')}(B)")],
    [k.cellp("<b>The license number goes on the lien itself</b>"),
     k.cellp("A contractor filing a lien “must record his contractor license "
             "number or registration number on the lien document.” A lien "
             "with no number on it is a lien to question."),
     k.cellp(f"{sec('29-5-15')}(A)")],
    [k.cellp("<b>A frivolous lien is expensive for the filer</b>"),
     k.cellp("“A contractor who files a frivolous lien is subject to a fine "
             "up to <b>five thousand dollars</b>, the loss of his "
             "registration or contractor license, or both.”"),
     k.cellp(f"{sec('29-5-15')}(B)")],
    [k.cellp("<b>Winning against a lien pays your lawyer</b>"),
     k.cellp("“If the party defending against the lien prevails, the "
             "defending party <b>must</b> be awarded costs of the action and "
             "a reasonable attorney's fee.” Capped at the amount of the "
             "lien. The fee shift runs both ways in South Carolina."),
     k.cellp(f"{sec('29-5-20')}(A)")],
    [k.cellp("<b>But the clock is short, and it is theirs</b>"),
     k.cellp("A lien dissolves unless, <b>within ninety days</b> of ceasing "
             "work, the claimant both serves you and files a sworn statement "
             "of account — and dissolves again unless suit is commenced and "
             "a notice of pendency filed <b>within six months</b>."),
     k.cellp(f"{sec('29-5-90')}, {sec('29-5-120')}(A)")],
]
flow.append(k.ref_table(
    "What the lien statutes give an owner-builder",
    [k.cellp("", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.95 * inch, CW - 3.15 * inch, 1.20 * inch]))
flow.append(k.cite(
    f"Title 29, Chapter 5, S.C. Code Ann. {sec('29-5-40')} caps the whole "
    f"exposure: “in no event shall the aggregate amount of liens set up "
    f"hereby exceed the amount due by the owner on the contract price of the "
    f"improvement made.” And {sec('29-5-80')} lets an owner head off a lien "
    f"for work not yet done “by giving notice, in writing, to the person "
    f"performing or furnishing such labor… that he will not be responsible "
    f"therefor.”"))

flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "$15 and fifteen days: the filing almost nobody makes", [
        Paragraph(f"Section&#160;29-5-23 lets a person who has a direct "
                  "agreement with, or the consent of, an owner file a "
                  "<b>Notice of Project Commencement</b> with the clerk of "
                  "court or register of deeds. It must be filed “within "
                  "fifteen days of the commencement of work” with “a filing "
                  "fee of fifteen dollars,” and a location notice must be "
                  "posted at the job site carrying wording the statute "
                  "prescribes.", S["body"]),
        Paragraph("Why it matters to you: the cap in "
                  f"{sec('29-5-20')}(B) — which stops a supplier to one of "
                  "your subs from claiming a lien against you for more than your sub was "
                  "owed — only operates if that notice exists. The statute is "
                  "blunt about it: “The failure to file a notice of project "
                  "commencement shall render the provisions of Sections "
                  "29-5-20(B) and 29-5-60(B) inapplicable.” Filing it also "
                  "“shall not constitute a cloud, lien, or encumbrance upon, "
                  "or defect to, the title.”", S["body"]),
        Paragraph("<b>The honest caveat:</b> the section is drafted for a "
                  "contractor-led job — the posted notice literally begins "
                  "“The contractor on the project has filed…” — and it does "
                  "not say in terms whether an owner acting as their own "
                  "builder files it in their own name. Ask the clerk of court "
                  "or register of deeds for your county how they take it, "
                  "before your fifteen days run out.", S["body"]),
    ]))

# ------------------------------------------------------- workers' comp
flow += k.h2_tight("WORKERS' COMPENSATION", reserve=2.0)
flow.append(k.body(
    "South Carolina's coverage test is <b>disjunctive</b>, and both halves "
    "matter. The Act does not apply to “any person who has regularly employed "
    "in service <b>less than four employees</b> in the same business within "
    "the State <b>or</b> who had a total annual payroll during the previous "
    "calendar year of <b>less than three thousand dollars</b> regardless of "
    "the number of persons employed during that period.”"))
flow.append(k.cite(
    f"S.C. Code Ann. {sec('42-1-360')}(2). The Workers' Compensation "
    f"Commission counts part-time workers and family members as employees. "
    f"It also does not issue exemption certificates — its own guidance says "
    f"the Commission “does not certify that employers are not subject to the "
    f"Act,” so any exemption affidavit a permit office asks for is a form "
    f"that office wrote, not a state one."))
flow.append(k.bullet(
    "<b>Opting in is stickier than opting out.</b> An exempt employer who "
    f"elects coverage comes under the Act thirty days after written notice "
    f"({sec('42-1-380')}), and stops being liable only sixty days after "
    f"written notice of withdrawal ({sec('42-1-390')})."))
flow.append(k.bullet(
    "<b>Read the statutory-employer section before you count heads.</b> "
    f"Section&#160;42-1-400 makes an “owner” who “undertakes to perform "
    "or execute any work <b>which is a part of his trade, business or "
    "occupation</b>” and subcontracts it liable to a subcontractor's workman "
    "as if he had employed them directly. Whether that reaches a homeowner "
    "building one house for themselves turns on that quoted phrase, and it is "
    "a question decided case by case — the Commission's own guidance answers "
    "the general version with “Maybe.”"))

# ----------------------------------------------------------- checklist
flow += k.h2_tight("BEFORE YOU GO TO THE COUNTER", reserve=2.0)
flow += k.check_table(
    "Work this with a pen",
    [
        ("Confirmed the property is in the name you will sign under, and how "
         "your office treats a lot held by an entity", []),
        ("Booked time to appear in person — the exemption requires it, and "
         "nobody may sign for you", []),
        ("Asked the permit office for its owner-builder disclosure form and "
         "read it (it may be narrower than the statute)",
         [("Form name", 0.5), ("Date", 0.5)]),
        ("Asked for the register-of-deeds forms at the same visit, as "
         f"{sec('40-59-260')}(D) requires — and established whether your "
         "county records the notice before the permit or after completion",
         [("Which", 0.6), ("Date", 0.4)]),
        ("Established whether your county lets a homeowner pull electrical, "
         "plumbing and mechanical permits, and on what terms", []),
        ("Listed every trade you intend to pay more than $500 and checked "
         "each credential with the Residential Builders Commission", []),
        ("Decided whether a Notice of Project Commencement will be filed, "
         "and by whom, inside fifteen days of starting work",
         [("Who files", 0.6), ("Date", 0.4)]),
        ("Counted employees against the four-employee and $3,000-payroll "
         "workers' compensation tests", []),
        ("Written the exemption cite on the application if the form asks for "
         f"authority: {sec('40-59-260')}", []),
    ])

# ------------------------------------------------------------- sources
flow += k.h2_tight("SOURCES", reserve=2.0)
flow.append(k.sources_table([
    ("The owner-builder exemption, its three conditions, the disclosure "
     "statement and the register-of-deeds notice",
     f"S.C. Code Ann. {sec('40-59-260')}"),
    ("Unlicensed practice is a misdemeanor; an unlicensed person may not "
     "lien or sue on the contract",
     f"S.C. Code Ann. {sec('40-59-30')}"),
    ("Residential builder $5,000; residential specialty $500; the "
     "thirteen specialty classifications and the license/registration split",
     f"S.C. Code Ann. {sec('40-59-20')}(6), (7)"),
    ("Maximum three specialty classifications; bond above $5,000; counties "
     "may license but may not re-examine",
     f"S.C. Code Ann. {sec('40-59-240')}"),
    ("The Commission is the exclusive licensing entity for residential work",
     f"S.C. Code Ann. {sec('40-59-270')}"),
    ("The building official must refuse a permit absent license, "
     "registration or exemption",
     f"S.C. Code Ann. {sec('40-59-280')}"),
    ("Scope of each specialty classification; the five-ton and "
     "175,000&#160;BTU/HR residential HVAC cap; which three trades are "
     "licensed by examination",
     "S.C. Code of Regs. 106-1, 106-2"),
    ("Chapter 11 threshold of $10,000; the owner exemption twin; the "
     "anti-splitting rule that binds owners",
     f"S.C. Code Ann. {sec('40-11-30')}, {sec('40-11-300')}, "
     f"{sec('40-11-360')}"),
    ("Mechanics' liens: license number on the lien, frivolous-lien fine, "
     "two-way fee shift, ninety days, six months, owner's cap, notice of "
     "nonresponsibility",
     f"S.C. Code Ann. {sec('29-5-15')}, {sec('29-5-20')}, {sec('29-5-40')}, "
     f"{sec('29-5-80')}, {sec('29-5-90')}, {sec('29-5-120')}"),
    ("Notice of Project Commencement — fifteen days, $15, and what failing "
     "to file costs the owner",
     f"S.C. Code Ann. {sec('29-5-23')}"),
    ("Workers' compensation: fewer than four employees or under $3,000 "
     "payroll; election and withdrawal; statutory employer",
     f"S.C. Code Ann. {sec('42-1-360')}, {sec('42-1-380')}, "
     f"{sec('42-1-390')}, {sec('42-1-400')}"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "sc-permit-kit",
                       "SC.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
