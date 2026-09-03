#!/usr/bin/env python3
"""OH.5 Forms & Documents Index.

Every document an Ohio owner-builder will meet, named as the agency names it,
with where it comes from and when. Plus two sections the other documents cannot
carry:

  - RCO 102.10, the work Ohio exempts from approval outright, reproduced as the
    code lists it. This is the section readers come back to for years, because
    it settles the shed / fence / deck / retaining wall questions with numbers.
    Note the four-part deck test in item 9: 200 square feet AND under 30 inches
    AND not attached AND not serving the required exit door. Fail any one and
    the deck needs approval.

  - The contract and lien documents, which on an owner-built house have nobody
    to come from. As your own general contractor you are the party who would
    normally receive these; nobody hands them to you, so they have to be on a
    list somewhere. This is that list.

Verified sources:
  OAC 4101:8-1-01 102.10        work exempt from approval, quoted
  OAC 4101:8-1-01 102.10.1, .2  emergency repairs and minor repairs
  OAC 4101:8-1-01 105.1, 105.3  approvals required; expiration
  OAC 4101:8-1-01 106.1         submittal documents
  R.C. 3791.04(A)(2)(b)         no seal required for a residential plan set
  R.C. 4722.02(A)               the nine mandatory contract contents
  R.C. 1311.011(B)(4),(6),(7)   the contractor's affidavit and joint checks
  R.C. 1311.06(B)               60 days for 1-2 family, 75 days otherwise
  R.C. 1311.04(O), 1311.05(E)   no Notice of Commencement for a home
                                construction contract
  OAC 3701-29-09(F)             the septic as-built drawing
  OAC 3701-28-03(B)             the private water system site plan contents

DELIBERATELY NOT PRINTED:
  - Any form number. Ohio's building and health forms are local and
    renumbered constantly; naming the DOCUMENT is durable, naming the form is
    not.
  - Any statement that a detached garage or pole barn is or is not exempt.
    R.C. 3781.06(C)(11) defines an accessory structure as an ATTACHED one,
    while the RCO's own exempt list speaks of detached accessory structures
    under 200 sq ft. The interaction is genuinely unresolved and the document
    sends the reader to ask rather than guessing.
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

FORM_ID = "OH.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Forms & Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document you will meet — what it is, when, and from where — plus "
    "the work Ohio exempts from approval outright.")

flow.append(k.disclaimer(
    "Documents are named as the rules and statutes name them. Local form "
    "numbers change constantly and are deliberately absent."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- state docs
flow += k.h2_tight("THE DOCUMENTS THAT EXIST WHEREVER YOU BUILD", reserve=2.2)
flow.append(k.body(
    "None of these depends on whether a building department is certified for "
    "your parcel. On a rural Ohio build this list is the whole of your "
    "paperwork."))
rows = [
    [k.cellp("<b>Soil evaluation report</b>"),
     k.cellp("A certified soil scientist, an equivalently registered soil "
             "professional, or the health district's own registered sanitarian "
             f"(OAC {k.rule('3701-29-07(A)')})"),
     k.cellp("Before design. You may not produce this yourself")],
    [k.cellp("<b>Sewage system design and site drawing</b>"),
     k.cellp("Your designer — no professional engineer required by Ohio rule"),
     k.cellp("Must show both the system and the replacement area meeting every "
             "isolation distance, and the field staked on site")],
    [k.cellp("<b>Sewage system installation permit</b>"),
     k.cellp("Local board of health"),
     k.cellp("Before any installation work")],
    [k.cellp("<b>Sewage system as-built drawing</b>"),
     k.cellp("Your registered installer, signed"),
     k.cellp(f"After installation. Records any change in component locations "
             f"and the distances to everything with an isolation requirement "
             f"(OAC {k.rule('3701-29-09(F)')}). Keep your copy")],
    [k.cellp("<b>Sewage system operation permit</b>"),
     k.cellp("Local board of health"),
     k.cellp("Issued on approval of the installation. Term set by your board, "
             f"capped at ten{NB}years — diarize the expiry")],
    [k.cellp("<b>Private water system permit</b>"),
     k.cellp("Local board of health"),
     k.cellp("Before drilling. The application includes a site plan showing "
             "distances to a long list of features")],
    [k.cellp("<b>Water sample result</b>"),
     k.cellp("Laboratory, through the health district"),
     k.cellp("The permit fee includes at least one sample")],
    [k.cellp("<b>Well log / drilling report</b>"),
     k.cellp("Your driller files it with the Department of Natural Resources"),
     k.cellp("Separate from the health district's permit — do not conflate the "
             "two. Ask your driller for a copy")],
    [k.cellp("<b>Zoning certificate</b>"),
     k.cellp("Township, county or municipality"),
     k.cellp("Where zoning has been adopted. Independent of the building code "
             "entirely")],
    [k.cellp("<b>Lot line survey</b>"),
     k.cellp("A surveyor"),
     k.cellp("Before any work if a building department has jurisdiction — and "
             "worth doing either way, since every setback you must meet is "
             "measured from a boundary")],
    [k.cellp("<b>Driveway or access permit</b>"),
     k.cellp("Department of Transportation district, county engineer, or "
             "township trustees"),
     k.cellp("Decided by which road you touch")],
    [k.cellp("<b>Notice of Intent, construction stormwater</b>"),
     k.cellp("Ohio EPA, Division of Surface Water"),
     k.cellp("Only at one acre of disturbance, or less inside a larger common "
             "plan of development")],
    [k.cellp("<b>Utility locate ticket</b>"),
     k.cellp("Ohio 811"),
     k.cellp("Before any excavation. Free")],
]
flow.append(k.ref_table(
    "State and county-level documents",
    [k.cellp("Document", bold=True), k.cellp("From whom", bold=True),
     k.cellp("When, and what to watch", bold=True)],
    rows, [1.6 * inch, 1.5 * inch, CW - 3.1 * inch]))

# ---------------------------------------------------------------- local docs
flow += k.h2_tight("THE DOCUMENTS THAT EXIST ONLY IF SOMEBODY IS CERTIFIED",
                   reserve=1.8)
flow.append(k.body(
    "Every item below comes from a building department certified for "
    "residential buildings. Where none has jurisdiction over your parcel, none "
    "of these documents exists — and no state office can issue them to you "
    "instead."))
flow += k.check_table(
    "Building-department documents, in the order you meet them",
    [
        ("<b>Residential construction documents</b> — the plan set. "
         "<b>No architect's or engineer's seal is required</b> for a "
         "residential building (§&#160;3791.04(A)(2)(b)).",
         [("Submitted", 1.0)]),
        ("<b>Certificate of plan approval.</b> Ask for the required-inspection "
         "list at the same time — the code says the official shall give it to "
         "you when this issues.", [("No.", 0.5), ("Date", 0.5)]),
        ("<b>The required-inspection list</b> for this project, drawn from RCO "
         "sections 108.2.1 to 108.2.12.", [("Received", 1.0)]),
        ("<b>On-site inspection record</b> — the inspector notes each "
         "satisfactory inspection on it. Keep it on site and keep it "
         "afterwards.", [("Held by", 1.0)]),
        ("<b>Amended construction documents</b>, if substantive changes are "
         "made after approval (RCO 106.3).", [("Date", 1.0)]),
        ("<b>Conditional approval to proceed</b>, if the department objects to "
         "part of the plans and the objection is an interpretation rather than "
         "a technical requirement (§&#160;3791.04(G)).", [("Date", 1.0)]),
        ("<b>Extension requests</b> — approval dies if work has not started "
         "within twelve&#160;months or is idle more than six&#160;months. Each "
         "extension must be requested at least ten&#160;days before expiry "
         "(§&#160;3791.04(C)).",
         [("Requested", 0.5), ("Granted", 0.5)]),
        ("<b>Certificate of occupancy.</b> Only a certified department can "
         "issue it — not a third-party inspector (§&#160;3781.10(E)(15)).",
         [("No.", 0.5), ("Date", 0.5)]),
        ("<b>Adjudication order</b>, if anything is denied — it must specify "
         "its reasons, and it starts your appeal clock.", [("Date", 1.0)]),
    ])

# ---------------------------------------------------------------- exempt
flow += k.h2_tight("WHAT NEEDS NO APPROVAL AT ALL", reserve=2.2)
flow.append(k.body(
    f"The RCO lists this itself, and the list is worth keeping. Read the "
    f"opening line carefully, because it is the part people forget: "
    f"<b>exemption from approval is not exemption from the code.</b>"))
flow.append(k.callout(
    f"OAC {k.rule('4101:8-1-01')}, RCO section 102.10 — the opening sentence",
    [
        Paragraph("\"Work exempt from approval. Approval shall not be required "
                  "for the following work; <b>however, this work shall comply "
                  "with all applicable provisions of the rules of the "
                  "board</b>.\"", S["body"]),
    ]))
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp("One-story detached accessory structures used as tool and storage "
             f"sheds, playhouses and similar uses, \"provided the floor area "
             f"does not exceed <b>two hundred square feet</b>\", and "
             f"playground structures")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp(f"Fences not over <b>six{NB}feet</b> high")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp(f"Retaining walls not over <b>four{NB}feet</b> in height "
             f"\"measured from the bottom of the footing to the top of the "
             f"wall, <b>unless supporting a surcharge</b>\"")],
    [k.cellp("<b>4</b>", center=True),
     k.cellp(f"Water tanks supported directly on grade, capacity not over "
             f"<b>five thousand gallons</b>, with a height-to-width ratio not "
             f"over two to one")],
    [k.cellp("<b>5</b>", center=True),
     k.cellp(f"Sidewalks and driveways not more than <b>thirty{NB}inches</b> "
             f"above grade, not over a basement or story below, and not part "
             f"of an accessible route")],
    [k.cellp("<b>6</b>", center=True),
     k.cellp("\"Painting, papering, tiling, carpeting, cabinets, counter tops "
             "and similar finish work\"")],
    [k.cellp("<b>7</b>", center=True),
     k.cellp("Swings and other playground equipment accessory to a one-, two- "
             "or three-family dwelling")],
    [k.cellp("<b>8</b>", center=True),
     k.cellp(f"Window awnings supported by an exterior wall, projecting not "
             f"more than <b>fifty-four{NB}inches</b> and needing no additional "
             f"support")],
    [k.cellp("<b>9</b>", center=True),
     k.cellp(f"<b>Decks</b> — and all four conditions must hold: not exceeding "
             f"<b>200 square{NB}feet</b>, <b>not more than thirty{NB}inches</b> "
             f"above grade at any point, <b>not attached</b> to a dwelling, "
             f"and <b>not serving the exit door</b> required by section 311.2")],
    [k.cellp("<b>10</b>", center=True),
     k.cellp("Above-ground storage tanks as defined in the RCO's definitions "
             "chapter, and their foundations")],
    [k.cellp("<b>11</b>", center=True),
     k.cellp("Battery-operated smoke or carbon monoxide alarms installed in "
             "existing buildings where no construction is taking place")],
]
flow.append(k.ref_table(
    "RCO 102.10, Building — reproduced as the code lists it",
    [k.cellp("", bold=True, center=True),
     k.cellp("Work exempt from approval", bold=True)],
    rows, [0.35 * inch, CW - 0.35 * inch]))
flow.append(k.cite(
    f"<b>The deck test is the one to read twice.</b> Four conditions, joined "
    f"by \"and\" — fail any one and the deck needs approval. A "
    f"180-square-foot deck twenty inches off the ground that happens to be "
    f"bolted to the house is <i>not</i> exempt, and neither is a free-standing "
    f"one you step onto from the required exit door. <b>And note what "
    f"exemption from approval does not do:</b> an exempt deck still has to "
    f"meet the code's structural, guard and ledger provisions. Nobody checks "
    f"— the requirement remains."))
flow.append(Spacer(1, 4))
flow.append(k.body(
    "The same section carries shorter exempt lists for the trades. In outline: "
    "<b>Electrical</b> — cord-and-plug temporary decorative lighting, "
    "reinstalling attachment plug receptacles but not their outlets, replacing "
    "branch-circuit overcurrent devices of the same capacity and type in the "
    "same location, wiring operating at less than twenty-five volts and "
    "incapable of supplying more than fifty watts, and minor repair work such "
    "as replacing lamps. <b>Gas and mechanical</b> — portable heating, cooking "
    "and clothes-drying appliances, portable ventilation and cooling "
    "equipment, and replacing any minor part that does not alter the "
    "equipment's approval or make it unsafe. <b>Plumbing</b> — repairing "
    "leaks, and clearing stoppages or repairing leaks in pipes, valves or "
    "fixtures including removing and reinstalling water closets, \"provided "
    "such repairs do not involve or require the replacement of more than one "
    "fixture or rearrangement of valves, pipes or fixtures.\""))
flow.append(k.callout_long(
    "Three qualifications on that list", [
        Paragraph("<b>Replacing a defective concealed pipe is new work.</b> "
                  "The plumbing exemption says so in terms: if a concealed "
                  "trap, drain, water, soil, waste or vent pipe \"becomes "
                  "defective and it becomes necessary to remove and replace "
                  "the same with new material, such work <b>shall be "
                  "considered as new work</b> and an approval shall be "
                  "obtained and inspection made.\"", S["body"]),
        Paragraph("<b>Emergency repairs are deferred, not excused.</b> Where "
                  "equipment replacement or repair must happen in an "
                  "emergency, \"an application for approval shall be submitted "
                  "<b>within the next working business day</b>\" (RCO "
                  "102.10.1).", S["body"]),
        Paragraph("<b>\"Minor repairs\" has a hard boundary.</b> RCO 102.10.2 "
                  "allows minor repairs without application or notice, then "
                  "excludes \"the cutting away of any wall, partition or "
                  "portion thereof, the removal or cutting of any structural "
                  "beam or load bearing support, or the removal or change of "
                  "any required means of egress\" — and any addition, "
                  "alteration, replacement or relocation of water supply, "
                  "sewer, drainage, gas, soil, waste or vent piping, electric "
                  "wiring, or mechanical work affecting public health or "
                  "general safety.", S["body"]),
    ]))
flow.append(k.cite(
    f"<b>One thing this list does not settle:</b> a detached garage or pole "
    f"barn larger than 200 square{NB}feet. Item 1 exempts <i>detached</i> "
    f"accessory structures up to that size, while R.C. {sec('3781.06(C)(11)')} "
    f"defines \"accessory structure\" as one \"<b>attached to</b> a "
    f"residential building\" — a garage, porch or screened-in patio. The two "
    f"texts do not obviously line up, and how a large detached outbuilding is "
    f"treated is a question for your department, or for the agricultural "
    f"exemption at {sec('3781.06(B)(1)')} if it genuinely serves a farm use. "
    f"Ask before you order the trusses."))

# ---------------------------------------------------------------- contracts
flow += k.h2_tight("THE CONTRACT AND LIEN DOCUMENTS — THESE ARE YOURS NOW",
                   reserve=2.2)
flow.append(k.body(
    "On a normal build a general contractor generates these and an owner "
    "receives them. As your own general contractor, <b>nobody is going to hand "
    "them to you</b>. Every one below is either something Ohio law entitles "
    "you to demand, or something that protects you only if you create it."))
rows = [
    [k.cellp("<b>Written home construction service contract</b>"),
     k.cellp("From each contractor on $25,000 or more"),
     k.cellp(f"Nine contents are mandatory, including a copy of their "
             f"certificate of insurance showing at least $250,000 general "
             f"liability ({sec('4722.02(A)')}). <b>A cost-plus contract "
             f"waives this requirement entirely</b>")],
    [k.cellp("<b>Change-order estimate</b>"),
     k.cellp("From the contractor"),
     k.cellp("Required once unforeseen excess costs cumulatively exceed "
             "$5,000. You elect written or oral notice by initialling a clause "
             "the statute scripts. Also waived by a cost-plus contract")],
    [k.cellp("<b>Certificate of insurance</b>"),
     k.cellp("From every trade, before they start"),
     k.cellp("General liability, and workers' compensation coverage for their "
             "own people. Verify it directly with the insurer rather than "
             "accepting a PDF")],
    [k.cellp("<b>Contractor's affidavit that all below them are paid</b>"),
     k.cellp("From each direct contractor, before final payment"),
     k.cellp(f"You may withhold payment until you get it, and your rights "
             f"\"shall not be prejudiced by\" failing to ask "
             f"({sec('1311.011(B)(6)')}). A lender must obtain one before "
             f"paying an original contractor (B)(4)")],
    [k.cellp("<b>Lien waivers and releases</b>"),
     k.cellp("From subs and suppliers"),
     k.cellp(f"Joint checks to a contractor and their sub as a condition of "
             f"release are expressly permitted, and a release given under the "
             f"section is valid \"without separate consideration\" "
             f"({sec('1311.011(B)(7)')}, (B)(9))")],
    [k.cellp("<b>Your own affidavit of full payment</b>"),
     k.cellp("Recorded by you with the county recorder"),
     k.cellp(f"After paying a contractor in full, you may record an affidavit "
             f"that you did — and a lien perfected after that payment \"is "
             f"void and the property wholly discharged\" "
             f"({sec('1311.011(B)(1)')})")],
    [k.cellp("<b>Written notice demanding release of a stale lien</b>"),
     k.cellp("From you to the lienholder"),
     k.cellp(f"Thirty days after that notice, a lienholder who has not "
             f"released \"is liable to the owner for all damages\", including "
             f"court costs and reasonable attorney fees "
             f"({sec('1311.011(B)(3)')})")],
    [k.cellp("<b>Notice of Commencement</b>"),
     k.cellp("Only if your lender requires it"),
     k.cellp(f"Ohio does <b>not</b> require one for a home construction "
             f"contract ({sec('1311.04(O)')}). If you record one anyway "
             f"because the lender asks, you gain the priority rules and your "
             f"subs are relieved of the notice-of-furnishing duty")],
]
flow.append(k.ref_table(
    "Documents an owner-builder has to generate or demand",
    [k.cellp("Document", bold=True), k.cellp("From whom", bold=True),
     k.cellp("Why it matters", bold=True)],
    rows, [1.65 * inch, 1.35 * inch, CW - 3.0 * inch]))
flow.append(k.cite(
    f"<b>The deadline that decides everything.</b> A lien affidavit on a one- "
    f"or two-family dwelling must be filed with the county recorder "
    f"\"<b>within sixty&#160;days</b> from the date on which the last labor or work "
    f"was performed or material was furnished\" ({sec('1311.06(B)(1)')}). "
    f"Anything not described in that paragraph falls to <b>seventy-five "
    f"days</b> under (B)(3) — which is where a <b>three-family</b> dwelling "
    f"lands, because Chapter{NB}1311 draws its residential line at one and two "
    f"family while the rest of Ohio law draws it at three. Diarize sixty days "
    f"from your last trade's final day, and do not close or refinance before "
    f"it runs."))

# ---------------------------------------------------------------- negatives
flow += k.h2_tight("WHAT OHIO NEVER ASKS YOU FOR", reserve=2.0)
flow.append(k.body(
    "These are negative findings — established by reading the statutes and "
    "rules and finding no such requirement, not inferred from silence "
    "elsewhere. If a guide or a salesperson tells you otherwise, ask them for "
    "the section number."))
rows = [
    [k.cellp("<b>A state contractor license, for you or your trades</b>"),
     k.cellp("Ohio issues no general contractor license at all, and its five "
             "trade licenses reach only a \"construction project\", which "
             "excludes a one-, two-, or three-family dwelling. <b>Your city or "
             "township may still require local registration</b>")],
    [k.cellp("<b>An owner-builder affidavit or exemption form</b>"),
     k.cellp("None exists at state level, because there is no state license to "
             "be exempt from. A certified local department may use its own")],
    [k.cellp("<b>An architect's or engineer's seal</b>"),
     k.cellp("\"No seal is required for any plans, drawings, specifications, "
             "or data submitted for approval for any residential buildings\"")],
    [k.cellp("<b>A holding period or a no-sale window</b>"),
     k.cellp("Ohio sets none. No annual cap on houses, no resale clawback — "
             "again because there is no licensing exemption whose conditions "
             "these would be")],
    [k.cellp("<b>A Notice of Commencement</b>"),
     k.cellp("Not for a home construction contract. Your lender may want one "
             "anyway")],
    [k.cellp("<b>A statewide minimum lot size for a septic system</b>"),
     k.cellp("Ohio's sewage rules set none. What constrains you is whether the "
             "system, the replacement area and every setback fit — and what "
             "your zoning and health district add")],
    [k.cellp("<b>Whole-house surge protection</b>"),
     k.cellp("The 2023 National Electrical Code requires it; Ohio rewrote all "
             "three sections to apply only \"where provided\". Worth "
             "installing, not required")],
]
flow.append(k.ref_table(
    "Requirements people expect to find in Ohio law, and do not",
    [k.cellp("Commonly assumed", bold=True),
     k.cellp("What the text actually shows", bold=True)],
    rows, [2.0 * inch, CW - 2.0 * inch]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "oh-permit-kit",
                       "OH.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
