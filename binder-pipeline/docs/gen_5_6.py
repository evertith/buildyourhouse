#!/usr/bin/env python3
"""5.6 Paint Color & Finish Tracking — rebuilt on the 2026 design system."""

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
FORM_ID = "5.6"
FORM_TITLE = "Paint Color & Finish Tracking"


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
    return Paragraph(text, S["cell-hdr-sm"])


HEADER_PAD = [("LEFTPADDING", (0, 1), (-1, 1), 4),
              ("RIGHTPADDING", (0, 1), (-1, 1), 4)]


def keep_for(n_rows, row_height=34, cap=3.7 * inch, floor=2.1 * inch):
    est = 68 + n_rows * (row_height or 34)
    return est if est <= cap else floor


def check_table(title, items, notes_header="Notes", notes_w=2.3 * inch,
                keep=None):
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
    heads = [h if isinstance(h, Flowable) else hdr(h) for h in headers]
    t = d.titled_table(title, heads, rows, col_widths, S,
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


def coats(n):
    return ChoiceSet([str(i) for i in range(1, n + 1)], box=9, font_size=8,
                     gap=5)


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Every colour, code and sheen in the house recorded in one place — "
            "so touch-ups five years from now still match.")

flow.append(d.FillInRow([("Project Name:", 1.0)]))
flow.append(d.FillInRow([("Address:", 1.0)]))
flow.append(d.FillInRow([("Painter:", 0.65), ("Date Started:", 0.35)]))
flow.append(Spacer(1, 10))

# ---------------- SECTION 1
flow += d.h2("SECTION 1: INTERIOR PAINT SCHEDULE", S)
flow.append(d.FillInRow([("Paint Brand — Primary:", 0.5),
                         ("Secondary:", 0.5)]))
flow.append(Spacer(1, 6))
flow.append(d.callout_box(
    "Finish Guide",
    [Paragraph("Flat (low/no sheen)&nbsp;&nbsp;·&nbsp;&nbsp;Eggshell (slight "
               "sheen)&nbsp;&nbsp;·&nbsp;&nbsp;Satin (soft sheen)"
               "&nbsp;&nbsp;·&nbsp;&nbsp;Semi-Gloss (shiny)"
               "&nbsp;&nbsp;·&nbsp;&nbsp;Gloss (very shiny)", S["body"])]))
flow.append(Spacer(1, 10))

INTERIOR_ROOMS = [
    "Entry/Foyer", "Living Room", "Dining Room", "Kitchen", "Family Room",
    "Master Bedroom", "Bedroom 2", "Bedroom 3", "Bedroom 4", "Office/Study",
    "Bonus Room", "Hallway - Main", "Hallway - Upper", "Stairway",
    "Master Bathroom", "Bathroom 2", "Bathroom 3", "Powder Room",
    "Laundry Room", "Pantry", "Master Closet", "Closet - Bedroom 2",
    "Closet - Bedroom 3", "Closet - Bedroom 4", "Linen Closet", "Coat Closet",
    "Garage (interior)", "Utility / Mechanical",
]
interior_rows = [[Paragraph(r, S["cell"]), "", "", "", "", "", coats(2),
                  d.Checkbox()] for r in INTERIOR_ROOMS]
interior_rows += [[d.FillIn("Other:", font_size=9, height=16), "", "", "", "",
                   "", coats(2), d.Checkbox()] for _ in range(2)]

flow += data_table(
    "Interior Paint Schedule",
    [shdr(h) for h in ["Room", "Wall Color", "Color Code", "Ceiling", "Trim",
                       "Finish", "Coats", "Touch-Up"]],
    interior_rows,
    [1.15 * inch, 1.0 * inch, 0.85 * inch, 0.85 * inch, 0.85 * inch,
     0.78 * inch, 0.7 * inch, 0.82 * inch],
    row_height=32,
    extra=[("LEFTPADDING", (6, 1), (-1, -1), 3),
           ("RIGHTPADDING", (6, 1), (-1, -1), 3),
           ("ALIGN", (7, 2), (7, -1), "CENTER")])

flow.append(Paragraph("Paint Color Reference Chart", S["h3"]))
flow.append(Paragraph(
    "Keep paint chip samples or color swatches with this document for future "
    "reference.", S["body"]))
flow += data_table(
    "Color Reference",
    ["Color Name", "Brand", "Color Code / Number", "Finish Used",
     "Rooms Where Used"],
    [["", "", "", "", ""] for _ in range(6)],
    [1.55 * inch, 1.35 * inch, 1.3 * inch, 1.15 * inch, 1.65 * inch],
    row_height=34)

# ---------------- SECTION 2
flow += d.h2("SECTION 2: EXTERIOR PAINT SCHEDULE", S)
flow.append(d.FillIn("Exterior Paint Brand:", height=26))
flow.append(d.checkbox_choice_row("Type:", ["Latex", "Oil-Based"], S))
flow.append(d.FillIn("Other:", height=26))
flow.append(Spacer(1, 6))

EXTERIOR_AREAS = [
    "Body/Siding", "Trim/Fascia", "Soffit", "Front Door", "Garage Door(s)",
    "Shutters", "Deck/Porch Floor", "Deck/Porch Railings", "Columns/Posts",
    "Foundation",
]
ext_rows = [[Paragraph(a, S["cell"]), "", "", "", coats(3), d.Checkbox(),
             d.Checkbox()] for a in EXTERIOR_AREAS]
ext_rows.append([d.FillIn("Other:", font_size=9, height=16), "", "", "",
                 coats(3), d.Checkbox(), d.Checkbox()])

flow += data_table(
    "Exterior Paint Colors",
    [shdr(h) for h in ["Area / Surface", "Color Name", "Code", "Finish",
                       "Coats", "Primer", "Complete"]],
    ext_rows,
    [1.4 * inch, 1.25 * inch, 0.9 * inch, 0.95 * inch, 1.05 * inch,
     0.65 * inch, 0.8 * inch],
    row_height=32,
    extra=[("LEFTPADDING", (4, 1), (-1, -1), 3),
           ("RIGHTPADDING", (4, 1), (-1, -1), 3),
           ("ALIGN", (5, 2), (-1, -1), "CENTER")])

flow.append(d.WriteBox(1.8, label="Exterior Paint Notes"))

# ---------------- SECTION 3
flow += d.h2("SECTION 3: PAINT PREPARATION & APPLICATION", S)

flow += check_table("Interior Preparation Checklist", [
    "All drywall repairs completed",
    "Surfaces sanded smooth",
    "Dust removed from all surfaces",
    "Walls wiped down/cleaned",
    "Trim caulked at walls and joints",
    "Nail holes filled in trim",
    ("Primer applied where needed", "Primer type:"),
    "Masking/protection of floors",
    "Masking/protection of fixtures",
    "Windows and doors masked",
    "Outlets/switches covered",
], notes_header="Notes / Date")

flow.append(Paragraph("Application Method", S["h3"]))
flow.append(d.checkbox_choice_row("Walls:", ["Roller", "Spray", "Combination"],
                                  S))
flow.append(d.checkbox_choice_row("Trim:", ["Brush", "Spray", "Combination"],
                                  S))
flow.append(Spacer(1, 6))

flow += check_table("Application Checklist", [
    "Cut-in at edges completed first",
    "Paint applied in thin, even coats",
    "No drips or runs",
    ("Adequate drying time between coats", "Recoat time:"),
    "Coverage uniform (no thin spots)",
    "Brush/roller marks minimized",
    "Clean paint lines at edges",
    "Second coat applied where needed",
])

# ---------------- SECTION 4
flow += d.h2("SECTION 4: TOUCH-UP PAINT STORAGE LOG", S)
flow.append(Paragraph(
    "Record the location of all touch-up paint for future reference.",
    S["body"]))

flow += data_table(
    "Touch-Up Paint Storage",
    ["Paint Color / Code", "Room(s) Used", "Finish Type", "Can Size",
     "Storage Location", "Qty"],
    [["", "", "", "", "", ""] for _ in range(14)],
    [1.35 * inch, 1.5 * inch, 1.05 * inch, 0.85 * inch, 1.55 * inch,
     0.7 * inch], row_height=32)

flow.append(d.callout_box(
    "Touch-Up Paint Storage Tips",
    [Paragraph("• Store paint in a cool, dry place away from extreme "
               "temperatures", S["body"]),
     Paragraph("• Ensure lids are tightly sealed to prevent drying", S["body"]),
     Paragraph("• Label each can with room name and date for easy "
               "identification", S["body"]),
     Paragraph("• Keep paint chips/samples with stored paint for color "
               "matching", S["body"]),
     Paragraph("• Dispose of old or dried paint according to local "
               "regulations", S["body"])]))

# ---------------- SECTION 5
flow += d.h2("SECTION 5: FINAL PAINT CHECKLIST & APPROVAL", S)

flow += check_table("Final Checklist", [
    "All interior rooms painted per schedule",
    "All ceiling paint complete",
    "All trim paint complete",
    "All exterior surfaces painted per schedule",
    "Paint coverage uniform throughout",
    "No missed spots or holidays",
    "Clean paint lines at all edges",
    "No drips, runs, or sags",
    "Touch-up completed where needed",
    "All masking/protection removed",
    "Floors and fixtures cleaned",
    "Windows cleaned of overspray",
    "Outlet/switch plates reinstalled",
    "Touch-up paint stored and labeled",
    "Paint schedule documented",
    "Final walkthrough completed",
])

flow += data_table(
    "Issues / Areas Needing Touch-Up",
    ["Room / Area", "Issue Description", "Resolved", "Date"],
    [["", "", d.Checkbox(), ""] for _ in range(5)],
    [1.95 * inch, 2.95 * inch, 0.95 * inch, 1.15 * inch], row_height=32)

flow.append(d.WriteBox(2.2, label="Overall Comments"))
flow.append(Spacer(1, 10))

flow += d.signature_block([
    ("Painter Signature", True),
    ("Owner / Builder Approval", True),
])


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-5-finish-work",
                       "5.6-paint-color-finish-tracking.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
