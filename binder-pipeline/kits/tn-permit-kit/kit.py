"""Shared furniture and helpers for the Tennessee Owner-Builder Permit Kit.

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

SECTION = "Tennessee Owner-Builder Permit Kit"
HEADER_LEFT = "TENNESSEE OWNER-BUILDER PERMIT KIT"
VERIFIED = "verified September 2026"

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


# Tennessee cites two ways and both break badly. Statutes carry the section
# symbol ("Tenn. Code Ann. § 68-120-101"), and platypus will happily break the
# line between the § and its number. Rules carry a chapter number with an
# embedded hyphen-dot ("0780-02-23-.07(2)(a)"), which platypus treats as a
# hyphenation opportunity and will split after any of the three hyphens.
# NB is the non-breaking space to put after every § — and after a bare number
# that owns a unit ("50 feet", "200 sq ft"), for the same reason.
NB = "&#160;"


def sec(number):
    """'§ 68-120-101' with the space that can never break."""
    return f"§{NB}{number}"


# A Tennessee rule cite is the widest token in this kit: "0780-02-23-.02(1)(a)"
# measures 95pt at 9pt and "§ 68-120-101(b)(1)(B)(i)" measures 108pt. Platypus
# splits a token longer than its column ANYWHERE, including after a hyphen, and
# a rule number broken across two lines reads as two different rule numbers.
# check.py cannot catch it either: its split-word detector only fires on short
# lowercase alphabetic fragments, and ".07(2)(a)" is neither. The fix is the
# same one the rest of the kit line uses — size the column, never the text. A
# cite column of 1.65in clears every cite printed here.
CITE_COL = 1.65 * inch


def body(text):
    return Paragraph(text, S["body"])


def bullet(text):
    return Paragraph(f"• {text}", S["bullet"])


def h2(text):
    return d.h2(text, S)


def h2_tight(text, reserve=1.5):
    """h2 for a heading immediately followed by a titled_table.

    design.h2 reserves 2.4in so a heading keeps ~2 rows of following content.
    A titled_table carries its own title and header and repeats both when it
    splits, so 1.5in already guarantees the heading plus two write-in rows —
    and the looser threshold was costing a full page of trapped whitespace in
    the checklist-heavy documents.

    `reserve` (inches) is tunable for the few headings whose table has an
    unusually tall first chunk: a reference table with wrapped prose in its
    first data row needs ~2in to avoid stranding the heading alone at the foot
    of a page, while the full 2.4in of design.h2 wastes most of a page.
    """
    from reportlab.platypus import CondPageBreak
    from reportlab.platypus import Paragraph as _P
    return [CondPageBreak(reserve * inch), _P(text, S["h2"]), d.H2Rule()]


def callout(title, paragraphs):
    """design.callout_box that can never split across a page.

    callout_box is a Table, so platypus will happily break it between rows and
    leave the title band stranded at the foot of one page with an open border.
    Every callout in this kit is short enough to keep whole.
    """
    from reportlab.platypus import KeepTogether
    return KeepTogether(d.callout_box(title, paragraphs))


def callout_long(title, paragraphs):
    """A callout that MAY split, repeating its title band on the next page.

    callout() wraps design.callout_box in KeepTogether, which is right for a
    short advisory. Tennessee's statutory quotations run long enough that a
    250pt callout arriving two thirds down a page throws the whole rest of the
    page away — several pages of pure whitespace across the kit. This rebuilds
    the same box as a LongTable that breaks between body paragraphs.

    repeatRows is deliberately 0. A titled_table repeats its header on
    continuation because a repeated column header is a familiar convention; a
    repeated advisory-box TITLE is not — it reads as a duplicated box, and a
    title like "Three things that are still true" appearing twice with two
    items and then one is actively misleading. The continuation therefore
    carries the border alone, and the title row is glued to the first body
    paragraph so a title can never strand at the foot of a page.

    Same border, padding and title stripe as design.callout_box; only the
    split behavior differs.
    """
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.platypus import LongTable, TableStyle

    d.register_fonts()
    w = CW
    title_style = ParagraphStyle(
        "callout-title", fontName=d.BOLD, fontSize=11, leading=14,
        textColor=d.INK)
    rows = [[Paragraph(title, title_style)]]
    rows += [[p] for p in paragraphs]
    t = LongTable(rows, colWidths=[w - 24], repeatRows=0, splitByRow=1)
    t.setStyle(TableStyle([
        ("BOX", (0, 0), (-1, -1), 1.5, d.INK),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 8),
        ("BACKGROUND", (0, 0), (-1, 0), d.SUBTOTAL_FILL),
        ("LINEBELOW", (0, 0), (-1, 0), 0.75, d.INK),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("TOPPADDING", (0, 1), (-1, 1), 8),
        # the title band may never be the last thing on a page
        ("NOSPLIT", (0, 0), (0, 1)),
    ]))
    return t


def disclaimer(extra=None):
    """The short note-style disclaimer every kit document carries."""
    txt = ("This is a process reference, not legal advice. Tennessee adopts one "
           "state residential code and then gives your jurisdiction three "
           "different ways to answer for it: run its own building department, "
           "let the State Fire Marshal enforce the state code through contract "
           "inspectors, or opt out entirely so that no residential building "
           "code is enforced at all. The unit is the <b>jurisdiction</b>, not "
           "the county — a city inside an opted-out county routinely has a "
           "different status from the county around it. What does not depend "
           "on any of that: the state electrical permit, the subsurface "
           "sewage disposal permit, and contractor licensing. Confirm every "
           "item with the office that will actually handle your parcel before "
           "you rely on it.")
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
        title or f"Sources — every Tennessee claim in this document "
                 f"({VERIFIED})",
        hdr, body_rows, [CW - 2.15 * inch, 2.15 * inch], S, write_rows=False)


def closing_note(text=None):
    """The closing source line, wrapped so it cannot orphan a single line.

    A four-line note landing two lines from the foot of a page splits and
    strands its tail on a sheet of its own. KeepTogether moves the whole note
    instead; it is short enough that the cost is never more than a few lines
    of whitespace on the previous page.
    """
    from reportlab.platypus import KeepTogether
    return KeepTogether(Paragraph(text or STATUTE_NOTE, S["note"]))


# Kept deliberately short. This note closes every document in the kit, and a
# longer version needed ~1.6in — more than the tail of a page usually has left,
# so KeepTogether threw it onto a sheet of its own at the end of TN.1. Trimming
# it to four lines reclaimed that page and tightened three others.
STATUTE_NOTE = (
    "<b>The rules are the part you actually need, and they are free.</b> "
    "<b>publications.tnsosfiles.com</b> hosts them as dated PDFs — "
    "<b>0780-02-23</b> residential, <b>0780-02-01</b> electrical, "
    "<b>0400-48-01</b> septic — and the filename carries the effective date, so "
    "you can always tell whether yours is current. Statutes are published under "
    "contract by LexisNexis at <b>lexisnexis.com/hottopics/tncode</b>. "
    "<b>One warning:</b> building and electrical rest on separate authority — "
    "Title 68, Chapter 120 and Title 68, Chapter 102. Conflating them is why so "
    "many guides wrongly imply that opting out of the building code ends your "
    "permit obligations. It does not. Read September 2026.")
