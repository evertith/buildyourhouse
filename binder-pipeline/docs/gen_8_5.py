#!/usr/bin/env python3
"""8.5 Common Measurements & Conversions — lumber sizes, conversions, standards."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 8: Quick Reference Guides"
FORM_ID = "8.5"
# doc_header renders through Paragraph markup, so the ampersand needs escaping.
FORM_TITLE_XML = "Common Measurements &amp; Conversions"
# The footer draws "<id> <title>" flush left against a centred copyright line;
# anything past ~146pt at 8pt collides with it. Keep the footer form short.
FORM_TITLE = "Common Measurements"

LUMBER = [
    ("1x2", '3/4" × 1-1/2"', "Trim, furring strips"),
    ("1x3", '3/4" × 2-1/2"', "Trim, lattice"),
    ("1x4", '3/4" × 3-1/2"', "Trim, boards"),
    ("1x6", '3/4" × 5-1/2"', "Trim, fascia, boards"),
    ("1x8", '3/4" × 7-1/4"', "Trim, shelving"),
    ("1x10", '3/4" × 9-1/4"', "Shelving, trim"),
    ("1x12", '3/4" × 11-1/4"', "Shelving, stair treads"),
    ("2x2", '1-1/2" × 1-1/2"', "Furring, light framing"),
    ("2x3", '1-1/2" × 2-1/2"', "Light framing, blocking"),
    ("2x4", '1-1/2" × 3-1/2"', "Wall framing, blocking"),
    ("2x6", '1-1/2" × 5-1/2"', "Floor joists, rafters, headers"),
    ("2x8", '1-1/2" × 7-1/4"', "Floor joists, rafters, headers"),
    ("2x10", '1-1/2" × 9-1/4"', "Floor joists, beams, headers"),
    ("2x12", '1-1/2" × 11-1/4"', "Floor joists, beams, headers"),
    ("4x4", '3-1/2" × 3-1/2"', "Posts, columns"),
    ("4x6", '3-1/2" × 5-1/2"', "Beams, posts"),
    ("6x6", '5-1/2" × 5-1/2"', "Large posts, beams"),
]

LINEAR = [
    ("Inches", "Feet", "÷ 12", '36" = 3 feet'),
    ("Feet", "Inches", "× 12", '5 feet = 60"'),
    ("Feet", "Yards", "÷ 3", "9 feet = 3 yards"),
    ("Yards", "Feet", "× 3", "2 yards = 6 feet"),
    ("Inches", "Centimeters", "× 2.54", '12" = 30.48 cm'),
    ("Feet", "Meters", "× 0.3048", "10 feet = 3.048 m"),
]

AREA = [
    ("1 square foot", "144 square inches", "Area calculations"),
    ("1 square yard", "9 square feet", "Carpet, concrete"),
    ("1 square (roofing)", "100 square feet", "Roofing materials"),
    ("1 cubic foot", "1,728 cubic inches", "Volume calculations"),
    ("1 cubic yard", "27 cubic feet", "Concrete, soil, gravel"),
    ("1 cubic yard concrete", 'Covers 81 sq ft at 4" thick',
     "Slab calculations"),
    ("1 gallon", "128 fluid ounces", "Paint, liquids"),
    ("1 gallon", "0.1337 cubic feet", "Liquid volume"),
]

BUILDING = [
    ("Stud spacing", '16" or 24" O.C.', "On center measurement"),
    ("Standard ceiling height", "8 feet", "Residential rooms"),
    ("Door height (interior)", '6\'-8" (80")', "Standard pre-hung"),
    ("Door height (exterior)", '6\'-8" to 8\'-0"', "Varies by style"),
    ("Door width (interior)", '24", 28", 30", 32", 36"', "Common sizes"),
    ("Door width (exterior)", '32", 36"', "Most common"),
    ("Window rough opening", '+2" width, +2-1/2" height',
     "Add to window size"),
    ("Door rough opening", '+2" width, +2-1/2" height', "Add to door size"),
    ("Countertop height", '36"', "Kitchen/bathroom standard"),
    ("Countertop depth", '24" to 25"', "Standard base cabinet"),
    ("Upper cabinet height", '12", 15", 18", 30", 42"', "Common sizes"),
    ("Stair riser (max)", '7-3/4"', "Residential code"),
    ("Stair tread (min)", '10"', "Residential code"),
]


def ref_table(title, headers, rows, widths, keep=True):
    header = [Paragraph(h, S["cell-bold"]) for h in headers]
    body = [[Paragraph(c, S["cell"]) for c in r] for r in rows]
    t = d.titled_table(title, header, body, widths, S, write_rows=False)
    return KeepTogether(t) if keep else t


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE_XML, S,
    purpose="Nominal-versus-actual lumber, unit conversions and the standard "
            "dimensions you measure against every day.")

flow.append(Paragraph(
    "Quick reference for common construction measurements, lumber dimensions, "
    "and unit conversions. Keep this handy for quick calculations on the job "
    "site.", S["body"]))
flow.append(Spacer(1, 6))

# The lumber table is 17 rows — let it split rather than shove it whole to a
# fresh page; titled_table repeats its title and header on the continuation.
flow.append(ref_table(
    "Actual Lumber Dimensions (Nominal vs. Actual)",
    ["Nominal Size", "Actual Size", "Common Uses"], LUMBER,
    [1.40 * inch, 1.70 * inch, CW - 3.10 * inch], keep=False))
flow.append(Spacer(1, 12))

flow.append(ref_table(
    "Linear Measurements &amp; Conversions",
    ["From", "To", "Multiply By", "Example"], LINEAR,
    [1.20 * inch, 1.40 * inch, 1.40 * inch, CW - 4.00 * inch]))
flow.append(Spacer(1, 12))

flow.append(ref_table(
    "Area &amp; Volume Conversions",
    ["Measurement", "Conversion", "Common Use"], AREA,
    [1.80 * inch, 2.40 * inch, CW - 4.20 * inch]))
flow.append(Spacer(1, 12))

flow.append(ref_table(
    "Standard Building Dimensions",
    ["Item", "Standard Dimension", "Notes"], BUILDING,
    [1.80 * inch, 2.10 * inch, CW - 3.90 * inch], keep=False))

flow.append(Spacer(1, 12))
flow.append(d.callout_box(
    "Quick Tips",
    [Paragraph(t, S["bullet"], bulletText="•") for t in [
        "When measuring, always double-check and measure twice before cutting",
        '"O.C." means "on center" — measured from center of one member to '
        "center of the next",
        "Rough openings are larger than actual door/window sizes to allow for "
        "shimming and adjustment",
        "Always verify local code requirements as they may differ from these "
        "standards",
    ]]))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-8-quick-reference",
                       "8.5-common-measurements.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
