#!/usr/bin/env python3
"""ID.5 Forms & Documents Index.

Every document an owner-builder will meet in Idaho, named as the agency names
it, with what it is, when it happens and where it comes from.

Two negative sections carry real weight here. "What needs no permit at all"
saves people from applying for things that do not exist. "What Idaho does not
require" exists because owner-builders arriving from other states routinely
budget for a blower door, whole-house AFCI, a surge device and residential
sprinklers, none of which Idaho demands — and because "not for sale, rent, or
lease" is not a thing you will be asked to sign.

Verified sources:
  DOPL Homeowner Electrical Permit Application (rev. 9/13/2022), Homeowner
    Plumbing Permit Application + Plumbing Permit Worksheet (rev. 8/17/2022),
    Homeowner HVAC Permit Application + fee schedule (rev. 8/17/2022)
                        the certification; "purchased Online at DBS.IDAHO.GOV";
                        "not an inspection request"; the fee worksheets
  DOPL electrical FAQ   the orange Job Identification Sticker; sticker colors;
                        the Enforcement Permit at double fee
  DOPL Plan Review Application (rev. 9/12/2023)   "DOPL does NOT issue
                        building permits for projects not owned by the State"
  § 54-5209             "no contractor registration provided" on the permit face
  IDAPA 58.01.03.005.07, .005.08, .011.05   "Individual and Subsurface System
                        Installation Permit"; two years; the as-built
  IDAPA 58.01.14.110.04   $400 / $300 / $40 minimum fees
  § 42-235; IDAPA 37.03.09.010.49   drilling permit, $75; the Start Card
  § 42-238(11)          well driller's report, 30 days
  § 55-2505(12), § 55-2508   property condition disclosure; new-house exemption
  IDAPA 24.39.30.600.03.b-c   R105.2 as amended (pools 4 ft; flag poles)
  § 54-2621             plumbing: no permit to clear stoppages or repair leaks
  § 54-5016(1)          HVAC: no permit for repair or maintenance
  § 39-4116(3), (5)     sprinklers; agricultural buildings
  § 39-4109B            EV infrastructure may not be required
  IDAPA 24.39.30.600.06.e   visual inspection in lieu of blower door
  IDAPA 24.39.10.600.01.k, .n, .o, .r   AFCI bedrooms only; SPD and emergency
                        disconnect permissive
  IDAPA 58.01.03.006.08.b   owner may install own standard septic system
  § 42-238(2), (3)      no owner may drill a well

DELIBERATELY NOT CLAIMED:
  - A form number for any local building permit or owner-builder declaration.
    Those vary by jurisdiction; the document gives write-in lines.
  - The septic permit's application form name. Districts use their own; the
    permit the rule names is printed instead.
  - Whether IRC Part IX appendices (radon, tiny houses) bind. Unresolved.
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

FORM_ID = "ID.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Forms & Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document you will meet, named as the agency names it — and the "
    "things Idaho never asks you for.")

flow.append(k.disclaimer(
    "Form names, revision dates and fees were read from the agencies' own "
    "current forms in September 2026. Where no form number is published, this "
    "document says so rather than inventing one."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- state docs
flow += k.h2_tight("THE STATE DOCUMENTS", reserve=2.4)
rows = [
    [k.cellp("<b>Application for Homeowner Permit — Electrical</b><br/>"
             "DOPL, rev. 9/13/2022"),
     k.cellp("The homeowner's own electrical permit. \"As of January 1, "
             "2023, all permits will need to be purchased Online at "
             "DBS.IDAHO.GOV\" — the paper form shows you the fields and the "
             "certification you will click through. \"This permit "
             "application is not an inspection request\""),
     k.cellp("$130–$325 by living space; $65 per inspection on an existing "
             "dwelling")],
    [k.cellp("<b>Application for Homeowner Permit — Plumbing</b>, with the "
             "<b>Plumbing Permit Worksheet</b><br/>DOPL, rev. 8/17/2022"),
     k.cellp("Same certification. The worksheet is the fee schedule and "
             "carries the definition that matters: living space \"utilized "
             "for sleeping, eating, cooking, bathing, washing, recreation, "
             "and sanitation purposes. An unfinished basement is considered "
             "part of the living space\""),
     k.cellp("$130–$325 by living space; $65 sewer and water lines if "
             "inspected together")],
    [k.cellp("<b>Application for Homeowner Permit — HVAC</b>, with the "
             "<b>Homeowner HVAC Permit Fee Schedule</b><br/>DOPL, rev. "
             "8/17/2022"),
     k.cellp("Same certification. The fee schedule is where the <b>Manual "
             "S, J and D review</b> line lives — \"required when installing "
             "the primary heating and/or cooling system in a NEW single or "
             "two-family dwelling\" — so the load, equipment and duct "
             "calculations travel with the application"),
     k.cellp("$100 base + per appliance and duct; $25 review")],
    [k.cellp("<b>Job Identification Sticker</b><br/>DOPL"),
     k.cellp("The orange sticker that marks the permitted job site; print "
             "one with an online permit and the inspector replaces it on the "
             "first visit. Yellow is a Correction Sticker. An <b>Enforcement "
             "Permit</b> — issued only by an inspector, only for work done "
             "without a permit — costs double"),
     k.cellp("Included with the permit")],
    [k.cellp("<b>Plan Review Application</b><br/>DOPL, rev. 9/12/2023"),
     k.cellp("<b>Not yours</b> — printed here because it is the document "
             "that settles the central question: \"DOPL does NOT issue "
             "building permits for projects not owned by the State. Contact "
             "the local government for these projects\""),
     k.cellp("—")],
    [k.cellp("<b>Individual and Subsurface System Installation Permit</b>"
             "<br/>Public health district"),
     k.cellp("The septic permit, by the rule's own name (IDAPA "
             "58.01.03.005.07). Invalid if not \"completed and approved "
             "within two (2) years\" (005.08). Ends with the district's "
             "<b>as-built drawing</b>, sent to you within 30 days of the "
             "final (011.05) — keep it with the deed"),
     k.cellp("$400 minimum; $300 tank only; $40 renewal (58.01.14.110.04); "
             "districts may differ")],
    [k.cellp("<b>Drilling permit</b> — and the <b>Start Card</b><br/>IDWR"),
     k.cellp(f"Required \"prior to beginning construction of any well\" "
             f"({sec('42-235')}). The rules define a \"Start Card\" as \"an "
             f"expedited drilling permit process for the construction of "
             f"cold water, single-family residential wells\" (IDAPA "
             f"37.03.09.010.49) — ask the driller which route applies"),
     k.cellp("$75 domestic")],
    [k.cellp("<b>Well driller's report</b><br/>IDWR"),
     k.cellp(f"The driller's log and report, filed \"within thirty (30) days "
             f"following the completion of the well\" ({sec('42-238(11)')}). "
             f"Searchable afterwards in IDWR's well-log search. <b>Get a "
             f"copy</b> — it is the well's only record"),
     k.cellp("Filed by the driller")],
    [k.cellp("<b>Property condition disclosure form</b><br/>"
             f"{sec('55-2508')}"),
     k.cellp(f"Required on a sale of a 1–4 unit residence — but a "
             f"never-inhabited new house is exempt except for \"annexation "
             f"and city service status\" ({sec('55-2505(12)')}). Live in it "
             f"first and the whole form applies later, including whether "
             f"work was done \"without a building permit\""),
     k.cellp("At sale")],
]
flow.append(k.ref_table(
    "What the state and its districts issue, and what it costs",
    [k.cellp("Document", bold=True), k.cellp("What it is", bold=True),
     k.cellp("Fee", bold=True)],
    rows, [1.8 * inch, CW - 1.8 * inch - 1.4 * inch, 1.4 * inch]))
flow.append(k.cite(
    "<b>The certification on all three homeowner forms, verbatim:</b> \"I "
    "certify that I am the owner of the residential property and will "
    "personally perform the work covered by this permit. I recognize this "
    "permit is only valid for work on a primary or secondary residence and "
    "associated outbuildings not used for commercial purposes or rented by a "
    "tenant. By signing this, I accept responsibility for all the work being "
    "performed, and understand that all work must be inspected by the "
    "Division of Occupational and Professional Licensing.\" Nothing about "
    "sale. Nothing about lease."))

# ---------------------------------------------------------------- local docs
flow += k.h2_tight("THE LOCAL DOCUMENTS — IF THEY EXIST WHERE YOU ARE",
                   reserve=1.8)
flow.append(k.body(
    "In an enforcing jurisdiction the city or county issues its own paperwork "
    "under its own names, and there is no statewide vocabulary for it. Write "
    "in what yours calls them."))
flow += k.check_table(
    "What my jurisdiction calls each document",
    [
        ("<b>Permit-process document</b> under § 39-4117(1) — the one that "
         "proves a building code is enforced. Where I found it:",
         [("Location / URL", 1.0)]),
        ("<b>Building permit application</b>, and whether there is a separate "
         "homeowner or owner-builder version:",
         [("Called", 0.6), ("Separate form?", 0.4)]),
        ("<b>Contractor-registration exemption declaration.</b> No state form "
         "exists; the statute requires only \"no contractor registration "
         "provided\" on the permit face (§ 54-5209). Mine is called:",
         [("Called", 1.0)]),
        ("<b>Zoning or land-use permit</b>, if separate:",
         [("Called", 0.6), ("Issued by", 0.4)]),
        ("<b>Driveway approach / encroachment permit</b>:",
         [("Called", 0.6), ("Road authority", 0.4)]),
        ("<b>911 address application</b>:",
         [("Called", 0.6), ("Issued by", 0.4)]),
        ("<b>Floodplain development permit</b>, if in a mapped hazard area:",
         [("Called", 0.6), ("Administrator", 0.4)]),
        ("<b>Certificate of occupancy</b> — ask whether one is issued, "
         "because where no code is enforced there is none:",
         [("Answer", 1.0)]),
    ])

# ---------------------------------------------------------------- no permit
flow += k.h2_tight("WHAT NEEDS NO PERMIT AT ALL", reserve=2.0)
flow.append(k.body(
    "<b>Building</b> — only meaningful in an enforcing jurisdiction, and "
    "Part I is locally amendable, so confirm. Idaho keeps IRC R105.2's list "
    "and amends two items (IDAPA 24.39.30.600.03.b–c):"))
rows = [
    [k.cellp("<b>Accessory structures</b>"),
     k.cellp("One-story detached, not over 200&#160;sq&#160;ft")],
    [k.cellp("<b>Fences, walls</b>"),
     k.cellp("Fences not over 7&#160;ft; retaining walls not over 4&#160;ft "
             "unless supporting a surcharge")],
    [k.cellp("<b>Pools</b>"),
     k.cellp("Prefabricated pools \"less than <b>four (4) feet</b>\" deep — "
             "Idaho replaced the model code's 24 inches")],
    [k.cellp("<b>Flag poles</b>"),
     k.cellp("Added by Idaho as item 11")],
    [k.cellp("<b>Decks, walks, drives, paint</b>"),
     k.cellp("Decks not over 200&#160;sq&#160;ft and not more than "
             "30&#160;in above grade; sidewalks and driveways; painting, "
             "papering, tiling, cabinets, counters")],
]
flow.append(k.ref_table(
    "IRC R105.2 as Idaho adopted it",
    [k.cellp("What", bold=True), k.cellp("The condition", bold=True)],
    rows, [1.9 * inch, CW - 1.9 * inch]))
flow.append(k.body(
    f"<b>Trades</b> — statewide. Plumbing: no permit \"for the clearing of "
    f"stoppages or repairing of leaks\" with no rearrangement of pipes or "
    f"fixtures ({sec('54-2621')}). HVAC: \"no permit shall be required to "
    f"perform work related to repair or maintenance of an existing HVAC "
    f"system\" ({sec('54-5016(1)')}). Electrical: <b>no equivalent</b> — the "
    f"chapter has no repair exception and no farm-building exception. "
    f"<b>Agricultural buildings</b> are exempt from the building codes, but "
    f"\"a place of human habitation, which means a space in a building for "
    f"living, sleeping, or cooking\" is not an agricultural building "
    f"({sec('39-4116(5)')}), and the plumbing and HVAC farm-building "
    f"exceptions carry the same carve-out."))

# ---------------------------------------------------------------- never
flow += k.h2_tight("WHAT IDAHO DOES NOT REQUIRE", reserve=2.2)
flow.append(k.body(
    "Worth knowing because owner-builders arriving from other states routinely "
    "budget for these. In Idaho none of them is mandatory — and on the first "
    "four no city or county may add them."))
flow.append(k.bullet(
    f"<b>Residential fire sprinklers.</b> Exempted by statute for one- and "
    f"two-family dwellings; R313.2 deleted from the code "
    f"({sec('39-4116(3)')})."))
flow.append(k.bullet(
    "<b>A blower-door test.</b> \"A visual inspection shall be considered "
    "acceptable in lieu of testing\" — the permit holder chooses at "
    "application (IDAPA 24.39.30.600.06.e). No local energy requirement may "
    f"differ from the state code ({sec('39-9701(2)')})."))
flow.append(k.bullet(
    "<b>Whole-house AFCI, a surge-protective device, an outdoor emergency "
    "disconnect.</b> AFCI applies to bedroom circuits only; the SPD and the "
    "emergency disconnect \"shall be permitted\" (IDAPA 24.39.10.600.01.k, "
    ".n, .o, .r)."))
flow.append(k.bullet(
    f"<b>EV charging infrastructure.</b> Neither the state nor any local "
    f"government may require a charging station, EV parking space or upgraded "
    f"conduit in a building plan ({sec('39-4109B')})."))
flow.append(k.bullet(
    "<b>A \"not for sale, rent or lease\" affidavit.</b> The words are on no "
    "statute, rule or form. The DOPL certification is \"will personally "
    "perform the work\" and \"not used for commercial purposes or rented by "
    "a tenant.\""))
flow.append(k.bullet(
    f"<b>A statewide snow load, frost depth or seismic category.</b> None "
    f"exists; IRC R301 design criteria are the county's to set "
    f"({sec('39-4116(4)(c)(iii)')}). The one statewide depth is the "
    f"42-inch water-service cover (IDAPA 24.39.20.600.21)."))
flow.append(k.bullet(
    "<b>A residential building permit from the state.</b> DOPL issues none. "
    "Where no local code is adopted, there is no building permit to apply "
    "for."))
flow.append(k.cite(
    "<b>One thing Idaho does require that other states do not:</b> "
    "whole-house mechanical ventilation in every new dwelling, whatever the "
    "air-leakage result (IDAPA 24.39.30.600.03.h). And a pre-plumbed water "
    "softener loop in every new house on a slab or with a finished basement "
    "(IDAPA 24.39.20.600.26)."))

# ---------------------------------------------------------------- the one thing
flow += k.h2_tight("THE ONE THING YOU MAY NOT DO YOURSELF", reserve=1.8)
flow.append(k.body(
    "Idaho is generous about owner-performed work. You may act as your own "
    "contractor, wire your own house, do your own plumbing and HVAC on "
    "homeowner permits, and install your own standard septic system. "
    "<b>You may not drill your own well.</b>"))
flow.append(k.callout(
    "The definition that closes the door", [
        Paragraph(f"\"It shall be unlawful for any person to drill a well in "
                  f"Idaho, including wells excepted under sections 42-227 and "
                  f"42-228, Idaho Code, without first complying with the "
                  f"provisions of this chapter\" ({sec('42-238(2)')}) — and "
                  f"\"a 'person' shall be defined as <b>any individual who "
                  f"drills or abandons any well for himself or another</b> in "
                  f"this state\" ({sec('42-238(3)')}). The chapter then "
                  f"requires a driller's license, an examination, references "
                  f"and a bond. IDWR's own page: \"All wells must be "
                  f"constructed by a well driller with a valid license from "
                  f"IDWR.\" Contrast the septic rule, which says in so many "
                  f"words that an installer's permit \"is not required for … "
                  f"owners installing their own standard or basic alternative "
                  f"system\" (IDAPA 58.01.03.006.08.b). The well is the "
                  f"exception, and it is written without one.", S["body"]),
    ]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "id-permit-kit",
                       "ID.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
