#!/usr/bin/env python3
"""SH.3 Hiring Walkthrough — Subcontractor Hiring Pack."""

from reportlab.platypus import KeepTogether, Paragraph, Spacer

import kitcommon as k
import design as d

S = k.S
CW = k.CW

FORM_ID = "SH.3"
FORM_TITLE = "Hiring Walkthrough"


def step(n, title, paras):
    """A numbered step: heading plus its body, kept together so a step number
    never lands alone at the foot of a page."""
    block = [Paragraph(f"{n}.&nbsp;&nbsp;{title}", S["h3"])]
    block += [Paragraph(t, S["body"]) for t in paras]
    return [KeepTogether(block)]


def warning(title, body):
    """A bordered warning. KeepTogether stops the title band from stranding on
    one page with its body on the next."""
    return [Spacer(1, 4),
            KeepTogether(d.callout_box(title, [Paragraph(body, S["body"])])),
            Spacer(1, 8)]


flow = []
flow += d.doc_header(
    FORM_ID, FORM_TITLE, S,
    purpose="The order to hire a subcontractor in, and what each step protects "
            "you from. Run it once per trade.")
flow.append(Paragraph(k.DISCLAIMER, S["note"]))

flow.append(Paragraph(
    "Hiring a sub is a sequence, and the steps are cheap in the order below "
    "and expensive in any other. Verifying a license takes ten minutes before "
    "you hire; tearing out unlicensed work takes weeks after. Budget three to "
    "five hours of vetting for every sub you take seriously — it is the "
    "highest-paid time you will spend on the job.", S["body"]))
flow.append(Spacer(1, 4))

flow += step(1, "Write the scope before you call anyone", [
    "Put on paper exactly what you want done, which materials are included, "
    "what is excluded, and when you need it finished. One page is enough. "
    "Every sub bids that same page — otherwise you are comparing three "
    "different jobs and calling it a price comparison."])

flow += step(2, "Get three bids on that one scope", [
    "Two bids give you no way to spot the outlier; three do. When one lands "
    "far under the others, treat it as a question rather than a bargain — ask "
    "what was left out, and get the answer in writing before you celebrate. "
    "Record the three side by side on the bid comparison worksheet in SH.1."])

flow += step(3, "Verify the license yourself", [
    "Ask for the number, then check it with the state licensing board. Not "
    "with the sub, and not by looking at a card in their truck. Confirm it is "
    "current, that the class covers the work you are buying, and that there "
    "is no discipline on file.",
    "Whether the work requires a license at all, and above what dollar "
    "amount, is set by state law and varies widely by state and trade. Look "
    "up your own state's board before you assume either way."])

flow += warning(
    "“I work under someone else's license”",
    "Walk away. It means the person doing your work is not the person the "
    "state licensed, and when the work fails you have recourse against "
    "neither of them.")

flow += step(4, "Verify insurance — both kinds", [
    "Get a certificate for general liability and a certificate for workers' "
    "compensation, both sent to you directly by the carrier or agent. A copy "
    "handed to you by the contractor proves nothing. Ask to be named as "
    "additional insured — it costs the sub nothing — then call the carrier "
    "and confirm the policy is in force on the dates you need it."])

flow += warning(
    "General liability will not cover their injured worker",
    "Only workers' compensation does. If a sub's employee is hurt on your "
    "site and the sub carries no comp, you can be treated as the employer and "
    "left holding the medical bills and lost wages. Exemptions for true sole "
    "proprietors vary by state — but the moment a sub brings a helper, get a "
    "current certificate or send them home.")

flow += step(5, "Call three references", [
    "Call them. An email gives a coached reference all the time in the world "
    "to write something flattering. Work down SH.2 Reference Check Form: a "
    "job like yours, did they finish when they said they would, how were "
    "changes priced, and finally — would you hire them again. The pause "
    "before that last answer is the answer."])

flow += step(6, "Put it in writing before anyone starts", [
    "Use <b>2.1 Subcontractor Agreement Template</b>, included in this pack. "
    "Scope, price, schedule, exclusions, insurance, warranty, how changes get "
    "priced and how disputes get resolved — signed by both parties before a "
    "tool comes out of the truck. Have your attorney review the template "
    "before you use it."])

flow += step(7, "Do not pay a large deposit", [
    "Most subs do not need your money to start. Materials-heavy trades "
    "sometimes do, and then the deposit should track the actual cost of "
    "materials rather than a percentage someone invented on the spot.",
    "Several states cap residential deposits by statute, and the cap can be "
    "far below what a sub asks for. Check your state's limit before you agree "
    "to any number. A sub who wants a large payment before any work exists is "
    "asking you to finance their business."])

flow += step(8, "Tie every payment to a finished, inspected milestone", [
    "Use <b>2.4 Payment Draw Schedule</b>, included in this pack. Write the "
    "milestones into the agreement and pay only for work that exists and has "
    "passed inspection. Hold retainage until the punch list is closed out.",
    "Never let payments run ahead of progress. The day you are paid up on a "
    "job that is half built is the day you lose every bit of leverage you "
    "had."])

flow += step(9, "Collect a lien waiver with every payment", [
    "Use <b>2.3 Lien Waiver Templates</b>, included in this pack. Conditional "
    "waiver with the payment request, unconditional once the payment clears, "
    "final unconditional with the last check — and collect them from material "
    "suppliers and sub-subcontractors too, not just the sub you hired.",
    "Lien law is state law. Deadlines, notice requirements and the wording a "
    "waiver must carry all differ, and some states mandate a specific "
    "statutory form. Confirm what your state requires before you rely on any "
    "waiver you sign."])

flow += warning(
    "Paying the sub is not the same as paying their supplier",
    "If the sub takes your money and never pays the lumberyard, the "
    "lumberyard can still record a lien against your house — and you can end "
    "up paying for the same materials twice. Waivers are how you close that "
    "hole, on every payment, every time.")

flow += step(10, "Use a change order for every change", [
    "Use <b>2.2 Change Order Form</b>, included in this pack. Nothing changes "
    "on a handshake. Price it, schedule it, sign it, then build it. Verbal "
    "changes are where budgets quietly die, and where two honest people end "
    "up in a dispute neither of them can prove."])

# ---------------- recap
flow += d.h2("BEFORE ANYONE STARTS WORK", S)
flow.append(Paragraph(
    "Every box below should be checked for every sub on your job.", S["body"]))
flow.append(d.items_checklist([
    "Scope is written down, and every bid was made against that same scope",
    "Three bids received and compared line by line, exclusions included",
    "License number verified directly with the state licensing board",
    "General liability certificate received from the carrier or agent",
    "Workers' comp certificate received, or a state exemption confirmed",
    "Named as additional insured, and the carrier called to confirm coverage",
    "Three references called — recent work, similar to yours",
    "Written agreement signed by both parties before any work begins",
    "Deposit is zero, or within your state's legal limit for residential work",
    "Payment milestones written into the agreement and tied to inspections",
    "Lien waiver forms on hand, ready to go out with the first payment",
], S, row_height=26))

flow.append(Spacer(1, 10))
flow.append(KeepTogether(d.callout_box(
    "The two that cost the most", [
        Paragraph("Nearly every owner-builder horror story starts in one of "
                  "two places: money paid for work that did not exist yet, or "
                  "a crew that started before anything was signed. Everything "
                  "above is built to keep you out of both.", S["body"]),
    ])))


if __name__ == "__main__":
    print(k.build("SH.3-hiring-walkthrough.pdf", FORM_ID, FORM_TITLE, flow))
