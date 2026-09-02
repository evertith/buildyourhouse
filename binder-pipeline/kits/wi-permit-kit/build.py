#!/usr/bin/env python3
"""Build every WISCONSIN Permit Kit document, audit the output, and zip the folder.

Usage:
  python3 build.py          # regenerate all PDFs and audit them
  python3 build.py --zip    # also write wi-permit-kit.zip
"""

import os
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out", "wi-permit-kit")
ZIP_PATH = os.path.join(HERE, "wi-permit-kit.zip")
ZIP_ROOT = "wi-permit-kit"

GENERATORS = [
    "gen_wi_0.py",
    "gen_wi_1.py",
    "gen_wi_2.py",
    "gen_wi_3.py",
    "gen_wi_4.py",
    "gen_wi_5.py",
]

EXPECTED = [
    "WI.0-cover-and-how-to-use.pdf",
    "WI.1-owner-builder-exemption.pdf",
    "WI.2-permit-application-checklist.pdf",
    "WI.3-inspection-sequence.pdf",
    "WI.4-where-to-file-directory.pdf",
    "WI.5-forms-and-documents-index.pdf",
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
