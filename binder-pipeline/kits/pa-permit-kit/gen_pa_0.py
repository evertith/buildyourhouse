#!/usr/bin/env python3
"""PA.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame, centered
title block, aligned project fill-in rules, brand and edition line. Page 2 is
the one-page orientation.

The cover carries a "Plan Review & Inspections by" field where every other
state's cover simply names the building department. That is the whole
Pennsylvania problem in one line: 35 P.S. § 7210.501(b) gives a municipality
five different ways to administer the code, and § 7210.501(e)(1) covers the
sixth case — the municipality that administers it not at all, where the duty to
go and hire a certified agency lands on the permit applicant. Until the owner
has written a name on that line, nobody is inspecting the house.

The Sewage Enforcement Officer gets a line of his own for the same reason: he
does not work for the building department, he is certified by DEP and retained
by the municipality, and under 34 Pa. Code § 403.21(e) the UCC does not reach
his subject at all.
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

FORM_ID = "PA.0"
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
    c.drawCentredString(cx, 8.75 * inch, "PENNSYLVANIA")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    # 12.5pt keeps this inside the 478pt the inner frame allows.
    c.drawCentredString(cx, 7.13 * inch,
                        "Find your code official · Pass five inspections · "
                        "Earn the certificate")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "Municipality (Twp / Boro / City):",
              "County:", "Plan Review & Inspections by:",
              "Sewage Enforcement Officer:", "Owner-Builder:",
              "Permit Application Date:"]
    # "Municipality (Twp / Boro / City):" is the widest label this cover
    # carries — 189pt at 12pt, wider than any other state's — so the gutter
    # sits at 3.65in to keep its left edge clear of the 0.65in inner frame.
    # The rule then starts at 3.80in and still leaves 241pt to write on.
    label_x = 3.65 * inch
    rule_x0 = 3.80 * inch
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
                        "In a municipality that opted out, nobody assigns you "
                        "an inspector — hiring one")
    c.drawCentredString(cx, 2.11 * inch,
                        "is your job, and the house still needs all five. "
                        "Read PA.1 first.")

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 1.80 * inch,
                        "Every Pennsylvania statute, regulation and threshold "
                        "in this kit")
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
    "Five working documents, from finding out who inspects your house to the "
    "certificate of occupancy that lets you move into it.",
    S["subtitle"]))

flow.append(k.body(
    "Pennsylvania is the state where the usual first question — <i>does the "
    "code apply out here?</i> — has a flat answer that almost every guide "
    "gets backwards. It does. The Uniform Construction Code applies to "
    "“the construction, alteration, repair and occupancy of <b>all buildings "
    "in this Commonwealth</b>” (35&nbsp;P.S. §&nbsp;7210.104(a)), and five "
    "inspections are required on every one- and two-family dwelling in it."))
flow.append(k.body(
    "What Pennsylvania actually varies is <b>who shows up</b>. A municipality "
    "may hire its own code official, retain a private agency, share one with "
    "the next township, or contract with another municipality — or it may "
    "elect not to administer the code at all. That last case is the one "
    "nobody explains properly: the code does not switch off, the inspections "
    "do not go away, and the job of <b>finding and paying a certified "
    "third-party agency moves onto you</b>, the permit applicant, by name, in "
    "the statute."))
flow.append(k.body(
    "That single fact reorganizes the whole build. It changes who you call "
    "first, what your lender is sent at the end, who your appeal goes to, and "
    "what happens if you simply never hire anybody — which is legal to do "
    "right up until you try to sell, insure or finance the house. "
    "<b>PA.1 works through it</b> in the order the decisions actually arrive."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>PA.1</b>"), k.cellp("Who Inspects Your House"),
     k.cellp("Whether the UCC reaches your project at all, the six ways a "
             "municipality can handle enforcement, and what to do in each. "
             "Also the exclusions that are genuinely outside the code — "
             "including the recreational cabin, which has a seven-part test. "
             "<b>Read this first.</b>")],
    [k.cellp("<b>PA.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("What to file, the review clock and how to cut it from fifteen "
             "days to five, and the Pennsylvania amendments that change what "
             "you build — stairs, wall bracing, floor membranes, the energy "
             "tables and the receptacles the Commonwealth struck out.")],
    [k.cellp("<b>PA.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The five inspections the statute names, in order, with the rule "
             "that the final one cannot pass until the other four have. Plus "
             "the certificate of occupancy, the appeal that is granted by "
             "default if the board sleeps, and a log.")],
    [k.cellp("<b>PA.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("How to establish which of Pennsylvania's 2,500-odd "
             "municipalities holds your parcel and how it handles the code, "
             "the offices that are not the building department, and a page to "
             "write down every one you confirmed.")],
    [k.cellp("<b>PA.5</b>"), k.cellp("Forms &amp; Documents Index"),
     k.cellp("Each document you will meet: what it is, when it is due, and "
             "which office it comes from — including the ones that arrive "
             "only because you are your own builder.")],
]
flow.append(k.ref_table(
    "The five documents",
    [k.cellp("", bold=True), k.cellp("Document", bold=True),
     k.cellp("What it does for you", bold=True)],
    rows, [0.55 * inch, 2.05 * inch, CW - 2.6 * inch]))

flow += k.h2("HOW TO USE IT")
flow.append(k.bullet(
    "<b>Start with PA.1, and settle the enforcement question before you "
    "spend anything.</b> One call to the municipal office answers it. Whether "
    "the answer is “we have a code official,” “we use an agency,” or “we "
    "opted out” changes who you are dealing with for the next year."))
flow.append(k.bullet(
    "<b>Work PA.2 with a pen, early.</b> The item that surprises Pennsylvania "
    "owner-builders is not a fee — it is that several of the rules in the "
    "printed code book on your desk have been struck out or replaced by the "
    "Commonwealth, and one of them, wall bracing, was rolled back to an "
    "edition published in 2006. Building to the book and failing the framing "
    "inspection is an expensive way to learn that."))
flow.append(k.bullet(
    "<b>If your municipality opted out, hire the agency before you break "
    "ground</b> — not when you are ready for the first inspection. The "
    "agency reviews the plans as well as inspecting the work, and it has no "
    "obligation to take you on."))
flow.append(k.bullet(
    "<b>Keep PA.3 on the job</b> and record every inspection as it happens, "
    "with the date and the result. In an opt-out municipality that log may be "
    "the only continuous record anyone holds, because the agency you hired is "
    "a private company and the township never sees the file until the end."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Pennsylvania claim here was read against its primary "
                  "source in September 2026 — the Pennsylvania Construction "
                  "Code Act and the other statutes at legis.state.pa.us, and "
                  "34 Pa. Code and 25 Pa. Code at pacodeandbulletin.gov — and "
                  "is cited where it appears. Where a number genuinely varies "
                  "by municipality, the kit says so and gives you a line to "
                  "write what you confirmed rather than printing a guess. Not "
                  "legal advice.", S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "pa-permit-kit",
                       "PA.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
