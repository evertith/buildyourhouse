#!/usr/bin/env python3
"""NE.3 Inspection Sequence.

Every Nebraska claim in this document was read out of its primary source in
September 2026 and is cited on-page.

The organizing idea: Nebraska fixes exactly ONE inspection track by statute —
electrical — and fixes it in unusual detail: a request due before you start, a
one-week response clock, a rough-in that must precede concealment, a
correction-order window of 10 to 17 days, and a power company that may not
connect you until you certify. Every other inspection on a house (footing,
framing, plumbing, insulation, final) exists only where a city or county chose
to run a program, and the state cannot run one. So this document prints the
electrical track as law, the two registrations (septic, well) as the other
mandatory records, and the building inspections as "where a program exists" —
and then spends a page on what to do where nobody is required to inspect you.

Verified sources:
  § 81-2124(3)          new single-family service equipment is inspected
  § 81-2125(1)          state inspection yields to a local certified program
  § 81-2126             request at or before commencement; 14-day letter; $250
  § 81-2129             certificate to the utility; supplier may refuse
  § 81-2134(2),(3)      rough-in before concealment; "within one week";
                        energizing before inspection is at your risk
  § 81-2136, -2137, -2138  condemnation, disconnection, correction orders
                        (10-17 calendar days)
  § 81-2141, -2142      appeal to the board
  § 81-2143(1)          Class IV felony (eff. 7-18-2026)
  Board Rule 12         temporary service: five working days' notice; verbal
                        authorization to energize
  Board Rule 13         five-month permit life; doorknob notices
  SED Homeowner Handout (5-22-24)   inspection types; rough-in "before
                        fiberglass insulation or drywall"; ~14 working days to
                        correct; the yellow permit card; forwarding to the
                        power supplier
  § 81-15,248(2); Title 124 ch. 10   septic registration within 45 days;
                        owner gets a copy
  § 46-602(1), -1241    well registration within 60 days; well log
  § 71-6409             (eff. 7-18-2026) virtual inspections; no
                        self-inspection
  § 81-1617, -1625      energy inspection only with permission or warrant;
                        two-year correction window
  Lincoln homeowner permit pages   inspect before concealment and at
                        completion; 120 days

DELIBERATELY NOT CLAIMED, and why:
  - Any inspection list attributed to the state. None exists. The local list
    is printed as typical and unattributed.
  - A certificate-of-occupancy rule. No state rule exists; local only.
  - A response time for any local building inspection. None is fixed by
    statute.
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

FORM_ID = "NE.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "One inspection track the statute fixes, two registrations that stand in "
    "for the rest — and what to do where nobody is required to inspect you.")

flow.append(k.disclaimer(
    "The electrical sequence below is statutory and applies on every parcel in "
    "the state. Everything else is local: where your city or county runs a "
    "building program its schedule governs, and where it does not, no "
    "building inspection is required of you by anyone."))
flow.append(Spacer(1, 10))

# ------------------------------------------------- two situations
flow += k.h2_tight("WHAT YOU GET DEPENDS ON WHO RUNS A PROGRAM", reserve=2.0)
flow.append(k.body(
    "NE.1 established that the code binds your house either way. Here is what "
    "that means once the concrete starts moving. <b>Read down the electrical "
    "column.</b> It is the same in both rows, and that is the point almost "
    "every Nebraska owner-builder misses."))
rows = [
    [k.cellp("<b>A city or county building program exists</b>"),
     k.cellp("The local department inspects, on its own adopted code — which "
             "may be newer than the state's — and its own schedule. Ask for "
             "the list; write it on the log at the end"),
     k.cellp("<b>Inspected.</b> By the local certified inspector if the city "
             "or county runs its own electrical program, otherwise by the "
             "State Electrical Division — the two do not always line up")],
    [k.cellp("<b>No building program</b>"),
     k.cellp("<b>Nobody.</b> No building permit, no footing or framing "
             "inspection, no certificate of occupancy — and no state agency "
             "may step in. The 2018 IRC and UPC bind the house anyway"),
     k.cellp("<b>Inspected. Still required.</b> The State Electrical "
             "Division, at temporary service, rough-in and final, and the "
             "power company holds the meter until you certify the request "
             "was filed")],
]
flow.append(k.ref_table(
    "Two situations, one electrical answer",
    [k.cellp("Where you are", bold=True),
     k.cellp("Who does the BUILDING inspections", bold=True),
     k.cellp("Who does the ELECTRICAL inspections", bold=True)],
    rows, [1.35 * inch, (CW - 1.35 * inch) * 0.5, (CW - 1.35 * inch) * 0.5]))
flow.append(k.cite(
    f"The building side rests on the Building Construction Act, "
    f"{sec('71-6406(7)')} (\"may adopt … inspections\"). The electrical side "
    f"rests on a different act entirely — the State Electrical Act, "
    f"{sec('81-2124(3)')} (every new single-family service is inspected) and "
    f"{sec('81-2125(1)')} (state inspection yields only to a county, city or "
    f"village that inspects with its own certified inspector by ordinance). "
    f"The two lists of jurisdictions are not the same, which is why NE.4 "
    f"sends you to the Division's map rather than to the county."))

# ------------------------------------------------- electrical track
flow += k.h2_tight("THE ELECTRICAL TRACK — THE ONE SEQUENCE THE STATUTE "
                   "FIXES", reserve=2.4)
flow.append(k.body(
    "This is unusual: a genuine statutory response time, a concealment rule "
    "with a cost attached, and a correction-order window with dates. The "
    "Division's homeowner handout adds the practical shape — temporary "
    "service, new service, rough-in, final, re-inspection — and the two agree."))
flow.append(k.callout_long(
    f"Neb. Rev. Stat. {sec('81-2134')} — state inspection procedures, "
    f"verbatim", [
        Paragraph("\"(1)(a) At or before commencement of any electrical "
                  "installation which is required by law to be inspected, "
                  "the person responsible for the installation shall forward "
                  "a request for inspection to the board completed in the "
                  "manner prescribed by the board …", S["body"]),
        Paragraph("(2) Where wiring is to be concealed, <b>the inspector must "
                  "be notified within reasonable time to complete a rough-in "
                  "inspection prior to concealment</b>, exclusive of "
                  "Saturdays, Sundays, and holidays. If wiring is concealed "
                  "before rough-in inspection without adequate notice having "
                  "been given to the inspector, <b>the person responsible for "
                  "having enclosed the wiring shall be responsible for all "
                  "costs resulting from uncovering and replacing the cover "
                  "material</b>.", S["body"]),
        Paragraph("(3) <b>Inspections shall be made within one week of the "
                  "appropriate request.</b> When necessary, circuits may be "
                  "energized by the authorized installer prior to inspection "
                  "but the installation shall remain subject to condemnation "
                  "and disconnection.\"", S["body"]),
    ]))
rows = [
    [k.cellp("<b>1</b>", center=True), k.cellp("<b>File the request</b>"),
     k.cellp("\"At or before commencement,\" with the fees, and — as a "
             "homeowner — the signed verification. Online since April 13, "
             "2026; homeowner permits are linked by Division staff after you "
             "register. You receive a permit number and the inspector's "
             "details on the \"yellow wiring permit card\""),
     k.cellp(f"{sec('81-2126')}; {sec('81-2134(1)')}")],
    [k.cellp("<b>2</b>", center=True), k.cellp("<b>Temporary service</b>"),
     k.cellp("A separate application, \"a minimum of five working days prior "
             "to the date energization is required\"; the inspector \"may "
             "verbally authorize energization.\" The handout: temporary "
             "services \"WILL NOT be energized by the power company until "
             "they receive authorization to do so from the State Electrical "
             "Inspector\""),
     k.cellp("Board Rule 12; handout")],
    [k.cellp("<b>3</b>", center=True), k.cellp("<b>New service</b>"),
     k.cellp("The meter base, service entrance and panel. \"When a permit is "
             "issued for the new service, the State Electrical Division "
             "office will forward a copy to the power supplier\" — which is "
             "why the form asks for the supplier's name and address"),
     k.cellp("Handout; " + sec("81-2129"))],
    [k.cellp("<b>4</b>", center=True), k.cellp("<b>Rough-in</b>"),
     k.cellp("\"Must be approved by the inspector before fiberglass "
             "insulation or drywall is installed.\" Notify \"within "
             "reasonable time\"; inspection within one week of the request; "
             "cover it first and you pay to uncover it"),
     k.cellp(f"{sec('81-2134(2)')}–(3); handout")],
    [k.cellp("<b>5</b>", center=True), k.cellp("<b>Final</b>"),
     k.cellp("After devices, fixtures and equipment are in. On approval the "
             "utility's liability for the installation \"shall be "
             "terminated\" — the reason the power company wants this done. "
             "Buy the $6 written approval notice; it is your record"),
     k.cellp(sec("81-2133"))],
    [k.cellp("<b>6</b>", center=True), k.cellp("<b>Correction, if any</b>"),
     k.cellp("For a defect that is not immediately dangerous the inspector "
             "issues a correction order \"noting specifically what changes "
             "are required\" and setting a final-inspection date \"not less "
             "than ten nor more than seventeen calendar days from the date "
             "of the order.\" Uncorrected, \"a condemnation or disconnection "
             "order may be issued.\" The handout allows \"approximately "
             "fourteen working days to make the corrections\""),
     k.cellp(f"{sec('81-2138')}; handout")],
    [k.cellp("<b>7</b>", center=True), k.cellp("<b>The meter</b>"),
     k.cellp("No connection \"until there is filed with the electrical "
             "utility supplying power a certificate of the property owner … "
             "that inspection has been requested and that the conditions of "
             "the installation are safe for energization.\" The supplier "
             "\"may refuse service without liability\" until it is"),
     k.cellp(sec("81-2129"))],
]
flow.append(k.ref_table(
    "The electrical sequence, in the order it happens",
    [k.cellp("", bold=True, center=True), k.cellp("Step", bold=True),
     k.cellp("What the statute and the Division say", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [0.35 * inch, 1.15 * inch, CW - 1.5 * inch - CITE, CITE]))
flow.append(k.cite(
    "Handout quotations are from the State Electrical Division's Homeowner "
    "Handout, updated May 22, 2024, at electrical.nebraska.gov/"
    "homeowner-handout. Requests for an inspection go to the inspector named "
    "on your permit card, who has a 24-hour voicemail line: \"State your name, "
    "your telephone number, your permit number, and whether you\" need a "
    "rough-in or a final. A dangerous defect skips the correction order: an "
    f"unenergized installation is condemned ({sec('81-2136')}), an energized "
    f"one disconnected ({sec('81-2137')}). Appeal is to the board, through a "
    f"hearing officer ({sec('81-2141')}–2142)."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Three clocks on the permit itself, and the felony behind the first", [
        Paragraph(f"<b>Before you start.</b> The request is due \"at or before "
                  f"commencement\" ({sec('81-2126')}). If the board becomes "
                  f"aware you did not file, it sends a certified letter giving "
                  f"<b>fourteen days</b>; a late request carries a <b>$250</b> "
                  f"delinquent fee; and failure to file within the fourteen "
                  f"days goes to the county attorney under {sec('81-2143')} — "
                  f"which, since <b>July 18, 2026</b>, makes \"fail[ing] to "
                  f"file a request for inspection when required\" a <b>Class "
                  f"IV felony</b> ({sec('81-2143(1)(c)')}, as amended by "
                  f"LB889).", S["body"]),
        Paragraph("<b>Five months.</b> Under Board Rule 13 the permit is void "
                  "if the work \"has not been started within five (5) months "
                  "after the date of\" issuance, or if no progress is made for "
                  "five consecutive months, after fourteen days' written "
                  "notice. An extension takes \"clear and convincing proof of "
                  "a practical hardship.\" If your build stalls — financing, "
                  "weather — write to the Division before the fifth month, "
                  "not after.", S["body"]),
        Paragraph(f"<b>Two knocks.</b> Rule 13 also prescribes what happens "
                  f"when an inspector cannot reach \"a property owner "
                  f"installing wiring pursuant to Sections 81-2121(5) and "
                  f"81-2124\": a doorknob notice card, a second attempt and a "
                  f"second card, and then the application \"stays on file, "
                  f"subject to inspection.\" An unanswered card does not close "
                  f"the file; it leaves the house uninspected with a "
                  f"certificate on record at the utility that says otherwise "
                  f"— see {sec('81-2143(1)(a)')} on false statements.",
                  S["body"]),
    ]))

# ------------------------------------------------- registrations
flow += k.h2_tight("THE TWO REGISTRATIONS THAT ARE ALSO YOUR INSPECTIONS",
                   reserve=2.2)
flow.append(k.body(
    "Nobody from the state comes to look at a septic system or a well on a "
    "private house. What the state requires instead is a <b>professional's "
    "signature on a registration</b> — and on a parcel with no building "
    "department, those two documents plus the electrical approval are the "
    "whole of your third-party record."))
rows = [
    [k.cellp("<b>Septic</b>"),
     k.cellp("The certified professional, engineer or environmental health "
             "specialist who built or supervised the system registers it "
             "with DWEE \"within forty-five days of completion,\" on DWEE's "
             "form, with the fee — and submits the signed certification, the "
             "scaled drawing and the perc data that make the general permit "
             "cover you"),
     k.cellp("\"[W]ill provide a copy of the system registration form to the "
             "system owner.\" <b>Ask for it at completion</b>, file it with "
             "the drawing, and note the reserve area on your site plan so "
             "nobody builds on it"),
     k.cellp(f"{sec('81-15,248(2)')}; Title 124 ch. 10 §{NB}004; GTS220000 "
             f"§{NB}II.A")],
    [k.cellp("<b>Well</b>"),
     k.cellp("Registered with DWEE \"within sixty days after completion,\" "
             "with the well-log information, by the licensed driller — or by "
             "you if you drilled it. $200 plus $25–$40"),
     k.cellp("Keep the well log: \"Any owner of a water well … shall keep "
             "and maintain an accurate well log.\" If a driller did it, get "
             "the registration number and the log before the final payment"),
     k.cellp(f"{sec('46-602(1)')}; {sec('46-1241')}; {sec('46-606(1)')}")],
    [k.cellp("<b>Radon</b>"),
     k.cellp("Required by statute; <b>no registration, no inspection, no "
             "form</b> outside a local program. Nothing in the Act names an "
             "inspector"),
     k.cellp("Photograph the vent pipe in the subslab material before the "
             "pour, the roof termination, the labels and the attic box. "
             "That is the only evidence the house will ever have"),
     k.cellp(f"{sec('76-3504')}")],
    [k.cellp("<b>Energy</b>"),
     k.cellp("Required by statute; no permit, no certificate, no inspection "
             "on request. DWEE or a local code authority may inspect \"only "
             "after permission has been granted by the owner or occupant or "
             "after a warrant has been issued\""),
     k.cellp("Keep the REScheck report or component table, the insulation "
             "certificates, and the blower-door and duct-test results. The "
             "two-year correction window runs from first occupancy"),
     k.cellp(f"{sec('81-1617')}; {sec('81-1622')}; {sec('81-1625')}")],
]
flow.append(k.ref_table(
    "Four obligations, one inspector — you",
    [k.cellp("", bold=True), k.cellp("Who files, and when", bold=True),
     k.cellp("What you keep", bold=True), k.cellp("Cite", bold=True)],
    rows, [0.8 * inch, (CW - 0.8 * inch - CITE) * 0.52,
           (CW - 0.8 * inch - CITE) * 0.48, CITE]))

# ------------------------------------------------- local program
flow += k.h2_tight("WHERE A LOCAL PROGRAM EXISTS", reserve=2.2)
flow.append(k.body(
    "No Nebraska statute lists the inspections a house gets. Where a city or "
    "county runs a program, the list is in its own administrative amendments "
    f"adopted under {sec('71-6406(7)')} — \"organization of enforcement … "
    f"examination of plans, inspections, appeals, permits, and fees\" — and "
    f"it varies. <b>The list below is typical of such programs and is not "
    f"attributed to the state.</b> Ask yours, and write its list on the log."))
rows = [
    [k.cellp("<b>Footing</b> — forms and reinforcing in place, before "
             "concrete"),
     k.cellp("Often combined with a foundation-wall or slab inspection; a "
             "monolithic pour is usually inspected once")],
    [k.cellp("<b>Underground plumbing and radon rough</b> — before the "
             "slab"),
     k.cellp("Where the program inspects plumbing at all; the UPC applies "
             "regardless, but nobody is obliged to inspect it")],
    [k.cellp("<b>Framing</b> with <b>rough plumbing, mechanical and "
             "electrical</b>"),
     k.cellp("The state electrical rough-in may be a separate visit by a "
             "different inspector; do not assume one covers the other")],
    [k.cellp("<b>Insulation</b>"),
     k.cellp("Where a local energy code exists; batts in before the visit, "
             "blown or sprayed insulation inspected before it goes in — ask "
             "which")],
    [k.cellp("<b>Final</b> and, where issued, a <b>certificate of "
             "occupancy</b>"),
     k.cellp("No state rule requires a CO for a house. Ask whether the local "
             "program issues one, because a lender may ask for it")],
]
flow.append(k.ref_table(
    "A typical local sequence — confirm yours",
    [k.cellp("Inspection", bold=True), k.cellp("Note", bold=True)],
    rows, [2.4 * inch, CW - 2.4 * inch]))
flow.append(k.cite(
    "<b>Lincoln, verified from its own pages</b> (September 2026): homeowner "
    "plumbing, mechanical and electrical permits \"may only be issued to a "
    "licensed contractor or a homeowner for their primary residence\"; \"The "
    "permit issued must be inspected before any work is concealed and must "
    "also be inspected when the installation of the work is completed\"; "
    f"\"Permits are valid for 120 days from issuances.\" <b>Virtual "
    f"inspections</b> are now lawful for a one- or two-family house under "
    f"{sec('71-6409')} (effective July 18, 2026), conducted live with the "
    f"permit holder and conditioned on naming a licensed or registered "
    f"contractor \"who is completing the work\" — and \"Authorized inspector "
    f"does not include an individual performing a self-performed inspection "
    f"for the individual's own permit or building.\" Ask whether your program "
    f"offers it and whether it will extend it to owner-performed work."))

# ------------------------------------------------- nobody inspects
flow += k.h2_tight("WHEN NOBODY IS REQUIRED TO INSPECT YOU", reserve=2.2)
flow.append(k.body(
    "On a parcel with no building program there is no building permit, no "
    "required building inspection and no certificate of occupancy — and, "
    "unlike some states, <b>no state office you can ask to inspect "
    "voluntarily</b>: the Act gives no agency that power over a private "
    "house. What you have instead is the code, which binds you, and a record "
    "you build yourself."))
flow.append(k.callout_long(
    "The record you are building, and who will read it", [
        Paragraph(f"<b>The buyer's lender, the appraiser and the insurer</b> "
                  f"will ask what the house was inspected to. Your answer is "
                  f"the electrical approval notice, the septic registration "
                  f"with its scaled drawing, the well registration and log, "
                  f"and the energy documentation — plus dated photographs at "
                  f"every stage that gets covered: footing steel, the radon "
                  f"pipe in the subslab material, underground plumbing, "
                  f"framing and rough-ins, insulation. Keep them together, "
                  f"and keep the emails in which the county told you no "
                  f"permit was required.", S["body"]),
        Paragraph(f"<b>The state, for two years.</b> If DWEE or a local code "
                  f"authority \"finds, within two years from the date a "
                  f"building is first occupied, that the building, at the "
                  f"time of construction, did not comply with the Nebraska "
                  f"Energy Code,\" it \"may order the owner or prime "
                  f"contractor to take those actions necessary to bring the "
                  f"building into compliance\" ({sec('81-1625')}). And \"a "
                  f"building owner may submit a written request that the "
                  f"department undertake a determination\" ({sec('81-1616')}) "
                  f"— a path a later buyer holds. Your blower-door result is "
                  f"the document that answers it.", S["body"]),
        Paragraph("<b>The seller-disclosure statement</b> you will sign when "
                  "you sell an occupied house is \"to the best of the seller's "
                  "belief and knowledge\" — and the person who built the "
                  "house knows more than most sellers. The inspection log "
                  "below is what you will be disclosing from.", S["body"]),
    ]))
flow.append(k.body(
    "<b>And the electrical inspections happen anyway.</b> Whatever your "
    "county decided about building codes, a State Electrical Division "
    "inspector — or the city's — will come out at temporary service, "
    "rough-in and final. That is not optional, the power company enforces "
    "it, and it is the one visit every Nebraska house gets."))

# ------------------------------------------------- log
flow += k.h2_tight("INSPECTION LOG — RECORD EVERY ONE", reserve=1.6)
flow += k.check_table(
    "Every visit and every filing, whoever required it",
    [
        ("<b>Electrical request for inspection</b> filed — before any wiring "
         "began — with the homeowner verification.",
         [("Date", 0.34), ("Permit number", 0.33), ("Inspector", 0.33)]),
        ("<b>Temporary service</b> — application five working days ahead; "
         "inspector's authorization to energize.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Footing / foundation</b> — local program, if any; otherwise my "
         "own dated photographs of the steel before the pour.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Radon rough</b> — vent pipe in the subslab material, sump lids, "
         "before the slab. Photographed.",
         [("Date", 0.34), ("By", 0.33), ("Result", 0.33)]),
        ("<b>Underground plumbing</b> — to the 2018 UPC (or the city's "
         "code). Local program or photographs.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Electrical rough-in</b> — state or local inspector, before "
         "insulation or drywall. Requested within reasonable time; due "
         "within one week.",
         [("Requested", 0.34), ("Inspected", 0.33), ("Result", 0.33)]),
        ("<b>Framing, rough plumbing, rough mechanical</b> — local program, "
         "if any; otherwise photographs.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Insulation</b> — local energy code, if any; the certificates "
         "and R-values kept either way.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Blower door and duct test</b> — under 3 ACH50; ducts ≤ 4 CFM "
         "per 100 sq ft unless all inside the envelope.",
         [("Date", 0.34), ("Tester", 0.33), ("Result", 0.33)]),
        ("<b>Electrical final</b> — approval notice ($6) requested and "
         "received; correction order, if any, closed within its 10–17 days.",
         [("Date", 0.34), ("Inspector", 0.33), ("Result", 0.33)]),
        ("<b>Certificate to the power supplier</b> filed; meter set.",
         [("Filed", 0.5), ("Meter set", 0.5)]),
        ("<b>Septic system registered</b> by the professional within 45 "
         "days; my copy received.",
         [("Registration", 0.5), ("Copy received", 0.5)]),
        ("<b>Well registered</b> within 60 days; well log in hand.",
         [("Registration", 0.5), ("Log received", 0.5)]),
        ("<b>Final building inspection / certificate of occupancy</b>, where "
         "a local program issues one.",
         [("Date", 0.5), ("Number", 0.5)]),
        ("Any inspection my local program requires that is not on this list "
         "— ask them, and write it here:",
         [("Inspection", 0.5), ("Date", 0.5)]),
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ne-permit-kit",
                       "NE.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
