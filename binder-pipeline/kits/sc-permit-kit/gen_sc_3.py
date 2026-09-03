#!/usr/bin/env python3
"""SC.3 Inspection Sequence.

Structured around the approvals that have to exist before other things can
happen, then the inspections themselves, then the two closing acts that most
owner-builders treat as one.

The South Carolina specifics that shape this document:
  - § 6-9-130(A) fixes the code edition at the permit ISSUANCE date, so the
    permit card is evidence, not paperwork.
  - § 15-3-640 requires the building permit itself to carry a bold-type notice
    of the owner's right to contract for a guarantee beyond eight years, and
    makes the certificate of occupancy statutory proof of substantial
    completion — which starts the eight-year repose clock and is one of the
    two candidate start dates for § 40-59-260(B)'s two-year sale clock.
  - § 6-9-80 sets a two-step civil penalty with a seven-calendar-day cure.
  - The register-of-deeds notice under § 40-59-260(E) happens AFTER the final
    inspection and is the last thing standing between the reader and a revoked
    exemption.

DHEC no longer exists. Septic and private wells are both administered by the
South Carolina Department of Environmental Services at des.sc.gov, and
scdhec.gov no longer serves a site.
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
NB = k.NB
sec = k.sec

FORM_ID = "SC.3"
FORM_TITLE = "Inspection Sequence"
TOPIC = "On the Job"

flow = []
flow += k.header(FORM_ID, FORM_TITLE,
                 "The approvals that come first, the inspections themselves, "
                 "and the two things that happen after the last one.")
flow.append(k.disclaimer())

# ------------------------------------------------------- approvals first
flow += k.h2("THE APPROVALS THAT COME BEFORE THE PERMIT")
flow.append(k.body(
    "South Carolina does not put these in one statute, so nobody hands you the "
    "list. Work down it before you file, because each of these is a separate "
    "office with its own queue and none of them will chase the others for "
    "you."))
rows = [
    [k.cellp("<b>Septic construction permit</b>"),
     k.cellp("Required before you build, if the parcel is not on public "
             "sewer. Administered by the <b>Department of Environmental "
             "Services</b> at <b>des.sc.gov</b> → Permits and Regulations → "
             "Septic Tanks. Several counties will not issue a building permit "
             "without a copy of it — Georgetown County says so on its own "
             "permit page."),
     k.cellp("SCDES")],
    [k.cellp("<b>Well permit</b>"),
     k.cellp("Also SCDES, in a different bureau: <b>des.sc.gov</b> → "
             "Programs → Bureau of Water → Residential Wells. Septic and "
             "wells are set on the same sheet of paper by your site plan, but "
             "they are approved by different parts of the agency."),
     k.cellp("SCDES")],
    [k.cellp("<b>Critical area or beachfront authorization</b>"),
     k.cellp("If the parcel is in or abutting a coastal critical area — "
             "tidelands, marsh, beaches, the beach and dune system — or "
             "seaward of a beachfront jurisdictional line, this is a "
             "<b>separate state approval you must secure yourself</b>. SCDES "
             "<b>Bureau of Coastal Management</b>. Assume your county will "
             "not warn you: no coastal county or city permit page checked for "
             "this kit names it as a precondition."),
     k.cellp("SCDES")],
    [k.cellp("<b>Zoning and setbacks</b>"),
     k.cellp("Usually the same building of government, always a different "
             "desk. Richland County, for one, requires a copy of the property "
             "plat and verification of setbacks and accessory structures "
             "through Zoning before permitting."),
     k.cellp("Local")],
    [k.cellp("<b>Driveway or encroachment permit</b>"),
     k.cellp("Owed to whoever maintains the road you are connecting to, which "
             "on a rural lot is often not your county. Establish who that is "
             "before you cut the driveway, not after."),
     k.cellp("Varies")],
    [k.cellp("<b>Land disturbance and stormwater</b>"),
     k.cellp("Triggered by acreage disturbed rather than by house size, and "
             "handled by the county or by the state depending on the "
             "jurisdiction. Horry County notes a stormwater notice of intent "
             "may run in parallel with the building permit."),
     k.cellp("Varies")],
]
flow.append(k.ref_table(
    "Approvals that sit upstream of your building permit",
    [k.cellp("", bold=True), k.cellp("What it is and where it lives",
                                     bold=True),
     k.cellp("Who", bold=True)],
    rows, [1.62 * inch, CW - 2.42 * inch, 0.80 * inch]))

flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "DHEC does not exist any more, and its website is gone", [
        Paragraph("The South Carolina Department of Health and Environmental "
                  "Control was split. Environmental programs — septic, "
                  "private wells, coastal — are now the <b>South Carolina "
                  "Department of Environmental Services (SCDES)</b> at "
                  "<b>des.sc.gov</b>. Public health went to the "
                  "<b>Department of Public Health</b> at <b>dph.sc.gov</b>.",
                  S["body"]),
        Paragraph("This matters because the old domain is dead, not "
                  "redirected. As of September 2026 <b>scdhec.gov returns "
                  "nothing</b> — no page, no forwarding. Anything you find "
                  "that points you at a DHEC form, a DHEC office or a "
                  "scdhec.gov address is stale, and a surprising amount of it "
                  "is still live on county websites: Anderson, Oconee, York, "
                  "Georgetown, Horry and Kershaw counties were all still "
                  "linking septic guidance to the dead host when this kit was "
                  "checked. Pickens and Berkeley had updated theirs.",
                  S["body"]),
        Paragraph("The old coastal branding is retired too. What guides still "
                  "call <b>OCRM</b> — the Office of Ocean and Coastal "
                  "Resource Management — is now the Bureau of Coastal "
                  "Management inside SCDES, and 2026 Act No.&#160;146, signed "
                  "15&#160;May&#160;2026, rewrote the coastal chapter's "
                  "definitions so that “Department” means the Department of "
                  "Environmental Services and “Division” means its Division "
                  "of Coastal Management.", S["body"]),
        Paragraph("<b>Here is the trap that follows from that.</b> The "
                  "state's own published code page for Title&#160;48 "
                  "Chapter&#160;39 was still printing the old DHEC and OCRM "
                  "wording in September 2026 — the amendments had not been "
                  "folded in. So the official-looking page will contradict "
                  "this kit, and the kit is the current one. Cite the acts, "
                  "not the code page, until it catches up. The coastal "
                  "regulations at Chapter&#160;30 <i>are</i> current; they "
                  "were retitled for the Coastal Division.", S["body"]),
    ]))

# ------------------------------------------------------------- beachfront
flow += k.h2("IF YOU ARE BUILDING ON AN ATLANTIC-FRONTING BEACH")
flow.append(k.body(
    "South Carolina's beachfront rules are <b>geometric, not flood-zone "
    "based</b>, and that surprises people who arrive expecting the FEMA map "
    "to be the whole story. Two lines run along the beach and everything "
    "turns on which side of them your house sits."))
rows = [
    [k.cellp("<b>The baseline</b>"),
     k.cellp("The crest of the primary oceanfront sand dune. The dune itself "
             "is defined by regulation as being at least "
             "<b>36&#160;inches</b> high and roughly continuous over "
             "<b>500&#160;feet</b> measured parallel to the shore."),
     k.cellp(f"{sec('48-39-280')}(A); Regs. 30-1(D)(45)")],
    [k.cellp("<b>The setback line</b>"),
     k.cellp("<b>Forty times</b> the average annual erosion rate, measured "
             "landward from the baseline, and <b>never less than "
             "20&#160;feet</b> landward of it. It is an erosion calculation, "
             "not a flood elevation."),
     k.cellp(f"{sec('48-39-280')}(B); Regs. 30-1(D)(48)")],
    [k.cellp("<b>Seaward of the baseline</b>"),
     k.cellp("No new construction or reconstruction, except a short "
             "statutory list. The only route is a <b>special permit</b>, "
             "which comes with a binding agreement to remove the structure."),
     k.cellp(f"{sec('48-39-290')}(A), (D)")],
    [k.cellp("<b>Partly seaward of the setback line</b>"),
     k.cellp("A new habitable structure here needs a written "
             "<b>certification to the agency — not a permit</b>, and there is "
             "<b>no fee</b>. The conditions are hard: <b>5,000&#160;square "
             "feet</b> of heated space maximum, sited “as far landward on the "
             "property as practicable,” drawings with footprint and "
             "cross-section, no erosion-control device built into the house, "
             "and no part on the primary dune or seaward of the baseline."),
     k.cellp(f"{sec('48-39-290')}(B)(1)(a); Regs. 30-16(A)(1)")],
    [k.cellp("<b>Anything else between the lines</b>"),
     k.cellp("Needs a department permit. A Major Beachfront Critical Area "
             "Permit carries a <b>$1,000</b> fee, against nothing for the "
             "certification above — so which side of that line your house "
             "falls on is worth establishing early."),
     k.cellp(f"{sec('48-39-290')}(B)(4)")],
    [k.cellp("<b>No hard armor</b>"),
     k.cellp("No new seawall, bulkhead or revetment seaward of the setback "
             "line. A grandfathered device destroyed more than "
             "<b>50 percent</b> above grade after 30&#160;June&#160;2005 "
             "<b>must be removed at the owner's expense</b>, and none may be "
             "enlarged, strengthened or rebuilt."),
     k.cellp(f"{sec('48-39-290')}(B)(2)(a)")],
]
flow.append(k.ref_table(
    "The two lines, and what each side of them costs",
    [k.cellp("", bold=True), k.cellp("The rule", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.70 * inch, CW - 3.55 * inch, 1.85 * inch]))
flow.append(k.cite(
    f"Also worth knowing before you buy: “destroyed beyond repair” is defined "
    f"as more than <b>two thirds</b> of replacement value "
    f"({sec('48-39-270')}(11)); destroying dune vegetation seaward of the "
    f"setback line is prohibited ({sec('48-39-310')}); and a seller must "
    f"disclose the baseline and setback line to a buyer "
    f"({sec('48-39-330')}). Enforcement runs $100 to $1,000 a day, and "
    f"unpermitted activity counts as an “act of concealment,” which defeats "
    f"the three-year limitations period ({sec('48-39-170')}(C)). One phrase "
    f"to retire: the “forty-year retreat policy” was <b>deleted</b> from the "
    f"statute by 2018 Act No.&#160;173. Guides still quote it."))

flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "The lines moved in July 2026, and they are still moving", [
        Paragraph("The beachfront jurisdictional lines are re-established "
                  "every seven to ten years, staggered by area, with the old "
                  "lines operative until the new ones are established "
                  f"({sec('48-39-280')}(C) and (D)). <b>Phase&#160;I lines "
                  "took effect on 24&#160;July&#160;2026</b>, covering the "
                  "Beaufort County beaches — Hilton Head, Fripp, Hunting, "
                  "Harbor and Daufuskie among them. <b>Phase&#160;II</b>, "
                  "covering the greater Charleston beaches — Folly, "
                  "Sullivan's Island, Isle of Palms, Kiawah, Seabrook, "
                  "Dewees and Morris, plus the Edisto set — is running "
                  "through 2028, and no proposed lines had been published "
                  "when this kit was checked.", S["body"]),
        Paragraph("So the line that governs your lot may be newer than any "
                  "advice you have been given, or it may be about to change. "
                  "You may appeal a line within one year for a fee of $100 "
                  f"per property, by certified mail to the Division "
                  f"({sec('48-39-280')}(F), as amended by 2026 Act "
                  f"No.&#160;146). And the state's own mapping viewer warns "
                  "that it is approximate — <b>a property-specific survey "
                  "must be performed</b> to establish where the lines fall "
                  "on your parcel.", S["body"]),
    ]))

flow.append(Spacer(1, 3))
flow.append(k.callout(
    "Flood: South Carolina sets no number, so your number is local", [
        Paragraph("There is no statewide freeboard requirement. The word does "
                  "not appear in the building code modifications or in the "
                  "coastal regulations, and there is no floodplain chapter in "
                  "the state code. The only flood modification South Carolina "
                  "makes to the residential code is Reg.&#160;8-1218, which "
                  "amends R322.1 to send floodway construction to ASCE&#160;24 "
                  "and then says: “Where there is a conflict with this code "
                  "and a locally adopted flood ordinance, <b>the more "
                  "restrictive provision shall apply</b>.”", S["body"]),
        Paragraph("Which means your freeboard comes from your local "
                  "floodplain administrator, and the spread is wide: Hilton "
                  "Head Island requires <b>3&#160;feet</b> above the base "
                  "flood elevation, or 13&#160;feet above mean sea level, "
                  "whichever is higher. Ask for the number in writing and put "
                  "it on SC.2. Note also that there is no state V-zone "
                  "permit — South Carolina's jurisdiction is the setback "
                  "line, not the FEMA zone, so clearing one tells you nothing "
                  "about the other.", S["body"]),
    ]))

# ------------------------------------------------- septic and well numbers
flow += k.h2("THE SEPTIC AND WELL NUMBERS THAT SHAPE YOUR SITE PLAN")
flow.append(k.body(
    "Draw the well, the tank and the field before you draw the house. South "
    "Carolina sets the separations in one regulation and they are not "
    "negotiable at the counter — they decide whether a lot works at all. "
    "Every distance below is from R.61-56, Section 200.6, which requires the "
    "installation area to be sized so that no part of the system, excluding "
    "solid pipes, falls inside these figures."))
rows = [
    [k.cellp("Private well"), k.cellp("<b>75&#160;ft</b>", center=True),
     k.cellp("Public well"), k.cellp("<b>100&#160;ft</b>", center=True)],
    [k.cellp("A building"), k.cellp("<b>5&#160;ft</b>", center=True),
     k.cellp("A property line"), k.cellp("<b>5&#160;ft</b>", center=True)],
    [k.cellp("A driveway or parking area"),
     k.cellp("<b>Not under</b>", center=True),
     k.cellp("An inground pool"), k.cellp("<b>15&#160;ft</b>", center=True)],
    [k.cellp("Delineated coastal critical area line, or mean high water of a "
             "stream, canal, pond or other body of water"),
     k.cellp("<b>75&#160;ft</b>", center=True),
     k.cellp("A drainage ditch, stormwater treatment system or detention "
             "pond, at maximum water elevation"),
     k.cellp("<b>25&#160;ft</b>", center=True)],
    [k.cellp("Piped drainage ditches"),
     k.cellp("<b>15&#160;ft</b>", center=True),
     k.cellp("Curtain drains"),
     k.cellp("<b>10&#160;ft up,<br/>25&#160;ft down</b>", center=True)],
    [k.cellp("Upslope of a basement"),
     k.cellp("<b>25&#160;ft</b>", center=True),
     k.cellp("Sides of a basement — 25&#160;ft if foundation drains sit at "
             "or below trench-bottom elevation"),
     k.cellp("<b>15&#160;ft</b>", center=True)],
    [k.cellp("Top of slope of an embankment or cut of 2&#160;ft or more, "
             "where any trench is above the invert"),
     k.cellp("<b>15&#160;ft</b>", center=True),
     k.cellp("Depth to the zone of saturation, below natural grade"),
     k.cellp("<b>36&#160;in</b>", center=True)],
    [k.cellp("Zone of saturation below the deepest point of effluent "
             "application"), k.cellp("<b>6&#160;in</b>", center=True),
     k.cellp("Depth to rock or other restrictive horizon below the deepest "
             "point of effluent application"),
     k.cellp("<b>12&#160;in</b>", center=True)],
]
flow.append(k.ref_table(
    "Septic separations, R.61-56 § 200.6 and § 200.4–200.5",
    [k.cellp("From", bold=True), k.cellp("At least", bold=True),
     k.cellp("From", bold=True), k.cellp("At least", bold=True)],
    rows, [(CW - 1.90 * inch) / 2, 0.95 * inch,
           (CW - 1.90 * inch) / 2, 0.95 * inch]))
flow.append(k.cite(
    "The table above is the floor, not the answer. Section 200.6(2) says only "
    "that “Greater protective offsets shall be required when utilizing "
    "certain system standards contained within this regulation” — naming no "
    "standard and no number, because the greater offsets sit inside the "
    "individual system standards. Two of them matter enormously on a small "
    "lot. <b>If your soils force a mounded, mounded-fill or elevated "
    "system</b>, the 75-foot water-body figure above rises to "
    "<b>125&#160;feet</b> from the critical area line, tidal waters, or the "
    "ordinary high water elevation of environmentally sensitive waters — <b>and "
    "that last term is not a coastal one.</b> The regulation defines "
    "environmentally sensitive waters to include outstanding resource waters, "
    "shellfish harvesting waters and trout-natural waters, “and including "
    "<b>lakes greater than forty (40) acres in size</b> and the Atlantic "
    "Ocean, regardless of their classifications.” A lakefront lot anywhere in "
    "South Carolina — Upstate or Midlands — on a fill-cap or mounded system "
    "is inside that 125-foot rule. Confirm your own water body rather than "
    "assuming; the acreage test is the thing to check. Separately, "
    "a <b>75-foot setback to every adjacent property line</b> can apply, "
    "measured not from the trench but from the point where the fill taper "
    "meets natural grade, or from the outer edge of the aggregate bed. That "
    "property-line figure is conditional: it attaches to contiguous lots in "
    "subdivisions approved after the standard took effect. The elevated "
    "infiltration system also carries an unconditional <b>50-foot</b> buffer "
    "to every property line, measured from the retaining wall. Ask which "
    "system standard your site evaluation calls for <i>before</i> you assume "
    "the five-foot property line figure is yours. "
    "Section 200.7 requires a usable repair or replacement area of at least "
    "<b>50 percent</b> of the size of the original system, free of impervious "
    "materials, buildings, setbacks and easements; the undisturbed ground "
    "between the trenches does not count towards it."))
flow.append(Spacer(1, 4))
rows = [
    [k.cellp("<b>Tank size</b>"),
     k.cellp("“No septic tank shall be installed which has a net liquid "
             "capacity of less than <b>one thousand (1000) gallons</b>. Such "
             "tanks shall be sufficient to serve dwellings of four (4) "
             "bedrooms or less. <b>Two hundred fifty (250) gallons</b> "
             "additional capacity shall be required for each bedroom over "
             "four.” Design flow is <b>120&#160;gpd per bedroom</b>."),
     k.cellp("R.61-56 § 201.1, § 501")],
    [k.cellp("<b>Permit life — two documents, two clocks</b>"),
     k.cellp("A “permit” here means both a <b>permit to construct</b> and an "
             "<b>approval to operate</b>, and both are required. The "
             "five-year figure is the shelf life of the <i>unbuilt</i> one: "
             "“Permits issued after the effective date of this regulation "
             "shall remain valid for a period of <b>five (5) years</b> from "
             "the date of issuance, provided the physical character of the "
             "property has not changed.” Once the system is installed and the "
             "approval to operate issues, “the construction and operation "
             "permit <b>remains in effect for the life of the onsite "
             "wastewater system</b> that it authorizes.” Your finished system "
             "does not expire in five years."),
     k.cellp("R.61-56 § 101.1, § 104.2(3)")],
    [k.cellp("<b>What you do before the site visit</b>"),
     k.cellp("The applicant must clear and mark property boundary lines and "
             "corners, post an identification marker in the front center of "
             "the lot, <b>stake the corners of the proposed building</b>, "
             "mark the proposed stub-out, septic tank and drain field area, "
             "locate the proposed or existing well, and identify any other "
             "structures that may influence the layout — with a site sketch "
             "on or attached to the application. Underbrush clearing may be "
             "required."),
     k.cellp("R.61-56 § 104.1(6)")],
    [k.cellp("<b>Backhoe pits</b>"),
     k.cellp("Required above the Fall Line separating the Piedmont from the "
             "Coastal Plain — so an Upstate or Midlands lot gets a dug pit, "
             "not just borings."),
     k.cellp("R.61-56 § 104.1(5)")],
    [k.cellp("<b>Covering it early is a violation</b>"),
     k.cellp("“It shall be considered a violation of this regulation to cover "
             "a system that has not been subject to final Department "
             "inspection or installer self-inspection.” Installation "
             "documentation is due within <b>two business days</b>."),
     k.cellp("R.61-56 § 104.3")],
]
flow.append(k.ref_table(
    "Five septic facts worth knowing before you buy the lot",
    [k.cellp("", bold=True), k.cellp("What the regulation says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.55 * inch, CW - 3.00 * inch, 1.45 * inch]))

flow.append(Spacer(1, 4))
flow.append(k.body(
    "Wells are a separate regulation and a genuinely different answer. The "
    "separations run from the <b>well</b> outward: <b>20&#160;feet</b> from "
    "sewer lines; <b>50&#160;feet</b> from lakes, streams and surface-water "
    "bodies, and from animal feedlots, barns and stables; <b>75&#160;feet</b> "
    "from a septic tank or tile field; <b>100&#160;feet</b> from land "
    "application sites, waste treatment lagoons, chemical, herbicide, "
    "pesticide and petroleum storage or handling sites, and landfills; and "
    "<b>5&#160;feet</b> from property lines and buildings."))
flow.append(k.cite("R.61-71 (Well Standards), Section E.1."))
flow.append(Spacer(1, 2))
flow.append(k.callout_long(
    "South Carolina lets you drill your own well", [
        Paragraph("This is unusual and it is stated twice. R.61-44 defines a "
                  "well driller to “include owners constructing or abandoning "
                  "wells on their own property <b>for their own personal use "
                  "only</b>, except that such owners are not required to be "
                  "licensed by the Department of Labor, Licensing, and "
                  "Regulation for constructing wells and are not subject to "
                  "the bonding requirements.” Section C.1 repeats it: the "
                  "licensing requirement “does not apply to owners "
                  "constructing or abandoning wells on their own property for "
                  "their own personal use only.”", S["body"]),
        Paragraph("What you do not escape is the general permit. It is "
                  "unlawful to construct a well “unless conditions of the "
                  "general permit issued by the Department have been "
                  "satisfied,” which means a <b>Notice of Intent</b> before "
                  "you start. The Department reviews it fast, and the "
                  "default is in your favor: approval, comments or denial "
                  "within <b>48&#160;hours</b> excluding weekends and state "
                  "holidays, and “If notice is not given to the applicant by "
                  "the end of the 48 hour period, coverage under the general "
                  "permit… will be considered approved.” Another "
                  "48&#160;hours' notice of the actual installation date is "
                  "required, and it may run concurrently.", S["body"]),
        Paragraph("Then the construction standards bind you exactly as they "
                  "bind a driller: grout the full annular space from a "
                  "minimum depth of <b>20&#160;feet</b>, grouted in place "
                  "within <b>five days</b> of borehole completion; casing "
                  "extending at least <b>one foot above land surface</b>; a "
                  "sanitary seal on top of the casing; disinfection on "
                  "completion to a chlorine residual of "
                  "<b>50 to 250&#160;ppm for at least four hours</b>; a "
                  "durable identification plate; and Water Well Record "
                  "Form&#160;1903 submitted <b>within thirty days</b> after "
                  "completion.", S["body"]),
    ]))

# ---------------------------------------------------------- the permit
flow += k.h2("WHAT YOUR PERMIT IS EVIDENCE OF")
flow.append(k.body(
    f"Two statutes turn the permit card into something worth photographing "
    f"the day you get it."))
flow.append(k.bullet(
    f"<b>It fixes your code edition.</b> “Buildings must be inspected in "
    f"accordance with the codes in effect for the locality on the date of the "
    f"issuance of the original building permit” ({sec('6-9-130')}(A)). If a "
    f"new edition takes effect mid-build, your job stays where it started. "
    f"The regulation says the same thing: work approved before the "
    f"implementation date “must be inspected under the building codes in "
    f"effect at the time the original building permit was issued” "
    f"(R.8-236(B))."))
flow.append(k.bullet(
    f"<b>It is required to carry a warning in bold type.</b> "
    f"Section{NB}15-3-640 provides that “A building permit for the construction "
    f"of an improvement to real property must contain in bold type notice to "
    f"the owner or possessor of the property of his rights under this section "
    f"to contract for a guarantee of the structure being free from defective "
    f"or unsafe conditions beyond eight years after substantial completion.” "
    f"Look for it. It is telling you that South Carolina's outside limit on "
    f"construction-defect claims is <b>eight years</b>, and that you may "
    f"negotiate a longer guarantee by contract before substantial "
    f"completion — which is the only moment you have any leverage to."))

flow.append(Spacer(1, 2))
flow.append(k.callout(
    "The eight-year clock, and why an owner-builder sits on both sides of it",
    [
        Paragraph(f"Section&#160;15-3-640 bars actions “based upon or "
                  "arising out of the defective or unsafe condition of an "
                  "improvement to real property… more than eight years after "
                  "substantial completion.” It protects whoever built the "
                  f"thing. But {sec('15-3-670')}(A) withdraws that protection "
                  "from “a person in actual possession or control, as owner, "
                  "tenant, or otherwise, of the improvement” who knew or "
                  "reasonably should have known of the defective condition. "
                  "Build it and live in it and you are on both sides of that "
                  "sentence.", S["body"]),
        Paragraph(f"One useful qualifier: {sec('15-3-670')}(B) says “the "
                  "violation of a building code of a jurisdiction or "
                  "political subdivision does not constitute per se fraud, "
                  "gross negligence, or recklessness, but this type of "
                  "violation may be admissible as evidence.” A failed "
                  "inspection is not automatically ruinous. A record of "
                  "having corrected it is worth keeping.", S["body"]),
    ]))

# --------------------------------------------------------- the sequence
flow += k.h2_tight("THE INSPECTION SEQUENCE", reserve=2.0)
flow.append(k.body(
    "South Carolina enforces the adopted code's inspection provisions through "
    "your local building official, and the administrative chapter is one of "
    "the few parts of the code the state leaves to local adoption "
    "(R.8-236(E)). So <b>the exact call list and the notice you owe are your "
    "office's</b>. What follows is the order the work happens in, with the "
    "state-specific items marked. Confirm the list at the counter and cross "
    "out what does not apply."))
flow += k.check_table(
    "Inspection log",
    [
        ("<b>Temporary power</b> — often the first thing you need and the "
         "easiest to forget to schedule", []),
        ("<b>Footing</b> — forms and steel in place, before concrete", []),
        ("<b>Foundation, slab or pier</b> — before pour or backfill. Exterior "
         "piers need one #4 dowel mid-depth (R.8-1220)", []),
        ("<b>Under-slab vapor retarder</b> — 10-mil ASTM E1745 Class A, "
         "joints lapped 6 inches (R.8-1225)", []),
        ("<b>Termite pretreatment record</b> — establish who produces it and "
         "who wants to see it", []),
        ("<b>Underground and under-slab plumbing</b>", []),
        ("<b>Framing and sheathing</b>", []),
        ("<b>Truss design drawings handed over</b> — the state code requires "
         "them “at the time of inspection” and with the truss shipment "
         "(R.8-1224, R.8-1227)", []),
        ("<b>Electrical rough-in</b>", []),
        ("<b>Plumbing rough-in</b>", []),
        ("<b>Mechanical rough-in</b>", []),
        ("<b>Insulation</b> — check the six-inch termite inspection strip at "
         "the sill is left open (R.8-1217)", []),
        ("<b>Energy compliance</b> — to the 2009 IECC, in whatever form your "
         "office accepts", []),
        ("<b>Crawl space</b>, if unvented — vapor retarder plus one of the "
         "four conditioning options (R.8-1221)", []),
        ("<b>Final electrical</b>", []),
        ("<b>Final plumbing</b> — the shower liner test is performed here, "
         "15 minutes, no leakage (R.8-1239)", []),
        ("<b>Final mechanical</b>", []),
        ("<b>Final building</b>", []),
        ("<b>Certificate of occupancy issued</b>", []),
    ], notes_header="Result / inspector")

# ------------------------------------------------------- failing one
flow += k.h2_tight("WHAT A VIOLATION ACTUALLY COSTS", reserve=2.0)
flow.append(k.body(
    "South Carolina writes this in the Building Codes Act rather than leaving "
    "it to local ordinance, and the structure is two-step with a cure period "
    "in the middle."))
rows = [
    [k.cellp("<b>First violation</b>"),
     k.cellp("“A person found to be in violation of a building code or "
             "regulation adopted pursuant to the provisions of this chapter "
             "must be cited and fined, by civil fine, in an amount <b>not "
             "more than two hundred dollars</b>.”"),
     k.cellp(f"{sec('6-9-80')}(B)")],
    [k.cellp("<b>Seven days to cure</b>"),
     k.cellp("“Before being charged with a second violation, the person must "
             "be given <b>seven calendar days</b> to remedy the violation "
             "<b>or submit a plan</b> for correcting the violation.” A plan "
             "counts. Submit one in writing and keep the copy."),
     k.cellp(f"{sec('6-9-80')}(B)")],
    [k.cellp("<b>Then it compounds</b>"),
     k.cellp("Failure to correct or submit a plan within those seven days "
             "means a civil fine “not to exceed <b>two thousand dollars</b>. "
             "<b>Each day a violation continues is a separate offense.</b>”"),
     k.cellp(f"{sec('6-9-80')}(C)")],
    [k.cellp("<b>Your neighbor has standing</b>"),
     k.cellp("Injunctive relief or mandamus may be sought not only by the "
             "building official and the county or municipal attorney but by "
             "“an <b>adjacent or neighboring property owner</b> who would be "
             "damaged by the violation.”"),
     k.cellp(f"{sec('6-9-80')}(A)")],
    [k.cellp("<b>Energy is separate</b>"),
     k.cellp("Under the Energy Standard Act the official “shall notify the "
             "permit holder in writing to bring the building into compliance… "
             "or to secure it from entry or both; if the permit holder fails "
             "to comply… the building official <b>shall revoke the "
             "permit</b>.”"),
     k.cellp(f"{sec('6-10-50')}(E)")],
]
flow.append(k.ref_table(
    "The penalty structure, and the cure period inside it",
    [k.cellp("", bold=True), k.cellp("What the statute says", bold=True),
     k.cellp("Cite", bold=True)],
    rows, [1.55 * inch, CW - 2.65 * inch, 1.10 * inch]))

# ---------------------------------------------------------- after final
flow += k.h2("AFTER THE FINAL: TWO CLOSING ACTS, NOT ONE")
flow.append(k.body(
    "Most owner-builders treat the certificate of occupancy as the end. In "
    "South Carolina it is the end of one thing and the start of three "
    "others."))
flow.append(k.bullet(
    f"<b>The certificate of occupancy is legally required before you move "
    f"in.</b> “A building constructed after the effective date of the Energy "
    f"Standard must not be used or occupied until a certificate of occupancy "
    f"has been issued” ({sec('6-10-50')}(F))."))
flow.append(k.bullet(
    f"<b>It is also statutory proof of substantial completion.</b> “For any "
    f"improvement to real property, a certificate of occupancy issued by a "
    f"county or municipality, in the case of new construction… shall "
    f"constitute proof of substantial completion of the improvement under the "
    f"provisions of Section 15-3-630, unless the contractor and owner, by "
    f"written agreement, establish a different date of substantial "
    f"completion” ({sec('15-3-640')}). That date starts the eight-year "
    f"repose clock."))
flow.append(k.bullet(
    f"<b>And it is one of the two candidate start dates for the two-year sale "
    f"clock.</b> Section&#160;40-59-260(B) runs its window from “two "
    f"years after completion or issuance of a certificate of occupancy.” One "
    f"certificate, two clocks, both running."))
flow.append(Spacer(1, 3))
flow.append(k.callout(
    "The filing that is easiest to skip and worst to skip", [
        Paragraph(f"Section&#160;40-59-260(E): the owner “must promptly "
                  "file as a matter of public record a notice with the "
                  "<b>register of deeds</b>, indexed under the owner's name "
                  "in the grantor's index, stating that the residential "
                  "building or structure was constructed by the owner as an "
                  "unlicensed builder. <b>Failure to do so revokes the "
                  "statutory exemption.</b>”", S["body"]),
        Paragraph("There is no deadline in days and no reminder. Counties "
                  "handle the timing differently — several fold the recording "
                  "into permit issuance so that it happens at the front of "
                  "the job rather than the back. Greenville County requires "
                  "the disclosure statement to be notarized <i>and</i> "
                  "recorded before it is submitted; Sumter requires recording "
                  "before the permit issues; Richland requires notarization "
                  "and filing with the Register of Deeds. Find out which way "
                  "yours runs, and if it runs the statutory way — after the "
                  "house exists — put a reminder somewhere you will see it "
                  "the week you get your certificate.", S["body"]),
    ]))

flow.append(Spacer(1, 4))
flow += k.check_table(
    "Closing out",
    [
        ("Certificate of occupancy issued and filed with your records",
         [("Date", 1.0)]),
        (f"Register-of-deeds notice under {sec('40-59-260')}(E) recorded, and "
         f"the recording reference written down",
         [("Book / page", 0.6), ("Date", 0.4)]),
        ("Permit card, every inspection result and the approved plans stored "
         "together — this is your evidence for the next eight years", []),
        ("Termite treatment record and any warranty in the same file", []),
        ("Septic final approval or sewer connection approval on file",
         [("Date", 1.0)]),
        ("Well completion paperwork and water test results on file, if you "
         "drilled", [("Date", 1.0)]),
        ("Two-year sale window diarized from both candidate dates — "
         "completion and certificate of occupancy",
         [("Earliest", 0.5), ("Latest", 0.5)]),
    ])

# -------------------------------------------------------------- sources
flow += k.h2_tight("SOURCES", reserve=2.0)
flow.append(k.sources_table([
    ("Septic and private wells are administered by the Department of "
     "Environmental Services, not by DHEC",
     "SCDES, des.sc.gov"),
    ("Coastal critical area and beachfront authorizations",
     "SCDES Bureau of Coastal Management"),
    ("The permit issuance date fixes the code edition your house is "
     "inspected against",
     f"S.C. Code Ann. {sec('6-9-130')}(A); Reg. 8-236(B)"),
    ("The building permit must carry a bold-type notice of the right to "
     "contract for a longer guarantee; eight-year repose; the certificate of "
     "occupancy is proof of substantial completion",
     f"S.C. Code Ann. {sec('15-3-640')}"),
    ("The repose limit is unavailable to an owner in possession who knew of "
     "the defect; a code violation is evidence but not per se recklessness",
     f"S.C. Code Ann. {sec('15-3-670')}"),
    ("Civil fines, the seven-calendar-day cure, daily accrual, and a "
     "neighbor's standing to seek an injunction",
     f"S.C. Code Ann. {sec('6-9-80')}"),
    ("Energy enforcement and permit revocation; no occupancy without a "
     "certificate", f"S.C. Code Ann. {sec('6-10-50')}(E), (F)"),
    ("The register-of-deeds notice, and what failing to file it does",
     f"S.C. Code Ann. {sec('40-59-260')}(B), (E)"),
    ("Truss drawings at inspection; shower liner test at final plumbing; "
     "termite inspection strip; slab and crawl space vapor retarders",
     "S.C. Code of Regs. 8-1224, 8-1227, 8-1239, 8-1217, 8-1225, 8-1221"),
    ("Administrative provisions of the code are left to local adoption, so "
     "the call list is your office's", "S.C. Code of Regs. 8-236(E)"),
    ("Septic separations, tank sizing, permit life, site preparation, "
     "backhoe pits above the Fall Line, repair area, and the bar on covering "
     "an uninspected system",
     "S.C. Code of Regs. 61-56 §§ 104, 200, 201, 501"),
    ("Well separations, grouting, casing above grade, sanitary seal, "
     "disinfection, identification plate, Form 1903 in thirty days",
     "S.C. Code of Regs. 61-71"),
    ("Owners may construct a well on their own property for personal use "
     "without an LLR license; the Notice of Intent and its 48-hour review",
     "S.C. Code of Regs. 61-44 §§ B, C, D"),
    ("The beachfront baseline and setback line, the certification route and "
     "its 5,000 sq ft cap, the hard-armor ban, dune vegetation, seller "
     "disclosure, enforcement and the lines review cycle",
     f"S.C. Code Ann. {sec('48-39-170')}, {sec('48-39-270')}, "
     f"{sec('48-39-280')}, {sec('48-39-290')}, {sec('48-39-310')}, "
     f"{sec('48-39-330')}; Regs. 30-1, 30-16"),
    ("The coastal agency's current name and authority",
     "2023 Act No. 60; 2026 Act No. 146"),
    ("No statewide freeboard; the more restrictive of code and local flood "
     "ordinance applies", "S.C. Code of Regs. 8-1218"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "sc-permit-kit",
                       "SC.3-inspection-sequence.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
