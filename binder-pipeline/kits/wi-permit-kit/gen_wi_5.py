#!/usr/bin/env python3
"""WI.5 Forms & Documents Index.

Every document a Wisconsin owner-builder will meet, named the way the agency
names it, with who produces it and where it goes.

Verified sources:
  SBD-5823             the Wisconsin Uniform Building Permit Application —
                       form number and instruction text read directly
  SPS 320.09 Note      the permit and application are reproduced at ch. SPS 325
                       Appendix A
  SPS 320.05           the complete exemption list — what needs no UDC permit
  SPS 320.02(1)(a) Note  cabins, seasonal homes and temporary residences are
                       INSIDE the code, not outside it
  SPS 320.05(9) Note   the park-model trap: keep the chassis and axles on it
  101.648              the religious waiver, and its no-fee rule
  SPS 305.31, 305.315  the two dwelling contractor credentials a sub may hold
  SPS 305.40(2)(a)     what a residential electrician credential covers
  101.654(2)(a)        the bond or $250,000 policy behind a certified builder
  SPS 383.55           POWTS reporting — the duty sits on the OWNER
  SPS 383.54(3)(b)     septic servicing at 1/3 sludge and scum volume

Deliberately NOT printed: the SBD form numbers for the sanitary permit
application and the soil evaluation report. They are widely quoted as SBD-6398
and SBD-8330, but neither could be verified against a department source in this
pass, and a wrong form number sends a reader to the wrong document. The forms
are named by title instead, with the instruction to get them from the county or
the department.
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

FORM_ID = "WI.5"
FORM_TITLE = "Forms & Documents Index"
TOPIC = "Documents & Credentials"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Every document you will meet, who produces it, and where it goes — plus "
    "what needs no permit at all.")

flow.append(k.disclaimer(
    "Form numbers and revision dates change. Where this document names a form "
    "number it was read directly; where it names only a title, the number "
    "could not be verified and you should ask the issuing office for the "
    "current form."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- index
flow += k.h2_tight("THE DOCUMENTS, IN THE ORDER YOU WILL MEET THEM")
rows = [
    [k.cellp("<b>Soil and Site Evaluation Report</b>"),
     k.cellp("A state-certified soil tester"),
     k.cellp("The county"),
     k.cellp("Every page signed with the tester's identification number and "
             "the date")],
    [k.cellp("<b>POWTS plans and specifications</b>"),
     k.cellp("A registered POWTS designer, architect, engineer or designer of "
             "plumbing systems — or the master plumber who will install it"),
     k.cellp("The county, or the department in the counties without plan-"
             "review delegation"),
     k.cellp("Includes the <b>management plan</b> that sets your servicing "
             "intervals")],
    [k.cellp("<b>Sanitary Permit Application</b>"),
     k.cellp("You, as the property owner — but it must name your master "
             "plumber"),
     k.cellp("The county"),
     k.cellp("The permit runs to <b>you</b>, not the installer. Valid 2 "
             "years, renewable, and transferable with the land")],
    [k.cellp("<b>Zoning / land use permit application</b>"),
     k.cellp("You"),
     k.cellp("County zoning in unincorporated towns; otherwise the "
             "municipality"),
     k.cellp("Add shoreland and floodplain review if the parcel is near "
             "water")],
    [k.cellp("<b>Well notification</b>"),
     k.cellp("You, or the driller on your behalf"),
     k.cellp("Department of Natural Resources"),
     k.cellp("Before construction begins. The driller must verify the "
             "notification number exists before spudding in")],
    [k.cellp("<b>Wisconsin Uniform Building Permit Application</b><br/>"
             "<font size=8>form SBD-5823</font>"),
     k.cellp("You"),
     k.cellp("Your municipality, county, the department, or your registered "
             "UDC inspection agency"),
     k.cellp("Carries the erosion control request on the same form, and a "
             "checkbox for one acre or more of disturbance")],
    [k.cellp("<b>Cautionary Statement to Owners Obtaining Building "
             "Permits</b>"),
     k.cellp("You sign it"),
     k.cellp("The permit issuer"),
     k.cellp("Mandatory for every owner applicant — see WI.1")],
    [k.cellp("<b>Driveway / access permit application</b>"),
     k.cellp("You"),
     k.cellp("The authority that maintains the road"),
     k.cellp("Town board, county highway department, or the Department of "
             "Transportation")],
    [k.cellp("<b>Notice of Intent</b>, construction site stormwater"),
     k.cellp("You, as landowner"),
     k.cellp("Department of Natural Resources"),
     k.cellp("Only at one acre or more; 14 working days ahead, with the plan "
             "already complete")],
    [k.cellp("<b>Well Construction Report</b>"),
     k.cellp("The driller"),
     k.cellp("The department <b>and you</b>, within 30 days, electronically"),
     k.cellp("Keep your copy — it is the permanent record of casing, static "
             "level, yield and geology")],
    [k.cellp("<b>Water sample results</b> — total coliform and nitrate"),
     k.cellp("The driller collects; a laboratory reports"),
     k.cellp("As directed"),
     k.cellp("Required after new well construction by rule, not merely by a "
             "lender")],
    [k.cellp("<b>POWTS maintenance and servicing reports</b>"),
     k.cellp("Your servicing provider performs; <b>you</b> report"),
     k.cellp("The county, within 30 days of the event"),
     k.cellp("The reporting duty sits on the owner for the life of the "
             "system")],
]
flow.append(k.ref_table(
    "What each document is, who makes it, and where it goes",
    [k.cellp("Document", bold=True), k.cellp("Produced by", bold=True),
     k.cellp("Filed with", bold=True), k.cellp("Notes", bold=True)],
    rows, [1.75 * inch, 1.45 * inch, 1.35 * inch, CW - 4.55 * inch]))
flow.append(k.cite(
    "The Wisconsin uniform building permit and its application are reproduced "
    "in the code itself — “<i>See ch. SPS 325 Appendix A for a copy of the "
    "Wisconsin uniform building permit and application</i>” (Note to "
    "s. SPS 320.09). The sanitary permit application and the soil evaluation "
    "report are prescribed by the department but are named here by title only: "
    "the rule says the application “<i>shall be made in a format prescribed by "
    "the department</i>” (s. SPS 383.21(2)(a)) without giving a number, and no "
    "department form number could be verified for either in this pass. Ask "
    "your county for the current forms."))

# ---------------------------------------------------------------- no permit
flow += k.h2_tight("WHAT NEEDS NO UDC PERMIT AT ALL", reserve=2.2)
flow.append(k.body(
    "Section SPS 320.05 lists twelve exemptions from the code. Several are "
    "genuinely useful to an owner-builder, and two are traps."))
rows = [
    [k.cellp("<b>Detached garages and accessory buildings</b>"),
     k.cellp("Outside the code, “<i>with the exception of s. SPS "
             "321.08(1)</i>” — the dwelling-separation rule still applies. "
             "Your municipality may still require a permit for it by ordinance "
             "under s. SPS 320.02(2)(c)")],
    [k.cellp("<b>Detached decks</b>"),
     k.cellp("Outside the code “<i>provided the deck does not serve an exit "
             "from the dwelling</i>”. A deck at your back door is not "
             "detached in the sense that matters")],
    [k.cellp("<b>Farm buildings</b>"),
     k.cellp("Outside the code where “<i>used exclusively for farm operations "
             "and not for human habitation</i>”. Both halves must be true")],
    [k.cellp("<b>Repairs and maintenance</b>"),
     k.cellp("Outside the code, including repair of electrical, plumbing, "
             "heating, ventilating and air conditioning systems already "
             "installed")],
    [k.cellp("<b>Existing dwellings</b>"),
     k.cellp("The code does not reach a dwelling begun before its effective "
             "date, or additions and alterations to one — unless your "
             "municipality has adopted the code for those by ordinance")],
    [k.cellp("<b>Dwellings on tribal trust land</b>"),
     k.cellp("Outside the code where the land is “<i>held in trust by the "
             "United States</i>”")],
    [k.cellp("<b>Camping units</b>"),
     k.cellp("Governed by ch. SPS 327 instead")],
    [k.cellp("<b>Religious waiver dwellings</b>"),
     k.cellp("Where a waiver has been accepted under Wis. Stat. s. 101.648. "
             "Neither a municipality nor the department “<i>may charge a "
             "person a fee to apply for or to receive a waiver</i>”")],
    [k.cellp("<b>Primitive rural hunting cabins</b>"),
     k.cellp("<b>Grandfathered only</b> — the structure must trace to one "
             "built before 31 December 1997. You cannot build a new one. See "
             "WI.1")],
]
flow.append(k.ref_table(
    "Exemptions from the Uniform Dwelling Code — s. SPS 320.05",
    [k.cellp("Exemption", bold=True), k.cellp("What it actually covers",
                                              bold=True)],
    rows, [1.95 * inch, CW - 1.95 * inch]))

flow.append(Spacer(1, 4))
flow.append(k.callout_long("Two exemptions that are not exemptions", [
    Paragraph("<b>Calling it a cabin changes nothing.</b> The scope note to "
              "s. SPS 320.02(1)(a) says the code reaches “<i>site-built "
              "dwellings, manufactured buildings used as dwellings, modular "
              "homes and dwellings that may be designated as <b>cabins, "
              "seasonal homes, temporary residences</b>, etc.</i>” A seasonal "
              "place on a lake is a dwelling and needs a permit.", S["body"]),
    Paragraph("<b>The park-model trap.</b> A titled recreational vehicle is "
              "outside the code — but only while it stays a vehicle. The note "
              "to s. SPS 320.05(9) is explicit: at the installation site "
              "“<i>the chassis and axles shall remain on the unit, with the "
              "towbar (hitch) and wheels left at the site. <b>Otherwise the "
              "unit, including a park model, is subject to the UDC.</b></i>” "
              "Take the axles off and you have converted a vehicle into a "
              "dwelling that has to meet the code.", S["body"]),
    Paragraph("<b>And a third worth knowing:</b> three or more dwelling units "
              "leaves the UDC entirely and lands in the commercial building "
              "code, chs. SPS 361 to 366 — a different code, a different plan "
              "review and, for an owner-builder, a very different project.",
              S["body"]),
]))

# ---------------------------------------------------------------- credentials
flow += k.h2_tight("THE CREDENTIALS — WHAT TO ASK A SUB TO SHOW YOU",
                   reserve=2.2)
flow.append(k.body(
    "You signed a statement at permit application saying you understand what "
    "happens if you hire an uninsured contractor. This is the table that makes "
    "that statement actionable. Verify each credential yourself through the "
    "department's public license search rather than accepting a card at face "
    "value."))
rows = [
    [k.cellp("<b>Dwelling Contractor Certification</b>"),
     k.cellp("Held by the <i>business</i>, through its owner, a partner, or "
             "the chairman or chief executive"),
     k.cellp("Proves financial responsibility: a bond of at least $5,000 "
             "<i>or</i> general liability cover of at least $250,000 per "
             "occurrence, plus worker's compensation and unemployment "
             "compliance. Valid one year")],
    [k.cellp("<b>Dwelling Contractor — Restricted</b>"),
     k.cellp("Same, but bonded under $25,000"),
     k.cellp("The holder agrees “<i>not to perform any work on a dwelling for "
             "which the estimated cost of completion is greater than the "
             "amount of the bond</i>”. Check the bond amount against your "
             "job")],
    [k.cellp("<b>Dwelling Contractor Qualifier</b>"),
     k.cellp("Held by an <i>individual</i>"),
     k.cellp("Proves education: at least 12 hours in an approved dwelling "
             "construction course covering construction laws, construction "
             "codes and business practices, with tests")],
    [k.cellp("<b>Master Plumber</b> / <b>Master Plumber-Restricted "
             "Service</b>"),
     k.cellp("Individual license"),
     k.cellp("Required for your POWTS, and named on your building permit for "
             "the plumbing installation. Licenses issue only to individuals "
             "and are not transferable")],
    [k.cellp("<b>Certified Soil Tester</b>"),
     k.cellp("Individual certification"),
     k.cellp("Required before anyone may construct soil bore holes or conduct "
             "the tests behind your sanitary permit")],
    [k.cellp("<b>Electrician credentials</b>"),
     k.cellp("Master, journeyman, or registered — with residential-only "
             "variants"),
     k.cellp("A residential master or journeyman electrician is limited to "
             "“<i>wiring associated with dwellings, dwelling units and "
             "detached accessory buildings … such as garages, carports, "
             "gazebos, and swimming pools</i>” — which is exactly your job, so "
             "a residential credential is not a lesser one here")],
    [k.cellp("<b>Registered HVAC Contractor</b>"),
     k.cellp("Registration, not a license"),
     k.cellp("Mandatory for anyone in the business of HVAC work, but it "
             "involves no examination. The exam-based certification is "
             "voluntary. For refrigerant work, ask for the federal EPA "
             "section 608 card instead")],
]
flow.append(k.ref_table(
    "Who holds what, and what it proves",
    [k.cellp("Credential", bold=True), k.cellp("Held by", bold=True),
     k.cellp("What it actually proves", bold=True)],
    rows, [1.9 * inch, 1.5 * inch, CW - 3.4 * inch]))
flow.append(k.cite(
    "Wis. Stat. ss. 101.654(2)(a), (2m), (3)(b), 101.178(2), (3)(a), "
    "145.06(2), 145.045(1); Wis. Admin. Code ss. SPS 305.31, 305.315, "
    "305.40(2)(a), 305.70(1). Remember that your own exemption means none of "
    "this financial backing stands behind the parts you build yourself — "
    "carry your own liability cover."))

# ---------------------------------------------------------------- keeping
flow += k.h2_tight("WHAT YOU KEEP AFTER THE FINAL INSPECTION", reserve=2.0)
flow.append(k.body(
    "Three obligations outlive the build, and the first one surprises people "
    "because it lands on the owner rather than on a contractor."))
flow.append(k.body(
    "<b>Septic reporting is yours.</b> “<i>The owner of a POWTS or the owner's "
    "agent shall report to the governmental unit or designated agent at the "
    "completion of each inspection, evaluation, maintenance, or servicing "
    "event specified in the approved management plan</i>”, and “<i>the owner "
    "of a POWTS is responsible for fulfillment of the reporting requirements "
    "under this section</i>” (s. SPS 383.55(1)(a), (c)). Reports go in within "
    "<b>30 calendar days</b> of the event and must carry the system's "
    "identifying number, its location, the date, and the license, "
    "certification or registration number of whoever did the work "
    "(s. SPS 383.55(2), (3)). A system “<i>not maintained in accordance with "
    "the approved management plan … shall be considered a human health "
    "hazard</i>” (s. SPS 383.53(2))."))
flow.append(k.callout(
    "The septic interval is not a calendar", [
        Paragraph("The familiar “pump it every three years” is not what "
                  "Wisconsin's rule says for a new system. Servicing of an "
                  "anaerobic treatment tank “<i>shall occur at least when the "
                  "combined sludge and scum volume equals <b>1/3 of the tank "
                  "volume</b></i>” (s. SPS 383.54(3)(b)) — a measurement, not "
                  "a date. The three-year figure is a <b>visual inspection</b> "
                  "duty, and it applies to systems that existed before "
                  "1 July 2000 (s. SPS 383.54(4)(d)1.). For your new system, "
                  "the intervals are whatever your approved management plan "
                  "says, so read it and put those dates in your calendar.", S["body"]),
    ]))
flow.append(k.body(
    "<b>Keep the well construction report</b> — it is the only permanent "
    "record of what the driller found, and a buyer, a lender or a pump "
    "installer will want it years from now. And <b>keep this kit with the "
    "permit</b>: the sources are printed on every page so that a future owner, "
    "inspector or appraiser can check any claim in it against the code as it "
    "stood when you built."))

flow.append(Spacer(1, 4))
flow.append(k.ref_table(
    "Sources — every Wisconsin claim in this document (verified September 2026)",
    [k.cellp("What this document states", bold=True),
     k.cellp("Authority", bold=True)],
    [[k.cellp("The uniform permit and application are printed in the code"),
      k.cellp("Note to s. SPS 320.09; ch. SPS 325 Appendix A")],
     [k.cellp("The sanitary permit application format is prescribed but "
              "unnumbered in the rule"),
      k.cellp("s. SPS 383.21(2)(a)")],
     [k.cellp("The twelve exemptions from the code"),
      k.cellp("s. SPS 320.05(1) to (12)")],
     [k.cellp("Cabins, seasonal homes and temporary residences are inside "
              "the code"),
      k.cellp("Note to s. SPS 320.02(1)(a)")],
     [k.cellp("The park-model chassis and axle rule"),
      k.cellp("Note to s. SPS 320.05(9)")],
     [k.cellp("Three or more units go to the commercial code"),
      k.cellp("s. SPS 320.05(2); chs. SPS 361 to 366")],
     [k.cellp("A municipality may require permits for work outside the code"),
      k.cellp("s. SPS 320.02(2)(c)")],
     [k.cellp("The religious waiver and its no-fee rule"),
      k.cellp("Wis. Stat. s. 101.648(8)")],
     [k.cellp("Bond of $5,000 or liability cover of $250,000"),
      k.cellp("Wis. Stat. s. 101.654(2)(a)")],
     [k.cellp("The restricted certification and its bond ceiling"),
      k.cellp("Wis. Stat. s. 101.654(2m)")],
     [k.cellp("What a residential electrician credential covers"),
      k.cellp("s. SPS 305.40(2)(a)")],
     [k.cellp("Plumbing licenses issue only to individuals"),
      k.cellp("Wis. Stat. s. 145.06(2)")],
     [k.cellp("POWTS reporting sits on the owner; 30 calendar days"),
      k.cellp("s. SPS 383.55(1)(a), (c), (2), (3)")],
     [k.cellp("Servicing at one third sludge and scum volume"),
      k.cellp("s. SPS 383.54(3)(b)")],
     [k.cellp("The 3-year visual inspection applies to pre-2000 systems"),
      k.cellp("s. SPS 383.54(4)(d)1.")]],
    [CW - 2.5 * inch, 2.5 * inch]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "wi-permit-kit",
                       "WI.5-forms-and-documents-index.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
