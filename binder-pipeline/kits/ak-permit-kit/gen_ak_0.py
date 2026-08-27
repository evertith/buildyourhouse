#!/usr/bin/env python3
"""AK.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom (gen_master.build_cover)
— double frame, centered title block, aligned project fill-in rules, brand and
edition line. Page 2 is the one-page orientation.

The cover carries a "Building Authority (or NONE)" field the other states'
covers do not. In Alaska that is the first fact an owner-builder has to
establish, and unlike every other state the honest answer is frequently
"nobody" — which changes what the rest of the kit is for. See AK.4.
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

FORM_ID = "AK.0"
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
    c.drawCentredString(cx, 8.75 * inch, "ALASKA")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 7.13 * inch,
                        "Qualify for the exemption · File what is required · "
                        "Prove the build")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "Borough (or Unorganized):",
              "City / Village:", "Building Authority (or NONE):",
              "Owner-Builder:", "Construction Begins:"]
    # "Building Authority (or NONE):" is 176pt at 12pt — the gutter has to
    # clear the 0.9in inside margin by that much or the label runs off-frame.
    label_x = 3.45 * inch
    rule_x0 = 3.6 * inch
    rule_x1 = PAGE_W - 1.35 * inch
    y = 5.85 * inch
    c.setFillColor(d.INK)
    for label in fields:
        c.setFont(d.BODY, 12)
        c.drawRightString(label_x, y, label)
        c.setLineWidth(0.75)
        c.line(rule_x0, y - 2, rule_x1, y - 2)
        y -= 0.56 * inch

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.35 * inch,
                        "Every Alaska statute, regulation, and threshold in "
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
    "Five working documents, from \"am I allowed to do this?\" to the record "
    "that proves the build.",
    S["subtitle"]))

flow.append(k.body(
    "Alaska is the easiest state in the country to get permission to build "
    "your own house, and the hardest one to <b>prove</b> you built it "
    "properly. There is no statewide residential building code, and over "
    "most of its land area no building department, no plan review, and no "
    "inspector who will ever see your work."))
flow.append(k.body(
    "So this kit answers a question the Lower 48 never has to ask: <b>what "
    "still binds me when nobody is checking?</b> Not \"nothing\" — a short "
    "stack of <i>state</i> rules reaches your house whether or not an "
    "official visits it, one of them a criminal statute covering every "
    "dwelling unit in Alaska. A second arrives through your lender and your "
    "utility. Both are cited here."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>AK.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("Which of the two exemptions you qualify under, the trade "
             "exclusions, and the two-year rules. <b>Read this first.</b>")],
    [k.cellp("<b>AK.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather on both paths — the local-permit one, and the "
             "no-building-department one where the gates are elsewhere.")],
    [k.cellp("<b>AK.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The order inspections happen in where a code is enforced — and "
             "the self-verification record to keep where none is.")],
    [k.cellp("<b>AK.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("Whether your parcel has a building authority at all, and the "
             "offices that apply even when it does not.")],
    [k.cellp("<b>AK.5</b>"), k.cellp("Forms &amp; Documents Index"),
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
    "<b>Start with AK.1.</b> A new house and a remodel come under different "
    "paragraphs, with different conditions."))
flow.append(k.bullet(
    "<b>Then do AK.4.</b> Establish whether any government reviews your "
    "house at all. Both answers are common here."))
flow.append(k.bullet(
    "<b>Work AK.2 with a pen.</b> Off the permit path, nobody hands you a "
    "checklist."))
flow.append(k.bullet(
    "<b>Keep AK.3 on the job.</b> That record stands in for the certificate "
    "you may never get."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Alaska claim here was read against its primary "
                  "source in August 2026 — the Alaska Statutes, the "
                  "Administrative Code, and the agencies' own pages — and is "
                  "cited where it appears. Not legal advice.", S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ak-permit-kit",
                       "AK.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
