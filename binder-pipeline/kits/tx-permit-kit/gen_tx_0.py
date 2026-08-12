#!/usr/bin/env python3
"""TX.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame,
centered title block, aligned project fill-in rules, brand and edition line.
The following pages carry the kit's thesis: Texas is a two-track state, and
which track you are on is decided by one question — is the lot inside a
city's limits or not.

Sources verified August 2026 (each cited where it appears):
  tdlr.texas.gov            no general-contractor or home-builder program on
                            TDLR's A-Z regulated-program list; the Texas
                            Residential Construction Commission's statute
                            expired in 2009
  Local Gov't Code § 214.212  IRC as of May 1, 2012 adopted as the municipal
                            residential building code; cities amend locally
  Local Gov't Code § 214.904  45-day municipal action clock on the permit
  Local Gov't Code § 233.153(d)(1)  the county building-standards subchapter
                            "may not be construed to require prior approval
                            by the county" — no county building permit
  Health & Safety Code § 366.051  septic (OSSF) permit + approved plan
  Water Code §§ 16.315, 16.3145  county floodplain rules / NFIP orders
  Health & Safety Code §§ 388.003–.004  statewide energy code, and how it is
                            enforced where no permit office exists
  Occupations Code Chs. 1305, 1301, 1302  the three licensed trades
  Insurance Code Ch. 2210   coastal windstorm certification (TWIA)
  Property Code § 53.254; Tex. Const. art. XVI § 50(a)(5)  homestead liens

Still deliberately hedged: the no-GC-license fact is printed as an
"as of August 2026" absence (legislatures create licenses), and every
local-variable item points at the office that owns it rather than printing
an answer that would rot.
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

FORM_ID = "TX.0"
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
    c.drawCentredString(cx, 8.75 * inch, "TEXAS")
    c.setFont(d.BOLD, 30)
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 7.13 * inch,
                        "Find your track · File what binds you · "
                        "Pass the inspections that exist")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "County:",
              "City / ETJ / unincorporated:", "Owner-Builder:"]
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
                        "Every Texas statute, agency rule, and requirement "
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
    "Five working documents that take a Texas owner-builder from \"do I "
    "even need a permit?\" to a house you can legally occupy, insure, and "
    "power.",
    S["subtitle"]))

flow.append(k.body(
    "Texas licenses no general contractors and issues no state residential "
    "building permit — as of August 2026 the Texas Department of Licensing "
    "and Regulation's own list of regulated programs contains no "
    "general-contractor or home-builder program, and the Texas Residential "
    "Construction Commission's statute expired in 2009 and was not replaced. "
    "Anyone, including you, may build a house. <b>But Texas is not a "
    "no-rules state.</b> The rules attach to the three licensed trades, to "
    "the land (septic, floodplain, driveway, well), to the coast "
    "(windstorm), to energy (a statewide energy code that applies even "
    "where no permit exists), and to the homestead lien system. Which of "
    "these bind you depends almost entirely on one question: <b>is your lot "
    "inside a city's limits or not?</b>"))
flow.append(k.cite(
    "Absence of a state GC license: TDLR regulated-program list, "
    "tdlr.texas.gov, checked August 2026 — verify nothing has changed there "
    "before you rely on it. Three trades ARE licensed: electrical, plumbing, "
    "HVAC (Occupations Code Chs. 1305, 1301, 1302) — see TX.1."))

flow += k.h2("THE TWO TRACKS — THE HEADLINE OF THIS KIT")
track_rows = [
    [k.cellp("<b>Who issues a building permit</b>"),
     k.cellp("The city. The IRC \"as it existed on May 1, 2012\" is the "
             "statutory municipal residential code; cities amend it and "
             "adopt newer editions, and the big cities all have. The city "
             "must act on your application within 45 days. "
             "(§§ 214.212, 214.904)"),
     k.cellp("Usually nobody. Counties generally cannot require a building "
             "permit for a single-family house — even the opt-in county "
             "building-standards subchapter \"may not be construed to "
             "require prior approval by the county.\" (§ 233.153(d)(1))")],
    [k.cellp("<b>What binds you anyway</b>"),
     k.cellp("The city's adopted codes, its inspection ladder, contractor "
             "registration, owner-builder (\"homestead\") permit rules, "
             "plat and zoning requirements, and the certificate of "
             "occupancy at the end."),
     k.cellp("Septic permit BEFORE construction (Health &amp; Safety Code "
             "§ 366.051), floodplain development permit (Water Code "
             "§§ 16.315, 16.3145), the statewide energy code (§§ 388.003–"
             ".004), trade licensing everywhere, and — on the coast — TDI "
             "windstorm certification (Insurance Code Ch. 2210).")],
    [k.cellp("<b>Who inspects</b>"),
     k.cellp("The city's inspectors, at every rung of the ladder, ending in "
             "a certificate of occupancy. See TX.3."),
     k.cellp("Five separate inspectors at most — septic, windstorm, energy, "
             "the electric utility's meter release, and (in opt-in "
             "counties) three private inspections. Nobody inspects your "
             "wiring by default. See TX.3.")],
]
flow.append(k.ref_table(
    "Track A vs. Track B — where your lot is decides everything",
    [k.cellp("", bold=True),
     k.cellp("TRACK A — inside a city's limits", bold=True),
     k.cellp("TRACK B — unincorporated county", bold=True)],
    track_rows, [1.35 * inch, (CW - 1.35 * inch) / 2, (CW - 1.35 * inch) / 2]))
flow.append(k.cite(
    "Local Gov't Code §§ 214.212, 214.904, 233.153(d)(1); Health &amp; "
    "Safety Code §§ 366.051, 388.003–.004; Water Code §§ 16.315, 16.3145; "
    "Insurance Code Ch. 2210. Statute text read at statutes.capitol.texas."
    "gov, August 2026. How to determine your track — including the ETJ, the "
    "in-between zone — is worked in TX.4."))

flow += k.h2("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>TX.1</b>"), k.cellp("The Owner-Builder's Legal Position"),
     k.cellp("No state license, no state permit — and the three trade-"
             "licensing regimes whose homeowner exemptions each use "
             "different words with different traps. <b>Read this "
             "first.</b>")],
    [k.cellp("<b>TX.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("Two checklists — one per track — plus the homestead lien "
             "rules that follow you on either one.")],
    [k.cellp("<b>TX.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("The municipal ladder on Track A; the five separate "
             "inspectors — and the honest gaps — on Track B.")],
    [k.cellp("<b>TX.4</b>"), k.cellp("Where to File Directory"),
     k.cellp("How to determine your track, the state agencies, the "
             "high-volume jurisdictions, and a page to fill in your own.")],
    [k.cellp("<b>TX.5</b>"), k.cellp("Forms &amp; Documents Index"),
     k.cellp("Each named form you will meet — WPI-1, TCEQ 0235, city "
             "homestead affidavits — what it is and where it lives.")],
]
flow.append(k.ref_table(
    "The five documents",
    [k.cellp("", bold=True), k.cellp("Document", bold=True),
     k.cellp("What it does for you", bold=True)],
    rows, [0.55 * inch, 2.05 * inch, CW - 2.6 * inch]))

flow += k.h2("HOW TO USE IT")
flow.append(k.bullet(
    "<b>Settle your track before anything else</b> — city limits, ETJ, or "
    "unincorporated county (TX.4 shows how). Every other answer in this kit "
    "depends on it."))
flow.append(k.bullet(
    "<b>Read TX.1 before you plan to do your own wiring, plumbing, or "
    "HVAC.</b> The three homeowner exemptions are not interchangeable, and "
    "the electrical one has a trap for new construction."))
flow.append(k.bullet(
    "<b>Work TX.2 with a pen</b> and do not file — or, on Track B, do not "
    "break ground — until the boxes are checked. The septic permit and the "
    "coastal windstorm notice both come BEFORE construction."))
flow.append(k.bullet(
    "<b>Keep TX.3 on the job</b> and record every inspection date and "
    "result as it happens — on Track B, the inspections you arrange are the "
    "only record that will ever exist."))
flow.append(k.bullet(
    "<b>Fill in TX.4 before you need it.</b> Texas splits the answers "
    "across a city, a county, and up to six state agencies; ten minutes of "
    "calls early saves weeks later."))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Texas claim here was read against its primary "
                  "source in August 2026 — statute text at "
                  "statutes.capitol.texas.gov, agency facts on the agency's "
                  "own pages — and is cited where it appears. Where cities "
                  "or counties differ, the kit says so and gives the "
                  "verification step instead of an answer that would rot. "
                  "This is a process reference, not legal advice, and does "
                  "not replace the office that will actually permit or "
                  "inspect your build. Texas passed major preemption and "
                  "ETJ legislation as recently as 2023–2025 — confirm "
                  "anything you rely on.", S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "tx-permit-kit",
                       "TX.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
