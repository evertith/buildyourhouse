#!/usr/bin/env python3
"""SH.0 Cover + Contents — Subcontractor Hiring Pack.

Two pages in one file: a canvas-drawn cover in the binder cover idiom, then a
contents page laid out through a standard design-system Frame so it carries the
same furniture as every other page in the pack.
"""

import os
import re
import subprocess

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas as rl_canvas
from reportlab.platypus import Frame, Paragraph, Spacer

import kitcommon as k
import design as d

S = k.S
CW = k.CW
PAGE_W, PAGE_H = letter

FORM_ID = "SH.0"
FORM_TITLE = "Cover & Contents"

# (form id, title, filename stem, has editable Word version)
NEW_DOCS = [
    ("SH.1", "Subcontractor Interview Scorecard",
     "SH.1-subcontractor-interview-scorecard", False),
    ("SH.2", "Reference Check Form", "SH.2-reference-check-form", False),
    ("SH.3", "Hiring Walkthrough", "SH.3-hiring-walkthrough", False),
]
CONTRACTS = [
    ("2.1", "Subcontractor Agreement Template",
     "2.1-subcontractor-agreement-template", True),
    ("2.2", "Change Order Form", "2.2-change-order-form", True),
    ("2.3", "Lien Waiver Templates", "2.3-lien-waiver-templates", True),
    ("2.4", "Payment Draw Schedule", "2.4-payment-draw-schedule", True),
]


def page_count(path):
    out = subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout
    m = re.search(r"Pages:\s+(\d+)", out)
    return int(m.group(1)) if m else 0


def counts():
    """Page counts read from the built PDFs, so the contents page can never
    drift from what actually ships."""
    rows = []
    for fid, title, stem, word in NEW_DOCS:
        rows.append((fid, title, page_count(os.path.join(k.OUT_ROOT, stem + ".pdf")),
                     word))
    for fid, title, stem, word in CONTRACTS:
        rows.append((fid, title,
                     page_count(os.path.join(k.OUT_ROOT, "contracts", stem + ".pdf")),
                     word))
    return rows


# ---------------------------------------------------------------- cover

def draw_cover(c):
    c.setStrokeColor(d.INK)
    c.setLineWidth(2)
    c.rect(0.55 * inch, 0.55 * inch, PAGE_W - 1.1 * inch, PAGE_H - 1.1 * inch)
    c.setLineWidth(0.75)
    c.rect(0.65 * inch, 0.65 * inch, PAGE_W - 1.3 * inch, PAGE_H - 1.3 * inch)

    cx = PAGE_W / 2

    c.setFillColor(d.INK)
    c.setFont(d.BOLD, 34)
    c.drawCentredString(cx, 8.55 * inch, "SUBCONTRACTOR")
    c.drawCentredString(cx, 8.0 * inch, "HIRING PACK")
    c.setLineWidth(1.5)
    c.line(2.1 * inch, 7.72 * inch, PAGE_W - 2.1 * inch, 7.72 * inch)
    c.setFont(d.BODY, 13)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 7.38 * inch,
                        "Vet, Compare and Hire Trades Without Getting Burned")

    fields = ["Project Name:", "Project Address:", "Owner-Builder:", "Start Date:"]
    label_x = 3.0 * inch
    rule_x0 = 3.15 * inch
    rule_x1 = PAGE_W - 1.35 * inch
    y = 5.6 * inch
    c.setFillColor(d.INK)
    for label in fields:
        c.setFont(d.BODY, 12.5)
        c.drawRightString(label_x, y, label)
        c.setLineWidth(0.75)
        c.line(rule_x0, y - 2, rule_x1, y - 2)
        y -= 0.62 * inch

    c.setFont(d.BODY, 10.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.55 * inch,
                        "Interview scorecard · Reference check form · Hiring "
                        "walkthrough")
    c.drawCentredString(cx, 2.28 * inch,
                        "Subcontractor agreement · Change order · Lien waivers "
                        "· Draw schedule")

    c.setFont(d.BOLD, 12)
    c.setFillColor(d.INK)
    c.drawCentredString(cx, 1.55 * inch, "BUILD YOUR HOUSE")
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 1.32 * inch, "build-your-house.com")
    c.drawCentredString(cx, 1.05 * inch, "2026 Edition")


# ---------------------------------------------------------------- contents

def contents_flowables():
    rows = counts()
    flow = [Paragraph("What's in This Pack", S["title"]),
            Paragraph("Seven documents: three built for hiring subs, and the "
                      "four contract templates you need once you have picked "
                      "one.", S["subtitle"])]

    data = [[Paragraph("Form", S["cell-bold"]),
             Paragraph("Document", S["cell-bold"]),
             Paragraph("Pages", S["cell-bold"]),
             Paragraph("Editable Word version", S["cell-bold"])]]
    for fid, title, pages, word in rows:
        data.append([Paragraph(f"<b>{fid}</b>", S["cell"]),
                     Paragraph(title, S["cell"]),
                     Paragraph(str(pages), S["cell-center"]),
                     Paragraph("Yes — editable-word/" if word else "—",
                               S["cell"])])
    flow.append(d.std_table(
        data, [0.7 * inch, 3.05 * inch, 0.65 * inch, CW - 4.4 * inch],
        header_rows=1, row_heights=[None] + [22] * (len(data) - 1)))
    flow.append(Paragraph(
        "Forms 2.1 to 2.4 sit in the <b>contracts/</b> folder and are the same "
        "documents that ship in Section 2 of the Owner-Builder Job Site "
        "Binder. Their Word versions are in <b>editable-word/</b>.", S["note"]))

    flow += d.h2("HOW TO USE IT", S)
    flow += k.bullets([
        "Read <b>SH.3 Hiring Walkthrough</b> first. It is the order everything "
        "else happens in, and it takes five minutes.",
        "Print one <b>SH.1</b> and three <b>SH.2</b> sheets for every candidate "
        "you take seriously — one scorecard per sub, one reference sheet per "
        "reference call.",
        "Fill in the Word versions of the contracts with your project details, "
        "print them, and sign before anyone starts work.",
        "Keep the completed sheets. If a job goes sideways later, the paper you "
        "filled in before you hired is the record that protects you.",
    ])

    flow.append(Spacer(1, 6))
    flow.append(d.callout_box("Before you rely on anything in here", [
        Paragraph("These documents are general templates for reference, not "
                  "legal advice — have your attorney review any contract "
                  "before you use it. Licensing requirements, deposit limits, "
                  "workers'-compensation exemptions and lien deadlines are set "
                  "by state law and vary widely. Verify your own state's rules "
                  "with its licensing board and your county recorder.",
                  S["body"]),
    ]))

    flow.append(Spacer(1, 10))
    flow.append(Paragraph(
        "This pack is the hiring half of the <b>Owner-Builder Job Site "
        "Binder</b> — the full binder carries 40+ forms across permits, "
        "foundation, rough-in, inspections, daily logs and budget. "
        "build-your-house.com", S["note"]))
    return flow


class _DocShim:
    """Minimal stand-in for a BinderDoc so the kit furniture painter can run
    against a bare canvas."""
    pagesize = letter
    _binder_section = k.SECTION
    _binder_form = f"{FORM_ID} {FORM_TITLE}"


def build():
    d.register_fonts()
    out = os.path.join(k.OUT_ROOT, "SH.0-cover-and-contents.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    c = rl_canvas.Canvas(out, pagesize=letter)
    c.setTitle("Subcontractor Hiring Pack — Cover & Contents")
    c.setAuthor("Build Your House")

    draw_cover(c)
    c.showPage()

    # page 2 is a verso: binding edge on the right, per the mirrored margins
    frame = Frame(d.MARGIN_OUTSIDE, d.MARGIN_BOTTOM,
                  PAGE_W - d.MARGIN_INSIDE - d.MARGIN_OUTSIDE,
                  PAGE_H - d.MARGIN_TOP - d.MARGIN_BOTTOM,
                  leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    # addFromList drops what will not fit without complaining, so check
    pending = contents_flowables()
    frame.addFromList(pending, c)
    if pending:
        raise SystemExit(f"contents page overflowed: {len(pending)} flowables "
                         "did not fit")
    k._draw_furniture(c, _DocShim(), 2, 2)
    c.showPage()
    c.save()
    return out


if __name__ == "__main__":
    print(build())
