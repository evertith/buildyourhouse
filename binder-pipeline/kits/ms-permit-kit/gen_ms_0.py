#!/usr/bin/env python3
"""MS.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame,
centered title block, aligned project fill-in rules, brand and edition line.
Page 2 is the one-page orientation.

The cover carries a "Code status" field the other states' covers do not. In
Mississippi that is the first unknown an owner-builder has to resolve, it is
not answerable from the county name alone, and it was decided by a resolution
entered on a board's minutes in 2006 or 2014 — see MS.1 and MS.4.
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

FORM_ID = "MS.0"
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
    c.drawCentredString(cx, 8.75 * inch, "MISSISSIPPI")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 7.13 * inch,
                        "Claim the exemption · Find out who inspects · "
                        "Build it right")

    # project fields — labels right-aligned to a common gutter
    # Labels are drawn right-aligned to label_x, so the LONGEST one sets how
    # far left the block reaches. "City / Town (or Unincorporated):" measured
    # 193.7pt at 12pt and pushed past the 0.9in binding margin.
    fields = ["Project Address:", "City / Town (if any):",
              "County:", "Code Status (see MS.4):", "Owner-Builder:",
              "Permit Application Date:"]
    label_x = 3.15 * inch
    rule_x0 = 3.3 * inch
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
                        "Every Mississippi statute, threshold, and requirement "
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
    "Mississippi is one of the easiest states in the country to build your "
    "own home in: a broad licensing exemption, no state permit, and across "
    "much of the state no building code enforced on your parcel at all."))
flow.append(k.body(
    "That last point is the one that trips people up. Whether a code binds "
    "your land was not decided by your county's population or how rural it "
    "looks. <b>It was decided by a resolution entered on a board's minutes — "
    "in 2006 for the coast, in 2014 for everyone else — and both windows are "
    "long closed.</b> You cannot change that answer, only find out what it "
    "is. MS.4 shows you how."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>MS.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("Whether you qualify, the one-per-year rule that is stricter "
             "than it looks, and the zero-dollar rule for everyone you hire. "
             "<b>Read this first.</b>")],
    [k.cellp("<b>MS.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather before you file — and what still applies when "
             "there is no building permit to file at all.")],
    [k.cellp("<b>MS.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The order inspections happen in, what each one checks, and "
             "what to do about it if nobody is coming.")],
    [k.cellp("<b>MS.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("How to establish whether <i>any</i> code binds your parcel, "
             "who to ask, and a page to write down what you confirmed.")],
    [k.cellp("<b>MS.5</b>"), k.cellp("Forms &amp; Documents Index"),
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
    "<b>Start with MS.1.</b> The exemption is yours and it is strong — but "
    "it runs on a rolling twelve months, not a calendar year, and it covers "
    "nobody you hire."))
flow.append(k.bullet(
    "<b>Then do MS.4 — before anything else practical.</b> Elsewhere the "
    "directory is a convenience; in Mississippi it settles whether you have "
    "a permit process at all."))
flow.append(k.bullet(
    "<b>Work MS.2 with a pen.</b> The approvals that are not building permits "
    "— septic, flood, driveway, power — apply in far more of Mississippi than "
    "the building code does."))
flow.append(k.bullet(
    "<b>Keep MS.3 on the job.</b> If no inspector is coming, it tells you "
    "what to buy instead."))

# A bordered callout here needed ~1.3in and KeepTogether pushed it onto a
# third, otherwise-empty page. The same assurance is stamped on the cover and
# repeated in each document's disclaimer, so it runs as a source line instead.
flow.append(k.cite(
    "<b>How these facts were checked.</b> Every Mississippi claim in this kit "
    "was read against its primary source in August 2026 — the Mississippi "
    "Code, the enacted bills as passed by the Legislature, and the State "
    "Board of Contractors' own published law and rules — and is cited on the "
    "page where it appears. Where the answer depends on your county, the kit "
    "says so and tells you how to find out. This is a process reference, not "
    "legal advice."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ms-permit-kit",
                       "MS.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
