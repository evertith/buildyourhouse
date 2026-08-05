#!/usr/bin/env python3
"""1.7 Excavation & Backfill Log — rebuilt on the 2026 design system."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Flowable, Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 1: Project Planning & Foundation"
FORM_ID = "1.7"
FORM_TITLE = "Excavation & Backfill Log"

CHOICE_BOX = 11
CHOICE_FS = 9


def choice_col(options, box=CHOICE_BOX, fs=CHOICE_FS):
    """Column width that guarantees a checkbox_choice_row fits on one line."""
    d.register_fonts()
    return sum(box + 5 + stringWidth(o, d.BODY, fs) + 18 for o in options) + 10


def choices(options, box=CHOICE_BOX, fs=CHOICE_FS):
    return d.checkbox_choice_row(None, options, S, box=box, font_size=fs)


class ChoiceBlock(Flowable):
    """Bold label + drawn checkbox options, wrapped onto as many lines as the
    width requires. design.checkbox_choice_row never wraps and, split into
    several flowables, would strand its label at a page foot — this is the same
    geometry (13pt drawn square, 22pt line pitch) in one atomic flowable."""

    def __init__(self, label, options, box=13, font_size=10.5, line_h=22):
        super().__init__()
        self.label = label
        self.options = options
        self.box = box
        self.fs = font_size
        self.line_h = line_h

    def _layout(self, avail):
        d.register_fonts()
        widths = [self.box + 5 + stringWidth(o, d.BODY, self.fs) + 18
                  for o in self.options]
        label_w = (stringWidth(self.label, d.BOLD, self.fs) + 14
                   if self.label else 0)
        if label_w + sum(widths) <= avail:
            return True, [list(zip(self.options, widths))]
        rows, row, used = [], [], 0.0
        for opt, w in zip(self.options, widths):
            if row and used + w > avail:
                rows.append(row)
                row, used = [], 0.0
            row.append((opt, w))
            used += w
        if row:
            rows.append(row)
        return False, rows

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self._inline, self._rows = self._layout(availWidth)
        lines = len(self._rows) + (0 if self._inline or not self.label else 1)
        self.height = lines * self.line_h
        return self.width, self.height

    def draw(self):
        d.register_fonts()
        c = self.canv
        c.setFillColor(d.INK)
        c.setStrokeColor(d.INK)
        y = self.height - self.line_h + 6
        x0 = 0
        if self.label:
            c.setFont(d.BOLD, self.fs)
            c.drawString(0, y, self.label)
            if self._inline:
                x0 = stringWidth(self.label, d.BOLD, self.fs) + 14
            else:
                y -= self.line_h
        c.setLineWidth(1)
        for row in self._rows:
            x = x0
            for opt, _w in row:
                c.rect(x, y - 3, self.box, self.box)
                x += self.box + 5
                c.setFont(d.BODY, self.fs)
                c.drawString(x, y, opt)
                x += stringWidth(opt, d.BODY, self.fs) + 18
            y -= self.line_h
            x0 = 0


def choice_block(label, options):
    return [ChoiceBlock(label, options)]


def heights_for(rows, widths, minimum=d.WRITE_ROW_PT, pad=10):
    out = []
    for row in rows:
        tallest = 0.0
        for cell, w in zip(row, widths):
            items = cell if isinstance(cell, list) else [cell]
            h = 0.0
            for it in items:
                if isinstance(it, Flowable):
                    h += it.wrap(w - 10, 10000)[1]
            tallest = max(tallest, h)
        out.append(max(minimum, tallest + pad))
    return out


def task_cell(item):
    if isinstance(item, str):
        return Paragraph(item, S["cell"])
    text, extras = item[0], item[1:]
    parts = [Paragraph(text, S["cell"])] if text else []
    for ex in extras:
        if ex and isinstance(ex[0], tuple):
            parts.append(d.FillInRow(ex, font_size=9.5, height=24))
        else:
            parts.append(choices(list(ex)))
    return parts


CHECK_COLS = [0.42 * inch, CW - 0.42 * inch - 1.0 * inch - 2.0 * inch,
              1.0 * inch, 2.0 * inch]


def check_table(title, task_header, items):
    header = ["", Paragraph(task_header, S["cell-bold"]),
              Paragraph("Date Completed", S["cell-bold"]),
              Paragraph("Notes", S["cell-bold"])]
    rows = [[d.Checkbox(), task_cell(it), "", ""] for it in items]
    return [d.titled_table(title, header, rows, CHECK_COLS, S,
                           row_heights=heights_for(rows, CHECK_COLS)),
            Spacer(1, 10)]


PF = ["Pass", "Fail"]
PF_W = choice_col(PF)

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="The permanent record of what came out of the hole and what went "
            "back in — depths, soil conditions, water, compaction, and final "
            "grade.")

flow.append(d.FillInRow([("Project Name:", 0.5),
                         ("Excavation Contractor:", 0.5)]))
flow.append(d.FillInRow([("Property Address:", 0.5), ("Contact Phone:", 0.5)]))
flow.append(d.FillInRow([("Owner-Builder:", 0.5), ("Equipment Used:", 0.5)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>PURPOSE:</b> This log documents all excavation and backfill activities "
    "for the foundation. Accurate records are essential for verifying code "
    "compliance, documenting soil conditions, and supporting warranty claims. "
    "Take photos at each stage.", S["body"]))
flow.append(Spacer(1, 8))

# ---------------- section 1
flow += d.h2("SECTION 1: PRE-EXCAVATION INFORMATION", S)
flow += check_table("Pre-Excavation Checklist", "Pre-Excavation Checklist", [
    ("811 utility locate completed", [("Ticket #:", 1.0)]),
    "All utility locations marked and photographed",
    "Building permit approved and posted on site",
    "Foundation layout staked and squared",
    "Erosion control measures in place",
    "Tree protection fencing installed (if applicable)",
])

# ---------------- section 2
flow += d.h2("SECTION 2: EXCAVATION WORK LOG", S)
flow.append(Paragraph("Excavation Schedule", S["h3"]))
flow.append(d.FillInRow([("Excavation start date:", 0.5), ("Start time:", 0.5)]))
flow.append(d.FillInRow([("Excavation completion date:", 0.55),
                         ("Completion time:", 0.45)]))
flow.append(d.FillInRow([("Total excavation duration:", 0.5),
                         ("Weather conditions:", 0.5)]))

flow.append(Paragraph("Excavation Depth Measurements", S["h3"]))
flow.append(d.FillIn("Required excavation depth per plan (inches below "
                     "finished grade):"))
flow.append(d.FillIn("Local frost depth requirement (inches):",
                     width=CW * 0.8))
flow.append(Spacer(1, 4))

dep_cols = [1.60 * inch, 0.95 * inch, 0.95 * inch, PF_W,
            CW - 1.60 * inch - 0.95 * inch - 0.95 * inch - PF_W]
dep_header = [Paragraph(t, S["cell-bold"]) for t in
              ("Measurement Location", "Required Depth (in)",
               "Actual Depth (in)", "Pass / Fail", "Notes")]
dep_locs = ["Northeast (NE) Corner", "Northwest (NW) Corner",
            "Southeast (SE) Corner", "Southwest (SW) Corner",
            "North Wall Midpoint", "South Wall Midpoint",
            "East Wall Midpoint", "West Wall Midpoint",
            "Center of Excavation"]
dep_rows = [[Paragraph(loc, S["cell"]), "", "", choices(PF), ""]
            for loc in dep_locs]
dep_rows.append([d.FillIn("Other:", font_size=9, height=22), "", "",
                 choices(PF), ""])
flow.append(d.titled_table("Excavation Depth Verification", dep_header,
                           dep_rows, dep_cols, S,
                           row_heights=heights_for(dep_rows, dep_cols)))

# ---------------- section 3
flow += d.h2("SECTION 3: SOIL CONDITIONS DOCUMENTATION", S)
flow.append(Paragraph("Soil Type &amp; Classification", S["h3"]))
flow += choice_block("Primary soil type:",
                     ["Clay", "Silt", "Sand", "Gravel", "Loam", "Mixed"])
flow.append(d.FillIn("Other (describe):"))
flow.append(d.FillIn("Soil color:"))
flow += choice_block("Soil moisture level:",
                     ["Dry", "Slightly moist", "Wet", "Saturated",
                      "Standing water"])
flow.append(d.FillIn("Soil bearing capacity (PSF, per geotechnical report or "
                     "code assumption):"))
flow += choice_block("Organic matter present:",
                     ["None", "Minimal", "Moderate",
                      "Significant (requires removal)"])
flow += choice_block("Frost-susceptible soil:", ["Yes", "No"])
flow.append(d.FillIn("Action taken:"))
flow.append(Spacer(1, 6))

rock_cols = [1.50 * inch, 0.90 * inch, 1.50 * inch, 1.60 * inch, 1.50 * inch]
rock_header = [Paragraph(t, S["cell-bold"]) for t in
               ("Location", "Depth Found (in)", "Type (rock, ledge, debris)",
                "Action Taken", "Notes")]
flow.append(d.titled_table("Rock, Ledge &amp; Obstacles Encountered",
                           rock_header, [["", "", "", "", ""] for _ in range(5)],
                           rock_cols, S))
flow.append(Spacer(1, 10))

flow.append(Paragraph("Water &amp; Drainage Issues", S["h3"]))
flow += choice_block("Standing water encountered:", ["Yes", "No"])
flow.append(d.FillIn("If yes — location:"))
flow += choice_block("Groundwater seepage:", ["Yes", "No"])
flow.append(d.FillIn("If yes — depth (inches):", width=CW * 0.7))
flow += choice_block("Flow rate:", ["Slow", "Moderate", "Fast"])
flow += choice_block("Dewatering required:", ["Yes", "No"])
flow += choice_block("Method:", ["Pump", "Sump", "Gravity drain"])
flow.append(d.FillIn("Other method:", width=CW * 0.7))
flow += choice_block("High water table noted:", ["Yes", "No"])
flow.append(d.FillIn("Depth from surface (feet):", width=CW * 0.7))
flow.append(Spacer(1, 6))
flow.append(d.WriteBox(1.1, label="Drainage Improvements Made"))
flow.append(Spacer(1, 10))

disp_a = ["Stockpiled", "Removed"]
disp_b = ["Removed", "Hauled away"]
disp_w = max(choice_col(disp_a), choice_col(disp_b))
disp_cols = [1.75 * inch, 1.00 * inch, disp_w,
             CW - 1.75 * inch - 1.00 * inch - disp_w]
disp_header = [Paragraph(t, S["cell-bold"]) for t in
               ("Material Type", "Est. Volume (cu. yds)", "Disposition",
                "Location / Notes")]
disp_rows = [
    [Paragraph("Topsoil (saved for landscaping)", S["cell"]), "",
     choices(disp_a), ""],
    [Paragraph("Subsoil (reusable for backfill)", S["cell"]), "",
     choices(disp_a), ""],
    [Paragraph("Rock/gravel", S["cell"]), "", choices(disp_a), ""],
    [Paragraph("Unsuitable material (organic, wet)", S["cell"]), "",
     choices(disp_b), ""],
]
flow.append(d.titled_table("Excavated Material Disposition", disp_header,
                           disp_rows, disp_cols, S,
                           row_heights=heights_for(disp_rows, disp_cols)))

# ---------------- section 4
flow += d.h2("SECTION 4: BACKFILL OPERATIONS LOG", S)
flow.append(Paragraph("Backfill Schedule", S["h3"]))
flow.append(d.FillInRow([("Backfill start date:", 0.5),
                         ("Days since concrete pour:", 0.5)]))
flow.append(d.FillInRow([("Backfill completion date:", 0.55),
                         ("Weather conditions:", 0.45)]))
flow += choice_block("Waterproofing cured:", ["Yes", "No", "N/A"])
flow += choice_block("Drainage tile installed:", ["Yes", "No", "N/A"])

flow.append(Paragraph("Backfill Material Specifications", S["h3"]))
flow += choice_block("Primary backfill material:",
                     ["Excavated soil", "Clean fill", "Sand", "Gravel",
                      "Crushed stone"])
flow.append(d.FillIn("Other:", width=CW * 0.7))
flow += choice_block("Material source:", ["On-site", "Imported"])
flow.append(d.FillIn("Supplier (if imported):"))
flow += choice_block("Material quality (check all that apply):",
                     ["Free of organic matter", "Free of large rocks (>3\")",
                      "Properly graded"])
flow += choice_block("Moisture content:",
                     ["Optimum for compaction", "Too wet", "Too dry"])
flow.append(d.FillIn("Action taken (if too wet or too dry):"))
flow.append(d.FillIn("Total backfill volume (cubic yards):", width=CW * 0.7))

flow.append(Paragraph("Compaction Method &amp; Testing", S["h3"]))
flow += choice_block("Compaction equipment used:",
                     ["Plate compactor", "Jumping jack", "Roller",
                      "Hand tamper"])
flow.append(d.FillIn("Other equipment:", width=CW * 0.7))
flow.append(d.FillInRow([("Lift thickness (in):", 0.5),
                         ("Passes per lift:", 0.5)]))
flow.append(d.FillInRow([("Total number of lifts:", 0.5),
                         ("Target compaction (%):", 0.5)]))
flow.append(Paragraph(
    "Typical values: lifts of 6–12 inches before compaction; target compaction "
    "90–95% of maximum dry density for backfill.", S["note"]))
flow += choice_block("Compaction testing performed:", ["Yes", "No"])
flow += choice_block("Test method:",
                     ["Nuclear density", "Proctor", "Visual"])
flow.append(d.FillIn("Other method:", width=CW * 0.7))
flow.append(Spacer(1, 6))

comp_cols = [1.40 * inch, 0.95 * inch, 1.15 * inch, PF_W,
             CW - 1.40 * inch - 0.95 * inch - 1.15 * inch - PF_W]
comp_header = [Paragraph(t, S["cell-bold"]) for t in
               ("Test Location", "Lift Depth (in)", "Compaction % Achieved",
                "Pass / Fail", "Notes / Actions")]
comp_rows = [[Paragraph(loc, S["cell"]), "", "", choices(PF), ""] for loc in (
    "NE Corner", "NW Corner", "SE Corner", "SW Corner",
    "North Wall", "South Wall", "East Wall", "West Wall")]
flow.append(d.titled_table("Compaction Test Results", comp_header, comp_rows,
                           comp_cols, S,
                           row_heights=heights_for(comp_rows, comp_cols)))

# ---------------- section 5
flow += d.h2("SECTION 5: FINAL GRADING &amp; DRAINAGE", S)
flow += check_table("Final Grading Checklist", "Final Grading Checklist", [
    "Backfill completed to within 6–8\" of final grade",
    "Grade slopes away from foundation (2% min, 6\" drop in 10 feet)",
    "No low spots or depressions where water can collect",
    "Swales or drainage paths direct water away from structure",
    "Perimeter drain outlet is clear and functional",
    "Final topsoil layer applied (if applicable)",
    "Erosion control measures in place until landscaping",
    "Grading verified after first significant rain event",
])

# ---------------- section 6
flow += d.h2("SECTION 6: PHOTO DOCUMENTATION", S)
flow.append(Paragraph(
    "Photographic evidence is critical for insurance claims, warranty issues, "
    "and inspection appeals. Take multiple photos from different angles at "
    "each stage.", S["body"]))
photo_cols = [1.0 * inch, 2.4 * inch, 1.7 * inch, 1.9 * inch]
photo_header = [Paragraph(t, S["cell-bold"]) for t in
                ("Date", "Photo Description", "File Name / Number", "Notes")]
photo_rows = [["", Paragraph(desc, S["cell"]), "", ""] for desc in (
    "Site before excavation begins",
    "Utility locate markings",
    "Foundation layout stakes/strings",
    "Excavation in progress",
    "Final excavation depth verification",
    "Soil conditions/layers exposed",
    "Rock or unusual conditions found",
    "Water/drainage issues encountered",
    "Foundation complete before backfill",
    "Waterproofing applied",
    "Drainage tile installation",
    "Backfill in progress (show lifts)",
    "Compaction equipment in use",
    "Final backfill completed",
    "Final grading and drainage")]
flow.append(d.titled_table("Photo Documentation Log", photo_header, photo_rows,
                           photo_cols, S,
                           row_heights=heights_for(photo_rows, photo_cols)))

# ---------------- section 7
flow += d.h2("SECTION 7: CONTRACTOR SIGN-OFF &amp; CERTIFICATION", S)
flow.append(Paragraph(
    "I certify that all excavation and backfill work has been completed in "
    "accordance with approved plans and industry best practices. All "
    "compaction meets or exceeds specified requirements.", S["body"]))
flow.append(Spacer(1, 8))
flow.append(Paragraph("Excavation Contractor", S["h3"]))
flow.append(d.FillInRow([("Signature:", 0.62), ("Date:", 0.38)]))
flow.append(d.FillInRow([("Name (printed):", 0.5), ("Company:", 0.5)]))
flow.append(d.FillIn("License # (if applicable):", width=CW * 0.7))
flow.append(Spacer(1, 6))
flow.append(Paragraph("Owner-Builder Acceptance", S["h3"]))
flow.append(d.FillInRow([("Signature:", 0.62), ("Date:", 0.38)]))

flow.append(Spacer(1, 12))
flow.append(d.WriteBox(2.4, label="NOTES, ISSUES & LESSONS LEARNED"))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-1-project-planning",
                       "1.7-excavation-backfill-log.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
