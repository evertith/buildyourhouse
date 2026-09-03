#!/usr/bin/env python3
"""TN.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame, centered
title block, aligned project fill-in rules, brand and edition line. Page 2 is
the one-page orientation.

The Tennessee cover carries a field no other kit in the line has: "Jurisdiction
Status (EXEMPT / SRBP / OPT OUT)". Those are the State Fire Marshal's own three
labels, and which one applies to the buyer's parcel decides whether there is a
building permit at all. It goes on the cover because it is the first thing to
establish and the thing every later document branches on.

The cover also asks for the CITY separately from the COUNTY and says why. A
county's status governs only its unincorporated area — that limitation is on the
face of the statute — so a city inside an opted-out county routinely carries a
different status from the county around it.
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

FORM_ID = "TN.0"
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
    c.drawCentredString(cx, 8.75 * inch, "TENNESSEE")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    # Centered on the PAGE, while the audit frame is the mirrored CONTENT box
    # [64.8, 568.8] — so the usable width here is 2*(306-64.8) = 482pt, not the
    # 504pt content width. This line measures 462pt at 12.5.
    c.drawCentredString(cx, 7.13 * inch,
                        "Find your status · File what applies either way · "
                        "Build to the 2018 IRC")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "City / Town:", "County:",
              "Jurisdiction Status:", "Owner-Builder:",
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

    # Two lines, not one: the single-line version measured 534pt against the
    # 482pt usable width and clipped both margins.
    c.setFont(d.BODY, 9.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.72 * inch,
                        "Jurisdiction status is EXEMPT, SRBP or OPT OUT.")
    c.drawCentredString(cx, 2.54 * inch,
                        "Look up your CITY first, then the county — TN.1 shows "
                        "you how.")

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.28 * inch,
                        "Every Tennessee statute, rule and requirement in this "
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
    "Five working documents, from \"which of three regimes am I in?\" to the "
    "last inspection.",
    S["subtitle"]))

flow.append(k.body(
    "Tennessee has <b>one</b> state residential building code and <b>three</b> "
    "different answers to who enforces it. The State Fire Marshal's Office "
    "publishes the answer for every jurisdiction in the state, and tags each "
    "one with a label: <b>EXEMPT</b>, <b>SRBP</b>, or <b>OPT OUT</b>."))
flow.append(k.body(
    "<b>EXEMPT</b> means the local government runs its own building department "
    "and enforces its own adopted code. <b>SRBP</b> means the State Residential "
    "Building Program applies — you buy a state permit and state contract "
    "inspectors come out. <b>OPT OUT</b> means the jurisdiction passed a "
    "resolution and <i>no residential building code is enforced there at "
    "all</i>. Fifty counties are EXEMPT, eight are SRBP, and thirty-seven have "
    "opted out."))
flow.append(k.body(
    "Two things about that map catch almost everybody. <b>The unit is the "
    "jurisdiction, not the county</b> — a county's resolution reaches only its "
    "unincorporated area, so a city inside an opted-out county frequently has "
    "its own building department. And <b>an opt-out is not permanent</b>: it "
    "expires 180&#160;days after that legislative body's next election unless "
    "the new body passes it again."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>TN.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("How to find your jurisdiction's status in about five minutes, "
             "the licensing exemption for building your own home, and what you "
             "may do yourself trade by trade. <b>Read this first.</b>")],
    [k.cellp("<b>TN.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather before you file — the code editions actually in "
             "force, the state fee schedule and how your fee is computed, and "
             "the approvals that apply no matter which regime you are in.")],
    [k.cellp("<b>TN.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The inspections the state rule requires, in the order the rule "
             "fixes them, the separate electrical track that runs alongside "
             "them, and fields for dates and results.")],
    [k.cellp("<b>TN.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("Which office handles your parcel under each of the three "
             "statuses, the offices that exist regardless, and a page to "
             "record every one you confirmed.")],
    [k.cellp("<b>TN.5</b>"), k.cellp("Forms &amp; Documents Index"),
     k.cellp("Each document you will meet: what it is, when, and from "
             "where — plus what needs no permit at all.")],
]
flow.append(k.ref_table(
    "The five documents",
    [k.cellp("", bold=True), k.cellp("Document", bold=True),
     k.cellp("What it does for you", bold=True)],
    rows, [0.55 * inch, 2.05 * inch, CW - 2.6 * inch]))

# design.h2 reserves 2.4in. The document table above ends roughly 2.4in from
# the foot of page 2, so the full reserve threw the whole heading to page 3 and
# left page 2 with a third of itself blank and page 3 half empty. 1.5in keeps
# the heading with its first two bullets, which balances the two pages.
flow += k.h2_tight("HOW TO USE IT", reserve=1.5)
flow.append(k.bullet(
    "<b>Start with TN.1.</b> Its first section settles which of the three "
    "statuses governs your parcel. Nothing else in the kit sequences correctly "
    "until you know that answer, and the answer is published — you do not have "
    "to guess at it."))
flow.append(k.bullet(
    "<b>Buy the electrical permit regardless.</b> This is the single most "
    "expensive mistake in Tennessee. The state electrical program rests on a "
    "different chapter of the code from the building program, and opting out "
    "of the building code does not touch it. Every one of the thirty-seven "
    "opt-out counties is still inside the State Electrical Program."))
flow.append(k.bullet(
    "<b>Then deal with the septic system.</b> On a rural Tennessee build the "
    "subsurface sewage disposal permit is the longest pole, and the state "
    "building permit rule will ask you to certify you have it."))
flow.append(k.bullet(
    "<b>Keep TN.3 on the job</b> and record every inspection as it happens — "
    "most of all if you are in an opt-out county where nobody is required to "
    "inspect you. It is the only evidence you will have when you sell, "
    "refinance or insure."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Tennessee claim here was read against its primary "
                  "source in September 2026 — the Secretary of State's "
                  "official rule chapters, the Tennessee Code, and the State "
                  "Fire Marshal's own published program pages — and is cited "
                  "where it appears. Where the answer genuinely depends on "
                  "your city or county, the kit says so and gives you a line "
                  "to write down what you confirmed. Not legal advice.",
                  S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "tn-permit-kit",
                       "TN.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
