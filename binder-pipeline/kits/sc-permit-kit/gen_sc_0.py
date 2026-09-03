#!/usr/bin/env python3
"""SC.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame, centered
title block, aligned project fill-in rules, brand and edition line. Page 2 is
the one-page orientation.

The cover carries a "Register of Deeds" field, which most states in this series
do not need. South Carolina is the only state in the program where an office
outside the building department can RETROACTIVELY destroy the exemption you
built under: § 40-59-260(E) requires the owner to file a notice with the
register of deeds stating the house was built by an unlicensed builder, and
says in terms that "Failure to do so revokes the statutory exemption." The
register who indexes that notice is therefore a permitting contact, and the
cover treats it as one.
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

FORM_ID = "SC.0"
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
    c.drawCentredString(cx, 8.75 * inch, "SOUTH CAROLINA")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 7.13 * inch,
                        "Sign the disclosure · File the notice · "
                        "Pass the inspections")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "City or Town:", "County:",
              "Building Department:", "Register of Deeds:",
              "Owner-Builder:", "Permit Application Date:"]
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
                        "In South Carolina the register of deeds is a "
                        "permitting contact too — the notice you")
    c.drawCentredString(cx, 2.11 * inch,
                        "file there is what keeps your exemption alive. "
                        "Read SC.1 first.")

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 1.80 * inch,
                        "Every South Carolina statute, regulation and "
                        "threshold in this kit")
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
    "Five working documents, from the disclosure you sign at the counter to "
    "the notice you file after the house is finished.",
    S["subtitle"]))

flow.append(k.body(
    "Most states in this series raise the same question first: <i>will anyone "
    "actually inspect this house?</i> South Carolina answers it in one "
    "sentence of statute. Section 6-9-10(A) says that all municipalities and "
    "counties in this State <b>shall enforce</b> the building, energy, "
    "electrical, plumbing, mechanical, gas and fire codes — and that each one "
    "<b>shall enforce only</b> the national codes the state has adopted. Your "
    "county does not get to write its own residential code, and it does not "
    "get to decide that houses are somebody else's problem."))
flow.append(k.body(
    "So South Carolina's real question is a different one: <b>which of the "
    "small obligations attached to your exemption will you forget?</b> The "
    "exemption itself is generous and the statute is short. But it is "
    "conditional on things that happen away from your desk — appearing in "
    "person to sign, taking a disclosure statement across the counter, and "
    "filing a notice at the register of deeds <i>after</i> the house is "
    "built. Miss that last one and the statute does not fine you. It says "
    "your exemption is revoked."))
flow.append(k.body(
    "The second thing this kit keeps straight is <b>who you are allowed to "
    "pay.</b> South Carolina has three dollar thresholds that decide whether "
    "the person standing on your lot needs a credential, and they are "
    "$500, $5,000 and $10,000 — three different numbers, in two different "
    "chapters, administered by two different boards. Almost every guide "
    "prints one of them and calls it the answer. <b>SC.1 keeps them "
    "apart</b>, because the smallest one is the one that decides whether "
    "your tile setter is legal."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>SC.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("The three conditions in § 40-59-260(A), the disclosure "
             "statement printed word for word, the register-of-deeds notice "
             "that keeps the exemption alive, and the three thresholds that "
             "decide who you may hire. <b>Read this first.</b>")],
    [k.cellp("<b>SC.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather before you file — the code editions actually in "
             "force, the energy standard set by statute rather than by the "
             "code council, the termite and crawl-space amendments, and how "
             "to get a real wind number for your parcel.")],
    [k.cellp("<b>SC.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The approvals that have to exist before other things can "
             "happen, the order the inspections run in, the code edition "
             "your permit date locks you into, and fields for dates and "
             "results.")],
    [k.cellp("<b>SC.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("How to establish which jurisdiction your parcel is actually "
             "in, the offices beyond the building department, the two "
             "agencies that replaced DHEC, and a page to write down every "
             "one you confirmed.")],
    [k.cellp("<b>SC.5</b>"), k.cellp("Forms &amp; Documents Index"),
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
    "<b>Start with SC.1.</b> The exemption is real, but two of its "
    "conditions happen at a counter and one happens months after your last "
    "inspection. Know all three before you go."))
flow.append(k.bullet(
    "<b>Work SC.2 with a pen, early.</b> The item that surprises South "
    "Carolina owner-builders is the termite amendment: in a very heavy "
    "termite zone the state code bars foam plastic below grade on your "
    "foundation walls and requires a six-inch inspection strip along the "
    "sill. That is an insulation purchasing decision disguised as "
    "paperwork, and it is far cheaper to make before you order."))
flow.append(k.bullet(
    "<b>Do not accept a wind speed from a table.</b> South Carolina's code "
    "sends you to maps published by the Building Codes Council as delineated "
    "by your own building official, and a separate statute forbids drawing "
    "those boundaries on political lines. SC.2 tells you where the maps are, "
    "which eleven counties have none, and gives you a line to write your "
    "answer on."))
flow.append(k.bullet(
    "<b>Check the date on your permit against 1&#160;January&#160;2027.</b> "
    "The Council has already adopted the 2024 codes and the 2023 electrical "
    "code, to be implemented that day. A permit issued before it keeps your "
    "whole build on the codes this kit describes. SC.2 explains what changes "
    "and what does not."))
flow.append(k.bullet(
    "<b>Keep SC.3 on the job</b> and record every inspection as it happens, "
    "with the date and the inspector's result."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every South Carolina claim here was read against its "
                  "primary source in September 2026 — the Code of Laws and "
                  "the Code of Regulations at scstatehouse.gov, and the "
                  "Department of Labor, Licensing and Regulation's own "
                  "residential builder and Building Codes Council pages at "
                  "llr.sc.gov — and is cited where it appears. The state's "
                  "code amendments are quoted from Chapter 8 of the Code of "
                  "Regulations, which is where the Building Codes Council is "
                  "required to promulgate them, rather than from a summary. "
                  "Where a number genuinely varies by county, the kit says so "
                  "and gives you a line to write what you confirmed rather "
                  "than printing a guess. Not legal advice.", S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "sc-permit-kit",
                       "SC.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
