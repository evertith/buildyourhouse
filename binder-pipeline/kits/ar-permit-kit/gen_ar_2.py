#!/usr/bin/env python3
"""AR.2 Permit Application Checklist.

The document that separates what applies to every Arkansas build from what
applies only where a local government created a permit office.

Verified sources:
  Rules Pertaining to Onsite Wastewater Systems, Arkansas State Board of
  Health, effective 5 September 2024 — note the current title DROPS the older
  "Rules and Regulations Pertaining to…" form that legacy forms still use:
    § 4.3     septic approval "prior to construction of a building or residence"
    § 4.1     mandatory sewer connection within 300 feet
    § 4.9.1   the published plan-review fee schedule
    § 4.10.1  Part I "shall be completed by a Designated Representative"
    § 4.10.3  "The system shall not be used until the Permit for Operation is
              issued"
    § 4.7     24 hours' notice before work starts
    § 7.1     two soil pits, primary AND secondary absorption areas, no
              absorption system in fill
    § 8.5     percolation test OR seasonal water table determination
  Ark. Code Ann. § 14-236-104(c)  the 10-acre / 200-foot exemption — present in
              the STATUTE and absent from the 2024 rule, which is why nobody
              finds it
  Ark. Code Ann. § 17-38-103      the state plumbing code as "minimum standards
              statewide in application"
  Ark. Code Ann. § 17-38-204(b),(c),(f)(1)  plumbing permits and inspections
              are MANDATORY where a utility system exists — "shall establish" —
              and the Department may take over where no local inspector exists
  Ark. Code Ann. § 17-28-305(c)   electrical permits are LOCAL OPTION — "may"
  17 CAR § 210-401(a),(b)         Arkansas adopts the 2026 NEC, with its own
              AFCI/GFCI and island-receptacle amendments
  17 CAR § 210-401(f)             "does not include any later amendments or
              editions"
  AFPC Vol. III                   2021 IRC, effective 1 January 2023; the
              deletions table; § R102.5 on appendices; § R105.2 exempt work
  NPDES ARR150000                 the one-acre construction stormwater trigger

DELIBERATELY NOT PRINTED:
  - Any city building-permit fee. Arkansas cities set their own by ordinance and
    the figures rot within a year; the document prints a write-in line instead.
  - Any claim that the septic permit gates the county building permit. State
    rule sequences septic before the residence; whether a county also demands it
    first is a per-county fact.
  - An Arkansas Energy Code edition. AFPC Vol. III deletes IRC Chapter 11 and
    points to the Arkansas Energy Code, but no current landing page or edition
    could be verified in September 2026. The document says so rather than
    printing the widely-repeated "2009 IECC" without a source.
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

FORM_ID = "AR.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "What to Gather"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What to have in hand before you file — starting with the approvals that "
    "apply whether or not anybody issues building permits where you are.")

flow.append(k.disclaimer(
    "Fees and code editions were read at their source in September 2026 and "
    "change on their own schedule."))
flow.append(Spacer(1, 10))

# ------------------------------------------------- what always applies
flow += k.h2_tight("WHAT APPLIES WHEREVER YOU BUILD", reserve=2.0)
flow.append(k.body(
    "Work this list first. None of it depends on whether your city or county "
    "issues building permits, and two items on it can stop a build outright."))
rows = [
    [k.cellp("<b>Onsite wastewater permit</b>"),
     k.cellp("Arkansas Department of Health, through the Environmental Health "
             "Specialist at your county health unit. Required before the "
             "residence is built, and the design must be done by a licensed "
             "Designated Representative"),
     k.cellp("Onsite Wastewater<br/>Rules § 4.3, § 4.10.1")],
    [k.cellp("<b>The state plumbing code</b>"),
     k.cellp("Adopted as \"minimum standards <b>statewide in application</b>… "
             "to all types of buildings, private or public, <b>rural or "
             "urban</b>.\" There is no rural exemption from the standard "
             "itself"),
     k.cellp(sec("17-38-103"))],
    [k.cellp("<b>Plumbing permits and inspections</b>"),
     k.cellp("<b>Mandatory</b> — not optional — wherever a water, sewer or gas "
             "utility system exists. Such a body \"<b>shall establish</b> a "
             "system of permits and inspections.\" Contrast the electrical "
             "rule below"),
     k.cellp(sec("17-38-204(c)"))],
    [k.cellp("<b>The 2026 National Electrical Code</b>"),
     k.cellp("Adopted statewide as \"the standard for the construction, "
             "installation, repair, and maintenance of electrical "
             "facilities.\" The <i>standard</i> binds you everywhere; the "
             "<i>permit</i> may not exist"),
     k.cellp("17 CAR § 210-401")],
    [k.cellp("<b>Well construction standards</b>"),
     k.cellp("If you drill, the technical rules bind you even when the "
             "license requirement does not — casing, grouting, sealing, "
             "disinfection, separation. <b>There is no well permit and no "
             "notice of intent</b>"),
     k.cellp(f"17 CAR pt. 11<br/>{sec('17-50-107(a)')}")],
    [k.cellp("<b>Floodplain development permit</b>"),
     k.cellp("Administered locally even where no building department exists — "
             "frequently by the county Office of Emergency Management. If you "
             "are outside the flood hazard area you may still need a document "
             "saying so"),
     k.cellp("Local ordinance under<br/>the NFIP")],
    [k.cellp("<b>Utility locate before digging</b>"),
     k.cellp("Free, and the step before footings, septic, water line or "
             "driveway cut. Arkansas 811"),
     k.cellp("ar811.org")],
]
flow.append(k.ref_table(
    "The list that does not care what county you are in",
    [k.cellp("Item", bold=True), k.cellp("What it is", bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.5 * inch, CW - 3.15 * inch, 1.65 * inch]))
flow.append(k.cite(
    "Note the asymmetry, because it is real and it surprises people: Arkansas "
    "makes plumbing permitting <b>mandatory</b> where a utility system exists "
    f"(\"shall establish\", {sec('17-38-204(c)')}) while making electrical "
    f"permitting <b>optional</b> (\"Any city or county <i>may</i> establish… a "
    f"system of permits and inspections\", {sec('17-28-305(c)')}). Where a "
    f"utility system exists but no local plumbing inspector has been provided, "
    f"the Department of Health \"may take immediate charge and entire control "
    f"of the plumbing inspection program\" ({sec('17-38-204(f)(1)')})."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "One rule that can delete your septic system entirely", [
        Paragraph("If a sanitary sewer is within <b>300 feet</b> of the point "
                  "where the sewer leaves your building, and the connection "
                  "can be made without crossing someone else's property, "
                  "connection is mandatory and no onsite system may be used "
                  "(Onsite Wastewater Rules § 4.1). Separately, a septic "
                  "permit \"shall be refused\" where community sewerage is "
                  "reasonably available or economically feasible "
                  f"({sec('14-236-113(b)')}). Measure this before you budget "
                  f"for a septic system.", S["body"]),
    ]))

# ------------------------------------------------- the sequence
flow += k.h2_tight("THE ONE SEQUENCE ARKANSAS FIXES IN RULE", reserve=1.8)
flow.append(k.body(
    "Most of the order of an Arkansas build is yours to choose. One step is "
    "not. The onsite wastewater rule puts the septic approval <b>before the "
    "house</b>, in terms, and it does so independently of anything your county "
    "does:"))
flow.append(k.callout(
    "Onsite Wastewater Rules § 4.3", [
        Paragraph("\"A completed Onsite Wastewater System Permit Application "
                  "and detailed plans and specifications… shall be submitted "
                  "to and receive the approval of the Arkansas Department of "
                  "Health or its Authorized Agent, <b>prior to construction of "
                  "a building or residence</b>.\"", S["body"]),
    ]))
flow.append(k.body(
    "That is also practical advice rather than mere paperwork. The absorption "
    "field and its reserve area have to fit, with their setbacks, on the same "
    "parcel as the house and the well — so the septic design constrains where "
    "the house can sit. Settle it before you fix the footprint, not after."))

flow += k.h2_tight("THE SEPTIC PACKAGE, IN ORDER", reserve=1.6)
flow += k.check_table(
    "Work these in sequence — this is the longest pole on a rural build",
    [
        ("Engage a licensed <b>Designated Representative</b>. You cannot "
         "design the system yourself: Part I \"shall be completed by a "
         "Designated Representative\" (§ 4.10.1). Find one through the county "
         "health unit or the state's licensee lookup.",
         [("DR name", 0.6), ("Date", 0.4)]),
        ("<b>Site and soil evaluation.</b> A minimum of <b>two soil pits</b> "
         "is required — one in the proposed primary absorption area, one in "
         "the secondary — and they \"shall be left open for use by the "
         "Authorized Agent\" (§ 7.1).", [("Date", 1.0)]),
        "Confirm you have BOTH a primary and a secondary (reserve) absorption "
        "area. Every design requires both, so a lot needs roughly twice the "
        "suitable soil area buyers expect (§ 4.2, § 7.1).",
        "Note which evaluation was used: Arkansas rates soil morphology first, "
        "and a percolation test is an option rather than the default "
        "(§ 8.5). No absorption system may be installed in fill (§ 7.1).",
        ("<b>Part I — Permit for Construction</b> issued by the Environmental "
         "Health Specialist. Valid one year; must be revalidated if older "
         "(§ 4.9).", [("Permit no.", 0.55), ("Issued", 0.45)]),
        ("Notify the Authorized Agent <b>at least 24 hours</b> before starting "
         "work (§ 4.7).", [("Date notified", 1.0)]),
        ("<b>Part II — installation inspection.</b> Documentation reaches the "
         "local health unit within 5 days (§ 4.10.2).",
         [("Date", 0.5), ("Result", 0.5)]),
        ("<b>Part III — Permit for Operation.</b> \"The system shall not be "
         "used until the Permit for Operation is issued\" (§ 4.10.3).",
         [("Issued", 1.0)]),
    ])
flow.append(Spacer(1, 2))
rows = [
    [k.cellp("1,500 sq ft or less"), k.cellp("$30", center=True)],
    [k.cellp("Over 1,500 up to 2,000 sq ft"), k.cellp("$45", center=True)],
    [k.cellp("Over 2,000 up to 3,000 sq ft"), k.cellp("$90", center=True)],
    [k.cellp("Over 3,000 up to 4,000 sq ft"), k.cellp("$120", center=True)],
    [k.cellp("Over 4,000 sq ft"), k.cellp("$150", center=True)],
    [k.cellp("Alteration, repair or extension"), k.cellp("$30", center=True)],
]
flow.append(k.ref_table(
    "Septic plan-review fee — one of the few figures Arkansas publishes",
    [k.cellp("Conditioned structure size", bold=True),
     k.cellp("Fee", bold=True, center=True)],
    rows, [CW - 1.5 * inch, 1.5 * inch]))
flow.append(k.cite(
    "Onsite Wastewater Rules § 4.9.1. Square footage excludes garages, "
    "carports and porches (§ 4.9.2.1). A fee waiver exists for low-income "
    "applicants under Act 725 of 2021 (§ 3.5 to § 3.6). Designated "
    "Representative and installer licenses are $100 a year (§ 13.1, § 14)."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "The 10-acre exemption — real, current, and missing from the rule book", [
        Paragraph("Ark. Code Ann. § 14-236-104(c): \"<b>The requirements of "
                  "this chapter shall not apply to any individual sewage "
                  "disposal system or alternate and experimental system which "
                  "is situated on a tract of land ten (10) acres or larger, in "
                  "which the field line or sewage disposal line is no closer "
                  "than two hundred feet (200′) to the property line.</b>\"",
                  S["body"]),
        Paragraph("<b>Both conditions have to be met.</b> Ten acres or more, "
                  "<i>and</i> every part of the system at least 200 feet from "
                  "every property line — the Department's own published "
                  "guidance adds \"<b>including roads</b>\", and says the "
                  "exemption applies to a single residence. On a square "
                  "ten-acre tract that leaves an envelope of roughly 260 feet "
                  "a side. On a long narrow ten acres it may be geometrically "
                  "impossible.", S["body"]),
        Paragraph("<b>Why your county health unit may never have heard of "
                  "it:</b> the exemption lives only in the statute. It is not "
                  "restated anywhere in the 2024 rule — searching the rule for "
                  "\"ten (10) acres\" or \"two hundred feet\" finds nothing. "
                  "Cite the statute, not the rule.", S["body"]),
        Paragraph("<b>What it does not do.</b> It does not license a bad "
                  "system. The Department may still act where a system is a "
                  "health hazard or a nuisance (§ 14-236-104(b)), and the "
                  "state's own guidance says the owner must still install and "
                  "operate it to meet state requirements. A municipality may "
                  "impose stricter local rules (§ 14-236-105). And an "
                  "unpermitted system is a real problem at resale, appraisal "
                  "and mortgage underwriting — which is a good reason to "
                  "permit one anyway.", S["body"]),
    ]))

# ------------------------------------------------- codes
flow += k.h2_tight("THE CODE EDITIONS ACTUALLY IN FORCE", reserve=1.8)
rows = [
    [k.cellp("<b>Building — one- and two-family</b>"),
     k.cellp("Arkansas Fire Prevention Code, 2021 Edition, <b>Volume III</b> — "
             "the 2021 International Residential Code with Arkansas amendments"),
     k.cellp("1 Jan 2023", center=True)],
    [k.cellp("<b>Building — other</b>"),
     k.cellp("AFPC Volume II — 2021 International Building Code"),
     k.cellp("1 Jan 2023", center=True)],
    [k.cellp("<b>Fire</b>"),
     k.cellp("AFPC Volume I — 2021 International Fire Code"),
     k.cellp("1 Jan 2023", center=True)],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("<b>2026 National Electrical Code</b> (NFPA 70), adopted by the "
             "Board of Electrical Examiners with Arkansas amendments — see "
             "below"),
     k.cellp("17 CAR<br/>§ 210-401", center=True)],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp("Arkansas State Plumbing Code. The AFPC deletes the IRC plumbing "
             "chapters outright and points here"),
     k.cellp(sec("17-38-103"), center=True)],
    [k.cellp("<b>Fuel gas</b>"),
     k.cellp("Arkansas State Gas Code. IRC Chapter 24 deleted in its entirety"),
     k.cellp("AFPC Vol. III", center=True)],
    [k.cellp("<b>Mechanical</b>"),
     k.cellp("\"the mechanical code for Arkansas\", per the AFPC's own "
             "cross-reference table"),
     k.cellp("AFPC Vol. III", center=True)],
    [k.cellp("<b>Energy</b>"),
     k.cellp("Arkansas Energy Code. IRC Chapter 11 is deleted in its entirety "
             "and replaced by a pointer. <b>Confirm the current edition with "
             "your jurisdiction</b> — see the note below"),
     k.cellp("AFPC Vol. III", center=True)],
]
flow.append(k.ref_table(
    "What binds a house in Arkansas",
    [k.cellp("Trade", bold=True), k.cellp("Code and edition", bold=True),
     k.cellp("Effective / cite", bold=True, center=True)],
    rows, [1.55 * inch, CW - 2.8 * inch, 1.25 * inch]))
flow.append(k.cite(
    "The Arkansas Fire Prevention Code, 2021 Edition is state rule 015.01.22 "
    "Ark. Code R. 005, effective 1 January 2023, and reads free at "
    "codes.iccsafe.org/codes/arkansas. <b>We have deliberately not printed an "
    "Arkansas Energy Code edition.</b> The figure repeated across the web is a "
    "2009 IECC base, but no current adopting document or agency landing page "
    "could be verified in September 2026 — and a wrong insulation table is "
    "worse than a blank one. Ask your building official, or the Department of "
    "Energy and Environment, and write the answer on the line below."))

flow.append(Spacer(1, 2))
flow += k.check_table(
    "Confirm the two editions this kit will not guess at",
    [
        ("Arkansas Energy Code edition in force for my build, and who told me:",
         [("Edition", 0.45), ("Source", 0.55)]),
        ("Whether my jurisdiction has adopted anything <b>more stringent</b> "
         "than the AFPC, which it may do — but only by amending the AFPC "
         "itself (Vol. I § 101.2.2):", [("Answer", 1.0)]),
    ])

flow += k.h2_tight("WHAT ARKANSAS DELETED FROM THE RESIDENTIAL CODE",
                   reserve=1.8)
flow.append(k.body(
    "This table is worth more than it looks. Arkansas struck whole blocks out "
    "of the 2021 IRC and replaced them with pointers to separate Arkansas "
    "codes. <b>If you quote an IRC chapter number from a national source "
    "without checking this list, you can print a requirement that does not "
    "exist in Arkansas — or miss one that does.</b>"))
rows = [
    [k.cellp("Chapter 11 — Energy Efficiency"),
     k.cellp("\"Deleted in its entirety. Refer to the Arkansas Energy Code.\"")],
    [k.cellp("Chapter 24 — Fuel Gas"),
     k.cellp("\"Deleted in its entirety. Refer to the Arkansas State Gas "
             "Code.\"")],
    [k.cellp("Chapters 25–33 — all plumbing"),
     k.cellp("\"Deleted in its entirety. Refer to the Arkansas State Plumbing "
             "Code.\"")],
    [k.cellp("Chapters 34–43 — all electrical"),
     k.cellp("\"Delete Chapter and refer to the National Electrical Code… as "
             "adopted by the Arkansas Board of Electrical Examiners.\"")],
    [k.cellp("<b>Every appendix</b>"),
     k.cellp("\"Deleted in its entirety.\" § R102.5 confirms: appendices "
             "\"are NOT adopted by the State of Arkansas and shall not apply "
             "<b>unless adopted by local ordinance</b>\"")],
]
flow.append(k.ref_table(
    "Struck from AFPC Volume III",
    [k.cellp("IRC content", bold=True),
     k.cellp("Arkansas treatment", bold=True)],
    rows, [2.05 * inch, CW - 2.05 * inch]))
# A callout placed straight after a titled_table butts its top border against
# the table's bottom border with no gap at all, which reads as one broken box.
# Every other callout in the kit follows a cite() or body(), which bring their
# own spaceBefore.
flow.append(Spacer(1, 8))
flow.append(k.callout(
    "The appendix deletion has teeth if you are building anything unusual", [
        Paragraph("Because every appendix is struck, Arkansas has <b>not</b> "
                  "adopted the IRC appendices for <b>tiny houses</b>, "
                  "strawbale, cob, light straw-clay, 3D-printed construction, "
                  "solar-ready provisions, radon control, or private sewage "
                  "disposal. There is no state code path for those methods — a "
                  "local jurisdiction would have to adopt the appendix by "
                  "ordinance. If you are planning an alternative-construction "
                  "build, that is the conversation to have with your building "
                  "official before you draw anything.", S["body"]),
    ]))

# ------------------------------------------------- NEC
flow += k.h2_tight("THE 2026 NEC — AND THE PARTS ARKANSAS REWROTE",
                   reserve=2.0)
flow.append(k.body(
    "Arkansas is on a <b>newer</b> electrical code than most of the country, "
    "not an older one. The Board of Electrical Examiners \"adopts and "
    "incorporates herein the National Electrical Code, <b>2026 edition</b>,\" "
    "and makes it \"the standard for the construction, installation, repair, "
    "and maintenance of electrical facilities and the performance of "
    "electrical work.\" But it did not adopt it clean — and the amendments "
    "land squarely on things you will wire in a kitchen and a laundry."))
rows = [
    [k.cellp("<b>AFCI and GFCI over 130 volts</b>"),
     k.cellp("\"shall <b>not</b> be required on dwelling units circuits over "
             "130&#160;volts, except for the requirements in Article 680 and "
             "682\" "
             "— that is, except pools, spas and similar water installations"),
     k.cellp("§ 210-401(b)(2)")],
    [k.cellp("<b>Laundry areas</b>"),
     k.cellp("AFCI/GFCI \"shall not apply\" in a dwelling unit laundry area — "
             "<b>except</b> for convenience outlets within <b>six feet</b> of "
             "a sink"),
     k.cellp("§ 210-401(b)(3)(A)")],
    [k.cellp("<b>Refrigerator, microwave</b>"),
     k.cellp("AFCI/GFCI \"shall not apply\" to a refrigerator or microwave "
             "appliance within a dwelling unit"),
     k.cellp("§ 210-401(b)(3)(B)")],
    [k.cellp("<b>Island and peninsula receptacles</b>"),
     k.cellp("At least one receptacle outlet within the island or peninsula "
             "for the first <b>9 sq ft</b> of countertop or work surface, one "
             "more for each additional <b>18 sq ft</b>, and at least one "
             "within <b>two feet</b> of the outer end of a peninsula. A "
             "peninsula is measured from the connected perpendicular wall"),
     k.cellp("§ 210-401(b)(4),(5)")],
]
flow.append(k.ref_table(
    "Arkansas amendments to the 2026 NEC, in 17 CAR § 210-401",
    [k.cellp("What", bold=True), k.cellp("What Arkansas says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.55 * inch, CW - 3.05 * inch, 1.5 * inch]))
flow.append(k.cite(
    "Read from the Board of Electrical Examiners' own published administrative "
    "rules, 17 CAR Part 210, September 2026. Two further points from the same "
    "section: the Board also adopts ANSI/NECA 1-2023, <i>Standard Practices "
    "for Good Workmanship in Electrical Contracting</i>, as the workmanship "
    "standard (§ 210-401(e)); and the adoption \"does not include any later "
    "amendments or editions of the standards incorporated by reference\" "
    "(§ 210-401(f)), so a newer NEC does not take effect in Arkansas until the "
    "Board adopts it after notice and hearing. <b>Confirm the edition before "
    "you buy a code book</b> — this is the item in the kit most likely to move."))

# ------------------------------------------------- stormwater + local
flow += k.h2_tight("STORMWATER — THE ONE-ACRE TEST", reserve=1.6)
flow.append(k.body(
    "Most single house sites fall below the threshold and need nothing. Run "
    "the test rather than assuming, because the acre counts <b>total "
    "disturbance</b> — house, driveway, septic field, pad and any pond — and "
    "because a lot inside a larger development can be swept in by the common-"
    "plan rule even when your own disturbance is under an acre."))
rows = [
    [k.cellp("Under 1 acre disturbed, not part of a larger common plan"),
     k.cellp("<b>No permit.</b> Below the threshold")],
    [k.cellp("1 acre up to 5 acres"),
     k.cellp("Automatic coverage under the construction general permit; "
             "required documents posted on site before work begins")],
    [k.cellp("5 acres or more"),
     k.cellp("Notice of Intent filed through the state e-filing system")],
]
flow.append(k.ref_table(
    "Arkansas construction general permit ARR150000",
    [k.cellp("Total disturbed area", bold=True),
     k.cellp("What it means for you", bold=True)],
    rows, [2.55 * inch, CW - 2.55 * inch]))
flow.append(k.cite(
    "Permit ARR150000, issued by the Division of Environmental Quality within "
    "the Arkansas Department of Energy and Environment. <b>A version boundary "
    "falls inside this kit's first year:</b> the permit effective 1 November "
    "2021 expires 31 October 2026, and the reissued permit runs 1 November "
    "2026 to 31 October 2031. Check which one governs the date you break "
    "ground. Note also that the agency is now the Division of Environmental "
    "Quality, not the former Arkansas Department of Environmental Quality, "
    "though its documents and web address still carry the old name."))

flow += k.h2_tight("IF A BUILDING PERMIT DOES EXIST WHERE YOU ARE",
                   reserve=1.6)
flow.append(k.body(
    "Arkansas cities set their own application requirements and their own fees "
    "by ordinance, and both move. Rather than print figures that will be wrong "
    "by the time you read them, here is the list to take to the counter — and "
    "room to write down what they actually tell you."))
flow += k.check_table(
    "Ask the permit counter for each of these, and write the answer",
    [
        ("Application form, and whether an owner-builder may sign it",
         [("Answer", 1.0)]),
        ("Plan requirements — how many sets, what scale, whether a sealed "
         "design is required", [("Answer", 1.0)]),
        ("Site plan requirements and the setbacks that apply to my lot, in "
         "writing", [("Front", 0.25), ("Rear", 0.25), ("Sides", 0.5)]),
        ("Building permit fee and how it is calculated",
         [("Fee", 0.4), ("Basis", 0.6)]),
        ("Plan review fee", [("Fee", 1.0)]),
        ("Separate trade permits — which of electrical, plumbing, mechanical "
         "and gas this office issues, and which come from elsewhere",
         [("Answer", 1.0)]),
        ("Whether the office requires the ADH septic permit before it will "
         "issue the building permit", [("Answer", 1.0)]),
        ("Impact, tap, meter and connection fees",
         [("Total", 0.35), ("What for", 0.65)]),
        ("Certificate of occupancy — whether one is issued, and what it "
         "requires", [("Answer", 1.0)]),
        ("Whether a homeowner may pull trade permits, and any competency "
         "demonstration required under § 17-28-305(b)(2)",
         [("Answer", 1.0)]),
    ])

# ------------------------------------------------- permit record
flow += k.h2_tight("PERMIT RECORD — FILL THIS IN AS EACH ONE ISSUES",
                   reserve=1.6)
flow += k.check_table(
    "Every approval on this build",
    [
        ("Onsite wastewater — Permit for Construction (Part I)",
         [("No.", 0.5), ("Issued", 0.5)]),
        ("Onsite wastewater — Permit for Operation (Part III)",
         [("No.", 0.5), ("Issued", 0.5)]),
        ("Well construction report, if a well was drilled — demand your copy",
         [("Date filed", 1.0)]),
        ("Floodplain development permit, or exemption certificate",
         [("No.", 0.5), ("Issued", 0.5)]),
        ("Driveway or access permit — state highway or county road",
         [("Issued by", 0.6), ("Date", 0.4)]),
        ("911 address assignment", [("Address", 0.7), ("Date", 0.3)]),
        ("Building permit, if one exists here",
         [("No.", 0.5), ("Issued", 0.5)]),
        ("Electrical permit, if one exists here",
         [("No.", 0.5), ("Issued", 0.5)]),
        ("Plumbing permit", [("No.", 0.5), ("Issued", 0.5)]),
        ("Mechanical / gas permit", [("No.", 0.5), ("Issued", 0.5)]),
        ("Stormwater coverage, if the site disturbs an acre or more",
         [("Ref.", 0.5), ("Date", 0.5)]),
        ("Certificate of occupancy, if one is issued here",
         [("No.", 0.5), ("Issued", 0.5)]),
    ],
    notes_header="Notes")
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ar-permit-kit",
                       "AR.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
