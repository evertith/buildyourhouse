#!/usr/bin/env python3
"""1.3 Permit Application Checklist — rebuilt on the 2026 design system."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer, Table, TableStyle

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 1: Project Planning & Foundation"
FORM_ID = "1.3"
FORM_TITLE = "Permit Application Checklist"

BOX_COL = 0.42 * inch


def check_list(items, row_height=24.5):
    """items_checklist that also accepts (text, [(label, fraction), ...]) so an
    item can carry its own drawn write-in rule (design.items_checklist takes
    plain strings only)."""
    data = []
    heights = []
    for it in items:
        if isinstance(it, tuple):
            text, fields = it
            cell = [Paragraph(text, S["cell"]),
                    d.FillInRow(fields, font_size=9.5, height=24)]
            heights.append(row_height + 24)
        else:
            cell = Paragraph(it, S["cell"])
            heights.append(row_height)
        data.append([d.Checkbox(), cell])
    t = Table(data, colWidths=[BOX_COL, CW - BOX_COL], rowHeights=heights)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def permit(title, documents, tracking_extra=None, expiration=True, tail=None):
    """One permit: heading, documents-to-submit checklist, tracking fields."""
    out = []
    out += d.h2(title, S)
    out.append(Paragraph("Documents to Submit", S["h3"]))
    out.append(check_list(documents))
    out.append(Paragraph("Submission &amp; Tracking", S["h3"]))
    out.append(d.FillInRow([("Application submitted (date):", 0.5),
                            ("By:", 0.5)]))
    out.append(d.FillInRow([("Permit fee ($):", 0.34), ("Paid date:", 0.33),
                            ("Receipt #:", 0.33)]))
    if tracking_extra:
        out += tracking_extra
    out.append(d.FillInRow([("PERMIT APPROVED (date):", 0.45),
                            ("Permit #:", 0.55)]))
    if expiration:
        out.append(d.FillIn("Permit expiration date:", width=CW * 0.6))
        out.append(Paragraph("Renew before expiration.", S["note"]))
    if tail:
        out += tail
    out.append(Spacer(1, 6))
    return out


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Every permit the build may require — what to submit, what it cost, "
            "when it was approved, and when it expires.")

flow.append(d.FillInRow([("Project Name:", 0.5), ("Property Address:", 0.5)]))
flow.append(d.FillInRow([("Owner-Builder:", 0.5), ("Parcel/Tax ID #:", 0.5)]))
flow.append(d.FillInRow([("Jurisdiction:", 0.5), ("Date Started:", 0.5)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>INSTRUCTIONS:</b> This checklist tracks all required permits for your "
    "construction project. Each jurisdiction has different requirements — "
    "verify with your local building department. Track application dates, fees "
    "paid, approval dates, and any resubmittal requirements.", S["body"]))

# ---------------- building permit
flow += permit(
    "BUILDING PERMIT (PRIMARY)",
    [
        "Complete building permit application form (jurisdiction-specific)",
        "Owner-builder affidavit/declaration (notarized if required)",
        "Proof of property ownership (deed or title)",
        ("Architectural plans (foundation, floor, elevation, cross-section)",
         [("Sets required:", 0.5), ("Sets submitted:", 0.5)]),
        "Structural engineering plans (if required) — stamped by licensed PE",
        "Energy compliance calculations (RESCHECK or equivalent)",
        "Site plan showing property boundaries, setbacks, easements, building "
        "footprint",
        "Property survey (recent, stamped by surveyor)",
        "Soil/geotechnical report (if on challenging terrain)",
        "Builder's risk insurance certificate",
        "General liability insurance certificate",
        "Workers' compensation exemption or coverage proof",
        "HOA/covenant approval (if applicable)",
    ],
    tracking_extra=[
        d.FillIn("Estimated processing time (weeks):", width=CW * 0.6),
        d.FillIn("Plan review comments received (date):", width=CW * 0.8),
        d.checkbox_choice_row("Corrections needed:", ["Yes", "No"], S),
        Spacer(1, 2),
        d.FillInRow([("Resubmittal date (if needed):", 0.5),
                     ("Resubmittal fee ($):", 0.5)]),
    ])

# ---------------- trade permits
flow += permit(
    "ELECTRICAL PERMIT",
    [
        "Electrical permit application",
        "Electrical plan/diagram showing panel, circuits, outlets, switches, "
        "fixtures",
        "Load calculation worksheet",
        "Master electrician license # (if doing own work, proof of "
        "owner-builder status)",
        "Copy of approved building permit",
    ])

flow += permit(
    "PLUMBING PERMIT",
    [
        "Plumbing permit application",
        "Plumbing plan showing supply lines, drain/waste/vent system, fixtures",
        "Water heater specifications",
        "Master plumber license # (if doing own work, proof of owner-builder "
        "status)",
        "Copy of approved building permit",
    ])

flow += permit(
    "MECHANICAL/HVAC PERMIT",
    [
        "Mechanical permit application",
        "HVAC plan showing equipment location, ductwork layout, return air "
        "pathways",
        "Equipment specifications (BTU capacity, efficiency ratings)",
        "Manual J load calculation (heating/cooling load)",
        "HVAC contractor license # (if subbing out) or owner-builder proof",
        "Copy of approved building permit",
    ])

flow += permit(
    "SEPTIC SYSTEM PERMIT (if applicable)",
    [
        "Septic system permit application (county health department typically)",
        "Percolation test results (conducted by approved contractor)",
        "Soil evaluation report",
        "Septic system design plan (showing tank, drain field, setbacks)",
        "Installer license/certification",
    ],
    expiration=False,
    tail=[d.checkbox_choice_row("Inspection required before cover:",
                                ["Yes", "No"], S),
          d.FillIn("Inspection date:", width=CW * 0.6)])

flow += permit(
    "WELL PERMIT (if applicable)",
    [
        "Well drilling permit application",
        "Proposed well location (site plan with setbacks from septic, property "
        "lines)",
        "Licensed well driller information",
    ],
    expiration=False,
    tail=[d.FillInRow([("Well completion report filed (date):", 0.55),
                       ("Well depth (feet):", 0.45)]),
          d.FillIn("Water quality test completed (date):", width=CW * 0.6),
          d.checkbox_choice_row("Water quality result:", ["Pass", "Fail"], S)])

flow += permit(
    "DRIVEWAY/CURB CUT PERMIT (if applicable)",
    [
        "Driveway permit application (Department of Transportation or Highway "
        "Dept)",
        "Site plan showing driveway location and sight distance",
        "Culvert specifications (if crossing ditch or drainage)",
    ],
    expiration=False)

flow += permit(
    "EROSION &amp; SEDIMENT CONTROL PERMIT (if applicable)",
    [
        "Erosion control plan (required if disturbing more than 1 acre or near "
        "waterways)",
        "SWPPP (Stormwater Pollution Prevention Plan) if needed",
    ],
    expiration=False)

# ---------------- other permits
other_cols = [2.10 * inch, 1.25 * inch, 1.00 * inch, 0.90 * inch, 1.75 * inch]
other_header = [Paragraph(t, S["cell-bold"]) for t in
                ("Permit Type", "Required?", "Date Applied", "Fee Paid ($)",
                 "Permit # / Status")]
other_rows = [["",
               d.checkbox_choice_row(None, ["Yes", "No"], S, box=11,
                                     font_size=9),
               "", "", ""] for _ in range(3)]
flow.append(d.titled_table("OTHER PERMITS (jurisdiction-specific)",
                           other_header, other_rows, other_cols, S,
                           row_heights=[d.WRITE_ROW_PT] * len(other_rows)))

# ---------------- contacts
flow += d.h2("PERMIT CONTACT INFORMATION", S)
for label in ("Building Department:", "Inspector Name:",
              "Health Department (septic):", "DOT/Highway Dept:",
              "Other Contact:"):
    flow.append(d.FillInRow([(label, 0.62), ("Phone:", 0.38)]))

flow.append(Spacer(1, 10))
flow.append(d.WriteBox(2.6, label="NOTES & IMPORTANT REMINDERS"))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-1-project-planning",
                       "1.3-permit-application-checklist.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
