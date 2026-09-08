#!/usr/bin/env python3
"""AZ.4 Where to File Directory.

Every web address in this document was confirmed in September 2026 — either
returning to an ordinary request, or (for the state agencies and a handful of
counties that sit behind an automated-request wall) opening in a browser. No
phone numbers appear anywhere in this kit — they go stale faster than anything
else on a printed page, and every office below can be reached from its own
site.

The organizing idea: Arizona has 15 counties and 91 municipalities, every one
of which adopts its own code, and the septic program is delegated by ADEQ to a
different county office in each county. So this document is the rule of the
road (city inside limits, county outside; the adopting ordinance is the
authority), then every county with its building and septic offices as its own
site names them, the big cities, the two opt-out counters and the no-code
county, and the state agencies.

Verified in this pass:
  § 9-802; § 11-864     the adopting ordinance is filed with the clerk
  § 9-836(A); § 11-1606 the handout
  § 49-107(A)           ADEQ delegation to county agencies
  County and city pages, September 2026 — URL set in the research dossier
  Cochise Owner-Builder Amendment page and PDF; Coconino AMMP page; Greenlee
                        Planning & Zoning page and County Engineer letter
  roc.az.gov; azdeq.gov; azwater.gov   read in a browser (automated requests
                        refused)
  ADEQ NOI form DWS 402 (rev. April 2025) as posted by La Paz County
  Legal Information Institute reproduction of the A.A.C.; Cochise County's
                        hosted copy of the Secretary of State's 18 A.A.C. 9
                        compilation

DELIBERATELY NOT PRINTED:
  - Apache and Santa Cruz county URLs. Both sites refused every request for
    this pass; their offices are named from archived copies of the counties'
    own documents and marked confirm.
  - Any URL longer than a line. Those are given as site → page path.
  - Arizona 811's web address (DNS failed twice on 8 September 2026).
  - The Industrial Commission's web address (not read this pass).
  - Any fee figure; any phone number.
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

FORM_ID = "AZ.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Fifteen counties, the big cities, the two opt-out counters, the no-code "
    "county and the three state agencies — as their own sites name them, "
    "September 2026.")

flow.append(k.disclaimer(
    "Every web address here was checked in September 2026. The Registrar, "
    "ADEQ and ADWR sites refuse automated requests and open only in a "
    "browser — if a link checker tells you they are down, they are not. "
    "Where a county's site refused every request, the office is named from "
    "the county's own archived documents and marked confirm."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- rule of road
flow += k.h2_tight("THE RULE OF THE ROAD", reserve=2.0)
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp(f"<b>Inside city or town limits, the city's ordinance governs; "
             f"outside, the county's.</b> The two routinely differ, and only "
             f"the city permit carries the §&#160;9-835 clocks (AZ.3). Ask "
             f"for the adopting ordinance number — the ordinance, "
             f"\"published in full\" and filed with the clerk, is the "
             f"authority ({ars('9-802')}; {sec('11-864')}) — and take the "
             f"handout you are owed at application ({sec('9-836(A)')}; "
             f"{sec('11-1606')}).")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp(f"<b>Septic is a different office, and it is the county's "
             f"even inside a city.</b> ADEQ delegates its onsite program "
             f"under {ars('49-107(A)')} to one agency per county — a "
             f"development-services division in nine, a health department "
             f"in four, Maricopa's Environmental Services Department, and "
             f"one (Cochise) its pages do not name. Named below.")],
]
flow.append(k.ref_table(
    "Two things before any address",
    [k.cellp("", bold=True, center=True), k.cellp("Rule", bold=True)],
    rows, [0.35 * inch, CW - 0.35 * inch]))

# ---------------------------------------------------------------- counties
flow += k.h2_tight("THE FIFTEEN COUNTIES — BUILDING PERMIT AND SEPTIC, "
                   "AS THEIR OWN SITES NAME THEM", reserve=2.4)
flow.append(k.body(
    "Code editions for each are in AZ.2. Addresses longer than a line are "
    "given as site → page."))
C = k.cellp
W = CW - 0.95 * inch
rows = [
    [C("<b>Maricopa</b>"),
     C("<b>Building:</b> Planning &amp; Development — "
       "maricopa.gov/2753/Adopted-Regulations. The county FAQ: \"Written "
       "documentation of an Arizona licensed contractor or owner-builder "
       "classification is required for all building permits per state law\" "
       "(citing §&#160;32-1169).<br/>"
       "<b>Septic:</b> Environmental Services Department — "
       "maricopa.gov/1631/Onsite-Wastewater-Septic-Systems")],
    [C("<b>Pima</b>"),
     C("<b>Building:</b> Development Services — "
       "pima.gov/1038/Building-Permits-Resources<br/>"
       "<b>Septic:</b> Development Services, On-Site Wastewater — "
       "pima.gov/1086/On-Site-Wastewater-Treatment-Facilities")],
    [C("<b>Pinal</b>"),
     C("<b>Building:</b> Building Safety — pinal.gov/189/Building-Safety<br/>"
       "<b>Septic:</b> Aquifer Protection Division (\"delegated by ADEQ\") — "
       "pinal.gov/185/Wells-Septic")],
    [C("<b>Yavapai</b>"),
     C("<b>Building:</b> Development Services — "
       "yavapaiaz.gov/Development-and-Permits/Codes-Ordinances<br/>"
       "<b>Septic:</b> Environmental Services Unit of Development Services — "
       "yavapaiaz.gov → Development Services → Environmental Services Unit")],
    [C("<b>Mohave</b>"),
     C("<b>Building:</b> Development Services, Building Division — "
       "mohave.gov/departments/development-services/building-division/ "
       "(the permit application carries the exemption checkbox and "
       "block)<br/>"
       "<b>Septic:</b> Environmental Quality / Waste Disposal (\"delegated … "
       "by ADEQ\") — publishes an \"On-Site Wastewater Application for "
       "Owner/Builders\" as an owner-builder packet")],
    [C("<b>Cochise</b>"),
     C("<b>Building:</b> Development Services, Building Safety — "
       "cochise.az.gov/211/Building-Safety (2024 codes from 1&#160;Sep 2026). "
       "<b>Owner-Builder Amendment:</b> cochise.az.gov/212/Owner-Builder-"
       "Amendment, with the amendment text linked as a PDF<br/>"
       "<b>Septic:</b> not stated on the county pages read; the amendment "
       "refers to \"Cochise County Environmental Health Department "
       "regulations\" — <b>confirm</b> the office at the counter")],
    [C("<b>Coconino</b>"),
     C("<b>Building:</b> Community Development — "
       "coconino.az.gov/2391/Building-Codes-Ordinances-Design-Criteri. "
       "<b>AMMP:</b> coconino.az.gov/2173/Alternative-Methods-and-Materials-"
       "Permit<br/>"
       "<b>Septic:</b> Community Development, Environmental Quality Division "
       "— coconino.az.gov/1156/Environmental-Quality")],
    [C("<b>Navajo</b>"),
     C("<b>Building:</b> Planning &amp; Development Services — "
       "navajocountyaz.gov/289/Building-Information<br/>"
       "<b>Septic:</b> Planning &amp; Development Services (its Environmental "
       "Health page says it \"does not inspect new septic systems\")")],
    [C("<b>Apache</b>"),
     C("<b>Building:</b> the county site refused every request in September "
       "2026; the code editions in AZ.2 are from an archived copy of the "
       "county's own FAQ, which also says no license is needed \"if you are "
       "an owner-builder and only hire employees.\" <b>Confirm the office "
       "and the edition at the counter.</b><br/>"
       "<b>Septic:</b> County Health Department")],
    [C("<b>Gila</b>"),
     C("<b>Building:</b> Community Development, Building Safety — "
       "gilacountyaz.gov → Community Development → Building Safety → "
       "Adopted Building Code (a \"signed Owner Builder Statement\" is "
       "required)<br/>"
       "<b>Septic:</b> Community Development (Wastewater)")],
    [C("<b>Graham</b>"),
     C("<b>Building:</b> Planning &amp; Zoning — "
       "graham.az.gov/277/Planning-Zoning (\"'dirt work' does not require a "
       "permit, everything else does\")<br/>"
       "<b>Septic:</b> Health Department — graham.az.gov/418/Septic-Wastewater")],
    [C("<b>Greenlee</b>"),
     C("<b>Building:</b> Planning &amp; Zoning — "
       "greenlee.az.gov/ova_dep/planning-and-zoning/ — where the County "
       "Engineer's \"Building Codes – Load Stds\" letter is posted: no "
       "code, no plan review, no inspection, no CO, and \"a building permit "
       "at no cost when a Zoning Use Permit and Floodplain Permit are "
       "issued\"<br/>"
       "<b>Septic:</b> Health Department")],
    [C("<b>La Paz</b>"),
     C("<b>Building:</b> Community Development — Ord. 2026-01 at "
       "co.la-paz.az.us/DocumentCenter/View/9776 (\"Owner's Acknowledgment "
       "&amp; Verification of Information\" form)<br/>"
       "<b>Septic:</b> Community Development — "
       "co.la-paz.az.us/590/SANITATION-SEPTIC, which also posts the ADEQ "
       "Notice of Intent form, the R18-9-A312(C) setback table and the "
       "well–property-line waiver form")],
    [C("<b>Santa Cruz</b>"),
     C("<b>Building:</b> the county site refused every request in September "
       "2026; editions in AZ.2 are from an archived copy of the county page "
       "(\"Owner Builder Form\"). <b>Confirm at the counter.</b><br/>"
       "<b>Septic:</b> Environmental Health — conventional systems only; "
       "others are directed to ADEQ")],
    [C("<b>Yuma</b>"),
     C("<b>Building:</b> Development Services — yumacountyaz.gov → "
       "Development Services → Laws &amp; Guidelines → Building Safety Code "
       "Amendments (adopts the City of Yuma's code under "
       "§&#160;11-861(C)(1))<br/>"
       "<b>Septic:</b> Development Services, Environmental Programs")],
]
flow.append(k.ref_table(
    "Unincorporated areas — verified September 2026",
    [C("County", bold=True), C("Building permit · Septic program", bold=True)],
    rows, [0.95 * inch, W]))

# ---------------------------------------------------------------- cities
flow += k.h2_tight("THE BIG CITIES — WHERE THE PAGE WAS READ", reserve=2.4)
flow.append(k.body(
    "Nine cities whose building-code page was read directly, with the "
    "owner-builder form each names. The other eleven in AZ.2's map — Mesa, "
    "Gilbert, Peoria, Prescott, Yuma, Sierra Vista, Kingman, Surprise, "
    "Buckeye, Queen Creek, Casa Grande — file through their Development "
    "Services or Building Safety pages; their edition rows are in AZ.2."))
rows = [
    [C("<b>Phoenix</b>"),
     C("Planning and Development — phoenix.gov → Planning and Development → "
       "Codes and Ordinances → Building Code. 2024 Phoenix Building "
       "Construction Code; HVAC-GFCI enforcement deferred to 1&#160;Mar 2027")],
    [C("<b>Tucson</b>"),
     C("Planning and Development Services — tucsonaz.gov → Planning and "
       "Development Services → Codes → Building Codes. \"Owner/Builder "
       "Affidavit\" on the Residential Permits page; rentals are commercial "
       "and need a licensed contractor")],
    [C("<b>Scottsdale</b>"),
     C("scottsdaleaz.gov/codes-and-ordinances/building-codes. "
       "\"Owner-Builder Declaration form\" required by the Tax Audit "
       "Division")],
    [C("<b>Chandler</b>"),
     C("Development Services — chandleraz.gov → Development Services → "
       "Building Safety, Plan Review, Permits and Inspections. Owner may "
       "perform the work; a leased or rented home needs a licensed "
       "contractor")],
    [C("<b>Glendale</b>"),
     C("Building Safety — "
       "glendaleaz.gov/Business/Building-Safety-Codes-Services/Building-Codes. "
       "Owners doing their own work \"will be required to sign "
       "verification\"")],
    [C("<b>Tempe</b>"),
     C("Community Development, Building Safety — tempe.gov → Community "
       "Development → Building Safety → Building Codes and Amendments. "
       "2018/2017 accepted through 31&#160;Dec 2026")],
    [C("<b>Flagstaff</b>"),
     C("flagstaff.az.gov/5142/Building-Code. Owner Authorization form; "
       "\"2024 Codes … being evaluated\"")],
    [C("<b>Lake Havasu City</b>"),
     C("lhcaz.gov/593/Codes. Notarized \"Owner/Builder Certification\" "
       "citing §&#160;32-1121(A)(5), at "
       "lhcaz.gov/DocumentCenter/View/1163/Owner---Builder-Certification-PDF")],
    [C("<b>Goodyear</b>"),
     C("Development Services — goodyearaz.gov → Development Services → "
       "Homeowner Permit FAQs: live in it, no licensed contractor needed; "
       "rent it out, licensed contractors required")],
]
flow.append(k.ref_table(
    "Inside city limits — verified September 2026",
    [C("City", bold=True), C("Office · page · what it says about owners",
                             bold=True)],
    rows, [1.25 * inch, CW - 1.25 * inch]))

# ---------------------------------------------------------------- state
flow += k.h2_tight("THE STATE AGENCIES — AND WHERE THE LAW ITSELF IS",
                   reserve=2.4)
rows = [
    [C("<b>Registrar of Contractors</b>"),
     C("roc.az.gov — license search (verify every contractor on the contract "
       "date, first-payment date and start date, §&#160;32-1132(C)); "
       "complaints (two years from occupancy, §&#160;32-1162(A)); the "
       "Residential Contractors' Recovery Fund; classifications at "
       "roc.az.gov/license-classifications. The Registrar licenses "
       "contractors, not you, and issues no permit")],
    [C("<b>ADEQ — septic</b>"),
     C("azdeq.gov/onsite-wastewater-treatment-facilities — ADEQ's onsite "
       "wastewater page. You file with your county's delegated program "
       "(above), not with ADEQ. La Paz County posts the current Notice of "
       "Intent form (DWS 402, rev. April 2025) at "
       "co.la-paz.az.us/DocumentCenter/View/9258")],
    [C("<b>ADWR — wells</b>"),
     C("azwater.gov/permitting-wells/well-drilling-arizona — ADWR's "
       "well-drilling page: the Notice of Intention to Drill and the single "
       "well license start here, and so does the question of whether your "
       "parcel sits in an active management area")],
    [C("<b>Flood maps</b>"),
     C("msc.fema.gov/portal/home — the Flood Insurance Rate Map the county "
       "floodplain permit and the septic limiting-condition test both read")],
    [C("<b>The statutes</b>"),
     C("azleg.gov/ars/&lt;title&gt;/&lt;section&gt;.htm — title unpadded, "
       "section padded to five digits: azleg.gov/ars/32/01121.htm, "
       "azleg.gov/ars/11/00321.htm; a decimal section uses a hyphen, "
       "azleg.gov/ars/9/00470-01.htm. A title's table of contents, "
       "azleg.gov/arsDetail/?title=32, shows a section published in two "
       "versions")],
    [C("<b>The rules</b>"),
     C("Arizona Administrative Code, one PDF per chapter at "
       "apps.azsos.gov/public_services/Title_18/18-09.pdf (septic) — and, "
       "far easier to read, section by section at "
       "law.cornell.edu/regulations/arizona (search \"R18-9-A312\" or "
       "\"R12-15-818\")")],
]
flow.append(k.ref_table(
    "Verified September 2026 — no phone numbers, by design",
    [C("What you need", bold=True), C("Where", bold=True)],
    rows, [1.55 * inch, CW - 1.55 * inch]))
flow.append(k.cite(
    "<b>Two offices this kit names without an address.</b> The Industrial "
    "Commission of Arizona, for the workers' compensation question in AZ.1 — "
    "its site was not read for this pass. And Arizona 811 for utility "
    "locates before you dig — its web address did not resolve when checked "
    "on 8&#160;September 2026; call 811 from any phone."))

# ---------------------------------------------------------------- sequence
flow += k.h2_tight("THE SEQUENCE, WHATEVER YOUR COUNTY", reserve=2.4)
flow.append(k.body(
    "\"No code\" is not \"no paperwork,\" and three of these fix things that "
    "cannot be fixed later — the recording date, the septic footprint, and "
    "the sale clock."))
rows = [
    [C("<b>1</b>", center=True), C("<b>Record the deed</b>"),
     C("In your own name as a natural person, before any construction — "
       "the §&#160;33-1002 owner-occupant test; nothing repairs the date "
       "later")],
    [C("<b>2</b>", center=True), C("<b>Confirm the jurisdiction</b>"),
     C("City or county; the adopting ordinance number and editions; the "
       "handout; whether the counter wants the Registrar's signature on your "
       "§&#160;32-1169 statement")],
    [C("<b>3</b>", center=True), C("<b>Septic site investigation</b>"),
     C("By a registered investigator. The 100-ft well setback, the 50-ft "
       "line on a well-served lot and the 100% reserve area decide where "
       "the house and well can go — before the footprint is fixed")],
    [C("<b>4</b>", center=True), C("<b>Zoning, floodplain, address</b>"),
     C("The zoning use permit on the §&#160;11-815(B) sketch and the "
       "floodplain permit are what the county building permit issues on, "
       "even in Greenlee")],
    [C("<b>5</b>", center=True), C("<b>Well notice</b>"),
     C("ADWR notice of intent with the county-health-approved site plan on "
       "five acres or less; the drilling card before the rig; or your own "
       "single well license after the exam")],
    [C("<b>6</b>", center=True), C("<b>Septic Notice of Intent</b>"),
     C("To the delegated county; no construction until the Construction "
       "Authorization; two years to finish")],
    [C("<b>7</b>", center=True), C("<b>Building permit</b>"),
     C("With the §&#160;32-1169 statement naming every licensed sub. On a "
       "city permit the §&#160;9-835 clocks start at submission; on a county "
       "permit, none does")],
    [C("<b>8</b>", center=True), C("<b>Utility and 811</b>"),
     C("Ask the power company in writing what it needs before setting a "
       "meter, and call 811 before any excavation")],
]
flow.append(k.ref_table(
    "Eight steps, in order",
    [C("", bold=True, center=True), C("Step", bold=True),
     C("Which office, and why the order", bold=True)],
    rows, [0.35 * inch, 1.7 * inch, CW - 2.05 * inch]))

# ---------------------------------------------------------------- write-in
# 2.2in: the first write-in row here is three lines of text plus two field
# lines, so the table's first chunk (title, header, row) needs ~2in.
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT",
                   reserve=2.2)
flow += k.check_table(
    "Every office that touches this build, confirmed and dated",
    [
        ("Jurisdiction (city or county) and its permit office; the adopting "
         "ordinance number and the editions on it; date confirmed:",
         [("Jurisdiction / office", 0.6), ("Ordinance", 0.4),
          ("Editions", 0.6), ("Date", 0.4)]),
        ("ADEQ-delegated septic program and the registered site "
         "investigator; ADWR file number and the licensed driller or my "
         "single well license:",
         [("Septic office", 0.5), ("Investigator", 0.5),
          ("ADWR file", 0.45), ("Driller / license", 0.55)]),
        ("Zoning office and setbacks; floodplain administrator and flood "
         "status; 911 addressing; fire district — its adopted code governs "
         "the house:",
         [("Zoning office", 0.55), ("Setbacks", 0.45), ("Flood", 0.3),
          ("911", 0.3), ("Fire dist.", 0.4)]),
        ("Electric utility and what it needs, in writing, before setting a "
         "meter; road authority for the driveway permit; date I called 811:",
         [("Utility", 0.35), ("Requires", 0.65), ("Road authority", 0.6),
          ("811 called", 0.4)]),
        ("ROC license numbers of every contractor on my § 32-1169 "
         "statement, verified on the contract, first-payment and start "
         "dates:", [("Contractors and ROC nos.", 1.0)]),
    ], date_w=0.9, notes_w=1.8)
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "az-permit-kit",
                       "AZ.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
