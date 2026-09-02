#!/usr/bin/env python3
"""LA.2 Permit Application Checklist.

What to assemble before you file, and what is actually in force while you are
assembling it.

The headline content is the code-date rule: a Louisiana inspector inspects
against "the codes in effect for the locality on the date of the application
for the original building permit," and the state's next code cycle takes effect
1 January 2027. That makes the application date a design decision.

CITATION POLICY FOR THIS DOCUMENT. Acts 2026, No. 881 (HB 1186) enacted
Chapter 62 of Title 37 — R.S. 37:3727 through 3750 — and by its Section 5
repealed R.S. 40:1730.21 through 1730.40.2 "in its entirety," effective
1 August 2026. Every Title 40 citation in circulation is therefore a citation
to repealed law, and this kit prints the Title 37 numbers. Note when checking:
as of verification the Legislature's own statute database at legis.la.gov had
not yet reloaded, still serving the repealed Title 40 sections and returning
nothing for a Title 37 lookup. Act 881's enrolled text is the controlling
source and is what was read.
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

FORM_ID = "LA.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Before You File"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "Everything to gather before you file — and the code "
                 "editions, deadlines and thresholds that decide what you are "
                 "filing for.")
flow.append(k.disclaimer())

# ------------------------------------------------------------------ codes
flow += k.h2("THE CODE THAT BINDS YOUR HOUSE")
flow.append(k.body(
    "Louisiana runs a single mandatory construction code for the entire "
    "state. Every parish and every municipality enforces the same technical "
    "requirements; what varies is the office, the forms and the fee. The "
    "editions below are what was in force when this kit was verified."))
rows = [
    [k.cellp("<b>International Residential Code</b> — your house"),
     k.cellp("<b>2021</b>"), k.cellp("1 January 2023"),
     k.cellp("Adopted without <b>Part I (Administrative)</b> and without "
             "<b>Part VIII (Electrical)</b> — and those two exclusions do "
             "more work than anything else in this table. Everything else is "
             "in, including <b>Part VII, the plumbing chapters</b>. Appendix "
             "AQ, Tiny Houses, is adopted; Appendix J at your parish's "
             "option.")],
    [k.cellp("International Building Code"), k.cellp("<b>2021</b>"),
     k.cellp("1 January 2023"),
     k.cellp("Not your house — 1- and 2-family dwellings use the IRC.")],
    [k.cellp("International Mechanical Code"), k.cellp("<b>2021</b>"),
     k.cellp("1 January 2023"), k.cellp("HVAC.")],
    [k.cellp("International Plumbing Code"), k.cellp("<b>2021</b>"),
     k.cellp("1 January 2023"),
     k.cellp("<b>Not your house.</b> A one- or two-family dwelling plumbs to "
             "<b>IRC Part VII</b>, which Louisiana adopts and amends heavily "
             "— see below. The IPC covers the buildings the IRC does not.")],
    [k.cellp("International Fuel Gas Code"), k.cellp("<b>2021</b>"),
     k.cellp("1 January 2023"), k.cellp("Gas piping and appliances.")],
    [k.cellp("International Existing Building Code"), k.cellp("<b>2021</b>"),
     k.cellp("1 January 2023"), k.cellp("Work on existing structures.")],
    [k.cellp("<b>International Energy Conservation Code</b>"),
     k.cellp("<b>2021</b>"), k.cellp("<b>mid-2023</b>"),
     k.cellp("The IECC came in months after the rest of the package, and the "
             "Commission's own publications disagree on the day — its "
             "edition sheet says 1 July 2023, a Louisiana Register citation "
             "in the same document says 1 August 2023. If a date matters to "
             "you, get it from your permit office in writing.")],
    [k.cellp("<b>National Electrical Code</b>"), k.cellp("<b>2020</b>"),
     k.cellp("1 January 2023"),
     k.cellp("The NEC governs your wiring directly, because Part VIII of the "
             "IRC is not adopted. Louisiana amends several articles, "
             "including 210.8 and 210.52(C).")],
]
flow.append(k.ref_table(
    "Code editions in force in Louisiana",
    [k.cellp("Code", bold=True), k.cellp("Edition", bold=True),
     k.cellp("Effective", bold=True), k.cellp("Notes", bold=True)],
    # "Edition" needs 0.8in: at 0.6in the header itself split as "Editio / n",
    # which check.py's mid-token detector catches and a reader would too.
    rows, [1.70 * inch, 0.8 * inch, 0.95 * inch, CW - 3.45 * inch]))
flow.append(k.cite(
    "Editions and adoption text: LAC Title 17, Part I, Chapter 1, §§103–117 "
    "(each section captioned &ldquo;Formerly LAC 55:VI.301.A…&rdquo;), as "
    "compiled by the Louisiana Uniform Construction Code Commission, "
    "<i>Building Code Adoption &amp; Inspector Licensing Law and Rules and "
    "Regulations</i>, 1 August 2026. Effective dates: the Commission's "
    "published construction-code history sheet, revision of 6 August 2026. "
    "Both are free at lsuccc.la."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "The most valuable date in this kit: 1 January 2027",
    [
        Paragraph(
            "Louisiana does not inspect your house against whatever code "
            "happens to be current when the inspector shows up. It inspects "
            "against the code that was in force when you <i>applied</i>. The "
            "rule is one sentence: a licensed inspector &ldquo;shall conduct "
            "a building inspection using <b>the codes in effect for the "
            "locality on the date of the application for the original "
            "building permit</b>.&rdquo;", S["body"]),
        Paragraph(
            "And Louisiana's next code cycle is already scheduled. The "
            "Commission approved adoption language for the <b>2024 "
            "I-Codes</b> and the <b>2023 NEC</b> at its meeting of 7 July "
            "2026, and the approved rule text carries an effective date of "
            "<b>1 January 2027</b>.", S["body"]),
        Paragraph(
            "Put those two facts together. <b>An application filed before "
            "1 January 2027 would lock your house to the 2021 I-Codes and the "
            "2020 NEC for the life of the build</b> — through a framing "
            "inspection that may not happen until 2028. An application filed "
            "after it would not. If you are near that line, the date you file "
            "is a design decision and a budget decision, not paperwork.",
            S["body"]),
        Paragraph(
            "<b>Treat the date as scheduled, not settled.</b> Approved "
            "language is not yet promulgated law: the rule still has to "
            "complete the Administrative Procedure Act process and "
            "legislative oversight and appear in the <i>Louisiana "
            "Register</i>, and no such publication had appeared when this kit "
            "was verified. Code cycles slip. Ask your permit office which "
            "editions they are enforcing on the day you file, and get the "
            "answer in writing — that written answer, with your application "
            "date, is what R.S.&nbsp;37:3734 protects.", S["body"]),
    ]))
flow.append(k.cite(
    "Code-date rule: La. R.S. 37:3734, &ldquo;Codes applicable to building "
    "inspections,&rdquo; enacted by Acts 2026, No. 881. Next-cycle editions "
    "and date: the Commission's construction-code history sheet, revision of "
    "6 August 2026, and its published notice of the 2023 NEC and 2024 "
    "I-Code adoption."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "The statute number changed on 1 August 2026 — almost nothing has caught up",
    [
        Paragraph(
            "Until this year Louisiana's construction-code law lived at "
            "<b>R.S.&nbsp;40:1730.21 and following</b>, run by the Louisiana "
            "State Uniform Construction Code <i>Council</i>. <b>Acts 2026, "
            "No.&nbsp;881</b> moved the whole program into <b>Title 37, "
            "Chapter 62 — R.S.&nbsp;37:3727 through 3750</b> and renamed the "
            "body the Louisiana Uniform Construction Code <i>Commission</i>. "
            "Section 5 of that Act repealed R.S.&nbsp;40:1730.21 through "
            "1730.40.2 <b>&ldquo;in its entirety.&rdquo;</b>", S["body"]),
        Paragraph(
            "So every Louisiana building-code citation you will find in "
            "guides, older kits, parish handouts and code-adoption trackers "
            "points at <b>repealed law</b>. This kit prints the live numbers. "
            "Expect to meet the old ones anyway — several parish permit pages "
            "still cite the retired state web address, let alone the retired "
            "statute.", S["body"]),
        Paragraph(
            "<b>One warning if you go to check.</b> At the time this kit was "
            "verified the Legislature's own database at legis.la.gov had not "
            "reloaded: it still served the repealed Title 40 sections as "
            "though live, and returned nothing at all for a Title 37 lookup. "
            "That is a database lag, not a legal fact. Read the Act itself, "
            "or the Commission's compiled volume, rather than the statute "
            "browser.", S["body"]),
    ]))
flow.append(k.cite(
    "Acts 2026, No. 881 (House Bill No. 1186), 2026 Regular Session: enacts "
    "Chapter 62 of Title 37 comprised of R.S. 37:3727 through 3750, and by "
    "Section 5 repeals R.S. 40:1730.21 through 1730.40.2. Effective "
    "1 August 2026 — confirmed by the Commission's own editor's note to its "
    "2023 NEC and 2024 I-Code adoption language."))

# ------------------------------------------------------------------ wins
flow += k.h2_tight("TWO THINGS NO PARISH MAY REQUIRE OF YOU", reserve=2.0)
flow.append(k.body(
    "Both are worth knowing before you walk in, because both save real money "
    "and both are occasionally asked for anyway."))
flow.append(k.callout_long(
    "No stamped plans for a prescriptive house",
    [
        Paragraph(
            "&ldquo;Notwithstanding any law to the contrary, <b>a "
            "municipality or parish shall not require that a residential "
            "building plan for a one- or two-family dwelling be prepared or "
            "stamped by a licensed architect or engineer if that dwelling "
            "falls within the prescriptive standards of the International "
            "Residential Code currently adopted in the Uniform Construction "
            "Code.</b>&rdquo;", S["body"]),
        Paragraph(
            "La. R.S. 37:3737(D). Read the condition carefully: it protects a "
            "house built <b>within the IRC's prescriptive standards</b>. Step "
            "outside them — a long clear span, an unusual foundation, an "
            "engineered wind detail — and you are back to needing a design "
            "professional. In much of south Louisiana the foundation alone "
            "will take you there.", S["body"]),
    ]))
flow.append(k.callout_long(
    "No residential fire sprinklers — and no local ordinance may add them",
    [
        Paragraph(
            "&ldquo;The commission shall not adopt or enforce any part of the "
            "International Residential Code or any other code or regulation "
            "that requires a fire protection sprinkler system in one- or "
            "two-family dwellings. <b>A municipality or parish shall not "
            "adopt or enforce an ordinance or other regulation requiring a "
            "fire protection sprinkler system in one- or two-family "
            "dwellings.</b>&rdquo;", S["body"]),
        Paragraph(
            "La. R.S. 37:3733(A)(3), carried into the code itself as the "
            "Louisiana amendments to 2021 IRC Sections R313.1 and R313.2. If "
            "you install one voluntarily it must be built to R313 — the "
            "amendment says so — but nobody may make you.", S["body"]),
    ]))

flow.append(k.callout_long(
    "And one thing a parish may only do with the Commission's permission",
    [
        Paragraph(
            "R.S.&nbsp;37:3748(E): &ldquo;If a governing authority or any "
            "municipality or parish finds that the state minimum standards do "
            "not meet its needs, <b>the local government may with approval of "
            "the commission provide requirements more stringent than those "
            "specified by the state.</b>&rdquo; A parish can be stricter than "
            "the state code — but not on its own say-so.", S["body"]),
        Paragraph(
            "And an inspector cannot invent stringency at the counter. "
            "R.S.&nbsp;37:3747(A)(11)(a) makes each of these <b>a violation "
            "of the authority of the commission</b>: &ldquo;(i) Enforcing a "
            "code requirement in an area or circumstance not specified in "
            "that requirement. (ii) Enforcing a requirement in a manner that "
            "is <b>more stringent than or exceeding the code "
            "requirement</b>. … (iv) Enforcing a code official's preference "
            "in the method or manner of installation if that preference is "
            "not required by the Uniform Construction Code or contradicts a "
            "manufacturer's installation instructions or "
            "specifications.&rdquo;", S["body"]),
        Paragraph(
            "That is a real remedy, and worth knowing exists before you need "
            "it. Ask politely which code section a demand comes from. If "
            "there is no section, you now know what the statute calls that.",
            S["body"]),
    ]))

# ------------------------------------------------------------------ framing
flow += k.h2_tight("THE AMENDMENT THAT CHANGES HOW YOU FRAME", reserve=2.0)
flow.append(k.body(
    "Most of Louisiana's amendments to the IRC are administrative. One is "
    "not, and it is the single biggest technique and cost difference between "
    "building here and building to the unamended code. Louisiana rewrote the "
    "wall-bracing section:"))
flow.append(k.callout(
    "Louisiana amendment to 2021 IRC Section R602.10, Wall Bracing", [
        Paragraph(
            "&ldquo;<b>In Climate Zone 2A, one and two family dwellings shall "
            "be continuously sheathed with a minimum 7/16&quot; wood "
            "structural panels (Table R602.10.4 CS-WSP), or it's structural "
            "equivalent as per an ICC-ESR and approved by the local building "
            "official.</b>&rdquo;", S["body"]),
        Paragraph(
            "Every parish in Louisiana is Climate Zone 2A, so this is every "
            "house in the state. <b>Continuous structural sheathing is "
            "mandatory</b> — let-in bracing, portal-frame-only and "
            "gypsum-only bracing methods are off the table. Price the whole "
            "wall in sheathing from the start; discovering this at framing "
            "inspection is expensive.", S["body"]),
    ]))
flow.append(k.body(
    "Three smaller amendments in the same family, each of which an inspector "
    "will look for: a <b>6&nbsp;mil</b> ASTM E1745 Class A vapor retarder "
    "under the slab (amended §R506.2.3); <b>ring-shank roof-sheathing "
    "nails</b> required wherever wind design is required, with the plain 8d "
    "common nail allowed only where it is not (amended Table R602.3(1)); and "
    "no climate exemption from decay-resistant lumber — Louisiana struck the "
    "IRC's exception, noting in the rule itself that the committee &ldquo;felt "
    "the State of Louisiana did not have such a geographical region to "
    "preclude.&rdquo;"))
flow.append(k.cite(
    "Louisiana amendments to 2021 IRC Sections R602.10, R506.2.3, Table "
    "R602.3(1) and R317.1, LAC 17:I.107. Climate zone: Louisiana amendment "
    "to 2021 IECC Section C301.2."))

# ------------------------------------------------------------------ flood
flow += k.h2("FLOOD: THE FREEBOARD ANSWER MOST GUIDES GET BACKWARDS")
flow.append(k.body(
    "You will read, in a great many places, that Louisiana deleted its "
    "statewide freeboard requirement and left elevation entirely to the "
    "parishes. That is not what the code in force says. Louisiana's own "
    "amendment to the IRC sets a <b>floor</b> that a parish may exceed and "
    "may not go under."))
flow.append(k.callout_long(
    "Louisiana amendment to 2021 IRC Section R322 — flood construction",
    [
        Paragraph(
            "&ldquo;Buildings and structures constructed in whole or in part "
            "in flood hazard areas, including A or V Zones and Coastal A "
            "Zones, as established in Table R301.2, … shall be designed and "
            "constructed in accordance with the provisions contained in this "
            "section. Buildings and structures that are located in more than "
            "one flood hazard area shall comply with the provisions "
            "associated with the most restrictive flood hazard area. "
            "Buildings and structures located in whole or in part in "
            "identified floodways shall be designed and constructed in "
            "accordance with ASCE 24-14. <b>The local jurisdictions, "
            "utilizing flood plain managers, shall have the authority to "
            "adopt higher freeboard amounts as needed (CRS, etc.) but shall "
            "not have the authority to adopt freeboard amounts less than "
            "those required in ASCE-24-14</b>&rdquo;", S["body"]),
        Paragraph(
            "The elevation your lowest floor must reach is therefore set by "
            "<b>ASCE&nbsp;24-14</b>, a referenced standard, applied through "
            "your parish's floodplain manager — and it varies with your flood "
            "zone and the building's flood design class. This kit prints no "
            "number for it, because the number is in a copyrighted standard "
            "and depends on facts about your lot. <b>Ask your floodplain "
            "manager, in writing, for the required lowest-floor elevation for "
            "your parcel</b>, and ask separately whether the parish has "
            "adopted freeboard above the ASCE&nbsp;24-14 minimum. Many have; "
            "the Community Rating System rewards it.", S["body"]),
    ]))
flow.append(k.cite(
    "Louisiana's amendment to IRC Section R322, LAC 17:I.107. <b>Cite it by "
    "the quoted text, not the sub-number:</b> the Office of the State Register's "
    "LAC heads this amendment R322.2.1 and the Commission's compiled volume "
    "heads the identical text R322.1. Separately, "
    "R.S. 37:3738(B)(3) provides that for residential "
    "construction &ldquo;the standards published by the Federal Emergency "
    "Management Agency for the National Flood Insurance Program apply.&rdquo; "
    "Two independent routes to the same conclusion: elevation is not optional "
    "and it is not purely local."))
flow.append(k.body(
    "One practical consequence worth planning for: an <b>elevation "
    "certificate</b> prepared by a surveyor is what documents compliance, and "
    "most parishes want one before the final. Budget for it, and get the "
    "surveyor booked early — after a storm season they are the bottleneck in "
    "south Louisiana."))

# ------------------------------------------------------------------ wind
flow += k.h2_tight("WIND, AND THE ONE CLIMATE ZONE", reserve=1.8)
flow.append(k.body(
    "Louisiana's design wind speeds are among the highest in the country and "
    "they vary sharply with distance from the coast. The kit prints no "
    "parish-by-parish wind table, because the governing figure comes from the "
    "IRC's own wind speed map and its ASCE references as applied to your "
    "site, and a table transcribed from a secondary source is exactly the "
    "kind of number that gets a house built wrong. <b>Get the design wind "
    "speed and the wind-borne debris determination for your parcel from your "
    "permit office in writing</b>, and put both on your plans."))
flow.append(k.body(
    "The energy side is simpler than anywhere else in the country, and this "
    "one <i>is</i> a flat statewide answer. The Louisiana amendment to the "
    "2021 IECC reads, in full: <b>&ldquo;All parishes in Louisiana shall be "
    "Climate Zone 2A warm humid climates.&rdquo;</b> One zone, whole state — "
    "so every IECC table you use is the same row from Shreveport to Venice, "
    "and the design problem is cooling, humidity and air sealing rather than "
    "insulation depth."))
flow.append(k.cite(
    "Louisiana amendment to 2021 IECC Section C301.2, as printed in the "
    "Commission's compiled rules, 1 August 2026 (LAC 17:I.117)."))

# ------------------------------------------------------------------ septic
flow += k.h2("IF YOU ARE NOT ON PUBLIC SEWER: START HERE, AND START EARLY")
flow.append(k.body(
    "The sewage permit is the longest pole on most rural Louisiana builds and "
    "it is a <b>state</b> permit, not a parish one — it comes from the state "
    "health officer, delivered through your local parish health unit, which "
    "is a state office rather than parish government. It issues in two "
    "stages, and the first stage has to be approved before you install "
    "anything."))
rows = [
    [k.cellp("<b>Stage 1</b> — temporary permit"),
     k.cellp("Authorizes the installation. Issued only after the state health "
             "officer has determined that connection to a community sewerage "
             "system is not feasible and that soil, drainage, lot size and "
             "dimensions will support a system. <b>Valid one year</b>; ask "
             "for an extension if the build slips.")],
    [k.cellp("<b>Stage 2</b> — final permit"),
     k.cellp("Issued after installation is verified, by an on-site inspection "
             "and/or a &ldquo;Certification by Installer&rdquo; form. If you "
             "installed it yourself you are not a licensed installer, so plan "
             "on the inspection.")],
    [k.cellp("The application document"),
     k.cellp("<b>LHS-47</b>, Application for Permit for Installation of "
             "On-Site Wastewater Disposal System. It is filled out at the "
             "parish health unit — it is not a blank download.")],
    [k.cellp("Before backfill"),
     k.cellp("<b>Nothing may be covered</b> until the sanitarian has "
             "verified the installation. Notify the office "
             "<b>24&nbsp;hours</b> ahead of expected completion.")],
    [k.cellp("Why the final approval matters later"),
     k.cellp("LDH's own applicant form notes that lenders and government "
             "agencies will not approve loans or refinancing on a residence "
             "with no record of final approval. Skipping it creates a "
             "financing problem, not just a compliance one.")],
]
flow.append(k.ref_table(
    "The two-stage individual sewage permit",
    [k.cellp("", bold=True), k.cellp("", bold=True)],
    rows, [1.85 * inch, CW - 1.85 * inch]))
flow.append(k.cite(
    "LAC 51:XIII.701.A, B and C; LHS-47 named in rule at LAC 51:XIII.731.D "
    "and 733.C.8; inspection, notice and validity from LDH forms SF-10ST "
    "(rev. 07/25) and the Office of Public Health's <i>Information Packet for "
    "Applicants</i>."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Three rules that decide whether you may install it yourself",
    [
        Paragraph(
            "<b>1. You must do the actual installation.</b> LDH's form "
            "SF-10ST states the exception plainly: &ldquo;The property owner "
            "(permit holder) may install a septic tank (non-mechanical) "
            "system for their own personal use <b>only if the property owner "
            "does the actual installation</b>.&rdquo;", S["body"]),
        Paragraph(
            "<b>2. You may not hire an unlicensed helper for any part of "
            "it.</b> Same form: &ldquo;Hiring an unlicensed person to perform "
            "any part of the installation of your septic tank will not be "
            "allowed under this exception and the system in question will not "
            "be approved by this office.&rdquo; The instinct to borrow a "
            "neighbor with a backhoe forfeits the exemption.", S["body"]),
        Paragraph(
            "<b>3. A mechanical plant is off the table.</b> An individual "
            "mechanical plant — the aerobic treatment unit Louisiana leans on "
            "wherever soils and water tables defeat a conventional field — "
            "must be installed and maintained by a licensed installer "
            "(LAC 51:XIII.705.A). And because the Sanitary Code's reduced "
            "lot sizes are themselves conditioned on using a mechanical "
            "plant, a small lot can push you off the self-install path "
            "without anyone telling you.", S["body"]),
    ]))

flow += k.h2_tight("The lot-size gate — check this before you buy",
                   reserve=2.0)
flow.append(k.body(
    "Louisiana sets a statewide minimum lot size for a home on an individual "
    "sewage system, and it is stricter than most people expect. These are the "
    "criteria the state health officer applies when deciding whether an "
    "individual system may be used at all."))
rows = [
    [k.cellp("Baseline for a single lot"),
     k.cellp("<b>22,500&nbsp;sq&nbsp;ft</b> minimum area and "
             "<b>125&nbsp;ft</b> minimum frontage."),
     k.cellp("LAC 51:XIII.511.B.4")],
    [k.cellp("Large lots"),
     k.cellp("<b>One&nbsp;acre</b> or more, with <b>125&nbsp;ft</b> "
             "frontage."), k.cellp("LAC 51:XIII.511.B.3")],
    [k.cellp("Where the parish runs a formal sewage permitting system"),
     k.cellp("22,500&nbsp;sq&nbsp;ft / 80&nbsp;ft frontage; or "
             "16,000&nbsp;sq&nbsp;ft / 80&nbsp;ft <b>with a mechanical "
             "plant</b>; or 12,000&nbsp;sq&nbsp;ft / 60&nbsp;ft with a "
             "mechanical plant followed by 50&nbsp;ft of modified absorption "
             "field."), k.cellp("LAC 51:XIII.511.B.6")],
    [k.cellp("Design flow ceiling"),
     k.cellp("The individual-system route assumes total anticipated design "
             "flow not exceeding <b>1,500&nbsp;gpd</b>."),
     k.cellp("LAC 51:XIII.511.B.2")],
]
flow.append(k.ref_table(
    "Minimum lot size for a home on an individual sewage system",
    [k.cellp("", bold=True), k.cellp("Requirement", bold=True),
     k.cellp("Citation", bold=True)],
    rows, [1.75 * inch, CW - 3.55 * inch, 1.80 * inch]))
flow.append(k.cite(
    "Read the third row carefully: the smaller lot sizes are available only "
    "in parishes whose governing authority &ldquo;has enacted and enforces a "
    "formal sewage permitting system,&rdquo; and two of the three require a "
    "mechanical plant — which you may not install yourself. Whether your "
    "parish qualifies is a question for the parish, and the answer changes "
    "what you may build on a small lot."))

# ------------------------------------------------------------------ well
flow += k.h2_tight("IF YOU ARE ON A PRIVATE WELL", reserve=2.0)
flow.append(k.body(
    "The well is the mirror image of the septic system, and getting this "
    "backwards is expensive."))
rows = [
    [k.cellp("Permit before drilling?"),
     k.cellp("<b>No.</b> A domestic well needs no pre-drilling permit "
             "statewide.")],
    [k.cellp("May you drill it yourself?"),
     k.cellp("<b>No.</b> &ldquo;All water wells, regardless of use or "
             "type&rdquo; must be drilled or constructed by a contractor "
             "licensed by the department — LAC 56:I.307.A. Reworking, "
             "plugging and abandonment too. This is the exact opposite of the "
             "septic rule.")],
    [k.cellp("Notification"),
     k.cellp("For a domestic well in a non-critical ground water area, a "
             "notification form goes in <b>within 60&nbsp;days after</b> "
             "installation — and the driller's own 30-day registration "
             "satisfies it. Registration is the <b>contractor's</b> legal "
             "duty, not yours.")],
    [k.cellp("Casing depth, private supply"),
     k.cellp("Not less than <b>10&nbsp;ft</b> below ground surface.")],
    [k.cellp("Casing height"),
     k.cellp("At least <b>12&nbsp;inches</b> above ground level; in "
             "flood-prone areas at least <b>2&nbsp;ft</b> above the highest "
             "flood level of the last ten years, and never less than "
             "2&nbsp;ft above grade.")],
    [k.cellp("Grouting, private supply"),
     k.cellp("Cemented from a minimum depth of <b>10&nbsp;ft</b> to the "
             "ground surface.")],
]
flow.append(k.ref_table(
    "Private water wells",
    [k.cellp("", bold=True), k.cellp("", bold=True)],
    rows, [1.85 * inch, CW - 1.85 * inch]))
flow.append(k.cite(
    "Licensed-driller requirement: LAC 56:I.307.A and B. Notification: "
    "LAC 43:VI.701.C. Registration duty: LAC 56:I.105.A. Construction "
    "numbers: LAC 51:XII.327.A.6, A.7 and A.8. <b>One agency-name warning:</b> "
    "the program now sits with the Department of Conservation and Energy, "
    "which was the Department of Energy and Natural Resources until "
    "1 October 2025 and the Department of Natural Resources before that. The "
    "rule text still names older agencies in places — LAC 51:XII.327.A.14 "
    "still says &ldquo;Louisiana Office of Public Works.&rdquo; Follow the "
    "agency, not the printed name."))

# ------------------------------------------------------------------ ldeq
flow += k.h2_tight("THE TWO ENVIRONMENTAL PERMITS PEOPLE MISS", reserve=2.0)
flow.append(k.body(
    "Neither is a building permit and neither comes from your parish, which "
    "is exactly why they get missed."))
flow.append(k.bullet(
    "<b>Construction stormwater.</b> If your project will disturb "
    "<b>one&nbsp;acre</b> or more — and clearing, grading and the driveway "
    "all count — you are into LDEQ's construction stormwater general permit "
    "and a notice of intent. On a large rural lot this is easier to trigger "
    "than people expect."))
flow.append(k.bullet(
    "<b>Treated sewage discharge.</b> If your system will discharge treated "
    "effluent to the surface rather than to a subsurface field, LDEQ's "
    "sanitary discharge general permit is in play. The Sanitary Code says so "
    "itself: individual systems other than a conventional septic tank with "
    "subsurface disposal &ldquo;shall comply with all provisions of the "
    "Louisiana Department of Environmental Quality Wastewater Discharge "
    "Permit&rdquo; (LAC 51:XIII.703.B)."))
flow.append(k.body(
    "There is a third permission that is not a permit at all: if your "
    "effluent will reach a roadside ditch on a state highway, that is the "
    "state highway department's ditch, and you need its consent. Ask before "
    "you design the outfall — a rejected outfall can change the entire "
    "system type."))

# ------------------------------------------------------------------ checklist
flow += k.h2("THE APPLICATION CHECKLIST")
flow.append(k.body(
    "Work this with a pen. The items in the first block are the ones "
    "Louisiana adds to what any state would ask for."))
flow += k.check_table("Louisiana-specific items", [
    "<b>Affidavit Claiming Exemption from Licensure</b>, LSLBC form, "
    "notarized, all eleven statements initialed. Latest revision checked.",
    "Confirmed with the permit office whether my site is in the "
    "<b>unincorporated parish</b> or inside a municipality.",
    "Design <b>wind speed</b> for the parcel, obtained in writing, and shown "
    "on the plans.",
    "<b>Wind-borne debris</b> determination for the parcel, obtained in "
    "writing.",
    "Flood zone and required <b>lowest-floor elevation</b> from the parish "
    "floodplain manager, in writing; parish freeboard above the "
    "ASCE&nbsp;24-14 minimum confirmed separately.",
    "<b>911 address assigned</b> and posted visibly at the property.",
    "Sewage: <b>LHS-47</b> temporary permit issued (or public sewer "
    "connection confirmed available).",
    "Property plat with a <b>surveyor's seal</b> or a Clerk of Court "
    "<b>&ldquo;true copy&rdquo;</b> certification.",
    "Driveway tie-in: state highway department permit if fronting a state "
    "route; parish permit if a parish road.",
], notes_header="Where obtained / reference")

flow += k.check_table("The usual application items", [
    "Completed building permit application.",
    "Site plan showing structures, distances to property lines, well and "
    "sewage system.",
    "Construction plans. <b>No architect or engineer seal required</b> if the "
    "house is within IRC prescriptive standards.",
    "Proof of ownership with the legal description — deed, bill of sale, act "
    "of donation.",
    "Termite pretreatment arrangement.",
    "Energy compliance documentation, 2021 IECC, Climate Zone 2A.",
    "Written contracts signed with every licensed subcontractor before any "
    "work begins.",
    "License verification printouts for every sub, from the board's database.",
], notes_header="Where obtained / reference")

# ------------------------------------------------------------------ record
flow += k.h2_tight("PERMIT RECORD", reserve=2.0)
flow.append(k.body(
    "Fill this in as each permit issues, and keep it with the job. The "
    "expiry column matters more in Louisiana than most states — your sewage "
    "temporary permit runs one year."))
hdr = [k.cellp("Permit or approval", bold=True),
       k.cellp("Issuing office", bold=True),
       k.cellp("Number", bold=True), k.cellp("Issued", bold=True),
       k.cellp("Expires", bold=True)]
rows = [[k.cellp(a), "", "", "", ""] for a in [
    "Building permit",
    "Sewage — temporary permit (LHS-47)",
    "Sewage — final permit",
    "Electrical permit",
    "Plumbing permit",
    "Mechanical permit",
    "Driveway / culvert",
    "LDEQ stormwater (if 1 acre or more)",
    "LDEQ discharge (if surface discharge)",
    "Certificate of occupancy",
    "",
]]
flow.append(d.titled_table(
    "Permits and approvals on this project", hdr, rows,
    [CW - 4.55 * inch, 1.55 * inch, 1.0 * inch, 1.0 * inch, 1.0 * inch], S))

# ------------------------------------------------------------------ sources
flow.append(Spacer(1, 8))
flow.append(k.sources_table([
    ("Code editions adopted, and the parts of the IRC excluded",
     "LAC 17:I.103–117 (formerly LAC 55:VI.301.A)"),
    ("Effective dates, and the scheduled 1 January 2027 next cycle",
     "LUCCC edition sheet rev. 6 Aug 2026; approved rule text, 7 Jul 2026"),
    ("Inspections use the codes in force on the original application date",
     "R.S. 37:3734, enacted by Acts 2026, No. 881"),
    ("No architect or engineer stamp for a prescriptive IRC house",
     "R.S. 37:3737(D)"),
    ("No residential sprinkler mandate, and no local override",
     "R.S. 37:3733(A)(3); LA amendments to IRC R313.1, R313.2"),
    ("Flood construction and the ASCE 24-14 freeboard floor",
     "LA amendment to IRC R322, LAC 17:I.107"),
    ("NFIP standards apply to residential construction",
     "R.S. 37:3738(B)(3)"),
    ("The whole state is Climate Zone 2A",
     "LA amendment to 2021 IECC C301.2"),
    ("Two-stage sewage permit from the state health officer",
     "LAC 51:XIII.701.A, B, C"),
    ("Owner may install a non-mechanical system, personally, with no "
     "unlicensed help", "LAC 51:XIII.705.A; LDH form SF-10ST item 1"),
    ("Nothing covered before the sanitarian verifies",
     "LDH form SF-10ST item 4"),
    ("Minimum lot area and frontage for an individual system",
     "LAC 51:XIII.511.B.2, .3, .4, .6"),
    ("Water wells must be drilled by a licensed contractor",
     "LAC 56:I.307.A, B"),
    ("Domestic well notification within 60 days after installation",
     "LAC 43:VI.701.C"),
    ("Well casing depth, height and grouting for a private supply",
     "LAC 51:XII.327.A.6, A.7, A.8"),
    ("Non-conventional systems fall under the LDEQ discharge permit",
     "LAC 51:XIII.703.B"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "la-permit-kit",
                       "LA.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
