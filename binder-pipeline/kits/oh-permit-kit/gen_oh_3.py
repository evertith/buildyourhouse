#!/usr/bin/env python3
"""OH.3 Inspection Sequence.

Ohio is unusual among the no-mandatory-enforcement states in that its code
actually names the inspections. Arkansas leaves the list to whatever local
program exists; Ohio prints twelve numbered subsections and then tells the
building official to hand the owner a list drawn from them at plan approval.
So this document can give the reader a real sequence rather than a method.

Two findings drive the document's shape:

  1. RCO 108.2.1 requires the lot lines to be marked BEFORE any work starts.
     It is the first numbered inspection item in the code and it is not an
     inspection of construction at all — it is a survey requirement. Almost
     nobody expects it, and it is the cheapest thing on this list to get wrong.

  2. RCO 108.2.5 makes the frame inspection conditional on the rough electrical,
     plumbing and heating already being APPROVED. In Ohio the trades clear
     before framing does, which inverts the order most owner-builders assume
     and is the single most common scheduling mistake available here.

Verified sources:
  OAC 4101:8-1-01 108.2       the required-inspection list and who supplies it
  OAC 4101:8-1-01 108.2.1     lot line markers, before any work
  OAC 4101:8-1-01 108.2.2-.9  the inspections themselves, quoted
  OAC 4101:8-1-01 108.2.11    findings, the on-site record, and the CO
  OAC 4101:8-1-01 108.3, .4   third-party reports; right of entry
  OAC 4101:8-1-01 110.1       the local board of building appeals
  R.C. 3781.10(E)(15)         third-party examiners, who pays, and the limit
  R.C. 3791.04(E)             thirty days of silence is an appealable denial
  R.C. 307.37                 the county drainage review and its 30-day clock
  OAC 3701-29-09(H)           the health district's twelve-month re-inspection
  R.C. 3781.03(C)             plumbing enforcement runs on its own track

DELIBERATELY NOT PRINTED:
  - Any inspection fee, or any "call 24 hours ahead" scheduling rule. Both are
    local and both change.
  - Any claim about how many inspections a particular department requires. The
    code sets the menu; the department sets the list.
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

FORM_ID = "OH.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The inspections the Residential Code of Ohio actually names, the one that "
    "happens before any work at all, and what to record when nobody is "
    "required to inspect you.")

flow.append(k.disclaimer(
    "The inspection list below is quoted from the Residential Code of Ohio's "
    "administration rule as filed with the Legislative Service Commission and "
    "read in September 2026."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- who lists
flow += k.h2_tight("OHIO NAMES ITS INSPECTIONS — AND HANDS YOU THE LIST",
                   reserve=2.0)
flow.append(k.body(
    "In most states the inspection schedule is whatever the local department "
    "prints on the back of the permit. Ohio writes the menu into the code and "
    "then requires the building official to give you your project's list at "
    "the moment your plans are approved."))
flow.append(k.callout(
    f"OAC {k.rule('4101:8-1-01')}, RCO section 108.2 — Required inspections", [
        Paragraph("\"<b>At the time that the certificate of plan approval is "
                  "issued, the residential building official shall provide to "
                  "the owner, or the owner's representative, a list of all "
                  "required inspections for each project.</b> The required "
                  "inspection list shall be created from the applicable "
                  "inspections set forth in sections 108.2.1 to 108.2.12. The "
                  "residential building official, upon notification from the "
                  "owner or the owner's agent that the work is ready for "
                  "inspection, shall cause the inspections set forth in the "
                  "required inspection list to be made by an appropriately "
                  "certified residential inspector in accordance with the "
                  "approved residential construction documents.\"", S["body"]),
    ]))
flow.append(k.body(
    "<b>Ask for that list in writing and keep it behind this sheet.</b> It is "
    "the definitive answer to \"what does this department actually want?\", it "
    "is your right to receive it, and it removes every later argument about "
    "whether an inspection was required. If it does not arrive with your plan "
    "approval, ask again in writing."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "And if the inspector does not come — RCO section 108.1", [
        Paragraph("\"It shall be the duty of the owner or the owner's "
                  "authorized representative to cause the work to remain "
                  "accessible and exposed for inspection purposes… until the "
                  "work has been inspected to verify compliance with the "
                  "approved construction documents, but <b>failure of the "
                  "inspectors to inspect the work within four days, exclusive "
                  "of Saturdays, Sundays, and legal holidays, after the work "
                  "is ready for inspection, allows the work to proceed.</b> "
                  "Subsequent work is allowed to proceed only to the point of "
                  "the next required inspection.\"", S["body"]),
        Paragraph("<b>This is one of the most useful sentences in the Ohio "
                  "code for anyone on a schedule</b> — and it comes with a "
                  "condition you have to create yourself. The four days run "
                  "from when the work is <i>ready</i> and the department has "
                  "been <i>notified</i>. Put the request in writing, date it, "
                  "photograph the exposed work the same day, and keep both. "
                  "Without that record you cannot show when the clock started, "
                  "and the protection is worth nothing.", S["body"]),
    ]))

# ---------------------------------------------------------------- lot lines
flow += k.h2_tight("THE FIRST ONE HAPPENS BEFORE YOU MOVE ANY DIRT",
                   reserve=2.0)
flow.append(k.body(
    "The first item on Ohio's list is not an inspection of construction. It is "
    "a survey requirement, it is easy to satisfy cheaply and almost impossible "
    "to satisfy late, and it catches people who have already excavated."))
flow.append(k.callout(
    "RCO section 108.2.1 — Lot line markers required", [
        Paragraph("\"<b>Before any work is started</b> in the construction of "
                  "a residential building or an addition to a residential "
                  "building to which the rules of the board are applicable "
                  "under section 101.2, <b>all boundary lines shall be clearly "
                  "marked at their intersections with permanent markers or "
                  "with markers which are offset at a distance which is of "
                  "record with the owner.</b>\"", S["body"]),
    ]))
flow.append(k.body(
    "<b>What that means in practice:</b> get the corners pinned by a surveyor "
    "before the excavator arrives, not after the footing is poured and a "
    "neighbor asks a question. The rule accepts offset markers as long as the "
    "offset distance is on record with you — which is how surveyors normally "
    "protect pins from being destroyed by machinery. It costs a fraction of "
    "moving a foundation."))
flow.append(k.cite(
    f"This is also the requirement that most often makes an owner-builder's "
    f"site plan real rather than approximate. Your septic isolation distances "
    f"are measured to the property line (OAC {k.rule('3701-29-06(G)(3)(a)')}), "
    f"your well keeps 10{NB}feet from lot lines and easements (OAC "
    f"{k.rule('3701-28-07(J)')}, Table 1), and your zoning setbacks are "
    f"measured from the same lines. One survey serves all of it. If you are in "
    f"a jurisdiction with no certified building department, RCO 108.2.1 does "
    f"not bind you — but every one of those other distances still does, and "
    f"they are all measured from boundaries you have to know."))

# ---------------------------------------------------------------- the list
flow += k.h2_tight("THE INSPECTIONS, AS THE CODE DESCRIBES THEM", reserve=1.8)
flow.append(k.body(
    "Read the trigger conditions carefully. Ohio writes them as \"shall be "
    "made after…\", which tells you exactly how far to get before you call — "
    "and in one case tells you that another inspection has to have passed "
    "first."))
rows = [
    [k.cellp("<b>108.2.2</b><br/>Footing or foundation"),
     k.cellp("\"after excavations for footings are complete and any required "
             "reinforcing steel is in place. For concrete foundations, any "
             "required forms shall be in place prior to inspection. Materials "
             "for the foundation shall be on the job, except where concrete is "
             "ready mixed… the concrete need not be on the job\"")],
    [k.cellp("<b>108.2.3</b><br/>Concrete slab and under-floor"),
     k.cellp("\"after in-slab and under-floor reinforcing steel and building "
             "service equipment, conduit, insulation, vapor retarder, piping "
             "accessories and other ancillary equipment items are in place, "
             "<b>but before any concrete is placed or floor sheathing "
             "installed, including the subfloor</b>\"")],
    [k.cellp("<b>108.2.4</b><br/>Lowest floor elevation"),
     k.cellp("The elevation certification required by section 322 is submitted "
             "to the building official. This is the floodplain one — it "
             "applies where section 322 does")],
    [k.cellp("<b>108.2.5</b><br/>Frame"),
     k.cellp("\"after the roof deck or sheathing, all framing, fire blocking "
             "and bracing are in place and pipes, chimneys and vents to be "
             "concealed are complete <b>and the rough electrical, plumbing, "
             "heating wires, pipes and ducts are approved</b>\" — read that "
             "last clause twice; see the note below")],
    [k.cellp("<b>108.2.6</b><br/>Lath or gypsum board"),
     k.cellp("\"after lathing and gypsum board, interior and exterior, is in "
             "place, but before any plastering is applied or before gypsum "
             "board joints and fasteners are taped and finished.\" "
             "<b>Exception:</b> gypsum board that is not part of a "
             "fire-resistive assembly or a shear assembly")],
    [k.cellp("<b>108.2.7</b><br/>Fire-resistant penetrations"),
     k.cellp("\"Protection of joints and penetrations in fire-resistance-rated "
             "assemblies shall not be concealed from view until inspected and "
             "approved\"")],
    [k.cellp("<b>108.2.8</b><br/>Energy efficiency"),
     k.cellp("Compliance with Chapter 11, including \"envelope insulation 'R' "
             "and 'U' values, fenestration 'U' value, duct system 'R' value, "
             "infiltration air barriers, caulking/sealing of openings in "
             "envelope and ductwork, and 'HVAC' and water heating equipment "
             "efficiency\"")],
    [k.cellp("<b>108.2.9</b><br/>Building service equipment"),
     k.cellp("Everything installed \"in accordance with the approved "
             "construction documents, the equipment listings, and the "
             "manufacturer's installation instructions\" — mechanical heating "
             "and ventilating, mechanical exhaust, plumbing, fire protection "
             "and electrical systems")],
    [k.cellp("<b>108.2.10</b><br/>Other inspections"),
     k.cellp("The official may require others \"to ascertain compliance\", and "
             "on projects \"of unusual magnitude\" may require full-time "
             "project representation by a registered design professional or "
             "inspection agency")],
]
flow.append(k.ref_table(
    "RCO sections 108.2.2 to 108.2.10",
    [k.cellp("Inspection", bold=True),
     k.cellp("When the code says it happens", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch]))
flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "The sequencing mistake Ohio makes easy", [
        Paragraph("<b>In Ohio the rough trades clear before the frame does.</b> "
                  "RCO 108.2.5 does not say the framing inspection happens "
                  "alongside the rough-ins or before them — it says the frame "
                  "inspection is made after the framing is complete "
                  "<i>and</i> \"the rough electrical, plumbing, heating wires, "
                  "pipes and ducts <b>are approved</b>.\"", S["body"]),
        Paragraph("Most owner-builders schedule the other way round, because "
                  "in plenty of jurisdictions elsewhere framing is inspected "
                  "first and the trades follow. Booking it backwards here "
                  "costs you a failed inspection and a re-inspection fee at "
                  "the exact moment the drywall crew is standing in the "
                  "driveway.", S["body"]),
        Paragraph("<b>Plan the rough-in inspections as a cluster that ends "
                  "with framing</b>, and confirm with your department how it "
                  "wants them called — some run them as one visit, some as "
                  "four. Write the answer on the log at the end of this "
                  "document.", S["body"]),
    ]))

flow.append(Spacer(1, 4))
flow.append(k.body(
    "<b>What happens when an inspection passes</b> is also written down, and "
    "it is worth knowing because it tells you where your evidence lives. Under "
    "RCO 108.2.11 the inspector \"shall communicate the findings to the "
    "owner's on-site representative, shall make a note of the satisfactory "
    "inspection <b>on an on-site inspection record</b> and in the inspector's "
    "log, and communicate the findings to the residential building official\", "
    "who then \"shall issue the certificate of occupancy in accordance with "
    "section 111.\" <b>Keep that on-site inspection record.</b> It is the "
    "primary document a lender, insurer or buyer will ask for."))
flow.append(k.cite(
    f"Two more things the code allows. The building official \"is authorized "
    f"to accept reports of approved inspection agencies\" (RCO 108.3), and the "
    f"statute permits certified departments to take plan-examination and "
    f"inspection reports from third-party examiners — but note who pays and "
    f"what they cannot do: \"Fees charged by a third-party examiner or "
    f"inspector are in addition to any fees prescribed by the political "
    f"subdivision… and are <b>the responsibility of the building owner</b>\", "
    f"and issuing the certificate of plan approval and the certificate of "
    f"occupancy \"<b>remains the exclusive authority</b> of the certified "
    f"personnel\" ({sec('3781.10(E)(15)')}). A third party can inspect you. "
    f"Only the department can sign you off."))

# ---------------------------------------------------------------- everywhere
flow += k.h2_tight("THE INSPECTIONS THAT HAPPEN WHEREVER YOU BUILD",
                   reserve=1.8)
flow.append(k.body(
    "These do not come from the building code and do not stop existing when no "
    "building department is certified for your parcel. On a rural build they "
    "may be the only inspections your house ever gets."))
flow += k.check_table(
    "Record each of these as it happens",
    [
        ("<b>Sewage system — installation inspection</b> by the board of "
         "health before covering. Nothing about this depends on a building "
         "department.", [("Inspector", 0.6), ("Date", 0.4)]),
        ("<b>Sewage system — the twelve-month revisit.</b> The board of health "
         "\"shall inspect the completed system again not later than twelve "
         "months after the approval of the installation to observe the "
         "system's operation\" (§&#160;3701-29-09(H)). Diarize it.",
         [("Due", 0.5), ("Done", 0.5)]),
        ("<b>Installer's as-built drawing</b> received, showing any change in "
         "component locations and the distances to everything with an "
         "isolation requirement (§&#160;3701-29-09(F)).", [("Date", 1.0)]),
        ("<b>Private water system</b> — the pre-construction site review with "
         "the health district, then the final inspection and water sample.",
         [("Sample result", 0.6), ("Date", 0.4)]),
        ("<b>Plumbing.</b> Enforcement runs on its own statutory track and may "
         "come from the health district, the Division of Industrial "
         "Compliance, a municipal building-inspection department or a "
         "contracting county department (§&#160;3781.03(C)). Establish which one, "
         "then book it.", [("Office", 0.6), ("Date", 0.4)]),
        ("<b>Building sewer / sanitary tap</b>, if on public sewer — inspected "
         "by whoever issued it: city engineer, board of health or sewer "
         "purveyor.", [("Office", 0.6), ("Date", 0.4)]),
        ("<b>Driveway or culvert</b> — the road authority's inspection of the "
         "approach.", [("Office", 0.6), ("Date", 0.4)]),
        ("<b>Electric service</b> — your utility's own inspection or release "
         "before it energizes. In a jurisdiction with no electrical permit "
         "this is often the only outside look at your wiring, so ask early "
         "what it involves.", [("Utility", 0.6), ("Date", 0.4)]),
    ])

# ---------------------------------------------------------------- nobody
flow += k.h2_tight("WHEN NOBODY IS REQUIRED TO INSPECT YOU", reserve=2.0)
flow.append(k.body(
    "If no building department certified for residential buildings has "
    "jurisdiction over your parcel, RCO 101.5 excuses you from requesting "
    "inspections and from obtaining a certificate of occupancy. <b>The code "
    "standard still applies to your house.</b> What disappears is the "
    "paperwork and the person who would have checked — which means the "
    "evidence has to come from you."))
flow.append(k.callout_long(
    "Build your own inspection record — it is an asset, not a chore", [
        Paragraph("<b>Photograph every stage before it is covered.</b> "
                  "Footings with steel in place. Under-slab plumbing and vapor "
                  "retarder before the pour. Every wall cavity before "
                  "insulation, from a distance and close up, with a tape "
                  "measure in frame where a dimension matters. Roof deck and "
                  "flashing. Panel interior with the dead front off. Date "
                  "every photograph.", S["body"]),
        Paragraph("<b>Hire the inspections you are not required to have.</b> "
                  "A private third-party inspector, an engineer for the "
                  "foundation, or a licensed electrician to review your "
                  "rough-in costs a fraction of one percent of the build. In a "
                  "jurisdiction with no certified department there is nobody "
                  "whose job it is to catch the mistake that burns the house "
                  "down, and your own eye is the least reliable instrument on "
                  "site.", S["body"]),
        Paragraph("<b>Get a blower-door and duct test done anyway.</b> They "
                  "are cheap, they are the only objective measurement of "
                  "whether the envelope you paid for exists, and the number is "
                  "the single most persuasive thing you can hand an appraiser "
                  "or a buyer later.", S["body"]),
        Paragraph("<b>Write down who told you no permit was required, and "
                  "when.</b> An email from the county or the township, dated "
                  "and filed behind OH.4, is the answer to the question a "
                  "lender or title company will ask years from now. Without "
                  "it, \"there was no building department\" is an assertion. "
                  "With it, it is a record.", S["body"]),
    ]))

# ---------------------------------------------------------------- appeals
flow += k.h2_tight("IF AN INSPECTION OR A REVIEW GOES AGAINST YOU",
                   reserve=1.8)
flow.append(k.body(
    "Ohio gives you three separate routes, and they run to three different "
    "places. Use them in order and in writing."))
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp("<b>The local board of building appeals</b>"),
     k.cellp("RCO section 110.1 provides for a hearing and a right of appeal "
             "from the residential building official's orders. This is the "
             "first stop for \"the inspector is reading the code wrong\"")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("<b>The thirty-day silence rule</b>"),
     k.cellp(f"Plan approval is a \"license\", and failure to approve within "
             f"thirty days is \"an adjudication order denying the issuance of "
             f"a license\" requiring a hearing — and any denial \"shall "
             f"specify the reasons\" ({sec('3791.04(E)')}). A stalled review "
             f"is a decision you can appeal, not a queue you must wait in")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("<b>The Board of Building Standards, for a conflicting local "
             "rule</b>"),
     k.cellp(f"A local authority may add residential regulations only if they "
             f"do not conflict with the state code — and <b>any person</b> may "
             f"ask the Board to rule on a conflict, which it must do within "
             f"<b>sixty days</b>. If it finds a conflict and the rule is not "
             f"necessary for health or safety, \"the regulation is not valid "
             f"and the local governing authority may not enforce\" it "
             f"({sec('3781.01(B)')} to (D))")],
]
flow.append(k.ref_table(
    "Three routes, three destinations",
    [k.cellp("", bold=True, center=True), k.cellp("Route", bold=True),
     k.cellp("What it is for", bold=True)],
    rows, [0.35 * inch, 1.85 * inch, CW - 2.2 * inch]))
flow.append(k.cite(
    f"One more worth knowing if you are in an unincorporated area of a county "
    f"that runs a building department: R.C. {sec('307.37')} builds a drainage "
    f"review into the county building permit application and puts a clock on "
    f"it — \"If the review is not completed within the thirty-day period…, the "
    f"proposed new construction <b>shall be deemed to have no adverse effects "
    f"on existing surface or subsurface drainage</b>.\" That section was "
    f"amended effective 9{NB}April 2025, so confirm the current text before "
    f"relying on the detail."))

# ---------------------------------------------------------------- log
flow += k.h2_tight("INSPECTION LOG — RECORD EVERY ONE", reserve=1.6)
flow += k.check_table(
    "Every inspection, whether or not anybody required it",
    [
        ("Lot lines marked — surveyor and date, BEFORE any work",
         [("Surveyor", 0.6), ("Date", 0.4)]),
        ("Footing / foundation", [("Result", 0.6), ("Inspector", 0.4)]),
        ("Concrete slab / under-floor, before the pour",
         [("Result", 0.6), ("Inspector", 0.4)]),
        ("Lowest floor elevation certificate, if in a flood hazard area",
         [("Result", 0.6), ("Date", 0.4)]),
        ("Rough plumbing", [("Result", 0.6), ("Inspector", 0.4)]),
        ("Rough electrical", [("Result", 0.6), ("Inspector", 0.4)]),
        ("Rough heating — wires, pipes and ducts",
         [("Result", 0.6), ("Inspector", 0.4)]),
        ("<b>Frame</b> — only after the three rough-ins above are approved",
         [("Result", 0.6), ("Inspector", 0.4)]),
        ("Lath or gypsum board, before taping",
         [("Result", 0.6), ("Inspector", 0.4)]),
        ("Fire-resistant penetrations, before concealment",
         [("Result", 0.6), ("Inspector", 0.4)]),
        ("Insulation and energy — envelope, fenestration, ducts, sealing",
         [("Result", 0.6), ("Inspector", 0.4)]),
        ("Blower door / duct leakage test result",
         [("Result", 0.6), ("Date", 0.4)]),
        ("Building service equipment — mechanical, plumbing, electrical",
         [("Result", 0.6), ("Inspector", 0.4)]),
        ("Sewage system installation, before covering",
         [("Result", 0.6), ("Inspector", 0.4)]),
        ("Private water system final and water sample",
         [("Result", 0.6), ("Date", 0.4)]),
        ("Electric service release", [("Utility", 0.6), ("Date", 0.4)]),
        ("Certificate of occupancy, if one is issued here",
         [("No.", 0.5), ("Date", 0.5)]),
        ("Sewage system twelve-month revisit",
         [("Result", 0.6), ("Date", 0.4)]),
    ],
    notes_header="Notes", date_w=0.8, notes_w=1.4)
flow.append(k.closing_note(
    "Whether or not a building department ever looked at this house, the log "
    "above is the record that it was built to a standard. Keep the on-site "
    "inspection record, the health district's approvals, the as-built septic "
    "drawing, the water sample, the blower-door number and the photographs "
    "together with this sheet. Three years from now, when an appraiser, an "
    "insurer or a buyer asks what your house was built to, this folder is the "
    "entire answer — and in a jurisdiction with no certified residential "
    "building department, it is the only answer that exists."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "oh-permit-kit",
                       "OH.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
