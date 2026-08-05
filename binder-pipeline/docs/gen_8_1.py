#!/usr/bin/env python3
"""8.1 Residential Code Quick Reference — IRC minimums the owner-builder hits daily."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, Spacer, Table, TableStyle

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 8: Quick Reference Guides"
FORM_ID = "8.1"
FORM_TITLE_XML = "Residential Code Quick Reference"
# The footer draws "<id> <title>" flush left against a centred copyright line;
# anything past ~146pt at 8pt collides with it. Keep the footer form short.
FORM_TITLE = "Residential Code Reference"

# Reference tables: (title, header cells, rows)
STAIRS = [
    ("Maximum Riser Height", "7.75 inches", "Height from one tread to next"),
    ("Minimum Tread Depth", "10 inches", "Measured horizontally"),
    ("Maximum Riser Variance", "3/8 inch", "Between tallest/shortest risers"),
    ("Maximum Tread Variance", "3/8 inch", "Between deepest/shallowest"),
    ("Minimum Stair Width", "36 inches", "Clear width, not including handrails"),
    ("Minimum Headroom", "6 feet 8 inches", "Measured vertically above nosing"),
    ("Handrail Height", "34-38 inches", "Measured from nosing"),
    ("Handrail Required", "When 4+ risers", "At least one side required"),
    ("Handrail Graspability", "1.25-2 inches", "Perimeter or grip size"),
    ("Handrail Clearance", "1.5 inches minimum", "From wall to handrail"),
]

GUARDRAILS = [
    ("Required When", "Drop exceeds 30 inches",
     "Porches, decks, landings, balconies"),
    ("Minimum Height", "36 inches residential",
     "Measured from deck/floor surface"),
    ("Sphere Test", "4 inch maximum opening",
     'No gaps allowing 4" sphere to pass'),
    ("Triangle Test", "6 inch max opening",
     "For stair guardrail triangular openings"),
    ("Load Requirements", "200 lbs concentrated",
     "At top rail in any direction"),
    ("Intermediate Rails", 'Spaced to prevent 4" sphere',
     "Balusters, pickets, or mesh"),
]

ELECTRICAL = [
    ("Wall Outlets - Spacing", "Maximum 12 feet apart",
     "No point more than 6 feet from outlet"),
    ("Wall Outlets - Doors", "Maximum 6 feet from door", "Measured along wall"),
    ("Kitchen Counter Outlets", "Maximum 4 feet apart",
     "Must be above counter height"),
    ("Kitchen Islands", "One outlet required", 'Island 24" x 12" or larger'),
    ("Bathroom Outlets", "One within 3 feet of sink", "Must be GFCI protected"),
    ("Garage Outlets", "At least one", "GFCI protected"),
    ("Exterior Outlets", "Front and back required",
     "GFCI protected, weather-resistant"),
    ("Basement Outlets", "At least one", "GFCI if unfinished"),
    ("Hallways", "One if 10+ feet long", "Measured along centerline"),
]

GFCI = [
    "All bathroom outlets",
    "Kitchen countertop outlets",
    "All exterior outlets",
    "All garage outlets",
    "Unfinished basement outlets",
    "Crawl space outlets",
    "Laundry room outlets (within 6 feet of sink)",
    "Wet bar sink outlets",
]

SMOKE = [
    ("Each Sleeping Room", "One smoke detector", "Inside each bedroom"),
    ("Outside Sleeping Areas", "One per sleeping area",
     "In hallway near bedrooms"),
    ("Each Story", "At least one", "Including basement, not crawl space"),
    ("Interconnection", "All must be interconnected",
     "When one sounds, all sound"),
    ("Power Source", "Hardwired with battery backup",
     "Or 10-year sealed battery"),
    ("CO Detectors", "Outside sleeping areas",
     "Required if fuel-burning appliances"),
    ("CO Detector - Each Level", "One per floor minimum", "Including basement"),
]

EGRESS = [
    ("Required Location", "Each sleeping room",
     "Basements with bedrooms also need egress"),
    ("Minimum Net Clear Opening", "5.7 square feet", "Actual openable area"),
    ("Minimum Opening Width", "20 inches", "Clear opening when open"),
    ("Minimum Opening Height", "24 inches", "Clear opening when open"),
    ("Maximum Sill Height", "44 inches", "From floor to bottom of opening"),
    ("Window Wells (if req.)", "9 sq ft minimum",
     "If window well depth &gt;44 inches"),
    ("Window Well Width", "36 inches minimum", "Horizontal projection"),
    ("Window Well Ladder", 'Required if &gt;44" deep',
     "Permanent ladder or steps"),
    ("Ladder Requirements", 'Max 18" projection',
     'Rungs 3" wide, 12" spacing max'),
]

CEILINGS = [
    ("Habitable Rooms", "7 feet", "Living rooms, bedrooms, kitchens"),
    ("Bathrooms", "6 feet 8 inches", "At fixtures and circulation paths"),
    ("Hallways", "6 feet 8 inches", "Minimum clear height"),
    ("Kitchens", "6 feet 8 inches", "At work areas"),
    ("Basements (unfinished)", "6 feet 8 inches",
     "Beams may project to 6 feet 4 inches"),
    ("Sloped Ceilings", "50% of room area at min height",
     "No portion below 5 feet"),
    ("Furred Ceilings", "Maintain minimum heights",
     "Account for lowered ceiling"),
]

ADDITIONAL = [
    ("Tempered Glass",
     'Required within 24" of door, bottom edge &lt;60" above floor'),
    ("Bathroom Ventilation",
     "Window 3 sq ft (1.5 sq ft openable) OR mechanical fan"),
    ("Mechanical Fan",
     "Min 50 CFM intermittent or 20 CFM continuous (bathroom)"),
    ("Stair Lighting",
     "Required at top and bottom, 3-way switches if 6+ risers"),
    ("Insulation",
     "Meet energy code for climate zone (R-values vary by location)"),
    ("Attic Access", 'Minimum 22" x 30" opening, accessible location'),
    ("Crawl Space Access", 'Minimum 18" x 24" opening'),
]


def ref_table(title, headers, rows, widths):
    """Every table here fits inside one page, so keep it whole: splitting a
    lookup table costs the reader a page turn mid-scan."""
    header = [Paragraph(h, S["cell-bold"]) for h in headers]
    body = [[Paragraph(c, S["cell"]) for c in r] for r in rows]
    return KeepTogether(
        d.titled_table(title, header, body, widths, S, write_rows=False))


def two_col_list(items):
    """Reference list set two-up inside a callout — no checkboxes, because
    these are conditions of the code, not tasks to tick off."""
    inner = CW - 48
    half = (len(items) + 1) // 2
    left, right = items[:half], items[half:]
    rows = []
    for i in range(half):
        r = [Paragraph(f"• {left[i]}", S["cell"]), ""]
        r[1] = Paragraph(f"• {right[i]}", S["cell"]) if i < len(right) else ""
        rows.append(r)
    t = Table(rows, colWidths=[inner / 2, inner / 2])
    t.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


W3 = [2.20 * inch, 1.80 * inch, CW - 4.00 * inch]
W3B = [2.00 * inch, 2.20 * inch, CW - 4.20 * inch]

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE_XML, S,
    purpose="The residential building code requirements you will reach for "
            "most often, in one place.")

# The disclaimer leads the document — nobody should read a number here without
# it.
flow.append(d.callout_box(
    "⚠ VERIFY WITH YOUR LOCAL JURISDICTION",
    [Paragraph(
        "This quick reference is based on the International Residential Code "
        "(IRC). Always verify requirements with your local building department "
        "as requirements may vary and local amendments may be more restrictive "
        "than the IRC. When in doubt, consult with your building inspector "
        "before proceeding.", S["body"])]))
flow.append(Spacer(1, 6))

# ---------------- stairs & guards
flow += d.h2("STAIRS, HANDRAILS & GUARDRAILS", S)
flow.append(ref_table("Stairs and Handrails",
                      ["Requirement", "Minimum/Maximum", "Notes"],
                      STAIRS, W3))
flow.append(Spacer(1, 10))
flow.append(ref_table("Guardrails",
                      ["Requirement", "Minimum/Maximum", "Notes"],
                      GUARDRAILS, W3))

# ---------------- electrical
flow += d.h2("ELECTRICAL OUTLETS AND CIRCUITS", S)
flow.append(ref_table("Outlet Placement",
                      ["Location", "Requirement", "Additional Notes"],
                      ELECTRICAL, W3B))
flow.append(Spacer(1, 10))
flow.append(d.callout_box("GFCI PROTECTION REQUIRED", [two_col_list(GFCI)]))

# ---------------- alarms
flow += d.h2("SMOKE AND CO DETECTORS", S)
flow.append(ref_table("Detector Placement and Power",
                      ["Location", "Requirement", "Notes"], SMOKE, W3B))

# ---------------- egress, ceilings, misc
flow += d.h2("EGRESS, CEILING HEIGHTS & OTHER REQUIREMENTS", S)
flow.append(ref_table(
    "Emergency Escape and Rescue Openings (Egress Windows)",
    ["Requirement", "Minimum/Maximum", "Notes"], EGRESS, W3))
flow.append(Spacer(1, 10))
flow.append(ref_table("Ceiling Heights",
                      ["Room Type", "Minimum Height", "Notes"],
                      CEILINGS, [2.00 * inch, 1.80 * inch, CW - 3.80 * inch]))
flow.append(Spacer(1, 10))
flow.append(ref_table("Additional Common Requirements",
                      ["Item", "Requirement"], ADDITIONAL,
                      [2.20 * inch, CW - 2.20 * inch]))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-8-quick-reference",
                       "8.1-residential-code-quick-reference.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
