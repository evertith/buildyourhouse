#!/usr/bin/env python3
"""VA.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame,
centered title block, aligned project fill-in rules, brand and edition line.
Pages 2–3 are the orientation: what is in the kit, how to work it, and the
six Virginia headline facts, each carrying its citation.

Sources verified August 2026 (all also cited on-page):
  § 54.1-1101(A)(7)   owner may build one primary residence for his own use
                      in any 24-month period without a contractor license
  § 54.1-1111         the written statement + affidavit signed at permit time
  13VAC5-63; DHCD     2021 USBC in force since Jan. 18, 2024; the only
                      permitted edition since Jan. 18, 2025
  § 36-98.01          mechanics' lien agent line on every 1–2 family permit,
                      at the applicant's option, else "None Designated"
  § 43-4.01           designating an agent forces lien claimants to 30-day
                      notice
  USBC § 103.5; 12VAC5-610-240   septic approval can gate the building permit
  24VAC30-73-60(A)    VDOT entrance permit before constructing a driveway
                      connection to a state-maintained road
  13VAC5-63-264       blower-door test mandatory, max 5 ACH50 in Zone 4
  § 36-98; § 36-105   one statewide code, enforced by local building depts

Still deliberately hedged: nothing on the cover itself — it prints only
dossier-verified headline facts; every hedged detail lives in VA.1–VA.5.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

import design as d
import kit as k

S = k.S
CW = k.CW
PAGE_W, PAGE_H = letter

FORM_ID = "VA.0"
FORM_TITLE = "Cover & How to Use"
TOPIC = "Start Here"


def draw_cover(c):
    d.register_fonts()
    c.setStrokeColor(d.INK)
    c.setLineWidth(2)
    c.rect(0.55 * inch, 0.55 * inch, PAGE_W - 1.1 * inch, PAGE_H - 1.1 * inch)
    c.setLineWidth(0.75)
    c.rect(0.65 * inch, 0.65 * inch, PAGE_W - 1.3 * inch, PAGE_H - 1.3 * inch)

    cx = PAGE_W / 2

    c.setFillColor(d.INK)
    c.setFont(d.BOLD, 30)
    c.drawCentredString(cx, 8.75 * inch, "VIRGINIA")
    c.setFont(d.BOLD, 30)
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 7.13 * inch,
                        "Qualify for the exemption · File the permit · "
                        "Pass the inspections")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "County / City:", "Owner-Builder:",
              "Permit Application Date:"]
    label_x = 3.05 * inch
    rule_x0 = 3.2 * inch
    rule_x1 = PAGE_W - 1.35 * inch
    y = 5.5 * inch
    c.setFillColor(d.INK)
    for label in fields:
        c.setFont(d.BODY, 12)
        c.drawRightString(label_x, y, label)
        c.setLineWidth(0.75)
        c.line(rule_x0, y - 2, rule_x1, y - 2)
        y -= 0.62 * inch

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.35 * inch,
                        "Every Virginia statute, regulation, and requirement "
                        "in this kit")
    c.drawCentredString(cx, 2.13 * inch,
                        "is cited on the page it appears on — verified "
                        "August 2026.")

    c.setFont(d.BOLD, 12)
    c.setFillColor(d.INK)
    c.drawCentredString(cx, 1.5 * inch, "BUILD YOUR HOUSE")
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 1.27 * inch, "build-your-house.com")
    c.drawCentredString(cx, 1.03 * inch, "First Edition — 2026")


flow = [Spacer(1, 1)]

flow.append(Paragraph("How to Use This Kit", S["title"]))
flow.append(Paragraph(
    "Five working documents that take a Virginia owner-builder from \"am I "
    "allowed to do this?\" to a certificate of occupancy.",
    S["subtitle"]))

flow.append(k.body(
    "Virginia is one of the cleaner states to build your own home in: the "
    "owner-builder exemption is a single sentence of statute, and the "
    "building code is <b>one statewide edition</b> — the Uniform Statewide "
    "Building Code — that no county or city may vary (Code of Virginia "
    "§ 36-98). What trips owner-builders up is that the USBC is "
    "<b>enforced locally</b>: every county, city, and town runs its own "
    "building department (§ 36-105), each with its own forms, fees, and "
    "portal. This kit separates the two — what the Commonwealth requires, "
    "fixed and cited here, and what your locality requires, which you fill "
    "in."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>VA.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("Whether you qualify, what you sign, and the strings the "
             "statute attaches. <b>Read this first.</b>")],
    [k.cellp("<b>VA.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather and verify before you file — zoning, septic "
             "and well, driveway, erosion control, energy code, the lien "
             "agent line.")],
    [k.cellp("<b>VA.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The statewide minimum inspections in order, what each one "
             "checks, and fields for dates and results.")],
    [k.cellp("<b>VA.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("Your locality's offices and portals, the state agencies, and "
             "how to find each one.")],
    [k.cellp("<b>VA.5</b>"), k.cellp("Forms &amp; Documents Index"),
     k.cellp("Each document you will meet: what it is, when, and from "
             "where.")],
]
flow.append(k.ref_table(
    "The five documents",
    [k.cellp("", bold=True), k.cellp("Document", bold=True),
     k.cellp("What it does for you", bold=True)],
    rows, [0.55 * inch, 2.05 * inch, CW - 2.6 * inch]))

flow += k.h2("HOW TO USE IT")
flow.append(k.bullet(
    "<b>Start with VA.1.</b> If you do not qualify for the exemption, "
    "nothing else in the kit matters yet."))
flow.append(k.bullet(
    "<b>Fill in VA.4 before you need it.</b> Ten minutes of phone calls "
    "early saves a week of chasing later."))
flow.append(k.bullet(
    "<b>Work VA.2 with a pen</b> and do not file until the boxes are "
    "checked. Incomplete applications are the most common cause of delay."))
flow.append(k.bullet(
    "<b>Keep VA.3 on the job</b> and record every inspection date and "
    "result as it happens."))

# ---------------------------------------------------------------- headline facts
flow += k.h2_tight("VIRGINIA IN SIX FACTS")
facts = [
    [k.cellp("<b>The exemption</b>"),
     k.cellp("You may build (or supervise building) <b>one primary "
             "residence, owned by you and for your own use, in any 24-month "
             "period</b> — no contractor license required. You claim it "
             "with a written statement supported by an affidavit at the "
             "permit counter."),
     k.cellp("§ 54.1-1101(A)(7); § 54.1-1111")],
    [k.cellp("<b>The code</b>"),
     k.cellp("The <b>2021 USBC</b> (2021 I-Codes, 2020 NEC) has governed "
             "since January 18, 2024, and has been the only permitted "
             "edition since January 18, 2025. The next edition is not "
             "expected before 2027."),
     k.cellp("13VAC5-63; dhcd.virginia.gov/codes")],
    [k.cellp("<b>The lien agent</b>"),
     k.cellp("Every one/two-family permit carries a mechanics' lien agent "
             "line — designated at <b>your option</b>, else the permit says "
             "\"None Designated.\" Designating one forces lien claimants to "
             "give notice within 30 days or lose lien coverage for earlier "
             "work."),
     k.cellp("§ 36-98.01; § 43-4.01")],
    [k.cellp("<b>The septic gate</b>"),
     k.cellp("On an unsewered lot, the VDH sewage approval comes first: the "
             "building official may refuse the building permit until state "
             "functional-design approval is in hand."),
     k.cellp("USBC § 103.5; 12VAC5-610-240")],
    [k.cellp("<b>The driveway</b>"),
     k.cellp("Most Virginia roads outside cities are state-maintained. A "
             "new entrance onto one requires a <b>VDOT land use permit "
             "before construction</b>."),
     k.cellp("24VAC30-73-60(A)")],
    [k.cellp("<b>The blower door</b>"),
     k.cellp("A blower-door test is <b>mandatory</b> for every new dwelling "
             "— there is no visual-inspection option — with a maximum "
             "leakage of 5 ACH50 in Climate Zone 4."),
     k.cellp("13VAC5-63-264")],
]
flow.append(k.ref_table(
    "The headline facts — each unpacked in the document it belongs to",
    [k.cellp("Fact", bold=True), k.cellp("What Virginia says", bold=True),
     k.cellp("Authority", bold=True)],
    facts, [1.2 * inch, CW - 1.2 * inch - 1.85 * inch, 1.85 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Virginia claim here was read against its primary "
                  "source — the Code of Virginia and Virginia "
                  "Administrative Code at law.lis.virginia.gov, plus the "
                  "responsible agencies' own pages — in August 2026, and is "
                  "cited where it appears; where localities differ the kit "
                  "says so and gives the verification step. This is a "
                  "process reference, not legal advice, and does not "
                  "replace your building department or the USBC itself. "
                  "Virginia's code changed editions as recently as 2024 — "
                  "confirm anything you rely on.", S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "va-permit-kit",
                       "VA.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
