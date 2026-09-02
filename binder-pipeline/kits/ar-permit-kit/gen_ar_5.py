#!/usr/bin/env python3
"""AR.5 Forms & Documents Index.

Every document an Arkansas owner-builder will actually meet, named the way the
issuing office names it — plus the two lists that save the most money: what
needs no permit even where permits exist, and what Arkansas never adopted.

Verified sources:
  Form EHP-19 (R 9/24)  Individual Onsite Wastewater System Permit Application,
              Arkansas Department of Health — the three-part structure, the
              owner's Utilization Verification at item 19, the DR's signature at
              item 20, and the one-year validity of the Permit for Construction
  Onsite Wastewater Rules § 4.9, § 4.10.1 to § 4.10.3, Appendix F
  17 CAR § 11-401, § 11-403  the well construction report and the copy owed to
              the customer on demand
  Ark. Code Ann. § 18-44-115  Notice to Owner — no lien on residential property
              of four or fewer units without it
  AFPC Vol. III § R105.2  work exempt from permit — verified UNAMENDED
  AFPC Vol. III § R102.5  appendices not adopted by the State of Arkansas
  AFPC Vol. III § R110  certificate of occupancy

DELIBERATELY NOT PRINTED:
  - Any local form number. Arkansas cities and counties name their own forms and
    change them; the document names the FUNCTION and leaves a line for the local
    name.
  - A tiny-house code path. There is none at state level — see the closing
    section, which says so rather than implying a workaround exists.
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

FORM_ID = "AR.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Forms & Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document you will meet — what it is, when it happens, and which "
    "office it comes from.")

flow.append(k.disclaimer(
    "State form numbers were current in September 2026. Local forms are named "
    "by each jurisdiction and are not listed here."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- state forms
flow += k.h2_tight("THE STATE DOCUMENTS", reserve=2.2)
flow.append(k.body(
    "These exist wherever you build in Arkansas. Note how few there are — and "
    "that the septic application is doing most of the work."))
rows = [
    [k.cellp("<b>Form EHP-19</b><br/>Individual Onsite Wastewater System "
             "Permit Application"),
     k.cellp("The septic application, and the single most important piece of "
             "paper on a rural Arkansas build. Three parts: <b>Part I</b> the "
             "Permit for Construction, completed by your Designated "
             "Representative; <b>Part II</b> the installation inspection; "
             "<b>Part III</b> the Permit for Operation. You sign item 19, the "
             "Utilization Verification, attesting bedroom count and square "
             "footage — get it right, it sizes the system"),
     k.cellp("Department of Health, through your county health unit")],
    [k.cellp("<b>Site plan</b><br/>Onsite Wastewater Rules, Appendix F"),
     k.cellp("Drawn as part of the septic application and more demanding than "
             "people expect. It has to show dimensioned property lines with "
             "the system tied to two of them, every setback distance, the well "
             "location and elevation, all wells and systems on adjoining "
             "property within 100 feet, the flagged percolation holes, and the "
             "flagged corners of <b>both</b> the primary and secondary "
             "absorption areas"),
     k.cellp("Prepared by your Designated Representative")],
    [k.cellp("<b>Well construction report</b><br/>17 CAR § 11-401"),
     k.cellp("Filed by whoever constructed the well within <b>90&#160;days</b>, "
             "carrying the longitude and latitude. \"A copy of the "
             "construction report shall be provided to the customer upon "
             "demand\" (§ 11-403) — so demand it. It is your only record of "
             "depth, casing and static water level, and a buyer's surveyor "
             "will ask for it"),
     k.cellp("Arkansas Natural Resources Commission, Department of "
             "Agriculture")],
    [k.cellp("<b>Notice to Owner</b><br/>Ark. Code Ann. § 18-44-115"),
     k.cellp("A lien notice, and it protects <b>you</b>. On residential "
             "property of four or fewer units no lien may be acquired unless "
             "the owner received this notice, and \"no lien may be claimed by "
             "any subcontractor, laborer, material supplier, or other lien "
             "claimant unless the owner… has received at least one (1) copy\". "
             "The residential contractor's duty is to give it before work "
             "starts"),
     k.cellp("From your contractor — keep it")],
    [k.cellp("<b>Stormwater coverage</b><br/>Permit ARR150000"),
     k.cellp("Only if total disturbance reaches one acre. Between one and five "
             "acres coverage is automatic with documents posted on site; at "
             "five acres and above a Notice of Intent is filed"),
     k.cellp("Division of Environmental Quality")],
    [k.cellp("<b>Access driveway permit</b>"),
     k.cellp("Needed where the driveway meets a <b>state highway</b>. A county "
             "road goes through the county Road Department instead, and a city "
             "street through the city"),
     k.cellp("Department of Transportation")],
    [k.cellp("<b>Homestead property tax credit</b>"),
     k.cellp("Filed after the build, with your county assessor — not with the "
             "state. The deadline is <b>15 October</b>. New construction goes "
             "on the assessment rolls without you doing anything; the credit "
             "does not"),
     k.cellp("County assessor")],
]
flow.append(k.ref_table(
    "What exists statewide",
    [k.cellp("Document", bold=True), k.cellp("What it is", bold=True),
     k.cellp("From", bold=True)],
    rows, [1.65 * inch, CW - 3.35 * inch, 1.7 * inch]))

# ---------------------------------------------------------------- local forms
flow += k.h2_tight("THE LOCAL DOCUMENTS — IF THEY EXIST WHERE YOU ARE",
                   reserve=2.2)
flow.append(k.body(
    "Every one of these is named by the office that issues it, so this table "
    "gives you the function and a line to write down what your jurisdiction "
    "calls it. In much of unincorporated Arkansas several of these rows will "
    "correctly read <b>none</b>."))
flow += k.check_table(
    "Write in the local name, or NONE",
    [
        ("<b>Building permit application</b> — exists only where a city or "
         "county created one", [("Local name", 0.65), ("Fee", 0.35)]),
        ("<b>Site or plot plan</b> to the local standard, which may differ "
         "from the septic site plan", [("Requirements", 1.0)]),
        ("<b>Electrical permit</b> — local option under § 17-28-305(c)",
         [("Local name", 0.65), ("Fee", 0.35)]),
        ("<b>Plumbing permit</b> — mandatory where a water, sewer or gas "
         "utility system exists (§ 17-38-204(c))",
         [("Issuing body", 0.65), ("Fee", 0.35)]),
        ("<b>Mechanical and gas permits</b>",
         [("Local name", 0.65), ("Fee", 0.35)]),
        ("<b>Floodplain development permit</b> — or the exemption certificate "
         "confirming you are outside the hazard area",
         [("Office", 0.65), ("Ref.", 0.35)]),
        ("<b>911 address assignment</b>", [("Office", 0.65), ("Ref.", 0.35)]),
        ("<b>Driveway or culvert permit</b> — county road or city street",
         [("Office", 0.65), ("Fee", 0.35)]),
        ("<b>Water tap and meter</b>, or the well",
         [("Provider", 0.65), ("Fee", 0.35)]),
        ("<b>Sewer connection</b>, if a main is within 300 feet — in which "
         "case connection is mandatory and no septic system may be used",
         [("Provider", 0.65), ("Fee", 0.35)]),
        ("<b>Certificate of occupancy</b> — AFPC Vol. III § R110, issued only "
         "where a permit program exists", [("Issued?", 1.0)]),
    ])

# ---------------------------------------------------------------- no permit
flow += k.h2_tight("WHAT NEEDS NO PERMIT AT ALL", reserve=2.2)
flow.append(k.body(
    "Even inside a city that permits everything, the code exempts a specific "
    "list of work. Arkansas adopted this list <b>unamended</b>, so it is the "
    "same wherever you are. It is worth reading before you apply for anything, "
    "because several of these are the outbuildings people assume they must "
    "permit."))
rows = [
    [k.cellp("Detached one-story accessory structures"),
     k.cellp("<b>200 sq ft</b> or less of floor area — the shed, the pump "
             "house, the small shop")],
    [k.cellp("Fences"), k.cellp("Not over <b>7 feet</b> high")],
    [k.cellp("Retaining walls"),
     k.cellp("Not over <b>4 feet</b> measured from the bottom of the footing "
             "to the top of the wall, unless supporting a surcharge")],
    [k.cellp("Water tanks"),
     k.cellp("Supported directly on grade, capacity <b>5,000 gallons</b> or "
             "less, with a height-to-diameter ratio no greater than 2 to 1")],
    [k.cellp("Sidewalks and driveways"),
     k.cellp("Though the connection to a public road is a separate permit — "
             "see the access driveway row above")],
    [k.cellp("Painting, papering, tiling, carpeting, cabinets, counters"),
     k.cellp("Finish work generally")],
    [k.cellp("Prefabricated swimming pools"),
     k.cellp("Less than <b>24 inches</b> deep")],
    [k.cellp("Swings and other playground equipment"), k.cellp("")],
    [k.cellp("Window awnings"),
     k.cellp("Projecting no more than <b>54 inches</b>, supported by an "
             "exterior wall")],
    [k.cellp("Decks"),
     k.cellp("Not exceeding <b>200 sq ft</b>, not more than <b>30 inches</b> "
             "above grade at any point, not attached to a dwelling, and not "
             "serving the required exit door")],
]
flow.append(k.ref_table(
    "Exempt from permit — AFPC Volume III § R105.2",
    [k.cellp("Work", bold=True), k.cellp("Limit", bold=True)],
    rows, [2.45 * inch, CW - 2.45 * inch]))
flow.append(k.cite(
    "Read September 2026 and confirmed unamended by Arkansas. Two cautions. "
    "<b>Exempt from permit is not exempt from the code</b> — § R105.2 says so "
    "in terms, and the structure still has to be built to standard. And the "
    "exemption is from the <i>building</i> permit only: a shed still has to "
    "respect your septic setbacks, and a deck near the absorption field still "
    "has to keep its distance."))

# ---------------------------------------------------------------- not adopted
flow += k.h2_tight("WHAT ARKANSAS NEVER ADOPTED", reserve=2.2)
flow.append(k.body(
    "This is the shortest section in the kit and it saves the most wasted "
    "effort. Arkansas struck <b>every appendix</b> out of its residential "
    "code: appendices \"are NOT adopted by the State of Arkansas and shall not "
    "apply unless adopted by local ordinance\" (§ R102.5). Among the things "
    "that removes from the state code:"))
flow.append(k.bullet(
    "<b>Tiny houses.</b> The IRC's tiny-house appendix — the one that permits "
    "reduced ceiling heights, ladders and loft stairs — is not adopted. "
    "Without it a dwelling in Arkansas meets the full residential code, or it "
    "meets a local ordinance that adopted the appendix."))
flow.append(k.bullet(
    "<b>Strawbale, cob, light straw-clay and 3D-printed construction.</b> Each "
    "has an IRC appendix; none is adopted here. There is no state code path "
    "for these methods, which is not the same as a ban — it means you and an "
    "engineer will be designing to the performance requirements of the main "
    "code instead."))
flow.append(k.bullet(
    "<b>Radon control, solar-ready provisions, and the private sewage "
    "appendix.</b> The last of these matters least, because Arkansas replaced "
    "it explicitly: the code's own cross-reference table says the "
    "international private sewage code \"is replaced by\" the Department of "
    "Health's onsite wastewater rules."))
flow.append(k.callout(
    "If you are building anything unusual, start here", [
        Paragraph("Take the appendix question to your building official — or, "
                  "if there is no building official, to the engineer who will "
                  "stamp your design — <b>before you draw anything</b>. A "
                  "local jurisdiction can adopt an appendix by ordinance, so "
                  "the answer genuinely differs by jurisdiction, and it is a "
                  "cheap question to ask early and an expensive one to "
                  "discover late.", S["body"]),
    ]))

flow += k.h2_tight("THE ONE THING YOU MAY NOT DO YOURSELF", reserve=1.8)
flow.append(k.body(
    "Arkansas is unusually generous to the owner-builder. You may build your "
    "own house without a license. You may install your own septic system. You "
    "may drill your own well. Against that, one clear prohibition is worth "
    "restating on its own, because it surprises people who have read the "
    "rest:"))
flow.append(k.callout(
    "You cannot design your own septic system", [
        Paragraph("\"Part I of the Permit Application form <b>shall be "
                  "completed by a Designated Representative</b> and approved "
                  "by the Department or its Authorized Agent prior to "
                  "initiating construction\" — Onsite Wastewater Rules "
                  "§ 4.10.1. The Designated Representative is a private "
                  "licensed professional, not a state employee, and you hire "
                  "them. The same rule adds, in capitals: <b>no changes or "
                  "alterations may be made to the system prior to or during "
                  "construction without prior approval of the Authorized "
                  "Agent.</b>", S["body"]),
        Paragraph("Installing it yourself afterwards is a different question, "
                  "and the statute preserves that right — the homeowner "
                  "retains \"all rights to install and repair his system\" "
                  "(§ 14-236-102(b)(2)). Confirm with your county "
                  "Environmental Health Specialist how they want a "
                  "homeowner-installed system documented, because the field "
                  "practice is not written down anywhere.", S["body"]),
    ]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ar-permit-kit",
                       "AR.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
