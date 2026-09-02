#!/usr/bin/env python3
"""Stranded-heading detector for the WISCONSIN Permit Kit PDFs.

check.py catches geometry defects — clipping, overlap, near-blank pages, words
split by a narrow column. It cannot see the defect that most often survives a
clean build and still looks amateur in print: a section heading that lands at
the foot of a page with nothing under it, or with a single line under it,
because the table or callout it introduces jumped to the next sheet.

design.h2 reserves 2.4in against exactly this, and kit.h2_tight relaxes that to
1.5in for headings whose following table carries its own repeated title. Both
are heuristics measured before layout, so both can still be beaten by a table
whose first chunk is taller than the reserve.

The detector works on rendered output instead. It finds heading lines — the
kit's h2 style is the only all-caps run set in bold at ~12.5pt — and measures
how much text sits below the heading's baseline on the same page. A heading
with less than MIN_TAIL points of content beneath it is stranded.

Usage: python3 orphan_headings.py
"""

import glob
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out", "wi-permit-kit")

FOOTER_Y = 792.0 - 0.62 * 72     # running-footer rule; content stops above it
MIN_TAIL = 46.0                  # pt of content that must follow a heading
NS = "{http://www.w3.org/1999/xhtml}"

# A heading is the kit's only line of consecutive all-caps words. Roman
# numerals, single initials and acronyms inside prose ("UDC", "POWTS", "DSPS",
# "NR") would false-positive, so a heading must be at least two words and at
# least 12 characters — no acronym run in this kit's body text is that long
# while also starting its line.
MIN_HEADING_WORDS = 2
MIN_HEADING_CHARS = 12


def lines(pdf):
    """[(page_index, [(y_top, y_bottom, x_min, text), ...])] grouped by line."""
    xml = subprocess.run(["pdftotext", "-bbox", pdf, "-"],
                         capture_output=True, text=True).stdout
    root = ET.fromstring(xml)
    pages = []
    for page in root.iter(f"{NS}page"):
        rows = {}
        for w in page.iter(f"{NS}word"):
            y0 = float(w.get("yMin"))
            key = round(y0 / 3.0)     # 3pt bucket tolerates baseline jitter
            rows.setdefault(key, []).append(
                (float(w.get("xMin")), y0, float(w.get("yMax")), w.text or ""))
        out = []
        for key in sorted(rows):
            ws = sorted(rows[key])
            out.append((
                min(w[1] for w in ws),          # y top (pdftotext y grows down)
                max(w[2] for w in ws),          # y bottom
                min(w[0] for w in ws),          # x min
                " ".join(w[3] for w in ws),
            ))
        pages.append(out)
    return pages


def is_heading(text):
    """The kit's h2 lines are all-caps. Ampersands and digits are allowed."""
    stripped = text.strip()
    if len(stripped) < MIN_HEADING_CHARS:
        return False
    words = stripped.split()
    if len(words) < MIN_HEADING_WORDS:
        return False
    letters = [c for c in stripped if c.isalpha()]
    if not letters:
        return False
    if any(c.islower() for c in letters):
        return False
    # reject anything that is mostly punctuation or digits
    return len(letters) >= len(stripped) * 0.6


def audit(pdf):
    problems = []
    name = os.path.basename(pdf)
    for i, rows in enumerate(lines(pdf), start=1):
        # Page 1 of the cover doc is drawn on the canvas, not laid out: its
        # all-caps brand block ("BUILD YOUR HOUSE") sits deliberately near the
        # foot with only the domain and edition line beneath it.
        if name.startswith("WI.0") and i == 1:
            continue
        # the running header is all-caps too; skip anything in the header band
        body_rows = [r for r in rows if r[0] > 0.75 * 72 and r[1] < FOOTER_Y - 4]
        for j, (y_top, y_bot, _x, text) in enumerate(body_rows):
            if not is_heading(text):
                continue
            below = [r for r in body_rows[j + 1:]]
            tail = (max(r[1] for r in below) - y_bot) if below else 0.0
            if tail < MIN_TAIL:
                problems.append(
                    f"{name} p{i}: stranded heading {text.strip()!r} "
                    f"({tail:.0f}pt of content below it)")
    return problems


def main():
    pdfs = sorted(glob.glob(os.path.join(OUT, "*.pdf")))
    if not pdfs:
        print(f"no PDFs in {OUT}")
        return 1
    allp = []
    for pdf in pdfs:
        allp += audit(pdf)
    if allp:
        print(f"{len(allp)} STRANDED HEADING(S):")
        for p in allp:
            print("  - " + p)
        return 1
    print(f"{len(pdfs)} documents: no stranded headings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
