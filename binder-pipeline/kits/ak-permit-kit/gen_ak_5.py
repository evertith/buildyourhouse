#!/usr/bin/env python3
"""AK.5 Forms & Documents Index — Alaska.

In a state where most owner-builders are never issued a permit or a
certificate of occupancy, the useful version of this document is not "here are
the forms." It is "here is the file you are building instead of a
certificate," because that file is what a lender, an insurer, an appraiser and
a buyer will ask for in its place.

Verified sources:
  AS 08.18.161(11)  the for-sale notice, "on forms provided by the department"
  AS 08.18.116(b)   filing it triggers a mandatory departmental investigation
  AS 18.60.720      the statutory ceiling on state plumbing permit fees
  AS 18.60.200(b)   boiler / unfired pressure vessel installation notice
  AS 18.70.095      smoke and CO alarms in all dwelling units in the state
  AS 34.70.010      seller's disclosure statement, before a written offer
  AS 34.70.120      EXEMPTION FOR FIRST SALES — the chapter does not apply to
                    a first transfer of property that has NEVER BEEN OCCUPIED.
                    A brand-new owner-built house sold before anyone moves in
                    is outside the disclosure statute; the same house sold
                    after you live in it is inside it. Widely misstated.
  AS 34.70.090(b),(c)  negligent violation = actual damages; wilful = up to
                    treble damages, plus costs and fees
  AS 34.70.110      the chapter can be waived by written agreement
  AS 34.70.200(3)   "residential real property" = single-family, or two
                    single-family dwellings in one building
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

FORM_ID = "AK.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document an Alaska owner-builder meets — what each one is, when "
    "it is needed, and which office it comes from — and the file you build "
    "in place of the certificate most of this state never issues.")

flow.append(k.disclaimer(
    "Where a borough or city issues your permit, its own forms govern. The "
    "obligations behind them do not change."))
flow.append(Spacer(1, 8))

DOCS = [
    ("Contractor registration search",
     "Not a form — the free lookup that tells you whether anyone you are "
     "about to pay is registered, and whether a general contractor holds the "
     "<b>residential contractor endorsement</b> required for work on a one- "
     "to four-unit dwelling. <b>When:</b> before signing anything, and print "
     "the result.",
     "commerce.alaska.gov → Corporations, Business and Professional "
     "Licensing → Search Licenses"),
    ("Owner-builder notice under AS 08.18.161(11)",
     "The one form the exemption itself names. Required if you <b>advertise "
     "for sale or sell</b> the structure during construction or within two "
     "years after construction <i>begins</i>. Filing it obliges the "
     "department to investigate whether you are running a contracting "
     "business (AS 08.18.116(b)). <b>When:</b> on advertising or sale inside "
     "the window.",
     "Department of Commerce, Community, and Economic Development, on its "
     "own form"),
    ("Geotechnical investigation report",
     "Required by no Alaska permit and by every honest assessment of the "
     "ground. The document that tells you whether you are founding on "
     "ice-rich permafrost, on a liquefiable soil, or on a slope. "
     "<b>When:</b> before you buy the land if you can, before you design if "
     "you cannot.",
     "A geotechnical engineering firm"),
    ("Survey and plot plan",
     "Boundaries, the building envelope, the wastewater system <i>and its "
     "reserve area</i>, the well, and the driveway, drawn together. Required "
     "by local departments; needed everywhere else because these four "
     "compete for the same ground and the separation distances are fixed.",
     "A land surveyor registered in Alaska"),
    ("DEC homeowner installer approval",
     "Only if you will install the septic system yourself. Complete DEC's "
     "training course, apply, and pay the <b>$275</b> fee. It authorizes "
     "<b>one system within a one-year period</b> on your own owner-occupied "
     "residence. <b>When:</b> before any excavation — installing without it "
     "or a certified installer is barred outright.",
     "Alaska DEC — dec.alaska.gov → Water → Wastewater → Onsite"),
    ("24-hour construction notification",
     "For a system that needs no plan approval, this replaces the permit: "
     "notify DEC \"<i>at least one day before beginning construction</i>\" "
     "on its form. <b>When:</b> the day before you dig.",
     "Alaska DEC, on its own form"),
    ("Documentation of Construction",
     "The 90-day registration that closes out an exempt system — the form, "
     "the installer's signature or engineer's seal, <b>photographs of eight "
     "specified stages</b>, and the <b>$115</b> fee. Miss it and the fix is "
     "an engineer-sealed adequacy report on a buried system. <b>When:</b> "
     "within 90 days of completing installation.",
     "Alaska DEC — filed through its online system"),
    ("Approval to Construct, and certification of construction",
     "The plan-review path instead, for an alternative system, a permafrost "
     "site or anything needing a waiver. DEC acts within 30 days; the "
     "approval is void if the work is not finished in two years; the "
     "certification of construction and record drawings are due within 60 "
     "days of completion. Plan review to 1,500&nbsp;gpd: <b>$655</b>.",
     "Alaska DEC, on engineer-prepared submittals"),
    ("Well log",
     "The driller's record of depth, casing, static level and yield. <b>Filing "
     "it is mandatory</b> — within 45 days, with both the owner and the "
     "Department of Natural Resources — and the duty falls on \"<i>a person "
     "who constructs the well</i>,\" so it is yours if you drill it "
     "yourself. Keep your copy; it is searchable later but easiest now.",
     "Your driller, filed with Alaska DNR"),
    ("Water test results",
     "What to test for depends on your area and on what your lender wants; "
     "arsenic is a genuine concern in parts of Alaska. Ask the office "
     "regulating your wastewater system and your lender, and keep every "
     "result with its date.",
     "A certified laboratory"),
    ("Driveway or access permit",
     "For a tie-in to a state-maintained road, the Alaska Department of "
     "Transportation and Public Facilities; for a borough or city road, that "
     "government. On a private road, a recorded easement and the road "
     "association's rules instead. <b>When:</b> before you cut the "
     "approach.",
     "Alaska DOT&amp;PF — dot.alaska.gov — or your borough or city"),
    ("Floodplain development permit",
     "Required in a mapped special flood hazard area in a community that "
     "participates in the National Flood Insurance Program — <b>including "
     "communities with no building code at all</b>. Riverine and ice-jam "
     "flooding are ordinary Alaska risks.",
     "The community's floodplain administrator"),
    ("Section 404 wetlands permit or determination",
     "Alaska holds an enormous share of the country's wetlands, and filling "
     "or grading in one without authorization is a federal matter. Get a "
     "determination before you design the driveway and the pad, not after. "
     "<b>When:</b> at the site-planning stage.",
     "U.S. Army Corps of Engineers, Alaska District"),
    ("911 address assignment",
     "Free, slow, and a prerequisite for utility service, deliveries and "
     "emergency response. Request it as soon as you own the parcel.",
     "Borough or city addressing office"),
    ("Zoning or land use permit",
     "Setbacks, height, accessory buildings, waterfront and habitat "
     "setbacks. <b>This exists in Alaska boroughs that have no building code "
     "whatsoever</b>, which is why \"no building permit\" never means \"no "
     "permit.\"",
     "Borough or city planning department"),
    ("State plumbing permit",
     "Where your community is at or above <b>2,500 population</b>, the state "
     "plumbing code applies to new construction and the Department of Labor "
     "issues permits and inspects. The statutory fee ceiling is $2.00 to "
     "issue plus $1.50 per fixture — confirm what is actually charged.",
     "DOLWD Labor Standards and Safety, Mechanical Inspection — "
     "labor.alaska.gov"),
    ("Boiler or pressure vessel installation notice",
     "Required within 30 days of installation — but the department's form "
     "scopes it to \"<i>any commercial or residential (six families) "
     "site</i>,\" so <b>a detached house is outside it</b> and you file "
     "nothing. Know the rule anyway: the statute is broader than the form, "
     "and an unusual pressure vessel is worth one call. See AK.2.",
     "DOLWD Mechanical Inspection — only at six families or more"),
    ("Smoke and carbon monoxide alarm record",
     "Not a form anyone will collect — but photograph the installed alarms, "
     "keep the receipts and note the model numbers. They are required in "
     "<b>every dwelling unit in the state</b>, and this is a five-minute "
     "record that answers a question an insurer or a buyer may well ask.",
     "You, at final"),
    ("Local building permit and inspection card",
     "Only where a borough or city reviews your house. The card lists the "
     "inspections <i>your</i> job requires and governs over any sequence "
     "printed anywhere, including AK.3.",
     "Your local building department"),
    ("Certificate of occupancy",
     "Issued only by a local building department. <b>Most Alaska "
     "owner-builders never receive one</b>, and its absence is normal rather "
     "than suspicious. Note the one place it does real work: a certificate "
     "from an <b>AHFC-approved municipality</b> substitutes for the PUR-102 "
     "inspection summary. Ask whether yours is on that list.",
     "Your local building department, if you have one"),
    ("Certificate of On-Site Systems Approval (COSA)",
     "<b>Anchorage only</b>, and required at nearly every transfer of a "
     "property served by a well or septic system — the certificate lenders "
     "and older paperwork still call the HAA. A private engineer performs it: "
     "a septic adequacy test, the tank pumped within 12 months, a surveyed "
     "as-built, a well yield test, and lab tests for coliform, arsenic and "
     "nitrate. <b>When:</b> before you sell.",
     "Municipality of Anchorage On-Site Water and Wastewater Section"),
    ("PUR-102 Summary of Building Inspections",
     "The document that stands in for a certificate of occupancy on a "
     "state-financed house — signed stage by stage across the five statutory "
     "inspections, then <b>recorded</b>. It also carries the <b>Exempt "
     "Builder's Certification</b> on which an owner-builder certifies they "
     "have not built another structure in the prior two years. <b>When:</b> "
     "throughout construction; recorded at the end.",
     "An AHFC-authorized inspector; recorded with the recorder's office"),
    ("PUR-101 BEES Certification",
     "The energy half. Completed <b>only by an AHFC-authorized energy "
     "rater</b> using the state's modeling software — you cannot "
     "self-certify. <b>When:</b> book the rater during design; raters are "
     "scarce off the road system.",
     "An AHFC-authorized energy rater"),
    ("Lender's construction standard and inspection reports",
     "If you are borrowing outside AHFC, get the standard in writing before "
     "you draw and keep every draw inspection report — collectively they are "
     "the closest thing to an inspection history your house will have. On a "
     "federally-backed loan the substitute for a permit and certificate is "
     "three inspections by a qualified third party. See AK.2, Step 4.",
     "Your lender, in writing"),
    ("Seller's disclosure statement",
     "At resale. See the box below — there is a real exemption for a first "
     "sale of a never-occupied house, and the penalties for getting it wrong "
     "run to treble damages.",
     "Alaska Real Estate Commission form, from the transferor"),
]

rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in DOCS]
flow.append(k.ref_table(
    "Documents an Alaska owner-builder will encounter",
    [k.cellp("Document", bold=True),
     k.cellp("What it is and when you need it", bold=True),
     k.cellp("Where it comes from", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - 1.7 * inch, 1.7 * inch]))

# ---------------------------------------------------------------- disclosure
flow.append(Spacer(1, 8))
flow += k.h2_tight("THE DISCLOSURE RULE AT RESALE — AND ITS REAL EXEMPTION")
flow.append(k.body(
    "Alaska requires a seller of residential real property to deliver a "
    "completed written disclosure statement, on the Real Estate Commission's "
    "form, <b>before the buyer makes a written offer</b>. Guides state that "
    "much and stop. Two sections later there is an exemption that applies to "
    "a great many owner-builders and almost never gets printed."))

flow.append(k.callout_long("First sale, never occupied — and what happens if you move in", [
    Paragraph("\"<i>This chapter does not apply to the transfer of an "
              "interest in residential real property if the transfer is the "
              "<b>first transfer</b> of the property and if the property has "
              "<b>never been occupied</b>.</i>\" (AS 34.70.120)", S["body"]),
    Paragraph("Both conditions, together. Build a house and sell it before "
              "anyone lives in it and the disclosure chapter does not reach "
              "the sale. Live in it for a winter and sell it and the chapter "
              "applies in full — which is the far commoner owner-builder "
              "story, and the one worth planning for. Note how this "
              "interacts with <b>AK.1</b>: the same house sold early enough "
              "to escape the disclosure statute is a house sold inside the "
              "two-year window that obliges you to file the "
              "AS 08.18.161(11) notice. The two rules pull in opposite "
              "directions, and knowing that before you list is worth more "
              "than knowing it after.", S["body"]),
    Paragraph("Where the chapter does apply, the penalties are not nominal. "
              "A person who <b>negligently</b> violates it \"<i>is liable to "
              "the transferee for the amount of the actual damages</i>\"; a "
              "person who \"<i>wilfully</i>\" violates it — the statute's own "
              "spelling — is liable \"<i>for up "
              "to <b>three times</b> the actual damages</i>,\" plus costs and "
              "attorney fees. The chapter can also be waived by written "
              "agreement between the parties (AS 34.70.110) — which is a "
              "thing buyers sometimes propose and sellers should think about "
              "carefully rather than sign.", S["body"]),
    Paragraph("None of this asks you to flag the house as owner-built. It "
              "asks you to disclose what you <b>know</b> about its "
              "condition. An owner-builder knows more about the house than "
              "any other seller in the market — which is exactly why the "
              "build record in the next section is worth keeping.",
              S["body"]),
]))
flow.append(k.cite(
    "AS 34.70.010; AS 34.70.050; AS 34.70.090(b), (c); AS 34.70.110; "
    "AS 34.70.120; AS 34.70.200(3) — \"residential real property\" means "
    "property whose primary purpose is a single-family dwelling, or two "
    "single-family dwellings in one building. Read at akleg.gov, August "
    "2026."))

# ---------------------------------------------------------------- the file
flow += k.h2_tight("THE FILE YOU BUILD INSTEAD OF A CERTIFICATE")
flow.append(k.body(
    "In most of the country the certificate of occupancy is the artifact "
    "that says a house was built properly. Most Alaska owner-builders will "
    "never hold one, and there is nothing wrong with that — but something "
    "has to do that job when the appraiser, the underwriter or the buyer "
    "arrives. What does the job is a file you assemble as you go, and it is "
    "almost impossible to assemble afterwards."))
flow.append(k.body(
    "Keep it in one place, keep two copies, and put one somewhere that will "
    "survive the house. The single highest-value item on the list is the "
    "cheapest: <b>photographs of every wall, floor and ceiling cavity taken "
    "the day before it was closed up</b>, with the date intact."))

flow += k.check_table("The build record — assemble as you go", [
    "Dated photographs of every stage, especially every cavity before it was "
    "covered — framing, insulation, air barrier, plumbing, wiring",
    "The AK.3 stage log, filled in as it happened rather than from memory",
    ("Geotechnical report and the foundation design that responds to it",
     [("Filed:", 1.0)]),
    ("Wastewater approval, the as-built, and the certification of completion",
     [("Filed:", 1.0)]),
    ("Well log and every water test result, with dates",
     [("Filed:", 1.0)]),
    "Structural engineer's sealed drawings and calculations",
    "Energy documentation: the rating or model, the air-sealing approach, and "
    "what the ventilation system is",
    "Every state or local permit, inspection report and correction notice, "
    "including the ones you passed",
    "Lender's draw inspection reports, in order",
    "Manufacturer documentation and warranties for the heating system, the "
    "ventilation equipment, the windows and the roof",
    "Receipts and model numbers for the smoke and carbon monoxide alarms",
    ("Contractor registration printouts for everyone you paid, with the "
     "dates you checked them", [("Filed:", 1.0)]),
], notes_header="Where it is kept")

flow.append(Spacer(1, 10))
flow.append(k.sources_table([
    ("The exemption's own notice form, and the investigation that filing it "
     "triggers", "AS 08.18.161(11); AS 08.18.116(b)"),
    ("Residential contractor endorsement is required of a general contractor "
     "for one- to four-unit residential work", "AS 08.18.025(a)"),
    ("State plumbing permits and the statutory fee ceiling of $2.00 to issue "
     "plus $1.50 per fixture", "8 AAC 63.020; AS 18.60.720(a)"),
    ("The boiler installation notice is scoped by the department's own form "
     "to commercial and six-family-or-larger residential sites — a detached "
     "house files nothing", "AS 18.60.200(b); DOLWD form"),
    ("Smoke and carbon monoxide alarms in all dwelling units in the state",
     "AS 18.70.095"),
    ("Seller's disclosure statement before a written offer, on the Real "
     "Estate Commission's form", "AS 34.70.010; AS 34.70.050"),
    ("The chapter does not apply to a first transfer of property that has "
     "never been occupied", "AS 34.70.120"),
    ("Negligent violation: actual damages. Wilful: up to treble damages plus "
     "costs and fees. The chapter may be waived in writing",
     "AS 34.70.090(b), (c); AS 34.70.110"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ak-permit-kit",
                       "AK.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
