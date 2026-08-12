#!/usr/bin/env python3
"""GA.1 Owner-Builder Exemption Walkthrough.

Every Georgia claim in this document was read out of the statute text at the
FindLaw O.C.G.A. mirror in August 2026 and is cited on-page. Where the statute
is silent or counties differ, the document says so and gives the verification
step.

Verified sources:
  O.C.G.A. § 43-41-17(h)  owner exemption; 24-month one-sale rule measured
                          from the sold structure's CO; no-delegation rule;
                          codes and local requirements still bind
  O.C.G.A. § 43-41-2(9)   residential contractor licensure attaches over $2,500
  O.C.G.A. § 43-41-17(b)  unlicensed contractor's contract is unenforceable
  O.C.G.A. § 43-41-17(e)  Chapter 14 trade licensees may contract directly
  O.C.G.A. § 43-41-17(f)  specialty contractors direct-to-owner; $10,000/25% cap
  O.C.G.A. § 43-41-12(a)  unlicensed contracting: misdemeanor, $500 minimum
  O.C.G.A. § 43-14-8      electrical/plumbing/conditioned-air licenses statewide
  O.C.G.A. § 43-14-13(d)  homeowner may self-perform trade work in own dwelling
  O.C.G.A. § 34-9-2(a)(2) workers' comp does not reach employers with fewer
                          than three regular employees

Still deliberately hedged: O.C.G.A. text traces to a mirror current through
March 28, 2024 (SB 503/2024, HB 635/2025, SB 125/2025 postdate it; none
reported to amend the text quoted here); whether a county requires its own
owner-builder affidavit (statute requires none — worksheet blank); the
subsection letters (e)/(f) of § 43-41-17; whether § 43-14-13(d) lets an
unlicensed helper work under you (printed as scope guidance — the statute is
silent); statutory-employer exposure under § 34-9-8 (kit says collect
certificates of insurance, never "you're safe").
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

import design as d
import kit as k

S = k.S
CW = k.CW

FORM_ID = "GA.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "Exemption & Qualification"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "How Georgia's owner-builder exemption actually works — the statute that "
    "creates it, the 24-month rule that poisons it, and the trade-work "
    "carve-outs that come with it.")

flow.append(k.disclaimer(
    "Statute text was read at the FindLaw O.C.G.A. mirror in August 2026 "
    "(stated currency March 28, 2024); statutes change."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION")
flow.append(k.body(
    "Georgia requires a licensed residential contractor for construction "
    "work whose total value exceeds <b>$2,500</b> — one of the lowest "
    "licensing thresholds in the country. The same chapter carves you out of "
    "it: build on real property you own, intend the finished building solely "
    "for occupancy by you and your family (or your firm and its employees), "
    "do not offer it for sale or lease, and you may act as your own "
    "contractor at any project cost. There is no state affidavit to sign and "
    "no fee to pay for the exemption itself — but one sale of a self-built "
    "house inside 24 months takes it away for the next one."))
flow.append(k.cite(
    "O.C.G.A. § 43-41-17(h); § 43-41-2(9). The $2,500 figure is the "
    "definition of \"residential contractor\" — work at or under it does not "
    "require licensure in the first place."))

rows = [
    [k.cellp("What is the $2,500 threshold, then?"),
     k.cellp("The point at which <i>contracting</i> requires a license. It "
             "governs the people you hire, not you.")],
    [k.cellp("Must you own the land, and live in it?"),
     k.cellp("Both. Real property owned by you, and the building intended "
             "upon completion for use or occupancy solely by you and your "
             "family, firm, or corporation — not the general public, and "
             "not offered for sale or lease")],
    [k.cellp("What kills the exemption?"),
     k.cellp("One prior sale or transfer of a structure you built without a "
             "licensed contractor, within the past 24 months — measured "
             "from the date that structure's certificate of occupancy "
             "issued")],
    [k.cellp("What do you sign, and who checks it?"),
     k.cellp("The statute requires no affidavit. Many Georgia counties "
             "require their own notarized owner-builder affidavit as local "
             "practice — ask yours and record the answer below")],
]
flow.append(k.ref_table(
    "The exemption at a glance",
    [k.cellp("Question", bold=True), k.cellp("Georgia's answer", bold=True)],
    rows, [2.7 * inch, CW - 2.7 * inch]))

# ---------------------------------------------------------------- the exemption
flow += k.h2_tight("THE EXEMPTION ITSELF — O.C.G.A. § 43-41-17(h)")
flow.append(k.body(
    "The licensing chapter carves the owner out in one long sentence: "
    "\"<i>Nothing in this chapter shall preclude any person from "
    "constructing a building or structure on real property owned by such "
    "person which is intended upon completion for use or occupancy solely "
    "by that person and his or her family, firm, or corporation and its "
    "employees, and not for use by the general public and not offered for "
    "sale or lease. In so doing, such person may act as his or her own "
    "contractor personally providing direct supervision and management of "
    "all work not performed by licensed contractors.</i>\""))

flow.append(k.callout("The conditions — all of them, all the time", [
    Paragraph("<b>(i)</b> The building sits on <b>real property you own</b>.",
              S["body"]),
    Paragraph("<b>(ii)</b> It is intended upon completion for use or "
              "occupancy <b>solely by you and your family, firm, or "
              "corporation and its employees</b> — and <b>not for use by "
              "the general public</b>.", S["body"]),
    Paragraph("<b>(iii)</b> It is <b>not offered for sale or lease</b>.",
              S["body"]),
    Paragraph("<b>(iv)</b> You <b>personally provide direct supervision and "
              "management</b> of all work not performed by licensed "
              "contractors.", S["body"]),
]))
flow.append(Spacer(1, 8))
flow.append(k.body(
    "Read condition (iv) closely — it is the working half of the exemption. "
    "You are not exempted from running the job; you are exempted from the "
    "license <i>because</i> you run the job. Work you do not supervise "
    "yourself must be performed by licensed contractors."))

flow.append(k.callout(
    "The 24-month rule — one sale poisons the next build", [
        Paragraph("\"<i>However, if, under this subsection, the person or "
                  "his or her family, firm, or corporation has previously "
                  "sold or transferred a building or structure which had "
                  "been constructed by such person acting without a "
                  "licensed residential or general contractor within the "
                  "prior 24 month period, starting from the date on which a "
                  "certificate of occupancy was issued for such building or "
                  "structure, then such person may not, under this "
                  "subsection, construct another separate building or "
                  "structure …</i>\" — and the statute goes on to presume "
                  "that the new building was never intended solely for your "
                  "own occupancy.", S["body"]),
        Paragraph("Three details people get wrong. First, the clock runs "
                  "from the <b>certificate of occupancy of the structure "
                  "you sold</b> — not from its sale date. Second, it "
                  "reaches sales by your <b>family, firm, or "
                  "corporation</b>, not just you. Third, it is both a bar "
                  "(\"may not … construct another\") and an <b>intent "
                  "presumption</b> that reaches backward: a quick sale is "
                  "evidence you never qualified. Keep every CO you are "
                  "ever issued.", S["body"]),
    ]))
flow.append(k.cite(
    "O.C.G.A. § 43-41-17(h). The closing presumption is condensed here — "
    "read the full sentence at the statute before you rely on its exact "
    "reach."))

# ---------------------------------------------------------------- no delegation
flow += k.h2_tight("NO DELEGATION — AND THE CODES STILL BIND YOU")
flow.append(k.body(
    "Two more sentences of § 43-41-17(h) close the loopholes people go "
    "looking for. On handing the job to someone else: \"<i>Further, such "
    "person may not delegate the responsibility to directly supervise and "
    "manage all or any part of the work relating thereto to any other "
    "person unless that person is licensed under this chapter and the work "
    "being performed is within the scope of that person's license.</i>\" "
    "Your unlicensed brother-in-law cannot run the job for you — on paper "
    "or in fact."))
flow.append(k.body(
    "And on the idea that no license means no rules: \"<i>In any event, "
    "however, all such work must be done in conformity with … any "
    "applicable county or municipal resolutions, ordinances, codes, "
    "permitting, or inspection requirements.</i>\" The exemption removes "
    "the license, not the building code — even in a county that enforces "
    "nothing (§ 8-2-25(a) makes the eight state minimum codes statewide; "
    "see GA.2 and GA.3)."))
flow.append(k.cite("O.C.G.A. § 43-41-17(h); § 8-2-25(a)."))

# ---------------------------------------------------------------- affidavit
flow += k.h2_tight("WHAT YOU SIGN — USUALLY A COUNTY FORM, NEVER A STATE ONE")
flow.append(k.body(
    "Unlike several neighboring states, § 43-41-17(h) contains <b>no "
    "affidavit or disclosure requirement</b> — the statutory text carries "
    "no form, no oath, and no filing. That absence was verified against the "
    "statute text in August 2026. What fills the gap is local practice: "
    "many Georgia counties require a <b>notarized owner-builder "
    "affidavit</b> of their own design at permit application, and some add "
    "a homeowner disclaimer form for each trade permit. Neither is a state "
    "requirement; both are real requirements where they exist. Ask your "
    "permit office and record the answer:"))
flow.append(Spacer(1, 4))
flow.append(d.FillInRow([("County affidavit required?  Y / N — form name:",
                          0.66), ("Notary needed:", 0.34)]))
flow.append(k.cite(
    "Statutory absence: O.C.G.A. § 43-41-17(h), read in full. County "
    "practice varies and is not cited to any statute — that is the point; "
    "get your county's answer in writing."))

# ---------------------------------------------------------------- hiring help
flow += k.h2_tight("HIRING HELP — WHO MAY LAWFULLY CONTRACT WITH YOU")
flow.append(k.body(
    "Because licensure attaches at $2,500, nearly every sub you hire is "
    "either licensed or breaking the law. The chapter leaves you three "
    "clean lanes:"))
flow.append(k.bullet(
    "<b>Licensed residential contractors</b> — for anything, at any "
    "value."))
flow.append(k.bullet(
    "<b>Chapter 14 trade licensees</b> — electrical, plumbing, conditioned "
    "air, low-voltage, and utility contractors may contract directly with "
    "you: \"<i>nothing in this chapter shall preclude a person licensed "
    "under Chapter 14 of this title … from offering to perform, "
    "performing, engaging in, or contracting to engage in the performance "
    "of construction work or services directly with an owner</i>.\" "
    "(§ 43-41-17(e))"))
flow.append(k.bullet(
    "<b>Specialty contractors</b> — framing, roofing, tile, and similar "
    "single-trade outfits may contract directly with you for their trade, "
    "plus incidental other work capped at the greater of <b>$10,000 or 25 "
    "percent</b> of the contract's total value at the time of contracting. "
    "(§ 43-41-17(f))"))
flow.append(k.cite(
    "O.C.G.A. § 43-41-17(e), (f). Subsection letters read from the "
    "statute's structure listing — two extractions agree, but confirm the "
    "letters at the official code if you ever cite them in a dispute."))

flow.append(k.callout(
    "Why you verify every license — the contract is void without one", [
        Paragraph("\"<i>As a matter of public policy, any contract entered "
                  "into on or after July 1, 2008, for the performance of "
                  "work for which a residential contractor or general "
                  "contractor license is required by this chapter … and "
                  "which is between an owner and a contractor who does not "
                  "have a valid and current license required for such work "
                  "… shall be unenforceable in law or in equity by the "
                  "unlicensed contractor.</i>\" (§ 43-41-17(b))", S["body"]),
        Paragraph("That sounds like it only hurts the contractor. It hurts "
                  "you too: a void contract voids its warranties in "
                  "practice, and an unlicensed sub who walks off leaves "
                  "you nothing to enforce. Verify every license before "
                  "signing — contractor and trade licenses both check at "
                  "sos.ga.gov.", S["body"]),
    ]))
flow.append(k.cite(
    "O.C.G.A. § 43-41-17(b). A 2024 session law (SB 503) renamed \"general "
    "contractor\" to \"commercial general contractor\" throughout the "
    "chapter — older handouts and the mirror text this kit quotes predate "
    "the rename; the rule itself is unchanged."))

flow.append(k.body(
    "<b>The criminal side.</b> Unlicensed contracting is a misdemeanor: on "
    "conviction, \"<i>a fine of not less than $500.00 or imprisonment of "
    "three months, or both fine and imprisonment in the discretion of the "
    "court</i>\" — per offense. That is the club held over anyone you hire "
    "without a license, and over you if you build outside the exemption's "
    "conditions and keep contracting anyway."))
flow.append(k.cite("O.C.G.A. § 43-41-12(a)."))

# ---------------------------------------------------------------- trade work
flow += k.h2_tight("DOING YOUR OWN ELECTRICAL, PLUMBING, AND HVAC WORK")
flow.append(k.body(
    "Georgia licenses the trades statewide — \"<i>No person shall engage in "
    "the electrical contracting business as an electrical contractor unless "
    "such person has a valid license from the Division of Electrical "
    "Contractors</i>,\" with parallel commands for master and journeyman "
    "plumbers and for conditioned air contractors (§ 43-14-8(a)–(c)). But "
    "the same chapter hands the homeowner a complete carve-out:"))

flow.append(k.callout("The homeowner trade carve-out — § 43-14-13(d)", [
    Paragraph("\"<i>This chapter shall not prohibit an individual from "
              "installing, altering, or repairing plumbing fixtures, "
              "air-conditioning and heating, air-conditioning and heating "
              "fixtures, utility systems, or electrical or low-voltage "
              "wiring services in a residential dwelling owned or occupied "
              "by such individual; provided, however, that all such work "
              "must be done in conformity with all other provisions of "
              "this chapter, the rules and regulations of the board, and "
              "any applicable county or municipal resolutions, ordinances, "
              "codes, or inspection requirements.</i>\"", S["body"]),
]))
flow.append(Spacer(1, 8))
flow.append(k.body(
    "<b>Read the scope before you celebrate.</b> The carve-out is written "
    "for \"an individual\" working on a dwelling that individual owns or "
    "occupies — it authorizes <b>your own hands</b>, not an unlicensed "
    "helper working under you; anyone you hire for trade work must hold "
    "the § 43-14-8 license. The statute is silent on helpers, so treat "
    "that as the safe reading, not settled law. And note the proviso: your "
    "self-performed work is still inspected to the trade codes (the state "
    "IPC, 2023 NEC, and IMC/IFGC — see GA.2) wherever your county "
    "inspects at all."))
flow.append(k.cite(
    "O.C.G.A. § 43-14-13(d), quoted in full; § 43-14-8(a)–(c). The "
    "helper-scope reading is guidance drawn from the exemption's wording, "
    "not quoted prohibition — the statute does not address helpers either "
    "way."))

# ---------------------------------------------------------------- workers comp
flow += k.h2_tight("WORKERS' COMPENSATION — WHEN HIRED HELP CHANGES THINGS")
flow.append(k.body(
    "Georgia's Workers' Compensation Act does not reach small employers: "
    "it does not apply \"<i>to any person, firm, or private corporation, "
    "including any public service corporation, that has regularly in "
    "service less than three employees in the same business within this "
    "state</i>\" (§ 34-9-2(a)(2)). An owner-builder who hires licensed "
    "subcontractors and regularly employs nobody is generally outside it."))
flow.append(k.body(
    "Two cautions. First, hiring helpers <b>directly</b> — by the hour, "
    "rather than contracting with their company — can put you at three "
    "regular employees faster than you expect. Second, § 34-9-8 makes a "
    "\"principal\" contractor liable for the comp of an uninsured sub's "
    "workers; whether an owner-builder can be that principal is a "
    "fact-and-case-law question this kit will not answer for you. The "
    "cheap protection is the same either way: <b>collect a certificate "
    "of insurance from every sub before they start</b>."))
flow.append(k.cite(
    "O.C.G.A. § 34-9-2(a)(2), quoted; § 34-9-8 flagged, not resolved — if "
    "you will pay workers directly, get advice before you do."))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS BEFORE YOU APPLY")
flow.append(k.body(
    "Every line below is a condition the statutes impose or a fact a "
    "permit counter (or a lender) will ask you to prove. Work down it with "
    "a pen. If you cannot check a box, resolve it before you file — not "
    "after."))

flow += k.check_table("Step 1 — Ownership and intent", [
    ("Land is owned in your name (or your firm's) as of the application "
     "date", [("Deed book/page:", 0.55), ("Parcel ID:", 0.45)]),
    "The finished building is intended solely for use or occupancy by you "
    "and your family (or your firm and its employees) — not the general "
    "public",
    "It is not offered for sale or lease, and no sale, lease, or listing "
    "is contemplated",
    ("Neither you nor your family, firm, or corporation has sold or "
     "transferred a self-built structure within the prior 24 months, "
     "measured from that structure's CO date",
     [("Prior self-build CO date (if any):", 1.0)]),
    ("Your county's owner-builder affidavit requirement confirmed and "
     "recorded", [("Required? Y/N:", 0.35), ("Form:", 0.65)]),
], notes_header="Notes / evidence")

flow += k.check_table("Step 2 — What you are taking on", [
    "You will personally provide direct supervision and management of all "
    "work not performed by licensed contractors — and will not delegate "
    "that role to anyone unlicensed",
    ("Every contractor you hire whose work exceeds $2,500 holds the "
     "required Georgia license — verified at sos.ga.gov before signing",
     [("Verified on:", 1.0)]),
    "Every electrical, plumbing, conditioned-air, low-voltage, or utility "
    "sub holds the Chapter 43-14 trade license — the homeowner carve-out "
    "covers your hands, not theirs",
    ("Certificate of insurance collected from every sub before work "
     "starts", [("File location:", 1.0)]),
    "You understand the state minimum codes bind this project even if "
    "your county inspects nothing (§ 8-2-25(a); § 43-41-17(h))",
], notes_header="Notes / evidence")

flow.append(k.body(
    "<b>Step 3 — the paperwork itself</b> (permit application, septic "
    "permit, Notice of Commencement, energy-test reports, and everything "
    "your county adds on top) is worked in <b>GA.2 Permit Application "
    "Checklist</b>, and each document is described in <b>GA.5 Forms &amp; "
    "Documents Index</b>."))

# ---------------------------------------------------------------- losing it
flow += k.h2_tight("WHAT TAKES THE EXEMPTION AWAY")
flow.append(k.bullet(
    "Offering the home for <b>sale or lease</b> — the exemption is written "
    "for a building \"not offered for sale or lease,\" full stop."))
flow.append(k.bullet(
    "A <b>prior sale within 24 months</b> of a self-built structure, "
    "measured from that structure's CO — by you or your family, firm, or "
    "corporation."))
flow.append(k.bullet("Not owning the land the building sits on."))
flow.append(k.bullet(
    "Handing supervision and management to an unlicensed person while "
    "your name stays on the permit."))
flow.append(k.bullet(
    "Building for the general public's use, or for occupants beyond your "
    "family, firm, or corporation and its employees."))
flow.append(Spacer(1, 4))
flow.append(k.body(
    "Consequences the statutes actually name: outside the exemption you "
    "are an unlicensed contractor — a <b>misdemeanor with a $500 minimum "
    "fine per offense</b> (§ 43-41-12(a)) — and any contract you sign to "
    "build for others is <b>unenforceable</b> (§ 43-41-17(b))."))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("Owner exemption: own land, occupancy solely by you/family/firm, not "
     "the public, not for sale or lease; act as your own contractor",
     "§ 43-41-17(h)"),
    ("One-sale-per-24-months rule; clock runs from the sold structure's "
     "CO; intent presumption", "§ 43-41-17(h)"),
    ("No delegation of supervision except to licensees within scope; all "
     "work in conformity with codes and local requirements",
     "§ 43-41-17(h)"),
    ("No state affidavit appears in the exemption; county affidavits are "
     "local practice", "§ 43-41-17(h) (absence verified)"),
    ("Residential contractor licensure attaches where work exceeds $2,500",
     "§ 43-41-2(9)"),
    ("Chapter 14 trade licensees and specialty contractors may contract "
     "directly with an owner; $10,000/25% incidental cap",
     "§ 43-41-17(e), (f)"),
    ("Unlicensed contractor's contract unenforceable; unlicensed "
     "contracting a misdemeanor, $500 minimum per offense",
     "§ 43-41-17(b); § 43-41-12(a)"),
    ("Trade licenses statewide; homeowner may self-perform trade work in "
     "own dwelling, subject to codes and inspection",
     "§ 43-14-8(a)–(c); § 43-14-13(d)"),
    ("Workers' comp does not reach employers with fewer than three "
     "regular employees", "§ 34-9-2(a)(2)"),
    ("Eight state minimum codes bind statewide without local adoption",
     "§ 8-2-25(a)"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ga-permit-kit",
                       "GA.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
