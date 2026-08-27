#!/usr/bin/env python3
"""MI.2 Permit Application Checklist — Michigan Edition.

Sources verified August 2026 (see the on-page sources tables):
  MCL 125.1510(1)      written application, verified affidavit of the SPECS,
                       full plans to scale, site plan, owner in fee named
  MCL 125.1510(6)      separate permits for particular kinds of work
  MCL 125.1510(7),(8)  no permit for ordinary repairs; no permit for a
                       building incidental to agricultural use of the land
  MCL 339.2012(1)(c),(d) and (2)  the architect/engineer seal exemptions and
                       the DEFINITION of "calculated floor area" — the trap
  MCL 324.9105(1), 9106, 9112, 9116  soil erosion: county unless a
                       municipality has assumed it; permit runs with the land;
                       control duty applies whether or not a permit is needed
  BCC-324 (04/2024)    the state Building Permit Application: the five
                       environmental control approvals, the 3,500 sq ft seal
                       statement, 2 sets of documents, 180-day expiry, the
                       2-business-day / 5-business-day inspection practice
  BCC Fee Schedule, effective April 1, 2024, and its Square Foot Construction
                       Cost Table (R-3 row) — state-enforced jurisdictions
  LARA BCC             the 2021 Residential/Energy rule sets are enjoined;
                       2015 IRC and 2015 IECC residential remain in effect

Deliberately NOT printed: a numeric soil-erosion acreage trigger. That figure
lives in the Part 91 administrative rules rather than in Part 91 itself, and
this kit does not print a number it has not read in its own source.
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

FORM_ID = "MI.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Application"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Everything a Michigan owner-builder gathers, verifies, and files — "
    "organized around the five approvals the State's own permit application "
    "asks your enforcing agency to sign off.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- gates
flow += k.h2_tight("THE FIVE APPROVALS PRINTED ON THE STATE'S OWN FORM")
flow.append(k.body(
    "Page 3 of the Bureau of Construction Codes' Building Permit Application "
    "carries a block headed <b>Environmental Control Approvals</b>, with a "
    "row for the enforcing agency to record whether each one was required, "
    "whether it was approved, and its date and number. It is the closest "
    "thing Michigan has to a statewide pre-permit checklist, and every one "
    "of the five is handled by <b>somebody other than the building "
    "inspector</b>."))

flow.append(k.bullet(
    "<b>A — Zoning.</b> Your township, city or village. Use, setbacks, "
    "height, lot coverage, accessory buildings. Zoning is <i>not</i> part of "
    "the construction code and is never preempted by it."))
flow.append(k.bullet(
    "<b>B — Fire District.</b> Your local fire authority. Commonly access, "
    "turnaround and water supply on rural parcels."))
flow.append(k.bullet(
    "<b>C — Health Department.</b> Your county or district health "
    "department: septic and private well. On a rural lot this is the long "
    "pole — start it first."))
flow.append(k.bullet(
    "<b>D — Soil Erosion.</b> Your county enforcing agency, unless your "
    "municipality has adopted its own approved ordinance (MCL 324.9105, "
    "9106)."))
flow.append(k.bullet(
    "<b>E — Flood Zone.</b> Floodplain review, where the parcel sits in a "
    "mapped special flood hazard area."))

flow.append(Spacer(1, 6))
flow.append(k.callout("Work these five backwards from the one that takes longest", [
    Paragraph("Owner-builders routinely fill in the building permit "
              "application first and then discover that the septic "
              "evaluation cannot be scheduled until the frost is out of the "
              "ground, or that the soil erosion permit is issued by an "
              "office in a different building than the one taking their "
              "plans. <b>Start C (health department) the day you have a "
              "parcel</b> — before you buy it, if you still can — and treat "
              "A, B, D and E as parallel tracks that all have to land before "
              "your building permit can issue.", S["body"]),
]))
flow.append(k.cite(
    "Bureau of Construction Codes Building Permit Application, form BCC-324 "
    "(04/2024), page 3, \"Environmental Control Approvals,\" read at "
    "michigan.gov/lara in August 2026. Local enforcing agencies use their "
    "own application forms; the five approvals behind the block are the "
    "same, but the form you fill in will look different."))

# ---------------------------------------------------------------- A
flow += k.h2_tight("A. SITE AND PROJECT VERIFICATION")
flow += k.check_table("A1: Before anything else", [
    "Confirmed <b>which agency issues each of your four permits</b> — "
    "township, city, village, county, or the State. Do MI.4 first; in "
    "Michigan this is not a formality",
    ("Parcel number and 911 address confirmed",
     [("Parcel #:", 0.55), ("Address:", 0.45)]),
    "Deed recorded in your name — the exemption belongs to \"an owner of "
    "property\"",
    "Zoning district and permitted use verified with the township, city or "
    "village",
    ("Required setbacks confirmed in writing",
     [("Front:", 0.25), ("Side:", 0.25), ("Rear:", 0.25), ("Other:", 0.25)]),
    "Easements, rights-of-way, and recorded restrictions identified",
    "Flood zone status checked; floodplain requirements identified if in a "
    "mapped special flood hazard area",
    "Driveway / road tie-in requirement confirmed with the county road "
    "commission (or MDOT if you connect to a state trunkline)",
    "HOA or covenant approval obtained if applicable — private, not "
    "governmental; no agency will check it for you",
], notes_header="Notes / who confirmed")

# ---------------------------------------------------------------- B
flow += k.h2_tight("B. THE APPLICATION PACKAGE")
flow.append(k.body(
    "Michigan tells you what the application must contain, in the statute "
    "itself: \"<i>a detailed statement in writing, verified by affidavit of "
    "the individual making it, of the specifications for the building or "
    "structure, and full and complete copies of the plans drawn to scale of "
    "the proposed work</i>,\" plus \"<i>a site plan showing the dimensions, "
    "and the location of the proposed building or structure and other "
    "buildings or structures on the same premises</i>,\" and the full name "
    "and street address of <b>the owner in fee</b> of the land."))

flow += k.check_table("B1: Forms and proofs", [
    "Building permit application, completed and signed — the signature sits "
    "under the section 23a warning; read it (see MI.1)",
    "Separate <b>electrical</b>, <b>plumbing</b> and <b>mechanical</b> "
    "permit applications — confirm whether each goes to the same office",
    ("Estimated project cost stated", [("Stated cost: $", 1.0)]),
    "Workers' compensation carrier, employer identification number, and "
    "unemployment agency number — or the <b>reason for exemption</b> for "
    "each. The state form gives you a line for the reason",
    "Any local homeowner affidavit or homeowner-permit acknowledgement your "
    "enforcing agency uses — read it before signing; its terms are local",
], notes_header="Notes")

flow += k.check_table("B2: Plans and supporting drawings", [
    "<b>Two sets</b> of construction documents (the state's requirement; "
    "confirm the count and format your agency wants — many now take digital)",
    "Site plan showing dimensions, the proposed building, every other "
    "structure on the premises, well and septic locations, and the driveway",
    "Foundation plan, floor plans, elevations, wall sections, framing plan",
    "Electrical, plumbing and mechanical layouts as your agency requires",
    ("Energy compliance documentation (see section D)",
     [("Path used:", 1.0)]),
    "Engineered or manufacturer specifications for anything non-standard — "
    "trusses, ICF, SIPs, long spans, deep or stepped foundations",
    ("<b>Calculated floor area</b> worked out and written down — this "
     "decides whether your plans need a seal",
     [("Calculated floor area:", 1.0)]),
], notes_header="Notes")

# ---------------------------------------------------------------- the trap
flow += k.h2_tight("THE 3,500 SQUARE FOOT RULE — MEASURED IN A WAY NOBODY EXPECTS")
flow.append(k.body(
    "Michigan requires construction documents to be sealed and signed by a "
    "licensed architect or professional engineer, and then exempts small "
    "houses. The state permit application prints the rule like this: "
    "\"<i>The seal and signature is not required for one- and two-family "
    "dwellings less than 3,500 square feet of calculated floor area.</i>\" "
    "Every Michigan summary repeats the number. Almost none of them prints "
    "the definition — and the definition is the whole rule."))

flow.append(k.callout(
    "\"Calculated floor area\" is habitable space only", [
        Paragraph("The Occupational Code defines it: \"<i><b>Calculated "
                  "floor area</b> means that portion of the total gross area "
                  "measured to the outside surfaces of exterior walls "
                  "intended to be <b>habitable space</b></i>.\" And then "
                  "defines that: \"<i><b>Habitable space</b> means space in "
                  "a building used for living, sleeping, eating, or cooking. "
                  "Habitable space <b>does not include</b> a heater or "
                  "utility room, a crawl space, a basement, an attic, a "
                  "garage, an open porch, a balcony, a terrace, a court, a "
                  "deck, a bathroom, a toilet room, a closet, a hallway, a "
                  "storage space, and other similar spaces</i>.\"",
                  S["body"]),
        Paragraph("Read that list again. <b>Basements, garages, attics, "
                  "bathrooms, closets, hallways, utility rooms, decks and "
                  "porches all come out.</b> A house a builder would market "
                  "as 4,200 square feet can sit comfortably under 3,500 "
                  "square feet of calculated floor area once the two "
                  "bathrooms, the mudroom, the stair hall, the walk-in "
                  "closets and the attached garage are removed — and it is "
                  "the calculated figure, not the marketing figure, that the "
                  "statute uses.", S["body"]),
        Paragraph("Two practical consequences. First, do the arithmetic "
                  "before you assume you need to pay for a sealed plan set; "
                  "plenty of Michigan owner-builders buy one they did not "
                  "need. Second, <b>show your work on the application</b> — "
                  "write the calculated floor area down and be ready to "
                  "explain which spaces you excluded and why, because the "
                  "plan reviewer is looking at the same definition.",
                  S["body"]),
    ]))

flow.append(k.body(
    "There is also a <b>second, separate exemption</b> that owner-builders "
    "almost never hear about, and it has no square-footage limit at all: the "
    "article does not apply to \"<i>an owner doing architectural, "
    "engineering, or surveying work upon or in connection with the "
    "construction of a building on the owner's property for the owner's own "
    "use to which employees and the public are not generally to have "
    "access</i>.\" That is a description of a house you are designing for "
    "yourself. Ask your enforcing agency how they apply it before you "
    "conclude either way — reviewers differ, and the seal question is worth "
    "settling in writing rather than in argument."))
flow.append(k.cite(
    "MCL 339.2012(1)(c), (1)(d) and (2)(a)–(b), Occupational Code. The "
    "3,500-square-foot statement is quoted from the Bureau of Construction "
    "Codes' Building Permit Application, form BCC-324 (04/2024), page 2, "
    "which cites 1980 PA 299. Note the form also exempts \"public works less "
    "than $15,000 in total construction cost\" — that is MCL 339.2011(2) and "
    "has nothing to do with your house. Verified August 2026."))

# ---------------------------------------------------------------- C
flow += k.h2_tight("C. SEPTIC, WELL, AND SOIL EROSION — NOT THE BUILDING OFFICE")
flow.append(k.body(
    "On a rural Michigan parcel these three approvals sit on separate "
    "tracks, with separate offices and separate timelines, and two of them "
    "can stop your building permit. None of them is handled by the person "
    "who reviews your plans."))

flow += k.check_table("C1: Septic and well — county or district health department", [
    "Health department identified — Michigan counties are served either by a "
    "county health department or by a multi-county <b>district</b> health "
    "department; find out which is yours",
    "Soil evaluation / percolation test applied for as early in the year as "
    "the ground allows",
    ("Septic permit issued — system type and drainfield location fixed",
     [("Permit #:", 0.55), ("Date:", 0.45)]),
    "Drainfield and reserve area shown on your site plan and consistent with "
    "the house footprint, the well, and the driveway",
    ("Well permit obtained from the health department <b>before</b> drilling",
     [("Permit #:", 0.55), ("Date:", 0.45)]),
    "Water sample submitted and results received after the well is completed "
    "— confirm who draws it and who pays",
    "Confirmed whether your health department's sign-off must reach the "
    "building office before the building permit can issue, or alongside it",
], notes_header="Notes")

flow.append(k.callout("Why your septic rules are local — and what that means", [
    Paragraph("Michigan has <b>no statewide sanitary code</b> for onsite "
              "wastewater. A house system is legal as a groundwater "
              "discharge that needs no state permit, on one condition: it is "
              "\"<i>less than 1,000 gallons per day and the disposal system "
              "is approved by the county, district, or city health "
              "department that has jurisdiction in accordance with <b>either "
              "the requirements of the local sanitary code or</b> the "
              "provisions of the publication entitled 'Michigan Criteria for "
              "Subsurface Sewage Disposal,' April 1994</i>.\" "
              "(R 323.2210(a)(i))", S["body"]),
    Paragraph("That <i>either/or</i> is the whole story: your health "
              "department picks its own yardstick, and the Criteria say they "
              "are only a floor. So there is no Michigan setback, tank size "
              "or perc figure to print — <b>ask yours, in writing, before "
              "you site the house.</b>", S["body"]),
]))
flow.append(k.cite(
    "Mich. Admin. Code R 323.2210(a)(i) (Part 22 groundwater rules under "
    "Part 31 of NREPA) is the provision that makes a house septic system "
    "lawful without a state permit. The <i>Michigan Criteria for Subsurface "
    "Sewage Disposal</i> (April 1994, originally Michigan Department of "
    "Public Health, now hosted by EGLE) is a <b>guideline</b> by its own "
    "terms — it \"<i>does not have the force or effect of law</i>\" as to "
    "you — but a health department that has adopted it is expected to "
    "follow it and may not approve proposals that do not meet it except by "
    "variance. Local authority: MCL 333.2441, under which local health "
    "department regulations \"<i>shall be at least as stringent as the "
    "standard established by state law</i>\" and \"<i>supersede inconsistent "
    "or conflicting local ordinances</i>.\" EGLE: onsite wastewater is a "
    "required local health department service, and roughly 35% of Michigan "
    "residents are on a private septic system. Legislation to create a "
    "statewide code (SB 771 of 2026) had not passed the Senate as of August "
    "2026. Verified August 2026."))

flow += k.check_table("C2: Soil erosion and sedimentation control (Part 91)", [
    "Identified your enforcing agency: the <b>county</b> is responsible "
    "throughout the county <i>unless</i> your municipality has adopted its "
    "own department-approved ordinance",
    ("Total earth change measured — house, driveway, septic field, staging "
     "and spoil. <b>One acre or more triggers a permit</b>",
     [("Acres disturbed:", 1.0)]),
    ("Measured to the <b>water's edge</b> of the nearest lake or stream — "
     "<b>within 500 feet triggers a permit regardless of acreage</b>",
     [("Distance:", 1.0)]),
    "Confirmed whether a stricter local ordinance applies — a municipality's "
    "department-approved ordinance may set the bar lower",
    ("Permit obtained before any earth is moved",
     [("Permit #:", 0.55), ("Date:", 0.45)]),
    "Controls actually installed and maintained — silt fence, inlet "
    "protection, stabilised construction entrance, seeding",
    "If you are <b>buying</b> a parcel that already has an SESC permit: got "
    "the written transfer notice from the seller",
], notes_header="Notes")

flow.append(k.callout(
    "The trigger, the hard stop, and the detail that catches people", [
        Paragraph("<b>The trigger is one acre or 500 feet.</b> \"<i>A "
                  "landowner or designated agent who contracts for, allows, "
                  "or engages in, an earth change in this state shall obtain "
                  "a permit from the appropriate enforcing agency before "
                  "commencing an earth change which disturbs <b>1 or more "
                  "acres of land</b> or which is <b>within 500 feet of the "
                  "water's edge of a lake or stream</b></i>.\" Note "
                  "<i>water's edge</i> — not the shoreline, not the ordinary "
                  "high-water mark. And \"lake\" is defined to mean a water "
                  "body of <b>1 acre or more</b>, so a small farm pond does "
                  "not pull you in. (R 323.1704(1); R 323.1701(1)(d))",
                  S["body"]),
        Paragraph("<b>It gates your building permit — and this rule is the "
                  "one to quote at the counter.</b> \"<i>A local agency or "
                  "general law township <b>shall not issue a building "
                  "permit</b> to a person engaged in an earth change if the "
                  "change requires a permit under part 91 or these rules "
                  "<b>until</b> the county or local enforcing agency has "
                  "issued the required state-prescribed permit</i>.\" There "
                  "is no equivalent anywhere in Part 91 itself — the "
                  "sequencing exists only in the rules. (R 323.1711(2))",
                  S["body"]),
        Paragraph("<b>The duty applies even below the threshold, and the "
                  "permit runs with the land.</b> An owner whose earth change "
                  "may contribute to sedimentation \"<i>shall implement and "
                  "maintain</i>\" controls regardless (MCL 324.9116); and on "
                  "a transfer the permit, its conditions <i>and "
                  "responsibility for existing violations</i> pass to the "
                  "buyer (MCL 324.9112(2)–(5)).", S["body"]),
    ]))
flow.append(k.cite(
    "Soil erosion: the numeric trigger and the building-permit hard stop are "
    "in the administrative rules promulgated under MCL 324.9104 — Mich. "
    "Admin. Code R 323.1701 to R 323.1714, read at "
    "ars.apps.lara.state.mi.us — <b>not</b> in Part 91 itself, which is why "
    "most summaries cite the statute and get the numbers from somewhere "
    "else. Permit trigger and definitions, R 323.1704(1) and R 323.1701(1)(d); "
    "building permit gate, R 323.1711(2); exemptions including the 24-hour "
    "stabilization rule and the discretionary waiver for earth changes under "
    "<b>225 square feet</b>, R 323.1705. Statute: county responsibility, MCL "
    "324.9105(1); municipal ordinances, which must be department-approved "
    "and may be <b>more restrictive</b>, MCL 324.9106(1)–(2); transfer, MCL "
    "324.9112; owner's control duty, MCL 324.9116. EGLE's program FAQ closes "
    "the loophole builders try to walk through: \"<i>cutting trees and "
    "removing stumps to accommodate future development activities is not "
    "'logging' and permits are required</i>.\" Verified August 2026."))

# ---------------------------------------------------------------- D
flow += k.h2_tight("D. CODE EDITIONS — MICHIGAN IS NOT WHERE THE TABLES SAY IT IS")
flow.append(k.body(
    "One code book covers your whole house. The Bureau states it for each "
    "trade in turn: \"<i>provisions for one- and two-family dwellings are "
    "included in the Michigan Residential Code</i>\" — building, electrical, "
    "mechanical and plumbing alike. You do not need to buy the Michigan "
    "Building, Plumbing or Mechanical Codes to build a house. You need the "
    "<b>Michigan Residential Code</b>."))

flow.append(k.callout(
    "Buy the 2015 book. A court order is why.", [
        Paragraph("Michigan adopted rule sets that would have updated the "
                  "Michigan Residential Code and the residential chapter of "
                  "the Energy Code to the <b>2021</b> IRC and 2021 IECC, "
                  "\"<i>set to become effective on August 29, 2025</i>.\" "
                  "They never took effect. On <b>July 7, 2025</b> the "
                  "Michigan Court of Claims issued a stipulated order in "
                  "<i>Home Builders Assoc et al. v LARA et al.</i> "
                  "temporarily preventing LARA from \"<i>taking additional "
                  "steps necessary to apply or implement</i>\" both rule "
                  "sets while the litigation continues.", S["body"]),
        Paragraph("LARA's own notice states the consequence: \"<i>While this "
                  "stipulated order remains in place, the <b>2015</b> "
                  "versions of the IRC and residential provisions of the "
                  "IECC standards currently adopted, in part, by each rule "
                  "set will remain valid and in effect.</i>\"", S["body"]),
        Paragraph("This is why \"adopted codes by state\" tables get "
                  "Michigan wrong. The rules were filed and carried a real "
                  "effective date, so the tables flipped Michigan to 2021 — "
                  "and then a court froze them seven weeks beforehand. Buy "
                  "the wrong edition and your wall assemblies, your "
                  "fenestration values and your air-sealing obligations are "
                  "all from a code that does not apply to you. <b>Confirm "
                  "the edition with your enforcing agency before you draw "
                  "plans</b>, because this one can change with a court "
                  "order rather than a legislative session.", S["body"]),
    ]))
flow.append(k.cite(
    "LARA Bureau of Construction Codes, \"2021 Code Injunction — Residential "
    "Part 5 and Energy Part 10,\" published at michigan.gov/lara and still "
    "the document linked from the Bureau's Part 5 and Part 10 entries when "
    "read in August 2026. The two rule sets are 2022-16-LR Construction Code "
    "— Part 5. Residential Code, and 2021-48 LR Construction Code — Part 10. "
    "Michigan Uniform Energy Code; both were still listed among the Bureau's "
    "currently-open rules at that date. Michigan's <b>electrical</b> code is "
    "a separate rule set (Part 8) and was not enjoined — it is also under "
    "active revision, with a public advisory meeting held in August 2026, so "
    "confirm the NEC edition your agency is enforcing before you buy wire."))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>The energy code is a separate rule set from the residential code, "
    "and the two tests it puts on you are not equally binding.</b> "
    "Residential energy sits in <b>Part 10</b>, which adopts the residential "
    "provisions of the <b>2015 IECC</b>. Michigan spans <b>three climate "
    "zones and only three</b> — 5A across the south, 6A through the northern "
    "Lower Peninsula and eastern UP, and 7 in ten western UP counties — with "
    "a county-by-county table in the code itself. Look yours up rather than "
    "guessing from latitude."))
flow.append(k.callout(
    "Duct testing is mandatory. The blower door is not.", [
        Paragraph("<b>Duct leakage: 4 cfm at 25 Pa per 100 square feet of "
                  "conditioned floor area, and the code labels it "
                  "\"(mandatory).\"</b> At rough-in the figure is 4 cfm, or 3 "
                  "cfm where the air handler is not yet installed. The real "
                  "way out is structural, not procedural: \"<i>the total "
                  "leakage test is not required for ducts and air handlers "
                  "located entirely within the building thermal "
                  "envelope</i>.\" Keep the ducts inside and the test "
                  "disappears.", S["body"]),
        Paragraph("<b>Air leakage: 4 ACH50 — labeled \"(prescriptive).\"</b> "
                  "Two changes from the base 2015 IECC, which sets 3 ACH50 "
                  "and marks it mandatory: Michigan loosened the number "
                  "<i>and</i> the status. Prescriptive means it is avoidable "
                  "by complying through the performance or energy-rating-"
                  "index path instead. Most summaries report these two "
                  "backwards.", S["body"]),
    ]))

flow += k.check_table("D1: Code and energy", [
    ("Edition of the Michigan Residential Code your agency is enforcing, "
     "confirmed in writing", [("Edition:", 0.5), ("Confirmed:", 0.5)]),
    ("NEC edition adopted by Michigan Part 8 rules, confirmed separately — "
     "it does not move with the residential code",
     [("NEC edition:", 0.5), ("Confirmed:", 0.5)]),
    ("Climate zone for your county looked up in the Part 10 table — 5A, 6A "
     "or 7", [("Climate zone:", 1.0)]),
    "Insulation R-values for walls, ceiling, floors and foundation shown on "
    "the plans",
    "Window and door U-factor and SHGC values documented",
    ("Compliance path chosen — prescriptive, simulated performance, or "
     "energy rating index. This decides whether you owe a blower-door result",
     [("Path:", 1.0)]),
    ("Duct leakage test arranged — this one is mandatory unless every duct "
     "and the air handler sit inside the thermal envelope",
     [("Tester:", 0.6), ("Result:", 0.4)]),
    "Ground snow load for your site obtained and given to whoever sizes your "
    "roof framing — Michigan's range is wide and the lake-effect belts are "
    "the high end",
], notes_header="Notes")
flow.append(k.cite(
    "Residential energy: Mich. Admin. Code <b>Part 10</b>, Michigan Uniform "
    "Energy Code — R 408.31059 adopts \"<i>the residential provisions of the "
    "international energy conservation code, 2015 edition</i>\"; duct "
    "leakage, R 408.31066; air leakage, R 408.31069; climate zone table, "
    "R 408.31060e, matched by the Residential Code's own Table N1101.10 at "
    "R 408.30547c. The Michigan Residential Code points there: \"<i>buildings "
    "shall be designed and constructed in accordance with the Michigan "
    "uniform energy code part 10 rules</i>\" (R 408.30524). <b>Do not use "
    "Part 10a</b> — that is the <i>commercial</i> energy code (2021 IECC and "
    "ASHRAE 90.1-2019, effective April 22, 2025) and it expressly excludes "
    "residential buildings. Verified August 2026."))

# ---------------------------------------------------------------- E
flow += k.h2_tight("E. FEES, AND THE CLOCKS THAT START WHEN THE PERMIT ISSUES")
flow.append(k.body(
    "Local fee schedules are local — ask for yours in writing. But if the "
    "<b>State</b> is your enforcing agency, the schedule is published, and "
    "it works in a way worth understanding even if it is not yours."))

fee_rows = [
    [k.cellp("<b>The fee is not based on your estimated cost</b>"),
     k.cellp("The state computes a \"total cost of improvement\" from its "
             "own <b>Square Foot Construction Cost Table</b>. For use group "
             "R-3 — one- and two-family — the table runs from $122.74 per "
             "square foot for Type IA construction down to <b>$95.34 for "
             "Type VB</b>, which is ordinary wood framing. Unfinished "
             "basements are computed separately at <b>20%</b> of table cost. "
             "Understating your build cost does not lower the fee.")],
    [k.cellp("<b>The building permit fee itself</b>"),
     k.cellp("Banded: $435.00 plus $2 per $1,000 over $100,000 in the "
             "$100,000–$500,000 band. The first $100.00 of an application "
             "fee is non-refundable. Plan review for state-issued permits is "
             "assessed at 30% of the building permit fee.")],
    [k.cellp("<b>Certificate of occupancy</b>"),
     k.cellp("$50.00, and required for all building permits except "
             "demolition permits.")],
    [k.cellp("<b>Trade permits</b>"),
     k.cellp("Each carries its own $75.00 non-refundable application fee, "
             "then per-item charges — electrical is priced per circuit, per "
             "service size, per 25 fixtures/outlets, and so on.")],
    [k.cellp("<b>Letting a permit lapse</b>"),
     k.cellp("$75.00 to re-open. Closed permits cannot be refunded.")],
]
flow.append(k.ref_table(
    "How the State's own fee schedule works (state-enforced jurisdictions)",
    [k.cellp("Item", bold=True), k.cellp("What it means for you", bold=True)],
    fee_rows, [2.1 * inch, CW - 2.1 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout("The 180-day rule — and the trap inside it", [
    Paragraph("\"<i>A permit remains valid as long as work is progressing, "
              "and inspections are requested and conducted. A permit shall "
              "become invalid if the authorized work is not commenced within "
              "180 days after issuance of the permit or if the authorized "
              "work is suspended or abandoned for a period of 180 days after "
              "the time of commencing the work.</i>\"", S["body"]),
    Paragraph("Then the sentence people miss, printed in capitals on the "
              "state's form: \"<i>A PERMIT WILL BE CLOSED WHEN NO "
              "INSPECTIONS ARE REQUESTED AND CONDUCTED WITHIN 180 DAYS OF "
              "THE DATE OF ISSUANCE OR THE DATE OF A PREVIOUS "
              "INSPECTION.</i>\" It is not enough to be working. The clock "
              "resets on <b>inspections</b>, not on effort — which is "
              "exactly the way a part-time owner-builder gets caught over a "
              "Michigan winter. If a long gap is coming, call an inspection "
              "you can pass before it starts.", S["body"]),
]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>What the State says about its own turnaround:</b> \"<i>the inspector "
    "will respond to an inspection request within two (2) business days to "
    "schedule the inspection. Inspections are typically performed within "
    "five (5) business days subject to the inspection schedule.</i>\" That "
    "is published practice for state-issued permits, not a statutory "
    "deadline, and it does not bind a local enforcing agency. Ask yours what "
    "to expect and write it in MI.4."))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Application filed:", 0.34), ("Permit issued:", 0.33),
                         ("Permit #:", 0.33)]))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 10))
flow.append(k.sources_table([
    ("Written application, verified affidavit of the specifications, full "
     "plans to scale, site plan, owner in fee named", "MCL 125.1510(1)"),
    ("Separate permits may be required for particular kinds of work, "
     "including plumbing and electrical", "MCL 125.1510(6)"),
    ("No building permit for ordinary repairs; none for a building "
     "incidental to agricultural use of the land",
     "MCL 125.1510(7), (8)"),
    ("Seal not required for 1- and 2-family dwellings under 3,500 sq ft of "
     "calculated floor area — which is habitable space only, excluding "
     "basements, garages, baths, closets, halls and utility rooms; plus a "
     "separate owner design exemption with no area limit",
     "MCL 339.2012(1)(c), (1)(d), (2); 339.2014(e)"),
    ("Septic: no statewide sanitary code — a house system is a permit-exempt "
     "discharge approved by the local health department under its own code "
     "or the 1994 Criteria", "R 323.2210(a)(i); MCL 333.2441"),
    ("Soil erosion permit: 1 or more acres, or within 500 feet of the "
     "water's edge of a lake or stream", "R 323.1704(1)"),
    ("No building permit may issue until the soil erosion permit has",
     "R 323.1711(2)"),
    ("County enforces countywide unless a municipality has an approved, "
     "possibly stricter ordinance; permit and violations transfer with the "
     "land; control duty applies regardless of threshold",
     "MCL 324.9105(1), 9106, 9112, 9116"),
    ("The 2021 IRC/IECC rule sets are enjoined; the 2015 editions remain in "
     "effect", "LARA BCC, 2021 Code Injunction notice"),
    ("Residential energy is Part 10 (2015 IECC): zones 5A/6A/7, duct leakage "
     "mandatory at 4 cfm, air leakage 4 ACH50 prescriptive",
     "R 408.31059, .31066, .31069"),
    ("Five environmental control approvals; two sets of construction "
     "documents; 180-day expiry and closure",
     "BCC-324 (04/2024), pp. 2–3"),
    ("State fee bands, $50 certificate of occupancy, $75 re-open, 30% plan "
     "review, R-3 square-foot cost table",
     "BCC Fee Schedule, eff. April 1, 2024"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "mi-permit-kit",
                       "MI.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
