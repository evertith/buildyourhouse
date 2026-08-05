#!/usr/bin/env python3
"""6.5 Safety Incident Report — rebuilt on the 2026 design system.

The browser-printed original leaked a stray copyright line and a duplicate
running header into the body on most pages, in places overprinting the
"Completed By" and "Detailed Root Cause" fields. All of that production junk
is dropped here.
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
CW = d.content_width()

SECTION = "Section 6: Daily Operations"
FORM_ID = "6.5"
FORM_TITLE = "Safety Incident Report"


# ---------------------------------------------------------------- local parts

class ChoiceSet(Flowable):
    """Drawn checkbox options that wrap to the available width.

    d.checkbox_choice_row draws a single line; this form's option lists run to
    twelve entries, so they have to reflow.
    """

    def __init__(self, options, box=11, font_size=10, gap=14, leading=19):
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
            w = self.box + 5 + pdfmetrics.stringWidth(opt, d.BODY, self.font_size)
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
                c.drawString(x + self.box + 5, y + 2, opt)
                x += w + self.gap
            y -= self.leading


def choice_block(label, options):
    """Bold label above drawn options that wrap across the full text width."""
    return [Paragraph(label, S["body-bold"]), ChoiceSet(options), Spacer(1, 4)]


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
    purpose="What happened, why it happened, and what you changed so it does "
            "not happen again.")

flow.append(d.callout_box(
    "IMPORTANT — WHEN TO USE THIS FORM",
    [Paragraph("Complete this form <b>IMMEDIATELY</b> after ANY of the "
               "following:", S["body"])]
    + bullets([
        "Any injury, no matter how minor (cuts, bruises, strains, etc.)",
        "Near-miss incidents (something almost caused an injury)",
        "Property damage from safety-related incidents",
        "Unsafe conditions discovered on site",
    ])
    + [Paragraph("This documentation protects you legally and helps prevent "
                 "future incidents.", S["body"])]))
flow.append(Spacer(1, 10))

flow.append(Paragraph(
    "<b>PURPOSE:</b> Safety incident reports document what happened, why it "
    "happened, and what you're doing to prevent it from happening again. "
    "These reports are critical for insurance claims, legal protection, "
    "workers' compensation claims, and identifying patterns that need to be "
    "addressed.", S["body"]))
flow.append(Spacer(1, 4))

flow.append(Paragraph("Instructions", S["h3"]))
for line in [
    "Complete this form as soon as possible after any incident — while "
    "details are fresh",
    "Be factual and objective — don't assign blame, just document facts",
    "Include all relevant details — more information is better than less",
    "Get witness statements and contact information",
    "Take photos of the incident location, equipment involved, and any "
    "injuries",
    "Keep completed reports in this section in chronological order",
    "Review incident reports periodically to identify safety improvement areas",
]:
    flow.append(Paragraph("• " + line, S["bullet"]))
flow.append(Spacer(1, 8))

flow.append(d.callout_box(
    "Emergency Response Reminder",
    bullets([
        "<b>FIRST PRIORITY:</b> Ensure scene is safe and provide necessary "
        "first aid",
        "Call 911 if serious injury or medical emergency",
        "Only move injured person if absolutely necessary for safety",
        "Keep injured person calm and comfortable",
        "Complete this report AFTER emergency response is handled",
    ])))
flow.append(Spacer(1, 12))

flow.append(d.FillInRow([("Incident Report Number:", 0.5),
                         ("Date of This Report:", 0.5)]))
flow.append(d.FillIn("Completed By:", height=28))

# ---------------- incident details
flow += d.h2("INCIDENT DETAILS", S)
flow.append(d.FillInRow([("Date of Incident:", 0.5),
                         ("Time of Incident:", 0.5)]))
flow.append(choice("Time of day:", ["AM", "PM"]))
flow.append(d.WriteBox(0.85, label="Exact Location on Site"))
flow.append(Spacer(1, 8))
flow += choice_block("Type of Incident:", [
    "Injury (with medical treatment)", "Injury (first aid only)",
    "Near-miss (no injury)", "Property damage",
    "Unsafe condition discovered", "Other",
])
flow.append(d.FillIn("If other, describe:", height=28))
flow.append(d.FillInRow([("Weather Conditions:", 0.6), ("Temperature:", 0.4)]))
flow.append(d.FillIn("Ground Conditions:", height=28))

# ---------------- persons involved
flow += d.h2("PERSON(S) INVOLVED", S)
flow.append(d.FillInRow([("Name:", 0.75), ("Age:", 0.25)]))
flow.append(d.FillIn("Address:", height=28))
flow.append(d.FillInRow([("Phone:", 0.45), ("Email:", 0.55)]))
flow += choice_block("Role:", [
    "Owner-Builder (you)", "Subcontractor", "Helper/Volunteer", "Visitor",
    "Delivery person", "Other",
])
flow.append(d.FillInRow([("If subcontractor, trade:", 0.5),
                         ("Company name:", 0.5)]))
flow.append(choice("Insurance Info on File:", ["Yes", "No"]))

# ---------------- witnesses
flow += d.h2("WITNESS INFORMATION", S)
for n in (1, 2, 3):
    flow.append(d.FillInRow([(f"Witness {n} Name:", 0.62), ("Phone:", 0.38)]))

# ---------------- description
flow += d.h2("DESCRIPTION OF INCIDENT", S)
flow.append(guide(
    "Describe exactly what happened in chronological order. Be specific: What "
    "task was being performed? What equipment was involved? What went wrong? "
    "Be objective and factual."))
flow.append(d.WriteBox(2.8))
flow.append(Spacer(1, 8))
flow.append(d.WriteBox(0.85, label="Equipment / Tools Involved"))
flow.append(Spacer(1, 6))
flow.append(d.WriteBox(0.85, label="Activity Being Performed"))

# ---------------- injuries
flow += d.h2("INJURIES SUSTAINED", S)
flow += choice_block("Type of Injury:", [
    "Cut/Laceration", "Bruise/Contusion", "Burn", "Fracture", "Sprain/Strain",
    "Eye injury", "Head injury", "Back injury", "Other",
])
flow.append(d.FillIn("Body Part(s) Injured:", height=28))
flow += choice_block("Severity:", [
    "Minor (first aid only)", "Moderate (medical attention recommended)",
    "Serious (immediate medical attention required)",
])
flow.append(d.WriteBox(1.2, label="Detailed Description of Injury"))

# ---------------- first aid / medical
flow += d.h2("FIRST AID / MEDICAL TREATMENT", S)
flow.append(choice("First Aid Provided On Site:", ["Yes", "No"]))
flow.append(d.FillInRow([("First Aid Administered By:", 0.65),
                         ("Time:", 0.35)]))
flow.append(d.WriteBox(1.0, label="First Aid Treatment Details"))
flow.append(Spacer(1, 8))
flow.append(choice("Medical Attention Sought:", ["Yes", "No"]))
flow += choice_block("Where Treated:", [
    "Emergency Room", "Urgent Care", "Doctor's Office", "Other",
])
flow.append(d.FillInRow([("Facility Name:", 0.5), ("Address:", 0.5)]))
flow += choice_block("Transported By:", [
    "Ambulance (911)", "Personal vehicle", "Walked", "Other",
])
flow.append(d.FillInRow([("Medical Professional's Name:", 0.55),
                         ("Contact Info:", 0.45)]))
flow.append(d.WriteBox(1.0, label="Diagnosis / Treatment Received"))
flow.append(Spacer(1, 8))
flow.append(choice("Work Restrictions Given:", ["Yes", "No"]))
flow.append(d.FillIn("If Yes, Details:", height=28))
flow.append(d.FillIn("Expected Return to Work Date:", height=28))

# ---------------- root cause
flow += d.h2("ROOT CAUSE ANALYSIS", S)
flow.append(guide(
    "Identify what caused this incident. Be honest — the goal is prevention, "
    "not blame. Check all that apply."))
flow += choice_block("Contributing Factors:", [
    "Lack of training", "Equipment malfunction", "Improper tool use",
    "No safety equipment used", "Fatigued/rushed", "Poor site housekeeping",
    "Weather conditions", "Inadequate lighting", "Distraction",
    "Improper procedure", "Horseplay", "Other",
])
flow.append(d.WriteBox(1.7, label="Detailed Root Cause Explanation"))

# ---------------- corrective actions
flow += d.h2("CORRECTIVE ACTIONS TAKEN", S)
flow.append(guide(
    "Document what immediate actions were taken to prevent recurrence and any "
    "long-term safety improvements implemented."))
flow.append(d.WriteBox(1.3, label="Immediate Actions Taken"))
flow.append(Spacer(1, 8))
flow.append(d.WriteBox(1.3, label="Long-Term Prevention Measures"))
flow.append(Spacer(1, 8))
flow.append(choice("Additional Training Provided:", ["Yes", "No"]))
flow.append(d.FillIn("If Yes, Details:", height=28))
flow.append(choice("Safety Equipment Added / Replaced:", ["Yes", "No"]))
flow.append(d.FillIn("If Yes, Details:", height=28))

# ---------------- photos & documentation
flow += d.h2("PHOTOS & DOCUMENTATION", S)
flow.append(choice("Photos Taken:", ["Yes", "No"]))
flow.append(d.FillIn("Photo Numbers / File Names:", height=28))
flow += choice_block("Photos Include:", [
    "Incident location", "Equipment involved", "Injuries", "Other",
])
flow.append(choice("Witness Statements Attached:", ["Yes", "No"]))
flow.append(d.FillIn("Number of Statements:", height=28))
flow.append(choice("Medical Records / Bills Attached:",
                   ["Yes", "No", "Pending"]))
flow.append(choice("Insurance Company Notified:", ["Yes", "No"]))
flow.append(d.FillInRow([("Date Notified:", 0.5),
                         ("Claim Number (if applicable):", 0.5)]))

# ---------------- certification
flow += d.h2("REPORT CERTIFICATION", S)
flow.append(Paragraph(
    "I certify that the information provided in this report is accurate and "
    "complete to the best of my knowledge.", S["body"]))
flow.append(Spacer(1, 8))
flow.append(d.FillIn("Report Completed By (Print Name):", height=32))
flow += d.signature_block([
    ("Signature", True),
    ("Reviewed By (if applicable)", True),
])

flow.append(Spacer(1, 10))
flow.append(d.callout_box(
    "End of Safety Incident Report",
    [Paragraph("Keep completed reports in chronological order. Review "
               "periodically to identify safety trends.", S["body"])]))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-6-daily-operations",
                       "6.5-safety-incident-report.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
