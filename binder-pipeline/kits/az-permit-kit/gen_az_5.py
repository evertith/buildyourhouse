#!/usr/bin/env python3
"""AZ.5 Forms & Documents Index.

Every document an owner-builder will meet in Arizona, named as the agency
names it, with what it is, when it happens and where it comes from — and the
30-day clarification letter, which is the one form the reader writes rather
than fills in.

Two negative sections carry real weight here. "What Arizona does not require"
exists because owner-builders arriving from other states budget for a state
trade license, a statewide energy code and residential sprinklers, none of
which Arizona has — and because the "once per 24 months" and "live in it two
years" rules people quote are not in the statute. "What you may do yourself"
exists because Arizona is unusually generous about it: an owner may install a
conventional septic system and, after an exam, drill their own exempt well.

Verified sources:
  § 32-1169(A), (B)     the statement; its content; unsworn falsification
  Jurisdiction form names (§ 3.6 of the dossier)   Tucson, Scottsdale, Peoria,
                        Lake Havasu City, Buckeye, Glendale, Casa Grande,
                        Sierra Vista, La Paz, Mohave, Gila, Santa Cruz
  § 32-1132(B)(1), (C); § 32-1162(A)   recovery fund; complaint window
  § 32-1158(A), (B)     contract contents; copies and receipts
  § 33-1002(A)(2)       the recorded deed
  § 33-992.01(B), (C)   preliminary twenty-day notice
  ADEQ form DWS 402 (rev. April 2025); A.A.C. R18-9-A301(D); A309(C); A312(C)
    row 2; A316; La Paz "Well-Property Line 50ft Setback Waiver"   septic
  § 45-596(A), (D), (F), (L); § 45-595(D); § 45-600; A.A.C. R12-15-807, 809
                        wells
  § 23-902(D); § 23-961(N)   independent-contractor agreement; sole-proprietor
                        waiver
  Cochise OBA Sec. 6; Coconino AMMP page   the recorded notices
  § 36-1681(E)          the pool safety notice
  § 9-839; § 11-1609    the clarification letter, element by element
  § 11-321(A); § 11-815(B); § 11-865(A)(1)   what needs no permit
  § 9-807; § 11-861(E); § 34-451; § 32-1101(B); § 9-467(E), (F); § 11-321(E),
    (H); § 9-468; § 11-323   what Arizona does not require
  § 32-1121(A)(5); A.A.C. R18-9-A309(C)(1), (2), A310(H); § 45-595(D);
    R12-15-807          what you may do yourself

DELIBERATELY NOT CLAIMED:
  - A form number for any local permit application or owner-builder
    statement. Each jurisdiction prints its own; write-in lines instead.
  - An ROC owner-builder notice. None was found on the Registrar's pages
    read; the statute is cited instead.
  - Any fee beyond the two ADWR notice fees fixed in § 45-596(L).
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
sec = k.sec
ars = k.ars
aac = k.aac
NB = k.NB

FORM_ID = "AZ.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Forms & Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document you will meet, named as the agency names it — the "
    "letter that answers any \"varies locally\" question in thirty days — "
    "and the things Arizona never asks you for.")

flow.append(k.disclaimer(
    "Form names and revision dates were read from the agencies' and "
    "jurisdictions' own current documents in September 2026. Where no form "
    "number is published, this document says so rather than inventing one."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- state docs
flow += k.h2_tight("THE DOCUMENTS FIXED BY STATE LAW", reserve=2.4)
C = k.cellp
rows = [
    [C("<b>The exemption statement</b><br/>Every permit application"),
     C(f"Signed, on the application: the basis of your exemption "
       f"(§&#160;32-1121(A)(5)) and \"the name and license number of any "
       f"general, mechanical, electrical or plumbing contractor who will be "
       f"employed on the work\" ({ars('32-1169(A)')}). The counter \"may "
       f"require\" the Registrar's signature verifying the exemption. A false "
       f"statement is unsworn falsification ((B)). Local names: Tucson and "
       f"Peoria \"Owner/Builder Affidavit\"; Scottsdale \"Owner-Builder "
       f"Declaration\"; Lake Havasu City \"Owner/Builder Certification\" "
       f"(notarized); Buckeye and Santa Cruz County \"Owner Builder Form\"; "
       f"Glendale \"verification\"; Casa Grande an affirmation; Sierra Vista "
       f"an \"Owner App\" per trade; La Paz \"Owner's Acknowledgment &amp; "
       f"Verification of Information\"; Gila \"Owner Builder Statement\"; "
       f"Mohave a checkbox on the application"),
     C("At application; before it, the licensed-sub list")],
    [C("<b>The recorded deed</b><br/>County recorder"),
     C(f"A deed or contract for conveyance \"recorded with the county "
       f"recorder\" in a natural person's name \"Prior to commencement of "
       f"the construction\" ({ars('33-1002(A)(2)(a)')}). The document that "
       f"switches off the one-year presumption and the subcontractor lien. "
       f"Keep the instrument number on the AZ.0 cover"),
     C("Before the first shovel")],
    [C("<b>Preliminary twenty-day notice</b><br/>From each supplier and "
       "non-wage sub"),
     C(f"\"Except for a person performing actual labor for wages, every "
       f"person who furnishes labor, professional services, materials … "
       f"shall, as a necessary prerequisite to the validity of any claim of "
       f"lien, serve the owner … with a written preliminary twenty day "
       f"notice\" ({ars('33-992.01(B)')}). File every one; it is your lien "
       f"ledger. Under the owner-occupant shield only a party with a direct "
       f"written contract with you can lien at all"),
     C("Within 20 days of first furnishing")],
    [C(f"<b>The contract</b><br/>{ars('32-1158')}"),
     C("Every contract over $1,000 with a contractor carries the "
       "§&#160;32-1158(A) list (AZ.1): parties, license number, jobsite, "
       "dates, the work, total price with taxes, deposit, progress "
       "payments and their stages, and the Registrar complaint notice in "
       "ten-point bold. You are owed \"a legible copy of all documents "
       "signed and a written and signed receipt for … any cash paid\" ((B))"),
     C("Before work; copies kept")],
    [C("<b>Registrar license search · complaint · recovery-fund claim</b>"
       "<br/>roc.az.gov"),
     C(f"Verify the license on the contract date, first-payment date and "
       f"start date ({ars('32-1132(C)')}). A written complaint on a new home "
       f"\"within two years after the earlier of the close of escrow or "
       f"actual occupancy\" ({sec('32-1162(A)(1)')}). The fund pays an "
       f"occupying owner for damage by a <i>licensed</i> residential "
       f"contractor ({sec('32-1132(B)(1)')})"),
     C("Before hiring; within two years of moving in")],
    [C("<b>Notice of Intent to Discharge</b><br/>ADEQ form DWS 402, rev. "
       "April 2025 — filed with the delegated county"),
     C("The septic application, with the site investigation and design. "
       "Leads to the <b>Construction Authorization</b> (no construction "
       "before it; two years to finish), then on your <b>Request for "
       "Discharge Authorization</b> — final site plan, tank watertightness "
       f"certification, and for an alternative system the installer's ROC "
       f"number and the designer's Certificate of Completion — to the "
       f"<b>Discharge Authorization</b> ({aac('R18-9-A301(D)')}; A309(C))"),
     C("Before the footprint is final")],
    [C("<b>Property-line setback waiver</b><br/>Recorded — La Paz County "
       "posts a form"),
     C("Reduces the 50-ft septic-to-line setback on a well-served lot to as "
       "little as 5&#160;ft where the neighbor agrees \"as evidenced by an "
       "appropriately recorded document\" to keep any new well 100&#160;ft "
       f"from your works ({aac('R18-9-A312(C)')}, row 2). La Paz's form: both "
       f"owners sign, notarized, recorded within 30 days \"or the waiver is "
       f"null and void\""),
     C("With the Notice of Intent, if needed")],
    [C("<b>Transfer of ownership inspection · Notice of Transfer</b><br/>"
       "ADEQ-qualified inspector; buyer files"),
     C(f"Within six months before a sale the seller retains a qualified "
       f"inspector; the Report of Inspection must show the tank was pumped "
       f"unless the system went into service within the prior 12 months; "
       f"the buyer files a Notice of Transfer with the county \"within 15 "
       f"calendar days after the property transfer\" "
       f"({aac('R18-9-A316')})"),
     C("At sale")],
    [C("<b>Notice of Intention to Drill</b><br/>ADWR"),
     C(f"Signed by the owner or lessee ({aac('R12-15-809')}); fee $150, or "
       f"$100 for a domestic well at 35&#160;gpm or less outside an AMA or "
       f"INA ({ars('45-596(L)')}); on five acres or less, with the well "
       f"site plan carrying \"written approval by the county health "
       f"authority\" ((F)). Returns the <b>drilling card</b> within 15 days "
       f"((D)); the well must be completed within a year ((E))"),
     C("Before the rig; site plan first")],
    [C("<b>Single well license</b><br/>ADWR — application and examination"),
     C(f"For an owner drilling an exempt well on their own land: \"No fee "
       f"may be charged\" ({ars('45-595(D)')}). The application lists the "
       f"rig, the design, the helpers and whether they are paid; the exam "
       f"is offered at least six times a year; passing grade 70 percent; "
       f"valid one year for one well at one location "
       f"({aac('R12-15-807')})"),
     C("Before drilling it yourself")],
    [C("<b>Well completion reports</b><br/>ADWR"),
     C(f"The driller's within 30 days of completion; <b>yours</b> within "
       f"30 days after the pump is installed — equipment, the 4-hour "
       f"tested capacity, drawdown, static level ({ars('45-600')})"),
     C("30 days after each event")],
    [C("<b>Independent-contractor agreement · sole-proprietor waiver</b>"
       "<br/>Workers' compensation"),
     C(f"A written agreement with the eight statutory statements, "
       f"disclosing that the contractor is not entitled to workers' "
       f"compensation from you, \"creates a rebuttable presumption of an "
       f"independent contractor relationship\" ({ars('23-902(D)')}); a sole "
       f"proprietor may sign the statutory waiver ({sec('23-961(N)')}). Have "
       f"both from anyone not on a licensed contractor's payroll"),
     C("Before the first paid day")],
    [C("<b>The recorded opt-out notice</b><br/>Cochise; Coconino"),
     C("Cochise: \"a notice that a permit has been issued pursuant to the "
       "provisions of this article shall be recorded with the County "
       "Recorder\" (OBA Sec. 6). Coconino AMMP: a recorded \"Notice of "
       "Disclosure Statement.\" Both follow the title"),
     C("At permit issuance")],
    [C("<b>Pool safety notice</b><br/>DHS-approved"),
     C(f"Anyone entering \"an agreement to build a swimming pool\" must give "
       f"the buyer the notice ({ars('36-1681(E)')}); the barrier rules are "
       f"in AZ.2"),
     C("With any pool contract")],
]
flow.append(k.ref_table(
    "Named as the statute, rule or agency names it",
    [C("Document", bold=True), C("What it is", bold=True),
     C("When", bold=True)],
    rows, [1.7 * inch, CW - 1.7 * inch - 1.25 * inch, 1.25 * inch]))

# ---------------------------------------------------------------- local docs
flow += k.h2_tight("THE LOCAL DOCUMENTS — WHAT YOURS CALLS THEM", reserve=1.8)
flow.append(k.body(
    "Each city and county issues its own paperwork under its own names, and "
    "there is no statewide vocabulary for it. Write in what yours calls "
    "them, and the date you received the §&#160;9-836 / §&#160;11-1606 "
    "handout."))
flow += k.check_table(
    "What my jurisdiction calls each document",
    [
        ("<b>Building permit application</b>, and the § 32-1169 statement — "
         "separate form, or a block on the application?",
         [("Called", 0.6), ("Separate?", 0.4)]),
        ("<b>The handout</b> — steps, time frames, contact, website, "
         "clarification notice (§ 9-836(A); § 11-1606):",
         [("Received", 0.4), ("Time frames stated", 0.6)]),
        ("<b>Zoning use permit</b> and the § 11-815(B) sketch:",
         [("Called", 0.6), ("Issued by", 0.4)]),
        ("<b>Floodplain development permit</b>, if in a mapped hazard area:",
         [("Called", 0.6), ("Administrator", 0.4)]),
        ("<b>Driveway approach / encroachment permit</b>, and the <b>911 "
         "address application</b>:",
         [("Called", 0.5), ("Road authority", 0.5), ("911 form", 0.5),
          ("Issued by", 0.5)]),
        ("<b>Certificate of occupancy</b> — ask whether one is issued on my "
         "permit, because under Greenlee, Cochise Option 2 and the "
         "Coconino AMMP there is none:", [("Answer", 1.0)]),
    ])

# ---------------------------------------------------------------- no permit
# 1.2in: prose follows this heading, not a table, so heading plus the first
# paragraph is all the reserve has to guarantee.
flow += k.h2_tight("WHAT NEEDS NO PERMIT — AND WHAT ARIZONA DOES NOT REQUIRE",
                   reserve=1.2)
flow.append(k.body(
    f"<b>Two statutory floors, neither of which reaches a house.</b> The "
    f"county building permit is for construction \"exceeding a cost of "
    f"$1,000\" ({ars('11-321(A)')}); the zoning permit is not required "
    f"\"for repairs or improvements of a value not exceeding five hundred "
    f"dollars\" ({sec('11-815(B)')}). The county code article does not apply "
    f"to construction \"incidental to\" farming, ranching and the like "
    f"({sec('11-865(A)(1)')}) — a barn, not a dwelling. Everything else is "
    f"the locally adopted IRC R105.2 list as amended; ask for it."))
flow.append(k.body(
    "<b>And what Arizona does not require</b>, which owner-builders "
    "arriving from other states routinely budget for:"))
flow.append(k.bullet(
    f"<b>A state trade license for you.</b> Arizona licenses contractors "
    f"only; \"Only contractors as defined in this section are licensed and "
    f"regulated by this chapter\" ({ars('32-1101(B)')}), and an owner under "
    f"§&#160;32-1121(A)(5) is expressly not a residential contractor "
    f"({sec('32-1101(A)(10)(b)')}). Title 32 has no electrician's or "
    f"plumber's chapter."))
flow.append(k.bullet(
    f"<b>Residential fire sprinklers.</b> No city or county may require them "
    f"in a one- or two-family house, or reach them through an access-road "
    f"rule ({ars('9-807')}; {sec('9-808')}; {sec('11-861(E)')}, (G))."))
flow.append(k.bullet(
    f"<b>A statewide energy code, insulation table or climate-zone map.</b> "
    f"The state standard reaches public capital projects only "
    f"({ars('34-451')}); Maricopa County's chapter is voluntary and five "
    f"counties have none."))
flow.append(k.bullet(
    f"<b>A business or transaction-privilege-tax license as a condition of "
    f"your permit</b> ({ars('9-467(E)')}; {sec('11-321(E)')}); <b>a permit "
    f"for the prior owner's unpermitted work</b> before yours issues, except "
    f"for health and safety ({sec('9-467(F)')}; {sec('11-321(H)')}); <b>an "
    f"engineer's stamp on a solar permit</b> without a written reason "
    f"({sec('9-468')}; {sec('11-323')})."))
flow.append(k.bullet(
    "<b>A \"once per 24 months,\" \"once per five years\" or \"live in it "
    "two years\" rule.</b> None is in §&#160;32-1121. The five-year limit is "
    "Cochise County's, on its opt-out permit only."))
flow.append(k.bullet(
    "<b>A statewide inspection list, permit life, fee schedule or review "
    "time for a county permit.</b> None exists; the only county clock is "
    "inspections \"at the earliest reasonable time\" (§&#160;11-863(B))."))

# ---------------------------------------------------------------- yourself
flow += k.h2_tight("WHAT YOU MAY DO YOURSELF — AND THE ONE THAT NEEDS AN EXAM",
                   reserve=2.2)
rows = [
    [C("<b>Act as your own builder; wire and plumb your own house</b>"),
     C("Yes, at the state level"),
     C(f"{ars('32-1121(A)(5)')}; {sec('32-1101(A)(10)(b)')}, (B) — the "
       f"local variable is whether the counter issues the trade permit, and "
       f"rentals are the line")],
    [C("<b>Install a conventional septic system</b>"),
     C("Yes"),
     C(f"{aac('R18-9-A309(C)(1)')} asks for no installer license number; "
       f"the county inspects before backfill and you certify the tank "
       f"watertightness test")],
    [C("<b>Install an alternative septic system</b>"),
     C("No"),
     C(f"{aac('R18-9-A309(C)(2)')} requires \"the name of the installation "
       f"contractor and the Registrar of Contractor's license number\" and "
       f"a designer's Certificate of Completion")],
    [C("<b>Do the site investigation or perc test</b>"),
     C("No"),
     C(f"{aac('R18-9-A310(H)')} — a registered engineer, geologist or "
       f"sanitarian, or a holder of a Department-recognized training "
       f"certificate")],
    [C("<b>Drill your own exempt well</b>"),
     C("Yes — after the exam"),
     C(f"{ars('45-595(D)')}: a single well license, no fee; "
       f"{aac('R12-15-807')}: application, examination at 70 percent, one "
       f"well, one year. Otherwise a licensed driller "
       f"({sec('45-595(A)')})")],
    [C("<b>Do the gas connection and fire-safety wiring</b>"),
     C("You, or a licensed contractor — not a helper"),
     C(f"{ars('32-1121(D)')} closes the casual and handyman exemptions to "
       f"fuel-gas and fire-safety work; paragraph (5) is untouched")],
]
flow.append(k.ref_table(
    "Arizona is generous about owner-performed work — here is the map",
    [C("Task", bold=True), C("May you?", bold=True), C("Why", bold=True)],
    rows, [1.9 * inch, 1.45 * inch, CW - 3.35 * inch]))
# ---------------------------------------------------------------- clarification
flow += k.h2_tight("THE THIRTY-DAY CLARIFICATION LETTER — A.R.S. § 9-839 / "
                   "§ 11-1609", reserve=2.4)
flow.append(k.body(
    f"The one form you write. A city or county \"shall respond within thirty "
    f"days of the receipt of the written request with a written explanation "
    f"of its interpretation or application\" ({ars('9-839')}; "
    f"{sec('11-1609')}) — and both statutes list what the request must "
    f"contain. Every \"it depends on your jurisdiction\" in this kit — the "
    f"code edition and grace period, the inspection list, the Registrar's "
    f"signature, the county's actual review time — becomes a dated written "
    f"answer. Draft it here, then send it."))
rows = [
    [C("<b>1. Your name and address</b>"), ""],
    [C("<b>2. The statute, ordinance or code provision</b> you need "
       "clarified — by section number"), ""],
    [C("<b>3. The relevant facts</b> — parcel, zoning, what you propose to "
       "build and how"), ""],
    [C("<b>4. Your proposed interpretation</b> — say what you believe the "
       "provision means for your parcel"), ""],
    [C("<b>5. Whether the issue is pending</b> on an existing application, "
       "and which"), ""],
    [C("<b>Sent · to · received · answered</b>"), ""],
]
# A form split across two sheets is not a form. KeepTogether moves it whole.
from reportlab.platypus import KeepTogether
flow.append(KeepTogether(d.titled_table(
    "Request for clarification — the five statutory elements",
    [C("Element", bold=True), C("Write here", bold=True)],
    rows, [2.35 * inch, CW - 2.35 * inch], S, write_rows=True,
    row_heights=[36, 44, 80, 80, 44, 36])))
flow.append(Spacer(1, 8))

flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "az-permit-kit",
                       "AZ.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
