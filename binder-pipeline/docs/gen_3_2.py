#!/usr/bin/env python3
"""3.2 Electrical Rough-In Log — rebuilt on the 2026 design system."""

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
FORM_ID = "3.2"
FORM_TITLE = "Electrical Rough-In Log"

ROOM_COLS = [0.42 * inch, 2.50 * inch, 1.70 * inch, 0.85 * inch,
             CW - 5.47 * inch]
SPEC_COLS = [0.42 * inch, 2.95 * inch, 1.75 * inch, CW - 5.12 * inch]
CHECK_COLS = [0.42 * inch, 3.60 * inch, CW - 4.02 * inch]
CIRCUIT_COLS = [0.80 * inch, 0.80 * inch, 2.40 * inch, 0.70 * inch,
                0.85 * inch, CW - 5.55 * inch]


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


def F(label, height=24):
    """A labelled drawn write-in rule inside a cell — never underscores."""
    return d.FillIn(label, font_size=9.5, height=height)


def FC(text, label="Count:"):
    """Write-in item whose name is too long to share a line with its rule:
    name above, drawn rule below, so the rule keeps real writing room."""
    return [P(text), d.FillIn(label, font_size=9, height=20)]


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


def room_table(title, items):
    """[box] Item/Location | Type/Specification | Circuit # | Notes."""
    header = ["",
              Paragraph("Item / Location", S["cell-bold"]),
              Paragraph("Type / Specification", S["cell-bold"]),
              Paragraph("Circuit #", S["cell-bold"]),
              Paragraph("Notes", S["cell-bold"])]
    rows = []
    for entry in items:
        item, spec = entry[0], entry[1]
        circuit = entry[2] if len(entry) > 2 else ""
        rows.append([d.Checkbox(), cell(item), cell(spec), circuit, ""])
    return [d.titled_table(title, header, rows, ROOM_COLS, S,
                           row_heights=measured_heights(rows, ROOM_COLS)),
            Spacer(1, 8)]


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
    purpose="Room-by-room record of every box, outlet, switch and circuit "
            "installed at rough-in — plus the circuit schedule, quality "
            "checks and inspection result.")

flow.append(d.FillInRow([("Property Address:", 1.0)]))
flow.append(d.FillInRow([("Permit Number:", 0.5), ("Inspection Date:", 0.5)]))
flow.append(d.FillInRow([("Inspector:", 0.5), ("Electrician:", 0.5)]))
flow.append(d.FillInRow([("License #:", 0.5), ("Phone:", 0.5)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>INSTRUCTIONS:</b> Work room by room. Record the circuit number for "
    "every device as you install it — that record becomes your panel "
    "directory, and reconstructing it after drywall is nearly impossible. "
    "Photograph each wall before insulation goes in.", S["body"]))
flow.append(Spacer(1, 4))

# ---------------- ROOM BY ROOM
flow += section("ROOM-BY-ROOM ROUGH-IN", S)

flow += room_table("Master Bedroom", [
    ("Ceiling light/fan box", C("Light", "Fan-rated")),
    (F("Wall outlets — count:"), "15A or 20A duplex"),
    ("Outlet spacing (12' max)", "Per code"),
    (F("Outlet height (in):"), "Typically 12\"–18\" AFF"),
    (F("Light switch(es) — count:"), C("Single", "3-way", "4-way")),
    (F("Switch height (in):"), "Typically 48\" AFF"),
    ("Cable/data outlets", "TV, phone, ethernet", "N/A"),
    ("Smoke detector location", "Hardwired + battery"),
    ("Closet light", "LED or protected fixture"),
])

flow += room_table("Master Bathroom", [
    ("Vanity lights", "Above/beside mirror"),
    (F("GFCI outlet(s) — count:"), "20A, within 3' of sink"),
    (F("Outlet height (in):"), "Typically 42\" AFF"),
    ("Exhaust fan/vent", "Dedicated circuit preferred"),
    ("Heat lamp (if applicable)", "Separate switch"),
    ("Shower/tub light", "Wet location rated"),
    ("Heated floor (if applicable)", "Dedicated 20A circuit"),
    ("Outlets 6' from water source", "Code compliance check", "N/A"),
])

flow += room_table("Bedroom #2", [
    ("Ceiling light/fan box", C("Light", "Fan-rated")),
    (F("Wall outlets — count:"), "15A or 20A duplex"),
    (F("Light switch(es) — count:"), C("Single", "3-way")),
    ("Cable/data outlets", "TV, ethernet", "N/A"),
    ("Closet light", "LED or protected"),
])

flow += room_table("Bedroom #3", [
    ("Ceiling light/fan box", C("Light", "Fan-rated")),
    (F("Wall outlets — count:"), "15A or 20A duplex"),
    (F("Light switch(es) — count:"), C("Single", "3-way")),
    ("Cable/data outlets", "TV, ethernet", "N/A"),
    ("Closet light", "LED or protected"),
])

flow += room_table("Bathroom #2", [
    ("Vanity lights", "Above/beside mirror"),
    (F("GFCI outlet(s) — count:"), "20A, within 3' of sink"),
    ("Exhaust fan/vent", "Dedicated circuit preferred"),
    ("Shower/tub light", "Wet location rated"),
])

flow += room_table("Kitchen", [
    ("Refrigerator outlet", "Dedicated 20A circuit"),
    ("Dishwasher outlet/junction", "Dedicated 20A circuit"),
    ("Garbage disposal outlet/switch", "20A circuit, switch above counter"),
    ("Microwave outlet", "Dedicated 20A circuit"),
    ("Range/cooktop", C("240V 50A", "Gas with 120V")),
    ("Range hood/vent fan", "Dedicated circuit"),
    ("Counter outlets — minimum 2", "20A GFCI, above backsplash"),
    ("Counter outlet spacing (4' max)", "Per code requirement"),
    ("Island outlet", "20A GFCI if applicable"),
    ("Under-cabinet lighting", "Switched circuit"),
    ("Ceiling light(s)", "Centered or per plan"),
    ("Pantry light", "Switched"),
    (F("Light switches — count:"), C("Single", "3-way")),
])
flow.append(d.WriteBox(1.2, label="Kitchen Notes"))
flow.append(Spacer(1, 8))

flow += room_table("Living Room / Family Room", [
    ("Ceiling light/fan boxes",
     [d.FillIn("Count:", font_size=8.5, height=18), C("Fan-rated")]),
    (F("Wall outlets — count:"), "15A or 20A duplex"),
    ("Outlet spacing (12' max)", "Per code"),
    (F("Light switches — count:"), C("Single", "3-way", "4-way")),
    ("Cable/data outlets", "TV, ethernet, phone", "N/A"),
    ("Fireplace outlet (if applicable)", "Dedicated circuit"),
    ("Smoke detector", "Hardwired + battery"),
])

flow += room_table("Dining Room", [
    ("Ceiling light/chandelier box", "Centered over table area"),
    (F("Wall outlets — count:"), "15A or 20A duplex"),
    (F("Light switches — count:"), C("Single", "3-way", "Dimmer")),
])

flow += room_table("Hallway(s)", [
    (F("Ceiling lights — count:"), "Spacing per plan"),
    (F("Wall outlets — count:"), "Within 25' spacing"),
    ("3-way switches at hall ends", "If hall over 10'"),
    ("Smoke/CO detectors", "Hardwired + battery"),
    ("Linen closet light", "Switched"),
])

flow += room_table("Laundry Room", [
    ("Washer outlet", "Dedicated 20A circuit"),
    ("Dryer outlet", C("240V 30A", "Gas with 120V")),
    ("Ceiling light", "Switched"),
    ("Utility sink outlet", "GFCI protected"),
    (FC("Additional outlets"), "For iron, etc."),
])

flow += room_table("Garage", [
    (FC("Garage door opener outlet(s)"), "Ceiling mounted"),
    (F("Wall outlets — count:"), "GFCI protected, 15A or 20A"),
    (F("Ceiling lights — count:"), "LED recommended"),
    ("3-way switches (garage/house)", "If applicable"),
    ("Workbench circuit", "Dedicated 20A recommended"),
    ("EV charger circuit (if applicable)", "240V 50A dedicated"),
    ("Smoke/CO detector", "Hardwired if attached garage"),
])

flow += room_table("Utility / Mechanical Room", [
    ("Furnace/air handler circuit", "Per equipment specs"),
    ("Water heater circuit", C("240V", "120V")),
    ("Ceiling light", "Required, switched at door"),
    ("Utility outlet", "20A minimum"),
    ("Sump pump outlet (if applicable)", "Dedicated 20A, GFCI"),
])

# ---------------- EXTERIOR
flow += section("EXTERIOR ELECTRICAL", S)
flow += room_table("Exterior Devices & Equipment Circuits", [
    ("Front porch light", "Weatherproof, switched inside"),
    ("Back porch/deck light", "Weatherproof, switched inside"),
    ("Front outlet", "GFCI, weatherproof cover"),
    ("Back outlet", "GFCI, weatherproof cover"),
    (FC("Side yard outlet(s)"), "GFCI, weatherproof"),
    ("Landscape lighting (if applicable)",
     "Low voltage transformer location"),
    ("Driveway/walkway lights", "As per plan"),
    ("Security lights/motion sensors", "Weatherproof boxes"),
    ("Well pump circuit (if applicable)", "Per pump specifications"),
    ("Septic pump circuit (if applicable)", "Dedicated, per specs"),
    ("Pool equipment (if applicable)", "Per code and equipment specs"),
    ("Hot tub circuit (if applicable)", "GFCI protected, per specs"),
    ("AC condensing unit disconnect", "Within sight, proper size"),
])
flow.append(d.WriteBox(1.2, label="Exterior Electrical Notes"))

# ---------------- SERVICE PANEL
flow += section("SERVICE PANEL & ELECTRICAL SERVICE", S)
flow += spec_table("Service, Grounding & Overcurrent Protection", [
    ("Main service panel size", C("100A", "150A", "200A")),
    ("Main panel location accessible", "Per code clearances"),
    ("Service entrance cable/conduit", "Proper size for service"),
    ("Meter base installed", "Utility approved location"),
    ("Grounding electrode system", "Rods, water pipe, etc."),
    ("Grounding electrode conductor", "Proper size, connections"),
    ("Main bonding jumper installed", "At service equipment"),
    ("Subpanel(s) if applicable", F("Location:", height=22)),
    ("Subpanel feeder size adequate", "Per load calculation"),
    ("Surge protection device", C("Installed", "Not included")),
    ("Circuit directory/labels prepared", "Ready for final"),
    ("AFCI breakers where required", "Bedrooms, living areas"),
    ("GFCI breakers/outlets where required",
     "Baths, kitchen, exterior, etc."),
    ("Generator interlock/transfer switch",
     C("Yes", "No", "Future provision")),
])
flow.append(d.WriteBox(1.2, label="Service Panel Notes"))

# ---------------- SPECIAL SYSTEMS
flow += section("SPECIAL SYSTEMS", S)
_special_header = ["",
                   Paragraph("System", S["cell-bold"]),
                   Paragraph("Status", S["cell-bold"]),
                   Paragraph("Notes", S["cell-bold"])]
_special_rows = [[d.Checkbox(), P(name), status, ""] for name, status in [
    ("Security system pre-wire", C("Yes", "No")),
    ("Doorbell/intercom wiring", C("Wired", "Wireless")),
    ("Whole-house audio pre-wire", C("Yes", "No")),
    ("Central vacuum rough-in", C("Yes", "No")),
    ("Home automation hubs/panels", C("Yes", "No")),
]]
flow.append(d.titled_table(
    "Low-Voltage & Pre-Wire", _special_header, _special_rows, SPEC_COLS, S,
    row_heights=measured_heights(_special_rows, SPEC_COLS)))
flow.append(Spacer(1, 8))

# ---------------- QUALITY
flow += section("ROUGH-IN QUALITY CHECKS", S)
flow += check_table("Boxes, Cable & Protection", [
    "All boxes properly secured to framing",
    "Box depth adequate for wall finish thickness",
    "Cable secured within 12\" of boxes",
    "Cable secured along runs per code (4.5' max)",
    "Cable protected where passing through framing",
    "Nail plates installed over cables in studs/joists",
    "Proper cable type used (NM-B, UF, etc.)",
    "Wire size adequate for circuit amperage",
    "Minimum 6\" of wire left at each box",
    "Cable sheathing extends into boxes 1/4\" min",
    "No damaged cable insulation visible",
    "Proper box fill not exceeded",
    "All splices made in approved boxes",
    "Recessed light boxes IC-rated if touching insulation",
    "Bathroom exhaust fans vented to exterior",
])
flow.append(d.WriteBox(1.2, label="General Notes"))

# ---------------- CIRCUIT SCHEDULE
flow += section("CIRCUIT SCHEDULE", S)
_circuit_header = [Paragraph("Circuit&nbsp;#", S["cell-bold"]),
                   Paragraph("Breaker Size", S["cell-bold"]),
                   Paragraph("Circuit Description / Location", S["cell-bold"]),
                   Paragraph("Wire Size", S["cell-bold"]),
                   Paragraph("AFCI / GFCI", S["cell-bold"]),
                   Paragraph("Notes", S["cell-bold"])]
_circuit_rows = [[Paragraph(str(n), S["cell-center"]), "", "", "", "", ""]
                 for n in range(1, 31)]
flow.append(d.titled_table(
    "Panel Directory — Record As You Wire", _circuit_header, _circuit_rows,
    CIRCUIT_COLS, S,
    row_heights=[d.WRITE_ROW_PT] * len(_circuit_rows)))
flow.append(Spacer(1, 8))

# ---------------- INSPECTION
flow += section("INSPECTION RESULTS & CORRECTIONS", S)

flow.append(Paragraph("Initial Electrical Rough-In Inspection", S["h3"]))
flow.append(d.FillInRow([("Inspection Date:", 0.5), ("Time:", 0.5)]))
flow.append(d.FillInRow([("Inspector Name:", 0.6),
                         ("Inspector Badge/ID:", 0.4)]))
flow.append(d.checkbox_choice_row(
    "RESULT:", ["PASSED", "FAILED — Corrections Required"], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.3, label="Deficiencies / Code Violations Found"))

flow.append(Paragraph("Corrections Made", S["h3"]))
flow.append(d.FillInRow([("Date Corrections Completed:", 1.0)]))
flow.append(d.FillInRow([("Licensed Electrician:", 0.65),
                         ("License #:", 0.35)]))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.2, label="Description of Corrections"))

flow.append(Paragraph("Re-Inspection (if required)", S["h3"]))
flow.append(d.FillInRow([("Re-Inspection Date:", 0.5), ("Time:", 0.5)]))
flow.append(d.FillInRow([("Inspector Name:", 1.0)]))
flow.append(d.checkbox_choice_row(
    "RESULT:", ["PASSED", "FAILED — Additional Corrections Required"], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.0, label="Additional Comments"))

# ---------------- SIGN-OFF
flow += section("FINAL SIGN-OFF", S)
flow += d.signature_block([
    ("Owner/Builder Signature", True),
    ("Licensed Electrician Signature", True),
    ("Inspector Signature", True),
])
flow.append(d.FillInRow([("Permit Number:", 1.0)]))
flow.append(d.checkbox_choice_row("FINAL APPROVAL:", ["YES"], S))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-3-rough-in-phase",
                       "3.2-electrical-rough-in-log.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
