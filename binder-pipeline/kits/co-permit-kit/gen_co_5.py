#!/usr/bin/env python3
"""CO.5 Forms & Documents Index — Colorado.

Colorado scatters its paperwork across two state boards, a state engineer, a
local public health agency, and whichever local government (if any) permits
buildings on your parcel. This index names the documents that actually exist,
says which office issues each, and — as usefully — names the ones people go
looking for that do not exist at all.

Sources verified August 2026:
  dpo.colorado.gov/ElectricalPlumbingPermits/Forms  the Division's published
                              form set, listed separately for contractors and
                              for HOMEOWNERS: Electrical Permit Application,
                              Solar Permit Application, Homeowner's Guide for
                              Electrical Installations, Requirements for Well
                              Wiring, Electrical Mobile and Modular Home
                              Guidelines, Submittal Guidelines for
                              Solar/Alternate Power Sources, Electrical
                              Inspection Map, Electrical Inspector Contact
                              List, Plumbing Permit Application, GAS PIPING
                              PERMIT APPLICATION (separate), Homeowner's Guide
                              for Plumbing and Gas Piping Installations,
                              Plumbing Mobile and Modular Home Guidelines,
                              Plumbing Inspection Map, Plumbing Inspector
                              Contact List, Remote Video Inspection Waiver
                              (Occupied Residential), variance request forms
  dwr.colorado.gov            Applications eForms Dashboard; Beginner's Guide
                              to Well Permits; Form Submittal, Payment Options
                              and Fee Schedule; Emergency Well Permit
                              Procedures; Fact Sheet for Home Buyers and Real
                              Estate Professionals; Well Permit Search; Well
                              Permit Map Viewer
  denvergov.org / pprbd.org   the two verified local owner-builder regimes
                              (see CO.1). NOTE: the Pueblo Regional Building
                              Department was succeeded on January 1, 2026 and
                              is no longer cited as a live office in this kit
  C.R.S. 25-10-106(1)(a)      the OWTS permit application is defined by local
                              board of health rule — there is no state form
  2021 IECC R401.3 as locally adopted — the permanent energy certificate

Still deliberately hedged: every local packet is its own; the Pueblo forms are
printed as one verified example, never as a statewide set; and no form numbers
are invented — where Colorado gives a document a name but no number, the kit
prints the name.
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

FORM_ID = "CO.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document a Colorado owner-builder is likely to meet — what each "
    "one is, when you need it, and which office it comes from.")

flow.append(k.disclaimer(
    "Colorado names most of its permit documents rather than numbering them, "
    "so this index prints names as published. Your local building department "
    "and public health agency each publish packets of their own."))
flow.append(Spacer(1, 8))

DOCS = [
    ("Electrical Permit Application",
     "The state electrical permit, bought before any wiring starts "
     "(C.R.S. 12-115-120(2)(b)). The Division publishes a <b>homeowner</b> "
     "form set alongside the contractor one, and a homeowner is a qualified "
     "applicant by statute. Buying online is \"<i>processed immediately upon "
     "payment</i>\"; a hard copy \"<i>may be delayed up to 7 business "
     "days</i>.\" <b>When:</b> before the first wire.",
     "DPO — dpo.colorado.gov &#8594;<br/>Electrical &amp; Plumbing Permits"),
    ("Plumbing Permit Application",
     "The state plumbing permit, bought before any plumbing starts "
     "(12-155-120(1)(c)(I)). For a residential job the application asks for a "
     "<b>fixture count</b> — traps, water hammer arrestors, backflow "
     "preventers, water heaters, fuel gas outlets and regulators — so count "
     "them off your plans first.",
     "DPO — same page"),
    ("Gas Piping Permit Application",
     "<b>Separate from the plumbing permit.</b> Fuel gas piping is "
     "plumbing-board work under its own adopted code, and on a propane build "
     "it is easy to forget until an inspector asks. <b>When:</b> before any "
     "gas piping is installed.",
     "DPO — same page"),
    ("Homeowner's Guide for Electrical Installations · Homeowner's Guide for "
     "Plumbing and Gas Piping Installations",
     "Two plain-language guides the Division publishes for homeowners doing "
     "their own work — the closest thing Colorado has to an official "
     "owner-builder handbook for the trades, and free. The same page carries "
     "a <b>Requirements for Well Wiring</b> handout, which almost every rural "
     "owner-builder needs and almost no general guide covers.",
     "DPO — Permit and Inspections Forms"),
    ("Electrical / Plumbing Inspection Map and Inspector Contact List",
     "How you find the human being who will inspect your house — the "
     "Division will not schedule for you. There is also a <b>Remote Video "
     "Inspection Waiver</b> for occupied residential work, worth asking "
     "about on a parcel where an inspector's drive time runs to hours. "
     "<b>When:</b> the day you buy the permit.",
     "DPO — Permit and Inspections Forms"),
    ("Certificate of approval (electrical; plumbing; gas)",
     "Not filed — received and kept. The inspector issues it when work passes "
     "(12-115-120(3)(a); 12-155-120(2)(a)). On the electrical side it is also "
     "your evidence that the work <i>was inspected</i> — the condition your "
     "homeowner exemption depends on (12-115-116(2)).",
     "Issued by your inspector"),
    ("Residential well permit application",
     "Filed with DWR through its Applications eForms Dashboard; DWR takes "
     "applications by email and fees online. <b>When:</b> first — "
     "\"<i>review of complete applications may take up to 49 days</i>,\" "
     "before a driller is scheduled. Read the <b>Beginner's Guide to Well "
     "Permits</b> first.",
     "DWR — dwr.colorado.gov,<br/>Well Permitting"),
    ("Well construction report · pump installation report",
     "Filed with DWR by your driller and pump installer, not by you — but "
     "they belong in your file, and a lender or buyer will ask. DWR's "
     "<b>Well Permit Search</b> and <b>Map Viewer</b> let you read what "
     "neighboring permits allow before you buy land.",
     "Filed by the driller; at DWR"),
    ("OWTS (septic) permit application",
     "There is no state form. Local board of health rules must provide the "
     "\"<i>procedures by which a person may apply</i>\" and set what the "
     "application must contain (C.R.S. 25-10-106(1)(a)), so the packet is "
     "your county's or health district's own. <b>When:</b> after the site "
     "evaluation and soil work, before the system is built — and the system "
     "may not be used until a final inspection passes (25-10-106(1)(h)).",
     "Your local public health agency"),
    ("Local building permit application and submittal checklist",
     "Only where your jurisdiction has adopted a building code; the local "
     "list governs. Colorado checklists typically ask for house plans, a "
     "soils report, a foundation plan, a site plan, an energy calculation, "
     "and Manual J and D load calculations — with the soils report and "
     "foundation plans carrying an original Colorado engineer's or "
     "architect's stamp.",
     "Your building department"),
    ("Local homeowner / owner-builder permit application",
     "Where one exists it is a local creation with local conditions — there "
     "is no state version. Denver requires a photo ID matching the deed, an "
     "exam for the trades, and occupancy \"<i>for at least one year after "
     "work is complete</i>\"; Pikes Peak Regional issues to an owner only for "
     "\"<i>your primary residence, which you own and reside in</i>.\" Ask "
     "what your department's version commits you to before you sign (CO.1).",
     "Your building department"),
    ("Project approval / routing sheet",
     "A Colorado pattern worth expecting: one sheet every interested agency "
     "must sign before the permit or the CO issues — and departments "
     "commonly require it completed even by an agency that says the job is "
     "outside its jurisdiction. Ask early who is on yours: fire district, "
     "health, roads, floodplain.",
     "Your building department"),
    ("Permanent energy certificate",
     "Not filed — <b>posted</b>. Under the 2021 IECC as adopted by Colorado "
     "jurisdictions, the builder completes a permanent certificate of "
     "insulation R-values, window U-factors, and equipment efficiencies and "
     "posts it near the furnace, in a utility room, or another approved "
     "interior location. As owner-builder, you are the builder.",
     "You complete it; 2021 IECC R401.3"),
]

rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in DOCS]
flow.append(k.ref_table(
    "Documents a Colorado owner-builder will actually encounter",
    [k.cellp("Document", bold=True),
     k.cellp("What it is and when you need it", bold=True),
     k.cellp("Where it comes from", bold=True)],
    rows, [1.8 * inch, CW - 1.8 * inch - 1.9 * inch, 1.9 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout("Forms that do not exist — stop looking for them", [
    Paragraph("There is <b>no state building permit application</b>, because "
              "Colorado issues no state building permit. There is <b>no state "
              "owner-builder affidavit or exemption form</b> — the homeowner "
              "exemptions in C.R.S. 12-115-116(2) and 12-155-118(2) are "
              "self-executing in the statute, and the only \"owner-builder "
              "form\" you may meet is one your local building department "
              "invented. There is <b>no statewide submittal checklist</b> and "
              "<b>no statewide certificate of occupancy</b>. And in a county "
              "that has adopted no building code there is no building "
              "inspection record at all — which is exactly why the documents "
              "in this index matter. When a lender, insurer, or buyer asks "
              "for \"the permit\" on such a build, what you hand them is this "
              "stack: the certificates of approval, the OWTS acceptance, the "
              "well permit and construction report, and the utility's final "
              "release.", S["body"]),
]))

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026): the Division's published form "
    "set, listed separately for contractors and homeowners — "
    "dpo.colorado.gov/ElectricalPlumbingPermits/Forms. Permit-before-work and "
    "certificate-of-approval duties — C.R.S. 12-115-120(2)(b), (3)(a); "
    "12-155-120(1)(c)(I), (2)(a); the inspection condition on the electrical "
    "exemption — 12-115-116(2). Well forms, the Beginner's Guide, the fee "
    "schedule, the 49-day review, and the permit search — dwr.colorado.gov. "
    "OWTS application content set by local rule and the final inspection "
    "before use — 25-10-106(1)(a), (1)(h). Local owner-builder terms — "
    "denvergov.org and pprbd.org, read August 2026. Energy certificate — "
    "2021 IECC R401.3 as adopted."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "co-permit-kit",
                       "CO.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
