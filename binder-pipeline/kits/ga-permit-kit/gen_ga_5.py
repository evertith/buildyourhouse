#!/usr/bin/env python3
"""GA.5 Forms & Documents Index.

Sources verified August 2026:
  O.C.G.A. § 43-41-17(h)   the exemption carries NO state affidavit or form;
                           county affidavits are local practice
  O.C.G.A. § 43-14-13(d)   homeowner trade permits ride the self-perform
                           carve-out where a county permits trades separately
  DPH Rule 511-3-1-.03     septic application "in writing on forms provided
                           by the County Board of Health"; 20-day decision;
                           12-month validity; final inspection + written
                           approval before backfill or use
  O.C.G.A. § 12-5-131.1(a) owner may drill a well at own primary residence
  O.C.G.A. § 12-7-7(a)     land disturbance permit from the certified Local
                           Issuing Authority; EPD where none
  EPD storm-water forms    NPDES NOI for GAR100001 (epd.georgia.gov)
  GDOT driveway regs       "Only original forms may be used. Residential
                           driveway applications can be obtained from the
                           appropriate Area Office." + the Permit Application
                           Information Sheet (Appendix B)
  O.C.G.A. § 44-14-361.5   Notice of Commencement: contents, filing with the
                           clerk of superior court, posting, forfeiture
  GA IECC R402.4.1.2       DET blower-door and duct reports, signed, provided
                           to the code official
  Verified county examples: Fulton County building permit application
    (fultoncountyga.gov); Hall County septic tank permit application
    (hallcounty.org)

Still deliberately hedged: county form names vary everywhere (the two named
examples are just that — examples); whether your county requires an
owner-builder affidavit or homeowner trade disclaimer (worksheet blanks);
Notice of Commencement templates (some clerks publish fill-ins — draft to
the statutory contents list either way); no statewide domestic-well permit
was found (county practice varies); workers'-comp certificates of insurance
are printed as practice guidance, not a statutory requirement.
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

FORM_ID = "GA.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document a Georgia owner-builder meets — what each one is, when "
    "it is needed, and which office it comes from.")

flow.append(k.disclaimer(
    "Georgia keeps almost no statewide forms — the obligations are state "
    "law, the paper is county paper."))
flow.append(Spacer(1, 8))

DOCS = [
    ("Building permit application",
     "The main application, where your jurisdiction issues permits at "
     "all. Local form, local fee schedule; most metro counties file "
     "through an online portal. <b>When:</b> after septic, zoning, and "
     "erosion control are lined up (GA.2). Verified example of the "
     "species: Fulton County's \"Building Permit Application and Site "
     "Plan Checklist.\"",
     "City or county permitting department (see GA.4)"),
    ("Owner-builder affidavit",
     "<b>No state form exists</b> — § 43-41-17(h) requires none. Many "
     "counties require their own notarized owner-builder affidavit as "
     "local practice, and its wording is theirs, not the State's. "
     "<b>When:</b> at application, if required. Record your county's "
     "answer below.",
     "County form, where required; notary usually needed"),
    ("Homeowner trade permit / disclaimer",
     "Where the county permits electrical, plumbing, and HVAC "
     "separately, you apply for the trade permits yourself under the "
     "§ 43-14-13(d) self-perform carve-out; some jurisdictions add a "
     "homeowner disclaimer form acknowledging you are doing licensed-"
     "trade work with your own hands. <b>When:</b> with or after the "
     "building permit, per local practice.",
     "County permitting department — county-specific"),
    ("Septic construction permit application",
     "No statewide form number: \"<i>Application for such a "
     "construction permit shall be made in writing on forms provided by "
     "the County Board of Health.</i>\" Decision due within 20 days of "
     "a completed application; the permit is valid 12 months and gates "
     "all physical development of the lot. <b>When:</b> first — before "
     "any site work, ideally before buying the land. Verified example: "
     "Hall County's \"Septic Tank Permit Application.\"",
     "County health department (environmental health), under DPH Rule "
     "511-3-1"),
    ("Septic final written approval",
     "Issued after the county's final inspection; the system may not be "
     "backfilled or used before it. Later site changes that adversely "
     "affect the system void the approval — keep it with the as-built "
     "drainfield location. <b>When:</b> at system completion, before "
     "building final.",
     "County health department, under Rule 511-3-1-.03(4)"),
    ("Private well — county approval, if any",
     "You may drill on your own property if it is your primary "
     "residence (§ 12-5-131.1(a)); developing for resale requires a "
     "licensed water well contractor. The kit found no statewide "
     "domestic-well permit — some county health departments approve "
     "individual wells, and septic setbacks constrain siting. "
     "<b>When:</b> ask environmental health before drilling.",
     "County health department — requirements vary"),
    ("Land disturbance permit application",
     "Required for land-disturbing activity outside the under-one-acre "
     "single-family exemption. Form names are local. <b>When:</b> "
     "before any disturbance begins.",
     "Certified Local Issuing Authority (county/city); EPD district "
     "office where none exists"),
    ("NPDES Notice of Intent (GAR100001)",
     "For construction disturbing one acre or more — coverage under the "
     "stand-alone construction general permit (GAR100002/100003 for "
     "infrastructure and common developments). <b>When:</b> filed with "
     "EPD before discharge; confirm the current waiting period against "
     "the permit text.",
     "EPD Watershed Protection Branch storm-water forms page, "
     "epd.georgia.gov"),
    ("GDOT residential driveway application",
     "For a driveway connecting to a state route. The regulations are "
     "strict about the paper itself: \"<i>Only original forms may be "
     "used. Residential driveway applications can be obtained from the "
     "appropriate Area Office</i>\" — with the Permit Application "
     "Information Sheet (Appendix B of the driveway regulations). "
     "<b>When:</b> permit in hand before any work in the right of way.",
     "GDOT District Area Office for your county, via dot.ga.gov"),
    ("Notice of Commencement",
     "No state form. Draft to the § 44-14-361.5(b) contents list: "
     "contractor name/address/phone; project name, location, and legal "
     "description; owner name and address; the person at whose "
     "instance improvements are made, if not the owner; surety if "
     "bonded; construction lender if any. <b>When:</b> filed within 15 "
     "days of physically commencing work, and posted on site — not "
     "filing forfeits the lien screen. Some clerks publish fill-in "
     "templates; the contents list governs either way.",
     "You draft it; filed with the clerk of superior court in the "
     "project county"),
    ("DET testing reports — blower door and duct",
     "The two mandatory energy tests, each signed by the certified DET "
     "verifier and \"provided to the code official\": blower door under "
     "5 ACH50 at completion, duct leakage at or under 6 cfm25/100 sq ft "
     "at rough-in or post-construction (excepted when ducts and air "
     "handlers sit entirely inside the envelope). <b>When:</b> duct "
     "test once ducts are sealed; blower door before final. Keep both "
     "forever.",
     "Your DET verifier produces them; copies to the code official and "
     "this binder"),
    ("Subcontractor certificates of insurance",
     "Not a statutory filing — the cheap protection this kit tells you "
     "to collect anyway. Workers' comp does not reach employers with "
     "fewer than three regular employees (§ 34-9-2(a)(2)), but "
     "principal-contractor exposure for uninsured subs' workers "
     "(§ 34-9-8) is unsettled for owner-builders. <b>When:</b> before "
     "each sub starts.",
     "Each subcontractor's insurer, at your request"),
    ("Certificate of occupancy",
     "Issued under your county's own administrative procedures — "
     "Georgia deletes the IRC's administration chapter, so timing and "
     "process are local. Keep it permanently: under § 43-41-17(h) the "
     "CO date starts the 24-month clock that decides whether a future "
     "sale poisons your next owner-built project.",
     "Permitting department, at the end"),
]

rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in DOCS]
flow.append(k.ref_table(
    "Documents a Georgia owner-builder will encounter",
    [k.cellp("Document", bold=True),
     k.cellp("What it is and when you need it", bold=True),
     k.cellp("Where it comes from", bold=True)],
    rows, [1.45 * inch, CW - 1.45 * inch - 1.75 * inch, 1.75 * inch]))

flow.append(Spacer(1, 8))
flow.append(k.body(
    "<b>Your county's answers</b> — the two forms Georgia leaves entirely "
    "to local practice:"))
flow.append(d.FillInRow([("County owner-builder affidavit required?  Y / N "
                          "— form name:", 1.0)]))
flow.append(d.FillInRow([("Homeowner trade disclaimer required?  Y / N — "
                          "form name:", 1.0)]))

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026): no state owner-builder "
    "affidavit — O.C.G.A. § 43-41-17(h), read in full; homeowner trade "
    "work — § 43-14-13(d). Septic application on county forms, the "
    "20-day decision, 12-month validity, and the final-approval rule — "
    "DPH Rule 511-3-1-.03(2)(a), (3)(a), (4), official DPH PDF. Wells — "
    "§ 12-5-131.1(a). Land disturbance permit structure — § 12-7-7(a). "
    "NPDES NOI and the GAR100001 family — EPD storm-water forms page. "
    "GDOT original-forms rule and the Area Office route — GDOT "
    "Regulations for Driveway and Encroachment Control, read directly. "
    "Notice of Commencement contents, filing, posting, and forfeiture — "
    "§ 44-14-361.5(b), (d). DET reports — GA IECC § R402.4.1.2, "
    "§§ R403.3.3–.3.4. Workers' comp threshold and the unsettled "
    "principal-contractor question — § 34-9-2(a)(2); § 34-9-8. County "
    "examples (Fulton, Hall) verified as examples only — your county's "
    "form names will differ."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ga-permit-kit",
                       "GA.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
