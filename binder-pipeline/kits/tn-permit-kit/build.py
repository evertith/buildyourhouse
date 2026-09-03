#!/usr/bin/env python3
"""Build every TENNESSEE Permit Kit document, audit the output, and zip the folder.

Usage:
  python3 build.py          # regenerate all PDFs and audit them
  python3 build.py --zip    # also write tn-permit-kit.zip
"""

import os
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out", "tn-permit-kit")
ZIP_PATH = os.path.join(HERE, "tn-permit-kit.zip")
ZIP_ROOT = "tn-permit-kit"

GENERATORS = [
    "gen_tn_0.py",
    "gen_tn_1.py",
    "gen_tn_2.py",
    "gen_tn_3.py",
    "gen_tn_4.py",
    "gen_tn_5.py",
]

EXPECTED = [
    "TN.0-cover-and-how-to-use.pdf",
    "TN.1-owner-builder-exemption.pdf",
    "TN.2-permit-application-checklist.pdf",
    "TN.3-inspection-sequence.pdf",
    "TN.4-where-to-file-directory.pdf",
    "TN.5-forms-and-documents-index.pdf",
]


def main():
    for gen in GENERATORS:
        path = os.path.join(HERE, gen)
        if not os.path.exists(path):
            print(f"MISSING generator {gen}")
            continue
        r = subprocess.run([sys.executable, path], capture_output=True,
                           text=True, cwd=HERE)
        if r.returncode != 0:
            print(f"FAILED {gen}\n{r.stderr}")
            return 1
        print(r.stdout.strip())

    print()
    audit = subprocess.run([sys.executable, os.path.join(HERE, "check.py")],
                           cwd=HERE)
    if audit.returncode != 0:
        print("\nAudit reported problems — not zipping.")
        return 1

    missing = [f for f in EXPECTED if not os.path.exists(os.path.join(OUT, f))]
    if missing:
        print("\nMissing expected PDFs:")
        for m in missing:
            print("  - " + m)
        return 1

    if "--zip" in sys.argv:
        if os.path.exists(ZIP_PATH):
            os.remove(ZIP_PATH)
        with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as z:
            for f in EXPECTED:
                z.write(os.path.join(OUT, f), f"{ZIP_ROOT}/{f}")
        print(f"\nWrote {ZIP_PATH} "
              f"({os.path.getsize(ZIP_PATH) / 1024:.0f} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
