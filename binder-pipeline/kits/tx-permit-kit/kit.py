"""Shared furniture and helpers for the Texas Owner-Builder Permit Kit.

Wraps binder-pipeline/design.py without modifying it. The binder's furniture
hard-codes "OWNER-BUILDER JOB SITE BINDER" in the running header; this module
re-implements only that function so the kit carries its own product line, and
adds a right-hand topic slot so the header orients the reader inside the kit.

Everything else — fonts, styles, drawn checkboxes, drawn rules, titled_table,
callout_box, mirrored duplex margins — comes straight from design.py.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))))

from reportlab.lib.units import inch
from reportlab.platypus import Frame, PageTemplate, Paragraph, Spacer

import design as d

SECTION = "Texas Owner-Builder Permit Kit"
HEADER_LEFT = "TEXAS OWNER-BUILDER PERMIT KIT"
VERIFIED = "verified August 2026"

S = d.make_styles()
CW = d.content_width()


# ---------------------------------------------------------------- furniture

def _draw_furniture(canv, doc, page_num, page_count):
    """design._draw_furniture with the kit's product line on the left and a
    per-document topic on the right. Page 1 of the cover doc is skipped."""
    if getattr(doc, "_kit_skip_first", False) and page_num == 1:
        return
    d.register_fonts()
    even = page_num % 2 == 0
    left = d.MARGIN_INSIDE if not even else d.MARGIN_OUTSIDE
    right = d.MARGIN_OUTSIDE if not even else d.MARGIN_INSIDE
    page_w, page_h = doc.pagesize
    x0, x1 = left, page_w - right

    canv.saveState()
    canv.setFont(d.BODY, 8)
    canv.setFillColor(d.FURNITURE_GREY)
    canv.drawString(x0, page_h - 0.55 * inch, HEADER_LEFT)
    canv.drawRightString(x1, page_h - 0.55 * inch, doc._kit_topic)
    canv.setStrokeColor(d.RULE_GREY)
    canv.setLineWidth(0.5)
    canv.line(x0, page_h - 0.62 * inch, x1, page_h - 0.62 * inch)

    canv.line(x0, 0.62 * inch, x1, 0.62 * inch)
    canv.setFont(d.BODY, 8)
    center_left = (x0 + x1) / 2 - canv.stringWidth(d.COPYRIGHT, d.BODY, 8) / 2
    form = doc._binder_form
    max_w = center_left - x0 - 8
    if canv.stringWidth(form, d.BODY, 8) > max_w:
        while form and canv.stringWidth(form + "…", d.BODY, 8) > max_w:
            form = form[:-1]
        form = form.rstrip() + "…"
    canv.drawString(x0, 0.45 * inch, form)
    canv.drawCentredString((x0 + x1) / 2, 0.45 * inch, d.COPYRIGHT)
    canv.drawRightString(x1, 0.45 * inch, f"Page {page_num} of {page_count}")
    canv.restoreState()


def _canvas_class(doc):
    from reportlab.pdfgen import canvas as _canvas

    class KitCanvas(_canvas.Canvas):
        def __init__(self, *a, **kw):
            super().__init__(*a, **kw)
            self._saved = []

        def showPage(self):
            self._saved.append(dict(self.__dict__))
            self._startPage()

        def save(self):
            count = len(self._saved)
            for i, state in enumerate(self._saved, start=1):
                self.__dict__.update(state)
                _draw_furniture(self, doc, i, count)
                super().showPage()
            super().save()

    return KitCanvas


class KitDoc(d.BinderDoc):
    def __init__(self, filename, form_id, form_title, topic, **kw):
        super().__init__(filename, form_id, form_title, SECTION, **kw)
        self._kit_topic = topic


def build(filename, form_id, form_title, topic, flowables, cover_fn=None):
    """Build one kit document. If cover_fn is given it draws a full-bleed cover
    on page 1 (no running furniture) and the flowables start on page 2."""
    doc = KitDoc(filename, form_id, form_title, topic)
    if cover_fn is not None:
        doc._kit_skip_first = True
        w, h = doc.pagesize
        cover = PageTemplate(
            id="cover",
            frames=[Frame(d.MARGIN_INSIDE, d.MARGIN_BOTTOM,
                          w - d.MARGIN_INSIDE - d.MARGIN_OUTSIDE, 12,
                          leftPadding=0, rightPadding=0,
                          topPadding=0, bottomPadding=0)],
            onPage=lambda canv, _doc: cover_fn(canv))
        doc.addPageTemplates([cover])
        doc._firstPageTemplateIndex = len(doc.pageTemplates) - 1
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    doc.build(flowables, canvasmaker=_canvas_class(doc))
    return filename


# ---------------------------------------------------------------- helpers

def header(form_id, form_title, purpose):
    return d.doc_header(form_id, form_title, S, purpose=purpose)


def cite(text):
    """Source line printed on-page, gen_8_2 style."""
    return Paragraph(text, S["note"])


def body(text):
    return Paragraph(text, S["body"])


def bullet(text):
    return Paragraph(f"• {text}", S["bullet"])


def h2(text):
    return d.h2(text, S)


def h2_tight(text):
    """h2 for a heading immediately followed by a titled_table.

    design.h2 reserves 2.4in so a heading keeps ~2 rows of following content.
    A titled_table carries its own title and header and repeats both when it
    splits, so 1.5in already guarantees the heading plus two write-in rows —
    and the looser threshold was costing a full page of trapped whitespace in
    the checklist-heavy documents.
    """
    from reportlab.platypus import CondPageBreak
    from reportlab.platypus import Paragraph as _P
    return [CondPageBreak(1.5 * inch), _P(text, S["h2"]), d.H2Rule()]


def callout(title, paragraphs):
    """design.callout_box that can never split across a page.

    callout_box is a Table, so platypus will happily break it between rows and
    leave the title band stranded at the foot of one page with an open border.
    Every callout in this kit is short enough to keep whole.
    """
    from reportlab.platypus import KeepTogether
    return KeepTogether(d.callout_box(title, paragraphs))


def disclaimer(extra=None):
    """The short note-style disclaimer every kit document carries."""
    txt = ("This is a process reference, not legal advice. Texas has no "
           "single permit counter: each city administers its own permits and "
           "code editions, county programs vary, and several state agencies "
           "each own one piece of the picture. Confirm every item with the "
           "office that will actually issue it before you rely on it.")
    if extra:
        txt += " " + extra
    return d.callout_box("Before you use this document",
                         [Paragraph(txt, S["body"])])


def checklist(items, width=None, min_h=24.5):
    """Drawn-checkbox list that AUTO-SIZES its rows.

    design.items_checklist fixes every row at 24.5pt, which silently overlaps
    any item that wraps past one line — fine for the binder's short supply
    lists, wrong for the statutory items in this kit. Same visual result,
    height measured from the wrapped paragraph.
    """
    from reportlab.platypus import LongTable, TableStyle
    w = width or CW
    box_w = 0.42 * inch
    text_w = w - box_w - 6
    data, heights = [], []
    for txt in items:
        p = Paragraph(txt, S["cell"])
        h = p.wrap(text_w, 10000)[1]
        data.append([d.Checkbox(), p])
        heights.append(max(min_h, h + 9))
    t = LongTable(data, colWidths=[box_w, w - box_w], rowHeights=heights,
                  splitByRow=1)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


def pack_fields(fields, cell_w, font_size=9.5, min_rule=40):
    """Greedily pack (label, fraction) fields so every drawn rule keeps at
    least min_rule pt of writing room inside a table cell. From gen_1_5."""
    from reportlab.pdfbase import pdfmetrics
    lines, line, used = [], [], 0.0
    needs = {}
    for label, _frac in fields:
        need = pdfmetrics.stringWidth(label, d.BODY, font_size) + 6 + min_rule
        needs[label] = need
        if line and used + need + 18 > cell_w:
            lines.append(line)
            line, used = [], 0.0
        line.append(label)
        used += need + (18 if len(line) > 1 else 0)
    if line:
        lines.append(line)
    out = []
    for labels in lines:
        total = sum(needs[lb] for lb in labels)
        out.append(d.FillInRow([(lb, needs[lb] / total) for lb in labels],
                               font_size=font_size, height=24))
    return out


def task_rows(items, cell_w):
    rows = []
    for it in items:
        if isinstance(it, tuple):
            text, fields = it
            cell = []
            if text:
                cell.append(Paragraph(text, S["cell"]))
            cell.extend(pack_fields(fields, cell_w))
            rows.append(cell)
        else:
            rows.append(Paragraph(it, S["cell"]))
    return rows


def check_table(title, items, notes_header="Notes", date_w=1.0, notes_w=2.0):
    """[box] Task | Date | Notes — the section-1 checklist model."""
    header_cells = ["", Paragraph("Item", S["cell-bold"]),
                    Paragraph("Date", S["cell-bold"]),
                    Paragraph(notes_header, S["cell-bold"])]
    task_w = CW - 0.42 * inch - date_w * inch - notes_w * inch
    rows = [[d.Checkbox(), cell, "", ""]
            for cell in task_rows(items, task_w - 10)]
    col = [0.42 * inch, task_w, date_w * inch, notes_w * inch]
    return [d.titled_table(title, header_cells, rows, col, S), Spacer(1, 8)]


def ref_table(title, header_cells, rows, widths):
    """Reference (non-write-in) table."""
    return d.titled_table(title, header_cells, rows, widths, S,
                          write_rows=False)


def cellp(text, bold=False, center=False):
    if center:
        return Paragraph(text, S["cell-center"])
    return Paragraph(text, S["cell-bold" if bold else "cell"])


def sources_table(rows, title=None):
    """Closing source list: (claim, authority). The authority IS the lookup
    key — see the URL-pattern note each document prints beneath it."""
    hdr = [cellp("What this document states", bold=True),
           cellp("Authority", bold=True)]
    body_rows = [[cellp(a), cellp(b)] for a, b in rows]
    return d.titled_table(
        title or f"Sources — every Texas claim in this document "
                 f"({VERIFIED})",
        hdr, body_rows, [CW - 2.15 * inch, 2.15 * inch], S, write_rows=False)


STATUTE_NOTE = (
    "Read any statute cited above at <b>statutes.capitol.texas.gov</b> — "
    "pick the code (Occupations, Local Government, Health &amp; Safety, "
    "Insurance, Property, Water), then the chapter; the Texas Constitution "
    "is under \"CN.\" All statute text verified August 2026.")
