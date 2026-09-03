#!/usr/bin/env python3
"""TN.5 Forms & Documents Index.

Every document an owner-builder will meet in Tennessee, named as the agency
names it, with what it is, when it happens and where it comes from.

Two negative sections carry real weight here. "What needs no permit at all" is
verified from the State Fire Marshal's own guidance and saves people from
applying for things that do not exist. "What Tennessee does not require" exists
because owner-builders arriving from other states routinely budget for a blower
door test and residential sprinklers, neither of which the state program
demands.

Verified sources:
  CN-0971 (Rev. 04-25)      the one septic/water form, its line items and fees
  0780-02-23-.05(4)         no form number is published; CORE is the path
  0780-02-23-.05(2)         additions of 30 sq ft or more need a permit
  0780-02-23-.05(5)         all building permits are non-transferable
  0780-02-23-.05(8)         duplicate permit, $10
  0780-02-23-.09            the certificate of occupancy and what gates it
  0780-02-01-.05(2)(a)      residential property owner's electrical permit
  0400-45-09-.10(1)(c),(d)  Notice of Intent, and the $75 fee
  0400-45-09-.15(1)         Report of Well Driller, 60 days
  0400-45-09-.16            hand-dug well abandonment — the one owner self-help
  SFMO guidance             what needs no state permit; sprinklers not mandatory

DELIBERATELY NOT CLAIMED:
  - A form number for the state building permit. The rule says only "a form
    prescribed by the Department" and permitting has moved into CORE.
  - When a septic Certificate of Verification is required. It is on the fee
    schedule but the rule chapter never uses the phrase.
  - Any local form name. Those vary by jurisdiction and are unverifiable in
    bulk; the document gives write-in lines instead.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

import design as d
import kit as k

S = k.S
CW = k.CW
sec = k.sec
NB = k.NB

FORM_ID = "TN.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Forms & Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document you will meet, named as the agency names it — and the "
    "things Tennessee never asks you for.")

flow.append(k.disclaimer(
    "Form numbers and fees were read from the agencies' own current forms in "
    "September 2026. Where no form number is published, this document says so "
    "rather than inventing one."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- state docs
flow += k.h2_tight("THE STATE DOCUMENTS", reserve=2.2)
rows = [
    [k.cellp("<b>CN-0971</b><br/>Application for Water Resources Services"),
     k.cellp("The one form that covers septic and most water services. The "
             "septic construction permit is line item 1. Its own instruction "
             "routes it: \"mail your application and fee to the office "
             "associated with your county shown on the next page\""),
     k.cellp("$400 permit evaluation up to 1,000&#160;gpd; $100 construction "
             "inspection")],
    [k.cellp("<b>State residential building permit</b>"),
     k.cellp("<b>No form number is published.</b> The rule requires only \"a "
             "form prescribed by the Department\" and permitting now runs "
             "through CORE at core.tn.gov. Anyone quoting you a form number is "
             "guessing"),
     k.cellp("Banded on construction cost — see TN.2")],
    [k.cellp("<b>Residential property owner's electrical permit</b>"),
     k.cellp("The homeowner's own electrical permit. Covers you and immediate "
             "family only, allows no unlicensed helpers, and <b>only one per "
             "twelve months</b>"),
     k.cellp("$35 rough-in, $35 final at 0–200&#160;amp")],
    [k.cellp("<b>Notice of Intent</b> to drill a water well"),
     k.cellp("Filed by the owner or the licensed driller <b>before drilling "
             "starts</b>. The driller must be able to document it on site. "
             "Expires in 180&#160;days"),
     k.cellp("$75 per property site")],
    [k.cellp("<b>Report of Well Driller</b>"),
     k.cellp("The completion report and well log, filed within "
             "<b>60&#160;days</b>. Includes latitude and longitude to the "
             "nearest second and confirmation that septic is 50&#160;feet or "
             "more away. <b>Get a copy — it is your well's only record</b>"),
     k.cellp("Filed by the driller")],
    [k.cellp("<b>Certificate of occupancy</b>"),
     k.cellp("Issued by the Division after all required inspections "
             "<b>and the final electrical inspection</b> pass. In an opt-out "
             "jurisdiction you can request one voluntarily"),
     k.cellp("Included; $100 for a temporary one")],
]
flow.append(k.ref_table(
    "What the state issues, and what it costs",
    [k.cellp("Document", bold=True), k.cellp("What it is", bold=True),
     k.cellp("Fee", bold=True)],
    rows, [1.75 * inch, CW - 1.75 * inch - 1.35 * inch, 1.35 * inch]))
flow.append(k.cite(
    "<b>One item we are flagging rather than explaining.</b> CN-0971 also "
    "lists a <b>Certificate of Verification</b> at $100, but rule chapter "
    "0400-48-01 never uses the phrase and the form does not say when it is "
    "needed. It reads like the document evidencing an approved system at a "
    "sale or closing. Ask the field office rather than assuming you need it."))

# ---------------------------------------------------------------- local docs
flow += k.h2_tight("THE LOCAL DOCUMENTS — IF THEY EXIST WHERE YOU ARE",
                   reserve=1.8)
flow.append(k.body(
    "In an EXEMPT jurisdiction the local government issues its own paperwork "
    "under its own names, and there is no statewide vocabulary for it. These "
    "are the ones that exist nearly everywhere they exist at all. Write in what "
    "yours calls them."))
flow += k.check_table(
    "What my jurisdiction calls each document",
    [
        ("<b>Building permit application</b> — and whether there is a separate "
         "homeowner or owner-builder version:",
         [("Called", 0.6), ("Separate form?", 0.4)]),
        ("<b>Owner-builder affidavit.</b> No <i>state</i> Board form exists; "
         "the affirmations are built into the permit application. Local "
         "jurisdictions often have their own:", [("Called", 1.0)]),
        ("<b>Zoning or land-use permit</b>, if separate from the building "
         "permit:", [("Called", 0.6), ("Issued by", 0.4)]),
        ("<b>Driveway or culvert permit</b>:",
         [("Called", 0.6), ("Road authority", 0.4)]),
        ("<b>911 address application</b>:",
         [("Called", 0.6), ("Issued by", 0.4)]),
        ("<b>Floodplain development permit</b>, if in a mapped hazard area:",
         [("Called", 0.6), ("Administrator", 0.4)]),
        ("<b>Certificate of occupancy</b> — ask whether the local jurisdiction "
         "issues one, because not all do:", [("Answer", 1.0)]),
    ])

# ---------------------------------------------------------------- no permit
flow += k.h2_tight("WHAT NEEDS NO STATE PERMIT AT ALL", reserve=2.0)
flow.append(k.body(
    "Verified from the State Fire Marshal's own guidance. <b>This is the state "
    "program's answer</b> — a local jurisdiction running its own code may "
    "require permits for all of it, so ask before you rely on any line here."))
rows = [
    [k.cellp("<b>Detached garages, sheds, barns</b>"),
     k.cellp("No state permit for detached structures <b>not used for living "
             "purposes</b>. The moment it contains a dwelling unit, that "
             "changes")],
    [k.cellp("<b>Placing a manufactured or modular home</b>"),
     k.cellp("No state permit to install one. <b>But the site work is "
             "different:</b> a site-built deck, patio or stoop attached to it "
             "needs a manufactured or modular site work permit")],
    [k.cellp("<b>Renovations to an existing house</b>"),
     k.cellp("The state program covers new construction and additions only. "
             "Renovation is outside it")],
    [k.cellp("<b>Additions under 30&#160;sq&#160;ft</b>"),
     k.cellp("Additions of <b>30&#160;square feet or more</b> of interior "
             "space need a permit. Below that, no. The existing house does not "
             "have to be brought up to code — the addition does")],
]
flow.append(k.ref_table(
    "No state permit required",
    [k.cellp("What", bold=True), k.cellp("The condition", bold=True)],
    rows, [2.2 * inch, CW - 2.2 * inch]))

# ---------------------------------------------------------------- never
flow += k.h2_tight("WHAT TENNESSEE DOES NOT REQUIRE", reserve=2.0)
flow.append(k.body(
    "Worth knowing because owner-builders arriving from other states routinely "
    "budget for these. Under the <b>state</b> program, none of them is "
    "mandatory."))
flow.append(k.bullet(
    "<b>A blower door test.</b> The mandatory whole-house air leakage test was "
    "replaced with a choice between a testing option and a visual inspection "
    "against a checklist."))
flow.append(k.bullet(
    "<b>Duct leakage testing.</b> Both the mandatory and the prescriptive "
    "provisions are optional."))
flow.append(k.bullet(
    "<b>Residential fire sprinklers.</b> Not mandatory in one- and two-family "
    "dwellings or townhouses. Because townhouses go unsprinklered, they must "
    "instead be separated by two-hour fire walls."))
flow.append(k.bullet(
    "<b>A separate energy or insulation inspection.</b> Energy compliance is "
    "observed during the inspections you are already having."))
flow.append(k.bullet(
    "<b>A state owner-builder affidavit form.</b> The Board for Licensing "
    "Contractors publishes no such thing. The affirmations live on the permit "
    "application you sign."))
flow.append(k.cite(
    "<b>All five are the state program's answers, and an EXEMPT jurisdiction "
    "may differ on every one of them.</b> A city on a newer local energy code "
    "can require a blower door; a local ordinance can require sprinklers. This "
    "list tells you what the <i>state</i> will not ask for — not what your "
    "building official will not ask for."))

# ---------------------------------------------------------------- the one thing
flow += k.h2_tight("THE ONE THING YOU MAY NOT DO YOURSELF", reserve=1.8)
flow.append(k.body(
    "Tennessee is generous about owner-performed work. You may act as your own "
    "general contractor, wire your own house on a homeowner electrical permit, "
    "and do your own plumbing. <b>You may not drill your own well.</b>"))
flow.append(k.callout(
    "The sentence that kills the \"my builder will handle it\" assumption", [
        Paragraph("TDEC states it without hedging: \"Tennessee licensed "
                  "<b>general contractors, licensed electricians, and licensed "
                  "plumbers ARE NOT permitted</b> to install or perform "
                  "maintenance on water wells, water well pumps, or water well "
                  "treatment systems <b>unless they are also licensed by the "
                  "TDEC, Division of Water Resources</b>.\"", S["body"]),
        Paragraph("The rules bar <i>any person</i> from constructing a well "
                  "except in accordance with the Water Wells Act, and they "
                  "carve out no exemption for owners. The owner's recognized "
                  "role is on the <i>paperwork</i> — you may file the Notice of "
                  "Intent yourself — which is easy to misread as permission to "
                  "dig. It is not. The one physical task the rules do let a "
                  "landowner perform is <b>abandoning a hand-dug well less "
                  "than sixty feet deep</b>.", S["body"]),
    ]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "tn-permit-kit",
                       "TN.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
