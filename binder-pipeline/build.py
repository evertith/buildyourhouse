#!/usr/bin/env python3
"""Assemble and verify the Owner-Builder Job Site Binder zip.

Usage:
  python3 build.py            # verify out/ inventory, report page counts
  python3 build.py --zip      # also build owner-builder-job-site-binder.zip
"""

import os
import re
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
ZIP_PATH = os.path.join(HERE, "owner-builder-job-site-binder.zip")
ZIP_ROOT = "owner-builder-job-site-binder"

SECTIONS = {
    "section-1-project-planning": [
        "1.1-master-project-timeline.pdf",
        "1.2-budget-tracking-spreadsheet.pdf",
        "1.3-permit-application-checklist.pdf",
        "1.4-site-preparation-checklist.pdf",
        "1.5-foundation-checklist.pdf",
        "1.6-foundation-inspection-form.pdf",
        "1.7-excavation-backfill-log.pdf",
        "SECTION-1-TITLE-PAGE.pdf",
    ],
    "section-2-contracts-legal": [
        "2.1-subcontractor-agreement-template.pdf",
        "2.2-change-order-form.pdf",
        "2.3-lien-waiver-templates.pdf",
        "2.4-payment-draw-schedule.pdf",
        "2.5-warranty-tracking-sheet.pdf",
        "2.6-material-delivery-receipt.pdf",
        "2.7-safety-requirements-liability.pdf",
        "2.8-dispute-resolution-procedure.pdf",
        "SECTION-2-TITLE-PAGE.pdf",
    ],
    "section-3-rough-in-phase": [
        "3.1-framing-inspection-checklist.pdf",
        "3.2-electrical-rough-in-log.pdf",
        "3.3-plumbing-rough-in-log.pdf",
        "3.4-hvac-rough-in-guide.pdf",
        "3.5-insulation-air-sealing-guide.pdf",
        "SECTION-3-TITLE-PAGE.pdf",
    ],
    "section-4-systems-installation": [
        "4.1-electrical-system-completion-log.pdf",
        "4.2-plumbing-system-completion-log.pdf",
        "4.3-hvac-system-completion.pdf",
        "4.4-final-systems-walkthrough.pdf",
        "SECTION-4-TITLE-PAGE.pdf",
    ],
    "section-5-finish-work": [
        "5.1-drywall-completion-checklist.pdf",
        "5.2-interior-door-installation-log.pdf",
        "5.3-trim-finish-carpentry-log.pdf",
        "5.4-flooring-installation-guide.pdf",
        "5.5-cabinet-installation-checklist.pdf",
        "5.6-paint-color-finish-tracking.pdf",
        "SECTION-5-TITLE-PAGE.pdf",
    ],
    "section-6-daily-operations": [
        "6.1-daily-job-site-log.pdf",
        "6.2-weather-delay-log.pdf",
        "6.3-material-delivery-storage-log.pdf",
        "6.4-tool-equipment-log.pdf",
        "6.5-safety-incident-report.pdf",
        "SECTION-6-TITLE-PAGE.pdf",
    ],
    "section-7-budget-expenses": [
        "7.1-expense-tracking-sheets.pdf",
        "7.2-receipt-organization-system.pdf",
        "7.3-cost-overrun-analysis.pdf",
        "7.4-payment-tracking.pdf",
        "7.5-final-budget-reconciliation.pdf",
        "SECTION-7-TITLE-PAGE.pdf",
    ],
    "section-8-quick-reference": [
        "8.1-residential-code-quick-reference.pdf",
        "8.2-span-tables.pdf",
        "8.3-material-calculators.pdf",
        "8.4-emergency-contacts.pdf",
        "8.5-common-measurements.pdf",
        "SECTION-8-TITLE-PAGE.pdf",
    ],
}

FRONT_MATTER = [
    "00-BINDER-COVER.pdf",
    "00-BINDER-SPINE-LABEL.pdf",
    "00-HOW-TO-USE-THIS-BINDER.pdf",
    "00-TABLE-OF-CONTENTS.pdf",
]

EDITABLE = {
    "editable-documents/word": [
        "2.1-subcontractor-agreement-template.docx",
        "2.2-change-order-form.docx",
        "2.3-lien-waiver-templates.docx",
        "2.4-payment-draw-schedule.docx",
    ],
    "editable-documents/excel": [
        "1.2-budget-tracking-spreadsheet.xlsx",
        "7.1-expense-tracking.xlsx",
        "7.4-payment-tracking.xlsx",
        "8.3-material-calculators.xlsx",
    ],
}


def page_count(path):
    out = subprocess.run(["pdfinfo", path], capture_output=True, text=True).stdout
    m = re.search(r"Pages:\s+(\d+)", out)
    return int(m.group(1)) if m else 0


def inventory():
    missing, total_pages, total_files, rows = [], 0, 0, []
    for rel in FRONT_MATTER:
        p = os.path.join(OUT, rel)
        if not os.path.exists(p):
            missing.append(rel)
            continue
        n = page_count(p)
        rows.append((rel, n))
        total_pages += n
        total_files += 1
    for folder, files in SECTIONS.items():
        for f in files:
            rel = f"{folder}/{f}"
            p = os.path.join(OUT, rel)
            if not os.path.exists(p):
                missing.append(rel)
                continue
            n = page_count(p)
            rows.append((rel, n))
            total_pages += n
            total_files += 1
    editable_missing = []
    for folder, files in EDITABLE.items():
        for f in files:
            rel = f"{folder}/{f}"
            if not os.path.exists(os.path.join(OUT, rel)):
                editable_missing.append(rel)
            else:
                total_files += 1
    return rows, missing, editable_missing, total_pages, total_files


def main():
    rows, missing, editable_missing, total_pages, total_files = inventory()
    for rel, n in rows:
        print(f"{n:4d}  {rel}")
    print(f"\nPDF pages total: {total_pages}")
    print(f"Files present:   {total_files}")
    if missing:
        print(f"\nMISSING PDFs ({len(missing)}):")
        for m in missing:
            print(f"  - {m}")
    if editable_missing:
        print(f"\nMISSING editable files ({len(editable_missing)}):")
        for m in editable_missing:
            print(f"  - {m}")
    if "--zip" in sys.argv:
        if missing or editable_missing:
            print("\nRefusing to zip with missing files.")
            sys.exit(1)
        if os.path.exists(ZIP_PATH):
            os.remove(ZIP_PATH)
        with zipfile.ZipFile(ZIP_PATH, "w", zipfile.ZIP_DEFLATED) as z:
            for rel in FRONT_MATTER:
                z.write(os.path.join(OUT, rel), f"{ZIP_ROOT}/{rel}")
            for folder, files in SECTIONS.items():
                for f in files:
                    z.write(os.path.join(OUT, folder, f),
                            f"{ZIP_ROOT}/{folder}/{f}")
            for folder, files in EDITABLE.items():
                for f in files:
                    z.write(os.path.join(OUT, folder, f),
                            f"{ZIP_ROOT}/{folder}/{f}")
        size = os.path.getsize(ZIP_PATH)
        print(f"\nWrote {ZIP_PATH} ({size/1024/1024:.1f} MB)")


if __name__ == "__main__":
    main()
