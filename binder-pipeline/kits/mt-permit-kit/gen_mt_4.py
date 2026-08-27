#!/usr/bin/env python3
"""MT.4 Where to File Directory — Montana.

The directory question in Montana is not "where is the office" but "does an
office exist for this at all, and if so which disciplines did it certify for."
The centerpiece is the Building Codes Program's own published list of certified
local government programs, transcribed with its per-discipline code letters,
because sorting that list by what each jurisdiction covers proves the kit's
thesis in a way no argument can: building-only certification is the norm, so a
local building permit and a STATE electrical permit on one house is the
ordinary case, not the exception.

Sources verified August 2026:
  bsd.dli.mt.gov/building-codes-permits/certified-government
                        the certified jurisdiction list, transcribed as
                        published with its key: B = Building, P = Plumbing,
                        M/G = Medical Gas, E = Electrical, M = Mechanical,
                        SP = Pool, W = WUI; and the statement "All other areas
                        are under the jurisdiction of the State Building Codes
                        Bureau"
  bsd.dli.mt.gov/building-codes-permits/permit-applications/electrical-permits
                        "State electrical permits are required on all
                        electrical work performed in Montana, except in cities,
                        counties and towns certified to issue electrical
                        permits and conduct inspections"; the homeowner and
                        alternative-energy permit forms
  bsd.dli.mt.gov/.../plumbing-permits and .../mechanical-permits
                        jurisdiction statements for each trade
  50-60-302, 50-60-102(1)(a), (2), MCA

Deliberately prints WEBSITES and navigation routes rather than phone numbers or
the names of individual building officials — both change often enough to be a
liability in print, and every block has a rule to write down what you
confirmed. Fee schedules are not printed at all: they are filed with and
approved by the department per jurisdiction (50-60-302(1)(b)) and change.

Still deliberately hedged: the list is a dated snapshot of a page the
department revises as programs certify and decertify; the kit says so on the
page and gives the verification step.
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

FORM_ID = "MT.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The department's own list of certified local programs — sorted by what "
    "each one actually covers — the state and county offices that own "
    "everything else, and a page to write down what you confirmed.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- three qs
flow += k.h2_tight("ONE LIST ANSWERS ALMOST EVERYTHING")
flow.append(k.body(
    "Montana makes this easier than most states, because there is a single "
    "published list and it is short. A county, city, or town \"<i>may not "
    "enforce a building code unless the code enforcement program has been "
    "certified by the department</i>\" (50-60-302(1)), and the Building Codes "
    "Program publishes every certified program with letter codes for the "
    "disciplines it covers. The department's own summary of everywhere else "
    "is one sentence: <b>\"<i>All other areas are under the jurisdiction of "
    "the State Building Codes Bureau.</i>\"</b>"))
flow.append(k.body(
    "So: find your city or county on the list below. If it is not there, no "
    "local building program has jurisdiction over your parcel — and because "
    "the state \"<i>may not enforce</i>\" the building code against a "
    "residential building of fewer than five dwelling units (50-60-102(2)), "
    "<b>no building permit exists for your house</b>. If it is there, read the "
    "letters, because they decide which of your four permits is local and "
    "which is still the state's."))

flow.append(k.callout("The number that reframes the whole state", [
    Paragraph("Montana has <b>56 counties</b>. On the department's certified "
              "list, <b>six county-level programs appear at all</b> — and two "
              "of those, Pondera and Toole, are certified for <b>commercial "
              "buildings only</b>. Every other county in Montana runs no "
              "building program whatsoever, which means that outside the "
              "incorporated cities and towns named below, the ordinary "
              "Montana house is built with <b>no building permit, no plan "
              "review, and no building inspection</b> — and with the "
              "electrical permit, the energy certification, and the county "
              "septic approval still fully in force. That is the state this "
              "kit is written for.", S["body"]),
]))
flow.append(Spacer(1, 6))

# ---------------------------------------------------------------- the list
flow += k.h2_tight("THE CERTIFIED PROGRAMS — SORTED BY WHAT THEY COVER")
flow.append(k.body(
    "Transcribed from the department's published list in August 2026, using "
    "its own key: <b>B</b> = Building, <b>P</b> = Plumbing, <b>M/G</b> = "
    "Medical Gas, <b>E</b> = Electrical, <b>M</b> = Mechanical, <b>SP</b> = "
    "Pool, <b>W</b> = WUI. The list carried a revision date of <b>July 30, "
    "2026</b> when this was transcribed. Unless a county is named, the "
    "jurisdiction is the <b>city limits</b> only — and that is statutory, not "
    "administrative: \"<i>A city or town that adopts a building code under "
    "this chapter may enforce its building code <b>only within the "
    "incorporated limits</b></i>\" (50-60-304(1)). Montana gives city "
    "building codes no extraterritorial reach at all, so a parcel across the "
    "road from town is state jurisdiction. Do not confuse this with the "
    "extraterritorial mileage rules you may have read about — those are "
    "<i>zoning</i> under 76-2-310, a different subject."))

list_rows = [
    [k.cellp("<b>All four trades</b><br/>B, P, E, M<br/>"
             "<font size=8.5>the local office handles everything</font>"),
     k.cellp("Belgrade · <b>Billings</b> · <b>Bozeman</b> · Columbia Falls · "
             "Darby · <b>Great Falls</b> · Hamilton · <b>Helena</b> · "
             "<b>Kalispell</b> · Manhattan · <b>Missoula (City)</b> · "
             "<b>Missoula County</b> · Polson · Stevensville · "
             "<b>Whitefish</b>")],
    [k.cellp("<b>Building only</b><br/>B (some add SP)<br/>"
             "<font size=8.5>electrical AND plumbing stay with the "
             "state</font>"),
     k.cellp("Choteau · Colstrip <i>(residential only)</i> · Conrad · Cut "
             "Bank · <b>Deer Lodge County</b> <i>(residential only)</i> · "
             "Deer Lodge (City) <i>(residential only)</i> · East Helena · "
             "Forsyth · Glasgow · Hardin <i>(residential only)</i> · Havre · "
             "Laurel · Lewistown · Libby <i>(residential only)</i> · "
             "Livingston · <b>Pondera County</b> <i>(commercial only)</i> · "
             "Red Lodge · <b>Richland County</b> <i>(county except "
             "Sidney)</i> · Ronan · Shelby · Sidney · <b>Toole County</b> "
             "<i>(commercial only)</i> · Townsend · Troy <i>(residential "
             "only)</i> · West Yellowstone <i>(residential only)</i>")],
    [k.cellp("<b>Some trades, not all</b><br/>"
             "<font size=8.5>read these letters twice</font>"),
     k.cellp("<b>Silver Bow</b> (county) — B, P, M, SP: building, plumbing, "
             "and mechanical are local, <b>but electrical is not</b>, so a "
             "Butte-Silver Bow house takes its electrical permit to the "
             "state. · <b>Miles City</b> — B, SP, E <i>(residential only)</i>: "
             "the mirror case, electrical local but plumbing and mechanical "
             "with the state.")],
    [k.cellp("<b>Wildland-urban interface</b><br/>W"),
     k.cellp("Only <b>Bozeman</b>, <b>Columbia Falls</b>, <b>Great Falls</b>, "
             "and <b>Whitefish</b> are certified for the WUI code. Building in "
             "the trees anywhere else means ignition-resistant construction "
             "and defensible space are yours to choose — see MT.2.")],
]
flow.append(k.ref_table(
    "Certified local government programs (as published, August 2026)",
    [k.cellp("What the program covers", bold=True),
     k.cellp("Jurisdictions", bold=True)],
    list_rows, [1.55 * inch, CW - 1.55 * inch]))
flow.append(Spacer(1, 6))

flow.append(k.callout_long("Read the letters, not the town's size", [
    Paragraph("<b>Building-only certification is the most common kind on this "
              "list.</b> Twenty-five of the roughly forty programs are "
              "certified for building and nothing else — so in those towns you "
              "will file a local building permit at city hall and then buy a "
              "<b>state electrical permit</b> from the Building Codes Program "
              "for the same house, with a state inspector driving to the site. "
              "Two different governments, two different applications, two "
              "different schedules, and neither one will remind you about the "
              "other.", S["body"]),
    Paragraph("The department states the electrical rule plainly on its own "
              "permits page: \"<i>State electrical permits are required on "
              "<b>all electrical work performed in Montana</b>, except in "
              "cities, counties and towns certified to issue electrical "
              "permits and conduct inspections.</i>\" The plumbing and "
              "mechanical pages carry parallel statements. So the question is "
              "never \"do I need an electrical permit\" — it is only "
              "<b>\"from whom.\"</b>", S["body"]),
    Paragraph("<b>And this list moves.</b> Programs certify, and they "
              "decertify: a local government that voluntarily gives up its "
              "program must notify the department at least <b>90 days</b> "
              "beforehand and keeps responsibility for finishing inspections "
              "and issuing certificates of occupancy on projects it already "
              "permitted (50-60-302(4)); if certification is revoked, "
              "\"<i>the state resumes its original jurisdiction</i>\" "
              "(50-60-302(3)). Re-check the list before you buy any permit, "
              "and be careful with a project that straddles a change.",
              S["body"]),
]))
flow.append(k.cite(
    "Certified jurisdiction list and key transcribed as published at "
    "bsd.dli.mt.gov &#8594; Building Codes Program &#8594; Certified City, "
    "County and Town Programs, August 2026; the department's statement that "
    "\"All other areas are under the jurisdiction of the State Building Codes "
    "Bureau\" appears on the same page. Trade-jurisdiction statements from the "
    "Electrical, Plumbing, and Mechanical Permits pages, same site. "
    "50-60-302(1), (3), (4); 50-60-102(2), MCA. This kit prints no phone "
    "numbers and no building officials' names — both change; write what you "
    "confirmed in the directory below."))

# ---------------------------------------------------------------- state
flow.append(Spacer(1, 4))
flow.append(k.callout("A right you did not know you had, new in 2025", [
    Paragraph("If a permit office delays your project or issues a stop-work "
              "order, it has to tell you <b>which code section</b> it is "
              "relying on. Under <b>50-60-119</b>, added by Ch. 483, Laws of "
              "2025, a department or local government that fails to cite the "
              "specific provision within <b>seven business days</b> of the "
              "delay or stop-work order is subject to a penalty of <b>$50 a "
              "day</b>. Ask for the citation in writing, politely, on day "
              "one — it is the fastest way to convert a vague objection into "
              "a specific one you can actually resolve.", S["body"]),
]))
flow.append(Spacer(1, 6))

flow += k.h2_tight("STATE AND COUNTY OFFICES — WHO OWNS WHICH PIECE")
state_rows = [
    [k.cellp("<b>Building Codes Program</b><br/>DLI"),
     k.cellp("The certified-jurisdiction list; state electrical, plumbing, and "
             "mechanical permits and inspections; the adopted code editions; "
             "snow and wind load information; inspection areas."),
     k.cellp("bsd.dli.mt.gov &#8594;<br/>Building Codes Program")],
    [k.cellp("<b>Electrical Safety Program</b><br/>DLI"),
     k.cellp("The <b>Homeowner Electrical Permit</b> — a form published "
             "specifically for homeowners personally performing work on their "
             "own home — plus the residential, commercial, alternative-energy, "
             "and transfer forms, and an Electrical Information Pamphlet. "
             "Permits may be bought online through the state business portal "
             "at <b>ebiz.mt.gov</b>."),
     k.cellp("bsd.dli.mt.gov &#8594;<br/>Electrical Permits<br/>"
             "<font size=8.5>(note: it is bsd.dli.mt.gov —<br/>plain "
             "dli.mt.gov/building-codes<br/>is a dead link)</font>")],
    [k.cellp("<b>Construction Contractor<br/>Program</b>"),
     k.cellp("The construction contractor <b>license</b> required by "
             "37-45-201 since January 1, 2026 — and the lookup you use to "
             "verify anyone you hire <b>on the date of the contract</b>, which "
             "is what switches on your 37-45-202 shield (MT.1)."),
     k.cellp("dli.mt.gov &#8594; Licensing<br/>&#8594; Lookup a License")],
    [k.cellp("<b>Independent Contractor<br/>Exemption Certificate</b>"),
     k.cellp("The ICEC program (39-71-417). Every one-person trade you engage "
             "should hold one; ask for a copy and file it."),
     k.cellp("dli.mt.gov &#8594; ICEC Program")],
    [k.cellp("<b>Board of Electricians ·<br/>Board of Plumbers</b>"),
     k.cellp("License verification for any electrician or plumber you hire, "
             "and the boards' rules. Remember a Montana-licensed electrician "
             "or plumber working within the scope of the license is exempt "
             "from the contractor chapter (37-45-104(16))."),
     k.cellp("dli.mt.gov &#8594;<br/>Professional Boards")],
    [k.cellp("<b>Secretary of State — ARM</b>"),
     k.cellp("The Administrative Rules of Montana. <b>Title 24, chapter "
             "301</b> carries every adopted code edition and every Montana "
             "amendment to it — including the plumbing fixture table at "
             "24.301.351."),
     k.cellp("rules.mt.gov")],
    [k.cellp("<b>Montana Legislature — MCA</b>"),
     k.cellp("Official statute text with a History line on every section, "
             "which is how you catch a repeal. Title 50 chapter 60 for "
             "permits; Title 37 chapters 45, 68, 69 for licenses."),
     k.cellp("mca.legmt.gov")],
    [k.cellp("<b>DEQ</b>"),
     k.cellp("Subdivision sanitation review and the wastewater program — the "
             "approval that decides whether a rural lot can carry a house at "
             "all. See MT.2."),
     k.cellp("deq.mt.gov &#8594; Water")],
    [k.cellp("<b>DNRC</b>"),
     k.cellp("Water rights, well permitting and exempt wells, and the forms "
             "filed after a well is drilled. Also the state floodplain "
             "program that local governments administer."),
     k.cellp("dnrc.mt.gov &#8594;<br/>Water Resources")],
    [k.cellp("<b>Your county</b>"),
     k.cellp("The septic permit and site evaluation (county sanitarian or "
             "environmental health), the <b>911 address assignment</b>, the "
             "road approach permit, floodplain administration, and zoning "
             "where the county has any. None of this is affected by the "
             "building-code exemption."),
     k.cellp("County government site<br/>&#8594; Environmental Health /<br/>"
             "Planning / Road Dept.")],
]
flow.append(k.ref_table(
    "Offices and what each is actually for",
    [k.cellp("Office", bold=True),
     k.cellp("Why you would go there", bold=True),
     k.cellp("Route", bold=True)],
    state_rows, [1.5 * inch, CW - 1.5 * inch - 1.75 * inch, 1.75 * inch]))
flow.append(k.cite(
    "Routes read from each agency's own site navigation, August 2026. "
    "37-45-104(16), 37-45-201, 37-45-202, MCA; 39-71-417, MCA. Deep links rot "
    "faster than domains — the navigation route is printed on purpose."))

# ---------------------------------------------------------------- questions
flow += k.h2_tight("THE FIVE QUESTIONS, AND WHO TO ASK")
ask_rows = [
    [k.cellp("<b>Is there a building permit for my house?</b>"),
     k.cellp("Your city or county — but check the certified list first, "
             "because if they are not on it the answer is no and you can stop. "
             "If they are on it, ask whether the local legislative body "
             "adopted the code for residential buildings of fewer than five "
             "dwelling units (50-60-102(1)(a)).")],
    [k.cellp("<b>Who issues my electrical permit?</b>"),
     k.cellp("Read the letters on the certified list: an <b>E</b> means local, "
             "no <b>E</b> means the Building Codes Program. Ask separately "
             "from the building question — the answers differ constantly.")],
    [k.cellp("<b>Does my lot have sanitation approval?</b>"),
     k.cellp("Your county environmental health office or sanitarian, and DEQ. "
             "Ask before you buy land, not after — MT.2 explains why this is "
             "the question that can end a project.")],
    [k.cellp("<b>What is my ground snow load?</b>"),
     k.cellp("The rule sends you to <b>ASCE/SEI 7-22</b> via the ASCE 7 "
             "Hazard Tool, <b>30 psf minimum</b> (ARM 24.301.154(5)). The "
             "department's own snow-load page still cites a 2004 study — "
             "<b>the rule governs</b>. Record your figure and its source.")],
    [k.cellp("<b>What will it take to get power?</b>"),
     k.cellp("Your power supplier — an investor-owned utility or a rural "
             "electric cooperative; both are bound by 50-60-605. Ask about "
             "line extension cost and lead time in the same conversation, "
             "because on a rural parcel that is usually the longest pole in "
             "the whole job.")],
]
flow.append(k.ref_table(
    "Ask these separately — the answers are independent of each other",
    [k.cellp("Question", bold=True), k.cellp("Who answers it", bold=True)],
    ask_rows, [1.9 * inch, CW - 1.9 * inch]))

# ---------------------------------------------------------------- directory
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT")
flow.append(k.body(
    "Confirm each entry with the office itself rather than copying it from a "
    "search result, and write the date. In a small Montana county office a "
    "name is worth more than a number."))


def office_block(label, sub):
    return [
        Paragraph(f"<b>{label}</b> — <font size=9.5>{sub}</font>", S["body"]),
        d.FillInRow([("Office / department:", 0.62), ("Phone:", 0.38)]),
        d.FillInRow([("Portal / address:", 0.44), ("Spoke with:", 0.34),
                     ("Confirmed:", 0.22)]),
        Spacer(1, 4),
    ]


for label, sub in [
    ("BUILDING PERMIT OFFICE", "city or county — or write NONE, and note the "
     "date you confirmed the parcel is outside every certified program"),
    ("ELECTRICAL PERMIT + INSPECTOR", "state Building Codes Program, or the "
     "certified local program if its listing shows E"),
    ("PLUMBING / MECHANICAL", "asked separately — the answer can differ from "
     "both building and electrical"),
    ("COUNTY ENVIRONMENTAL HEALTH", "septic permit, site evaluation, final "
     "approval — and whether the lot already has sanitation approval"),
    ("DEQ — SUBDIVISION SANITATION", "the certificate that may gate the septic "
     "permit; ask before you buy land"),
    ("DNRC — WATER RIGHTS / WELL", "exempt well limits, and what must be filed "
     "after the well is drilled"),
    ("COUNTY ADDRESSING / ROAD DEPT.", "911 address assignment and the road "
     "approach permit — both are commonly prerequisites"),
    ("FLOODPLAIN ADMINISTRATOR", "usually the county planning office; ask even "
     "if you think you are clear of the mapped area"),
    ("POWER SUPPLIER", "utility or rural electric cooperative — line "
     "extension, temporary service, and what releases the permanent meter"),
]:
    flow += office_block(label, sub)

flow.append(Spacer(1, 6))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026): the certified jurisdiction list, "
    "its key, and its July 30, 2026 revision date — bsd.dli.mt.gov, Building "
    "Codes Program. Per-trade statements — the Electrical, Plumbing, and "
    "Mechanical Permits pages. City limits only — 50-60-304(1); certification "
    "and the 90-day notice — 50-60-302; the residential exemption — "
    "50-60-102(1)(a), (2); citation-or-penalty — 50-60-119, MCA."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "mt-permit-kit",
                       "MT.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
