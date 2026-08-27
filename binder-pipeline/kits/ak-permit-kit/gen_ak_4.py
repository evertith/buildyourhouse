#!/usr/bin/env python3
"""AK.4 Where to File Directory — Alaska.

The design problem this document solves: Michigan publishes a Statewide
Jurisdiction List that answers "who enforces here?" for every unit of
government in the state. ALASKA PUBLISHES NO SUCH LIST. There is no single
document, state or private, that tells an owner-builder whether their parcel
has a building authority. So this document cannot be a lookup table — it has
to be a PROCEDURE, plus the state-level facts that are fixed regardless of the
answer, plus a directory the reader fills in.

REVISED AFTER FIRST DRAFT: the first draft printed NO jurisdiction table at
all and said so in a callout, on the reasoning that a table goes stale. Late
research verified the map jurisdiction by jurisdiction from each government's
own code, so the document now prints it WITH A DATE ON IT, framed as "a
starting point for question 3, not a substitute for it." The five questions
remain the spine because they cannot go stale; the table earns its place
because a reader deserves to know what to expect before they call.

Key verified findings now printed: Anchorage is on the 2024 IRC (AMC
23.05.010, AO 2026-33, April 2026) — NOT the 2018 edition still quoted
everywhere online; Juneau moved to the 2024 IRC in October 2025; adopted
editions across the state span FIFTEEN YEARS, 2009 to 2024; the borough/city
split is the #1 buyer error and FNSB states it in a quotable sentence; the
Fire Marshal's deferred-jurisdiction list names CITIES and transfers FIRE plan
review only — an authority that never reached a three-plex-or-smaller house.
City of Bethel could not be verified either way and is deliberately omitted.

Verified sources:
  AS 18.70.080(a)(2)   Fire Marshal standards reach residential buildings of
                       four or more dwelling units
  13 AAC 50.020        2021 IBC adopted; Section 101.2 Exception 1 excludes
                       detached one-, two-, and three-family dwellings
  AS 18.60.735         communities under 2,500 population exempt from the
                       state plumbing chapter; municipalities may set
                       standards "no less stringent"
  AS 18.60.590(b)      municipalities and rural electrification associations
                       may prescribe electrical standards "not less stringent"
  8 AAC 70.010/.090(4) state electrical inspection covers public structures
                       and places of employment
  18 AAC 72            DEC onsite wastewater, statewide or delegated locally
  AS 29.35.010         general powers of a municipality (borough/city split)
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

FORM_ID = "AK.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Alaska's hardest question is whether anyone regulates your parcel at "
    "all. No published list answers it, so this document gives you the five "
    "questions that do — and a page to write down what you confirmed.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- no list
flow += k.h2_tight("THERE IS NO LIST — AND THAT IS THE FINDING")
flow.append(k.body(
    "In most states, an owner-builder's first task is to find the right "
    "counter. In Alaska it is to find out whether a counter exists. Several "
    "states publish a jurisdiction list that answers this parcel by parcel. "
    "<b>Alaska publishes nothing of the kind</b>, for a reason that is "
    "structural rather than administrative: the state never took the power "
    "to regulate houses in the first place, so it has nothing to delegate "
    "and no register of who has taken it up."))
flow.append(k.body(
    "The Department of Public Safety's authority to set building standards "
    "runs to \"<i>buildings used for residential purposes containing <b>four "
    "or more dwelling units</b></i>,\" and the code it adopts excludes "
    "\"<i>Detached one-, two-, and three-family dwellings</i>\" in terms. "
    "Below that line, whether your house is reviewed is entirely a question "
    "of what your borough or city has chosen to do — and boroughs and cities "
    "are separate governments with separate answers on the same map."))
flow.append(k.cite(
    "AS 18.70.080(a)(2); 13 AAC 50.020, adopting the International Building "
    "Code 2021 edition, Section 101.2 Exception 1. Read at akleg.gov, "
    "August 2026."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "The single most expensive mistake in Alaska owner-building", [
        Paragraph("<b>The borough and the city are different governments, "
                  "and on this question they usually give different "
                  "answers.</b> In the Fairbanks North Star Borough, the "
                  "Matanuska-Susitna Borough, the Kenai Peninsula Borough, "
                  "the Ketchikan Gateway Borough and the Kodiak Island "
                  "Borough, the <b>borough has no building code</b> and "
                  "<b>cities inside it do</b>. A parcel two miles apart can "
                  "face a full plan review or none at all.", S["body"]),
        Paragraph("The Fairbanks North Star Borough states the pattern more "
                  "cleanly than any summary could: \"<i>Building permits are "
                  "only required within the City of Fairbanks and City of "
                  "North Pole. Since the FNSB has not adopted a building "
                  "code, building permits are not required in the Borough "
                  "at-large outside of these two cities.</i>\" Establish "
                  "which side of a city line your parcel sits on <b>from the "
                  "borough parcel viewer, not from your mailing "
                  "address</b> — a rural address routinely carries a nearby "
                  "city's name while the lot sits outside it.", S["body"]),
    ]))

# ---------------------------------------------------------------- five questions
flow += k.h2_tight("THE FIVE QUESTIONS THAT SETTLE YOUR PARCEL")
flow.append(k.body(
    "Ask them in this order. Each one changes which office you ask next, and "
    "the answers together determine everything in AK.2 and AK.3."))

q_rows = [
    [k.cellp("<b>1</b>"),
     k.cellp("<b>Which borough is the parcel in — or is it in the "
             "unorganized borough?</b>"),
     k.cellp("Organized boroughs cover a minority of Alaska's land area. If "
             "you are in the unorganized borough there is no borough "
             "government at all, and the questions below collapse to the "
             "state and federal ones.")],
    [k.cellp("<b>2</b>"),
     k.cellp("<b>Is the parcel inside a city's limits?</b>"),
     k.cellp("This is the question people get wrong, because a rural mailing "
             "address often carries a nearby city's name while the parcel "
             "sits outside it. A city can enforce a full building code inside "
             "a borough that enforces none. Confirm from the parcel viewer, "
             "not the mailing address.")],
    [k.cellp("<b>3</b>"),
     k.cellp("<b>Does that borough or city issue a building permit for a "
             "single-family dwelling — and under which code edition?</b>"),
     k.cellp("Ask both governments separately, and ask for the <i>edition</i> "
             "in writing. Local adoptions differ from each other and from the "
             "state minimums, and buying the wrong code book is an expensive "
             "way to find out.")],
    [k.cellp("<b>4</b>"),
     k.cellp("<b>Is your community at or above 2,500 population?</b>"),
     k.cellp("At or above it, the state plumbing code applies to your new "
             "construction and the Department of Labor inspects — including "
             "on parcels with no building department whatsoever. Below it, "
             "the community is exempt from the chapter outright.")],
    [k.cellp("<b>5</b>"),
     k.cellp("<b>Who regulates onsite wastewater here — DEC, or a delegated "
             "local program?</b>"),
     k.cellp("On a parcel with no building department this is normally the "
             "only mandatory approval of the entire build, and it has the "
             "longest lead time. Establish the office before you pay anyone "
             "for a soils test.")],
]
flow.append(k.ref_table(
    "Work these in order, and write the answers into the directory below",
    [k.cellp("", bold=True), k.cellp("Question", bold=True),
     k.cellp("Why it decides what happens next", bold=True)],
    q_rows, [0.35 * inch, 1.95 * inch, CW - 2.3 * inch]))
flow.append(k.cite(
    "AS 18.60.735 — \"<i>An organized municipality or unorganized village "
    "having less than 2,500 population is exempt from the provisions of "
    "AS 18.60.705 — 18.60.740</i>\"; 18 AAC 72 for onsite wastewater. "
    "Municipalities may set standards \"<i>no less stringent</i>\" than the "
    "state's for plumbing (AS 18.60.735) and electrical work "
    "(AS 18.60.590(b)) — so a local answer can be stricter than the state "
    "one, never weaker."))

# ---------------------------------------------------------------- the map
flow += k.h2_tight("THE MAP AS IT STOOD IN AUGUST 2026")
flow.append(k.body(
    "Below is what each of these governments was doing when this edition was "
    "compiled, read from each one's own code or published page. <b>It is a "
    "starting point for question 3, not a substitute for it.</b> An assembly "
    "can adopt or repeal a code in one session, and two of the entries below "
    "changed within the last year — so use this to know what to expect, and "
    "the five questions to know what is true."))

j_yes = [
    [k.cellp("<b>Anchorage</b>"), k.cellp("<b>2024</b> IRC"),
     k.cellp("AMC 23.05.010; local amendments AMC ch. 23.85. Adopted April "
             "2026 — <b>not the 2018 edition still quoted online</b>. NEC "
             "2023.")],
    [k.cellp("<b>Juneau</b>"), k.cellp("<b>2024</b> IRC"),
     k.cellp("CBJ 19.04.R010.1, effective October 2025. NEC 2023. Note CBJ "
             "19.04.R010.2 pulls in the fire code's <b>apparatus access</b> "
             "provisions — a real gate on a rural lot.")],
    [k.cellp("<b>Kenai</b>"), k.cellp("<b>2021</b> IRC"),
     k.cellp("KMC 4.32.010, amendments KMC 4.32.015 — heavy: 70&nbsp;psf ground "
             "snow, 42&nbsp;in. frost depth, −18 °F winter design, sprinklers "
             "deleted.")],
    [k.cellp("<b>Seward</b>"), k.cellp("<b>2021</b> IRC"),
     k.cellp("SCC 12.05.021. SCC 12.01.025 makes a water/sewer receipt a "
             "prerequisite to any building, electrical or plumbing permit.")],
    [k.cellp("<b>Sitka</b>"), k.cellp("<b>2021</b> IRC"),
     k.cellp("Plus 2021 UPC and 2020 NEC. Published design criteria: 150&nbsp;mph "
             "wind, 50&nbsp;psf ground snow, 18&nbsp;in. minimum frost depth.")],
    [k.cellp("<b>Fairbanks</b> (city)"), k.cellp("<b>2018</b> IRC"),
     k.cellp("FGC 10-401. NEC 2020. The borough around it issues nothing — "
             "see below.")],
    [k.cellp("<b>North Pole</b>"), k.cellp("<b>2018</b> IRC"),
     k.cellp("NPMC Title 15.")],
    [k.cellp("<b>Palmer</b>"), k.cellp("<b>2015</b> IRC"),
     k.cellp("PMC 15.12.010, amendments PMC 15.16. PMC 15.12.020 lets the "
             "building official modify provisions on written application "
             "\"<i>when there are practical difficulties</i>.\"")],
    [k.cellp("<b>Ketchikan</b> (city)"), k.cellp("<b>2012</b> IRC"),
     k.cellp("KMC Title 19. The city's own handout limits the IRC to "
             "single-family and duplex; triplex and larger go to the IBC.")],
    [k.cellp("<b>Kodiak</b> (city)"), k.cellp("<b>2012</b> IRC"),
     k.cellp("KCC 14.04.010. Its amendments delete the IRC plumbing and "
             "electrical chapters in favor of the UPC and NEC.")],
    [k.cellp("<b>Soldotna</b>"), k.cellp("<b>2012</b> IRC"),
     k.cellp("SMC 15.07.010. Adopts other codes expressly \"<i>with all "
             "revisions in 13 AAC 50.020</i>\" — state amendments layered on "
             "a local edition.")],
    [k.cellp("<b>Valdez</b>"), k.cellp("<b>2009</b> IRC"),
     k.cellp("VMC 15.06.010. Permit expiry extended to 360 days. Ask about "
             "VMC 15.06.070's amendment naming <i>each contractor</i> as the "
             "permit applicant — it matters to an owner-builder.")],
    [k.cellp("<b>Nome</b>"), k.cellp("<b>2009</b> IRC"),
     k.cellp("Nome Code ch. 5.10. \"A permit is required for all new "
             "construction.\"")],
]
flow.append(k.ref_table(
    "Issues residential building permits — and the edition it enforces",
    [k.cellp("Jurisdiction", bold=True), k.cellp("Residential code", bold=True),
     k.cellp("Citation and what to watch", bold=True)],
    j_yes, [1.25 * inch, 1.0 * inch, CW - 2.25 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "Fifteen years of code editions are in force in Alaska simultaneously",
    [
        Paragraph("Look down that middle column: <b>2009 in Valdez and Nome, "
                  "2012 in Ketchikan, Kodiak and Soldotna, 2015 in Palmer, "
                  "2018 in Fairbanks and North Pole, 2021 in Kenai, Seward "
                  "and Sitka, 2024 in Anchorage and Juneau.</b> There is no "
                  "state cycle pulling them together, so a builder moving "
                  "between two Alaska towns is working to codes fifteen "
                  "years apart.", S["body"]),
        Paragraph("Anchorage and Juneau both moved to the 2024 codes very "
                  "recently — Anchorage in April 2026, Juneau in October "
                  "2025. That is precisely why the \"Anchorage uses the 2018 "
                  "IRC\" claim is still circulating in guides and forums. "
                  "<b>Buy the code book after you confirm the edition, not "
                  "before.</b>", S["body"]),
    ]))

flow.append(Spacer(1, 8))
j_no = [
    [k.cellp("<b>Fairbanks North Star Borough</b>"),
     k.cellp("No building code, no building permit outside the two cities — "
             "the borough says so in terms. Does run a <b>floodplain "
             "permit</b> and service-area driveway and right-of-way "
             "permits.")],
    [k.cellp("<b>Matanuska-Susitna Borough</b>"),
     k.cellp("No building permit exists. Does require a <b>driveway "
             "permit</b> on a borough road, a <b>floodplain development "
             "permit</b> in a mapped hazard area (MSB 17.29), an address "
             "request, and encroachment and utility permits. See the trap "
             "below.")],
    [k.cellp("<b>Kenai Peninsula Borough</b>"),
     k.cellp("No building code — its Title 18 \"Buildings and Construction\" "
             "contains only local-hire and public-works-contract chapters. "
             "Does set <b>building setbacks</b> (KPB 20.30) and issues "
             "driveway, encroachment and near-water permits.")],
    [k.cellp("<b>Ketchikan Gateway Borough</b>"),
     k.cellp("No building permit; issues a <b>zoning permit</b> \"<i>for most "
             "new construction</i>,\" plus floodplain and driveway permits. "
             "City of Ketchikan residents need both.")],
    [k.cellp("<b>Kodiak Island Borough</b>"),
     k.cellp("No borough building permit; issues zoning compliance permits "
             "and refers building permits to the City of Kodiak. Whether the "
             "city inspects outside city limits — <b>confirm locally</b>.")],
    [k.cellp("<b>City of Wasilla</b>"),
     k.cellp("No building code. But a <b>land use administrative permit</b> "
             "is required \"<i>before the construction, alteration, addition, "
             "or modification of a building</i>\" (WMC 16.90.010.B), with an "
             "as-built survey after any structure over 250&nbsp;sq&nbsp;ft. Owner-"
             "friendly detail: you may draw your own site plan.")],
    [k.cellp("<b>City of Homer</b>"),
     k.cellp("States it plainly: \"<i>The City of Homer does not have a "
             "building inspection program and does not issue building "
             "permits.</i>\" Issues a zoning permit, driveway permit and "
             "water/sewer permit instead.")],
    [k.cellp("<b>North Slope Borough</b>"),
     k.cellp("No building code found; the residential gate is a "
             "<b>District Residential Permit</b> covering \"<i>digging for "
             "foundation and building homes</i>.\" Confirm locally.")],
    [k.cellp("<b>Unorganized borough</b>"),
     k.cellp("No local government at all, so no building permit, no zoning "
             "and no local plan review. Only the state and federal gates in "
             "this kit apply.")],
]
flow.append(k.ref_table(
    "Issues no residential building permit — and what it requires instead",
    [k.cellp("Jurisdiction", bold=True),
     k.cellp("What applies instead", bold=True)],
    j_no, [1.9 * inch, CW - 1.9 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "Two Mat-Su traps, one of them a permit you do not need", [
        Paragraph("<b>The \"Borough Land Use Permit\" is not a zoning permit "
                  "for your house.</b> It authorizes commercial or private "
                  "use of unimproved <i>borough-owned</i> land, carries "
                  "liability insurance and a security deposit, and is "
                  "administered by the Land Management Division. Building on "
                  "your own lot, you do not need one — and people apply for "
                  "it anyway because the name sounds like the thing they are "
                  "looking for.", S["body"]),
        Paragraph("<b>The driveway permit depends on whose road it is.</b> "
                  "The borough permits a tie-in to a <i>borough</i> road; a "
                  "state-maintained road is Alaska DOT&amp;PF; a private road "
                  "needs neither but does need your easement. The borough's "
                  "own guidance is to confirm jurisdiction before applying.",
                  S["body"]),
    ]))
flow.append(k.cite(
    "Adopted editions and permit status read from each jurisdiction's own "
    "municipal code or published page, August 2026: Anchorage AMC 23.05.010 "
    "and ch. 23.85; Juneau CBJ 19.04.R010.1–.2; Kenai KMC 4.32.010, .015; "
    "Seward SCC 12.05.021, 12.01.025; Sitka published design criteria; "
    "Fairbanks FGC 10-401; North Pole NPMC Title 15; Palmer PMC 15.12.010, "
    ".020; Ketchikan KMC Title 19; Kodiak KCC 14.04.010; Soldotna SMC "
    "15.07.010; Valdez VMC 15.06.010, .070; Nome Code ch. 5.10; Kenai "
    "Peninsula Borough Title 18 and 20.30; Mat-Su MSB 17.29; Wasilla WMC "
    "16.90.010, .020. <b>The City of Bethel could not be verified either "
    "way</b> and is deliberately omitted rather than guessed at. Two "
    "jurisdictions' trade-code editions were also unverifiable — Seward's "
    "plumbing and electrical editions are adopted as \"the city designated "
    "edition\" with no year in the code, and Palmer's non-residential "
    "editions were not confirmed. Ask."))

# ---------------------------------------------------------------- deferred
flow += k.h2_tight("THE DEFERRED-JURISDICTION LIST, AND WHAT IT IS NOT")
flow.append(k.body(
    "The State Fire Marshal publishes a list of <b>deferred jurisdictions</b> "
    "— governments that have taken over fire and life safety plan review "
    "from the state under AS 18.70.080. You will find this list, and you will "
    "be tempted to read it as \"the places with building departments.\" "
    "<b>It is not that list</b>, and the difference matters."))
flow.append(k.body(
    "As it stood in August 2026 it named thirteen entries: <b>Anchorage Fire "
    "Department, Anchorage Building Safety, City of Palmer, Juneau, "
    "Fairbanks, Kenai, Ketchikan, Seward, Kodiak, Sitka, Soldotna, "
    "University of Alaska Fairbanks,</b> and <b>Central Mat-Su Fire Service "
    "Area</b>. Read it carefully: the entries are <b>cities</b>, not "
    "boroughs — \"Fairbanks\" is the city, not the borough around it; "
    "\"Kodiak\" is the city, not the island borough. One entry is a "
    "university and one is a fire service area."))
flow.append(k.callout(
    "Deferral moves fire plan review, not your building permit", [
        Paragraph("The Fire Marshal's own page states the underlying rule "
                  "and its exemption together: \"<i>Construction, repair, "
                  "remodel, addition, or change of occupancy of any building "
                  "or structure … must be approved by the State Fire Marshal "
                  "before any work begins</i>,\" and then — \"<i><b>Residential "
                  "housing that is three-plex or smaller is exempt from this "
                  "requirement.</b></i>\"", S["body"]),
        Paragraph("So deferral transfers an authority that <b>never reached "
                  "your house in the first place</b>. A jurisdiction can be "
                  "on that list and still issue you no building permit, and "
                  "the Central Mat-Su Fire Service Area is exactly that "
                  "case — it holds deferred fire plan review inside a borough "
                  "that issues no building permits at all.", S["body"]),
    ]))
flow.append(k.cite(
    "Alaska Department of Public Safety, Division of Fire and Life Safety, "
    "Plan Review — <b>dps.alaska.gov</b> → Divisions → Fire and Life Safety "
    "→ Plan Review, read August 2026. Authority stated on that page: "
    "AS 18.70.080 and 13 AAC 50.027."))

# ---------------------------------------------------------------- fixed
flow += k.h2_tight("WHAT IS FIXED NO MATTER HOW THOSE QUESTIONS COME OUT")
flow.append(k.body(
    "Three things do not depend on your borough at all. They are the reason "
    "\"nobody regulates my parcel\" is never quite true, and they are the "
    "part of Alaska that catches out people who have checked only with their "
    "borough."))

fixed_rows = [
    [k.cellp("<b>Smoke and CO alarms</b>"),
     k.cellp("Required in <b>every dwelling unit in the state</b>, by "
             "statute, enforced as a class B misdemeanor. Detail in AK.2."),
     k.cellp("AS 18.70.095")],
    [k.cellp("<b>The 2020 NEC</b>"),
     k.cellp("The state minimum electrical code. Your single-family house is "
             "not inspected by the State — but the standard still applies "
             "and knowing violation is a misdemeanor. AK.1."),
     k.cellp("8 AAC 70.025(a)")],
    [k.cellp("<b>Onsite wastewater</b>"),
     k.cellp("DEC regulates statewide except where it has delegated the "
             "program locally. No borough opts out of this. AK.2, Step 2."),
     k.cellp("18 AAC 72")],
]
flow.append(k.ref_table(
    "Applies on every parcel in Alaska",
    [k.cellp("What", bold=True), k.cellp("Where it comes from", bold=True),
     k.cellp("Authority", bold=True)],
    fixed_rows, [1.35 * inch, CW - 1.35 * inch - 1.35 * inch, 1.35 * inch]))

# ---------------------------------------------------------------- offices
flow += k.h2_tight("THE OFFICES THAT APPLY WITH OR WITHOUT A BUILDING PERMIT")
flow.append(k.body(
    "Where no building department assembles these for you, this is the list "
    "nobody hands you. Each is a different government, and several will not "
    "know the others exist."))

find_rows = [
    [k.cellp("<b>Onsite wastewater</b>"),
     k.cellp("Alaska DEC — <b>dec.alaska.gov</b> → Water → Wastewater → "
             "Onsite — or the delegated borough or municipal program. Ask "
             "which one covers your parcel <i>before</i> commissioning any "
             "soils work.")],
    [k.cellp("<b>Plumbing and gas permits,<br/>certificates of fitness, "
             "boilers</b>"),
     k.cellp("Alaska Department of Labor and Workforce Development, Labor "
             "Standards and Safety Division, <b>Mechanical Inspection "
             "Section</b> — <b>labor.alaska.gov</b> → Labor Standards and "
             "Safety → Mechanical Inspection. This is the state office an "
             "Alaska owner-builder is most likely to meet.")],
    [k.cellp("<b>Contractor registration</b>"),
     k.cellp("Division of Corporations, Business and Professional Licensing "
             "— <b>commerce.alaska.gov</b> → Professional Licensing → "
             "Construction Contractors. Also where the AS 08.18.161(11) "
             "owner-builder notice is filed, and where you verify anyone you "
             "hire.")],
    [k.cellp("<b>Zoning, land use, platting,<br/>911 addressing</b>"),
     k.cellp("Your borough's planning department, and your city's if the "
             "parcel is inside one. <b>These exist in Alaska boroughs with "
             "no building code at all</b> — never assume no building permit "
             "means no permit.")],
    [k.cellp("<b>Driveway / access</b>"),
     k.cellp("Alaska Department of Transportation and Public Facilities — "
             "<b>dot.alaska.gov</b> — for a tie-in to a state-maintained "
             "road; otherwise the borough, the city, or the road "
             "association that maintains it.")],
    [k.cellp("<b>Floodplain</b>"),
     k.cellp("Your community's floodplain administrator, usually in the "
             "borough or city planning office. State coordination sits with "
             "the Division of Community and Regional Affairs at "
             "<b>commerce.alaska.gov</b>.")],
    [k.cellp("<b>Wetlands</b>"),
     k.cellp("U.S. Army Corps of Engineers, <b>Alaska District</b> — a "
             "federal permit, entirely independent of anything the state or "
             "your borough says. Ask at the site-planning stage.")],
    [k.cellp("<b>Water rights and well logs</b>"),
     k.cellp("Alaska Department of Natural Resources, Division of Mining, "
             "Land and Water — <b>dnr.alaska.gov</b>. Ordinary single-family "
             "domestic use normally needs no water right; confirm rather "
             "than assume.")],
    [k.cellp("<b>Fire and life safety</b>"),
     k.cellp("State Fire Marshal, Division of Fire and Life Safety, "
             "Department of Public Safety — <b>dps.alaska.gov</b>. Plan "
             "review reaches four or more dwelling units, but the statewide "
             "smoke-alarm standard is theirs and it reaches you.")],
    [k.cellp("<b>Energy standard and financing</b>"),
     k.cellp("Alaska Housing Finance Corporation — <b>ahfc.us</b> — for the "
             "state energy standard and its loan programs, plus whatever "
             "your own lender imposes. Where no government reviews your "
             "house, this is the layer that does.")],
    [k.cellp("<b>Electric utility</b>"),
     k.cellp("Your cooperative or utility sets its own conditions for "
             "energizing a new service, and in unincorporated Alaska that is "
             "frequently the only technical review your wiring will get. Ask "
             "before you set the meter base.")],
]
flow.append(k.ref_table(
    "Finding the right office for your parcel",
    [k.cellp("What you need", bold=True),
     k.cellp("Who has it, and how to get there", bold=True)],
    find_rows, [1.7 * inch, CW - 1.7 * inch]))

# ---------------------------------------------------------------- directory
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT")
flow.append(k.body(
    "Confirm each of these by phone rather than copying it from a search "
    "result, and write down the name of the person you spoke to. In a small "
    "Alaska office a name is worth more than a number, and the same person "
    "will still be there when you call back in April. Phone numbers are left "
    "blank deliberately — a wrong number printed in a kit is worse than no "
    "number."))

flow.append(Spacer(1, 4))
flow.append(Paragraph("<b>THE FIVE ANSWERS</b>", S["body"]))
flow.append(d.FillInRow([("Borough (or Unorganized):", 0.5),
                         ("Inside a city? Which:", 0.5)]))
flow.append(d.FillInRow([("Building permit required? Y / N:", 0.42),
                         ("By whom:", 0.3), ("Code edition:", 0.28)]))
flow.append(d.FillInRow([("Community population:", 0.34),
                         ("State plumbing? Y / N:", 0.33),
                         ("Confirmed:", 0.33)]))
flow.append(d.FillInRow([("Wastewater regulated by:", 0.6),
                         ("Confirmed:", 0.4)]))
flow.append(Spacer(1, 8))


def office_block(label, sub):
    """One office: department and phone, then portal plus who and when."""
    return [
        Paragraph(f"<b>{label}</b> — <font size=9.5>{sub}</font>", S["body"]),
        d.FillInRow([("Office / department:", 0.62), ("Phone:", 0.38)]),
        d.FillInRow([("Portal / address:", 0.44), ("Spoke with:", 0.34),
                     ("Confirmed:", 0.22)]),
        Spacer(1, 4),
    ]


for label, sub in [
    ("BUILDING PERMIT", "borough or city — or write NONE, and note who you "
     "asked"),
    ("WASTEWATER", "DEC or the delegated local program — start here"),
    ("PLUMBING &amp; GAS", "state Mechanical Inspection where the community "
     "is 2,500 or more"),
    ("ZONING / LAND USE", "setbacks, use, waterfront setbacks — exists "
     "without a building code"),
    ("911 ADDRESSING", "borough or city — needed before utilities"),
    ("DRIVEWAY / ACCESS", "DOT&amp;PF on a state road, otherwise borough, "
     "city or road association"),
    ("FLOODPLAIN", "community floodplain administrator, if in a mapped "
     "hazard area"),
    ("ELECTRIC UTILITY", "temporary construction power, and conditions for "
     "energizing"),
    ("LENDER", "construction standard, draw inspections, energy requirement"),
]:
    flow += office_block(label, sub)

# ---------------------------------------------------------------- state
flow += k.h2_tight("STATE-LEVEL CONTACTS")
flow.append(k.body(
    "These are stable and worth knowing. Navigation routes are given rather "
    "than deep links, because Alaska agency URLs move and a domain plus a "
    "route survives a redesign."))

state_rows = [
    [k.cellp("<b>Labor and Workforce Development</b><br/>"
             "<font size=9>Mechanical Inspection Section</font>"),
     k.cellp("Plumbing and gas permits and inspections where the community "
             "is 2,500 or more; electrical inspection at three-plex and "
             "above; certificates of fitness; boilers and pressure vessels. "
             "The state office you are most likely to deal with."),
     k.cellp("labor.alaska.gov")],
    [k.cellp("<b>Commerce, Community, and Economic Development</b><br/>"
             "<font size=9>Corporations, Business and Professional "
             "Licensing</font>"),
     k.cellp("Contractor registration and the residential contractor "
             "endorsement; the free license search you use before hiring "
             "anyone; the owner-builder notice under AS 08.18.161(11)."),
     k.cellp("commerce.alaska.gov")],
    [k.cellp("<b>Environmental Conservation</b><br/>"
             "<font size=9>Division of Water</font>"),
     k.cellp("Onsite wastewater under 18 AAC 72, and the list of local "
             "programs to which it has delegated review. Drinking water "
             "guidance for private wells."),
     k.cellp("dec.alaska.gov")],
    [k.cellp("<b>Public Safety</b><br/>"
             "<font size=9>Fire and Life Safety / State Fire Marshal</font>"),
     k.cellp("Plan review for buildings of four or more dwelling units and "
             "non-residential occupancies; the statewide smoke-alarm "
             "installation standard that reaches every dwelling in Alaska."),
     k.cellp("dps.alaska.gov")],
    [k.cellp("<b>Alaska Housing Finance Corporation</b>"),
     k.cellp("The state residential energy standard and the loan and rebate "
             "programs that carry it. Where no government reviews your "
             "house, an AHFC-backed loan is often what does."),
     k.cellp("ahfc.us")],
    [k.cellp("<b>Natural Resources</b><br/>"
             "<font size=9>Mining, Land and Water</font>"),
     k.cellp("Water rights and the well log database — useful before you "
             "drill, to see what neighboring wells found and at what depth."),
     k.cellp("dnr.alaska.gov")],
    [k.cellp("<b>Transportation and Public Facilities</b>"),
     k.cellp("Driveway and approach permits where you tie into a "
             "state-maintained road."),
     k.cellp("dot.alaska.gov")],
    [k.cellp("<b>Alaska Legislature</b>"),
     k.cellp("The statutes and the Administrative Code themselves, free and "
             "current — every AS and AAC citation in this kit was read "
             "here. Bills &amp; Laws → Alaska Statutes, or → Alaska "
             "Administrative Code."),
     k.cellp("akleg.gov")],
]
flow.append(k.ref_table(
    "State agencies and what each is actually for",
    [k.cellp("Agency", bold=True),
     k.cellp("Why you would contact them", bold=True),
     k.cellp("Website", bold=True)],
    # "commerce.alaska.gov" is 104pt at 9.5pt and the cell eats ~8pt of
    # padding, so 1.45in broke it to "commerce.alaska.g / ov".
    state_rows, [1.8 * inch, CW - 1.8 * inch - 1.6 * inch, 1.6 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026). The Fire Marshal's residential "
    "authority and the four-dwelling-unit line: AS 18.70.080(a)(2), and "
    "13 AAC 50.020 adopting the 2021 IBC with Section 101.2 Exception 1 "
    "excluding detached one-, two- and three-family dwellings. The 2,500 "
    "population line for the state plumbing chapter: AS 18.60.735. Local "
    "standards may be no less stringent than the state's: AS 18.60.735 "
    "(plumbing) and AS 18.60.590(b) (electrical). State electrical "
    "inspection scope: 8 AAC 70.010 with the definition of \"public "
    "structure\" at 8 AAC 70.090(4). Onsite wastewater: 18 AAC 72. Agency "
    "scope descriptions confirmed against each agency's own pages, read "
    "August 2026. Statutes and regulations at akleg.gov."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ak-permit-kit",
                       "AK.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
