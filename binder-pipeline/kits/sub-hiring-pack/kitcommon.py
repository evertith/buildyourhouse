#!/usr/bin/env python3
"""Shared setup for the Subcontractor Hiring Pack kit.

The pack ships as a standalone product, so its running header names the pack
rather than the binder. design.py is shared with the binder build and must not
be modified, so the furniture painter is reimplemented here and swapped in at
import time — everything else (styles, metrics, drawn components) comes
straight from the design system.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_PIPELINE = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, _PIPELINE)

from reportlab.lib.styles import ParagraphStyle          # noqa: E402
from reportlab.lib.units import inch                     # noqa: E402
from reportlab.platypus import Flowable, Paragraph       # noqa: E402

import design as d                                       # noqa: E402

SECTION = "Subcontractor Hiring Pack"
BRAND_HEADER = "BUILD YOUR HOUSE"

DISCLAIMER = ("Template for general reference — have your attorney review before "
              "use. Not legal advice.")

STATE_NOTE = ("Licensing thresholds, deposit limits, workers'-compensation "
              "exemptions and lien deadlines are set by state law and vary "
              "widely. Verify every rule below with your own state's licensing "
              "board, insurance carrier and county recorder before you rely on "
              "it.")

OUT_ROOT = os.path.join(_HERE, "out", "subcontractor-hiring-pack")

S = d.make_styles()
CW = d.content_width()

BULLET = ParagraphStyle("kit-bullet", parent=S["bullet"], bulletFontName=d.BODY,
                        bulletFontSize=10.5)
STEP = ParagraphStyle("kit-step", parent=S["body"], leftIndent=22,
                      firstLineIndent=-22, spaceAfter=4)


# ---------------------------------------------------------------- furniture

def _draw_furniture(canv, doc, page_num, page_count):
    """Same geometry as design._draw_furniture; the left header names the
    product the customer bought instead of the binder."""
    d.register_fonts()
    even = page_num % 2 == 0
    left = d.MARGIN_INSIDE if not even else d.MARGIN_OUTSIDE
    right = d.MARGIN_OUTSIDE if not even else d.MARGIN_INSIDE
    page_w, page_h = doc.pagesize
    x0, x1 = left, page_w - right

    canv.saveState()
    canv.setFont(d.BODY, 8)
    canv.setFillColor(d.FURNITURE_GREY)
    canv.drawString(x0, page_h - 0.55 * inch, BRAND_HEADER)
    canv.drawRightString(x1, page_h - 0.55 * inch, doc._binder_section)
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


d._draw_furniture = _draw_furniture


# ---------------------------------------------------------------- components

class FieldLine(Flowable):
    """One ruled entry line: optional drawn checkbox, label, a drawn rule to the
    right margin, and optional tail text after the rule. Lifted from the 2.1
    contract idiom so the pack's new forms match the contracts it ships with."""

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


class RatingScale(Flowable):
    """A 1–5 scoring scale: drawn boxes with the numeral printed above each.
    Boxes are vector rectangles, never font glyphs, so they survive any RIP."""

    def __init__(self, n=5, box=13, gap=8, font_size=7.5, height=30,
                 align="center"):
        super().__init__()
        self.n = n
        self.box = box
        self.gap = gap
        self.font_size = font_size
        self._height = height
        self.align = align

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self.height = self._height
        return self.width, self.height

    def draw(self):
        d.register_fonts()
        c = self.canv
        total = self.n * self.box + (self.n - 1) * self.gap
        x = (self.width - total) / 2 if self.align == "center" else 0
        c.setStrokeColor(d.INK)
        c.setFillColor(d.INK)
        for i in range(1, self.n + 1):
            c.setFont(d.BODY, self.font_size)
            c.drawCentredString(x + self.box / 2, self.box + 6, str(i))
            c.setLineWidth(1)
            c.rect(x, 2, self.box, self.box)
            x += self.box + self.gap


class WriteLines(Flowable):
    """A run of drawn writing rules with no box — answer space under a call
    script question. Lighter than a WriteBox when the question is the frame.

    bottom_gap keeps the last rule clear of whatever follows, so the answer
    space never reads as belonging to the next question.
    """

    def __init__(self, lines=2, pitch=None, indent=0, bottom_gap=11):
        super().__init__()
        self.lines = lines
        self.pitch = pitch or d.LINE_PITCH_PT
        self.indent = indent
        self.bottom_gap = bottom_gap

    def wrap(self, availWidth, availHeight):
        self.width = availWidth
        self.height = self.lines * self.pitch + self.bottom_gap
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setStrokeColor(d.INK)
        c.setLineWidth(0.75)
        y = self.bottom_gap + (self.lines - 1) * self.pitch
        for _ in range(self.lines):
            c.line(self.indent, y, self.width, y)
            y -= self.pitch


def bullets(items, style=None, bullet="•"):
    return [Paragraph(t, style or BULLET, bulletText=bullet) for t in items]


def numbered(items, style=None):
    return [Paragraph(t, style or BULLET, bulletText=f"{i}.")
            for i, t in enumerate(items, 1)]


def question(text, lines=2, options=None, style=None):
    """A call-script question and its answer space, kept on one page so a
    heading never strands its rules (or its checkboxes) on the next."""
    from reportlab.platypus import KeepTogether
    block = [Paragraph(text, style or S["body-bold"])]
    if options:
        block.append(d.checkbox_choice_row("", options, S))
    block.append(WriteLines(lines))
    return [KeepTogether(block)]


def build(filename, form_id, form_title, flowables):
    out = os.path.join(OUT_ROOT, filename)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, form_id, form_title, SECTION, flowables)
    return out
