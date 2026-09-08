#!/usr/bin/env python3
"""AZ.1 The Code Is Local, the Permit Is Not.

Every Arizona claim in this document was read against its primary source in
September 2026 and is cited on-page. Statutes were read on the Legislature's
own server (azleg.gov, one section per page); the Cochise County Owner-Builder
Amendment from the county's posted ordinance text; the Greenlee County letter
from the county's own site.

Verified sources:
  § 11-861(A)           a county building code is OPTIONAL ("may adopt"); rural
                        or unclassified zones may be exempted from it
  § 11-321(A), (G)      the county building permit is MANDATORY for construction
                        over $1,000; copies to the assessor and Dept. of Revenue
  § 9-467(A)            the city twin of the reporting rule
  § 11-815(B), (C)      zoning permit; class 2 misdemeanor, each day separate
  § 9-802; § 11-864     the adopting ordinance is published in full and filed
                        with the clerk — the authoritative edition statement
  Greenlee County Engineer letter (19 Oct 2012, posted Sept 2026)  "no building
                        codes … Arizona Law requires the County to issue a
                        building permit"
  Cochise County Owner-Builder Amendment, Secs. 1–2, 4–7, 9, 12, 15–16, 21–22,
                        27; county program page  the ≥ 4-acre opt-out
  Coconino County AMMP page   the ≤ 600 sq ft opt-out
  § 32-1121(A)(5)       the exemption, verbatim; "offering"; prima facie;
                        owner-occupant carve-out; "rent" includes "labor"
  § 32-1121(A)(6)       the developer route — a licensed GC, named in the sales
                        documents
  § 32-1121(A)(11)      wage employees of an exempt owner
  § 32-1121(A)(14), (D) the casual-work exemption and its two exclusions; gas
                        and fire-safety work
  § 32-1101(A)(3), (A)(10)(b), (B)   "contractor"; the owner is NOT a
                        residential contractor; only contractors are regulated
  § 32-1121(B)          no separate license for in-scope trade work
  § 32-1151; § 32-1164(A)(2), (B); § 32-1153; § 33-981(C)   the crime and its
                        civil teeth
  § 32-1169(A), (B)     the signed exemption statement on every application;
                        unsworn falsification (§ 13-2704)
  § 32-1158(A), (B), (C)   contract contents over $1,000
  § 32-1132(B)(1), (C)  recovery-fund claimant; licensed on three dates
  § 32-1162(A)          two-year complaint window from occupancy
  § 33-1002(A)(2), (B), (C)   owner-occupant; no lien without a direct written
                        contract; waiver void
  § 33-981(B)           the contractor as the owner's agent
  § 33-992.01(B), (C)   the preliminary twenty-day notice
  § 23-901(6)(b); § 23-902(A), (B), (D); § 23-961(N)   workers' compensation
  Chandler, Tucson, Goodyear building pages   "rental … licensed contractor"

DELIBERATELY NOT CLAIMED, and why:
  - "Once per 24 months," "once per five years," "must live in it two years."
    None is in § 32-1121. The five-year figure is Cochise County's local limit
    on its opt-out permit and is printed only as that.
  - A homeowner workers'-compensation bright line. § 23-901(6)(b) is a two-part
    fact test; no statute exempts a homeowner by name.
  - Which counters demand an ROC-signed exemption verification under
    § 32-1169(A). "May require" — not verified for any jurisdiction.
  - Which version of § 32-1121 a court would apply. azleg.gov publishes two
    (L19 Ch. 140 and Ch. 145); paragraphs (A)(5), (A)(6) and (A)(11) differ by
    one word ("such a project" / "such project"; "shall" / "must") and in no
    substance. The kit cites the paragraph without a version.
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
ars = k.ars
NB = k.NB
CITE = k.CITE_COL

FORM_ID = "AZ.1"
FORM_TITLE = "The Code Is Local, the Permit Is Not"
TOPIC = "Who Enforces What"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What is statewide in Arizona and what is not — the permit no county may "
    "waive, the exemption, the deed you record, and the statement you sign.")

flow.append(k.disclaimer(
    "Statute text was read on the Arizona Legislature's own site in September "
    "2026, the Cochise County amendment from the county's posted ordinance, "
    "and the no-code letter from Greenlee County's own site. Where a sentence "
    "is quoted, it is quoted verbatim."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION", reserve=2.0)
flow.append(k.body(
    "Arizona is the state where <b>the code is local but the permit is "
    "not</b> — and where the owner-builder rules everyone quotes as \"varies "
    "by jurisdiction\" are, at the state level, fixed by four sections of the "
    "Revised Statutes."))
rows = [
    [k.cellp("Do you need a license to build your own house?"),
     k.cellp(f"<b>No.</b> An owner who improves their own property "
             f"\"themselves, with their own employees or with duly licensed "
             f"contractors\" is exempt from the contractor chapter, if the "
             f"house is for the owner's occupancy and \"not intended for sale "
             f"or for rent\" ({ars('32-1121(A)(5)')}). The definition of "
             f"residential contractor expressly excludes you "
             f"({sec('32-1101(A)(10)(b)')})")],
    [k.cellp("Is there a statewide building code?"),
     k.cellp(f"<b>No.</b> A county \"may\" adopt one and may exempt rural "
             f"zones from it ({ars('11-861(A)')}); a city adopts one by "
             f"reference in a published ordinance ({sec('9-802')}). No state "
             f"agency adopts a residential, energy or electrical code")],
    [k.cellp("Do you need a building permit?"),
     k.cellp(f"<b>Yes, everywhere.</b> Every board of supervisors \"shall "
             f"require a building permit for any construction of a building "
             f"… exceeding a cost of $1,000\" ({ars('11-321(A)')}); inside "
             f"a city, the city's own ordinance governs. A \"no-permit "
             f"county\" does not exist. What varies is whether the permit "
             f"carries a code")],
    [k.cellp("So what is a \"no-code county\"?"),
     k.cellp("<b>Greenlee.</b> Its engineer: \"Greenlee County has adopted "
             "no building codes … With some exceptions, Arizona Law "
             "requires the County to issue a building permit.\" Two other "
             "counties — Cochise on parcels of four acres or more, Coconino "
             "under 600&#160;sq&#160;ft — let you opt out of plan review "
             "and inspection while keeping the permit")],
    [k.cellp("May you do your own wiring and plumbing?"),
     k.cellp(f"<b>At the state level, yes.</b> Arizona licenses contractors, "
             f"not tradespeople, and \"only contractors … are licensed and "
             f"regulated by this chapter\" ({ars('32-1101(B)')}). Whether "
             f"your city issues you the permit is local — and every site "
             f"read draws the line at rentals")],
    [k.cellp("What is the one-year rule, really?"),
     k.cellp(f"Selling, renting, <b>or offering</b> the house within a year "
             f"of completion is \"prima facie evidence\" you built for sale "
             f"— rebuttable, and <b>switched off entirely</b> for an "
             f"owner-occupant under {sec('33-1002')}: deed recorded before "
             f"construction, 30 days' residence after")],
    [k.cellp("What do you sign?"),
     k.cellp(f"A statement, on every permit application, of the exemption "
             f"you claim <b>and the name and license number of every "
             f"licensed contractor you will use</b> "
             f"({ars('32-1169(A)')}). A false one is unsworn falsification "
             f"({sec('32-1169(B)')})")],
    [k.cellp("What about septic and the well?"),
     k.cellp(f"Both statewide. A septic system runs on an ADEQ general "
             f"permit administered by your county ({ars('49-241(B)(9)')}); "
             f"a well needs a notice of intent to ADWR before drilling "
             f"({sec('45-454(G)')}). You may drill your own exempt well on a "
             f"no-fee single well license, after an exam "
             f"({sec('45-595(D)')}). AZ.2")],
]
flow.append(k.ref_table(
    "The Arizona position at a glance",
    [k.cellp("Question", bold=True), k.cellp("Arizona's answer", bold=True)],
    rows, [2.2 * inch, CW - 2.2 * inch]))
flow.append(k.cite(
    "Arizona Revised Statutes Title 9, Chapter 7 (municipal codes and "
    "licensing time frames); Title 11, Chapters 2, 6 and 11 (county permits, "
    "codes and licensing); Title 32, Chapter 10 (Registrar of Contractors); "
    "Title 33, Chapter 7 (liens); Title 45 and Title 49 (wells; aquifer "
    "protection). All read September 2026."))

# ---------------------------------------------------------------- no code / permit
# 1.6in: prose follows, not a table; the heading needs only its first
# paragraph, and 2.2in was throwing away a third of the previous page.
flow += k.h2_tight("FIRST — NO STATEWIDE CODE, ONE STATEWIDE PERMIT",
                   reserve=1.3)
flow.append(k.body(
    f"The county statute is permissive about the <b>code</b>: \"In any county "
    f"that has adopted zoning pursuant to this chapter, the board of "
    f"supervisors <b>may</b> adopt and enforce, for the unincorporated areas "
    f"of the county so zoned, a building code and other related codes … "
    f"<b>except that the board may authorize that areas zoned rural or "
    f"unclassified may be exempt from the provisions of the code "
    f"adopted</b>\" ({ars('11-861(A)')}). Three things follow. A county "
    f"building code is optional. A county may carve rural zones out of it — "
    f"the statutory root of both county opt-outs below. And it is conditioned "
    f"on zoning. The same statute is not permissive about the <b>permit</b>:"))
flow.append(k.callout_long(
    f"Arizona Revised Statutes {sec('11-321(A)')} — the permit no county may "
    f"waive", [
        Paragraph("\"Except in those cities and towns that have an ordinance "
                  "relating to the issuance of building permits, the board "
                  "of supervisors <b>shall require a building permit for any "
                  "construction of a building or an addition to a building "
                  "exceeding a cost of $1,000</b> within its jurisdiction. "
                  "The building permit shall be filed with the board of "
                  "supervisors or its designated agent.\"", S["body"]),
        Paragraph(f"And the permit is a tax event. One copy of every permit "
                  f"goes to the county assessor and one to the Department of "
                  f"Revenue, with the permit number, issue date and parcel "
                  f"number; both are notified again on the certificate of "
                  f"occupancy, completion, expiration or cancellation "
                  f"({sec('11-321(G)')}; {sec('9-467(A)')} for cities). "
                  f"\"Nobody will know\" is not an Arizona option.",
                  S["body"]),
        Paragraph(f"The zoning statute adds its own permit and its own "
                  f"penalty: \"it is unlawful to erect, construct, "
                  f"reconstruct, alter or use any building or other structure "
                  f"within a zoning district covered by the ordinance without "
                  f"first obtaining a building permit from the inspector,\" "
                  f"on \"a sketch of the proposed construction containing "
                  f"sufficient information for the enforcement of the zoning "
                  f"ordinance\" ({sec('11-815(B)')}). Violation is a "
                  f"<b>class 2 misdemeanor</b> and \"Each day … is a "
                  f"separate offense\" ({sec('11-815(C)')}); any neighboring "
                  f"owner \"who is specially damaged\" may sue to abate "
                  f"({sec('11-815(H)')}).", S["body"]),
    ]))
flow.append(Spacer(1, 4))
flow.append(k.body(
    "<b>So the correct sentence is:</b> every Arizona county must issue a "
    "building permit for a house. What differs is whether that permit "
    "carries a building <i>code</i> — plan review and inspections — or is "
    "only a zoning, floodplain and assessor permit. Greenlee County's own "
    "engineer says it exactly this way:"))
flow.append(k.callout(
    "Greenlee County — the one county with no code, in its own words", [
        Paragraph("From the County Engineer's letter posted on the county's "
                  "Planning &amp; Zoning page (dated 19&#160;October 2012, "
                  "still posted September 2026): \"Currently, Greenlee "
                  "County has adopted no building codes. Because we have no "
                  "codes, Greenlee County has not determined and does not "
                  "recommend building loads, does not review plans, does not "
                  "inspect construction, or issue a Certificate of "
                  "Occupancy. I suggest that owners contract for inspections "
                  "and use a conservative Building Code. <b>With some "
                  "exceptions, Arizona Law requires the County to issue a "
                  "building permit. We issue a building permit at no cost "
                  "when a Zoning Use Permit and Floodplain Permit are "
                  "issued.</b>\"", S["body"]),
        Paragraph("That last sentence is §&#160;11-321(A) in practice. No "
                  "code county is not no permit county — and every "
                  "statewide rule in this kit, from the septic setbacks to "
                  "the exemption statement, applies in Greenlee exactly as "
                  "it applies in Phoenix.", S["body"]),
    ]))
flow.append(Spacer(1, 4))
flow.append(k.body(
    f"<b>Where the edition lives.</b> A city enacts a code by reference, but "
    f"\"the adopting ordinance shall be published in full\" and filed with "
    f"the clerk ({ars('9-802')}); a county's likewise ({sec('11-864')}). The "
    f"authoritative statement of which code edition binds your lot is "
    f"<b>the adopting ordinance on file with the clerk</b>, not the building "
    f"department's web page. Ask for the number; AZ.2 has the line."))

# ---------------------------------------------------------------- opt-outs
flow += k.h2_tight("THE TWO COUNTY OPT-OUTS — FROM INSPECTION, NOT FROM THE "
                   "PERMIT", reserve=2.4)
flow.append(k.body(
    "Both rest on the rural-zone exemption in §&#160;11-861(A). Both keep the "
    "permit. Both leave a mark on the title. Read from the counties' own "
    "ordinance text and program pages, September 2026."))
rows = [
    [k.cellp("<b>Who qualifies</b>"),
     k.cellp("A \"Rural Residential Owner-Builder\" — the §&#160;32-1121(A)(5) "
             "definition, verbatim — on a parcel \"<b>at least four-acres</b>\" "
             "in a zoning district \"with a minimum parcel size of four-acres "
             "per dwelling unit\" (Sec. 1). Usable \"<b>once in every five "
             "years</b>\" for a dwelling on all of that owner's "
             "unincorporated Cochise parcels (Sec. 2)"),
     k.cellp("Zoning AR or G; parcel of at least 2&#160;acres; "
             "<b>600&#160;sq&#160;ft</b> interior or less; one story; an "
             "alternative method or material; owner-occupied and not rented "
             "or sold for one year")],
    [k.cellp("<b>What you skip</b>"),
     k.cellp("<b>Option 1</b>: full plan review, but \"only limited Building "
             "Code inspections dealing with the trade areas of Mechanical, "
             "Electrical, Plumbing and Fire Prevention.\" <b>Option 2</b>: "
             "\"no building code inspections … no construction plans are "
             "required to be submitted or reviewed\" (Sec. 5). Plans may be "
             "hand-drawn (Sec. 9)"),
     k.cellp("\"Projects participating in this program will not be required "
             "to apply for a traditional building permit or undergo plan "
             "review or building inspections\"")],
    [k.cellp("<b>What survives</b>"),
     k.cellp("\"By statute, this exemption does not exempt owner-builders "
             "from state, county building codes, or fire-district adopted "
             "fire codes and regulations regarding smoke detectors, nor … "
             "from health regulations regarding wastewater treatment "
             "systems\" (Sec. 1); \"all permits required under State law "
             "and County ordinance\" (Sec. 7). Near a military airport, "
             "sound attenuation under §&#160;28-8482(B) (Sec. 4(B))"),
     k.cellp("Signed affidavits of electrical, mechanical, fire and "
             "plumbing compliance at completion; the statewide septic and "
             "well rules apply regardless (AZ.2)")],
    [k.cellp("<b>The mark on the title</b>"),
     k.cellp("\"Each time a permit is issued pursuant to this amendment … a "
             "notice that a permit has been issued pursuant to the "
             "provisions of this article <b>shall be recorded with the "
             "County Recorder</b>\" (Sec. 6). Use of the amendment \"would "
             "be considered a factor against a rezoning to a higher "
             "density\" (Sec. 27)"),
     k.cellp("A recorded <b>Notice of Disclosure Statement</b>")],
    [k.cellp("<b>Certificate of occupancy</b>"),
     k.cellp("Option 1: a \"<b>conditioned</b> Certificate of Occupancy\" "
             "(Sec. 16). Option 2: the county page states it is \"not "
             "eligible for a Certificate of Occupancy\""),
     k.cellp("None")],
    [k.cellp("<b>Details</b>"),
     k.cellp("Permit life <b>36 months</b> plus one 12-month extension "
             "(Sec. 12); inspections requested <b>24 hours</b> ahead "
             "(Sec. 15); \"Potable water shall be available\" (Sec. 22); no "
             "dwelling \"shall be required to be connected to a source of "
             "electrical power, or wired\" (Sec. 21)"),
     k.cellp("A cabin program, not a house program — the 600-sq-ft cap "
             "decides that")],
]
flow.append(k.ref_table(
    "Cochise County Owner-Builder Amendment · Coconino County Alternative "
    "Methods and Materials Permit",
    [k.cellp("", bold=True), k.cellp("Cochise (≥ 4 acres)", bold=True),
     k.cellp("Coconino (≤ 600 sq ft)", bold=True)],
    rows, [1.3 * inch, (CW - 1.3 * inch) * 0.6, (CW - 1.3 * inch) * 0.4]))
flow.append(k.cite(
    "Cochise County, \"Amendment to the Cochise County Building Safety Code "
    "for Rural Residential Owner-Built Dwellings and Accessory Structures\" "
    "(county PDF) and its Owner-Builder Amendment page; Coconino County, "
    "Alternative Methods and Materials Permit page. <b>Three consequences "
    "before you choose.</b> A lender or buyer will ask for the certificate "
    "of occupancy, and under Option 2 or the AMMP it cannot be obtained "
    "later. The recorded notice follows the title forever. And the one-year "
    "clock in §&#160;32-1121(A)(5) runs from \"completion or issuance of a "
    "certificate of occupancy\" — where none issues, the only start date is "
    "completion, a fact you should document the day it happens."))

# ---------------------------------------------------------------- exemption
flow += k.h2_tight("THE EXEMPTION — A.R.S. § 32-1121(A)(5), VERBATIM",
                   reserve=2.4)
flow.append(k.body(
    "One paragraph carries the whole owner-builder position. Every summary "
    "of it that circulates leaves out at least one of its five moving parts, "
    "so here it is whole, with the parts marked."))
flow.append(k.callout_long(
    "The chapter does not apply to —", [
        Paragraph("\"Owners of property who improve such property or who "
                  "build or improve structures or appurtenances on such "
                  "property and who do the work <b>themselves, with their "
                  "own employees or with duly licensed contractors</b>, if "
                  "the structure, group of structures or appurtenances, "
                  "including the improvements thereto, are intended for "
                  "occupancy <b>solely by the owner</b> and are not intended "
                  "for occupancy by members of the public as the owner's "
                  "employees or business visitors and the structures or "
                  "appurtenances are <b>not intended for sale or for "
                  "rent</b>.", S["body"]),
        Paragraph("In all actions brought under this chapter, <b>except an "
                  "action against an owner-occupant as defined in section "
                  "33-1002</b>, proof of the sale or rent <b>or the offering "
                  "for sale or rent</b> of any such structure by the "
                  "owner-builder within one year after completion or "
                  "issuance of a certificate of occupancy is <b>prima facie "
                  "evidence</b> that such a project was undertaken for the "
                  "purpose of sale or rent. For the purposes of this "
                  "paragraph, 'sale' or 'rent' includes any arrangement by "
                  "which the owner receives compensation in <b>money, "
                  "provisions, chattels or labor</b> from the occupancy or "
                  "the transfer of the property or the structures on the "
                  "property.\"", S["body"]),
    ]))
flow.append(Spacer(1, 4))
rows = [
    [k.cellp("<b>1. The trigger is \"offering.\"</b>"),
     k.cellp("Sale, rent, \"or the offering for sale or rent.\" Listing the "
             "house, or advertising it for rent, inside the year is enough "
             "to raise the presumption — whether or not anyone bites")],
    [k.cellp("<b>2. The clock has two possible starts.</b>"),
     k.cellp("\"Completion or issuance of a certificate of occupancy.\" Where "
             "no CO will ever issue — Greenlee, Cochise Option 2, the "
             "Coconino AMMP — the only start is \"completion,\" a fact "
             "question you should date and document yourself")],
    [k.cellp("<b>3. It is \"prima facie evidence\" — rebuttable.</b>"),
     k.cellp("Not a bar on selling. It shifts the burden onto you to show "
             "you did not build for sale: a mortgage in your name, "
             "utilities, voter registration, a genuine reason for the move. "
             "Survivable with records; miserable without them")],
    [k.cellp("<b>4. It is switched off for an owner-occupant.</b>"),
     k.cellp("\"Except an action against an owner-occupant as defined in "
             "section 33-1002.\" That definition — a recorded deed before "
             "construction and 30 days' residence in the year after — is the "
             "next section, and it is the same status that blocks liens")],
    [k.cellp("<b>5. \"Rent\" includes \"labor.\"</b>"),
     k.cellp("Letting a helper live in the house in exchange for work is "
             "compensation \"from the occupancy,\" which the statute calls "
             "rent. This is the trap every state hides somewhere; Arizona "
             "puts it in the definition")],
]
flow.append(k.ref_table(
    "Five things the paragraph actually says",
    [k.cellp("The part", bold=True), k.cellp("What it does", bold=True)],
    rows, [2.35 * inch, CW - 2.35 * inch]))
flow.append(k.cite(
    "<b>And three things it does not say.</b> There is no \"once per 24 "
    "months\" rule, no \"once per five years\" rule, and no \"must live in it "
    "two years\" rule anywhere in §&#160;32-1121. The five-year figure is "
    "Cochise County's local limit on its opt-out permit and nothing else; the "
    "24-month figure appears on at least one municipal FAQ and has no "
    "statutory source. <b>The developer route is separate</b>: an owner "
    "building \"for the purpose of sale or rent\" is exempt only by "
    "contracting the whole project with a licensed general contractor whose "
    "\"names and license numbers shall be included in all sales documents\" "
    f"({ars('32-1121(A)(6)')}). There is no owner-as-general-contractor route "
    "to a spec house in Arizona."))

# ---------------------------------------------------------------- off-switch
flow += k.h2_tight("THE OFF-SWITCH — RECORD THE DEED, MOVE IN", reserve=2.4)
flow.append(k.body(
    "The phrase \"owner-occupant as defined in section 33-1002\" is the most "
    "valuable cross-reference in the chapter, because §&#160;33-1002 is the "
    "mechanics' lien statute. Qualify under it and two things happen at "
    "once: the one-year presumption cannot be used against you, and no "
    "subcontractor or supplier can lien your house."))
flow.append(k.callout_long(
    f"Arizona Revised Statutes {sec('33-1002')} — who is an owner-occupant, "
    f"and what it buys", [
        Paragraph("An \"owner-occupant\" is a natural person who \"(a) Prior "
                  "to commencement of the construction … holds legal or "
                  "equitable title to the dwelling by a deed or contract for "
                  "the conveyance of real property <b>recorded with the "
                  "county recorder</b> … and (b) Resides or intends to reside "
                  "in the dwelling <b>at least thirty days during the "
                  "twelve-month period immediately following completion</b> "
                  "… and does not intend to sell or lease the dwelling to "
                  "others\" ((A)(2)).", S["body"]),
        Paragraph("Evidence of intent may be \"The placing of his or her "
                  "personal belongings and furniture in the dwelling\" and "
                  "\"Occupancy either by the person or members of his or her "
                  "family.\"", S["body"]),
        Paragraph("\"No lien provided for in this article shall be allowed or "
                  "recorded by the person claiming a lien against the "
                  "dwelling of a person who became an owner-occupant prior to "
                  "the construction … <b>except by a person having executed "
                  "in writing a contract directly with the "
                  "owner-occupant</b>\" ((B)). Any waiver of the section "
                  "\"is void\" ((C)).", S["body"]),
    ]))
flow.append(Spacer(1, 4))
flow.append(k.body(
    "<b>Read the two conditions as instructions.</b> The deed or purchase "
    "contract must be <i>recorded</i>, in your own name as a natural person, "
    "before the first shovel — an LLC or a trust is not a natural person, "
    "and a deed recorded a week into the footings misses the definition by a "
    "week. Then live in the house for thirty days within the year after it "
    "is finished. Do those two things and the one-year rule is not a rule "
    "about you."))
rows = [
    [k.cellp("<b>Who can lien the house</b>"),
     k.cellp("Only \"a person having executed in writing a contract directly "
             "with the owner-occupant.\" Your electrician's supplier, your "
             "framer's sub, the lumberyard your plumber uses — none of them, "
             "unless you signed with them yourself. Outside the shield, "
             "every contractor \"is the agent of the owner for the purposes "
             "of this article, and the owner shall be liable for the "
             "reasonable value of labor or materials furnished to his "
             "agent\" — which is how a sub's supplier reaches an owner who "
             "is not an owner-occupant"),
     k.cellp(f"{ars('33-1002(B)')}; {sec('33-981(B)')}")],
    [k.cellp("<b>The paper that arrives anyway</b>"),
     k.cellp("\"Except for a person performing actual labor for wages, every "
             "person who furnishes labor, professional services, materials "
             "… shall, as a necessary prerequisite to the validity of any "
             "claim of lien, serve the owner … with a written preliminary "
             "twenty day notice,\" within 20 days of first furnishing. Keep "
             "every one — the file is your lien ledger"),
     k.cellp(f"{ars('33-992.01(B)')}, (C)")],
    [k.cellp("<b>The rule for your contracts</b>"),
     k.cellp("The choice of who you sign a direct written contract with is "
             "the choice of who can lien your house. Sign directly with the "
             "trades you hire; let each trade buy its own materials and hire "
             "its own help; and collect a signed lien waiver at every "
             "payment regardless"),
     k.cellp("Kit rule")],
]
flow.append(k.ref_table(
    "The lien shield, worked",
    [k.cellp("", bold=True), k.cellp("What the statute says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.55 * inch, CW - 1.55 * inch - CITE, CITE]))

# ---------------------------------------------------------------- who may help
flow += k.h2_tight("WHO MAY HELP YOU — THREE LAWFUL CATEGORIES AND ONE CRIME",
                   reserve=2.4)
flow.append(k.body(
    "The paragraph allows the work to be done \"themselves, with their own "
    "employees or with duly licensed contractors.\" That is the whole list. "
    "The rest of the chapter fills in the edges, and the edges are where "
    "owner-builders get hurt."))
rows = [
    [k.cellp("<b>Yourself</b>"),
     k.cellp("Any part of the work, including the gas connection and the "
             "fire-safety wiring that a helper may not touch (below)"),
     k.cellp(ars("32-1121(A)(5)"))],
    [k.cellp("<b>Your wage employees</b>"),
     k.cellp("The chapter does not apply to \"Any person who engages in the "
             "activities regulated by this chapter, as an employee of an "
             "exempt property owner or as an employee with wages as the "
             "person's sole compensation.\" A helper paid <b>wages</b> is "
             "lawful. A helper paid by the job, by a share of the work, or "
             "in kind is not an employee — and \"in kind\" includes a place "
             "to sleep (see part 5 of the exemption)"),
     k.cellp(ars("32-1121(A)(11)"))],
    [k.cellp("<b>Licensed contractors</b>"),
     k.cellp("Verify at the Registrar: the recovery fund covers you only if "
             "the contractor was licensed on \"1. The date that the "
             "underlying contract was signed. 2. The date that the first "
             "payment was made. 3. The date that the underlying work first "
             "commenced\""),
     k.cellp(ars("32-1132(C)"))],
    [k.cellp("<b>Not the \"casual work\" helper</b>"),
     k.cellp("Unlicensed work under $1,000 \"of a casual or minor nature\" "
             "is exempt — but \"This exemption does not apply: (a) In any "
             "case in which the performance of the work requires a local "
             "building permit. (b) In any case in which the work or "
             "construction is only a part of a larger or major operation.\" "
             "A house build is both"),
     k.cellp(ars("32-1121(A)(14)"))],
    [k.cellp("<b>Never gas or fire-safety work by a non-employee</b>"),
     k.cellp("The casual and handyman exemptions never reach \"All fire "
             "safety and mechanical, electrical and plumbing work that is "
             "done in connection with fire safety installation\" — "
             "hardwired or interconnected smoke alarms and sprinklers — or "
             "\"All work done … that involves connecting to any supply of "
             "natural gas, propane or other petroleum or gaseous fuel.\" You "
             "may do it; a licensed contractor may; a day-rate helper "
             "may not"),
     k.cellp(ars("32-1121(D)"))],
]
flow.append(k.ref_table(
    "The three lawful categories, and the two that look lawful and are not",
    [k.cellp("Who", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.55 * inch, CW - 1.55 * inch - CITE, CITE]))
flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "The crime — and who it falls on", [
        Paragraph(f"\"It is unlawful for any person … to engage in the "
                  f"business of, submit a bid … act or offer to act in the "
                  f"capacity of or purport to have the capacity of a "
                  f"contractor without having a contractor's license … "
                  f"<b>Evidence of securing a permit from a governmental "
                  f"agency or the employment of a person on a construction "
                  f"project shall be accepted in any court as prima facie "
                  f"evidence of existence of a contract</b>\" "
                  f"({ars('32-1151')}).", S["body"]),
        Paragraph(f"Contracting without a license is a "
                  f"<b>class 1 misdemeanor</b> with a fine \"not less than "
                  f"one thousand dollars\" for a first offense and \"not "
                  f"less than two thousand dollars\" thereafter "
                  f"({sec('32-1164(A)(2)')}, (B)). An unlicensed contractor "
                  f"cannot sue you to collect ({sec('32-1153')}) and "
                  f"\"shall not have the lien rights\" ({sec('33-981(C)')}).",
                  S["body"]),
        Paragraph(f"The chapter penalizes the unlicensed <i>contractor</i>, "
                  f"not the owner who hired one: \"Only contractors as "
                  f"defined in this section are licensed and regulated by "
                  f"this chapter\" ({ars('32-1101(B)')}). Your exposure is "
                  f"practical — no recovery fund, no Registrar complaint, "
                  f"and, if the helper was not a wage employee, a workers' "
                  f"compensation and injury problem that is entirely yours.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- trades
flow += k.h2_tight("ARIZONA LICENSES CONTRACTORS, NOT TRADESPEOPLE",
                   reserve=2.4)
flow.append(k.body(
    f"A \"contractor\" is anyone who \"for compensation\" builds, alters or "
    f"repairs a structure or does \"any part thereof,\" including one who "
    f"\"Connect[s] such a structure or improvements to utility service lines "
    f"and metering devices and the sewer line\" and who \"Provide[s] "
    f"mechanical or structural service\" ({ars('32-1101(A)(3)')}). Then the "
    f"sentence that settles the do-it-yourself question at the state level: "
    f"\"Only contractors as defined in this section are licensed and "
    f"regulated by this chapter\" ((B)). And the definition of residential "
    f"contractor \"Does not include an owner making improvements to the "
    f"owner's property pursuant to section 32-1121, subsection A, paragraph "
    f"5\" ({sec('32-1101(A)(10)(b)')})."))
flow.append(k.body(
    "Title 32 has one construction chapter — Chapter 10, Contractors — and "
    "no chapter for electricians, plumbers or HVAC technicians as "
    "individuals; trade competence is a matter for the licensed entity's "
    f"qualifying party ({sec('32-1101(A)(8)')}). <b>So owner-occupant "
    "electrical and plumbing is not a \"varies locally\" question at the "
    "state level.</b> The local variable is whether your city or county "
    "will <i>issue</i> a homeowner the trade permit, and the jurisdictions' "
    "own sites answer it the same way every time:"))
rows = [
    [k.cellp("<b>Chandler</b>"),
     k.cellp("The owner-applicant may perform the work; \"If you own a home "
             "that you lease or rent to others, a licensed contractor is "
             "required\"")],
    [k.cellp("<b>Tucson</b>"),
     k.cellp("An Owner/Builder Affidavit is required; \"Rental units are "
             "considered commercial property and all commercial permits "
             "require a licensed contractor\"")],
    [k.cellp("<b>Goodyear</b>"),
     k.cellp("\"If you own the house and live in it, you do not need to hire "
             "Licensed Contractors … If you own the house and rent it out, "
             "Licensed Contractors are required\"")],
]
flow.append(k.ref_table(
    "Three cities, one line — from their own building pages, September 2026",
    [k.cellp("City", bold=True), k.cellp("What it says", bold=True)],
    rows, [1.3 * inch, CW - 1.3 * inch]))
flow.append(k.cite(
    "That line is §&#160;32-1121(A)(5)'s \"not intended … for rent,\" applied "
    "at the counter. No city site read for this kit limits homeowner "
    "electrical permits to particular tasks; the limit is the building's use. "
    "Whether any Arizona city licenses tradespeople by its own ordinance was "
    "not verified for all 91 municipalities — none of the twenty read "
    "mentions one — so ask, in writing, before you assume."))

# ---------------------------------------------------------------- § 32-1169
flow += k.h2_tight("THE STATEMENT YOU SIGN — A.R.S. § 32-1169", reserve=2.4)
flow.append(k.body(
    "Every summary that says Arizona has \"no statewide owner-builder form\" "
    "is right about the form and wrong about the thing that matters. The "
    "<i>form</i> is local. The <i>content</i> is statutory, it is on every "
    "building-permit application in the state, and a false one is a crime."))
flow.append(k.callout_long(
    f"Arizona Revised Statutes {sec('32-1169')}, verbatim", [
        Paragraph("\"A. Each county, city or other political subdivision or "
                  "authority of this state … that requires the issuance of a "
                  "building permit as a condition precedent to the "
                  "construction … of a building … for which a license is "
                  "required under this chapter, as part of the application "
                  "procedures which it uses, <b>shall require that each "
                  "applicant for a building permit file a signed statement "
                  "that the applicant is properly licensed</b> to perform the "
                  "work described in the permit under this chapter with the "
                  "applicant's license number. <b>If the applicant purports "
                  "to be exempt from the licensing requirements of this "
                  "chapter, the statement shall contain the basis of the "
                  "asserted exemption and the name and license number of any "
                  "general, mechanical, electrical or plumbing contractor who "
                  "will be employed on the work.</b> The local issuing "
                  "authority may require from the applicant a statement "
                  "signed by the registrar to verify any purported "
                  "exemption.", S["body"]),
        Paragraph("B. The filing of an application containing false or "
                  "incorrect information concerning an applicant's "
                  "contractor's license with the intent to avoid the "
                  "licensing requirements of this chapter is <b>unsworn "
                  "falsification pursuant to section 13-2704</b>.\"",
                  S["body"]),
    ]))
flow.append(Spacer(1, 4))
flow.append(k.bullet(
    "<b>The \"Owner/Builder Affidavit,\" \"Owner-Builder Declaration,\" "
    "\"Owner Builder Form\" and \"verification\" your city hands you are all "
    "the same thing</b> — that jurisdiction's implementation of (A). Twelve "
    "of the jurisdictions read name one (AZ.5 lists them); Maricopa County's "
    "FAQ cites the section itself: \"Written documentation of an Arizona "
    "licensed contractor or owner-builder classification is required for "
    "all building permits per state law. Refer to ARS 11-1605, 32-1121, "
    "32-1151, and 32-1169.\""))
flow.append(k.bullet(
    "<b>You must know your licensed subs at application, not after.</b> The "
    "statement names \"any general, mechanical, electrical or plumbing "
    "contractor who will be employed on the work,\" with license numbers. "
    "AZ.2 puts that list before the permit application in the checklist."))
flow.append(k.bullet(
    "<b>Ask whether the counter wants the Registrar's signature.</b> The "
    "issuing authority \"may require … a statement signed by the registrar to "
    "verify any purported exemption.\" Which counters do was not verified for "
    "any jurisdiction; if yours does, get it first."))
flow.append(k.bullet(
    "<b>Weigh the two rules by their teeth.</b> The one-year sale rule is "
    "civil and rebuttable. A false §&#160;32-1169 statement is unsworn "
    "falsification — a criminal offense. Naming a licensed sub you do not "
    "intend to use, or claiming the exemption for a house you mean to rent, "
    "is the second kind."))

# ---------------------------------------------------------------- hiring
flow += k.h2_tight("WHEN YOU HIRE — THE CONTRACT, THE FUND, AND THE TWO-YEAR "
                   "WINDOW", reserve=2.4)
flow.append(k.body(
    f"Every contract \"in an amount of more than $1,000 entered into between "
    f"a contractor and the owner of a property to be improved shall contain "
    f"in writing at least\": the contractor's name, business address and "
    f"license number; your name and mailing address and the jobsite address "
    f"or legal description; the contract date and \"The estimated date of "
    f"completion\"; a description of the work; \"The total dollar amount … "
    f"including all applicable taxes\"; \"The dollar amount of any advance "
    f"deposit\"; \"The dollar amount of any progress payment and the stage "
    f"of construction at which the contractor will be entitled to collect "
    f"progress payments\"; and notice of your right to complain to the "
    f"Registrar within two years, \"prominently displayed in the contract in "
    f"at least ten-point bold type\" ({ars('32-1158(A)')}). None of it is "
    f"\"a prerequisite to the formation or enforcement of a contract\" ((C)) "
    f"— a drafting minimum, not a defense — and the contractor must give you "
    f"\"a legible copy of all documents signed and a written and signed "
    f"receipt for … any cash paid\" ((B))."))
flow.append(k.cite(
    "<b>No statutory deposit cap exists in Arizona.</b> Add your own deposit "
    "limit, a lien-waiver-at-every-payment term and a retainage term as "
    "negotiated items, and label them as yours. <b>The recovery fund is open "
    f"to you</b>: an individual who \"Owns residential real property that is "
    f"damaged by the failure of a residential contractor to adequately build "
    f"or improve a residential structure\" and \"Actually occupies or intends "
    f"to occupy\" it \"as the individual's primary residence\" may claim "
    f"({ars('32-1132(B)(1)')}) — but only for damage by a <i>licensed</i> "
    f"residential contractor, which is one more reason the licensed-sub route "
    f"matters. <b>The window is two years from the day you move in</b>: a "
    f"complaint on a new home build must be filed \"within two years after "
    f"the earlier of the close of escrow or actual occupancy\" "
    f"({ars('32-1162(A)(1)')}) — not from the day the defect appears."))

# ---------------------------------------------------------------- comp
flow += k.h2_tight("WORKERS' COMPENSATION — THE HONEST POSITION", reserve=2.4)
flow.append(k.body(
    f"No Arizona statute says in terms that a homeowner building a personal "
    f"residence is, or is not, an \"employer.\" What the statutes do say: "
    f"employers subject to the chapter include \"every person who employs any "
    f"workers or operatives regularly employed in the same business or "
    f"establishment under contract of hire … except domestic servants,\" and "
    f"\"'regularly employed' includes all employments … <b>in the usual "
    f"trade, business, profession or occupation of an employer</b>\" "
    f"({ars('23-902(A)')}). \"Employee\" excludes \"a person whose employment "
    f"is both: (i) Casual. (ii) Not in the usual course of the trade, "
    f"business or occupation of the employer\" ({sec('23-901(6)(b)')})."))
flow.append(k.callout_long(
    "What that two-part test means, and the paper to have", [
        Paragraph("The exclusion needs <b>both</b> halves — casual, <i>and</i> "
                  "outside your usual trade. Building your own house is "
                  "outside your trade unless you are in construction; "
                  "whether a helper paid by the day for three months is "
                  "\"casual\" is a fact question no statute answers, so this "
                  "kit does not tell you that day labor is exempt.",
                  S["body"]),
        Paragraph(f"Have the paper regardless: a written "
                  f"independent-contractor agreement with the statutory "
                  f"statements \"creates a rebuttable presumption of an "
                  f"independent contractor relationship\" if it discloses "
                  f"that the contractor is not entitled to workers' "
                  f"compensation from you ({ars('23-902(D)')}); a sole "
                  f"proprietor may sign the statutory waiver — \"I am a sole "
                  f"proprietor … I am not the employee of … for workers' "
                  f"compensation purposes\" ({sec('23-961(N)')}); and every "
                  f"licensed contractor you hire should hand you a "
                  f"certificate. Then put the coverage question to the "
                  f"Industrial Commission of Arizona in writing before the "
                  f"first day of paid labor, and keep the answer with the "
                  f"deed.", S["body"]),
    ]))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS WITH A PEN",
                   reserve=1.6)
flow += k.check_table(
    "Confirm each of these before you break ground",
    [
        ("My deed or purchase contract is recorded with the county recorder "
         "in my own name as a natural person, and the recording date is "
         "before any construction began (§ 33-1002(A)(2)(a)):",
         [("Recorded", 0.5), ("Instrument no.", 0.5)]),
        "I intend to live in the house at least thirty days within the year "
        "after it is finished, and I do not intend to sell or lease it "
        "(§ 33-1002(A)(2)(b)). I will not list it, advertise it, or let "
        "anyone live in it in exchange for work inside that year "
        "(§ 32-1121(A)(5)).",
        ("I know whether my parcel is inside city limits, and which "
         "adopting ordinance — city or county — sets the code edition on my "
         "permit (§ 9-802; § 11-864). Ordinance number and date:",
         [("Jurisdiction", 0.4), ("Ordinance", 0.35), ("Date", 0.25)]),
        ("If I am using the Cochise or Coconino opt-out: I qualify on "
         "acreage and zoning, I know the notice will be recorded against "
         "my title and no (or a conditioned) certificate of occupancy will "
         "issue, and I will date the \"completion\" that starts the "
         "one-year clock:", [("Program / option", 1.0)]),
        ("Every person I pay is a wage employee (§ 32-1121(A)(11)) or a "
         "licensed contractor verified at the Registrar on the contract, "
         "first-payment and start dates (§ 32-1132(C)). Nobody is paid by "
         "the job, by a share, or with a place to sleep:",
         [("Licensed subs and ROC nos.", 1.0)]),
        "My § 32-1169 statement names § 32-1121(A)(5) as the basis and "
        "lists every licensed general, mechanical, electrical and plumbing "
        "contractor I will use, with license numbers — and I asked whether "
        "the counter wants the Registrar's signature on it.",
        ("Every contract over $1,000 has the § 32-1158(A) contents plus my "
         "own deposit and lien-waiver terms; I keep a file of every "
         "preliminary twenty-day notice (§ 33-992.01); and I put the "
         "workers' compensation question to the Industrial Commission in "
         "writing before the first day of paid labor:",
         [("ICA asked", 0.5), ("Answered", 0.5)]),
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "az-permit-kit",
                       "AZ.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
