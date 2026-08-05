#!/usr/bin/env python3
"""4.3 HVAC System Completion & Commissioning — rebuilt on the 2026 design
system."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import CondPageBreak, Flowable, Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 4: Systems Installation"
FORM_ID = "4.3"
FORM_TITLE = "HVAC System Completion"

MEASURE_COLS = [3.90 * inch, CW - 3.90 * inch]


class ChoiceCell(Flowable):
    """Mutually-exclusive options as drawn boxes, wrapping to fit a table cell.

    Replaces the ☐ glyph runs the old build used inside status columns.
    """

    def __init__(self, options, box=9, font_size=8, gap=7, lead=12):
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
            w = self.box + 3 + stringWidth(opt, d.BODY, self.font_size)
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
                x += self.box + 3
                c.setFont(d.BODY, self.font_size)
                c.drawString(x, y + 1, opt)
                x += stringWidth(opt, d.BODY, self.font_size) + self.gap
            y -= self.lead


class CenterBox(Flowable):
    """A drawn checkbox centred in its column — for single-mark test columns."""

    def __init__(self, size=14):
        super().__init__()
        self.size = size

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self.height = self.size
        return self.width, self.height

    def draw(self):
        self.canv.setStrokeColor(d.INK)
        self.canv.setLineWidth(1)
        self.canv.rect((self.width - self.size) / 2.0, 0, self.size, self.size)


def P(text):
    return Paragraph(text, S["cell"])


def C(*options):
    return ChoiceCell(list(options))


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


def head(labels):
    return [Paragraph(t, S["cell-bold"]) for t in labels]


def log_table(title, labels, cols, count, marks=None):
    marks = marks or {}
    rows = []
    for _ in range(count):
        rows.append([CenterBox() if marks.get(c) == "box"
                     else (C(*marks[c]) if c in marks else "")
                     for c in range(len(labels))])
    return [d.titled_table(title, head(labels), rows, cols, S,
                           row_heights=measured_heights(rows, cols)),
            Spacer(1, 8)]


def measure_table(title, items):
    """Commissioning readings: labelled measurement, written-in value.
    A `None` value is a blank write-in cell; a ChoiceCell gives drawn boxes."""
    rows = [[P(label), value if value is not None else ""]
            for label, value in items]
    return [d.titled_table(title, head(["Measurement", "Reading / Value"]),
                           rows, MEASURE_COLS, S,
                           row_heights=measured_heights(rows, MEASURE_COLS)),
            Spacer(1, 8)]



def section(title, styles=None, min_space=3.4):
    """An h2 that will not strand itself at the foot of a page: it reserves
    room for the heading plus the opening rows of whatever follows."""
    return [CondPageBreak(min_space * inch)] + d.h2(title, S)


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Installation, startup and commissioning of the complete HVAC "
            "system — the measurements that prove it runs efficiently, "
            "safely and as designed.")

flow.append(d.FillInRow([("Project Address:", 1.0)]))
flow.append(d.FillInRow([("Project Name:", 0.6), ("Permit Number:", 0.4)]))
flow.append(d.FillInRow([("HVAC Contractor:", 0.62),
                         ("License Number:", 0.38)]))
flow.append(d.FillInRow([("Contact Phone:", 1.0)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>PURPOSE:</b> This document verifies proper installation, startup and "
    "commissioning of the complete HVAC system. Proper commissioning ensures "
    "the system operates efficiently, safely and as designed.", S["body"]))
flow.append(Spacer(1, 4))

# ---------------- EQUIPMENT INSTALLATION
flow += section("EQUIPMENT INSTALLATION", S)

flow.append(Paragraph("Indoor Unit (Furnace / Air Handler)", S["h3"]))
flow.append(d.FillInRow([("Make/Model:", 0.6), ("Serial Number:", 0.4)]))
flow.append(d.FillInRow([("BTU Input/Output:", 0.5), ("AFUE Rating:", 0.5)]))
flow.append(d.FillInRow([("Location:", 0.6), ("Installation Date:", 0.4)]))
flow.append(d.checkbox_choice_row(
    "FUEL TYPE:", ["Natural Gas", "Propane", "Electric", "Oil"], S))
flow.append(Spacer(1, 4))
flow.append(d.items_checklist([
    "Unit installed level and properly supported",
    "Proper clearances maintained (front, sides, top per manufacturer)",
    "Unit properly secured to platform or hung from joists",
    "Gas line connected properly (if gas) — no leaks",
    "Gas shut-off valve within 6 feet (if gas)",
    "Gas line pressure tested (if gas)",
    "Electrical connection made — proper voltage and amperage",
    "Electrical disconnect within sight of unit",
    "Condensate drain line installed with proper slope",
    "Condensate drain terminates appropriately",
    "Condensate trap installed (if required)",
    "Secondary drain pan installed (if in attic/living space)",
    "Secondary drain pan alarm/sensor installed",
    "Combustion air intake adequate (if gas)",
    "Vent pipe properly installed (if gas)",
    "Vent pipe properly supported and sloped",
    "Vent termination proper distance from windows/openings",
    "Filter access accessible",
    "Blower door/access panels properly secured",
], S))

flow.append(Paragraph("Outdoor Unit (Condensing Unit / Heat Pump)", S["h3"]))
flow.append(d.FillInRow([("Make/Model:", 0.6), ("Serial Number:", 0.4)]))
flow.append(d.FillInRow([("Tonnage:", 0.5), ("SEER Rating:", 0.5)]))
flow.append(d.FillInRow([("Refrigerant Type:", 0.5), ("Location:", 0.5)]))
flow.append(d.checkbox_choice_row("TYPE:",
                                  ["Air Conditioner", "Heat Pump"], S))
flow.append(Spacer(1, 4))
flow.append(d.items_checklist([
    "Unit installed on level pad (concrete or composite)",
    "Pad stable and properly sized",
    "Unit level side-to-side and front-to-back (within 1/4\")",
    "Proper clearances maintained (12\" sides, 24\" service side, 60\" top)",
    "No vegetation or obstructions blocking airflow",
    "Refrigerant lines connected and insulated",
    "Line set insulation complete — no exposed copper",
    "Line set properly secured to structure",
    "Electrical disconnect installed within sight of unit",
    "Electrical disconnect proper rating (check data plate)",
    "Whip (flexible conduit) to unit installed properly",
    "Electrical connections tight at contactor and terminals",
    "Condenser fan rotates freely by hand (power off)",
    "Coil fins undamaged and clean",
    "Service valves accessible",
], S))

# ---------------- DUCTWORK
flow += section("DUCTWORK COMPLETION", S)
flow.append(d.items_checklist([
    "All supply registers installed",
    "All supply registers properly secured",
    "Register boot connections sealed with mastic",
    "All return grilles installed",
    "Return grille connections sealed",
    "Main trunk line connections sealed",
    "All branch take-offs sealed",
    "Flexible duct properly supported (every 4–5 feet)",
    "Flexible duct not kinked or crushed",
    "Ductwork insulation complete (if required)",
    "No disconnected ductwork",
    "Filter installed — correct size recorded below",
    "Filter access accessible",
    "Return air pathways adequate (no blocked returns)",
    "Access panels installed for dampers and controls",
], S))
flow.append(Spacer(1, 4))
flow.append(d.FillInRow([("Filter size installed:", 1.0)]))
flow.append(Spacer(1, 6))

flow += log_table(
    "Register / Grille Schedule",
    ["Room", "Supply Register Size", "Qty", "Return Grille Size", "Qty",
     "Notes"],
    [1.55 * inch, 1.30 * inch, 0.55 * inch, 1.25 * inch, 0.55 * inch,
     CW - 5.20 * inch],
    15)

# ---------------- THERMOSTAT
flow += section("THERMOSTAT INSTALLATION", S)
flow.append(d.FillInRow([("Make/Model:", 0.6), ("Location:", 0.4)]))
flow.append(d.FillInRow([("Number of Zones:", 1.0)]))
flow.append(d.checkbox_choice_row(
    "TYPE:", ["Programmable", "Non-Programmable", "Smart/WiFi"], S))
flow.append(Spacer(1, 4))
flow.append(d.items_checklist([
    "Thermostat located on interior wall (not exterior)",
    "Location away from direct sunlight",
    "Location away from heat sources (lamps, appliances)",
    "Location away from drafts (doors, windows)",
    "Thermostat mounted level at 52–60\" height",
    "All wires properly labeled",
    "All wire connections tight",
    "Thermostat wired correctly — tested with system",
    "Programmable thermostat programmed (if applicable)",
    "Smart thermostat connected to WiFi (if applicable)",
    "Homeowner trained on thermostat operation",
    "Manual/instructions left with homeowner",
], S))

# ---------------- COMMISSIONING
flow += section("SYSTEM COMMISSIONING", S)
flow.append(Paragraph(
    "Professional commissioning must be performed by a qualified HVAC "
    "technician:", S["body"]))
flow.append(d.FillInRow([("Commissioning Technician:", 0.6),
                         ("Company:", 0.4)]))
flow.append(d.FillInRow([("License Number:", 0.5),
                         ("Commissioning Date:", 0.5)]))
flow.append(Spacer(1, 6))

flow += measure_table("Refrigerant Charging (Air Conditioner / Heat Pump)", [
    ("Refrigerant type", None),
    ("Charge weight (lbs)", None),
    ("Charging method", C("Subcooling", "Superheat", "Weigh-In")),
    ("Outdoor temperature (°F)", None),
    ("Indoor temperature (°F)", None),
    ("Indoor relative humidity (%)", None),
])

flow += measure_table("Subcooling Method (preferred for TXV systems)", [
    ("High side pressure (PSI)", None),
    ("Saturation temperature (°F)", None),
    ("Liquid line temperature (°F)", None),
    ("Subcooling (°F)", None),
    ("Target subcooling per manufacturer", None),
    ("Subcooling within spec", C("Yes", "No")),
])

flow += measure_table("Superheat Method (fixed orifice / piston systems)", [
    ("Low side pressure (PSI)", None),
    ("Saturation temperature (°F)", None),
    ("Suction line temperature (°F)", None),
    ("Superheat (°F)", None),
    ("Target superheat per manufacturer", None),
    ("Superheat within spec", C("Yes", "No")),
])

flow += measure_table("Airflow Verification", [
    ("Blower speed setting", None),
    ("Supply air temperature (°F)", None),
    ("Return air temperature (°F)", None),
    ("Temperature split (°F)", None),
    ("Target split (cooling: 15–20°F)", None),
    ("Airflow CFM (if measured)", None),
    ("Target airflow (400 CFM/ton)", None),
    ("Airflow adequate", C("Yes", "No")),
])

flow += measure_table("Gas Furnace Checks (if applicable)", [
    ("Gas type", C("Natural Gas", "Propane")),
    ("Manifold pressure (in. w.c.)", None),
    ("Target manifold pressure", None),
    ("Temperature rise (°F)", None),
    ("Target temperature rise range", None),
    ("Flame appearance", C("Blue/Stable", "Other — describe in notes")),
    ("Carbon monoxide test (PPM)", None),
    ("CO level acceptable (&lt;10 PPM)", C("Yes", "No")),
    ("Vent draft adequate", C("Yes", "No", "N/A")),
])

# ---------------- OPERATIONAL TESTING
flow += section("OPERATIONAL TESTING", S)

flow.append(Paragraph("Heating Mode Test", S["h3"]))
flow.append(d.items_checklist([
    "Thermostat set to HEAT mode",
    "Temperature set above room temperature",
    "Furnace/heat pump starts within 1–2 minutes",
    "Ignition sequence normal (if gas)",
    "Burner flames stable and blue (if gas)",
    "Blower starts after heat-up delay",
    "Warm air from all supply registers",
    "Airflow adequate at all registers",
    "System runs continuously without cycling",
    "No unusual noises during operation",
    "System reaches temperature setpoint and cycles off",
    "Blower continues for cool-down period",
    "No error codes or warning lights",
], S))

flow.append(Paragraph("Cooling Mode Test", S["h3"]))
flow.append(d.items_checklist([
    "Thermostat set to COOL mode",
    "Temperature set below room temperature",
    "Outdoor unit starts (compressor and fan)",
    "Indoor blower starts",
    "Cool air from all supply registers",
    "Temperature drop 15–20°F (supply vs. return)",
    "Condensate draining properly",
    "No water leaks from indoor unit",
    "Outdoor unit running smoothly — no unusual noises",
    "System runs continuously without short-cycling",
    "System reaches temperature setpoint and cycles off",
    "No error codes or warning lights",
], S))

flow.append(Paragraph("General System Operation", S["h3"]))
flow.append(d.items_checklist([
    "Thermostat controls system properly",
    "Fan mode AUTO and ON both work",
    "System cycles properly — not short-cycling",
    "No vibration in ductwork during operation",
    "No whistling or whooshing sounds from registers",
    "All rooms receiving adequate airflow",
    "Return air adequate — no negative pressure issues",
    "Emergency heat operates (if heat pump) — or N/A",
    "Reversing valve operates (if heat pump) — or N/A",
    "Outdoor unit clean and free of debris",
], S))

# ---------------- AIRFLOW BALANCING
flow += section("AIRFLOW BALANCING", S)
flow.append(Paragraph("Verify adequate airflow to all rooms:", S["body"]))
flow += log_table(
    "Room-by-Room Balance Record",
    ["Room", "Supply Register", "Airflow", "Temperature",
     "Damper Adjustment", "Notes"],
    [1.30 * inch, 1.15 * inch, 1.15 * inch, 1.05 * inch, 0.95 * inch,
     CW - 5.60 * inch],
    18, marks={2: ("Good", "Low")})
flow.append(d.items_checklist([
    "All rooms receiving airflow",
    "Hot/cold spots identified and addressed",
    "Dampers adjusted for balanced airflow",
    "Temperature variation between rooms minimal (within 3–4°F)",
], S))

# ---------------- FINAL INSPECTION
flow += section("FINAL HVAC INSPECTION", S)
flow.append(d.FillInRow([("Inspection Requested Date:", 0.5),
                         ("Inspection Scheduled Date:", 0.5)]))
flow.append(d.FillInRow([("Inspector Name:", 1.0)]))
flow.append(d.FillInRow([("Inspection Date:", 0.5),
                         ("Inspection Time:", 0.5)]))
flow.append(Spacer(1, 4))
flow.append(Paragraph("Pre-Inspection Checklist", S["h3"]))
flow.append(d.items_checklist([
    "All equipment properly installed",
    "All ductwork complete and sealed",
    "System commissioned by qualified technician",
    "Refrigerant charge verified",
    "Heating and cooling both tested",
    "Thermostat functioning properly",
    "All required disconnects installed",
    "Proper clearances maintained",
    "Condensate drains functioning",
    "Work completed per approved plans",
], S))
flow.append(Spacer(1, 4))
flow.append(d.checkbox_choice_row(
    "INSPECTION RESULT:",
    ["PASSED — Certificate Issued", "FAILED — Corrections Required"], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.7, label="Required Corrections"))
flow.append(Spacer(1, 6))
flow.append(d.FillInRow([("Corrections Completed Date:", 0.5),
                         ("Re-Inspection Date:", 0.5)]))
flow.append(d.checkbox_choice_row("RE-INSPECTION RESULT:",
                                  ["PASSED", "FAILED"], S))

# ---------------- WARRANTY
flow += section("WARRANTY & DOCUMENTATION", S)
flow.append(d.FillInRow([("Equipment Warranty Period:", 0.5),
                         ("Parts Warranty Period:", 0.5)]))
flow.append(d.FillInRow([("Labor Warranty Period:", 0.5),
                         ("Compressor Warranty Period:", 0.5)]))
flow.append(d.checkbox_choice_row("REGISTRATION REQUIRED:", ["Yes", "No"], S))
flow.append(d.checkbox_choice_row("REGISTRATION COMPLETED:",
                                  ["Yes", "No", "N/A"], S))
flow.append(d.FillInRow([("Registration Date:", 1.0)]))
flow.append(Spacer(1, 4))
flow.append(Paragraph("Documentation Provided to Homeowner", S["h3"]))
flow.append(d.items_checklist([
    "Equipment owner's manuals (indoor and outdoor units)",
    "Thermostat manual and programming guide",
    "Warranty information and registration",
    "Filter size and replacement schedule",
    "Maintenance schedule and recommendations",
    "Contractor contact information for service",
    "As-built duct layout (if available)",
    "Commissioning report with all measurements",
], S))

flow.append(Paragraph("Sign-Off", S["h3"]))
flow += d.signature_block([
    ("HVAC Technician Signature", True),
    ("Owner/Builder Signature", True),
])


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-4-systems-installation",
                       "4.3-hvac-system-completion.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
