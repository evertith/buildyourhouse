#!/usr/bin/env python3
"""1.6 Foundation Inspection Form — rebuilt on the 2026 design system."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import Flowable, KeepTogether, Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 1: Project Planning & Foundation"
FORM_ID = "1.6"
FORM_TITLE = "Foundation Inspection Form"

CHOICE_BOX = 11
CHOICE_FS = 9


def choice_col(options):
    """Column width that guarantees a checkbox_choice_row fits on one line.
    Mirrors checkbox_choice_row's own geometry: box + 5 + label + 18."""
    d.register_fonts()
    w = sum(CHOICE_BOX + 5 + stringWidth(o, d.BODY, CHOICE_FS) + 18
            for o in options)
    return w + 10  # cell padding


def choices(options):
    return d.checkbox_choice_row(None, options, S, box=CHOICE_BOX,
                                 font_size=CHOICE_FS)


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


PF = ["Pass", "Fail"]
PFN = ["Pass", "Fail", "N/A"]
PF_W = choice_col(PF)
RESULT_W = choice_col(PFN)
REQ_W = 1.7 * inch


def fill(label):
    """Marks a 'Required' cell that the inspector writes into."""
    return ("fill", label)


def verify_table(title, items, required_header="Required"):
    """[box] Item to Verify | Required | Actual value + Pass/Fail result."""
    item_w = CW - 0.42 * inch - REQ_W - RESULT_W
    cols = [0.42 * inch, item_w, REQ_W, RESULT_W]
    header = ["", Paragraph("Item to Verify", S["cell-bold"]),
              Paragraph(required_header, S["cell-bold"]),
              Paragraph("Actual / Result", S["cell-bold"])]
    rows = []
    for item, required, actual, opts in items:
        if isinstance(required, tuple):
            # label above a full-width drawn rule: the column is too narrow for
            # an inline label + a rule with real writing room
            req = [Paragraph(required[1].rstrip(":"), S["cell"]),
                   d.FillIn("", font_size=9, height=22)]
        else:
            req = Paragraph(required, S["cell"])
        res = []
        if actual:
            res.append(d.FillIn(actual, font_size=9, height=22))
        if opts:
            res.append(choices(opts))
        rows.append([d.Checkbox(), Paragraph(item, S["cell"]), req, res])
    return [d.titled_table(title, header, rows, cols, S,
                           row_heights=heights_for(rows, cols)),
            Spacer(1, 10)]


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="The official pre-pour inspection record — depths, dimensions, "
            "rebar, forms, anchor bolts, and the inspector's sign-off.")

flow.append(d.FillInRow([("Project Name:", 0.5), ("Inspection Date:", 0.5)]))
flow.append(d.FillInRow([("Property Address:", 0.5), ("Permit #:", 0.5)]))
flow.append(d.FillInRow([("Owner-Builder:", 0.5), ("Inspection Time:", 0.5)]))
flow.append(d.FillInRow([("Inspector Name:", 0.5), ("Weather:", 0.5)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>PURPOSE:</b> This form documents the official foundation inspection "
    "required before concrete can be poured. The inspector will verify that "
    "all foundation work complies with approved plans and local building "
    "codes. Keep this completed form in your job site binder permanently.",
    S["body"]))
flow.append(Spacer(1, 4))
flow.append(d.callout_box(
    "⚠ IMPORTANT",
    [Paragraph("Concrete pour <b>MUST NOT</b> proceed until this inspection is "
               "PASSED and signed off by the building inspector.", S["body"])]))
flow.append(Spacer(1, 12))

# ---------------- section 1
flow += d.h2("SECTION 1: FOOTER DEPTH MEASUREMENTS", S)
flow.append(d.FillIn("Required frost depth per local code (inches below "
                     "finished grade):", width=CW * 0.92))
flow.append(Spacer(1, 4))

s1_cols = [1.60 * inch, 0.85 * inch, 0.85 * inch, PF_W,
           CW - 1.60 * inch - 0.85 * inch - 0.85 * inch - PF_W]
s1_header = [Paragraph(t, S["cell-bold"]) for t in
             ("Measurement Location", "Plan Depth (in)", "Actual Depth (in)",
              "Pass / Fail", "Inspector Notes")]
s1_rows = [[Paragraph(loc, S["cell"]), "", "", choices(PF), ""] for loc in (
    "Northeast (NE) Corner", "Northwest (NW) Corner",
    "Southeast (SE) Corner", "Southwest (SW) Corner",
    "North Wall Midpoint", "South Wall Midpoint",
    "East Wall Midpoint", "West Wall Midpoint",
    "Interior Footer/Pier #1", "Interior Footer/Pier #2")]
flow.append(d.titled_table("Footer Depth Verification", s1_header, s1_rows,
                           s1_cols, S,
                           row_heights=heights_for(s1_rows, s1_cols)))
flow.append(Spacer(1, 6))
flow.append(d.checkbox_choice_row("OVERALL FOOTER DEPTH VERIFICATION:",
                                  ["PASS", "FAIL"], S))

# ---------------- section 2
flow += d.h2("SECTION 2: FOOTER DIMENSIONS", S)
s2_cols = [1.55 * inch, 1.15 * inch, 1.15 * inch, PF_W,
           CW - 1.55 * inch - 1.15 * inch - 1.15 * inch - PF_W]
s2_header = [Paragraph(t, S["cell-bold"]) for t in
             ("Item", "Required (per plan)", "Actual Value",
              "Pass / Fail", "Notes")]
s2_rows = [[Paragraph(item, S["cell"]),
            Paragraph(req, S["cell"]) if req else "",
            "", choices(PF), ""] for item, req in (
    ("Footer width (inches)", ""),
    ("Footer height/depth (inches)", ""),
    ("Footer is level (max variance)", "1/4\" in 10'"),
    ("Forms are straight and secure", "No bowing"),
    ("Forms properly braced", "Per plan"))]
flow.append(d.titled_table("Footer Dimension Verification", s2_header, s2_rows,
                           s2_cols, S,
                           row_heights=heights_for(s2_rows, s2_cols)))

# ---------------- section 3
flow += d.h2("SECTION 3: REBAR INSPECTION", S)

flow += verify_table("3A: Rebar Size &amp; Configuration", [
    ("Rebar size matches plan", fill("Size #:"), "Actual #:", PF),
    ("Number of continuous bars in footer", fill("Bars:"), "Actual:", PF),
    ("Rebar spacing meets plan requirements", fill("Spacing:"), "Actual:", PF),
])

flow += verify_table("3B: Rebar Placement &amp; Support", [
    ("Rebar elevated on chairs (min 3\" from bottom)", "3\" clearance",
     "Actual:", PF),
    ("Rebar has adequate side clearance (min 2\" from forms)", "2\" clearance",
     "Actual:", PF),
    ("Rebar is continuous (no gaps or breaks)", "Continuous", None, PF),
    ("Splices overlap minimum 18\" and are tied with wire", "18\" overlap",
     None, PF),
    ("Corner rebar is properly bent or overlapped (no gaps)", "Per code",
     None, PF),
])

flow += verify_table("3C: Rebar Condition", [
    ("Rebar is clean (no excessive rust, scale, oil, mud)", "Clean surface",
     None, PF),
    ("Rebar is properly secured and will not shift during pour", "Secure",
     None, PF),
])

flow += verify_table("3D: Wall Rebar (if applicable)", [
    ("Vertical wall rebar size and spacing per plan", fill("Size/spacing:"),
     "Actual:", PF),
    ("Horizontal wall rebar installed per plan", fill("Bars:"), "Actual:", PF),
    ("Wall rebar properly tied to footer rebar/dowels", "Per plan", None, PF),
])

# ---------------- section 4
flow += d.h2("SECTION 4: FORM ALIGNMENT &amp; LAYOUT", S)
flow += verify_table("Form Alignment &amp; Layout Verification", [
    ("Foundation layout matches approved plan dimensions", "Per plan",
     None, PF),
    ("All corners are square (diagonal measurements equal)", "Within 1/4\"",
     "Diag A / B:", PF),
    ("Foundation walls are plumb (vertical)", "1/4\" in 10'", None, PF),
    ("Foundation walls are level (horizontal top)", "1/4\" in 10'", None, PF),
    ("Wall height matches plan specifications", fill("Inches:"), "Actual:", PF),
    ("Wall thickness matches plan specifications", fill("Inches:"), "Actual:",
     PF),
    ("Forms are adequately braced to prevent blowout", "Secure", None, PF),
], required_header="Requirement")

# ---------------- section 5
flow += d.h2("SECTION 5: ANCHOR BOLTS &amp; HARDWARE", S)
flow += verify_table("Anchor Bolt &amp; Hardware Verification", [
    ("Anchor bolts on-site and ready for installation", "Available", None,
     ["Yes", "No"]),
    ("Anchor bolt size matches plan", fill("Diameter:"), "Actual:", PF),
    ("Anchor bolt length is adequate for embedment", fill("Inches:"),
     "Actual:", PF),
    ("Anchor bolt spacing plan provided", "Max 6' o.c.", "Spacing:", PF),
    ("Anchor bolts required within 12\" of corners", "12\" max", None, PF),
], required_header="Requirement")

# ---------------- section 6
flow += d.h2("SECTION 6: PLUMBING UNDER-SLAB (if applicable)", S)
flow += verify_table("Under-Slab Plumbing Verification", [
    ("Plumbing rough-in inspection passed separately", "Required", "Date:",
     ["Pass", "N/A"]),
    ("All drain pipes slope properly (1/4\" per foot min)", "1/4\" per foot",
     None, PFN),
    ("All plumbing stubs are capped/protected", "Capped", None, PFN),
    ("Plumbing is properly supported (no sagging pipes)", "Supported", None,
     PFN),
], required_header="Requirement")

# ---------------- section 7
flow += d.h2("SECTION 7: VAPOR BARRIER &amp; BASE (for slabs)", S)
flow += verify_table("Vapor Barrier &amp; Base Verification", [
    ("Gravel base installed and compacted", "4–6 inches", "Depth:", PFN),
    ("Vapor barrier installed (minimum 6 mil poly)", "6 mil min", "Mil:", PFN),
    ("Vapor barrier seams overlap 6\" and are sealed", "6\" overlap", None,
     PFN),
    ("Vapor barrier has no tears or punctures", "Intact", None, PFN),
    ("Vapor barrier sealed around all penetrations", "Sealed", None, PFN),
], required_header="Requirement")

# ---------------- section 8
flow += d.h2("SECTION 8: GENERAL SITE CONDITIONS", S)
s8_cols = [0.42 * inch, CW - 0.42 * inch - PF_W - 2.0 * inch, PF_W,
           2.0 * inch]
s8_header = ["", Paragraph("Item to Verify", S["cell-bold"]),
             Paragraph("Result", S["cell-bold"]),
             Paragraph("Inspector Notes", S["cell-bold"])]
s8_rows = [[d.Checkbox(), Paragraph(item, S["cell"]), choices(PF), ""]
           for item in (
    "Building permit is posted in visible location on site",
    "Approved foundation plans are available on-site",
    "Site is accessible for concrete delivery trucks",
    "Erosion controls are in place and functional",
    "No unsafe conditions observed on site")]
flow.append(d.titled_table("General Site Conditions", s8_header, s8_rows,
                           s8_cols, S,
                           row_heights=heights_for(s8_rows, s8_cols)))

# ---------------- section 9
flow += d.h2("SECTION 9: DEFICIENCIES &amp; CORRECTIVE ACTIONS", S)
flow.append(Paragraph("List all deficiencies found during inspection and "
                      "required corrective actions.", S["body"]))
s9_cols = [0.50 * inch, 2.80 * inch, 2.60 * inch, 1.10 * inch]
s9_header = [Paragraph(t, S["cell-bold"]) for t in
             ("Item #", "Deficiency Description", "Required Corrective Action",
              "Corrected (date)")]
s9_rows = [[Paragraph(str(n), S["cell-center"]), "", "", ""]
           for n in range(1, 7)]
flow.append(d.titled_table("Deficiency Log", s9_header, s9_rows, s9_cols, S,
                           row_heights=[d.WRITE_ROW_PT] * len(s9_rows)))

# ---------------- section 10
flow += d.h2("SECTION 10: INSPECTION RESULT &amp; SIGN-OFF", S)
flow.append(Paragraph("INSPECTION RESULT (check one):", S["body-bold"]))
flow.append(d.items_checklist([
    "<b>PASSED</b> — Approved to pour concrete",
    "<b>CONDITIONAL PASS</b> — Approved with minor corrections (see Section 9)",
    "<b>FAILED</b> — Re-inspection required after corrections",
], S))
flow.append(Spacer(1, 6))
flow.append(d.checkbox_choice_row("Re-inspection required:", ["Yes", "No"], S))
flow.append(d.FillInRow([("Re-inspection date:", 0.5), ("Time:", 0.5)]))
flow.append(Spacer(1, 4))
# comments box and signatures travel together so neither ends up alone on a page
flow.append(KeepTogether([
    d.WriteBox(2.4, label="Inspector Comments / Additional Requirements"),
    Spacer(1, 12),
    Paragraph("Building Inspector", S["h3"]),
    d.FillInRow([("Signature:", 0.62), ("Date:", 0.38)]),
    d.FillInRow([("Name (printed):", 0.5), ("License/ID #:", 0.5)]),
    Spacer(1, 6),
    Paragraph("Owner-Builder Acknowledgement", S["h3"]),
    d.FillInRow([("Signature:", 0.62), ("Date:", 0.38)]),
]))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-1-project-planning",
                       "1.6-foundation-inspection-form.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
