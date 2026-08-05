#!/usr/bin/env python3
"""1.1 Master Project Timeline — rebuilt on the 2026 design system (LANDSCAPE)."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import Flowable, Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width(landscape=True)

SECTION = "Section 1: Project Planning & Foundation"
FORM_ID = "1.1"
FORM_TITLE = "Master Project Timeline"

# [box] Task | Duration | Start | End | Actual Start | Actual End | Status
COLS = [0.42 * inch, 2.93 * inch, 0.95 * inch, 1.00 * inch, 1.00 * inch,
        1.05 * inch, 1.05 * inch, 1.10 * inch]

HEADER = [""] + [Paragraph(t, S["cell-bold"]) for t in
                 ("Task", "Duration", "Start Date", "End Date",
                  "Actual Start", "Actual End", "Status")]


def heights_for(rows, widths, minimum=d.WRITE_ROW_PT, pad=10):
    """Row heights that fit the tallest cell but never drop below the 29pt
    handwriting minimum (titled_table auto-sizes rows carrying flowables,
    which would otherwise produce ~26pt rows)."""
    out = []
    for row in rows:
        tallest = 0.0
        for cell, w in zip(row, widths):
            items = cell if isinstance(cell, list) else [cell]
            h = 0.0
            for it in items:
                if isinstance(it, Flowable):
                    h += it.wrap(w - 10, 10000)[1]
            tallest = max(tallest, h)
        out.append(max(minimum, tallest + pad))
    return out


def phase_table(title, tasks):
    """tasks: (task_text, duration) tuples; task_text None => custom-task row."""
    rows = []
    for task, duration in tasks:
        if task is None:
            first = d.FillIn("Custom task:", font_size=9.5, height=24)
        else:
            first = Paragraph(task, S["cell"])
        dur = Paragraph(duration, S["cell-center"]) if duration else ""
        rows.append([d.Checkbox(), first, dur, "", "", "", "", ""])
    return [d.titled_table(title, HEADER, rows, COLS, S,
                           row_heights=heights_for(rows, COLS)),
            Spacer(1, 10)]


CUSTOM = [(None, ""), (None, "")]

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="A Gantt-style schedule covering typical owner-builder construction "
            "from pre-construction through final completion — six phases, "
            "planned vs. actual dates, and inspection milestones.")

flow.append(d.FillInRow([("Project Name:", 0.55), ("Project Start Date:", 0.45)]))
flow.append(d.FillInRow([("Project Address:", 0.55), ("Target Completion:", 0.45)]))
flow.append(d.FillInRow([("Owner-Builder:", 0.55),
                         ("Total Duration (weeks):", 0.45)]))
flow.append(Spacer(1, 6))

flow += d.h2("INSTRUCTIONS FOR USE", S)
flow.append(Paragraph(
    "<b>Timeline Format:</b> This Gantt-style timeline covers typical "
    "owner-builder construction from pre-construction through final completion. "
    "Adjust durations based on your specific project, climate, and availability.",
    S["body"]))
flow.append(Paragraph(
    "<b>Dependencies:</b> Tasks are organized in typical sequence. Weather "
    "delays, inspection failures, or material delays will push dependent tasks.",
    S["body"]))
flow.append(Paragraph(
    "<b>Weather Buffer:</b> Add 10–15% buffer time for outdoor work in areas "
    "with variable weather. More in harsh climates.", S["body"]))
flow.append(Spacer(1, 4))
flow.append(d.callout_box(
    "⚠ INSPECTION MILESTONES",
    [Paragraph("Tasks marked <b>(INSP)</b> are inspection milestones — work "
               "cannot proceed until the inspection passes.", S["body"])],
    width=CW))
flow.append(Spacer(1, 12))

flow += phase_table("PHASE 1: PRE-CONSTRUCTION (Weeks 1–4)", [
    ("Finalize plans and specifications", "1–2 weeks"),
    ("Submit permit applications", "1 day"),
    ("Await permit approval", "2–4 weeks"),
    ("Secure financing/construction loan", "2–3 weeks"),
    ("Obtain builder's risk insurance", "1 week"),
    ("Interview and hire subcontractors", "2–3 weeks"),
    ("Order long-lead materials (windows, doors, trusses)", "1 week"),
    ("Schedule portable toilet and dumpster", "1–2 days"),
] + CUSTOM)

flow += phase_table("PHASE 2: SITE PREPARATION &amp; FOUNDATION (Weeks 5–8)", [
    ("Call 811 — Utility locate", "2–3 days"),
    ("Site clearing and tree protection", "1–3 days"),
    ("Rough grading and access road", "1–2 days"),
    ("Install temporary power and water", "1–2 days"),
    ("Install erosion control measures", "1 day"),
    ("Foundation layout and batter boards", "1 day"),
    ("Excavation for foundation", "1–2 days"),
    ("Footer forms, rebar, and plumbing stubs", "2–3 days"),
    ("<b>FOOTER INSPECTION (INSP)</b>", "1 day"),
    ("Pour footers", "1 day"),
    ("Footer curing (minimum 3–7 days)", "3–7 days"),
    ("Foundation wall forms and rebar", "2–4 days"),
    ("<b>FOUNDATION WALL INSPECTION (INSP)</b>", "1 day"),
    ("Pour foundation walls", "1 day"),
    ("Foundation curing and form removal", "3–7 days"),
    ("Waterproofing and drainage installation", "1–2 days"),
    ("Backfill and compaction", "1–2 days"),
    ("<b>FOUNDATION FINAL INSPECTION (INSP)</b>", "1 day"),
] + CUSTOM)

flow += phase_table("PHASE 3: ROUGH-IN (Weeks 9–14)", [
    ("Floor framing and subfloor", "3–5 days"),
    ("Wall framing", "5–7 days"),
    ("Roof framing/truss installation", "2–4 days"),
    ("Roof sheathing", "1–2 days"),
    ("<b>FRAMING INSPECTION (INSP)</b>", "1 day"),
    ("Roofing (underlayment and shingles)", "2–4 days"),
    ("Window and exterior door installation", "2–3 days"),
    ("House wrap and exterior moisture barrier", "1–2 days"),
    ("Plumbing rough-in", "3–5 days"),
    ("<b>PLUMBING ROUGH-IN INSPECTION (INSP)</b>", "1 day"),
    ("HVAC rough-in (ducts, vents)", "3–5 days"),
    ("<b>HVAC ROUGH-IN INSPECTION (INSP)</b>", "1 day"),
    ("Electrical rough-in", "4–6 days"),
    ("<b>ELECTRICAL ROUGH-IN INSPECTION (INSP)</b>", "1 day"),
] + CUSTOM)

flow += phase_table("PHASE 4: INSULATION &amp; DRYWALL (Weeks 15–18)", [
    ("Insulation installation (walls, ceiling, floors)", "2–4 days"),
    ("<b>INSULATION INSPECTION (INSP)</b>", "1 day"),
    ("Drywall hanging", "3–5 days"),
    ("Drywall taping and mudding (3 coats)", "5–7 days"),
    ("Drywall sanding and touch-up", "1–2 days"),
    ("Texture application (if applicable)", "1–2 days"),
] + CUSTOM)

flow += phase_table("PHASE 5: FINISH WORK (Weeks 19–26)", [
    ("Interior door installation", "1–2 days"),
    ("Interior trim (baseboards, casings, crown)", "4–6 days"),
    ("Cabinet installation (kitchen and baths)", "2–3 days"),
    ("Countertop templating", "1 day"),
    ("Countertop fabrication (wait time)", "5–10 days"),
    ("Countertop installation", "1 day"),
    ("Interior painting (primer and 2 coats)", "5–7 days"),
    ("Flooring installation (LVP, tile, hardwood)", "3–7 days"),
    ("Plumbing fixtures (sinks, toilets, tubs)", "2–3 days"),
    ("Electrical fixtures (switches, outlets, lights)", "2–3 days"),
    ("HVAC system startup and trim-out", "1–2 days"),
    ("Appliance installation", "1 day"),
    ("Tile work (backsplash, showers)", "2–4 days"),
    ("Exterior siding installation", "4–7 days"),
    ("Exterior trim and soffit/fascia", "2–3 days"),
    ("Gutters and downspouts", "1 day"),
    ("Driveway and walkways", "2–3 days"),
    ("Deck/porch construction (if applicable)", "3–5 days"),
] + CUSTOM)

flow += phase_table("PHASE 6: FINAL COMPLETION (Weeks 27–30)", [
    ("Final grading and drainage", "1–2 days"),
    ("Landscaping (seeding, sod, plants)", "2–4 days"),
    ("Mailbox and address numbers", "1 day"),
    ("Interior and exterior final cleaning", "1–2 days"),
    ("Punch list walkthrough", "1 day"),
    ("Complete punch list items", "2–5 days"),
    ("<b>FINAL BUILDING INSPECTION (INSP)</b>", "1 day"),
    ("<b>CERTIFICATE OF OCCUPANCY (CO)</b>", "1–3 days"),
    ("Utility final connections and activation", "1–2 days"),
    ("Final HVAC system testing and balancing", "1 day"),
    ("Remove temporary facilities (toilet, dumpster)", "1 day"),
    ("Close out construction loan/convert to mortgage", "1–2 weeks"),
] + CUSTOM)

# ---------------- weather delay log
w_cols = [1.30 * inch, 3.20 * inch, 3.00 * inch, 0.90 * inch, 1.10 * inch]
w_header = [Paragraph(t, S["cell-bold"]) for t in
            ("Date", "Delayed Task", "Reason", "Days Lost", "New Target Date")]
w_rows = [["", "", "", "", ""] for _ in range(8)]
flow.append(d.titled_table("WEATHER DELAYS &amp; BUFFER TRACKING", w_header,
                           w_rows, w_cols, S))

flow.append(Spacer(1, 12))
flow.append(d.WriteBox(2.2, label="NOTES & CRITICAL DEPENDENCIES"))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-1-project-planning",
                       "1.1-master-project-timeline.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow, landscape=True)
    print(f"built {out}")
