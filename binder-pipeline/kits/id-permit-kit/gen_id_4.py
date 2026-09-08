#!/usr/bin/env python3
"""ID.4 Where to File Directory.

Every web address in this document was confirmed to resolve in September 2026.
No phone numbers appear anywhere in this kit — they go stale faster than
anything else on a printed page, and every office below can be reached from its
own site. That rule also keeps us from reproducing DOPL's inspector list, which
names an inspector and a phone number for every city.

The organizing idea: unlike Tennessee, Idaho publishes NO list of which counties
enforce a building code, and DOPL publishes no roster of which cities run their
own trade programs (it holds one — 30 days' written notice is required — but
puts out only a permit map and an inspector schedule). So this document is a
method plus the offices that exist regardless: DOPL, the seven health districts
the statute fixes by county, and IDWR.

Verified in this pass:
  § 39-408              the seven public health districts, county by county
  § 39-4117(1)          the published permit-process document
  § 54-1001B(4), (5); § 54-2601(7), (8)   a city or county starting its own
                        electrical or plumbing program gives DOPL 30 days'
                        written notice; DOPL backstops a terminated program for
                        one year
  DOPL ele-permits page   "Purchase your permit on-line HERE Based on location"
                        → the location-based map
  DOPL Inspector List with Schedules, created 5 August 2026 — three columns,
                        ELECTRICAL / HVAC / PLUMBING, no building column
  DOPL homeowner forms   "As of January 1, 2023, all permits will need to be
                        purchased Online at DBS.IDAHO.GOV"; "email or mail all
                        … forms to the Boise office"
  DOPL HVAC board news   "Canyon County HVAC Program Coming to DOPL
                        September 1, 2023"
  DEQ septic page       seven districts "administer these rules under a
                        memorandum of understanding (MOU) with DEQ"
  IDWR wells page       drilling permit; licensed driller; driller search
  City of Boise building page   FY27 Building, Plumbing, Mechanical and Fuel
                        Gas, and Electrical Code fee schedules
  City of Coeur d'Alene building page   2018 I-Codes; "Local plumbing codes will
                        remain under the 2017 Idaho State Plumbing code with
                        current City Amendments"

DELIBERATELY NOT PRINTED:
  - A list of no-building-department counties. None is published.
  - Cities running their own trade programs beyond Boise and Coeur d'Alene.
  - The ArcGIS map's raw address (110 characters; un-typeable). The document
    prints the DOPL page it is linked from.
  - Any local fee figure.
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

FORM_ID = "ID.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Idaho publishes no list of who enforces what — here is the method, the "
    "offices that exist regardless, and two cities as worked examples.")

flow.append(k.disclaimer(
    "Every web address here was checked in September 2026. Programs move in "
    "both directions — a county can adopt a building code at any time, and "
    "trade programs transfer to and from DOPL — so re-check before you file, "
    "not just before you buy."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- method
flow += k.h2_tight("HOW TO TELL AN ENFORCING JURISDICTION FROM ONE THAT IS NOT",
                   reserve=2.2)
flow.append(k.body(
    f"No state agency publishes the answer, and the statute is why: any local "
    f"government \"may elect to implement a building code enforcement program "
    f"by passing an ordinance\" ({sec('39-4116(1)')}), so a list would be "
    f"stale the day it printed. What the statute does give you is a document "
    f"that <b>must</b> exist wherever a building permit is required."))
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp("<b>City first, then county.</b> Inside city limits the city's "
             "ordinance governs; outside, the county's. Search the city or "
             "county website for \"building permit\" and \"building "
             "department.\"")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp(f"<b>Look for the permit-process document.</b> \"A local "
             f"government that requires building permits shall make "
             f"available a document that describes in detail the "
             f"requirements of its building permit process … on its website "
             f"and in physical form upon request\" ({sec('39-4117(1)')}). "
             f"Found it: enforcing. Not found: ask for it by that section "
             f"number.")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("<b>No building department? Get it in writing.</b> A dated "
             "email from the clerk or planning office stating that no "
             "building-code ordinance has been adopted for the parcel's "
             "location. File it with the deed.")],
    [k.cellp("<b>4</b>", center=True),
     k.cellp("<b>Now the trade side, separately.</b> Open DOPL's electrical "
             "permits page and follow \"Purchase your permit on-line HERE "
             "Based on location\" — the map tells you whether DOPL or a "
             "local program issues each trade permit at your address. "
             "The three answers can differ from each other.")],
    [k.cellp("<b>5</b>", center=True),
     k.cellp("<b>Write all four answers on the cover</b> — building permit "
             "from, and electrical, plumbing and HVAC permits from — with "
             "the date you confirmed them.")],
]
flow.append(k.ref_table(
    "The five-minute method",
    [k.cellp("", bold=True, center=True), k.cellp("Step", bold=True)],
    rows, [0.35 * inch, CW - 0.35 * inch]))
flow.append(k.cite(
    f"Trade programs move. A city or county starting its own electrical or "
    f"plumbing enforcement \"shall provide the division … notice of such "
    f"decision in writing at least thirty (30) days prior to implementation\" "
    f"({sec('54-1001B(4)')}; {sec('54-2601(7)')}); one that terminates a "
    f"program hands it back, and DOPL \"shall provide … enforcement services "
    f"in the jurisdiction for a minimum of one (1) year\" "
    f"({sec('54-1001B(5)')}; {sec('54-2601(8)')}). DOPL's HVAC board news "
    f"records one going the other way: \"Canyon County HVAC Program Coming to "
    f"DOPL September 1, 2023.\" The map is current; a two-year-old forum "
    f"answer is not."))

# ---------------------------------------------------------------- DOPL
flow += k.h2_tight("DOPL — ONE OFFICE, INSPECTORS BY CITY", reserve=2.2)
flow.append(k.body(
    "The Division of Occupational and Professional Licenses runs the "
    "electrical, plumbing and HVAC programs and contractor registration from "
    "Boise — its forms say \"email or mail all license applications, permit "
    "applications, fees, or forms to the Boise office\" — and puts inspectors "
    "in the field by city and ZIP code. There are no regional permit "
    "counters. Three things to know how to find:"))
rows = [
    [k.cellp("<b>The permit</b>"),
     k.cellp("\"As of January 1, 2023, all permits will need to be purchased "
             "Online at DBS.IDAHO.GOV\" — the forms still print, but the "
             "transaction is online. Register a free account, then buy the "
             "homeowner electrical, plumbing or HVAC permit. Each trade page "
             "at dopl.idaho.gov links the purchase and the location map")],
    [k.cellp("<b>The inspector</b>"),
     k.cellp("The <b>Inspector List with Schedules</b> — linked from every "
             "trade's permit page — lists each city and ZIP with its "
             "electrical, HVAC and plumbing inspector and their inspection "
             "days. The copy read for this kit was created 5&#160;August "
             "2026; the file is re-issued and its name changes. There is no "
             "building column, because DOPL inspects no houses")],
    [k.cellp("<b>The inspection request</b>"),
     k.cellp("eTRAKiT, linked from each permit page (\"To schedule your "
             "inspection online please click HERE\"): find the permit, "
             "Request Inspection, choose the type and date. Next-day "
             "requests until 7 p.m. Mountain. Or the inspection line with "
             "the codes in ID.3")],
    [k.cellp("<b>The license check</b>"),
     k.cellp("DOPL's public search — contractor registrations, electrical "
             "licenses, plumbing and HVAC certificates, discipline — is at "
             "edopl.idaho.gov, Online Services → Public Search")],
]
flow.append(k.ref_table(
    "Finding your way around DOPL",
    [k.cellp("What you need", bold=True), k.cellp("Where it is", bold=True)],
    rows, [1.55 * inch, CW - 1.55 * inch]))

# ---------------------------------------------------------------- health districts
flow += k.h2_tight("THE SEVEN HEALTH DISTRICTS, BY COUNTY", reserve=2.4)
flow.append(k.body(
    f"Septic permits do not come from DEQ. \"Idaho's seven public health "
    f"districts administer these rules under a memorandum of understanding "
    f"(MOU) with DEQ. The public health districts conduct site evaluations, "
    f"issue septic system permits, inspect installations\" (DEQ septic page). "
    f"The districts are fixed by statute, county by county "
    f"({sec('39-408')}):"))
rows = [
    [k.cellp("<b>1</b>", center=True), k.cellp("Panhandle Health District"),
     k.cellp("Boundary, Bonner, Kootenai, Benewah, Shoshone"),
     k.cellp("panhandlehealthdistrict.org")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("Public Health – Idaho North Central District"),
     k.cellp("Latah, Clearwater, Nez Perce, Lewis, Idaho"),
     k.cellp("idahopublichealth.com")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("Southwest District Health"),
     k.cellp("Adams, Washington, Payette, Gem, Canyon, Owyhee"),
     k.cellp("swdh.org")],
    [k.cellp("<b>4</b>", center=True), k.cellp("Central District Health"),
     k.cellp("Valley, Boise, Ada, Elmore"), k.cellp("cdh.idaho.gov")],
    [k.cellp("<b>5</b>", center=True),
     k.cellp("South Central Public Health District"),
     k.cellp("Camas, Blaine, Gooding, Lincoln, Jerome, Minidoka, Twin Falls, "
             "Cassia"),
     k.cellp("phd5.idaho.gov")],
    [k.cellp("<b>6</b>", center=True),
     k.cellp("Southeastern Idaho Public Health"),
     k.cellp("Power, Oneida, Bannock, Franklin, Caribou, Bear Lake, Bingham, "
             "Butte"),
     k.cellp("siphidaho.org")],
    [k.cellp("<b>7</b>", center=True),
     k.cellp("Eastern Idaho Public Health"),
     k.cellp("Lemhi, Custer, Clark, Jefferson, Bonneville, Teton, Madison, "
             "Fremont"),
     k.cellp("eiph.idaho.gov")],
]
flow.append(k.ref_table(
    f"Idaho Code {sec('39-408')} — \"There is hereby established … seven (7) "
    f"public health districts\"",
    [k.cellp("No.", bold=True, center=True), k.cellp("District", bold=True),
     k.cellp("Counties", bold=True), k.cellp("Website", bold=True)],
    rows, [0.4 * inch, 1.75 * inch, CW - 0.4 * inch - 1.75 * inch - 1.8 * inch,
           1.8 * inch]))
flow.append(k.cite(
    "Ask your district for its septic-permit application checklist and its "
    "fee schedule: the state rule sets minimum fees and each district \"may "
    "adopt different fees … [and] must have their fee schedules published "
    "online\" (IDAPA 58.01.14.110), and the well rules note that \"additional "
    "siting and separation distance requirements are set forth by the "
    "governing district health department\" (IDAPA 37.03.09.025.01.d). The "
    "statewide separations in ID.2 are floors."))

# ---------------------------------------------------------------- two cities
flow += k.h2_tight("TWO CITIES THAT RUN THEIR OWN TRADE PROGRAMS", reserve=2.2)
flow.append(k.body(
    "Both verified from the city's own pages in September 2026. They are "
    "printed as worked examples of what a local program looks like, not as a "
    "list — DOPL's map is the list."))
rows = [
    [k.cellp("<b>Boise</b>"),
     k.cellp("Planning and Development Services, Building Division. Its fee "
             "page carries four separate schedules — <b>Building Code, "
             "Plumbing Code, Mechanical Code and Fuel Gas Code, and "
             "Electrical Code</b> (FY27) — so inside Boise all three trade "
             "permits are the city's, on the city's fees, with the city's "
             "inspectors. The Idaho electrical and plumbing codes remain the "
             "standard by statute. The city also publishes permit-processing "
             "timeframes by quarter"),
     k.cellp("cityofboise.org → Planning and Development Services → "
             "Building")],
    [k.cellp("<b>Coeur d'Alene</b>"),
     k.cellp("Building Services \"has adopted the 2018 International Codes\" "
             "and enforces \"all applicable building, mechanical, "
             "accessibility, plumbing and housing codes.\" Plumbing: "
             "\"Local plumbing codes will remain under the 2017 Idaho State "
             "Plumbing code with current City Amendments\" — a city program "
             "with its own amendments, as § 54-2601 allows after a hearing. "
             "Ask the counter which trade permits it issues itself and which "
             "go to DOPL"),
     k.cellp("cdaid.org/building")],
]
flow.append(k.ref_table(
    "Two local programs, from the cities' own pages",
    [k.cellp("City", bold=True), k.cellp("What its page says", bold=True),
     k.cellp("Where", bold=True)],
    rows, [1.05 * inch, CW - 1.05 * inch - 1.85 * inch, 1.85 * inch]))

# ---------------------------------------------------------------- sequence
flow += k.h2_tight("THE SEQUENCE, WHATEVER YOUR STATUS", reserve=2.4)
flow.append(k.body(
    "\"No building permit\" is not \"no paperwork.\" The risk is doing these "
    "in the wrong order, because two of them constrain where the house can "
    "physically sit."))
rows = [
    [k.cellp("<b>1</b>", center=True), k.cellp("<b>Confirm both statuses</b>"),
     k.cellp("Building-code status from the city or county; trade-permit "
             "authority from DOPL's map. Before relying on any of the rest")],
    [k.cellp("<b>2</b>", center=True), k.cellp("<b>Septic site evaluation</b>"),
     k.cellp("The health district. The 20% slope limit, the two-drainfield "
             "rule and the 100-ft well separation decide where the house and "
             "well can go — before the footprint is fixed")],
    [k.cellp("<b>3</b>", center=True), k.cellp("<b>Zoning and address</b>"),
     k.cellp("Local land-use approval under the Local Land Use Planning Act "
             "and a 911 address are county and city matters the building "
             "code never touched; a no-code county still has zoning "
             "setbacks. Ask the planning office")],
    [k.cellp("<b>4</b>", center=True), k.cellp("<b>Well drilling permit</b>"),
     k.cellp("IDWR, $75, before the rig arrives. Only a licensed driller may "
             "drill; find one in IDWR's licensed-driller search")],
    [k.cellp("<b>5</b>", center=True), k.cellp("<b>Building permit</b>"),
     k.cellp("If, and only if, the jurisdiction enforces a code. Its "
             "process document lists what to submit; the 10-business-day "
             "completeness clock starts at receipt")],
    [k.cellp("<b>6</b>", center=True), k.cellp("<b>Three trade permits</b>"),
     k.cellp("DOPL online, or the city or county program. Electrical before "
             "any wiring; plumbing before groundwork; HVAC with the Manual "
             "J/S/D calculations")],
    [k.cellp("<b>7</b>", center=True), k.cellp("<b>Utility</b>"),
     k.cellp("Ask what the power supplier needs before it will set a meter. "
             "By statute that includes a passed DOPL (or local) electrical "
             "inspection; decide the temporary-power route in ID.3 first")],
    [k.cellp("<b>8</b>", center=True), k.cellp("<b>Utility locate</b>"),
     k.cellp("Call 811 before any excavation. DOPL's permit page warns that "
             "the excavation portion of a permit \"may be suspended\" for a "
             "violation of Title 55, Chapter 22")],
]
flow.append(k.ref_table(
    "Eight steps, in order",
    [k.cellp("", bold=True, center=True), k.cellp("Step", bold=True),
     k.cellp("Which office, and why the order", bold=True)],
    rows, [0.35 * inch, 1.6 * inch, CW - 1.95 * inch]))

# ---------------------------------------------------------------- addresses
flow += k.h2_tight("STATE-LEVEL ADDRESSES", reserve=2.0)
flow.append(k.body(
    "All confirmed to resolve in September 2026. <b>We print no phone numbers "
    "anywhere in this kit</b> — they go stale faster than anything else on a "
    "printed page, and every office below can be reached from its own site."))
rows = [
    [k.cellp("<b>Trade permits, by location</b>"),
     k.cellp("dopl.idaho.gov/ele/ele-permits/ — \"Purchase your permit "
             "on-line HERE Based on location\" opens the map. Plumbing and "
             "HVAC: /plb/plb-permits/ and /hvac/hvac-permits/")],
    [k.cellp("<b>Buy the permit, request inspections</b>"),
     k.cellp("dbs.idaho.gov — the online permitting system named on every "
             "DOPL form; eTRAKiT is linked from each permit page")],
    [k.cellp("<b>Inspector by city</b>"),
     k.cellp("\"Inspector List with Schedules\" — linked from "
             "dopl.idaho.gov/plb/plb-permits/ and the other trade pages")],
    [k.cellp("<b>Check a registration or license</b>"),
     k.cellp("edopl.idaho.gov/OnlineServices/?link=PubSearch")],
    [k.cellp("<b>Building Code Board; rulemaking status</b>"),
     k.cellp("dopl.idaho.gov/bld/bld-statutes-and-rules/")],
    [k.cellp("<b>Septic — the rules, and your district</b>"),
     k.cellp("deq.idaho.gov/water-quality/wastewater/septic-and-septage/ "
             "(\"Find Your Public Health District\"); district sites above")],
    [k.cellp("<b>Wells — permit, drillers, well logs</b>"),
     k.cellp("idwr.idaho.gov/wells/ and idwr.idaho.gov/wells/well-construction/ "
             "(licensed-driller search, well-log search)")],
    [k.cellp("<b>The statutes</b>"),
     k.cellp("legislature.idaho.gov/statutesrules/idstat/ — Title 39, "
             "Chapter 41 (building); Title 54, Chapters 10, 26, 50, 52; "
             "Title 42 (wells)")],
    [k.cellp("<b>The rules</b>"),
     k.cellp("adminrules.idaho.gov/rules/current/24/243930.pdf (building), "
             "243910.pdf (electrical), 243920.pdf (plumbing), 243970.pdf "
             "(HVAC); /58/580103.pdf (septic); /37/370309.pdf (wells)")],
]
# 1.7in label column. The widest single token in the right column is
# "edopl.idaho.gov/OnlineServices/?link=PubSearch" (~215pt at 9.5pt) and the
# widest line "deq.idaho.gov/water-quality/wastewater/septic-and-septage/"
# (~270pt); the right column at CW-1.7in = 382pt clears both without a
# mid-token split. Measured at 9.5pt, the "cell" style, not the 9pt note.
flow.append(k.ref_table(
    "Verified September 2026",
    [k.cellp("What you need", bold=True), k.cellp("Where", bold=True)],
    rows, [1.7 * inch, CW - 1.7 * inch]))
flow.append(k.cite(
    "<b>One address people will hand you that is dead:</b> dbs.idaho.gov's "
    "old \"building program\" page, from before the Division of Building "
    "Safety was folded into DOPL, now redirects to DOPL's home page. The "
    "legacy statement that DBS enforced the code in unincorporated areas is "
    "gone with it; DOPL's Plan Review Application is the current word."))

# ---------------------------------------------------------------- write-in
# 2.2in, not 1.6: the first write-in row here is three lines of text plus a
# field line, so the table's first chunk (title, header, row) needs ~2in, and
# at 1.6in and again at 2.0in the heading was stranded alone at the foot of
# the addresses page with the table on the next. 2.2in moves the heading with
# it; the whole eight-row table then fits one page with the closing note.
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT",
                   reserve=2.2)
flow += k.check_table(
    "Every office that touches this build, confirmed and dated",
    [
        ("Building-code status of my CITY and my COUNTY, where I found the "
         "§ 39-4117(1) document or the written statement that there is "
         "none, and the building permit office (if any) with the code "
         "edition it reviews to:",
         [("City", 0.34), ("County", 0.33), ("Date", 0.33),
          ("Office", 0.6), ("Edition", 0.4)]),
        ("Electrical, plumbing and HVAC permits from (DOPL or local), per "
         "the map; my DOPL inspectors from the Inspector List, and their "
         "days:",
         [("Elec.", 0.25), ("Plb.", 0.25), ("HVAC", 0.25), ("Date", 0.25),
          ("Inspectors / days", 1.0)]),
        ("Public health district No. ___ and the office I file the septic "
         "application with:", [("Office", 1.0)]),
        ("Zoning / planning office and its setbacks; 911 addressing office; "
         "floodplain administrator and whether the parcel is in a mapped "
         "hazard area:",
         [("Zoning", 0.25), ("Setbacks", 0.25), ("911", 0.25),
          ("Flood: in / out", 0.25)]),
        ("Driveway approach or encroachment permit — which road authority "
         "owns the road I touch — and the date I called 811 before "
         "excavating:", [("Authority", 0.6), ("811 called", 0.4)]),
        ("Electric utility or co-op, and what it needs before setting a "
         "meter:", [("Utility", 0.5), ("Requires", 0.5)]),
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "id-permit-kit",
                       "ID.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
