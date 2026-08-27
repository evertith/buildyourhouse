#!/usr/bin/env python3
"""MT.0 Cover + How to Use.

Page 1 is drawn on the canvas in the binder cover idiom — double frame,
centered title block, aligned project fill-in rules, brand and edition line.
The following pages carry the kit's thesis: Montana writes a real statewide
building code and then, by statute, declines to apply it to your house. What
survives that exemption is what this kit is about — an electrical permit
enforced at the power meter, an energy code you certify yourself, and a
sanitation review that can decide whether the lot is buildable at all.

Sources verified August 2026 (each also cited where it appears in MT.1-MT.5).
Statute text read from the Montana Code Annotated at mca.legmt.gov, the
Legislature's own server:
  50-60-102(1)(a)   the state building code "does not apply to" residential
                    buildings of fewer than five dwelling units unless the
                    local legislative body adopts it
  50-60-102(2)      the state "may not enforce" the code for those buildings
  50-60-102(5)      the ENERGY provisions apply to residential buildings anyway
  50-60-802(1)      and are enforced by builder self-certification in writing
  50-60-205(1)      where no local code is adopted, the state code applies and
                    the state enforces it
  50-60-301(2)(a)   a local government may NOT be more stringent than the state
                    code — a ceiling, not a floor
  50-60-604         electrical permits and inspections, state or certified local
  50-60-605         no power supplier may energize without an electrical permit
  50-60-607         energizing without a permit is a misdemeanor
  37-68-103(3)(a)   the homeowner electrical exemption reaches the LICENSE only
  50-60-506(4)      the homeowner plumbing exemption reaches the PERMIT itself

Still deliberately hedged: which local governments run certified programs (a
fact that rots — the kit gives the verification step and the state's own list);
every adopted code edition, which lives in ARM Title 24 chapter 301 rather than
in statute; and every fee.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

import design as d
import kit as k

S = k.S
CW = k.CW
PAGE_W, PAGE_H = letter

FORM_ID = "MT.0"
FORM_TITLE = "Cover & How to Use"
TOPIC = "Start Here"


def draw_cover(c):
    d.register_fonts()
    c.setStrokeColor(d.INK)
    c.setLineWidth(2)
    c.rect(0.55 * inch, 0.55 * inch, PAGE_W - 1.1 * inch, PAGE_H - 1.1 * inch)
    c.setLineWidth(0.75)
    c.rect(0.65 * inch, 0.65 * inch, PAGE_W - 1.3 * inch, PAGE_H - 1.3 * inch)

    cx = PAGE_W / 2

    c.setFillColor(d.INK)
    c.setFont(d.BOLD, 30)
    c.drawCentredString(cx, 8.75 * inch, "MONTANA")
    c.drawCentredString(cx, 8.25 * inch, "OWNER-BUILDER")
    c.drawCentredString(cx, 7.75 * inch, "PERMIT KIT")
    c.setLineWidth(1.5)
    c.line(1.9 * inch, 7.47 * inch, PAGE_W - 1.9 * inch, 7.47 * inch)
    c.setFont(d.BODY, 12.5)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 7.13 * inch,
                        "The code that may not apply to your house · "
                        "The permits that apply anyway")

    # project fields — labels right-aligned to a common gutter
    fields = ["Project Address:", "County:",
              "City / unincorporated:", "Owner-Builder:"]
    label_x = 3.35 * inch
    rule_x0 = 3.5 * inch
    rule_x1 = PAGE_W - 1.35 * inch
    y = 5.5 * inch
    c.setFillColor(d.INK)
    for label in fields:
        c.setFont(d.BODY, 12)
        c.drawRightString(label_x, y, label)
        c.setLineWidth(0.75)
        c.line(rule_x0, y - 2, rule_x1, y - 2)
        y -= 0.62 * inch

    # verification stamp
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 2.35 * inch,
                        "Every Montana statute, rule, and requirement in this "
                        "kit is cited on")
    c.drawCentredString(cx, 2.13 * inch,
                        "the page it appears on — verified August 2026.")

    c.setFont(d.BOLD, 12)
    c.setFillColor(d.INK)
    c.drawCentredString(cx, 1.5 * inch, "BUILD YOUR HOUSE")
    c.setFont(d.BODY, 10)
    c.setFillColor(d.FURNITURE_GREY)
    c.drawCentredString(cx, 1.27 * inch, "build-your-house.com")
    c.drawCentredString(cx, 1.03 * inch, "First Edition — 2026")


flow = [Spacer(1, 1)]

flow.append(Paragraph("How to Use This Kit", S["title"]))
flow.append(Paragraph(
    "Five working documents that take a Montana owner-builder from \"does a "
    "building permit even exist for my parcel?\" to a house you can legally "
    "occupy, insure, and — the part Montana enforces hardest — get permanent "
    "power to.",
    S["subtitle"]))

flow.append(k.body(
    "Montana looks, at first, like the easiest state in the country to build "
    "your own house in. It licenses no general contractor. It writes one "
    "statewide building code and then says in plain statutory language that "
    "the code <b>\"does not apply to … residential buildings containing less "
    "than five dwelling units\"</b> unless your local government has adopted "
    "it, and that the state <b>\"may not enforce\"</b> it for those buildings "
    "(50-60-102(1)(a), (2), MCA). Across most of Montana's land area that is "
    "literally true: nobody will issue you a building permit, because there "
    "is no building permit to issue."))

flow.append(k.body(
    "Then people conclude \"no permits,\" and that is where it gets "
    "expensive. Montana puts the building code, the plumbing permit, and the "
    "electrical permit in <b>one chapter but four different parts</b>, and "
    "the exemption you just read sits in Part 1 and reaches Part 2. It does "
    "not reach the electrical part. It does not reach the energy provisions "
    "— the same section that grants the exemption turns around three "
    "subsections later and says the energy code applies to your house anyway. "
    "And none of it reaches water, wastewater, or the sanitation review that "
    "in rural Montana decides whether a lot is buildable at all."))

flow.append(k.callout("The Montana inversion — read this twice", [
    Paragraph("It is entirely normal, and legal, to build a house in Montana "
              "where <b>no building permit exists</b>, <b>no plan review "
              "happens</b>, and <b>no building inspector ever visits</b> — "
              "and to still owe an <b>electrical permit</b> that your power "
              "supplier is forbidden to connect you without, and a "
              "<b>written energy-code certification</b> that you, as the "
              "builder, must hand to yourself, as the owner, when the house "
              "is finished. Energizing an installation with no electrical "
              "permit is a <b>misdemeanor</b>. "
              "(50-60-102(1)(a), (5); 50-60-605; 50-60-607; 50-60-802(1))",
              S["body"]),
]))
flow.append(Spacer(1, 6))

flow += k.h2_tight("WHAT THE EXEMPTION REACHES — AND WHAT IT DOES NOT")
sys_rows = [
    [k.cellp("<b>Building code and building permit</b>"),
     k.cellp("<b>Exempt</b> — usually"),
     k.cellp("The state building code \"<i>does not apply to … residential "
             "buildings containing less than five dwelling units</i>\" "
             "<b>unless the local legislative body by ordinance or resolution "
             "makes the state building code applicable</b>, and the state "
             "\"<i>may not enforce</i>\" it for them (50-60-102(1)(a), (2)). "
             "Inside a certified city or county that has adopted it, you are "
             "back under a full permit and inspection process.")],
    [k.cellp("<b>Energy code</b>"),
     k.cellp("<b>Applies anyway</b>"),
     k.cellp("Three subsections later: the energy-conservation provisions "
             "\"<i>apply to residential buildings</i>,\" excepting only farm "
             "and ranch buildings and private garages (50-60-102(5)(a)). For "
             "a house under five units not otherwise covered, they are "
             "enforced \"<i>through the builder self-certification "
             "program</i>\" (50-60-102(5)(b)(ii); 50-60-802).")],
    [k.cellp("<b>Electrical permit</b>"),
     k.cellp("<b>Applies anyway</b>"),
     k.cellp("Electrical installations are Part 6, with their own exceptions "
             "list at 50-60-602 — and that list says nothing about houses. "
             "The permit and inspection duty is at 50-60-604, and 50-60-605 "
             "bars your power supplier from energizing without the permit in "
             "hand. See MT.1.")],
    [k.cellp("<b>Plumbing permit</b>"),
     k.cellp("<b>Owner exemption</b>"),
     k.cellp("A separate and unusually generous carve-out: the owner of "
             "residential property may install \"<i>all sanitary plumbing and "
             "potable water supply piping without a permit if the owner "
             "personally does the work</i>\" (50-60-506(4)). Read MT.1 before "
             "you rely on it — the license rule attached to it is narrower "
             "than the permit rule.")],
    [k.cellp("<b>Water, septic, land</b>"),
     k.cellp("<b>Untouched</b>"),
     k.cellp("Nothing in chapter 60 speaks to wells, septic systems, "
             "sanitation review, floodplain, access, or zoning. These are "
             "different agencies under different titles, and in rural "
             "Montana they are the approvals that actually gate the build. "
             "See MT.2.")],
]
flow.append(k.ref_table(
    "One exemption, five different answers",
    [k.cellp("The piece of your house", bold=True),
     k.cellp("Status", bold=True),
     k.cellp("What the statute actually says", bold=True)],
    sys_rows, [1.55 * inch, 1.0 * inch, CW - 2.55 * inch]))
flow.append(k.cite(
    "50-60-102(1)(a), (2), (5)(a), (5)(b)(ii); 50-60-506(4); 50-60-602; "
    "50-60-604; 50-60-605; 50-60-802, MCA. Statute text read from the Montana "
    "Code Annotated at mca.legmt.gov, August 2026. How to settle each of "
    "these for your own parcel is worked in MT.4."))

flow += k.h2("THE FOUR QUESTIONS THIS KIT MAKES YOU ANSWER FIRST")
flow.append(k.body(
    "Nothing else can be answered until these are, and they are independent "
    "of one another. <b>(1)</b> Has the county, city, or town my parcel sits "
    "in adopted the state building code for residential buildings, and is its "
    "enforcement program certified? <b>(2)</b> Who issues my <b>electrical</b> "
    "permit — the Department of Labor &amp; Industry, or a certified local "
    "program? <b>(3)</b> Does my lot already have sanitation approval, and "
    "can it get a septic permit and a legal water supply at all? <b>(4)</b> "
    "What is the ground snow load at my exact site, and who is going to "
    "engineer the roof to it? In Montana that last question is not a "
    "formality — it is the one the absence of an inspector makes most "
    "dangerous."))

flow += k.h2_tight("WHAT IS IN THE KIT")
rows = [
    [k.cellp("<b>MT.1</b>"), k.cellp("Owner-Builder Exemption Walkthrough"),
     k.cellp("No state contractor license, a building code that may not apply "
             "— and the three duties that survive anyway. Includes the kit's "
             "headline finding: the homeowner electrical exemption is a "
             "<i>license</i> exemption only, while the plumbing one reaches "
             "the <i>permit</i>. <b>Read this first.</b>")],
    [k.cellp("<b>MT.2</b>"), k.cellp("Permit Application Checklist"),
     k.cellp("Sanitation, water, and access first — because in Montana those "
             "decide whether the lot is buildable — then the building permit "
             "if one exists, then the electrical permit that exists either "
             "way.")],
    [k.cellp("<b>MT.3</b>"), k.cellp("Inspection Sequence"),
     k.cellp("What gets inspected when a building inspector is involved, what "
             "gets inspected when one is not, and the power-supplier release "
             "that is the real finish line.")],
    [k.cellp("<b>MT.4</b>"), k.cellp("Where-to-File Directory"),
     k.cellp("How to determine whether your parcel is inside a certified "
             "local program, the state offices that own the rest, and a page "
             "to fill in your own.")],
    [k.cellp("<b>MT.5</b>"), k.cellp("Forms &amp; Documents Index"),
     k.cellp("Each named form and certificate you will meet, which office it "
             "comes from — and the ones people go looking for that Montana "
             "does not have.")],
]
flow.append(k.ref_table(
    "The five documents",
    [k.cellp("", bold=True), k.cellp("Document", bold=True),
     k.cellp("What it does for you", bold=True)],
    rows, [0.55 * inch, 2.15 * inch, CW - 2.7 * inch]))

flow += k.h2("HOW TO USE IT")
flow.append(k.body(
    "<b>Read MT.1 first</b>, before you plan to do your own wiring or "
    "plumbing. Montana's homeowner exemptions are real and among the most "
    "generous in the country, and they are also written in two different "
    "titles with two different scopes — the difference decides whether you "
    "owe a permit. <b>Work MT.2 with a pen, starting at the bottom of the "
    "page</b>: sanitation approval and a legal water supply are the long "
    "poles on a rural Montana parcel, and a lot that cannot get them cannot "
    "get a house. <b>Keep MT.3 on the job</b> — where no building inspector "
    "is coming, the log in it is the only construction record your future "
    "lender, insurer, or buyer will ever see. And <b>fill in MT.4 before you "
    "need it</b>: Montana splits the answers across a state bureau, possibly "
    "a certified local program, a county sanitarian, DEQ, and DNRC."))

flow.append(Spacer(1, 6))
flow.append(k.callout(
    "How these facts were checked — and what this is not", [
        Paragraph("Every Montana claim here was read against its primary "
                  "source in August 2026 — statute text from the Montana Code "
                  "Annotated on the Legislature's own server at "
                  "mca.legmt.gov, code adoptions from the Administrative "
                  "Rules of Montana at rules.mt.gov, agency facts from the "
                  "agency's own pages — and is cited where it appears. Where "
                  "a widely repeated statement about Montana turned out to "
                  "come from an agency summary rather than the statute, this "
                  "kit prints the statute and says so. Where the answer is "
                  "genuinely local, the kit gives you the verification step "
                  "rather than a number that would rot. Statutes and adopted "
                  "code editions change. This is a process reference, not "
                  "legal advice.", S["body"]),
    ]))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "mt-permit-kit",
                       "MT.0-cover-and-how-to-use.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow, cover_fn=draw_cover)
    print(f"built {out}")
