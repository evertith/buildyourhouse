#!/usr/bin/env python3
"""3.5 Insulation & Air Sealing Guide — rebuilt on the 2026 design system."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import CondPageBreak, Flowable, Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 3: Rough-In Phase"
FORM_ID = "3.5"
FORM_TITLE = "Insulation & Air Sealing Guide"

SCHEDULE_COLS = [1.55 * inch, 2.05 * inch, 0.95 * inch, 0.95 * inch,
                 CW - 5.50 * inch]
SPEC_COLS = [0.42 * inch, 2.95 * inch, 1.75 * inch, CW - 5.12 * inch]
CHECK_COLS = [0.42 * inch, 3.60 * inch, CW - 4.02 * inch]


class ChoiceCell(Flowable):
    """Mutually-exclusive options as drawn boxes, wrapping to fit a table cell.

    design.checkbox_choice_row is single-line and overflows narrow columns;
    this keeps the same visual language inside a spec column.
    """

    def __init__(self, options, box=9, font_size=8.5, gap=9, lead=13):
        super().__init__()
        self.options = options
        self.box = box
        self.font_size = font_size
        self.gap = gap
        self.lead = lead
        self._rows = [list(options)]

    def _layout(self, avail):
        d.register_fonts()
        rows, cur, x = [], [], 0.0
        for opt in self.options:
            w = self.box + 4 + stringWidth(opt, d.BODY, self.font_size)
            if cur and x + w > avail:
                rows.append(cur)
                cur, x = [], 0.0
            cur.append(opt)
            x += w + self.gap
        if cur:
            rows.append(cur)
        return rows

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self._rows = self._layout(availWidth)
        self.height = len(self._rows) * self.lead
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setStrokeColor(d.INK)
        c.setFillColor(d.INK)
        c.setLineWidth(0.75)
        y = self.height - self.lead + 3
        for row in self._rows:
            x = 0.0
            for opt in row:
                c.rect(x, y, self.box, self.box)
                x += self.box + 4
                c.setFont(d.BODY, self.font_size)
                c.drawString(x, y + 1, opt)
                x += stringWidth(opt, d.BODY, self.font_size) + self.gap
            y -= self.lead


def P(text):
    return Paragraph(text, S["cell"])


def F(label, height=24, font_size=9.5):
    """A labelled drawn write-in rule inside a cell — never underscores."""
    return d.FillIn(label, font_size=font_size, height=height)


def C(*options):
    return ChoiceCell(list(options))


def cell(value):
    return P(value) if isinstance(value, str) else value


def measured_heights(rows, cols, minimum=d.WRITE_ROW_PT, pad=10):
    """Row heights that never clip: max wrapped cell height, floored at the
    handwriting minimum (titled_table auto-sizes any row holding a Paragraph)."""
    heights = []
    for row in rows:
        tallest = 0
        for content, width in zip(row, cols):
            if isinstance(content, str) or content is None:
                continue
            flowables = content if isinstance(content, list) else [content]
            tallest = max(tallest, sum(f.wrap(width - 10, 10000)[1]
                                       for f in flowables))
        heights.append(max(minimum, tallest + pad))
    return heights


def spec_table(title, items):
    """[box] Item | Specification | Notes."""
    header = ["",
              Paragraph("Item", S["cell-bold"]),
              Paragraph("Specification", S["cell-bold"]),
              Paragraph("Notes", S["cell-bold"])]
    rows = [[d.Checkbox(), cell(item), cell(spec), ""] for item, spec in items]
    return [d.titled_table(title, header, rows, SPEC_COLS, S,
                           row_heights=measured_heights(rows, SPEC_COLS)),
            Spacer(1, 8)]


def check_table(title, items):
    """[box] Item | Notes."""
    header = ["",
              Paragraph("Item", S["cell-bold"]),
              Paragraph("Notes", S["cell-bold"])]
    rows = [[d.Checkbox(), cell(item), ""] for item in items]
    return [d.titled_table(title, header, rows, CHECK_COLS, S,
                           row_heights=measured_heights(rows, CHECK_COLS)),
            Spacer(1, 8)]



def section(title, styles=None, min_space=3.4):
    """An h2 that will not strand itself at the foot of a page: it reserves
    room for the heading plus the opening rows of whatever follows."""
    return [CondPageBreak(min_space * inch)] + d.h2(title, S)


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="The insulation schedule with required and installed R-values, "
            "plus the air sealing checklist that decides whether the house "
            "actually performs at those numbers.")

flow.append(d.FillInRow([("Property Address:", 1.0)]))
flow.append(d.FillInRow([("Permit Number:", 0.5), ("Inspection Date:", 0.5)]))
flow.append(d.FillInRow([("Insulation Contractor:", 1.0)]))
flow.append(d.FillInRow([("Phone:", 0.5), ("License #:", 0.5)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>INSTRUCTIONS:</b> Record the R-value you actually installed next to "
    "the R-value code requires — inspectors check both. Do the air sealing "
    "pass <i>before</i> insulation goes in; every penetration on this list "
    "is unreachable once the cavity is filled.", S["body"]))
flow.append(Spacer(1, 4))

# ---------------- INSULATION SCHEDULE
flow += section("INSULATION SCHEDULE", S)
_sched_header = [Paragraph("Location", S["cell-bold"]),
                 Paragraph("Insulation Type", S["cell-bold"]),
                 Paragraph("R-Value Required", S["cell-bold"]),
                 Paragraph("R-Value Installed", S["cell-bold"]),
                 Paragraph("Notes", S["cell-bold"])]
_sched_rows = [[P(location), types, "", "", ""] for location, types in [
    ("Exterior Walls",
     C("Fiberglass", "Spray Foam", "Cellulose", "Mineral Wool")),
    ("Ceiling/Attic", C("Blown-in", "Batt", "Spray Foam", "Rigid Board")),
    ("Cathedral Ceiling",
     [C("Spray Foam", "Batt + Rigid", "Other"),
      d.FillIn("If other:", font_size=8.5, height=18)]),
    ("Floor (over uncond. space)",
     C("Fiberglass", "Spray Foam", "Rigid Board")),
    ("Basement Walls", C("Rigid Board", "Spray Foam", "Batt", "N/A")),
    ("Crawlspace Walls", C("Rigid Board", "Spray Foam", "N/A")),
    ("Crawlspace Floor (if vented)", C("Batt", "Spray Foam", "N/A")),
    ("Rim Joist",
     C("Spray Foam", "Rigid + Caulk", "Batt (not recommended)")),
    ("Garage Ceiling (if cond. above)", C("Batt", "Blown-in", "N/A")),
    ("Knee Walls", C("Batt", "Spray Foam", "N/A")),
]]
flow.append(d.titled_table(
    "R-Values by Assembly — Required vs. Installed", _sched_header,
    _sched_rows, SCHEDULE_COLS, S,
    row_heights=measured_heights(_sched_rows, SCHEDULE_COLS)))
flow.append(Spacer(1, 10))

flow.append(Paragraph("Climate Zone & Code Requirements", S["h3"]))
flow.append(d.FillInRow([("IECC Climate Zone:", 1.0)]))
flow.append(Paragraph("Minimum R-values per code:", S["body"]))
flow.append(d.FillInRow([("Walls: R-", 0.34), ("Ceiling: R-", 0.33),
                         ("Floor: R-", 0.33)]))
flow.append(d.FillInRow([("Energy Code Version:", 1.0)]))

# ---------------- AIR SEALING
flow += section("AIR SEALING CHECKLIST", S)
flow += check_table("Top Plates & Framing Penetrations", [
    "Top plates of exterior walls sealed to drywall/sheathing",
    "Top plates of interior walls sealed (if attic above)",
    "Bottom plates sealed to subfloor",
    "Rim joist sealed to sill plate",
    "Rim joist sealed to subfloor",
    "Band joist/rim joist fully insulated and sealed",
    "All wall-to-floor intersections sealed",
    "All wall-to-ceiling intersections sealed",
])
flow += check_table("Electrical Penetrations", [
    "Electrical boxes in exterior walls sealed to drywall",
    "Airtight electrical box gaskets installed (if applicable)",
    "Wire penetrations through plates sealed with foam/caulk",
    "Service panel penetrations sealed",
    "Recessed lights IC-rated for contact with insulation",
    "Non-IC recessed lights have airtight cover box",
    "Recessed lights sealed to drywall",
])
flow += check_table("Plumbing Penetrations", [
    "Plumbing pipes through plates sealed with foam",
    "Plumbing stack penetrations through attic sealed",
    "Bathtub/shower plumbing wall sealed at access",
    "Under-sink cabinet backs sealed (exterior walls)",
    "Basement/crawlspace plumbing penetrations sealed",
])
flow += check_table("HVAC Penetrations", [
    "HVAC duct boots sealed to drywall/subfloor",
    "Supply register boots sealed airtight",
    "Return air grille boots sealed airtight",
    "Ductwork penetrations through top plates sealed",
    "Bathroom exhaust fan housing sealed to drywall",
    "Kitchen range hood duct sealed at penetrations",
    "Dryer vent sealed at all penetrations",
    "Combustion appliance vents sealed at penetrations",
])
flow += check_table("Window & Door Rough Openings", [
    "Window rough openings sealed with foam before install",
    "Door rough openings sealed with foam before install",
    "Window/door frames caulked to rough opening",
    "Window/door frames sealed to exterior sheathing",
    "Windows/doors shimmed and spaces foamed (not overfilled)",
])
flow += check_table("Attic & Ceiling Penetrations", [
    "Attic access door/hatch weatherstripped",
    "Attic access door/hatch insulated on top",
    "Pull-down attic stairs insulated cover installed",
    "Chimney chase sealed and insulated at attic floor",
    "Chimney clearances to combustibles maintained",
    "Dropped ceilings/soffits sealed at top",
    "Knee wall access doors weatherstripped/insulated",
    "All ceiling penetrations (wires, pipes) sealed",
])

# ---------------- QUALITY
flow += section("AIR SEALING & INSULATION QUALITY", S)
flow += check_table("General Air Sealing", [
    "Garage walls/ceiling to house sealed (fire barrier)",
    "Cantilever floors sealed and insulated",
    "Stairwell walls to unconditioned space sealed",
    "Behind tubs/showers on exterior walls sealed",
    "Fireplace firebox sealed to framing",
])
flow += spec_table("Vapor Barrier", [
    ("Vapor barrier required per climate zone", C("Yes", "No")),
    ("Vapor barrier type used", C("Poly", "Kraft-faced", "N/A")),
    ("Vapor barrier on warm side of insulation", ""),
    ("Vapor barrier overlapped at seams (6\" minimum)", ""),
    ("Vapor barrier sealed at penetrations", ""),
    ("No double vapor barriers created", ""),
])
flow += check_table("Insulation Installation Quality", [
    "Batt insulation completely fills cavities (no gaps)",
    "Batt insulation not compressed (reduces R-value)",
    "Insulation split around wires/pipes (not behind)",
    "Insulation tight to electrical boxes",
    "Blown insulation to proper depth/density",
    "Spray foam properly expanded (not overspray)",
    "Proper ventilation maintained (if vented attic)",
    "Soffit vents not blocked by insulation",
    "Attic ventilation baffles installed",
    "Attic insulation depth markers/rulers installed",
])
flow.append(d.WriteBox(1.8, label="Final Notes"))

# ---------------- SIGN-OFF
flow += section("INSPECTION SIGN-OFF", S)
flow += d.signature_block([
    ("Owner/Builder", True),
    ("Insulation Contractor", True),
    ("Inspector", True),
])
flow.append(d.checkbox_choice_row(
    "RESULT:", ["PASSED", "Corrections Required"], S))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-3-rough-in-phase",
                       "3.5-insulation-air-sealing-guide.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
