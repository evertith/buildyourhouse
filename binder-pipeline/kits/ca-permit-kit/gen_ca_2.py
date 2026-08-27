#!/usr/bin/env python3
"""CA.2 Permit Application Checklist — California Edition.

Sources verified August 2026 (see the on-page sources tables):
  H&S 19825          the statutory permit application; ID and signature
                     verification; agent authorization in (b)
  Lab 3800(a)        comp declaration under penalty of perjury, per 19825
  Ed Code 17620(b)   NO BUILDING PERMIT without school district certification
  Ed Code 17620(c)   or, if the district elected Gov 66007(a), no final
                     inspection / certificate of occupancy instead
  H&S 18938.5(a)     code edition locks at APPLICATION SUBMITTAL date
  H&S 18938.6        commence within 12 months; 180-day written extensions
  CRC 1.1.8/1.1.8.1  local amendments: more restrictive only, express findings
                     on climatic/topographical/geological conditions, FILED
                     with BSC (fire districts with HCD); effective date = date
                     filed
  CRC 1.1.9          only standards effective at application submittal apply
  2025 CRC Ch. 44    NFPA 70-23 => the CURRENT California Electrical Code is
                     built on the 2023 NEC. (2022 CRC referenced NFPA 70-20.)
                     Read out of the code's own referenced-standards table,
                     which is better evidence than any agency summary.
  2025 CRC R309.2    "An automatic sprinkler system shall be installed in one-
                     and two-family dwellings." NO new-construction exception,
                     NO fire-zone trigger. WAS R313.2 before the 2025 edition
                     renumbered Chapter 3 — R313 is now Ceiling Height.
  2025 CRC R337      now only a signpost: WUI provisions moved to the new
                     Title 24 PART 7, California Wildland-Urban Interface Code
  PRC 4291 /         100 ft defensible space (SRA / local VHFHSZ); the
  Gov 51182          (a)(5) pre-construction certification for insurance;
                     ember-resistant zone deferred for new structures until
                     the Board of Forestry updates regs + guidance
                     (both Stats. 2025, Ch. 731 — AB 1455, eff. Oct 13 2025)
  Wat 13750.5        C-57 Water Well Contractor's License required to drill —
                     no owner exception
  SWRCB OWTS Policy  adopted Apr 18 2023, OAL-approved Sep 26 2023; LAMPs

  H&S 19825(c)       the Notice to Property Owner / Owner's Acknowledgment —
                     12 initialed items, on the ISSUER's letterhead, signed
                     and returned BEFORE the permit issues
  2025 Energy Code   PV required on all single-family: 702.3.1 [old
                     150.1(c)14]; exemptions <80 sq ft solar-available roof
                     area and <1.8 kWdc; 25% reduction with a qualifying
                     battery. Battery NOT mandatory, battery-READY is
                     (702.2.2 [150.0(s)]). Prescriptive space-conditioning
                     baseline is a heat pump. Duct leakage 5% requires field
                     verification.
  CEC ECC Program    from Jan 1 2026 the HERS Program no longer runs Energy
                     Code compliance — it is the Energy Code Compliance
                     Program and an ECC-Rater. CF1R Certificate of Compliance,
                     CF2R Certificate of Installation, CF3R Certificate of
                     Verification. Owner may sign the CF1R on a <=2-story
                     wood-framed dwelling; the CF3R may NOT be self-performed.
  Zone 0             Board of Forestry ADOPTED the emergency regulations
                     19 Aug 2026; effective on filing, expected ~Sept 2026.
                     New buildings comply in full from the effective date;
                     new vs existing turns on permit application date.
  Part 7 CWUIC       R337 REPEALED and CBC Ch. 7A emptied; the WUI content is
                     Part 7, Chapter 5.
  CGP                1 acre, or less if part of a larger common plan totalling
                     an acre; enrol via SMARTS for a WDID before disturbance.

Still deliberately unprinted: the California climate-zone count, any fee
figure, and any local threshold — all replaced with a "confirm it and write it
here" instruction.
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

FORM_ID = "CA.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Application"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Everything a California owner-builder gathers, verifies, and files — with "
    "the state-level gates that stop an application cold, and the two code "
    "renumberings that make older checklists point at the wrong sections.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- gates
flow += k.h2_tight("THE GATES SET BY STATE LAW")
flow.append(k.body(
    "Most of what your city or county asks for is local. These are not — they "
    "are conditions state law places on the issuing of your permit, and no "
    "jurisdiction can waive them. Clear these before you worry about anything "
    "else."))

flow.append(k.bullet(
    "<b>1. The application itself is a statutory form.</b> Health &amp; Safety "
    "Code § 19825 requires every city and county to use a permit application "
    "\"<i>in substantially the same form</i>\" it sets out — including the "
    "Owner-Builder Declaration you sign under penalty of perjury. You must "
    "also present identification sufficient to identify the property owner "
    "and, if asked, verify the signature. (§ 19825(a); see CA.1)"))
flow.append(k.bullet(
    "<b>2. The Notice to Property Owner.</b> A <i>second</i> signed document, "
    "on your building department's own letterhead: twelve statements you read "
    "and initial one at a time, then sign and return. \"<i>A permit shall not "
    "be issued unless the property owner complies with this section.</i>\" Ask "
    "for it before the day you apply. (H&amp;S § 19825(c); see CA.1)"))
flow.append(k.bullet(
    "<b>3. The workers' compensation declaration.</b> Signed under penalty of "
    "perjury as part of the same application: you self-insure, you carry a "
    "policy, or you certify you will not employ anyone in a way that makes "
    "you subject to the comp laws. (Labor Code § 3800(a); H&amp;S § 19825)"))
flow.append(k.bullet(
    "<b>4. School district fee certification.</b> A city or county "
    "\"<i>shall not issue a building permit for any construction absent "
    "certification by the appropriate school district</i>\" that its fee has "
    "been paid, or that it does not apply. Some districts instead defer this "
    "to the end, in which case no final inspection or certificate of "
    "occupancy may issue without it. (Education Code § 17620(b), (c))"))
flow.append(k.bullet(
    "<b>5. Your code edition locks on the day you submit.</b> \"<i>Only those "
    "building standards … effective at the local level at the time an "
    "application for a building permit is submitted</i>\" apply to your "
    "project. (H&amp;S § 18938.5(a); California Residential Code § 1.1.9)"))

flow.append(Spacer(1, 6))
flow.append(k.callout_long("The school fee gate surprises almost everyone", [
    Paragraph("It is a hard statutory gate on a <b>new residential "
              "structure</b>, it is assessed on assessable square footage, and "
              "the certificate comes from the <b>school district</b> — not "
              "from the building department, which merely refuses to proceed "
              "without it. Fee levels are set under Government Code § 65995 "
              "and adjusted periodically by the State Allocation Board, so "
              "this kit prints no rate: <b>ask your district for its current "
              "per-square-foot figure in writing</b>, and start that "
              "conversation early — districts are not open the same hours as "
              "your building counter.", S["body"]),
]))

# ---------------------------------------------------------------- A
flow += k.h2_tight("A. SITE AND PROJECT VERIFICATION")
flow += k.check_table("A1: Before anything else", [
    "Confirmed which jurisdiction issues your permit — city if the parcel is "
    "inside city limits, county if unincorporated (see CA.4)",
    ("Assessor's Parcel Number and situs address confirmed",
     [("APN:", 0.5), ("Address:", 0.5)]),
    "Title recorded in your name — you must own the property to claim § 7044",
    "Zoning district and permitted use verified with planning",
    ("Required setbacks confirmed in writing",
     [("Front:", 0.25), ("Side:", 0.25), ("Rear:", 0.25), ("Other:", 0.25)]),
    ("<b>Fire Hazard Severity Zone</b> for the parcel looked up, and whether "
     "it is State Responsibility Area or Local Responsibility Area",
     [("Zone:", 0.5), ("SRA / LRA:", 0.5)]),
    "Easements and recorded restrictions identified; flood zone and Coastal "
    "Zone status checked — a Coastal Development Permit is a separate approval "
    "on its own timeline. HOA or covenant approval obtained if applicable: "
    "private, not governmental, and nobody at the county will check it",
], notes_header="Notes / who confirmed")

# ---------------------------------------------------------------- B
flow += k.h2_tight("B. THE APPLICATION PACKAGE")
flow += k.check_table("B1: Forms and declarations", [
    "Building permit application on your jurisdiction's version of the "
    "§ 19825 form, completed and signed",
    "Owner-Builder Declaration completed — and you have identified which "
    "§ 7044 branch you are claiming (see CA.1)",
    ("<b>Notice to Property Owner</b> obtained, all twelve items initialed, "
     "signed and returned — the permit cannot issue without it",
     [("Requested:", 0.5), ("Returned:", 0.5)]),
    "Photo identification and proof of ownership ready to present",
    "Workers' compensation declaration completed — the correct one of the "
    "three options, truthfully",
    ("Construction lending agency named, or noted as none (Civil Code "
     "§ 8172). If anyone other than you will sign, the Authorization of Agent "
     "is completed and returned <b>before</b> issuance (§ 19825(b))",
     [("Lender / none:", 0.6), ("Agent returned:", 0.4)]),
    ("School district fee certification obtained — or confirmed the district "
     "defers it to final", [("District:", 0.6), ("Date:", 0.4)]),
    ("Estimated construction valuation stated — this usually sets your fee",
     [("Stated valuation: $", 1.0)]),
], notes_header="Notes")

flow += k.check_table("B2: Plans and supporting drawings", [
    "Complete plan set in the number and format your jurisdiction requires — "
    "most California jurisdictions now take digital submittal",
    "Site plan: property lines, setbacks, building footprint, driveway, "
    "septic and well locations if applicable, easements, and slope",
    "Foundation plan, floor plans, elevations, wall sections, framing plan",
    "Structural calculations and engineer's stamp where required — most of "
    "California sits in high seismic design categories, and hillside sites, "
    "retaining walls and long spans commonly trigger engineering. Include "
    "manufacturer specifications for trusses, ICF, SIPs or anything "
    "non-standard",
    ("Title 24 energy compliance documentation (see section F)",
     [("Path used:", 0.5), ("Prepared by:", 0.5)]),
    "Fire sprinkler system design — required in every new dwelling (see D) — "
    "and electrical, plumbing and mechanical layouts as your jurisdiction "
    "requires",
], notes_header="Notes")

# ---------------------------------------------------------------- C
flow += k.h2_tight("C. CODE EDITIONS — AND THE TWO RENUMBERINGS")
flow.append(k.body(
    "The <b>2025 California Building Standards Code (Title 24)</b> is the "
    "edition in force; it took effect <b>January 1, 2026</b>. Because "
    "H&amp;S § 18938.5 locks your edition at the date you <i>submit</i>, a "
    "project that submitted before that date may still be running on the 2022 "
    "code — which is exactly why you should write your submittal date down "
    "and know which book you are being reviewed against."))

flow.append(k.callout_long(
    "Buy the 2023 NEC — not the newest one on the shelf", [
        Paragraph("California's electrical code always trails the national "
                  "one. The cleanest proof is the Residential Code's own "
                  "referenced-standards table: the <b>2025</b> California "
                  "Residential Code lists \"<b>70—23: National Electrical "
                  "Code</b>,\" while the <b>2022</b> edition listed "
                  "\"<b>70—20</b>.\" So the current California Electrical Code "
                  "is built on the <b>2023 NEC</b>, and the California "
                  "amendments sit on top of it.", S["body"]),
        Paragraph("Buy the 2023 NEC, and say \"2023\" at the counter. A newer "
                  "NEC on your bench will disagree with your inspector on real "
                  "requirements, and the disagreements are in exactly the "
                  "places that get red-tagged.", S["body"]),
    ]))

flow.append(k.callout_long(
    "Two section numbers moved on January 1, 2026", [
        Paragraph("<b>Fire sprinklers were R313. They are now R309.</b> The "
                  "2025 edition reorganized Chapter 3 of the Residential Code. "
                  "The one- and two-family sprinkler requirement that sat at "
                  "R313.2 is now at <b>R309.2</b> — and R313 in the 2025 code "
                  "is \"Ceiling Height.\" Every article, checklist and county "
                  "handout still citing \"CRC R313\" for sprinklers is "
                  "pointing at the wrong section.", S["body"]),
        Paragraph("<b>Wildfire construction left the Residential Code "
                  "entirely.</b> Section R337 is now only a signpost: "
                  "\"<i>Provisions for materials and construction methods for "
                  "exterior wildfire exposure are now located in Part 7, "
                  "California Wildland-Urban Interface Code.</i>\" California "
                  "created a <b>new Part 7 of Title 24</b> for this in the "
                  "2025 edition and repealed R337 outright; CBC Chapter 7A is "
                  "an empty pointer too. The content you actually build to is "
                  "<b>Part 7, Chapter 5</b>. Guides that send you to "
                  "\"Chapter 7A\" or \"R337\" are describing the old "
                  "arrangement.", S["body"]),
    ]))
flow.append(k.cite(
    "Model-code editions read from the referenced-standards chapter of the "
    "2025 and 2022 California Residential Codes (NFPA 70—23 and 70—20 "
    "respectively; NFPA 13D—25 and 13D—22). Sprinkler renumbering corroborated "
    "by the same tables, which point NFPA 13D at R309.1.1/R309.2.1 in the 2025 "
    "edition and at R313.1.1/R313.2.1 in the 2022. WUI relocation quoted from "
    "the 2025 CRC § R337 user note. Effective date of the 2025 edition: "
    "January 1, 2026. Verified August 2026 — confirm the edition your "
    "jurisdiction is enforcing before you submit."))

flow.append(k.body(
    "<b>Local amendments are real, and they are limited.</b> A city or county "
    "may adopt changes to Title 24, but only ones that are <b>more "
    "restrictive</b>, and only with \"<i>express findings for each amendment, "
    "addition or deletion based upon climatic, topographical or geological "
    "conditions</i>,\" which must be <b>filed with the California Building "
    "Standards Commission</b> (fire-district findings go to HCD). An "
    "amendment's effective date is <b>the date it was filed</b>. If you are "
    "told something is required and you cannot find it in Title 24, ask "
    "whether it is a filed local amendment, an adopted ordinance, or a "
    "preference. <b>You can check this yourself:</b> the Building Standards "
    "Commission publishes a searchable database of the amendments filed with "
    "it, one per code cycle, at <b>dgs.ca.gov/BSC/Codes</b> — look for the "
    "ordinances list for the current cycle and search your city or county by "
    "name."))
flow.append(k.cite(
    "California Residential Code § 1.1.8, § 1.1.8.1, § 1.1.9; Health &amp; "
    "Safety Code § 17958, § 17958.5, § 17958.7, § 18941.5, and § 13869.7 for "
    "fire protection districts."))

# ---------------------------------------------------------------- D
flow += k.h2_tight("D. FIRE SPRINKLERS — YES, YOURS TOO")
flow.append(k.callout_long(
    "Every new California home needs an automatic sprinkler system", [
        Paragraph("2025 California Residential Code <b>§ R309.2</b>: "
                  "\"<i>An automatic sprinkler system shall be installed in "
                  "one- and two-family dwellings.</i>\"", S["body"]),
        Paragraph("There is <b>no exception for new construction</b> and "
                  "<b>no fire-zone trigger</b>. The only exceptions are "
                  "additions or alterations to existing buildings that are not "
                  "already sprinklered, and a detached accessory dwelling unit "
                  "of 1,200 square feet or less on a lot whose existing "
                  "primary residence has no sprinklers. Guides that list "
                  "sprinklers as \"often required in wildfire zones\" have "
                  "this badly wrong — it is a statewide requirement on every "
                  "new dwelling.", S["body"]),
        Paragraph("Design and installation follow <b>NFPA 13D</b> or § R309.3. "
                  "Budget for it at design stage, not after plan check: it "
                  "affects your water service size, your pressure, and — on a "
                  "well — your tank and pump. And note B&amp;P § 7057(c): even "
                  "a licensed general contractor may not contract for a fire "
                  "protection system without the right classification, so this "
                  "comes from a sprinkler specialist.", S["body"]),
    ]))
flow.append(d.FillInRow([("Sprinkler contractor:", 0.42),
                         ("License #:", 0.29), ("Water flow / pressure:", 0.29)]))

# ---------------------------------------------------------------- E
flow += k.h2_tight("E. WILDFIRE — ZONE, CONSTRUCTION, AND DEFENSIBLE SPACE")
flow.append(k.body(
    "Three separate things, often confused. <b>Your zone</b> is a mapped "
    "designation. <b>How you must build</b> is now Title 24 Part 7, the "
    "California Wildland-Urban Interface Code. <b>Defensible space</b> is a "
    "vegetation duty on the land, imposed by two parallel statutes depending "
    "on who is responsible for fire protection where you are."))

flow.append(k.body(
    "<b>Defensible space is the same duty under two different statutes.</b> In "
    "the <b>State Responsibility Area</b> it is Public Resources Code § 4291; "
    "in a <b>Very High Fire Hazard Severity Zone designated by a local "
    "agency</b> it is Government Code § 51182. Both require you to "
    "\"<i>maintain defensible space of 100 feet from each side and from the "
    "front and rear of the structure, but not beyond the property line</i>,\" "
    "with more intense fuel reduction between five and thirty feet. Which one "
    "reaches you follows from your zone — which is why the zone lookup is the "
    "first line of the checklist below."))
flow.append(k.callout_long(
    "The certification your insurer will ask for — and almost nobody knows about", [
        Paragraph("Both statutes carry the same requirement, and it lands "
                  "squarely on an owner-builder. <b>Before</b> constructing a "
                  "new building in the zone, \"<i>the owner shall obtain a "
                  "certification from the local building official that the "
                  "dwelling or structure, as proposed to be built, complies "
                  "with all applicable state and local building standards</i>,\" "
                  "and provide a copy on request to the insurer providing "
                  "<b>course of construction</b> cover. On completion, the "
                  "owner \"<i>shall obtain from the local building official a "
                  "copy of the final inspection report</i>\" demonstrating "
                  "compliance, and provide it on request to the property "
                  "insurer.", S["body"]),
        Paragraph("Ask for both documents by name, at the counter, as part of "
                  "your permit conversation. California wildfire insurance is "
                  "hard enough to obtain without discovering at the end that "
                  "you never collected the paperwork that proves how you "
                  "built.", S["body"]),
    ]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>The ember-resistant zone — \"Zone 0\" — needs checking rather than "
    "assuming.</b> Both statutes now describe an ember-resistant zone within "
    "<b>five feet</b> of the structure, and more intense fuel reduction "
    "between five and thirty feet. PRC § 4291(g)(1) provides that the "
    "ember-resistant zone requirement \"<i>shall not take effect for new "
    "structures until the board updates the regulations … and the guidance "
    "document</i>,\" with existing structures following three years later. "
    "<b>That rulemaking is now all but done.</b> The Board of Forestry and "
    "Fire Protection <b>adopted</b> the Zone 0 emergency regulations on "
    "<b>19 August 2026</b>, and expects them to take effect on filing — "
    "around September 2026. Under the adopted text, <b>new</b> buildings must "
    "comply in full <b>from the effective date</b>, and whether you count as "
    "new turns on whether your permit application went in before or after it. "
    "Existing structures are staged over three to five years."))
flow.append(k.callout_long("Zone 0 — check the date before you design the first five feet", [
    Paragraph("Zone 0 is \"<i>the area within five (5) feet around each "
              "Building or Structure</i>\" in which \"<i>no Combustible "
              "materials are permitted</i>,\" subject to enumerated "
              "exceptions, and it reaches the State Responsibility Area and "
              "locally designated Very High zones. Because the effective date "
              "was days away when this kit was verified, <b>confirm the "
              "current status with the Board of Forestry before you finalize "
              "your site plan</b> and write the answer in the box below. If "
              "you will permit after it lands, design to it now — no "
              "combustible fencing, gates, mulch, planting or stored material "
              "against the walls. Designing to it early is cheap; retrofitting "
              "a completed house is not.", S["body"]),
]))

flow += k.check_table("E1: Wildfire", [
    ("Fire Hazard Severity Zone confirmed from the official map — not from a "
     "real-estate listing", [("Zone:", 0.5), ("Checked:", 0.5)]),
    "If in a WUI area: design reviewed against <b>Title 24 Part 7</b> — roof, "
    "eaves, vents, siding, glazing, decking — with listed WUI-compliant "
    "products specified and their listings kept with the submittal",
    ("Pre-construction certification requested from the building official, and "
     "your course-of-construction insurer told what you are building",
     [("Requested:", 0.5), ("Insurer:", 0.5)]),
    ("Current Zone 0 / ember-resistant zone status confirmed with the Board "
     "of Forestry", [("Status:", 0.6), ("Checked:", 0.4)]),
    "Fire department access reviewed — road width, grade, turnarounds, and "
    "water supply for firefighting",
    "Final inspection report obtained at completion and filed with your "
    "insurance papers",
], notes_header="Notes")
flow.append(k.cite(
    "PRC § 4291 and Gov. Code § 51182, both as amended by Stats. 2025, "
    "Ch. 731 (AB 1455), effective October 13, 2025; building standards "
    "referenced at Gov. Code § 51189(b). WUI construction provisions: 2025 "
    "California Residential Code § R337 user note, directing to Title 24 "
    "Part 7. Verified August 2026."))

# ---------------------------------------------------------------- F
flow += k.h2_tight("F. TITLE 24 ENERGY COMPLIANCE")
flow.append(k.body(
    "The <b>2025 California Energy Code (Title 24, Part 6)</b> took effect "
    "<b>January 1, 2026</b>. It is the part of California's code most "
    "owner-builders hire out, and sensibly so: compliance is demonstrated "
    "either prescriptively or by whole-building modeling in Energy "
    "Commission-approved software, and the documentation set is unforgiving."))
flow.append(k.callout_long("Solar is required. Batteries are not — yet.", [
    Paragraph("<b>§ 702.3.1</b> (numbered <b>§ 150.1(c)14</b> before the 2025 "
              "restructure renumbered the Standards): \"<i>All single-family "
              "residential buildings shall have a newly installed photovoltaic "
              "(PV) system or newly installed PV modules meeting the minimum "
              "qualification requirements specified in Joint Appendix "
              "JA11.</i>\" Size comes from an equation driven by conditioned "
              "floor area and dwelling units, not by a rule of thumb.",
              S["body"]),
    Paragraph("The exemptions are narrow and numeric: no PV is required if the "
              "solar-available roof area is <b>less than 80 contiguous square "
              "feet</b>, or if the calculated system comes out <b>below 1.8 "
              "kWdc</b>; there are further exceptions for roofs that cannot "
              "carry the snow load and for projects with planning approval "
              "before 2020. If you install a qualifying battery, the PV may be "
              "<b>reduced by 25%</b>.", S["body"]),
    Paragraph("<b>Battery storage is not mandatory</b> for a single-family "
              "home — but <b>battery-ready is</b>. Where the electrical "
              "service exceeds 125A the Energy Code requires a 225A busbar, "
              "four identified backup branch circuits, and reserved space and "
              "raceway for a future transfer switch, alongside solar-ready and "
              "heat-pump-ready provisions. The prescriptive space-conditioning "
              "baseline is a <b>heat pump</b>; a gas furnace is still "
              "reachable, but only through the performance path.", S["body"]),
]))
flow.append(Spacer(1, 6))

flow.append(k.callout_long(
    "\"HERS rater\" is the wrong name now — ask for an ECC-Rater", [
        Paragraph("As of <b>January 1, 2026</b> the Home Energy Rating System "
                  "program no longer runs Energy Code compliance. Field "
                  "verification and diagnostic testing moved to the Energy "
                  "Commission's <b>Energy Code Compliance (ECC) Program</b>, "
                  "and the person who does your verification is an "
                  "<b>ECC-Rater</b> working under an ECC-Provider. Every guide "
                  "written before 2026 — and most written since — still says "
                  "\"hire a HERS rater.\"", S["body"]),
        Paragraph("What you can and cannot sign: on a wood-framed dwelling of "
                  "two stories or fewer that needs no licensed design "
                  "professional, <b>you may sign the CF1R yourself</b> in the "
                  "Responsible Building Designer block, and your installers "
                  "sign the CF2Rs. The <b>CF3R cannot be self-performed</b> — "
                  "the ECC-Rater is an independent third party to the "
                  "installing contractor and may not certify a CF1R as the "
                  "responsible person.", S["body"]),
        Paragraph("Assume you will need one: <b>duct leakage testing</b> is "
                  "mandatory on essentially every new home with ducts, at 5% "
                  "of air handler airflow, \"<i>as confirmed through field "
                  "verification and diagnostic testing</i>.\" Raters are "
                  "scheduled, and a finished but unverified house cannot pass "
                  "its final. Identify yours at design stage.", S["body"]),
    ]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "The three compliance documents are the <b>CF1R Certificate of "
    "Compliance</b> (design, submitted with your application), the <b>CF2R "
    "Certificate of Installation</b> (signed by whoever installed the "
    "measure), and the <b>CF3R Certificate of Verification</b> (the "
    "ECC-Rater's field verification). Fill in the rest below with your energy "
    "consultant."))

flow += k.check_table("F1: Get these in writing", [
    ("Which <b>climate zone</b> is the parcel in, and which <b>compliance "
     "path</b> are you using?", [("Zone:", 0.4), ("Path:", 0.6)]),
    ("<b>PV system size</b> calculated — or the specific exemption you are "
     "relying on, confirmed in writing before design",
     [("kWdc:", 0.4), ("Exemption:", 0.6)]),
    ("<b>ECC-Rater</b> identified and booked, and the list of measures "
     "requiring CF3R verification agreed",
     [("Rater:", 0.55), ("Provider:", 0.45)]),
    ("Which <b>CF1R / CF2R / CF3R</b> documents your department wants, and at "
     "which stage", [("Answer:", 1.0)]),
], notes_header="Answer / who confirmed")

# ---------------------------------------------------------------- G
flow += k.h2_tight("G. SEPTIC, WELL, AND WATER")
flow.append(k.body(
    "On a rural parcel these are the long poles, and both run on a different "
    "track from your building permit. Start them <b>before</b> you design the "
    "house — ideally before you buy the land, if you still can."))

flow.append(k.body(
    "<b>Septic.</b> California regulates on-site wastewater through the State "
    "Water Resources Control Board's <b>OWTS Policy</b> — formally the Water "
    "Quality Control Policy for Siting, Design, Operation and Maintenance of "
    "Onsite Wastewater Treatment Systems — adopted <b>April 18, 2023</b> and "
    "approved by the Office of Administrative Law on <b>September 26, 2023</b>. "
    "In practice you will not deal with the State Board. Most counties "
    "implement the Policy through a <b>Local Agency Management Program "
    "(LAMP)</b> approved by their Regional Water Quality Control Board, and "
    "your septic permit comes from the <b>county environmental health "
    "department</b> under that LAMP. Where no LAMP applies, the Policy's own "
    "standards and the Regional Board govern. Your first question is simply: "
    "<i>does my county have an approved LAMP, and who issues my permit?</i>"))

flow.append(k.callout_long("You may wire your own house. You may not drill your own well.", [
    Paragraph("Water Code § 13750.5: \"<i>No person shall undertake to dig, "
              "bore, or drill a water well … to deepen or reperforate such a "
              "well, or to abandon or destroy such a well, unless the person "
              "responsible for that construction … possesses a <b>C-57 Water "
              "Well Contractor's License</b>.</i>\"", S["body"]),
    Paragraph("There is <b>no owner exception</b> — unlike the electrical and "
              "plumbing work § 7044 lets you self-perform. And B&amp;P "
              "§ 7057(c) stops even a licensed general building contractor "
              "from taking the work without the C-57 classification. Hire a "
              "C-57, and verify the license.", S["body"]),
]))

flow += k.check_table("G1: Septic and well", [
    ("Confirmed whether your county has an approved LAMP and which office "
     "issues the septic permit", [("Office:", 0.6), ("LAMP?", 0.4)]),
    "Site and soil evaluation applied for — percolation or soil profile as "
    "your county requires. This is the test that decides what system your "
    "land can carry, and what it will cost",
    ("Septic permit application filed", [("Permit #:", 0.55), ("Date:", 0.45)]),
    "System type and disposal field location shown on the site plan, "
    "consistent with the house footprint, the well, and your setbacks",
    ("Well permit obtained from the permitting agency <b>before</b> drilling",
     [("Permit #:", 0.55), ("Date:", 0.45)]),
    ("C-57 licensed well contractor engaged and license verified",
     [("Contractor:", 0.6), ("License #:", 0.4)]),
    ("Well completion report filed by the driller, and water quality tested "
     "— a lender or a buyer will ask one day",
     [("Tested:", 0.5), ("Result:", 0.5)]),
    "If on public water and sewer instead: will-serve letters or connection "
    "commitments obtained, and connection fees budgeted — this replaces the "
    "septic and well track entirely",
], notes_header="Notes")
flow.append(k.cite(
    "State Water Resources Control Board OWTS Policy, adopted April 18, 2023, "
    "OAL-approved September 26, 2023 (waterboards.ca.gov → Water Issues → "
    "Programs → OWTS), which also publishes a LAMP contact list and a map tool "
    "for the Policy's impaired-area attachment. Well drilling license: Water "
    "Code § 13750.5. This kit prints no percolation-test or permit-fee figures "
    "because both are set locally. Verified August 2026."))

# ---------------------------------------------------------------- H
flow += k.h2_tight("H. GRADING, STORMWATER, AND ACCESS")
flow += k.check_table("H1: Site work approvals", [
    ("Grading permit requirement confirmed with your building or public works "
     "department, and a geotechnical or soils report obtained if the site is "
     "sloped or filled", [("Required?", 0.4), ("Trigger:", 0.6)]),
    ("Total land disturbance calculated — house, driveway, septic area, "
     "staging and spoil", [("Total acres disturbed:", 1.0)]),
    ("<b>One acre or more</b> disturbed — or less, if your work is part of a "
     "larger common plan of development totalling an acre — brings you under "
     "the statewide <b>Construction General Permit</b>. Enroll through the "
     "State Water Board's SMARTS system and get your WDID <b>before</b> ground "
     "disturbance", [("Covered?", 0.4), ("WDID:", 0.6)]),
    ("Driveway or encroachment permit — confirm who maintains the road you "
     "connect to. A connection onto a state highway is a Caltrans "
     "encroachment permit. Erosion and sediment control measures shown on the "
     "plans", [("Road authority:", 0.6), ("Permit:", 0.4)]),
    ("Address assigned by the jurisdiction, and the fire authority satisfied "
     "with access and turnaround", [("Address:", 0.6), ("Fire OK:", 0.4)]),
    "If demolishing an existing structure: asbestos survey and notification to "
    "your local air district completed first. Tree protection and oak "
    "ordinance requirements checked — many California jurisdictions require a "
    "permit to remove protected trees",
], notes_header="Notes")


# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Application submitted:", 0.34),
                         ("Permit issued:", 0.33), ("Permit #:", 0.33)]))
flow.append(Spacer(1, 10))
flow.append(k.sources_table([
    ("The permit application, Owner-Builder Declaration and agent "
     "authorization are statutory and statewide; ID required",
     "H&amp;S § 19825(a), (b)"),
    ("A second signed document — the Notice to Property Owner and its twelve "
     "initialed acknowledgments — gates the permit", "H&amp;S § 19825(c)"),
    ("Workers' comp declaration under penalty of perjury at application",
     "Lab. § 3800(a)"),
    ("PV required on all single-family; exemptions under 80 sq ft of "
     "solar-available roof or under 1.8 kWdc; battery-ready, not battery, is "
     "mandatory", "2025 Energy Code § 702.3.1, § 702.2.2"),
    ("Energy Code compliance verification moved from the HERS Program to the "
     "ECC Program on January 1, 2026", "California Energy Commission"),
    ("No building permit without school district fee certification — or, "
     "where the district elected otherwise, no final inspection or CO",
     "Ed. Code § 17620(b), (c)"),
    ("Code edition locks at submittal; permit valid on commencement within 12 "
     "months, with 180-day extensions",
     "H&amp;S § 18938.5(a), § 18938.6; CRC § 1.1.9"),
    ("Local amendments: more restrictive only, express findings, filed with "
     "the BSC, effective on the date filed", "CRC § 1.1.8, § 1.1.8.1"),
    ("The current California Electrical Code is built on the 2023 NEC; the "
     "2022 edition on the 2020 NEC", "2025 / 2022 CRC Ch. 44 — NFPA 70—23, —20"),
    ("Automatic sprinklers in all one- and two-family dwellings (was R313.2 "
     "before the 2025 renumbering); WUI construction moved to Title 24 Part 7",
     "2025 CRC § R309.2; § R337 note"),
    ("100 feet of defensible space in the SRA and in a locally designated Very "
     "High FHSZ; pre-construction certification and final report for your "
     "insurer; ember-resistant zone deferred for new structures",
     "PRC § 4291; Gov. § 51182"),
    ("C-57 license required to drill a water well — no owner exception; OWTS "
     "Policy implemented locally through LAMPs",
     "Water Code § 13750.5; SWRCB"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ca-permit-kit",
                       "CA.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
