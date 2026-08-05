#!/usr/bin/env python3
"""2.1 Subcontractor Agreement Template — 2026 design system."""

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
FORM_ID = "2.1"
# Footer furniture is centred against the copyright line; the long form of the
# title collides with it, so the footer carries the short form.
FORM_TITLE = "Subcontractor Agreement"
DISPLAY_TITLE = "Subcontractor Agreement Template"

DISCLAIMER = ("Template for general reference — have your attorney review before "
              "use. Not legal advice.")

BULLET = ParagraphStyle("bullet2", parent=S["bullet"], bulletFontName=d.BODY,
                        bulletFontSize=10.5)


# ---------------------------------------------------------------- local components
# Built here rather than in design.py, per the rebuild brief.

class FieldLine(Flowable):
    """One ruled entry line: optional drawn checkbox, label, a drawn rule to the
    right margin, and optional tail text sitting after the rule.

        [ ] General Liability Insurance: Minimum $ ______ per occurrence
    """

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


class InitialsLine(Flowable):
    """Lightweight article sign-off, right aligned: 'Initials: ___ / ___'."""

    def __init__(self, label="Initials (Owner / Subcontractor):", rule_w=58,
                 font_size=9.5, height=28):
        super().__init__()
        self.label = label
        self.rule_w = rule_w
        self.font_size = font_size
        self._height = height

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self.height = self._height
        return self.width, self.height

    def draw(self):
        d.register_fonts()
        c = self.canv
        baseline = 10
        rw = self.rule_w
        c.setFont(d.BODY, self.font_size)
        c.setFillColor(d.FURNITURE_GREY)
        lw = c.stringWidth(self.label, d.BODY, self.font_size)
        x = max(0, self.width - (lw + 10 + rw + 14 + rw))
        c.drawString(x, baseline, self.label)
        x += lw + 10
        c.setStrokeColor(d.INK)
        c.setLineWidth(0.75)
        c.line(x, baseline - 2, x + rw, baseline - 2)
        x += rw + 4
        c.setFillColor(d.INK)
        c.drawString(x, baseline, "/")
        x += 10
        c.line(x, baseline - 2, x + rw, baseline - 2)


def bullets(items, style=None, bullet="•"):
    return [Paragraph(t, style or BULLET, bulletText=bullet) for t in items]


def numbered(items, style=None):
    return [Paragraph(t, style or BULLET, bulletText=f"{i}.")
            for i, t in enumerate(items, 1)]


def article_end():
    return [Spacer(1, 4), InitialsLine()]


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, DISPLAY_TITLE, S,
    purpose="A written agreement between the owner-builder and each trade "
            "contractor — scope, price, payment, insurance, warranty and "
            "dispute terms, executed before any work begins.")
flow.append(Paragraph(DISCLAIMER, S["note"]))
flow.append(Spacer(1, 4))

# ---------------- ARTICLE 1
flow += d.h2("ARTICLE 1 — PROJECT INFORMATION", S)

flow.append(d.FillIn("Project Address:"))
flow.append(d.FillIn("Legal Description:"))

flow.append(Paragraph("Owner / General Contractor", S["h3"]))
flow.append(d.FillIn("Name:"))
flow.append(d.FillIn("Address:"))
flow.append(d.FillInRow([("City / State / ZIP:", 0.6), ("Phone:", 0.4)]))
flow.append(d.FillIn("Email:"))

flow.append(Paragraph("Subcontractor", S["h3"]))
flow.append(d.FillIn("Company Name:"))
flow.append(d.FillInRow([("License #:", 0.5), ("State:", 0.5)]))
flow.append(d.FillIn("Contact Person:"))
flow.append(d.FillIn("Address:"))
flow.append(d.FillInRow([("City / State / ZIP:", 0.6), ("Phone:", 0.4)]))
flow.append(d.FillIn("Email:"))

flow.append(Paragraph("Project Description", S["h3"]))
flow.append(d.WriteBox(0.75))
flow.append(Spacer(1, 6))

flow.append(Paragraph("Key Dates", S["h3"]))
flow.append(d.FillInRow([("Agreement Date:", 0.5), ("Work Start Date:", 0.5)]))
flow.append(d.FillInRow([("Substantial Completion Date:", 0.5),
                         ("Final Completion Date:", 0.5)]))
flow += article_end()

# ---------------- ARTICLE 2
flow += d.h2("ARTICLE 2 — SCOPE OF WORK", S)

flow.append(d.WriteBox(2.75, label="Detailed Description of Work to be Performed"))
flow.append(Spacer(1, 8))

flow.append(Paragraph("Specifications and Standards", S["h3"]))
flow.append(FieldLine("Work shall comply with all applicable building codes and "
                      "regulations", box=True, rule=False))
flow.append(FieldLine("Work shall comply with approved plans dated:", box=True))
flow.append(FieldLine("Work shall meet industry standards for:", box=True))
flow.append(FieldLine("Other specifications:", box=True))
flow.append(Spacer(1, 6))

flow.append(Paragraph("Materials", S["h3"]))
flow.append(d.WriteBox(1.35, label="Materials to be provided by Subcontractor"))
flow.append(Spacer(1, 8))
flow.append(d.WriteBox(1.35, label="Materials to be provided by Owner"))
flow.append(Spacer(1, 8))

flow.append(d.WriteBox(1.6, label="Exclusions — work NOT included in this agreement"))
flow += article_end()

# ---------------- ARTICLE 3
flow += d.h2("ARTICLE 3 — PAYMENT TERMS", S)

flow.append(d.FillIn("Total Contract Amount ($):"))
flow.append(Spacer(1, 4))

pay_rows = [[str(n), "", ""] for n in range(1, 6)]
pay_table = d.titled_table(
    "Payment Schedule",
    [Paragraph("Draw #", S["cell-bold"]),
     Paragraph("Milestone / Completion Point", S["cell-bold"]),
     Paragraph("Amount ($)", S["cell-bold"])],
    pay_rows, [0.85 * inch, 4.15 * inch, 2.0 * inch], S)
pay_table.setStyle(d.TableStyle([("ALIGN", (0, 2), (0, -1), "CENTER")]))
flow.append(pay_table)
flow.append(Spacer(1, 8))

flow.append(d.FillInRow([("Retention (%):", 0.5), ("Retention Amount ($):", 0.5)]))
flow.append(FieldLine("Payment due within", rule_w=54,
                      tail="days of invoice submission"))
flow.append(Spacer(1, 4))

flow.append(Paragraph("Final Payment Conditions", S["h3"]))
flow.append(Paragraph("Final payment shall be made upon:", S["body"]))
flow.append(d.items_checklist([
    "Completion of all work per specifications",
    "Passing final inspection",
    "Receipt of unconditional lien waiver from Subcontractor",
    "Receipt of lien waivers from all material suppliers",
    "Submission of warranties and operating manuals (if applicable)",
    "Correction of any punch list items",
], S))
flow.append(Spacer(1, 6))

flow.append(Paragraph("Change Orders", S["h3"]))
flow.append(Paragraph(
    "All changes to the scope of work must be approved in writing via Change "
    "Order Form before work begins. No additional payment will be made for work "
    "performed without a signed change order.", S["body"]))
flow.append(Paragraph("Change orders must include:", S["body"]))
flow += bullets([
    "Detailed description of change",
    "Cost impact (materials and labor)",
    "Schedule impact",
    "Signatures of both parties",
])
flow += article_end()

# ---------------- ARTICLE 4
flow += d.h2("ARTICLE 4 — LEGAL REQUIREMENTS AND RESPONSIBILITIES", S)

flow.append(Paragraph("Insurance Requirements", S["h3"]))
flow.append(Paragraph(
    "Subcontractor shall maintain the following insurance coverage throughout "
    "the duration of this agreement:", S["body"]))
flow.append(FieldLine("General Liability Insurance: Minimum $", box=True, rule_w=110,
                      tail="per occurrence"))
flow.append(FieldLine("Workers' Compensation Insurance (if required by state law)",
                      box=True, rule=False))
flow.append(FieldLine("Vehicle Insurance: Minimum $", box=True, rule_w=110,
                      tail="per occurrence"))
flow.append(Paragraph(
    "Subcontractor shall provide Certificate of Insurance to Owner before work "
    "begins.", S["body"]))
flow.append(Spacer(1, 4))

flow.append(Paragraph("License Verification", S["h3"]))
flow.append(FieldLine("Subcontractor license verified with state licensing board",
                      box=True, rule=False))
flow.append(FieldLine("License in good standing as of:", box=True))
flow.append(Spacer(1, 4))

flow.append(Paragraph("Lien Waivers", S["h3"]))
flow.append(Paragraph("Subcontractor agrees to provide:", S["body"]))
flow += bullets([
    "Conditional lien waiver with each progress payment request",
    "Unconditional lien waiver upon receipt of each progress payment",
    "Final unconditional lien waiver upon receipt of final payment",
    "Lien waivers from all material suppliers and sub-subcontractors",
])
flow.append(Spacer(1, 4))

flow.append(Paragraph("Warranty", S["h3"]))
flow.append(Paragraph("Subcontractor warrants that all work shall be:", S["body"]))
flow += bullets([
    "Performed in a workmanlike manner",
    "Free from defects in materials and workmanship",
    "In compliance with all applicable codes and regulations",
    "Performed by qualified personnel",
])
flow.append(FieldLine("Warranty Period:", rule_w=110,
                      tail="from date of substantial completion"))
flow.append(Paragraph(
    "Subcontractor shall promptly correct any defects in materials or "
    "workmanship that appear during the warranty period at no additional cost "
    "to Owner.", S["body"]))
flow.append(Spacer(1, 4))

flow.append(Paragraph("Permits and Inspections", S["h3"]))
flow.append(d.checkbox_choice_row("Permits obtained by (check one):",
                                  ["Owner", "Subcontractor"], S))
flow.append(Spacer(1, 4))
flow.append(Paragraph(
    "Subcontractor shall notify Owner at least 48 hours before inspections are "
    "required and shall coordinate with inspector to schedule inspections. "
    "Subcontractor shall correct any work that fails inspection at no "
    "additional cost to Owner.", S["body"]))
flow += article_end()

# ---------------- ARTICLE 5
flow += d.h2("ARTICLE 5 — DISPUTE RESOLUTION", S)
flow.append(Paragraph(
    "Any disputes arising under this agreement shall be resolved as follows:",
    S["body"]))
flow += numbered([
    "<b>Direct Communication:</b> Parties shall first attempt to resolve "
    "disputes through direct communication within 7 days of dispute arising.",
    "<b>Written Notice:</b> If dispute is not resolved, the aggrieved party "
    "shall provide written notice detailing the dispute within 14 days.",
    "<b>Meeting:</b> Parties shall meet in person within 14 days of written "
    "notice to attempt resolution.",
    "<b>Mediation:</b> If meeting does not resolve dispute, parties agree to "
    "participate in mediation with a mutually agreed upon mediator. Cost of "
    "mediation shall be split equally.",
    "<b>Arbitration / Litigation:</b> If mediation fails, parties may pursue "
    "the option selected below.",
])
flow.append(Spacer(1, 4))
flow.append(d.checkbox_choice_row("If mediation fails (check one):",
                                  ["Binding arbitration", "Litigation"], S))
flow.append(d.FillInRow([("Litigation venue — County:", 0.55), ("State:", 0.45)]))
flow.append(Spacer(1, 4))

flow.append(Paragraph("Termination", S["h3"]))
flow.append(Paragraph(
    "<b>By Owner:</b> Owner may terminate this agreement for cause (failure to "
    "perform, safety violations, code violations) with 7 days written notice. "
    "Owner may terminate without cause with 14 days written notice.", S["body"]))
flow.append(Paragraph(
    "<b>By Subcontractor:</b> Subcontractor may terminate for non-payment after "
    "providing 14 days written notice and opportunity to cure.", S["body"]))
flow.append(Paragraph(
    "Upon termination, Subcontractor shall be paid for all work completed to "
    "date, less any costs incurred by Owner to correct deficiencies.", S["body"]))
flow.append(Spacer(1, 4))

flow.append(Paragraph("Indemnification", S["h3"]))
flow.append(Paragraph(
    "Subcontractor agrees to indemnify and hold harmless Owner from any claims, "
    "damages, losses, or expenses (including attorney fees) arising from:",
    S["body"]))
flow += bullets([
    "Subcontractor's negligent acts or omissions",
    "Injury to persons or property caused by Subcontractor or its employees",
    "Failure to comply with applicable laws and regulations",
    "Claims by Subcontractor's employees, suppliers, or sub-subcontractors",
])
flow += article_end()

# ---------------- ARTICLE 6
flow += d.h2("ARTICLE 6 — ADDITIONAL TERMS AND CONDITIONS", S)

flow.append(Paragraph("Site Access and Scheduling", S["h3"]))
flow.append(Paragraph(
    "Subcontractor shall coordinate work schedule with Owner and other trades.",
    S["body"]))
flow.append(d.FillIn("Site access hours:"))

flow.append(Paragraph("Cleanup", S["h3"]))
flow.append(Paragraph(
    "Subcontractor shall maintain a clean and safe work area and remove all "
    "debris and materials at the end of each workday. Final cleanup shall "
    "include removal of all tools, equipment, and materials.", S["body"]))

flow.append(Paragraph("Safety", S["h3"]))
flow.append(Paragraph(
    "Subcontractor shall comply with all OSHA regulations and maintain a safe "
    "work environment. Subcontractor is responsible for safety of its employees "
    "and shall provide all required personal protective equipment.", S["body"]))

flow.append(Paragraph("Damage to Property", S["h3"]))
flow.append(Paragraph(
    "Subcontractor shall be responsible for any damage to existing structures, "
    "fixtures, or property caused by Subcontractor or its employees.", S["body"]))

flow.append(Paragraph("Assignment", S["h3"]))
flow.append(Paragraph(
    "This agreement may not be assigned without written consent of both "
    "parties.", S["body"]))

flow.append(Paragraph("Entire Agreement", S["h3"]))
flow.append(Paragraph(
    "This agreement constitutes the entire agreement between parties and "
    "supersedes all prior negotiations, representations, or agreements. This "
    "agreement may only be modified by written amendment signed by both "
    "parties.", S["body"]))

flow.append(Paragraph("Governing Law", S["h3"]))
flow.append(FieldLine("This agreement shall be governed by the laws of the State of"))
flow += article_end()

# ---------------- SIGNATURES
flow += d.h2("SIGNATURES", S)
flow.append(Paragraph(
    "By signing below, parties acknowledge they have read, understood, and "
    "agree to all terms and conditions of this agreement.", S["body"]))
flow.append(Spacer(1, 6))

flow.append(KeepTogether([
    Paragraph("Owner / General Contractor", S["h3"]),
    *d.signature_block([("Signature", True)]),
    d.FillIn("Print Name:"),
]))
flow.append(Spacer(1, 10))
flow.append(KeepTogether([
    Paragraph("Subcontractor", S["h3"]),
    *d.signature_block([("Signature", True)]),
    d.FillInRow([("Print Name:", 0.5), ("Title:", 0.5)]),
]))
flow.append(Spacer(1, 10))
flow.append(KeepTogether([
    Paragraph("Witness (optional)", S["h3"]),
    *d.signature_block([("Signature", True)]),
    d.FillIn("Print Name:"),
]))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-2-contracts-legal",
                       "2.1-subcontractor-agreement-template.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
