#!/usr/bin/env python3
"""OH.2 Permit Application Checklist.

What to gather before filing — organized around the fact that in Ohio the
building permit is the one approval that might not exist, while the sewage
permit, the private water permit, the zoning certificate and the stormwater
notice do not care what your county decided about building-code certification.

The centerpiece of this document is the code-editions table, because Ohio's
residential electrical standard moved from the 2017 NEC to the 2023 NEC on
15 April 2024 and almost nothing published since has caught up. The reason is
worth printing and is printed: the Board of Building Standards files its rules
as redline PDFs, so the referenced-standards line literally reads "70—17 23"
with the 17 struck through. Extract that text and the strikethrough is lost.

Verified sources:
  OAC 4101:8-1-01 101.1   the RCO's title and its 2018 IRC base, quoted
  OAC 4101:8-1-01 101.2   scope — every one-, two-, or three-family dwelling
  OAC 4101:8-44-01        referenced standards: NFPA 70—23, IECC—18
  OAC 4101:8-34-01 3401.1 NFPA 70 incorporated wholesale, plus 8 amendments
  OAC 3701-29-06(G)(3)    the septic isolation distances
  OAC 3701-29-06(G)(1)    the replacement-area requirement
  OAC 3701-29-07(A)       who may perform the soil evaluation
  OAC 3701-29-03(H)       the owner-installer registration waiver, precisely
  OAC 3701-29-09(I)       the operation permit and its ten-year cap
  OAC 3701-28-03(A),(B)   the private water permit and its site-plan contents
  OAC 3701-28-18(A)(3),(4)  the owner-driller registration path
  OAC 3701-28-07(D),(G),(H)  well setbacks outside Table 1
  Ohio EPA OHC000006      construction stormwater general permit, one acre
  R.C. 3791.04(C),(D),(E),(G)  expiration, the conclusive presumption, the
                          30-day rule, and conditional approval

DELIBERATELY NOT PRINTED:
  - Any permit fee. Health-district and building-department fees are local and
    change annually. The document names which fees EXIST, which is stable and
    useful, and leaves the amounts to the write-in lines.
  - Any frost depth, ground snow load or seismic design category as a STATEWIDE
    number. These are not omissions in the code, they are blanks the code
    leaves for each jurisdiction to fill in — which is itself the finding, and
    is printed as such. The only statewide floor is RCO 403.1.4's 12 inches.
  - "Annual operation permit." The rule sets no annual term; the board of
    health picks one, capped at ten years.
  - Any Ohio EPA discharging-system permit number. That permit expires at the
    end of 2026 and would date the kit; the construction stormwater permit is
    printed with both of its dates instead.

Sprinklers, radon and the plumbing edition were all open when this document was
first drafted and are now resolved from the rule text, so they are printed as
fact rather than omitted: RCO 313.2 (no sprinkler requirement), RCO 101.1 (no
appendices adopted, so no radon provisions exist), and RCO 2501.1 with the
April 2024 amendment that unpinned the plumbing edition.
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

FORM_ID = "OH.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "What to Gather"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The approvals that apply wherever you build, the code editions actually "
    "in force, and the one standard Ohio changed in 2024 that most guides "
    "still print wrong.")

flow.append(k.disclaimer(
    "Code editions and rule text were read at codes.ohio.gov in September "
    "2026, including the Board of Building Standards' filed rule PDFs."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- everywhere
flow += k.h2_tight("WHAT APPLIES WHEREVER YOU BUILD", reserve=2.0)
flow.append(k.body(
    "Work this list first. Every item on it is a state-level requirement that "
    "does not depend on whether a building department is certified for your "
    "parcel — which means it applies in the most rural township in Ohio "
    "exactly as it applies in Columbus."))
rows = [
    [k.cellp("<b>Sewage treatment system permit</b>"),
     k.cellp("Local board of health"),
     k.cellp(f"Statewide rules at OAC {k.rule('3701-29')}, in force since "
             f"1{NB}January 2015. Constrains where the house can sit — do "
             f"it before you fix the footprint")],
    [k.cellp("<b>Private water system permit</b>"),
     k.cellp("Local board of health"),
     k.cellp(f"OAC {k.rule('3701-28')}, in force since 1{NB}January 2020. "
             f"Required <b>before</b> drilling: \"no work shall commence until "
             f"a valid permit has been issued\"")],
    [k.cellp("<b>Zoning certificate</b>"),
     k.cellp("Township, county or municipality"),
     k.cellp(f"A wholly separate authority from the building code. Townships "
             f"zone under R.C. Chapter{NB}519, counties under Chapter{NB}303 — "
             f"both only in unincorporated territory")],
    [k.cellp("<b>Driveway or access permit</b>"),
     k.cellp("Depends on the road"),
     k.cellp("State route: the Ohio Department of Transportation district. "
             f"County road: the county engineer ({sec('5543.16')}). Township "
             f"road: the township trustees ({sec('5571.02')})")],
    [k.cellp("<b>Building sewer / sanitary tap</b>"),
     k.cellp("City engineer, board of health, or sewer purveyor"),
     k.cellp(f"Only if you are on public sewer. That office \"shall issue all "
             f"the necessary permits\" for building sewers "
             f"({sec('3781.03')})")],
    [k.cellp("<b>Floodplain development permit</b>"),
     k.cellp("Local floodplain administrator"),
     k.cellp("Issued by the community, not the state. Check the flood map "
             "before you buy, not after")],
    [k.cellp("<b>Construction stormwater notice</b>"),
     k.cellp("Ohio EPA"),
     k.cellp("Only at one acre of disturbance — but read the common-plan trap "
             "below before deciding you are under it")],
    [k.cellp("<b>Utility locate</b>"),
     k.cellp("Ohio 811"),
     k.cellp("Free, and required before any excavation")],
]
flow.append(k.ref_table(
    "The approvals that do not depend on a building department",
    [k.cellp("What", bold=True), k.cellp("Who issues it", bold=True),
     k.cellp("What to know", bold=True)],
    rows, [1.6 * inch, 1.35 * inch, CW - 2.95 * inch]))
flow.append(k.cite(
    "Contrast this with the building permit itself, which exists only where a "
    "building department certified for residential buildings has jurisdiction "
    "over your parcel. OH.1 explains that test; OH.4 shows you how to run it "
    "against your own address."))

# ---------------------------------------------------------------- editions
flow += k.h2_tight("THE CODE EDITIONS ACTUALLY IN FORCE", reserve=1.8)
flow.append(k.body(
    "The Residential Code of Ohio is not a book you buy — it is a set of "
    "rules in the Ohio Administrative Code, one rule per code chapter, free to "
    "read at codes.ohio.gov. Its own opening section names both its title and "
    "its model-code base:"))
flow.append(k.callout(
    f"OAC {k.rule('4101:8-1-01')}, RCO section 101.1", [
        Paragraph("\"Chapters 4101:8-1 to 4101:8-25, 4101:8-29, 4101:8-34, and "
                  "4101:8-44 of the Administrative Code are designated as the "
                  "<b>'Residential Code of Ohio for One-, Two-, and "
                  "Three-Family Dwellings'</b> for which the designation 'RCO' "
                  "may be substituted. <b>The 2018 edition of the "
                  "'International Residential Code', first printing, Chapters "
                  "2 through 24, 29, and 44</b> as published by the "
                  "'International Code Council, Inc.' is used as the basis of "
                  "this document as is incorporated fully except as modified "
                  "in italic herein.\"", S["body"]),
    ]))
rows = [
    [k.cellp("<b>Residential Code of Ohio</b><br/>1-, 2- and 3-family "
             "dwellings"),
     k.cellp("2018 International Residential Code with Ohio amendments"),
     k.cellp(f"Effective 1{NB}July 2019"),
     k.cellp(f"OAC {k.rule('4101:8')}")],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("<b>2023 National Electrical Code</b> (NFPA 70), incorporated "
             "whole and then amended — see the next section"),
     k.cellp(f"Effective <b>15{NB}April 2024</b>"),
     k.cellp(f"OAC {k.rule('4101:8-34-01')}<br/>OAC {k.rule('4101:8-44-01')}")],
    [k.cellp("<b>Energy</b>"),
     k.cellp("2018 International Energy Conservation Code — <b>not</b> moved "
             "by the 2024 amendment"),
     k.cellp(f"Effective 1{NB}July 2019"),
     k.cellp(f"OAC {k.rule('4101:8-11-01')}<br/>OAC {k.rule('4101:8-44-01')}")],
    [k.cellp("<b>Foundations</b>"),
     k.cellp("RCO Chapter 4, amended separately from the rest of the code"),
     k.cellp(f"Effective 1{NB}March 2024"),
     k.cellp(f"OAC {k.rule('4101:8-4-01')}")],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp("<b>The Ohio Plumbing Code</b>, incorporated into the RCO — "
             "currently on the 2021 International Plumbing Code, a "
             "<i>newer</i> cycle than the rest of your house code"),
     k.cellp(f"OPC effective 15{NB}October 2025"),
     k.cellp(f"RCO 2501.1<br/>OAC {k.rule('4101:3')}")],
]
flow.append(k.ref_table(
    "What governs your house, and since when",
    [k.cellp("Subject", bold=True), k.cellp("Standard", bold=True),
     k.cellp("In force", bold=True), k.cellp("Rule", bold=True)],
    rows, [1.25 * inch, CW - 4.2 * inch, 1.05 * inch, 1.9 * inch]))
flow.append(k.cite(
    f"Note the shape of that table: Ohio advanced its electrical standard by "
    f"six years in April 2024 and left the energy standard where it was. Both "
    f"editions are fixed in the same rule, OAC {k.rule('4101:8-44-01')}, on "
    f"pages 29 and 31 of the filed PDF. The RCO also has no chapters 26 to 28, "
    f"30 to 33, or 35 to 43: Ohio collapsed the model code's ten electrical "
    f"chapters into a single Chapter{NB}34 and kept only two of its plumbing "
    f"chapters."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Why almost every source still tells you 2017 — and how to check us", [
        Paragraph("The Board of Building Standards publishes each rule as a "
                  "PDF of the <i>amendment</i>: deleted text is struck "
                  "through, new text is underlined, on the same line. In the "
                  "referenced-standards table the National Electrical Code "
                  "line therefore reads, as printed, "
                  "<b>70—<s>17</s><u>23</u></b>.", S["body"]),
        Paragraph("Copy that line, or run any text extractor over the page, "
                  "and the strikethrough disappears. What comes out is "
                  "\"70—1723\" — which a careful writer then reads as 2017, "
                  "because 17 comes first. <b>That single formatting artifact "
                  "is why the 2017 answer is still circulating two years after "
                  "it stopped being true.</b>", S["body"]),
        Paragraph("<b>Check it yourself in two minutes.</b> Open "
                  "codes.ohio.gov, go to Ohio Administrative Code rule "
                  "4101:8-44-01, click View Rule Text, and look at page 31 "
                  "with your eyes rather than your clipboard. The 17 is "
                  "crossed out. Then look at page 29, where IECC—18 sits with "
                  "no strikethrough at all — which is how you know the energy "
                  "edition genuinely did not move.", S["body"]),
        Paragraph("<b>The practical consequence, and it is not academic:</b> "
                  "your permit is reviewed against the edition in force when "
                  "your plans are approved. If a supplier, an electrician or a "
                  "guide is working from the 2017 book, the surge-protection, "
                  "GFCI and receptacle rules they quote you are the wrong "
                  "ones. Ask your plan reviewer which edition, and write the "
                  "answer down.", S["body"]),
    ]))

# ---------------------------------------------------------------- NEC amends
flow += k.h2_tight("WHAT OHIO CHANGED IN THE 2023 NEC", reserve=1.8)
flow.append(k.body(
    "Ohio does not rewrite the electrical code — it adopts NFPA 70 whole and "
    "then applies a short list of amendments. Several of them save real money "
    "and are routinely missed by electricians working from the national book."))
rows = [
    [k.cellp("<b>Whole-house surge protection is not mandatory</b>"),
     k.cellp("The 2023 NEC requires a surge-protective device on dwelling "
             "services. Ohio rewrote all three sections to read \"<b>Where "
             "provided as part of</b>\" the feeder or service, an SPD is to be "
             "installed in accordance with this section — turning a mandate "
             "into a conditional"),
     k.cellp("215.18(A)<br/>225.42(A)<br/>230.67(A)")],
    [k.cellp("<b>Outdoor HVAC equipment is exempt from GFCI</b>"),
     k.cellp("Ohio's rewritten outdoor-outlet section carries "
             "\"<b>Exception No. 2: GFCI protection is not required for "
             "listed HVAC equipment</b>\" — the amendment that has caused the "
             "most nuisance-tripping grief in states that did not make it"),
     k.cellp("210.8(F)")],
    [k.cellp("<b>No receptacle required at the service equipment</b>"),
     k.cellp("\"<b>Exception No. 1: The receptacle outlet shall not be "
             "required to be installed in one-, two-, or three-family "
             "dwellings.</b>\""),
     k.cellp("210.64")],
    [k.cellp("<b>A sump pump and a garage-door opener get relief</b>"),
     k.cellp("A single receptacle serving a sump pump needs no GFCI where a "
             "GFCI-protected duplex sits within six&#160;feet of it; and the "
             "ceiling-mounted single receptacle serving a garage door opener "
             "is excepted"),
     k.cellp("210.8(A)(5)<br/>210.8(A)(2)")],
    [k.cellp("<b>Kitchen countertop circuits need no AFCI</b>"),
     k.cellp("\"<b>Exception No. 2: Branch circuits supplying receptacle "
             "outlets installed to serve only the kitchen countertop surfaces "
             "shall be permitted to be installed without arc-fault circuit "
             "interrupter protection.</b>\""),
     k.cellp("210.12(A)")],
    [k.cellp("<b>A three-family dwelling is treated as multi-family</b>"),
     k.cellp("\"Any reference in NFPA 70 to 'one- and two-family dwellings' "
             "will include 'one-, two- and three-family dwellings.'\" Where "
             "the NEC names a one- or two-family dwelling specifically, a "
             "three-family dwelling is regulated as multi-family"),
     k.cellp("RCO 3401.1")],
]
flow.append(k.ref_table(
    f"Ohio's amendments to NFPA 70, from OAC {k.rule('4101:8-34-01')}",
    [k.cellp("What Ohio changed", bold=True),
     k.cellp("What the amendment says", bold=True),
     k.cellp("NEC section", bold=True)],
    rows, [1.55 * inch, CW - 2.65 * inch, 1.1 * inch]))
flow += k.check_table(
    "Confirm these with your electrician before rough-in",
    [
        ("I confirmed which NEC edition my permit is reviewed against.",
         [("Answer", 0.6), ("Date", 0.4)]),
        "My electrician knows Ohio does not mandate a whole-house surge "
        "protective device — and I have decided whether I want one anyway.",
        "My outdoor condenser circuit is planned around Ohio's listed-HVAC "
        "GFCI exception rather than the national rule.",
        ("Panel and service location confirmed with the utility.",
         [("Utility", 0.6), ("Date", 0.4)]),
    ])

# ---------------------------------------------------------------- RCO amends
flow += k.h2_tight("WHAT OHIO CHANGED IN THE RESIDENTIAL CODE ITSELF",
                   reserve=1.8)
flow.append(k.body(
    "The RCO is the 2018 IRC \"except as modified in italic herein\", and "
    "several of Ohio's modifications matter more to an owner-builder than "
    "anything in the model code. Four of them are money; two of them are "
    "things a national guide will tell you wrongly."))
rows = [
    [k.cellp("<b>Fire sprinklers are not required</b>"),
     k.cellp("Ohio replaced the model code's mandate with an explicit "
             "non-requirement: \"<b>An automatic residential fire sprinkler "
             "system is not required to be installed in one-, two-, or "
             "three-family dwellings.</b>\" Section 313.3 still governs a "
             "system you choose to install"),
     k.cellp("RCO 313.2")],
    [k.cellp("<b>There is no statewide frost depth</b>"),
     k.cellp("The climatic design table's frost-line cell is <b>blank by "
             "design</b> — footnote b: \"The jurisdiction shall fill in the "
             "frost line depth column with the minimum depth of footing below "
             "finish grade.\" Ground snow load and seismic category are blank "
             "for the same reason. <b>The only statewide floor is 12 inches "
             "below undisturbed ground</b>"),
     k.cellp("RCO Table<br/>301.2(1)<br/>RCO 403.1.4")],
    [k.cellp("<b>Freestanding outbuildings lost their frost exemption</b>"),
     k.cellp("The March 2024 Foundations amendment <b>deleted</b> the model "
             "code's exemptions for freestanding accessory structures of 600 "
             "and 400 square feet. Only one exception survives: decks not "
             "supported by a dwelling. <b>Your pole barn needs frost-depth "
             "footings in Ohio</b>"),
     k.cellp("RCO 403.1.4.1")],
    [k.cellp("<b>The code has no radon requirement at all</b>"),
     k.cellp("Not \"locally adopted\" — <b>absent</b>. Ohio adopted IRC "
             "Chapters 2 through 24, 29 and 44 and <b>no appendices</b>, and "
             "radon control is Appendix F. A local jurisdiction could add a "
             "rule, but only through the non-conflict process in OH.3"),
     k.cellp("RCO 101.1")],
    [k.cellp("<b>Stairs may be steeper than the model code</b>"),
     k.cellp("Ohio permits a riser of <b>up to 8¼&#160;inches</b> and a tread "
             "of <b>as little as 9&#160;inches</b>, against the model code's "
             "7¾ and 10. That shortens the stair run and can save real floor "
             "area in a small house"),
     k.cellp("RCO 311.7.5.1<br/>RCO 311.7.5.2")],
    [k.cellp("<b>Smoke alarms need both technologies</b>"),
     k.cellp("\"<b>On each level within each dwelling unit smoke alarms "
             "utilizing photoelectric and ionization technologies shall be "
             "installed.</b> Separate or dual-sensing smoke alarms may be "
             "used.\" A single-technology alarm on a level does not comply"),
     k.cellp("RCO 314.1.2")],
    [k.cellp("<b>A screened porch can skip the guard</b>"),
     k.cellp("Guards are required above 30&#160;inches, and \"insect screening "
             "shall not be considered as a guard\" — but Ohio adds an "
             "exception for a protective bar 34 to 38&#160;inches above the "
             "deck on the interior side of the screening, resisting "
             "50&#160;pounds per lineal foot"),
     k.cellp("RCO 312.1.1")],
]
flow.append(k.ref_table(
    "Ohio's own amendments, and what they cost or save you",
    [k.cellp("What Ohio did", bold=True),
     k.cellp("What the code says", bold=True), k.cellp("Section", bold=True)],
    rows, [1.55 * inch, CW - 2.9 * inch, 1.35 * inch]))
flow.append(k.cite(
    f"<b>The frost-depth point deserves emphasis because guides get it wrong "
    f"in both directions.</b> Ohio publishes no frost number, so any source "
    f"quoting you \"32 to 42 inches\" as the Ohio code is quoting something "
    f"that is not in the code. What Ohio <i>does</i> fix statewide in the same "
    f"table is a 115{NB}mph ultimate design wind speed, severe weathering, and "
    f"a requirement for ice barrier underlayment everywhere — footnote h "
    f"records that \"all jurisdictions in Ohio have a history of local damage "
    f"from the effects of ice damming.\" <b>Get your frost depth from your "
    f"building department in writing.</b> Where none is certified, there is no "
    f"published figure at all and you should design to documented local "
    f"practice."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Your plumbing code is newer than your building code — and that is a "
    "recent change", [
        Paragraph("The RCO does not contain the model code's plumbing "
                  "chapters. Section 2501.1 replaces all of them with a "
                  "pointer: \"The provisions of the <b>'Ohio Plumbing Code' as "
                  "referenced in Chapter 44 shall be incorporated herein</b>… "
                  "and shall govern the installation, testing and operation of "
                  "the plumbing in buildings within the scope of this code\", "
                  "with a single Ohio change to shower pan lining at "
                  "2501.1.1.", S["body"]),
        Paragraph("<b>The April 2024 amendment cut the edition loose.</b> The "
                  "referenced-codes table used to pin residential plumbing to "
                  "the 2017 Ohio Plumbing Code; that pin is struck through in "
                  "the filed rule, leaving a general pointer to the plumbing "
                  "chapters as they stand. <b>The Ohio Plumbing Code now in "
                  f"effect took effect 15{NB}October 2025 and is based on "
                  f"the 2021 International Plumbing Code.</b> So your plumbing "
                  f"is reviewed against a 2021 model code while the rest of "
                  f"your house is reviewed against a 2018 one.", S["body"]),
        Paragraph("<b>And it is very often inspected by a different office.</b> "
                  "In the Board of Building Standards' own dataset, the "
                  "plumbing entity named for a residential-certified "
                  "jurisdiction is a <b>county health district in roughly "
                  "two thirds of cases</b> rather than the building "
                  "department — a separate agency, a separate submission and a "
                  "separate fee. Because plumbing enforcement flows from R.C. "
                  f"{sec('3781.03(C)')} and not from building-department "
                  f"certification, a health district can require a plumbing "
                  f"inspection in a county with no building department at all. "
                  f"Confirm both tracks before you start.", S["body"]),
    ]))

flow.append(Spacer(1, 4))
flow.append(k.body(
    f"<b>One more thing worth knowing before you pay an energy consultant.</b> "
    f"Ohio's energy chapter offers <b>five</b> compliance paths, not the usual "
    f"two — the prescriptive route, the simulated performance route, the "
    f"Energy Rating Index route, the International Energy Conservation Code "
    f"itself, and <b>an Ohio-specific option written by the Ohio Home "
    f"Builders Association</b> at RCO section 1112 "
    f"(OAC {k.rule('4101:8-11-01')} 1101.2.1). For a modest owner-built house "
    f"the last of those is frequently the cheapest way to demonstrate "
    f"compliance. Ask your reviewer which paths they see most often. Ohio's "
    f"climate zones are set by a statewide county table: nine southern "
    f"counties — Adams, Brown, Clermont, Gallia, Hamilton, Lawrence, Pike, "
    f"Scioto and Washington — are Zone{NB}4A, and the other seventy-nine are "
    f"Zone{NB}5A."))

# ---------------------------------------------------------------- septic
flow += k.h2_tight("THE SEWAGE SYSTEM PACKAGE, IN ORDER", reserve=1.6)
flow.append(k.body(
    "On a rural Ohio build this is the longest pole and the one that decides "
    "where the house physically sits. It runs entirely through your local "
    "board of health under statewide rules, and it is completely independent "
    "of whether anybody permits your building."))
flow += k.check_table(
    "The sewage permit sequence",
    [
        ("<b>Soil evaluation.</b> You may not do this yourself. It must be "
         "done by a soil scientist certified by the Soil Science Society of "
         "America, an equivalently registered soil professional, or a "
         "registered sanitarian on the health district's own staff "
         "(§&#160;3701-29-07(A)). You may hire your own rather than use the "
         "district's.", [("Evaluator", 0.6), ("Date", 0.4)]),
        ("<b>Design.</b> Ohio requires no professional engineer and creates no "
         "registered-designer credential — the rule's test is a functional one "
         "(§&#160;3701-29-10(A)). The designer must visit the site and stake or "
         "flag the absorption area.", [("Designer", 0.6), ("Date", 0.4)]),
        "<b>The site drawing must show the isolation distances met by BOTH "
         "the system and the replacement area</b> (§&#160;3701-29-10(C)(9)). This "
         "is the drawing the health district actually reviews.",
        ("<b>Installation permit</b> from the board of health, before any "
         "work.", [("Permit no.", 0.6), ("Date", 0.4)]),
        "<b>If I am installing it myself:</b> I understand I must first "
        "register as an installer with my board of health. There is no blanket "
        "homeowner exemption — see the box below.",
        ("<b>Installer's as-built drawing</b> received and filed "
         "(§&#160;3701-29-09(F)). Any change to component locations needs prior "
         "approval and may not violate an isolation distance.",
         [("Date", 1.0)]),
        ("<b>Operation permit</b> issued. Term is set by your board of health "
         "and may not exceed ten&#160;years (§&#160;3701-29-09(I)(4)) — it is not "
         "an annual permit by state rule.",
         [("Term", 0.5), ("Expires", 0.5)]),
        "I know the board of health inspects the completed system again "
        "within twelve&#160;months of approving the installation "
        "(§&#160;3701-29-09(H)).",
    ])
flow.append(k.callout_long(
    "\"I'll install my own septic\" — read the sentence first", [
        Paragraph("Ohio's rule is one sentence and it is not the exemption "
                  f"people expect. OAC {k.rule('3701-29-03(H)')}: "
                  f"\"<b>When the registered installer performs the duties of "
                  f"an installer on only the registrant's personal residence, "
                  f"the board of health may waive paragraphs (C)(1), (C)(4), "
                  f"and (C)(6) of this rule.</b>\"", S["body"]),
        Paragraph("The subject of that sentence is \"<b>the registered "
                  "installer</b>.\" You must become one first — registration "
                  "is with your board of health, per health district, expiring "
                  "at the end of each calendar year. What the district "
                  "<i>may</i> waive is the registration fee, the $500,000 "
                  "general liability insurance, and the surety bond. What is "
                  "not on the waiver list, and therefore still applies: proof "
                  "of compliance with the Department of Health's testing "
                  "requirements, any system-specific training the product "
                  "approval demands, and the continuing-education requirement "
                  "on renewal.", S["body"]),
        Paragraph("<b>And note the verb is \"may,\" not \"shall.\"</b> Every "
                  "one of those waivers is discretionary. Ask your district "
                  "what it actually does before you build a schedule or a "
                  "budget around installing it yourself.", S["body"]),
    ]))

flow.append(Spacer(1, 4))
flow.append(k.body(
    "<b>Two siting rules will shape your site plan more than anything else in "
    "this kit.</b>"))
rows = [
    [k.cellp("<b>The replacement area</b>"),
     k.cellp(f"Every new system needs a <i>second</i> fully compliant area "
             f"held in reserve: \"sufficient suitable area shall be available "
             f"to accommodate a STS <b>including a designated area for "
             f"complete relocation and replacement</b>\", and every isolation "
             f"distance \"shall be met for the STS <b>and designated "
             f"replacement area</b>\". It must be identified at design, staked, "
             f"and protected from construction damage — and a board of health "
             f"<b>may not waive it</b> when reviewing new lots")],
    [k.cellp("<b>No statewide minimum lot size</b>"),
     k.cellp("Ohio's sewage rules set none. The functional constraint is "
             "whether two compliant absorption areas plus every setback fit on "
             "the parcel. Your <i>zoning</i> and your health district may "
             "impose an acreage minimum of their own, and often do")],
]
flow.append(k.ref_table(
    f"OAC {k.rule('3701-29-06(G)')} — the two rules that size your lot",
    [k.cellp("Rule", bold=True), k.cellp("What it requires", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch]))
flow.append(k.cite(
    "Ohio's septic setbacks are unusual in shape: rather than a long "
    "row-by-row table, the whole statewide scheme is four short paragraphs "
    f"that group many features under two numbers. All components of a system "
    f"keep <b>10{NB}feet</b> from a utility line, roadway, driveway or other "
    f"hardscape, property line or right-of-way, properly sealed well, building "
    f"or other structure, recorded easement, intermittent stream, swale, "
    f"horizontal geothermal loop, irrigation line or gray water system. The "
    f"absorption field keeps <b>50{NB}feet</b> from an impoundment, lake, "
    f"river, wetland, perennial stream, and road or stream cut-bank; and all "
    f"components keep <b>50{NB}feet</b> from any water supply source and from "
    f"a vertical geothermal loop. OAC {k.rule('3701-29-06(G)(3)(a)')} to (c). "
    f"<b>Every number is a statewide floor</b> — your board of health may "
    f"require more (OAC {k.rule('3701-29-22')})."))

# ---------------------------------------------------------------- well
flow += k.h2_tight("THE PRIVATE WATER SYSTEM PACKAGE", reserve=1.6)
flow.append(k.body(
    f"A well, spring, cistern or pond serving the house is a \"private water "
    f"system\" and is permitted by the same board of health, under OAC "
    f"{k.rule('3701-28')}. <b>The permit must exist before any work starts</b> "
    f"— \"no work shall commence until a valid permit has been issued and "
    f"approved\" — and the emergency exception is expressly unavailable on raw "
    f"land where no structure yet exists."))
flow += k.check_table(
    "The private water sequence",
    [
        ("<b>Application, including a site plan.</b> The rule lists what it "
         "must show: distances from roadways, rights-of-way, buildings, "
         "driveways, sewage systems, sewers, existing and sealed wells, oil "
         "and gas wells, fuel and chemical tanks, streams, lakes, ponds, "
         "ditches, leaching pits, privies, manure ponds, lagoons and piles, "
         "lot lines and easements (§&#160;3701-28-03(B)).",
         [("Date filed", 1.0)]),
        ("<b>Pre-construction site review with the health district</b> to "
         "confirm the isolation distances are met — mandatory, and before "
         "construction (§&#160;3701-28-03(A)(3)(a)).", [("Date", 1.0)]),
        "I know the review clock is ten business days, or fifteen where plans "
        "are required (§&#160;3701-28-03(A)(3)).",
        "<b>If I am drilling it myself:</b> I must register with the Ohio "
        "Department of Health as a private water systems contractor and post a "
        "surety bond. Only the liability insurance is waived. See the box.",
        ("<b>Water sample</b> — the application fee includes at least one "
         "(§&#160;3701-28-03(A)(1)).", [("Result", 0.6), ("Date", 0.4)]),
        ("Well log filed by the driller with the Ohio Department of Natural "
         "Resources — separate from the health district permit. Do not "
         "conflate them.", [("Date", 1.0)]),
    ])
flow.append(k.callout_long(
    "Drilling your own well is allowed — and the fine print is expensive", [
        Paragraph("Ohio splits owner work into two paths and they are not "
                  "equally easy. If you are building the pump, pressure tank, "
                  "distribution piping, a treatment system, a spring, a pond "
                  "or a hauled-water tank — anything <i>except</i> drilling — "
                  f"you \"shall obtain a registration to perform work, but are "
                  f"<b>exempt from the bonding and business liability "
                  f"insurance requirements</b>\" (OAC "
                  f"{k.rule('3701-28-18(A)(3)')}). That is a light "
                  f"requirement.", S["body"]),
        Paragraph("Drilling is carved out of that relief. An owner \"drilling "
                  "a well for construction or alteration purposes shall obtain "
                  "a registration to perform work, but are <b>exempt from the "
                  "business liability insurance requirements</b>\" — and "
                  "nothing else (OAC "
                  f"{k.rule('3701-28-18(A)(4)')}). <b>The surety bond still "
                  f"applies to an owner-driller.</b> A new registrant also "
                  f"receives a mandatory Department of Health field assessment "
                  f"during construction.", S["body"]),
        Paragraph("<b>Read the two paragraphs side by side before you decide.</b> "
                  "For most owner-builders, hiring a registered driller is "
                  "faster and cheaper than becoming one; doing your own pump "
                  "and distribution work is genuinely straightforward. Confirm "
                  "the current fee and bond figures with the Department of "
                  "Health — they are set by rule and they change.", S["body"]),
    ]))
flow.append(k.cite(
    f"Well setbacks worth knowing at the site-planning stage, from OAC "
    f"{k.rule('3701-28-07')}: a well, spring box or pond may not sit within "
    f"<b>10{NB}feet</b> of a building foundation, or closer than "
    f"<b>5{NB}feet</b> to the edge of a deck, porch or extended slab that is "
    f"not part of the foundation (D); a water source keeps <b>10{NB}feet</b> "
    f"from an established road right-of-way, or <b>25{NB}feet</b> from the "
    f"edge of the driving surface where none is designated (G); and "
    f"<b>5{NB}feet</b> from a private driveway or parking lot (H). Table 1 to "
    f"paragraph (J) then carries a full thirty-four-row list — including "
    f"<b>10{NB}feet</b> to lot lines and easements, <b>50{NB}feet</b> to any "
    f"component of a sewage or gray water system, and <b>100{NB}feet</b> to an "
    f"unabandoned leaching pit or drywell. OH.5 tells you where to read it."))

# ---------------------------------------------------------------- stormwater
flow += k.h2_tight("STORMWATER — THE ONE-ACRE TEST AND ITS TRAP", reserve=1.6)
flow.append(k.body(
    "Most single-house sites never reach the threshold. The trap is the second "
    "half of the sentence, which sweeps in a lot of owner-builders who "
    "correctly measured their own lot."))
flow.append(k.callout(
    "Ohio EPA construction stormwater general permit OHC000006", [
        Paragraph("Coverage is required for \"excavating, grubbing and/or "
                  "filling activities that disturb <b>one or more acres</b>\", "
                  "and construction disturbing one or more acres <b>or</b> "
                  "less than an acre where the work \"<b>is part of a larger "
                  "common plan of development</b>\" that will ultimately "
                  "disturb one or more acres is eligible for coverage under "
                  "the permit.", S["body"]),
        Paragraph("<b>If your lot is in a subdivision, the common plan is the "
                  "subdivision — not your lot.</b> A half-acre disturbance on "
                  "a single lot inside a twelve-acre development is inside the "
                  "permit. Ask the developer whether their coverage extends to "
                  "individual lot construction, and get the answer in writing.",
                  S["body"]),
    ]))
flow.append(k.cite(
    f"Permit OHC000006 was effective 23{NB}April 2023 and expires "
    f"22{NB}April 2028, so a renewal falls inside the life of many builds "
    f"— check the current permit number before filing. Coverage is obtained by "
    f"filing a Notice of Intent with Ohio EPA's Division of Surface Water, and "
    f"the fee is tiered by disturbed acreage. Two watersheds have their own "
    f"separate construction stormwater permits rather than the general one: "
    f"<b>Big Darby Creek</b> and the <b>Olentangy River</b>. If you are "
    f"building in central Ohio, check which permit applies to you."))

# ---------------------------------------------------------------- if exists
flow += k.h2_tight("IF A BUILDING DEPARTMENT DOES HAVE JURISDICTION",
                   reserve=1.8)
flow.append(k.body(
    "Then Ohio gives you five statutory protections that most owner-builders "
    "never learn they have. All five are in one section, R.C. 3791.04, and all "
    "five are worth knowing before your first plan review rather than after."))
rows = [
    [k.cellp("<b>No seal required</b>"),
     k.cellp("\"No seal is required for any plans, drawings, specifications, "
             "or data submitted for approval for <b>any residential "
             "buildings</b>\". You do not need an architect or engineer to "
             "stamp a house plan in Ohio"),
     k.cellp(sec("3791.04(A)(2)(b)"))],
    [k.cellp("<b>Silence past 30&#160;days is a denial you can appeal</b>"),
     k.cellp("Plan approval is defined as a \"license\", and \"the failure to "
             "approve plans or specifications as submitted… "
             "<b>within thirty&#160;days</b>\" is \"an adjudication order "
             "denying the issuance of a "
             "license\" requiring a hearing. A denial \"shall specify the "
             "reasons\""),
     k.cellp(sec("3791.04(E)"))],
    [k.cellp("<b>Approved plans are conclusively presumed to comply</b>"),
     k.cellp("Once approved, the structure \"and every particular represented "
             "by and disclosed in those plans shall, <b>in the absence of "
             "fraud or a serious safety or sanitation hazard, be conclusively "
             "presumed to comply</b>\" — and you are locked to \"any rule in "
             "effect at the time of approval\""),
     k.cellp(sec("3791.04(D)"))],
    [k.cellp("<b>Conditional approval to keep building</b>"),
     k.cellp("If the department objects to part of the plans you \"may request "
             "the agency to issue conditional approval to proceed with "
             "construction <b>up to the point of the objection</b>\" — "
             "available where the objection is a conflicting interpretation "
             "rather than a specific technical requirement"),
     k.cellp(sec("3791.04(G)"))],
    [k.cellp("<b>Foundation-only permits are authorized</b>"),
     k.cellp("Rules may provide for approving \"the plans for construction of "
             "a <b>foundation or any other part</b> of a building… before the "
             "complete plans… are submitted\""),
     k.cellp(sec("3791.04(D)"))],
]
flow.append(k.ref_table(
    "Five things R.C. 3791.04 gives you",
    [k.cellp("Protection", bold=True), k.cellp("What the statute says",
                                               bold=True),
     k.cellp("Cite", bold=True)],
    # The Cite column has to fit "§ 3791.04(A)(2)(b)", which measures 87.9pt at
    # the cell style's 9.5pt. 1.15in leaves 72.8pt inside the 5pt side padding
    # and broke the citation after "(2". 1.45in leaves 94.4pt.
    rows, [1.5 * inch, CW - 2.95 * inch, 1.45 * inch]))
flow.append(k.callout(
    "The deadline that is yours to miss", [
        Paragraph(f"Plan approval \"is invalid if construction… <b>has not "
                  f"commenced within twelve&#160;months</b> of the approval\", and "
                  f"if work \"is delayed or suspended for <b>more than "
                  f"six&#160;months</b>\" the approval is likewise invalid "
                  f"({sec('3791.04(C)')}). One twelve-month extension and two "
                  f"six-month extensions are available — but each must be "
                  f"requested <b>at least ten&#160;days before the approval "
                  f"expires</b>. That ten-day rule is statutory, it is easy to "
                  f"miss on a slow self-build, and missing it means "
                  f"resubmitting the whole plan set.", S["body"]),
    ]))

# ---------------------------------------------------------------- record
flow += k.h2_tight("PERMIT RECORD — FILL THIS IN AS EACH ONE ISSUES",
                   reserve=1.6)
flow += k.check_table(
    "Every approval this build needed, and what it cost",
    [
        ("Building plan approval, if one exists here",
         [("No.", 0.4), ("Fee", 0.3), ("Date", 0.3)]),
        ("Zoning certificate", [("No.", 0.4), ("Fee", 0.3), ("Date", 0.3)]),
        ("Sewage treatment system installation permit",
         [("No.", 0.4), ("Fee", 0.3), ("Date", 0.3)]),
        ("Sewage treatment system operation permit, and its term",
         [("Term", 0.5), ("Expires", 0.5)]),
        ("Private water system permit",
         [("No.", 0.4), ("Fee", 0.3), ("Date", 0.3)]),
        ("Water sample result", [("Result", 0.6), ("Date", 0.4)]),
        ("Driveway or access permit",
         [("Office", 0.4), ("No.", 0.3), ("Date", 0.3)]),
        ("Building sewer / sanitary tap, if on public sewer",
         [("No.", 0.4), ("Fee", 0.3), ("Date", 0.3)]),
        ("Floodplain development permit, if applicable",
         [("No.", 0.5), ("Date", 0.5)]),
        ("Ohio EPA stormwater Notice of Intent, if one acre or a common plan",
         [("No.", 0.5), ("Date", 0.5)]),
        ("Ohio 811 locate ticket", [("No.", 0.5), ("Date", 0.5)]),
        ("Electric service application", [("Utility", 0.6), ("Date", 0.4)]),
    ],
    notes_header="Notes", date_w=0.8, notes_w=1.4)
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "oh-permit-kit",
                       "OH.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
