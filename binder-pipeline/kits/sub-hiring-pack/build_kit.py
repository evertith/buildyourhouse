#!/usr/bin/env python3
"""Assemble the Subcontractor Hiring Pack.

  python3 build_kit.py         # build the new PDFs, stage the reused files
  python3 build_kit.py --zip   # ...and write sub-hiring-pack.zip

The four contract PDFs and their Word versions are copied verbatim from the
shipping binder — never regenerated here, so the pack and the binder can never
disagree about what 2.1 says.
"""

import os
import re
import shutil
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
BINDER = os.path.join(REPO, "owner-builder-job-site-binder")
OUT = os.path.join(HERE, "out", "subcontractor-hiring-pack")
ZIP_PATH = os.path.join(HERE, "sub-hiring-pack.zip")
ZIP_ROOT = "subcontractor-hiring-pack"

NEW_PDFS = [
    ("gen_sh_1.py", "SH.1-subcontractor-interview-scorecard.pdf"),
    ("gen_sh_2.py", "SH.2-reference-check-form.pdf"),
    ("gen_sh_3.py", "SH.3-hiring-walkthrough.pdf"),
]
COVER = ("gen_sh_0.py", "SH.0-cover-and-contents.pdf")

CONTRACT_STEMS = [
    "2.1-subcontractor-agreement-template",
    "2.2-change-order-form",
    "2.3-lien-waiver-templates",
    "2.4-payment-draw-schedule",
]


def page_count(path):
    out = subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout
    m = re.search(r"Pages:\s+(\d+)", out)
    return int(m.group(1)) if m else 0


def run(script):
    subprocess.run([sys.executable, os.path.join(HERE, script)], check=True,
                   cwd=HERE, stdout=subprocess.DEVNULL)


def stage_reused():
    src_pdf = os.path.join(BINDER, "section-2-contracts-legal")
    src_doc = os.path.join(BINDER, "editable-documents", "word")
    dst_pdf = os.path.join(OUT, "contracts")
    dst_doc = os.path.join(OUT, "editable-word")
    os.makedirs(dst_pdf, exist_ok=True)
    os.makedirs(dst_doc, exist_ok=True)
    missing = []
    for stem in CONTRACT_STEMS:
        for src, dst, ext in ((src_pdf, dst_pdf, ".pdf"),
                              (src_doc, dst_doc, ".docx")):
            s = os.path.join(src, stem + ext)
            if not os.path.exists(s):
                missing.append(s)
                continue
            shutil.copy2(s, os.path.join(dst, stem + ext))
    return missing


def inventory():
    rows = []
    for rel in sorted(os.listdir(OUT)):
        p = os.path.join(OUT, rel)
        if os.path.isfile(p):
            rows.append((rel, page_count(p), os.path.getsize(p)))
    for folder in ("contracts", "editable-word"):
        for rel in sorted(os.listdir(os.path.join(OUT, folder))):
            p = os.path.join(OUT, folder, rel)
            n = page_count(p) if rel.endswith(".pdf") else 0
            rows.append((f"{folder}/{rel}", n, os.path.getsize(p)))
    return rows


def main():
    os.makedirs(OUT, exist_ok=True)
    for script, _pdf in NEW_PDFS:
        run(script)
    missing = stage_reused()
    if missing:
        print("MISSING source files:")
        for m in missing:
            print(f"  - {m}")
        sys.exit(1)
    # cover last: its contents table reads page counts off the built PDFs
    run(COVER[0])

    rows = inventory()
    total_pages = sum(n for _r, n, _s in rows)
    print(f"{'pages':>6}  {'bytes':>9}  file")
    for rel, n, size in rows:
        print(f"{n if n else '-':>6}  {size:>9,}  {rel}")
    print(f"\n{len(rows)} files · {total_pages} PDF pages")

    if "--zip" in sys.argv:
        if os.path.exists(ZIP_PATH):
            os.remove(ZIP_PATH)
        with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as z:
            for rel, _n, _s in rows:
                z.write(os.path.join(OUT, rel), f"{ZIP_ROOT}/{rel}")
        print(f"\nWrote {ZIP_PATH} ({os.path.getsize(ZIP_PATH)/1024/1024:.2f} MB)")


if __name__ == "__main__":
    main()
