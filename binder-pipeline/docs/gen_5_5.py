#!/usr/bin/env python3
"""5.5 Cabinet Installation Checklist — rebuilt on the 2026 design system."""

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
FORM_ID = "5.5"
FORM_TITLE = "Cabinet Installation Checklist"


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


def check_table(title, items, notes_header="Notes / Measurements",
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


def guide(text):
    """A printed rule-of-thumb, set below the table it qualifies."""
    return Paragraph(text, S["note"])


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Base and upper cabinets, hardware, countertops and vanities — "
            "level, plumb, secured and sealed, verified against real numbers.")

flow.append(d.FillInRow([("Project Name:", 1.0)]))
flow.append(d.FillInRow([("Address:", 1.0)]))
flow.append(d.FillInRow([("Cabinet Installer:", 0.65), ("Date Started:", 0.35)]))
flow.append(Spacer(1, 10))

# ---------------- SECTION 1
flow += d.h2("SECTION 1: KITCHEN CABINETS — BASE CABINETS", S)
flow.append(d.FillInRow([("Cabinet Manufacturer:", 0.5), ("Style:", 0.5)]))
flow.append(d.FillInRow([("Color / Finish:", 1.0)]))
flow.append(Spacer(1, 6))

flow += check_table("Base Cabinet Installation Checklist", [
    "All base cabinets received and inspected",
    "Cabinets checked for damage before install",
    "Wall studs located and marked",
    ("High point of floor located", "Location:"),
    "Base cabinets shimmed level (side to side)",
    "Base cabinets shimmed level (front to back)",
    ("All cabinets at consistent height", "Height (in):"),
    "All base cabinets plumb",
    "Cabinets secured to wall studs (min 2 screws)",
    "Adjacent cabinets fastened together",
    "Face frames aligned flush",
    ("Toe kick installed", "Height (in):"),
    "Toe kick level across all cabinets",
    "Shims cut flush and not visible",
])

flow.append(d.WriteBox(1.6, label="Base Cabinet Notes"))

# ---------------- SECTION 2
flow += d.h2("SECTION 2: KITCHEN CABINETS — UPPER CABINETS", S)

flow += check_table("Upper Cabinet Installation Checklist", [
    "All upper cabinets received and inspected",
    "Ledger board installed for support",
    "Upper cabinets level (side to side)",
    "Upper cabinets level (front to back)",
    ("All cabinets at consistent height", "Above counter (in):"),
    "All upper cabinets plumb",
    "Cabinets secured to wall studs (min 2 screws)",
    "Adjacent cabinets fastened together",
    "Face frames aligned flush",
    "Cabinet bottoms aligned",
    "Shims cut flush and not visible",
    "Cabinets don't interfere with range hood",
    ("Clearance above range adequate", "Clearance (in):"),
])

flow.append(guide("Typical: 18\" above counter, 54\" from floor."))
flow.append(d.FillInRow([("Actual height above counter (in):", 0.5),
                         ("Actual height from floor (in):", 0.5)]))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.6, label="Upper Cabinet Notes"))
flow.append(Spacer(1, 8))

flow += check_table("Cabinet Doors and Drawers", [
    "All doors align properly with each other",
    "Door reveals consistent (typically 1/16\")",
    "All doors open and close smoothly",
    "Door hinges adjusted properly",
    "Self-closing hinges function correctly",
    "All drawers operate smoothly",
    "Drawer fronts align with doors",
    "Soft-close mechanism works (if equipped)",
    "No binding or interference",
], notes_header="Notes")

# ---------------- SECTION 3
flow += d.h2("SECTION 3: CABINET HARDWARE & TRIM", S)
flow.append(d.checkbox_choice_row("Hardware Type:", ["Knobs", "Pulls", "Both"],
                                  S))
flow.append(d.FillIn("Finish:", height=26))
flow.append(Spacer(1, 6))

flow += check_table("Hardware Installation", [
    "Hardware template/jig used for consistency",
    "All hardware installed at consistent location",
    "Hardware properly aligned (vertical/horizontal)",
    "All screws tight and secure",
    "Hardware operates smoothly",
    "No scratches on hardware or cabinets",
], notes_header="Notes")

flow += check_table("Cabinet Trim & Filler Pieces", [
    "Filler pieces installed where needed",
    "Filler pieces cut to proper width",
    "Filler pieces match cabinet finish",
    "Crown molding installed (if applicable)",
    "Crown molding miters tight",
    "Crown molding secured properly",
    "Scribe molding installed (if applicable)",
    "Light rail molding (if applicable)",
    "End panels installed",
    ("Valance installed above sink", "Height (in):"),
    "All trim tight to cabinets/walls",
], notes_header="Location / Notes")

# ---------------- SECTION 4
flow += d.h2("SECTION 4: COUNTERTOP INSTALLATION", S)
flow.append(d.checkbox_choice_row(
    "Countertop Material:",
    ["Granite", "Quartz", "Laminate", "Butcher Block"], S))
flow.append(d.FillIn("Other:", height=26))
flow.append(d.FillInRow([("Color / Style:", 0.4), ("Thickness:", 0.28),
                         ("Edge Profile:", 0.32)]))
flow.append(Spacer(1, 6))

flow += check_table("Pre-Installation", [
    ("Template created and approved", "Template date:"),
    "Sink location verified",
    "Cooktop location verified (if applicable)",
    ("Faucet holes verified", "Configuration:"),
    "Cabinets confirmed level and secure",
], notes_header="Notes")

flow += check_table("Countertop Installation Checklist", [
    "Countertop level across all sections",
    ("Seams tight and aligned (if any)", "Seam locations:"),
    "Seam color match acceptable",
    ("Overhang correct at all edges", "Overhang (in):"),
    "Countertop properly supported",
    "Secured to cabinets appropriately",
    ("Sink cutout correct size", "Verified:"),
    "Sink properly sealed/caulked",
    ("Cooktop cutout correct (if applicable)", "Verified:"),
    "Faucet holes correct size and location",
    ("Backsplash height consistent", "Height (in):"),
    "Backsplash properly sealed at wall",
    "Backsplash sealed at counter joint",
    ("Countertop sealed (if stone)", "Sealer:"),
    "All edges finished properly",
    "No chips or damage",
])
flow.append(guide("Typical overhang: 1\" to 1.5\"."))
flow.append(guide("Typical backsplash: 4\" or full height."))

# ---------------- SECTION 5
flow += d.h2("SECTION 5: BATHROOM VANITY CABINETS", S)

flow += check_table("Master Bathroom Vanity", [
    "Vanity level (side to side)",
    "Vanity level (front to back)",
    "Vanity plumb",
    "Properly secured to wall studs",
    ("Height appropriate for users", "Height (in):"),
    "Doors and drawers operate smoothly",
    "Hardware installed correctly",
    ("Countertop / vanity top installed", "Material:"),
    "Countertop level",
    ("Sink(s) properly sealed", "Number of sinks:"),
    "Faucet holes correct",
    "Backsplash installed and sealed",
    "Top sealed (if stone)",
], notes_header="Notes")
flow.append(guide("Standard: 32\"–36\" to counter top."))

flow += data_table(
    "Additional Bathroom Vanities",
    ["Location", "Installed", "Level / Plumb", "Top Installed", "Sealed",
     "Complete"],
    [[Paragraph(r, S["cell"]), d.Checkbox(), d.Checkbox(), d.Checkbox(),
      d.Checkbox(), d.Checkbox()]
     for r in ["Bathroom 2", "Bathroom 3", "Powder Room"]],
    [1.9 * inch, 1.0 * inch, 1.15 * inch, 1.15 * inch, 0.9 * inch, 0.9 * inch],
    row_height=32,
    extra=[("ALIGN", (1, 2), (-1, -1), "CENTER")])

flow.append(d.WriteBox(1.6, label="Bathroom Vanity Notes"))

# ---------------- SECTION 6
flow += d.h2("SECTION 6: FINAL CABINET APPROVAL", S)

flow += check_table("Final Checklist", [
    "All kitchen base cabinets properly installed",
    "All kitchen upper cabinets properly installed",
    "All doors and drawers function correctly",
    "All hardware installed and functioning",
    "All trim and filler pieces installed",
    "Kitchen countertops installed correctly",
    "All bathroom vanities installed correctly",
    "All sinks properly sealed",
    "Stone countertops sealed (if applicable)",
    "No damage to cabinets or countertops",
    "All protective film/tape removed",
    "Cabinets cleaned and ready for use",
    "Care instructions received",
    "Warranty documentation collected",
    "Touch-up kit received (if applicable)",
], notes_header="Notes")

flow += data_table(
    "Issues / Punch List Items",
    ["Item / Issue", "Location", "Resolved", "Date"],
    [["", "", d.Checkbox(), ""] for _ in range(5)],
    [2.9 * inch, 2.0 * inch, 0.95 * inch, 1.15 * inch], row_height=32)

flow.append(d.WriteBox(2.2, label="Overall Comments"))
flow.append(Spacer(1, 10))

flow += d.signature_block([
    ("Installer Signature", True),
    ("Owner / Builder Approval", True),
])


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-5-finish-work",
                       "5.5-cabinet-installation-checklist.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
