#!/usr/bin/env python3
"""SC.4 Where to File Directory.

Prints HOSTS and navigation paths rather than deep links. Two reasons, both
learned from South Carolina specifically:

  - Domain churn here is severe. charlestoncounty.org, spartanburgcounty.org,
    yorkcountygov.com, florenceco.org, sumtercountysc.org, mylancastersc.org
    and gtcounty.org have all been superseded by .gov hosts. Worse,
    laurenscounty.us is no longer county-controlled at all — it now redirects
    to an unrelated commercial website. A printed deep link is a liability.
  - CivicPlus numeric page IDs get recycled between departments, so a printed
    /191/Building-Codes can silently become the Fire Coordinator's page.

A host plus a navigation path survives both. Every host below was fetched and
content-confirmed in September 2026.

No phone numbers anywhere, by design: every office publishes current contact
details on the page this directory sends you to, and printed numbers go stale
faster than anything else on the sheet.
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
NB = k.NB
sec = k.sec

FORM_ID = "SC.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Where to File"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "Which office has your parcel, the offices beyond the "
                 "building department, and a page to record what you "
                 "confirmed.")
flow.append(k.disclaimer())

# --------------------------------------------------------- jurisdiction
flow += k.h2("FIRST, ESTABLISH WHO ACTUALLY HAS YOUR PARCEL")
flow.append(k.body(
    f"South Carolina answers the “does anyone permit out here?” question in "
    f"statute: {sec('6-9-10')}(A) requires all municipalities and counties to "
    f"enforce the codes, and {sec('6-9-30')}(A) requires each county to "
    f"appoint a building official “so that the unincorporated area of the "
    f"county is under the jurisdiction of a building official.” There is no "
    f"general unincorporated gap here. <b>Assume a permit is required "
    f"everywhere in South Carolina.</b>"))
flow.append(k.body(
    "The live question is therefore <i>which</i> office, and the answer turns "
    "on one thing: <b>are you inside a municipality's limits?</b> If you are, "
    "the city or town issues your permit and the county does not. Annexed "
    "parcels on the fringes of Greenville, Columbia, Charleston, Rock Hill, "
    "Bluffton and Fort Mill are where owner-builders most often apply to the "
    "wrong office and lose weeks. Check the parcel against your county's GIS "
    "viewer before you fill anything in, and if the boundary is ambiguous, "
    "ask both offices in writing."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "There is one lawful way out of enforcement, and no public list of who "
    "used it", [
        Paragraph(f"Section&#160;6-9-30(B) lets a municipality or county "
                  "that “determines that it is unable to arrange for services "
                  "for any annual period at costs totally within the schedule "
                  "of fees recommended in the appendices to the building "
                  "codes” submit an affidavit to the Building Codes Council "
                  "and be “exempt from the requirements of this chapter” for "
                  "up to five years, renewable. It is a financial-hardship "
                  "escape, and it is real law.", S["body"]),
        Paragraph("The Council does not publish a roster of who currently "
                  "holds one. So if a rural office tells you it does not "
                  "issue building permits, do not just accept it and do not "
                  "assume it is wrong: ask whether the jurisdiction has filed "
                  f"a {sec('6-9-30')}(B) affidavit, and get the answer in "
                  "writing. Your lender, your insurer and your eventual buyer "
                  "will all ask the same question.", S["body"]),
    ]))

# --------------------------------------------------- offices beyond BD
flow += k.h2_tight("THE OFFICES BEYOND THE BUILDING DEPARTMENT", reserve=2.2)
rows = [
    [k.cellp("<b>Register of deeds</b>"),
     k.cellp("Where the notice that keeps your exemption alive is recorded, "
             f"indexed under your name in the grantor's index "
             f"({sec('40-59-260')}(E)). County-level office; some counties "
             f"combine it with the clerk of court."),
     k.cellp("Your county")],
    [k.cellp("<b>Clerk of court</b>"),
     k.cellp("Where a Notice of Project Commencement is filed if you use one "
             f"— fifteen days, $15 ({sec('29-5-23')}). Either office takes "
             f"it; ask yours which."),
     k.cellp("Your county")],
    [k.cellp("<b>Septic</b>"),
     k.cellp("<b>des.sc.gov</b> → Permits &amp; Regulations → Septic Tanks. "
             "The agency also publishes homeowner resources, a “before you "
             "buy land” page and an e-permitting route."),
     k.cellp("SCDES")],
    [k.cellp("<b>Private wells</b>"),
     k.cellp("<b>des.sc.gov</b> → Programs → Bureau of Water → Residential "
             "Wells. Same agency as septic, different bureau — and there is a "
             "separate coastal plain well map at <b>gis.des.sc.gov</b>."),
     k.cellp("SCDES")],
    [k.cellp("<b>Coastal critical area, beachfront</b>"),
     k.cellp("<b>des.sc.gov</b> → Programs → Bureau of Coastal Management → "
             "Critical Area Permitting, or Beachfront Management. This is the "
             "office guides still call OCRM."),
     k.cellp("SCDES")],
    [k.cellp("<b>Termite treatment regulation</b>"),
     k.cellp("The state code's added termite treatment route is enforced by "
             "the <b>Clemson University Department of Pesticide "
             "Regulation</b> (R.8-1215) — neither your building department "
             "nor a health agency."),
     k.cellp("Clemson")],
    [k.cellp("<b>Contractor license lookup</b>"),
     k.cellp("<b>llr.sc.gov</b> → Licensee Lookup. Covers both residential "
             "builders and residential specialty licensees and registrants. "
             "Use it before you pay anyone more than $500."),
     k.cellp("SC LLR")],
    [k.cellp("<b>Code editions and amendments</b>"),
     k.cellp("<b>scstatehouse.gov/coderegs/</b> → Chapter 8. Not the "
             "Building Codes Council's own Codes page, which still serves a "
             "2019 scan of the previous edition."),
     k.cellp("State")],
    [k.cellp("<b>Road access</b>"),
     k.cellp("Whoever maintains the road you are connecting to. Several "
             "counties — Pickens among them — point residents at a state "
             "encroachment permit for driveways off state-maintained roads."),
     k.cellp("Varies")],
]
flow.append(k.ref_table(
    "Nine offices that are not your building department",
    [k.cellp("", bold=True), k.cellp("What it does and how to find it",
                                     bold=True),
     k.cellp("Who", bold=True)],
    rows, [1.72 * inch, CW - 2.62 * inch, 0.90 * inch]))

flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "Three dead ends that are still in circulation", [
        Paragraph("<b>scdhec.gov serves nothing.</b> The Department of Health "
                  "and Environmental Control was split; environmental "
                  "programs went to the Department of Environmental Services "
                  "at des.sc.gov and public health to the Department of "
                  "Public Health at dph.sc.gov. The old domain was not "
                  "redirected — it simply fails. County pages at Anderson, "
                  "Oconee, York, Georgetown, Horry and Kershaw were still "
                  "linking septic guidance to it in September 2026. Pickens "
                  "and Berkeley had updated theirs.", S["body"]),
        Paragraph("<b>OCRM is a retired brand.</b> Coastal work is the Bureau "
                  "of Coastal Management inside SCDES. A guide that tells you "
                  "to file with OCRM is telling you the right thing under the "
                  "wrong name — but it also tells you how old the guide is.",
                  S["body"]),
        Paragraph("<b>laurenscounty.us is not Laurens County.</b> The legacy "
                  "domain now redirects to an unrelated commercial medical "
                  "practice. The county is at <b>laurenscountysc.gov</b>. "
                  "Several other counties have moved to .gov hosts and left "
                  "working redirects behind — Charleston, Spartanburg, York, "
                  "Florence, Sumter, Lancaster and Georgetown — but this one "
                  "did not.", S["body"]),
    ]))

# ----------------------------------------------------------- counties
flow += k.h2_tight("COUNTY BUILDING OFFICES", reserve=2.2)
flow.append(k.body(
    "Hosts and navigation, not deep links — see the note at the foot of this "
    "document for why. All confirmed September 2026."))
rows = [
    [k.cellp("<b>Aiken</b>"), k.cellp("Planning &amp; Development"),
     k.cellp("aikencountysc.gov"), k.cellp("Citizenserve")],
    [k.cellp("<b>Anderson</b>"), k.cellp("Building &amp; Codes"),
     k.cellp("andersoncountysc.org"), k.cellp("OpenGov")],
    [k.cellp("<b>Beaufort</b>"), k.cellp("Building Inspections"),
     k.cellp("beaufortcountysc.gov → Building Codes"), k.cellp("None found")],
    [k.cellp("<b>Berkeley</b>"), k.cellp("Building and Codes Enforcement"),
     k.cellp("berkeleycountysc.gov → Permitting"), k.cellp("County-run")],
    [k.cellp("<b>Charleston</b>"), k.cellp("Building Inspection Services"),
     k.cellp("charlestoncounty.gov"), k.cellp("Tyler EnerGov")],
    [k.cellp("<b>Dorchester</b>"), k.cellp("Building Services"),
     k.cellp("dorchestercountysc.gov"), k.cellp("InfoVision Evolve")],
    [k.cellp("<b>Florence</b>"), k.cellp("Planning"),
     k.cellp("florencecountysc.gov → Planning"), k.cellp("County-hosted")],
    [k.cellp("<b>Georgetown</b>"), k.cellp("Building Department"),
     k.cellp("gtcountysc.gov"), k.cellp("None found")],
    [k.cellp("<b>Greenville</b>"), k.cellp("Building Safety"),
     k.cellp("greenvillecounty.org → Building Safety"), k.cellp("eTRAKiT")],
    [k.cellp("<b>Horry</b>"), k.cellp("Code Enforcement"),
     k.cellp("horrycountysc.gov"), k.cellp("Tyler EnerGov")],
    [k.cellp("<b>Kershaw</b>"), k.cellp("Building Permits and Inspections"),
     k.cellp("kershaw.sc.gov → Planning &amp; Zoning"),
     k.cellp("None found")],
    [k.cellp("<b>Lancaster</b>"), k.cellp("Development Services"),
     k.cellp("lancastercountysc.gov"), k.cellp("InfoVision Evolve")],
    [k.cellp("<b>Laurens</b>"), k.cellp("Building Codes"),
     k.cellp("laurenscountysc.gov"), k.cellp("None found")],
    [k.cellp("<b>Lexington</b>"), k.cellp("Building Permits"),
     k.cellp("lex-co.sc.gov → Community Development"),
     k.cellp("CityView / BluePrince")],
    [k.cellp("<b>Oconee</b>"), k.cellp("Building Codes"),
     k.cellp("oconeesc.com"), k.cellp("Citizenserve")],
    [k.cellp("<b>Pickens</b>"), k.cellp("Building Codes"),
     k.cellp("co.pickens.sc.us"), k.cellp("Tyler EnerGov")],
    [k.cellp("<b>Richland</b>"),
     k.cellp("Building Permitting and Inspections"),
     k.cellp("richlandcountysc.gov"), k.cellp("eTRAKiT")],
    [k.cellp("<b>Spartanburg</b>"), k.cellp("Building Codes"),
     k.cellp("spartanburgcounty.gov"), k.cellp("Tyler EnerGov")],
    [k.cellp("<b>Sumter</b>"), k.cellp("Building Inspections"),
     k.cellp("sumtercountysc.gov"), k.cellp("None found")],
    [k.cellp("<b>York</b>"), k.cellp("Building &amp; Codes"),
     k.cellp("yorkcountysc.gov"), k.cellp("None found")],
]
flow.append(k.ref_table(
    "Twenty counties, confirmed September 2026",
    [k.cellp("County", bold=True), k.cellp("Office name", bold=True),
     k.cellp("Where to look", bold=True), k.cellp("Portal", bold=True)],
    rows, [1.25 * inch, 1.62 * inch, CW - 4.32 * inch, 1.45 * inch]))
flow.append(k.cite(
    "South Carolina has 46 counties. The twenty above are where most "
    "owner-building happens and are the ones this kit verified page by page. "
    "For any other county, search for the county name plus “building codes” "
    "and check that the host ends in a South Carolina government domain "
    "before you trust the page — several counties have live legacy hosts, and "
    "at least one legacy host now belongs to somebody else entirely."))

# -------------------------------------------------------------- cities
flow += k.h2_tight("CITIES AND TOWNS THAT ISSUE THEIR OWN PERMITS",
                   reserve=2.2)
flow.append(k.body(
    "If your lot is inside these limits, apply here and not to the county."))
rows = [
    [k.cellp("<b>Aiken</b>"), k.cellp("cityofaikensc.gov → Permitting &amp; "
                                      "Codes"), k.cellp("None evident")],
    [k.cellp("<b>Charleston</b>"), k.cellp("charleston-sc.gov → Permit "
                                           "Center"), k.cellp("Tyler EnerGov")],
    [k.cellp("<b>Columbia</b>"),
     k.cellp("columbiasc.gov → Planning and Development Services"),
     k.cellp("Tyler EnerGov")],
    [k.cellp("<b>Florence</b>"),
     k.cellp("cityofflorencesc.gov → Building Department"),
     k.cellp("None — in person or email")],
    [k.cellp("<b>Goose Creek</b>"),
     k.cellp("goosecreeksc.gov → Building Permits"), k.cellp("OpenGov")],
    [k.cellp("<b>Greenville</b>"),
     k.cellp("greenvillesc.gov → Building Permit Center"),
     k.cellp("City e-forms plus a service center")],
    [k.cellp("<b>Hilton Head Island</b>"),
     k.cellp("hiltonheadislandsc.gov → Building Permits"),
     k.cellp("Tyler EnerGov")],
    [k.cellp("<b>Mount Pleasant</b>"),
     k.cellp("tompsc.com → Building and Permit Center"), k.cellp("OPAL")],
    [k.cellp("<b>Myrtle Beach</b>"),
     k.cellp("cityofmyrtlebeach.com → Construction Services"),
     k.cellp("None — email or file share")],
    [k.cellp("<b>North Charleston</b>"),
     k.cellp("northcharleston.org → Construction and Development"),
     k.cellp("City-hosted")],
    [k.cellp("<b>North Myrtle Beach</b>"),
     k.cellp("nmb.us → Planning &amp; Development"), k.cellp("OpenGov")],
    [k.cellp("<b>Rock Hill</b>"),
     k.cellp("cityofrockhill.com → Permits &amp; Inspections"),
     k.cellp("None for permits")],
    [k.cellp("<b>Spartanburg</b>"),
     k.cellp("cityofspartanburg.org → Building Permits"),
     k.cellp("Commercial plan review only")],
    [k.cellp("<b>Summerville</b>"),
     k.cellp("summervillesc.gov → Permitting"), k.cellp("Citizenserve")],
    [k.cellp("<b>Sumter</b>"), k.cellp("sumtersc.gov → Permits"),
     k.cellp("None evident")],
]
flow.append(k.ref_table(
    "Fifteen municipalities, confirmed September 2026",
    [k.cellp("City or town", bold=True), k.cellp("Where to look", bold=True),
     k.cellp("Portal", bold=True)],
    rows, [1.55 * inch, CW - 4.05 * inch, 2.50 * inch]))
flow.append(k.cite(
    "Two cautions. <b>Rock Hill and Greenville County both publish OpenGov "
    "links that are procurement portals — bids and requests for proposals — "
    "not permit portals.</b> And the City of Sumter is a different office "
    "from Sumter County; so are the City of Charleston and Charleston County, "
    "the City of Greenville and Greenville County, the City of Spartanburg "
    "and Spartanburg County, the City of Florence and Florence County, and "
    "the City of Aiken and Aiken County. Five of South Carolina's busiest "
    "permitting relationships are city-and-county pairs sharing a name."))

# ---------------------------------------------------- owner-builder forms
flow += k.h2("WHICH OFFICES PUBLISH AN OWNER-BUILDER FORM")
flow.append(k.body(
    f"Every one of these is a local rendering of the same statute — "
    f"{sec('40-59-260')} — so if yours is not listed, ask for it by the name "
    f"the statute uses: the <b>disclosure statement</b> the permitting agency "
    f"must provide, and the <b>register-of-deeds notice</b> forms it must "
    f"hand you at the same visit. Where a jurisdiction has published one, its "
    f"own wording is worth reading, because several of them add requirements "
    f"the statute does not state."))
rows = [
    [k.cellp("<b>Greenville County</b>"),
     k.cellp("“Owner Builder Disclosure Statement.” The county requires it "
             "notarized <b>and recorded</b> before it is submitted.")],
    [k.cellp("<b>Richland County</b>"),
     k.cellp("“Statement of Disclosure.” Must be notarized and filed with the "
             "Register of Deeds. Bring a copy of the property plat.")],
    [k.cellp("<b>Charleston County</b>"),
     k.cellp("“Unlicensed Residential Builder's Disclosure Statement,” headed "
             "as an acknowledgment under § 40-59-260(E). Notarized, two "
             "witnesses, and recorded as a condition of approving the permit "
             "application. Adds “direct, on-site supervision” and bars "
             "homeowners from pulling permits for work on a manufactured "
             "home.")],
    [k.cellp("<b>Oconee County</b>"),
     k.cellp("“Owner/Builder Disclosure.” The county also publishes a “Work "
             "Exempt From Permit” list, a site plan checklist and a farm "
             "structure affidavit.")],
    [k.cellp("<b>Anderson County</b>"),
     k.cellp("An owner-builder <b>subcontractor listing</b> — the document "
             "where you name the licensed trades on your job.")],
    [k.cellp("<b>City of Columbia</b>"),
     k.cellp("“Homeowner Affidavit / Homeowner-Occupant Work Permit "
             "Certification.” States the register-of-deeds requirement and "
             "that failure to file revokes the exemption.")],
    [k.cellp("<b>Hilton Head Island</b>"),
     k.cellp("“Unlicensed Residential Builder's Disclosure Statement” — "
             "submitted to Beaufort County, not to the town.")],
    [k.cellp("<b>City of Sumter</b>"),
     k.cellp("Requires the owner/builder affidavit to be <b>recorded with the "
             "Sumter County Register of Deeds before a building permit can be "
             "obtained</b>. The form is the county's, not the city's.")],
    [k.cellp("<b>City of Aiken</b>"),
     k.cellp("A homeowners' question-and-answer page rather than a form — and "
             "the clearest published local statement that an owner may do "
             "their own building, plumbing, electrical and mechanical work on "
             "their own house, subject to the two-year rule, personal "
             "supervision, and the register-of-deeds filing.")],
    [k.cellp("<b>Kershaw County</b>"),
     k.cellp("No owner-builder form, but publishes an “Affidavit of "
             f"Construction of a Farm Structure” — the {sec('6-9-65')} filing "
             f"that has to happen <i>before</i> you build the barn.")],
]
flow.append(k.ref_table(
    "Published owner-builder documents, and what each one adds",
    [k.cellp("", bold=True), k.cellp("What they publish", bold=True)],
    rows, [1.70 * inch, CW - 1.70 * inch]))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "The online-only county and the personal-appearance statute", [
        Paragraph("Greenville County states that “All permits must be "
                  "submitted through eTrakit.” Spartanburg County's own "
                  "building permits link redirects straight into its portal. "
                  "The City of Greenville runs entirely on electronic forms.",
                  S["body"]),
        Paragraph(f"But {sec('40-59-260')}(C) says an owner claiming the "
                  "exemption “must personally appear and sign the building "
                  "permit application,” and (D) says the agency must hand you "
                  "the register-of-deeds forms when you do. <b>Do not assume "
                  "you can complete an owner-builder permit entirely online "
                  "anywhere in South Carolina.</b> Ask the office how it "
                  "reconciles its portal with the personal-appearance "
                  "requirement, and book the visit.", S["body"]),
    ]))

# ------------------------------------------------------ confirmed page
flow += k.h2_tight("OFFICES I CONFIRMED", reserve=2.0)
flow.append(k.body(
    "Fill this in as you go. It is the page worth having on the job when "
    "somebody asks who approved what."))
flow += k.check_table(
    "My offices",
    [
        ("Building department — jurisdiction and office name",
         [("Office", 1.0)]),
        ("Confirmed my parcel is inside / outside municipal limits",
         [("Which", 1.0)]),
        ("Portal name and my account set up", [("Portal", 1.0)]),
        ("Register of deeds — and whether the notice records before the "
         "permit or after completion", [("Which", 1.0)]),
        ("Clerk of court, if the Notice of Project Commencement goes there",
         [("Office", 1.0)]),
        ("Zoning contact and the setbacks confirmed for this parcel",
         [("Front / side / rear", 1.0)]),
        ("Septic — SCDES office or authorized agent handling my application",
         [("Contact", 1.0)]),
        ("Well — SCDES bureau contact, if drilling", [("Contact", 1.0)]),
        ("Coastal critical area or beachfront — needed? who confirmed?",
         [("Yes / No", 0.4), ("Confirmed by", 0.6)]),
        ("Road authority for my driveway connection", [("Authority", 1.0)]),
        ("Stormwater or land disturbance contact, if disturbing one acre "
         "or more", [("Contact", 1.0)]),
        ("Utility providers — power, water, gas — and what each needs before "
         "connection", [("Providers", 1.0)]),
        ("Termite treatment provider and who issues the record",
         [("Provider", 1.0)]),
    ], notes_header="Confirmed", date_w=0.85, notes_w=1.35)

# -------------------------------------------------------------- sources
flow += k.h2_tight("SOURCES", reserve=2.0)
flow.append(k.sources_table([
    ("Enforcement is mandatory in every municipality and county; each county "
     "must place its unincorporated area under a building official",
     f"S.C. Code Ann. {sec('6-9-10')}(A), {sec('6-9-30')}(A)"),
    ("The financial-hardship affidavit that exempts a jurisdiction from the "
     "chapter", f"S.C. Code Ann. {sec('6-9-30')}(B)"),
    ("The register-of-deeds notice, the disclosure statement, and the "
     "agency's duty to hand over the forms",
     f"S.C. Code Ann. {sec('40-59-260')}(C), (D), (E)"),
    ("Notice of Project Commencement goes to the clerk of court or the "
     "register of deeds", f"S.C. Code Ann. {sec('29-5-23')}"),
    ("Farm structure affidavit must be filed before construction",
     f"S.C. Code Ann. {sec('6-9-65')}"),
    ("Termite treatment route enforced by the Clemson University Department "
     "of Pesticide Regulation", "S.C. Code of Regs. 8-1215"),
    ("Septic, private wells, and coastal critical area and beachfront "
     "authorization", "SCDES, des.sc.gov"),
    ("Contractor and specialty credential lookup", "SC LLR, llr.sc.gov"),
    ("Every county and city office named here", "Fetched September 2026"),
]))
flow.append(k.closing_note(
    "This directory prints hosts and navigation paths instead of deep links "
    "on purpose. South Carolina counties have moved hosts in numbers — "
    "charlestoncounty.org, spartanburgcounty.org, yorkcountygov.com, "
    "florenceco.org, sumtercountysc.org, mylancastersc.org and gtcounty.org "
    "have all been superseded — and the numeric page identifiers many county "
    "sites use are recycled between departments, so a printed link can "
    "quietly land on the wrong office. A host plus a menu path survives both. "
    "Everything here was fetched and content-confirmed in September 2026; "
    "confirm anything that matters with the office itself."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "sc-permit-kit",
                       "SC.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
