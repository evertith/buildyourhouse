#!/usr/bin/env python3
"""NE.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame, centered
title block, aligned project fill-in rules, brand and edition line. Page 2 is
the one-page orientation.

The Nebraska cover carries two fields no other kit in the line pairs together:
"Building Permit Office" and "Electrical Inspection". The first may honestly be
NONE — Nebraska requires no county, city or village to issue a building permit,
and no state agency may inspect a private house. The second is never none: a
new house is inspected for electrical everywhere in the state, either by a
local program or by the State Electrical Division, and the power company may
not connect it until the owner certifies that the inspection was requested.
Those two answers are the first thing to establish and the thing every later
document branches on.
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

FORM_ID = "NE.0"
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
    c.drawCentredString(cx, 8.75 * inch, "NEBRASKA")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    # Centered on the PAGE, while the audit frame is the mirrored CONTENT box
    # [64.8, 568.8] — so the usable width here is 2*(306-64.8) = 482pt, not the
    # 504pt content width. This line measures well under that at 12.5.
    c.drawCentredString(cx, 7.13 * inch,
                        "One code everywhere · A permit almost nowhere · "
                        "An inspector at the meter")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "City / Village:", "County:",
              "Building Permit Office:", "Electrical Inspection:",
              "Owner-Builder:"]
    # "Building Permit Office:" is the widest label here; the gutter sits at
    # 3.28in to stay clear of the 0.9in binding margin, matching the rest of
    # the kit line.
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

    # Two lines, not one: a single line here would exceed the 482pt usable
    # width and clip both margins.
    c.setFont(d.BODY, 9.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.72 * inch,
                        "Building permit office may honestly be NONE. "
                        "Electrical inspection never is:")
    c.drawCentredString(cx, 2.54 * inch,
                        "write STATE or the name of the local program — "
                        "NE.4 shows you how to look it up.")

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.28 * inch,
                        "Every Nebraska statute, rule and requirement in this "
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
    "Five working documents, from \"what binds my house and who can stop me?\" "
    "to the last inspection.",
    S["subtitle"]))

flow.append(k.body(
    "Nebraska has <b>one</b> state building code — the 2018 International "
    "Residential Code and the 2018 Uniform Plumbing Code, adopted by statute — "
    "and the statute then says something almost no other state says: that code "
    "is \"the legally applicable code <b>regardless of whether</b> the county, "
    "city, or village has provided for the administration or enforcement\" of "
    "it. The code binds your house everywhere. <b>Nobody has to issue a permit "
    "or inspect it</b>, and no state agency may."))
flow.append(k.body(
    "So the question most kits in this series spend a document on — <i>does "
    "the code apply to me?</i> — has a one-word answer here, and the question "
    "that actually decides your build is a different one: <b>who, if anyone, "
    "can stop you?</b> Outside the cities and counties that chose to run a "
    "building department, the answer is three offices that do not depend on "
    "one: the <b>State Electrical Division</b>, whose inspection is enforced "
    "by the power company at the meter; the <b>energy code</b>, which the "
    "statute makes you enforce on yourself; and the <b>septic and well "
    "filings</b>, made by the licensed professional or by you."))
flow.append(k.body(
    "Two things about that arrangement catch almost everybody. Your right to "
    "wire your own house is a <b>license</b> exemption, not an inspection "
    "exemption — and since <b>July 18, 2026</b>, failing to file the request "
    "for that inspection is a <b>felony</b>. And you may drill your own well "
    "on your own homestead, but you may <b>not</b> install your own septic "
    "system: a certified installer must be physically on the site."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>NE.1</b>"), k.cellp("What Binds You and Who Can Stop You"),
     k.cellp("The sentence that makes the code apply without a building "
             "department, the four state obligations that reach every house, "
             "what you may do with your own hands, and the registration act "
             "that governs everyone you hire. <b>Read this first.</b>")],
    [k.cellp("<b>NE.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather before you file — the code editions actually in "
             "force, the five electrical sections still on the 2017 text, the "
             "energy values, the radon rule and its two exemptions, the septic "
             "and well packages with their setbacks and fees.")],
    [k.cellp("<b>NE.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The one inspection track the statute fixes — electrical, with "
             "its one-week clock and five-month permit life — the two "
             "mandatory registrations, the 2026 rule on virtual inspections, "
             "and what to do where nobody is required to inspect you.")],
    [k.cellp("<b>NE.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("The state map that tells you who inspects electrical at your "
             "address, the three-step check for whether a building permit "
             "exists, the state offices, Lincoln and Sarpy County worked, and "
             "a page to record what you confirmed.")],
    [k.cellp("<b>NE.5</b>"), k.cellp("Forms &amp; Documents Index"),
     k.cellp("Each document you will meet, named as the agency names it — "
             "plus the paper Nebraska never asks you for, and the one thing "
             "you may not do yourself.")],
]
flow.append(k.ref_table(
    "The five documents",
    [k.cellp("", bold=True), k.cellp("Document", bold=True),
     k.cellp("What it does for you", bold=True)],
    rows, [0.55 * inch, 2.05 * inch, CW - 2.6 * inch]))

# design.h2 reserves 2.4in. The document table above ends roughly 2.4in from
# the foot of page 2, so the full reserve would throw the whole heading to page
# 3 and leave page 2 with a third of itself blank. 1.5in keeps the heading with
# its first two bullets, which balances the two pages.
flow += k.h2_tight("HOW TO USE IT", reserve=1.5)
flow.append(k.bullet(
    "<b>Start with NE.1.</b> Its first pages settle what the code requires of "
    "you whether or not anyone checks, and which of the four statewide "
    "obligations will actually reach your parcel. Nothing else in the kit "
    "sequences correctly until you have that straight."))
flow.append(k.bullet(
    "<b>File the electrical request for inspection before you start "
    "wiring.</b> This is the single most expensive mistake in Nebraska. The "
    "request is due \"at or before commencement,\" a late one costs $250, the "
    "utility may refuse to connect you without your certificate that it was "
    "filed, and not filing at all is now a Class IV felony. None of that "
    "depends on whether your county has a building department."))
flow.append(k.bullet(
    "<b>Then deal with the septic system.</b> On a rural Nebraska build the "
    "septic professional is the longest pole — you cannot install the system "
    "yourself — and the setback table decides where the house can sit."))
flow.append(k.bullet(
    "<b>Keep NE.3 on the job</b> and record every inspection and filing as it "
    "happens — most of all where nobody is required to inspect you. The "
    "electrical approval and the septic and well registrations may be the "
    "only third-party evidence your house ever gets, and a buyer's lender will "
    "ask for it."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Nebraska claim here was read against its primary "
                  "source in September 2026 — the Revised Statutes as the "
                  "Legislature publishes them, the 2026 slip laws, the "
                  "agencies' own rule titles and forms, and the State "
                  "Electrical Division's inspection map — and is cited where "
                  "it appears. Where the answer genuinely depends on your "
                  "city or county, the kit says so and gives you a line to "
                  "write down what you confirmed. Not legal advice.",
                  S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ne-permit-kit",
                       "NE.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
