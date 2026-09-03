#!/usr/bin/env python3
"""TN.3 Inspection Sequence.

Every Tennessee claim in this document was read out of its primary source in
September 2026 and is cited on-page.

The organising idea: Tennessee runs TWO inspection programs over one house, on
two different chapters of the rules and two different chapters of the code, and
they interlock only at the very end. A buyer who thinks "my county opted out, so
I get no inspections" is wrong about the electrical half, and the certificate of
occupancy is gated on the electrical final.

Verified sources:
  0780-02-23-.07(2)(a)  the required inspections, verbatim and IN ORDER
  0780-02-23-.07(2)(b)  separate slab inspection when not a monolith pour
  0780-02-23-.07(2)(c)  "Energy efficiency inspections shall occur during the
                        required inspections" — there is no standalone energy
                        or insulation inspection
  0780-02-23-.07(4)     inspections happen in the order set out, and work may
                        not proceed past each point without approval
  0780-02-23-.07(1)     deputy building inspectors appointed under contract
  0780-02-23-.07(5)     any inspection may be waived on a letter from a
                        Tennessee-registered architect or engineer
  0780-02-23-.09(1),(2) CO required before occupancy, and gated on the final
                        ELECTRICAL inspection
  0780-02-23-.08(5)     one free re-inspection, $100 for each one after
  0780-02-01-.05(1)     electrical permit sources; issuing agent max $5
  0780-02-01-.05(2)(a)  residential property owner's electrical permit — one
                        per TWELVE months, a different clock from the building
                        permit's twenty-four
  0780-02-01-.05(6)     an electrical rejection requires a NEW permit
  0780-02-01-.04(10)    no final electrical certificate if a required building
                        permit was never obtained
  0780-02-01-.04(11)    power must be on for the final electrical inspection
  0780-02-01-.21        the electrical fee schedule
  T.C.A. § 68-120-101(b)(1)(D)  an owner in an OPT OUT jurisdiction may request
                        an SFMO inspection and receive documentation

DELIBERATELY NOT CLAIMED, and why:
  - Any inspection list for an EXEMPT jurisdiction. Those run their own adopted
    code and their own schedule; the document says so and gives a write-in.
  - That every opt-out county participates in the NFIP. Not verified per-county.
  - A named permit application form number. The rule says only "a form
    prescribed by the Department"; the real path is the CORE online workflow.
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
CITE = k.CITE_COL

FORM_ID = "TN.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Two inspection programs run over one Tennessee house — and only one of "
    "them stops when your county opts out.")

flow.append(k.disclaimer(
    "The sequence below is the STATE program's, which governs SRBP "
    "jurisdictions. An EXEMPT jurisdiction runs its own schedule under its own "
    "adopted code; ask it, and write the answer on the log at the end."))
flow.append(Spacer(1, 10))

# ------------------------------------------------- three regimes
flow += k.h2_tight("WHAT YOU GET DEPENDS ON YOUR STATUS", reserve=2.0)
flow.append(k.body(
    "TN.1 established which of the three labels applies to your parcel. Here "
    "is what each one means once the concrete starts moving. <b>Read down the "
    "electrical column.</b> It is the same in all three rows, and that is the "
    "point almost every Tennessee owner-builder misses."))
rows = [
    [k.cellp("<b>EXEMPT</b><br/>50 counties"),
     k.cellp("The local building department inspects, on its own adopted code "
             "and its own schedule. Ask them for the list — it will usually "
             "be longer than the state's"),
     k.cellp("Local, <b>unless</b> the jurisdiction is on the state electrical "
             "exempt list. Most are not")],
    [k.cellp("<b>SRBP</b><br/>8 counties"),
     k.cellp("State contract inspectors, on the sequence fixed by rule "
             "0780-02-23-.07 — the one set out below"),
     k.cellp("<b>State.</b> Separate permit, separate inspector, separate fee")],
    [k.cellp("<b>OPT OUT</b><br/>37 counties"),
     k.cellp("<b>Nobody.</b> No building permit, no framing inspection, no "
             "certificate of occupancy — unless you ask for one voluntarily"),
     k.cellp("<b>State. Still required.</b> Every one of the 37 opt-out "
             "counties is inside the State Electrical Program")],
]
flow.append(k.ref_table(
    "Three statuses, two programs",
    [k.cellp("Status", bold=True),
     k.cellp("Who does the BUILDING inspections", bold=True),
     k.cellp("Who does the ELECTRICAL inspections", bold=True)],
    rows, [1.0 * inch, (CW - 1.0 * inch) * 0.54, (CW - 1.0 * inch) * 0.46]))
flow.append(k.cite(
    "The building program rests on T.C.A. Title 68, Chapter 120 and rule "
    "chapter 0780-02-23. The electrical program rests on a different chapter "
    f"entirely — T.C.A. {sec('68-102-113')}, {sec('68-102-143')} and "
    f"{sec('68-102-150')}, implemented at rule chapter 0780-02-01. The opt-out "
    f"at {sec('68-120-101(b)(1)(B)(i)')} is written against \"the standards "
    f"established pursuant to subsection (a)\" — the building standards. It "
    f"does not reach the electrical chapter, and rule 0780-02-01 contains no "
    f"opt-out mechanism at all."))

# ------------------------------------------------- the sequence
flow += k.h2_tight("THE STATE SEQUENCE, IN THE ORDER THE RULE FIXES IT",
                   reserve=2.4)
flow.append(k.body(
    "This is the whole of it, quoted. Note that the order is not advisory — a "
    "separate paragraph makes it binding, and forbids you from building past "
    "each point until that inspection has been approved."))
flow.append(k.callout_long(
    "Rule 0780-02-23-.07(2)(a) — Inspections shall be required on:", [
        Paragraph("\"1. <b>Foundations</b> after poles or piers are set or "
                  "trenches or basement areas are excavated and any required "
                  "forms erected and any required reinforcing steel is in "
                  "place and supported prior to the placing of concrete… "
                  "<b>Monolith poured slabs shall be inspected as the "
                  "footing</b> for the structure.", S["body"]),
        Paragraph("2. …<b>plumbing and mechanical systems</b> prior to "
                  "covering or concealment, before fixtures or appliances are "
                  "set or installed, and prior to or at the same time as the "
                  "framing inspection.", S["body"]),
        Paragraph("3. <b>Frame</b> after roof, framing, fire stopping, draft "
                  "stopping, bracing rough in plumbing, rough in mechanical "
                  "and rough in electrical are in place.", S["body"]),
        Paragraph("4. <b>Attached garages.</b> 5. <b>Prefabricated walls.</b> "
                  "6. <b>Fire renovations.</b>", S["body"]),
        Paragraph("7. <b>Final</b> after the permitted work is complete and "
                  "prior to occupancy.\"", S["body"]),
        Paragraph("<b>And the order binds:</b> \"Inspections shall be "
                  "conducted in the order set out in paragraph (2)… Work shall "
                  "not be done beyond the point indicated in each successive "
                  "inspection without first obtaining approval\" "
                  "(rule 0780-02-23-.07(4)).", S["body"]),
    ]))
flow.append(k.cite(
    "Read from the Secretary of State's official rule chapter 0780-02-23, "
    "\"One and Two Family Dwellings and Townhouses\", effective 25 February "
    "2024, at publications.tnsosfiles.com. Two additions sit just below the "
    "quoted list: a <b>separate slab inspection</b> is required whenever the "
    "slab is not a monolith pour (rule .07(2)(b)), and \"energy efficiency "
    "inspections shall occur during the required inspections\" "
    "(rule .07(2)(c)) — there is no standalone insulation or energy visit."))

flow.append(Spacer(1, 4))
flow.append(k.body(
    "<b>In practice that is three inspections on most houses, four on some.</b> "
    "The State Fire Marshal's own guidance puts it plainly: \"Three inspections "
    "will be required: the foundation prior to pour, the rough-in/framing, and "
    "at final construction. If your foundation is to be a concrete slab under a "
    "living space with separately poured footing, you will need a fourth "
    "inspection.\" Plumbing and mechanical are inspected too, at or before the "
    "framing visit."))

# ------------------------------------------------- insulation trap
flow += k.h2_tight("THE INSULATION TRAP — IT DEPENDS WHICH KIND YOU BUY",
                   reserve=2.0)
flow.append(k.body(
    "This one costs people a whole inspection cycle, and it is decided at the "
    "builders' merchant weeks earlier. <b>Batt insulation must be IN before "
    "the framing inspection. Blown or sprayed insulation must be inspected "
    "BEFORE it goes in.</b> Same inspection, opposite instructions."))
rows = [
    [k.cellp("<b>Batt or roll</b>"),
     k.cellp("\"If batt or roll wall insulation is used, <b>it must be in "
             "place prior to requesting an inspection.</b> If a plastic vapor "
             "barrier is used, it should be installed <i>after</i> the "
             "inspection\"")],
    [k.cellp("<b>Loose-fill or spray</b>"),
     k.cellp("\"If loose-fill or spray applied insulation is used, <b>the "
             "request should be made before it is installed</b>\" — and a "
             "manufacturer's product data sheet and installation certificate "
             "stating the product meets or exceeds the energy code will be "
             "required")],
]
flow.append(k.ref_table(
    "The rough-in/framing inspection, two ways",
    [k.cellp("Insulation type", bold=True),
     k.cellp("What the State Fire Marshal's guidance says", bold=True)],
    rows, [1.55 * inch, CW - 1.55 * inch]))
flow.append(k.cite(
    "State Fire Marshal's Office, Residential Permit FAQs, page last modified "
    "25 February 2026. The vapor barrier instruction is easy to skim past and "
    "is the reason a batt job sometimes fails on a second visit: the inspector "
    "has to see the insulation, so the plastic goes on afterwards."))

# ------------------------------------------------- electrical
flow += k.h2_tight("THE ELECTRICAL TRACK RUNS ALONGSIDE, ON ITS OWN RULES",
                   reserve=2.0)
flow.append(k.body(
    "The State Fire Marshal says it in one sentence, and it is worth reading "
    "twice: <b>\"The state residential building permit is a building permit "
    "only. It is not… an electrical permit.\"</b> The same page lists four "
    "other things it is not — grading or fill approval, floodplain compliance, "
    "a septic or sewer permit, or zoning approval."))
rows = [
    [k.cellp("<b>Where the permit comes from</b>"),
     k.cellp("\"the power distributor, local building official, Commissioner, "
             "or designee, or other issuing agent authorized by the "
             "Commissioner.\" An issuing agent may charge no more than "
             f"<b>$5.00</b> for issuing it, on top of the inspection fee"),
     k.cellp("0780-02-01-.05(1)")],
    [k.cellp("<b>Doing it yourself</b>"),
     k.cellp("\"Any person may perform electrical work (for which an "
             "inspection is required) upon his/her own residence provided "
             "he/she first applies for and obtains a <b>residential property "
             "owner's electrical permit</b>.\" It covers you and immediate "
             "family — no unlicensed helpers"),
     k.cellp("0780-02-01-.05(2)(a)")],
    [k.cellp("<b>A rejection costs a permit</b>"),
     k.cellp("An electrical rejection requires you to buy a <b>new electrical "
             "permit</b>. This is the opposite of the building permit, which "
             "carries one free re-inspection"),
     k.cellp("0780-02-01-.05(6)")],
    [k.cellp("<b>Power on for the final</b>"),
     k.cellp("\"electrical power shall be supplied to the building in order "
             "for the inspector to perform the final inspection\" — arrange "
             "the service release with the utility before you book it"),
     k.cellp("0780-02-01-.04(11)")],
]
flow.append(k.ref_table(
    "The electrical program, in four rules",
    [k.cellp("", bold=True), k.cellp("What the rule says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.35 * inch, CW - 1.35 * inch - CITE, CITE]))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "Two clocks, and they are different lengths", [
        Paragraph("The <b>building</b> permit rule allows a property owner "
                  "\"only one (1) property owner's permit within a "
                  "<b>twenty-four (24) month</b> period\" "
                  "(rule 0780-02-23-.05(3)). The <b>electrical</b> rule allows "
                  "a residential property owner's electrical permit "
                  "<b>once per twelve months</b> "
                  "(rule 0780-02-01-.05(2)(a)). Twenty-four months and twelve "
                  "months, in two different rule chapters, for the same house. "
                  "If you are building a second dwelling — a shop with a "
                  "dwelling unit, a parent's cottage — check both before you "
                  "assume either.", S["body"]),
    ]))

flow.append(Spacer(1, 4))
flow.append(k.body(
    "<b>The electrical fee schedule is published in full</b>, which is unusual "
    "and useful. These are ceilings — the rule sets what the fee \"shall not "
    "exceed.\""))
rows = [
    [k.cellp("Rough-in inspection, 0–1,000&#160;amp"), k.cellp("$35.00", center=True)],
    [k.cellp("Final inspection, 0–200&#160;amp"), k.cellp("$35.00", center=True)],
    [k.cellp("Final inspection, 201–400&#160;amp"), k.cellp("$40.00", center=True)],
    [k.cellp("Final inspection, 401–600&#160;amp"), k.cellp("$50.00", center=True)],
    [k.cellp("Re-inspection after a rejection"), k.cellp("$35.00", center=True)],
    [k.cellp("Inspection of a dwelling unit's heating and/or cooling system"),
     k.cellp("$35.00", center=True)],
    [k.cellp("Consultation inspection, optional and on request"),
     k.cellp("$50.00", center=True)],
]
flow.append(k.ref_table(
    "Electrical inspection fees — rule 0780-02-01-.21",
    [k.cellp("Inspection", bold=True),
     k.cellp("Fee ceiling", bold=True, center=True)],
    rows, [CW - 1.35 * inch, 1.35 * inch]))
flow.append(k.cite(
    "A typical 200-amp house is therefore <b>$35 rough-in plus $35 final</b>, "
    "plus $35 if the heating and cooling system is inspected, plus up to $5 to "
    "the issuing agent. Rule chapter 0780-02-01, \"Electrical Installations\", "
    "effective 14 July 2025."))

# ------------------------------------------------- the interlock
flow += k.h2_tight("WHERE THE TWO PROGRAMS FINALLY MEET", reserve=2.0)
flow.append(k.body(
    "They run independently for the whole build and then interlock twice at "
    "the end, in both directions."))
flow.append(k.bullet(
    "<b>The certificate of occupancy needs the electrical final.</b> \"A new "
    "one (1) or two (2) family dwelling, townhouse… shall not be occupied "
    "until the Division has issued a certificate of occupancy,\" and that "
    "certificate \"shall be issued after the passage of all inspections "
    "required by this chapter <b>and passage of the final electrical "
    "inspection</b>\" (rule 0780-02-23-.09)."))
flow.append(k.bullet(
    "<b>And the electrical final needs the building permit.</b> The electrical "
    "inspector \"shall not issue a final certificate of approval on an "
    "installation <b>if a building permit has not been obtained, if "
    "required</b>… or all inspections have not been performed\" "
    "(rule 0780-02-01-.04(10)). The words <i>if required</i> are doing the "
    "work: in an opt-out jurisdiction no building permit is required, so "
    "nothing is missing."))

flow.append(Spacer(1, 4))
rows = [
    [k.cellp("<b>How fast must they come?</b>"),
     k.cellp("\"The law requires all inspections to occur <b>within three "
             "working days</b> of when the request is made to the inspector, "
             "<b>except for footer inspections which are to be performed "
             "within one working day</b> of the request\"")],
    [k.cellp("<b>Who books it?</b>"),
     k.cellp("The permit holder — that is you. The Fire Marshal's guidance is "
             "explicit: \"Subcontractors should not schedule an inspection\"")],
    [k.cellp("<b>What does a failure cost?</b>"),
     k.cellp("\"One re-inspection per permit may be performed without any "
             "additional fee. A second or subsequent re-inspection costs "
             "<b>$100</b> each\"")],
    [k.cellp("<b>Can any of it be waived?</b>"),
     k.cellp("Yes. \"Any inspection may be waived if an inspection letter "
             "approving the work is signed and submitted by an <b>Architect or "
             "Engineer currently registered with the State of Tennessee</b>\" "
             "(rule 0780-02-23-.07(5)). Worth knowing if you are using an "
             "engineer for a difficult foundation anyway")],
]
flow.append(k.ref_table(
    "Turnaround, booking, failure and waiver",
    [k.cellp("", bold=True), k.cellp("The answer", bold=True)],
    rows, [1.85 * inch, CW - 1.85 * inch]))
flow.append(k.cite(
    "Inspections are booked at <b>core.tn.gov</b> — the Comprehensive Online "
    "Regulatory and Enforcement System, which is also where the permit is "
    "bought — or by email to the State Fire Marshal's permits mailbox with the "
    "full permit number and the date the work will be ready."))

# ------------------------------------------------- opt out
flow += k.h2_tight("WHEN NOBODY IS REQUIRED TO INSPECT YOU", reserve=2.2)
flow.append(k.body(
    "In an OPT OUT jurisdiction there is no building permit, no required "
    "inspection and no certificate of occupancy. <b>You can still ask for all "
    "three</b>, and there is a good reason to."))
flow.append(k.callout_long(
    "The voluntary inspection — and why a lender may make you want it", [
        Paragraph("The statute creates the right expressly: \"the owner of a "
                  "building, structure, or premises located in a county or "
                  "municipality that has taken action pursuant to subdivision "
                  "(b)(1)(B) <b>may request that the state fire marshal "
                  "inspect</b> the building… to determine whether [it] meets "
                  "the statewide codes,\" and on passing, \"the state fire "
                  "marshal <b>must issue documentation to the owner "
                  f"evidencing such</b>\" ({sec('68-120-101(b)(1)(D)')}).",
                  S["body"]),
        Paragraph("The State Fire Marshal's own page on opt-out jurisdictions "
                  "gives the commercial reason: owners of one- or two-family "
                  "dwellings \"<b>may now be able to access lenders and loan "
                  "programs previously unavailable to them because those "
                  "lenders or loan programs required a CO</b>.\"", S["body"]),
        Paragraph("<b>Decide this before you pour, not after.</b> A voluntary "
                  "inspection is only useful if it happens at the stages an "
                  "inspector can actually see — you cannot have a footing "
                  "inspected through a finished slab. If there is any chance "
                  "you will want the documentation, buy the permit at the "
                  "start and run the normal sequence.", S["body"]),
    ]))
flow.append(k.body(
    "<b>And the electrical inspections happen anyway.</b> Whatever your "
    "building status, in all but a short list of jurisdictions the state "
    "electrical permit is required and a Deputy Electrical Inspector will come "
    "out at rough-in and at final. That is not optional and it does not depend "
    "on your county's resolution."))

# ------------------------------------------------- log
flow += k.h2_tight("INSPECTION LOG — RECORD EVERY ONE", reserve=1.6)
flow += k.check_table(
    "Every visit, whoever required it",
    [
        ("<b>Foundation</b> — forms and any reinforcing steel in place, before "
         "concrete. A monolith slab is inspected as the footing.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Slab</b>, only if it is not a monolith pour and is under living "
         "space. Not required for a garage slab.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Plumbing and mechanical</b> — before covering, before fixtures "
         "are set, at or before the framing inspection.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Electrical rough-in</b> — state permit, separate inspector.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Frame</b> — roof, framing, fire stopping, draft stopping, "
         "bracing and all three rough-ins in place. Batt insulation IN; "
         "blown insulation NOT yet.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Prefabricated walls</b>, if any were used.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Attached garage</b>, if there is one.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Electrical final</b> — power must be on at the building for this "
         "one.", [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Final building</b> — after the permitted work is complete and "
         "before occupancy.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Certificate of occupancy issued.</b> Gated on the final "
         "electrical inspection as well as the building ones.",
         [("Date", 0.5), ("Number", 0.5)]),
        ("Any inspection my EXEMPT jurisdiction requires that is not on this "
         "list — ask them, and write it here:",
         [("Inspection", 0.5), ("Date", 0.5)]),
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "tn-permit-kit",
                       "TN.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
