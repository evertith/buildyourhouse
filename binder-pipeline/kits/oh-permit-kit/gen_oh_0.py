#!/usr/bin/env python3
"""OH.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame, centered
title block, aligned project fill-in rules, brand and edition line. Page 2 is
the one-page orientation.

Like Arkansas's, the Ohio cover carries a building-department field with an
explicit "or write NONE" instruction, because in Ohio that is a real possible
answer — and unlike Arkansas, the answer is spelled out inside the code itself.
RCO section 101.5 excuses the owner from submitting construction documents,
seeking approvals, requesting inspections and obtaining a certificate of
occupancy where no certified residential building department has jurisdiction.

The cover also carries a Local Health District line, which no other kit does.
In Ohio the health district is not a rural afterthought: it permits the sewage
treatment system and the private water system under statewide rules that do not
care whether a building department exists, and RCO 102.11 hands it "sanitary
construction" even where one does.
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

FORM_ID = "OH.0"
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
    c.drawCentredString(cx, 8.75 * inch, "OHIO")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    # Centered on the PAGE, while the audit frame is the mirrored CONTENT box
    # [64.8, 568.8] — so the usable width here is 2*(306-64.8) = 482pt, not the
    # 504pt content width. This line measures 431pt at 12.5.
    c.drawCentredString(cx, 7.13 * inch,
                        "Find who is certified · File what applies anyway · "
                        "Build to the code")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "City / Village / Township:", "County:",
              "Building Department:", "Local Health District:",
              "Owner-Builder:"]
    # Labels are right-aligned to label_x, so the GUTTER has to clear the 0.9in
    # (64.8pt) binding margin by the width of the longest label. The longest
    # here is "City / Village / Township:" at 148.4pt, so 3.1in = 223.2pt puts
    # its left edge at 74.8pt — inside the frame with room to spare. Spelling
    # the department field "Residential Building Department:" instead measures
    # 199.6pt and starts at 48.8pt, which clips; the line under the fields
    # carries the full phrase instead.
    label_x = 3.1 * inch
    rule_x0 = 3.25 * inch
    rule_x1 = PAGE_W - 1.05 * inch
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
                        "No certified residential building department here? "
                        "Write NONE — and read OH.1 first.")

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.28 * inch,
                        "Every Ohio statute, code section and requirement in "
                        "this kit")
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
    "Five working documents, from \"is anybody certified to inspect this "
    "parcel?\" to the last inspection.",
    S["subtitle"]))

flow.append(k.body(
    "Ohio does something almost no other state does. It writes <b>one "
    "residential code for the entire state</b> — the Residential Code of Ohio, "
    "which by its own terms governs \"every one-, two-, or three-family "
    "dwelling\" — and then, <b>inside that same code</b>, it tells you when you "
    "do not have to file anything at all."))
flow.append(k.callout(
    f"OAC {k.rule('4101:8-1-01')}, RCO section 101.5 — the sentence this kit "
    f"is built around", [
        Paragraph("\"<b>Jurisdiction without a certified residential building "
                  "department.</b> If no municipal, township, or county "
                  "building department is certified by the Board of Building "
                  "Standards for residential buildings in accordance with "
                  "section 3781.10(E) of the Revised Code has jurisdiction, "
                  "<b>the owner is not required to make submission of "
                  "construction documents, seek approvals, request "
                  "inspections, or obtain certificates of occupancy required "
                  "in this Chapter.</b>\"", S["body"]),
    ]))
flow.append(k.body(
    "Read that twice. It is not a loophole somebody found — it is the code's "
    "own text, and the awkward grammar is the state's, not ours. Ohio does not "
    "require a city, a township or a county to run a residential building "
    "department. Where none is certified, there is no plan review, no permit, "
    "no inspection and no certificate of occupancy, because the code itself "
    "says so."))
flow.append(k.body(
    "<b>What that does not mean is that the code stops applying.</b> The "
    "standard still governs your house; only the paperwork disappears. And "
    "several things that are <i>not</i> in the building code apply to your "
    "parcel no matter what your county decided — the sewage treatment system "
    "permit, the private water system permit, and the contract and lien rules "
    "that decide whether you can be made to pay for the same work twice."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>OH.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("Why Ohio has no owner-builder exemption and does not need one, "
             "the definition chain that puts your house outside the state "
             "trade licenses altogether, and the question that reshapes the "
             "whole build: is anybody certified here? <b>Read this first.</b>")],
    [k.cellp("<b>OH.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather before you file — the approvals that apply "
             "wherever you build, the code editions actually in force, and the "
             "referenced standard Ohio changed in 2024 that almost every guide "
             "still prints wrong.")],
    [k.cellp("<b>OH.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The inspection list the RCO actually names, the one that has to "
             "happen before any work starts at all, and what to do — and "
             "record — when nobody is required to inspect you.")],
    [k.cellp("<b>OH.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("How to establish whether a certified residential building "
             "department covers your parcel, the offices that exist even when "
             "none does, and a page to record every one you confirmed.")],
    [k.cellp("<b>OH.5</b>"), k.cellp("Forms &amp; Documents Index"),
     k.cellp("Each document you will meet: what it is, when, and from where — "
             "plus the work Ohio exempts from approval outright, listed as the "
             "code lists it.")],
]
flow.append(k.ref_table(
    "The five documents",
    [k.cellp("", bold=True), k.cellp("Document", bold=True),
     k.cellp("What it does for you", bold=True)],
    rows, [0.55 * inch, 2.05 * inch, CW - 2.6 * inch]))

flow += k.h2("HOW TO USE IT")
flow.append(k.bullet(
    "<b>Start with OH.1.</b> Its first section settles whether a certified "
    "residential building department has jurisdiction over your parcel. "
    "Nothing else in the kit sequences correctly until you know that answer."))
flow.append(k.bullet(
    "<b>Then deal with the sewage system.</b> On a rural Ohio build the "
    "household sewage treatment system permit is the longest pole, it comes "
    "from your local health district rather than any building department, and "
    "it constrains where the house can physically sit."))
flow.append(k.bullet(
    "<b>Work OH.2 with a pen.</b> The approvals that apply everywhere deserve "
    "more of your attention than the one that might not apply at all."))
flow.append(k.bullet(
    "<b>Keep OH.3 on the job</b> and record every inspection as it happens — "
    "most of all if nobody is required to inspect you. It is the only evidence "
    "you will have when you sell, refinance or insure."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Ohio claim here was read against its primary source "
                  "in September 2026 — the Ohio Revised Code and the Ohio "
                  "Administrative Code at codes.ohio.gov, and the Board of "
                  "Building Standards' own filed rule text — and is cited "
                  "where it appears. Where the answer genuinely depends on "
                  "your municipality, township or county, the kit says so and "
                  "gives you a line to write down what you confirmed. Not "
                  "legal advice.", S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "oh-permit-kit",
                       "OH.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
