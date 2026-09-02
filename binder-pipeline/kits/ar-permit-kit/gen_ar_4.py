#!/usr/bin/env python3
"""AR.4 Where to File Directory.

Arkansas publishes no statewide list of which cities and counties issue
building permits — unlike Kentucky, which prints a per-county inspector sheet.
So this document cannot hand the reader an answer. What it hands them instead
is the METHOD that produces the answer in about ten minutes, the five counties
where that method was run in September 2026 and what it returned, and the
offices that exist in a county with no building department at all.

Every URL printed here was verified to resolve in September 2026. Offices,
never phone numbers: numbers rot faster than anything else on a printed page.

Verified sources:
  Each county's own department or elected-officials index — the enumeration IS
  the evidence, and it is reproducible by the reader.
  Ark. Code Ann. § 14-14-802(b), § 14-17-207(a)  the county services power, and
  the absence of "building codes" from either enumeration.
  Ark. Code Ann. § 14-56-202  the city permit power.

DELIBERATELY NOT PRINTED:
  - Washington County. Our own state guide asserts that unincorporated
    Washington County requires no building permit, no inspection and no
    certificate of occupancy. The county's site refused every automated request
    in this pass, so the claim could not be verified — and the county does
    operate a Planning and Development office, which makes a blanket "no
    permit" sentence risky. The kit names the method instead of the answer.
  - Lonoke County has no locatable official website. Saying so is the honest
    finding; inventing a URL is not.
  - Any phone number, anywhere.
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

FORM_ID = "AR.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "How to find out whether anybody permits your parcel — and the offices "
    "that exist even when nobody does.")

flow.append(k.disclaimer(
    "Every web address here was checked in September 2026. Offices move; the "
    "method in the next section outlives any list."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- no list
flow += k.h2_tight("THERE IS NO LIST — SO HERE IS THE METHOD", reserve=2.0)
flow.append(k.body(
    "Some states publish a register of which jurisdictions enforce the "
    "building code. <b>Arkansas does not.</b> No state agency maintains a list "
    "of which of the 75 counties and several hundred municipalities issue "
    "residential building permits, because no state agency has any reason to: "
    "the decision is local, permissive, and nobody has to report it to anyone."))
flow.append(k.body(
    "That sounds like bad news and is actually manageable, because the answer "
    "is sitting in plain sight on your county's own website. A county that "
    "runs a building department lists it among its departments. A county that "
    "does not, does not. <b>The absence is the finding</b> — and it takes "
    "about ten minutes to establish."))
flow.append(k.callout_long(
    "The ten-minute method", [
        Paragraph("<b>1. Open your county's official site and find its "
                  "Departments or Elected Officials index.</b> Get the "
                  "complete list, not the search box. Watch the domain: "
                  "Arkansas counties use no consistent pattern — some are "
                  "<i>.gov</i>, some <i>.com</i>, one uses <i>.ar.gov</i> — "
                  "and several plausible-looking addresses are parked domains "
                  "or private community sites rather than the county.",
                  S["body"]),
        Paragraph("<b>2. Read the whole list for a Building, Planning, Zoning, "
                  "Permits or Development office.</b> If the list runs "
                  "Assessor, Circuit Clerk, Collector, Coroner, County Clerk, "
                  "County Judge, Emergency Management, Road Department, "
                  "Sheriff, Treasurer — and stops — there is no building "
                  "department, and there is no building permit to pull.",
                  S["body"]),
        Paragraph("<b>3. Do not be fooled by three lookalikes.</b> "
                  "\"Buildings and Grounds\" is facilities maintenance for "
                  "county-owned property. \"Environmental Inspections\" is "
                  "usually stormwater and nuisance enforcement. \"Emergency "
                  "Management\" often houses the floodplain administrator and "
                  "911 addressing — both of which you do need, neither of "
                  "which is a building department.", S["body"]),
        Paragraph("<b>4. Then ask the city anyway.</b> A county mailing "
                  "address does not mean you are outside municipal reach: "
                  "cities have planning areas and extraterritorial "
                  "jurisdiction. Ring the nearest city and ask whether your "
                  "parcel is inside anything of theirs. This is the step "
                  "people skip, and getting it wrong invalidates everything "
                  "else.", S["body"]),
        Paragraph("<b>5. Get the answer in writing and date it.</b> Email is "
                  "fine. Write it on the directory page at the end of this "
                  "document. In three years, when an appraiser asks why there "
                  "is no permit on file, that email is your answer.",
                  S["body"]),
    ]))

flow += k.h2_tight("WHAT THE METHOD RETURNED IN SEPTEMBER 2026", reserve=2.0)
flow.append(k.body(
    "We ran it on five counties chosen to span the state. In every one, the "
    "county's own published department list contained no building, planning, "
    "zoning or permits office. <b>This is a snapshot, not a guarantee</b> — "
    "a quorum court can create a department at any time, so re-run the method "
    "on your own county rather than relying on this table."))
rows = [
    [k.cellp("<b>Garland</b><br/>Hot Springs"),
     k.cellp("21 departments listed, none of them a building or planning "
             "office. Has Addressing, a Floodplain function under Emergency "
             "Management, a Road Department, and Environmental Inspections — "
             "which handles stormwater, not buildings")],
    [k.cellp("<b>White</b><br/>Searcy"),
     k.cellp("Assessor, Circuit Clerk, Collector, Coroner, County Clerk, "
             "Emergency Management, County Judge, Quorum Court, Road "
             "Department, Sheriff, Treasurer, Veteran Services. No building "
             "or planning office")],
    [k.cellp("<b>Crawford</b><br/>Van Buren"),
     k.cellp("Sixteen offices listed including 911 Communications and "
             "Emergency Management. No building, planning or permits office")],
    [k.cellp("<b>Baxter</b><br/>Mountain Home"),
     k.cellp("Has a \"Buildings and Grounds\" department — which maintains "
             "county-owned facilities and runs a work-order system. It is not "
             "a permit office. No building or planning department")],
    [k.cellp("<b>Boone</b><br/>Harrison"),
     k.cellp("Assessor, Circuit Clerk, Collector, County Clerk, County Judge, "
             "District Court, Emergency Management, Quorum Court, Road and "
             "Bridge, Treasurer, Veterans, Sheriff. No building or planning "
             "office")],
]
flow.append(k.ref_table(
    "Five counties, one result — verified from each county's own index",
    [k.cellp("County", bold=True),
     k.cellp("What its published department list shows", bold=True)],
    rows, [1.25 * inch, CW - 1.25 * inch]))
flow.append(k.cite(
    "Two warnings from running this ourselves. <b>A working web address is not "
    "proof of an official site:</b> at least two plausible county domains "
    "returned a normal page and were parked advertising domains, and one "
    "county-named site that looks entirely official is a privately run "
    "community and tourism site. Check for the county seal, the elected "
    "officials and a government domain. <b>And some counties have no website "
    "at all</b> — for one of the counties we tried, no official site exists to "
    "link to, which leaves the county courthouse as the only way in."))

# ---------------------------------------------------------------- rural
flow += k.h2_tight("THE OFFICES THAT EXIST WHEN NO BUILDING DEPARTMENT DOES",
                   reserve=2.4)
flow.append(k.body(
    "\"No building permit\" is not the same as \"no paperwork.\" A rural "
    "Arkansas build still touches a short, specific list of offices. The real "
    "risk is not missing an agency — it is doing them in the wrong order, "
    "because two of them constrain where the house can physically sit."))
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp("<b>Confirm nobody has jurisdiction</b>"),
     k.cellp("County department index, plus the nearest city's planning "
             "office. Do this before relying on any of it")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("<b>911 address</b>"),
     k.cellp("Addressing coordinator, 911 Communications, or Emergency "
             "Management depending on the county. Early — utilities and often "
             "the septic permit need it")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("<b>Septic permit</b>"),
     k.cellp("County health unit, through a licensed Designated "
             "Representative. <b>Constrains the house position</b> — do it "
             "before you fix the footprint")],
    [k.cellp("<b>4</b>", center=True),
     k.cellp("<b>Water</b>"),
     k.cellp("A licensed well contractor, or the rural water association. No "
             "well permit exists; the construction standards still apply")],
    [k.cellp("<b>5</b>", center=True),
     k.cellp("<b>Floodplain determination</b>"),
     k.cellp("County floodplain administrator, frequently inside Emergency "
             "Management. You may need a document certifying that you are "
             "<i>outside</i> the hazard area")],
    [k.cellp("<b>6</b>", center=True),
     k.cellp("<b>Driveway or access permit</b>"),
     k.cellp("Decided by the road you touch: a state highway means the "
             "Department of Transportation; a county road means the county "
             "Road Department under the County Judge; a city street means the "
             "city")],
    [k.cellp("<b>7</b>", center=True),
     k.cellp("<b>Electric service</b>"),
     k.cellp("Your utility or co-op — in practice the only electrical gate "
             "where no local permit program exists. Ask early")],
    [k.cellp("<b>8</b>", center=True),
     k.cellp("<b>Utility locate</b>"),
     k.cellp("Arkansas 811, free, before any excavation")],
    [k.cellp("<b>9</b>", center=True),
     k.cellp("<b>Stormwater</b>"),
     k.cellp("Only if total disturbance reaches one acre. Most single house "
             "sites do not")],
    [k.cellp("<b>10</b>", center=True),
     k.cellp("<b>Assessor, afterwards</b>"),
     k.cellp("New construction goes on the rolls by itself. What you file is "
             "the homestead property tax credit — the deadline is "
             "<b>15 October</b>")],
]
flow.append(k.ref_table(
    "The rural sequence",
    [k.cellp("", bold=True, center=True), k.cellp("Step", bold=True),
     k.cellp("Which office, and why the order", bold=True)],
    rows, [0.35 * inch, 1.75 * inch, CW - 2.1 * inch]))

# ---------------------------------------------------------------- state
flow += k.h2_tight("STATE-LEVEL ADDRESSES", reserve=2.0)
flow.append(k.body(
    "All verified to resolve in September 2026. We print no phone numbers "
    "anywhere in this kit — they go stale faster than anything else on a "
    "printed page, and every office below can be reached from its own site."))
rows = [
    [k.cellp("Verify a contractor's license"),
     k.cellp("labor.arkansas.gov — Arkansas Contractors Licensing Board, then "
             "<i>Find A Licensed Contractor</i>")],
    [k.cellp("Verify an electrician or HVACR license"),
     k.cellp("labor.arkansas.gov — Department of Labor and Licensing rosters")],
    [k.cellp("Verify a plumber"),
     k.cellp("Department of Health, <b>not</b> Labor and Licensing — "
             "adhplumbinghvacrlookup.arkansas.gov")],
    [k.cellp("Apply for a septic permit"),
     k.cellp("septictankpermitonline.adh.arkansas.gov")],
    [k.cellp("Find a Designated Representative"),
     k.cellp("onsitewastewater.adh.arkansas.gov")],
    [k.cellp("Find your county health unit"),
     k.cellp("healthy.arkansas.gov/health-units")],
    [k.cellp("Onsite wastewater rules and program"),
     k.cellp("healthy.arkansas.gov — Onsite Wastewater")],
    [k.cellp("Water wells and licensed drillers"),
     k.cellp("agriculture.arkansas.gov — Natural Resources Division")],
    [k.cellp("Floodplain management, state NFIP"),
     k.cellp("agriculture.arkansas.gov — Floodplain Management")],
    [k.cellp("Check your flood zone"),
     k.cellp("msc.fema.gov")],
    [k.cellp("Driveway onto a state highway"),
     k.cellp("ardot.gov/permits — Access Driveway Permits")],
    [k.cellp("Construction stormwater"),
     k.cellp("adeq.state.ar.us — Division of Environmental Quality. Note the "
             "old domain: the agency renamed, the address did not")],
    [k.cellp("State Fire Marshal"),
     k.cellp("dps.arkansas.gov — Division of Emergency Management. <b>Not</b> "
             "the State Police, which is a different office")],
    [k.cellp("Homestead property tax credit"),
     k.cellp("dfa.arkansas.gov — Assessment Coordination Division")],
    [k.cellp("Parcel and mapping data"),
     k.cellp("gis.arkansas.gov")],
    [k.cellp("Utility locate before digging"),
     k.cellp("ar811.org")],
    [k.cellp("Read the statutes"),
     k.cellp("arkleg.state.ar.us — Arkansas Code")],
    [k.cellp("Read the agency rules"),
     k.cellp("codeofarrules.arkansas.gov")],
    [k.cellp("Read the building code free"),
     k.cellp("codes.iccsafe.org/codes/arkansas — Volume III is residential")],
]
flow.append(k.ref_table(
    "What you actually need, and where it lives",
    [k.cellp("To do this", bold=True), k.cellp("Go here", bold=True)],
    rows, [2.35 * inch, CW - 2.35 * inch]))

# ---------------------------------------------------------------- own
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT",
                   reserve=1.6)
flow += k.check_table(
    "Every office that touches this build, and what it told you",
    [
        ("<b>City</b> — does it require a building permit for my parcel?",
         [("Office", 0.45), ("Answer", 0.35), ("Date", 0.2)]),
        ("<b>County</b> — does it require a building permit?",
         [("Office", 0.45), ("Answer", 0.35), ("Date", 0.2)]),
        ("Is the parcel inside a city planning area or extraterritorial "
         "jurisdiction?", [("Confirmed with", 0.75), ("Date", 0.25)]),
        ("County health unit — Environmental Health Specialist",
         [("Name", 0.6), ("Unit", 0.4)]),
        ("Designated Representative for the septic design",
         [("Name", 0.6), ("License", 0.4)]),
        ("Septic installer, if not doing it myself",
         [("Name", 0.6), ("License", 0.4)]),
        ("911 addressing office", [("Office", 1.0)]),
        ("County floodplain administrator", [("Office", 1.0)]),
        ("Road authority for my driveway — state, county or city",
         [("Office", 1.0)]),
        ("Electric utility or co-op, and its service requirements",
         [("Name", 1.0)]),
        ("Water — well contractor, or the rural water association",
         [("Name", 1.0)]),
        ("Plumbing permit and inspection authority — the utility body that "
         "serves this parcel", [("Office", 1.0)]),
        ("Electrical inspector, if anyone inspects here",
         [("Name", 0.6), ("License", 0.4)]),
        ("Building official, if one exists", [("Name", 0.6), ("Office", 0.4)]),
        ("County assessor — for the homestead credit", [("Office", 1.0)]),
    ],
    # check_table always draws four columns; date_w=0 collapses one to zero
    # width and reportlab raises on the negative available width. The rows here
    # already carry their own fill-in rules, so the Date and Notes columns are
    # kept narrow rather than removed.
    notes_header="Notes", date_w=0.8, notes_w=1.5)
flow.append(k.closing_note(
    "Because Arkansas publishes no register of permitting jurisdictions, the "
    "answers you write above are the only record that this question was ever "
    "asked. Date them, keep the emails behind this sheet, and re-check before "
    "you start any later phase — a quorum court or a city council can create a "
    "permit requirement between your foundation and your framing."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ar-permit-kit",
                       "AR.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
