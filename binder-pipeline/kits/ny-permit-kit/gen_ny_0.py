#!/usr/bin/env python3
"""NY.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame, centered
title block, aligned project fill-in rules, brand and edition line. Pages 2–3
are the orientation.

The New York cover carries a field no other kit in the line has: "Permit
Office (Town / County / DOS)". Executive Law § 381(2) sends enforcement down a
three-rung ladder — the town, village or city; then the county; then the
Department of State — and which rung issues the buyer's permit is the first
thing to establish, because the application form, the fee schedule and the
inspector all come from that office. The code itself is the same on every
rung, which is the thing that makes New York unlike Tennessee or Pennsylvania.

The cover also says the New York City carve-out once, in one line, and never
again: Executive Law § 383(1)(c) keeps the five boroughs on their own code.
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

FORM_ID = "NY.0"
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
    c.drawCentredString(cx, 8.75 * inch, "NEW YORK")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    # Centered on the PAGE, while the audit frame is the mirrored CONTENT box
    # [64.8, 568.8] — so the usable width here is 2*(306-64.8) = 482pt, not the
    # 504pt content width. This line measures ~455pt at 12.5.
    c.drawCentredString(cx, 7.13 * inch,
                        "Find your permit office · File the CE-200 · "
                        "Build to the 2025 Uniform Code")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "City / Town / Village:", "County:",
              "Permit Office (Tier):", "Owner-Builder:",
              "Permit Application Date:"]
    # "Permit Application Date:" is the widest label here at 155pt; the gutter
    # sits at 3.28in to stay clear of the 0.9in binding margin, matching the
    # rest of the kit line.
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

    # Three short lines, not one long one: each must clear the 482pt usable
    # width at 9.5pt, which is roughly 105 characters.
    c.setFont(d.BODY, 9.5)
    c.setFillColor(d.FURNITURE_GREY)
    # The first line originally read "New York State outside New York City —
    # …" and measured 496pt at 9.5, clipping the left margin by 7pt; check.py
    # caught it. Trimmed to ~90 characters.
    c.drawCentredString(cx, 2.90 * inch,
                        "Outside New York City only — the five boroughs keep "
                        "their own code (Exec. Law § 383(1)(c)).")
    c.drawCentredString(cx, 2.72 * inch,
                        "Your permit office is your town, village or city; "
                        "your county; or the Department of State.")
    c.drawCentredString(cx, 2.54 * inch,
                        "The code is the same on all three — NY.1 shows you "
                        "how to tell which one is yours.")

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.28 * inch,
                        "Every New York statute, rule and requirement in this "
                        "kit")
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
    "Five working documents, from “which government issues my permit?” "
    "to the certificate of occupancy.",
    S["subtitle"]))

flow.append(k.body(
    "New York has <b>one</b> Uniform Fire Prevention and Building Code and "
    "<b>one</b> Energy Code, in force on every parcel in the state outside "
    "New York City: no county where the code does not apply, no opt-out that "
    "switches it off, no acreage below which it stops. The five boroughs "
    f"keep their own code under Executive Law {k.sec('383(1)(c)')}, and "
    "nothing in this kit is about them."))
flow.append(k.body(
    "What New York does instead is hand the <i>enforcement</i> of that code "
    "down a ladder. Executive Law " + k.sec("381(2)") + " makes your town, "
    "village or city the permit office by default; a local government that "
    "declines the job passes it to the county; a county that declines passes "
    "it to the Department of State. <b>Same code on every rung. Different "
    "office, different fee, different local law, different inspector.</b> "
    "The first thing to establish is which rung you are on."))
flow.append(k.body(
    "Then three things catch almost everybody, and none is in the code book. "
    "<b>The permit is gated by a workers' compensation form</b> (General "
    "Municipal Law " + k.sec("125") + ") — for an owner-builder, a "
    "job-specific Form CE-200 filed as a homeowner. <b>The electrical "
    "inspector is whoever your office has approved</b> (19 NYCRR "
    + k.sec("1203.2(e)(4)") + "). And <b>the gas question has a court-set "
    "clock</b> that, on the day this kit was assembled, runs out on "
    "31&#160;December 2026."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>NY.1</b>"), k.cellp("Who Enforces Your House"),
     k.cellp("The three-rung ladder and how to find your rung; why there is "
             "no owner-builder exemption to claim; the CE-200 permit gate; "
             "the 2025 code editions; and the dated all-electric status box. "
             "<b>Read this first.</b>")],
    [k.cellp("<b>NY.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What the state rule entitles the reviewer to demand, the "
             "1,500&#160;sq&#160;ft stamped-plan rule, the numbers your office "
             "writes into Table R301.2, New York's own energy values, and the "
             "septic and well rules that fix where the house can sit.")],
    [k.cellp("<b>NY.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The eleven inspection elements the state rule requires, the "
             "electrical special-inspection track, the 30-day order-to-remedy "
             "clock, the appeal you do have, and the certificate of "
             "occupancy — with a log for every visit.")],
    [k.cellp("<b>NY.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("How to identify your permit office on the ladder, the county "
             "health department for septic and wells, the two regional "
             "overlays that reach one house, the county license laws, and a "
             "page to record every office you confirmed.")],
    [k.cellp("<b>NY.5</b>"), k.cellp("Forms &amp; Documents Index"),
     k.cellp("Each document you will meet, named as the agency names it — "
             "plus what may need no permit, what New York never asks for, "
             "and the two things you may not do yourself.")],
]
flow.append(k.ref_table(
    "The five documents",
    [k.cellp("", bold=True), k.cellp("Document", bold=True),
     k.cellp("What it does for you", bold=True)],
    rows, [0.55 * inch, 2.05 * inch, CW - 2.6 * inch]))

# design.h2 reserves 2.4in. The document table above ends roughly 2in from the
# foot of page 2, so the full reserve threw the whole heading to page 3 and
# left page 2 with a third of itself blank. 1.5in keeps the heading with its
# first two bullets, which balances the two pages.
flow += k.h2_tight("HOW TO USE IT", reserve=1.5)
flow.append(k.bullet(
    "<b>Start with NY.1.</b> Its first section settles which government "
    "issues your permit. Nothing else in the kit sequences correctly until "
    "you know that, and the answer is a clerk's question away — you do not "
    "have to guess at it."))
flow.append(k.bullet(
    "<b>Get the CE-200 before you walk in.</b> No city, town or village may "
    "issue a building permit without carrier proof of workers' compensation "
    "coverage or an affidavit that you have engaged no employees. The "
    "affidavit is Form CE-200, applied for online as a homeowner, and it is "
    "job-specific — one per permit."))
flow.append(k.bullet(
    "<b>Ask for the approved electrical inspection agency list before you "
    "buy wire.</b> Your office may accept an electrical inspection only from "
    "an agency it has approved, and there is no state list. The name goes on "
    "the statement of special inspections in your application."))
flow.append(k.bullet(
    "<b>If you are planning gas or propane, read the dated box in NY.1 "
    "before you file.</b> The trigger is the date a substantially complete "
    "application is submitted, not the date you occupy. A complete "
    "application in before the suspension lifts is outside the prohibition."))
flow.append(k.bullet(
    "<b>Keep NY.3 on the job</b> and record every inspection as it happens. "
    "The certificate of occupancy cannot issue until the office holds the "
    "electrical agency's final report and the written blower-door result, "
    "and those two documents come from people you hired, not from the "
    "office."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every New York claim here was read against its primary "
                  "source in September 2026 — the Executive Law and the other "
                  "consolidated laws, the Department of State's own rule-text "
                  "PDFs for 19 NYCRR, the 2025 Residential and Energy Codes "
                  "in the ICC's free viewer, the Health Department's "
                  "Appendices 75-A and 5-B, the Workers' Compensation Board's "
                  "own forms guidance, and the federal court docket that "
                  "governs the all-electric date — and is cited where it "
                  "appears. Where the answer genuinely depends on your "
                  "municipality, the kit says so and gives you a line to "
                  "write down what you confirmed. Not legal advice.",
                  S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ny-permit-kit",
                       "NY.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
