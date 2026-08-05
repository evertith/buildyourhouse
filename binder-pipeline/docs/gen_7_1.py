#!/usr/bin/env python3
"""7.1 Expense Tracking Sheets — daily expense ledger, monthly summary, analysis."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import Flowable, Paragraph, Spacer, Table, TableStyle

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 7: Budget & Expenses"
FORM_ID = "7.1"
FORM_TITLE = "Expense Tracking Sheets"

# Blank ledger lines. Sized to fill roughly three pages so the sheet can be
# photocopied as often as the build needs.
LEDGER_ROWS = 52

CATEGORIES = [
    "Site Preparation", "Foundation", "Framing", "Roofing",
    "Exterior (Siding, Windows, Doors)",
    "Rough-In (Plumbing, Electrical, HVAC)", "Insulation", "Drywall",
    "Flooring", "Cabinets &amp; Countertops",
    "Fixtures (Plumbing, Lighting, etc.)", "Paint &amp; Finishes",
    "Permits &amp; Fees", "Tools &amp; Equipment", "Labor (Subcontractors)",
    "Contingency", "Other",
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


def money_table(title, rows, money_headers, first_header, first_width):
    """Category-down / money-across table. The '$' lives in the column header,
    never loose in the cells."""
    header = [Paragraph(first_header, S["cell-bold"])] + \
        [Paragraph(h, S["cell-bold"]) for h in money_headers]
    money_w = (CW - first_width) / len(money_headers)
    col = [first_width] + [money_w] * len(money_headers)
    body = [[Paragraph(r, S["cell"])] + [""] * len(money_headers) for r in rows]
    t = d.titled_table(title, header, body, col, S,
                       row_heights=[d.WRITE_ROW_PT] * len(body))
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, -1), (-1, -1), d.SUBTOTAL_FILL),
        ("LINEABOVE", (0, -1), (-1, -1), 1.5, d.INK),
    ]))
    return t


def action_rows(n):
    """Drawn checkbox + writing rule, for open-ended action items."""
    rows = [[d.Checkbox(), d.FillIn("")] for _ in range(n)]
    t = Table(rows, colWidths=[0.42 * inch, CW - 0.42 * inch],
              rowHeights=[d.WRITE_ROW_PT] * n)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 6),
    ]))
    return t


def note_pair(left_label, right_label, height_in=1.35):
    """Two labelled write-boxes side by side — twice the writing room of a
    stacked pair in the same vertical space."""
    col = (CW - 0.2 * inch) / 2
    t = Table([[d.WriteBox(height_in, label=left_label), "",
                d.WriteBox(height_in, label=right_label)]],
              colWidths=[col, 0.2 * inch, col])
    t.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="A running ledger for every dollar that leaves the project, plus a "
            "month-end roll-up against your budget.")

flow.append(d.FillIn("Month:", width=3.4 * inch))
flow.append(Spacer(1, 6))

flow.append(Paragraph(
    "<b>INSTRUCTIONS:</b> Record every purchase immediately. Keep this binder "
    "on-site or readily accessible. File receipts daily.", S["body"]))
flow.append(Spacer(1, 4))

flow.append(d.callout_box(
    "Budget Categories",
    [Paragraph(
        "Site Prep · Foundation · Framing · Roofing · Exterior · Rough-In "
        "(Plumbing/Electrical/HVAC) · Insulation · Drywall · Flooring · "
        "Cabinets/Countertops · Fixtures · Paint/Finishes · Permits/Fees · "
        "Tools/Equipment · Labor · Contingency · Other", S["body"])]))
flow.append(Spacer(1, 10))

# ---------------- daily ledger
ledger_header = [
    Paragraph("Date", S["cell-bold"]),
    Paragraph("Vendor", S["cell-bold"]),
    Paragraph("Description", S["cell-bold"]),
    Paragraph("Budget Category", S["cell-bold"]),
    Paragraph("Amount ($)", S["cell-bold"]),
    Paragraph("Payment Method", S["cell-bold"]),
    Paragraph("Receipt Filed?", S["cell-bold"]),
    Paragraph("Receipt Location", S["cell-bold"]),
]
ledger_cols = [0.55 * inch, 1.05 * inch, 1.35 * inch, 0.85 * inch,
               0.78 * inch, 0.82 * inch, 0.72 * inch, 0.88 * inch]
ledger_rows = [["", "", "", "", "", "", YesNo(), ""]
               for _ in range(LEDGER_ROWS)]

ledger = d.titled_table("Detailed Expense Log", ledger_header, ledger_rows,
                        ledger_cols, S,
                        row_heights=[d.WRITE_ROW_PT] * LEDGER_ROWS)
ledger.setStyle(TableStyle([
    ("LEFTPADDING", (6, 1), (6, -1), 3),
    ("RIGHTPADDING", (6, 1), (6, -1), 3),
    ("ALIGN", (6, 2), (6, -1), "CENTER"),
]))
flow.append(ledger)

# ---------------- month-end roll-up
flow += d.h2("MONTHLY SUMMARY", S)
flow.append(Paragraph(
    "Total every category at month end and compare it against the budget you "
    "set in Section 1.", S["body"]))
flow.append(Spacer(1, 4))
flow.append(money_table(
    "Spending by Budget Category",
    CATEGORIES + ["<b>TOTAL</b>"],
    ["Budgeted Amount ($)", "Spent This Month ($)", "Total Spent to Date ($)"],
    "Budget Category", 2.05 * inch))

flow += d.h2("MONTHLY SUMMARY ANALYSIS", S)
flow.append(d.FillInRow([("Month:", 0.5), ("Total Spent This Month ($):", 0.5)]))
flow.append(d.FillInRow([("Budget Remaining ($):", 0.4),
                         ("Percentage of Total Budget Used (%):", 0.6)]))
flow.append(Spacer(1, 8))

flow += d.h2("NOTES AND OBSERVATIONS", S)
flow.append(note_pair("Categories Over Budget This Month",
                      "Categories Under Budget This Month"))
flow.append(note_pair("Unexpected Expenses",
                      "Cost-Saving Measures Implemented"))
flow.append(d.WriteBox(1.35, label="Projected Expenses for Next Month"))

flow.append(Paragraph("Action Items", S["h3"]))
flow.append(action_rows(5))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-7-budget-expenses",
                       "7.1-expense-tracking-sheets.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
