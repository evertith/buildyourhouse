#!/usr/bin/env python3
"""3.3 Plumbing Rough-In Log — rebuilt on the 2026 design system."""

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
FORM_ID = "3.3"
FORM_TITLE = "Plumbing Rough-In Log"

FIXTURE_COLS = [0.42 * inch, 2.20 * inch, 1.85 * inch, 1.05 * inch,
                CW - 5.52 * inch]
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


def fixture_table(title, items):
    """[box] Fixture/Location | Rough-In Height/Spec | Spacing | Notes."""
    header = ["",
              Paragraph("Fixture / Location", S["cell-bold"]),
              Paragraph("Rough-In Height / Spec", S["cell-bold"]),
              Paragraph("Spacing", S["cell-bold"]),
              Paragraph("Notes", S["cell-bold"])]
    rows = []
    for entry in items:
        fixture, spec = entry[0], entry[1]
        spacing = entry[2] if len(entry) > 2 else ""
        rows.append([d.Checkbox(), cell(fixture), cell(spec),
                     P(spacing) if spacing else "", ""])
    return [d.titled_table(title, header, rows, FIXTURE_COLS, S,
                           row_heights=measured_heights(rows, FIXTURE_COLS)),
            Spacer(1, 8)]


def spec_table(title, items, item_header="Item"):
    """[box] Item | Specification | Notes."""
    header = ["",
              Paragraph(item_header, S["cell-bold"]),
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
    purpose="Supply, DWV and fixture rough-in dimensions recorded room by "
            "room, with the pressure test record and inspection result.")

flow.append(d.FillInRow([("Property Address:", 1.0)]))
flow.append(d.FillInRow([("Permit Number:", 0.5), ("Inspection Date:", 0.5)]))
flow.append(d.FillInRow([("Inspector:", 0.5), ("Plumber:", 0.5)]))
flow.append(d.FillInRow([("License #:", 0.5), ("Phone:", 0.5)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>INSTRUCTIONS:</b> Record the actual rough-in height and spacing you "
    "measure — not the target — for every stub-out. Verify each dimension "
    "against the fixture you actually bought before the walls close; a "
    "toilet flange 1\" off is a demolition job later.", S["body"]))
flow.append(Spacer(1, 4))

# ---------------- WATER SUPPLY
flow += section("WATER SUPPLY SYSTEM", S)
flow += spec_table("Service, Distribution & Protection", [
    ("Main water service line size", "Typically 3/4\" or 1\""),
    ("Main shut-off valve accessible", F("Location:", height=22)),
    ("Water pressure regulator (if required)",
     C("Installed", "Not required")),
    ("Water meter/pit (municipal)", C("Installed", "Well system")),
    ("Main distribution lines sized correctly",
     "Per fixture unit calculation"),
    ("Hot water trunk line size", "Typically 3/4\""),
    ("Cold water trunk line size", "Typically 3/4\""),
    ("Branch lines sized per code", "1/2\" typical to fixtures"),
    ("Pipe material type", C("PEX", "Copper", "CPVC")),
    ("Pipes properly supported/strapped", "Per code spacing"),
    ("Pipes protected from freezing", "Exterior walls, crawlspace"),
    ("Nail plates over pipes in framing", "Where within 1.25\" of edge"),
])
flow.append(d.WriteBox(1.2, label="Water Supply System Notes"))

# ---------------- FIXTURE ROUGH-IN
flow += section("FIXTURE ROUGH-IN BY ROOM", S)

flow += fixture_table("Master Bathroom", [
    ("Toilet — cold supply stub", "6\"–8\" AFF, left side", "12\" from wall"),
    ("Toilet — drain rough-in", "Correct distance from wall",
     "12\" or 10\" per spec"),
    ("Toilet — vent connection", "Per code requirements", "Within 6' typical"),
    ("Vanity sink — hot supply", "21\" AFF typical", "4\" right of center"),
    ("Vanity sink — cold supply", "21\" AFF typical", "4\" left of center"),
    ("Vanity sink — drain rough-in", "16\" AFF typical", "Centered on sink"),
    ("Shower valve rough-in", "48\" AFF typical (adjust)",
     "Centered in shower"),
    ("Shower head stub-out", "78\"–80\" AFF", "Centered"),
    ("Shower drain location", "Proper slope to drain", "Per shower pan spec"),
    ("Handheld shower outlet (if appl.)", "Per preference"),
    ("Body spray outlets (if appl.)", "Per plan/preference"),
    ("Tub spout rough-in (if appl.)", "4\" above tub rim",
     "Centered or per plan"),
    ("Tub drain/overflow assembly", "Access panel required", "Per tub specs"),
    ("Tub/shower valve type", C("Single", "Thermo", "Press-bal")),
])
flow.append(d.WriteBox(1.2, label="Master Bathroom Notes"))
flow.append(Spacer(1, 8))

flow += fixture_table("Bathroom #2", [
    ("Toilet — cold supply stub", "6\"–8\" AFF, left side", "12\" from wall"),
    ("Toilet — drain rough-in", "Per toilet spec", "12\" or 10\""),
    ("Vanity sink — hot supply", "21\" AFF", "8\" centers"),
    ("Vanity sink — cold supply", "21\" AFF", "8\" centers"),
    ("Vanity sink — drain", "16\" AFF", "Centered"),
    ("Shower/tub valve", "48\" AFF typical", "Centered"),
    ("Shower head stub-out", "78\"–80\" AFF", "Centered"),
    ("Tub drain/overflow", "Per tub specifications", "Access provided"),
])

flow += fixture_table("Bathroom #3 (if applicable)", [
    ("Toilet — cold supply stub", "6\"–8\" AFF, left side", "12\" from wall"),
    ("Toilet — drain rough-in", "Per toilet spec", "12\" or 10\""),
    ("Vanity sink — hot supply", "21\" AFF", "8\" centers"),
    ("Vanity sink — cold supply", "21\" AFF", "8\" centers"),
    ("Vanity sink — drain", "16\" AFF", "Centered"),
    ("Shower valve", "48\" AFF typical", "Centered"),
    ("Shower head stub-out", "78\"–80\" AFF", "Centered"),
])

flow += fixture_table("Kitchen", [
    ("Kitchen sink — hot supply", "18\"–22\" AFF", "8\" centers typical"),
    ("Kitchen sink — cold supply", "18\"–22\" AFF", "8\" centers typical"),
    ("Kitchen sink — drain", "16\" AFF typical", "Centered on sink"),
    ("Kitchen sink — vent connection", "Per code requirements"),
    ("Dishwasher — hot supply", "12\" AFF, behind kickplate",
     "Near sink connection"),
    ("Dishwasher — drain connection", "High loop or air gap",
     "Connect to disposal/sink"),
    ("Dishwasher shut-off valve location", "Accessible under sink"),
    ("Garbage disposal — drain", "Connection to sink drain",
     "Per disposal specs"),
    ("Ice maker supply line", "To refrigerator location",
     "1/4\" copper or PEX"),
    ("Pot filler supply (if appl.)", "Height per range specs",
     "Hot water supply"),
    ("Instant hot water dispenser (if appl.)", "Supply and mounting"),
    ("Gas line for range/cooktop (if appl.)", "Proper size and shutoff",
     "Per appliance specs"),
])
flow.append(d.WriteBox(1.2, label="Kitchen Notes"))
flow.append(Spacer(1, 8))

flow += fixture_table("Laundry Room", [
    ("Washer — hot supply", "42\" AFF typical", "6\" apart"),
    ("Washer — cold supply", "42\" AFF typical", "6\" apart"),
    ("Washer — drain standpipe", "42\"–48\" AFF", "2\" diameter minimum"),
    ("Washer drain — P-trap installed", "Below floor/wall", "Accessible"),
    ("Washer drain — vent connection", "Per code requirements"),
    ("Washer box recessed (if appl.)", "Flush with finished wall",
     "Between studs"),
    ("Gas line for dryer (if appl.)", "Behind dryer location",
     "1/2\" line with shutoff"),
    ("Utility sink — hot supply", "18\" AFF", "8\" centers"),
    ("Utility sink — cold supply", "18\" AFF", "8\" centers"),
    ("Utility sink — drain", "16\" AFF", "Centered"),
    ("Floor drain (if required)", "Proper slope to drain", "Per code"),
])

flow += fixture_table("Powder Room / Half Bath", [
    ("Toilet — cold supply stub", "6\"–8\" AFF, left side", "12\" from wall"),
    ("Toilet — drain rough-in", "Per toilet spec", "12\" typical"),
    ("Sink — hot supply", "21\" AFF", "8\" centers"),
    ("Sink — cold supply", "21\" AFF", "8\" centers"),
    ("Sink — drain", "16\" AFF", "Centered"),
])

# ---------------- EXTERIOR
flow += section("EXTERIOR PLUMBING", S)
flow += spec_table("Hose Bibs, Condensate & Gas", [
    ("Front hose bib", C("Standard", "Frost-proof")),
    ("Back hose bib", C("Standard", "Frost-proof")),
    (FC("Side yard hose bib(s)"), C("Standard", "Frost-proof")),
    ("Hose bibs have shutoff valves inside", "Required for winterization"),
    ("Hose bibs slope down for drainage", "Prevent freezing"),
    ("HVAC condensate drain line", "3/4\" PVC typical"),
    ("Condensate drain terminates properly", "Away from foundation"),
    ("Gas meter location (if applicable)", "Accessible, proper clearances"),
    ("Gas line sizing adequate", "Per appliance load calculation"),
    ("Irrigation system connection (if appl.)", F("Location:", height=22)),
], item_header="Item / Location")

# ---------------- WATER HEATER
flow += section("WATER HEATER ROUGH-IN", S)
flow += spec_table("Supply, Relief & Combustion", [
    ("Cold water supply to heater", "3/4\" minimum"),
    ("Hot water outlet from heater", "3/4\" minimum"),
    ("Shut-off valve on cold supply", "Required"),
    ("TPR valve discharge pipe rough-in", "3/4\" to within 6\" of floor"),
    ("Drain pan drain (if required)", "To approved location"),
    ("Gas line for gas WH (if appl.)", "Proper size per BTU rating"),
    ("Combustion air provisions (gas)", "Per code requirements"),
    ("Water heater location accessible", "Service clearances maintained"),
    ("Expansion tank provision (if req.)", "On cold supply side"),
])

# ---------------- DWV
flow += section("DWV (DRAIN-WASTE-VENT) SYSTEM", S)
flow += spec_table("Drains, Stacks & Vents", [
    ("Main drain line size", "3\" or 4\" per code"),
    ("Main drain slope adequate", "1/4\" per foot minimum"),
    ("Main stack vent size", "3\" or 4\" to roof"),
    ("Stack vent extends through roof", "Flashed and sealed"),
    ("Branch drain sizes adequate", "Per fixture unit load"),
    ("Toilet drain line size", "3\" minimum"),
    ("Shower drain line size", "2\" minimum"),
    ("Sink drain line size", "1.5\" minimum"),
    ("Washing machine drain size", "2\" minimum"),
    ("All fixtures have proper trap", "P-traps correctly installed"),
    ("Traps accessible for service", "Not buried in concrete"),
    ("All fixtures properly vented", "Per code requirements"),
    ("Vent pipe sizing adequate", "1.5\" or 2\" typical"),
    ("Vent penetrations through roof flashed", "Watertight"),
    ("Vent terminals above roof surface", "6\" minimum, 12\" in snow areas"),
    ("AAVs (Air Admittance Valves) if used", C("Used", "Not used")),
    ("AAVs accessible if used", "Not sealed in walls"),
    ("Cleanout(s) installed", "Accessible locations"),
    ("Cleanout at base of stack", "Required"),
    ("Cleanout(s) at direction changes", "If required by code"),
])
flow += spec_table("Fittings, Support & Connection", [
    ("No improper fittings used in drains", "DWV fittings only"),
    ("All joints properly glued/assembled", "No dry fits"),
    ("All drain lines properly supported", "Per code spacing"),
    ("Pipe penetrations through framing adequate",
     "Not weakening structure"),
    ("Underground drains properly bedded", "Sand or approved material"),
    ("Connection to septic/sewer verified", "Proper slope and connection"),
])
flow.append(d.WriteBox(1.2, label="DWV System Notes"))

# ---------------- PRESSURE TEST
flow += section("PRESSURE TEST RECORD", S)
flow.append(Paragraph("Water Supply System Pressure Test", S["h3"]))
flow.append(d.FillInRow([("Test Date:", 0.5), ("Time:", 0.5)]))
flow.append(d.FillInRow([("Test Pressure (PSI):", 0.5),
                         ("Test Duration (hrs/min):", 0.5)]))
flow.append(d.checkbox_choice_row("TEST MEDIUM:", ["Water", "Air"], S))
flow.append(Spacer(1, 4))
flow.append(Paragraph("Test Results", S["body-bold"]))
flow.append(d.items_checklist([
    "PASSED — No leaks detected, pressure maintained",
    "FAILED — Leaks found (describe below)",
], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.3, label="Leak Locations (if any)"))
flow.append(Paragraph("Repairs Made", S["h3"]))
flow.append(d.FillInRow([("Date:", 0.5), ("Plumber:", 0.5)]))
flow.append(d.WriteBox(1.2, label="Description of Repairs"))
flow.append(Paragraph("Re-Test Results (if applicable)", S["h3"]))
flow.append(d.FillInRow([("Re-Test Date:", 0.5), ("PSI:", 0.5)]))
flow.append(d.checkbox_choice_row("RESULT:", ["PASSED", "FAILED"], S))

# ---------------- QUALITY
flow += section("GENERAL PLUMBING QUALITY CHECKS", S)
flow += check_table("Support, Protection & Access", [
    "All supply lines properly supported/strapped",
    "Strapping/support spacing per code",
    "No pipes in exterior walls (if possible)",
    "Pipes in exterior walls insulated/protected",
    "Pipes through penetrations protected",
    "Nail plates over pipes within 1.25\" of framing edge",
    "All penetrations will be fire-stopped",
    "Proper clearance from electrical",
    "All connections tight and secure",
    "Correct materials used throughout",
    "Transitions between materials proper",
    "Shower valves backing/blocking installed",
    "Tub/shower valve access provided",
    "Water hammer arrestors installed if needed",
    "Stub-outs capped/protected during construction",
    "Rough-in dimensions verified with fixtures",
    "All required shut-off valves planned",
])
flow.append(d.WriteBox(1.2, label="Additional Plumbing Notes"))

# ---------------- INSPECTION
flow += section("INSPECTION RESULTS & CORRECTIONS", S)

flow.append(Paragraph("Initial Plumbing Rough-In Inspection", S["h3"]))
flow.append(d.FillInRow([("Inspection Date:", 0.5), ("Time:", 0.5)]))
flow.append(d.FillInRow([("Inspector Name:", 0.6),
                         ("Inspector Badge/ID:", 0.4)]))
flow.append(d.checkbox_choice_row(
    "RESULT:", ["PASSED", "FAILED — Corrections Required"], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.3, label="Deficiencies / Code Violations Found"))

flow.append(Paragraph("Corrections Made", S["h3"]))
flow.append(d.FillInRow([("Date Corrections Completed:", 1.0)]))
flow.append(d.FillInRow([("Licensed Plumber:", 0.65), ("License #:", 0.35)]))
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
    ("Licensed Plumber Signature", True),
    ("Inspector Signature", True),
])
flow.append(d.FillInRow([("Permit Number:", 1.0)]))
flow.append(d.checkbox_choice_row("FINAL APPROVAL:", ["YES"], S))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-3-rough-in-phase",
                       "3.3-plumbing-rough-in-log.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
