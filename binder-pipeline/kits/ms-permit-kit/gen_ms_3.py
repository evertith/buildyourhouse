#!/usr/bin/env python3
"""MS.3 Inspection Sequence.

Mississippi is the state where an inspection document has to be written twice:
once for the reader whose jurisdiction enforces a code, and once for the reader
whose jurisdiction does not. Roughly half this document is about what to do
when nobody is coming — which no competing guide treats as a real workflow.

Care taken on sourcing: the inspection sequence itself is a property of the
International Residential Code, which a Mississippi jurisdiction adopts (or
does not) under SB 2378 (2014) § 1 and § 17-2-3(5). It is NOT a Mississippi
statutory sequence, and this document does not present it as one. Statutory
claims are limited to what was read in the enacted text.

Deliberately NOT claimed: any specific number of required inspections, any
statewide inspection fee, any statewide re-inspection rule, or that a
certificate of occupancy is issued everywhere — in a jurisdiction with no
building code there is no CO, and saying otherwise would mislead exactly the
reader who most needs the truth.
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

FORM_ID = "MS.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The order inspections happen in, what each one is really checking — and "
    "what to do instead when your county does not send anybody.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- two realities
flow += k.h2_tight("TWO REALITIES, AND YOU NEED TO KNOW WHICH IS YOURS")
flow.append(k.body(
    "Work MS.4 before this document. If a building code is enforced on your "
    "parcel, the first half of this sheet is your schedule and you should "
    "record every visit on it. If no code is enforced, the first half is "
    "still your <b>quality plan</b> — the same milestones, bought privately "
    "instead of provided publicly — and the second half explains why that is "
    "worth paying for."))

flow.append(k.callout(
    "The inspections are the code's, not the state's", [
        Paragraph("Mississippi has no statewide inspection schedule, because "
                  "it has no statewide inspection program. The sequence below "
                  "is the one the <b>International Residential Code</b> "
                  "produces, and a Mississippi jurisdiction gets it only by "
                  "adopting the IRC. Which edition it adopted is a local "
                  "question — the statute permits \"<i>one (1) of the last "
                  "three (3) adopted editions</i>,\" so the details shift a "
                  "little between neighboring counties.", S["body"]),
        Paragraph("Treat the list as the shape of the process rather than a "
                  "checklist your inspector will recognize word for word. "
                  "<b>Ask your building official for their own inspection "
                  "list at the time you pull the permit</b> and write any "
                  "differences into the notes column.", S["body"]),
    ]))

# ---------------------------------------------------------------- sequence
flow += k.h2_tight("THE SEQUENCE — RECORD EVERY VISIT HERE")
flow.append(k.body(
    "Call for each inspection when the work is complete and still <b>open to "
    "view</b>. The expensive mistake in every state is covering work before "
    "it is approved; the remedy is opening it back up at your cost."))

flow += k.check_table("Site and foundation", [
    ("<b>Temporary power</b> — the pole or pedestal your utility requires "
     "before it will energize the site",
     [("Date:", 0.5), ("Result:", 0.5)]),
    ("<b>Footing</b> — trenches excavated to bearing, reinforcement in place, "
     "forms set. Called before any concrete arrives",
     [("Date:", 0.5), ("Result:", 0.5)]),
    ("<b>Slab / foundation</b> — vapor retarder, reinforcement, anchor bolt "
     "layout, and any under-slab work complete",
     [("Date:", 0.5), ("Result:", 0.5)]),
    ("<b>Under-slab plumbing</b> — drain, waste and vent below the slab, "
     "usually held under test pressure while the inspector looks",
     [("Date:", 0.5), ("Result:", 0.5)]),
    ("<b>Termite pretreatment</b> — Mississippi lies wholly within the "
     "region the IRC marks \"<b>very heavy</b>\" for termite infestation, so "
     "an adopted IRC requires protection. Keep the treatment certificate; "
     "lenders and buyers ask for it",
     [("Date:", 0.5), ("Company:", 0.5)]),
], notes_header="Notes / corrections")

flow += k.check_table("Frame and rough-in", [
    ("<b>Framing and sheathing</b> — after the building is dried in, before "
     "anything is concealed. On the coast this is also where the continuous "
     "load path is checked: straps, clips, and the fastening schedule",
     [("Date:", 0.5), ("Result:", 0.5)]),
    ("<b>Electrical rough-in</b> — boxes, cable, service, grounding and "
     "bonding, before insulation",
     [("Date:", 0.5), ("Result:", 0.5)]),
    ("<b>Plumbing rough-in</b> — supply, drain, waste and vent under test",
     [("Date:", 0.5), ("Result:", 0.5)]),
    ("<b>Mechanical rough-in</b> — duct, refrigerant lines, combustion air, "
     "flue and fuel gas piping under test",
     [("Date:", 0.5), ("Result:", 0.5)]),
    ("<b>Insulation and air sealing</b> — after all rough-ins pass, before "
     "drywall. The energy provisions come from whichever IRC edition your "
     "jurisdiction adopted, so confirm what yours expects",
     [("Date:", 0.5), ("Result:", 0.5)]),
], notes_header="Notes / corrections")

flow += k.check_table("Finals", [
    ("<b>Final electrical</b> — devices, panel schedule, arc-fault and "
     "ground-fault protection, smoke and carbon monoxide alarms",
     [("Date:", 0.5), ("Result:", 0.5)]),
    ("<b>Final plumbing</b> — fixtures set, traps and vents complete, water "
     "heater relief piping",
     [("Date:", 0.5), ("Result:", 0.5)]),
    ("<b>Final mechanical</b> — equipment running, condensate handled, "
     "combustion appliances vented and tested",
     [("Date:", 0.5), ("Result:", 0.5)]),
    ("<b>Septic approval</b> — the health department's sign-off on the onsite "
     "system. On most rural parcels this gates occupancy in practice, and it "
     "is required whether or not a building code applies",
     [("Date:", 0.5), ("Document #:", 0.5)]),
    ("<b>Final building / certificate of occupancy</b> — grading and "
     "drainage, steps, guards, handrails, address numbers. <i>Where no "
     "building code is enforced there is no certificate of occupancy at all</i>",
     [("Date:", 0.5), ("CO #:", 0.5)]),
], notes_header="Notes / corrections")

# ---------------------------------------------------------------- no inspector
flow += k.h2_tight("IF NOBODY IS COMING — BUYING YOUR OWN INSPECTIONS")
flow.append(k.body(
    "In a Mississippi county that adopted no code, or that opted out in 2014, "
    "there is no plan review, no permit and no inspector. That is lawful, and "
    "the licensing statute assumes it — one of the exemptions in "
    "§ 73-59-15 is written specifically for \"<i>any county or municipality "
    "which does not require a building permit or any local certification for "
    "such construction</i>.\" But three parties will still want evidence that "
    "your house was built properly, and none of them accepts \"the county "
    "did not require it\" as an answer."))

why_rows = [
    [k.cellp("<b>Your lender</b>"),
     k.cellp("Construction lending is released in draws against inspected "
             "progress. A lender in a no-code county will usually send its "
             "own inspector, or require you to supply third-party reports, "
             "before releasing each draw. Ask what they want <b>before</b> "
             "you close, because it sets your inspection schedule.")],
    [k.cellp("<b>Your insurer</b>"),
     k.cellp("Builder's risk during construction, and the homeowner policy "
             "afterward, are both priced on how the house was built. On the "
             "coast, wind-mitigation features are what make wind coverage "
             "affordable — and they have to be documented by someone at the "
             "time they are installed, because they are invisible once the "
             "house is finished.")],
    [k.cellp("<b>Your buyer, one day</b>"),
     k.cellp("An owner-built house with no permit history and no inspection "
             "reports is a harder sale and a slower one. A folder of dated "
             "third-party reports and photographs turns \"unpermitted\" into "
             "\"documented,\" which is a different conversation entirely.")],
]
flow.append(k.ref_table(
    "Who asks, even when the county does not",
    [k.cellp("Party", bold=True), k.cellp("What they need from you", bold=True)],
    why_rows, [1.35 * inch, CW - 1.35 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>Buy the same milestones the code would have given you.</b> A licensed "
    "home inspector or a structural engineer will visit for a few hundred "
    "dollars a trip. Four visits — footing, framing, pre-drywall with the "
    "rough-ins exposed, and final — cover the moments where a defect becomes "
    "permanently hidden. Photograph everything yourself in addition, "
    "date-stamped, and keep it with this binder."))

flow += k.check_table("Your private inspection plan (no-code parcels)", [
    ("Third-party inspector or engineer engaged, and the four visits booked "
     "into the schedule rather than called at the last minute",
     [("Firm:", 0.55), ("Booked:", 0.45)]),
    ("Lender's own inspection and draw requirements confirmed in writing "
     "before closing",
     [("Confirmed:", 1.0)]),
    ("Builder's risk insurer asked what documentation it wants during "
     "construction",
     [("Confirmed:", 1.0)]),
    "Photographs at each milestone — footings before pour, framing and "
    "connectors, all rough-ins before insulation, insulation before drywall",
    ("Termite treatment performed and certificate filed, even with no "
     "inspector to show it to",
     [("Date:", 0.5), ("Company:", 0.5)]),
    ("Septic system approval obtained from the health department — this one "
     "is not optional and does not depend on your building-code status",
     [("Date:", 0.5), ("Document #:", 0.5)]),
    "Every trade contractor's State Board of Contractors license verified "
    "before they started — the zero-dollar rule in § 73-59-3(1)(d) applies "
    "whether or not anyone inspects the work",
], notes_header="Notes / evidence")

# ---------------------------------------------------------------- MS specifics
flow += k.h2_tight("THREE MISSISSIPPI CONDITIONS WORTH AN EXTRA LOOK")
flow.append(k.bullet(
    "<b>Termites.</b> The whole state sits in the IRC's \"very heavy\" "
    "infestation region, and the coast additionally contends with the "
    "Formosan subterranean termite. Soil treatment, a bait system or an "
    "approved barrier is the code answer where a code applies, and the "
    "sensible answer everywhere else."))
flow.append(k.bullet(
    "<b>Expansive clay.</b> Parts of central Mississippi, notably the Jackson "
    "metropolitan area, sit on soils that shrink and swell enough to move a "
    "slab. A geotechnical report before you design the foundation costs far "
    "less than the repair does. This is a soils question, not a code "
    "question, and no inspector will raise it for you."))
flow.append(k.bullet(
    "<b>Wind and flood on the coast.</b> In Jackson, Harrison, Hancock, Stone "
    "and Pearl River counties the 2006 law imposed wind and flood mitigation "
    "requirements — subject to the opt-out described in MS.4. Whatever your "
    "county's status, the insurance market on the coast prices these features "
    "whether or not an inspector checks them, and the connectors have to be "
    "documented while they are still visible."))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("There is no statewide Mississippi inspection schedule; the sequence "
     "comes from whichever edition of the International Residential Code the "
     "local jurisdiction adopted, and the statute allows any of the last "
     "three adopted editions",
     "SB 2378 (2014) § 1(1); § 17-2-3(5)"),
    ("Building in a jurisdiction that requires no building permit or local "
     "certification is contemplated by the licensing statute itself",
     "§ 73-59-15(1)(g)"),
    ("Electrical, plumbing, mechanical and HVAC contractors must hold a state "
     "license no matter the dollar amount, inspected or not",
     "§ 73-59-3(1)(d)"),
    ("Wind and flood mitigation requirements for the five named coastal "
     "counties, and the opt-out that accompanied them",
     "§ 17-2-1; HB 1406 (2006) § 1"),
    ("Residential fire sprinklers are excluded from the IRC as adopted "
     "statewide, though a county or municipality may still require them",
     "SB 2378 (2014) § 1(1)(b); § 17-2-3(7)"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ms-permit-kit",
                       "MS.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
