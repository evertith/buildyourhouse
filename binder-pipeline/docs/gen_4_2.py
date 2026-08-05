#!/usr/bin/env python3
"""4.2 Plumbing System Completion Log — rebuilt on the 2026 design system."""

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
FORM_ID = "4.2"
FORM_TITLE = "Plumbing System Completion Log"

STATUS_COLS = [2.60 * inch, 2.30 * inch, CW - 4.90 * inch]


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


def status_table(title, items, item_header="Item", cols=None):
    cols = cols or STATUS_COLS
    rows = [[P(name), status, ""] for name, status in items]
    return [d.titled_table(title, head([item_header, "Status", "Notes"]),
                           rows, cols, S,
                           row_heights=measured_heights(rows, cols)),
            Spacer(1, 8)]



def section(title, styles=None, min_space=3.4):
    """An h2 that will not strand itself at the foot of a page: it reserves
    room for the heading plus the opening rows of whatever follows."""
    return [CondPageBreak(min_space * inch)] + d.h2(title, S)


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Installation and testing of every plumbing fixture and system — "
            "verified leak-free and functioning before final inspection.")

flow.append(d.FillInRow([("Project Address:", 1.0)]))
flow.append(d.FillInRow([("Project Name:", 0.6), ("Permit Number:", 0.4)]))
flow.append(d.FillInRow([("Plumber / Company:", 0.62),
                         ("License Number:", 0.38)]))
flow.append(d.FillInRow([("Contact Phone:", 1.0)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>PURPOSE:</b> This log documents the installation and testing of all "
    "plumbing fixtures and systems. Use it to verify every fixture is "
    "properly installed, leak-free and functioning correctly before final "
    "inspection.", S["body"]))
flow.append(Spacer(1, 4))

# ---------------- INSTALLATION STANDARDS
flow += section("FIXTURE INSTALLATION STANDARDS", S)
flow.append(Paragraph("Each fixture must meet these installation "
                      "requirements:", S["body"]))
flow.append(d.items_checklist([
    "Fixture installed level and plumb (check with level)",
    "All supply line connections tight — no leaks under pressure",
    "All drain connections sealed — no leaks during drain test",
    "Fixture operates correctly — no drips, proper flow",
    "Shut-off valves installed and operational",
    "Shut-off valves accessible (not behind permanently fixed items)",
    "Aerators installed and clean (no debris from construction)",
    "P-traps properly installed and vented",
    "All fixtures properly secured to backing/blocking",
    "All mounting hardware tight and secure",
    "Caulking/sealing complete where fixture meets wall/floor",
    "Manufacturer's installation instructions followed",
], S))

# ---------------- KITCHEN
flow += section("KITCHEN PLUMBING", S)

flow.append(Paragraph("Kitchen Sink", S["h3"]))
flow.append(d.FillInRow([("Sink Make/Model:", 0.55),
                         ("Faucet Make/Model:", 0.45)]))
flow.append(d.FillInRow([("Installation Date:", 1.0)]))
flow.append(d.items_checklist([
    "Sink properly supported (clips or undermount hardware secure)",
    "Sink level and properly sealed to countertop",
    "Hot supply line to left side (standard)",
    "Cold supply line to right side (standard)",
    "Supply lines connected and tight — no leaks",
    "Shut-off valves installed (hot and cold)",
    "Shut-off valves operate properly",
    "Faucet installed per manufacturer instructions",
    "Faucet operates smoothly — both hot and cold",
    "Spray hose operates properly (if equipped)",
    "Aerator installed and clean",
    "P-trap properly installed",
    "Drain connections tight — no leaks",
    "Drain stopper operates properly",
    "Water pressure adequate",
    "Hot water delivery time acceptable",
], S))

flow.append(Paragraph("Dishwasher", S["h3"]))
flow.append(d.FillInRow([("Dishwasher Make/Model:", 1.0)]))
flow.append(d.items_checklist([
    "Water supply line connected (typically 3/8\" or 1/2\")",
    "Supply line shut-off valve installed and accessible",
    "Drain line connected to disposal or drain",
    "High loop installed on drain line (or air gap)",
    "Dishwasher secured to countertop/cabinets",
    "Dishwasher level front-to-back and side-to-side",
    "Door opens and closes properly",
    "Test cycle run — fills properly",
    "Test cycle run — drains completely",
    "No leaks during test cycle",
    "Spray arms rotate freely",
], S))

flow.append(Paragraph("Garbage Disposal", S["h3"]))
flow.append(d.FillInRow([("Disposal Make/Model:", 1.0)]))
flow.append(d.items_checklist([
    "Disposal properly mounted to sink",
    "Discharge drain connected and sealed",
    "Dishwasher connection made (if applicable)",
    "Disposal operates properly",
    "No leaks at mounting flange",
    "No leaks at discharge connection",
    "Reset button accessible",
    "Allen wrench for jam clearing included",
], S))

flow.append(Paragraph("Ice Maker Line", S["h3"]))
flow += status_table("Supply & Material", [
    ("Ice maker supply line installed", C("Yes", "No", "N/A")),
    ("Supply line material", C("Copper", "PEX", "Braided stainless")),
])
flow.append(d.items_checklist([
    "Shut-off valve installed and accessible",
    "Supply line properly secured",
    "Connection to refrigerator made",
    "No leaks at connections",
    "Ice maker produces ice (if refrigerator installed)",
], S))

flow += status_table("Other Kitchen Fixtures", [
    ("Pot filler faucet", C("Installed", "N/A")),
    ("Water filtration system", C("Installed", "N/A")),
    ("Instant hot water dispenser", C("Installed", "N/A")),
    ("Bar sink", C("Installed", "N/A")),
])

# ---------------- BATHROOMS
flow += section("BATHROOM PLUMBING — FIXTURE LOG", S)

flow.append(Paragraph("Bathroom #1", S["h3"]))
flow.append(d.FillInRow([("Location / Name:", 1.0)]))
flow.append(d.checkbox_choice_row("TYPE:",
                                  ["Full", "3/4", "Half", "Master"], S))
flow.append(Spacer(1, 4))
flow.append(Paragraph("Sink / Vanity", S["body-bold"]))
flow.append(d.FillInRow([("Faucet Make/Model:", 1.0)]))
flow.append(d.items_checklist([
    "Sink/vanity installed and level",
    "Hot/cold supply connected — no leaks",
    "Shut-off valves installed and working",
    "Faucet operates properly",
    "Drain connected — no leaks",
    "Pop-up drain operates smoothly",
    "P-trap properly installed",
    "Adequate water pressure",
    "Hot water delivery time acceptable",
], S))

flow.append(Paragraph("Toilet", S["body-bold"]))
flow.append(d.FillInRow([("Toilet Make/Model:", 1.0)]))
flow.append(d.items_checklist([
    "Toilet properly set on flange",
    "Toilet level and secure",
    "Wax ring seal — no leaks at base",
    "Water supply connected — no leaks",
    "Shut-off valve installed and working",
    "Toilet flushes properly — complete flush",
    "Tank fills properly — stops at correct level",
    "No continuous running",
    "No leaks at tank-to-bowl connection",
    "Seat installed properly",
], S))

flow.append(Paragraph("Shower / Tub", S["body-bold"]))
flow.append(d.checkbox_choice_row(
    "TYPE:", ["Shower only", "Tub only", "Tub/shower combo", "N/A"], S))
flow.append(d.FillInRow([("Fixture Make/Model:", 1.0)]))
flow.append(d.items_checklist([
    "Valve installed properly — no leaks behind wall",
    "Shower head/tub spout installed",
    "Hot/cold operation correct (left hot, right cold)",
    "Water temperature appropriate (120°F max)",
    "Water pressure adequate",
    "Diverter operates properly (tub/shower)",
    "No leaks at shower head connection",
    "No leaks at tub spout",
    "Drain operates properly",
    "Tub stopper/trip lever works (if applicable)",
    "Shower door installed and seals properly (if applicable)",
    "No leaks during operation",
], S))

flow.append(Paragraph("Bathroom #2", S["h3"]))
flow.append(d.FillInRow([("Location / Name:", 1.0)]))
flow.append(d.checkbox_choice_row("TYPE:",
                                  ["Full", "3/4", "Half", "Master"], S))
flow.append(Spacer(1, 4))
flow.append(Paragraph("Sink / Vanity", S["body-bold"]))
flow.append(d.FillInRow([("Faucet Make/Model:", 1.0)]))
flow.append(d.items_checklist([
    "All installation checks complete (see Bathroom #1 checklist)",
    "No leaks — supply or drain",
    "Operates properly",
], S))
flow.append(Paragraph("Toilet", S["body-bold"]))
flow.append(d.FillInRow([("Toilet Make/Model:", 1.0)]))
flow.append(d.items_checklist([
    "All installation checks complete (see Bathroom #1 checklist)",
    "No leaks",
    "Flushes properly",
], S))
flow.append(Paragraph("Shower / Tub", S["body-bold"]))
flow.append(d.checkbox_choice_row(
    "TYPE:", ["Shower only", "Tub only", "Tub/shower combo", "N/A"], S))
flow.append(d.FillInRow([("Fixture Make/Model:", 1.0)]))
flow.append(d.items_checklist([
    "All installation checks complete (see Bathroom #1 checklist)",
    "No leaks",
    "Operates properly",
], S))

flow.append(Paragraph("Bathroom #3", S["h3"]))
flow.append(d.FillInRow([("Location / Name:", 1.0)]))
flow.append(d.checkbox_choice_row("TYPE:",
                                  ["Full", "3/4", "Half", "N/A"], S))
flow.append(Spacer(1, 4))
flow.append(d.items_checklist([
    "All fixtures installed per checklists above",
    "All fixtures tested — no leaks, proper operation",
], S))

flow.append(Paragraph("Bathroom #4", S["h3"]))
flow.append(d.FillInRow([("Location / Name:", 1.0)]))
flow.append(d.checkbox_choice_row("TYPE:",
                                  ["Full", "3/4", "Half", "N/A"], S))
flow.append(Spacer(1, 4))
flow.append(d.items_checklist([
    "All fixtures installed per checklists above",
    "All fixtures tested — no leaks, proper operation",
], S))

# ---------------- LAUNDRY
flow += section("LAUNDRY PLUMBING", S)
flow.append(d.items_checklist([
    "Washer box/outlet installed at proper height (typically 42–48\")",
    "Hot and cold supply valves installed",
    "Supply valves operate properly (quarter-turn or multi-turn)",
    "Supply valves accessible",
    "Drain standpipe installed (18–30\" high typical)",
    "P-trap installed on standpipe",
    "Washer hoses connected (if washer installed)",
    "No leaks at valve connections",
    "Washer test cycle run (if washer installed)",
    "Drain handles washer discharge without overflow",
    "Laundry sink installed (if applicable)",
    "Laundry sink faucet operates properly (if applicable)",
], S))
flow += status_table("Dryer Gas Supply", [
    ("Gas line for dryer (if applicable)", C("Installed", "N/A")),
])

# ---------------- WATER HEATER
flow += section("WATER HEATER INSTALLATION", S)
flow.append(d.FillInRow([("Make/Model:", 0.6), ("Capacity:", 0.4)]))
flow.append(d.FillInRow([("Location:", 0.6), ("Installation Date:", 0.4)]))
flow.append(d.checkbox_choice_row(
    "TYPE:", ["Electric", "Gas", "Tankless", "Heat Pump"], S))
flow.append(Spacer(1, 4))
flow.append(d.items_checklist([
    "Water heater properly supported/secured",
    "Water heater level (tank type)",
    "Cold water inlet connected properly",
    "Hot water outlet connected properly",
    "Shut-off valve on cold water inlet",
    "TPR (temperature/pressure relief) valve installed",
    "TPR discharge pipe installed — terminates 6\" above floor or outside",
    "TPR discharge pipe proper material (copper or CPVC)",
    "Drain valve accessible",
    "Gas line connected properly (if gas) — no leaks",
    "Gas shut-off valve within 6 feet (if gas)",
    "Vent pipe properly installed (if gas)",
    "Vent pipe terminates properly outside",
    "Electrical connection made (if electric)",
    "Electrical disconnect accessible (if electric)",
    "Pan installed under heater (if in living space or attic)",
    "Pan drain line runs to exterior or floor drain",
    "Earthquake straps installed (if required by code)",
    "Expansion tank installed (if required)",
    "Water heater producing hot water",
    "Temperature set to 120°F or lower",
    "No leaks at any connections",
    "Manufacturer's instructions left with homeowner",
    "Warranty information recorded",
], S))

# ---------------- EXTERIOR
flow += section("EXTERIOR PLUMBING", S)
flow += log_table(
    "Hose Bibs (Exterior Faucets)",
    ["Location", "Type", "Frost-Free", "Operates OK", "No Leaks",
     "Shut-off Valve", "Notes"],
    [1.30 * inch, 0.88 * inch, 0.92 * inch, 0.85 * inch, 0.75 * inch,
     0.90 * inch, CW - 5.60 * inch],
    6, marks={2: "box", 3: "box", 4: "box", 5: "box"})
flow.append(d.items_checklist([
    "All hose bibs freeze-proof type (if required by climate)",
    "All hose bibs properly secured to structure",
    "All hose bibs slope down when off (for drainage)",
    "Interior shut-off valves accessible for winter shutdown",
], S))
flow += status_table("Exterior Shower", [
    ("Exterior shower (if applicable)", C("Installed", "Tested", "N/A")),
])

# ---------------- SYSTEM TESTING
flow += section("COMPLETE SYSTEM TESTING", S)

flow.append(Paragraph("Pressure Test", S["h3"]))
flow.append(d.FillInRow([("Test Date:", 0.5),
                         ("Static Pressure (PSI):", 0.5)]))
flow.append(d.FillInRow([("Test Duration:", 0.5), ("Pressure Loss:", 0.5)]))
flow.append(Spacer(1, 4))
flow.append(d.items_checklist([
    "All fixtures and supply lines pressurized",
    "System pressure 40–60 PSI (typical residential)",
    "Pressure held steady for minimum 15 minutes",
    "No visible leaks at any connection",
    "No drop in pressure during test",
    "Pressure regulator functioning (if installed)",
], S))

flow.append(Paragraph("Drain Flow Test", S["h3"]))
flow.append(d.items_checklist([
    "All drains flow freely — no slow drainage",
    "No gurgling sounds from drains",
    "All P-traps holding water (no dry traps)",
    "No sewer gas odors",
    "All vents functioning properly",
    "Multiple fixtures run simultaneously — drains handle load",
    "No leaks at drain connections under use",
], S))

flow.append(Paragraph("Hot Water Performance", S["h3"]))
flow.append(d.FillInRow([("Furthest Fixture from Water Heater:", 1.0)]))
flow.append(d.FillInRow([("Hot Water Delivery Time (min):", 0.5),
                         ("Temperature at Tap (°F):", 0.5)]))
flow.append(Spacer(1, 4))
flow.append(d.items_checklist([
    "Hot water delivery time acceptable (typically under 2 minutes)",
    "Water temperature 120°F or lower (scalding prevention)",
    "Consistent temperature at all fixtures",
    "Adequate hot water volume for household needs",
], S))

# ---------------- SPECIAL SYSTEMS
flow += section("SPECIAL SYSTEMS (if applicable)", S)

flow.append(Paragraph("Well System", S["h3"]))
flow.append(d.checkbox_choice_row("WELL INSTALLED:", ["Yes", "No", "N/A"], S))
flow.append(d.FillInRow([("Well Depth (ft):", 0.5), ("Pump HP:", 0.5)]))
flow.append(d.checkbox_choice_row("PUMP TYPE:",
                                  ["Submersible", "Jet", "Other"], S))
flow.append(d.FillInRow([("If other, specify:", 1.0)]))
flow.append(d.FillInRow([("Pressure Tank Size (gal):", 1.0)]))
flow.append(d.FillInRow([("Cut-In Pressure (PSI):", 0.5),
                         ("Cut-Out Pressure (PSI):", 0.5)]))
flow.append(Spacer(1, 4))
flow.append(d.items_checklist([
    "Pump operates properly",
    "Pressure tank properly charged",
    "Pressure switch functioning correctly",
    "Well cap sealed properly",
    "Water quality test completed",
    "Adequate flow rate for household needs",
], S))

flow.append(Paragraph("Septic System", S["h3"]))
flow.append(d.checkbox_choice_row("SEPTIC SYSTEM INSTALLED:",
                                  ["Yes", "No", "N/A"], S))
flow.append(d.FillInRow([("Tank Size (gal):", 0.5),
                         ("Drain Field Type:", 0.5)]))
flow.append(d.checkbox_choice_row("TANK TYPE:",
                                  ["Concrete", "Plastic", "Fiberglass"], S))
flow.append(d.FillInRow([("Installation Date:", 0.5),
                         ("Inspection Date:", 0.5)]))
flow.append(d.checkbox_choice_row("INSPECTION RESULT:",
                                  ["Passed", "Failed"], S))

# ---------------- FINAL INSPECTION
flow += section("FINAL PLUMBING INSPECTION", S)
flow.append(d.FillInRow([("Inspection Requested Date:", 0.5),
                         ("Inspection Scheduled Date:", 0.5)]))
flow.append(d.FillInRow([("Inspector Name:", 1.0)]))
flow.append(d.FillInRow([("Inspection Date:", 0.5),
                         ("Inspection Time:", 0.5)]))
flow.append(Spacer(1, 4))
flow.append(Paragraph("Pre-Inspection Checklist", S["h3"]))
flow.append(d.items_checklist([
    "All fixtures installed and tested",
    "No leaks anywhere in system",
    "All drains flowing properly",
    "Water pressure adequate throughout",
    "Hot water system functioning",
    "All shut-off valves accessible",
    "Access panels installed where required",
    "Clean-outs accessible",
    "All work completed per approved plans",
], S))
flow.append(Spacer(1, 4))
flow.append(d.checkbox_choice_row(
    "INSPECTION RESULT:",
    ["PASSED — Certificate Issued", "FAILED — Corrections Required"], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.2, label="Required Corrections"))
flow.append(Spacer(1, 6))
flow.append(d.FillInRow([("Corrections Completed Date:", 0.5),
                         ("Re-Inspection Date:", 0.5)]))
flow.append(d.checkbox_choice_row("RE-INSPECTION RESULT:",
                                  ["PASSED", "FAILED"], S))

flow.append(Paragraph("Sign-Off", S["h3"]))
flow += d.signature_block([
    ("Plumber Signature", True),
    ("Owner/Builder Signature", True),
])


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-4-systems-installation",
                       "4.2-plumbing-system-completion-log.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, "Plumbing Completion Log", SECTION, flow)  # short footer title; page title stays full
    print(f"built {out}")
