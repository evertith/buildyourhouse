#!/usr/bin/env python3
"""MS.5 Forms & Documents Index.

Every document an owner-builder in Mississippi will be handed or asked for,
what it is, when it appears, and where it comes from — plus the structures
Mississippi exempts from its construction code outright, several of which
require an affidavit the reader would otherwise never know to file.

Verified sources:
  § 17-2-7(1),(3)  farm structures are exempt, but ONLY if the owner files an
                   affidavit BEFORE constructing, stating the purpose or
                   intended use
  § 17-2-9(3)      hunting and fishing camps are exempt, but the owner must
                   file a sworn affidavit with the board of supervisors, and
                   the camp must be in an unincorporated area
  § 17-2-9(4)      manufactured housing built to the federal standard
  § 17-2-9(5)      Pearl River County only: salvage lumber and green cut
                   timber for personal use, not for sale
  § 17-2-7(5), § 17-2-9(6)  none of these exemptions reach NFIP floodplain
                   ordinances
  § 41-67-*        the wastewater documents, as in MS.2
  § 73-59-17       evidence of license or exemption at the permit counter

Deliberately NOT claimed: that any of these forms has a statewide number or
format apart from the MSDH ones. Mississippi has no statewide building permit
application, so every local document here is described by what it does rather
than by a form number that would be wrong in most counties.
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

FORM_ID = "MS.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document you will be handed or asked for, what it is, when it "
    "appears, and where it comes from — plus the buildings Mississippi "
    "exempts outright, and the affidavits that unlock them.")

flow.append(k.disclaimer(
    "Only the wastewater forms have statewide numbers. Mississippi has no "
    "statewide building permit application, so local documents are described "
    "by what they do."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- state forms
flow += k.h2_tight("STATE-LEVEL DOCUMENTS")

state_rows = [
    [k.cellp("<b>Statement of Intent</b><br/>MSDH Form 908"),
     k.cellp("Your notice of intent for an onsite wastewater system. Filed "
             "with the legal description, a plot plan and the fee. Required "
             "<b>before</b> you construct or place the residence"),
     k.cellp("MSDH, Division of On-site Wastewater — msdh.ms.gov")],
    [k.cellp("<b>Site soil evaluation</b>"),
     k.cellp("The evaluation of your soil, carried out by the local "
             "environmentalist, that determines which systems your lot will "
             "accept. Can move the house on the lot, which is why it comes "
             "early"),
     k.cellp("MSDH, after Form 908")],
    [k.cellp("<b>Permit / recommendation</b>"),
     k.cellp("Issued to you after the evaluation. Lists the system options "
             "recommended for your property. <b>This is what your water "
             "supplier asks to see before setting a meter</b>"),
     k.cellp("MSDH")],
    [k.cellp("<b>Installation affidavit</b>"),
     k.cellp("Signed by your <b>certified installer</b> after the system goes "
             "in, and filed with the Department. Without it there is no final "
             "approval"),
     k.cellp("Certified installer → MSDH")],
    [k.cellp("<b>Maintenance affidavit</b>"),
     k.cellp("Signed by <b>you</b>, and required only for an advanced "
             "treatment system. Goes with the continuing maintenance "
             "agreement the statute requires in perpetuity"),
     k.cellp("You → MSDH")],
    [k.cellp("<b>Final approval</b>"),
     k.cellp("The Department's sign-off once it holds the affidavits. Ask for "
             "it by name and keep it — your lender, insurer and eventual "
             "buyer will all want it"),
     k.cellp("MSDH")],
    [k.cellp("<b>Two-acre exemption affidavit</b>"),
     k.cellp("Signed by the person who installed the system, attesting that "
             "all wastewater is contained on the tract and no watercourse is "
             "impacted. Only relevant on two acres or more — and only if no "
             "county ordinance, water association or lender requires final "
             "approval anyway"),
     k.cellp("Installer → MSDH")],
    [k.cellp("<b>Contractor license verification</b>"),
     k.cellp("Not a form you file — a check you run, on every electrical, "
             "plumbing, mechanical and HVAC contractor, no matter how small "
             "the job. Print or screenshot the result and date it"),
     k.cellp("State Board of Contractors — msboc.us")],
]
flow.append(k.ref_table(
    "Documents with a statewide identity",
    [k.cellp("Document", bold=True), k.cellp("What it is", bold=True),
     k.cellp("Where from", bold=True)],
    state_rows, [1.5 * inch, CW - 1.5 * inch - 1.5 * inch, 1.5 * inch]))

# ---------------------------------------------------------------- local
flow += k.h2_tight("LOCAL DOCUMENTS — NAMES VARY, FUNCTIONS DO NOT")

local_rows = [
    [k.cellp("<b>Building permit application</b>"),
     k.cellp("Exists only where a code is enforced. No statewide form. Expect "
             "to supply plans, a site plan and your septic paperwork")],
    [k.cellp("<b>Evidence of exemption</b>"),
     k.cellp("Whatever your building official accepts to satisfy § 73-59-17 — "
             "a recorded deed plus a signed statement, a local homeowner "
             "affidavit, or a declaration on the application itself. "
             "<b>Ask what form it takes before you drive there</b>")],
    [k.cellp("<b>Site plan / plot plan</b>"),
     k.cellp("House, setbacks, driveway, well and septic field. The same "
             "drawing usually serves the health department and the building "
             "office, so draw it once and well")],
    [k.cellp("<b>Recorded deed</b>"),
     k.cellp("Proof you own the property, which is what the licensing "
             "exemption is built on. Chancery clerk")],
    [k.cellp("<b>Floodplain development permit</b>"),
     k.cellp("Required in a mapped flood hazard area in a community that "
             "takes part in the National Flood Insurance Program — and the "
             "construction-code exemptions expressly do not reach it")],
    [k.cellp("<b>Elevation certificate</b>"),
     k.cellp("Prepared by a surveyor or engineer where you build in a flood "
             "hazard area. Drives your flood insurance rating as well as "
             "compliance")],
    [k.cellp("<b>Driveway / culvert permit</b>"),
     k.cellp("County road department for a county road; MDOT for a numbered "
             "state highway. Settle the culvert size before you grade")],
    [k.cellp("<b>E-911 address assignment</b>"),
     k.cellp("The new address for the dwelling. Utilities and lenders both "
             "ask for it, and it takes longer than you expect")],
    [k.cellp("<b>Termite treatment certificate</b>"),
     k.cellp("From the pest control operator. Mississippi is wholly within "
             "the region the code marks \"very heavy\" for termites, and "
             "buyers and lenders ask for this years later")],
    [k.cellp("<b>Utility service applications</b>"),
     k.cellp("Temporary construction power, permanent service, and water "
             "membership. Ask your electric supplier early what release it "
             "needs before it will energize")],
    [k.cellp("<b>Certificate of occupancy</b>"),
     k.cellp("Issued at the end where a building code is enforced. <b>Where "
             "no code is enforced there is no certificate of occupancy</b> — "
             "which is why the private inspection reports in MS.3 matter so "
             "much for resale")],
]
flow.append(k.ref_table(
    "Documents whose name depends on your county",
    [k.cellp("Document", bold=True), k.cellp("What it is", bold=True)],
    local_rows, [2.05 * inch, CW - 2.05 * inch]))

# ---------------------------------------------------------------- exempt
flow += k.h2_tight("WHAT MISSISSIPPI EXEMPTS OUTRIGHT — AND THE AFFIDAVITS")
flow.append(k.body(
    "Even where a construction code is fully enforced, the statute carves out "
    "several categories of structure. Two of them are unlocked by an "
    "affidavit most owners never learn about, and one of those has to be "
    "filed <b>before</b> you build."))

ex_rows = [
    [k.cellp("<b>Farm structures</b>"),
     k.cellp("A structure on a farm, other than a residence or something "
             "attached to it — barns, sheds, poultry houses, but not public "
             "livestock areas. A building that later converts to another use "
             "loses the exemption"),
     k.cellp("<b>Yes — before you build.</b> An affidavit filed with the "
             "county or municipal official responsible for enforcing the "
             "code, stating the purpose or intended use")],
    [k.cellp("<b>Hunting and fishing camps</b>"),
     k.cellp("A private unattached outdoor recreational structure. Must be in "
             "an <b>unincorporated</b> area of the county, within or near "
             "land where hunting or fishing may legally take place"),
     k.cellp("<b>Yes.</b> A signed affidavit sworn by the owner and filed "
             "with the board of supervisors")],
    [k.cellp("<b>Manufactured housing</b>"),
     k.cellp("Housing built to the Federal Manufactured Home Construction and "
             "Safety Standards Act — governed by the federal standard rather "
             "than the local code"),
     k.cellp("No affidavit in the code exemption")],
    [k.cellp("<b>Salvage and green timber</b><br/>(Pearl River County only)"),
     k.cellp("Pearl River County and its municipalities may not enforce code "
             "provisions barring, or requiring permit approval for, the use "
             "of salvage lumber or green cut timber — provided it is for "
             "personal use and not for sale"),
     k.cellp("No affidavit named")],
    [k.cellp("<b>Industrial and pipeline facilities</b>"),
     k.cellp("Manufacturing, utilities, telecommunications, pipelines and gas "
             "processing, by federal industry classification. Not relevant to "
             "a house, listed so you recognize it in the statute"),
     k.cellp("—")],
]
flow.append(k.ref_table(
    "Structures outside the state construction code",
    [k.cellp("Category", bold=True), k.cellp("Scope", bold=True),
     k.cellp("Affidavit required?", bold=True)],
    ex_rows, [1.45 * inch, CW - 1.45 * inch - 1.95 * inch, 1.95 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "The limit on every one of these exemptions", [
        Paragraph("None of them reaches flood rules. Both exemption sections "
                  "close with the same sentence: \"<i>The provisions of this "
                  "section shall not apply to any floodplain management "
                  "ordinances or regulations necessary for eligibility for "
                  "the National Flood Insurance Program.</i>\" A barn, a "
                  "hunting camp, or a manufactured home in a mapped flood "
                  "hazard area is still subject to the floodplain ordinance.",
                  S["body"]),
        Paragraph("And note what the farm-structure exemption does <b>not</b> "
                  "do: it expressly \"<i>does not affect the authority of the "
                  "governing body of a county or municipality to issue "
                  "building permits before an affidavit … is filed</i>.\" "
                  "File the affidavit first, not after somebody asks.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- keeping
flow += k.h2_tight("WHAT TO KEEP, AND FOR HOW LONG")
flow.append(k.body(
    "Keep everything in this binder for as long as you own the house, and "
    "hand it to the buyer when you sell. An owner-built Mississippi house "
    "with a complete paper trail is an ordinary transaction; the same house "
    "without one is a negotiation. The documents that matter most a decade "
    "later are the ones nobody thinks to keep: the health department's final "
    "approval, the termite certificate, the trade contractors' license "
    "verifications, and — if you built where no code applied — your private "
    "inspection reports and dated photographs."))

flow += k.check_table("Your permanent file", [
    ("Health department final approval, or the two-acre exemption paperwork",
     [("Filed:", 1.0)]),
    ("Septic permit or recommendation, and the as-built location of the "
     "field", [("Filed:", 1.0)]),
    ("Building permit and certificate of occupancy, if your parcel had them",
     [("Filed:", 1.0)]),
    ("Termite treatment certificate", [("Filed:", 1.0)]),
    ("Every trade contractor's license verification, dated",
     [("Filed:", 1.0)]),
    ("Elevation certificate and flood documentation, if applicable",
     [("Filed:", 1.0)]),
    ("Private inspection reports and milestone photographs",
     [("Filed:", 1.0)]),
    ("The clerk's written confirmation of your parcel's code status — the "
     "single most useful piece of paper for a no-code build",
     [("Filed:", 1.0)]),
], notes_header="Where kept")

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("Farm structures are exempt only if the owner files an affidavit before "
     "constructing, stating the purpose or intended use; the exemption does "
     "not affect the authority to issue permits before it is filed",
     "§ 17-2-7(1), (3), (4)"),
    ("Hunting and fishing camps are exempt on a sworn affidavit filed with "
     "the board of supervisors, and must be in an unincorporated area",
     "§ 17-2-9(3)"),
    ("Manufactured housing built to the federal standard, and Pearl River "
     "County salvage lumber and green cut timber for personal use",
     "§ 17-2-9(4), (5)"),
    ("No construction-code exemption reaches NFIP floodplain ordinances",
     "§ 17-2-7(5); § 17-2-9(6)"),
    ("The wastewater documents: notice of intent, department approval, the "
     "two-acre exemption affidavit, and the perpetual maintenance agreement "
     "for advanced systems",
     "§ 41-67-5; § 41-67-6(7); § 41-67-7(1), (5)"),
    ("The building official must be furnished evidence of license or "
     "exemption before issuing a permit", "§ 73-59-17"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ms-permit-kit",
                       "MS.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
