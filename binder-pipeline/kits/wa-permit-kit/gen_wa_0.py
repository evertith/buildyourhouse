#!/usr/bin/env python3
"""WA.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame,
centered title block, aligned project fill-in rules, brand and edition line.
Page 2 is the one-page orientation.
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

FORM_ID = "WA.0"
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
    c.drawCentredString(cx, 8.75 * inch, "WASHINGTON")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 7.13 * inch,
                        "Keep the exemption · File the permits · "
                        "Pass the inspections")

    fields = ["Project Address:", "County:", "City / Town:",
              "Owner-Builder:", "Permit Application Date:"]
    label_x = 3.05 * inch
    rule_x0 = 3.2 * inch
    rule_x1 = PAGE_W - 1.35 * inch
    y = 5.72 * inch
    c.setFillColor(d.INK)
    for label in fields:
        c.setFont(d.BODY, 12)
        c.drawRightString(label_x, y, label)
        c.setLineWidth(0.75)
        c.line(rule_x0, y - 2, rule_x1, y - 2)
        y -= 0.58 * inch

    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.35 * inch,
                        "Every Washington statute, rule, and threshold in "
                        "this kit")
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
    "Five working documents that take a Washington owner-builder from "
    "\"am I allowed to do this?\" to a final inspection.",
    S["subtitle"]))

flow.append(k.body(
    "Washington gives you a genuinely good deal. The building code is "
    "statewide and mandatory — \"<i>there shall be in effect in all counties "
    "and cities the state building code</i>\" — so there is no county where "
    "the rules are a mystery, and none where they simply do not apply. There "
    "is no general contractor license to qualify for, only a registration you "
    "are exempt from on your own property. And a complete permit application "
    "<b>locks in the rules on the day you file it</b>."))

flow.append(k.body(
    "What catches owner-builders here is not difficulty, it is <b>geography of "
    "authority</b>: the permits for one house come from more than one agency. "
    "Your building permit comes from a city or county. Your <b>electrical</b> "
    "permit usually comes from the State — Labor &amp; Industries — because "
    "the residential code hands electrical work to a different rule book "
    "entirely: \"<i>Electrical Code is regulated by chapter 296-46B WAC or "
    "Electrical Code as adopted by the local jurisdiction.</i>\" Septic and "
    "wells come from a third office again. This kit separates them so you "
    "know which counter you are standing at."))
flow.append(k.cite(
    "RCW 19.27.031(1); WAC 51-51-003, the rule adopting the 2021 "
    "International Residential Code for Washington. Both read at "
    "app.leg.wa.gov, August 2026."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>WA.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("Which exemption you are actually using, what takes it away, and "
             "the separate rules for doing your own electrical and plumbing. "
             "<b>Read this first.</b>")],
    [k.cellp("<b>WA.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather and verify before you file — water, septic, "
             "critical areas, the energy code paperwork, and the clocks the "
             "State puts on your reviewer.")],
    [k.cellp("<b>WA.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The order inspections happen in, which agency calls each one, "
             "the three tests you must pass, and fields for dates and "
             "results.")],
    [k.cellp("<b>WA.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("Every office you will deal with, how to find yours, and a page "
             "to write down what you confirmed.")],
    [k.cellp("<b>WA.5</b>"), k.cellp("Forms &amp; Documents Index"),
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
    "<b>Start with WA.1.</b> If you do not qualify for the exemption, "
    "nothing else in the kit matters yet."))
flow.append(k.bullet(
    "<b>Fill in WA.4 before you need it.</b> Washington sends you to more "
    "counters than most states; an hour spent finding them early saves a "
    "week of chasing later."))
flow.append(k.bullet(
    "<b>Work WA.2 with a pen</b> and do not file until the boxes are "
    "checked. In Washington a <i>complete</i> application is worth more than "
    "an early one — completeness is what starts your reviewer's clock and "
    "what freezes the rules in your favor."))
flow.append(k.bullet(
    "<b>Keep WA.3 on the job</b> and record every inspection date and result "
    "as it happens — including the ones you call to a different agency."))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Washington claim here was read against its primary "
                  "source — the RCW and WAC text at app.leg.wa.gov, and the "
                  "responsible agency's own pages — in August 2026, and is "
                  "cited where it appears. Where the answer is local, the kit "
                  "says so and gives you the verification step instead of "
                  "guessing. This is a process reference, not legal advice, "
                  "and it does not replace your building department or the "
                  "State Building Code. Washington runs a three-year code "
                  "cycle and amends between cycles — confirm anything you "
                  "rely on.", S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "wa-permit-kit",
                       "WA.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
