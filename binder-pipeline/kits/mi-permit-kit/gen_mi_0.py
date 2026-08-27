#!/usr/bin/env python3
"""MI.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom (gen_master.build_cover)
— double frame, centered title block, aligned project fill-in rules, brand and
edition line. Page 2 is the one-page orientation.

The cover carries an "Enforcing agency" field the other states' covers do not.
In Michigan that is the first unknown an owner-builder has to resolve, and it
is not answerable from the county name alone — see MI.4.
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

FORM_ID = "MI.0"
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
    c.drawCentredString(cx, 8.75 * inch, "MICHIGAN")
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
    fields = ["Project Address:", "Township / City / Village:", "County:",
              "Enforcing Agency:", "Owner-Builder:",
              "Permit Application Date:"]
    label_x = 3.05 * inch
    rule_x0 = 3.2 * inch
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
                        "Every Michigan statute, threshold, and requirement "
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
    "Five working documents, from \"am I allowed to do this?\" to the "
    "certificate of occupancy.",
    S["subtitle"]))

flow.append(k.body(
    "Michigan is one of the better states to build your own home in: a "
    "one-sentence licensing exemption, and permission to do your own "
    "<b>electrical, plumbing and mechanical</b> work as well — which most "
    "licensing states withhold."))
flow.append(k.body(
    "What trips owner-builders up here is not the rules but <b>finding out "
    "who enforces them.</b> One statewide code is administered by <b>1,824 "
    "separate units of government</b>, and the four trades are assigned "
    "<i>separately</i> — so one parcel can be inspected by a township for "
    "one trade and by the State of Michigan for another. This kit separates "
    "what Michigan law fixes, cited here, from what your enforcing agency "
    "decides, which you fill in."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>MI.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("Whether you qualify, the four exemptions you rely on, and "
             "what takes them away. <b>Read this first.</b>")],
    [k.cellp("<b>MI.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather before you file — the five environmental "
             "approvals, plan requirements, the sealed-plans threshold.")],
    [k.cellp("<b>MI.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The order inspections happen in, what each one checks, and "
             "fields for dates and results.")],
    [k.cellp("<b>MI.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("How to find <i>your</i> enforcing agency — per trade — and a "
             "page to write down what you confirmed.")],
    [k.cellp("<b>MI.5</b>"), k.cellp("Forms &amp; Documents Index"),
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
    "<b>Start with MI.1.</b> If you do not qualify for the exemption, "
    "nothing else here matters yet."))
flow.append(k.bullet(
    "<b>Then do MI.4 — before anything else practical.</b> Elsewhere the "
    "directory is a convenience; in Michigan it is a prerequisite."))
flow.append(k.bullet(
    "<b>Work MI.2 with a pen.</b> Incomplete applications are the "
    "commonest cause of delay."))
flow.append(k.bullet(
    "<b>Keep MI.3 on the job</b> and record every inspection as it "
    "happens."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Michigan claim here was read against its primary "
                  "source in August 2026 — the Compiled Laws, the "
                  "Administrative Code, and the Bureau of Construction "
                  "Codes' own forms and lists — and is cited where it "
                  "appears. Where enforcing agencies differ, the kit says "
                  "so. Not legal advice.", S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "mi-permit-kit",
                       "MI.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
