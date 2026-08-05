#!/usr/bin/env python3
"""7.2 Receipt Organization System — filing method, category index, storage checklist."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 7: Budget & Expenses"
FORM_ID = "7.2"
FORM_TITLE = "Receipt Organization System"


def bullets(items, style=None):
    return [Paragraph(t, style or S["bullet"], bulletText="•") for t in items]


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="A filing method that keeps every receipt findable — for warranty "
            "claims, tax time, and disputes years after the build.")

flow.append(d.callout_box(
    "Why Receipt Organization Matters",
    [Paragraph("Proper receipt organization is essential for:", S["body"])] +
    bullets([
        "Tracking expenses accurately and staying within budget",
        "Warranty claims and returns",
        "Tax deductions and documentation for the IRS",
        "Insurance claims in case of loss or damage",
        "Resolving payment disputes with vendors",
        "Proving costs if you sell the property",
    ])))
flow.append(Spacer(1, 6))

# ---------------- instructions
flow += d.h2("RECEIPT ORGANIZATION INSTRUCTIONS", S)

flow.append(Paragraph("1. Label Envelopes or Folders by Month and Category",
                      S["h3"]))
flow.append(Paragraph(
    "Create a filing system using large envelopes, accordion folders, or a "
    "filing box. Label each section with:", S["body"]))
flow += bullets([
    'Month and Year (e.g., "January 2024")',
    "Budget Category (see list below)",
])
flow.append(Paragraph(
    'Example: "January 2024 - Foundation" or "March 2024 - Framing"',
    S["body"]))

flow.append(Paragraph("2. File Receipts Immediately", S["h3"]))
flow.append(Paragraph(
    "When you return from a purchase or receive a receipt:", S["body"]))
flow += bullets([
    "Record the expense in your Expense Tracking Sheet (Section 7.1) the "
    "same day",
    "Write the corresponding expense log entry number on the receipt",
    "File the receipt in the appropriate envelope/folder immediately",
    'Check the "Receipt Filed" box in your expense log',
    "Note the receipt location (envelope/folder label) in your expense log",
])

flow.append(Paragraph("3. Note Any Missing Receipts", S["h3"]))
flow.append(Paragraph("If you cannot locate a receipt:", S["body"]))
flow += bullets([
    'Mark "N" for Receipt Filed in your expense log',
    'Write "MISSING RECEIPT" in the Receipt Location column',
    "Try to obtain a duplicate from the vendor",
    "If unavailable, write a memo documenting the purchase (date, vendor, "
    "amount, items purchased)",
    "Attach credit card/bank statement showing the transaction",
])

flow.append(Paragraph("4. Digital Backup Recommended", S["h3"]))
flow.append(Paragraph("To protect against loss or damage:", S["body"]))
flow += bullets([
    "Scan or photograph all receipts (especially thermal receipts that fade)",
    "Store digital copies in organized folders on your computer or cloud "
    "storage",
    'Use the same naming convention: "2024-01-Foundation-Receipt-001.pdf"',
    "Back up digital files regularly to an external drive or cloud service",
])

# ---------------- category index
flow += d.h2("RECEIPT ORGANIZATION CATEGORIES", S)
flow.append(Paragraph(
    "Organize your receipts using these budget categories. Create a separate "
    "envelope or folder section for each, and tick it off once the folder "
    "exists.", S["body"]))
flow.append(Spacer(1, 4))

CATEGORY_ROWS = [
    ("Site Preparation", "Clearing, grading, excavation, driveway"),
    ("Foundation", "Concrete, rebar, forms, waterproofing, footer materials"),
    ("Framing", "Lumber, engineered beams, joists, sheathing, fasteners"),
    ("Roofing", "Shingles, underlayment, drip edge, vents, flashing"),
    ("Exterior", "Siding, windows, doors, trim, house wrap"),
    ("Rough-In", "Plumbing pipes, electrical wire, HVAC equipment, fixtures"),
    ("Insulation", "Fiberglass batts, spray foam, rigid foam boards"),
    ("Drywall", "Drywall sheets, joint compound, tape, screws"),
    ("Flooring", "Hardwood, tile, carpet, underlayment, adhesives"),
    ("Cabinets", "Kitchen cabinets, bathroom vanities, countertops"),
    ("Fixtures", "Sinks, toilets, faucets, light fixtures, appliances"),
    ("Paint", "Interior paint, exterior paint, primer, brushes, rollers"),
    ("Permits", "Building permits, inspection fees, impact fees"),
    ("Other", "Landscaping, garage door, miscellaneous hardware"),
]

header = ["", Paragraph("Category", S["cell-bold"]),
          Paragraph("Examples of Items/Services", S["cell-bold"])]
rows = [[d.Checkbox(), Paragraph(name, S["cell"]),
         Paragraph(examples, S["cell"])]
        for name, examples in CATEGORY_ROWS]
flow.append(d.titled_table(
    "Folder Index", header, rows,
    [0.42 * inch, 1.5 * inch, CW - 0.42 * inch - 1.5 * inch], S,
    row_heights=[26] * len(rows)))

# ---------------- storage checklist
flow += d.h2("RECEIPT STORAGE CHECKLIST", S)
flow.append(d.items_checklist([
    "Envelopes or folders labeled with month and category",
    "All receipts filed within 24 hours of purchase",
    "Receipt numbers match expense log entries",
    "Missing receipts documented with memos and statements",
    "Digital backup system established",
    "Receipts scanned or photographed weekly",
    "Digital files backed up to cloud or external drive",
    "Receipt storage kept in secure, dry location",
    "All receipts retained for at least 7 years after project completion",
], S))

flow.append(Spacer(1, 10))
flow.append(d.WriteBox(3.2, label="NOTES"))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-7-budget-expenses",
                       "7.2-receipt-organization-system.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
