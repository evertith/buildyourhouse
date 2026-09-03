#!/usr/bin/env python3
"""Stranded-heading detector for the SOUTH CAROLINA Permit Kit PDFs.

check.py catches geometry defects — blank pages, clipping, overlap, split
words. It cannot see the one layout defect that survives all four and still
looks broken in print: a section heading that lands as the LAST line on a
page, with the content it introduces starting on the next sheet.

design.h2 already emits a CondPageBreak reserving 2.4in, and kit.h2_tight
reserves a tunable 1.5in, so a stranded heading means the reserve was too
small for what actually followed. The fix is always in the generator (raise
the reserve, or move the heading), never here.

The kit's h2 headings are set in ALL CAPS; its running header and footer are
drawn on the canvas outside the content band. So: take the last text line
inside the content band on each page, and flag it if it reads as a heading.

Usage:
  python3 orphan_headings.py            # audit out/sc-permit-kit/*.pdf
  python3 orphan_headings.py <dir|pdf>  # audit somewhere else
"""

import glob
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out", "sc-permit-kit")

# Content band, in pdftotext's top-down coordinates on a 792pt page. The
# running header baseline sits 0.55in from the top and the footer 0.45in from
# the bottom; both are canvas-drawn furniture and must not count as content.
BAND_TOP = 52.0
BAND_BOTTOM = 742.0
LINE_TOL = 3.0            # pt of vertical slack when grouping words to a line


def lines_by_page(pdf):
    """[[ (y, text) ]] — text lines inside the content band, per page."""
    xml = subprocess.run(["pdftotext", "-bbox", pdf, "-"],
                         capture_output=True, text=True).stdout
    root = ET.fromstring(xml)
    pages = []
    for page in root.iter("{http://www.w3.org/1999/xhtml}page"):
        words = []
        for w in page.iter("{http://www.w3.org/1999/xhtml}word"):
            y0, y1 = float(w.get("yMin")), float(w.get("yMax"))
            if y0 < BAND_TOP or y1 > BAND_BOTTOM:
                continue
            words.append((float(w.get("xMin")), y0, w.text or ""))
        rows = []
        for x, y, text in sorted(words, key=lambda t: (t[1], t[0])):
            if rows and abs(y - rows[-1][0]) <= LINE_TOL:
                rows[-1][1].append((x, text))
            else:
                rows.append((y, [(x, text)]))
        pages.append([(y, " ".join(t for _x, t in sorted(ws)))
                      for y, ws in rows])
    return pages


def is_heading(text):
    """An ALL-CAPS run of words with no sentence punctuation.

    The kit sets every h2 in caps ("WHERE TO FILE", "WHAT APPLIES EVERYWHERE").
    Ordinary prose never ends a page that way; an acronym-only line such as
    "ADH" or a table cell reading "NEC 2020" would, so a heading has to carry
    at least two words or twelve characters before we believe it.
    """
    t = text.strip().rstrip("·-—")
    if not t or t != t.upper():
        return False
    if not re.search(r"[A-Z]{2}", t):
        return False
    if re.search(r"[.;:?!]$", t):
        return False
    letters = re.sub(r"[^A-Z]", "", t)
    if len(letters) < 4:
        return False
    return len(t.split()) >= 2 or len(t) >= 12


def audit(pdf):
    problems = []
    name = os.path.basename(pdf)
    pages = lines_by_page(pdf)
    for i, rows in enumerate(pages, start=1):
        if not rows or i == len(pages):
            continue
        last = rows[-1][1]
        if is_heading(last):
            problems.append(f"{name} p{i}: heading stranded at page foot "
                            f"{last!r}")
        # A heading with a single orphaned line under it reads nearly as badly
        # as a bare one; flag it separately so the generator can raise the
        # reserve rather than nudge it.
        elif len(rows) >= 2 and is_heading(rows[-2][1]):
            problems.append(f"{name} p{i}: heading {rows[-2][1]!r} keeps only "
                            f"one line ({last[:48]!r})")
    return len(pages), problems


def main():
    target = sys.argv[1] if len(sys.argv) > 1 else OUT
    if os.path.isdir(target):
        pdfs = sorted(glob.glob(os.path.join(target, "*.pdf")))
    else:
        pdfs = [target]
    if not pdfs:
        print(f"no PDFs in {target}")
        return 1
    allp = []
    for pdf in pdfs:
        n, problems = audit(pdf)
        allp += problems
        print(f"{n:3d} pages  {os.path.basename(pdf)}")
    if allp:
        print(f"\n{len(allp)} STRANDED HEADING(S):")
        for p in allp:
            print("  - " + p)
        return 1
    print("\nno stranded headings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
