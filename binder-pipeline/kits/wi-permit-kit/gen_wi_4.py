#!/usr/bin/env python3
"""WI.4 Where to File Directory.

Verified sources:
  DSPS "UDC Delegated Municipalities List", dated 19 August 2026 — 1,771 rows
  DSPS "UDC and Camping Unit Programs Permitting and Inspection Map", R.4/2/2026
  145.01(5)            the sanitary-permit authority is THE COUNTY, except in a
                       county of 750,000 or more (Milwaukee) where it is the
                       city, village or town
  59.70(5)(a)          every responsible governmental unit shall enact a POWTS
                       ordinance covering its entire area; no other municipality
                       may enact or enforce one
  145.20(1)(a)         the county may park the POWTS program in ANY office —
                       which is why the office name varies statewide
  145.19(1r)           the county holds prior soil test results and must accept
                       them unless the soil has been altered
  281.34(3)(a)         WELL NOTIFICATION to DNR is required BEFORE construction
  NR 812.10(1)(a)      an owner MAY drill their own well on their own land
  NR 812.10(8),(11)    the driller verifies the notification; the construction
                       report is filed within 30 days, electronically
  NR 812.08 Table A    the well separation distances — reproduced in full
  NR 812.08(1),(4)     highest point on the property; distances measured to the
                       source and NOT waived at a property line
  SPS 383.43 Table 383.43-1  the POWTS horizontal setbacks
  86.07(2)(a)          driveway permit from the authority that MAINTAINS the
                       road; Trans 231.05 for the residential driveway spec
  59.692(1c),(1)(b)    counties shall zone all shorelands; 1,000 ft / 300 ft
  NR 115.05(1)         75-foot setback, 35-foot buffer, 15% impervious, lot
                       sizes
  NR 116.03(20),(41)   flood protection elevation = regional flood + 2&nbsp;feet
  NR 116.12(1)         no house, no septic and no well in a floodway
  NR 216.42, .44       one acre; notice of intent 14 working days ahead

Deliberately NOT printed: phone numbers, staff names, county fees, and any
county-by-county addressing table. The addressing office moves between
departments after a reorganization and could not be verified across a
representative sample.
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

FORM_ID = "WI.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Offices, Setbacks & Lookups"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "How to find out who inspects your parcel, which office issues what, and "
    "the separation distances that decide where the house can actually go.")

flow.append(k.disclaimer(
    "No phone numbers are printed anywhere in this kit — they go stale faster "
    "than anything else. Office names and web addresses are given instead."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- lookup
flow += k.h2_tight("HOW TO FIND OUT WHO INSPECTS YOUR PARCEL")
flow.append(k.body(
    "This is the single most useful procedure in the Wisconsin kit, and almost "
    "nobody outside the trade knows the two documents it depends on. The "
    "department publishes both, free, and together they resolve any parcel in "
    "the state."))
flow.append(k.body(
    "<b>Start with the right jurisdiction.</b> In rural Wisconsin your "
    "jurisdiction is almost always a <b>Town</b> — “Town of Grant, Portage "
    "County” — and it is <i>not</i> the city on your mailing address. Get the "
    "exact entity from the county land-records or parcel viewer, or from the "
    "legal description on the deed, before you look anything up."))
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp("<b>UDC Delegated Municipalities List</b><br/>"
             "<font size=8>dsps.wi.gov → Programs → Delegated Agent → "
             "UDCDelegatedMuni.pdf</font>"),
     k.cellp("Search it for your exact municipality. If it is listed, "
             "<b>that municipality issues your permit and does your "
             "inspections</b>, and the list names the municipal contact and "
             "the inspector currently under contract")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("<b>UDC Permit and Inspection Map</b><br/>"
             "<font size=8>dsps.wi.gov → Programs → Maps → "
             "UDCPermitInspectionMap.pdf</font>"),
     k.cellp("If your municipality is <i>not</i> on the list, find your county "
             "on this one-page color map. It tells you whether to contact the "
             "county, the department, or a named private inspection agency")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("<b>Whoever that turns out to be, use them for everything</b>"),
     k.cellp("“<i>A person who obtains a Wisconsin uniform building permit "
             "from a registered UDC inspection agency shall retain the same "
             "agency to conduct the inspections for the project.</i>” "
             "(s. SPS 320.08(2))")],
]
flow.append(k.ref_table(
    "The three-step lookup",
    [k.cellp("", bold=True), k.cellp("Document", bold=True),
     k.cellp("What it tells you", bold=True)],
    rows, [0.32 * inch, 2.35 * inch, CW - 2.67 * inch]))
flow.append(k.cite(
    "The list carried 1,771 numbered rows when read for this edition (dated "
    "19 August 2026) and states: “<i>Contact the municipalities listed below "
    "for one- and two-family dwelling and camping unit construction and "
    "inspections. For projects within municipalities not listed below, contact "
    "the inspection agency responsible for your area.</i>” The map was revised "
    "2 April 2026 and is headed “<i>Who is my contact for permitting and "
    "inspection services?</i>” Both are updated periodically — pull the "
    "current versions rather than relying on a number printed here."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long("Two things on those documents that mislead people",
                           [
    Paragraph("<b>“Opt-Out” does not mean “no permits here.”</b> The "
              "delegation column that shows Delegated or Opt-Out on the "
              "municipalities list refers to <b>camping units</b> under "
              "ch. SPS 327, not to the Uniform Dwelling Code. A county can "
              "show Opt-Out there and still hold full UDC delegation. Do not "
              "read it as an absence of building permits.", S["body"]),
    Paragraph("<b>One county is split down the middle.</b> On the inspection "
              "map, <b>Clark County</b> is divided — the northern part and the "
              "southern part fall to two different contracted agencies. If "
              "your parcel is in Clark County you have to know which half you "
              "are in before you call anyone.", S["body"]),
    Paragraph("<b>Thirteen counties hold UDC delegation</b> and issue permits "
              "for the cities, villages and towns within them that have no "
              "delegation of their own: <b>Adams, Bayfield, Buffalo, Chippewa, "
              "Eau Claire, Florence, Forest, Langlade, Marquette, Richland, "
              "Trempealeau, Waupaca and Waushara</b>. Everywhere else that is "
              "not a delegated municipality, the contact is the department or "
              "one of its contracted agencies.", S["body"]),
    Paragraph("<b>And there is no gap.</b> The department's own program page "
              "states that “<i>the UDC is enforced in all Wisconsin "
              "municipalities</i>”, and its owner brochure adds the sentence "
              "that matters most: “<i>Regardless of permit requirements, state "
              "statutes require compliance with the UDC rules by owners and "
              "builders even if there is no enforcement.</i>”", S["body"]),
]))

# ---------------------------------------------------------------- offices
flow += k.h2_tight("WHICH OFFICE ISSUES WHAT", reserve=2.0)
rows = [
    [k.cellp("<b>Building permit</b> (UDC), including erosion control"),
     k.cellp("Your municipality, your county if it holds delegation, the "
             "department, or a contracted UDC inspection agency — use the "
             "lookup above"),
     k.cellp("s. SPS 320.08(1)")],
    [k.cellp("<b>Sanitary permit</b> (POWTS / septic)"),
     k.cellp("<b>The county</b>, statewide — except in a county of 750,000 or "
             "more people, where it is the city, village or town"),
     k.cellp("Wis. Stat. s. 145.01(5)")],
    [k.cellp("<b>Soil and site evaluation</b>"),
     k.cellp("A state-certified soil tester; the report is filed with the "
             "county"),
     k.cellp("s. SPS 385.40(1)")],
    [k.cellp("<b>Well notification</b>, before drilling"),
     k.cellp("Department of Natural Resources — the owner or the constructor "
             "may obtain the number"),
     k.cellp("Wis. Stat. s. 281.34(3)(a)")],
    [k.cellp("<b>Well construction report</b>, after drilling"),
     k.cellp("Filed by the driller with the department and with you, within "
             "30 days, electronically"),
     k.cellp("s. NR 812.10(11)")],
    [k.cellp("<b>Zoning / land use permit</b>"),
     k.cellp("County zoning in unincorporated towns; otherwise the town, "
             "village or city"),
     k.cellp("Wis. Stat. s. 59.69")],
    [k.cellp("<b>Shoreland zoning</b>"),
     k.cellp("<b>The county</b> — every county must zone all shorelands in "
             "its unincorporated area"),
     k.cellp("Wis. Stat. s. 59.692(1c)")],
    [k.cellp("<b>Floodplain zoning</b>"),
     k.cellp("The county in unincorporated territory; the city or village "
             "inside one"),
     k.cellp("s. NR 116.02")],
    [k.cellp("<b>Driveway / access permit</b>"),
     k.cellp("Whichever authority <b>maintains</b> the road you are cutting "
             "into — the town board, the county highway department, or the "
             "Department of Transportation"),
     k.cellp("Wis. Stat. s. 86.07(2)(a)")],
    [k.cellp("<b>Construction site stormwater</b>, one acre or more"),
     k.cellp("Department of Natural Resources, by notice of intent"),
     k.cellp("s. NR 216.42(1)")],
]
flow.append(k.ref_table(
    "The full permit stack for a rural Wisconsin build",
    [k.cellp("Filing", bold=True), k.cellp("Who issues it", bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.75 * inch, CW - 3.5 * inch, 1.75 * inch]))

flow.append(Spacer(1, 4))
flow.append(k.body(
    "<b>Why the county office has a different name in every county.</b> The "
    "statute lets each county put the septic program wherever it likes: the "
    "governing body “<i>may assign the duties of administering the private "
    "on-site wastewater treatment system program to any office, department, "
    "committee, board, commission, position or employee</i>” "
    "(Wis. Stat. s. 145.20(1)(a)). So you will find it under Planning and "
    "Zoning, Land Conservation, Land and Water Conservation, Land Services, "
    "Land Information, Community Development, Environmental Health, Public "
    "Health, or a standalone Sanitarian. <b>Search your county's site for the "
    "words “sanitary permit”, not for a department name.</b>"))
flow.append(k.callout(
    "Two things to ask the county before you spend money", [
        Paragraph("<b>1. Is there already a soil test on this parcel?</b> "
                  "“<i>The results of any percolation test or other test … "
                  "shall be retained by the governmental unit where the "
                  "property is located. The governmental unit shall make the "
                  "test results available to an applicant … and shall accept "
                  "the test results as the basis for a sanitary permit "
                  "application unless the soil at the test site is "
                  "altered.</i>” (Wis. Stat. s. 145.19(1r)) A previous owner "
                  "may already have paid for your soil evaluation.",
                  S["body"]),
        Paragraph("<b>2. Does the county run a delegated well program?</b> "
                  "A county authorized under Wis. Stat. s. 59.70(6)(b) and "
                  "ch. NR 845 “<i>may require that a permit be obtained</i>” "
                  "before a private well is constructed. The state "
                  "notification is not always the only step.", S["body"]),
    ]))

# ---------------------------------------------------------------- well
flow += k.h2_tight("THE WELL — YOU MAY DRILL IT YOURSELF", reserve=2.0)
flow.append(k.body(
    "This is the mirror image of the septic answer. Wisconsin does <b>not</b> "
    "require a license to drill a well on your own land: an individual "
    "constructing a well must be a licensed water well driller “<i>except that "
    "a license is not required for … an individual performing well drilling on "
    "real estate owned or leased by that individual</i>” "
    "(s. NR 812.10(1)(a)). Every construction standard in ch. NR 812 still "
    "applies to the well you drill — the exemption is from the credential, not "
    "from the code."))
flow.append(k.body(
    "But there <b>is</b> a filing before the rig arrives, and it is your job, "
    "not the driller's: “<i>An owner shall notify the department of the "
    "location of a well that is not a high capacity well <b>before "
    "construction of the well begins</b></i>” (Wis. Stat. s. 281.34(3)(a)). "
    "The driller must then confirm it exists — they “<i>shall either obtain a "
    "well notification or verify that the well owner has obtained a department "
    "well notification including the notification number … before the well "
    "construction operation is started</i>” (s. NR 812.10(8)). Afterwards the "
    "driller files a well construction report with the department and with you "
    "within 30 days (s. NR 812.10(11)). <b>Keep your copy.</b> It is the only "
    "permanent record of casing depth, static level, yield and geology, and "
    "buyers and lenders ask for it years later."))
flow.append(k.callout(
    "Look at the neighbors' wells before you buy the land", [
        Paragraph("Because every well construction report since the system "
                  "went electronic is public, you can search the wells around "
                  "a parcel and see what depth, what geology and what yield "
                  "the drillers actually found — before you make an offer. "
                  "The public search is the Well Construction Information "
                  "System at <b>apps.dnr.wi.gov</b>. On a rural parcel this is "
                  "the cheapest due diligence available to you.", S["body"]),
    ]))

rows = [
    [k.cellp("Unconsolidated (sand and gravel)"),
     k.cellp("2&nbsp;inches", center=True),
     k.cellp("<b>25&nbsp;feet</b>, or 10&nbsp;feet below the static water level when "
             "that level is more than 15&nbsp;feet down")],
    [k.cellp("Sandstone bedrock"), k.cellp("6&nbsp;inches", center=True),
     k.cellp("<b>30&nbsp;feet</b>")],
    [k.cellp("Crystalline igneous or metamorphic bedrock"),
     k.cellp("6&nbsp;inches", center=True), k.cellp("<b>40&nbsp;feet</b>")],
    [k.cellp("Limestone or dolomite, top 20&nbsp;feet or more down"),
     k.cellp("6&nbsp;inches", center=True), k.cellp("<b>40&nbsp;feet</b>")],
    [k.cellp("Limestone or dolomite, top less than 20&nbsp;feet down"),
     k.cellp("6&nbsp;inches", center=True), k.cellp("<b>60&nbsp;feet</b>")],
]
flow.append(k.ref_table(
    "Minimum casing, by formation (ss. NR 812.13, 812.14)",
    [k.cellp("Formation", bold=True), k.cellp("Min. diameter", bold=True),
     k.cellp("Minimum casing depth", bold=True)],
    rows, [CW - 4.15 * inch, 1.05 * inch, 3.1 * inch]))
flow.append(k.cite(
    "These are minimums; greater depth is required in special well casing "
    "depth areas under s. NR 812.12(3). The casing must terminate “<i>at least "
    "12&nbsp;inches above the established ground surface</i>” (s. NR 812.29(1)), "
    "and a well may not terminate in or extend through a basement or a crawl "
    "space (s. NR 812.08(2)(c)) — with a narrow exception for a qualifying "
    "walkout basement. Water samples for total coliform bacteria and nitrate "
    "must be collected after new well construction (s. NR 812.46(1)(b)); that "
    "is state law, not merely a lender's condition."))

# ---------------------------------------------------------------- table A
flow += k.h2_tight("WELL SEPARATION DISTANCES — NR 812.08, TABLE A",
                   reserve=2.2)
flow.append(k.body(
    "This table decides where the well can go, and therefore — because the "
    "septic and the house have to clear it too — where everything else goes. "
    "Lay all three out together before you commit to a house position."))
flow.append(k.callout_long("Read these four rules before you read the table", [
    Paragraph("<b>Measured to the source, and the property line is "
              "irrelevant.</b> “<i>Separation distances shall be measured from "
              "the edge of the well, reservoir, or spring, to the nearest edge "
              "of the contaminant source or as specified in Table A. "
              "<b>Separation distance requirements to possible contaminant "
              "sources may not be waived because of a property line.</b></i>” "
              "(s. NR 812.08(4)) A neighbor's drain field 30&nbsp;feet away on the "
              "far side of your lot line still breaks the 50-foot rule.",
              S["body"]),
    Paragraph("<b>Anything not listed gets 8&nbsp;feet.</b> A well shall be located "
              "“<i>such that any potential contaminant source, not identified "
              "in this section or in Table A, is a minimum of 8&nbsp;feet from the "
              "well, reservoir, or spring</i>” (s. NR 812.08(1)(d)).",
              S["body"]),
    Paragraph("<b>Put it high.</b> The well shall be located “<i>so that the "
              "well, reservoir or spring is protected from surface water flow "
              "and flooding, and located at the highest point on the property "
              "consistent with the general layout and surroundings if "
              "reasonably possible</i>” (s. NR 812.08(1)(b)).", S["body"]),
    Paragraph("<b>There is no well-to-house number.</b> Table A has no "
              "foundation row. Buildings are handled by construction rules "
              "instead: no well in line with a downspout, none terminating in "
              "a basement or crawl space, and an access hatch if a structure "
              "is built over it (s. NR 812.08(2)).", S["body"]),
]))

flow.append(Spacer(1, 6))
rows = [
    [k.cellp("<b>POWTS dispersal component</b> (soil absorption unit or "
             "mound), under 12,000&nbsp;gallons per day"),
     k.cellp("<b>50</b>", center=True)],
    [k.cellp("<b>POWTS treatment component</b> — septic tanks, aerobic "
             "treatment units or filters"),
     k.cellp("<b>25</b>", center=True)],
    [k.cellp("<b>POWTS holding component</b> — a wastewater holding tank"),
     k.cellp("<b>25</b>", center=True)],
    [k.cellp("Sanitary building sewer"), k.cellp("8", center=True)],
    [k.cellp("Sanitary collector sewer"), k.cellp("25", center=True)],
    [k.cellp("Storm sewer"), k.cellp("8", center=True)],
    [k.cellp("Drain — sanitary building"), k.cellp("8", center=True)],
    [k.cellp("<b>Shoreline</b> — lake or pond, measured to the regional "
             "high-water elevation; river or stream, to the edge of the "
             "floodway"),
     k.cellp("<b>25</b>", center=True)],
    [k.cellp("Ditch — edge of"), k.cellp("8", center=True)],
    [k.cellp("Culvert, stormwater"), k.cellp("8", center=True)],
    [k.cellp("Stormwater detention basin, measured to the edge"),
     k.cellp("25", center=True)],
    [k.cellp("Stormwater infiltration basin or system at a single- or "
             "two-family residence, including rain gardens and infiltration "
             "trenches"),
     k.cellp("8", center=True)],
    [k.cellp("Swimming pool, above or below ground, measured from edge of "
             "water"), k.cellp("8", center=True)],
    [k.cellp("Cistern"), k.cellp("8", center=True)],
    [k.cellp("Nonpotable well"), k.cellp("8", center=True)],
    [k.cellp("Pit or alcove — noncomplying"), k.cellp("8", center=True)],
    [k.cellp("Heat exchange drillhole"), k.cellp("10", center=True)],
    [k.cellp("Sump — wastewater, watertight"), k.cellp("8", center=True)],
    [k.cellp("Sump — wastewater, not watertight"), k.cellp("25", center=True)],
    [k.cellp("Privy — vault privy (watertight)"), k.cellp("25", center=True)],
    [k.cellp("Privy — pit privy (not watertight)"), k.cellp("50", center=True)],
    [k.cellp("<b>Liquid propane gas tank</b>, buried or surface, and "
             "associated buried gas lines serving a single-family residence"),
     k.cellp("<b>8</b>", center=True)],
    [k.cellp("Fuel oil tank, 1,500&nbsp;gallons or less on the surface, or any "
             "size buried, serving a single-family residence"),
     k.cellp("25", center=True)],
    [k.cellp("Fuel oil tank over 1,500&nbsp;gallons on the surface, or any size "
             "buried"), k.cellp("100", center=True)],
    [k.cellp("Gasoline or other petroleum tank — surface, under 1,500 "
             "gallons, not including liquid propane tanks"),
     k.cellp("25", center=True)],
    [k.cellp("Gasoline or other petroleum tank — buried"),
     k.cellp("100", center=True)],
    [k.cellp("Grease interceptor (buried trap)"), k.cellp("25", center=True)],
    [k.cellp("Pet animal shelter or kennel housing not more than 5 pets"),
     k.cellp("8", center=True)],
    [k.cellp("Pet animal shelter or kennel housing more than 5 pets"),
     k.cellp("50", center=True)],
    [k.cellp("Pet waste pit disposal unit"), k.cellp("50", center=True)],
    [k.cellp("Animal barn or barn pen, measured to the nearest outside edge "
             "of the building or structure"), k.cellp("50", center=True)],
    [k.cellp("Animal shelter; animal yard, including a calf hutch"),
     k.cellp("50", center=True)],
    [k.cellp("Silo, not including dry grain storage structures"),
     k.cellp("50", center=True)],
    [k.cellp("Manure storage structure — fabricated, liquid-tight"),
     k.cellp("100", center=True)],
    [k.cellp("Manure storage structure — earthen, excavated or non-liquid "
             "tight"), k.cellp("250", center=True)],
    [k.cellp("Manure stack — temporary"), k.cellp("150", center=True)],
    [k.cellp("Cemetery grave sites"), k.cellp("50", center=True)],
    [k.cellp("Fertilizer or pesticide storage tank, any size, potable wells"),
     k.cellp("100", center=True)],
    [k.cellp("Salvage yard or junkyard"), k.cellp("250", center=True)],
    [k.cellp("Salt or deicing material storage area"),
     k.cellp("250", center=True)],
    [k.cellp("Quarry"), k.cellp("500", center=True)],
    [k.cellp("Landfill, active, proposed or closed"),
     k.cellp("1,200", center=True)],
    [k.cellp("Coal storage over 500 tons"), k.cellp("1,200", center=True)],
]
flow.append(k.ref_table(
    "Minimum separation distances between a well and possible contamination "
    "sources, in feet",
    [k.cellp("Source, as the table names it", bold=True),
     k.cellp("Feet", bold=True)],
    rows, [CW - 0.95 * inch, 0.95 * inch]))
flow.append(k.cite(
    "Wis. Admin. Code s. NR 812.08, Table A, “Minimum Separation Distance "
    "Requirements Between Potable or Nonpotable Wells, Reservoirs, Springs, "
    "and Possible Contamination Sources.” Chapter as published, Register "
    "February 2026 No. 842; Table A last amended by CR 25-013, effective "
    "1 March 2026. The rows above are the ones a house site meets; the full "
    "table also covers silage, sludge, wastewater plants, solid waste and "
    "hazardous waste facilities. Two footnotes matter on a house site: the "
    "POWTS dispersal distance “<i>does not apply if the component has been "
    "abandoned in accordance with s. SPS 383.33</i>”, and the pond-shoreline "
    "distance does not apply to “<i>synthetically lined decorative yard ponds "
    "located on residential lots</i>.”"))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "The abandonment footnote can rescue a tight lot", [
        Paragraph("If an old drain field sits where your 50&nbsp;feet needs to be, "
                  "footnote 2 to Table A says the separation distance "
                  "“<i>does not apply if the component has been abandoned in "
                  "accordance with s. SPS 383.33</i>”. Properly abandoning the "
                  "old system removes its setback. On a small or awkward "
                  "parcel that is sometimes the difference between a workable "
                  "layout and no layout at all — raise it with the county "
                  "before you conclude the lot cannot be built on.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- POWTS
flow += k.h2_tight("POWTS SETBACKS — SPS 383.43, TABLE 383.43-1", reserve=2.2)
flow.append(k.body(
    "The septic side has its own, much shorter table. Note that it does "
    "<b>not</b> carry a well distance — it defers to the well chapter, which "
    "is why the numbers above govern."))
rows = [
    [k.cellp("<b>Building</b>"), k.cellp("10", center=True),
     k.cellp("5", center=True), k.cellp("none", center=True)],
    [k.cellp("<b>Property line</b>"), k.cellp("5", center=True),
     k.cellp("2", center=True), k.cellp("2", center=True)],
    [k.cellp("<b>Swimming pool</b>"), k.cellp("15", center=True),
     k.cellp("none", center=True), k.cellp("none", center=True)],
    [k.cellp("<b>Ordinary high-water mark of navigable waters</b>"),
     k.cellp("50", center=True), k.cellp("10", center=True),
     k.cellp("10", center=True)],
    [k.cellp("<b>Water service and private water main</b>"),
     k.cellp("10", center=True), k.cellp("10", center=True),
     k.cellp("5", center=True)],
    [k.cellp("<b>Well</b>"),
     k.cellp("chs. NR 811 &amp; 812", center=True),
     k.cellp("chs. NR 811 &amp; 812", center=True),
     k.cellp("chs. NR 811 &amp; 812", center=True)],
]
flow.append(k.ref_table(
    "Horizontal setback parameters, in feet",
    [k.cellp("Physical feature", bold=True),
     k.cellp("Dispersal component, or treatment component of in situ soil",
             bold=True),
     k.cellp("Exterior subsurface treatment or holding tank", bold=True),
     k.cellp("Forcemains, suction and pump discharge lines", bold=True)],
    rows, [CW - 4.35 * inch, 1.6 * inch, 1.5 * inch, 1.25 * inch]))
flow.append(k.cite(
    "Wis. Admin. Code s. SPS 383.43, Table 383.43-1, “Horizontal Setback "
    "Parameters”; chapter as published, Register August 2026 No. 848, table "
    "content effective 1 July 2013. Footnotes: the 5-foot tank distance "
    "excludes recreational-vehicle transfer tanks; “none” is subject to the "
    "accessibility rule in s. SPS 383.43(8)(f); and “<i>road right-of-way "
    "lines may be more restrictive than property lines</i>.” The trigger "
    "sentence reads: “<i>POWTS treatment, holding and dispersal components "
    "shall be located so as to provide the minimum horizontal setback "
    "distances as outlined in Table 383.43-1 as safety factors for public "
    "health, waters of the state and structures in the event of component "
    "failure.</i>” (s. SPS 383.43(8)(i))"))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "The vertical number people get wrong", [
        Paragraph("Wisconsin's required vertical separation is <b>24 "
                  "inches</b>, not three feet: “<i>The infiltrative surface of "
                  "unsaturated soil to which influent is discharged shall be "
                  "located at least 24&nbsp;inches above the estimated highest "
                  "groundwater elevation and bedrock.</i>” "
                  "(s. SPS 383.44(3)(a))", S["body"]),
        Paragraph("The 36-inch figure is genuinely Wisconsin's — it is just "
                  "forty years out of date. The code says so itself in a note: "
                  "“<i>Since December 1, 1969 to July 1, 2000, the state "
                  "plumbing code required 36&nbsp;inches of soil between the "
                  "infiltrative surface of a POWTS and high groundwater or "
                  "bedrock.</i>” Since 2000 it has been 24&nbsp;inches. And note "
                  "there is <b>no table in the code that maps soil depth to a "
                  "system type</b> — no rule says “this depth means a mound”. "
                  "The soil tester's application rate and the 24-inch "
                  "separation decide the design, and the system type falls out "
                  "of that.", S["body"]),
    ]))

# ---------------------------------------------------------------- shoreland
flow += k.h2_tight("IF THE PARCEL IS NEAR WATER", reserve=2.2)
flow.append(k.body(
    "Shoreland zoning is county-run and mandatory: “<i>each county shall zone "
    "by ordinance all shorelands in its unincorporated area</i>” "
    "(Wis. Stat. s. 59.692(1c)). Shorelands reach <b>1,000&nbsp;feet from a lake, "
    "pond or flowage</b> and <b>300&nbsp;feet from a river or stream, or to the "
    "landward side of the floodplain, whichever is greater</b> "
    "(s. 59.692(1)(b)). And “structure” is defined widely enough to include a "
    "sidewalk, a deck, a retaining wall and a fire pit (s. 59.692(1)(e))."))
rows = [
    [k.cellp("<b>Setback from the ordinary high-water mark</b>"),
     k.cellp("<b>75&nbsp;feet</b> to the nearest part of any building or structure. "
             "Where an existing development pattern exists it may be reduced "
             "to the average of the adjacent lots, but <b>never below 35 "
             "feet</b>")],
    [k.cellp("<b>Vegetative buffer zone</b>"),
     k.cellp("<b>35&nbsp;feet</b> inland from the ordinary high-water mark, with "
             "vegetation removal prohibited except for maintenance, access and "
             "viewing corridors, and the other listed exceptions")],
    [k.cellp("<b>Impervious surface</b>"),
     k.cellp("Generally <b>15%</b> of the lot, applied to anything within "
             "<b>300&nbsp;feet</b> of the ordinary high-water mark. Up to 30% is "
             "possible with a county-approved <b>mitigation plan recorded at "
             "the register of deeds</b>")],
    [k.cellp("<b>Minimum unsewered lot</b>"),
     k.cellp("<b>100&nbsp;feet</b> average width and <b>20,000 square feet</b> "
             "area. Sewered: 65&nbsp;feet and 10,000 square feet")],
]
flow.append(k.ref_table(
    "Shoreland minimum standards — s. NR 115.05(1)",
    [k.cellp("Standard", bold=True), k.cellp("What it requires", bold=True)],
    rows, [1.95 * inch, CW - 1.95 * inch]))
flow.append(k.cite(
    "Chapter NR 115 as published, Register November 2024 No. 827. Counties may "
    "not regulate a matter more restrictively than a shoreland zoning standard "
    "(Wis. Stat. s. 59.692(1d)(a)), but may regulate matters NR 115 does not "
    "reach. One live conflict to be aware of: NR 115.05(1)(c)2.b caps an "
    "access and viewing corridor at the lesser of 30&nbsp;percent of frontage or "
    "200&nbsp;feet, while Wis. Stat. s. 59.692(1f)(b)1. forbids an ordinance from "
    "setting that maximum below the greater of 10&nbsp;feet or 35&nbsp;percent, subject "
    "to the same 200-foot ceiling. The rule has not been conformed to the "
    "later statute — treat the <b>200-foot cap as certain</b> and get your "
    "county's current corridor figure in writing."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "Do the impervious arithmetic before you make an offer", [
        Paragraph("On a minimum unsewered lake lot — 20,000 square feet — a "
                  "15% impervious cap is <b>3,000 square feet total</b> for "
                  "the house footprint, the garage, the driveway, the patio "
                  "and the walks combined. That is a smaller house than most "
                  "buyers picture once a driveway is in.", S["body"]),
        Paragraph("There is relief if your county has adopted it: NR "
                  "115.05(1)(e)3m. lets a county <i>exclude</i> impervious "
                  "area whose runoff “<i>is treated by devices such as "
                  "stormwater ponds, constructed wetlands, infiltration "
                  "basins, rain gardens, bioswales or other engineered "
                  "systems</i>”. Ask the county zoning office whether it "
                  "allows treated-surface credit before you redesign the "
                  "house.", S["body"]),
    ]))

flow.append(Spacer(1, 6))
flow.append(k.callout_long("Floodplain: what is forbidden, and what it costs",
                           [
    Paragraph("<b>In the floodway, three things are simply prohibited</b>: a "
              "structure “<i>designed for human habitation</i>”, “<i>any "
              "sewage system, whether public or private</i>” except portable "
              "latrines removed during flooding, and “<i>any well … used to "
              "obtain water for ultimate human consumption</i>” "
              "(s. NR 116.12(1)(b), (e), (f)). No house, no septic, no well.",
              S["body"]),
    Paragraph("<b>In the flood fringe you can build, on fill.</b> The lowest "
              "floor excluding basement must be at or above the <b>flood "
              "protection elevation</b>, which is “<i>2&nbsp;feet above the regional "
              "flood elevation</i>” (s. NR 116.03(20)). The fill must be "
              "“<i>not less than one foot above the regional flood "
              "elevation</i>”, extend “<i>at least 15&nbsp;feet beyond the limits "
              "of any structure</i>”, and “<i>dryland access shall be "
              "provided</i>” (s. NR 116.13(2)(b)). Any basement floor must be "
              "at or above the regional flood elevation and floodproofed — and "
              "“<i>no variance may be granted to allow any floor below the "
              "regional flood elevation</i>”.", S["body"]),
    Paragraph("This is also the one place Wisconsin makes you buy a "
              "professional. A registered land surveyor, architect or engineer "
              "“<i>shall certify the actual elevation … of the lowest "
              "structural member required to be elevated</i>” "
              "(s. SPS 321.33(3)) — and floodplain construction is the sole "
              "exception to the rule that a municipality may not require a "
              "sealed plan. <b>Get a flood zone determination and the regional "
              "flood elevation from the county zoning office in writing before "
              "you close on riparian land.</b>", S["body"]),
]))

# ---------------------------------------------------------------- driveway
flow += k.h2_tight("THE DRIVEWAY, AND THE ONE-ACRE LINE", reserve=2.0)
flow.append(k.body(
    "One statute covers every class of road and the rule is simply <i>whoever "
    "maintains it, permits it</i>: no person “<i>shall make any excavation or "
    "fill or install any culvert or make any other alteration in any highway … "
    "without a permit therefor from the highway authority maintaining the "
    "highway</i>” (Wis. Stat. s. 86.07(2)(a)). A state highway means the "
    "Department of Transportation; a county trunk highway means the county "
    "highway department; a town road means the <b>town board</b> — which is "
    "the one owner-builders forget, and often the slowest, because town boards "
    "meet monthly."))
flow.append(k.body(
    "For a residential entrance onto a state highway the specification is "
    "printed in the rule: a noncommercial rural driveway may be no “<i>less "
    "than 16&nbsp;feet nor greater than 24&nbsp;feet</i>” wide measured at right angles "
    "to the centerline, with a return radius no “<i>greater than 30&nbsp;feet</i>”, "
    "placed at approximately right angles to the pavement except where "
    "topography requires otherwise (s. Trans 231.05). Note also that a state "
    "permit “<i>shall not supersede more restrictive requirements imposed by "
    "valid applicable local ordinances</i>” (s. Trans 231.01(4)) — it does not "
    "get you past county zoning. If your frontage is on a controlled-access "
    "highway, direct driveway access may not be available at all "
    "(Wis. Stat. s. 84.25)."))
flow.append(k.callout(
    "One acre of disturbance is closer than it looks", [
        Paragraph("Below one acre, erosion control rides on your building "
                  "permit. At one acre or more it becomes a separate "
                  "Department of Natural Resources permit: a notice of intent "
                  "“<i>shall be submitted so that it is received by the "
                  "department at least 14 working days prior to the "
                  "commencement of any land disturbing construction "
                  "activities</i>” (s. NR 216.44(1)), with the erosion control "
                  "and stormwater plan completed <i>before</i> the notice goes "
                  "in (s. NR 216.44(2)).", S["body"]),
        Paragraph("<b>And the fee doubles if you file late</b>: “<i>If an "
                  "applicant applies for a permit after land disturbance has "
                  "commenced, the application fees … shall be doubled.</i>” "
                  "(s. NR 216.43(4)) A house pad, a driveway, a septic field "
                  "and a materials staging area on a wooded lot cross an acre "
                  "far more easily than people expect. If you are anywhere "
                  "near the line, file.", S["body"]),
    ]))

# ---------------------------------------------------------------- write-in
flow += k.h2_tight("WRITE DOWN WHAT YOU CONFIRMED", reserve=2.0)
flow.append(k.body(
    "Every line below has a different answer depending on your parcel. Fill "
    "them in once and you will not have to find them again."))
flow += k.check_table(
    "My offices, confirmed",
    [("Exact municipality of the parcel (town, village or city)",
      [("Name", 0.6), ("County", 0.4)]),
     ("Is it on the UDC Delegated Municipalities List?",
      [("Yes / No", 0.4), ("Checked on", 0.6)]),
     ("Who issues my building permit and does my inspections",
      [("Name", 1.0)]),
     ("County office that issues sanitary permits",
      [("Office", 1.0)]),
     ("County zoning office",
      [("Office", 1.0)]),
     ("Does the county run a delegated well program under NR 845?",
      [("Yes / No", 0.4), ("Confirmed by", 0.6)]),
     ("Is there an existing soil test on this parcel?",
      [("Yes / No", 0.4), ("Date", 0.6)]),
     ("Shoreland: is any part within 1,000 ft of a lake or 300 ft of a "
      "stream?", [("Yes / No", 0.4), ("Setback required", 0.6)]),
     ("Floodplain: flood zone and regional flood elevation",
      [("Zone", 0.4), ("RFE", 0.6)]),
     ("Road authority for my driveway",
      [("Town / County / DOT", 0.6), ("Permit no.", 0.4)]),
     ("Total land disturbance — over one acre?",
      [("Acres", 0.4), ("NOI filed", 0.6)]),
     ("Rural address / fire number assigned by",
      [("Office", 0.6), ("Address", 0.4)])],
    notes_header="Notes")

flow.append(Spacer(1, 4))
flow.append(k.body(
    "<b>On the rural address:</b> Wisconsin has no single statewide office for "
    "it. Ask when you file for zoning, and try Land Information, Real Property "
    "Lister, Planning and Zoning, or Emergency Management, in that order. The "
    "number is normally keyed to your approved <i>driveway</i> location rather "
    "than the house, so the driveway permit usually has to come first."))

flow.append(Spacer(1, 4))
flow.append(k.ref_table(
    "Sources — every Wisconsin claim in this document (verified September 2026)",
    [k.cellp("What this document states", bold=True),
     k.cellp("Authority", bold=True)],
    [[k.cellp("The two DSPS lookup documents and the 13 delegated counties"),
      k.cellp("UDC Delegated Municipalities List, 19 Aug 2026; UDC Permit and "
              "Inspection Map, rev. 2 Apr 2026")],
     [k.cellp("Same agency issues the permit and does the inspections"),
      k.cellp("s. SPS 320.08(2)")],
     [k.cellp("Sanitary permits come from the county"),
      k.cellp("Wis. Stat. s. 145.01(5)")],
     [k.cellp("The county may put the POWTS program in any office"),
      k.cellp("Wis. Stat. s. 145.20(1)(a)")],
     [k.cellp("The county holds and must accept prior soil test results"),
      k.cellp("Wis. Stat. s. 145.19(1r)")],
     [k.cellp("An owner may drill their own well"),
      k.cellp("s. NR 812.10(1)(a)")],
     [k.cellp("Well notification to the department before construction"),
      k.cellp("Wis. Stat. s. 281.34(3)(a); s. NR 812.10(8)")],
     [k.cellp("Construction report within 30 days, to the department and to "
              "you"), k.cellp("s. NR 812.10(11)")],
     [k.cellp("Minimum casing depths and diameters"),
      k.cellp("ss. NR 812.13, 812.14, 812.29(1)")],
     [k.cellp("Coliform and nitrate sampling after new construction"),
      k.cellp("s. NR 812.46(1)(b)")],
     [k.cellp("The well separation distances"),
      k.cellp("s. NR 812.08, Table A; CR 25-013, eff. 1 Mar 2026")],
     [k.cellp("Distances measured to the source, not waived at a lot line"),
      k.cellp("s. NR 812.08(4)")],
     [k.cellp("The POWTS horizontal setbacks"),
      k.cellp("s. SPS 383.43, Table 383.43-1")],
     [k.cellp("24&nbsp;inches of vertical separation"),
      k.cellp("s. SPS 383.44(3)(a)")],
     [k.cellp("Counties shall zone all shorelands; 1,000 ft and 300 ft"),
      k.cellp("Wis. Stat. s. 59.692(1c), (1)(b)")],
     [k.cellp("75-foot setback, 35-foot buffer, 15% impervious, lot sizes"),
      k.cellp("s. NR 115.05(1)(a), (b), (c), (e)")],
     [k.cellp("Flood protection elevation is regional flood plus 2&nbsp;feet"),
      k.cellp("s. NR 116.03(20)")],
     [k.cellp("No house, septic or well in a floodway"),
      k.cellp("s. NR 116.12(1)(b), (e), (f)")],
     [k.cellp("Driveway permit from the maintaining authority; the rural "
              "driveway spec"),
      k.cellp("Wis. Stat. s. 86.07(2)(a); ss. Trans 231.01(4), 231.05")],
     [k.cellp("One acre; 14 working days; doubled late fee"),
      k.cellp("ss. NR 216.42(1), 216.44(1), 216.43(4)")]],
    [CW - 2.65 * inch, 2.65 * inch]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "wi-permit-kit",
                       "WI.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
