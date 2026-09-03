#!/usr/bin/env python3
"""OH.1 Owner-Builder Exemption Walkthrough.

Every Ohio claim in this document was read out of its primary source in
September 2026 and is cited on-page. Where the statute is silent, or the answer
depends on a local ordinance, the document says so and gives the verification
step rather than guessing.

The Ohio story is not the Arkansas story even though both states end with "your
county may not inspect you." Arkansas gets there by omission — nothing requires
a county to create a building department, so most never did. Ohio gets there BY
TEXT: the code and the statute each contain a sentence that says, in terms, that
where no residential-certified department has jurisdiction the owner submits
nothing. That is a much stronger thing to be able to print, and it is why this
document leads with the two quotations rather than with an inference.

The second Ohio distinctive is the definition chain. Ohio genuinely licenses
electrical, plumbing, HVAC, refrigeration and hydronics contractors — and that
licensure does not reach a one-, two-, or three-family dwelling at all, because
"construction project" is defined to exclude a "residential building." Almost
every guide, including our own state guide, tells Ohio readers to hire
OCILB-licensed trades for their house. As a matter of state law that is wrong.

Verified sources:
  R.C. 4740.01(A),(D)     the five licensed trades, named
  R.C. 4740.01(F)         "construction project" EXCLUDES a residential building
  R.C. 3781.06(C)(9)      "residential building" = 1-, 2-, 3-family dwelling
  R.C. 3781.06(C)(11)     "accessory structure" means an ATTACHED one
  R.C. 4740.13(A)         the license requirement itself
  R.C. 4740.99            minor misdemeanor first violation, M4 after
  R.C. 4740.12(A),(B)     local trade regulation expressly preserved
  R.C. 4740.14            the state names "general contractors" and does not
                          license them
  OAC 4101:8-1-01 101.5   the RCO's own no-certified-department sentence
  R.C. 3791.04(A)(1)(a),(b)  the same rule in statute — and the asymmetry with
                          nonresidential work, which DOES fall back to the state
  R.C. 3781.10(E)(2),(3),(8),(10)  three certifications, granted on application
  R.C. 3781.10(E)(7)      enforcement may be contracted out, incl. to the state
  R.C. 3781.01(B),(C),(D) local add-on rules, and the 60-day challenge
  R.C. 3781.06(B)(1)      the agricultural exemption
  R.C. 3791.04(A)(2)(b)   no architect or engineer seal for a house
  R.C. 4722.01,.02,.03,.04,.08  the Home Construction Service Suppliers Act,
                          the $25,000 line, and the cost-plus trap
  R.C. 1345.01(A)         home construction service contracts are OUTSIDE the
                          Consumer Sales Practices Act
  R.C. 1311.04(O)         no Notice of Commencement for a home construction
                          contract
  R.C. 1311.06(B)(1),(3)  60 days for a one- or two-family dwelling, 75 days
                          otherwise — the three-family seam
  R.C. 1311.011(A),(B)    the homeowner payment defense

DELIBERATELY NOT CLAIMED, and why:
  - Any count of certified residential building departments, or any list of
    counties with or without one. No machine-readable roster was retrieved this
    pass, and a fabricated number here would be the worst possible error. The
    document gives the method and OH.4 gives the lookup.
  - That a municipality must enforce the residential code while a county or
    township may decline. R.C. 3781.10(E)(10) treats all three layers
    identically as voluntary applicants. Several guides assert the split; the
    statute does not support it.
  - That a homeowner in Ohio has a statutory right to do their own electrical
    or plumbing work. There is no such state provision, and none is needed
    where the state license does not reach the house — but a local ordinance
    may still require a licensed trade, and R.C. 4740.12(B) expressly preserves
    that power. The document says exactly this and sends the reader to ask.
  - That no permits at all are required where no building department is
    certified. The sewage permit, the private water permit, zoning, floodplain
    and the separate plumbing enforcement track all survive. The verified claim
    is narrower and is the one printed.
  - Any statement that a particular county has no certified department. That is
    a per-parcel fact and the document gives the method, not the answer.
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

FORM_ID = "OH.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "Exemption & Qualification"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Why Ohio has no owner-builder exemption and does not need one — and the "
    "one question about your own parcel that changes the shape of the entire "
    "build.")

flow.append(k.disclaimer(
    "Statute and rule text was read at codes.ohio.gov in September 2026, "
    "including the Board of Building Standards' own filed rule PDFs; all of "
    "them change."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION", reserve=2.0)
flow.append(k.body(
    "Most states hand an owner-builder an <i>exemption</i>: a paragraph "
    "excusing you from a contractor license you would otherwise need. "
    "<b>Ohio has no such paragraph, and does not need one</b>, because Ohio "
    "never licensed the thing you are about to do. There is no state general "
    "contractor license in Ohio — not for residential work, not for anything."))
flow.append(k.body(
    "Ohio does license five construction trades. The surprise, and it is a "
    "genuine one, is that <b>those licenses do not reach a one-, two-, or "
    "three-family dwelling at all.</b> They are commercial licenses. The next "
    "section walks the four-step definition chain that proves it, because "
    "almost every guide to building in Ohio — including, until this kit was "
    "written, our own — tells you the opposite."))
flow.append(k.body(
    "So the interesting question in Ohio is not <i>may I build it</i>. It is "
    "<b>whether anybody is certified to review, permit and inspect it</b> — "
    "and Ohio is unusual in answering that question in its own published text "
    "rather than leaving you to infer it."))

rows = [
    [k.cellp("Do you need a license to build your own house?"),
     k.cellp("<b>No.</b> Ohio issues no general contractor license of any "
             "kind. The state's own advisory committee statute refers to "
             f"\"general contractors\" as a real trade and licenses none of "
             f"them ({sec('4740.14')})")],
    [k.cellp("Do you need a licensed electrician or plumber for your house?"),
     k.cellp("<b>Not as a matter of state law.</b> The state trade licenses "
             f"reach only a \"construction project\", and that term is defined "
             f"to exclude a residential building ({sec('4740.01(F)')}). "
             f"<b>Your city or township may still require one</b> — see the "
             f"next two sections")],
    [k.cellp("Is there an owner-builder affidavit or exemption form?"),
     k.cellp("<b>No.</b> There is no state form, because there is no state "
             "license to be exempt from. A certified local department may have "
             "its own")],
    [k.cellp("Is there a limit on how many houses, or a holding period?"),
     k.cellp("<b>No.</b> Ohio sets no annual cap, no not-for-sale window and "
             "no resale clawback, because none of those attach to a license "
             "you never needed")],
    [k.cellp("Do you need a building permit?"),
     k.cellp("<b>Only if a building department certified for residential "
             "buildings has jurisdiction over your parcel.</b> If none does, "
             "the code and the statute both say you submit nothing. This is "
             "the sentence the rest of the kit turns on")],
    [k.cellp("Do you need an architect or engineer to seal the plans?"),
     k.cellp(f"<b>No.</b> \"No seal is required for any plans… submitted for "
             f"approval for any residential buildings\" "
             f"({sec('3791.04(A)(2)(b)')}). That is a state rule and a local "
             f"department cannot add a seal requirement that conflicts with "
             f"it")],
    [k.cellp("Does the building code apply either way?"),
     k.cellp("<b>Yes. Always.</b> The Residential Code of Ohio governs \"every "
             "one-, two-, or three-family dwelling\" by its own scope. Only "
             "the paperwork is conditional")],
]
flow.append(k.ref_table(
    "The Ohio position at a glance",
    [k.cellp("Question", bold=True), k.cellp("Ohio's answer", bold=True)],
    rows, [2.45 * inch, CW - 2.45 * inch]))
flow.append(k.cite(
    "Statutes are cited as R.C. — the Ohio Revised Code — and rules as OAC, "
    "the Ohio Administrative Code. Both read free at codes.ohio.gov by number "
    "alone. The Residential Code of Ohio is OAC Chapter 4101:8; the Board of "
    "Building Standards inside the Department of Commerce adopts it."))

# ---------------------------------------------------------------- chain
flow += k.h2_tight("THE FOUR-LINK CHAIN THAT PUTS YOUR HOUSE OUTSIDE THE STATE "
                   "TRADE LICENSES", reserve=2.0)
flow.append(k.body(
    "This is the single most valuable thing in this document, and you can "
    "check every link of it yourself in about five minutes at codes.ohio.gov. "
    "Ohio's construction licensing chapter is R.C. Chapter 4740, administered "
    "by the Ohio Construction Industry Licensing Board. Follow the "
    "definitions."))
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp(f"<b>The prohibition</b><br/>{sec('4740.13(A)')}"),
     k.cellp("\"No person shall act as or claim to be <b>a type of contractor "
             "that this chapter licenses</b> unless that person holds… a "
             "license issued pursuant to this chapter\"")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp(f"<b>Which types?</b><br/>{sec('4740.01(A)')}, {sec('4740.01(D)')}"),
     k.cellp("A license is one issued \"as a <b>heating, ventilating, and air "
             "conditioning contractor, refrigeration contractor, electrical "
             "contractor, plumbing contractor, or hydronics contractor</b>.\" "
             "Five trades. No general contractor, roofer, framer, concrete, "
             "drywall or excavation license exists")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp(f"<b>A contractor of what?</b><br/>{sec('4740.01(B)')}, "
             f"{sec('4740.01(F)')}"),
     k.cellp("Each of those five is defined only by reference to work on a "
             "\"construction project\" — and: \"'Construction project' means a "
             "construction project involving a building or structure subject "
             "to Chapter 3781… <b>but not an industrialized unit or a "
             "residential building as defined in section 3781.06</b>\"")],
    [k.cellp("<b>4</b>", center=True),
     k.cellp(f"<b>What is a residential building?</b><br/>"
             f"{sec('3781.06(C)(9)')}"),
     k.cellp("\"'Residential building' means a <b>one-family, two-family, or "
             "three-family dwelling house, and any accessory structure "
             "incidental to that dwelling house</b>\"")],
]
flow.append(k.ref_table(
    "Follow the definitions and the license disappears",
    [k.cellp("", bold=True, center=True), k.cellp("Step", bold=True),
     k.cellp("What the statute says", bold=True)],
    rows, [0.35 * inch, 1.65 * inch, CW - 2.0 * inch]))
flow.append(Spacer(1, 4))
flow.append(k.callout(
    "What that chain actually means for your build", [
        Paragraph("The Ohio electrical, plumbing, HVAC, refrigeration and "
                  "hydronics contractor licenses are <b>commercial</b> "
                  "licenses. As a matter of <i>state</i> law they are not "
                  "required for work on a one-, two-, or three-family dwelling "
                  "house. An electrician wiring your house is not required by "
                  "the State of Ohio to hold a state license, and neither are "
                  "you.", S["body"]),
        Paragraph("<b>Do not read that as \"anyone can wire your house.\" "
                  "Read it as \"the rule you are looking for is local, not "
                  "state.\"</b> Ohio expressly kept that power with your city "
                  "or township, and the next section is about how to find it. "
                  "The competence question is also entirely unaffected: the "
                  "2023 National Electrical Code applies to your house whoever "
                  "holds the screwdriver.", S["body"]),
    ]))
flow.append(k.cite(
    f"Penalty, for completeness: acting as a licensed type of contractor "
    f"without the license is \"a minor misdemeanor on the first violation and "
    f"a misdemeanor of the fourth degree on subsequent violations\" "
    f"({sec('4740.99')}). Two carve-outs inside {sec('4740.13')} are worth "
    f"knowing anywhere: control wiring under twenty-five volts is not separate "
    f"contracting for a licensed trade (D), and a person is \"not an "
    f"electrical contractor subject to licensure\" for fire alarm, burglar "
    f"alarm, cabling, tele-data, sound, communication, landscape lighting and "
    f"irrigation work \"using less than fifty volts\" (also D)."))

flow.append(Spacer(1, 4))
flow.append(k.body(
    f"<b>Ohio then says out loud that the local rule survives.</b> "
    f"{sec('4740.12(B)')} provides that \"nothing in this chapter shall be "
    f"construed to limit the operation of any statute or rule of this state or "
    f"any ordinance or rule of any political subdivision… that either "
    f"regulates the installation, repair, maintenance, or alteration of "
    f"plumbing systems, hydronics systems, electrical systems, heating, "
    f"ventilating, and air conditioning systems, or refrigeration systems\" or "
    f"\"requires the registration and assessment of a registration or license "
    f"fee of tradespersons\". <b>That sentence is the whole reason Ohio feels "
    f"like a patchwork.</b> There is one state code and eighty-eight counties' "
    f"worth of local answers about who may install what under it."))
flow.append(k.closing_note(
    f"One nuance we are not going to resolve for you, because the statute does "
    f"not. {sec('4740.12(A)')} says no political subdivision \"may adopt an "
    f"ordinance or rule that requires contractor registration and the "
    f"assessment of a registration or license fee unless that ordinance or "
    f"rule also requires any contractor who registers and pays the "
    f"registration or license fee to be licensed in the contractor's trade "
    f"pursuant to this chapter.\" How that interacts with a purely residential "
    f"local trade license — where the state license does not exist to be "
    f"required — is not settled in the text, and cities plainly do issue such "
    f"licenses. Ask your jurisdiction what it requires and comply with the "
    f"answer; do not argue this paragraph at a permit counter."))

# ---------------------------------------------------------------- the big one
flow += k.h2_tight("THE QUESTION THAT DECIDES YOUR BUILD", reserve=2.0)
flow.append(k.body(
    "Ohio writes one residential code for the whole state. It does not require "
    "anyone to enforce it on your house. What makes Ohio unusual is that both "
    "the code and the statute say so <b>in terms</b> — you are not relying on "
    "an inference from a permissive verb, you are relying on two sentences "
    "that describe your situation directly."))
flow.append(k.callout_long(
    "The two texts, in full", [
        Paragraph(f"<b>OAC {k.rule('4101:8-1-01')}, RCO section 101.5 — "
                  f"Jurisdiction without a certified residential building "
                  f"department.</b> \"If no municipal, township, or county "
                  f"building department is certified by the Board of Building "
                  f"Standards for residential buildings in accordance with "
                  f"section 3781.10(E) of the Revised Code has jurisdiction, "
                  f"<b>the owner is not required to make submission of "
                  f"construction documents, seek approvals, request "
                  f"inspections, or obtain certificates of occupancy required "
                  f"in this Chapter.</b>\"", S["body"]),
        Paragraph(f"<b>R.C. {sec('3791.04(A)(1)')} — the same rule in "
                  f"statute, and the asymmetry.</b> Before construction the "
                  f"owner \"shall submit plans or drawings, specifications, "
                  f"and data… to the municipal, township, or county building "
                  f"department having jurisdiction <b>unless one of the "
                  f"following applies</b>: (a) If no… department certified for "
                  f"<b>nonresidential</b> buildings… has jurisdiction, the "
                  f"owner shall make the submissions… <b>to the "
                  f"superintendent of industrial compliance</b>. (b) If no "
                  f"certified… department certified for <b>residential</b> "
                  f"buildings… has jurisdiction, <b>the owner is not required "
                  f"to make the submissions</b>.\"", S["body"]),
        Paragraph("<b>Read (a) against (b).</b> Ohio built a state backstop "
                  "for commercial work and deliberately did not build one for "
                  "houses. If nobody local is certified for a warehouse, your "
                  "plans go to Columbus. If nobody local is certified for your "
                  "house, your plans go nowhere. That contrast is the clearest "
                  "evidence that the residential gap is a choice the "
                  "legislature made, not an oversight.", S["body"]),
    ]))
flow.append(k.cite(
    "The grammar of RCO 101.5 (\"If no… department is certified… has "
    "jurisdiction\") is the state's, quoted as filed. The rule is published as "
    "a PDF at codes.ohio.gov under OAC 4101:8; section 101.5 sits on the "
    "second page of the Administration chapter."))

flow.append(Spacer(1, 4))
flow.append(k.body(
    "<b>Certification is something a local government applies for, and it "
    "comes in three separate flavors.</b> This matters more than it sounds, "
    "because a department can hold one flavor and not another — and it "
    "\"may enforce only the type of building code for which certified\"."))
rows = [
    [k.cellp("<b>Nonresidential</b>"),
     k.cellp("Commercial and industrial buildings"),
     k.cellp("A department with only this certification <b>cannot touch your "
             "house</b>, however large its office is")],
    [k.cellp("<b>Residential — new construction</b>"),
     k.cellp("\"the erection and construction of new residential buildings\""),
     k.cellp("This is the one that decides whether your new house is "
             "permitted and inspected")],
    [k.cellp("<b>Residential — repair and alteration</b>"),
     k.cellp("\"the repair and alteration of existing residential "
             "buildings\" — a separate certification a department "
             "\"<b>may also</b>\" obtain"),
     k.cellp("A department certified only for new construction cannot "
             "regulate your later remodel")],
]
flow.append(k.ref_table(
    f"Three certifications, R.C. {sec('3781.10(E)(2)')} and (E)(10)",
    [k.cellp("Certification", bold=True), k.cellp("Covers", bold=True),
     k.cellp("What it means for you", bold=True)],
    rows, [1.6 * inch, 1.75 * inch, CW - 3.35 * inch]))
flow.append(k.cite(
    f"Certification \"shall be granted <b>upon application</b> by the "
    f"municipal corporation, the board of township trustees, or the board of "
    f"county commissioners\" ({sec('3781.10(E)(10)')}), and the Board \"shall "
    f"not require a building department… to be certified for residential "
    f"building code enforcement <b>if that building department does not "
    f"enforce the state residential building code</b>\" "
    f"({sec('3781.10(E)(3)')}). Departments \"have jurisdiction… only with "
    f"respect to the types of buildings and subject matters for which they are "
    f"certified\" ({sec('3781.10(E)(8)')}). <b>Note what the statute does not "
    f"say:</b> it does not require cities to be certified and let counties opt "
    f"out. All three layers are voluntary applicants on identical terms. "
    f"Guides that draw a city-versus-county line are adding one."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Two traps in the \"nobody is certified here\" finding", [
        Paragraph("<b>1. A county with no building department of its own may "
                  "still have an inspector.</b> Enforcement authority may be "
                  "exercised on a jurisdiction's behalf by contract — by "
                  "another municipality, township or county, by a health "
                  "district, by a private firm furnishing architectural or "
                  "engineering services, or by the state's own Division of "
                  "Industrial Compliance under a contract authorized by R.C. "
                  f"{sec('121.083(B)')} ({sec('3781.10(E)(7)')}). \"No "
                  f"building department listed on the county website\" is "
                  f"therefore not the end of the enquiry. Ask who does their "
                  f"inspections.", S["body"]),
        Paragraph("<b>2. \"No building permit\" never means \"no permits.\" "
                  "</b>The sewage treatment system permit and the private "
                  "water system permit come from your local health district "
                  "under statewide rules that do not mention building "
                  "departments. Plumbing enforcement runs on its own track "
                  "entirely. Zoning is a separate authority again — a township "
                  "with zoning and no building department can still require a "
                  "zoning certificate. OH.2 and OH.4 carry the list.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- plumbing
flow += k.h2_tight("THE PLUMBING TRACK RUNS SEPARATELY — AND MAY SURVIVE WHEN "
                   "THE BUILDING PERMIT DOES NOT", reserve=2.0)
flow.append(k.body(
    "This catches careful people. Building-code enforcement flows from a "
    "Board of Building Standards certification. <b>Plumbing enforcement does "
    "not.</b> It is assigned by a different statute to a wider and different "
    "set of bodies, none of which needs a building-department certification to "
    "act."))
flow.append(k.callout(
    f"R.C. {sec('3781.03(C)')} — who enforces the plumbing rules", [
        Paragraph("\"<b>The division of industrial compliance in the "
                  "department of commerce, boards of health of health "
                  "districts, certified departments of building inspection of "
                  "municipal corporations, and county building departments</b> "
                  "that have authority to perform inspections pursuant to a "
                  "contract under division (C)(1) of section 3703.01 of the "
                  "Revised Code… shall enforce this chapter and Chapter 3791. "
                  "of the Revised Code and the rules adopted pursuant to those "
                  "chapters <b>that relate to plumbing. Building drains are "
                  "considered plumbing</b> for the purposes of enforcement of "
                  "those chapters.\"", S["body"]),
    ]))
flow.append(k.body(
    "<b>The practical consequence:</b> it is entirely possible to have a "
    "parcel with no residential building permit and still owe a plumbing "
    "permit and inspection — commonly from the county health district. Which "
    "of the four bodies applies to your parcel is a local fact. Ask, in these "
    "words: <i>who inspects residential plumbing here, and do I need a permit "
    "for it?</i> Write the answer on the directory page in OH.4."))
flow.append(k.cite(
    f"Separately, RCO section 102.11 hands two subjects to other offices even "
    f"inside a fully certified jurisdiction: fire prevention to the fire chief, "
    f"and \"provisions relating to sanitary construction\" to \"the department "
    f"of health, the boards of health of city or general health districts, or "
    f"the residential departments of building inspection\". Section 102.11(3), "
    f"citing R.C. {sec('3781.03')}, gives the city engineer's department, the "
    f"boards of health, or the sewer purveyor \"complete supervision and "
    f"regulation of the entire sewerage and drainage system… including the "
    f"building sewer and all laterals\" and provides that they \"shall issue "
    f"all the necessary permits\" for it."))

# ---------------------------------------------------------------- ag
flow += k.h2_tight("THE AGRICULTURAL EXEMPTION — REAL, AND NARROWER THAN "
                   "PEOPLE HOPE", reserve=1.8)
flow.append(k.body(
    f"Ohio exempts farm buildings from the whole state building-code scheme, "
    f"and the exemption is worth knowing precisely because people routinely "
    f"stretch it over a house. It does not reach a dwelling."))
flow.append(k.callout(
    f"R.C. {sec('3781.06(B)(1)')}", [
        Paragraph("Sections 3781.06 to 3781.18, 3781.40 and 3791.04 \"do not "
                  "apply to… <b>Buildings or structures that are incident to "
                  "the use for agricultural purposes of the land on which the "
                  "buildings or structures are located, provided those "
                  "buildings or structures are not used in the business of "
                  "retail trade.</b>\" A building is not in retail trade if "
                  "fifty per&#160;cent or more of gross income from product "
                  "sales in it comes from products \"produced or raised in a "
                  "normal crop year on farms owned or operated by the "
                  "seller.\"", S["body"]),
    ]))
flow.append(k.body(
    f"\"Agricultural purposes\" is defined broadly at {sec('3781.06(C)(1)')} — "
    f"it runs from ordinary farming and pasturage through apiculture, "
    f"algaculture, viticulture, olericulture and pomiculture to animal and "
    f"poultry husbandry. <b>What it never covers is the house you live in.</b> "
    f"A barn on your parcel can be exempt while the dwelling forty feet away "
    f"is fully inside the Residential Code of Ohio. Do not let a builder tell "
    f"you the farm exemption travels."))
flow.append(Spacer(1, 4))
flow.append(k.callout(
    "One exception that can move your whole project into the commercial code",
    [
        Paragraph(f"If you are building anything other than a single-family "
                  f"house, read RCO section 101.2's exceptions before you "
                  f"design. Exception 4: \"<b>Buildings or structures "
                  f"containing two or three dwelling units with a shared exit "
                  f"shall comply with the requirements of the 'OBC.'</b>\" "
                  f"Exception 3 does the same for a residential building "
                  f"attached to an occupancy within the commercial code's "
                  f"scope.", S["body"]),
        Paragraph("<b>A shared exit is the trigger.</b> A duplex or triplex "
                  "where the units share a common stair or entry leaves the "
                  "Residential Code of Ohio entirely and is reviewed under the "
                  "Ohio Building Code — which means sealed drawings, a "
                  "commercial plan review, and the state Division of "
                  "Industrial Compliance as a backstop if no local department "
                  "is certified for nonresidential work. Give each unit its "
                  "own exit and you stay in the residential code. That is a "
                  "design decision with a very large cost attached, and it is "
                  "made on paper long before anyone pours a footing.",
                  S["body"]),
    ]))
flow.append(k.cite(
    f"One related definition worth reading before you plan outbuildings: "
    f"\"accessory structure\" is defined at {sec('3781.06(C)(11)')} as one "
    f"that is <b>attached to</b> the dwelling — \"a garage, porch, or "
    f"screened-in patio\". A <i>detached</i> garage or shed is therefore not "
    f"an accessory structure under that definition, and how it is treated "
    f"depends on your local department and on the RCO's own exempt-work list, "
    f"which OH.5 prints in full."))

# ---------------------------------------------------------------- hiring subs
flow += k.h2_tight("HIRING SUBCONTRACTORS — OHIO HANDS YOU A WEAPON MOST "
                   "OWNER-BUILDERS NEVER FIRE", reserve=2.0)
flow.append(k.body(
    "Ohio's Home Construction Service Suppliers Act, R.C. Chapter 4722, "
    "imposes <b>nothing at all</b> on you. A \"supplier\" is defined as one "
    "who \"contracts with an owner to provide home construction services "
    "<b>for compensation</b>\", and you do not contract with yourself. There "
    "is no registration, bond or filing anywhere in the chapter that attaches "
    "to an owner."))
flow.append(k.body(
    "<b>What Chapter 4722 does instead is regulate everyone you hire</b> — and "
    "it applies to each of your subcontractors individually, because each of "
    "them is contracting with you for home construction services. Any contract "
    "of <b>$25,000 or more</b> triggers the whole apparatus."))
rows = [
    [k.cellp("<b>A written contract, with nine required contents</b>"),
     k.cellp(f"{sec('4722.02(A)')}"),
     k.cellp("Including \"a copy of the supplier's certificate of insurance "
             "showing general liability coverage in an amount of not less than "
             "two hundred fifty thousand dollars.\" <b>The statute makes your "
             "contractor hand you their certificate of insurance</b>")],
    [k.cellp("<b>A change-order estimate</b>"),
     k.cellp(f"{sec('4722.02(B)')}"),
     k.cellp("Required whenever unforeseen excess costs cumulatively exceed "
             "<b>$5,000</b> across the whole contract. You choose written or "
             "oral notice by initialling a clause the statute scripts")],
    [k.cellp("<b>A 10% cap on the deposit</b>"),
     k.cellp(f"{sec('4722.04')}"),
     k.cellp("\"not more than ten per&#160;cent of the contract price\" before "
             "work begins — except up to 75% of a special-order item that is "
             "not returnable or usable")],
    # "A prohibited-practices list" broke as "prohibited-practi / ces" in the
    # 1.6in column: reportlab treats the hyphen as a break opportunity and the
    # fragment left behind is three characters, which check.py's split-word
    # detector (<= 2 characters) does not catch. Worded to break at a space.
    [k.cellp("<b>A list of prohibited practices</b>"),
     k.cellp(f"{sec('4722.03(A)')}"),
     k.cellp("Eleven of them, including failing \"to perform the home "
             "construction service in a workmanlike manner\" and representing "
             "that work \"is necessary to comply with the residential building "
             "code when such is not the fact\"")],
    [k.cellp("<b>Your remedy if they break it</b>"),
     k.cellp(f"{sec('4722.08(A)')}"),
     k.cellp("Rescind the transaction, or recover \"actual economic damages "
             "plus an amount not exceeding five thousand dollars in "
             "noneconomic damages\". Attorney fees only if the supplier acted "
             "<b>knowingly</b>")],
]
flow.append(k.ref_table(
    "What every sub on a $25,000-or-more contract owes you by statute",
    [k.cellp("What you get", bold=True), k.cellp("Cite", bold=True),
     k.cellp("The detail that matters", bold=True)],
    # 0.95in is too narrow for the Cite column: "§ 4722.02(A)" measures 61pt at
    # the cell style's 9.5pt, and a 0.95in column leaves 58.4pt inside the 5pt
    # side padding — so the closing parenthesis wrapped onto a line of its own.
    # check.py cannot see this (it strips brackets before testing a fragment),
    # so it has to be caught by eye. 1.15in leaves 72.8pt.
    rows, [1.6 * inch, 1.15 * inch, CW - 2.75 * inch]))
flow.append(k.cite(
    f"The threshold is written twice and not identically: {sec('4722.01(C)')} "
    f"defines the contract as one \"for an amount <i>exceeding</i> twenty-five "
    f"thousand dollars\" while {sec('4722.02(A)')} bars performing a service "
    f"\"the cost of which <i>equals or exceeds</i> twenty-five thousand "
    f"dollars\". Treat the line as \"$25,000 or more\" and do not build a plan "
    f"around the exact-$25,000 edge. \"Residential building\" here means the "
    f"same 1-, 2-, or 3-family dwelling as everywhere else "
    f"({sec('4722.01(F)')}), and \"workmanlike manner\" is defined by "
    f"reference to \"the minimum quantifiable standards promulgated by the "
    f"Ohio home builders association\" ({sec('4722.01(G)')})."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "The cost-plus trap — read this before you sign anything", [
        Paragraph("<b>Every one of those protections evaporates on a "
                  "cost-plus contract, and cost-plus is extremely common in "
                  "custom residential work.</b> The statute says so three "
                  f"times. A supplier on a cost-plus contract \"need not "
                  f"comply with the requirements in divisions (A) and (B)\" — "
                  f"that is the written contract and the change-order estimate "
                  f"({sec('4722.02(C)')}). The excess-cost duty likewise does "
                  f"not apply ({sec('4722.03(B)')}). And the deposit cap "
                  f"carries its own sentence: \"This section does not apply to "
                  f"a home construction service supplier who enters into a "
                  f"cost-plus contract\" ({sec('4722.04')}).", S["body"]),
        Paragraph(f"A cost-plus contract is defined at {sec('4722.01(A)')} as "
                  f"one \"under which payment to the supplier is based on the "
                  f"cost of a product plus the supplier's rate for labor to "
                  f"install the product plus an agreed percentage of profit or "
                  f"a stipulated fee.\" If a contractor proposes one, they are "
                  f"proposing — whether or not they know it — that you waive "
                  f"the written-contract mandate, the change-order estimate "
                  f"and the ten per&#160;cent deposit cap. That may still be "
                  f"the right deal. Make it a decision rather than an "
                  f"accident.", S["body"]),
    ]))

flow.append(Spacer(1, 4))
flow.append(k.body(
    f"<b>One more inversion worth knowing.</b> A home construction service "
    f"contract is expressly carved <i>out</i> of Ohio's Consumer Sales "
    f"Practices Act: \"'Consumer transaction' does not include… transactions "
    f"involving a home construction service contract as defined in section "
    f"4722.01\" ({sec('1345.01(A)')}). So the bigger the job, the narrower "
    f"your statutory remedy — the Chapter 4722 remedy replaces the Consumer "
    f"Sales Practices Act's, rather than adding to it. Work below the $25,000 "
    f"line is not a \"home construction service contract\" as defined and so "
    f"is not carved out. That is a genuine inversion and it surprises people; "
    f"if a dispute gets serious, it is a question for a lawyer, not for this "
    f"page."))

# ---------------------------------------------------------------- liens
flow += k.h2_tight("THE LIEN RULES — WHERE OHIO IS UNUSUALLY GOOD TO YOU, AND "
                   "ONE SEAM TO WATCH", reserve=2.0)
flow.append(k.body(
    "Ohio gives an owner building a home to live in a protection most states "
    "do not: <b>you cannot be made to pay twice.</b> It applies to a \"home "
    "construction contract\", which R.C. 1311.011(A)(1) defines as one for the "
    "improvement of a <b>single- or double-family dwelling</b> \"if the "
    "dwelling… is used or is intended to be used as a personal residence by "
    "the owner\"."))
flow.append(k.callout_long(
    f"R.C. {sec('1311.011(B)')} — the payment defense", [
        Paragraph("\"<b>(1) No original contractor, subcontractor, material "
                  "supplier, or laborer has a lien to secure payment… if the "
                  "owner… paid the original contractor in full</b>… and the "
                  "payment was made prior to the owner's… receipt of a copy of "
                  "an affidavit of mechanics' lien pursuant to section "
                  "1311.07… any lien perfected on the property by any "
                  "subcontractor, material supplier, or laborer… <b>is void "
                  "and the property wholly discharged from the lien</b>, if "
                  "the lien was perfected after full payment was made…\"",
                  S["body"]),
        Paragraph("\"<b>(2)</b> If the original contractor has not been paid "
                  "in full… <b>no subcontractor, material supplier, or laborer "
                  "has a lien… for an amount greater than the amount due under "
                  "the home construction contract that has not been paid to "
                  "the original contractor.</b>\" Claimants share that unpaid "
                  "balance pro rata, \"except that mechanics' liens filed by "
                  "laborers have priority\" — and the balance is computed "
                  "\"minus the cost to complete the contract\".", S["body"]),
        Paragraph("\"<b>(3)</b> If, after receiving written notice from an "
                  "owner… that full payment has been made… the lienholder "
                  "<b>fails within thirty&#160;days</b>… to cause the lien… to be "
                  "released of record, the lienholder <b>is liable to the "
                  "owner… for all damages</b>… including \"court costs and "
                  "reasonable attorney fees\".", S["body"]),
    ]))
flow.append(k.body(
    f"Two things make this usable rather than theoretical. First, "
    f"{sec('1311.011(B)(6)')} lets you <b>withhold payment</b> until the "
    f"contractor gives you a sworn affidavit that everyone below them is paid "
    f"— and provides that your rights \"shall not be prejudiced by\" failing "
    f"to ask for one. Second, {sec('1311.011(B)(7)')} expressly blesses "
    f"<b>joint checks</b> to the contractor and their sub as a condition of "
    f"getting lien releases, and (B)(9) makes any such release valid \"without "
    f"separate consideration\"."))
flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Four precision points, because this is where money is lost", [
        Paragraph("<b>1. The defense is per contract, not per house.</b> "
                  f"\"Original contractor\" includes <i>anyone the owner has "
                  f"directly contracted with</i> ({sec('1311.011(A)(4)')}). As "
                  f"your own general contractor you have many original "
                  f"contractors. Paying your framer in full protects you "
                  f"against the framer's suppliers. It does nothing about your "
                  f"plumber's.", S["body"]),
        Paragraph("<b>2. The clock is the arrival of a lien affidavit "
                  "copy.</b> The protection covers payments made <i>before</i> "
                  "you receive one under section 1311.07. The moment a copy "
                  "lands, stop paying on that contract and get advice.",
                  S["body"]),
        Paragraph("<b>3. It only covers a home you will live in.</b> The "
                  "definition requires the dwelling be \"used or… intended to "
                  "be used as a personal residence by the owner\". A house "
                  "built to sell is outside it.", S["body"]),
        Paragraph("<b>4. Three-family houses fall through the seam.</b> Ohio "
                  "uses \"one-, two-, or three-family\" as its unit everywhere "
                  "else — the building code, the trade licenses, Chapter 4722. "
                  "<b>Chapter 1311 does not.</b> The payment defense reaches a "
                  "\"single- or double-family dwelling\" only, and the "
                  f"sixty-day lien deadline at {sec('1311.06(B)(1)')} reaches "
                  f"\"a one- or two-family dwelling\" only. A three-family "
                  f"dwelling gets neither: it falls to the residual "
                  f"seventy-five-day period at {sec('1311.06(B)(3)')} and "
                  f"outside the payment defense altogether. If you are "
                  f"building a triplex, this paragraph is the most important "
                  f"one on the page.", S["body"]),
    ]))
flow.append(k.closing_note(
    f"<b>And one piece of paperwork you probably do not owe.</b> Ohio's Notice "
    f"of Commencement rules do not apply to a home construction contract: "
    f"\"This section does not apply to a home construction contract as defined "
    f"in section 1311.011\" ({sec('1311.04(O)')}), and the notice-of-furnishing "
    f"section carries the same exclusion ({sec('1311.05(E)')}). <b>Your "
    f"construction lender may still require one</b>, and the statute expressly "
    f"contemplates that — if you record one because the lender asks, you get "
    f"the priority rules of section 1311.13 and your subs are relieved of the "
    f"notice-of-furnishing duty. Liens are recorded with the county recorder, "
    f"and \"no exemptions apply against any lien under this chapter\" "
    f"({sec('1311.06(E)')}), so the homestead exemption is no shield."))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS WITH A PEN",
                   reserve=1.6)
flow += k.check_table(
    "Confirm each of these before you break ground",
    [
        ("I established whether a building department <b>certified for "
         "residential buildings</b> has jurisdiction over this parcel — asking "
         "the municipality or village, the township, and the county. Answer:",
         [("Office", 0.5), ("Answer", 0.5)]),
        ("If a department is certified, I confirmed <b>which</b> certification "
         "it holds — new construction, repair and alteration, or "
         "nonresidential only.", [("Answer", 1.0)]),
        ("If none is certified, I asked whether the jurisdiction <b>contracts "
         "out</b> its enforcement to another subdivision, a health district, a "
         "private firm or the state Division of Industrial Compliance "
         "(§&#160;3781.10(E)(7)). Answer:", [("Answer", 1.0)]),
        ("I got that answer <b>in writing</b> and dated it.",
         [("Date", 0.4), ("From", 0.6)]),
        ("I asked separately who inspects <b>residential plumbing</b> here, "
         "and whether a plumbing permit is required (§&#160;3781.03(C) lists four "
         "possible bodies). Answer:", [("Office", 0.5), ("Answer", 0.5)]),
        ("I asked my municipality or township whether it requires "
         "<b>contractor or tradesperson registration</b> for work on my own "
         "home, and whether an owner may do their own electrical and plumbing "
         "(§&#160;4740.12(B) preserves that power). Answer:",
         [("Answer", 1.0)]),
        ("I confirmed whether <b>zoning</b> applies — township zoning, county "
         "zoning, or municipal — and what a zoning certificate requires. This "
         "is separate from the building code entirely.",
         [("Office", 0.5), ("Answer", 0.5)]),
        "I understand the Residential Code of Ohio governs this house whether "
        "or not anyone inspects it, and that the electrical standard is the "
        "2023 National Electrical Code as modified by RCO Chapter 34.",
        "I know that no architect or engineer seal is required for my plans "
        "(§&#160;3791.04(A)(2)(b)), and that a local department cannot add one.",
        "Every subcontractor contract of $25,000 or more will be in writing "
        "and will include the certificate of insurance §&#160;4722.02(A) requires.",
        "I have decided deliberately, in writing, whether any contract is "
        "cost-plus — knowing that cost-plus waives the written-contract "
        "mandate, the change-order estimate and the 10% deposit cap.",
        "I will pay each direct contractor in full only against a sworn "
        "affidavit that those below them are paid (§&#160;1311.011(B)(6)), and I "
        "will use joint checks where a sub is exposed.",
        ("If this is a three-family dwelling, I have read the seam paragraph "
         "above and taken advice — the payment defense and the 60-day lien "
         "window do not reach it. Not applicable / advice taken:",
         [("Answer", 1.0)]),
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "oh-permit-kit",
                       "OH.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
