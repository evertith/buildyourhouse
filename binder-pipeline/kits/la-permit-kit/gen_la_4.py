#!/usr/bin/env python3
"""LA.4 Where to File Directory.

The strongest single finding behind this document: all 64 Louisiana parish
governments are registered with the Uniform Construction Code Commission as
code-enforcement jurisdictions, each with its own credential number. There is
no Louisiana parish that is off the permitting map, and the "some parishes are
exempt by affidavit" folklore describes law that is no longer in force.

DELIBERATELY NOT PRINTED: deep permit-page URLs, one per parish. They split
across table columns, they rot faster than anything else in the kit, and the
Commission's own jurisdiction registry plus the state's parish index find the
current page in two clicks. The office NAME is the durable, checkable thing;
that is what the directory carries. Parishes whose office name could not be
read off an official page are named in a separate, clearly-labelled block
rather than guessed at.
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

FORM_ID = "LA.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Where to File"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "Parish or town, staff or contractor — how to find the "
                 "office that will actually handle your parcel, and a page to "
                 "write down what you confirmed.")
flow.append(k.disclaimer())

# ------------------------------------------------------------------ structure
flow += k.h2("THERE IS NO SUCH THING AS A NO-PERMIT PARISH")
flow.append(k.body(
    "If you have built in Texas, Mississippi or Alabama, you will be looking "
    "for the rural parish where nobody enforces anything. It does not exist "
    "in Louisiana, and the belief that it does is the most expensive "
    "misconception an owner-builder can carry into this state."))
flow.append(k.body(
    "The enforcement statute says every municipality and parish <b>shall</b> "
    "enforce the Uniform Construction Code, and then closes the door "
    "expressly: <b>&ldquo;Nothing in this Chapter allows any local government "
    "to avoid enforcement.&rdquo;</b> An older version of Louisiana law did "
    "let a parish file an affidavit claiming an exemption. That mechanism is "
    "gone from the operative text — the section heading still carries the "
    "words, but the affidavit itself is no longer there. If you find a page "
    "telling you your parish opted out, it is describing repealed law."))
flow.append(k.callout(
    "Checked against the Commission's own register, September 2026", [
        Paragraph(
            "Every one of Louisiana's <b>64 parish governments</b> was run "
            "through the Uniform Construction Code Commission's public "
            "jurisdiction registry. <b>All 64 returned a credential "
            "number.</b> Not most. All of them. Whatever else is true about "
            "how thinly your parish is staffed, it is a registered code "
            "enforcement jurisdiction, and LA.3 gives you the statutory route "
            "to get inspected when the counter is quiet.", S["body"]),
    ]))

flow += k.h2_tight("PARISH OR TOWN? SETTLE THIS FIRST", reserve=2.0)
flow.append(k.body(
    "The parish building official is appointed to oversee <b>the "
    "unincorporated area</b> of the parish. Inside a town's corporate limits, "
    "the town is the authority. Roughly 150 Louisiana municipalities are "
    "registered with the Commission separately from the 64 parish "
    "governments, which is direct evidence that those towns run their own "
    "code enforcement."))
flow.append(k.callout(
    "A mailing address is not a jurisdiction", [
        Paragraph(
            "A parcel with a Ruston, Covington or Opelousas mailing address "
            "may sit well outside those city limits — and the reverse "
            "happens too. Before you drive anywhere, confirm in writing "
            "whether the parcel is inside or outside the corporate limits. "
            "Filing in the wrong place costs weeks, and in a couple of "
            "parishes the reach is genuinely surprising: St. Landry Parish's "
            "permit office states that it also covers anyone inside the city "
            "limits of Arnaudville, Palmetto and Melville.", S["body"]),
    ]))

# ------------------------------------------------------------------ how
flow += k.h2("HOW TO FIND YOUR OFFICE, IN THREE STEPS")
rows = [
    [k.cellp("<b>1</b>"),
     k.cellp("Confirm the jurisdiction"),
     k.cellp("Settle whether the parcel is inside a municipality or in the "
             "unincorporated parish. The assessor's parcel record and the "
             "parish GIS map will tell you; get it in writing.")],
    [k.cellp("<b>2</b>"),
     k.cellp("Find the office"),
     k.cellp("Start from the State of Louisiana's own parish index at "
             "<b>la.gov</b> (Local Louisiana), which links every parish "
             "government site. Then look for Permits, Permits &amp; "
             "Inspections, Planning &amp; Development, Planning &amp; "
             "Zoning, Community Development, or Public Works — Louisiana "
             "files permitting under all six names.")],
    [k.cellp("<b>3</b>"),
     k.cellp("Find the inspector"),
     k.cellp("Use the Commission's public search, reachable from "
             "<b>lsuccc.la</b>, to look up your jurisdiction and the licensed "
             "inspectors who cover it. This is also how you check that a "
             "private inspector you are considering is genuinely licensed, "
             "and how you find one who already works your parish.")],
]
flow.append(k.ref_table(
    "Finding the office that handles your parcel",
    [k.cellp("", bold=True), k.cellp("", bold=True),
     k.cellp("", bold=True)],
    rows, [0.35 * inch, 1.45 * inch, CW - 1.80 * inch]))
flow.append(k.cite(
    "This kit prints office names rather than deep links. Permit-page URLs "
    "are the fastest-rotting thing in any directory — several Louisiana "
    "parish pages found during verification still point at a state web "
    "address that was retired — while an office name and a route to it stay "
    "good. Both starting points above are stable state-level entry points."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Your parish may have hired its building official",
    [
        Paragraph(
            "Louisiana expressly allows a parish to contract enforcement out "
            "— to another government, to a regional planning commission, or "
            "to a licensed private inspector. Several parishes publish "
            "exactly who that is. Bossier Parish states that <b>Code "
            "Inspections Plus</b> &ldquo;serves as the building official for "
            "Bossier Parish.&rdquo; St. Martin Parish states that all "
            "construction inspections are conducted by <b>Building Code "
            "Inspection Services, LLC</b>, a contracted third-party provider. "
            "Union Parish names <b>Lagniappe Inspection Services</b> as its "
            "building official. Concordia Parish states that <b>IBTS</b> "
            "handles all inspections for the parish. Caddo Parish has an "
            "agreement under which the <b>City of Shreveport</b> performs all "
            "residential inspections for the parish.", S["body"]),
        Paragraph(
            "Two regional planning commissions do this work at scale: the "
            "<b>Rapides Area Planning Commission</b>, which covers "
            "unincorporated Rapides and took on Vernon Parish in March 2025, "
            "and the <b>South Central Planning &amp; Development "
            "Commission</b> in Houma, which describes itself as providing "
            "code enforcement across a five-parish region. If your parish "
            "website is thin on permitting detail, this is usually why — the "
            "work is happening somewhere else.", S["body"]),
        Paragraph(
            "A large share of Louisiana jurisdictions take applications "
            "through a shared online permitting portal rather than at a "
            "counter. Ask which portal yours uses before you make the drive.",
            S["body"]),
    ]))

# ------------------------------------------------------------------ directory
flow += k.h2("PARISH DIRECTORY")
flow.append(k.body(
    "Office names below were read off each parish government's own website in "
    "September 2026. Names change; use this to know what you are looking for "
    "and who to ask for, then confirm at the counter."))
D = [
    ("Acadia", "Police Jury",
     "Building Permits office", "Publishes a Self Contracting Form for "
     "owner-builders and a no-sewer affidavit. Under 200 sq ft, no permit."),
    ("Ascension", "Parish Government",
     "Building Department / Permitting, under Planning &amp; Development",
     "Has a Residential New Construction application, an address application "
     "and a flood zone determination form."),
    ("Allen", "Police Jury", "Permits, Buildings &amp; Solid Waste",
     "Permit required before construction, wiring, piping, re-roofing or "
     "moving a manufactured home."),
    ("Beauregard", "Police Jury", "Permit Office",
     "Permit required outside city or town limits. Wants the assessor parcel "
     "listing, culvert permit, 911 permit, sewer permit and your electric "
     "account number."),
    ("Bossier", "Police Jury",
     "Building official is a contracted private firm",
     "Bossier City and Benton permit separately."),
    ("Caddo", "Parish Commission",
     "Public Works — Permits Division",
     "Residential inspections performed by the City of Shreveport under "
     "agreement. The parish page lists stale code years; the state codes "
     "govern."),
    ("Concordia", "Police Jury", "Police Jury permit intake",
     "Inspections performed by a contracted provider."),
    ("East Baton Rouge", "Consolidated city-parish",
     "Permits &amp; Inspections Division, Department of Development",
     "Baker, Central, Zachary and St. George permit their own."),
    ("Grant", "Police Jury", "Building Permit Office",
     "States that only the homeowner or a licensed builder may apply. "
     "E-911 address requested from the sheriff's office first."),
    ("Iberia", "Parish Government", "Permits Department",
     "New Iberia permits separately."),
    ("Iberville", "Parish Government", "Permits &amp; Inspections Department",
     "Online-only filing. Plaquemine, St. Gabriel, White Castle and "
     "Maringouin permit separately."),
    ("Jackson", "Police Jury", "Uniform Building Code office",
     "Permits by email or mail, with a published checklist; three to five "
     "business day review."),
    ("Jefferson", "Parish Government", "Building Permits Department",
     "Engineering automatically reviews every new dwelling permit. Gretna, "
     "Harahan, Kenner, Westwego, Grand Isle and Jean Lafitte permit "
     "separately."),
    ("Lafayette", "Consolidated city-parish",
     "Development and Planning Department",
     "Broussard, Carencro, Duson, Scott and Youngsville permit separately."),
    ("Lafourche", "Parish Government", "Permits &amp; Planning Department",
     "A current electric utility bill is required with any permit "
     "application."),
    ("Lincoln", "Police Jury",
     "Police Jury permit intake — issues a Project Permit",
     "Separate residential driveway-culvert application. Ruston, Grambling, "
     "Dubach, Choudrant and Simsboro permit separately."),
    ("Livingston", "Parish Government", "Building &amp; Permit Department",
     "Publishes a request for flood zone determination. Denham Springs, "
     "Walker and Livingston permit separately."),
    ("Natchitoches", "Parish Government", "Planning &amp; Zoning Department",
     "City of Natchitoches permits separately."),
    ("Orleans", "City and parish are coterminous",
     "Department of Safety and Permits",
     "The only permit authority in the parish. Separate divisions for "
     "electrical, mechanical, floodplain and stormwater."),
    ("Ouachita", "Police Jury", "Parish Permit Office",
     "Publishes a roster of registered third-party private inspectors — the "
     "clearest illustration in the state of the private-inspector route."),
    ("Plaquemines", "Parish Government", "Permits, Planning &amp; Zoning",
     "Filing runs through an online portal; confirm the office name at the "
     "counter."),
    ("Rapides", "Police Jury",
     "Rapides Area Planning Commission, under contract",
     "The Police Jury site lists no permit office. Alexandria, Pineville, "
     "Ball and Boyce permit separately."),
    ("Red River", "Police Jury", "Permit Officer division", ""),
    ("Sabine", "Police Jury", "Building Code Office",
     "Separate parish planning commission."),
    ("St. Bernard", "Parish Government", "Department of Community Development",
     "Publishes new residential construction and elevation requirement "
     "documents."),
    ("St. Helena", "Police Jury", "Building Department",
     "Publishes a six-step permit process starting at the 911 office. The "
     "page cites a stale code year; the state codes govern."),
    ("St. James", "Parish Government", "Office of Planning and Permitting",
     ""),
    ("St. Landry", "Parish Government", "Parish Permits Office",
     "Also covers anyone inside the city limits of Arnaudville, Palmetto and "
     "Melville. By appointment. Issues temporary electrical service on new "
     "construction."),
    ("St. Martin", "Parish Government", "Building Permits Department",
     "All construction inspections conducted by a contracted third-party "
     "provider."),
    ("St. Tammany", "Parish Government", "Department of Permits and "
     "Inspections", "Also runs parish contractor registration."),
    ("Tangipahoa", "Parish Government", "Parish Permit Office",
     "Amite, Hammond, Ponchatoula, Independence, Tickfaw, Roseland, Kentwood "
     "and Tangipahoa village permit separately."),
    ("Terrebonne", "Consolidated city-parish",
     "Permits Division, under Planning and Zoning",
     "Also issues culvert and coastal use permits and holds elevation "
     "certificates."),
    ("Union", "Police Jury",
     "Police Jury office; building official is a contracted firm",
     "Publishes the clearest counter walkthrough in the state — application "
     "form collected from the 911 office."),
    ("Vernon", "Police Jury",
     "Rapides Area Planning Commission, under contract, with a local office "
     "in Leesville",
     "Joined RAPC in March 2025. Bring two sets of plans and a Manual J."),
    ("Washington", "Parish Government",
     "Licensing &amp; Permits Department", "Publishes a single-family "
     "residence permitting procedure and a floodplain determination "
     "service."),
    ("West Baton Rouge", "Parish Council",
     "Community Planning &amp; Development — Permit Office",
     "Addis, Brusly and Port Allen permit separately."),
    ("West Feliciana", "Parish Government", "Permits &amp; Inspections",
     "Building, electrical, plumbing, manufactured housing, roofing and "
     "culvert permits."),
]
rows = [[k.cellp(f"<b>{p}</b>"), k.cellp(g), k.cellp(o), k.cellp(n)]
        for p, g, o, n in D]
flow.append(k.ref_table(
    "Parish permitting offices, read from official parish sites "
    "(September 2026)",
    [k.cellp("Parish", bold=True), k.cellp("Governing body", bold=True),
     k.cellp("Office", bold=True), k.cellp("Notes", bold=True)],
    # Parish column needs 1.30in: "Plaquemines" measures 68.7pt bold and
    # "Natchitoches" 70.1pt, which both overflow the 69.6pt a 1.05in column
    # leaves after padding — they were splitting as "Plaquemine / s".
    rows, [1.30 * inch, 1.15 * inch, 1.70 * inch, CW - 4.15 * inch]))

flow += k.h2_tight("The parishes not listed above", reserve=2.0)
flow.append(k.body(
    "Twenty-seven parishes are absent from that table. That is a statement "
    "about this kit's verification standard, not about those parishes: each "
    "is a registered code enforcement jurisdiction with the Commission, but "
    "an official page naming its permit office could not be read during "
    "verification, and this kit does not print an office name it has not "
    "seen. They are:"))
flow.append(k.body(
    "Assumption, Avoyelles, Bienville, Caldwell, Calcasieu, Cameron, "
    "Catahoula, Claiborne, DeSoto, East Carroll, East Feliciana, Evangeline, "
    "Franklin, Jefferson Davis, LaSalle, Madison, Morehouse, Pointe Coupee, "
    "Richland, St. Charles, St. John the Baptist, St. Mary, Tensas, "
    "Vermilion, Webster, West Carroll and Winn."))
flow.append(k.body(
    "For any of these, work the three steps above. St. Charles Parish is "
    "worth one note: it contains <b>no incorporated municipalities</b>, so "
    "the parish government is the only permit authority anywhere in it — "
    "there is no city-versus-parish question to settle."))

# ------------------------------------------------------------------ write-in
flow += k.h2("MY OFFICES — FILL THIS IN AND KEEP IT WITH THE JOB")
w = CW
flow.append(d.titled_table(
    "Confirmed for this project",
    [k.cellp("What", bold=True), k.cellp("Office / person", bold=True),
     k.cellp("Confirmed how and when", bold=True)],
    [[k.cellp(a), "", ""] for a in [
        "Is the parcel inside a municipality? (yes / no)",
        "Building permit office",
        "Building official (name and license number)",
        "Are third-party or private inspectors accepted here?",
        "Online permit portal used",
        "Parish health unit (sewage permit)",
        "911 / address assignment office",
        "Floodplain manager",
        "Culvert / driveway — parish public works or state highway district",
        "Electrical: may a homeowner pull the permit, and does this "
        "jurisdiction register individual electricians?",
        "Plan review turnaround quoted",
    ]],
    [2.35 * inch, 2.15 * inch, w - 4.50 * inch], S))

# ------------------------------------------------------------------ sources
flow.append(Spacer(1, 8))
flow.append(k.sources_table([
    ("Every municipality and parish shall enforce; no local government may "
     "avoid enforcement", "R.S. 37:3737(A)(1)"),
    ("The parish appoints a building official for its unincorporated area",
     "R.S. 37:3741"),
    ("A parish may contract enforcement to another public entity or a "
     "licensed private inspector", "R.S. 37:3740"),
    ("A regional planning commission may hold the building-official role",
     "R.S. 37:3737(G)"),
    ("All 64 parish governments registered as code enforcement jurisdictions",
     "LUCCC public jurisdiction registry, September 2026"),
    ("Parish office names, governing bodies and municipal carve-outs",
     "Each parish government's own website, September 2026"),
    ("Named contracted providers and regional commissions",
     "Bossier, St. Martin, Union, Concordia, Caddo, Rapides and Vernon "
     "parish pages"),
    ("State index of parish governments", "la.gov, Local Louisiana"),
]))
flow.append(k.closing_note(
    "Two lookups answer almost anything this document leaves open. The state "
    "parish index at <b>la.gov</b> links every parish government. The "
    "Commission's public search, from <b>lsuccc.la</b>, confirms your "
    "jurisdiction is registered and lists the inspectors licensed to cover "
    "it — which is also how you check anyone offering to inspect your house. "
    "Read September 2026."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "la-permit-kit",
                       "LA.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
