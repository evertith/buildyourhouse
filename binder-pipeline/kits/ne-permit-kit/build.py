#!/usr/bin/env python3
"""Build every NEBRASKA Permit Kit document, audit the output (check.py and
orphan_headings.py), and zip the folder.

Usage:
  python3 build.py          # regenerate all PDFs and audit them
  python3 build.py --zip    # also write ne-permit-kit.zip
"""

import os
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out", "ne-permit-kit")
ZIP_PATH = os.path.join(HERE, "ne-permit-kit.zip")
ZIP_ROOT = "ne-permit-kit"

GENERATORS = [
    "gen_ne_0.py",
    "gen_ne_1.py",
    "gen_ne_2.py",
    "gen_ne_3.py",
    "gen_ne_4.py",
    "gen_ne_5.py",
]

EXPECTED = [
    "NE.0-cover-and-how-to-use.pdf",
    "NE.1-what-binds-you-and-who-can-stop-you.pdf",
    "NE.2-permit-application-checklist.pdf",
    "NE.3-inspection-sequence.pdf",
    "NE.4-where-to-file-directory.pdf",
    "NE.5-forms-and-documents-index.pdf",
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

    print()
    orphans = subprocess.run(
        [sys.executable, os.path.join(HERE, "orphan_headings.py")], cwd=HERE)
    if orphans.returncode != 0:
        print("\nStranded headings reported — not zipping.")
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
