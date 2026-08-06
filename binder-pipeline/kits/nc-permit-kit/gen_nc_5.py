#!/usr/bin/env python3
"""NC.5 Forms & Documents Index.

Sources verified August 2026:
  G.S. 87-14(a)(1),(a)(2)  owner exemption affidavit; workers' comp proof
  G.S. 44A-11.1(a),(b)     lien agent threshold, timing, DOI registry
  G.S. 44A-11.2(d),(e)     posting the permit / lien agent sign on the property
  G.S. 160D-1110(a),(g)    trade permits; lien agent details on the permit
  G.S. 113A-57(4)          erosion plan over one acre, filed 30 days ahead
  G.S. 160D-1116(a),(b)    certificate of compliance; temporary CO
  15A NCAC 18E             septic IP / CA / Operation Permit via local health
  liensnc.com              LiensNC appointment fee, $30 for a 1-2 family
                           dwelling (LiensNC's published fee, not statutory)
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

FORM_ID = "NC.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document a North Carolina owner-builder meets — what each one is, "
    "when it is needed, and which office it comes from.")

flow.append(k.disclaimer(
    "Form names and numbers are local; the obligations behind them are not."))
flow.append(Spacer(1, 8))

DOCS = [
    ("Building permit application",
     "The main application. Triggers the $40,000 tests for licensure, "
     "workers' comp, and lien agent. <b>When:</b> after zoning, septic and "
     "erosion control are lined up.",
     "City, town, or county inspections department"),
    ("Owner exemption affidavit",
     "A <i>verified</i> — i.e. sworn and notarized — affidavit that you own "
     "the land, will personally superintend the work, and will attend every "
     "inspection. <b>When:</b> at application. The department forwards a copy "
     "to the Licensing Board, which verifies your claim.",
     "Inspections department form; notary required"),
    ("Workers' compensation proof or affirmation",
     "Proof of coverage \"as required by Chapter 97,\" which reaches "
     "employers of three or more. With no employees you affirm that instead. "
     "<b>When:</b> at application.",
     "Inspections department form — wording varies by county"),
    ("Appointment of lien agent",
     "Required at $40,000 or more, <b>before you first contract with anyone "
     "to improve the property</b>. You choose from the registry of lien "
     "agents kept by the Department of Insurance. New construction is not "
     "exempt — the exemption covers improvements to an <i>existing</i> "
     "owner-occupied dwelling.",
     "Commonly filed at <b>liensnc.com</b>; $30 published appointment fee "
     "for a 1–2 family dwelling"),
    ("Permit posting / lien agent sign",
     "The building permit must be conspicuously and continuously posted on "
     "the property until construction is complete. If the permit does not "
     "carry the lien agent's contact information, a sign disclosing it must "
     "be posted instead.",
     "You post it — nobody reminds you"),
    ("Erosion and sedimentation control plan",
     "Required when land disturbance exceeds <b>one acre</b>. Must be filed "
     "at least 30 days before disturbance begins and <b>approved before the "
     "building permit may issue</b>.",
     "NC DEQ land resources program, or a delegated local program — ask "
     "which applies in your county"),
    ("Septic — three approvals in sequence",
     "<b>Improvement Permit (IP)</b> follows the soil and site evaluation "
     "and establishes that the site will support a system, and what kind. "
     "<b>Construction Authorization (CA)</b> lets it be built. <b>Operation "
     "Permit</b> is issued after installation and inspection, and is what "
     "lets the system be used. <b>Your building permit cannot issue until "
     "the CA has</b> — statewide, not a local quirk. <b>When:</b> start the "
     "IP as early as possible — before you buy the land if you still can.",
     "County (local) health department, under 15A NCAC 18E"),
    ("Well construction permit + Certificate of Completion",
     "The permit is required <b>before</b> a private drinking water well is "
     "constructed, and is valid five years. After construction the health "
     "department inspects and issues a <b>Certificate of Completion</b> — "
     "the well may not be placed in service without it. The department then "
     "samples the water within 30 days; you do not arrange that yourself.",
     "County health department, under 15A NCAC 02C .0300"),
    ("Driveway / access permit",
     "<b>Normally not required for a single residence.</b> NCDOT's rule "
     "excludes residential driveway connections unless there is a safety "
     "hazard, a highway project, or excessive/obvious drainage complications. "
     "Contact the District Engineer anyway — they flag design issues and "
     "arrange your driveway pipe.",
     "NCDOT District Engineer if the road is state-maintained; otherwise the "
     "city or county"),
    ("Trade permits — electrical, plumbing, mechanical",
     "Separate permits are required for plumbing systems, heating and "
     "cooling equipment, and electrical wiring, in addition to the building "
     "permit. Doing the work yourself under the owner exemption does not "
     "waive them.",
     "Inspections department — some counties bundle these into one permit"),
    ("Certificate of compliance",
     "Issued after the final inspection when the completed work complies. "
     "This is the statutory name for what everyone calls the certificate of "
     "occupancy. Occupying before it issues is a Class 1 misdemeanor.",
     "Inspections department, at the end"),
    ("Temporary certificate of occupancy",
     "May be issued for a stated period, for all or part of the building, if "
     "the inspector finds it may safely be occupied before final completion.",
     "Inspections department, on request"),
]

rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in DOCS]
flow.append(k.ref_table(
    "Documents a North Carolina owner-builder will encounter",
    [k.cellp("Document", bold=True),
     k.cellp("What it is and when you need it", bold=True),
     k.cellp("Where it comes from", bold=True)],
    rows, [1.45 * inch, CW - 1.45 * inch - 1.75 * inch, 1.75 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026, General Statutes at ncleg.gov): "
    "affidavit and workers' comp proof — § 87-14(a)(1), (a)(2), with Chapter "
    "97 reaching employers of three or more, § 97-2(1). Lien agent at "
    "$40,000+, designated before first contracting, chosen from the "
    "Department of Insurance registry — § 44A-11.1(a), (b); details on the "
    "permit — § 160D-1110(g); permit posted continuously, or a lien agent "
    "sign — § 44A-11.2(d), (e). Separate plumbing, mechanical and electrical "
    "permits — § 160D-1110(a). Erosion plan over one acre filed 30 days "
    "ahead — § 113A-57(4). Certificate of compliance, temporary CO, and the "
    "occupancy penalty — § 160D-1116. Septic IP / CA / OP and the "
    "building-permit gate — 15A NCAC 18E, § .0204(f). Well permit, "
    "Certificate of Completion, and the health department's 30-day sampling "
    "duty — 15A NCAC 02C .0304, .0306(c) and 15A NCAC 18A .3802(a). "
    "Residential driveway exclusion — 19A NCAC 02B § .0601(a). The $30 "
    "appointment fee is LiensNC's published fee for a 1–2 family dwelling, "
    "not a statutory one — confirm it at liensnc.com before you budget it."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "nc-permit-kit",
                       "NC.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
