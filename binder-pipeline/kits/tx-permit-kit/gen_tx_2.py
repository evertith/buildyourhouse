#!/usr/bin/env python3
"""TX.2 Permit Application Checklist — Texas Edition, two tracks.

Sources verified August 2026 (see the on-page sources table):
  Loc. Gov't Code § 214.212   IRC as of May 1, 2012 = the municipal
                              residential code; local amendments; newer
                              editions; § 214.217 21-day notice in big cities
  Loc. Gov't Code § 214.904   45-day municipal action clock; fee refund
  Loc. Gov't Code Ch. 212; HB 3699 (2023)  platting; published checklists
  Loc. Gov't Code §§ 233.062–.063, 233.152–.157  county fire-code permits are
                              non-residential; Subchapter F opt-in standards,
                              three inspections, no county fee, no prior
                              approval
  Health & Safety Code § 366.051, .052, .0515  OSSF permit + approved plan
                              BEFORE construction; the precise 10-acre
                              exemption; aerobic maintenance
  30 TAC Ch. 285; TCEQ Form 0235  OSSF rules and TCEQ's application form
  Water Code §§ 16.315, 16.3145, 16.3221  county floodplain orders; Class C
                              misdemeanor, each day a separate offense
  Health & Safety Code §§ 388.003–.004  statewide energy code (2015 IRC
                              Ch. 11 as of Aug. 2026); the three verbatim
                              compliance options outside cities; 3-year
                              retention; ERI scores in § 388.003(j)
  Insurance Code §§ 2210.251, 2210.2515  windstorm: WPI-1 notice BEFORE
                              construction; certificate = evidence of TWIA
                              insurability; the two certificate routes
  43 TAC § 11.52; TxDOT Form 1058  driveway onto the state system
  Occ. Code § 1901.001(15)(A); Water Code Ch. 36  wells; groundwater districts
  Tex. Const. art. XVI § 50(a)(5); Property Code § 53.254  homestead liens —
                              written contract BEFORE work, both spouses,
                              filed with the county clerk
  Property Code § 5.008(e)    seller's disclosure exemption for a never-
                              occupied new house
  Humber v. Morton, 426 S.W.2d 554 (Tex. 1968); Centex Homes v. Buecher,
  95 S.W.3d 266 (Tex. 2002)   builder-vendor implied warranties
  Houston / San Antonio / Fort Worth / Dallas permitting portals and plan
                              requirements — each city's published pages

Still deliberately hedged: which IRC edition YOUR city enforces; whether
your county requires driveway/culvert permits on county roads; groundwater
district rules; whether a not-yet-occupied house is already "homestead" for
lien purposes; whether SECO adopts a newer energy edition during the kit's
life; and which counties have opted into Subchapter F (no statewide roster
exists — you ask the county).
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

FORM_ID = "TX.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Application"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Two checklists — one for a lot inside a city, one for the "
    "unincorporated county — plus the homestead lien rules that apply on "
    "both tracks.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

flow += k.h2_tight("FIRST: WHICH CHECKLIST IS YOURS?")
flow.append(k.body(
    "Work <b>Track A</b> if your lot is inside a city's limits: the city "
    "issues a building permit and everything funnels through its portal. "
    "Work <b>Track B</b> if the lot is unincorporated: there is usually no "
    "building permit at all — instead, four or five separate approvals "
    "each gate one thing you need (the septic system, the floodplain, the "
    "insurance, the driveway, the meter). In a city's ETJ, start with "
    "Track B and ask the city which of its rules — usually platting — "
    "reach you. How to determine your track is worked in TX.4."))

# ================================================================ TRACK A
flow += k.h2_tight("TRACK A — LOT INSIDE A CITY'S LIMITS")
flow.append(k.body(
    "The statutory floor: the International Residential Code \"as it "
    "existed on May 1, 2012\" is \"adopted as a municipal residential "
    "building code in this state\" and applies to all residential "
    "construction in a municipality (Local Gov't Code § 214.212(a), (b)). "
    "Cities may amend it after a public hearing and by ordinance, and may "
    "adopt newer ICC editions (§ 214.212(c)–(e)) — the big cities all "
    "have. Which edition <b>your</b> city enforces is a local fact this "
    "kit deliberately does not print: ask, and write it below. Houston, "
    "for example, is on the 2021 code family per the Houston Permitting "
    "Center."))
flow.append(k.callout("Your one statewide guarantee — the 45-day clock", [
    Paragraph("The city must grant or deny the permit, provide written "
              "reasons, or reach a written agreement with you within "
              "<b>45 days</b> of the application — and must refund permit "
              "fees if it blows an agreed extended deadline. "
              "(Local Gov't Code § 214.904)", S["body"]),
]))
flow.append(Spacer(1, 6))

flow += k.check_table("A1: Before you file", [
    ("City permitting portal identified and account registered — Houston: "
     "iPermits/ProjectDox; San Antonio: BuildSA; Fort Worth: Accela; "
     "Dallas: DallasNow", [("Portal:", 1.0)]),
    ("IRC edition and local amendments your city enforces confirmed",
     [("Edition:", 0.5), ("Confirmed:", 0.5)]),
    "Lot is legally platted — or the replat is filed and approved before "
    "the permit (Ch. 212; the city must publish its complete "
    "plat-application checklist)",
    "Zoning, setbacks, and any overlay districts confirmed in writing",
    "Flood zone checked; if any part of the site is in a Special Flood "
    "Hazard Area, the city's floodplain development requirements "
    "identified (cities must maintain NFIP-eligibility ordinances — Water "
    "Code § 16.3145)",
    "Contractor registration sorted: yours, if the city lets an "
    "owner-builder act as general contractor — and the city's answer to "
    "TX.1's two questions filed with this kit",
    "Homeowner/homestead affidavit forms obtained for each trade the city "
    "lets you pull yourself (see TX.5)",
], notes_header="Notes / who confirmed")

flow += k.check_table("A2: The application package", [
    "Application completed in the city's portal",
    "Site/plot plan: property lines, setbacks, footprint, driveway, "
    "easements, drainage",
    "Foundation plan — engineered in the expansive-soil metros; "
    "city-variable but near-universal, so ask before you draw",
    "Floor plans, elevations, wall sections, window and door schedule",
    ("Energy-code compliance documentation — cities administer and enforce "
     "the energy code and report to SECO (Health &amp; Safety Code "
     "§ 388.003(c))", [("Path/report:", 1.0)]),
    "Registration numbers for each trade contractor — or the homeowner "
    "affidavit where the city allows it",
    "Driveway / curb-cut approval per the city standard",
    "Tree rules checked — San Antonio, for example, requires a tree "
    "inspection before the certificate of occupancy",
    ("Filed, and the 45-day clock noted",
     [("Filed:", 0.5), ("Day 45:", 0.5)]),
], notes_header="Notes")
flow.append(k.cite(
    "Loc. Gov't Code §§ 214.212, 214.217, 214.904; Ch. 212 as amended by "
    "HB 3699 (2023); Water Code § 16.3145; Health &amp; Safety Code "
    "§ 388.003(c). Portal names and plan-content items reflect each named "
    "city's published requirements, read August 2026; your city's list "
    "governs."))

# ================================================================ TRACK B
flow += k.h2_tight("TRACK B — LOT IN THE UNINCORPORATED COUNTY")
flow.append(k.callout("The frame — read this first", [
    Paragraph("No county building permit exists for a single-family "
              "house. County fire-code permits expressly apply only to "
              "commercial, public, and 4-plus-unit buildings (Local Gov't "
              "Code §§ 233.062(a), 233.063), and the opt-in county "
              "building-standards subchapter \"<i>may not be construed to "
              "… require prior approval by the county before the "
              "beginning of new residential construction</i>\" "
              "(§ 233.153(d)(1)). What follows is not a permit "
              "application — it is the list of the separate approvals "
              "that ARE required, each from a different office.",
              S["body"]),
]))
flow.append(Spacer(1, 8))

# ---- B1 septic
flow.append(Paragraph("B1 — Septic (OSSF): the permit that functions as "
                      "the de facto building permit", S["h3"]))
flow.append(k.body(
    "\"<i>A person must hold a permit and an approved plan to construct, "
    "alter, repair, extend, or operate an on-site sewage disposal "
    "system.</i>\" (Health &amp; Safety Code § 366.051(a)) The permit "
    "comes from the local \"authorized agent\" — usually the county — or "
    "from TCEQ where no agent exists (§ 366.051(b)); the rules are 30 TAC "
    "Ch. 285, and a site evaluation comes first. Because it is the one "
    "approval nearly every rural build needs BEFORE construction, treat "
    "it as your building permit: start it first."))
flow += k.check_table("B1: Septic", [
    ("Authorized agent for your county identified (TCEQ's lookup map at "
     "tceq.texas.gov)", [("Agent:", 1.0)]),
    "Site evaluation performed and filed",
    ("Permit application filed — the county's own packet, or TCEQ Form "
     "0235 where TCEQ is the permitting authority",
     [("Filed:", 0.5), ("Permit #:", 0.5)]),
    "10-acre exemption checked precisely: single residence on a tract of "
    "10 acres or larger, disposal lines no closer than 100 feet to the "
    "property line, effluent retained on-site, no nuisance, no groundwater "
    "pollution — all conditions, not any (§ 366.052(a), (b))",
    "If an aerobic system: owner maintenance duties under § 366.0515 "
    "understood (penalties apply in counties of 40,000+ population)",
], notes_header="Notes")

# ---- B2 floodplain
flow.append(Paragraph("B2 — Floodplain development permit", S["h3"]))
flow.append(k.body(
    "Every Texas county must adopt NFIP-eligibility orders (Water Code "
    "§ 16.3145) and may enforce floodplain management rules (§ 16.315). "
    "Violating the subchapter is a <b>Class C misdemeanor — and each day "
    "is a separate offense</b> (§ 16.3221). Practically: if any part of "
    "the site is in a Special Flood Hazard Area, you need a county "
    "floodplain development permit and an elevation certificate before "
    "construction. Some counties go further — Montgomery County requires "
    "a development permit for ALL land development, in and outside the "
    "floodplain (mctx.org)."))
flow += k.check_table("B2: Floodplain", [
    "Flood zone determined for every part of the site — not just the "
    "house pad",
    ("County floodplain administrator identified (TX.4)",
     [("Office:", 1.0)]),
    ("If in an SFHA: floodplain development permit obtained BEFORE "
     "construction", [("Permit #:", 0.5), ("Date:", 0.5)]),
    "Elevation certificate arranged",
    "Asked whether your county requires a development permit even outside "
    "the floodplain (Montgomery County does)",
], notes_header="Notes")

# ---- B3 energy
flow.append(Paragraph("B3 — Energy code: yes, even here", S["h3"]))
flow.append(k.body(
    "The fact that surprises everyone: Texas has a statewide energy code "
    "that applies where no permit office exists. For single-family "
    "construction it is the energy efficiency chapter (Ch. 11) of the "
    "IRC; SECO adopted the <b>2015 edition</b> effective September 1, "
    "2016, and it remains the statewide standard as of August 2026 — "
    "check SECO's single-family page, because a public-input process on "
    "newer editions opened in late 2025 and the law lets SECO adopt a "
    "newer edition with at least nine months' notice (Health &amp; Safety "
    "Code § 388.003(a), (a-1))."))
flow.append(k.body(
    "How you comply outside a city is spelled out verbatim in "
    "§ 388.004(a): \"<i>For construction outside of the local "
    "jurisdiction of a municipality: (1) a building certified by a "
    "national, state, or local accredited energy efficiency program shall "
    "be considered in compliance; (2) a building with inspections from "
    "private code-certified inspectors using the energy efficiency "
    "chapter of the International Residential Code or International "
    "Energy Conservation Code shall be considered in compliance; and (3) "
    "a builder who does not have access to either of the above methods "
    "for a building shall certify compliance using a form provided by the "
    "laboratory, enumerating the code-compliance features of the "
    "building.</i>\" \"The laboratory\" is the Energy Systems Laboratory "
    "at Texas A&amp;M (esl.tamu.edu), which publishes the builder "
    "self-certification form. As the builder, <b>you keep the original "
    "compliance documentation for three years and give the owner a "
    "copy</b> (§ 388.004(b)) — as owner-builder, that means your own "
    "file. An ERI path with declining maximum scores by climate zone is "
    "in § 388.003(j)."))
flow += k.check_table("B3: Energy code", [
    ("Compliance route chosen: accredited program / private code-"
     "certified inspector / ESL builder self-certification form",
     [("Route:", 1.0)]),
    "Insulation, window, and equipment choices checked against 2015 IRC "
    "Chapter 11 (edition as of August 2026 — confirm at SECO's page)",
    "Documentation filed and the three-year retention copy in this "
    "binder",
], notes_header="Notes")

# ---- B4 windstorm
flow.append(Paragraph("B4 — Windstorm certification (coastal counties "
                      "only)", S["h3"]))
flow.append(k.body(
    "This applies in the designated catastrophe area: the 14 first-tier "
    "coastal counties — Aransas, Brazoria, Calhoun, Cameron, Chambers, "
    "Galveston, Jefferson, Kenedy, Kleberg, Matagorda, Nueces, Refugio, "
    "San Patricio, Willacy — plus the parts of Harris County east of "
    "SH 146 (tdi.texas.gov/wind). The notice comes BEFORE construction, "
    "verbatim: \"<i>A person shall provide written notice on a form "
    "prescribed by and submitted to the department of the person's intent "
    "to construct … a structure for which the person is seeking coverage "
    "under this chapter before the person begins to construct … the "
    "structure.</i>\" (Insurance Code § 2210.2515(b)) TDI's form for this "
    "is the <b>WPI-1</b>."))
flow.append(k.callout("Why you cannot skip it", [
    Paragraph("To be insurable by TWIA — the windstorm insurer of last "
              "resort on the coast — a structure built on or after "
              "January 1, 1988 \"<i>must comply with the plan of "
              "operation</i>\" (§ 2210.251(a)), and the certificate of "
              "compliance \"<i>is evidence of insurability of the "
              "structure by the association</i>\" (§ 2210.251(g)). Two "
              "routes to the certificate (§ 2210.2515(c), (d)): a "
              "licensed professional engineer's sealed design and "
              "affirmation, or a TDI-appointed qualified inspector "
              "inspecting during construction; TDI issues the "
              "WPI-8/WPI-8-E. Building first and trying to buy TWIA later "
              "is the classic coastal owner-builder disaster.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow += k.check_table("B4: Windstorm (skip unless coastal)", [
    "Confirmed whether the site is in the catastrophe area "
    "(tdi.texas.gov/wind — first-tier county list)",
    ("WPI-1 filed with TDI BEFORE construction begins",
     [("Filed:", 1.0)]),
    ("Certificate route chosen: engineer (sealed design/affirmation) or "
     "TDI-appointed qualified inspector during construction",
     [("Route:", 1.0)]),
    "Inspection-at-each-phase plan made (see TX.3) — missed phases cannot "
    "be re-inspected after cover",
], notes_header="Notes")

# ---- B5-B7
flow.append(Paragraph("B5 — Driveway, well, and the opt-in county "
                      "standards", S["h3"]))
flow += k.check_table("B5: Driveway / well / Subchapter F", [
    "Driveway onto a STATE-system highway (including FM roads): TxDOT "
    "permit obtained BEFORE constructing the access — TxDOT Form 1058 to "
    "the local district/area office; no work in the right of way until "
    "the executed permit is in hand, with 24-hour notice to TxDOT "
    "(43 TAC § 11.52)",
    "Driveway onto a COUNTY road: asked the county road &amp; bridge / "
    "engineer's office whether a driveway or culvert permit is required "
    "(county-variable — Comal County, for example, lists one)",
    "Well: groundwater conservation district identified and its "
    "registration/permit and spacing rules confirmed BEFORE drilling — "
    "your own-property, own-use well needs no TDLR license (Occ. Code "
    "§ 1901.001(15)(A)), but the district's rules still apply",
    "Asked the county one exact question: \"Has the commissioners court "
    "adopted a resolution under Local Government Code chapter 233, "
    "subchapter F?\" (No statewide roster exists)",
    "If YES — Subchapter F county: new construction must conform to the "
    "IRC as of May 1, 2008 or the county seat's edition (§ 233.153(a)); "
    "YOU hire one of the six listed inspector types for at least three "
    "inspections — foundation before concrete, framing/mechanical before "
    "drywall, final (§ 233.154(a)); county notice forms before starting "
    "and within 10 days after final, if the county requires them "
    "(§ 233.154(b), (c)); no county fee is allowed (§ 233.153(f))",
], notes_header="Notes")
flow.append(k.cite(
    "Health &amp; Safety Code §§ 366.051, 366.052, 366.0515; 30 TAC "
    "Ch. 285; TCEQ Form 0235; Water Code §§ 16.315, 16.3145, 16.3221; "
    "Health &amp; Safety Code §§ 388.003–.004; Insurance Code "
    "§§ 2210.251, 2210.2515; 43 TAC § 11.52; TxDOT Form 1058; Occ. Code "
    "§ 1901.001(15)(A); Loc. Gov't Code §§ 233.062–.063, 233.152–.157 "
    "(El Paso County is a verified opted-in example, epcounty.com). "
    "Verified August 2026."))

# ================================================================ liens
flow += k.h2_tight("BOTH TRACKS — THE HOMESTEAD LIEN RULES ARE YOUR "
                   "CONTRACT LAW")
flow.append(k.body(
    "Texas has no state license board watching your subs — what it has "
    "instead is the strongest homestead protection in the country, and it "
    "cuts both ways: it protects your house from bad lien claims, and it "
    "voids lien rights for anyone who skips the formalities, which makes "
    "good subs insist on them. The constitutional baseline (Tex. Const. "
    "art. XVI § 50(a)(5)) protects the homestead from forced sale except, "
    "among others, for \"<i>work and material used in constructing new "
    "improvements thereon, if contracted for in writing</i>\" — and for "
    "repair or renovation of <b>existing</b> improvements only if further "
    "conditions are met (both spouses' consent, a 5-day wait after the "
    "credit application, a 3-day rescission right, closing at a lender, "
    "attorney, or title office)."))
flow.append(k.callout(
    "Get the structure right — most summaries print it wrong", [
        Paragraph("For <b>NEW improvements</b> — your build — the "
                  "constitution requires the <b>written contract</b>. The "
                  "extra (A)–(D) conditions attach to <b>repair or "
                  "renovation of EXISTING improvements</b>, not to new "
                  "construction. (Tex. Const. art. XVI § 50(a)(5))",
                  S["body"]),
        Paragraph("The statutory mechanics (Property Code § 53.254): to "
                  "fix a lien on a homestead, the contract must be "
                  "written, \"<i>executed before the material is "
                  "furnished or the labor is performed</i>,\" signed by "
                  "<b>both spouses</b> if married, and <b>filed with the "
                  "county clerk</b>. Lien affidavits against a homestead "
                  "must carry the 10-point bold \"THIS IS NOT A LIEN\" "
                  "notice (§ 53.254(f)), and subcontractor notices must "
                  "include the statutory warning about the owner's 10 "
                  "percent retainage (§ 53.254(g)).", S["body"]),
    ]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "Whether a not-yet-occupied house is already \"homestead\" for lien "
    "purposes is fact-dependent — intent plus preparation can establish "
    "homestead before occupancy. The safe course, and this kit's rule: "
    "<b>behave as if homestead rules apply</b> — written contract, both "
    "spouses' signatures, before work begins, filed with the clerk, for "
    "every trade — and reserve <b>10 percent retainage for 30 days after "
    "completion</b>, the duty the § 53.254(g) notice reflects."))
flow += k.check_table("L1: Lien hygiene, every sub and supplier", [
    "Written contract signed BEFORE any material is furnished or labor "
    "performed",
    "Both spouses signed, if married",
    ("Contract filed with the county clerk",
     [("Clerk file #:", 0.5), ("Date:", 0.5)]),
    "10 percent retainage withheld for 30 days after completion",
], notes_header="Trade / contractor")

flow.append(k.body(
    "<b>If you sell later:</b> the seller's-disclosure statute does not "
    "apply to a transfer \"<i>of a new residence of not more than one "
    "dwelling unit which has not previously been occupied for residential "
    "purposes</i>\" (Property Code § 5.008(e)). But a builder-vendor "
    "selling a new house gives common-law implied warranties of good "
    "workmanship and habitability (Humber v. Morton, 426 S.W.2d 554 "
    "(Tex. 1968)), and habitability is effectively non-waivable except "
    "for known defects (Centex Homes v. Buecher, 95 S.W.3d 266 (Tex. "
    "2002)). Whether a one-off owner-builder who sells soon after "
    "completion counts as a builder-vendor is fact-specific — treat a "
    "quick sale as a risk, not a plan. There is no statutory new-home "
    "warranty in Texas; the TRCC scheme died in 2009."))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 10))
flow.append(k.sources_table([
    ("IRC (May 1, 2012) is the municipal residential code; cities amend "
     "and adopt newer editions", "Loc. Gov't Code § 214.212"),
    ("45-day municipal action clock, with fee refund",
     "Loc. Gov't Code § 214.904"),
    ("Cities must publish the complete plat-application checklist",
     "Ch. 212; HB 3699 (2023)"),
    ("County fire-code permits reach only commercial/public/4+ unit "
     "buildings", "Loc. Gov't Code §§ 233.062(a), 233.063"),
    ("Opt-in subchapter creates no prior county approval; no county fee",
     "Loc. Gov't Code § 233.153(d)(1), (f)"),
    ("Subchapter F: IRC (May 1, 2008) or county seat's edition; three "
     "private inspections; county notices",
     "Loc. Gov't Code §§ 233.153(a), 233.154"),
    ("OSSF permit + approved plan before construction; authorized agents; "
     "TCEQ where none", "Health & Safety Code § 366.051; 30 TAC Ch. 285"),
    ("The 10-acre OSSF exemption and its exact conditions",
     "Health & Safety Code § 366.052"),
    ("County NFIP orders mandatory; violations a Class C misdemeanor, "
     "each day separate", "Water Code §§ 16.3145, 16.3221"),
    ("Statewide energy code = IRC Ch. 11, 2015 edition as of Aug. 2026; "
     "adoption process", "H&S Code § 388.003(a), (a-1); SECO"),
    ("Three compliance routes outside cities; 3-year retention; owner "
     "copy", "H&S Code § 388.004(a), (b)"),
    ("Windstorm notice before construction (WPI-1); certificate = "
     "evidence of TWIA insurability",
     "Ins. Code §§ 2210.2515(b), 2210.251(a), (g)"),
    ("Driveway permit before constructing access to the state system",
     "43 TAC § 11.52; TxDOT Form 1058"),
    ("Own-property, own-use well exempt from TDLR licensing",
     "Occ. Code § 1901.001(15)(A)"),
    ("New-improvement homestead lien requires a written contract; "
     "repair/renovation adds conditions", "Tex. Const. art. XVI § 50(a)(5)"),
    ("Homestead lien contract: written, pre-work, both spouses, filed "
     "with the clerk", "Property Code § 53.254"),
    ("Seller's disclosure not required for a never-occupied new house",
     "Property Code § 5.008(e)"),
    ("Implied warranties of workmanship and habitability on a "
     "builder-vendor sale", "Humber v. Morton; Centex v. Buecher"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "tx-permit-kit",
                       "TX.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
