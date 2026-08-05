#!/usr/bin/env python3
"""5.3 Trim & Finish Carpentry Log — rebuilt on the 2026 design system."""

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
S["cell-hdr-sm"] = ParagraphStyle("cell-hdr-sm", parent=S["cell-bold"],
                                  fontSize=8, leading=9.5)
CW = d.content_width()

SECTION = "Section 5: Finish Work"
FORM_ID = "5.3"
FORM_TITLE = "Trim & Finish Carpentry Log"


# ---------------------------------------------------------------- local parts

class ChoiceSet(Flowable):
    """Drawn checkbox options that wrap to the available width."""

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


def hdr(text):
    return Paragraph(text, S["cell-hdr"])


def shdr(text):
    """8pt header for the narrow tick columns of a room matrix."""
    return Paragraph(text, S["cell-hdr-sm"])


HEADER_PAD = [("LEFTPADDING", (0, 1), (-1, 1), 4),
              ("RIGHTPADDING", (0, 1), (-1, 1), 4)]


def keep_for(n_rows, row_height=34, cap=3.7 * inch, floor=2.1 * inch):
    """Short tables are held together whole; long ones only need enough room to
    be worth starting, since the title and header repeat after a break."""
    est = 68 + n_rows * (row_height or 34)
    return est if est <= cap else floor


def check_table(title, items, notes_header="Notes / Location",
                notes_w=2.3 * inch, keep=None):
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


def matrix_table(title, label_header, check_headers, labels, notes_header=None,
                 label_w=1.25 * inch, notes_w=1.85 * inch, row_height=30,
                 keep=None):
    """Room/location down the side, one drawn tick box per quality column."""
    n = len(check_headers)
    heads = [shdr(label_header)] + [shdr(h) for h in check_headers]
    body_w = CW - label_w - (notes_w if notes_header else 0)
    widths = [label_w] + [body_w / n] * n
    if notes_header:
        heads.append(shdr(notes_header))
        widths.append(notes_w)
    rows = []
    for lab in labels:
        cell = lab if isinstance(lab, Flowable) else Paragraph(lab, S["cell"])
        row = [cell] + [d.Checkbox() for _ in range(n)]
        if notes_header:
            row.append("")
        rows.append(row)
    t = d.titled_table(title, heads, rows, widths, S,
                       row_heights=[row_height] * len(rows))
    t.setStyle(TableStyle([
        ("LEFTPADDING", (1, 1), (-1, 1), 3),
        ("RIGHTPADDING", (1, 1), (-1, 1), 3),
        ("ALIGN", (1, 2), (n, -1), "CENTER"),
    ]))
    keep = keep_for(len(rows), row_height) if keep is None else keep
    return [CondPageBreak(keep), t, Spacer(1, 8)]


def numbered_slots(prefix, count):
    """'Door #1:' style write-in labels down the left column of a matrix."""
    return [d.FillIn(f"{prefix} #{i}:", font_size=9, height=16)
            for i in range(1, count + 1)]


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Baseboard, casing, crown and millwork tracked room by room — "
            "miters, nail holes and caulk signed off before paint.")

flow.append(d.FillInRow([("Project Name:", 1.0)]))
flow.append(d.FillInRow([("Address:", 1.0)]))
flow.append(d.FillInRow([("Carpenter:", 0.65), ("Date Started:", 0.35)]))
flow.append(Spacer(1, 10))

# ---------------- SECTION 1
flow += d.h2("SECTION 1: BASEBOARD INSTALLATION", S)
flow.append(d.FillInRow([("Baseboard Profile / Style:", 0.65),
                         ("Height:", 0.35)]))
flow.append(Spacer(1, 6))

ROOMS = ["Entry/Foyer", "Living Room", "Dining Room", "Kitchen", "Family Room",
         "Master Bedroom", "Bedroom 2", "Bedroom 3", "Bedroom 4",
         "Master Bath", "Bath 2", "Bath 3", "Hallway 1", "Hallway 2",
         "Laundry Room", "Office/Study", "Bonus Room"]

flow += matrix_table(
    "Baseboard by Room", "Room / Area",
    ["Completed", "Caulked Top", "Nail Holes Filled", "Corners Tight",
     "Paint Ready"],
    ROOMS + [d.FillIn("Other:", font_size=9, height=16)],
    notes_header="Notes")

flow.append(d.WriteBox(1.5, label="Baseboard Installation Notes"))

# ---------------- SECTION 2
flow += d.h2("SECTION 2: DOOR CASING / TRIM", S)
flow.append(d.FillInRow([("Casing Profile / Style:", 0.65), ("Width:", 0.35)]))
flow.append(Spacer(1, 6))

flow += matrix_table(
    "Door Casing by Opening", "Door Location",
    ["Casing Complete", "Reveals Even", "Miters Tight", "Nail Holes Filled",
     "Paint Ready"],
    numbered_slots("Door", 24), label_w=2.6 * inch, notes_w=0)

flow.append(d.WriteBox(1.8, label="Door Casing Installation Notes"))
flow.append(Spacer(1, 8))

flow += data_table(
    "Door Trim Issues / Repairs Needed",
    ["Door Location", "Issue Description", "Corrected", "Date"],
    [["", "", d.Checkbox(), ""] for _ in range(5)],
    [1.95 * inch, 2.95 * inch, 0.95 * inch, 1.15 * inch], row_height=32)

# ---------------- SECTION 3
flow += d.h2("SECTION 3: WINDOW CASING / TRIM", S)
flow.append(d.FillInRow([("Window Casing Profile / Style:", 0.65),
                         ("Width:", 0.35)]))
flow.append(Spacer(1, 6))

flow += matrix_table(
    "Window Casing by Opening", "Window Location",
    ["Casing Complete", "Sill Installed", "Apron (if appl.)", "Miters Tight",
     "Paint Ready"],
    numbered_slots("Window", 20), label_w=2.6 * inch, notes_w=0)

flow.append(d.WriteBox(1.5, label="Window Casing Installation Notes"))
flow.append(Spacer(1, 8))

flow += data_table(
    "Window Trim Issues / Repairs",
    ["Window Location", "Issue Description", "Corrected", "Date"],
    [["", "", d.Checkbox(), ""] for _ in range(5)],
    [1.95 * inch, 2.95 * inch, 0.95 * inch, 1.15 * inch], row_height=32)

# ---------------- SECTION 4
flow += d.h2("SECTION 4: CROWN MOLDING", S)
flow.append(d.FillInRow([("Crown Molding Profile / Style:", 0.65),
                         ("Size:", 0.35)]))
flow.append(Spacer(1, 6))

flow += matrix_table(
    "Crown Molding by Room", "Room / Area",
    ["Crown Installed", "Miters Tight", "Caulked at Ceiling",
     "Nail Holes Filled", "Paint Ready"],
    ["Entry/Foyer", "Living Room", "Dining Room", "Kitchen", "Family Room",
     "Master Bedroom", "Bedroom 2", "Bedroom 3", "Bedroom 4", "Office/Study",
     "Bonus Room"]
    + [d.FillIn("Other:", font_size=9, height=16) for _ in range(2)],
    notes_header="Notes")

flow.append(d.WriteBox(1.5, label="Crown Molding Notes"))

# ---------------- SECTION 5
flow += d.h2("SECTION 5: OTHER TRIM & MILLWORK", S)

flow += data_table(
    "Chair Rail",
    ["Room / Area", "Installed", "Height from Floor", "Miters Tight",
     "Paint Ready", "Notes"],
    [[Paragraph(r, S["cell"]), d.Checkbox(), "", d.Checkbox(), d.Checkbox(), ""]
     for r in ["Dining Room", "Hallway", "Bedroom"]]
    + [[d.FillIn("Other:", font_size=9, height=16), d.Checkbox(), "",
        d.Checkbox(), d.Checkbox(), ""] for _ in range(2)],
    [1.3 * inch, 0.75 * inch, 1.15 * inch, 0.8 * inch, 0.8 * inch, 2.2 * inch],
    row_height=32)

flow += data_table(
    "Wainscoting / Paneling",
    ["Room / Area", "Installed", "Height", "Cap Molding", "Paint Ready",
     "Notes"],
    [[Paragraph(r, S["cell"]), d.Checkbox(), "", d.Checkbox(), d.Checkbox(), ""]
     for r in ["Dining Room", "Bath", "Hallway"]]
    + [[d.FillIn("Other:", font_size=9, height=16), d.Checkbox(), "",
        d.Checkbox(), d.Checkbox(), ""]],
    [1.3 * inch, 0.75 * inch, 1.0 * inch, 0.95 * inch, 0.8 * inch, 2.2 * inch],
    row_height=32)

flow += data_table(
    "Built-Ins and Shelving",
    ["Location / Description", "Installed", "Finish Applied", "Hardware",
     "Complete", "Notes"],
    [["", d.Checkbox(), d.Checkbox(), d.Checkbox(), d.Checkbox(), ""]
     for _ in range(5)],
    [2.0 * inch, 0.75 * inch, 0.95 * inch, 0.85 * inch, 0.8 * inch,
     1.65 * inch],
    row_height=32)

# ---------------- SECTION 6
flow += d.h2("SECTION 6: FINAL TRIM CHECKLIST & APPROVAL", S)

flow += check_table("Final Trim Checklist", [
    "All baseboard installed and finished",
    "All door casings installed and finished",
    "All window casings installed and finished",
    "Crown molding complete (where specified)",
    "Chair rail complete (where specified)",
    "All miters tight and professional",
    "All nail holes filled",
    "All joints caulked where required",
    "Touch-up sanding complete",
    "All trim ready for final paint/stain",
    "Built-ins and shelving complete",
    "Hardware installed on built-ins",
    "All trim debris removed",
    "Final walkthrough completed",
], notes_header="Notes")

flow.append(d.WriteBox(2.0, label="Overall Comments"))
flow.append(Spacer(1, 10))

flow += d.signature_block([
    ("Carpenter Signature", True),
    ("Owner / Builder Approval", True),
])


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-5-finish-work",
                       "5.3-trim-finish-carpentry-log.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
