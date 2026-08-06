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

Usage:
  python3 build_print_edition.py           # build + verify
  python3 build_print_edition.py --verify  # verify an existing build only
"""

import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PyPDF2 import PdfReader, PdfWriter, Transformation
from PyPDF2.generic import NameObject, NumberObject
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas as rl_canvas

import design as d

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
SRC = os.path.join(REPO, "owner-builder-job-site-binder")
OUT = os.path.join(HERE, "out")

TRIM_W, TRIM_H = 612.0, 792.0          # 8.5 x 11 in, in points
COVER_W, COVER_H = 1242.0, 810.0       # POST /cover-dimensions/, coil, letter
COVER_BLEED = 9.0                      # 0.125in, the difference from 2x trim
COVER_SAFE = 36.0                      # keep cover text 0.5in off every trim edge

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


def build_interior():
    writer = PdfWriter()
    plan = []
    for path in reading_order():
        reader = PdfReader(path)
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
    path = os.path.join(OUT, "interior.pdf")
    with open(path, "wb") as fh:
        writer.write(fh)
    return path, plan, len(writer.pages), trailing


# ------------------------------------------------------------------ cover

NAVY = d.colors.HexColor(0x102C42)      # --navy, src/styles/globals.css
CREAM = d.colors.HexColor(0xF6F1E4)     # --cream

BACK_SUMMARY = [
    "1  Project Planning & Foundation",
    "2  Contracts & Legal Documents",
    "3  Rough-In Phase",
    "4  Systems Installation",
    "5  Finish Work",
    "6  Daily Operations",
    "7  Budget & Expenses",
    "8  Quick Reference",
]


def build_cover(page_count):
    d.register_fonts()
    path = os.path.join(OUT, "cover.pdf")
    c = rl_canvas.Canvas(path, pagesize=(COVER_W, COVER_H))
    c.setTitle("Owner-Builder Job Site Binder — Coil-Bound Cover")

    # The wrap is two trim-width panels butted together: back on the left,
    # front on the right, with bleed on the three outer edges of each.
    fold = COVER_BLEED + TRIM_W          # x of the shared trim edge / cut line
    fy = COVER_BLEED                     # y of the bottom trim edge

    # ---- back panel: navy, bled off the left, top and bottom.
    c.setFillColor(NAVY)
    c.rect(0, 0, fold, COVER_H, stroke=0, fill=1)

    bx = COVER_BLEED                     # left trim edge of the back panel
    bcx = bx + TRIM_W / 2                # back panel centre
    c.setFillColor(CREAM)
    c.setFont(d.BOLD, 22)
    c.drawCentredString(bcx, fy + TRIM_H - 1.5 * inch, "BUILD YOUR HOUSE")
    c.setStrokeColor(CREAM)
    c.setLineWidth(1)
    c.line(bcx - 1.6 * inch, fy + TRIM_H - 1.75 * inch,
           bcx + 1.6 * inch, fy + TRIM_H - 1.75 * inch)

    c.setFont(d.BODY, 11.5)
    c.drawCentredString(bcx, fy + TRIM_H - 2.15 * inch,
                        "Your Complete Construction Management System")

    c.setFont(d.BOLD, 13)
    c.drawString(bx + 1.15 * inch, fy + TRIM_H - 3.1 * inch, "WHAT'S INSIDE")
    y = fy + TRIM_H - 3.55 * inch
    c.setFont(d.BODY, 11.5)
    for line in BACK_SUMMARY:
        c.drawString(bx + 1.15 * inch, y, line)
        y -= 0.34 * inch

    y -= 0.25 * inch
    c.setStrokeColor(CREAM)
    c.setLineWidth(0.6)
    c.line(bx + 1.15 * inch, y, bx + TRIM_W - 1.15 * inch, y)
    y -= 0.42 * inch
    c.setFont(d.BODY, 11)
    for line in [
        "57 forms, checklists, contracts and trackers",
        "for owner-builders running their own job site.",
        "Printed double-sided and coil-bound to lie flat.",
    ]:
        c.drawString(bx + 1.15 * inch, y, line)
        y -= 0.28 * inch

    c.setFont(d.BOLD, 12)
    c.drawCentredString(bcx, fy + 0.95 * inch, "build-your-house.com")
    c.setFont(d.BODY, 9.5)
    c.drawCentredString(bcx, fy + 0.68 * inch, "Second Edition — Revised 2026")

    # ---- front panel: the digital cover design, bled right, top and bottom.
    c.setFillColor(CREAM)
    c.rect(fold, 0, COVER_W - fold, COVER_H, stroke=0, fill=1)

    fx = fold                            # left trim edge of the front panel
    cx = fx + TRIM_W / 2

    c.setStrokeColor(d.INK)
    c.setLineWidth(2)
    c.rect(fx + 0.55 * inch, fy + 0.55 * inch, TRIM_W - 1.1 * inch, TRIM_H - 1.1 * inch)
    c.setLineWidth(0.75)
    c.rect(fx + 0.65 * inch, fy + 0.65 * inch, TRIM_W - 1.3 * inch, TRIM_H - 1.3 * inch)

    c.setFillColor(d.INK)
    c.setFont(d.BOLD, 34)
    c.drawCentredString(cx, fy + 8.55 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, fy + 8.0 * inch, "JOB SITE BINDER")
    c.setLineWidth(1.5)
    c.line(fx + 2.1 * inch, fy + 7.72 * inch, fx + TRIM_W - 2.1 * inch, fy + 7.72 * inch)
    c.setFont(d.BODY, 13)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, fy + 7.38 * inch, "Your Complete Construction Management System")

    fields = ["Project Name:", "Project Address:", "Owner-Builder:", "Start Date:"]
    label_x = fx + 3.0 * inch
    rule_x0 = fx + 3.15 * inch
    rule_x1 = fx + TRIM_W - 1.35 * inch
    y = fy + 5.6 * inch
    c.setFillColor(d.INK)
    for label in fields:
        c.setFont(d.BODY, 12.5)
        c.drawRightString(label_x, y, label)
        c.setLineWidth(0.75)
        c.line(rule_x0, y - 2, rule_x1, y - 2)
        y -= 0.62 * inch

    c.setFont(d.BOLD, 12)
    c.setFillColor(d.INK)
    c.drawCentredString(cx, fy + 1.72 * inch, "BUILD YOUR HOUSE")
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, fy + 1.49 * inch, "build-your-house.com")
    c.drawCentredString(cx, fy + 1.22 * inch, "Second Edition — Revised 2026")
    c.setFont(d.BOLD, 10)
    c.setFillColor(d.INK)
    c.drawCentredString(cx, fy + 0.95 * inch,
                        f"Coil-Bound Edition · {page_count} pages")

    c.showPage()
    c.save()
    return path


# ------------------------------------------------------------------ verify

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

    fonts = subprocess.run(["pdffonts", interior], capture_output=True, text=True).stdout
    rows = [l.split() for l in fonts.splitlines()[2:] if l.strip()]
    not_embedded = [r for r in rows if len(r) > 3 and r[3] == "no" and "Helvetica" not in r[0]]
    check("all glyph-painting fonts embedded", not not_embedded,
          "; ".join(r[0] for r in not_embedded) or f"{len(rows)} font records")
    helv = [r[0] for r in rows if "Helvetica" in r[0]]
    if helv:
        print(f"         note: unused base-14 reference present ({', '.join(helv)}) — paints no glyphs")

    print("\nCOVER")
    cinfo = subprocess.run(["pdfinfo", cover], capture_output=True, text=True).stdout
    cpages = int(next(l for l in cinfo.splitlines() if l.startswith("Pages:")).split()[1])
    check("cover is a single wrap page", cpages == 1, f"{cpages}")
    cr = PdfReader(cover)
    cw = round(float(cr.pages[0].mediabox.width), 2)
    ch = round(float(cr.pages[0].mediabox.height), 2)
    check("cover matches Lulu /cover-dimensions/",
          (cw, ch) == (COVER_W, COVER_H), f"{cw}x{ch}pt (want {COVER_W}x{COVER_H})")
    cfonts = subprocess.run(["pdffonts", cover], capture_output=True, text=True).stdout
    crows = [l.split() for l in cfonts.splitlines()[2:] if l.strip()]
    cbad = [r for r in crows if len(r) > 3 and r[3] == "no"]
    check("cover fonts embedded", not cbad, "; ".join(r[0] for r in cbad) or f"{len(crows)} fonts")

    return ok


def main():
    verify_only = "--verify" in sys.argv
    if verify_only:
        interior = os.path.join(OUT, "interior.pdf")
        expected = len(PdfReader(interior).pages)
        cover = os.path.join(OUT, "cover.pdf")
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
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
