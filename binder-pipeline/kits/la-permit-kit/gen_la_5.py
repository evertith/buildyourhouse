#!/usr/bin/env python3
"""LA.5 Forms & Documents Index.

Every document a Louisiana owner-builder will be asked for, named the way the
agency that issues it names it — because asking for the right document by its
right name is most of what makes a counter visit short.

Form numbers printed here (LHS-47, SF-10ST, SF-11ST, FORM-A, FORM-B,
DNR-GW-1S) were read off the issuing agency's own rule text or its own
published form. Where a document has no number — the LSLBC affidavit is the
important case — that is stated rather than invented.
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

FORM_ID = "LA.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Forms Index"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "Every document you will be asked for, named as the office "
                 "that issues it names it — and the short list of things that "
                 "need no permit at all.")
flow.append(k.disclaimer())

flow += k.h2("THE DOCUMENTS")
flow.append(k.body(
    "Louisiana routes an owner-builder through four different levels of "
    "government — a state licensing board, a state health office, your parish "
    "or town, and in some cases the state highway department and the state "
    "environmental agency. Nothing arrives in one packet. This is the whole "
    "set."))

W = [1.95 * inch, 1.35 * inch, CW - 3.30 * inch]
HDR = [k.cellp("Document", bold=True), k.cellp("From", bold=True),
       k.cellp("What it is, and when", bold=True)]


def table(title, rows):
    return k.ref_table(
        title, HDR,
        [[k.cellp(a), k.cellp(b), k.cellp(c)] for a, b, c in rows], W)


flow.append(table("Licensing and the exemption", [
    ("<b>Affidavit Claiming Exemption from Licensure</b>",
     "State Licensing Board for Contractors",
     "The document that gets an owner-builder a permit. Notarized, eleven "
     "initialed statements. <b>It carries no form number</b> — only a "
     "revision date, which was 1 August 2025 when this kit was verified. "
     "Goes to your local permit official <i>before</i> the permit issues."),
    ("Church Owner/Builder Affidavit",
     "State Licensing Board for Contractors",
     "<b>Not your form.</b> It implements a different exemption and sits on "
     "the same forms page. Confusingly, the words &ldquo;Owner/Builder&rdquo; "
     "appear in its title and not in yours."),
    ("Written subcontractor contracts",
     "You",
     "Not a state form, but a statutory requirement you attest to on the "
     "affidavit: a signed written contract with each licensed sub, with no "
     "work beginning before all parties sign."),
    ("License verification printout",
     "State Licensing Board for Contractors",
     "The board runs a public contractor search. Print the result for each "
     "sub and keep it with the contract — your exemption does not cover "
     "them."),
]))

flow.append(table("The building permit", [
    ("Building permit application",
     "Your parish or municipality",
     "In several parishes this form is physically issued by the <b>911 "
     "office</b>, which completes and signs part of it before you take it "
     "anywhere else. Ask where the form comes from, not just where it goes."),
    ("Construction plans",
     "You or your designer",
     "One to two sets. <b>No architect or engineer seal may be required</b> "
     "if the house is within the IRC's prescriptive standards. At least one "
     "parish also asks for a <b>Manual J</b> load calculation."),
    ("Site plan",
     "You",
     "May be hand drawn. See the note under the sewage permit below — the "
     "health office says so in writing."),
    ("Legal description / parcel listing",
     "Tax assessor or clerk of court",
     "Several parishes ask for the current parcel listing from the "
     "assessor."),
    ("Property plat",
     "Surveyor, or clerk of court",
     "The health office needs a plat bearing a <b>Louisiana surveyor's "
     "seal</b> <i>or</i> designated a <b>&ldquo;true copy&rdquo; by the clerk "
     "of court</b>. The second route means an existing recorded plat can "
     "satisfy this without a new survey."),
    ("911 / E-911 address assignment",
     "Parish 911 district, sheriff, or permit office",
     "Usually the first step in the whole process. One parish will not assign "
     "the address until the front door is in place — ask early what triggers "
     "it."),
    ("Certificate of occupancy",
     "Your permitting authority",
     "Notify them of completion before anyone occupies. On a new-construction "
     "mortgage the lender records it in the parish conveyance records, and "
     "you owe the lender a copy."),
]))

flow.append(table("Sewage and water", [
    ("<b>LHS-47</b> — Application for Permit for Installation of On-Site "
     "Wastewater Disposal System",
     "Parish health unit (state health office)",
     "The application and the stage-one temporary permit in one document. "
     "Filled out at the health unit — not a blank download. <b>Valid one "
     "year</b>; ask for an extension if the build slips."),
    ("<b>SF-10ST</b> — Applicant Notification and Acknowledgement",
     "Parish health unit",
     "Signed by you. This is the form that states the owner-install rule: you "
     "must do the actual installation, and hiring an unlicensed person for "
     "any part of it voids the exception."),
    ("<b>SF-11ST</b> — Perpetual Maintenance Acknowledgement",
     "Parish health unit", "Signed by you."),
    ("<b>FORM-A</b> — Lot Size Requirements",
     "Parish health unit",
     "Informational, and worth reading before you buy a lot — the statewide "
     "minimum is 22,500&nbsp;sq&nbsp;ft with 125&nbsp;ft of frontage unless "
     "your parish qualifies for the reduced sizes."),
    ("<b>FORM-B</b> — Directions to Property",
     "Parish health unit",
     "A sanitarian is coming out to survey the site. Mark your property "
     "boundaries clearly so they can see where the lot ends."),
    ("Certification by Installer",
     "Your licensed installer",
     "Due within 15&nbsp;days of completion. If you installed the system "
     "yourself you are not a licensed installer, so your final approval runs "
     "through the sanitarian's on-site inspection instead."),
    ("Water well notification",
     "State water administration office",
     "For a domestic well in a non-critical ground water area, due within "
     "<b>60&nbsp;days after</b> installation — and the driller's own 30-day "
     "registration satisfies it."),
    ("<b>DNR-GW-1S</b> — Water Well Registration Short Form",
     "Your licensed water well contractor",
     "Registration is the <b>contractor's</b> duty, not yours. Ask for a copy "
     "for your file anyway."),
]))

flow.append(table("Site, access and hazards", [
    ("Access Connection Permit Certificate",
     "State highway department district",
     "Required where your driveway ties into a state or US route. There is a "
     "residential version of the form. It asks for culvert diameter, length "
     "and material, so lay the site out first."),
    ("Culvert / driveway permit",
     "Parish public works",
     "The parish equivalent, for a parish-maintained road. Several parishes "
     "make it a precondition to the building permit."),
    ("Flood zone determination",
     "Parish floodplain manager",
     "In Louisiana this is usually the same person who signs your building "
     "permit. Several parishes publish a dedicated request form."),
    ("Elevation Certificate",
     "Licensed surveyor",
     "In a Special Flood Hazard Area expect to need it <b>twice</b> — a "
     "proposed certificate before the permit and a final one before the "
     "certificate of occupancy. Book the surveyor early."),
    ("LDEQ notice of intent — construction stormwater",
     "State environmental agency",
     "If the project will disturb <b>one&nbsp;acre</b> or more. Clearing, "
     "grading and the driveway all count toward it."),
    ("LDEQ discharge coverage",
     "State environmental agency",
     "If your system discharges treated effluent to the surface rather than "
     "to a subsurface field."),
]))

# ------------------------------------------------------------------ nothing
flow += k.h2("WHAT NEEDS NO PERMIT — AND THE TRAP INSIDE IT")
flow.append(k.body(
    "Louisiana carves a few things out of code enforcement. Read the "
    "exclusions inside the carve-outs, because they are where people get "
    "caught."))
flow.append(k.callout_long(
    "Farm structures and recreational structures — but not a house",
    [
        Paragraph(
            "A parish &ldquo;shall not enforce that portion of the Uniform "
            "Construction Code which regulates the construction or "
            "improvement of a farm structure or private outdoor recreational "
            "structure, <b>other than a residence or structure attached to a "
            "residence</b>.&rdquo; And the definition closes the same door "
            "again: a farm structure is one built on a farm <b>&ldquo;other "
            "than a residence&rdquo;</b> or a structure attached to it.",
            S["body"]),
        Paragraph(
            "So the barn may be exempt. <b>The house on the farm is not.</b> "
            "Do not let anyone tell you that building on agricultural land "
            "exempts the dwelling.", S["body"]),
    ]))
flow.append(k.callout_long(
    "Small accessory buildings — with a south-Louisiana exception",
    [
        Paragraph(
            "Detached accessory structures at or under "
            "<b>200&nbsp;square&nbsp;feet</b> can fall outside enforcement — "
            "<b>but not in hurricane-prone regions where the ultimate design "
            "wind speed is 130&nbsp;mph or greater</b>, which is a great deal "
            "of south Louisiana. Check your parcel's design wind speed before "
            "relying on the exemption; it is the same number you needed for "
            "the house.", S["body"]),
        Paragraph(
            "And note the statute's own backstop: these exemptions "
            "&ldquo;do[es] not affect the power of the governing authority of "
            "a parish or municipality to issue building permits&rdquo; for "
            "such structures anyway. Exempt from the <i>code</i> is not the "
            "same as exempt from the <i>permit</i>. Ask before you build.",
            S["body"]),
    ]))
flow.append(k.body(
    "One more that is genuinely a different track rather than an exemption: a "
    "<b>manufactured home</b> built to federal HUD standards is not built to "
    "the state code, but its installation is regulated, the installing "
    "plumber must be Louisiana-licensed, and a jurisdiction that collects a "
    "placement fee must inspect the installation. If you are placing rather "
    "than building, that is a different set of paperwork than this kit "
    "covers."))

# ------------------------------------------------------------------ where
flow += k.h2_tight("WHERE TO GET ALL OF IT", reserve=2.0)
flow.append(k.body(
    "Four sources cover almost everything above, and all four are free."))
flow.append(k.bullet(
    "<b>lslbc.gov</b> — the State Licensing Board for Contractors: the "
    "exemption affidavit, the forms page, and the public contractor search "
    "you should be running on every sub."))
flow.append(k.bullet(
    "<b>lsuccc.la</b> — the Uniform Construction Code Commission: the "
    "compiled law and rules volume, the current code editions and their "
    "effective dates, and the public search that confirms your jurisdiction "
    "and lists the inspectors licensed to work in it."))
flow.append(k.bullet(
    "<b>Your parish health unit</b> — every sewage form in this index. They "
    "are not downloads; you get them where you apply."))
flow.append(k.bullet(
    "<b>Your parish or municipal permit office</b> — the building permit "
    "application, the culvert permit, the flood determination, and the answer "
    "to every question this kit tells you to ask locally. LA.4 has the page "
    "to write those answers on."))

# ------------------------------------------------------------------ sources
flow.append(Spacer(1, 8))
flow.append(k.sources_table([
    ("Affidavit title, revision date, notarization and eleven statements",
     "LSLBC, Affidavit Claiming Exemption from Licensure"),
    ("The affidavit goes to the local permit official before issuance",
     "R.S. 37:2157(A)(13); R.S. 37:2160(C)"),
    ("Written subcontractor contracts before work begins",
     "La. R.S. 37:2159(A), (B)"),
    ("No architect or engineer stamp for a prescriptive IRC house",
     "R.S. 37:3737(D)"),
    ("LHS-47 is the application and temporary permit",
     "LAC 51:XIII.731.D, 733.C.8; LDH form SF-10ST"),
    ("Temporary permit valid one year; extension on request",
     "OPH applicant packet"),
    ("Site plan may be hand drawn; plat needs a seal or a clerk's true copy",
     "OPH applicant packet, Steps One and Two"),
    ("Certification by Installer due within 15 days",
     "LAC 51:XIII.701.C"),
    ("Minimum lot area and frontage", "LAC 51:XIII.511.B.4"),
    ("Domestic well notification within 60 days after installation",
     "LAC 43:VI.701.C"),
    ("Well registration is the contractor's duty; short form for domestic "
     "wells", "LAC 56:I.105.A, D"),
    ("Farm structures exempt, other than a residence",
     "R.S. 37:3738(B)(1)(a), (B)(2)"),
    ("Accessory structures at 200 sq ft, excluded in 130 mph wind regions",
     "R.S. 37:3738(B)(1)(b)"),
    ("Exemption does not affect the power to issue building permits",
     "R.S. 37:3738(B)(4)"),
    ("Manufactured homes run on federal standards plus state installation "
     "rules", "R.S. 37:3737(B); R.S. 37:3738(G)"),
    ("Certificate of occupancy recorded by the lender",
     "R.S. 37:3737(E)(1)–(2)"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "la-permit-kit",
                       "LA.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
