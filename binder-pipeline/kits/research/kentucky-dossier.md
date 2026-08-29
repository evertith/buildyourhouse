# Kentucky Owner-Builder Dossier — research for the KY Permit Kit (six documents)

Compiled 27 August 2026. Statute text was read from the OFFICIAL Kentucky Revised Statutes at
apps.legislature.ky.gov. **Note the trap in the endpoint**: `statute.aspx?id=NNNNN` returns a **PDF**
despite the `.aspx` extension, so it must be fetched with `curl` and extracted with `pdftotext -layout`
— a WebFetch or an HTML tag-stripper returns binary garbage. Administrative regulations were read from
the OFFICIAL Kentucky Administrative Regulations at the same host, where the pattern is the mirror
image: `apps.legislature.ky.gov/law/kar/{title}/{chapter}/{section}.pdf` (note: **no** `titles/`
segment) returns **HTML**, not a PDF, despite the `.pdf` extension. Agency facts, the adopted-code
list, the NEC enforcement notices and the 119 county inspector sheets were read from the Department of
Housing, Buildings and Construction at **dhbc.ky.gov** directly. Every claim is tagged:

  [V] = verified against a primary source (statute or regulation text read directly, or the
  administering agency's own page/notice/document). Safe to print with the citation.
  [H] = hedge — could not be pinned to a primary source, is locally variable, or is a proven-negative
  that can only be stated carefully. Print only with the hedge language and a verification step.

---------------------------------------------------------------------------
## WARNING FOR FUTURE EDITORS — FOUR MINEFIELDS

  1. **The endpoint content types are inverted.** `statute.aspx?id=` → PDF. `law/kar/815/007/125.pdf`
     → HTML. Getting this backwards is why a naive scrape of Kentucky law returns nothing usable.
     Chapter index (gives the section→id map): `statute.aspx` has none, use
     `chapter.aspx?id=NNNNN`; **KRS Chapter 198B is chapter id 38087**, 318 is 38833, 227A is 38354,
     376 is 39141, 342 is 38914, 151 is 37731, 100 is 37543. The full title index that lists every
     chapter with its id is at `apps.legislature.ky.gov/law/statutes/`.
     `legislature.ky.gov/Law/Statutes/Pages/default.aspx` returns **403** — never print it.

  2. **Kentucky renders an amended regulation with new text immediately followed by the text it
     replaced, with no visible strikethrough once the markup is stripped.** A current fee reads on
     screen as "fifty (50) forty-five (45) dollars." **The FIRST figure is the one in force.** Confirm
     against the last `eff.` date on the HISTORY line at the foot of the regulation. Getting this
     backwards would have printed a plumbing permit base fee of $45 instead of $50 and a per-fixture
     charge of $7 instead of $14. The kit prints this warning to buyers in its STATUTE_NOTE, because a
     buyer re-checking a fee will hit exactly the same thing.

  3. **REPEALED SECTIONS IN KRS 198B — do not cite.** 198B.020 (repealed 2017), 198B.035 (repealed
     2000), 198B.110 (repealed 2015), 198B.200 (repealed 2017), 198B.250 (repealed 2017), 198B.652
     (repealed 2017), 198B.4005 and 198B.4007 (repealed 2017), 318.056 (repealed 1966), 318.057
     (repealed 1986), 318.070 (repealed 1960), 318.071 and 318.074 (repealed 2017), 227A.080 (repealed
     2009). Also **KRS 198B.055 (structural steel welding) is NOT YET IN FORCE — effective January 1,
     2027.** Do not print it as current law.

  4. **The NEC edition is not in any regulation.** 815 KAR 7:125 incorporates the 2015 IRC and the 2018
     Kentucky Residential Code by reference and stops there; 815 KAR 35:015 confirms the NEC is
     "incorporated by reference in 815 KAR 7:120 and 815 KAR 7:125," i.e. **inside the code documents
     themselves**, which are copyrighted and not free text. The only free authority for the NEC year
     and for Kentucky's delayed articles is the Department's own adopted-code list and its NEC notices
     at dhbc.ky.gov. Anyone re-verifying must go there, not to the KAR.

---------------------------------------------------------------------------
## THE STRUCTURAL HEADLINE (this is the kit's thesis) — THE KENTUCKY INVERSION

Kentucky is the state where **the standard is mandatory and the enforcement is optional, and the State
is forbidden by statute from filling the gap.** One residential code binds every house in the
Commonwealth — no local code, no county writing its own rules, and the statutory definition of
"building" expressly reaches single-family dwellings. And then the same chapter makes the **building
permit, the inspections and the certificate of occupancy not mandatory** for a single-family residence
unless the local government passed an ordinance, and bars the Department from asserting jurisdiction
over enforcement on single-family dwellings. This is the exact inverse of Michigan, where the State is
the *default* enforcing agency; in Kentucky the State is *prohibited* from being the backstop for
houses.

What actually enforces the code on a rural Kentucky house is therefore not a building official. It is
**three statewide instruments plus two utility chokepoints**:

  * the **state plumbing installation permit** from the Department, required in all 120 counties;
  * the **state HVAC permit** for the initial system, required in any building designed for human
    occupancy;
  * the **certified electrical inspector's final certificate of approval**, without which **no utility
    may initiate permanent electric service**; and
  * **no permanent water supply** from any public utility or water district until the interior plumbing
    is installed and approved.

The practical consequence, which no competing Kentucky guide states: **in roughly one Kentucky county in
three, nobody will ever inspect your house — but you still cannot get power or water without two
signatures, and your septic permit is a statutory precondition of the permit that leads to one of
them.**

---------------------------------------------------------------------------
## KY.0 — Cover summary facts (the inversion, in headlines)

1. [V] The code is mandatory and reaches your house by definition. KRS 198B.050(1): "The department
   shall adopt and promulgate a **mandatory** Uniform State Building Code that establishes standards
   for the construction of all buildings, as defined in KRS 198B.010, in the state." KRS 198B.010(4):
   "'Building' means any combination of materials … affording facilities or shelter for any human
   occupancy, whether infrequent or regular, **and also means single-family dwellings**, including
   those sold or constructed under a trade or brand name."

2. [V] And the permit is not. KRS 198B.060(1): each local government shall enforce the code in its
   jurisdiction "**except that permits, inspections, and certificates of occupancy shall not be
   mandatory for single-family residences unless a local government passes an ordinance requiring
   inspections of single-family residences.**" Repeated in the code regulation itself, 815 KAR 7:125
   Section 2(2)(a): "**Permits, inspections, and certificates of occupancy shall not be required for a
   single-family dwelling unless required by local ordinance.**"

3. [V] No state backstop. KRS 198B.060(4)(b): the department may preempt an inadequate local program
   "**except that the department shall not preempt or assert jurisdiction for the enforcement of the
   code on single-family dwellings.**" Reinforced at 198B.060(8) (nothing "shall require a
   single-family dwelling to be permitted or inspected unless a local government has established a
   building inspection program") and 198B.060(13) (same for the certificate of occupancy).

4. [V] The three statewide permits. KRS 318.134(1)(a) (plumbing permit "from the department") with KRS
   318.015(1) ("in **all counties** of the Commonwealth"); KRS 198B.6671(1) (HVAC permit before an
   initial system, and "**No installation shall begin before the application for the permit has been
   filed**") with 198B.6671(6) (required "except in buildings designed for human occupancy");
   KRS 198B.060(11) (electrical certificate of approval).

5. [V] The two utility chokepoints. KRS 198B.060(11): "**no utility shall initiate permanent electrical
   service to any new building**, or any building which has been moved, until a final certificate of
   approval has been issued by a certified electrical inspector" — with "nothing in this section shall
   prohibit the supply or use of necessary electrical services during the construction and testing
   process." KRS 318.165: "**No permanent water supply shall be provided to any building by any public
   utility or water district where the interior plumbing system has not been installed and approved** in
   accordance with the provisions of KRS Chapter 318 and the State Plumbing Code."

6. [V] Kentucky has 120 counties. The Department publishes **119** county inspector sheets;
   **Gallatin County has none** (verified by diffing the published list at dhbc.ky.gov against the 120
   county names).

---------------------------------------------------------------------------
## KY.1 — What you may do yourself, and the question that governs the build

7. [V] **No state residential GC or home builder license.** This is a proven negative and is printed as
   one. The licensing provisions of KRS Chapter 198B were read in full: the Commonwealth licenses
   electrical (KRS Chapter 227A), plumbing (KRS Chapter 318), HVAC (KRS 198B.650–198B.689), elevators
   (198B.400–198B.540), fire sprinkler contractors and inspectors (198B.550–198B.6417), boilers
   (KRS 236) and manufactured housing (KRS 227.550–227.665). None creates a residential builder
   license. [H] Local business or contractor **registration** is a separate matter, is genuinely local,
   and the kit prints a write-in line rather than a list. KRS 318.140(3) expressly preserves local
   **occupational license fees** on persons engaged in the plumbing business, which is the mechanism
   local registration tends to run through.

8. [V] **ELECTRICAL — the widest homeowner right in the kit, and every competing guide narrows it.**
   KRS 227A.030(3), complete: "Nothing in KRS 227A.010 to 227A.140 shall prohibit or interfere with the
   ability of **a homeowner or farmer to install or repair electrical wiring on his or her real
   property**." That is the whole provision. There is **no occupancy condition, no single-family
   limitation, no requirement that the owner personally perform the work, no time limit and no
   affidavit** in the text, and **farmers are named expressly**. The live build-your-house.com guide
   states it as "exempts an owner and on-site resident of a single-family dwelling who personally does
   the electrical wiring" — three conditions that are not in the statute. The exemption is from the
   **license** only; it does not touch the certified electrical inspector's certificate of approval
   under KRS 198B.060(11), which is what actually gates the power.

9. [V] **PLUMBING — the right is regulatory, not statutory, which makes it the most fragile of the
   three.** KRS 318.030(1) is flat: "No person shall engage in plumbing … unless he or she is the
   holder of a valid and effective active master plumber's license … or … journeyman plumber's
   license." The only *statutory* exemptions (KRS 318.020) are apprentices, maintenance men and water
   company/district employees — **there is no homeowner exemption anywhere in KRS Chapter 318.** The
   homeowner right exists solely at 815 KAR 20:050 Section 2(1)(b): a permit "shall be issued only to
   (a) a licensed master plumber; or (b) **a homeowner who wishes to construct, install, or alter
   plumbing, sewerage, or drainage in a home occupied by the homeowner or constructed by the homeowner
   for the homeowner's own personal residential use**, if: 1. Application is made for the permit prior
   to the beginning of the work; 2. The homeowner files with the application an **affidavit** stating
   that the homeowner shall abide by the terms of this section; 3. All work shall be performed in
   compliance with 815 KAR Chapter 20; 4. **All the work shall be personally performed by the
   homeowner**; and 5. The homeowner **shall not have obtained another homeowner permit for
   construction of a new home issued within the last five (5) years.**"

10. [V] **HVAC — the narrowest occupancy test and the heaviest paperwork.** KRS 198B.674(3) exempts
    "**An individual owner of real property while practicing heating, ventilation, and air conditioning
    work on or within property owned and occupied by the individual**" — owned **AND** occupied.
    815 KAR 8:070 Section 2(2) issues the permit to a homeowner installing "in the homeowner's legal
    residence or in a home constructed by a homeowner for personal residential use" on filing (b)1 an
    **affidavit**, (b)2 **proof of adequate sizing**, and (b)3 **a complete design plan of all related
    duct and piping of system**, with (d) "**All the work shall be personally performed by the
    owner.**"

11. [V] **The two five-year rules are DIFFERENT COUNTERS and one is stricter.** Plumbing,
    815 KAR 20:050 §2(1)(b)5, bars only "another homeowner permit **for construction of a new home**
    issued within the last five (5) years" — so a homeowner plumbing permit for a repair or remodel does
    not spend the allowance. HVAC, 815 KAR 8:070 §2(3): "**Only one (1) homeowner HVAC construction
    permit shall be issued to an individual within a five (5) year period.**" No "new home" qualifier —
    any homeowner HVAC construction permit counts. No published source distinguishes these; the kit
    does.

12. [V] **The workers' compensation affidavit, and its uncapped penalty.** KRS 198B.060(10)(a): "No
    permit … shall be issued by any building department or by any political subdivision of the
    Commonwealth of Kentucky to any person seeking the permit **unless the person shall assure, by
    affidavit, that all contractors and subcontractors employed, or that will be employed**, on
    activity covered by the permit shall be in compliance with Kentucky requirements for **workers'
    compensation insurance according to KRS Chapter 342 and unemployment insurance according to KRS
    Chapter 341**." (b): the penalty is "an amount not to exceed **four thousand dollars ($4,000)** or
    an amount equal to **the sum of all uninsured and unsatisfied claims** brought under … KRS Chapter
    342 and unemployment insurance claims for which no wages were reported …, **whichever is
    greater**." (c): enforced by the **county attorney**. Note this attaches to the *local* permit, so
    it bites only where an ordinance exists.

13. [V] **Skipping the optional certificate of occupancy has a price.** KRS 198B.130(1): anyone
    "damaged as a result of a violation of this chapter or the Uniform State Building Code, has a cause
    of action … An award may include damages and the cost of litigation. **If a certificate of
    occupancy was not issued, then an award may also include reasonable attorney's fees.**" (2): within
    **one year** of discovery, and "in no event … more than **ten (10) years** after the date of first
    occupation or settlement date, whichever is sooner." This is the kit's argument for requesting a CO
    you are not required to obtain, and it is not made anywhere else.

14. [V] Penalties. Plumbing, KRS 318.990: "fined not less than ten dollars ($10) nor more than one
    hundred dollars ($100) or imprisoned for not more than ninety (90) days or both for each offense.
    **Each day the violation continues shall constitute a separate offense.**" The daily multiplier is
    the operative part; the headline numbers are trivially small and are printed with that framing.

15. [V] Farmstead carve-out. KRS 318.015(3): "This chapter shall **not apply to farmsteads**." Real,
    narrow, and frequently over-read — it reaches the plumbing chapter only, not the building code, not
    the electrical certificate, not the health department's septic rules. [H] "Farmstead" is not defined
    in the text read; the kit says "ask before you rely on it."

16. [V] Urban-county farm building exemption. KRS 198B.060(3): urban-county governments "may determine
    service districts within their boundaries within which **farm dwellings and other farm buildings**,
    not used in the business of retail trade or as a place of regular employment for ten (10) or more
    people, shall be exempt from the requirements of the Uniform State Building Code." Permissive and
    geographically narrow — printed with "check whether your urban-county government has actually done
    it."

17. [V] Local HVAC programs are frozen. KRS 198B.6673(4): "**No local governing entity shall impose any
    other additional heating, ventilation, and air conditioning inspection or permit requirements, or
    establish any local inspection or permitting program, unless those provisions were in place before
    January 1, 2007.**" 198B.6673(2) lets the Department authorize entities that had programs as of
    1 January 2007, and an authorized entity's permit "shall be considered a permit issued by the
    department."

18. [V] Local plumbing authorization works the same way. KRS 318.140(1): a local government may by
    ordinance enact the State Plumbing Code and issue permits; where the Department authorizes it, "a
    permit issued under the provisions of the local government plumbing code ordinance **shall be
    deemed a permit issued by the department**; provided, however, that inspectors of the department
    shall have **concurrent jurisdiction** with local government plumbing inspectors."

---------------------------------------------------------------------------
## KY.2 — Application, the statutory sequence, code editions, and the NEC trap

19. [V] **The septic permit gates the state plumbing permit, in statute.** KRS 318.134(2): "All
    applications for plumbing installation permits shall be accompanied by plans and specifications of
    the proposed plumbing installation, location, and construction of the water supply system to be
    used. **If an on-site sewage disposal system that does not have a surface discharge is proposed, a
    valid on-site sewage disposal permit issued by the Cabinet for Health and Family Services or its
    designated agent shall accompany the application.**" Most guides describe this ordering as local
    practice; it is law.

20. [V] **Code editions currently in force** — Department of Housing, Buildings and Construction,
    "Codes Currently Adopted by Kentucky" (dhbc.ky.gov/Documents/Find Currently Enforced Code.pdf, read
    27 Aug 2026), corroborated by 815 KAR 7:125 and 815 KAR 7:120:
      * **2018 Kentucky Residential Code, Third Edition (August 2024)**, based on the **2015 IRC**.
        815 KAR 7:125 §2(1) and §3; HISTORY last entry **eff. 12-3-2024**; 7-year expiration 12/3/2031.
      * 2018 Kentucky Building Code, based on the 2015 IBC (815 KAR 7:120 §2).
      * **2015 International Mechanical Code.**
      * **2009 IECC for residential buildings only** (2012 IECC is commercial only).
      * **2012 NFPA 54 National Fuel Gas Code** — *not* the IFGC. Unusual and worth printing.
      * **Kentucky State Plumbing Law, Regulations and Code, 815 KAR Chapter 20** — Kentucky adopts
        **neither the IPC nor the UPC**. Corroborated by KRS 198B.050(2), under which the Uniform State
        Building Code "shall encompass the Kentucky State Plumbing Code promulgated pursuant to KRS
        318.130 … and the national electrical code."
      * **2023 NFPA 70 National Electrical Code.** [H] **The agency's own document prints "(effective
        October 1, 2014)" beside the 2023 NEC entry — plainly a stale parenthetical carried over from
        an older edition. DO NOT PRINT THAT DATE.** The kit prints the edition without it.
      * 2015 International Fire Code (new construction, only where the KBC body references it), 2009
        ICC/ANSI A117.1, 2013 NFPA 13/13D/13R/14, 2013 NFPA 72, 2012 NFPA 101, 2015 IEBC.
      * The document closes "The above is for reference only and is only representative of the many
        codes and standards currently used."

21. [V] **THE NEC TRAP — this is the kit's marketing spine alongside the local-option inversion.**
    Department notice "July 15, 2026 NEC Update" (dhbc.ky.gov/Documents/, read 27 Aug 2026):
      * "This is a reminder that **effective July 15, 2026**, several provisions of the **2023 National
        Electrical Code (NEC) that were delayed under the 2018 Kentucky Residential Code** will become
        fully enforceable. The delayed enforcement period for the following articles expires on that
        date." — **210.52(C)** receptacle locations for islands, peninsulas, wall spaces, countertops
        and work surfaces; **230.67** surge protection for services supplying dwelling units;
        **314.27(C)** outlet boxes for ceiling-suspended (paddle) fans.
      * "**Provisions That Remain Delayed.** The following GFCI requirements in the 2023 NEC under the
        2018 Kentucky Residential Code **remain delayed and are not yet enforceable**: **210.8(A)** —
        GFCI protection for receptacles over 125 volts; **210.8(D)(8), (9), (10), and (11)** — GFCI
        protection requirements for specified branch circuits and outlets."
      * 314.27(C) clarification: it "**does not require every ceiling outlet box to be listed for
        ceiling fan support.** The requirement applies only to outlet boxes installed in the **habitable
        rooms** of dwelling units where a ceiling-suspended (paddle) fan could reasonably be installed
        in the future."
      * Grandfather rule: "**If a project has gone through a building code plan review and the approval
        from the review was before July 15, 2026, or the electrical permit was issued before July 15,
        2026, then the work under the scope of the electrical permit would not be required to follow
        the requirements that will begin mandatory enforcement on July 15, 2026.**"
      * The notice also lists 20 current 2023 NEC Tentative Interim Amendments (TIA 23-1 … 23-20) and
        points to nfpa.org for the PDF. The kit does not reproduce the TIA list — too volatile.
    **Why this is the trap:** the delay period expired six weeks before this kit shipped, so every
    guide written before 15 July 2026 is now stale in one direction; and the still-delayed GFCI
    articles are the half that actually changes what a builder installs, and no summary mentions them.

22. [V] **Next cycle.** Department notice "2026 NEC Task Force Announcement", dated **18 March 2026**:
    the Department "has began review of the 2026 National Electrical Code, NFPA 70" and established an
    NEC Task Force to identify changes against "the **currently adopted 2023 National Electrical
    Code**" and recommend adoption. Members from the Home Builders Association of Kentucky, Kentucky
    Association of Electrical Inspectors, IBEW, Independent Electrical Contractors and Schneider
    Electric; chaired by Darryl Morgan of HBC; meetings April–May 2026, open to the public.
    **No adoption date announced as of August 2026.**

23. [V] **Plumbing permit fees, from the regulation** — 815 KAR 20:050 (HISTORY last **eff. 3-1-2022**;
    the 3/2022 amendment raised them, and the impact statement confirms "fees must be increased"):
      * §4(1) one- and two-family: **$50 base plus $14** for each plumbing fixture, appliance or opening
        left for one; each domestic water heater; and each separately metered water or sewer service if
        more than one is installed. (Superseded figures $45 and $7.)
      * §4(3)(a) a single new or replacement water heater alone: **$50** flat.
      * §5(1) "A person with a plumbing permit shall be entitled to **five (5) plumbing inspections at
        no additional cost**." §5(2) each additional inspection **$50**, payable before the final.
        §5(3) additional inspection fees do not apply if the permit cost exceeded **$250**.
      * §6(1) the permit "**shall expire one (1) year after the date of issuance** unless construction
        is ongoing, in which case the permit shall remain effective until the completion of the planned
        plumbing inspection." §6(2) void if work ceases for more than **twelve (12) months**.
      * §1(1) permit required for: a new plumbing installation; moving or relocating a fixture, soil or
        waste opening or conductor; a new or replaced house sewer; a new or replaced water service;
        adding a backflow prevention device; a new or replaced water heater. §1(3) **no permit** for the
        repair of leaks, cocks or valves, or cleaning out waste or sewer pipes.
      * §7 incorporates the "**Plan Application Form**", edition **2/2020**.

24. [V] **HVAC permit fees** — 815 KAR 8:070 §4(1): one- and two-family dwelling installations and
    **Homeowner permits**, "**$105 for the first system plus fifty (50) dollars for each additional
    system**." §1(2) names the four application forms, including "**HVAC Construction Permit
    Application: Homeowner One & Two Family Dwellings**". §3(1) replacement furnaces, condensing units,
    heat pumps, fan coils, chillers and non-KRS-236 heating boilers are permitted and inspected on
    request.

25. [V] **Local fees are at cost.** KRS 198B.060(18): each local government and the department may
    establish a fee schedule; "**The fees shall be designed to fully cover, but shall not exceed, the
    cost of the service performed.**" This is why Kentucky building permit fees are low, and why the
    kit prints a blank rather than a national average. [H] No statewide local fee schedule exists; the
    kit prints a write-in line.

26. [H] **The plumbing plan-submission question is genuinely unresolved and the kit says so.**
    815 KAR 20:050 §3(1) reads "Except as provided in subsection (2) of this section, plumbing plans
    shall be submitted to the department for review and approval prior to the issuance of a plumbing
    permit," and §3(2)'s field-inspection exceptions cover only existing buildings and multi-family
    dwellings — so read literally a **new single-family house** would need a plan submission. But the
    enabling statute, KRS 318.160, reaches "any plumbing, sewerage, or water supply system of **any
    public building or establishment**." The two do not line up. **The kit deliberately prints neither
    answer**; it prints a checklist row instructing the reader to ask the Division of Plumbing and get
    the answer in writing, with a fill-in line. This is the single most important hedge in the kit.

---------------------------------------------------------------------------
## KY.3 — Inspections: the one real clock, and the rights nobody invokes

27. [V] **The only hard inspection deadline in the Kentucky residential scheme is the HVAC one.**
    KRS 198B.6672(3): "Any inspection required by KRS 198B.6671 **shall be scheduled with the property
    owner or owners or their agent or agents at least one (1) business day in advance and shall be
    completed within three (3) business days of the scheduled inspection.**" There is no equivalent for
    building, plumbing or electrical, and the kit says so explicitly rather than implying a general
    service standard.

28. [V] KRS 198B.6672(1),(2): no person shall use or permit the use of an HVAC system an authorized
    inspector determines was not installed in accordance with the codes, or where a required permit was
    not obtained or applied for.

29. [V] KRS 198B.6677(1): if an installation fails the code "**or if the property owner refuses to
    allow an inspection, the inspector shall refuse to approve the work**," and continued use may be
    prohibited where it "threatens human life or if the property owner refused to allow an inspection."
    (2) an aggrieved applicant "may request a hearing in accordance with KRS Chapter 13B."

30. [V] KRS 198B.060(9): the applicant "**by the act of applying for the permit, shall be deemed to
    have consented to inspection** by the local government or the department, of the building during
    construction and upon the completion of construction."

31. [V] **An inspector may not overrule your approved drawings.** KRS 198B.062: "All buildings shall be
    constructed according to the construction documents approved by the building official having
    jurisdiction … **No on-site inspector shall order changes in the construction of a building which
    are contrary to the approved construction documents.**" If the inspector believes the approved
    documents are incomplete or non-compliant, "the on-site inspector **shall refer the matter to the
    building official** having jurisdiction." Also: "Any approved changes to the construction of the
    building shall be recorded with the construction documents **before the certificate of occupancy
    shall be issued**."

32. [V] **Appeal clocks.** KRS 198B.070(3): a local appeals board "shall convene a hearing to consider
    the appeal **within fifteen (15) days of receipt**"; parties notified by certified mail "**no later
    than ten (10) days prior** to the date of the hearing"; the board "shall render a decision **within
    five (5) working days after the hearing**." (4) its decision is appealable only to the Department.
    (5) the Department hears appeals from local boards, or directly from local building officials where
    no local board has jurisdiction.

33. [V] **Certified electrical inspectors** — 815 KAR 35:015 (statutory authority KRS 227.489). Two
    classes: "**electrical inspector one (1) and two (2) family**" (exam ≥70% focused on one- and
    two-family dwellings, plus **four years** experience in residential wiring installation and design;
    certified to inspect one- or two-family dwellings and manufactured/mobile homes) and "**electrical
    inspector general**" (broader exam plus **eight years**; any property type). Alternative
    qualification: a registered professional electrical engineer of 3 years, or a currently licensed
    master electrician. Application on **Form EL-11** with a **$100** fee (waived for
    Department-employed inspectors), a photograph, proof of experience, and **proof of a $5,000 bond**
    under KRS 227.487(4) unless employed by the Department or a local government rules otherwise. A
    passing score is valid three years. [H] **A proposed amendment to 815 KAR 35:015 exists** (the site
    shows "A proposed version of this document exists") — re-check before the next edition.

34. [V] KRS 198B.060(15) lets local governments contract out plan review and inspection to certified
    persons, requiring department certification under KRS 198B.090 for plans-and-specifications and
    building inspectors, certification under **KRS 318.140** for plumbing inspectors, and **no conflict
    of interest** between the inspection function and other employment or business activities.
    KRS 198B.6673(3): a local HVAC inspector needs **six years** as a licensed journeyman or master, or
    to be a certified building inspector who has passed the HVAC examinations.

35. [V] KRS 198B.140: "No person shall hinder an inspector enforcing any of the provisions of this
    chapter in the performance of his lawful duties."

36. [H] **There is no statutory residential inspection sequence.** The seven-step sequence the kit
    prints for jurisdictions that do require permits is explicitly labeled "a working sequence, not a
    statutory list," with a note that the jurisdiction's permit card governs. Nothing in KRS 198B or
    815 KAR 7:125 prescribes footing/foundation/rough-in/framing ordering for a single-family dwelling,
    unlike Michigan's R 408.30509.

---------------------------------------------------------------------------
## KY.4 — Who inspects (the kit's differentiator)

37. [V] **The county inspector sheets are Kentucky's Statewide Jurisdiction List, and almost nobody
    outside the trade knows they exist.** dhbc.ky.gov → HOW DO I? → **Contact an Inspector**
    (`docs_cols.aspx?cat=312`), then one PDF per county at
    `https://dhbc.ky.gov/Documents/{County}%20County.pdf`. All 119 were downloaded and tallied
    27 August 2026.

38. [V] **The tally.** Of the 119 published sheets:
      * **25 print "None"** for Local Building Inspector, in the revealing form "**None / For Commercial
        construction Contact Dept. Housing, Buildings Construction for building permits**" — which is
        KRS 198B.060(4)(b) in practice: the State handles commercial there, and for a house, nobody.
        The 25: Bracken, Breathitt, Elliott, Estill, Harlan, Jackson, Knott, Lawrence, Lee, Leslie,
        Letcher, Lewis, Magoffin, Martin, Menifee, Montgomery, Morgan, Nicholas, Owsley, Pendleton,
        Powell, Robertson, Rockcastle, Trimble, Wolfe.
      * **10 carry no Local Building Inspector line at all**: Caldwell, Carlisle, Cumberland, Green,
        Logan, Metcalfe, Russell, Simpson, Taylor, Woodford.
      * **4 name one person as "State & Local Building Inspector"**: Ballard, Fulton, Graves, Hickman.
      * **80 name a local building inspector.**
    => **35 of Kentucky's 120 counties show no local building inspector on the state's own sheet —
    close to one in three.**
    [H] **The caveat is printed with the number and must never be dropped:** the sheets are a contact
    list of inspectors, not a register of ordinances. A city inside one of those counties may still
    require permits, and a county with a named inspector may still not require them for single-family
    dwellings. Sheet formats vary and some counties combine roles, so the classification is the
    author's reading of the agency's wording.

39. [V] **The sheets are maintained.** 117 of 119 carry an "Updated" stamp: **70 revised in 2026, 41 in
    2025, 6 in 2024**, across 43 distinct revision dates, the most recent in August 2026.

40. [V] **Every published sheet names a State Electrical Inspector** (119/119) and a Boiler Inspector
    (119/119). Other field frequencies: Plumbing Inspector 122 occurrences, Local Electrical Inspector
    125, State Elevator Inspector 121, State Manufactured Housing Inspector 117, State Building
    Inspector 115, HVAC Inspector 115, Health Dept. Environmentalist 115, Local Building Inspector 107.

41. [V] **The sheets print the plumbing inspector's office hours and office address, and that address
    is routinely the COUNTY HEALTH DEPARTMENT.** Owsley County, verbatim: "Office Hours: Wednesday
    (12:00 p.m. – 1 p.m. EST); Office Address: Owsley County Health Department, 501 KY Highway 28,
    Booneville, KY 41314." This is the most useful practical fact in the whole directory: the state
    plumbing inspector keeps hours in the same building as the health department that issues the septic
    permit — the two things KRS 318.134(2) chains together.

42. [V] **The recurring electrical line, which is the real answer for most of rural Kentucky:**
    "**Local Electrical Inspector: Contact the County Judge Executive's office or City office where
    work is to be performed.**" Appears on Owsley, Jefferson, Woodford and most others.

43. [V] Individual examples worth knowing. **Jefferson**: "Local Building Inspector & HVAC Inspector:
    Louisville - Metro Municipal Office … www.louisvilleky.gov … 444 South Fifth St., Louisville 40202
    **(Excludes the City of Jeffersontown)**", with a pointer to Louisville's Construction Review pages;
    Jeffersontown runs its own. **Warren**: separate county *and* city local building inspectors,
    separate county and city local electrical inspectors, three named plumbing inspectors with office
    hours at the Warren County Health Department, and three health department environmentalists.
    **Daviess**: "Local Building, Electrical & HVAC Inspector — Daviess / City of Owensboro,
    www.iompc.org" (a combined city-county body).

44. [V] Agency domains, all fetched successfully 27 August 2026: **dhbc.ky.gov** (the Department — note
    `hbc.ky.gov` returns a near-empty stub and must not be printed), **apps.legislature.ky.gov**,
    **chfs.ky.gov** (Cabinet for Health and Family Services), **eec.ky.gov** (Energy and Environment
    Cabinet), **transportation.ky.gov** (Transportation Cabinet), **kygeonet.ky.gov**, **ppc.ky.gov**.
    `eec.ky.gov` and `chfs.ky.gov` return 403 to a default curl user-agent and 200 to a browser
    user-agent — they are live; do not conclude otherwise from a bare curl.
    **`water.ky.gov` timed out and is NOT printed anywhere in the kit.**

---------------------------------------------------------------------------
## KY.5 — Forms, and what needs no permit

45. [V] Named state forms: the plumbing "**Plan Application Form**", 2/2020, incorporated by
    815 KAR 20:050 §7; and the four HVAC forms at 815 KAR 8:070 §1(2), of which the owner-builder uses
    "**HVAC Construction Permit Application: Homeowner One & Two Family Dwellings**". [H] The kit does
    not name a state *building* permit form, because in Kentucky the building permit is a local
    instrument and many jurisdictions issue none at all.

46. [V] What needs no permit: plumbing — repair of leaks, cocks or valves, and cleaning out waste or
    sewer pipes (815 KAR 20:050 §1(3)). HVAC — "No permit or inspection shall be required for the
    installation of **window unit air conditioners or space heaters**" (KRS 198B.6671(5)) and none is
    required at all "except in buildings designed for human occupancy" (198B.6671(6)).

47. [H] **Kentucky publishes no general residential permit-exemption list** of the kind most states put
    in their code's R105.2 (sheds under X square feet, fences, decks). The kit says so and explains
    why: where no local ordinance requires a building permit for the house, there is nothing for a shed
    to be exempt *from*; and where an ordinance applies, the exemptions are that jurisdiction's. A
    write-in line follows. This is a proven negative stated carefully rather than a gap left silent.

---------------------------------------------------------------------------
## DELIBERATELY OMITTED — and why

* **Any septic detail beyond KRS 318.134(2).** The 902 KAR onsite sewage citations, the site-evaluation
  procedure, whether a homeowner may install their own system, and septic fees were assigned to a
  research sub-agent whose report never arrived. Rather than paraphrase secondary sources, the kit
  prints only what the plumbing statute establishes (the septic permit must accompany the plumbing
  application, issued by the Cabinet for Health and Family Services or its designated agent) and routes
  the reader to the environmentalist named on their county inspector sheet, with fill-in lines. **This
  is the largest open item; see below.**
* **Any processing time or "typical timeline."** Kentucky publishes none statewide except the HVAC
  1-business-day / 3-business-day rule, which is printed. The kit says explicitly that it does not
  print one and tells the reader to ask.
* **Local building permit fee figures.** Set at cost by each local government (KRS 198B.060(18)); no
  statewide schedule exists. A national average would be a guess. Write-in line instead.
* **Phone numbers, everywhere.** The county inspector sheets carry direct-dial and cell numbers for
  named individuals; they change constantly. The kit prints websites and navigation routes and gives
  the reader a rule to write the number they confirmed.
* **The 2023 NEC TIA list** (TIA 23-1 … 23-20). Too volatile for print; the kit points at the
  Department's notice instead.
* **The "(effective October 1, 2014)" parenthetical** beside the 2023 NEC on the Department's
  adopted-code list — an evident stale artifact. Printing it would import an agency typo.
* **Frost depth, seismic design category, ground snow load and the rest of Table R301.2.** These live
  inside the 2018 Kentucky Residential Code, Third Edition, which is copyrighted and not free text. The
  live state guide prints specific figures (24"/30"/33" frost depth, SDC D0–D2 by county) that could
  not be verified from any free primary source in the time available. **The kit prints none of them.**
* **Any claim that Kentucky is a "mini/maxi" code state.** See open questions.
* **Mechanic's lien deadlines (KRS Chapter 376) and up-the-ladder workers' compensation liability
  (KRS 342.610).** Assigned to a sub-agent whose report never arrived; not independently verified in
  time. The kit covers owner exposure through the verified KRS 198B.060(10) affidavit and
  KRS 198B.130 private action instead. Candidates for the second edition.

---------------------------------------------------------------------------
## OPEN QUESTIONS / UNCONFIRMED

1. **Is Kentucky genuinely a "mini/maxi" code state?** The live guide asserts local governments may
   adopt neither a weaker nor a stronger residential code. That proposition was **not found** in
   KRS 198B.050, .060 or .080. What those sections actually say is that the code is mandatory
   (198B.050(1)) and that departmental amendments are "effective statewide" (198B.080(2)) — which is
   not the same as barring a local government from adding requirements. Indeed KRS 198B.060(1) plainly
   *permits* a local government to require permits and inspections the state does not, and
   KRS 198B.6673(4) bars additional local HVAC requirements **specifically**, which would be redundant
   if a general preemption already existed. **The kit therefore never uses the phrase "mini/maxi" and
   never claims local governments cannot be stricter.** It says the technical standard is one statewide
   code and that enforcement is a local option. Someone should find the actual authority for the
   mini/maxi claim, or establish that it is folklore.
2. **The plumbing plan-submission conflict** (item 26). Needs an answer in writing from the Division of
   Plumbing.
3. **Septic**: the 902 KAR citations, the official name of the permit and of the site evaluation,
   whether a homeowner may install their own system, statewide vs. local fees, and setback distances.
4. **Floodplain**: whether the Division of Water's KRS 151.250 permit applies to a dwelling in a
   floodplain in a county with no local ordinance. The kit asserts only that Kentucky administers
   floodplain construction at state level and that it "can apply even where your county has no building
   permit" — which follows from the permit being a separate state program, but the statutory text was
   not read.
5. **Whether every county's electrical inspection is genuinely available.** KRS 198B.060(11) conditions
   the utility bar on a certified electrical inspector having "been provided for by the local
   government or the department." All 119 sheets name a State Electrical Inspector, which strongly
   implies universal coverage, but the conditional wording deserves a direct answer from the Department.
6. **Gallatin County** has no published inspector sheet. Why, and who covers it?
7. **815 KAR 35:015 has a proposed amendment pending** — check what it changes before the next edition.
8. **Local contractor/business registration**: which Kentucky cities actually run one, and under what
   authority. The live guide names Louisville, Lexington and Bowling Green; not verified here.

---------------------------------------------------------------------------
## FREE CODE ACCESS (for buyers)

* **Statutes and regulations**: apps.legislature.ky.gov — Kentucky Law → Kentucky Revised Statutes →
  KRS Title Page (Chapter 198B building code, 227A electrical, 318 plumbing); or Kentucky
  Administrative Regulations → KAR List by Title (815 Housing, Buildings and Construction; 902 Public
  Health; 401 Energy and Environment). Free, no account.
* **Which codes are in force**: dhbc.ky.gov → HOW DO I? → "Find Currently Enforced Code" — a one-page
  PDF listing every adopted code and edition. Free.
* **Who inspects your county**: dhbc.ky.gov → HOW DO I? → "Contact an Inspector" → your county. Free.
* **NEC enforcement notices**: dhbc.ky.gov → LATEST NEWS. This is the only free authority for
  Kentucky's delayed NEC articles. Free.
* [H] The 2018 Kentucky Residential Code itself is copyrighted and is **not** freely readable; it may be
  "inspected, copied, or obtained, subject to applicable copyright law" at the Department, 500 Mero
  Street, Frankfort, Monday–Friday 8 a.m.–4:30 p.m. (815 KAR 7:125 §3(2)). Buyers wanting the full text
  must buy it or read it at the Department.

---------------------------------------------------------------------------
## LATE ADDENDUM — corrections applied after first hand-off (27–28 August 2026)

All four research sub-agents' reports arrived AFTER the kit had been built and handed off. Five items
corrected something already printed; the rest filled the acknowledged septic gap. The kit was rebuilt,
re-audited and re-zipped. Final build: **39 pages (3 / 10 / 10 / 5 / 6 / 5)**, audit-clean.

### CORRECTION 1 — the county tally was WRONG: 35 → **41 of 119**
My classifier treated a "Local Building Inspector:" heading with an EMPTY value as a named inspector.
Six sheets do exactly that: **Hancock, Livingston, Ohio, Todd, Union, Webster**. Verified by hand.
Correct tally of the 119 published sheets:
  explicit "None" ......... 25
  heading present, blank ... 6
  no such line at all ..... 10   => **41 of 119 (34%) show no local building inspector**
  "State & Local" ......... 2
  named ................... 76
[H] **A second caveat was added at the same time, and matters as much as the number:** several of the
76 name an inspector for a CITY ONLY — sheets carry wording like "City Limits ONLY", "(No County
Building Inspector)", "Fulton City Limits ONLY", "(County ONLY)". My regex caught 7 (Bath, Boyd,
Carroll, Fleming, Floyd, Franklin, Fulton); a wider net finds ~12. So "76 named" materially overstates
county-wide coverage, and the kit now says so. Do NOT print "78 counties require permits" or any
derived figure.
INDEPENDENT PROOF EXHIBIT worth keeping: Boyd County's own site publishes, under "Building Permits for
Residential Construction & Remodeling", the words **"Non Required"** — a county government confirming
the statutory result. (boydcountyky.gov/202/Construction-Permits-Inspection-Contacts)

### CORRECTION 2 — KRS 198B.060(11) is CONDITIONAL and I had printed it flat
The bar operates only "**After a certified electrical inspector has been provided for by the local
government or the department**." KY.1's table carried the condition; KY.1's and KY.3's callouts and
KY.5's row had dropped it. All now carry it, with the evidence that it bites in practice: **all 119
published county sheets name a State Electrical Inspector.** Phrase it that way, never as a flat
unconditional bar.

### CORRECTION 3 — the "mini/maxi" preemption IS real, and open question 1 is CLOSED
I could not find it in KRS 198B and the kit avoided the claim. It is not in the statutes — it is in the
code book. **Kentucky Residential Code R101.3:** "The purpose of this code is to establish minimum and
maximum requirements … **Local governments shall not adopt or enforce any other building code for
detached single family dwellings, two-family dwellings and townhouses.**" (KBC 101.3 is the commercial
analogue.) The kit now quotes it. The right framing, which the guide gets muddled: **locals may not
change the technical standard (R101.3), but KRS 198B.060(1) plainly does let them switch enforcement
on.** Same code everywhere; local choice about whether anyone checks.
=> **My state-guide error list was wrong on this point and was retracted.** The live guide's mini/maxi
claim is substantially correct; its fault is citing 815 KAR 7:125 for it instead of KRC R101.3, and
building an unsupported radon-preemption argument on top.

### CORRECTION 4 — NFPA 54 edition: the agency's own documents CONFLICT
HBC's adopted-codes list says **2012 NFPA 54**. The Kentucky Residential Code's own referenced-standards
chapter (Ch. 44) says **54-09**, referenced at G2401.1. Kentucky adopts **no IFGC at all** — residential
fuel gas runs through KRC Chapter 24. The kit no longer pins the year; it names NFPA 54, states that
the two sources disagree, and tells the reader to ask their inspector. [H] Firm this up if HBC
reconciles its documents.

### CORRECTION 5 — scope trap: the permit exemption says "single-family" only
Both KRS 198B.060(1) and 815 KAR 7:125 §2(2)(a) say "single-family residences"/"single-family
dwelling," while 815 KAR 7:125 §1 defines "two (2) family dwelling" and "townhouse" as separate terms
and §2(1) applies the code to all three. So the permit/inspection/CO waiver arguably does **not** reach
a duplex or a townhouse. A caveat line was added to KY.1.

### GAP CLOSED — septic, and it turns out to gate the ELECTRICITY too
The largest omission at first hand-off is now filled and printed.
* Regs, all Current: **902 KAR 10:085** (main systems reg, site evaluation, sizing, setbacks; cert. eff.
  8-10-2023), **902 KAR 10:081** (component construction standards), **902 KAR 10:110** (permit
  issuance, incl. homeowner permits; eff. 6-16-2021), **902 KAR 10:140** (installer certification),
  **902 KAR 10:170** (septic tank servicing).
  **DO NOT CITE — INACTIVE/REPEALED: 902 KAR 10:060 (the old fee reg), 10:090, 10:100, 10:130.** Several
  web guides still cite 10:060 for fees; that is dead law. The $50 fee now lives at 10:110 §2(1)(b).
* It is a **CONSTRUCTION permit**, on form **DFS-307, "On-site Sewage Disposal System Construction
  Application and Permit" (10/20)**, incorporated at 902 KAR 10:110 §3. **There is NO separate operation
  permit for a residential system** — "operation permit" returns zero hits across 10:085 and 10:110.
  What follows installation is an inspection before backfill (10:085 §9(1)).
* **NOT a perc test.** "Percolation" appears zero times in 902 KAR 10:085. Ratings are by soil
  morphology from borings or backhoe pits to 42 inches: SUITABLE / PROVISIONALLY SUITABLE / UNSUITABLE.
* **Statutory shot clock, KRS 211.350(3):** site evaluations completed "within fifteen (15) working
  days of receipt of the application," plus "an additional ten (10) working days" after any further
  information is submitted. Printed — it is the only septic deadline Kentucky gives the applicant.
* **Homeowners MAY install their own system** — 902 KAR 10:110 §2(4): permits "may be issued to
  homeowners" if applied for before starting, work done to the regulations, "**all work is personally
  performed by the homeowner, except that necessary excavation and backfilling work may be performed by
  a certified installer if notification of intent is made at the time of application**" with the
  installer named; and "**No person shall be issued more than one (1) homeowner permit to construct or
  alter an on-site sewage disposal system in any five (5) year period**," repairs excepted. That is a
  **THIRD five-year ration**, separate from the plumbing and HVAC ones. "Homeowner" (§1(8)) excludes
  anyone "who is a builder or contractor who engages in a business of constructing or rehabilitating
  residential structures for sale or resale."
* Fees are hybrid: **$50** state permit fee in regulation (10:110 §2(1)(b)) plus the local board of
  health's fees under KRS 211.355. [H] Local examples verified by the sub-agent (not by me): Lincoln
  Trail District HD site eval $300 / new system permit $320 / **homeowner installation $520**; Green
  River $200 site eval; Franklin County $250 / $270. **A homeowner-install permit is not automatically
  cheaper** — the kit says so without printing the county figures.
* **KRS 211.350(8) — THE THIRD GATE, and it strengthens the kit's whole thesis.** A certified electrical
  inspector shall not issue certificates of approval of temporary or permanent wiring "unless the
  inspector has in his or her possession a **notice of release**" from the local health department:
  initial release on application for the site evaluation (that is your CONSTRUCTION power), final
  release "upon approval of an on-site sewage disposal plan." Exception at (8)(c): does not apply in a
  county that has adopted the Uniform State Building Code and enforces on-site sewage permitting.
  => On a septic site the health department gates the plumbing permit (KRS 318.134(2)) **and** the
  electricity. Printed in KY.1 and KY.3.

### GAP CLOSED — wells, and the contrast is the point
**A Kentucky homeowner may NOT drill their own well.** KRS 223.405: "It is unlawful for any person …
to construct, alter, or repair a water well without first having obtained a valid certificate as a
water well driller or as a water well driller's assistant." **There is no homeowner exemption** — the
only KRS 223.425(3) exemption is for dowsers, and it expressly does not extend to installing wells.
No drilling permit is required; the controls are the certified driller, the well record filed with the
cabinet, and a fecal coliform test on a potable well (KRS 223.440). [H] Statute says **30 days** for the
record; the current reg 401 KAR 6:310 §1(6) says **60**. Real conflict — the kit prints neither number.
Farm carve-out by definition, KRS 223.400(7): "water well" excludes stock and general farmstead wells
"if the wells do not provide water for human consumption" — a farm DRINKING-water well is fully covered.
This is a sharp, printable contrast: electrical, plumbing, HVAC and septic all have homeowner routes;
the well does not.

### GAP CLOSED — floodplain, now firmly cited
**KRS 151.250(2)**, verbatim: "No person, city, county, or other political subdivision of the state
shall commence the filling of, or **place a building**, barrier, or obstruction of any sort in, any area
in the floodplain or floodway unless plans and specifications for such work have been submitted to and
approved by the cabinet and a permit issued as required in subsection (1) above." Subsection (1) opens
"**Notwithstanding any other provision of law**" and nothing conditions either subsection on a local
ordinance. So the state floodplain permit applies **in full in a county with no building permit at
all** — the pairing with 815 KAR 7:125 §2(2)(a) is now printed in KY.5.
Also verified: KRS 151.260(2) plans "shall be drawn by an engineer … unless waived by the cabinet"
(a real cost item); KRS 151.260(3) 20-working-day response; KRS 151.280(1) starting site preparation
before issuance counts as commencing without a permit; 401 KAR 4:060 §6(2)(a) lowest floor at or above
BFE; 401 KAR 4:050 §1 exemption where the stream's watershed is under one square mile.

### ADDED — KRS 198B.990(1), the penalty I had missed
"…shall be fined not less than ten dollars ($10) nor more than **one thousand dollars ($1,000)**. Each
day the violation continues shall constitute a separate offense." It reaches KRS 198B.140, **198B.6671
(installing HVAC without the permit)**, 198B.6672, the Uniform State Building Code and the Residential
Code. Ten times the plumbing penalty and now printed alongside it. [H] Not verified by me: KRS
198B.686(1) HVAC unlicensed practice = Class A misdemeanor; KRS 227A.130 electrical = $500–$5,000
and/or 10–180 days, but it penalizes only KRS 227A.020 violations and homeowners are exempted out of
227A by 227A.030(3).

### AVAILABLE BUT DELIBERATELY NOT PRINTED — the KRC's own tables
A sub-agent recovered the Kentucky Residential Code's internal amendments from **up.codes' reproduction**
of the code, not from a purchased copy (ICC Digital Codes 403s and HBC does not host the copyrighted
book). Its own confidence note: "for anything going into print I'd have someone eyeball a purchased
copy of the Third Edition." Under this kit's accuracy standard that is not a primary source, so **none
of the following was printed**, and the kit's silence on frost depth and seismic remains deliberate:
* Table R301.2(1) replaced by a Kentucky per-county table; ground snow 15 psf most counties, 20 psf in a
  northern/eastern band; **ultimate design wind speed 115 mph for all Kentucky counties**; weathering
  severe and termite moderate-to-heavy statewide. Kentucky's table omits winter design temp, ice
  barrier, air freezing index and mean annual temp — while R905.1.2 and R303.10 still key off them.
* Table R403.1.4 frost depth: **24 in for "All other KY Counties"**, 27 in (Bell, Clay, Knox, Lawrence,
  Owsley), 30 in (Boone, Breathitt, Campbell, Harlan, Johnson, Kenton, Leslie, Magoffin, Perry), 33 in
  (Floyd, Knott, Letcher, Martin, Pike). Plus Kentucky language allowing footings to bear on exposed
  solid rock without reaching frost depth.
* Table R301.2.2.1 seismic: **D2** Fulton, Hickman, Carlisle, Ballard, McCracken, Graves; **D1** Calloway,
  Marshall, Livingston; **D0** Lyon, Crittenden, Trigg, Caldwell, Union; **C** Webster, Henderson, McLean,
  Christian, Ohio; **B** everywhere else including Jefferson and Fayette. And R301.2.2 exempts detached
  one- and two-family dwellings in SDC A/B/C from the seismic provisions entirely — so seismic only
  bites in the far-western block.
* **R313 automatic sprinklers: DELETED** — the heading survives with no body. **Appendix F radon: NOT
  adopted** (R102.5 admits only Appendices K, R and S).
* R101.2 exception 3 exempts farm dwellings and farm buildings outside a municipality; R105.2 exempts
  sheds ≤200 sf, decks ≤200 sf and ≤30 in above grade if unattached and not serving the required exit
  door, fences ≤7 ft, retaining walls ≤4 ft.
**Recommendation for the second edition:** buy the 2018 Kentucky Residential Code, Third Edition and
verify these against it. The seismic table and the frost-depth table are the two highest-value pieces of
Kentucky content still missing from the kit, and the sprinkler/radon deletions would let the kit answer
two very common search queries.

### ALSO AVAILABLE, NOT YET PRINTED (second-edition candidates)
* **KRS 376.010(5) owner-occupied lien protection** — for a single or double family dwelling the
  non-privity notice window is a flat **75 days** (5)(a), and (5)(d) is genuinely protective: the lien
  "shall not be applicable to the extent that an owner-occupant … has, **prior to receipt of the notice**
  …, **paid the contractor**." (5)(e): the contractor cannot be the owner's authorized agent. Filing:
  KRS 376.080(1) six months, plus a copy mailed to the owner within 7 days or the lien dissolves;
  enforcement suit within 12 months (KRS 376.090(1)).
* **KRS 342.610(2) up-the-ladder workers' comp.** The trigger is work "of a kind which is a regular or
  recurrent part of the work of the trade, business, occupation, or profession of such person," so a
  one-time owner-builder is not "deemed a contractor." [H] There is **no express homeowner carve-out**;
  the only express exclusion in (2) is agricultural land, and KRS 342.650(2)'s 20-consecutive-work-day
  exemption covers "maintenance, repair, remodeling," **not new construction**. Risk to flag: someone who
  builds repeatedly, or who is in the construction trade, can be pulled in. Pairs with KRS 342.610(6),
  which requires the building official to demand proof of coverage before issuing the permit.
* **KRS 227A.020(6): local licensing of electricians is PREEMPTED**, not permitted — the chapter
  "shall supersede all ordinances or regulations regulating electricians … of any city, county,
  urban-county, charter county, or consolidated local government," preserving only zoning and
  occupational payroll taxes. Combined with KRS 82.082(1)–(2) home rule (a local power is barred where
  "there is a comprehensive scheme of legislation on the same general subject"), this explains the
  asymmetry precisely: locals **may** register general contractors (no state scheme exists) but **may
  not** license electricians or plumbers.
* **KRS 227.480(1)(a)** requires an electrical permit before commencing work, and **227.480(2)(a)**
  exempts "a homeowner or farmer who does construction, alteration, or repairs of any electrical system
  on his or her own premises" from the proof-of-licensure requirement — the homeowner gets the permit
  without a license. **815 KAR 35:020 §1(1)(b)**: a department inspector inspects "if a certified
  electrical inspector has not been made available by the local government" — the state electrical
  backstop that has no building-code equivalent.
* **The Division of Plumbing Inspector Itinerary** (dhbc.ky.gov/Documents/Itinerary 7.6.26.pdf) — a
  weekday county circuit assigning each state plumbing inspector a county per day with a **~90-minute
  daily availability window** (typically 8:00–9:30 am). Jefferson and Fayette are split by ZIP instead.
  This is arguably the single best practical detail in Kentucky owner-building and belongs in KY.4's
  next edition.
* **Roving contract inspectors** explain the rural pattern: KRS 198B.060(14)–(15) let local governments
  associate and contract out, and one named individual covers up to 11 counties. In Ballard, Carlisle,
  Hickman, Fulton and Graves the state inspector is contracted as the local inspector.
* **Eight different permit portal products** across ten sampled jurisdictions (OpenGov, iWorQ, GovBuilt,
  GovWell, Accela, Tyler EnerGov, SmartGov, Lexington's custom One-Stop Shop). There is no Kentucky
  standard — a sellable observation in its own right.
* Verified fee schedules for a worked-example table: **Lexington** $0.10/sq ft (min $150) + $180/unit,
  $25 residential plan review, double fees for work started without a permit; **Madison County**
  valuation-based, $380 for the first $100,000 plus $2.25 per additional thousand, $30 CO, $50 minimum.
  [H] The **state electrical permit fee sheet** (dhbc.ky.gov/documents/ElectricalPermitFee.pdf) is tiered
  by "complete value" and, read literally, would put a $300k house at $4,500 — almost certainly the
  value of the ELECTRICAL WORK, not the house. **Do not print a figure until HBC confirms the basis.**

### STILL OPEN AFTER THE ADDENDUM
1. The plumbing plan-submission conflict (item 26) — still needs an answer in writing from the Division
   of Plumbing.
2. Gallatin County has no published inspector sheet. Why, and who covers it?
3. 815 KAR 35:015 has a proposed amendment pending; 815 KAR 7:070 does too. Neither 7:120 nor 7:125 has
   one, so no move off the 2015 IRC is filed.
4. The state electrical permit fee valuation basis (above).
5. Whether the "January 1, 2025" NEC mandatory date repeated by the live state guide has any primary
   source. None was found; the documented date is 815 KAR 7:125's 12-3-2024 effective date.
