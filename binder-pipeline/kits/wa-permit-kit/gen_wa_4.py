#!/usr/bin/env python3
"""WA.4 Where to File Directory.

Washington has a statewide building code but no statewide permit counter, and
— unusually — the trades are split across agencies: building, plumbing and
mechanical are local; electrical is the Department of Labor & Industries
unless an incorporated city or town runs its own program; on-site sewage is
the local health jurisdiction; water availability runs through Ecology or a
purveyor.

Deliberately prints agency DOMAINS and lookup routes rather than deep links or
phone numbers. Deep links inside county sites proved unstable when checked in
August 2026 — several returned a 200 for an unrelated page — and direct-dial
numbers change often enough that a printed number is a liability. Every block
has a rule for the reader to write what they confirmed.

Domains verified live (HTTP reachable), August 2026:
  lni.wa.gov, secure.lni.wa.gov/verify/, sbcc.wa.gov, ecology.wa.gov,
  doh.wa.gov, dor.wa.gov, wsdot.wa.gov, dnr.wa.gov, app.leg.wa.gov,
  wabo.org, mrsc.org, kingcounty.gov, piercecountywa.gov,
  snohomishcountywa.gov, spokanecounty.gov, clark.wa.gov,
  thurstoncountywa.gov, kitsap.gov, yakimacounty.us, whatcomcounty.us,
  bentoncountywa.gov, skagitcounty.net, islandcountywa.gov,
  lewiscountywa.gov, franklincountywa.gov, tpchd.org, snohd.org, srhd.org,
  kitsappublichealth.org, bfhd.wa.gov
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

FORM_ID = "WA.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The offices a Washington owner-builder deals with — there are more of "
    "them than in most states — how to find each one for your parcel, and a "
    "page to write down what you confirmed.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- who issues
flow += k.h2_tight("FOUR AGENCIES, ONE HOUSE")
flow.append(k.body(
    "The building code is statewide; permits are not issued by the State — "
    "except the electrical one, which usually is. That inversion is the whole "
    "reason this document exists. Before you gather a single form, settle "
    "which four offices are yours."))

who_rows = [
    [k.cellp("<b>Building, plumbing, mechanical</b>"),
     k.cellp("City or town if your parcel is inside the limits; otherwise the "
             "county. This office issues the permit, reviews the plans, and "
             "calls most of your inspections."),
     k.cellp("City or county")],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("Labor &amp; Industries, statewide — unless you are inside an "
             "incorporated city or town that runs its own electrical "
             "program, in which case that city does. Counties cannot."),
     k.cellp("L&amp;I or city")],
    [k.cellp("<b>On-site sewage, and often well siting</b>"),
     k.cellp("Your local health jurisdiction: a county health department, or "
             "a multi-county health district. Frequently not the same agency "
             "as your building department, and often not in the same "
             "building."),
     k.cellp("Local health")],
    [k.cellp("<b>Water availability</b>"),
     k.cellp("A water purveyor's letter, an Ecology water right, or a "
             "permit-exempt well under the rules for your water resource "
             "inventory area. Your building department will not issue without "
             "this evidence."),
     k.cellp("Purveyor or Ecology")],
]
flow.append(k.ref_table(
    "Who issues what",
    [k.cellp("Permit or approval", bold=True),
     k.cellp("Who handles it", bold=True), k.cellp("Agency", bold=True)],
    who_rows, [1.85 * inch, CW - 1.85 * inch - 1.25 * inch, 1.25 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout("Settle the electrical question first", [
    Paragraph("Two calls, ten minutes, and it decides who you deal with for "
              "the rest of the job. <b>First</b>, confirm whether your parcel "
              "is inside city or town limits or in unincorporated county — "
              "your county assessor's parcel lookup will tell you. "
              "<b>Second</b>, if you are inside a city, ask that city "
              "directly whether it runs its own electrical inspection "
              "program. If it does not, or if you are in unincorporated "
              "county, your electrical permit and inspections come from "
              "L&amp;I.", S["body"]),
    Paragraph("Getting this wrong does not merely waste a phone call — it "
              "means nobody inspects your rough-in before you cover it. "
              "(RCW 19.28.010(3), (4); RCW 19.28.101(1))", S["body"]),
]))

# ---------------------------------------------------------------- how to find
flow += k.h2_tight("HOW TO FIND EACH OFFICE")
find_rows = [
    [k.cellp("<b>Building department</b><br/>(permit, plan review, most "
             "inspections)"),
     k.cellp("Search \"<i>[your county] WA building permit</i>\" or "
             "\"<i>[your city] WA permits</i>.\" Nearly every Washington "
             "jurisdiction now runs an online permit portal — ask which one "
             "and register before you file, not on filing day.")],
    [k.cellp("<b>L&amp;I electrical</b><br/>(permit, inspection, contractor "
             "and electrician lookup)"),
     k.cellp("<b>lni.wa.gov</b> → Licensing &amp; Permits → Electrical. "
             "Permits and inspection requests are handled online. Verify any "
             "contractor or electrician at "
             "<b>secure.lni.wa.gov/verify/</b>.")],
    [k.cellp("<b>Local health jurisdiction</b><br/>(septic, often wells)"),
     k.cellp("The Department of Health publishes the authoritative list of "
             "every local health jurisdiction in the state at <b>doh.wa.gov</b> "
             "→ About Us → Washington's Public Health System → Local Health "
             "Jurisdictions. Use that rather than guessing — several counties "
             "share a district.")],
    [k.cellp("<b>Water availability</b>"),
     k.cellp("If you will connect to a public system, ask the purveyor for a "
             "written letter stating the ability to serve. If you will drill, "
             "start at <b>ecology.wa.gov</b> → Water &amp; Shorelines → Water "
             "Supply → Water Availability, and find your water resource "
             "inventory area before you budget anything.")],
    [k.cellp("<b>Planning / zoning and critical areas</b>"),
     k.cellp("Often a separate counter from building, sometimes the same one. "
             "Ask who confirms zoning, setbacks, and whether any critical "
             "area or shoreline designation touches your parcel — you need "
             "that answer before plan review, not during it.")],
    [k.cellp("<b>Road approach</b>"),
     k.cellp("If your driveway meets a <b>state highway</b>, the access "
             "permit comes from WSDOT — <b>wsdot.wa.gov</b>. If it meets a "
             "county or city road, it comes from that road authority. "
             "Establish which road you are actually connecting to first.")],
]
flow.append(k.ref_table(
    "Finding the right office for your parcel",
    [k.cellp("Office", bold=True), k.cellp("How to find it", bold=True)],
    find_rows, [2.05 * inch, CW - 2.05 * inch]))

# ---------------------------------------------------------------- state level
flow += k.h2_tight("STATE-LEVEL CONTACTS")
flow.append(k.body(
    "These are stable and worth knowing. Phone numbers are left for you to "
    "write in — a wrong number printed in a kit is worse than no number."))

state_rows = [
    [k.cellp("<b>Labor &amp; Industries (L&amp;I)</b>"),
     k.cellp("Contractor registration and the public verification lookup; "
             "electrician certification; and — for most of the state — your "
             "electrical permit and electrical inspections."),
     k.cellp("lni.wa.gov")],
    [k.cellp("<b>State Building Code Council</b>"),
     k.cellp("Publishes the Washington State Building Code, the state "
             "amendments, and the wildland-urban interface and tsunami map "
             "resources. Also where a local residential amendment must be "
             "approved."),
     k.cellp("sbcc.wa.gov")],
    [k.cellp("<b>Department of Ecology</b>"),
     k.cellp("Water rights and water availability, water resource inventory "
             "areas, well construction under chapter 18.104 RCW, and the "
             "construction stormwater permit."),
     k.cellp("ecology.wa.gov")],
    [k.cellp("<b>Department of Health</b>"),
     k.cellp("Writes the on-site sewage rule (chapter 246-272A WAC) that your "
             "local health jurisdiction administers, and publishes the "
             "directory of those jurisdictions."),
     k.cellp("doh.wa.gov")],
    [k.cellp("<b>Department of Revenue</b>"),
     k.cellp("Retail sales tax on construction — see WA.5. Also the sales tax "
             "rate lookup for your exact address."),
     k.cellp("dor.wa.gov")],
    [k.cellp("<b>Department of Natural Resources</b>"),
     k.cellp("The statewide wildfire hazard map that the wildland-urban "
             "interface provisions key to."),
     k.cellp("dnr.wa.gov")],
    [k.cellp("<b>Washington State Legislature</b>"),
     k.cellp("The RCW and WAC text itself — every citation in this kit can be "
             "read here in about a minute."),
     k.cellp("app.leg.wa.gov")],
]
flow.append(k.ref_table(
    "State agencies and what each is actually for",
    [k.cellp("Agency", bold=True),
     k.cellp("Why you would contact them", bold=True),
     k.cellp("Website", bold=True)],
    state_rows, [1.85 * inch, CW - 1.85 * inch - 1.3 * inch, 1.3 * inch]))

# ---------------------------------------------------------------- counties
flow += k.h2_tight("HIGH-VOLUME COUNTIES — VERIFIED DOMAINS")
flow.append(k.body(
    "The domain is the durable key; navigate from the home page rather than "
    "trusting a deep link. Where the health jurisdiction is a separate "
    "organization with its own domain, it is given — that separation is "
    "exactly the thing owner-builders miss."))

county_rows = [
    ("King", "kingcounty.gov", "kingcounty.gov (Public Health — Seattle &amp; "
     "King County)"),
    ("Pierce", "piercecountywa.gov", "tpchd.org (Tacoma-Pierce County Health "
     "Department)"),
    ("Snohomish", "snohomishcountywa.gov", "snohd.org (Snohomish County "
     "Health Department)"),
    ("Spokane", "spokanecounty.gov", "srhd.org (Spokane Regional Health "
     "District)"),
    ("Clark", "clark.wa.gov", "clark.wa.gov (Clark County Public Health)"),
    ("Thurston", "thurstoncountywa.gov", "thurstoncountywa.gov"),
    ("Kitsap", "kitsap.gov", "kitsappublichealth.org (Kitsap Public Health "
     "District)"),
    ("Yakima", "yakimacounty.us", "via the DOH directory"),
    ("Whatcom", "whatcomcounty.us", "whatcomcounty.us"),
    ("Benton", "bentoncountywa.gov", "bfhd.wa.gov (Benton-Franklin Health "
     "District)"),
    ("Franklin", "franklincountywa.gov", "bfhd.wa.gov (Benton-Franklin Health "
     "District)"),
    ("Skagit", "skagitcounty.net", "skagitcounty.net"),
    ("Island", "islandcountywa.gov", "islandcountywa.gov"),
    ("Lewis", "lewiscountywa.gov", "lewiscountywa.gov"),
]
rows = [[k.cellp(f"<b>{a}</b>"), k.cellp(b), k.cellp(c)]
        for a, b, c in county_rows]
flow.append(k.ref_table(
    "County domains, checked live August 2026",
    [k.cellp("County", bold=True), k.cellp("County site", bold=True),
     k.cellp("Local health jurisdiction", bold=True)],
    rows, [1.05 * inch, 1.85 * inch, CW - 2.9 * inch]))
flow.append(k.cite(
    "Each domain above was requested and returned a live Washington "
    "government site in August 2026; <b>department names and page paths "
    "inside those sites were not all separately verified</b>, so navigate "
    "from the home page. Not in the table? Two statewide directories cover "
    "the rest: local health jurisdictions at <b>doh.wa.gov</b>, and building "
    "departments through the Washington Association of Building Officials at "
    "<b>wabo.org</b> — a professional association, not a government agency. "
    "<b>mrsc.org</b> (Municipal Research and Services Center) is the standard "
    "reference for Washington local government and is likewise "
    "non-governmental."))

# ---------------------------------------------------------------- directory
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT")
flow.append(k.body(
    "Confirm each entry by speaking to the office rather than copying it from "
    "a search result, and write the date you confirmed it. Note the name of "
    "the person you spoke to — in a permit office, having a name is worth "
    "more than having a number."))


def office_block(label, sub):
    return [
        Paragraph(f"<b>{label}</b> — <font size=9.5>{sub}</font>", S["body"]),
        d.FillInRow([("Office / department:", 0.62), ("Phone:", 0.38)]),
        d.FillInRow([("Portal / address:", 0.44), ("Spoke with:", 0.34),
                     ("Confirmed:", 0.22)]),
        Spacer(1, 4),
    ]


for label, sub in [
    ("BUILDING DEPARTMENT", "issues the permit; most inspections"),
    ("ELECTRICAL — L&amp;I OR CITY", "circle which; permit and inspections"),
    ("PLANNING / ZONING", "setbacks, critical areas, address assignment"),
    ("LOCAL HEALTH JURISDICTION", "on-site sewage; often well siting"),
    ("WATER — PURVEYOR OR ECOLOGY", "evidence of adequate supply"),
    ("ROAD AUTHORITY", "driveway approach — WSDOT, county, or city"),
    ("ELECTRIC UTILITY", "temporary construction power and permanent service"),
    ("ENERGY TESTING AGENCY", "blower door, duct, ventilation — book early"),
]:
    flow += office_block(label, sub)

flow.append(Spacer(1, 4))
flow.append(k.cite(
    "<b>Sources</b> (verified August 2026 at app.leg.wa.gov): the state "
    "building code is in effect in all counties and cities — RCW "
    "19.27.031(1); electrical is regulated by chapter 296-46B WAC or the "
    "local jurisdiction's electrical code — WAC 51-51-003; L&amp;I inspects "
    "electrical work and only cities and towns may legislate in the field — "
    "RCW 19.28.101(1) with RCW 19.28.010(3), (4); on-site sewage is permitted "
    "by the local health officer — WAC 246-272A-0200(2); evidence of an "
    "adequate water supply is a condition of the building permit — RCW "
    "19.27.097(1)."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "wa-permit-kit",
                       "WA.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
