#!/usr/bin/env python3
"""5.4 Flooring Installation Guide — rebuilt on the 2026 design system."""

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
FORM_ID = "5.4"
FORM_TITLE = "Flooring Installation Guide"


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


def check_table(title, items, notes_header="Notes / Location",
                notes_w=2.3 * inch, keep=None):
    """[box] Item | Notes table. Item forms:
    str         -> checkbox + text
    (str, str)  -> checkbox + text + labelled rule in the Notes column
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


def choice(label, options):
    """Full-width mutually exclusive options on one line."""
    return d.checkbox_choice_row(label, options, S)


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Room-by-room flooring schedule plus install checklists for "
            "hardwood, tile, carpet and LVP/laminate.")

flow.append(d.FillInRow([("Project Name:", 1.0)]))
flow.append(d.FillInRow([("Address:", 1.0)]))
flow.append(d.FillInRow([("Installer:", 0.65), ("Date Started:", 0.35)]))
flow.append(Spacer(1, 10))

# ---------------- schedule
flow += d.h2("FLOORING SCHEDULE — ROOM BY ROOM", S)

SCHEDULE_ROOMS = [
    "Entry/Foyer", "Living Room", "Dining Room", "Kitchen", "Family Room",
    "Master Bedroom", "Bedroom 2", "Bedroom 3", "Bedroom 4",
    "Master Bathroom", "Bathroom 2", "Bathroom 3", "Hallway - Main",
    "Hallway - Upper", "Laundry Room", "Office/Study", "Bonus Room",
    "Closet - Master", "Closet - Bedroom 2", "Closet - Bedroom 3",
]
sched_rows = [[Paragraph(r, S["cell"]), "", "", "", "", "", ""]
              for r in SCHEDULE_ROOMS]
sched_rows += [[d.FillIn("Other:", font_size=9, height=16), "", "", "", "",
                "", ""] for _ in range(2)]

flow += data_table(
    "Flooring Schedule",
    [shdr(h) for h in ["Room / Area", "Flooring Type", "Material / Brand",
                       "Color / Finish", "Sq Ft", "Installer", "Install Date"]],
    sched_rows,
    [1.3 * inch, 0.95 * inch, 1.2 * inch, 1.05 * inch, 0.6 * inch,
     0.95 * inch, 0.95 * inch], row_height=32)

# ---------------- SECTION 1
flow += d.h2("SECTION 1: HARDWOOD / ENGINEERED FLOORING", S)

flow.append(Paragraph("Pre-Installation Measurements & Selections", S["h3"]))
flow.append(d.FillInRow([("Acclimation temperature (°F):", 0.5),
                         ("Humidity (%):", 0.5)]))
flow.append(d.FillIn("Subfloor moisture content (%):", height=28))
flow.append(choice("Underlayment required:", ["Yes", "No"]))
flow.append(d.FillIn("Underlayment type:", height=28))
flow.append(Spacer(1, 6))

flow += check_table("Pre-Installation Checklist", [
    "Flooring acclimated (minimum 3-7 days)",
    "Subfloor clean, flat, and dry",
    "Floor flatness checked (1/8\" in 10')",
    "High spots sanded/ground down",
    "Low spots filled with leveling compound",
    "Underlayment installed correctly",
    ("Installation direction determined", "Direction:"),
    "Starting wall straight and square",
], notes_header="Details / Notes")

flow += check_table("Installation Checklist", [
    "Starter row installed straight",
    "Proper expansion gap at walls (1/2\" typical)",
    "Boards properly staggered (min 6\" offset)",
    "Nail spacing correct (8-10\" along length)",
    "Face nailing at starter row only",
    "Blind nailing at 45-degree angle",
    "No squeaks when walking on floor",
    "Transitions at doorways installed",
    "Reducer strips where needed",
    "T-molding at room transitions",
    "All cuts clean and professional",
    "No visible gaps between boards",
])

flow.append(d.WriteBox(1.6, label="Hardwood / Engineered Installation Notes"))
flow.append(Spacer(1, 8))

flow += data_table(
    "Issues Encountered",
    ["Location", "Issue Description", "Resolution", "Resolved", "Date"],
    [["", "", "", d.Checkbox(), ""] for _ in range(4)],
    [1.4 * inch, 2.05 * inch, 1.85 * inch, 0.9 * inch, 0.8 * inch],
    row_height=34)

flow += data_table(
    "Rooms Completed — Hardwood / Engineered",
    ["Room Name", "Square Feet", "Install Date", "Final Inspection",
     "Ready for Use"],
    [[d.FillIn("Room:", font_size=9, height=16), "", "", d.Checkbox(),
      d.Checkbox()] for _ in range(5)],
    [2.1 * inch, 1.15 * inch, 1.2 * inch, 1.3 * inch, 1.25 * inch],
    row_height=32)

# ---------------- SECTION 2
flow += d.h2("SECTION 2: TILE FLOORING", S)

flow.append(Paragraph("Tile Specifications", S["h3"]))
flow.append(choice("Tile Type:", ["Ceramic", "Porcelain", "Stone"]))
flow.append(d.FillIn("Other:", height=26))
flow.append(d.FillInRow([("Tile Size:", 0.3), ("Brand / Style:", 0.4),
                         ("Color:", 0.3)]))
flow.append(Spacer(1, 6))

flow += check_table("Pre-Installation Checklist", [
    "Layout planned to minimize cuts",
    "Layout dry-fitted before installation",
    "Subfloor properly prepared",
    ("Backer board installed (if required)", "Type:"),
    "Backer board seams taped and thinset",
    "Floor is level and flat",
], notes_header="Details / Notes")

flow.append(Paragraph("Thinset & Grout Selections", S["h3"]))
flow.append(choice("Thinset type selected:", ["Modified", "Unmodified"]))
flow.append(d.FillIn("Grout color selected:", height=28))
flow.append(choice("Grout type:", ["Sanded", "Unsanded", "Epoxy"]))
flow.append(Spacer(1, 6))

flow += check_table("Installation Checklist", [
    "Reference lines snapped and square",
    "Thinset mixed to proper consistency",
    ("Proper trowel size used", "Trowel size:"),
    "Thinset coverage adequate (90%+ coverage)",
    "Tiles set level with each other",
    ("Grout lines consistent throughout", "Joint size:"),
    "Spacers used consistently",
    "All cut tiles have clean edges",
    "Lippage minimized (flush tiles)",
    "Tiles cleaned before grout sets",
])

flow += check_table("Grouting and Sealing Checklist", [
    ("Thinset fully cured before grouting", "Wait time:"),
    "Grout mixed to proper consistency",
    "Grout applied with rubber float",
    "Joints filled completely",
    "Excess grout removed from tile surface",
    "Grout lines uniform and consistent",
    "Haze cleaned from tiles",
    ("Grout fully cured before sealing", "Cure time:"),
    ("Sealer applied (if required)", "Sealer type:"),
    "Sealer allowed to cure properly",
    "Transitions/thresholds installed",
])

flow.append(d.WriteBox(1.6, label="Tile Installation Notes"))
flow.append(Spacer(1, 8))

flow += data_table(
    "Rooms Completed — Tile",
    ["Room Name", "Square Feet", "Tile Date", "Grout Date", "Seal Date",
     "Complete"],
    [[d.FillIn("Room:", font_size=9, height=16), "", "", "", "", d.Checkbox()]
     for _ in range(4)],
    [1.7 * inch, 1.05 * inch, 1.05 * inch, 1.1 * inch, 1.05 * inch,
     1.05 * inch], row_height=32)

# ---------------- SECTION 3
flow += d.h2("SECTION 3: CARPET INSTALLATION", S)

flow.append(Paragraph("Carpet Specifications", S["h3"]))
flow.append(d.FillInRow([("Carpet Brand:", 0.35), ("Style:", 0.35),
                         ("Color:", 0.3)]))
flow.append(choice("Fiber Type:", ["Nylon", "Polyester", "Olefin", "Wool"]))
flow.append(d.FillIn("Other:", height=26))
flow.append(Spacer(1, 6))

flow += check_table("Installation Checklist", [
    ("Carpet pad installed", "Pad type:"),
    "Pad seams taped",
    "Tack strips installed 1/2\" from wall",
    "Tack strips pointing toward wall",
    "Carpet properly stretched",
    "Power stretcher used (not knee kicker only)",
    ("Carpet seams inconspicuous", "Seam locations:"),
    "Seams properly sealed/heat bonded",
    "Carpet tucked at walls",
    "No wrinkles or bubbles",
    "Transitions at doorways installed",
    "Metal edge strips at hard surface transitions",
    "Carpet cleaned/vacuumed",
])

flow += data_table(
    "Rooms Completed — Carpet",
    ["Room Name", "Square Yards", "Install Date", "Seams", "Complete"],
    [[d.FillIn("Room:", font_size=9, height=16), "", "",
      ChoiceSet(["Y", "N"], box=9, font_size=8.5, gap=7), d.Checkbox()]
     for _ in range(5)],
    [2.1 * inch, 1.3 * inch, 1.3 * inch, 1.2 * inch, 1.1 * inch],
    row_height=32)

# ---------------- SECTION 4
flow += d.h2("SECTION 4: LVP / LAMINATE FLOORING", S)

flow.append(choice("Flooring Type:", ["LVP (Luxury Vinyl Plank)", "Laminate"]))
flow.append(d.FillInRow([("Brand:", 0.35), ("Style:", 0.35), ("Color:", 0.3)]))
flow.append(choice("Underlayment required:", ["Yes", "No"]))
flow.append(d.FillIn("Underlayment type:", height=28))
flow.append(Spacer(1, 6))

flow += check_table("Installation Checklist", [
    "Flooring acclimated (24-48 hours minimum)",
    "Subfloor clean, flat, and dry",
    "Underlayment installed (if required)",
    "Moisture barrier installed (if needed)",
    ("Installation direction determined", "Direction:"),
    "First row started straight",
    "Expansion gaps at all walls (1/4\" minimum)",
    "Planks/boards staggered properly",
    "Locking mechanism engaged fully",
    "No gaps between planks",
    "Transitions at doorways installed",
    "Reducer strips where needed",
    "T-molding at transitions",
    "Quarter round or shoe molding (if applicable)",
])

flow += data_table(
    "Rooms Completed — LVP / Laminate",
    ["Room Name", "Square Feet", "Install Date", "Transitions", "Complete"],
    [[d.FillIn("Room:", font_size=9, height=16), "", "", d.Checkbox(),
      d.Checkbox()] for _ in range(4)],
    [2.3 * inch, 1.4 * inch, 1.4 * inch, 1.0 * inch, 0.9 * inch],
    row_height=32)

# ---------------- SECTION 5
flow += d.h2("SECTION 5: FINAL FLOORING CHECKLIST", S)

flow += check_table("Final Checklist", [
    "All flooring installed per schedule",
    "All transitions/thresholds installed",
    "All reducer strips installed",
    "All T-moldings installed",
    "Floor protection installed during other work",
    "No scratches or damage to flooring",
    "All flooring cleaned",
    "Warranty documentation collected",
    "Care/maintenance instructions received",
    "Final walkthrough completed",
], notes_header="Notes")

flow.append(d.WriteBox(2.6, label="Overall Comments"))
flow.append(Spacer(1, 10))

flow += d.signature_block([
    ("Installer Signature", True),
    ("Owner / Builder Approval", True),
])


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-5-finish-work",
                       "5.4-flooring-installation-guide.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
