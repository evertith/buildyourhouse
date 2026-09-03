#!/usr/bin/env python3
"""PA.3 Inspection Sequence.

Two findings shape this document and neither is in general circulation.

First, Pennsylvania's required residential inspection list is FIVE items long
and it is named in the statute — 35 P.S. § 7210.501(e)(1) — not left to the
local official. Published Pennsylvania advice routinely prints a ten- to
thirteen-item list borrowed from a municipal handout and calls it the state
requirement. The difference matters in an opt-out municipality, where the
owner is buying inspections from a private agency and needs to know what he is
actually obliged to buy.

Second, and much more consequential: an owner in an opt-out municipality has
NO STATUTORY APPEAL. 34 Pa. Code § 403.121(a) requires a board of appeals only
of a municipality that adopted a UCC ordinance; § 403.63(i) grants the right to
appeal only in such a municipality; and the Industrial Board hears appeals of
DEPARTMENT decisions, which a private agency's residential decision is not. So
the opt-out bargain is: you pick your inspector, and you give up the right to
appeal him. That belongs in the document that tells you how inspections work.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

import kit as k

S = k.S
CW = k.CW

FORM_ID = "PA.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections & CO"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The five inspections Pennsylvania requires by statute, the certificate "
    "that ends the job, what to do when you disagree — and the appeal you do "
    "not have if your municipality opted out.")
flow.append(k.disclaimer())

# ------------------------------------------------------------- the five
flow += k.h2_tight("FIVE INSPECTIONS, NAMED IN THE STATUTE", 2.0)
flow.append(k.body(
    "Pennsylvania does not leave the inspection list to local practice. The "
    "Act names it, and names it in the section governing municipalities that "
    "<i>did not</i> adopt an enforcement ordinance — which is the clearest "
    "possible signal that the list is a floor everywhere. The regulation "
    "repeats it for enforcing municipalities at 34&nbsp;Pa. Code "
    "§&nbsp;403.64(d) and (f)."))
flow.append(k.callout(
    "35 P.S. § 7210.501(e)(1)", [
        Paragraph("“For one-family and two-family dwelling units and utility "
                  "and miscellaneous use structures, all of the following "
                  "five inspections shall be required: (i)&nbsp;Foundation "
                  "inspection. (ii)&nbsp;Plumbing, mechanical and electrical "
                  "inspection. (iii)&nbsp;Frame and masonry inspection. "
                  "(iv)&nbsp;Wallboard inspection. (v)&nbsp;Final "
                  "inspection. <b>The final inspection shall not be deemed "
                  "approved until all previous inspections have been "
                  "successfully completed and passed.</b>”", S["body"]),
    ]))
flow.append(k.body(
    "Read the last sentence twice. It is the sequencing rule for the whole "
    "job: a final inspection is not a way to catch up on a missed wallboard "
    "inspection. If a stage was never inspected, the final cannot be "
    "approved, and without an approved final there is no certificate of "
    "occupancy."))

rows = [
    [k.cellp("<b>1. Foundation</b>"),
     k.cellp("Before the foundation is covered. In practice this is where "
             "footing depth, reinforcement, drainage and the under-slab "
             "vapor retarder get looked at — remember Pennsylvania reduced "
             "that retarder to 6 mil (PA.2)."),
     k.cellp("§&nbsp;403.64(d)(1)")],
    [k.cellp("<b>2. Plumbing, mechanical<br/>and electrical</b>"),
     k.cellp("The rough-in inspection, written as a single item covering all "
             "three systems. Check the four amended electrical sections in "
             "PA.2 before you call for it. <b>In Allegheny County the "
             "plumbing half of this is not a UCC inspection at all</b> — it "
             "is the county's, on its own code."),
     k.cellp("§&nbsp;403.64(d)(2)")],
    [k.cellp("<b>3. Frame and masonry</b>"),
     k.cellp("The framing inspection. This is where the 2006 IRC wall "
             "bracing provisions bite, and where the floor-membrane "
             "requirement of 35 P.S. §&nbsp;7210.304(h) is checked if your "
             "floor system needs it."),
     k.cellp("§&nbsp;403.64(d)(3)")],
    [k.cellp("<b>4. Wallboard</b>"),
     k.cellp("A distinctly Pennsylvanian inspection, and one owner-builders "
             "forget because most states have no such item. It happens after "
             "the board is hung and before finish — schedule it, or your "
             "final cannot pass."),
     k.cellp("§&nbsp;403.64(d)(4)")],
    [k.cellp("<b>5. Final</b>"),
     k.cellp("The official conducts a final inspection of the completed work "
             "and files a final inspection report indicating compliance. "
             "That report is what the certificate of occupancy is issued "
             "against."),
     k.cellp("§&nbsp;403.64(f)")],
]
flow.append(k.ref_table(
    "The required five — and what each one is really checking",
    [k.cellp("Inspection", bold=True), k.cellp("What it covers", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.6 * inch, CW - 2.85 * inch, 1.25 * inch]))
flow.append(Spacer(1, 6))
flow.append(k.callout(
    "Five is the floor, not the ceiling", [
        Paragraph("Section 403.64(e) lets the official “conduct other "
                  "inspections to ascertain compliance with the Uniform "
                  "Construction Code or municipal ordinances,” and many "
                  "municipalities do — separate footing, insulation, "
                  "underground plumbing and gas-pressure inspections are all "
                  "common. So a local list of ten or twelve items is normal "
                  "and lawful. What is <b>not</b> right is a guide that "
                  "presents such a list as the statewide requirement.",
                  S["body"]),
        Paragraph("Ask your official or agency, in writing, for the list it "
                  "will actually run — and write it on the log at the back "
                  "of this document. In an opt-out municipality you are "
                  "buying that list under contract, so its length is a price "
                  "term.", S["body"]),
    ]))

# ------------------------------------------------------------- the clock
flow += k.h2_tight("THERE IS NO CLOCK ON THE INSPECTOR", 2.0)
flow.append(k.body(
    "Pennsylvania puts a statutory deadline on nearly everything else in "
    "this process — fifteen business days to rule on your permit, five to "
    "issue a certificate of occupancy, thirty days to convene an appeal "
    "hearing. <b>There is no deadline anywhere for an inspector to show "
    "up.</b> Section 403.64(b) obliges you to notify the official when work "
    "is ready and to provide access; it sets no notice period, and no "
    "provision of the Act or Chapter 403 obliges the official to respond "
    "within any time at all."))
flow.append(k.callout(
    "This is the one place opting out is a genuine advantage", [
        Paragraph("If your municipality runs the program, the schedule is "
                  "whatever the office manages and you have no statutory "
                  "lever. If your municipality opted out, you are <b>hiring "
                  "the agency under a contract you negotiate</b> — so put "
                  "response times in it. Ask for a stated turnaround on "
                  "inspection requests and on plan review, what happens on a "
                  "failed re-inspection, and what a re-inspection costs. "
                  "Nothing in the UCC gives you those terms; a contract "
                  "can.", S["body"]),
        Paragraph("Fees are worth negotiating for the same reason. Under "
                  "34 Pa. Code §&nbsp;401.2a a municipality or third-party "
                  "agency “may establish fees” with <b>no state maximum</b> — "
                  "but subsection (b) requires the fee schedule to be made "
                  "available to the public. Ask for it from more than one "
                  "agency.", S["body"]),
    ]))

# ------------------------------------------------------------------- CO
flow += k.h2_tight("THE CERTIFICATE OF OCCUPANCY", 2.0)
flow.append(k.body(
    "“A residential building may not be used or occupied without a "
    "certificate of occupancy issued by a building code official” "
    "(§&nbsp;403.65(a)). The official must issue it <b>within 5 business "
    "days</b> of receiving a final inspection report showing compliance — "
    "<b>10 business days in cities of the first class</b>, which means "
    "Philadelphia."))
flow.append(k.body(
    "Check the certificate before you file it away. The regulation requires "
    "it to state the permit number and address, the owner's name and "
    "address, the portion of the building it covers, a statement that the "
    "building was inspected for UCC compliance, the issuing official's name, "
    "<b>the construction code edition applicable</b>, whether an automatic "
    "sprinkler system is provided, and any special stipulations. The code "
    "edition line is worth having in writing — it is the record of which "
    "rules your house was actually judged against."))
flow.append(k.bullet(
    "<b>A temporary certificate is available</b> for a portion of the "
    "building that can be occupied safely, for a period the official sets "
    "(§ 403.65(f)). A partial certificate for an independently compliant "
    "portion is also possible (§ 403.65(c))."))
flow.append(k.bullet(
    "<b>In an opt-out municipality the paperwork still reaches the "
    "township.</b> The third-party agency must submit a copy of the "
    "certificate of occupancy to the municipality (§ 403.65(e)), and must "
    "send the final inspection report to the property owner, the builder and "
    "a lender designated by the builder (§§ 403.64(g), 403.103(f)). If you "
    "are your own builder, designate your own lender — that report is often "
    "what a construction loan converts on."))
flow.append(k.bullet(
    "<b>Keep the final report and the certificate permanently.</b> A "
    "third-party agency is required to retain copies of final inspection "
    "reports (§ 403.103(e)), but it is a private company. Your file is the "
    "one that will still exist when you sell."))

# --------------------------------------------------------------- appeals
flow += k.h2_tight("IF YOU DISAGREE — AND THE GAP IF YOU OPTED OUT", 2.2)
flow.append(k.body(
    "In a municipality that administers the code, the appeal route is good "
    "and it is fast. The municipality must establish or designate a board of "
    "appeals, and members of the governing body may not sit on it. For a "
    "one- or two-family dwelling the board “<b>shall convene a hearing "
    "within 30 days</b> of the appeal” and render a written decision within "
    "five business days of the last hearing — ten in cities of the first "
    "class. And then the sentence that matters: “<b>If the board of appeals "
    "fails to act within the time period under this paragraph, the appeal "
    "shall be deemed granted.</b>”"))
flow.append(k.cite(
    "35 P.S. § 7210.501(c)(1), (5). The appeal fee is capped at the actual "
    "costs of public notice, the court reporter's appearance fee and "
    "necessary administrative fees — § 7210.501(c)(4). Grounds for appeal "
    "are that the Act was incorrectly interpreted, that it does not fully "
    "apply, or that an equivalent form of construction is to be used "
    "(§ 7210.501(c)(2))."))

flow.append(k.callout_long(
    "In an opt-out municipality there is no board to appeal to", [
        Paragraph("This is the least-known fact in Pennsylvania "
                  "owner-building, and it is the other half of the opt-out "
                  "bargain. Follow the three texts:", S["body"]),
        Paragraph("<b>(1)</b> 34 Pa. Code §&nbsp;403.121(a) requires a board "
                  "of appeals of a municipality that <i>has adopted</i> a UCC "
                  "ordinance, or of municipalities party to a joint "
                  "agreement. An opt-out municipality is neither, so no board "
                  "is required and generally none exists. <b>(2)</b> "
                  "§&nbsp;403.63(i) grants a residential permit applicant the "
                  "right to appeal “in a municipality which has adopted an "
                  "ordinance for the administration and enforcement of the "
                  "act” — an express qualifier that excludes you. <b>(3)</b> "
                  "The Department's Industrial Board hears appeals from "
                  "<i>Department</i> decisions; in an opt-out municipality "
                  "your residential decision-maker is a private company, not "
                  "the Department.", S["body"]),
        Paragraph("<b>So: you choose your inspector, and you give up the "
                  "statutory right to appeal him.</b> What remains is a "
                  "written, signed complaint to L&amp;I under 34 Pa. Code "
                  "§&nbsp;403.104(a), which can lead to decertification "
                  "proceedings against the official — but that is discipline "
                  "of the inspector, not review of the decision about your "
                  "house. It will not get your framing passed.", S["body"]),
        Paragraph("<b>The practical remedy is contractual, and you must "
                  "arrange it in advance.</b> Before you sign with an "
                  "agency, ask what happens when you disagree with an "
                  "inspector: is there a supervising official who will "
                  "re-review, is there a second opinion available within the "
                  "firm, and how is it requested. Get the answer in the "
                  "engagement letter. This costs nothing to negotiate before "
                  "you hire and is unobtainable afterwards.", S["body"]),
    ]))

flow.append(Spacer(1, 4))
flow += k.h2_tight("THE ARGUMENT THAT WORKS EVERYWHERE", 1.6)
flow.append(k.body(
    "One route survives in both worlds, and it is underused. A building code "
    "official “<b>shall approve an alternative material, design or method of "
    "construction</b> if the proposed design is satisfactory and complies "
    "with the intent of the Uniform Construction Code and the offered "
    "material, method or work is equivalent to Uniform Construction Code "
    "requirements for its intended purpose.” The same subsection requires "
    "the official to accept compliance with the International Performance "
    "Code of 2021 as an alternative to compliance with the UCC. That is "
    "written into §&nbsp;403.103 — the opt-out section itself — so it binds "
    "the private agency you hired just as it binds a municipal official. "
    "“Shall approve,” not “may.” If you are proposing something unusual, "
    "make the equivalency argument in writing and keep the reply."))

# ------------------------------------------------------------------- log
flow += k.h2_tight("INSPECTION LOG", 1.6)
flow.append(k.body(
    "Fill in the five statutory inspections first, then add whatever "
    "additional items your official or agency told you it will run."))
flow += k.check_table(
    "Required inspections — 35 P.S. § 7210.501(e)(1)", [
        ("<b>1. Foundation</b> — before covering",
         [("Requested", 0.34), ("Inspected", 0.33), ("Result", 0.33)]),
        ("<b>2. Plumbing, mechanical and electrical</b> — rough-in",
         [("Requested", 0.34), ("Inspected", 0.33), ("Result", 0.33)]),
        ("<b>3. Frame and masonry</b>",
         [("Requested", 0.34), ("Inspected", 0.33), ("Result", 0.33)]),
        ("<b>4. Wallboard</b>",
         [("Requested", 0.34), ("Inspected", 0.33), ("Result", 0.33)]),
        ("<b>5. Final</b> — cannot pass until 1–4 have passed",
         [("Requested", 0.34), ("Inspected", 0.33), ("Result", 0.33)]),
    ], notes_header="Inspector / notes")
flow += k.check_table(
    "Additional inspections this jurisdiction runs — § 403.64(e)", [
        ("", [("Inspection", 0.4), ("Requested", 0.3), ("Result", 0.3)]),
        ("", [("Inspection", 0.4), ("Requested", 0.3), ("Result", 0.3)]),
        ("", [("Inspection", 0.4), ("Requested", 0.3), ("Result", 0.3)]),
        ("", [("Inspection", 0.4), ("Requested", 0.3), ("Result", 0.3)]),
        ("", [("Inspection", 0.4), ("Requested", 0.3), ("Result", 0.3)]),
    ], notes_header="Notes")
flow += k.check_table(
    "Closing out", [
        ("Final inspection report received",
         [("Date", 0.5), ("From", 0.5)]),
        ("Report sent to lender (if you designated one)",
         [("Date", 1.0)]),
        ("Certificate of occupancy issued — check it names the code edition",
         [("Date", 0.5), ("Edition shown", 0.5)]),
        ("Certificate filed with the municipality by the agency "
         "(opt-out only)", [("Confirmed", 1.0)]),
    ], notes_header="Notes")

# --------------------------------------------------------------- sources
flow.append(Spacer(1, 4))
flow.append(k.sources_table([
    ("The five required residential inspections, and the final-inspection "
     "rule", "35 P.S. § 7210.501(e)(1)"),
    ("Required inspections and reports in an enforcing municipality",
     "34 Pa. Code § 403.64(d), (f)"),
    ("Official may conduct additional inspections",
     "34 Pa. Code § 403.64(e)"),
    ("Permit holder must notify when ready; no response deadline set",
     "34 Pa. Code § 403.64(b)"),
    ("Fees may be established with no state maximum; schedule is public",
     "34 Pa. Code § 401.2a(a), (b)"),
    ("Certificate of occupancy required; 5 or 10 business days; contents",
     "34 Pa. Code § 403.65(a), (b)"),
    ("Temporary and partial certificates",
     "34 Pa. Code § 403.65(c), (f)"),
    ("Agency files the certificate with the municipality; report to owner, "
     "builder and lender",
     "34 Pa. Code §§ 403.64(g), 403.65(e), 403.103(e), (f)"),
    ("Board of appeals: 30-day hearing, 5 or 10 business days to decide, "
     "deemed granted", "35 P.S. § 7210.501(c)(5)"),
    ("Appeal fee cap and grounds for appeal",
     "35 P.S. § 7210.501(c)(2), (4)"),
    ("Board of appeals required only of enforcing municipalities",
     "34 Pa. Code §§ 403.121(a), 403.63(i)"),
    ("Complaints to the Department about officials and agencies",
     "34 Pa. Code § 403.104(a); 35 P.S. § 7210.105(a)"),
    ("Alternative materials, designs and methods must be approved if "
     "equivalent", "34 Pa. Code § 403.103(c)"),
]))
flow.append(Spacer(1, 6))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "pa-permit-kit",
                       "PA.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
