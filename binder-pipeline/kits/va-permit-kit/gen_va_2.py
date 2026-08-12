#!/usr/bin/env python3
"""VA.2 Permit Application Checklist — Virginia Edition.

Sources verified August 2026 (see the on-page sources table):
  USBC § 108.1/.2 (13VAC5-63-80)  permit before work begins; owner may apply;
                            256 sq ft detached-shed exemption
  § 54.1-1111               owner exemption statement + affidavit at filing
  § 54.1-402(A)(1)          no architect seal required for 1–2 family plans
                            up to three stories (excluding electrical and
                            mechanical systems)
  USBC § 110.1/.6 (13VAC5-63-100)  review "within a reasonable time" — no
                            fixed day-count; permit abandoned at six months,
                            extensions up to one year per request
  USBC § 103.5 (13VAC5-63-30); § 32.1-164(B)(1)  septic approval gates the
                            building permit on an unsewered lot
  12VAC5-610-240/-250/-300(A)/-340  VDH septic construction permit (dies at
                            18 months), filed at the local health department;
                            operation permit after final inspection
  § 32.1-163.5              private OSE/PE designs must be accepted; 15
                            working days or deemed approved
  12VAC5-630-220(B)/-230(A)/-330  private well construction permit before
                            drilling; local health department; inspection
                            statement on completion
  § 62.1-44.15:34(A); § 62.1-44.15:24; 9VAC25-875-530(B)  no land disturbance
                            until land-disturbance approval; 10,000 sq ft
                            threshold (2,500 in a CBPA); agreement in lieu of
                            a plan for a single-family detached house
  24VAC30-73-10/-20(C)/-60(A); § 33.2-240  VDOT entrance permit before
                            construction; district staff issue them
  § 36-98.01; § 43-1; § 43-4.01  the mechanics' lien agent line — owner's
                            option, "None Designated" otherwise, and the
                            30-day notice effect that protects the owner
  13VAC5-63; DHCD codes page; DHCD 2021 VRC FAQ  2021 USBC in force since
                            Jan. 18, 2024, sole edition since Jan. 18, 2025;
                            2021 I-Codes + 2020 NEC; 2024 cycle not before
                            2027; ceiling R-60 in Zones 3 and 4
  13VAC5-63-264             blower door mandatory at 5 ACH50 (Zone 4
                            verbatim); the seven eligible tester categories;
                            duct-test report signed and given to the official
  § 36-99.7                 asbestos certification — pre-1985 renovation/
                            demolition only; a footnote here, not a gate

Still deliberately hedged: the exact § 110.7 three-year completion sentence
(printed as a labeled paraphrase); the duct-testing trigger and its
exceptions (the document says to ask, and refuses to print an
inside-the-envelope exemption); the Zone 3 phrasing of the 5-ACH50 rate and
which localities sit in Zone 3A vs 4A; well water sampling duty
(12VAC5-630-431 is named, no duty is printed); floodplain (no single
statewide permit — FEMA FIRM check plus the locality's floodplain
administrator); and the state-maintained-roads assumption, phrased per the
dossier as "unless you are in a city, a town that maintains its streets, or
Henrico or Arlington."
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

FORM_ID = "VA.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Application"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Everything a Virginia owner-builder gathers, verifies, and files — "
    "with the four state-level gates that stop an application cold, and "
    "the one optional line that protects you.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- gates
flow += k.h2_tight("THE FOUR GATES SET BY STATE LAW")
flow.append(k.body(
    "Most of what your locality asks for is local. These four are not — "
    "they are conditions Virginia law places on your project, and no "
    "county, city, or town can waive them. Clear these before you worry "
    "about anything else."))

flow.append(k.bullet(
    "<b>1. The exemption statement</b> — a written statement, supported by "
    "an affidavit, that you are not subject to contractor licensure. The "
    "building official may not lawfully issue the permit without it. "
    "(§ 54.1-1111; see VA.1)"))
flow.append(k.bullet(
    "<b>2. Septic approval first</b> — on an unsewered lot, the building "
    "official may \"<i>refuse to issue a permit until the applicant has "
    "supplied certificates of functional design approval from the "
    "appropriate state agency</i>\" — and sewage disposal is on that list. "
    "(USBC § 103.5; § 32.1-164(B)(1))"))
flow.append(k.bullet(
    "<b>3. Land-disturbance approval</b> — no land-disturbing activity may "
    "begin until the local erosion/stormwater authority has issued its "
    "approval; for a single detached house an \"agreement in lieu of a "
    "plan\" replaces the engineered plan. (§ 62.1-44.15:34(A))"))
flow.append(k.bullet(
    "<b>4. The VDOT entrance permit</b> — \"<i>No entrance of any nature "
    "may be constructed within the right-of-way until the location has "
    "been approved by VDOT and an entrance permit has been issued.</i>\" "
    "Most rural Virginia driveways connect to a VDOT road. "
    "(24VAC30-73-60(A))"))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "The lien agent line — the option you should probably take", [
        Paragraph("Virginia puts a mechanics' lien agent line on every one- "
                  "or two-family dwelling permit — included \"<i>at the "
                  "request of the applicant</i>,\" and if you do not "
                  "request one, the permit must say <b>\"None "
                  "Designated\"</b> (§ 36-98.01). Take the option: with an "
                  "agent on the permit, anyone who wants lien rights must "
                  "notify the agent \"<i>within 30 days of the first date "
                  "that he performs labor or furnishes material</i>,\" and "
                  "a late notice limits the lien \"<i>to labor performed "
                  "or materials furnished on or after the date a notice is "
                  "given</i>\" (§ 43-4.01).", S["body"]),
    ]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "Without an agent on the permit, a supplier your subcontractor never "
    "paid can surface months later with lien rights you never saw coming. "
    "The agent must be a Virginia attorney, a title insurance company (or "
    "its subsidiary or licensed agents), or a financial institution "
    "authorized to accept deposits (§ 43-1) — your closing attorney or "
    "title company is the usual choice. There is no separate state form; "
    "it is a field on the permit application. See VA.5."))

# ---------------------------------------------------------------- A
flow += k.h2_tight("A. SITE AND PROJECT VERIFICATION")
flow += k.check_table("A1: Before anything else", [
    "Confirmed which locality issues your permit — county, city, or town "
    "(see VA.4)",
    ("Parcel identification number and 911 address confirmed",
     [("Parcel ID:", 0.55), ("Address:", 0.45)]),
    "Deed recorded in your name — you must own the residence to claim the "
    "exemption",
    "Zoning district and permitted use verified with planning/zoning",
    ("Required setbacks confirmed in writing",
     [("Front:", 0.25), ("Side:", 0.25), ("Rear:", 0.25), ("Other:", 0.25)]),
    "Easements, rights-of-way, and recorded restrictions identified",
    "Flood zone checked on the FEMA FIRM map for the parcel; if in a "
    "mapped floodplain, asked the locality's floodplain administrator "
    "whether a local floodplain development permit applies",
    "Chesapeake Bay Preservation Area status asked about — it drops the "
    "erosion-control trigger to 2,500 sq ft (see section D)",
    "HOA or covenant approval obtained if applicable — private, not "
    "governmental; the locality will not check it for you",
], notes_header="Notes / who confirmed")
flow.append(k.cite(
    "Floodplain: Virginia has no single statewide floodplain permit — the "
    "USBC/VRC flood provisions and local floodplain zoning ordinances tied "
    "to the NFIP govern, so the check is the FIRM map plus your locality's "
    "floodplain administrator. DCR is Virginia's NFIP coordinator "
    "(dcr.virginia.gov). Verified August 2026."))

# ---------------------------------------------------------------- B
flow += k.h2_tight("B. THE APPLICATION PACKAGE")
flow.append(k.body(
    "The USBC requires that \"<i>application for a permit shall be made "
    "to the building official and a permit shall be obtained prior to the "
    "commencement</i>\" of the work — and you may file it yourself: the "
    "applicant may be \"<i>the owner or lessee of the relevant property "
    "or the agent of either or by the RDP, contractor, or subcontractor "
    "associated with the work or any of their agents</i>\" (USBC "
    "§ 108.1). One curiosity worth knowing: one-story detached sheds "
    "with a building area up to <b>256 square feet</b> need no permit "
    "at all (§ 108.2)."))

flow += k.check_table("B1: Forms and proofs", [
    "Building permit application, completed and signed — the form is your "
    "locality's own; there is no statewide version",
    "Owner exemption statement + affidavit, per § 54.1-1111 — expect to "
    "notarize",
    ("Mechanics' lien agent designated on the application — or the permit "
     "will read \"None Designated\"",
     [("Agent:", 0.6), ("Date:", 0.4)]),
    ("Estimated construction cost stated — this usually sets the fee",
     [("Stated cost: $", 1.0)]),
    "Separate trade permit applications identified: electrical, plumbing, "
    "mechanical (some localities combine them; ask)",
    "Fee schedule obtained with the application — fees are set locally "
    "under § 36-105(B)",
], notes_header="Notes")

flow += k.check_table("B2: Plans and supporting drawings", [
    "Complete plan sets in the count and format your locality requires — "
    "many Virginia localities now take digital submission",
    "Site plan showing property lines, setbacks, the building footprint, "
    "the driveway entrance, well and septic locations, and any easements",
    "Foundation plan, floor plans, elevations, wall sections, and a "
    "framing plan",
    "Electrical, plumbing and mechanical layouts as your locality requires",
    ("Energy code compliance documentation (see section E)",
     [("Prepared by:", 1.0)]),
    "Engineered or manufacturer specifications for anything non-standard "
    "— trusses, ICF, SIPs, long spans, steep-slope foundations",
], notes_header="Notes")

flow.append(k.callout("You do not need an architect for house plans", [
    Paragraph("Virginia's architect-licensing law lets non-licensees "
              "prepare plans for \"<i>single- and two-family homes, "
              "townhouses, and multifamily dwellings, excluding electrical "
              "and mechanical systems, not exceeding three stories</i>\" — "
              "the plans must identify who drew them and that person's "
              "occupation. (§ 54.1-402(A)(1)) If you are told your plans "
              "need a seal, ask which provision requires it.", S["body"]),
]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>The clocks on your application and permit.</b> Virginia sets no "
    "fixed day-count for residential plan review — the USBC requires the "
    "building official to examine the application \"<i>within a "
    "reasonable time after filing</i>\" (§ 110.1), so ask your department "
    "its current turnaround and budget for it. Once issued, \"<i>a permit "
    "shall be considered abandoned if work is not commenced within six "
    "months after issuance or if authorized work is suspended or "
    "abandoned for a period of six months</i>\" — with extensions "
    "available up to one year per request (§ 110.6). And § 110.7 gives "
    "single-family dwelling permits a three-year completion window from "
    "issuance, extendable on a showing of substantive progress — that "
    "last sentence is a paraphrase of the section, not quoted text; read "
    "§ 110.7 itself before you rely on the details."))
flow.append(k.cite(
    "USBC § 108.1, § 108.2 (13VAC5-63-80); § 110.1, § 110.6, § 110.7 "
    "(13VAC5-63-100); § 54.1-402(A)(1); § 36-105(B). Verified August "
    "2026."))

# ---------------------------------------------------------------- C
flow += k.h2_tight("C. SEPTIC AND WELL — THE HEALTH DEPARTMENT, NOT THE "
                   "BUILDING OFFICE")
flow.append(k.body(
    "On-site sewage and private drinking water wells are permitted by the "
    "<b>Virginia Department of Health through your local health "
    "department</b>, on a different track and a different timeline from "
    "your building permit. The rule is absolute: \"<i>No person or owner "
    "shall construct, operate, expand or modify a sewage disposal or "
    "handling system without a written permit from the commissioner</i>\" "
    "(12VAC5-610-240), and state law requires \"<i>a permit from the "
    "Commissioner prior to the construction, installation, modification "
    "or operation of a sewerage system</i>\" (§ 32.1-164(B)(1)). Start "
    "this before anything else — before you buy the land, if you still "
    "can."))

flow.append(k.callout(
    "Your building permit can be held for this — statewide", [
        Paragraph("USBC § 103.5 lets the building official \"<i>refuse to "
                  "issue a permit until the applicant has supplied "
                  "certificates of functional design approval from the "
                  "appropriate state agency</i>\" — and water supply and "
                  "sewage disposal are on that functional-design list. On "
                  "an unsewered lot, VDH approval comes first. There is no "
                  "path around VDH.", S["body"]),
    ]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>The private-sector shortcut, and its shot clock.</b> You do not "
    "have to wait for a health-department evaluation: VDH \"<i>shall "
    "accept private site evaluations and designs … designed and certified "
    "by a licensed professional engineer, in consultation with a licensed "
    "onsite soil evaluator, or by a licensed onsite soil evaluator</i>\" "
    "(OSE). And on a single-lot submission the department must act "
    "\"<i>within 15 working days</i>\" — issue the permit or approval, or "
    "set out its reasons for denial in writing — or \"<i>the designs, "
    "evaluations or subdivision reviews shall be deemed approved and the "
    "appropriate letter, permit or approval shall be issued</i>.\" "
    "(§ 32.1-163.5) Hiring an OSE is how most rural builds keep the "
    "septic track off the critical path."))

flow += k.check_table("C1: Septic and well", [
    "Determined whether the lot is served by public sewer and water — if "
    "both, this section is a connection question for the utility, not VDH",
    ("VDH sewage-system application filed at the local health department "
     "— or a licensed OSE/PE hired to evaluate, design, and submit",
     [("Filed / OSE:", 0.6), ("Date:", 0.4)]),
    ("Septic construction permit issued — valid 18 months",
     [("Permit #:", 0.55), ("Date:", 0.45)]),
    "System type and drainfield location shown on your site plan and "
    "consistent with the house footprint",
    "If an alternative (non-conventional) system: designer and operating "
    "requirements confirmed under 12VAC5-613",
    "Operation permit obtained after installation and final inspection — "
    "before the system is used",
    ("Private well construction permit obtained from the local health "
     "department <b>before</b> drilling",
     [("Permit #:", 0.55), ("Date:", 0.45)]),
    "VDH inspection statement received after well completion",
    "Water sampling for the new well asked about at the local health "
    "department — who collects, what panel, and when",
], notes_header="Notes")

flow.append(k.cite(
    "Septic permit requirement, application at the local health "
    "department, 18-month permit life, and the operation permit: "
    "12VAC5-610-240, -250, -300(A), -340. Alternative systems: 12VAC5-613. "
    "OSE/PE acceptance and the 15-working-day deemed-approval clock: "
    "§ 32.1-163.5. Well permit before construction, local filing, and the "
    "completion inspection statement: 12VAC5-630-220(B), -230(A), -330 "
    "(regulations amended effective November 6, 2024; text verified "
    "post-amendment). Water-quality sampling duties sit in 12VAC5-630-431 "
    "— this kit prints no sampling promise because the who-and-when was "
    "not verified; ask your health department. Verified August 2026."))

# ---------------------------------------------------------------- D
flow += k.h2_tight("D. DRIVEWAY AND EROSION / STORMWATER")
flow.append(k.body(
    "<b>Virginia is different about roads.</b> Outside incorporated "
    "cities and towns, most public roads are maintained by VDOT, not the "
    "county. Unless you are in a city, a town that maintains its streets, "
    "or Henrico or Arlington (which run their own roads), assume the road "
    "you connect to is VDOT's — and VDOT's rule is a hard gate: \"<i>No "
    "entrance of any nature may be constructed within the right-of-way "
    "until the location has been approved by VDOT and an entrance permit "
    "has been issued.</i>\" (24VAC30-73-60(A)) A \"private entrance\" is "
    "one \"<i>that serves up to two private residences and is used for "
    "the exclusive benefit of the occupants</i>\"; district "
    "administrators or their designees issue the permits, and state law "
    "directs the Commissioner to \"<i>permit suitable connections</i>\" "
    "from private roads to improved highways (§ 33.2-240). File form "
    "LUP-A with the private-entrance schedule LUP-PE at the VDOT district "
    "office for your locality — see VA.5."))

flow += k.check_table("D1: Driveway access and erosion / stormwater", [
    "Determined who maintains the road you connect to — VDOT, a city or "
    "town, or Henrico/Arlington county",
    ("If VDOT: land use permit applied for (LUP-A + LUP-PE) at the "
     "district office <b>before</b> any entrance construction",
     [("District:", 0.5), ("Applied:", 0.5)]),
    "Entrance location, sight distance, and any pipe/culvert requirements "
    "settled with the district permit staff before installing anything",
    "If locally maintained: the locality's entrance requirements confirmed",
    ("Total land disturbance calculated — house, driveway, septic area, "
     "staging and spoil piles", [("Total sq ft disturbed:", 1.0)]),
    "If 10,000 sq ft or more (2,500 sq ft in a Chesapeake Bay "
    "Preservation Area): erosion/stormwater requirements apply",
    "Agreement in lieu of a plan requested from the local "
    "erosion/stormwater (VESMP) office for the single-family build, and "
    "executed",
    "Land-disturbance approval issued — <b>no land-disturbing activity "
    "may begin before it</b>",
    "Asked whether the authority waives the Responsible Land Disturber "
    "certificate for an agreement in lieu of a plan",
], notes_header="Notes")

flow.append(k.body(
    "<b>The erosion/stormwater rule, in the statute's own words.</b> "
    "\"<i>A person shall not conduct any land-disturbing activity until "
    "(i) he has submitted to the appropriate VESMP authority an "
    "application that includes a permit registration statement, if "
    "required, a soil erosion control and stormwater management plan or "
    "an executed agreement in lieu of a plan, if required, and (ii) the "
    "VESMP authority has issued its land-disturbance approval.</i>\" The "
    "thresholds: the requirements \"<i>shall apply to any activity that "
    "disturbs 10,000 square feet or more</i>\" — and in a Chesapeake Bay "
    "Preservation Area, single-family construction triggers at "
    "\"<i>2,500 square feet or more</i>.\" The owner-builder shortcut is "
    "the <b>agreement in lieu of a plan</b>: a contract between you and "
    "the local authority that replaces the engineered plan, available "
    "for \"<i>a single family detached residential structure with less "
    "than one acre of land disturbance</i>\" — outright when the house "
    "sits outside a common plan of development or sale, and inside one "
    "only where the development has an approved stormwater pollution "
    "prevention plan (and permit, if required). The authority "
    "\"<i>may waive the Responsible Land Disturber certificate "
    "requirement for an agreement in lieu of a plan</i>.\""))
flow.append(k.cite(
    "Entrance permits: 24VAC30-73-60(A), -20(C), -10; § 33.2-240. "
    "Erosion/stormwater: § 62.1-44.15:34(A) (prohibition, thresholds, RLD "
    "waiver); § 62.1-44.15:24 (agreement in lieu of a plan, defined); "
    "9VAC25-875-530(B) (when the agreement may be used) — the consolidated "
    "regulation 9VAC25-875 has been effective since July 1, 2024, "
    "administered locally under DEQ oversight. Each locality maintains its "
    "own agreement-in-lieu form; ask its erosion/stormwater office. "
    "Verified August 2026."))

# ---------------------------------------------------------------- E
flow += k.h2_tight("E. CODE EDITION AND ENERGY COMPLIANCE")
flow.append(k.body(
    "The <b>2021 Uniform Statewide Building Code</b> governs your "
    "project. DHCD's own words: \"<i>The effective date of the 2021 "
    "Uniform Statewide Building Code … is Jan. 18, 2024</i>\" — and since "
    "January 18, 2025 it has been the <b>only</b> edition a permit may "
    "issue under. It incorporates the <b>2021 IBC, IRC and IECC</b> and "
    "the <b>2020 National Electrical Code</b> (NFPA 70-20). The 2024 code "
    "cycle is underway, but DHCD staff guidance says the 2024-based "
    "residential code \"<i>will likely be effective in 2027</i>\" — "
    "nothing about it changes a permit pulled in 2026."))
flow.append(k.cite(
    "13VAC5-63 and its Documents Incorporated by Reference "
    "(13VAC5-63-9999); dhcd.virginia.gov/codes; DHCD 2021 VRC FAQ "
    "(updated January 8, 2025). Verified August 2026."))

flow.append(k.callout(
    "The blower door is mandatory in Virginia — no visual option", [
        Paragraph("Every new dwelling must be blower-door tested; the "
                  "visual-inspection alternative was eliminated back in "
                  "the 2018 energy code. The 2021 standard, as Virginia "
                  "amends it: \"<i>The building or dwelling unit shall be "
                  "tested and verified as having an air leakage rate not "
                  "exceeding five air changes per hour in Climate Zone "
                  "4.</i>\" That <b>5 ACH50</b> figure is a Virginia "
                  "amendment — the unamended 2021 IECC would demand 3.0.",
                  S["body"]),
        Paragraph("Virginia also names who may run the test: \"<i>a "
                  "Virginia licensed general contractor, a Virginia "
                  "licensed HVAC contractor, a Virginia licensed home "
                  "inspector, a Virginia registered design professional, a "
                  "certified BPI Envelope Professional, a certified HERS "
                  "rater, or a certified duct and envelope tightness "
                  "rater.</i>\" Book one before drywall is scheduled, not "
                  "after.", S["body"]),
        Paragraph("Virginia spans Climate Zones 3 and 4 under the 2021 "
                  "code. The companion provision extends the 5-ACH50 rate "
                  "to the Zone 3 localities per the regulation's text, but "
                  "this kit did not verify that sentence verbatim — if "
                  "your locality is in Zone 3, <b>confirm your zone and "
                  "your target number with your building department</b> "
                  "before you order the test.", S["body"]),
    ]))
flow.append(k.cite(
    "13VAC5-63-264, provisions R402.4.1.2 and R402.4.1.3 (VRC "
    "N1102.4.1.2/.3). Verified August 2026."))

flow.append(k.body(
    "<b>Ceilings jumped to R-60.</b> DHCD confirms it in writing: "
    "\"<i>The minimum insulation R-Value for ceilings in Climate Zones 3 "
    "and 4 increased from 49 in the 2018 VRC, to 60 in the 2021 "
    "VRC.</i>\" DHCD also notes the 2024 IRC later walked that back — but "
    "R-60 governs your 2026 permit unless your building official approves "
    "a code modification under VCC 106.3. Price the extra insulation into "
    "the plan rather than fighting it at final."))
flow.append(k.body(
    "<b>Duct testing is required too.</b> Duct leakage testing has been "
    "required in Virginia since the 2018 energy code and continues under "
    "the 2021 edition, and the paper matters: \"<i>A written report of "
    "the results of the test shall be signed by the party conducting the "
    "test and provided to the code official.</i>\" This kit does not "
    "print the test's trigger conditions or exceptions — in particular, "
    "do <b>not</b> assume ducts inside the conditioned envelope are "
    "exempt. Ask your building department which duct tests apply to your "
    "system, and get the answer before the mechanical rough-in."))

flow += k.check_table("E1: Energy code", [
    ("Climate zone for your locality confirmed with the building "
     "department", [("Climate zone:", 1.0)]),
    "Insulation R-values for walls, ceiling (R-60 in Zones 3 and 4) and "
    "floors shown on the plans",
    "Window and door U-factor and SHGC values documented",
    ("Blower-door test booked with a tester from the permitted categories "
     "— target 5 ACH50 in Zone 4",
     [("Tester:", 0.6), ("Result:", 0.4)]),
    ("Duct leakage testing scope confirmed with the building department; "
     "test arranged", [("Tester:", 0.6), ("Result:", 0.4)]),
    "Signed written test reports delivered to the code official before "
    "final",
], notes_header="Notes")
flow.append(k.cite(
    "Code edition and R-60: 13VAC5-63; DHCD 2021 VRC FAQ; VRC "
    "§ N1102.1.3; modification authority VCC 106.3. Blower door and duct "
    "testing: 13VAC5-63-264 (R402.4.1.2/.3, R403.3.3–R403.3.5). Verified "
    "August 2026 — confirm your department's practice before you submit."))

# ---------------------------------------------------------------- demolition footnote
flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>One footnote if you are demolishing first:</b> Virginia's "
    "permit-time asbestos certification (§ 36-99.7) applies only to "
    "renovating or demolishing a building whose initial permit predates "
    "January 1, 1985 — and even then single-family dwellings are "
    "excepted. It is not a gate on your new house; it only surfaces if "
    "you are taking down an old non-dwelling structure on the lot first."))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Application filed:", 0.34),
                         ("Permit issued:", 0.33),
                         ("Permit #:", 0.33)]))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 10))
flow.append(k.sources_table([
    ("Permit before work begins; the owner may apply personally; "
     "256 sq ft shed exemption", "USBC § 108.1, § 108.2"),
    ("Owner exemption statement + affidavit; official may not issue "
     "without it", "§ 54.1-1111"),
    ("Lien agent line on every 1–2 family permit at the applicant's "
     "request, else \"None Designated\"", "§ 36-98.01"),
    ("Who may serve as lien agent; 30-day notice or the lien is limited "
     "to later work", "§ 43-1; § 43-4.01"),
    ("No architect seal required for 1–2 family plans to three stories",
     "§ 54.1-402(A)(1)"),
    ("Review \"within a reasonable time\" — no fixed day-count; six-month "
     "abandonment, extensions to one year; three-year completion window "
     "(paraphrase)", "USBC § 110.1, § 110.6, § 110.7"),
    ("Building official may hold the permit for functional-design "
     "(septic/water) approval", "USBC § 103.5; § 32.1-164(B)(1)"),
    ("No septic construction without a written VDH permit; 18-month "
     "permit life; operation permit after inspection",
     "12VAC5-610-240, -300(A), -340"),
    ("Private OSE/PE evaluations must be accepted; 15 working days or "
     "deemed approved", "§ 32.1-163.5"),
    ("Private well construction permit before drilling; inspection "
     "statement on completion", "12VAC5-630-220(B), -330"),
    ("No land disturbance before land-disturbance approval; 10,000 sq ft "
     "threshold; 2,500 in a CBPA; RLD waiver",
     "§ 62.1-44.15:34(A)"),
    ("Agreement in lieu of a plan for a single-family detached house",
     "§ 62.1-44.15:24; 9VAC25-875-530(B)"),
    ("No entrance constructed in the right-of-way without VDOT approval "
     "and a permit; district staff issue",
     "24VAC30-73-60(A), -20(C)"),
    ("Suitable private connections to improved highways shall be "
     "permitted", "§ 33.2-240"),
    ("2021 USBC effective Jan. 18, 2024; sole edition since Jan. 18, "
     "2025; 2021 I-Codes + 2020 NEC", "13VAC5-63; dhcd.virginia.gov"),
    ("2024-based residential code likely 2027", "DHCD 2021 VRC FAQ"),
    ("Ceiling R-60 in Climate Zones 3 and 4", "DHCD FAQ; VRC N1102.1.3"),
    ("Blower door mandatory, 5 ACH50 in Zone 4; seven eligible tester "
     "categories; signed duct-test report to the official",
     "13VAC5-63-264"),
    ("Asbestos certification: pre-1985 renovation/demolition only; "
     "single-family dwellings excepted", "§ 36-99.7"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "va-permit-kit",
                       "VA.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
