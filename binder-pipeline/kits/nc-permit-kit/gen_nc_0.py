#!/usr/bin/env python3
"""NC.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom (gen_master.build_cover)
— double frame, centered title block, aligned project fill-in rules, brand and
edition line. Page 2 is the one-page orientation.
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

FORM_ID = "NC.0"
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
    c.drawCentredString(cx, 8.75 * inch, "NORTH CAROLINA")
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
                        "Every North Carolina statute, threshold, and "
                        "requirement in this kit")
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
    "Five working documents that take a North Carolina owner-builder from "
    "\"am I allowed to do this?\" to a certificate of compliance.",
    S["subtitle"]))

flow.append(k.body(
    "North Carolina is one of the better states to build your own home in: "
    "the law is written in your favor and the building code is statewide. "
    "What trips owner-builders up is that <b>permits are administered by 100 "
    "counties and dozens of municipalities</b>, each with its own forms and "
    "portal. This kit separates the two — what the State requires, fixed and "
    "cited here, and what your jurisdiction requires, which you fill in."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>NC.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("Whether you qualify, what you swear to, and what takes the "
             "exemption away. <b>Read this first.</b>")],
    [k.cellp("<b>NC.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather and verify before you file — zoning, septic and "
             "well, driveway, erosion control, energy code.")],
    [k.cellp("<b>NC.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The order inspections happen in, what each one checks, and "
             "fields for dates and results.")],
    [k.cellp("<b>NC.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("Your county's offices, numbers, and portals — and how to find "
             "each one.")],
    [k.cellp("<b>NC.5</b>"), k.cellp("Forms &amp; Documents Index"),
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
    "<b>Start with NC.1.</b> If you do not qualify for the exemption, "
    "nothing else in the kit matters yet."))
flow.append(k.bullet(
    "<b>Fill in NC.4 before you need it.</b> Ten minutes of phone calls "
    "early saves a week of chasing later."))
flow.append(k.bullet(
    "<b>Work NC.2 with a pen</b> and do not file until the boxes are "
    "checked. Incomplete applications are the most common cause of delay."))
flow.append(k.bullet(
    "<b>Keep NC.3 on the job</b> and record every inspection date and result "
    "as it happens."))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every North Carolina claim here was read against its "
                  "primary source in August 2026 and is cited where it "
                  "appears; where counties differ the kit says so and gives "
                  "the verification step. This is a process reference, not "
                  "legal advice, and does not replace your inspections "
                  "department or the State Building Code. North Carolina "
                  "moved the contractor threshold as recently as 2023 — "
                  "confirm anything you rely on.", S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "nc-permit-kit",
                       "NC.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
