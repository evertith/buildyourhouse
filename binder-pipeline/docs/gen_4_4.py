#!/usr/bin/env python3
"""4.4 Final Systems Walkthrough — rebuilt on the 2026 design system."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import CondPageBreak, Flowable, Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 4: Systems Installation"
FORM_ID = "4.4"
FORM_TITLE = "Final Systems Walkthrough"


class ChoiceCell(Flowable):
    """Mutually-exclusive options as drawn boxes, wrapping to fit a table cell.

    Replaces the ☐ glyph runs the old build used inside test columns.
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


def log_table(title, labels, cols, count, marks=None, first_col=None,
              center_first=False):
    """A walkthrough test log: blank write-in cells except the columns named in
    `marks` ({index: 'box' | (opt, opt, ...)}). first_col supplies fixed row
    labels (fixture names, issue numbers) instead of a blank cell."""
    marks = marks or {}
    style = S["cell-center"] if center_first else S["cell"]
    rows = []
    for i in range(count):
        row = []
        for c in range(len(labels)):
            if first_col is not None and c == 0:
                text = first_col[i] if i < len(first_col) else ""
                row.append(Paragraph(text, style) if text else "")
            elif c in marks:
                mark = marks[c]
                row.append(CenterBox() if mark == "box" else C(*mark))
            else:
                row.append("")
        rows.append(row)
    return [d.titled_table(title, head(labels), rows, cols, S,
                           row_heights=measured_heights(rows, cols)),
            Spacer(1, 8)]



def section(title, styles=None, min_space=3.4):
    """An h2 that will not strand itself at the foot of a page: it reserves
    room for the heading plus the opening rows of whatever follows."""
    return [CondPageBreak(min_space * inch)] + d.h2(title, S)


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="The final quality check before inspection and move-in — every "
            "light, outlet, fixture, register, door and window tested and "
            "recorded, with an issues log to drive corrections.")

flow.append(d.FillInRow([("Project Address:", 1.0)]))
flow.append(d.FillInRow([("Project Name:", 1.0)]))
flow.append(d.FillInRow([("Walkthrough Date:", 0.5), ("Conducted By:", 0.5)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>PURPOSE:</b> This walkthrough verifies that ALL systems are "
    "functioning properly before final inspection and move-in. Test every "
    "fixture, outlet, switch and system. This is your final quality check.",
    S["body"]))
flow.append(Paragraph(
    "<b>INSTRUCTIONS:</b> Go through every room systematically. Check every "
    "box as you test. Record any issue in the Notes column and carry it to "
    "the Issues Identified log for correction. Do not skip anything — test "
    "everything.", S["body"]))
flow.append(Spacer(1, 4))

# ---------------- ELECTRICAL
flow += section("ELECTRICAL SYSTEMS WALKTHROUGH", S)

flow.append(Paragraph(
    "Turn on EVERY light switch in the house and verify operation:",
    S["body"]))
flow += log_table(
    "Complete Lighting Test",
    ["Room / Location", "Switch Tested", "Light Works", "Bulbs OK",
     "3-Way Works", "Dimmer OK", "Notes"],
    [1.40 * inch, 0.75 * inch, 0.78 * inch, 0.72 * inch, 1.05 * inch,
     1.00 * inch, CW - 5.70 * inch],
    30, marks={1: "box", 2: "box", 3: "box", 4: ("OK", "N/A"),
               5: ("OK", "N/A")})

flow.append(Paragraph("Test EVERY outlet with a circuit tester:", S["body"]))
flow += log_table(
    "Complete Outlet Test",
    ["Room / Location", "Outlet Tested", "Polarity OK", "GFCI Trips",
     "GFCI Resets", "Notes"],
    [1.60 * inch, 0.78 * inch, 0.85 * inch, 1.05 * inch, 1.10 * inch,
     CW - 5.38 * inch],
    35, marks={1: "box", 2: "box", 3: ("OK", "N/A"), 4: ("OK", "N/A")})

flow.append(Paragraph("Safety Device Testing", S["h3"]))
flow.append(d.items_checklist([
    "All smoke detectors tested — alarm sounds",
    "All smoke detectors interconnected — test one, all alarm",
    "All carbon monoxide detectors tested — alarm sounds",
    "All GFCI outlets tested — trip function works",
    "All GFCI outlets reset properly",
    "AFCI breakers tested — function properly",
], S))

flow.append(Paragraph("Exterior Electrical", S["h3"]))
flow.append(d.items_checklist([
    "All exterior lights tested and working",
    "All exterior outlets tested — GFCI protected",
    "Garage door opener operates properly",
    "Garage lights work",
    "Doorbell works (front and back if applicable)",
    "Landscape lighting tested (if installed)",
], S))

# ---------------- PLUMBING
flow += section("PLUMBING SYSTEMS WALKTHROUGH", S)

flow.append(Paragraph("Test hot AND cold water at every fixture:", S["body"]))
flow += log_table(
    "Run Every Faucet",
    ["Location / Fixture", "Cold Runs", "Hot Runs", "Pressure OK",
     "No Leaks", "Drains OK", "Notes"],
    [1.55 * inch, 0.72 * inch, 0.72 * inch, 0.85 * inch, 0.75 * inch,
     0.78 * inch, CW - 5.37 * inch],
    22, marks={1: "box", 2: "box", 3: "box", 4: "box", 5: "box"},
    first_col=[
        "Kitchen Sink", "Kitchen Sink Spray", "Master Bath Sink 1",
        "Master Bath Sink 2", "Master Shower", "Master Tub",
        "Bath 2 Sink", "Bath 2 Shower/Tub", "Bath 3 Sink",
        "Bath 3 Shower/Tub", "Bath 4 Sink", "Powder Room Sink",
        "Laundry Sink", "Utility Sink", "Hose Bib — Front",
        "Hose Bib — Back", "Hose Bib — Side",
    ])

flow += log_table(
    "Flush Every Toilet",
    ["Location", "Flushes Properly", "Fills Properly", "Stops Filling",
     "No Leaks", "No Running", "Notes"],
    [1.45 * inch, 0.90 * inch, 0.85 * inch, 0.85 * inch, 0.75 * inch,
     0.85 * inch, CW - 5.65 * inch],
    6, marks={1: "box", 2: "box", 3: "box", 4: "box", 5: "box"})

flow.append(Paragraph("Appliance Testing", S["h3"]))
flow.append(d.items_checklist([
    "Dishwasher — run complete cycle, fills properly",
    "Dishwasher — drains completely, no leaks",
    "Garbage disposal — operates properly, no leaks",
    "Washing machine — fills properly (if installed)",
    "Washing machine — drains properly (if installed)",
    "Ice maker — produces ice (if installed)",
    "Water heater — producing hot water consistently",
], S))

flow.append(Paragraph("Leak Check", S["h3"]))
flow.append(d.items_checklist([
    "Check under all sinks — no leaks",
    "Check around all toilets — no water at base",
    "Check all shut-off valve connections — no drips",
    "Check water heater connections — no leaks",
    "Check around tub/shower surrounds — no water damage",
    "Check ceilings below bathrooms — no water stains",
    "Check basement/crawl space — no pipe leaks",
], S))

# ---------------- HVAC
flow += section("HVAC SYSTEMS WALKTHROUGH", S)

flow.append(Paragraph("Extended Heating Test (30 minutes minimum)", S["h3"]))
flow.append(d.FillInRow([("Test Start Time:", 0.5),
                         ("Start Temperature:", 0.5)]))
flow.append(d.FillInRow([("Target Temperature:", 0.5), ("Test End Time:", 0.5)]))
flow.append(d.FillInRow([("End Temperature:", 1.0)]))
flow.append(Spacer(1, 4))
flow.append(d.items_checklist([
    "System starts when thermostat calls for heat",
    "Warm air from all registers within 5 minutes",
    "System runs continuously without cycling off",
    "Temperature rises steadily",
    "All rooms getting warm air",
    "No cold spots in house",
    "System reaches setpoint and cycles off properly",
    "No unusual noises during operation",
    "No burning smell",
    "Blower operates smoothly",
], S))

flow.append(Paragraph("Extended Cooling Test (30 minutes minimum)", S["h3"]))
flow.append(d.FillInRow([("Test Start Time:", 0.5),
                         ("Start Temperature:", 0.5)]))
flow.append(d.FillInRow([("Target Temperature:", 0.5), ("Test End Time:", 0.5)]))
flow.append(d.FillInRow([("End Temperature:", 1.0)]))
flow.append(Spacer(1, 4))
flow.append(d.items_checklist([
    "System starts when thermostat calls for cooling",
    "Outdoor unit running (compressor and fan)",
    "Cool air from all registers within 5 minutes",
    "System runs continuously without short-cycling",
    "Temperature drops steadily",
    "All rooms getting cool air",
    "No warm spots in house",
    "Condensate draining properly (check drain)",
    "System reaches setpoint and cycles off properly",
    "No unusual noises from indoor or outdoor unit",
], S))

flow += log_table(
    "Airflow Check — Every Register",
    ["Room", "Airflow Adequate", "Register Secure", "Notes"],
    [2.00 * inch, 1.25 * inch, 1.25 * inch, CW - 4.50 * inch],
    20, marks={1: "box", 2: "box"})

flow.append(Paragraph("Thermostat Function", S["h3"]))
flow.append(d.items_checklist([
    "Thermostat displays correctly",
    "Heat mode functions",
    "Cool mode functions",
    "Fan AUTO mode works",
    "Fan ON mode works",
    "Temperature displayed accurately",
    "Program operates correctly (if programmable)",
    "WiFi connected (if smart thermostat)",
], S))

# ---------------- DOORS & WINDOWS
flow += section("DOORS AND WINDOWS WALKTHROUGH", S)

flow += log_table(
    "Test Every Door",
    ["Door Location", "Opens / Closes", "Latches", "Lock Works",
     "No Sticking", "Weatherstrip OK", "Notes"],
    [1.30 * inch, 0.85 * inch, 0.80 * inch, 0.85 * inch, 0.85 * inch,
     1.18 * inch, CW - 5.83 * inch],
    20, marks={1: "box", 2: "box", 3: "box", 4: "box", 5: "box"})

flow += log_table(
    "Test Every Window",
    ["Window Location", "Opens / Closes", "Locks", "Screen OK", "No Damage",
     "Weatherstrip OK", "Notes"],
    [1.30 * inch, 0.85 * inch, 0.70 * inch, 0.85 * inch, 0.95 * inch,
     1.18 * inch, CW - 5.83 * inch],
    20, marks={1: "box", 2: "box", 3: "box", 4: "box", 5: "box"})

# ---------------- FINAL CHECKS
flow += section("FINAL SYSTEM CHECKS", S)

flow.append(Paragraph("Safety Systems", S["h3"]))
flow.append(d.items_checklist([
    "All smoke detectors working and interconnected",
    "All CO detectors working",
    "All GFCI outlets working",
    "Fire extinguisher locations identified",
    "Main electrical panel labeled completely",
    "Main water shut-off accessible and labeled",
    "Main gas shut-off accessible and labeled (if gas)",
    "Emergency phone numbers posted",
], S))

flow.append(Paragraph("Garage", S["h3"]))
flow.append(d.items_checklist([
    "Garage door opener works — remote and wall button",
    "Garage door safety sensors working (obstruction test)",
    "Garage door opens and closes smoothly",
    "Garage door emergency release works",
    "Garage lights work",
    "Garage outlets work (GFCI protected)",
    "Garage service door works and locks",
], S))

flow.append(Paragraph("Miscellaneous", S["h3"]))
flow.append(d.items_checklist([
    "Doorbell works (all locations)",
    "Attic access operable",
    "Crawl space access operable (if applicable)",
    "Sump pump operates (if applicable)",
    "Well pump operates (if applicable)",
    "Septic alarm tested (if applicable)",
    "Security system tested (if applicable)",
    "Intercom system tested (if applicable)",
], S))

# ---------------- ISSUES
flow += section("ISSUES IDENTIFIED", S)
flow.append(Paragraph(
    "List every issue found during the walkthrough for immediate correction:",
    S["body"]))
flow += log_table(
    "Issues & Corrections Log",
    ["#", "System", "Location", "Issue Description", "Corrected",
     "Date Fixed"],
    [0.42 * inch, 1.00 * inch, 1.30 * inch, 2.50 * inch, 0.90 * inch,
     CW - 6.12 * inch],
    25, marks={4: "box"},
    first_col=[str(n) for n in range(1, 26)], center_first=True)

# ---------------- COMPLETION
flow += section("WALKTHROUGH COMPLETION", S)
flow.append(Paragraph("Walkthrough Summary", S["h3"]))
flow.append(d.FillInRow([("Total Items Checked:", 0.5),
                         ("Issues Found:", 0.5)]))
flow.append(d.FillInRow([("Issues Corrected:", 0.5),
                         ("Outstanding Issues:", 0.5)]))
flow.append(Spacer(1, 6))
flow.append(d.items_checklist([
    "All systems tested and functioning properly",
    "All identified issues corrected",
    "House ready for final inspection",
    "House ready for occupancy",
], S))
flow.append(Spacer(1, 6))
flow.append(d.WriteBox(1.9, label="Notes / Comments"))

flow.append(Paragraph("Sign-Off", S["h3"]))
flow.append(d.FillInRow([("Conducted By (print name):", 1.0)]))
flow += d.signature_block([("Signature", True)])
flow.append(d.FillInRow([("Owner/Builder (print name):", 1.0)]))
flow += d.signature_block([("Signature", True)])


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-4-systems-installation",
                       "4.4-final-systems-walkthrough.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
