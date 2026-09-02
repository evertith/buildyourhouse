#!/usr/bin/env python3
"""FL.1 Owner-Builder Exemption Walkthrough.

The organizing fact of this document is that Florida gives an owner-builder
TWO exemptions, not one, and they are not the same exemption written twice.

Chapter 489 is split into parts. Part I licenses the thirteen contractor
categories listed at s. 489.105(3), Fla. Stat. — general, building,
residential, roofing, mechanical, plumbing, pool, solar and the rest.
Electrical contracting is not among them; it is licensed separately under
Part II, s. 489.505. So the Part I owner-builder exemption at s. 489.103(7)
cannot reach electrical work, and Part II carries its own owner exemption at
s. 489.503(6) to fill the gap.

The two were drafted at different times and they do not match. Part I's
sale test is triggered by "any such structure" and creates a "presumption";
Part II's is triggered by "more than one such structure" and creates "prima
facie evidence." Part I asks for occupancy OR use; the disclosure statement
Part II makes you sign says use AND occupancy. Each part prints its own
disclosure statement. Guides that collapse the two into a single
"owner-builder rule" get at least one of those limits wrong, which is the
reason this document exists.
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

FORM_ID = "FL.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "The Exemption"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "What Florida lets you build yourself, which of the two "
                 "exemptions covers it, and the conditions attached to each.")
flow.append(k.disclaimer())

# ------------------------------------------------------------------ opener
flow += k.h2("THE THING ALMOST EVERY GUIDE GETS WRONG")
flow.append(k.body(
    "Florida does not have <i>an</i> owner-builder exemption. It has "
    "<b>two</b>, in two different parts of the same chapter, and you may well "
    "need both on one house."))
flow.append(k.body(
    "Chapter 489 is split. <b>Part I</b> licenses the thirteen contractor "
    "categories listed at s. 489.105(3) — general, building and residential "
    "contractors, and also roofing, mechanical, air-conditioning, plumbing, "
    "pool/spa, solar and underground utility. <b>Electrical contracting is "
    "not on that list.</b> It is licensed separately, under <b>Part II</b>, "
    "at s. 489.505. That single drafting fact is why there are two "
    "exemptions: the Part I exemption at <b>s. 489.103(7)</b> cannot reach "
    "your wiring, so Part II carries its own at <b>s. 489.503(6)</b>."))
flow.append(k.body(
    "They were written at different times and they do not say the same "
    "thing. The table below is the difference, side by side. If you take one "
    "page from this kit to the building department, take this one."))

flow += k.h2_tight("THE TWO EXEMPTIONS, SIDE BY SIDE", reserve=2.2)
rows = [
    [k.cellp("<b>Where it lives</b>"),
     k.cellp("s. 489.103(7), Fla. Stat. (Part I)"),
     k.cellp("s. 489.503(6), Fla. Stat. (Part II)")],
    [k.cellp("<b>What it exempts you from</b>"),
     k.cellp("Needing a Part I contractor license — general, building, "
             "residential, roofing, mechanical, plumbing, pool, solar and "
             "the rest of s. 489.105(3)"),
     k.cellp("Needing an electrical contractor license")],
    [k.cellp("<b>What you may build</b>"),
     k.cellp("A farm outbuilding, or a one-family or two-family residence. "
             "(A commercial building too, but only up to $75,000 — that cap "
             "is on <i>commercial</i> work and does not touch your house.)"),
     k.cellp("A farm outbuilding, or a single-family or duplex residence. "
             "(Commercial under $75,000.)")],
    [k.cellp("<b>Whose use</b>"),
     k.cellp("“for the occupancy <i>or</i> use of such owners”"),
     k.cellp("The disclosure statement you sign says “The home or "
             "building must be for your own use <i>and</i> occupancy.”")],
    [k.cellp("<b>The sale test</b>"),
     k.cellp("Sale or lease of <b>any</b> such structure within 1&nbsp;year of "
             "completion “creates a <b>presumption</b> that the "
             "construction was undertaken for purposes of sale or lease”"),
     k.cellp("Sale or lease of <b>more than one</b> such structure within 1 "
             "year of completion is “<b>prima facie evidence</b>” "
             "of the same thing")],
    [k.cellp("<b>Disclosure statement</b>"),
     k.cellp("Yes — the twelve numbered paragraphs printed later in this "
             "document"),
     k.cellp("Yes — a separate, shorter one, also printed later")],
    [k.cellp("<b>Personal appearance</b>"),
     k.cellp("Required: the owner “must personally appear and sign the "
             "building permit application”"),
     k.cellp("Required: the owner “shall personally appear and sign the "
             "building permit application”")],
]
flow.append(k.ref_table(
    "Part I and Part II are not the same exemption",
    [k.cellp("", bold=True), k.cellp("General contracting", bold=True),
     k.cellp("Electrical", bold=True)],
    rows, [1.30 * inch, (CW - 1.30 * inch) / 2, (CW - 1.30 * inch) / 2]))
flow.append(k.cite(
    "Sources: ss. 489.103(7), 489.105(3), 489.503(6) and 489.505, Fla. Stat. "
    "(2026). Quotations are the statutes' own words."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "Why the sale test matters more than the square footage", [
        Paragraph("There is <b>no square-footage cap and no dollar cap</b> on "
                  "a one- or two-family residence under either exemption. The "
                  "$75,000 figure in both statutes attaches to "
                  "<i>commercial</i> buildings only. What actually limits you "
                  "is the sale test — and the two parts set it differently. "
                  "Sell one house you wired yourself within a year and you "
                  "have tripped Part I's presumption while leaving Part II's "
                  "“more than one” test untouched. Do not assume "
                  "clearing one clears the other.", S["body"]),
    ]))

# ---------------------------------------------------------------- coverage
flow += k.h2("WHAT THE GENERAL EXEMPTION ACTUALLY COVERS")
flow.append(k.body(
    "Section 489.103(7)(a) exempts “owners of property when acting as "
    "their own contractor and providing direct, onsite supervision themselves "
    "of all work not performed by licensed contractors,” in four "
    "situations. Only the first is the ordinary build-your-own-house case; "
    "the other three are narrow, and two of them are worth knowing about "
    "because almost nobody does."))
rows = [
    [k.cellp("<b>1</b>"),
     k.cellp("<b>Building or improving a farm outbuilding, or a one-family "
             "or two-family residence</b>, for the owner's occupancy or use "
             "and not offered for sale or lease. This is your house."),
     k.cellp("489.103(7)(a)1.")],
    [k.cellp("<b>2</b>"),
     k.cellp("<b>Repairing or replacing wood shakes, asphalt or fiberglass "
             "shingles</b> on a one-, two-, or three-family residence — but "
             "only where the property was damaged in an event the Governor "
             "has declared a state of emergency by executive order. A "
             "hurricane provision."),
     k.cellp("489.103(7)(a)2.")],
    [k.cellp("<b>3</b>"),
     k.cellp("<b>Installing or replacing solar panels</b> on a one-, two-, "
             "or three-family residence — but only where the local "
             "government is participating in a named federal grant program "
             "(a “SunShot Initiative: Rooftop Solar Challenge” "
             "grant). That program is old, so <b>ask your building "
             "department whether this pathway is live where you are</b> "
             "before relying on it. You must still use a licensed electrical "
             "contractor for the wiring and any interconnection."),
     k.cellp("489.103(7)(a)3.")],
    [k.cellp("<b>4</b>"),
     k.cellp("<b>Finishing a permit your contractor walked away from</b>, "
             "where the local permitting agency determines the listed "
             "contractor substantially completed the project. You must get "
             "the agency's approval first — and this is the one case where "
             "you are <b>not</b> required to occupy the home for a year "
             "afterward."),
     k.cellp("489.103(7)(a)4.")],
]
flow.append(k.ref_table(
    "The four situations the Part I exemption covers",
    [k.cellp("", bold=True), k.cellp("What it allows", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [0.42 * inch, CW - 1.72 * inch, 1.30 * inch]))

flow.append(Spacer(1, 2))
flow.append(k.body(
    "Note what situation 1 does <b>not</b> say. It does not cap your square "
    "footage. It does not cap your budget. It does not limit you to one "
    "permit in any period — Florida sets <b>no frequency limit</b> on the "
    "Part I owner-builder exemption, unlike several other states. And "
    "because s. 489.105(3) defines a contractor as someone who does the work "
    "<i>“for compensation… for others or for resale to others,”</i> "
    "work you do on your own home for no compensation is outside the "
    "definition before any exemption is reached."))

# ------------------------------------------------------------------ trades
flow += k.h2("CAN YOU DO YOUR OWN PLUMBING, ROOFING AND HVAC?")
flow.append(k.body(
    "This is the question owner-builders actually ask, and the answer turns "
    "on four words at the very top of the exemption statute. Section 489.103 "
    "opens: <b>“This part does not apply to”</b> — and then lists "
    "owners acting as their own contractor. Not “this section”; "
    "<i>this part</i>. Plumbing, mechanical, air-conditioning, roofing, "
    "sheet metal and pool contracting are all licensed inside Part I, at "
    "s. 489.105(3)(d)–(q). So when Part I stops applying to you, it stops "
    "applying for those trades too."))
flow.append(k.body(
    "That is why there is no separate plumbing exemption and no separate "
    "roofing disclosure statement to sign, the way there is for electrical. "
    "Electrical needed its own exemption precisely <i>because</i> it sits "
    "outside Part I."))
rows = [
    [k.cellp("<b>You, personally, on your own house</b>"),
     k.cellp("Plumbing, mechanical, HVAC, roofing and the rest of the Part I "
             "trades are covered by the general exemption. Electrical is "
             "covered by the Part II exemption, with its own disclosure "
             "statement. <b>Permits and inspections still apply to all of "
             "it.</b>"),
     k.cellp("ss. 489.103(7), 489.503(6)")],
    [k.cellp("<b>Anyone you pay to do a licensed trade</b>"),
     k.cellp("Must hold the license for that trade. The disclosure statement "
             "makes checking it <i>your</i> job, and s. 489.113(2) bars an "
             "unlicensed sub from performing work in the listed trade "
             "categories even under someone else's supervision."),
     k.cellp("s. 489.103(7)(c) ¶6; s. 489.113(2)")],
    [k.cellp("<b>Anyone you pay who is not licensed</b>"),
     k.cellp("May only work as your <b>directly supervised employee</b>, on "
             "work that is not in a licensed trade category — never as your "
             "contractor and never supervising others."),
     k.cellp("s. 489.103(7)(b), (c) ¶6, ¶8")],
]
flow.append(k.ref_table(
    "Who may do the trade work",
    [k.cellp("", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.75 * inch, CW - 3.35 * inch, 1.60 * inch]))
flow.append(k.cite(
    "One caution: this is what the statute says, and building departments "
    "vary in how readily they accept owner-performed trade work in practice. "
    "Some will ask you to demonstrate competence. Ask your county before you "
    "plan a schedule around self-performing a trade."))

# -------------------------------------------------------------- conditions
flow += k.h2("THE FOUR CONDITIONS, AND WHERE PEOPLE TRIP")
flow.append(k.body(
    "The exemption is generous. It is also conditional, and two of its "
    "conditions are satisfied at a counter rather than at your desk."))
flow.append(k.bullet(
    "<b>Direct, onsite supervision, by you.</b> The statute exempts owners "
    "“providing direct, onsite supervision <i>themselves</i> of all work "
    "not performed by licensed contractors.” Paragraph (b) closes the "
    "obvious workaround: “The owner may not delegate the owner's "
    "responsibility to directly supervise all work to any other person unless "
    "that person is registered or certified under this part and the work "
    "being performed is within the scope of that person's license.” "
    "(s. 489.103(7)(b))"))
flow.append(k.bullet(
    "<b>For your occupancy or use, and not offered for sale or lease.</b> "
    "Note the wording is disjunctive in Part I — occupancy <i>or</i> use."))
flow.append(k.bullet(
    "<b>You must personally appear and sign the permit application.</b> Not "
    "your spouse, not your designer, not the contractor helping you. "
    "s. 489.103(7)(c). The one carve-out is an electronically submitted solar "
    "application under situation 3."))
flow.append(k.bullet(
    "<b>You must sign the disclosure statement</b>, and the agency must be "
    "satisfied you understand it. The statute adds an identity step at "
    "issuance: “A copy of the property owner's driver license, the "
    "notarized signature of the property owner, or other type of verification "
    "acceptable to the local permitting agency is required when the permit is "
    "issued.” Ask your county which of the three it wants before you "
    "make the trip."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "What happens if a condition fails", [
        Paragraph("This is not a paperwork foot-fault. Section 489.103(7)(c) "
                  "directs the agency: “If any person violates the "
                  "requirements of this subsection, the local permitting "
                  "agency <b>shall withhold final approval, revoke the "
                  "permit, or pursue any action or remedy for unlicensed "
                  "activity</b> against the owner and any person performing "
                  "work that requires licensure under the permit issued.” "
                  "Withholding final approval means no certificate of "
                  "occupancy on a finished house.", S["body"]),
    ]))

# ------------------------------------------------------------- disclosure I
flow += k.h2("THE DISCLOSURE STATEMENT YOU WILL SIGN")
flow.append(k.body(
    "The statute prints this statement in full and requires the permitting "
    "agency to give it to you “in substantially the following form.” "
    "It is twelve numbered paragraphs. Below is what each one commits you to "
    "— read it before you are standing at the counter with a pen, because "
    "several of them are obligations rather than acknowledgements."))
rows = [
    [k.cellp("<b>1–3</b>"),
     k.cellp("You understand state law normally requires a licensed "
             "contractor, that you are the <b>responsible party of record</b> "
             "on the permit, and that you could instead have shifted that "
             "risk by hiring a licensed contractor and putting the permit in "
             "their name.")],
    [k.cellp("<b>4</b>"),
     k.cellp("What you may build, and the sale test: if the home “is "
             "sold or leased within 1&nbsp;year after the construction is "
             "complete, the law will presume that I built or substantially "
             "improved it for sale or lease, which violates the "
             "exemption.”")],
    [k.cellp("<b>5</b>"),
     k.cellp("You will provide <b>direct, onsite supervision</b> of the "
             "construction.")],
    [k.cellp("<b>6</b>"),
     k.cellp("“I may not hire an unlicensed person to act as my "
             "contractor or to supervise persons working on my building or "
             "residence. It is my responsibility to ensure that the persons "
             "whom I employ have the licenses required by law and by county "
             "or municipal ordinance.”")],
    [k.cellp("<b>7</b>"),
     k.cellp("You may be <b>personally liable for injuries</b> to an "
             "unlicensed person or their employees working on your property, "
             "and your homeowner's insurance may not cover those injuries. "
             "You state you are aware of the limits of your coverage.")],
    [k.cellp("<b>8</b>"),
     k.cellp("The one that costs money: anyone unlicensed working on your "
             "building “must work under my direct supervision and must "
             "be employed by me, which means that I must comply with laws "
             "requiring the withholding of federal income tax and social "
             "security contributions under the Federal Insurance "
             "Contributions Act (FICA) and must provide workers' "
             "compensation for the employee.”")],
    [k.cellp("<b>9–12</b>"),
     k.cellp("You will abide by the laws governing owner-builders "
             "<b>and employers</b>; the construction must comply with all "
             "codes and zoning; where to get employer guidance; the property "
             "address; and a promise to notify the issuer of any change to "
             "what you disclosed.")],
]
flow.append(k.ref_table(
    "The twelve-point disclosure statement, s. 489.103(7)(c)",
    [k.cellp("¶", bold=True), k.cellp("What you are signing", bold=True)],
    rows, [0.62 * inch, CW - 0.62 * inch]))
flow.append(k.cite(
    "Quotations are verbatim from the disclosure statement as printed in "
    "s. 489.103(7)(c), Fla. Stat. (2026). Your county's form should match it "
    "substantially; read the copy you are handed."))

flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "Paragraph 8, and the one place Florida's own statutes pull against "
    "each other", [
        Paragraph("Most owner-builders read paragraph 8 as boilerplate. It is "
                  "not. It says that any unlicensed person working on your "
                  "house is <b>your employee</b> — federal income tax "
                  "withholding, FICA, and workers' compensation. Paying a "
                  "neighbor cash to help frame is the exact fact pattern it "
                  "describes.", S["body"]),
        Paragraph("But the workers' compensation chapter says something that "
                  "does not sit comfortably alongside it. Section 440.02(19)"
                  "(b) provides that “A homeowner shall not be "
                  "considered the employer of persons hired by the homeowner "
                  "to carry out construction on the homeowner's own premises "
                  "if those premises are not intended for immediate lease, "
                  "sale, or resale.” And s. 440.02(10) excludes from "
                  "“construction industry” altogether "
                  "“a homeowner's act of construction… upon his or "
                  "her own premises.”", S["body"]),
        Paragraph("So the disclosure statement you sign warns you that you "
                  "must provide workers' compensation, while chapter 440 says "
                  "a homeowner in your position is not the employer. "
                  "<b>This kit will not tell you which one wins</b>, because "
                  "that answer depends on facts we cannot see and is not "
                  "settled by the text of either statute. What we will tell "
                  "you is that the gap is real, the exposure runs in one "
                  "direction only — an injured worker on your lot — and this "
                  "is worth one conversation with a Florida insurance agent "
                  "or attorney <i>before</i> anyone swings a hammer for you.",
                  S["body"]),
    ]))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "Two different one-year clocks, started by two different events", [
        Paragraph("Florida hands an owner-builder two separate one-year "
                  "rules and they do not run together. The exemption's clock "
                  "in s. 489.103(7)(a)1. runs <b>from completion</b> — sell "
                  "or lease within a year of finishing and you trip the "
                  "presumption. The workers' compensation clock in "
                  "s. 440.02(10) runs <b>from commencement</b> — the "
                  "homeowner carve-out holds only if the premises are not "
                  "intended to be sold, resold or leased within 1&nbsp;year "
                  "<i>after the commencement of construction</i>. On a build "
                  "that takes fourteen months, those two clocks expire "
                  "several months apart.", S["body"]),
    ]))

# ------------------------------------------------------------ disclosure II
flow += k.h2("THE SECOND DISCLOSURE, FOR YOUR OWN WIRING")
flow.append(k.body(
    "If you intend to do your own electrical work you are relying on the "
    "Part II exemption, and you will sign a second, shorter disclosure "
    "statement. It is printed at s. 489.503(6)(c). Three things in it differ "
    "from the Part I version and are worth reading closely:"))
flow.append(k.bullet(
    "<b>Use and occupancy.</b> “The home or building must be for your "
    "own use and occupancy.” Part I says occupancy <i>or</i> use; this "
    "one reads as both."))
flow.append(k.bullet(
    "<b>A different sale test.</b> “If you sell or lease <b>more than "
    "one building</b> you have wired yourself within 1&nbsp;year after the "
    "construction is complete, the law will presume that you built it for "
    "sale or lease.” More than one — not any."))
flow.append(k.bullet(
    "<b>The same hard limit on hired help.</b> “You may not hire an "
    "unlicensed person as your electrical contractor.”"))
flow.append(k.body(
    "The Part II exemption also carries the same abandoned-permit provision "
    "as Part I, at s. 489.503(6)(b), with the same relief from the "
    "one-year occupancy expectation."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "An exemption from the license is not an exemption from the code", [
        Paragraph("Neither exemption excuses you from anything else. You "
                  "still pull permits, you still pass every inspection, and "
                  "your work is judged against the full Florida Building Code "
                  "and the electrical code it adopts — by an inspector who "
                  "does not grade owner-builders on a curve. The exemption "
                  "buys you the right to be the contractor. It does not lower "
                  "the standard.", S["body"]),
    ]))

# ------------------------------------------------------------------ hiring
flow += k.h2("IF YOU HIRE ANYONE: THREE PROTECTIONS AND ONE TRAP")
flow.append(k.body(
    "The moment you pay someone, Florida's licensing law starts working "
    "either for you or against you. These four provisions decide which."))
rows = [
    [k.cellp("<b>Verify the license yourself</b>"),
     k.cellp("Paragraph 6 of the disclosure makes this <i>your</i> "
             "responsibility, not theirs. Search the licensee by name or "
             "number at <b>myfloridalicense.com</b>. Note Florida has two "
             "tiers: a <b>certified</b> contractor may work statewide, while "
             "a <b>registered</b> contractor is limited to the specific "
             "local jurisdictions that licensed them — a registered "
             "contractor is not licensed everywhere."),
     k.cellp("s. 489.103(7)(c) ¶6; s. 489.113")],
    [k.cellp("<b>An unlicensed contractor cannot enforce the contract — "
             "or lien you</b>"),
     k.cellp("“As a matter of public policy, contracts entered into on "
             "or after October 1, 1990, by an unlicensed contractor shall be "
             "unenforceable in law or in equity by the unlicensed "
             "contractor,” and “no lien or bond claim shall exist "
             "in favor of the unlicensed contractor.” This is real "
             "protection, but it is a defense after the fact — far worse "
             "than not hiring them."),
     k.cellp("s. 489.128(1), (2)")],
    [k.cellp("<b>Unlicensed contracting is a crime, and worse after a "
             "storm</b>"),
     k.cellp("Acting as a contractor without being registered or certified "
             "is a <b>first-degree misdemeanor</b>; a second offense, or an "
             "offense committed <b>during a state of emergency declared by "
             "the Governor</b>, is a <b>third-degree felony</b>. The "
             "department may also issue a stop-work order."),
     k.cellp("s. 489.127(1)(f), (2)(a)–(c), (3)")],
    [k.cellp("<b>The trap: borrowing a license</b>"),
     k.cellp("A licensed contractor “may not enter into an agreement, "
             "oral or written, whereby his or her certification number or "
             "registration number is used” by someone unlicensed, and "
             "may not pull a permit for work they are not actually "
             "performing or supervising. The favor of “I'll pull it for "
             "you” is prohibited on the contractor's side."),
     k.cellp("s. 489.127(4)(a)–(c)")],
]
flow.append(k.ref_table(
    "What the licensing law does for you, and to you",
    [k.cellp("", bold=True), k.cellp("What it means", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.55 * inch, CW - 3.10 * inch, 1.55 * inch]))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "Starting before the permit is in effect is itself an offense", [
        Paragraph("Section 489.127(1)(h) makes it unlawful for <b>any "
                  "person</b> to “commence or perform work for which a "
                  "building permit is required pursuant to part IV of chapter "
                  "553 without such building permit being in effect,” and "
                  "subsection (2)(a) makes a violation of subsection (1) by an "
                  "unlicensed person a first-degree misdemeanor. An "
                  "owner-builder is, by definition, an unlicensed person. "
                  "Clearing the lot and setting forms while the application is "
                  "still in review is the version of this that people actually "
                  "do.", S["body"]),
    ]))

# --------------------------------------------------------------- checklist
flow += k.h2_tight("BEFORE YOU GO TO THE COUNTER", reserve=2.0)
flow += k.check_table(
    "Owner-builder qualification check",
    [("I own the property, and the structure is a one-family or two-family "
      "residence or a farm outbuilding", []),
     ("The home is for my own occupancy or use and is not offered for sale "
      "or lease", []),
     ("I understand the 1-year sale test, and I have checked the "
      "<i>separate</i> test that applies if I am also doing my own wiring",
      []),
     ("I will personally provide direct, onsite supervision of all work not "
      "done by licensed contractors", []),
     ("I can appear in person to sign the permit application", []),
     ("I have asked my county which identity verification it requires at "
      "issuance — driver license copy, notarized signature, or other",
      [("County requires:", 1.0)]),
     ("I have read the twelve-point disclosure statement, including "
      "paragraph 8 on withholding and workers' compensation", []),
     ("Every person I intend to pay is either a licensed contractor or will "
      "be my payrolled employee with workers' compensation", []),
     ("I have verified each contractor at myfloridalicense.com, and checked "
      "whether a <i>registered</i> contractor's jurisdiction covers my "
      "parcel", [("Verified on:", 1.0)]),
     ("If I am doing my own electrical work, I have asked for the "
      "<i>second</i> disclosure statement under s. 489.503(6)", []),
     ],
    notes_header="Notes")

# ----------------------------------------------------------------- sources
flow += k.h2_tight("SOURCES", reserve=2.0)
flow.append(k.sources_table([
    ("Chapter 489 is split: Part I licenses thirteen contractor categories, "
     "which do not include electrical; electrical is licensed under Part II",
     "ss. 489.105(3), 489.505"),
    ("A “contractor” is one who does the work for compensation for "
     "others or for resale to others", "s. 489.105(3)"),
    ("The Part I owner-builder exemption, its four situations, and the "
     "$75,000 cap that applies to commercial buildings only",
     "s. 489.103(7)(a)1.–4."),
    ("Sale or lease of any such structure within 1&nbsp;year creates a "
     "presumption the construction was for sale or lease",
     "s. 489.103(7)(a)1."),
    ("The owner may not delegate direct supervision except to someone "
     "licensed for that scope of work", "s. 489.103(7)(b)"),
    ("Personal appearance to sign the application; the disclosure statement; "
     "driver license, notarized signature or other verification at issuance; "
     "and the agency's duty to withhold approval or revoke on violation",
     "s. 489.103(7)(c)"),
    ("The twelve-point disclosure statement, including ¶6 on hiring "
     "unlicensed persons and ¶8 on FICA withholding and workers' "
     "compensation", "s. 489.103(7)(c)"),
    ("The separate electrical owner exemption, its “more than one "
     "structure” prima facie test, and its own disclosure statement "
     "requiring use and occupancy", "s. 489.503(6)(a), (c)"),
    ("Finishing a permit a contractor substantially completed, with no "
     "1-year occupancy requirement", "ss. 489.103(7)(a)4., 489.503(6)(b)"),
    ("Contracts by an unlicensed contractor are unenforceable by them, and "
     "no lien or bond claim exists in their favor", "s. 489.128(1), (2)"),
    ("Unlicensed contracting is a first-degree misdemeanor; a repeat "
     "offense or one during a Governor-declared state of emergency is a "
     "third-degree felony; stop-work orders",
     "s. 489.127(1)(f), (2)(a)–(c), (3)"),
    ("Commencing work without the required building permit in effect is a "
     "prohibited act", "s. 489.127(1)(h)"),
    ("A licensee may not let their license number be used by an unlicensed "
     "person, nor pull permits for work they are not performing",
     "s. 489.127(4)(a)–(c)"),
    ("Certified contractors may work statewide; registered contractors are "
     "limited to the jurisdictions that licensed them",
     "ss. 489.113(1), 489.105(8), (10)"),
    ("An unlicensed subcontractor may not perform work in the listed trade "
     "categories even under a licensee's supervision", "s. 489.113(2)"),
    ("A homeowner is not the employer of persons hired to build on their own "
     "premises not intended for immediate lease, sale or resale; and a "
     "homeowner's own construction is outside the construction industry if "
     "not to be sold or leased within 1&nbsp;year of commencement",
     "ss. 440.02(19)(b), 440.02(10)"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "fl-permit-kit",
                       "FL.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
