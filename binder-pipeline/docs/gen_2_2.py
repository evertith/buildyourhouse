#!/usr/bin/env python3
"""2.2 Change Order Form — 2026 design system."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Flowable, KeepTogether, Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 2: Contracts & Legal Documents"
FORM_ID = "2.2"
FORM_TITLE = "Change Order Form"

DISCLAIMER = ("Template for general reference — have your attorney review before "
              "use. Not legal advice.")

BULLET = ParagraphStyle("bullet2", parent=S["bullet"], bulletFontName=d.BODY,
                        bulletFontSize=10.5)


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


def bullets(items, style=None, bullet="•"):
    return [Paragraph(t, style or BULLET, bulletText=bullet) for t in items]


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Every change to an agreed scope — priced, scheduled and signed by "
            "both parties before the work is done. Unsigned changes do not get "
            "paid.")
flow.append(Paragraph(DISCLAIMER, S["note"]))
flow.append(Spacer(1, 4))

flow.append(d.FillInRow([("Change Order Number:", 0.5), ("Date:", 0.5)]))

# ---------------- project information
flow += d.h2("PROJECT INFORMATION", S)
flow.append(d.FillIn("Project Address:"))
flow.append(d.FillIn("Owner Name:"))
flow.append(d.FillInRow([("Subcontractor / Trade:", 0.58),
                         ("Original Contract Date:", 0.42)]))

# ---------------- financial summary
flow += d.h2("FINANCIAL SUMMARY", S)
fin_items = [
    "Original Contract Amount",
    "Previous Change Orders (total)",
    "Revised Contract Amount (before this change order)",
    "This Change Order Amount",
    "New Contract Amount (including this change order)",
]
flow.append(d.titled_table(
    "Contract Value",
    [Paragraph("Item", S["cell-bold"]), Paragraph("Amount ($)", S["cell-bold"])],
    [[Paragraph(t, S["cell"]), ""] for t in fin_items],
    [4.6 * inch, 2.4 * inch], S, row_heights=[d.WRITE_ROW_PT] * len(fin_items)))
flow.append(Spacer(1, 8))
flow.append(d.checkbox_choice_row("This change order is an (check one):",
                                  ["Addition (+)", "Deduction (–)"], S))

# ---------------- description of change
flow += d.h2("DESCRIPTION OF CHANGE", S)
flow.append(d.WriteBox(
    2.5, label="Detailed description of work to be added, deleted, or modified"))

# ---------------- reason for change
flow += d.h2("REASON FOR CHANGE", S)
flow.append(Paragraph("Check all that apply:", S["body"]))
flow.append(d.items_checklist([
    "Owner-requested modification",
    "Design change",
    "Unforeseen site conditions",
    "Code requirement / inspector request",
    "Material substitution / unavailability",
    "Correction of error or omission",
    "Upgrade / enhancement",
    "Value engineering",
], S))
flow.append(FieldLine("Other:", box=True))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.6, label="Detailed explanation"))

# ---------------- cost breakdown
flow += d.h2("COST BREAKDOWN", S)

BAND, WRITE, SUB = 22, d.WRITE_ROW_PT, 26
cost_rows, cost_heights, band_idx, sub_idx = [], [], [], []


def band(label):
    band_idx.append(len(cost_rows))
    cost_rows.append([Paragraph(label, S["cell-bold"]), "", ""])
    cost_heights.append(BAND)


def write_rows(n):
    for _ in range(n):
        cost_rows.append(["", "", ""])
        cost_heights.append(WRITE)


def subtotal(label):
    sub_idx.append(len(cost_rows))
    cost_rows.append([Paragraph(label, S["cell-bold"]), "", ""])
    cost_heights.append(SUB)


band("LABOR")
write_rows(3)
subtotal("Labor Subtotal")
band("MATERIALS")
write_rows(4)
subtotal("Materials Subtotal")
band("EQUIPMENT / OTHER")
write_rows(2)
subtotal("Equipment Subtotal")
total_row = len(cost_rows)
cost_rows.append([Paragraph("TOTAL COST IMPACT", S["cell-bold"]), "", ""])
cost_heights.append(28)

cost_table = d.titled_table(
    "Cost Impact of This Change Order",
    [Paragraph("Description", S["cell-bold"]),
     Paragraph("Quantity", S["cell-bold"]),
     Paragraph("Cost ($)", S["cell-bold"])],
    cost_rows, [4.0 * inch, 1.4 * inch, 1.6 * inch], S,
    row_heights=cost_heights)
cmds = []
for i in band_idx:
    r = i + 2
    cmds += [("SPAN", (0, r), (-1, r)),
             ("BACKGROUND", (0, r), (-1, r), d.SUBTOTAL_FILL)]
for i in sub_idx:
    r = i + 2
    cmds.append(("BACKGROUND", (0, r), (1, r), d.SUBTOTAL_FILL))
tr = total_row + 2
cmds += [("BACKGROUND", (0, tr), (1, tr), d.SUBTOTAL_FILL),
         ("LINEABOVE", (0, tr), (-1, tr), 1.5, d.INK)]
cost_table.setStyle(d.TableStyle(cmds))
flow.append(cost_table)

# ---------------- schedule impact
flow += d.h2("SCHEDULE IMPACT", S)
flow.append(d.FillInRow([("Original Completion Date:", 0.5),
                         ("New Completion Date:", 0.5)]))
flow.append(FieldLine("Schedule impact (+ or – days):", rule_w=90))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.35, label="Explanation of schedule impact"))

# ---------------- impact on other trades
flow += d.h2("IMPACT ON OTHER TRADES", S)
flow.append(d.checkbox_choice_row(
    "Check one:", ["No impact on other trades", "Impacts other trades"], S))
flow.append(Spacer(1, 4))
flow.append(d.FillIn("Trades affected:"))
flow.append(d.WriteBox(1.35, label="If other trades are impacted, explain"))

# ---------------- supporting documentation
flow += d.h2("SUPPORTING DOCUMENTATION", S)
flow.append(Paragraph("Attached documents (check all that apply):", S["body"]))
flow.append(d.items_checklist([
    "Revised drawings / sketches",
    "Material quotes / invoices",
    "Photos of conditions requiring change",
    "Inspector notes / requirements",
    "Engineer specifications",
], S))
flow.append(FieldLine("Other:", box=True))

# ---------------- payment terms
flow += d.h2("PAYMENT TERMS FOR THIS CHANGE ORDER", S)
flow.append(Paragraph("Check one:", S["body"]))
flow.append(FieldLine("Payment due with next regular draw", box=True, rule=False))
flow.append(FieldLine("Payment upon completion of change order work", box=True,
                      rule=False))
flow.append(FieldLine("Payment in installments:", box=True))
flow.append(FieldLine("Other:", box=True))

# ---------------- approvals
flow += d.h2("APPROVALS AND SIGNATURES", S)
flow.append(Paragraph(
    "By signing below, both parties agree to the changes described in this "
    "Change Order and acknowledge that this Change Order modifies the original "
    "contract accordingly.", S["body"]))
flow.append(Spacer(1, 6))
flow.append(KeepTogether([
    Paragraph("Owner Approval", S["h3"]),
    *d.signature_block([("Signature", True)]),
    d.FillIn("Print Name:"),
]))
flow.append(Spacer(1, 10))
flow.append(KeepTogether([
    Paragraph("Subcontractor Approval", S["h3"]),
    *d.signature_block([("Signature", True)]),
    d.FillInRow([("Print Name:", 0.5), ("Company:", 0.5)]),
]))
flow.append(Spacer(1, 10))
flow.append(d.WriteBox(1.4, label="NOTES"))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-2-contracts-legal",
                       "2.2-change-order-form.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
