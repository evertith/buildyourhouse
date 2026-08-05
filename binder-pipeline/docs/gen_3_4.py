#!/usr/bin/env python3
"""3.4 HVAC Rough-In Guide — rebuilt on the 2026 design system."""

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
FORM_ID = "3.4"
FORM_TITLE = "HVAC Rough-In Guide"

# Measurement tables get a taller floor than the 0.40in minimum — a duct size
# and a CFM figure both have to fit, written by hand, on a job site.
DUCT_ROW_PT = 32

OVERVIEW_COLS = [2.60 * inch, 2.30 * inch, CW - 4.90 * inch]
SUPPLY_COLS = [0.42 * inch, 1.75 * inch, 1.05 * inch, 0.85 * inch,
               0.95 * inch, CW - 5.02 * inch]
RETURN_COLS = [0.42 * inch, 2.10 * inch, 1.35 * inch, 1.15 * inch,
               CW - 5.02 * inch]
EQUIP_COLS = [0.42 * inch, 2.60 * inch, 1.90 * inch, CW - 4.92 * inch]
SPEC_COLS = [0.42 * inch, 2.95 * inch, 1.75 * inch, CW - 5.12 * inch]
CHECK_COLS = [0.42 * inch, 3.60 * inch, CW - 4.02 * inch]


class ChoiceCell(Flowable):
    """Mutually-exclusive options as drawn boxes, wrapping to fit a table cell.

    This is what replaces the old '[] Forced Air [] Radiant [] Heat Pump'
    glyph run that used to split mid-option across lines.
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


def spec_table(title, items, item_header="Item", cols=None):
    """[box] Item | Specification | Notes."""
    cols = cols or SPEC_COLS
    header = ["",
              Paragraph(item_header, S["cell-bold"]),
              Paragraph("Specification", S["cell-bold"]),
              Paragraph("Notes", S["cell-bold"])]
    rows = [[d.Checkbox(), cell(item), cell(spec), ""] for item, spec in items]
    return [d.titled_table(title, header, rows, cols, S,
                           row_heights=measured_heights(rows, cols)),
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
    purpose="System design, duct layout and equipment rough-in recorded "
            "room by room, with the load calculation, quality checklist and "
            "inspection result.")

flow.append(d.FillInRow([("Property Address:", 1.0)]))
flow.append(d.FillInRow([("Permit Number:", 0.5), ("Inspection Date:", 0.5)]))
flow.append(d.FillInRow([("HVAC Contractor:", 0.65), ("License #:", 0.35)]))
flow.append(d.FillInRow([("Phone:", 1.0)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>INSTRUCTIONS:</b> Fill in the system overview and load calculation "
    "before any duct goes up — undersized returns and guessed equipment "
    "capacity are the two most common and most expensive HVAC mistakes an "
    "owner-builder makes. Record actual duct and register sizes as installed.",
    S["body"]))
flow.append(Spacer(1, 4))

# ---------------- SYSTEM OVERVIEW
flow += section("SYSTEM OVERVIEW", S)
_ov_header = [Paragraph("System Component", S["cell-bold"]),
              Paragraph("Type / Specification", S["cell-bold"]),
              Paragraph("Notes", S["cell-bold"])]
_ov_rows = [[P(name), cell(spec), ""] for name, spec in [
    ("Heating System Type", C("Forced Air", "Radiant", "Heat Pump")),
    ("Heating Source", C("Gas", "Electric", "Oil", "Heat Pump")),
    ("Cooling System Type", C("Central AC", "Heat Pump", "Mini-Split")),
    ("System Capacity — Heating", F("BTU:")),
    ("System Capacity — Cooling", F("Tons:")),
    ("Furnace/Air Handler Location",
     C("Basement", "Attic", "Closet", "Garage")),
    ("Condensing Unit Location", F("Location:")),
    ("Zoned System", [C("Yes", "No"), F("If yes, zones:", height=20,
                                        font_size=9)]),
    ("Thermostat Type", C("Programmable", "Smart", "Manual")),
    ("Number of Thermostats", F("Qty:")),
]]
flow.append(d.titled_table("Equipment & Controls Summary", _ov_header,
                           _ov_rows, OVERVIEW_COLS, S,
                           row_heights=measured_heights(_ov_rows,
                                                        OVERVIEW_COLS)))
flow.append(Spacer(1, 8))

# ---------------- LOAD CALCULATION
flow += section("LOAD CALCULATION", S)
flow.append(d.checkbox_choice_row(
    "MANUAL J LOAD CALCULATION PERFORMED:", ["Yes", "No"], S))
flow.append(d.FillInRow([("Calculated By:", 0.65), ("Date:", 0.35)]))
flow.append(d.FillInRow([("Total Heating Load (BTU):", 1.0)]))
flow.append(d.FillInRow([("Total Cooling Load (BTU):", 0.55),
                         ("or Tons:", 0.45)]))
flow.append(d.checkbox_choice_row(
    "LOAD CALCULATION DOCUMENTS ATTACHED:", ["Yes", "No"], S))

# ---------------- SUPPLY DUCT
flow += section("DUCTWORK LAYOUT — SUPPLY", S)
_supply_header = ["",
                  Paragraph("Location / Room", S["cell-bold"]),
                  Paragraph("Register Size", S["cell-bold"]),
                  Paragraph("CFM Req'd", S["cell-bold"]),
                  Paragraph("Duct Size", S["cell-bold"]),
                  Paragraph("Notes", S["cell-bold"])]
_supply_rows = []
for room, register in [
    ("Main trunk line", "N/A"),
    ("Master Bedroom", ""), ("Master Bathroom", ""),
    ("Bedroom #2", ""), ("Bedroom #3", ""), ("Bedroom #4", ""),
    ("Bathroom #2", ""), ("Living Room", ""), ("Dining Room", ""),
    ("Kitchen", ""), ("Family Room", ""), ("Office/Den", ""),
    ("Hallway(s)", ""), ("Basement/Lower Level", ""), ("Bonus Room", ""),
]:
    _supply_rows.append([d.Checkbox(), P(room),
                         P(register) if register else "", "", "", ""])
_supply_rows.append([d.Checkbox(), F("Other:", height=22, font_size=9),
                     "", "", "", ""])
flow.append(d.titled_table(
    "Supply Registers & Branch Ducts", _supply_header, _supply_rows,
    SUPPLY_COLS, S,
    row_heights=measured_heights(_supply_rows, SUPPLY_COLS,
                                 minimum=DUCT_ROW_PT)))
flow.append(Spacer(1, 8))
flow.append(d.WriteBox(1.2, label="Supply Ductwork Notes"))

# ---------------- RETURN DUCT
flow += section("DUCTWORK LAYOUT — RETURN AIR", S)
_return_header = ["",
                  Paragraph("Location", S["cell-bold"]),
                  Paragraph("Return Grille Size", S["cell-bold"]),
                  Paragraph("Duct Size", S["cell-bold"]),
                  Paragraph("Notes", S["cell-bold"])]
_return_rows = []
for loc, grille in [
    ("Main return trunk", "N/A"),
    ("Central hallway return", ""), ("Master bedroom return", ""),
    ("Bedroom #2 return", ""), ("Living area return", ""),
    ("Basement return", ""), ("Second floor return", ""),
]:
    _return_rows.append([d.Checkbox(), P(loc),
                         P(grille) if grille else "", "", ""])
_return_rows.append([d.Checkbox(), F("Other:", height=22, font_size=9),
                     "", "", ""])
flow.append(d.titled_table(
    "Return Grilles & Return Ducts", _return_header, _return_rows,
    RETURN_COLS, S,
    row_heights=measured_heights(_return_rows, RETURN_COLS,
                                 minimum=DUCT_ROW_PT)))
flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Total Return Air CFM Required:", 1.0)]))
flow.append(d.checkbox_choice_row(
    "RETURN AIR ADEQUATELY SIZED FOR SYSTEM:", ["Yes", "No"], S))
flow.append(d.checkbox_choice_row(
    "RETURN AIR LOCATED AWAY FROM SUPPLY REGISTERS:", ["Yes", "No"], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.2, label="Return Air Sizing Notes"))

# ---------------- EQUIPMENT LOCATIONS
flow += section("EQUIPMENT LOCATIONS", S)
_eq_header = ["",
              Paragraph("Equipment / Item", S["cell-bold"]),
              Paragraph("Location", S["cell-bold"]),
              Paragraph("Notes / Requirement", S["cell-bold"])]
_eq_rows = [[d.Checkbox(), P(item), "", P(note) if note else ""]
            for item, note in [
    ("Furnace/Air Handler", ""),
    ("Equipment clearances verified", "Per manufacturer specs"),
    ("Access for service/filter change", "Adequate access provided"),
    ("Condensing unit pad location", ""),
    ("Condensing unit clearances", "Min. 24\" one side, 12\" others"),
    ("Thermostat location — Zone 1", ""),
    ("Thermostat location — Zone 2", ""),
    ("Thermostat on interior wall", "Not on exterior wall"),
    ("Thermostat away from heat sources", "Not near windows, vents, etc."),
    ("Zone dampers (if applicable)", ""),
]]
flow.append(d.titled_table(
    "Equipment & Thermostat Placement", _eq_header, _eq_rows, EQUIP_COLS, S,
    row_heights=measured_heights(_eq_rows, EQUIP_COLS,
                                 minimum=DUCT_ROW_PT)))
flow.append(Spacer(1, 8))

# ---------------- UTILITIES
flow += section("UTILITIES & CONNECTIONS REQUIRED", S)
flow += spec_table("Gas Line (if applicable)", [
    ("Gas line size to furnace", "Per BTU load/distance"),
    ("Gas shut-off valve at equipment", "Within 6' of unit"),
    ("Gas line properly supported", "Per code"),
    ("Sediment trap installed", "Drip leg at appliance"),
    ("Gas line pressure tested", C("Yes", "Pending")),
])
flow += spec_table("Electrical Requirements", [
    ("Furnace/Air Handler circuit", F("Amps (dedicated):", height=22,
                                      font_size=9)),
    ("Condensing unit circuit", F("Amps (dedicated):", height=22,
                                  font_size=9)),
    ("Disconnect switch at condensing unit", "Within sight of unit"),
    ("Thermostat wiring — 18/5 or greater", "Common wire included"),
    ("Zone control wiring (if applicable)", "Per system specs"),
])
flow += spec_table("Condensate Drain", [
    ("Primary condensate drain line", "3/4\" PVC typical"),
    ("Drain line properly sloped", "1/4\" per foot minimum"),
    ("Drain terminates to approved location", "Floor drain, exterior, etc."),
    ("P-trap in condensate line", "Required for proper operation"),
    ("Secondary/emergency drain pan (if req.)", "For attic installations"),
    ("Emergency drain visible termination", "Alert to primary drain clog"),
])
flow += spec_table("Combustion Air & Venting (Gas/Oil Systems)", [
    ("Combustion air provisions adequate", "Per manufacturer/code"),
    ("Vent pipe size correct", "Per appliance specs"),
    ("Vent termination location approved", "Clearances from openings"),
    ("Vent properly supported/sloped", "Per manufacturer"),
])

# ---------------- QUALITY CHECKLIST
flow += section("ROUGH-IN QUALITY CHECKLIST", S)
flow += check_table("Ductwork Installation", [
    "All ductwork installed per approved plan",
    "Duct sizes match design specifications",
    "Ductwork properly supported every 4'–6'",
    "All joints sealed with mastic or approved tape",
    "No cloth duct tape used (not code compliant)",
    "Flexible duct fully extended (no sagging)",
    "Flexible duct runs limited to 8'–10' max",
    "Proper transition fittings used",
    "Return air plenums sealed at equipment",
    "No return air leaks in unconditioned spaces",
    "Supply boots properly installed and sealed",
    "Boot supports installed in ceiling/floor",
    "Register/grille locations marked",
    "Ductwork in unconditioned spaces insulated",
    "Insulation R-value meets code minimum",
    "Vapor barrier on insulation facing outward",
    "No sharp bends or kinks in ductwork",
    "Turning vanes in square elbows (if required)",
])
flow.append(d.WriteBox(1.2, label="Ductwork Notes"))

flow += check_table("Equipment Rough-In", [
    "Equipment platform/stand level and secure",
    "Vibration isolation if required",
    "Refrigerant line set path planned/installed",
    "Line set properly sized for system",
    "Line set insulated and protected",
    "Line set penetrations sealed",
    "Thermostat wire run to all locations",
    "Extra thermostat wire coiled at equipment",
    "Condensate drain rough-in complete",
    "Equipment access door/panel clearance verified",
])
flow += check_table("Penetrations & Sealing", [
    "All duct penetrations through fire-rated walls sealed",
    "Duct penetrations through roof properly flashed",
    "Duct penetrations to exterior sealed airtight",
    "No ducts running through garage (if code prohibits)",
    "Fire dampers installed where required",
    "Backdraft dampers on exhaust vents",
])
flow += check_table("Code Compliance", [
    "System meets energy code requirements",
    "Equipment SEER/AFUE ratings meet minimums",
    "Duct insulation meets energy code",
    "Combustion air meets code requirements",
    "Equipment clearances meet manufacturer specs",
    "Gas venting meets code and manufacturer specs",
    "Return air not from garage or bathrooms",
])

# ---------------- ADDITIONAL COMPONENTS
flow += section("ADDITIONAL HVAC COMPONENTS", S)
flow += spec_table("Ventilation & Exhaust", [
    ("Whole-house ventilation system", C("ERV", "HRV", "Exhaust", "N/A")),
    ("Kitchen range hood exhaust duct",
     [P("To exterior"), F("CFM:", height=20, font_size=9)]),
    ("Bathroom exhaust — Master",
     [P("To exterior"), F("CFM:", height=20, font_size=9)]),
    ("Bathroom exhaust — Bath #2",
     [P("To exterior"), F("CFM:", height=20, font_size=9)]),
    ("Bathroom exhaust — Bath #3",
     [P("To exterior"), F("CFM:", height=20, font_size=9)]),
    ("Laundry room exhaust (if req.)", "To exterior"),
    ("Dryer vent duct", "4\" rigid to exterior"),
    ("Dryer vent length within limits", "Max length per code"),
    ("All exhaust ducts terminate outside", "Not into attic/crawlspace"),
    ("Exhaust vent terminations have caps", "Pest/weather protection"),
], item_header="Item / Location")

flow += spec_table("Air Quality & Filtration", [
    ("Filter location/access planned", ""),
    ([P("Filter size"),
      d.FillInRow([("W:", 0.34), ("H:", 0.33), ("D:", 0.33)],
                  font_size=9, height=20, gap=8)], ""),
    ("Upgraded filtration system (if applicable)",
     C("HEPA", "Electronic", "Media", "Standard")),
    ("UV light system (if applicable)", F("Location:", height=22,
                                          font_size=9)),
    ("Humidifier rough-in (if applicable)",
     C("Whole-house", "Bypass", "Steam")),
    ("Humidifier water line to equipment", "1/4\" line with shutoff"),
    ("Dehumidifier provisions (if applicable)", ""),
])
flow.append(d.WriteBox(1.2, label="General Notes"))

# ---------------- INSPECTION
flow += section("INSPECTION RESULTS & CORRECTIONS", S)

flow.append(Paragraph("Initial HVAC Rough-In Inspection", S["h3"]))
flow.append(d.FillInRow([("Inspection Date:", 0.5), ("Time:", 0.5)]))
flow.append(d.FillInRow([("Inspector Name:", 0.6),
                         ("Inspector Badge/ID:", 0.4)]))
flow.append(d.checkbox_choice_row(
    "RESULT:", ["PASSED", "FAILED — Corrections Required"], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.3, label="Deficiencies / Code Violations Found"))

flow.append(Paragraph("Corrections Made", S["h3"]))
flow.append(d.FillInRow([("Date Corrections Completed:", 1.0)]))
flow.append(d.FillInRow([("HVAC Contractor:", 0.65), ("License #:", 0.35)]))
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
    ("HVAC Contractor Signature", True),
    ("Inspector Signature", True),
])
flow.append(d.FillInRow([("Permit Number:", 1.0)]))
flow.append(d.checkbox_choice_row("FINAL APPROVAL:", ["YES"], S))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-3-rough-in-phase",
                       "3.4-hvac-rough-in-guide.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
