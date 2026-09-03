#!/usr/bin/env python3
"""PA.4 Where to File Directory.

Pennsylvania has roughly 2,560 municipalities and no central permit portal, so
a directory of building departments is impossible and would be obsolete within
a month if it were not. What IS possible, and is worth more, is a single
authoritative lookup: L&I maintains a live table of every municipality in the
Commonwealth with its UCC election and the name of its building code official.
That one table answers the kit's central question for any reader in the state,
and every opt-out row has a blank official — which is the fact itself,
rendered as a gap in a spreadsheet.

So this document is built around one link rather than a hundred, and then
covers the offices that are NOT the building department, which is where
Pennsylvania owner-builders actually lose time: the sewage enforcement officer
who works for the municipality but is certified by DEP, the county
conservation district that has no other role in your build, and PennDOT if
your driveway touches a state road.

Every URL printed here was fetched and returned HTTP 200 in September 2026.
Anything that would not resolve was left out rather than guessed at — see the
dossier's open questions.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from reportlab.lib.units import inch
from reportlab.platypus import Spacer

import kit as k

S = k.S
CW = k.CW

FORM_ID = "PA.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Where to File"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "How to find out which municipality holds your parcel and how it handles "
    "the code, plus the offices beyond the building department that can stop "
    "your permit.")
flow.append(k.disclaimer())

# ------------------------------------------------------------ the split
flow += k.h2_tight("FIRST, THE THING THAT CONFUSES EVERYONE", 2.0)
flow.append(k.body(
    "In Pennsylvania the <b>municipality</b> — your township, borough or city "
    "— is the unit of local government that matters for building. "
    "<b>Counties do not issue building permits.</b> A county is not a layer "
    "above your township for this purpose; it runs a different, much shorter "
    "list of things. If you have been calling the county to ask about your "
    "building permit, that is why the answers have been unhelpful."))
rows = [
    [k.cellp("<b>Your municipality</b><br/>(township, borough or city)"),
     k.cellp("The building permit and the UCC — or the notice that it has "
             "opted out. Zoning. The sewage permit, through its sewage "
             "enforcement officer. Local driveway permits. Any local trade "
             "licensing.")],
    [k.cellp("<b>Your county</b>"),
     k.cellp("The <b>conservation district</b> for erosion control and "
             "stormwater. The <b>recorder of deeds</b> for your deed and any "
             "liens. The assessment office. In a few counties, a health "
             "department — and in Allegheny County, the plumbing code "
             "itself.")],
    [k.cellp("<b>The Commonwealth</b>"),
     k.cellp("L&amp;I writes and interprets the UCC, certifies code officials "
             "and third-party agencies, and publishes the municipal election "
             "table. DEP sets the sewage standards your municipal officer "
             "applies. PennDOT permits driveways onto state highways. "
             "<b>None of them permits or inspects your house.</b>")],
]
flow.append(k.ref_table(
    "Who does what",
    [k.cellp("Level", bold=True), k.cellp("What it actually handles",
                                          bold=True)],
    rows, [2.1 * inch, CW - 2.1 * inch]))

# ------------------------------------------------------------ the lookup
flow += k.h2_tight("THE ONE LOOKUP THAT ANSWERS THE CENTRAL QUESTION", 2.0)
flow.append(k.body(
    "L&amp;I maintains a live table of <b>every municipality in "
    "Pennsylvania</b>, with its county, its type, whether it elected to "
    "administer and enforce the UCC or opted out, the effective date of that "
    "election, and the name of its building code official. Look up your own "
    "municipality here before you do anything else in this kit."))
flow.append(k.callout(
    "PA L&amp;I — municipal UCC elections table", [
        k.body("<b>pa.gov</b> → Agencies → Labor &amp; Industry → Uniform "
               "Construction Code → <b>Municipal Elections and Contact "
               "Information</b>"),
        k.body("When this kit was compiled the table held <b>2,563 "
               "municipalities: 2,444 had opted in and 119 had opted "
               "out</b> — about one in twenty-two. Thirty-four of the "
               "sixty-seven counties contain at least one opt-out "
               "municipality and no county is entirely opted out, so a "
               "neighboring township tells you nothing about yours."),
        k.body("<b>Read the building code official column.</b> On an opt-out "
               "row it is blank — because there is no municipal official to "
               "name. That blank is the whole finding in PA.1, printed as a "
               "gap in a spreadsheet."),
        k.body("<i>Elections change.</i> A municipality may switch on 180 "
               "days' notice, and the file is updated continuously — the "
               "counts above are September 2026. Check the table rather than "
               "trusting this paragraph."),
    ]))
flow.append(k.body(
    "If you are not certain which municipality your parcel is in, the "
    "Department of Community and Economic Development runs an address lookup "
    "that returns it: <b>apps.dced.pa.gov</b> → <b>Find Your "
    "Municipality</b>. DCED cautions that the geocoding behind it is outside "
    "its control, so on a rural parcel or near a municipal line confirm the "
    "answer with the county or the municipality itself. Your deed and your "
    "property tax bill also name it. Pennsylvania has many identically named "
    "townships in different counties, so always match on <b>county plus "
    "municipality</b>."))

# -------------------------------------------------------------- offices
flow += k.h2_tight("THE OFFICES", 2.2)
W = [1.7 * inch, CW - 4.25 * inch, 2.55 * inch]
HDR = [k.cellp("Office", bold=True), k.cellp("What you file or find there",
                                             bold=True),
       k.cellp("Where", bold=True)]
rows = [
    [k.cellp("<b>Your municipality</b>"),
     k.cellp("Building permit, zoning approval, sewage permit, local driveway "
             "permit. In an opt-out municipality: the written notice that you "
             "must obtain your own third-party agency."),
     k.cellp("Named in the L&amp;I<br/>elections table above")],
    [k.cellp("<b>Certified third-party<br/>agencies</b>"),
     k.cellp("The list of private agencies certified to perform UCC plan "
             "review and inspections. <b>Essential in an opt-out "
             "municipality.</b> Agencies marked <b>R</b> can perform the full "
             "range of residential approvals — that is the marking you need. "
             "Only agencies that volunteered detail are linked to a page "
             "showing counties served."),
     k.cellp("pa.gov → Labor &amp;<br/>Industry → Bureau of<br/>"
             "Occupational and<br/>Industrial Safety →<br/>"
             "<b>Third Party Agencies</b>")],
    [k.cellp("<b>Certified code<br/>officials search</b>"),
     k.cellp("Individual inspectors and their certification categories. Use "
             "it to check independently — L&amp;I's own caveat on the agency "
             "list is that entries are “based on information voluntarily "
             "provided … and may not accurately reflect an agency's current "
             "complement.”"),
     k.cellp("pa.gov → Labor &amp;<br/>Industry → UCC →<br/>"
             "<b>Certified Code Officials</b>")],
    [k.cellp("<b>Sewage enforcement<br/>officer (SEO)</b>"),
     k.cellp("Your on-lot sewage permit, soil testing and percolation test. "
             "The SEO is <b>retained by your municipality</b> but certified "
             "by the Commonwealth — ask the municipal office who theirs is. "
             "This is not a UCC function and is not affected by an opt-out "
             "election."),
     k.cellp("Your municipal office.<br/>DEP publishes a live<br/>"
             "<b>active SEOs by county</b><br/>report; standards are<br/>"
             "at <b>25 Pa. Code Ch. 73</b>")],
    [k.cellp("<b>PA DEP —<br/>septic systems</b>"),
     k.cellp("The Commonwealth's homeowner-facing guidance on on-lot systems, "
             "and the program under which SEOs are certified. DEP does not "
             "normally issue your permit; your municipality does."),
     k.cellp("pa.gov/agencies/dep →<br/>Residents → My Water →<br/>"
             "<b>Septic Systems</b>; and<br/>Clean Water → "
             "<b>Act 537<br/>Sewage Facilities</b>")],
    [k.cellp("<b>PA DEP —<br/>private wells</b>"),
     k.cellp("Guidance on private water wells, drilling and water testing. "
             "Read PA.4's note below on what Pennsylvania does and does not "
             "regulate here."),
     k.cellp("pa.gov/agencies/dep →<br/>Residents → My Water →<br/>"
             "<b>Private Wells</b>")],
    [k.cellp("<b>County conservation<br/>district</b>"),
     k.cellp("Erosion and sediment control plans and construction stormwater "
             "permitting. Every county has one, and it is the office most "
             "often missed on a rural lot. Find yours through the state "
             "association's directory."),
     k.cellp("<b>pacd.org</b>")],
    [k.cellp("<b>PennDOT</b>"),
     k.cellp("Highway occupancy permit, if your driveway meets a state "
             "highway. Your building permit must carry notice that an HOP is "
             "required, and PennDOT has 60 days to act or the permit is "
             "deemed issued. Ask for the <b>minimum use driveway</b> "
             "form — it covers a driveway expected to carry no more than 25 "
             "vehicles a day, which is what a house is."),
     k.cellp("pa.gov/agencies/penndot;<br/>or your PennDOT<br/>"
             "district office")],
    [k.cellp("<b>PA One Call</b>"),
     k.cellp("Utility line location before you excavate. Confirm whether the "
             "homeowner exemption reaches what you are doing — it does not "
             "extend to contractors you hire."),
     k.cellp("<b>pa1call.org</b>")],
    [k.cellp("<b>Office of Attorney<br/>General — HICPA</b>"),
     k.cellp("Search a home improvement contractor's registration. Remember "
             "that new-home construction is outside HICPA, so a sub framing "
             "your house may legitimately have no registration (PA.1)."),
     # One line, deliberately: a <br/> after "hicsearch." split the hostname
     # across two lines and a reader cannot tell it is one address.
     k.cellp("<b>hicsearch.attorneygeneral.gov</b>")],
    [k.cellp("<b>County recorder<br/>of deeds</b>"),
     k.cellp("Your deed, easements and rights-of-way — which you need for "
             "the site plan — and where mechanics' lien claims are filed "
             "against your property."),
     k.cellp("Your county courthouse")],
    [k.cellp("<b>FEMA Flood Map<br/>Service Center</b>"),
     k.cellp("Confirm whether your lot is in a mapped flood hazard area "
             "before you design. Drives the extra submissions in "
             "34 Pa. Code §&nbsp;403.62a(d)."),
     k.cellp("<b>msc.fema.gov</b>")],
    [k.cellp("<b>PA DEP — radon</b>"),
     k.cellp("Pennsylvania has among the highest indoor radon in the country "
             "and the UCC requires nothing about it (PA.2). If you want a "
             "passive system, this is where the guidance and the certified "
             "professional list live."),
     k.cellp("pa.gov/agencies/dep →<br/>Radiation Protection →<br/>"
             "<b>Radon Division</b>")],
    [k.cellp("<b>The law itself</b>"),
     k.cellp("Regulations — anything cited “Pa. Code” — at the first site. "
             "Statutes — anything cited “P.S.” — at the second. They are "
             "different websites and neither carries the other's material."),
     k.cellp("<b>pacodeandbulletin.gov</b><br/><b>legis.state.pa.us</b>")],
]
flow.append(k.ref_table("Where to file, and where to look things up",
                        HDR, rows, W))
flow.append(Spacer(1, 6))
flow.append(k.cite(
    "Every address above was checked in September 2026. Pennsylvania moved "
    "its agency websites to pa.gov recently and deep links have not been "
    "stable through that migration, so this table gives you the agency and "
    "the path to click rather than a long URL that may rot — and the two "
    "legal-research sites, which have not moved, in full."))

# ------------------------------------------------- Allegheny + Philadelphia
flow += k.h2_tight("TWO PLACES WHERE THIS ALL WORKS DIFFERENTLY", 2.0)
flow.append(k.bullet(
    "<b>Allegheny County.</b> Plumbing is not a UCC subject here. "
    "35 P.S. § 7210.501(a.1) bars a municipality in a county of the second "
    "class from administering and enforcing the plumbing provisions, and the "
    "county enforces its own plumbing code under the Local Health "
    "Administration Law instead. Expect a separate permit, a separate "
    "inspector and county plumber licensing, from the county health "
    "department rather than your municipality."))
flow.append(k.bullet(
    "<b>Philadelphia.</b> A city of the first class, with its own department "
    "of licenses and inspections, its own permitting system and its own trade "
    "licensing. The one place the UCC gives it a different number is the "
    "certificate of occupancy clock, which is 10 business days rather than 5 "
    "(34 Pa. Code § 403.65(b)) — and the appeal decision deadline, likewise "
    "10 rather than 5."))

# ------------------------------------------------------------- the wells
flow += k.h2_tight("A NOTE ON WELLS", 1.6)
flow.append(k.body(
    "If your lot needs a well, do not assume the permit-and-inspection "
    "pattern you have just learned for sewage carries across to water. It "
    "does not. Sewage is governed by a detailed state regulation — "
    "25&nbsp;Pa. Code Chapter 73 — administered by a certified officer, with "
    "isolation distances you can look up. <b>Ask your municipality whether it "
    "has a well ordinance, and ask your driller in writing what construction "
    "standard they will build to</b>, because the answer may be “our own.” "
    "Specify casing depth, grouting, the cap and a post-completion water "
    "test in the contract rather than assuming an inspector will check them."))
flow.append(k.cite(
    "The isolation distances in 25 Pa. Code § 73.13 are written from the "
    "septic side: the absorption area must be 100 feet from an individual "
    "water supply and the treatment tank 50 feet. That is a constraint on "
    "where your septic system may go relative to a well — plan both at once, "
    "on the same drawing, before either is installed."))

# ------------------------------------------------------------- write-ins
flow += k.h2_tight("THE OFFICES YOU CONFIRMED", 1.6)
flow.append(k.body(
    "Fill this in as you go. On an owner-built house this page is the only "
    "place the whole picture exists — and in an opt-out municipality no "
    "single office holds it at all."))
flow += k.check_table(
    "Confirmed offices for this project", [
        ("Municipality — and its UCC election (opt-in / opt-out)",
         [("Municipality", 0.55), ("Election", 0.45)]),
        ("Building code official, or the third-party agency you engaged",
         [("Name", 1.0)]),
        ("Zoning officer", [("Name", 1.0)]),
        ("Sewage enforcement officer", [("Name", 1.0)]),
        ("County conservation district", [("District", 1.0)]),
        ("PennDOT district — if the driveway meets a state highway",
         [("District", 0.5), ("HOP no.", 0.5)]),
        ("County recorder of deeds — book and page of your deed",
         [("Book", 0.5), ("Page", 0.5)]),
        ("Well driller — and the standard they contracted to build to",
         [("Driller", 1.0)]),
        ("Flood zone determination", [("Zone", 0.5), ("Panel", 0.5)]),
        ("Local trade licensing required? (electrical / plumbing)",
         [("Answer", 1.0)]),
    ], notes_header="Confirmed on / notes")

# --------------------------------------------------------------- sources
flow.append(Spacer(1, 4))
flow.append(k.sources_table([
    ("Municipalities administer and enforce; five arrangements",
     "35 P.S. § 7210.501(b)"),
    ("Opt-out: municipality must notify; applicant obtains a certified "
     "third-party agency",
     "34 Pa. Code § 403.103(b); 35 P.S. § 7210.501(e)(1)"),
    ("Municipal election counts, and the officials named",
     "PA L&amp;I municipal elections table, retrieved September 2026"),
    ("Third-party agencies must be certified by the Department",
     "34 Pa. Code § 401.1; PA L&amp;I third-party agency list"),
    ("Allegheny County plumbing carve-out",
     "35 P.S. § 7210.501(a.1); 34 Pa. Code § 403.21(a)(6)(i)"),
    ("Certificate of occupancy: 10 business days in cities of the first class",
     "34 Pa. Code § 403.65(b)"),
    ("On-lot sewage governed by Chapter 73, outside the UCC",
     "34 Pa. Code § 403.21(e)"),
    ("Septic isolation distances — absorption area and treatment tank",
     "25 Pa. Code § 73.13(b), (c)"),
    ("Highway occupancy permit notice and PennDOT's 60-day clock",
     "35 P.S. § 7210.502(b)"),
]))
flow.append(Spacer(1, 2))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "pa-permit-kit",
                       "PA.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
