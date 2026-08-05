#!/usr/bin/env python3
"""7.3 Cost Overrun Analysis — two repeatable overrun post-mortems."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, Spacer, Table, TableStyle

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 7: Budget & Expenses"
FORM_ID = "7.3"
FORM_TITLE = "Cost Overrun Analysis"

REASONS = [
    "Underestimated material costs",
    "Underestimated labor costs",
    "Material price increases after initial budget",
    "Scope creep (added features or upgraded materials)",
    "Design changes or corrections",
    "Unforeseen site conditions",
    "Mistakes or rework required",
    "Code requirements not initially considered",
    "Weather delays increasing costs",
]

IMPACTS = [
    "Absorbed by contingency fund",
    "Requires cuts in other categories (list below)",
    "Requires additional financing",
]


def bullets(items, style=None):
    return [Paragraph(t, style or S["bullet"], bulletText="•") for t in items]


def two_col_checklist(items):
    """Check-all-that-apply list in two columns — half the height of a stack,
    and these options are read as a set rather than in sequence."""
    box_w = 0.42 * inch
    text_w = (CW - 0.2 * inch) / 2 - box_w
    half = (len(items) + 1) // 2
    left, right = items[:half], items[half:]
    rows = []
    for i in range(half):
        r = [d.Checkbox(), Paragraph(left[i], S["cell"]), ""]
        if i < len(right):
            r += [d.Checkbox(), Paragraph(right[i], S["cell"])]
        else:
            r += ["", ""]
        rows.append(r)
    t = Table(rows, colWidths=[box_w, text_w, 0.2 * inch, box_w, text_w])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 5),
        ("LEFTPADDING", (4, 0), (4, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def boxed_pair(left_label, right_label, height_in=1.5):
    """Two labelled write-boxes side by side. The label is a wrapping
    Paragraph, so it can run longer than the box is wide."""
    col = (CW - 0.2 * inch) / 2

    def cell(label):
        return [Paragraph(label, S["cell-bold"]), Spacer(1, 3),
                d.WriteBox(height_in)]

    t = Table([[cell(left_label), "", cell(right_label)]],
              colWidths=[col, 0.2 * inch, col])
    t.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return t


def other_row(label="Other:"):
    """A drawn checkbox followed by a labelled writing rule."""
    t = Table([[d.Checkbox(), d.FillIn(label)]],
              colWidths=[0.42 * inch, CW - 0.42 * inch],
              rowHeights=[d.WRITE_ROW_PT])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 6),
    ]))
    return t


def financials(n):
    # "Financial Details" is the table's title; the row-label column is headed
    # "Item" so the phrase does not appear twice, one line above itself.
    header = [Paragraph("Item", S["cell-bold"]),
              Paragraph("Amount ($)", S["cell-bold"])]
    rows = [[Paragraph(t, S["cell"]), ""] for t in (
        "Original Budget Amount",
        "Current Actual Cost",
        "Overrun Amount",
        "Percentage Over Budget (%)",
    )]
    return d.titled_table("Financial Details", header, rows,
                          [CW - 2.6 * inch, 2.6 * inch], S,
                          row_heights=[d.WRITE_ROW_PT] * len(rows))


def overrun_form(n):
    out = []
    out += d.h2(f"COST OVERRUN ANALYSIS #{n}", S)
    # Identity fields and the money table are one unit; never let the four-row
    # table strand a single line on the next page.
    out.append(KeepTogether([
        d.FillInRow([("Budget Category:", 0.55),
                     ("Date Overrun Identified:", 0.45)]),
        Spacer(1, 6),
        financials(n),
    ]))

    out.append(Paragraph("Reason for Overrun (check all that apply)", S["h3"]))
    out.append(two_col_checklist(REASONS))
    out.append(other_row())

    out.append(Paragraph("Detailed Explanation", S["h3"]))
    out.append(d.WriteBox(1.6))

    out.append(Paragraph("Could It Have Been Prevented?", S["h3"]))
    out.append(d.checkbox_choice_row("", ["Yes", "No", "Partially"], S))
    out.append(Spacer(1, 4))
    out.append(boxed_pair(
        "If yes or partially, how could it have been prevented?",
        "Lesson Learned"))

    out.append(Paragraph("Impact on Total Budget", S["h3"]))
    out.append(d.items_checklist(IMPACTS, S))
    out.append(other_row())
    out.append(Spacer(1, 4))
    out.append(boxed_pair("Budget Categories to be Reduced (if applicable)",
                          "Action Plan Moving Forward"))
    return out


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="A post-mortem for every budget category that blows past its "
            "allocation.")

flow.append(d.callout_box(
    "Purpose of Cost Overrun Analysis",
    [Paragraph(
        "When expenses exceed your budget, it's critical to document and "
        "analyze what happened. This analysis helps you:", S["body"])] +
    bullets([
        "Understand the true financial impact of the overrun",
        "Identify root causes and prevent future budget issues",
        "Make informed decisions about adjustments to other categories",
        "Learn valuable lessons for future projects",
        "Communicate clearly with lenders or partners about budget changes",
    ])))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>WHEN TO USE THIS FORM:</b> Complete a Cost Overrun Analysis whenever a "
    "budget category exceeds its allocated amount by more than 5%.", S["body"]))

flow += overrun_form(1)
flow += overrun_form(2)

flow += d.h2("ADDITIONAL NOTES", S)
flow.append(d.WriteBox(2.6))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-7-budget-expenses",
                       "7.3-cost-overrun-analysis.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
