#!/usr/bin/env python3
"""Stranded-heading detector for the permit-kit PDFs.

check.py catches geometry (clipping, overlap, near-blank pages, mid-token
column splits). It cannot see the one defect a reader notices first: a heading
that sits at the foot of a page with nothing — or almost nothing — under it,
so the section it names begins on the next sheet. design.h2 guards against
this with a 2.4in CondPageBreak and kit.h2_tight with a tunable reserve, but a
heading emitted directly (or one whose following flowable is a table that
splits at its first row) still strands.

The detector reads pdftohtml -xml, which reports a font size and a bold flag
per text block. design.make_styles renders at 1.5x in that coordinate space:
19pt title -> 29, 13pt h2 -> 20, 11pt h3 / callout title / table title -> 17,
10.5pt body -> 16, 9.5pt cell -> 14. Anything bold at 17 or above that is the
last real block on its page, or is followed by less than MIN_FOLLOW lines, is
reported.

Usage:
  python3 orphan_headings.py                 # audits ./out/<kit-dir>/*.pdf
  python3 orphan_headings.py path/to/*.pdf   # or explicit files
"""

import glob
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))

HEADING_MIN_SIZE = 17     # 11pt and up, in pdftohtml's 1.5x space
H2_SIZE = 19              # 13pt h2 and larger: the headings that matter most
MIN_FOLLOW = 2            # body lines a heading needs under it on its own page
FOOTER_TOP = 1090         # running footer lives below this
HEADER_BOTTOM = 90        # running header lives above this


def blocks(pdf):
    """[[(top, left, text, size, bold)] per page] via pdftohtml -xml."""
    xml = subprocess.run(
        ["pdftohtml", "-xml", "-i", "-stdout", pdf],
        capture_output=True, text=True).stdout
    # poppler emits raw ampersands in some URLs; ET will not parse those
    xml = re.sub(r"&(?!(amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)", "&amp;",
                 xml)
    root = ET.fromstring(xml)
    pages = []
    for page in root.iter("page"):
        sizes = {f.get("id"): int(f.get("size"))
                 for f in page.iter("fontspec")}
        out = []
        for t in page.iter("text"):
            raw = "".join(t.itertext()).strip()
            if not raw:
                continue
            bold = t.find("b") is not None
            out.append((int(t.get("top")), int(t.get("left")), raw,
                        sizes.get(t.get("font"), 0), bold))
        out.sort()
        pages.append(out)
    return pages


def audit(pdf):
    problems = []
    name = os.path.basename(pdf)
    for i, page in enumerate(blocks(pdf), start=1):
        body = [b for b in page
                if HEADER_BOTTOM < b[0] < FOOTER_TOP]
        for j, (top, left, text, size, bold) in enumerate(body):
            if not bold or size < HEADING_MIN_SIZE:
                continue
            after = body[j + 1:]
            # a following block at the same size and left edge is the heading's
            # own second line, not content under it
            follow = [b for b in after
                      if not (b[4] and b[3] == size and abs(b[1] - left) < 4)]
            if len(follow) >= MIN_FOLLOW:
                continue
            kind = "H2" if size >= H2_SIZE else "heading"
            tail = ("nothing follows" if not follow
                    else f"only {len(follow)} line(s) follow")
            problems.append(
                f"{name} p{i}: stranded {kind} at y={top} — {tail}: "
                f"{text[:62]!r}")
    return problems


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if args:
        pdfs = sorted(args)
    else:
        pdfs = sorted(glob.glob(os.path.join(HERE, "out", "*", "*.pdf")))
    if not pdfs:
        print("no PDFs found")
        return 1
    allp = []
    for pdf in pdfs:
        problems = audit(pdf)
        allp += problems
        print(f"{len(problems):3d} stranded  {os.path.basename(pdf)}")
    if allp:
        print(f"\n{len(allp)} STRANDED HEADING(S):")
        for p in allp:
            print("  - " + p)
        return 1
    print("\nno stranded headings found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
