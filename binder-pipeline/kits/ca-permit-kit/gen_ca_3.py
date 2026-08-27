#!/usr/bin/env python3
"""CA.3 Inspection Sequence — California.

Sources verified August 2026, quoted from the 2025 California Residential Code,
Chapter 1, Division II, Administration:
  R109.1.1    foundation and footings — before concrete
  R109.1.1.1  concrete slab and under-floor
  R109.1.2    rough plumbing, mechanical, gas and electrical — BEFORE framing
  R109.1.3    floodplain: lowest-floor elevation, sealed, before going vertical
  R109.1.4    frame and masonry
  R109.1.4.1  MOISTURE CONTENT VERIFICATION per CALGreen Ch. 4 Div. 4.5
              — a California-only inspection item
  R109.1.4.2  lath and gypsum board
  R109.1.5    other inspections; .5.1 fire-resistance-rated construction;
              .5.2 special inspections -> CBC Chapter 17;
              .5.3 WEATHER-EXPOSED BALCONY waterproofing, not concealed until
              inspected — the other California-only item
  R109.1.6    final inspection, after work complete and prior to occupancy
  R109.1.6.1  flood elevation documentation before final
  R109.1.6.2  OPERATION AND MAINTENANCE MANUAL placed in the building at final,
              per CALGreen Ch. 4 Div. 4.4 — gates the final, nobody expects it
  R109.2      building official may accept reports of approved agencies
  R109.3      permit holder's duty to request and to provide access
  R109.4      no work beyond each successive inspection without approval
  R110.1-.4   certificate of occupancy; contents; temporary CO; revocation
  R111.1      no utility connection until approved by the building official
  Note to R109.1: "Reinforcing steel or structural framework ... shall not be
              covered or concealed without first obtaining the approval of the
              enforcing agency."
  H&S 18938.6 permit validity — commence within 12 months; 180-day extensions

Note: the CRC sets NO numeric turnaround for an inspection request. The
enforcing agency must act "within a reasonable time." Any 24- or 48-hour figure
is local practice.
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

FORM_ID = "CA.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The order California inspections happen in, what each inspector is "
    "actually looking at, the two California adds nobody expects, and a log to "
    "record every result as you go.")

flow.append(k.disclaimer(
    "Your permit card lists the inspections your job requires — it governs."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- who sets it
flow += k.h2_tight("WHAT THE STATE SETS AND WHAT YOUR JURISDICTION SETS")
flow.append(k.body(
    "The <b>definitions</b> below are statewide. They come from Section R109 "
    "of the California Residential Code — Chapter 1, Division II — and they "
    "say what condition the work must be in before each inspection can be "
    "called. The <b>list of inspections your particular job needs</b>, and the "
    "order your department calls them in, is local; it is printed on your "
    "permit card. Where the two differ, your permit card and your inspector "
    "govern."))
flow.append(k.body(
    "California also gives the building official an express reserve power: "
    "under § R109.1.5 they \"<i>shall have the authority to make or require "
    "any other inspections to ascertain compliance with this code and other "
    "laws</i>.\" So the list is a floor, not a ceiling."))

flow.append(k.callout_long("The rule that governs everything else", [
    Paragraph("\"<i>Work shall not be done beyond the point indicated in each "
              "successive inspection without first obtaining the approval of "
              "the building official … Any portions that do not comply shall "
              "be corrected and such portion shall not be covered or concealed "
              "until authorized by the building official.</i>\" (§ R109.4)",
              S["body"]),
    Paragraph("And the standing note to § R109.1: \"<i>Reinforcing steel or "
              "structural framework of any part of any building or structure "
              "shall not be covered or concealed without first obtaining the "
              "approval of the enforcing agency.</i>\" Covering work before it "
              "is signed off is the one mistake that reliably costs real money "
              "in California, because the remedy is opening it up again.",
              S["body"]),
]))

# ---------------------------------------------------------------- the sequence
flow += k.h2_tight("THE SEQUENCE — WHAT MUST BE COMPLETE BEFORE YOU CALL",
                   reserve=2.05)
seq = [
    ("1. Foundation and footings",
     "After poles or piers are set, or trenches or basement areas excavated, "
     "any required forms erected, and any required reinforcing steel in place "
     "and supported — <b>prior to the placing of concrete</b>. Includes "
     "excavations for thickened slabs supporting bearing walls, partitions or "
     "equipment. Materials must be on site, except ready-mixed concrete.",
     "§ R109.1.1"),
    ("2. Concrete slab / under-floor",
     "After in-slab or under-floor reinforcing steel and building service "
     "equipment, conduits and piping are installed, but <b>before any concrete "
     "is placed or floor sheathing — including the subfloor — is "
     "installed</b>.",
     "§ R109.1.1.1"),
    ("3. Rough plumbing, mechanical, gas, electrical",
     "Prior to covering or concealment, before fixtures or appliances are set, "
     "and <b>prior to framing inspection</b>. Note the order: California puts "
     "the trade roughs <i>before</i> the frame inspection, not alongside it.",
     "§ R109.1.2"),
    ("4. Floodplain elevation",
     "Only in a flood hazard area: upon placement of the lowest floor and "
     "<b>before further vertical construction</b>, documentation of the "
     "lowest-floor elevation, <b>prepared and sealed by a registered design "
     "professional</b>.",
     "§ R109.1.3"),
    ("5. Frame and masonry",
     "After roof, masonry, framing, firestopping, draftstopping and bracing "
     "are in place, chimneys and vents to be concealed are complete, and the "
     "<b>rough electrical, plumbing, heating, wires, pipes and ducts are "
     "approved</b>.",
     "§ R109.1.4"),
    ("6. Moisture content verification",
     "Moisture content of framing members is verified against the California "
     "Green Building Standards Code, Chapter 4, Division 4.5. Wet framing "
     "fails, and drying it is a schedule problem, not a paperwork one.",
     "§ R109.1.4.1"),
    ("7. Lath and gypsum board",
     "After lathing and gypsum board, interior and exterior, is in place — but "
     "<b>before any plastering is applied</b> or joints and fasteners are "
     "taped and finished. On a stucco house this is its own milestone.",
     "§ R109.1.4.2"),
    ("8. Balcony / elevated walking surface waterproofing",
     "Where a balcony or elevated walking surface is exposed to rain, snow or "
     "irrigation and the structural framing is protected by an impervious "
     "moisture barrier, <b>no element of that barrier system may be concealed "
     "until inspected and approved</b>.",
     "§ R109.1.5.3"),
    ("9. Fire-resistance-rated construction",
     "Where rated construction is required — between dwelling units or because "
     "of location on the property — after lath or gypsum panels are in place "
     "but before plaster or taping. Joints and penetrations may not be "
     "concealed until inspected.",
     "§ R109.1.5.1"),
    ("10. Final",
     "After the permitted work is complete and <b>prior to occupancy</b>. In a "
     "flood hazard area the elevation documentation must be in before the "
     "final. And the operation and maintenance manual must be in the building "
     "— see below.",
     "§ R109.1.6"),
]
rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in seq]
flow.append(k.ref_table(
    "Standard California residential inspection sequence",
    [k.cellp("Inspection", bold=True),
     k.cellp("What must be complete / what is verified", bold=True),
     k.cellp("Code", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - 0.95 * inch, 0.95 * inch]))
flow.append(k.cite(
    "Quoted from the 2025 California Residential Code, Chapter 1, Division II, "
    "Administration, § R109.1.1 through § R109.1.6.2. Your jurisdiction will "
    "add its own — energy and HERS verification, solar, septic and well "
    "sign-offs, fire department inspections, and a grading final where a "
    "grading permit was issued. Verified August 2026."))

flow.append(k.callout_long(
    "Two inspections that are pure California — and one document at the final", [
        Paragraph("<b>Moisture content verification (§ R109.1.4.1).</b> Most "
                  "states inspect framing. California also checks that the "
                  "framing is <i>dry enough</i>, against CALGreen Chapter 4, "
                  "Division 4.5. If your lumber has been rained on and "
                  "wrapped, you can fail a frame inspection on moisture alone. "
                  "Plan your dry-in around it.", S["body"]),
        Paragraph("<b>Balcony waterproofing (§ R109.1.5.3).</b> California "
                  "requires the impervious moisture barrier under any "
                  "weather-exposed balcony, deck or elevated walking surface "
                  "to be inspected <b>before it is covered</b>. If your design "
                  "has any elevated exterior walking surface, that is a hold "
                  "point most owner-builders discover after they have decked "
                  "over it.", S["body"]),
        Paragraph("<b>The operation and maintenance manual (§ R109.1.6.2).</b> "
                  "\"<i>At the time of final inspection, a manual, compact "
                  "disc, web-based reference or other media acceptable to the "
                  "enforcing agency shall be placed in the building</i>\" per "
                  "CALGreen Chapter 4, Division 4.4. It is a real condition of "
                  "your final. Start collecting appliance manuals, equipment "
                  "data and maintenance instructions from your first "
                  "delivery — assembling it the week of your final is "
                  "miserable.", S["body"]),
    ]))

# ---------------------------------------------------------------- duties
flow += k.h2_tight("YOUR DUTIES, AND WHAT THE BUILDING OFFICIAL MAY DO")
flow.append(k.bullet(
    "<b>Calling the inspection is your job.</b> \"<i>It shall be the duty of "
    "the permit holder or their agent to notify the building official that "
    "such work is ready for inspection</i>,\" and the duty of the person "
    "requesting it \"<i>to provide access to and means for inspection of such "
    "work</i>.\" Ladders, keys, a safe route — yours. (§ R109.3)"))
flow.append(k.bullet(
    "<b>Special inspections are a separate regime.</b> Section R109.1.5.2 "
    "sends you to <b>California Building Code Chapter 17</b>. In California's "
    "seismic design categories these are common on engineered work. You pay "
    "for them, an approved special inspector performs them, and they are "
    "reported directly to the building official — ask at plan check whether "
    "your approved plans carry a special inspection schedule."))
flow.append(k.cite(
    "One thing the code does <b>not</b> give you: a deadline. The enforcing "
    "agency must make the inspections \"<i>within a reasonable time</i>\" of "
    "your notification. There is no numeric statutory turnaround — any 24- or "
    "48-hour figure you have heard is local practice, and in busy California "
    "jurisdictions it is often longer. Ask at your first inspection how far "
    "ahead to book, so it is not a surprise at your fifth."))

# ---------------------------------------------------------------- certificate
flow += k.h2_tight("THE CERTIFICATE AT THE END — AND YOUR UTILITIES")
flow.append(k.body(
    "\"<i>A building or structure shall not be used or occupied in whole or in "
    "part … until the building official has issued a certificate of occupancy "
    "therefor.</i>\" (§ R110.1) California uses the plain name — certificate "
    "of occupancy — and it issues after the building official inspects and "
    "finds no violations."))
flow.append(k.body(
    "Worth knowing what it must contain (§ R110.2), because two of the items "
    "matter later: <b>the edition of the code under which the permit was "
    "issued</b> — your proof of which rulebook your house was built to — and "
    "<b>whether an automatic sprinkler system is provided and whether it was "
    "required</b>. Keep the certificate with your insurance papers; both "
    "entries answer questions an insurer or a buyer will eventually ask."))
flow.append(k.body(
    "A <b>temporary certificate of occupancy</b> may be issued before the "
    "whole work is complete, \"<i>provided that such portion or portions shall "
    "be occupied safely</i>,\" and the building official sets the period it is "
    "valid for (§ R110.3). A certificate can also be <b>suspended or "
    "revoked</b> in writing if it was issued in error or on incorrect "
    "information (§ R110.4)."))

flow.append(k.callout_long("No power and no water until they say so", [
    Paragraph("\"<i>A person shall not make connections from a utility, a "
              "source of energy, fuel or power, or water system or sewer "
              "system to any building or system that is regulated by this code "
              "for which a permit is required, until approved by the building "
              "official.</i>\" (§ R111.1)", S["body"]),
    Paragraph("Your utility will want the building department's release before "
              "it energizes permanent service, and the lead time on a new "
              "service connection in California is frequently measured in "
              "months, not weeks. Apply for permanent service <b>early</b> and "
              "ask the utility what it needs from the building department, in "
              "what form. A finished house waiting on a meter is a common and "
              "entirely avoidable ending.", S["body"]),
]))

# ---------------------------------------------------------------- when it goes wrong
flow += k.h2_tight("WHEN AN INSPECTION GOES WRONG")
wrong = [
    [k.cellp("<b>You failed</b>"),
     k.cellp("The building official must \"<i>notify the permit holder or an "
             "agent … wherein the same fails to comply</i>.\" Fix exactly what "
             "is named, and do not cover it until authorized. Re-inspection "
             "fees and how soon you may re-call are local — ask early."),
     k.cellp("§ R109.4")],
    [k.cellp("<b>You want to change something</b>"),
     k.cellp("Approved construction documents govern. Get a revision approved "
             "before you build the change; on engineered work that usually "
             "means the engineer of record revises and re-stamps first."),
     k.cellp("§ R106")],
    [k.cellp("<b>You got a stop work order</b>"),
     k.cellp("Work stops on the portion named until the order is released. "
             "Get the order in writing and address exactly what it cites."),
     k.cellp("§ R114")],
    [k.cellp("<b>You disagree with the ruling</b>"),
     k.cellp("There is a formal route: the code provides a means of appeal "
             "from the building official's decision. Ask your department for "
             "the appeal procedure and its deadline in writing — the clock is "
             "usually short and local."),
     k.cellp("§ R112")],
    [k.cellp("<b>Your permit went stale</b>"),
     k.cellp("A permit remains valid if work on the site was commenced within "
             "<b>12 months</b> of issuance and has not been abandoned. "
             "Extensions of not more than <b>180 days</b> each may be granted "
             "in writing for justifiable cause — you have to ask."),
     k.cellp("H&amp;S § 18938.6")],
]
flow.append(k.ref_table(
    "Failures, changes, stop orders, appeals, and expiry",
    [k.cellp("Situation", bold=True), k.cellp("What to do", bold=True),
     k.cellp("Authority", bold=True)],
    wrong, [1.45 * inch, CW - 1.45 * inch - 1.15 * inch, 1.15 * inch]))
flow.append(k.cite(
    "Permit validity is statutory, not merely a code provision: Health &amp; "
    "Safety Code § 18938.6(a) and (b), added by AB 2913 (Stats. 2018, Ch. 655). "
    "The statutory test is <b>commencement within 12 months and no "
    "abandonment</b> — the 180-day figure in that section is the maximum "
    "length of a discretionary extension, not a rolling inspection clock. If "
    "your jurisdiction applies a rolling-inspection rule, that is its adopted "
    "code provision or ordinance; ask which, and get the expiry date printed "
    "on your permit."))

# ---------------------------------------------------------------- the log
flow += k.h2_tight("INSPECTION LOG — RECORD EVERY ONE")
flow.append(k.body(
    "Fill this in as it happens, not from memory. If a result is ever "
    "disputed, or a later inspector questions earlier work, this page and your "
    "photographs are the record you have. Photograph every rough-in before it "
    "is covered, whatever the inspector says."))

log_header = [k.cellp("Inspection", bold=True),
              k.cellp("Called", bold=True),
              k.cellp("Held", bold=True),
              k.cellp("Result", bold=True),
              k.cellp("Inspector", bold=True),
              k.cellp("Corrections required / notes", bold=True)]
log_names = [
    "Foundation / footings", "Slab / under-floor", "Plumbing rough",
    "Mechanical / gas rough", "Electrical rough", "Floodplain elevation",
    "Frame and masonry", "Moisture content", "Balcony waterproofing",
    "Lath / gypsum board", "Insulation", "Energy / HERS verification",
    "Septic / well", "Final — building",
]
log_rows = [[k.cellp(n) if n else "", "", "", "", "", ""] for n in log_names]
widths = [1.22 * inch, 0.66 * inch, 0.66 * inch, 0.78 * inch, 0.98 * inch]
widths.append(CW - sum(widths))
flow.append(d.titled_table(
    "Inspection log", log_header, log_rows, widths, S,
    row_heights=[28] * len(log_rows)))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Certificate of occupancy issued:", 0.55),
                         ("Number:", 0.45)]))

flow.append(Spacer(1, 10))
flow.append(k.sources_table([
    ("Foundation before concrete; slab and under-floor before concrete or "
     "subfloor", "2025 CRC § R109.1.1, § R109.1.1.1"),
    ("Trade roughs before the framing inspection; frame and masonry only "
     "after those roughs are approved", "§ R109.1.2, § R109.1.4"),
    ("Floodplain lowest-floor elevation, sealed, before going vertical",
     "§ R109.1.3"),
    ("Framing moisture content verified against CALGreen; lath and gypsum "
     "before plaster or taping", "§ R109.1.4.1, § R109.1.4.2"),
    ("Balcony moisture barrier and fire-rated construction not concealed "
     "until inspected; special inspections per CBC Chapter 17",
     "§ R109.1.5.1–.5.3"),
    ("Building official may require any other inspection; final after "
     "completion and prior to occupancy, with the operation and maintenance "
     "manual in the building",
     "§ R109.1.5, § R109.1.6, § R109.1.6.2"),
    ("Permit holder calls and provides access; reports of approved agencies "
     "may be accepted; no work past an inspection point without approval, and "
     "nothing concealed until authorized",
     "§ R109.2, § R109.3, § R109.4"),
    ("No occupancy without a certificate; it names the code edition and the "
     "sprinkler status; temporary CO available",
     "§ R110.1, § R110.2, § R110.3"),
    ("No utility connection until approved by the building official",
     "§ R111.1"),
    ("Permit valid on commencement within 12 months; 180-day extensions",
     "H&amp;S § 18938.6"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ca-permit-kit",
                       "CA.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
