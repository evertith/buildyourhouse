#!/usr/bin/env python3
"""6.4 Tool & Equipment Log — rebuilt on the 2026 design system.

Landscape: the tool register and rental ledger carry eight and nine columns.
In portrait, serial numbers, dates and dollar amounts all fall below the
half-inch of writing room the design review requires.

The browser-printed original leaked a stray copyright line and a duplicate
running header into the body on most pages, overprinting ledger rows — in one
place mid-sentence through a bullet ("...before leaving the rental yard —
document existing damage"). All of that production junk is dropped here.
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
FORM_ID = "6.4"
FORM_TITLE = "Tool & Equipment Log"


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


def small_set(options):
    return ChoiceSet(options, box=9, font_size=8.5, gap=6)


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="What tools are on site, who owns them, what condition they are "
            "in — and when rentals are due back.")

flow.append(Paragraph(
    "<b>PURPOSE:</b> Tools and equipment represent a significant investment "
    "and theft risk on construction sites. This log helps you track what tools "
    "are on site, who owns them, and their condition. For rental equipment, it "
    "helps you manage costs by tracking rental periods and ensuring timely "
    "returns.", S["body"]))
flow.append(Spacer(1, 4))

flow.append(Paragraph("Instructions", S["h3"]))
for line in [
    "Log all tools brought to the site, whether yours, borrowed, or rented",
    "Record serial numbers for valuable tools — essential for theft claims",
    "Note when tools are removed from site to avoid disputes about missing "
    "items",
    "For rentals, track start and return dates carefully to avoid extra "
    "charges",
    "Document tool condition to avoid liability for existing damage",
    "Update this log weekly at minimum, or whenever tools arrive/leave",
]:
    flow.append(Paragraph("• " + line, S["bullet"]))
flow.append(Spacer(1, 8))

flow.append(d.callout_box(
    "IMPORTANT — Tool Theft Prevention",
    [Paragraph(
        "Construction tool theft is extremely common. Lock up tools every "
        "night, mark valuable tools with your name or ID, photograph expensive "
        "equipment, and consider tool insurance. Document serial numbers for "
        "all power tools — you'll need them for police reports and insurance "
        "claims.", S["body"])], width=CW))

# ---------------- tools on site
flow += d.h2("TOOLS ON SITE", S)
flow.append(guide(
    "List all tools currently on your job site. Include power tools, hand "
    "tools, ladders, scaffolding, etc. Update when tools come and go."))

flow += data_table(
    "Tool Register",
    [shdr(h) for h in ["Tool Description", "Brand / Model", "Serial Number",
                       "Owner", "Date Brought to Site", "Date Removed",
                       "Condition", "Value"]],
    [["", "", "", small_set(["Mine", "Borrowed", "Rental"]), "", "",
      small_set(["Good", "Fair", "Poor"]), ""] for _ in range(12)],
    [1.6 * inch, 1.05 * inch, 1.05 * inch, 1.7 * inch, 0.95 * inch,
     0.9 * inch, 1.3 * inch, 0.95 * inch], row_height=42)

# ---------------- borrowed tools
flow += d.h2("BORROWED TOOLS", S)
flow.append(guide(
    "Keep detailed records of borrowed tools to ensure they're returned in "
    "good condition and disputes don't damage relationships."))

flow += data_table(
    "Borrowed Tool Register",
    [shdr(h) for h in ["Tool Description", "Borrowed From (Name)",
                       "Contact Info", "Date Borrowed",
                       "Condition When Borrowed", "Date Returned",
                       "Condition When Returned", "Returned"]],
    [["", "", "", "", "", "", "", d.Checkbox()] for _ in range(8)],
    [1.6 * inch, 1.3 * inch, 1.35 * inch, 0.95 * inch, 1.3 * inch,
     0.95 * inch, 1.3 * inch, 0.75 * inch], row_height=38,
    extra=[("ALIGN", (7, 2), (7, -1), "CENTER")])

# ---------------- rental equipment
flow += d.h2("RENTAL EQUIPMENT LOG", S)
flow.append(guide(
    "Track rental equipment carefully. Late returns can result in expensive "
    "extra charges. Rental companies charge by the day, week, or month — know "
    "your rental terms and plan accordingly."))

rental_rows = [["", "", "", "",
                [small_set(["Daily", "Weekly", "Monthly"]),
                 d.FillIn("$", font_size=9, height=18)],
                "", "", "", ""] for _ in range(6)]
rental_rows.append([Paragraph("TOTAL RENTAL EQUIPMENT COSTS:", S["cell-bold"]),
                    "", "", "", "", "", "", "",
                    Paragraph("$", S["cell-bold"])])

flow += data_table(
    "Rental Register",
    [shdr(h) for h in ["Equipment Type", "Rental Company",
                       "Rental Agreement #", "Start Date", "Rental Rate",
                       "Due Back Date", "Actual Return Date",
                       "Late Fees (if any)", "Total Cost"]],
    rental_rows,
    [1.25 * inch, 1.2 * inch, 1.05 * inch, 0.9 * inch, 1.5 * inch,
     0.9 * inch, 0.95 * inch, 0.85 * inch, 0.9 * inch],
    row_height=None, pad=8,
    extra=[("SPAN", (0, 8), (7, 8)),
           ("BACKGROUND", (0, 8), (-1, 8), d.SUBTOTAL_FILL)])

# ---------------- rental notes
flow += d.h2("RENTAL EQUIPMENT NOTES", S)

for _ in range(2):
    flow.append(CondPageBreak(3.6 * inch))
    flow.append(Paragraph("Rental Details & Issues", S["h3"]))
    flow.append(d.FillInRow([("Equipment:", 0.55),
                             ("Rental Agreement #:", 0.45)]))
    flow.append(d.WriteBox(0.9, label="Condition at Pickup"))
    flow.append(Spacer(1, 6))
    flow.append(d.WriteBox(0.9, label="Condition at Return"))
    flow.append(Spacer(1, 6))
    flow.append(choice("Any Damage Charges:", ["Yes", "No"]))
    flow.append(d.FillInRow([("Amount: $", 0.3), ("Description:", 0.7)]))
    flow.append(Spacer(1, 10))

flow.append(d.callout_box(
    "Rental Cost Saving Tips",
    bullets([
        "Understand rental periods — daily, 4-hour, weekly, monthly rates vary "
        "significantly",
        "Weekend rates are often cheaper — plan equipment use for "
        "Friday-Monday",
        "Return equipment as early as possible on the due date to avoid extra "
        "charges",
        "Inspect equipment carefully before leaving the rental yard — document "
        "existing damage",
        "Keep gas receipts if required to refuel equipment",
        "Consider buying vs. renting for tools you'll need throughout the "
        "project",
        "Compare prices between rental companies — rates vary widely",
    ]), width=CW))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-6-daily-operations",
                       "6.4-tool-equipment-log.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow, landscape=True)
    print(f"built {out}")
