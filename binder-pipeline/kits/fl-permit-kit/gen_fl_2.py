#!/usr/bin/env python3
"""FL.2 Permit Application Checklist.

Two things in this document are the reason it exists.

The first is FLORIDA PRODUCT APPROVAL. Section 553.842(5), Fla. Stat. names
eight categories of product — panel walls, exterior doors, roofing, skylights,
windows, shutters, impact protective systems and structural components — that
must carry a statewide approval before they may be used in construction in
Florida. An owner-builder meets this as a plan-review demand for an approval
number against every exterior opening, and it is a purchasing constraint
disguised as paperwork: the cheapest window on the rack may simply have no
Florida approval.

The second is the STATUTORY REVIEW CLOCK at s. 553.792. Florida does not
merely encourage a timely plan review, it prices it: 30 business days for a
residential permit on a structure under 7,500 square feet, and a 10 percent
reduction in the permit fee for every business day the local government runs
late. Almost no owner-builder knows the clock exists, which means almost none
of them start it deliberately or notice when it is missed.

Deliberately NOT printed here: a county fee table (fees are local and go
stale), a county wind-speed table (the code points to the ASCE tool instead of
a static table), and the verbatim windborne-debris-region definition (the
8th Edition amended limb 1 and the exact current wording could not be pulled
from a primary source — the kit prints the practical consequence and tells the
reader to confirm the parcel).
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

FORM_ID = "FL.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Before You File"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "What to gather before you file, which numbers the plan "
                 "reviewer will look for, and how long they have to answer.")
flow.append(k.disclaimer())

# ------------------------------------------------------------ code editions
flow += k.h2("WHAT IS IN FORCE RIGHT NOW")
flow.append(k.body(
    "Florida runs one building code statewide, updated on a three-year cycle. "
    "Your project is reviewed against the edition in force, so the first "
    "thing to establish is which edition that is."))
rows = [
    [k.cellp("<b>Florida Building Code, Residential</b>"),
     k.cellp("8th Edition (2023), based on the <b>2021 IRC</b>"),
     k.cellp("Detached one- and two-family dwellings and townhouses not more "
             "than three stories, plus accessory structures")],
    [k.cellp("<b>Florida Building Code, Energy Conservation</b>"),
     k.cellp("8th Edition (2023), based on the <b>2021 IECC</b>"),
     k.cellp("All of Florida is a hot-humid climate zone; the performance "
             "path was tightened 5% in this edition")],
    [k.cellp("<b>Electrical (NFPA 70, the NEC)</b>"),
     k.cellp("<b>Read the note below</b> — the 8th Edition as adopted "
             "referenced the 2020 NEC, and the Commission has since updated "
             "the referenced standard to the 2023 NEC"),
     k.cellp("Adopted through the code rather than as a separate state "
             "electrical code")],
    [k.cellp("<b>Plumbing, Mechanical, Fuel Gas, Existing Building</b>"),
     k.cellp("8th Edition (2023)"),
     k.cellp("Separate volumes of the same code")],
    [k.cellp("<b>Test Protocols for HVHZ</b>"),
     k.cellp("8th Edition (2023)"),
     k.cellp("Its own volume — applies in Miami-Dade and Broward")],
    [k.cellp("<b>Wind</b>"),
     k.cellp("<b>ASCE 7-22</b>"),
     k.cellp("Updated from ASCE 7-16 in this edition. Speeds are unchanged "
             "for most of Florida; some panhandle areas increased")],
]
flow.append(k.ref_table(
    "Code editions in force in Florida, effective 31 December 2023",
    [k.cellp("Code", bold=True), k.cellp("Edition", bold=True),
     k.cellp("Notes", bold=True)],
    rows, [2.00 * inch, 2.15 * inch, CW - 4.15 * inch]))
flow.append(k.cite(
    "Effective date and edition from the Florida Building Commission's own "
    "portal at floridabuilding.org; base I-Code years and the ASCE 7-22 "
    "change from the Commission's published Analysis of Changes for the 8th "
    "Edition. Read September 2026."))

flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "Two moving targets worth checking on the day you file", [
        Paragraph("<b>The 9th Edition (2026).</b> The Commission's own code "
                  "menu lists it as a <i>Draft</i>, and a public comment "
                  "period was still running in late 2026. No effective date "
                  "has been published. Any guide that gives you one is "
                  "guessing — but the edition that governs you is set when "
                  "you apply, so check floridabuilding.org before you file a "
                  "borderline project.", S["body"]),
        Paragraph("<b>Which NEC edition applies.</b> This one causes real "
                  "confusion. The 8th Edition as originally adopted pointed "
                  "at the 2020 NEC; the Commission has since revised the "
                  "referenced standard to the <b>2023 NEC</b>, using a "
                  "fast-track power the Legislature gave it specifically for "
                  "the electrical code (s. 553.73(8)(a)6.). That is why you "
                  "will find both answers in print, and both are defensible "
                  "citations to different documents. <b>Ask your electrical "
                  "plan reviewer which edition your permit is reviewed "
                  "against</b> and write it down — it changes receptacle, "
                  "GFCI and surge-protection requirements.", S["body"]),
    ]))

# ----------------------------------------------------------- local amendment
flow += k.h2("HOW MUCH YOUR COUNTY CAN CHANGE (VERY LITTLE)")
flow.append(k.body(
    "In most states this kit covers, the local jurisdiction is the wild card. "
    "In Florida it is close to fixed. A local government may amend the "
    "<i>administrative</i> provisions of the code, and may adopt "
    "<i>technical</i> amendments only if they are <b>more stringent</b>, no "
    "more often than once every six months, after an advertised public "
    "hearing, on evidence of a specific local need — and the amendment must "
    "not introduce a subject the code does not address."))
flow.append(k.body(
    "Then the part worth knowing: a local technical amendment "
    "“is effective only until the adoption of the new edition of the "
    "Florida Building Code by the commission every third year,” at which "
    "point the Commission either adopts it statewide or rescinds it "
    "(s. 553.73(4)(e)). Local amendments <b>expire on the code cycle.</b> "
    "Two carve-outs matter to you: provisions on wind resistance and water "
    "intrusion may never be weakened (s. 553.73(7)(f)), and <b>flood</b> "
    "amendments follow a separate, easier track and do not necessarily "
    "sunset (s. 553.73(5))."))
flow.append(k.cite(
    "Practical translation: expect the same technical code everywhere in "
    "Florida, and expect your genuine local variation to be about flood "
    "elevation, fees and process rather than construction standards."))

# -------------------------------------------------------- product approval
flow += k.h2("PRODUCT APPROVAL — THE ONE THAT SURPRISES PEOPLE")
flow.append(k.body(
    "Florida approves building products at the state level, and the approval "
    "attaches to the product, not to your project. Section 553.842(5) lists "
    "the categories that <b>must</b> be approved before use in construction "
    "in this state:"))
flow.append(k.callout(
    "The eight categories, in the statute's own words", [
        Paragraph("“panel walls, exterior doors, roofing, skylights, "
                  "windows, shutters, impact protective systems, and "
                  "structural components” (s. 553.842(5), Fla. Stat.)",
                  S["body"]),
    ]))
flow.append(k.body(
    "Each approved product carries a <b>Florida approval number</b>, written "
    "as FL followed by digits, and you look it up free at the Commission's "
    "product search: <b>floridabuilding.org/pr/pr_app_srch.aspx</b>. At plan "
    "review you will be asked to identify the approval number for every "
    "exterior opening and covered product. Most building departments have "
    "their own schedule or spreadsheet for this; the format is local, so "
    "<b>ask for their template before you submit</b> rather than inventing "
    "one."))
flow.append(k.body(
    "Two consequences owner-builders discover late. First, this is a "
    "<b>purchasing constraint</b>: a window with no Florida approval cannot "
    "be permitted here no matter how good it is, so check the number before "
    "you order, not after it arrives. Second, the approval is genuinely "
    "portable — statewide approval “shall preclude local jurisdictions "
    "from requiring further testing, evaluation, or submission of other "
    "evidence as a condition of using the product” so long as you use it "
    "consistently with its approval (s. 553.842(4)). A building official who "
    "wants to refuse an approved product must put the reasons in a signed "
    "written report (s. 553.842(9))."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "Miami-Dade and Broward: a second vocabulary", [
        Paragraph("The High-Velocity Hurricane Zone is <b>Broward and "
                  "Miami-Dade counties</b>. There you will also meet the "
                  "Miami-Dade <b>Notice of Acceptance</b> (NOA), issued by "
                  "that county's Product Control Division — which the statute "
                  "also names as an approved evaluation entity for the "
                  "statewide system (s. 553.842(8)(a)). The two systems "
                  "overlap rather than compete, and which one your plan "
                  "reviewer will accept for a given product is a local "
                  "question. Ask before you buy. The HVHZ also uses its own "
                  "Uniform Permit Application for roofing (FBC Building "
                  "s. 1525).", S["body"]),
    ]))

# ------------------------------------------------------------------- wind
flow += k.h2("WIND, AND WHETHER YOU MUST PROTECT YOUR OPENINGS")
flow.append(k.body(
    "Your design wind speed is site-specific. The code now expressly permits "
    "location-specific speeds from the <b>ASCE Wind Design Geodatabase</b>, "
    "and the public tool is at <b>ascehazardtool.org</b>. This kit prints no "
    "county wind-speed table on purpose: the authoritative answer is a "
    "lookup for your coordinates, confirmed by your building department at "
    "plan review, and a table would only invite you to use the wrong number."))
flow.append(k.body(
    "Whether you must protect your openings depends on being inside the "
    "<b>windborne debris region</b>. The test has two limbs — a proximity to "
    "water combined with a design speed at or above 130&nbsp;mph, or a design "
    "speed at or above 140&nbsp;mph anywhere. The 8th Edition <b>amended the "
    "first limb</b>, and the Commission's own change notes say the effect is "
    "that some inland parcels near large bodies of water now fall inside the "
    "region."))
flow.append(k.callout(
    "Do not assume inland means exempt", [
        Paragraph("That amendment is the single most likely way for a "
                  "Florida owner-builder to budget wrong. A lakefront or "
                  "riverfront lot well away from the coast can sit inside the "
                  "windborne debris region and require protected openings "
                  "throughout. Because this kit could not obtain the exact "
                  "current wording of that definition from a primary source, "
                  "it will not paraphrase it: <b>ask your building department "
                  "to confirm, in writing, whether your parcel is in the "
                  "windborne debris region</b> before you price windows.",
                  S["body"]),
    ]))
flow.append(Spacer(1, 2))
flow.append(k.body(
    "If you are in the region, every exterior glazed opening must be "
    "protected — but <b>impact glass is not the only route</b>. The "
    "residential code accepts glazing meeting the Large Missile Test of "
    "ASTM E1996 and E1886, or TAS 201, 202 and 203, or AAMA 506; garage door "
    "glazing has its own standard. It also keeps a specific plywood "
    "exception: 7/16-inch wood structural panels, precut and predrilled with "
    "permanently installed corrosion-resistant hardware, on buildings with a "
    "mean roof height of 33&nbsp;feet or less where the design speed does not "
    "exceed 180&nbsp;mph. Storage sheds not designed for human habitation and "
    "720&nbsp;square feet or less are excepted."))
flow.append(k.cite(
    "FBC Residential R301.2.1.2 and R202; ASCE 7-22 as referenced by the 8th "
    "Edition. The plywood option is a real cost lever — confirm it is "
    "acceptable for your specific openings with your plan reviewer."))

# ----------------------------------------------------------------- energy
flow += k.h2("THE ENERGY PAPERWORK, AND THE TEST BEFORE YOUR CO")
flow.append(k.body(
    "Florida has three compliance paths and its own forms. There is no "
    "single “Form R405 PDF” to download, and Florida does not run on "
    "REScheck — the performance path's submittal is the report generated by "
    "Commission-approved energy software."))
rows = [
    [k.cellp("<b>Form R400-2023</b>"),
     k.cellp("Residential Energy Conservation Code Documentation Checklist — "
             "the cover sheet referenced across all three paths")],
    [k.cellp("<b>Prescriptive (R402)</b>"),
     k.cellp("<b>Form R402-2023</b>, the equipment requirements and "
             "installed-values table, now carrying SEER2 and HSPF2 "
             "labeling, with signature lines for preparer, owner and code "
             "official")],
    [k.cellp("<b>Performance (R405)</b>"),
     k.cellp("A report from Commission-approved software. The 8th Edition "
             "tightened this path: maximum total e-Ratio dropped from 1.00 "
             "to 0.95")],
    [k.cellp("<b>Energy Rating Index (R406)</b>"),
     k.cellp("A third path, based on a HERS-style index")],
]
flow.append(k.ref_table(
    "Which energy documents you will file",
    [k.cellp("Path", bold=True), k.cellp("What you submit", bold=True)],
    rows, [1.75 * inch, CW - 1.75 * inch]))

flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "The blower door test is mandatory, and you may not run it yourself", [
        Paragraph("Before your certificate of occupancy, the house has to "
                  "pass a building air leakage test. The maximum leakage rate "
                  "in Florida's climate zones is <b>7&nbsp;air changes per hour at "
                  "50&nbsp;pascals</b> — 7&nbsp;ACH50. The test happens after every "
                  "pipe, wire and other penetration of the thermal envelope "
                  "has been sealed.", S["body"]),
        Paragraph("Two things follow. The test must be performed by an energy "
                  "auditor or rater, a Class A or B air-conditioning or "
                  "mechanical contractor, or a third party approved by the "
                  "code official — <b>not by you and not self-certified</b>, "
                  "so budget for it. And if your house comes in "
                  "<b>tighter than 3&nbsp;ACH50</b>, the code then requires "
                  "whole-house mechanical ventilation. Building tight is "
                  "correct; just know it brings a ventilation obligation with "
                  "it rather than discovering that at the final inspection.",
                  S["body"]),
    ]))
flow.append(k.cite(
    "FBC Energy Conservation R402.4.1.2 and the Commission's own residential "
    "air leakage testing fact sheet. A duct leakage test is also standard on "
    "new construction; this kit does not print a leakage figure for it "
    "because the threshold was not confirmed against the current code book — "
    "ask your rater for the number they will test to."))

# ------------------------------------------------------------- the clock
flow += k.h2("HOW LONG THEY HAVE TO ANSWER — AND WHAT LATE COSTS THEM")
flow.append(k.body(
    "This is the most valuable page in the document and almost nobody uses "
    "it. Florida puts a statutory clock on residential plan review, and "
    "prices the overrun as a discount on your permit fee."))
rows = [
    [k.cellp("<b>Is the application complete?</b>"),
     k.cellp("The local government has <b>5&nbsp;business days</b> to tell you in "
             "writing what is missing. If it does not, your application is "
             "<b>automatically deemed complete</b>."),
     k.cellp("553.792(1)(c)")],
    [k.cellp("<b>The review itself</b>"),
     k.cellp("<b>30&nbsp;business days</b> for a residential permit — including a "
             "single-family dwelling — where the structure is <b>under 7,500 "
             "square feet</b>. 60&nbsp;business days at 7,500&nbsp;square feet or "
             "more."),
     k.cellp("553.792(1)(a)1.–2.")],
    [k.cellp("<b>If they run late</b>"),
     k.cellp("The permit fee is reduced by <b>10% for each business day</b> "
             "past the deadline, calculated on the original fee — unless the "
             "delay is your fault, mutually agreed, or force majeure."),
     k.cellp("553.792(1)(e)")],
    [k.cellp("<b>If they find deficiencies</b>"),
     k.cellp("A timely, specific written deficiency notice gives you "
             "<b>10&nbsp;business days</b> to revise; they then get <b>10&nbsp;business "
             "days</b> to approve or deny. Miss that second window and the "
             "penalty rises to <b>20% per business day</b>."),
     k.cellp("553.792(1)(f)–(g)")],
]
flow.append(k.ref_table(
    "The statutory plan review clock",
    [k.cellp("Stage", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.60 * inch, CW - 2.85 * inch, 1.25 * inch]))
flow.append(k.cite(
    "Section 553.792, Fla. Stat. Day counts are BUSINESS days throughout. "
    "Date-stamp your submittal and every response — the clock is only useful "
    "if you can show when it started."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "The other route: hire the review", [
        Paragraph("Section 553.791 lets you retain a <b>private provider</b> "
                  "— a licensed building code administrator, engineer or "
                  "architect — to do your plan review and inspections instead "
                  "of the county. Two things make it worth pricing. The local "
                  "jurisdiction <b>must</b> reduce your permit fee by its "
                  "cost savings, and may not charge inspection fees at all "
                  "beyond a reasonable administrative fee. And the deadlines "
                  "tighten sharply: the building official has 20&nbsp;business "
                  "days to issue or give written deficiencies — 10 if an "
                  "engineer or architect sealed the affidavit, and just "
                  "<b>5&nbsp;business days</b> for a single-trade review on a "
                  "one- or two-family dwelling — after which the permit is "
                  "<b>deemed approved as a matter of law</b>. Certificates of "
                  "occupancy run to 2&nbsp;business days for a one- or two-family "
                  "dwelling. You must notify the building official in "
                  "writing, on the Commission's form, at permit application "
                  "or by 2:00 p.m. two business days before the first "
                  "inspection.", S["body"]),
    ]))

# ------------------------------------------------------------------- fees
flow += k.h2("FEES: WHAT THEY MAY CHARGE, AND THE ONE YOU CANNOT AVOID")
flow.append(k.body(
    "This kit prints no county fee schedule, because building permit fees, "
    "plan review fees and impact fees are set locally and change. What is "
    "statewide is the <i>rule</i> about them, and it is unusually favorable "
    "to you."))
flow.append(k.bullet(
    "<b>Permit fees may only fund code enforcement.</b> Fees, fines and "
    "related investment earnings “may only be used for carrying out the "
    "local government's responsibilities in enforcing the Florida Building "
    "Code,” and total fee revenue may not exceed the cost of the "
    "allowable activities (s. 553.80(7)(a)). An owner or builder holding a "
    "valid permit issued for a fee <b>may bring a civil action</b> against "
    "the local government to enforce that limit."))
flow.append(k.bullet(
    "<b>Impact fees are the big number</b>, and they are separate from your "
    "permit fee. They may not be collected earlier than the date the "
    "building permit issues (s. 163.31801(4)(e)). Increases are capped: not "
    "more than 50% of the current rate, phased over two or four annual "
    "increments depending on size, and <b>not more than once every four "
    "years</b> (s. 163.31801(6)). Water and sewer connection fees are "
    "<i>not</i> impact fees and are not capped by that section."))
flow.append(k.bullet(
    "<b>A fee increase cannot ambush a pending application.</b> A local "
    "government must give <b>90&nbsp;days' notice</b> before a new or increased "
    "impact fee takes effect, and new or increased fees “may not apply "
    "to current or pending permit applications submitted before the "
    "effective date” unless the change reduces what you owe "
    "(s. 163.31801(4)(d)). Filing before an announced increase locks in the "
    "old rate."))
flow.append(k.bullet(
    "<b>Every local government must publish its schedule.</b> Section "
    "163.31801(13) requires them to report each fee's purpose, the method "
    "used to calculate it, and the amount charged per dwelling type — so ask "
    "for the published impact fee schedule and budget from it."))

# ---------------------------------------------------------------- the set
flow += k.h2_tight("THE DOCUMENT SET — WORK THIS WITH A PEN", reserve=2.0)
flow += k.check_table(
    "What to gather before you file",
    [("Completed building permit application, <b>signed by you in person</b> "
      "at the counter", []),
     ("Owner-builder disclosure statement, signed — plus the separate "
      "electrical disclosure if you will do your own wiring (see FL.1)", []),
     ("Identity verification the county accepts at issuance: driver license "
      "copy, notarized signature, or other", [("Which one:", 1.0)]),
     ("Construction drawings, and a site plan or survey showing the "
      "structure, setbacks and elevations", []),
     ("<b>Product approval schedule</b> — manufacturer, model and FL number "
      "for every exterior window, door, skylight, shutter and roofing "
      "product (Miami-Dade NOA in the HVHZ)",
      [("Department's template obtained:", 1.0)]),
     ("Confirmation in writing of your design wind speed, exposure category, "
      "and <b>whether the parcel is in the windborne debris region</b>",
      [("Vult:", 0.5), ("In region?", 0.5)]),
     ("Truss engineering from the manufacturer's engineer, plus a truss "
      "placement plan", []),
     ("Energy compliance: Form R400-2023 checklist plus either Form "
      "R402-2023 or an approved-software performance report", []),
     ("Flood zone determination; if in a special flood hazard area, the "
      "elevation documentation your floodplain administrator requires",
      [("Flood zone:", 0.6), ("BFE:", 0.4)]),
     ("Septic construction permit or utility sewer availability, and well "
      "permit or water service — see FL.4", []),
     ("Proof of workers' compensation coverage or exemption, if the county "
      "asks for it on the application", []),
     ("Notice of Commencement prepared — recorded before work starts, and "
      "filed with the building department before the first inspection "
      "(see FL.3)", []),
     ],
    notes_header="Notes")

flow.append(Spacer(1, 2))
flow += k.h2_tight("KEEPING THE PERMIT ALIVE", reserve=1.6)
flow.append(k.body(
    "An owner-builder build runs long, and permits die quietly. The code's "
    "administrative chapter sets three clocks worth writing on the wall: an "
    "<b>application</b> is deemed abandoned <b>180&nbsp;days</b> after filing "
    "unless pursued in good faith or a permit issued; a <b>permit</b> becomes "
    "invalid if work is not commenced within <b>6&nbsp;months</b>, or if work is "
    "suspended or abandoned for <b>6&nbsp;months</b>. The rule that saves you is "
    "the definition of active progress: <b>“Work shall be considered to "
    "be in active progress when the permit has received an approved "
    "inspection within 180&nbsp;days.”</b> Get one approved inspection every "
    "six months and the permit stays alive."))
flow.append(k.cite(
    "FBC Building 105.3.2, 105.4.1 and 105.4.1.3. These live in the code's "
    "administrative chapter, not in statute, and are among the provisions a "
    "local government may amend administratively — confirm yours."))

# ----------------------------------------------------------------- record
flow += k.h2_tight("PERMIT RECORD", reserve=2.0)
flow += k.check_table(
    "Fill this in as each permit issues",
    [("Building permit", [("No.:", 0.5), ("Issued:", 0.25),
                          ("Expires:", 0.25)]),
     ("Electrical permit", [("No.:", 0.5), ("Issued:", 0.25),
                            ("Expires:", 0.25)]),
     ("Plumbing permit", [("No.:", 0.5), ("Issued:", 0.25),
                          ("Expires:", 0.25)]),
     ("Mechanical / HVAC permit", [("No.:", 0.5), ("Issued:", 0.25),
                                   ("Expires:", 0.25)]),
     ("Roofing permit", [("No.:", 0.5), ("Issued:", 0.25),
                         ("Expires:", 0.25)]),
     ("Septic (OSTDS) construction permit", [("No.:", 0.5),
                                             ("Issued:", 0.5)]),
     ("Well construction permit", [("No.:", 0.5), ("Issued:", 0.5)]),
     ("Driveway / access permit", [("No.:", 0.5), ("Issued:", 0.5)]),
     ("Notice of Commencement recorded", [("Book/Page:", 0.5),
                                          ("Recorded:", 0.5)]),
     ("Application date-stamped (starts the s. 553.792 clock)",
      [("Date filed:", 0.5), ("Answer due:", 0.5)]),
     ],
    notes_header="Notes")

# ----------------------------------------------------------------- sources
flow += k.h2_tight("SOURCES", reserve=2.0)
flow.append(k.sources_table([
    ("Florida Building Code 8th Edition (2023), effective 31 December 2023; "
     "Residential based on the 2021 IRC, Energy on the 2021 IECC; wind now "
     "on ASCE 7-22", "Florida Building Commission, floridabuilding.org"),
    ("The 9th Edition (2026) is published as a draft with no adopted "
     "effective date", "floridabuilding.org code menu"),
    ("The Commission may adopt an updated NEC outside the three-year cycle",
     "s. 553.73(8)(a)6."),
    ("Local technical amendments must be more stringent, follow a noticed "
     "hearing on evidence of local need, and expire at the next triennial "
     "edition; wind and water intrusion provisions may not be weakened; "
     "flood amendments follow a separate track",
     "s. 553.73(4)(b), (4)(e), (5), (7)(f)"),
    ("The eight product categories requiring statewide approval",
     "s. 553.842(5)"),
    ("Statewide approval precludes local jurisdictions from requiring "
     "further testing or evidence; a building official denying an approved "
     "product must issue a signed written report",
     "s. 553.842(4), (9)"),
    ("Miami-Dade's Product Control Division is a Commission-approved "
     "evaluation entity", "s. 553.842(8)(a)"),
    ("The HVHZ is Broward and Miami-Dade counties, with its own Uniform "
     "Permit Application for roofing",
     "FBC Building Ch. 2 definitions; FBC Building s. 1525"),
    ("Opening protection standards and the wood structural panel exception",
     "FBC Residential R301.2.1.2"),
    ("Maximum building air leakage of 7&nbsp;ACH50; whole-house mechanical "
     "ventilation required below 3&nbsp;ACH50; who may perform the test",
     "FBC Energy Conservation R402.4.1.2"),
    ("Residential plan review in 30&nbsp;business days under 7,500&nbsp;sq&nbsp;ft; "
     "5&nbsp;business days to state deficiencies or the application is deemed "
     "complete; 10% per business day fee reduction, rising to 20% on a "
     "second review", "s. 553.792(1)(a), (c), (e), (f)–(g)"),
    ("Private provider review and inspection, mandatory fee reduction, and "
     "the deemed-approved windows", "s. 553.791(2)(b), (4), (7)(a), (10), (14)"),
    ("Permit and application expiration, and the 180-day approved inspection "
     "that keeps a permit in active progress",
     "FBC Building 105.3.2, 105.4.1, 105.4.1.3"),
    ("Building permit fees may fund only code enforcement, with a private "
     "right of action to enforce that limit", "s. 553.80(7)(a)"),
    ("Impact fees: collection no earlier than permit issuance, increase "
     "caps and frequency limit, 90&nbsp;days' notice, protection for pending "
     "applications, and the duty to publish the schedule",
     "s. 163.31801(4)(d)–(e), (6), (13)"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "fl-permit-kit",
                       "FL.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
