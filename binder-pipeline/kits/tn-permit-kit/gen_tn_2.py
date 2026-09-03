#!/usr/bin/env python3
"""TN.2 Permit Application Checklist.

Every Tennessee claim in this document was read against its primary source in
September 2026 and is cited on-page.

The organising idea: separate what depends on your jurisdiction's status from
what does not. The building permit and its fee depend entirely on the status.
The septic permit, the well filings, the electrical permit and the stormwater
threshold do not care at all.

Verified sources:
  0780-02-23-.02(1)(a)  2018 IRC + Appendix Q, and the ten Tennessee amendments
                        including the energy provisions reverted to 2009 tables
  0780-02-23-.02(1)(b)  2018 IECC with the same 2009 reversions
  0780-02-01-.02(1)     2017 NEC, effective 1 October 2018, with the AFCI
                        exemptions — the edition trap
  0780-02-23-.08        the state fee schedule and every add-on fee
  0780-02-23-.05(4)     what the application must contain and certify
  0780-02-23-.05(7)     180 days to commence, two years to expire
  0400-48-01-.06(1)     the septic CONSTRUCTION permit is the operative permit
  0400-48-01-.06(2)     refused where public sewer is accessible
  0400-48-01-.06(4)     three-year expiry
  0400-48-01-.06(5)(a)  the electrical-inspector gate: evidence of a septic
                        APPLICATION before power is released
  0400-48-01-.06(5)(d)  and the carve-out where a countywide building permit
                        program exists
  0400-48-01-.07(1)(a)  site suitability by high or extra-high intensity soil map
  0400-48-01-.18        "approved soil consultant" — an approval, not a license
  0400-45-09-.10(1)(c)  Notice of Intent BEFORE drilling; .10(1)(d) $75 fee
  0400-45-09-.10(1)(h)  the NOI expires in 180 days
  0400-45-09-.15(1)     Report of Well Driller within 60 days
  0400-45-09-.10(2)(d)  the graduated well-to-property-line rule
  0400-45-09-.12(1)     disinfection is mandatory at 100 ppm for 12 hours
  CN-0971 (Rev. 04-25)  the application form, its routing instruction and fees
  TNR100000             the construction stormwater permit and its one-acre
                        trigger; and the 2026 CGP effective 1 October 2026

DELIBERATELY NOT CLAIMED, and why:
  - Any reduced stormwater acreage threshold for special or impaired
    watersheds. The concept exists in Tennessee but no number was verified.
  - Any per-jurisdiction fee. Only three fee bases in the state were verifiable
    and two of them are local; a wrong fee is worse than no fee.
  - That an owner may drill their own well. The rules require a licensed driller
    and contain no owner exemption for drilling; the only verified owner
    self-help is abandoning a hand-dug well under sixty feet.
  - A 2018 IECC R-value table. Tennessee replaced those tables with the 2009
    ones, so printing 2018 numbers would be actively wrong.
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

FORM_ID = "TN.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "What to Gather"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What to gather before you file — and which of it applies no matter what "
    "your jurisdiction decided about the building code.")

flow.append(k.disclaimer(
    "Fee figures were read from the rules and the agencies' own fee pages in "
    "September 2026. One of them — the minimum construction cost per square "
    "foot — is a website number rather than a rule number and will drift. "
    "Check it before you budget."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- applies anyway
flow += k.h2_tight("WHAT APPLIES WHATEVER YOUR STATUS", reserve=2.0)
flow.append(k.body(
    "TN.1 settled whether a building permit exists where you are building. "
    "<b>This page is the part that does not care.</b> Every item below applies "
    "in an opted-out county exactly as it applies in Nashville."))
rows = [
    [k.cellp("<b>Subsurface sewage disposal permit</b>"),
     k.cellp("Unless you are on public sewer. TDEC, on form CN-0971. "
             "<b>Constrains where the house can sit</b> — do it first")],
    [k.cellp("<b>State electrical permit</b>"),
     k.cellp("Unless your jurisdiction is on the state's electrical exempt "
             "list. Survives a building-code opt-out completely")],
    [k.cellp("<b>Notice of Intent to drill</b>"),
     k.cellp("If you are on a well. Filed <i>before</i> drilling starts, and "
             "the driller must be able to show it on site")],
    [k.cellp("<b>Zoning approval</b>"),
     k.cellp("A building-code opt-out is not a zoning opt-out. The state "
             "permit expressly excludes zoning")],
    [k.cellp("<b>Floodplain development permit</b>"),
     k.cellp("If the parcel is in a mapped hazard area. Local administrator, "
             "independent of the building code")],
    [k.cellp("<b>Construction stormwater permit</b>"),
     k.cellp("Only if total disturbance reaches <b>one acre</b> — see the last "
             "section, because driveways are what push people over")],
    [k.cellp("<b>Utility locate</b>"),
     k.cellp("Tennessee 811, free, before any excavation")],
]
flow.append(k.ref_table(
    "The approvals that do not depend on your jurisdiction's status",
    [k.cellp("What", bold=True), k.cellp("When and why", bold=True)],
    rows, [2.1 * inch, CW - 2.1 * inch]))

# ---------------------------------------------------------------- code editions
flow += k.h2_tight("THE CODE EDITIONS ACTUALLY IN FORCE", reserve=1.8)
rows = [
    [k.cellp("<b>Residential building</b>"),
     k.cellp("<b>2018 International Residential Code</b>, plus Appendix Q "
             "(tiny houses), with ten Tennessee amendments"),
     k.cellp("0780-02-23-.02(1)(a)")],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("<b>2017 National Electrical Code</b>, effective 1 October 2018. "
             "<b>Not 2020. Not 2023.</b> See below"),
     k.cellp("0780-02-01-.02(1)")],
    [k.cellp("<b>Energy</b>"),
     k.cellp("2018 IECC <i>or</i> Chapter 11 of the 2018 IRC, your choice — "
             "but with the envelope tables and the testing provisions "
             "<b>replaced by the 2009 editions</b>"),
     k.cellp("0780-02-23-.02(1)(b)")],
    [k.cellp("<b>Plumbing, mechanical, fuel gas</b>"),
     k.cellp("The <b>2018 IRC's own chapters</b>. <b>Not</b> the 2021 IPC, IMC "
             "or IFGC — those are adopted in the separate commercial chapter "
             "and do not govern a house"),
     k.cellp("0780-02-23-.02(1)(a)")],
    [k.cellp("<b>Fire sprinklers</b>"),
     k.cellp("<b>Not mandatory</b> in one- and two-family dwellings or "
             "townhouses. Because townhouses are unsprinklered they must be "
             "separated by two-hour fire walls"),
     k.cellp(sec("68-120-101(a)(8)"))],
]
flow.append(k.ref_table(
    "What binds a house under the state program",
    [k.cellp("Trade", bold=True), k.cellp("Code and edition", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - CITE, CITE]))
flow.append(k.cite(
    "<b>This table is the STATE program's.</b> An EXEMPT jurisdiction enforces "
    "its own adopted code and need only stay within <b>seven years</b> of the "
    "current published edition — so a large city may well be on something "
    "newer, including a newer NEC. Ask yours which editions it reviews to and "
    "write them on the line below."))

flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "The 2017 NEC is the single most expensive assumption in Tennessee", [
        Paragraph("Tennessee is <b>two code cycles behind</b> on electrical and "
                  "the rule is current, not stale — chapter 0780-02-01 was "
                  "revised on 14&#160;July 2025 and still adopts the "
                  "\"<b>National Electrical Code, 2017 edition</b>… effective "
                  "October 1, 2018.\" The State Fire Marshal's own electrical "
                  "page says the same thing.", S["body"]),
        Paragraph("<b>Two Tennessee amendments sit on top of it, and both are "
                  "more permissive than the national text.</b> Section 110.24 "
                  "available fault current \"shall be optional,\" and arc-fault "
                  "protection \"shall be optional for bathrooms, laundry areas, "
                  "garages, unfinished basements… and for branch circuits "
                  "dedicated to supplying refrigeration equipment.\"", S["body"]),
        Paragraph("<b>Why it costs money either way.</b> Design to the 2023 NEC "
                  "and you buy protection Tennessee does not require. Design to "
                  "a national reference and you may miss a 2017-era rule that "
                  "later editions changed. And if you are in an EXEMPT city "
                  "that adopted a newer NEC, none of the above applies to you. "
                  "Ask which edition your inspector reviews against, and write "
                  "it down before you buy a panel.", S["body"]),
    ]))

flow.append(Spacer(1, 2))
flow += k.check_table(
    "Confirm the two editions this kit will not guess at for your jurisdiction",
    [
        ("The residential code edition my jurisdiction reviews to, and who "
         "told me:", [("Edition", 0.45), ("Source", 0.55)]),
        ("The NEC edition my electrical inspector reviews to:",
         [("Edition", 0.45), ("Source", 0.55)]),
    ])

# ---------------------------------------------------------------- energy
flow += k.h2_tight("THE ENERGY ANSWER — NO MANDATORY BLOWER DOOR", reserve=2.0)
flow.append(k.body(
    "Tennessee adopts the 2018 energy code on paper and then amends the parts "
    "with teeth back to <b>2009</b>. If you have built in a 2018 or 2021 IECC "
    "state, this will not be what you expect."))
rows = [
    [k.cellp("<b>Whole-house air leakage test</b>"),
     k.cellp("<b>Not mandatory.</b> The 2018 testing section is \"replaced "
             "with Section N1102.4.2.1 <b>Testing Option</b> and Section "
             "N1102.4.2.2 <b>Visual Inspection</b> from 2009 IRC\" — a choice "
             "between a test and a checklist inspection")],
    [k.cellp("<b>Duct testing and duct leakage</b>"),
     k.cellp("\"Duct Testing (Mandatory)\" and \"Duct Leakage (Prescriptive)\" "
             "are <b>optional</b>. Both of them")],
    [k.cellp("<b>Insulation and window tables</b>"),
     k.cellp("The 2018 tables are \"replaced with Table N1102.1… and Table "
             "N1102.1.2 Equivalent U-Factor <b>from 2009 IRC</b>.\" "
             "<b>Do not build to 2018 IECC R-values and assume they are "
             "required here</b>")],
    [k.cellp("<b>Rooms with fuel-burning appliances</b>"),
     k.cellp("Section N1102.4.4 is \"deleted in its entirety\"")],
    [k.cellp("<b>A separate energy inspection</b>"),
     k.cellp("There is none. \"Energy efficiency inspections shall occur "
             "during the required inspections\" (rule .07(2)(c))")],
]
flow.append(k.ref_table(
    "What Tennessee did to the energy code",
    [k.cellp("Provision", bold=True), k.cellp("Tennessee's treatment",
                                              bold=True)],
    rows, [1.95 * inch, CW - 1.95 * inch]))
flow.append(k.cite(
    "Quoted from rule 0780-02-23-.02(1)(a) items 5 to 8 and .02(1)(b). "
    "<b>The reverse error is also possible:</b> this is the state program's "
    "answer. An EXEMPT jurisdiction on a newer local code may well require a "
    "blower door. The paperwork that <i>is</i> required either way: blown or "
    "sprayed insulation needs \"a manufacturer's product data sheet and "
    "installation certificate stating the product meets or exceeds the energy "
    "code.\""))

# ---------------------------------------------------------------- the fee
flow += k.h2_tight("THE STATE PERMIT FEE, AND HOW IT IS COMPUTED", reserve=2.0)
flow.append(k.body(
    "This section applies in SRBP jurisdictions, and to anyone in an opt-out "
    "county buying a state permit voluntarily. The fee is banded on "
    "<b>estimated cost of construction</b> — and the state sets a floor under "
    "that estimate so you cannot shrink the fee by lowballing it."))
rows = [
    [k.cellp("$0 to $5,000"), k.cellp("$100", center=True)],
    [k.cellp("$5,001 to $100,000"), k.cellp("$350", center=True)],
    [k.cellp("$100,001 to $150,000"), k.cellp("$400", center=True)],
    [k.cellp("$150,001 to $200,000"), k.cellp("$450", center=True)],
    [k.cellp("$200,001 to $250,000"), k.cellp("$500", center=True)],
    [k.cellp("$250,001 to $300,000"), k.cellp("$550", center=True)],
    [k.cellp("$300,001 and up"),
     k.cellp("$550 for the first $300,000, plus $50 for each additional "
             "$50,000 or fraction of it", center=True)],
]
flow.append(k.ref_table(
    "Base permit fee — rule 0780-02-23-.08(1)",
    [k.cellp("Total construction cost", bold=True),
     k.cellp("Fee", bold=True, center=True)],
    rows, [CW - 2.6 * inch, 2.6 * inch]))
flow.append(k.cite(
    "The floor on your estimate, from the State Fire Marshal's fee page as it "
    "read on 25&#160;March 2026: \"<b>The cost of construction cannot be less "
    "than $60.57 per heated square foot of construction.</b>\" <b>Treat that "
    "figure as perishable</b> — it is published on a web page rather than in "
    "the rule, and the rule itself sets the floor by reference to ICC Building "
    "Valuation Data at a 0.60 cost modifier. Check it the week you file."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "A worked example, so the arithmetic is not a surprise", [
        Paragraph("A <b>2,000&#160;sq&#160;ft heated</b> house. Minimum "
                  "declarable cost is 2,000 × $60.57 = <b>$121,140</b>, which "
                  "lands in the $100,001–$150,000 band: <b>$400</b> base. The "
                  "HVAC and plumbing inspection is required on all new "
                  "construction and adds <b>$100</b>. If the footings are cast "
                  "separately from the slab, the slab inspection adds another "
                  "<b>$100</b>. <b>So $500, or $600 with a separate pour</b> — "
                  "with one re-inspection included free.", S["body"]),
        Paragraph("<b>The fee that hurts is the one for starting early.</b> "
                  "Anyone who begins work before obtaining the permit \"shall "
                  "be subject to an additional fee of <b>one hundred percent "
                  "(100%) of the required permit fee for each violation</b>\" "
                  "(rule .08(9)).", S["body"]),
    ]))

flow.append(Spacer(1, 2))
rows = [
    [k.cellp("Plumbing and mechanical inspection"), k.cellp("$100", center=True),
     k.cellp("Required on all new construction")],
    [k.cellp("Slab inspection, other than a monolith pour"),
     k.cellp("$100", center=True),
     k.cellp("When footing and slab are cast separately")],
    [k.cellp("Prefabricated wall inspection"), k.cellp("$100", center=True),
     k.cellp("If prefabricated walls are used")],
    [k.cellp("Re-inspection after more than one rejection"),
     k.cellp("$100", center=True), k.cellp("The first re-inspection is free")],
    [k.cellp("Consultation inspection, or a temporary CO"),
     k.cellp("$100", center=True), k.cellp("On request")],
    [k.cellp("Duplicate permit, if you lose it"), k.cellp("$10", center=True),
     k.cellp("Rule .05(8)")],
]
flow.append(k.ref_table(
    "The add-on fees — rule 0780-02-23-.08",
    [k.cellp("Fee", bold=True), k.cellp("Amount", bold=True, center=True),
     k.cellp("When", bold=True)],
    rows, [2.6 * inch, 0.9 * inch, CW - 3.5 * inch]))

flow.append(Spacer(1, 4))
flow.append(k.body(
    "<b>What the application itself must contain</b> is short: location, a "
    "description of the work, use and occupancy, the valuation, the square "
    "footage, and your signature. You must also <b>certify, with proof "
    "available on request, the \"availability of public sewer or a septic "
    "permit\"</b> — which is why the septic package below comes first. And "
    "usefully: \"proof of licensure is not required for a property owner "
    "purchasing the permit when the property owner is performing the work\" "
    "(rule .05(4))."))
flow.append(k.body(
    "<b>Two clocks start at issue.</b> Work must commence within "
    "<b>180&#160;days</b> or the permit is void, and the permit expires "
    "<b>two years</b> from issue or when the certificate of occupancy is "
    "issued, whichever comes first (rule .05(7)). Permits are "
    "non-transferable, and if you stop acting as the owner-builder and hire a "
    "contractor, a <b>new permit</b> is required."))

# ---------------------------------------------------------------- septic
flow += k.h2_tight("THE SEPTIC PACKAGE, IN ORDER", reserve=1.8)
flow.append(k.body(
    "One form covers it: <b>CN-0971, Application for Water Resources "
    "Services</b>. The septic construction permit is line item 1 on it."))
rows = [
    [k.cellp("<b>0</b>", center=True), k.cellp("<b>Is there sewer?</b>"),
     k.cellp("If a public sewer is accessible, TDEC \"shall <b>refuse</b> to "
             "grant a permit\" for a septic system (rule .06(2)). Settle this "
             "first")],
    [k.cellp("<b>1</b>", center=True),
     k.cellp("<b>Soil and site evaluation</b>"),
     k.cellp("Suitability is determined by a \"high or extra-high intensity "
             "soil map completed by an <b>approved soil consultant</b>.\" On a "
             "lot that is not part of a subdivision you may instead let TDEC's "
             "own staff evaluate the site")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("<b>Percolation test</b>, sometimes"),
     k.cellp("Conditional, not universal — it needs at least 24&#160;inches of "
             "undisturbed soil and a slope of 30% or less. TDEC must be "
             "notified <b>at least three days before</b> the test")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("<b>Construction permit</b>"),
     k.cellp("The operative permit: no one may \"construct, alter, extend or "
             "repair\" a system without one. It <b>expires in three years</b>")],
    [k.cellp("<b>4</b>", center=True),
     k.cellp("<b>Construction inspection</b>"),
     k.cellp("\"<b>No system shall be covered without the inspection and "
             "authorization of the Commissioner.</b>\" If the system has "
             "electrical components, an electrical inspector must approve them "
             "first")],
]
flow.append(k.ref_table(
    "The sequence, and what each step actually is",
    [k.cellp("", bold=True, center=True), k.cellp("Step", bold=True),
     k.cellp("What the rule says", bold=True)],
    rows, [0.35 * inch, 1.75 * inch, CW - 2.1 * inch]))
flow.append(k.cite(
    "Rule chapter 0400-48-01, \"Regulations to Govern Subsurface Sewage "
    "Disposal Systems\", TDEC Division of Water Resources. <b>Note the "
    "agency:</b> septic moved from the Department of Health to TDEC — the "
    "chapter's own administrative history records that it was \"renumbered from "
    "1200-01-06\", the Health Department's series. Any guide that sends you to "
    "the county health department is working from pre-2013 sources. Fees, from "
    "CN-0971: <b>$400</b> for the permit evaluation up to 1,000&#160;gallons "
    "per day, plus <b>$100</b> for the required conventional system "
    "construction inspection — <b>$500</b> for a normal house."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Two things about the septic permit that are pure Tennessee", [
        Paragraph("<b>It can gate your electricity.</b> Anyone intending to "
                  "construct a house \"shall furnish evidence to the official "
                  "electrical inspector that… an application for a subsurface "
                  "sewage disposal system construction permit has been made… "
                  "or… the house is served by a public sewerage system\" "
                  "(rule .06(5)(a)). Note it is an <i>application</i>, not an "
                  "issued permit. This does not apply \"[w]here there is an "
                  "established <b>countywide building permit program</b>\" — "
                  "so it bites hardest in exactly the rural counties that have "
                  "no building code.", S["body"]),
        Paragraph("<b>Nine counties are not served by a TDEC field office at "
                  "all.</b> Shelby, Madison, Davidson, Williamson, Hamilton, "
                  "Knox, Blount, Sevier and Jefferson are <i>contract "
                  "counties</i> — if you are in one of them, your county "
                  "environmental health office is the counter, not the state. "
                  "The commonly repeated version of this list names only five "
                  "and would misroute an application in four counties.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- well
flow += k.h2_tight("IF YOU ARE ON A WELL", reserve=2.0)
rows = [
    [k.cellp("<b>You may not drill it yourself</b>"),
     k.cellp("The rules bar <i>any person</i> from constructing a well except "
             "in accordance with the Water Wells Act and require a TDEC "
             "license to drill. TDEC states it flatly: Tennessee licensed "
             "<b>general contractors, electricians and plumbers are not "
             "permitted</b> to install or maintain wells, pumps or treatment "
             "systems unless separately licensed by TDEC")],
    [k.cellp("<b>Notice of Intent, before drilling</b>"),
     k.cellp("Filed by the owner or the driller <b>prior to commencement</b>, "
             "with a <b>$75</b> fee. \"No well or borehole shall be drilled "
             "unless the driller has documentation that a Notice of Intent has "
             "been filed.\" It <b>expires in 180&#160;days</b>")],
    [k.cellp("<b>Report of Well Driller, after</b>"),
     k.cellp("Within <b>60&#160;days</b> of completion — with the log, casing "
             "detail, static water level, and latitude and longitude to the "
             "nearest second. It must also confirm the <b>septic tank and "
             "field lines are 50&#160;feet or more from the well</b>")],
    [k.cellp("<b>Disinfection is mandatory</b>"),
     k.cellp("\"All water wells shall be disinfected upon completion\" to a "
             "chlorine residual of at least <b>100&#160;ppm</b>, left standing "
             "<b>not less than 12&#160;hours</b>, then pumped out")],
]
flow.append(k.ref_table(
    "The well sequence",
    [k.cellp("", bold=True), k.cellp("What the rule requires", bold=True)],
    rows, [1.95 * inch, CW - 1.95 * inch]))
flow.append(k.cite(
    "Chapter 0400-45-09, \"Water Well Licensing Regulations and Well "
    "Construction Standards\" — like the septic chapter, renumbered out of the "
    "Health Department's 1200 series. <b>A property-line rule worth knowing "
    "before you site the well:</b> new wells may not be closer than "
    "<b>10&#160;feet</b> to a property line, and a well between 10 and "
    "25&#160;feet of one requires <b>35&#160;feet of casing</b> set in grout "
    "(rule .10(2)(d)). Siting the well a few feet further in can save a great "
    "deal of casing."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "The 25-foot number in the well rules is not for your drinking water well",
    [
        Paragraph("The well chapter contains a second setback table, at rule "
                  "0400-45-09-.17, giving <b>25&#160;feet</b> from septic tanks "
                  "and drain fields. <b>That table is for closed-loop "
                  "geothermal boreholes.</b> For a water supply well the "
                  "distance is <b>50&#160;feet</b>, and it is stated three "
                  "separate times — in the septic chapter's table, in the well "
                  "chapter's Table A, and again on the driller's completion "
                  "report. A reader skimming the chapter and finding 25 feet "
                  "will site their well far too close.", S["body"]),
    ]))

# ---------------------------------------------------------------- stormwater
flow += k.h2_tight("STORMWATER — THE ONE-ACRE TEST, AND A DATE", reserve=2.0)
flow.append(k.body(
    "You need a construction stormwater permit if the work results in "
    "\"<b>the disturbance of 1 acre or more of total land area</b>.\" Most "
    "single-house lots stay under it. <b>What pushes owner-builders over is "
    "almost never the house.</b> Total land area includes the driveway, the "
    "septic field and its reserve area, the well pad, staging and spoil — and a "
    "long drive on a rural parcel adds up faster than people expect."))
flow.append(k.callout(
    "A dated change you need to be on the right side of", [
        Paragraph("Tennessee's construction general permit turned over while "
                  "this kit was being written. The outgoing permit expired "
                  "<b>30&#160;September 2026</b>; the <b>2026</b> permit took "
                  "effect <b>1&#160;October 2026</b> and runs to 2031. TDEC's "
                  "own notice warned that the forms would change on that date. "
                  "<b>If you are breaking ground on or after 1 October 2026, "
                  "make sure you are working from the 2026 permit and its "
                  "forms</b>, not a copy someone saved earlier.", S["body"]),
    ]))
flow.append(k.body(
    "<b>Separately, and more likely to catch you:</b> if your driveway crosses "
    "a stream or you disturb a wetland, that is an <b>Aquatic Resource "
    "Alteration Permit</b>, which is a different permit from a different "
    "program — and TDEC lists \"<b>road and utility "
    "crossings</b>\" among the activities that require one. General permits "
    "exist for routine crossings. A federal Army Corps permit and, near a TVA "
    "reservoir, a TVA approval may sit on top."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "And the one nobody sees coming: draining to a sinkhole makes it a well", [
        Paragraph("Tennessee is karst country, and its Underground Injection "
                  "Control rules define an <b>\"improved sinkhole\"</b> as \"a "
                  "naturally occurring karst depression <b>modified by man</b> "
                  "in such a manner that the chemical, physical, biological, "
                  "radiological, or bacteriological properties of the water or "
                  "fluids moving into the subsurface through it have been or "
                  "will be altered.\"", S["body"]),
        Paragraph("The same chapter defines an <b>injection well</b> to include "
                  "\"(c) <b>An improved sinkhole</b>\" and \"(e) Modified "
                  "recharge point,\" lists both among Class&#160;V wells, and "
                  "then requires that \"<b>all injection wells and activities "
                  "must be authorized by permit or by rule.</b>\"", S["body"]),
        Paragraph("<b>In plain terms:</b> route your driveway runoff, your roof "
                  "drains or a graded swale into a sinkhole on your lot and you "
                  "have arguably built a Class&#160;V injection well. Filling "
                  "or grading around a sinkhole is not neutral earthwork in "
                  "Tennessee. Many Class&#160;V wells are authorized by rule "
                  "rather than by individual permit, so this is usually a "
                  "conversation rather than a catastrophe — but it is one to "
                  "have with the field office <i>before</i> the excavator "
                  "arrives.", S["body"]),
    ]))
flow.append(k.cite(
    "Chapter 0400-45-06, \"Underground Injection Control\", revised November "
    "2024 — another chapter renumbered out of the Health Department's 1200 "
    "series. <b>We have deliberately not printed a fee</b>, because the "
    "chapter's fee rule was not read. Note also that the UIC chapter defines a "
    "<i>septic system</i> as \"a 'well' that is used to emplace sanitary waste "
    "below the surface\" — which is why the septic chapter excludes sinkholes "
    "from usable area and the UIC chapter regulates altering them. The two "
    "point the same way."))

# ---------------------------------------------------------------- record
flow += k.h2_tight("PERMIT RECORD — FILL THIS IN AS EACH ONE ISSUES",
                   reserve=1.6)
flow += k.check_table(
    "Every approval on this build",
    [
        ("<b>Septic construction permit</b> — or written confirmation that "
         "public sewer is available:",
         [("Number", 0.4), ("Issued", 0.3), ("Expires", 0.3)]),
        ("<b>Septic construction inspection</b> passed, before covering:",
         [("Date", 0.5), ("Inspector", 0.5)]),
        ("<b>Notice of Intent to drill</b> filed, and the driller's TDEC "
         "license number:", [("NOI number", 0.5), ("Driller license", 0.5)]),
        ("<b>Report of Well Driller</b> received — due within 60&#160;days of "
         "completion:", [("Date received", 0.5), ("Well ID", 0.5)]),
        ("<b>Building permit</b>, if one exists where I am building:",
         [("Number", 0.4), ("Issued", 0.3), ("Expires", 0.3)]),
        ("<b>Electrical permit</b>:",
         [("Number", 0.4), ("Issued", 0.3), ("Amps", 0.3)]),
        ("<b>Zoning approval</b>:", [("Reference", 0.5), ("Date", 0.5)]),
        ("<b>Floodplain determination</b> — in or out of the mapped hazard "
         "area:", [("Result", 0.5), ("Who confirmed", 0.5)]),
        ("<b>Driveway or culvert permit</b>, and whether the crossing needed "
         "an ARAP:", [("Permit", 0.5), ("ARAP needed?", 0.5)]),
        ("<b>Stormwater</b> — total disturbed area I calculated, and whether "
         "it reached one acre:", [("Acres", 0.4), ("Permit if needed", 0.6)]),
        ("<b>911 address</b> assigned:", [("Address", 0.6), ("Date", 0.4)]),
        ("<b>Certificate of occupancy</b>, if one is issued where I am "
         "building:", [("Number", 0.5), ("Date", 0.5)]),
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "tn-permit-kit",
                       "TN.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
