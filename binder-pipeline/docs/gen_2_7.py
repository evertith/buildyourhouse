#!/usr/bin/env python3
"""2.7 Safety Requirements & Liability — 2026 design system."""

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
FORM_ID = "2.7"
FORM_TITLE = "Safety Requirements & Liability"

DISCLAIMER = ("Template for general reference — have your attorney review before "
              "use. Not legal advice.")

BULLET = ParagraphStyle("bullet2", parent=S["bullet"], bulletFontName=d.BODY,
                        bulletFontSize=10.5)
SUBBULLET = ParagraphStyle("bullet3", parent=BULLET, leftIndent=52,
                           bulletIndent=40)
CELL_BULLET = ParagraphStyle("cell-bullet", parent=S["cell"],
                             leftIndent=10, bulletIndent=0,
                             spaceAfter=1)


# ---------------------------------------------------------------- local components
# Built here rather than in design.py, per the rebuild brief.

class FieldLine(Flowable):
    """One ruled entry line: optional drawn checkbox, label, a drawn rule to the
    right margin, and optional tail text sitting after the rule."""

    def __init__(self, text, box=False, rule=True, tail=None, rule_w=None,
                 indent=0, font_size=10.5, box_size=16, height=None):
        super().__init__()
        self.text = text
        self.box = box
        self.rule = rule
        self.tail = tail
        self.rule_w = rule_w
        self.indent = indent
        self.font_size = font_size
        self.box_size = box_size
        self._height = height

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self.height = self._height or (d.WRITE_ROW_PT if self.rule else 24.5)
        return self.width, self.height

    def draw(self):
        d.register_fonts()
        c = self.canv
        baseline = 9
        x = self.indent
        c.setFillColor(d.INK)
        c.setStrokeColor(d.INK)
        if self.box:
            c.setLineWidth(1)
            c.rect(x, baseline - 4, self.box_size, self.box_size)
            # 18pt gutter keeps the label aligned with d.items_checklist rows
            x += self.box_size + 18
        c.setFont(d.BODY, self.font_size)
        if self.text:
            c.drawString(x, baseline, self.text)
            x += c.stringWidth(self.text, d.BODY, self.font_size) + 6
        if self.rule:
            if self.rule_w:
                right = x + self.rule_w
                if self.tail:
                    c.drawString(right + 8, baseline, self.tail)
            else:
                right = self.width
                if self.tail:
                    tw = c.stringWidth(self.tail, d.BODY, self.font_size)
                    c.drawString(self.width - tw, baseline, self.tail)
                    right = self.width - tw - 6
            c.setLineWidth(0.75)
            c.line(x, baseline - 2, right, baseline - 2)


def bullets(items, style=None, bullet="•"):
    return [Paragraph(t, style or BULLET, bulletText=bullet) for t in items]


def numbered(items, style=None):
    return [Paragraph(t, style or BULLET, bulletText=f"{i}.")
            for i, t in enumerate(items, 1)]


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, "Safety Requirements &amp; Liability", S,
    purpose="All contractors, subcontractors, and visitors must comply with "
            "these safety requirements while on the job site. Safety is "
            "everyone's responsibility.")
flow.append(Paragraph(DISCLAIMER, S["note"]))
flow.append(Spacer(1, 4))

flow.append(d.FillIn("Project Name:"))
flow.append(d.FillIn("Project Address:"))
flow.append(d.FillInRow([("Owner:", 0.62), ("Effective Date:", 0.38)]))

# ---------------- PPE
flow += d.h2("PERSONAL PROTECTIVE EQUIPMENT (PPE) REQUIREMENTS", S)
flow.append(Paragraph("REQUIRED at all times on site:", S["body-bold"]))
flow.append(d.items_checklist([
    "Hard hat in designated areas or when overhead work is being performed",
    "Safety glasses or goggles when operating power tools or in designated areas",
    "Work boots with slip-resistant soles (no tennis shoes or sandals)",
    "Long pants (no shorts)",
    "High-visibility vest (when required by site conditions)",
], S))
flow.append(Spacer(1, 6))

flow.append(Paragraph("REQUIRED for specific tasks:", S["body-bold"]))
flow.append(d.items_checklist([
    "Hearing protection when noise levels exceed 85 decibels",
    "Respirator or dust mask when working with the materials listed below",
], S))
flow += bullets([
    "Insulation materials",
    "Drywall dust / sanding",
    "Spray paint or coatings",
    "Demolition work",
    "Other airborne contaminants",
], style=SUBBULLET)
flow.append(Spacer(1, 4))
flow.append(d.items_checklist([
    "Gloves appropriate for the task (cut-resistant, chemical-resistant, etc.)",
    "Fall protection harness when working above 6 feet",
    "Knee pads for floor work",
], S))
flow.append(Spacer(1, 6))

flow.append(Paragraph("PPE Availability", S["h3"]))
flow.append(d.checkbox_choice_row("Owner will provide basic PPE:",
                                  ["Yes", "No"], S))
flow.append(d.FillIn("Location of PPE on site:"))
flow.append(Paragraph(
    "Each contractor / subcontractor is responsible for providing their own PPE "
    "appropriate for their work.", S["body"]))

# ---------------- fall protection
flow += d.h2("FALL PROTECTION", S)
flow.append(Paragraph("Fall protection is REQUIRED when working:", S["body-bold"]))
flow += bullets([
    "6 feet or more above ground level",
    "On scaffolding",
    "On roof surfaces",
    "Near unprotected edges or openings",
    "On ladders above 6 feet for extended periods",
])
flow.append(Spacer(1, 6))
flow.append(Paragraph("Fall Protection Measures", S["h3"]))
flow.append(d.items_checklist([
    "Guardrails installed around floor openings and edges",
    "Safety harness and lanyard system available",
    "Safety nets (if applicable)",
    "Warning line systems",
    "Hole covers clearly marked",
], S))
flow.append(Spacer(1, 6))
flow.append(Paragraph("Scaffolding Requirements", S["h3"]))
flow.append(d.items_checklist([
    "Erected by qualified personnel",
    "Inspected before each use",
    "Equipped with guardrails and toe boards",
    "On stable, level surface",
    "Tagged with inspection date",
], S))

# ---------------- ladder safety
flow += d.h2("LADDER SAFETY", S)
flow.append(Paragraph("All ladders must:", S["body-bold"]))
flow.append(d.items_checklist([
    "Be in good condition (no broken rungs, damaged rails, or missing parts)",
    "Be properly rated for the load (minimum Type II — 225 lbs)",
    "Be placed on stable, level surface",
    "Be secured at top or have someone foot the ladder",
    "Extend at least 3 feet above landing when used for roof access",
    "Be set at proper angle (4:1 ratio — 1 foot out for every 4 feet up)",
], S))
flow.append(Spacer(1, 6))
flow.append(Paragraph("Ladder Use Rules", S["h3"]))
flow += bullets([
    "Maintain three points of contact at all times",
    "Face ladder when climbing up or down",
    "Do not stand on top two rungs",
    "Do not overreach — move ladder instead",
    "Never use metal ladders near electrical work",
    "Inspect ladder before each use",
])

# ---------------- power tools
flow += d.h2("POWER TOOL &amp; EQUIPMENT SAFETY", S)
flow.append(Paragraph("General Requirements:", S["body-bold"]))
flow.append(d.items_checklist([
    "All power tools must have guards in place and functioning",
    "Ground Fault Circuit Interrupter (GFCI) protection required for all "
    "electrical tools",
    "Extension cords must be 12-gauge or heavier, in good condition",
    "Tools must be inspected before each use",
    "Only trained operators may use power tools",
    "Tools must be unplugged when changing blades, bits, or attachments",
], S))
flow.append(Spacer(1, 8))

tool_rows = [
    ("Circular Saws", ["Lower guard must be functional",
                       "Unplug before blade changes",
                       "Secure work piece before cutting"]),
    ("Table Saws", ["Blade guard in place",
                    "Use push sticks for narrow cuts",
                    "Stand to side, never directly behind blade"]),
    ("Nail Guns", ["Sequential trigger preferred over bump fire",
                   "Never point at anyone",
                   "Disconnect air supply before clearing jams"]),
    ("Powder-Actuated Tools", ["Operator certification required",
                               "Never use on brittle materials",
                               "Hearing and eye protection mandatory"]),
]
flow.append(KeepTogether(d.titled_table(
    "Specific Tool Safety",
    [Paragraph("Tool", S["cell-bold"]),
     Paragraph("Safety Requirements", S["cell-bold"])],
    [[Paragraph(name, S["cell-bold"]),
      [Paragraph(r, CELL_BULLET, bulletText="•") for r in reqs]]
     for name, reqs in tool_rows],
    [1.9 * inch, 5.1 * inch], S)))

# ---------------- trenching
flow += d.h2("TRENCHING &amp; EXCAVATION SAFETY", S)
flow.append(Paragraph("Required for trenches 4 feet or deeper:", S["body-bold"]))
flow.append(d.items_checklist([
    "Protective system (shoring, shielding, or sloping)",
    "Competent person on site for daily inspections",
    "Ladders or ramps within 25 feet of workers",
    "Soil and adjacent areas inspected for indications of possible cave-in",
    "Utilities located and marked before digging (call 811)",
    "Spoil piles kept at least 2 feet from edge",
], S))
flow.append(Spacer(1, 6))
flow.append(d.callout_box(
    "⚠ Never enter a trench without proper protection.", []))

# ---------------- housekeeping
flow += d.h2("SITE CLEANLINESS &amp; HOUSEKEEPING", S)
flow.append(Paragraph("Daily Requirements:", S["body-bold"]))
flow.append(d.items_checklist([
    "Remove debris and trash at end of each workday",
    "Stack materials neatly and securely",
    "Keep walkways and exits clear",
    "Cover or barricade floor openings",
    "Remove protruding nails from lumber",
    "Coil hoses and cords when not in use",
    "Store flammable materials in approved containers away from ignition sources",
], S))
flow.append(Spacer(1, 4))
flow.append(d.FillInRow([("Dumpster Location:", 0.5),
                         ("Trash Removal Schedule:", 0.5)]))

# ---------------- emergency
flow += d.h2("EMERGENCY INFORMATION", S)
flow.append(d.callout_box("EMERGENCY CONTACTS", [
    Paragraph("Emergency Services: <b>911</b>", S["body"]),
    Paragraph("Poison Control: <b>1-800-222-1222</b>", S["body"])]))
flow.append(Spacer(1, 8))
flow.append(d.FillIn("First Aid Kit Location:"))
flow.append(d.FillIn("Fire Extinguisher Location(s):"))
flow.append(d.FillIn("Emergency Eyewash Station:"))
flow.append(d.FillInRow([("Project Owner:", 0.62), ("Phone:", 0.38)]))
flow.append(d.FillInRow([("Site Supervisor:", 0.62), ("Phone:", 0.38)]))
flow.append(d.FillIn("Nearest Hospital:"))
flow.append(d.FillIn("Hospital Address:"))
flow.append(d.FillInRow([("Hospital Phone:", 0.5), ("Distance from site:", 0.5)]))
flow.append(d.FillIn("Estimated travel time:"))

# ---------------- incident reporting
flow += d.h2("INCIDENT REPORTING", S)
flow.append(Paragraph(
    "All injuries, near-misses, and safety incidents MUST be reported "
    "immediately.", S["body-bold"]))
flow.append(Paragraph("Reporting Procedure:", S["body-bold"]))
flow += numbered([
    "Provide first aid / call 911 if necessary",
    "Notify project owner immediately",
    "Complete incident report form within 24 hours",
    "Document scene with photos (if safe to do so)",
    "Preserve evidence and interview witnesses",
    "Identify root cause and corrective actions",
])
flow.append(Spacer(1, 4))
flow.append(d.FillIn("Incident Report Forms Located:"))

# ---------------- OSHA
flow += d.h2("OSHA COMPLIANCE &amp; REGULATIONS", S)
flow.append(Paragraph(
    "This job site shall comply with all applicable OSHA (Occupational Safety "
    "and Health Administration) regulations, including but not limited to:",
    S["body"]))
flow += bullets([
    "29 CFR 1926 — Safety and Health Regulations for Construction",
    "Hazard Communication Standard (Right to Know)",
    "Lockout / Tagout procedures for equipment",
    "Confined space entry requirements",
    "Electrical safety standards",
    "Material handling and storage",
])
flow.append(Spacer(1, 4))
flow.append(d.FillIn("Required OSHA posters shall be displayed at:"))
flow.append(Spacer(1, 4))
flow.append(Paragraph("Safety Data Sheets (SDS)", S["h3"]))
flow.append(Paragraph(
    "SDS for all hazardous materials used on site must be available and "
    "accessible to all workers, and reviewed before using any hazardous "
    "material.", S["body"]))
flow.append(d.FillIn("Safety Data Sheets are kept in:"))

# ---------------- liability
flow += d.h2("LIABILITY &amp; ACKNOWLEDGMENT", S)
flow.append(Paragraph("Contractor / Subcontractor Responsibilities", S["h3"]))
flow.append(Paragraph(
    "Each contractor and subcontractor agrees that they:", S["body"]))
flow += bullets([
    "Are responsible for the safety of their own employees",
    "Will comply with all safety requirements outlined in this document",
    "Will provide appropriate PPE to their employees",
    "Maintain required insurance coverage",
    "Will report all incidents and injuries immediately",
    "Are responsible for any OSHA violations by their employees",
    "Will conduct their own safety training and toolbox talks",
])
flow.append(Spacer(1, 4))
flow.append(Paragraph("Right to Stop Work", S["h3"]))
flow.append(Paragraph(
    "Any person has the right and responsibility to stop work if they observe "
    "unsafe conditions or practices. Work shall not resume until the hazard is "
    "corrected.", S["body"]))
flow.append(KeepTogether([
    Paragraph("Violation of Safety Requirements", S["h3"]),
    Paragraph("Failure to comply with these safety requirements may result in:",
              S["body"]),
    *bullets([
        "Immediate removal from job site",
        "Termination of contract",
        "Withholding of payment",
    ])]))

# ---------------- acknowledgment
flow += d.h2("ACKNOWLEDGMENT", S)
flow.append(Paragraph(
    "I acknowledge that I have read, understand, and agree to comply with all "
    "safety requirements outlined in this document. I understand that failure to "
    "comply may result in removal from the job site and/or termination of "
    "contract.", S["body"]))
flow.append(Spacer(1, 8))
flow.append(KeepTogether([
    *d.signature_block([("Signature", True)]),
    d.FillInRow([("Print Name:", 0.5), ("Company:", 0.5)]),
    d.FillIn("Trade:"),
]))
flow.append(Spacer(1, 6))
flow.append(Paragraph(
    "Photocopy this acknowledgment page and have every contractor, "
    "subcontractor and regular visitor sign their own copy. File the signed "
    "copies behind this form.", S["note"]))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-2-contracts-legal",
                       "2.7-safety-requirements-liability.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
