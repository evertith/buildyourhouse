#!/usr/bin/env python3
"""NC.1 Owner-Builder Exemption Walkthrough.

Every North Carolina claim in this document was read out of the statute text
at ncleg.gov in August 2026 and is cited on-page. Where the statute is silent
or counties differ, the document says so and gives the verification step.

Verified sources:
  G.S. 87-1     general contractor defined; $40,000; owner exemption (b)(2)
  G.S. 87-13    unlicensed contracting = Class 2 misdemeanor
  G.S. 87-14    permit prerequisites; the verified affidavit; workers' comp
  G.S. 87-21    plumbing/heating "engaged in the business" definition
  G.S. 87-43.1  electrical own-property exception (5a)
  G.S. 97-2     workers' comp applies at three or more employees
  G.S. 160D-1110/1111/1112/1113/1115/1116  permits, expiry, inspections, CO
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

FORM_ID = "NC.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "Exemption & Qualification"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "How North Carolina's owner-builder exemption actually works — the two "
    "statutes that create it, the affidavit you sign to claim it, and the "
    "conditions that take it away.")

flow.append(k.disclaimer(
    "Statute text was read at ncleg.gov in August 2026; statutes change."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION")
flow.append(k.body(
    "North Carolina requires a licensed general contractor for construction "
    "work costing <b>$40,000 or more</b>. The statute that creates that "
    "requirement also carves you out of it: if you own the land and the "
    "building is intended solely for occupancy by you and your family, you "
    "may act as your own general contractor at any project cost. You claim "
    "that carve-out by signing a verified affidavit when you pull the permit, "
    "and you keep it by actually living in the house."))
flow.append(k.cite(
    "N.C.G.S. § 87-1(a) and § 87-1(b)(2). The $40,000 figure replaced $30,000 "
    "effective October 1, 2023 (S.L. 2023-108, s. 2(a)) — older guides and "
    "older county handouts still print $30,000."))

rows = [
    [k.cellp("What is the $40,000 threshold, then?"),
     k.cellp("It is the point at which <i>contracting</i> requires a license. "
             "It governs the people you hire, not you.")],
    [k.cellp("Must you own the land, and live in it?"),
     k.cellp("Both. Land owned by you, and the building solely occupied by "
             "you and your family after completion")],
    [k.cellp("For how long?"),
     k.cellp("At least 12 months following completion, or the State presumes "
             "you never qualified")],
    [k.cellp("What do you sign, and who checks it?"),
     k.cellp("A verified affidavit at permit application (§ 87-14(a)(1)); "
             "the inspector forwards it to the NC Licensing Board, which "
             "verifies your claim")],
]
flow.append(k.ref_table(
    "The exemption at a glance",
    [k.cellp("Question", bold=True), k.cellp("North Carolina's answer", bold=True)],
    rows, [2.7 * inch, CW - 2.7 * inch]))

# ---------------------------------------------------------------- the exemption
flow += k.h2_tight("THE EXEMPTION ITSELF — N.C.G.S. § 87-1(b)(2)")
flow.append(k.body(
    "The licensing article does not apply to \"<i>any person, firm, or "
    "corporation who constructs or alters a building on land owned by that "
    "person, firm, or corporation</i>\" provided both of the following are "
    "true. Both. Failing either one puts you back under the license "
    "requirement."))

flow.append(k.callout("The two conditions — both required", [
    Paragraph("<b>(i)</b> The building is intended <b>solely for occupancy by "
              "that person and his family</b> after completion.", S["body"]),
    Paragraph("<b>(ii)</b> The person <b>complies with G.S. 87-14</b> — the "
              "affidavit, and proof of workers' compensation coverage as "
              "Chapter 97 requires it.", S["body"]),
]))
flow.append(Spacer(1, 8))
flow.append(k.body(
    "Read condition (i) closely. It says <b>solely for occupancy by you and "
    "your family</b> — not \"primary residence,\" and it never mentions "
    "selling or renting. Those consequences arrive through the presumption "
    "below: a house you have sold or rented is no longer solely occupied "
    "by you."))

flow.append(k.callout(
    "The 12-month presumption — the sentence that ends most exemptions", [
        Paragraph("\"<i>If the building is not occupied solely by the person "
                  "and his family, firm, or corporation for at least 12 "
                  "months following completion, it shall be presumed that the "
                  "person, firm, or corporation did not intend the building "
                  "solely for occupancy by that person and his family, firm, "
                  "or corporation.</i>\"", S["body"]),
        Paragraph("Two details people get wrong. First, the clock runs from "
                  "<b>completion</b> — not from the certificate of "
                  "occupancy, and the section does not define completion. "
                  "Second, it is a <b>presumption</b>, not an automatic "
                  "crime: it shifts the burden onto you to prove you did "
                  "intend to live there. Neither point is a reason to cut it "
                  "close. If you may need to sell or rent inside a year, get "
                  "the Board's position in writing before you pull the "
                  "permit.", S["body"]),
    ]))
flow.append(k.cite("N.C.G.S. § 87-1(b)(2), final sentence."))

# ---------------------------------------------------------------- affidavit
flow += k.h2_tight("WHAT YOU SIGN — THE VERIFIED AFFIDAVIT, § 87-14(a)(1)")
flow.append(k.body(
    "Before the permit issues, an applicant claiming the § 87-1(b)(2) "
    "exemption must \"<i>execute a verified affidavit</i>\" attesting to "
    "three things. Verified means sworn — you are signing under oath, and "
    "the statute at § 87-14(b) makes it a misdemeanor for the inspector to "
    "issue the permit without it."))

flow.append(k.checklist([
    "a. That you are the owner of the property on which the building is "
    "being constructed.",
    "b. That you will personally superintend and manage all aspects of the "
    "construction, and will not delegate that duty to any person not "
    "licensed as a general contractor.",
    "c. That you will be personally present for all inspections required by "
    "the North Carolina State Building Code — unless the plans were drawn "
    "and sealed by an architect licensed under Chapter 83A.",
])) 
flow.append(Spacer(1, 6))
flow.append(k.body(
    "Item (b) is the one owner-builders misread. It does <b>not</b> stop you "
    "from hiring subcontractors — it stops you from handing the "
    "superintending role to an unlicensed person and calling yourself the "
    "builder on paper. You must actually run the job. Anyone you hire to run "
    "it for you at $40,000 or more must hold a general contractor license."))
flow.append(k.body(
    "The inspections department \"<i>shall transmit a copy of the affidavit "
    "to the Board</i>,\" which verifies you were entitled to the exemption. "
    "If the Board decides you were not, the permit is revoked under "
    "§ 160D-1115. Contracting without a required license is a <b>Class 2 "
    "misdemeanor</b> under § 87-13."))
flow.append(k.cite(
    "N.C.G.S. § 87-14(a)(1)a–c; § 87-13; § 160D-1115."))

flow.append(k.body(
    "<b>Four positions the Licensing Board states plainly</b> in its guidance "
    "for inspectors and permit clerks. <b>No power of attorney</b> — you "
    "cannot assign someone to act as owner-builder for you. <b>Only the "
    "person on the deed</b> may apply; if a husband or wife is listed "
    "individually, the other spouse cannot. <b>\"Family\" is narrow</b>: "
    "\"<i>a spouse or other family member who lives in the same "
    "household</i>,\" plus guests and social invitees where no consideration "
    "is received. And <b>land does not count toward the $40,000</b> — "
    "project cost under § 87-10(a1) is \"<i>the value of the project minus "
    "the cost of the land and ancillary improvements to the land</i>.\""))
flow.append(k.cite(
    "NC Licensing Board for General Contractors, FAQ for inspectors and "
    "permit clerks (nclbgc.org), read August 2026 — administrative positions "
    "rather than statutory text, but the Board verifies your affidavit, so "
    "these are what get applied to you. Check any contractor's licence at "
    "nclbgc.org/license-search/."))

# ---------------------------------------------------------------- inspections
flow += k.h2_tight("YOU MUST BE AT EVERY INSPECTION — § 160D-1113")
flow.append(k.body(
    "This is not a courtesy expectation; it is a separate statutory command "
    "on the inspector: \"<i>If a building permit has been obtained by an "
    "owner exempt from licensure under G.S. 87-1(b)(2), no inspection shall "
    "be conducted without the owner being present, unless the plans for the "
    "building were drawn and sealed by an architect licensed pursuant to "
    "Chapter 83A of the General Statutes.</i>\""))

flow.append(k.callout("Architect — not engineer", [
    Paragraph("Both § 87-14(a)(1)c and § 160D-1113 name an <b>architect</b> "
              "licensed under Chapter 83A. Neither says \"or engineer.\" "
              "Plenty of guidance online — including guidance written for "
              "North Carolina — says \"architect or engineer.\" The statutory "
              "text does not. If you are planning to skip inspections on the "
              "strength of an engineer's seal, confirm that with your "
              "inspections department in writing first.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "Practical consequence: budget your own time for every inspection on the "
    "job, on the inspector's schedule, not yours. For a full house that is "
    "commonly a dozen or more separate visits across building, electrical, "
    "plumbing, and mechanical. See <b>NC.3</b> for the sequence."))

# ---------------------------------------------------------------- workers comp
flow += k.h2_tight("WORKERS' COMPENSATION — § 87-14(a)(2)")
flow.append(k.body(
    "The permit statute requires you to \"<i>furnish proof that the applicant "
    "has in effect Workers' Compensation insurance as required by Chapter "
    "97</i>.\" The operative words are <b>as required by Chapter 97</b>. "
    "Chapter 97 defines covered employment as private employment "
    "\"<i>in which three or more employees are regularly employed</i>\" "
    "(§ 97-2(1))."))
flow.append(k.body(
    "So an owner-builder who hires licensed subcontractors and regularly "
    "employs nobody is generally not an employer Chapter 97 reaches. That is "
    "why NC jurisdictions hand you an affirmation form rather than demanding "
    "a policy. <b>The form and its wording are local.</b> Ask your "
    "inspections department which form they use and how they want the "
    "no-employee case stated — and note that hiring even a couple of helpers "
    "directly can change the answer."))
flow.append(k.cite(
    "N.C.G.S. § 87-14(a)(2); § 97-2(1). Whether any given worker on your job "
    "counts as your employee is a fact question — if you are paying people "
    "directly, get advice before you sign."))

# ---------------------------------------------------------------- trade work
flow += k.h2_tight("DOING YOUR OWN ELECTRICAL, PLUMBING, AND MECHANICAL WORK")
flow.append(k.body(
    "The general contractor exemption and the trade licensing exemptions are "
    "<b>different statutes with different tests</b>. Qualifying for one does "
    "not qualify you for the others. Here is what each one actually says."))

trade_rows = [
    [k.cellp("<b>Electrical</b>"),
     k.cellp("The electrical licensing article does not apply to a person "
             "\"installing, maintaining, altering or repairing electric work "
             "… <i>upon that person's own property and for that person's own "
             "benefit when such property is not intended at the time for "
             "rent, lease, or sale</i>.\""),
     k.cellp("§ 87-43.1(5a)")],
    [k.cellp("<b>Plumbing &amp; heating</b>"),
     k.cellp("Licensing attaches to those \"engaged in the business.\" A "
             "person who installs on property \"<i>intended for sale or to be "
             "used primarily for rental</i>\" is deemed engaged in the "
             "business even without pay. Your own non-rental, non-resale "
             "home falls outside that."),
     k.cellp("§ 87-21(a)(5)")],
    [k.cellp("<b>Mechanical / HVAC</b>"),
     k.cellp("Same plumbing-and-heating article governs the heating side. "
             "Handling refrigerant is a separate <b>federal</b> matter: EPA "
             "Section 608 technician certification is required to open a "
             "refrigerant circuit, and refrigerant may not be sold to "
             "uncertified persons."),
     k.cellp("§ 87-21; 40 C.F.R. Part 82, Subpart F")],
]
flow.append(k.ref_table(
    "Trade-by-trade — what the licensing statutes say",
    [k.cellp("Trade", bold=True), k.cellp("The statutory test", bold=True),
     k.cellp("Authority", bold=True)],
    trade_rows, [1.15 * inch, CW - 1.15 * inch - 1.55 * inch, 1.55 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout("A permit is still required for every trade", [
    Paragraph("Being exempt from a <b>license</b> is not being exempt from a "
              "<b>permit</b>. Section 160D-1110(a) requires permits for the "
              "building, for plumbing systems, for heating and cooling "
              "equipment, and for electrical wiring — separately. Doing your "
              "own work without pulling those permits is the single most "
              "expensive mistake in this kit, because the remedy is opening "
              "up finished work.", S["body"]),
]))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS BEFORE YOU APPLY")
flow.append(k.body(
    "Every line below is a condition the statutes impose or a fact the "
    "permit counter will ask you to prove. Work down it with a pen. If you "
    "cannot check a box, resolve it before you file — not after."))

flow += k.check_table("Step 1 — Ownership and intent", [
    ("Land is owned in your name (or your firm's) as of the permit "
     "application date", [("Deed book/page:", 0.55), ("Parcel ID:", 0.45)]),
    "You intend the finished building solely for occupancy by you and your "
    "family — not as a rental, spec house, flip, or second home you will not "
    "occupy",
    "You can hold it, occupied by your household, for at least 12 months "
    "following completion",
    "No purchase, lease, or listing agreement for the property exists or is "
    "contemplated inside that window",
    ("If any of the above is uncertain, you have the Board's written "
     "position before applying", [("Date requested:", 0.5), ("Response:", 0.5)]),
], notes_header="Notes / evidence")

flow += k.check_table("Step 2 — What you are swearing to", [
    "You will personally superintend and manage all aspects of construction, "
    "and are not handing that role to an unlicensed person acting as your de "
    "facto builder",
    "Any contractor you hire whose own contract is $40,000 or more holds a "
    "current NC general contractor license",
    ("License verified at the NC Licensing Board (nclbgc.org) for each such "
     "contractor", [("Verified on:", 1.0)]),
    "You will be personally present at every required inspection",
    "You understand the architect-sealed-plans exception is the only "
    "statutory way out of that",
], notes_header="Notes / evidence")

flow.append(k.body(
    "<b>Step 3 — the paperwork itself</b> (owner exemption affidavit, "
    "workers' compensation form, lien agent designation, and everything your "
    "county adds on top) is worked in <b>NC.2 Permit Application "
    "Checklist</b>, and each document is described in <b>NC.5 Forms &amp; "
    "Documents Index</b>."))

# ---------------------------------------------------------------- losing it
flow += k.h2_tight("WHAT TAKES THE EXEMPTION AWAY")
flow.append(k.bullet(
    "Selling, leasing, or renting the home — including short-term rental — so "
    "that it is not solely occupied by you and your family for 12 months "
    "following completion."))
flow.append(k.bullet("Not owning the land the building sits on."))
flow.append(k.bullet(
    "Handing day-to-day superintendence to an unlicensed person while your "
    "name stays on the permit."))
flow.append(k.bullet(
    "Building something you never intended to live in — a spec house, a "
    "rental, an investment flip."))
flow.append(k.bullet(
    "Signing the affidavit and then not appearing at inspections, absent "
    "architect-sealed plans."))
flow.append(Spacer(1, 4))
flow.append(k.body(
    "Consequences the statutes actually name: the Board reports the "
    "exemption invalid and the <b>permit is revoked</b> (§ 160D-1115); "
    "unlicensed contracting is a <b>Class 2 misdemeanor</b> (§ 87-13); and "
    "occupying a building before the certificate of compliance issues is a "
    "<b>Class 1 misdemeanor</b> (§ 160D-1116(c))."))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("$40,000 triggers the general contractor license requirement",
     "G.S. 87-1(a)"),
    ("Owner exemption: own the land, building solely for your family's "
     "occupancy", "G.S. 87-1(b)(2)"),
    ("12-month sole-occupancy presumption, running from completion",
     "G.S. 87-1(b)(2)"),
    ("Threshold rose from $30,000 to $40,000 on October 1, 2023",
     "S.L. 2023-108, s. 2(a)"),
    ("Verified affidavit, its three attestations, and Board review; permit "
     "revoked if the claim is invalid", "G.S. 87-14(a)(1); 160D-1115"),
    ("Workers' comp proof \"as required by Chapter 97,\" which reaches "
     "employers of three or more", "G.S. 87-14(a)(2); 97-2(1)"),
    ("Project cost excludes the land; Board positions on the exemption",
     "G.S. 87-10(a1); nclbgc.org FAQ"),
    ("No inspection without the owner present; architect-sealed exception",
     "G.S. 160D-1113"),
    ("Own-property electrical work exception", "G.S. 87-43.1(5a)"),
    ("Plumbing/heating licensing turns on sale or rental intent",
     "G.S. 87-21(a)(5)"),
    ("Separate permits for building, plumbing, mechanical, electrical",
     "G.S. 160D-1110(a)"),
    ("Unlicensed contracting is a Class 2 misdemeanor", "G.S. 87-13"),
    ("Occupying before the certificate of compliance is a Class 1 misdemeanor",
     "G.S. 160D-1116(c)"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "out", "nc-permit-kit",
                       "NC.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
