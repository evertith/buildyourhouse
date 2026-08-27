#!/usr/bin/env python3
"""WA.1 Owner-Builder Exemption Walkthrough.

Every Washington claim in this document was read out of the statute text at
app.leg.wa.gov in August 2026 and is cited on-page.

Verified sources:
  RCW 18.27.090(12)   own-property / personal-residence exemption from
                      contractor registration; the selling-demolishing-leasing
                      carve-out
  RCW 18.27.090(11)   owner who contracts with a REGISTERED contractor; the
                      "owned for less than twelve months" carve-out
  RCW 18.27.090(9)    the $500 casual/minor/inconsequential threshold and its
                      anti-splitting language
  RCW 18.27.090(13)   owner performing maintenance/repair/alteration on own
                      properties, or using own employees
  RCW 18.27.090(14)   architects, engineers, certified electricians and
                      plumbers exempt within the scope of their certification
  RCW 18.27.110(2),(3) the jurisdiction must print the registration number and
                      warn you about unregistered contractors; a permit
                      obtained by falsifying an exemption is FORFEITED
  RCW 19.28.261(1)    homeowner electrical exemption; the rent/sale/lease and
                      12-month carve-outs; the 24-month affidavit route that
                      applies ONLY to buildings intended for rent/sale/lease
  RCW 19.28.261(6)    the friend/neighbor/relative helper provision
  RCW 19.28.101(5)    L&I approval required before the utility connects
  RCW 18.106.150(1)   homeowner plumbing exemption — note it carries NO
                      rent/sale/lease condition, unlike electrical
  RCW 18.106.150(6),(7) helper provision; medical gas excluded
  RCW 19.28.010(3),(4) cities and towns — not counties — may run their own
                      electrical inspection programs
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

FORM_ID = "WA.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "Exemption & Qualification"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Which Washington exemptions you are actually relying on — there are "
    "three, with three different tests — what each one costs you if you get "
    "it wrong, and what takes it away.")

flow.append(k.disclaimer(
    "Statute text was read at app.leg.wa.gov in August 2026; statutes "
    "change."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION")
flow.append(k.body(
    "Washington does not issue a general contractor license. It requires "
    "anyone who contracts to do construction work <b>for others</b> to "
    "<b>register</b> with the Department of Labor &amp; Industries. Building "
    "on your own land, you are not contracting for anyone, and the statute "
    "says so explicitly. There is no project-cost threshold to clear, no "
    "affidavit sworn before a licensing board, and no requirement that you "
    "personally attend inspections. Compared with most states this is an "
    "easy door to walk through."))
flow.append(k.body(
    "The mistake is stopping there. <b>Contractor registration is only one "
    "of three separate exemptions</b>, written in three separate chapters "
    "with three different tests. Qualifying for one does not qualify you for "
    "the others — and the electrical one is materially stricter than the "
    "plumbing one, which is the opposite of what most people assume."))

rows = [
    [k.cellp("Do you need a license to be your own GC?"),
     k.cellp("No. Washington has registration, not licensure, and working on "
             "your own property is exempt from it")],
    [k.cellp("Is there a dollar threshold?"),
     k.cellp("Not for you. The $500 figure in the chapter governs small jobs "
             "done <i>for others</i>, not the size of your house")],
    [k.cellp("Must you live in it?"),
     k.cellp("Not for the registration exemption — it applies \"whether "
             "occupied by him or her or not.\" Occupancy matters for the "
             "<b>electrical</b> exemption")],
    [k.cellp("What kills it?"),
     k.cellp("Building for the purpose of <b>selling, demolishing, or "
             "leasing</b> the property")],
    [k.cellp("Do you still need permits?"),
     k.cellp("Yes — every one of them. Exempt from a registration is not "
             "exempt from a permit")],
]
flow.append(k.ref_table(
    "The exemption at a glance",
    [k.cellp("Question", bold=True),
     k.cellp("Washington's answer", bold=True)],
    rows, [2.7 * inch, CW - 2.7 * inch]))

# ---------------------------------------------------------------- the exemption
flow += k.h2_tight("THE EXEMPTION ITSELF — RCW 18.27.090(12)")
flow.append(k.body(
    "The registration provisions of chapter 18.27 RCW do not apply to:"))
flow.append(k.callout("RCW 18.27.090(12), in full", [
    Paragraph("\"<i>Any person working on his or her own property, whether "
              "occupied by him or her or not, and any person working on his "
              "or her personal residence, whether owned by him or her or not "
              "but this exemption shall not apply to any person who performs "
              "the activities of a contractor on his or her own property for "
              "the purpose of selling, demolishing, or leasing the "
              "property.</i>\"", S["body"]),
]))
flow.append(Spacer(1, 8))
flow.append(k.body(
    "Read it twice, because it is doing two jobs at once. The first clause "
    "covers <b>your own property</b> — and note the words \"<i>whether "
    "occupied by him or her or not</i>.\" You do not have to live there. The "
    "second clause covers <b>your personal residence</b> \"<i>whether owned "
    "by him or her or not</i>\" — which is how a tenant may work on the home "
    "they live in. As an owner-builder you are almost always relying on the "
    "first clause."))
flow.append(k.body(
    "Then the carve-out, and it is a <b>purpose</b> test, not a timing test. "
    "The exemption disappears if you are doing the work \"<i>for the purpose "
    "of selling, demolishing, or leasing the property</i>.\" A spec house, a "
    "flip, or a rental you never intended to occupy is outside it from the "
    "first day, regardless of how long you hold it. Nothing in this "
    "subsection sets a number of months."))

flow += k.h2_tight("THE SECOND EXEMPTION YOU ARE ALSO USING — RCW 18.27.090(11)")
flow.append(k.body(
    "The moment you hire someone, a different subsection carries you: "
    "\"<i>An owner who contracts for a project with a <b>registered "
    "contractor</b>, except that this exemption shall not deprive the owner "
    "of the protections of this chapter against registered and unregistered "
    "contractors.</i>\" Two things follow from the wording."))
flow.append(k.bullet(
    "<b>It only names registered contractors.</b> Hiring registered trades "
    "keeps you plainly inside the exemption. Hiring an unregistered one puts "
    "you outside the four corners of the subsection and hands you the risk "
    "the statute is trying to protect you from."))
flow.append(k.bullet(
    "<b>It has its own, different carve-out</b> — and this is the twelve-month "
    "rule people half-remember: it \"<i>does not apply to a person who "
    "performs the activities of a contractor for the purpose of leasing or "
    "selling improved property he or she has owned for <b>less than twelve "
    "months</b></i>.\""))

flow.append(k.callout("Two carve-outs, two different tests — do not merge them", [
    Paragraph("Subsection <b>(12)</b> asks <i>what was your purpose</i>: "
              "selling, demolishing, or leasing. It sets no clock. Subsection "
              "<b>(11)</b> asks <i>how long have you owned it</i>: under "
              "twelve months, coupled with a purpose of leasing or selling.",
              S["body"]),
    Paragraph("Practical reading: build to live in it. If there is a real "
              "chance you will sell or lease inside a year of buying the "
              "land, get advice before you pull the permit rather than after "
              "— and note the consequence below is the permit itself, not a "
              "fine.", S["body"]),
]))
flow.append(k.cite(
    "RCW 18.27.090(11) and (12). Two further subsections are worth knowing: "
    "<b>(13)</b> exempts an owner who performs maintenance, repair and "
    "alteration work on their own properties or uses their own employees to "
    "do it; <b>(9)</b> treats a whole undertaking whose aggregate contract "
    "price is under <b>$500</b> as \"<i>casual, minor, or inconsequential</i>\" "
    "— but expressly not where the work is part of a larger operation, or "
    "where a job is split into sub-$500 contracts to evade the chapter."))

# ---------------------------------------------------------------- forfeiture
flow += k.h2_tight("WHAT IT COSTS IF YOU CLAIM IT WRONGLY")
flow.append(k.body(
    "Washington does not fine you for a bad exemption claim. It takes the "
    "permit: \"<i>If a building permit is obtained by an applicant or "
    "contractor who falsifies information to obtain an exemption provided "
    "under RCW 18.27.090, the building permit shall be <b>forfeited</b>.</i>\" "
    "Forfeited, on a house you are part way through building, is the most "
    "expensive sentence in this kit."))
flow.append(k.body(
    "The same statute gives you two things at the counter that most "
    "owner-builders never notice they are owed. At the time of issuing the "
    "permit, every city, town and county is responsible for <b>printing the "
    "contractor registration number on the building permit</b> and for "
    "\"<i>providing a written notice to the building permit applicant "
    "informing them of contractor registration laws and the potential risk "
    "and monetary liability to the homeowner for using an unregistered "
    "contractor</i>.\" If nobody hands you that notice, ask for it."))
flow.append(k.cite("RCW 18.27.110(2)(a), (2)(b), (3)."))

# ---------------------------------------------------------------- trades
flow += k.h2_tight("DOING YOUR OWN ELECTRICAL, PLUMBING, AND MECHANICAL WORK")
flow.append(k.body(
    "Here the three chapters come apart. Each exemption below is from a "
    "<b>license or certification</b> requirement. None of them is an "
    "exemption from a <b>permit</b>."))

trade_rows = [
    [k.cellp("<b>Electrical</b>"),
     k.cellp("No license or certified electrician is needed \"<i>to do "
             "electrical work at his or her residence or farm or place of "
             "business or on other property owned by him or her</i>\" — "
             "<b>unless</b> the work is on the construction of a new building "
             "<i>intended for rent, sale, or lease</i>, or on property "
             "offered for sale within 12 months after obtaining it."),
     k.cellp("RCW 19.28.261(1)")],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp("\"<i>Nothing in this chapter shall be construed to require that "
             "a person obtain a license in order to do plumbing work at his "
             "or her residence or farm or place of business or on other "
             "property owned by him or her.</i>\" Note what is <b>absent</b>: "
             "no rent, sale, or lease condition and no twelve-month clock. "
             "Medical gas systems are excluded."),
     k.cellp("RCW 18.106.150(1), (7)")],
    [k.cellp("<b>Mechanical / HVAC</b>"),
     k.cellp("Washington does not run a separate statewide mechanical "
             "certification for this work; it is permitted and inspected "
             "under the mechanical code by your local building department. "
             "Handling refrigerant is a separate <b>federal</b> matter: EPA "
             "Section 608 certification is required to open a refrigerant "
             "circuit, and refrigerant may not be sold to uncertified "
             "persons."),
     k.cellp("40 C.F.R. Part 82, Subpart F")],
]
flow.append(k.ref_table(
    "Trade by trade — what each exemption actually says",
    [k.cellp("Trade", bold=True), k.cellp("The statutory test", bold=True),
     k.cellp("Authority", bold=True)],
    trade_rows, [1.05 * inch, CW - 1.05 * inch - 1.5 * inch, 1.5 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "The \"24 months\" rule is real — but it is not the rule for your house", [
        Paragraph("Guides routinely tell Washington owner-builders that to do "
                  "their own electrical on a new home they must intend to "
                  "occupy it as a principal residence for 24 months. That "
                  "condition is in the statute, but read where it sits. "
                  "RCW 19.28.261(1) gives the plain exemption for work on "
                  "property you own. The 24-month language is in the sentence "
                  "that <i>follows</i>, and it opens: \"<i>However, if the "
                  "construction is of a new residential building with up to "
                  "four units <b>intended for rent, sale, or lease</b>, the "
                  "owner may receive an exemption … if he or she provides a "
                  "signed affidavit to the department …</i>\"", S["body"]),
        Paragraph("So the affidavit, the 24-month occupancy intent, and the "
                  "\"<i>only receive an exemption once every twenty-four "
                  "months</i>\" limit are the terms of a <b>rescue route for "
                  "buildings that are intended for rent, sale, or lease</b> "
                  "— the classic case being an owner building a fourplex and "
                  "living in one unit. A single-family house you are building "
                  "to live in is not intended for rent, sale or lease, so it "
                  "is covered by the plain exemption instead.", S["body"]),
        Paragraph("<b>Confirm this with L&amp;I before you buy wire.</b> It "
                  "is your money and your inspection, the distinction turns "
                  "on a single sentence, and L&amp;I is the agency that "
                  "issues the permit and forms its own view of your "
                  "intent.", S["body"]),
    ]))
flow.append(k.cite("RCW 19.28.261(1), including the second paragraph."))

flow.append(k.body(
    "<b>You are allowed help.</b> Both chapters carry the same quiet "
    "provision: nothing in them restricts \"<i>the right of any householder "
    "to assist or receive assistance from a friend, neighbor, relative, or "
    "other person when none of the individuals doing the … installation hold "
    "themselves out as engaged in the trade or business</i>.\" The limit is "
    "in the last clause — the moment someone is holding themselves out as "
    "being in the business, they need their own credentials."))
flow.append(k.cite("RCW 19.28.261(6); RCW 18.106.150(6)."))

flow.append(k.callout("A permit is still required for every trade", [
    Paragraph("Being exempt from a <b>license</b> is not being exempt from a "
              "<b>permit</b>. Your building, plumbing and mechanical permits "
              "come from your city or county. Your <b>electrical</b> permit "
              "and inspection come from L&amp;I — or, if you are inside an "
              "incorporated city or town that runs its own electrical "
              "program, from that city. And no electrical work \"<i>may be "
              "concealed until it has been approved by the inspector</i>,\" "
              "nor may the utility connect you before L&amp;I has approved. "
              "Doing trade work without pulling the permit is the most "
              "expensive mistake available to you, because the remedy is "
              "opening up finished work.", S["body"]),
]))
flow.append(k.cite(
    "RCW 19.28.101(4), (5); RCW 19.28.010(3), (4) — note the local option "
    "belongs to <b>incorporated cities and towns</b>, not counties. See "
    "WA.3 and WA.4."))

# ---------------------------------------------------------------- hiring
flow += k.h2_tight("VERIFYING ANYONE YOU HIRE")
flow.append(k.body(
    "Your permit office must verify a contractor's registration before "
    "issuing a permit for that contractor's work, but nobody verifies the "
    "people you pay directly. Do it yourself, in writing, before work starts "
    "— L&amp;I publishes a public lookup at <b>secure.lni.wa.gov/verify/</b> "
    "that returns registration status, bond and insurance."))
flow.append(k.bullet(
    "<b>General trades</b> — a current <b>contractor registration</b> under "
    "chapter 18.27 RCW. Check that it is active, and check the bond and "
    "liability insurance while you are there."))
flow.append(k.bullet(
    "<b>Electrical</b> — a different credential entirely. An electrical "
    "<b>contractor</b> holds a license under chapter 19.28 RCW, and the "
    "individuals doing the work hold certificates of competency. Certified "
    "electricians are separately exempt from contractor registration when "
    "operating within the scope of their certification, so do not treat a "
    "missing 18.27 registration as proof of anything until you have checked "
    "the electrical license. (RCW 18.27.090(14))"))
flow.append(k.bullet(
    "<b>Plumbing</b> — certification under chapter 18.106 RCW, with the same "
    "carve-out from contractor registration."))
flow.append(k.bullet(
    "<b>Septic</b> — installers and designers are regulated separately again; "
    "see WA.2 section D."))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS BEFORE YOU APPLY")
flow.append(k.body(
    "Every line below is a condition a statute imposes or a fact your permit "
    "counter will ask you to stand behind. Work down it with a pen. If you "
    "cannot check a box, resolve it before you file — not after."))

flow += k.check_table("Step 1 — Ownership and purpose", [
    ("Land is owned in your name as of the permit application date",
     [("Recorded:", 0.5), ("Parcel #:", 0.5)]),
    "You are <b>not</b> undertaking the work for the purpose of selling, "
    "demolishing, or leasing the property, and no purchase, listing, or lease "
    "agreement exists or is contemplated",
    "If you have owned the property less than twelve months, you have "
    "considered RCW 18.27.090(11) and are not building to lease or sell",
    ("If any of that is uncertain, you have written advice before applying",
     [("Date:", 0.5), ("From:", 0.5)]),
], notes_header="Notes / evidence")

flow += k.check_table("Step 2 — The trades you intend to do yourself", [
    "Electrical: you own the property, and the house is not being built for "
    "rent, sale, or lease",
    ("You have confirmed with L&amp;I which property owner electrical permit "
     "applies to your job and what it costs",
     [("Confirmed:", 0.5), ("Permit type:", 0.5)]),
    "Plumbing: you own the property (no rent/sale/lease condition applies "
    "here) and you are not touching medical gas",
    "Mechanical: local permit identified; EPA 608 certification held by "
    "whoever opens a refrigerant circuit",
    "You understand that every one of these still needs its own permit and "
    "inspection",
], notes_header="Notes / evidence")

flow += k.check_table("Step 3 — Everyone you are paying", [
    ("Each contractor's registration verified at secure.lni.wa.gov/verify/",
     [("Verified on:", 1.0)]),
    "Electrical contractor's chapter 19.28 license verified separately from "
    "contractor registration; bond and insurance checked, not assumed",
    "You have received the written notice about unregistered contractors that "
    "RCW 18.27.110(2)(b) requires the permit office to give you",
    "Nobody is being paid in a way that quietly makes you their employer — if "
    "you are unsure, get advice before the first payment",
], notes_header="Notes / evidence")

# ---------------------------------------------------------------- losing it
flow += k.h2_tight("WHAT TAKES THE EXEMPTION AWAY")
flow.append(k.bullet(
    "Performing the activities of a contractor on your own property <b>for "
    "the purpose of selling, demolishing, or leasing</b> it. (18.27.090(12))"))
flow.append(k.bullet(
    "Acting as a contractor to lease or sell improved property you have owned "
    "for <b>less than twelve months</b>. (18.27.090(11))"))
flow.append(k.bullet(
    "Not owning the property — unless it is your personal residence, which is "
    "the other half of subsection (12)."))
flow.append(k.bullet(
    "For <b>electrical</b> only: building a new house intended for rent, "
    "sale, or lease without the L&amp;I affidavit route, or working on "
    "property offered for sale within 12 months of acquiring it. "
    "(19.28.261(1)(a), (b))"))
flow.append(k.bullet(
    "Falsifying information to obtain any of it — which forfeits the building "
    "permit outright. (18.27.110(3))"))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("Own-property and personal-residence exemption from contractor "
     "registration, and the selling/demolishing/leasing carve-out",
     "RCW 18.27.090(12)"),
    ("Owner contracting with a registered contractor; the twelve-month "
     "carve-out", "RCW 18.27.090(11)"),
    ("$500 casual, minor or inconsequential threshold, and the anti-splitting "
     "rule", "RCW 18.27.090(9)"),
    ("Owner performing maintenance, repair and alteration on own properties",
     "RCW 18.27.090(13)"),
    ("Certified electricians and plumbers exempt from contractor registration "
     "within the scope of their certification", "RCW 18.27.090(14)"),
    ("Permit office must print the registration number and give written "
     "notice about unregistered contractors", "RCW 18.27.110(2)"),
    ("A permit obtained by falsifying an exemption is forfeited",
     "RCW 18.27.110(3)"),
    ("Homeowner electrical exemption; the rent/sale/lease and 12-month "
     "carve-outs; the 24-month affidavit route for buildings intended for "
     "rent, sale or lease", "RCW 19.28.261(1)"),
    ("Householder may give and receive help from friends, neighbors and "
     "relatives", "RCW 19.28.261(6); 18.106.150(6)"),
    ("No electrical work concealed before approval; no utility connection "
     "before approval", "RCW 19.28.101(4), (5)"),
    ("Incorporated cities and towns — not counties — may run their own "
     "electrical programs", "RCW 19.28.010(3), (4)"),
    ("Homeowner plumbing exemption, with no rent/sale/lease condition; "
     "medical gas excluded", "RCW 18.106.150(1), (7)"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "wa-permit-kit",
                       "WA.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
