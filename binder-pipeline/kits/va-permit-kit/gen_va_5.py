#!/usr/bin/env python3
"""VA.5 Forms & Documents Index.

Sources verified August 2026:
  USBC § 108.1 (13VAC5-63-80)  the owner may file the permit application
  § 54.1-1111              the exemption statement + affidavit, a local form
  § 36-98.01; § 43-1; § 43-4.01  lien agent line on the permit application;
                           who may serve; the 30-day notice effect
  VDH uniform application  "Commonwealth of Virginia Application for:
                           Sewage System / Water Supply" — verified by
                           title; no stable form number is printed on it
  § 32.1-163.5             OSE/PE private designs; 15 working days or
                           deemed approved
  12VAC5-610-240/-300(A)/-340  septic construction permit (18-month life);
                           operation permit after final inspection
  12VAC5-630-220(B)/-330   well construction permit; inspection statement
  § 62.1-44.15:24; 9VAC25-875-530(B)  agreement in lieu of a plan — each
                           locality maintains its own form
  VDOT land use permits    verified form titles: LUP-A (application),
                           LUP-PE "Private entrance installation"
                           (rev. 3-2024); surety LUP-SB / LUP-CSB / LUP-LC
  13VAC5-63-264            blower-door result; duct-test report signed and
                           provided to the code official
  USBC § 116.1/.1.1; § 54.1-1101(B)  CO, temporary CO, and the CO-before-
                           sale duty

Still deliberately hedged: local form titles everywhere they vary (the
permit application and the exemption affidavit have no statewide versions,
so the index teaches the search instead of naming a state form); the VDH
uniform application is cited by title, not number, because no stable form
number is printed on it; and no statewide agreement-in-lieu template
exists — buyers are directed to the locality's erosion/stormwater office.
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

FORM_ID = "VA.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document a Virginia owner-builder meets — what each one is, "
    "when it is needed, and which office it comes from.")

flow.append(k.disclaimer(
    "Form names and numbers are local wherever noted; the obligations "
    "behind them are not."))
flow.append(Spacer(1, 8))

DOCS = [
    ("Building permit application",
     "The main application. There is <b>no statewide form</b> — every "
     "locality issues its own USBC application, and the owner may file "
     "it personally (USBC § 108.1). <b>When:</b> after zoning, septic, "
     "and erosion control are lined up. Find it by searching "
     "\"<i>[your locality] building permit application</i>\" on the "
     "locality's .gov site.",
     "Your locality's building department or permit portal"),
    ("Owner exemption statement / affidavit",
     "The written statement, supported by an affidavit, that you are not "
     "subject to contractor licensure — the official may not issue the "
     "permit without it (§ 54.1-1111). A local form, often titled "
     "\"Contractor's License Exemption\" or \"Owner's Affidavit\"; names "
     "vary. <b>When:</b> at application. Expect to notarize.",
     "Building department form; notary usually required"),
    ("Mechanics' lien agent designation",
     "Not a separate state form — a <b>field on the permit "
     "application</b> (§ 36-98.01). At your request the permit carries "
     "the agent's name, address and phone; otherwise it must say "
     "\"None Designated.\" The agent must be a Virginia attorney, title "
     "insurance company, or deposit-taking financial institution "
     "(§ 43-1). Designating one forces lien claimants to 30-day notice "
     "(§ 43-4.01) — the notices are their problem, not yours. "
     "<b>When:</b> line up the agent before you file.",
     "Your closing attorney or title company agrees to serve; you name "
     "them on the application"),
    ("VDH sewage system / water supply application",
     "The VDH uniform application — \"Commonwealth of Virginia "
     "Application for: Sewage System / Water Supply\" — used for septic "
     "<b>and</b> private wells. Cited here by title: no stable form "
     "number is printed on it, and district offices bundle it into "
     "local packages. <b>When:</b> first — before you buy the lot if "
     "you still can.",
     "Local health department (VDH), in person or via the local "
     "package"),
    ("OSE / PE evaluation and design package",
     "The private-sector alternative: a site evaluation and system "
     "design by a licensed onsite soil evaluator, or a PE consulting "
     "one, which VDH <b>must accept</b> — and act on within <b>15 "
     "working days</b> for a single lot, or the design is deemed "
     "approved (§ 32.1-163.5). <b>When:</b> whenever the health "
     "department's own timeline threatens your critical path.",
     "A licensed OSE or PE you hire; submitted to the local health "
     "department"),
    ("Septic construction permit + operation permit",
     "The written permit that must exist before any septic construction "
     "(12VAC5-610-240). The construction permit is <b>null and void "
     "after 18 months</b> (12VAC5-610-300(A)); the operation permit "
     "follows installation and final inspection and is what lets the "
     "system be used (12VAC5-610-340).",
     "Local health department (VDH)"),
    ("Private well construction permit + inspection statement",
     "A written VDH construction permit is required <b>before</b> "
     "drilling, altering, or deepening a private well "
     "(12VAC5-630-220(B)); you or your agent apply at the local health "
     "department, and VDH issues an inspection statement on completion "
     "(12VAC5-630-330). Ask the health department about water sampling "
     "for the new well — this kit prints no sampling promise.",
     "Local health department (VDH)"),
    ("Agreement in lieu of a plan (erosion / stormwater)",
     "The single-family shortcut: a contract with the local VESMP "
     "authority that replaces the engineered erosion/stormwater plan "
     "for a detached house under one acre of disturbance "
     "(§ 62.1-44.15:24; 9VAC25-875-530(B)). <b>Each locality maintains "
     "its own form</b> — there is no statewide template. <b>When:</b> "
     "before any land-disturbing activity; the land-disturbance "
     "approval gates all sitework.",
     "The locality's erosion/stormwater (VESMP) office"),
    ("VDOT land use permit — LUP-A + LUP-PE",
     "The entrance permit for a driveway onto a state-maintained road: "
     "form <b>LUP-A</b> (\"Land use permit application\") with schedule "
     "<b>LUP-PE</b> (\"Private entrance installation,\" rev. 3-2024); "
     "surety, where required, rides on LUP-SB / LUP-CSB / LUP-LC. "
     "<b>When:</b> before constructing any entrance in the "
     "right-of-way (24VAC30-73-60(A)). Online filing is available.",
     "VDOT district office for your locality — vdot.virginia.gov → "
     "Land Use Permits"),
    ("Energy test reports — blower door and ducts",
     "The blower-door result (mandatory, 5 ACH50 in Zone 4, run by one "
     "of the seven permitted tester categories) and the duct-leakage "
     "report — \"<i>a written report of the results of the test shall "
     "be signed by the party conducting the test and provided to the "
     "code official</i>\" (13VAC5-63-264). <b>When:</b> at final — but "
     "book the testers months earlier. See VA.2, section E.",
     "Your hired tester; delivered to the building department"),
    ("Certificate of occupancy / temporary CO",
     "Required before occupancy (USBC § 116.1); a temporary CO may "
     "issue on request for a safely occupiable portion before all work "
     "completes (§ 116.1.1). If you sell, the CO must exist <b>before "
     "conveying to the buyer</b>, absent a written waiver — a Class 1 "
     "misdemeanor otherwise (§ 54.1-1101(B)).",
     "Building department, at the end"),
]

rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in DOCS]
flow.append(k.ref_table(
    "Documents a Virginia owner-builder will encounter",
    [k.cellp("Document", bold=True),
     k.cellp("What it is and when you need it", bold=True),
     k.cellp("Where it comes from", bold=True)],
    rows, [1.45 * inch, CW - 1.45 * inch - 1.75 * inch, 1.75 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026; Code of Virginia and VAC at "
    "law.lis.virginia.gov): owner may file the application — USBC "
    "§ 108.1. Exemption statement + affidavit — § 54.1-1111; the form is "
    "local, so ask for it by function. Lien agent line, eligible agents, "
    "and the 30-day notice effect — § 36-98.01; § 43-1; § 43-4.01. VDH "
    "uniform sewage/water application — verified by title; no stable "
    "form number exists, so this index prints none. OSE/PE acceptance "
    "and the 15-working-day deemed-approval clock — § 32.1-163.5. Septic "
    "construction permit, its 18-month life, and the operation permit — "
    "12VAC5-610-240, -300(A), -340. Well permit and inspection statement "
    "— 12VAC5-630-220(B), -330. Agreement in lieu of a plan — "
    "§ 62.1-44.15:24; 9VAC25-875-530(B); each locality's own form. VDOT "
    "form titles LUP-A, LUP-PE (rev. 3-2024) and the surety forms — "
    "vdot.virginia.gov, Land Use Permits. Energy test reports — "
    "13VAC5-63-264. CO, temporary CO, and the CO-before-sale duty — "
    "USBC § 116.1, § 116.1.1; § 54.1-1101(B)."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "va-permit-kit",
                       "VA.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
