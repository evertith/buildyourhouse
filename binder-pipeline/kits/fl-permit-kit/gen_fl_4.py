#!/usr/bin/env python3
"""FL.4 Where to File Directory.

Deliberate design decision, and the reason this document does not look like
the other states' directories: IT PRINTS NO DEEP LINKS TO COUNTY BUILDING
DEPARTMENTS.

Every candidate county permitting URL was curl-verified while building this
kit. Of thirty deep links tested, eleven were dead or redirected to an
unrelated page, and several county sites (Brevard, Sarasota, Marion, Clay,
St. Lucie) refuse automated requests outright, so their content could not be
confirmed at all. Worse, the CivicPlus-style numeric URLs that several
counties use — /168/Building-Inspections — silently resolve to whatever page
now holds that ID: one tested link for a building department resolved to a
stormwater master plan, and another to a flood-hazard page. A printed table of
those links would be wrong on arrival for a third of the state and, worse,
confidently wrong.

What IS durable, and is what this document prints instead:
  - the county's own root domain, verified to respond;
  - the statewide agencies, whose URLs are institutional and stable;
  - the METHOD for establishing which of Florida's 400+ municipalities or 67
    counties actually has jurisdiction over the parcel, which is the question
    a directory cannot answer anyway.

The sequencing map at the top is the real content: s. 381.0065(4), Fla. Stat.
makes the septic construction permit a prerequisite to the building permit, so
for a rural Florida owner-builder the building department is not the first
office to visit.
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

FORM_ID = "FL.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Ask"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "Which government has your parcel, which office comes "
                 "first, and a page to record what you confirmed.")
flow.append(k.disclaimer())

# ------------------------------------------------------------- jurisdiction
flow += k.h2("FIRST: WHICH GOVERNMENT IS ACTUALLY YOURS?")
flow.append(k.body(
    "Florida has 67&nbsp;counties and more than 400 municipalities, and a great "
    "many cities run their own building departments entirely separately from "
    "the surrounding county. A parcel with an Orlando mailing address may be "
    "permitted by the City of Orlando, or by Orange County, and the mailing "
    "address will not tell you which. The construction lien statute assumes "
    "this: it applies to “every municipality and county in the state "
    "which now has or hereafter may have a system of issuing building "
    "permits” (s. 713.135(8), Fla. Stat.)."))
flow.append(k.callout(
    "The reliable way to settle it", [
        Paragraph("Look your parcel up on the <b>county property "
                  "appraiser's</b> parcel search. Every Florida county has "
                  "one, it is free, and the record shows the parcel's taxing "
                  "authorities and whether it sits inside a municipality. "
                  "That answer — not the mailing address, not the ZIP code — "
                  "tells you whose building department you are dealing with. "
                  "Search for your county's name plus “property "
                  "appraiser.” Then confirm by asking the department "
                  "itself before you file anything.", S["body"]),
    ]))

# ---------------------------------------------------------------- sequence
flow += k.h2("SECOND: THE ORDER THESE OFFICES COME IN")
flow.append(k.body(
    "On a rural Florida lot the building department is <b>not</b> the first "
    "office you visit. Two approvals are prerequisites to the building "
    "permit itself, so filing in the wrong order costs you months."))
rows = [
    [k.cellp("<b>1</b>"), k.cellp("<b>Septic construction permit</b>"),
     k.cellp("If the lot is on septic, no building or plumbing permit may "
             "issue without it. The site evaluation behind it has to be "
             "performed by a qualified professional and is valid for the "
             "life of the permit — start here."),
     k.cellp("s. 381.0065(4)")],
    [k.cellp("<b>2</b>"), k.cellp("<b>Well construction permit</b>"),
     k.cellp("From your water management district, if you are not on a "
             "public water system. Separate program, separate office from "
             "septic — do not assume one visit covers both."),
     k.cellp("Rule 62-532.400")],
    [k.cellp("<b>3</b>"),
     k.cellp("<b>CCCL permit, if you are seaward of the line</b>"),
     k.cellp("A separate state permit from the Department of Environmental "
             "Protection, independent of your building permit. Check the "
             "line before you buy, not after."),
     k.cellp("s. 161.053")],
    [k.cellp("<b>4</b>"), k.cellp("<b>Zoning and access</b>"),
     k.cellp("Zoning or land-use verification, address assignment, and a "
             "driveway or access permit — from the county, or from the "
             "Department of Transportation if you connect to a state road."),
     k.cellp("local; s. 335.182")],
    [k.cellp("<b>5</b>"), k.cellp("<b>Building permit</b>"),
     k.cellp("With the owner appearing in person to sign, the disclosure "
             "statement, and the product approval schedule (FL.1, FL.2)."),
     k.cellp("s. 489.103(7)(c)")],
    [k.cellp("<b>6</b>"), k.cellp("<b>Notice of Commencement</b>"),
     k.cellp("Recorded at the clerk of the circuit court before work "
             "starts, posted at the site, copy filed with the building "
             "department before the first inspection (FL.3)."),
     k.cellp("ss. 713.13, 713.135")],
]
flow.append(k.ref_table(
    "The filing order on a rural lot",
    [k.cellp("", bold=True), k.cellp("Office / approval", bold=True),
     k.cellp("Why it sits here", bold=True), k.cellp("Cite", bold=True)],
    rows, [0.34 * inch, 1.70 * inch, CW - 3.34 * inch, 1.30 * inch]))

# ------------------------------------------------------------------ septic
flow += k.h2("SEPTIC: THE ONE ANSWER THAT CHANGED, AND IS STILL CHANGING")
flow.append(k.body(
    "Almost every Florida guide in print says the <b>Department of Health</b> "
    "regulates septic systems. That has not been true since the Clean "
    "Waterways Act moved the onsite sewage program to the <b>Department of "
    "Environmental Protection</b>, effective 1 July 2021 (ch. 2020-150, Laws "
    "of Florida). But the correction most people then make is also wrong, "
    "because the transfer is being implemented <b>county by county</b> and is "
    "not finished."))
flow.append(k.callout_long(
    "Where you actually file, as of September 2026", [
        Paragraph("<b>In these 17&nbsp;counties, the Department of Environmental "
                  "Protection issues the permit directly:</b> Bay, Calhoun, "
                  "Escambia, Franklin, Gadsden, Gulf, Holmes, Jackson, "
                  "Jefferson, Leon, Liberty, Marion, Okaloosa, Santa Rosa, "
                  "Wakulla, Walton and Washington.", S["body"]),
        Paragraph("<b>In the other 50&nbsp;counties — which is every major metro, "
                  "including Miami-Dade, Broward, Palm Beach, Orange, "
                  "Hillsborough and Duval — you file with the Environmental "
                  "Health program of your local county health department</b>, "
                  "which administers the program under the Department of "
                  "Environmental Protection's direction.", S["body"]),
        Paragraph("The Department's own statement is that transition of the "
                  "remaining counties “will occur depending on "
                  "legislative approval,” with no published schedule. So "
                  "<b>check the list before you file</b>: "
                  "floridadep.gov/water/onsite-sewage, then the permitting "
                  "FAQ. Your county may have moved since this kit was "
                  "printed.", S["body"]),
    ]))
flow.append(Spacer(1, 2))
flow.append(k.body(
    "Two more things worth knowing before you call. The rule chapter was "
    "renumbered in the same move, from <b>64E-6</b> to <b>62-6, F.A.C.</b> — "
    "county forms, contractor paperwork and older articles still say 64E-6, "
    "and they mean the same rules. And you <b>may install your own septic "
    "system</b>: a property owner “who personally performs "
    "construction, maintenance, or repairs to a system serving his or her own "
    "owner-occupied single-family residence is exempt from registration "
    "requirements… but is subject to all permitting requirements” "
    "(s. 381.0065(4), Fla. Stat.). Note the limits — personally, own, "
    "owner-occupied, single-family — and note that the <b>site evaluation for "
    "a new system still cannot be self-performed</b>: it takes a Florida "
    "licensed engineer with soils training, department personnel, a Master "
    "Septic Tank Contractor, a certified professional soil scientist, or a "
    "person certified under s. 381.0101."))

# ------------------------------------------------------------------- wells
flow += k.h2_tight("WELLS: THE FIVE WATER MANAGEMENT DISTRICTS", reserve=2.2)
rows = [
    [k.cellp("<b>Northwest Florida</b>"),
     k.cellp("The 16 westernmost counties: Bay, Calhoun, Escambia, Franklin, "
             "Gadsden, Gulf, Holmes, Jackson, Leon, Liberty, Okaloosa, Santa "
             "Rosa, Wakulla, Walton, Washington and western Jefferson"),
     k.cellp("nwfwater.com<br/>Rule 40A-3")],
    [k.cellp("<b>Suwannee River</b>"),
     k.cellp("North-central Florida, the Suwannee River basin. Check the "
             "district's own map for your county"),
     k.cellp("srwmd.org<br/>Rule 40B-3")],
    [k.cellp("<b>St. Johns River</b>"),
     k.cellp("18&nbsp;counties in northeast and east-central Florida. Check the "
             "district's own map for your county"),
     k.cellp("sjrwmd.com<br/>Rule 40C-3")],
    [k.cellp("<b>Southwest Florida</b>"),
     k.cellp("West-central Florida, the Tampa Bay region and inland. Check "
             "the district's own map for your county"),
     k.cellp("swfwmd.state.fl.us<br/>Rule 40D-3")],
    [k.cellp("<b>South Florida</b>"),
     k.cellp("Broward, Collier, Glades, Hendry, Lee, Martin, Miami-Dade, "
             "Monroe, Palm Beach and St. Lucie entirely, plus parts of "
             "Charlotte, Highlands, Okeechobee, Orange, Osceola and Polk"),
     k.cellp("sfwmd.gov<br/>Rule 40E-3")],
]
flow.append(k.ref_table(
    "Who issues your well permit",
    [k.cellp("District", bold=True), k.cellp("Coverage", bold=True),
     k.cellp("Where / rule", bold=True)],
    rows, [1.35 * inch, CW - 3.20 * inch, 1.85 * inch]))
flow.append(k.cite(
    "County lists are as published by the districts themselves. Two districts "
    "do not publish a plain county list on their landing pages, so this kit "
    "does not invent one — use the district's map tool. A permit is required "
    "before construction, repair or abandonment of any water well, and the "
    "application may be made by the owner or by the well contractor on the "
    "owner's behalf (Rule 62-532.400(1), F.A.C.)."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "Can you drill your own well? Almost certainly not the one you want", [
        Paragraph("There is a real exemption, and it is narrower than it "
                  "sounds. Section 373.326(2), Fla. Stat. lets an unlicensed "
                  "person construct “a well that is 2&nbsp;inches or under in "
                  "diameter, on the person's own or leased property, intended "
                  "for use only in a single-family house which is his or her "
                  "residence.” Two inches or under is a driven "
                  "well point — not the four- to six-inch cased well with a "
                  "submersible pump that a modern household water supply "
                  "needs. For that you will hire a licensed water well "
                  "contractor. And the exemption is from the "
                  "<i>contractor license</i> only: the district permit is "
                  "still required either way.", S["body"]),
    ]))

# ------------------------------------------------------------- state offices
flow += k.h2_tight("THE STATEWIDE OFFICES AND LOOKUPS", reserve=2.2)
rows = [
    [k.cellp("Verify a contractor's license"),
     k.cellp("Dept. of Business and Professional Regulation"),
     k.cellp("myfloridalicense.com")],
    [k.cellp("Look up a product's FL approval number"),
     k.cellp("Florida Building Commission product search"),
     k.cellp("floridabuilding.org/pr/pr_app_srch.aspx")],
    [k.cellp("Read the building code, free"),
     k.cellp("Florida Building Commission"),
     k.cellp("floridabuilding.org")],
    [k.cellp("Your design wind speed"),
     k.cellp("ASCE 7 Hazard Tool"),
     k.cellp("ascehazardtool.org")],
    [k.cellp("Septic permitting, and which office has your county"),
     k.cellp("Dept. of Environmental Protection, Onsite Sewage Program"),
     k.cellp("floridadep.gov/water/onsite-sewage")],
    [k.cellp("Your county health department (septic, in 50&nbsp;counties)"),
     k.cellp("Florida Department of Health"),
     k.cellp("floridahealth.gov/all-county-locations.html")],
    [k.cellp("Coastal construction control line permit and map"),
     k.cellp("Dept. of Environmental Protection"),
     k.cellp("floridadep.gov/rcp/coastal-construction-control-line")],
    [k.cellp("Your flood zone and base flood elevation"),
     k.cellp("FEMA Map Service Center"),
     k.cellp("msc.fema.gov")],
    [k.cellp("Record the Notice of Commencement"),
     k.cellp("Clerk of the circuit court, your county"),
     k.cellp("search your county plus “clerk of court official "
             "records”")],
    [k.cellp("Read a statute cited in this kit"),
     k.cellp("The Florida Senate"),
     k.cellp("flsenate.gov/Laws/Statutes")],
    [k.cellp("Read a rule cited in this kit"),
     k.cellp("Florida Administrative Code"),
     k.cellp("flrules.org")],
]
flow.append(k.ref_table(
    "Every statewide lookup this kit refers to",
    [k.cellp("What you need", bold=True), k.cellp("Who has it", bold=True),
     k.cellp("Where", bold=True)],
    rows, [2.05 * inch, 2.10 * inch, CW - 4.15 * inch]))
flow.append(k.cite(
    "Every address above returned a live page in September 2026. This kit "
    "prints no phone numbers: they change faster than anything else on a "
    "government page, and every office above can be reached from its own "
    "site."))

# ---------------------------------------------------------------- counties
flow += k.h2("COUNTY BUILDING DEPARTMENTS")
flow.append(k.body(
    "A note on what this page does and does not give you. Deep links into "
    "county permitting pages are the least durable thing a printed kit can "
    "carry — when the addresses below were tested, roughly a third of the "
    "obvious permitting URLs were dead or silently redirected to an unrelated "
    "page, because several counties use numeric page addresses that get "
    "reassigned. So this kit prints each county's <b>main site</b>, which is "
    "stable, and leaves you one search away from a current permitting page. "
    "Search the county site for “building permit.”"))
counties = [
    ("Alachua", "alachuacounty.us"), ("Bay", "baycountyfl.gov"),
    ("Brevard", "brevardfl.gov"), ("Broward *", "broward.org"),
    ("Charlotte", "charlottecountyfl.gov"), ("Citrus", "citruscounty.gov"),
    ("Clay", "claycountygov.com"), ("Collier", "collier.gov"),
    ("Duval / Jacksonville", "jacksonville.gov"),
    ("Escambia", "myescambia.com"), ("Hernando", "hernandocounty.us"),
    ("Hillsborough", "hcfl.gov"), ("Lake", "lakecountyfl.gov"),
    ("Lee", "leegov.com"), ("Leon", "leoncountyfl.gov"),
    ("Manatee", "mymanatee.org"), ("Marion", "marionfl.org"),
    ("Martin", "martin.fl.us"), ("Miami-Dade *", "miamidade.gov"),
    ("Monroe", "monroecounty-fl.gov"), ("Okaloosa", "myokaloosa.com"),
    ("Orange", "orangecountyfl.net"), ("Osceola", "osceola.org"),
    ("Palm Beach", "discover.pbc.gov"), ("Pasco", "pascocountyfl.gov"),
    ("Pinellas", "pinellas.gov"), ("Polk", "polkfl.gov"),
    ("St. Johns", "sjcfl.us"), ("St. Lucie", "stlucieco.gov"),
    ("Santa Rosa", "santarosa.fl.gov"), ("Sarasota", "scgov.net"),
    ("Seminole", "seminolecountyfl.gov"), ("Volusia", "volusia.org"),
]
half = (len(counties) + 1) // 2
rows = []
for i in range(half):
    a = counties[i]
    b = counties[i + half] if i + half < len(counties) else ("", "")
    rows.append([k.cellp(a[0]), k.cellp(a[1]),
                 k.cellp(b[0]), k.cellp(b[1])])
col = (CW - 0.0) / 4
flow.append(k.ref_table(
    "County main sites — search each for “building permit”",
    [k.cellp("County", bold=True), k.cellp("Website", bold=True),
     k.cellp("County", bold=True), k.cellp("Website", bold=True)],
    rows, [1.25 * inch, CW / 2 - 1.25 * inch,
           1.25 * inch, CW / 2 - 1.25 * inch]))
flow.append(k.cite(
    "* Broward and Miami-Dade are the High-Velocity Hurricane Zone — expect "
    "the Miami-Dade Notice of Acceptance vocabulary and the HVHZ Uniform "
    "Permit Application there (FL.2). Each address above responded when "
    "tested in September 2026. If your parcel is inside a city, the city's "
    "own building department may be the one that permits it — settle that "
    "first, using the property appraiser."))

# ------------------------------------------------------------------ record
flow += k.h2_tight("WHAT I CONFIRMED", reserve=2.0)
flow.append(k.body(
    "Fill this in as you confirm each office. The point of the page is that "
    "you spoke to somebody and wrote down what they said, with a date — which "
    "is worth more than any printed directory when a question comes up eight "
    "months from now."))
flow += k.check_table(
    "My offices",
    [("<b>Building department</b> — county or city?",
      [("Office:", 0.55), ("Confirmed:", 0.45)]),
     ("", [("Portal / address:", 0.6), ("Spoke with:", 0.4)]),
     ("<b>Septic</b> — DEP directly, or county health department?",
      [("Office:", 0.55), ("Confirmed:", 0.45)]),
     ("", [("Permit no.:", 0.6), ("Spoke with:", 0.4)]),
     ("<b>Well</b> — water management district",
      [("District:", 0.55), ("Confirmed:", 0.45)]),
     ("<b>Clerk of court</b> — for recording the Notice of Commencement",
      [("Office:", 0.55), ("Confirmed:", 0.45)]),
     ("<b>Floodplain administrator</b> — flood zone, BFE, freeboard, "
      "elevation certificate checkpoints",
      [("Zone:", 0.3), ("BFE:", 0.3), ("Confirmed:", 0.4)]),
     ("<b>Zoning</b> — setbacks, land use, address assignment",
      [("Office:", 0.55), ("Confirmed:", 0.45)]),
     ("<b>Driveway / access</b> — county road or state road?",
      [("Office:", 0.55), ("Confirmed:", 0.45)]),
     ("<b>Utility</b> — power, and water if not on a well",
      [("Office:", 0.55), ("Confirmed:", 0.45)]),
     ("<b>CCCL</b> — only if seaward of the coastal construction control "
      "line", [("Confirmed:", 1.0)]),
     ],
    notes_header="Notes / what they told me")

# ----------------------------------------------------------------- sources
flow += k.h2_tight("SOURCES", reserve=2.0)
flow.append(k.sources_table([
    ("Counties and municipalities both issue building permits in Florida",
     "s. 713.135(8)"),
    ("A septic construction permit is a prerequisite to the building or "
     "plumbing permit, and final installation approval a prerequisite to "
     "occupancy", "s. 381.0065(4)"),
    ("The onsite sewage program transferred from the Department of Health to "
     "the Department of Environmental Protection effective 1 July 2021",
     "ch. 2020-150, Laws of Florida"),
    ("The transfer is phased; DEP issues directly in 17&nbsp;counties and county "
     "health departments administer the rest",
     "Dept. of Environmental Protection, onsite sewage permitting FAQ"),
    ("Rule chapter 62-6, F.A.C., formerly 64E-6",
     "Rule 62-6, F.A.C., history notes"),
    ("An owner personally performing work on their own owner-occupied "
     "single-family residence is exempt from septic contractor registration "
     "but not from permitting", "s. 381.0065(4)"),
    ("The site evaluation for a new system must be performed by one of five "
     "named qualified persons", "Rule 62-6.004(3), F.A.C."),
    ("A permit is required before constructing, repairing or abandoning a "
     "water well, applied for by the owner or the contractor",
     "Rule 62-532.400(1), F.A.C."),
    ("Water well contractors are licensed by the water management districts",
     "s. 373.323"),
    ("An owner may construct a well 2&nbsp;inches or under in diameter on their "
     "own property for their own single-family residence without a "
     "contractor license", "s. 373.326(2)"),
    ("A separate Department of Environmental Protection permit is required "
     "to construct seaward of the coastal construction control line",
     "s. 161.053; Rule 62B-33, F.A.C."),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "fl-permit-kit",
                       "FL.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
