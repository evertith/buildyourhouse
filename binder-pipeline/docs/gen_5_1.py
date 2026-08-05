#!/usr/bin/env python3
"""5.1 Drywall Completion Checklist — rebuilt on the 2026 design system."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    CondPageBreak,
    Flowable,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

import design as d

S = d.make_styles()
S["cell-hdr"] = ParagraphStyle("cell-hdr", parent=S["cell-bold"],
                               fontSize=9, leading=11)
CW = d.content_width()

SECTION = "Section 5: Finish Work"
FORM_ID = "5.1"
FORM_TITLE = "Drywall Completion Checklist"


# ---------------------------------------------------------------- local parts

class ChoiceSet(Flowable):
    """Drawn checkbox options that wrap to the available width.

    d.checkbox_choice_row draws one line only; these option sets have to sit in
    narrow table cells, so this variant reflows. Boxes are drawn, never glyphs.
    """

    def __init__(self, options, box=10, font_size=9, gap=9, leading=15):
        super().__init__()
        self.options = list(options)
        self.box = box
        self.font_size = font_size
        self.gap = gap
        self.leading = leading

    def wrap(self, availWidth, availHeight):
        d.register_fonts()
        self.width = availWidth
        self._lines, cur, x = [], [], 0.0
        for opt in self.options:
            w = self.box + 4 + pdfmetrics.stringWidth(opt, d.BODY, self.font_size)
            if cur and x + w > availWidth:
                self._lines.append(cur)
                cur, x = [], 0.0
            cur.append((opt, w))
            x += w + self.gap
        if cur:
            self._lines.append(cur)
        self.height = self.leading * len(self._lines)
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setStrokeColor(d.INK)
        c.setFillColor(d.INK)
        c.setLineWidth(1)
        c.setFont(d.BODY, self.font_size)
        y = self.height - self.leading + (self.leading - self.box) / 2.0
        for line in self._lines:
            x = 0
            for opt, w in line:
                c.rect(x, y, self.box, self.box)
                c.drawString(x + self.box + 4, y + 1.5, opt)
                x += w + self.gap
            y -= self.leading


def labeled_box(text, style=None, width=None):
    """One drawn checkbox with its label, as a body-level flowable."""
    w = width or CW
    t = Table([[d.Checkbox(), Paragraph(text, style or S["body"])]],
              colWidths=[0.42 * inch, w - 0.42 * inch])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (1, 0), (1, 0), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    return t


def blank_check_lines(n, label=""):
    """n rows of 'drawn checkbox + writing rule' — for open-ended punch lists."""
    rows = [[d.Checkbox(), d.FillIn(label, height=18)] for _ in range(n)]
    t = Table(rows, colWidths=[0.42 * inch, CW - 0.42 * inch],
              rowHeights=[31] * n)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
    ]))
    return t


def hdr(text):
    """Column header cell: 9pt bold, tight leading so short labels never
    break mid-word in a narrow column."""
    return Paragraph(text, S["cell-hdr"])


HEADER_PAD = [("LEFTPADDING", (0, 1), (-1, 1), 4),
              ("RIGHTPADDING", (0, 1), (-1, 1), 4)]


def keep_for(n_rows, row_height=34, cap=3.7 * inch, floor=2.1 * inch):
    """Short tables are held together whole; long ones only need enough room to
    be worth starting, since the title and header repeat after a break."""
    est = 68 + n_rows * (row_height or 34)
    return est if est <= cap else floor


def check_table(title, items, notes_header="Notes / Location",
                notes_w=2.3 * inch, keep=None):
    """[box] Item | Notes table. Item forms:
    str                       -> checkbox + text
    (str, str)                -> checkbox + text + labelled rule in Notes
    list[(label, fraction)]   -> full-width drawn fill-in row (measurements)
    Flowable                  -> full-width spanned row (choice sets, notes)
    """
    keep = keep_for(len(items), 34) if keep is None else keep
    header = ["", hdr("Item"), hdr(notes_header)]
    # No full-width spanned rows here. A cell SPANned after construction is
    # still height-calculated at its own (narrow) column width, which inflated
    # one-line notes into 140pt rows. Full-width fields go at body level.
    rows = []
    for it in items:
        if isinstance(it, tuple):
            text, note = it
            rows.append([d.Checkbox(), Paragraph(text, S["cell"]),
                         d.FillIn(note, font_size=9, height=16)])
        else:
            rows.append([d.Checkbox(), Paragraph(it, S["cell"]), ""])
    col = [0.42 * inch, CW - 0.42 * inch - notes_w, notes_w]
    t = d.titled_table(title, header, rows, col, S)
    t.setStyle(TableStyle([("TOPPADDING", (0, 2), (-1, -1), 9),
                           ("BOTTOMPADDING", (0, 2), (-1, -1), 9)]
                          + HEADER_PAD))
    return [CondPageBreak(keep), t, Spacer(1, 8)]


def data_table(title, headers, rows, col_widths, row_height=32, pad=None,
               keep=None, extra=None):
    """Columnar write-in table. row_height=None auto-sizes with generous
    padding so flowable cells (choice sets) can never clip. The CondPageBreak
    stops a table breaking with only a row or two left behind."""
    t = d.titled_table(title, [hdr(h) for h in headers], rows, col_widths, S,
                       row_heights=None if row_height is None
                       else [row_height] * len(rows))
    keep = keep_for(len(rows), row_height) if keep is None else keep
    cmds = list(HEADER_PAD)
    if pad:
        cmds += [("TOPPADDING", (0, 2), (-1, -1), pad),
                 ("BOTTOMPADDING", (0, 2), (-1, -1), pad)]
    if extra:
        cmds += extra
    t.setStyle(TableStyle(cmds))
    return [CondPageBreak(keep), t, Spacer(1, 8)]


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Hanging, three-coat taping, sanding and texture — inspected stage "
            "by stage, with problem areas documented before paint.")

flow.append(d.FillInRow([("Project Name:", 1.0)]))
flow.append(d.FillInRow([("Address:", 1.0)]))
flow.append(d.FillInRow([("Inspector / Supervisor:", 0.65), ("Date:", 0.35)]))
flow.append(Spacer(1, 10))

# ---------------- SECTION 1
flow += d.h2("SECTION 1: DRYWALL HANGING INSPECTION", S)

flow += check_table("Hanging Inspection", [
    "All walls covered with drywall",
    "All ceilings covered with drywall",
    "Proper screw spacing (12\" o.c. walls, 12\" o.c. ceilings)",
    "No screws proud of surface (all dimpled)",
    "Corner bead installed on all outside corners",
    "Corner bead straight and secure",
    "Cutouts for electrical boxes correct and clean",
    "Cutouts for mechanical vents correct",
    "Cutouts for plumbing access correct",
    "HVAC register openings cut accurately",
    "Recessed lighting openings cut properly",
    "Joints staggered (no four-way intersections)",
    "Proper moisture-resistant drywall in wet areas",
    "Proper fire-rated drywall where required",
    "No gaps larger than 1/4\" at joints",
])

flow.append(d.WriteBox(1.3, label="Additional Hanging Notes"))

# ---------------- SECTION 2
flow += d.h2("SECTION 2: TAPING AND FINISHING", S)

flow += check_table("First Coat (Tape and Embed)", [
    "All joints taped with paper or mesh tape",
    "Tape embedded in joint compound",
    "No bubbles or wrinkles in tape",
    "Corner bead coated",
    "Inside corners taped and embedded",
    "All screw dimples filled",
    "No ridges or high spots",
    "Compound feathered at edges",
    "Adequate drying time allowed (24+ hours)",
])
flow.append(d.FillInRow([("First Coat Completion Date:", 0.55),
                         ("Inspector:", 0.45)]))
flow.append(Spacer(1, 6))

flow += check_table("Second Coat (Fill and Feather)", [
    "All joints covered with wider coat",
    "Screw dimples filled again if needed",
    "Feathered edges 2-3\" wider than first coat",
    "Corner beads coated smoothly",
    "Inside corners smooth and even",
    "Any imperfections from first coat corrected",
    "No trowel marks or ridges",
    "Smooth transition from joint to field",
    "Adequate drying time allowed (24+ hours)",
])
flow.append(d.FillInRow([("Second Coat Completion Date:", 0.55),
                         ("Inspector:", 0.45)]))
flow.append(Spacer(1, 6))

flow += check_table("Third Coat (Final Skim / Finish Coat)", [
    "Final skim coat applied to all joints",
    "Feathered edges 4-6\" wider than second coat",
    "All screw dimples completely invisible",
    "Corners perfectly smooth",
    "No visible ridges or imperfections",
    "Smooth transition — can't see/feel joints",
    "Entire surface ready for texture/paint",
    "Adequate drying time allowed (24+ hours)",
])
flow.append(d.FillInRow([("Third Coat Completion Date:", 0.55),
                         ("Inspector:", 0.45)]))
flow.append(Spacer(1, 6))

flow += check_table("Sanding", [
    "All joints sanded smooth",
    "No high spots or ridges remain",
    "Corners sanded carefully (not oversanded)",
    "Entire surface smooth to touch",
    "Dust cleaned from all surfaces",
    "Dust vacuumed from floors",
    "Light test performed (no shadows/defects)",
    "Touch-up areas identified and listed below",
])
flow.append(d.FillInRow([("Sanding Completion Date:", 0.55),
                         ("Inspector:", 0.45)]))
flow.append(Spacer(1, 6))

flow.append(Paragraph("Texture Application (if applicable)", S["h3"]))
flow.append(d.checkbox_choice_row(
    "Texture Type:", ["Orange Peel", "Knockdown", "Skip Trowel", "Smooth"], S))
flow.append(d.FillIn("Other:", height=26))
flow.append(Spacer(1, 4))
flow += check_table("Texture Checklist", [
    "Surface properly primed before texture",
    "Texture pattern consistent throughout",
    "Texture density/coverage uniform",
    "Knockdown timing consistent (if applicable)",
    "Corners and edges textured properly",
    "Ceiling texture matches walls (if same)",
    "No drips or runs in texture",
    "Sample approved before full application",
    "Adequate drying time before painting",
])
flow.append(d.FillInRow([("Texture Completion Date:", 0.55),
                         ("Applicator:", 0.45)]))
flow.append(Spacer(1, 6))

flow += data_table(
    "Touch-Up Areas Needed",
    ["Location / Room", "Issue", "Corrected", "Date"],
    [["", "", d.Checkbox(), ""] for _ in range(8)],
    [1.95 * inch, 2.95 * inch, 0.95 * inch, 1.15 * inch], row_height=32)

# ---------------- SECTION 3
flow += d.h2("SECTION 3: PROBLEM AREAS DOCUMENTATION", S)

flow += data_table(
    "Cracks Noted",
    ["Location", "Length", "Width", "Cause", "Repair Method", "Repaired"],
    [["", "", "", "", "", d.Checkbox()] for _ in range(6)],
    [1.45 * inch, 0.8 * inch, 0.8 * inch, 1.4 * inch, 1.6 * inch, 0.95 * inch],
    row_height=32)

flow += data_table(
    "Nail Pops Noted",
    ["Location / Room", "Number of Pops", "Cause (if known)", "Repaired",
     "Date"],
    [["", "", "", d.Checkbox(), ""] for _ in range(6)],
    [1.7 * inch, 1.15 * inch, 1.85 * inch, 0.95 * inch, 1.35 * inch],
    row_height=32)

flow += data_table(
    "Other Repairs Needed",
    ["Location", "Description of Issue", "Priority", "Completed", "Date"],
    [["", "", ChoiceSet(["High", "Med", "Low"], box=9, font_size=8.5, gap=6),
      d.Checkbox(), ""] for _ in range(6)],
    [1.3 * inch, 2.1 * inch, 1.45 * inch, 0.95 * inch, 1.2 * inch],
    row_height=44)

# ---------------- SECTION 4
flow += d.h2("SECTION 4: FINAL APPROVAL", S)

approval = [
    ("Overall drywall installation quality", ["Pass", "Fail"]),
    ("Taping and finishing quality", ["Pass", "Fail"]),
    ("Texture application (if applicable)", ["Pass", "Fail", "N/A"]),
    ("All repairs completed satisfactorily", ["Pass", "Fail"]),
    ("Surface ready for priming/painting", ["Pass", "Fail"]),
    ("Acceptable for next phase of work", ["Yes", "No"]),
]
flow += data_table(
    "Quality Check Sign-Off",
    ["Quality Check", "Result", "Notes"],
    [[Paragraph(t, S["cell"]), ChoiceSet(opts, box=9, font_size=8.5, gap=7), ""]
     for t, opts in approval],
    [2.6 * inch, 1.5 * inch, 2.9 * inch], row_height=None, pad=11)

flow.append(d.WriteBox(2.0, label="Overall Comments / Observations"))
flow.append(Spacer(1, 10))

flow += d.signature_block([
    ("Inspector / Supervisor Signature", True),
    ("Owner / Builder Signature", True),
])

flow.append(Paragraph("Items to be Completed Before Next Phase", S["h3"]))
flow.append(blank_check_lines(5))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-5-finish-work",
                       "5.1-drywall-completion-checklist.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
