#!/usr/bin/env python3
"""PA.2 Permit Application Checklist.

The center of gravity in this document is not the application form — there
isn't a state one — but the Pennsylvania amendments to the model codes.

Pennsylvania adopts the 2021 I-Codes and then changes a great many of them,
in two different places: the Department's regulation at 34 Pa. Code § 403.21,
and the Act itself at 35 P.S. § 7210.304, where the General Assembly wrote
several technical requirements directly into statute in Act 1 of 2011. An
owner-builder working from a purchased code book has no way to know that, and
three of the amendments are expensive to discover late — wall bracing rolled
back to the 2006 IRC, a gypsum membrane required under most engineered floors,
and an energy table the Commonwealth rewrote rather than adopted.

The document therefore prints the amendments as a table of DIFFERENCES from
the book on the reader's desk, not as a restatement of the code.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from reportlab.lib.units import inch
from reportlab.platypus import KeepTogether, Paragraph, Spacer

import kit as k

S = k.S
CW = k.CW

FORM_ID = "PA.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Before You File"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What goes in the application, how long the reviewer has, and the "
    "Pennsylvania amendments that make the code book on your desk wrong in "
    "places that matter.")
flow.append(k.disclaimer())

flow.append(k.body(
    "Pennsylvania publishes no statewide building permit application form. "
    "The form is the municipality's or the third-party agency's, and it "
    "varies. What does not vary is <b>what the regulation entitles the "
    "reviewer to demand</b>, and that list is short enough to work through "
    "before you go anywhere near a counter."))

# ------------------------------------------------------------ what to file
flow += k.h2_tight("WHAT THE APPLICATION MUST CARRY", 2.0)
rows = [
    [k.cellp("<b>Construction documents</b>"),
     k.cellp("Plans and specifications, submitted to the building code "
             "official. The official may waive them where the nature of the "
             "work does not require review — which will not be the case for "
             "a house."),
     k.cellp("§&nbsp;403.62a(b), (c)")],
    [k.cellp("<b>A site plan</b>"),
     k.cellp("Showing “the size and location of the new construction and "
             "existing structures on the site and the structures' distance "
             "from lot lines.” This is a code requirement in its own right, "
             "not a courtesy sketch."),
     k.cellp("§&nbsp;403.62a(e)")],
    [k.cellp("<b>Every other permit or approval</b>"),
     k.cellp("All other permits or approvals related to the construction. In "
             "practice this is where your sewage permit, zoning approval, "
             "driveway permit and stormwater approval get collected."),
     k.cellp("§&nbsp;403.62a(b)")],
    [k.cellp("<b>Flood hazard information</b>"),
     k.cellp("If the lot is in a mapped flood hazard area: the flood hazard "
             "and floodway boundaries, flood zones, the design flood "
             "elevation, and the proposed lowest floor elevation including "
             "basement. In a Zone AO shallow-flooding area, the height above "
             "highest adjacent grade as well."),
     k.cellp("§&nbsp;403.62a(d)")],
]
flow.append(k.ref_table(
    "34 Pa. Code § 403.62a — the residential permit application",
    [k.cellp("Item", bold=True), k.cellp("What the regulation requires",
                                         bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.5 * inch, CW - 2.85 * inch, 1.35 * inch]))
flow.append(Spacer(1, 6))
flow.append(k.cite(
    "Note the section number. §&nbsp;403.62a governs <b>residential</b> "
    "permit applications; §&nbsp;403.42a is the near-identical commercial "
    "section, and the two are easy to cite in place of one another. The "
    "residential permit and inspection sections are §§&nbsp;403.61—403.66."))

# ------------------------------------------------------------- the clock
flow += k.h2_tight("THE REVIEW CLOCK — AND HOW TO CUT IT TO FIVE DAYS", 2.0)
flow.append(k.body(
    "Pennsylvania puts the reviewer on a statutory clock and attaches a real "
    "consequence to missing it. For a one- or two-family dwelling the code "
    "official must grant or deny the application, in whole or in part, "
    "<b>within 15 business days of the filing date</b> — and if he fails to "
    "act within that time, “<b>the application shall be deemed approved</b>.”"))
flow.append(k.callout(
    "The five-day route is worth more than it costs", [
        Paragraph("The same sentence sets a much shorter clock on one "
                  "condition: where “the drawings have been prepared by "
                  "design professionals who are licensed or registered under "
                  "the laws and regulations of this Commonwealth <b>and the "
                  "application contains a certification by the licensed or "
                  "registered design professional that the plans meet the "
                  "applicable standards</b> of the Uniform Construction Code "
                  "and ordinance as appropriate,” the deadline is "
                  "<b>five business days</b>.", S["body"]),
        Paragraph("Pennsylvania does not otherwise require a house to be "
                  "designed by an architect or engineer. So the seal is "
                  "optional — but buying one converts a three-week review "
                  "into a one-week review, and the certification language "
                  "has to be on the application for the short clock to run. "
                  "If you are paying a design professional anyway, ask "
                  "specifically for that certification.", S["body"]),
    ]))
flow.append(k.body(
    "Two more timing facts from the same section. Once the plan is approved, "
    "the code administrator “shall issue a building permit <b>immediately "
    "upon receipt of all other required permits or approvals</b> related to "
    "the construction” — so plan approval and permit issuance are separate "
    "events, and the gap between them is filled by your septic, driveway and "
    "zoning paperwork. And any revision to approved plans “shall necessitate "
    "an additional plan review prior to the issuing of the building "
    "permit.”"))

flow.append(k.callout(
    "Ask for the list — then verify it yourself", [
        Paragraph("Section 7210.502(a)(1) requires that “<b>the municipality "
                  "shall also provide a list of all other required permits "
                  "necessary prior to issuance of the building permit</b>.” "
                  "Ask for it in writing; it is the fastest way to discover "
                  "the approvals your particular lot triggers.", S["body"]),
        Paragraph("Then read the next sentence, which is the reason PA.4 "
                  "exists: “<b>The municipality will not be liable for the "
                  "completeness of any list.</b>” A missing item on that list "
                  "is still your problem, and still stops your permit.",
                  S["body"]),
    ]))

# --------------------------------------------------------- code editions
flow += k.h2_tight("WHAT CODE YOU ARE ACTUALLY BUILDING TO", 2.0)
rows = [
    [k.cellp("One- and two-family dwellings"),
     k.cellp("<b>2021 International Residential Code</b>, with the "
             "Pennsylvania exclusions and modifications below"),
     k.cellp("§&nbsp;403.21(a)(7)")],
    [k.cellp("Energy"),
     k.cellp("<b>2021 International Energy Conservation Code</b> — but with "
             "Pennsylvania's own replacement envelope tables"),
     k.cellp("§&nbsp;403.21(a)(9)")],
    [k.cellp("Electrical"),
     k.cellp("The <b>electrical chapters of the 2021 IRC</b> (Chapters "
             "34—43). Pennsylvania does not adopt NFPA 70 by reference at "
             "all — see below"),
     k.cellp("§&nbsp;403.21(a)(7)")],
    [k.cellp("Plumbing"),
     k.cellp("IRC plumbing provisions for a dwelling; the 2021 "
             "International Plumbing Code otherwise — <b>except in Allegheny "
             "County</b>, which runs its own plumbing code"),
     k.cellp("§&nbsp;403.21(a)(6)")],
    [k.cellp("Mechanical and fuel gas"),
     k.cellp("2021 International Mechanical Code and 2021 International Fuel "
             "Gas Code"),
     k.cellp("§&nbsp;403.21(a)(3), (4)")],
    [k.cellp("Wall bracing"),
     k.cellp("<b>The 2006 IRC.</b> Not a typo — see the amendments table"),
     k.cellp("35 P.S.<br/>§&nbsp;7210.304(i)")],
]
flow.append(k.ref_table(
    "Editions in force — effective 1 January 2026",
    [k.cellp("System", bold=True), k.cellp("Adopted edition", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.6 * inch, CW - 2.9 * inch, 1.3 * inch]))
flow.append(Spacer(1, 6))
flow.append(k.callout(
    "If you check this on L&amp;I's website, you may be told 2018", [
        Paragraph("The 2021 codes were adopted by a regulation published at "
                  "55&nbsp;Pa.B. 7701, amending 34 Pa. Code §&nbsp;403.21 on "
                  "7 November 2025, effective 1 January 2026. As this kit "
                  "went to press the Department's own Uniform Construction "
                  "Code home page still described the 2018 I-Code series with "
                  "an effective date of 14 February 2022 — the previous "
                  "cycle. <b>The regulation governs, not the web page.</b> "
                  "Read 34 Pa. Code §&nbsp;403.21 at pacodeandbulletin.gov "
                  "and check the Pennsylvania Bulletin line at the top of the "
                  "chapter for how current it is.", S["body"]),
        Paragraph("One transitional rule matters if your project straddles "
                  "the date: under §&nbsp;403.1(a)(2), work for which a "
                  "design or construction contract was executed before the "
                  "effective date of the amendment complies with the codes in "
                  "effect when that contract was signed.", S["body"]),
    ]))

# ------------------------------------------------------------ amendments
flow += k.h2_tight("THE PENNSYLVANIA AMENDMENTS THAT CHANGE THE BUILDING",
                   2.2)
flow.append(k.body(
    "These are differences from the printed model code, not restatements of "
    "it. Each one is a place where building to the book fails inspection, or "
    "where the book demands something Pennsylvania does not."))
rows = [
    [k.cellp("<b>Wall bracing</b>"),
     k.cellp("The 2009 IRC bracing provisions “<b>and successor "
             "provisions</b>” are excluded from the UCC, and the wall bracing "
             "requirements of <b>2006 IRC sections R602.10—R602.11.3</b> are "
             "what Pennsylvania enforces. Your 2021 code book's bracing "
             "chapter is not the law here."),
     k.cellp("35 P.S.<br/>§&nbsp;7210.304(i)")],
    [k.cellp("<b>Floor membrane</b>"),
     k.cellp("A floor assembly not required to be fire-resistance rated must "
             "carry <b>1/2-inch gypsum wallboard, a 5/8-inch wood structural "
             "panel, or equivalent on the underside of the floor framing</b>. "
             "Exceptions: space below is sprinklered; a crawl space not used "
             "for storage or fuel-fired appliances; up to 80 sq ft per story "
             "left unprotected if fireblocked at its perimeter; and "
             "dimension lumber or structural composite lumber of 2×10 nominal "
             "or greater. <b>This is the I-joist rule</b>, and it is in the "
             "statute rather than the code book."),
     k.cellp("35 P.S.<br/>§&nbsp;7210.304(h)")],
    [k.cellp("<b>No sprinkler mandate</b>"),
     k.cellp("IRC §&nbsp;R313.2 “and any successor triennial revisions” is "
             "excluded from the Act. Pennsylvania does not require automatic "
             "fire sprinklers in a one- or two-family dwelling. A builder "
             "must still <b>offer</b> the option in writing at or before a "
             "purchase contract, with cost information — relevant if you "
             "later build to sell."),
     k.cellp("35 P.S.<br/>§&nbsp;7210.304(g)")],
    [k.cellp("<b>Stairs are steeper here</b>"),
     k.cellp("Maximum riser <b>8¼ inches</b>, minimum tread <b>9 inches</b> — "
             "both more permissive than the model code. Riser variation "
             "within a flight no more than 3/8 inch; greatest tread depth no "
             "more than 3/8 inch over the smallest; minimum 3 ft clear width; "
             "6 ft 8 in headroom; handrails may project 3½ inches each side."),
     k.cellp("34 Pa. Code<br/>§&nbsp;403.21<br/>(a)(7)(ii)")],
    [k.cellp("<b>Vapor retarder</b>"),
     k.cellp("The under-slab vapor retarder requirement is reduced from the "
             "2021 IRC's 10-mil ASTM E1745 Class A sheet to "
             "<b>6 mil</b>."),
     k.cellp("34 Pa. Code<br/>§&nbsp;403.21<br/>(a)(7)(iv)(E)")],
    [k.cellp("<b>No radon provisions</b>"),
     k.cellp("Appendices to the adopted codes “are not adopted” except for "
             "the existing-building code and two IBC appendices. "
             "<b>IRC Appendix F, radon-resistant construction, is therefore "
             "not part of the UCC</b> — no passive radon system is required "
             "anywhere in Pennsylvania by the building code, in a state with "
             "high radon. Building one is a choice, and a cheap one before "
             "the slab goes down."),
     k.cellp("34 Pa. Code<br/>§&nbsp;403.21(c)")],
    [k.cellp("<b>Three receptacle rules<br/>rolled back</b>"),
     k.cellp("Pennsylvania excludes three 2021 IRC electrical sections "
             "<b>and puts older text back in their place</b> — see the "
             "electrical table below. Island countertops, tub and shower "
             "space, and foyers are all governed by earlier editions than "
             "the book your electrician is working from."),
     k.cellp("34 Pa. Code<br/>§&nbsp;403.21<br/>(a)(7)(iii), (vi),<br/>(viii)")],
    [k.cellp("<b>Other exclusions</b>"),
     k.cellp("Also excluded: R311.7.4 (stair walkline), R325.5 (openness), "
             "R703.7 (exterior plaster and stucco), R806.2 (minimum "
             "ventilation area) and R1005.8 (chimney insulation shield). "
             "R314.4 (smoke alarm interconnection) is excluded as well, and "
             "for alterations, repairs and additions the regulation "
             "substitutes non-interconnected battery-operated alarms — "
             "confirm with your official what he expects on new work."),
     k.cellp("34 Pa. Code<br/>§&nbsp;403.21<br/>(a)(7)(i), (iii)")],
]
flow.append(k.ref_table(
    "Differences between the printed 2021 IRC and Pennsylvania law",
    [k.cellp("Subject", bold=True), k.cellp("What Pennsylvania actually "
                                            "requires", bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.35 * inch, CW - 2.85 * inch, 1.5 * inch]))
flow.append(Spacer(1, 6))
flow.append(k.cite(
    "Two sources, deliberately. The Department amends the codes by "
    "regulation at 34 Pa. Code § 403.21; the General Assembly wrote several "
    "technical rules directly into the Act itself in 2011, and those live at "
    "35 P.S. § 7210.304 where nobody looks for them. Wall bracing, the floor "
    "membrane and the sprinkler exclusion are all statutory."))

# ---------------------------------------------------------------- energy
flow += k.h2_tight("ENERGY — PENNSYLVANIA REWROTE THE TABLE", 2.2)
flow.append(k.body(
    "Pennsylvania did not adopt the 2021 IECC envelope tables. It replaced "
    "them. The values below are Pennsylvania's own Table R402.1.3 as printed "
    "in the regulation, for the three climate zones found in the "
    "Commonwealth. <b>Confirm your zone with your code official</b> — under "
    "34 Pa. Code §&nbsp;403.103(d) it is the building code official who "
    "determines the climatic and geographic design criteria in IRC Table "
    "R301.2(1)."))
rows = [
    [k.cellp("Ceiling"), k.cellp("R-49", center=True),
     k.cellp("R-49", center=True), k.cellp("R-49", center=True)],
    [k.cellp("Wood frame wall"),
     k.cellp("R-20, or 13+5", center=True),
     k.cellp("R-23, or 13+7.5,<br/>or 20+3.8", center=True),
     k.cellp("R-20+5, or 13+10", center=True)],
    [k.cellp("Floor"), k.cellp("R-19", center=True),
     k.cellp("R-30", center=True), k.cellp("R-30", center=True)],
    [k.cellp("Basement wall"), k.cellp("10/13", center=True),
     k.cellp("15/19", center=True), k.cellp("15/19", center=True)],
    [k.cellp("Crawl space wall"), k.cellp("10/13", center=True),
     k.cellp("15/19", center=True), k.cellp("15/19", center=True)],
    [k.cellp("Slab R-value &amp; depth"),
     k.cellp("R-10, 2 ft", center=True),
     k.cellp("R-10, 4 ft<br/>or R-15, 3 ft", center=True),
     k.cellp("R-10, 4 ft", center=True)],
    [k.cellp("Window U-factor"), k.cellp("0.32", center=True),
     k.cellp("0.30", center=True), k.cellp("0.30", center=True)],
    [k.cellp("Glazed SHGC"), k.cellp("0.40", center=True),
     k.cellp("NR", center=True), k.cellp("NR", center=True)],
    [k.cellp("<b>Blower door</b>"), k.cellp("<b>3.0 ACH50</b>", center=True),
     k.cellp("<b>3.0 ACH50</b>", center=True),
     k.cellp("<b>3.0 ACH50</b>", center=True)],
]

# The envelope table is the single most-consulted page in the kit and it is
# only ten short rows. Left to split it strands the header plus one row on a
# page of its own, which reads as a broken table rather than a continuation.
# KeepTogether moves the whole thing instead; it is short enough that the
# cost is never more than a partial page above it.
flow.append(KeepTogether(k.ref_table(
    "Pennsylvania Table R402.1.3 — minimum insulation and fenestration",
    [k.cellp("Component", bold=True), k.cellp("Zone 4", bold=True),
     k.cellp("Zone 5", bold=True), k.cellp("Zone 6", bold=True)],
    rows, [1.85 * inch, (CW - 1.85 * inch) / 3, (CW - 1.85 * inch) / 3,
           (CW - 1.85 * inch) / 3])))
flow.append(Spacer(1, 6))
flow.append(k.cite(
    "34 Pa. Code § 403.21(a)(9)(vi)(D), Table R402.1.3. Skylights are "
    "U-0.55 in all three zones. Two-number entries "
    "follow the table's own footnotes: “13+5” means R-13 cavity plus R-5 "
    "continuous insulation; “10/13” means R-10 continuous <i>or</i> R-13 "
    "cavity, and “15/19” may alternatively be met with R-13 cavity plus R-5 "
    "continuous. A floor may alternatively be insulated to fill the framing "
    "cavity at not less than R-19. Zone 4 values are the “except Marine” "
    "row. The air leakage limit is 2021 IECC R402.4.1.2, which Pennsylvania "
    "did not amend: 3 air changes per hour in Climate Zones 3 through 8, "
    "which is all of Pennsylvania."))
flow.append(Spacer(1, 4))
flow.append(k.callout(
    "Three energy details worth money", [
        Paragraph("<b>The ceiling stayed at R-49.</b> The unamended 2021 "
                  "IECC would have required R-60 in these zones; "
                  "Pennsylvania's replacement table keeps R-49. Do not let a "
                  "supplier upsell you to a national number your code does "
                  "not ask for — but do not assume the reverse either, since "
                  "a municipality may adopt a stricter ordinance.",
                  S["body"]),
        Paragraph("<b>The blower door is real and it is 3.0.</b> Any guide "
                  "quoting 5.0 or 4.0 ACH50 for Pennsylvania is repeating a "
                  "figure from an older code cycle. Air sealing to 5.0 and "
                  "testing at 3.0 is a failed test and a scramble.",
                  S["body"]),
        Paragraph("<b>Duct leakage testing has two Pennsylvania "
                  "exceptions.</b> Under the amended R403.3.5 no duct "
                  "air-leakage test is required where the ducts and air "
                  "handlers are entirely within the building thermal "
                  "envelope, or for ducts serving heat or energy recovery "
                  "ventilators not integrated with the heating or cooling "
                  "ducts. Designing the ducts inside the envelope removes a "
                  "test and a failure mode.", S["body"]),
    ]))
flow.append(k.body(
    "For compliance you may use REScheck, or a Pennsylvania-specific "
    "prescriptive package called <b>“Pennsylvania's Alternative Residential "
    "Energy Provisions”</b>, both named in the regulation at 34 Pa. Code "
    "§&nbsp;403.21(d)(1). The performance and energy-rating-index paths "
    "exist but Pennsylvania has excluded and rewritten large parts of them, "
    "so the prescriptive route is the predictable one for an owner-builder."))

# ------------------------------------------------------------ electrical
flow += k.h2_tight("ELECTRICAL — THERE IS NO NEC EDITION TO LOOK UP", 2.0)
flow.append(k.body(
    "This surprises electricians as often as owners. <b>The Pennsylvania UCC "
    "adopts no edition of NFPA 70, the National Electrical Code, for "
    "residential work.</b> The phrases “NFPA 70” and “National Electrical "
    "Code” do not appear in 34 Pa. Code Chapter 403 at all. What governs the "
    "wiring in a Pennsylvania house is <b>Chapters 34 through 43 of the 2021 "
    "IRC</b> (sections E3401—E4304). Every Pennsylvania electrical amendment "
    "is written in those E-section numbers, which is the proof of it. So if "
    "a guide tells you Pennsylvania is “on the 2020 NEC,” treat that as "
    "background trivia rather than a citation — there is no such adoption to "
    "point at, and quoting an NEC article number to a Pennsylvania inspector "
    "will not settle an argument."))
flow.append(k.body(
    "That matters less than the next point, which is where Pennsylvania "
    "actually catches people. The Commonwealth did not simply delete three "
    "receptacle rules — it <b>replaced them with the text of earlier "
    "editions</b>. Everything else in Chapters 34—43, including all the AFCI "
    "and GFCI requirements and service sizing, is the 2021 IRC as "
    "published."))
rows = [
    [k.cellp("<b>E3901.4.2</b><br/>Island and peninsula<br/>countertop spaces"),
     k.cellp("2021 text excluded. The <b>2018 IRC</b> version governs. The "
             "2021 edition substantially rewrote island receptacle rules; "
             "Pennsylvania rejected the rewrite."),
     k.cellp("§&nbsp;403.21(a)(7)<br/>(iii)(KK); (viii)(J)")],
    [k.cellp("<b>E4002.11</b><br/>Bathtub and<br/>shower space"),
     k.cellp("2021 text excluded. The <b>2018 IRC</b> version governs."),
     k.cellp("§&nbsp;403.21(a)(7)<br/>(iii)(MM); (viii)(K)")],
    [k.cellp("<b>E3901.11</b><br/>Foyers"),
     k.cellp("2021 text excluded. The <b>2015 IRC</b> version governs, "
             "further modified so the trigger reads <b>6 feet</b> rather "
             "than 3 feet, with a minimum of one receptacle."),
     k.cellp("§&nbsp;403.21(a)(7)<br/>(iii)(LL); (vi)(O)")],
    [k.cellp("<b>E4004.5</b><br/>Means of support"),
     k.cellp("Adopted as modified — the internal cross-reference to "
             "E3906.12 is replaced with E3905.6.3."),
     k.cellp("§&nbsp;403.21(a)(7)<br/>(iv)(NN)")],
]
flow.append(k.ref_table(
    "The four electrical sections Pennsylvania changed",
    [k.cellp("Section", bold=True), k.cellp("What governs instead",
                                            bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.75 * inch, CW - 3.35 * inch, 1.6 * inch]))
flow.append(Spacer(1, 6))
flow.append(k.cite(
    "Mark these four in your code book before the rough-in. Island "
    "countertop receptacles, tub and shower clearance and foyer receptacles "
    "are three of the most routinely inspected residential electrical items, "
    "and all three are places where a current 2021 IRC — and current "
    "training — will give a Pennsylvania electrician the wrong answer."))

# ---------------------------------------------------------- permit life
flow += k.h2_tight("ONCE THE PERMIT IS ISSUED", 1.8)
flow.append(k.bullet(
    "<b>180 days to start.</b> A permit becomes invalid unless authorized "
    "work begins within 180 days of issuance, or if work is suspended or "
    "abandoned for 180 days after commencing. Extensions must be requested "
    "in writing and granted in writing (34 Pa. Code § 403.63(g))."))
flow.append(k.bullet(
    "<b>Five years, maximum.</b> “A permit may be valid for no more than 5 "
    "years from its issue date” — the outer limit on a slow "
    "owner-built project (§ 403.63(g))."))
flow.append(k.bullet(
    "<b>Keep the permit and the stamped plans on site.</b> The permit holder "
    "keeps a copy of the permit on the work site until construction is "
    "complete, and a copy of the reviewed construction documents open to "
    "inspection (§§ 403.63(c), (h))."))
flow.append(k.bullet(
    "<b>A foundation-only permit is available.</b> The official may issue a "
    "permit for foundations before the documents for the whole building are "
    "submitted — useful for a long build, though it is expressly no "
    "assurance the rest will be approved (§ 403.63(e))."))
flow.append(k.bullet(
    "<b>Changes require a new review.</b> Work must be installed per the "
    "approved documents; a revised set must be submitted and approved for "
    "changes made during construction (§ 403.63(j))."))

flow.append(Spacer(1, 4))
flow += k.check_table(
    "Before you file", [
        ("Confirmed who reviews and inspects — municipal office or "
         "third-party agency (PA.1)", [("Name", 1.0)]),
        ("Obtained the municipality's written list of all other required "
         "permits", [("Date requested", 0.5), ("Received", 0.5)]),
        "Site plan drawn showing all structures and their distances from "
        "every lot line",
        ("Sewage permit issued, or public sewer connection confirmed "
         "(see PA.4)", [("Permit no.", 1.0)]),
        ("Driveway: highway occupancy permit applied for if the lot touches "
         "a state highway", [("Applied", 0.5), ("Issued", 0.5)]),
        "Zoning approval obtained from the municipality",
        "Flood hazard status checked; elevation data prepared if the lot is "
        "in a mapped area",
        ("Climate zone confirmed with the code official, and the energy "
         "compliance path chosen", [("Zone", 0.4), ("Path", 0.6)]),
        "Plans checked against the Pennsylvania amendments above — "
        "especially wall bracing and the floor membrane",
        "Decided whether to obtain a design professional's certification "
        "for the five-business-day review",
    ], notes_header="Notes")

# --------------------------------------------------------------- sources
flow.append(Spacer(1, 4))
flow.append(k.sources_table([
    ("Residential permit application contents; site plan; flood data",
     "34 Pa. Code § 403.62a"),
    ("15 business days, or 5 with a design professional's certification",
     "35 P.S. § 7210.502(a)(1); 34 Pa. Code § 403.63(a)"),
    ("Failure to act means the application is deemed approved",
     "35 P.S. § 7210.502(a)(3)"),
    ("Municipality must list other required permits; not liable for the list",
     "35 P.S. § 7210.502(a)(1)"),
    ("2021 I-Codes adopted; effective 1 January 2026",
     "34 Pa. Code § 403.21; 55 Pa.B. 7701"),
    ("Contract signed before the amendment keeps the older codes",
     "34 Pa. Code § 403.1(a)(2)"),
    ("Appendices not adopted — no IRC Appendix F radon requirement",
     "34 Pa. Code § 403.21(c)"),
    ("Stair riser and tread; struck IRC provisions; vapor retarder",
     "34 Pa. Code § 403.21(a)(7)"),
    ("Wall bracing enforced from the 2006 IRC",
     "35 P.S. § 7210.304(i)"),
    ("Floor membrane requirement and its exceptions",
     "35 P.S. § 7210.304(h)"),
    ("Residential sprinklers excluded; builder's offer duty",
     "35 P.S. § 7210.304(g)"),
    ("Pennsylvania's replacement energy tables",
     "34 Pa. Code § 403.21(a)(9)(vi)"),
    ("Compliance via REScheck or PA Alternative Residential Energy Provisions",
     "34 Pa. Code § 403.21(d)(1)"),
    ("Code official sets the climatic and geographic design criteria",
     "34 Pa. Code § 403.103(d)"),
    ("Permit life: 180 days, 5 years; foundation-only permits; revisions",
     "34 Pa. Code § 403.63"),
]))
flow.append(Spacer(1, 6))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "pa-permit-kit",
                       "PA.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
