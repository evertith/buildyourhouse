"""
Shared design system for the Owner-Builder Job Site Binder.

Implements the 2026 redesign spec:
- Embedded DejaVu Sans family (no base-14 dependency; survives any print RIP)
- Mirrored duplex margins: 0.9in binding edge, 0.6in outside edge
- Type scale: title 19/bold, H2 13/bold + rule, H3 11/bold, body 10.5/14
- Drawn checkboxes (16pt / 0.22in square, 1pt stroke) — never font glyphs
- Drawn fill-in rules — never underscore runs
- Table headers: #E6E6E6 fill, black bold text, 1.5pt rule below, repeatRows
- Write-in rows >= 0.40in; ruled free-text boxes at 22pt line pitch
- Running header + "Form N.N | Page X of Y" footer, (c) 2026
"""

import os

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import landscape as _landscape
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    Frame,
    LongTable,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

# ---------------------------------------------------------------- fonts

_HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(_HERE, "fonts")

BODY = "Binder"
BOLD = "Binder-Bold"
ITALIC = "Binder-Italic"
BOLD_ITALIC = "Binder-BoldItalic"

_registered = False


def register_fonts():
    global _registered
    if _registered:
        return
    pdfmetrics.registerFont(TTFont(BODY, os.path.join(FONT_DIR, "DejaVuSans.ttf")))
    pdfmetrics.registerFont(TTFont(BOLD, os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")))
    pdfmetrics.registerFont(TTFont(ITALIC, os.path.join(FONT_DIR, "DejaVuSans-Oblique.ttf")))
    pdfmetrics.registerFont(
        TTFont(BOLD_ITALIC, os.path.join(FONT_DIR, "DejaVuSans-BoldOblique.ttf"))
    )
    pdfmetrics.registerFontFamily(
        BODY, normal=BODY, bold=BOLD, italic=ITALIC, boldItalic=BOLD_ITALIC
    )
    _registered = True


# ---------------------------------------------------------------- palette / metrics

INK = colors.black
FURNITURE_GREY = colors.HexColor(0x595959)  # running header/footer text
RULE_GREY = colors.HexColor(0x8C8C8C)       # table grid lines
FAINT_GREY = colors.HexColor(0xB3B3B3)      # writing rules inside boxes
HEADER_FILL = colors.HexColor(0xE6E6E6)     # table header band
SUBTOTAL_FILL = colors.HexColor(0xF2F2F2)   # subtotal / zebra band

PAGE_W, PAGE_H = letter

MARGIN_INSIDE = 0.9 * inch   # binding edge (3-hole punch)
MARGIN_OUTSIDE = 0.6 * inch
MARGIN_TOP = 0.9 * inch      # below running header
MARGIN_BOTTOM = 0.8 * inch   # above footer

CHECKBOX_PT = 16             # 0.22in drawn square
WRITE_ROW_PT = 29            # 0.40in minimum handwriting row
LINE_PITCH_PT = 22           # ruled line pitch in free-text boxes

COPYRIGHT = "© 2026 Build Your House · build-your-house.com"


# ---------------------------------------------------------------- paragraph styles

def make_styles():
    register_fonts()
    s = {}
    s["title"] = ParagraphStyle(
        "title", fontName=BOLD, fontSize=19, leading=23, textColor=INK,
        spaceAfter=6, alignment=TA_LEFT)
    s["subtitle"] = ParagraphStyle(
        "subtitle", fontName=BODY, fontSize=10.5, leading=14,
        textColor=FURNITURE_GREY, spaceAfter=14)
    s["h2"] = ParagraphStyle(
        "h2", fontName=BOLD, fontSize=13, leading=16, textColor=INK,
        spaceBefore=14, spaceAfter=4, keepWithNext=1)
    s["h3"] = ParagraphStyle(
        "h3", fontName=BOLD, fontSize=11, leading=14, textColor=INK,
        spaceBefore=10, spaceAfter=3, keepWithNext=1)
    s["body"] = ParagraphStyle(
        "body", fontName=BODY, fontSize=10.5, leading=14, textColor=INK,
        spaceAfter=5)
    s["body-bold"] = ParagraphStyle(
        "body-bold", parent=s["body"], fontName=BOLD)
    s["bullet"] = ParagraphStyle(
        "bullet", parent=s["body"], leftIndent=16, bulletIndent=4,
        spaceAfter=3)
    s["cell"] = ParagraphStyle(
        "cell", fontName=BODY, fontSize=9.5, leading=12, textColor=INK)
    s["cell-bold"] = ParagraphStyle(
        "cell-bold", parent=s["cell"], fontName=BOLD)
    s["cell-center"] = ParagraphStyle(
        "cell-center", parent=s["cell"], alignment=TA_CENTER)
    s["note"] = ParagraphStyle(
        "note", fontName=ITALIC, fontSize=9, leading=12,
        textColor=FURNITURE_GREY, spaceBefore=6, spaceAfter=6)
    return s


class H2Rule(Flowable):
    """0.75pt rule drawn under an H2 heading. Emit right after the H2 Paragraph."""

    def __init__(self, width=None):
        super().__init__()
        self._width = width

    def wrap(self, availWidth, availHeight):
        self.width = self._width or availWidth
        self.height = 6
        return self.width, self.height

    def draw(self):
        self.canv.setStrokeColor(INK)
        self.canv.setLineWidth(0.75)
        self.canv.line(0, self.height - 2, self.width, self.height - 2)


def h2(text, styles):
    """Heading 2 with its rule. A CondPageBreak guarantees the heading starts
    with at least ~2 rows of following content rather than orphaning."""
    from reportlab.platypus import CondPageBreak
    return [CondPageBreak(2.4 * inch), Paragraph(text, styles["h2"]), H2Rule()]


def titled_table(title, header_cells, rows, col_widths, styles,
                 write_rows=True, row_heights=None):
    """Table with its section title INSIDE as row 0 (spanned, no grid) and the
    column header as row 1, repeatRows=2. The title can never orphan away from
    its table, and continuation pages repeat both title and header.

    rows: list of row-lists (cell = str, Paragraph, Flowable, or list of
    Flowables). row_heights: optional list per body row; None entries
    auto-size. Default: WRITE_ROW_PT for rows whose non-first cells are all
    empty strings (write-in rows), auto for rows carrying flowable content.
    """
    ncols = len(header_cells)
    title_style = ParagraphStyle(
        "table-title", fontName=BOLD, fontSize=11, leading=14, textColor=INK,
        spaceAfter=0)
    data = [[Paragraph(title, title_style)] + [""] * (ncols - 1)]
    data.append(list(header_cells))
    data.extend(rows)

    if row_heights is None:
        if write_rows:
            # fit the tallest cell but never drop below the handwriting
            # minimum (pure auto-sizing produced ~26pt rows for a bare
            # 16pt Checkbox + padding)
            row_heights = []
            for r in rows:
                tallest = 0.0
                for cell, w in zip(r, col_widths):
                    items = cell if isinstance(cell, list) else [cell]
                    h = 0.0
                    for it in items:
                        if isinstance(it, Flowable):
                            h += it.wrap(w - 10, 10000)[1]
                    tallest = max(tallest, h)
                row_heights.append(max(WRITE_ROW_PT, tallest + 10))
        else:
            row_heights = [None] * len(rows)
    heights = [None, None] + list(row_heights)

    t = LongTable(data, colWidths=col_widths, rowHeights=heights,
                  repeatRows=2, splitByRow=1)
    cmds = [
        ("SPAN", (0, 0), (-1, 0)),
        ("LEFTPADDING", (0, 0), (-1, 0), 0),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 5),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
        ("FONTNAME", (0, 0), (-1, -1), BODY),
        ("FONTSIZE", (0, 0), (-1, -1), 9.5),
        ("TEXTCOLOR", (0, 0), (-1, -1), INK),
        ("VALIGN", (0, 1), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 1), (-1, -1), 5),
        ("RIGHTPADDING", (0, 1), (-1, -1), 5),
        ("TOPPADDING", (0, 1), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 5),
        # header band
        ("BACKGROUND", (0, 1), (-1, 1), HEADER_FILL),
        ("FONTNAME", (0, 1), (-1, 1), BOLD),
        ("LINEBELOW", (0, 1), (-1, 1), 1.5, INK),
        # grid on header+body only, never the title row
        ("GRID", (0, 1), (-1, -1), 0.5, RULE_GREY),
        ("BOX", (0, 1), (-1, -1), 1, INK),
    ]
    t.setStyle(TableStyle(cmds))
    return t


def callout_box(title, body_flowables, width=None, stripe=True):
    """Bordered advisory box: bold title band + content. B&W-safe (no fills
    heavier than SUBTOTAL_FILL)."""
    register_fonts()
    w = width or content_width()
    title_style = ParagraphStyle(
        "callout-title", fontName=BOLD, fontSize=11, leading=14, textColor=INK)
    rows = [[Paragraph(title, title_style)]] if title else []
    for fl in body_flowables:
        rows.append([fl])
    t = Table(rows, colWidths=[w - 24])
    cmds = [
        ("BOX", (0, 0), (-1, -1), 1.5, INK),
        ("LEFTPADDING", (0, 0), (-1, -1), 12),
        ("RIGHTPADDING", (0, 0), (-1, -1), 12),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
        ("BOTTOMPADDING", (0, -1), (-1, -1), 8),
    ]
    if title and stripe:
        cmds += [
            ("BACKGROUND", (0, 0), (-1, 0), SUBTOTAL_FILL),
            ("LINEBELOW", (0, 0), (-1, 0), 0.75, INK),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
            ("TOPPADDING", (0, 1), (-1, 1), 8),
        ]
    t.setStyle(TableStyle(cmds))
    return t


def items_checklist(items, styles, width=None, row_height=None):
    """Single-column checklist: drawn box + item text. For supply lists,
    pre-inspection verifications, etc. No date/notes columns."""
    w = width or content_width()
    data = [[Checkbox(), Paragraph(txt, styles["cell"])] for txt in items]
    heights = [row_height or 24.5] * len(data)
    t = Table(data, colWidths=[0.42 * inch, w - 0.42 * inch],
              rowHeights=heights)
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("LEFTPADDING", (1, 0), (1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 2),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    return t


class checkbox_choice_row(Flowable):
    """'LABEL  [ ] Option A   [ ] Option B  ...' with drawn boxes on one line."""

    def __init__(self, label, options, styles=None, box=13, font_size=10.5):
        super().__init__()
        self.label = label
        self.options = options
        self.box = box
        self.font_size = font_size

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self.height = max(self.box + 8, 22)
        return self.width, self.height

    def draw(self):
        register_fonts()
        c = self.canv
        baseline = 6
        x = 0
        if self.label:
            c.setFont(BOLD, self.font_size)
            c.setFillColor(INK)
            c.drawString(x, baseline, self.label)
            x += c.stringWidth(self.label, BOLD, self.font_size) + 14
        c.setLineWidth(1)
        c.setStrokeColor(INK)
        for opt in self.options:
            c.rect(x, baseline - 3, self.box, self.box)
            x += self.box + 5
            c.setFont(BODY, self.font_size)
            c.drawString(x, baseline, opt)
            x += c.stringWidth(opt, BODY, self.font_size) + 13


def signature_block(parties, width=None):
    """Signature rules for sign-off: [(role_label, with_date), ...]."""
    w = width or content_width()
    flows = []
    for role, with_date in parties:
        if with_date:
            flows.append(FillInRow([(role + ":", 0.66), ("Date:", 0.34)],
                                   height=40))
        else:
            flows.append(FillIn(role + ":", width=w, height=40))
    return flows


# ---------------------------------------------------------------- drawn components

class Checkbox(Flowable):
    """Drawn checkbox — a real vector square, never a font glyph."""

    def __init__(self, size=CHECKBOX_PT):
        super().__init__()
        self.size = size

    def wrap(self, availWidth, availHeight):
        return self.size, self.size

    def draw(self):
        self.canv.setStrokeColor(INK)
        self.canv.setLineWidth(1)
        self.canv.rect(0, 0, self.size, self.size)


class FillIn(Flowable):
    """A label followed by a drawn writing rule: 'Label  ______________'.

    Never wraps; the rule is drawn, so it cannot reflow or orphan.
    width=None stretches the rule to the right margin.
    """

    def __init__(self, label, width=None, label_font=BODY, font_size=10.5,
                 rule_gap=6, height=None):
        super().__init__()
        self.label = label
        self._req_width = width
        self.label_font = label_font
        self.font_size = font_size
        self.rule_gap = rule_gap
        self._height = height or WRITE_ROW_PT

    def wrap(self, availWidth, availHeight):
        self.width = self._req_width or availWidth
        self.height = self._height
        return self.width, self.height

    def draw(self):
        register_fonts()
        c = self.canv
        baseline = 8
        c.setFont(self.label_font, self.font_size)
        c.setFillColor(INK)
        label_w = 0
        if self.label:
            c.drawString(0, baseline, self.label)
            label_w = c.stringWidth(self.label, self.label_font, self.font_size)
            label_w += self.rule_gap
        c.setStrokeColor(INK)
        c.setLineWidth(0.75)
        c.line(label_w, baseline - 2, self.width, baseline - 2)


class FillInRow(Flowable):
    """Several FillIn fields on one shared baseline, widths as fractions."""

    def __init__(self, fields, gap=18, font_size=10.5, height=None):
        # fields: list of (label, fraction_of_row)
        super().__init__()
        self.fields = fields
        self.gap = gap
        self.font_size = font_size
        self._height = height or WRITE_ROW_PT

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self.height = self._height
        return self.width, self.height

    def draw(self):
        register_fonts()
        c = self.canv
        baseline = 8
        usable = self.width - self.gap * (len(self.fields) - 1)
        x = 0
        c.setFont(BODY, self.font_size)
        c.setFillColor(INK)
        c.setStrokeColor(INK)
        c.setLineWidth(0.75)
        for label, frac in self.fields:
            w = usable * frac
            label_w = 0
            if label:
                c.setFont(BODY, self.font_size)
                c.drawString(x, baseline, label)
                label_w = c.stringWidth(label, BODY, self.font_size) + 6
            c.line(x + label_w, baseline - 2, x + w, baseline - 2)
            x += w + self.gap


class WriteBox(Flowable):
    """Free-text writing box with faint ruled lines at LINE_PITCH_PT."""

    def __init__(self, height_in=2.75, ruled=True, label=None):
        super().__init__()
        self._height = height_in * inch
        self.ruled = ruled
        self.label = label

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self.height = self._height
        return self.width, self.height

    def draw(self):
        register_fonts()
        c = self.canv
        top = self.height
        if self.label:
            c.setFont(BOLD, 10.5)
            c.setFillColor(INK)
            c.drawString(0, self.height - 12, self.label)
            top = self.height - 18
        c.setStrokeColor(INK)
        c.setLineWidth(1)
        c.rect(0, 0, self.width, top)
        if self.ruled:
            c.setStrokeColor(FAINT_GREY)
            c.setLineWidth(0.5)
            y = top - LINE_PITCH_PT
            while y > LINE_PITCH_PT * 0.4:
                c.line(6, y, self.width - 6, y)
                y -= LINE_PITCH_PT


# ---------------------------------------------------------------- tables

def std_table_style(header_rows=1, write_rows=False, grid=True):
    cmds = [
        ("FONTNAME", (0, 0), (-1, -1), BODY),
        ("FONTSIZE", (0, 0), (-1, -1), 9.5),
        ("TEXTCOLOR", (0, 0), (-1, -1), INK),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]
    if header_rows:
        last = header_rows - 1
        cmds += [
            ("BACKGROUND", (0, 0), (-1, last), HEADER_FILL),
            ("FONTNAME", (0, 0), (-1, last), BOLD),
            ("LINEBELOW", (0, last), (-1, last), 1.5, INK),
            ("VALIGN", (0, 0), (-1, last), "MIDDLE"),
        ]
    if grid:
        cmds.append(("GRID", (0, 0), (-1, -1), 0.5, RULE_GREY))
        cmds.append(("BOX", (0, 0), (-1, -1), 1, INK))
    if write_rows:
        # callers should also pass rowHeights >= WRITE_ROW_PT for body rows
        cmds.append(("TOPPADDING", (0, 1), (-1, -1), 6))
        cmds.append(("BOTTOMPADDING", (0, 1), (-1, -1), 6))
    return TableStyle(cmds)


def std_table(data, col_widths, header_rows=1, write_rows=False,
              row_heights=None, extra_style=None, grid=True):
    """LongTable that repeats its header and splits at row boundaries."""
    if row_heights is None and write_rows:
        row_heights = [None] * min(header_rows, len(data)) + \
            [WRITE_ROW_PT] * (len(data) - header_rows)
    t = LongTable(data, colWidths=col_widths, rowHeights=row_heights,
                  repeatRows=header_rows, splitByRow=1)
    style = std_table_style(header_rows=header_rows, write_rows=write_rows,
                            grid=grid)
    t.setStyle(style)
    if extra_style:
        t.setStyle(TableStyle(extra_style))
    return t


def checklist_table(rows, styles, col_widths=None, task_header="Task",
                    notes_header="Notes / Measurements"):
    """The section-1 checklist model: [box] Task | Date | Notes. Kept as-is
    per design review, with drawn boxes and >=0.40in rows."""
    header = ["", Paragraph(task_header, styles["cell-bold"]),
              Paragraph("Date", styles["cell-bold"]),
              Paragraph(notes_header, styles["cell-bold"])]
    data = [header]
    for task in rows:
        data.append([Checkbox(), Paragraph(task, styles["cell"]), "", ""])
    if col_widths is None:
        content_w = PAGE_W - MARGIN_INSIDE - MARGIN_OUTSIDE
        col_widths = [0.42 * inch, content_w - 0.42 * inch - 1.0 * inch - 2.1 * inch,
                      1.0 * inch, 2.1 * inch]
    return std_table(data, col_widths, header_rows=1, write_rows=True)


# ---------------------------------------------------------------- page furniture

class _BinderCanvasMixin:
    """Two-pass canvas: draws running header/footer with Page X of Y."""


def _draw_furniture(canv, doc, page_num, page_count):
    register_fonts()
    even = page_num % 2 == 0
    # mirrored margins: binding edge is left on odd (recto), right on even (verso)
    left = MARGIN_INSIDE if not even else MARGIN_OUTSIDE
    right = MARGIN_OUTSIDE if not even else MARGIN_INSIDE
    page_w = doc.pagesize[0]
    page_h = doc.pagesize[1]
    x0, x1 = left, page_w - right

    canv.saveState()
    # header
    canv.setFont(BODY, 8)
    canv.setFillColor(FURNITURE_GREY)
    canv.drawString(x0, page_h - 0.55 * inch, "OWNER-BUILDER JOB SITE BINDER")
    canv.drawRightString(x1, page_h - 0.55 * inch, doc._binder_section)
    canv.setStrokeColor(RULE_GREY)
    canv.setLineWidth(0.5)
    canv.line(x0, page_h - 0.62 * inch, x1, page_h - 0.62 * inch)
    # footer — truncate the form title so it can never overprint the
    # centered copyright (long titles collided at 8pt)
    canv.line(x0, 0.62 * inch, x1, 0.62 * inch)
    canv.setFont(BODY, 8)
    center_left = (x0 + x1) / 2 - \
        canv.stringWidth(COPYRIGHT, BODY, 8) / 2
    form = doc._binder_form
    max_w = center_left - x0 - 8
    if canv.stringWidth(form, BODY, 8) > max_w:
        while form and canv.stringWidth(form + "…", BODY, 8) > max_w:
            form = form[:-1]
        form = form.rstrip() + "…"
    canv.drawString(x0, 0.45 * inch, form)
    canv.drawCentredString((x0 + x1) / 2, 0.45 * inch, COPYRIGHT)
    canv.drawRightString(x1, 0.45 * inch, f"Page {page_num} of {page_count}")
    canv.restoreState()


def make_canvas_class(doc):
    from reportlab.pdfgen import canvas as _canvas

    class BinderCanvas(_canvas.Canvas):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
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

    return BinderCanvas


class BinderDoc(BaseDocTemplate):
    """Duplex-mirrored document with running furniture.

    build_doc() is the normal entry point.
    """

    def __init__(self, filename, form_id, form_title, section_title,
                 landscape=False, **kw):
        register_fonts()
        pagesize = _landscape(letter) if landscape else letter
        super().__init__(
            filename, pagesize=pagesize,
            leftMargin=MARGIN_INSIDE, rightMargin=MARGIN_OUTSIDE,
            topMargin=MARGIN_TOP, bottomMargin=MARGIN_BOTTOM,
            title=f"{form_id} {form_title}",
            author="Build Your House", **kw)
        self._binder_form = f"{form_id} {form_title}" if form_id else form_title
        self._binder_section = section_title
        w, h = pagesize
        odd = PageTemplate(
            id="odd",
            frames=[Frame(MARGIN_INSIDE, MARGIN_BOTTOM,
                          w - MARGIN_INSIDE - MARGIN_OUTSIDE,
                          h - MARGIN_TOP - MARGIN_BOTTOM,
                          leftPadding=0, rightPadding=0,
                          topPadding=0, bottomPadding=0)])
        even = PageTemplate(
            id="even",
            frames=[Frame(MARGIN_OUTSIDE, MARGIN_BOTTOM,
                          w - MARGIN_INSIDE - MARGIN_OUTSIDE,
                          h - MARGIN_TOP - MARGIN_BOTTOM,
                          leftPadding=0, rightPadding=0,
                          topPadding=0, bottomPadding=0)])
        self.addPageTemplates([odd, even])

    def afterPage(self):
        # next page's template: odd pages (1,3,..) use index 0
        self._nextPageTemplateIndex = self.page % 2


def content_width(landscape=False):
    w = (_landscape(letter) if landscape else letter)[0]
    return w - MARGIN_INSIDE - MARGIN_OUTSIDE


def build_doc(filename, form_id, form_title, section_title, flowables,
              landscape=False):
    doc = BinderDoc(filename, form_id, form_title, section_title,
                    landscape=landscape)
    doc.build(flowables, canvasmaker=make_canvas_class(doc))
    return filename


def doc_header(form_id, form_title, styles, purpose=None):
    """Standard first-page header block: title + optional purpose line."""
    out = [Paragraph(f"{form_id}&nbsp;&nbsp;{form_title}".strip(), styles["title"])]
    if purpose:
        out.append(Paragraph(purpose, styles["subtitle"]))
    else:
        out.append(Spacer(1, 10))
    return out
