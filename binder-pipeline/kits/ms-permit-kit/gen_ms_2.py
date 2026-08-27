#!/usr/bin/env python3
"""MS.2 Permit Application Checklist.

The organizing insight: in Mississippi the building permit is the OPTIONAL
part. The approval that binds every parcel in the state — code or no code — is
the health department's onsite wastewater approval, and it is welded to your
water service by statute.

Verified sources (all read in the enacted bill text, August 2026):
  § 41-67-5(1)   no owner shall CONSTRUCT OR PLACE any residence which may
                 require an onsite system "without having first submitted a
                 notice of intent to the department" — statewide, and wholly
                 independent of any building code
  § 41-67-5(2)   "No public utility supplying water shall make connection ...
                 without the prior written approval of the department" — the
                 enforcement mechanism. Construction-period connection is
                 allowed only if a plan is approved AND the owner agrees to
                 inspection and approval before use or occupancy
  § 41-67-6(7)   the TWO-ACRE exemption from department approval and from
                 § 41-67-5(2), on three conditions including the installer's
                 signed affidavit
  § 41-67-7(1)   approval required except per § 41-67-6(7); department must
                 answer within 5 working days; DEEMED APPROVED if it does not
                 respond within 10 calendar days
  § 41-67-7(5)   advanced treatment systems require a continuing maintenance
                 agreement with a certified installer in perpetuity unless the
                 owner is a qualified homeowner maintenance provider
  § 41-67-31     the chapter stands repealed July 1, 2028 (2023 HB 522) —
                 Mississippi reenacts this law on a cycle, so a reader in 2028
                 should re-check rather than assume
  § 73-59-17     the building official must be furnished evidence of license
                 or exemption
  MSDH Form 908  "Statement of Intent - Individual On-site Wastewater Disposal
                 System (IOWDS): New" — the five-step process

Deliberately NOT printed: the dollar fees on Form 908. The form's revision
stamp is 2017 and a nine-year-old fee printed as current in a paid product is
exactly the kind of error this kit exists to avoid. The structure is printed
and the amount is a write-in. Also not printed: the MSDH list of water
associations and cities requiring Final Approval — it is dated April 2021 and
carries the Department's own caveat that it "may or may not be complete," so
the kit prints the CATEGORIES to ask about instead of a stale roster.
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

FORM_ID = "MS.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Applications & Approvals"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What to gather before you file — starting with the one approval that "
    "binds every parcel in Mississippi whether or not a building code does.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- the order
flow += k.h2_tight("DO THESE IN THIS ORDER")
flow.append(k.body(
    "Most permit checklists start with the building permit. In Mississippi "
    "that is the wrong end. Your building permit may not exist; your "
    "<b>wastewater approval</b> almost certainly does, it can dictate where "
    "on the lot the house may sit, and until it is in hand a public water "
    "utility is <b>forbidden by statute</b> from connecting you."))

ord_rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp("<b>Notice of intent for the septic system</b>"),
     k.cellp("Required before you construct or place the residence. Statewide. "
             "Drives the soil evaluation, which can move the house on the lot")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("<b>Establish your code status</b>"),
     k.cellp("MS.4. Whether a building permit exists at all, and who issues "
             "it")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("<b>Flood determination</b>"),
     k.cellp("Before you design. If you are in a mapped flood hazard area it "
             "changes the foundation, and the ordinance applies even where "
             "the building code does not")],
    [k.cellp("<b>4</b>", center=True),
     k.cellp("<b>Driveway and address</b>"),
     k.cellp("Road access permission and an E-911 address. Utilities and "
             "lenders both ask for the address")],
    [k.cellp("<b>5</b>", center=True),
     k.cellp("<b>Building permit, if one exists</b>"),
     k.cellp("With evidence of your licensing exemption — the building "
             "official is required to ask for it")],
    [k.cellp("<b>6</b>", center=True),
     k.cellp("<b>Utility applications</b>"),
     k.cellp("Temporary construction power, permanent service, water "
             "membership and meter")],
]
flow.append(k.ref_table(
    "The sequence that avoids rework",
    [k.cellp("", bold=True), k.cellp("Step", bold=True),
     k.cellp("Why it comes here", bold=True)],
    ord_rows, [0.4 * inch, 2.15 * inch, CW - 2.55 * inch]))

# ---------------------------------------------------------------- septic
flow += k.h2_tight("THE WASTEWATER APPROVAL — THE ONE THAT ALWAYS APPLIES")
flow.append(k.body(
    "This is the most important page in the kit for anyone building outside a "
    "sewer district. Mississippi's Individual On-site Wastewater Disposal "
    "System Law sits in the <b>public health</b> title, not the building-code "
    "title, so a county's building-code status has no effect on it whatever. "
    "It applies in an opted-out county exactly as it applies in Gulfport."))

flow.append(k.callout_long(
    "The two sentences that govern your build", [
        Paragraph("<b>You must file before you build.</b> \"<i>No owner, "
                  "lessee or developer shall construct or place any mobile, "
                  "modular or permanently constructed residence, building or "
                  "facility, which may require the installation of an "
                  "individual on-site wastewater disposal system, <b>without "
                  "having first submitted a notice of intent to the "
                  "department</b>.</i>\" Note what triggers it: constructing "
                  "or placing the <b>residence</b> — not installing the "
                  "septic system. The obligation lands at the start of your "
                  "project, not the end. (§ 41-67-5(1))", S["body"]),
        Paragraph("<b>And your water is locked to it.</b> \"<i>No public "
                  "utility supplying water shall make connection to any "
                  "dwelling, house, mobile home or residence <b>without the "
                  "prior written approval of the department</b> certifying "
                  "that the plan for the sewage treatment and disposal system "
                  "at the location of the property complies with this "
                  "chapter.</i>\" This is why the health department's "
                  "paperwork is what your water association asks to see "
                  "before it will set a meter. (§ 41-67-5(2))", S["body"]),
        Paragraph("There is a construction-period allowance, and it comes "
                  "with a condition worth reading twice: connections "
                  "\"<i>may be made during construction if the department has "
                  "approved a plan … <b>and the owner of the property has "
                  "agreed to have the system inspected and approved by the "
                  "department before the use or occupancy of the "
                  "property</b></i>.\" You can get construction water on an "
                  "approved plan — but you have promised the inspection, and "
                  "occupancy is the deadline.", S["body"]),
    ]))
flow.append(k.cite(
    "Miss. Code Ann. § 41-67-5(1), (2), quoted verbatim from the Mississippi "
    "Individual On-site Wastewater Disposal System Law as reenacted by House "
    "Bill 522, 2023 Regular Session, read at billstatus.ls.state.ms.us and "
    "published by MSDH at msdh.ms.gov → Regulation → On-Site Wastewater → "
    "Laws and regulations. Verified August 2026."))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>The process, as the Department runs it.</b> The application is the "
    "Department's <i>Statement of Intent — Individual On-site Wastewater "
    "Disposal System (IOWDS): New</i>, Form 908, filed with the legal "
    "description of the property, a plot plan showing the buildings and "
    "improvements, and the fee. Apply online through the Department's "
    "wastewater application page at <b>msdh.ms.gov</b>, or by mail to the "
    "Division of On-site Wastewater in Jackson."))

step_rows = [
    [k.cellp("<b>1. Application</b>"),
     k.cellp("Form 908 with the legal description, plot plan and fee")],
    [k.cellp("<b>2. Site soil evaluation</b>"),
     k.cellp("Carried out by the local environmentalist — the step often "
             "called a percolation test. This determines which systems your "
             "soil will accept, and can move the house on the lot")],
    [k.cellp("<b>3. Permit / recommendation</b>"),
     k.cellp("Issued to you after the evaluation, listing the system options "
             "recommended for your property. <b>This is the document you "
             "present to your water supplier to get a meter</b>")],
    [k.cellp("<b>4. Installation and inspection</b>"),
     k.cellp("A <b>certified installer</b> installs one of the recommended "
             "systems, and is responsible for contacting the Department "
             "<b>24 hours before starting work</b> to schedule the "
             "inspection")],
    [k.cellp("<b>5. Final approval</b>"),
     k.cellp("Issued once the Department has the installer's signed "
             "installation affidavit — plus, for an advanced treatment "
             "system, your signed maintenance affidavit")],
]
flow.append(k.ref_table(
    "The five steps, and what you receive at each",
    [k.cellp("Step", bold=True), k.cellp("What happens", bold=True)],
    step_rows, [1.55 * inch, CW - 1.55 * inch]))
flow.append(k.cite(
    "Mississippi State Department of Health, <i>Statement of Intent — "
    "Individual On-site Wastewater Disposal System (IOWDS): New</i>, Form "
    "908. Fees are set by the Department and are deliberately not reproduced "
    "here — ask for the current schedule when you apply and write it into the "
    "checklist below."))

# ---------------------------------------------------------------- two acres
flow.append(Spacer(1, 6))
flow.append(k.callout_long(
    "The two-acre exemption — real, statutory, and narrower than it sounds", [
        Paragraph("Mississippi exempts larger lots from the Department's "
                  "final approval, and from the water-connection bar with it: "
                  "\"<i>Any lot or tract that is <b>two (2) acres or "
                  "larger</b> shall be exempt from the requirements of this "
                  "chapter and regulations of the department relating to "
                  "approval of individual on-site wastewater disposal systems "
                  "by the department, and shall be exempt from the provisions "
                  "of Section 41-67-5(2), provided that: (a) All wastewater "
                  "is contained on the lot or tract; (b) No watercourse … is "
                  "impacted; and (c) <b>The person who installed the … system "
                  "provides the department with a signed affidavit</b> "
                  "attesting that the requirements of paragraphs (a) and (b) "
                  "are met.</i>\"", S["body"]),
        Paragraph("Read the three conditions as a set — the exemption is not "
                  "automatic just because the tract is big. All three must "
                  "hold, and the third puts a signature requirement on "
                  "whoever installed the system.", S["body"]),
        Paragraph("<b>And it only helps if nobody else wants the final "
                  "approval.</b> The Department's own application asks you to "
                  "confirm that final approval is not required by your board "
                  "of supervisors under a county ordinance, your water "
                  "association or supplier, your <b>lender</b>, a public "
                  "utility authority, or a subdivision agreement. Several "
                  "Mississippi counties do require it by ordinance, a number "
                  "of rural water associations require it, and FHA-backed "
                  "financing requires it. Ask all of them before you rely on "
                  "the exemption — and note that the Department publishes its "
                  "list of such entities with the warning that it \"may or "
                  "may not be complete.\"", S["body"]),
    ]))
flow.append(k.cite(
    "Miss. Code Ann. § 41-67-6(7), quoted verbatim. The categories of entity "
    "that may still require final approval are those listed on MSDH Form 908 "
    "and on the Department's map of county on-site wastewater ordinances."))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "Two more provisions worth knowing", [
        Paragraph("<b>A clock runs on the Department.</b> Once you have met "
                  "the requirements, \"<i>the department must approve or "
                  "disapprove the request within five (5) working days</i>,\" "
                  "must give written reasons for a disapproval, and — the "
                  "part to remember — \"<i>if the department does not respond "
                  "to the request within ten (10) calendar days, the request "
                  "… <b>shall be deemed approved</b></i>.\" (§ 41-67-7(1))",
                  S["body"]),
        Paragraph("<b>An aerobic or advanced system is a lifetime "
                  "commitment.</b> Where the soil will not take a "
                  "conventional field, the statute requires the property "
                  "owner to \"<i>keep a continuing maintenance agreement with "
                  "a certified installer on all advanced treatment systems "
                  "<b>in perpetuity</b></i>\" — unless the owner qualifies as "
                  "a homeowner maintenance provider through the Department's "
                  "training, which it provides without charge. Budget the "
                  "contract, or take the training. (§ 41-67-7(5))", S["body"]),
    ]))

# ---------------------------------------------------------------- building permit
flow += k.h2_tight("THE BUILDING PERMIT — IF YOUR PARCEL HAS ONE")
flow.append(k.body(
    "Work MS.4 first. If a code is enforced, assemble the items below; if it "
    "is not, skip to the next section, because there is no application to "
    "make. Nothing here is a statewide list — Mississippi has no statewide "
    "permit application — so treat it as the common denominator and add "
    "whatever your office asks for."))

flow += k.check_table("For the building permit application", [
    ("Recorded deed in your name, and the parcel number",
     [("Parcel ID:", 1.0)]),
    "<b>Evidence that you are exempt</b> from residential builder licensing — "
    "§ 73-59-17 requires the building official to refuse the permit without "
    "evidence of license or exemption. Ask what form that evidence takes "
    "before you go",
    "Site plan showing the house, setbacks, driveway, well and septic "
    "location — usually the same plot plan the health department wanted",
    "Floor plans, elevations and a foundation plan. Ask whether your "
    "jurisdiction requires plans sealed by an architect or engineer for a "
    "one- or two-family dwelling; this is set locally and varies",
    "Energy compliance documentation, to whichever edition of the code your "
    "jurisdiction adopted — confirm the edition, because the statute permits "
    "any of the last three",
    ("Septic permit or recommendation from the health department, or written "
     "confirmation of public sewer availability",
     [("Document #:", 1.0)]),
    "Flood determination, and an elevation certificate if you are in a mapped "
    "flood hazard area",
    ("Driveway or road access approval — county road department, or MDOT if "
     "you tie into a numbered state highway", [("Approved:", 1.0)]),
    ("Licensed trade contractors identified, with license numbers, for "
     "electrical, plumbing, mechanical and HVAC",
     [("Verified at msboc.us on:", 1.0)]),
], notes_header="Notes")

# ---------------------------------------------------------------- no permit
flow += k.h2_tight("IF THERE IS NO BUILDING PERMIT — WHAT STILL APPLIES")
flow.append(k.body(
    "An opt-out is an opt-out of <b>the building code</b>. Everything below "
    "sits in a different statute or a different contract, and none of it "
    "cares what your board of supervisors resolved in 2014."))

flow += k.check_table("Approvals that survive a no-code parcel", [
    ("<b>Wastewater notice of intent</b> filed before construction, and the "
     "permit or recommendation received (§ 41-67-5(1))",
     [("Filed:", 0.5), ("Received:", 0.5)]),
    "<b>Water connection</b> — your supplier may not connect without the "
    "Department's prior written approval, unless your tract qualifies under "
    "the two-acre exemption <i>and</i> the supplier does not require final "
    "approval anyway (§ 41-67-5(2); § 41-67-6(7))",
    ("<b>Floodplain development permit</b> if your community takes part in "
     "the National Flood Insurance Program — the state construction-code "
     "exemptions are written expressly not to reach NFIP ordinances",
     [("Flood zone:", 0.5), ("Permit:", 0.5)]),
    ("<b>E-911 address assignment</b> — usually needed before a utility will "
     "set a meter", [("Address issued:", 1.0)]),
    ("<b>Driveway / culvert permission</b> from the county road department, "
     "or MDOT on a state highway", [("Approved:", 1.0)]),
    "<b>Electric utility requirements</b> — ask what release or inspection "
    "your supplier wants before energizing, since in a no-code county there "
    "is no municipal electrical inspector to sign anything",
    "<b>Zoning</b>, if your county or city has it — separate from building "
    "code, and it may exist where the code does not",
    "<b>Licensed trades</b> — the zero-dollar rule in § 73-59-3(1)(d) applies "
    "whether or not anybody inspects the work",
    "<b>Lender and insurer requirements</b> — usually the strictest thing "
    "applying to a no-code build. Ask both before you close",
], notes_header="Notes / reference #")

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("A notice of intent must be submitted to the health department before "
     "constructing or placing a residence that may require an onsite system — "
     "statewide, regardless of building-code status", "§ 41-67-5(1)"),
    ("No public water utility may connect without the department's prior "
     "written approval; construction-period connection requires an approved "
     "plan and the owner's agreement to inspection before use or occupancy",
     "§ 41-67-5(2)"),
    ("Lots of two acres or larger are exempt from department approval and "
     "from § 41-67-5(2) on three conditions, including the installer's signed "
     "affidavit", "§ 41-67-6(7)"),
    ("The department must approve or disapprove within five working days, and "
     "a request is deemed approved if it does not respond within ten calendar "
     "days", "§ 41-67-7(1)"),
    ("Advanced treatment systems require a continuing maintenance agreement "
     "in perpetuity unless the owner is a qualified homeowner maintenance "
     "provider", "§ 41-67-7(5)"),
    ("The wastewater chapter stands repealed July 1, 2028 unless reenacted — "
     "Mississippi extends it on a cycle", "§ 41-67-31 (2023 HB 522)"),
    ("The building official must be furnished evidence of license or "
     "exemption before issuing a permit", "§ 73-59-17"),
    ("Electrical, plumbing, mechanical and HVAC contractors of any tier must "
     "be licensed no matter the dollar amount", "§ 73-59-3(1)(d)"),
    ("NFIP floodplain ordinances are unaffected by the state "
     "construction-code exemptions", "§ 17-2-7(5); § 17-2-9(6)"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ms-permit-kit",
                       "MS.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
