#!/usr/bin/env python3
"""FL.5 Forms & Documents Index.

Every document a Florida owner-builder will meet, named the way the issuing
agency names it, with the office it comes from and the moment it is due.

The second half is the construction lien paperwork, which belongs in a permit
kit for a reason specific to Florida: an owner-builder is their own contractor,
so the statutory documents that normally flow FROM a general contractor TO an
owner have no one to flow from. The final payment affidavit, the two statutory
lien waivers, and the notice of contest of lien are the owner-builder's own
job, and the notice of contest (s. 713.22(2), Fla. Stat.) — which cuts a
lienor's window to sue from a year to sixty days — is the most useful
underused tool in the chapter.

The closing section prints what the kit deliberately does NOT tell you and
why. That page exists because the alternative — quietly omitting the things we
could not verify — would leave a reader assuming the silence meant the
requirement did not exist.
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

FORM_ID = "FL.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "The Paperwork"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "Every document you will meet, what it is called, who "
                 "issues it, and when it is due.")
flow.append(k.disclaimer())

# ------------------------------------------------------------- the permit set
flow += k.h2_tight("THE PERMIT DOCUMENTS", reserve=2.2)
rows = [
    [k.cellp("<b>Building permit application</b>"),
     k.cellp("Your building department"),
     k.cellp("You sign it <b>in person</b> at the counter — the exemption "
             "requires it")],
    [k.cellp("<b>Owner-Builder Disclosure Statement</b>"),
     k.cellp("Given to you by the local permitting agency; text is printed "
             "in the statute"),
     k.cellp("Signed before the permit issues. Twelve numbered "
             "paragraphs — see FL.1")],
    [k.cellp("<b>Electrical owner disclosure statement</b>"),
     k.cellp("Same, under the separate Part II exemption"),
     k.cellp("Only if you will do your own wiring. Different terms from "
             "the one above")],
    [k.cellp("<b>Identity verification</b>"),
     k.cellp("Your building department"),
     k.cellp("At permit issuance: driver license copy, notarized "
             "signature, or another method the agency accepts")],
    [k.cellp("<b>Product approval schedule</b>"),
     k.cellp("Format set by your building department; FL numbers come from "
             "the state product search"),
     k.cellp("With the plans. One approval number per exterior opening and "
             "covered product")],
    [k.cellp("<b>Form R400-2023</b>"),
     k.cellp("Florida Building Commission"),
     k.cellp("Residential Energy Conservation Code Documentation "
             "Checklist — with the application")],
    [k.cellp("<b>Form R402-2023</b>, or a performance report"),
     k.cellp("Commission form, or Commission-approved energy software"),
     k.cellp("Prescriptive path uses the form; performance path uses the "
             "software's report. Not REScheck")],
    [k.cellp("<b>Truss engineering and placement plan</b>"),
     k.cellp("Your truss manufacturer's engineer"),
     k.cellp("With the plans. The engineering is sealed; ask your reviewer "
             "what they expect for the placement plan")],
    [k.cellp("<b>Private provider notice</b>"),
     k.cellp("Commission-adopted form, filed with the building official"),
     k.cellp("Only if you hire your own plan review and inspections — at "
             "application, or 2&nbsp;business days before the first inspection")],
]
flow.append(k.ref_table(
    "Getting the permit",
    [k.cellp("Document", bold=True), k.cellp("Who issues it", bold=True),
     k.cellp("When", bold=True)],
    rows, [2.05 * inch, 1.95 * inch, CW - 4.00 * inch]))

# ------------------------------------------------------------- other agencies
flow += k.h2_tight("THE DOCUMENTS FROM EVERYONE ELSE", reserve=2.2)
rows = [
    [k.cellp("<b>Form DEP 4015</b>"),
     k.cellp("Dept. of Environmental Protection, or your county health "
             "department"),
     k.cellp("Septic construction permit application, with a scaled site "
             "plan and floor plan. <b>Before your building permit</b>")],
    [k.cellp("<b>Form DEP 4016</b>"),
     k.cellp("Same"),
     k.cellp("The septic construction permit and inspection document "
             "itself. Valid 18&nbsp;months")],
    [k.cellp("<b>Site evaluation and soil profiles</b>"),
     k.cellp("A licensed engineer with soils training, department "
             "personnel, a Master Septic Tank Contractor, a certified soil "
             "scientist, or a person certified under s. 381.0101"),
     k.cellp("With the septic application. <b>You may not perform this "
             "yourself</b> for a new system. Valid 180&nbsp;days before "
             "application")],
    [k.cellp("<b>Final installation approval</b>"),
     k.cellp("Same agency as your septic permit"),
     k.cellp("<b>Before occupancy</b> — a statutory precondition, separate "
             "from your certificate of occupancy")],
    [k.cellp("<b>Well construction permit</b>"),
     k.cellp("Your water management district"),
     k.cellp("Before drilling. Applied for by you or by the well "
             "contractor on your behalf")],
    [k.cellp("<b>Elevation Certificate</b>"),
     k.cellp("A surveyor or engineer, on the FEMA form"),
     k.cellp("In a flood hazard area: at placement of the lowest floor "
             "before further vertical construction, and again at final")],
    [k.cellp("<b>CCCL permit</b>"),
     k.cellp("Dept. of Environmental Protection"),
     k.cellp("Before construction seaward of the coastal construction "
             "control line. A separate state permit")],
    [k.cellp("<b>Termite Certificate of Compliance</b>"),
     k.cellp("A licensed pest control company"),
     k.cellp("Issued to the building department after treatment. Soil "
             "treatment goes in after backfill and compaction")],
    [k.cellp("<b>Blower door test report</b>"),
     k.cellp("An energy auditor or rater, a Class A or B air-conditioning "
             "or mechanical contractor, or an approved third party"),
     k.cellp("Before the certificate of occupancy. Maximum 7&nbsp;ACH50. Not "
             "self-certified")],
    [k.cellp("<b>Driveway or access permit</b>"),
     k.cellp("Your county, or the Dept. of Transportation for a state road"),
     k.cellp("Before you build the connection")],
]
flow.append(k.ref_table(
    "Approvals that are not building permits",
    [k.cellp("Document", bold=True), k.cellp("Who issues it", bold=True),
     k.cellp("When", bold=True)],
    rows, [2.05 * inch, 2.10 * inch, CW - 4.15 * inch]))

# ------------------------------------------------------------------- liens
flow += k.h2("THE LIEN PAPERWORK — WHICH IS YOURS NOW")
flow.append(k.body(
    "Florida's construction lien law assumes a general contractor stands "
    "between the owner and the subs. As an owner-builder you removed that "
    "person, so the documents that normally protect an owner have nobody to "
    "come from. These are now your job, and the deadlines are short."))
rows = [
    [k.cellp("<b>Notice of Commencement</b>"),
     k.cellp("Recorded by you at the clerk of the circuit court before work "
             "begins; posted at the site; a copy filed with the building "
             "department before the first inspection. The statute prints "
             "the form."),
     k.cellp("s. 713.13")],
    [k.cellp("<b>Notice to Owner</b>"),
     k.cellp("Comes <i>to</i> you, from subs and suppliers you did not "
             "contract with directly. They must serve it before commencing "
             "or <b>within 45&nbsp;days</b> of first furnishing. Keep every one — "
             "the list of who served you is the list of who can lien you."),
     k.cellp("s. 713.06(2)(a)")],
    [k.cellp("<b>Waiver and Release of Lien upon Progress Payment</b>"),
     k.cellp("Collect one from each sub and supplier every time you pay. "
             "The statute prescribes the wording, and you may not demand a "
             "different form."),
     k.cellp("s. 713.20(4), (6)")],
    [k.cellp("<b>Waiver and Release of Lien upon Final Payment</b>"),
     k.cellp("The unconditional version, at final payment. Note that a lien "
             "right cannot be waived in advance — a waiver signed before "
             "work starts is unenforceable."),
     k.cellp("s. 713.20(2), (5)")],
    [k.cellp("<b>Contractor's Final Payment Affidavit</b>"),
     k.cellp("Sworn, on the statutory form, stating every lienor who served "
             "a notice has been paid. <b>Retain final payment until you "
             "have it.</b> Pay without it and the property is exposed to "
             "the full amount of valid liens you had notice of."),
     k.cellp("s. 713.06(3)(d)")],
    [k.cellp("<b>Notice of Contest of Lien</b>"),
     k.cellp("Your counterpunch. Recording it cuts a lienor's time to sue "
             "from one year to <b>60&nbsp;days from service</b>; a lienor who "
             "does not sue in that window has their lien "
             "“extinguished automatically.”"),
     k.cellp("s. 713.22(2)")],
    [k.cellp("<b>Notice of Termination</b>"),
     k.cellp("Ends the Notice of Commencement's effective period once all "
             "lienors are paid. Must be accompanied by the contractor's "
             "affidavit, served before recording, and takes effect no "
             "earlier than 30&nbsp;days after recording."),
     k.cellp("s. 713.132")],
]
flow.append(k.ref_table(
    "The documents that decide whether you pay twice",
    [k.cellp("Document", bold=True), k.cellp("What it does", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [2.10 * inch, CW - 3.35 * inch, 1.25 * inch]))

flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "Three deadlines worth writing on the wall", [
        Paragraph("<b>45&nbsp;days</b> — a sub or supplier not in direct contract "
                  "with you must serve a Notice to Owner within 45&nbsp;days of "
                  "first furnishing. Failure to serve it, or to serve it in "
                  "time, “is a complete defense to enforcement of a "
                  "lien.”", S["body"]),
        Paragraph("<b>90&nbsp;days</b> — a claim of lien must be recorded "
                  "“not later than 90&nbsp;days after the final furnishing "
                  "of the labor or services or materials by the "
                  "lienor.” After that the window closes.", S["body"]),
        Paragraph("<b>1&nbsp;year, or 60&nbsp;days if you act</b> — a recorded lien "
                  "does not continue longer than one year unless the lienor "
                  "sues. Record a Notice of Contest of Lien and that becomes "
                  "60&nbsp;days from service. Most owner-builders never learn this "
                  "exists.", S["body"]),
    ]))
flow.append(k.cite(
    "Sections 713.06(2)(a), 713.08(5) and 713.22(1)–(2), Fla. Stat. (2026). "
    "Lien law is where an owner-builder's money is genuinely at risk; if a "
    "lien is recorded against your property, this kit's job is to tell you "
    "the clock exists, not to replace a construction attorney."))

# ------------------------------------------------------------ what we omit
flow += k.h2("WHAT THIS KIT DELIBERATELY DOES NOT TELL YOU")
flow.append(k.body(
    "Everything in this kit was read against a primary source. A few things "
    "an owner-builder reasonably wants were checked and then <b>left out</b> "
    "because they could not be verified to that standard. Silence would imply "
    "they do not matter, so here they are, with what to ask instead."))
flow.append(k.bullet(
    "<b>County permit fees, plan review fees and impact fees.</b> Set "
    "locally, revised often, and frequently misquoted. Ask for the published "
    "impact fee schedule — every local government is required to publish "
    "one — and get the building permit fee in writing with your application."))
flow.append(k.bullet(
    "<b>A county-by-county wind speed table.</b> The code itself now points "
    "to a location-specific lookup rather than a table, so a table would only "
    "invite you to design to the wrong number. Use ascehazardtool.org and "
    "confirm with your building department."))
flow.append(k.bullet(
    "<b>The exact wording of the windborne debris region definition.</b> The "
    "8th Edition amended it, and the current wording could not be obtained "
    "from a primary source. Ask your building department to confirm in "
    "writing whether your parcel is in the region — and do not assume an "
    "inland lot is exempt."))
flow.append(k.bullet(
    "<b>A freeboard figure, or which ASCE 24 edition applies.</b> Freeboard "
    "above base flood elevation is set by local ordinance and varies. Ask "
    "your floodplain administrator for the number and for which elevation "
    "certificates they require, at which stages."))
flow.append(k.bullet(
    "<b>A duct leakage figure.</b> The air leakage limit is verified at "
    "7&nbsp;ACH50; the duct test threshold was not, so it is not printed. Ask "
    "your rater what they will test to."))
flow.append(k.bullet(
    "<b>A minimum lot frontage for a private-well lot.</b> The half-acre "
    "minimum area is verified; a companion dimension figure was not. Ask "
    "your septic permitting office."))
flow.append(k.bullet(
    "<b>Whether you personally must carry workers' compensation.</b> Two "
    "Florida statutes point different directions here and this kit will not "
    "pick one for you — see FL.1. Ask a Florida insurance agent or attorney "
    "before anyone works on your lot."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "One habit worth more than this whole kit", [
        Paragraph("Whenever an office tells you something that matters — your "
                  "flood zone, your wind speed, whether your parcel is in the "
                  "windborne debris region, which septic office has your "
                  "county, what verification they want at issuance — "
                  "<b>ask them to put it in an email</b>, and file it. "
                  "Staff turn over, portals change, and the person who told "
                  "you in March may not be there in September. A dated "
                  "written answer is the difference between a conversation "
                  "and a record.", S["body"]),
    ]))

# ----------------------------------------------------------------- sources
flow += k.h2_tight("SOURCES", reserve=2.0)
flow.append(k.sources_table([
    ("The owner-builder disclosure statement and the personal appearance "
     "requirement", "s. 489.103(7)(c)"),
    ("The separate electrical owner disclosure statement", "s. 489.503(6)(c)"),
    ("Private provider notice to the building official", "s. 553.791(4)"),
    ("Septic construction permit application and permit forms, and the "
     "18-month term", "Rules 62-6.003(1), 62-6.004(1), F.A.C."),
    ("Who may perform the site evaluation for a new system, and its 180-day "
     "validity", "Rule 62-6.004(3), F.A.C."),
    ("Septic construction permit before the building permit; final "
     "installation approval before occupancy", "s. 381.0065(4)"),
    ("Well construction permit required before construction",
     "Rule 62-532.400(1), F.A.C."),
    ("Termite treatment and the Certificate of Compliance to the building "
     "department", "FBC Residential R318.1"),
    ("Building air leakage testing, the 7&nbsp;ACH50 limit and who may perform it",
     "FBC Energy Conservation R402.4.1.2"),
    ("Elevation certification at the lowest floor and at final inspection",
     "FBC Building 110.3"),
    ("Notice of Commencement: form, recording, posting and filing",
     "ss. 713.13, 713.135"),
    ("Notice to Owner within 45&nbsp;days, and that failure to serve is a "
     "complete defense to the lien", "s. 713.06(2)(a)"),
    ("The two statutory lien waiver forms, the bar on advance waiver, and "
     "the bar on demanding a different form", "s. 713.20(2), (4), (5), (6)"),
    ("The Contractor's Final Payment Affidavit and the duty to retain final "
     "payment until it is furnished", "s. 713.06(3)(d)"),
    ("A claim of lien must be recorded within 90&nbsp;days of final furnishing",
     "s. 713.08(5)"),
    ("A lien lasts 1&nbsp;year unless suit is brought; a Notice of Contest of "
     "Lien reduces that to 60&nbsp;days from service", "s. 713.22(1), (2)"),
    ("Notice of Termination mechanics", "s. 713.132"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "fl-permit-kit",
                       "FL.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
