#!/usr/bin/env python3
"""MT.5 Forms & Documents Index — Montana.

Montana scatters an owner-builder's paperwork across a state bureau, possibly a
certified local program, a county sanitarian, a county clerk and recorder, DEQ,
DNRC, and a power supplier — and for the ordinary rural house, several of the
documents people go looking for do not exist at all. This index names what is
real, says which office issues it, and is equally careful to name the ones that
are not.

Sources verified August 2026:
  bsd.dli.mt.gov  Electrical Permits page: online and printable applications —
                  Residential Permit, Commercial Permit, Permit Transfer Form,
                  Alternative Energy Permit ("for use by non-licensed
                  installers"), and the HOMEOWNER ELECTRICAL PERMIT ("Permit
                  for Homeowners personally performing work on their own
                  home"); plus an Electrical Information Pamphlet
                  Plumbing Permits page: online and printable applications; the
                  2021 UPC effective June 11, 2022; ARM 24.301.351 fixture
                  table, with a legible copy published because the rule "is
                  very difficult to read"
                  Mechanical Permits page: online and printable applications
                  Building Permits page: Building Permit/Plan Review
                  Application and a Commercial Building Checklist
  50-60-106(2)(c) / 50-60-118  the department's single-family dwelling
                  checklist that certified jurisdictions must make available,
                  and the 10-working-day clock attached to it
  50-60-802(1)    the energy certification the builder writes
  50-60-107       certificates of occupancy, issued by certified locals
  37-45-201       the construction contractor license
  39-71-417       the independent contractor exemption certificate
  76-4-121, -122, -125  certificate of subdivision approval, sanitary
                  restrictions, and exemption certifications on a plat or
                  certificate of survey
  85-2-306(3)(b), (3)(c), (3)(d)  notice of intent, notice of completion, and
                  the certificate of water right

Still deliberately hedged: no form numbers are invented — where Montana names a
document without numbering it, the kit prints the name as published; county
septic and addressing packets are each their own and are described by function;
and no fees appear anywhere.
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

FORM_ID = "MT.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document a Montana owner-builder is likely to meet — what each one "
    "is, when you need it, and which office it comes from.")

flow.append(k.disclaimer(
    "Montana names most of its permit documents rather than numbering them, so "
    "this index prints names as published. Your county's septic and addressing "
    "packets are its own."))
flow.append(Spacer(1, 8))

DOCS = [
    ("Homeowner Electrical Permit <font size=8.5>(type EOWN)</font>",
     "The one form most readers of this kit need. The department publishes it "
     "specifically as a \"<i>Permit for Homeowners personally performing work "
     "on their own home</i>,\" alongside the residential (ERES) and "
     "commercial (ECON) versions. Remember why you still need it: "
     "37-68-103(3)(a) excuses you from the electrician's <b>license</b>, not "
     "from the permit (MT.1) — and the permit rule limits it to your own "
     "residence, not a spec or rental build (ARM 24.301.431(3)). Valid "
     "<b>18 months</b> with one 18-month renewal. <b>When:</b> before the "
     "first wire — and certainly before your power supplier will connect you "
     "(50-60-605).",
     "DLI — bsd.dli.mt.gov &#8594;<br/>Electrical Permits;<br/>online at "
     "ebiz.mt.gov"),
    ("Alternative Energy Permit",
     "A separate electrical application the department publishes \"<i>for use "
     "by non-licensed installers</i>\" for generators, solar, and wind. Read "
     "it against 37-68-103(3)(b), which removes <b>grid-tied generator</b> "
     "work from the homeowner exemption — the permit form and the licensing "
     "question are two different tests, so settle both before you buy panels.",
     "DLI — same page"),
    ("Electrical Permit — Residential / Commercial · Permit Transfer Form · "
     "Electrical Information Pamphlet",
     "The contractor-facing versions, the form for moving a permit to another "
     "party, and a plain-language pamphlet the Building Codes Bureau publishes "
     "to explain state electrical requirements. The pamphlet is free and is "
     "the closest thing Montana offers to an official owner-builder handbook "
     "for the trade.",
     "DLI — same page"),
    ("Plumbing Permit application",
     "Needed only if someone other than you does the plumbing, or if a "
     "certified local program has jurisdiction — as owner of residential "
     "property doing the work personally you need no permit at all "
     "(50-60-506(4)). If you do apply, note that Montana runs the <b>Uniform "
     "Plumbing Code</b>, not the IPC. <b>Ask for the legible fixture "
     "table:</b> the department publishes a clear copy because ARM 24.301.351 "
     "\"<i>is very difficult to read</i>.\"",
     "DLI — Plumbing Permits,<br/>or your local program"),
    ("Mechanical Permit application",
     "Covers heating, ventilating, cooling and — worth noting — <b>gas "
     "piping</b>. The department ties state mechanical permits to buildings "
     "\"<i>to which state building permits are applicable</i>,\" which your "
     "exempt house is not; confirm your building's status rather than "
     "assuming either way. <b>When:</b> before installation, if required.",
     "DLI — Mechanical Permits,<br/>or your local program"),
    ("Building Permit / Plan Review Application · Commercial Building "
     "Checklist",
     "The state building permit package — which you will probably never file, "
     "because a residential building of fewer than five dwelling units is "
     "outside the state building code (50-60-102(1)(a)). Listed here so you "
     "recognize it and do not waste weeks on it. Where a state building permit "
     "<i>is</i> required, it must be issued before the plumbing, mechanical, "
     "or electrical permits are.",
     "DLI — Building Permits"),
    ("The department's single-family dwelling checklist",
     "Worth asking for by name. Certified jurisdictions must make available "
     "\"<i>a checklist devised by the department pursuant to 50-60-118 for "
     "single-family dwellings</i>,\" and a contractor who attaches a completed "
     "one to the submitted plans is entitled to the permit or a written plan "
     "disapproval <b>within 10 working days</b> (50-60-106(2)(c)). A statewide "
     "checklist with a clock attached to it.",
     "Your certified local program"),
    ("Construction contractor license",
     "Required since <b>January 1, 2026</b> of anyone engaging in business as "
     "a construction contractor (37-45-201). As an owner working on your own "
     "property you are exempt (37-45-104(13)) — but you will use the "
     "<b>license lookup</b> constantly, because verifying a contractor's "
     "license <b>on the date of the contract</b> is what switches on your "
     "liability shield (37-45-202).",
     "DLI &#8594; Lookup a License"),
    ("Independent Contractor Exemption Certificate (ICEC)",
     "Held by a solo trade with no employees (39-71-417). Ask for a copy from "
     "every one-person business you engage and file it — hiring someone who "
     "lacks a required certificate is named as unprofessional conduct for a "
     "licensee (37-45-301(1)(d)), and the underlying question is who counts as "
     "your employee.",
     "The contractor holds it;<br/>DLI ICEC Program"),
    ("Certificate of Subdivision Approval — or the exemption certification",
     "<b>The document that decides whether the parcel is buildable.</b> One of "
     "these must exist before you may erect or occupy a building needing water "
     "or sewage facilities (76-4-121). An exemption instead of a certificate "
     "is fine, but it must appear on the plat or certificate of survey and "
     "\"<i>must quote in its entirety the wording of the applicable "
     "exemption</i>\" (76-4-122(2)(c)). <b>When:</b> before you buy the land.",
     "County clerk and recorder<br/>(the record); DEQ / county<br/>(the review)"),
    ("County septic permit and site evaluation",
     "There is no state form. The application, the soil and site work, the "
     "setbacks, and the inspection before cover are your county's under its "
     "own regulations, with the local health officer holding real statutory "
     "authority (76-4-122(2)(a); 76-4-125(2)). <b>When:</b> after the site "
     "evaluation, before any excavation for the system.",
     "County environmental<br/>health / sanitarian"),
    ("Notice of Intent to Appropriate Groundwater",
     "Filed with DNRC and <b>authorized</b> by it <b>before</b> you drill "
     "(85-2-306(3)(b)). Defects are notified within 10 business days and an "
     "uncorrected notice terminates after 60 days. Once authorized you have "
     "five years to complete the appropriation.",
     "DNRC — dnrc.mt.gov &#8594;<br/>Water Resources"),
    ("Notice of Completion · Certificate of Water Right",
     "Filed <b>within 60 days</b> of completing the well and putting water to "
     "beneficial use (85-2-306(3)(c)(i)). No certificate of water right issues "
     "until it is correct and complete — and <b>the date you file it is the "
     "priority date of your right</b> (85-2-306(3)(d)). Do not let this one "
     "sit in a truck.",
     "DNRC — same"),
    ("911 address assignment · road approach permit · floodplain development "
     "permit",
     "Three small county approvals that other applications depend on. The "
     "address is what a permit application and a power supplier both key on; "
     "the approach permit comes from whoever owns the road, which may be MDT "
     "if you meet a state highway; the floodplain permit applies whether or "
     "not a building permit does. <b>When:</b> early, all three.",
     "County addressing, road<br/>department, and floodplain<br/>administrator"),
    ("Your written energy certification",
     "Not filed — <b>written, signed, and kept</b>. \"<i>A person who begins "
     "construction on a residential building … shall certify in writing to the "
     "building owner at the conclusion of construction that the residential "
     "building has been constructed in compliance with the energy-efficient "
     "construction standards</i>\" (50-60-802(1)). As owner-builder you are "
     "both parties. Name the adopted edition, list the R-values, U-factors, "
     "and equipment efficiencies you actually installed, date it, sign it.",
     "You write it"),
    ("The permanent energy label",
     "Not filed — <b>stuck inside your electrical panel</b>. Under 50-60-803 "
     "and ARM 24.301.162 the builder completes a signed and dated permanent "
     "self-adhesive label, roughly four inches by six, listing insulation "
     "R-values, window U-factor, heating and cooling equipment efficiencies, "
     "and water heater efficiency, and permanently attaches it to the "
     "interior of the electrical panel. It is separate from the written "
     "certification above, and it is the version a home inspector will "
     "actually find in fifteen years. <b>When:</b> at completion.",
     "You complete it;<br/>50-60-803, MCA"),
    ("Floodplain development permit — Joint Application",
     "Where any part of the site is in a designated floodplain or floodway "
     "(76-5-404). DNRC publishes a Joint Application for Proposed Work in "
     "Montana's Streams, Wetlands, Floodplains, and Other Water Bodies; its "
     "<b>Section C</b> is the city or county floodplain development permit. "
     "Fees and timelines are set locally and vary widely. Design to the "
     "two-foot freeboard in 76-5-402 before you draw the foundation. "
     "<b>When:</b> before any site work.",
     "Local floodplain<br/>administrator; form at<br/>dnrc.mt.gov"),
    ("Certificate of occupancy",
     "Issued by a certified local program at the end of the job "
     "(50-60-106(2)(e); 50-60-107). <b>Outside a certified program there is "
     "no certificate of occupancy</b>, because there is no program to issue "
     "one — see the note below.",
     "Your certified local program"),
]

rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in DOCS]
flow.append(k.ref_table(
    "Documents a Montana owner-builder will actually encounter",
    [k.cellp("Document", bold=True),
     k.cellp("What it is and when you need it", bold=True),
     k.cellp("Where it comes from", bold=True)],
    rows, [1.75 * inch, CW - 1.75 * inch - 1.75 * inch, 1.75 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout_long("Forms that do not exist — stop looking for them", [
    Paragraph("There is <b>no state owner-builder affidavit, exemption form, "
              "or registration</b>. The exemptions in 37-45-104(13), "
              "37-68-103(3)(a), and 50-60-506(4) are self-executing in the "
              "statute — nobody grants them to you and there is nothing to "
              "apply for. There is <b>no state building permit for a house</b> "
              "of fewer than five dwelling units. There is <b>no state "
              "certificate of occupancy</b>, and outside a certified program "
              "no certificate of occupancy at all. And there is no longer any "
              "such thing as a <b>construction contractor registration</b> — "
              "it became a license on January 1, 2026 (MT.1).", S["body"]),
    Paragraph("Which raises the question this kit exists to answer: when a "
              "lender, insurer, appraiser, or future buyer asks for \"the "
              "permits\" on a rural Montana build, <b>what do you hand "
              "them?</b> This stack: the <b>electrical permit and its final "
              "approval</b>; the <b>signed energy certification</b>; the "
              "<b>certificate of subdivision approval or the recorded "
              "exemption</b>; the <b>county septic permit and final</b>; the "
              "<b>DNRC notice of completion and certificate of water "
              "right</b>; the <b>address assignment and approach permit</b>; "
              "and the record you built yourself in MT.3 — the snow load you "
              "designed to, the photographs of everything now covered, and the "
              "product data for the assemblies that matter. Assembled, that is "
              "a stronger file than most permitted houses ever produce. "
              "Unassembled, it is nothing, and you will be reconstructing it "
              "from memory years later.", S["body"]),
]))

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026): the electrical, plumbing, "
    "mechanical, and building permit form sets and their published "
    "descriptions — bsd.dli.mt.gov, Building Codes Program. The single-family "
    "checklist and its 10-working-day clock — 50-60-106(2)(c); 50-60-118, "
    "MCA. Certificates of occupancy — 50-60-106(2)(e); 50-60-107, MCA. "
    "Contractor licensing and the liability shield — 37-45-104(13), "
    "37-45-201, 37-45-202, 37-45-301(1)(d), MCA; 39-71-417, MCA. Sanitation "
    "documents — 76-4-121, 76-4-122(2)(a), (2)(c), 76-4-125(2), MCA. Water "
    "filings — 85-2-306(3)(b), (3)(c)(i), (3)(d), MCA. Energy certification — "
    "50-60-802(1), MCA. Homeowner trade exemptions — 37-68-103(3)(a), (3)(b); "
    "50-60-506(4), MCA."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "mt-permit-kit",
                       "MT.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
