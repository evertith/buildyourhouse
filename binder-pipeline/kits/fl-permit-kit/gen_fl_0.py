#!/usr/bin/env python3
"""FL.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame, centered
title block, aligned project fill-in rules, brand and edition line. Page 2 is
the one-page orientation.

The cover carries a "Clerk of Court (for the NOC)" field, which no other state's
cover needs. Florida is the only state in the program where a county office
OUTSIDE the building department can stop your inspections: s. 713.135(1)(d),
Fla. Stat. bars the building department from performing the first inspection
until a certified copy of the recorded Notice of Commencement is on file. The
clerk who records it is therefore a permitting contact, and the cover treats it
as one.
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

FORM_ID = "FL.0"
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
    c.drawCentredString(cx, 8.75 * inch, "FLORIDA")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    # 12.5pt keeps this inside the 478pt the inner frame allows.
    c.drawCentredString(cx, 7.13 * inch,
                        "Sign the disclosure · Record the notice · "
                        "Pass the inspections")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "City / Town:", "County:",
              "Building Department:", "Clerk of Court (for the NOC):",
              "Owner-Builder:", "Permit Application Date:"]
    # "Clerk of Court (for the NOC):" is the widest label this cover carries,
    # so the gutter sits at 3.45in to keep it clear of the 0.9in binding
    # margin; the rule then starts at 3.60in.
    label_x = 3.45 * inch
    rule_x0 = 3.60 * inch
    rule_x1 = PAGE_W - 1.35 * inch
    y = 5.95 * inch
    c.setFillColor(d.INK)
    for label in fields:
        c.setFont(d.BODY, 12)
        c.drawRightString(label_x, y, label)
        c.setLineWidth(0.75)
        c.line(rule_x0, y - 2, rule_x1, y - 2)
        y -= 0.52 * inch

    c.setFont(d.BODY, 9.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.30 * inch,
                        "In Florida the clerk who records your Notice of "
                        "Commencement is a permitting")
    c.drawCentredString(cx, 2.11 * inch,
                        "contact too — no recorded notice, no first "
                        "inspection. Read FL.1 first.")

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 1.80 * inch,
                        "Every Florida statute, rule and threshold in this "
                        "kit")
    c.drawCentredString(cx, 1.60 * inch,
                        "is cited on the page it appears on — verified "
                        "September 2026.")

    c.setFont(d.BOLD, 12)
    c.setFillColor(d.INK)
    c.drawCentredString(cx, 1.16 * inch, "BUILD YOUR HOUSE")
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 0.96 * inch, "build-your-house.com")
    c.drawCentredString(cx, 0.78 * inch, "First Edition — 2026")


flow = [Spacer(1, 1)]

flow.append(Paragraph("How to Use This Kit", S["title"]))
flow.append(Paragraph(
    "Five working documents, from the disclosure statement you have to sign "
    "in person to the certificate of occupancy.",
    S["subtitle"]))

flow.append(k.body(
    "Most states in this series raise the same question first: <i>will anyone "
    "actually inspect this house?</i> In Florida that question has no "
    "purchase. One building code binds every parcel in all 67&nbsp;counties, every "
    "jurisdiction issues permits and inspects, and your local government is "
    "not free to write its own residential code instead."))
flow.append(k.body(
    "So Florida's real question is a different one: <b>how many separate "
    "offices have to say yes before the building department will even look at "
    "your application?</b> The building permit is one of them. Depending on "
    "your lot, the others can include the county <b>clerk of court</b>, the "
    "Department of Environmental Protection for your septic system, a "
    "<b>water management district</b> for your well, and — if you are seaward "
    "of the coastal construction control line — the Department of "
    "Environmental Protection again, for an entirely separate state permit."))
flow.append(k.body(
    "The good news is that Florida's owner-builder exemption is one of the "
    "most generous in the country, and it is <b>two</b> exemptions rather "
    "than one — the general contracting exemption and a separate electrical "
    "exemption, written in different words, with different limits. Almost "
    "every guide collapses them into one rule and gets the limits wrong. "
    "<b>FL.1 keeps them apart</b>, because which one you are relying on "
    "changes what you may build and when you may sell it."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>FL.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("The two exemptions and their different tests, the twelve-point "
             "disclosure statement you must sign, and the personal "
             "appearance the statute requires. <b>Read this first.</b>")],
    [k.cellp("<b>FL.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather before you file — the product approval schedule "
             "for every exterior opening, the wind design criteria, the "
             "energy form, code editions and the fees to budget for.")],
    [k.cellp("<b>FL.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The Notice of Commencement that gates your first inspection, "
             "the order the rest happen in, and fields for dates and "
             "results.")],
    [k.cellp("<b>FL.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("How to establish which jurisdiction your parcel is actually "
             "in, the offices beyond the building department, and a page to "
             "write down every one you confirmed.")],
    [k.cellp("<b>FL.5</b>"), k.cellp("Forms &amp; Documents Index"),
     k.cellp("Each document you will meet: what it is, when it is due, and "
             "which office it comes from.")],
]
flow.append(k.ref_table(
    "The five documents",
    [k.cellp("", bold=True), k.cellp("Document", bold=True),
     k.cellp("What it does for you", bold=True)],
    rows, [0.55 * inch, 2.05 * inch, CW - 2.6 * inch]))

flow += k.h2("HOW TO USE IT")
flow.append(k.bullet(
    "<b>Start with FL.1.</b> The exemption is real and it is generous, but it "
    "is conditional — and two of its conditions (appearing in person, signing "
    "the disclosure) happen at the counter, not at your desk. Know them "
    "before you go."))
flow.append(k.bullet(
    "<b>Work FL.2 with a pen, early.</b> The item that surprises Florida "
    "owner-builders is the product approval schedule: every exterior window, "
    "door and skylight has to be identified by an approval number at plan "
    "review. That is a purchasing decision disguised as paperwork, and it is "
    "much cheaper to make before you order."))
flow.append(k.bullet(
    "<b>Record the Notice of Commencement before you call for the first "
    "inspection</b> — not before the final one. It is recorded at the clerk "
    "of court, not the building department, and the building department is "
    "barred by statute from inspecting until it has a certified copy."))
flow.append(k.bullet(
    "<b>Keep FL.3 on the job</b> and record every inspection as it happens, "
    "with the date and the inspector's result."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Florida claim here was read against its primary "
                  "source in September 2026 — the Florida Statutes at "
                  "flsenate.gov, the Florida Administrative Code at "
                  "flrules.org, and the Florida Building Commission's own "
                  "code and product approval pages at floridabuilding.org — "
                  "and is cited where it appears. Where a number genuinely "
                  "varies by county, the kit says so and gives you a line to "
                  "write what you confirmed rather than printing a guess. "
                  "Not legal advice.", S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "fl-permit-kit",
                       "FL.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
