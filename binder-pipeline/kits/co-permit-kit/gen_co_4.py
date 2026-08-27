#!/usr/bin/env python3
"""CO.4 Where to File Directory — Colorado.

The directory question in Colorado is not "where is the office" but "which of
several offices owns each piece of my house" — and the answer differs by trade
within the same county. The centerpiece is the Division of Professions and
Occupations' own published lists of the jurisdictions that run their own
electrical and plumbing inspection programs, because comparing the two lists
proves the kit's thesis in a way no argument can.

Sources verified August 2026:
  dpo.colorado.gov/ElectricalPlumbingPermits  the two published lists of local
                              inspection areas, transcribed as published; the
                              homeowner permit route; inspector contact lists
                              and inspection maps; the address the Division
                              asks local governments to use for notices of
                              intent to commence or cease permitting
  C.R.S. 12-115-120(8)        a local government may commence or cease its
                              electrical program ONLY as of July 1, with
                              written notice to the board by October 1 of the
                              preceding year — which is why the list moves
                              and when
  C.R.S. 12-155-120(6)        the plumbing twin requires written notice but
                              sets no July 1 restriction
  dwr.colorado.gov            well permitting, eForms dashboard, well permit
                              search and map viewer
  C.R.S. 25-10-110            local public health agencies hold primary OWTS
                              enforcement
  Local department domains published BY the Division on its own permits page:
                              denvergov.org, jeffco.us, bouldercounty.gov,
                              adcogov.org, pitkincounty.com, prbd.com,
                              co.grand.co.us, co.laplata.co.us,
                              jacksoncountyco.gov, co.teller.co.us,
                              cityofdelta.net

Deliberately prints WEBSITES and lookup routes rather than phone numbers —
direct-dial numbers change often enough that a printed number is a liability,
and every block has a rule to write the number you confirmed.

Still deliberately hedged: the two lists are a dated snapshot of a page the
Division revises; the kit says so on the page and gives the verification step.
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

FORM_ID = "CO.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "How to pin down which offices own your parcel — including the Division's "
    "own published lists of who inspects electrical and plumbing where — plus "
    "a page to write down what you confirmed.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- step one
flow += k.h2_tight("SETTLE THREE QUESTIONS, NOT ONE")
flow.append(k.body(
    "Everything in this kit branches on three independent answers. <b>(1) "
    "Does a building permit exist for my parcel, and from whom?</b> — a "
    "county or municipal question, and in a few Colorado counties the answer "
    "is none. <b>(2) Who issues my electrical permit?</b> <b>(3) Who issues "
    "my plumbing and gas piping permit?</b> Questions 2 and 3 run on "
    "different statutory tests and have genuinely different answers in ten "
    "Colorado counties — asking once and assuming twice is the classic "
    "mistake."))
flow.append(k.callout("Get it in writing, from the office that will issue it",
                      [
    Paragraph("Ask the county or city planning and building office: "
              "\"<i>Is this parcel inside a municipality or unincorporated? "
              "Do you require a building permit for a new single-family "
              "dwelling? Which code editions have you adopted, and do you run "
              "your own electrical and plumbing inspection programs?</i>\" "
              "Then check the trade answers against the Division's published "
              "lists below. If the two disagree, resolve it before you buy a "
              "permit.", S["body"]),
]))
flow.append(Spacer(1, 6))

# ---------------------------------------------------------------- the lists
flow += k.h2_tight("THE DIVISION'S PUBLISHED LISTS — WHO DOES NOT USE THE "
                   "STATE")
flow.append(k.body(
    "The Division of Professions and Occupations publishes, on its permits "
    "page, the jurisdictions that run their own inspection programs. Its "
    "instruction is that if your county appears on the relevant list, you "
    "\"<i>do not continue with the permit application process</i>\" and go to "
    "the local jurisdiction instead — and that <b>\"<i>You are responsible "
    "for determining the correct inspection authority.</i>\"</b> Transcribed "
    "as published in August 2026:"))

list_rows = [
    [k.cellp("<b>Electrical</b><br/>local program"),
     k.cellp("Adams (except Federal Heights) · Arapahoe (except Bow Mar, "
             "Deer Trail, and Sheridan city limits) · Boulder · Broomfield · "
             "Chaffee · City of Pueblo and Town of Boone · Delta (City of "
             "Delta only) · Denver · Douglas · Eagle (except Minturn and Town "
             "of Avon) · El Paso · Jefferson · Larimer · Mesa · Pitkin · "
             "Pueblo · Routt · San Miguel (Telluride and Mountain Village) · "
             "Summit · Teller · Weld")],
    [k.cellp("<b>Plumbing</b><br/>local program"),
     k.cellp("Adams (except Federal Heights) · Arapahoe (except Bow Mar and "
             "Sheridan city limits) · Boulder · Broomfield · Chaffee · City "
             "of Pueblo and Town of Boone · <b>Clear Creek</b> · Denver · "
             "Douglas · Eagle · El Paso · <b>Elbert</b> · <b>Garfield</b> · "
             "<b>Gilpin</b> · <b>Grand</b> · <b>Jackson</b> · Jefferson · "
             "<b>La Plata</b> · <b>Lake</b> · Larimer · Mesa · <b>Moffat</b> "
             "· Pitkin · <b>Prowers</b> · Pueblo · Routt · Summit · Teller · "
             "Weld")],
]
flow.append(k.ref_table(
    "Jurisdictions the State does NOT inspect (as published, August 2026)",
    [k.cellp("Trade", bold=True),
     k.cellp("Counties and areas running their own program", bold=True)],
    list_rows, [1.15 * inch, CW - 1.15 * inch]))
flow.append(Spacer(1, 6))

flow.append(k.callout("Read the two lists against each other", [
    Paragraph("<b>Ten counties appear on the plumbing list but not the "
              "electrical one</b> — Clear Creek, Elbert, Garfield, Gilpin, "
              "Grand, Jackson, La Plata, Lake, Moffat, and Prowers "
              "(bolded above). Build in any of them and you take your "
              "plumbing permit to the county and your <b>electrical permit "
              "to the State</b>, with two different inspectors on two "
              "different schedules. It runs the other way too: <b>Delta "
              "(City of Delta only)</b> and <b>San Miguel (Telluride and "
              "Mountain Village)</b> appear for electrical but not plumbing. "
              "And the exceptions are per-town — Federal Heights inside "
              "Adams, Minturn and Avon inside Eagle for electrical, Deer "
              "Trail inside Arapahoe for electrical but not plumbing. This "
              "is the whole thesis of the kit on one page.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow.append(k.callout("This list moves — and the statute says when", [
    Paragraph("A local government may start or stop running its own "
              "electrical inspection program \"<i>only as of July 1 of any "
              "year</i>,\" with written notice to the board \"<i>on or before "
              "October 1 of the preceding calendar year</i>\" "
              "(C.R.S. 12-115-120(8)). The plumbing statute requires written "
              "notice but sets no comparable date (12-155-120(6)). So: treat "
              "the lists above as a dated snapshot, <b>re-check them at "
              "dpo.colorado.gov before you buy any permit</b>, and be "
              "especially careful with a project that straddles a July 1.",
              S["body"]),
]))

# ---------------------------------------------------------------- agencies
flow += k.h2_tight("STATE OFFICES — WHO OWNS WHICH PIECE")
state_rows = [
    [k.cellp("<b>DPO — Electrical &amp; Plumbing Permits</b>"),
     k.cellp("Buy the state electrical, plumbing, and gas piping permits; "
             "the local-jurisdiction lists above; inspection maps and "
             "inspector contact lists; the homeowner permit route and "
             "guides."),
     k.cellp("dpo.colorado.gov &#8594;<br/>Electrical &amp; Plumbing<br/>Permits")],
    [k.cellp("<b>State Electrical Board</b>"),
     k.cellp("The adopted NEC edition and its effective date (board rules, "
             "3 CCR 710-1), licensing, variances, rulemaking notices."),
     k.cellp("dpo.colorado.gov/Electrical")],
    [k.cellp("<b>State Plumbing Board</b>"),
     k.cellp("The Colorado Plumbing Code and Colorado Fuel Gas Code as "
             "adopted (board rules, 3 CCR 720-1), plumbing licensing, and "
             "variances."),
     k.cellp("dpo.colorado.gov/Plumbing")],
    [k.cellp("<b>DORA license lookup</b>"),
     k.cellp("Verify any electrician or plumber you hire, and confirm the "
             "firm's contractor registration, before they touch the job."),
     k.cellp("dora.colorado.gov")],
    [k.cellp("<b>Division of Water Resources</b>"),
     k.cellp("Well permits and the eForms dashboard; the Beginner's Guide to "
             "Well Permits; permit search and map viewer; Designated Basin "
             "and Denver Basin rules."),
     k.cellp("dwr.colorado.gov")],
    [k.cellp("<b>Your local public health agency</b>"),
     k.cellp("The OWTS (septic) permit, site evaluation, local OWTS rules, "
             "and the final inspection. Primary enforcement sits here, not "
             "with the state (25-10-110)."),
     k.cellp("County or district<br/>public health")],
    [k.cellp("<b>Division of Fire Prevention<br/>and Control</b>"),
     k.cellp("The <b>2025 Colorado Wildfire Resiliency Code</b> — structure "
             "hardening and site requirements that apply \"<i>within the "
             "wildland-urban interface areas of Colorado, as designated in "
             "this code</i>,\" plus the mapping and the petition process for "
             "code variations."),
     k.cellp("dfpc.colorado.gov")],
    [k.cellp("<b>Colorado Energy Office</b>"),
     k.cellp("The model electric ready and solar ready code and the model low "
             "energy and carbon code that the energy-code triggers in CO.2 "
             "point at."),
     k.cellp("energyoffice.colorado.gov")],
    [k.cellp("<b>Secretary of State — CCR</b>"),
     k.cellp("The Code of Colorado Regulations: the official text of every "
             "board rule cited in this kit, with each past version and its "
             "effective date."),
     k.cellp("sos.state.co.us/CCR")],
]
flow.append(k.ref_table(
    "State offices and what each is actually for",
    [k.cellp("Office", bold=True),
     k.cellp("Why you would go there", bold=True),
     k.cellp("Website", bold=True)],
    state_rows, [1.5 * inch, CW - 1.5 * inch - 1.95 * inch, 1.95 * inch]))
flow.append(k.cite(
    "Domains from each agency's own site navigation, read August 2026. This "
    "kit prints no phone numbers — numbers rot; write the one you confirmed "
    "in the directory below."))

# ---------------------------------------------------------------- local
flow += k.h2_tight("WHO PERMITS YOUR PARCEL — TWO THINGS TO EXPECT")
flow.append(k.body(
    "The Division's permits page links straight to the local jurisdictions it "
    "hands you off to — rare local URLs with a state agency standing behind "
    "them: <b>denvergov.org</b>, <b>jeffco.us</b>, <b>bouldercounty.gov</b>, "
    "<b>adcogov.org</b>, <b>pitkincounty.com</b>, <b>co.grand.co.us</b>, "
    "<b>co.laplata.co.us</b>, <b>jacksoncountyco.gov</b>, "
    "<b>co.teller.co.us</b>, <b>cityofdelta.net</b>. Each department's own "
    "page governs — and two structural surprises are worth expecting."))
flow.append(k.callout("A Colorado peculiarity: regional building departments",
                      [
    Paragraph("In parts of Colorado the permit authority is neither the city "
              "nor the county but a <b>regional building department</b> "
              "serving several governments at once. The largest is the "
              "<b>Pikes Peak Regional Building Department</b> (pprbd.org), "
              "which issues permits for unincorporated El Paso County; the "
              "cities of Colorado Springs, Fountain, and Manitou Springs; the "
              "towns of Green Mountain Falls, Monument, and Palmer Lake; and, "
              "in Teller County, Woodland Park only. Its own pages currently "
              "disagree about whether Calhan is served — the site header "
              "lists it, the homeowner page excludes it — so near a boundary, "
              "get the answer in writing.", S["body"]),
    Paragraph("<b>And these departments themselves change.</b> The Pueblo "
              "Regional Building Department was "
              "succeeded effective <b>January 1, 2026</b>: Pueblo city limits "
              "and the Town of Boone now go to the <b>Southern Colorado "
              "Building Department</b> (socobd.com), the rest of the county "
              "including Pueblo West to the <b>Pueblo County Building "
              "Division</b> (pueblopermits.com). Older guides — and some "
              "state pages — still link to the predecessor.", S["body"]),
]))

# ---------------------------------------------------------------- patterns
flow += k.h2_tight("FINDING THE REST")
find_rows = [
    [k.cellp("<b>Local public health (septic)</b>"),
     k.cellp("Search \"<i>[your county] CO public health onsite "
             "wastewater</i>\" — some counties run their own agency, others "
             "belong to a health district. Every local board of health must "
             "have adopted OWTS rules (25-10-104(2)); ask for them.")],
    [k.cellp("<b>Your state inspector</b>"),
     k.cellp("Not the Division switchboard — use the <b>inspection map and "
             "inspector contact list</b> on the Division's permits page, and "
             "note the name in the block below when you buy the permit.")],
    [k.cellp("<b>Water provider or well</b>"),
     k.cellp("For a tap, the municipality or water and sanitation district "
             "serving the parcel — ask for a written will-serve. For a well, "
             "DWR's permit search and map viewer show what neighboring "
             "parcels hold.")],
    [k.cellp("<b>Road authority and fire district</b>"),
     k.cellp("County road and bridge, the municipality, or CDOT where the "
             "driveway meets a state highway — confirm which owns your "
             "frontage before you cut it. The fire district is usually yet "
             "another special district, with its own access, water-supply, "
             "and defensible-space rules. Find both by parcel, early.")],
]
flow.append(k.ref_table(
    "Finding the right office for your parcel",
    [k.cellp("Office", bold=True), k.cellp("How to find it", bold=True)],
    find_rows, [1.8 * inch, CW - 1.8 * inch]))

# ---------------------------------------------------------------- directory
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT")
flow.append(k.body(
    "Confirm each entry by phone rather than copying it from a search result, "
    "and write the date. In a small county office, a name is worth more than "
    "a number."))


def office_block(label, sub):
    return [
        Paragraph(f"<b>{label}</b> — <font size=9.5>{sub}</font>", S["body"]),
        d.FillInRow([("Office / department:", 0.62), ("Phone:", 0.38)]),
        d.FillInRow([("Portal / address:", 0.44), ("Spoke with:", 0.34),
                     ("Confirmed:", 0.22)]),
        Spacer(1, 4),
    ]


for label, sub in [
    ("BUILDING PERMIT OFFICE", "county, municipality, or regional building "
     "department — and whether a permit is required at all"),
    ("ELECTRICAL PERMIT + INSPECTOR", "state or local; inspector's name and "
     "number from the contact list"),
    ("PLUMBING / GAS PERMIT + INSPECTOR", "asked separately — the answer can "
     "differ from electrical"),
    ("LOCAL PUBLIC HEALTH — OWTS", "septic permit, site evaluation, final "
     "inspection"),
    ("WATER — DWR, DRILLER, OR PROVIDER", "well permit (allow up to 49 days "
     "for review), or the will-serve letter for a tap"),
    ("ROAD AUTHORITY / ADDRESSING", "driveway permit — county, city, or "
     "CDOT — and the assigned address"),
    ("FIRE DISTRICT / WILDFIRE", "access, water supply, defensible space; who "
     "reviews for the Wildfire Resiliency Code"),
    ("ELECTRIC UTILITY", "line extension, temporary power, meter set — no "
     "permanent service without the final electrical approval"),
]:
    flow += office_block(label, sub)

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026): jurisdiction lists, homeowner "
    "permit route, and inspector contact lists — "
    "dpo.colorado.gov/ElectricalPlumbingPermits, transcribed as published. "
    "Change cadence — C.R.S. 12-115-120(8), 12-155-120(6). Local OWTS rules "
    "and enforcement — 25-10-104(2), 25-10-110. Wells — dwr.colorado.gov. "
    "Pueblo Regional Building Department — prbd.com."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "co-permit-kit",
                       "CO.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
