#!/usr/bin/env python3
"""SC.5 Forms & Documents Index.

Every document an owner-builder meets in South Carolina, named the way the
office that issues it names it, in the order the job produces them.

Carries two things that do not fit anywhere else:
  - § 40-59-265 in full. It is a statewide, statutory list of work that needs
    no building permit and no credential, enacted by 2022 Act No. 186. Most
    states leave that list to the local code official; South Carolina put it
    in the licensing chapter, where nobody looks for it.
  - The "deliberately not printed" page. Fees, review times and cost ranges
    are the most-requested and least-durable numbers in this subject, and a
    printed guess is worth less than a blank line with the right question
    beside it.
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
NB = k.NB
sec = k.sec

FORM_ID = "SC.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Documents"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "Every document you will meet, what it does, when it is due, "
                 "and which office it comes from.")
flow.append(k.disclaimer())

# ------------------------------------------------------------- the index
flow += k.h2_tight("THE DOCUMENTS, IN THE ORDER YOU MEET THEM", reserve=2.2)
rows = [
    [k.cellp("<b>Owner-builder disclosure statement</b>"),
     k.cellp("The statement the permitting agency must give you, whose "
             f"wording {sec('40-59-260')}(C) prints. Read it: it may say more "
             f"than the statute does."),
     k.cellp("At the counter, when you sign"),
     k.cellp("Building department")],
    [k.cellp("<b>Building permit application</b>"),
     k.cellp("You must <b>personally appear and sign</b> it to claim the "
             "exemption. Chapter 11 separately requires an exempt owner to "
             "list the name and license number of every licensed contractor "
             f"on the project ({sec('40-11-420')}(C))."),
     k.cellp("Before work"),
     k.cellp("Building department")],
    [k.cellp("<b>Register-of-deeds notice forms</b>"),
     k.cellp("The agency must give you “all forms necessary” for the "
             f"{sec('40-59-260')}(E) filing at the moment you sign. Ask for "
             f"them by name."),
     k.cellp("Same visit"),
     k.cellp("Building department")],
    [k.cellp("<b>Septic construction permit</b>"),
     k.cellp("Site evaluation and permit for an onsite wastewater system. "
             "Several counties will not issue a building permit without a "
             "copy."),
     k.cellp("Before the permit"),
     k.cellp("SCDES")],
    [k.cellp("<b>Well permit</b>"),
     k.cellp("For a private drinking water well. Different bureau from "
             "septic, same agency."),
     k.cellp("Before drilling"),
     k.cellp("SCDES")],
    [k.cellp("<b>Critical area or beachfront authorization</b>"),
     k.cellp("A separate state approval for coastal parcels. Nobody local "
             "will chase it for you."),
     k.cellp("Before the permit"),
     k.cellp("SCDES Coastal")],
    [k.cellp("<b>Plat or survey</b>"),
     k.cellp("Richland County, among others, asks for a copy of the property "
             "plat at application. Also how you prove setbacks."),
     k.cellp("At application"),
     k.cellp("Surveyor")],
    [k.cellp("<b>Construction drawings and site plan</b>"),
     k.cellp("To your office's scale and content rules. The design criteria "
             "on SC.2 belong on the drawings."),
     k.cellp("At application"),
     k.cellp("You or your designer")],
    [k.cellp("<b>Farm structure affidavit</b>"),
     k.cellp(f"Only if you are building a barn or shed under "
             f"{sec('6-9-65')}, and it must be filed <b>before</b> "
             f"construction to work at all."),
     k.cellp("Before that build"),
     k.cellp("Building department")],
    [k.cellp("<b>Notice of Project Commencement</b>"),
     k.cellp("Optional, $15, and it preserves the statutory cap on "
             "second-tier liens. Fifteen days from starting work."),
     k.cellp("Within 15 days of start"),
     k.cellp("Clerk of court or register of deeds")],
    [k.cellp("<b>Location notice at the job site</b>"),
     k.cellp("Posted if a Notice of Project Commencement is filed, carrying "
             "the wording the statute prescribes, along with the contractor's "
             "name and address."),
     k.cellp("With the above"),
     k.cellp("You post it")],
    [k.cellp("<b>Truss design drawings</b>"),
     k.cellp("Must arrive with the truss shipment and be given to the "
             "building official at the time of inspection. Twelve enumerated "
             "contents."),
     k.cellp("At delivery and at framing"),
     k.cellp("Truss supplier")],
    [k.cellp("<b>Termite treatment record</b>"),
     k.cellp("Establish early who produces it and who wants to see it. The "
             "state code's added treatment route runs through the Clemson "
             "University Department of Pesticide Regulation."),
     k.cellp("Before slab or backfill"),
     k.cellp("Treatment provider")],
    [k.cellp("<b>Energy compliance documentation</b>"),
     k.cellp("To the <b>2009 IECC</b>, which is the Energy Standard set by "
             "statute — not to the residential code's energy chapter, which "
             "South Carolina does not adopt."),
     k.cellp("As your office requires"),
     k.cellp("You or your designer")],
    [k.cellp("<b>Elevation certificate</b>"),
     k.cellp("If the parcel is in a mapped flood hazard area. Coastal A Zones "
             "are inside the state's flood provisions."),
     k.cellp("As required"),
     k.cellp("Surveyor")],
    [k.cellp("<b>Certificate of occupancy</b>"),
     k.cellp("Required before occupancy, and statutory proof of substantial "
             "completion — which starts the eight-year repose clock."),
     k.cellp("At the end"),
     k.cellp("Building department")],
    [k.cellp("<b>Register-of-deeds notice</b>"),
     k.cellp("The filing stating the structure “was constructed by the owner "
             "as an unlicensed builder.” <b>Failure to file revokes the "
             "exemption.</b> Some counties record it at the front of the job "
             "instead."),
     k.cellp("Promptly after — or before the permit, locally"),
     k.cellp("Register of deeds")],
]
flow.append(k.ref_table(
    "The document trail, start to finish",
    [k.cellp("Document", bold=True), k.cellp("What it is", bold=True),
     k.cellp("When", bold=True), k.cellp("From", bold=True)],
    rows, [1.55 * inch, CW - 4.55 * inch, 1.35 * inch, 1.65 * inch]))

# ------------------------------------------------------- no permit list
flow += k.h2("WORK THAT NEEDS NO PERMIT AND NO CREDENTIAL")
flow.append(k.body(
    f"Most states leave this list to the local code official. South Carolina "
    f"wrote it into the licensing chapter, where nobody looks: "
    f"{sec('40-59-265')}, added by 2022 Act No.&#160;186 effective "
    f"16&#160;May&#160;2022. Subsection (B) is the operative sentence — the "
    f"listed improvements “are exempt from building permit application "
    f"requirements and an owner of residential property who makes these "
    f"improvements is not required to have a residential builder or "
    f"residential specialty contractor's license or be subject to the "
    f"penalties provided in this chapter.”"))
rows = [
    [k.cellp("<b>Building</b>"),
     k.cellp("One-story detached accessory structures with floor area not "
             "exceeding <b>200&#160;square feet</b> · fences not over "
             "<b>7&#160;feet</b> high · retaining walls not over "
             "<b>4&#160;feet</b> measured from the bottom of the footing to "
             "the top of the wall, unless supporting a surcharge · water "
             "tanks supported directly on grade with capacity not exceeding "
             "<b>5,000&#160;gallons</b> and a height-to-width ratio not "
             "exceeding <b>2:1</b> · sidewalks and driveways · painting, "
             "papering, tiling, carpeting, cabinets, counter tops and similar "
             "finish work · prefabricated swimming pools less than "
             "<b>24&#160;inches</b> deep · swings and other playground "
             "equipment · window awnings on an exterior wall projecting not "
             "more than <b>54&#160;inches</b> and needing no additional "
             "support · decks not exceeding <b>200&#160;square feet</b> and "
             "not more than <b>30&#160;inches</b> above grade at any point")],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("Listed cord-and-plug connected temporary decorative lighting · "
             "reinstallation of attachment plug receptacles but not the "
             "outlets · replacement of branch circuit overcurrent devices of "
             "the required capacity in the same location · wiring, devices, "
             "appliances or equipment operating at less than "
             "<b>25&#160;volts</b> and not capable of supplying more than "
             "<b>50&#160;watts</b> · minor repair work including lamp "
             "replacement and connecting approved portable equipment to "
             "approved permanently installed receptacles")],
    [k.cellp("<b>Gas</b>"),
     k.cellp("Portable heating, cooking or clothes drying appliances · "
             "replacement of a minor part that does not alter approval of "
             "equipment or make it unsafe · portable fuel-cell appliances not "
             "connected to a fixed piping system and not interconnected to a "
             "power grid")],
    [k.cellp("<b>Mechanical</b>"),
     k.cellp("Portable heating, ventilation and cooling appliances · steam, "
             "hot- or chilled-water piping within regulated heating or "
             "cooling equipment · replacement of a minor part · portable "
             "evaporative coolers · self-contained refrigeration systems "
             "containing <b>10&#160;pounds</b> or less of refrigerant or "
             "actuated by motors of <b>1&#160;horsepower</b> or less · "
             "portable fuel-cell appliances")],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp("Stopping leaks in drains, water, soil, waste or vent pipe — but "
             "“if any concealed trap, drainpipe, water, soil, waste or vent "
             "pipe becomes defective and it becomes necessary to remove and "
             "replace the same with new material, such work must be "
             "considered as <b>new work</b> and a permit must be obtained” · "
             "clearing stoppages, repairing leaks in pipes, valves or "
             "fixtures, and removing and reinstalling water closets, provided "
             "the repairs do not involve replacing or rearranging valves, "
             "pipes or fixtures")],
]
flow.append(k.ref_table(
    f"S.C. Code Ann. {sec('40-59-265')}(A) — the statewide list",
    [k.cellp("", bold=True), k.cellp("Exempt work", bold=True)],
    rows, [1.05 * inch, CW - 1.05 * inch]))
flow.append(k.cite(
    "Two cautions. This is an exemption from the <b>permit</b> and from "
    "<b>Chapter 59 licensing</b>. It is not an exemption from zoning, from "
    "setbacks, from a homeowners' association, or from the flood ordinance — "
    "and a 200-square-foot shed still has to sit where your zoning lets it "
    "sit. Second: your local office may publish its own exempt-work list. "
    "Oconee County does. Where the two differ, the statute is the floor and "
    "the local list is what the counter will actually apply, so ask."))

# ------------------------------------------------------ records to keep
flow += k.h2_tight("THE RECORDS TO KEEP, AND FOR HOW LONG", reserve=2.0)
flow.append(k.body(
    f"South Carolina's outside limit on construction-defect claims is "
    f"<b>eight years</b> from substantial completion ({sec('15-3-640')}), and "
    f"your certificate of occupancy is what proves that date. Keep the "
    f"following together for at least that long — the file is also what "
    f"answers a buyer who finds your register-of-deeds notice in the title "
    f"search."))
flow += k.check_table(
    "The file",
    [
        ("The permit card or printout, with the issuance date legible — it "
         "fixes your code edition", [("Permit no.", 1.0)]),
        ("Approved plans as stamped, and any revisions approved during the "
         "build", []),
        ("Every inspection result, including the ones that failed and the "
         "correction that followed", []),
        ("The signed owner-builder disclosure statement", []),
        ("The recorded register-of-deeds notice, with its book and page",
         [("Book / page", 1.0)]),
        ("Certificate of occupancy", [("Date", 1.0)]),
        ("Septic permit and final approval; well completion record and water "
         "test results", []),
        ("Truss design drawings and any engineered element calculations", []),
        ("Termite treatment record and warranty", []),
        ("Every contractor's license or registration number, captured at the "
         "time you hired them", []),
        ("Lien waivers or receipts for everyone you paid", []),
        ("Any written answer an office gave you — wind speed, seismic "
         "category, exempt-work list, homeowner trade permits", []),
    ])

# --------------------------------------------------- what is not printed
flow += k.h2("WHAT THIS KIT DELIBERATELY DOES NOT PRINT")
flow.append(k.body(
    "Some numbers are asked for constantly and cannot honestly be printed in "
    "a document that will sit in a binder for a year. Here is what was left "
    "out, why, and the question to ask instead."))
rows = [
    [k.cellp("<b>Permit fees</b>"),
     k.cellp("No statewide schedule exists. Each county and municipality sets "
             f"its own on a simple majority vote ({sec('6-9-90')}), and "
             f"several revise annually."),
     k.cellp("“What is the total permit and plan review fee for a new "
             "single-family dwelling of this square footage and valuation?”")],
    [k.cellp("<b>Review and inspection timelines</b>"),
     k.cellp("Not set by statute, and they swing with staffing and season."),
     k.cellp("“What is your current plan review turnaround, and how much "
             "notice do you need for an inspection?”")],
    [k.cellp("<b>Design wind speed by county</b>"),
     k.cellp("The code sends you to Council maps as delineated by your own "
             "building official, and a statute forbids drawing "
             "climatological boundaries on political lines "
             f"({sec('6-9-105')}(C))."),
     k.cellp("“What ultimate design wind speed and exposure category apply to "
             "this parcel, and is it in a wind-borne debris region?”")],
    [k.cellp("<b>Seismic design category</b>"),
     k.cellp("Same mechanism as wind — a map question your building official "
             "delineates, bounded by the ATC data the regulation names."),
     k.cellp("“What seismic design category applies to this parcel?”")],
    [k.cellp("<b>License and registration fees</b>"),
     k.cellp("Published in a regulation and separately on the agency's "
             "website, and the two do not always agree. Not needed by an "
             "exempt owner in any case."),
     k.cellp("Check llr.sc.gov directly if you ever need one.")],
    [k.cellp("<b>Construction cost ranges</b>"),
     k.cellp("Septic, well and construction cost figures move faster than "
             "anything else in this subject and vary more by site than by "
             "state."),
     k.cellp("Get three quotes for the actual parcel.")],
    [k.cellp("<b>Which jurisdictions have opted out of enforcement</b>"),
     k.cellp(f"The {sec('6-9-30')}(B) affidavit route exists, but the "
             f"Building Codes Council publishes no roster of who holds one."),
     k.cellp("“Has this jurisdiction filed a § 6-9-30(B) affidavit with the "
             "Building Codes Council?”")],
    [k.cellp("<b>Phone numbers</b>"),
     k.cellp("They change more often than anything else on a printed page, "
             "and every office publishes current ones."),
     k.cellp("Use the hosts and navigation paths on SC.4.")],
]
flow.append(k.ref_table(
    "Left out on purpose — and what to ask instead",
    [k.cellp("", bold=True), k.cellp("Why", bold=True),
     k.cellp("Ask this", bold=True)],
    rows, [1.45 * inch, (CW - 1.45 * inch) / 2, (CW - 1.45 * inch) / 2]))

# -------------------------------------------------------------- sources
flow += k.h2_tight("SOURCES", reserve=2.0)
flow.append(k.sources_table([
    ("The disclosure statement, the personal appearance, the forms the "
     "agency must provide, and the register-of-deeds notice",
     f"S.C. Code Ann. {sec('40-59-260')}"),
    ("An exempt owner must obtain the permit and list every licensed "
     "contractor on the application",
     f"S.C. Code Ann. {sec('40-11-420')}(C)"),
    ("The statewide list of work exempt from permit and from licensing",
     f"S.C. Code Ann. {sec('40-59-265')}"),
    ("Farm structure affidavit, filed before construction",
     f"S.C. Code Ann. {sec('6-9-65')}"),
    ("Notice of Project Commencement and the posted location notice",
     f"S.C. Code Ann. {sec('29-5-23')}"),
    ("Eight-year repose; the certificate of occupancy as proof of "
     "substantial completion", f"S.C. Code Ann. {sec('15-3-640')}"),
    ("The 2009 IECC is the Energy Standard; the residential code's energy "
     "chapter is not adopted",
     f"S.C. Code Ann. {sec('6-10-30')}; S.C. Code of Regs. 8-1230"),
    ("Truss drawings with the shipment and at inspection; the termite "
     "treatment route", "S.C. Code of Regs. 8-1224, 8-1227, 8-1215"),
    ("Permit fees are set locally by simple majority vote",
     f"S.C. Code Ann. {sec('6-9-90')}"),
    ("Climatological boundaries may not follow political lines",
     f"S.C. Code Ann. {sec('6-9-105')}(C)"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "sc-permit-kit",
                       "SC.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
