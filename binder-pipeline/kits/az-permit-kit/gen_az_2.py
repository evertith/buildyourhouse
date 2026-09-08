#!/usr/bin/env python3
"""AZ.2 Permit Application Checklist.

Every Arizona claim in this document was read against its primary source in
September 2026 and is cited on-page.

The organizing idea: nothing about the building code is statewide, so the
document prints the edition map as each jurisdiction's own site or ordinance
stated it on 3 September 2026, dated, with a confirm-at-the-counter rule for
every cell that could not be closed on a primary source — and then prints the
two rulebooks that ARE statewide and reach every lot: the ADEQ septic general
permit and the ADWR well rules, with the numbers that decide where the house
can sit.

Verified sources:
  § 9-802; § 11-864     the adopting ordinance is the edition authority
  § 11-861(C)(1)        a county may adopt its largest city's code (Yuma)
  County and city adopting ordinances and code pages, 15 counties and 20
                        cities, read 3 September 2026 (the two tables)
  Phoenix building-code page   HVAC-GFCI enforcement deferred to 1 Mar 2027
  § 34-451              the state energy standard reaches public buildings only
  § 28-8482(B)          military-airport R-18 wall / R-30 roof (a noise rule)
  § 9-807; § 11-861(E)  no residential sprinkler mandate
  § 9-808(A), (D); § 11-861(G)   access roads may not back-door sprinklers
  § 36-1681(A)–(E)      pool barrier
  § 45-312; § 45-314(B) plumbing fixtures; labels stay on until inspected
  § 9-467(B)–(F); § 11-321(B)–(E), (H)   utility choice; no business-license
                        condition; prior owner's unpermitted work
  § 9-468; § 11-323     solar permit limits
  § 33-439              solar covenants void
  § 9-806; § 11-861(D)  WUI code optional
  § 11-865(A)(1)        farming exemption — construction INCIDENTAL to farming
  § 32-1169(A)          the statement; licensed subs named at application
  § 9-836(A); § 11-1606; § 9-834(H); § 11-1604(H); § 9-839; § 11-1609
                        the counter handout; the 30-day clarification
  § 49-241(A), (B)(9); § 49-107(A); § 49-245(D)   septic general permit and
                        delegation
  A.A.C. R18-9-A301(D); A309(A)(5), (C); A310(C)(2), (D)(2), (E)(1), (F)(1)(a),
    (H); A312(C) Table 1, (D)(1), (D)(2)(a), (D)(4)(a), (E)(1); A314(A)(4)(a);
    E302(C)(1)(h)       the septic rulebook (LII text current to 29 A.A.R. 1023,
                        eff. 19 Jun 2023, cross-checked against the Secretary
                        of State's Supp. 17-4 compilation and La Paz County's
                        posted setback table)
  ADEQ form DWS 402 (rev. April 2025, as posted by La Paz County)   ADEQ's
                        own R18-1-525 time frames: 42 + 31 = 73 business days
  La Paz County "Well-Property Line 50ft Setback Waiver"   recorded within
                        30 days or void
  § 45-454(B), (C), (D), (G), (I); § 45-595(A), (D); § 45-596(A), (D)–(G), (L);
  § 45-600; § 45-593(D) wells
  A.A.C. R12-15-801(25), 803(B), 807, 809, 810(A), 811(A)(1), (B)(1), (C),
    816, 818, 821       well construction

DELIBERATELY NOT CLAIMED, and why:
  - Any IECC climate zone or R-value as an Arizona requirement. No statewide
    energy code exists; five counties have none and Maricopa's is voluntary.
  - Any permit, plan-review, impact or tap fee. No state schedule; "reasonable
    fees" (§ 11-863(C)) is the whole statute.
  - The state fire code edition. dffm.az.gov was unreachable; § 37-1383 was
    read and it excludes dwellings under five units from the provisions that
    matter.
  - Utility pre-energization requirements. Service manuals not fetched.
  - A statewide NEC year. The map carries the year per jurisdiction, dated.
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
aac = k.aac
NB = k.NB
CITE = k.CITE_COL

FORM_ID = "AZ.2"
FORM_TITLE = "Permit Application Checklist"
TOPIC = "What to Gather"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "The code editions actually in force where you are, the rules that bind "
    "every lot regardless, and the septic and well packages that decide "
    "where the house can sit.")

flow.append(k.disclaimer(
    "The edition maps were read from each jurisdiction's own website or "
    "adopting ordinance on 3&#160;September 2026. Where a cell could not be "
    "closed on a primary source it says <b>confirm</b> — and every cell, "
    "verified or not, is confirmed at the counter by asking for the adopting "
    "ordinance number. No fee is printed anywhere in this document, because "
    "no state schedule exists."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- editions
flow += k.h2_tight("THE CODE EDITIONS — LOCAL, DATED, CONFIRMED AT THE COUNTER",
                   reserve=2.2)
flow.append(k.body(
    f"No edition of anything is statewide. A city adopts a code by reference "
    f"in an ordinance that \"shall be published in full\" and filed with the "
    f"clerk ({ars('9-802')}); a county's adopting ordinance is likewise "
    f"published and filed ({sec('11-864')}), and a county may simply adopt "
    f"\"the largest city in that county\"'s code, tracking its changes within "
    f"ninety days ({sec('11-861(C)(1)')}) — Yuma County does. <b>The "
    f"ordinance is the authority, the web page is a summary of it</b>, and "
    f"the September 2026 spread runs from the 2003 IRC to the 2024. Read your "
    f"row, then ask the counter for the ordinance number and write it on the "
    f"record at the end."))

C = k.cellp
rows = [
    [C("<b>Maricopa</b>"), C("2018"), C("2017"),
     C("2018 IECC <b>voluntary</b>: Chapter 11 or IECC compliance \"is "
       "optional unless specifically required through ordinance by "
       "Maricopa County\""),
     C("Local Additions &amp; Addenda TA2022001; Board 17&#160;Aug 2022, "
       "effective 30 days later")],
    [C("<b>Pima</b>"), C("2024"), C("2023"),
     C("IECC per Ord. 2018-30 Ex. G; a 2024 IECC amendment set (Ord. 2026-6) "
       "is posted — <b>confirm</b> its effective date"),
     C("Ord. 2025-15, effective 1&#160;Jan 2026")],
    [C("<b>Pinal</b>"), C("2018"), C("2017"), C("2018 IECC"),
     C("Ord. 121819-BCO (hearing 18&#160;Dec 2019); PCDSC 6.05.030")],
    [C("<b>Yavapai</b>"), C("2024 (2018 before 1&#160;Jan 2026)"), C("2023"),
     C("<b>2012 IECC</b> retained (Ord. 2025-13)"),
     C("Ords. 2025-3 to 2025-13, Oct 2025, effective 1&#160;Jan 2026")],
    [C("<b>Mohave</b>"), C("2018"), C("2017"),
     C("2018 via IRC Ch. 11: \"The Residential Provisions of the IECC are not "
       "adopted\""),
     C("Ord. 2021-03, adopted 7&#160;Jun 2021, effective 30 days after; "
       "revised through 15&#160;Jul 2024")],
    [C("<b>Cochise</b>"), C("2024 from 1&#160;Sep 2026 (2015 before)"),
     C("2023 (2014 before)"), C("<b>2012 IECC</b> continued"),
     C("Resolution 26-23 (July 2026), replacing Res. 21-15 (eff. 26&#160;Aug "
       "2021). Owner-Builder Amendment: AZ.1")],
    [C("<b>Coconino</b>"), C("2024 (2018 plans accepted through 31&#160;Dec "
                             "2026)"), C("2023"), C("2018 IECC (not 2024)"),
     C("Ordinance 2026-03, effective 2&#160;Jun 2026. AMMP: AZ.1")],
    [C("<b>Navajo</b>"), C("2018"), C("2017 (by reference in the addenda)"),
     C("None listed"),
     C("Resolution 9-2022, adopted 22&#160;Mar 2022, effective 22&#160;Jun "
       "2022")],
    [C("<b>Apache</b>"), C("2015"), C("2011"), C("<b>Confirm</b>"),
     C("Read from an archived copy (March 2025) of the county's own FAQ; the "
       "county site was unreachable. <b>Confirm every cell</b>")],
    [C("<b>Gila</b>"), C("2012"), C("2011"),
     C("County R-value table in ordinance §&#160;103; IRC Ch. 11 \"is "
       "optional and not required\""),
     C("Ord. 2017-02, passed 11&#160;Jul 2017, effective 30 days after")],
    [C("<b>Graham</b>"), C("<b>2003</b>"),
     C("2002 (§&#160;5.14.2) or 1999 (§&#160;5.14.9) — the county's own "
       "ordinance is inconsistent; <b>confirm</b>"),
     C("2003 IECC \"for Graham County Government Buildings only\""),
     C("P&amp;Z Ordinance §&#160;5.14; date not verified. County FAQ: "
       "\"'dirt work' does not require a permit, everything else does\"")],
    [C("<b>Greenlee</b>"), C("<b>None</b>"), C("None"), C("None"),
     C("No code adopted — County Engineer letter, 19&#160;Oct 2012, still "
       "posted. The permit still issues (AZ.1)")],
    [C("<b>La Paz</b>"), C("2018"), C("<b>2020</b>"),
     C("Not in the adopted list"),
     C("Ord. 2026-01, adopted 6&#160;Jul 2026, effective 6&#160;Aug 2026")],
    [C("<b>Santa Cruz</b>"), C("2012"), C("2011"), C("None listed"),
     C("Ord. 2013-03, passed 17&#160;Jul 2013, effective 1&#160;Sep 2013 — "
       "read from an archived copy (May 2026) of the county page; "
       "<b>confirm</b>")],
    [C("<b>Yuma</b>"), C("2024 (adopts the City of Yuma's code under "
                         "§&#160;11-861(C)(1))"),
     C("2020 amendments posted; <b>confirm</b> whether 2023 came in with the "
       "city's 2025 adoption"),
     C("2009 IECC amendments posted"),
     C("Ord. 2026-01, approved 19&#160;Feb 2026, effective 23&#160;Mar 2026")],
]
# Column plan (CW = 504pt): county 0.85in, IRC 0.95in, NEC 0.95in, energy
# 1.75in, instrument = remainder (~2.5in). The NEC column has to hold "2023
# (2014 before)" without a mid-token split; 0.95in does at 9.5pt.
flow.append(k.ref_table(
    "Unincorporated areas — the 15 counties, as their own sites and "
    "ordinances stated it on 3 September 2026",
    [C("County", bold=True), C("IRC", bold=True), C("NEC", bold=True),
     C("Energy", bold=True), C("Adopting instrument, effective", bold=True)],
    rows, [0.85 * inch, 0.95 * inch, 0.95 * inch, 1.75 * inch,
           CW - 4.5 * inch]))
flow.append(k.cite(
    "Five counties have no residential energy code at all or make it "
    "optional. The electrical spread — from the 1999/2002 NEC in Graham "
    "County to the 2023 — is the widest of any state in this kit line, and it "
    "is the reason this kit never prints an NEC year as an Arizona rule."))

rows = [
    [C("<b>Phoenix</b>"), C("2024 (Phoenix Building Construction Code)"),
     C("2023 — enforcement of 210.8(F) Exc. 2 (HVAC GFCI) <b>deferred to "
       "1&#160;Mar 2027</b>"), C("2024 IECC"),
     C("Ord. G-7397; Council 18&#160;Jun 2025; effective 1&#160;Aug 2025; "
       "2018 code allowed for complete plans through 31&#160;Dec 2025")],
    [C("<b>Tucson</b>"), C("2024 (eff. 1&#160;Jan 2026)"),
     C("2023 (eff. 1&#160;Jan 2026)"), C("2024 IECC (eff. 1&#160;Jul 2026)"),
     C("Amendments under Ord. 12171; Mayor &amp; Council 3&#160;Jun 2025 and "
       "16&#160;Dec 2025")],
    [C("<b>Mesa</b>"), C("2024"), C("2023"), C("2024 IECC + App. RE"),
     C("Ords. 5981/5982/5987, passed 8&#160;Dec 2025, effective 8&#160;Jan "
       "2026 (read from the ordinances; city page unreachable)")],
    [C("<b>Scottsdale</b>"), C("<b>2021</b>"), C("2020"),
     C("2021 IECC + 2021 IgCC mandatory"),
     C("Ord. 4550 (20&#160;Sep 2022, effective January 2023); Ord. 4576 "
       "(IECC)")],
    [C("<b>Chandler</b>"), C("2024"), C("2023"), C("2024 IECC"),
     C("Ord. 5108; plans on or after 1&#160;Jul 2025")],
    [C("<b>Gilbert</b>"), C("2018 (App. H, P, Q)"), C("2017"), C("2018 IECC"),
     C("Ord. 2739; Ord. 2788 (IRC amendments)")],
    [C("<b>Glendale</b>"), C("2024"), C("2023"), C("2024 IECC"),
     C("Ord. O25-51, passed 9&#160;Dec 2025, effective 9&#160;Jan 2026")],
    [C("<b>Tempe</b>"), C("2024 (eff. 1&#160;Jul 2026; 2018 allowed through "
                          "31&#160;Dec 2026)"),
     C("2023 (2017 allowed through 31&#160;Dec 2026)"), C("2024 IECC"),
     C("2024 ordinance number not verified — <b>confirm</b>")],
    [C("<b>Peoria</b>"), C("2018"), C("2017"), C("2018 IECC"),
     C("Ord. 2019-12; date not verified — <b>confirm</b>")],
    [C("<b>Flagstaff</b>"), C("2018"), C("2017"), C("2018 IECC"),
     C("Res. 2019-26 / Ord. 2019-16, adopted 18&#160;Jun 2019, effective "
       "19&#160;Jul 2019; \"2024 Codes … being evaluated\"")],
    [C("<b>Prescott</b>"), C("2024 (App. BF)"), C("2023"),
     C("<b>2012 IECC</b> \"with 2018 Revisions\"; IRC Ch. 11 deleted and "
       "replaced"),
     C("Ord. 2025-1924 / Res. 2025-1958 (IRC), Ord. 2025-1923 (NEC), "
       "18&#160;Nov 2025; IECC Ord. 2019-1669")],
    [C("<b>Yuma</b>"), C("2024"), C("2020"),
     C("2009 IECC amendments (Ord. O2013-15)"),
     C("Effective 3&#160;Nov 2025; 2024 mandatory from 1&#160;Feb 2026; "
       "ordinance number not verified — <b>confirm</b>")],
    [C("<b>Sierra Vista</b>"), C("2018"), C("2017"),
     C("<b>2006 IECC</b> residential; 2012 commercial"),
     C("Resolution 2023-043 (amendments); adopting ordinance not verified — "
       "<b>confirm</b>")],
    [C("<b>Lake Havasu City</b>"), C("2024"), C("2023"),
     C("None listed among adopted codes — <b>confirm</b>"),
     C("Ord. 25-1370; effective 1&#160;Feb 2026; 2018-designed projects "
       "accepted to 1&#160;May 2026")],
    [C("<b>Kingman</b>"), C("2018"), C("2017"),
     C("2018 IECC with residential provisions R101.1–R406.6.5 <b>not "
       "adopted</b>; IRC Ch. 11 amended"),
     C("Ord. 1916 §&#160;4, 15&#160;Dec 2020")],
    [C("<b>Surprise</b>"), C("2024"), C("2023"), C("2024 IECC"),
     C("Ord. 2025-14, passed 2&#160;Dec 2025; amendments dated 1&#160;Jan "
       "2026")],
    [C("<b>Goodyear</b>"), C("2024"), C("2023"), C("2024 IECC"),
     C("Council 23&#160;Mar 2026; building codes effective 23&#160;Jun 2026")],
    [C("<b>Buckeye</b>"), C("2024"), C("2023"), C("<b>2018 IECC</b>"),
     C("Projects submitted on or after 1&#160;Jan 2025; Ord. 20-24 not "
       "directly read — <b>confirm</b>")],
    [C("<b>Queen Creek</b>"), C("2021"), C("2020"), C("2021 IECC"),
     C("Ord. 797-22; effective 1&#160;Jan 2023")],
    [C("<b>Casa Grande</b>"), C("2018"), C("2017"), C("2018 IECC"),
     C("2019 Building &amp; Technical Administrative Code, effective "
       "1&#160;Jul 2019")],
]
flow.append(k.ref_table(
    "Inside city limits — 20 cities and towns, as their own sites and "
    "ordinances stated it on 3 September 2026",
    [C("City", bold=True), C("IRC", bold=True), C("NEC", bold=True),
     C("Energy", bold=True), C("Adopting instrument, effective", bold=True)],
    rows, [0.95 * inch, 1.05 * inch, 1.05 * inch, 1.5 * inch,
           CW - 4.55 * inch]))
flow.append(k.cite(
    "<b>Transition rules are local too.</b> There is no state rule for which "
    "edition a plan in the pipeline gets. Phoenix honored 2018 plans "
    "\"submitted through December 31, 2025\"; Tempe accepts either set "
    "\"through December 31, 2026\"; Coconino County accepts 2018 plans "
    "\"through 12/31/26\"; Lake Havasu City accepted 2018-designed projects "
    "\"up to 90 days (May 1, 2026) after the effective date.\" <b>Get the "
    "grace-period sentence from your ordinance in writing before you choose "
    "an edition to design to</b> — and if you are in Phoenix wiring to the "
    "2023 NEC, the city is \"deferring enforcement\" of the HVAC-equipment "
    "GFCI rule: \"Full enforcement of the GFCI requirement for HVAC equipment "
    "will now take effect on March 1st, 2027.\""))

# ---------------------------------------------------------------- energy
flow += k.h2_tight("ENERGY — NO STATE CODE, AND DO NOT PRINT ANYONE'S R-VALUES",
                   reserve=2.0)
flow.append(k.body(
    f"The only state energy statute directs the governor's energy office to "
    f"adopt standards \"for construction of all new capital projects as "
    f"defined in section 41-790, including buildings designed and constructed "
    f"by school districts, community college districts and universities\" "
    f"({ars('34-451')}) — public buildings. A house answers to whatever its "
    f"jurisdiction adopted, which in the tables above runs from the 2024 IECC "
    f"(Phoenix, Tucson, Mesa, Chandler, Glendale, Tempe, Surprise, Goodyear) "
    f"through 2021, 2018, 2012 (Prescott, Yavapai, Cochise), 2009 (Yuma) and "
    f"2006 (Sierra Vista) to a county R-value table (Gila), a voluntary "
    f"chapter (Maricopa County — the largest unincorporated population in "
    f"the state has no mandatory residential energy code) and none at all "
    f"(Navajo, Santa Cruz, La Paz, Greenlee). <b>Any guide that prints a "
    f"\"typical Zone 2B\" insulation table as an Arizona requirement is "
    f"printing the model code, not Arizona.</b> Ask the counter for the "
    f"energy chapter your ordinance adopted, by section, and design to that."))
flow.append(k.cite(
    f"<b>The one statewide envelope number that exists is a noise rule.</b> "
    f"In \"territory in the vicinity of a military airport or ancillary "
    f"military facility,\" residential buildings outside the noise contours "
    f"must have \"a minimum of R18 exterior wall assembly, a minimum of R30 "
    f"roof and ceiling assembly, dual-glazed windows and solid wood, "
    f"foam-filled fiberglass or metal doors,\" or an architect's or engineer's "
    f"certification of a 45&#160;dB maximum interior level "
    f"({ars('28-8482(B)')}). The Cochise Owner-Builder Amendment repeats it "
    f"(Sec. 4(B)). If Luke, Davis-Monthan, Yuma or a Guard facility is near, "
    f"ask the planning office whether the parcel is in the mapped territory."))

# ---------------------------------------------------------------- statewide rules
flow += k.h2_tight("WHAT APPLIES ON EVERY LOT, WHATEVER YOUR CODE — OR NONE",
                   reserve=2.4)
flow.append(k.body(
    "Everything in this table is state statute. It applies in Greenlee County "
    "and under a Cochise Option 2 permit exactly as it applies in Scottsdale, "
    "and no city or county may adopt around it."))
rows = [
    [C("<b>Sprinklers cannot be mandated</b>"),
     C("A city or county \"shall not adopt a code or ordinance … that "
       "prohibits a person or entity from choosing to install or equip or "
       "not install or equip fire sprinklers in a single family detached "
       "residence or any residential building that contains not more than "
       "two dwelling units\"; the only exception is an ordinance \"adopted "
       "before December 31, 2009.\" The text must appear on every "
       "residential sprinkler permit application"),
     C(f"{ars('9-807')}; {sec('11-861(E)')}")],
    [C("<b>— and access roads cannot back-door them</b>"),
     C("No fire-code access-road or approved-route requirement \"that "
       "directly or indirectly requires a one or two family residence … to "
       "install fire sprinklers\"; enforceable by private civil action with "
       "attorney fees, damages \"and the cost of the sprinkler system\""),
     C(f"{ars('9-808(A)')}, (D); {sec('11-861(G)')}")],
    [C("<b>Pool barrier</b>"),
     C("Any pool \"eighteen inches or more in depth … wider than eight feet "
       "… intended for swimming\": a barrier at least <b>5&#160;ft</b> high, "
       "no opening a <b>4-inch</b> sphere passes, self-closing self-latching "
       "gates opening outward with the latch <b>54&#160;in</b> or more above "
       "grade, at least <b>20&#160;in</b> from the water's edge. Where the "
       "house is part of the enclosure: a 4-ft interior barrier, a keyed "
       "motorized cover, or self-latching doors plus latched or screened "
       "windows. Exception: \"A residence in which all residents are at "
       "least six years of age\""),
     C(f"{ars('36-1681(A)')}–(D)")],
    [C("<b>Plumbing fixtures</b>"),
     C("No plumbing fixture may be installed \"in any new residential "
       "construction\" unless lavatory and kitchen faucets and showerheads "
       "flow at most 3&#160;gpm at 80&#160;psi, water closets at most "
       "1.6&#160;gal per flush, urinals 1&#160;gal, and evaporative coolers "
       "and decorative fountains recycle. Where a permit is required, "
       "compliance labels \"shall not be removed from the fixtures … until "
       "the fixtures have been installed and inspected\""),
     C(f"{ars('45-312')}; {sec('45-314(B)')}")],
    [C("<b>Utility choice</b>"),
     C("A permit may not be denied \"based on the utility provider "
       "proposed,\" fees may not be structured to restrict the choice, and "
       "\"utility service\" means \"water, wastewater, natural gas, "
       "including propane gas, or electric service\""),
     C(f"{ars('9-467(B)')}–(D), (I)(2); {sec('11-321(B)')}–(D), (K); "
       f"{sec('9-810')}")],
    [C("<b>No business license as a condition</b>"),
     C("A city or county \"may not require an applicant for a building "
       "permit to hold a transaction privilege tax license or business "
       "license as a condition for issuing the building permit\""),
     C(f"{ars('9-467(E)')}; {sec('11-321(E)')}")],
    [C("<b>The prior owner's unpermitted work</b>"),
     C("A subsequent owner cannot be made to permit \"the construction or "
       "addition done by the prior owner before issuing a permit for a "
       "building addition,\" except to enforce a provision \"that affects "
       "the public health or safety\""),
     C(f"{ars('9-467(F)')}; {sec('11-321(H)')}")],
    [C("<b>Solar</b>"),
     C("The permit \"shall not require a stamp from a professional engineer "
       "… unless an engineering stamp is deemed necessary,\" and then only "
       "with \"a written explanation\"; the fee \"shall not exceed the "
       "actual cost of issuing a permit,\" itemized on request. Any deed or "
       "CC&amp;R provision that \"effectively prohibits the installation or "
       "use of a solar energy device … is void and unenforceable\""),
     C(f"{ars('9-468')}; {sec('11-323')}; {sec('33-439')}")],
    [C("<b>Refrigerants; wildland-urban interface</b>"),
     C("No local code \"may prohibit the use of refrigerants that are "
       "listed as acceptable pursuant to the clean air act.\" A city or "
       "county \"may adopt a current wildland-urban interface code\" — "
       "optional, so no statewide defensible-space distance exists"),
     C(f"{ars('9-810.01')}; {sec('11-861(J)')}; {sec('9-806')}; "
       f"{sec('11-861(D)')}")],
    [C("<b>Farming — not a house</b>"),
     C("The county code article \"does not apply to\" construction "
       "\"incidental to\" \"farming, dairying, agriculture, viticulture, "
       "horticulture or stock or poultry raising.\" Nothing in it says a "
       "dwelling is incidental to farming; this kit prints no agricultural "
       "route for a house. Get the county's position in writing under "
       "§&#160;11-1609 if a barn and a house share the parcel"),
     C(ars("11-865(A)(1)"))],
]
flow.append(k.ref_table(
    "Statewide by statute — binding in a no-code county and under an opt-out",
    [C("Subject", bold=True), C("The rule", bold=True), C("Cite", bold=True)],
    rows, [1.45 * inch, CW - 1.45 * inch - CITE, CITE]))

# ---------------------------------------------------------------- before you apply
flow += k.h2_tight("BEFORE YOU APPLY — THE STATEMENT AND THE HANDOUT",
                   reserve=2.4)
flow.append(k.body(
    f"Two things are fixed by statute about the application itself, in every "
    f"jurisdiction. First, the §&#160;32-1169 statement (AZ.1): you will sign "
    f"that you claim the §&#160;32-1121(A)(5) exemption and name \"any "
    f"general, mechanical, electrical or plumbing contractor who will be "
    f"employed on the work\" with license numbers ({ars('32-1169(A)')}). "
    f"That means the licensed-sub list is assembled <i>before</i> the "
    f"application, not after. Second, the counter owes you a handout:"))
rows = [
    [C("<b>At the time you obtain an application</b>"),
     C("\"1. A list of all of the steps the applicant is required to take "
       "in order to obtain the license. 2. The applicable licensing time "
       "frames. 3. The name and telephone number of a … contact person … "
       "4. The website address … 5. Notice that an applicant may receive a "
       "clarification\" — \"license\" includes a permit"),
     C(f"{ars('9-836(A)')}; {sec('11-1606')}")],
    [C("<b>Printed on the application</b>"),
     C("A city or county \"shall not base a licensing decision in whole or "
       "in part on a licensing requirement or condition that is not "
       "specifically authorized by statute, rule, ordinance or code,\" and "
       "must \"prominently print\" that section on every application"),
     C(f"{ars('9-834(A)')}, (H); {sec('11-1604(A)')}, (H)")],
    [C("<b>The 30-day clarification letter</b>"),
     C("A written request stating your name and address, the provision "
       "needing clarification, the relevant facts, \"the applicant's "
       "proposed interpretation,\" and whether the issue is pending on an "
       "existing application; the city or county \"shall respond within "
       "thirty days … with a written explanation of its interpretation or "
       "application.\" <b>This is the universal tool for every \"varies "
       "locally\" question in this kit.</b> AZ.5 has the template"),
     C(f"{ars('9-839')}; {sec('11-1609')}")],
]
flow.append(k.ref_table(
    "What the counter owes you, city or county",
    [C("", bold=True), C("The statute", bold=True), C("Cite", bold=True)],
    rows, [1.55 * inch, CW - 1.55 * inch - CITE, CITE]))
flow.append(k.cite(
    "The permit record at the end of this document has a line for each of "
    "these — the ordinance number and editions, the statement and whether "
    "the Registrar's signature was wanted, the handout and its date."))

# ---------------------------------------------------------------- septic
flow += k.h2_tight("THE SEPTIC PACKAGE — ADEQ'S GENERAL PERMIT, RUN BY YOUR "
                   "COUNTY", reserve=2.4)
flow.append(k.body(
    f"\"Sewage treatment facilities, including on-site wastewater treatment "
    f"facilities\" are discharging facilities that \"shall be operated "
    f"pursuant to either an individual permit or a general permit\" — the "
    f"Aquifer Protection Permit ({ars('49-241(A)')}, (B)(9)). ADEQ \"may "
    f"delegate to a local environmental agency, county health department, "
    f"public health services district or municipality any functions, powers "
    f"or duties\" ({sec('49-107(A)')}), and has, county by county (the "
    f"office in each is in AZ.4). The rulebook is 18&#160;A.A.C. 9, "
    f"Article 3, and it is the same everywhere. Every number below is a "
    f"regulatory minimum "
    f"the county may raise \"on a site- or area-specific basis\" "
    f"({aac('R18-9-A312(C)(3)')}) — and every setback is measured to the "
    f"facility \"Including Reserve Area.\""))
rows = [
    [C("<b>1</b>", center=True), C("<b>Site investigation</b>"),
     C("Only \"an Arizona-registered professional engineer,\" geologist or "
       "sanitarian, or a holder of \"a certificate of training from a "
       "course recognized by the Department\" may do it (A310(H)). <b>You "
       "cannot self-certify the perc test.</b> Two test locations in the "
       "primary area, one in the reserve (A310(E)(1), (F)(1)(a)). A slope "
       "\"greater than 15 percent,\" a 100-year flood zone that may affect "
       "function, rock, fill, or a subsurface limit within 12&#160;ft is a "
       "\"limiting condition\" that pushes the design off the standard "
       "system (A310(C)(2), (D)(2))")],
    [C("<b>2</b>", center=True), C("<b>Notice of Intent to Discharge</b>"),
     C("ADEQ form DWS 402 (rev. April 2025), filed with the delegated county. "
       "It carries ADEQ's own posted clocks under R18-1-525: a single 4.02 "
       "general permit is <b>42 business days administrative + 31 "
       "substantive = 73 overall</b>; each R18-9-A312(G) alternative request "
       "\"adds eight business days\"; and \"Review fees established by "
       "delegated counties or cities may differ.\" Those are ADEQ's clocks. "
       "A delegated county's clock is the county's — AZ.3")],
    [C("<b>3</b>", center=True), C("<b>Construction Authorization</b>"),
     C("\"A person shall not begin facility construction until the Director "
       "issues a Construction Authorization\"; \"A person shall complete "
       "construction within <b>two years</b> of receiving a Construction "
       "Authorization,\" or the notice expires and \"the person shall not "
       "continue construction or discharge\" (A301(D))")],
    [C("<b>4</b>", center=True), C("<b>Who installs</b>"),
     C("<b>Conventional</b> (everything under R18-9-E302): the Discharge "
       "Authorization issues on an accurate site plan and a certification "
       "that the tank \"passed the watertightness test\" — <b>no installer "
       "license number is required</b> (A309(C)(1)), so an owner who may "
       "do the work \"themselves\" under §&#160;32-1121(A)(5) may install it, "
       "subject to the county's inspection before backfill. "
       "<b>Alternative</b> (E303 to E323): requires \"The name of the "
       "installation contractor and the Registrar of Contractor's license "
       "number\" and a Certificate of Completion from the designer of "
       "record, who must verify installation before backfill (A309(C)(2))")],
    [C("<b>5</b>", center=True), C("<b>Discharge Authorization</b>"),
     C("After construction you submit the Request for Discharge "
       "Authorization; the agency \"may inspect the facility before "
       "issuing.\" Changes during construction that still conform need no "
       "re-approval but must be recorded on the site plan (A301(D)(1)(e)). "
       "Nothing may be paved over a disposal works (E302(C)(1)(h))")],
]
flow.append(k.ref_table(
    "18 A.A.C. 9, Article 3 — the sequence",
    [C("", bold=True, center=True), C("Step", bold=True),
     C("What the rule says", bold=True)],
    rows, [0.35 * inch, 1.5 * inch, CW - 1.85 * inch]))

rows = [
    [C("<b>Building</b> — \"Includes porches, decks (including pool decks), "
       "and steps … breezeways, roofed patios, carports, covered walks\""),
     C("<b>10</b>", center=True), C("Row 1")],
    [C("<b>Property line shared with a lot not served by a common drinking "
       "water system or an existing well</b> — reducible \"to a minimum of "
       "5 feet\" if the neighbor agrees \"as evidenced by an appropriately "
       "recorded document\" to keep any new well 100&#160;ft from your "
       "works, and the Department approves"),
     C("<b>50</b>", center=True), C("Row 2")],
    [C("All other property lines"), C("5", center=True), C("Row 3")],
    [C("<b>Public or private water supply well</b>"),
     C("<b>100</b>", center=True), C("Row 4")],
    [C("Perennial or intermittent stream; lake, reservoir or canal — from "
       "the high water line of the 10-year, 24-hour event"),
     C("100", center=True), C("Rows 5, 6")],
    [C("<b>Wash or drainage easement with a drainage area over "
       "20&#160;acres</b> — from the channel bank; reducible to 25&#160;ft "
       "with floodplain-administrator-approved erosion protection"),
     C("<b>50</b>", center=True), C("Row 8")],
    [C("Water main; domestic service line (crossing allowed at 45–90° with "
       "1&#160;ft vertical separation)"),
     C("10; 5", center=True), C("Rows 9, 10")],
    [C("Downslope or cut bank over 15%, culvert, ditch — from a trench or "
       "bed with no limiting condition; with one"),
     C("20; 50", center=True), C("Row 11b")],
    [C("Driveway (a reinforced tank may sit under one, \"except for "
       "disposal works\"); swimming pool excavation; easement other than "
       "drainage"),
     C("5", center=True), C("Rows 12–14")],
    [C("<b>Earth fissures</b>"), C("<b>100</b>", center=True), C("Row 15")],
]
flow.append(k.ref_table(
    f"Setbacks in feet — {aac('R18-9-A312(C)')}, Table 1, measured to the "
    f"facility including the reserve area",
    [C("From", bold=True), C("Feet", bold=True, center=True),
     C("Table row", bold=True)],
    rows, [CW - 0.8 * inch - 1.0 * inch, 0.8 * inch, 1.0 * inch]))
flow.append(k.cite(
    "<b>The two numbers that decide small lots.</b> 100&#160;ft from any well "
    "— stated from both sides, because ADWR's rule independently forbids "
    "drilling a well \"within 100 feet of any septic tank system, sewage "
    "disposal area\" unless the ADWR Director authorizes it in writing "
    f"({aac('R12-15-818')}) — and the 50-ft line on a well-served lot, which "
    "is the one that breaks a rural parcel. La Paz County's own \"Well-Property "
    "Line 50ft Setback Waiver\" shows the practice: both owners sign, "
    "notarized, \"record this document to deed … within 30 days, or the "
    "waiver is null and void.\" A \"common drinking water system\" is one "
    "that \"currently serves or is under legal obligation to serve the "
    "property.\""))

rows = [
    [C("1"), C("≤ 7 / &gt; 7", center=True), C("1,000 / 1,000", center=True),
     C("150 / 300", center=True)],
    [C("2"), C("≤ 14 / &gt; 14", center=True), C("1,000 / 1,000", center=True),
     C("300 / 450", center=True)],
    [C("3"), C("≤ 21 / &gt; 21", center=True),
     C("<b>1,000 / 1,250</b>", center=True), C("450 / 600", center=True)],
    [C("4"), C("≤ 28 / &gt; 28", center=True), C("1,250 / 1,500", center=True),
     C("600 / 750", center=True)],
    [C("5"), C("≤ 35 / &gt; 35", center=True), C("1,500 / 2,000", center=True),
     C("750 / 900", center=True)],
    [C("6"), C("≤ 42 / &gt; 42", center=True), C("2,000 / 2,500", center=True),
     C("900 / 1,050", center=True)],
]
flow.append(k.ref_table(
    f"Tank size and design flow by bedrooms AND fixture count — "
    f"{aac('R18-9-A314(A)(4)(a)')}",
    [C("Bedrooms", bold=True), C("Fixture units", bold=True, center=True),
     C("Minimum tank, gal", bold=True, center=True),
     C("Design flow, gpd", bold=True, center=True)],
    rows, [1.2 * inch, (CW - 1.2 * inch) / 3, (CW - 1.2 * inch) / 3,
           (CW - 1.2 * inch) / 3]))
flow.append(k.cite(
    "Fixture units (A314(A)(4)(a)(ii)): water closet <b>3</b>; bathtub, bidet, "
    "clothes washer, dishwasher, kitchen sink, utility tub <b>2</b> each; "
    "service sink 3; single lavatory or bar sink 1. A three-bedroom house "
    "with two full baths, kitchen, laundry and a utility sink is already at "
    "the 21-unit line — <b>the fixture count, not the bedroom count, decides "
    "whether the tank is 1,000 or 1,250 gallons.</b> Tank: two compartments, "
    "liquid depth at least 42&#160;in, two 20-in access openings with risers "
    "to within 6&#160;in of grade (A314(A)(1)). <b>Absorption area</b> = "
    "design flow ÷ soil absorption rate (A312(D)(1)); the rate comes from the "
    "percolation test — at 10&#160;min/in, 0.63&#160;gal/day/sq&#160;ft for a "
    "trench — so a 450-gpd house at that rate needs about 714&#160;sq&#160;ft "
    "of trench, <b>and the same again in reserve</b>: \"a reserve area of 100 "
    "percent of the primary area\" (A312(D)(4)(a)). Vertical separation to "
    "the seasonal high water table: 10&#160;ft at rates from 0.63 to 1.20, "
    "5&#160;ft from 0.20 to 0.63, 60&#160;ft for a seepage pit (A312(E)(1)). "
    "<b>And the sewer test</b>: you \"shall connect to a sewage collection "
    "system if\" a nitrogen-management designation, an ordinance or an "
    "adopted area-wide plan requires it, or a sewer extension is at the "
    "property boundary and the connection fee is not more than $6,000 and "
    "the building sewer not more than $3,000 (A309(A)(5)) — those are the "
    "rule's thresholds, not fees."))

# ---------------------------------------------------------------- well
flow += k.h2_tight("IF YOU ARE ON A WELL — ADWR, AND THE EXAM THAT LETS YOU "
                   "DRILL IT", reserve=1.8)
rows = [
    [C("<b>An exempt well</b>"),
     C(f"Non-irrigation withdrawals \"from wells having a pump with a maximum "
       f"capacity of not more than thirty-five gallons per minute\" are "
       f"exempt from the Groundwater Code except as listed "
       f"({ars('45-454(B)')}). Inside an active management area: one exempt "
       f"well per use per site, a second only if the first cannot produce "
       f"3&#160;gpm on a parcel of at least an acre ((I))")],
    [C("<b>The 100-ft municipal-provider ban</b>"),
     C(f"Since 2006 an exempt well \"may not be drilled on land if any part "
       f"of the land is within one hundred feet of the operating water "
       f"distribution system of a municipal provider with an assured water "
       f"supply designation\" in an AMA established by 1&#160;July 1994 — "
       f"exemptions on request if service is refused within 30 days, costs "
       f"more than the well, or an easement is refused "
       f"({sec('45-454(C)')}, (D)). Ask the water provider in writing first")],
    [C("<b>Notice of intent, before drilling</b>"),
     C(f"\"A person shall file a notice of intention to drill with the "
       f"director … before drilling an exempt well or causing an exempt well "
       f"to be drilled\" ({sec('45-454(G)')}), signed by the owner or lessee "
       f"({aac('R12-15-809')}). Fee <b>$150</b>, or <b>$100</b> for a well "
       f"outside an AMA or irrigation non-expansion area used solely for "
       f"domestic purposes at 35&#160;gpm or less ({sec('45-596(L)')}). "
       f"Within 15 days of a complete notice ADWR mails \"a drilling card "
       f"that authorizes the drilling of the well to the well driller\" "
       f"((D)); drilling starts only with the card \"at the well site\" "
       f"({aac('R12-15-810(A)')}); \"The well shall be completed within one "
       f"year after the date of the notice\" ((E))")],
    [C("<b>Domestic well on five acres or less — the site plan</b>"),
     C(f"The notice must carry \"a well site plan of the property\" showing "
       f"the parcel number, \"the proposed well location and the location "
       f"of any septic tank or sewer system that is either located on the "
       f"property or within one hundred feet of the proposed well site,\" "
       f"and \"written approval by the county health authority that "
       f"controls the installation of septic tanks\" ({ars('45-596(F)')}). "
       f"A variance where \"parcel size, geology or location of "
       f"improvements\" prevent compliance may require a registered "
       f"engineer's or geologist's certification ((G))")],
    [C("<b>Who drills — including you</b>"),
     C(f"\"New well construction … shall be performed under the direct and "
       f"personal supervision of a well driller who holds a well driller's "
       f"license\" ({ars('45-595(A)')}) — <b>or</b> \"A person who drills or "
       f"modifies an exempt well on land owned by that person shall first "
       f"obtain a single well license from the department … <b>No fee may "
       f"be charged for a single well license</b>\" ((D)). The license is an "
       f"exam, not a form: the application lists the rig, the design, the "
       f"helpers and \"whether the applicant will compensate them\"; the "
       f"exam is offered \"no less than six times yearly\"; passing grade "
       f"<b>70 percent</b>; valid one year for \"one exempt well at the "
       f"location specified\" ({aac('R12-15-807')})")],
    [C("<b>Construction</b>"),
     C(f"Steel or thermoplastic casing at least 1&#160;ft above grade; a "
       f"surface seal of steel casing and continuous cement grout, \"The "
       f"minimum length of the steel casing … 20 feet,\" a 1½-in annulus, a "
       f"20-ft seal ({aac('R12-15-811(A)(1)')}, (B)(1)). \"No well shall be "
       f"drilled within 100 feet of any septic tank system, sewage disposal "
       f"area,\" landfill or fuel storage \"unless authorized in writing by "
       f"the Director\" ({aac('R12-15-818')}), who \"may require\" a longer "
       f"seal or more distance ({aac('R12-15-821')})")],
    [C("<b>After</b>"),
     C(f"The driller's report within 30 days of completion; <b>your own</b> "
       f"completion report within 30 days after the pump goes in — "
       f"equipment, the 4-hour tested capacity, drawdown, static level "
       f"({ars('45-600')}). Abandonment only by a licensed driller or single "
       f"well licensee, after a notice and an abandonment card "
       f"({aac('R12-15-816')})")],
]
flow.append(k.ref_table(
    "The well sequence — Title 45 and 12 A.A.C. 15, Article 8",
    [C("", bold=True), C("What the statute and rule require", bold=True)],
    rows, [1.7 * inch, CW - 1.7 * inch]))
flow.append(k.cite(
    "<b>Not in Title 45 or the rule:</b> a well-to-property-line distance. "
    "None exists; the property line is reached only through ADEQ's 50-ft "
    "septic-to-line rule on the neighbor's side. Do not let anyone print one "
    "as state law."))

# ---------------------------------------------------------------- record
flow += k.h2_tight("PERMIT RECORD — FILL THIS IN AS EACH ONE ISSUES",
                   reserve=1.6)
flow += k.check_table(
    "Every approval on this build",
    [
        ("<b>Deed or contract recorded</b> in my own name before any "
         "construction (§ 33-1002):",
         [("Recorded", 0.4), ("Instrument no.", 0.6)]),
        ("<b>Septic Construction Authorization</b> from the delegated county, "
         "or written confirmation of sewer availability — and the two-year "
         "expiry:",
         [("Number", 0.4), ("Issued", 0.3), ("Expires", 0.3)]),
        ("<b>Septic Discharge Authorization</b> — the county's inspection "
         "before backfill, the tank watertightness certification, and the "
         "as-built site plan:",
         [("Inspected", 0.5), ("DA issued", 0.5)]),
        ("<b>ADWR notice of intent</b> file number, the drilling card, the "
         "driller's license or my single well license, and the two "
         "completion reports — driller's within 30 days of completion, "
         "mine within 30 days of the pump:",
         [("File no.", 0.35), ("Card", 0.3), ("License", 0.35),
          ("Driller's report", 0.5), ("My report", 0.5)]),
        ("<b>Zoning use permit</b> and <b>floodplain permit</b> — the "
         "county building permit issues on these:",
         [("Zoning", 0.5), ("Flood", 0.5)]),
        ("<b>Building permit</b> — the issuing jurisdiction, the adopting "
         "ordinance and code editions printed on it, its life, the "
         "§ 32-1169 statement filed with it (and whether the Registrar's "
         "signature was wanted), and the § 9-836 / § 11-1606 handout:",
         [("Number", 0.3), ("Ordinance / editions", 0.4), ("Expires", 0.3),
          ("Stmt. filed", 0.3), ("ROC sig.?", 0.3),
          ("Handout received", 0.4)]),
        ("<b>Certificate of occupancy</b>, or the dated record of "
         "\"completion\" where none will issue — the day the one-year clock "
         "starts; and if I built under the Cochise or Coconino opt-out, the "
         "option and the recorded notice's instrument number:",
         [("CO no. / completion date", 1.0), ("Option", 0.4),
          ("Recorded notice no.", 0.6)]),
    ], date_w=0.9, notes_w=1.8)
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "az-permit-kit",
                       "AZ.2-permit-application-checklist.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
