#!/usr/bin/env python3
"""PA.1 Who Inspects Your House.

Every other state's document 1 in this series walks an owner-builder exemption:
the paragraph that lets you act as your own contractor, and the conditions
attached to it. Pennsylvania has no such paragraph, because it has no state
contractor license to be exempt FROM. L&I says so on its own contractor
licensing page, in one sentence.

So the document that earns its place here answers the question Pennsylvania
actually poses, which no other state in the program poses in the same form:
the code applies to your house no matter where you build, five inspections are
required no matter where you build, and yet in a large minority of
municipalities NOBODY IS ASSIGNED TO DO THEM. 35 P.S. § 7210.501(e)(1) moves
that duty onto the permit applicant by name. An owner who never reads that
sentence builds an uninspected house, which is not illegal and is not a
problem until the day he tries to sell, insure or refinance it.

The order of the document follows the order the decisions arrive: is my
project inside the code at all (§ 7210.104(b), and the recreational cabin
test that is the one real way out) → how does my municipality handle
enforcement (the five paths of § 7210.501(b) plus the sixth non-path) → what
do I do in the opt-out case → what credentials does anyone need (none from the
state) → what the local ones actually are.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

import kit as k

S = k.S
CW = k.CW

FORM_ID = "PA.1"
FORM_TITLE = "Who Inspects Your House"
TOPIC = "Who Inspects"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Whether the Uniform Construction Code reaches your project, who is "
    "responsible for enforcing it where you are building, and what you must "
    "do if the answer is nobody yet.")
flow.append(k.disclaimer())

flow.append(k.body(
    "Start with the sentence that settles the question most guides spend a "
    "page hedging. The Pennsylvania Construction Code Act applies to "
    "“<b>the construction, alteration, repair and occupancy of all buildings "
    "in this Commonwealth</b>” (35&nbsp;P.S. §&nbsp;7210.104(a)). There is no "
    "rural exception, no acreage exception and no county that has escaped it. "
    "If you are building a house in Pennsylvania, the Uniform Construction "
    "Code (UCC) is the code it must meet."))
flow.append(k.body(
    "What varies — and it varies enormously — is <b>who administers and "
    "enforces that code on your lot</b>. The Act hands each municipality a "
    "menu, and one of the choices is to decline the job altogether. Where a "
    "municipality has declined, the code still binds your house and the "
    "required inspections still have to happen; the difference is that the "
    "Commonwealth has assigned the duty of going out and hiring an inspector "
    "to <b>you</b>."))
flow.append(k.callout(
    "The error this document exists to correct", [
        Paragraph("“Opting out” is the single most misreported fact in "
                  "Pennsylvania homebuilding. It does not mean the code stops "
                  "applying, and it does not mean the inspections stop. It "
                  "means the municipality is not running the program — so "
                  "there is no office to call, no permit desk to walk into, "
                  "and no one who will notice that your house was never "
                  "inspected until a buyer's lender, a title company or an "
                  "insurance underwriter asks for the certificate of "
                  "occupancy you never obtained.", S["body"]),
    ]))

# ------------------------------------------------------------------ scope
flow += k.h2_tight("FIRST: IS YOUR PROJECT INSIDE THE CODE AT ALL", 2.0)
flow.append(k.body(
    "A short list of construction sits outside the UCC entirely. This is the "
    "real exemption list in Pennsylvania, and it is worth reading before you "
    "assume your project is on it — most of it is accessory and agricultural "
    "work, not houses."))

rows = [
    [k.cellp("<b>Accessory structures</b>"),
     k.cellp("Carports, detached private garages, greenhouses and sheds, "
             "<b>if</b> the building area is under 1,000&nbsp;sq&nbsp;ft and "
             "the structure is accessory to a detached one-family dwelling. "
             "A municipal ordinance may still reach it."),
     k.cellp("34 Pa. Code<br/>§&nbsp;403.1(b)(3)")],
    [k.cellp("<b>Agricultural buildings</b>"),
     k.cellp("Excluded outright. The Act defines the term, and a building "
             "used for a dwelling is not one."),
     k.cellp("35 P.S.<br/>§&nbsp;7210.104(b)(4)")],
    [k.cellp("<b>Recreational cabins</b>"),
     k.cellp("Excluded if the structure meets a seven-part definition "
             "<b>and</b> the owner files an affidavit or proof of insurance "
             "with the municipality. See the box below — the test is "
             "strict."),
     k.cellp("35 P.S.<br/>§&nbsp;7210.104(b)(7)")],
    [k.cellp("<b>On-lot sewage systems</b>"),
     k.cellp("Not a UCC subject at all. Your septic system is governed by 25 "
             "Pa. Code Chapter 73 and permitted by a sewage enforcement "
             "officer, on a separate track. See PA.4."),
     k.cellp("34 Pa. Code<br/>§&nbsp;403.21(e)")],
    [k.cellp("<b>Repairs and most alterations</b>"),
     k.cellp("Repairs to residential buildings, and alterations that make no "
             "structural change and no change to means of egress. Replacing "
             "a window or door is expressly not a structural change."),
     k.cellp("35 P.S.<br/>§&nbsp;7210.104(b)(5), (6)")],
    [k.cellp("<b>Propane fuel systems</b>"),
     k.cellp("Tubing, piping, appliances, equipment and fixtures for "
             "liquefied petroleum gas are regulated under their own act, not "
             "the UCC."),
     k.cellp("34 Pa. Code<br/>§&nbsp;403.1(b)(6)")],
    [k.cellp("<b>Manufactured housing</b>"),
     k.cellp("Units shipped from the factory under § 7210.901(a) are handled "
             "under § 403.25, not as site-built construction."),
     k.cellp("34 Pa. Code<br/>§&nbsp;403.1(b)(5)")],
]
flow.append(k.ref_table(
    "Construction the UCC does not reach",
    [k.cellp("Category", bold=True), k.cellp("What the exclusion covers",
                                             bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.35 * inch, CW - 3.0 * inch, 1.65 * inch]))
flow.append(Spacer(1, 6))

flow.append(k.callout_long(
    "The recreational cabin test — all seven parts must be true", [
        Paragraph("A “recreational cabin” is excluded from the Act "
                  "altogether, which makes it the one genuine way to build a "
                  "structure in Pennsylvania with no UCC permit and no UCC "
                  "inspections. The definition at 35&nbsp;P.S. "
                  "§&nbsp;7210.103 is deliberately narrow, and every part of "
                  "it has to hold. A structure which is:", S["body"]),
        Paragraph("(1) utilized principally for recreational activity; "
                  "(2)&nbsp;not utilized as a domicile or residence for any "
                  "individual for any time period; (3)&nbsp;not utilized for "
                  "commercial purposes; (4)&nbsp;not greater than two stories "
                  "in height, excluding basement; (5)&nbsp;not utilized by "
                  "the owner or any other person as a place of employment; "
                  "(6)&nbsp;not a mailing address for bills and "
                  "correspondence; and (7)&nbsp;not listed as an individual's "
                  "place of residence on a tax return, driver's license, car "
                  "registration or voter registration.", S["body"]),
        Paragraph("<b>Read part (2) carefully before you plan around this.</b> "
                  "A cabin you sleep in on weekends is still not a domicile; "
                  "a cabin you move into while you build the real house is. "
                  "The exclusion is not self-executing either: under "
                  "§&nbsp;7210.104(b)(7)(ii) the owner must file with the "
                  "municipality <b>either</b> an affidavit on the "
                  "Department's prescribed form attesting that the structure "
                  "meets the definition, <b>or</b> valid proof of insurance "
                  "from an insurer authorized to do business in Pennsylvania "
                  "stating the same thing. File nothing and you have not "
                  "claimed the exclusion.", S["body"]),
    ]))
flow.append(Spacer(1, 8))

# ------------------------------------------------------- the six paths
flow += k.h2_tight("THE SIX WAYS A MUNICIPALITY HANDLES THE CODE", 2.2)
flow.append(k.body(
    "Section 7210.501(b) gives a municipality that has adopted the enforcing "
    "ordinance five ways to run the program. Section 7210.501(e) covers the "
    "sixth case — the municipality that never adopted one. <b>One phone call "
    "to the municipal office tells you which of these you are in, and it is "
    "the most valuable call you will make all year.</b>"))

rows = [
    [k.cellp("<b>1</b>"), k.cellp("Its own employee"),
     k.cellp("The municipality designates an employee as its municipal code "
             "official. You deal with a township, borough or city office.")],
    [k.cellp("<b>2</b>"), k.cellp("A retained third-party agency"),
     k.cellp("The municipality retains one or more code officials or private "
             "agencies to act <i>on its behalf</i>. You still apply at the "
             "municipal office; the inspector arrives from a company. "
             "<b>The municipality chose and pays them, not you.</b>")],
    [k.cellp("<b>3</b>"), k.cellp("A joint program with neighbors"),
     k.cellp("Two or more municipalities administer the code together under "
             "an intergovernmental agreement. Your permit may be issued from "
             "the next township over.")],
    [k.cellp("<b>4</b>"), k.cellp("A contract with another municipality"),
     k.cellp("One municipality buys the service from another. That "
             "municipality's code official then holds full authority in "
             "yours.")],
    [k.cellp("<b>5</b>"), k.cellp("An agreement with L&amp;I"),
     k.cellp("Available only for buildings <i>other than</i> one- and "
             "two-family dwellings. <b>The Department does not review or "
             "inspect houses under this option</b>, which is why L&amp;I is "
             "not the answer for your project."),
     ],
    [k.cellp("<b>6</b>"), k.cellp("<b>Elected not to administer</b>"),
     k.cellp("The municipality adopted no enforcing ordinance. There is no "
             "municipal building department for the UCC. <b>You</b> must "
             "obtain the services of a certified third-party agency for plan "
             "review and inspections. The next section is entirely about "
             "this case.")],
]
flow.append(k.ref_table(
    "How enforcement is arranged — 35 P.S. §§ 7210.501(b) and 7210.501(e)",
    [k.cellp("", bold=True), k.cellp("Arrangement", bold=True),
     k.cellp("What it means for you", bold=True)],
    rows, [0.4 * inch, 1.85 * inch, CW - 2.25 * inch]))
flow.append(Spacer(1, 6))
flow.append(k.cite(
    "Paths 1–5 are 35 P.S. § 7210.501(b)(1)–(5). Path 6 is 35 P.S. "
    "§ 7210.501(e)(1) and 34 Pa. Code § 403.103. Note the asymmetry in "
    "path 5: § 7210.501(b)(5) lets a municipality contract with the "
    "Department only for “structures other than one-family or two-family "
    "dwelling units and utility and miscellaneous use structures.”"))
flow.append(Spacer(1, 8))

# --------------------------------------------------------------- opt-out
flow += k.h2_tight("IF YOUR MUNICIPALITY ELECTED NOT TO ADMINISTER", 2.2)
flow.append(k.body(
    "This is the case the rest of the internet gets wrong, so here is the "
    "regulation itself. 34&nbsp;Pa. Code §&nbsp;403.103(b), in full:"))
flow.append(k.callout(
    "34 Pa. Code § 403.103(b)", [
        Paragraph("“An applicant for a residential building permit shall "
                  "obtain the services of a third-party agency certified in "
                  "the appropriate categories to conduct the plan review and "
                  "inspections under §§&nbsp;403.61—403.66 (relating to "
                  "permit and inspection process for residential "
                  "buildings).”", S["body"]),
    ]))
flow.append(k.body(
    "Three things follow from that sentence, and each of them costs money or "
    "time if you learn it late."))
flow.append(k.bullet(
    "<b>The inspection requirements do not change.</b> The cross-reference is "
    "to §§ 403.61—403.66 — the same sections that govern a house in a "
    "municipality with a full building department. Same code, same five "
    "inspections, same certificate of occupancy. The statute is explicit "
    "about the list even in the opt-out case: 35 P.S. § 7210.501(e)(1) names "
    "foundation; plumbing, mechanical and electrical; frame and masonry; "
    "wallboard; and final."))
flow.append(k.bullet(
    "<b>The agency does your plan review too, not just your inspections.</b> "
    "So it has to be engaged before you build, not when you are ready for a "
    "footing inspection. A certified agency is a private business with no "
    "obligation to take your job."))
flow.append(k.bullet(
    "<b>L&amp;I is not your fallback.</b> Under § 403.103(g) the Department "
    "picks up buildings <i>other than</i> residential in an opt-out "
    "municipality — commercial work, in practice. L&amp;I's own UCC page puts "
    "it plainly: “Certified third party agencies hired by property owners (or "
    "their contractors) enforce the residential requirements of the UCC in "
    "all opt-out municipalities.”"))

flow.append(Spacer(1, 4))
flow += k.check_table(
    "If you are in an opt-out municipality — do these in order", [
        "Confirm in writing that the municipality has not adopted a UCC "
        "enforcement ordinance. Ask for the notice § 7210.501(e)(1) requires "
        "the municipality to give you.",
        "Ask the municipality which local permits it <i>does</i> still issue "
        "— zoning, driveway, stormwater and sewage are municipal and are "
        "unaffected by the UCC election.",
        "Obtain L&amp;I's list of certified third-party agencies and identify "
        "those serving your county (see PA.4).",
        "Confirm the agency is certified in the categories your job needs — "
        "the regulation says “certified in the appropriate categories,” and "
        "the categories are separate for building, electrical, plumbing and "
        "mechanical.",
        "Get a written scope and fee: plan review, the five inspections, "
        "re-inspection charges, and who issues the certificate of occupancy.",
        "Confirm the agency has no financial interest in your project — a "
        "code administrator may not review or approve work in which he has "
        "one (35 P.S. § 7210.502(c)).",
        "Confirm the agency will send the final inspection report to you, "
        "your builder and your lender, and file the certificate of occupancy "
        "with the municipality (34 Pa. Code §§ 403.103(f), 403.65(e)).",
    ], notes_header="Confirmed with / notes")

# ------------------------------------------------------------- licensing
flow += k.h2_tight("WHAT NOBODY CAN ASK YOU FOR: A CONTRACTOR LICENSE", 2.0)
flow.append(k.body(
    "Pennsylvania issues no general contractor license of any kind — not to "
    "you, and not to the people you hire. The Department of Labor &amp; "
    "Industry states it in one sentence on its own contractor licensing page: "
    "“<b>The Commonwealth of Pennsylvania currently has no licensure or "
    "certification requirements for most construction contractors (or their "
    "employees).</b>” There is no owner-builder exemption in Pennsylvania "
    "because there is nothing to be exempt from."))
flow.append(k.body(
    "The one state registration that touches residential work is the Home "
    "Improvement Consumer Protection Act (HICPA), administered by the Office "
    "of Attorney General — and it reaches neither your project nor you. Two "
    "separate exclusions do the work, and it is worth knowing which is which:"))

rows = [
    [k.cellp("<b>Your new house is not a “home improvement”</b>"),
     k.cellp("The definition lists what counts — repair, replacement, "
             "remodeling, and so on — and then says the term “does not "
             "include … <b>the construction of a new home</b>.” So HICPA "
             "does not apply to the build itself, and a contractor framing "
             "your new house is not doing home improvement work."),
     k.cellp("73 P.S.<br/>§&nbsp;517.2, def.<br/>(2)(i)")],
    [k.cellp("<b>Your own labor is not covered either</b>"),
     k.cellp("The term also excludes “any work performed without "
             "compensation by the owner of the owner's private residence or "
             "residential rental property.” You are not a contractor when "
             "you work on your own house."),
     k.cellp("73 P.S.<br/>§&nbsp;517.2, def.<br/>(2)(v)")],
    [k.cellp("<b>And the small-volume floor</b>"),
     k.cellp("A person whose home improvements totaled less than "
             "$5,000 in the previous taxable year is outside the definition "
             "of “contractor” entirely — worth knowing when you check a "
             "small sub's registration and find none."),
     k.cellp("73 P.S.<br/>§&nbsp;517.2, def.<br/>of “contractor” (1)")],
]
flow.append(k.ref_table(
    "Why HICPA registration is not part of your build",
    [k.cellp("Exclusion", bold=True), k.cellp("What the statute says",
                                              bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.75 * inch, CW - 3.35 * inch, 1.6 * inch]))
flow.append(Spacer(1, 6))
flow.append(k.callout(
    "The trap inside the good news", [
        Paragraph("Because your project is outside HICPA, none of HICPA's "
                  "protections come with it. On a remodel the statute would "
                  "hand you a written contract with mandatory terms, a "
                  "capped deposit and a registered, insured counterparty. On "
                  "your new house you get none of that by operation of law — "
                  "you get whatever you negotiate. The next table is the "
                  "remedy: these are the terms the Commonwealth thought "
                  "important enough to compel on a $6,000 bathroom, and "
                  "there is no reason to accept less on a $60,000 framing "
                  "package.", S["body"]),
    ]))

flow += k.h2_tight("THE HICPA TERMS TO COPY INTO YOUR OWN SUBCONTRACTS", 2.0)
rows = [
    [k.cellp("Deposit cap"),
     k.cellp("On a contract over $5,000, no more than <b>one-third of the "
             "contract price</b>, plus the cost of special-order materials if "
             "the contract designates them. HICPA makes taking more a "
             "prohibited act."),
     k.cellp("§&nbsp;517.9(10)")],
    [k.cellp("Liability insurance"),
     k.cellp("Not less than <b>$50,000</b> covering personal injury and "
             "<b>$50,000</b> covering property damage, with the current "
             "amount stated in the contract. Ask for the certificate, not "
             "the assurance."),
     k.cellp("§&nbsp;517.7(a)(11)")],
    [k.cellp("Time-and-materials cap"),
     k.cellp("Where the work is priced T&amp;M, a written initial estimate "
             "before work starts, and a cost that <b>may not exceed 10% above "
             "that estimate</b> without a written change order signed by "
             "both."),
     k.cellp("§&nbsp;517.7(a)(8)")],
    [k.cellp("Written change orders"),
     k.cellp("A description of the work, the materials, and specifications "
             "“that cannot be changed without a written change order signed "
             "by the owner and the contractor.”"),
     k.cellp("§&nbsp;517.7(a)(7)")],
    [k.cellp("Named subcontractors"),
     k.cellp("The names and addresses of all subcontractors known at "
             "signing. A post office box alone does not count as an "
             "address."),
     k.cellp("§&nbsp;517.7(a)(10)")],
    [k.cellp("Dates and deposit shown"),
     k.cellp("Approximate start and completion dates; the down payment and "
             "the special-order materials cost listed <b>separately</b>."),
     k.cellp("§&nbsp;517.7(a)(6), (9)")],
]
flow.append(k.ref_table(
    "Terms HICPA compels on a remodel — and you must negotiate on a new build",
    [k.cellp("Term", bold=True), k.cellp("What it requires", bold=True),
     k.cellp("HICPA cite", bold=True)],
    rows, [1.5 * inch, CW - 2.75 * inch, 1.25 * inch]))
flow.append(Spacer(1, 6))
flow.append(k.cite(
    "HICPA is the Home Improvement Consumer Protection Act, Act 132 of 2008, "
    "73 P.S. §§ 517.1—517.19. The registration itself is checked at the "
    "Office of Attorney General; a registration number is not a competency "
    "credential, and the Act says so."))

# ---------------------------------------------------------------- trades
flow += k.h2_tight("TRADE LICENSING IS LOCAL — AND ALLEGHENY IS ITS OWN CASE",
                   2.2)
flow.append(k.body(
    "There is no statewide electrician, plumber or HVAC license in "
    "Pennsylvania. L&amp;I again: “Some of Pennsylvania's 2,562 "
    "municipalities have established local licensure or certification "
    "requirements for contractors or construction trades people. Typically, "
    "these requirements pertain to home improvement contractors, electrical "
    "contractors (or electricians), and plumbing contractors (or plumbers).” "
    "There is no central registry to search — the municipality is the only "
    "authority on its own rules, which is why PA.4 sends you there."))
flow.append(k.callout(
    "Allegheny County plumbing is carved out of the UCC by statute", [
        Paragraph("If you are building in Allegheny County — a “county of "
                  "the second class” — your plumbing is not a UCC subject at "
                  "all. Section 7210.501(a.1) provides that a municipality in "
                  "such a county “<b>shall not administer and enforce "
                  "plumbing code provisions</b>” of its UCC ordinance, and "
                  "that the county retains authority to promulgate and "
                  "enforce its own plumbing code under the Local Health "
                  "Administration Law. The regulation repeats it: 34 Pa. Code "
                  "§ 403.21(a)(6)(i) says such a municipality “may not "
                  "administer and enforce” the International Plumbing Code "
                  "adopted by the chapter.", S["body"]),
        Paragraph("In practice that means a second permit, a second "
                  "inspector and a second rulebook for the plumbing on your "
                  "house, from the county health department rather than your "
                  "municipality — and county plumber licensing that has "
                  "nothing to do with the UCC. Budget the time; it is a "
                  "genuine parallel track, not a formality.", S["body"]),
    ]))

# ------------------------------------------------------------- write-ins
flow += k.h2_tight("WRITE DOWN WHAT YOU CONFIRMED", 1.6)
flow.append(k.body(
    "Everything above is statewide. These four answers are yours alone, and "
    "every later document in this kit depends on them."))
flow += k.check_table(
    "Your enforcement picture", [
        ("Municipality (township / borough / city) and county",
         [("Municipality", 0.5), ("County", 0.5)]),
        ("Which of the six arrangements applies here (1–6 above)",
         [("Path", 0.35), ("Confirmed by", 0.65)]),
        ("Who performs plan review and inspections — office or agency name",
         [("Name", 1.0)]),
        ("Local trade licensing: does the municipality require registered or "
         "licensed electricians or plumbers?",
         [("Answer", 1.0)]),
    ], notes_header="Notes")

# --------------------------------------------------------------- sources
flow.append(Spacer(1, 4))
flow.append(k.sources_table([
    ("The UCC applies to all buildings in the Commonwealth",
     "35 P.S. § 7210.104(a)"),
    ("Exclusions: agricultural, recreational cabin, repairs, alterations",
     "35 P.S. § 7210.104(b)"),
    ("Recreational cabin — seven-part definition",
     "35 P.S. § 7210.103"),
    ("Accessory structures under 1,000 sq ft; propane; manufactured housing",
     "34 Pa. Code § 403.1(b)"),
    ("On-lot sewage is governed by Chapter 73, not the UCC",
     "34 Pa. Code § 403.21(e)"),
    ("The five ways a municipality may administer and enforce",
     "35 P.S. § 7210.501(b)"),
    ("Allegheny County plumbing carve-out",
     "35 P.S. § 7210.501(a.1); 34 Pa. Code § 403.21(a)(6)(i)"),
    ("Opt-out: the applicant must obtain a certified third-party agency",
     "34 Pa. Code § 403.103(b)"),
    ("Opt-out: five required inspections named in the statute",
     "35 P.S. § 7210.501(e)(1)"),
    ("Opt-out: L&amp;I covers only non-residential",
     "34 Pa. Code § 403.103(g)"),
    ("Code administrator may not have a financial interest",
     "35 P.S. § 7210.502(c)"),
    ("Final report to owner, builder and lender; CO filed with municipality",
     "34 Pa. Code §§ 403.103(f), 403.65(e)"),
    ("No state licensure for most construction contractors",
     "PA L&amp;I, Contractor Licensing page"),
    ("HICPA excludes new-home construction and uncompensated owner work",
     "73 P.S. § 517.2"),
    ("HICPA deposit cap, insurance minimum, T&amp;M cap, change orders",
     "73 P.S. §§ 517.7(a), 517.9(10)"),
]))
flow.append(Spacer(1, 6))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "pa-permit-kit",
                       "PA.1-who-inspects-your-house.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
