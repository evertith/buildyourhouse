#!/usr/bin/env python3
"""VA.1 Owner-Builder Exemption Walkthrough.

Every Virginia claim in this document was read out of the statute text at
law.lis.virginia.gov in August 2026 and is cited on-page. Where the statute
is silent or localities differ, the document says so and gives the
verification step.

Verified sources:
  § 54.1-1100      "contractor" defined; Class C starts over $1,000;
                   Class B $30,000–$150,000; Class A $150,000+
  § 54.1-1101(A)   "The provisions of this chapter shall not apply to:" —
                   the exemption switches off the whole licensing chapter
  § 54.1-1101(A)(7) one primary residence owned by him, for his own use,
                   in any 24-month period
  § 54.1-1101(A)(8),(10)  family-gift and own-rental exemptions
  § 54.1-1101(B)   CO before conveying to a third-party purchaser; Class 1
                   misdemeanor; third violation within 36 months a Class 6
                   felony
  § 54.1-1101(C)   exempt persons must still comply with the USBC
  § 54.1-1111      written statement + affidavit at permit time; the
                   official may not issue the permit without it
  § 54.1-1128/1129 tradesman defined by work "for the general public for
                   compensation"; licensure command
  § 54.1-1131(C)   the only express tradesman exemption: under-$250
                   single-family work
  § 54.1-1115/.01  unenforceable contracts; Class 1 misdemeanor; sole
                   responsibility for hiring the uncredentialed
  § 65.2-101/800   workers' comp reaches three or more regular employees;
                   subject employers must insure
  § 65.2-302(A)    statutory-employer liability turns on the owner's own
                   "trade, business or occupation"

Still deliberately hedged: any resale holding period (the statute states
none, so this document prints none); each locality's name for the exemption
affidavit form; the self-performed-trades conclusion (a synthesis of two
statutes, flagged as such, with the confirm-with-your-official step); and
statutory-employer exposure, which is framed as risk management, not legal
assurance — no Virginia statute was found conditioning a residential permit
on workers' comp certification, and the document says exactly that.
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

FORM_ID = "VA.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "Exemption & Qualification"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "How Virginia's owner-builder exemption actually works — the one "
    "sentence that creates it, the statement you sign to claim it, and the "
    "strings the Code of Virginia attaches.")

flow.append(k.disclaimer(
    "Statute text was read at law.lis.virginia.gov in August 2026; statutes "
    "change."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION")
flow.append(k.body(
    "Virginia licenses anyone who contracts to build for others — and the "
    "lowest license class, Class C, starts at contracts of just over "
    "<b>$1,000</b>. The exemption statute carves you out of the entire "
    "licensing chapter: you may perform or supervise the construction of "
    "<b>one primary residence owned by you and for your own use in any "
    "24-month period</b> without a contractor license. You claim it by "
    "filing a written statement, supported by an affidavit, when you pull "
    "the permit — and the building official is forbidden to issue the "
    "permit without it."))
flow.append(k.cite(
    "Code of Virginia § 54.1-1100 (definitions and license classes); "
    "§ 54.1-1101(A)(7) (the exemption); § 54.1-1111 (the statement and "
    "affidavit)."))

rows = [
    [k.cellp("What does the license law govern, then?"),
     k.cellp("Contracting to build <i>for others</i> \"for a fixed price, "
             "commission, fee, or percentage.\" It governs the people you "
             "hire, not you — and it reaches them from just over $1,000 "
             "per job.")],
    [k.cellp("Must you own the home?"),
     k.cellp("Yes. The residence must be \"owned by him and for his own "
             "use\" — a house built to sell or to rent is not for your "
             "own use.")],
    [k.cellp("How many can you build?"),
     k.cellp("No more than <b>one</b> primary residence in any 24-month "
             "period.")],
    [k.cellp("Is there a fixed holding period after completion?"),
     k.cellp("The statute states none — Virginia polices intent through "
             "\"for his own use,\" not a resale clock. This kit prints no "
             "waiting period, because none appears in the section text; "
             "see the certificate-of-occupancy string below before you "
             "plan any early sale.")],
    [k.cellp("What do you sign, and who checks it?"),
     k.cellp("A written statement, supported by an affidavit, that you are "
             "not subject to licensure (§ 54.1-1111). The building "
             "official may not lawfully issue the permit without your "
             "license number or that evidence of exemption.")],
]
flow.append(k.ref_table(
    "The exemption at a glance",
    [k.cellp("Question", bold=True), k.cellp("Virginia's answer", bold=True)],
    rows, [2.7 * inch, CW - 2.7 * inch]))

# ---------------------------------------------------------------- the exemption
flow += k.h2_tight("THE EXEMPTION ITSELF — § 54.1-1101(A)(7)")
flow.append(k.body(
    "Section 54.1-1101(A) opens: \"<i>The provisions of this chapter shall "
    "not apply to:</i>\" — and the chapter it switches off is the whole of "
    "Chapter 11 of Title 54.1, which contains both the contractor article "
    "and the tradesman article. Subdivision (A)(7) is yours:"))

flow.append(k.callout("The operative sentence — quoted in full", [
    Paragraph("\"<i>Any person who performs or supervises the construction, "
              "removal, repair, or improvement of no more than one primary "
              "residence owned by him and for his own use during any "
              "24-month period</i>\"", S["body"]),
    Paragraph("Three limits in one sentence: <b>one</b> residence, "
              "<b>owned by you</b>, <b>for your own use</b> — and the "
              "24-month window that stops the exemption from becoming a "
              "spec-building business. \"Performs or supervises\" means "
              "you may do the work yourself, hire it out, or both.",
              S["body"]),
]))
flow.append(k.cite("Code of Virginia § 54.1-1101(A)(7)."))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "Read \"<b>for his own use</b>\" closely — it is Virginia's "
    "anti-speculation line. The statute sets no occupancy clock and no "
    "resale waiting period; it polices your <b>intent</b>. A house you "
    "planned to sell or rent from the start was never for your own use, "
    "no matter how long you hold it. If your plans are genuinely "
    "uncertain, get your building department's position — and anything "
    "from DPOR — in writing before you pull the permit."))

flow.append(k.callout("Two related exemptions worth knowing", [
    Paragraph("<b>The family gift</b> — subdivision (A)(8) exempts \"<i>any "
              "person who performs or supervises the construction, removal, "
              "repair, or improvement of a house upon his own real property "
              "as a bona fide gift to a member of his immediate "
              "family</i>.\"", S["body"]),
    Paragraph("<b>Your own rentals — repair and improvement only</b> — "
              "subdivision (A)(10) exempts \"<i>any person who performs or "
              "supervises the repair or improvement of residential dwelling "
              "units owned by him</i>\" that are subject to the Virginia "
              "Residential Landlord and Tenant Act. It does not cover "
              "building a new rental.", S["body"]),
]))
flow.append(k.cite("Code of Virginia § 54.1-1101(A)(8), (A)(10)."))

# ---------------------------------------------------------------- the CO string
flow += k.h2_tight("THE STRING ATTACHED — A CERTIFICATE OF OCCUPANCY "
                   "BEFORE ANY SALE")
flow.append(k.body(
    "The exemption statute's own title warns you: \"Exemptions; failure to "
    "obtain certificate of occupancy; penalties.\" Subsection (B) requires "
    "an owner who built under the exemption to obtain a certificate of "
    "occupancy \"<i>for any building constructed, repaired or improved by "
    "him prior to conveying such property to a third-party purchaser</i>\" "
    "— unless the purchaser waives the requirement in writing. Violating "
    "that is a <b>Class 1 misdemeanor</b>; a third violation within 36 "
    "months is a <b>Class 6 felony</b>."))
flow.append(k.body(
    "And subsection (C) closes the loop that matters most day to day: "
    "exempt persons \"<i>shall comply with the provisions of the Uniform "
    "Statewide Building Code</i>.\" <b>The exemption waives the license — "
    "never the permit, never the inspections, never the code.</b>"))
flow.append(k.cite("Code of Virginia § 54.1-1101(B), (C)."))

# ---------------------------------------------------------------- what you sign
flow += k.h2_tight("WHAT YOU SIGN AT THE COUNTER — § 54.1-1111")
flow.append(k.body(
    "Where a licensed contractor writes a license number on the "
    "application, you file \"<i>a written statement, supported by an "
    "affidavit, that he is not subject to licensure or certification as a "
    "contractor or subcontractor pursuant to this chapter</i>.\" The same "
    "section then binds the official: \"<i>It shall be unlawful for the "
    "building official or other authority to issue or allow the issuance "
    "of such permits unless the applicant has furnished his license or "
    "certificate number issued pursuant to this chapter or evidence of "
    "being exempt from the provisions of this chapter.</i>\""))
flow.append(k.callout("The form is local — the obligation is not", [
    Paragraph("There is no single statewide owner-exemption form. Each "
              "locality prints its own, commonly titled \"Contractor's "
              "License Exemption,\" \"Owner's Affidavit,\" or similar. Ask "
              "your building department for its version when you pick up "
              "the application package, and expect it to need notarizing. "
              "See <b>VA.5</b>.", S["body"]),
]))
flow.append(k.cite("Code of Virginia § 54.1-1111."))

# ---------------------------------------------------------------- trade work
flow += k.h2_tight("DOING YOUR OWN ELECTRICAL, PLUMBING, AND HVAC WORK")
flow.append(k.body(
    "Virginia licenses tradesmen — electricians, plumbers, and HVAC "
    "workers — in the <b>same Chapter 11</b> that the owner-builder "
    "exemption switches off. Two provisions do the work:"))

trade_rows = [
    [k.cellp("<b>Who is a \"tradesman\"</b>"),
     k.cellp("\"<i>any individual who engages in, or offers to engage in, "
             "work for the general public for compensation in the trades "
             "of electrical, plumbing and heating, ventilation and air "
             "conditioning.</i>\" Working on your own house is not working "
             "for the general public for compensation."),
     k.cellp("§ 54.1-1128")],
    [k.cellp("<b>The licensure command</b>"),
     k.cellp("\"<i>no individual shall engage in, or offer to engage in, "
             "work as a tradesman … unless he has been licensed</i>\" — "
             "but this command sits inside the chapter that "
             "§ 54.1-1101(A)(7) says \"shall not apply to\" you."),
     k.cellp("§ 54.1-1129")],
]
flow.append(k.ref_table(
    "The two statutes you read together",
    [k.cellp("Provision", bold=True), k.cellp("What it says", bold=True),
     k.cellp("Authority", bold=True)],
    trade_rows, [1.55 * inch, CW - 1.55 * inch - 1.15 * inch, 1.15 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "Honest label: this is a synthesis — confirm it before you rely on it", [
        Paragraph("Read together, the two statutes put an owner doing his "
                  "own electrical, plumbing, or HVAC work on his own "
                  "primary residence outside the licensing scheme. But no "
                  "Virginia statute says \"owners may wire their own "
                  "house\" in so many words, and some building departments "
                  "quiz owner applicants before issuing trade permits. "
                  "<b>Confirm with your building official, before you "
                  "plan on it, that they will issue you the trade "
                  "permits.</b> For the record, the only express exemption "
                  "in the tradesman article is trivial: § 54.1-1131(C) "
                  "covers single-family residence work \"<i>where the "
                  "value of the work performed is less than $250 and such "
                  "individual does not hold himself out to the general "
                  "public as a tradesman</i>.\"", S["body"]),
        Paragraph("<b>And a license is not a permit.</b> Exempt or not, "
                  "§ 54.1-1101(C) holds you to the USBC — every trade "
                  "still needs its permit and must pass its inspections. "
                  "Doing your own work without pulling those permits is "
                  "the single most expensive mistake in this kit, because "
                  "the remedy is opening up finished work.", S["body"]),
    ]))

# ---------------------------------------------------------------- workers comp
flow += k.h2_tight("WORKERS' COMPENSATION WHEN YOU HIRE PEOPLE")
flow.append(k.body(
    "Virginia's Workers' Compensation Act reaches an employer once "
    "<b>three or more employees</b> are regularly in service: the Act's "
    "definition of \"employee\" excludes \"<i>employees of any person, "
    "firm or private corporation … that has regularly in service less "
    "than three employees in the same business within this "
    "Commonwealth</i>\" (unless coverage is voluntarily elected). Once "
    "you are subject, § 65.2-800 is unequivocal: \"<i>Every employer "
    "subject to the compensation provisions of this title shall insure "
    "the payment of compensation to his employees in the manner "
    "hereinafter provided.</i>\" Hiring even a couple of helpers directly "
    "puts you close to that line — count heads before you do."))
flow.append(k.cite("Code of Virginia § 65.2-101 (definition of "
                   "\"Employee\"); § 65.2-800."))

flow.append(k.callout(
    "Your subs' workers — manage the risk, don't litigate it", [
        Paragraph("Section 65.2-302(A) makes an owner who subcontracts "
                  "work that is part of his own \"trade, business or "
                  "occupation\" liable for compensation to the sub's "
                  "workers as if \"<i>the worker had been immediately "
                  "employed by him</i>.\" Whether a one-time owner-builder "
                  "is \"in the trade or business\" of construction is a "
                  "question the statute does not answer — so do not bet "
                  "on the answer. <b>Require a current workers' "
                  "compensation certificate from every subcontractor "
                  "before they set foot on the site</b>, and keep the "
                  "certificates with this kit.", S["body"]),
        Paragraph("One contrast with other states: this kit found no "
                  "Virginia statute that conditions a residential building "
                  "permit on workers' compensation certification. Your "
                  "locality's application form may still ask — answer "
                  "whatever it asks accurately.", S["body"]),
    ]))
flow.append(k.cite("Code of Virginia § 65.2-302(A)."))

# ---------------------------------------------------------------- hiring subs
flow += k.h2_tight("THE PEOPLE YOU HIRE — LICENSES AND THE $1,000 LINE")
flow.append(k.body(
    "Your exemption does nothing for your subcontractors. Anyone who "
    "contracts <i>with you</i> is a contractor under § 54.1-1100, and the "
    "license classes are set by dollar value:"))

class_rows = [
    [k.cellp("<b>Class C</b>"),
     k.cellp("Single contract \"<i>over $1,000 but less than $30,000</i>\" "
             "(or under $250,000 of such work in any 12-month period)")],
    [k.cellp("<b>Class B</b>"),
     k.cellp("Single contract \"<i>$30,000 or more, but less than "
             "$150,000</i>\"")],
    [k.cellp("<b>Class A</b>"),
     k.cellp("Single contract \"<i>$150,000 or more</i>\" (or $1 million "
             "or more annually)")],
]
flow.append(k.ref_table(
    "DPOR contractor license classes — § 54.1-1100",
    [k.cellp("Class", bold=True), k.cellp("Contract value", bold=True)],
    class_rows, [1.15 * inch, CW - 1.15 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "So <b>every sub you hire for a job over $1,000 must hold at least a "
    "Class C license</b> in the right classification. Verify each one at "
    "DPOR's License Lookup, <b>dpor.virginia.gov</b>, before you sign — "
    "not after. Two more reasons beyond the law: an unlicensed "
    "contractor's contract \"<i>shall not be enforceable by the unlicensed "
    "contractor</i>\" unless he substantially performed in good faith and "
    "\"<i>did not have actual knowledge that a license or certificate was "
    "required</i>\" (§ 54.1-1115(C)) — which protects you very little "
    "when the work is bad. And knowing violations of the licensing "
    "chapter are <b>Class 1 misdemeanors</b> (§ 54.1-1115). If a "
    "contractor uses uncredentialed workers, § 54.1-1115.01 makes that "
    "contractor \"<i>solely responsible for any monetary penalty or other "
    "sanction</i>\" — put it in your subcontract anyway."))
flow.append(k.cite(
    "Code of Virginia § 54.1-1100; § 54.1-1115(A)–(C); § 54.1-1115.01. "
    "License lookup: dpor.virginia.gov → License Lookup."))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS BEFORE YOU APPLY")
flow.append(k.body(
    "Every line below is a condition the statutes impose or a fact the "
    "permit counter will ask you to prove. Work down it with a pen. If "
    "you cannot check a box, resolve it before you file — not after."))

flow += k.check_table("Step 1 — Ownership and intent", [
    ("Land is owned in your name as of the permit application date",
     [("Deed book/page:", 0.55), ("Parcel ID:", 0.45)]),
    "The house will be your primary residence, for your own use — not a "
    "spec house, flip, rental, or a home built mainly to sell",
    "You have not built or supervised another primary residence under this "
    "exemption within the past 24 months",
    "If a sale might come early: you understand a certificate of occupancy "
    "must issue before conveying to a buyer, absent the buyer's written "
    "waiver (§ 54.1-1101(B))",
    ("If intent is uncertain, you have your building department's position "
     "in writing before applying",
     [("Date requested:", 0.5), ("Response:", 0.5)]),
], notes_header="Notes / evidence")

flow += k.check_table("Step 2 — What you sign and who you hire", [
    "Your locality's owner-exemption statement/affidavit form obtained — "
    "names vary; ask for the \"contractor exemption\" or \"owner "
    "affidavit\" form",
    "Written statement supported by an affidavit ready to sign at "
    "application (§ 54.1-1111) — expect to notarize",
    "Every subcontractor whose contract exceeds $1,000 holds a current "
    "DPOR license of the right class",
    ("Each license verified at dpor.virginia.gov → License Lookup",
     [("Verified on:", 1.0)]),
    "Workers' compensation certificate collected from every subcontractor",
    "If self-performing electrical, plumbing, or HVAC: your building "
    "official has confirmed they will issue you the trade permits",
], notes_header="Notes / evidence")

flow.append(k.body(
    "<b>Step 3 — the paperwork itself</b> (the application package, the "
    "lien agent line, septic and well, erosion control, energy "
    "documentation) is worked in <b>VA.2 Permit Application Checklist</b>, "
    "and each document is described in <b>VA.5 Forms &amp; Documents "
    "Index</b>."))

# ---------------------------------------------------------------- losing it
flow += k.h2_tight("WHAT TAKES THE EXEMPTION AWAY")
flow.append(k.bullet(
    "Building or supervising <b>more than one</b> primary residence in a "
    "24-month period."))
flow.append(k.bullet("Not owning the residence you are building."))
flow.append(k.bullet(
    "A house that was never <b>for your own use</b> — built to sell, to "
    "rent, or for someone outside the family-gift exemption."))
flow.append(k.bullet(
    "Conveying to a buyer before the certificate of occupancy issues, "
    "without the buyer's written waiver."))
flow.append(k.bullet(
    "Treating the exemption as a pass on permits or inspections — "
    "§ 54.1-1101(C) holds you to the USBC in full."))
flow.append(Spacer(1, 4))
flow.append(k.body(
    "Consequences the statutes actually name: selling without the CO is a "
    "<b>Class 1 misdemeanor</b>, and a third violation within 36 months "
    "is a <b>Class 6 felony</b> (§ 54.1-1101(B)); knowing violations of "
    "the licensing chapter are <b>Class 1 misdemeanors</b> "
    "(§ 54.1-1115)."))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("Contracting for others requires a DPOR license; Class C over "
     "$1,000, Class B at $30,000, Class A at $150,000", "§ 54.1-1100"),
    ("The exemption switches off the entire licensing chapter — "
     "contractors and tradesmen both", "§ 54.1-1101(A)"),
    ("One primary residence, owned by you, for your own use, per 24 "
     "months", "§ 54.1-1101(A)(7)"),
    ("Family-gift exemption; own-rentals repair/improvement exemption",
     "§ 54.1-1101(A)(8), (A)(10)"),
    ("CO before conveying to a third-party purchaser, absent written "
     "waiver; Class 1 misdemeanor; third violation in 36 months a Class 6 "
     "felony", "§ 54.1-1101(B)"),
    ("Exempt persons must comply with the USBC — permits and inspections "
     "never waived", "§ 54.1-1101(C)"),
    ("Written statement + affidavit; unlawful for the official to issue "
     "without it", "§ 54.1-1111"),
    ("\"Tradesman\" reaches work for the general public for "
     "compensation; the licensure command sits inside the exempted "
     "chapter", "§ 54.1-1128; § 54.1-1129"),
    ("Only express tradesman exemption: under $250, single-family, no "
     "holding out", "§ 54.1-1131(C)"),
    ("Workers' comp reaches employers of three or more; subject employers "
     "must insure", "§ 65.2-101; § 65.2-800"),
    ("Statutory-employer liability turns on the owner's own trade, "
     "business or occupation", "§ 65.2-302(A)"),
    ("Unlicensed contractor's contract generally unenforceable; knowing "
     "violations Class 1 misdemeanor; hirer of the uncredentialed solely "
     "responsible", "§ 54.1-1115; § 54.1-1115.01"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "va-permit-kit",
                       "VA.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
