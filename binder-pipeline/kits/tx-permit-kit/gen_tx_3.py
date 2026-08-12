#!/usr/bin/env python3
"""TX.3 Inspection Sequence — Texas, two tracks.

Sources verified August 2026:
  San Antonio Residential Inspection Guide (docsonline.sanantonio.gov) —
    stage inspections; the six required finals (Building, Electrical,
    Mechanical, Gas, Plumbing, Tree) before the CO and utility transfer
  Fort Worth General Inspections List (fortworthtexas.gov) — foundation
    approved with steel in place before concrete; framing only after trade
    rough-ins; final "finals out" all permits and supports the CO
  Health & Safety Code §§ 366.004, 366.051; 30 TAC Ch. 285 — OSSF inspected
    by the authorized agent before cover/use; construction without the
    permit and approved plan is unlawful
  Occ. Code § 1305.201(e); 16 TAC § 73.100 — unincorporated electrical work
    must meet the 2023 NEC, but no state agency inspects it (TDLR licenses
    people, not houses)
  Insurance Code § 2210.2515; tdi.texas.gov/wind — windstorm inspections at
    each construction phase after the WPI-1; WPI-8/WPI-8-E at the end
  Health & Safety Code § 388.004 — the three energy-compliance routes and
    the three-year documentation duty
  Loc. Gov't Code § 233.154 — the three private inspections in opt-in
    counties (El Paso County program as the worked example, epcounty.com)
  Bluebonnet Electric Cooperative tariff, Section III (bluebonnet.coop) —
    meter-loop inspection required for all new locations; $125 re-inspection

Still deliberately hedged: the generic municipal ladder is labelled typical
(exact names and count vary by city); utility meter-release requirements
differ by provider (Bluebonnet is the verified printed example); and
lender/insurer inspections are framed as practical reality, not law.
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

FORM_ID = "TX.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Inside a city: the inspection ladder and who runs it. Outside one: "
    "the five separate inspectors that exist, the gaps where nobody "
    "inspects at all, and a log for both.")

flow.append(k.disclaimer(
    "On Track A your permit card lists the inspections your job requires — "
    "it governs. On Track B, this document is the closest thing to a "
    "permit card you will get."))
flow.append(Spacer(1, 10))

# ================================================================ TRACK A
flow += k.h2_tight("TRACK A — THE MUNICIPAL LADDER")
flow.append(k.body(
    "No Texas statute enumerates residential inspections; each city's "
    "adopted IRC and local amendments do. The ladder below is the "
    "<b>typical</b> shape — verify names and count against your own "
    "city's published list. Two verified anchors: <b>San Antonio</b> "
    "publishes a Residential Inspection Guide with inspections at each "
    "covered stage, and requires final inspections in <b>Building, "
    "Electrical, Mechanical, Gas, Plumbing, and a Tree Inspection</b> "
    "before the certificate of occupancy and utility transfer. <b>Fort "
    "Worth's</b> General Inspections List has the foundation approved "
    "with steel in place before concrete, framing called only after the "
    "trade rough-ins, and a final inspection that \"finals out\" all "
    "permits and supports the CO."))

seq = [
    ("1. T-pole / temporary power",
     "Temporary construction service inspected and released to the "
     "utility."),
    ("2. Plumbing rough (underground)",
     "Under-slab plumbing inspected before the slab is poured."),
    ("3. Foundation / pre-pour",
     "Forms, steel, and embedments in place — approved before any "
     "concrete is placed (Fort Worth words it exactly that way)."),
    ("4. Framing + trade rough-ins",
     "Framing with electrical, plumbing, and mechanical rough-ins "
     "complete — called only after the trades are in. Coastal: windstorm "
     "nailing/connector inspections fall here too (see Track B, "
     "windstorm)."),
    ("5. Insulation / energy",
     "Insulation and air-sealing verified against the city's energy code "
     "before cover."),
    ("6. Wallboard",
     "Some cities inspect drywall fastening before tape and float."),
    ("7. Gas test",
     "Pressure test witnessed before the meter is set."),
    ("8. Sewer / water yard lines",
     "Yard utilities inspected before burial."),
    ("9. Trade finals",
     "Electrical, plumbing, mechanical (and gas) each final out."),
    ("10. Building final → CO",
     "The building final closes the permit; the certificate of occupancy "
     "issues (San Antonio requires the CO application after all finals; "
     "Fort Worth issues the CO at final-out)."),
]
rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b)] for a, b in seq]
flow.append(k.ref_table(
    "Typical municipal ladder — verify locally; names and count vary",
    [k.cellp("Inspection", bold=True),
     k.cellp("What must be complete / what is verified", bold=True)],
    rows, [2.0 * inch, CW - 2.0 * inch]))
flow.append(k.cite(
    "San Antonio Residential Inspection Guide, docsonline.sanantonio.gov; "
    "Fort Worth General Inspections List, fortworthtexas.gov — both read "
    "August 2026. The ladder itself is a typical composite, not any one "
    "city's list: your permit card governs."))

flow += k.h2_tight("TRACK A — INSPECTION LOG")
log_header = [k.cellp("Inspection", bold=True),
              k.cellp("Called", bold=True),
              k.cellp("Held", bold=True),
              k.cellp("Result", bold=True),
              k.cellp("Inspector", bold=True),
              k.cellp("Corrections required / notes", bold=True)]
log_names = [
    "T-pole / temp power", "Plumbing rough (u/g)", "Foundation / pre-pour",
    "Framing + rough-ins", "Insulation / energy", "Wallboard", "Gas test",
    "Yard lines", "Final — electrical", "Final — plumbing",
    "Final — mechanical", "Final — building / CO", "", "",
]
log_rows = [[k.cellp(n) if n else "", "", "", "", "", ""] for n in log_names]
widths = [1.45 * inch, 0.72 * inch, 0.72 * inch, 0.62 * inch, 1.05 * inch]
widths.append(CW - sum(widths))
flow.append(d.titled_table(
    "Track A inspection log", log_header, log_rows, widths, S,
    row_heights=[30] * len(log_rows)))

# ================================================================ TRACK B
flow += k.h2_tight("TRACK B — THERE IS NO LADDER; THERE ARE FIVE SEPARATE "
                   "INSPECTORS")
flow.append(k.body(
    "In the unincorporated county nobody owns your job the way a city "
    "inspections department does. Each inspection below exists on its own "
    "legal track, with its own inspector, and <b>you</b> are the only "
    "person who will ever sequence them. Between them are gaps — work "
    "that is regulated but never inspected — covered honestly below, "
    "because pretending an inspection exists is how corners get built "
    "wrong."))

b_rows = [
    [k.cellp("<b>Septic (OSSF)</b>"),
     k.cellp("The authorized agent (usually the county) inspects the "
             "installation under 30 TAC Ch. 285 <b>before the system is "
             "covered or used</b>. Constructing without the permit and "
             "approved plan is unlawful."),
     k.cellp("H&amp;S Code §§ 366.004, 366.051; 30 TAC Ch. 285")],
    [k.cellp("<b>Windstorm</b><br/>(coastal only)"),
     k.cellp("After the WPI-1 notice, TDI or your engineer inspects at "
             "<b>each construction phase</b> — contact TDI for each phase "
             "when TDI is the inspector. WPI-8/WPI-8-E certificate at the "
             "end. A phase covered up uninspected cannot be certified."),
     k.cellp("Ins. Code § 2210.2515; tdi.texas.gov/wind")],
    [k.cellp("<b>Energy code</b>"),
     k.cellp("Your chosen § 388.004 route IS the inspection: an accredited "
             "program (e.g., an ERI/ENERGY STAR rating), a private "
             "code-certified inspector, or the ESL builder "
             "self-certification form. Keep the documentation three years; "
             "give the owner a copy."),
     k.cellp("H&amp;S Code § 388.004")],
    [k.cellp("<b>Subchapter F counties only</b>"),
     k.cellp("Three private inspections YOU arrange and pay for: "
             "foundation before concrete, framing/mechanical before "
             "drywall, and final — by one of the six listed inspector "
             "types — with county notice forms where required. El Paso "
             "County runs a worked example of this program."),
     k.cellp("Loc. Gov't Code § 233.154; epcounty.com")],
    [k.cellp("<b>Utility meter release</b>"),
     k.cellp("The de facto final. Electric cooperatives require a passing "
             "meter-loop inspection before energizing new construction — "
             "Bluebonnet Electric's tariff requires it \"for all new and "
             "existing locations,\" with a $125 re-inspection fee on "
             "failure. Requirements differ by utility; some require a "
             "licensed electrician's certification or a third-party "
             "inspection. <b>Call your provider's new-construction desk "
             "before you wire.</b>"),
     k.cellp("Bluebonnet tariff § III (verified example)")],
]
flow.append(k.ref_table(
    "The five inspectors that exist on Track B",
    [k.cellp("Who", bold=True), k.cellp("What actually happens", bold=True),
     k.cellp("Authority", bold=True)],
    b_rows, [1.35 * inch, CW - 1.35 * inch - 1.55 * inch, 1.55 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "The honest gap — licensing applies; routine inspection does not "
    "exist", [
        Paragraph("<b>Electrical:</b> nobody inspects by default. The "
                  "licensing law still applies and the work must meet the "
                  "2023 NEC even in unincorporated areas (Occ. Code "
                  "§ 1305.201(e)) — but no state agency performs "
                  "residential electrical inspections there. TDLR licenses "
                  "people, not houses. The practical inspectors are the "
                  "utility at meter release, your lender's draw inspector, "
                  "and your insurer. The same logic covers plumbing and "
                  "HVAC: code duties without a code official.", S["body"]),
        Paragraph("What to do about it: hire a private code-certified "
                  "inspector for the stages a city would have inspected — "
                  "pre-pour, rough-in, pre-drywall, final. It is the "
                  "cheapest insurance on the job, and on the energy "
                  "chapter it doubles as your § 388.004(2) compliance "
                  "route.", S["body"]),
    ]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>Lender and insurer inspections</b> — construction-loan draw "
    "inspections and the insurer's replacement-cost or four-point-style "
    "reviews — are, in practice, the only whole-house quality gates on "
    "this track. That is practical reality, not law; treat their "
    "checklists as a floor, not a code."))

flow.append(k.callout("There is no CO out here — these are the occupancy "
                      "gates", [
    Paragraph("No statute creates a certificate of occupancy in "
              "unincorporated Texas. What functions instead: the <b>OSSF "
              "approval</b> (you cannot lawfully use the septic system "
              "without the permit — H&amp;S Code § 366.051), the "
              "<b>meter release</b> (no power without it), and — coastal "
              "— the <b>windstorm certificate</b>, without which TWIA "
              "coverage is not available. Clear all three and you are as "
              "\"final\" as Track B gets.", S["body"]),
]))

flow += k.h2_tight("TRACK B — INSPECTION LOG")
b_log_names = [
    "OSSF — site evaluation", "OSSF — pre-cover / final",
    "Windstorm — foundation phase", "Windstorm — framing phase",
    "Windstorm — final / WPI-8", "Energy — route inspection / cert",
    "Subch. F — foundation pre-pour", "Subch. F — frame pre-drywall",
    "Subch. F — final", "Private inspector — rough-in",
    "Private inspector — final", "Meter-loop / utility release", "", "",
]
b_log_rows = [[k.cellp(n) if n else "", "", "", "", "", ""]
              for n in b_log_names]
flow.append(d.titled_table(
    "Track B inspection log", log_header, b_log_rows, widths, S,
    row_heights=[30] * len(b_log_rows)))

flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("OSSF operation approved:", 0.4),
                         ("Meter released:", 0.3),
                         ("WPI-8 issued (coastal):", 0.3)]))

flow.append(Spacer(1, 8))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026). Municipal ladders: San Antonio "
    "Residential Inspection Guide (docsonline.sanantonio.gov) — six "
    "required finals before the CO; Fort Worth General Inspections List "
    "(fortworthtexas.gov) — steel before concrete, framing after "
    "rough-ins, final-out. OSSF inspection before cover/use and the "
    "unlawfulness of unpermitted construction — Health &amp; Safety Code "
    "§§ 366.004, 366.051; 30 TAC Ch. 285. Unincorporated electrical work "
    "must meet the state electrical code (2023 NEC) with no routine state "
    "inspection — Occ. Code § 1305.201(e); 16 TAC § 73.100. Windstorm "
    "phase inspections and certificates — Insurance Code § 2210.2515; "
    "tdi.texas.gov/wind. Energy compliance routes and the three-year "
    "documentation duty — Health &amp; Safety Code § 388.004. Subchapter F "
    "private inspections and notices — Local Gov't Code § 233.154 (El "
    "Paso County program, epcounty.com). Meter-loop inspection — "
    "Bluebonnet Electric Cooperative tariff, Section III: one verified "
    "example; your utility's requirements govern."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "tx-permit-kit",
                       "TX.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
