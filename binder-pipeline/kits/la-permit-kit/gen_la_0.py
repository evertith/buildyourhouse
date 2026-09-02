#!/usr/bin/env python3
"""LA.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame, centered
title block, aligned project fill-in rules, brand and edition line. Page 2 is
the one-page orientation.

The cover carries a "Parish" field and a separate "Permit Office" field because
in Louisiana those are two different answers: the parish building official
covers only the unincorporated area (R.S. 37:3741), so a site with a city
mailing address may still be filed with the town. The "or write NONE" idiom the
Kentucky cover needed has no place here — Louisiana forbids a local government
from avoiding enforcement (R.S. 37:3737(A)(1)), so there is always an office.
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

FORM_ID = "LA.0"
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
    c.drawCentredString(cx, 8.75 * inch, "LOUISIANA")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 7.13 * inch,
                        "Sign the right affidavit · File with the right "
                        "office · Pass the inspections")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "City / Town:", "Parish:",
              "Permit Office:", "Owner-Builder:",
              "Permit Application Date:"]
    label_x = 3.05 * inch
    rule_x0 = 3.20 * inch
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
                        "Your permit office may be the parish or the town — "
                        "LA.4 shows you how to tell.")

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.28 * inch,
                        "Every Louisiana statute, threshold, and requirement "
                        "in this kit")
    c.drawCentredString(cx, 2.06 * inch,
                        "is cited on the page it appears on — verified "
                        "September 2026.")

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
    "Five working documents, from the affidavit that gets you the permit to "
    "the certificate of occupancy your lender has to file.",
    S["subtitle"]))

flow.append(k.body(
    "Louisiana gives an owner-builder something most states do not: a named "
    "statutory exemption that lets you <b>hire and direct subcontractors</b> "
    "on your own house without a contractor license. It is not a loophole and "
    "it is not local practice — the Legislature wrote it down, and it wrote "
    "down the affidavit that proves you are entitled to it."))
flow.append(k.body(
    "It also gives you a mandatory statewide code that <b>no parish is allowed "
    "to opt out of</b>. There is no Louisiana equivalent of the rural county "
    "where nobody inspects. Every parish must enforce, and where a parish is "
    "too small to staff a counter, the law names the workaround and gives it "
    "to you by name."))
flow.append(k.body(
    "The problem is that almost everything written about building in "
    "Louisiana is out of date. The exemption statute everyone cites was "
    "<b>repealed in 2022</b>. The licensing threshold everyone quotes was "
    "changed. The construction-code chapter was <b>renumbered into a "
    "different Title</b> of the Revised Statutes, and the agency that runs it "
    "was renamed. This kit was rebuilt from the current text in September "
    "2026, and every page shows you where to check it yourself."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>LA.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("The exemption that actually exists, the one that was repealed, "
             "the affidavit and who receives it, and the trade-by-trade "
             "answer on what you may do yourself. <b>Read this first.</b>")],
    [k.cellp("<b>LA.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather before you file — the affidavit, the sewage "
             "permit, the code editions in force, the flood and wind "
             "questions, and the deadline that decides which code you "
             "build to.")],
    [k.cellp("<b>LA.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The order inspections happen in, the private-inspector route "
             "the statute gives you by name, and fields for dates and "
             "results.")],
    [k.cellp("<b>LA.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("Parish or town — how to settle which one, how to find the "
             "licensed inspector who already covers your parish, and a page "
             "to write down every office you confirmed.")],
    [k.cellp("<b>LA.5</b>"), k.cellp("Forms &amp; Documents Index"),
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
    "<b>Start with LA.1.</b> The affidavit of exemption is a precondition to "
    "your building permit, not a form you file afterwards. Knowing which "
    "statute it comes from is what stops a counter clerk handing you the "
    "wrong one."))
flow.append(k.bullet(
    "<b>Settle parish or town before anything else.</b> The parish building "
    "official covers only the unincorporated area. A city mailing address is "
    "not the same as being inside the city limits, and filing in the wrong "
    "place costs weeks. LA.4 walks it."))
flow.append(k.bullet(
    "<b>Start the sewage permit early</b> if you are not on public sewer. It "
    "is a two-stage state permit and the first stage has to be approved "
    "before you may install anything."))
flow.append(k.bullet(
    "<b>Watch the code date in LA.2.</b> Louisiana pins your house to the "
    "codes in force on the day you applied for your original building "
    "permit — which makes your application date a design decision, not "
    "paperwork."))
flow.append(k.bullet(
    "<b>Keep LA.3 on the job</b> and record every inspection as it happens, "
    "with the name of the inspector and their license number."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Louisiana claim here was read against its primary "
                  "source in September 2026 — the Revised Statutes at "
                  "legis.la.gov, the Louisiana Administrative Code at "
                  "doa.la.gov, and the Louisiana Uniform Construction Code "
                  "Commission's own compiled law-and-rules volume — and is "
                  "cited where it appears. Where the answer genuinely depends "
                  "on your parish or your town, the kit says so and gives you "
                  "a line to write what you confirmed. Not legal advice.",
                  S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "la-permit-kit",
                       "LA.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
