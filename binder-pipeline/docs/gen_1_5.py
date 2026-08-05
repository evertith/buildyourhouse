#!/usr/bin/env python3
"""1.5 Foundation Checklist — exemplar document on the 2026 design system."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 1: Project Planning & Foundation"
FORM_ID = "1.5"
FORM_TITLE = "Foundation Checklist"


TASK_CELL_W = None  # set after CW known


def pack_fields(fields, cell_w, font_size=9.5, min_rule=40):
    """Greedily pack (label, fraction) fields into lines so every drawn rule
    keeps at least min_rule pt of writing room inside a table cell."""
    from reportlab.pdfbase import pdfmetrics
    lines, line, used = [], [], 0.0
    needs = {}
    for label, _frac in fields:
        need = pdfmetrics.stringWidth(label, d.BODY, font_size) + 6 + min_rule
        needs[label] = need
        if line and used + need + 18 > cell_w:
            lines.append(line)
            line, used = [], 0.0
        line.append(label)
        used += need + (18 if len(line) > 1 else 0)
    if line:
        lines.append(line)
    out = []
    for labels in lines:
        total = sum(needs[lb] for lb in labels)
        out.append(d.FillInRow(
            [(lb, needs[lb] / total) for lb in labels],
            font_size=font_size, height=24))
    return out


def task_rows(items, cell_w):
    """items: list of task strings, or (task, fillins) tuples where fillins is a
    list of (label, fraction) drawn inside the task cell. Fields are re-packed
    so no rule drops below ~0.55in of writing room."""
    rows = []
    for it in items:
        if isinstance(it, tuple):
            text, fields = it
            cell = []
            if text:
                cell.append(Paragraph(text, S["cell"]))
            cell.extend(pack_fields(fields, cell_w))
            rows.append(cell)
        else:
            rows.append(Paragraph(it, S["cell"]))
    return rows


def check_table(title, items, notes_header="Notes / Measurements"):
    header = ["", Paragraph("Task", S["cell-bold"]),
              Paragraph("Date", S["cell-bold"]),
              Paragraph(notes_header, S["cell-bold"])]
    task_w = CW - 0.42 * inch - 1.0 * inch - 2.0 * inch
    rows = [[d.Checkbox(), cell, "", ""]
            for cell in task_rows(items, task_w - 10)]
    col = [0.42 * inch, task_w, 1.0 * inch, 2.0 * inch]
    return [d.titled_table(title, header, rows, col, S), Spacer(1, 8)]


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Pre-pour preparation, pour-day execution, and post-pour finishing "
            "— every step from batter boards to backfill.")

# Project info block
flow.append(d.FillInRow([("Project Name:", 0.5), ("Foundation Type:", 0.5)]))
flow.append(d.FillInRow([("Owner-Builder:", 0.5), ("Start Date:", 0.5)]))
flow.append(d.FillInRow([("Foundation Contractor:", 0.5),
                         ("Target Completion:", 0.5)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>INSTRUCTIONS:</b> This checklist covers all phases of foundation "
    "construction: pre-pour preparation, pour day activities, and post-pour "
    "finishing. A proper foundation is critical — take your time, double-check "
    "measurements, and don't skip inspections. Document everything with photos.",
    S["body"]))
flow.append(Spacer(1, 4))

flow.append(d.callout_box(
    "⚠ CRITICAL REMINDER — Foundation work cannot proceed until:",
    [Paragraph("• Building permit is approved and posted on site", S["body"]),
     Paragraph("• Site preparation is 100% complete", S["body"]),
     Paragraph("• All utilities are located (811 call completed)", S["body"]),
     Paragraph("• Foundation layout has been verified and approved", S["body"])]))
flow.append(Spacer(1, 10))

# ---------------- SECTION A
flow += d.h2("SECTION A: PRE-POUR PREPARATION", S)

flow += check_table("A1: Foundation Layout & Batter Boards", [
    "Review foundation plans and verify all dimensions",
    "Establish reference point/benchmark (permanent marker, stake, etc.)",
    "Set up batter boards 3–4 feet outside all corners",
    "String layout lines between batter boards",
    "Verify all corners are square (3-4-5 method or diagonal measurement)",
    ("Diagonal measurements (must be equal!):",
     [("A:", 0.5), ("B:", 0.5)]),
    "Mark excavation limits with spray paint or stakes",
    "Take photos of string layout from multiple angles",
    "Have layout verified by surveyor or experienced builder (recommended)",
])

flow += check_table("A2: Excavation", [
    ("Verify frost depth requirement (check local code):",
     [("Frost depth (in):", 1.0)]),
    "Excavate to required depth below finish grade (frost depth + footer)",
    "Verify excavation depth at all corners and mid-points (record below)",
    ("", [("NE:", 0.25), ("NW:", 0.25), ("SE:", 0.25), ("SW:", 0.25)]),
    "Remove all loose soil, roots, organic matter from excavation",
    "Ensure excavation bottom is level and undisturbed soil",
    "Document any rock, ledge, or unusual soil conditions encountered",
    "Stockpile excavated soil away from work area (for later backfill)",
])

flow += check_table("A3: Gravel Base & Compaction", [
    "Install gravel base per plan (typically 4–6\" of crushed stone)",
    ("", [("Gravel type used:", 0.6), ("Depth (in):", 0.4)]),
    "Compact gravel base with plate compactor or roller",
    "Verify base is level (max 1/4\" variance in 10 feet)",
    "Install drainage tile around perimeter (if required)",
    "Verify drainage tile slopes to daylight or sump (1/8\" per foot min)",
])

flow += check_table("A4: Footer Forms & Rebar", [
    "Install footer forms per plan dimensions",
    ("", [("Footer width (in):", 0.5), ("Footer depth (in):", 0.5)]),
    "Forms are straight, level, and properly braced",
    "Verify footer width and depth at multiple locations",
    "Install rebar per plan (typically #4 or #5, 2 bars continuous)",
    ("", [("Rebar size: #", 0.4), ("Configuration:", 0.6)]),
    "Rebar is elevated on chairs (3\" min clearance from bottom)",
    "All rebar splices overlap minimum 18\" and are tied with wire",
    "Rebar is clean (no rust scale, oil, or debris)",
    "Corner rebar is properly bent or overlapped (no gaps)",
])

flow += check_table("A5: Plumbing Under-Slab Rough-In", [
    "Install all plumbing stubs per plan (water supply, drains, vents)",
    "Verify plumbing stub locations match plan dimensions",
    "All drain pipes slope properly (1/4\" per foot minimum)",
    "Pressure test water supply lines (if required by inspector)",
    "Cap all plumbing stubs to prevent concrete entry during pour",
    "Support all pipes properly (no sagging, proper bedding in gravel)",
    "Take photos of all plumbing locations before pour",
])

flow += check_table("A6: Vapor Barrier (for slab-on-grade)", [
    "Install vapor barrier (minimum 6 mil poly, 10 mil preferred)",
    "Overlap all seams minimum 6\" and tape with approved sealing tape",
    "Run vapor barrier up sides of forms (3–6\" above slab height)",
    "Seal vapor barrier around all plumbing penetrations",
    "Repair any tears or punctures with approved patch/tape",
    "Place sand layer over vapor barrier if required (prevents punctures)",
])

flow += check_table("A7: Foundation Wall Forms (if applicable)", [
    "Erect foundation wall forms (ICF, wood, or metal forms)",
    ("", [("Wall height (in):", 0.5), ("Wall thickness (in):", 0.5)]),
    "Forms are plumb, level, and properly braced (check with 4' level)",
    "Install tie rods/snap ties at proper spacing per form manufacturer",
    "Install vertical rebar in walls per plan (typically #4 @ 16–24\" o.c.)",
    "Install horizontal rebar per plan (min 2 continuous bars)",
    "Tie vertical rebar to footer rebar (dowels or epoxy anchors)",
    "Install anchor bolts at proper spacing (typically 6' o.c., 12\" from corners)",
    ("", [("Anchor bolt size:", 0.42), ("Embedment depth (in):", 0.58)]),
    "Create forms for window wells, bulkhead openings (if applicable)",
    "Coat forms with release agent/oil (prevents concrete adhesion)",
    "Double-check all dimensions before calling for inspection",
])

flow.append(Paragraph("A8: Pre-Inspection Checklist", S["h3"]))
flow.append(Paragraph("Critical items to verify before calling the inspector:",
                      S["body"]))
flow.append(d.items_checklist([
    "Foundation layout is square (diagonals match within 1/4\")",
    "Excavation depth meets or exceeds frost depth requirement",
    "Footer dimensions (width and depth) match approved plans",
    "Rebar size, spacing, and placement meet code requirements",
    "Rebar has proper concrete cover (3\" min from soil, 2\" from forms)",
    "All plumbing under slab is installed and positioned correctly",
    "Vapor barrier is intact with no tears or unsealed penetrations",
    "Forms are clean, braced, and will not move during concrete pour",
    "Anchor bolts are on-site and ready to install during pour",
    "Site is accessible for inspector vehicle and concrete trucks",
    "Building permit is posted in visible location on site",
    "Approved foundation plans are available on-site for inspector review",
], S))
flow.append(Spacer(1, 6))

flow.append(Paragraph("A9: Foundation Inspection", S["h3"]))
flow.append(d.callout_box(
    "⚠ STOP — Do not pour concrete until inspection is passed.", []))
flow.append(Spacer(1, 6))
flow.append(d.FillInRow([("Inspection Requested:", 0.5), ("Inspector:", 0.5)]))
flow.append(d.FillInRow([("Inspection Date:", 0.4), ("Time:", 0.3),
                         ("Weather:", 0.3)]))
flow.append(d.checkbox_choice_row("INSPECTION RESULT:",
                                  ["PASSED", "FAILED", "CONDITIONAL"], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.3, label="Inspector Comments / Requirements"))
flow.append(Spacer(1, 6))
flow.append(d.items_checklist([
    "All inspector-required corrections completed and re-inspected (if needed)",
], S))
flow.append(d.FillInRow([("Final Approval Date:", 0.5),
                         ("Approved to Pour (initials):", 0.5)]))

# ---------------- SECTION B
flow += d.h2("SECTION B: POUR DAY PREPARATION & EXECUTION", S)

flow += check_table("B1: Concrete Order & Scheduling", [
    "Calculate concrete quantity needed (cubic yards) — add 5% waste",
    ("", [("Quantity ordered (yd³):", 0.5), ("Mix design:", 0.5)]),
    "Specify concrete strength (typically 3000–4000 PSI for foundations)",
    "Request appropriate slump (4–5\" typical, 6–7\" if using pump)",
    "Order fiber reinforcement additive (if specified in plans)",
    ("", [("Ready-mix company:", 0.6), ("Phone:", 0.4)]),
    ("", [("Pour date scheduled:", 0.5), ("Arrival time:", 0.5)]),
    ("", [("Number of trucks:", 0.5), ("Load spacing (min):", 0.5)]),
    ("Confirm pump truck if needed:", [("Company:", 0.6), ("Time:", 0.4)]),
], notes_header="Notes")

flow += check_table("B2: Weather & Site Conditions", [
    "Check 3-day weather forecast (no rain during pour, no freeze for 7 days)",
    ("Pour day forecast:", [("High °F:", 0.34), ("Low °F:", 0.33),
                            ("Precip? Y / N", 0.33)]),
    "Reschedule if temperature will be below 40°F or above 90°F",
    "Have tarps/plastic sheeting ready in case of unexpected rain",
    "Have insulated blankets ready if cold weather (below 50°F)",
    "Verify access road is dry and firm enough for heavy trucks",
], notes_header="Notes")

flow.append(Paragraph("B3: Tools, Materials & Labor", S["h3"]))
flow.append(Paragraph("Items needed on-site before the pour begins:",
                      S["body"]))
flow.append(Paragraph("Tools & Equipment", S["body-bold"]))
flow.append(d.items_checklist([
    "Wheelbarrows (at least 2) and shovels (multiple)",
    "Concrete vibrator (electric or gas-powered)",
    "Bull float and hand floats (magnesium or wood)",
    "Screed board (straight 2x4 or 2x6, longer than pour width)",
    "Hand tamper and concrete rake",
    "4-foot level and tape measure",
    "Edging tools and grooving tools (for control joints)",
    "Rubber boots and gloves for all workers",
], S))
flow.append(Paragraph("Materials", S["body-bold"]))
flow.append(d.items_checklist([
    "Anchor bolts (verify correct size/length, have extras)",
    "Curing compound or plastic sheeting for curing",
    "Water source for cleaning tools and curing concrete",
    "Form release oil (if not already applied)",
    "Foam backer rod for control joints (if applicable)",
], S))
flow.append(Paragraph("Labor", S["body-bold"]))
flow.append(d.items_checklist([
    "Minimum 4–6 workers lined up and confirmed for pour day",
    "Workers briefed on safety (wet concrete is caustic — wear PPE!)",
    "Assign specific roles: screeding, floating, vibrating, tool cleaning",
    "First aid kit on-site with eye wash (concrete in eyes = emergency!)",
], S))
flow.append(Spacer(1, 6))

flow += check_table("B4: During the Pour", [
    ("", [("Pour start time:", 0.5), ("Truck #1 arrival:", 0.5)]),
    "Verify concrete slump before discharge (3–6\" typical)",
    "DO NOT add water to concrete without reducing payment (weakens mix!)",
    "Pour concrete in sections, working systematically (don't overfill areas)",
    "Vibrate concrete thoroughly to eliminate voids (especially near forms)",
    "DO NOT over-vibrate (causes segregation and weak concrete)",
    "Monitor forms for movement, bulging, or failure during pour",
    "Install anchor bolts while concrete is still workable",
    "Verify anchor bolt spacing and alignment (check with string line)",
    "Screed concrete level with top of forms (use straight 2x4)",
    "Bull float surface to smooth and level",
    "Create control joints if pouring slab (every 10–15 feet)",
    "Take concrete test cylinders (if required by inspector/engineer)",
    ("", [("Pour completion time:", 0.5), ("Total duration (hrs):", 0.5)]),
    ("", [("Total concrete used (yd³):", 0.5), ("Waste/short (yd³):", 0.5)]),
], notes_header="Notes")

# ---------------- SECTION C
flow += d.h2("SECTION C: POST-POUR FINISHING & CURING", S)

flow += check_table("C1: Finishing (if slab/exposed surface)", [
    "Wait for bleed water to evaporate (do not finish while water is present!)",
    "Hand float surface to desired texture",
    "Edge all perimeter areas with edging tool",
    "Groove control joints to 1/4 depth of slab",
    "Broom finish surface if non-slip texture desired",
    "Do final troweling when concrete is firm enough to support weight",
], notes_header="Notes")

flow += check_table("C2: Curing", [
    "Apply curing compound OR cover with plastic sheeting (within 12 hours)",
    "Keep concrete moist for minimum 7 days (14 days in cold weather)",
    "Protect from freezing temperatures (cover with insulated blankets)",
    "Protect from excessive heat and sun (mist with water if needed)",
    "Protect from rain damage in first 24 hours (cover with tarps)",
], notes_header="Notes")

flow += check_table("C3: Form Removal & Waterproofing", [
    "Wait minimum 3 days before removing forms (7 days in cold weather)",
    "Remove forms carefully to avoid chipping or damaging concrete",
    "Remove snap ties and patch holes with mortar/hydraulic cement",
    "Inspect foundation walls for honeycomb, voids, or defects",
    "Repair any defects before waterproofing (surface must be sound)",
    "Apply dampproofing/waterproofing per plan (tar, membrane, etc.)",
    "Install drainage board or protection board over waterproofing",
    "Verify perimeter drain tile is in place and functional",
], notes_header="Notes")

flow += check_table("C4: Backfill & Compaction", [
    "Wait minimum 7 days after pour before backfilling (14 days preferred)",
    "Ensure waterproofing is fully cured before backfill",
    "Remove large rocks and debris from backfill material",
    "Backfill in 12\" lifts, compacting each layer (plate compactor)",
    "Keep heavy equipment away from walls (compact by hand near walls)",
    "Grade soil away from foundation (2% min slope, 6\" drop in 10 feet)",
    "Protect foundation from erosion until final grading/landscaping",
], notes_header="Notes")

flow.append(Paragraph("C5: Final Inspection & Approval", S["h3"]))
flow.append(d.FillInRow([("Final Inspection Requested:", 0.5),
                         ("Inspector:", 0.5)]))
flow.append(d.FillInRow([("Inspection Date:", 0.5), ("Time:", 0.5)]))
flow.append(d.items_checklist([
    "Foundation is fully cured (minimum 7 days since pour)",
    "Forms removed and all repairs completed",
    "Waterproofing applied and drainage installed",
    "Backfill completed and properly compacted",
    "Final grading slopes away from foundation",
], S))
flow.append(Spacer(1, 4))
flow.append(d.checkbox_choice_row("FINAL INSPECTION RESULT:",
                                  ["PASSED", "FAILED", "CONDITIONAL"], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.1, label="Inspector Comments"))
flow.append(Spacer(1, 6))
flow.append(d.FillInRow([("Approved to Proceed with Framing (initials):", 0.6),
                         ("Date:", 0.4)]))

# ---------------- sign-off
flow += d.h2("FOUNDATION COMPLETION SIGN-OFF", S)
flow.append(Paragraph(
    "I certify that the foundation has been constructed according to approved "
    "plans and all inspections have passed. The foundation is ready for the "
    "next phase of construction.", S["body"]))
flow.append(Spacer(1, 8))
flow += d.signature_block([
    ("Owner-Builder Signature", True),
    ("Foundation Contractor (if applicable)", True),
])

# ---------------- photo documentation
flow += d.h2("PHOTO DOCUMENTATION — FOUNDATION", S)
flow.append(Paragraph(
    "Document all critical stages with photos. These are essential for "
    "warranty claims, inspection appeals, and future reference.", S["body"]))

photo_rows = [
    "Excavation complete and depth verified",
    "Rebar installed before inspection",
    "Plumbing under-slab installed",
    "Vapor barrier and gravel base",
    "Forms ready for inspection",
    "During pour — concrete placement",
    "Anchor bolts installed",
    "Finished surface after pour",
    "Forms removed — walls complete",
    "Waterproofing applied",
    "Drainage system installed",
    "Backfill completed",
]
photo_data = [[Paragraph("Date", S["cell-bold"]),
               Paragraph("Photo Description", S["cell-bold"]),
               Paragraph("File Name / Number", S["cell-bold"]),
               Paragraph("Notes", S["cell-bold"])]]
for desc in photo_rows:
    photo_data.append(["", Paragraph(desc, S["cell"]), "", ""])
flow.append(d.std_table(
    photo_data,
    [1.0 * inch, 2.6 * inch, 1.7 * inch, CW - 1.0 * inch - 2.6 * inch - 1.7 * inch],
    header_rows=1, write_rows=True))

flow.append(Spacer(1, 10))
flow.append(d.WriteBox(2.6, label="NOTES, ISSUES & LESSONS LEARNED"))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-1-project-planning",
                       "1.5-foundation-checklist.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
