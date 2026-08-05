#!/usr/bin/env python3
"""2.3 Lien Waiver Templates — 2026 design system.

Four waiver variants: conditional / unconditional x partial / final payment.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Flowable, KeepTogether, Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 2: Contracts & Legal Documents"
FORM_ID = "2.3"
FORM_TITLE = "Lien Waiver Templates"

DISCLAIMER = ("Template for general reference — have your attorney review before "
              "use. Not legal advice. Several states prescribe the exact wording "
              "of lien waivers; check your state's statute before signing.")

BULLET = ParagraphStyle("bullet2", parent=S["bullet"], bulletFontName=d.BODY,
                        bulletFontSize=10.5)

WARNING = (
    "<b>WARNING:</b> This document waives rights unconditionally and states that "
    "you have been paid for giving up those rights. This document is enforceable "
    "against you if you sign it, even if you have not been paid. If you have not "
    "been paid, use a conditional waiver and release form.")

WARNING_CONDITIONAL = (
    "<b>NOTICE:</b> This waiver is CONDITIONAL. It becomes effective only when "
    "the payment identified below is actually received by the person signing. "
    "If that payment is not received, this document waives nothing. To "
    "acknowledge a payment already received, use an unconditional waiver "
    "instead.")

WARNING_CONDITIONAL_FINAL = (
    "<b>NOTICE:</b> This waiver is CONDITIONAL. It waives all remaining lien "
    "rights only when the FINAL payment identified below is actually received "
    "by the person signing. If that payment is not received, this document "
    "waives nothing. To acknowledge final payment already received, use an "
    "unconditional final waiver instead.")

WARNING_FINAL = (
    "<b>WARNING:</b> This document waives ALL rights unconditionally and states "
    "that you have been paid IN FULL for giving up those rights. This document is "
    "enforceable against you if you sign it, even if you have not been paid. If "
    "you have not been paid in full, use a conditional waiver and release form.")


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


def project_block():
    return [d.FillIn("Project Name:"),
            d.FillIn("Project Address:"),
            d.FillInRow([("Owner Name:", 0.62), ("Date:", 0.38)])]


def claimant_and_signature(warning_text):
    """Claimant identity, execution rules and the statutory-style warning, kept
    together so a waiver can never be signed away from its own warning."""
    return [KeepTogether([
        Paragraph("Company / Individual Information", S["body-bold"]),
        d.FillInRow([("Name of Claimant:", 0.5), ("Company Name:", 0.5)]),
        d.FillInRow([("License Number:", 0.5), ("Phone:", 0.5)]),
        d.FillIn("Address:"),
        Spacer(1, 6),
        *d.signature_block([("Signature", True)]),
        d.FillInRow([("Print Name:", 0.5), ("Title:", 0.5)]),
        Spacer(1, 6),
        d.callout_box(None, [Paragraph(warning_text, S["body"])]),
    ])]


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Four waivers covering every payment situation — conditional or "
            "unconditional, progress payment or final. Collect the matching "
            "waiver with every cheque you write.")
flow.append(Paragraph(DISCLAIMER, S["note"]))

# ================================================================ 1. CONDITIONAL / PARTIAL
flow += d.h2("CONDITIONAL LIEN WAIVER (Partial Payment)", S)
flow += project_block()
flow.append(Spacer(1, 4))
flow.append(KeepTogether([Paragraph(
    "Upon receipt of payment in the amount stated under Payment Information "
    "below, the undersigned hereby waives and releases any and all lien rights, "
    "stop payment notice rights, and bond rights the undersigned has or may have "
    "against the above-referenced property for labor, services, equipment, or "
    "materials furnished to the property through the through-date stated below.",
    S["body"]),
    Paragraph(
    "<b>This waiver is CONDITIONAL upon payment.</b> This waiver and release is "
    "void and of no effect unless and until the undersigned actually receives "
    "payment in the amount stated above.", S["body"])]))

flow.append(Paragraph("Payment Information", S["body-bold"]))
flow.append(d.FillInRow([("Payment Amount ($):", 0.5), ("Check Number:", 0.5)]))
flow.append(d.FillInRow([("Date of Check:", 0.5), ("Through-Date:", 0.5)]))
flow.append(d.FillInRow([("Payment Period — From:", 0.55), ("To:", 0.45)]))

flow.append(Paragraph("Exceptions", S["body-bold"]))
flow.append(Paragraph("This waiver does not cover:", S["body"]))
flow += bullets([
    "Any work, materials, or services provided after the through-date listed above",
    "Any retention amounts held",
])
flow.append(FieldLine("Disputed claims for extra work in the amount of $",
                      rule_w=120))
flow.append(FieldLine("Other exceptions:"))
flow += claimant_and_signature(WARNING_CONDITIONAL)

# ================================================================ 2. UNCONDITIONAL / PARTIAL
flow += d.h2("UNCONDITIONAL LIEN WAIVER (Partial Payment)", S)
flow += project_block()
flow.append(Spacer(1, 4))
flow.append(KeepTogether([Paragraph(
    "The undersigned has been paid and has received progress payment in the "
    "amount stated under Payment Information below, and hereby waives and "
    "releases any and all lien rights, stop payment notice rights, and bond "
    "rights the undersigned has or may have against the above-referenced "
    "property for labor, services, equipment, or materials furnished to the "
    "property through the through-date stated below.", S["body"]),
    Paragraph(
    "<b>This waiver is UNCONDITIONAL.</b> This waiver and release is effective "
    "immediately upon signing and is not dependent upon receipt of payment.",
    S["body"])]))

flow.append(Paragraph("Payment Information", S["body-bold"]))
flow.append(d.FillInRow([("Payment Amount Received ($):", 0.55),
                         ("Check Number:", 0.45)]))
flow.append(d.FillInRow([("Date Payment Received:", 0.55),
                         ("Through-Date:", 0.45)]))
flow.append(d.FillInRow([("Payment Period — From:", 0.55), ("To:", 0.45)]))

flow.append(Paragraph("Amount Summary", S["body-bold"]))
flow.append(d.FillInRow([("Total contract amount to date ($):", 0.55),
                         ("Previous payments received ($):", 0.45)]))
flow.append(d.FillInRow([("This payment amount ($):", 0.5),
                         ("Balance remaining ($):", 0.5)]))

flow.append(Paragraph("Exceptions", S["body-bold"]))
flow.append(Paragraph("This waiver does not cover:", S["body"]))
flow += bullets([
    "Any work, materials, or services provided after the through-date listed above",
])
flow.append(FieldLine("Retention amounts held in the amount of $", rule_w=120))
flow.append(FieldLine("Disputed claims for extra work in the amount of $",
                      rule_w=120))
flow.append(FieldLine("Other exceptions:"))
flow += claimant_and_signature(WARNING)

# ================================================================ 3. CONDITIONAL / FINAL
flow += d.h2("CONDITIONAL LIEN WAIVER (Final Payment)", S)
flow += project_block()
flow.append(Spacer(1, 4))
flow.append(KeepTogether([Paragraph(
    "Upon receipt of FINAL payment in the amount stated under Final Payment "
    "Information below, the undersigned hereby waives and releases any and all "
    "lien rights, stop payment notice rights, and bond rights the undersigned "
    "has or may have against the above-referenced property for all labor, "
    "services, equipment, or materials furnished to the property.", S["body"]),
    Paragraph(
    "<b>This waiver is CONDITIONAL upon receipt of final payment.</b> This "
    "waiver and release is void and of no effect unless and until the "
    "undersigned actually receives final payment in the amount stated above.",
    S["body"])]))

flow.append(Paragraph("Final Payment Information", S["body-bold"]))
flow.append(d.FillInRow([("Total Contract Amount ($):", 0.5),
                         ("Previous Payments Received ($):", 0.5)]))
flow.append(d.FillInRow([("Final Payment Amount ($):", 0.5),
                         ("Check Number:", 0.5)]))
flow.append(d.FillInRow([("Date of Check:", 0.5),
                         ("Retention amount released ($):", 0.5)]))

flow.append(Paragraph("Certification", S["body-bold"]))
flow.append(Paragraph("The undersigned certifies that:", S["body"]))
flow.append(d.items_checklist([
    "All work has been completed per contract specifications",
    "All materials have been paid for",
    "All subcontractors and suppliers have been paid in full",
    "All required warranties have been provided to owner",
    "All punch list items have been completed",
], S))

flow.append(Paragraph("Exceptions", S["body-bold"]))
flow.append(d.WriteBox(
    1.15, label="This waiver does not cover (if none, write “NONE”)"))
flow.append(Spacer(1, 6))
flow += claimant_and_signature(WARNING_CONDITIONAL_FINAL)

# ================================================================ 4. UNCONDITIONAL / FINAL
flow += d.h2("UNCONDITIONAL LIEN WAIVER (Final Payment)", S)
flow += project_block()
flow.append(Spacer(1, 4))
flow.append(KeepTogether([Paragraph(
    "The undersigned has been paid in full and has received FINAL payment in the "
    "amount stated under Final Payment Information below, and hereby waives and "
    "releases any and all lien rights, stop payment notice rights, and bond "
    "rights the undersigned has or may have against the above-referenced "
    "property for all labor, services, equipment, or materials furnished to the "
    "property.", S["body"]),
    Paragraph(
    "<b>This waiver is UNCONDITIONAL and FINAL.</b> This waiver and release is "
    "effective immediately upon signing and releases all rights to file liens or "
    "claims against the property.", S["body"])]))

flow.append(Paragraph("Final Payment Information", S["body-bold"]))
flow.append(d.FillInRow([("Total Contract Amount ($):", 0.5),
                         ("Total Change Orders ($):", 0.5)]))
flow.append(d.FillInRow([("Final Contract Amount ($):", 0.5),
                         ("Previous Payments Received ($):", 0.5)]))
flow.append(d.FillInRow([("Retention Released ($):", 0.5),
                         ("Final Payment Amount ($):", 0.5)]))
flow.append(d.FillInRow([("Check Number:", 0.5),
                         ("Date Payment Received:", 0.5)]))

flow.append(Paragraph("Final Certification", S["body-bold"]))
flow.append(Paragraph("The undersigned certifies that:", S["body"]))
flow.append(d.items_checklist([
    "All work has been completed per contract specifications",
    "All materials have been paid for in full",
    "All subcontractors and suppliers have been paid in full",
    "All required warranties have been provided to owner",
    "All punch list items have been completed",
    "Final inspection has been passed",
    "No outstanding claims or disputes exist",
], S))

flow.append(Paragraph("Exceptions", S["body-bold"]))
flow.append(d.callout_box(None, [Paragraph(
    "This is a FINAL waiver with NO exceptions. If any claims remain, do NOT "
    "sign this form.", S["body-bold"])]))
flow.append(Spacer(1, 6))
flow += claimant_and_signature(WARNING_FINAL)


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-2-contracts-legal",
                       "2.3-lien-waiver-templates.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
