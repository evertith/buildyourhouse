#!/usr/bin/env python3
"""2.8 Dispute Resolution Procedure — 2026 design system."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import Flowable, Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 2: Contracts & Legal Documents"
FORM_ID = "2.8"
FORM_TITLE = "Dispute Resolution Procedure"

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


def step_meta(timeline, objective):
    """The timeline / objective strip that opens each step."""
    return d.callout_box(None, [
        Paragraph(f"<b>Timeline:</b> {timeline}", S["body"]),
        Paragraph(f"<b>Objective:</b> {objective}", S["body"])])


def pros_cons(pros, cons):
    return d.std_table(
        [[Paragraph("Pros", S["cell-bold"]), Paragraph("Cons", S["cell-bold"])],
         [[Paragraph(p, CELL_BULLET, bulletText="•") for p in pros],
          [Paragraph(c, CELL_BULLET, bulletText="•") for c in cons]]],
        [3.5 * inch, 3.5 * inch], header_rows=1)


# ---------------------------------------------------------------- document

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Five escalating steps from a phone call to a courtroom. Work them "
            "in order and document each one — most disputes die at step one or "
            "two, and the paper trail is what wins the ones that don't.")
flow.append(Paragraph(DISCLAIMER, S["note"]))
flow.append(Spacer(1, 4))

flow.append(d.FillIn("Project Name:"))
flow.append(d.FillIn("Project Address:"))
flow.append(d.FillIn("Owner:"))
flow.append(Spacer(1, 4))
flow.append(Paragraph(
    "This document outlines the procedures for resolving disputes between the "
    "owner and contractors / subcontractors. Following these steps can help "
    "resolve issues efficiently and cost-effectively while maintaining "
    "professional relationships.", S["body"]))

# ================================================================ STEP 1
flow += d.h2("STEP 1: INITIAL COMMUNICATION", S)
flow.append(step_meta("Within 3 business days of issue arising",
                      "Resolve the issue through direct, informal communication"))
flow.append(Spacer(1, 8))
flow.append(Paragraph("Actions", S["h3"]))
flow += numbered([
    "Identify the specific issue or concern",
    "Contact the other party directly (phone call or in-person meeting preferred)",
    "Discuss the issue calmly and professionally",
    "Listen to the other party's perspective",
    "Attempt to reach a mutually acceptable solution",
    "Document the conversation and any agreements reached",
])
flow.append(Spacer(1, 4))
flow.append(Paragraph("Documentation", S["h3"]))
flow.append(d.FillIn("Date of communication:"))
flow.append(d.checkbox_choice_row("Method:",
                                  ["Phone", "In-person", "Email", "Text"], S))
flow.append(d.FillIn("Parties involved:"))
flow.append(d.WriteBox(1.35, label="Summary of discussion"))
flow.append(Spacer(1, 6))
flow.append(d.checkbox_choice_row("Agreement reached:", ["Yes", "No"], S))
flow.append(d.WriteBox(1.1, label="If yes, describe"))
flow.append(Spacer(1, 6))
flow.append(Paragraph(
    "If the issue is resolved at this step, no further action is needed. If not "
    "resolved, proceed to Step 2.", S["body-bold"]))

# ================================================================ STEP 2
flow += d.h2("STEP 2: WRITTEN NOTICE", S)
flow.append(step_meta("Within 7 business days if Step 1 does not resolve the issue",
                      "Formally document the dispute and proposed resolution"))
flow.append(Spacer(1, 8))
flow.append(Paragraph("Actions", S["h3"]))
flow += numbered(["Prepare written notice of dispute including the items below"])
flow += bullets([
    "Detailed description of the issue",
    "Relevant contract provisions or agreements",
    "Timeline of events",
    "Supporting documentation (photos, invoices, emails, etc.)",
    "Desired resolution",
    "Deadline for response (typically 7 business days)",
], style=SUBBULLET)
flow += [Paragraph(t, BULLET, bulletText=f"{i}.") for i, t in enumerate([
    "Deliver notice via certified mail, return receipt requested",
    "Keep copies of all documentation",
    "Await written response from other party",
], start=2)]
flow.append(Spacer(1, 4))
flow.append(Paragraph("Written Notice Checklist", S["h3"]))
flow.append(d.items_checklist([
    "Description of dispute clearly stated",
    "Relevant dates and timeline included",
    "Supporting documents attached",
    "Specific resolution requested",
    "Response deadline specified",
    "Sent via certified mail",
    "Copy kept for records",
], S))
flow.append(Spacer(1, 6))
flow.append(Paragraph("Documentation", S["h3"]))
flow.append(d.FillInRow([("Date notice sent:", 0.5),
                         ("Date response received:", 0.5)]))
flow.append(d.FillIn("Certified mail tracking #:"))
flow.append(d.WriteBox(1.35, label="Response summary"))
flow.append(Spacer(1, 6))
flow.append(d.checkbox_choice_row("Agreement reached:", ["Yes", "No"], S))
flow.append(Spacer(1, 4))
flow.append(Paragraph(
    "If the issue is resolved at this step, document the agreement in writing "
    "and have both parties sign. If not resolved, proceed to Step 3.",
    S["body-bold"]))

# ================================================================ STEP 3
flow += d.h2("STEP 3: FORMAL MEETING", S)
flow.append(step_meta(
    "Within 14 business days of written notice if issue remains unresolved",
    "Meet face-to-face to negotiate a resolution"))
flow.append(Spacer(1, 8))
flow.append(Paragraph("Actions", S["h3"]))
flow += numbered(["Schedule meeting at mutually convenient time and neutral "
                  "location",
                  "Both parties should bring:"])
flow += bullets([
    "All relevant documentation",
    "Contract and any change orders",
    "Photos, invoices, correspondence",
    "Witnesses (if applicable)",
], style=SUBBULLET)
flow.append(Paragraph("Conduct meeting professionally:", BULLET, bulletText="3."))
flow += bullets([
    "Present facts and evidence",
    "Allow each party to speak without interruption",
    "Focus on solutions, not blame",
    "Explore compromise options",
], style=SUBBULLET)
flow += [Paragraph(t, BULLET, bulletText=f"{i}.") for i, t in enumerate([
    "Document meeting minutes and any agreements",
    "Both parties sign meeting summary",
], start=4)]
flow.append(Spacer(1, 4))
flow.append(Paragraph("Meeting Documentation", S["h3"]))
flow.append(d.FillInRow([("Date of meeting:", 0.5), ("Time:", 0.5)]))
flow.append(d.FillIn("Location:"))
flow.append(d.FillIn("Attendees:"))
flow.append(d.WriteBox(1.8, label="Summary of discussion"))
flow.append(Spacer(1, 6))
flow.append(d.WriteBox(1.35, label="Proposed solutions discussed"))
flow.append(Spacer(1, 6))
flow.append(d.checkbox_choice_row("Agreement reached:", ["Yes", "No"], S))
flow.append(Spacer(1, 4))
flow.append(Paragraph(
    "If agreement is reached, both parties must sign a written settlement "
    "agreement. If not resolved, proceed to Step 4.", S["body-bold"]))

# ================================================================ STEP 4
flow += d.h2("STEP 4: MEDIATION", S)
flow.append(step_meta("Within 30 days if Steps 1–3 do not resolve the issue",
                      "Use a neutral third-party mediator to facilitate "
                      "resolution"))
flow.append(Spacer(1, 8))
flow.append(Paragraph("What is Mediation?", S["h3"]))
flow.append(Paragraph(
    "Mediation is a voluntary process where a neutral third party (mediator) "
    "helps both sides reach a mutually acceptable agreement. The mediator does "
    "not make decisions but facilitates communication and negotiation.",
    S["body"]))
flow.append(Paragraph("Benefits of Mediation", S["h3"]))
flow += bullets([
    "Less expensive than arbitration or litigation",
    "Faster resolution (typically 1–2 sessions)",
    "Confidential process",
    "Preserves business relationships",
    "Both parties control the outcome",
    "Non-binding (unless agreement is reached)",
])
flow.append(Spacer(1, 4))
flow.append(Paragraph("Actions", S["h3"]))
flow += numbered(["Both parties agree to participate in mediation",
                  "Select mediator:"])
flow += bullets([
    "Mutually agreed upon individual",
    "Local mediation service",
    "Construction dispute specialist",
], style=SUBBULLET)
flow += [Paragraph(t, BULLET, bulletText=f"{i}.") for i, t in enumerate([
    "Split mediation costs equally (unless otherwise agreed)",
    "Prepare mediation statement outlining position and desired outcome",
    "Attend mediation session(s)",
    "If agreement is reached, sign binding settlement agreement",
], start=3)]
flow.append(Spacer(1, 4))
flow.append(Paragraph("Mediation Resources", S["h3"]))
flow += bullets([
    "American Arbitration Association (AAA): www.adr.org",
    "Local bar association mediation services",
    "State court-annexed mediation programs",
    "Private mediation services",
])
flow.append(Spacer(1, 4))
flow.append(Paragraph("Mediation Documentation", S["h3"]))
flow.append(d.FillIn("Mediator selected:"))
flow.append(d.FillInRow([("Contact:", 0.62), ("Phone:", 0.38)]))
flow.append(d.FillInRow([("Date of mediation:", 0.5),
                         ("Cost, split equally ($):", 0.5)]))
flow.append(d.checkbox_choice_row("Agreement reached:", ["Yes", "No"], S))
flow.append(d.WriteBox(1.1, label="Settlement amount / terms"))
flow.append(Spacer(1, 6))
flow.append(Paragraph(
    "If mediation is successful, both parties sign a settlement agreement and "
    "the dispute is resolved. If mediation fails, proceed to Step 5.",
    S["body-bold"]))

# ================================================================ STEP 5
flow += d.h2("STEP 5: ARBITRATION OR LITIGATION", S)
flow.append(step_meta("If all other methods fail",
                      "Obtain a binding decision from an arbitrator or court"))
flow.append(Spacer(1, 8))

flow.append(Paragraph("Option A: Binding Arbitration", S["h3"]))
flow.append(Paragraph(
    "Arbitration is a formal process where a neutral arbitrator (like a private "
    "judge) hears evidence from both sides and makes a binding decision. The "
    "decision is final and generally cannot be appealed.", S["body"]))
flow += numbered([
    "File demand for arbitration with arbitration organization (AAA, JAMS, etc.)",
    "Pay filing fee (typically $1,000–$3,000+)",
    "Select arbitrator (or use arbitration service's selection process)",
    "Conduct discovery (exchange of information / evidence)",
    "Attend arbitration hearing",
    "Arbitrator issues binding decision",
    "Decision is enforceable in court",
])
flow.append(Spacer(1, 6))
flow.append(pros_cons(
    ["Faster than court litigation", "Less formal procedures",
     "Arbitrator may have construction expertise", "Private and confidential"],
    ["Can be expensive (arbitrator fees, attorney fees)",
     "Limited appeal rights", "Discovery may be limited"]))

flow.append(Paragraph("Option B: Small Claims Court", S["h3"]))
flow.append(Paragraph(
    "Small claims court is appropriate when the dispute amount is below the "
    "state's small claims limit (typically $5,000–$10,000 depending on state).",
    S["body"]))
flow += numbered([
    "File claim at county small claims court",
    "Pay filing fee (typically $30–$100)",
    "Serve defendant with claim",
    "Attend hearing (no attorneys required in most states)",
    "Present evidence to judge",
    "Judge issues decision (usually immediately)",
])
flow.append(Spacer(1, 6))
flow.append(pros_cons(
    ["Inexpensive and fast", "Simple procedures, no attorney needed",
     "Quick resolution (typically within 30–90 days)"],
    ["Limited to lower dollar amounts", "Limited discovery",
     "Appeal rights may be limited"]))

flow.append(Paragraph("Option C: Civil Litigation", S["h3"]))
flow.append(Paragraph(
    "Civil litigation in regular court is typically used for larger disputes "
    "exceeding small claims limits or when arbitration is not required by "
    "contract.", S["body"]))
flow += numbered([
    "Hire attorney",
    "File complaint in civil court",
    "Serve defendant with complaint",
    "Defendant files answer",
    "Discovery phase (depositions, interrogatories, document requests)",
    "Pre-trial motions and hearings",
    "Trial (before judge or jury)",
    "Judge or jury renders verdict",
    "Right to appeal",
])
flow.append(Spacer(1, 6))
flow.append(pros_cons(
    ["Full discovery rights", "Right to jury trial", "Right to appeal",
     "Established rules of evidence and procedure"],
    ["Expensive (attorney fees, court costs, expert witnesses)",
     "Time-consuming (can take 1–3+ years)", "Public record",
     "Uncertain outcome"]))

# ================================================================ documentation
flow += d.h2("DOCUMENTATION REQUIREMENTS", S)
flow.append(Paragraph(
    "Throughout the dispute resolution process, maintain documentation of:",
    S["body"]))
flow.append(d.items_checklist([
    "All communications (emails, letters, text messages)",
    "Meeting notes and summaries",
    "Photos of disputed work or conditions",
    "Invoices, payment records, receipts",
    "Contract and any change orders",
    "Relevant building codes or specifications",
    "Expert reports or inspections",
    "Timeline of events",
    "Witness statements",
    "Any other relevant evidence",
], S))
flow.append(Spacer(1, 4))
flow.append(d.FillIn("Documentation storage location:"))

# ================================================================ timeline summary
flow += d.h2("TIMELINE SUMMARY", S)
flow.append(d.titled_table(
    "Escalation at a Glance",
    [Paragraph("Step", S["cell-bold"]), Paragraph("Timeline", S["cell-bold"]),
     Paragraph("Action", S["cell-bold"])],
    [[Paragraph(a, S["cell"]), Paragraph(b, S["cell"]), Paragraph(c, S["cell"])]
     for a, b, c in [
         ("1. Initial Communication", "3 days",
          "Direct communication to resolve issue"),
         ("2. Written Notice", "7 days", "Formal written notice of dispute"),
         ("3. Formal Meeting", "14 days", "Face-to-face negotiation meeting"),
         ("4. Mediation", "30 days", "Third-party mediation"),
         ("5. Arbitration / Litigation", "As needed",
          "Binding arbitration or court"),
     ]],
    [1.9 * inch, 1.1 * inch, 4.0 * inch], S, write_rows=False))
flow.append(Spacer(1, 10))

flow.append(d.callout_box("IMPORTANT NOTES", bullets([
    "Attempt to resolve disputes at the earliest possible step",
    "Keep all communications professional and documented",
    "Consult with an attorney before proceeding to arbitration or litigation",
    "Check your contract for specific dispute resolution requirements",
    "Be aware of statute of limitations for filing claims in your state",
    "Consider the cost of dispute resolution versus the amount in dispute",
])))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-2-contracts-legal",
                       "2.8-dispute-resolution-procedure.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
