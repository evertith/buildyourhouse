#!/usr/bin/env python3
"""KY.5 Forms & Documents Index.

Form names are the Department's own where the regulation names them (the
plumbing "Plan Application Form" incorporated by 815 KAR 20:050 Section 7, and
the four HVAC application forms named in 815 KAR 8:070 Section 1(2)). Local
instruments are described rather than named, because they vary and many
Kentucky jurisdictions issue none at all.

Verified sources:
  815 KAR 20:050 §1(3), §2(1)(b), §7   plumbing: what needs no permit, the
                                       homeowner affidavit, the Plan
                                       Application Form (2/2020)
  815 KAR 8:070 §1(2), §2(2)           the four HVAC forms by name, and the
                                       homeowner filing requirements
  KRS 198B.6671(5), (6)                window units, space heaters, and
                                       buildings designed for human occupancy
  KRS 318.015(3)                       chapter 318 does not apply to farmsteads
  KRS 198B.060(3)                      urban-county farm dwelling exemption
  KRS 198B.060(10)                     the workers' compensation affidavit
  KRS 198B.060(11)                     the electrical certificate of approval
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

FORM_ID = "KY.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document a Kentucky owner-builder meets — what each one is, when "
    "it is needed, and which office it comes from.")

flow.append(k.disclaimer(
    "State form names below are the Department's. Local forms vary, and in "
    "much of Kentucky there is no local form at all — the obligations behind "
    "the state ones do not change either way."))
flow.append(Spacer(1, 8))

DOCS = [
    ("County inspector sheet",
     "Not a form — the <b>lookup</b>. One page per county naming your state "
     "electrical inspector, plumbing inspector and their office hours, HVAC "
     "inspector, health department environmentalist, and whether a local "
     "building inspector exists at all. <b>When:</b> first, before anything "
     "else. Free.",
     "dhbc.ky.gov → HOW DO I? → Contact an Inspector"),
    ("On-site sewage disposal construction permit",
     "The septic permit, on form <b>DFS-307</b>, preceded by a site "
     "evaluation the health department must complete in <b>15 working "
     "days</b>. By statute it must <b>accompany your state plumbing permit "
     "application</b> if you are on a system without surface discharge — so "
     "this is the long pole. There is no separate operation permit; there is "
     "an inspection before backfill. <b>When:</b> before the plumbing "
     "application, and ideally before the house is sited.",
     "County health department, under the Cabinet for Health and Family "
     "Services"),
    ("Homeowner septic installation",
     "You may install your own system. The permit issues to a homeowner if "
     "you apply first and <b>personally perform all the work</b> — except "
     "excavation and backfill, which a certified installer may do <i>only if "
     "you name them on the application</i>. <b>One homeowner septic permit "
     "per person per five years</b>, repairs excepted. Not available if you "
     "are building for sale or resale.",
     "Part of the septic permit application"),
    ("Water well: certified driller and a filed well record",
     "The one trade a Kentucky homeowner may <b>not</b> do themselves. It is "
     "unlawful to construct, alter or repair a water well without a state "
     "driller's certificate, and there is no homeowner exemption — the "
     "contrast with electrical, plumbing, HVAC and septic is stark. No permit "
     "to drill is required; the controls are the certified driller, the well "
     "record filed with the state, and a bacteriological test on a potable "
     "well.",
     "A certified water well driller; record filed with the Division of Water"),
    ("State plumbing installation permit application",
     "Filed with the Department, not your county — unless a local government "
     "has been authorized to issue, in which case its permit \"<i>shall be "
     "deemed a permit issued by the department</i>.\" Must be applied for "
     "<b>before work begins</b>, with plans and specifications of the plumbing "
     "and of the water supply system.",
     "Department of Housing, Buildings and Construction, Division of Plumbing"),
    ("Homeowner plumbing affidavit",
     "Filed <i>with</i> the plumbing application: your sworn statement that "
     "you will abide by 815 KAR Chapter 20. The permit is issued only to a "
     "licensed master plumber or to a homeowner meeting all five conditions — "
     "including that <b>all the work be personally performed by you</b>.",
     "Part of the plumbing permit application"),
    ("Plan Application Form",
     "The plumbing plan-review form incorporated by reference into the "
     "regulation (edition 2/2020), submitted with three identical sets of "
     "plans where plan review applies. <b>Ask whether your house needs this at "
     "all</b> — see KY.2.",
     "Division of Plumbing"),
    ("HVAC Construction Permit Application: Homeowner One &amp; Two Family "
     "Dwellings",
     "One of four named HVAC application forms, and the one you use. Applied "
     "for <b>before the HVAC work starts</b>.",
     "Department of Housing, Buildings and Construction"),
    ("HVAC homeowner filings",
     "Three things go in with that form: an <b>affidavit</b> to abide by the "
     "regulation, <b>proof of adequate sizing</b> of the system, and <b>a "
     "complete design plan of all related duct and piping</b>. The heaviest "
     "paperwork of the three trades.",
     "Part of the HVAC permit application"),
    ("Electrical final certificate of approval",
     "Issued by a <b>certified electrical inspector</b>. Not optional and not "
     "skippable: without it \"<i>no utility shall initiate permanent "
     "electrical service to any new building</i>.\" <b>When:</b> at the end of "
     "the electrical work, before you expect permanent power.",
     "Certified electrical inspector — local, or the state inspector on your "
     "county sheet"),
    ("Local building permit application",
     "Only where your city or county passed an ordinance requiring permits for "
     "single-family dwellings. Wholly a local instrument — form, plan "
     "requirements and fees are all set locally. <b>When:</b> after zoning and "
     "the health department are lined up.",
     "Your city or county building department, if it has one"),
    ("Workers' compensation and unemployment affidavit",
     "Required by statute before <b>any</b> Kentucky building department or "
     "political subdivision may issue a permit: your sworn assurance that "
     "every contractor and subcontractor is in compliance. Penalty is $4,000 "
     "or the sum of all uninsured claims, whichever is greater.",
     "Part of the local permit application"),
    ("Certificates of insurance from subcontractors",
     "Not a government form — the evidence behind the affidavit you just "
     "signed. Collect one from every sub <b>before</b> they start and check "
     "the expiry against your schedule.",
     "Each subcontractor's insurer"),
    ("Construction documents and site plan",
     "Plans to the 2018 Kentucky Residential Code, Third Edition. Required "
     "with a local building permit application; worth drawing properly "
     "regardless, because the code binds your house whether or not anyone "
     "reviews the drawings.",
     "You or your designer"),
    ("Zoning approval / setback confirmation",
     "A separate question from building permits, and not answered by them. "
     "Many Kentucky counties have zoning and no building permit, or the "
     "reverse. Get setbacks <b>in writing before you draw</b>.",
     "City or county planning, or the county judge/executive"),
    ("911 address assignment",
     "You will need an address before a utility will open an account. "
     "<b>When:</b> early — it is quick, and it blocks things if left late.",
     "County 911 / emergency services office"),
    ("Driveway or entrance permit",
     "An encroachment or entrance permit where the driveway meets a "
     "state-maintained route; otherwise the county road department. Confirm "
     "which authority owns your road before assuming.",
     "Kentucky Transportation Cabinet district office, or the county"),
    ("Floodplain permit",
     "A <b>state</b> permit, and the statute names buildings expressly: no "
     "one shall \"<i>place a building, barrier, or obstruction of any sort in, "
     "any area in the floodplain or floodway</i>\" without the cabinet's "
     "approval. It opens \"<i>notwithstanding any other provision of law</i>\" "
     "and is <b>not</b> conditioned on any local ordinance — so it applies in "
     "full even in a county with no building permit. Plans must be drawn by a "
     "licensed engineer unless the cabinet waives it. <b>When:</b> before you "
     "buy, if you can.",
     "Energy and Environment Cabinet, Division of Water — eec.ky.gov"),
    ("Certificate of occupancy",
     "Required before occupancy where a local government has established "
     "jurisdiction; <b>not required for a single-family dwelling where it has "
     "not</b>. Request one anyway if you can — without it, a later "
     "code-violation award against you may add reasonable attorney's fees, for "
     "up to ten years.",
     "Your local building official, where one exists"),
]

rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in DOCS]
flow.append(k.ref_table(
    "Documents a Kentucky owner-builder will encounter",
    [k.cellp("Document", bold=True),
     k.cellp("What it is and when you need it", bold=True),
     k.cellp("Where it comes from", bold=True)],
    rows, [1.55 * inch, CW - 1.55 * inch - 1.72 * inch, 1.72 * inch]))

flow.append(Spacer(1, 8))
flow += k.h2_tight("WHAT NEEDS NO PERMIT AT ALL")
flow.append(k.body(
    "Kentucky's exemptions are narrow and specific. Each exempts you from the "
    "<b>permit</b> only — never from the code, and never from zoning."))
flow.append(k.bullet(
    "<b>Plumbing:</b> no permit for the repair of <b>leaks, cocks or "
    "valves</b>, or for <b>cleaning out waste or sewer pipes</b>. Everything "
    "else on the list in the regulation — a new installation, moving a "
    "fixture or waste opening, a new or replaced house sewer or water service, "
    "adding a backflow preventer, a new or replaced water heater — does need "
    "one. (815 KAR 20:050 §1(1), (3))"))
flow.append(k.bullet(
    "<b>HVAC:</b> \"<i>No permit or inspection shall be required for the "
    "installation of <b>window unit air conditioners or space heaters</b></i>,\" "
    "and none is required at all \"<i>except in buildings designed for human "
    "occupancy</i>\" — which a house is. The permit requirement reaches the "
    "<b>initial</b> system; replacement equipment is permitted and inspected "
    "on request under a separate provision. (KRS 198B.6671(5), (6); "
    "815 KAR 8:070 §1(1), §3(1))"))
flow.append(k.bullet(
    "<b>Farmsteads:</b> \"<i>This chapter shall not apply to farmsteads</i>\" "
    "— the plumbing chapter, in terms. This is a real carve-out and it is "
    "frequently over-read; it does not touch the building code, the electrical "
    "certificate of approval, or the health department's septic rules. Ask "
    "before you rely on it. (KRS 318.015(3))"))
flow.append(k.bullet(
    "<b>Farm buildings in an urban-county government:</b> an urban-county "
    "government \"<i>may determine service districts within their boundaries "
    "within which farm dwellings and other farm buildings, not used in the "
    "business of retail trade or as a place of regular employment for ten (10) "
    "or more people, shall be exempt from the requirements of the Uniform "
    "State Building Code</i>.\" This is permissive and geographically narrow — "
    "check whether your urban-county government has actually done it. "
    "(KRS 198B.060(3))"))

flow.append(Spacer(1, 6))
flow.append(k.callout("The exemption that is not on this list", [
    Paragraph("You will not find a general Kentucky exemption for small "
              "detached accessory buildings, decks, or fences of the kind most "
              "states publish in their code's permit-exemption section. That "
              "is because in much of Kentucky the question does not arise: "
              "where no local ordinance requires a building permit for the "
              "house itself, there is nothing for a shed to be exempt "
              "<i>from</i>. Where an ordinance does apply, the exemptions are "
              "<b>that jurisdiction's</b> and you have to ask for them.",
              S["body"]),
    Paragraph("The trade permits are the constant. A detached garage you run "
              "power and a hose bib to still touches the electrical "
              "certificate of approval and the plumbing permit, whatever your "
              "county says about the building.", S["body"]),
]))

flow.append(Spacer(1, 8))
flow += k.pack_fields([("Local permit exemptions confirmed with:", 0),
                       ("Date:", 0)], CW)

flow.append(Spacer(1, 8))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026; statutes and regulations at "
    "apps.legislature.ky.gov, forms and county sheets at dhbc.ky.gov). "
    "Plumbing permits, what needs none, the homeowner conditions and the Plan "
    "Application Form (2/2020) — 815 KAR 20:050 Sections 1, 2 and 7. The state "
    "plumbing permit and the septic permit that must accompany it — "
    "KRS 318.134(1)(a), (2). Local authorization and deemed department "
    "permits — KRS 318.140(1). Farmsteads — KRS 318.015(3). The four HVAC "
    "application forms and the homeowner filings — 815 KAR 8:070 Sections "
    "1(2), 2(2), 3(1). Window units, space heaters and buildings designed for "
    "human occupancy — KRS 198B.6671(5), (6). The workers' compensation "
    "affidavit — KRS 198B.060(10). The electrical certificate of approval and "
    "permanent service — KRS 198B.060(11). Certificates of occupancy — "
    "KRS 198B.060(13); attorney's fees where none was issued — KRS 198B.130. "
    "Urban-county farm building exemption — KRS 198B.060(3). On-site sewage "
    "construction permit, the DFS-307 form, the homeowner permit and its "
    "five-year limit — 902 KAR 10:085 Section 2 and 902 KAR 10:110 Sections "
    "1(8), 2(4) and 3; the fifteen-working-day site evaluation — "
    "KRS 211.350(3). Water well drillers must be certified and there is no "
    "homeowner exemption — KRS 223.405 and 223.425(3); well records — "
    "KRS 223.440. State floodplain permit for placing a building in a "
    "floodplain — KRS 151.250(2), with the engineer requirement at "
    "KRS 151.260(2)."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ky-permit-kit",
                       "KY.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
