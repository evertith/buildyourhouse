#!/usr/bin/env python3
"""2.6 Material Delivery Receipt — 2026 design system."""

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
FORM_ID = "2.6"
FORM_TITLE = "Material Delivery Receipt"

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
                 indent=0, font_size=10.5, box_size=16, gutter=18, height=None):
        super().__init__()
        self.text = text
        self.box = box
        self.rule = rule
        self.tail = tail
        self.rule_w = rule_w
        self.indent = indent
        self.font_size = font_size
        self.box_size = box_size
        self.gutter = gutter
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
            # gutter 18 aligns with d.items_checklist, 5 with checkbox_choice_row
            x += self.box_size + self.gutter
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
    purpose="Sign nothing until it is counted. Record what arrived, what "
            "condition it arrived in, and what the supplier owes you — before "
            "the driver leaves.")
flow.append(Paragraph(DISCLAIMER, S["note"]))
flow.append(Spacer(1, 4))

flow.append(d.FillInRow([("Delivery Date:", 0.5), ("Time:", 0.5)]))
flow.append(d.FillIn("Project Address:"))
flow.append(d.FillIn("Owner Name:"))

# ---------------- supplier
flow += d.h2("SUPPLIER INFORMATION", S)
flow.append(d.FillIn("Supplier / Vendor Name:"))
flow.append(d.FillIn("Address:"))
flow.append(d.FillInRow([("Phone:", 0.45), ("Email:", 0.55)]))
flow.append(d.FillInRow([("Purchase Order #:", 0.36), ("Invoice #:", 0.32),
                         ("Account #:", 0.32)]))

# ---------------- delivery
flow += d.h2("DELIVERY INFORMATION", S)
flow.append(d.FillIn("Delivery Company:"))
flow.append(d.FillInRow([("Driver Name:", 0.64), ("Truck #:", 0.36)]))
flow.append(Paragraph("Delivery Method (check one):", S["body-bold"]))
flow.append(d.checkbox_choice_row(
    None, ["Flatbed truck", "Box truck", "Pickup truck"], S))
flow.append(d.checkbox_choice_row(None, ["Boom truck", "Crane"], S))
flow.append(FieldLine("Other:", box=True, box_size=13, gutter=5))

# ---------------- materials
flow += d.h2("MATERIALS DELIVERED", S)
mat_rows = [[str(n), "", "", "", ""] for n in range(1, 13)]
mat_table = d.titled_table(
    "Materials Received",
    [Paragraph("#", S["cell-bold"]),
     Paragraph("Description / Item", S["cell-bold"]),
     Paragraph("Qty Ordered", S["cell-bold"]),
     Paragraph("Qty Received", S["cell-bold"]),
     Paragraph("Unit (ea, box, bundle, etc.)", S["cell-bold"])],
    mat_rows,
    [0.45 * inch, 3.0 * inch, 0.95 * inch, 0.95 * inch, 1.65 * inch], S)
mat_table.setStyle(d.TableStyle([("ALIGN", (0, 2), (0, -1), "CENTER")]))
flow.append(mat_table)

# ---------------- condition
flow += d.h2("CONDITION ASSESSMENT", S)
flow.append(Paragraph("Overall Condition (check one):", S["body-bold"]))
flow.append(FieldLine("Excellent — no damage, all items as ordered", box=True,
                      rule=False))
flow.append(FieldLine("Good — minor cosmetic issues that do not affect function",
                      box=True, rule=False))
flow.append(FieldLine("Fair — some damage noted, usable but may need discount / "
                      "credit", box=True, rule=False))
flow.append(FieldLine("Poor — significant damage, items not usable, return / "
                      "replacement required", box=True, rule=False))
flow.append(Spacer(1, 6))

dmg_rows = [["", "", d.checkbox_choice_row(
    None, ["Return", "Replace", "Credit"], S, box=11, font_size=8.5)]
    for _ in range(5)]
flow.append(d.titled_table(
    "Specific Damage or Issues",
    [Paragraph("Item #", S["cell-bold"]),
     Paragraph("Description of Damage", S["cell-bold"]),
     Paragraph("Action Required", S["cell-bold"])],
    dmg_rows, [0.7 * inch, 3.3 * inch, 3.0 * inch], S,
    row_heights=[d.WRITE_ROW_PT] * len(dmg_rows)))
flow.append(Spacer(1, 8))

flow.append(Paragraph("Discrepancies (check all that apply):", S["body-bold"]))
flow.append(d.items_checklist([
    "Items missing from order (list below)",
    "Wrong items delivered (list below)",
    "Quantity discrepancies (noted in table above)",
    "No discrepancies",
], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.35, label="Details"))
flow.append(Spacer(1, 6))
flow.append(d.checkbox_choice_row("Photos taken:", ["Yes", "No"], S))
flow.append(FieldLine("Number of photos:", rule_w=90))

# ---------------- storage
flow += d.h2("STORAGE INFORMATION", S)
flow.append(d.FillIn("Storage Location on Site:"))
flow.append(KeepTogether([
    Paragraph("Storage Conditions:", S["body-bold"]),
    d.items_checklist([
        "Covered / protected from weather",
        "Level surface",
        "Off ground (elevated on blocking / pallets)",
        "Secured / locked area",
    ], S),
    FieldLine("Other:", box=True)]))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.0, label="Special Handling Notes"))

# ---------------- follow-up
flow += d.h2("FOLLOW-UP REQUIRED", S)
flow.append(d.items_checklist([
    "No follow-up needed — delivery complete and correct",
    "Contact supplier regarding damage (within 24 hours)",
    "Request replacement items",
    "Request credit / refund for damaged items",
], S))
flow.append(FieldLine("Back-ordered items expected on:", box=True))
flow.append(FieldLine("Other:", box=True))
flow.append(Spacer(1, 4))
flow.append(d.FillInRow([("Supplier contact for issues — Name:", 0.62),
                         ("Phone:", 0.38)]))

# ---------------- notes
flow += d.h2("NOTES", S)
flow.append(d.WriteBox(2.2))

# ---------------- signatures
flow += d.h2("SIGNATURES", S)
flow.append(Paragraph(
    "By signing below, all parties acknowledge the delivery and condition of "
    "materials as documented above.", S["body"]))
flow.append(Spacer(1, 6))
flow.append(KeepTogether([
    Paragraph("Received by (Owner or Authorized Representative)", S["h3"]),
    *d.signature_block([("Signature", True)]),
    d.FillIn("Print Name:"),
]))
flow.append(Spacer(1, 10))
flow.append(KeepTogether([
    Paragraph("Delivered by (Driver)", S["h3"]),
    *d.signature_block([("Signature", True)]),
    d.FillIn("Print Name:"),
]))
flow.append(Spacer(1, 10))
flow.append(d.callout_box("IMPORTANT", bullets([
    "Inspect all materials immediately upon delivery",
    "Note any damage or discrepancies on this form AND on the driver's delivery "
    "ticket",
    "Take photos of any damaged items before the driver leaves",
    "Contact supplier within 24 hours of delivery to report any issues",
    "Keep this form with your project documentation",
    "Attach copies of purchase order, invoice, and driver's delivery ticket",
])))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-2-contracts-legal",
                       "2.6-material-delivery-receipt.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
