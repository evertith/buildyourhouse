#!/usr/bin/env python3
"""Build the Lulu print-on-demand artifacts for the coil-bound Job Site Binder.

Produces two files in binder-pipeline/print-edition/out/:

  interior.pdf  every shipping binder PDF merged in reading order, normalised
                to a single 8.5x11 portrait trim size.
  cover.pdf     the one-piece wrap cover (back | front) at the size Lulu's
                /cover-dimensions/ endpoint reports for this pod package.

Two rules drive the interior and both come from the design system:

1. Documents start on a recto. design.BinderDoc mirrors its margins off the
   page number (0.9in binding edge on odd pages, 0.6in on even), so a document
   that starts on a verso has every margin backwards and the coil eats the text.
   A blank page is inserted after any document with an odd page count.

2. Landscape documents are rotated onto the portrait trim. Lulu takes one trim
   size per interior file; 1.1, 6.3 and 6.4 are authored at 792x612. Their
   content is rotated a quarter turn counter-clockwise so the head of the table
   lands on the left edge and the reader turns the book clockwise (the coil
   ends up at the top, not under the book). That also puts the landscape top
   margin -- the widest at 0.9in -- on the recto binding edge.

Two failures shaped the build and verify steps. Lulu rejected the first printed
order (Oct 2026) for both, and the original structural checks passed on it:

* Every font must be embedded. ReportLab references Helvetica without embedding
  it, and paragraph bullets are drawn in it, so both files are re-written through
  Ghostscript's pdfwrite, which embeds a metric-identical URW clone (distill()).
* Every source reader must outlive the merge (see build_interior), and verify()
  now compares every interior page's text with the source page it should be.

Usage:
  python3 build_print_edition.py           # build + verify
  python3 build_print_edition.py --verify  # verify an existing build only
  python3 build_print_edition.py --cover   # rebuild the cover only, verify both
"""

import hashlib
import math
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyPDF2 import PdfReader, PdfWriter, Transformation
from PyPDF2.generic import NameObject, NumberObject
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.utils import simpleSplit
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas as rl_canvas

import design as d

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(REPO, "owner-builder-job-site-binder")
OUT = os.path.join(HERE, "out")

TRIM_W, TRIM_H = 612.0, 792.0          # 8.5 x 11 in, in points
COVER_W, COVER_H = 1242.0, 810.0       # POST /cover-dimensions/, coil, letter
COVER_BLEED = 9.0                      # 0.125in, the difference from 2x trim

# Reading order. The spine label is a cut-out sheet and has no place in a bound
# book; the binder cover doubles as the interior title page.
FRONT_MATTER = [
    "00-BINDER-COVER.pdf",
    "00-HOW-TO-USE-THIS-BINDER.pdf",
    "00-TABLE-OF-CONTENTS.pdf",
]

SECTION_DIRS = [
    "section-1-project-planning",
    "section-2-contracts-legal",
    "section-3-rough-in-phase",
    "section-4-systems-installation",
    "section-5-finish-work",
    "section-6-daily-operations",
    "section-7-budget-expenses",
    "section-8-quick-reference",
]


def reading_order():
    """Absolute paths in the order they are bound: front matter, then each
    section's title page followed by its documents in form-number order."""
    paths = [os.path.join(SRC, f) for f in FRONT_MATTER]
    for i, folder in enumerate(SECTION_DIRS, start=1):
        base = os.path.join(SRC, folder)
        title = os.path.join(base, f"SECTION-{i}-TITLE-PAGE.pdf")
        docs = sorted(
            f for f in os.listdir(base)
            if f.endswith(".pdf") and not f.startswith("SECTION-")
        )
        paths.append(title)
        paths.extend(os.path.join(base, f) for f in docs)
    missing = [p for p in paths if not os.path.exists(p)]
    if missing:
        raise SystemExit("missing source PDFs:\n  " + "\n  ".join(missing))
    return paths


def add_portrait_page(writer, page):
    """Append one source page normalised to the portrait trim size."""
    box = page.mediabox
    w = float(box.width)
    h = float(box.height)
    # Move any non-zero mediabox origin to (0, 0) before doing anything else.
    ox, oy = float(box.left), float(box.bottom)
    if ox or oy:
        page.add_transformation(Transformation().translate(-ox, -oy))

    if abs(w - TRIM_W) < 1 and abs(h - TRIM_H) < 1:
        pass
    elif abs(w - TRIM_H) < 1 and abs(h - TRIM_W) < 1:
        # Landscape: quarter turn counter-clockwise, head to the left edge.
        page.add_transformation(Transformation().rotate(90).translate(h, 0))
    else:
        raise SystemExit(f"unexpected page size {w}x{h}pt — not letter portrait or landscape")

    page.mediabox.lower_left = (0, 0)
    page.mediabox.upper_right = (TRIM_W, TRIM_H)
    page.cropbox = page.mediabox
    for key in ("/BleedBox", "/TrimBox", "/ArtBox"):
        page.pop(NameObject(key), None)
    page[NameObject("/Rotate")] = NumberObject(0)
    writer.add_page(page)


def distill(src, dst):
    """Re-write a PDF through Ghostscript so that every font is embedded.

    Lulu's preflight rejects any unembedded font ("Missing font"). pdfwrite
    substitutes its metric-identical URW clone for Helvetica and embeds it.
    AutoRotatePages=/None is load-bearing: by default pdfwrite re-orients pages
    by their text direction, which would undo the landscape rotation.
    """
    subprocess.run(
        ["gs", "-q", "-dNOPAUSE", "-dBATCH", "-dSAFER", "-sDEVICE=pdfwrite",
         "-dPDFSETTINGS=/prepress", "-dCompatibilityLevel=1.4",
         "-dEmbedAllFonts=true", "-dSubsetFonts=true", "-dAutoRotatePages=/None",
         "-dDownsampleColorImages=false", "-dDownsampleGrayImages=false",
         "-dDownsampleMonoImages=false", f"-sOutputFile={dst}", src],
        check=True,
    )


def build_interior():
    writer = PdfWriter()
    plan = []
    # PyPDF2 3.0.1 remembers which source objects it has already copied under
    # id(reader). Rebinding `reader` lets the previous one be garbage-collected,
    # the next reader can be allocated at the same address, and its pages then
    # resolve to the previous document's already-copied streams and fonts. The
    # Aug 2026 build shipped that way: 95 of 396 pages carried another document's
    # content. Holding every reader until write() keeps the ids unique.
    readers = []
    for path in reading_order():
        reader = PdfReader(path)
        readers.append(reader)
        n = len(reader.pages)
        start = len(writer.pages) + 1
        if start % 2 == 0:
            raise SystemExit(f"{os.path.basename(path)} would start on a verso (page {start})")
        for page in reader.pages:
            add_portrait_page(writer, page)
        padded = n % 2 == 1
        if padded:
            writer.add_blank_page(width=TRIM_W, height=TRIM_H)
        plan.append((os.path.relpath(path, SRC), start, n, padded))

    # A book is printed on sheets: the last leaf needs a back.
    trailing = len(writer.pages) % 2 == 1
    if trailing:
        writer.add_blank_page(width=TRIM_W, height=TRIM_H)

    writer.add_metadata({
        "/Title": "Owner-Builder Job Site Binder — Coil-Bound Edition",
        "/Author": "Build Your House",
        "/Subject": "Owner-builder construction management system, Second Edition",
    })
    os.makedirs(OUT, exist_ok=True)
    merged = os.path.join(OUT, "interior-merged.pdf")
    with open(merged, "wb") as fh:
        writer.write(fh)
    path = os.path.join(OUT, "interior.pdf")
    distill(merged, path)
    os.remove(merged)
    return path, plan, len(writer.pages), trailing


# ------------------------------------------------------------------ cover
#
# The cover wears the website's Blueprint design system (src/styles/globals.css):
# the navy hero with its drafting grid and corner marks, the orange rule under
# it, warm paper, Fraunces headings, Hanken Grotesk copy and JetBrains Mono
# labels. The fonts are static instances of the site's own self-hosted files
# (binder-pipeline/fonts, SIL OFL). The site's translucent hairlines and text
# are pre-mixed against their ground, so every colour here is solid and nothing
# depends on PDF transparency surviving Lulu's normalisation.
#
# The coil runs down the shared edge: the left of the front, the right of the
# back. Text keeps 1in off that edge and 0.75in off the others.

COVER_FONTS = {
    "Fraunces-SemiBold": "Fraunces-SemiBold.ttf",
    "Fraunces-SemiBoldItalic": "Fraunces-SemiBoldItalic.ttf",
    "Fraunces-MediumItalic": "Fraunces-MediumItalic.ttf",
    "HankenGrotesk-Regular": "HankenGrotesk-Regular.ttf",
    "JetBrainsMono-Regular": "JetBrainsMono-Regular.ttf",
    "JetBrainsMono-Medium": "JetBrainsMono-Medium.ttf",
}
DISPLAY, DISPLAY_IT, SUB_IT = "Fraunces-SemiBold", "Fraunces-SemiBoldItalic", "Fraunces-MediumItalic"
BODY, MONO, MONO_MED = "HankenGrotesk-Regular", "JetBrainsMono-Regular", "JetBrainsMono-Medium"

# globals.css tokens
PAPER, PAPER_2 = 0xF2ECDF, 0xE9E0CE
INK, INK_2 = 0x232019, 0x56503F
ORANGE = 0xC75A22
NAVY, NAVY_2 = 0x102C42, 0x0B2032
CREAM = 0xF6F1E4

# The eight sections in binding order, with what each one holds. The form
# counts are read from the source folders (section_form_counts).
SECTION_BLURBS = [
    ("Project Planning & Foundation", "Timeline, budget, permits, site prep, foundation, excavation"),
    ("Contracts & Legal Documents", "Sub agreements, change orders, lien waivers, draws, warranties"),
    ("Rough-In Phase", "Framing, electrical, plumbing and HVAC rough-in, insulation"),
    ("Systems Installation", "Electrical, plumbing and HVAC completion, final walkthrough"),
    ("Finish Work", "Drywall, doors, trim, flooring, cabinets, paint"),
    ("Daily Operations", "Daily log, weather delays, deliveries, tools, safety incidents"),
    ("Budget & Expenses", "Expenses, receipts, cost overruns, payments, final reconciliation"),
    ("Quick Reference", "Code quick reference, span tables, calculators, emergency contacts"),
]


def register_cover_fonts():
    for name, filename in COVER_FONTS.items():
        if name not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont(name, os.path.join(d.FONT_DIR, filename)))


def section_form_counts():
    """Documents per section, excluding the section title page."""
    return [
        sum(1 for f in os.listdir(os.path.join(SRC, folder))
            if f.endswith(".pdf") and not f.startswith("SECTION-"))
        for folder in SECTION_DIRS
    ]


def rgb(value, alpha=1.0, ground=None):
    """A globals.css colour, optionally pre-mixed at `alpha` over `ground`."""
    r, g, b = (value >> 16) & 255, (value >> 8) & 255, value & 255
    if ground is not None:
        gr, gg, gb = (ground >> 16) & 255, (ground >> 8) & 255, ground & 255
        r, g, b = (alpha * r + (1 - alpha) * gr, alpha * g + (1 - alpha) * gg,
                   alpha * b + (1 - alpha) * gb)
    return colors.Color(r / 255, g / 255, b / 255)


def text(c, x, y, s, font, size, color, track=0.0, align="left"):
    """Draw s with CSS-style letter-spacing (`track`, in em). Returns its width."""
    # The site's font files are latin subsets (no arrows, for one). A missing
    # glyph prints as a blank box, so stop the build instead.
    missing = sorted({ch for ch in s if ord(ch) not in pdfmetrics.getFont(font).face.charToGlyph})
    if missing:
        raise SystemExit(f"{font} has no glyph for {missing!r} in {s!r}")
    space = track * size
    width = pdfmetrics.stringWidth(s, font, size) + space * (len(s) - 1)
    if align == "right":
        x -= width
    elif align == "center":
        x -= width / 2
    c.setFillColor(color)
    c.setFont(font, size)
    c.drawString(x, y, s, charSpace=space)
    return width


def hairline(c, x0, y0, x1, y1, color, width=0.6):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(x0, y0, x1, y1)


def blueprint_grid(c, x0, y0, x1, y1, ox, oy, ground):
    """.bp-grid: a fine 1/4in grid with a heavier line every 1-1/4in, clipped to
    the box and squared to (ox, oy), the trim corner."""
    step = 0.25 * inch
    c.saveState()
    clip = c.beginPath()
    clip.rect(x0, y0, x1 - x0, y1 - y0)
    c.clipPath(clip, stroke=0, fill=0)
    for major, alpha, width in ((False, 0.08, 0.4), (True, 0.13, 0.6)):
        c.setStrokeColor(rgb(CREAM, alpha, ground))
        c.setLineWidth(width)
        for k in range(math.floor((x0 - ox) / step), math.ceil((x1 - ox) / step) + 1):
            if (k % 5 == 0) == major:
                c.line(ox + k * step, y0, ox + k * step, y1)
        for k in range(math.floor((y0 - oy) / step), math.ceil((y1 - oy) / step) + 1):
            if (k % 5 == 0) == major:
                c.line(x0, oy + k * step, x1, oy + k * step)
    c.restoreState()


def corner_marks(c, x0, y0, x1, y1, size, color):
    """The L-shaped marks in the corners of the site's navy hero."""
    c.setStrokeColor(color)
    c.setLineWidth(0.75)
    for x, y, dx, dy in ((x0, y1, 1, -1), (x1, y1, -1, -1), (x0, y0, 1, 1), (x1, y0, -1, 1)):
        c.line(x, y, x + dx * size, y)
        c.line(x, y, x, y + dy * size)


def eyebrow(c, x, y, s, color, rule_color, rule_len):
    """.bp-eyebrow with its trailing rule."""
    width = text(c, x, y, s, MONO_MED, 7.5, color, track=0.2)
    hairline(c, x + width + 10, y + 2.6, x + width + 10 + rule_len, y + 2.6, rule_color)


def logo(c, x, top, ink, accent, rule, label):
    """The header lockup: Build Your / House, a rule, OWNER-BUILDER FIELD GUIDE."""
    size = 16
    text(c, x, top - 12.5, "Build Your", DISPLAY, size, ink, track=-0.01)
    text(c, x, top - 28.5, "House", DISPLAY_IT, size, accent, track=-0.01)
    rx = x + pdfmetrics.stringWidth("Build Your", DISPLAY, size) + 11
    hairline(c, rx, top - 1, rx, top - 32, rule)
    for i, line in enumerate(("OWNER-", "BUILDER", "FIELD GUIDE")):
        text(c, rx + 9, top - 8.5 - i * 8.4, line, MONO, 5.6, label, track=0.16)


def dimension_line(c, x0, x1, y, label, color, label_color):
    """A drafting dimension: extension ticks, 45-degree slashes, centred label."""
    width = text(c, (x0 + x1) / 2, y - 2.3, label, MONO, 6.5, label_color, track=0.18,
                 align="center")
    gap = width / 2 + 10
    c.setStrokeColor(color)
    c.setLineWidth(0.6)
    c.line(x0, y, (x0 + x1) / 2 - gap, y)
    c.line((x0 + x1) / 2 + gap, y, x1, y)
    for x in (x0, x1):
        c.line(x, y - 6, x, y + 6)
        c.line(x - 3.5, y - 3.5, x + 3.5, y + 3.5)


def stamp(c, cx, cy, s, color, angle):
    """The site's rotated rubber-stamp tag."""
    c.saveState()
    c.translate(cx, cy)
    c.rotate(angle)
    size = 7.5
    width = pdfmetrics.stringWidth(s, MONO_MED, size) + 0.2 * size * (len(s) - 1)
    c.setStrokeColor(color)
    c.setLineWidth(1)
    c.rect(-width / 2 - 10, -size / 2 - 7, width + 20, size + 14, stroke=1, fill=0)
    text(c, -width / 2, -size * 0.36, s, MONO_MED, size, color, track=0.2)
    c.restoreState()


def cover_front(c, fx, fy, page_count, form_count):
    """Front panel: the navy hero, orange rule, and a paper title block to fill in."""
    X = lambda v: fx + v * inch
    Y = lambda v: fy + v * inch
    right = fx + TRIM_W + COVER_BLEED
    L, R = X(1.0), X(7.75)
    band = Y(2.95)                      # top of the paper zone
    navy_floor = band + 5               # the orange rule is 5pt, as under the hero

    c.setFillColor(rgb(NAVY))
    c.rect(fx, 0, right - fx, COVER_H, stroke=0, fill=1)
    c.setFillColor(rgb(PAPER_2))
    c.rect(fx, 0, right - fx, band, stroke=0, fill=1)
    c.setFillColor(rgb(ORANGE))
    c.rect(fx, band, right - fx, navy_floor - band, stroke=0, fill=1)
    blueprint_grid(c, fx, navy_floor, right, COVER_H, fx, fy, NAVY)
    corner_marks(c, X(0.75), navy_floor + 0.3 * inch, X(8.0), Y(10.5), 0.2 * inch,
                 rgb(CREAM, 0.45, NAVY))

    muted = rgb(CREAM, 0.62, NAVY)
    logo(c, L, Y(10.12), rgb(CREAM), rgb(ORANGE), rgb(CREAM, 0.3, NAVY), muted)
    text(c, R, Y(9.98), "PRINTED EDITION", MONO, 6.5, muted, track=0.16, align="right")
    text(c, R, Y(9.84), f"{page_count} PP · 8.5 × 11 IN", MONO, 6.5, muted, track=0.16,
         align="right")
    hairline(c, L, Y(9.5), R, Y(9.5), rgb(CREAM, 0.22, NAVY))

    eyebrow(c, L, Y(8.3), "SECOND EDITION · REVISED 2026", rgb(ORANGE),
            rgb(ORANGE, 0.55, NAVY), 0.9 * inch)
    size = min(52.0, (R - L) / pdfmetrics.stringWidth("The Owner-Builder", DISPLAY, 1))
    text(c, L, Y(7.55), "The Owner-Builder", DISPLAY, size, rgb(CREAM), track=-0.022)
    text(c, L, Y(7.55) - size * 1.02, "Job Site Binder", DISPLAY_IT, size, rgb(ORANGE),
         track=-0.022)
    text(c, L, Y(7.55) - size * 1.02 - 0.52 * inch,
         "Every contract, checklist, and form for your build.", SUB_IT, 15.5,
         rgb(CREAM, 0.86, NAVY))

    top, bottom = Y(5.75), Y(4.8)
    rule = rgb(CREAM, 0.22, NAVY)
    hairline(c, L, top, R, top, rule)
    hairline(c, L, bottom, R, bottom, rule)
    cells = [("PAGES", str(page_count)), ("SECTIONS", f"{len(SECTION_DIRS):02d}"),
             ("FORMS", str(form_count)), ("REVISED", "2026")]
    width = (R - L) / len(cells)
    for i, (key, value) in enumerate(cells):
        x = L + i * width
        if i:
            hairline(c, x, bottom, x, top, rule)
        pad = 14 if i else 0
        text(c, x + pad, top - 17, key, MONO, 6.5, muted, track=0.16)
        text(c, x + pad, bottom + 13, value, DISPLAY, 25, rgb(CREAM), track=-0.01)

    dimension_line(c, L, R, Y(3.72), "FOR OWNER-BUILDERS RUNNING THEIR OWN JOB SITE",
                   rgb(CREAM, 0.35, NAVY), muted)

    # Title block, as in the corner of a drawing sheet. Paper, so a pen works.
    y0, y1 = Y(0.6), Y(2.55)
    edge = rgb(INK, 0.32, CREAM)
    c.setFillColor(rgb(CREAM))
    c.setStrokeColor(edge)
    c.setLineWidth(0.75)
    c.rect(L, y0, R - L, y1 - y0, stroke=1, fill=1)
    head = y1 - 0.3 * inch
    hairline(c, L, head, R, head, edge, 0.75)
    text(c, L + 9, head + 7.5, "TITLE BLOCK", MONO_MED, 6.5, rgb(ORANGE), track=0.2)
    text(c, R - 9, head + 7.5, "KEEP ON SITE", MONO, 6.5, rgb(INK_2), track=0.16,
         align="right")
    rows = [[("PROJECT", 1.0)], [("SITE ADDRESS", 1.0)],
            [("OWNER-BUILDER", 0.62), ("PHONE", 0.38)],
            [("PERMIT NO.", 0.62), ("START DATE", 0.38)]]
    row_h = (head - y0) / len(rows)
    for r, row in enumerate(rows):
        row_top = head - r * row_h
        if r:
            hairline(c, L, row_top, R, row_top, edge, 0.5)
        x = L
        for j, (label, share) in enumerate(row):
            if j:
                hairline(c, x, row_top - row_h, x, row_top, edge, 0.5)
            text(c, x + 9, row_top - 11.5, label, MONO, 6, rgb(INK_2), track=0.14)
            x += share * (R - L)


def cover_back(c, bx, fy, page_count, form_counts):
    """Back panel: the contents sheet on paper over the site's navy footer."""
    X = lambda v: bx + v * inch
    Y = lambda v: fy + v * inch
    fold = bx + TRIM_W
    L, R = X(0.75), X(7.5)
    band = Y(2.8)                       # top of the navy footer band

    c.setFillColor(rgb(PAPER))
    c.rect(0, 0, fold, COVER_H, stroke=0, fill=1)
    c.setFillColor(rgb(NAVY_2))
    c.rect(0, 0, fold, band, stroke=0, fill=1)
    c.setFillColor(rgb(ORANGE))
    c.rect(0, band, fold, 4, stroke=0, fill=1)
    blueprint_grid(c, 0, 0, fold, band, bx, fy, NAVY_2)

    logo(c, L, Y(10.12), rgb(INK), rgb(ORANGE), rgb(INK, 0.32, PAPER), rgb(INK_2))
    text(c, R, Y(9.98), "SECOND EDITION", MONO, 6.5, rgb(INK_2), track=0.16, align="right")
    text(c, R, Y(9.84), "REVISED 2026", MONO, 6.5, rgb(INK_2), track=0.16, align="right")
    hair = rgb(INK, 0.16, PAPER)
    hairline(c, L, Y(9.5), R, Y(9.5), hair)

    eyebrow(c, L, Y(9.0), "WHAT'S INSIDE", rgb(ORANGE), rgb(ORANGE, 0.5, PAPER), 0.9 * inch)
    text(c, L, Y(8.48), f"Eight sections, {page_count} pages", DISPLAY, 27, rgb(INK),
         track=-0.022)
    text(c, L, Y(8.14), "The contracts, checklists, and logs a build actually generates.",
         SUB_IT, 12.5, rgb(INK_2))
    stamp(c, X(6.62), Y(8.72), "FIELD COPY", rgb(ORANGE), 5)

    top, row_h = Y(7.78), 0.57 * inch
    for i, ((title, blurb), n) in enumerate(zip(SECTION_BLURBS, form_counts), start=1):
        y = top - (i - 1) * row_h
        hairline(c, L, y, R, y, hair)
        text(c, L, y - 0.245 * inch, f"SEC. {i:02d}", MONO_MED, 7, rgb(ORANGE), track=0.12)
        text(c, L + 0.82 * inch, y - 0.255 * inch, title, DISPLAY, 13, rgb(INK), track=-0.01)
        text(c, L + 0.82 * inch, y - 0.43 * inch, blurb, BODY, 8.6, rgb(INK_2))
        text(c, R, y - 0.245 * inch, f"{n:02d} FORMS", MONO, 6.5, rgb(INK_2), track=0.14,
             align="right")
    hairline(c, L, top - len(SECTION_BLURBS) * row_h, R, top - len(SECTION_BLURBS) * row_h, hair)

    # Footer band: why paper, and the spec box from the homepage hero.
    muted = rgb(CREAM, 0.62, NAVY_2)
    eyebrow(c, L, Y(2.3), "WHY PAPER", rgb(ORANGE), rgb(ORANGE, 0.55, NAVY_2), 0.55 * inch)
    text(c, L, Y(1.92), "A job site eats phones.", DISPLAY, 20, rgb(CREAM), track=-0.02)
    copy = ("Printed on both sides and coil-bound, so it lies flat on a tailgate or a "
            "sheet of plywood and stays open at the page you’re working from.")
    for i, line in enumerate(simpleSplit(copy, BODY, 9.2, X(4.35) - L)):
        text(c, L, Y(1.62) - i * 13, line, BODY, 9.2, rgb(CREAM, 0.8, NAVY_2))

    sx0, sx1 = X(4.75), R
    sy1 = Y(2.4)
    rule = rgb(CREAM, 0.2, NAVY_2)
    c.setStrokeColor(rule)
    c.setLineWidth(0.6)
    specs = [("BINDING", "Coil"), ("TRIM", "8.5 × 11 in"), ("PAGES", str(page_count)),
             ("FORMS", str(sum(form_counts)))]
    spec_h = 0.27 * inch
    c.rect(sx0, sy1 - 0.27 * inch - spec_h * len(specs), sx1 - sx0,
           0.27 * inch + spec_h * len(specs), stroke=1, fill=0)
    text(c, sx0 + 9, sy1 - 0.17 * inch, "BINDER SPECS", MONO, 6, muted, track=0.16)
    text(c, sx1 - 9, sy1 - 0.17 * inch, "PRINTED EDITION", MONO, 6, muted, track=0.16,
         align="right")
    for i, (key, value) in enumerate(specs):
        y = sy1 - 0.27 * inch - i * spec_h
        hairline(c, sx0 + 9, y, sx1 - 9, y, rule)
        text(c, sx0 + 9, y - 0.17 * inch, key, MONO, 6, muted, track=0.16)
        text(c, sx1 - 9, y - 0.19 * inch, value, DISPLAY, 11.5,
             rgb(ORANGE) if i == 0 else rgb(CREAM), align="right")

    hairline(c, L, Y(0.9), R, Y(0.9), rule)
    text(c, L, Y(0.66), "BUILD-YOUR-HOUSE.COM", MONO_MED, 6.5, muted, track=0.18)
    text(c, R, Y(0.66), "OWNER-BUILDER JOB SITE BINDER", MONO, 6.5, muted, track=0.18,
         align="right")


def build_cover(page_count):
    register_cover_fonts()
    form_counts = section_form_counts()
    if len(form_counts) != len(SECTION_BLURBS):
        raise SystemExit("SECTION_BLURBS is out of step with SECTION_DIRS")
    raw = os.path.join(OUT, "cover-raw.pdf")
    c = rl_canvas.Canvas(raw, pagesize=(COVER_W, COVER_H))
    c.setTitle("Owner-Builder Job Site Binder — Coil-Bound Cover")

    # The wrap is two trim-width panels butted together: back on the left,
    # front on the right, with bleed on the three outer edges of each.
    fold = COVER_BLEED + TRIM_W          # x of the shared trim edge / cut line
    cover_back(c, COVER_BLEED, COVER_BLEED, page_count, form_counts)
    cover_front(c, fold, COVER_BLEED, page_count, sum(form_counts))

    c.showPage()
    c.save()
    path = os.path.join(OUT, "cover.pdf")
    distill(raw, path)
    os.remove(raw)
    return path


# ------------------------------------------------------------------ verify

def unembedded_fonts(pdf):
    """Names of the fonts pdffonts reports as not embedded. The emb flag is read
    from the right because the type column can be two words ("Type 1")."""
    out = subprocess.run(["pdffonts", pdf], capture_output=True, text=True, check=True).stdout
    rows = [l.split() for l in out.splitlines()[2:] if l.strip()]
    return [r[0] for r in rows if len(r) >= 6 and r[-5] == "no"]


def gs_errors(pdf):
    """Ghostscript's count of errors while drawing every page."""
    r = subprocess.run(["gs", "-q", "-dNOPAUSE", "-dBATCH", "-sDEVICE=nullpage", pdf],
                       capture_output=True, text=True)
    return (r.stdout + r.stderr).count("Error")


def page_words(pdf):
    """Each page's alphanumeric words, sorted, so that the landscape rotation
    (which changes extraction order) still compares equal."""
    text = subprocess.run(["pdftotext", "-enc", "UTF-8", pdf, "-"],
                          capture_output=True, text=True, check=True).stdout
    return [sorted(re.findall(r"[A-Za-z0-9]+", page)) for page in text.split("\f")]


def pages_not_matching_sources(interior):
    """Walk the merge plan and compare every interior page's text with the
    source page it should be, and check that padding pages are empty."""
    got = page_words(interior)
    bad, k = [], 0
    for path in reading_order():
        src = page_words(path)
        n = len(PdfReader(path).pages)
        for j in range(n):
            if k >= len(got) or got[k] != src[j]:
                bad.append(f"p{k + 1} ({os.path.relpath(path, SRC)} p{j + 1})")
            k += 1
        if n % 2:
            if k >= len(got) or got[k]:
                bad.append(f"p{k + 1} (blank pad)")
            k += 1
    return bad, k


def md5sum(path):
    with open(path, "rb") as fh:
        return hashlib.md5(fh.read()).hexdigest()


def verify(interior, cover, expected_pages):
    ok = True

    def check(label, passed, detail=""):
        nonlocal ok
        ok = ok and passed
        print(f"  [{'ok ' if passed else 'FAIL'}] {label}{(' — ' + detail) if detail else ''}")

    print("\nINTERIOR")
    info = subprocess.run(["pdfinfo", interior], capture_output=True, text=True).stdout
    pages = int(next(l for l in info.splitlines() if l.startswith("Pages:")).split()[1])
    check("page count matches the merge plan", pages == expected_pages, f"{pages}")
    check("page count is even (duplex)", pages % 2 == 0, f"{pages}")

    reader = PdfReader(interior)
    sizes = {(round(float(p.mediabox.width), 2), round(float(p.mediabox.height), 2))
             for p in reader.pages}
    rotations = {int(p.get("/Rotate", 0) or 0) for p in reader.pages}
    check("every page is 612x792pt", sizes == {(TRIM_W, TRIM_H)}, str(sorted(sizes)))
    check("no page-level /Rotate", rotations == {0}, str(sorted(rotations)))

    bad = unembedded_fonts(interior)
    check("every font embedded", not bad, "; ".join(sorted(set(bad))) or "all embedded")
    errors = gs_errors(interior)
    check("draws without Ghostscript errors", errors == 0, f"{errors} errors")
    mismatched, walked = pages_not_matching_sources(interior)
    check("every page carries its source page's text", not mismatched,
          (", ".join(mismatched[:5]) + (f" and {len(mismatched) - 5} more" if len(mismatched) > 5 else ""))
          if mismatched else f"{walked} pages")

    print("\nCOVER")
    cinfo = subprocess.run(["pdfinfo", cover], capture_output=True, text=True).stdout
    cpages = int(next(l for l in cinfo.splitlines() if l.startswith("Pages:")).split()[1])
    check("cover is a single wrap page", cpages == 1, f"{cpages}")
    cr = PdfReader(cover)
    cw = round(float(cr.pages[0].mediabox.width), 2)
    ch = round(float(cr.pages[0].mediabox.height), 2)
    check("cover matches Lulu /cover-dimensions/",
          (cw, ch) == (COVER_W, COVER_H), f"{cw}x{ch}pt (want {COVER_W}x{COVER_H})")
    cbad = unembedded_fonts(cover)
    check("cover fonts embedded", not cbad, "; ".join(sorted(set(cbad))) or "all embedded")
    cerrors = gs_errors(cover)
    check("cover draws without Ghostscript errors", cerrors == 0, f"{cerrors} errors")

    return ok


def main():
    verify_only = "--verify" in sys.argv
    cover_only = "--cover" in sys.argv
    if verify_only or cover_only:
        interior = os.path.join(OUT, "interior.pdf")
        expected = len(PdfReader(interior).pages)
        cover = build_cover(expected) if cover_only else os.path.join(OUT, "cover.pdf")
        plan, trailing = [], False
    else:
        interior, plan, expected, trailing = build_interior()
        cover = build_cover(expected)

    if plan:
        print(f"{'start':>6}  {'pp':>3}  pad  document")
        for rel, start, n, padded in plan:
            print(f"{start:>6}  {n:>3}  {'+1 ' if padded else '   '}  {rel}")
        print(f"\ndocuments: {len(plan)}   "
              f"blanks: {sum(1 for *_, p in plan if p) + (1 if trailing else 0)}   "
              f"FINAL PAGE COUNT: {expected}")

    ok = verify(interior, cover, expected)
    print(f"\ninterior: {interior} ({os.path.getsize(interior)/1024/1024:.2f} MB)")
    print(f"cover:    {cover} ({os.path.getsize(cover)/1024:.1f} KB)")
    print(f"\nLulu line item page_count MUST be {expected}")
    print("PRINT_ASSETS md5s for workers/downloads/src/index.js (upload these exact files):")
    print(f"  interior: {md5sum(interior)}")
    print(f"  cover:    {md5sum(cover)}")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
