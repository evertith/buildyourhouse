#!/usr/bin/env python3
"""4.1 Electrical System Completion Log — rebuilt on the 2026 design system."""

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
FORM_ID = "4.1"
FORM_TITLE = "Electrical System Completion Log"


class ChoiceCell(Flowable):
    """Mutually-exclusive options as drawn boxes, wrapping to fit a table cell.

    Replaces the ☐ glyph runs the old build used inside test-log columns.
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


def head(labels):
    return [Paragraph(t, S["cell-bold"]) for t in labels]


def log_table(title, labels, cols, count, marks=None, first_col=None):
    """A test/verification log: blank write-in cells except the columns named
    in `marks` ({index: 'box' | (opt, opt, ...)}). first_col supplies fixed
    row labels (e.g. circuit numbers) instead of a blank cell."""
    marks = marks or {}
    rows = []
    for i in range(count):
        row = []
        for c in range(len(labels)):
            if first_col is not None and c == 0:
                row.append(Paragraph(first_col[i], S["cell-center"]))
            elif c in marks:
                mark = marks[c]
                row.append(CenterBox() if mark == "box" else C(*mark))
            else:
                row.append("")
        rows.append(row)
    return [d.titled_table(title, head(labels), rows, cols, S,
                           row_heights=measured_heights(rows, cols)),
            Spacer(1, 8)]


def status_table(title, items, cols, item_header="System"):
    header = head([item_header, "Status", "Notes"])
    rows = [[P(name), status, ""] for name, status in items]
    return [d.titled_table(title, header, rows, cols, S,
                           row_heights=measured_heights(rows, cols)),
            Spacer(1, 8)]



def section(title, styles=None, min_space=3.4):
    """An h2 that will not strand itself at the foot of a page: it reserves
    room for the heading plus the opening rows of whatever follows."""
    return [CondPageBreak(min_space * inch)] + d.h2(title, S)


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Completion and testing of the electrical system from rough-in "
            "through final inspection — every outlet, switch, fixture and "
            "circuit verified before the inspector arrives.")

flow.append(d.FillInRow([("Project Address:", 1.0)]))
flow.append(d.FillInRow([("Project Name:", 0.6), ("Permit Number:", 0.4)]))
flow.append(d.FillInRow([("Electrician / Company:", 0.62),
                         ("License Number:", 0.38)]))
flow.append(d.FillInRow([("Contact Phone:", 1.0)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>PURPOSE:</b> This log documents the completion and testing of all "
    "electrical systems from rough-in through final inspection. Use it to "
    "verify every outlet, switch, fixture and circuit is properly installed "
    "and functioning before final inspection.", S["body"]))
flow.append(Spacer(1, 4))

# ---------------- ROUGH-IN TO FINISH
flow += section("ROUGH-IN TO FINISH VERIFICATION", S)
flow.append(Paragraph("Review rough-in work and verify proper completion:",
                      S["body"]))
flow.append(d.items_checklist([
    "All electrical boxes properly located per plan",
    "All boxes properly secured to framing",
    "Box depth appropriate for wall finish thickness",
    "All boxes filled out flush with finished wall surface",
    "Vapor barrier properly sealed around boxes (if applicable)",
    "All required backing/blocking installed for fixtures",
    "All cables properly secured within 8\" of boxes",
    "Cable stapling meets code (every 4.5 feet, 12\" from boxes)",
    "Proper cable protection through studs (1-1/4\" from edge or nail plates)",
    "No damaged cable jackets or conductors",
    "All wire splices made in accessible boxes only",
    "All boxes have required cubic inch capacity for number of conductors",
], S))

# ---------------- DEVICE INSTALLATION
flow += section("DEVICE INSTALLATION VERIFICATION", S)
flow.append(d.items_checklist([
    "All receptacles installed with correct orientation "
    "(ground down or up per preference)",
    "All receptacles same color throughout (white or ivory — consistent)",
    "All receptacles properly secured to boxes (no gaps)",
    "All receptacles 15A or 20A as required by circuit",
    "Tamper-resistant receptacles installed per code (if required)",
    "GFCI receptacles installed in all required locations "
    "(bathrooms, kitchen, garage, exterior)",
    "AFCI breakers or receptacles installed per code requirements",
    "All switch devices properly installed and secured",
    "Switch heights consistent throughout (typically 48\" to center)",
    "Dimmer switches compatible with light fixtures/bulbs",
    "3-way and 4-way switches wired correctly",
    "All device cover plates installed (correct size and color)",
    "Weatherproof covers installed on all exterior receptacles",
    "Weatherproof covers installed on all exterior switches",
    "In-use covers provided for exterior GFCI receptacles",
], S))

# ---------------- OUTLET TESTING
flow += section("OUTLET TESTING LOG", S)
flow.append(Paragraph("Test and document each outlet/receptacle:", S["body"]))
flow += log_table(
    "Receptacle Test Record",
    ["Room / Location", "Outlet ID", "Polarity OK", "GFCI Test", "Notes"],
    [1.90 * inch, 1.00 * inch, 0.90 * inch, 0.90 * inch, CW - 4.70 * inch],
    30, marks={2: "box", 3: "box"})
flow.append(Paragraph(
    "<b>Testing notes:</b> Use an outlet tester for polarity. Press TEST on "
    "every GFCI outlet — it should trip. Press RESET to restore power.",
    S["body"]))

# ---------------- LIGHTING FIXTURES
flow += section("LIGHTING FIXTURES INSTALLATION", S)
flow += log_table(
    "Fixture Installation & Test Record",
    ["Room / Location", "Fixture Type", "Installed", "Bulb Type",
     "Dimmer Compatible", "Tested OK", "Notes"],
    [1.25 * inch, 1.10 * inch, 0.85 * inch, 0.95 * inch, 1.00 * inch,
     0.75 * inch, CW - 5.90 * inch],
    25, marks={2: "box", 4: ("Y", "N"), 5: "box"})

# ---------------- CEILING FANS
flow += section("CEILING FAN INSTALLATION & TESTING", S)
flow += log_table(
    "Ceiling Fan Record",
    ["Room / Location", "Fan Model", "Box Rated for Fan", "Light Kit",
     "Remote / Wall Control", "All Speeds Work", "No Wobble", "Notes"],
    [1.15 * inch, 1.00 * inch, 0.85 * inch, 0.65 * inch, 1.00 * inch,
     0.80 * inch, 0.75 * inch, CW - 6.20 * inch],
    8, marks={2: "box", 3: "box", 5: "box", 6: "box"})
flow.append(Paragraph("Fan Installation Checks", S["h3"]))
flow.append(d.items_checklist([
    "Ceiling box rated for fan weight (must be fan-rated box)",
    "Fan properly secured to fan-rated box or brace",
    "Downrod length appropriate for ceiling height",
    "All fan blades balanced and secure",
    "Light kit properly installed (if applicable)",
    "Wall control or remote functioning properly",
    "All fan speeds operate smoothly",
    "No wobble or unusual noise at any speed",
    "Reverse function works (summer/winter direction)",
], S))

# ---------------- SWITCH TESTING
flow += section("SWITCH OPERATION TESTING", S)
flow.append(Paragraph("Test every switch and verify correct fixture control:",
                      S["body"]))
flow += log_table(
    "Switch Test Record",
    ["Room / Location", "Switch Location", "Controls Which Fixture", "Type",
     "Works OK", "Notes"],
    [1.30 * inch, 1.30 * inch, 1.60 * inch, 0.70 * inch, 0.75 * inch,
     CW - 5.65 * inch],
    35, marks={4: "box"})
flow.append(Paragraph(
    "<b>Type codes:</b> S = single-pole · 3 = 3-way · 4 = 4-way · "
    "D = dimmer · P = pilot light · T = timer", S["body"]))

# ---------------- PANEL
flow += section("ELECTRICAL PANEL COMPLETION", S)
flow.append(d.FillInRow([("Panel Make/Model:", 0.6),
                         ("Main Breaker Size:", 0.4)]))
flow.append(d.FillInRow([("Panel Location:", 0.6),
                         ("Number of Circuits:", 0.4)]))
flow.append(Spacer(1, 6))
flow.append(Paragraph("Panel Completion Checklist", S["h3"]))
flow.append(d.items_checklist([
    "All circuit breakers properly installed and seated",
    "All breaker connections tight (proper torque per manufacturer)",
    "Main breaker correct size for service (typically 100A, 150A or 200A)",
    "All circuits properly labeled on breaker",
    "Panel directory card completely filled out and legible",
    "All GFCI breakers installed and functioning (test button works)",
    "All AFCI breakers installed per code requirements",
    "Combination AFCI/GFCI breakers where required",
    "No double-tapped breakers (unless breaker is rated for 2 wires)",
    "All unused breaker spaces filled with blank plates",
    "All knockouts sealed (no open holes in panel)",
    "Panel cover/dead front properly installed",
    "Panel cover screws all installed and tight",
    "Proper working clearance maintained (30\" wide x 36\" deep x 6'6\" high)",
    "Panel properly grounded (ground wire to ground bar)",
    "Neutral and ground bars properly separated (if required)",
    "Service entrance cable properly secured",
    "Panel labeled \"MAIN ELECTRICAL PANEL\" or \"MAIN DISCONNECT\"",
], S))

# ---------------- CIRCUIT DIRECTORY
flow += section("CIRCUIT DIRECTORY", S)
flow.append(Paragraph("Document all circuits for the panel directory:",
                      S["body"]))
flow += log_table(
    "Panel Directory",
    ["Breaker #", "Amperage", "Type", "Circuit Description / Serves",
     "GFCI", "AFCI"],
    [0.75 * inch, 0.92 * inch, 0.70 * inch, 2.95 * inch, 0.85 * inch,
     CW - 6.17 * inch],
    42, marks={4: "box", 5: "box"},
    first_col=[str(n) for n in range(1, 43)])
flow.append(Paragraph(
    "<b>Type codes:</b> SP = single-pole · DP = double-pole (240V)",
    S["body"]))

# ---------------- DETECTORS
flow += section("SMOKE & CO DETECTOR INSTALLATION", S)
flow += log_table(
    "Detector Record",
    ["Location", "Type", "Make / Model", "Inter-<br/>connected",
     "Battery Backup", "Tested OK", "Install Date"],
    [1.25 * inch, 0.78 * inch, 1.00 * inch, 1.12 * inch, 0.90 * inch,
     0.78 * inch, CW - 5.83 * inch],
    12, marks={3: "box", 4: "box", 5: "box"})
flow.append(Paragraph("Detector Requirements & Testing", S["h3"]))
flow.append(d.items_checklist([
    "Smoke detector in every bedroom",
    "Smoke detector outside each sleeping area",
    "Smoke detector on every level including basement",
    "All smoke detectors hard-wired with battery backup",
    "All smoke detectors interconnected (test one, all sound)",
    "Carbon monoxide detector on every level",
    "Carbon monoxide detector near sleeping areas",
    "CO detectors hard-wired with battery backup (or plug-in with battery)",
    "All detectors tested with test button — alarm sounds",
    "Interconnection tested — trigger one, all alarm",
    "Date of installation written on detector",
    "Manufacturer instructions left with homeowner",
], S))

# ---------------- SPECIAL SYSTEMS
flow += section("SPECIAL SYSTEMS & EQUIPMENT", S)

flow.append(Paragraph("Kitchen Appliances", S["h3"]))
flow.append(d.items_checklist([
    "Range/cooktop circuit — proper voltage (240V or 120V)",
    "Range receptacle matches appliance plug, or direct wire connection made",
    "Dishwasher circuit — dedicated 20A circuit",
    "Dishwasher receptacle or direct wire as required",
    "Disposal circuit — GFCI protected or on dedicated circuit",
    "Microwave circuit — dedicated 20A circuit (if built-in)",
    "Refrigerator circuit — dedicated 20A circuit",
    "All appliances tested and functioning",
], S))

flow.append(Paragraph("HVAC Equipment", S["h3"]))
flow.append(d.items_checklist([
    "Furnace/air handler circuit — correct amperage",
    "Disconnect switch installed within sight of equipment",
    "Condensing unit circuit — correct amperage (typically 30–60A)",
    "Condensing unit disconnect installed and accessible",
    "Thermostat wiring complete and functioning",
    "All HVAC equipment properly grounded",
], S))

flow.append(Paragraph("Water Heater", S["h3"]))
flow.append(d.items_checklist([
    "Water heater circuit — correct amperage (check data plate)",
    "Water heater properly wired (240V for electric)",
    "Disconnect or breaker lockout as required by code",
    "Water heater properly grounded",
], S))

flow.append(Paragraph("Laundry", S["h3"]))
flow.append(d.items_checklist([
    "Washer circuit — dedicated 20A circuit",
    "Dryer circuit — 240V 30A circuit (electric dryer)",
    "Dryer receptacle — NEMA 10-30R or 14-30R",
    "All laundry area outlets GFCI protected",
], S))

flow.append(Paragraph("Garage & Exterior", S["h3"]))
flow.append(d.items_checklist([
    "All garage receptacles GFCI protected",
    "Garage door opener circuit and receptacle",
    "Garage door opener functioning properly",
    "All exterior receptacles GFCI protected",
    "All exterior receptacles have weatherproof covers",
    "All exterior lighting installed and functioning",
    "Exterior lighting on photocell or timer (if specified)",
    "Landscape lighting transformer installed (if applicable)",
    "Service entrance lighting installed and functioning",
], S))

flow += status_table("Other Systems", [
    ("Doorbell / chime — working", C("Yes", "No")),
    ("Security system — installed", C("Yes", "No", "N/A")),
    ("Generator transfer switch", C("Yes", "No", "N/A")),
    ("Sump pump circuit", C("Yes", "No", "N/A")),
    ("Well pump circuit", C("Yes", "No", "N/A")),
    ("Septic pump circuit", C("Yes", "No", "N/A")),
    ("Attic / crawl space lights", C("Yes", "No", "N/A")),
], [2.60 * inch, 2.30 * inch, CW - 4.90 * inch])

# ---------------- FINAL TESTING
flow += section("FINAL ELECTRICAL TESTING", S)
flow.append(Paragraph("Complete this testing before requesting the final "
                      "inspection:", S["body"]))
flow.append(d.items_checklist([
    "ALL outlets tested with circuit tester — correct polarity, "
    "no open grounds",
    "ALL GFCI outlets tested — trip function works, reset function works",
    "ALL switches tested — operate correct fixtures",
    "ALL 3-way and 4-way switches tested from all locations",
    "ALL light fixtures tested — all bulbs working",
    "ALL dimmer switches tested — smooth dimming operation",
    "ALL ceiling fans tested — all speeds, reverse function, light kits",
    "ALL smoke detectors tested — alarm sounds",
    "ALL smoke detectors interconnection tested — all alarm together",
    "ALL carbon monoxide detectors tested — alarm sounds",
    "ALL appliance circuits tested with appliances operating",
    "ALL exterior outlets and lights tested",
    "Garage door opener tested",
    "Doorbell tested",
    "Panel directory verified — all circuits correctly labeled",
    "Main disconnect operation tested",
    "No flickering lights when major loads turn on",
    "No warm or hot outlets, switches or breakers under load",
    "No buzzing or humming from outlets, switches or panel",
], S))

# ---------------- FINAL INSPECTION
flow += section("FINAL ELECTRICAL INSPECTION", S)
flow.append(d.FillInRow([("Inspection Requested Date:", 0.5),
                         ("Inspection Scheduled Date:", 0.5)]))
flow.append(d.FillInRow([("Inspector Name:", 1.0)]))
flow.append(d.FillInRow([("Inspection Date:", 0.5),
                         ("Inspection Time:", 0.5)]))
flow.append(d.checkbox_choice_row(
    "INSPECTION RESULT:",
    ["PASSED — Certificate Issued", "FAILED — Corrections Required"], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.9, label="Required Corrections"))
flow.append(Spacer(1, 6))
flow.append(d.FillInRow([("Corrections Completed Date:", 0.5),
                         ("Re-Inspection Date:", 0.5)]))
flow.append(d.checkbox_choice_row("RE-INSPECTION RESULT:",
                                  ["PASSED", "FAILED"], S))

flow.append(Paragraph(
    "Certificate of Occupancy / Electrical Certificate", S["h3"]))
flow.append(d.FillInRow([("Certificate Number:", 0.6), ("Date Issued:", 0.4)]))
flow.append(d.FillInRow([("Issued By:", 1.0)]))

flow.append(Paragraph("Sign-Off", S["h3"]))
flow += d.signature_block([
    ("Electrician Signature", True),
    ("Owner/Builder Signature", True),
])


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-4-systems-installation",
                       "4.1-electrical-system-completion-log.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, "Electrical Completion Log", SECTION, flow)  # short footer title; page title stays full
    print(f"built {out}")
