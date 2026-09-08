#!/usr/bin/env python3
"""NE.1 What Binds You and Who Can Stop You.

Every other state's document 1 in this series walks an owner-builder
exemption. Nebraska has none, because it has nothing to be exempt FROM: no
state contractor license exists, and the Contractor Registration Act says in
one sentence that an owner working on their own property "is not a contractor."
So the document that earns its place here answers the question Nebraska
actually poses: the 2018 IRC and UPC are "the legally applicable code
regardless of whether the county, city, or village has provided for the
administration or enforcement" of them (§ 71-6406(7)), nobody has to permit or
inspect a house, the state may not — and yet four state obligations reach every
house anyway, enforced by mechanisms that do not need a building department.

Every Nebraska claim in this document was read against its primary source in
September 2026 and is cited on-page. Statutes are the Revised Statutes as
published at nebraskalegislature.gov; each page carries a Source line and, for
2026 amendments, an Effective Date line, both of which were read.

Verified sources:
  § 71-6403(1)-(2)   2018 IBC/IRC/IEBC/UPC adopted by reference; IRC R313 and
                     chapters 25-33 excluded; RRNC folded in. Last amended 2021.
  § 71-6404(2)       where the state code applies (state buildings; adopters;
                     non-adopters after two years)
  § 71-6406(1)(b),(3)(a),(5),(7)  the default, the no-older-edition rule, and
                     the sentence that makes the code apply without enforcement
  § 71-6407          farm buildings; nothing authorizes a state agency to
                     regulate them
  § 71-6409          (eff. 7-18-2026) virtual inspections; no self-inspection
  § 23-114.03-.05    county zoning permits for nonfarm buildings; farmstead
                     residences at the county's option; Class III misdemeanor
  § 14-419, § 15-905 city regulation in the extraterritorial zoning jurisdiction
  § 81-2121(5)       the electrical homeowner exemption — a LICENSE exemption
  § 81-2124(3)       new single-family service equipment is inspected
  § 81-2126          request at or before commencement; $250 late fee
  § 81-2129          no connection without the owner's certificate
  § 81-2143          (as amended by LB889, eff. 7-18-2026) Class IV felony
  § 81-2102(4),(5),(17)  Class B licensees confined to municipalities under
                     100,000; "special electrician" covers HVAC and well pumps
  § 81-1609(2)       "contractor" = whoever is responsible for the overall
                     construction — the owner-builder
  § 81-1622, -1625, -1626  the builder's own energy duty; two-year order;
                     Class IV misdemeanor
  § 18-132(4), § 23-172(4),(6)  2018 UPC is the default plumbing code; no duty
                     to inspect
  § 18-1901          municipal plumbing boards (Omaha shall; Lincoln may)
  § 46-1233(2)       owner may drill a well on abode land
  § 81-15,248(1); Title 124 ch. 9 § 004  owner may NOT install septic;
                     "physically present at the site"
  § 48-2103(3), -2104(1), -2105, -2107, -2114, -2117  Contractor Registration Act
  § 48-116           statutory employer; cure = require the contractor's policy
  § 52-129, -135, -136, -137  Construction Lien Act; protected party; 120 days
  § 76-2,120(6)(k)   seller disclosure exemption for never-occupied new houses

DELIBERATELY NOT CLAIMED, and why:
  - That an owner-builder is outside the Workers' Compensation Act. §§ 48-106
    and 48-115 support it on their face, but a tribunal decides "usual course"
    on facts; the document prints the § 48-116 certificate rule instead.
  - That a relative may wire the house. § 81-2143(2) narrows one felony; it
    does not amend the § 81-2108 license requirement. Printed for accuracy only.
  - That a farmhouse is exempt from the code. The farm carve-out lives in the
    default path only and is undefined; § 23-114.03 makes a farmstead residence
    the county's call.
  - Any count of counties with a building-permit program. No primary source
    exists; the statute makes it optional and unreported.
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
CITE = k.CITE_COL

FORM_ID = "NE.1"
FORM_TITLE = "What Binds You and Who Can Stop You"
TOPIC = "Who Enforces"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The code applies to your house whether or not anyone checks — and the "
    "four state obligations that reach a rural parcel with no building "
    "department at all.")

flow.append(k.disclaimer(
    "Two sections quoted here were amended in 2026 and carry an Effective Date "
    "line on the statute page. Older agency documents — including the State "
    "Electrical Division's own rules — have not caught up. Where they "
    "disagree, this document prints the statute and says so."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION", reserve=2.0)
flow.append(k.body(
    "Nebraska has no owner-builder exemption because it has nothing to be "
    "exempt from. There is no state contractor license, no state building "
    "permit, and no state building inspector for a private house. What there "
    "is instead is a code that binds you <b>by statute</b>, and a short list "
    "of state obligations that reach every house through the power company, "
    "your own signature, and the professionals you are required to use."))
rows = [
    [k.cellp("Do you need a license to build your own house?"),
     k.cellp(f"<b>No.</b> Nebraska issues no general contractor license. The "
             f"Contractor Registration Act says a person \"who performs work "
             f"or has work performed on his or her own property … is not a "
             f"contractor\" ({sec('48-2104(1)')})")],
    [k.cellp("Does the building code apply if nobody inspects?"),
     k.cellp(f"<b>Yes.</b> The 2018 IRC and UPC are \"the legally applicable "
             f"code regardless of whether the county, city, or village has "
             f"provided for the administration or enforcement\" "
             f"({sec('71-6406(7)')})")],
    [k.cellp("Does anyone have to issue a building permit?"),
     k.cellp("<b>No.</b> A local government \"may\" adopt permits and "
             "inspections; nothing says it must, and nothing lets a state "
             "agency inspect a private house. Where a county chose to run a "
             "program, its rules apply. Where it did not, nobody's do")],
    [k.cellp("Is there a frequency limit or a sale test?"),
     k.cellp("<b>None.</b> No statute caps how often you may build for "
             "yourself. But building \"to be held … for sale or rental\" makes "
             f"you a contractor ({sec('48-2103(3)')}), and a house that is "
             "not your principal residence is outside the electrical "
             f"exemption ({sec('81-2121(5)')})")],
    [k.cellp("Can you wire your own house?"),
     k.cellp(f"<b>Yes, and it will be inspected.</b> The homeowner exemption "
             f"is from the <i>license</i> ({sec('81-2121(5)')}). A new "
             f"service is inspected everywhere ({sec('81-2124(3)')}), the "
             f"utility may not connect you until you certify the request was "
             f"filed ({sec('81-2129')}), and not filing is a felony "
             f"({sec('81-2143(1)(c)')})")],
    [k.cellp("Can you do your own plumbing and HVAC?"),
     k.cellp("<b>No state license exists for either.</b> The plumbing "
             "standard is the 2018 UPC everywhere; a city may license "
             "plumbers by ordinance and require a permit. Ask the city")],
    [k.cellp("Can you drill your own well? Install your own septic?"),
     k.cellp(f"<b>Well, yes</b> — on land you own and use as your abode "
             f"({sec('46-1233(2)')}). <b>Septic, no</b> — a certified "
             f"installer, engineer or environmental health specialist must be "
             f"physically present ({sec('81-15,248(1)')}; Title 124 ch. 9 "
             f"§{NB}004)")],
    [k.cellp("Who checks the energy code?"),
     k.cellp(f"<b>You do.</b> With no local energy code, \"the prime "
             f"contractor shall build … to the best of his or her knowledge, "
             f"according to the Nebraska Energy Code\" ({sec('81-1622(1)')}) "
             f"— and the owner-builder is the contractor ({sec('81-1609(2)')})")],
]
flow.append(k.ref_table(
    "The Nebraska position at a glance",
    [k.cellp("Question", bold=True), k.cellp("Nebraska's answer", bold=True)],
    rows, [2.2 * inch, CW - 2.2 * inch]))
flow.append(k.cite(
    "Statutes read at nebraskalegislature.gov in September 2026. The Building "
    "Construction Act is §§ 71-6401 to 71-6409; the State Electrical Act "
    "§§ 81-2101 et seq.; the Nebraska Energy Code §§ 81-1608 to 81-1626; the "
    "Contractor Registration Act §§ 48-2101 to 48-2117."))

# ---------------------------------------------------------------- the sentence
flow += k.h2_tight("THE SENTENCE THAT DECIDES YOUR BUILD", reserve=2.4)
flow.append(k.body(
    "Most states adopt a code and then require somebody to enforce it. "
    "Nebraska adopts a code, tells every local government it <i>may</i> "
    "enforce it, and then closes the obvious gap with one sentence at the end "
    "of the local-option section:"))
flow.append(k.callout_long(
    f"Neb. Rev. Stat. {sec('71-6406')} — the code that applies whether or not "
    f"anyone enforces it", [
        Paragraph("\"(1)(a) Any county, city, or village <b>may</b> enact, "
                  "administer, or enforce a local building or construction "
                  "code if or as long as such county, city, or village: (i) "
                  "Adopts the state building code; or (ii) Adopts a building "
                  "or construction code that conforms generally with the "
                  "state building code.", S["body"]),
        Paragraph("(b) If a county, city, or village does not adopt a code as "
                  "authorized under subdivision (a) of this subsection within "
                  "two years after an update to the state building code, "
                  "<b>the state building code shall apply</b> in the county, "
                  "city, or village, except that such code shall not apply to "
                  "construction on a farm or for farm purposes.\"", S["body"]),
        Paragraph("\"(7) A county, city, or village <b>may</b> adopt "
                  "amendments for the proper administration and enforcement "
                  "of its local building or construction code including "
                  "organization of enforcement, qualifications of staff "
                  "members, examination of plans, inspections, appeals, "
                  "permits, and fees. … Any local building or construction "
                  "code adopted under subdivision (1)(a) of this section or "
                  "the state building code if applicable under subdivision "
                  "(1)(b) of this section <b>shall be the legally applicable "
                  "code regardless of whether the county, city, or village "
                  "has provided for the administration or enforcement</b> of "
                  "its local building or construction code under this "
                  "subsection.\"", S["body"]),
    ]))
flow.append(k.cite(
    f"The state building code itself is {sec('71-6403(1)')}: the <b>2018 "
    f"International Building Code</b>, the <b>2018 International Residential "
    f"Code</b> \"except section R313 and chapters 25 through 33,\" the 2018 "
    f"International Existing Building Code, and the <b>2018 Uniform Plumbing "
    f"Code</b> — plus the radon-resistant construction standards of "
    f"{sec('76-3504')} ({sec('71-6403(2)')}). Its Source line ends with a 2021 "
    f"conforming amendment; <b>no newer edition has been adopted as of "
    f"September 2026</b>, and only the Legislature can change it."))

flow.append(Spacer(1, 4))
rows = [
    [k.cellp("<b>The code binds without a permit</b>"),
     k.cellp("Read the last sentence of (7) again. It is written for exactly "
             "the county that never set up a building department. The 2018 "
             "IRC is the standard your house must meet there, and a buyer, "
             "lender, insurer or court will measure it against that standard"),
     k.cellp(sec("71-6406(7)"))],
    [k.cellp("<b>Nobody has to permit or inspect</b>"),
     k.cellp("\"May,\" three times. Nothing in the Act requires any county, "
             "city or village to issue a permit, review a plan or inspect. "
             "And the only place the Act sends a state inspector is a "
             "<i>state-owned</i> building — the state has no residential "
             "permit program"),
     k.cellp(f"{sec('71-6406(7)')}; {sec('71-6405(1)')}")],
    [k.cellp("<b>No local government may run an older edition</b>"),
     k.cellp("A local code \"shall not be deemed to conform\" if it \"includes "
             "a prior edition of any component\" of the state code, or omits "
             "radon-resistant construction. A county telling you it is still "
             "on the 2012 IRC is telling you something the statute forbids"),
     k.cellp(f"{sec('71-6406(3)')}, (5)")],
    [k.cellp("<b>A local government may run a newer one</b>"),
     k.cellp("Adopting \"any supplement, new edition, appendix, or "
             "component\" still conforms. Lincoln is on the 2021 IRC and UPC "
             "for that reason. So the state edition is a <i>floor</i>; ask "
             "the city which it reviews to"),
     k.cellp(sec("71-6406(2)(b)"))],
    [k.cellp("<b>Plumbing is the UPC, not the IRC chapters</b>"),
     k.cellp("IRC chapters 25–33 are its plumbing chapters, and they are "
             "excluded because Nebraska adopted the Uniform Plumbing Code "
             "instead. Where no city or county plumbing code exists, the 2018 "
             "UPC \"shall apply to all buildings\" — with \"no obligation … "
             "to inspect\""),
     k.cellp(f"{sec('71-6403(1)(b)')}, (d); {sec('23-172(4)')}, (6); "
             f"{sec('18-132(4)')}")],
]
flow.append(k.ref_table(
    "What falls out of that sentence",
    [k.cellp("", bold=True), k.cellp("What it means for you", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.65 * inch, CW - 1.65 * inch - CITE, CITE]))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "New in 2026: virtual inspections, and the one thing they can never be", [
        Paragraph(f"Laws 2026, LB441 added {sec('71-6409')}, effective "
                  f"<b>July 18, 2026</b>. Any permitting entity may now "
                  f"\"allow for virtual inspection by an authorized "
                  f"inspector\" of a one- or two-family dwelling under three "
                  f"stories and under 10,000{NB}sq{NB}ft, conducted live, and "
                  f"may accept photo or video for nonstructural "
                  f"reinspections. The definition then closes a door: "
                  f"\"<b>Authorized inspector does not include an individual "
                  f"performing a self-performed inspection for the "
                  f"individual's own permit or building.</b>\"", S["body"]),
        Paragraph("Two things follow. Whatever a county offers, it may not "
                  "let you inspect yourself. And the virtual path is "
                  "conditioned on naming \"the contractor who is licensed or "
                  "registered … and who is completing the work\" — which an "
                  "owner doing the work personally is not. The text does not "
                  "resolve whether an owner-builder can use it. <b>Ask whether "
                  "your county will extend it, and do not assume.</b>",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- farm & zoning
flow += k.h2_tight("THE FARM CARVE-OUT, AND THE ZONING PERMIT THAT SURVIVES "
                   "EVERYTHING", reserve=2.2)
flow.append(k.body(
    "The state-code default \"shall not apply to construction on a farm or "
    f"for farm purposes\" ({sec('71-6406(1)(b)')}), and nothing in the Act "
    f"authorizes \"any state agency or political subdivision to regulate the "
    f"construction of farm buildings\" where that is otherwise prohibited "
    f"({sec('71-6407')}). <b>Do not build a farmhouse on that sentence.</b> "
    f"Three things about it:"))
flow.append(k.bullet(
    "\"On a farm or for farm purposes\" is <b>not defined</b> anywhere in the "
    "Act, and the carve-out is written into the <i>default</i> path only — a "
    "county that adopted its own code is not, by this section, kept off farm "
    "construction."))
flow.append(k.bullet(
    f"The county zoning statute defines the farm exemption for its own "
    f"purposes as buildings \"utilized for agricultural purposes on a "
    f"farmstead of <b>twenty acres or more</b> which produces <b>one thousand "
    f"dollars or more</b> of farm products each year\" — and then says "
    f"outright: \"<b>The county board may decide whether buildings located on "
    f"farmsteads used as residences shall be subject to such county's zoning "
    f"regulations and permit requirements.</b>\" ({sec('23-114.03')})"))
flow.append(k.bullet(
    "A dwelling is a residence first and a farm building second. Whether "
    "your farmstead house needs a county permit is the county board's call, "
    "farm by farm. <b>Ask the county in writing before you rely on it.</b>"))
flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Even with no building code, a county may require a ZONING permit for "
    "the house", [
        Paragraph(f"\"The county board shall provide for enforcement of the "
                  f"zoning regulations within its county by requiring the "
                  f"issuance of permits prior to the erection, construction, "
                  f"reconstruction, alteration, repair, or conversion of any "
                  f"nonfarm building or structure within a zoned area\" "
                  f"({sec('23-114.04(1)')}). That permit \"shall not be issued "
                  f"unless the plans … <b>including sanitation, plumbing and "
                  f"sewage disposal</b>, are filed in writing in the building "
                  f"inspector's office and such plans fully conform to all "
                  f"zoning regulations\" ({sec('23-114.04(2)')}).", S["body"]),
        Paragraph(f"Building \"without having first obtained a permit\" is a "
                  f"<b>Class III misdemeanor</b>, each day a separate offense "
                  f"after notice ({sec('23-114.05')}). This is a zoning "
                  f"permit, not a code permit — it exists in counties that "
                  f"never adopted a building code — and it is the reason the "
                  f"septic design has to exist before the county will look at "
                  f"the house.", S["body"]),
        Paragraph(f"<b>And near a city, the city may govern.</b> A county's "
                  f"codes reach \"all of the county except within the limits "
                  f"of any incorporated city or village and except within an "
                  f"unincorporated area where a city or village has been "
                  f"granted zoning jurisdiction\" ({sec('23-172(5)')}). Omaha "
                  f"regulates construction, \"electric wiring, heating, "
                  f"plumbing, pipefitting\" across its three-mile "
                  f"extraterritorial zone ({sec('14-419(1)')}–(2)); Lincoln "
                  f"has the same power under {sec('15-905')}. A rural-looking "
                  f"parcel a few miles out may be under city rules.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- four things
flow += k.h2_tight("THE FOUR THINGS THAT REACH YOUR HOUSE ANYWAY",
                   reserve=2.4)
flow.append(k.body(
    "This is the page to keep. Outside a city or county that runs a program, "
    "no building official will ever visit — and every one of these still "
    "applies, because each is enforced by something other than a building "
    "department."))
rows = [
    [k.cellp("<b>1. State electrical inspection</b>"),
     k.cellp("Every new single-family installation \"requiring new electrical "
             "service equipment\" is inspected — by the State Electrical "
             "Division, or by a local certified inspector where the city or "
             "county runs its own program"),
     k.cellp("<b>The power company.</b> No connection until your certificate "
             "that inspection was requested is on file with the utility, "
             "which \"may refuse service without liability\""),
     k.cellp(f"{sec('81-2124(3)')}; {sec('81-2129')}")],
    [k.cellp("<b>2. Nebraska Energy Code</b>"),
     k.cellp("The 2018 IECC, unamended, statewide, for every building started "
             "on or after July 1, 2020. No exemption for a house, a farm "
             "dwelling or an owner-built home"),
     k.cellp("<b>You.</b> The prime contractor — the owner-builder — \"shall "
             "build … according to the Nebraska Energy Code.\" Two-year "
             "post-occupancy correction order; Class IV misdemeanor"),
     k.cellp(f"{sec('81-1614')}; {sec('81-1622')}; {sec('81-1625')}; "
             f"{sec('81-1626')}")],
    [k.cellp("<b>3. Septic registration</b>"),
     k.cellp("No onsite wastewater system may be sited, laid out, built or "
             "inspected except by or under a certified professional, "
             "engineer or environmental health specialist who is physically "
             "on site"),
     k.cellp("<b>The professional.</b> They must register the system with "
             "DWEE within 45 days of completion and hand you a copy. Civil "
             "penalty up to $10,000 per violation per day"),
     k.cellp(f"{sec('81-15,248(1)')}–(2); {sec('81-15,253')}; Title 124 "
             f"ch. 9 §{NB}004")],
    [k.cellp("<b>4. Well registration</b>"),
     k.cellp("Every well is registered with DWEE within 60 days of "
             "completion, with the well log — by the licensed driller, or "
             "\"the owner of the water well if the owner constructed the "
             "water well\""),
     k.cellp("<b>You, or your driller.</b> An unregistered well is the "
             "record that is missing when you sell; a licensee who fails to "
             "file is subject to discipline"),
     k.cellp(f"{sec('46-602(1)')}; {sec('46-1241')}; {sec('46-1235')}")],
]
flow.append(k.ref_table(
    "Statewide, whoever does or does not run a building department",
    [k.cellp("Obligation", bold=True), k.cellp("What it requires", bold=True),
     k.cellp("Who enforces it, and how", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.2 * inch, (CW - 1.2 * inch - CITE) * 0.5,
           (CW - 1.2 * inch - CITE) * 0.5, CITE]))
flow.append(k.cite(
    f"A fifth applies by statute but is checked by nobody outside a local "
    f"program: <b>radon-resistant new construction</b>, required of every "
    f"regularly occupied building built after September 1, 2019 "
    f"({sec('76-3504')}), with two exemptions — an architect- or "
    f"engineer-designed project, and the counties DHHS lists below "
    f"2.7{NB}pCi/L ({sec('76-3505')}). NE.2 prints the standard and the county "
    f"list."))

# ---------------------------------------------------------------- electrical
flow += k.h2_tight("ELECTRICAL — A LICENSE EXEMPTION, NOT AN INSPECTION "
                   "EXEMPTION", reserve=2.4)
flow.append(k.body(
    "The State Electrical Act licenses anyone who wires \"for another\" "
    f"({sec('81-2106')}, {sec('81-2108')}), and then carves you out in one "
    f"subdivision. Read the carve-out exactly, because guides routinely add "
    f"conditions that are not in it and drop the ones that are."))
flow.append(k.callout(
    f"Neb. Rev. Stat. {sec('81-2121')} — the homeowner exemption, verbatim", [
        Paragraph("\"Nothing in the State Electrical Act shall be construed "
                  "to: … (5) Prohibit an owner of property from performing "
                  "work on his or her <b>principal residence, if such "
                  "residence is not larger than a single-family dwelling, or "
                  "farm property</b>, excluding commercial or industrial "
                  "installations or installations in public-use buildings or "
                  "facilities, <b>or require such owner to be licensed under "
                  "the act</b>.\"", S["body"]),
    ]))
flow.append(k.bullet(
    "It exempts you from the <b>license</b>. It says nothing about "
    f"inspection or the request for inspection; those live in {sec('81-2124')} "
    f"and {sec('81-2126')}, and they apply to you."))
flow.append(k.bullet(
    "\"Principal residence … not larger than a single-family dwelling\" — a "
    "duplex, a spec house, a rental or a second home is outside it. \"Farm "
    "property\" is a separate category."))
flow.append(k.bullet(
    "It does <b>not</b> say \"without compensation\" and it does <b>not</b> say "
    "you must personally do the work. Those conditions appear in published "
    "guides; they are not in the statute or in the State Electrical "
    "Division's own homeowner handout. What the handout does require is a "
    "signed <b>homeowner verification</b> that you know the code and the Act "
    "before a permit is issued to you."))
flow.append(Spacer(1, 4))
rows = [
    [k.cellp("<b>A new house is inspected, everywhere</b>"),
     k.cellp("\"All new electrical installations for single-family "
             "residential applications <b>requiring new electrical service "
             "equipment</b> shall be subject to the inspection and "
             "enforcement provisions of the act.\" A new house has new "
             "service equipment. State inspection yields only to a county, "
             "city or village that inspects with its own certified "
             f"inspector by ordinance ({sec('81-2125(1)')}) — NE.4 has the "
             f"map"),
     k.cellp(sec("81-2124(3)"))],
    [k.cellp("<b>The request is due before you start</b>"),
     k.cellp("\"At or before commencement of any installation required to be "
             "inspected by the board, the licensee <b>or owner</b> making "
             "such installation shall submit to the board a request for "
             "inspection … together with … the inspection fees.\" If the "
             "board learns you did not, it sends a certified letter giving "
             "14 days; \"Any person filing a late request for inspection "
             "shall pay a delinquent fee of <b>two hundred fifty "
             "dollars</b>,\" and after the 14 days the file goes to the "
             "county attorney"),
     k.cellp(sec("81-2126"))],
    [k.cellp("<b>The meter is the checkpoint</b>"),
     k.cellp("\"No electrical installation subject to inspection by the "
             "board shall be newly connected or reconnected for use until "
             "there is filed with the electrical utility supplying power a "
             "<b>certificate of the property owner</b> or licensed "
             "electrician directing the work that inspection has been "
             "requested and that the conditions of the installation are safe "
             "for energization. … Any supplier may refuse service without "
             "liability for such refusal until such conditions have been met\""),
     k.cellp(sec("81-2129"))],
    [k.cellp("<b>Why the utility will insist</b>"),
     k.cellp("On inspection and approval, \"all liability upon any supplier "
             "of electrical service for subsequent damage or loss arising "
             "from any installation shall be terminated.\" The power company "
             "has a statutory reason to want the inspection done, and the "
             "Division forwards a copy of a new-service permit to the "
             "supplier"),
     k.cellp(sec("81-2133"))],
]
flow.append(k.ref_table(
    "What still applies to you, in the statute's words",
    [k.cellp("", bold=True), k.cellp("What the section says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.55 * inch, CW - 1.55 * inch - CITE, CITE]))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Since July 18, 2026, not filing is a felony — and the Division's own "
    "documents still say misdemeanor", [
        Paragraph(f"Laws 2026, LB889 (approved April 14, 2026; effective "
                  f"<b>July 18, 2026</b>) struck \"Class I misdemeanor\" from "
                  f"{sec('81-2143(1)')} and inserted \"<b>Class IV "
                  f"felony</b>.\" The section now reads: \"It shall be a Class "
                  f"IV felony to knowingly and willfully commit … (a) To make "
                  f"a false statement in any … request for inspection, "
                  f"certificate, or other lawfully authorized or required "
                  f"form …; (b) To perform electrical work for another without "
                  f"a proper license … while claiming to have such license; "
                  f"<b>(c) To fail to file a request for inspection when "
                  f"required</b>; (d) To interfere with or refuse entry to an "
                  f"inspector …; or (e) To fail or neglect to comply with the "
                  f"act or any lawful rule, regulation, or order of the "
                  f"board.\"", S["body"]),
        Paragraph("Note (a): the homeowner verification you sign is one of "
                  "those forms. Note also what has <i>not</i> caught up. The "
                  "State Electrical Board Rules PDF dated April 23, 2024 "
                  "(Rule 13) still says a person \"may be guilty of a "
                  "misdemeanor under §81-2143,\" and every pre-2026 guide "
                  "repeats it. The slip law was read; the statute page "
                  "carries the Effective Date. <b>The statute wins.</b>",
                  S["body"]),
        Paragraph(f"The same bill added a family carve-out, "
                  f"{sec('81-2143(2)')}: subdivision (1)(b) — the <i>unlicensed "
                  f"work while claiming a license</i> felony — \"shall not be "
                  f"construed to prohibit a person from performing electrical "
                  f"work for such person's parent, stepparent, spouse, "
                  f"descendant, grandparent, brother, sister, cousin, uncle, "
                  f"or aunt … without a license.\" <b>Printed for accuracy, "
                  f"not as permission.</b> It narrows one felony. It does not "
                  f"amend the {sec('81-2108')} license requirement, and the "
                  f"installation is inspected either way. Whether it reaches "
                  f"the license rule is untested.", S["body"]),
    ]))

flow.append(Spacer(1, 4))
rows = [
    [k.cellp("<b>The furnace and condenser wiring is a licensed specialty</b>"),
     k.cellp("\"Special electrician\" covers \"well pump wiring, air "
             "conditioning and refrigeration installation.\" Your own furnace "
             "wiring is inside your exemption; a hired HVAC installer wiring "
             "the unit is not, unless licensed for it. A licensed pump "
             "installer may wire a well pump \"to the first control\" without "
             "an electrical license"),
     k.cellp(f"{sec('81-2102(17)')}; {sec('81-2121(7)')}")],
    [k.cellp("<b>A Class B electrician cannot work in Omaha or Lincoln</b>"),
     k.cellp("Class B contractors and journeymen are confined to residential "
             "work up to 400 amps \"in any municipality which has a population "
             "of less than one hundred thousand.\" Relevant when hiring: check "
             "the class of license against the city"),
     k.cellp(f"{sec('81-2102(4)')}–(5)")],
    [k.cellp("<b>The Division misquotes its own statute</b>"),
     k.cellp("The homeowner handout (May 2024) prints the exemption as work on "
             "a \"principal residence or/arm property\" — dropping the \"not "
             "larger than a single-family dwelling\" limit and garbling \"or "
             "farm.\" The statute controls; it is quoted above"),
     k.cellp("SED handout; " + sec("81-2121(5)"))],
]
flow.append(k.ref_table(
    "Three details that decide who may touch the wiring",
    [k.cellp("", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.8 * inch, CW - 1.8 * inch - CITE, CITE]))
flow.append(k.cite(
    "The electrical code itself is the <b>2023 NEC</b>, effective August 1, "
    f"2024, with five sections held at their 2017 text ({sec('81-2104(5)')}) — "
    f"NE.2 lists them. The request-for-inspection form, fees, clocks and "
    f"permit life are in NE.2 and NE.3."))

# ---------------------------------------------------------------- energy
flow += k.h2_tight("ENERGY — THE CODE YOU ENFORCE ON YOURSELF", reserve=2.2)
flow.append(k.body(
    "There is no state energy permit, no state energy inspection on request, "
    "and no state certificate. What the statute does instead is name the "
    "person responsible and give them a duty:"))
flow.append(k.callout(
    f"Neb. Rev. Stat. {sec('81-1622')} — where no local energy code exists", [
        Paragraph("\"(1) When no architect or engineer is retained, <b>the "
                  "prime contractor shall build or cause to be built, to the "
                  "best of his or her knowledge, according to the Nebraska "
                  "Energy Code</b>; and (2) When an architect or engineer is "
                  "retained: (a) The architect or engineer shall place his or "
                  "her state registration seal on all construction drawings "
                  "which shall indicate that the design meets the Nebraska "
                  "Energy Code and (b) the prime contractor responsible for "
                  "the actual construction shall build or cause to be built "
                  "in accordance with the construction documents prepared by "
                  "the architect or engineer.\"", S["body"]),
    ]))
rows = [
    [k.cellp("<b>Who the \"contractor\" is</b>"),
     k.cellp("\"The person or entity responsible for the overall construction "
             "of any building.\" On an owner-built house that is you"),
     k.cellp(sec("81-1609(2)"))],
    [k.cellp("<b>What it is</b>"),
     k.cellp("\"The 2018 International Energy Conservation Code,\" applied to "
             "every building started on or after July 1, 2020. Exemptions: "
             "unheated and uncooled buildings, federal buildings, "
             "manufactured and modular units, historic buildings. <b>Not "
             "houses, not farm dwellings, not owner-builders</b>"),
     k.cellp(f"{sec('81-1609(9)')}; {sec('81-1614')}; {sec('81-1615')}")],
    [k.cellp("<b>The two-year window</b>"),
     k.cellp("If the Director of DWEE \"or the local code authority finds, "
             "within two years from the date a building is first occupied,\" "
             "that it did not comply, they \"may order the owner or prime "
             "contractor to take those actions necessary to bring the "
             "building into compliance\""),
     k.cellp(sec("81-1625"))],
    [k.cellp("<b>The penalty</b>"),
     k.cellp("Failure to comply, or \"ordering, instructing, or directing "
             "another not to comply,\" is a Class IV misdemeanor"),
     k.cellp(sec("81-1626"))],
    [k.cellp("<b>How anyone would find out</b>"),
     k.cellp("Inspections \"shall be conducted only after permission has been "
             "granted by the owner or occupant or after a warrant has been "
             "issued.\" And \"a building owner may submit a written request "
             "that the department undertake a determination\" — the "
             "complaint path a later buyer holds"),
     k.cellp(f"{sec('81-1617')}; {sec('81-1616')}")],
    [k.cellp("<b>The local option</b>"),
     k.cellp("Any county, city or village \"may adopt and enforce a local "
             "energy code,\" charge fees, and waive a specific requirement it "
             "finds \"not economically justified\" after filing its analysis "
             "with DWEE. Where one exists, its inspections apply"),
     k.cellp(sec("81-1618"))],
]
flow.append(k.ref_table(
    "The Nebraska Energy Code in six rules",
    [k.cellp("", bold=True), k.cellp("What the statute says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - CITE, CITE]))
flow.append(k.cite(
    "DWEE's energy-code page (September 2026) says that where no local code "
    "exists its Planning and Aid Division \"will enforce the code.\" Read with "
    f"{sec('81-1622')}, that means the determination-on-request and the "
    f"two-year order above — not a permit and not a routine visit. The 2018 "
    f"IECC prescriptive values, the blower-door limit and the climate zone are "
    f"in NE.2."))

# ---------------------------------------------------------------- own hands
flow += k.h2_tight("WHAT YOU MAY DO WITH YOUR OWN HANDS", reserve=2.4)
rows = [
    [k.cellp("<b>Electrical</b>"),
     k.cellp("<b>Yes</b>, on your principal residence (single-family) or farm "
             "property, without a license"),
     k.cellp("Inspected regardless; request filed before you start; utility "
             "holds the meter until you certify; homeowner verification "
             "signed"),
     k.cellp(f"{sec('81-2121(5)')}; {sec('81-2124(3)')}; {sec('81-2126')}; "
             f"{sec('81-2129')}")],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp("<b>No state license exists</b> for plumbers at all. The "
             "standard is the 2018 UPC everywhere a city or county has not "
             "adopted its own"),
     k.cellp("Omaha <i>shall</i> and Lincoln <i>may</i> have a plumbing "
             "board whose plumbers are \"licensed within such cities\"; the "
             "board may compel plans to be submitted. Lincoln issues a "
             "homeowner plumbing permit for a primary residence. Ask the "
             "city; outside one, nobody has to inspect"),
     k.cellp(f"{sec('18-1901(1)')}, (6); {sec('18-1906')}; "
             f"{sec('18-132(4)')}; {sec('23-172(4)')}")],
    [k.cellp("<b>Mechanical</b><br/>(HVAC)"),
     k.cellp("<b>No state license or permit.</b> Verified by reading the full "
             "section indexes of Chapters 18, 38, 71 and 81 — the only hits "
             "are municipal plumbing boards and the electrical specialty"),
     k.cellp("The standard is the 2018 IRC's own chapters 12–24, which were "
             "adopted. The <i>wiring</i> of the unit is a licensed electrical "
             "specialty if anyone but you does it"),
     k.cellp(f"{sec('71-6403(1)(b)')}; {sec('81-2102(17)')}")],
    [k.cellp("<b>Water well</b>"),
     k.cellp("<b>Yes.</b> \"An individual may construct a water well or "
             "install and repair pumps and pumping equipment onsite on land "
             "owned by him or her and used by him or her for farming, "
             "ranching, or agricultural purposes or as his or her place of "
             "abode\""),
     k.cellp("To the Title 134 construction standards — the exemption is "
             "from the license, not the standard. You register it within 60 "
             "days and keep the well log"),
     k.cellp(f"{sec('46-1233(1)')}–(2); {sec('46-602(1)')}; "
             f"{sec('46-1241')}")],
    [k.cellp("<b>Septic</b>"),
     k.cellp("<b>No.</b> No system \"shall be sited, laid out, constructed … "
             "or inspected unless\" the work \"is carried out or supervised "
             "by\" a certified professional, a Nebraska-licensed engineer or "
             "a registered environmental health specialist"),
     k.cellp("And \"supervised\" means present: no one may do the work "
             "unless the responsible installer, engineer or specialist \"is "
             "physically present at the site where such work is being "
             "performed.\" You may dig beside a Master Installer who stays "
             "on site. You may not build it alone"),
     k.cellp(f"{sec('81-15,248(1)')}; Title 124 ch. 9 §{NB}004")],
]
flow.append(k.ref_table(
    "Five trades, five different answers",
    [k.cellp("Trade", bold=True), k.cellp("May you do it yourself?",
                                          bold=True),
     k.cellp("The condition that matters", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.1 * inch, (CW - 1.1 * inch - CITE) * 0.47,
           (CW - 1.1 * inch - CITE) * 0.53, CITE]))
# 1.1in, not 0.95in: at 0.95in "Mechanical" broke as "Mechanica / l" — the
# only split-word hit in the first build of this kit. Size the column, never
# the text.
flow.append(k.cite(
    "There is no statewide plumber registry to search, because plumbing "
    "licenses are city licenses issued under city ordinances. <b>Inside a "
    "city with a plumbing board, ask whether a homeowner may pull the "
    "plumbing permit and write the answer down.</b> Lincoln's conditions are "
    "verified in NE.4; Omaha's could not be read and must be confirmed at the "
    "counter."))

# ---------------------------------------------------------------- registration
flow += k.h2_tight("THE REGISTRATION ACT — YOU ARE OUTSIDE IT; EVERYONE YOU "
                   "HIRE IS INSIDE", reserve=2.2)
flow.append(k.body(
    "Nebraska's only statewide contractor law is a <b>$40 registration</b> "
    "with the Department of Labor, and the Legislature says what it is not: "
    "\"It is not the intent of the Legislature to endorse the quality or "
    f"performance of services provided by any individual contractor\" "
    f"({sec('48-2102')}). It matters to you for one reason — the public "
    f"registry tells you whether the people you hire carry workers' "
    f"compensation."))
rows = [
    [k.cellp("<b>You do not register</b>"),
     k.cellp("\"Any person who performs work or has work performed on his or "
             "her own property … is not a contractor for purposes of the "
             "Contractor Registration Act.\" The Department's own page: a "
             "contractor works on real property \"other than their own "
             "property\""),
     k.cellp(sec("48-2104(1)"))],
    [k.cellp("<b>Every trade you hire does</b>"),
     k.cellp("\"Before performing any construction work in Nebraska, a "
             "contractor shall be registered\" — including \"any "
             "subcontractor\" and anyone \"providing or arranging for labor.\" "
             "Annual fee capped at $40; it reached the cap August 1, 2026"),
     k.cellp(f"{sec('48-2104(1)')}; {sec('48-2103(3)')}; "
             f"{sec('48-2107')}")],
    [k.cellp("<b>What the registry shows</b>"),
     k.cellp("Registration requires \"proof of workers' compensation "
             "insurance, self-insurance, or a signed statement that none is "
             "required,\" and the public database must flag each contractor "
             "as insured, self-insured, or \"a sole proprietor with no "
             "employees and does not carry workers' compensation "
             "insurance.\" Lapse of coverage revokes the registration"),
     k.cellp(f"{sec('48-2105')}; {sec('48-2117(3)')}; {sec('48-2109')}")],
    [k.cellp("<b>What happens if you hire an unregistered one</b>"),
     k.cellp("<b>Nothing, to you.</b> Every duty and penalty in the Act "
             "attaches to the contractor — a citation and an administrative "
             "penalty up to $500, then $5,000. Verified absence: no section "
             "penalizes the person who hires. The reason to check anyway is "
             "the next row"),
     k.cellp(f"{sec('48-2114')}; §§ 48-2101–2117")],
    [k.cellp("<b>A spec builder is a contractor</b>"),
     k.cellp("The definition reaches construction of property \"to be held "
             "either for sale or rental.\" Building to sell is not "
             "owner-building, whatever the permit says — and it also takes "
             "you outside the electrical exemption's \"principal residence\""),
     k.cellp(f"{sec('48-2103(3)')}; {sec('81-2121(5)')}")],
]
flow.append(k.ref_table(
    "The Contractor Registration Act, as it touches an owner-builder",
    [k.cellp("", bold=True), k.cellp("What the Act says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.7 * inch, CW - 1.7 * inch - CITE, CITE]))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Workers' compensation — the one sentence that protects you, and the "
    "honest position on the rest", [
        Paragraph(f"Nebraska treats as an employer anyone \"creating or "
                  f"carrying into operation any scheme, artifice, or device\" "
                  f"to get work done without answering to the workers under "
                  f"the Act, jointly and severally liable with the immediate "
                  f"employer. The same section then says it \"shall not be "
                  f"construed as applying to an owner who lets a contract to a "
                  f"contractor in good faith … <b>if the owner … requires the "
                  f"contractor … to procure a policy or policies of insurance "
                  f"from an insurance company licensed to write such insurance "
                  f"in this state</b>\" ({sec('48-116')}).", S["body"]),
        Paragraph("<b>So the rule is mechanical: require a workers' "
                  "compensation certificate (ACORD 25) from every contractor "
                  "with employees before they start, and check the Department "
                  "of Labor registry flag for anyone who says they have "
                  "none.</b> The Department requires the same certificate of "
                  "every registrant with one or more employees, naming the "
                  "Department as certificate holder.", S["body"]),
        Paragraph(f"On whether an owner-builder who hires a day laborer "
                  f"directly is an \"employer\": the Act applies to an "
                  f"employer who employs \"in the regular trade, business, "
                  f"profession, or vocation of such employer\" "
                  f"({sec('48-106(1)')}), and \"employee\" excludes anyone whose "
                  f"employment is \"not in the usual course of the trade, "
                  f"business, profession, or occupation of his or her "
                  f"employer\" ({sec('48-115')}). Building your own house is "
                  f"not your trade. <b>We are not printing that as a safe "
                  f"harbor</b> — a tribunal decides \"usual course\" on facts, "
                  f"and being wrong carries a Class I misdemeanor plus "
                  f"personal liability ({sec('48-145.01(1)')}). Insure the "
                  f"risk or hire through a registered, insured contractor.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- liens & sale
flow += k.h2_tight("LIENS — YOU ARE A \"PROTECTED PARTY,\" AND IT CHANGES THE "
                   "ARITHMETIC", reserve=2.2)
flow.append(k.body(
    "The Nebraska Construction Lien Act gives a homeowner a status most "
    "states do not: a <b>protected party</b> is \"an individual who contracts "
    "to give a real estate security interest in, or to buy or to have "
    "improved, residential real estate all or a part of which he or she "
    f"occupies or intends to occupy as a residence\" ({sec('52-129(1)(a)')}). "
    f"An owner-builder building their own home is one. Three consequences:"))
rows = [
    [k.cellp("<b>The 120-day clock</b>"),
     k.cellp("A claimant's lien \"does not attach and may not be enforced "
             "unless … not later than one hundred twenty days after his or "
             "her final furnishing of services or materials, he or she has "
             "recorded a lien\""),
     k.cellp(sec("52-137(1)"))],
    [k.cellp("<b>The notice, and its warning</b>"),
     k.cellp("A sub or supplier \"may give notice of the right to assert a "
             "lien to the contracting owner,\" and the notice must carry the "
             "words: \"<b>If you did not contract with the person giving "
             "this notice, any future payments you make in connection with "
             "this project may subject you to double liability.</b>\" The "
             "section applies only when the owner is a protected party — "
             "which is you"),
     k.cellp(f"{sec('52-135(1)')}, (6)")],
    [k.cellp("<b>The cap</b>"),
     k.cellp("Against a protected-party owner, a claimant who is not your "
             "direct contractor is capped at the lesser of their own unpaid "
             "amount or <b>the amount you still owed the prime contractor "
             "when the notice arrived</b>. Payments made in good faith before "
             "notice are \"properly made\""),
     k.cellp(f"{sec('52-136(2)')}, (5)")],
]
flow.append(k.ref_table(
    "What protected-party status does for you",
    [k.cellp("", bold=True), k.cellp("What the Act says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.55 * inch, CW - 1.55 * inch - CITE, CITE]))
flow.append(k.body(
    "<b>The practical rule:</b> keep every \"notice of the right to assert a "
    "lien\" you receive with its date; once one arrives, stop paying the "
    "prime contractor's unpaid balance to anyone else until it is resolved; "
    "and collect a signed lien waiver with every payment to every trade. If "
    "you are your own general contractor, every trade is contracting with "
    "you directly, which makes the waivers the whole of your protection."))
flow.append(Spacer(1, 4))
flow.append(k.callout(
    "When you sell — the disclosure statement, and the exemption you lose by "
    "moving in", [
        Paragraph(f"Every seller of residential real property gives the "
                  f"written disclosure statement ({sec('76-2,120(2)')}) — "
                  f"except on a transfer \"of newly constructed residential "
                  f"real property which has never been occupied\" "
                  f"({sec('76-2,120(6)(k)')}). An owner-builder who lives in "
                  f"the house and sells later is inside the statute. The "
                  f"statement is \"to the best of the seller's belief and "
                  f"knowledge,\" and the seller is not liable for errors "
                  f"\"not within the personal knowledge of the seller\" "
                  f"((5), (8)) — which, for the person who built the house, "
                  f"is a narrower shield than usual. The inspection log and "
                  f"the registrations in NE.3 are what you will be disclosing "
                  f"from.", S["body"]),
    ]))

# ---------------------------------------------------------------- checklist
# 2.6in, not 1.6in: the section above ends about 1.7in from the foot of its
# page, and at 1.6in the heading sat alone as the last line of page 13.
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS WITH A PEN",
                   reserve=2.6)
flow += k.check_table(
    "Confirm each of these before you break ground",
    [
        ("I asked the county clerk whether a building code was adopted by "
         "resolution and whether a zoning permit is required for a nonfarm "
         "dwelling — and, if I am inside a city or its extraterritorial "
         "zone, I asked the city. Answer and date:",
         [("Answer", 0.6), ("Date", 0.4)]),
        ("I looked my parcel up on the State Electrical Division's inspection "
         "map. Electrical inspection where I am building is:",
         [("State / local program", 0.6), ("Date read", 0.4)]),
        "I am the record owner, and this house will be my principal residence "
        "— not a rental, not for sale — so the electrical homeowner exemption "
        "reaches me.",
        "I understand the code binds this house whether or not anyone "
        "inspects it, that I am the \"prime contractor\" for the energy code, "
        "and that a two-year correction order follows first occupancy.",
        ("If I am building on a farmstead, I asked the county board in "
         "writing whether the residence is subject to its zoning permit. "
         "Answer:", [("Answer", 0.6), ("Who told me", 0.4)]),
        ("Every trade I hire appears in the Department of Labor contractor "
         "registry, and I noted each one's workers' compensation flag. "
         "Outstanding:", [("Still to check", 1.0)]),
        ("I collected a workers' compensation certificate (ACORD 25) from "
         "every contractor with employees before they started. Outstanding:",
         [("Still needed from", 1.0)]),
        "I have chosen a certified Master Installer, engineer or environmental "
        "health specialist for the septic system, because I may not build it "
        "myself.",
        ("If I am drilling my own well, I understand the Title 134 standards "
         "apply to me and that I register it within 60 days. Otherwise my "
         "driller's license number:", [("License", 1.0)]),
        ("If I am doing my own wiring, I will file the request for inspection "
         "with the homeowner verification before I start, and I know the "
         "utility will not connect me until I certify it was filed. Filed:",
         [("Date", 0.5), ("Permit number", 0.5)]),
        "I am collecting a signed lien waiver at every payment to every trade, "
        "and I will keep any notice of the right to assert a lien with its "
        "date.",
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ne-permit-kit",
                       "NE.1-what-binds-you-and-who-can-stop-you.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
