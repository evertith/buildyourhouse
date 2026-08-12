#!/usr/bin/env python3
"""GA.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame,
centered title block, aligned project fill-in rules, brand and edition line.
Page 2 is the one-page orientation with Georgia's headline facts.

Sources verified August 2026 (each also cited where it appears in GA.1–GA.5):
  O.C.G.A. § 43-41-17(h)   owner exemption — own land, own occupancy, no
                           license at any project cost; one-sale-per-24-months
  O.C.G.A. § 43-41-2(9)    residential contractor licensing attaches over
                           $2,500 of work
  O.C.G.A. § 8-2-25(a)     the eight mandatory state minimum codes apply
                           statewide with no local adoption
  O.C.G.A. § 8-2-26(a)(4)  permits and inspections are a local-option power
  DCA, new mandatory state codes effective January 1, 2026: 2024 I-Codes with
    2026 Georgia Amendments; 2023 NEC; energy stays the 2015 IECC with the
    Georgia Supplements and Amendments (dca.georgia.gov)
  GA IECC amendments R402.4.1.2, R403.3.3 — the two mandatory DET tests
  DPH Rule 511-3-1-.03(2)  no physical development of a septic lot before the
                           county construction permit

Still deliberately hedged: O.C.G.A. quotes trace to a mirror current through
March 28, 2024 (2024-2025 session laws pending recheck — none reported to
touch the exemption text); which counties actually enforce permits is a
worksheet question, not a printed roster.
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

FORM_ID = "GA.0"
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
    c.drawCentredString(cx, 8.75 * inch, "GEORGIA")
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
    fields = ["Project Address:", "County:", "Owner-Builder:",
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
                        "Every Georgia statute, rule, and requirement in "
                        "this kit is cited on the")
    c.drawCentredString(cx, 2.13 * inch,
                        "page it appears on — verified August 2026.")

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
    "Five working documents that take a Georgia owner-builder from \"am I "
    "allowed to do this?\" to a certificate of occupancy.",
    S["subtitle"]))

flow.append(k.body(
    "Georgia is one of the friendlier states to build your own home in — "
    "and one of the strangest to permit in. The eight state minimum codes "
    "bind you statewide whether or not anyone enforces them (§ 8-2-25(a)), "
    "but <b>permits and inspections are a local option</b> (§ 8-2-26(a)(4)) "
    "— some counties run full permit portals, and some have no building "
    "department at all. This kit separates the two: what the State fixes, "
    "cited here, and what your jurisdiction decides, which you fill in."))

fact_rows = [
    [k.cellp("The owner exemption is real and cost-unlimited — own land, "
             "own occupancy, not for sale or lease. But <b>one sale of a "
             "self-built structure within 24 months</b> (measured from that "
             "structure's CO) poisons the exemption for the next build."),
     k.cellp("§ 43-41-17(h)")],
    [k.cellp("Contractor licensing attaches over <b>$2,500</b> of work — "
             "among the lowest thresholds in the country. It governs the "
             "people you hire, not you."),
     k.cellp("§ 43-41-2(9)")],
    [k.cellp("Effective <b>January 1, 2026</b>: 2024 I-Codes with 2026 "
             "Georgia Amendments and the <b>2023 NEC</b>; energy stays the "
             "<b>2015 IECC</b> with Georgia amendments. Two tests are "
             "mandatory — blower door under <b>5 ACH50</b>, duct leakage "
             "at or under <b>6 cfm25/100 sq ft</b> — by a certified DET "
             "verifier."),
     k.cellp("DCA; GA IECC R402.4.1.2, R403.3.3")],
    [k.cellp("On a septic lot, <b>no physical development may begin</b> "
             "until the County Health Department issues the septic "
             "construction permit."),
     k.cellp("DPH Rule 511-3-1-.03(2)")],
]
flow.append(k.ref_table(
    "Georgia headline facts (each developed, with its full cite, in GA.1–GA.3)",
    [k.cellp("The fact", bold=True), k.cellp("Authority", bold=True)],
    fact_rows, [CW - 1.7 * inch, 1.7 * inch]))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>GA.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("Whether you qualify, the 24-month rule, doing your own trade "
             "work, and what takes the exemption away. <b>Read this "
             "first.</b>")],
    [k.cellp("<b>GA.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather and verify before you file — the code stack, "
             "septic and well, erosion control, driveway, Notice of "
             "Commencement, energy tests.")],
    [k.cellp("<b>GA.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The inspection ladder for a Georgia dwelling, the energy-test "
             "gates, and fields for dates and results.")],
    [k.cellp("<b>GA.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("Your county's offices and portals, the state agencies, and "
             "how to find each one.")],
    [k.cellp("<b>GA.5</b>"), k.cellp("Forms &amp; Documents Index"),
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
    "<b>Start with GA.1.</b> If you do not qualify — or you sold a "
    "self-built house in the last 24 months — nothing else matters yet."))
flow.append(k.bullet(
    "<b>Settle jurisdiction first</b> (GA.4): whether your parcel is "
    "inside a city, and whether your county enforces permits at all."))
flow.append(k.bullet(
    "<b>Work GA.2 with a pen</b> and do not file until the boxes are "
    "checked. On a septic lot, the health-department permit comes before "
    "you touch the ground."))
flow.append(k.bullet(
    "<b>Keep GA.3 on the job</b> and record every inspection date and "
    "result as it happens — especially the two DET test reports."))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Georgia claim here was read against its primary "
                  "source in August 2026 and is cited where it appears; "
                  "where counties differ the kit says so. One honest "
                  "caveat: O.C.G.A. text was read at a mirror current "
                  "through March 28, 2024. The 2024–2025 session laws "
                  "(SB 503, HB 635, SB 125) postdate it; none is reported "
                  "to change the exemption text this kit quotes, but "
                  "confirm anything you rely on at the official code. "
                  "This is a process reference, not legal advice.",
                  S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ga-permit-kit",
                       "GA.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
