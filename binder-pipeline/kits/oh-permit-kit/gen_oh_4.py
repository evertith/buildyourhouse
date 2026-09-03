#!/usr/bin/env python3
"""OH.4 Where to File Directory.

Arkansas's directory document had to hand the reader a METHOD, because no
Arkansas agency publishes which jurisdictions permit. Ohio is the opposite and
it is the best news in the kit: the Board of Building Standards publishes an
address-searchable map of every jurisdiction with its residential and
commercial certification flags, and the map is backed by a public dataset.
So this document hands the reader an ANSWER — their own address, in about two
minutes — plus the statewide picture that answer sits inside.

The statewide counts printed here were computed directly from the Board's own
feature service on 2 September 2026 and re-derived independently before print:

  County records      88 total   36 residential-certified   64 commercial
  Municipal records  921 total  475 residential-certified  656 commercial
  Township records  2340 total   10 residential-certified   29 commercial

The 36/52 county split is the Ohio thesis in one number, and the gap between
64 commercial and 36 residential is the R.C. 3791.04(A)(1)(a)/(b) asymmetry
showing up in behavior: the state backstops commercial plan review, so counties
that want only commercial coverage take it; nobody backstops residential.

Township counts are deliberately described qualitatively rather than as a
denominator. The service carries 2,340 township rows against roughly 1,300
actual Ohio townships, so the rows are split polygons and the denominator would
be wrong; the numerator (ten residential-certified rows) is safe to characterize
as "almost none" and is not printed as a ratio.

Every URL printed here was fetched and returned HTTP 200 in September 2026.
Offices, never phone numbers.

DELIBERATELY NOT PRINTED:
  - Any count of Ohio's local health districts. The ODH locator renders its
    directory client-side, no official total was located, and the commonly
    repeated "about 110" could not be confirmed. The locator URL and the
    city-versus-general-district explanation are printed instead.
  - Any per-county building department address or fee.
  - Whether any specific county contracts its enforcement to the state.
  - Any phone number, anywhere.
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

FORM_ID = "OH.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Ohio publishes the answer to \"does anybody permit my parcel?\" — here is "
    "how to get it for your own address, and the offices that exist either "
    "way.")

flow.append(k.disclaimer(
    "Every web address here returned a live page in September 2026. Offices "
    "move; the lookup tool in the next section outlives any printed list."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- the tool
flow += k.h2_tight("OHIO PUBLISHES THE ANSWER — AND IT IS A MAP", reserve=2.0)
flow.append(k.body(
    "This is the single most useful thing in the Ohio kit. The Board of "
    "Building Standards maintains an <b>address-searchable lookup</b> that "
    "tells you which jurisdiction, if any, has residential code-enforcement "
    "authority over a specific parcel — and it reports residential and "
    "commercial certification <b>separately</b>, which is exactly the "
    "distinction that decides whether your house needs a permit."))
flow.append(k.callout(
    "The Board of Building Standards' own description of the tool", [
        Paragraph("\"The information provided by this application is based on "
                  "the records of the Board of Building Standards to help an "
                  "owner identify the entity or entities that have "
                  "<b>commercial or residential code enforcement authority "
                  "based on address</b>. The owner is responsible for "
                  "confirming with the listed jurisdiction or entity of its "
                  "authority.\"", S["body"]),
    ]))
flow.append(k.body(
    "<b>How to run it.</b> Go to <b>com.ohio.gov</b> and search for the Board "
    "of Building Standards, then follow <i>Building Departments</i> to "
    "<i>Building Department Look Up</i>. Enter the parcel address. Read four "
    "things off the result and write all four on the directory page at the end "
    "of this document."))
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp("<b>Residential certified — yes or no</b>"),
     k.cellp("This is the question. If every entity returned for your address "
             "says <i>No</i>, there is no residential building permit for your "
             "house, and no state office can issue you one")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("<b>Which entity holds it</b>"),
     k.cellp("You may get a municipal record and a county record for the same "
             "address. The municipality's own department governs inside its "
             "corporation limits; the county's covers unincorporated territory "
             "and municipalities without their own")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("<b>Commercial certified — separately</b>"),
     k.cellp("Frequently <i>Yes</i> where residential is <i>No</i>. A "
             "commercial-only department cannot permit or inspect your house, "
             "however large it is. Do not read a staffed building department "
             "as an answer to the residential question")],
    [k.cellp("<b>4</b>", center=True),
     k.cellp("<b>The plumbing entity</b>"),
     k.cellp("The dataset names it in its own field, and it is <b>very often "
             "the county health district rather than the building "
             f"department</b> — which is what {sec('3781.03(C)')} predicts. "
             f"Check it separately or you will miss a required inspection")],
]
flow.append(k.ref_table(
    "Four things to read off your result",
    [k.cellp("", bold=True, center=True), k.cellp("Field", bold=True),
     k.cellp("What it tells you", bold=True)],
    rows, [0.35 * inch, 1.75 * inch, CW - 2.1 * inch]))
flow.append(k.cite(
    "The lookup is a live map application, so it needs a browser rather than a "
    "printout — which is precisely why it is worth more than any list we could "
    "print. It is maintained by the office that issues the certifications, so "
    "it updates when a jurisdiction's status changes. <b>Re-run it before any "
    "later phase of your build:</b> a municipality or a county can apply for "
    "residential certification at any time, and the answer you got at "
    "foundation is not guaranteed at framing."))

# ---------------------------------------------------------------- statewide
flow += k.h2_tight("WHAT THAT DATA SHOWS ABOUT OHIO AS A WHOLE", reserve=2.0)
flow.append(k.body(
    "We downloaded the Board's own dataset in September 2026 and counted it. "
    "The picture explains why Ohio owner-builders get such wildly different "
    "answers from each other."))
rows = [
    [k.cellp("<b>Counties</b>"),
     k.cellp("<b>36 of 88</b>", center=True),
     k.cellp("64 of 88", center=True),
     k.cellp("Fewer than half of Ohio's counties hold county-wide residential "
             "certification — but nearly three quarters hold commercial")],
    [k.cellp("<b>Cities and villages</b>"),
     k.cellp("<b>475 of 921</b>", center=True),
     k.cellp("656 of 921", center=True),
     k.cellp("Municipal residential certification is close to a coin flip. "
             "Being inside a city or village settles nothing by itself")],
    [k.cellp("<b>Townships</b>"),
     k.cellp("<b>almost none</b>", center=True),
     k.cellp("almost none", center=True),
     k.cellp("Ten residential-certified township records in the entire "
             "dataset. A township zoning inspector is not a building "
             "inspector, and the two offices answer different questions")],
]
flow.append(k.ref_table(
    "Residential and commercial certification, from the Board's own dataset "
    "(September 2026)",
    [k.cellp("Layer", bold=True),
     k.cellp("Residential certified", bold=True, center=True),
     k.cellp("Commercial certified", bold=True, center=True),
     k.cellp("What it means", bold=True)],
    rows, [1.1 * inch, 1.05 * inch, 1.0 * inch, CW - 3.15 * inch]))
flow.append(k.body(
    f"<b>Look at the gap between those two columns.</b> Sixty-four counties "
    f"took commercial certification; thirty-six took residential. That is not "
    f"an accident of staffing — it is the statute showing up in behavior. "
    f"Under {sec('3791.04(A)(1)(a)')}, if no local department is certified for "
    f"<i>nonresidential</i> work, plans go to the state Superintendent of "
    f"Industrial Compliance. Under (b), if none is certified for "
    f"<i>residential</i> work, <b>nothing goes anywhere.</b> Ohio built a "
    f"backstop for warehouses and not for houses, and counties responded "
    f"exactly as you would expect."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "The 23 counties with no residential certification anywhere in them", [
        Paragraph("Fifty-two counties hold no <i>county-wide</i> residential "
                  "certification — but in twenty-nine of those, a city or "
                  "village inside the county runs its own certified "
                  "department. <b>In the twenty-three below, no county, no "
                  "municipality and no township holds residential "
                  "certification at all.</b> These are the places where, as "
                  "things stood in September 2026, there was genuinely no "
                  "residential building permit to be had anywhere within the "
                  "county line.", S["body"]),
        Paragraph("<b>Adams, Auglaize, Belmont, Coshocton, Guernsey, Hardin, "
                  "Harrison, Holmes, Lawrence, Marion, Mercer, Monroe, "
                  "Morgan, Morrow, Noble, Perry, Putnam, Seneca, Tuscarawas, "
                  "Van Wert, Vinton, Williams and Wyandot.</b>", S["body"]),
        Paragraph("<b>The other twenty-nine are patchwork counties</b> — the "
                  "county is not certified but part of it is covered "
                  "municipally: Allen, Ashland, Athens, Carroll, Columbiana, "
                  "Crawford, Cuyahoga, Defiance, Erie, Fairfield, Fulton, "
                  "Gallia, Hancock, Henry, Highland, Hocking, Huron, Jackson, "
                  "Jefferson, Knox, Lorain, Meigs, Muskingum, Paulding, Pike, "
                  "Ross, Sandusky, Scioto and Washington. <b>Cuyahoga is the "
                  "extreme case:</b> the county holds no residential "
                  "certification while most of the cities inside it do. In a "
                  "patchwork county the answer changes at the city line, which "
                  "is exactly why you check the address rather than the "
                  "county.", S["body"]),
        Paragraph("<b>And twenty-nine counties are certified for commercial "
                  "work but not residential</b> — Allen, Ashland, Auglaize, "
                  "Belmont, Coshocton, Crawford, Fairfield, Fulton, Gallia, "
                  "Guernsey, Hancock, Henry, Holmes, Huron, Lawrence, Meigs, "
                  "Mercer, Monroe, Morgan, Muskingum, Noble, Perry, Pike, "
                  "Ross, Sandusky, Seneca, Tuscarawas, Washington and "
                  "Wyandot. They have a staffed building department with an "
                  "office and a counter, and <b>it cannot issue a permit for "
                  "your house.</b> Do not read the existence of a department "
                  "as an answer to the residential question.", S["body"]),
    ]))
flow.append(k.cite(
    "The thirty-six counties <i>with</i> county-wide residential certification "
    "are Ashtabula, Brown, Butler, Champaign, Clark, Clermont, Clinton, Darke, "
    "Delaware, Fayette, Franklin, Geauga, Greene, Hamilton, Lake, Licking, "
    "Logan, Lucas, Madison, Mahoning, Medina, Miami, Montgomery, Ottawa, "
    "Pickaway, Portage, Preble, Richland, Shelby, Stark, Summit, Trumbull, "
    "Union, Warren, Wayne and Wood. All of these figures were computed from "
    "the Board of Building Standards' own published dataset on 2 September "
    "2026 and checked twice. Shared arrangements are visible in it: Darke, "
    "Miami and Shelby counties list one combined residential department, and "
    "Akron shares an address with Summit County. <b>Status changes</b> — a "
    "legislative body can apply for certification at any time. Treat every "
    "list on this page as a dated snapshot and run the lookup for your own "
    "parcel."))

# ---------------------------------------------------------------- layers
flow += k.h2_tight("WHICH LAYER DOES WHAT", reserve=2.0)
flow.append(k.body(
    "Ohio land is either inside a municipal corporation — a city or a village "
    "— or it is unincorporated, in which case it sits in a township. Every "
    "parcel is also in exactly one of eighty-eight counties. The layers do not "
    "overlap the way people assume, and the office that stops your build is "
    "often not the one you were expecting."))
rows = [
    [k.cellp("<b>Building permit and inspections</b>"),
     k.cellp("A municipal, county or (very rarely) township building "
             "department — <b>only</b> if certified for residential buildings "
             "at that address")],
    [k.cellp("<b>Zoning certificate</b>"),
     k.cellp(f"A different office almost always. Municipalities zone under "
             f"their own ordinances; townships under R.C. Chapter{NB}519 and "
             f"counties under Chapter{NB}303, both <b>only in unincorporated "
             f"territory</b>. A parcel is under county or township zoning, not "
             f"both — and some unincorporated Ohio has neither")],
    [k.cellp("<b>Sewage system and private water</b>"),
     k.cellp("The local board of health, always, statewide, whether or not any "
             "building department exists. This is the most reliable sentence "
             "in the whole kit")],
    [k.cellp("<b>Plumbing</b>"),
     k.cellp(f"Its own statutory track: the Division of Industrial Compliance, "
             f"a board of health, a certified municipal building-inspection "
             f"department, or a contracting county department "
             f"({sec('3781.03(C)')}). Check the lookup's plumbing field")],
    [k.cellp("<b>Driveway or culvert</b>"),
     k.cellp(f"Whoever owns the road. State route: the Department of "
             f"Transportation district. County road: the county engineer — "
             f"\"The owners of land shall construct and keep in repair all "
             f"approaches or driveways from the public roads, <b>under the "
             f"direction of the county engineer</b>\" ({sec('5543.16')}). "
             f"Township road: the trustees, who \"shall have control of the "
             f"township roads\" ({sec('5571.02')})")],
    [k.cellp("<b>Building sewer / sanitary tap</b>"),
     k.cellp("The city engineer's department, the board of health, or the "
             "sewer purveyor — whichever supervises the system your lateral "
             "joins")],
    [k.cellp("<b>Floodplain development permit</b>"),
     k.cellp("The local floodplain administrator. The Department of Natural "
             "Resources coordinates Ohio's role in the national program but "
             "does not issue your permit")],
]
flow.append(k.ref_table(
    "Seven approvals, six different offices",
    [k.cellp("What you need", bold=True), k.cellp("Who has it", bold=True)],
    rows, [1.75 * inch, CW - 1.75 * inch]))
flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "Two Ohio-specific confusions worth heading off", [
        Paragraph("<b>1. A township zoning inspector is not a building "
                  "inspector.</b> They read the township zoning resolution, "
                  "not the Residential Code of Ohio. They decide <i>where</i> "
                  "on the lot and <i>whether</i> the use is allowed; a "
                  "building department decides <i>how</i> it is built. In much "
                  "of unincorporated Ohio the zoning inspector exists and the "
                  "building department does not — so you can need a zoning "
                  "certificate and no building permit on the same parcel. A "
                  "township may also adopt a property-maintenance code under "
                  f"{sec('505.73')}, but that section reaches \"the repair and "
                  f"continued maintenance of structures\" and must govern "
                  f"\"subject matter not addressed by the state residential "
                  f"building code\" — <b>it is not a new-construction permit "
                  f"power.</b>", S["body"]),
        Paragraph("<b>2. Villages and cities sit differently for health.</b> "
                  f"Under {sec('3709.01')}, \"<b>Each city constitutes a city "
                  f"health district. The townships and villages in each county "
                  f"shall be combined into a general health district.</b>\" So "
                  f"a village normally deals with the <i>county's</i> general "
                  f"health district for septic and well — while often running "
                  f"its own building department for everything else. That "
                  f"split catches people, because the building-department "
                  f"pattern and the health-district pattern point opposite "
                  f"ways for exactly the same parcel. Districts also merge, so "
                  f"\"one per county\" is wrong.", S["body"]),
    ]))

# ---------------------------------------------------------------- rural
flow += k.h2_tight("THE SEQUENCE WHEN NO BUILDING DEPARTMENT IS CERTIFIED",
                   reserve=2.2)
flow.append(k.body(
    "\"No building permit\" is not \"no paperwork.\" The real risk is doing "
    "these in the wrong order, because two of them constrain where the house "
    "can physically sit."))
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp("<b>Confirm nobody has jurisdiction</b>"),
     k.cellp("The Board of Building Standards lookup, then the municipality "
             "and the township directly. Get it in writing and date it")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("<b>Zoning</b>"),
     k.cellp("Township or county. Ask about setbacks, minimum lot size and "
             "accessory structures before you site anything")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("<b>Survey and mark the lot lines</b>"),
     k.cellp("Every setback you are about to work to — septic, well, zoning — "
             "is measured from a boundary. Do this before the soil evaluation, "
             "not after")],
    [k.cellp("<b>4</b>", center=True),
     k.cellp("<b>Soil evaluation and sewage permit</b>"),
     k.cellp("Board of health. <b>Constrains the house position</b>, and needs "
             "a replacement area as well as the system itself. The longest "
             "pole on a rural build")],
    [k.cellp("<b>5</b>", center=True),
     k.cellp("<b>Private water system permit</b>"),
     k.cellp("Board of health, before drilling. Sited against the septic "
             "system, so plan the two together")],
    [k.cellp("<b>6</b>", center=True),
     k.cellp("<b>Floodplain determination</b>"),
     k.cellp("Local floodplain administrator. You may need a document "
             "certifying you are <i>outside</i> the hazard area")],
    [k.cellp("<b>7</b>", center=True),
     k.cellp("<b>Driveway or access permit</b>"),
     k.cellp("Decided by which road you touch — state, county or township")],
    [k.cellp("<b>8</b>", center=True),
     k.cellp("<b>Address assignment</b>"),
     k.cellp("Usually the county's 911 or addressing office. Utilities and "
             "often the health district need it")],
    [k.cellp("<b>9</b>", center=True),
     k.cellp("<b>Electric service</b>"),
     k.cellp("Your utility or co-op — in practice the only outside look at "
             "your wiring where no electrical permit exists. Ask early what "
             "they require")],
    [k.cellp("<b>10</b>", center=True),
     k.cellp("<b>Utility locate</b>"),
     k.cellp("Ohio 811, free, before any excavation")],
    [k.cellp("<b>11</b>", center=True),
     k.cellp("<b>Stormwater</b>"),
     k.cellp("Only at one acre of disturbance — or less, if your lot is part "
             "of a larger common plan of development")],
]
flow.append(k.ref_table(
    "The rural sequence",
    [k.cellp("", bold=True, center=True), k.cellp("Step", bold=True),
     k.cellp("Which office, and why the order", bold=True)],
    rows, [0.35 * inch, 1.75 * inch, CW - 2.1 * inch]))

# ---------------------------------------------------------------- state
flow += k.h2_tight("STATE-LEVEL ADDRESSES", reserve=2.0)
flow.append(k.body(
    "All verified to resolve in September 2026. We print no phone numbers "
    "anywhere in this kit — they go stale faster than anything else on a "
    "printed page, and every office below can be reached from its own site."))
rows = [
    [k.cellp("Find out who permits your parcel"),
     k.cellp("com.ohio.gov — Board of Building Standards, then <i>Building "
             "Departments</i> → <i>Building Department Look Up</i>")],
    [k.cellp("The lookup map itself"),
     k.cellp("maps.ohio.gov — the Board's building department application")],
    [k.cellp("Read the building code free"),
     k.cellp("codes.ohio.gov — Ohio Administrative Code, chapter 4101:8")],
    [k.cellp("Read the statutes"),
     k.cellp("codes.ohio.gov — Ohio Revised Code, chapters 3781 and 3791")],
    [k.cellp("Verify a trade contractor's state license"),
     k.cellp("elicense.ohio.gov — remember this is the <b>commercial</b> "
             "license; it is not required for work on a house")],
    [k.cellp("Find your local health district"),
     k.cellp("odh.ohio.gov — <i>Find Local Health Departments</i>. The most "
             "important address in this kit on a rural build")],
    [k.cellp("Sewage treatment system rules and program"),
     k.cellp("odh.ohio.gov — Sewage Treatment Systems; rules at codes.ohio.gov "
             f"under OAC {k.rule('3701-29')}")],
    [k.cellp("Private water system rules"),
     k.cellp(f"codes.ohio.gov — OAC {k.rule('3701-28')}")],
    [k.cellp("Construction stormwater permit"),
     k.cellp("epa.ohio.gov — Division of Surface Water, stormwater program")],
    [k.cellp("Water well logs and drilling records"),
     k.cellp("waterwells.ohiodnr.gov — useful for predicting depth and yield "
             "from neighboring wells before you drill")],
    [k.cellp("Floodplain management"),
     k.cellp("ohiodnr.gov — Division of Water Resources, Floodplains")],
    [k.cellp("Check your flood zone"),
     k.cellp("msc.fema.gov")],
    [k.cellp("Driveway onto a state route"),
     k.cellp("transportation.ohio.gov/about/districts — find your district, "
             "then Right-of-Way &amp; Utility Permits")],
    [k.cellp("Appeal a building department decision"),
     k.cellp("bbalookup.com.ohio.gov — Board of Building Appeals case "
             "database")],
    [k.cellp("Utility locate before digging"),
     k.cellp("oups.org — Ohio 811")],
    [k.cellp("Parcel data, and the homestead credit afterwards"),
     k.cellp("Your county auditor's Real Estate or Property Search. Ohio has "
             "no statewide parcel portal — each of the 88 auditors runs their "
             "own")],
]
flow.append(k.ref_table(
    "What you actually need, and where it lives",
    [k.cellp("To do this", bold=True), k.cellp("Go here", bold=True)],
    rows, [2.35 * inch, CW - 2.35 * inch]))
flow.append(k.cite(
    "<b>One warning about Ohio's state websites.</b> The Commerce, Health, "
    "EPA and Natural Resources sites all run on the same portal, and short "
    "marketing-style addresses on them frequently return a page that loads "
    "normally and says \"No content found\" — a soft failure that looks like a "
    "working link. If a page looks empty, do not conclude the program was "
    "discontinued; search the agency's site for the program name instead. "
    "Every address above was checked as a live page, not merely as a link."))

# ---------------------------------------------------------------- own
# 1.6in leaves the heading alone at the foot of page 6: this table's first
# write-in row wraps to three lines and carries two fill-in rules, so its first
# chunk is taller than the usual two-row reserve.
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT",
                   reserve=2.1)
flow += k.check_table(
    "Every office that touches this build, and what it told you",
    [
        ("<b>Board of Building Standards lookup</b> — residential certified "
         "for my address? Yes / No",
         [("Entity", 0.5), ("Answer", 0.3), ("Date", 0.2)]),
        ("Which entity, and is it municipal or county?",
         [("Entity", 0.6), ("Layer", 0.4)]),
        ("Commercial certified for the same address? (Not the same question.)",
         [("Answer", 1.0)]),
        ("<b>Plumbing entity</b> named by the lookup, and whether a plumbing "
         "permit is required", [("Office", 0.6), ("Answer", 0.4)]),
        ("<b>Municipality or village</b> — confirmed directly",
         [("Office", 0.5), ("Answer", 0.3), ("Date", 0.2)]),
        ("<b>Township</b> — zoning, and whether it has any building authority",
         [("Office", 0.5), ("Answer", 0.3), ("Date", 0.2)]),
        ("<b>County</b> — building department and zoning",
         [("Office", 0.5), ("Answer", 0.3), ("Date", 0.2)]),
        ("<b>Local health district</b> — the sanitarian handling my parcel",
         [("District", 0.6), ("Name", 0.4)]),
        ("Soil evaluator engaged", [("Name", 0.6), ("Credential", 0.4)]),
        ("Septic system designer", [("Name", 0.6), ("Date", 0.4)]),
        ("Septic installer, and their registration",
         [("Name", 0.6), ("Registration", 0.4)]),
        ("Private water systems contractor, and their registration",
         [("Name", 0.6), ("Registration", 0.4)]),
        ("Surveyor for the lot line markers", [("Name", 1.0)]),
        ("Road authority for my driveway — state, county or township",
         [("Office", 1.0)]),
        ("County floodplain administrator", [("Office", 1.0)]),
        ("911 addressing office", [("Office", 1.0)]),
        ("Electric utility or co-op, and its service requirements",
         [("Name", 1.0)]),
        ("County auditor — for the homestead credit afterwards",
         [("Office", 1.0)]),
    ],
    notes_header="Notes", date_w=0.8, notes_w=1.4)
flow.append(k.closing_note(
    "Ohio is one of the few states where the answer to \"does anybody permit "
    "my parcel?\" is published, authoritative and free — so there is no excuse "
    "for guessing, and no reason to accept a neighbor's answer about a "
    "different address. Run the lookup, get the confirmation in writing, date "
    "it, and keep the email behind this sheet. Re-check before any later "
    "phase: a jurisdiction can apply for residential certification at any "
    "time, and the answer that was true at your foundation is not guaranteed "
    "at your framing."))


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "oh-permit-kit",
                       "OH.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
