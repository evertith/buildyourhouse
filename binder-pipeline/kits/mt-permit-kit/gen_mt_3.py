#!/usr/bin/env python3
"""MT.3 Inspection Sequence — Montana.

Montana's inspection problem is the opposite of most states'. The question is
not "what order do the inspections come in" but "will anyone inspect this house
at all, and if not, what do I have to show for it afterwards." This document
handles both cases: the certified-jurisdiction ladder, and the far more common
rural build where the only inspection is electrical and the only compliance
record is the one you write yourself.

Sources verified August 2026:
  50-60-102(1)(a),(2)  the state may not enforce the building code for
                       residential buildings of fewer than five dwelling units
  50-60-102(5)(b)(ii)  the energy provisions are enforced through builder
                       self-certification for exactly those buildings
  50-60-802(1)         the certification is written, to the building owner, at
                       the conclusion of construction
  50-60-604            electrical inspections and permits — DLI or a certified
                       county, city, or town; the inspector must demand proof
                       of licensure from anyone on site required to hold it
  50-60-605            no power supplier may connect or energize without the
                       electrical permit delivered to it; 14-day temporary
                       connections may be authorized by rule
  50-60-607            energizing without a permit is a misdemeanor
  50-60-106(2)(a),(d),(e)  certified locals examine plans, order remedies
                       during and in the course of construction, and issue
                       certificates of occupancy under 50-60-107
  50-60-106(2)(c)      the department's single-family checklist, and the
                       10-working-day permit-or-disapproval clock for a
                       contractor who attaches a completed one
  50-60-302(1)(c)      a local inspector must be a state-licensed journeyman in
                       the craft inspected or nationally certified

Still deliberately hedged: the residential inspection ladder itself, which no
Montana statute enumerates — it is labeled TYPICAL and the reader is told the
permit card governs; every local scheduling method; and the septic inspection
sequence, which belongs to the county and is worked in MT.2.
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

FORM_ID = "MT.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Who inspects a Montana house — which in much of the state is almost "
    "nobody — how the electrical inspection and the power-supplier release "
    "actually work, and the record you have to build yourself when no "
    "inspector is coming.")

flow.append(k.disclaimer(
    "Where a certified local building program has jurisdiction, its permit "
    "card lists the inspections your job requires and it governs. The "
    "electrical inspection is additional to it unless that same jurisdiction "
    "is certified for electrical too."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- two worlds
flow += k.h2_tight("FIRST DECIDE WHICH MONTANA YOU ARE BUILDING IN")
flow.append(k.body(
    "Everything on the following pages branches on one fact you settled in "
    "MT.1: has the county, city, or town where your parcel sits adopted the "
    "state building code for residential buildings of fewer than five dwelling "
    "units, and is its enforcement program certified under 50-60-302? If yes, "
    "you get a conventional ladder and a certificate of occupancy at the end. "
    "If no, the state \"<i>may not enforce</i>\" the building code for your "
    "house (50-60-102(2)) — <b>no plan review, no framing inspection, no "
    "certificate of occupancy</b> — and the only inspection anyone performs is "
    "the electrical one."))

world_rows = [
    [k.cellp("<b>Building</b>"),
     k.cellp("Full ladder: footing through final, plus plan review. "
             "Certificate of occupancy issued at the end (50-60-106(2)(e); "
             "50-60-107)."),
     k.cellp("<b>None.</b> The state may not enforce the code for your house "
             "(50-60-102(2)) and no local program exists to. Nobody visits.")],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("Local, if the jurisdiction is certified for electrical; "
             "otherwise still the Department of Labor &amp; Industry "
             "(50-60-604). Ask — certification is per craft."),
     k.cellp("<b>Required.</b> DLI inspects and issues the permit "
             "(50-60-604). This is the only inspection most rural Montana "
             "houses ever get.")],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp("Local permit and inspection where a local code covers plumbing "
             "and provides inspection procedures — which removes the state "
             "permit (50-60-506(3))."),
     k.cellp("No permit at all if you personally do the work as owner of the "
             "residential property (50-60-506(4)). Nobody inspects it "
             "either.")],
    [k.cellp("<b>Energy</b>"),
     k.cellp("Verified through the local program where the building is "
             "subject to the code."),
     k.cellp("<b>You certify it yourself</b>, in writing, at the end "
             "(50-60-102(5)(b)(ii); 50-60-802(1)).")],
    [k.cellp("<b>Septic and water</b>"),
     k.cellp("County and DEQ, on their own schedule — unchanged either way. "
             "See MT.2.", ),
     k.cellp("County and DEQ, on their own schedule — unchanged either way. "
             "See MT.2.")],
]
flow.append(k.ref_table(
    "The same house, two completely different inspection regimes",
    [k.cellp("Discipline", bold=True),
     k.cellp("Inside a certified local program", bold=True),
     k.cellp("Outside one — most of Montana by area", bold=True)],
    world_rows, [0.95 * inch, (CW - 0.95 * inch) / 2,
                 (CW - 0.95 * inch) / 2]))
flow.append(k.cite(
    "50-60-102(2), (5)(b)(ii); 50-60-106(2)(e); 50-60-107; 50-60-302; "
    "50-60-506(3), (4); 50-60-604; 50-60-802(1), MCA. Read August 2026. "
    "Certification is granted per discipline, so a jurisdiction can run a "
    "building program and leave electrical with the state — confirm each "
    "separately (MT.4)."))

# ---------------------------------------------------------------- electrical
flow += k.h2_tight("THE ELECTRICAL INSPECTION — THE ONE THAT ALWAYS HAPPENS")
flow.append(k.body(
    "Whoever else does or does not visit your site, this one does. The "
    "statute names who: \"<i>The department of labor and industry or an "
    "authorized representative or a county, city, or town certified to perform "
    "an inspection pursuant to 50-60-302 <b>shall inspect electrical "
    "installations, issue electrical permits for these installations, and "
    "establish and charge a reasonable and uniform fee</b></i>\" (50-60-604). "
    "Three operational facts follow from that sentence and the two after it."))

el_rows = [
    [k.cellp("<b>Buy the permit first</b>"),
     k.cellp("The permit is the thing your power supplier will demand, and it "
             "is issued by DLI or a certified local program — not by your "
             "electrician's goodwill. A homeowner relying on the exemption in "
             "37-68-103(3)(a) still buys it, because that exemption reaches "
             "the license only (MT.1).")],
    [k.cellp("<b>Expect to show licenses</b>"),
     k.cellp("\"<i>As part of any inspection, the inspector <b>shall require "
             "proof of licensure</b> from any person who is required to be "
             "licensed who is involved with or, in the inspector's judgment, "
             "appears to be involved with electrical installations if the "
             "person is on the site</i>\" (50-60-604). Violations are reported "
             "to the board of electricians. If a friend is helping you wire, "
             "understand what that means before inspection day.")],
    [k.cellp("<b>Inspectors cover distance</b>"),
     k.cellp("Montana is the fourth-largest state by area with a small number "
             "of electrical inspectors. Book early, be specific about "
             "directions to a rural site, and have the work genuinely ready — "
             "a wasted trip on a two-hour drive is not a rescheduling, it is "
             "a week. Confirm the current scheduling method with the office "
             "that issued your permit and write it in the block below.")],
]
flow.append(k.ref_table(
    "What the electrical statute actually obliges",
    [k.cellp("Point", bold=True), k.cellp("What it means on your job",
                                          bold=True)],
    el_rows, [1.5 * inch, CW - 1.5 * inch]))
flow.append(Spacer(1, 6))

flow.append(Paragraph("The mechanics, from the department's own rules",
                      S["h3"]))
mech_rows = [
    [k.cellp("<b>Two inspections</b>"),
     k.cellp("Not a long ladder — a <b>cover (rough-in)</b> inspection and a "
             "<b>final</b>. The permittee, \"<i>whether an electrical "
             "contractor or a homeowner</i>,\" notifies the area inspector "
             "when the work is ready (ARM 24.301.441). On approval at final "
             "the inspector applies a <b>green approved tag</b> "
             "(ARM 24.301.451).")],
    [k.cellp("<b>The 48-hour rule —<br/>read this before you "
             "insulate</b>"),
     k.cellp("\"<i>Insulation and wallboard <b>shall not be applied prior to "
             "inspection unless 48 hours, excluding Saturdays, Sundays and "
             "holidays, have expired</b> after the electrical installation is "
             "complete and notice to inspect has been received</i>\" "
             "(ARM 24.301.441). That is a genuine self-release valve for a "
             "remote site: give proper notice, wait two business days, and "
             "you may close up. Document the notice and the date.")],
    [k.cellp("<b>Permits run 18 months</b>"),
     k.cellp("Valid <b>18 months</b>, with one <b>18-month renewal</b> "
             "(ARM 24.301.431(9)). An owner-build routinely outruns the first "
             "term — put the expiry in your calendar the day you buy it. "
             "A transfer form exists if the permit needs to move.")],
    [k.cellp("<b>Order of operations</b>"),
     k.cellp("No electrical permit issues until the building permit has been "
             "issued \"<i>or it has been determined that a building permit is "
             "not required</i>\" (ARM 24.301.431(12)). For an exempt house "
             "that determination is the thing you supply — the department "
             "provides for the owner to establish the exemption in writing "
             "(ARM 24.301.142(4)). Expect to say so in the application, and "
             "keep a copy.")],
]
flow.append(k.ref_table(
    "How the state electrical inspection actually runs",
    [k.cellp("Point", bold=True), k.cellp("The rule", bold=True)],
    mech_rows, [1.6 * inch, CW - 1.6 * inch]))
flow.append(k.cite(
    "ARM 24.301.431(9), (12); 24.301.441; 24.301.451; 24.301.142(4). The "
    "department reproduces these rules in its Electrical Information "
    "Pamphlet, which it labels unofficial guidance — read the rules "
    "themselves before relying on a deadline. Read August 2026."))
flow.append(Spacer(1, 4))

flow.append(k.callout_long("The finish line is the meter, not the final", [
    Paragraph("\"<i>Except for temporary connections that the department of "
              "labor and industry may authorize by rule for a period <b>not "
              "exceeding 14 days</b> without a preconnection inspection, "
              "<b>power suppliers may not connect with or energize an "
              "electrical installation under this part unless the owner or a "
              "licensed electrical contractor has delivered to the power "
              "supplier an electrical permit covering the installation</b></i>"
              "\" (50-60-605). \"Power suppliers\" expressly includes "
              "<b>cooperatives</b> and municipalities — a rural electric co-op "
              "is bound exactly as an investor-owned utility is.", S["body"]),
    Paragraph("And energizing around them is a crime: any person other than a "
              "power supplier who energizes an installation for which no "
              "electrical permit has been issued \"<i>is guilty of a "
              "<b>misdemeanor</b></i>\" (50-60-607). That reaches the "
              "temptation everyone on a long rural build eventually has — "
              "backfeeding the panel from a generator to run heat while you "
              "finish. Sort the permit out first.", S["body"]),
    Paragraph("<b>The permit is also your cut-in card.</b> Montana's "
              "mechanism is unusually simple: the utility may energize "
              "provisionally on receipt of <b>the power supplier's copy of "
              "the electrical permit</b> (ARM 24.301.431(5)), with the "
              "provisional designation removed when the final passes. A "
              "certified local jurisdiction may additionally demand proof of "
              "an approved inspection first. Montana's largest "
              "investor-owned utility says it plainly in its own new-service "
              "documents: \"<i>According to Montana law, you must obtain and "
              "provide our New Construction office a copy of an electrical "
              "permit.</i>\" Rural cooperatives ask for the same thing.",
              S["body"]),
    Paragraph("<b>Plan the sequence backwards from the connection date.</b> "
              "Ask your power supplier, early and in writing: line extension "
              "cost and lead time; how much footage is included before "
              "charges start; whether it wants a temporary construction "
              "service and how long that lasts; who digs, and who supplies "
              "trench, conduit, and pull rope; and how long after your "
              "electrical final it schedules the meter set. Expect it to "
              "require a <b>permanent assigned address</b> before it will do "
              "anything — on a rural build the utility, not the county, is "
              "usually what forces you to go get one. On a remote parcel the "
              "line extension is routinely the longest lead item on the whole "
              "job, ahead of anything a permit office does.", S["body"]),
]))
flow.append(k.cite(
    "50-60-604, 50-60-605, 50-60-607, MCA; 37-68-103(3)(a), MCA. Read August "
    "2026. The 14-day temporary connection is authorized by rule — confirm "
    "the current rule in ARM Title 24, chapter 301 at rules.mt.gov and confirm "
    "the practice with your own power supplier."))

# ---------------------------------------------------------------- ladder
flow += k.h2_tight("THE TYPICAL LADDER — AND WHO OWNS EACH RUNG")
flow.append(k.body(
    "No Montana statute enumerates residential inspections; where a certified "
    "program has jurisdiction, its adopted code and permit card do. The order "
    "below is the <b>typical</b> shape an IRC-based code produces, annotated "
    "with what happens on the same rung when no building program has "
    "jurisdiction. Verify names and count against your own permit card."))

seq = [
    ("1. Footing / setback", "LOCAL — or nobody",
     "Forms and steel before concrete. Where nobody inspects, this is the rung "
     "to hire your own engineer for: a footing is unreachable afterwards."),
    ("2. Foundation / damproofing", "LOCAL — or nobody",
     "Before backfill. Frost depth in Montana runs deep and is set locally; "
     "confirm the figure for your site in writing and record it."),
    ("3. Underground plumbing / slab", "LOCAL — or nobody",
     "Under-slab drain, waste, and vent tested before the pour. No state "
     "plumbing inspection exists where you did the work yourself under "
     "50-60-506(4)."),
    ("4. Rough electrical", "DLI or certified LOCAL",
     "Wiring complete and open. <b>This one happens everywhere.</b> Book it "
     "early — the inspector may be driving a long way."),
    ("5. Rough plumbing", "LOCAL — or nobody",
     "Local where a local code covers plumbing with inspection procedures "
     "(50-60-506(3)); otherwise not inspected if you did it yourself."),
    ("6. Framing / sheathing", "LOCAL — or nobody",
     "Where a local program is involved this is called after the trade "
     "rough-ins pass, including the electrical one it does not control."),
    ("7. Insulation and air barrier", "LOCAL — or YOU",
     "Against the adopted energy code. Where nobody inspects, this is the "
     "rung your own energy certification will rest on — photograph it."),
    ("8. Final electrical", "DLI or certified LOCAL",
     "The approval that releases the power supplier to set a permanent meter "
     "(50-60-605)."),
    ("9. Septic final", "COUNTY / DEQ",
     "Before the system is covered and before it is used — the county's "
     "sequence, not the building department's. See MT.2."),
    ("10. Building final / CO", "LOCAL only",
     "Only where a certified local program has jurisdiction (50-60-106(2)(e); "
     "50-60-107). Elsewhere <b>there is no certificate of occupancy</b> — see "
     "below."),
    ("11. Energy certification", "YOU",
     "\"<i>At the conclusion of construction</i>\" the builder certifies in "
     "writing to the owner (50-60-802(1)). As owner-builder you are both."),
]
rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in seq]
flow.append(k.ref_table(
    "Typical order — the permit card governs where one exists",
    [k.cellp("Inspection", bold=True), k.cellp("Whose", bold=True),
     k.cellp("What must be complete", bold=True)],
    rows, [1.7 * inch, 1.25 * inch, CW - 2.95 * inch]))
flow.append(Spacer(1, 6))

flow.append(k.callout("If a certified program does have your job", [
    Paragraph("Two rules worth holding it to. Its inspectors must themselves "
              "be <b>state-licensed journeymen in the craft they are "
              "inspecting</b>, or certified by an approved national body "
              "(50-60-302(1)(c)). And the department publishes a "
              "<b>single-family dwelling checklist</b> that certified "
              "jurisdictions must make available; a contractor who attaches a "
              "completed one to the plans is entitled to the building permit "
              "or a notice of plan disapproval <b>within 10 working days</b> "
              "(50-60-106(2)(c)). Ask for that checklist by name — it is the "
              "closest thing Montana publishes to a statewide submittal list, "
              "and it comes with a clock attached.", S["body"]),
]))

# ---------------------------------------------------------------- no CO
flow += k.h2_tight("WHEN NOBODY IS COMING — BUILD THE RECORD YOURSELF")
flow.append(k.body(
    "This is the part of Montana owner-building that costs people money years "
    "later. Where no building program has jurisdiction there is no plan "
    "review, no inspection card, and <b>no certificate of occupancy</b> — so "
    "when a lender's appraiser, an insurance underwriter, or a buyer's home "
    "inspector asks what this house was built to and who checked, the honest "
    "answer is whatever you can document. Nobody else is keeping that record. "
    "Collect these as you go, not at the end:"))
flow.append(k.checklist([
    "<b>The electrical permit and the final electrical approval</b>, plus "
    "whatever your power supplier accepted before setting the meter "
    "(50-60-605). This is the one genuinely independent inspection your house "
    "received — it is worth more to a future buyer than you think.",
    "<b>Your written energy certification</b> under 50-60-802(1), naming the "
    "adopted edition you built to, dated and signed at the conclusion of "
    "construction — with the insulation R-values, window U-factors, and "
    "equipment efficiencies you actually installed listed on it.",
    "<b>The septic permit, the approved design, and the county's final "
    "approval</b>, plus any as-built the county requires — and the <b>well "
    "log or water-supply documentation</b> and whatever you filed with DNRC "
    "(MT.2).",
    "<b>The structural basis of the roof</b>: the ground snow load figure you "
    "designed to, where it came from, and any engineer's letter, calculation, "
    "or stamped truss package. In a state where nobody checks this, the "
    "documentation <i>is</i> the assurance.",
    "<b>Photographs of everything that gets covered</b> — footing steel before "
    "the pour, foundation waterproofing before backfill, framing connections, "
    "plumbing tests, insulation and air sealing before drywall. Date them. "
    "This is the substitute for an inspection card, and it is free.",
    "<b>Receipts and product data</b> for the assemblies that matter: "
    "windows, insulation, roofing, trusses, the panel and service equipment. "
    "Keep them with the certification, not in a shoebox.",
]))

# ---------------------------------------------------------------- logs
flow += k.h2_tight("INSPECTION AND MILESTONE LOG")
flow.append(k.body(
    "Log every inspection that happens — and every milestone that passes with "
    "nobody watching. Where no inspector signs a card, this page is the card."))
log_header = [k.cellp("Stage", bold=True),
              k.cellp("Authority / self", bold=True),
              k.cellp("Called", bold=True),
              k.cellp("Held", bold=True),
              k.cellp("Result", bold=True),
              k.cellp("Corrections / photos taken / notes", bold=True)]
log_names = [
    "Footing / setback", "Foundation / damproofing",
    "Underground plumbing / slab", "Rough electrical", "Rough plumbing",
    "Framing / sheathing", "Insulation / air barrier", "Final electrical",
    "Power supplier — permit delivered", "Septic final",
    "Building final / CO (if any)", "Energy certification signed", "",
]
log_rows = [[k.cellp(n) if n else "", "", "", "", "", ""] for n in log_names]
widths = [1.45 * inch, 0.92 * inch, 0.7 * inch, 0.55 * inch, 0.72 * inch]
widths.append(CW - sum(widths))
flow.append(d.titled_table(
    "Record every stage as it happens — nobody else keeps this record",
    log_header, log_rows, widths, S,
    row_heights=[28] * len(log_rows)))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Electrical inspector / office:", 0.5),
                         ("Permit #:", 0.25), ("Issued:", 0.25)]))
flow.append(d.FillInRow([("Power supplier:", 0.4),
                         ("Meter set:", 0.3), ("CO issued:", 0.3)]))
flow.append(d.FillInRow([("Ground snow load designed to:", 0.5),
                         ("Source:", 0.5)]))

flow.append(Spacer(1, 10))
flow.append(k.sources_table([
    ("The state may not enforce the building code for residential buildings of "
     "fewer than five dwelling units", "50-60-102(2), MCA"),
    ("The energy provisions are enforced for those buildings through builder "
     "self-certification", "50-60-102(5)(b)(ii); 50-60-802(1), MCA"),
    ("Electrical inspections and permits by DLI or a certified county, city, "
     "or town; the inspector must require proof of licensure on site",
     "50-60-604, MCA"),
    ("No power supplier — including a cooperative — may connect or energize "
     "without the electrical permit delivered to it; temporary connections up "
     "to 14 days by rule", "50-60-605, MCA"),
    ("Energizing an installation with no electrical permit is a misdemeanor",
     "50-60-607, MCA"),
    ("Certified locals examine plans, order remedies during construction, and "
     "issue certificates of occupancy",
     "50-60-106(2)(a), (d), (e); 50-60-107, MCA"),
    ("The department's single-family checklist and the 10-working-day "
     "permit-or-disapproval clock", "50-60-106(2)(c), MCA"),
    ("A local inspector must be a state-licensed journeyman in the craft "
     "inspected or nationally certified", "50-60-302(1)(c), MCA"),
    ("No state plumbing permit where a local code covers plumbing with "
     "inspection procedures; none at all where the owner personally does the "
     "work", "50-60-506(3), (4), MCA"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "mt-permit-kit",
                       "MT.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
