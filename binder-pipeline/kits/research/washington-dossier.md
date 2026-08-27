# Washington Owner-Builder Permit Kit — Research Dossier

Researched August 2026, primary-source-first. Every RCW and WAC quotation below was
pulled with `curl` from **app.leg.wa.gov** (the Washington State Legislature's own
text) and de-tagged locally, not read through a summariser or a third-party mirror.
Washington is unusually good for this: the Legislature publishes both the RCW and the
WAC as free HTML, and the State Energy Code is written *into* chapter 51-11R WAC
rather than incorporated by reference — so the numeric requirements are quotable
state rule text, not ICC copyright.

Agency pages (sbcc.wa.gov, lni.wa.gov, ecology.wa.gov, doh.wa.gov, dor.wa.gov,
dnr.wa.gov) were fetched live and checked for a 200 plus real content.

**Currency check.** Several load-bearing sections were amended recently and the
dossier quotes the *current* codified text: RCW 19.27.095 (2026 c 166 s 4),
RCW 36.70B.070 (2026 c 235 s 2; 2026 c 166 s 5), RCW 36.70B.080 (2026 c 235 s 3;
2025 c 208 s 5; 2023 c 338 s 7, effective 1/1/2025), RCW 19.27.031 (2024 c 170 s 1;
2024 c 133 s 1), RCW 19.28.261 (2021 c 51 s 1), WAC 246-272A-0250 (WSR 24-06-046,
effective 4/1/25). The 2021 residential and energy codes took effect **March 15,
2024** (WSR 23-23-104 for the IRC; WSR 24-03-084 for WSEC-R).

**Divergence from the sibling kits.** NC/GA/TX/VA all print a code-cited inspection
list. Washington adopts the IRC's administrative Chapter 1 as model text
(WAC 51-51-003 excludes only chapters 11 and 25–43), so the enumerated inspection
list is ICC's copyrighted text rather than a Washington rule this kit can quote and
verify line by line. WA.3 therefore prints the *common Washington sequence* with the
**agency** named for each call — which is the more useful axis here anyway — and says
plainly that the permit card governs. See Open Questions #1.

---

## The two traps

Washington has two facts that function the way NC's 2017-NEC carve-out does: widely
repeated wrong, checkable in a minute, and expensive to get wrong.

### Trap 1 (structural) — your electrical permit does not come from your building department

The rule that adopts the residential code hands electrical work to a different rule
book entirely. **WAC 51-51-003**:

> The 2021 edition of the *International Residential Code* as published by the
> International Code Council is hereby adopted by reference with the following
> additions, deletions, and exceptions: Provided that chapters 11 and 25 through 43
> of this code are not adopted. Energy Code is regulated by chapter 51-11R WAC;
> Plumbing Code is regulated by chapter 51-56 WAC; **Electrical Code is regulated by
> chapter 296-46B WAC or Electrical Code as adopted by the local jurisdiction.**

Chapter 296-46B WAC is the Department of Labor & Industries' rule book. The statute
behind it is blunter — **RCW 19.28.101(1)**:

> The director shall cause an inspector to inspect all wiring, appliances, devices,
> and equipment to which this chapter applies… **Nothing contained in this chapter
> may be construed as providing any authority for any subdivision of government to
> adopt by ordinance any provisions contained or provided for in this chapter except
> those pertaining to cities and towns pursuant to RCW 19.28.010(3).**

The local option is confirmed at **RCW 19.28.010(3)** ("This chapter shall not limit
the authority or power of any **city or town**… A city or town shall require that its
electrical inspectors meet the qualifications provided for state electrical
inspectors in accordance with RCW 19.28.321") and **RCW 19.28.010(4)**
("**Incorporated cities and towns** where electrical inspections are required by
local ordinances may enforce…").

**So counties cannot run electrical programs at all.** In unincorporated county —
which is where most owner-builders build — the electrical permit and every electrical
inspection come from the State. An owner-builder who assumes the county inspector
covers the rough-in covers wiring nobody approved, and **RCW 19.28.101(4)** says "No
electrical wiring or equipment subject to this chapter may be concealed until it has
been approved by the inspector making the inspection."

### Trap 2 (misquotation) — the "24 months" electrical rule is not the rule for your house

Nearly every guide, including our own live WA state guide, tells owner-builders they
must intend to occupy a new home for 24 months to do their own electrical. That
condition exists — but read where the sentence sits. **RCW 19.28.261(1)**:

> Nothing in RCW 19.28.161 through 19.28.271 shall be construed to require that a
> person obtain a license or a certified electrician in order to do electrical work
> at his or her residence or farm or place of business or on other property owned by
> him or her unless:
> (a) The electrical work is on the construction of a new building intended for rent,
> sale, or lease; or
> (b) The electrical work is on property that is offered for sale within 12 months
> after obtaining the property.
>
> **However, if the construction is of a new residential building with up to four
> units intended for rent, sale, or lease,** the owner may receive an exemption from
> the requirement to obtain a license or use a certified electrician if he or she
> provides a signed affidavit to the department stating that he or she will be
> performing the work and will occupy one of the units as his or her principal
> residence. The owner shall apply to the department for this exemption and **may
> only receive an exemption once every twenty-four months.** It is intended that the
> owner receiving this exemption shall occupy the unit as his or her principal
> residence for **twenty-four months** after completion of the units.

The affidavit, the 24-month occupancy intent and the once-every-24-months limit are
the terms of a **rescue route for buildings intended for rent, sale, or lease** — the
classic case being an owner building a fourplex and living in one unit. A
single-family house you are building to live in is not intended for rent, sale or
lease, so subsection (1) covers it directly.

The kit states this and still tells the reader to confirm with L&I, because the
distinction turns on a single sentence and L&I both issues the permit and forms its
own view of the applicant's intent.

### The asymmetry nobody notices

**Electrical** (RCW 19.28.261(1)) carries a rent/sale/lease carve-out and a 12-month
resale carve-out. **Plumbing** (RCW 18.106.150(1)) carries **neither**:

> Nothing in this chapter shall be construed to require that a person obtain a
> license in order to do plumbing work at his or her residence or farm or place of
> business or on other property owned by him or her.

That is the whole subsection. People assume the two trade exemptions mirror each
other. They do not, and the stricter one is the one people assume is looser.

---

## WA.0 — Cover summary facts

1. **No general contractor licence exists.** Washington regulates by *registration*
   under chapter 18.27 RCW. Working on your own property is exempt —
   RCW 18.27.090(12). No project-cost threshold, no affidavit before a licensing
   board, no statutory duty to attend inspections personally.
2. **Statewide, mandatory code, no opt-out.** RCW 19.27.031(1): "there shall be in
   effect in **all counties and cities** the state building code."
3. **Code stack in force (effective March 15, 2024):** 2021 IRC (ch. 51-51 WAC),
   2021 WSEC-R (ch. 51-11R WAC), Uniform Plumbing Code (ch. 51-56 WAC) — **UPC, not
   IPC**. Electrical: ch. 296-46B WAC (L&I) or the local city/town code.
4. **Three mandatory performance tests**, with no visual alternative to any of them:
   blower door at 4.0 ACH50, duct leakage, and verified ventilation airflow.
5. **The water gate.** RCW 19.27.097(1) makes evidence of an adequate water supply a
   precondition of the building permit, and in 15 named WRIAs the permit-exempt well
   is capped at 950 or 3,000 gpd with a $500 fee.
6. **The Washington twist:** one house, four agencies — city/county building, L&I (or
   a city) for electrical, the local health jurisdiction for septic, and a purveyor or
   Ecology for water.

---

## WA.1 — Owner-builder exemption

### The exemption — RCW 18.27.090(12), in full

> Any person working on his or her own property, whether occupied by him or her or
> not, and any person working on his or her personal residence, whether owned by him
> or her or not but this exemption shall not apply to any person who performs the
> activities of a contractor on his or her own property for the purpose of selling,
> demolishing, or leasing the property.

Two exemptions in one sentence: **own property** (occupancy irrelevant) and
**personal residence** (ownership irrelevant — this is how a tenant may work on the
home they live in). The carve-out is a **purpose** test, not a timing test; it sets no
number of months.

### The second exemption every owner-builder also uses — RCW 18.27.090(11)

> An owner who contracts for a project with a registered contractor, except that this
> exemption shall not deprive the owner of the protections of this chapter against
> registered and unregistered contractors. The exemption prescribed in this
> subsection does not apply to a person who performs the activities of a contractor
> for the purpose of leasing or selling improved property he or she has owned for
> **less than twelve months**.

Note it names **registered** contractors only. This is also where the twelve-month
rule people half-remember actually lives — (11), not (12), and coupled with a purpose
of leasing or selling.

### Other subsections worth knowing

- **(9)** — an undertaking whose aggregate contract price is under **$500** is
  "casual, minor, or inconsequential," expressly not where the work is part of a
  larger operation or split into sub-$500 contracts to evade the chapter.
- **(13)** — an owner performing maintenance, repair and alteration on their own
  properties, or using their own employees.
- **(14)** — licensed architects and engineers, certified electricians, and certified
  plumbers are exempt from contractor registration **within the scope of their
  certification**. Consequence for verification: a missing 18.27 registration on an
  electrician proves nothing until you have checked the chapter 19.28 licence.

### The penalty is the permit, not a fine — RCW 18.27.110

- (2)(a) the jurisdiction must **print the contractor registration number on the
  building permit**;
- (2)(b) and must give the applicant "a written notice… informing them of contractor
  registration laws and the potential risk and monetary liability to the homeowner
  for using an unregistered contractor" — a thing owner-builders are owed and rarely
  receive;
- (3) "If a building permit is obtained by an applicant or contractor who falsifies
  information to obtain an exemption provided under RCW 18.27.090, the building
  permit **shall be forfeited**."

### Trade exemptions

| Trade | Test | Authority |
|---|---|---|
| Electrical | Own property, **unless** new building intended for rent/sale/lease, or property offered for sale within 12 months of acquiring it | RCW 19.28.261(1) |
| Plumbing | Own property. No rent/sale/lease condition, no clock. Medical gas excluded | RCW 18.106.150(1), (7) |
| Mechanical/HVAC | No separate statewide certification; permitted and inspected locally. Refrigerant handling is federal | 40 C.F.R. Part 82, Subpart F |

Both chapters carry the same helper provision — RCW 19.28.261(6) and
RCW 18.106.150(6): a householder may assist or receive assistance from "a friend,
neighbor, relative, or other person when none of the individuals doing the…
installation hold themselves out as engaged in the trade or business."

Verification: **secure.lni.wa.gov/verify/** (checked live, HTTP 200).

---

## WA.2 — Permit application checklist

### The four state-law gates

1. **Proof of water** — RCW 19.27.097(1).
2. **A complete application** — RCW 19.27.095(1)–(2), RCW 36.70B.070. Completeness is
   what vests you and what starts the reviewer's clock.
3. **Energy credits on the drawings** — WAC 51-11R-40620 (§ R406.3), a submission
   requirement written into the code itself.
4. **The electrical permit is elsewhere** — WAC 51-51-003.

### Vesting — RCW 19.27.095(1)

> A valid and fully complete building permit application for a structure, that is
> permitted under the zoning or other land use control ordinances in effect on the
> date of the application shall be considered under the building permit ordinance in
> effect at the time of application, and the zoning or other land use control
> ordinances in effect on the date of application.

**RCW 19.27.095(2)** fixes minimum contents for any project over **$5,000**: legal
description or tax parcel number and street address; owner's name, address, phone;
**the prime contractor's business name, address, phone and current state contractor
registration number**; and either the interim-construction lender or the payment-bond
firm. Those details are then printed on the permit and on the posted inspection
record card (subsection (3)).

The registration-number line is the one that stops owner-builders — they are exempt
and have no number to write. **RCW 19.27.095(5)** is the related relief: missing
lender or bond information means the application "shall be processed forthwith" and
"shall not cause the application to be deemed incomplete for the purposes of
vesting."

### Water — the gate most owner-builders trip over

**RCW 19.27.097(1)(a)**:

> Each applicant for a building permit of a building necessitating potable water shall
> provide evidence of an adequate water supply for the intended use of the building.
> Evidence may be in the form of a water right permit from the department of ecology,
> a letter from an approved water purveyor stating the ability to provide water, or
> another form sufficient to verify the existence of an adequate water supply. **An
> application for a water right shall not be sufficient proof of an adequate water
> supply.**

Baseline — **RCW 90.44.050**: permit-exempt withdrawal "for single or group domestic
uses in an amount not exceeding **five thousand gallons a day**," plus lawn or
non-commercial garden up to half an acre.

The 2018 streamflow-restoration law replaced that in 15 WRIAs:

| Cap | WRIAs | Authority |
|---|---|---|
| **950 gpd** per connection, $500 fee, plus on-site stormwater management | 7 Snohomish, 8 Cedar-Sammamish, 9 Duwamish-Green, 10 Puyallup-White, 12 Chambers-Clover, 13 Deschutes, 14 Kennedy-Goldsborough, 15 Kitsap | RCW 90.94.030(3)(a)(vi) |
| **3,000 gpd** per connection, $500 fee | 1 Nooksack, 11 Nisqually, 22 Lower Chehalis, 23 Upper Chehalis, 49 Okanogan, 55 Little Spokane, 59 Colville | RCW 90.94.020(5)(f) |

Both read "An applicant shall pay a fee of five hundred dollars to the permitting
authority" and both are prefaced "**Until rules have been adopted that specify
otherwise**" — Ecology has been adopting basin rules since, so the kit tells the
reader to confirm the current figure. $350 of each fee is transmitted to Ecology
annually; restrictions are recorded against title.

Also from RCW 19.27.097(1): WRIAs 5, 17, 18, 27, 28, 32, 45, 46, 48 and 57 have
instream flow rules that **explicitly** regulate permit-exempt withdrawals (evidence
must match the specific rule); WRIAs 3 and 4 (Skagit) carry additional requirements
under ch. 173-503 WAC following *Swinomish Indian Tribal Community v. Department of
Ecology*, 178 Wn.2d 571 (2013); WRIAs 37, 38 and 39 (Yakima) are governed by
adjudicated rights. Elsewhere, a well report under ch. 18.104 RCW may itself
demonstrate availability (subsection (1)(g)).

### Septic — WAC 246-272A

**-0200(2)**: except for a minor repair, an applicant "shall submit an application and
obtain a permit from the local health officer **prior to beginning construction**,"
including the soil and site evaluation (-0220), a dimensioned site plan showing the
initial **and reserve** areas, and a design carrying the "name, signature and stamp of
the designer."
**-0200(4)(a)**: the health officer must respond within **30 days** (tracing to
RCW 70.05.074).
**-0200(4)(f)**: the permit's expiration "may not exceed **five years** from the date
of permit issuance."

Owner installation — **WAC 246-272A-0250(1)–(2)**:

> (1) Only installers may construct OSS, except as noted under subsection (2)…
> (2) The local health officer **may allow** the resident owner of a single-family
> residence to install the OSS for that single-family residence except when:
> (a) The primary and reserve areas are within **200 feet of marine water**;
> (b) The primary and reserve areas are within **100 feet of surface water**; or
> (c) The installation permit meets Table X standards in WAC 246-272A-0280.

Note *may allow* — discretionary, not a right — and note how much Puget Sound
waterfront the setbacks remove. Subsection (3) then binds the owner-installer as it
binds a professional: follow the approved design, keep it on site, change nothing
without the designer's and health officer's prior authorisation, be "on the site at
all times during the excavation and construction," and "cover the installation only
after the local health officer has given approval to cover."

Local health jurisdictions may add their own rules under WAC 246-272A-0013; forms and
fees are theirs.

### Code editions and the energy code

**RCW 19.27.031(1)** enumerates the adopted model codes: IBC, IRC, IMC (LP gas to
NFPA 58 / ANSI Z223.1-NFPA 54), IFC, the referenced portions of the IWUIC, and — note
— "**The Uniform Plumbing Code** and Uniform Plumbing Code Standards, published by the
International Association of Plumbing and Mechanical Officials: PROVIDED, That any
provisions of such code affecting sewers or fuel gas piping are not adopted." Not the
IPC. Conflicts resolve to the first-named code. Three-year adoption cycle,
subsection (3).

**Local amendments — RCW 19.27.060(1)(a):**

> no amendment to a code enumerated in RCW 19.27.031… that affects single-family or
> multifamily residential buildings shall be effective unless the amendment is
> approved by the building code council.

Three Washington amendments to the IRC an owner-builder trips over:

- **Sprinklers — WAC 51-51-0313.** "R313.2 One- and two-family dwellings automatic
  sprinkler systems. **This section is not adopted.**" Townhouse units do require
  them, except in townhouse buildings of no more than four units.
- **Radon — WAC 51-51-0332.** Appendix F applies in "high radon potential counties
  (zone 1) designated in Table AF101(1)" **and** "to all buildings constructed using
  the provisions of Section R408.3 Unvented crawl space compliance method." Choose a
  conditioned crawl space anywhere in the state and you have opted in.
- **Design criteria — WAC 51-51-0301.** "Additional criteria shall be established by
  the local jurisdiction and set forth in Table R301.2." Snow, wind, seismic design
  category and frost depth are local, in writing, not from a statewide table.

**Climate zones — WAC 51-11R-30100, Table R301.1.** All 39 counties, two zones only:

- **4C (Marine):** Clallam, Clark, Cowlitz, Grays Harbor, Island, Jefferson, King,
  Kitsap, Lewis, Mason, Pacific, Pierce, San Juan, Skagit, Snohomish, Thurston,
  Wahkiakum, Whatcom.
- **5B (Dry):** Adams, Asotin, Benton, Chelan, Columbia, Douglas, Ferry, Franklin,
  Garfield, Grant, Kittitas, Klickitat, Lincoln, Okanogan, Pend Oreille, **Skamania**,
  Spokane, Stevens, Walla Walla, Whitman, Yakima.

There is **no zone 6** in Washington's table. Skamania is 5B despite sitting west of
the crest — the geography-misleads case.

**Prescriptive envelope — WAC 51-11R-40213, Table R402.1.3.** One column, headed
"Climate Zone 5 and Marine 4," so the numbers are identical statewide:

| Component | Requirement | Footnote |
|---|---|---|
| Fenestration *U*-factor | 0.30 | 0.32 above 4,000 ft elevation (j) |
| Skylight *U*-factor | 0.50 | |
| Ceiling | **R-60** | R-38 for single rafter-/joist-vaulted ceilings where full depth extends over the top plate (e) |
| Wood frame wall | **R-20+5 or R-13+10** | first figure cavity, second continuous (i) |
| Floor | R-30 | |
| Below-grade wall | R-10/15/21 int + 5TB | R-5 thermal break between slab and basement wall (c) |
| Slab | R-10, 4 ft | R-10 continuous under heated slabs (d) |

**Credits — WAC 51-11R-40620, § R406.3:** 5.0 credits for a small dwelling unit
(<1,500 sq ft conditioned floor area with <300 sq ft fenestration), **8.0** for a
medium unit (everything not otherwise listed), **9.0** for a large unit (>5,000 sq ft),
6.5 for R-2 units, 2.0 for additions of 150–500 sq ft. And: "The drawings included
with the building permit application shall identify which options have been selected
and the point value of each option, regardless of whether separate mechanical,
plumbing, electrical, or other permits are utilized for the project."

**The three tests:**

| Test | Requirement | Section |
|---|---|---|
| Blower door | "The building or dwelling unit **shall** be tested for air leakage" (R402.4.1.2). "The maximum air leakage rate for any dwelling unit **under any compliance path** shall not exceed **4.0 air changes per hour**" at 50 Pa (R402.4.1.3.1). Signed report with verified location and time stamp to owner and code official. Only exception: additions under 500 sq ft | WAC 51-11R-40240 |
| Duct leakage | "Ducts shall be leak tested in accordance with WSU RS-33." Rough-in ≤4.0 cfm/100 sq ft CFA at 25 Pa (≤3.0 without the air handler); post-construction ≤4.0; ducts and air handlers entirely inside the envelope ≤8.0 — **"Ducts located in crawl spaces do not qualify for this exception"** | WAC 51-11R-40320, §§ R403.3.5–.3.6 |
| Ventilation airflow | "Mechanical ventilation systems shall be tested and verified to provide the minimum ventilation flow rates required by Section R403.6." Signed written report to the code official. Whole-house mechanical ventilation required in the first place (R403.6) | WAC 51-11R-40350 |

Duct insulation, for completeness: R-8 for ducts ≥3 in. outside conditioned space, R-6
under 3 in., R-10 in slab or ground (R403.3.1).

### Who may draw the plans — RCW 18.08.410(5)

> [This chapter shall not affect or prevent] Any person from doing design work
> including preparing construction contract documents and administration of the
> construction contract for the erection, enlargement, repair, or alteration of a
> structure or any appurtenance to a structure **regardless of size**, if the
> structure is to be used for a residential building of up to and including four
> dwelling units…

No architect's stamp is required by the licensing statute at any square footage. That
is licence, not code — where the building code demands calculations (and much of
western Washington's seismic design category does), they are still required.

### What the State guarantees the applicant

- **RCW 36.70B.070(1), (4)(a)** — written completeness determination within **28
  days**; "an application shall be deemed procedurally complete on the **29th day**"
  if the jurisdiction says nothing.
- **RCW 36.70B.080(1)(d)** — final decision within **65 days** (no public notice),
  **100 days** (notice), **170 days** (notice and hearing), from the determination of
  completeness. Subsection (1)(g) excludes time spent waiting on the applicant, EIS
  preparation, and appeal periods.
- **RCW 36.70B.080(1)(l)** — "When permit time periods… are not met, a portion of the
  permit fee **must be refunded**": **10%** if the overrun is within 20% of the
  original period, **20%** beyond. A jurisdiction may instead collect only 80% up
  front. Does not apply to a jurisdiction that has implemented at least three of the
  RCW 36.70B.160(1) options.
- **RCW 19.27.060(1)(a)** — SBCC approval required for local residential amendments.

Caveat carried into the kit: chapter 36.70B RCW binds jurisdictions "planning pursuant
to RCW 36.70A.040" (fully planning under the GMA). Most of the state's population, but
the kit says "ask whether yours does" rather than asserting universality.

---

## WA.3 — Inspection sequence

Building, plumbing and mechanical from the city or county; **electrical from L&I or an
incorporated city**; septic pre-cover from the local health officer; the three tests
from a third-party tester.

Two rights on the electrical side, both from **RCW 19.28.101(2)** and both worth the
price of the kit on their own:

> Upon request, electrical inspections will be made by the department within
> **forty-eight hours**, excluding holidays, Saturdays, and Sundays. If, upon
> **written** request, the electrical inspector fails to make an electrical inspection
> within twenty-four hours, the serving utility may immediately connect electrical
> power to the installation if the necessary electrical work permit is displayed.

Note *written* — a phone call does not start that clock.

Other operative provisions: **19.28.101(3)** — 15 days to correct after notice, "or
such further reasonable time as may upon request be granted"; inspector may order
service disconnected and reconnection without approval is unlawful. **19.28.101(4)** —
nothing concealed before approval, and work must be "sufficiently accessible to permit
the inspector to employ any testing methods." **19.28.101(5)** — inspection and
approval required "before requesting the electric utility to connect."
**WAC 246-272A-0250(3)(g)** — cover the septic system only after the health officer
approves.

---

## WA.4 — Where to file

Four agencies, one house. Domains fetched live August 2026 (HTTP 200 unless noted):

**State:** lni.wa.gov · secure.lni.wa.gov/verify/ · sbcc.wa.gov · ecology.wa.gov ·
doh.wa.gov · dor.wa.gov · wsdot.wa.gov · dnr.wa.gov · app.leg.wa.gov

**Counties:** kingcounty.gov · piercecountywa.gov (403 to automated agents; domain
resolves and is correct) · snohomishcountywa.gov · spokanecounty.gov · clark.wa.gov ·
thurstoncountywa.gov · kitsap.gov · yakimacounty.us · whatcomcounty.us ·
bentoncountywa.gov · franklincountywa.gov · skagitcounty.net · islandcountywa.gov ·
lewiscountywa.gov

**Separate health jurisdictions:** tpchd.org (Tacoma-Pierce) · snohd.org (Snohomish) ·
srhd.org (Spokane Regional) · kitsappublichealth.org (Kitsap) · bfhd.wa.gov
(Benton-Franklin, serving both counties)

**Statewide directories:** local health jurisdictions at doh.wa.gov → About Us →
Washington's Public Health System → Local Health Jurisdictions (verified 200);
building departments via wabo.org (Washington Association of Building Officials — a
professional association, **not** a government agency); mrsc.org (Municipal Research
and Services Center — likewise non-governmental).

**Deep links were rejected on evidence.** Several county deep links returned HTTP 200
for an unrelated page — `yakimacounty.us/151/Building-Codes` resolved to "Victim Impact
Panel," `whatcomcounty.us/319/Planning-Development-Services` to "Safety Training."
The kit prints domains and navigation routes only. **No phone numbers anywhere**;
write-in rules instead, per the house standard.

---

## WA.5 — Forms index

Fifteen documents across the four agencies, plus the one nobody warns about: the
**invoice**. Building a house for your own occupancy makes you the *consumer*, so every
trade you hire directly is a "prime contractor" performing for a consumer, and
**WAC 458-20-170(4)(a)**: "Prime contractors are required to collect from consumers the
retail sales tax measured by the full contract price. Where no gross contract price is
stated, the measure of sales tax is the total amount of construction costs including
any charges for licenses, fees, permits, etc." Labour included. State rate 6.5%
(**RCW 82.08.020(1)**) plus local rates — real money on a house, and a genuine shock
to buyers arriving from states that do not tax construction labour. Rate lookup at
dor.wa.gov/taxes-rates/sales-use-tax-rates (verified 200).

Related definition worth having: a "speculative builder" is "one who constructs
buildings for sale or rental upon real estate owned by him" (WAC 458-20-170(2)(a)) and
"must pay sales tax upon all materials purchased by them and on all charges made by
their subcontractors" ((2)(e)) — a different tax posture that pairs neatly with losing
the RCW 18.27.090(12) exemption.

---

## Consolidated claims manifest

| Claim | Citation |
|---|---|
| Own-property / personal-residence exemption; selling/demolishing/leasing carve-out | RCW 18.27.090(12) |
| Owner contracting with a registered contractor; twelve-month carve-out | RCW 18.27.090(11) |
| $500 casual/minor threshold; anti-splitting | RCW 18.27.090(9) |
| Owner maintenance/repair/alteration on own properties | RCW 18.27.090(13) |
| Certified electricians/plumbers exempt from registration in scope | RCW 18.27.090(14) |
| Registration number printed on permit; written notice about unregistered contractors | RCW 18.27.110(2) |
| Permit forfeited if an exemption is obtained by falsification | RCW 18.27.110(3) |
| Homeowner electrical exemption; rent/sale/lease and 12-month carve-outs; 24-month affidavit route | RCW 19.28.261(1) |
| Friend/neighbour/relative helper provision | RCW 19.28.261(6); 18.106.150(6) |
| Homeowner plumbing exemption, no rent/sale/lease condition; medical gas excluded | RCW 18.106.150(1), (7) |
| L&I inspects electrical; only cities and towns may legislate in the field | RCW 19.28.101(1); 19.28.010(3), (4) |
| 48-hour inspection commitment; 24-hour written-request remedy | RCW 19.28.101(2) |
| 15 days to correct; disconnection powers | RCW 19.28.101(3) |
| Nothing concealed before approval; accessibility at inspection | RCW 19.28.101(4) |
| No utility connection before approval | RCW 19.28.101(5) |
| State building code in all counties and cities; UPC not IPC; three-year cycle | RCW 19.27.031(1), (3) |
| SBCC approval required for local residential amendments | RCW 19.27.060(1)(a) |
| Vesting on a complete application | RCW 19.27.095(1) |
| Application contents over $5,000; missing lender/bond data does not break vesting | RCW 19.27.095(2), (3), (5) |
| Evidence of adequate water supply; water right application insufficient; WRIA lists | RCW 19.27.097(1) |
| 5,000 gpd permit-exempt domestic baseline | RCW 90.44.050 |
| 3,000 gpd cap + $500 fee, WRIAs 1/11/22/23/49/55/59 | RCW 90.94.020(5)(f) |
| 950 gpd cap + $500 fee + on-site stormwater, WRIAs 7/8/9/10/12/13/14/15 | RCW 90.94.030(3) |
| Anyone may design a residential building up to four dwelling units, any size | RCW 18.08.410(5) |
| 28 days to completeness; deemed complete day 29 | RCW 36.70B.070(1), (4)(a) |
| 65/100/170-day decision clocks; excluded time | RCW 36.70B.080(1)(d), (g) |
| 10%/20% fee refund; 80% up-front option; the 36.70B.160 exception | RCW 36.70B.080(1)(l) |
| Retail sales tax on the full contract price incl. labour; speculative builder definition | WAC 458-20-170(4)(a), (2) |
| 6.5% state sales tax rate | RCW 82.08.020(1) |
| 2021 IRC adopted; ch. 11 and 25–43 not adopted; electrical sent to 296-46B WAC or local | WAC 51-51-003 |
| One- and two-family sprinkler section not adopted; townhouse rule and four-unit exception | WAC 51-51-0313 |
| Radon Appendix F in zone 1 counties and in any unvented-crawl-space house | WAC 51-51-0332 |
| Local jurisdiction sets Table R301.2 design criteria | WAC 51-51-0301 |
| All 39 counties are 4C or 5B; Skamania is 5B | WAC 51-11R-30100, Table R301.1 |
| One prescriptive envelope column statewide; R-60 ceiling; R-20+5 or R-13+10 wall; U-0.30 | WAC 51-11R-40213, Table R402.1.3 |
| Air leakage testing mandatory, 4.0 ACH50 under any compliance path | WAC 51-11R-40240 |
| Duct leak test and leakage limits; crawl spaces excluded from the 8.0 allowance | WAC 51-11R-40320 |
| Whole-house ventilation required; airflow tested and verified | WAC 51-11R-40350 |
| Energy credits 5.0/8.0/9.0; options shown on the drawings | WAC 51-11R-40620 |
| Septic permit from the local health officer before construction; 30-day response; ≤5-year permit | WAC 246-272A-0200(2), (4)(a), (4)(f) |
| Resident owner may be allowed to install; 200 ft marine / 100 ft surface water exclusions; cover only after approval | WAC 246-272A-0250(1)–(3) |
| Local health jurisdictions may adopt additional rules | WAC 246-272A-0013 |
| IWUIC ignition-resistant provisions adopted on completion of the DNR maps | RCW 19.27.560; RCW 43.30.580 |

URL patterns: `app.leg.wa.gov/RCW/default.aspx?cite=18.27.090` and
`app.leg.wa.gov/WAC/default.aspx?cite=296-46B-925`, chapter and section swapped in.

---

## Deliberately omitted — and why

1. **The radon Zone 1 county list.** WAC 51-51-0332 points at "Table AF101(1)" — the
   IRC's own table, ICC copyright, not reproducible from a free primary source. EPA's
   radon-zone page and DOH's radon page both 404'd on the paths tried. The kit cites
   the rule, names both triggers, and tells the reader to look their county up in the
   code book or ask the building department. **Better an instruction than a guessed
   county list.**
2. **L&I electrical permit fee amounts.** RCW 19.28.101(6) sets fees by rule
   (WAC 296-46B-905). Not verified line by line in time; the kit tells the reader to
   confirm the current fee with L&I rather than printing a number that ages badly.
3. **Permit fees and processing timelines generally.** No statewide source exists and
   the per-jurisdiction figures circulating online are unsourced. The kit prints the
   *statutory clocks* instead, which are real and enforceable.
4. **IRC Chapter 1 inspection subsection numbers (R109.x).** Adopted as ICC model text
   rather than rewritten into the WAC, so not independently verifiable from a
   Washington primary source. WA.3 prints the common sequence with the agency named
   and says the permit card governs. See Open Questions #1.
5. **Whether the WUI ignition-resistant provisions bind a given parcel.** RCW
   19.27.560(1) adopts them "upon the completion of a statewide wildfire hazard map
   and a base-level wildfire risk map for each county… per RCW 43.30.580," and SBCC's
   DNR Maps page states "Maps are now live for the Wildland Urban Interface Code and
   the Tsunami Code" — so the condition appears satisfied. But no adoption date was
   published on that page, so the kit does not assert one; it points at SBCC and says
   confirm with the building department. Resources: sbcc.wa.gov → State Codes,
   Regulations & Guidelines → Wildland-Urban Interface Code Resources (story map at
   `storymaps.arcgis.com/stories/7016c437623a445997c072a05e26afbb`, verified 200) and
   → DNR Maps.
6. **A count of Washington cities and towns.** The kit says "39 counties and hundreds
   of cities and towns." The 39 is certain; the city count was not verified against a
   primary source, so it is not printed as a number.
7. **Which specific cities run their own electrical programs.** L&I's roster was not
   located from a primary source in time. Because the statute makes this a
   *city-and-town* question with counties categorically excluded, the kit gives the
   reader a decisive two-call procedure instead of a list that would go stale. **This
   is the highest-value gap to close in a future revision** — a verified roster would
   let the kit answer the question directly rather than delegating it.
8. **Septic designer self-preparation.** WAC 246-272A-0200(2)(a)(x) requires the
   designer's "name, signature and stamp," and designers are licensed under ch. 18.210
   RCW; the exemption structure of that chapter was not run to ground (RCW 18.210.020
   is unprofessional conduct, not exemptions). The kit says to ask the local health
   jurisdiction whether you may prepare your own design.

---

## Open questions / hedges

1. **IRC Chapter 1 and local amendment practice.** Chapter 1 *is* adopted
   (WAC 51-51-003 excludes only chapters 11 and 25–43, and WAC 51-51-01010 amends
   R101), so R105 permit expiry and R109 inspections are the statewide baseline. But
   RCW 19.27.060(1) lets locals amend, subject to SBCC approval for residential, and
   jurisdictions do amend administrative provisions. The kit therefore asserts the
   *agency* split (statutory, hard) and hedges the *list and order* (local). Worth
   revisiting if a future revision can verify how many jurisdictions amend Chapter 1.
2. **GMA coverage for the permit clocks.** Chapter 36.70B RCW binds jurisdictions
   planning under RCW 36.70A.040. The kit says "most of the state's population — ask
   whether yours does." A verified count of fully-planning counties would let this be
   stated precisely.
3. **UNCONFIRMED — future code effective dates.** The live WA state guide asserts "the
   2024 building codes take effect **May 3, 2027**" and "the **2026 NEC** takes effect
   **December 31, 2026**." **Neither could be confirmed** from SBCC or L&I in this
   research pass. They are not printed anywhere in the kit, and they should be
   re-verified before the state guide is next updated. If true they matter — a permit
   filed near either date vests to a different edition (RCW 19.27.095(1)).
4. **WRIA rule supersession.** Both RCW 90.94.020(5) and 90.94.030(3) apply "until
   rules have been adopted that specify otherwise." Ecology has been adopting basin
   rules since 2018, so the 950 and 3,000 gpd figures may be superseded in specific
   basins. The kit states the statutory defaults, flags the supersession clause
   explicitly, and directs the reader to Ecology. A future revision could check
   ch. 173-5xx WAC basin by basin.
5. **Yakima County's local health jurisdiction.** `yakimapublichealth.org` did not
   resolve. The kit routes Yakima readers through the DOH directory rather than
   guessing a domain.
6. **L&I homeowner permit mechanics.** Whether L&I still requires a property owner to
   obtain the permit in person and answer competency questions was not verified. The
   kit's checklist line asks the reader to confirm "which property owner electrical
   permit applies to your job and what it costs" rather than describing a process that
   may have moved online.

---

## Kit output

Six documents, **35 pages**, `check.py` clean, `wa-permit-kit.zip` built.

| Document | Pages |
|---|---|
| WA.0 Cover & How to Use | 3 |
| WA.1 Owner-Builder Exemption Walkthrough | 7 |
| WA.2 Permit Application Checklist | 11 |
| WA.3 Inspection Sequence | 6 |
| WA.4 Where to File Directory | 5 |
| WA.5 Forms & Documents Index | 3 |
