#!/usr/bin/env python3
"""NE.2 Permit Application Checklist.

Every Nebraska claim in this document was read against its primary source in
September 2026 and is cited on-page.

The organizing idea: Nebraska has no statewide building-permit statute for a
house — no application contents, no plan-review clock, no permit life, no
certificate of occupancy rule. Those exist only where a city or county chose to
create them. So this document is built around the things the STATE does fix,
which apply on every parcel: the code editions, the electrical request and its
fees, the energy values, the radon standard, the septic and well packages.
The local building permit gets a write-in, not a guess.

Verified sources:
  § 71-6403(1)          2018 IBC / IRC (less R313, ch. 25-33) / IEBC / UPC
  § 81-2104(5)          2023 NEC; 2017 text for 210.8(A), 210.8(A)(3),
                        210.8(A)(5), 230.67(A), 230.85
  SED adoption notice   "Beginning August 1st, 2024 … NFPA 70 … 2023"
  § 81-1609(9), -1611, -1614  2018 IECC, statewide, from July 1, 2020
  DWEE Residential Energy Code Fact Sheet   "unamended 2018 IECC"; the
                        prescriptive table; 3 ACH50; ducts; Manual J
  DWEE Energy Impact Study   "entire state of Nebraska in a single climate
                        zone (5)"
  § 76-3504, -3505, -3506, -3507   RRNC standards, exemptions, conversion
  DHHS report to the Legislature, Jan 1 2024   77 of 93 counties above 2.7;
                        the 14 below; Hall at exactly 2.7; Arthur untested
  § 81-2126, -2135(2)   request at or before commencement; $250 late fee
  Application for State Electrical Inspection (rev. 3-27-26)   fee schedule
  Board Rule 13 (4-23-24)   five-month permit life
  § 81-15,248; Title 124 ch. 2, 3, 9, 10, App. A; GTS220000   septic
  § 46-602(1), -606(1), -1224(3), -1233(2), -1241   wells
  Title 134 ch. 4 (eff. 6-28-2026) Chart 1, Chart 2, § 012.01   well siting
  § 23-114.04           county zoning permit; plans incl. sewage disposal
  § 76-2321(1)          One-Call: two full business days, not more than ten

DELIBERATELY NOT CLAIMED, and why:
  - Any building-permit fee, plan-review percentage or tap fee. No state
    schedule exists; every local figure in circulation is unverified.
  - A frost depth, snow load or wind speed. IRC Table R301.2 is filled in
    locally; no state table exists.
  - "4 inches of clean aggregate" or a vapor retarder as radon LAW. They are
    IRC Appendix F practice, not § 76-3504.
  - A stormwater acreage threshold. Not read in a Nebraska source.
  - Title 178 ch. 12 numbers for wells. Superseded June 28, 2026.
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
CITE = k.CITE_COL

FORM_ID = "NE.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "What to Gather"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What to gather before you file — and the part of it that applies whether "
    "or not your county ever created a building permit.")

flow.append(k.disclaimer(
    "Fee figures were read from the agencies' own current forms and rule "
    "titles in September 2026 — the State Electrical Division's application "
    "revised March 27, 2026, and Title 124 Appendix A. No local building-permit "
    "fee is printed anywhere in this kit, because no state schedule exists and "
    "no local one could be verified."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- applies anyway
flow += k.h2_tight("WHAT APPLIES WHATEVER YOUR COUNTY DECIDED", reserve=2.0)
flow.append(k.body(
    "NE.1 settled that the code binds your house whether or not anyone "
    "inspects it. <b>This page is the paperwork that exists either way.</b> "
    "Every item below applies on a parcel with no building department exactly "
    "as it applies in Lincoln."))
rows = [
    [k.cellp("<b>Request for state electrical inspection</b>"),
     k.cellp("Before any wiring starts, unless your city or county runs its "
             "own certified program — then theirs. The one filing with a "
             "felony behind it. Gates the power connection")],
    [k.cellp("<b>Septic general-permit certification and registration</b>"),
     k.cellp("Unless you are on public sewer. Made by the certified "
             "professional, not you. <b>Constrains where the house can "
             "sit</b> — the setback table is below. Do it first")],
    [k.cellp("<b>Well registration and well log</b>"),
     k.cellp("If you are on a well. Within 60 days of completion, by the "
             "driller — or by you, if you drilled it")],
    [k.cellp("<b>County zoning permit</b>"),
     k.cellp("In a zoned county, for \"any nonfarm building\" — required "
             "even where no building code exists, and it must show "
             "\"sanitation, plumbing and sewage disposal\"")],
    [k.cellp("<b>Radon-resistant construction</b>"),
     k.cellp("Statewide by statute, checked by nobody outside a local "
             "program. Two exemptions, one of which is a county list")],
    [k.cellp("<b>Nebraska Energy Code</b>"),
     k.cellp("No permit, no certificate, no inspection on request. You build "
             "to it; the values are below")],
    [k.cellp("<b>Utility locate</b>"),
     k.cellp(f"Nebraska 811, free, \"at least two full business days, but "
             f"no more than ten business days, before commencing the "
             f"excavation\" ({sec('76-2321(1)')})")],
    [k.cellp("<b>Floodplain</b>"),
     k.cellp("Check the parcel on the FEMA Flood Map Service Center and ask "
             "the county or city whether a floodplain development permit "
             "applies. Local, and independent of the building code")],
]
flow.append(k.ref_table(
    "The approvals that do not depend on a building department",
    [k.cellp("What", bold=True), k.cellp("When and why", bold=True)],
    rows, [2.35 * inch, CW - 2.35 * inch]))

# ---------------------------------------------------------------- code editions
flow += k.h2_tight("THE CODE EDITIONS ACTUALLY IN FORCE", reserve=1.8)
rows = [
    [k.cellp("<b>Residential building</b>"),
     k.cellp("<b>2018 International Residential Code</b>, \"except section "
             "R313 and chapters 25 through 33\" — sprinklers and the "
             "plumbing chapters are carved out"),
     k.cellp(sec("71-6403(1)(b)"))],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp("<b>2018 Uniform Plumbing Code</b> (IAPMO). <b>Not</b> the IPC "
             "and <b>not</b> the IRC plumbing chapters. The default in every "
             "city, village and county without its own plumbing ordinance"),
     k.cellp(f"{sec('71-6403(1)(d)')}; {sec('18-132(4)')}; "
             f"{sec('23-172(4)')}")],
    [k.cellp("<b>Mechanical, fuel gas</b>"),
     k.cellp("The 2018 IRC's own chapters 12–24, which were adopted with the "
             "rest of the IRC"),
     k.cellp(sec("71-6403(1)(b)"))],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("<b>2023 National Electrical Code</b>, effective August 1, "
             "2024 — with <b>five sections held at their 2017 text</b>. See "
             "below"),
     k.cellp(sec("81-2104(5)"))],
    [k.cellp("<b>Energy</b>"),
     k.cellp("<b>2018 IECC</b>, unamended, under a separate act. IRC chapter "
             "11 mirrors it; a local government that deletes any of chapter "
             "11 must notify DWEE within 30 days"),
     k.cellp(f"{sec('81-1609(9)')}; {sec('81-1611')}; "
             f"{sec('71-6406(4)')}")],
    [k.cellp("<b>Radon</b>"),
     k.cellp("The statutory minimum standards, folded into the state "
             "building code. <b>Less</b> than IRC Appendix F — see below"),
     k.cellp(f"{sec('76-3504')}; {sec('71-6403(2)')}")],
    [k.cellp("<b>Fire sprinklers</b>"),
     k.cellp("<b>No statewide requirement</b> for one- and two-family "
             "dwellings — R313 is excluded. But a city or county <i>may</i> "
             "adopt R313 and still \"conform generally,\" and nothing in "
             "the Act forbids it. Check the local amendments"),
     k.cellp(f"{sec('71-6403(1)(b)')}; {sec('71-6406(2)(c)(iii)')}")],
]
flow.append(k.ref_table(
    "What binds a house under the state code",
    [k.cellp("Trade", bold=True), k.cellp("Code and edition", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.35 * inch, CW - 1.35 * inch - CITE, CITE]))
flow.append(k.cite(
    "<b>This table is the state's floor.</b> A local government may adopt "
    f"\"any supplement, new edition, appendix\" and still conform "
    f"({sec('71-6406(2)(b)')}); it may <i>not</i> run an older edition "
    f"({sec('71-6406(3)(a)')}). <b>Lincoln</b> (its own codes page, September "
    f"2026) is on the <b>2021</b> IBC, IRC, UPC, IMC, IFGC and IEBC, the 2023 "
    f"NEC and the 2018 IECC, each with local amendments. <b>Unincorporated "
    f"Sarpy County</b> adopted the 2018 IBC, IRC, IMC, IFGC, IECC and the "
    f"2018 <b>IPC</b> — not the UPC — by Resolution 2024-150, effective June "
    f"4, 2024. Editions change only when the Legislature amends "
    f"{sec('71-6403')}; the two-year local-adoption clock runs from that "
    f"amendment. No 2021 or 2024 adoption bill had passed as of September "
    f"2026. Watch the Legislature, not an agency."))

flow.append(Spacer(1, 2))
flow += k.check_table(
    "Confirm the editions this kit will not guess at for your jurisdiction",
    [
        ("The residential and plumbing code editions my city or county "
         "reviews to (or \"none adopted — state code applies\"), and who told "
         "me:", [("Editions", 0.5), ("Source", 0.5)]),
        ("Whether my jurisdiction adopted R313 (sprinklers) or any IRC "
         "appendix in its local amendments:",
         [("Answer", 0.6), ("Source", 0.4)]),
        ("The frost depth, ground snow load and wind speed my jurisdiction "
         "fills into IRC Table R301.2 — no state table exists; get the "
         "figures in writing:", [("Frost", 0.3), ("Snow", 0.3), ("Wind", 0.4)]),
    ])

# ---------------------------------------------------------------- NEC
flow += k.h2_tight("THE 2023 NEC — WITH FIVE SECTIONS HELD AT 2017",
                   reserve=2.2)
flow.append(k.body(
    "Nebraska is current on electrical and then reaches back two editions for "
    "five specific sections. The statute names them; a code book on its own "
    "will give the wrong answer on every one."))
flow.append(k.callout(
    f"Neb. Rev. Stat. {sec('81-2104(5)')} — the edition, verbatim", [
        Paragraph("The board \"shall be governed by the minimum standards set "
                  "forth in the National Electrical Code issued and adopted "
                  "by the National Fire Protection Association beginning in "
                  "the <b>2023 edition</b> of the National Electrical Code, "
                  "Publication Number 70-2023, <b>except that the minimum "
                  "standards set forth in the 2017 edition of the National "
                  "Electrical Code shall apply for sections 210.8(A), "
                  "210.8(A)(3), 210.8(A)(5), 230.67(A), and 230.85</b>.\"",
                  S["body"]),
    ]))
rows = [
    [k.cellp("<b>210.8(A)</b>"), k.cellp("Dwelling-unit GFCI protection — the "
                                         "list of locations"),
     k.cellp("2017 text applies", center=True)],
    [k.cellp("<b>210.8(A)(3)</b>"), k.cellp("Outdoor receptacles"),
     k.cellp("2017 text applies", center=True)],
    [k.cellp("<b>210.8(A)(5)</b>"), k.cellp("Basement receptacles"),
     k.cellp("2017 text applies", center=True)],
    [k.cellp("<b>230.67(A)</b>"), k.cellp("Surge-protective device at the "
                                          "service"),
     k.cellp("2017 text applies", center=True)],
    [k.cellp("<b>230.85</b>"), k.cellp("Emergency disconnect at the "
                                       "service"),
     k.cellp("2017 text applies", center=True)],
]
flow.append(k.ref_table(
    "The five sections — everything else is the 2023 NEC as published",
    [k.cellp("Section", bold=True), k.cellp("Subject (the NEC's own heading)",
                                            bold=True),
     k.cellp("Nebraska rule", bold=True, center=True)],
    rows, [1.2 * inch, CW - 1.2 * inch - 1.6 * inch, 1.6 * inch]))
flow.append(k.cite(
    "The Division's own notice: \"Beginning August 1st, 2024, the Nebraska "
    "State Electrical Division will be adopting the NFPA 70 National Electric "
    "Code 2023.\" <b>Two things guides get wrong here.</b> There is <b>no "
    "AFCI</b> section on the list — arc-fault requirements are the 2023 text. "
    "And the carve-backs run <i>toward</i> the older, lighter requirement: "
    "read the 2017 book for those five sections and design the rest to 2023. "
    "<b>Inside a city or county with its own electrical program</b>, ask which "
    "edition its inspector reviews to; a local program must meet the state "
    f"standard but may exceed it ({sec('81-2125(1)')}). Lincoln reviews to "
    f"the 2023 NEC."))

# ---------------------------------------------------------------- energy
flow += k.h2_tight("THE ENERGY ANSWER — 2018 IECC, UNAMENDED, ZONE 5 "
                   "EVERYWHERE", reserve=2.2)
flow.append(k.body(
    "DWEE's fact sheet says it in one line: \"The unamended 2018 IECC was "
    "adopted in Nebraska statewide on July 1, 2020.\" Its energy impact study "
    "adds the other fact you need: the climate zone map \"place[s] the "
    "<b>entire state of Nebraska in a single climate zone (5)</b>.\" So there "
    "is one column of the table to read, and it is this one."))
rows = [
    [k.cellp("Windows and doors (fenestration U-factor)"), k.cellp("U-0.30", center=True)],
    [k.cellp("Skylights"), k.cellp("U-0.55", center=True)],
    [k.cellp("Ceiling"), k.cellp("R-49", center=True)],
    [k.cellp("Wood-frame wall"), k.cellp("R-20 cavity, or R-13 cavity + R-5 "
                                         "continuous", center=True)],
    [k.cellp("Mass wall"), k.cellp("R-13 continuous or R-17 cavity", center=True)],
    [k.cellp("Floor over unconditioned space"), k.cellp("R-30", center=True)],
    [k.cellp("Basement wall"), k.cellp("R-15 continuous or R-19 cavity", center=True)],
    [k.cellp("Slab on grade"), k.cellp(f"R-10, to 2{NB}ft", center=True)],
    [k.cellp("Crawl-space wall"), k.cellp("R-15 continuous or R-19 cavity", center=True)],
    [k.cellp("<b>Whole-house air leakage (blower door)</b>"),
     k.cellp(f"<b>less than 3 air changes per hour at 50{NB}pascals</b>",
             center=True)],
    [k.cellp("Duct leakage"),
     k.cellp(f"≤ 4{NB}CFM per 100{NB}sq{NB}ft; not required when all ducts "
             f"are inside the thermal envelope", center=True)],
    [k.cellp("Mechanical ventilation"), k.cellp("Whole-house system required",
                                                center=True)],
    [k.cellp("Load calculation"), k.cellp("ACCA Manual J required",
                                          center=True)],
]
flow.append(k.ref_table(
    "2018 IECC prescriptive values, climate zone 5 — DWEE's quick reference",
    [k.cellp("Component", bold=True), k.cellp("Requirement", bold=True,
                                              center=True)],
    rows, [2.6 * inch, CW - 2.6 * inch]))
flow.append(k.cite(
    "Values read from DWEE's Residential Energy Code Fact Sheet (2018 IECC) "
    "and its Energy Impact Study comparing the 2018 and 2021 IECC, at "
    "dwee.nebraska.gov, September 2026. DWEE's compliance paths are "
    "<b>REScheck</b> or the component table with no trade-offs. <b>There is "
    "no Nebraska energy certificate</b> — the IECC's own posted certificate "
    f"(R401.3) is a code requirement, not a state form. The duty is yours "
    f"({sec('81-1622(1)')}); the exposure is the two-year order "
    f"({sec('81-1625')}). A city or county with its own energy code may "
    f"inspect and may waive a requirement it finds not economically justified "
    f"({sec('81-1618')}) — ask whether yours has one."))

# ---------------------------------------------------------------- radon
flow += k.h2_tight("RADON-RESISTANT CONSTRUCTION — THE STATUTE, AND ITS TWO "
                   "EXEMPTIONS", reserve=2.4)
flow.append(k.body(
    "\"Except as provided in section 76-3505, new construction built after "
    "September 1, 2019, in the State of Nebraska that is intended to be "
    "regularly occupied by people shall be built using radon resistant new "
    f"construction\" ({sec('76-3504')}). A local code that omits it does not "
    f"conform ({sec('71-6406(3)(b)')}). <b>What the statute actually requires "
    f"is shorter than the IRC appendix most guides quote:</b>"))
flow.append(k.callout_long(
    f"Neb. Rev. Stat. {sec('76-3504')} — the minimum standards, in the "
    f"statute's words", [
        Paragraph("<b>Sumps.</b> A sump pit open to soil or terminating "
                  "drain tile \"shall be covered with a gasketed or otherwise "
                  "sealed lid\"; a sump used as the suction point \"shall have "
                  "a lid designed to accommodate the vent pipe\"; a sump used "
                  "as a floor drain \"shall have a lid equipped with a "
                  "trapped inlet.\"", S["body"]),
        Paragraph(f"<b>Passive subslab depressurization</b>, in basement or "
                  f"slab-on-grade buildings: \"A minimum three-inch diameter "
                  f"… ABS, PVC, or equivalent gas-tight pipe shall be embedded "
                  f"vertically into the subslab permeable material before the "
                  f"slab is cast. A 'T' fitting or equivalent method shall be "
                  f"used\" — or the pipe is \"inserted directly into an "
                  f"interior perimeter drain tile loop or through a sealed "
                  f"sump cover.\" It runs \"up through the building floors\" "
                  f"and terminates \"at least twelve inches above the surface "
                  f"of the roof in a location at least ten feet away from any "
                  f"window or other opening into the conditioned spaces … "
                  f"that is less than two feet below the exhaust point and ten "
                  f"feet from any window or other opening in adjoining or "
                  f"adjacent buildings.\" Where interior footings divide the "
                  f"subslab material, each area gets its own vent pipe. Every "
                  f"exposed vent pipe is labeled \"Radon Reduction System\" "
                  f"on each floor and in accessible attics.", S["body"]),
        Paragraph("<b>Power source.</b> \"An electrical circuit terminated in "
                  "an approved box shall be installed during construction in "
                  "the attic or other anticipated location of vent pipe "
                  "fans.\"", S["body"]),
    ]))
flow.append(k.cite(
    "<b>Not in the statute</b> (verified absence): any aggregate depth under "
    "the slab, any vapor retarder, any soil-gas membrane. Those are IRC "
    "Appendix F practice and good practice — build them if you like — but no "
    "Nebraska statute adopts or excludes any IRC appendix, so they are law "
    f"only where a local code says so. A contractor may convert the passive "
    f"system to an active one, but \"a radon mitigation specialist shall "
    f"conduct any postinstallation testing\" ({sec('76-3506')}). Radon is "
    f"<b>DHHS</b>; onsite wastewater is DWEE."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "The two exemptions — one of them is a county list, and it moves", [
        Paragraph(f"\"New construction after September 1, 2019, shall not be "
                  f"required to use radon resistant new construction if (1) "
                  f"<b>the construction project utilizes the design of an "
                  f"architect or professional engineer</b> licensed under the "
                  f"Engineers and Architects Regulation Act, (2) the "
                  f"construction project is located in a county in which the "
                  f"average radon concentration is <b>less than two and "
                  f"seven-tenths picocuries per liter</b> of air as determined "
                  f"by the department pursuant to section 76-3507\" "
                  f"({sec('76-3505')}). The third exemption is expressly "
                  f"\"other than for any residential dwelling unit.\"",
                  S["body"]),
        Paragraph(f"DHHS's determination to the Legislature dated January 1, "
                  f"2024 (data October 2018 through September 2023): <b>77 of "
                  f"93 counties exceed 2.7{NB}pCi/L</b>. The fourteen "
                  f"below it: <b>Blaine</b> (one test), <b>Cherry, Dundy, "
                  f"Grant, Lincoln, Logan, Loup, McPherson, Merrick, Rock, "
                  f"Sheridan, Sioux, Thomas</b> and <b>Wheeler</b>. "
                  f"<b>Arthur</b> had no tests at all, and <b>Hall</b> "
                  f"averaged exactly 2.7 — which is not \"less than,\" so the "
                  f"exemption does not reach it by its terms. The list is "
                  f"redetermined annually on rolling data; confirm your "
                  f"county on DHHS's radon data page before you rely on it.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- electrical fees
flow += k.h2_tight("THE ELECTRICAL REQUEST, ITS FEES AND ITS CLOCKS",
                   reserve=2.2)
flow.append(k.body(
    "The State Electrical Division calls it a permit; the statute calls it a "
    "<b>request for inspection</b>, due \"at or before commencement,\" with "
    f"the fees \"due and payable … at or before commencement of the "
    f"installation\" ({sec('81-2126')}; {sec('81-2135(2)')}). The Division's "
    f"online licensing and permitting system went live on <b>April 13, "
    f"2026</b>; homeowner permits in it \"must be linked by NSED Office Staff "
    f"once you have registered an account.\" The paper form is the "
    f"<b>Application for State Electrical Inspection</b>, revised March 27, "
    f"2026, which is where these fees come from."))
rows = [
    [k.cellp("NEW electrical service, 1–400 amps"), k.cellp("$75", center=True)],
    [k.cellp("Branch circuit or feeder, each (including extensions)"),
     k.cellp("$10", center=True)],
    [k.cellp("EXISTING service, regardless of size"), k.cellp("$50", center=True)],
    [k.cellp("Reconnect"), k.cellp("$75", center=True)],
    [k.cellp("Approval notice, if you want a written one"), k.cellp("$6", center=True)],
    [k.cellp("<b>Homeowner minimum permit fee</b>"), k.cellp("<b>$100</b>", center=True)],
    [k.cellp("Minimum permit fee, general"), k.cellp("$50", center=True)],
    [k.cellp(f"Supervisory fee, by statute ({sec('81-2126')})"),
     k.cellp("50 cents", center=True)],
    [k.cellp(f"<b>Late request</b> — filed after the 14-day certified-mail "
             f"notice ({sec('81-2126')})"),
     k.cellp("<b>$250</b>", center=True)],
]
flow.append(k.ref_table(
    "Fee schedule — Application for State Electrical Inspection, rev. 3-27-26",
    [k.cellp("Item", bold=True), k.cellp("Fee", bold=True, center=True)],
    rows, [CW - 1.4 * inch, 1.4 * inch]))
flow.append(k.cite(
    "The Division announced that \"As of April 1, 2026 the permit fees have "
    "been updated to reflect increases to some fees.\" Its May 2024 homeowner "
    "handout still works an example at $35 and $5 — <b>that example is "
    "stale</b>; the form governs. The form's own notice, in capitals: "
    "\"INSPECTION FEES WILL NOT BE REFUNDED OR TRANSFERRED,\" and \"FEES WILL "
    "NOT BE REFUNDED IF APPLICATION CONTAINS FALSE INFORMATION\" — so fill "
    "it in carefully the first time."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "A worked example, so the arithmetic is not a surprise", [
        Paragraph(f"A new house with a <b>200-amp service and 30 branch "
                  f"circuits</b>: $75 for the new service plus 30 × $10 = "
                  f"$300 for the circuits — <b>$375</b>, well above the $100 "
                  f"homeowner minimum. Add $6 if you want the written approval "
                  f"notice (buy it: it is the one third-party record of the "
                  f"wiring your house will ever have). A 200-amp service with "
                  f"fewer than three circuits would fall to the $100 minimum, "
                  f"which no house does.", S["body"]),
        Paragraph("<b>What the form asks for:</b> the type of request "
                  "(Contractor / <b>Homeowner</b> / Utility Reconnect), the "
                  "type of installation (Single-Family Residence), a "
                  "description and location, the owner, the installer and "
                  "license, the <b>power supplier's name and address</b> — "
                  "because the Division forwards a copy of a new-service "
                  "permit to the utility — and the estimated completion date. "
                  "As a homeowner you also sign the <b>homeowner "
                  "verification</b> that you know the code and the Act.",
                  S["body"]),
    ]))
flow.append(k.body(
    "<b>Two clocks start at issue.</b> Under State Electrical Board Rule 13, "
    "the permit is void if the work \"has not been started within five (5) "
    "months\" of issuance, or if no progress is made for five consecutive "
    "months, after fourteen days' written notice; an extension needs \"clear "
    "and convincing proof of a practical hardship.\" And the inspector must be "
    "notified \"within reasonable time\" before any wiring is concealed "
    f"({sec('81-2134(2)')}). NE.3 has the full sequence."))

# ---------------------------------------------------------------- septic
flow += k.h2_tight("THE SEPTIC PACKAGE, IN ORDER", reserve=2.4)
flow.append(k.body(
    "Onsite wastewater is DWEE's <b>Title 124</b>. A system \"is to be "
    "permitted by the Department before any construction\" (ch. 3 §&#160;002), "
    "and there are two routes: a <b>general permit</b> for a conventional "
    "septic tank and subsurface leach field (also holding tanks, lagoons and "
    "mounds), which an owner is \"authorized to construct … under … if they "
    "meet the conditions of the permit\" (ch. 3 §&#160;003.06); or an "
    "individual <b>construction and operating permit</b> whose plans \"will be "
    "prepared and properly stamped and signed by a Professional Engineer\" "
    "(ch. 3 §&#160;004.03). A normal house rides the general permit."))
rows = [
    [k.cellp("<b>0</b>", center=True), k.cellp("<b>Choose the professional</b>"),
     k.cellp(f"You may not site, lay out or build the system yourself; a "
             f"Master or Journeyman Installer, engineer or environmental "
             f"health specialist must be \"physically present at the site\" "
             f"({sec('81-15,248(1)')}; ch. 9 §{NB}004)")],
    [k.cellp("<b>1</b>", center=True),
     k.cellp("<b>Soil evaluation and percolation test</b>"),
     k.cellp(f"Perc tests only by an engineer, environmental health "
             f"specialist, or certified Inspector, Soil Evaluator, Master or "
             f"Journeyman Installer (ch. 2 §{NB}012.01). Soil is unsuitable "
             f"\"if the percolation rate is faster than five minutes per inch "
             f"or is slower than 60 minutes per inch\" — faster is rescued by "
             f"a 12-inch loamy-sand liner; slower is off the general permit "
             f"and needs an engineer (GTS220000 §{NB}III.J)")],
    [k.cellp("<b>2</b>", center=True), k.cellp("<b>Site it</b>"),
     k.cellp(f"Seasonal high groundwater \"at least four feet below the "
             f"bottom of the infiltrative surface\" (§{NB}III.C); no absorption "
             f"system in fill except sand fill (§{NB}III.J.4); a <b>reserve "
             f"area</b> for a replacement system, carrying all the setbacks "
             f"(ch. 2 §{NB}008). The setback table is on the next page")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("<b>General-permit coverage</b>"),
     k.cellp("Coverage \"is granted to an owner of a dwelling\" who submits, "
             "with the registration, the professional's signed "
             "certification, \"an appropriately scaled drawing of the onsite "
             "wastewater treatment system\" and the percolation or seepage "
             f"data (GTS220000 §{NB}II.A). A pressure-dosed system is not "
             f"covered (§{NB}III.K.21)")],
    [k.cellp("<b>4</b>", center=True), k.cellp("<b>Registration</b>"),
     k.cellp(f"By the professional, \"within forty-five days of completion\" "
             f"({sec('81-15,248(2)')}). <b>$140</b> registration; late "
             f"<b>$150</b> at 46–90 days, <b>$450</b> at 91 or more (App. A). "
             f"The professional \"will provide a copy of the system "
             f"registration form to the system owner\" (ch. 10 §{NB}004) — "
             f"<b>get it</b>")],
]
flow.append(k.ref_table(
    "The sequence, and what each step actually is",
    [k.cellp("", bold=True, center=True), k.cellp("Step", bold=True),
     k.cellp("What the rule says", bold=True)],
    rows, [0.35 * inch, 1.6 * inch, CW - 1.95 * inch]))
flow.append(k.cite(
    "Title 124, Rules and Regulations for the Design, Operation and "
    "Maintenance of Onsite Wastewater Treatment Systems, effective June 27, "
    "2022, and the general permit GTS220000 (septic tank and subsurface leach "
    "field), read from DWEE's Title 124 booklet, form 23-017 ver. 02.2026. An "
    "individual construction permit application is <b>$450</b> (App. A). "
    "Cesspools, dry wells, leaching pits and seepage pits are prohibited "
    f"(ch. 2 §{NB}003). Civil penalty for a violation: up to <b>$10,000</b> "
    f"per violation per day ({sec('81-15,253')}). DWEE may delegate the "
    f"program to a county or city with a program \"at least as stringent\" "
    f"({sec('81-15,248(3)')}), and \"Nothing in this Title will prevent more "
    f"stringent local requirements\" (ch. 2 §{NB}014) — <b>every number here "
    f"is a state floor</b>."))

flow.append(Spacer(1, 4))
rows = [
    [k.cellp("Private drinking-water well"), k.cellp("50", center=True),
     k.cellp("<b>100</b>", center=True), k.cellp("100", center=True)],
    [k.cellp("Public community well"), k.cellp("500", center=True),
     k.cellp("500", center=True), k.cellp("1,000", center=True)],
    [k.cellp("Surface water"), k.cellp("50", center=True),
     k.cellp("50", center=True), k.cellp("50", center=True)],
    [k.cellp("Pressure water main or service line, suction line"),
     k.cellp("10", center=True), k.cellp("25", center=True),
     k.cellp("25", center=True)],
    [k.cellp("<b>Property line</b>"), k.cellp("<b>5</b>", center=True),
     k.cellp("<b>5</b>", center=True), k.cellp("50", center=True)],
    [k.cellp("Driveway, parking, sidewalk, impermeable surface"),
     k.cellp("5", center=True), k.cellp("5", center=True),
     k.cellp("50", center=True)],
    [k.cellp("<b>Your foundation, Class 2</b> — house sits <i>higher</i> "
             "than the system (the default)"),
     k.cellp("10", center=True), k.cellp("<b>10</b>", center=True),
     k.cellp("100", center=True)],
    [k.cellp("<b>Your foundation, Class 1</b> — any part of the basement, "
             "footing or slab sits <i>lower</i> than the system"),
     k.cellp("15", center=True), k.cellp("<b>30</b>", center=True),
     k.cellp("100", center=True)],
    [k.cellp("Class 3 — slab on grade, not living quarters"),
     k.cellp("7", center=True), k.cellp("10", center=True),
     k.cellp("50", center=True)],
    [k.cellp("Neighbor's foundation, Class 1 / 2 / 3"),
     k.cellp("25 / 20 / 15", center=True), k.cellp("40 / 30 / 20", center=True),
     k.cellp("200 / 200 / 100", center=True)],
    [k.cellp("Horizontal closed-loop geothermal well"),
     k.cellp("25", center=True), k.cellp("25", center=True),
     k.cellp("25", center=True)],
]
flow.append(k.ref_table(
    "Setbacks in feet — Title 124 ch. 2 Table 2.1",
    [k.cellp("From", bold=True), k.cellp("Tank", bold=True, center=True),
     k.cellp("Absorption field", bold=True, center=True),
     k.cellp("Lagoon", bold=True, center=True)],
    rows, [CW - 3.3 * inch, 1.0 * inch, 1.3 * inch, 1.0 * inch]))
flow.append(k.cite(
    "<b>The row that moves the house is the foundation class.</b> Table 2.1's "
    "footnote: Class 1 is \"a basement, a non-basement footing, swimming pool, "
    "or slab-on-grade living quarters where any portion … is lower in "
    "elevation than the onsite wastewater treatment system component\"; Class "
    "2 is the same structures higher in elevation. Put the drainfield uphill "
    "of a walk-out basement and the distance triples from 10 to 30 feet. "
    "\"A person is not to construct or relocate a foundation, well, water "
    "line, surface water feature, or property line within the setback "
    f"distances listed in Table 2.1\" (ch. 2 §{NB}011) — a variance needs an "
    f"engineer's letter. Between trenches, and between tank and nearest "
    f"trench, undisturbed soil of 4 / 6 / 10 feet at slopes under 10% / "
    f"10–20% / over 20% (GTS220000 §{NB}III.K.9)."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Sizing, from the general permit — so you can check the professional's "
    "arithmetic", [
        Paragraph(f"<b>Design flow</b> is \"100 gallons per day plus 100 "
                  f"gallons per day per bedroom\" (Table 1): a 3-bedroom house "
                  f"is <b>400{NB}gpd</b>, 4 bedrooms 500, 5 bedrooms 600. A "
                  f"garage floor drain adds at least 100{NB}gpd "
                  f"(§{NB}III.L.3). Over 1,000{NB}gpd is off the general "
                  f"permit.", S["body"]),
        Paragraph(f"<b>Septic tank</b> (Table 3; \"in no case … less than "
                  f"1,000\" gallons): at 400{NB}gpd, <b>1,000</b> gallons "
                  f"with no grinder pump and no large tub; <b>1,250</b> with "
                  f"one of them; <b>1,500</b> with both. \"Large capacity "
                  f"tub\" is a working volume over 50 gallons. At 500{NB}gpd "
                  f"the three figures are 1,250 / 1,500 / 1,750; at "
                  f"600{NB}gpd, 1,500 / 1,750 / 2,000. A single-compartment "
                  f"tank fed by a pump is upsized 50% (§{NB}III.H.3).",
                  S["body"]),
        Paragraph(f"<b>Absorption trench bottom area</b> (Table 5), at "
                  f"400{NB}gpd: <b>495{NB}sq{NB}ft</b> at a perc rate over 5 "
                  f"to 10 minutes per inch; <b>630</b> at 10–20; <b>750</b> "
                  f"at 20–30; <b>825</b> at 30–40; <b>990</b> at 40–50; "
                  f"<b>1,050</b> at 50–60; over 60 is \"Ineligible for general "
                  f"permit.\" Gravity trenches are limited to 150{NB}ft "
                  f"(§{NB}III.K.5), and beds carry a multiplier. Trench bottoms "
                  f"stay 4{NB}ft above seasonal high groundwater.", S["body"]),
    ]))

# ---------------------------------------------------------------- well
flow += k.h2_tight("IF YOU ARE ON A WELL", reserve=2.2)
rows = [
    [k.cellp("<b>You may drill it yourself</b>"),
     k.cellp("\"An individual may construct a water well or install and "
             "repair pumps and pumping equipment onsite on land owned by him "
             "or her and used by him or her for farming, ranching, or "
             "agricultural purposes or as his or her place of abode.\" The "
             "exemption is from the <i>license</i>: \"Any person constructing "
             "a water well … shall do such work in accordance with the rules "
             "and regulations\""),
     k.cellp(f"{sec('46-1233(1)')}–(2)")],
    [k.cellp("<b>Registration, within 60 days</b>"),
     k.cellp("Every well \"shall be registered with the department … within "
             "sixty days after completion,\" filed by the licensed driller "
             "\"or the owner of the water well if the owner constructed the "
             "water well,\" with the well-log information. Fee: <b>$200</b> "
             "plus the board's <b>$25–$40</b> for a well designed to pump "
             f"50{NB}gpm or less"),
     k.cellp(f"{sec('46-602(1)')}; {sec('46-606(1)')}; "
             f"{sec('46-1224(3)')}")],
    [k.cellp("<b>The well log</b>"),
     k.cellp("\"Any owner of a water well or a licensed water well contractor "
             "who engages in … constructing a water well shall keep and "
             "maintain an accurate well log\" — eighteen listed items. If you "
             "drill, you keep it"),
     k.cellp(sec("46-1241"))],
    [k.cellp("<b>The construction standards</b>"),
     k.cellp("<b>DWEE Title 134 ch. 4</b>, effective <b>June 28, 2026</b> — "
             "\"Regulations Governing Water Well Construction, Pump "
             "Installation and Water Well Decommissioning Standards.\" It "
             "<b>replaced</b> DHHS Title 178 ch. 12; do not use a 178 copy"),
     k.cellp(f"Title 134 ch. 4")],
    [k.cellp("<b>A variance, if Chart 1 cannot be met</b>"),
     k.cellp("A written request \"at least 10 days prior\" to construction, "
             "with \"a scaled map showing the location of the well in "
             "relation to property lines, structures, utilities, and "
             "contamination sources\""),
     k.cellp(f"Title 134 ch. 4 §{NB}012.01")],
    [k.cellp("<b>Pump wiring</b>"),
     k.cellp("A licensed pump installation contractor may wire \"pumps and "
             "pumping equipment at a water well location to the first "
             "control\" without an electrical license. Beyond the first "
             "control it is electrical work"),
     k.cellp(sec("81-2121(7)"))],
]
flow.append(k.ref_table(
    "The well package",
    [k.cellp("", bold=True), k.cellp("What the rule requires", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.65 * inch, CW - 1.65 * inch - CITE, CITE]))

flow.append(Spacer(1, 4))
rows = [
    [k.cellp("Any septic lateral field (soil absorption system)"),
     k.cellp("<b>100</b>", center=True)],
    [k.cellp("Any septic tank"), k.cellp("<b>50</b>", center=True)],
    [k.cellp("Wastewater lagoon, privy, cesspool, subsurface disposal system"),
     k.cellp("100", center=True)],
    [k.cellp("Pressurized sanitary sewer line, or a non-watertight one"),
     k.cellp("50", center=True)],
    [k.cellp("Watertight sanitary sewer line; storm sewer"),
     k.cellp("10", center=True)],
    [k.cellp("Animal-waste structure; feeding-operation holding pens"),
     k.cellp("100", center=True)],
    [k.cellp("Storm water way; frost-proof hydrant; well pit; any depression "
             "that could retain stagnant water"),
     k.cellp("10", center=True)],
]
flow.append(k.ref_table(
    "Minimum distance from a domestic well, in feet — Title 134 ch. 4 Chart 1 "
    "(2026)",
    [k.cellp("To", bold=True), k.cellp("Feet", bold=True, center=True)],
    rows, [CW - 1.2 * inch, 1.2 * inch]))
flow.append(k.cite(
    "The septic rule (Table 2.1) and the well rule (Chart 1) agree: "
    f"100{NB}feet from drainfield to well, 50 from tank. <b>Chart 2</b> lets a "
    f"driller go to 50–100{NB}ft from a lateral field (25–50 from a tank) "
    f"only where Chart 1 cannot be met, with prior written DWEE approval, "
    f"full-length chip-bentonite grout and protective silts or clays; below "
    f"that, a declaratory ruling. <b>Verified absence:</b> Title 134 ch. 4 "
    f"has <b>no well-to-property-line rule</b> for a domestic well — the 600 "
    f"and 1,000-foot rows apply only to irrigation and industrial wells — and "
    f"no surface-water row. \"These are minimum requirements. Local "
    f"requirements may be more stringent\" (ch. 4 §{NB}001); ask your Natural "
    f"Resources District whether it requires its own permit for a domestic "
    f"well."))

# ---------------------------------------------------------------- record
# 2.6in, not 1.6in: at 1.6in the heading stranded at the foot of page 10.
flow += k.h2_tight("PERMIT RECORD — FILL THIS IN AS EACH ONE ISSUES",
                   reserve=2.6)
flow += k.check_table(
    "Every approval on this build",
    [
        ("<b>Request for state (or local) electrical inspection</b> filed "
         "before wiring began, with the homeowner verification:",
         [("Permit number", 0.4), ("Filed", 0.3), ("Fee paid", 0.3)]),
        ("<b>Certificate to the power supplier</b> that inspection was "
         "requested and the installation is safe to energize:",
         [("Utility", 0.5), ("Date filed", 0.5)]),
        ("<b>Septic professional</b> engaged — name, certificate class and "
         "number:", [("Name", 0.5), ("Certificate", 0.5)]),
        ("<b>Septic general-permit coverage</b> — scaled drawing and perc "
         "data submitted; or the individual permit number if engineered:",
         [("Reference", 0.5), ("Date", 0.5)]),
        ("<b>Septic system registration</b> — copy received from the "
         "professional (due within 45 days of completion):",
         [("Registration", 0.5), ("Date received", 0.5)]),
        ("<b>Well registration</b> filed within 60 days, and the well log "
         "kept:", [("Registration", 0.4), ("Filed", 0.3), ("Driller", 0.3)]),
        ("<b>County zoning permit</b> (or written confirmation that none is "
         "required):", [("Number", 0.4), ("Issued", 0.3), ("Office", 0.3)]),
        ("<b>Local building permit</b>, if one exists where I am building:",
         [("Number", 0.4), ("Issued", 0.3), ("Expires", 0.3)]),
        ("<b>Radon</b> — my county is / is not on the DHHS under-2.7 list, and "
         "the passive system is / is not required:",
         [("County status", 0.5), ("Date checked", 0.5)]),
        ("<b>Energy</b> — the REScheck report or component table I built to, "
         "and the posted certificate:", [("Path", 0.5), ("Date", 0.5)]),
        ("<b>Floodplain determination</b> — in or out of the mapped hazard "
         "area:", [("Result", 0.5), ("Who confirmed", 0.5)]),
        ("<b>Driveway or culvert permit</b> — which road authority:",
         [("Permit", 0.5), ("Authority", 0.5)]),
        ("<b>911 address</b> assigned:", [("Address", 0.6), ("Date", 0.4)]),
        ("<b>Nebraska 811</b> locate requested at least two full business "
         "days before excavation:", [("Ticket", 0.5), ("Date", 0.5)]),
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ne-permit-kit",
                       "NE.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
