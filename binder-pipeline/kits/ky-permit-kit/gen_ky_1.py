#!/usr/bin/env python3
"""KY.1 Owner-Builder Exemption Walkthrough.

Every Kentucky claim in this document was read out of the primary source in
August 2026 and is cited on-page. Where the statute is silent or the answer
depends on a local ordinance, the document says so and gives the verification
step.

Verified sources:
  KRS 198B.010(4)      "building" expressly "also means single-family
                       dwellings" — the CODE reaches your house
  KRS 198B.050(1),(2)  a MANDATORY Uniform State Building Code; it encompasses
                       the Kentucky State Plumbing Code (KRS 318.130) and the
                       national electrical code
  KRS 198B.060(1)      permits, inspections and certificates of occupancy
                       "shall not be mandatory for single-family residences
                       unless a local government passes an ordinance"
  KRS 198B.060(4)(b)   the department "shall not preempt or assert jurisdiction
                       for the enforcement of the code on single-family
                       dwellings" — NO STATE BACKSTOP
  KRS 198B.060(8),(13) nothing requires a single-family dwelling to be permitted
                       or inspected, or a CO to issue, absent a local program
  KRS 198B.060(10)     the workers' compensation / unemployment insurance
                       affidavit, and its $4,000-or-more penalty
  KRS 198B.060(11)     no utility may initiate PERMANENT ELECTRIC service until
                       a certified electrical inspector issues a final
                       certificate of approval
  KRS 198B.130         private action; 1 year from discovery, 10 years outside;
                       attorney's fees added IF NO CO WAS ISSUED
  KRS 227A.030(3)      homeowner/farmer ELECTRICAL exemption — note there is NO
                       occupancy, no single-family and no personally-performed
                       condition in the text; do not add one
  KRS 318.015(1),(3)   chapter 318 is in force in ALL counties; does not apply
                       to farmsteads
  KRS 318.134(1),(2)   the state PLUMBING installation permit, and the septic
                       permit that must accompany the application
  KRS 318.165          no permanent WATER supply until the plumbing is approved
  KRS 318.030(1)       flat licensing rule — there is NO homeowner exemption in
                       the plumbing statute; the right is regulatory only
  815 KAR 20:050 §2(1)(b)  the homeowner plumbing permit and its five conditions
  KRS 198B.6671(1),(6) the state HVAC permit for an initial system
  KRS 198B.674(3)      HVAC homeowner exemption — "owned AND occupied"
  815 KAR 8:070 §2(2),(3)  homeowner HVAC permit conditions and the 5-year rule
  KRS 198B.6673(4)     local HVAC programs frozen at their 1 Jan 2007 footprint
  815 KAR 7:125 §2     the 2015 IRC + 2018 Kentucky Residential Code, and
                       §2(2)(a) repeating the permit exemption in the code reg

Deliberately NOT claimed: that Kentucky imposes a holding period, a
not-for-sale window, an owner-present-at-inspection rule, or a project-cost
threshold on an owner-builder. None appears in KRS 198B, 227A or 318.
Deliberately NOT claimed: that a homeowner plumbing plan submission is required
for a new single-family house. 815 KAR 20:050 §3(1) read alone would sweep one
in, but its enabling statute KRS 318.160 reaches "any public building or
establishment." The document prints a write-in line instead of guessing.
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

FORM_ID = "KY.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "Exemption & Qualification"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What Kentucky actually lets you do yourself — and the one question about "
    "your own county that changes the shape of the entire build.")

flow.append(k.disclaimer(
    "Statute and regulation text was read at apps.legislature.ky.gov in "
    "August 2026; both change."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION")
flow.append(k.body(
    "<b>There is no Kentucky state license for a general contractor or home "
    "builder.</b> The Commonwealth licenses <i>trades</i> — electricians and "
    "electrical contractors, master and journeyman plumbers, master and "
    "journeyman HVAC contractors and mechanics, plus elevator, boiler, fire "
    "sprinkler and manufactured-housing work. It does not license the person "
    "who builds the house. So \"owner-builder\" in Kentucky is not an "
    "exemption you claim; it is simply a thing you are allowed to be."))
flow.append(k.body(
    "Which means the interesting question in Kentucky is not <i>may I build "
    "it</i>. It is <b>who, if anyone, is going to inspect it</b> — and there "
    "the Commonwealth does something no other state does quite so plainly."))

rows = [
    [k.cellp("Do you need a state license to build your own house?"),
     k.cellp("<b>No</b> — and not to build someone else's either. Kentucky "
             "has no residential general contractor or home builder license "
             "at the state level. Your city or county may still require a "
             "local business or contractor registration; ask")],
    [k.cellp("Is there a project-cost threshold?"),
     k.cellp("<b>No.</b> Nothing in the building chapter is keyed to project "
             "value")],
    [k.cellp("Must you own the land? Must you live in it?"),
     k.cellp("For the <b>building</b> side, neither is a licensing condition "
             "— there is no license. But <b>each trade exemption sets its own "
             "test</b>, and they are not the same test. See the trade section "
             "below")],
    [k.cellp("How long must you keep it?"),
     k.cellp("<b>The statutes set no period.</b> No holding period, no "
             "not-for-sale window, no waiting period anywhere in KRS 198B, "
             "227A or 318")],
    [k.cellp("Do you need a building permit?"),
     k.cellp("<b>Only if your city or county passed an ordinance requiring "
             "one.</b> This is the sentence the rest of this kit turns on — "
             "read the next section before anything else")],
    [k.cellp("Does the building code apply to you either way?"),
     k.cellp("<b>Yes. Always.</b> The code is mandatory statewide and reaches "
             "single-family dwellings by definition. Only the enforcement is "
             "optional")],
]
flow.append(k.ref_table(
    "The Kentucky position at a glance",
    [k.cellp("Question", bold=True), k.cellp("Kentucky's answer", bold=True)],
    rows, [2.55 * inch, CW - 2.55 * inch]))
flow.append(k.cite(
    "Trade licensing: KRS Chapter 227A (electrical), KRS Chapter 318 "
    "(plumbing), KRS 198B.650 to 198B.689 (HVAC). The absence of a residential "
    "builder license is a negative — it was checked by reading the licensing "
    "provisions of KRS Chapter 198B in full in August 2026, and none creates "
    "one. Local registration is a separate question and is genuinely local."))

# ---------------------------------------------------------------- the big one
flow += k.h2_tight("THE SENTENCE THAT DECIDES YOUR BUILD")
flow.append(k.body(
    "Kentucky adopts <b>one mandatory residential code for the whole "
    "Commonwealth</b>, and the code itself forbids anything else: \"<i>Local "
    "governments shall not adopt or enforce any other building code for "
    "detached single family dwellings, two-family dwellings and "
    "townhouses.</i>\" There is no local code, no county writing its own "
    "rules, no shopping for a weaker jurisdiction. And the code plainly "
    "reaches your house: the statutory definition of \"building\" says so in "
    "as many words — it \"<i>also means <b>single-family dwellings</b></i>.\""))
flow.append(k.body(
    "Then the same chapter takes the enforcement away again."))

flow.append(k.callout_long("Read this twice — it is the whole kit", [
    Paragraph("<b>The statute.</b> Each local government shall employ a "
              "building official and enforce the Uniform State Building Code "
              "in its jurisdiction, \"<i><b>except that permits, inspections, "
              "and certificates of occupancy shall not be mandatory for "
              "single-family residences unless a local government passes an "
              "ordinance requiring inspections of single-family "
              "residences.</b></i>\" (KRS 198B.060(1))", S["body"]),
    Paragraph("<b>The code regulation says it again.</b> The very regulation "
              "that adopts the Kentucky Residential Code repeats it as an "
              "exception on the face of the code: \"<i><b>Permits, "
              "inspections, and certificates of occupancy shall not be "
              "required for a single-family dwelling unless required by local "
              "ordinance.</b></i>\" (815 KAR 7:125, Section 2(2)(a))",
              S["body"]),
    Paragraph("<b>And the State is forbidden to fill the gap.</b> This is the "
              "part that surprises people who have built elsewhere. Where a "
              "local program is failing, the department may normally step in "
              "and preempt it — \"<i>except that the department <b>shall not "
              "preempt or assert jurisdiction for the enforcement of the code "
              "on single-family dwellings</b></i>.\" There is no state "
              "backstop for houses. If your county has no ordinance, nobody "
              "inspects. (KRS 198B.060(4)(b))", S["body"]),
    Paragraph("Two more subsections close it off: nothing \"<i>shall require a "
              "single-family dwelling to be permitted or inspected unless a "
              "local government has established a building inspection "
              "program</i>\" (KRS 198B.060(8)), and nothing shall \"<i>require "
              "a certificate of occupancy to be issued for any single-family "
              "dwelling unless a local government has established "
              "jurisdiction</i>\" (KRS 198B.060(13)).", S["body"]),
]))
flow.append(Spacer(1, 8))
flow.append(k.cite(
    "KRS 198B.010(4), 198B.060(1), (4)(b), (8), (13); 815 KAR 7:125 Section "
    "2(2)(a). The bar on local codes is <b>Kentucky Residential Code section "
    "R101.3</b> — it lives in the code book, not in the statutes, which is why "
    "it is so often mis-cited. KRS 198B.060 was last amended by 2022 Ky. Acts "
    "ch. 66, sec. 2, effective July 14, 2022; 815 KAR 7:125 was last effective "
    "December 3, 2024. Read at apps.legislature.ky.gov, August 2026. "
    "<b>One limit on the exemption:</b> both the statute and the regulation "
    "say \"<i>single-family</i>\" — and 815 KAR 7:125 Section 1 defines "
    "two-family dwellings and townhouses as separate things. If you are "
    "building a duplex or a townhouse, do not assume the permit exemption "
    "reaches you; ask."))

flow.append(k.callout(
    "What \"no building permit\" does NOT mean", [
        Paragraph("It does not mean the code does not apply. The Kentucky "
                  "Residential Code is <b>mandatory</b> and it governs your "
                  "house whether or not anyone ever inspects it. What "
                  "disappears in a county with no ordinance is the "
                  "<i>inspection</i> — not the standard, not your liability, "
                  "and not the three permits in the next section.", S["body"]),
        Paragraph("And skipping the certificate of occupancy has a specific "
                  "price. Anyone damaged by a violation of the code has a "
                  "statutory cause of action against whoever committed it, for "
                  "up to <b>ten years</b> after first occupation or the "
                  "settlement date. The award \"<i>may include damages and the "
                  "cost of litigation</i>\" — and then: \"<i><b>If a "
                  "certificate of occupancy was not issued, then an award may "
                  "also include reasonable attorney's fees.</b></i>\" A future "
                  "buyer's lawyer knows this. Getting a CO you were not "
                  "required to get is the cheapest insurance in this kit. "
                  "(KRS 198B.130(1), (2))", S["body"]),
    ]))

# ---------------------------------------------------------------- always apply
flow += k.h2_tight("THE THREE THINGS THAT APPLY ANYWAY")
flow.append(k.body(
    "Whatever your county does about building permits, these three do not "
    "depend on it. They come from different chapters, they are administered "
    "by the Commonwealth rather than your county, and they are where "
    "Kentucky owner-builders actually get stopped."))

always = [
    [k.cellp("<b>1. State plumbing permit</b>"),
     k.cellp("\"<i>No person, firm, or corporation shall … construct, "
             "install, or alter … any plumbing <b>without first having "
             "procured a plumbing installation permit therefor from the "
             "department</b></i>.\" And the plumbing chapter is in force "
             "\"<i>in <b>all counties</b> of the Commonwealth</i>\" — with "
             "one carve-out: it \"<i>shall not apply to <b>farmsteads</b></i>.\" "
             "Your septic permit must accompany the application."),
     k.cellp("KRS 318.134(1)(a), (2); KRS 318.015(1), (3)")],
    [k.cellp("<b>2. State HVAC permit</b>"),
     k.cellp("\"<i>Any person who installs an <b>initial</b> heating, "
             "ventilation, or air conditioning system shall apply for a permit "
             "prior to beginning the installation. <b>No installation shall "
             "begin before the application for the permit has been "
             "filed.</b></i>\" Required in any building designed for human "
             "occupancy — which a house is."),
     k.cellp("KRS 198B.6671(1), (6)")],
    [k.cellp("<b>3. Electrical certificate of approval</b>"),
     k.cellp("Not a permit exactly — a gate. Once a certified electrical "
             "inspector has been provided for, \"<i><b>no utility shall "
             "initiate permanent electrical service to any new building</b> … "
             "until a final certificate of approval has been issued by a "
             "certified electrical inspector</i>.\" Temporary construction "
             "power is expressly not blocked."),
     k.cellp("KRS 198B.060(11)")],
]
flow.append(k.ref_table(
    "Required whether or not your county issues building permits",
    [k.cellp("What", bold=True), k.cellp("What the law says", bold=True),
     k.cellp("Authority", bold=True)],
    always, [1.55 * inch, CW - 1.55 * inch - 1.62 * inch, 1.62 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout("The two utilities are the real inspectors", [
    Paragraph("In a county with no building ordinance, the practical "
              "enforcement of the Kentucky Residential Code is not a building "
              "official. It is the people who connect your services, and two "
              "separate statutes put them in that position.", S["body"]),
    Paragraph("<b>Power.</b> \"<i><b>After a certified electrical inspector "
              "has been provided for by the local government or the "
              "department</b>, no utility shall initiate permanent electrical "
              "service to any new building … until a final certificate of "
              "approval has been issued by a certified electrical "
              "inspector.</i>\" Read the opening condition: the bar switches on "
              "once an inspector has been provided for. In practice that is "
              "everywhere — <b>all 119 of the Department's published county "
              "sheets name a state electrical inspector.</b> "
              "(KRS 198B.060(11))", S["body"]),
    Paragraph("<b>Water.</b> \"<i>No permanent water supply shall be provided "
              "to any building by any public utility or water district where "
              "the interior plumbing system has not been installed and "
              "approved in accordance with the provisions of KRS Chapter 318 "
              "and the State Plumbing Code.</i>\" No condition on that one at "
              "all. (KRS 318.165)", S["body"]),
    Paragraph("<b>And a third gate sits behind the first.</b> A certified "
              "electrical inspector may not issue a certificate of approval "
              "for temporary or permanent wiring \"<i>unless the inspector has "
              "in his or her possession a notice of release</i>\" from the "
              "local health department — the initial release comes when you "
              "apply for the septic site evaluation, the final release "
              "\"<i>upon approval of an on-site sewage disposal plan</i>.\" On "
              "a septic site your health department therefore gates your "
              "electricity as well as your plumbing permit. (This does not "
              "apply in a county that has adopted the Uniform State Building "
              "Code and enforces on-site sewage permitting.) "
              "(KRS 211.350(8))", S["body"]),
    Paragraph("So the county may not care whether your house was ever "
              "inspected — but you will still be sitting in a finished, "
              "unpowered, waterless building until an electrical inspector and "
              "a plumbing inspector have both signed. <b>Plan the build around "
              "those signatures, not around the building permit.</b>",
              S["body"]),
]))

# ---------------------------------------------------------------- trade work
flow += k.h2_tight("DOING YOUR OWN WIRING, PLUMBING AND HVAC")
flow.append(k.body(
    "Kentucky lets a homeowner do all three. It is one of the genuinely "
    "generous states on this. But the three permissions come from <b>three "
    "different instruments with three different tests</b>, and they are "
    "commonly — including in print — flattened into one rule with conditions "
    "borrowed from whichever is strictest. Read them separately."))

trade_rows = [
    [k.cellp("<b>Electrical</b>"),
     k.cellp("The widest of the three, and it is a single sentence: "
             "\"<i>Nothing in KRS 227A.010 to 227A.140 shall prohibit or "
             "interfere with the ability of <b>a homeowner or farmer to "
             "install or repair electrical wiring on his or her real "
             "property</b>.</i>\" Note what is <b>not</b> in it — no occupancy "
             "condition, no single-family limitation, no requirement that you "
             "personally perform the work, no time limit, and no affidavit. "
             "Farmers are named expressly."),
     k.cellp("KRS 227A.030(3)")],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp("Narrower, and it lives in a <b>regulation</b>, not the statute — "
             "KRS 318.030(1) itself is flat that no person shall engage in "
             "plumbing without a master's or journeyman's license. The "
             "regulation issues a permit to a homeowner working \"<i>in a home "
             "occupied by the homeowner <b>or</b> constructed by the homeowner "
             "for the homeowner's own personal residential use</i>\" on five "
             "conditions: apply before you start; file an <b>affidavit</b>; "
             "work to 815 KAR Chapter 20; <b>all work personally performed by "
             "you</b>; and no other homeowner permit for construction of a new "
             "home in the last <b>five years</b>."),
     k.cellp("815 KAR 20:050, Section 2(1)(b); KRS 318.030(1)")],
    [k.cellp("<b>HVAC</b>"),
     k.cellp("The statutory exemption is bare — \"<i>an individual owner of "
             "real property while practicing heating, ventilation, and air "
             "conditioning work on or within property <b>owned and "
             "occupied</b> by the individual</i>\" — but the permit regulation "
             "adds the most paperwork of the three: an <b>affidavit</b>, "
             "<b>proof of adequate sizing</b>, and <b>a complete design plan "
             "of all related duct and piping</b>, all filed with the "
             "application, plus personal performance."),
     k.cellp("KRS 198B.674(3); 815 KAR 8:070, Section 2(2)")],
]
flow.append(k.ref_table(
    "Three exemptions, three different tests",
    [k.cellp("Trade", bold=True),
     k.cellp("What the instrument actually says", bold=True),
     k.cellp("Authority", bold=True)],
    trade_rows, [1.0 * inch, CW - 1.0 * inch - 1.72 * inch, 1.72 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "<b>Do not flatten them.</b> They differ on <b>occupancy</b> (HVAC "
    "requires you to own <i>and</i> occupy; plumbing accepts a home you are "
    "building for your own use; electrical does not mention occupancy at "
    "all), on <b>who holds the tool</b> (plumbing and HVAC both require the "
    "work to be personally performed by you; the electrical sentence imposes "
    "no such condition), and on <b>paperwork</b> (electrical: none; plumbing: "
    "an affidavit; HVAC: an affidavit plus sizing proof plus a duct and piping "
    "design). All three exempt you from a <b>license</b> only — never from the "
    "permit, and never from the code."))

flow.append(k.callout("The five-year rules are two separate counters", [
    Paragraph("Both the plumbing and the HVAC homeowner permits are "
              "rationed, and the two rations are worded differently — so "
              "using one does not spend the other, and one is stricter than "
              "people assume.", S["body"]),
    Paragraph("<b>Plumbing</b> bars you only if you \"<i>obtained another "
              "homeowner permit <b>for construction of a new home</b> issued "
              "within the last five (5) years</i>\" — a homeowner plumbing "
              "permit for a repair or a remodel does not use up your "
              "allowance. <b>HVAC</b> has no such qualifier: \"<i><b>Only one "
              "(1) homeowner HVAC construction permit shall be issued to an "
              "individual within a five (5) year period.</b></i>\" Any "
              "homeowner HVAC construction permit counts. If you pulled one "
              "for a previous property, check the date before you plan on "
              "installing your own system.", S["body"]),
]))
flow.append(k.cite(
    "815 KAR 20:050 Section 2(1)(b)5 (plumbing, last effective March 1, 2022); "
    "815 KAR 8:070 Section 2(3) (HVAC). Both read at apps.legislature.ky.gov, "
    "August 2026. Note also that no local government may add to the HVAC "
    "scheme: \"<i>No local governing entity shall impose any other additional "
    "heating, ventilation, and air conditioning inspection or permit "
    "requirements, or establish any local inspection or permitting program, "
    "unless those provisions were in place before January 1, 2007.</i>\" "
    "(KRS 198B.6673(4)) Local HVAC programs are frozen at their 2007 "
    "footprint."))

# ---------------------------------------------------------------- affidavit
flow += k.h2_tight("THE AFFIDAVIT NOBODY WARNS YOU ABOUT")
flow.append(k.body(
    "If you <i>do</i> apply for a building permit, Kentucky makes you swear to "
    "something about other people. No permit may be issued by any building "
    "department or political subdivision \"<i>unless the person shall assure, "
    "<b>by affidavit</b>, that all contractors and subcontractors employed, or "
    "that will be employed, on activity covered by the permit shall be in "
    "compliance with Kentucky requirements for <b>workers' compensation "
    "insurance</b> according to KRS Chapter 342 and <b>unemployment "
    "insurance</b> according to KRS Chapter 341</i>.\""))
flow.append(k.body(
    "The penalty is not nominal and it is not capped at a flat number. A "
    "person who fails to comply \"<i>shall be fined an amount not to exceed "
    "<b>four thousand dollars ($4,000)</b> or an amount equal to <b>the sum of "
    "all uninsured and unsatisfied claims</b> brought under … KRS Chapter 342 "
    "and unemployment insurance claims for which no wages were reported …, "
    "<b>whichever is greater</b></i>\" — and it is enforced by your county "
    "attorney. Read that as: if an uninsured subcontractor is badly hurt on "
    "your site, the ceiling is the size of the injury, not $4,000."))
flow.append(k.body(
    "This is the single strongest practical argument for collecting a "
    "certificate of insurance from every sub before they set foot on the "
    "property. <b>KY.2</b> gives you the log to record them in."))
flow.append(k.cite("KRS 198B.060(10)(a), (b), (c)."))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS BEFORE YOU APPLY")
flow.append(k.body(
    "Every line below is either a condition Kentucky law imposes or a fact you "
    "have to establish about your own parcel. Work down it with a pen. If you "
    "cannot check a box, resolve it before you file — not after."))

flow += k.check_table("Step 1 — Settle the jurisdiction question first", [
    ("Asked your <b>city</b> whether it has an ordinance requiring building "
     "permits and inspections for single-family dwellings",
     [("Answer (Y/N):", 0.4), ("Who told you:", 0.6)]),
    ("Asked your <b>county</b> the same question — if the parcel is outside "
     "city limits, this is the one that governs",
     [("Answer (Y/N):", 0.4), ("Who told you:", 0.6)]),
    "If <b>either</b> says yes, you are on the ordinary permitted path and "
    "KY.2 applies in full",
    "If <b>both</b> say no, you still need the state plumbing permit, the "
    "state HVAC permit, and an electrical certificate of approval — and you "
    "should still consider requesting a certificate of occupancy",
    ("Confirmed whether your parcel is subject to <b>county planning and "
     "zoning</b>, which is a separate question from building permits",
     [("Answer:", 1.0)]),
], notes_header="Notes / who confirmed")

flow += k.check_table("Step 2 — The trade exemptions you are relying on", [
    "<b>Electrical:</b> you are the homeowner (or farmer) and the wiring is on "
    "your own real property — KRS 227A.030(3). No further conditions apply to "
    "the license exemption",
    "<b>Electrical, the real gate:</b> identified who your <b>certified "
    "electrical inspector</b> will be, because your power company cannot "
    "connect you permanently without their final certificate of approval",
    "<b>Plumbing:</b> the home is occupied by you or being built for your own "
    "personal residential use; you will file the affidavit; <b>you personally</b> "
    "will do the work",
    ("<b>Plumbing, five-year check:</b> you have not obtained a homeowner "
     "plumbing permit for construction of a new home in the last five years",
     [("Last one (date or none):", 1.0)]),
    "<b>HVAC:</b> you own <b>and occupy</b> the property, and you personally "
    "will install the system",
    ("<b>HVAC, five-year check:</b> you have not been issued <i>any</i> "
     "homeowner HVAC construction permit in the last five years — stricter "
     "than the plumbing rule",
     [("Last one (date or none):", 1.0)]),
    "<b>HVAC paperwork ready:</b> affidavit, proof of adequate sizing, and a "
    "complete design plan of all related duct and piping",
    "For any trade you will <b>not</b> do yourself, the licensed contractor "
    "you hire will pull that permit under their own license",
    ("Each contractor's state license verified with the Department of "
     "Housing, Buildings and Construction before they start",
     [("Verified on:", 1.0)]),
], notes_header="Notes / evidence")

flow += k.check_table("Step 3 — Protect yourself", [
    "Certificate of insurance collected from <b>every</b> subcontractor, "
    "showing workers' compensation cover — you may be signing an affidavit "
    "about their compliance",
    "Decided whether you will request a <b>certificate of occupancy</b> even "
    "if your jurisdiction does not require one, and why (KRS 198B.130(1))",
    "Photographic record of every stage that will be covered up, whether or "
    "not an inspector ever attends",
    ("Asked the Division of Plumbing whether your house needs a <b>plumbing "
     "plan submission</b> or will be handled by field inspection — the "
     "regulation and its enabling statute do not line up cleanly here, so get "
     "your answer in writing",
     [("Answer:", 1.0)]),
], notes_header="Notes / evidence")

flow.append(k.body(
    "<b>Step 4 — the paperwork itself</b> (the applications, the septic "
    "approval that gates the plumbing permit, code editions and fees) is "
    "worked in <b>KY.2 Permit Application Checklist</b>, and every document is "
    "described in <b>KY.5 Forms &amp; Documents Index</b>."))

# ---------------------------------------------------------------- penalties
flow += k.h2_tight("WHAT IT COSTS TO GET IT WRONG")
flow.append(k.bullet(
    "<b>Unlicensed plumbing work</b> outside the homeowner permit: a fine of "
    "\"<i>not less than ten dollars ($10) nor more than one hundred dollars "
    "($100) or imprisoned for not more than ninety (90) days or both for each "
    "offense</i>\" — and \"<i><b>each day the violation continues shall "
    "constitute a separate offense</b></i>.\" The daily multiplier is the part "
    "that matters. (KRS 318.990)"))
flow.append(k.bullet(
    "<b>Building code and HVAC-permit violations</b> carry the bigger number: "
    "\"<i>not less than ten dollars ($10) nor more than <b>one thousand "
    "dollars ($1,000)</b>. Each day the violation continues shall constitute a "
    "separate offense.</i>\" It reaches the Uniform State Building Code, the "
    "Residential Code, and — named expressly — installing an HVAC system "
    "without the permit. (KRS 198B.990(1))"))
flow.append(k.bullet(
    "<b>No permanent power, no permanent water.</b> Not a fine — just a "
    "finished house you cannot live in. (KRS 198B.060(11); KRS 318.165)"))
flow.append(k.bullet(
    "<b>The workers' compensation affidavit:</b> up to $4,000 <i>or</i> the "
    "sum of all uninsured claims, whichever is greater. (KRS 198B.060(10)(b))"))
flow.append(k.bullet(
    "<b>No certificate of occupancy:</b> reasonable attorney's fees added to "
    "any damages award against you in a code-violation claim, for up to ten "
    "years. (KRS 198B.130)"))

flow.append(Spacer(1, 8))
flow.append(k.callout("Three things Kentucky does NOT do to you", [
    Paragraph("Worth knowing, because guides written for other states import "
              "all three. Kentucky sets <b>no holding period</b> and no "
              "\"not offered for sale within X months\" clause on an "
              "owner-builder — there is no builder license to be exempt from, "
              "so there is nothing for a resale to disqualify you from. It "
              "sets <b>no project-cost threshold</b>. And it has <b>no state "
              "owner-builder affidavit</b> about occupancy; the affidavits "
              "Kentucky does require are the trade ones (plumbing and HVAC) "
              "and the workers' compensation one, and they are about "
              "different things entirely.", S["body"]),
    Paragraph("The trade exemptions do carry their own occupancy tests, and "
              "the plumbing and HVAC five-year rations are real. Those are the "
              "limits to plan around — not an imaginary resale window.",
              S["body"]),
]))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("The code is mandatory statewide and reaches single-family dwellings by "
     "definition", "KRS 198B.010(4); 198B.050(1)"),
    ("Permits, inspections and certificates of occupancy are not mandatory "
     "for a single-family residence unless a local government passes an "
     "ordinance", "KRS 198B.060(1), (8), (13); 815 KAR 7:125 §2(2)(a)"),
    ("The department may not preempt or assert jurisdiction over enforcement "
     "on single-family dwellings — there is no state backstop",
     "KRS 198B.060(4)(b)"),
    ("State plumbing installation permit required from the department; the "
     "chapter is in force in all counties but not on farmsteads; the septic "
     "permit must accompany the application",
     "KRS 318.134(1)(a), (2); 318.015(1), (3)"),
    ("State HVAC permit required before an initial system is installed, in "
     "any building designed for human occupancy",
     "KRS 198B.6671(1), (6)"),
    ("No permanent electric service without a certified electrical "
     "inspector's final certificate of approval; no permanent water supply "
     "until the plumbing is approved", "KRS 198B.060(11); 318.165"),
    ("Homeowner and farmer electrical exemption, with no occupancy, "
     "single-family or personal-performance condition", "KRS 227A.030(3)"),
    ("Homeowner plumbing permit: affidavit, personally performed, one "
     "new-home permit per five years — a regulation, not a statute",
     "815 KAR 20:050 §2(1)(b); KRS 318.030(1)"),
    ("Homeowner HVAC exemption requires owned AND occupied; the permit adds "
     "an affidavit, sizing proof and a duct and piping design; one permit per "
     "five years", "KRS 198B.674(3); 815 KAR 8:070 §2(2), (3)"),
    ("The workers' compensation and unemployment insurance affidavit, and its "
     "$4,000-or-greater penalty enforced by the county attorney",
     "KRS 198B.060(10)"),
    ("Private action for a code violation: one year from discovery, ten years "
     "outside, attorney's fees added if no certificate of occupancy issued",
     "KRS 198B.130(1), (2)"),
    ("Penalties: $10–$1,000 per day under the building chapter, reaching the "
     "codes and the HVAC permit; $10–$100 per day for plumbing",
     "KRS 198B.990(1); 318.990"),
    ("No local government may adopt or enforce any other building code for "
     "one- and two-family dwellings or townhouses",
     "Kentucky Residential Code R101.3"),
    ("On a septic site the health department's notice of release also gates "
     "the electrical certificate of approval", "KRS 211.350(8)"),
]))
flow.append(k.cite(k.STATUTE_NOTE))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ky-permit-kit",
                       "KY.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
