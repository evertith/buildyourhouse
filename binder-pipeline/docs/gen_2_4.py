#!/usr/bin/env python3
"""2.4 Payment Draw Schedule — 2026 design system."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Flowable, PageBreak, Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 2: Contracts & Legal Documents"
FORM_ID = "2.4"
FORM_TITLE = "Payment Draw Schedule"

DISCLAIMER = ("Template for general reference — have your attorney review before "
              "use. Not legal advice.")

BULLET = ParagraphStyle("bullet2", parent=S["bullet"], bulletFontName=d.BODY,
                        bulletFontSize=10.5)

DRAW_COLS = [3.3 * inch, 1.7 * inch, 2.0 * inch]


# ---------------------------------------------------------------- local components
# Built here rather than in design.py, per the rebuild brief.

class FieldLine(Flowable):
    """One ruled entry line: optional drawn checkbox, label, a drawn rule to the
    right margin, and optional tail text sitting after the rule."""

    def __init__(self, text, box=False, rule=True, tail=None, rule_w=None,
                 indent=0, font_size=10.5, box_size=16, height=None):
        super().__init__()
        self.text = text
        self.box = box
        self.rule = rule
        self.tail = tail
        self.rule_w = rule_w
        self.indent = indent
        self.font_size = font_size
        self.box_size = box_size
        self._height = height

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self.height = self._height or (d.WRITE_ROW_PT if self.rule else 24.5)
        return self.width, self.height

    def draw(self):
        d.register_fonts()
        c = self.canv
        baseline = 9
        x = self.indent
        c.setFillColor(d.INK)
        c.setStrokeColor(d.INK)
        if self.box:
            c.setLineWidth(1)
            c.rect(x, baseline - 4, self.box_size, self.box_size)
            # 18pt gutter keeps the label aligned with d.items_checklist rows
            x += self.box_size + 18
        c.setFont(d.BODY, self.font_size)
        if self.text:
            c.drawString(x, baseline, self.text)
            x += c.stringWidth(self.text, d.BODY, self.font_size) + 6
        if self.rule:
            if self.rule_w:
                right = x + self.rule_w
                if self.tail:
                    c.drawString(right + 8, baseline, self.tail)
            else:
                right = self.width
                if self.tail:
                    tw = c.stringWidth(self.tail, d.BODY, self.font_size)
                    c.drawString(self.width - tw, baseline, self.tail)
                    right = self.width - tw - 6
            c.setLineWidth(0.75)
            c.line(x, baseline - 2, right, baseline - 2)


def two_col_checklist(items):
    """Checklist in two columns — same drawn box and row pitch as
    d.items_checklist, half the vertical space."""
    from reportlab.platypus import Table, TableStyle
    col = (CW - 2 * 0.42 * inch) / 2
    rows = []
    for i in range(0, len(items), 2):
        pair = items[i:i + 2]
        row = [d.Checkbox(), Paragraph(pair[0], S["cell"])]
        row += ([d.Checkbox(), Paragraph(pair[1], S["cell"])] if len(pair) > 1
                else ["", ""])
        rows.append(row)
    t = Table(rows, colWidths=[0.42 * inch, col, 0.42 * inch, col],
              rowHeights=[24.5] * len(rows))
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 4),
        ("LEFTPADDING", (3, 0), (3, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def money_table(title, retention_label, balance_fixed=None):
    """The nine-line draw arithmetic. Bold rows are the ones that carry forward."""
    lines = [
        ("Labor", False),
        ("Materials", False),
        ("Equipment", False),
        ("Subtotal This Draw", True),
        (retention_label, False),
        ("Amount Due This Draw", True),
        ("Previous Payments", False),
        ("Total Paid to Date", True),
        ("Contract Balance Remaining", True),
    ]
    rows, heights, bold_rows = [], [], []
    for i, (label, strong) in enumerate(lines):
        style = S["cell-bold"] if strong else S["cell"]
        amount = ""
        if balance_fixed is not None and label == "Contract Balance Remaining":
            amount = Paragraph(balance_fixed, S["cell-bold"])
        rows.append([Paragraph(label, style), amount, ""])
        heights.append(d.WRITE_ROW_PT)
        if strong:
            bold_rows.append(i)
    t = d.titled_table(
        title,
        [Paragraph("Description", S["cell-bold"]),
         Paragraph("Amount ($)", S["cell-bold"]),
         Paragraph("Notes", S["cell-bold"])],
        rows, DRAW_COLS, S, row_heights=heights)
    t.setStyle(d.TableStyle(
        [("BACKGROUND", (0, i + 2), (0, i + 2), d.SUBTOTAL_FILL)
         for i in bold_rows]))
    return t


def draw_block(number, title, retention_label, final=False):
    out = [PageBreak()]
    out += d.h2(title, S)
    out.append(d.FillInRow([("Draw Date:", 0.5),
                            ("Percentage Complete (%):", 0.5)]))
    out.append(d.WriteBox(1.0, label="Work Completed This Period"))
    out.append(Spacer(1, 6))
    out.append(money_table(f"Draw {number} — Amount Calculation", retention_label,
                           balance_fixed="0.00" if final else None))
    out.append(Spacer(1, 6))

    if final:
        out.append(Paragraph("Final Payment Requirements — ALL must be checked",
                             S["body-bold"]))
        out.append(two_col_checklist([
            "Unconditional final lien waiver received",
            "All supplier / subcontractor lien waivers received",
            "Final inspection passed",
            "All punch list items completed",
            "Warranties and manuals received",
            "All required permits closed out",
        ]))
    else:
        out.append(Paragraph("Lien Waivers Received", S["body-bold"]))
        out.append(d.items_checklist([
            "Conditional lien waiver submitted",
            "Unconditional lien waiver for previous payment",
            "Supplier lien waivers attached",
        ], S))
        out.append(Spacer(1, 4))
        out.append(d.checkbox_choice_row(
            "INSPECTION:", ["Passed", "Not yet required", "Failed (see notes)"], S))

    out.append(Spacer(1, 4))
    out.append(d.FillInRow([("Inspector:", 0.28), ("Date:", 0.20),
                            ("Payment Date:", 0.30), ("Check #:", 0.22)]))
    out += d.signature_block([("Owner Signature", True)])
    return out


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Five draws from first payment to final release — what was completed, "
            "what is owed, what is retained, and the waivers and inspections "
            "required before the cheque is written.")
flow.append(Paragraph(DISCLAIMER, S["note"]))
flow.append(Spacer(1, 4))

flow.append(d.FillIn("Project Name:"))
flow.append(d.FillIn("Project Address:"))
flow.append(d.FillInRow([("Owner:", 0.5), ("Subcontractor / Trade:", 0.5)]))
flow.append(d.FillInRow([("Original Contract Amount ($):", 0.55),
                         ("Retention Percentage (%):", 0.45)]))

flow.append(Spacer(1, 8))

# Overview of all five draws. Added in the rebuild: without it page 1 carried
# only the project fields and sat two-thirds empty.
flow.append(d.titled_table(
    "Draw Summary — all five draws at a glance",
    [Paragraph(t, S["cell-bold"]) for t in
     ("Draw #", "Date", "% Complete", "Amount Due ($)", "Date Paid", "Check #")],
    [[str(n), "", "", "", "", ""] for n in range(1, 6)]
    + [[Paragraph("TOTAL", S["cell-bold"]), "", "", "", "", ""]],
    [0.8 * inch, 1.15 * inch, 1.1 * inch, 1.45 * inch, 1.25 * inch, 1.25 * inch],
    S))
flow.append(Spacer(1, 10))

flow.append(d.callout_box(
    "Before releasing any draw", [
        Paragraph("Verify the work claimed is actually in place, collect the "
                  "lien waiver covering the previous payment, and confirm any "
                  "inspection required at this stage has passed. Retention is "
                  "held from every draw until final completion.", S["body"])]))

for n, (title, retention, final) in enumerate([
    ("DRAW 1", "Less Retention", False),
    ("DRAW 2", "Less Retention", False),
    ("DRAW 3", "Less Retention", False),
    ("DRAW 4", "Less Retention", False),
    ("DRAW 5 — FINAL PAYMENT", "Plus Retention Release", True),
], start=1):
    flow += draw_block(n, title, retention, final=final)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-2-contracts-legal",
                       "2.4-payment-draw-schedule.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
