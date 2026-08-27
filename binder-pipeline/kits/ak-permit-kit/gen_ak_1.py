#!/usr/bin/env python3
"""AK.1 Owner-Builder Exemption Walkthrough.

Every Alaska claim in this document was read out of the primary source in
August 2026 and is cited on-page. Statute text was read at akleg.gov (Alaska
Statutes 2025); regulations from the Alaska Administrative Code at the same
source.

Verified sources:
  AS 08.18.011(a)   registration required before working as a contractor
  AS 08.18.171(4)   "contractor" = a person who, IN THE PURSUIT OF AN
                    INDEPENDENT BUSINESS, undertakes ... — the threshold word
  AS 08.18.161(9)   exemption for work on an EXISTING STRUCTURE on your own
                    property, and on your own EXISTING RESIDENCE. This is the
                    remodel paragraph. It does NOT reach new construction —
                    the near-universal error in Alaska owner-builder writing
  AS 08.18.161(11)  the NEW-CONSTRUCTION exemption: owner acting as own
                    contractor; ONE building every two years; the for-sale
                    notice; and the definition of when construction BEGINS
  AS 08.18.161(8)   an owner who contracts with a registered contractor
  AS 08.18.116(b)   the department SHALL investigate a filed (11) notice
  AS 08.18.025      residential contractor endorsement — required of the
                    GENERAL CONTRACTOR, not of the owner; arctic coursework
  AS 08.18.071      bond amounts; AS 08.18.101 insurance minimums
  AS 08.18.151      an unregistered contractor may not sue to collect — the
                    provision that protects the owner
  AS 08.18.125      administrative fine $1,000 / $1,500, and (e) the remote
                    community carve-out
  AS 08.18.131      civil penalty up to $1,000, each day a separate violation
  AS 08.18.141      class B misdemeanor on a repeat knowing violation
  AS 08.40.190(b)(3),(c)  homeowner ELECTRICAL exclusion — owned by installer
                    or immediate family, not intended for sale; and (c), which
                    keeps the department's regulations applying
  AS 08.40.390(b)(3) mechanical exclusion — 1- or 2-family residence not
                    intended for sale. NOTE: no ownership condition, and no
                    subsection (c). The asymmetry is real; do not flatten it
  AS 08.40.190(b)(2) / 08.40.390(b)(2)  the remote thresholds differ by an
                    order of magnitude: $5,000 / pop. 500 for electrical,
                    $50,000 / pop. 5,000 for mechanical
  AS 18.60.715(c)   "Nothing ... prohibits a person from performing plumbing
                    work on the person's own property" — unconditional
  AS 18.62.010/.070 certificate of fitness. NOTE the correction below.
  12 AAC 21.650(a)  16 contact hours of continuing competency — this is the
                    RENEWAL requirement, and it is the true source of the
                    "16-hour course" figure that guides misattribute to the
                    ENTRY course. AS 08.18.025(b)(4) sets no hour count.
  12 AAC 21.680(3)  the only exam standard in law is a 70 percent passing
                    score. The widely-quoted "50-question exam" is unsourced.

CORRECTION APPLIED AFTER FIRST DRAFT — the certificate of fitness. An earlier
draft rested on AS 18.62.010's word "employed," reasoning that an owner
working on their own house is not employed and so is outside the scheme. That
reading is weaker than it looks: the implementing regulation drops the word.
8 AAC 90.105(a) requires a certificate of "an individual ENGAGED IN THE
PERFORMANCE OF WORK subject to the standards established in AS 18.60.580 and
AS 18.60.705." The operative mechanism is SCOPE, not employment — the
electrical program reaches only "public structures" and places of employment
(8 AAC 70.010), and the plumbing chapter exempts communities under 2,500
(AS 18.60.735) and preserves work on your own property (AS 18.60.715(c)).
There is NO express homeowner exemption from the certificate of fitness; the
regulations were searched for one and contain none. Note also the regulations
live at 8 AAC 90, not 8 AAC 60.

Deliberately NOT claimed: that AS 08.18.161(9) is the exemption a new-build
owner relies on; that the two-year limit or the for-sale notice appears in
(9); that AS 08.40.190 covers mechanical work (it is the electrical article —
mechanical is AS 08.40.390); that the $5,000 / population-500 remote threshold
applies to anything but electrical; that a homeowner is expressly exempt from
the certificate of fitness; that the endorsement entry course is 16 hours or
its exam 50 questions.
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

FORM_ID = "AK.1"
FORM_TITLE = "Owner-Builder Exemption Walkthrough"
TOPIC = "Exemption & Qualification"

flow = []
flow += k.header(
    FORM_ID, FORM_TITLE,
    "Which of Alaska's twelve exemptions you actually build under — most "
    "guides name the wrong one — the two-year conditions attached to it, and "
    "the trade rules that are not waived with it.")

flow.append(k.disclaimer(
    "Statute text was read at akleg.gov in August 2026 against the Alaska "
    "Statutes 2025 compilation; statutes change."))
flow.append(Spacer(1, 10))

# ---------------------------------------------------------------- short version
flow += k.h2_tight("THE SHORT VERSION")
flow.append(k.body(
    "Alaska has <b>no general contractor license</b> and no license "
    "examination. What it has is <b>registration</b>: a person may not work "
    "as a contractor until the Department of Commerce, Community, and "
    "Economic Development has issued a certificate of registration. Building "
    "your own house is not that — but the reason it is not that matters, "
    "because Alaska writes its exemption as a list of twelve numbered "
    "paragraphs, and <b>a new house and a remodel come under different "
    "paragraphs with different conditions.</b>"))
flow.append(k.cite(
    "AS 08.18.011(a) and AS 08.18.161, Alaska Statutes, Title 8, Chapter 18 "
    "(Construction Contractors). Read at akleg.gov, August 2026."))

rows = [
    [k.cellp("Is there a license exam?"),
     k.cellp("<b>No.</b> Alaska registers contractors; it does not license "
             "them by examination the way most states do. There is no "
             "general contractor exam to be exempted from")],
    [k.cellp("Is there a project-cost threshold?"),
     k.cellp("<b>No.</b> Nothing in the exemption is keyed to the value of "
             "your house. Bond amounts are keyed to project value — but "
             "those are a <i>registered contractor's</i> obligation, not "
             "yours")],
    [k.cellp("Must you own the land?"),
     k.cellp("For a new house, yes — the paragraph you rely on is written "
             "for \"<i>an owner who acts as the owner's own contractor</i>\"")],
    [k.cellp("Must you live in it?"),
     k.cellp("<b>The statute does not say so.</b> Alaska conditions the "
             "exemption on <i>frequency</i> and on <i>selling</i>, not on "
             "occupancy — which is unusual, and cuts in your favor")],
    [k.cellp("How often may you do it?"),
     k.cellp("<b>Once every two years.</b> One home, duplex, triplex, "
             "four-plex, or commercial building. This is a real, printed "
             "limit and most states have no equivalent")],
    [k.cellp("Can you sell it?"),
     k.cellp("Yes — but advertising or selling it during construction or "
             "within two years of the <b>start</b> triggers a notice you "
             "must file, and an investigation the department <i>shall</i> "
             "conduct")],
    [k.cellp("Can you do your own wiring, plumbing and heating?"),
     k.cellp("Largely yes, under <b>three separate exclusions in two "
             "different statutes</b>, each with its own test. None of them "
             "comes with the contractor exemption")],
]
flow.append(k.ref_table(
    "The exemption at a glance",
    [k.cellp("Question", bold=True), k.cellp("Alaska's answer", bold=True)],
    rows, [2.5 * inch, CW - 2.5 * inch]))

# ---------------------------------------------------------------- (9) vs (11)
flow += k.h2_tight("THE PARAGRAPH ALMOST EVERYONE CITES IS THE WRONG ONE")
flow.append(k.body(
    "Search for the Alaska owner-builder exemption and you will be given "
    "<b>AS 08.18.161</b> — correct — and then a paraphrase of paragraph "
    "<b>(9)</b>, usually rendered as \"a person performing work on that "
    "person's own property.\" Read the actual words:"))

flow.append(k.callout("What paragraph (9) really says", [
    Paragraph("The chapter does not apply to \"<i>a person working on an "
              "<b>existing structure</b> on that person's own property, "
              "whether occupied by the person or not, and a person working "
              "on that person's <b>own existing residence</b>, whether owned "
              "by the person or not</i>.\" (AS 08.18.161(9))", S["body"]),
    Paragraph("<b>Existing.</b> Twice. Paragraph (9) is the <b>remodel and "
              "repair</b> paragraph — it is what lets you re-roof your "
              "cabin, or renovate the house you rent. A bare lot has no "
              "existing structure on it, so (9) does nothing for a new "
              "house. Every summary that offers (9) as <i>the</i> "
              "owner-builder exemption has quietly dropped the word that "
              "decides the question.", S["body"]),
]))

flow.append(Spacer(1, 6))
flow.append(k.body(
    "The paragraph that lets you <b>build a new house</b> is <b>(11)</b>, "
    "and it is a single 200-word sentence carrying every condition Alaska "
    "imposes on an owner-builder. It is reproduced in full below because no "
    "paraphrase of it is safe."))

flow.append(k.callout_long(
    "Paragraph (11) — the new-construction exemption, in full", [
        # Split into three paragraphs at the statute's own semicolons. The
        # quote is one 200-word sentence; as a single flowable it exceeds
        # what remains on any page it starts near the foot of, and
        # callout_long's NOSPLIT on (title, first paragraph) then throws the
        # whole box to the next page. Three paragraphs let it break.
        Paragraph("The chapter does not apply to \"<i>an owner who acts as "
                  "the owner's own contractor and in doing so performs the "
                  "work independently or hires workers or subcontractors, "
                  "purchases materials, and, as such, sees to the paying for "
                  "all labor, subcontractors, and materials; in this case, "
                  "<b>the owner shall be limited to construction of one "
                  "home, duplex, triplex, four-plex, or commercial building "
                  "every two years</b>;</i>", S["body"]),
        Paragraph("<i>an owner who advertises the structure under "
                  "construction for sale or sells the structure during the "
                  "period of construction or within two years after the "
                  "period of construction begins <b>shall file, on forms "
                  "provided by the department, a notice</b> indicating that "
                  "the owner is not engaged in a business for which the "
                  "owner is required to register as a contractor under this "
                  "chapter;</i>", S["body"]),
        Paragraph("<i>for the purposes of this paragraph, <b>construction "
                  "begins on the date that is the earlier of</b> when the "
                  "owner (A) begins the actual construction work; or (B) "
                  "enters into an agreement with another person for the "
                  "other person to provide labor, to act as a "
                  "subcontractor, or to provide materials for the "
                  "construction</i>.\" (AS 08.18.161(11))", S["body"]),
        Paragraph("Read what it does <b>not</b> require. It does not require "
                  "you to occupy the house. It does not require the "
                  "structure to be a residence at all — a commercial "
                  "building is named in the same breath. It does not bar you "
                  "from hiring subcontractors; it expressly contemplates "
                  "that you will. And it does not forbid you to sell. What "
                  "it does is cap you at <b>one building every two "
                  "years</b> and attach a filing duty to selling early.",
                  S["body"]),
    ]))
flow.append(k.cite(
    "AS 08.18.161(9) and (11), quoted verbatim. The full section lists "
    "twelve exemptions; (8) also exempts \"an owner who contracts for a "
    "project with a registered contractor,\" which is the paragraph you rely "
    "on for the parts of the job you hand to a registered firm. Read at "
    "akleg.gov, August 2026."))

# ---------------------------------------------------------------- the clock
flow += k.h2_tight("THE TWO-YEAR CLOCK STARTS EARLIER THAN YOU THINK")
flow.append(k.body(
    "The for-sale window runs for two years \"<i>after the period of "
    "construction <b>begins</b></i>\" — not after it ends, and not from the "
    "certificate of occupancy. And the statute defines the start date for "
    "you, at the <b>earlier</b> of two events: the day you begin actual "
    "construction work, or the day you <b>enter into an agreement with "
    "another person to provide labor, to act as a subcontractor, or to "
    "provide materials</b>."))
flow.append(k.body(
    "Signing an excavation contract in March and breaking ground in June "
    "means the clock started in March. On a house that takes fourteen months "
    "to finish, you are already ten months into the window on the day you "
    "move in. That is worth knowing in both directions: it is a shorter "
    "window than people assume, and it is <b>the one date in this kit worth "
    "writing down on the day it happens.</b>"))
flow.append(Spacer(1, 4))
flow.append(d.FillInRow([("Earlier of first work / first agreement — date:", 0.6),
                         ("Two-year window ends:", 0.4)]))
flow.append(Spacer(1, 6))

flow.append(k.callout_long(
    "What filing the notice actually sets in motion", [
    Paragraph("If you advertise or sell inside that window, the notice is "
              "not a formality you file and forget. The statute that "
              "receives it is directive: \"<i>If an owner files a notice of "
              "the advertisement of a structure for sale or the sale of a "
              "structure during the period of construction or for two years "
              "after the period of construction begins under AS "
              "08.18.161(11), the department <b>shall investigate</b> and "
              "take appropriate action under this chapter if the notice and "
              "circumstances indicate that the owner is operating a business "
              "for which the owner is required to register as a "
              "contractor</i>.\" (AS 08.18.116(b))", S["body"]),
    Paragraph("So the test is not the sale itself — it is whether the "
              "circumstances show you were running a contracting business. "
              "The definition the department is measuring you against is "
              "narrow and helpful: a \"contractor\" is a person who acts "
              "\"<b><i>in the pursuit of an independent business</i></b>\" "
              "(AS 08.18.171(4)). One house, sold because a job moved or a "
              "marriage ended, is not an independent business. A second "
              "house inside two years starts to look like one — which is "
              "exactly why the frequency cap and the notice sit in the same "
              "sentence.", S["body"]),
    Paragraph("<b>Keep the evidence while it is cheap.</b> Your reason for "
              "selling, in writing and dated. The listing history. Proof "
              "this is the only structure you have built in the period. "
              "Assembling that two years later, from memory, is how a "
              "defensible position becomes an expensive one.", S["body"]),
]))

# ---------------------------------------------------------------- trades
flow += k.h2_tight("THE TRADES ARE A SEPARATE QUESTION — AND A SEPARATE TITLE")
flow.append(k.body(
    "Qualifying under AS 08.18.161(11) exempts you from <b>contractor "
    "registration</b>. It says nothing about whether you may wire, plumb or "
    "heat the house yourself. Those live in different chapters, they are "
    "worded differently from each other, and the differences are not "
    "cosmetic."))

trade_rows = [
    [k.cellp("<b>Electrical</b>"),
     k.cellp("Excluded: \"<i>electrical installation on residential property "
             "that is <b>owned by the installer or a member of the "
             "installer's immediate family</b> and <b>not intended for sale "
             "at the time of making the installation</b></i>.\" Two "
             "conditions — ownership and not-for-sale — and both must hold "
             "when the work is done."),
     k.cellp("AS 08.40.190(b)(3)")],
    [k.cellp("<b>Mechanical</b><br/>(heating, gas, plumbing systems)"),
     k.cellp("Excluded: \"<i>mechanical installation on a <b>single-family "
             "residence or a two-family residence that is not intended for "
             "sale</b> at the time of making the installation</i>.\" Note "
             "what is <b>missing</b>: no ownership condition at all, and it "
             "is capped at two dwelling units."),
     k.cellp("AS 08.40.390(b)(3)")],
    [k.cellp("<b>Plumbing</b><br/>(the state plumbing code)"),
     k.cellp("The broadest of the three, and unconditional: \"<i>Nothing in "
             "AS 18.60.705 — 18.60.740 <b>prohibits a person from "
             "performing plumbing work on the person's own property</b></i>.\" "
             "No not-for-sale clause, no occupancy clause."),
     k.cellp("AS 18.60.715(c)")],
]
flow.append(k.ref_table(
    "Doing your own trade work — three exclusions, three different tests",
    [k.cellp("Trade", bold=True),
     k.cellp("What the statute actually says", bold=True),
     k.cellp("Authority", bold=True)],
    trade_rows, [1.35 * inch, CW - 1.35 * inch - 1.35 * inch, 1.35 * inch]))

flow.append(Spacer(1, 6))
flow.append(k.callout_long(
    "The asymmetry no Alaska guide prints — and the remote thresholds that "
    "differ tenfold", [
        Paragraph("Guides routinely cite <b>AS 08.40.190</b> for \"electrical "
                  "and mechanical\" homeowner work. AS 08.40.190 is in the "
                  "<b>electrical administrator</b> article and reaches "
                  "electrical work only. The mechanical exclusion is a "
                  "different section — <b>AS 08.40.390</b> — in a different "
                  "article, and it is worded differently in a way that "
                  "matters: <b>the electrical exclusion requires you to own "
                  "the property; the mechanical one does not.</b>",
                  S["body"]),
        Paragraph("The same two sections carry a remote-community exclusion, "
                  "and the numbers are <b>an order of magnitude apart.</b> "
                  "Electrical: work costing not more than <b>$5,000</b>, in "
                  "a community of under <b>500</b> people or more than 50 "
                  "miles by air or water from a licensed electrical "
                  "administrator (AS 08.40.190(b)(2)). Mechanical: work "
                  "costing not more than <b>$50,000</b>, in a community of "
                  "under <b>5,000</b> people or the same 50-mile test "
                  "(AS 08.40.390(b)(2)). A single figure quoted for \"trade "
                  "work\" in remote Alaska is wrong for one of the two "
                  "trades, whichever figure it is.", S["body"]),
    ]))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "And an exclusion from the license is not an exclusion from the code",
    [
        Paragraph("The electrical article says so in terms: work within the "
                  "exclusions \"<i>is nevertheless subject to the inspection "
                  "provisions of AS 08.40.070 and <b>must follow the "
                  "regulations adopted by the department, other than "
                  "regulations requiring licensure for the work</b></i>.\" "
                  "(AS 08.40.190(c)) The regulation you must follow is "
                  "<b>8 AAC 70.025(a)</b> — the <b>2020 edition of NFPA 70, "
                  "the National Electrical Code</b>, which \"constitutes the "
                  "minimum electrical code for the state.\"", S["body"]),
        Paragraph("And it has teeth that survive the absence of an "
                  "inspector. A person who <b>knowingly</b> violates \"<i>a "
                  "minimum electrical standard established under AS 18.60.580 "
                  "— 18.60.590</i>\" is guilty of a misdemeanor punishable by "
                  "a fine of <b>not more than $5,000</b> (AS 08.40.180). "
                  "There is no comparable exemption from the plumbing side "
                  "either: the state's minimum plumbing standards \"<i>are "
                  "to be followed <b>throughout the state</b></i>\" "
                  "(8 AAC 63.010(a)). See <b>AK.2</b> for which of these is "
                  "actually inspected where you are building — the answer "
                  "surprises people.", S["body"]),
    ]))
flow.append(k.cite(
    "AS 08.40.190(b)(2), (b)(3), (c); AS 08.40.390(b)(2), (b)(3); "
    "AS 08.40.180; AS 18.60.715(c); 8 AAC 70.025(a); 8 AAC 63.010(a). Note "
    "that AS 08.40.390 has <b>no subsection (c)</b> — the "
    "\"still-follow-the-regulations\" sentence appears in the electrical "
    "article only. Statutes and regulations read at akleg.gov, August 2026."))

flow.append(Spacer(1, 6))
flow += k.h2_tight("THE CERTIFICATE OF FITNESS — WHY IT DOES NOT REACH YOU")
flow.append(k.body(
    "Alaska requires a <b>certificate of fitness</b> to do electrical or "
    "plumbing work, and this is where most descriptions of Alaska law go "
    "wrong in a way that frightens owner-builders off work they are entitled "
    "to do. There is <b>no express homeowner exemption</b> from the "
    "certificate of fitness. Searching the whole certificate-of-fitness "
    "statute and its regulations for \"homeowner,\" \"own residence\" or "
    "\"single-family\" returns nothing at all."))
flow.append(k.body(
    "What protects you is not an exemption — it is <b>scope</b>. Both "
    "AS 18.62.010 and AS 18.62.070 attach the duty only to work \"<i>subject "
    "to the standards established in AS 18.60.580 and AS 18.60.705</i>.\" So "
    "the question is never \"am I exempt?\" It is \"<b>is my work inside "
    "either program in the first place?</b>\" And for a detached "
    "single-family house the answer is largely no:"))
flow.append(k.bullet(
    "<b>Electrical.</b> The program is limited by 8 AAC 70.010 to "
    "\"<i>public structures</i>\" and places of employment, and a \"public "
    "structure\" is defined as buildings such as hotels, <b>resident housing "
    "with more than one rental unit</b>, restaurants and places of public "
    "assembly. The Department describes its own reach as three-plex and "
    "above. Your house is outside it — and note the trigger is the "
    "<b>building type, not the location</b>: a four-plex in the unorganized "
    "borough is inside the program even though nothing else there is."))
flow.append(k.bullet(
    "<b>Plumbing.</b> Two independent limits. Communities under 2,500 "
    "population are exempt from the chapter outright (AS 18.60.735), and "
    "above that line AS 18.60.715(c) still says \"<i>Nothing … prohibits a "
    "person from performing plumbing work on the person's own property</i>.\" "
    "That is a genuine statutory homeowner right, and it is the only one of "
    "the three trades that has one in those terms."))
flow.append(k.callout(
    "One caution on the regulation, because it is stricter than the statute",
    [
        Paragraph("If you go looking, you will find that AS 18.62.010 frames "
                  "the duty around being \"<i>employed</i>\" — which reads "
                  "as though an owner working on their own house is outside "
                  "it by definition. <b>Do not rest on that reading.</b> The "
                  "implementing regulation drops the word: 8 AAC 90.105(a) "
                  "requires a certificate of \"<i>an individual <b>engaged in "
                  "the performance of work</b> subject to the standards "
                  "established in AS 18.60.580 and AS 18.60.705</i>.\"",
                  S["body"]),
        Paragraph("So the employment argument is weaker than it looks, and "
                  "the scope argument above is the one that actually holds. "
                  "It is still worth one phone call to the Mechanical "
                  "Inspection Section before you start — write down what you "
                  "are told, and by whom.", S["body"]),
    ]))
flow.append(Spacer(1, 4))
flow.append(d.FillInRow([("Confirmed with:", 0.4), ("Date:", 0.25),
                         ("What you were told:", 0.35)]))
flow.append(k.cite(
    "AS 18.62.010; AS 18.62.070; 8 AAC 90.105(a) — the certificate-of-"
    "fitness regulations are in <b>8 AAC 90</b>; 8 AAC 70.010 and "
    "8 AAC 70.090(4); AS 18.60.735; AS 18.60.715(c). Penalty for working "
    "without a required certificate is a fine of not more than $500 "
    "(AS 18.62.080)."))

# ---------------------------------------------------------------- hiring
flow += k.h2_tight("WHEN YOU HIRE — WHAT TO CHECK, AND WHAT PROTECTS YOU")
flow.append(k.body(
    "Your exemption is yours. It does not travel to the people you pay. "
    "Anyone working as a contractor on your job needs their own "
    "registration, and for a house there is a second layer most owners never "
    "hear about."))
flow.append(k.body(
    "<b>The residential contractor endorsement.</b> A general contractor "
    "\"<i>may not undertake the construction or alteration ... of a "
    "privately-owned residential structure of one to four units</i>\" "
    "without a <b>residential contractor endorsement</b> — and \"alteration\" "
    "means changes worth more than <b>25 percent</b> of the value of the "
    "structure. To hold it, a contractor must pass an examination that "
    "\"<i>may test competence in relation to <b>arctic structural and "
    "thermal construction techniques</b></i>\" and, within the two years "
    "before applying, must have completed \"<i>the Alaska craftsman home "
    "program sponsored by the department, or its equivalent, or a "
    "<b>postsecondary course in arctic engineering</b>, or its "
    "equivalent</i>.\" Renewal requires proof of continued competency."))
flow.append(k.body(
    "You do not need it — the endorsement attaches to the general "
    "contractor, and you are exempt from the chapter that creates it. But "
    "<b>the contractor you hire to frame your house does</b>, and it is a "
    "one-minute check. It is also the clearest statement Alaska makes about "
    "its own climate: the state considers cold-climate housing a distinct "
    "competency and makes professionals prove it. Nothing forces you to "
    "learn it. Everything about the building does."))
flow.append(k.callout(
    "The \"16-hour course\" you will read about is the renewal, not the entry",
    [
        Paragraph("Guides state that the endorsement takes \"a 16-hour "
                  "course and a 50-question exam.\" Neither figure is in the "
                  "law. AS 08.18.025(b)(4) sets <b>no hour count</b> for the "
                  "entry course — it names the Alaska craftsman home program "
                  "or a postsecondary arctic engineering course \"<i>or its "
                  "equivalent</i>.\" The real 16 is the <b>renewal</b> "
                  "requirement: 12 AAC 21.650(a) calls for <b>16 contact "
                  "hours</b> of continuing competency every two years. And "
                  "the only examination standard in the regulations is a "
                  "<b>passing score of 70 percent</b> (12 AAC 21.680(3)) — "
                  "no question count appears anywhere.", S["body"]),
        Paragraph("It matters because it is the kind of detail a contractor "
                  "will quote at you to sound authoritative. Ask instead for "
                  "the two things that are checkable: the endorsement on the "
                  "state license search, and a current <b>Alaska business "
                  "license</b>, which is a separate requirement from "
                  "contractor registration and which people do let lapse.",
                  S["body"]),
    ]))
flow.append(k.cite(
    "AS 08.18.025(a), (b)(2), (b)(4), (c); 12 AAC 21.650(a); 12 AAC "
    "21.680(3). Registration verification is free at "
    "<b>commerce.alaska.gov</b> → Division of Corporations, Business and "
    "Professional Licensing → Search Licenses. Search by name or license "
    "number and read the status line, the endorsement, and the expiry date."))

flow.append(Spacer(1, 4))
flow.append(k.callout(
    "The provision that protects you when a contractor is not registered", [
        Paragraph("\"<i>A person acting in the capacity of a contractor ... "
                  "<b>may not bring an action in a court of this state for "
                  "the collection of compensation</b> for the performance of "
                  "work or for breach of a contract for which registration "
                  "is required under this chapter <b>without alleging and "
                  "proving</b> that the contractor ... was a registered "
                  "contractor at the time of contracting</i>.\" "
                  "(AS 08.18.151)", S["body"]),
        Paragraph("An unregistered contractor cannot sue you for the "
                  "balance. That is a genuine remedy and it is worth knowing "
                  "before a dispute rather than during one — but it is a "
                  "poor substitute for checking the registration first, "
                  "because it does nothing about the bad work itself. A "
                  "registered contractor also carries a bond you could claim "
                  "against: <b>$25,000</b> for a general contractor, "
                  "<b>$20,000</b> for one with a residential endorsement "
                  "doing exclusively residential work, <b>$10,000</b> for a "
                  "mechanical or specialty contractor, and liability cover "
                  "of at least $20,000 property damage and $50,000 per "
                  "person. An unregistered one carries none of it.",
                  S["body"]),
    ]))
flow.append(k.cite("AS 08.18.151; AS 08.18.071(b)(1)–(3); AS 08.18.101(a)(2)."))

# ---------------------------------------------------------------- checklist
flow += k.h2_tight("QUALIFICATION CHECKLIST — WORK THIS BEFORE YOU START")
flow.append(k.body(
    "Every line below is a condition Alaska law imposes or a fact worth "
    "fixing in writing at the time it is cheap to fix. Work down it with a "
    "pen."))

flow += k.check_table("Step 1 — The exemption you are relying on", [
    "You have identified the paragraph: <b>AS 08.18.161(11)</b> for a new "
    "structure, <b>(9)</b> only for work on something already standing",
    ("You have <b>not</b> built a home, duplex, triplex, four-plex, or "
     "commercial building under this exemption within the past two years",
     [("Last such build (or NONE):", 1.0)]),
    ("You have recorded the date construction <b>begins</b> — the earlier of "
     "first actual work and first agreement for labor, subcontracting, or "
     "materials", [("Date:", 0.5), ("Which event:", 0.5)]),
    "You understand the for-sale window runs <b>two years from that date</b>, "
    "not from completion",
    "If any sale or advertising is contemplated inside that window, you have "
    "the department's notice form and know that AS 08.18.116(b) requires an "
    "investigation once it is filed",
    "You own the property, or the ownership is settled, before you begin",
], notes_header="Notes / evidence")

flow += k.check_table("Step 2 — The trade exclusions you are relying on", [
    "<b>Electrical:</b> the property is owned by you or an immediate family "
    "member <i>and</i> is not intended for sale at the time you do the work "
    "— both conditions, AS 08.40.190(b)(3)",
    "<b>Mechanical:</b> it is a single-family or two-family residence not "
    "intended for sale at the time of installation — AS 08.40.390(b)(3)",
    "<b>Plumbing:</b> the work is on your own property — AS 18.60.715(c)",
    "You have confirmed whether your community is at or above the "
    "<b>2,500 population</b> line that brings the state plumbing code and "
    "state plumbing inspection into play (AK.2 and AK.4)",
    "You have the correct code editions in hand before buying material: "
    "<b>2020 NEC</b> and <b>2018 UPC</b> statewide, or your local "
    "jurisdiction's editions if it enforces its own",
    ("For any trade you will not do yourself, the contractor is registered — "
     "and holds the residential endorsement if they are the general "
     "contractor", [("Verified on:", 0.5), ("Registration no.:", 0.5)]),
], notes_header="Notes / evidence")

flow.append(k.body(
    "<b>Step 3 — everything that is actually required of the building</b> "
    "(wastewater, water, access, floodplain, wetlands, the statewide rules "
    "that apply with or without a permit, and the lender's requirements) is "
    "worked in <b>AK.2 Permit Application Checklist</b>. Who to file each "
    "one with is <b>AK.4</b>."))

# ---------------------------------------------------------------- penalties
flow += k.h2_tight("WHAT IT COSTS TO GET THIS WRONG")
flow.append(k.body(
    "None of this reaches a genuine owner-builder — you are exempt, so there "
    "is no offense. It is here because the numbers show where Alaska draws "
    "the line, and because the last one is a piece of Alaska in miniature."))
flow.append(k.bullet(
    "<b>Administrative fine.</b> The department may impose \"<i>not more "
    "than $1,000 for the first violation and not more than $1,500 for a "
    "second or subsequent violation</i>\" of the registration requirement or "
    "the residential endorsement requirement. (AS 08.18.125(a))"))
flow.append(k.bullet(
    "<b>Civil penalty and injunction.</b> The superior court may enjoin "
    "unregistered contracting and \"<i>may impose a civil penalty of not "
    "more than $1,000 for each violation. <b>Each day that an unlawful act "
    "continues constitutes a separate violation.</b></i>\" "
    "(AS 08.18.131)"))
flow.append(k.bullet(
    "<b>Criminal, but only on repeat.</b> Unregistered contracting is a "
    "<b>class B misdemeanor</b> only where the person knowingly violates the "
    "registration or endorsement requirement <i>and</i> has previously been "
    "convicted, found guilty, or fined for the same thing. A first offense "
    "is a violation punishable under Title 12. (AS 08.18.141(a), (b))"))
flow.append(Spacer(1, 4))
flow.append(k.callout_long("The carve-out that only Alaska would write", [
    Paragraph("\"<i>The department <b>may not impose an administrative "
              "fine</b> on a person who is acting as a contractor or home "
              "inspector in an area with a <b>population of 1,000 or less "
              "that is not connected by road or rail to Anchorage or "
              "Fairbanks</b>.</i>\" (AS 08.18.125(e))", S["body"]),
    Paragraph("The Legislature wrote the road system into the penalty "
              "provision. It is a useful reminder of how this state "
              "actually regulates construction: not by drawing lines on a "
              "map of boroughs, but by asking how big the community is and "
              "whether you can drive to it. You will see the same logic "
              "again in the plumbing code's 2,500-person threshold and in "
              "the trade exclusions' 500- and 5,000-person tests. "
              "<b>In Alaska, population and access are the code map.</b>",
              S["body"]),
]))

# ---------------------------------------------------------------- sources
flow.append(Spacer(1, 12))
flow.append(k.sources_table([
    ("Registration, not licensure, and only for a person acting \"in the "
     "pursuit of an independent business\"",
     "AS 08.18.011(a); 08.18.171(4)"),
    ("Paragraph (9) reaches an EXISTING structure or existing residence — "
     "remodels and repairs, not a new house", "AS 08.18.161(9)"),
    ("Paragraph (11) is the new-construction exemption: one building every "
     "two years; notice on advertising or selling within two years of the "
     "start; construction begins at the earlier of first work or first "
     "agreement for labor, subcontracting or materials",
     "AS 08.18.161(11)"),
    ("Once that notice is filed the department shall investigate whether the "
     "owner is operating a contracting business", "AS 08.18.116(b)"),
    ("Residential contractor endorsement for 1–4 unit residential work; "
     "\"alteration\" is a change worth more than 25% of value; arctic "
     "coursework and continued competency", "AS 08.18.025(a), (b), (c)"),
    ("An unregistered contractor may not sue to collect; registered "
     "contractors carry a $25,000 / $20,000 / $10,000 bond and stated "
     "liability minimums",
     "AS 08.18.151; 08.18.071(b); 08.18.101(a)"),
    ("Penalties: $1,000 / $1,500 administrative, $1,000 civil per day, class "
     "B misdemeanor only on repeat — and no administrative fine off the road "
     "system in a community of 1,000 or less",
     "AS 08.18.125(a), (e); 08.18.131; 08.18.141"),
    ("Homeowner electrical exclusion requires ownership AND not-for-sale; "
     "mechanical requires only a 1- or 2-family residence not for sale; "
     "plumbing on your own property is unconditional",
     "AS 08.40.190(b)(3); 08.40.390(b)(3); AS 18.60.715(c)"),
    ("Remote-community exclusions differ tenfold: $5,000 / pop. 500 "
     "electrical, $50,000 / pop. 5,000 mechanical",
     "AS 08.40.190(b)(2); 08.40.390(b)(2)"),
    ("Exclusion from licensure is not exclusion from the code; the 2020 NEC "
     "is the state minimum electrical code and knowing violation is a "
     "misdemeanor up to $5,000",
     "AS 08.40.190(c); 08.40.180; 8 AAC 70.025(a)"),
]))
flow.append(k.closing_note())


if __name__ == "__main__":
    out = os.path.join(_HERE, "out", "ak-permit-kit",
                       "AK.1-owner-builder-exemption.pdf")
    k.build(out, FORM_ID, FORM_TITLE, TOPIC, flow)
    print(f"built {out}")
