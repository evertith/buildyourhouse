#!/usr/bin/env python3
"""6.1 Daily Job Site Log — rebuilt on the 2026 design system.

The browser-printed original leaked a stray copyright line and a duplicate
running header into the body on most pages, overprinting table rows. All of
that production junk is dropped here. The original also carried one full log
plus three abbreviated blank templates; that structure is kept, with the
templates sized to photocopy as a two-page spread.
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
    PageBreak,
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
FORM_ID = "6.1"
FORM_TITLE = "Daily Job Site Log"


# ---------------------------------------------------------------- local parts

class ChoiceSet(Flowable):
    """Drawn checkbox options that wrap to the available width."""

    def __init__(self, options, box=10, font_size=9, gap=9, leading=15):
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
            w = self.box + 4 + pdfmetrics.stringWidth(opt, d.BODY, self.font_size)
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
                c.drawString(x + self.box + 4, y + 1.5, opt)
                x += w + self.gap
            y -= self.leading


def hdr(text):
    return Paragraph(text, S["cell-hdr"])


HEADER_PAD = [("LEFTPADDING", (0, 1), (-1, 1), 4),
              ("RIGHTPADDING", (0, 1), (-1, 1), 4)]


def keep_for(n_rows, row_height=34, cap=3.7 * inch, floor=2.1 * inch):
    est = 68 + n_rows * (row_height or 34)
    return est if est <= cap else floor


def data_table(title, headers, rows, col_widths, row_height=34, pad=None,
               keep=None, extra=None):
    heads = [h if isinstance(h, Flowable) else hdr(h) for h in headers]
    t = d.titled_table(title, heads, rows, col_widths, S,
                       row_heights=None if row_height is None
                       else [row_height] * len(rows))
    keep = keep_for(len(rows), row_height) if keep is None else keep
    cmds = list(HEADER_PAD)
    if pad:
        cmds += [("TOPPADDING", (0, 2), (-1, -1), pad),
                 ("BOTTOMPADDING", (0, 2), (-1, -1), pad)]
    if extra:
        cmds += extra
    t.setStyle(TableStyle(cmds))
    return [CondPageBreak(keep), t, Spacer(1, 8)]


def blank_rows(n, ncols):
    return [[""] * ncols for _ in range(n)]


def choice(label, options):
    return d.checkbox_choice_row(label, options, S)


def guide(text):
    return Paragraph(text, S["note"])


# Crew sign-in rows sit at 43pt — the one row height the design review found
# correctly sized for handwriting in the whole binder.
CREW_ROW = 43


def crew_table(rows=6):
    return data_table(
        "Subcontractors on Site",
        ["Subcontractor Name", "Trade", "Crew Size", "Time On / Off",
         "Total Hours"],
        blank_rows(rows, 5),
        [2.0 * inch, 1.4 * inch, 0.9 * inch, 1.35 * inch, 1.35 * inch],
        row_height=CREW_ROW)


# ---------------------------------------------------------------- page 1

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Your primary record of everything that happens on site — one "
            "entry per working day.")

flow.append(Paragraph(
    "<b>PURPOSE:</b> The Daily Job Site Log is your primary record of "
    "everything that happens on your construction site. Complete one entry "
    "for each day work occurs. This log serves as documentation for insurance "
    "claims, disputes, schedule tracking, and your own peace of mind.",
    S["body"]))
flow.append(Spacer(1, 4))

flow.append(Paragraph("Instructions", S["h3"]))
for line in [
    "Fill out this log at the end of each work day while details are fresh",
    "Be specific and detailed — you may need this information months or "
    "years later",
    "Record actual hours, not estimates",
    "Note anything unusual, even if it seems minor at the time",
    "Take photos throughout the day and reference photo numbers in your log",
    "Keep completed logs in chronological order in this binder",
]:
    flow.append(Paragraph("• " + line, S["bullet"]))
flow.append(Spacer(1, 8))

flow.append(d.callout_box(
    "Tips for Effective Daily Logging",
    [Paragraph("• Make entries consistent and complete — establish a routine",
               S["body"]),
     Paragraph("• Record conversations and verbal agreements", S["body"]),
     Paragraph("• Note weather conditions that affect work", S["body"]),
     Paragraph("• Document any changes from the original plan", S["body"]),
     Paragraph("• Keep entries factual and objective", S["body"])]))
flow.append(Spacer(1, 10))

flow.append(d.callout_box(
    "How to use these sheets",
    [Paragraph(
        "A full-detail log follows, then three abbreviated daily templates for "
        "routine days. Photocopy whichever version suits the day and file the "
        "completed sheets in date order.", S["body"])]))

# ---------------------------------------------------------------- full log

flow.append(PageBreak())
flow.append(Paragraph("DAILY JOB SITE LOG — FULL DETAIL", S["title"]))
flow.append(d.FillInRow([("Date:", 0.5), ("Day of Week:", 0.5)]))
flow.append(Spacer(1, 6))

flow += d.h2("SITE CONDITIONS", S)
flow.append(d.FillInRow([("Weather:", 0.6), ("Temperature:", 0.4)]))
flow.append(d.FillInRow([("Hours on Site — Start:", 0.36), ("End:", 0.3),
                         ("Total Hours:", 0.34)]))
flow.append(choice("Site Accessible:", ["Yes", "No"]))
flow.append(d.FillIn("Any Access Issues?", height=26))

flow += d.h2("WHO WAS ON SITE TODAY", S)
flow.append(d.FillIn("Owner-Builder:", height=26))
flow.append(d.FillInRow([("Your Hours:", 0.3), ("to", 0.3), ("Total:", 0.4)]))
flow.append(d.FillInRow([("Helper / Family Member:", 0.6), ("Hours:", 0.4)]))
flow.append(Spacer(1, 6))
flow += crew_table(6)

flow.append(Paragraph("Inspectors", S["h3"]))
flow.append(d.FillInRow([("Inspector Name:", 0.5),
                         ("Type of Inspection:", 0.5)]))
flow.append(d.FillInRow([("Time Arrived:", 0.5), ("Time Departed:", 0.5)]))
flow.append(choice("Result:", ["Pass", "Fail", "Partial"]))
flow.append(Spacer(1, 6))

flow.append(Paragraph("Suppliers / Deliveries", S["h3"]))
flow.append(d.FillInRow([("Supplier Name:", 0.65), ("Time:", 0.35)]))
flow.append(d.WriteBox(0.9, label="Materials Delivered"))
flow.append(Spacer(1, 8))

flow += data_table(
    "Visitors",
    ["Name", "Reason for Visit", "Time", "Notes"],
    blank_rows(4, 4),
    [1.8 * inch, 2.4 * inch, 1.0 * inch, 1.8 * inch])

flow += d.h2("WORK COMPLETED TODAY", S)
flow.append(guide(
    "Be specific and detailed. Describe what was accomplished, where on the "
    "site, and quality of work. This is your primary progress record."))
flow.append(d.WriteBox(3.0, label="Detailed Description of Progress"))
flow.append(Spacer(1, 8))
flow.append(choice("Photos Taken:", ["Yes", "No"]))
flow.append(d.FillIn("Photo Numbers / References:", height=26))
flow.append(choice("Video Taken:", ["Yes", "No"]))
flow.append(d.FillIn("Video File Names:", height=26))

flow += d.h2("MATERIALS DELIVERED TODAY", S)
flow += data_table(
    "Deliveries Received",
    ["Supplier", "Items", "Quantity", "Cost", "PO / Invoice #"],
    blank_rows(5, 5),
    [1.5 * inch, 2.2 * inch, 0.95 * inch, 0.85 * inch, 1.5 * inch])

flow += d.h2("ISSUES / PROBLEMS ENCOUNTERED", S)
flow.append(guide(
    "Document any issues, no matter how small. Include problems with work "
    "quality, materials, schedule, safety, or anything unusual."))

for n in (1, 2, 3):
    flow.append(CondPageBreak(3.6 * inch))
    flow.append(Paragraph(f"Issue #{n}", S["h3"]))
    flow.append(d.WriteBox(1.1, label="Description"))
    flow.append(Spacer(1, 6))
    flow.append(d.WriteBox(0.85, label="Action Taken"))
    flow.append(Spacer(1, 6))
    flow.append(choice("Resolved:", ["Yes", "No", "Partially"]))
    flow.append(choice("Follow-up Needed:", ["Yes", "No"]))
    flow.append(d.WriteBox(0.75, label="Follow-up Details"))
    flow.append(Spacer(1, 8))

flow += d.h2("TOMORROW'S PLAN", S)
flow.append(guide(
    "Plan ahead to ensure materials, tools, and people are ready. This section "
    "helps you stay organized and proactive."))
flow.append(d.FillInRow([("Date:", 0.34), ("Planned Hours:", 0.33),
                         ("to", 0.33)]))
flow.append(choice("Who Will Be On Site:", ["Owner-Builder (you)"]))
flow.append(d.FillIn("Helper:", height=26))
flow.append(d.WriteBox(0.8, label="Subcontractors Expected"))
flow.append(Spacer(1, 6))
flow.append(d.WriteBox(1.0, label="Expected Work to be Completed"))
flow.append(Spacer(1, 8))

flow += data_table(
    "Materials Needed",
    ["Material / Item", "Quantity", "Status", "Action Required"],
    [["", "", ChoiceSet(["On site", "Ordered", "Need to order"], box=9,
                        font_size=8.5, gap=6), ""] for _ in range(4)],
    [2.3 * inch, 0.95 * inch, 1.85 * inch, 1.9 * inch], row_height=44)

flow.append(Paragraph("Inspections Scheduled", S["h3"]))
flow.append(d.FillInRow([("Inspection Type:", 0.5), ("Scheduled Time:", 0.5)]))
flow.append(d.FillInRow([("Inspector Name:", 0.5), ("Confirmation #:", 0.5)]))
flow.append(choice("Ready for Inspection:", ["Yes", "No"]))
flow.append(d.FillIn("If No, What's Needed:", height=26))
flow.append(Spacer(1, 6))

flow.append(Paragraph("Tool & Equipment Needs", S["h3"]))
flow.append(d.items_checklist(["All tools on site and ready"], S))
flow.append(d.WriteBox(0.8, label="Tools / Equipment Needed Tomorrow"))
flow.append(Spacer(1, 6))

flow.append(Paragraph("Expected Deliveries", S["h3"]))
flow.append(d.FillInRow([("Supplier:", 0.6), ("Expected Time:", 0.4)]))
flow.append(d.WriteBox(0.7, label="Items"))

flow += d.h2("SAFETY INCIDENTS", S)
flow.append(choice("Any Injuries Today:", ["Yes", "No"]))
flow.append(choice("Any Near-Misses:", ["Yes", "No"]))
flow.append(Spacer(1, 4))
flow.append(d.callout_box(
    "If yes to either above, complete a Safety Incident Report (Section 6.5) "
    "and reference it here.", []))
flow.append(Spacer(1, 6))
flow.append(d.FillInRow([("Incident Report #:", 0.4),
                         ("Brief Description:", 0.6)]))
flow.append(guide(
    "Note any safety concerns, hazards identified, corrective actions taken, "
    "or safety equipment used."))
flow.append(d.WriteBox(1.5, label="Safety Observations"))

flow += d.h2("NOTES / ADDITIONAL INFORMATION", S)
flow.append(guide(
    "Use this space for any additional information, observations, "
    "conversations, decisions made, or reminders for later."))
flow.append(d.WriteBox(3.2))
flow.append(Spacer(1, 10))
flow.append(d.FillInRow([("Completed By:", 0.36), ("Signature:", 0.34),
                         ("Date:", 0.3)]))


# ---------------------------------------------------------------- quick log

def quick_template():
    """Abbreviated daily template — designed as a two-page photocopy spread."""
    out = [PageBreak()]
    out.append(Paragraph("DAILY JOB SITE LOG — DAILY TEMPLATE", S["title"]))
    out.append(d.FillInRow([("Date:", 0.5), ("Day of Week:", 0.5)]))
    out.append(Spacer(1, 6))

    out += d.h2("SITE CONDITIONS", S)
    out.append(d.FillInRow([("Weather:", 0.6), ("Temperature:", 0.4)]))
    out.append(d.FillInRow([("Hours on Site — Start:", 0.36), ("End:", 0.3),
                            ("Total Hours:", 0.34)]))

    out += d.h2("WHO WAS ON SITE TODAY", S)
    out.append(d.FillIn("Owner-Builder:", height=26))
    out.append(d.FillInRow([("Your Hours:", 0.3), ("to", 0.3),
                            ("Total:", 0.4)]))
    out.append(Spacer(1, 6))
    out += crew_table(4)
    out.append(d.FillInRow([("Inspector:", 0.5), ("Type:", 0.5)]))
    out.append(choice("Result:", ["Pass", "Fail"]))

    out += d.h2("WORK COMPLETED TODAY", S)
    out.append(d.WriteBox(2.2))
    out.append(Spacer(1, 8))
    out.append(choice("Photos Taken:", ["Yes", "No"]))
    out.append(d.FillIn("Photo Numbers:", height=26))

    out += d.h2("MATERIALS DELIVERED TODAY", S)
    out += data_table(
        "Deliveries Received",
        ["Supplier", "Items", "Quantity", "Cost / PO #"],
        blank_rows(4, 4),
        [1.6 * inch, 2.6 * inch, 1.1 * inch, 1.7 * inch])

    out += d.h2("ISSUES / PROBLEMS", S)
    out.append(d.WriteBox(1.1, label="Problem"))
    out.append(Spacer(1, 6))
    out.append(d.WriteBox(0.85, label="Action Taken"))
    out.append(Spacer(1, 6))
    out.append(choice("Resolved:", ["Yes", "No"]))
    out.append(choice("Follow-up Needed:", ["Yes", "No"]))

    out += d.h2("TOMORROW'S PLAN", S)
    out.append(d.FillIn("Date:", height=26))
    out.append(d.WriteBox(0.9, label="Expected Work"))
    out.append(Spacer(1, 6))
    out.append(d.FillIn("Who will be on site:", height=26))
    out.append(d.FillIn("Materials needed:", height=26))
    out.append(d.FillIn("Inspections scheduled:", height=26))

    out += d.h2("SAFETY & NOTES", S)
    out.append(choice("Safety Incidents:", ["Yes", "No"]))
    out.append(d.FillIn("Report #:", height=26))
    out.append(d.WriteBox(2.6, label="Notes"))
    out.append(Spacer(1, 10))
    out.append(d.FillInRow([("Completed By:", 0.6), ("Date:", 0.4)]))
    return out


for _ in range(3):
    flow += quick_template()

flow.append(Spacer(1, 16))
flow.append(d.callout_box(
    "End of Daily Job Site Log",
    [Paragraph("Make copies of blank templates as needed. Keep completed logs "
               "in chronological order.", S["body"])]))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-6-daily-operations",
                       "6.1-daily-job-site-log.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
