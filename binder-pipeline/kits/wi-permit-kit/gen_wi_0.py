#!/usr/bin/env python3
"""WI.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame, centered
title block, aligned project fill-in rules, brand and edition line. Pages 2-3 are
the orientation.

The Wisconsin cover carries an "Enforcing Authority" field rather than the
"Local Building Department" line the Kentucky cover uses, because in Wisconsin
the answer is never NONE. Under Wis. Stat. s. 101.651(3)(b) the department
itself is the residual enforcer, and in a department-jurisdiction municipality
the permit comes from a private registered UDC inspection agency
(s. SPS 320.08(1)) — so the field has an answer everywhere, but it is one of
four different kinds of answer and the owner has to go find out which.
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

FORM_ID = "WI.0"
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
    c.drawCentredString(cx, 8.75 * inch, "WISCONSIN")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 7.13 * inch,
                        "Septic first · Then the permit · Then eight kinds "
                        "of inspection")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "Town / Village / City:", "County:",
              "Who Enforces the UDC:", "Owner-Builder:",
              "Sanitary Permit Date:"]
    # "Who Enforces the UDC:" is the widest label at 12pt, 144pt wide. The
    # gutter sits at 3.22in, which leaves it starting at 88pt — clear of the
    # 0.9in (65pt) binding margin. The longer "…UDC Here:" measured 173pt and
    # clipped.
    label_x = 3.22 * inch
    rule_x0 = 3.37 * inch
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
                        "Your town, your county, or a private state-registered "
                        "agency. Read WI.1 before you guess.")

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.28 * inch,
                        "Every Wisconsin statute, threshold, and requirement "
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
    "Five working documents, from “who is going to inspect this?” to the "
    "final inspection that lets you move in.",
    S["subtitle"]))

flow.append(k.body(
    "Wisconsin is the opposite of the states where owner-builders usually get "
    "into trouble. There is <b>no gap</b> here. One code — the Uniform "
    "Dwelling Code — binds every new one- and two-family dwelling in the "
    "state, and if your town has not taken up enforcement, the statute hands "
    "the job to the department rather than leaving it undone. You will get a "
    "permit and you will get inspections. The only open question is <i>who "
    "does them</i>, and there are exactly four possible answers."))
flow.append(k.body(
    "What catches people out in Wisconsin is not the building permit. It is "
    "the <b>order</b>. On an unsewered parcel the county sanitary permit has "
    "to be in hand before the municipality may lawfully issue your building "
    "permit — that is a statute, not a local habit — and the septic side is "
    "the one part of the job a Wisconsin homeowner is <b>not allowed to do "
    "themselves</b>. So the first phone call on a rural Wisconsin build is not "
    "to the building inspector. It is to the county."))
flow.append(k.body(
    "The second thing that catches people out is that the trades are four "
    "different rules with four different tests, and two of them are worded in "
    "a way that does not obviously reach a house nobody lives in yet. This kit "
    "prints all four side by side, in the legislature's own words, and tells "
    "you which question to put to your inspector before you pick up a tool."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>WI.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("The one-sentence exemption that lets you pull your own permit, "
             "and then the four trades — which are four separate rules. "
             "<b>Read this first.</b>")],
    [k.cellp("<b>WI.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to gather, in the order Wisconsin makes you gather it: "
             "sanitary permit, then plans and site plan, then the uniform "
             "permit. Plus every code edition in force — including the "
             "electrical code that changed this month.")],
    [k.cellp("<b>WI.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("Every inspection the code names, the three clocks that let you "
             "keep working when the inspector does not show, and a log.")],
    [k.cellp("<b>WI.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("How to find which of the four enforcement models covers your "
             "parcel, plus the county offices, the shoreland rules, and a "
             "page to write down every office you confirmed.")],
    [k.cellp("<b>WI.5</b>"), k.cellp("Forms &amp; Documents Index"),
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
    "<b>Start with WI.1.</b> Its first section tells you which of the four "
    "enforcement models covers your parcel, and its second tells you what you "
    "may do with your own hands. Nothing else sequences correctly until you "
    "know both."))
flow.append(k.bullet(
    "<b>If you are not on a sewer, call the county next.</b> The soil "
    "evaluation and the sanitary permit are the longest pole on a rural "
    "Wisconsin build, and by statute the building permit cannot issue until "
    "they are done."))
flow.append(k.bullet(
    "<b>Work WI.2 with a pen.</b> Wisconsin's plan submittal is short and its "
    "site plan requirements are specific — and the state forbids your "
    "municipality from making you have the plans stamped by an architect or "
    "engineer on an ordinary house."))
flow.append(k.bullet(
    "<b>Keep WI.3 on the job.</b> Two of its numbers are worth money: after "
    "you call for an inspection you may keep building at the end of the "
    "second business day, and you may occupy at the end of the fifth."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Wisconsin claim here was read against its primary "
                  "source in September 2026 — the Statutes and the "
                  "Administrative Code at docs.legis.wisconsin.gov, and the "
                  "Department of Safety and Professional Services' own pages "
                  "— and is cited where it appears. Where the answer genuinely "
                  "depends on your municipality's ordinance, the kit says so "
                  "and gives you a line to write what you confirmed. Not legal "
                  "advice.", S["body"]),
    ]))

flow += k.h2_tight("THE FOUR ANSWERS TO “WHO INSPECTS MY HOUSE?”")
flow.append(k.body(
    "Every parcel in Wisconsin falls under one of these. Find yours before you "
    "do anything else; WI.4 shows you how."))
rows = [
    [k.cellp("<b>1.</b>"), k.cellp("Your city, village or town enforces, with "
                                   "its own certified inspectors"),
     k.cellp("The common case in cities and larger villages. You file at the "
             "municipal building department")],
    [k.cellp("<b>2.</b>"), k.cellp("Your municipality enforces, but contracts "
                                   "the inspections out"),
     k.cellp("Very common in smaller municipalities. You still file with the "
             "municipality; a private agency or a shared inspector does the "
             "visits")],
    [k.cellp("<b>3.</b>"), k.cellp("Your town asked the county to do it"),
     k.cellp("Available to a town, village or city of 2,500 or fewer people "
             "that passed a resolution. The county enforces")],
    [k.cellp("<b>4.</b>"), k.cellp("Nobody local took it up, so the state has "
                                   "jurisdiction"),
     k.cellp("You buy the permit from a <b>private registered UDC inspection "
             "agency</b> — and you are then locked to that same agency for "
             "every inspection on the job")],
]
flow.append(k.ref_table(
    "Four enforcement models, and only four",
    [k.cellp("", bold=True), k.cellp("Model", bold=True),
     k.cellp("What it means for you", bold=True)],
    rows, [0.4 * inch, 2.3 * inch, CW - 2.7 * inch]))
flow.append(k.cite(
    "Models 1 and 2 are the four enforcement methods a municipality must "
    "declare to the department under s. SPS 320.06(1)(b)1. to 4. Model 3 is "
    "Wis. Stat. s. 101.651(2m)(a) and (3)(a). Model 4 is s. 101.651(3)(b), "
    "under which the department “shall provide inspection services and "
    "shall enforce this subchapter throughout” the municipality, with the "
    "permit obtained from a registered UDC inspection agency under s. SPS "
    "320.08(1) and the same agency retained for inspections under s. SPS "
    "320.08(2). Larger municipalities that do not inspect are covered by "
    "s. 101.65(2), which requires them to contract with the department for "
    "the services they do not perform."))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "The sentence that reorders a rural Wisconsin build", [
        Paragraph("“<i>No county, city, town or village may issue a "
                  "building permit for construction of any structure requiring "
                  "connection to a private on-site wastewater treatment system "
                  "unless a private on-site wastewater treatment system "
                  "satisfying all applicable regulations already exists to "
                  "serve the proposed structure <b>or all permits necessary to "
                  "install a private on-site wastewater treatment system have "
                  "been obtained.</b></i>” (Wis. Stat. s. 145.195(1))",
                  S["body"]),
        Paragraph("If you are not connecting to a municipal sewer, the county "
                  "sanitary permit comes <b>first</b>. The code says it again "
                  "from the building side: a uniform building permit “may "
                  "not be issued unless conformance with s. SPS 383.25(2) has "
                  "first been determined” (s. SPS 320.09(9)(c)).",
                  S["body"]),
    ]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "wi-permit-kit",
                       "WI.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
