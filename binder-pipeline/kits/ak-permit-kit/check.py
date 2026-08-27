#!/usr/bin/env python3
"""Output audit for the ALASKA Permit Kit PDFs.

Catches the four defects that survive a clean build but ruin a printed page:
  - near-blank pages (an orphaned tail line on its own sheet)
  - text outside the frame (clipping at the margins)
  - overlapping words (fixed-height table rows swallowing wrapped text)
  - words broken mid-token by a too-narrow table column ("commerce.alaska.g /
    ov", "Phot / os"). This kit found two of these by eye; the detector looks
    for a very short lowercase fragment starting a line, which is what the
    tail of a broken word always looks like and what ordinary prose never
    does.

Usage: python3 check.py
"""

import glob
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out", "ak-permit-kit")

PAGE_W, PAGE_H = 612.0, 792.0
MARGIN_OUTSIDE = 0.6 * 72
MARGIN_INSIDE = 0.9 * 72
TOL = 4.0                 # pt of slack before we call it clipping
MIN_WORDS = 25            # below this a page reads as blank
NS = {"h": "http://www.w3.org/1999/xhtml"}

# Real two-letter words that legitimately begin a line. Anything else that
# short, lowercase, and line-initial is the tail of a word a narrow column
# split in half.
SHORT_OK = {
    "a", "i", "an", "as", "at", "be", "by", "do", "go", "he", "if", "in",
    "is", "it", "me", "my", "no", "of", "on", "or", "so", "to", "up", "us",
    "we",
}


def words(pdf):
    """[(page_index, text, x0, y0, x1, y1)] via pdftotext -bbox."""
    xml = subprocess.run(["pdftotext", "-bbox", pdf, "-"],
                         capture_output=True, text=True).stdout
    root = ET.fromstring(xml)
    pages = []
    for page in root.iter("{http://www.w3.org/1999/xhtml}page"):
        ws = []
        for w in page.iter("{http://www.w3.org/1999/xhtml}word"):
            ws.append((w.text or "", float(w.get("xMin")), float(w.get("yMin")),
                       float(w.get("xMax")), float(w.get("yMax"))))
        pages.append(ws)
    return pages


def overlaps(a, b):
    """Fraction of the smaller box covered by the intersection."""
    ax0, ay0, ax1, ay1 = a
    bx0, by0, bx1, by1 = b
    ix = min(ax1, bx1) - max(ax0, bx0)
    iy = min(ay1, by1) - max(ay0, by0)
    if ix <= 0 or iy <= 0:
        return 0.0
    inter = ix * iy
    smaller = min((ax1 - ax0) * (ay1 - ay0), (bx1 - bx0) * (by1 - by0))
    return inter / smaller if smaller else 0.0


def audit(pdf):
    problems = []
    name = os.path.basename(pdf)
    pages = words(pdf)
    for i, ws in enumerate(pages, start=1):
        # page 1 of the cover doc is intentionally sparse
        is_cover = name.startswith("AK.0") and i == 1
        if len(ws) < MIN_WORDS and not is_cover:
            problems.append(f"{name} p{i}: near-blank ({len(ws)} words)")

        even = i % 2 == 0
        left = MARGIN_OUTSIDE if even else MARGIN_INSIDE
        right = PAGE_W - (MARGIN_INSIDE if even else MARGIN_OUTSIDE)
        for text, x0, y0, x1, y1 in ws:
            if x0 < left - TOL or x1 > right + TOL:
                problems.append(
                    f"{name} p{i}: outside frame x=[{x0:.0f},{x1:.0f}] "
                    f"frame=[{left:.0f},{right:.0f}] {text!r}")
                break

        # line-initial short lowercase fragments: a split word's tail
        rows_by_y = {}
        for text, x0, y0, x1, y1 in ws:
            rows_by_y.setdefault(round(y0), []).append((x0, text))
        for y, row in sorted(rows_by_y.items()):
            row.sort()
            first = row[0][1] or ""
            bare = first.strip(".,;:()\u201c\u201d\"'")
            if (len(bare) <= 2 and bare.isalpha() and bare.islower()
                    and bare not in SHORT_OK):
                problems.append(
                    f"{name} p{i}: split word? line starts {first!r}")

        boxes = [(w[1], w[2], w[3], w[4], w[0]) for w in ws]
        boxes.sort(key=lambda b: (b[1], b[0]))
        hits = 0
        for a in range(len(boxes)):
            for b in range(a + 1, min(a + 40, len(boxes))):
                if boxes[b][1] - boxes[a][1] > 14:
                    break
                if overlaps(boxes[a][:4], boxes[b][:4]) > 0.45:
                    hits += 1
                    if hits <= 2:
                        problems.append(
                            f"{name} p{i}: overlapping text "
                            f"{boxes[a][4]!r} / {boxes[b][4]!r}")
        if hits > 2:
            problems.append(f"{name} p{i}: ...{hits - 2} more overlaps")
    return len(pages), problems


def main():
    pdfs = sorted(glob.glob(os.path.join(OUT, "*.pdf")))
    if not pdfs:
        print(f"no PDFs in {OUT}")
        return 1
    total, allp = 0, []
    for pdf in pdfs:
        n, problems = audit(pdf)
        total += n
        allp += problems
        print(f"{n:3d} pages  {os.path.basename(pdf)}")
    print(f"\n{len(pdfs)} documents, {total} pages total")
    if allp:
        print(f"\n{len(allp)} PROBLEM(S):")
        for p in allp:
            print("  - " + p)
        return 1
    print("\nno geometry problems found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
