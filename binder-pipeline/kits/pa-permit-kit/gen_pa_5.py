#!/usr/bin/env python3
"""PA.5 Forms & Documents Index.

Pennsylvania publishes no statewide building permit application, so an index
of "the forms" would be a very short and misleading document. What an
owner-builder actually needs is an index of the PAPER that will pass through
his hands — where each piece originates, what triggers it, and when it is due
relative to the permit.

The organizing insight is that the documents fall into three groups, and the
third is the one that catches owner-builders: documents nobody will ask you
for, that exist only because you are your own builder. In a normal build the
general contractor generates the certificates of insurance, the subcontract
terms and the lien paperwork. Acting as your own contractor does not remove
those documents from the job; it removes the person who was producing them.
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

FORM_ID = "PA.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "The Paperwork"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document this build will generate: what it is, which office it "
    "comes from, and when it is due.")
flow.append(k.disclaimer())

flow.append(k.body(
    "There is no Commonwealth building permit application form. The form "
    "belongs to your municipality or to the third-party agency you engage, "
    "and it will not look like anyone else's. What <i>is</i> consistent is "
    "the set of documents a Pennsylvania house generates, so that is what "
    "this index covers. Work down it and mark what your project actually "
    "triggers."))

W = [1.95 * inch, CW - 4.20 * inch, 1.15 * inch, 1.10 * inch]
HDR = [k.cellp("Document", bold=True), k.cellp("What it is", bold=True),
       k.cellp("Comes from", bold=True), k.cellp("When", bold=True)]

# ----------------------------------------------------- before the permit
flow += k.h2_tight("BEFORE THE BUILDING PERMIT", 2.0)
rows = [
    [k.cellp("<b>Municipal UCC election</b><br/>lookup"),
     k.cellp("Not a form — a lookup. L&amp;I publishes a table of every "
             "municipality with its opt-in or opt-out decision and the "
             "building code official's name. Settles who you are dealing "
             "with. See PA.4."),
     k.cellp("PA L&amp;I"), k.cellp("First")],
    [k.cellp("<b>Zoning permit or<br/>zoning approval</b>"),
     k.cellp("Confirms the use, the setbacks and the height are allowed. "
             "Entirely separate from the UCC and unaffected by an opt-out "
             "election — the municipality issues this either way."),
     k.cellp("Municipality"), k.cellp("Before permit")],
    [k.cellp("<b>Sewage permit</b><br/>(on-lot systems)"),
     k.cellp("Issued by the municipality through its sewage enforcement "
             "officer under the Sewage Facilities Act. Preceded by soil "
             "testing and a percolation test. Not a UCC document — "
             "34 Pa. Code §&nbsp;403.21(e) puts on-lot sewage outside the "
             "code entirely."),
     k.cellp("Municipal SEO"), k.cellp("Before permit")],
    [k.cellp("<b>Sewage planning module</b>"),
     k.cellp("The Act 537 planning step for a new lot, where an exemption "
             "does not apply. Runs through the municipality to DEP and is "
             "the slowest item on many rural projects."),
     k.cellp("Municipality<br/>and DEP"), k.cellp("Before sewage<br/>permit")],
    [k.cellp("<b>Highway occupancy permit</b>"),
     k.cellp("Required for a driveway meeting a state highway. The building "
             "permit must carry notice that an HOP is required. PennDOT has "
             "60 days to act or the permit is deemed issued."),
     k.cellp("PennDOT"), k.cellp("Before permit")],
    [k.cellp("<b>Erosion and sediment<br/>control plan</b>"),
     k.cellp("Earth disturbance triggers an E&amp;S plan, and larger "
             "disturbance triggers an NPDES construction stormwater permit "
             "through the county conservation district. Confirm your "
             "threshold with the district — see PA.4."),
     k.cellp("County<br/>conservation<br/>district"),
     k.cellp("Before ground<br/>is broken")],
    [k.cellp("<b>Construction documents</b>"),
     k.cellp("Plans and specifications. No architect or engineer seal is "
             "required for a house — but a licensed design professional's "
             "<i>certification</i> that the plans meet the UCC cuts the "
             "review clock from 15 business days to 5."),
     k.cellp("You or your<br/>designer"), k.cellp("With application")],
    [k.cellp("<b>Site plan</b>"),
     k.cellp("Required by regulation, not courtesy: size and location of new "
             "and existing structures and their distance from lot lines "
             "(34 Pa. Code §&nbsp;403.62a(e))."),
     k.cellp("You"), k.cellp("With application")],
    [k.cellp("<b>Flood hazard data</b>"),
     k.cellp("Only if the lot is in a mapped flood hazard area: boundaries, "
             "zones, design flood elevation and proposed lowest floor "
             "elevation (§&nbsp;403.62a(d))."),
     k.cellp("You / surveyor"), k.cellp("With application")],
    [k.cellp("<b>The municipality's list of<br/>other required permits</b>"),
     k.cellp("You are entitled to it by statute — and the same sentence says "
             "the municipality is not liable for its completeness. Ask in "
             "writing, then verify each item yourself."),
     k.cellp("Municipality"), k.cellp("At application")],
]
flow.append(k.ref_table("Approvals that come before, or with, the permit",
                        HDR, rows, W))

# ------------------------------------------------------- during the job
flow += k.h2_tight("DURING THE JOB", 2.0)
rows = [
    [k.cellp("<b>Building permit</b>"),
     k.cellp("Municipal or agency form. Keep a copy on the work site until "
             "construction is complete (§&nbsp;403.63(h)). Invalid if work "
             "does not begin within 180 days; valid no more than 5 years."),
     k.cellp("Municipality<br/>or agency"), k.cellp("Before work")],
    [k.cellp("<b>Stamped construction<br/>documents</b>"),
     k.cellp("The official stamps or notes each page as reviewed and "
             "approved and returns a set with any required changes marked. "
             "Keep them on site, open to inspection (§&nbsp;403.63(c))."),
     k.cellp("Reviewer"), k.cellp("At issuance")],
    [k.cellp("<b>Third-party agency<br/>engagement letter</b>"),
     k.cellp("Opt-out municipalities only, and the most important document "
             "you will negotiate. Scope, fees, re-inspection charges, "
             "response times, and what happens when you disagree — because "
             "you have no statutory appeal (PA.3)."),
     k.cellp("You and the<br/>agency"), k.cellp("Before work")],
    [k.cellp("<b>PA One Call ticket</b>"),
     k.cellp("Utility line location before excavation. Confirm whether the "
             "homeowner exemption reaches your situation — it does not "
             "extend to contractors you hire."),
     k.cellp("PA One Call"), k.cellp("Before digging")],
    [k.cellp("<b>Revised construction<br/>documents</b>"),
     k.cellp("Any change from the approved documents requires a revised set "
             "and an additional plan review (§§&nbsp;403.63(j), "
             "7210.502(a)(1))."),
     k.cellp("You"), k.cellp("On any change")],
    [k.cellp("<b>Inspection records</b>"),
     k.cellp("The official notifies you whether work complies or fails "
             "(§&nbsp;403.64(c)). Log every one — see the log in PA.3."),
     k.cellp("Official<br/>or agency"), k.cellp("Each inspection")],
    [k.cellp("<b>Energy compliance<br/>documentation</b>"),
     k.cellp("REScheck output, or the “Pennsylvania Alternative Residential "
             "Energy Provisions” package. Plus the blower door test result — "
             "3.0 ACH50 across the whole Commonwealth."),
     k.cellp("You / rater"), k.cellp("Permit and<br/>final")],
]
flow.append(k.ref_table("Documents the build itself generates", HDR, rows, W))

# ------------------------------------------------------------ closing out
flow += k.h2_tight("CLOSING OUT", 2.4)
rows = [
    [k.cellp("<b>Final inspection report</b>"),
     k.cellp("Filed by the official and indicating UCC compliance. A "
             "third-party agency must send a copy to the property owner, the "
             "builder and a lender designated by the builder."),
     k.cellp("Official<br/>or agency"), k.cellp("After final")],
    [k.cellp("<b>Certificate of occupancy</b>"),
     k.cellp("You may not occupy without it. Due within 5 business days of a "
             "compliant final report — 10 in Philadelphia. Check that it "
             "names the construction code edition."),
     k.cellp("Building code<br/>official"), k.cellp("Before you<br/>move in")],
    [k.cellp("<b>Sewage system<br/>final approval</b>"),
     k.cellp("The SEO's sign-off on the installed system, on its own track "
             "from the UCC final."),
     k.cellp("Municipal SEO"), k.cellp("Before use")],
    [k.cellp("<b>Well completion report</b>"),
     k.cellp("Where a well is drilled, the driller files a completion record "
             "with the Commonwealth. Ask your driller for a copy for your "
             "own file — see PA.4."),
     k.cellp("Well driller"), k.cellp("After drilling")],
]
flow.append(k.ref_table("Documents that end the job", HDR, rows, W))

# ------------------------------------------------- your own contractor
flow += k.h2_tight("THE DOCUMENTS NOBODY WILL ASK YOU FOR", 2.2)
flow.append(k.body(
    "This is the group that catches owner-builders, and it catches them "
    "quietly. On a normal build a general contractor produces these; acting "
    "as your own contractor does not remove them from the job, it removes "
    "the person who was producing them. None of them is filed with a "
    "government office, which is exactly why nobody chases you for one."))
rows = [
    [k.cellp("<b>Written subcontracts</b>"),
     k.cellp("Your new house is outside HICPA, so none of its mandatory "
             "terms apply automatically. PA.1 lists the terms the "
             "Commonwealth compels on a remodel — a capped deposit, a "
             "10% time-and-materials ceiling, written change orders, stated "
             "insurance — to copy into your own agreements."),
     k.cellp("You"), k.cellp("Before each<br/>trade starts")],
    [k.cellp("<b>Certificates of insurance</b>"),
     k.cellp("From every subcontractor, naming coverage limits and dates. "
             "HICPA's remodel benchmark is $50,000 personal injury and "
             "$50,000 property damage; on a new house you set the number, so "
             "set it deliberately."),
     k.cellp("Each sub"), k.cellp("Before each<br/>trade starts")],
    [k.cellp("<b>Workers' compensation<br/>evidence</b>"),
     k.cellp("Ask every sub for proof of coverage for their own people, and "
             "keep it. An uninsured worker injured on your lot is a problem "
             "that arrives long after the work is done."),
     k.cellp("Each sub"), k.cellp("Before each<br/>trade starts")],
    [k.cellp("<b>Lien waivers</b>"),
     k.cellp("Exchanged for payment, so that paying your contractor also "
             "clears the claims of the people behind them. Confirm the "
             "current requirements with a Pennsylvania attorney before you "
             "rely on a form from the internet."),
     k.cellp("You and each<br/>payee"), k.cellp("At every<br/>payment")],
    [k.cellp("<b>Photographic record</b>"),
     k.cellp("Photograph every wall cavity, every rough-in and every "
             "connection before it is covered. In an opt-out municipality "
             "this matters twice over: the inspection file sits with a "
             "private company, and you have no statutory appeal if a "
             "dispute arises."),
     k.cellp("You"), k.cellp("Ongoing")],
    [k.cellp("<b>The kit itself</b>"),
     k.cellp("Keep PA.3's inspection log and PA.4's confirmed-offices page "
             "with the permit. Together they are the continuous record of "
             "the build that no single office holds."),
     k.cellp("You"), k.cellp("Ongoing")],
]
flow.append(k.ref_table(
    "Paper that exists only because you are your own contractor",
    HDR, rows, W))
flow.append(Spacer(1, 6))
flow.append(k.callout(
    "One document you will want in fifteen years", [
        k.body("When you sell, Pennsylvania's Real Estate Seller Disclosure "
               "Law obliges you to disclose known material defects — and an "
               "owner-built house invites questions no other seller gets: was "
               "it permitted, was it inspected, where is the certificate of "
               "occupancy. A complete permit file answers all three in one "
               "envelope. An incomplete one is the reason some owner-built "
               "houses sell at a discount, and it is the strongest practical "
               "argument for doing the paperwork properly even where nobody "
               "is checking."),
    ]))

flow.append(Spacer(1, 4))
flow.append(k.sources_table([
    ("No statewide permit application; site plan and flood hazard "
     "submissions", "34 Pa. Code § 403.62a"),
    ("Design professional certification shortens review to 5 business days",
     "35 P.S. § 7210.502(a)(1)"),
    ("Municipality must provide the list of other required permits",
     "35 P.S. § 7210.502(a)(1)"),
    ("On-lot sewage is outside the UCC",
     "34 Pa. Code § 403.21(e)"),
    ("Highway occupancy permit notice; PennDOT's 60-day clock",
     "35 P.S. § 7210.502(b)"),
    ("Permit kept on site; 180 days; 5 years; revisions need a new review",
     "34 Pa. Code § 403.63(c), (g), (h), (j)"),
    ("Final report to owner, builder and lender; certificate of occupancy",
     "34 Pa. Code §§ 403.64(g), 403.65"),
    ("HICPA contract terms used here as a drafting benchmark",
     "73 P.S. §§ 517.7(a), 517.9(10)"),
]))
flow.append(Spacer(1, 2))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "pa-permit-kit",
                       "PA.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
