#!/usr/bin/env python3
"""3.1 Framing Inspection Checklist — rebuilt on the 2026 design system."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import CondPageBreak, Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 3: Rough-In Phase"
FORM_ID = "3.1"
FORM_TITLE = "Framing Inspection Checklist"

COLS = [0.42 * inch, 3.00 * inch, 1.50 * inch, CW - 4.92 * inch]


def measured_heights(rows, cols, minimum=d.WRITE_ROW_PT, pad=10):
    """Row heights that never clip: max wrapped cell height, floored at the
    handwriting minimum. Needed because titled_table auto-sizes any row that
    carries a Paragraph, which would drop write-in rows below 0.40in."""
    heights = []
    for row in rows:
        tallest = 0
        for cell, width in zip(row, cols):
            if isinstance(cell, str) or cell is None:
                continue
            flowables = cell if isinstance(cell, list) else [cell]
            tallest = max(tallest, sum(f.wrap(width - 10, 10000)[1]
                                       for f in flowables))
        heights.append(max(minimum, tallest + pad))
    return heights


def spec_table(title, items):
    """[box] Item | Spec/Code | Notes — the framing checklist model."""
    header = ["",
              Paragraph("Item", S["cell-bold"]),
              Paragraph("Spec / Code", S["cell-bold"]),
              Paragraph("Notes", S["cell-bold"])]
    rows = [[d.Checkbox(), Paragraph(item, S["cell"]),
             Paragraph(spec, S["cell"]), ""] for item, spec in items]
    return [d.titled_table(title, header, rows, COLS, S,
                           row_heights=measured_heights(rows, COLS)),
            Spacer(1, 8)]



def section(title, styles=None, min_space=3.4):
    """An h2 that will not strand itself at the foot of a page: it reserves
    room for the heading plus the opening rows of whatever follows."""
    return [CondPageBreak(min_space * inch)] + d.h2(title, S)


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Every framing item the inspector will look at — foundation "
            "connections through roof structure — plus the results, "
            "corrections and sign-off record.")

flow.append(d.FillInRow([("Property Address:", 1.0)]))
flow.append(d.FillInRow([("Permit Number:", 0.5), ("Inspection Date:", 0.5)]))
flow.append(d.FillInRow([("Inspector Name:", 0.6), ("Phone:", 0.4)]))
flow.append(d.FillInRow([("Builder / GC:", 0.5),
                         ("Framing Contractor:", 0.5)]))
flow.append(Spacer(1, 8))

flow.append(Paragraph(
    "<b>INSTRUCTIONS:</b> Walk the frame with this checklist before you call "
    "for inspection. Check each item, record measurements in the Notes "
    "column, and photograph anything that will be covered by sheathing or "
    "drywall. Items that fail here are far cheaper to fix now than after the "
    "inspector red-tags them.", S["body"]))
flow.append(Spacer(1, 4))

# ---------------- FOUNDATION-TO-FRAME
flow += section("FOUNDATION-TO-FRAME CONNECTIONS", S)
flow += spec_table("Sill Plates, Anchorage & Hold-Downs", [
    ("Sill plate properly installed", "PT lumber required"),
    ("Sill plate size matches plans", "Typically 2x6"),
    ("Anchor bolts present and properly spaced", "Max 6' o.c., 12\" from ends"),
    ("Anchor bolt size and embedment depth", "1/2\" min, 7\" embedment"),
    ("Washers and nuts on all anchor bolts", "Required"),
    ("Sill seal/gasket installed", "Required under sill plate"),
    ("Termite shield installed (if required)", "Per local code"),
    ("Pressure-treated lumber used where required",
     "All wood within 6\" of masonry"),
    ("Hold-downs installed at shear walls", "Per engineer specs"),
    ("Simpson straps/ties at all connections", "Per plan specifications"),
])
flow.append(d.WriteBox(1.2, label="Foundation Connection Notes"))

# ---------------- WALL FRAMING
flow += section("WALL FRAMING", S)
flow += spec_table("Plates, Studs, Openings & Blocking", [
    ("Wall plates: bottom plate installed", "Properly nailed to floor"),
    ("Wall plates: double top plates installed", "Joints offset 48\" minimum"),
    ("Stud spacing — exterior walls", "16\" or 24\" o.c. per plan"),
    ("Stud spacing — interior walls", "16\" or 24\" o.c. per plan"),
    ("Stud size matches plans", "Typically 2x4 or 2x6"),
    ("Load-bearing wall studs sized correctly", "Per structural plan"),
    ("Wall height matches plans", "Check ceiling height specs"),
    ("Headers properly sized for spans", "Per span table/engineer"),
    ("King studs present at all openings", "Full height studs"),
    ("Jack studs (trimmers) under headers", "Both sides of opening"),
    ("Cripple studs above/below openings", "Match wall stud spacing"),
    ("Corner framing adequate for insulation",
     "3-stud or California corners"),
    ("Partition wall backing installed", "At all T-intersections"),
    ("Fire blocking installed in walls", "10' max height intervals"),
    ("Fire blocking at floor/ceiling levels", "Required at horizontal voids"),
])
flow += spec_table("Plumb, Bracing & Sheathing", [
    ("Walls plumb and straight", "1/4\" in 10' maximum"),
    ("Bracing adequate until sheathing", "Temporary bracing as needed"),
    ("Sheathing installed and nailed properly", "Per manufacturer/code"),
    ("Sheathing edge support at horizontal joints",
     "Blocking or clips required"),
    ("Wall sheathing gaps at panel edges", "1/8\" spacing recommended"),
    ("Proper nailing of sheathing to framing", "6\" o.c. edges, 12\" field"),
    ("Shear wall plywood/OSB thickness", "Per engineered plan"),
    ("Shear wall nailing pattern followed", "Per engineered plan"),
    ("House wrap/weather barrier installed", "If applicable at this stage"),
    ("Weather barrier lapped correctly", "Shingle style, bottom to top"),
])
flow.append(d.WriteBox(1.2, label="Wall Framing Notes"))

# ---------------- FLOOR FRAMING
flow += section("FLOOR FRAMING", S)
flow += spec_table("Joists, Bearing & Subfloor", [
    ("Floor joist size matches plans", "Verify size for spans"),
    ("Floor joist spacing", "12\", 16\", or 24\" o.c. per plan"),
    ("Joists properly bearing on supports", "Minimum 1.5\" bearing"),
    ("Joist hangers installed where required", "Proper size for joist"),
    ("All joist hanger nails installed", "Every hole filled"),
    ("Rim joist/band board installed", "Proper size and connection"),
    ("Bridging/blocking installed", "As required by code/plan"),
    ("Subfloor thickness adequate", "3/4\" typical for 16\" o.c."),
    ("Subfloor glued and screwed", "Reduces squeaks"),
    ("Subfloor edges supported properly", "Tongue &amp; groove or blocking"),
    ("Subfloor gaps at panel edges", "1/8\" spacing recommended"),
])
flow += spec_table("Openings, Cantilevers & Engineered Joists", [
    ("Floor openings properly framed", "Doubled joists/headers"),
    ("Cantilevers properly supported", "Per code/engineering"),
    ("Cantilever joists extended back 2x", "Min. ratio for cantilever"),
    ("Engineered floor joists (I-joist/TJI) installed per manufacturer",
     "Check installation guide"),
    ("Web stiffeners at bearing points (I-joists)", "Required at supports"),
    ("No unauthorized cuts in I-joist webs", "Follow mfr. guidelines"),
    ("Floor level and flat", "1/4\" in 10' maximum"),
    ("Squeaks addressed before covering", "Walk and check"),
])
flow.append(d.WriteBox(1.2, label="Floor Framing Notes"))

# ---------------- ROOF FRAMING
flow += section("ROOF FRAMING", S)
flow += spec_table("Rafters, Ridge & Ties", [
    ("Rafter/truss size matches plans", "Verify engineered specs"),
    ("Rafter/truss spacing", "16\" or 24\" o.c. per plan"),
    ("Roof pitch matches plans", "Verify with level/square"),
    ("Ridge board size adequate", "Depth ≥ rafter cut end"),
    ("Ridge beam properly sized (if load-bearing)", "Per engineered plan"),
    ("Rafters properly bird-mouthed", "Proper seat and heel cut"),
    ("Collar ties installed where required", "Upper third of attic space"),
    ("Rafter ties/ceiling joists adequate", "Prevent wall spreading"),
    ("Hurricane ties/clips installed", "Each rafter to top plate"),
    ("Gable end bracing installed", "Per code requirements"),
])
flow += spec_table("Eaves, Sheathing & Trusses", [
    ("Roof overhang/eave depth per plan", "Verify dimension"),
    ("Fascia backing/blocking installed", "For fascia attachment"),
    ("Soffit backing/frieze blocks installed", "As required"),
    ("Roof sheathing thickness adequate", "1/2\" min. for 24\" spacing"),
    ("Roof sheathing properly attached", "6\" o.c. edges, 12\" field"),
    ("Sheathing gaps at panel edges", "1/8\" spacing recommended"),
    ("H-clips installed if required", "Check sheathing span rating"),
    ("Valley framing properly supported", "Valley rafters/jack rafters"),
    ("Hip framing properly installed", "Hip rafters/jack rafters"),
    ("Roof openings properly framed", "Chimneys, skylights, vents"),
    ("Trusses installed per placement plan", "Check orientation marks"),
    ("Truss bracing installed per engineer", "Lateral, diagonal bracing"),
    ("No unauthorized truss modifications", "Check for cuts/notches"),
    ("Truss uplift clips at interior walls", "If specified by engineer"),
])
flow.append(d.WriteBox(1.2, label="Roof Framing Notes"))

# ---------------- STRUCTURAL ELEMENTS
flow += section("STRUCTURAL ELEMENTS", S)
flow += spec_table("Engineering, Beams & Posts", [
    ("Engineered plans on site for inspection", "Required for review"),
    ("Engineering notes highlighted/marked", "Call-outs clearly visible"),
    ("Load-bearing walls identified", "Per structural plan"),
    ("Load-bearing wall studs sized correctly", "Per point loads/spans"),
    ("Beams sized per engineering", "LVL, steel, timber"),
    ("Beam spans match approved plans", "Verify dimensions"),
    ("Beam-to-post connections proper", "Simpson caps or engineer spec"),
    ("Post size adequate for loads", "Per engineered plan"),
    ("Posts bear on proper footings", "Check foundation plan"),
    ("Post-to-footing connection adequate", "Simpson base or embedded"),
    ("Steel beams properly installed", "Verify size and bearing"),
    ("Steel beam connections bolted properly", "Proper bolt size/quantity"),
    ("LVL beams oriented correctly", "Check manufacturer stamp"),
    ("Glulam beams oriented correctly", "Top stamped side up"),
])
flow += spec_table("Lateral Resistance", [
    ("Lateral bracing installed", "Shear walls, hold-downs"),
    ("Shear wall hold-downs installed", "Simpson HD or specified"),
    ("All hold-down bolts tight", "Check torque if specified"),
    ("Portal frames installed if required", "For garage openings, etc."),
    ("Special seismic requirements met", "Per local code/zone"),
    ("Hurricane/wind tie-down requirements met", "Per local code/zone"),
])
flow.append(d.WriteBox(1.2, label="Structural Notes"))

# ---------------- GENERAL QUALITY
flow += section("GENERAL FRAMING QUALITY", S)
flow += spec_table("Material, Workmanship & Access", [
    ("Lumber grade appropriate for use", "Check stamps on lumber"),
    ("No splits/checks compromising strength", "Visual inspection"),
    ("Framing members properly oriented", "Crown up on joists/rafters"),
    ("Nailing schedule followed", "Per code requirements"),
    ("No overdriven nails (crushed wood)", "Visual inspection"),
    ("All framing secure/no loose members", "Push test, visual"),
    ("Proper backing for drywall at corners", "Prevent cracks"),
    ("Backing installed for wall-mounted items", "Grab bars, TVs, cabinets"),
    ("Framing clear of plumbing/electrical runs",
     "Adequate space for trades"),
    ("Notches in framing within code limits", "Max 1/4 depth for bearing"),
    ("Holes drilled in framing within limits", "Center 1/3, max 1/3 width"),
    ("Nail plates over drilled holes/notches", "Protect wiring/plumbing"),
    ("Recessed ceiling areas properly framed", "Tray ceilings, soffits"),
    ("Stairwell opening properly sized/framed", "Per code width/headroom"),
    ("Attic access opening framed", "Min 22\" x 30\" opening"),
    ("Crawl space access opening framed", "Min 18\" x 24\" opening"),
    ("Mechanical room clearances maintained", "For equipment access/service"),
])
flow.append(d.WriteBox(1.2, label="General Quality Notes"))

# ---------------- INSPECTION RESULTS
flow += section("INSPECTION RESULTS & CORRECTIONS", S)

flow.append(Paragraph("Initial Inspection", S["h3"]))
flow.append(d.FillInRow([("Inspection Date:", 0.5), ("Time:", 0.5)]))
flow.append(d.FillInRow([("Inspector:", 1.0)]))
flow.append(d.checkbox_choice_row(
    "RESULT:", ["PASSED", "FAILED — Corrections Required"], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.5, label="Deficiencies / Items Requiring Correction"))

flow.append(Paragraph("Corrections Made", S["h3"]))
flow.append(d.FillInRow([("Date Corrections Completed:", 1.0)]))
flow.append(d.FillInRow([("Contractor / Person Making Corrections:", 1.0)]))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.4, label="Description of Corrections"))

flow.append(Paragraph("Re-Inspection (if required)", S["h3"]))
flow.append(d.FillInRow([("Re-Inspection Date:", 0.5), ("Time:", 0.5)]))
flow.append(d.FillInRow([("Inspector:", 1.0)]))
flow.append(d.checkbox_choice_row(
    "RESULT:", ["PASSED", "FAILED — Additional Corrections Required"], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.2, label="Comments"))

# ---------------- SIGN-OFF
flow += section("FINAL SIGN-OFF", S)
flow += d.signature_block([
    ("Builder Signature", True),
    ("Inspector Signature", True),
])
flow.append(d.FillInRow([("Permit Number:", 1.0)]))
flow.append(d.checkbox_choice_row("FINAL APPROVAL:", ["YES"], S))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-3-rough-in-phase",
                       "3.1-framing-inspection-checklist.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
