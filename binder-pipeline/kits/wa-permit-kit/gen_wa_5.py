#!/usr/bin/env python3
"""WA.5 Forms & Documents Index.

Sources verified August 2026 (app.leg.wa.gov unless noted):
  RCW 19.27.095(2),(3)  application contents over $5,000; printed on the
                        permit and on the posted inspection record card
  RCW 19.27.097(1)      evidence of adequate water supply; a water right
                        APPLICATION is not sufficient proof
  RCW 90.94.020(5), 90.94.030(3)  $500 fee, reduced withdrawal caps, and the
                        recording of restrictions against title
  RCW 18.27.110(2)      the permit office must print the registration number
                        and hand you a written notice about unregistered
                        contractors
  RCW 19.28.101(5)      electrical work permit; L&I approval before the
                        utility connects
  RCW 18.104            water well construction; the well report
  WAC 246-272A-0200     on-site sewage permit application contents; 30-day
                        response; permit not to exceed five years
  WAC 51-11R-40620      energy credit options shown on the drawings
  WAC 51-11R-40240/40320/40350  the three signed test reports
  WAC 458-20-170        retail sales tax on construction for a consumer
  RCW 82.08.020(1)      the 6.5 percent state rate, before local rates
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

FORM_ID = "WA.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document a Washington owner-builder meets — what each one is, when "
    "it is needed, and which of the four agencies it comes from.")

flow.append(k.disclaimer(
    "Form names and numbers are local; the obligations behind them are not."))
flow.append(Spacer(1, 8))

DOCS = [
    ("Building permit application",
     "The main application. For any project over <b>$5,000</b> the statute "
     "fixes minimum contents, including the prime contractor's registration "
     "number — the line owner-builders have nothing to write on. Ask how your "
     "office wants it handled. <b>When:</b> after water, sewage and zoning "
     "are lined up. Completeness is what vests you.",
     "City or county building department"),
    ("Owner-builder acknowledgment",
     "There is <b>no statewide form</b>. Most jurisdictions use their own "
     "acknowledgment that you are building on your own property and are "
     "exempt from contractor registration. <b>When:</b> at application — ask "
     "for it by name before you file.",
     "City or county — local form"),
    ("Notice about unregistered contractors",
     "Not something you file — something you are <b>owed</b>. At issuance the "
     "jurisdiction must print the contractor registration number on the "
     "permit and give you written notice of the registration laws and \"<i>the "
     "potential risk and monetary liability to the homeowner for using an "
     "unregistered contractor</i>.\" If nobody hands it to you, ask.",
     "City or county, at issuance"),
    ("Evidence of adequate water supply",
     "A purveyor's letter stating the ability to serve, a water right permit, "
     "or another sufficient form. <b>A water right application is expressly "
     "not sufficient proof.</b> <b>When:</b> with the building permit "
     "application — it is a statutory precondition, not a formality.",
     "Water purveyor, or Ecology"),
    ("WRIA fee receipt and recorded restriction",
     "In 15 water resource inventory areas a new permit-exempt domestic "
     "connection carries a <b>$500 fee</b> paid to the permitting authority, "
     "a reduced withdrawal cap (950 or 3,000 gallons per day depending on the "
     "basin), and restrictions recorded against your title. <b>When:</b> at "
     "building permit. Confirm the current figure for your basin.",
     "City or county, under RCW 90.94"),
    ("Water well report (well log)",
     "Filed by the driller for a new well and constructed under chapter "
     "18.104 RCW. Outside the regulated basins, a well report consistent with "
     "that chapter is itself a recognized way to demonstrate physical and "
     "legal water availability. Keep your copy.",
     "Licensed well driller; Ecology"),
    ("On-site sewage permit application",
     "Carries the soil and site evaluation, a dimensioned site plan showing "
     "the initial <b>and reserve</b> areas, and a design bearing the "
     "designer's name, signature and stamp. The health officer must respond "
     "within 30 days; the permit may not run more than five years. "
     "<b>When:</b> start the soil evaluation first, before anything else.",
     "Local health jurisdiction"),
    ("Owner-installer permission",
     "The local health officer <b>may</b> allow the resident owner of a "
     "single-family residence to install their own system — not within 200 "
     "feet of marine water, not within 100 feet of surface water, and not "
     "where Table X standards apply. Discretionary. Get it in writing.",
     "Local health jurisdiction"),
    ("Electrical work permit",
     "A separate permit from a separate agency, bought before the work "
     "starts. Nothing may be concealed until the inspector approves it, and "
     "the utility may not connect until L&amp;I has approved. <b>When:</b> "
     "before temporary power, and again for the house.",
     "L&amp;I — or an incorporated city running its own program"),
    ("Plumbing and mechanical permits",
     "Issued locally under the Uniform Plumbing Code and the mechanical code. "
     "Doing the work yourself under a homeowner exemption does not waive "
     "them.",
     "City or county building department"),
    ("Energy credit documentation",
     "\"<i>The drawings included with the building permit application shall "
     "identify which options have been selected and the point value of each "
     "option.</i>\" Not an attachment — it belongs on the drawings. "
     "<b>When:</b> at application.",
     "You, on your plan set"),
    ("Three signed test reports",
     "Blower door (4.0 ACH50), duct leakage, and ventilation airflow "
     "verification. Each produces a written report signed by the testing "
     "party and provided to the code official. <b>When:</b> late, but book "
     "the tester early — in rural counties they set your schedule.",
     "Your testing agency, to the code official"),
    ("Critical areas, shoreline, or SEPA documents",
     "Where a wetland, stream, steep slope, geologic hazard, floodplain or "
     "shoreline designation touches your parcel, or where the project "
     "triggers environmental review. These run on their own timeline and are "
     "the most common cause of a long Washington permit. <b>When:</b> "
     "ask before you buy the land, if you still can.",
     "City or county planning"),
    ("Road approach permit",
     "From WSDOT if your driveway meets a state highway; otherwise from the "
     "county or city road authority. Establish which road you are actually "
     "connecting to before you assume.",
     "WSDOT, county, or city"),
    ("Certificate of occupancy",
     "Issued by the building department at the end, under the administrative "
     "provisions of the adopted International Residential Code. Ask early "
     "what it wants in hand — commonly every trade final including the "
     "electrical one, the energy test reports, and septic approval.",
     "City or county building department"),
]

rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)] for a, b, c in DOCS]
flow.append(k.ref_table(
    "Documents a Washington owner-builder will encounter",
    [k.cellp("Document", bold=True),
     k.cellp("What it is and when you need it", bold=True),
     k.cellp("Where it comes from", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - 1.7 * inch, 1.7 * inch]))

flow.append(Spacer(1, 8))
flow.append(k.callout(
    "One more document you will meet every month: the invoice", [
        Paragraph("Washington taxes construction <b>labor</b>, and people "
                  "arriving from states that do not are caught by it. "
                  "Building a house for your own occupancy makes you the "
                  "<b>consumer</b>. Every trade you hire directly is "
                  "therefore a \"prime contractor\" performing for a "
                  "consumer, and prime contractors \"<i>are required to "
                  "collect from consumers the retail sales tax measured by "
                  "the full contract price</i>\" — labor included, and "
                  "including permit and license fees the contractor paid and "
                  "passes on.", S["body"]),
        Paragraph("The state rate alone is <b>6.5 percent</b> and local rates "
                  "sit on top of it, so on a house this is a real line in the "
                  "budget rather than a rounding error. Look up the combined "
                  "rate for your exact site address at <b>dor.wa.gov</b>, and "
                  "budget it against every subcontractor invoice — not just "
                  "against materials. (WAC 458-20-170(4)(a); RCW "
                  "82.08.020(1))", S["body"]),
    ]))

flow.append(Spacer(1, 8))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026 at app.leg.wa.gov): application "
    "contents over $5,000, and their appearance on the permit and the posted "
    "inspection record card — RCW 19.27.095(2), (3). Evidence of an adequate "
    "water supply, and a water right application not being sufficient proof — "
    "RCW 19.27.097(1). The $500 fee, the reduced caps and recording against "
    "title — RCW 90.94.020(5)(f), RCW 90.94.030(3); both apply \"<i>until "
    "rules have been adopted that specify otherwise</i>,\" so confirm your "
    "basin. Well construction and the well report — chapter 18.104 RCW. "
    "Registration number printed on the permit and the written notice about "
    "unregistered contractors — RCW 18.27.110(2). Electrical permit, "
    "concealment, and utility connection — RCW 19.28.101(4), (5). On-site "
    "sewage application contents, the 30-day response and the five-year "
    "limit — WAC 246-272A-0200(2), (4)(a), (4)(f); owner installation — WAC "
    "246-272A-0250(2). Energy credits on the drawings — WAC 51-11R-40620. "
    "The three test reports — WAC 51-11R-40240, 51-11R-40320, 51-11R-40350. "
    "Retail sales tax on the full contract price — WAC 458-20-170(4)(a) with "
    "the 6.5 percent state rate at RCW 82.08.020(1); local rates are "
    "additional and change, so use the Department of Revenue's own lookup."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "wa-permit-kit",
                       "WA.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
