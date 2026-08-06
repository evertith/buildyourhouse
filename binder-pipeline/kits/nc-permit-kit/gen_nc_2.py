#!/usr/bin/env python3
"""NC.2 Permit Application Checklist — NC Edition.

Sources verified August 2026 (see the on-page sources table):
  G.S. 87-14(a), (a1)      affidavit, workers' comp, lien agent at $40,000
  G.S. 44A-11.1(a)         when a lien agent must be designated
  G.S. 160D-1110(a),(b),(e),(g)  permits required; plan review clock; erosion
                            control precondition; lien agent on the permit
  G.S. 160D-1111           permit expiry
  G.S. 113A-57(3),(4)      one-acre land disturbance threshold, 30-day filing
  15A NCAC 18E             septic: Improvement Permit, Construction
                            Authorization, Operation Permit, issued by the
                            local health department
  15A NCAC 18E .0204(f)    no building permit until the CA has issued
  15A NCAC 02C .0300       well permit before drilling; Certificate of
                            Completion before the well may be used
  15A NCAC 18A .3802(a)    the health department samples a new well within
                            30 days — not the homeowner
  19A NCAC 02B .0601       driveway permits are NORMALLY NOT REQUIRED for a
                            single residence; District Engineer handles them
  ncosfm.gov               2018 code editions in effect. One- and two-family
                            dwellings are EXCLUDED from the 2020 State
                            Electrical Code (Amendments 10.1 & 10.2) and are
                            governed by the 2017 edition — corroborated by
                            ncbeec.org. Do not write "NC uses the 2020 NEC."
  2018 NCECC               R401.2 four compliance paths; R402.4.2 blower door
                            OPTIONAL at 5.0 ACH50 statewide; R403.3.3 duct
                            leakage test MANDATORY; three climate zones

Still deliberately hedged: which compliance path a given county accepts, and
whether a delegated local erosion program sets a threshold below one acre.
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

FORM_ID = "NC.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Application"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Everything a North Carolina owner-builder gathers, verifies, and files — "
    "with the four state-level gates that stop an application cold.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- gates
flow += k.h2_tight("THE FOUR GATES SET BY STATE LAW")
flow.append(k.body(
    "Most of what your county asks for is local. These four are not — they "
    "are conditions the General Statutes place on the issuing of your permit, "
    "and no county can waive them. Clear these before you worry about "
    "anything else."))

flow.append(k.bullet(
    "<b>1. Owner exemption affidavit</b> — verified (sworn): you own the "
    "property, will personally superintend the work, and will be present at "
    "every inspection. Forwarded to the Licensing Board. (§ 87-14(a)(1))"))
flow.append(k.bullet(
    "<b>2. Workers' compensation</b> — proof of coverage \"as required by "
    "Chapter 97,\" which reaches employers with three or more regular "
    "employees; jurisdictions use an affirmation form for everyone else. "
    "(§ 87-14(a)(2); § 97-2(1))"))
flow.append(k.bullet(
    "<b>3. Lien agent</b> — at $40,000 or more, designated before you first "
    "contract with anyone to improve the property, with the agent's details "
    "printed on the permit itself. (§ 44A-11.1(a); § 87-14(a1); "
    "§ 160D-1110(g))"))
flow.append(k.bullet(
    "<b>4. Erosion control</b> — if the job disturbs more than one acre, a "
    "plan filed at least 30 days ahead and <b>approved before the building "
    "permit may issue</b>. (§ 113A-57(4); § 160D-1110(e))"))

flow.append(Spacer(1, 6))
flow.append(k.callout("The lien agent trap", [
    Paragraph("Owner-builders routinely assume the \"owner-occupied "
              "residence\" exemption covers them. It does not. G.S. "
              "44A-11.1(a) exempts improvements to an <b>existing</b> "
              "single-family dwelling the owner already occupies. A house "
              "you are building does not exist yet and you do not occupy it "
              "— so at $40,000 or more, designate the lien agent. See NC.5.",
              S["body"]),
]))

# ---------------------------------------------------------------- A
flow += k.h2_tight("A. SITE AND PROJECT VERIFICATION")
flow += k.check_table("A1: Before anything else", [
    "Confirmed which jurisdiction issues your permit — city/town or county "
    "(see NC.4)",
    ("Parcel identification number and 911 address confirmed",
     [("PIN:", 0.55), ("Address:", 0.45)]),
    "Deed recorded in your name — you must own the land to claim the "
    "exemption",
    "Zoning district and permitted use verified with planning/zoning",
    ("Required setbacks confirmed in writing",
     [("Front:", 0.25), ("Side:", 0.25), ("Rear:", 0.25), ("Other:", 0.25)]),
    "Easements, rights-of-way, and recorded restrictions identified",
    "Flood zone status checked; floodplain requirements identified if in a "
    "Special Flood Hazard Area",
    "HOA or covenant approval obtained if applicable — private, not "
    "governmental; the county will not check it for you",
], notes_header="Notes / who confirmed")

# ---------------------------------------------------------------- B
flow += k.h2_tight("B. THE APPLICATION PACKAGE")
flow += k.check_table("B1: Forms and proofs", [
    "Building permit application, completed and signed",
    "Owner exemption affidavit — notarized (\"verified\") as § 87-14 requires",
    "Workers' compensation form as your jurisdiction words it",
    ("Lien agent designated and details supplied to the inspections "
     "department", [("Agent:", 0.6), ("Date:", 0.4)]),
    ("Estimated construction cost stated — this sets the $40,000 tests and "
     "usually the fee", [("Stated cost: $", 1.0)]),
    "Separate trade permit applications identified: electrical, plumbing, "
    "mechanical (some counties combine them; ask)",
], notes_header="Notes")

flow += k.check_table("B2: Plans and supporting drawings", [
    "Two complete plan sets (confirm how many and what format — most NC "
    "jurisdictions now take digital submission)",
    "Site plan showing property lines, setbacks, the building footprint, "
    "driveway, well and septic locations, and any easements",
    "Foundation plan, floor plans, elevations, wall sections, and a framing "
    "plan",
    "Electrical, plumbing and mechanical layouts as your county requires",
    ("Energy code compliance documentation (see section E)",
     [("Path used:", 1.0)]),
    "Engineered or manufacturer specifications for anything non-standard — "
    "trusses, ICF, SIPs, long spans, steep-slope foundations",
], notes_header="Notes")

flow.append(k.callout("They cannot require a seal just because", [
    Paragraph("\"<i>A local government shall not require residential "
              "building plans for one- and two-family dwellings to be sealed "
              "by a licensed engineer or licensed architect unless required "
              "by the North Carolina State Building Code.</i>\" "
              "(G.S. 160D-1110(b)) If you are told your plans need a seal, "
              "ask which Code provision requires it. Note the separate "
              "trade-off: architect-sealed plans are the only way out of "
              "attending every inspection (§ 160D-1113).", S["body"]),
]))

# ---------------------------------------------------------------- C
flow += k.h2_tight("C. SEPTIC AND WELL — COUNTY HEALTH, NOT THE BUILDING OFFICE")
flow.append(k.body(
    "On-site wastewater and private drinking water wells are permitted by "
    "your <b>local health department</b> under state rules, on a different "
    "track and a different timeline from your building permit. Septic runs "
    "as three sequential approvals under 15A NCAC 18E, and the first one "
    "depends on your soil — which is why it should be the very first thing "
    "you start, before you buy land if you still can."))

flow.append(k.body(
    "The three approvals, in order: the <b>Improvement Permit (IP)</b> "
    "follows the soil and site evaluation and establishes that the site can "
    "support a system and what kind; the <b>Construction Authorization "
    "(CA)</b> allows the system to actually be built; and the <b>Operation "
    "Permit (OP)</b> is issued after installation and a pre-cover "
    "inspection, and is what lets the system be used. The IP and CA are "
    "separate instruments, but § 18E .0204(c) lets a county issue them "
    "together when the IP carries no conditions."))

flow.append(k.callout("Your building permit is gated on the CA — statewide", [
    Paragraph("This one is not a county-by-county question. 15A NCAC 18E "
              "§ .0204(f): \"<i>A building permit shall not be issued for a "
              "design unit until CAs for all components of the wastewater "
              "system serving that design unit have been issued.</i>\" Note "
              "it is the <b>Construction Authorization</b> that unlocks the "
              "building permit, not the Improvement Permit — people get that "
              "backwards and lose weeks. Start the soil evaluation before "
              "anything else on this list.", S["body"]),
]))

flow += k.check_table("C1: Septic and well", [
    "Soil / site evaluation applied for with the county health department "
    "(or a Licensed Soil Scientist hired to do it and submit it for you)",
    ("Improvement Permit issued", [("IP #:", 0.55), ("Date:", 0.45)]),
    ("Construction Authorization issued — the building permit cannot issue "
     "before this", [("CA #:", 0.55), ("Date:", 0.45)]),
    "System type and drainfield location shown on your site plan and "
    "consistent with the house footprint",
    "Operation Permit obtained after installation and the pre-cover "
    "inspection — the system may not be used before it issues",
    ("Well construction permit obtained from the county health department "
     "<b>before</b> drilling, if you will have a well",
     [("Permit #:", 0.55), ("Date:", 0.45)]),
    "Grout inspection scheduled by the well contractor with the health "
    "department before grouting",
    ("Certificate of Completion issued — the well may not be placed in "
     "service without it", [("Date:", 1.0)]),
], notes_header="Notes")

flow.append(k.body(
    "<b>The health department samples your well, not you.</b> Within 30 days "
    "of issuing the Certificate of Completion it \"<i>shall collect water "
    "samples and submit them to a certified laboratory</i>\" — or ensure a "
    "certified lab does (15A NCAC 18A § .3802(a)). Your job is simply not to "
    "let it be forgotten. Testing covers total coliform, with fecal coliform "
    "or E. coli if present, plus a chemical panel including arsenic, lead, "
    "nitrate, nitrite, fluoride, iron, manganese, sodium and pH. Bacteria "
    "samples are drawn only after the disinfectant has been flushed out."))

flow.append(k.cite(
    "Septic permit names and sequence: 15A NCAC 18E (on-site wastewater "
    "rules), administered by local health departments. Well permitting is "
    "also a county health department function. The specific application "
    "forms, fees, and required water tests are set locally — confirm each "
    "with your county. Verified August 2026."))

# ---------------------------------------------------------------- D
flow += k.h2_tight("D. DRIVEWAY AND EROSION CONTROL")
flow.append(k.body(
    "<b>You probably do not need an NCDOT driveway permit — call anyway.</b> "
    "19A NCAC 02B § .0601(a) requires a Street and Driveway Access Permit to "
    "connect within a state right of way, then says \"<i>driveway "
    "connections to residences are normally excluded from this requirement</i>\" "
    "unless there is a public safety hazard, a highway construction project, "
    "or excessive or obvious drainage complications. NCDOT's policy manual "
    "agrees: \"<i>PERMITS will normally not be required for a single "
    "residence.</i>\" Contact the District Engineer anyway — the policy asks "
    "you to, so they can flag design issues and <b>arrange your driveway "
    "pipe</b>. No application fee; the form carries a $50 construction "
    "inspection fee. A stricter local ordinance governs (§ .0601(c))."))

flow += k.check_table("D1: Driveway access and erosion control", [
    "Determined whether the road you connect to is state-maintained (NCDOT) "
    "or city/county-maintained — this decides who you talk to",
    ("If state-maintained: NCDOT District Engineer contacted, and whether a "
     "permit is required for your connection confirmed in writing",
     [("District:", 0.5), ("Contacted:", 0.5)]),
    "Driveway pipe size and sight-distance requirements settled before "
    "anything is installed",
    "If city or county maintained: their driveway requirements confirmed — "
    "and any stricter local ordinance identified",
    ("Total land disturbance calculated — house, driveway, septic area, "
     "staging and spoil piles", [("Total acres disturbed:", 1.0)]),
    "If <b>more than one acre</b>: erosion and sedimentation control plan "
    "filed at least 30 days before any land disturbance begins",
    "Confirmed who reviews it — NC DEQ's land resources program or a "
    "delegated local program",
    "Plan approved — <b>the building permit cannot legally issue for "
    "land-disturbing activity until it is</b>",
    "If one acre or less: confirmed whether a local ordinance sets a lower "
    "threshold than the State's one acre",
    "Exposed slopes must be stabilized within 21 calendar days of completing "
    "a grading phase",
], notes_header="Notes")

flow.append(k.cite(
    "Driveways: 19A NCAC 02B § .0601, § .0602 (application goes to the "
    "District Engineer); NCDOT Policy on Street and Driveway Access; form "
    "TEB 65-04. Find your division at ncdot.gov → Divisions → Highways. "
    "One-acre threshold, 30-day filing and the 21-day ground cover rule: "
    "N.C.G.S. § 113A-57(2), (3), (4); no building permit for land-disturbing "
    "activity without an approved plan: § 160D-1110(e). Note the statute "
    "says <b>more than</b> one acre — exactly one acre does not trigger it, "
    "though a delegated local program may set a lower bar (§ 113A-60). "
    "Verified August 2026."))

# ---------------------------------------------------------------- E
flow += k.h2_tight("E. CODE EDITIONS AND ENERGY COMPLIANCE")
flow.append(k.body(
    "The <b>2018</b> North Carolina Residential, Energy Conservation, "
    "Plumbing, Mechanical and Fuel Gas Codes are the editions in effect. The "
    "2024 State Building Code has been adopted but its effective date "
    "remains deferred with no date set; it may be used as an alternative "
    "method on request under Administrative Code § 102.5."))

flow.append(k.callout(
    "The electrical code for your house is the 2017 NEC — not the 2020", [
        Paragraph("Nearly every summary online says \"North Carolina uses "
                  "the 2020 NEC.\" That is true for commercial work and "
                  "wrong for yours. The Office of State Fire Marshal lists "
                  "the current code as the \"2020 State Electrical Code "
                  "(2020 NEC with State Amendments; <b>excluding one- and "
                  "two-family dwellings</b>, see Amendments 10.1 &amp; "
                  "10.2).\" Those amendments send houses back to the "
                  "<b>2017 State Electrical Code</b>.", S["body"]),
        Paragraph("The NC Board of Examiners of Electrical Contractors says "
                  "the same thing: the 2020 code \"<i>is not applicable to "
                  "one- and two-family dwellings,</i>\" and the 2017 edition "
                  "\"<i>will remain effective for one- and two-family "
                  "dwellings including their accessory structures.</i>\" "
                  "Detached garages, pools and PV are covered too. Buy the "
                  "right book, and say \"2017\" at the counter.", S["body"]),
    ]))
flow.append(k.cite(
    "ncosfm.gov → Codes → State Electrical Division; ncbeec.org, \"2020 NEC "
    "Status Update.\" The 2023 State Electrical Code is on indefinite delay "
    "(S.L. 2025-2, § 5.12). Verified August 2026."))

flow.append(k.body(
    "<b>Energy compliance has four paths</b> under the 2018 NCECC "
    "(§ R401.2): prescriptive (R401–R404); simulated performance (R405); an "
    "energy rating index / HERS approach (R406); or REScheck keyed to the "
    "2018 IECC. Pick one before you draw, because they drive different "
    "documentation."))

flow.append(k.body(
    "<b>A blower-door test is optional; a duct test is not.</b> North "
    "Carolina did not adopt mandatory envelope testing — § R402.4.2 gives "
    "two coequal options: a <b>Visual Inspection Option</b> certified by the "
    "builder or permit holder, or a <b>Testing Option</b> at <b>5.0 "
    "ACH50</b> (or 0.30 CFM50 per square foot of surface area), the same "
    "figure in every NC climate zone. But <b>duct leakage testing is "
    "mandatory</b> (§ R403.3.3): 5 CFM25 per 100 sq ft total, or 4 to the "
    "outside, excepting ducts wholly inside the thermal envelope and systems "
    "serving 750 sq ft or less. One trap — an unvented conditioned attic on "
    "the reduced-R alternative requires a blower-door result under <b>3.0 "
    "ACH50</b> (§ R402.2.2.2), and the visual option is gone."))

flow.append(k.body(
    "<b>North Carolina has three climate zones, and geography will mislead "
    "you.</b> Zone 5A is six mountain counties: Alleghany, Ashe, Avery, "
    "Mitchell, Watauga and Yancey. Much of the west and northern Piedmont is "
    "4A — including <b>Wake, Durham and Buncombe</b>. The coastal plain and "
    "southern Piedmont are 3A — including <b>Mecklenburg</b>. Charlotte sits "
    "in a warmer zone than Raleigh. Look your county up in Table R301.1 "
    "rather than guessing."))

flow += k.check_table("E1: Energy code", [
    ("Compliance path chosen and confirmed acceptable to your department",
     [("Path:", 1.0)]),
    ("Climate zone for your county looked up in Table R301.1",
     [("Climate zone:", 1.0)]),
    "Insulation R-values for walls, ceiling and floors shown on the plans",
    "Window and door U-factor and SHGC values documented",
    "Air sealing approach documented — and decided whether you are using the "
    "Visual Inspection Option or a blower-door test",
    ("Duct leakage test arranged — this one is mandatory",
     [("Tester:", 0.6), ("Result:", 0.4)]),
], notes_header="Notes")
flow.append(k.cite(
    "Code editions: NC Office of State Fire Marshal, \"Codes — Current and "
    "Past.\" Compliance paths and envelope values: 2018 NC Energy "
    "Conservation Code § R401.2, § R402.4.2, § R403.3.3, § R402.2.2.2 and "
    "Table R301.1, per the OSFM approved-amendments compilation. Verified "
    "August 2026 — confirm your department's practice before you submit."))

# ---------------------------------------------------------------- rights
flow += k.h2_tight("WHAT THE STATE GUARANTEES YOU")
flow.append(k.bullet(
    "<b>A review clock.</b> If your local government reviews residential "
    "plans, \"<i>all initial reviews for the building permit shall be "
    "performed within 15 business days of submission</i>\" — and if the "
    "initial review is not done within 20 business days, the jurisdiction "
    "must refund 10% of your total permit application fee for each business "
    "day late, up to 10 days. (§ 160D-1110(b))"))
flow.append(k.bullet(
    "<b>One permit for simultaneous work</b> applied for at the same time, "
    "at the same address, under the Residential Code. (§ 160D-1110(d)(2))"))
flow.append(k.bullet(
    "<b>Two clocks once it issues.</b> The permit expires six months after "
    "issuance if work has not commenced — or sooner by local ordinance — and "
    "expires immediately if work is discontinued for 12 months after "
    "commencement. Guides claiming an \"18-month\" NC permit are describing "
    "local practice, not the statute. (§ 160D-1111)"))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Application filed:", 0.34), ("Permit issued:", 0.33),
                         ("Permit #:", 0.33)]))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 10))
flow.append(k.sources_table([
    ("Owner exemption affidavit and workers' comp proof at $40,000+",
     "G.S. 87-14(a)(1), (a)(2)"),
    ("Chapter 97 reaches employers with three or more employees",
     "G.S. 97-2(1)"),
    ("Lien agent required at $40,000+; exemption is for improvements to an "
     "existing owner-occupied dwelling", "G.S. 44A-11.1(a); 87-14(a1)"),
    ("Lien agent details must appear on the permit", "G.S. 160D-1110(g)"),
    ("Erosion plan required over one acre, filed 30 days ahead; slopes "
     "stabilized within 21 days", "G.S. 113A-57(2), (4)"),
    ("No building permit for land-disturbing activity without an approved "
     "plan", "G.S. 160D-1110(e)"),
    ("Plan review within 15 business days; fee refund past 20; no seal "
     "required on 1–2 family plans unless the Code requires it",
     "G.S. 160D-1110(b)"),
    ("One permit for simultaneous same-address residential projects",
     "G.S. 160D-1110(d)(2)"),
    ("Permit expiry: six months to commence, 12 months of inactivity",
     "G.S. 160D-1111"),
    ("Septic: Improvement Permit, Construction Authorization, Operation "
     "Permit, via the local health department", "15A NCAC 18E"),
    ("No building permit until the Construction Authorization has issued",
     "15A NCAC 18E .0204(f)"),
    ("Well permit before drilling; Certificate of Completion before service",
     "15A NCAC 02C .0304, .0306(c)"),
    ("The local health department samples a new well within 30 days",
     "15A NCAC 18A .3802(a)"),
    ("Driveway permits normally not required for a single residence",
     "19A NCAC 02B .0601(a)"),
    ("2018 Residential / Energy / Plumbing / Mechanical Codes in effect",
     "ncosfm.gov — Codes, Current and Past"),
    ("One- and two-family dwellings are excluded from the 2020 State "
     "Electrical Code and governed by the 2017 edition",
     "ncosfm.gov State Electrical; ncbeec.org"),
    ("Four energy compliance paths; 5.0 ACH50 if tested; duct test mandatory",
     "2018 NCECC R401.2, R402.4.2, R403.3.3"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "nc-permit-kit",
                       "NC.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
