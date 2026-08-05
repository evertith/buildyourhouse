#!/usr/bin/env python3
"""6.3 Material Delivery & Storage Log — rebuilt on the 2026 design system.

Landscape: the delivery ledger carries nine columns, and portrait cannot give
"Quantity", "Cost" and "Storage Location" the half-inch of writing room the
design review requires.

The browser-printed original leaked a stray copyright line and a duplicate
running header into the body on most pages, overprinting ledger rows. All of
that production junk is dropped here.
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
CW = d.content_width(landscape=True)

SECTION = "Section 6: Daily Operations"
FORM_ID = "6.3"
FORM_TITLE = "Material Delivery & Storage Log"


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


def keep_for(n_rows, row_height=34, cap=3.0 * inch, floor=1.9 * inch):
    est = 68 + n_rows * (row_height or 34)
    return est if est <= cap else floor


def data_table(title, headers, rows, col_widths, row_height=34, pad=None,
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
    return d.checkbox_choice_row(label, options, S)


def guide(text):
    return Paragraph(text, S["note"])


def bullets(items):
    return [Paragraph("• " + t, S["body"]) for t in items]


INV_COLS = [2.2 * inch, 1.4 * inch, 2.4 * inch, 1.9 * inch, 1.6 * inch]
INV_HEADERS = [shdr(h) for h in
               ["Material Type", "Quantity on Hand", "Location on Site",
                "Condition", "Need to Order More?"]]


def _cond():
    return ChoiceSet(["Good", "Needs Protection"], box=9, font_size=8.5, gap=6)


def _order():
    return ChoiceSet(["Yes", "No"], box=9, font_size=8.5, gap=6)


def inventory_master(groups):
    """All material categories as one continuous ledger with banded category
    rows. Separate per-category tables stranded up to 40% of a landscape page
    each time one refused to split.
    """
    rows, heights, cmds = [], [], []
    for title, materials, blanks in groups:
        r = len(rows) + 2
        rows.append([Paragraph(title, S["cell-bold"]), "", "", "", ""])
        heights.append(24)
        cmds += [("SPAN", (0, r), (-1, r)),
                 ("BACKGROUND", (0, r), (-1, r), d.SUBTOTAL_FILL)]
        for m in materials:
            rows.append([Paragraph(m, S["cell"]), "", "", _cond(), _order()])
            heights.append(38)
        for _ in range(blanks):
            rows.append(["", "", "", _cond(), _order()])
            heights.append(38)
    t = d.titled_table("On-Site Inventory", INV_HEADERS, rows, INV_COLS, S,
                       row_heights=heights)
    t.setStyle(TableStyle(HEADER_PAD + cmds))
    return [CondPageBreak(1.7 * inch), t, Spacer(1, 8)]


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="What arrived, when, in what condition, where it went and when it "
            "was used — plus a running count of what is still on site.")

flow.append(Paragraph(
    "<b>PURPOSE:</b> Keeping accurate records of material deliveries and "
    "on-site inventory is critical for cost control, project scheduling, and "
    "preventing theft or loss. This log helps you track what arrives, when it "
    "arrives, its condition, where it's stored, and when it's used.",
    S["body"]))
flow.append(Spacer(1, 4))

flow.append(Paragraph("Instructions", S["h3"]))
for line in [
    "Log every material delivery immediately upon arrival — don't wait until "
    "later",
    "Inspect all deliveries for damage or shortages before the driver leaves",
    "Note storage location so you (and your subs) can easily find materials "
    "later",
    "Cross-reference purchase orders and invoices to verify accuracy",
    "Update the \"Used On\" date when materials are installed or consumed",
    "Use the Current Inventory section to track what's on site at any given "
    "time",
    "Take photos of damaged deliveries immediately for insurance/return "
    "purposes",
]:
    flow.append(Paragraph("• " + line, S["bullet"]))
flow.append(Spacer(1, 8))

flow.append(d.callout_box(
    "Delivery Inspection Checklist",
    bullets([
        "Count all items before driver leaves",
        "Check for damage to materials or packaging",
        "Verify items match purchase order and packing slip",
        "Note any shortages or wrong items immediately",
        "Get driver's signature on damage/shortage notes",
        "Contact supplier same day about any issues",
    ]), width=CW))

# ---------------- delivery log
flow += d.h2("MATERIAL DELIVERY LOG", S)
flow += data_table(
    "Deliveries Received",
    [shdr(h) for h in ["Date Received", "Supplier", "Items Delivered",
                       "Quantity", "PO Number", "Condition",
                       "Storage Location", "Cost", "Used On (Date)"]],
    [["", "", "", "", "",
      ChoiceSet(["Good", "Damaged", "Short"], box=9, font_size=8.5, gap=6),
      "", "", ""] for _ in range(20)],
    [0.75 * inch, 1.0 * inch, 1.55 * inch, 0.75 * inch, 0.75 * inch,
     1.65 * inch, 1.25 * inch, 0.8 * inch, 1.0 * inch], row_height=38)

# ---------------- delivery issues
flow += d.h2("DAMAGED OR SHORT DELIVERIES", S)
flow.append(guide(
    "Document any delivery issues in detail. This is critical for getting "
    "replacements or credits from suppliers."))

flow.append(Paragraph("Delivery Issue Report", S["h3"]))
flow.append(d.FillInRow([("Date:", 0.3), ("Supplier:", 0.45), ("PO #:", 0.25)]))
flow.append(choice("Issue:",
                   ["Damaged", "Short Quantity", "Wrong Item", "Other"]))
flow.append(d.WriteBox(1.1, label="Description"))
flow.append(Spacer(1, 6))
flow.append(choice("Driver Notified:", ["Yes", "No"]))
flow.append(d.FillIn("Driver Signature:", height=28))
flow.append(choice("Supplier Contacted:", ["Yes", "No"]))
flow.append(d.FillInRow([("Contact Person:", 0.6), ("Date:", 0.4)]))
flow.append(choice("Resolution:",
                   ["Replacement Scheduled", "Credit Issued", "Pending"]))
flow.append(choice("Photo Taken:", ["Yes", "No"]))
flow.append(d.FillIn("Photo Numbers:", height=28))

# ---------------- inventory
flow += d.h2("CURRENT INVENTORY ON SITE", S)
flow.append(guide(
    "Use this section to track what materials are currently on your job site. "
    "Update regularly, especially before ordering more materials. This "
    "prevents over-ordering and helps you locate materials quickly."))
flow.append(d.FillInRow([("Inventory Last Updated:", 0.5),
                         ("Updated By:", 0.5)]))
flow.append(Spacer(1, 8))

flow += inventory_master([
    ("FRAMING MATERIALS",
     ["2x4 Studs", "2x6 Studs", "Plywood/OSB Sheathing"], 1),
    ("CONCRETE & MASONRY", ["Rebar", "Concrete Blocks"], 1),
    ("ROOFING MATERIALS",
     ["Shingles/Roofing Material", "Underlayment"], 1),
    ("WINDOWS & DOORS", ["Windows", "Exterior Doors", "Interior Doors"], 0),
    ("DRYWALL & INSULATION",
     ["Drywall Sheets", "Insulation Batts", "Joint Compound"], 0),
    ("FLOORING MATERIALS", ["Hardwood Flooring", "Tile", "Carpet"], 0),
    ("ELECTRICAL & PLUMBING",
     ["Wire/Romex", "PEX/Copper Pipe", "Fixtures"], 0),
    ("OTHER MATERIALS", [], 4),
])

flow.append(d.callout_box(
    "Material Storage Best Practices",
    bullets([
        "Keep lumber elevated and covered — moisture is the enemy",
        "Store drywall flat and dry — moisture ruins drywall quickly",
        "Protect windows and doors in original packaging until installation",
        "Keep electrical and plumbing materials secure — small items walk off "
        "easily",
        "Store paint and chemicals in temperature-controlled areas",
        "Label storage areas so subcontractors can find materials",
        "Lock up high-value items when site is unattended",
        "Take photos of material storage areas regularly",
    ]), width=CW))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-6-daily-operations",
                       "6.3-material-delivery-storage-log.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow, landscape=True)
    print(f"built {out}")
