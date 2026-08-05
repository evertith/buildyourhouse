#!/usr/bin/env python3
"""2.5 Warranty Tracking Sheet — 2026 design system."""

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
FORM_ID = "2.5"
FORM_TITLE = "Warranty Tracking Sheet"

DISCLAIMER = ("Template for general reference — have your attorney review before "
              "use. Not legal advice.")

BULLET = ParagraphStyle("bullet2", parent=S["bullet"], bulletFontName=d.BODY,
                        bulletFontSize=10.5)

# Item / Manufacturer / Installer / Install Date / Warranty Period / Expiration
WCOLS = [1.55 * inch, 1.15 * inch, 1.15 * inch, 0.95 * inch, 1.05 * inch,
         1.15 * inch]


# ---------------------------------------------------------------- local components
# Built here rather than in design.py, per the rebuild brief.

class ChoiceGroups(Flowable):
    """Two or more 'LABEL [ ] A [ ] B' groups sharing one line — the yes/no
    pairs that would otherwise each burn a full row."""

    def __init__(self, groups, box=13, font_size=10.5, gap=34, height=22):
        super().__init__()
        self.groups = groups
        self.box = box
        self.font_size = font_size
        self.gap = gap
        self._height = height

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self.height = self._height
        return self.width, self.height

    def draw(self):
        d.register_fonts()
        c = self.canv
        baseline = 6
        x = 0
        c.setFillColor(d.INK)
        c.setStrokeColor(d.INK)
        for gi, (label, opts) in enumerate(self.groups):
            if gi:
                x += self.gap
            if label:
                c.setFont(d.BOLD, self.font_size)
                c.drawString(x, baseline, label)
                x += c.stringWidth(label, d.BOLD, self.font_size) + 10
            for opt in opts:
                c.setLineWidth(1)
                c.rect(x, baseline - 3, self.box, self.box)
                x += self.box + 5
                c.setFont(d.BODY, self.font_size)
                c.drawString(x, baseline, opt)
                x += c.stringWidth(opt, d.BODY, self.font_size) + 14


def bullets(items, style=None, bullet="•"):
    return [Paragraph(t, style or BULLET, bulletText=bullet) for t in items]


def warranty_table(title, items):
    """items: list of row labels; blank strings give free write-in rows."""
    header = [Paragraph(t, S["cell-bold"]) for t in
              ("Item / System", "Manufacturer", "Installer", "Install Date",
               "Warranty Period", "Expiration")]
    rows = [[Paragraph(it, S["cell"]) if it else "", "", "", "", "", ""]
            for it in items]
    return d.titled_table(title, header, rows, WCOLS, S,
                          row_heights=[d.WRITE_ROW_PT] * len(rows))


def category(heading, table_title, items, extras=(), notes=False, trailing=()):
    out = d.h2(heading, S)
    out.append(warranty_table(f"{table_title} — warranty details", items))
    out.append(Spacer(1, 8))
    out.extend(extras)
    out.append(d.FillIn("Documentation Location:"))
    out.append(ChoiceGroups([("Registration Required:", ["Yes", "No"]),
                             ("Completed:", ["Yes", "No"])]))
    out.append(Spacer(1, 4))
    out.append(d.FillInRow([("Contact for Claims:", 0.62), ("Phone:", 0.38)]))
    if notes:
        out.append(d.FillIn("Notes:"))
    out.extend(trailing)
    return out


def extended_warranty_row():
    return ChoiceGroups([("Extended Warranty Purchased:", ["Yes", "No"])])


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Every warranty on the house in one place — who covers it, for how "
            "long, when it expires, and where the paperwork lives.")
flow.append(Paragraph(DISCLAIMER, S["note"]))
flow.append(Spacer(1, 4))

flow.append(d.FillIn("Project Name:"))
flow.append(d.FillIn("Project Address:"))
flow.append(d.FillInRow([("Owner:", 0.62), ("Date Started:", 0.38)]))
flow.append(Spacer(1, 4))
flow.append(Paragraph(
    "Use this form to track all warranties for materials, equipment, and "
    "workmanship. Keep all warranty documentation in a safe location and note "
    "where it is stored.", S["body"]))

flow += category("STRUCTURAL &amp; FOUNDATION", "Structural &amp; Foundation", [
    "Foundation", "Waterproofing", "Framing", "Engineered Lumber"])

flow += category("ROOFING SYSTEM", "Roofing System", [
    "Roofing Shingles", "Underlayment", "Flashing", "Installation Labor"],
    notes=True)

flow += category("WINDOWS &amp; DOORS", "Windows &amp; Doors", [
    "Windows", "Entry Doors", "Garage Doors", "Patio Doors"])

flow += category("HVAC SYSTEM", "HVAC System", [
    "Furnace / Heater", "Air Conditioner", "Heat Pump", "Ductwork",
    "Thermostat", "Installation Labor"],
    extras=[d.FillIn("Model Numbers:"), d.FillIn("Serial Numbers:")],
    trailing=[extended_warranty_row(),
              d.FillIn("Extended warranty expires:")])

flow += category("PLUMBING", "Plumbing", [
    "Water Heater", "Plumbing Fixtures", "Faucets", "Installation Labor"])

flow += category("ELECTRICAL", "Electrical", [
    "Electrical Panel", "Light Fixtures", "Ceiling Fans", "Installation Labor"])

flow += category("APPLIANCES", "Appliances", [
    "Refrigerator", "Range / Oven", "Dishwasher", "Microwave", "Washer",
    "Dryer"],
    extras=[d.FillIn("Model / Serial Numbers:")],
    trailing=[extended_warranty_row(),
              d.FillIn("Extended warranty expires:")])

flow += category("FLOORING &amp; FINISHES", "Flooring &amp; Finishes", [
    "Hardwood Flooring", "Tile", "Carpet", "Countertops", "Cabinets"])

flow += d.h2("ADDITIONAL ITEMS", S)
flow.append(warranty_table("Additional Items — warranty details",
                           ["", "", "", ""]))

flow += d.h2("IMPORTANT NOTES", S)
flow.append(d.callout_box(None, bullets([
    "Register all products requiring registration within 30 days of installation",
    "Keep all warranty documents in a fireproof safe or safety deposit box",
    "Make copies of all warranty documents for this binder",
    "Note any maintenance requirements that must be performed to keep warranty "
    "valid",
    "Keep receipts and invoices with warranty documents",
    "Set calendar reminders for warranty expiration dates",
])))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-2-contracts-legal",
                       "2.5-warranty-tracking-sheet.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
