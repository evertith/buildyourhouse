#!/usr/bin/env python3
"""ID.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame, centered
title block, aligned project fill-in rules, brand and edition line. Page 2 is
the one-page orientation.

The Idaho cover carries two fields no eastern kit in the line needs: "Building
Permit From" and "Trade Permits From", written as two separate answers. In
Idaho they routinely have two different answers — a county with no building
department at all, and DOPL for the electrical, plumbing and HVAC permits — and
the thesis of the whole kit is that the second answer never depends on the
first. A "Health District No." line follows, because Idaho routes every septic
permit through one of seven districts fixed by statute, and the number is the
first thing that office will ask.
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

FORM_ID = "ID.0"
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
    c.drawCentredString(cx, 8.75 * inch, "IDAHO")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    # Centered on the PAGE, while the audit frame is the mirrored CONTENT box
    # [64.8, 568.8] — so the usable width here is 2*(306-64.8) = 482pt. This
    # line measures ~380pt at 12.5.
    c.drawCentredString(cx, 7.13 * inch,
                        "The building permit is optional · "
                        "The trade permits are not")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "City / Town:", "County:",
              "Building Permit From:", "Trade Permits From:",
              "Health District No.:", "Owner-Builder:"]
    # "Building Permit From:" is the widest label here at ~140pt; the gutter
    # sits at 3.28in to stay clear of the 0.9in binding margin, matching the
    # rest of the kit line. Seven fields at 0.5in pitch run 5.95in → 2.95in.
    label_x = 3.28 * inch
    rule_x0 = 3.43 * inch
    rule_x1 = PAGE_W - 1.35 * inch
    y = 5.95 * inch
    c.setFillColor(d.INK)
    for label in fields:
        c.setFont(d.BODY, 12)
        c.drawRightString(label_x, y, label)
        c.setLineWidth(0.75)
        c.line(rule_x0, y - 2, rule_x1, y - 2)
        y -= 0.5 * inch

    c.setFont(d.BODY, 9.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.62 * inch,
                        "\"Building Permit From\" may honestly read NONE. "
                        "\"Trade Permits From\" never does.")
    c.drawCentredString(cx, 2.44 * inch,
                        "Write DOPL, or the city or county that runs its own "
                        "program — ID.1 shows you how to tell.")

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.16 * inch,
                        "Every Idaho statute, rule and requirement in this "
                        "kit")
    c.drawCentredString(cx, 1.94 * inch,
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
    "Five working documents, from \"does anyone permit my house?\" to the "
    "last inspection tag.",
    S["subtitle"]))

flow.append(k.body(
    "Idaho's Building Code Act does not impose a building permit on a private "
    "house. It <b>authorizes</b> each city and county to adopt and enforce a "
    "building code, and the state Division of Occupational and Professional "
    "Licenses (DOPL) enforces the Act only for the buildings the Act puts "
    "under the state — state-owned buildings, public schools, modular and "
    "manufactured units. Where your county or city has adopted no ordinance, "
    "there is <b>no residential building permit, no plan review, no building "
    "inspection and no certificate of occupancy.</b> DOPL's own plan-review "
    "form says it in one line: \"DOPL does NOT issue building permits for "
    "projects not owned by the State.\""))
flow.append(k.body(
    "That is the half everybody knows. The other half is the reason this kit "
    "exists. <b>Three permits survive that gap, and each one is statewide:</b> "
    "an electrical permit, a plumbing permit and an HVAC permit — from DOPL "
    "wherever no city or county runs its own program — plus the "
    "health-district septic permit and the IDWR well drilling permit, which "
    "never depended on the building code at all. The electrical permit is "
    "enforced at the meter: by statute your power supplier, rural co-op "
    "included, may not energize the house until a state inspection has "
    "passed."))
flow.append(k.body(
    "And one trap that catches owner-builders specifically: the rule that "
    "lets a utility energize <b>temporary construction power</b> ahead of an "
    "inspection is written for a licensed electrical contractor's permit "
    "only. A homeowner permit does not open that door."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>ID.1</b>"), k.cellp("The Building Permit Is Optional, the "
                                     "Trade Permits Are Not"),
     k.cellp("Who, if anyone, enforces a building code on your parcel and "
             "how to tell; the three permits that apply regardless; the "
             "three owner exemptions with their three different tests; the "
             "temporary-power trap. <b>Read this first.</b>")],
    [k.cellp("<b>ID.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("The code editions actually in force — and the 2024 update the "
             "Legislature rejected — the NEC amended downward, the energy "
             "table Idaho wrote itself, the trade fees as the rules set "
             "them, and the septic and well packages.")],
    [k.cellp("<b>ID.3</b>"), k.cellp("Inspection Sequence &amp; Clocks"),
     k.cellp("The 10-business-day completeness clock, the 48-business-hour "
             "inspection rule with its self-help remedy on all four tracks, "
             "the trade inspection ladders the rules fix, and a log.")],
    [k.cellp("<b>ID.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("How to tell an enforcing jurisdiction from one that is not, "
             "DOPL and its inspector list, the seven health districts by "
             "county, IDWR, two cities that run their own trade programs, "
             "and a page to record every office you confirmed.")],
    [k.cellp("<b>ID.5</b>"), k.cellp("Forms &amp; Documents Index"),
     k.cellp("Each document you will meet, named as the agency names it: "
             "the three DOPL homeowner permit applications and what you "
             "certify on them, the septic and well permits — and what Idaho "
             "never asks you for.")],
]
flow.append(k.ref_table(
    "The five documents",
    [k.cellp("", bold=True), k.cellp("Document", bold=True),
     k.cellp("What it does for you", bold=True)],
    rows, [0.55 * inch, 2.05 * inch, CW - 2.6 * inch]))

flow += k.h2_tight("HOW TO USE IT", reserve=1.5)
flow.append(k.bullet(
    "<b>Start with ID.1.</b> Its first section settles whether any building "
    "code is enforced on your parcel. Nothing else sequences correctly until "
    "you know that — and unlike most states, Idaho publishes no list, so the "
    "kit gives you the verification step the statute itself created."))
flow.append(k.bullet(
    "<b>Buy the three trade permits regardless.</b> Electrical, plumbing and "
    "HVAC permits rest on three separate chapters of Title 54, none of which "
    "cares whether your county adopted a building code. A homeowner doing "
    "his own work still buys them. The electrical one is the one your "
    "utility will check."))
flow.append(k.bullet(
    "<b>Then deal with the septic system and the well.</b> Both are permitted "
    "by agencies the building code never touched — the health district and "
    "IDWR — and the septic separation distances constrain where the house "
    "can physically sit."))
flow.append(k.bullet(
    "<b>Keep ID.3 on the job</b> and record every inspection tag as it goes "
    "on — most of all if nobody is required to inspect the building itself. "
    "It is the only evidence you will have when you sell, refinance or "
    "insure."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Idaho claim here was read against its primary "
                  "source in September 2026 — the Idaho Code on the "
                  "Legislature's own site, the IDAPA rule chapters at "
                  "adminrules.idaho.gov, DOPL's own forms and program pages, "
                  "and the House Business Committee's minutes — and is cited "
                  "where it appears. Where the answer genuinely depends on "
                  "your city or county, the kit says so and gives you a line "
                  "to write down what you confirmed. Not legal advice.",
                  S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "id-permit-kit",
                       "ID.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
