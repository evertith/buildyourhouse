#!/usr/bin/env python3
"""7.5 Final Budget Reconciliation — closing accounting for the whole project."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, Spacer, Table, TableStyle

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 7: Budget & Expenses"
FORM_ID = "7.5"
FORM_TITLE = "Final Budget Reconciliation"

CATEGORIES = [
    "Site Preparation", "Foundation", "Framing", "Roofing",
    "Exterior (Siding, Windows, Doors)",
    "Rough-In (Plumbing, Electrical, HVAC)", "Insulation", "Drywall",
    "Flooring", "Cabinets &amp; Countertops",
    "Fixtures (Plumbing, Lighting, etc.)", "Paint &amp; Finishes",
    "Permits &amp; Fees", "Tools &amp; Equipment", "Labor (Subcontractors)",
    "Contingency (Used/Unused)", "Other",
]


def bullets(items, style=None):
    return [Paragraph(t, style or S["bullet"], bulletText="•") for t in items]


def boxed_pair(left_label, right_label, height_in=1.5):
    """Two labelled write-boxes side by side; labels wrap as Paragraphs."""
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


def top_five(title, item_header, money_header, reason_header):
    header = [Paragraph(h, S["cell-bold"]) for h in
              ("Rank", item_header, money_header, reason_header)]
    rows = [[Paragraph(f"{i}.", S["cell"]), "", "", ""] for i in range(1, 6)]
    return d.titled_table(
        title, header, rows,
        [0.55 * inch, 2.40 * inch, 1.35 * inch, 2.70 * inch], S,
        row_heights=[d.WRITE_ROW_PT] * len(rows))


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="The closing set of books for the build — estimated against actual, "
            "category by category.")

flow.append(d.callout_box(
    "Purpose of Final Budget Reconciliation",
    [Paragraph(
        "This final accounting document provides a complete financial picture "
        "of your owner-builder project. Use it to:", S["body"])] +
    bullets([
        "Document the total project cost for future reference",
        "Identify where you stayed on budget and where you went over",
        "Extract valuable lessons for future building projects",
        "Provide accurate cost data if you sell the property",
        "Support tax filings and potential deductions",
    ])))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>WHEN TO COMPLETE:</b> Fill in this reconciliation when all work is "
    "finished and all invoices have been paid.", S["body"]))

# ---------------- project overview
flow += d.h2("PROJECT OVERVIEW", S)
flow.append(d.FillIn("Project Address:"))
flow.append(d.FillInRow([("Project Start Date:", 0.5),
                         ("Project Completion Date:", 0.5)]))
flow.append(d.FillInRow([("Total Duration (months):", 0.5),
                         ("Square Footage Built:", 0.5)]))

# ---------------- category reconciliation
flow += d.h2("FINAL BUDGET SUMMARY", S)
summary_header = [Paragraph(h, S["cell-bold"]) for h in
                  ("Budget Category", "Estimated Budget ($)",
                   "Actual Cost ($)", "Variance +/- ($)")]
summary_rows = [[Paragraph(c, S["cell"]), "", "", ""]
                for c in CATEGORIES + ["<b>TOTAL PROJECT COST</b>"]]
money_w = (CW - 2.05 * inch) / 3
summary = d.titled_table(
    "Estimated vs. Actual by Category", summary_header, summary_rows,
    [2.05 * inch] + [money_w] * 3, S,
    row_heights=[d.WRITE_ROW_PT] * len(summary_rows))
summary.setStyle(TableStyle([
    ("BACKGROUND", (0, -1), (-1, -1), d.SUBTOTAL_FILL),
    ("LINEABOVE", (0, -1), (-1, -1), 1.5, d.INK),
]))
flow.append(summary)

# ---------------- headline numbers
flow += d.h2("FINAL BUDGET ANALYSIS", S)
flow.append(d.FillInRow([("Total Estimated Budget ($):", 0.5),
                         ("Total Actual Cost ($):", 0.5)]))
flow.append(d.FillInRow([("Total Variance +/- ($):", 0.5),
                         ("Cost Per Square Foot ($):", 0.5)]))
flow.append(d.FillIn("Percentage Variance (%) — circle one: over / under budget:"))
flow.append(Spacer(1, 8))

flow.append(KeepTogether(top_five(
    "Biggest Cost Overruns (Top 5)", "Category/Item",
    "Amount Over Budget ($)", "Primary Reason")))
flow.append(Spacer(1, 10))
flow.append(KeepTogether(top_five(
    "Biggest Cost Savings (Top 5)", "Category/Item",
    "Amount Saved ($)", "How Savings Achieved")))

# ---------------- retrospective
flow += d.h2("LESSONS LEARNED FOR FUTURE PROJECTS", S)
flow.append(boxed_pair("1. Budgeting", "2. Cost Control"))
flow.append(boxed_pair("3. Vendor/Subcontractor Selection",
                       "4. Areas to Allocate More Budget Next Time"))
flow.append(Paragraph("5. Overall Financial Advice for Future Owner-Builders",
                      S["cell-bold"]))
flow.append(Spacer(1, 3))
flow.append(d.WriteBox(3.4))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-7-budget-expenses",
                       "7.5-final-budget-reconciliation.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
