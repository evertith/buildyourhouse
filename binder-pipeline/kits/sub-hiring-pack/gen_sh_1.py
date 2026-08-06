#!/usr/bin/env python3
"""SH.1 Subcontractor Interview Scorecard — Subcontractor Hiring Pack."""

import os

from reportlab.lib.units import inch
from reportlab.platypus import PageBreak, Paragraph, Spacer

import kitcommon as k
import design as d

S = k.S
CW = k.CW

FORM_ID = "SH.1"
FORM_TITLE = "Subcontractor Interview Scorecard"

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="One sheet per candidate. Verify license and insurance first — "
            "those are pass/fail — then score experience and fit, check the "
            "walk-away list, and compare the bids side by side.")
flow.append(Paragraph(k.DISCLAIMER, S["note"]))

flow.append(d.FillInRow([("Trade / Scope:", 0.6), ("Interview Date:", 0.4)]))
flow.append(d.FillInRow([("Company Name:", 0.6), ("Phone:", 0.4)]))
flow.append(d.FillInRow([("Contact Person:", 0.6), ("Email:", 0.4)]))

# ---------------- SECTION A
flow += d.h2("SECTION A — PASS / FAIL VERIFICATION", S)
flow.append(Paragraph(
    "Fill this in before you score anything, and verify with the state board "
    "and the insurance carrier — not with the sub. Whether a license is "
    "required, the dollar threshold that triggers it, and which sole "
    "proprietors may skip workers' comp are all set by state law: look yours "
    "up before you accept an exemption claim.", S["body"]))
flow.append(Spacer(1, 2))

flow.append(Paragraph("License", S["h3"]))
flow.append(d.FillInRow([("License #:", 0.38), ("State:", 0.26),
                         ("Expires:", 0.36)]))
flow.append(d.FillInRow([("Verified with licensing board (agency):", 0.62),
                         ("Date checked:", 0.38)]))
flow.append(d.checkbox_choice_row(
    "Status:", ["Current", "Expired", "Not required for this trade / state"], S))
flow.append(d.checkbox_choice_row(
    "Disciplinary actions on file:", ["None found", "Found (see notes)"], S))

flow.append(Paragraph("Insurance", S["h3"]))
flow.append(k.FieldLine("General liability certificate received from the "
                        "carrier or agent directly", box=True, rule=False))
flow.append(d.FillInRow([("GL carrier:", 0.5), ("Policy #:", 0.5)]))
flow.append(d.FillInRow([("Limit per occurrence $:", 0.5),
                         ("Policy expires:", 0.5)]))
flow.append(k.FieldLine("Workers' compensation certificate received",
                        box=True, rule=False))
flow.append(d.FillInRow([("WC carrier:", 0.5), ("Policy expires:", 0.5)]))
flow.append(d.checkbox_choice_row(
    "Workers' comp:", ["Carried", "Sub claims state exemption — verify"], S))
flow.append(k.FieldLine("Asked to be named as additional insured",
                        box=True, rule=False))
flow.append(k.FieldLine("Business name on both certificates matches the name "
                        "on the bid", box=True, rule=False))
flow.append(d.FillInRow([("Called carrier to confirm policy active — date:", 0.6),
                         ("Spoke with:", 0.4)]))
flow.append(d.checkbox_choice_row("SECTION A RESULT:",
                                  ["PASS — continue", "FAIL — stop here"], S))

# ---------------- SECTION B
flow += d.h2("SECTION B — EXPERIENCE & FIT (SCORE 1–5)", S)
flow.append(Paragraph(
    "Score each line 1 (weak) to 5 (strong) from what you saw and heard. A "
    "blank is a zero — if you did not ask, you do not know.", S["body"]))

QUESTIONS = [
    "Established business — years in operation, stable crew, real address",
    "New-construction experience, not remodel work only",
    "Named three or more comparable projects from the past year, with specifics",
    "Actually read your plans, and raised a real question or challenge",
    "Realistic start date and duration — booked out, not free tomorrow",
    "Knows the inspection sequence for this trade and their first-pass record",
    "Clear answer on who physically does the work and who supervises it",
    "Communication: how they will update you, how often, and by what method",
    "Prices and documents changes in writing before doing the work",
    "Warranty and callback policy — what is covered, for how long",
    "Answered honestly about a job that went wrong and how they fixed it",
    "Spoke respectfully about inspectors, past clients and other trades",
    "Payment terms tied to milestones, deposit within your state's limits",
]

score_w = 1.75 * inch
rows = [[Paragraph(q, S["cell"]), k.RatingScale(gap=10)] for q in QUESTIONS]
flow.append(d.titled_table(
    "Scored Questions",
    [Paragraph("Question", S["cell-bold"]),
     Paragraph("Score (1–5)", S["cell-bold"])],
    rows, [CW - score_w, score_w], S,
    row_heights=[32] * len(rows)))
flow.append(Spacer(1, 8))

flow.append(d.FillInRow([("TOTAL SCORE (of 65):", 0.5),
                         ("Candidate # of:", 0.5)]))
flow.append(Paragraph(
    "Guidelines, not a verdict: <b>under 39</b> — keep looking; <b>39–51</b> — "
    "only with clean references; <b>52 and up</b> — strong candidate, and "
    "still check the references.", S["body"]))

# ---------------- SECTION C
flow += d.h2("SECTION C — WALK-AWAY RED FLAGS", S)
flow.append(Paragraph(
    "Every box below is a reason to stop, not a point to negotiate. One check "
    "outweighs any score in Section B.", S["body-bold"]))
flow.append(d.items_checklist([
    "Asks for a large deposit up front (many states cap residential deposits)",
    "Will not give a license number, or works “under someone else's license”",
    "Cannot produce a certificate of insurance sent directly by the carrier",
    "Certificate looks homemade or altered, or the policy has expired",
    "No references, or references you cannot reach",
    "Cash only, or wants to be paid without an invoice or receipt",
    "“We don't need a permit for this”, or offers to work around the inspector",
    "Wants to start immediately and has no other work booked",
    "Bid is far below the others and they cannot explain what is excluded",
    "Refuses to put the scope of work in writing",
    "Pressures you to sign today, or claims the price expires",
    "Bad-mouths inspectors, past clients, or the other trades on your job",
    "Wants materials paid for and delivered somewhere other than your site",
], S, row_height=26))

# ---------------- SECTION D
flow += d.h2("SECTION D — DECISION", S)
flow.append(d.checkbox_choice_row("VERDICT:",
                                  ["Hire", "Backup", "Reject"], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(1.5, label="Notes — what stood out, good or bad"))
flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Completed by:", 0.6), ("Date:", 0.4)]))

# ---------------- SECTION E
flow.append(PageBreak())
flow += d.h2("SECTION E — BID COMPARISON WORKSHEET", S)
flow.append(d.callout_box("Three bids, one written scope", [
    Paragraph("If two bids do not describe the same work, their prices are not "
              "comparable — get them re-quoted against your written scope. And "
              "when one bid lands well under the others, something is missing "
              "from it: a permit, an allowance, haul-off, or the part nobody "
              "wants to do. Ask what is excluded, in writing.", S["body"]),
]))
flow.append(Spacer(1, 8))

LINES = [
    ("Company", 30),
    ("Bid date / price good until", 30),
    ("Total price ($)", 30),
    ("Scope — what is included", 56),
    ("Materials supplied by (sub / owner)", 30),
    ("Exclusions — what is NOT included", 56),
    ("Earliest start date", 30),
    ("Duration / completion date", 30),
    ("Deposit asked (%) and payment terms", 38),
    ("Warranty period", 30),
    ("License + insurance verified (Y / N)", 30),
]
bid_w = (CW - 1.85 * inch) / 3
bid_rows = [[Paragraph(label, S["cell-bold"]), "", "", ""]
            for label, _h in LINES]
flow.append(d.titled_table(
    "Compare the three bids against the same written scope",
    [Paragraph("Item", S["cell-bold"]),
     Paragraph("Bid 1", S["cell-bold"]),
     Paragraph("Bid 2", S["cell-bold"]),
     Paragraph("Bid 3", S["cell-bold"])],
    bid_rows, [1.85 * inch, bid_w, bid_w, bid_w], S,
    row_heights=[h for _label, h in LINES]))
flow.append(Spacer(1, 8))
flow.append(d.WriteBox(0.8, label="Bid selected, and why"))


if __name__ == "__main__":
    print(k.build("SH.1-subcontractor-interview-scorecard.pdf",
                  FORM_ID, FORM_TITLE, flow))
