#!/usr/bin/env python3
"""6.2 Weather Delay Log — rebuilt on the 2026 design system.

The browser-printed original leaked a stray copyright line and a duplicate
running header into the body of most pages, overprinting the tracking table.
All of that production junk is dropped here.
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
CW = d.content_width()

SECTION = "Section 6: Daily Operations"
FORM_ID = "6.2"
FORM_TITLE = "Weather Delay Log"


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


def blank_rows(n, ncols):
    return [[""] * ncols for _ in range(n)]


def choice(label, options):
    return d.checkbox_choice_row(label, options, S)


def guide(text):
    return Paragraph(text, S["note"])


def bullets(items):
    return [Paragraph("• " + t, S["body"]) for t in items]


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Weather days, who they stopped, what they cost and how the "
            "schedule recovers.")

flow.append(Paragraph(
    "<b>PURPOSE:</b> Weather delays are one of the most common causes of "
    "construction schedule changes. This log helps you track weather-related "
    "delays, document their impact on your project timeline, and plan recovery "
    "strategies. This documentation is valuable for insurance claims, lender "
    "updates, and managing subcontractor schedules.", S["body"]))
flow.append(Spacer(1, 4))

flow.append(Paragraph("Instructions", S["h3"]))
for line in [
    "Record any day when weather prevents or significantly delays work (even "
    "partial days)",
    "Be specific about weather conditions — \"heavy rain\" is better than "
    "\"bad weather\"",
    "Document which trades/tasks were affected — some work can continue in "
    "certain weather",
    "Track cumulative delays to understand total schedule impact",
    "Note any costs incurred due to weather delays (extended equipment "
    "rentals, etc.)",
    "Update your master schedule when weather causes significant delays",
]:
    flow.append(Paragraph("• " + line, S["bullet"]))
flow.append(Spacer(1, 8))

flow.append(d.callout_box(
    "Common Weather Conditions That Delay Construction",
    bullets([
        "<b>Rain</b> — affects concrete pours, roofing, exterior painting, "
        "drywall delivery",
        "<b>Snow/Ice</b> — affects all outdoor work, material deliveries, "
        "site access",
        "<b>Extreme Cold</b> — affects concrete curing, paint application, "
        "some materials",
        "<b>Extreme Heat</b> — affects worker safety, some material "
        "installation",
        "<b>High Winds</b> — affects roofing, siding, crane operations, safety",
        "<b>Mud/Site Conditions</b> — even after rain stops, site may be "
        "unusable",
    ])))
flow.append(Spacer(1, 12))

flow += d.h2("PROJECT WEATHER DELAY SUMMARY", S)
flow.append(d.FillInRow([("Project Name:", 0.5), ("Project Address:", 0.5)]))
flow.append(d.FillInRow([("Original Completion Date:", 0.5),
                         ("Current Projected Completion:", 0.5)]))
flow.append(d.FillInRow([("Total Weather Delay Days to Date:", 0.5),
                         ("Schedule Impact (days):", 0.5)]))

# ---------------- tracking log
flow += d.h2("WEATHER DELAY TRACKING LOG", S)
flow += data_table(
    "Delay Tracking",
    [shdr(h) for h in ["Date", "Weather Condition", "Temp / Wind",
                       "Work Affected", "Delay (Days)", "Impact on Schedule",
                       "Make-Up Plan"]],
    blank_rows(24, 7),
    [0.75 * inch, 1.15 * inch, 0.8 * inch, 1.5 * inch, 0.65 * inch,
     0.9 * inch, 1.25 * inch], row_height=34)

# ---------------- costs
flow += d.h2("WEATHER-RELATED COSTS", S)
flow.append(guide(
    "Track any costs directly attributed to weather delays, such as extended "
    "equipment rentals, rescheduling fees, or additional labor costs."))

cost_rows = [["", "", "", "", "",
              ChoiceSet(["Insurance", "Warranty", "No"], box=9, font_size=8.5,
                        gap=6)] for _ in range(5)]
cost_rows.append([Paragraph("TOTAL WEATHER-RELATED COSTS:", S["cell-bold"]),
                  "", "", "", Paragraph("$", S["cell-bold"]), ""])

flow += data_table(
    "Cost Record",
    [shdr(h) for h in ["Date", "Description of Cost",
                       "Related to Weather Event", "Vendor / Contractor",
                       "Amount", "Recoverable?"]],
    cost_rows,
    [0.8 * inch, 1.75 * inch, 1.4 * inch, 1.3 * inch, 0.75 * inch,
     1.0 * inch], row_height=None, pad=10,
    extra=[("SPAN", (0, 7), (3, 7)),
           ("BACKGROUND", (0, 7), (-1, 7), d.SUBTOTAL_FILL)])

# ---------------- monthly summary
flow += d.h2("MONTHLY WEATHER DELAY SUMMARY", S)
flow.append(guide(
    "Summarize weather delays by month to identify patterns and seasons with "
    "highest impact. This helps with planning future projects."))

flow += data_table(
    "Monthly Summary",
    [shdr(h) for h in ["Month / Year", "Total Delay Days",
                       "Primary Weather Issues", "Most Affected Trades",
                       "Notes / Lessons Learned"]],
    blank_rows(12, 5),
    [1.0 * inch, 0.95 * inch, 1.7 * inch, 1.45 * inch, 1.9 * inch],
    row_height=34)

# ---------------- schedule adjustments
flow += d.h2("SCHEDULE ADJUSTMENT NOTES", S)
flow.append(guide(
    "Use this section to document how you've adjusted your master schedule due "
    "to accumulated weather delays, and communicate these changes to "
    "stakeholders."))

for _ in range(2):
    flow.append(CondPageBreak(4.2 * inch))
    flow.append(Paragraph("Schedule Adjustment Record", S["h3"]))
    flow.append(d.FillIn("Date of Adjustment:", height=26))
    flow.append(d.WriteBox(1.0, label="Reason"))
    flow.append(Spacer(1, 6))
    flow.append(d.WriteBox(1.2, label="Changes Made"))
    flow.append(Spacer(1, 6))
    flow.append(choice("Stakeholders Notified:",
                       ["Lender", "Subcontractors", "Inspector"]))
    flow.append(d.FillIn("Other:", height=26))
    flow.append(Spacer(1, 10))

flow.append(d.callout_box(
    "Tips for Managing Weather Delays",
    bullets([
        "Monitor weather forecasts and plan accordingly",
        "Build weather contingency time into your original schedule "
        "(10-15% is typical)",
        "Have indoor tasks ready to work on during bad weather days",
        "Protect materials and work-in-progress from weather damage",
        "Communicate schedule impacts to subcontractors immediately",
        "Take photos of weather conditions causing delays for documentation",
        "Review your insurance policy to understand weather-related coverage",
    ])))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-6-daily-operations",
                       "6.2-weather-delay-log.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
