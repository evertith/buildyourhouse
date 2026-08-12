#!/usr/bin/env python3
"""GA.2 Permit Application Checklist — Georgia Edition.

Sources verified August 2026 (see the on-page sources table):
  O.C.G.A. § 8-2-25(a),(b)  the eight mandatory state minimum codes apply
                            statewide with no local adoption; permissive
                            codes only where locally adopted
  O.C.G.A. § 8-2-26(a)(4)   permits and inspections are a local-option power
  O.C.G.A. § 8-2-26(g)      private professional providers (plan review /
                            inspection) — verified in substance
  DCA announcement + 2026 amendments packet: 2024 IRC/IBC/IPC/IMC/IFGC/ISPSC
    with 2026 Georgia Amendments and 2023 NEC effective January 1, 2026;
    IRC Parts IV (energy), VII (plumbing), VIII (electrical) deleted and
    replaced by the state IECC, IPC, and NEC
  O.C.G.A. § 8-2-4          no mandatory fire sprinklers in 1-2 family
                            dwellings (quoted in the DCA packet)
  Ga. Comp. R. & Regs. 110-11-1-.34  energy code = 2015 IECC with the Georgia
                            Supplements and Amendments (2020/2022/2023)
  GA IECC R402.4.1.2        blower door mandatory: < 5 ACH50, certified DET
                            verifier, signed written report to code official
  GA IECC R403.3.3/.3.4     duct test mandatory: total leakage <= 6 cfm25 per
                            100 sq ft; exception for ducts and air handlers
                            entirely inside the envelope
  DPH Rule 511-3-1-.03      septic: no physical development before the county
                            construction permit; 20-day decision clock;
                            12-month validity; site inspection first
  O.C.G.A. § 12-5-131.1(a)  owner may drill a well on own primary-residence
                            property; resale development requires a licensed
                            water well contractor
  O.C.G.A. § 12-7-7(a)      land-disturbance permit / NOI required
  O.C.G.A. § 12-7-17(4)     single-family exemption under one acre outside a
                            larger common plan
  EPD NPDES construction stormwater: GAR100001 / GAR100002 / GAR100003
  O.C.G.A. § 44-14-361.5    Notice of Commencement — 15 days, superior court
                            clerk, posted on site; contents; forfeiture
  GDOT Regulations for Driveway and Encroachment Control; O.C.G.A. § 32-6-131
  EPD Floodplain Management Unit — local NFIP ordinances govern per parcel

Still deliberately hedged: septic-permit-before-building-permit sequencing
(county ordinance/practice — the quotable state gate is on physical
development); the § 12-7-17(8) provisos near state waters and trout streams
(exact distances not verified — none printed); § 8-2-26(g) procedural terms;
the NPDES 14-day NOI clock and 2023-2028 permit term (read via EPD-hosted
documents — confirm against the GAR100001 PDF); which counties enforce
permits at all (no official roster — worksheet); O.C.G.A. mirror currency
(March 28, 2024).
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

FORM_ID = "GA.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Application"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Everything a Georgia owner-builder gathers, verifies, and files — with "
    "the state-level gates that stop a project cold whether or not your "
    "county runs a permit counter.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- the split
flow += k.h2_tight("THE GEORGIA SPLIT — MANDATORY CODES, LOCAL-OPTION PERMITS")
flow.append(k.body(
    "Eight state minimum codes bind your project no matter where in Georgia "
    "it sits: \"<i>the state minimum standard codes enumerated in "
    "subdivisions (9)(A)(i)(I) through (9)(A)(i)(VIII) and (9)(B)(i)(I) "
    "through (9)(B)(i)(VIII) of Code Section 8-2-20 shall have state-wide "
    "application and shall not require adoption by a municipality or "
    "county</i>\" (§ 8-2-25(a)). The eight are the building, electrical, "
    "fuel gas, mechanical, plumbing, residential, energy conservation, and "
    "fire codes."))
flow.append(k.body(
    "Enforcement is a different statute. Section 8-2-26(a) is a grant of "
    "power, not a command: \"<i>The governing body of any municipality or "
    "county adopting any state minimum standard code shall have the "
    "power</i>\" — and then, at (a)(4), \"<i>To require permits and to fix "
    "charges therefor.</i>\" Your county <b>may</b> run a permit office. "
    "Nothing makes it."))

flow.append(k.callout(
    "If your county has no building department", [
        Paragraph("Then there is no permit to pull — and nothing else "
                  "changes. Section 8-2-25(a) still binds the work to the "
                  "eight mandatory codes, and § 43-41-17(h) makes your own "
                  "exemption conditional on doing the work \"in conformity "
                  "with\" them. Enforcement is optional for the "
                  "<i>government</i>; the code is not optional for "
                  "<i>you</i>. No official roster of non-enforcing counties "
                  "exists — call the county and record its answer in GA.4, "
                  "and see GA.3 for how to verify your own work when nobody "
                  "else will.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "Two footnotes. The <b>permissive</b> codes — property maintenance, "
    "existing buildings, green building — apply only where locally "
    "adopted (§ 8-2-25(b)). And applicants may retain <b>private "
    "professional providers</b> for plan review and inspection "
    "(§ 8-2-26(g)) — useful where the queue is long; the kit does not "
    "print that subsection's procedural terms, so read it before "
    "invoking it."))
flow.append(k.cite(
    "O.C.G.A. § 8-2-25(a), (b); § 8-2-26(a)(4), (g); § 43-41-17(h). "
    "Verified August 2026."))

# ---------------------------------------------------------------- gates
flow += k.h2_tight("THE STATE-LEVEL GATES — CLEAR THESE FIRST")
flow.append(k.body(
    "Most of what a permit counter asks for is local. These are not — they "
    "are state rules that run on their own tracks, and three of them bite "
    "before any ground is broken:"))
flow.append(k.bullet(
    "<b>1. Septic.</b> On a lot that will use an on-site sewage system, "
    "<b>no physical development may begin</b> until the County Health "
    "Department issues the septic construction permit. (DPH Rule "
    "511-3-1-.03(2) — section C below)"))
flow.append(k.bullet(
    "<b>2. Land disturbance.</b> No land-disturbing activity without a "
    "permit from the local issuing authority or a notice of intent to EPD "
    "— unless your build fits the under-one-acre single-family exemption. "
    "(§ 12-7-7(a); § 12-7-17(4) — section D)"))
flow.append(k.bullet(
    "<b>3. State-route driveway.</b> Any construction work inside a state "
    "highway right of way needs a GDOT permit first, from the District "
    "Area Office. (GDOT driveway regulations; § 32-6-131 — section E)"))
flow.append(k.bullet(
    "<b>4. Notice of Commencement.</b> Filed within <b>15 days</b> of "
    "starting work, with the clerk of superior court, and posted on site "
    "— or you forfeit the lien-law screen. (§ 44-14-361.5 — section F)"))

# ---------------------------------------------------------------- A
flow += k.h2_tight("A. SITE AND PROJECT VERIFICATION")
flow += k.check_table("A1: Before anything else", [
    "Confirmed which jurisdiction (city or unincorporated county) your "
    "parcel is in — and whether it requires building permits at all "
    "(see GA.4)",
    ("Parcel identification number and 911 address confirmed",
     [("Parcel ID:", 0.55), ("Address:", 0.45)]),
    "Deed recorded in your name — you must own the land to claim the "
    "exemption",
    ("Zoning district, permitted use, and setbacks verified in writing "
     "with planning/zoning",
     [("Front:", 0.25), ("Side:", 0.25), ("Rear:", 0.25), ("Other:", 0.25)]),
    "Easements, rights-of-way, and recorded restrictions identified",
    ("Flood zone checked with your community's floodplain administrator "
     "and the state flood map viewer (georgiadfirm.com)",
     [("Zone:", 0.4), ("Confirmed with:", 0.6)]),
    "HOA or covenant approval obtained if applicable — private, not "
    "governmental; the county will not check it for you",
], notes_header="Notes / who confirmed")
flow.append(k.cite(
    "Floodplain construction rules are your community's NFIP ordinance — a "
    "local determination from the flood insurance rate map, coordinated at "
    "the state level by EPD's Floodplain Management Unit "
    "(epd.georgia.gov). This kit prints no elevation or permit rule "
    "because there is no statewide one. Verified August 2026."))

# ---------------------------------------------------------------- B
flow += k.h2_tight("B. THE APPLICATION PACKAGE")
flow += k.check_table("B1: Forms and proofs", [
    "Building permit application, completed and signed — the form is "
    "local; see GA.5 for how to find yours",
    ("County owner-builder affidavit, notarized, if your county requires "
     "one (no state form exists — GA.1)",
     [("Required? Y/N:", 0.4), ("Form:", 0.6)]),
    ("Septic construction permit issued (section C) — most counties want "
     "it attached to the building application",
     [("Permit #:", 0.55), ("Date:", 0.45)]),
    "Homeowner trade permits identified — where the county permits "
    "electrical, plumbing, and HVAC separately, you apply under the "
    "§ 43-14-13(d) carve-out; some use a homeowner disclaimer form",
    ("Estimated construction cost stated — this drives the $2,500 "
     "licensing test for your subs and usually the fee",
     [("Stated cost: $", 1.0)]),
    "Notice of Commencement drafted and ready to file within 15 days of "
    "starting work (section F)",
], notes_header="Notes")

flow += k.check_table("B2: Plans and supporting drawings", [
    "Plan sets in the count and format your jurisdiction takes (many "
    "metro counties are digital-only; ask before printing)",
    "Site plan showing property lines, setbacks, the building footprint, "
    "driveway, well and septic locations, and any easements",
    "Foundation plan, floor plans, elevations, wall sections, and a "
    "framing plan",
    "Electrical, plumbing and mechanical layouts as your county requires "
    "— reviewed against the state IPC, 2023 NEC, and IMC/IFGC, not the "
    "IRC chapters (section G)",
    ("Energy code compliance documentation and the two DET tests planned "
     "(section G)", [("DET verifier:", 1.0)]),
    "Engineered or manufacturer specifications for anything non-standard "
    "— trusses, ICF, SIPs, long spans, steep-slope foundations",
], notes_header="Notes")

# ---------------------------------------------------------------- C
flow += k.h2_tight("C. SEPTIC AND WELL — COUNTY HEALTH, NOT THE BUILDING OFFICE")
flow.append(k.body(
    "On-site sewage is permitted by your <b>County Health Department</b> "
    "under the state DPH rules, on its own track and its own timeline. In "
    "Georgia it is the hardest state gate on the whole project, because it "
    "bars the ground itself:"))

flow.append(k.callout(
    "No site work on a septic lot until the permit issues — statewide", [
        Paragraph("\"<i>No person may begin the physical development of a "
                  "lot or structure where an on-site sewage management "
                  "system will be utilized, nor install an on-site sewage "
                  "management system or component thereof, without having "
                  "first obtained from the County Health Department a "
                  "construction permit for the installation of an onsite "
                  "sewage management system.</i>\" (DPH Rule "
                  "511-3-1-.03(2))", S["body"]),
        Paragraph("Note what is gated: not just the septic install — "
                  "<b>the physical development of the lot</b>. Clearing "
                  "and grading a septic lot before this permit is a "
                  "violation. Start here, before you buy the land if you "
                  "still can.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "The mechanics: you apply \"in writing on forms provided by the "
    "County Board of Health\"; the county must \"<i>approve or disapprove "
    "such application within twenty days after the receipt of a completed "
    "application</i>\" (Rule -.03(2)(a)); the permit issues only after a "
    "site inspection \"<i>shows favorable findings relative to absorption "
    "rates, soil characteristics, groundwater, rock</i>\" and related "
    "factors (Rule -.03(3)); and it \"<i>shall remain valid for not more "
    "than twelve months from the date of issue</i>\" (Rule -.03(3)(a))."))
flow.append(k.body(
    "<b>Sequencing against the building permit.</b> The state rule bars "
    "physical development — it does not say which permit issues first. "
    "In practice, Georgia counties nearly universally require the septic "
    "permit <b>before</b> the building permit; expect to hand it in as "
    "an attachment, and confirm your county's order rather than "
    "assuming it."))

flow += k.check_table("C1: Septic and well", [
    "Septic application filed with the County Health Department on its "
    "forms — site inspection scheduled",
    ("Septic construction permit issued after favorable site findings — "
     "valid 12 months; no lot development before this",
     [("Permit #:", 0.55), ("Date:", 0.45)]),
    "System and drainfield location shown on your site plan and "
    "consistent with the house footprint and any well",
    "Final: system not backfilled or used until the county's final "
    "inspection and written approval (see GA.3)",
    ("If drilling a well: confirmed the property is your primary "
     "residence — the owner-drilling right does not cover land developed "
     "for resale", [("Driller/licensee:", 1.0)]),
    ("Well siting checked against the DPH septic-separation rules, and "
     "the county asked whether it approves individual wells",
     [("County answer:", 1.0)]),
], notes_header="Notes")

flow.append(k.body(
    "<b>Wells.</b> The Water Well Standards Act leaves the owner a lane: "
    "\"<i>Nothing in this part shall prohibit a person from drilling a "
    "well on his or her own property if such property is his or her "
    "primary residence.</i>\" Land \"developing for resale\" needs a "
    "licensed water well contractor (§ 12-5-131.1(a)). The kit found "
    "<b>no statewide domestic-well permit</b> — but some county health "
    "departments approve individual wells, and well-to-septic separation "
    "runs through the DPH on-site sewage rules. Confirm both locally "
    "before drilling."))
flow.append(k.cite(
    "DPH Rule 511-3-1-.03(2), (2)(a), (3), (3)(a) — official DPH rules "
    "PDF, read directly; O.C.G.A. § 12-5-131.1(a). "
    "Septic-before-building-permit sequencing is county practice, not a "
    "quotable state rule — the quotable gate is on physical development. "
    "Verified August 2026."))

# ---------------------------------------------------------------- D
flow += k.h2_tight("D. EROSION, SEDIMENTATION, AND STORMWATER")
flow.append(k.body(
    "\"<i>No land-disturbing activities shall be conducted in this state, "
    "except those land-disturbing activities provided for in Code Section "
    "12-7-17, without the operator first securing a permit from a local "
    "issuing authority or providing notice of intent to the division as "
    "required by this Code section.</i>\" (§ 12-7-7(a)) The exemption "
    "most owner-builders ride is § 12-7-17(4): \"<i>The construction of "
    "single-family residences, when such construction disturbs less than "
    "one acre and is not a part of a larger common plan of development or "
    "sale with a planned disturbance of equal to or greater than one "
    "acre.</i>\""))

flow.append(k.callout("Exempt from the permit is not exempt from the rules", [
    Paragraph("Even inside the single-family exemption, the § 12-7-6(b) "
              "minimum standards — including stream buffers — still apply "
              "to your work. And the exemption itself carries provisos for "
              "construction near state waters and trout streams that "
              "narrow it. This kit deliberately prints no buffer or "
              "proximity distances, because it could not verify the exact "
              "statutory text — read § 12-7-17 in full and ask your local "
              "issuing authority before you rely on the exemption near "
              "any stream or lake.", S["body"]),
]))

flow += k.check_table("D1: Erosion control and NPDES", [
    ("Total land disturbance calculated — house, driveway, septic area, "
     "staging and spoil piles", [("Total acres disturbed:", 1.0)]),
    "If under one acre and not part of a larger common plan: exemption "
    "applies — but § 12-7-6(b) minimum standards and buffers still bind, "
    "and any work near a stream, lake, or trout water gets flagged to "
    "the local issuing authority first",
    ("If not exempt: land disturbance permit obtained from the certified "
     "local issuing authority (or EPD district where none)",
     [("Authority:", 0.6), ("Permit #:", 0.4)]),
    ("If disturbing one acre or more: NPDES coverage under the right "
     "general permit (GAR100001 stand-alone); NOI filed with EPD and the "
     "waiting period confirmed against the current permit text",
     [("NOI filed:", 1.0)]),
], notes_header="Notes")
flow.append(k.cite(
    "O.C.G.A. § 12-7-7(a); § 12-7-17(4); § 12-7-6(b) obligation noted "
    "without printed distances. NPDES permit family and forms: EPD "
    "storm-water forms page (epd.georgia.gov). EPD-hosted documents state "
    "the 2023 permits run through July 2028 and authorize discharge 14 "
    "days after a complete NOI — this kit treats both as unconfirmed; "
    "read the current GAR100001 before you schedule around them. "
    "Verified August 2026."))

# ---------------------------------------------------------------- E
flow += k.h2_tight("E. DRIVEWAY — GDOT IF YOU TOUCH A STATE ROUTE")
flow.append(k.body(
    "If your driveway connects to a <b>state route</b>, GDOT's driveway "
    "and encroachment regulations control: \"<i>A permit is required "
    "prior to performing any construction work or non-routine maintenance "
    "within</i>\" the state highway right of way, and \"<i>Application "
    "for residential driveways and temporary use driveways are made at "
    "the District Area Office.</i>\" The statute behind it (§ 32-6-131) "
    "bars unpermitted <b>commercial</b> driveways — and the regulations "
    "classify any driveway serving more than four dwelling units as "
    "commercial. A county or city road instead? The county or city sets "
    "the rules — ask public works."))

flow += k.check_table("E1: Driveway access", [
    "Determined whether the road you connect to is a state route, a "
    "county road, or a city street — this decides who you talk to",
    ("If a state route: residential driveway application obtained from "
     "and filed with the GDOT District Area Office — original forms "
     "only", [("District/Area office:", 0.6), ("Filed:", 0.4)]),
    "Permit in hand before any work in the right of way — including "
    "culvert, apron, or grading at the road",
    "If county or city road: their driveway/culvert requirements "
    "confirmed and any permit obtained",
], notes_header="Notes")
flow.append(k.cite(
    "GDOT Regulations for Driveway and Encroachment Control (read "
    "directly, dot.ga.gov); O.C.G.A. § 32-6-131. Verified August 2026."))

# ---------------------------------------------------------------- F
flow += k.h2_tight("F. NOTICE OF COMMENCEMENT — 15 DAYS, OR YOU LOSE THE SCREEN")
flow.append(k.body(
    "Georgia's lien law gives an owner one cheap, powerful filing: "
    "\"<i>Not later than 15 days after the contractor physically "
    "commences work on the property, a notice of commencement shall be "
    "filed by the owner, the agent of the owner, or by the contractor "
    "with the clerk of the superior court in the county in which the "
    "project is located. A copy of the notice of commencement shall be "
    "posted on the project site.</i>\" (§ 44-14-361.5(b)) Filing it "
    "activates the Notice-to-Contractor screen that cuts off hidden "
    "remote lien claimants — the suppliers and sub-subs you never met. "
    "Not filing forfeits exactly that (§ 44-14-361.5(d))."))

flow += k.check_table("F1: Notice of Commencement", [
    "Drafted with the statutory contents: contractor's name, address, "
    "and phone; project name, location, and legal description; owner's "
    "name and address; the person at whose instance improvements are "
    "made, if not the owner; surety, if bonded; construction lender, "
    "if any",
    ("Filed with the clerk of superior court in the project county "
     "within 15 days of physically commencing work",
     [("Filed:", 0.5), ("Book/page:", 0.5)]),
    "Copy posted on the project site and kept posted; stamped copy in "
    "this binder",
], notes_header="Notes")
flow.append(k.cite(
    "O.C.G.A. § 44-14-361.5(b), (d); statutory contents list per "
    "subsection (b). No state form exists — some clerks publish fill-in "
    "templates; draft to the contents list either way. Verified August "
    "2026."))

# ---------------------------------------------------------------- G
flow += k.h2_tight("G. CODE EDITIONS AND THE TWO MANDATORY ENERGY TESTS")
flow.append(k.body(
    "<b>Effective January 1, 2026</b>, Georgia's DCA adopted new "
    "mandatory state codes: the <b>2024</b> IRC, IBC, IPC, IMC, IFGC, and "
    "ISPSC, each with 2026 Georgia Amendments, plus the <b>2023 NEC</b> "
    "(and a 2024 IFC through the Safety Fire Commissioner). The "
    "amendments packet itself: \"<i>The INTERNATIONAL RESIDENTIAL CODE "
    "FOR ONE- AND TWO-FAMILY DWELLINGS, 2024 Edition … shall constitute "
    "the official Georgia State Minimum Standard One- and Two-Family "
    "Dwelling Code.</i>\""))

flow.append(k.callout(
    "Georgia guts three parts of the IRC — buy the right books", [
        Paragraph("The 2026 Georgia Amendments delete the IRC's energy "
                  "part (\"<i>Part IV, Energy Conservation (Chapter 11), "
                  "is deleted</i>\"), its plumbing part (\"<i>Part VII, "
                  "Plumbing (Chapters 25 through 33), is deleted</i>\"), "
                  "and its electrical part (\"<i>Part VIII, Electrical "
                  "(Chapters 34 through 43), is deleted from the "
                  "INTERNATIONAL RESIDENTIAL CODE</i>\"). Your plumbing "
                  "is inspected to the state IPC, your wiring to the "
                  "2023 NEC, and your energy work to the Georgia Energy "
                  "Code — not to IRC chapters. An IRC-only bookshelf "
                  "will not cover your house.", S["body"]),
        Paragraph("One relief: by statute, no state or post-2010 local "
                  "code \"<i>shall include a requirement that fire "
                  "sprinklers be installed in a single-family dwelling or "
                  "a residential building that contains no more than two "
                  "dwelling units</i>\" (§ 8-2-4, quoted in the DCA "
                  "packet).", S["body"]),
]))
flow.append(k.cite(
    "DCA, \"New Mandatory State Codes\" announcement and "
    "current-state-minimum-codes page (dca.georgia.gov); 2026 Georgia "
    "Amendments packet (\"Revised January 1, 2026\"), read directly. "
    "Verified August 2026 — if you file before a county has caught up, "
    "confirm which edition its reviewers are working from."))

flow.append(k.body(
    "<b>The energy code did not move.</b> It remains the <b>2015 IECC</b> "
    "with the Georgia Supplements and Amendments (2020, 2022, "
    "2022-additional, and 2023) — untouched by the 2026 cycle: \"<i>The "
    "INTERNATIONAL ENERGY CONSERVATION CODE, 2015 Edition … shall "
    "constitute the official Georgia State Minimum Standard Energy "
    "Code.</i>\" (Ga. Comp. R. &amp; Regs. 110-11-1-.34) Buy the 2015 "
    "book and the Georgia amendment packets, not a newer IECC."))

flow.append(k.callout(
    "Two tests are mandatory — there is no visual-inspection option", [
        Paragraph("<b>Blower door.</b> \"<i>All one and two-family "
                  "dwelling units shall be tested and verified to less "
                  "than five air changes per hour at 50 Pascals (ACH50) "
                  "for Climate Zones 2, 3, and 4. … A written report of "
                  "the results of the test shall be signed by the party "
                  "conducting the test and provided to the code official. "
                  "… Testing shall be conducted by a certified duct and "
                  "envelope tightness (DET) verifier.</i>\" (GA amended "
                  "IECC § R402.4.1.2) Unlike some states, Georgia offers "
                  "no visual-inspection alternative — plan and budget for "
                  "the test.", S["body"]),
        Paragraph("<b>Duct leakage.</b> \"<i>Ducts shall be pressure "
                  "tested to determine air leakage</i>\" (§ R403.3.3, "
                  "Mandatory), at rough-in or post-construction, and "
                  "\"<i>the total leakage shall be less than or equal to "
                  "6 cubic feet per minute … per 100 square feet … of "
                  "conditioned floor area</i>\" (§ R403.3.4). One "
                  "exception: \"<i>A duct air leakage test shall not be "
                  "required where the ducts and air handlers are located "
                  "entirely within the building thermal envelope.</i>\" "
                  "Designing the ducts inside the envelope saves you the "
                  "test — and energy.", S["body"]),
]))

flow += k.check_table("G1: Energy code", [
    ("Certified DET verifier engaged for the blower door (and duct test "
     "if required)", [("Verifier:", 0.6), ("Cert #:", 0.4)]),
    "Insulation R-values, window/door U-factors and SHGC shown on the "
    "plans per the 2015 IECC with Georgia amendments",
    ("Ducts and air handlers entirely inside the thermal envelope? If "
     "yes, the duct test is excepted — note it on the plans",
     [("Inside envelope? Y/N:", 1.0)]),
    ("Blower door result under 5 ACH50 — signed written report to the "
     "code official and a copy in this binder",
     [("Result:", 0.5), ("Date:", 0.5)]),
    ("Duct leakage at or under 6 cfm25/100 sq ft (unless excepted) — "
     "signed report retained", [("Result:", 0.5), ("Date:", 0.5)]),
], notes_header="Notes")
flow.append(k.cite(
    "Ga. Comp. R. &amp; Regs. 110-11-1-.34; Georgia amendments to the "
    "2015 IECC — § R402.4.1.2 (2020 packet, effective January 1, 2020) "
    "and §§ R403.3.3, R403.3.4 with exception 1, read directly from the "
    "DCA amendment PDFs; the 2023 packet does not touch these sections. "
    "Verified August 2026."))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Application filed:", 0.34),
                         ("Permit issued:", 0.33), ("Permit #:", 0.33)]))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 10))
flow.append(k.sources_table([
    ("Eight mandatory codes statewide with no local adoption; permissive "
     "codes only where adopted", "§ 8-2-25(a), (b)"),
    ("Permits/inspections a local-option power; private professional "
     "providers", "§ 8-2-26(a)(4), (g)"),
    ("Owner-builder work must conform to codes and any local permitting "
     "or inspection requirements", "§ 43-41-17(h)"),
    ("2024 I-Codes with 2026 GA Amendments and 2023 NEC effective "
     "January 1, 2026; IRC energy/plumbing/electrical parts deleted",
     "DCA; 2026 GA Amendments packet"),
    ("No mandatory fire sprinklers in one- and two-family dwellings",
     "§ 8-2-4 (in DCA packet)"),
    ("Energy code is the 2015 IECC with Georgia Supplements and "
     "Amendments", "Ga. Comp. R. &amp; Regs. 110-11-1-.34"),
    ("Blower door mandatory (< 5 ACH50, DET verifier, signed report); "
     "duct test mandatory (≤ 6 cfm25/100 sq ft) unless ducts inside the "
     "envelope", "GA IECC R402.4.1.2; R403.3.3–.3.4"),
    ("No physical development of a septic lot before the county "
     "construction permit; 20-day decision; 12-month validity; site "
     "inspection first", "DPH Rule 511-3-1-.03"),
    ("Owner may drill a well on own primary-residence property; resale "
     "development requires a licensed contractor", "§ 12-5-131.1(a)"),
    ("Land-disturbance permit or NOI required; single-family exemption "
     "under one acre; minimum standards still apply when exempt",
     "§ 12-7-7(a); § 12-7-17(4); § 12-7-6(b)"),
    ("NPDES construction general permits GAR100001/2/3",
     "EPD, epd.georgia.gov"),
    ("Notice of Commencement: 15 days, superior court clerk, posted on "
     "site; failure forfeits the screen", "§ 44-14-361.5(b), (d)"),
    ("GDOT permit for work in state right of way; residential "
     "applications at the District Area Office", "GDOT regs; § 32-6-131"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ga-permit-kit",
                       "GA.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
