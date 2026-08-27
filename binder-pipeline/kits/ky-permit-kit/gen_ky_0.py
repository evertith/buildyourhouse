#!/usr/bin/env python3
"""KY.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame, centered
title block, aligned project fill-in rules, brand and edition line. Page 2 is
the one-page orientation.

The cover carries a "Local Building Department" field with an explicit "or write
NONE" instruction, which no other state's cover needs. In Kentucky that is a
real possible answer: KRS 198B.060(1) and 815 KAR 7:125 Section 2(2)(a) make the
building permit, the inspections and the certificate of occupancy optional for a
single-family dwelling unless the local government passed an ordinance requiring
them, and KRS 198B.060(4)(b) forbids the state from filling the gap.
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

FORM_ID = "KY.0"
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
    c.drawCentredString(cx, 8.75 * inch, "KENTUCKY")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    # 12.5pt fits 478pt inside the inner frame; the longer "…permits that
    # always apply…" wording measured 501pt and clipped the left margin.
    c.drawCentredString(cx, 7.13 * inch,
                        "Find out who inspects · File the three state "
                        "permits · Pass the inspections")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "City / Town:", "County:",
              "Local Building Department:", "Owner-Builder:",
              "Permit Application Date:"]
    # "Local Building Department:" is 164pt at 12pt — the widest label any kit
    # cover carries — so the gutter sits at 3.28in rather than the usual 3.05in
    # to keep it clear of the 0.9in binding margin.
    label_x = 3.28 * inch
    rule_x0 = 3.43 * inch
    rule_x1 = PAGE_W - 1.35 * inch
    y = 5.85 * inch
    c.setFillColor(d.INK)
    for label in fields:
        c.setFont(d.BODY, 12)
        c.drawRightString(label_x, y, label)
        c.setLineWidth(0.75)
        c.line(rule_x0, y - 2, rule_x1, y - 2)
        y -= 0.56 * inch

    c.setFont(d.BODY, 9.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.62 * inch,
                        "If your city or county has no building permit "
                        "ordinance, write NONE — and read KY.1.")

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.28 * inch,
                        "Every Kentucky statute, threshold, and requirement "
                        "in this kit")
    c.drawCentredString(cx, 2.06 * inch,
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
    "Five working documents, from \"who is actually going to inspect this?\" "
    "to the certificate of occupancy.",
    S["subtitle"]))

flow.append(k.body(
    "Kentucky is one of the easiest states in the country to build your own "
    "home in, and one of the easiest to get badly wrong. There is <b>no state "
    "general contractor license</b> to be exempt from, and the statute lets a "
    "homeowner do their own wiring in one flat sentence with no conditions "
    "attached to it."))
flow.append(k.body(
    "The part nobody tells you is this. Kentucky writes <b>one mandatory "
    "residential code</b> that binds every house in the state — and then makes "
    "the <b>building permit, the inspections and the certificate of occupancy "
    "optional</b> unless your city or county passed an ordinance requiring "
    "them. The state is then <b>forbidden by statute</b> from stepping in on a "
    "single-family dwelling. So in much of Kentucky the code legally governs "
    "your house and <i>no building official will ever look at it.</i>"))
flow.append(k.body(
    "That does not mean nothing applies. Three things apply everywhere, and "
    "they are the ones that stop your build cold: a <b>state plumbing "
    "permit</b> from Frankfort, an <b>electrical certificate of approval</b> "
    "your power company needs before it will connect you, and a <b>health "
    "department septic permit</b> that has to be in hand before the state will "
    "even take your plumbing application. This kit separates the three from "
    "the optional part, and cites both."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>KY.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("What you may do yourself, trade by trade, and the one question "
             "that changes everything: does your jurisdiction require a "
             "permit? <b>Read this first.</b>")],
    [k.cellp("<b>KY.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather before you file — the state plumbing permit, the "
             "septic approval that gates it, the workers' compensation "
             "affidavit, code editions and fees.")],
    [k.cellp("<b>KY.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The order inspections happen in, who calls each one when there "
             "is no building department, and fields for dates and results.")],
    [k.cellp("<b>KY.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("How to find out whether your county has an ordinance at all, "
             "and a page to write down every office you confirmed.")],
    [k.cellp("<b>KY.5</b>"), k.cellp("Forms &amp; Documents Index"),
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
    "<b>Start with KY.1.</b> Its first section settles whether a building "
    "permit exists where you are building. Nothing else in the kit sequences "
    "correctly until you know."))
flow.append(k.bullet(
    "<b>Then call the health department</b> — the septic permit is the "
    "longest pole on a rural Kentucky build, and by statute it has to be in "
    "hand before your state plumbing application will be accepted."))
flow.append(k.bullet(
    "<b>Work KY.2 with a pen.</b> The permits that always apply are worth "
    "more attention than the one that might not."))
flow.append(k.bullet(
    "<b>Keep KY.3 on the job</b> and record every inspection as it happens — "
    "especially if nobody is required to inspect you."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Kentucky claim here was read against its primary "
                  "source in August 2026 — the Revised Statutes and the "
                  "Administrative Regulations at apps.legislature.ky.gov, and "
                  "the Department of Housing, Buildings and Construction's own "
                  "pages — and is cited where it appears. Where the answer "
                  "genuinely depends on your local ordinance, the kit says so "
                  "and gives you a line to write what you confirmed. Not legal "
                  "advice.", S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ky-permit-kit",
                       "KY.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
