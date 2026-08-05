#!/usr/bin/env python3
"""1.4 Site Preparation Checklist — rebuilt on the 2026 design system."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import Flowable, Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 1: Project Planning & Foundation"
FORM_ID = "1.4"
FORM_TITLE = "Site Preparation Checklist"

# [box] Task | Date Completed | Notes / Issues
COLS = [0.42 * inch, CW - 0.42 * inch - 1.0 * inch - 2.0 * inch,
        1.0 * inch, 2.0 * inch]
HEADER = ["", Paragraph("Task", S["cell-bold"]),
          Paragraph("Date Completed", S["cell-bold"]),
          Paragraph("Notes / Issues", S["cell-bold"])]


def heights_for(rows, widths, minimum=d.WRITE_ROW_PT, pad=10):
    out = []
    for row in rows:
        tallest = 0.0
        for cell, w in zip(row, widths):
            items = cell if isinstance(cell, list) else [cell]
            h = 0.0
            for it in items:
                if isinstance(it, Flowable):
                    h += it.wrap(w - 10, 10000)[1]
            tallest = max(tallest, h)
        out.append(max(minimum, tallest + pad))
    return out


def task_cell(item):
    """item: plain text, or (text, extra, extra, ...) where each extra is a
    list of (label, fraction) drawn as a write-in row, or a list of strings
    drawn as a row of checkbox choices."""
    if isinstance(item, str):
        return Paragraph(item, S["cell"])
    text, extras = item[0], item[1:]
    parts = [Paragraph(text, S["cell"])] if text else []
    for ex in extras:
        if ex and isinstance(ex[0], tuple):
            parts.append(d.FillInRow(ex, font_size=9.5, height=24))
        else:
            parts.append(d.checkbox_choice_row(None, list(ex), S, box=11,
                                               font_size=9))
    return parts


def check_table(title, items):
    rows = [[d.Checkbox(), task_cell(it), "", ""] for it in items]
    return [d.titled_table(title, HEADER, rows, COLS, S,
                           row_heights=heights_for(rows, COLS)),
            Spacer(1, 10)]


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Everything that has to happen before the first shovel of "
            "foundation work — boundaries, utilities, clearing, access, "
            "erosion control, and temporary services.")

flow.append(d.FillInRow([("Project Name:", 0.5), ("Site Address:", 0.5)]))
flow.append(d.FillInRow([("Owner-Builder:", 0.5), ("Start Date:", 0.5)]))
flow.append(d.FillInRow([("Site Supervisor:", 0.5), ("Completion Date:", 0.5)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>INSTRUCTIONS:</b> Complete all site preparation tasks before beginning "
    "foundation work. Proper site preparation prevents costly delays and "
    "ensures safe, efficient construction. Document completion dates and take "
    "photos of critical steps.", S["body"]))
flow.append(Spacer(1, 4))

flow.append(d.callout_box(
    "⚠ CRITICAL — CALL BEFORE YOU DIG",
    [Paragraph("Call 811 (or your local utility locate service) at least 2–3 "
               "business days before any digging. Hitting underground "
               "utilities can cause serious injury, death, or expensive "
               "damage. <b>IT'S THE LAW.</b>", S["body"])]))
flow.append(Spacer(1, 12))

flow += check_table("PROPERTY BOUNDARY &amp; SURVEY", [
    "Obtain recent property survey (stamped by licensed surveyor)",
    "Verify all property corners are staked/marked and visible",
    "Identify all easements (utility, drainage, access rights-of-way)",
    "Confirm building setback requirements from property lines",
    "Mark setback lines with temporary stakes or flagging",
    "Verify no encroachment on neighbors' property or easements",
])

flow += check_table("UTILITY LOCATION (CALL 811)", [
    ("Call 811 for underground utility locate — MANDATORY",
     [("Ticket #:", 1.0)], [("Valid until:", 1.0)]),
    ("Utilities marked (check each one located):",
     ["Electric", "Gas", "Water"], ["Sewer", "Telecom"],
     [("Other:", 1.0)]),
    "Take photos of all marked utility locations for records",
    "Hand-dig within 24\" of all marked utilities (no machinery)",
    "Private utilities (septic, well, propane) marked by owner/contractor",
    "Contact utility companies if locate marks expired (renew every 30 days)",
])

flow += check_table("TREE PROTECTION &amp; CLEARING", [
    "Identify trees to be saved/protected (per plan or local ordinance)",
    "Install tree protection fencing at drip line (not at trunk!)",
    "Post \"TREE PROTECTION ZONE — NO EQUIPMENT\" signs",
    "Remove trees/vegetation in building footprint and work zones",
    "Grind or remove stumps in building area and driveway",
    "Clear brush and undergrowth from work areas",
    "Stockpile topsoil for later use in landscaping (if applicable)",
    "Dispose of debris properly (haul away, burn if permitted, chip)",
])

flow += check_table("GRADING &amp; ACCESS", [
    "Perform rough grading to establish building pad elevation",
    "Establish positive drainage away from building area (2% min slope)",
    "Create or improve access road/driveway for construction traffic",
    "Add gravel base to access road if needed (prevent mud/rutting)",
    "Ensure access road can accommodate concrete trucks, delivery trucks",
    "Create turnaround area for large vehicles if needed",
    "Level and compact area for material storage and staging",
])

flow += check_table("EROSION &amp; SEDIMENT CONTROL", [
    "Install silt fence downslope of disturbed areas",
    "Place erosion control matting on steep slopes (if applicable)",
    "Install inlet protection for storm drains",
    "Create temporary diversion swales if needed",
    "Stabilize disturbed areas not actively being worked (seed/straw)",
    "Inspect and maintain erosion controls weekly and after rain events",
])

flow += d.h2("TEMPORARY UTILITIES &amp; FACILITIES", S)

flow += check_table("Temporary Power", [
    "Contact electric utility for temporary power service",
    "Install temporary power pole with meter base and panel (per code)",
    ("Inspection of temporary power:", ["Required", "Not Required"],
     [("Inspection date:", 1.0)]),
    ("Power connected and active", [("Account #:", 1.0)]),
])

flow += check_table("Temporary Water", [
    ("Temporary water source:", ["Municipal tap", "Well", "Water delivery"]),
    "Install temporary water line/hydrant at site",
    ("Water available and tested", [("Account #:", 1.0)]),
])

flow += check_table("Sanitation &amp; Waste", [
    ("Portable toilet delivered and positioned",
     [("Vendor:", 1.0)], [("Service schedule:", 1.0)]),
    ("Dumpster/waste container delivered and positioned",
     [("Vendor:", 1.0)], [("Size:", 0.35), ("Dump schedule:", 0.65)]),
])

flow += check_table("SITE SECURITY &amp; STORAGE", [
    "Install job box or storage container for tools and materials",
    ("Secure job box with quality locks", [("Lock code/key #:", 1.0)]),
    "Post \"NO TRESPASSING\" and \"HARD HAT AREA\" signs",
    "Install temporary fencing if required by jurisdiction or for safety",
    "Post building permit in visible location (required by law)",
    "Create secure area for storing expensive materials (windows, etc.)",
    "Notify neighbors of construction start date and contact info",
])

flow += check_table("FINAL SITE PREPARATION CHECKS", [
    "Site is level and ready for foundation layout",
    "Access road is passable in current weather conditions",
    "All required permits obtained and posted",
    "Utilities are located, marked, and documented with photos",
    "Erosion controls are in place and functional",
    "Temporary power and water are active and accessible",
    "Tool storage and sanitation facilities are in place",
    "Safety equipment available (first aid kit, fire extinguisher)",
    "Emergency contact numbers posted (911, poison control, inspector)",
    "Site walkthrough completed with all stakeholders",
])

# ---------------- sign-off
flow += d.h2("SITE PREPARATION SIGN-OFF", S)
flow.append(Paragraph(
    "I certify that all site preparation tasks have been completed in "
    "accordance with approved plans, local codes, and safety requirements. The "
    "site is ready for foundation work to commence.", S["body"]))
flow.append(Spacer(1, 8))
flow += d.signature_block([
    ("Owner-Builder Signature", True),
    ("Site Supervisor (if different)", True),
])

# ---------------- photo log
flow += d.h2("PHOTO DOCUMENTATION LOG", S)
flow.append(Paragraph(
    "Take photos of site conditions before, during, and after preparation. "
    "Document utility locations, tree protection, erosion controls, and final "
    "site readiness.", S["body"]))
photo_cols = [1.0 * inch, 2.4 * inch, 1.7 * inch, 1.9 * inch]
photo_header = [Paragraph(t, S["cell-bold"]) for t in
                ("Date", "Photo Description", "File Name / Number", "Notes")]
flow.append(d.std_table([photo_header] + [["", "", "", ""] for _ in range(8)],
                        photo_cols, header_rows=1, write_rows=True))

flow.append(Spacer(1, 8))
flow.append(d.WriteBox(1.85, label="NOTES & ISSUES ENCOUNTERED"))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-1-project-planning",
                       "1.4-site-preparation-checklist.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
