#!/usr/bin/env python3
"""TX.5 Forms & Documents Index — Texas.

Sources verified August 2026:
  Ins. Code § 2210.2515(b),(c),(d)  WPI-1 pre-construction notice; the two
                              certificate routes; TDI issues WPI-8/WPI-8-E
                              (tdi.texas.gov/wind)
  TCEQ Form 0235              OSSF permit application where TCEQ is the
                              permitting authority; counties publish their
                              own packets (Comal County example)
  H&S Code § 388.004(a)(3),(b)  the ESL builder self-certification form for
                              unincorporated areas (esl.tamu.edu); 3-year
                              retention and the owner's copy
  43 TAC § 11.52; TxDOT Form 1058  driveway onto the state system
  mctx.org                    Montgomery County residential development
                              permit (structure and non-structure versions)
  houstonpermittingcenter.org form CE1284, Homeowner's Plumbing and
                              Irrigation System Permit Application
  fortworthtexas.gov          Homestead Permit Affidavit (mechanical and
                              plumbing versions)
  sa.gov / docsonline.sanantonio.gov  Residential Building Permit
                              Application; homeowner's-permit attestation
  tdlr.texas.gov/electricians/exemptions.htm  the electrical homeowner
                              exemption has NO form — it is self-executing
  Property Code § 53.254      the homestead lien "form" is a contract you
                              write: pre-work, both spouses, filed with the
                              county clerk

Still deliberately hedged: WPI-3 appears in older TDI materials — current
TDI pages surface WPI-1 and the WPI-8 series, so verify at
tdi.texas.gov/wind before treating WPI-3 as a live form; every county's
floodplain-permit name varies; and every city's owner-builder form differs
— the three printed are verified examples, not a statewide set.
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

FORM_ID = "TX.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every named form a Texas owner-builder is likely to meet — what each "
    "one is, when it is needed, and which office it comes from.")

flow.append(k.disclaimer(
    "Texas scatters its forms across state agencies, counties, and cities; "
    "the named forms below are verified, but your county's and city's "
    "packets are their own."))
flow.append(Spacer(1, 8))

DOCS = [
    ("TDI Form WPI-1 — Application for Certificate of Compliance",
     "The windstorm pre-construction notice: written notice of intent to "
     "construct, \"<i>before the person begins to construct</i>,\" for any "
     "structure seeking TWIA-eligible certification in the coastal "
     "catastrophe area. <b>When:</b> before ground breaks — late is the "
     "one thing this form cannot be.",
     "TDI, tdi.texas.gov/wind"),
    ("TDI WPI-8 / WPI-8-E — Certificate of Compliance",
     "The certificate at the end of the windstorm process — engineer "
     "route or TDI-appointed qualified-inspector route — and the document "
     "TWIA treats as evidence of insurability. Certificates are "
     "searchable on TDI's site. (A WPI-3 appears in older materials; "
     "verify at tdi.texas.gov/wind before relying on it as a live form.)",
     "Issued by TDI after the phase inspections"),
    ("TCEQ Form 0235 — OSSF Permit Application",
     "The septic application <b>where TCEQ itself is the permitting "
     "authority</b> — most counties are their own authorized agent and "
     "publish their own packet instead (Comal County's Engineer's Office "
     "packet is a verified example). <b>When:</b> before construction; "
     "the site evaluation comes first.",
     "TCEQ (tceq.texas.gov) or your county's authorized agent"),
    ("ESL builder self-certification form (Texas Building Energy Code "
     "Compliance)",
     "The § 388.004(a)(3) route: for a house outside any city, the "
     "builder certifies energy-code compliance on the Energy Systems "
     "Laboratory's form, enumerating the code-compliance features. "
     "<b>When:</b> at completion — then keep the original three years and "
     "give the owner a copy (§ 388.004(b)).",
     "Energy Systems Laboratory, esl.tamu.edu"),
    ("TxDOT Form 1058 — Permit to Construct Access Driveway Facilities on "
     "Highway Right of Way",
     "Required before constructing a driveway onto a state-system highway "
     "(FM roads included). Filed with the local TxDOT district/area "
     "office; no work in the right of way until the executed permit is in "
     "hand, with 24-hour notice to TxDOT. District-specific requirement "
     "sheets exist.",
     "TxDOT district / area office"),
    ("County floodplain development permit",
     "Every NFIP county has one; the name varies (\"Development Permit,\" "
     "\"Floodplain Development Permit\"). Montgomery County's residential "
     "development permit — structure and non-structure versions — is the "
     "verified example, and it applies even outside the floodplain there. "
     "<b>When:</b> before construction, if any part of the site is in an "
     "SFHA (or countywide where so ordered).",
     "County floodplain administrator (Montgomery: mctx.org)"),
    ("Houston Form CE1284 — Homeowner's Plumbing and Irrigation System "
     "Permit Application",
     "Houston's owner path for plumbing: the homeowner may pull the "
     "permit and do the work on a residence they \"own, occupy, and have "
     "… registered as their homestead.\" Remember the contrast: Houston "
     "has <b>no</b> homeowner path for electrical.",
     "Houston Permitting Center, houstonpermittingcenter.org"),
    ("Fort Worth Homestead Permit Affidavit",
     "The homeowner certifies they own and live at the address and will "
     "personally perform the work under a specific permit — published in "
     "mechanical and plumbing versions by Development Services.",
     "City of Fort Worth, fortworthtexas.gov"),
    ("San Antonio Residential Building Permit Application + homeowner's "
     "permit attestation",
     "The city's residential application (2025 form), plus the "
     "homeowner's-permit route: attest that you own and will occupy or "
     "rent the residence for 12 months after completion, and take "
     "responsibility for all inspections.",
     "San Antonio DSD — sa.gov; forms at docsonline.sanantonio.gov"),
    ("Your subcontract — the homestead lien \"form\"",
     "Not a government form at all, and more important than most that "
     "are: to fix a lien on a homestead the contract must be written, "
     "executed <b>before</b> material or labor, signed by <b>both "
     "spouses</b> if married, and <b>filed with the county clerk</b> "
     "(Property Code § 53.254). Good subs will insist; treat one who "
     "will not as a warning.",
     "You write it — see TX.2's lien section"),
    ("TDLR electrical exemption — deliberately NOT a form",
     "There is no TDLR form for the homeowner electrical exemption; it is "
     "self-executing in the statute. What you print instead — for a "
     "doubting county official or utility — is TDLR's own exemptions "
     "page, and (for a new build) TDLR's written answer to the "
     "owns-and-resides question from TX.1.",
     "tdlr.texas.gov/electricians/exemptions.htm"),
]

rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in DOCS]
flow.append(k.ref_table(
    "Named forms and documents a Texas owner-builder will encounter",
    [k.cellp("Document", bold=True),
     k.cellp("What it is and when you need it", bold=True),
     k.cellp("Where it comes from", bold=True)],
    rows, [1.75 * inch, CW - 1.75 * inch - 1.85 * inch, 1.85 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout("Forms that do not exist — stop looking for them", [
    Paragraph("There is no state owner-builder affidavit (no state permit "
              "exists to attach one to), no county building-permit "
              "application for a single-family house, no certificate of "
              "occupancy in unincorporated areas, and no TDLR exemption "
              "form. When a lender or insurer asks for \"the permit\" on "
              "a Track B build, what you hand them instead is this kit's "
              "stack: the OSSF permit, the floodplain permit, the energy "
              "certification, the meter release — and, coastal, the "
              "WPI-8.", S["body"]),
]))

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026): WPI-1 notice before "
    "construction and the certificate routes — Insurance Code "
    "§ 2210.2515(b), (c), (d); WPI-8/WPI-8-E on tdi.texas.gov/wind, where "
    "the WPI-3 hedge should also be checked. TCEQ Form 0235 and the "
    "authorized-agent structure — tceq.texas.gov; Comal County packet, "
    "comalcounty.gov. ESL self-certification form and the three-year "
    "retention duty — Health &amp; Safety Code § 388.004(a)(3), (b); "
    "esl.tamu.edu. TxDOT Form 1058 — 43 TAC § 11.52; district offices. "
    "Montgomery County development permits — mctx.org. Houston CE1284 — "
    "houstonpermittingcenter.org. Fort Worth Homestead Permit Affidavits "
    "— fortworthtexas.gov. San Antonio application and homeowner "
    "attestation — sa.gov and docsonline.sanantonio.gov. Homestead lien "
    "contract requirements — Property Code § 53.254. Statutes at "
    "statutes.capitol.texas.gov."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "tx-permit-kit",
                       "TX.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
