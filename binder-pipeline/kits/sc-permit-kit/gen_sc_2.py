#!/usr/bin/env python3
"""SC.2 Permit Application Checklist.

Built around what South Carolina actually enforces, which is not what the
Building Codes Council's own website hands you. The Council's Codes page links
a PDF named "Residential Code" that is a scan of State Register Vol. 43,
Issue 5 (24 May 2019), Document No. 4868 — the 2018 IRC modification summary.
The text in force is Article 12 of Chapter 8 of the Code of Regulations, the
2021 IRC modification summary, added by SCSR 46-5 Doc. No. 5074 effective
27 May 2022. Section 6-9-55 is why: any provision affecting one- and two-family
dwellings has to be promulgated as a regulation, so the regulation IS the code
amendment, not a summary of one.

The other structural fact this document carries: South Carolina's residential
energy standard is not in the building code at all. R.8-1230 says the Council
"does not adopt IRC Chapter 11," and § 6-10-30 names the 2009 IECC in statute.
The Council cannot move it; only the General Assembly can, and it last did in
2012.
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
NB = k.NB
sec = k.sec

FORM_ID = "SC.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Before You File"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "The code editions actually in force, the amendments that "
                 "change what you buy, and what to gather before you file.")
flow.append(k.disclaimer())

# --------------------------------------------------------- what is in force
flow += k.h2_tight("WHAT IS ACTUALLY IN FORCE", reserve=2.2)
flow.append(k.body(
    "South Carolina adopts the model codes statewide and amends them in one "
    f"place. Section&#160;6-9-55(A) requires the Building Codes Council "
    "to “promulgate as regulations… any provision of or amendment to any "
    "building code that would affect construction requirements for one-family "
    "or two-family dwellings” — and says that until it does, the provision "
    "“shall not be enforced.” So the amendments are not a handout. They are "
    "<b>Articles 8 through 14 of Chapter 8 of the S.C. Code of "
    "Regulations</b>, and each article opens by naming its edition."))
rows = [
    [k.cellp("Residential"), k.cellp("<b>2021</b> International Residential "
                                     "Code, as modified"),
     k.cellp("Reg. Art. 12, R.8-1200")],
    [k.cellp("Building"), k.cellp("<b>2021</b> International Building Code, "
                                  "as modified — non-residential"),
     k.cellp("Reg. Art. 8, R.8-800")],
    [k.cellp("Electrical"), k.cellp("<b>2020</b> National Electrical Code, as "
                                    "modified. Note the year: it does "
                                    "<i>not</i> track the 2021 suite."),
     k.cellp("Reg. Art. 11, R.8-1100")],
    [k.cellp("Plumbing"), k.cellp("<b>2021</b> International Plumbing Code, "
                                  "as modified"),
     k.cellp("Reg. Art. 14, R.8-1400")],
    [k.cellp("Mechanical"), k.cellp("<b>2021</b> International Mechanical "
                                    "Code, as modified"),
     k.cellp("Reg. Art. 13, R.8-1300")],
    [k.cellp("Fuel gas"), k.cellp("<b>2021</b> International Fuel Gas Code, "
                                  "as modified"),
     k.cellp("Reg. Art. 10")],
    [k.cellp("Fire"), k.cellp("<b>2021</b> International Fire Code, as "
                              "modified"),
     k.cellp("Reg. Art. 9")],
    [k.cellp("<b>Energy</b>"),
     k.cellp("<b>2009 IECC</b> — set by statute, not by the Council. The "
             "Council “does not adopt IRC Chapter 11.” See below."),
     k.cellp(f"{sec('6-10-30')}; R.8-1230")],
]
flow.append(k.ref_table(
    "South Carolina code editions, from the regulation that carries them",
    [k.cellp("Discipline", bold=True), k.cellp("Edition in force", bold=True),
     k.cellp("Where it says so", bold=True)],
    rows, [1.05 * inch, CW - 2.75 * inch, 1.70 * inch]))
flow.append(k.cite(
    "Each article states it the same way — R.8-1200: “This code is identical "
    "to the 2021 Edition of the International Residential Code except for the "
    "following modifications.” Read them free at "
    "<b>scstatehouse.gov/coderegs/</b> — Chapter 8 is one PDF. Statewide "
    "modifications “shall be mandatory for all jurisdictions in the state” "
    "(R.8-240(K)), and local governments “are prohibited from writing or "
    "publishing any other building codes in part or in whole” (R.8-236(C))."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "Do not use the PDF on the Council's own Codes page", [
        Paragraph("The Building Codes Council's website has a Codes menu with "
                  "a link named <i>Residential Code</i>. As of September 2026 "
                  "that link serves a scanned copy of <i>South Carolina State "
                  "Register</i> Vol. 43, Issue 5, dated 24&#160;May&#160;2019 "
                  "— Document No.&#160;4868, headed “2018 International "
                  "Residential Code Modification Summary.” It is a code "
                  "edition and several amendment cycles out of date, and "
                  "because it is a scan you cannot even search it.", S["body"]),
        Paragraph("The current text is Article 12 of Chapter 8 of the Code of "
                  "Regulations, which carries the 2021 IRC modifications and "
                  "was last amended effective 27&#160;May&#160;2022. If a "
                  "plan reviewer quotes you a modification, check it there.",
                  S["body"]),
    ]))

flow.append(k.body(
    f"Two dates decide which edition your house is built to. "
    f"Section{NB}6-9-130(A) fixes it: “Buildings must be inspected in "
    f"accordance with the codes in effect for the locality <b>on the date of "
    f"the issuance of the original building permit</b>,” falling back to the "
    f"date the completed application was submitted if no issuance date can be "
    f"found. The regulation says the same from the other side: work “for "
    f"which a completed building permit application has been approved prior "
    f"to the implementation date… must be inspected under the building codes "
    f"in effect at the time the original building permit was issued” "
    f"(R.8-236(B)). <b>A new edition landing in the middle of your build does "
    f"not move your job.</b> Keep the dated permit."))
flow.append(k.body(
    "The current suite has a date on it. The Building Codes Council's own "
    "adoption notice records that <b>on 6&#160;October&#160;2021</b> it "
    "“adopted the latest editions of the mandatory codes and appendices with "
    "modifications, as referenced in S.C. Code Ann. §&#160;6-9-50… to be "
    "enforced by all municipalities and counties in South Carolina,” and that "
    "“The Council established the <b>implementation date for local "
    "jurisdictions as January&#160;1,&#160;2023</b>.” The same notice lists "
    "the editions exactly as the regulation does, including the 2020 NEC and "
    "the 2009 IECC under the Energy Standard Act — and adds a warning worth "
    "keeping: “Only the modifications approved and listed on the Council's "
    "website are valid for use in the State. Building code modifications that "
    "have not been approved by the Council are invalid and cannot be adopted, "
    "employed or enforced by municipalities and counties.”"))
flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "The codes above roll over on 1 January 2027 — and your permit date "
    "decides whether that reaches you", [
        Paragraph("This is the most important date in this document, and it "
                  "is close. On <b>26&#160;August&#160;2025</b> the Building "
                  "Codes Council adopted the <b>2024</b> editions of the "
                  "building, residential, fire, plumbing, mechanical and fuel "
                  "gas codes together with the <b>2023 National Electrical "
                  "Code</b>, and “established the implementation date for "
                  "local jurisdictions as <b>January&#160;1,&#160;2027</b>.”",
                  S["body"]),
        Paragraph("Everything printed in this kit is the stack in force "
                  "<b>now</b> — the 2021 codes and the 2020 NEC, implemented "
                  "1&#160;January&#160;2023 — and it stays in force through "
                  "the end of 2026. The one thing that does <i>not</i> move "
                  "is the energy standard: the 2024 modification index says "
                  "again that the 2009&#160;IECC “has been statutorily "
                  "adopted as the energy standard and is mandatory for use in "
                  "all jurisdictions within the State.”", S["body"]),
        Paragraph("<b>Here is what to do about it.</b> Section&#160;6-9-130(A) "
                  "fixes your house to the codes in effect on the date your "
                  "original building permit was <i>issued</i>. A permit "
                  "issued before 1&#160;January&#160;2027 keeps your whole "
                  "build on the 2021 stack, however long it runs. A permit "
                  "issued on or after that date lands on the 2024 stack. If "
                  "you are permitting in late 2026, that single date is worth "
                  "more to your schedule than anything else on this page — "
                  "and if you slip past it, ask your plan reviewer which "
                  "edition your drawings are being reviewed against before "
                  "you resubmit.", S["body"]),
        Paragraph("Two changes worth knowing in advance. At the rollover the "
                  "wind and seismic sections stop pointing at the Council's "
                  "county maps and the ATC website and point instead at the "
                  "<b>ASCE Hazard Tool</b> — so the map advice on the next "
                  "page has a shelf life. And South Carolina's own amendments "
                  "are renumbered: the termite provisions move from R318 to "
                  "<b>R305</b>, and the sprinkler section from R313 to "
                  "<b>R309</b>. Same rules, different addresses.", S["body"]),
    ]))
flow.append(Spacer(1, 3))
flow.append(k.body(
    f"How often that happens is now a four-year question, not a three-year "
    f"one: R.8-240(A) requires the Council to adopt the latest editions “at "
    f"least every four (4) years,” a change made effective "
    f"24&#160;May&#160;2024. Adoption runs through a Notice in the State "
    f"Register, a comment period “of not less than one hundred eighty days,” "
    f"a study committee and at least one public meeting, and the Council “shall "
    f"determine whether the amended or modified code becomes effective on the "
    f"first day of January or July” ({sec('6-9-40')})."))

# ------------------------------------------------------------- the energy
flow += k.h2("THE ENERGY STANDARD IS A STATUTE, NOT A CODE")
flow.append(k.body(
    "This is the South Carolina answer that confuses everyone, and it has a "
    "clean explanation. The Building Codes Council <b>does not adopt the "
    "energy chapter of the residential code at all</b> — R.8-1230 reads, in "
    "full: “IRC Chapter 11 Energy Efficiency. The Building Codes Council does "
    "not adopt IRC Chapter 11.”"))
flow.append(k.body(
    f"What applies instead is the <b>Energy Standard Act</b>, Title 6 Chapter "
    f"10, and it names its own edition in the statute: “The 2009 edition of "
    f"the International Energy Conservation Code is adopted as the Energy "
    f"Standard. All new and renovated buildings and additions constructed "
    f"within the State must comply with this standard” "
    f"({sec('6-10-30')}). That sentence was last changed by 2012 Act "
    f"No.&#160;143, effective 1&#160;January&#160;2013, which “substituted "
    f"‘2009’ for ‘2006’.”"))
flow.append(k.body(
    "So the reason South Carolina is on a 2009 energy code is not inertia at "
    "the code council. <b>The council has no power over it.</b> Moving the "
    "energy standard takes an act of the General Assembly, and the last one "
    "was in 2012."))
rows = [
    [k.cellp("<b>Fireplaces</b>"),
     k.cellp("“Notwithstanding Section 402.4.3 of the 2009 Edition of the "
             "International Energy Conservation Code, new wood-burning "
             "fireplaces shall have <b>tight-fitting flue dampers and outdoor "
             "combustion air</b>.” A statutory requirement, not a code one."),
     k.cellp(f"{sec('6-10-35')}")],
    [k.cellp("<b>Who enforces it</b>"),
     k.cellp("“Local building officials shall enforce the provisions of the "
             "Energy Standard.” Where there is no building official the "
             "jurisdiction may designate its engineer, director of public "
             "works, or chief fire inspector."),
     k.cellp(f"{sec('6-10-50')}(A), (B)")],
    [k.cellp("<b>What non-compliance costs</b>"),
     k.cellp("The official “shall notify the permit holder in writing to "
             "bring the building into compliance… or to secure it from entry "
             "or both; if the permit holder fails to comply… the building "
             "official <b>shall revoke the permit</b>.”"),
     k.cellp(f"{sec('6-10-50')}(E)")],
    [k.cellp("<b>Log and recreational buildings</b>"),
     k.cellp("Local jurisdictions “must provide an appeals board and process "
             "for the routine granting of variations” for residential "
             "recreational dwellings not intended as permanent residences and "
             "for buildings “such as log buildings which, if insulation were "
             "required on the walls, would change the character” of them."),
     k.cellp(f"{sec('6-10-70')}(A)")],
    [k.cellp("<b>Modular</b>"),
     k.cellp("An energy variation granted to a local jurisdiction “shall "
             "apply only to site constructed buildings.” A properly labeled "
             "modular building is accepted as in full compliance."),
     k.cellp("Reg. 8-250(D)")],
]
flow.append(k.ref_table(
    "Four things in the Energy Standard Act you will not find in the code "
    "book",
    [k.cellp("", bold=True), k.cellp("What it says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.35 * inch, CW - 2.55 * inch, 1.20 * inch]))
flow.append(k.cite(
    "One wrinkle worth knowing before you argue with anyone: an Editor's Note "
    "to Chapter 10, quoting 1997 Act No. 123, Section 6, provides that "
    "“Chapter 10 of Title 6 of the 1976 Code is not applicable in counties or "
    "municipalities which have fully implemented building codes as required "
    "in Section 6-9-10.” Read together with R.8-1230, the practical answer in "
    "every jurisdiction is the same 2009 IECC — but if a plan reviewer cites "
    "a different energy edition, that note is where the argument comes from. "
    "Ask, and write the answer down."))

# --------------------------------------------------------------- the wind
flow += k.h2("GETTING A REAL WIND NUMBER FOR YOUR PARCEL")
flow.append(k.body(
    "South Carolina is one of the few states carrying serious hurricane "
    "exposure and a serious earthquake zone at once, and it handles both the "
    "same way: <b>by map, delegated to your building official.</b> The "
    "modified wind section reads:"))
flow.append(k.body(
    "“Buildings and portions thereof shall be constructed in accordance with "
    "the previously published maps by the South Carolina Building Codes "
    "Council. <b>The local building official may delineate the wind design "
    "category within their jurisdiction</b> provided that it does not surpass "
    "those provided on the Applied Technology Council (ATC) website.”"))
flow.append(k.cite(
    "IRC Section R301.2.1 as modified, S.C. Code of Regs. 8-1202. The same "
    "section keeps the continuous load path requirement — “A continuous load "
    "path shall be provided to transmit the applicable uplift forces in "
    "Section R802.11 from the roof assembly to the foundation” — and sends "
    "asphalt shingles to R905.2.4 and metal roof shingles to R905.4.4 for "
    "wind speed."))
flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "Why this kit does not print a wind speed for your county", [
        Paragraph("Because South Carolina law forbids the state from drawing "
                  f"the line that way. Section&#160;6-9-105(C): “Where a "
                  "boundary for a physical or climatological condition is "
                  "referenced in a code, the council, upon adoption of the "
                  "code, is required to define the boundary so that it "
                  "approximates the physical or climatological area, using "
                  "logical geographic features such as major highways, "
                  "waterbodies, or ridgelines. <b>Political boundaries may "
                  "not be used unless they approximate the physical "
                  "area.</b>”", S["body"]),
        Paragraph("A table of design wind speeds by county is therefore an "
                  "approximation of a boundary the statute specifically "
                  "declines to draw on county lines — and on the coast the "
                  "difference between one side of a highway and the other is "
                  "real money in straps, sheathing and glazing. Two lots in "
                  "the same county, ten miles apart, do not get the same "
                  "answer.", S["body"]),
        Paragraph("<b>The maps do exist, and you can download them.</b> They "
                  "are at <b>llr.sc.gov/bcc/maps.aspx</b> — “Wind/Seismic "
                  "Maps,” one free PDF per county, reachable from the "
                  "Council's Building Code Adoption page rather than from its "
                  "Codes page. The Council's own wording: the maps “are "
                  "intended to be <b>the primary source</b> for defining the "
                  "appropriate boundaries for wind and seismic design in "
                  "South Carolina for single- and two-family dwellings.”",
                  S["body"]),
        Paragraph("Three things to know before you open one. They are "
                  "hand-drawn contour lines over old highway sheets, and "
                  "<b>interpolating between the lines is expressly the "
                  "building official's call</b>, not yours. The maps approved "
                  "for the current code cycle are keyed to the "
                  "<b>2015</b>&#160;IRC — an older wind standard than the "
                  "2021 code they sit inside. And <b>eleven counties have no "
                  "approved map at all</b>: Anderson, Cherokee, Greenville, "
                  "Greenwood, Laurens, McCormick, Oconee, Pickens, "
                  "Spartanburg, Sumter and Union — which includes the three "
                  "largest Upstate markets.", S["body"]),
        Paragraph("For those eleven the regulation and the Council both send "
                  "you to the Applied Technology Council website. <b>As of "
                  "September 2026 that site is offline</b>, returning a "
                  "“Website Suspended” placeholder. The working substitute is "
                  "the <b>ASCE Hazard Tool</b> at <b>ascehazardtool.org</b>, "
                  "which is live, free, takes a street address and returns "
                  "wind, seismic, snow and flood parameters. Use it to arrive "
                  "informed — but the number that governs your permit is the "
                  "one your building official gives you in writing. Record it "
                  "below.", S["body"]),
        Paragraph("<b>For orientation only, and not a substitute for asking:</b> "
                  "across the Council's published county maps South Carolina "
                  "runs from about <b>115&#160;mph</b> ultimate in the "
                  "Upstate and Midlands to roughly <b>150&#160;mph</b> on the "
                  "immediate Atlantic shoreline of Horry, Georgetown and "
                  "Charleston counties. Everything in between is interpolated "
                  "by the local official, and a few counties carry a flat "
                  "blanket value written on the map instead of contours.",
                  S["body"]),
    ]))
flow.append(Spacer(1, 4))
flow += k.check_table(
    "Design criteria to confirm with your building official — write the "
    "answers here",
    [
        ("Ultimate design wind speed (V<sub>ult</sub>), 3-second gust, Risk "
         "Category II", [("mph", 0.45), ("Confirmed by", 0.55)]),
        ("Exposure category for this parcel (B, C or D)",
         [("Category", 0.45), ("Date", 0.55)]),
        ("Is the parcel in a wind-borne debris region? If yes, what opening "
         "protection is required", [("Yes / No", 0.4), ("Requirement", 0.6)]),
        ("Seismic design category from the Council's map as delineated here",
         [("SDC", 0.4), ("Confirmed by", 0.6)]),
        ("Flood zone, and Base Flood Elevation if in one — plus any local "
         "freeboard above BFE", [("Zone", 0.35), ("BFE + freeboard", 0.65)]),
        ("Frost depth used for footings in this jurisdiction",
         [("Inches", 0.4), ("Date", 0.6)]),
        ("Ground snow load, if the office specifies one",
         [("psf", 0.4), ("Date", 0.6)]),
        ("Termite probability designation for this parcel — “very heavy” "
         "changes what insulation you may use", [("Designation", 1.0)]),
    ], notes_header="Confirmed by", date_w=0.85, notes_w=1.45)

# ------------------------------------------------------------- seismic
flow += k.h2_tight("SEISMIC: THE OTHER MAP", reserve=2.0)
flow.append(k.body(
    "The seismic section is worded almost identically, and it is not a "
    "formality in the Lowcountry: “Buildings shall be assigned a seismic "
    "design category in accordance with the previously published maps by the "
    "S.C. Building Codes Council. The local building official may delineate "
    "the seismic design category within their jurisdiction, as long as it "
    "does not surpass those provided on the Applied Technology Council (ATC) "
    "website.”"))
flow.append(k.cite(
    "IRC Section R301.2.2.1 as modified, S.C. Code of Regs. 8-1203. The "
    "same county maps carry the seismic categories, at "
    "<b>llr.sc.gov/bcc/maps.aspx</b>."))
flow.append(Spacer(1, 2))
flow.append(k.callout(
    "The seismic sentence that decides whether this costs you anything", [
        Paragraph("A <b>detached</b> one- or two-family dwelling picks up the "
                  "residential code's seismic provisions only in Seismic "
                  "Design Categories D<sub>0</sub>, D<sub>1</sub> and "
                  "D<sub>2</sub>. In category&#160;<b>C</b> a detached house "
                  "does <b>not</b> trigger them — but a <b>townhouse</b> in "
                  "category&#160;C does. That one distinction is the whole "
                  "question for most Lowcountry lots, and Charleston County "
                  "spans several categories, so the answer can change across "
                  "a parcel line rather than a county line.", S["body"]),
        Paragraph("Two ways out if you land high. R301.2.2.1.1 lets the "
                  "building official reclassify a site downward on soil "
                  "conditions — that is how a geotech report can move a "
                  "marginal Lowcountry lot from engineered back to "
                  "prescriptive. And on the coast the wind trigger usually "
                  "bites first anyway: once the ultimate design wind speed "
                  "reaches 140&#160;mph the prescriptive wind provisions stop "
                  "applying and the house needs engineering regardless of "
                  "what the seismic map says. R.8-1201 defines “Accepted "
                  "Engineering Practice” for that case, requiring design “by "
                  "a South Carolina licensed Architect or Engineer.”",
                  S["body"]),
    ]))

# ------------------------------------------------------------- termites
flow += k.h2("THE TERMITE AMENDMENTS THAT DECIDE YOUR INSULATION ORDER")
flow.append(k.body(
    "Every guide tells you South Carolina has bad termites. Here is the part "
    "that changes a purchase order. In areas designated “very heavy” for "
    "termite probability, the state code <b>bans foam plastic below grade on "
    "your foundation</b> and requires an inspection gap you have to build in "
    "deliberately."))
rows = [
    [k.cellp("<b>No foam below grade</b>"),
     k.cellp("“Extruded and expanded polystyrene, polyisocyanurate and other "
             "foam plastics <b>shall not be installed on the exterior face or "
             "under interior or exterior foundation walls or slab "
             "foundations located below grade</b>.” Exceptions: structural "
             "members entirely noncombustible or pressure-preservative "
             "treated; and the interior side of basement walls."),
     k.cellp("R.8-1216")],
    [k.cellp("<b>Six inches of clear above grade</b>"),
     k.cellp("“The clearance between foam plastics installed above grade and "
             "exposed earth shall be not less than <b>6&#160;inches</b>.”"),
     k.cellp("R.8-1216")],
    [k.cellp("<b>A crawl space inspection gap</b>"),
     k.cellp("“For crawl space applications, foam plastic shall be installed "
             "so as to provide a termite inspection gap of no less than "
             "<b>6&#160;inches</b> along the top of the foundation wall and "
             "foundation sill plate.”"),
     k.cellp("R.8-1216")],
    [k.cellp("<b>A six-inch strip at the sill</b>"),
     k.cellp("“Where foam plastic is applied in accordance with R318.4, a "
             "<b>continuous 6&#160;inch strip centered along the sill "
             "plate</b> shall be left open for termite activity "
             "inspection.”"),
     k.cellp("R.8-1217")],
    [k.cellp("<b>A seventh treatment method</b>"),
     k.cellp("South Carolina adds to the IRC's list of subterranean termite "
             "control methods: “Treatments may be conducted as outlined in "
             "Section 27-1085 of the Rules and Regulations for the "
             "Enforcement of the SC Pesticide Control Act and enforced by the "
             "<b>Clemson University Department of Pesticide Regulation</b>.”"),
     k.cellp("R.8-1215")],
]
flow.append(k.ref_table(
    "IRC R318 as South Carolina modified it",
    [k.cellp("", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.60 * inch, CW - 2.55 * inch, 0.95 * inch]))
flow.append(k.cite(
    "S.C. Code of Regs. 8-1215 through 8-1217, modifying IRC Sections R318.1, "
    "R318.4 and R318.5. Two consequences to plan for: a below-grade exterior "
    "foam detail that is routine in other states cannot be built here, and "
    "your termite treatment is regulated by an agency — the Clemson "
    "University Department of Pesticide Regulation — that is neither your "
    "building department nor a health agency. Ask who signs the treatment "
    "record your inspector wants to see."))

# ---------------------------------------------------- crawl spaces, slabs
flow += k.h2("CRAWL SPACES AND SLABS: THE HUMIDITY AMENDMENTS")
flow.append(k.body(
    "South Carolina rewrote the unvented crawl space section, deleted the "
    "code's own under-floor vapor retarder section, and set a thicker slab "
    "vapor retarder than the model code. If you are building over a crawl "
    "space in the Lowcountry, this is the page to hand your framer."))
flow.append(k.bullet(
    "<b>Unvented crawl space.</b> Exposed earth covered with a continuous "
    "vapor retarder meeting <b>ASTM&#160;E1745 Class&#160;A</b>; joints "
    "overlapped <b>6&#160;inches</b> and sealed or taped; edges extending not "
    "less than <b>6&#160;inches up the stem wall</b>, attached and sealed. "
    "Then <i>one</i> of: continuously operated mechanical exhaust at "
    "<b>1&#160;cfm per 50&#160;square feet</b> of crawl space floor area with "
    "an air pathway to the common area and insulated perimeter walls; a "
    "conditioned air supply at the same rate with a return air pathway; a "
    "plenum in an existing structure complying with M1601.5; or "
    "dehumidification sized to the manufacturer's specifications. "
    "(R.8-1221, modifying R408.3)"))
flow.append(k.bullet(
    "<b>The model code's under-floor vapor retarder section is gone.</b> "
    "“Section R408.8 is deleted without substitution.” (R.8-1223)"))
flow.append(k.bullet(
    "<b>Slab vapor retarder is 10&#160;mil, Class&#160;A.</b> “A minimum "
    "10-mil vapor retarder conforming to ASTM&#160;E1745 Class&#160;A "
    "requirements with joints lapped not less than 6&#160;inches shall be "
    "placed between the concrete floor slab and the base course or the "
    "prepared subgrade.” Not required for utility buildings and unheated "
    "accessory structures, unheated storage rooms under "
    "70&#160;square&#160;feet and carports, flatwork, or where the building "
    "official approves based on local site conditions. (R.8-1225, modifying "
    "R506.2.3)"))
flow.append(k.bullet(
    "<b>Access openings are specified.</b> Through the floor, not smaller "
    "than <b>18 by 24&#160;inches</b>; through a perimeter wall, not less "
    "than <b>16 by 24&#160;inches</b>; a below-grade through-wall access "
    "needs an areaway of at least the same size with its bottom below the "
    "threshold. (R.8-1222, modifying R408.4)"))
flow.append(k.bullet(
    "<b>Piers are prescriptive, and exterior piers get a dowel.</b> Piers "
    "under interior bearing-wall girders: solidly grouted, minimum nominal "
    "dimension <b>8&#160;inches</b>, maximum height ten times the nominal "
    "thickness. Piers under exterior bearing walls: solidly filled, “shall "
    "contain a minimum of one #4 dowel mid-depth,” minimum nominal dimension "
    "8&#160;inches, and maximum height <b>four</b> times the nominal "
    "thickness — ten times only where accepted engineering practice shows "
    "enough foundation wall to resist the lateral loads. (R.8-1220, modifying "
    "R404.1.9.2)"))

# ------------------------------------------------ deleted and added
flow += k.h2("WHAT SOUTH CAROLINA DELETED, AND WHAT IT ADDED")
flow.append(k.body(
    "Deletions are worth as much as requirements when you are budgeting, and "
    "South Carolina has made several that other states have not."))
rows = [
    [k.cellp("<b>Deleted</b>", center=True),
     k.cellp("<b>Residential fire sprinklers.</b> “An automatic residential "
             "fire sprinkler system shall not be required to be installed in "
             "one- and two-family dwellings” — and the same for townhouses "
             "built to R302.2."), k.cellp("R.8-1213")],
    [k.cellp("<b>Deleted</b>", center=True),
     k.cellp("<b>Whole-house mechanical ventilation.</b> “The Building Codes "
             "Council does not adopt IRC Section R303.4.”"),
     k.cellp("R.8-1208")],
    [k.cellp("<b>Deleted</b>", center=True),
     k.cellp("<b>Window fall protection.</b> R312.2, R312.2.1 and R312.2.2 "
             "are all not adopted."), k.cellp("R.8-1212")],
    [k.cellp("<b>Deleted</b>", center=True),
     k.cellp("<b>Whole-house surge protection.</b> Said twice: IRC E3606.5 "
             "“is deleted without substitution,” and NEC Article 230.67 "
             "“including (A) through (D), does not apply in this State.”"),
     k.cellp("R.8-1247; R.8-1106")],
    [k.cellp("<b>Deleted</b>", center=True),
     k.cellp("<b>The 2020 NEC outdoor-outlet GFCI rule.</b> “NEC Article "
             "210.8(F) Outdoor Outlets. This article does not apply in this "
             "State.” Walk-out basement receptacles are also excluded from "
             "the basement GFCI requirement."),
     k.cellp("R.8-1104; R.8-1251")],
    [k.cellp("<b>Deleted</b>", center=True),
     k.cellp("<b>The hose bibb section.</b> IRC P2903.10 “is deleted without "
             "substitution.”"), k.cellp("R.8-1245")],
    [k.cellp("<b>Added</b>", center=True),
     k.cellp("<b>Three IRC appendices, adopted on purpose.</b> Appendix AH "
             "Patio Covers, Appendix AJ Existing Buildings, and "
             "<b>Appendix&#160;AQ Tiny Houses</b>. Appendices are "
             "unenforceable in South Carolina unless named at adoption "
             "(R.8-236(D)) — these were named."),
     k.cellp("R.8-1255 to R.8-1257")],
    [k.cellp("<b>Added</b>", center=True),
     k.cellp("<b>A guard trigger the model code does not have.</b> Guards are "
             "required over 30&#160;inches “and at any point where a downward "
             "slope exceeds 3V:12H within 36&#160;inches horizontally to the "
             "edge of the open side. <b>Insect screening shall not be "
             "considered as a guard.</b>”"), k.cellp("R.8-1211")],
    [k.cellp("<b>Added</b>", center=True),
     k.cellp("<b>Truss drawings on site.</b> “Truss design drawings… shall be "
             "provided to the building official <b>at the time of "
             "inspection</b>. Truss design drawings shall be provided with "
             "the shipment of trusses delivered to the job site.” Twelve "
             "enumerated contents. Ask your supplier for the package in "
             "writing when you order."), k.cellp("R.8-1224; R.8-1227")],
    [k.cellp("<b>Changed</b>", center=True),
     k.cellp("<b>Stair risers.</b> “The maximum riser height shall be "
             "7&#160;3/4&#160;inches. The maximum riser height for masonry "
             "stairs shall be 8&#160;inches.”"), k.cellp("R.8-1210")],
    [k.cellp("<b>Changed</b>", center=True),
     k.cellp("<b>Dryer duct length.</b> “The maximum length of a clothes "
             "dryer exhaust duct shall not exceed <b>35&#160;feet</b> from "
             "the dryer location to the wall or roof termination.” "
             "Terminations get a backdraft damper, and “screens shall not be "
             "installed at the duct termination.”"),
     k.cellp("R.8-1234; R.8-1232")],
    [k.cellp("<b>Changed</b>", center=True),
     k.cellp("<b>Water service depth.</b> “Water service pipe shall be "
             "installed not less than <b>12&#160;inches deep</b> and not less "
             "than <b>6&#160;inches below the frost line</b>.”"),
     k.cellp("R.8-1241")],
]
flow.append(k.ref_table(
    "Amendments that change a budget or a detail",
    [k.cellp("", bold=True), k.cellp("What South Carolina did", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [0.82 * inch, CW - 2.12 * inch, 1.30 * inch]))
flow.append(k.cite(
    "All from S.C. Code of Regs. Chapter 8, Articles 11 and 12 — the 2020 NEC "
    "and 2021 IRC modification summaries. Two of these are commonly "
    "misreported. A statute at "
    f"{sec('6-9-55')}(C) bars enforcement of “Section 501.3 of the <b>2012</b> "
    "International Residential Code,” which was the fire protection of floors "
    "rule; the 2012 edition is not in force, and South Carolina <i>does</i> "
    "adopt the current version of that rule as R302.13, with exceptions for "
    "floors over a crawl space and for framing of 2×10 nominal or greater "
    "(R.8-1207). And the sprinkler answer is the regulation above, not "
    f"{sec('6-9-55')}(B), whose July 2015 date has long passed."))

# ---------------------------------------------------------------- package
flow += k.h2_tight("THE PERMIT PACKAGE", reserve=2.0)
flow.append(k.body(
    "South Carolina does not set a statewide list of what a residential "
    "permit application must contain, so the specifics are your office's. "
    "What follows is the set every South Carolina jurisdiction asks for in "
    "some form, plus the items this state's statutes add."))
flow += k.check_table(
    "Gather before you file",
    [
        ("Completed building permit application — signed by you, in person "
         f"({sec('40-59-260')}(C))", [("Date", 1.0)]),
        ("The owner-builder disclosure statement your office uses, read and "
         "signed", [("Form name", 1.0)]),
        ("Register-of-deeds notice forms, requested at the same visit "
         f"({sec('40-59-260')}(D))", []),
        ("Name and license or registration number of every licensed "
         "contractor on the project — Chapter 11 requires an exempt owner to "
         f"list them on the application ({sec('40-11-420')}(C))", []),
        ("Two sets of construction drawings to the scale your office "
         "specifies, with the design criteria above shown on them", []),
        ("Site plan showing setbacks, driveway, well and septic components "
         "if applicable, and drainage", []),
        ("Deed or plat establishing ownership and the parcel identification "
         "number", []),
        ("Septic construction permit or public sewer availability letter", []),
        ("Well permit or public water availability letter", []),
        ("Floodplain documentation and elevation certificate if the parcel "
         "is in a mapped flood hazard area", []),
        ("Driveway or encroachment permit if you are connecting to a "
         "state-maintained road", []),
        ("Land disturbance or stormwater coverage if you will disturb one "
         "acre or more", []),
        ("Truss package, when it arrives — the drawings must be on site and "
         "given to the inspector (R.8-1224)", []),
        ("Termite treatment arrangement, and who will produce the record "
         "your inspector wants", []),
        ("Energy compliance documentation to the 2009 IECC, in the form your "
         "office accepts", []),
        ("Fee schedule read, and the payment method your office takes "
         "confirmed", [("Estimate", 1.0)]),
    ])
flow.append(k.cite(
    "Fees are set locally: a county or municipality “may impose fees "
    f"necessary and consistent with Section 6-9-30(B)” on a simple majority "
    f"vote ({sec('6-9-90')}), and the building official “may prescribe fees "
    f"for construction permits and inspections” ({sec('6-9-30')}(A)). No "
    f"statewide schedule exists, which is why this kit gives you a line "
    f"rather than a number."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "Two exemptions that live in the licensing chapter, not the code", [
        Paragraph(f"<b>Small work needs no permit at all.</b> "
                  f"Section{NB}40-59-265, added by 2022 Act No.&#160;186 "
                  f"effective 16&#160;May&#160;2022, lists work that is "
                  f"“exempt from building permit application requirements” "
                  f"statewide — including one-story detached accessory "
                  f"structures not exceeding 200&#160;square&#160;feet, "
                  f"fences not over 7&#160;feet, retaining walls not over "
                  f"4&#160;feet unless supporting a surcharge, decks not "
                  f"exceeding 200&#160;square&#160;feet and not more than "
                  f"30&#160;inches above grade at any point, sidewalks and "
                  f"driveways, and finish work. SC.5 carries the full list.",
                  S["body"]),
        Paragraph(f"<b>Farm buildings are outside the code — if you file "
                  f"first.</b> Section&#160;6-9-65 bars a county or "
                  f"municipality from enforcing the building code on a farm "
                  f"structure, but only if “<b>before</b> constructing a farm "
                  f"structure” the owner files an affidavit with the building "
                  f"official stating that it is being built as one, including "
                  f"a statement of intended use. FEMA flood standards still "
                  f"apply, the jurisdiction may still require a permit, and a "
                  f"structure “originally qualifying as a ‘farm structure’ but "
                  f"later converted to another use” is not one.", S["body"]),
    ]))

# -------------------------------------------------------------- sources
flow += k.h2_tight("SOURCES", reserve=2.0)
flow.append(k.sources_table([
    ("Every code edition in force, and the modifications to each",
     "S.C. Code of Regs. Ch. 8, Arts. 8–14"),
    ("Residential code provisions must be promulgated as regulations before "
     "they may be enforced", f"S.C. Code Ann. {sec('6-9-55')}(A)"),
    ("Adoption procedure, 180-day comment period, January or July effective "
     "dates", f"S.C. Code Ann. {sec('6-9-40')}; Reg. 8-240"),
    ("The 2021 suite was adopted 6 October 2021 with an implementation date "
     "of 1 January 2023",
     "SC Building Codes Council, 2021 Code Adoptions notice"),
    ("The 2024 suite and the 2023 NEC were adopted 26 August 2025 with an "
     "implementation date of 1 January 2027; the 2009 IECC does not move "
     "with them",
     "SC Building Codes Council, 2024 Modifications Index"),
    ("Wind and seismic county maps, and the note that they are the primary "
     "source", "SC Building Codes Council, Wind/Seismic Maps"),
    ("The permit issuance date fixes the code edition your house is "
     "inspected against",
     f"S.C. Code Ann. {sec('6-9-130')}; Reg. 8-236(B)"),
    ("Statewide modifications are mandatory; local governments may not write "
     "their own building codes", "Reg. 8-240(K); Reg. 8-236(C)"),
    ("Climatological boundaries must follow geography, not political lines",
     f"S.C. Code Ann. {sec('6-9-105')}(C)"),
    ("Wind and seismic design categories come from Council maps as "
     "delineated by the local building official",
     "Reg. 8-1202; Reg. 8-1203"),
    ("The 2009 IECC is the Energy Standard, adopted by statute; the Council "
     "does not adopt IRC Chapter 11",
     f"S.C. Code Ann. {sec('6-10-30')}; Reg. 8-1230"),
    ("Fireplace dampers and outdoor combustion air; energy enforcement and "
     "permit revocation; log and recreational variances",
     f"S.C. Code Ann. {sec('6-10-35')}, {sec('6-10-50')}, {sec('6-10-70')}"),
    ("Termite amendments: no foam below grade, six-inch clearances, the "
     "inspection strip, and the Clemson treatment route",
     "Reg. 8-1215, 8-1216, 8-1217"),
    ("Unvented crawl spaces, deleted under-floor vapor retarder, 10-mil slab "
     "retarder, access openings, pier rules",
     "Reg. 8-1220 to 8-1225"),
    ("No residential sprinkler mandate; no whole-house ventilation or window "
     "fall protection; no surge protection; no outdoor-outlet GFCI rule",
     "Reg. 8-1213, 8-1208, 8-1212, 8-1247, 8-1104, 8-1106"),
    ("Appendices AH, AJ and AQ adopted; appendices otherwise unenforceable",
     "Reg. 8-1255 to 8-1257; Reg. 8-236(D)"),
    ("Statewide list of work needing no building permit",
     f"S.C. Code Ann. {sec('40-59-265')}"),
    ("Farm structures are outside the code if an affidavit is filed first",
     f"S.C. Code Ann. {sec('6-9-65')}"),
    ("Permit fees are set locally",
     f"S.C. Code Ann. {sec('6-9-30')}(A), {sec('6-9-90')}"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "sc-permit-kit",
                       "SC.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
