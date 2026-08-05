#!/usr/bin/env python3
"""8.4 Emergency Contacts — the call list that lives at the job site entrance."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 8: Quick Reference Guides"
FORM_ID = "8.4"
FORM_TITLE = "Emergency Contacts"


def contact_table(title, headers, rows, widths):
    """Rows carry either a known number or blank writing room; every row sits
    at the handwriting height so the sheet can be filled in on site."""
    header = [Paragraph(h, S["cell-bold"]) for h in headers]
    body = []
    for r in rows:
        body.append([Paragraph(c, S["cell"]) if c else "" for c in r])
    return KeepTogether(
        d.titled_table(title, header, body, widths, S,
                       row_heights=[d.WRITE_ROW_PT] * len(body)))


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Every number you would need in a hurry, on one sheet.")

flow.append(d.callout_box(
    "⚠ IN AN EMERGENCY, CALL 911 FIRST",
    [Paragraph(
        "Keep this list updated and posted visibly at your job site. Include "
        "after-hours contact numbers where available. In case of emergency, "
        "call 911 first, then notify the appropriate contacts below.",
        S["body"])]))
flow.append(Spacer(1, 10))

flow.append(contact_table(
    "Emergency Services", ["Service", "Phone Number"],
    [("Emergency (Fire/Medical/Police)", "<b>911</b>"),
     ("Poison Control Center", "<b>1-800-222-1222</b>"),
     ("Police (Non-Emergency)", ""),
     ("Fire Department (Non-Emergency)", ""),
     ("Hospital/Urgent Care", "")],
    [2.60 * inch, CW - 2.60 * inch]))
flow.append(Spacer(1, 10))

flow.append(contact_table(
    "Building Department &amp; Inspectors",
    ["Contact", "Name", "Phone Number"],
    [("Building Inspector", "", ""),
     ("Electrical Inspector", "", ""),
     ("Plumbing Inspector", "", ""),
     ("Mechanical Inspector", "", ""),
     ("Building Dept Main Line", "", "")],
    [2.10 * inch, 2.45 * inch, CW - 4.55 * inch]))
flow.append(Spacer(1, 10))

flow.append(contact_table(
    "Utility Companies", ["Utility", "Company Name", "Phone Number"],
    [("Electric Company", "", ""),
     ("Gas Company", "", ""),
     ("Water/Sewer Company", "", ""),
     ("Telephone/Internet", "", ""),
     ("Utility Location Service (811)", "Call Before You Dig", "<b>811</b>")],
    [2.10 * inch, 2.45 * inch, CW - 4.55 * inch]))
flow.append(Spacer(1, 10))

flow.append(contact_table(
    "Insurance &amp; Project Contacts",
    ["Contact Type", "Name/Company", "Phone Number"],
    [("Homeowner's Insurance Agent", "", ""),
     ("Builder's Risk Insurance", "", ""),
     ("Project Architect/Engineer", "", ""),
     ("General Contractor (if any)", "", "")],
    [2.10 * inch, 2.45 * inch, CW - 4.55 * inch]))
flow.append(Spacer(1, 10))

flow.append(contact_table(
    "Subcontractor Emergency Contacts",
    ["Trade", "Company/Name", "Primary Phone", "After-Hours Phone"],
    [(t, "", "", "") for t in
     ("Excavation", "Foundation", "Framing", "Electrical", "Plumbing",
      "HVAC", "Roofing", "Drywall", "Flooring", "Other:")],
    [1.30 * inch, 2.10 * inch, 1.80 * inch, CW - 5.20 * inch]))

flow.append(Spacer(1, 12))
flow.append(d.callout_box(
    "⚠ IMPORTANT",
    [Paragraph(
        "Keep a copy of this page in your vehicle and with your project "
        "documents. Update immediately when contact information changes. Post "
        "a copy at the job site entrance.", S["body"])]))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-8-quick-reference",
                       "8.4-emergency-contacts.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
