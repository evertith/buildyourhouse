#!/usr/bin/env python3
"""1.2 Budget Tracking Spreadsheet — rebuilt on the 2026 design system.

Money columns are empty write-in cells; the dollar sign lives in the column
header, never repeated inside every cell.

Portrait: 157 write-in rows at the 29pt handwriting minimum need every inch of
frame height a page can give, and a portrait frame is 37% taller than landscape.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import Flowable, Paragraph, Spacer, TableStyle

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 1: Project Planning & Foundation"
FORM_ID = "1.2"
FORM_TITLE = "Budget Tracking Spreadsheet"

COLS = [2.35 * inch, 1.00 * inch, 1.00 * inch, 1.00 * inch, 1.65 * inch]
HEADER = [Paragraph(t, S["cell-bold"]) for t in
          ("Item Description", "Estimated Cost ($)", "Actual Cost ($)",
           "Variance ($)", "Notes / Vendor")]


def heights_for(rows, widths, minimum=d.WRITE_ROW_PT, pad=10):
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


def budget_table(title, items, subtotal_label):
    rows = []
    for it in items:
        first = it if isinstance(it, Flowable) else Paragraph(it, S["cell"])
        rows.append([first, "", "", "", ""])
    rows.append([Paragraph(subtotal_label, S["cell-bold"]), "", "", "", ""])
    t = d.titled_table(title, HEADER, rows, COLS, S,
                       row_heights=heights_for(rows, COLS))
    sub = len(rows) + 1  # title row + header row + body index of the subtotal
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, sub), (-1, sub), d.SUBTOTAL_FILL),
        ("FONTNAME", (0, sub), (-1, sub), d.BOLD),
        ("LINEABOVE", (0, sub), (-1, sub), 1, d.INK),
    ]))
    return [t, Spacer(1, 12)]


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Every construction cost, by category — estimated against actual, "
            "with per-category subtotals and a whole-project roll-up.")

flow.append(d.FillInRow([("Project Name:", 0.6), ("Total Budget ($):", 0.4)]))
flow.append(d.FillInRow([("Owner-Builder:", 0.6), ("Date Created:", 0.4)]))
flow.append(d.FillInRow([("Lender/Financing:", 0.6), ("Last Updated:", 0.4)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>INSTRUCTIONS:</b> Track all construction costs by category. Update "
    "regularly. Calculate variance (Actual − Estimated). Negative variance = "
    "under budget, positive variance = over budget. Monitor percentage of "
    "budget used to avoid overruns. Enter figures in dollars — the column "
    "headings carry the units.", S["body"]))
flow.append(Spacer(1, 10))

flow += budget_table("LAND &amp; SITE COSTS", [
    "Land purchase/lot cost",
    "Closing costs and fees",
    "Land survey",
    "Soil/percolation testing",
], "LAND &amp; SITE SUBTOTAL")

flow += budget_table("SITE PREPARATION", [
    "Site clearing and tree removal",
    "Grading and excavation",
    "Driveway/access road",
    "Erosion control measures",
    "Temporary utilities (power, water)",
    "Portable toilet rental (duration)",
    "Dumpster rental (duration)",
    "Storage container/job box",
], "SITE PREPARATION SUBTOTAL")

flow += budget_table("FOUNDATION", [
    "Foundation excavation",
    "Gravel/stone base",
    "Rebar and wire mesh",
    "Concrete (footers)",
    "Concrete (foundation walls/slab)",
    "Concrete pump rental",
    "Form lumber and supplies",
    "Anchor bolts and hardware",
    "Waterproofing/dampproofing",
    "Drainage tile and pipe",
    "Vapor barrier/poly sheeting",
    "Backfill and compaction",
    "Foundation labor (if subbed)",
], "FOUNDATION SUBTOTAL")

flow += budget_table("FRAMING", [
    "Framing lumber (studs, plates, joists)",
    "Engineered lumber (LVL, I-joists, etc.)",
    "Roof trusses or rafters",
    "Sheathing (wall, floor, roof)",
    "House wrap/moisture barrier",
    "Nails, screws, hangers, hardware",
    "Framing labor (if subbed)",
    "Crane rental (truss setting)",
], "FRAMING SUBTOTAL")

flow += budget_table("ROOFING", [
    "Roofing underlayment (felt/synthetic)",
    "Shingles/roofing material",
    "Ridge vent and accessories",
    "Drip edge and flashing",
    "Gutters and downspouts",
    "Roofing labor (if subbed)",
], "ROOFING SUBTOTAL")

flow += budget_table("EXTERIOR FINISHES", [
    "Siding material",
    "Exterior trim boards",
    "Soffit and fascia",
    "Exterior paint/stain",
    "Exterior doors (front, rear, garage)",
    "Windows",
    "Exterior labor (if subbed)",
], "EXTERIOR FINISHES SUBTOTAL")

flow += budget_table("PLUMBING ROUGH-IN", [
    "Supply pipes (PEX, copper, etc.)",
    "Drain/waste/vent (DWV) pipes",
    "Fittings, connectors, valves",
    "Water heater",
    "Plumbing rough-in labor (if subbed)",
], "PLUMBING ROUGH-IN SUBTOTAL")

flow += budget_table("HVAC ROUGH-IN", [
    "HVAC unit(s) — furnace/AC/heat pump",
    "Ductwork and registers",
    "Ventilation fans (bath, kitchen)",
    "HVAC labor/installation (if subbed)",
], "HVAC ROUGH-IN SUBTOTAL")

flow += budget_table("ELECTRICAL ROUGH-IN", [
    "Electrical panel/breaker box",
    "Wire and cable (Romex, etc.)",
    "Boxes, connectors, staples",
    "Service entrance/meter base",
    "Electrical rough-in labor (if subbed)",
], "ELECTRICAL ROUGH-IN SUBTOTAL")

flow += budget_table("INSULATION", [
    "Wall insulation (fiberglass/spray foam)",
    "Ceiling/attic insulation",
    "Floor/rim joist insulation",
    "Insulation labor (if subbed)",
], "INSULATION SUBTOTAL")

flow += budget_table("DRYWALL", [
    "Drywall sheets (1/2\", 5/8\")",
    "Joint compound (mud)",
    "Tape, corner bead, screws",
    "Texture materials (if applicable)",
    "Drywall labor (hanging, taping, finishing)",
], "DRYWALL SUBTOTAL")

flow += budget_table("DOORS &amp; INTERIOR TRIM", [
    "Interior doors (slab and pre-hung)",
    "Door hardware (knobs, hinges, locks)",
    "Baseboards",
    "Window and door casing",
    "Crown molding (if applicable)",
    "Closet shelving and rods",
    "Trim labor (if subbed)",
], "DOORS &amp; TRIM SUBTOTAL")

flow += budget_table("FLOORING", [
    "LVP/vinyl plank flooring",
    "Tile (bathroom, kitchen, entry)",
    "Hardwood flooring",
    "Carpet (bedrooms, stairs)",
    "Underlayment and adhesives",
    "Flooring labor (if subbed)",
], "FLOORING SUBTOTAL")

flow += budget_table("CABINETS &amp; COUNTERTOPS", [
    "Kitchen cabinets (base and upper)",
    "Bathroom vanities",
    "Kitchen countertops",
    "Bathroom countertops",
    "Cabinet hardware (pulls, hinges)",
    "Cabinet installation labor (if subbed)",
], "CABINETS &amp; COUNTERTOPS SUBTOTAL")

flow += budget_table("PLUMBING FIXTURES", [
    "Kitchen sink and faucet",
    "Bathroom sinks and faucets",
    "Toilets",
    "Bathtubs",
    "Shower enclosures and doors",
    "Shower/tub fixtures and valves",
    "Plumbing fixture installation labor",
], "PLUMBING FIXTURES SUBTOTAL")

flow += budget_table("ELECTRICAL FIXTURES &amp; FINISH", [
    "Light fixtures (interior and exterior)",
    "Ceiling fans",
    "Receptacles and switches",
    "Cover plates",
    "Doorbell/smoke detectors/CO detectors",
    "Electrical trim-out labor (if subbed)",
], "ELECTRICAL FIXTURES SUBTOTAL")

flow += budget_table("PAINTING", [
    "Interior primer",
    "Interior paint",
    "Exterior primer and paint",
    "Painting supplies (brushes, rollers, tape)",
    "Painting labor (if subbed)",
], "PAINTING SUBTOTAL")

flow += budget_table("FINISH ITEMS &amp; APPLIANCES", [
    "Kitchen appliances (range, refrigerator, DW)",
    "Microwave/range hood",
    "Laundry appliances (washer/dryer)",
    "Mirrors and shower doors",
    "Tile backsplash materials and labor",
    "Garage door and opener",
    "Deck/patio materials and labor",
], "FINISH ITEMS SUBTOTAL")

flow += budget_table("LANDSCAPING &amp; FINAL SITE WORK", [
    "Final grading and drainage",
    "Topsoil and seeding/sod",
    "Trees, shrubs, and plantings",
    "Mulch and landscape fabric",
    "Driveway paving/concrete",
    "Walkways and steps",
    "Mailbox and house numbers",
], "LANDSCAPING SUBTOTAL")

flow += budget_table("PERMITS, FEES &amp; INSURANCE", [
    "Building permit",
    "Electrical permit",
    "Plumbing permit",
    "Mechanical/HVAC permit",
    "Septic/well permits",
    "Impact/tap fees (water, sewer)",
    "Builder's risk insurance",
    "General liability insurance",
    "Plan review/engineering fees",
], "PERMITS &amp; INSURANCE SUBTOTAL")

flow += budget_table("CONTINGENCY &amp; MISCELLANEOUS", [
    "Contingency fund (10–15% recommended)",
    "Tool purchases/rentals",
    "Miscellaneous supplies",
    "Cleanup and waste removal",
    "Inspection fees (beyond permit costs)",
    d.FillIn("Other:", font_size=9.5, height=24),
    d.FillIn("Other:", font_size=9.5, height=24),
], "CONTINGENCY SUBTOTAL")

# ---------------- budget summary
sum_cols = [2.35 * inch, 1.55 * inch, 1.55 * inch, 1.55 * inch]
sum_header = [Paragraph(t, S["cell-bold"]) for t in
              ("Category", "Estimated Total ($)", "Actual Total ($)",
               "% of Budget")]
sum_rows = [
    [Paragraph("GRAND TOTAL — ALL CATEGORIES", S["cell-bold"]), "", "", ""],
    [Paragraph("Total Variance (Actual − Estimated)", S["cell"]), "", "", ""],
    [Paragraph("Remaining Budget Available", S["cell"]), "", "", ""],
]
sum_t = d.titled_table("BUDGET SUMMARY", sum_header, sum_rows, sum_cols, S,
                       row_heights=heights_for(sum_rows, sum_cols, minimum=34))
sum_t.setStyle(TableStyle([
    ("BACKGROUND", (0, 2), (-1, 2), d.SUBTOTAL_FILL),
    ("FONTNAME", (0, 2), (-1, 2), d.BOLD),
    ("SPAN", (1, 3), (-1, 3)),
    ("SPAN", (1, 4), (-1, 4)),
]))
flow.append(sum_t)

flow.append(Spacer(1, 8))
flow.append(d.WriteBox(2.3, label="BUDGET STATUS NOTES"))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-1-project-planning",
                       "1.2-budget-tracking-spreadsheet.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
