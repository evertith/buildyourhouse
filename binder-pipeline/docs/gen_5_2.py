#!/usr/bin/env python3
"""5.2 Interior Door Installation Log — rebuilt on the 2026 design system.

The original repeated one identical door block 32 times to fill 20 pages. Here
the block is designed once and printed three times, with the door number as a
fill-in so the sheet photocopies for any number of doors.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    CondPageBreak,
    Flowable,
    PageBreak,
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
FORM_ID = "5.2"
FORM_TITLE = "Interior Door Installation Log"


# ---------------------------------------------------------------- local parts

class ChoiceSet(Flowable):
    """Drawn checkbox options with an optional bold lead-in label, wrapping to
    the available width.

    d.checkbox_choice_row lays out on a single line: "Door Style:" with its six
    options needs 504.5pt in a 504pt frame and ran past the right margin, and
    "Handing:" cleared it by under a point. Wrapping removes the dependence on
    that margin entirely.
    """

    def __init__(self, options, label=None, box=13, font_size=10.5, gap=14,
                 leading=20):
        super().__init__()
        self.options = list(options)
        self.label = label
        self.box = box
        self.font_size = font_size
        self.gap = gap
        self.leading = leading

    def wrap(self, availWidth, availHeight):
        d.register_fonts()
        self.width = availWidth
        items = []
        if self.label:
            items.append((self.label, True, pdfmetrics.stringWidth(
                self.label, d.BOLD, self.font_size)))
        for opt in self.options:
            items.append((opt, False, self.box + 5 + pdfmetrics.stringWidth(
                opt, d.BODY, self.font_size)))
        self._lines, cur, x = [], [], 0.0
        for it in items:
            if cur and x + it[2] > availWidth:
                self._lines.append(cur)
                cur, x = [], 0.0
            cur.append(it)
            x += it[2] + self.gap
        if cur:
            self._lines.append(cur)
        self.height = self.leading * len(self._lines)
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setStrokeColor(d.INK)
        c.setFillColor(d.INK)
        c.setLineWidth(1)
        y = self.height - self.leading + (self.leading - self.box) / 2.0
        for line in self._lines:
            x = 0
            for text, is_label, w in line:
                if is_label:
                    c.setFont(d.BOLD, self.font_size)
                    c.drawString(x, y + 2, text)
                else:
                    c.rect(x, y, self.box, self.box)
                    c.setFont(d.BODY, self.font_size)
                    c.drawString(x + self.box + 5, y + 2, text)
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


def hdr(text):
    return Paragraph(text, S["cell-hdr"])


HEADER_PAD = [("LEFTPADDING", (0, 1), (-1, 1), 4),
              ("RIGHTPADDING", (0, 1), (-1, 1), 4)]


def check_table(title, items, notes_header="Notes / Location",
                notes_w=2.3 * inch, keep=2.6 * inch):
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


# ---------------------------------------------------------------- document

CHECKLIST = [
    "Frame/jamb installed level and plumb",
    "Door slab hung (if pre-hung, verify operation)",
    "Hinges properly installed and secure",
    "Door operates smoothly (no binding)",
    "Door latches properly",
    "Reveal even all around (1/8\" typical)",
    "Strike plate installed and aligned",
    "Door stop installed (if applicable)",
    "Hardware installed (handle/knob)",
    "Ready for paint/stain",
]


def door_record():
    """One complete door-by-door record. Photocopy as many as you have doors."""
    out = [Paragraph("DOOR RECORD", S["h2"]), d.H2Rule(), Spacer(1, 4)]
    out.append(d.FillInRow([("Door #:", 0.2), ("Location / Room:", 0.5),
                            ("Size:", 0.3)]))
    out.append(ChoiceSet(
        ["Hollow Core", "Solid Core", "Panel", "French", "Bifold", "Pocket"],
        label="Door Style:"))
    out.append(ChoiceSet(
        ["Left Hand", "Right Hand", "Left Hand Reverse", "Right Hand Reverse"],
        label="Handing:"))
    out.append(Spacer(1, 6))
    out += check_table("Installation Checklist", CHECKLIST,
                       notes_header="Notes", keep=0.1 * inch)
    out.append(d.FillInRow([("Installation Date:", 0.5), ("Installer:", 0.5)]))
    out.append(labeled_box("Final Check", S["body-bold"]))
    return out


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Door-by-door tracking of frame, swing, reveal and hardware — one "
            "record per door, photocopied as many times as the house needs.")

flow.append(d.FillInRow([("Project Name:", 1.0)]))
flow.append(d.FillInRow([("Address:", 1.0)]))
flow.append(d.FillInRow([("Installer:", 0.65), ("Date Started:", 0.35)]))
flow.append(Spacer(1, 10))

flow.append(Paragraph(
    "<b>INSTRUCTIONS:</b> Record all interior door installations. Verify each "
    "item before checking complete. Check door operation, proper reveal, and "
    "hardware function before final approval.", S["body"]))
flow.append(Spacer(1, 4))

flow.append(d.callout_box(
    "Common Door Sizes",
    [Paragraph("2'0\" (24\")&nbsp;&nbsp;·&nbsp;&nbsp;2'4\" (28\")"
               "&nbsp;&nbsp;·&nbsp;&nbsp;2'6\" (30\")"
               "&nbsp;&nbsp;·&nbsp;&nbsp;2'8\" (32\")"
               "&nbsp;&nbsp;·&nbsp;&nbsp;3'0\" (36\")", S["body"])]))
flow.append(Spacer(1, 10))

flow.append(d.callout_box(
    "How to use these sheets",
    [Paragraph(
        "Three blank door records follow, one per page. Photocopy the blank "
        "record before you start and file the completed sheets in door-number "
        "order behind this cover page.", S["body"])]))

for i in range(3):
    flow.append(PageBreak())
    flow += door_record()


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-5-finish-work",
                       "5.2-interior-door-installation-log.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
