#!/usr/bin/env python3
"""8.2 Span Tables — rebuilt with verified IRC 2021/2018 values.

Sources (cross-verified against two independent reproductions each):
- Floor joists:   IRC Table R502.3.1(2)  (40 psf LL, 10 psf DL, L/360)
- Ceiling joists: IRC Table R802.4.1(2)  (20 psf LL limited storage, L/240)
- Rafters:        IRC 2021 Table R802.4.1(3) (30 psf ground snow, 10 psf DL,
                  ceiling not attached, L/180)
- Headers:        IRC 2021 Table R602.7(1) (30 psf snow, 24-ft building width)
- Deck joists:    IRC 2021 Table R507.6   (40 psf LL, spans w/o overhang)

The previous edition's Southern Pine values pre-dated the 2013 SPIB design-value
revision and overstated allowable spans by up to ~2 ft. Do not reuse them.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

import design as d

S = d.make_styles()
CW = d.content_width()

SECTION = "Section 8: Quick Reference Guides"
FORM_ID = "8.2"
FORM_TITLE = "Span Tables"

SPECIES = ["Southern Pine", "Douglas Fir-Larch", "Hem-Fir", "Spruce-Pine-Fir"]

# ---- IRC Table R502.3.1(2): floor joists, No. 2, 40/10, L/360 (@12/16/19.2/24)
FLOOR = {
    "2x8": {
        "Southern Pine":    ["13'-6\"", "11'-10\"", "10'-10\"", "9'-8\""],
        "Douglas Fir-Larch": ["14'-2\"", "12'-9\"", "11'-8\"", "10'-5\""],
        "Hem-Fir":          ["13'-2\"", "12'-0\"", "11'-3\"", "10'-2\""],
        "Spruce-Pine-Fir":  ["13'-6\"", "12'-3\"", "11'-8\"", "10'-5\""],
    },
    "2x10": {
        "Southern Pine":    ["16'-2\"", "14'-0\"", "12'-10\"", "11'-5\""],
        "Douglas Fir-Larch": ["18'-0\"", "15'-7\"", "14'-3\"", "12'-9\""],
        "Hem-Fir":          ["16'-10\"", "15'-2\"", "13'-10\"", "12'-5\""],
        "Spruce-Pine-Fir":  ["17'-3\"", "15'-5\"", "14'-1\"", "12'-7\""],
    },
    "2x12": {
        "Southern Pine":    ["19'-1\"", "16'-6\"", "15'-1\"", "13'-6\""],
        "Douglas Fir-Larch": ["20'-11\"", "18'-1\"", "16'-6\"", "14'-9\""],
        "Hem-Fir":          ["20'-4\"", "17'-7\"", "16'-1\"", "14'-4\""],
        "Spruce-Pine-Fir":  ["20'-7\"", "17'-10\"", "16'-3\"", "14'-7\""],
    },
}

# ---- IRC Table R802.4.1(2): ceiling joists, No. 2, 20 psf limited storage
CEILING = {
    "2x6": {
        "Southern Pine":    ["13'-11\"", "12'-0\"", "11'-0\"", "9'-10\""],
        "Douglas Fir-Larch": ["15'-0\"", "13'-0\"", "11'-11\"", "10'-8\""],
        "Hem-Fir":          ["14'-5\"", "12'-8\"", "11'-7\"", "10'-4\""],
        "Spruce-Pine-Fir":  ["14'-9\"", "12'-10\"", "11'-9\"", "10'-6\""],
    },
    "2x8": {
        "Southern Pine":    ["17'-7\"", "15'-3\"", "13'-11\"", "12'-6\""],
        "Douglas Fir-Larch": ["19'-1\"", "16'-6\"", "15'-1\"", "13'-6\""],
        "Hem-Fir":          ["18'-6\"", "16'-0\"", "14'-8\"", "13'-1\""],
        "Spruce-Pine-Fir":  ["18'-9\"", "16'-3\"", "14'-10\"", "13'-3\""],
    },
    "2x10": {
        "Southern Pine":    ["20'-11\"", "18'-1\"", "16'-6\"", "14'-9\""],
        "Douglas Fir-Larch": ["23'-3\"", "20'-2\"", "18'-5\"", "16'-5\""],
        "Hem-Fir":          ["22'-7\"", "19'-7\"", "17'-10\"", "16'-0\""],
        "Spruce-Pine-Fir":  ["22'-11\"", "19'-10\"", "18'-2\"", "16'-3\""],
    },
}

# ---- IRC 2021 Table R802.4.1(3): rafters, No. 2, 30 psf ground snow, DL 10
RAFTER = {
    "2x6": {
        "Southern Pine":    ["12'-11\"", "11'-2\"", "10'-2\"", "9'-2\""],
        "Douglas Fir-Larch": ["14'-0\"", "12'-1\"", "11'-0\"", "9'-10\""],
        "Hem-Fir":          ["13'-7\"", "11'-9\"", "10'-9\"", "9'-7\""],
        "Spruce-Pine-Fir":  ["13'-9\"", "11'-11\"", "10'-11\"", "9'-9\""],
    },
    "2x8": {
        "Southern Pine":    ["16'-4\"", "14'-2\"", "12'-11\"", "11'-7\""],
        "Douglas Fir-Larch": ["17'-8\"", "15'-4\"", "14'-0\"", "12'-6\""],
        "Hem-Fir":          ["17'-2\"", "14'-11\"", "13'-7\"", "12'-2\""],
        "Spruce-Pine-Fir":  ["17'-5\"", "15'-1\"", "13'-9\"", "12'-4\""],
    },
    "2x10": {
        "Southern Pine":    ["19'-5\"", "16'-10\"", "15'-4\"", "13'-9\""],
        "Douglas Fir-Larch": ["21'-7\"", "18'-9\"", "17'-1\"", "15'-3\""],
        "Hem-Fir":          ["21'-0\"", "18'-2\"", "16'-7\"", "14'-10\""],
        "Spruce-Pine-Fir":  ["21'-4\"", "18'-5\"", "16'-10\"", "15'-1\""],
    },
    "2x12": {
        "Southern Pine":    ["22'-10\"", "19'-10\"", "18'-1\"", "16'-2\""],
        "Douglas Fir-Larch": ["25'-1\"", "21'-8\"", "19'-10\"", "17'-9\""],
        "Hem-Fir":          ["24'-4\"", "21'-1\"", "19'-3\"", "17'-3\""],
        "Spruce-Pine-Fir":  ["24'-8\"", "21'-5\"", "19'-6\"", "17'-6\""],
    },
}

# ---- IRC 2021 Table R602.7(1): headers, 30 psf ground snow, 24-ft building
# (span, jack studs each end)
HEADERS = [
    # size, roof+ceiling, +1 center-bearing floor, +2 center-bearing floors
    ("2-2x4",  ("3'-1\"", 1),  ("2'-6\"", 1), ("2'-1\"", 1)),
    ("2-2x6",  ("4'-7\"", 1),  ("3'-9\"", 1), ("3'-2\"", 2)),
    ("2-2x8",  ("5'-9\"", 1),  ("4'-10\"", 2), ("4'-0\"", 2)),
    ("2-2x10", ("6'-10\"", 2), ("5'-8\"", 2), ("4'-9\"", 2)),
    ("2-2x12", ("8'-1\"", 2),  ("6'-8\"", 2), ("5'-7\"", 2)),
    ("3-2x8",  ("7'-3\"", 1),  ("6'-0\"", 1), ("5'-0\"", 2)),
    ("3-2x10", ("8'-7\"", 1),  ("7'-2\"", 2), ("5'-11\"", 2)),
    ("3-2x12", ("10'-1\"", 2), ("8'-5\"", 2), ("7'-0\"", 2)),
    ("4-2x8",  ("8'-4\"", 1),  ("6'-11\"", 1), ("5'-9\"", 1)),
    ("4-2x10", ("9'-11\"", 1), ("8'-3\"", 2), ("6'-10\"", 2)),
    ("4-2x12", ("11'-8\"", 1), ("9'-8\"", 2), ("8'-1\"", 2)),
]

# ---- IRC 2021 Table R507.6: deck joists, 40 psf, span without overhang
DECK = [
    ("Southern Pine #2", [
        ("2x6", "9'-11\"", "9'-0\"", "7'-7\""),
        ("2x8", "13'-1\"", "11'-10\"", "9'-8\""),
        ("2x10", "16'-2\"", "14'-0\"", "11'-5\""),
        ("2x12", "18'-0\"", "16'-6\"", "13'-4\""),
    ]),
    ("Doug Fir-Larch / Hem-Fir / SPF #2", [
        ("2x6", "8'-10\"", "8'-0\"", "6'-10\""),
        ("2x8", "11'-8\"", "10'-7\"", "8'-8\""),
        ("2x10", "14'-11\"", "13'-0\"", "10'-7\""),
        ("2x12", "17'-5\"", "15'-1\"", "12'-4\""),
    ]),
]

SPACINGS = ['12" O.C.', '16" O.C.', '19.2" O.C.', '24" O.C.']


def species_table(title, data):
    header = [Paragraph("Species (No. 2 grade)", S["cell-bold"])] + \
        [Paragraph(sp, S["cell-center"]) for sp in
         [f"<b>{x}</b>" for x in SPACINGS]]
    rows = []
    for sp in SPECIES:
        rows.append([Paragraph(sp, S["cell"])] +
                    [Paragraph(v, S["cell-center"]) for v in data[sp]])
    widths = [CW - 4 * 1.15 * inch] + [1.15 * inch] * 4
    return d.titled_table(title, header, rows, widths, S, write_rows=False)


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="Maximum allowable spans for No. 2 grade dimensional lumber, from "
            "the 2021 International Residential Code. Values are maximums — "
            "your plans and local amendments govern.")

flow.append(d.callout_box(
    "Before you use these tables",
    [Paragraph("• Values assume No. 2 grade lumber, single span, bearing at "
               "each end. Spans are in feet-inches.", S["body"]),
     Paragraph("• Your local jurisdiction may amend these values. The "
               "approved plans and your building department always govern.",
               S["body"]),
     Paragraph("• Engineered lumber (I-joists, LVL) has different span "
               "capabilities — use the manufacturer's tables.", S["body"])]))
flow.append(Spacer(1, 10))

# Floor joists
flow += d.h2("FLOOR JOISTS — Living Areas", S)
flow.append(Paragraph(
    "40 psf live load, 10 psf dead load, deflection limit L/360. "
    "IRC Table R502.3.1(2).", S["note"]))
for size in ["2x8", "2x10", "2x12"]:
    flow.append(species_table(f"Floor Joists — {size}", FLOOR[size]))
    flow.append(Spacer(1, 8))
flow.append(Paragraph(
    "Notes: O.C. = on center. For cantilevers, maximum overhang = 1/4 of the "
    "back span. Provide blocking or bridging at mid-span for joists over "
    "8 feet.", S["note"]))

# Ceiling joists
flow += d.h2("CEILING JOISTS — Attic With Limited Storage", S)
flow.append(Paragraph(
    "20 psf live load (uninhabitable attic with limited storage), deflection "
    "limit L/240. IRC Table R802.4.1(2). If your attic will never carry "
    "storage, code allows longer spans — these values are the safe, "
    "conservative choice.", S["note"]))
for size in ["2x6", "2x8", "2x10"]:
    flow.append(species_table(f"Ceiling Joists — {size}", CEILING[size]))
    flow.append(Spacer(1, 8))

# Rafters
flow += d.h2("COMMON RAFTERS — Snow Load Areas", S)
flow.append(Paragraph(
    "30 psf ground snow load, 10 psf dead load, ceiling not attached to "
    "rafters, deflection limit L/180. IRC 2021 Table R802.4.1(3). Higher "
    "snow areas require shorter spans — check your local ground snow load.",
    S["note"]))
for size in ["2x6", "2x8", "2x10", "2x12"]:
    flow.append(species_table(f"Rafters — {size}", RAFTER[size]))
    flow.append(Spacer(1, 8))

# Headers
flow += d.h2("HEADERS & GIRDERS — Exterior Bearing Walls", S)
flow.append(Paragraph(
    "Douglas Fir-Larch, Hem-Fir, Southern Pine, or Spruce-Pine-Fir, No. 2 or "
    "better. 30 psf ground snow, 24-foot building width. IRC 2021 Table "
    "R602.7(1). \"Jacks\" = number of jack (trimmer) studs required at EACH "
    "end of the header.", S["note"]))
hdr_header = [Paragraph("Header Size", S["cell-bold"]),
              Paragraph("Supporting Roof + Ceiling", S["cell-center"]),
              Paragraph("+ One Floor", S["cell-center"]),
              Paragraph("+ Two Floors", S["cell-center"])]
hdr_rows = []
for size, rc, one, two in HEADERS:
    hdr_rows.append([
        Paragraph(size, S["cell"]),
        Paragraph(f"{rc[0]} ({rc[1]} jack{'s' if rc[1] > 1 else ''})",
                  S["cell-center"]),
        Paragraph(f"{one[0]} ({one[1]} jack{'s' if one[1] > 1 else ''})",
                  S["cell-center"]),
        Paragraph(f"{two[0]} ({two[1]} jack{'s' if two[1] > 1 else ''})",
                  S["cell-center"]),
    ])
flow.append(d.titled_table(
    "Header Spans (span + jack studs per end)", hdr_header, hdr_rows,
    [1.5 * inch, (CW - 1.5 * inch) / 3.0, (CW - 1.5 * inch) / 3.0,
     (CW - 1.5 * inch) / 3.0], S, write_rows=False))
flow.append(Paragraph(
    "Notes: \"+ One Floor\" / \"+ Two Floors\" = header also supports one or "
    "two center-bearing floors above. Install headers on edge, crown up. King "
    "stud required each side in addition to jack studs. Wider buildings, "
    "higher snow loads, or clear-span floors above require larger headers — "
    "see IRC Table R602.7(1) or consult an engineer.", S["note"]))

# Deck joists
flow += d.h2("DECK JOISTS", S)
flow.append(Paragraph(
    "40 psf live load, 10 psf dead load, wet service. Span measured from face "
    "of support to face of support, no overhang. IRC 2021 Table R507.6.",
    S["note"]))
deck_header = [Paragraph("Joist Size", S["cell-bold"]),
               Paragraph('<b>12" O.C.</b>', S["cell-center"]),
               Paragraph('<b>16" O.C.</b>', S["cell-center"]),
               Paragraph('<b>24" O.C.</b>', S["cell-center"])]
for group, rows in DECK:
    deck_rows = [[Paragraph(sz, S["cell"]),
                  Paragraph(a, S["cell-center"]),
                  Paragraph(b, S["cell-center"]),
                  Paragraph(c, S["cell-center"])] for sz, a, b, c in rows]
    flow.append(d.titled_table(
        f"Deck Joists — {group}", deck_header, deck_rows,
        [1.9 * inch] + [(CW - 1.9 * inch) / 3.0] * 3, S, write_rows=False))
    flow.append(Spacer(1, 8))
flow.append(Paragraph(
    "Deck notes: use pressure-treated or naturally durable lumber; joist "
    "hangers at ledger connections; cantilever (overhang) limited to 1/4 of "
    "the actual joist span; check local amendments.", S["note"]))

flow.append(Spacer(1, 6))
flow.append(d.callout_box(
    "IMPORTANT DISCLAIMER",
    [Paragraph(
        "These tables are general reference for common residential "
        "conditions, transcribed from the 2021 International Residential "
        "Code. Actual requirements vary with species, grade, moisture, load "
        "duration, snow load, and local amendments. Confirm all structural "
        "sizing with your building department and, where required, a licensed "
        "engineer.", S["body"])]))


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "out", "section-8-quick-reference",
                       "8.2-span-tables.pdf")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    d.build_doc(out, FORM_ID, FORM_TITLE, SECTION, flow)
    print(f"built {out}")
