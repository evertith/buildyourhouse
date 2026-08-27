# Alaska Owner-Builder Dossier — research for the AK Permit Kit (six documents)

Compiled August 2026. Statute text was read from the OFFICIAL Alaska Statutes (2025 compilation) and the OFFICIAL
Alaska Administrative Code, both published by the Alaska Legislature at akleg.gov. The fetch pattern that works —
the public pages are JavaScript shells, but their AJAX endpoint returns plain HTML:

    https://www.akleg.gov/basis/statutes.asp?media=print&type=fetch&secStart=08.18.011
    https://www.akleg.gov/basis/aac.asp?media=print&type=fetch&secStart=13.50.010

`secStart` returns that section and everything after it, in chunks of roughly 50–60k characters, so fetch from a
section *before* the one you want. The response is **cp1252, not utf-8** — decode accordingly or you get a
UnicodeDecodeError on the section-symbol character. Agency facts were read from the administering agencies' own
pages. Every claim is tagged:

  [V] = verified against a primary source (statute or regulation text read directly, or the administering
  agency's own page). Safe to print with the citation.
  [H] = hedge — could not be pinned to a primary source, is locally variable, or is a proven-negative that can
  only be stated carefully. Print only with the hedge language and a verification step.

WARNING FOR FUTURE EDITORS — FOUR CITATION MINEFIELDS. Alaska's live law is scattered across four titles and the
secondary sources get it wrong consistently and in the same ways.

  1. **AS 08.18.161(9) is NOT the new-construction exemption.** It reaches "a person working on an **existing
     structure** on that person's own property … and a person working on that person's **own existing
     residence**." Both clauses say *existing*. It is the remodel-and-repair paragraph. The new-house exemption
     is **AS 08.18.161(11)**, and it carries conditions (9) does not. Essentially every Alaska owner-builder
     summary online, including the live state guide, quotes (9) and then attributes (11)'s two-year rules to it.
  2. **AS 08.40.190 is the ELECTRICAL article only.** It sits in AS 08.40.005 — 08.40.200 (electrical
     administrators). The mechanical exclusion is **AS 08.40.390**, in AS 08.40.210 — 08.40.490. They are worded
     differently in ways that matter (see item 9). Guides routinely cite AS 08.40.190 for "electrical and
     mechanical."
  3. **AS 18.60.705 names the 1997 UPC on its face and is superseded by regulation.** The statute adopts the 1997
     Uniform Plumbing Code "unless the department adopts by regulation a later edition" — and the department did.
     **8 AAC 63.010(a)(1) adopts the 2018 UPC.** The statute is what a search engine surfaces; the regulation is
     what the inspector holds. Twenty-one years apart.
  4. **The Department of Labor's own printed compilations lag the live code.** Its "Electrical Safety Statutes and
     Regulations" booklet (May 2018, still linked from the live page in August 2026) prints 8 AAC 70.025 as
     adopting the **2017** NEC. The current AAC adopts the **2020** NEC. Read the AAC, not the booklet.

THE STRUCTURAL HEADLINE (this is the kit's thesis) — **ALASKA REGULATES BY POPULATION AND UNIT COUNT, NOT BY
JURISDICTION.** Every other state's kit answers "which government enforces on this parcel?" In Alaska that
question frequently has no answer, and asking it is a trap, because the rules that DO bind a house are drawn on
lines that have nothing to do with borough boundaries:

  - State Fire Marshal building standards: **four or more dwelling units** (AS 18.70.080(a)(2))
  - State electrical inspection: **public structures / three-plex and above** (8 AAC 70.010, 8 AAC 70.090(4))
  - State plumbing code and inspection: **communities of 2,500 population or more** (AS 18.60.735)
  - Smoke and CO alarms: **every dwelling unit in the state**, no threshold at all (AS 18.70.095)
  - Contractor administrative fines: **not available** in a community of 1,000 or less off the road system
    (AS 08.18.125(e))
  - Remote trade-work exclusions: **500 people / $5,000** electrical, **5,000 people / $50,000** mechanical

So the practical consequence, which no competing Alaska guide states: **an owner-builder in a Mat-Su or Interior
community over 2,500 people has no building department and still gets a State of Alaska plumbing inspection.**

---------------------------------------------------------------------------
## AK.0 — Cover summary facts

1. [V] No statewide residential building code, and the exclusion is statutory rather than a policy choice.
   AS 18.70.080(a)(2): the Department of Public Safety shall adopt regulations establishing minimum standards for
   "fire and life safety criteria in commercial, industrial, business, institutional, or other public buildings,
   and buildings used for residential purposes **containing four or more dwelling units**." The department has no
   authority below four units to begin with.

2. [V] The adopted code says so too. 13 AAC 50.020 adopts the **International Building Code 2021 Edition**, and
   revises Section 101.2's exception to read "Exceptions: 1. **Detached one-, two-, and three-family dwellings.**
   2. Multiple single-family dwellings (townhouses) not more than three stories above grade plane in height …"
   Note the Alaska-specific reach to *three* family dwellings, wider than the IBC's usual two.

3. [V] 13 AAC 50.020 also redirects the IBC's trade references: all references to "ICC Electrical Code" or
   "NFPA 70" are replaced with "Electrical Code as adopted by **8 AAC 70.025**," and references to the
   International Fuel Gas Code and International Plumbing Code with "Plumbing Code as adopted by **8 AAC
   63.010**." Those two regulations are where the live editions live.

4. [V] There is no Alaska equivalent of a statewide jurisdiction list. This was searched for and none exists —
   which is itself the finding, and is why AK.4 is a procedure rather than a table. The state never took the
   power to regulate one- to three-family dwellings, so it has nothing to delegate and keeps no register of which
   boroughs and cities have taken the power up on their own.

---------------------------------------------------------------------------
## AK.1 — The exemption, and the trade exclusions that do not come with it

5. [V] Registration, not licensure. AS 08.18.011(a): "A person may not submit a bid or work as a contractor until
   that person has been issued a **certificate of registration** as a contractor by the department." There is no
   general contractor licensing examination in Alaska.

6. [V] The threshold word is in the definition. AS 08.18.171(4): "'contractor' means a person who, **in the
   pursuit of an independent business**, undertakes or offers to perform, or claims to have the capacity to
   perform, or submits a bid for a project to construct, alter, repair, move, or demolish a building …" An owner
   building their own house is not pursuing an independent business. This is the definitional backstop behind
   both exemptions and it is worth citing alongside them.

7. [V] **AS 08.18.161(9) — the REMODEL paragraph.** The chapter does not apply to "a person working on an
   **existing structure** on that person's own property, whether occupied by the person or not, and a person
   working on that person's **own existing residence**, whether owned by the person or not." Note the second
   clause: it covers work on a residence you occupy but do not own — a tenant's own repairs. Neither clause
   reaches a bare lot.

8. [V] **AS 08.18.161(11) — the NEW-CONSTRUCTION paragraph, quoted in full in the kit.** The chapter does not
   apply to "an owner who acts as the owner's own contractor and in doing so performs the work independently or
   hires workers or subcontractors, purchases materials, and, as such, sees to the paying for all labor,
   subcontractors, and materials; in this case, **the owner shall be limited to construction of one home, duplex,
   triplex, four-plex, or commercial building every two years**; an owner who advertises the structure under
   construction for sale or sells the structure during the period of construction or **within two years after
   the period of construction begins** shall file, on forms provided by the department, a notice indicating that
   the owner is not engaged in a business for which the owner is required to register as a contractor under this
   chapter; for the purposes of this paragraph, **construction begins on the date that is the earlier of** when
   the owner (A) begins the actual construction work; or (B) enters into an agreement with another person for the
   other person to provide labor, to act as a subcontractor, or to provide materials for the construction."
   - Note what is ABSENT: **no occupancy requirement**, and no requirement that the structure be a residence —
     "or commercial building" is in the same sentence. Do not import an occupancy condition.
   - The clock starts at the **earlier** of first work and first agreement, which is usually earlier than
     groundbreaking. This is the kit's write-it-down-today item.

9. [V] AS 08.18.161(8) also exempts "an owner who contracts for a project with a registered contractor" — the
   paragraph you rely on for the scopes you hand to a registered firm.

10. [V] Filing the notice is not a formality. AS 08.18.116(b): "If an owner files a notice of the advertisement of
    a structure for sale or the sale of a structure … under AS 08.18.161(11), the department **shall investigate**
    and take appropriate action under this chapter if the notice and circumstances indicate that the owner is
    operating a business for which the owner is required to register as a contractor under this chapter."

11. [V] **The residential contractor endorsement — required of the CONTRACTOR, not of the owner.**
    AS 08.18.025(a): a general contractor "may not undertake the construction or alteration, or submit a bid to
    undertake the construction or alteration of a privately-owned residential structure of **one to four units**
    or advertise or publicly represent that the general contractor may undertake work of this type in the state
    without a residential contractor endorsement." "In this subsection, '**alteration**' means changes that have
    a value **greater than 25 percent** of the value of the structure being altered."
    AS 08.18.025(b)(2): the examination "may test competence in relation to **arctic structural and thermal
    construction techniques** and other matters as determined by the department in consultation with
    representatives of the construction industry."
    AS 08.18.025(b)(4): within the two years preceding application the applicant must have "satisfactorily
    completed either the **Alaska craftsman home program** sponsored by the department, or its equivalent, or a
    **postsecondary course in arctic engineering**, or its equivalent."
    AS 08.18.025(c): renewal requires "proof of continued competency relating to residential contracting."
    [H] **THE 16-HOUR / 50-QUESTION FIGURES ARE NOT IN THE STATUTE.** The live state guide states a "16-hour
    course and a 50-question exam." AS 08.18.025 sets no hours and no question count. Those figures may come from
    12 AAC 21 or from a course provider; they were NOT verified in this pass. **Do not print them.**

12. [V] Bond amounts, AS 08.18.071(b): general contractor **$25,000**; general contractor with a residential
    contractor endorsement performing exclusively residential work **$20,000**; mechanical or specialty contractor
    or home inspector **$10,000**; a contractor whose work on one project has an aggregate contract price of
    $10,000 or less, not divided to evade a higher requirement, **$5,000**.

13. [V] Insurance, AS 08.18.101(a)(2): public liability and property damage insurance of "not less than **$20,000
    for damage to property**, **$50,000 for injury, including death, to any one person**, and **$100,000** for
    injury, including death, to more than one person." Not required where each project has an aggregate contract
    price of $2,500 or less. Workers' compensation to the extent required under AS 23.30 (AS 08.18.101(a)(1)).

14. [V] **The provision that protects the owner.** AS 08.18.151: "A person acting in the capacity of a contractor
    or home inspector **may not bring an action** in a court of this state **for the collection of compensation**
    for the performance of work or for breach of a contract for which registration is required under this chapter
    **without alleging and proving** that the contractor … was a registered contractor … at the time of
    contracting for the performance of the work."

15. [V] Penalties, ascending:
    - AS 08.18.125(a): administrative fine "not more than **$1,000** for the first violation and not more than
      **$1,500** for a second or subsequent violation" of AS 08.18.011 or 08.18.025.
    - AS 08.18.125(e): the department **may not** impose an administrative fine "on a person who is acting as a
      contractor or home inspector in an area with a **population of 1,000 or less that is not connected by road
      or rail to Anchorage or Fairbanks**." A genuinely Alaskan provision and a good closing beat for AK.1.
    - AS 08.18.131: injunction, plus "a civil penalty of not more than **$1,000 for each violation. Each day that
      an unlawful act continues constitutes a separate violation.**"
    - AS 08.18.141(a): **class B misdemeanor** only where the person knowingly violates AS 08.18.011 or 08.18.025
      AND has previously been convicted, found guilty under AS 08.18.117, or fined under AS 08.18.125. (b): any
      other violation of the chapter "is guilty of a violation punishable under AS 12." So a first offense is
      NOT a misdemeanor.

16. [V] **THE TRADE ASYMMETRY — three exclusions in two chapters, and they are not the same rule.**
    - **Electrical, AS 08.40.190(b)(3):** excluded is "electrical installation on residential property that is
      **owned by the installer or a member of the installer's immediate family** and **not intended for sale at
      the time of making the installation**." TWO conditions.
    - **Mechanical, AS 08.40.390(b)(3):** excluded is "mechanical installation on a **single-family residence or
      a two-family residence that is not intended for sale** at the time of making the installation."
      **NO ownership condition at all**, and capped at two dwelling units.
    - **Plumbing, AS 18.60.715(c):** "Nothing in AS 18.60.705 — 18.60.740 **prohibits a person from performing
      plumbing work on the person's own property**." Unconditional — no not-for-sale clause, no occupancy clause.
    - **The remote thresholds differ tenfold.** AS 08.40.190(b)(2): electrical work "the cost of which does not
      exceed **$5,000**," in communities "under **500**" population or over 50 miles by air or water from a
      licensed electrical administrator. AS 08.40.390(b)(2): mechanical work "the cost of which does not exceed
      **$50,000**," in communities "under **5,000**" population, same 50-mile test.
    - **Only the electrical article has the still-follow-the-code clause.** AS 08.40.190(c): "Work within the
      exclusionary provisions of this section is nevertheless subject to the inspection provisions of AS 08.40.070
      and **must follow the regulations adopted by the department, other than regulations requiring licensure for
      the work**." AS 08.40.390 has **no subsection (c)**.
    [H] AS 08.40.070 is titled "Inspection or investigation by department" and its text is an investigatory power
    over "the work of a licensee" — subpoenas, oaths, records. It is NOT a construction-inspection regime, and it
    should not be described as "your homeowner work is still subject to inspection under AS 08.40.070" the way
    the live state guide does. The cross-reference is real; the implication is not.

17. [V] Teeth without an inspector. AS 08.40.180: "A person who knowingly violates AS 08.40.005 — 08.40.200, or
    who knowingly violates a valid regulation or order of the department **or a minimum electrical standard
    established under AS 18.60.580 — 18.60.590** that was in effect at the time that the installation or repair
    was made, is guilty of a misdemeanor, and upon conviction is punishable by a fine of **not more than
    $5,000**." Parallel provision for mechanical at AS 08.40.380(a), same $5,000.

18. [V] Certificate of fitness. AS 18.62.010: "In connection with work performed subject to the standards
    established in AS 18.60.580 and AS 18.60.705, a person may not **be employed** without a certificate of
    fitness to perform the work …" AS 18.62.070 lists the trades required to obtain one. AS 18.62.080: violation
    is a misdemeanor punishable by a fine of not more than $500. AS 18.62.030: application fee $50, journeyman or
    trainee certificate $200.
    [H] **The scheme is framed around being EMPLOYED**, which reads as leaving an owner doing their own work
    outside it, and it sits alongside rather than above the AS 08.40 homeowner exclusions. But nothing verified
    in this pass says so expressly. The kit prints this as a confirm-and-write-down item, which is the right
    treatment. Do not upgrade it to a flat statement without an official source.

---------------------------------------------------------------------------
## AK.2 — What binds the building when nothing binds the paperwork

19. [V] **THE KIT'S HEADLINE TRAP — the one construction requirement that reaches every dwelling in Alaska.**
    AS 18.70.095(a): "**Smoke detection devices shall be installed and maintained in all dwelling units in the
    state**, and carbon monoxide detection devices shall be installed and maintained in all qualifying dwelling
    units in the state. The smoke detection devices must be of a type and shall be installed **in a manner
    approved by the state fire marshal**. The carbon monoxide detection devices must have an alarm and shall be
    installed and maintained according to manufacturers' recommendations."
    - The force of this is structural: the fire marshal's *regulatory* power stops at four dwelling units
      (AS 18.70.080(a)(2)) and the adopted code excludes detached 1–3 family dwellings (13 AAC 50.020), but the
      smoke-alarm duty is **in the statute itself**, fifteen sections away, with no threshold of any kind.
    - **13 AAC 50.030(b)**: "Single-station smoke detection devices as required by AS 18.70.095 must meet the
      requirements of **NFPA Standard 72-2019**, as adopted by reference and, at a minimum, must be installed **in
      accordance with IBC Section 907.2.11** and the standards of this subsection. Smoke detectors may be **solely
      battery operated** when installed in **existing buildings built before January 1, 1989** or in **buildings
      without commercial power**." A new house on the grid is neither — so battery-only alarms do not satisfy it.
    - "Qualifying dwelling unit" for the CO alarms, AS 18.70.095(d)(3): one that "(A) contains or is serviced by a
      carbon-based-fueled appliance or device that produces by-products of combustion; (B) has an attached garage
      or carport; or (C) is adjacent to a parking space." In Alaska, effectively every house.
    - **Enforced as a crime.** AS 18.70.100(a): violation of AS 18.70.010 — 18.70.100 or a regulation adopted
      under them is a **class B misdemeanor**, and "when not otherwise specified, each **10 days** that the
      violation or noncompliance continues is a separate offense." AS 18.70.100(c) carves the carbon monoxide
      provision down to a non-criminal "violation."
    [H] "Hard-wired and interconnected" is the practical consequence of IBC 907.2.11 for a new dwelling with
    commercial power; the kit says so and tells the reader to confirm placement against NFPA 72 and the fire
    marshal's guidance. Do not print a specific alarm-location schedule — the IBC text is not freely readable.

20. [V] **The 2020 NEC is the statewide minimum.** 8 AAC 70.025(a): "The **2020 Edition of NFPA 70, National
    Electrical Code**, issued by the National Fire Protection Association on August 5, 2019, and approved by the
    American National Standards Institute on August 25, 2019, **constitutes the minimum electrical code for the
    state** and is adopted by reference." (b) adopts the 2017 National Electrical Safety Code (ANSI C2-2017).
    - Enabling statute AS 18.60.580; amendment power AS 18.60.590(a); local authority preserved at
      AS 18.60.590(b) — municipalities and rural electrification associations may prescribe standards "not less
      stringent."
    - [V] Scope caveat, AS 18.60.640(b): "These standards are the **recommended minimum standards** for all new
      structures in the state." And 8 AAC 70.010 limits the inspection regulations to "public structures" and
      places of employment. So the *standard* is statewide; the *state inspection* is not. The kit states both.
    - [V] 8 AAC 70.090(4) / AS 18.60.660(4) define "public structure" as "buildings such as hotels, **resident
      housing with more than one rental unit**, restaurants, taverns, lodging houses, children's homes,
      auditoriums, town halls, or any structure designed or used for public assembly."

21. [V] **The 2018 UPC is the statewide minimum, by regulation, over a statute that still says 1997.**
    8 AAC 63.010(a): "The codes set out in this section are adopted in accordance with AS 18.60.705 as the
    minimum plumbing standards **to be followed throughout the state**, except as provided under AS 18.60.710 or
    18.60.735." (a)(1) adopts the **Uniform Plumbing Code, 2018 edition** with two Alaska revisions: an added
    § 1210.2.3.1 barring LP-gas piping serving an appliance in a pit or basement where heavier-than-air gas could
    collect, and a rewritten § 612.2 on multipurpose wet-pipe sprinkler systems. (a)(2) and (a)(3) adopt the 2018
    Uniform Swimming Pool, Spa and Hot Tub Code and the 2018 Uniform Solar, Hydronics and Geothermal Code.
    - AS 18.60.705(a)(1) still adopts the **1997** UPC on its face, "unless the department adopts by regulation a
      later edition." It did. **This is the trap.**
    - AS 18.60.715(a): "The code applies to **all new construction**, all new work in relocated buildings, and to
      any alteration, repairs, or reconstruction of buildings."
    - **AS 18.60.735 — the 2,500 line:** "AS 18.60.705 — 18.60.740 do not affect the authority of a municipality
      to prescribe by ordinance, rule, or order, standards for their respective areas of jurisdiction **no less
      stringent** than those established under AS 18.60.705. AS 18.60.705 — 18.60.740 are not intended to
      duplicate or preempt code administration or enforcement by municipalities. **An organized municipality or
      unorganized village having less than 2,500 population is exempt from the provisions of AS 18.60.705 —
      18.60.740.**"
    - [V] Corroborated by the agency: Alaska DOLWD, Labor Standards and Safety, Mechanical Inspection Section
      (labor.alaska.gov/lss/plumbing_electrical.htm, page updated August 4, 2025): "Electrical Inspectors inspect
      new and altered electrical systems on all commercial structures and **on dwellings of three-plex and
      above**. **Plumbing Inspectors conduct inspections of work performed on new and altered plumbing, gas, and
      fuel piping installations in communities of 2,500 and above.**"

22. [V] Lead limits reach a house directly. AS 18.60.705(b): "the use of a pipe or pipe fitting containing more
    than **8.0 percent lead**, or of solder or flux containing more than **0.2 percent lead** in the installation
    or repair of a public water system or in the installation or repair of plumbing **of a residential** or
    nonresidential **facility that provides water for human consumption is prohibited**. This subsection does not
    apply to the use of leaded joints necessary to repair cast iron pipe."

23. [V] State plumbing permit fees are capped by a very old statute. 8 AAC 63.020: "Permits will be issued on a
    fee basis in accordance with the schedule outlined in AS 18.60.720." AS 18.60.720(a): "If the department by
    regulation requires permits for plumbing work, fees **may not exceed** the following: (1) for issuing each
    permit … **$2.00**; (2) a permit for each (A) plumbing fixture or trap or set of fixtures on one trap … 1.50;
    (B) building sewer or trailer park sewer … 5.00; (D) cesspool … 5.00; (E) private sewage disposal system …
    10.00; (F) water heater and/or vent … 1.50; (G) gas piping system of one to five outlets … 1.50 …"
    [H] Print as a **statutory ceiling**, not as the price. What the department actually charges was not verified.

24. [H] **THE BOILER QUESTION — printed in the kit as a question, not a rule.**
    AS 18.60.200(b): "A person who installs a boiler or unfired pressure vessel **shall notify** the Department of
    Labor and Workforce Development of the installation, **using a form provided by the department**."
    AS 18.60.210(b)(2) exempts "steam and hot water heating boilers, used exclusively for heating purposes, that
    are located in private residences or in apartment houses of fewer than six families" — **but only "from the
    requirements of AS 18.60.320 — 18.60.360,"** which are the certificate-inspection, certificate-issuance,
    suspension and fee sections. AS 18.60.200 is outside that range, so on its face the notice duty survives.
    AS 18.60.210(a)(9) fully exempts automatic utility hot water heaters used for space heating through the
    potable system within stated limits (≤120 gallons, ≤210 °F, ≤150 psig, ≤200,000 BTU/hr, tempering valve at
    ≤140 °F).
    **This reading was NOT confirmed with the department.** Whether DOLWD applies the notice duty to a residential
    hydronic boiler is an administrative question. The kit prints it as an ask-and-write-down item. **Do not
    upgrade it to a flat requirement without an agency source. Good candidate for a second edition.**

25. [H] **DEC onsite wastewater — 18 AAC 72 — NOT INDEPENDENTLY VERIFIED IN THIS PASS.** The kit deliberately
    prints no separation distance, no tank size, no percolation procedure and no fee, and instead gives the reader
    fill-in rules and tells them to get the numbers in writing from the office that will approve the system. It
    states only that onsite wastewater is regulated statewide by DEC under 18 AAC 72 or by a delegated local
    program, that an engineer is commonly required, and that the as-built and certification of completion is what
    a future buyer's lender will want. **All of that is safe; none of it is a number.** A second edition should
    pin: the applicability section, whether a registered professional engineer is mandatory, the exact name of the
    approval, the delegated-program list, and whether the post-construction as-built is a legal requirement.

26. [H] Wetlands, floodplain, driveway and addressing are stated in the kit at the level of "this office exists
    and this is what it does," without any threshold or fee. That is deliberate. The Corps of Engineers Alaska
    District, the NFIP floodplain administrator, Alaska DOT&PF driveway permits and borough 911 addressing were
    not individually verified in this pass and no number is printed for any of them.

27. [H] **AHFC / BEES — NOT VERIFIED IN THIS PASS.** The live state guide asserts BEES is "2018 IECC + ASHRAE
    62.2-2016 + Alaska amendments" with a "5-Star minimum," mandatory on state-financed homes. **The kit does not
    repeat any of it.** AK.2 Step 4 instead frames the financing layer generically — the lender's construction
    standard, its draw inspections, its energy requirement, and what it will accept in place of a certificate of
    occupancy — and gives the reader four questions to ask and write-in lines for the answers. That framing is
    defensible without any AHFC figure, and it survives an AHFC program change. A second edition should pin the
    current BEES edition, its statutory basis, its exact applicability, the compliance document, and whether AHFC
    requires the builder to hold the AS 08.18.025 residential endorsement.

---------------------------------------------------------------------------
## AK.3 — Inspections: three regimes on three different lines

28. [V] There is no statutory list of residential inspections because there is no residential code. What exists:
    - Local building department, if any — its permit card governs.
    - State plumbing inspection: AS 18.60.715(a) + AS 18.60.735 (2,500 population) + 8 AAC 63.010 (2018 UPC).
    - State electrical inspection: 8 AAC 70.010, public structures and places of employment; agency scope
      "three-plex and above."
    - State Fire Marshal: four or more dwelling units, AS 18.70.080(a)(2).

29. [V] **Owner rights when a state plumbing inspector does come — unusually explicit and never invoked.**
    AS 18.60.725(a): "A department inspector **shall** give written notice to the owner of a constructed premise
    or the contractor of a premise under construction of each violation of the code. The notice of violation
    **must accurately describe the violation and give specific reference to the section and paragraph of the
    code**. In addition, the notice must **prescribe the necessary changes** so that the work will comply with
    the code."
    AS 18.60.725(b): "In case of complaints by a contractor, builder, or installer charging arbitrary actions or
    incompetence on the part of an inspector, the commissioner, after reviewing written presentation of the
    dispute, may require reinspection by a **new inspector who has no connection with either disputant**."
    8 AAC 63.025(a): a notice of violation "is final unless the person affected or the owner or contractor of a
    construction premise affected files an appeal with the commissioner **within 30 days** after receipt of the
    notice," in writing, specifying objections and the relief sought.

30. [V] **Two routes by which an inspection failure reaches your utility service.**
    AS 18.60.710: "The department may by regulation designate appropriate inspection to a public or private
    utility company. **A company so designated may refuse utility connections** if an installation does not meet
    the requirements of this code."
    AS 18.60.630: an authorized electrical inspector gives written notice of each violation; "If **within 15
    days** after receipt of written notice of an electrical violation, the person notified does not rectify the
    condition, the inspector shall notify the electric utility firm … Upon notice in writing from the inspector,
    the supplier of electrical power **may discontinue services** to the premises where the alleged violation
    exists." AS 18.60.650: a person who installs wiring not in compliance and fails to correct it after written
    notice is punishable by a fine of not more than $1,000.
    [H] AS 18.60.610's delegation runs to "a public or commercial structure as defined in AS 18.60.660," so the
    statutory utility-inspector route does not reach a single-family house. What a utility requires
    *contractually* before energizing a new service is a separate matter and was not verified — the kit prints it
    as an ask-your-utility item with a fill-in line.

31. [H] There is **no deadline anywhere in Alaska law** for an inspector to appear after a request, and no
    deemed-approval remedy. Stated as a negative in the kit, with a write-it-down prompt.

32. [H] Everything in the kit's twelve-stage sequence that is not carrying a state citation is common practice,
    and the document says so in terms: "Stages marked 'Local' are common practice and are inspected only if a
    borough or city enforces a code — they are **not** Alaska law." Frost depth in particular carries **no state
    figure** and none is printed; Anchorage's often-quoted 42 inches is a local amendment and was not verified in
    this pass.

---------------------------------------------------------------------------
## AK.4 — Who, if anyone, regulates the parcel

33. [V] The document is a **procedure, not a table**, and that is a deliberate design decision recorded in the
    generator's docstring. The five questions: which borough (or unorganized); inside a city or not; does that
    borough or city issue a building permit and under which edition; is the community at or above 2,500; and who
    regulates onsite wastewater. None can go out of date.

34. [V] Local standards may be stricter, never weaker. AS 18.60.735 (plumbing) and AS 18.60.590(b) (electrical)
    both preserve municipal authority to prescribe standards "no less stringent" / "not less stringent" than the
    state's. So a local answer can add to the state floor and can never subtract from it.

35. [H] **THE JURISDICTION MAP WAS NOT VERIFIED IN THIS PASS.** Anchorage's adopted residential code edition,
    Mat-Su's and FNSB's absence of a borough building code, Juneau's and the smaller cities' programs, and the
    State Fire Marshal's deferred-jurisdiction list were all researched and no verified result reached the kit.
    Two secondary signals worth recording for a second edition, neither sufficient to print:
    - The Municipality of Anchorage's own codes page lists "**2024 Local Amendments**" as its most recent
      amendment set, which is hard to reconcile with the widely-repeated claim that Anchorage is on the 2018 IRC.
      **Treat "Anchorage = 2018 IRC" as unverified.** Settle 2018 vs 2021 before printing it anywhere.
    - The Fairbanks North Star Borough's own "Permitting & Inspections" landing page lists only Code Enforcement,
      Forms & Permits and Public Works — no building department — consistent with the long-standing understanding
      that FNSB has no borough-wide building code. Consistent, but not proof.
    The kit prints **no jurisdiction-specific claim** as a result, which is why it can ship without this.

36. [V] Offices that apply with or without a building permit, each a different government: DEC or a delegated
    local program (wastewater); DOLWD Mechanical Inspection (plumbing and gas permits, certificates of fitness,
    boilers); DCCED Corporations, Business and Professional Licensing (contractor registration and the
    AS 08.18.161(11) notice); borough and city planning (zoning, platting, 911 addressing); Alaska DOT&PF or the
    borough/city/road association (driveway); the community floodplain administrator; the U.S. Army Corps of
    Engineers Alaska District (wetlands); Alaska DNR Mining, Land and Water (water rights, well logs); the State
    Fire Marshal (4+ units, and the statewide smoke-alarm standard); AHFC and your own lender; your electric
    utility.

---------------------------------------------------------------------------
## AK.5 — Documents, and the file you build instead of a certificate

37. [V] **The seller-disclosure exemption almost nobody prints.** AS 34.70.010 requires the transferor to deliver
    a completed written disclosure statement on the Real Estate Commission's form "before the transferee … makes a
    written offer." But **AS 34.70.120**: "This chapter does not apply to the transfer of an interest in
    residential real property if the transfer is the **first transfer** of the property and if the property has
    **never been occupied**." Both conditions together.
    - So a brand-new owner-built house sold before anyone moves in is outside the disclosure chapter; the same
      house sold after a winter of occupancy is inside it in full.
    - It interacts with AS 08.18.161(11): the same early sale that escapes the disclosure statute is the sale that
      triggers the owner-builder notice and the mandatory departmental investigation. The two rules pull in
      opposite directions. **This pairing is the kit's second-best original observation.**
    - AS 34.70.090(b): negligent violation → liable for actual damages. (c): a person who "**wilfully**" violates
      it (the statute's spelling) is liable "for up to **three times** the actual damages." (d): costs and
      attorney fees may also be awarded.
    - AS 34.70.110: the chapter can be waived by written agreement between transferor and transferee.
    - AS 34.70.020: if the statement is delivered after a written offer, the transferee may terminate within 3
      days (in person) or 6 days (by mail).
    - AS 34.70.200(3): "residential real property" means property "whose primary purpose is to provide a
      single-family dwelling, or two single-family dwellings in one building."
    [H] The live state guide states the disclosure duty without the first-sale exemption. That is an omission
    worth correcting on the guide.

38. [V] AS 34.70.090(a): "A transfer that is subject to this chapter is **not invalidated** solely because a
    person fails to comply with this chapter." Useful reassurance; the remedy is damages, not rescission.

39. The kit's closing section — "the file you build instead of a certificate" — is original framing rather than a
    sourced claim, and is written as such. Its premise (most Alaska owner-builders never receive a certificate of
    occupancy, so the build record does that work for the appraiser, underwriter and buyer) follows directly from
    the verified facts above and asserts nothing about any particular lender's requirements.

---------------------------------------------------------------------------
## NOT VERIFIED / DO NOT PRINT

40. **RESOLVED — see LATE ADDENDUM item A.** (Was: no Alaska separation distance or sizing figure verified.)
41. **RESOLVED — see LATE ADDENDUM item C.** (Was: no BEES edition or AHFC program term verified.)
42. **RESOLVED — see LATE ADDENDUM item D.** The "16-hour course" is real but is the RENEWAL requirement, not
    the entry course. The "50-question exam" remains unsourced and is still DO-NOT-PRINT.
43. **RESOLVED — see LATE ADDENDUM item B.** (Was: no jurisdiction-specific claim verified.)
44. [H] Any frost depth, snow load or seismic design category as an Alaska-wide figure. All are site- and
    jurisdiction-specific; the kit says to get them from an engineer and prints none.
45. [H] That the state "inspects" homeowner electrical work under AS 08.40.070. See item 16 — the cross-reference
    is real but AS 08.40.070 is an investigatory power over licensees, not a construction-inspection regime.
46. **PARTLY RESOLVED — see LATE ADDENDUM item E.** There is no express homeowner exemption from the certificate
    of fitness; the mechanism is SCOPE, not an exemption, and the "employed" reading in item 18 was WEAKER than
    the first draft assumed. Still a confirm-and-record item in the kit, but for a better-stated reason.
47. [H] What any Alaska electric utility requires before energizing a new residential service. Framed as an
    ask-your-utility item with a fill-in line.
48. **RESOLVED — see LATE ADDENDUM item F.** DOLWD's own form scopes the notice to commercial and
    six-family-or-larger residential sites. A detached house files nothing. The kit now says so.

## FREE CODE AND STATUTE ACCESS (for buyers)
- Alaska Statutes and the Alaska Administrative Code, free and current: **akleg.gov** → Bills & Laws → Alaska
  Statutes, or → Alaska Administrative Code. Both searchable by section number.
- NFPA free read-only access to NFPA 70 (the National Electrical Code) and NFPA 72: **nfpa.org**.
- Contractor registration and endorsement search, free: **commerce.alaska.gov** → Professional Licensing →
  Search Licenses.
- DOLWD Mechanical Inspection publishes consolidated statute-and-regulation booklets for plumbing, electrical
  and boilers at **labor.alaska.gov** → Labor Standards and Safety → Mechanical Inspection. **Useful for
  orientation, but they lag the live code** — see minefield 4 above. Always confirm an edition against the AAC.


---------------------------------------------------------------------------
# LATE ADDENDUM — RESEARCH THAT ARRIVED AFTER THE FIRST BUILD

The four research streams commissioned for this kit all completed, but every one of their reports was lost in
transit on first send and had to be re-requested (four rounds; each resume reported "no active task" with no
report delivered). They landed after the kit had already been built to 41 pages from primary-source work done
directly. Everything below was then applied, and the kit rebuilt to 55 pages. **Where this addendum conflicts
with anything above, the addendum governs.**

## A. DEC ONSITE WASTEWATER — 18 AAC 72 [V]

**THE CITATION TRAP, and it is a good one.** 18 AAC 72 was rewritten effective **1 October 2023** and amended
**13 August 2025**. Three sections that every older summary relies on now read, in the code itself, "Repealed":
**72.020** (separation distances), **72.025** (holding tanks), **72.035** (conventional onsite systems). Anyone
quoting 18 AAC 72.020 for a setback is quoting a section that no longer exists. Live ranges for a house:
**72.501–72.560** conventional, **72.601–72.660** alternative, **72.100** private-well distances.

**THE BURIED PERMISSION — an owner may install their own septic system.** 18 AAC 72.400 bars anyone from
installing a conventional system unless certified under .405 or approved under .410 — but .410 is an
**approved-homeowner** route: DEC training course, application, and a **$275** training fee (72.954(c)),
authorizing **one system within a one-year period** on your own owner-occupied residence. 18 AAC 72.511 gives
three no-plan-approval routes: (a) certified installer, ≤1,500 gpd; (b) engineer-designed and engineer-inspected,
≤2,500 gpd; (c) approved homeowner. On route (c) the soils must still be classified by **a registered engineer or
a soils laboratory** (72.511(c)(2)). Percolation test mandatory in SM/GM/ML, unnecessary in clean SW/SP
(72.530(f)(3) note a).

**SEPARATION DISTANCES — main ruled these should be printed, and they are.** All [V] from reg text:
- **100 ft** private well to septic tank / absorption field / sewer line / holding tank / pit privy / "other
  potential source of contamination," nearest edge to nearest edge — **18 AAC 72.100(a)(1)**. (Public-system well:
  200 ft, 18 AAC 80.020 Table A. **Do not print a "Class C" column — that classification was repealed in 2017.**)
- **100 ft** to the high water level of a lake, river, stream, spring or slough — **18 AAC 72.520(b)**. Print the
  definition with it: **72.990(91)** makes "slough" include **a swamp, bog, or marsh**, which on an Alaska parcel
  is often most of it.
- **4 ft** vertical to the annual high water table; **6 ft** to an impermeable horizon including bedrock, clay and
  **permafrost** — **18 AAC 72.520(d)(1), (2)**.
- **50 ft** from a slope steeper than 25% with a >10 ft drop — **18 AAC 72.520(c)**.
- Also: 25 ft well to private sewer line / building sump / fuel tank (72.100(a)(2), (4)); field-to-field 6 ft or
  2× media depth (72.520(e)); tank-to-field 5 ft (72.520(f)).

**THE NEGATIVE FINDING, worth as much as the positives.** 18 AAC 72.520 was read in full and contains **no
property-line setback and no foundation setback**. DEC's installation manual lists 10 ft for each and footnotes
both "Recommended minimum horizontal separation distance." **Inside Anchorage those 10 ft ARE mandatory**
(AMC 15.65.210B.1), along with a 20-ft small-slope setback and seasonal groundwater adjustment factors. Print
the recommendation as a recommendation and Anchorage as the exception.

**SIZING** [V]: design flow **150 gpd per bedroom** (72.530(b)(1)); minimum tank **1,000 gal** to three bedrooms,
**+250 gal per bedroom over three** (72.530(e)(2)); field area off the 72.530(f)(3) table by perc rate and USCS
class, most conservative governing; frost cover **2 ft** southwest Alaska, **3 ft** Southeast and coast south and
east of Valdez, **4 ft** "all remaining areas of the state" (72.530(c)), with approved insulation substitutable
for up to 2 of those feet but never below 2 ft of actual soil. **SAND LINER**: a two-foot sand liner is mandatory
in clean gravels absent a slow enough percolation rate (72.530(f)(3)) — ground that drains too fast fails for the
opposite reason to ground that drains too slowly, and it surprises people.

**THE MOST ACTIONABLE SINGLE INSTRUCTION IN THE STATE** — main's phrase, and correct: **photograph the open
trench.** The 90-day Documentation of Construction requires photographs of eight specified stages, two of which
exist for only a few hours: the open excavation of the absorption field, and the field with media and pipe in
place immediately before backfill. Once covered, the photograph cannot be taken and the ordinary registration
route closes. Given its own callout in AK.2 rather than a table cell.

**PERMAFROST IS A CLIFF, not a complication** [V]. 18 AAC 72.511(d)(4): an exempt system "may not be located in
an area (A) **known or suspected to contain permafrost**; (B) where other conventional onsite wastewater systems
have been known to perform poorly; (C) where the groundwater table is within four feet of the ground surface…"
Note the standard is **suspected**. Suspicion pushes you into engineer design plus DEC plan approval, and
72.265(6) then requires a **laboratory soil-moisture profile analysis** and a **geotechnical study** showing the
area "will remain stable under the proposed design." This is the strongest argument in the kit for buying the
geotech report early.

**THE TWO PAPER TRAILS** [V]. Exempt systems: notify DEC "at least one day before beginning construction"
(72.550(a)), then within **90 days** file a **Documentation of Construction** with signature or seal,
**photographs of eight specified stages**, and a **$115** registration fee (72.550(c); 72.955(a)). Plan-review
systems: an **"Approval to Construct"** — the literal heading of 72.225 — with DEC acting within **30 days** and
the approval void if work is not finished within **2 years**; then a **certification of construction** signed by
owner, each contractor and the observing engineer, plus record drawings, within **60 days** (72.240(c)). Plan
review fee ≤1,500 gpd: **$655** (72.955(a)(1)(A)).
**The 90 days is the cheapest deadline in the kit**: miss it and the cure is an **after-the-fact registration**
under 72.560 requiring an **engineer-sealed adequacy report** on a buried system. DEC keeps the record and any
buyer or lender can pull it for a **$25** retrieval fee (72.955(b), (c)).

**WELLS** [V]. **No state permit** to drill a private domestic well — 18 AAC 80 applies to *public* systems
(80.005(b)); a single-family well is a "private water system" (80.1990) and DEC's own BMP document says
"Application of these BMPs is voluntary." Three real duties survive that: the 72.100(a) separations are
mandatory; 72.100(c) requires a construction "method equivalent to" the 18 AAC 80 protections; and the **well log
is mandatory** — 11 AAC 93.140(a) requires "the water well contractor **or a person who constructs the well**" to
file within **45 days** with **both the owner and the department**, via DNR's Well Log Tracking System. Drill it
yourself and the duty is yours. **Water right** needed only above 11 AAC 93.035(b) thresholds (>5,000 gal in a
day, or recurring >500 gpd more than 10 days a year); DNR's standard quantity for a fully plumbed single-family
home is **500 gpd** (11 AAC 93.040(d)(1)), so an ordinary house sits at or below the line.
**ARSENIC** [V]: no testing mandate, but the Alaska Section of Epidemiology (Bulletin 2016-14) documents
Fairbanks-area private wells to **960 ppb**, ~100× the 10 ppb standard, and states arsenic in private wells "is a
known problem in some communities" there. Carbon filters and softeners do not remove it; reverse osmosis does.

**PIT PRIVIES ARE LEGAL STATEWIDE with no DEC approval** [V] — 18 AAC 72.030(a), subject to 100 ft to surface
water, the 72.100 well distances, not in flood-prone areas or wetlands, 4 ft vertical to the annual high water
table, and a protective shelter. (b): only non-waterborne human waste. (c): decommission when solids come within
2 ft of the surface. Local governments may still restrict them. **Holding tanks** are alternative systems needing
an engineer (72.611(a)(4)) and DEC guidance discourages them for year-round residences. **Cesspools banned
outright** (72.015(a)).

**DELEGATED PROGRAMS** [V/H]. 18 AAC 72.110 authorizes delegation. **Municipality of Anchorage is the one
substantial delegated program** — "On-Site Water and Wastewater Section," Development Services Department; AMC
Title 15 ch. 15.55 (wells) and 15.65 (wastewater); AMC 15.65.005A: "When the requirements within this chapter
conflict with … 18 AAC 72 or the UPC, **this chapter shall prevail**." Two Anchorage-specific facts: an
**engineer's sealed design is always required** (AMC 15.65.050D.3), and **a new well needs a municipal permit**
(AMC 15.55.050A) — unlike the rest of the state. [H] FNSB, Mat-Su, Kenai Peninsula and Juneau: no local onsite
program found; LIKELY-negative, not proven. No published DEC list of delegated entities was findable.

**ANCHORAGE COSA** [V] — the certificate everyone still calls the HAA. AMC 15.65.060A: "Prior to the transfer by
gift, deed or contract of ownership or use interest in an on-site wastewater disposal system regulated by this
chapter, the transferor shall obtain a COSA from the department," with a parallel well requirement at
AMC 15.55.055A and exceptions for spouse and family-trust transfers. Required since an August 1998 ordinance. A
private engineer performs it: adequacy test at 150 gal/bedroom, tank pumped within 12 months, surveyor's as-built,
well yield test, and lab tests for coliform, arsenic and nitrate. **Anchorage only** — no equivalent found in
FNSB, Mat-Su, Kenai or Juneau. [H] COSA validity period not verified; do not print one.

## B. THE JURISDICTION MAP [V] — AND A DESIGN REVERSAL

The first draft of AK.4 printed **no** jurisdiction table and carried a callout explaining why. That reasoning
(a table goes stale; readers rely on it instead of calling) was sound but is outweighed now that the map is
verified jurisdiction by jurisdiction from each government's own code. **AK.4 now prints the table with a date on
it**, framed as "a starting point for question 3, not a substitute for it," and the five questions remain the
spine. This mirrors main's editorial ruling on the septic numbers: print what is verified, blank what is local.

**ANCHORAGE IS ON THE 2024 IRC.** AMC 23.05.010 adoption table; **AO No. 2026-33, 14 April 2026**; local
residential amendments at **AMC ch. 23.85**. Also 2024 IBC/IMC/UPC/IFC/IECC/IEBC/IFGC and the **2023 NEC** (the
one off-cycle row). **The widely-repeated "Anchorage uses the 2018 IRC" is stale** — this was the single most
valuable correction in the late research.

**Issues residential building permits** [V]: Anchorage **2024** IRC · Juneau **2024** IRC (CBJ 19.04.R010.1,
Serial 2025-26, eff. 21 Oct 2025; note 19.04.R010.2 pulls in fire-apparatus access, a real rural gate) · Kenai
**2021** (KMC 4.32.010; heavy amendments at .015 — 70 psf snow, 42 in frost, −18 °F, SDC D2, sprinklers deleted,
IRC ch. 11–42 deleted) · Seward **2021** (SCC 12.05.021; SCC 12.01.025 makes a water/sewer receipt a prerequisite
to any permit) · Sitka **2021** (plus 2021 UPC, 2020 NEC; published criteria 150 mph wind, 50 psf snow, 18 in
frost) · Fairbanks city **2018** (FGC 10-401) · North Pole **2018** (NPMC Title 15) · Palmer **2015**
(PMC 15.12.010; .020 lets the official modify on written application for "practical difficulties") · Ketchikan
city **2012** (KMC Title 19; its handout limits the IRC to single-family and duplex) · Kodiak city **2012**
(KCC 14.04.010; deletes IRC plumbing/electrical chapters to UPC/NEC) · Soldotna **2012** (SMC 15.07.010; adopts
others "with all revisions in 13 AAC 50.020" — state amendments layered on a local edition) · Valdez **2009**
(VMC 15.06.010; permit expiry 360 days; .070 names *each contractor* as applicant, which an owner-builder should
ask about) · Nome **2009** (Nome Code ch. 5.10).

**FIFTEEN YEARS OF EDITIONS IN FORCE SIMULTANEOUSLY**, 2009 to 2024, with no state cycle pulling them together.
Anchorage and Juneau both moved to 2024 within the last year, which is exactly why the stale claims persist.

**Issues NO residential building permit** [V]: **FNSB** — and its own FAQ is the cleanest quotable proof of the
borough/city pattern in the state: *"Building permits are only required within the City of Fairbanks and City of
North Pole. Since the FNSB has not adopted a building code, building permits are not required in the Borough
at-large outside of these two cities."* · **Mat-Su Borough** — verified by exhaustive enumeration of all 27
Permit Center permits, none of which is a building permit; requires driveway (borough roads), floodplain
(MSB 17.29), address request, encroachment and utility permits; multifamily only at 5+ units (MSB ch. 17.73) ·
**Kenai Peninsula Borough** — KPB Title 18 "Buildings and Construction" contains only local-hire and
public-works-contract chapters; does set building setbacks (KPB 20.30) · **Ketchikan Gateway Borough** — zoning
permit "for most new construction," plus floodplain and driveway · **Kodiak Island Borough** — zoning compliance
only, refers building permits to City of Kodiak · **City of Wasilla** — no building code, but WMC 16.90.010.B
requires a **land use administrative permit** "before the construction, alteration, addition, or modification of
a building," with an as-built survey after any structure over 250 sq ft, and WMC 16.90.020.B expressly lets the
owner draw their own site plan for a single-family dwelling or duplex · **City of Homer** — *"The City of Homer
does not have a building inspection program and does not issue building permits."* · **North Slope Borough** —
no building code found; residential gate is a District Residential Permit covering "digging for foundation and
building homes" [H, inferred from the code TOC] · **Unorganized borough** — nothing local at all.

**THE MAT-SU LAND USE PERMIT TRAP** [V]: the "Borough Land Use Permit" is **not** a zoning permit for your house.
It authorizes commercial or private use of unimproved **borough-owned** land, needs liability insurance and a
security deposit, and is run by the Land Management Division. Building on your own lot you do not need one — and
people apply anyway because the name sounds like the thing they are looking for.

**THE DEFERRED-JURISDICTION LIST, AND WHAT IT IS NOT** [V]. Thirteen entries as at August 2026: Anchorage Fire
Department, Anchorage Building Safety, City of Palmer, Juneau, Fairbanks, Kenai, Ketchikan, Seward, Kodiak, Sitka,
Soldotna, University of Alaska Fairbanks, Central Mat-Su FSA. **The entries are CITIES, not boroughs** —
"Fairbanks" is the city, "Kodiak" is the city, "Ketchikan" is the city. One is a university and one is a fire
service area. Deferral under AS 18.70.080 / 13 AAC 50.027 transfers **fire and life safety plan review**, not
building-permit authority — and the Fire Marshal's own page states the exemption that makes this moot for a house:
*"Residential housing that is three-plex or smaller is exempt from this requirement."* So deferral moves an
authority that never reached your house. Central Mat-Su FSA is exactly that case: deferred fire plan review inside
a borough that issues no building permits.

**THE THREE-PLEX LINE IS THE ORGANIZING PRINCIPLE** [V]. Fire Marshal exempts "three-plex or smaller"; DOLWD
inspects electrical at "three-plex and above." Same line, two agencies, and it matches 13 AAC 50.020 § 101.2
Exception 1 and AS 18.70.080(a)(2) exactly.

**UTILITY ENERGIZING INSPECTION — the assumed trap DID NOT VERIFY.** MEA, GVEA, Chugach and Homer Electric were
all checked; none publishes a third-party electrical inspection requirement before energizing a new single-family
service (MEA references only meter-base specs and project photos; GVEA 403'd). **Do not print that they do.** The
kit frames it as an ask-your-utility item with a fill-in line, which was already the right treatment. The
verified content that replaces it runs the other way and is stronger: the 2020 NEC applies statewide but nobody
inspects a single-family house — **code applies, no inspector**.

## C. THE FINANCING LAYER [V] — AND A FRAMING CORRECTION

**The hypothesis was right in substance and wrong in attribution.** It is **not** "your lender's code." It is
**state law** that uses loan eligibility as its enforcement mechanism; AHFC is a public corporation of the state.
Print "enforced through the mortgage, not the permit counter," never "the lender's code, not the government's."

- **AS 18.56.300(a)**: AHFC "may not make or purchase a housing loan for residential housing the construction of
  which begins **after June 30, 1992**" unless inspected; **(b)** names five stages: "(1) plan approval; (2)
  completion of footings and foundations; (3) completion of electrical installation, plumbing, and framing; (4)
  completion of installation of insulation; (5) final approval."
- **AS 46.11.040** and **AS 18.56.096(c)**: no state financial assistance or AHFC loan for a residential building
  whose construction began **after December 31, 1991** unless it meets thermal and lighting energy standards.
  **Two different trigger dates, six months apart — do not conflate them.**
- **15 AAC 150.035(a)**: the **2018 IRC with Alaska-specific amendments** is "the residential building code for
  buildings used for residential purposes containing four or fewer dwelling units," applicable "to a residential
  unit that is **not located within a municipality that has an approved municipal building code**." Drafted
  precisely for the ungoverned parcel.
- **15 AAC 155.010**: BEES = **2018 IECC + ASHRAE 62.2-2016 + Alaska-specific amendments**, buildings begun on or
  after 1 January 2019; **5 Star** minimum — **89 points** on the rating scale — and **4 ACH50** maximum (source
  the 5 Star to AHFC's published standard, **not** to 15 AAC 155.030(a)(1), which still reads "four-star plus").
  Alaska adds a climate zone the IECC does not have: **Zone 9**, the North Slope, with ceilings to **R-65**.
- **THE EXEMPTION THAT DOES NOT EXIST, and the most consequential omission caught in the late pass.**
  **15 AAC 155.020 names only two BEES exemptions — community fuel-cost and disaster housing.** There is NO
  owner-builder exemption, NO cash-build exemption, NO log-home exemption and NO remoteness exemption. Readers
  (and log builders especially) conflate this with the *contractor* exception at AS 18.56.096(a)(3), which is
  real and does cover owner-builders. You skip the contractor credential; you do not skip BEES. The kit now
  names the confusion explicitly.
- **THE INCENTIVES, which reach a cash build.** The **New Home Construction Rebate** is **$10,000**, first-come
  until funds are exhausted, for **5 Star Plus** — a notch ABOVE the BEES floor, keep the two distinct — with the
  foundation inspected on or after **2 January 2025**, and **AHFC financing is not required**. That makes it a
  second enforcement channel reaching cash builders. **EEIRR** cuts roughly 0.25–0.50 percent on the first
  **$250,000** of an AHFC loan depending on rating and gas availability. Both are funding-dependent — print with
  a confirm-before-relying instruction.
- **THE BEST DETAIL IN THE WHOLE KIT**: AHFC's IRC amendments **delete "Chapter 1, Part 2 — Administration and
  Enforcement"** — the permit system, inspection card and certificate of occupancy — and the BEES amendment
  document defines "**CODE OFFICIAL. The officer or other designated duly authorized representative of AHFC**."
  The financier is literally the building official.
- **PUR-101** BEES certification, completed **only** by an AHFC-authorized energy rater using AkWarm (no
  self-certification). **PUR-102** Summary of Building Inspections, signed per stage and then **recorded** —
  "Recording the PUR-102 is the only means of tracking compliance with the law." A CO from an **approved
  municipality** substitutes. The 15 approved municipalities: Anchorage (service area), Fairbanks city, Juneau,
  Kenai, Ketchikan, Kodiak city and borough, Nome, North Pole, Palmer, Petersburg SA1, Seward, Sitka, Skagway,
  Soldotna, Valdez. **Wasilla and Mat-Su outside Palmer city are NOT on it.**
- **Owner-builders are expressly accommodated**: AS 18.56.096(a)(3) excepts work "(A) … totally or substantially
  performed by the borrower; (B) … performed by a borrower who acts as the contractor; or (C) … in an area
  designated by the corporation as exempt … because of the unavailability of registered contractors." The PUR-102
  carries an **Exempt Builder's Certification** on which an owner-builder certifies "that I have not built a
  single family building, duplex, triplex, fourplex or commercial building within the prior two years" — **the
  AS 08.18.161(11) two-year rule follows you onto the mortgage paperwork.**
- **THE RESALE HOOK, and it is the strongest practical argument in the kit**: an uninspected house can be made
  AHFC-eligible later only by **destructive inspection** accepted case by case — holes cut in finished sheetrock,
  an engineer and inspector engaged, a notarized certification recorded after the fact. So the five inspections
  are the cheapest resale insurance an Alaska owner-builder can buy, and they are cheapest while the stage is open.
- **FHA — DO NOT PRINT THE 10-YEAR WARRANTY.** Operative text is **Mortgagee Letter 2020-36** (mandatory for case
  numbers on/after 4 Jan 2021), rewriting Handbook 4000.1 II.A.8.i: "copies of the building permit (or equivalent)
  and CO (or equivalent); or three inspections (footing, framing and final) performed by the local authority with
  jurisdiction over the Property or an ICC certified RCI or CI …; or in the absence of such ICC certified RCI or
  CI … three inspections … performed by a disinterested third-party, who is a registered architect or a structural
  engineer…" HUD's own note: "particularly relevant in jurisdictions where building permits are not issued."
  **The insured ten-year protection plan option and the 90% LTV cap were ELIMINATED** (83 FR 64269, Dec 2018).
- [H] Do not state AHFC's market share. Do not cite **AS 18.56.310** — it does not exist.

## D. THE ENDORSEMENT NUMBERS — A CONFLATION, NOW UNPICKED [V]

The live state guide's "16-hour course and a 50-question exam" is two errors in one clause.
- **No hour count exists for the entry course.** AS 08.18.025(b)(4) names the Alaska craftsman home program or a
  postsecondary arctic engineering course "or its equivalent," with no hours; 12 AAC 21.680(4) merely
  cross-references it.
- **The real 16 is the RENEWAL requirement**: 12 AAC 21.650(a) — "**16 contact hours** of acceptable continuing
  competency activities," every two years. DOLWD's own homeowner brochure lists the course and the 16 contact
  hours as two separate lines. (A third appearance of the number probably seeded the confusion: 12 AAC 21.665(a)(5)
  awards 16 contact hours for passing the endorsement examination.)
- **"50 questions" is unsourced and remains DO-NOT-PRINT.** The only exam standard in law is 12 AAC 21.680(3) — "a
  score of at least **70 percent** … administered by PSI Services, LLC or other examination approved by the
  department." Any question count comes from a vendor bulletin that changes without rulemaking.
- Also worth a line in any vetting checklist: a registered contractor must additionally hold a **current Alaska
  business license** under AS 43.70, separate from AS 08.18 registration.
- 12 AAC 21 adds **nothing** to the AS 08.18.161(11) owner-builder notice — no form number, no fee, no filing
  address. Do not cite a form number for it.

## E. CERTIFICATE OF FITNESS — THE FIRST DRAFT'S REASONING WAS WEAK [V]

The first draft leaned on AS 18.62.010's word "**employed**," reasoning that an owner working on their own house
is not employed. **The implementing regulation undercuts that**: 8 AAC 90.105(a) drops the word and requires a
certificate of "an individual **engaged in the performance of work** subject to the standards established in
AS 18.60.580 and AS 18.60.705."

The operative mechanism is **scope**, not employment, and there is **no express homeowner exemption** — the whole
certificate-of-fitness packet was searched for "homeowner / own residence / own property / single-family" and
returned zero hits. What protects a detached single-family house is that it falls outside both programs:
electrical reaches only "public structures" and places of employment (8 AAC 70.010; "public structure" =
resident housing with **more than one rental unit** and similar, 8 AAC 70.090(4)); plumbing exempts communities
under 2,500 (AS 18.60.735) and preserves work on your own property (AS 18.60.715(c)). **Note the regulations are
at 8 AAC 90, not 8 AAC 60.** Note also the electrical trigger is **building type, not geography** — a four-plex
in the unorganized borough still needs certified electricians.

## F. THE BOILER NOTICE — REFUTED FOR A HOUSE [V]

The first draft printed this as an open question, correctly. It is now answered, and the answer is **no notice for
a detached single-family home**. DOLWD's "Notification of New Boiler Installation" form states the information
must be submitted "within 30 days of installation at **ANY COMMERCIAL OR RESIDENTIAL (SIX FAMILIES) SITE** in the
State of Alaska" — tracking the AS 18.60.210(b)(2) line. **Worth printing the residual tension**: AS 18.60.200(b)
says "a person who installs" with no residential limit, so the six-family carve-out is **agency interpretation on
a form, not statutory text**. Unusual pressure vessels or anything serving more than one dwelling are still worth
a call.

## G. THREE STALE OFFICIAL DOCUMENTS — a better version of the edition trap [V]

DOLWD publishes consolidated statute-and-regulation booklets that contradict the live code and each other:
1. **Electrical Safety Statutes and Regulations** (May 2018, still linked in Aug 2026) prints 8 AAC 70.025 as
   adopting the **2017 NEC**. The live AAC adopts the **2020 NEC**.
2. `/lss/forms/2017_Plumbing_Code.pdf`, linked from the boilers page, prints the **2015 UPC**.
3. `/lss/forms/Plumbing_Code.pdf`, linked from the Mechanical Inspection home page, correctly prints the
   **2018 UPC** — which is the current 8 AAC 63.010(a)(1) edition.
Three official documents, three different answers, all from the same agency. Combined with AS 18.60.705's own
1997 UPC text, this is a far stronger and more concrete trap than the statute-versus-regulation point alone.

## H. STILL UNVERIFIED AFTER THE LATE RESEARCH — DO NOT PRINT

- **City of Bethel** — could not be determined either way; deliberately omitted from AK.4's table rather than
  guessed at. Do not state that Bethel has or lacks a building department.
- **Seward's UPC and NEC editions** — adopted as "the city designated edition" with no year in the code.
- **Palmer's IBC / NEC / UPC / IMC editions** (its 2015 IRC is solid). **Soldotna's department name.**
- **Kodiak Island Borough** — whether City of Kodiak inspection service extends outside city limits. The city
  publishes a *joint* city/borough permit application, which suggests it does, but this was not confirmed.
- **North Slope Borough** — explicit confirmation that no building code exists (inferred from the code TOC).
- **Utility energizing inspection requirements** for any Alaska utility.
- **USACE Nationwide Permit 29** — the Alaska District never names NWP 29; it links "See list of Nationwide
  Permits." Write "the applicable nationwide permit," not a number.
- **DCCED / DCRA state NFIP coordination specifics** — commerce.alaska.gov 403'd on every route.
- **Homeowner's insurance practice in unpermitted areas** — no citable Alaska-specific source found.
- **COSA validity period** — commonly quoted as 1–2 years; not in the code sections read.
- **The Anchorage well-permit subsection.** Two sources conflict: main's digest gives **AMC 15.55.040A**, the
  septic research gave **AMC 15.55.050A**. muni.org is unreachable to automated fetch, so the tie could not be
  broken. The kit cites **AMC 15.55** without a subsection and tells the reader to confirm with the On-Site
  Water and Wastewater Section. Resolve before a second edition.
- **Approved-Homeowner "exempt from the written exam."** Asserted in the digest, not found in the regulation text
  read. NOT printed. (The online-course option IS supported — 18 AAC 72.410(a) references "an online training
  course offered or endorsed by the department.")
- **RESOLVED — "a contractor-installed boiler triggers the 8 AAC 80.015 notice" is a SOUND citation.** I
  challenged it on the ground that 8 AAC 80 is the drinking-water chapter. **That was my error, and the next
  editor should not repeat it: there are two chapter 80s.** **8 AAC 80** is DOLWD's boiler and unfired pressure
  vessel chapter — the source is DOLWD's own *Boiler & Unfired Pressure Vessels — Statutes and Regulations*
  packet at labor.alaska.gov/lss/forms/boiler-stats-regs.pdf, which prints 8 AAC 80.015 (its eleven notification
  fields are what the installation form reproduces). **18 AAC 80** is DEC drinking water, which is what I was
  thinking of. Title 8 = Labor; Title 18 = Environmental Conservation. **No rebuild was needed**: the kit's
  treatment is form-based rather than reg-based and reads correctly as printed, and a contractor-installed
  boiler is outside the owner-builder frame anyway. A second edition could add one line telling a reader whose
  boiler is contractor-installed to ask for a copy of the filed notice.
