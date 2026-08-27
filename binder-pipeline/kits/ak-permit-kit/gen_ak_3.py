#!/usr/bin/env python3
"""AK.3 Inspection Sequence — Alaska.

Alaska has no statewide residential building code, so there is no statutory
list of residential inspections to print. What the state DOES have is three
separate inspection regimes drawn on three different lines, none of which is a
borough boundary:

  13 AAC 50.020        State Fire Marshal adopts the 2021 IBC; its Section
                       101.2 Exception 1 excludes "Detached one-, two-, and
                       three-family dwellings" from the adopted code
  AS 18.70.080(a)(2)   the enabling statute reaches only buildings "used for
                       residential purposes containing four or more dwelling
                       units" — so the exclusion is statutory, not a policy
  8 AAC 70.010         the state ELECTRICAL inspection regs apply to "public
                       structures" and places of employment; "public
                       structure" (8 AAC 70.090(4)) means resident housing
                       with MORE THAN ONE rental unit and similar. DOLWD's own
                       page: electrical inspection at "three-plex and above"
  AS 18.60.735         communities under 2,500 population are EXEMPT from the
                       state plumbing code; at or above it, the code applies
                       and DOLWD inspects — single-family houses included
  AS 18.60.715(a)      "The code applies to all new construction"
  AS 18.60.720         statutory CAP on state plumbing permit fees: $2.00 to
                       issue, $1.50 per fixture. Print as a cap, not a price
  AS 18.60.725(a)      written notice of violation must give "specific
                       reference to the section and paragraph of the code"
                       and prescribe the necessary changes
  AS 18.60.725(b)      on a complaint of arbitrary action or incompetence the
                       commissioner may require reinspection by a new
                       inspector "who has no connection with either disputant"
  AS 18.60.710         the department may designate inspection to a utility,
                       and that company "may refuse utility connections"
  AS 18.60.630         electrical: 15 days after written notice, the inspector
                       may notify the power supplier, who "may discontinue
                       services"

Deliberately NOT claimed: a statewide residential inspection sequence; that
the State inspects single-family electrical (it does not); that any Alaska
statute sets a deadline for an inspector to appear.
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

FORM_ID = "AK.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Which of your house actually gets inspected in Alaska — the answer is "
    "rarely \"all of it\" and rarely \"none of it\" — the order it happens "
    "in, and the record to keep for the stages nobody will ever look at.")

flow.append(k.disclaimer(
    "Where a borough or city enforces its own code, its permit card governs "
    "and lists the inspections your job requires."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- who inspects
flow += k.h2_tight("THREE INSPECTION REGIMES, DRAWN ON THREE DIFFERENT LINES")
flow.append(k.body(
    "There is no Alaska residential building code and therefore no statutory "
    "list of inspections. But \"no code\" does not mean \"no inspector.\" "
    "Three separate regimes reach residential construction in this state, and "
    "<b>not one of them is drawn on a borough boundary.</b> They are drawn on "
    "the number of dwelling units in your building and the population of your "
    "community. Work out which apply to you before you assume either that "
    "everything will be inspected or that nothing will."))

who_rows = [
    [k.cellp("<b>Local building department</b><br/>"
             "<font size=9>(borough or city, if any)</font>"),
     k.cellp("Everything — plan review, footings through final, and the "
             "certificate of occupancy — under whatever code that "
             "jurisdiction has adopted. <b>Most of Alaska has none.</b> "
             "Establish yours in AK.4 before reading further."),
     k.cellp("Local ordinance")],
    [k.cellp("<b>State plumbing inspection</b><br/>"
             "<font size=9>DOLWD Mechanical Inspection</font>"),
     k.cellp("Plumbing, gas and fuel piping on <b>new construction</b>, in "
             "communities of <b>2,500 population and above</b> — "
             "<b>single-family houses included</b>. Below 2,500 the community "
             "is statutorily exempt. This is the regime owner-builders are "
             "most often blindsided by, because it arrives where there is no "
             "building department at all."),
     k.cellp("AS 18.60.715(a); AS 18.60.735")],
    [k.cellp("<b>State electrical inspection</b><br/>"
             "<font size=9>DOLWD Mechanical Inspection</font>"),
     k.cellp("\"Public structures\" and places of employment — which by "
             "definition means resident housing with <b>more than one rental "
             "unit</b> and similar. The Department describes its own scope as "
             "<b>three-plex and above</b>. <b>Your single-family house is not "
             "inspected by the State</b> — but the 2020 NEC still applies to "
             "it. See AK.1."),
     k.cellp("8 AAC 70.010; 8 AAC 70.090(4)")],
    [k.cellp("<b>State Fire Marshal</b><br/>"
             "<font size=9>plan review</font>"),
     k.cellp("Buildings \"<i>used for residential purposes containing "
             "<b>four or more dwelling units</b></i>\" and non-residential "
             "occupancies. The adopted code's own text excludes "
             "\"<i>Detached one-, two-, and three-family dwellings</i>.\" "
             "<b>A house is outside it entirely.</b>"),
     k.cellp("AS 18.70.080(a)(2); 13 AAC 50.020")],
]
flow.append(k.ref_table(
    "Who inspects what — and on which line",
    [k.cellp("Regime", bold=True),
     k.cellp("What it reaches", bold=True),
     k.cellp("Authority", bold=True)],
    who_rows, [1.5 * inch, CW - 1.5 * inch - 1.45 * inch, 1.45 * inch]))
flow.append(k.cite(
    "AS 18.60.715(a) — \"<i>The code applies to all new construction</i>\"; "
    "AS 18.60.735 — \"<i>An organized municipality or unorganized village "
    "having less than 2,500 population is exempt from the provisions of "
    "AS 18.60.705 — 18.60.740</i>\"; 8 AAC 70.010; 8 AAC 70.090(4); "
    "AS 18.70.080(a)(2); 13 AAC 50.020, adopting the 2021 IBC with Section "
    "101.2 Exception 1. Scope descriptions confirmed against the Department "
    "of Labor and Workforce Development, Labor Standards and Safety "
    "Division, Mechanical Inspection Section — labor.alaska.gov → Labor "
    "Standards and Safety → Mechanical Inspection, read August 2026."))

flow.append(Spacer(1, 6))
flow.append(k.callout_long(
    "The one that surprises people: a state plumbing inspection with no "
    "building department in sight", [
        Paragraph("An owner-builder in a Mat-Su or Interior community over "
                  "2,500 people typically concludes, correctly, that no "
                  "government will review the house. Then a <b>State of "
                  "Alaska</b> plumbing inspector arrives, because the "
                  "plumbing code is not administered by the borough — it is "
                  "administered by the Department of Labor and Workforce "
                  "Development, and its trigger is <b>population, not "
                  "jurisdiction</b>.", S["body"]),
        Paragraph("The code being enforced is the <b>2018 Uniform Plumbing "
                  "Code</b>, adopted by regulation (8 AAC 63.010(a)(1)) as "
                  "the minimum standard \"<i>to be followed throughout the "
                  "state</i>.\" <b>Do not read the statute instead:</b> "
                  "AS 18.60.705 still names the <b>1997</b> UPC on its face, "
                  "because it adopts that edition \"<i>unless the department "
                  "adopts by regulation a later edition</i>\" — and the "
                  "department did. The statute is what a search engine hands "
                  "you; the regulation is what the inspector is holding, and "
                  "they are twenty-one years and seven editions apart.", S["body"]),
        Paragraph("<b>And do not trust the state's own PDFs on the "
                  "edition.</b> The Department of Labor publishes "
                  "consolidated statute-and-regulation booklets, and three of "
                  "them are stale in three different directions: its "
                  "<i>Electrical Safety</i> booklet still prints 8 AAC 70.025 "
                  "as adopting the <b>2017</b> NEC when the live code adopts "
                  "the <b>2020</b>; one plumbing PDF on its site prints the "
                  "<b>2015</b> UPC; another prints the correct <b>2018</b>. "
                  "Three official documents, three different answers, all "
                  "linked from the same agency.", S["body"]),
        Paragraph("<b>Confirm your community's population status before you "
                  "rough in, and confirm every edition against the "
                  "Administrative Code itself at akleg.gov.</b> The "
                  "population threshold is a real cliff: on one side the code "
                  "and the inspection apply to your house, on the other the "
                  "community is exempt outright.", S["body"]),
    ]))
flow.append(Spacer(1, 6))
flow.append(d.FillInRow([("Community:", 0.34), ("Population / source:", 0.33),
                         ("State plumbing? Y / N:", 0.33)]))

# ---------------------------------------------------------------- fees
flow += k.h2_tight("WHAT A STATE PLUMBING PERMIT COSTS")
flow.append(k.body(
    "Where the state plumbing code applies, permits \"<i>will be issued on a "
    "fee basis in accordance with the schedule outlined in AS "
    "18.60.720</i>.\" That statute is a <b>ceiling</b>, not a price list — "
    "it says fees \"<i>may not exceed</i>\" the amounts it sets — and the "
    "amounts have not been revisited in a long time. For issuing each permit: "
    "<b>$2.00</b>. Per plumbing fixture or trap: <b>$1.50</b>. Building "
    "sewer: <b>$5.00</b>. Private sewage disposal system: <b>$10.00</b>. "
    "Water heater and vent: <b>$1.50</b>. Gas piping system of one to five "
    "outlets: <b>$1.50</b>."))
flow.append(k.body(
    "Ask the Mechanical Inspection Section what it currently charges rather "
    "than assuming these figures are the invoice. The point worth carrying "
    "away is the shape of the thing: <b>the cost of this permit is never the "
    "reason to skip it.</b> Skipping it means an uninspected plumbing system "
    "in a house you will one day have to sell or insure."))
flow.append(k.cite(
    "8 AAC 63.020; AS 18.60.720(a)(1), (2)(A), (2)(B), (2)(E), (2)(F), "
    "(2)(G). Read at akleg.gov, August 2026. Confirm current charges with "
    "the Mechanical Inspection Section before budgeting."))
flow.append(Spacer(1, 4))
flow.append(d.FillInRow([("Permit fee quoted:", 0.4), ("By:", 0.3),
                         ("Date:", 0.3)]))

# ---------------------------------------------------------------- sequence
flow += k.h2_tight("THE SEQUENCE — WHAT MUST BE COMPLETE BEFORE YOU CALL")
flow.append(k.body(
    "Below is the order a new house on a frost-protected or deep foundation "
    "is normally built and checked in Alaska. Where a borough or city "
    "enforces a code, <b>your permit card governs</b> and may add or rename "
    "stages — confirm it at your first inspection. Where none does, work the "
    "same sequence anyway and record each stage yourself: the column that "
    "matters then is not \"result\" but \"photographed.\""))
seq = [
    ("1. Site and layout",
     "Setbacks and elevation confirmed against the survey, wastewater "
     "components staked clear of the building envelope and the drive, and "
     "any floodplain elevation requirement identified before excavation.",
     "Local / AK.2"),
    ("2. Excavation and subgrade",
     "Bearing surface exposed and, on any site with permafrost risk, checked "
     "against the geotechnical report before anything is placed. This is the "
     "one stage in Alaska that cannot be corrected later at reasonable cost.",
     "Geotech"),
    ("3. Footing / foundation",
     "Forms, reinforcing and any sub-slab or perimeter insulation in place "
     "before concrete. Confirm frost depth or the frost-protected shallow "
     "foundation detail from your design — Alaska frost depths vary enormously "
     "and no state figure exists.",
     "Local"),
    ("4. Under-slab and buried services",
     "Under-slab drain, waste and vent piping under test; water service and "
     "any buried electrical in; vapor retarder and fill placed, before the "
     "pour. <b>Where the state plumbing code applies this stage is a state "
     "inspection.</b>",
     "AS 18.60.715(a)"),
    ("5. Damp-proofing and backfill",
     "Foundation waterproofing or damp-proofing applied and drainage placed "
     "before backfill. Backfilling early is the commonest way to lose a stage "
     "you cannot re-open.",
     "Local"),
    ("6. Plumbing rough-in",
     "Water, waste and vent complete and under test; fuel gas piping "
     "pressure-tested. Inspected by the State in communities of 2,500 and "
     "above, and by your local department if one exists.",
     "AS 18.60.715(a); 8 AAC 63.010"),
    ("7. Mechanical rough-in",
     "Heating distribution, combustion air, venting and equipment set. If you "
     "install a boiler or unfired pressure vessel, see the installation "
     "notice in AK.5 before you close the wall.",
     "Local; AK.5"),
    ("8. Electrical rough-in",
     "Boxes, cable, panel, and the grounding electrode system in. <b>Not "
     "inspected by the State on a single-family house</b> — but the 2020 NEC "
     "still applies, and this is the stage a utility or a lender's inspector "
     "is most likely to ask about.",
     "8 AAC 70.025(a)"),
    ("9. Framing",
     "Roof, framing, bracing, firestopping and sheathing complete, after the "
     "rough-ins so nothing has to be re-cut. Photograph every wall before it "
     "is covered.",
     "Local"),
    ("10. Insulation, air barrier and vapor retarder",
     "Before any wall or ceiling covering. <b>In this climate this is the "
     "stage that decides whether the house lasts</b>, and in most of Alaska "
     "it is the stage with no inspector at all. Treat the self-record here as "
     "non-optional.",
     "AK.2 energy"),
    ("11. Finals — each trade",
     "Plumbing and gas final where the state code applies; electrical and "
     "mechanical finals; building final and the certificate of occupancy "
     "where a local department issues one.",
     "Local; state"),
    ("12. Smoke and carbon monoxide alarms",
     "Required in <b>every dwelling unit in Alaska</b>, code or no code — see "
     "AK.2. Verify type, placement and interconnection at final, and keep the "
     "receipt and a photograph.",
     "AS 18.70.095; 13 AAC 50.030(b)"),
]
rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in seq]
flow.append(k.ref_table(
    "Working Alaska residential sequence",
    [k.cellp("Stage", bold=True),
     k.cellp("What must be complete / what is verified", bold=True),
     k.cellp("Who, if anyone", bold=True)],
    rows, [1.35 * inch, CW - 1.35 * inch - 1.3 * inch, 1.3 * inch]))
flow.append(k.cite(
    "Stages carrying a state citation are inspected by the State where the "
    "population threshold is met. Stages marked \"Local\" are common practice "
    "and are inspected only if a borough or city enforces a code — they are "
    "<b>not</b> Alaska law. Nothing in this sequence is a statutory list, "
    "because Alaska does not publish one for houses."))

# ---------------------------------------------------------------- rights
flow += k.h2_tight("YOUR RIGHTS WHEN A STATE INSPECTOR DOES COME")
flow.append(k.body(
    "The plumbing statute gives an owner-builder two protections that are "
    "unusually explicit, and almost nobody invokes them."))
flow.append(k.bullet(
    "<b>A written notice that cites the code.</b> \"<i>A department "
    "inspector <b>shall</b> give written notice to the owner of a "
    "constructed premise or the contractor of a premise under construction of "
    "each violation of the code. The notice of violation <b>must accurately "
    "describe the violation and give specific reference to the section and "
    "paragraph of the code</b>. In addition, the notice must <b>prescribe the "
    "necessary changes</b> so that the work will comply with the code.</i>\" "
    "You are entitled to know exactly which paragraph you failed, and to be "
    "told what would fix it — in writing. (AS 18.60.725(a))"))
flow.append(k.bullet(
    "<b>A fresh inspector if you think you were treated arbitrarily.</b> "
    "\"<i>In case of complaints by a contractor, builder, or installer "
    "charging arbitrary actions or incompetence on the part of an inspector, "
    "the commissioner, after reviewing written presentation of the dispute, "
    "may require reinspection by a <b>new inspector who has no connection "
    "with either disputant</b>.</i>\" Put the dispute in writing; the "
    "statute is built around a written presentation. (AS 18.60.725(b))"))
flow.append(k.bullet(
    "<b>An appeal with a real clock.</b> A notice of violation \"<i>is final "
    "unless the person affected or the owner or contractor of a construction "
    "premise affected files an appeal with the commissioner <b>within 30 "
    "days</b> after receipt of the notice</i>,\" in writing, specifying the "
    "objections and the relief sought. (8 AAC 63.025(a))"))
flow.append(Spacer(1, 4))
flow.append(k.callout("What no Alaska statute gives you", [
    Paragraph("There is <b>no deadline</b> anywhere in Alaska law for an "
              "inspector to appear after you request an inspection, and no "
              "deemed-approval remedy if one never does. Where a local "
              "department issues your permit, ask what its practice is and "
              "write it into AK.4. Where the State is your only inspector, "
              "build the wait into the schedule rather than into the "
              "critical path — the season is short enough already.",
              S["body"]),
]))

# ---------------------------------------------------------------- utility
flow += k.h2_tight("THE INSPECTION THAT CAN LEAVE YOU WITHOUT POWER")
flow.append(k.body(
    "Two statutes let an inspection failure reach your utility service "
    "directly, and they run whether or not a building department exists."))
flow.append(k.body(
    "On the <b>plumbing</b> side, the department \"<i>may by regulation "
    "designate appropriate inspection to a public or private utility "
    "company</i>,\" and \"<i>a company so designated <b>may refuse utility "
    "connections</b> if an installation does not meet the requirements of "
    "this code</i>.\" (AS 18.60.710) On the <b>electrical</b> side, an "
    "authorized inspector gives written notice of each violation, and "
    "\"<i>if within <b>15 days</b> after receipt of written notice ... the "
    "person notified does not rectify the condition, the inspector shall "
    "notify the electric utility ... Upon notice in writing from the "
    "inspector, the supplier of electrical power <b>may discontinue "
    "services</b> to the premises</i>.\" (AS 18.60.630)"))
flow.append(k.body(
    "Separately from any of that, <b>your utility sets its own conditions "
    "for energizing a new service</b>, and in unincorporated Alaska those "
    "conditions are often the only technical review your electrical work will "
    "ever receive. Ask your cooperative what it requires <i>before</i> you "
    "set the meter base, not after — the answer varies by utility and is not "
    "set by statute."))
flow.append(Spacer(1, 4))
# "Requires before energizing" is the substantive answer and wants a whole
# rule to itself; sharing a line with two other fields left about 45pt to
# write a sentence in.
flow.append(d.FillInRow([("Utility:", 0.62), ("Confirmed:", 0.38)]))
flow.append(d.FillInRow([("Requires before energizing:", 1.0)]))

# ---------------------------------------------------------------- the log
flow += k.h2_tight("INSPECTION AND SELF-VERIFICATION LOG")
flow.append(k.body(
    "Fill this in as it happens, not from memory. Where an inspector came, "
    "record who and the result. <b>Where none did, that is the entry that "
    "matters most</b> — write the date you completed the stage, and note "
    "whether you photographed it. In Alaska this log and your photographs "
    "are frequently the only evidence that exists about how your house was "
    "built, and a lender, an insurer, an appraiser or a buyer will ask for "
    "exactly that in place of a certificate you were never issued."))

log_header = [k.cellp("Stage", bold=True),
              k.cellp("Who", bold=True),
              k.cellp("Called", bold=True),
              k.cellp("Done", bold=True),
              k.cellp("Photos", bold=True),
              k.cellp("Result / notes", bold=True)]
log_names = [
    "Site &amp; layout", "Excavation / subgrade", "Footing / foundation",
    "Under-slab services", "Damp-proof / backfill", "Plumbing rough",
    "Mechanical rough", "Electrical rough", "Framing",
    "Insulation / air barrier", "Final — plumbing", "Final — electrical",
    "Final — mechanical", "Final — building", "Smoke / CO alarms",
    "",
]
log_rows = [[k.cellp(n) if n else "", "", "", "", "", ""] for n in log_names]
# "Photos" is 37pt at 9.5pt bold and the cell eats ~8pt of padding, so 0.56in
# split it to "Phot / os". 0.66in clears it; the notes column absorbs the
# difference and still runs over three inches.
widths = [1.24 * inch, 0.66 * inch, 0.62 * inch, 0.58 * inch, 0.66 * inch]
widths.append(CW - sum(widths))
flow.append(d.titled_table(
    "Stage log — record every one, inspected or not", log_header, log_rows,
    widths, S, row_heights=[30] * len(log_rows)))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Certificate of occupancy issued (if any):", 0.58),
                         ("Number:", 0.42)]))

flow.append(Spacer(1, 10))
flow.append(k.sources_table([
    ("No statewide residential building code, and the adopted state code "
     "expressly excludes detached one-, two- and three-family dwellings",
     "AS 18.70.080(a)(2); 13 AAC 50.020"),
    ("The state plumbing code applies to all new construction, and "
     "communities under 2,500 population are exempt",
     "AS 18.60.715(a); AS 18.60.735"),
    ("The current statewide plumbing standard is the 2018 UPC by regulation, "
     "not the 1997 edition still named in the statute",
     "8 AAC 63.010(a)(1); AS 18.60.705(a)"),
    ("State electrical inspection reaches public structures and places of "
     "employment — not a single-family house",
     "8 AAC 70.010; 8 AAC 70.090(4)"),
    ("Statutory ceiling on state plumbing permit fees: $2.00 to issue, $1.50 "
     "per fixture, $10.00 for a private sewage disposal system",
     "8 AAC 63.020; AS 18.60.720(a)"),
    ("Written notice of violation must cite the section and paragraph and "
     "prescribe the fix; a disputed inspection may be redone by an "
     "unconnected inspector; 30 days to appeal",
     "AS 18.60.725(a), (b); 8 AAC 63.025(a)"),
    ("A designated utility may refuse connection over plumbing; a power "
     "supplier may discontinue service 15 days after an unremedied "
     "electrical violation notice", "AS 18.60.710; AS 18.60.630"),
    ("Smoke and carbon monoxide alarms are required in every dwelling unit "
     "in the state", "AS 18.70.095; 13 AAC 50.030(b)"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ak-permit-kit",
                       "AK.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
