#!/usr/bin/env python3
"""TN.4 Where to File Directory.

Every web address in this document was confirmed to resolve in September 2026.
No phone numbers appear anywhere in this kit — they go stale faster than
anything else on a printed page, and every office below can be reached from its
own site. That rule also keeps us from reproducing the State Fire Marshal's
jurisdiction table, which carries inspector names, emails and phone numbers.

The organising idea: unlike most states in this line, Tennessee DOES publish the
answer. There is a dated, per-jurisdiction table covering all 95 counties and 378
municipalities. So this document is not a "how to find out whether anyone has
jurisdiction" method — it is a "here is the list, here is how to read it, and
here is the place where the state contradicts itself" document.

Verified in this pass:
  The jurisdictions table was fetched and its HTML parsed directly: 95 county
  rows breaking exactly 50 EXEMPT / 37 OPT OUT / 8 SRBP, page self-dated
  8/21/2026.
  The SRBP county list on the "apply for a residential permit" page lists SEVEN
  counties and omits Campbell County, which the dated jurisdictions page lists as
  SRBP with a named assigned inspector. Both pages fetched 2 September 2026.
  TDEC publishes EIGHT Environmental Field Offices; the CN-0971 septic
  application form routes to SEVEN. The kit tells the reader to use the map on
  the form rather than printing a county-to-office table.

DELIBERATELY NOT PRINTED:
  - Any per-county fee figure except the state schedule. Only three fee bases in
    the whole state were verifiable, and a wrong fee is worse than none.
  - A TVA Section 26a URL or threshold. TVA returned HTTP 403 to every automated
    request; unverified.
  - A statewide E-911 addressing process. Addressing is administered county by
    county and no statewide document was verified.
  - Any claim about Sevier County post-wildfire construction requirements. No
    such ordinance was found on the county's own site.
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

FORM_ID = "TN.4"
FORM_TITLE = "Where to File Directory"
TOPIC = "Who to Contact"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Tennessee publishes the answer — here is where the list lives, how to read "
    "it, and the one place the state contradicts itself.")

flow.append(k.disclaimer(
    "Every web address here was checked in September 2026. Offices move and the "
    "jurisdiction list changes by design — see the note on expiry below."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- the list
flow += k.h2_tight("THE LIST EXISTS — AND IT IS BETTER THAN MOST STATES GIVE YOU",
                   reserve=2.0)
flow.append(k.body(
    "Most states leave you ringing round to find out whether anybody permits "
    "your parcel. <b>Tennessee publishes it.</b> The State Fire Marshal's Office "
    "maintains a single table covering every one of the state's 95&#160;counties "
    "and 378&#160;municipalities, tags each with its status, and — unusually — "
    "names the inspector assigned to it."))
flow.append(k.callout(
    "The one address to write down", [
        Paragraph("<b>tn.gov/commerce/fire/residential-permits/"
                  "jurisdictions-inspectors.html</b>", S["body"]),
        Paragraph("The page carries its own currency date. When this kit was "
                  "assembled it read \"This information is accurate as of "
                  "8/21/2026\", and the table held 95 county rows breaking "
                  "<b>50 EXEMPT, 37 OPT OUT and 8 SRBP</b>. Check the date on "
                  "the page against the date on this kit — if the page has "
                  "moved on, the page wins.", S["body"]),
    ]))

flow.append(Spacer(1, 4))
flow.append(k.body(
    "<b>Read your CITY row first.</b> A county's row governs only its "
    "unincorporated area — that limit is written into the statute itself, which "
    "confines county action \"to the jurisdictional boundaries outside any "
    "municipality located within the county.\" So a city inside an opted-out "
    "county routinely runs its own building department."))
rows = [
    [k.cellp("<b>Grundy County</b> — OPT OUT"),
     k.cellp("<b>Monteagle</b>, inside it — EXEMPT")],
    [k.cellp("<b>Franklin County</b> — OPT OUT"),
     k.cellp("Cowan, Decherd, Estill Springs, Huntland, Monteagle, Tullahoma "
             "and Winchester — <b>all EXEMPT</b>")],
    [k.cellp("<b>Campbell County</b> — SRBP"),
     k.cellp("Caryville, Jacksboro and Jellico — EXEMPT; LaFollette and Rocky "
             "Top — SRBP")],
    [k.cellp("<b>Claiborne County</b> — OPT OUT"),
     k.cellp("Speedwell — also OPT OUT; but Cumberland Gap, Harrogate, New "
             "Tazewell and Tazewell — EXEMPT")],
]
# 2.3in. "Claiborne County — OPT OUT" measures 150pt and needs 2.22in; at
# 1.95in every OPT OUT row wrapped to two lines, and on page 1 that left the
# bare words "OPT OUT" as the last line on the page — which orphan_headings.py
# correctly read as an all-caps heading stranded at a page foot. Binding the
# status with a non-breaking space only moved the wrap; the column had to grow.
flow.append(k.ref_table(
    "Four places a county-level answer would be wrong",
    [k.cellp("The county says…", bold=True),
     k.cellp("…and the cities inside it say something else", bold=True)],
    rows, [2.3 * inch, CW - 2.3 * inch]))

# ---------------------------------------------------------------- the conflict
flow += k.h2_tight("WHERE THE STATE CONTRADICTS ITSELF", reserve=2.2)
flow.append(k.body(
    "The State Fire Marshal publishes the list of state-enforced counties in "
    "<b>two</b> places, and in September 2026 the two did not agree. We fetched "
    "both and parsed them rather than eyeballing them, because this is the sort "
    "of thing that is easy to get wrong and expensive to be wrong about."))
# The page paths are deliberately NOT printed in this column. Both are longer
# than a 2in cell and split mid-word — "…/residential-permits/jurisd" +
# "ictions-inspectors.html" — which reads as broken and is un-typeable. The
# full address of each page is printed in the state-addresses table later in
# this document, so the name alone identifies it here.
rows = [
    [k.cellp("<b>The jurisdictions and inspectors table</b><br/>"
             "<i>the one with the currency date on it</i>"),
     k.cellp("<b>Eight</b> SRBP counties: Campbell, Chester, Giles, Hardeman, "
             "Hawkins, Lauderdale, Meigs, Smith"),
     k.cellp("Lists Campbell County as SRBP <b>with a named assigned "
             "inspector</b>")],
    [k.cellp("<b>The apply-for-a-permit page</b><br/>"
             "<i>reached from the residential permits hub</i>"),
     k.cellp("<b>Seven</b> SRBP counties: Chester, Giles, Hardeman, Hawkins, "
             "Lauderdale, Meigs, Smith"),
     k.cellp("Carries no date. <b>Campbell County is absent entirely</b>")],
]
flow.append(k.ref_table(
    "Two official pages, two different answers",
    [k.cellp("Page", bold=True), k.cellp("What it lists", bold=True),
     k.cellp("Notes", bold=True)],
    rows, [2.0 * inch, (CW - 2.0 * inch) * 0.52,
           (CW - 2.0 * inch) * 0.48]))
flow.append(k.cite(
    "Both pages were fetched and their markup parsed on 2 September 2026. We are "
    "not guessing at which is right: the dated table is the better source "
    "because it carries a currency stamp, covers every jurisdiction rather than "
    "a summary, and names the inspector. <b>But if you are in Campbell County, "
    "or anywhere the two disagree when you read them, do not pick a winner "
    "yourself.</b> Ask the office, get the answer in writing, and record it on "
    "the directory page at the end of this document."))

flow.append(Spacer(1, 4))
flow.append(k.callout_long(
    "And remember the list is designed to change", [
        Paragraph("An opt-out resolution <b>expires 180&#160;days after that "
                  "legislative body's next election</b> unless the incoming "
                  "body passes it again. The rule requiring a jurisdiction to "
                  "file \"the date of the next election for the legislative "
                  "body\" when it opts out exists precisely because of that "
                  "sunset (rule 0780-02-23-.14).", S["body"]),
        Paragraph("So a county that had no building code when you bought the "
                  "land can have one by the time you pour — and the State Fire "
                  "Marshal resumes enforcement automatically if the resolution "
                  "lapses. <b>Re-check the list before you file, not just "
                  "before you buy.</b>", S["body"]),
    ]))

# ---------------------------------------------------------------- where to file
flow += k.h2_tight("WHERE TO FILE UNDER EACH STATUS", reserve=2.2)
rows = [
    [k.cellp("<b>EXEMPT</b>"),
     k.cellp("The local building department. Their adopted code edition and "
             "their fee schedule govern, and both may differ from the state's — "
             "an exempt jurisdiction need only stay within <b>seven years</b> "
             "of the current published edition")],
    [k.cellp("<b>SRBP</b>"),
     k.cellp("The state, at <b>core.tn.gov</b>, or in person from a contracted "
             "issuing agent. State fee schedule, state contract inspectors, "
             "state certificate of occupancy")],
    [k.cellp("<b>OPT OUT</b>"),
     k.cellp("Nobody, for the building permit. You may still buy a state permit "
             "<i>voluntarily</i> and receive inspections and a certificate of "
             "occupancy — which is often the cheapest way to satisfy a "
             "construction lender")],
]
flow.append(k.ref_table(
    "The building permit",
    [k.cellp("Status", bold=True), k.cellp("Where the permit comes from",
                                           bold=True)],
    rows, [1.0 * inch, CW - 1.0 * inch]))
flow.append(k.cite(
    "The seven-year currency requirement on exempt jurisdictions is "
    f"{sec('68-120-101(b)(5)(A)')}. It is worth knowing because it is the "
    f"reason a large city can be on a newer code than the state: Tennessee's "
    f"own residential code is the 2018 IRC, and an exempt jurisdiction may have "
    f"adopted something more recent. Ask yours which edition it reviews to, and "
    f"write it down — TN.2 has the line for it."))

# ---------------------------------------------------------------- regardless
flow += k.h2_tight("THE OFFICES THAT EXIST WHATEVER YOUR STATUS", reserve=2.4)
flow.append(k.body(
    "\"No building permit\" is not the same as \"no paperwork.\" The real risk "
    "is not missing an office — it is doing them in the wrong order, because "
    "two of them constrain where the house can physically sit."))
rows = [
    [k.cellp("<b>1</b>", center=True),
     k.cellp("<b>Confirm your status</b>"),
     k.cellp("The jurisdictions table, then your city. Do this before relying "
             "on any of the rest")],
    [k.cellp("<b>2</b>", center=True),
     k.cellp("<b>911 address</b>"),
     k.cellp("Administered county by county — often a 911 district or "
             "emergency communications office. Early: utilities and often the "
             "septic permit need it")],
    [k.cellp("<b>3</b>", center=True),
     k.cellp("<b>Septic permit</b>"),
     k.cellp("TDEC Division of Water Resources on form <b>CN-0971</b>, unless "
             "your county runs its own program. <b>Constrains the house "
             "position</b> — do it before you fix the footprint")],
    [k.cellp("<b>4</b>", center=True),
     k.cellp("<b>Zoning approval</b>"),
     k.cellp("A building-code opt-out is <i>not</i> a zoning opt-out. The "
             "state permit expressly excludes zoning approval")],
    [k.cellp("<b>5</b>", center=True),
     k.cellp("<b>Electrical permit</b>"),
     k.cellp("The state, unless you are inside one of the electrical exempt "
             "jurisdictions. <b>Required even where the building code is "
             "not</b>")],
    [k.cellp("<b>6</b>", center=True),
     k.cellp("<b>Floodplain determination</b>"),
     k.cellp("The local floodplain administrator. Separate from the building "
             "code and unaffected by an opt-out")],
    [k.cellp("<b>7</b>", center=True),
     k.cellp("<b>Driveway or culvert permit</b>"),
     k.cellp("Decided by the road you touch: a state highway means the "
             "Department of Transportation, a county road the county highway "
             "department, a city street the city")],
    [k.cellp("<b>8</b>", center=True),
     k.cellp("<b>Utility locate</b>"),
     k.cellp("Tennessee 811, free, before any excavation")],
]
flow.append(k.ref_table(
    "The sequence, whatever your status",
    [k.cellp("", bold=True, center=True), k.cellp("Step", bold=True),
     k.cellp("Which office, and why the order", bold=True)],
    rows, [0.35 * inch, 1.55 * inch, CW - 1.9 * inch]))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "The septic office list has a wrinkle — use the form, not a table", [
        Paragraph("TDEC's own directory lists <b>eight</b> Environmental Field "
                  "Offices. The septic application form, <b>CN-0971</b>, routes "
                  "to <b>seven</b>. We are not going to print a "
                  "county-to-office table when the two published sources "
                  "disagree, because the form's own instruction settles it: "
                  "<i>\"MAIL YOUR APPLICATION AND FEE TO THE OFFICE ASSOCIATED "
                  "WITH YOUR COUNTY SHOWN ON THE NEXT PAGE.\"</i> Page 2 of the "
                  "form you download is the map that governs.", S["body"]),
        Paragraph("<b>Two counties run their own environmental health septic "
                  "programs</b> rather than going through a field office: "
                  "Blount and Sevier. And Hardeman is split — its septic work "
                  "goes to one office and its other water matters to another.",
                  S["body"]),
    ]))

# ---------------------------------------------------------------- addresses
flow += k.h2_tight("STATE-LEVEL ADDRESSES", reserve=2.0)
flow.append(k.body(
    "All confirmed to resolve in September 2026. <b>We print no phone numbers "
    "anywhere in this kit</b> — they go stale faster than anything else on a "
    "printed page, and every office below can be reached from its own site."))
rows = [
    [k.cellp("<b>Your jurisdiction's status</b>"),
     k.cellp("tn.gov/commerce/fire/residential-permits/"
             "jurisdictions-inspectors.html")],
    [k.cellp("<b>Buy a permit, book an inspection</b>"),
     k.cellp("core.tn.gov — the Comprehensive Online Regulatory and Enforcement "
             "System. This is the transactional system")],
    [k.cellp("<b>Check a contractor's license</b>"),
     k.cellp("verify.tn.gov — license verification search. <b>Not the same "
             "system as CORE</b>, and the two are widely confused")],
    [k.cellp("<b>State residential permit fees</b>"),
     k.cellp("tn.gov/commerce/fire/residential-permits/"
             "fire-residential-building-permit-fees.html")],
    [k.cellp("<b>Opt-out jurisdictions explained</b>"),
     k.cellp("tn.gov/commerce/fire/residential-permits/"
             "opt-out-jurisdictions.html")],
    [k.cellp("<b>Residential permit questions</b>"),
     k.cellp("tn.gov/commerce/fire/residential-permits/"
             "fire-residential-faqs.html")],
    [k.cellp("<b>Electrical permits</b>"),
     k.cellp("tn.gov/commerce/fire/permit/electrical.html")],
    [k.cellp("<b>Septic — field offices</b>"),
     k.cellp("tn.gov/environment/contacts/field-offices.html")],
    [k.cellp("<b>The rules themselves</b>"),
     k.cellp("publications.tnsosfiles.com — chapter 0780-02-23 residential, "
             "0780-02-01 electrical, 0400-48-01 septic")],
]
# 1.3in, not 2.05in. The label column is sized by the LONGEST URL in the right
# column, not by how the labels look: at 2.05in the fee address wrapped as
# "…/fire-residential-building-permit" + "-fees.html", which is a defect rather
# than an ugliness — anyone typing it in gets a 404, and check.py cannot see it
# because the fragment is neither short nor alphabetic.
#
# Measure at 9.5pt, NOT 9pt: these cells are Paragraphs in the "cell" style,
# which is 9.5pt, while the note style is 9. Getting that wrong is what made a
# first attempt at 1.6in look sufficient on paper and still wrap on the page.
# The widest address here is 392.6pt; 1.3in leaves 400.4pt. Labels may wrap.
flow.append(k.ref_table(
    "Verified September 2026",
    [k.cellp("What you need", bold=True), k.cellp("Where", bold=True)],
    rows, [1.3 * inch, CW - 1.3 * inch]))
flow.append(k.cite(
    "<b>Two addresses people mix up.</b> <i>verify.tn.gov</i> is where you "
    "check that a contractor holds a license in the right classification and "
    "within their monetary limit. <i>core.tn.gov</i> is where money changes "
    "hands: permits, licenses and inspection requests. They are different "
    "systems run for different purposes, and conflating them is common enough "
    "that Knox County's own homeowner affidavit points buyers explicitly to "
    "the verification search."))

# ---------------------------------------------------------------- write-in
flow += k.h2_tight("YOUR DIRECTORY — FILL THIS IN BEFORE YOU NEED IT",
                   reserve=1.6)
flow += k.check_table(
    "Every office that touches this build, confirmed and dated",
    [
        ("My jurisdiction status, and the date I read it off the state list:",
         [("City", 0.34), ("Status", 0.33), ("Date read", 0.33)]),
        ("If I am inside a city, the CITY's status separately — it may differ "
         "from the county's:", [("City status", 0.5), ("Date read", 0.5)]),
        ("Building permit office, and whether it is local or the state:",
         [("Office", 0.6), ("Local or state", 0.4)]),
        ("The code edition they review to. Ask — an exempt jurisdiction need "
         "only be within seven years of current:",
         [("Edition", 0.5), ("Confirmed with", 0.5)]),
        ("Electrical permit source, and whether my jurisdiction is on the "
         "state electrical exempt list:",
         [("Source", 0.6), ("Exempt?", 0.4)]),
        ("Septic: the TDEC field office my CN-0971 routes to, or my county's "
         "own environmental health office:", [("Office", 1.0)]),
        ("Zoning office, and whether zoning approval is needed before the "
         "building permit:", [("Office", 0.6), ("Needed?", 0.4)]),
        ("911 addressing office:", [("Office", 0.6), ("Address issued", 0.4)]),
        ("Floodplain administrator, and whether my parcel is in a mapped "
         "hazard area:", [("Office", 0.6), ("In or out", 0.4)]),
        ("Driveway or culvert permit — which road authority owns the road I "
         "touch:", [("Authority", 1.0)]),
        ("Electric utility or co-op, and what they need before setting a "
         "meter:", [("Utility", 0.5), ("Requires", 0.5)]),
        "I called Tennessee 811 before any excavation.",
    ])
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "tn-permit-kit",
                       "TN.4-where-to-file-directory.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
