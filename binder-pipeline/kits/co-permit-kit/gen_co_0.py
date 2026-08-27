#!/usr/bin/env python3
"""CO.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame,
centered title block, aligned project fill-in rules, brand and edition line.
The following pages carry the kit's thesis: Colorado runs TWO permit systems
over one house, and they are decided independently. The building permit is
purely local and may not exist at all. The electrical and plumbing/gas permits
are STATE permits by default, everywhere a local government does not run its
own qualifying program.

Sources verified August 2026 (each also cited where it appears in CO.1-CO.5).
Statute text read from the official Colorado Revised Statutes 2026 PDFs
published by the Office of Legislative Legal Services (olls.info/crs, linked
from leg.colorado.gov):
  C.R.S. 30-28-201(1)    counties "authorized to" adopt a building code —
                         permissive; agricultural shelter may be excepted
  C.R.S. 30-28-205(1)    "After the adoption of the building code" it is
                         unlawful to build without a county permit — the
                         permit duty is contingent on the county adopting one
  C.R.S. 31-15-601       municipal building and fire regulation powers
  C.R.S. 12-115-120(1)(a)(I), (2)(a)  state electrical permit unless the local
                         government runs a qualifying program
  C.R.S. 12-155-120(1)(a)  state plumbing AND GAS PIPING permit unless the
                         local entity conducts inspections and issues permits
  C.R.S. 12-115-120(11)(c), 12-155-120(11)(c)  a homeowner working on their
                         own home is a "qualified applicant" for both permits
  C.R.S. 12-115-116(2)   the homeowner electrical exemption is conditioned on
                         the work being inspected — the kit's headline trap
  C.R.S. 12-155-118(2)   the plumbing exemption carries no inspection condition
  C.R.S. 12-115-120(1)(c)  no utility service without proof of final approval
  C.R.S. 12-120-403(1)(a)  one- to four-family dwellings are exempt from the
                         architect-licensing requirement — you may draw your
                         own plans

Still deliberately hedged: which counties currently require no building permit
(a county-by-county fact that rots — the kit gives the verification step, not
a roster); every adopted code edition; and every local fee.
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

FORM_ID = "CO.0"
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
    c.drawCentredString(cx, 8.75 * inch, "COLORADO")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 7.13 * inch,
                        "Two permit systems · One house · "
                        "Find out which offices own yours")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "County:",
              "City / unincorporated:", "Owner-Builder:"]
    label_x = 3.35 * inch
    rule_x0 = 3.5 * inch
    rule_x1 = PAGE_W - 1.35 * inch
    y = 5.5 * inch
    c.setFillColor(d.INK)
    for label in fields:
        c.setFont(d.BODY, 12)
        c.drawRightString(label_x, y, label)
        c.setLineWidth(0.75)
        c.line(rule_x0, y - 2, rule_x1, y - 2)
        y -= 0.62 * inch

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.35 * inch,
                        "Every Colorado statute, board rule, and requirement "
                        "in this kit is cited on")
    c.drawCentredString(cx, 2.13 * inch,
                        "the page it appears on — verified August 2026.")

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
    "Five working documents that take a Colorado owner-builder from \"which "
    "office does my house even answer to?\" to a house you can legally "
    "occupy, insure, and — the part Colorado enforces hardest — get "
    "permanent power to.",
    S["subtitle"]))

flow.append(k.body(
    "Most states hand you one permit counter. Colorado hands you two, and "
    "they are decided separately. <b>The building permit is entirely "
    "local.</b> Colorado adopts no statewide residential building code and "
    "licenses no general contractor; a board of county commissioners is "
    "merely \"<i>authorized to</i>\" adopt a building code, and the duty to "
    "get a permit exists only \"<i>after the adoption of the building "
    "code</i>\" — so in some unincorporated counties there is no building "
    "permit to apply for at all. <b>The electrical and plumbing permits are "
    "STATE permits.</b> Unless your city or county runs its own qualifying "
    "inspection program, you buy those permits from the Colorado State "
    "Electrical Board and the State Plumbing Board and a state inspector "
    "comes out."))

flow.append(k.callout("The Colorado inversion — read this twice", [
    Paragraph("It is entirely possible, and common, to build in "
              "unincorporated Colorado where <b>no building permit exists "
              "for your house</b> and a <b>state permit is still required "
              "before you run the first wire or the first pipe</b>. People "
              "who hear \"my county has no building code\" and conclude "
              "\"no permits\" are wrong in the most expensive way "
              "available: the utility may not connect permanent power "
              "without proof of final electrical approval. "
              "(C.R.S. 30-28-205(1); 12-115-120(2)(a), (1)(c))", S["body"]),
]))
flow.append(Spacer(1, 6))

flow += k.h2("TWO SYSTEMS, ONE HOUSE — THE HEADLINE OF THIS KIT")
sys_rows = [
    [k.cellp("<b>Who decides whether it exists</b>"),
     k.cellp("Your county or municipality, alone. A board of county "
             "commissioners \"<i>is authorized to</i>\" adopt a building "
             "code (30-28-201(1)); until it does, there is no county "
             "building permit (30-28-205(1)). Home-rule cities set their "
             "own."),
     k.cellp("The General Assembly, statewide. The permit exists for every "
             "installation in new construction — the only question is "
             "<b>who issues it</b>.")],
    [k.cellp("<b>Who issues it</b>"),
     k.cellp("The county building department or the city. If your "
             "jurisdiction adopted no code, nobody does — and no building "
             "permit is required."),
     k.cellp("The State Electrical Board and the State Plumbing Board — "
             "<b>unless</b> your local government runs its own qualifying "
             "program, in which case the local building department does "
             "(12-115-120(1)(a)(I); 12-155-120(1)(a)).")],
    [k.cellp("<b>Which code applies</b>"),
     k.cellp("Whichever edition your jurisdiction adopted, with local "
             "amendments — this kit prints no edition, because there is no "
             "statewide answer. Ask, and write it down."),
     k.cellp("The National Electrical Code and the Colorado plumbing code "
             "as adopted by the boards — a statewide <b>floor</b>. Local "
             "governments may be stricter, never weaker "
             "(12-115-107(2)(a)(I); 12-155-106(2)).")],
    [k.cellp("<b>May you pull it yourself</b>"),
     k.cellp("Local policy. Most Colorado jurisdictions let an owner permit "
             "their own home; some attach an affidavit or occupancy "
             "condition. Confirm in writing — CO.1."),
     k.cellp("Yes, by statute. \"<i>Qualified applicant</i>\" expressly "
             "includes \"<i>a homeowner performing work on the homeowner's "
             "home</i>\" for both permits (12-115-120(11)(c); "
             "12-155-120(11)(c)).")],
]
flow.append(k.ref_table(
    "The local track and the state track are settled separately",
    [k.cellp("", bold=True),
     k.cellp("LOCAL — the building permit", bold=True),
     k.cellp("STATE — electrical, plumbing, gas piping", bold=True)],
    sys_rows, [1.3 * inch, (CW - 1.3 * inch) / 2, (CW - 1.3 * inch) / 2]))
flow.append(k.cite(
    "C.R.S. 30-28-201(1), 30-28-205(1), 31-15-601; 12-115-120(1)(a)(I), "
    "(2)(a), (11)(c); 12-155-120(1)(a), (11)(c); 12-115-107(2)(a)(I); "
    "12-155-106(2). Statute text read from the official Colorado Revised "
    "Statutes 2026 at leg.colorado.gov, August 2026. How to settle both "
    "questions for your parcel is worked in CO.4."))

flow += k.h2("THE FOUR QUESTIONS THIS KIT MAKES YOU ANSWER FIRST")
flow.append(k.body(
    "Nothing else can be answered until these are, and they are independent "
    "of each other — a jurisdiction can run an electrical program and not a "
    "plumbing one, because the statutes use different tests. Ask each "
    "separately and get the answers in writing. <b>(1)</b> Does my county or "
    "city require a building permit for a new single-family home, and under "
    "which code edition and amendments? <b>(2)</b> For ELECTRICAL, does my "
    "jurisdiction issue the permit and inspect, or do I buy a state permit? "
    "<b>(3)</b> For PLUMBING AND GAS PIPING, same question asked separately. "
    "<b>(4)</b> Where do my water and wastewater come from — and is a well "
    "permit obtainable here at all? In Colorado that last one is settled "
    "before design, not after (CO.2)."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>CO.1</b>"), k.cellp("The Owner-Builder's Legal Position"),
     k.cellp("No state license, no state building code — and the two state "
             "trade permits that apply anyway. Includes the kit's headline "
             "trap: the homeowner electrical exemption is conditioned on "
             "getting inspected. <b>Read this first.</b>")],
    [k.cellp("<b>CO.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("Two checklists — the local building permit and the state "
             "trade permits — plus the land approvals (water, wastewater, "
             "access) that gate everything in Colorado.")],
    [k.cellp("<b>CO.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The local ladder, where the state electrical and plumbing "
             "inspections slot into it, and the utility release that is the "
             "real finish line.")],
    [k.cellp("<b>CO.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("How to determine who permits your parcel, the state agencies "
             "that own a piece, and a page to fill in your own offices.")],
    [k.cellp("<b>CO.5</b>"), k.cellp("Forms &amp; Documents Index"),
     k.cellp("Each named form and permit you will meet, what it is, and "
             "which office it comes from.")],
]
flow.append(k.ref_table(
    "The five documents",
    [k.cellp("", bold=True), k.cellp("Document", bold=True),
     k.cellp("What it does for you", bold=True)],
    rows, [0.55 * inch, 2.05 * inch, CW - 2.6 * inch]))

flow += k.h2("HOW TO USE IT")
flow.append(k.body(
    "<b>Read CO.1 first</b>, before you plan to do your own wiring or "
    "plumbing — Colorado's homeowner exemptions are real and generous, and "
    "the electrical one has a condition inside it that most people never "
    "see. <b>Work CO.2 with a pen</b>, starting with water and wastewater: a "
    "well permit is not a formality here, and in over-appropriated areas it "
    "can decide whether the house is buildable at all. <b>Keep CO.3 on the "
    "job</b> and log every inspection as it happens, including the state ones "
    "you schedule yourself and nobody will chase you about. And <b>fill in "
    "CO.4 before you need it</b> — Colorado splits the answers across a "
    "county, possibly a city, two state boards, a public health agency, and "
    "the Division of Water Resources."))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Colorado claim here was read against its primary "
                  "source in August 2026 — statute text from the official "
                  "Colorado Revised Statutes 2026 published by the Office "
                  "of Legislative Legal Services, board rules from the Code "
                  "of Colorado Regulations, agency facts from the agency's "
                  "own pages — and is cited where it appears. Colorado "
                  "renumbered its entire professions title in 2019, so older "
                  "guides cite sections that no longer exist; this kit uses "
                  "current numbering. Where jurisdictions differ, the kit "
                  "gives the verification step rather than an answer that "
                  "would rot. This is a process reference, not legal advice.",
                  S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "co-permit-kit",
                       "CO.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
