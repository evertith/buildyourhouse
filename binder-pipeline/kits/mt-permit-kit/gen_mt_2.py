#!/usr/bin/env python3
"""MT.2 Permit Application Checklist — Montana, land first.

Montana's application problem is not "what goes in the packet." In much of the
state there is no packet, because there is no building permit. The problem is
that the approvals which DO gate the build live in three other titles and are
worked in an order nobody tells you: sanitation approval on the parcel, then
water, then septic, then the small access permits, and only then the permits
people think of as permits.

The document leads with 76-4-121 because it is the single most valuable
sentence in this kit for anyone buying rural land: a statewide prohibition on
erecting or occupying a building that needs water or sewage facilities until
the parcel's sanitation status is resolved. It sits entirely outside the
building-code chapter, so the residential exemption never touches it.

Sources verified August 2026:
  76-4-121              may not erect any building or shelter requiring water
                        or sewage facilities, or occupy any permanent building,
                        until a certificate of subdivision approval, a
                        76-4-127 certification, or a 76-4-125 exemption
  76-4-122(2)(a),(c)    the clerk and recorder may not accept a filing without
                        one of the three; an exemption certification "must
                        quote in its entirety the wording of the applicable
                        exemption"
  76-4-125(1),(3)       the exclusions, and using an exemption in lieu of a
                        certificate of subdivision approval
  76-4-125(2)           a local health officer may require replacement
                        drainfield capacity on a remainder
  85-2-306(2)           inside a controlled ground water area, only by permit
  85-2-306(3)(a)(iii)   outside a stream depletion zone: 35 gpm and 10 acre-feet
  85-2-306(3)(a)(iv)    inside a stream depletion zone: 20 gpm and 2 acre-feet
  85-2-306(3)(a)(iii),(iv)  combined appropriation from the same source by two
                        or more wells exceeding the limit requires a permit
  85-2-306(3)(b)        notice of INTENT filed and AUTHORIZED before
                        appropriating; 10 business days to notify defects;
                        60 days to cure; 5 years to complete
  85-2-306(3)(c),(d)    notice of COMPLETION within 60 days; certificate of
                        water right; date of filing is the priority date
  50-60-102(1)(a),(5)   the building-code exemption and the energy carve-back
  50-60-802(1)          builder self-certification
  bsd.dli.mt.gov        adopted code editions and their June 11, 2022 effective
                        date; the electrical, plumbing, and mechanical permit
                        jurisdiction statements

Still deliberately hedged: the septic permit process itself, which is the
county's under its own regulations — the kit gives the statutory hooks and the
verification step, not a county-by-county answer; every fee; the minimum design
roof snow load, which lives in ARM and which the kit sends the reader to read;
and whether any particular parcel can get a well at all.
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

FORM_ID = "MT.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "Application"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The land approvals that decide whether a Montana parcel can carry a house "
    "at all, then the building permit if one exists, then the electrical "
    "permit that exists either way — in the order you have to work them.")

flow.append(k.disclaimer())
flow.append(Spacer(1, 10))

flow += k.h2_tight("IN MONTANA THE BUILDING DEPARTMENT IS NOT THE PROBLEM")
flow.append(k.body(
    "In most states you start at the building counter. In much of Montana "
    "there is no building counter — and the approvals that can actually stop "
    "your project live in Title 76 (land and subdivisions), Title 85 (water), "
    "and your county's own health regulations. None of them is affected by the "
    "building-code exemption in MT.1, and two of them can take months. Work "
    "them in this order: <b>1. Sanitation status of the parcel. 2. Water. "
    "3. Septic. 4. Access and address. 5. The permits.</b> Items 1 and 2 are "
    "the ones that end projects, and they are the ones people do last."))

# ================================================================ SANITATION
flow += k.h2_tight("1. SANITATION APPROVAL — THE SENTENCE TO READ BEFORE YOU "
                   "BUY LAND")
flow.append(k.body(
    "This is the most important paragraph in the kit for anyone buying rural "
    "Montana land, and it has nothing to do with building permits. It is a "
    "flat statutory prohibition:"))
flow.append(k.callout_long("MCA 76-4-121 — Restrictions on subdivision "
                           "activities", [
    Paragraph("\"<i>A person <b>may not</b> dispose of any lot within a "
              "subdivision, erect any facility for the supply of water or "
              "disposal of sewage or solid waste, <b>erect any building or "
              "shelter in a subdivision that requires facilities for the "
              "supply of water or disposal of sewage or solid waste, or occupy "
              "any permanent buildings</b> in a subdivision until: (1) a "
              "certificate of subdivision approval has been issued pursuant to "
              "76-4-114 indicating that the reviewing authority has approved "
              "the subdivision application and that <b>the subdivision is not "
              "subject to a sanitary restriction</b>; (2) the certifying "
              "authority has provided certification pursuant to 76-4-127 that "
              "the subdivision will be provided with adequate municipal or "
              "county water and/or sewer district facilities and adequate "
              "storm water drainage; or (3) the subdivision is otherwise "
              "exempt from review under 76-4-125.</i>\"", S["body"]),
    Paragraph("Read what it forbids: <b>erecting the building</b>, and "
              "<b>occupying it</b>. Not permitting it — erecting it. So on a "
              "parcel that never cleared sanitation review, the fact that your "
              "county issues no building permit is beside the point: a "
              "different statute, in a different title, administered by a "
              "different agency, already says you may not put the house there. "
              "\"No building permit required\" and \"you may build\" are not "
              "the same sentence, and this is where the difference bites.",
              S["body"]),
]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "So a buildable parcel has one of three things behind it: a <b>certificate "
    "of subdivision approval</b> showing it is not subject to a sanitary "
    "restriction; a <b>76-4-127 certification</b> that municipal or county "
    "water and sewer will serve it; or a properly claimed <b>exemption</b> "
    "under 76-4-125. The exemption route has a formality worth knowing, "
    "because it is how you verify one from the public record: a person "
    "claiming an exemption must place an acknowledged certification on the "
    "plat or certificate of survey, and \"<i>The certification <b>must quote "
    "in its entirety the wording of the applicable exemption</b></i>\" "
    "(76-4-122(2)(c); the same requirement appears at 76-4-125(3)). A "
    "county clerk and recorder may not accept the filing otherwise "
    "(76-4-122(2))."))
flow.append(k.callout("How to check a parcel — before you close, not after", [
    Paragraph("Pull the <b>certificate of survey or plat</b> for the parcel at "
              "the county clerk and recorder and read what is printed on its "
              "face. You are looking for one of: a certificate of subdivision "
              "approval, a 76-4-127 certification, or an exemption "
              "certification <b>with the exemption quoted in full</b>. If you "
              "find none of those, or you find the words <b>\"sanitary "
              "restriction\"</b> without a later release, treat the parcel as "
              "not yet buildable and take the question to DEQ and the county "
              "before you sign anything. Ask the seller for the certificate of "
              "subdivision approval by name — a seller who has one produces it "
              "immediately, and a seller who cannot is telling you something.",
              S["body"]),
]))
flow.append(Spacer(1, 6))

flow.append(Paragraph("The exemption that becomes the problem", S["h3"]))
flow.append(k.body(
    "Here is the mechanism, because it catches people who did everything "
    "right. \"Subdivision\" is defined broadly — a division creating one or "
    "more parcels of <b>less than 20 acres</b> for sale, rent, or lease "
    "(76-4-102(25)) — so an ordinary sub-20-acre rural lot is inside the Act. "
    "Many such lots were legally created and legally sold using a <b>\"no "
    "facilities\" exclusion</b>: the reviewing authority may exclude \"<i>a "
    "parcel that has no facilities for water supply, wastewater disposal, "
    "storm drainage, or solid waste disposal, <b>if no facilities will be "
    "constructed on the parcel</b></i>\" (ARM 17.36.605(2)(a)). DEQ's own "
    "explanation of what that means later is worth reading twice: such "
    "exclusions \"<i>are listed on the front of the survey</i>,\" and \"<i>In "
    "either case, a <b>COSA must be issued for the lot(s) prior to developing "
    "facilities that require sewer or water</b></i>.\""))
flow.append(k.callout_long("The trap, stated plainly", [
    Paragraph("<b>The lot was exempted from sanitation review precisely "
              "because nobody was going to build on it.</b> Building a house "
              "is the event the exemption assumed would never happen. So the "
              "exemption printed on your certificate of survey — the thing "
              "that made the parcel cheap and easy to sell — is the same "
              "thing that means you must now go through DEQ subdivision "
              "review and obtain a certificate of subdivision approval before "
              "you may put in a well or a septic system, and before you may "
              "erect or occupy the house (76-4-121).", S["body"]),
    Paragraph("Two more things people get wrong here. <b>The COSA is not the "
              "septic permit.</b> DEQ answers this directly: \"<i>Do I need a "
              "permit to install a drainfield now that I have a COSA? — Yes, "
              "even th[ough] you have a COSA, a drainfield permit is still "
              "required by the local health department.</i>\" Two approvals, "
              "two offices, in that order. And <b>the county does not issue "
              "the COSA</b>: a certified local reviewing authority reviews and "
              "\"<i>make[s] a recommendation for approval to the "
              "department</i>,\" and then \"<i>the department shall issue a "
              "certificate of subdivision approval</i>\" (76-4-114(3)(c)). "
              "DEQ signs it, whoever reviewed it.", S["body"]),
    Paragraph("<b>And the COSA constrains the site, not just the paperwork.</b> "
              "It comes with an <b>approved lot layout</b>, and the well has "
              "to go where that layout puts it — you do not get to move it "
              "later because the driller preferred a different spot. Adding a "
              "second dwelling to the parcel means going back for a rewritten "
              "certificate. Ask the county for the COSA <i>and</i> the "
              "approved lot layout together; the layout is the document your "
              "site plan has to match.", S["body"]),
    Paragraph("<b>There is no clean statewide lookup for this.</b> DEQ says "
              "it \"<i>tries to have digital copies</i>\" but that \"<i>local "
              "county environmental health departments are the best resource "
              "for obtaining these documents</i>,\" and that if your lot was "
              "created after 1961 and is under 20 acres it will \"<i>either "
              "have a COSA or … have sanitary restrictions placed on it</i>.\" "
              "So do both: read the recorded document, then ask the county.",
              S["body"]),
]))
flow.append(Spacer(1, 6))
flow += k.check_table("L1: Sanitation status of the parcel", [
    ("Certificate of survey or plat pulled from the county clerk and recorder "
     "and read", [("Document / book and page:", 1.0)]),
    ("Which of the three applies: certificate of subdivision approval / "
     "76-4-127 municipal or county service certification / 76-4-125 exemption "
     "quoted in full on the face of the document",
     [("Which:", 0.6), ("Cited exemption:", 0.4)]),
    "Checked specifically for the words \"sanitary restriction\" and, if "
    "present, for the document releasing it",
    ("If none of the three: DEQ subdivision program and the county contacted, "
     "and the review path and timeline confirmed in writing before any "
     "purchase or construction commitment",
     [("Spoke with:", 0.55), ("Date:", 0.45)]),
], notes_header="Notes / who confirmed")
flow.append(k.cite(
    "76-4-121; 76-4-122(2), (2)(a), (2)(c); 76-4-125(1), (2), (3); 76-4-127, "
    "MCA. Read August 2026. Whether a particular parcel is inside or outside "
    "the definition of a reviewable subdivision is a legal question about that "
    "parcel's history — this document tells you which record to read and which "
    "office to ask, not what your parcel's answer is."))

# ================================================================ WATER
flow += k.h2_tight("2. WATER — THE \"EXEMPT\" WELL IS NOT EXEMPT FROM "
                   "PAPERWORK")
flow.append(k.body(
    "Montana water law is prior-appropriation law, and a well is a water "
    "right, not a utility hookup. Small wells escape the full <b>permit</b> "
    "process — which is what \"exempt well\" means — but they do not escape "
    "<b>filing</b>, and the filing is reviewed and can be denied. Anyone who "
    "tells you a domestic well in Montana is paperwork-free has not read "
    "85-2-306(3)(b)."))

w_rows = [
    [k.cellp("<b>Outside a stream<br/>depletion zone</b>"),
     k.cellp("No permit needed where the appropriation \"<i>is <b>35 gallons a "
             "minute or less</b>, and does not exceed <b>10 acre-feet a "
             "year</b></i>\" — \"<i>except that a <b>combined appropriation "
             "from the same source by two or more wells or developed springs "
             "exceeding 10 acre-feet, regardless of the flow rate, requires a "
             "permit</b></i>\" (85-2-306(3)(a)(iii)).")],
    [k.cellp("<b>Inside a stream<br/>depletion zone</b>"),
     k.cellp("Much tighter: \"<i>is <b>20 gallons a minute or less</b>, and "
             "does not exceed <b>2 acre-feet a year</b></i>,\" with the same "
             "combined-appropriation limit (85-2-306(3)(a)(iv)). In practice "
             "this is a narrow case — as of this printing only <b>one</b> "
             "stream depletion zone has been designated in Montana, on Rye "
             "Creek in Ravalli County. Confirm with DNRC rather than assuming "
             "either way, since designations can be added.")],
    [k.cellp("<b>Inside a controlled<br/>ground water area</b>"),
     k.cellp("The exemption does not apply at all. Ground water may be "
             "appropriated \"<i>only … according to a permit received pursuant "
             "to 85-2-508</i>\" or according to a rule adopted under 85-2-506 "
             "(85-2-306(2)). This is the answer that can make a parcel "
             "unbuildable — ask DNRC by legal description.")],
]
flow.append(k.ref_table(
    "Which exempt-well limit applies to your parcel",
    [k.cellp("Where the parcel is", bold=True),
     k.cellp("What the statute allows", bold=True)],
    w_rows, [1.5 * inch, CW - 1.5 * inch]))
flow.append(Spacer(1, 6))

flow.append(k.callout_long("Two filings, in this order — and the second one "
                           "sets your priority date", [
    Paragraph("<b>Before you drill — and this is new.</b> \"<i>Before "
              "appropriating groundwater … a person <b>shall file with the "
              "department</b> … a correct and complete <b>notice of intent to "
              "appropriate groundwater</b></i>\" (85-2-306(3)(b)(i)). This "
              "pre-drilling filing was created by <b>House Bill 681 of the "
              "2025 session and took effect January 1, 2026</b>; DNRC "
              "implements it on <b>Form 602I</b>, which carries a <b>$400 "
              "filing fee</b>. The department notifies you of defects within "
              "10 business days; an uncorrected notice terminates after 60 "
              "days; and within 10 business days of a correct and complete "
              "notice the department \"<i>shall review the notice for "
              "compliance … and shall <b>authorize or deny</b> the "
              "notice</i>.\" Authorization is good for <b>5 years</b>, "
              "extendable once.", S["body"]),
    Paragraph("<b>The sting, if you skipped it.</b> DNRC states that it can "
              "<b>no longer process a Notice of Completion without an "
              "authorized Notice of Intent on file</b>. So a well drilled "
              "without the front-end filing cannot be perfected at the back "
              "end — you do not get the certificate of water right, and the "
              "priority date you were counting on never attaches. If you were "
              "told at any point that a Montana domestic well is simply "
              "'drill, then file within 60 days,' that advice is from before "
              "2026.", S["body"]),
    Paragraph("<b>After you drill.</b> \"<i>Within <b>60 days</b> of "
              "completion of the well … and appropriation of the ground water "
              "for beneficial use, the appropriator shall file a <b>notice of "
              "completion</b></i>\" (85-2-306(3)(c)(i)), and it must establish "
              "that the work was done \"<i>in substantial accordance with the "
              "notice of intent … authorized by the department</i>.\" Miss the "
              "cure period and \"<i>the department authorization expires and a "
              "new notice of intent … is required</i>.\"", S["body"]),
    Paragraph("<b>Why the deadline matters more than it looks.</b> \"<i>A "
              "certificate of water right may not be issued until a correct "
              "and complete notice has been filed</i>,\" and \"<i>The <b>date "
              "of filing of the notice of completion is the date of priority "
              "of the right</b></i>\" (85-2-306(3)(d)). In a "
              "first-in-time-first-in-right state, sitting on that form is not "
              "an administrative slip — it is your seniority against every "
              "neighbor who files before you.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow.append(Paragraph("\"Combined appropriation\" — what it means now",
                      S["h3"]))
flow.append(k.body(
    "The phrase in the statute does a great deal of work, and its meaning "
    "moved recently. The definition in force is <b>ARM 36.12.101(14)</b>, "
    "current version effective <b>October 1, 2025</b>: \"<i>an appropriation "
    "of water from the <b>same source aquifer</b> by two or more groundwater "
    "developments, the purpose of which, in the department's judgment, "
    "<b>could have been accomplished by a single appropriation</b>. "
    "Groundwater developments <b>need not be physically connected</b> nor have "
    "a common distribution system … They can be developed gradually or in "
    "increments.</i>\" Note what that is not: <b>not a distance test</b>, and "
    "<b>not something you escape by phasing</b>. (The subsection was "
    "renumbered in the 2025 amendment; older sources cite 36.12.101(12).)"))
flow.append(k.callout_long("Why this changed — and what it means for one "
                           "house on one lot", [
    Paragraph("On <b>February 14, 2024</b>, Montana's First Judicial District "
              "Court decided <i>Upper Missouri Waterkeeper v. DNRC</i>, "
              "holding, in DEQ's summary, that DNRC \"<i>incorrectly applied "
              "the law when it determined that a developer was entitled to "
              "appropriate up to 10 acre-feet of water for each phase of a "
              "four-phased subdivision</i>\" and that DNRC \"<i>is required to "
              "treat all phases of a multi-phased development as part of the "
              "same combined appropriation</i>.\" DNRC rescinded its combined "
              "appropriation guidance and <b>stopped issuing predetermination "
              "letters</b>.", S["body"]),
    Paragraph("<b>The practical read.</b> One house, one well, one lot, "
              "outside a controlled ground water area and outside a stream "
              "depletion zone, at 35 gpm or less and 10 acre-feet or less: "
              "the exception applies on its face and you are almost certainly "
              "fine. <b>The risk is not your well — it is your neighbors'.</b> "
              "If your lot sits in a subdivision whose other lots draw from "
              "the same source aquifer, DNRC now counts all of them together "
              "against a single 10 acre-foot ceiling for the whole "
              "development. Ask DNRC, by legal description, what has already "
              "been claimed there before you buy.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow += k.check_table("L2: Water supply", [
    ("Water source determined: exempt well / permitted well / municipal or "
     "district service / cistern with hauled water", [("Source:", 1.0)]),
    ("DNRC asked, by legal description, whether the parcel is inside a "
     "controlled ground water area or a stream depletion zone — the answer "
     "changes the limits and can remove the exemption entirely",
     [("Answer:", 0.6), ("Date:", 0.4)]),
    ("Notice of intent to appropriate groundwater filed AND authorized before "
     "any drilling (85-2-306(3)(b))",
     [("Filed:", 0.5), ("Authorized:", 0.5)]),
    "Checked whether other wells draw from the same source on the same "
    "development — a combined appropriation over the limit needs a permit "
    "regardless of flow rate",
    ("Notice of completion filed within 60 days of putting water to beneficial "
     "use — this date is your priority date (85-2-306(3)(c)(i), (3)(d))",
     [("Completed:", 0.5), ("Notice filed:", 0.5)]),
    ("If municipal or district service instead: written will-serve and the "
     "connection fee in writing", [("Provider:", 1.0)]),
    "If you intend to drill the well YOURSELF: exemption permit obtained from "
    "the Board of Water Well Contractors BEFORE any drilling — see the note "
    "below",
], notes_header="Notes / who confirmed")
flow.append(k.callout("Drilling your own well — one permit, obtained first", [
    Paragraph("Montana licenses water well contractors, and the homeowner "
              "carve-out is not automatic. Under <b>37-43-302(2)</b> you may "
              "construct a well on your own land — used as your residence, "
              "farm, or ranch, with the work <b>personally performed</b> — "
              "only if you hold an <b>exemption permit from the Board of "
              "Water Well Contractors</b>, and the Board's application "
              "carries a <b>$100 fee</b>. The order matters: the permit is "
              "something you obtain <b>before</b> the drilling, not a form "
              "you file afterwards. And it stacks on the water-right filings "
              "above rather than replacing them — the exemption permit lets "
              "you do the drilling; the Form 602I notice of intent lets you "
              "appropriate the water.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow.append(k.cite(
    "85-2-306(1), (2), (3)(a)(iii), (3)(a)(iv), (3)(b), (3)(c), (3)(d), MCA, "
    "as published in the Montana Code Annotated at mca.legmt.gov, read August "
    "2026. This section has been amended many times; check its History line "
    "for changes since this printing. Note also 85-2-306(1): you generally "
    "need a possessory interest in the property where the water will be used "
    "and exclusive rights in the well works, and a person without a possessory "
    "interest must give the landowner at least 30 days' written notice."))

# ================================================================ SEPTIC
flow += k.h2_tight("3. SEPTIC — A COUNTY PERMIT UNDER A STATE FRAME")
flow.append(k.body(
    "Sanitation approval on the parcel (step 1) and the permit to install an "
    "actual system are two different things, and people conflate them. The "
    "installation permit is your <b>county's</b>, issued by the local health "
    "department or sanitarian under the county's own regulations. The statute "
    "assumes that office exists and gives it real authority — a filing under "
    "the sanitation part requires \"<i>approval of the local health officer "
    "having jurisdiction</i>\" (76-4-122(2)(a)), and a local health officer "
    "may require that a remainder parcel \"<i>include acreage or features "
    "sufficient to accommodate a <b>replacement drainfield</b></i>\" "
    "(76-4-125(2)) — a reminder that Montana expects you to have room for the "
    "system you will need in twenty years, not just the one you install now."))
flow.append(k.body(
    "The county's rules must be \"<i>no less stringent</i>\" than the state's "
    "(ARM 17.36.911(2); MCA 50-2-116(1)(j)), so a handful of numbers are the "
    "same everywhere and are worth designing around from the first site "
    "sketch — because they set how much usable land you actually have."))
sep_rows = [
    [k.cellp("<b>Well to drainfield</b>"),
     k.cellp("<b>100 feet.</b> ARM 17.36.323, Table 2 — from a drinking water "
             "well to a drainfield or soil absorption system, and the same "
             "100 feet from a mixing zone to a drinking water well. "
             "<b>50 feet</b> from the well to sealed components. A sewage "
             "lagoon is <b>1,000 feet</b>. A smaller well isolation zone is "
             "possible only if the department approves one.")],
    [k.cellp("<b>Property boundaries</b>"),
     k.cellp("<b>10 feet</b>, though an easement may satisfy it "
             "(ARM 17.36.323, Table 2). Surface water and springs to a "
             "drainfield: <b>100 feet</b>.")],
    [k.cellp("<b>Depth to a limiting layer</b>"),
     k.cellp("\"<i>For subsurface systems, a minimum separation of at least "
             "<b>four feet</b> of natural soil must exist between the "
             "infiltrative surface … and a limiting layer</i>\" "
             "(ARM 17.36.320(4)) — <b>six feet</b> on slopes over 15 percent. "
             "This is the number that quietly decides whether a lot works.")],
    [k.cellp("<b>The site work</b>"),
     k.cellp("The reviewing authority may require percolation tests per DEQ "
             "Circular DEQ-4 within each proposed system boundary; the "
             "applicant provides soil descriptions within 25 feet of each "
             "proposed drainfield boundary, and \"<i>At least one test hole "
             "must be dug for each individual drainfield</i>\" "
             "(ARM 17.36.325). Groundwater monitoring is required if water "
             "may come within seven feet of the surface at any time of year.")],
    [k.cellp("<b>The well isolation zone<br/>must fit on your land</b>"),
     k.cellp("A \"well isolation zone\" is the area within a <b>100-foot "
             "radius</b> of the well (76-4-102(27)), and for parcels created "
             "after October 1, 2021 both it and the drainfield mixing zone "
             "must lie inside the subdivision boundary or be secured by "
             "easement (76-4-104(7)(i)). On a small lot this, not the house, "
             "is the binding constraint.")],
]
flow.append(k.ref_table(
    "State minimums your county cannot go below",
    [k.cellp("What", bold=True), k.cellp("The rule", bold=True)],
    sep_rows, [1.5 * inch, CW - 1.5 * inch]))
flow.append(Spacer(1, 6))
flow.append(k.body(
    "Beyond those, the detail is county-level, so this kit gives you the "
    "questions rather than an answer that would be wrong in most counties. "
    "Ask your county environmental health office, in one call: what the site "
    "evaluation "
    "requires and who may perform it; whether soil pits or percolation testing "
    "are required and when in the year they can be done; the setbacks from the "
    "well, the property lines, surface water, and any cut bank; the minimum "
    "depth to groundwater or bedrock; whether a homeowner may install their "
    "own system or a licensed installer is required; and which inspection must "
    "happen <b>before the system is covered</b>. Get the answers in writing "
    "and file them here."))
flow += k.check_table("L3: Wastewater", [
    ("County environmental health / sanitarian office identified and the "
     "current regulations obtained", [("Office:", 1.0)]),
    ("Site evaluation and soil work completed by whoever the county accepts — "
     "and scheduled for a season when the ground can actually be read",
     [("By:", 0.6), ("Date:", 0.4)]),
    "Asked whether a homeowner may install their own system here, or a "
    "licensed installer is required — this is a county answer, not a state one",
    ("Permit issued BEFORE any excavation for the system",
     [("Permit #:", 0.5), ("Date:", 0.5)]),
    "Room for a replacement drainfield identified and kept clear of driveway, "
    "building, and utility routes (76-4-125(2))",
    "Inspection before cover scheduled, and the final approval obtained and "
    "filed with this kit",
], notes_header="Notes")

# ================================================================ ACCESS
flow += k.h2_tight("4. ACCESS AND ADDRESS — SMALL APPROVALS THAT BLOCK BIG "
                   "ONES")
flow.append(k.body(
    "Two approvals that cost little and are expensive to discover late, "
    "because other applications ask for their output. An <b>assigned 911 "
    "address</b> is what a permit application, a power supplier, and the "
    "emergency-services database all key on — and on raw rural land it does "
    "not exist until somebody assigns it. A <b>road approach permit</b> comes "
    "from whoever owns the road: the county road department, the "
    "municipality, or the Montana Department of Transportation where a "
    "driveway meets a state highway. Ask early which one owns your frontage; "
    "on a rural parcel that is genuinely not obvious from a map."))
flow.append(k.callout("Floodplain — a separate permit, and two feet of "
                      "freeboard", [
    Paragraph("If any part of your site is in a designated floodplain or "
              "floodway this is not optional and not folded into anything "
              "else: \"<i>It is unlawful for a person to establish an "
              "artificial obstruction or nonconforming use within a designated "
              "flood plain or a designated floodway <b>without a permit</b> "
              "from the department or the responsible political "
              "subdivision</i>\" (76-5-404) — and a house counts, because "
              "\"artificial obstruction\" reaches buildings and fill "
              "(76-5-103). It is expressly \"<i>an added requirement</i>\" on "
              "top of every other approval (76-5-108). The design number is "
              "the part to catch early: outside the floodway, a residential "
              "structure's lowest floor <b>including the basement</b> must be "
              "at least <b>two feet above</b> the 100-year flood elevation "
              "(76-5-402). Montana is a two-foot-freeboard state — stricter "
              "than the federal baseline, and it changes your foundation "
              "design, not just your paperwork. Local governments administer "
              "these permits; DNRC oversees the program and publishes the "
              "administrator list.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow += k.check_table("L4: Access, address, and the rest of the land", [
    ("911 address assigned by the county addressing authority",
     [("Address:", 1.0)]),
    ("Road approach / driveway permit obtained from the road authority — "
     "county, city, or MDT for a state highway",
     [("Authority:", 0.55), ("Permit #:", 0.45)]),
    "Floodplain status checked with the county floodplain administrator and a "
    "development permit obtained if any part of the site is in a mapped hazard "
    "area — this applies whether or not a building permit does",
    "Zoning and setbacks confirmed in writing — many Montana counties have no "
    "zoning at all, some have districts, and \"no zoning\" is still an answer "
    "worth having in writing",
    "Easements, covenants, and any HOA architectural review identified — "
    "private restrictions bind you where no public code does — and the fire "
    "district asked directly about access width, turnaround, and water supply",
], notes_header="Notes")

# ================================================================ PERMITS
flow += k.h2_tight("5. THE PERMITS — WHICH ONES EXIST FOR YOUR HOUSE")
flow.append(k.body(
    "Now, and only now, the permits. Which of these you owe was settled in "
    "MT.1 and MT.4; this table is the summary you work from. The middle column "
    "is the ordinary rural case — a house of fewer than five dwelling units "
    "outside every certified program."))

p_rows = [
    [k.cellp("<b>Building</b>"),
     k.cellp("<b>None.</b> The state building code does not apply and the "
             "state may not enforce it (50-60-102(1)(a), (2))."),
     k.cellp("Local building permit, plan review, and inspections.")],
    [k.cellp("<b>Electrical</b>"),
     k.cellp("<b>Required — from the state.</b> The department: \"<i>State "
             "electrical permits are required on <b>all</b> electrical work "
             "performed in Montana, except in cities, counties and towns "
             "certified</i>.\" A <b>Homeowner Electrical Permit</b> form is "
             "published for owners doing their own work."),
     k.cellp("Local, but <b>only if the jurisdiction's listing shows E</b> — "
             "most show building only (MT.4).")],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp("<b>None if you personally do the work</b> as owner of the "
             "residential property (50-60-506(4)). If someone else does it, a "
             "state plumbing permit."),
     k.cellp("Local where the local code covers plumbing with inspection "
             "procedures, which removes the state permit (50-60-506(3)).")],
    [k.cellp("<b>Mechanical</b><br/>(includes gas piping)"),
     k.cellp("<b>None.</b> The rules say it outright: \"<i>The department "
             "shall not enforce the IMC in buildings exempted from state "
             "building codes by 50-60-102, MCA</i>\" (ARM 24.301.172(2)), and "
             "the fuel gas rule carries the same sentence "
             "(ARM 24.301.173(2)). Your house is such a building."),
     k.cellp("Local where the listing shows M.")],
    [k.cellp("<b>Energy</b>"),
     k.cellp("<b>You certify it, in writing, at the end</b> "
             "(50-60-102(5)(b)(ii); 50-60-802(1)). Not a permit — a duty."),
     k.cellp("Verified through the local program.")],
]
flow.append(k.ref_table(
    "What you owe, by discipline",
    [k.cellp("Discipline", bold=True),
     k.cellp("Outside every certified program", bold=True),
     k.cellp("Inside one", bold=True)],
    p_rows, [1.15 * inch, (CW - 1.15 * inch) * 0.56,
             (CW - 1.15 * inch) * 0.44]))
flow.append(Spacer(1, 6))
flow.append(k.callout_long("Codes you are building to, even where nobody "
                           "checks", [
    Paragraph("Montana adopted its current family of codes <b>effective June "
              "11, 2022</b>: the <b>2021 IRC</b>, 2021 IBC, <b>2021 Uniform "
              "Plumbing Code</b> (Montana uses the UPC, not the IPC — the "
              "fixture table is at ARM 24.301.351, and the department "
              "publishes a legible copy because the rule itself is hard to "
              "read), 2021 IMC, 2021 IFGC, <b>2021 IECC</b>, and the "
              "<b>2020 National Electrical Code</b>. All of them are amended "
              "by ARM Title 24, chapter 301, and several of those adopting "
              "rules were themselves amended effective September 2024 — so "
              "read the rule, not just the model code.", S["body"]),
    Paragraph("<b>Four Montana amendments that change what you build.</b> "
              "<b>(1) Snow load:</b> the IRC's snow provisions are rewritten "
              "to ASCE 7-22 with a <b>30 psf minimum</b> outside certified "
              "jurisdictions — a floor, not a design value; see the next "
              "page. <b>(2) Frost depth:</b> outside certified jurisdictions, "
              "<b>three feet</b> for a single-story frame house and <b>four "
              "feet</b> for multistory or masonry (ARM 24.301.142(9)). "
              "<b>(3) Air leakage:</b> Montana replaced IECC R402.4.1.2 with a "
              "blower-door limit of <b>four air changes per hour</b> at 50 "
              "pascals in Climate Zone 6 — <i>not</i> the national three — and "
              "requires \"<i>a written report of the results of the test … "
              "signed by the party conducting the test</i>\" "
              "(ARM 24.301.161(1)(k)). <b>(4) Sprinklers:</b> IRC R313 is "
              "deleted in its entirety, matching the statutory bar at "
              "50-60-203(5)(a).", S["body"]),
    Paragraph("<b>And Montana amends the NEC downward in two places</b>, "
              "which matters if you are wiring from national material: ARM "
              "24.301.401 adopts the <b>2020</b> edition, then amends "
              "210.8(A) and (B) to <b>remove 250-volt receptacles</b> from "
              "the GFCI requirement and amends 210.12 to <b>delete every "
              "reference to kitchens</b> from AFCI. In both spots Montana is "
              "<i>less</i> stringent than the model code. <b>Check the date "
              "before relying on any of this:</b> a code-adoption rulemaking "
              "was under way as this edition went to print, with a hearing "
              "noticed for August 2026, so the 2020 NEC and the 2021 I-codes "
              "may be replaced within months. Confirm at bsd.dli.mt.gov "
              "before you design.", S["body"]),
]))
flow.append(Spacer(1, 6))
flow += k.check_table("P1: The permits and the certification", [
    ("Confirmed from the certified-jurisdiction list whether a local program "
     "covers this parcel, and for which disciplines (MT.4)",
     [("Program:", 0.5), ("Disciplines:", 0.5)]),
    ("Electrical permit obtained BEFORE the work — Homeowner Electrical Permit "
     "if you are doing it yourself. Fee for a single-family dwelling is set by "
     "rule: $200 up to a 200-amp service (ARM 24.301.461)",
     [("Permit #:", 0.5), ("Date:", 0.5)]),
    "Confirmed that YOU will perform all work under the permit — no person "
    "other than the permittee may do any of it (ARM 24.301.431(8))",
    "Grid-tied solar, wind, or standby generator work assigned to a licensed "
    "electrician — the homeowner exemption does not cover it "
    "(37-68-103(3)(b)); note the department publishes a separate "
    "alternative-energy permit form",
    "Plumbing decided: personally performed under 50-60-506(4), or permitted",
    ("Mechanical and gas piping status confirmed with the department for THIS "
     "building", [("Answer:", 1.0)]),
    ("Adopted energy code edition and effective date written down, and the "
     "written certification prepared for signature at completion "
     "(50-60-802(1))", [("Edition:", 0.5), ("Signed:", 0.5)]),
], notes_header="Notes")

# ================================================================ HAZARDS
flow += k.h2_tight("6. THE TWO THINGS NOBODY WILL CHECK FOR YOU")
flow.append(k.body(
    "Where no plan reviewer reads your drawings, two decisions have no "
    "backstop at all, and both are structural."))
flow.append(k.callout_long("Snow load, and the wildland-urban interface", [
    Paragraph("<b>Ground snow load — and check where your number came "
              "from.</b> Montana replaced the IRC's snow provisions outright: "
              "outside certified jurisdictions, ground snow loads are taken "
              "from <b>ASCE/SEI 7-22</b> through the <b>ASCE 7 Hazard "
              "Tool</b> (asce7hazardtool.online), with a <b>minimum design "
              "roof snow load of 30 psf</b> after allowed reductions unless a "
              "Montana-licensed design professional justifies less "
              "(ARM 24.301.154(5), current version effective September 2024).",
              S["body"]),
    Paragraph("<b>This tripped us up, so it will trip you up.</b> The "
              "department's own snow-load web page still points at a Montana "
              "State University study from 2004. <b>The rule governs, not the "
              "web page</b> — pull your site's value from the ASCE 7 Hazard "
              "Tool, and if an older guide, a truss supplier, or a neighbor "
              "quotes you a figure, ask which source it came from before you "
              "build a roof on it. Values change sharply over short horizontal "
              "distances, so a number for the valley floor is not a number for "
              "a bench a thousand feet higher. Treat the 30 psf as a "
              "<b>floor, not a target</b>. <b>Write your site's figure and its "
              "source into MT.3</b>, and design for drift and sliding loads "
              "where roof planes change, behind parapets, and against taller "
              "walls — that is where most snow failures actually happen.",
              S["body"]),
    Paragraph("<b>Wildfire.</b> Montana <i>has</i> adopted the <b>2021 "
              "Wildland Urban Interface Code</b> among its state codes, "
              "effective June 11, 2022 — but on the department's certified "
              "list only <b>four jurisdictions</b> (Bozeman, Columbia Falls, "
              "Great Falls, and Whitefish) are certified to enforce it, and "
              "the residential exemption keeps it away from most houses. So if "
              "you are building in the trees anywhere else, ignition-resistant "
              "construction and defensible space are <b>your</b> decision and "
              "nobody else's: a Class A roof kept clear of needles, "
              "ember-resistant vents and enclosed eaves, ignition-resistant "
              "siding and decking, and managed vegetation around the "
              "structure. Your insurer will care about this long before any "
              "inspector does.", S["body"]),
]))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 10))
flow.append(k.sources_table([
    ("You may not erect a building requiring water or sewage facilities, or "
     "occupy a permanent building, until sanitation approval, a municipal "
     "service certification, or an exemption applies", "76-4-121, MCA"),
    ("An exemption certification must quote the applicable exemption in its "
     "entirety, and the clerk and recorder may not accept a filing otherwise",
     "76-4-122(2); 76-4-125(3), MCA"),
    ("Local health officer approval, and replacement-drainfield capacity",
     "76-4-122(2)(a); 76-4-125(2), MCA"),
    ("Exempt well outside a stream depletion zone: 35 gpm and 10 acre-feet; "
     "combined appropriation over the limit needs a permit",
     "85-2-306(3)(a)(iii), MCA"),
    ("Inside a stream depletion zone: 20 gpm and 2 acre-feet",
     "85-2-306(3)(a)(iv), MCA"),
    ("Inside a controlled ground water area, only by permit",
     "85-2-306(2), MCA"),
    ("Notice of intent filed and authorized before appropriating; 5 years to "
     "complete", "85-2-306(3)(b), MCA"),
    ("Notice of completion within 60 days; the filing date is the priority "
     "date of the right", "85-2-306(3)(c)(i), (3)(d), MCA"),
    ("The state building code does not apply to residential buildings of fewer "
     "than five dwelling units; the energy provisions apply anyway",
     "50-60-102(1)(a), (2), (5), MCA"),
    ("State electrical permits required on all electrical work except in "
     "certified jurisdictions; mechanical permits tied to buildings to which "
     "state building permits apply",
     "DLI Building Codes Program<br/>permit pages, bsd.dli.mt.gov"),
    ("2021 IRC, 2021 UPC, 2021 IECC, 2020 NEC and the rest, effective June 11, "
     "2022, all amended by ARM Title 24, chapter 301",
     "DLI Current Codes, bsd.dli.mt.gov"),
    ("A sub-20-acre parcel is a \"subdivision\"; a \"no facilities\" exclusion "
     "assumes nothing will be built, so a COSA is needed before developing "
     "water or sewer", "76-4-102(25), MCA;<br/>ARM 17.36.605(2)(a); DEQ"),
    ("The COSA is issued by DEQ on a local reviewing authority's "
     "recommendation, and is separate from the county septic permit",
     "76-4-114(3)(c), MCA; DEQ"),
    ("Well to drainfield 100 feet; four feet of natural soil above a limiting "
     "layer; well isolation zone must lie within the boundary",
     "ARM 17.36.323 Table 2;<br/>ARM 17.36.320(4);<br/>76-4-104(7)(i), MCA"),
    ("Pre-drilling Notice of Intent (Form 602I, $400) created by HB 681, "
     "effective January 1, 2026; no Notice of Completion may be processed "
     "without an authorized one", "85-2-306(3)(b), MCA;<br/>DNRC"),
    ("\"Combined appropriation\" means the same source aquifer, not a "
     "distance test, and phases count together after the February 2024 "
     "decision", "ARM 36.12.101(14), eff.<br/>10/1/2025; DEQ"),
    ("A homeowner drilling their own well needs a Board of Water Well "
     "Contractors exemption permit ($100) first", "37-43-302(2), MCA"),
    ("Floodplain permit required; lowest floor including basement two feet "
     "above the 100-year flood elevation",
     "76-5-404; 76-5-402;<br/>76-5-108, MCA"),
    ("No state mechanical or fuel gas enforcement in buildings exempted by "
     "50-60-102", "ARM 24.301.172(2);<br/>ARM 24.301.173(2)"),
    ("Snow load to ASCE 7-22 via the ASCE 7 Hazard Tool, 30 psf minimum; "
     "frost depth 3 ft frame / 4 ft multistory",
     "ARM 24.301.154(5);<br/>ARM 24.301.142(9)"),
    ("Blower door 4 ACH50 in Climate Zone 6 with a signed report; Montana "
     "amends the 2020 NEC downward at 210.8 and 210.12",
     "ARM 24.301.161(1)(k);<br/>ARM 24.301.401"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "mt-permit-kit",
                       "MT.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
