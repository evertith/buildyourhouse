#!/usr/bin/env python3
"""Stranded-heading detector for the FLORIDA Permit Kit PDFs.

check.py catches geometry defects — clipping, overlap, near-blank sheets. It
cannot see the defect that actually looks worst in print: a section heading
that lands as the LAST thing on a page, with the content it introduces
starting on the next sheet. The reader turns the page to find out what
"WHAT THE BUILDING DEPARTMENT KEEPS" means.

design.h2 guards against this with a CondPageBreak reserving 2.4in, and
kit.h2_tight reserves a tunable 1.5in for headings whose following table
carries its own repeated title. Both are heuristics on the FOLLOWING
content's height, and both can be defeated: a heading followed by a tall
KeepTogether, or by a table whose first chunk is taller than the reserve,
will still strand. This measures the built PDF instead of trusting the
reserve.

Method: the kit's type scale separates headings from everything else by size
alone. h2 is 13pt, the document title 19pt; body is 10.5pt, table cells
9.5pt, and every 11pt bold item (titled_table's title row, callout_box's
title band) is structurally protected from splitting away from its content by
repeatRows=2 or by NOSPLIT. So the last text line on a page whose glyph boxes
measure 12pt or taller is a heading with nothing under it.

Usage: python3 orphan_headings.py [--verbose]
"""

import glob
import os
import subprocess
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out", "fl-permit-kit")

PAGE_H = 792.0
HEADER_BAND = 46.0        # running header sits at y≈40; content starts below
FOOTER_BAND = PAGE_H - 52  # footer rule at y≈730 in pdftotext's top-down space
HEADING_PT = 12.0          # h2 is 13pt; body 10.5pt; every 11pt item is pinned
LINE_TOL = 3.0             # words within this many pt of y share a line
NS = "{http://www.w3.org/1999/xhtml}"


def pages(pdf):
    """[[(text, x0, y0, x1, y1)]] per page, via pdftotext -bbox."""
    xml = subprocess.run(["pdftotext", "-bbox", pdf, "-"],
                         capture_output=True, text=True).stdout
    root = ET.fromstring(xml)
    out = []
    for page in root.iter(f"{NS}page"):
        ws = []
        for w in page.iter(f"{NS}word"):
            ws.append((w.text or "", float(w.get("xMin")),
                       float(w.get("yMin")), float(w.get("xMax")),
                       float(w.get("yMax"))))
        out.append(ws)
    return out


def content_words(ws):
    """Drop the running header and the footer — furniture is drawn on every
    page and would otherwise always be the last line."""
    return [w for w in ws if HEADER_BAND < w[2] and w[4] < FOOTER_BAND]


def last_line(ws):
    """The bottom-most line on the page as [(text, ...)], top-down y."""
    if not ws:
        return []
    bottom = max(w[2] for w in ws)
    return sorted([w for w in ws if abs(w[2] - bottom) <= LINE_TOL],
                  key=lambda w: w[1])


def audit(pdf, verbose=False):
    problems = []
    name = os.path.basename(pdf)
    for i, ws in enumerate(pages(pdf), start=1):
        line = last_line(content_words(ws))
        if not line:
            continue
        height = max(w[4] - w[2] for w in line)
        text = " ".join(w[0] for w in line)
        if verbose:
            print(f"    {name} p{i}: last line {height:5.1f}pt  {text[:58]!r}")
        if height >= HEADING_PT:
            problems.append(
                f"{name} p{i}: stranded heading ({height:.1f}pt) {text!r}")
    return problems


def main():
    verbose = "--verbose" in sys.argv
    pdfs = sorted(glob.glob(os.path.join(OUT, "*.pdf")))
    if len(sys.argv) > 1 and sys.argv[-1].endswith(".pdf"):
        pdfs = [sys.argv[-1]]
    if not pdfs:
        print(f"no PDFs in {OUT}")
        return 1
    allp = []
    for pdf in pdfs:
        allp += audit(pdf, verbose)
    if allp:
        print(f"{len(allp)} STRANDED HEADING(S):")
        for p in allp:
            print("  - " + p)
        return 1
    print(f"no stranded headings in {len(pdfs)} document(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
