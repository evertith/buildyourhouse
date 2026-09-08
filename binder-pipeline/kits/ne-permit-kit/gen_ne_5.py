#!/usr/bin/env python3
"""NE.5 Forms & Documents Index.

Every document an owner-builder will meet in Nebraska, named as the agency
names it, with what it is, when it happens and where it comes from.

Two negative sections carry real weight here. "What Nebraska does not have"
saves people from applying for things that do not exist — a state building
permit, an owner-builder affidavit, an energy certificate, a general
contractor license. "The one thing you may not do yourself" exists because the
published guides have the well and the septic system backwards.

Verified sources:
  Application for State Electrical Inspection (rev. 3-27-26)   fees; fields
  SED Homeowner Handout (5-22-24)   "Request for State Electrical Inspection
                        with Homeowner Verification"
  SED notice            online system live April 13, 2026; homeowner permits
                        linked by staff
  § 81-2129             the certificate to the utility — no state form
  Title 124 booklet, form 23-017 ver. 02.2026   general permits, system
                        registration form, certification; App. A fees
  § 46-602(1), -606(1), -1224(3), -1241   well registration, fees, well log
  Title 134 ch. 4 § 012.01   variance request
  § 48-2117; DOL page   the contractor registry; ACORD 25
  § 52-135, -137        notice of right to assert a lien; 120 days
  § 76-2,120            seller disclosure; never-occupied exemption
  § 81-15,248(1); Title 124 ch. 9 § 004   owner may not install septic

DELIBERATELY NOT CLAIMED:
  - A form number for any local building or zoning permit. Local; write-in.
  - A state form for the utility certificate. § 81-2129 prescribes none; the
    utility's own paper or the Division's forwarded permit serves.
  - A "Nebraska Energy Code certificate." None exists.
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

FORM_ID = "NE.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Forms & Documents"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document you will meet, named as the agency names it — and the "
    "paper Nebraska never asks you for.")

flow.append(k.disclaimer(
    "Form names and fees were read from the agencies' own current forms in "
    "September 2026. Where no form exists, this document says so rather than "
    "inventing one."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- state docs
flow += k.h2_tight("THE STATE DOCUMENTS", reserve=2.4)
rows = [
    [k.cellp("<b>Request for State Electrical Inspection with Homeowner "
             "Verification</b>"),
     k.cellp("The Division's name for the homeowner permit. Filed \"at or "
             "before commencement\" of wiring, online since April 13, 2026 "
             "(homeowner permits are linked by Division staff after you "
             "register) or on the paper <b>Application for State Electrical "
             "Inspection</b>, rev. 3-27-26. You sign the verification that "
             "you know the NEC and the Act"),
     k.cellp("$75 new service to 400 A + $10 per circuit; homeowner minimum "
             "$100; late $250")],
    [k.cellp("<b>Certificate to the electrical utility</b>"),
     k.cellp(f"Your statement to the power supplier \"that inspection has "
             f"been requested and that the conditions of the installation "
             f"are safe for energization\" ({sec('81-2129')}). <b>No state "
             f"form</b>; the Division forwards a copy of the new-service "
             f"permit to the supplier, and the utility has its own paper. "
             f"Ask the utility what it wants"),
     k.cellp("None")],
    [k.cellp("<b>Approval notice</b>"),
     k.cellp("Optional written approval of the final electrical inspection. "
             "The one third-party record of the wiring your house will ever "
             "have; buy it"),
     k.cellp("$6")],
    [k.cellp("<b>Onsite wastewater general-permit certification and system "
             "registration</b>"),
     k.cellp("In DWEE's Title 124 booklet (form 23-017). The certified "
             "professional, engineer or environmental health specialist "
             "signs the certification, attaches the scaled drawing and the "
             "perc data, and registers the system within 45 days of "
             "completion. You receive a copy"),
     k.cellp("$140; late $150 (46–90 days), $450 (91+)")],
    [k.cellp("<b>Application for Permit</b> (onsite wastewater)"),
     k.cellp("The individual construction and operating permit for a system "
             "the general permit does not cover — plans \"prepared and "
             "properly stamped and signed by a Professional Engineer\""),
     k.cellp("$450")],
    [k.cellp("<b>Water well registration</b>"),
     k.cellp("DWEE's registration form, with the well-log information, "
             "within 60 days of completion — by the licensed driller, or by "
             "you if you drilled it"),
     k.cellp("$200 + $25–$40")],
    [k.cellp("<b>Well log</b>"),
     k.cellp(f"Kept by \"any owner of a water well or a licensed water well "
             f"contractor\" — eighteen listed items ({sec('46-1241')}). Not "
             f"a form you file; a record you keep"),
     k.cellp("None")],
    [k.cellp("<b>Water well variance request</b>"),
     k.cellp("Written, \"at least 10 days prior\" to construction, with a "
             "scaled map showing property lines, structures, utilities and "
             "contamination sources — only if Chart 1 cannot be met "
             f"(Title 134 ch. 4 §{NB}012.01)"),
     k.cellp("Ask")],
    [k.cellp("<b>Contractor registry printout</b> and <b>ACORD 25</b>"),
     k.cellp("The Department of Labor's search result for each trade you "
             "hire, showing its workers' compensation flag — plus the "
             "contractor's own certificate of insurance naming you as "
             "certificate holder"),
     k.cellp("Free")],
]
flow.append(k.ref_table(
    "What the state issues or requires, and what it costs",
    [k.cellp("Document", bold=True), k.cellp("What it is", bold=True),
     k.cellp("Fee", bold=True)],
    rows, [1.7 * inch, CW - 1.7 * inch - 1.35 * inch, 1.35 * inch]))
flow.append(k.cite(
    "Fees from the Application for State Electrical Inspection (rev. "
    "3-27-26), Title 124 Appendix A (effective June 27, 2022) and "
    f"{sec('46-606(1)')} and {sec('46-1224(3)')}. The Division's homeowner "
    f"handout still works its fee example at the pre-April-2026 rates; the "
    f"form governs."))

# ---------------------------------------------------------------- local docs
flow += k.h2_tight("THE LOCAL DOCUMENTS — IF THEY EXIST WHERE YOU ARE",
                   reserve=1.8)
flow.append(k.body(
    "Where a city or county runs a program it issues its own paperwork under "
    "its own names, and there is no statewide vocabulary for it. These are "
    "the ones that exist nearly everywhere they exist at all. Write in what "
    "yours calls them."))
flow += k.check_table(
    "What my jurisdiction calls each document",
    [
        ("<b>County zoning permit</b> for a nonfarm building, with the plans "
         "\"including sanitation, plumbing and sewage disposal\":",
         [("Called", 0.6), ("Issued by", 0.4)]),
        ("<b>Building permit application</b> — and whether there is a "
         "homeowner version and on what conditions:",
         [("Called", 0.6), ("Conditions?", 0.4)]),
        ("<b>Local electrical permit</b>, if my city or county runs its own "
         "program instead of the state:", [("Called", 0.6), ("Issued by", 0.4)]),
        ("<b>Plumbing permit</b>, if inside a city with a plumbing board, and "
         "whether a homeowner may hold it:",
         [("Called", 0.6), ("Homeowner?", 0.4)]),
        ("<b>Driveway or culvert permit</b>:",
         [("Called", 0.6), ("Road authority", 0.4)]),
        ("<b>911 address application</b>:",
         [("Called", 0.6), ("Issued by", 0.4)]),
        ("<b>Floodplain development permit</b>, if in a mapped hazard area:",
         [("Called", 0.6), ("Administrator", 0.4)]),
        ("<b>Certificate of occupancy</b> — ask whether the local program "
         "issues one, because no state rule requires it:",
         [("Answer", 1.0)]),
    ])

# ---------------------------------------------------------------- does not have
flow += k.h2_tight("WHAT NEBRASKA DOES NOT HAVE", reserve=2.2)
flow.append(k.body(
    "Worth knowing because owner-builders arriving from other states budget "
    "for these, and because anyone who tries to sell you one is selling "
    "something that does not exist."))
rows = [
    [k.cellp("<b>A state building permit</b>"),
     k.cellp("None. Permits exist only where a city or county created them "
             f"under {sec('71-6406(7)')}. The state code applies without one")],
    [k.cellp("<b>A general contractor license</b>"),
     k.cellp("None. The Contractor Registration Act is a $40 registration "
             "for people who work on property \"other than their own,\" and "
             f"the Legislature disclaims any endorsement ({sec('48-2102')})")],
    [k.cellp("<b>An owner-builder affidavit</b>"),
     k.cellp("None at state level — there is no exemption to affirm. The "
             "only owner-specific signature is the electrical <b>homeowner "
             "verification</b>. A local program may have its own form")],
    [k.cellp("<b>A state plumber or HVAC license</b>"),
     k.cellp("None. Plumbing licenses are city licenses under city "
             f"ordinances ({sec('18-1901')}); no statewide registry exists. "
             f"HVAC has no license at all; the wiring of the unit is an "
             f"electrical specialty")],
    [k.cellp("<b>A Nebraska Energy Code certificate</b>"),
     k.cellp("None. The code is the unamended 2018 IECC and the duty is "
             f"yours ({sec('81-1622')}). The IECC's own posted certificate "
             f"(R401.3) is a code requirement, not a state form")],
    [k.cellp("<b>A statewide sprinkler requirement</b>"),
     k.cellp("None — IRC R313 is excluded from the state code. A city or "
             f"county may adopt it ({sec('71-6406(2)(c)(iii)')}); check the "
             f"local amendments")],
    [k.cellp("<b>A state certificate of occupancy</b>"),
     k.cellp("None. Local programs may issue one; ask, because a lender may "
             "want it")],
    [k.cellp("<b>A voluntary state inspection</b>"),
     k.cellp("None. Unlike some states, no Nebraska agency can be asked to "
             "inspect a private house against the building code. The "
             "electrical inspection is the only state visit")],
    [k.cellp("<b>A list of counties with building permits</b>"),
     k.cellp("None. No statute requires a county to have a program or to "
             "report one. NE.4 gives you the three-question check")],
]
flow.append(k.ref_table(
    "Nine things that do not exist in Nebraska",
    [k.cellp("", bold=True), k.cellp("The position", bold=True)],
    rows, [2.1 * inch, CW - 2.1 * inch]))

# ---------------------------------------------------------------- the one thing
flow += k.h2_tight("THE ONE THING YOU MAY NOT DO YOURSELF", reserve=2.0)
flow.append(k.body(
    "Nebraska is generous about owner-performed work. You may act as your own "
    "general contractor, wire your own principal residence without a license, "
    "and drill your own well on your own homestead. <b>You may not install "
    "your own septic system</b> — and the published guides have this exactly "
    "backwards, licensing the well and loosening the septic."))
flow.append(k.callout(
    "The two sentences that settle it", [
        Paragraph(f"\"A private onsite wastewater treatment system shall not "
                  f"be sited, laid out, constructed, closed, reconstructed, "
                  f"altered, modified, repaired, inspected, or pumped unless "
                  f"the siting, layout, construction … or pumping is <b>carried "
                  f"out or supervised by</b> either a certified professional "
                  f"…, a professional engineer licensed in Nebraska, or a "
                  f"registered environmental health specialist registered in "
                  f"Nebraska\" ({sec('81-15,248(1)')}). There is no owner "
                  f"exception anywhere in the Act.", S["body"]),
        Paragraph(f"And \"supervised\" does not mean a phone call: \"No person "
                  f"will engage in the siting, layout, construction … of a "
                  f"private onsite wastewater system unless a Master "
                  f"Installer, a Journeyman Installer, a professional "
                  f"engineer, or a registered environmental health specialist "
                  f"who is responsible for such work <b>is physically present "
                  f"at the site where such work is being performed</b> and is "
                  f"supervising the work\" (Title 124 ch. 9 §{NB}004). You may "
                  f"run the excavator beside a Master Installer who stays on "
                  f"site. You may not build it alone, and the professional — "
                  f"not you — registers it. Civil penalty: up to $10,000 per "
                  f"violation per day ({sec('81-15,253')}).", S["body"]),
    ]))
flow.append(k.cite(
    f"Compare the well: \"an individual may construct a water well or install "
    f"and repair pumps and pumping equipment onsite on land owned by him or "
    f"her and used by him or her … as his or her place of abode\" "
    f"({sec('46-1233(2)')}) — to the Title 134 standards, registered by you "
    f"within 60 days ({sec('46-602(1)')})."))

# ---------------------------------------------------------------- lien paper
flow += k.h2_tight("THE LIEN PAPER — THREE DOCUMENTS TO KEEP, ONE TO DEMAND",
                   reserve=2.0)
rows = [
    [k.cellp("<b>Notice of the right to assert a lien</b>"),
     k.cellp(f"Sent to you by a sub or supplier you did not contract with, "
             f"carrying the statutory warning about <b>double liability</b> "
             f"({sec('52-135')}). Date it on receipt; from that day, unpaid "
             f"balances owed to the prime contractor may be reachable")],
    [k.cellp("<b>Lien waiver</b>"),
     k.cellp("Not a statutory form; a signed release you <b>demand</b> from "
             "every trade and supplier with every payment. As your own "
             "general contractor, every trade contracts with you directly, "
             "and the waivers are the whole of your protection")],
    [k.cellp("<b>Recorded construction lien</b>"),
     k.cellp(f"What a claimant records with the register of deeds within "
             f"<b>120 days</b> of last furnishing labor or materials "
             f"({sec('52-137(1)')}); after that it \"does not attach and may "
             f"not be enforced.\" Check the county's records before you "
             f"close a construction loan or sell")],
    [k.cellp("<b>Seller disclosure statement</b>"),
     k.cellp(f"The written statement every seller of residential property "
             f"gives ({sec('76-2,120')}) — except on \"newly constructed "
             f"residential real property which has never been occupied\" "
             f"((6)(k)). Once you have lived in the house, you give it, to "
             f"the best of your knowledge — and you built it")],
]
flow.append(k.ref_table(
    "The Construction Lien Act and the sale",
    [k.cellp("Document", bold=True), k.cellp("What it is and what to do",
                                             bold=True)],
    rows, [1.9 * inch, CW - 1.9 * inch]))
flow.append(k.cite(
    f"As a \"protected party\" — an individual who has residential real "
    f"estate improved which they occupy or intend to occupy "
    f"({sec('52-129(1)(a)')}) — the notice mechanism and the payment cap in "
    f"{sec('52-136')} run in your favor. NE.1 sets them out."))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ne-permit-kit",
                       "NE.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
