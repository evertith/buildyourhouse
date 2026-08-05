#!/usr/bin/env python3
"""8.3 Material Calculators — take-off formulas, worked examples, coverage tables."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, Spacer, Table, TableStyle

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 8: Quick Reference Guides"
FORM_ID = "8.3"
FORM_TITLE = "Material Calculators"

FORMULA_STYLE = ParagraphStyle(
    "formula", fontName=d.BOLD, fontSize=12, leading=16, textColor=d.INK)


def formula(text):
    """The calculator's headline equation, set on a light band so it reads as
    the answer you came to the page for."""
    t = Table([[Paragraph(text, FORMULA_STYLE)]], colWidths=[CW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), d.SUBTOTAL_FILL),
        ("BOX", (0, 0), (-1, -1), 1, d.INK),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, -1), 9),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    return t


def ref_table(title, headers, rows, widths):
    header = [Paragraph(h, S["cell-bold"]) for h in headers]
    body = [[Paragraph(c, S["cell"]) for c in r] for r in rows]
    return KeepTogether(
        d.titled_table(title, header, body, widths, S, write_rows=False))


def tips(title, items):
    """Held together — a tips list orphaning its last bullet onto a fresh page
    reads as an error."""
    return [KeepTogether(
        [Paragraph(title, S["body-bold"])] +
        [Paragraph(t, S["bullet"], bulletText="•") for t in items])]


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Take-off formulas and coverage tables for the materials you order "
            "by the truckload.")

flow.append(d.callout_box(
    "How to use these calculators",
    [Paragraph(
        "Use these formulas and calculators to estimate material quantities "
        "for your project. Always add 5-15% extra for waste, cuts, and "
        "mistakes. Order materials in standard sizes and quantities to "
        "minimize cost.", S["body"])]))
flow.append(Spacer(1, 4))

# ---------------- concrete
flow += d.h2("CONCRETE CALCULATOR", S)
flow.append(formula("Cubic Yards = (Length × Width × Thickness in inches) ÷ 324"))
flow.append(Spacer(1, 8))
flow.append(Paragraph(
    "<b>Example:</b> For a 20' × 30' slab that is 4\" thick:<br/>"
    "(20 × 30 × 4) ÷ 324 = 2,400 ÷ 324 = 7.4 cubic yards<br/>"
    "Order 8 cubic yards (rounded up for waste)", S["body"]))
flow.append(Spacer(1, 6))
flow.append(ref_table(
    "Concrete Coverage by Slab Thickness",
    ["Slab Thickness", "Square Feet per Cubic Yard"],
    [("4 inches", "81 sq ft"), ("5 inches", "65 sq ft"),
     ("6 inches", "54 sq ft"), ("8 inches", "40 sq ft")],
    [2.20 * inch, CW - 2.20 * inch]))

# ---------------- drywall
flow += d.h2("DRYWALL CALCULATOR", S)
flow.append(formula("Sheets Needed = Total Area ÷ 32 (for 4' × 8' sheets)"))
flow.append(Spacer(1, 8))
flow.append(Paragraph(
    "<b>Example:</b> For a room with 800 sq ft of wall and ceiling area:<br/>"
    "800 ÷ 32 = 25 sheets<br/>"
    "Order 28 sheets (add 10% for waste and cuts)", S["body"]))
flow.append(Spacer(1, 4))
flow += tips("Drywall Tips:", [
    "Use 4' × 8' sheets for walls, 4' × 12' for ceilings if possible",
    "1 gallon joint compound per 100 sq ft of drywall",
    "1 roll of tape per 100 linear feet of seams",
    "1 pound of screws per 8 sheets (1,000 screws approx)",
])

# ---------------- paint
flow += d.h2("PAINT CALCULATOR", S)
flow.append(formula("Gallons Needed = Total Area ÷ 350 (per coat)"))
flow.append(Spacer(1, 8))
flow.append(Paragraph(
    "<b>Example:</b> For 1,200 sq ft of wall area with 2 coats:<br/>"
    "1,200 ÷ 350 = 3.4 gallons per coat<br/>"
    "3.4 × 2 coats = 6.8 gallons total<br/>"
    "Order 7 gallons (round up)", S["body"]))
flow.append(Spacer(1, 6))
flow.append(ref_table(
    "Paint Coverage by Surface",
    ["Surface Type", "Coverage per Gallon"],
    [("Smooth drywall/plaster", "400 sq ft"),
     ("Textured drywall", "350 sq ft"),
     ("Rough wood/concrete", "300 sq ft"),
     ("Primer on new drywall", "300 sq ft")],
    [2.60 * inch, CW - 2.60 * inch]))

# ---------------- flooring
flow += d.h2("FLOORING CALCULATOR", S)
flow.append(formula(
    "Square Feet Needed = (Length × Width) × 1.10 (waste factor)"))
flow.append(Spacer(1, 8))
flow.append(Paragraph(
    "<b>Example:</b> For a 12' × 15' room:<br/>"
    "12 × 15 = 180 sq ft<br/>"
    "180 × 1.10 = 198 sq ft<br/>"
    "Order 200 sq ft (round up to nearest package size)", S["body"]))
flow.append(Spacer(1, 6))
flow.append(ref_table(
    "Flooring Waste Factors",
    ["Flooring Type", "Recommended Waste Factor"],
    [("Carpet, sheet vinyl", "5-10% (1.05 - 1.10)"),
     ("Hardwood, straight pattern", "10-15% (1.10 - 1.15)"),
     ("Tile, diagonal pattern", "15-20% (1.15 - 1.20)"),
     ("Laminate, complex room", "10-15% (1.10 - 1.15)")],
    [2.80 * inch, CW - 2.80 * inch]))

# ---------------- siding
flow += d.h2("SIDING CALCULATOR", S)
flow.append(formula("Square Feet = (Total Wall Area) − (Window/Door Areas)"))
flow.append(Spacer(1, 8))
flow.append(Paragraph(
    "<b>Example:</b> For a wall 40' long × 10' high with two 3' × 5' "
    "windows:<br/>"
    "Wall area: 40 × 10 = 400 sq ft<br/>"
    "Window area: 2 × (3 × 5) = 30 sq ft<br/>"
    "Net siding: 400 − 30 = 370 sq ft<br/>"
    "With 10% waste: 370 × 1.10 = 407 sq ft", S["body"]))
flow.append(Spacer(1, 4))
flow += tips("Siding Material Tips:", [
    "Add 10-15% waste for lap siding",
    "Add 15-20% waste for diagonal or fancy patterns",
    'Vinyl siding sold by "square" (100 sq ft)',
    "Account for starter strips, J-channels, and trim",
])

# ---------------- roofing
flow += d.h2("ROOFING CALCULATOR", S)
flow.append(formula("Squares Needed = (Roof Area in sq ft) ÷ 100"))
flow.append(Spacer(1, 8))
flow.append(Paragraph(
    "<b>Example:</b> For a roof with 2,400 sq ft of area:<br/>"
    "2,400 ÷ 100 = 24 squares<br/>"
    "With 10% waste: 24 × 1.10 = 26.4 squares<br/>"
    "Order 27 squares", S["body"]))
flow.append(Spacer(1, 6))
flow.append(ref_table(
    "Roof Pitch Multipliers",
    ["Roof Pitch", "Multiplier", "Example: 1,000 sq ft floor"],
    [("Flat to 3:12", "1.03", "1,030 sq ft roof"),
     ("4:12", "1.05", "1,050 sq ft roof"),
     ("5:12", "1.08", "1,080 sq ft roof"),
     ("6:12", "1.12", "1,120 sq ft roof"),
     ("8:12", "1.20", "1,200 sq ft roof"),
     ("10:12", "1.30", "1,300 sq ft roof"),
     ("12:12", "1.41", "1,410 sq ft roof")],
    [1.60 * inch, 1.40 * inch, CW - 3.00 * inch]))
flow.append(Spacer(1, 8))
# Corrected: the previous edition inverted the ice & water shield coverage.
flow += tips("Roofing Additional Materials:", [
    "Ridge cap: 1 bundle per 30 linear feet",
    "Starter strip: 1 bundle per 100 linear feet",
    "Ice &amp; water shield: 1 roll covers ~2 squares "
    "(200 sq ft; 36in × 66.7ft roll)",
    "Underlayment: 4 squares per roll (400 sq ft coverage)",
])

# ---------------- framing
flow += d.h2("FRAMING LUMBER ESTIMATOR", S)
flow.append(ref_table(
    "Stud, Joist and Plate Counts",
    ["Application", "Spacing", "Formula"],
    [("Wall studs", '16" O.C.',
      "(Linear feet × 0.75) + extras for corners/openings"),
     ("Wall studs", '24" O.C.',
      "(Linear feet × 0.50) + extras for corners/openings"),
     ("Floor/ceiling joists", '16" O.C.', "(Linear feet × 0.75) + 1"),
     ("Floor/ceiling joists", '24" O.C.', "(Linear feet × 0.50) + 1"),
     ("Plates (top/bottom)", "Per wall",
      "Linear feet × 3 (for top double plate + bottom)")],
    [1.60 * inch, 1.00 * inch, CW - 2.60 * inch]))

flow.append(Spacer(1, 12))
flow.append(d.callout_box(
    "⚠ IMPORTANT",
    [Paragraph(
        "These calculators provide estimates only. Always verify measurements "
        "on-site and consult with suppliers for material recommendations. "
        "Order extra materials for waste, mistakes, and future repairs. Keep "
        "leftover materials labeled and stored properly for warranty and "
        "maintenance purposes.", S["body"])]))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-8-quick-reference",
                       "8.3-material-calculators.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
