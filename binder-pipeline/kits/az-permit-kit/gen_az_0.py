#!/usr/bin/env python3
"""AZ.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame, centered
title block, aligned project fill-in rules, brand and edition line. Page 2 is
the one-page orientation.

The Arizona cover carries two fields no other kit in the line needs. "IRC / NEC
on the Permit" exists because Arizona adopts no statewide edition of anything:
the edition that binds the house is whatever the local adopting ordinance says,
and the spread in September 2026 runs from the 2003 IRC to the 2024. "Deed
Recorded On" exists because the one thing that switches off the one-year
sale presumption AND blocks every subcontractor lien is being an owner-occupant
under A.R.S. § 33-1002 — a natural person whose deed was recorded BEFORE
construction started. The date on that line has to be earlier than every other
date in the kit.
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

FORM_ID = "AZ.0"
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
    c.drawCentredString(cx, 8.75 * inch, "ARIZONA")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    # Centered on the PAGE, while the audit frame is the mirrored CONTENT box
    # [64.8, 568.8] — so the usable width here is 2*(306-64.8) = 482pt. This
    # line measures ~360pt at 12.5.
    c.drawCentredString(cx, 7.13 * inch,
                        "No statewide code · One statewide permit")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "City / Town (if inside limits):",
              "County:", "Permit Issued By:", "IRC / NEC on the Permit:",
              "Deed Recorded On:", "Owner-Builder:"]
    # "City / Town (if inside limits):" is the widest label here at ~172pt;
    # the gutter sits at 3.45in to stay clear of the 0.9in binding margin.
    # Seven fields at 0.5in pitch run 5.95in → 2.95in.
    label_x = 3.45 * inch
    rule_x0 = 3.6 * inch
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
                        "\"Permit Issued By\" never reads NONE in Arizona — "
                        "a county with no code still issues one.")
    c.drawCentredString(cx, 2.44 * inch,
                        "\"Deed Recorded On\" must be earlier than every "
                        "other date in this kit. AZ.1 explains why.")

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.16 * inch,
                        "Every Arizona statute, rule and requirement in this "
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
    "Five working documents, from \"which rules are actually statewide?\" to "
    "the last inspection tag.",
    S["subtitle"]))

flow.append(k.body(
    "Arizona is sold as the \"no statewide code\" state, and that much is "
    "true: no state agency adopts a residential building code, an energy "
    "code or an edition of the electrical code, and the edition that binds "
    "your house is whatever your city or county wrote into its adopting "
    "ordinance. What the circulating advice gets wrong is the next step. It "
    "turns \"no statewide code\" into \"no permit,\" \"no rules\" and "
    "\"varies locally\" for things that are in fact fixed by statute for "
    "every lot in the state."))
flow.append(k.body(
    "<b>There is a statewide building permit.</b> Every board of supervisors "
    "\"shall require a building permit for any construction of a building … "
    "exceeding a cost of $1,000\" (A.R.S. §&#160;11-321(A)). A \"no-permit "
    "county\" does not exist. A <b>no-code</b> county does — one, Greenlee, "
    "in its own engineer's words — and two counties let a rural owner-builder "
    "opt out of plan review and inspection while keeping the permit. "
    "<b>There is a statewide owner-builder statement</b>, signed on every "
    "permit application, naming every licensed contractor you will use "
    "(§&#160;32-1169); a false one is a crime. <b>There is a statewide "
    "off-switch for the one-year sale rule</b>, and it is the same status "
    "that blocks subcontractor liens: a deed recorded before construction, "
    "and thirty days' residence after (§&#160;33-1002). And <b>the permit "
    "clocks run against city counters only</b> — the county statute carves "
    "every residential-lot permit out."))
flow.append(k.body(
    "Then the two rulebooks that are genuinely statewide and reach every lot, "
    "including the no-code county: ADEQ's septic general permit, with its "
    "100-foot well setback and its 50-foot property-line rule on well-served "
    "lots, and ADWR's well rules — under which an owner may drill their own "
    "exempt well on a no-fee license, after passing an exam."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>AZ.1</b>"), k.cellp("The Code Is Local, the Permit Is Not"),
     k.cellp("The statewide permit and the one no-code county; the two "
             "county opt-outs and what survives them; the exemption quoted "
             "at the words that decide arguments; the deed-and-residence "
             "off-switch; who may lawfully help you; the statement you "
             "sign; workers' compensation honestly. <b>Read this "
             "first.</b>")],
    [k.cellp("<b>AZ.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("The code editions actually in force in 15 counties and 20 "
             "cities, dated, with the confirm-at-the-counter rule for "
             "everything else; what applies on every lot regardless; the "
             "septic and well packages with the numbers that decide where "
             "the house can sit.")],
    [k.cellp("<b>AZ.3</b>"), k.cellp("Inspection Sequence &amp; Clocks"),
     k.cellp("The city/county asymmetry — one request for corrections, a "
             "15-working-day denial notice, an automatic refund and no "
             "mid-build plan changes on a city permit; \"at the earliest "
             "reasonable time\" on a county one — the septic and well "
             "clocks, the certificate of occupancy you may never get, and "
             "a log.")],
    [k.cellp("<b>AZ.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("Every county and the big cities as their own sites describe "
             "them, the Registrar, the ADEQ-delegated septic programs, "
             "ADWR, the two opt-out counters and the no-code county, and a "
             "page to record every office you confirmed.")],
    [k.cellp("<b>AZ.5</b>"), k.cellp("Forms &amp; Documents Index"),
     k.cellp("Each document you will meet, named as the agency names it: "
             "the §&#160;32-1169 statement, the ADEQ Notice of Intent and "
             "its two authorizations, the ADWR notice and the single well "
             "license, the recorded deed — and the 30-day clarification "
             "letter that answers every \"varies locally\" question.")],
]
flow.append(k.ref_table(
    "The five documents",
    [k.cellp("", bold=True), k.cellp("Document", bold=True),
     k.cellp("What it does for you", bold=True)],
    rows, [0.55 * inch, 2.05 * inch, CW - 2.6 * inch]))

flow += k.h2_tight("HOW TO USE IT", reserve=1.5)
flow.append(k.bullet(
    "<b>Record the deed before the first shovel, then start with AZ.1.</b> "
    "The owner-occupant status that protects you is defined by a deed "
    "\"recorded with the county recorder\" <i>prior to commencement of the "
    "construction</i>. Nothing else in this kit can fix that date afterward."))
flow.append(k.bullet(
    "<b>Find your adopting ordinance, not your building department's web "
    "page.</b> The authoritative statement of which code edition binds your "
    "lot is the ordinance on file with the clerk. AZ.2 prints the map with "
    "the date it was read and tells you to ask for the ordinance number."))
flow.append(k.bullet(
    "<b>Then the septic site investigation and the well notice</b> — both "
    "state rules, both administered by offices the building code never "
    "touched, and the septic setbacks constrain where the house can "
    "physically sit."))
flow.append(k.bullet(
    "<b>Know which of your permits has a clock.</b> A city house permit "
    "carries statutory time frames and a refund; a county one carries none. "
    "AZ.3 tells you which you hold and what to do about it."))
flow.append(k.bullet(
    "<b>Keep AZ.3 on the job</b> and record every inspection as it happens — "
    "most of all if you built under an opt-out and no certificate of "
    "occupancy will ever issue. It is the only evidence you will have when "
    "you sell, refinance or insure."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Arizona claim here was read against its primary "
                  "source in September 2026 — the Arizona Revised Statutes "
                  "on the Legislature's own site, the Arizona Administrative "
                  "Code section by section, the Registrar of Contractors' "
                  "pages, ADEQ's own Notice of Intent form, and the adopting "
                  "ordinances and code pages of 15 counties and 20 cities — "
                  "and is cited where it appears. Where the answer genuinely "
                  "depends on your city or county, the kit says so and gives "
                  "you a line to write down what you confirmed. Not legal "
                  "advice.", S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "az-permit-kit",
                       "AZ.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
