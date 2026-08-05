#!/usr/bin/env python3
"""7.4 Payment Tracking — subcontractor draw schedules and lien waiver status."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import Flowable, KeepTogether, Paragraph, Spacer, Table, TableStyle

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 7: Budget & Expenses"
FORM_ID = "7.4"
FORM_TITLE = "Payment Tracking"

SUBCONTRACTOR_BLOCKS = 5

DRAWS = [
    "Draw 1 (Deposit/Start)",
    "Draw 2 (Progress)",
    "Draw 3 (Progress)",
    "Final Payment",
]


class YesNo(Flowable):
    """Drawn 'Y / N' box pair sized for a narrow table cell."""

    WIDTH = 38

    def __init__(self, box=9, font_size=8, gap=5):
        super().__init__()
        self.box = box
        self.font_size = font_size
        self.gap = gap

    def wrap(self, availWidth, availHeight):
        self.width = self.WIDTH
        self.height = self.box + 4
        return self.width, self.height

    def draw(self):
        d.register_fonts()
        c = self.canv
        c.setStrokeColor(d.INK)
        c.setFillColor(d.INK)
        c.setLineWidth(0.9)
        x = 0
        for label in ("Y", "N"):
            c.rect(x, 2, self.box, self.box)
            x += self.box + 2
            c.setFont(d.BODY, self.font_size)
            c.drawString(x, 4, label)
            x += c.stringWidth(label, d.BODY, self.font_size) + self.gap


def bullets(items, style=None):
    return [Paragraph(t, style or S["bullet"], bulletText="•") for t in items]


def payment_table(n):
    """std_table rather than titled_table: the block heading directly above
    already names this table, and the whole block is held in a KeepTogether so
    there is no split for a repeating title row to protect against."""
    header = [Paragraph(h, S["cell-bold"]) for h in (
        "Payment", "Date", "Amount ($)", "Paid?", "Check #",
        "Lien Waiver Received?", "Notes")]
    rows = [[Paragraph(label, S["cell"]), "", "", YesNo(), "", YesNo(), ""]
            for label in DRAWS]
    rows.append([Paragraph("TOTAL PAID ($)", S["cell-bold"]), "", "", "",
                 Paragraph("BALANCE OWED ($)", S["cell-bold"]), "", ""])
    # Payment column holds "Draw 1 (Deposit/Start)" on one line, so no body row
    # wraps and every row sits at the 29pt handwriting height. That keeps the
    # block under half a page, so two subcontractors share a sheet.
    # 1.15in on the lien column sets "Lien Waiver / Received?" on two lines
    # rather than three, which is what buys the second block its page space.
    col = [1.65 * inch, 0.78 * inch, 0.78 * inch, 0.62 * inch, 0.72 * inch,
           1.15 * inch, 1.30 * inch]
    t = d.std_table([header] + rows, col, header_rows=1,
                    row_heights=[None] + [d.WRITE_ROW_PT] * len(rows))
    t.setStyle(TableStyle([
        ("LEFTPADDING", (3, 0), (3, -1), 3),
        ("RIGHTPADDING", (3, 0), (3, -1), 3),
        ("LEFTPADDING", (5, 0), (5, -1), 3),
        ("RIGHTPADDING", (5, 0), (5, -1), 3),
        ("ALIGN", (3, 1), (3, -2), "CENTER"),
        ("ALIGN", (5, 1), (5, -2), "CENTER"),
        # totals band: label, writing room, label, writing room
        ("SPAN", (0, -1), (1, -1)),
        ("SPAN", (2, -1), (3, -1)),
        ("SPAN", (4, -1), (5, -1)),
        ("BACKGROUND", (0, -1), (-1, -1), d.SUBTOTAL_FILL),
        ("LINEABOVE", (0, -1), (-1, -1), 1.5, d.INK),
    ]))
    return t


def payment_block(n):
    """One subcontractor per block, kept whole so the heading never strands."""
    return [KeepTogether([
        Paragraph(f"Subcontractor Payment Tracking #{n}", S["h3"]),
        d.FillInRow([("Subcontractor Name:", 0.6), ("Trade:", 0.4)]),
        d.FillInRow([("Contract Date:", 0.45),
                     ("Total Contract Amount ($):", 0.55)]),
        Spacer(1, 6),
        payment_table(n),
        Spacer(1, 8),
        Paragraph("Work Completion Status Before Final Payment:",
                  S["body-bold"]),
        d.checkbox_choice_row("", [
            "All work completed per contract",
            "Punch list items completed",
            "Final inspection passed",
        ], S, 12, 9.5),
        Spacer(1, 12),
    ])]


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Every draw, check number and lien waiver, tracked per "
            "subcontractor.")

flow.append(d.callout_box(
    "Importance of Payment Tracking",
    [Paragraph("Tracking subcontractor payments is essential for:", S["body"])] +
    bullets([
        "Managing cash flow and ensuring funds are available when needed",
        "Protecting against mechanic's liens by obtaining lien waivers",
        "Verifying work completion before releasing payments",
        "Maintaining professional relationships with subcontractors",
        "Documenting payment history in case of disputes",
    ])))
flow.append(Spacer(1, 8))

flow.append(d.callout_box(
    "⚠ CRITICAL — Lien Waiver Best Practices",
    bullets([
        "<b>Never make a payment without receiving a lien waiver</b>",
        "For progress payments: obtain \"Conditional Waiver and Release Upon "
        "Progress Payment\" before paying",
        "For final payment: obtain \"Unconditional Waiver and Release Upon "
        "Final Payment\" before paying",
        "Keep all lien waivers in Section 3 (Subcontractor Management)",
        "Verify subcontractor has paid their suppliers before releasing final "
        "payment",
    ])))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>INSTRUCTIONS:</b> Use the forms below to track all payments to "
    "subcontractors. Update immediately when payments are made.", S["body"]))

for i in range(1, SUBCONTRACTOR_BLOCKS + 1):
    flow += payment_block(i)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-7-budget-expenses",
                       "7.4-payment-tracking.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
