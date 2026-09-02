#!/usr/bin/env python3
"""AR.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame, centered
title block, aligned project fill-in rules, brand and edition line. Page 2 is
the one-page orientation.

Like Kentucky's, the Arkansas cover carries a "Local Building Department" field
with an explicit "or write NONE" instruction, because in Arkansas that is a real
possible answer. The Arkansas Fire Prevention Code binds the house as a
construction standard, but nothing in Arkansas law requires a county to create a
building department, and the code's own text ("should they choose to adopt",
AFPC Vol. I Section 101.2.2) concedes that local adoption is a choice.
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

FORM_ID = "AR.0"
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
    c.drawCentredString(cx, 8.75 * inch, "ARKANSAS")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    # Centered on the PAGE, while the audit frame is the mirrored CONTENT box
    # [64.8, 568.8] — so the usable width here is 2*(306-64.8) = 482pt, not the
    # 504pt content width. This line measures 469pt at 12.5; "…Build to the
    # code regardless" measured 494 and clipped the left margin.
    c.drawCentredString(cx, 7.13 * inch,
                        "Find out who inspects · File what applies anyway · "
                        "Build to code regardless")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "City / Town:", "County:",
              "Local Building Department:", "Owner-Builder:",
              "Permit Application Date:"]
    # "Local Building Department:" is the widest label on any kit cover, so the
    # gutter sits at 3.28in to stay clear of the 0.9in binding margin.
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
                        "If your county has no building department, write "
                        "NONE — and read AR.1 before anything else.")

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.28 * inch,
                        "Every Arkansas statute, code section and requirement "
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
    "Five working documents, from \"is there even a building department "
    "here?\" to the last inspection.",
    S["subtitle"]))

flow.append(k.body(
    "Arkansas does something that catches nearly every owner-builder out. It "
    "writes <b>one building code for the entire state</b> — the Arkansas Fire "
    "Prevention Code — and it forbids your city or county from adopting a "
    "different one. Then it declines to make anybody enforce it on a house."))
flow.append(k.body(
    "There is no statewide building permit for a one- or two-family dwelling, "
    "no state residential plan review, and no state building inspector. The "
    "code's own text gives the game away: local governments may adopt the "
    "Arkansas Fire Prevention Code \"<i>should they choose to adopt</i>\" it "
    f"(Volume I, Section 101.2.2). Cities are <b>permitted</b> to require a "
    f"building permit (Ark. Code Ann. {k.sec('14-56-202')}) — not required "
    f"to. Counties have only a general power to provide services "
    f"({k.sec('14-14-802')}), and \"building codes\" appears nowhere in what "
    f"that statute lists. Most unincorporated Arkansas has no building "
    f"department at all."))
flow.append(k.body(
    "So in much of this state the code legally governs your house and "
    "<i>no building official will ever look at it.</i> That is not permission "
    "to build badly — the standard still applies to you, and so does your "
    "liability. It means <b>you</b> are the inspection."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>AR.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("The licensing exemption for building your own home, what you may "
             "do yourself trade by trade, and the question that reshapes the "
             "whole build: does a building permit exist where you are "
             "building? <b>Read this first.</b>")],
    [k.cellp("<b>AR.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather before you file — the approvals that apply "
             "wherever you build, the code editions actually in force, and "
             "what Arkansas deleted from the residential code.")],
    [k.cellp("<b>AR.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The order inspections happen in, who calls each one when there "
             "is no building department, and fields for dates and results.")],
    [k.cellp("<b>AR.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("How to find out whether your jurisdiction issues permits at "
             "all, the offices that exist even when no building department "
             "does, and a page to record every one you confirmed.")],
    [k.cellp("<b>AR.5</b>"), k.cellp("Forms &amp; Documents Index"),
     k.cellp("Each document you will meet: what it is, when, and from "
             "where — plus what needs no permit at all.")],
]
flow.append(k.ref_table(
    "The five documents",
    [k.cellp("", bold=True), k.cellp("Document", bold=True),
     k.cellp("What it does for you", bold=True)],
    rows, [0.55 * inch, 2.05 * inch, CW - 2.6 * inch]))

flow += k.h2("HOW TO USE IT")
flow.append(k.bullet(
    "<b>Start with AR.1.</b> Its first section settles whether a building "
    "permit exists where you are building. Nothing else in the kit sequences "
    "correctly until you know that answer."))
flow.append(k.bullet(
    "<b>Then deal with the septic system.</b> On a rural Arkansas build the "
    "onsite wastewater permit is the longest pole, and it is a state "
    "requirement that does not care whether your county issues building "
    "permits."))
flow.append(k.bullet(
    "<b>Work AR.2 with a pen.</b> The approvals that apply everywhere deserve "
    "more of your attention than the one that might not apply at all."))
flow.append(k.bullet(
    "<b>Keep AR.3 on the job</b> and record every inspection as it happens — "
    "most of all if nobody is required to inspect you. It is the only "
    "evidence you will have when you sell, refinance or insure."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Arkansas claim here was read against its primary "
                  "source in September 2026 — the Arkansas Code, the Code of "
                  "Arkansas Rules, the Arkansas Fire Prevention Code's own "
                  "adopted text, and the state agencies' own pages — and is "
                  "cited where it appears. Where the answer genuinely depends "
                  "on your city or county, the kit says so and gives you a "
                  "line to write down what you confirmed. Not legal advice.",
                  S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ar-permit-kit",
                       "AR.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
