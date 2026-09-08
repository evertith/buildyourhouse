#!/usr/bin/env python3
"""NY.2 Permit Application Checklist.

Every New York claim in this document was read against its primary source in
September 2026 and is cited on-page.

The organizing idea: Part 1203 is a FLOOR, not the permit ordinance. It tells
you the least any permit office may ask for — and the least it may inspect —
and then lets the local law add to it. So this document prints the floor with
its cite, then gives a write-in line for the local answer, and never invents a
fee or a review clock where the rule has none.

Three New York facts drive the structure. Plans for a house over 1,500 sq ft
gross must be stamped — a state law, not a local one. The climatic numbers
(frost, snow, wind) are written into Table R301.2 BY THE PERMIT OFFICE, so
there is no statewide frost depth to print. And the energy values are New
York's own, stricter than the model code the guide-writers copy from.

Verified sources:
  19 NYCRR § 1203.3(a)(1)     permit required; eight OPTIONAL exemptions
  19 NYCRR § 1203.3(a)(2)     application contents — tax map number, statement
                              of special inspections
  19 NYCRR § 1203.3(a)(3)     drawing contents — braced wall designs, thermal
                              envelope, energy statement, site plan "drawn in
                              accordance with an accurate boundary survey",
                              design-professional evidence
  19 NYCRR § 1203.3(a)(4)–(8) plan examination, expiry, revocation, display;
                              NO review clock; NO fee (verified absence)
  Ed. Law § 7307(5), § 7209(7)(b)  the 1,500 sq ft stamped-plan rule
  Ed. Law § 7307(1), § 7209(1)     officials may not accept unstamped plans
  2025 RCNYS [NY] R106.6       design professional "when required by Article
                              145 or Article 147 of the Education Law"
  2025 RCNYS [NY] R106.1, R106.2  waiver of documents; site plan
  2025 RCNYS [NY] R301.2 notes b, d, o  the AHJ fills in frost, wind, snow
  19 NYCRR § 1202.12          where DOS is AHJ the OWNER supplies the criteria
  2025 RCNYS [NY] R301.2.3    70 psf engineering threshold; Fig. R301.2(4)
                              note 1, +2 psf per 100 ft above 1,000 ft
  2025 ECCCNYS [NY] Table R301.1(1)  climate zone by county
  2025 ECCCNYS [NY] Table R402.1.3   R-49, U-0.27, walls R-30 or 20&5ci
  2025 ECCCNYS [NY] R402.5.1.2, .3   testing mandatory; 3.0 / 2.5 ACH
  2025 ECCCNYS R401.2, R401.3        compliance paths; the posted certificate
  19 NYCRR § 1203.2(e)(4)     electrical is a special inspection
  2025 RCNYS [NY] R309.2, R310.2.1, R306.1, R115, R101.2.1, R104.2.2
  19 NYCRR § 1219.2(a)(18)    "story above grade plane"
  Exec. Law § 378(5-a), (5-b), (5-c)  CO alarms, smoke alarms, solid fuel
  10 NYCRR § 75.5(b); App. 75-A §§ 75-A.3(b), 75-A.4(a), (b), 75-A.6(a)
  10 NYCRR App. 5-B Table 1; 2025 RCNYS [NY] P2602.1.1; ECL § 15-1525
  GBL §§ 770, 771; Lien Law § 71-a(4)  the custom-home contract

DELIBERATELY NOT CLAIMED, and why:
  - Any permit fee figure. Part 1203 sets none; the DOS model local law says a
    fee schedule "shall be established by resolution." One town's number on
    one day is worse than no number.
  - Any review-clock or CO-clock day count. None exists in Part 1203 or
    Article 18 (verified absence).
  - A frost depth by region. Table R301.2 note b puts the number in the hands
    of the permit office. The "36/42/48 in" tables are local custom.
  - A ground snow load by county. Parcel-specific from two figures and an
    elevation surcharge; the 70 psf figure is a code threshold, not a county.
  - Any radon construction requirement. Appendix BE is "for informational
    purposes" ([NY] R101.2.1).
  - A 2025 NYStretch. NYSERDA published only the 2020 edition in Sept 2026.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
sys.path.insert(0, os.path.dirname(os.path.dirname(_HERE)))

from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer

import kit as k

S = k.S
CW = k.CW
sec = k.sec
NB = k.NB
CITE = k.CITE_COL

FORM_ID = "NY.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "What to Gather"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "What the state rule entitles your permit office to demand, the numbers "
    "it fills in itself, and the New York values that make the model code "
    "book on your desk wrong.")

flow.append(k.disclaimer(
    "Part 1203 sets no fee and no review clock. Where a number is the "
    "permit office's to set, this document gives you a line, not a guess."))
flow.append(Spacer(1, 10))

# ------------------------------------------------------- the application
flow += k.h2_tight("WHAT THE APPLICATION MUST CONTAIN — THE STATE FLOOR", 2.2)
flow.append(k.body(
    "Every code enforcement program in the state — town, county or DOS — must "
    "require at least this. Your office's local law may add to it, and "
    "“may adopt provisions for administration and enforcement that are more "
    f"stringent than the minimum standards” (19 NYCRR {sec('1203.3')}). It "
    "may not require less."))
rows = [
    [k.cellp("<b>The application</b>"),
     k.cellp("A description of the location, nature, extent and scope of the "
             "work; <b>the tax map number</b> and street address; the "
             "occupancy classification; where applicable, a <b>statement of "
             "special inspections</b> (this is where your electrical agency "
             "goes); construction documents; any submittal the codes require; "
             "and anything else the office “may deem necessary.”"),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(a)(2)"))],
    [k.cellp("<b>The drawings</b>"),
     k.cellp("“Drawn to scale on suitable material or in electronic media,” "
             "and where applicable showing: the means of egress; “a "
             "representation of the <b>building thermal envelope</b>”; "
             "structural information “including but not limited to <b>braced "
             "wall designs</b>; the size, section, and relative locations of "
             "structural members; design loads”; every service system; and "
             "“a <b>written statement indicating compliance with the Energy "
             "Code</b>.”"),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(a)(3)"))],
    [k.cellp("<b>The site plan</b>"),
     k.cellp("“A site plan, drawn to scale and <b>drawn in accordance with an "
             "accurate boundary survey</b>, showing the size and location of "
             "new construction and existing structures and appurtenances on "
             "the site; distances from lot lines; the established street "
             "grades and the proposed finished grades; and, as applicable, "
             "flood hazard areas, floodways, and design flood elevations.” "
             "A sketch on the deed plat is not this."),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(a)(3)(viii)"))],
    [k.cellp("<b>The stamp, when one is required</b>"),
     k.cellp("Evidence that the documents were prepared by a New York "
             "licensed architect (Ed. Law Art. 147) or engineer (Art. 145): "
             "the seal, the signature, the registration expiration date, "
             "and the firm's Certificate of Authorization number where a "
             "firm rather than a sole practitioner submits. <b>When</b> a "
             "stamp is required is the next section."),
     k.cellp("19 NYCRR<br/>" + sec("1203.3(a)(3)(ix)"))],
]
flow.append(k.ref_table(
    "The Part 1203 floor for a building permit application",
    [k.cellp("Item", bold=True), k.cellp("What the rule requires", bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.35 * inch, CW - 1.35 * inch - CITE, CITE]))
flow.append(Spacer(1, 6))
flow.append(k.callout(
    "Three things the rule does not do", [
        Paragraph("<b>No fee.</b> Part 1203 carries no fee schedule; the DOS "
                  "model local law says a fee schedule “shall be established "
                  "by resolution” of the legislative body. <b>No review "
                  "clock.</b> Nothing in Part 1203 or Article 18 sets a "
                  "number of days for plan examination. <b>No mandatory "
                  "exemption list.</b> The eight categories the rule lets an "
                  "office exempt — one-story accessory sheds to "
                  "<b>144&#160;sq&#160;ft</b>, window awnings, finish work, "
                  "listed portable appliances, like-for-like equipment "
                  "replacement, non-structural repairs — are exempt only "
                  "<i>if your municipality adopted the exemption</i> "
                  f"({sec('1203.3(a)(1)')}), and “an exemption from the "
                  "requirement to obtain a building permit shall not be "
                  "deemed an authorization for work to be performed in "
                  "violation” of the codes. Ask your office for its fee, its "
                  "review time and its exemption list, and write the answers "
                  "on the permit record at the end.", S["body"]),
    ]))

# ------------------------------------------------------------- CE-200
flow += k.h2_tight("BEFORE ANYTHING ELSE: THE CE-200 OR THE CARRIER FORMS",
                   1.8)
flow.append(k.body(
    "General Municipal Law " + sec("125") + " forbids any city, town or "
    "village to issue a building permit without carrier proof of coverage or "
    "an affidavit of no employees (NY.1). Do this first: the certificate is "
    "<b>job-specific</b> and takes an online account to obtain."))
flow.append(k.checklist([
    "I created a NY.gov Business account at <b>businessexpress.ny.gov</b> "
    "and applied for Form CE-200 under <b>Apply as a Homeowner</b> — or, if "
    "I carry a policy, asked my carrier to send Forms C-105.2 and DB-120.1 "
    "to the permit office.",
    "I printed and signed the CE-200 and recorded its number. I know it "
    "covers <b>this permit only</b>, and a separate certificate is needed for "
    "any later permit.",
    "From every trade I hire, I am collecting a C-105.2 and DB-120.1 naming "
    "me as certificate holder — <b>not an ACORD certificate</b>, which the "
    "Board says is not acceptable proof.",
]))

# ------------------------------------------------------------ stamped plans
flow += k.h2_tight("STAMPED PLANS — THE 1,500 SQUARE FOOT RULE", 1.8)
flow.append(k.body(
    "This is a state law, and it applies whichever government issues your "
    "permit. Education Law " + sec("7307(5)") + " (architecture) provides "
    "that the article “shall not apply to … <b>residence buildings of gross "
    "area of fifteen hundred square feet or less, not including garages, "
    "carports, porches, cellars, or uninhabitable basements or attics</b>.” "
    "Section " + sec("7209(7)(b)") + " (engineering) carries the same "
    "exclusion. Above that line, " + sec("7307(1)") + " and "
    + sec("7209(1)") + " forbid any state, county, city, town or village "
    "official to “accept or approve any plans or specifications that are not "
    "stamped” by a New York-licensed architect or engineer."))
rows = [
    [k.cellp("<b>More than 1,500&#160;sq&#160;ft gross</b>"),
     k.cellp("Architect- or engineer-stamped drawings, statewide. Gross area "
             "excludes the garage, carport, porches, cellar and any "
             "uninhabitable basement or attic — so a 1,400&#160;sq&#160;ft "
             "house on a full unfinished basement is under the line."),
     k.cellp("Ed. Law<br/>" + sec("7307(5)") + ";<br/>" + sec("7209(7)(b)"))],
    [k.cellp("<b>1,500&#160;sq&#160;ft or less</b>"),
     k.cellp("The state does not require a stamp — <b>but the code hands the "
             "question back to your office.</b> Documents “shall be prepared "
             "by a registered design professional when required by Article "
             "145 or Article 147 … <b>by the stricter of</b> Code Enforcement "
             "Program of the authority having jurisdiction or a Part "
             "1203-Compliant Code Enforcement Program, or by any other "
             "applicable law.” Ask whether the local law requires one."),
     k.cellp("2025 RCNYS<br/>[NY] R106.6")],
    [k.cellp("<b>Either way</b>"),
     k.cellp("The office may still demand “structural information including "
             "… braced wall designs” " + f"({sec('1203.3(a)(3)(v)')})" +
             ", and any site with a ground snow load above "
             "<b>70&#160;psf</b> must be “designed in accordance with "
             "accepted engineering practice” — see below. Separately, the "
             "office “may waive the requirement for construction documents "
             "where a registered design professional is not required by law” "
             "and the work is minor."),
     k.cellp("2025 RCNYS<br/>[NY] R301.2.3;<br/>[NY] R106.1")],
]
flow.append(k.ref_table(
    "Who must draw your house",
    [k.cellp("Size", bold=True), k.cellp("What the law requires", bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.55 * inch, CW - 1.55 * inch - CITE, CITE]))
flow.append(k.cite(
    "Article 147 is architecture, Article 145 engineering. Education Law "
    f"{sec('7306(1)(c)')} separately confirms that “builders, or "
    "superintendents employed by such builders” may supervise construction "
    "without an architect — so the stamp is about the <i>drawings</i>, not "
    "about who swings the hammer."))

# --------------------------------------------------------- Table R301.2
# 1.6in: the stamped-plans cite ends ~2.3in from the foot of its page; at 2.2
# the reserve fired and left the tail of that page blank. The nine-line lead
# under this heading splits cleanly, and the frost-depth box that follows it
# is a KeepTogether that moves on its own.
flow += k.h2_tight("TABLE R301.2 — THE NUMBERS YOUR OFFICE FILLS IN", 1.6)
flow.append(k.body(
    "Every residential code has a Table R301.2 of climatic and geographic "
    "design criteria. In New York the table is blank until the permit office "
    "fills it. [NY] R301.2: “Additional criteria shall be established by the "
    "authority having jurisdiction and set forth in Table R301.2.” The "
    "footnotes are explicit — note b: “The authority having jurisdiction "
    "shall fill in the <b>frost line depth</b> column with the minimum depth "
    "of footing below finish grade.” Note d: the AHJ “shall fill in this part "
    "of the table with the <b>wind speed</b> from the ultimate design wind "
    "speeds map.” Note o: the AHJ “shall fill in this section … using the "
    "<b>Ground Snow Loads</b> in Figure R301.2(3) in accordance with Section "
    "R301.2.3.”"))
flow.append(k.callout(
    "So there is no statewide frost depth, and this kit prints none", [
        Paragraph("Guides that print “36 inches south of the Catskills, "
                  "42 inches upstate, 48 inches in the North Country” are "
                  "describing local custom. The number that binds your "
                  "footings is the one your office wrote into its Table "
                  "R301.2 — ask for the table, and copy it below. Where DOS "
                  "is the permit office, 19 NYCRR " + sec("1202.12") +
                  " reverses the burden: <b>you</b> supply “ground snow load; "
                  "wind design loads; seismic design category; potential "
                  "damage from weathering, frost, and termite; winter design "
                  "temperature; whether ice barrier underlayment is required; "
                  "the air freezing index; and the mean annual temperature,” "
                  "and if the town never set them, a licensed architect or "
                  "engineer establishes them (" + sec("1202.12(b)") + ").",
                  S["body"]),
    ]))
flow.append(Spacer(1, 2))
flow += k.check_table(
    "My office's Table R301.2 — copy every entry", [
        ("Frost line depth (minimum footing depth below finish grade):",
         [("Inches", 0.4), ("Source", 0.6)]),
        ("Ground snow load, allowable stress design, for this parcel:",
         [("psf", 0.4), ("Elevation surcharge applied?", 0.6)]),
        ("Ultimate design wind speed, and whether the parcel is in a "
         "windborne-debris region:", [("mph", 0.4), ("Debris region?", 0.6)]),
        ("Seismic design category; weathering; termite:",
         [("Seismic", 0.34), ("Weathering", 0.33), ("Termite", 0.33)]),
        ("Winter design temperature; ice barrier underlayment required?; "
         "air freezing index; mean annual temperature:",
         [("Winter °F", 0.25), ("Ice barrier", 0.25), ("AFI", 0.25),
          ("Mean °F", 0.25)]),
        ("Flood hazard: FIRM panel and date, zone, and design flood "
         "elevation if any:", [("Panel", 0.4), ("Zone", 0.3), ("DFE", 0.3)]),
    ])

# ------------------------------------------------------------------ snow
flow += k.h2_tight("SNOW — THE NUMBER THAT FORCES AN ENGINEER", 2.2)
flow.append(k.callout_long(
    "2025 RCNYS [NY] R301.2.3 Snow loads — the operative sentences", [
        Paragraph("“Ground snow loads shall be the larger of those determined "
                  "in accordance with Figure R301.2(3) and Figure R302.2(4) "
                  "[sic — the figure is R301.2(4)], or shall be determined in "
                  "accordance in with Section 1608 of the Building Code of "
                  "New York State. Wood-framed construction … in regions with "
                  "allowable stress design ground snow loads, pg(asd), "
                  "<b>70&#160;pounds per square foot</b> (3.35 kPa) or less, "
                  "shall be in accordance with Chapters 5, 6 and 8. Buildings "
                  "in regions with allowable stress design ground snow loads, "
                  "pg(asd), <b>greater than 70&#160;pounds per square foot</b> "
                  "(3.35 kPa) shall be designed in accordance with accepted "
                  "engineering practice.”", S["body"]),
        Paragraph("<b>And the elevation surcharge</b>, Figure R301.2(4) "
                  "Note 1: “For sites at elevations above 1,000&#160;feet "
                  "(304.8&#160;m), the ground snow load shown in Figure "
                  "301.2(4) shall be increased from the mapped value by "
                  "<b>2&#160;psf</b> (0.096&#160;kN/m2) for every "
                  "<b>100&#160;feet</b> (30.48&#160;m) above 1,000&#160;feet "
                  "(304.8&#160;m).”", S["body"]),
    ]))
flow.append(k.cite(
    "<b>Read it as an instruction.</b> Pull both figures for the parcel — "
    "Figure R301.2(3) Note 1 points to the ASCE 7 Hazard Tool geodatabase "
    "(asce7hazardtool.online) and Figure R301.2(4) is the New York map — add "
    "2&#160;psf per 100&#160;ft above 1,000&#160;ft to the mapped value, and "
    "take the larger. Over 70&#160;psf the prescriptive framing chapters no "
    "longer apply and the roof needs an engineer whatever the house's size. "
    "The 70&#160;psf figure is a <b>statewide code threshold</b>, not any "
    "county's policy, and this kit prints no county list — a hillside lot in "
    "a valley county can cross it on the surcharge alone."))

# ---------------------------------------------------------------- energy
# 1.6in for the same reason: the snow cite ends ~1.8in from the foot, and the
# seven-line lead under this heading splits cleanly ahead of the zone table.
flow += k.h2_tight("ENERGY — NEW YORK'S OWN VALUES, NOT THE MODEL CODE'S", 1.6)
flow.append(k.body(
    "19 NYCRR " + sec("1240.4(a)") + " adopts the 2025 ECCCNYS Residential "
    "Provisions. The book carries New York values tagged [NY], and they "
    "differ from the 2024 IECC in the two places guide-writers copy from: "
    "the ceiling stays at <b>R-49</b> (the model code is R-60 in Zones 5–6) "
    "and the window U-factor is <b>0.27</b> (the model code is 0.30). Build "
    "to a national reference and you will miss both. First, find your "
    "county's zone — the table is in the code, not on NYSERDA's website."))
rows = [
    [k.cellp("<b>Zone 4</b>"),
     k.cellp("Bronx, Kings, Nassau, New York, Queens, Richmond, Suffolk, "
             "<b>Westchester</b>")],
    [k.cellp("<b>Zone 6</b>"),
     k.cellp("Chenango, Clinton, <b>Delaware</b>, Essex, Franklin, Fulton, "
             "Hamilton, Herkimer, Jefferson, Lewis, Madison, Montgomery, "
             "Oneida, Otsego, St. Lawrence, <b>Sullivan</b>, <b>Ulster</b>, "
             "Warren")],
    [k.cellp("<b>Zone 5</b>"),
     k.cellp("Every other county — Albany, Allegany, Broome, Cattaraugus, "
             "Cayuga, Chautauqua, Chemung, Columbia, Cortland, Dutchess, "
             "Erie, Genesee, Greene, Livingston, Monroe, Niagara, Onondaga, "
             "Ontario, Orange, Orleans, Oswego, Putnam, Rensselaer, Rockland, "
             "Saratoga, Schenectady, Schoharie, Schuyler, Seneca, Steuben, "
             "Tioga, Tompkins, Washington, Wayne, Wyoming, Yates")],
]
flow.append(k.ref_table(
    "Climate zone by county — 2025 ECCCNYS [NY] Table R301.1(1)",
    [k.cellp("Zone", bold=True), k.cellp("Counties", bold=True)],
    rows, [0.95 * inch, CW - 0.95 * inch]))
flow.append(k.cite(
    "Note that <b>Ulster, Sullivan and Delaware are Zone 6</b> — the "
    "Catskills, not just the North Country — and Westchester is Zone 4 with "
    "Long Island. The zone decides the air-leakage limit below."))

flow.append(Spacer(1, 4))
rows = [
    [k.cellp("Ceiling"), k.cellp("<b>R-49</b>", center=True)],
    [k.cellp("Insulation entirely above roof deck"),
     k.cellp("R-30 ci", center=True)],
    [k.cellp("Wood-framed wall"),
     k.cellp("<b>R-30</b>, or 20&amp;5ci, or 13&amp;10ci, or 0&amp;20ci",
             center=True)],
    [k.cellp("Floor"), k.cellp("R-30, or 19&amp;7.5ci, or 20ci", center=True)],
    [k.cellp("Basement wall"), k.cellp("15ci, or 19, or 13&amp;5ci",
                                       center=True)],
    [k.cellp("Unheated slab"), k.cellp("R-10ci, 4&#160;ft", center=True)],
    [k.cellp("Heated slab"),
     k.cellp("R-10ci, 4&#160;ft <b>and</b> R-10 full slab", center=True)],
    [k.cellp("Crawl space wall"), k.cellp("15ci, or 19, or 13&amp;5ci",
                                          center=True)],
    [k.cellp("Vertical fenestration U-factor"),
     k.cellp("<b>0.27</b> (0.30 only above 4,000&#160;ft or in "
             "windborne-debris regions, Zones 5–6)", center=True)],
    [k.cellp("Skylight U-factor"), k.cellp("0.50", center=True)],
    [k.cellp("Glazed fenestration SHGC"),
     k.cellp("0.40 in Zones 4 and 5; not required in Zone 6", center=True)],
]
flow.append(k.ref_table(
    "Insulation minimum R-values — 2025 ECCCNYS [NY] Table R402.1.3, "
    "identical in Zones 4, 5 and 6",
    [k.cellp("Component", bold=True),
     k.cellp("Zones 4, 5, 6", bold=True, center=True)],
    rows, [2.4 * inch, CW - 2.4 * inch]))
flow.append(k.cite(
    "“13&amp;5ci” means R-13 cavity plus R-5 continuous. The U-factor "
    "alternative, [NY] Table R402.1.2: fenestration 0.27, ceiling 0.026, "
    "wood-frame wall 0.045, floor 0.033, basement wall 0.050, crawl space "
    "wall 0.055. R402.2.1 lets full-height uncompressed R-38 over the top "
    "plate satisfy the R-49 ceiling requirement in the prescriptive path."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "The blower door is mandatory, and the limit depends on your zone", [
        Paragraph("<b>[NY] R402.5.1.3:</b> the air leakage rate “shall be not "
                  "greater than <b>3.0 air changes per hour in Climate Zones "
                  "4 and 5</b>, or 0.19 cubic foot … of the building thermal "
                  "envelope area; and not greater than <b>2.5 air changes per "
                  "hour in Climate Zone 6</b>, or 0.16 cubic foot … of the "
                  "building thermal envelope area.” Exception 2: a building "
                  "of 1,500&#160;sq&#160;ft or less of conditioned floor area "
                  "may instead meet 0.27 cfm per square foot of enclosure "
                  "area.", S["body"]),
        Paragraph("<b>[NY] R402.5.1.2:</b> “The building or each dwelling "
                  "unit … shall be tested for air leakage … Where required by "
                  "the building official, testing shall be conducted by an "
                  "approved third party. A written report … shall be … "
                  "provided to the building official.” That written report "
                  "is a <b>certificate-of-occupancy precondition</b>: the "
                  "office may not issue the CO until it has “received and "
                  "reviewed each written statement of the results of tests "
                  "performed to show compliance with the Energy Code” "
                  f"(19 NYCRR {sec('1203.3(d)(2)(iv)')}).", S["body"]),
        Paragraph("<b>Three compliance paths</b> ([NY] R401.2): prescriptive "
                  "(R401–R404 <i>and</i> the R408 additional efficiency "
                  "package), simulated performance (R405), or Energy Rating "
                  "Index (R406). Whichever you use, a permanent R401.3 "
                  "certificate goes up at the furnace or utility room — NY.3 "
                  "lists what it must show.", S["body"]),
    ]))
flow.append(k.cite(
    "<b>NYStretch.</b> NYSERDA's stretch energy code is adopted municipality "
    "by municipality, and in September 2026 NYSERDA's site still offered the "
    "<b>2020</b> edition and said only that updates are “planned.” No "
    "statewide list of adopting municipalities is published. Ask your office "
    "whether it has adopted NYStretch and which edition; this kit prints "
    "nothing further about it."))

# ------------------------------------------------------------- electrical
flow += k.h2_tight("ELECTRICAL — NAME THE AGENCY ON THE APPLICATION", 2.0)
flow.append(k.body(
    "The application's “statement of special inspections” "
    f"({sec('1203.3(a)(2)(iv)')}) is where the electrical inspector is named, "
    "and the office may accept a special inspection only from a person "
    "“employed or retained by an agency that has been approved by the "
    "authority having jurisdiction” " + f"({sec('1203.2(e)(4)')})" + ". "
    "<b>There is no state list.</b> Ask the office for its list, engage an "
    "agency, and put the name on the application. The Electrical Part is NEC "
    "2023-based statewide (Chapters 34–43), limited to 120/240-volt, 0- to "
    "400-ampere single-phase services (E3401.2)."))
flow += k.check_table(
    "The electrical track, before you file", [
        ("Approved agencies the office will accept, and the one I engaged:",
         [("Agency", 1.0)]),
        ("Whether the local law lets a homeowner wire an owner-occupied "
         "house, and any local electrician license law:",
         [("Own wiring?", 0.4), ("License law?", 0.6)]),
    ])

# --------------------------------------------------------- code traps
flow += k.h2_tight("SPRINKLERS, ALARMS, FLOOD, SOLID FUEL — WHAT NEW YORK "
                   "CHANGED", 2.2)
rows = [
    [k.cellp("<b>Sprinklers at three stories</b>"),
     k.cellp("“An automatic sprinkler system shall be installed in one- and "
             "two-family dwellings where such dwellings have a height of "
             "<b>three stories above grade plane</b>.” A one- or two-story "
             "house needs none — but a walk-out basement <b>counts as a "
             "story</b> if its ceiling is more than 6&#160;ft above grade "
             "plane, more than 6&#160;ft above finished ground for over half "
             "the perimeter, or more than 12&#160;ft at any point. Townhouses "
             "also at any height with a public water main available."),
     k.cellp("2025 RCNYS<br/>[NY] R309.1, R309.2;<br/>19 NYCRR<br/>"
             + sec("1219.2(a)(18)"))],
    [k.cellp("<b>Heat detection in the garage</b>"),
     k.cellp("Smoke alarms in the dwelling per NFPA 72, <b>and</b> “heat "
             "detection shall be provided in new attached garages” — a New "
             "York addition. Carbon monoxide alarms per Fire Code §&#160;915; "
             "the statutory floor is a CO detector in every dwelling with a "
             "fuel-burning appliance or attached garage."),
     k.cellp("2025 RCNYS<br/>[NY] R310.2.1, R311;<br/>Exec. Law<br/>"
             + sec("378(5-a)"))],
    [k.cellp("<b>Flood — wider than the model code</b>"),
     k.cellp("Flood-resistant construction applies in “A Zones, <b>shaded X "
             "Zones, B Zones</b>, Coastal A Zones, and V Zones.” The model "
             "code stops at the A and V zones. If your FIRM shows shaded X, "
             "you are inside it."),
     k.cellp("2025 RCNYS<br/>[NY] R306.1")],
    [k.cellp("<b>Wood stove — a second permit</b>"),
     k.cellp("Any solid fuel-burning appliance, chimney or flue needs its own "
             "permit, inspection and <b>certificate of compliance before it "
             "is operated</b>; the statute sets a fine of not more than "
             "$250."),
     k.cellp("2025 RCNYS<br/>[NY] R115;<br/>Exec. Law<br/>"
             + sec("378(5-c)"))],
    [k.cellp("<b>Radon: not required</b>"),
     k.cellp("Appendix BE Radon Control Methods is “included for "
             "informational purposes” — not adopted, and a town cannot adopt "
             "it without Code Council approval (Exec. Law §&#160;379). "
             "<b>Appendix BB Tiny Houses IS adopted</b>; strawbale, cob and "
             "hemp-lime are informational, via written alternative-method "
             "approval."),
     k.cellp("2025 RCNYS<br/>[NY] R101.2.1;<br/>[NY] R104.2.2")],
]
flow.append(k.ref_table(
    "Five New York amendments a national code book will not show you",
    [k.cellp("Provision", bold=True), k.cellp("What New York says", bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - CITE, CITE]))
flow.append(k.cite(
    "The 2025 RCNYS renumbered Chapter 3: sprinklers are <b>R309</b>, smoke "
    "alarms R310, carbon monoxide R311, flood R306. A reference to “R313” for "
    "sprinklers is the 2020 numbering and is wrong in the 2025 book."))

# ----------------------------------------------------------- septic/well
flow += k.h2_tight("SEPTIC AND WELL — SETTLE THESE BEFORE THE FOOTPRINT", 2.2)
flow.append(k.body(
    "Both are inside the Uniform Code by reference — [NY] P2602.1.2 "
    "incorporates the Health Department's Appendix 75-A for septic and [NY] "
    "P2602.1.1 incorporates Appendix 5-B for wells — and both are approved "
    "by the county health department or DOH district office, not the "
    "building office (NY.4 has the routing). Two rules decide who does the "
    "work: septic plans “<b>shall be prepared directly by or under the "
    "supervision of a design professional</b>” (10 NYCRR "
    f"{sec('75.5(b)')}), and private wells “<b>shall be installed by a well "
    "driller registered with the Department of Environmental "
    "Conservation</b>” ([NY] P2602.1.1). You may not design the one or drill "
    "the other."))
rows = [
    [k.cellp("<b>Design flow</b>"),
     k.cellp("“A minimum daily flow of <b>110&#160;gallons per day per "
             "bedroom</b>” for new construction. A garbage grinder or an "
             "expansion attic counts as another bedroom."),
     k.cellp("App. 75-A<br/>" + sec("75-A.3(b)") + ";<br/>" + sec("75-A.6(a)"))],
    [k.cellp("<b>Tank</b>"),
     k.cellp("<b>1,000&#160;gal</b> for 1–3 bedrooms; 1,250 for 4; 1,500 for "
             "5; 1,750 for 6; +250 per bedroom beyond."),
     k.cellp("App. 75-A<br/>Table 3")],
    [k.cellp("<b>Absorption field distances</b>"),
     k.cellp("<b>100&#160;ft</b> to a well or suction line; <b>100&#160;ft</b> "
             "to a stream, lake, watercourse <b>or wetland</b>; "
             "<b>20&#160;ft</b> to the dwelling; <b>10&#160;ft</b> to the "
             "property line. Septic tank: 50 / 50 / 10 / 10. Well distances "
             "rise <b>50%</b> where aquifer water enters the well less than "
             "50&#160;ft below grade (note g), and to <b>200&#160;ft</b> where "
             "the system is upgrade and in the direct drainage path to the "
             "well (note a). Plus a <b>50% reserve area</b> “whenever "
             "possible.”"),
     k.cellp("App. 75-A<br/>Table 2;<br/>" + sec("75-A.4(a)(5)"))],
    [k.cellp("<b>Site disqualifiers</b>"),
     k.cellp("Below the 10-year flood level; slopes over <b>15%</b>; less "
             "than <b>four feet of useable soil</b> above rock or seasonal "
             "high groundwater; percolation faster than <b>one minute per "
             "inch</b> unless blended. Groundwater at least 2&#160;ft below "
             "trench bottom."),
     k.cellp("App. 75-A<br/>" + sec("75-A.4(a)") + ", (c)(2)")],
    [k.cellp("<b>The well</b>"),
     k.cellp("Appendix 5-B Table 1 protects the well from the other "
             "direction: 100&#160;ft from an absorption field, 50&#160;ft from "
             "a septic tank, 25&#160;ft from a stream or wetland, 200&#160;ft "
             "from a cesspool, 300&#160;ft from a salt pile — again +50% for a "
             "shallow well — and “a well shall be located upgradient of any "
             "potential or known source of contamination.” <b>Appendix 5-B "
             "sets no well-to-property-line or well-to-house distance.</b> "
             "The driller files a completion report with DEC and “shall "
             "provide a copy … to the water well owner.”"),
     k.cellp("App. 5-B<br/>Table 1; " + sec("5-B.2(c)") + ";<br/>ECL<br/>"
             + sec("15-1525(3)"))],
]
flow.append(k.ref_table(
    "The numbers that fix where the house can sit",
    [k.cellp("Item", bold=True), k.cellp("Rule", bold=True),
     k.cellp("Authority", bold=True)],
    rows, [1.5 * inch, CW - 1.5 * inch - CITE, CITE]))
flow.append(k.cite(
    "10 NYCRR Appendix 75-A effective 16&#160;March 2016; Appendix 5-B "
    "effective 23&#160;November 2005. <b>Two overlays change these numbers "
    "for one house</b>: inside the Adirondack Park the leach field must be "
    "100&#160;ft from the mean high-water mark in every land use area, and "
    "inside the New York City watershed the field must be 100&#160;ft from a "
    "watercourse or wetland and 300&#160;ft from a reservoir, with the "
    "plans approved by the City's Department of Environmental Protection. "
    "NY.4 has both."))

# ---------------------------------------------------------- the builder
flow += k.h2_tight("IF YOU HIRE A BUILDER FOR PART OF IT — ARTICLE 36-A", 2.0)
flow.append(k.body(
    "General Business Law Article 36-A is New York's home-improvement "
    "contract law, and unlike most states' it reaches a new house: “home "
    "improvement” “shall also mean <b>the construction of a custom home</b>” "
    f"({sec('770(3)')}), and a custom home is “a new single family residence "
    "to be constructed on premises owned of record by the purchaser at the "
    "time of contract, provided that such residence is intended for "
    f"residential occupancy by such purchaser” ({sec('770(7)')}). A contract "
    f"over <b>$500</b> is covered ({sec('770(4)')}). So an owner who "
    "contracts with a builder to erect the whole house on the owner's lot "
    "is buying a custom home, and the protections attach by statute."))
flow.append(k.callout_long(
    f"What GBL {sec('771')} requires the contract to say", [
        Paragraph("Every such contract “shall be evidenced by a writing” "
                  "containing, among other things: the contractor's name, "
                  "address, telephone and license number if any; the "
                  "approximate start and substantial-completion dates and "
                  "whether completion is of the essence; a description of the "
                  "work and materials and the agreed price; a bold notice that "
                  "an unpaid contractor or subcontractor may file a mechanic's "
                  "lien; a notice that the contractor must deposit all "
                  "payments received before completion in escrow, or post a "
                  "bond, contract of indemnity or irrevocable letter of "
                  "credit; any progress-payment schedule, with amounts "
                  "“bearing a reasonable relationship” to the work performed; "
                  "the owner's right to cancel until midnight of the third "
                  "business day; and the contractor's insurance disclosure. "
                  "In plain English, with a signed copy to the owner before "
                  f"work begins ({sec('771(2)')}).", S["body"]),
        Paragraph("<b>The escrow is real.</b> Lien Law " + sec("71-a(4)") +
                  ": payments received by a home improvement contractor "
                  "“prior to the substantial completion of work … shall be "
                  "deposited within five business days … in an escrow "
                  "account,” unless the contractor posts “a bond or contract "
                  "of indemnity … or an irrevocable letter of credit.” A "
                  "builder who takes your deposit into operating funds is "
                  "breaking this section.", S["body"]),
    ]))
flow.append(k.cite(
    "<b>What this kit does not claim:</b> that Article 36-A reaches a framing "
    "crew or an electrician you hire directly to build new — §&#160;770(3)'s "
    "core definition is “repair, replacement, remodeling … of residential "
    "property,” and new construction by trade is not squarely inside it. Use "
    "the §&#160;771 list as the benchmark for every trade contract anyway. "
    "Several counties license home-improvement contractors and most of those "
    "laws exclude a new home; Westchester's does not — NY.4."))

# ---------------------------------------------------------------- record
flow += k.h2_tight("PERMIT RECORD — FILL THIS IN AS EACH ONE ISSUES", 1.6)
flow += k.check_table(
    "Every approval on this build", [
        ("<b>Form CE-200</b> (or carrier forms C-105.2 / DB-120.1) filed "
         "with the application:", [("CE-200 number", 0.6), ("Date", 0.4)]),
        ("<b>Building permit</b> — rung, number, fee paid, expiration date "
         "and the deadline to commence if the local law sets one:",
         [("Rung", 0.2), ("Number", 0.3), ("Fee", 0.2), ("Expires", 0.3)]),
        ("<b>Stamped plans</b> — architect or engineer, registration number "
         "and expiration:", [("Professional", 0.6), ("Reg. exp.", 0.4)]),
        ("<b>Septic</b> — design professional's plan approved by the county "
         "health department or DOH district office:",
         [("Approval", 0.5), ("Date", 0.5)]),
        ("<b>Well</b> — DEC-registered driller, registration number, and "
         "completion report received:",
         [("Driller reg.", 0.5), ("Report date", 0.5)]),
        ("<b>Electrical agency</b> engaged and named on the statement of "
         "special inspections:", [("Agency", 1.0)]),
        ("<b>Zoning / site plan approval</b>, if separate, and the "
         "<b>driveway permit</b> from whichever road authority:",
         [("Zoning ref.", 0.5), ("Driveway", 0.5)]),
        ("<b>Floodplain determination</b> — zone (including shaded X):",
         [("Zone", 0.4), ("Who confirmed", 0.6)]),
        ("<b>Adirondack Park Agency permit</b> or <b>NYC DEP watershed "
         "approval</b>, if the parcel is inside either:",
         [("Which", 0.4), ("Reference", 0.6)]),
        ("<b>Certificate of occupancy</b> — and the solid-fuel certificate "
         "of compliance, if any:",
         [("CO number", 0.35), ("Date", 0.3), ("Solid-fuel cert.", 0.35)]),
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ny-permit-kit",
                       "NY.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
