#!/usr/bin/env python3
"""SH.2 Reference Check Form — Subcontractor Hiring Pack."""

from reportlab.platypus import Paragraph, Spacer

import kitcommon as k
import design as d

S = k.S
CW = k.CW

FORM_ID = "SH.2"
FORM_TITLE = "Reference Check Form"

flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="One sheet per reference. Work down the script, write the answers "
            "where they fall, then finish the verification section — the part "
            "most owner-builders skip and later wish they had not.")
flow.append(Paragraph(k.DISCLAIMER, S["note"]))

flow.append(d.callout_box("Call. Don't email.", [
    Paragraph("Three references minimum, all from the past year, all on work "
              "like yours. You hear hesitation on the phone that never shows "
              "up in an email, and a coached reference is far harder to fake "
              "out loud. Weekday evenings, 6–8 PM.", S["body"]),
]))
flow.append(Spacer(1, 6))

flow.append(d.FillInRow([("Subcontractor / company:", 0.6), ("Trade:", 0.4)]))
flow.append(d.FillInRow([("Reference name:", 0.6), ("Phone:", 0.4)]))
flow.append(d.FillInRow([("Their project — city:", 0.6),
                         ("Date & time called:", 0.4)]))
flow.append(d.checkbox_choice_row(
    "Reference is a:", ["Homeowner", "General contractor", "Supplier"], S))

# ---------------- the call
flow += d.h2("THE CALL", S)

flow.append(d.callout_box("Open with this", [
    Paragraph("“Hi, my name is ______. I'm building a house in ______ and I'm "
              "considering ______ for the ______ work. They gave me your name "
              "as a reference — do you have five minutes for ten quick "
              "questions?”", S["body"]),
]))
flow.append(Spacer(1, 8))
flow.append(Paragraph(
    "<b>Listen, don't just record.</b> The pause before question 10 tells you "
    "more than the answer does, and generic praise with no specific story "
    "means the reference barely remembers the job.", S["body"]))
flow.append(Spacer(1, 4))

flow += k.question("1. What work did they do for you, and when?", 2)
flow += k.question("2. Was your job about the same size and scope as mine?", 1)
flow += k.question("3. Did they start on the day they said they would?", 1,
                   options=["Yes", "No"])
flow += k.question("4. Did they finish when they said they would?", 1,
                   options=["Yes", "No"])
flow += k.question("5. Did the work pass inspection the first time?", 1,
                   options=["Yes", "No", "Not permitted work"])
flow += k.question("6. Was the final price close to the quote? What changed?", 2)
flow += k.question("7. When something changed, did they price it in writing "
                   "<i>before</i> doing the work?", 1,
                   options=["Yes", "No", "Nothing changed"])
flow += k.question("8. What went wrong on the job, and how did they handle it?", 3)
flow += k.question("9. How was communication — did they return calls and keep "
                   "you posted?", 1)
flow += k.question("10. Would you hire them again?", 1,
                   options=["Yes, without hesitation", "Yes, with reservations",
                            "No"])
flow += k.question("11. Anything you wish you'd known before you hired them?", 3)

# ---------------- verification
flow += d.h2("VERIFICATION — DO NOT TAKE THEIR WORD FOR IT", S)
flow.append(Paragraph(
    "References tell you how someone works; this tells you whether they are "
    "allowed to. Licensing, workers'-comp exemptions and lien records are set "
    "by state and county — look yours up before checking a box.", S["body"]))

flow.append(Paragraph("License lookup", S["h3"]))
flow.append(d.FillInRow([("Licensing agency / board:", 0.58),
                         ("Phone or website:", 0.42)]))
flow.append(d.FillInRow([("License #:", 0.36), ("Class / trade:", 0.33),
                         ("Date checked:", 0.31)]))
flow.append(d.checkbox_choice_row(
    "Status:", ["Current", "Expired", "None on file", "Not required here"], S))
flow.append(d.checkbox_choice_row(
    "Class covers my scope:", ["Yes", "No"], S))
flow.append(d.checkbox_choice_row(
    "Board complaints or discipline:", ["None found", "Found (see notes)"], S))

flow.append(Paragraph("Insurance certificate", S["h3"]))
flow.append(d.checkbox_choice_row(
    "Certificate came from:", ["Carrier", "Agent", "The contractor (weakest)"],
    S))
flow.append(d.FillInRow([("GL carrier:", 0.4), ("Limit $:", 0.3),
                         ("Expires:", 0.3)]))
flow.append(d.FillInRow([("Workers' comp carrier:", 0.55),
                         ("Expires:", 0.45)]))
flow.append(k.FieldLine("Called the carrier or agent and confirmed the policy "
                        "is active", box=True, rule=False))
flow.append(k.FieldLine("Asked to be named as additional insured",
                        box=True, rule=False))

flow.append(Paragraph("Lien and legal history", S["h3"]))
flow.append(d.FillInRow([("County recorder / clerk searched:", 0.6),
                         ("Date:", 0.4)]))
flow.append(d.checkbox_choice_row(
    "Liens, lawsuits or judgments against them:", ["None found", "Found"], S))
flow.append(d.checkbox_choice_row(
    "Liens they filed on past jobs:", ["None found", "Found"], S))

# ---------------- result
flow += d.h2("RESULT", S)
flow.append(d.checkbox_choice_row(
    "This reference is:", ["Clear", "A concern", "Disqualifying"], S))
flow.append(Spacer(1, 4))
flow.append(d.WriteBox(0.8, label="Notes — quotes, hesitations, anything that "
                                  "did not add up"))
flow.append(Spacer(1, 8))
flow.append(d.FillInRow([("Checked by:", 0.6), ("Date:", 0.4)]))


if __name__ == "__main__":
    print(k.build("SH.2-reference-check-form.pdf", FORM_ID, FORM_TITLE, flow))
