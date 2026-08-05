#!/usr/bin/env python3
"""Master materials: cover, spine labels, table of contents, how-to-use guide,
and the eight section title pages.

Per the design review:
- Cover: aligned fill-in rules, vertically centered title block, brand +
  edition line, no overlap between labels and rules.
- Spine: two correctly sized inserts (2" and 3" binders) on one landscape
  sheet, dashed cut lines with crop marks, project-name field.
- TOC: navigates by form number (no fake composite page refs).
- How-to: no "color-coded" claim; hanging-indent bullets; running furniture.
- Title pages: black display type (never grey), section contents listed.
- Title pages are written ONLY into their section folders (no root dupes).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.pagesizes import landscape, letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.platypus import Paragraph, Spacer

import design as d

d.register_fonts()
S = d.make_styles()
OUT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "out")

SECTIONS = [
    ("1", "Project Planning & Foundation", "section-1-project-planning", [
        ("1.1", "Master Project Timeline"),
        ("1.2", "Budget Tracking Spreadsheet"),
        ("1.3", "Permit Application Checklist"),
        ("1.4", "Site Preparation Checklist"),
        ("1.5", "Foundation Checklist"),
        ("1.6", "Foundation Inspection Form"),
        ("1.7", "Excavation & Backfill Log"),
    ]),
    ("2", "Contracts & Legal Documents", "section-2-contracts-legal", [
        ("2.1", "Subcontractor Agreement Template"),
        ("2.2", "Change Order Form"),
        ("2.3", "Lien Waiver Templates"),
        ("2.4", "Payment Draw Schedule"),
        ("2.5", "Warranty Tracking Sheet"),
        ("2.6", "Material Delivery Receipt"),
        ("2.7", "Safety Requirements & Liability"),
        ("2.8", "Dispute Resolution Procedure"),
    ]),
    ("3", "Rough-In Phase", "section-3-rough-in-phase", [
        ("3.1", "Framing Inspection Checklist"),
        ("3.2", "Electrical Rough-In Log"),
        ("3.3", "Plumbing Rough-In Log"),
        ("3.4", "HVAC Rough-In Guide"),
        ("3.5", "Insulation & Air Sealing Guide"),
    ]),
    ("4", "Systems Installation", "section-4-systems-installation", [
        ("4.1", "Electrical System Completion Log"),
        ("4.2", "Plumbing System Completion Log"),
        ("4.3", "HVAC System Completion"),
        ("4.4", "Final Systems Walkthrough"),
    ]),
    ("5", "Finish Work", "section-5-finish-work", [
        ("5.1", "Drywall Completion Checklist"),
        ("5.2", "Interior Door Installation Log"),
        ("5.3", "Trim & Finish Carpentry Log"),
        ("5.4", "Flooring Installation Guide"),
        ("5.5", "Cabinet Installation Checklist"),
        ("5.6", "Paint Color & Finish Tracking"),
    ]),
    ("6", "Daily Operations", "section-6-daily-operations", [
        ("6.1", "Daily Job Site Log"),
        ("6.2", "Weather Delay Log"),
        ("6.3", "Material Delivery & Storage Log"),
        ("6.4", "Tool & Equipment Log"),
        ("6.5", "Safety Incident Report"),
    ]),
    ("7", "Budget & Expenses", "section-7-budget-expenses", [
        ("7.1", "Expense Tracking Sheets"),
        ("7.2", "Receipt Organization System"),
        ("7.3", "Cost Overrun Analysis"),
        ("7.4", "Payment Tracking"),
        ("7.5", "Final Budget Reconciliation"),
    ]),
    ("8", "Quick Reference Guides", "section-8-quick-reference", [
        ("8.1", "Residential Code Quick Reference"),
        ("8.2", "Span Tables"),
        ("8.3", "Material Calculators"),
        ("8.4", "Emergency Contacts"),
        ("8.5", "Common Measurements"),
    ]),
]

PAGE_W, PAGE_H = letter


# ------------------------------------------------------------------ cover

def build_cover():
    path = os.path.join(OUT, "00-BINDER-COVER.pdf")
    c = rl_canvas.Canvas(path, pagesize=letter)
    c.setTitle("Owner-Builder Job Site Binder — Cover")

    # frame
    c.setStrokeColor(d.INK)
    c.setLineWidth(2)
    c.rect(0.55 * inch, 0.55 * inch, PAGE_W - 1.1 * inch, PAGE_H - 1.1 * inch)
    c.setLineWidth(0.75)
    c.rect(0.65 * inch, 0.65 * inch, PAGE_W - 1.3 * inch, PAGE_H - 1.3 * inch)

    cx = PAGE_W / 2

    # title block — vertically centered zone
    c.setFillColor(d.INK)
    c.setFont(d.BOLD, 34)
    c.drawCentredString(cx, 8.55 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 8.0 * inch, "JOB SITE BINDER")
    c.setLineWidth(1.5)
    c.line(2.1 * inch, 7.72 * inch, PAGE_W - 2.1 * inch, 7.72 * inch)
    c.setFont(d.BODY, 13)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 7.38 * inch, "Your Complete Construction Management System")

    # project fields — labels right-aligned to a common gutter, rules aligned
    fields = ["Project Name:", "Project Address:", "Owner-Builder:", "Start Date:"]
    label_x = 3.0 * inch          # right edge of labels
    rule_x0 = 3.15 * inch         # all rules start here
    rule_x1 = PAGE_W - 1.35 * inch
    y = 5.6 * inch
    c.setFillColor(d.INK)
    for label in fields:
        c.setFont(d.BODY, 12.5)
        c.drawRightString(label_x, y, label)
        c.setLineWidth(0.75)
        c.line(rule_x0, y - 2, rule_x1, y - 2)
        y -= 0.62 * inch

    # brand + edition
    c.setFont(d.BOLD, 12)
    c.setFillColor(d.INK)
    c.drawCentredString(cx, 1.55 * inch, "BUILD YOUR HOUSE")
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 1.32 * inch, "build-your-house.com")
    c.drawCentredString(cx, 1.05 * inch, "Second Edition — Revised 2026")

    c.showPage()
    c.save()
    return path


# ------------------------------------------------------------------ spine

def build_spine_h():
    """Horizontal strips version — simpler and fits both sizes on one sheet."""
    path = os.path.join(OUT, "00-BINDER-SPINE-LABEL.pdf")
    W, H = landscape(letter)
    c = rl_canvas.Canvas(path, pagesize=landscape(letter))
    c.setTitle("Owner-Builder Job Site Binder — Spine Labels")

    def strip(y0, strip_w, label):
        x0 = (W - 10.5 * inch) / 2
        w = 10.5 * inch
        # dashed cut outline
        c.setStrokeColor(d.RULE_GREY)
        c.setLineWidth(0.5)
        c.setDash(4, 3)
        c.rect(x0, y0, w, strip_w)
        c.setDash()
        # crop marks
        c.setStrokeColor(d.INK)
        c.setLineWidth(0.5)
        m = 0.16 * inch
        for (x, y, dx, dy) in [(x0, y0, -1, -1), (x0 + w, y0, 1, -1),
                               (x0, y0 + strip_w, -1, 1),
                               (x0 + w, y0 + strip_w, 1, 1)]:
            c.line(x + 2 * dx, y, x + 2 * dx + dx * m, y)
            c.line(x, y + 2 * dy, x, y + 2 * dy + dy * m)
        # text
        big = strip_w > 2.2 * inch
        c.setFillColor(d.INK)
        c.setFont(d.BOLD, 22 if big else 16)
        ty = y0 + strip_w * (0.58 if big else 0.52)
        c.drawCentredString(W / 2, ty, "OWNER-BUILDER JOB SITE BINDER")
        c.setFont(d.BODY, 12 if big else 10)
        py = y0 + strip_w * (0.24 if big else 0.18)
        c.drawString(x0 + 0.9 * inch, py, "Project:")
        c.setLineWidth(0.75)
        pw = c.stringWidth("Project:", d.BODY, 12 if big else 10)
        c.line(x0 + 0.9 * inch + pw + 8, py - 2, x0 + w - 0.9 * inch, py - 2)
        # caption
        c.setFillColor(d.FURNITURE_GREY)
        c.setFont(d.BODY, 8.5)
        c.drawString(x0, y0 - 0.2 * inch,
                     f"{label} — cut along dashed line")
        c.setFillColor(d.INK)

    strip(4.9 * inch, 2.75 * inch, 'Insert for 3-inch binder (2.75" spine)')
    strip(1.2 * inch, 1.8 * inch, 'Insert for 2-inch binder (1.8" spine)')

    c.setFillColor(d.FURNITURE_GREY)
    c.setFont(d.BODY, 9)
    c.drawCentredString(W / 2, H - 0.55 * inch,
                        "BINDER SPINE LABELS — print on cardstock if possible, "
                        "cut out, and slide into the binder's clear spine pocket.")
    c.showPage()
    c.save()
    return path


# ------------------------------------------------------------------ title pages

def build_title_pages():
    paths = []
    for num, name, folder, docs in SECTIONS:
        os.makedirs(os.path.join(OUT, folder), exist_ok=True)
        path = os.path.join(OUT, folder, f"SECTION-{num}-TITLE-PAGE.pdf")
        c = rl_canvas.Canvas(path, pagesize=letter)
        c.setTitle(f"Section {num}: {name}")
        cx = PAGE_W / 2

        c.setStrokeColor(d.INK)
        c.setLineWidth(2)
        c.rect(0.55 * inch, 0.55 * inch, PAGE_W - 1.1 * inch, PAGE_H - 1.1 * inch)

        c.setFillColor(d.INK)
        c.setFont(d.BOLD, 26)
        c.drawCentredString(cx, 7.9 * inch, f"SECTION {num}")
        c.setFont(d.BOLD, 20)
        c.drawCentredString(cx, 7.35 * inch, name.upper())
        c.setLineWidth(1.5)
        c.line(2.2 * inch, 7.05 * inch, PAGE_W - 2.2 * inch, 7.05 * inch)

        c.setFont(d.BOLD, 11)
        c.drawCentredString(cx, 6.35 * inch, "IN THIS SECTION")
        y = 5.95 * inch
        for fid, title in docs:
            c.setFont(d.BOLD, 11)
            c.drawString(2.35 * inch, y, fid)
            c.setFont(d.BODY, 11)
            c.drawString(2.95 * inch, y, title)
            y -= 0.34 * inch

        c.setFont(d.BODY, 9)
        c.setFillColor(d.FURNITURE_GREY)
        c.drawCentredString(cx, 0.85 * inch,
                            "Owner-Builder Job Site Binder · © 2026 Build Your "
                            "House · build-your-house.com")
        c.showPage()
        c.save()
        paths.append(path)
    return paths


# ------------------------------------------------------------------ TOC

def build_toc():
    path = os.path.join(OUT, "00-TABLE-OF-CONTENTS.pdf")
    flow = []
    flow.append(Paragraph("Table of Contents", S["title"]))
    flow.append(Paragraph(
        "Documents are numbered by section — find any form by its number on "
        "the tab dividers and each page's footer.", S["subtitle"]))
    entry = ParagraphStyle("toc-entry", parent=S["body"], fontSize=10.5,
                           leading=15, leftIndent=26, firstLineIndent=-26,
                           spaceAfter=1)
    for num, name, _folder, docs in SECTIONS:
        flow += d.h2(f"SECTION {num}: {name.upper()}", S)
        for fid, title in docs:
            flow.append(Paragraph(
                f"<b>{fid}</b>&nbsp;&nbsp;{title}", entry))
    d.build_doc(path, "", "Table of Contents", "Front Matter", flow)
    return path


# ------------------------------------------------------------------ how to use

def build_howto():
    path = os.path.join(OUT, "00-HOW-TO-USE-THIS-BINDER.pdf")
    B = S["bullet"]
    flow = []
    flow.append(Paragraph("How to Use This Binder", S["title"]))
    flow.append(Paragraph(
        "Your central command center for managing an owner-builder "
        "construction project — every form, checklist, and log you need to "
        "keep professional records from first permit to final inspection.",
        S["subtitle"]))

    flow.append(Paragraph(
        "Keep this binder on-site and accessible at all times. It works "
        "because it is paper: no battery, no signal, nothing to load — and "
        "you can hand any page to a sub or an inspector.", S["body"]))

    flow += d.h2("SETTING UP", S)
    flow.append(Paragraph("What you'll need:", S["body-bold"]))
    for item in [
        "3-ring binder — heavy-duty 2″ or 3″ with D-rings",
        "8 divider tabs, labeled for each section",
        "Clear sheet protectors (about 50) for blank masters and "
        "frequently used references",
        "Three-hole punch, sticky notes, and page flags",
    ]:
        flow.append(Paragraph(f"• {item}", B))
    flow.append(Paragraph(
        "Print everything double-sided at an office-supply store (about "
        "$40–60), punch, and assemble in numbered order: cover, this guide, "
        "table of contents, then Sections 1 through 8 with a tab at each "
        "section title page. Slide the spine label into the binder's spine "
        "pocket.", S["body"]))
    flow.append(Paragraph(
        "Editable versions included: the ZIP also contains Word (.docx) "
        "versions of the contract documents and Excel (.xlsx) versions of the "
        "budget and tracking spreadsheets — customize them with your project "
        "details, then print and punch the results into the binder.",
        S["body"]))

    flow += d.h2("THE EIGHT SECTIONS", S)
    blurbs = [
        ("Section 1 — Project Planning & Foundation",
         "Use during pre-construction and foundation work. Start here: master "
         "timeline and budget first."),
        ("Section 2 — Contracts & Legal Documents",
         "Subcontractor agreements, change orders, lien waivers, and payment "
         "records. Update after every transaction."),
        ("Section 3 — Rough-In Phase",
         "Framing and rough-in checklists for electrical, plumbing, and HVAC "
         "inspections."),
        ("Section 4 — Systems Installation",
         "Final installation and testing of mechanical, electrical, and "
         "plumbing systems before closing walls."),
        ("Section 5 — Finish Work",
         "Drywall, doors, trim, flooring, cabinets, and paint."),
        ("Section 6 — Daily Operations",
         "Daily logs, deliveries, weather delays, and safety incidents — "
         "the section you'll touch every working day."),
        ("Section 7 — Budget & Expenses",
         "Expense tracking, receipts, cost-overrun analysis, and final "
         "reconciliation."),
        ("Section 8 — Quick Reference Guides",
         "Code requirements, span tables, calculators, and emergency "
         "contacts."),
    ]
    for head, text in blurbs:
        flow.append(Paragraph(f"<b>{head}.</b> {text}", S["body"]))

    flow += d.h2("WHEN TO USE EACH FORM", S)
    for when, what in [
        ("Daily", "Daily Job Site Log (6.1); Material Delivery & Storage Log "
                  "(6.3) whenever a delivery arrives."),
        ("Before each phase", "Review that section's checklists so you know "
                              "what's coming."),
        ("Before every inspection", "Complete the matching inspection "
                                    "checklist — walk it with a pen before "
                                    "you call the inspector."),
        ("When hiring subs", "Subcontractor Agreement (2.1); track payments "
                             "with the Payment Draw Schedule (2.4)."),
        ("For every expense", "Log it in the Expense Tracking Sheets (7.1); "
                              "file the receipt (7.2)."),
        ("When anything changes", "Document it immediately with a Change "
                                  "Order Form (2.2)."),
    ]:
        flow.append(Paragraph(f"<b>{when}:</b> {what}", B))

    flow += d.h2("HABITS THAT KEEP YOU ORGANIZED", S)
    for tip in [
        "Set aside 15 minutes at the end of each day to update logs and file "
        "receipts — consistency beats perfection.",
        "Photocopy (or reprint) blank forms before you use the last one; "
        "keep blank masters in sheet protectors.",
        "Take photos to supplement written logs and reference them by date "
        "in the daily log.",
        "Review the master timeline every Sunday and adjust for actual "
        "progress.",
    ]:
        flow.append(Paragraph(f"• {tip}", B))

    d.build_doc(path, "", "How to Use This Binder", "Front Matter", flow)
    return path


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    print(build_cover())
    print(build_spine_h())
    for p in build_title_pages():
        print(p)
    print(build_toc())
    print(build_howto())
