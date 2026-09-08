#!/usr/bin/env python3
"""NE.4 Where to File Directory.

Every web address in this document was confirmed to resolve in September 2026.
No phone numbers appear anywhere in this kit — they go stale faster than
anything else on a printed page, and every office below can be reached from its
own site. That rule also keeps us from reproducing the State Electrical
Division's inspection map attributes, which carry inspector names, emails and
phone numbers.

The organizing idea: Nebraska publishes ONE authoritative lookup — the State
Electrical Division's map of who inspects electrical at any address — and
publishes NOTHING on which counties issue building permits, because no statute
requires a county to and none requires anyone to report it. So this document
is two things: here is the map and how to read it; and here is the three-step
check you run yourself for the building permit, because no list exists.

Verified in this pass:
  The SED inspection-jurisdiction layer (NSED_Inspector_Programs) was queried
  directly: 43 features; every one not listed below is "State of Nebraska".
  Five counties and fourteen cities run their own programs; La Vista (Sarpy),
  Waverly (Lancaster) and Boys Town (Douglas) are state-inspected despite the
  county around them.
  Lincoln's codes and homeowner-permit pages were read (WebFetch; the site
  refuses curl). Sarpy County Resolution 2024-150 was read from the county's
  document center.
  Omaha's and Douglas County's sites returned 403 to every method. Nothing
  Omaha-specific is printed as fact; the document prints the statutory frame
  and the confirm-at-the-counter instruction.

DELIBERATELY NOT PRINTED:
  - A count of counties or cities with building-permit programs. No primary
    source exists.
  - Any Omaha or Douglas County fee, edition, frost depth or procedure.
  - A county-to-NRD table or an NRD domestic-well permit rule. Not verified;
    the document says ask.
  - A statewide 911 addressing process. Administered locally.
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
NB = k.NB

FORM_ID = "NE.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The one map Nebraska publishes, the list it does not, and the offices "
    "that exist whatever your county decided.")

flow.append(k.disclaimer(
    "Every web address here was checked in September 2026. The electrical map "
    "changes when a city adopts an inspection ordinance; the building-permit "
    "answer changes when a county board passes a resolution. Neither is "
    "announced anywhere central."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- the map
flow += k.h2_tight("THE MAP EXISTS FOR ELECTRICAL — AND IT IS THE LOOKUP "
                   "THAT MATTERS", reserve=2.0)
flow.append(k.body(
    "State electrical inspection \"shall not apply within the jurisdiction of "
    "any county, city, or village which provides by resolution or ordinance\" "
    "its own wiring standards and its own inspection \"by a certified "
    f"electrical inspector\" ({sec('81-2125(1)')}). The State Electrical "
    f"Division publishes exactly who has done that, as a map. When this kit "
    f"was assembled the map's data layer held 43 features and broke down as "
    f"follows — <b>everyone not on this list is inspected by the state.</b>"))
rows = [
    [k.cellp("<b>Counties (5 of 93)</b>"),
     k.cellp("<b>Lancaster, Hall, Dodge, Douglas, Sarpy</b>")],
    [k.cellp("<b>Cities (14)</b>"),
     k.cellp("<b>Lincoln, Omaha, Bellevue, Papillion, Gretna, Ralston, Grand "
             "Island, Hastings, Kearney, Fremont, Norfolk, York, South Sioux "
             "City</b> (which also covers the villages of Jackson and Homer) "
             "and <b>Hickman</b>")],
    [k.cellp("<b>The traps inside those counties</b>"),
     k.cellp("<b>La Vista</b> (Sarpy County), <b>Waverly</b> (Lancaster "
             "County) and <b>Boys Town</b> (Douglas County) are each "
             "explicitly <b>State of Nebraska</b> on the layer, despite the "
             "county around them. So are the villages of Lancaster, Dodge and "
             "Douglas counties. <b>Look the parcel up; do not infer from the "
             "county</b>")],
]
flow.append(k.ref_table(
    "Who runs their own electrical inspection — SED layer, September 2026",
    [k.cellp("Level", bold=True), k.cellp("Jurisdictions", bold=True)],
    rows, [1.7 * inch, CW - 1.7 * inch]))
flow.append(k.callout(
    "The one address to write down", [
        Paragraph("<b>electrical.nebraska.gov/nsed-inspection-gis-mapping</b> "
                  "— the Division's notice page, which links the interactive "
                  "map. Enter the address; the parcel's inspector "
                  "jurisdiction and district inspector are shown on the map "
                  "itself.", S["body"]),
        Paragraph("A local program must meet the state standard and may "
                  "exceed it; a subdivision that runs one files its ordinance "
                  f"with the board and may not charge a state licensee a "
                  f"local license fee ({sec('81-2130')}). Where the map says "
                  f"<b>State of Nebraska</b>, the request for inspection, the "
                  f"fees and the clocks in NE.2 and NE.3 are yours; where it "
                  f"names a city or county, that program's permit replaces "
                  f"the state's and its fee schedule applies — ask.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- no list
flow += k.h2_tight("NO LIST EXISTS FOR BUILDING PERMITS — HERE IS THE CHECK "
                   "YOU RUN INSTEAD", reserve=2.2)
flow.append(k.body(
    "No state agency publishes which of Nebraska's 93 counties or its cities "
    "and villages issue building permits, and this is not an oversight: "
    f"{sec('71-6406(7)')} makes administration optional, {sec('23-172')} lets "
    f"a county adopt a code by resolution, and nothing requires anyone to "
    f"report it. <b>Any guide that gives you a number is guessing.</b> The "
    f"honest path is three questions, each to the office that holds the "
    f"answer."))
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp("<b>The county clerk</b>"),
     k.cellp(f"Two questions. Has the county board adopted a building code "
             f"by resolution under {sec('23-172')} — and which editions? "
             f"And does the county's zoning resolution require a permit "
             f"\"prior to the erection … of any nonfarm building\" under "
             f"{sec('23-114.04')}? A county can have the second without the "
             f"first. A copy of any adopted code must be on file \"in the "
             f"office of the clerk\" ({sec('71-6406(8)')})")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("<b>The city or village clerk</b>, if you are inside one — or "
             "near one"),
     k.cellp(f"County codes reach \"all of the county except within the "
             f"limits of any incorporated city or village and except within "
             f"an unincorporated area where a city or village has been "
             f"granted zoning jurisdiction and is exercising such "
             f"jurisdiction\" ({sec('23-172(5)')}). Omaha's reach is three "
             f"miles ({sec('14-419(1)')}); Lincoln's is set by "
             f"{sec('15-905')}; smaller cities have their own zones. Ask the "
             f"city whether your parcel is inside its extraterritorial "
             f"jurisdiction, and if so, whose permit")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("<b>The State Electrical Division's map</b>"),
     k.cellp("For the electrical answer, which does not follow the building "
             "answer: the two lists are made under different statutes by "
             "different resolutions. A county may run its own electrical "
             "inspection whatever it decided about a building code, and a "
             "city inside such a county may still be state-inspected "
             "(La Vista, Waverly)")],
]
flow.append(k.ref_table(
    "Three questions, three offices",
    [k.cellp("", bold=True, center=True), k.cellp("Ask", bold=True),
     k.cellp("What you are asking, and why", bold=True)],
    rows, [0.35 * inch, 1.6 * inch, CW - 1.95 * inch]))
flow.append(k.cite(
    "<b>Get each answer in writing and date it.</b> Email is fine. Write it on "
    "the directory page at the end of this document. In three years, when an "
    "appraiser asks why there is no building permit on file, that email is "
    "your answer — and it is the only one you will have, because the state "
    f"keeps no record. If the answer is \"no code adopted,\" the state code "
    f"applies by default ({sec('71-6406(1)(b)')}) and binds the house whether "
    f"or not anyone inspects it ({sec('71-6406(7)')})."))

# ---------------------------------------------------------------- state offices
flow += k.h2_tight("THE STATE OFFICES — FOUR AGENCIES, AND WHICH DOES WHAT",
                   reserve=2.4)
flow.append(k.body(
    "Nebraska splits a house between four state agencies, and published "
    "guides routinely swap two of them. <b>Radon is DHHS. Septic is DWEE.</b>"))
rows = [
    [k.cellp("<b>State Electrical Division</b> (NSED)"),
     k.cellp("The request for inspection, homeowner verification, "
             "inspections, the map, the Board rules. Online permitting since "
             "April 13, 2026"),
     k.cellp(f"{sec('81-2101')} et seq.")],
    [k.cellp("<b>Department of Water, Energy, and Environment</b> (DWEE)"),
     k.cellp("<b>Three programs:</b> the Nebraska Energy Code (the fact "
             "sheet, REScheck, the two-year order); <b>onsite wastewater</b> "
             "(Title 124, the general permits, system registration, "
             "installer certification); and <b>water wells</b> (Title 134, "
             "well registration, driller licensing). Rule PDFs issued before "
             "2025 still say \"NDEE\" — same agency, renamed"),
     k.cellp(f"{sec('81-1609(1)')}; {sec('81-15,248')}; {sec('46-1207')}")],
    [k.cellp("<b>Department of Health and Human Services</b> (DHHS)"),
     k.cellp("<b>Radon</b>: the county-average determination that decides "
             "the under-2.7 exemption, the RRNC requirements document, "
             "mitigation-specialist licensing"),
     k.cellp(f"{sec('76-3503(3)')}; {sec('76-3507')}")],
    [k.cellp("<b>Department of Labor</b> (DOL)"),
     k.cellp("The <b>contractor registry</b> — every trade you hire, with "
             "its workers' compensation flag. You do not register"),
     k.cellp(f"{sec('48-2104(1)')}; {sec('48-2117')}")],
    [k.cellp("<b>Nebraska 811</b>"),
     k.cellp("The One-Call center. Notice \"at least two full business days, "
             "but no more than ten business days,\" before excavation"),
     k.cellp(sec("76-2321(1)"))],
    [k.cellp("<b>Your Natural Resources District</b> (NRD)"),
     k.cellp("Nebraska's 23 NRDs regulate groundwater locally. <b>Ask yours "
             "whether it requires a permit or a spacing rule for a domestic "
             "well</b> — this kit could not verify a statewide answer and "
             "prints none"),
     k.cellp("Ask")],
]
flow.append(k.ref_table(
    "Who holds which piece of your house",
    [k.cellp("Agency", bold=True), k.cellp("What it does for a house",
                                           bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.9 * inch, CW - 1.9 * inch - 1.55 * inch, 1.55 * inch]))

# ---------------------------------------------------------------- Lincoln
flow += k.h2_tight("LINCOLN, WORKED — THE CITY THAT PUBLISHES ITS CONDITIONS",
                   reserve=2.2)
flow.append(k.body(
    "Lincoln is the example this kit can verify end to end, because Building "
    "&amp; Safety publishes its editions and its homeowner conditions. It is "
    f"also the proof that the state edition is a floor: Lincoln is ahead of "
    f"the state on every code but energy, which {sec('71-6406(2)(b)')} "
    f"expressly allows."))
rows = [
    [k.cellp("<b>Codes</b>"),
     k.cellp("<b>2021</b> IBC, IRC, IEBC, IMC, IFGC and <b>Uniform Plumbing "
             "Code</b>; <b>2023</b> NEC; <b>2018</b> IECC — each \"&amp; "
             "Local Amendments,\" in Lincoln Municipal Code Titles 20–25")],
    [k.cellp("<b>Who may hold a trade permit</b>"),
     k.cellp("Electrical, mechanical and plumbing permits \"may only be "
             "issued to a licensed contractor or a homeowner for their "
             "primary residence\"")],
    [k.cellp("<b>The homeowner conditions</b>"),
     k.cellp("\"Only the owner of the residence can apply for the permit.\" "
             "\"You must presently reside in the single-family dwelling or "
             "reside there after the construction is complete.\" \"The house "
             "cannot be in the process of being prepared for sale, not a "
             "rental property, or for intended use for becoming a rental "
             "property\"")],
    [k.cellp("<b>Permit life and inspections</b>"),
     k.cellp("\"Permits are valid for 120 days from issuances.\" \"The permit "
             "issued must be inspected before any work is concealed and must "
             "also be inspected when the installation of the work is "
             "completed\"")],
    [k.cellp("<b>Fees</b>"),
     k.cellp("Building permits: \"The minimum fee starts at $65 and increases "
             "from there\"; new homes are \"calculated based on the square "
             "footage with a $100 deposit.\" Homeowner trade permits: \"All "
             "permits will have a minimum $35 fee\"; \"Additional inspection "
             "trips are $35\"")],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("The City of Lincoln and Lancaster County each run their own "
             "program (SED layer) — but <b>Waverly</b> and the county's "
             "villages are state-inspected")],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp(f"Lincoln is a city of the primary class, so its plumbing board "
             f"is optional by statute ({sec('18-1901(2)')}); its homeowner "
             f"plumbing permit exists on the conditions above")],
]
flow.append(k.ref_table(
    "Lincoln — from the city's own pages, September 2026",
    [k.cellp("", bold=True), k.cellp("What the city says", bold=True)],
    rows, [1.75 * inch, CW - 1.75 * inch]))
flow.append(k.cite(
    "Read at lincoln.ne.gov — Building &amp; Safety \"Codes,\" \"Homeowner "
    "Building Permits,\" and the homeowner plumbing, mechanical and electrical "
    "project pages. The permit portal is <b>permits.lincoln.ne.gov/"
    "CitizenAccess</b>. <b>Treat the fees as perishable</b>; they are web-page "
    "figures, not ordinance figures."))

# ---------------------------------------------------------------- Sarpy
flow += k.h2_tight("SARPY COUNTY, WORKED — A COUNTY THAT ADOPTED BY "
                   "RESOLUTION", reserve=2.0)
flow.append(k.body(
    f"Sarpy is the example of a county that used {sec('23-172')}: "
    f"<b>Resolution 2024-150</b>, adopted and effective <b>June 4, 2024</b>, "
    f"adopts for \"the entire unincorporated area of Sarpy County\" the "
    f"<b>2018</b> International Building, Residential, Plumbing, Mechanical, "
    f"Fuel Gas and Energy Conservation Codes (with ICC/ANSI A117.1-2009), "
    f"replacing the 2012 editions, \"as amended.\""))
flow.append(k.bullet(
    "<b>Note the plumbing code: the 2018 IPC, not the UPC.</b> A county may "
    f"adopt a plumbing code of its own under {sec('23-172')} and still "
    f"conform ({sec('71-6406(2)(d)')}); the UPC is only the default where no "
    f"resolution exists. Inside unincorporated Sarpy, plumb to the IPC."))
flow.append(k.bullet(
    "<b>Electrical is a patchwork.</b> Sarpy County, Bellevue, Papillion and "
    "Gretna each run their own inspection program. <b>La Vista is "
    "state-inspected.</b> The county's portal is "
    "<b>co-sarpy-ne.smartgovcommunity.com</b>; Planning &amp; Building is at "
    "sarpy.gov/215/Planning-Building."))
flow.append(k.bullet(
    "The resolution's own narrative says the county adopts on alternate code "
    "cycles — expect a 2024-code resolution around 2028. Ask which edition "
    "is current the week you file."))

# ---------------------------------------------------------------- Omaha
flow += k.h2_tight("OMAHA AND DOUGLAS COUNTY — CONFIRM AT THE COUNTER",
                   reserve=2.2)
flow.append(k.callout_long(
    "Why this kit prints nothing Omaha-specific as fact", [
        Paragraph("Omaha's Planning Department pages (planning.omaha.gov) and "
                  "Douglas County Environmental Services (dceservices.org) "
                  "refused every automated request made for this kit — a "
                  "geographic block that returns \"This service is not "
                  "available in your region.\" Nothing on those sites could "
                  "be read. <b>So the Omaha code edition, its local "
                  "amendments, its plan-review fee, its frost depth and its "
                  "homeowner-permit procedure are not printed here</b>, and "
                  "any guide that prints them without a date should be "
                  "checked against the city's own page in a normal browser.",
                  S["body"]),
        Paragraph(f"What the statute does say: a city of the metropolitan "
                  f"class <b>shall</b> have a plumbing board ({sec('18-1901(1)')}) "
                  f"whose plumbers are \"licensed within such cities\" "
                  f"({sec('18-1901(6)')}) and which may \"compel the owner or "
                  f"contractor to first submit the plans and specifications "
                  f"for plumbing\" ({sec('18-1906')}); the city may regulate "
                  f"construction, \"electric wiring, heating, plumbing, "
                  f"pipefitting\" within the city and its three-mile zone, "
                  f"\"except as to construction on farms for farm purposes\" "
                  f"({sec('14-419(1)')}–(2)); and any code it adopts must "
                  f"conform under {sec('71-6406')} ({sec('14-419(4)')}). On "
                  f"the SED layer, the <b>City of Omaha</b>, <b>Douglas "
                  f"County</b> and <b>Ralston</b> each inspect their own "
                  f"electrical; <b>Boys Town</b> is state-inspected.",
                  S["body"]),
        Paragraph("<b>What to confirm at the counter, and write on the "
                  "directory page:</b> the residential and plumbing code "
                  "editions and where the amendments are published; whether "
                  "a homeowner may hold the building, plumbing and electrical "
                  "permits on a primary residence and on what conditions; "
                  "the fee basis; whether plan review is required and its "
                  "turnaround; whether the city or the county has "
                  "jurisdiction over your parcel if it is outside the city "
                  "limits.", S["body"]),
    ]))

# ---------------------------------------------------------------- sequence
flow += k.h2_tight("THE SEQUENCE, WHATEVER YOUR COUNTY DECIDED", reserve=2.4)
flow.append(k.body(
    "\"No building permit\" is not the same as \"no paperwork.\" The real "
    "risk is not missing an office — it is doing them in the wrong order, "
    "because two of them constrain where the house can physically sit."))
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp("<b>Run the three-question check</b>"),
     k.cellp("County clerk, city clerk, SED map. Before relying on any of the "
             "rest")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("<b>Septic professional and site evaluation</b>"),
     k.cellp("The perc test and the Table 2.1 setbacks fix where the "
             "drainfield, its reserve area and therefore the house can go. "
             "<b>Before you fix the footprint</b>")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("<b>Well siting</b>"),
     k.cellp("100 feet from the drainfield, 50 from the tank, both ways "
             "round. A variance request needs 10 days and a scaled map")],
    [k.cellp("<b>4</b>", center=True),
     k.cellp("<b>County zoning permit</b>, where zoned"),
     k.cellp("It needs the plans \"including sanitation, plumbing and sewage "
             "disposal\" — which is why steps 2 and 3 come first")],
    [k.cellp("<b>5</b>", center=True),
     k.cellp("<b>911 address</b>"),
     k.cellp("Administered locally — county or city. The electrical request "
             "and the utility need it")],
    [k.cellp("<b>6</b>", center=True),
     k.cellp("<b>Local building permit</b>, if one exists"),
     k.cellp("On the local program's form, to its editions, on its schedule")],
    [k.cellp("<b>7</b>", center=True),
     k.cellp("<b>Electrical request for inspection</b>"),
     k.cellp("State or local, <b>before any wiring</b>, with the homeowner "
             "verification and the power supplier's details. Temporary "
             "service five working days ahead")],
    [k.cellp("<b>8</b>", center=True),
     k.cellp("<b>Power supplier</b>"),
     k.cellp("Ask the utility what it needs before it sets a meter — the "
             "statute says your certificate that inspection was requested; "
             "the Division forwards the new-service permit")],
    [k.cellp("<b>9</b>", center=True),
     k.cellp("<b>Nebraska 811</b>"),
     k.cellp("At least two full business days before any excavation")],
    [k.cellp("<b>10</b>", center=True),
     k.cellp("<b>Floodplain and driveway</b>"),
     k.cellp("The FEMA map and the county or city floodplain administrator; "
             "the road authority you touch for a driveway or culvert")],
]
flow.append(k.ref_table(
    "The order that avoids re-doing anything",
    [k.cellp("", bold=True, center=True), k.cellp("Step", bold=True),
     k.cellp("Which office, and why the order", bold=True)],
    rows, [0.35 * inch, 1.85 * inch, CW - 2.2 * inch]))

# ---------------------------------------------------------------- addresses
flow += k.h2_tight("STATE-LEVEL ADDRESSES", reserve=2.0)
flow.append(k.body(
    "All confirmed to resolve in September 2026. <b>We print no phone numbers "
    "anywhere in this kit</b> — they go stale faster than anything else on a "
    "printed page, and every office below can be reached from its own site."))
rows = [
    [k.cellp("<b>Who inspects electrical at my address</b>"),
     k.cellp("electrical.nebraska.gov/nsed-inspection-gis-mapping")],
    [k.cellp("<b>The homeowner handout and permit</b>"),
     k.cellp("electrical.nebraska.gov/homeowner-handout")],
    [k.cellp("<b>The Act and the Board rules</b>"),
     k.cellp("electrical.nebraska.gov/statutes-rules")],
    [k.cellp("<b>Check a contractor's registration</b>"),
     k.cellp("dol.nebraska.gov/conreg/Search")],
    [k.cellp("<b>Energy code, fact sheet, REScheck</b>"),
     k.cellp("dwee.nebraska.gov/state-energy-information/energy-codes")],
    [k.cellp("<b>Septic — Title 124 and the general permits</b>"),
     k.cellp("dwee.nebraska.gov — search \"Title 124 Onsite Wastewater "
             "Treatment Systems Booklet\" (form 23-017)")],
    [k.cellp("<b>Wells — Title 134</b>"),
     k.cellp("dwee.nebraska.gov — Water Quality › Groundwater › Water Well "
             "Standards")],
    [k.cellp("<b>Radon — county data and RRNC requirements</b>"),
     k.cellp("dhhs.ne.gov/Pages/Radon-Data.aspx")],
    [k.cellp("<b>Any statute</b>"),
     k.cellp("nebraskalegislature.gov/laws/statutes.php?statute=71-6403")],
    [k.cellp("<b>Lincoln codes and permits</b>"),
     k.cellp("lincoln.ne.gov/City/Departments/Building-Safety/Codes; "
             "permits.lincoln.ne.gov/CitizenAccess")],
    [k.cellp("<b>Sarpy County</b>"),
     k.cellp("sarpy.gov/215/Planning-Building; "
             "co-sarpy-ne.smartgovcommunity.com")],
    [k.cellp("<b>Omaha / Douglas County</b> (geo-restricted)"),
     k.cellp("planning.omaha.gov/building-and-development-division; "
             "dceservices.org/permits-and-inspections")],
    [k.cellp("<b>Flood map</b>"), k.cellp("msc.fema.gov/portal/home")],
]
# 1.75in for the label column. The widest address in the right column is
# "dwee.nebraska.gov/state-energy-information/energy-codes" at 9.5pt, which
# clears the remaining 4.75in with room to spare; the labels wrap instead.
flow.append(k.ref_table(
    "Verified September 2026",
    [k.cellp("What you need", bold=True), k.cellp("Where", bold=True)],
    rows, [1.75 * inch, CW - 1.75 * inch]))
flow.append(k.cite(
    "<b>Two addresses people mix up.</b> The Division's map tells you who "
    "<i>inspects</i>; the Division's online system (linked from its home "
    "page since April 13, 2026) is where the <i>request</i> is filed and paid. "
    "And the Legislature's statute pages — not any agency's summary — are "
    "where the current text and its effective date live."))

# ---------------------------------------------------------------- write-in
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT",
                   reserve=1.6)
flow += k.check_table(
    "Every office that touches this build, confirmed and dated",
    [
        ("County clerk: building code adopted by resolution? Editions? "
         "Zoning permit required for a nonfarm dwelling?",
         [("Answer", 0.6), ("Date", 0.4)]),
        ("City or village clerk: am I inside the city or its "
         "extraterritorial zone, and whose permit applies?",
         [("Answer", 0.6), ("Date", 0.4)]),
        ("SED map: electrical inspection at my address is STATE or (name "
         "the program):", [("Answer", 0.6), ("Date read", 0.4)]),
        ("Building permit office, if one exists, and the editions it "
         "reviews to:", [("Office", 0.5), ("Editions", 0.5)]),
        ("Septic professional (Master Installer / engineer / REHS) and "
         "certificate number:", [("Name", 0.5), ("Certificate", 0.5)]),
        ("Well driller and license number — or \"self\" if I am drilling on "
         "my own abode land:", [("Driller", 0.5), ("License", 0.5)]),
        ("Natural Resources District, and whether it requires a domestic-well "
         "permit:", [("NRD", 0.5), ("Permit?", 0.5)]),
        ("Electric utility or public power district, and what it needs "
         "before setting a meter:", [("Utility", 0.5), ("Requires", 0.5)]),
        ("911 addressing office:", [("Office", 0.6), ("Address issued", 0.4)]),
        ("Floodplain administrator, and whether my parcel is in a mapped "
         "hazard area:", [("Office", 0.6), ("In or out", 0.4)]),
        ("Road authority for the driveway or culvert:", [("Authority", 1.0)]),
        "I called Nebraska 811 at least two full business days before any "
        "excavation.",
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ne-permit-kit",
                       "NE.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
