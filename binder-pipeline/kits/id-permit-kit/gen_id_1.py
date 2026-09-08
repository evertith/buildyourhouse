#!/usr/bin/env python3
"""ID.1 The Building Permit Is Optional, the Trade Permits Are Not.

Every Idaho claim in this document was read against its primary source in
September 2026 and is cited on-page. Statutes were read on the Legislature's
own server (legislature.idaho.gov, one section per page); rules from the IDAPA
chapter PDFs at adminrules.idaho.gov; the DOPL forms from dopl.idaho.gov.

Verified sources:
  § 39-4103(1), (2)     the Act AUTHORIZES; the buildings it puts under DOPL
  § 39-4111(1), (2)     the two permit clauses — "purview of the division" and
                        "local government jurisdiction enforcing building codes"
  § 39-4116(1)-(7)      how a local government becomes enforcing; the codes it
                        must adopt; sprinkler exemption; what it may amend
                        (R301 design criteria); ag buildings; laws at application
  § 39-4117(1)          the published permit-process document — the verification
                        step for "is my county enforcing?"
  § 39-9701(2)          energy-code preemption of every local government
  § 41-253(2)           5-acre rural exemption from IFC water/access
  § 54-1001B            state electrical inspection inapplicable in a city or
                        county running its own program; 30 days' notice; 1-year
                        backstop
  § 54-1005(3), (4)     the power supplier may not energize before a passed
                        inspection; contractor-only exception by rule
  IDAPA 24.39.10.200.04 that rule: temporary construction power at the request
                        of a LICENSED ELECTRICAL CONTRACTOR
  § 54-1016(2)(a)       electrical LICENSING exemption — "primary or secondary
                        residence"; grid-tied renewables preplan review
  § 54-2602(1)(a)       plumbing certificate exemption — "owns or is a contract
                        purchaser"
  § 54-2620(1), (2)     plumbing permit statewide; issued to a (1)(a) owner
  § 54-5002(1)(a)       HVAC certificate exemption — same test as plumbing
  § 54-5016(1)          HVAC permit "from the authority having jurisdiction"
  IDAPA 24.39.20.500.01.b, 24.39.70.500.01.b  homeowners "must secure" a permit
  DOPL homeowner permit applications (ELE rev. 9/13/2022; PLB rev. 8/17/2022;
                        HVAC rev. 9/13/2022)  the certification: "will personally
                        perform" / "not used for commercial purposes or rented
                        by a tenant"
  DOPL Plan Review Application (rev. 9/12/2023)  "DOPL does NOT issue building
                        permits for projects not owned by the State"
  § 54-5202, -5203(3), -5204, -5205(2)(f), (k), (l), (p), -5208, -5209, -5210,
  -5217              contractor REGISTRATION; the owner exemptions verbatim;
                        no lien, no suit; $300,000 GL; the permit face
  § 45-525              general-contractor disclosure to the homeowner
  § 72-212              workers' compensation exemptions; "casual employment"
                        undefined in § 72-102 (verified absence)
  § 55-2505(12)         never-inhabited new house exempt from the disclosure form
  IDAPA 58.01.03.005.01, .006.08.b   septic permit; owner may install own
                        standard system
  § 42-235, § 42-238(2), (3)   $75 drilling permit; no owner may drill

DELIBERATELY NOT CLAIMED, and why:
  - "Not for sale, rent, or lease" as a homeowner-permit rule. "Sale" and
    "lease" appear in no Idaho statute, rule or DOPL form. The form says "not
    used for commercial purposes or rented by a tenant."
  - A list of which counties have no building department. No state agency
    publishes one, and § 39-4116(1) lets any county adopt or contract for a
    program at any time. The document gives the verification step instead.
  - Which cities beyond Boise and Coeur d'Alene run their own trade programs.
    DOPL holds the list (30 days' notice is required) but publishes only a
    permit map and an inspector schedule.
  - Whether IRC Part IX appendices (radon, tiny houses) are enforceable in a
    jurisdiction that has not spoken to them. Unresolved; the document says ask.
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
sec = k.sec
NB = k.NB
CITE = k.CITE_COL

FORM_ID = "ID.1"
FORM_TITLE = "The Building Permit Is Optional, the Trade Permits Are Not"
TOPIC = "Who Enforces What"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Who, if anyone, enforces a building code on your parcel — and the three "
    "permits that apply whatever the answer is.")

flow.append(k.disclaimer(
    "Statute text was read on the Idaho Legislature's own site in September "
    "2026, rules from the current IDAPA chapters, and the owner certifications "
    "from DOPL's own permit forms. Where a sentence is quoted, it is quoted "
    "verbatim."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION", reserve=2.0)
flow.append(k.body(
    "Idaho is the state where <b>the building permit is optional but the "
    "trade permits are not</b> — and where the owner exemptions everyone "
    "quotes are three different tests in three different chapters, none of "
    "which says what the web pages say."))
rows = [
    [k.cellp("Do you need a license to build your own house?"),
     k.cellp(f"<b>No.</b> Idaho registers contractors rather than licensing "
             f"them, and an owner \"performing construction on the owner's "
             f"personal residential real property, <b>whether or not occupied "
             f"by the owner</b>\" is exempt ({sec('54-5205(2)(l)')})")],
    [k.cellp("Do you need a building permit?"),
     k.cellp(f"<b>Only if your city or county has adopted a building-code "
             f"ordinance.</b> The Act makes it unlawful to build without a "
             f"permit \"in a local government jurisdiction enforcing building "
             f"codes\" — and says nothing about anywhere else "
             f"({sec('39-4111(2)')})")],
    [k.cellp("Does the state issue one where the county does not?"),
     k.cellp("<b>No.</b> DOPL's own form: \"DOPL does NOT issue building "
             "permits for projects not owned by the State. Contact the local "
             "government for these projects\"")],
    [k.cellp("Do you need electrical, plumbing and HVAC permits?"),
     k.cellp(f"<b>Yes, everywhere in the state</b>, from DOPL unless your "
             f"city or county runs its own program — and a homeowner doing "
             f"his own work buys them too ({sec('54-1005')}, "
             f"{sec('54-2620')}, {sec('54-5016')})")],
    [k.cellp("May you do your own wiring, plumbing and HVAC?"),
     k.cellp("<b>Yes, on homeowner permits</b> — but the three exemptions "
             "are three different tests. See the section on them")],
    [k.cellp("Is there a \"not for sale, rent or lease\" rule?"),
     k.cellp("<b>Not in any statute or rule.</b> The DOPL form you sign says "
             "\"not used for commercial purposes or rented by a tenant\" and "
             "\"will personally perform the work.\" That is the form's "
             "condition, and it is the only place the words appear")],
    [k.cellp("What about septic and the well?"),
     k.cellp(f"A health-district installation permit before any septic work "
             f"(IDAPA 58.01.03.005.01) and a $75 IDWR drilling permit before "
             f"any well ({sec('42-235')}). You may install your own standard "
             f"septic system. <b>You may not drill your own well</b>")],
]
flow.append(k.ref_table(
    "The Idaho position at a glance",
    [k.cellp("Question", bold=True), k.cellp("Idaho's answer", bold=True)],
    rows, [2.35 * inch, CW - 2.35 * inch]))
flow.append(k.cite(
    "Idaho Code Title 39, Chapter 41 (the Building Code Act); Title 54, "
    "Chapters 10 (electrical), 26 (plumbing), 50 (HVAC) and 52 (contractor "
    "registration); Title 42 (wells). Rules of the Division of Occupational "
    "and Professional Licenses at IDAPA 24.39; DEQ septic rules at IDAPA "
    "58.01.03. All read September 2026."))

# ---------------------------------------------------------------- who enforces
flow += k.h2_tight("FIRST — DOES ANYONE ENFORCE A BUILDING CODE WHERE YOU ARE?",
                   reserve=2.2)
flow.append(k.body(
    "The Act's first substantive sentence is the whole story: \"This chapter "
    f"<b>authorizes</b> the state division of occupational and professional "
    f"licenses and local governments to adopt and enforce building codes\" "
    f"({sec('39-4103(1)')}). It authorizes. It does not impose. The buildings "
    f"it places under the state are \"all buildings and other facilities owned "
    f"by any state government agency or entity\" ({sec('39-4103(2)')}), plus "
    f"manufactured and modular units ({sec('39-4116(7)')}). A private house "
    f"is not on that list. The permit section then has exactly two clauses:"))
flow.append(k.callout_long(
    f"Idaho Code {sec('39-4111')} — Permits required", [
        Paragraph("\"(1) It shall be unlawful for any person to do … any "
                  "construction, improvement, extension or alteration of any "
                  "building, residence or structure, <b>coming under the "
                  "purview of the division</b>, in the state of Idaho without "
                  "first procuring a permit from the division …", S["body"]),
        Paragraph("(2) It shall be unlawful for any person to do … any "
                  "construction, improvement, extension or alteration of any "
                  "building, residence or structure <b>in a local government "
                  "jurisdiction enforcing building codes</b>, without first "
                  "procuring a permit in accordance with the applicable "
                  "ordinance or ordinances of the local government.\"",
                  S["body"]),
        Paragraph("A private house in a county that has adopted no "
                  "building-code ordinance is in neither clause. That is the "
                  "whole \"no-permit county\" phenomenon, and it is statutory "
                  "— not a gap in enforcement.", S["body"]),
        Paragraph("<b>And the agency says so on its own form.</b> DOPL's Plan "
                  "Review Application (revised 12&#160;September 2023), in "
                  "the project-type box: \"The Division of Occupational and "
                  "Professional Licenses is responsible for projects owned by "
                  "the State of Idaho or any of its departments or agencies … "
                  "<b>DOPL does NOT issue building permits for projects not "
                  "owned by the State. Contact the local government for "
                  "these projects.</b>\" Any guide that calls DOPL \"the "
                  "default building authority\" for a house is wrong, and "
                  "this sentence is the citation.", S["body"]),
    ]))
flow.append(Spacer(1, 4))
flow.append(k.body(
    f"<b>How a local government becomes an enforcing one.</b> \"Local "
    f"governments that have not previously instituted and implemented a code "
    f"enforcement program … may elect to implement a building code "
    f"enforcement program by passing an ordinance evidencing the intent to do "
    f"so. Local governments may contract with a public or private entity to "
    f"administer their building code enforcement program\" "
    f"({sec('39-4116(1)')}). Two consequences. Any county can adopt a program "
    f"at any time, so no printed list would stay true. And the unit is the "
    f"<b>jurisdiction</b>: a city's ordinance governs inside its limits, the "
    f"county's outside them, and the two routinely differ."))
flow.append(k.callout_long(
    "The lookup — the statute created the verification step for you", [
        Paragraph(f"<b>1. Look up your CITY first.</b> If the parcel is "
                  f"inside city limits, the city's ordinance governs, not the "
                  f"county's. Then the county for an unincorporated parcel.",
                  S["body"]),
        Paragraph(f"<b>2. Look for the permit-process document.</b> Since "
                  f"1&#160;July 2025, \"a local government that requires "
                  f"building permits shall make available a document that "
                  f"describes in detail the requirements of its building "
                  f"permit process … on its website and in physical form upon "
                  f"request\" ({sec('39-4117(1)')}). If the city or county "
                  f"requires building permits, that document must exist. If "
                  f"it does not, ask why.", S["body"]),
        Paragraph("<b>3. If there is no building department, get it in "
                  "writing.</b> A dated email from the county clerk or "
                  "planning office stating that no building-code ordinance "
                  "has been adopted. In five years, when an appraiser or "
                  "insurer asks why there is no permit on file, that email is "
                  "the answer.", S["body"]),
        Paragraph("<b>4. Then check the trade side separately</b> — it has "
                  "its own map. DOPL's permit page links a location-based map "
                  "(\"Purchase your permit on-line HERE Based on location\") "
                  "that tells you whether DOPL or a local program issues the "
                  "electrical, plumbing and HVAC permits for your address. "
                  "ID.4 has the addresses.", S["body"]),
        Paragraph("<b>5. Write both answers on the cover of this kit.</b> "
                  "They are two different answers.", S["body"]),
    ]))

# ---------------------------------------------------------------- what survives
flow += k.h2_tight("WHAT SURVIVES WHEN THERE IS NO BUILDING PERMIT", reserve=1.8)
flow.append(k.body(
    "Five permits, from three agencies, none of which reads the Building Code "
    "Act. Every one applies in a county with no building department exactly "
    "as it applies in Boise."))
rows = [
    [k.cellp("<b>Electrical permit</b>"),
     k.cellp("From DOPL, except \"within cities or counties that, by "
             "ordinance or building code, prescribe the manner in which "
             "wires or equipment … shall be installed … and provided that "
             "actual inspections are made.\" Bought <b>before work is "
             "commenced</b>. Enforced by your utility — see below"),
     k.cellp(f"{sec('54-1001B(1)')}; {sec('54-1005')}; IDAPA "
             f"24.39.10.500.01.a")],
    [k.cellp("<b>Plumbing permit</b>"),
     k.cellp("Unlawful to do any plumbing \"in the state of Idaho without "
             "first procuring a permit from the division,\" except inside a "
             "city or county with an equivalent ordinance. \"Homeowners "
             "making plumbing installations on their own premises … must "
             "secure a plumbing permit\""),
     k.cellp(f"{sec('54-2620(1)')}; IDAPA 24.39.20.500.01.b")],
    [k.cellp("<b>HVAC permit</b>"),
     k.cellp("Unlawful to install any HVAC system \"in any building, "
             "residence or structure in the state of Idaho without first "
             "obtaining a permit from the authority having jurisdiction\" — "
             "DOPL unless a local mechanical program exists. Repair and "
             "maintenance of an existing system excepted"),
     k.cellp(f"{sec('54-5016(1)')}; IDAPA 24.39.70.500.01.b")],
    [k.cellp("<b>Septic installation permit</b>"),
     k.cellp("\"No person may modify, repair or expand or install any "
             "individual or subsurface sewage disposal system within the "
             "state of Idaho unless there is a valid installation permit.\" "
             "Issued by your public health district"),
     k.cellp("IDAPA 58.01.03.005.01")],
    [k.cellp("<b>Well drilling permit</b>"),
     k.cellp("\"Prior to beginning construction of any well … the driller or "
             "well owner shall obtain a permit from the director of the "
             "department of water resources.\" $75 for a domestic well"),
     k.cellp(sec("42-235"))],
]
flow.append(k.ref_table(
    "Five permits that do not care whether your county has a building code",
    [k.cellp("Permit", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.35 * inch, CW - 1.35 * inch - CITE, CITE]))
flow.append(k.cite(
    f"<b>Licensing, by contrast, is exclusively the state's.</b> No local "
    f"jurisdiction may require additional electrical licensure or fees "
    f"({sec('54-1002(5)')}); the same for HVAC ({sec('54-5015(2)')}); and "
    f"since 1&#160;January 2007 no city or county may run its own contractor "
    f"registration program ({sec('54-5213(1)')}). A local program changes who "
    f"issues the <i>permit</i>, never who licenses the <i>person</i>."))

# ---------------------------------------------------------------- utility lock
flow += k.h2_tight("THE PERMIT YOUR POWER COMPANY ENFORCES — AND THE "
                   "TEMPORARY-POWER TRAP", reserve=2.4)
flow.append(k.body(
    "Most states enforce the electrical permit with a fine. Idaho enforces it "
    "at the meter, and names the co-ops:"))
flow.append(k.callout_long(
    f"Idaho Code {sec('54-1005(3)')}–(4), verbatim", [
        Paragraph("\"(3) Individuals, firms, <b>cooperatives</b>, corporations, "
                  "or municipalities selling electricity, hereinafter known as "
                  "the power supplier, <b>shall not connect with or energize "
                  "any electrical installation</b>, coming under the "
                  "provisions of this chapter, <b>unless an inspection has "
                  "been conducted and resulted as 'passed'</b> by the "
                  "administrator, covering the installation to be energized. "
                  "Electrical installations approved by the board and "
                  "addressed through administrative rule may be connected and "
                  "energized by the power supplier after the purchase of an "
                  "electrical permit by a <b>licensed electrical "
                  "contractor</b>.", S["body"]),
        Paragraph("(4) It shall be unlawful for any person … other than a "
                  "power supplier to energize any electrical installation "
                  "coming under the provisions of this chapter prior to the "
                  "purchase of an electrical permit covering such "
                  "installation.\"", S["body"]),
    ]))
flow.append(k.body(
    "Read the last sentence of (3) again, because the rule that implements "
    "it is the trap for anyone on a homeowner permit:"))
flow.append(k.callout(
    "IDAPA 24.39.10.200.04 — the only door to power before inspection", [
        Paragraph("\"At the request of a <b>licensed electrical contractor</b> "
                  "and upon receipt of a copy of an electrical permit, a power "
                  "supply company may connect and energize an electrical "
                  "service, to the line side of the service disconnect, prior "
                  "to a passed inspection in the following situations: to "
                  "preserve life or property or to provide <b>temporary "
                  "service for construction</b>. Any contractor energizing an "
                  "electrical installation prior to an inspection assumes full "
                  "responsibility for the installation.\"", S["body"]),
    ]))
flow.append(Spacer(1, 4))
flow.append(k.body(
    "<b>What that means on a homeowner permit:</b> the utility may not "
    "energize a construction service ahead of a passed inspection at "
    "<i>your</i> request. The exception is written for a licensed contractor's "
    "permit. So the first decision on the electrical track is made before the "
    "footings: either a licensed electrical contractor pulls the permit for "
    "the temporary service and the utility energizes it on his request, or "
    "you build the temporary service yourself on your homeowner permit and "
    "wait for a state inspector to pass it before the meter goes in, or you "
    "run the job on a generator. ID.3 sets the three options out with the "
    "48-business-hour inspection clock that now applies to that inspection."))

# ---------------------------------------------------------------- three tests
flow += k.h2_tight("THREE OWNER EXEMPTIONS, THREE DIFFERENT TESTS", reserve=2.4)
flow.append(k.body(
    "\"The owner-builder exemption\" in Idaho is really three provisions in "
    "three chapters, and they do not say the same thing. Each is quoted at "
    "the words that decide arguments."))
rows = [
    [k.cellp(f"<b>Contractor registration</b><br/>{sec('54-5205(2)(l)')}"),
     k.cellp("\"An owner performing construction on the owner's personal "
             "residential real property, <b>whether or not occupied by the "
             "owner</b>\""),
     k.cellp("<b>No occupancy test.</b> Its anti-flip proviso attaches only "
             "to an owner \"who is otherwise regulated by this chapter\" — "
             "someone in the contracting business — building \"for the "
             "purpose of promptly selling\"")],
    [k.cellp(f"<b>Electrical — licensing only</b><br/>{sec('54-1016(2)(a)')}"),
     k.cellp("\"The <b>licensing provisions</b> of this chapter shall not "
             "apply to … any property owner performing <b>noncommercial</b> "
             "electrical work in the owner's <b>primary or secondary "
             "residence</b> or associated outbuildings or land associated "
             "with the entire property on which those buildings sit\""),
     k.cellp("<b>A license-only exemption.</b> The permit duty and the "
             "utility lock are untouched. Grid-tied renewables need \"a "
             "preplan review in accordance with local jurisdictions' "
             "policies\" before the permit")],
    [k.cellp(f"<b>Plumbing</b><br/>{sec('54-2602(1)(a)')}<br/>"
             f"<b>HVAC</b><br/>{sec('54-5002(1)(a)')}"),
     k.cellp("Certificate of competency not required for \"any person who "
             "does plumbing work [installs or maintains an HVAC system] in a "
             "<b>single or duplex family dwelling</b>, including accessory "
             "buildings, quarters and grounds … provided that such person "
             "<b>owns or is a contract purchaser</b> of the premises\""),
     k.cellp("<b>No residence test at all</b>, and a contract purchaser "
             "qualifies. Identical wording in both chapters. Both add: you "
             "must \"comply with the minimum standards and rules\" — the "
             "code still applies to you")],
]
flow.append(k.ref_table(
    "The three layers, quoted where it matters",
    [k.cellp("Which exemption", bold=True), k.cellp("What it says", bold=True),
     k.cellp("What that means", bold=True)],
    rows, [1.45 * inch, (CW - 1.45 * inch) * 0.52, (CW - 1.45 * inch) * 0.48]))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Where \"not rented by a tenant\" and \"will personally perform\" actually "
    "live", [
        Paragraph("Not in the statutes above, and not in the rules — IDAPA "
                  "24.39.20.500.01.b and 24.39.70.500.01.b simply say such "
                  "homeowners \"must secure\" a permit. They are the "
                  "certification printed on all three <b>DOPL homeowner "
                  "permit applications</b>, identical on each: \"I certify "
                  "that I am the owner of the residential property and "
                  "<b>will personally perform the work</b> covered by this "
                  "permit. I recognize this permit is only valid for work on a "
                  "primary or secondary residence and associated outbuildings "
                  "<b>not used for commercial purposes or rented by a "
                  "tenant</b>. By signing this, I accept responsibility for all "
                  "the work being performed, and understand that all work must "
                  "be inspected.\"", S["body"]),
        Paragraph("So the operative conditions on a homeowner trade permit are "
                  "an <b>agency form condition</b>, and they are exactly two: "
                  "you do the work yourself, and the building is not "
                  "commercial or tenanted. <b>\"Sale\" and \"lease\" appear "
                  "nowhere</b> — not in Title 54, not in IDAPA 24.39, not on "
                  "the form. A guide that prints \"not for sale, rent, or "
                  "lease\" has combined the form's words with someone else's "
                  "state.", S["body"]),
    ]))

flow.append(Spacer(1, 4))
flow.append(k.body(
    "<b>The two anti-flip provisos are different, and neither is a "
    "\"12-month rule.\"</b> Guides collapse them. The statute keeps them "
    "apart:"))
rows = [
    [k.cellp(f"<b>You hire a registered contractor</b><br/>"
             f"{sec('54-5205(2)(k)')}"),
     k.cellp("Exempt — but not \"an owner who, <b>with the intent to evade "
             "this chapter</b>, constructs a building, residence or other "
             "improvement on the owner's property with the intention and for "
             "the purpose of selling the improved property at any time during "
             "the construction or within twelve (12) months of completion\"")],
    [k.cellp(f"<b>You do the construction yourself</b><br/>"
             f"{sec('54-5205(2)(l)')}"),
     k.cellp("Exempt — but not \"an owner <b>who is otherwise regulated by "
             "this chapter</b> who constructs a building … with the intention "
             "and for the purpose of promptly selling the improved property, "
             "unless the owner has continuously occupied the property as the "
             "owner's primary residence for not less than twelve (12) months "
             "prior to the sale\"")],
]
flow.append(k.ref_table(
    "Two provisos, two qualifiers",
    [k.cellp("Your situation", bold=True), k.cellp("The proviso, verbatim",
                                                   bold=True)],
    rows, [1.85 * inch, CW - 1.85 * inch]))
flow.append(k.cite(
    "Read the qualifiers. Proviso (k) needs <i>intent to evade</i>; proviso "
    "(l) reaches only an owner <i>otherwise regulated by this chapter</i> — "
    "that is, a person already in the contracting business. An ordinary "
    "owner-builder who finishes the house, lives in it, and later sells is "
    f"inside both. Also useful: work under <b>$2,000</b> aggregate that is "
    f"not part of a larger project ({sec('54-5205(2)(f)')}), and \"a person "
    f"working on the person's own residence, if the residence is owned by a "
    f"person other than the resident\" ({sec('54-5205(2)(p)')})."))

# ---------------------------------------------------------------- permit face
flow += k.h2_tight("THE PERMIT FACE — \"NO CONTRACTOR REGISTRATION PROVIDED\"",
                   reserve=2.0)
flow.append(k.body(
    f"This is the statutory root of every \"owner-builder exemption "
    f"declaration\" form a county hands out. The form is local; the phrase "
    f"and the posting duty are state law. No permit issuer \"shall issue any "
    f"permit without first requesting presentment of an Idaho contractor's "
    f"registration number … provided however, a permit may be issued to a "
    f"person otherwise exempt from the provisions of this chapter provided "
    f"such permit shall conspicuously contain the phrase <b>'no contractor "
    f"registration provided'</b> on the face of such permit. No authority "
    f"charged with the duty of issuing such permit shall be required to verify "
    f"that the person applying for such permit is exempt\" "
    f"({sec('54-5209(1)')}). And: \"All building permits or other permits for "
    f"construction of any type shall be <b>posted at the construction "
    f"site</b>\" so that phrase is visible ({sec('54-5209(2)')}). DOPL's "
    f"trade permits come with an orange Job Identification Sticker for the "
    f"same purpose."))

# ---------------------------------------------------------------- local powers
flow += k.h2_tight("WHAT YOUR COUNTY MAY CHANGE, AND WHAT IT MAY NOT",
                   reserve=2.4)
flow.append(k.body(
    "An enforcing jurisdiction does not write its own code. It must adopt, by "
    "ordinance, the International Building Code, \"Idaho residential code, "
    f"parts I-III and IX\" and the \"2018 Idaho energy conservation code\" "
    f"({sec('39-4116(2)')}) — and may not adopt a newer IRC or IECC than the "
    f"Idaho Building Code Board has. What it may touch is short and specific:"))
rows = [
    [k.cellp("<b>Design criteria — snow, frost, wind, seismic, flood</b>"),
     k.cellp("Locally amendable by ordinance: IRC Part I (administrative), "
             "Part II (definitions), \"<b>Section R301, Design Criteria</b>\" "
             "and Part IX (appendices). <b>No statewide snow-load, "
             "frost-depth or seismic figure exists</b> — ask the building "
             "official for the adopted value or the required study, and "
             "write it in ID.2"),
     k.cellp(sec("39-4116(4)(c)"))],
    [k.cellp("<b>The rest of Part III</b>"),
     k.cellp("Only on a finding of \"good cause for building or life "
             "safety,\" after a public hearing on 30 days' written notice"),
     k.cellp(sec("39-4116(4)(d)"))],
    [k.cellp("<b>Anything the Board rejected</b>"),
     k.cellp("A local jurisdiction \"shall not adopt any provision … that "
             "[has] been expressly rejected or exempted\" by the Board"),
     k.cellp(sec("39-4116(4)(b)"))],
    [k.cellp("<b>Energy — nothing</b>"),
     k.cellp("The energy chapter \"preempt[s], eliminate[s], and prohibit[s]\" "
             "any local energy requirement \"that differ[s] from or [is] more "
             "extensive than\" the state code. \"Verify locally\" is the "
             "wrong instruction here"),
     k.cellp(sec("39-9701(2)"))],
    [k.cellp("<b>Sprinklers — nothing</b>"),
     k.cellp("One- and two-family dwellings \"are hereby exempted\" from "
             "every sprinkler requirement in the IFC, IBC and residential "
             "code. Binding on local governments; voluntary installation "
             "allowed"),
     k.cellp(sec("39-4116(3)"))],
    [k.cellp("<b>The law that governs your permit</b>"),
     k.cellp("\"Permits shall be governed by the laws in effect at the time "
             "the permit application is received.\" File before a change, "
             "and the change does not reach you"),
     k.cellp(sec("39-4116(6)"))],
]
flow.append(k.ref_table(
    "The local government's powers over the residential code",
    [k.cellp("Subject", bold=True), k.cellp("What the Act says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.6 * inch, CW - 1.6 * inch - CITE, CITE]))
flow.append(k.cite(
    f"<b>Two rural carve-outs worth knowing.</b> Agricultural buildings are "
    f"exempt from the codes, but the exemption \"does not include … a place of "
    f"human habitation, which means a space in a building for living, "
    f"sleeping, or cooking\" ({sec('39-4116(5)')}) — so no \"barndominium\" "
    f"rides on it. And a detached single-family dwelling on <b>five acres or "
    f"more</b>, outside a city and its area of impact, \"shall be exempt from "
    f"the water supply and access requirements\" of the International Fire "
    f"Code unless a county ordinance requires them ({sec('41-253(2)')}). "
    f"<b>One open question:</b> Part IX is the IRC appendices (radon, tiny "
    f"houses among them), and no source read here resolves whether adopting "
    f"\"Part IX\" wholesale makes an appendix enforceable where the local "
    f"ordinance is silent. Ask the building official in writing which "
    f"appendices the ordinance adopted."))

# ---------------------------------------------------------------- hiring
flow += k.h2_tight("WHEN YOU HIRE — REGISTRATION, AND THE TEETH BEHIND IT",
                   reserve=2.4)
flow.append(k.body(
    f"Idaho's contractor credential is a <b>registration</b>: no examination, "
    f"no experience test. What the application demands tells you what it is "
    f"for — a workers' compensation certificate \"or a statement why not "
    f"required,\" and general liability insurance <b>including products and "
    f"completed operations of at least $300,000</b> single limit "
    f"({sec('54-5210(1)')}). The definition of contractor reaches anyone who "
    f"\"undertakes, offers to undertake, purports to have the capacity to "
    f"undertake, or submits a bid to, or does himself or by or through "
    f"others, perform construction\" ({sec('54-5203(3)')}) — every trade you "
    f"hire is inside it unless separately licensed. Three provisions make "
    f"checking worth your while:"))
rows = [
    [k.cellp("<b>No lien</b>"),
     k.cellp("An unregistered contractor \"shall be denied and shall be "
             "deemed to have conclusively waived any right to place a lien "
             "upon real property\" — except subs, employees and suppliers "
             "who did not know"),
     k.cellp(sec("54-5208"))],
    [k.cellp("<b>No lawsuit for payment</b>"),
     k.cellp("An unregistered contractor may not \"bring or maintain any "
             "action in any court of this state for the collection of "
             "compensation\""),
     k.cellp(sec("54-5217(2)"))],
    [k.cellp("<b>Insurance you can name</b>"),
     k.cellp("Every registrant carries the $300,000 policy, and \"the name of "
             "the insurance company, the insured and policy number shall be "
             "made available … to persons … stating that they possess a "
             "claim against the contractor\""),
     k.cellp(sec("54-5210(1)(e)"))],
    [k.cellp("<b>Four disclosures you are owed</b>"),
     k.cellp("Before any residential contract over $2,000 a general "
             "contractor must disclose in writing that you may (a) require "
             "lien waivers from subs, (b) receive proof of liability and "
             "workers' compensation cover, (c) buy extended title insurance "
             "against unfiled liens, and (d) require a surety bond — and "
             "before final payment must hand over a signed list of every sub "
             "and supplier over $500. Failure is a Consumer Protection Act "
             "violation. <b>When you are your own GC, each trade with a "
             "direct contract over $2,000 is the \"general contractor\" for "
             "this section</b>"),
     k.cellp(f"{sec('45-525(1)')}, (3)–(5)")],
]
flow.append(k.ref_table(
    "Why the registration number on the invoice matters",
    [k.cellp("", bold=True), k.cellp("What the statute says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - CITE, CITE]))
flow.append(k.cite(
    "Verify registration, electrical licenses and plumbing and HVAC "
    "certificates in one place: DOPL's public search at "
    "<b>edopl.idaho.gov</b> (Online Services → Public Search). Electrical "
    f"contractors must carry $300,000 liability ({sec('54-1003A(1)')}); "
    f"plumbing and HVAC contractors post a $2,000 compliance bond "
    f"({sec('54-2606(3)(d)')}; {sec('54-5007')}). Mechanics' liens: a claim "
    f"must be recorded within <b>90&#160;days</b> of the last labor or "
    f"materials and a copy served on you within <b>5 business days</b> of "
    f"recording ({sec('45-507')}). Collect a lien waiver at every payment."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "Workers' compensation — the honest position", [
        Paragraph(f"Exempt from coverage \"unless coverage thereof is "
                  f"elected\": \"casual employment,\" household family members "
                  f"of a sole proprietor, and the sole proprietor himself "
                  f"({sec('72-212(2)')}, (4), (6)). <b>\"Casual employment\" "
                  f"is not defined</b> — the definitions section, "
                  f"{sec('72-102')}, has no entry for it — so this kit does "
                  f"not tell you that paying day labor is exempt. The same "
                  f"section defines \"employer\" to include \"the owner or "
                  f"lessee of premises … who, by reason of there being an "
                  f"independent contractor or for any other reason, is not "
                  f"the direct employer of the workers there employed\" "
                  f"({sec('72-102(12)(a)')}). That is the reason to demand a "
                  f"workers' compensation certificate from every trade — "
                  f"registered contractors must have filed one — and to ask "
                  f"the Industrial Commission before paying anyone by the "
                  f"hour.", S["body"]),
    ]))

# ---------------------------------------------------------------- selling
flow += k.h2_tight("WHEN YOU SELL", reserve=1.8)
flow.append(k.body(
    f"The Property Condition Disclosure Act requires the {sec('55-2508')} "
    f"form on any transfer of a one- to four-unit residence — except "
    f"\"a transfer that involved <b>newly constructed residential real "
    f"property that previously has not been inhabited</b>, except that "
    f"disclosure of annexation and city service status shall be declared\" "
    f"({sec('55-2505(12)')}). Sell before anyone lives in it and you answer "
    f"the three annexation questions only. Live in it and sell later and you "
    f"complete the whole form, including question 8 — whether \"any "
    f"substantial additions or alterations [have] been made without a "
    f"building permit\" — which is one more reason to keep the written "
    f"answer from step 3 of the lookup above."))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS WITH A PEN",
                   reserve=1.6)
flow += k.check_table(
    "Confirm each of these before you break ground",
    [
        ("I looked up my CITY's building-code status first, then the "
         "county's, and found (or could not find) the § 39-4117(1) "
         "permit-process document. Answer and date:",
         [("Enforcing?", 0.4), ("Office", 0.35), ("Date", 0.25)]),
        ("If no building code is enforced, I have a dated written statement "
         "from the county or city saying so. From:", [("Office", 1.0)]),
        ("I checked DOPL's location-based permit map for who issues the "
         "electrical, plumbing and HVAC permits at my address:",
         [("Electrical", 0.34), ("Plumbing", 0.33), ("HVAC", 0.33)]),
        "I am the record owner or contract purchaser of the parcel, and I "
        "understand the contractor exemption applies whether or not I "
        "occupy the house.",
        "If I am doing my own wiring: this is my primary or secondary "
        "residence, the work is noncommercial, and I know the exemption is "
        "from LICENSING only — the permit and the passed inspection are still "
        "required before the utility may energize. I have decided how "
        "temporary construction power will be handled: a licensed electrical "
        "contractor's permit, my own service inspected before the meter is "
        "set, or a generator.",
        "On each DOPL homeowner permit I will certify that I will personally "
        "perform the work and that the building is not commercial or rented "
        "to a tenant. Anyone else doing that trade's work needs the license.",
        ("For every trade I hire, I checked registration or license at "
         "edopl.idaho.gov, collected a workers' compensation certificate "
         "naming me, and will collect a signed lien waiver at every payment. "
         "Outstanding:", [("Still needed from", 1.0)]),
        ("I asked the building official in writing which IRC appendices the "
         "local ordinance adopts, and what ground snow load, frost depth and "
         "seismic category apply. Answer:",
         [("Appendices", 0.4), ("Snow / frost / seismic", 0.6)]),
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "id-permit-kit",
                       "ID.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
