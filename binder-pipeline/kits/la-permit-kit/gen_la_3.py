#!/usr/bin/env python3
"""LA.3 Inspection Sequence.

Louisiana's inspection story has three parts that no general guide assembles:

  - the approvals that happen BEFORE the building permit exists, several of
    which are physically issued by offices that are not the permit office
    (the 911 office, the parish health unit, public works);
  - the building inspections themselves, which are performed by a
    Commission-licensed inspector who may be parish staff, a regional planning
    commission, a contracted private firm, or a private inspector the OWNER
    hires under the route the statute gives homeowners by name;
  - the closing sequence, where the certificate of occupancy is recorded in
    the parish conveyance records by the lender and the utilities are released.

Deliberately NOT printed: a statewide inspection list, because there is none
and the reason is precise. Louisiana adopts the IRC "not including Part
I-Administrative" (R.S. 37:3733(A)(3)), and IRC Part I is Chapter 1 — the
chapter carrying R109, Inspections. The one chapter that would have supplied a
required-inspection list is the one the state left out, so the schedule comes
from the parish's own administrative ordinance. The list printed here is
labelled as one parish's published requirements, used as a representative
example.
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

FORM_ID = "LA.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "Inspections"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "Who inspects your house in Louisiana, in what order, and "
                 "the route the statute gives you when your parish has no "
                 "counter.")
flow.append(k.disclaimer())

# ------------------------------------------------------------------ who
flow += k.h2("WHO INSPECTS — AND THE SENTENCE WORTH THE PRICE OF THIS KIT")
flow.append(k.body(
    "Louisiana requires that code enforcement be done by an inspector "
    "<b>licensed by the state commission</b>. That inspector might be on your "
    "parish's payroll, might work for a regional planning commission, might "
    "be a private firm the parish has contracted with — or might be someone "
    "<b>you hire yourself</b>. That last option is not a workaround. It is "
    "written into the enforcement statute, and homeowners claiming the "
    "owner-builder exemption are named in it."))
flow.append(k.callout_long(
    "The private-inspector route, in the statute's own words",
    [
        Paragraph(
            "&ldquo;Licensed contractors, <b>and homeowners exempted from the "
            "contractor licensing law pursuant to R.S. 37:2157, may establish "
            "agreements with private inspectors to conduct plan reviews, "
            "inspections, and enforce the State Uniform Construction "
            "Code.</b>&rdquo;", S["body"]),
        Paragraph(
            "With one condition attached, also verbatim: &ldquo;A local "
            "jurisdiction shall not accept an inspection report or plan "
            "review for the enforcement of the Uniform Construction Code from "
            "a private inspector <b>unless that inspector has a contract to "
            "provide inspection services with that jurisdiction … or has "
            "registered with that jurisdiction</b>.&rdquo;", S["body"]),
        Paragraph(
            "So the sequence is: find a Commission-licensed inspector who "
            "already works your parish, confirm they are contracted with or "
            "registered to that parish, and the parish must then take their "
            "reports. In a thinly staffed rural parish this is how an "
            "owner-builder keeps a build moving instead of waiting on a "
            "schedule nobody is keeping.", S["body"]),
    ]))
flow.append(k.cite(
    "La. R.S. 37:3737(A)(1), enacted by Acts 2026, No. 881. If you meet this "
    "rule cited as R.S. 40:1730.23, that is the repealed numbering — see the "
    "note in LA.2. Some parishes publish their registered private inspectors: "
    "Ouachita Parish maintains a roster on its permit-office site, which is "
    "the clearest public illustration of how the rule works in practice."))

flow.append(Spacer(1, 4))
rows = [
    [k.cellp("<b>Parish runs its own office</b>"),
     k.cellp("Most populous parishes. A Permits &amp; Inspections, Planning "
             "&amp; Development or Public Works division does plan review, "
             "issues the permit and inspects.")],
    [k.cellp("<b>Consolidated city-parish</b>"),
     k.cellp("One government covers both. East Baton Rouge, Lafayette and "
             "Terrebonne are consolidated; Orleans Parish and the City of New "
             "Orleans are coterminous, so the City's department is the only "
             "authority in the parish.")],
    [k.cellp("<b>Contracted out</b>"),
     k.cellp("The parish appoints an outside building official under an "
             "agreement the statute expressly authorizes. It may be a "
             "regional planning commission, a neighboring government, or a "
             "private inspection firm. Bossier, Union, Concordia, St. Martin, "
             "Vernon and Rapides all publish arrangements like this.")],
    [k.cellp("<b>You bring your own inspector</b>"),
     k.cellp("The route quoted above. Available to an owner-builder anywhere, "
             "subject to the inspector being registered with or contracted to "
             "your jurisdiction.")],
]
flow.append(k.ref_table(
    "Four ways your house gets inspected in Louisiana",
    [k.cellp("", bold=True), k.cellp("", bold=True)],
    rows, [1.65 * inch, CW - 1.65 * inch]))

# ------------------------------------------------------------------ before
flow += k.h2("STAGE ONE: THE APPROVALS THAT COME BEFORE THE PERMIT")
flow.append(k.body(
    "This is the part that catches people who have built in other states. In "
    "much of Louisiana the building permit application is effectively a "
    "<b>routing sheet</b>: other offices sign it before the permit office "
    "will look at it, and in some parishes the application form is not even "
    "handed out by the permit office. Union Parish's published instructions "
    "have the applicant collect the form from the 9-1-1 office, which "
    "completes and signs the top portion, then take it to the parish health "
    "unit for a second signature, and only then to the Police Jury."))
rows = [
    [k.cellp("<b>1</b>"), k.cellp("911 / E-911 address"),
     k.cellp("The parish 911 district, the sheriff's office, or the permit "
             "office itself, depending on parish."),
     k.cellp("<b>Do this first.</b> It appeared as step one on more parish "
             "pages than any other item. One parish warns that the address "
             "will not be assigned until your front door is in place, so ask "
             "early what their trigger is.")],
    [k.cellp("<b>2</b>"), k.cellp("Sewage approval"),
     k.cellp("The <b>parish health unit</b> — a Louisiana Department of "
             "Health office, not parish government — or a letter from the "
             "public sewer utility."),
     k.cellp("The LHS-47 temporary permit, or written confirmation of public "
             "sewer service. Several parishes will not accept an application "
             "without it.")],
    [k.cellp("<b>3</b>"), k.cellp("Driveway / culvert"),
     k.cellp("Parish public works for a parish road; the state highway "
             "department for any state or US route."),
     k.cellp("On a state route the document is an <b>Access Connection "
             "Permit</b> and there is a residential version of the form. It "
             "asks for culvert diameter, length and material, so have the "
             "site laid out before you apply.")],
    [k.cellp("<b>4</b>"), k.cellp("Flood determination"),
     k.cellp("The parish floodplain manager — in Louisiana usually the same "
             "person who signs your building permit."),
     k.cellp("In a Special Flood Hazard Area expect a <b>proposed</b> "
             "elevation certificate before the permit and a <b>final</b> one "
             "before the certificate of occupancy.")],
    [k.cellp("<b>5</b>"), k.cellp("Legal description"),
     k.cellp("Tax assessor or clerk of court."),
     k.cellp("Several parishes ask for the current parcel listing from the "
             "assessor; the health unit wants a plat with a surveyor's seal "
             "<i>or</i> a clerk of court &ldquo;true copy&rdquo; "
             "certification.")],
    [k.cellp("<b>6</b>"), k.cellp("Utility account"),
     k.cellp("Your electric provider."),
     k.cellp("Unusual outside Louisiana: some parishes want the electrical "
             "provider's account number, or a current utility bill, with the "
             "application itself.")],
]
flow.append(k.ref_table(
    "Pre-permit approvals, in the order they usually run",
    [k.cellp("", bold=True), k.cellp("Approval", bold=True),
     k.cellp("Who", bold=True), k.cellp("Notes", bold=True)],
    rows, [0.35 * inch, 1.25 * inch, 1.75 * inch, CW - 3.35 * inch]))
flow.append(k.cite(
    "Compiled from published requirement lists on the permit pages of "
    "Ouachita, Union, Beauregard, Vernon, Grant, Acadia, Ascension, Caddo, "
    "St. Helena and St. Martin parishes, read September 2026. Every parish "
    "differs in the details — this is the recurring shape, not a universal "
    "list. Confirm yours and write it into LA.4."))

# ------------------------------------------------------------------ during
flow += k.h2("STAGE TWO: THE BUILDING INSPECTIONS")
flow.append(k.body(
    "Louisiana publishes <b>no statewide inspection schedule</b> for a one- "
    "or two-family dwelling, and there is a precise reason for that which is "
    "worth understanding, because it tells you where your schedule actually "
    "comes from."))
flow.append(k.callout(
    "Why there is no state inspection list — and where yours comes from", [
        Paragraph(
            "Louisiana adopts the IRC <b>&ldquo;not including Part "
            "I-Administrative.&rdquo;</b> Part I is IRC Chapter 1, and IRC "
            "Chapter 1 is where <b>R109, Inspections</b> lives, along with "
            "permits, fees and construction documents. So the chapter that "
            "would have given Louisiana a required-inspection list is the one "
            "chapter the state deliberately left out — and the predecessor "
            "statute was explicit that the agency could not add it back.",
            S["body"]),
        Paragraph(
            "Your inspection schedule therefore comes from your parish or "
            "town, under its own administrative ordinance. <b>Ask for the "
            "inspection card or schedule when the permit issues</b> and put "
            "it beside the log at the back of this document. Do not assume "
            "the sequence you used in another state.", S["body"]),
    ]))
flow.append(k.body(
    "Rather than invent a list, here is one parish's <i>published</i> set of "
    "required inspections, which is representative of what a Louisiana "
    "owner-builder should expect to call in."))
flow.append(k.callout(
    "Ouachita Parish's published required inspections", [
        Paragraph(
            "&ldquo;plumbing rough-in / foundation / open wall / electrical "
            "service connection / final for certificate of occupancy.&rdquo; "
            "Read that order carefully — the <b>plumbing rough-in comes "
            "first</b>, because on a slab the drain lines are in the ground "
            "before the foundation is poured. That is the inspection an "
            "owner-builder is most likely to pour concrete over.", S["body"]),
    ]))
flow.append(k.body(
    "Whatever your jurisdiction schedules, the state adds a handful of hard "
    "requirements on top. These four are worth knowing by name."))
flow.append(k.bullet(
    "<b>Your inspector has to physically show up.</b> R.S.&nbsp;37:3737(H) "
    "requires that a properly-licensed inspector conduct all inspections and "
    "<b>&ldquo;be present on site for all inspections other than roofing "
    "inspections, reinspections where that inspector previously visited the "
    "site, and emergency utility reconnection inspections.&rdquo;</b> "
    "Geotagged photographs or video may be accepted for those three "
    "exceptions and nothing else. If someone proposes to inspect your framing "
    "from a phone, that is not what the statute allows."))
flow.append(k.bullet(
    "<b>The roof is separately mandated.</b> R.S.&nbsp;37:3737(I)(2) requires "
    "the jurisdiction to permit and inspect one- and two-family dwellings "
    "&ldquo;for roof construction and reroofing in compliance with the "
    "International Residential Code Chapters 8 and 9 requirements.&rdquo; "
    "This one is not optional anywhere in the state."))
flow.append(k.bullet(
    "<b>The energy tests need certified testers.</b> The adopted energy "
    "provisions require blower-door testing performed by individuals "
    "certified by a nationally recognized organization, and duct-leakage "
    "testing likewise, with the building official directed to accept written "
    "reports from those certified individuals. Book them; there is no visual "
    "alternative."))
flow.append(k.bullet(
    "<b>The insulation certificate is a physical artifact.</b> A Louisiana "
    "insulation certificate posted in a utility area is a code requirement, "
    "and it is the sort of thing a final inspector looks for and an "
    "owner-builder forgets."))
flow.append(k.body(
    "Two more rules are about not covering work up, and they are the ones "
    "that cost money when missed."))
flow.append(k.bullet(
    "<b>Septic: nothing may be covered before the sanitarian verifies it.</b> "
    "The health department's own applicant form says the system "
    "&ldquo;must be inspected by an Office of Public Health sanitarian before "
    "any portion of the system is covered,&rdquo; and asks for "
    "<b>24&nbsp;hours</b> notice ahead of expected completion. Backfilling "
    "early means digging it up."))
flow.append(k.bullet(
    "<b>Third-party reports have to reach the parish.</b> If you are using a "
    "private or contracted inspector, the parish still needs the "
    "documentation in its file. Ouachita states it plainly: applicants using "
    "third-party inspectors &ldquo;must make sure permit office receives "
    "documentation of inspections.&rdquo; Nobody will chase it for you."))
flow.append(k.body(
    "Remember the rule from LA.2 while you build: your inspector works from "
    "<b>the codes in effect when you applied</b>, not the codes current on "
    "the day of the inspection. If a code cycle turns over mid-build, that "
    "sentence is your protection — bring your dated application if it is ever "
    "questioned."))

# ------------------------------------------------------------------ close
flow += k.h2_tight("STAGE THREE: CLOSING OUT", reserve=2.0)
rows = [
    [k.cellp("Final inspections"),
     k.cellp("Building, electrical, plumbing, mechanical — plus the final "
             "elevation certificate if you are in a Special Flood Hazard "
             "Area.")],
    [k.cellp("Septic final approval"),
     k.cellp("The sanitarian's final verification, with the installer present "
             "and the state identification tag turned in to the local health "
             "unit. Until that is done, the health office will not approve "
             "the site for utilities.")],
    [k.cellp("Certificate of occupancy"),
     k.cellp("Issued by the permitting authority. Notify them that the "
             "project is complete <b>before anyone occupies the "
             "building</b> — at least one parish states that requirement "
             "explicitly.")],
    [k.cellp("The recording step most owners miss"),
     k.cellp("On a new-construction mortgage the <b>lender files the "
             "certificate of occupancy in the parish conveyance records</b>, "
             "and the statute puts the duty on you to hand the lender a copy. "
             "Do not treat the CO as the last piece of paper you will ever "
             "need.")],
    [k.cellp("Utility release"),
     k.cellp("Several parishes tie permanent power to the final inspection "
             "and, on a septic site, to the health unit's sign-off. Line the "
             "two up or you will be finished and dark.")],
]
flow.append(k.ref_table(
    "The closing sequence",
    [k.cellp("", bold=True), k.cellp("", bold=True)],
    rows, [1.85 * inch, CW - 1.85 * inch]))
flow.append(k.cite(
    "Certificate of occupancy recording: R.S. 37:3737(E)(1)–(2) — the lender "
    "files the CO in the conveyance records and &ldquo;the owner of the new "
    "residential construction shall provide the lender a copy of the "
    "certificate of occupancy.&rdquo; Septic final approval and utility "
    "release: LDH form SF-10ST and the Office of Public Health applicant "
    "packet. Occupancy notice: Ouachita Parish Police Jury permit office."))

# ------------------------------------------------------------------ log
flow += k.h2("INSPECTION LOG")
flow.append(k.body(
    "Record every inspection as it happens, including the inspector's license "
    "number. In a state where your inspector may be a private firm rather "
    "than a parish employee, that number is what ties the report to a person "
    "the Commission licenses."))
hdr = [k.cellp("Inspection", bold=True), k.cellp("Date called", bold=True),
       k.cellp("Date done", bold=True),
       k.cellp("Inspector / license no.", bold=True),
       k.cellp("Result", bold=True)]
rows = [[k.cellp(a), "", "", "", ""] for a in [
    "Septic — site survey by sanitarian",
    "Plumbing rough-in / under-slab",
    "Foundation",
    "Septic — final verification (before cover)",
    "Framing / open wall",
    "Electrical rough-in",
    "Mechanical rough-in",
    "Insulation",
    "Electrical service connection",
    "Final elevation certificate (flood zone)",
    "Final electrical",
    "Final plumbing",
    "Final mechanical",
    "Final building",
    "Certificate of occupancy issued",
    "",
    "",
]]
flow.append(d.titled_table(
    "Inspections on this project", hdr, rows,
    [CW - 4.75 * inch, 1.0 * inch, 1.0 * inch, 1.75 * inch, 1.0 * inch], S))
flow.append(k.cite(
    "The rows above are a working sequence assembled from published parish "
    "requirements and the health department's septic process. <b>They are not "
    "a statewide schedule</b> — Louisiana does not publish one for dwellings. "
    "Cross out what your jurisdiction does not call for, and write in what it "
    "adds."))

# ------------------------------------------------------------------ sources
flow.append(Spacer(1, 8))
flow.append(k.sources_table([
    ("Enforcement must be by a Commission-licensed inspector",
     "R.S. 37:3737(A)(1)"),
    ("Homeowners exempt under R.S. 37:2157 may hire private inspectors",
     "R.S. 37:3737(A)(1)"),
    ("A private inspector must be contracted with or registered to the "
     "jurisdiction", "R.S. 37:3737(A)(1)"),
    ("A parish may contract enforcement to another entity or a licensed "
     "private inspector", "R.S. 37:3740"),
    ("Inspections use the codes in force on the original application date",
     "R.S. 37:3734"),
    ("No state inspection schedule: IRC Part I-Administrative, which contains "
     "R109, is not adopted", "R.S. 37:3733(A)(3)"),
    ("Inspector must be present on site, with three named exceptions",
     "R.S. 37:3737(H)"),
    ("Roof construction and reroofing must be permitted and inspected",
     "R.S. 37:3737(I)(2)"),
    ("Blower-door and duct-leakage testing by certified individuals; "
     "insulation certificate posted", "LA amendments to 2021 IECC, LAC 17:I.117"),
    ("Lender records the certificate of occupancy; owner supplies the copy",
     "R.S. 37:3737(E)(1)–(2)"),
    ("Nothing covered before the sanitarian verifies; 24 hours notice",
     "LDH form SF-10ST; OPH applicant packet"),
    ("Utilities not approved until final verification and tag returned",
     "OPH applicant packet"),
    ("Representative required-inspection list and third-party documentation "
     "rule", "Ouachita Parish Police Jury permit office"),
    ("Pre-permit routing through the 911 office and parish health unit",
     "Union Parish Police Jury, building permit instructions"),
    ("Residential access connection permit on a state route",
     "Louisiana DOTD, Access Connection Permit Certificate"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "la-permit-kit",
                       "LA.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
