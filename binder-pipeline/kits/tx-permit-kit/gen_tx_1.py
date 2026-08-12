#!/usr/bin/env python3
"""TX.1 The Owner-Builder's Legal Position in Texas.

Every Texas claim in this document was read out of the statute text at
statutes.capitol.texas.gov in August 2026, or against the administering
agency's own pages, and is cited on-page. Where the statute is silent or
cities differ, the document says so and gives the verification step.

Verified sources:
  tdlr.texas.gov            no GC/home-builder program on the A-Z list; TRCC
                            statute expired 2009 (printed as an as-of-2026
                            absence, never a timeless one)
  Occ. Code § 1305.151      electrical license required
  Occ. Code § 1305.003(a)(6)  homeowner electrical exemption, verbatim —
                            "owns and resides in" + municipal-ordinance carve-in
  Occ. Code § 1305.201(d),(e)  local ordinances govern in cities; unincorporated
                            work must meet the state electrical code (2023 NEC
                            per 16 TAC § 73.100)
  tdlr.texas.gov/electricians/exemptions.htm  TDLR's own gloss
  Occ. Code § 1301.003      TSBPE continued to Sept. 1, 2033 — plumbing did
                            NOT move to TDLR
  Occ. Code § 1301.051      homestead plumbing exemption, verbatim
  Occ. Code § 1301.052      rural exemption excludes new construction
  Occ. Code § 1301.255      plumbing codes adopted by board rule
  Occ. Code § 1302.053      HVAC homeowner exemption, verbatim
  Occ. Code § 1302.052      exempt work still subject to municipal permits
  Occ. Code § 1302.251      HVAC license; valid statewide
  Occ. Code § 1901.001(15)(A)  own-property water well carve-out
  Houston Permitting Center; Fort Worth Development Services; San Antonio DSD
                            city registration and homeowner-permit practices
  HB 2127 (2023); SB 2038 → Loc. Gov't Code §§ 42.101–.105; HB 3699 (2023)

Still deliberately hedged: whether the electrical "owns and resides in"
exemption covers a NEW house you do not yet occupy (no TDLR interpretation
found — the biggest legal-risk item in the kit); the homestead/"person's
home" scope of the plumbing and HVAC exemptions for a not-yet-occupied
build; HB 2127's practical reach; and every city's owner-builder permit
practice, which the buyer confirms in writing.
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

FORM_ID = "TX.1"
FORM_TITLE = "The Owner-Builder's Legal Position in Texas"
TOPIC = "Legal Position"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What Texas actually requires of a person building their own house — "
    "the licenses that do not exist, the three trade licenses that do, and "
    "the city-hall practices that decide what you may do yourself.")

flow.append(k.disclaimer(
    "Statute text was read at statutes.capitol.texas.gov in August 2026; "
    "statutes change."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION")
flow.append(k.body(
    "Texas has <b>no statewide general contractor license</b> and <b>no "
    "state building permit</b> for houses. You do not apply to the State "
    "for permission to be your own builder — there is no affidavit, no "
    "exemption to claim, no board that reviews you. What Texas regulates "
    "instead is narrower and sharper: <b>electrical, plumbing, and HVAC "
    "work each require a state license</b>, each licensing law has a "
    "homeowner carve-out, and <b>the three carve-outs use different words "
    "with different traps</b>. On top of that, if your lot is inside a "
    "city, the city's permit system treats you as the contractor of record "
    "— and each city has its own rules about what an owner may pull "
    "permits for."))
flow.append(k.cite(
    "Absence of a GC license: TDLR's regulated-program list (tdlr.texas."
    "gov), checked August 2026. Trade licensing: Occupations Code Chs. "
    "1305 (electrical), 1301 (plumbing), 1302 (HVAC)."))

rows = [
    [k.cellp("Do you need a license to build your own house?"),
     k.cellp("No. As of August 2026 no Texas state agency issues a general "
             "contractor or home builder license — for you or anyone "
             "else.")],
    [k.cellp("Do you need a state permit?"),
     k.cellp("No such permit exists. Building permits in Texas are "
             "municipal; counties generally cannot require one for a "
             "single-family house (see TX.2).")],
    [k.cellp("May you wire, plumb, and duct it yourself?"),
     k.cellp("Each trade has its own homeowner exemption with its own "
             "wording — and the electrical one is genuinely uncertain for "
             "a new build. Read the trade sections below before you "
             "decide.")],
    [k.cellp("Who checks any of this?"),
     k.cellp("Inside a city: the city's permit and inspection system. "
             "Outside one: almost nobody by default — which is its own "
             "kind of trap (see TX.3).")],
]
flow.append(k.ref_table(
    "The position at a glance",
    [k.cellp("Question", bold=True), k.cellp("Texas's answer", bold=True)],
    rows, [2.7 * inch, CW - 2.7 * inch]))

# ---------------------------------------------------------------- the absence
flow += k.h2_tight("THE ABSENCE — NO GC LICENSE, NO STATE PERMIT")
flow.append(k.body(
    "This is a provable absence, and worth proving, because officials and "
    "lenders sometimes doubt it. The Texas Department of Licensing and "
    "Regulation's public A-Z list of every program it regulates contains "
    "no general-contractor, home-builder, or residential-construction "
    "program; its construction-side programs are air conditioning and "
    "refrigeration contractors, electricians, and water well drillers and "
    "pump installers (plus elevators, boilers, and industrialized "
    "housing). The agency that once registered builders — the Texas "
    "Residential Construction Commission — was abolished when its statute "
    "expired in 2009 and was never replaced."))
flow.append(k.body(
    "There is also no statewide permit counter. The building-permit "
    "statutes are all municipal (Local Government Code Chapter 214), and "
    "the county statutes affirmatively deny permit power over houses "
    "(Chapter 233 — worked in TX.2). The Texas State Law Library's "
    "building-codes guide puts it plainly: state law adopts minimum "
    "residential <i>codes</i> for cities and some unincorporated areas — "
    "codes, not permits."))

flow.append(k.callout("Print-date warning — say it the careful way", [
    Paragraph("The accurate sentence is: \"<b>As of August 2026, no Texas "
              "state agency issues a general contractor or home builder "
              "license.</b>\" It is not \"no license is ever required\" — "
              "three trades ARE licensed, below — and it is not a timeless "
              "fact: legislatures create licenses, and the TRCC's "
              "existence from 2003 to 2009 proves Texas has tried. Verify "
              "nothing has changed at tdlr.texas.gov before you rely on "
              "this.", S["body"]),
]))
flow.append(k.cite(
    "TDLR regulated-program list, tdlr.texas.gov, August 2026; Local Gov't "
    "Code Chs. 214, 233; Texas State Law Library building-codes guide, "
    "guides.sll.texas.gov."))

# ---------------------------------------------------------------- electrical
flow += k.h2_tight("ELECTRICAL — OCCUPATIONS CODE CH. 1305 (TDLR)")
flow.append(k.body(
    "The rule: \"<i>Except as provided by Section 1305.003, a person or "
    "business may not perform or offer to perform electrical work … unless "
    "the person or business holds an appropriate license issued or "
    "recognized under this chapter.</i>\" (§ 1305.151) The homeowner "
    "carve-out is in § 1305.003(a)(6): the chapter does not apply to "
    "\"<i>work not specifically regulated by a municipal ordinance that is "
    "performed in or on a dwelling by a person who owns and resides in the "
    "dwelling</i>.\" TDLR's own gloss agrees: a person who performs "
    "electrical work on a dwelling \"that they own and reside in\" is not "
    "required by the state to be licensed — with the caveat that municipal "
    "or regional regulations may override the exemption."))

flow.append(k.callout(
    "The two traps in (a)(6) — read them before you buy wire", [
        Paragraph("<b>Trap one: \"not specifically regulated by a municipal "
                  "ordinance.\"</b> A city ordinance can take the exemption "
                  "away entirely — and Houston does. The City of Houston "
                  "issues electrical permits only to registered, licensed "
                  "master electricians; a homeowner cannot pull an "
                  "electrical permit in Houston at all (Houston Permitting "
                  "Center, electrical permit pages and the Houston "
                  "Electrical Code administrative provisions). Ask your "
                  "city before assuming the state exemption reaches you.",
                  S["body"]),
        Paragraph("<b>Trap two: \"owns and RESIDES in the dwelling.\"</b> A "
                  "new house under construction is a dwelling you do not "
                  "yet reside in. TDLR has published no formal "
                  "interpretation for new construction, and the plain text "
                  "reads as existing-residence work — contrast the plumbing "
                  "and HVAC exemptions, which use ownership language, not "
                  "residence-in-the-dwelling. <b>The safe reading is that "
                  "wiring a new house you do not yet occupy is NOT clearly "
                  "covered.</b> If you are building in an unincorporated "
                  "area and counting on this exemption, either hire a "
                  "licensed electrician or put the question to TDLR in "
                  "writing and keep the answer. This is the biggest "
                  "legal-risk item in this kit.", S["body"]),
    ]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "Even where the exemption applies, the code still does: \"<i>Electrical "
    "work performed in an unincorporated area of the state must be "
    "installed in accordance with standards at least as stringent as the "
    "requirements of the state electrical code</i>\" (§ 1305.201(e)) — "
    "which, by TDLR rule, is the <b>2023 National Electrical Code</b>, "
    "effective September 1, 2023. Inside a city, electrical work must "
    "follow local ordinances (§ 1305.201(d))."))
flow.append(k.cite(
    "Occ. Code §§ 1305.151, 1305.003(a)(6), 1305.201(d), (e); 16 TAC "
    "§ 73.100 (2023 NEC); TDLR exemptions page, tdlr.texas.gov/"
    "electricians/exemptions.htm. All read August 2026."))

# ---------------------------------------------------------------- plumbing
flow += k.h2_tight("PLUMBING — OCCUPATIONS CODE CH. 1301 (TSBPE — NOT TDLR)")
flow.append(k.body(
    "Plumbing is licensed by the <b>Texas State Board of Plumbing "
    "Examiners</b> — a standalone board, not TDLR. The board survived its "
    "2019 sunset scare and was continued; its statute now runs to "
    "September 1, 2033 (§ 1301.003, as amended 2021 and 2023). Guides "
    "claiming plumbing moved to TDLR are wrong."))
flow.append(k.body(
    "The homeowner exemption is one sentence, verbatim: \"<i>PLUMBING BY "
    "PROPERTY OWNER IN HOMESTEAD. A property owner is not required to be "
    "licensed under this chapter to perform plumbing in the property "
    "owner's homestead.</i>\" (§ 1301.051) No occupancy condition, no "
    "resale condition — in the statute itself."))

flow.append(k.callout("Two edges to respect", [
    Paragraph("<b>\"Homestead\" for a house that does not exist yet.</b> "
              "Texas homestead law can attach to land intended and "
              "prepared for homestead use before the house exists, but "
              "neither Chapter 1301 nor the board's rules define the term "
              "for this exemption. For a new build on land you own and "
              "intend as your homestead the exemption is generally "
              "understood to apply — but confirm with TSBPE "
              "(tsbpe.texas.gov) before relying on it, and city permits "
              "and inspections apply regardless.", S["body"]),
    Paragraph("<b>The rural exemption is NOT for you.</b> § 1301.052 "
              "exempts some unlicensed plumbing outside cities — but only "
              "work \"<i>other than plumbing performed in conjunction with "
              "new construction, repair, or remodeling</i>.\" A new house "
              "is new construction; the homestead exemption in § 1301.051 "
              "is the one that matters.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "Codes: the board adopts the Uniform Plumbing Code and International "
    "Plumbing Code and may adopt later editions by rule (§ 1301.255(a), "
    "(b)); licensees working in areas not otherwise regulated must follow "
    "the board-adopted code (§ 1301.255(c)); cities may amend locally "
    "(§ 1301.255(d)). This kit prints no UPC/IPC edition year — the board "
    "adopts editions by rule and has amended them repeatedly. Verify the "
    "current edition in the board rules at tsbpe.texas.gov."))
flow.append(k.cite(
    "Occ. Code §§ 1301.003, 1301.051, 1301.052, 1301.255; tsbpe.texas.gov. "
    "Read August 2026."))

# ---------------------------------------------------------------- HVAC
flow += k.h2_tight("HVAC — OCCUPATIONS CODE CH. 1302 (TDLR)")
flow.append(k.body(
    "A license is required to engage in air conditioning and refrigeration "
    "contracting (§ 1302.251(a)); the state license is valid statewide and "
    "cities may not require a municipal license on top of it "
    "(§ 1302.251(b)). The homeowner exemption, verbatim: "
    "\"<i>HOMEOWNERS. This chapter does not apply to a person who engages "
    "in air conditioning and refrigeration contracting in a building owned "
    "solely by the person as the person's home.</i>\" (§ 1302.053)"))
flow.append(k.body(
    "Those are narrower words than the plumbing exemption, and two "
    "readings are unresolved: <b>\"owned solely by the person\"</b> on "
    "jointly titled property, and <b>\"as the person's home\"</b> for a "
    "new build you do not yet live in. No TDLR published interpretation "
    "was found on either. For a new build, confirm with TDLR before "
    "relying on it. And exemption from the license is not exemption from "
    "the permit: \"<i>Work performed by a person who is exempt from this "
    "chapter is subject to any permit, inspection, or approval required by "
    "a municipal ordinance.</i>\" (§ 1302.052)"))
flow.append(k.cite(
    "Occ. Code §§ 1302.251(a), (b), 1302.053, 1302.052. Read August 2026."))

# ---------------------------------------------------------------- summary table
flow += k.h2_tight("THE THREE EXEMPTIONS SIDE BY SIDE")
trade_rows = [
    [k.cellp("<b>Electrical</b><br/>TDLR"),
     k.cellp("\"…performed in or on a dwelling by a person who <b>owns and "
             "resides in</b> the dwelling\" — and only where no municipal "
             "ordinance regulates it"),
     k.cellp("New construction (you do not reside there yet); cities can "
             "abolish it by ordinance — Houston has"),
     k.cellp("§ 1305.003(a)(6)")],
    [k.cellp("<b>Plumbing</b><br/>TSBPE"),
     k.cellp("\"A property owner is not required to be licensed … to "
             "perform plumbing in the property owner's <b>homestead</b>\""),
     k.cellp("\"Homestead\" scope for a not-yet-occupied new build — "
             "generally understood to apply, unconfirmed by rule"),
     k.cellp("§ 1301.051")],
    [k.cellp("<b>HVAC</b><br/>TDLR"),
     k.cellp("\"…contracting in a building <b>owned solely</b> by the "
             "person <b>as the person's home</b>\""),
     k.cellp("Joint title; a new build not yet \"the person's home\""),
     k.cellp("§ 1302.053")],
]
flow.append(k.ref_table(
    "Trade-by-trade — three different wordings, three different traps",
    [k.cellp("Trade", bold=True), k.cellp("The exemption's words", bold=True),
     k.cellp("The unresolved edge", bold=True), k.cellp("Authority", bold=True)],
    trade_rows,
    [1.0 * inch, 2.6 * inch, CW - 1.0 * inch - 2.6 * inch - 1.05 * inch,
     1.05 * inch]))
flow.append(Spacer(1, 6))
flow.append(k.callout("The rule that covers all three", [
    Paragraph("Being exempt from a <b>license</b> is never being exempt "
              "from a <b>permit</b>. Inside a city, the city's permit, "
              "inspection, and registration ordinances apply to exempt "
              "work in every trade (§ 1302.052 says so expressly for HVAC; "
              "§ 1305.201(d) for electrical; § 1301.255(d) lets cities "
              "amend the plumbing code locally). Outside a city, the "
              "licensing laws still apply — the enforcement gap in TX.3 is "
              "not a legality gap.", S["body"]),
]))

# ---------------------------------------------------------------- wells
flow += k.h2_tight("WATER WELLS — THE ONE CLEAN CARVE-OUT")
flow.append(k.body(
    "The own-property exemption is built into the definition: a "
    "\"<i>water well driller</i>\" \"<i>does not include a person who … "
    "drills, bores, cores, or constructs a water well on the person's own "
    "property for the person's own use</i>\" (Occ. Code "
    "§ 1901.001(15)(A)). A landowner may drill their own well without a "
    "TDLR license. The real gate is local: most of Texas sits inside a "
    "groundwater conservation district (Water Code Ch. 36), and districts "
    "commonly require registration or a permit before ANY well is drilled "
    "— even exempt domestic wells — plus spacing rules. Find and call your "
    "district before you drill; TX.2 carries the checklist line."))
flow.append(k.cite(
    "Occ. Code § 1901.001(15)(A); Water Code Ch. 36. District rules are "
    "district-by-district — verified only as to the pattern, August 2026."))

# ---------------------------------------------------------------- city practice
flow += k.h2_tight("CITY HALL PRACTICE — REGISTRATION AND OWNER-BUILDER "
                   "PERMITS")
flow.append(k.body(
    "Inside a city, the licensing statutes are only half the story. Cities "
    "require the person pulling each permit to be registered or licensed "
    "with the city — and each city decides which permits an owner-occupant "
    "may pull personally. Three verified examples of how differently that "
    "goes:"))

city_rows = [
    [k.cellp("<b>Fort Worth</b>"),
     k.cellp("Anyone pulling building, mechanical, plumbing, or electrical "
             "permits must hold a Development Services <b>Contractor "
             "Registration</b> — and the city publishes <b>Homestead "
             "Permit Affidavit</b> forms by which a homeowner certifies "
             "they own and live at the address and will personally perform "
             "the work under a specific permit (mechanical and plumbing "
             "versions).")],
    [k.cellp("<b>San Antonio</b>"),
     k.cellp("Contractors register with Development Services before "
             "permitting; the city licenses residential \"Home Improvement "
             "Contractors\" (Class I/II). Homeowners \"<i>attesting that "
             "they own and will occupy or rent their residence for a "
             "period of 12 months after project completion can request a "
             "homeowner's permit … and will be responsible for all "
             "inspections</i>\" (sa.gov, DSD Residential Permits).")],
    [k.cellp("<b>Houston</b>"),
     k.cellp("A homeowner may obtain the <b>plumbing</b> permit and do the "
             "work on a residence they \"own, occupy, and have … "
             "registered as their homestead\" — form CE1284, the "
             "Homeowner's Plumbing and Irrigation System Permit "
             "Application — but <b>electrical</b> permits issue only to "
             "licensed master electricians. Same city, opposite answers "
             "by trade.")],
]
flow.append(k.ref_table(
    "Three cities, three different owner-builder doors (verified "
    "August 2026)",
    [k.cellp("City", bold=True),
     k.cellp("What its own pages say", bold=True)],
    city_rows, [1.15 * inch, CW - 1.15 * inch]))
flow.append(Spacer(1, 6))
flow.append(k.callout("The two questions to ask your city — in writing", [
    Paragraph("The label differs city to city — \"homeowner permit,\" "
              "\"homestead affidavit,\" \"owner-builder\" — and some "
              "cities have no homeowner path for some trades. Before you "
              "count on doing any work yourself, ask the permit office: "
              "<b>(1) May the owner-occupant pull this permit personally? "
              "(2) Which trades are excluded?</b> Keep the written answer "
              "with this kit.", S["body"]),
]))
flow.append(k.cite(
    "fortworthtexas.gov, Development Services — Contractor Registration and "
    "Homestead Affidavits PDF; sa.gov, DSD Contractor and Residential "
    "Permits pages; houstonpermittingcenter.org, form CE1284 and electrical "
    "permit pages. All read August 2026."))

# ---------------------------------------------------------------- 2023-25 laws
flow += k.h2_tight("THE 2023–2025 LAWS — WHAT CHANGED AROUND YOU")
flow.append(k.bullet(
    "<b>HB 2127 (2023), the \"Texas Regulatory Consistency Act,\"</b> "
    "preempts city regulation in fields occupied by several state codes, "
    "including the Occupations Code. A district court held it "
    "unconstitutional in 2023; the Third Court of Appeals reversed and "
    "upheld it in July 2025. Its practical effect on trade permitting is "
    "still unsettled in 2026 — this kit prints no \"city X can no longer "
    "require Y\" claims, and the express municipal authorizations cited "
    "above (like § 1305.201) were not repealed."))
flow.append(k.bullet(
    "<b>SB 2038 (2023):</b> landowners in most ETJ areas may petition for "
    "release from a city's extraterritorial jurisdiction (Local Gov't Code "
    "§ 42.102); if the city sits on a valid petition, \"<i>the area is "
    "released by operation of law</i>\" (§ 42.105(d)). 2025's HB 2512 "
    "narrowed which areas qualify (§ 42.101) — check the exclusions before "
    "planning around a release. What the ETJ means for you is worked in "
    "TX.4."))
flow.append(k.bullet(
    "<b>HB 3699 (2023)</b> tightened municipal platting: cities must "
    "publish their complete plat-application checklist, and the trigger "
    "for when a plat is required was narrowed. Relevant at the \"is my lot "
    "legally platted?\" step inside cities and the ETJ — see TX.2, "
    "Track A."))
flow.append(k.cite(
    "HB 2127 (88R) and the July 2025 Third Court of Appeals decision; "
    "SB 2038 (88R) → Local Gov't Code §§ 42.101–.105, as amended by "
    "HB 2512 (89R, 2025); HB 3699 (88R), enrolled bill analysis at "
    "capitol.texas.gov. Read August 2026."))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("POSITION CHECKLIST — SETTLE THESE BEFORE YOU PLAN THE "
                   "WORK")
flow.append(k.body(
    "Every line is a decision this document has shown to be yours to make "
    "— and most of them change the budget. Work down it with a pen."))

flow += k.check_table("Step 1 — Your track and your city's rules", [
    ("Determined whether the lot is inside city limits, inside an ETJ, or "
     "unincorporated (TX.4 shows how)",
     [("Track:", 1.0)]),
    "If inside a city: asked the permit office, in writing, whether an "
    "owner-occupant may pull the building permit and each trade permit "
    "personally — and which trades are excluded",
    ("City's owner-builder / homestead form identified (name and number "
     "vary by city — see TX.5)", [("Form:", 1.0)]),
    "If in an ETJ: checked whether the city applies platting or other "
    "rules there, and whether an SB 2038 release petition makes sense "
    "for the lot",
], notes_header="Notes / who answered")

flow += k.check_table("Step 2 — Trade-by-trade decisions", [
    ("ELECTRICAL: decided between a licensed electrician (license "
     "verified with TDLR) and the homeowner exemption — and if relying "
     "on the exemption for a NEW build, put the question to TDLR in "
     "writing first (the \"owns and resides in\" trap)",
     [("License #:", 0.55), ("Verified:", 0.45)]),
    "PLUMBING: confirmed the homestead exemption covers your situation "
    "with TSBPE if the house is not yet occupied — or hired a licensed "
    "plumber",
    "HVAC: confirmed with TDLR if title is joint or the house is not yet "
    "your home — or hired a licensed contractor",
    "WELL (if any): groundwater conservation district identified and its "
    "registration/permit and spacing rules confirmed BEFORE drilling",
    ("Written answers filed with this kit",
     [("TDLR:", 0.34), ("TSBPE:", 0.33), ("District:", 0.33)]),
], notes_header="Notes")

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("No state GC license as of August 2026; TRCC expired 2009",
     "TDLR program list, tdlr.texas.gov"),
    ("Electrical homeowner exemption — owns AND resides; cities can "
     "override", "Occ. Code §§ 1305.151, 1305.003(a)(6)"),
    ("Houston issues electrical permits only to licensed masters",
     "houstonpermittingcenter.org"),
    ("Unincorporated electrical work must meet the 2023 NEC",
     "Occ. Code § 1305.201(e); 16 TAC § 73.100"),
    ("Plumbing board (TSBPE) continued through Sept. 1, 2033",
     "Occ. Code § 1301.003"),
    ("Homestead plumbing exemption", "Occ. Code § 1301.051"),
    ("Rural plumbing exemption excludes new construction",
     "Occ. Code § 1301.052"),
    ("HVAC homeowner exemption — \"owned solely … as the person's home\"",
     "Occ. Code § 1302.053"),
    ("Exempt HVAC work still subject to municipal permits",
     "Occ. Code § 1302.052"),
    ("Own-property, own-use water well needs no TDLR license",
     "Occ. Code § 1901.001(15)(A)"),
    ("City owner-builder practice: Fort Worth homestead affidavits; San "
     "Antonio homeowner's permit (12-month attestation); Houston "
     "plumbing-only, form CE1284",
     "fortworthtexas.gov; sa.gov; houstonpermittingcenter.org"),
    ("HB 2127 upheld on appeal July 2025; practical reach unsettled",
     "88R HB 2127; Third Ct. App. (2025)"),
    ("ETJ release by petition; release by operation of law if the city "
     "sits on it", "Loc. Gov't Code §§ 42.102, 42.105(d)"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "tx-permit-kit",
                       "TX.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
