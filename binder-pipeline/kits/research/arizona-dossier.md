# Arizona Owner-Builder Permit Kit — Research Dossier

Kit 22 of the 50-state program (phase 5 with ID, NY, NE). Compiled September
2026 for `binder-pipeline/kits/az-permit-kit/` (AZ.0–AZ.5).

**Marking convention.** `[V]` = read in a primary source and quoted here.
`[H]` = secondary, inferred, or reasoned — not printed in the kit as a
citation. Anything unverifiable was deleted rather than softened.

**Primary sources used.**

| Source | What it is | Where |
|---|---|---|
| A.R.S. Title 32, Ch. 10 (§§ 32-1101 et seq.) | Registrar of Contractors statute; § 32-1121 exemptions | azleg.gov/ars/32/01121.htm |
| A.R.S. Title 9, Ch. 7, Art. 1 (§§ 9-801 et seq.) | Municipal building codes | azleg.gov/ars/9/ |
| A.R.S. Title 11, Ch. 6, Art. 3 (§§ 11-861 et seq.) | County building codes | azleg.gov/ars/11/ |
| A.R.S. Title 45 (§§ 45-454, 45-595 et seq.) | Groundwater Code — exempt wells, well construction | azleg.gov/ars/45/ |
| A.R.S. Title 33, Ch. 7 (§§ 33-981, 33-992.01, 33-1002) | Mechanics' liens; owner-occupant shield | azleg.gov/ars/33/ |
| A.R.S. Title 23, Ch. 6 (§§ 23-901, 23-902, 23-961) | Workers' compensation | azleg.gov/ars/23/ |
| A.R.S. Title 49, Ch. 2 (§§ 49-107, 49-241, 49-245) | Aquifer protection permits; delegation | azleg.gov/ars/49/ |
| A.R.S. §§ 36-1681, 45-311–315, 28-8482, 34-451, 37-1383, 33-439 | Pool barriers; plumbing fixtures; military-airport noise; public-building energy; state fire code; solar covenants | azleg.gov |
| A.A.C. Title 18, Ch. 9, Art. 3 (R18-9-A301–A316, E302) | ADEQ onsite wastewater general permits | LII reproduction (current to 29 A.A.R. 1023, eff. 19 Jun 2023); SOS Supp. 17-4 compilation via Cochise County; La Paz County setback table and ADEQ forms |
| A.A.C. Title 12, Ch. 15, Art. 8 (R12-15-801–822) | ADWR well construction rules | LII reproduction |
| ROC pages | License classifications; FAQ (read in browser) | roc.az.gov |
| Cochise County Owner-Builder Amendment | County ordinance text (PDF) and program page | cochise.az.gov |
| County and city adopting ordinances and code pages | Code editions in force (20 cities, 15 counties) | each jurisdiction, read by research subagents 3 Sep 2026 |

> **Fetching note for future revisions.** `azleg.gov` serves every statute
> section as clean HTML at `https://www.azleg.gov/ars/<title>/<section>.htm`
> with the title **unpadded** and the section zero-padded to five digits
> (`/ars/9/00835.htm`, `/ars/32/01121.htm`); decimal sections use a hyphen
> (`/ars/9/00470-01.htm`, not `00470.01`). The title tables of contents at
> `https://www.azleg.gov/arsDetail/?title=<n>` list every section and are
> the way to spot dual versions (Title 32 lists "32-1121" and "32-1121;
> Version 2"). A default curl works; a browser User-Agent is harmless.
> **`apps.azsos.gov` (the A.A.C. PDFs), `azdeq.gov`, `static.azdeq.gov`,
> `legacy.azdeq.gov`, `azwater.gov`, `roc.az.gov` and `dffm.az.gov` all sit
> behind a JavaScript challenge that returns HTTP 403 to curl and to
> WebFetch regardless of headers.** roc.az.gov and apps.azsos.gov load in
> the Chrome extension (the A.A.C. PDF renders but yields no extractable
> text and is 4.7 MB); azwater.gov and dffm.az.gov were not on the
> extension's allowed-domain list. Workarounds used: the Legal Information
> Institute's reproduction of the A.A.C. (`law.cornell.edu/regulations/
> arizona/Ariz-Admin-Code-SS-R18-9-A312`, section by section, with the
> agency's historical notes), Cochise County's hosted copy of the Secretary
> of State's 18 A.A.C. 9 compilation (Supp. 17-4, two-column PDF, text
> interleaves badly), and La Paz County's posted ADEQ forms. County and
> city sites are mostly curl-friendly with a browser User-Agent; Apache
> County, Santa Cruz County, Mesa, Surprise and Queen Creek are not.

---

## 0. THE HEADLINE — WHAT MAKES THIS KIT DIFFERENT

Arizona is sold as the "no statewide code" state, and that is true. What the
circulating advice gets wrong is the next step: it turns "no statewide code"
into "no permit," "no rules," and "varies locally" for things that are in
fact fixed by statute for every lot in the state. The kit's value is the
line between the two.

Six findings carry the kit:

1. **There is no statewide building code, but there IS a statewide building
   permit.** `[V]` § 11-321(A): every board of supervisors "shall require a
   building permit for any construction of a building … exceeding a cost of
   $1,000." A "no-permit county" does not exist. A "no-code county" does —
   Greenlee, in its own engineer's words — and two counties (Cochise on
   ≥ 4-acre parcels, Coconino under 600 sq ft) let a rural owner-builder opt
   out of plan review and inspection while keeping the permit.
2. **The owner-builder statement is statutory, on every application, and
   lying on it is a crime.** `[V]` § 32-1169(A) requires a signed statement of
   the exemption claimed *and the name and licence number of every licensed
   general, mechanical, electrical and plumbing contractor to be used*; (B)
   makes a false statement unsworn falsification. The "no statewide
   owner-builder form" line in the published guide is wrong in the way that
   matters.
3. **The one-year rule has an off-switch, and it is the same status that
   blocks subcontractor liens.** `[V]` § 32-1121(A)(5) disapplies the prima
   facie presumption "in an action against an owner-occupant as defined in
   section 33-1002" — a natural person with a deed **recorded before
   construction starts** who resides in the house at least 30 days in the
   year after completion. § 33-1002(B): no lien against that person's
   dwelling "except by a person having executed in writing a contract
   directly with the owner-occupant." *Record the deed, move in* is the
   kit's first instruction. The trap on the other side: "rent" includes
   compensation in "labor."
4. **The permit clocks apply to city house permits and not to county
   ones.** `[V]` § 9-835 gives a city applicant posted time frames, one
   comprehensive request for corrections, an automatic fee refund and a bar
   on mid-build plan changes; § 11-1605(M)(2) removes every licence
   "necessary for the construction or development of a residential lot"
   from the county equivalent. In unincorporated Arizona the only statutory
   clock is inspections "at the earliest reasonable time."
5. **Septic and wells are the real statewide code.** `[V]` ADEQ's
   R18-9-A312(C) table (100 ft to a well; **50 ft to a property line on a
   well-served lot**, reducible to 5 ft by a recorded neighbour waiver; 100%
   reserve area) and ADWR's R12-15-818 (100 ft from any septic system, from
   the well's side) bind everywhere, including under the Cochise and
   Greenlee no-inspection regimes. An owner may drill their own exempt well
   on a no-fee single well licence — after passing ADWR's exam.
6. **Arizona licenses contractors, not tradespeople, and the owner is
   expressly not a contractor.** `[V]` § 32-1101(A)(10)(b) removes "an owner
   making improvements to the owner's property pursuant to section 32-1121,
   subsection A, paragraph 5" from the definition of residential contractor.
   Owner-occupant electrical and plumbing is therefore not a "varies
   locally" question at the state level; the local variable is whether the
   AHJ issues the permit, and every AHJ site read draws the line at rentals.

---

## 1. THE CENTRAL THESIS — WHO ENFORCES

Arizona has **no statewide residential building code**. Every code that
governs a house is adopted locally by reference. But the state is not a
"no-rules" state: a **county building permit is mandatory statewide by
statute**, a short list of statewide rules bind regardless of local code, and
the state's own "regulatory bill of rights" clocks run against the permit
counter. The kit's job is to separate exactly what is statewide from what is
local.

### 1.1 Cities and towns — A.R.S. Title 9, Ch. 7, Art. 1 `[V]`

**§ 9-801(1)**: "Code" means "a published compilation of rules or regulations
prepared by a technical trade association and includes any building code,
electrical wiring code, health or sanitation code, fire prevention code,
wildland-urban interface code…"

**§ 9-802**: "A municipality may enact the provisions of a code or public
record theretofore in existence without setting forth the provisions, but
**the adopting ordinance shall be published in full**." At least three paper
copies, or one paper plus one electronic copy, "shall be filed in the office
of the clerk of the municipality and kept available for public use and
inspection. A code or public record enacted by reference may be amended in
the same manner."

Consequence for the kit: the authoritative statement of what code edition
binds a city lot is **the adopting ordinance on file with the city clerk**,
not the building department's web page. AZ.4 tells the reader to ask for the
ordinance number.

### 1.2 Counties — A.R.S. Title 11, Ch. 6, Art. 3 `[V]`

**§ 11-861(A)**, verbatim:

> "In any county that has adopted zoning pursuant to this chapter, the board
> of supervisors **may** adopt and enforce, for the unincorporated areas of
> the county so zoned, a building code and other related codes to regulate
> the quality, type of material and workmanship of all aspects of
> construction of buildings or structures, **except that the board may
> authorize that areas zoned rural or unclassified may be exempt from the
> provisions of the code adopted**."

Three things follow, all statutory:

1. A county building code is **optional** ("may adopt"). A county can lawfully
   have none. **Greenlee County has none** — see § 1.6.
2. A county may **exempt rural or unclassified zones** from its code. This is
   the statutory root of the Cochise County Owner-Builder Amendment and the
   Coconino County Alternative Methods and Materials program (§ 1.5).
3. It is conditioned on zoning. No zoning, no building code.

**§ 11-861(C)(1)**: county codes are limited to "any building, electrical,
plumbing or mechanical code that has been adopted by any national organization
or association that is organized and conducted for the purpose of developing
codes **or that has been adopted by the largest city in that county**. If the
board of supervisors adopts a city code, it shall adopt, within ninety days
after receiving a written notification of a change to the city code, the same
change or shall terminate the adopted city code." (Yuma County uses this
route and adopts the City of Yuma's code — § 3.)

**§ 11-862(A)**: any county code "shall contain a provision for an advisory
board consisting of at least five members in order to determine the
suitability of alternative materials and construction and to permit
interpretations of the provisions of such code." Members: a licensed
architect, a licensed engineer, a licensed general contractor, a member of
the public, and a person in the electrical, mechanical or plumbing trade. This
is the county-level appeal/alternative-methods body; AZ.3 names it.

**§ 11-863(B)**: "any such rules or regulations relating to inspections shall
require that such inspections be made **at the earliest reasonable time**."
(C): the board "may establish and charge reasonable fees for permits issued
and inspections made pursuant to any code." No state fee schedule exists.

**§ 11-864**: the adopting ordinance "shall be published in full"; copies filed
with the clerk of the board or the county planning and zoning department.

**§ 11-866**: "A penalty clause contained in a code adopted by reference shall
not be adopted by reference but shall be set forth in full in the adopting
ordinance. The penalty provisions of section 11-815 may be applied."

### 1.3 The county building PERMIT is mandatory statewide — the finding that kills "no-permit counties" `[V]`

**§ 11-321(A)**, verbatim:

> "Except in those cities and towns that have an ordinance relating to the
> issuance of building permits, the board of supervisors **shall require a
> building permit for any construction of a building or an addition to a
> building exceeding a cost of $1,000** within its jurisdiction. The building
> permit shall be filed with the board of supervisors or its designated
> agent."

**§ 11-321(G)**: one copy of every permit goes to the county assessor and one
to the Department of Revenue, with permit number, issue date and parcel
number; on CO, certificate of completion, expiration or cancellation, both are
notified again. **The permit is a tax event.** § 9-467(A) is the identical
rule for cities.

**§ 11-815(B)** (zoning enforcement), verbatim: "it is unlawful to erect,
construct, reconstruct, alter or use any building or other structure within a
zoning district covered by the ordinance without first obtaining a building
permit from the inspector and for that purpose the applicant shall provide
the zoning inspector with **a sketch of the proposed construction containing
sufficient information for the enforcement of the zoning ordinance**. A permit
is not required for repairs or improvements of a value not exceeding five
hundred dollars." The inspector "shall issue the permit when it appears that
the proposed erection … fully conforms to the zoning ordinance. In any other
case the inspector shall withhold the permit."

**§ 11-815(C)**: violation of a zoning ordinance is a **class 2 misdemeanor**;
"Each day … is a separate offense." (D): civil penalties up to the class 2
maximum, per day. (H): the board, county attorney, inspector "or any adjacent
or neighboring property owner who is specially damaged" may sue for
injunction or abatement.

**So the correct statement is:** every Arizona county must issue a building
permit for a house; what differs is whether that permit carries a *building
code* (plan review and inspections) or is only a *zoning/floodplain/assessor*
permit. Greenlee County's own engineer says it exactly this way — § 1.6.

### 1.4 Unlicensed "no-code" is not "no-rules" `[V]`

Even where no county building code exists, these statewide rules apply
(details and cites in § 2.2): the ROC exemption conditions (§ 32-1121), the
septic Aquifer Protection Permit (§ 49-241(B)(9)), the ADWR well rules
(§§ 45-454, 45-595, 45-596), pool barriers (§ 36-1681), water-saving plumbing
fixtures (§ 45-312), the ban on mandatory residential sprinklers (§ 11-861(E),
§ 9-807), and military-airport sound attenuation (§ 28-8482).

### 1.5 The two county opt-outs `[V]`

**Cochise County — Owner-Builder Amendment.** Read from the county's own
PDF, "Amendment to the Cochise County Building Safety Code for Rural
Residential Owner-Built Dwellings and Accessory Structures," and its
Development Services page, September 2026.

- Purpose (Sec. 1): "to exempt a Rural Residential Owner-Builder from the
  requirement for construction plan review and inspections under the
  currently adopted version of the Cochise County Building Safety Code,
  provided the property is located in a Zoning District with a minimum
  parcel size of **four-acres per dwelling unit** and the subject parcel is
  **at least four-acres** in size."
- What survives (Sec. 1): "By statute, this exemption does not exempt
  owner-builders from state, county building codes, or fire-district adopted
  fire codes and regulations regarding smoke detectors, nor does it exempt
  owner-builders from health regulations regarding wastewater treatment
  systems."
- Definition of owner-builder (Sec. 3(B)) is § 32-1121(A)(5) verbatim, and
  Sec. 4(A) repeats the one-year prima facie rule verbatim.
- Frequency limit (Sec. 2): "limited to use by the owner-builder **once in
  every five years** for Residential Dwellings on all properties within the
  unincorporated area of Cochise County owned by that individual."
- Two options (Sec. 5): **Option 1** — full plan review, but "only limited
  Building Code inspections dealing with the trade areas of Mechanical,
  Electrical, Plumbing and Fire Prevention"; **Option 2** — "no building code
  inspections … no construction plans are required to be submitted or
  reviewed."
- **Recording trap** (Sec. 6): "Each time a permit is issued pursuant to this
  amendment … a notice that a permit has been issued pursuant to the
  provisions of this article **shall be recorded with the County Recorder**."
  This follows the title forever.
- Sec. 7: "does not affect the requirement that prior to construction the
  Rural Residential Owner-Builder must obtain all permits required under
  State law and County ordinance."
- Plans may be hand-drawn (Sec. 9). Permit life **36 months**, one 12-month
  extension on written request with substantial progress (Sec. 12).
  Inspections requested **24 hours** in advance (Sec. 15).
- CO: Option 1 yields a "**conditioned** Certificate of Occupancy" (Sec. 16);
  the county page states Option 2 is "not eligible for a Certificate of
  Occupancy."
- Electrical (Sec. 21): "No dwelling or accessory structure constructed
  pursuant to this amendment shall be required to be connected to a source of
  electrical power, or wired, or otherwise fitted for electrification."
- Sec. 22: "Potable water shall be available to the dwelling site."
- Sec. 27: use of the amendment "would be considered a factor against a
  rezoning to a higher density"; change to commercial use requires a
  registered design professional's certification of full code compliance.
- Sec. 4(B): near a military airport the owner-builder "is required to
  provide high noise sound attenuation … as defined and required by ARS §
  28-8482B."

**Coconino County — Alternative Methods and Materials Permit Program
(AMMP).** `[V]` (county page, read by research subagent, September 2026):
"allows rural owner-builders of small innovative dwellings the option of
seeking an exemption from some aspects of currently adopted building codes.
Projects participating in this program will not be required to apply for a
traditional building permit or undergo plan review or building inspections."
Qualifications on the county page: AR or G zoning, parcel ≥ 2 acres, ≤ 600 sq
ft interior, one story, alternative method used, owner-occupied and not
rented or sold for one year, signed affidavits of electrical/mechanical/
fire/plumbing compliance at completion, and a **recorded Notice of Disclosure
Statement**. No CO. The 600 sq ft cap makes it a cabin program, not a house
program; the kit mentions it in AZ.4 only.

### 1.6 The county with no building code at all — Greenlee `[V]`

Greenlee County's own Planning & Zoning page links a County Engineer letter
(dated 19 October 2012, still posted September 2026, read by research
subagent): "Currently, Greenlee County has adopted no building codes. Because
we have no codes, Greenlee County has not determined and does not recommend
building loads, does not review plans, does not inspect construction, or
issue a Certificate of Occupancy. I suggest that owners contract for
inspections and use a conservative Building Code. **With some exceptions,
Arizona Law requires the County to issue a building permit. We issue a
building permit at no cost when a Zoning Use Permit and Floodplain Permit are
issued.**"

That last sentence is § 11-321(A) in practice. The kit's framing: *no code
county ≠ no permit county*.

### 1.7 Fire — the one state code, and it barely reaches a house `[V]`

**§ 37-1383(A)(2)**: the State Fire Marshal adopts by rule "a state fire code
establishing minimum standards." (A)(2)(e) covers exits and fire protection
"in places in which numbers of persons work, live or congregate, **excluding
family dwellings that have fewer than five residential dwelling units**."
(A)(5): the marshal enforces the code "throughout this state except in any
city with a population of one hundred thousand persons or more that has in
effect a nationally recognized fire code … and that has enacted an ordinance
to assume such jurisdiction." (A)(8): the marshal inspects "all other
occupancies … except family dwellings having fewer than five residential
dwelling units."

**§ 11-861(B)**: a county may adopt a fire prevention code in unincorporated
areas "in which a fire district has not adopted a nationally recognized fire
code pursuant to section 48-805," and (C)(2) it must be "as stringent as the
state fire code adopted pursuant to section 37-1383."

Kit statement: the state fire code exists but is written around
non-residential occupancies; for a house the live fire rules are the **fire
district's** adopted code (or the county's, where no district has one) plus
the residential code's smoke-alarm provisions. The published guide's line
that fire is "the main statewide exception" overstates it.

### 1.8 The regulatory bill of rights runs against the permit counter `[V]`

Title 9, Ch. 7, Art. 4 (cities) and Title 11, Ch. 11, Art. 1 (counties) —
detail in § 4. The headline: **§ 9-834(A)** "A municipality shall not base a
licensing decision in whole or in part on a licensing requirement or
condition that is not specifically authorized by statute, rule, ordinance or
code." **§ 11-1604(A)** is the county twin. (H) in both: the municipality or
county "shall prominently print the provisions of subsections A, B, C, D, E,
F and G of this section on all license applications." "License" includes a
permit (§ 9-831(3); § 11-1601(4)). So every Arizona building permit
application must carry this text.

---

## 2. SCOPE — WHAT IS OUTSIDE THE CODE

### 2.1 Statutory exemptions from the county code article `[V]`

**§ 11-865(A)**: "This article does not apply to: 1. Construction or
operation incidental to construction and repair to irrigation and drainage
ditches or appurtenances thereto, of regularly constituted districts or
reclamation districts, or to **farming, dairying, agriculture, viticulture,
horticulture or stock or poultry raising**, or clearing or other work on land
in rural areas for fire prevention purposes. 2. Devices used in
manufacturing … and construction, operation and maintenance of electric, gas
or other public utility systems…"

**§ 11-865(C)**: an owner of property classified agricultural under
§ 42-12002(1)(a), (b) or (d) who "desires to change the agricultural use of
all or part of the property … shall not implement a change endangering
public health or safety."

`[H]` The statute exempts construction *incidental to* farming. Nothing in it
says a dwelling is incidental to farming, and the kit does not print an
"agricultural exemption" route for a house. It prints the paragraph so the
reader knows why the barn and the house are treated differently and tells the
reader to get the county's position in writing under § 11-1609 (§ 4).

**Dollar floors** `[V]`: county building permit only for construction
"exceeding a cost of $1,000" (§ 11-321(A)); zoning permit not required "for
repairs or improvements of a value not exceeding five hundred dollars"
(§ 11-815(B)). Neither floor reaches a house.

**Rural/unclassified zones** `[V]`: § 11-861(A), § 1.2 above.

### 2.2 Statewide rules that bind regardless of local code `[V]`

Everything in this table is state statute and applies on every lot in Arizona,
including in Greenlee County and under the Cochise Option 2 permit.

| Subject | Rule | Cite |
|---|---|---|
| **Septic** | "Sewage treatment facilities, including on-site wastewater treatment facilities" are discharging facilities that "shall be operated pursuant to either an individual permit or a general permit" — the Aquifer Protection Permit | § 49-241(A), (B)(9) |
| Septic — delegation | ADEQ "may delegate to a local environmental agency, county health department, public health services district or municipality any functions, powers or duties"; general-permit rules "may require a person … to notify the director of the person's intent to operate the facility pursuant to the general permit, apply for coverage … and pay the applicable fee" | § 49-107(A); § 49-245(D) |
| **Wells** | Notice of intention to drill before drilling any well; licensed driller; domestic well site plan on parcels ≤ 5 acres — § 6 | §§ 45-454(G), 45-595(A), 45-596(A), (F) |
| **Pool barrier** | Any pool "eighteen inches or more in depth … wider than eight feet … intended for swimming" needs a barrier at least **5 ft** high; no opening a **4-inch** sphere passes; self-closing, self-latching gates with the latch **≥ 54 in** above grade (or on the pool side ≥ 5 in below the top with no opening > ½ in within 24 in), opening outward; barrier **≥ 20 in** from the water's edge; no exterior handholds | § 36-1681(A), (B) |
| Pool — house as barrier | Alternatives when the residence forms part of the enclosure: a 4-ft interior barrier; a keyed motorized safety cover; or self-latching doors plus sleeping-room escape windows latched ≥ 54 in above floor and other windows screened, keyed to 4 in, or latched ≥ 54 in | § 36-1681(C) |
| Pool — exceptions | Political subdivisions with an ordinance equal to or more stringent; "A residence in which all residents are at least six years of age" | § 36-1681(D)(5)–(7) |
| Pool — notice | Anyone entering "an agreement to build a swimming pool" must give the buyer a DHS-approved safety notice | § 36-1681(E) |
| **Plumbing fixtures** | Since 1 Jan 1994 no person may "install any plumbing fixture … in any new residential construction" unless: lavatory and kitchen faucets ≤ 3 gpm at 80 psi; showerheads ≤ 3 gpm; water closets ≤ 1.6 gal/flush; urinals ≤ 1 gal/flush; evaporative coolers and decorative fountains with recycling systems | § 45-312 |
| Fixture labels | Where a building or plumbing permit is required, compliance labels "shall not be removed from the fixtures … until the fixtures have been installed and inspected" | § 45-314(B) |
| **Sprinklers cannot be mandated** | A municipality/county "shall not adopt a code or ordinance … that prohibits a person or entity from choosing to install or equip or not install or equip fire sprinklers in a single family detached residence or any residential building that contains not more than two dwelling units"; exception only for ordinances "adopted before December 31, 2009"; the text must appear on every residential sprinkler permit application | § 9-807; § 11-861(E) |
| Access roads cannot back-door sprinklers | No fire-code access-road or approved-route requirement "that directly or indirectly requires a one or two family residence or a utility or miscellaneous accessory building or structure to install fire sprinklers"; enforceable by private civil action with attorney fees, damages "and the cost of the sprinkler system" | § 9-808(A), (D); § 11-861(G) |
| **Utility choice** | A permit "may not [be denied] based on the utility provider proposed"; fees may not be structured to restrict the choice; "utility service" means "water, wastewater, natural gas, including propane gas, or electric service" | § 9-467(B)–(D), (I)(2); § 11-321(B)–(D), (K); § 9-810 |
| No business license as a permit condition | A city or county "may not require an applicant for a building permit to hold a transaction privilege tax license or business license as a condition for issuing the building permit" | § 9-467(E); § 11-321(E) |
| Prior owner's unpermitted work | A subsequent owner cannot be made to permit "the construction or addition done by the prior owner before issuing a permit for a building addition," except to enforce a provision "that affects the public health or safety" | § 9-467(F); § 11-321(H) |
| Permit copies | Every building permit copy goes to the county assessor and the Department of Revenue with parcel number; both are told again at CO, completion, expiration or cancellation | § 9-467(A); § 11-321(G) |
| **Solar permits** | Plans must show location, mounting details, one- or three-line diagram (or an automated platform), inverter cut sheets; "shall not require a stamp from a professional engineer … unless an engineering stamp is deemed necessary" and then only with "a written explanation"; fee "shall not exceed the actual cost of issuing a permit," itemized on request | § 9-468; § 11-323 |
| Solar covenants void | Any deed or CC&R provision that "effectively prohibits the installation or use of a solar energy device … is void and unenforceable" (instruments before 17 April 1980 excepted) | § 33-439 |
| Solar-ready piping | A county code "may contain a provision requiring new single family residences … to be designed to facilitate the future installation of solar water heating equipment" — i.e., accessible piping; optional, not mandatory | § 11-861.01 |
| Refrigerants | No local code "may prohibit the use of refrigerants that are listed as acceptable pursuant to the clean air act" | § 9-810.01; § 11-861(J) |
| **Military airport noise** | In "territory in the vicinity of a military airport or ancillary military facility" the political subdivision must require, for residential buildings outside the noise contours, "a minimum of **R18 exterior wall assembly**, a minimum of **R30 roof and ceiling assembly**, dual-glazed windows and solid wood, foam-filled fiberglass or metal doors," or an architect's/engineer's certification of a **45 dB** maximum interior level | § 28-8482(B) |
| Wildland-urban interface | A city or county "**may** adopt a current wildland-urban interface code" — optional, with a required public process | § 9-806; § 11-861(D) |

### 2.3 What is NOT statewide — verified negatives `[V]`

| Claim | Status | Basis |
|---|---|---|
| Statewide residential building code | **None.** | Title 9 Art. 1 and Title 11 Art. 3 authorize only local adoption by reference; no state agency is given a residential code |
| Statewide residential **energy** code | **None.** | § 34-451 directs the governor's energy office to adopt energy standards only "for construction of all new capital projects as defined in section 41-790, including buildings designed and constructed by school districts, community college districts and universities" — public buildings |
| Statewide NEC edition | **None.** | § 3.4 |
| Statewide setbacks | **None.** | Zoning is county (Title 11, Ch. 6, Art. 1) and municipal (§ 9-462.01) |
| Statewide inspection list | **None.** | § 11-863(B) requires only that inspections be "made at the earliest reasonable time" |
| Statewide permit fee schedule | **None.** | § 11-863(C) "reasonable fees"; § 9-467(G)/§ 11-321(I) "reasonable costs" |
| Statewide owner-builder affidavit form | **No form — but the content is statutory.** | § 32-1169(A) requires a signed exemption statement on every permit application naming the basis of the exemption and every licensed sub (§ 5.11); each AHJ prints its own form (§ 3.6). See § 10 item 1. |

---

## 3. CODE EDITIONS AND AMENDMENTS

No edition is statewide. The maps below were read from each jurisdiction's own
website, adopting ordinance or code host by two research subagents on
3 September 2026; every row is marked `[V]` on that basis and carries the URL
the subagent read. Rows the subagents could not close on a primary source are
marked NOT VERIFIED and must not be printed as fact. **The kit prints the map
with the retrieval date and the instruction to confirm the adopting ordinance
number with the clerk (§ 1.1).**

### 3.1 Counties — unincorporated areas `[V]`

| County | IRC | NEC | Energy | Adopting instrument, effective | Opt-out / exemption | Septic permit issuer |
|---|---|---|---|---|---|---|
| Maricopa | 2018 | 2017 | 2018 IECC **voluntary** ("Compliance with Chapter 11 Energy Efficiency or the International Energy Conservation Code is optional unless specifically required through ordinance by Maricopa County") | Local Additions & Addenda TA2022001; BOS 17 Aug 2022, effective 30 days later | None | Environmental Services Dept. |
| Pima | 2024 | 2023 | IECC per Ord. 2018-30 Ex. G, with a 2024 IECC amendment set (Ord. 2026-6) posted; effective date of 2026-6 NOT VERIFIED | Ord. 2025-15, effective 1 Jan 2026 | None found | Development Services (On-Site Wastewater) |
| Pinal | 2018 | 2017 | 2018 IECC | Ord. 121819-BCO (hearing 18 Dec 2019); PCDSC 6.05.030 | None | Aquifer Protection Division ("delegated by ADEQ") |
| Yavapai | 2024 (2018 before 1 Jan 2026) | 2023 | **2012 IECC** retained (Ord. 2025-13) | Ords. 2025-3 to 2025-13, Oct 2025, effective 1 Jan 2026 | None | Environmental Services Unit of Development Services |
| Mohave | 2018 | 2017 | 2018 via IRC Ch. 11 ("The Residential Provisions of the IECC are not adopted") | Ord. 2021-03, adopted 7 Jun 2021, effective 30 days after; revised to 15 Jul 2024 | None now; pre-2007 "building overlay" amnesty only | Development Services, Environmental Quality/Waste Disposal ("delegated … by ADEQ") |
| Cochise | **2024 from 1 Sep 2026** (2015 before) | 2023 (2014 before) | **2012 IECC** continued | Resolution 26-23 (July 2026); replaced Res. 21-15 (eff. 26 Aug 2021) | Owner-Builder Amendment (§ 1.5) | NOT VERIFIED on county pages |
| Coconino | 2024 (2018 accepted through 31 Dec 2026) | 2023 | 2018 IECC (not 2024) | Ordinance 2026-03, effective 2 Jun 2026 | AMMP (§ 1.5) | Community Development, Environmental Quality Division |
| Navajo | 2018 | 2017 (by reference in addenda) | None listed | Resolution 9-2022, adopted 22 Mar 2022, effective 22 Jun 2022 | None | Planning & Development Services (Environmental Health "does not inspect new septic systems") |
| Apache | 2015 (county FAQ; site Cloudflare-walled, read from an archived copy of the county's own PDF, March 2025) | 2011 | NOT VERIFIED | NOT VERIFIED | None; "not if you are an owner-builder and only hire employees" | County Health Department |
| Gila | 2012 | 2011 | County R-value table in ordinance § 103; "Chapter 11 Energy Efficiency … is optional and not required" | Ord. 2017-02, passed 11 Jul 2017, effective 30 days after | None | Community Development (Wastewater) |
| Graham | **2003** | 2002 (§ 5.14.2) / 1999 (§ 5.14.9) — internal inconsistency in the county's own ordinance | 2003 IECC "for Graham County Government Buildings only" | P&Z Ordinance § 5.14; date NOT VERIFIED | None ("'dirt work' does not require a permit, everything else does") | Health Department |
| **Greenlee** | **NONE ADOPTED** | none | none | County Engineer letter 19 Oct 2012, still posted | Whole county: no plan review, no inspections, no CO; permit issued at no cost with zoning-use and floodplain permits | Health Department |
| La Paz | 2018 | **2020** | Not in adopted list | Ord. 2026-01, adopted 6 Jul 2026, effective 6 Aug 2026 | None; "Owner's Acknowledgment & Verification of Information" form | Community Development |
| Santa Cruz | 2012 (site Cloudflare-walled; archived copy of county page May 2026) | 2011 | None listed | Ord. 2013-03, passed 17 Jul 2013, effective 1 Sep 2013 | None; "Owner Builder Form" | Environmental Health (conventional systems only; others direct to ADEQ) |
| Yuma | 2024 (adopts the City of Yuma's code under § 11-861(C)(1)) | 2020 amendments posted; 2023 NOT VERIFIED | 2009 IECC amendments posted | Ord. 2026-01, approved 19 Feb 2026, effective 23 Mar 2026 | None | Development Services, Environmental Programs |

**Spread: 2003 IRC (Graham) to 2024 IRC (Pima, Yavapai, Coconino, Yuma,
Cochise).** Five counties have no residential energy code at all or make it
optional (Maricopa, Gila, Graham, Navajo, Santa Cruz, La Paz, Greenlee).

### 3.2 Cities and towns `[V]`

| City | IRC | NEC | Energy | Adopting instrument, effective | Owner-builder statement on the city's own site |
|---|---|---|---|---|---|
| Phoenix | 2024 Phoenix Building Construction Code (2024 IRC with App. BA, BB, BF, BG, BI, BJ, BO, CA, CB, CD, CE, CF, NB, NE) | 2023 — **enforcement of 210.8(F) Exception 2 (HVAC GFCI) deferred to 1 Mar 2027** | 2024 IECC | Ord. G-7397; Council 18 Jun 2025; effective 1 Aug 2025; 2018 PBCC allowed for complete plans through 31 Dec 2025 | None found beyond a DIY permit list |
| Tucson | 2024 (eff. 1 Jan 2026) | 2023 (eff. 1 Jan 2026) | 2024 IECC (eff. **1 Jul 2026**) | Amendments under Ord. 12171; M&C 3 Jun 2025 and 16 Dec 2025 | **Owner/Builder Affidavit** required; "Rental units are considered commercial property and all commercial permits require a licensed contractor" |
| Mesa | 2024 (App. BB, BF, NE) | 2023 | 2024 IECC + App. RE | Ords. 5981/5982/5987, passed 8 Dec 2025, effective 30 days after (8 Jan 2026); city page unreachable, read from the ordinances | NOT VERIFIED |
| Scottsdale | **2021** | 2020 | 2021 IECC + 2021 IgCC mandatory | Ord. 4550 (20 Sep 2022, eff. 1 Jan / 7 Jan 2023); Ord. 4576 (IECC) | "Owner-Builder Declaration form" required by the Tax Audit Division |
| Chandler | 2024 | 2023 | 2024 IECC | Ord. 5108; plans on/after 1 Jul 2025 | Owner-applicant may perform work; "If you own a home that you lease or rent to others, a licensed contractor is required" |
| Gilbert | 2018 (App. H, P, Q) | 2017 | 2018 IECC | Ord. 2739; Ord. 2788 (IRC amendments) | None for SFR |
| Glendale | 2024 (App. BB, BC, BF, BO, CF) | 2023 | 2024 IECC | Ord. O25-51, passed 9 Dec 2025, effective 9 Jan 2026 | "Residential property owners doing their own work will be required to sign verification" |
| Tempe | 2024 (eff. 1 Jul 2026; 2018 allowed through 31 Dec 2026) | 2023 (2017 allowed through 31 Dec 2026) | 2024 IECC | 2024 ordinance number NOT VERIFIED | NOT VERIFIED |
| Peoria | 2018 | 2017 | 2018 IECC | Ord. 2019-12 (city PDF title); date NOT VERIFIED | "Owner/Builder Affidavit (PDF)" listed |
| Flagstaff | 2018 | 2017 | 2018 IECC | Res. 2019-26 / Ord. 2019-16, adopted 18 Jun 2019, effective 19 Jul 2019; "2024 Codes … being evaluated" | Owner Authorization form |
| Prescott | 2024 (App. BF) | 2023 | **2012 IECC** ("with 2018 Revisions"); IRC Ch. 11 deleted and replaced | Ord. 2025-1924 / Res. 2025-1958 (IRC), Ord. 2025-1923 (NEC), 18 Nov 2025; IECC Ord. 2019-1669 | NOT VERIFIED |
| Yuma | 2024 | 2020 | 2009 IECC amendments (Ord. O2013-15) | Effective 3 Nov 2025; 2024 mandatory from 1 Feb 2026; ordinance number NOT VERIFIED | NOT VERIFIED |
| Sierra Vista | 2018 | 2017 | **2006 IECC** residential; 2012 commercial | Resolution 2023-043 (amendments); ordinance NOT VERIFIED | Separate "Owner App" forms for electrical, plumbing, additions |
| Lake Havasu City | 2024 | 2023 | None listed among adopted codes (negative NOT VERIFIED) | Ord. 25-1370; effective 1 Feb 2026 | Notarized Owner/Builder Certification citing § 32-1121(A)(5) |
| Kingman | 2018 | 2017 | 2018 IECC with residential provisions R101.1–R406.6.5 **not adopted**; IRC Ch. 11 amended | Ord. 1916 § 4, 15 Dec 2020 | Weak |
| Surprise | 2024 | 2023 | 2024 IECC | Ord. 2025-14, passed 2 Dec 2025; amendments dated 1 Jan 2026 | NOT VERIFIED |
| Goodyear | 2024 | 2023 | 2024 IECC | Council 23 Mar 2026; building codes effective 23 Jun 2026 | "If you own the house and live in it, you do not need to hire Licensed Contractors … If you own the house and rent it out, Licensed Contractors are required" |
| Buckeye | 2024 | 2023 | **2018 IECC** | Effective for projects submitted on/after 1 Jan 2025; Ord. 20-24 NOT directly read | "Owner Builder Form" listed |
| Queen Creek | 2021 | 2020 | 2021 IECC | Ord. 797-22; effective 1 Jan 2023 | NOT VERIFIED |
| Casa Grande | 2018 | 2017 | 2018 IECC | 2019 Building & Technical Administrative Code, effective 1 Jul 2019 | FAQ: owner "may act as your own contractor" and signs the § 32-1121 affirmation |

### 3.3 Transition rules are local `[V]`

There is no state transition rule. Each adopting ordinance sets its own:
Phoenix honoured 2018 plans "submitted through December 31, 2025"; Tempe
accepts either set "through December 31, 2026"; Coconino County accepts 2018
plans "through 12/31/26"; Lake Havasu City accepted 2018-designed projects
"up to 90 days (May 1, 2026) after the effective date." AZ.2 tells the reader
to get the grace-period sentence from the ordinance in writing before
choosing an edition to design to.

### 3.4 ⚠ ELECTRICAL — the Arizona trap `[V]`

**Arizona adopts no edition of NFPA 70 statewide, has no state electrical
inspector, and licenses no individual electricians.** What governs is the
NEC edition in the local adopting ordinance — and the map runs from the
**1999/2002 NEC in Graham County** through 2011 (Apache, Gila, Santa Cruz),
2014 (Cochise until 1 Sep 2026), 2017 (Maricopa, Pinal, Mohave, Navajo,
Gilbert, Peoria, Flagstaff, Sierra Vista, Kingman, Casa Grande), 2020
(Scottsdale, Queen Creek, Yuma city and county, La Paz) to 2023 (Phoenix,
Tucson, Mesa, Chandler, Glendale, Tempe, Prescott, Surprise, Goodyear,
Buckeye, Lake Havasu City, Pima, Yavapai, Coconino, Cochise from 1 Sep 2026).

Three consequences the kit prints:

1. **Never print an NEC year as an Arizona citation.** The kit cites "the NEC
   edition in your adopting ordinance" and prints the map with a date.
2. **Phoenix's HVAC-GFCI deferral is real and dated**: "the city of Phoenix is
   deferring enforcement at this time. Full enforcement of the GFCI
   requirement for HVAC equipment will now take effect on March 1st, 2027."
   Tripwire, § 9.
3. **Where no county code exists, nobody inspects the wiring before the
   utility connects it.** Greenlee's engineer: "does not inspect
   construction." Coconino's AMMP page says the program yields no utility
   "green tag." `[H]` What the serving utility (APS, SRP, TEP, UniSource, a
   co-op) requires before setting a meter is set in the utility's own service
   requirements manual and was not fetched here; AZ.3 tells the reader to ask
   the utility, in writing, what clearance it needs, before framing.

The Cochise amendment's electrical section is worth quoting for the
"off-grid" reader: "No dwelling or accessory structure constructed pursuant
to this amendment shall be required to be connected to a source of electrical
power, or wired, or otherwise fitted for electrification."

### 3.5 Energy — no state code, and the local picture is chaotic `[V]`

§ 34-451 reaches only public capital projects (§ 2.3). Locally:

- **2024 IECC**: Phoenix, Tucson (from 1 Jul 2026), Mesa, Chandler, Glendale,
  Tempe, Surprise, Goodyear.
- **2021 IECC**: Scottsdale, Queen Creek.
- **2018 IECC**: Gilbert, Peoria, Flagstaff, Kingman (with the residential
  provisions struck), Casa Grande, Buckeye (paired with the 2024 IRC), Pinal,
  Coconino, Mohave (via IRC Ch. 11).
- **2012 IECC**: Prescott, Yavapai County, Cochise County.
- **2009 IECC**: Yuma city and county.
- **2006 IECC**: Sierra Vista (residential).
- **Voluntary or a county table**: Maricopa County (optional unless required
  by ordinance), Gila County (ordinance § 103 minimums: R-13 walls at 2×4,
  R-19 at 2×6, R-38 ceilings with attic, R-19 floors, U-0.35 windows).
- **None**: Navajo, Santa Cruz, La Paz, Greenlee; Lake Havasu City lists none.

**Do not print R-values or a climate-zone map as Arizona requirements.** The
published guide's "typical Zone 2B" table is unsourced (§ 12). The one
statewide envelope number that exists is the military-airport rule, R-18
walls / R-30 roof (§ 2.2), and it is a noise rule, not an energy rule.

### 3.6 Owner-builder forms the jurisdictions themselves name `[V]`

No statewide form exists. Jurisdiction sites name: Tucson "Owner/Builder
Affidavit"; Scottsdale "Owner-Builder Declaration form" (Tax Audit Division);
Peoria "Owner/Builder Affidavit"; Lake Havasu City "Owner/Builder
Certification" (notarized, recites the one-year no-sale rule); Buckeye "Owner
Builder Form"; Glendale a signed "verification"; Casa Grande a signed
affirmation reciting § 32-1121(A)(5); Sierra Vista separate "Owner App" forms
per trade; La Paz County "Owner's Acknowledgment & Verification of
Information"; Mohave County a checkbox and exemption block on the permit
application; Gila County "signed Owner Builder Statement"; Santa Cruz County
"Owner Builder Form"; Maricopa County requires "Written documentation of an
Arizona licensed contractor or owner-builder classification … for all
building permits." **Chandler, Tucson and Goodyear each say on their own
sites that a rental requires a licensed contractor** — that is § 32-1121(A)(5)
"not intended … for rent," applied at the counter.

---

## 4. PERMITS, CLOCKS AND INSPECTIONS

Arizona's permit clocks live in the "regulatory bill of rights" articles —
**Title 9, Ch. 7, Art. 4 (§§ 9-831 to 9-843) for cities** and **Title 11,
Ch. 11, Art. 1 (§§ 11-1601 to 11-1613) for counties** — plus the 2024-era
**§ 9-470.01** third-party review statute. "License" includes "the whole or
part of any municipal permit, certificate, approval, registration, charter or
similar form of permission required by law" (§ 9-831(3); § 11-1601(4)).

### 4.1 ⚠ The city/county asymmetry — strongest original finding `[V]`

**§ 11-1605(M)**, verbatim: "This section does not apply to a license that is
either: 1. Issued within seven working days after receipt of the initial
application or a permit that expires within twenty-one working days after
issuance. **2. Necessary for the construction or development of a
residential lot, including swimming pools, hardscape and property walls,
subdivisions or master planned community.**"

**§ 9-835(O)** (cities) exempts only the seven-day / twenty-one-day permits.

**Result: every statutory review clock, one-request-for-corrections rule,
fee refund and mid-construction-change bar in § 9-835 applies to a CITY
house permit and NONE of the § 11-1605 equivalents apply to a COUNTY house
permit.** In unincorporated Arizona the only statutory clock on a residential
building permit is § 11-863(B), inspections "at the earliest reasonable
time." The published guide's timeline table has this exactly backwards
(counties faster). The kit prints the asymmetry as the reason to (a) prefer a
city lot if speed matters, or (b) ask a county in writing under § 11-1609
what its posted time frame is, knowing it is not enforceable by refund.

What still applies in a county: §§ 11-1604 (no unauthorized conditions,
printed on every application), 11-1606 (list of steps and contact at
application), 11-1609 (written clarification within 30 days).

### 4.2 The city clock — § 9-835 `[V]`

| Rule | Text | Cite |
|---|---|---|
| Posted time frames | A municipality "shall have in place an overall time frame during which the municipality will either grant or deny each type of license," stating separately "the administrative completeness review time frame and the substantive review time frame," posted on its website | § 9-835(A), (B) |
| Completeness notice | Written or electronic notice of administrative completeness or deficiencies within the completeness time frame; if none issues, "the application is deemed administratively complete" | § 9-835(D), (F) |
| Deficiency list | "a comprehensive list of the specific deficiencies"; clock suspended until the missing information arrives; withdrawal possible after 15 days or more | § 9-835(E), (F) |
| **One request for corrections** | "During the substantive review time frame, a municipality may make one comprehensive written or electronic request for corrections," amendable once to add missed legal requirements "and the legal authority for the requirements"; supplemental requests "limited to issues previously identified" | § 9-835(G) |
| Meeting | "Within ten working days after a request by the applicant, the municipality shall meet or discuss with the applicant the request for corrections" | § 9-835(G) |
| **Residential no-denial rule** | "a municipality may not deny a residential license application that is necessary for land development or building construction unless the municipality considers the application withdrawn or the municipality has notified the applicant and the property owner within fifteen working days after the submission of the application that the application may be subject to denial because of excessive substantive deficiencies" | § 9-835(G) |
| Extension | By mutual written agreement, not more than 50% of the overall time frame | § 9-835(I) |
| Denial contents | Justification with statute/ordinance/code references; appeal rights with the number of working days to protest; resubmittal fee amount and method | § 9-835(J) |
| **Automatic refund** | If a municipality "makes more than one comprehensive … request for corrections and one supplemental … request … to a license application necessary for residential building construction … or does not issue … within the overall time frame," it "shall refund to the applicant all fees charged for reviewing and acting on the application … The municipality shall not require an applicant to submit an application for a refund … within thirty working days … may not be waived by an applicant" | § 9-835(K) |
| Resubmittal fees | After denial, no fee beyond "the cost of processing the resubmitted revisions or corrections"; after withdrawal, not more than 50% of the original unrefunded fee | § 9-835(L), (M) |
| **No mid-build changes** | A municipality "may not modify, rescind or request any subsequent modifications or revisions to an approved plan or permit for residential land development or residential building construction during construction if the construction is done in accordance with the approved plan or permit" unless: a field condition unknown at review; the applicant's own request; or correction of a code noncompliance the municipality had not already ruled on | § 9-835(N) |
| Waiver | "A municipality shall not request or initiate discussions with a person about waiving that person's rights" | § 9-834(D) |
| Enforcement | Private civil action; court "may award reasonable attorney fees, damages and all fees associated with the license application" | § 9-834(E) |

### 4.3 § 9-470.01 — third-party review, cities ≥ 30,000 `[V]`

"If a municipality with a population of thirty thousand persons or more does
not approve, conditionally approve or respond with required additions or
revisions to an application for a single-family residential building permit
**within fifteen working days after the date the application is submitted**,
any required review of the application may be performed by a qualified third
party selected by the municipality … A municipality shall maintain a list of
at least three third-party reviewers."

The catch, verbatim: "The time frame prescribed by this subsection does not
begin until the applicant has satisfied the following requirements: 1. The
municipality has approved construction documents for the dwelling to be
constructed. 2. The municipality has approved vertical construction
activities to begin in the subdivision … or, if the dwelling is not to be
constructed in a subdivision, on the individual lot."

`[H]` Reading (A)(1) with the definition in (I) ("a plan, permit or other
document that is related to building construction"), the fifteen-day clock
for a one-off custom house attaches to the steps *after* the construction
documents are approved — permit issuance — not to the plan review itself.
The kit prints the section and says so rather than promising a 15-day plan
review. Other terms `[V]`: the municipality "may not request or require an
applicant to waive a deadline" (C); the applicant may appeal any decision
(D); the applicant pays the third-party fees to the municipality (F); it
does not apply to hillside ordinances or federal floodplain reviews (G); the
building official's power to withhold a CO is untouched (H).

### 4.4 What you must be handed at the counter `[V]`

**§ 9-836(A) / § 11-1606** — at the time the applicant obtains an
application: "1. A list of all of the steps the applicant is required to
take in order to obtain the license. 2. The applicable licensing time frames.
3. The name and telephone number of a [municipal/county] contact person …
4. The website address … 5. Notice that an applicant may receive a
clarification … as provided in section 9-839 [11-1609]."

**§ 9-839 / § 11-1609 — the clarification letter.** A written request stating
the applicant's name and address, the provision needing clarification, the
relevant facts, "the applicant's proposed interpretation," and whether the
issue is pending on any existing application. The municipality "shall respond
**within thirty days** of the receipt of the written request with a written
explanation of its interpretation or application." This is the kit's
universal tool for every "varies locally" question: AZ.5 includes a template.

### 4.5 Inspections `[V]`

- **No statewide list.** § 11-863(B): county inspection rules "shall require
  that such inspections be made at the earliest reasonable time." Nothing in
  Title 9 or 11 names an inspection.
- **Inspection-rights statute does not cover the inspections you schedule.**
  § 9-833 (photo ID, statement of purpose and authority, report copy within
  30 working days) — but § 9-833(N)(2): "Does not apply to a municipal
  inspection that is requested and scheduled by the regulated person."
  Routine building inspections are requested and scheduled by the permittee.
  The kit does not cite § 9-833 as an inspection right.
- **Local sequences read from county sites** (subagent, `[V]` as to what the
  county says): Graham County lists setback, footing, framing, rough
  electrical/mechanical/plumbing, drywall, final. Cochise Option 1 requires
  only mechanical, electrical, plumbing and fire-prevention inspections;
  Cochise inspections are requested "at least twenty-four (24) hours in
  advance." Everything else is in the adopted IRC R109 as amended locally.
- **Alternative materials and interpretations**: in a county, the § 11-862
  advisory board; in a city, whatever the adopting ordinance creates.
  § 9-835(J)(2) requires every denial to state the appeal route and its
  deadline.

### 4.6 Certificate of occupancy `[V]`

No statute requires a CO for a single-family dwelling; the requirement is in
the locally adopted IRC R110 as amended. State law mentions the CO only as a
reporting event (§ 9-467(A), § 11-321(G)) and as the start of the one-year
no-sale clock (§ 32-1121(A)(5)). Greenlee County issues none; Cochise Option 2
yields none and Option 1 a "conditioned" one; Coconino AMMP yields none. The
kit warns that a lender or buyer will ask for it and that in those programs
it cannot be obtained later.

### 4.7 Permit life and fees `[V]`

Local. The only verified figure is Cochise's 36 months plus one 12-month
extension. Fees: "reasonable" (§ 11-863(C)); "reasonable costs associated
with reviewing and issuing" (§ 9-467(G), § 11-321(I)); solar fees capped at
actual cost with an itemized list on request (§ 9-468(B), § 11-323(B)).
Greenlee: "a building permit at no cost." **No dollar figure is printed.**

---

## 5. LICENSING AND CONTRACTS

### 5.1 The exemption — A.R.S. § 32-1121(A)(5), verbatim `[V]`

> "Owners of property who improve such property or who build or improve
> structures or appurtenances on such property and who do the work
> **themselves, with their own employees or with duly licensed contractors**,
> if the structure, group of structures or appurtenances, including the
> improvements thereto, are intended for occupancy **solely by the owner** and
> are not intended for occupancy by members of the public as the owner's
> employees or business visitors and the structures or appurtenances are
> **not intended for sale or for rent**. In all actions brought under this
> chapter, **except an action against an owner-occupant as defined in section
> 33-1002**, proof of the sale or rent **or the offering for sale or rent** of
> any such structure by the owner-builder within one year after completion or
> issuance of a certificate of occupancy is **prima facie evidence** that such
> a project was undertaken for the purpose of sale or rent. For the purposes
> of this paragraph, 'sale' or 'rent' includes any arrangement by which the
> owner receives compensation in **money, provisions, chattels or labor** from
> the occupancy or the transfer of the property or the structures on the
> property."

> **Two versions on azleg.gov.** The Title 32 table of contents lists both
> "32-1121" (`/ars/32/01121.htm`, tagged L19 Ch. 140 § 1, with paragraph 18
> for cable/telecom installers) and "32-1121; Version 2"
> (`/ars/32/01121.01.htm`, tagged L19 Ch. 145 § 5, with subsection E on joint
> ventures and reformatted paragraphs 4, 9 and 14). Two 2019 session laws
> amended the section and Legislative Council publishes both. **Paragraphs
> (A)(5), (A)(6) and (A)(11) are word-for-word identical in both**, so the
> kit's citations are safe whichever text a court applies. Say "A.R.S.
> § 32-1121(A)(5)" and nothing about versions in the kit. `[V]`

### 5.2 The one-year rule's real test `[V]`

Five things the statute actually says, against what circulates:

1. **Trigger is "sale or rent or the offering for sale or rent."** Listing
   the house, or advertising it for rent, inside the year is enough.
2. **Clock starts at "completion or issuance of a certificate of occupancy."**
   Where no CO issues (Greenlee, Cochise Option 2, Coconino AMMP) the only
   start date is "completion," which is a fact question the owner should
   document.
3. **It is "prima facie evidence," i.e., rebuttable.** It is not a bar on
   selling. The published guide gets this right; most summaries do not.
4. **It is switched off "in an action against an owner-occupant as defined in
   section 33-1002."** § 33-1002(A)(2): an "owner-occupant" is a natural person
   who "(a) Prior to commencement of the construction … holds legal or
   equitable title to the dwelling by a deed or contract for the conveyance of
   real property **recorded with the county recorder** … and (b) Resides or
   intends to reside in the dwelling **at least thirty days during the
   twelve-month period immediately following completion** … and does not
   intend to sell or lease the dwelling to others." Evidence may be "The
   placing of his or her personal belongings and furniture in the dwelling"
   and "Occupancy either by the person or members of his or her family."
   **Kit instruction: record the deed before the first shovel, and move in.**
5. **"Rent" includes "labor."** Letting a helper live in the house in
   exchange for work is compensation "from the occupancy," which the
   statute calls rent. This is the Arizona version of the trap every state
   hides somewhere; the kit prints it in AZ.1.

There is **no** "once per 24 months" rule, "once per five years" rule, or
"must live in it two years" rule in the statute. The five-year figure is
Cochise County's local limit on its opt-out permit (§ 1.5); the 24-month
figure appears on at least one municipal FAQ and has no statutory source.

### 5.3 Who may help you — three lawful categories and one crime `[V]`

The paragraph allows the owner to do the work "themselves, with their own
employees or with duly licensed contractors." The chapter fills in the edges:

- **Your employees** — § 32-1121(A)(11): the chapter does not apply to "Any
  person who engages in the activities regulated by this chapter, as an
  employee of an exempt property owner or as an employee with wages as the
  person's sole compensation." A helper paid wages is lawful. A helper paid
  by the job, by a share, or in kind is not an employee.
- **Licensed contractors** — verify at the ROC (§ 11). § 32-1132(C): to be
  covered by the recovery fund the contractor must have been licensed "1.
  The date that the underlying contract was signed. 2. The date that the
  first payment was made. 3. The date that the underlying work first
  commenced."
- **The casual-work exemption is closed to a house** — § 32-1121(A)(14)
  exempts unlicensed work under an aggregate contract price of $1,000 that
  is "of a casual or minor nature," but "This exemption does not apply: (a)
  In any case in which the performance of the work requires a local building
  permit. (b) In any case in which the work or construction is only a part of
  a larger or major operation." A house build is both.
- **Gas and fire-safety work are never exempt under (A)(4), (9) or (14)** —
  § 32-1121(D): "All fire safety and mechanical, electrical and plumbing
  work that is done in connection with fire safety installation" ("hardwired
  or interconnected smoke alarms and fire sprinklers") and "All work done …
  that involves connecting to any supply of natural gas, propane or other
  petroleum or gaseous fuel." Note (D) limits paragraphs 4, 9 and 14 — not
  paragraph 5. The owner-builder may still do this work personally; a
  non-employee helper may not.
- **The crime** — § 32-1151: "It is unlawful for any person … to engage in
  the business of, submit a bid … act or offer to act in the capacity of or
  purport to have the capacity of a contractor without having a contractor's
  license … **Evidence of securing a permit from a governmental agency or the
  employment of a person on a construction project shall be accepted in any
  court as prima facie evidence of existence of a contract.**" § 32-1164(A)(2),
  (B): acting as a contractor without a license is a **class 1 misdemeanor**,
  fine "not less than one thousand dollars" for a first offense and "not less
  than two thousand dollars" thereafter. § 32-1153: an unlicensed contractor
  cannot sue to collect. § 33-981(C): "A person who is required to be
  licensed as a contractor but who does not hold a valid license … shall not
  have the lien rights."

The chapter penalises the unlicensed *contractor*, not the owner who hired
one (§ 32-1101(B): "Only contractors as defined in this section are licensed
and regulated by this chapter"). The owner's exposure is practical: no
recovery fund, no ROC complaint jurisdiction, and a helper who can walk away
without lien or contract rights — and, if the helper is not a wage employee,
a possible workers' compensation and injury-liability problem (§ 5.9).

### 5.4 Trade licensing — Arizona licenses contractors, not tradespeople `[V]`

§ 32-1101(A)(3) defines "Contractor" as anyone who "for compensation" builds,
alters or repairs or does "any part thereof," including one who "Connect[s]
such a structure or improvements to utility service lines and metering
devices and the sewer line" and who "Provide[s] mechanical or structural
service." § 32-1101(B): "Only contractors as defined in this section are
licensed and regulated by this chapter." § 32-1121(B): a person licensed in
a trade "is not required to obtain and maintain a separate license for
mechanical or structural service work the person performs within the scope
of that trade."

**The owner-builder is expressly not a residential contractor** —
§ 32-1101(A)(10)(b): "Residential contractor … Does not include an owner
making improvements to the owner's property pursuant to section 32-1121,
subsection A, paragraph 5." That is the statutory basis for the guide's
correct statement that an owner-occupant may do their own electrical and
plumbing: the ROC chapter simply does not reach them. Whether the AHJ will
*issue* a homeowner an electrical or plumbing permit is a local
administrative question (§ 3.6), and the jurisdictions' own sites answer it
for owner-occupied houses (Goodyear, Chandler, Tucson, Casa Grande, Apache
County) — with rentals excluded everywhere.

### 5.5 Building for sale or rent — § 32-1121(A)(6) `[V]`

"Owners of property who are acting as developers and who build structures …
for the purpose of sale or rent and who contract for such a project with a
general contractor licensed pursuant to this chapter … To qualify for the
exemption under this paragraph, the licensed contractors' names and license
numbers shall be included in all sales documents." There is no
owner-as-general-contractor route to a spec house.

### 5.6 Contract terms — § 32-1158 as the drafting benchmark `[V]`

Every contract "in an amount of more than $1,000 entered into between a
contractor and the owner of a property to be improved shall contain in
writing at least": contractor name, business address and license number;
owner name and mailing address and the jobsite address or legal description;
contract date; "The estimated date of completion"; description of the work;
"The total dollar amount … including all applicable taxes"; "The dollar
amount of any advance deposit"; "The dollar amount of any progress payment
and the stage of construction at which the contractor will be entitled to
collect progress payments"; and the owner's right to complain to the
Registrar, "prominently displayed in the contract in at least ten-point bold
type." (B): the contractor must give "a legible copy of all documents signed
and a written and signed receipt for … any cash paid." (C): none of this is
"a prerequisite to the formation or enforcement of a contract."

**No statutory deposit cap exists** (contrast Pennsylvania's one-third). The
kit prints the § 32-1158 list as the minimum and adds its own deposit and
lien-waiver terms as negotiated items, labelled as such.

### 5.7 Recovery fund — the owner-builder is an eligible claimant `[V]`

§ 32-1132(B)(1): an individual who "(a) Owns residential real property that
is damaged by the failure of a residential contractor to adequately build or
improve a residential structure or appurtenance" and "(b) Actually occupies
or intends to occupy the residential real property … as the individual's
primary residence." Also an LLC with an occupying member and a revocable
living trust whose trustors occupy. The fund pays only for damage by a
"residential contractor that is licensed pursuant to this chapter" —
another reason the licensed-sub route matters.

### 5.8 Liens — the owner-occupant shield `[V]`

- **§ 33-1002(B)**: "No lien provided for in this article shall be allowed or
  recorded by the person claiming a lien against the dwelling of a person who
  became an owner-occupant prior to the construction … **except by a person
  having executed in writing a contract directly with the owner-occupant**."
  (C): any waiver of this section "is void." Definition in § 5.2 item 4:
  recorded title before commencement plus 30 days' residence in the year
  after completion.
- **§ 33-981(B)**: "Every contractor, subcontractor, architect, builder or
  other person having charge or control of the construction … is the agent of
  the owner for the purposes of this article, and the owner shall be liable
  for the reasonable value of labor or materials furnished to his agent."
  Outside the owner-occupant shield, this is how a sub's supplier reaches the
  owner.
- **§ 33-992.01(B), (C)**: "Except for a person performing actual labor for
  wages, every person who furnishes labor, professional services, materials
  … shall, as a necessary prerequisite to the validity of any claim of lien,
  serve the owner … with a written preliminary twenty day notice," given
  "not later than twenty days after the claimant has first furnished" to the
  jobsite. Kit: a file of every 20-day notice received is the lien ledger.

Kit rule for AZ.5: **write a direct contract with every sub and supplier you
want to have lien rights, and none with anyone else** — the shield only
works for an owner-occupant, and only against parties without a direct
written contract.

### 5.9 Workers' compensation `[V]`

- § 23-902(A): employers subject to the chapter include "every person who
  employs any workers or operatives regularly employed in the same business
  or establishment under contract of hire … except domestic servants. …
  'regularly employed' includes all employments, whether continuous
  throughout the year, or for only a portion of the year, **in the usual
  trade, business, profession or occupation of an employer**."
- § 23-901(6)(b): "employee" excludes "a person whose employment is both:
  (i) Casual. (ii) Not in the usual course of the trade, business or
  occupation of the employer."
- § 23-902(B) (statutory employer) applies only where the contracted work "is
  a part or process in the trade or business of the employer."
- § 23-902(D): a written independent-contractor agreement with the eight
  listed statements "creates a rebuttable presumption of an independent
  contractor relationship" if it discloses that the contractor is not
  entitled to workers' compensation from the business.
- § 23-961(N): a sole proprietor may sign the statutory waiver form ("I am a
  sole proprietor … I am not the employee of … for workers' compensation
  purposes").

`[H]` No Arizona statute says in terms that a homeowner building a personal
residence is or is not an "employer." The two-part test in § 23-901(6)(b)
(casual **and** outside the employer's trade) is the closest thing to a
homeowner exemption, and it is fact-dependent. The kit prints the test, the
§ 23-902(D) agreement and the § 23-961(N) waiver as the paper to have, and
tells the reader to put the coverage question to the Industrial Commission
of Arizona in writing before the first day of paid labor. The published
guide's flat "Workers' comp not required for casual labor" is deleted (§ 12).

### 5.10 Lifetime of a claim against a contractor `[V]`

§ 32-1162(A): a written complaint to the Registrar "must be filed: 1. For
new home builds or other new building construction, **within two years after
the earlier of the close of escrow or actual occupancy**. 2. For all other
projects, within two years after the completion of the specific project."
§ 32-1158(A)(9) requires every contract over $1,000 to state this period.
Kit: the two-year ROC window starts the day you move in, not the day the
defect appears.

### 5.11 ⚠ The statewide owner-builder statement — A.R.S. § 32-1169 `[V]`

This is the Arizona equivalent of California's H&S § 19825, and it is the
statute every "no statewide form" summary (including § 2.3 and § 3.6 above,
written before this section was retrieved — see § 10) misses. Verbatim:

> "A. Each county, city or other political subdivision or authority of this
> state … that requires the issuance of a building permit as a condition
> precedent to the construction … of a building … for which a license is
> required under this chapter, as part of the application procedures which it
> uses, **shall require that each applicant for a building permit file a
> signed statement that the applicant is properly licensed** to perform the
> work described in the permit under this chapter with the applicant's
> license number. **If the applicant purports to be exempt from the licensing
> requirements of this chapter, the statement shall contain the basis of the
> asserted exemption and the name and license number of any general,
> mechanical, electrical or plumbing contractor who will be employed on the
> work.** The local issuing authority may require from the applicant a
> statement signed by the registrar to verify any purported exemption.
>
> B. The filing of an application containing false or incorrect information
> concerning an applicant's contractor's license with the intent to avoid the
> licensing requirements of this chapter is **unsworn falsification pursuant
> to section 13-2704**."

Consequences for the kit:

1. The "Owner/Builder Affidavit," "Owner-Builder Declaration," "exemption
   block" and "verification" forms in § 3.6 are all the same thing: each
   AHJ's implementation of § 32-1169(A). The **content** is statutory (basis
   of exemption = § 32-1121(A)(5); names and license numbers of every
   licensed sub you will use); only the **form** is local.
2. An owner-builder must therefore know, at application, which licensed
   general, mechanical, electrical and plumbing contractors will be on the
   job. AZ.2's checklist puts "list of licensed subs with ROC numbers" before
   the permit application, not after.
3. The AHJ "may require … a statement signed by the registrar to verify any
   purported exemption" — the kit tells the reader to ask the counter whether
   it wants an ROC-signed verification and, if so, to get it first.
4. A false statement is a crime (§ 13-2704). The one-year no-sale rule is
   civil and rebuttable; lying on the § 32-1169 statement is not.

Maricopa County's own FAQ cites exactly this section: "Written documentation
of an Arizona licensed contractor or owner-builder classification is
required for all building permits per state law. Refer to ARS 11-1605,
32-1121, 32-1151, and 32-1169."

### 5.12 No chapter licenses electricians or plumbers as individuals `[V]`

The Title 32 table of contents on azleg.gov (read 8 September 2026) lists
one construction chapter — **Chapter 10, Contractors** — and no chapter for
electricians, plumbers, HVAC technicians or journeymen of any kind; the other
chapters are architects/engineers (Ch. 1) and the health, cosmetology,
real-estate and similar professions. Individual trade competency in Arizona
is a matter for the licensed contracting entity's qualifying party
(§ 32-1101(A)(8)), not a state trade card. `[H]` Whether any city licenses
tradespeople by ordinance was not verified; none of the twenty city sites
read in § 3.2 mentioned such a licence.

---

## 6. SITE PLAN STUDIO EXTRACTION

Feeds `src/lib/siteplan/rules.ts`. Two statewide rulebooks apply on every
Arizona lot:

- **Septic**: 18 A.A.C. 9, Article 3 (ADEQ general Aquifer Protection
  Permits), administered by the county agency ADEQ has delegated under
  § 49-107 (issuer per county in § 3.1). Text read from the Legal Information
  Institute's reproduction of the A.A.C., current through the amendment at
  29 A.A.R. 1023 **effective 19 June 2023**, and cross-checked against the
  Secretary of State's official compilation (Supp. 17-4, hosted by Cochise
  County) and La Paz County's published "R18-9-A312(C) Setback Table." The
  2023 amendment added three parentheticals to the table ("including pool
  decks"; "including domestic water holding tanks"; canal measured "from the
  edge of the canal"); the numbers did not change. `[V]`
- **Wells**: A.R.S. Title 45 (read on azleg.gov) and 12 A.A.C. 15, Article 8
  (ADWR well construction, read from LII). `[V]`

> **Framing note for the tool.** R18-9-A312(C): "The following setbacks apply
> unless the Department: 1. Specifies alternative setbacks under Article 3,
> Part E of this Chapter; 2. Approves a different setback under the procedure
> specified in subsection (G); or 3. **Establishes a more stringent setback on
> a site- or area-specific basis** to ensure compliance with water quality
> standards." Present every number as a regulatory minimum the delegated
> county may increase, never as an approval. And the setbacks are measured to
> the facility "**Including Reserve Area**" — the reserve field counts.

### 6.1 R18-9-A312(C), Table — setbacks in feet `[V]`

| # | Feature requiring setback | Feet | Special provision (verbatim, abridged) |
|---|---|---|---|
| 1 | **Building** | **10** | "Includes porches, decks (including pool decks), and steps (covered or uncovered), breezeways, roofed patios, carports, covered walks, and similar structures" |
| 2 | **Property line shared with any adjoining lot or parcel not served by a common drinking water system or an existing water well** | **50** | Reducible "to a minimum of 5 feet" if "The owners of any affected undeveloped adjacent properties agree, as evidenced by an appropriately recorded document, to limit the location of any new well on their property to at least 100 feet from the proposed treatment works and primary and reserve disposal works" and the Department approves |
| 3 | All other property lines | 5 | None |
| 4 | **Public or private water supply well** | **100** | None |
| 5 | Perennial or intermittent stream | 100 | "from the high water line of the peak streamflow from a 10-year, 24-hour rainfall event" |
| 6 | Lake, reservoir, or canal | 100 | high water line (10-year, 24-hour event); "from the edge of the canal" |
| 7 | Drinking water intake from a surface water source | 200 | to the intake structure |
| 8 | **Wash or drainage easement with a drainage area of more than 20 acres** | **50** | "from the nearest edge of the defined natural channel bank or drainage easement boundary"; reducible to 25 ft with erosion protection approved by the floodplain administrator |
| 9 | Water main or branch water line | 10 | None |
| 10 | Domestic service water line (including domestic water holding tanks) | 5 | crossing allowed at 45–90° with 1 ft vertical separation; parallel at 1–5 ft if the water line is 1 ft above and in a separate trench or bench |
| 11a | Downslopes or cut banks > 15%, culverts, ditches — from treatment works components | 10 | to the closest point of daylighting |
| 11b | — from trench, bed, chamber or gravelless trench, no limiting subsurface condition | 20 | |
| 11b | — same, with a limiting subsurface condition (R18-9-A310(D)(2)) | 50 | |
| 11c | — from subsurface drip lines | 3 | |
| 12 | Driveway | 5 | to the nearest edge of the excavation; a reinforced tank may sit under a driveway, "except for disposal works" |
| 13 | Swimming pool excavation | 5 | "Except if soil loading or stability concerns indicate the need for a greater separation" |
| 14 | Easement (except drainage easement) | 5 | None |
| 15 | **Earth fissures** | **100** | None |

Footnote to row 2, verbatim: "A 'common drinking water system' means a system
that currently serves or is under legal obligation to serve the property and
may include a drinking water utility, a well-sharing agreement, or other
viable water supply agreement."

**The two numbers the tool leads with**: well-to-any-septic-component
**100 ft** (row 4, and it is the *same* 100 ft the neighbour must promise in
the row-2 waiver), and the **50-ft property-line rule on well-served lots**,
which is the one that breaks small rural parcels. La Paz County's own
"Well-Property Line 50ft Setback Waiver" shows the practice: both owners
sign, notarised, "record this document to deed … within 30 days, or the
waiver is null and void." `[V]`

### 6.2 Reserve area and sizing — R18-9-A312(D), R18-9-A314 `[V]`

- **Reserve area** (A312(D)(4)(a)): "For a dwelling, a primary area for the
  disposal works sized according to subsection (D)(1) **and a reserve area of
  100 percent of the primary area**, excluding the footprint of the treatment
  works. A reserve area is not required for a lot in a subdivision approved
  before 1974 if the lot conforms to its original approved configuration."
- **Absorption area** (A312(D)(1)): "the soil absorption area by dividing the
  design flow by the applicable soil absorption rate"; where methods
  disagree, "use the lowest SAR value."
- **Design flow and tank size** (A314(A)(4)(a)) — by bedrooms and fixture
  count:

| Bedrooms | Fixture count | Min. tank (gal) | Design flow (gpd) |
|---|---|---|---|
| 1 | ≤ 7 / > 7 | 1000 / 1000 | 150 / 300 |
| 2 | ≤ 14 / > 14 | 1000 / 1000 | 300 / 450 |
| 3 | ≤ 21 / > 21 | 1000 / 1250 | 450 / 600 |
| 4 | ≤ 28 / > 28 | 1250 / 1500 | 600 / 750 |
| 5 | ≤ 35 / > 35 | 1500 / 2000 | 750 / 900 |
| 6 | ≤ 42 / > 42 | 2000 / 2500 | 900 / 1050 |

  Fixture units (A314(A)(4)(a)(ii)): water closet 1.6 gpf **3**; bathtub 2;
  bidet 2; clothes washer 2; separate dishwasher 2; kitchen sink incl.
  dishwasher 2; service sink 3; utility tub 2; single lavatory 1; bar sink 1.
  So a 3-bedroom house with two full baths, kitchen, laundry and a utility
  sink is already near the 21-unit line — the fixture count, not the bedroom
  count, decides whether the tank is 1,000 or 1,250 gallons. Minimum tank is
  **1,000 gallons** on any dwelling. Tank geometry (A314(A)(1)(c)): two
  compartments, inlet compartment 67–75% of capacity, liquid depth ≥ 42 in,
  1,000-gal tank ≥ 8 ft long; (d) two 20-in access openings with risers "to
  ensure accessibility within 6 inches below finished grade."
- **Soil absorption rate** (A312(D)(2)(a)), percolation minutes/inch →
  SAR gal/day/sq ft for trench/chamber/pit (bed in parentheses): < 1.00 —
  **site-specific SAR required**; 1–3: 1.20 (0.93); 3: 1.10 (0.73); 5: 0.90
  (0.60); 10: 0.63 (0.42); 15: 0.50 (0.33); 20: 0.44 (0.29); 30: 0.36 (0.24);
  45: 0.29 (0.20); 60: 0.25 (0.17); 60+ to 120: 0.20 (0.13); > 120 —
  site-specific required. Between listed values use the slower rate
  ((D)(2)(c)). Worked example for the tool's help text: 3 bedrooms, ≤ 21
  fixtures, 450 gpd, perc 10 min/in → 450 ÷ 0.63 ≈ **714 sq ft** of trench
  absorption area, then the same again in reserve.
- **Trench geometry** (E302(C)(2)(c)): length ≤ 100 ft; bottom width 12–36
  in; absorption area counted as bottom plus both sidewalls to 48 in below
  the pipe, max 11 sq ft per linear foot; cover over aggregate 9–24 in;
  aggregate 12 in under and 2 in over the pipe; pipe 3–4 in, level; spacing
  "2 times effective depth or five feet, whichever is greater." Beds: width
  10–12 ft, pipes 4–6 ft apart, cover 9–14 in. Nothing may be paved over a
  disposal works (E302(C)(1)(h)).

### 6.3 Vertical separation to groundwater — R18-9-A312(E)(1) `[V]`

For a septic-tank-effluent trench or chamber: SAR 0.63–1.20 → **10 ft** to the
seasonal high water table; SAR 0.20–0.63 → **5 ft**; seepage pit → **60 ft**;
SAR ≥ 1.20 or < 0.20 → "Not allowed for septic tank effluent." Less
separation forces a treatment technology from E303–E322 (A312(E)(2)).

### 6.4 Site limiting conditions — R18-9-A310 `[V]`

Arizona calls these "limiting conditions," not disqualifiers: a limiting
condition removes the standard 4.02 septic-tank option and pushes the design
to an alternative general permit (E302(A)(1): the standard design "serves
sites where no site limitations are identified"). The tool should flag, not
deny.

**Surface** (A310(C)(2)): slope "greater than 15 percent at the intended
location"; setbacks in A312(C) not met; adverse surface drainage; "A 100-year
flood hazard zone, as indicated on the applicable flood insurance rate map,
is located within the property … and the flood hazard zone may adversely
affect the ability of the facility to function properly"; "An outcropping of
rock that cannot be excavated"; "Fill material deposits exist in the intended
location."

**Subsurface, within 12 ft of the surface** (A310(D)(2)): SAR above 1.20 or
below 0.20 gal/day/sq ft; vertical separation below A312(E)(1); seasonal
saturation in surface soils; an impervious layer, a saturation zone, or "Soil
with more than 50 percent rock fragments"; open fractures, karst, or cobble
deposits; any condition conveying wastewater to a water of the state.

**Who may do the site investigation** (A310(H)): only "an Arizona-registered
professional engineer," "Arizona-registered geologist," "Arizona-registered
sanitarian," a holder of "a certificate of training from a course recognized
by the Department," or another Department-designated category. **An
owner-builder cannot self-certify the perc test.** Test locations: at least
two in the primary area and one in the reserve (A310(E)(1), (F)(1)(a)).

### 6.5 The sewer-availability rule — R18-9-A309(A)(5) `[V]`

A person constructing a new onsite facility "shall connect to a sewage
collection system if" a nitrogen-management designation, "A county, municipal,
or sanitary district ordinance," or an adopted area-wide plan requires it,
**or** "A sewer service line extension is available at the property boundary
and both of the following apply: i. The service connection fee is not more
than $6000 for a dwelling … and ii. The cost of constructing the building
sewer from the wastewater source to the service connection is not more than
$3000 for a dwelling." The tool's septic path should ask whether a sewer
stub exists at the lot line.

### 6.6 The septic permit process and clocks `[V]`

R18-9-A301(D): "A person shall not begin facility construction until the
Director issues a **Construction Authorization**" (issued after review of the
Notice of Intent to Discharge); "A person shall complete construction within
**two years** of receiving a Construction Authorization"; after construction
the applicant submits the Request for Discharge Authorization; the agency
"may inspect the facility before issuing a **Discharge Authorization**"; if
the completion documents are not received within the two years "the Notice
of Intent to Discharge expires, and the person shall not continue
construction or discharge." Changes during construction that still conform
to the rule's standard need no re-approval but must be recorded on the site
plan (A301(D)(1)(e)).

ADEQ's Notice of Intent form (DWS 402, rev. April 2025, read from La Paz
County's posted copy) states ADEQ's own licensing time frames under
R18-1-525: a single 4.02 general permit is **42 business days
administrative + 31 substantive = 73 overall**; each R18-9-A312(G)
alternative request "adds eight business days"; priority review doubles the
fee; and "Review fees established by delegated counties or cities may
differ." `[V]` These are ADEQ's clocks; a delegated county's clock is the
county's (§ 4.1 — county residential-lot licences are outside § 11-1605).

### 6.7 Transfer of ownership — R18-9-A316 `[V]`

"Within six months before the date of property transfer, the person who is
transferring a property served by an on-site wastewater treatment facility
shall retain an inspector to perform a transfer of ownership inspection."
Qualified inspectors: registered engineer or sanitarian, a licensed septage
hauler, "A contractor licensed by the Registrar of Contractors in one of the
following categories: i. Residential license B-4 or C-41; ii. Commercial
license A, A-12, or L-41; or iii. Dual license KA or K-41," or a certified
wastewater operator — each with an ADEQ-recognised training certificate.
The Report of Inspection must show the tank was pumped unless a Discharge
Authorization issued and the facility "was put into service within 12 months
before" the inspection. The buyer files a Notice of Transfer "within 15
calendar days after the property transfer" with the delegated county agency
(for facilities built on or after 1 January 2001). (F): no inspection is
required if a Discharge Authorization issued but the facility "was not put
into service before the property transfer." Kit: an owner-builder who sells
inside the one-year window is selling a house with a septic system under
one year old, and A316(C)(2)(a) is written for exactly that case.

### 6.8 Wells — statute `[V]`

| Rule | Text | Cite |
|---|---|---|
| Exempt well | Non-irrigation withdrawals "from wells having a pump with a maximum capacity of not more than thirty-five gallons per minute" drilled on or after 28 April 1983 are exempt from the Groundwater Code except as listed | § 45-454(B) |
| Notice of intent | "A person shall file a notice of intention to drill with the director pursuant to section 45-596 before drilling an exempt well or causing an exempt well to be drilled" | § 45-454(G) |
| **The 100-ft municipal-provider rule** | From 1 Jan 2006 "an exempt well … may not be drilled on land if any part of the land is within one hundred feet of the operating water distribution system of a municipal provider with an assured water supply designation within the boundaries of an active management area established on or before July 1, 1994" — exemptions on request if service is refused within 30 days, if connecting costs more than the well, if an easement is refused, or on a written no-service agreement | § 45-454(C), (D) |
| One exempt well per use per site in an AMA | with a second allowed only if the first cannot produce 3 gpm, the parcel is ≥ 1 acre, combined draw ≤ 5 AF/yr and the county health authority has approved the location in writing after a site visit | § 45-454(I) |
| Licensed driller | "New well construction, including modifications of wells, shall be performed under the direct and personal supervision of a well driller who holds a well driller's license" | § 45-595(A) |
| **Owner may drill an exempt well on own land** | "A person who drills or modifies an exempt well on land owned by that person shall first obtain a single well license from the department. The department shall issue the license to drill the well according to standard small well construction standards. **No fee may be charged for a single well license**" | § 45-595(D); R12-15-801(25) |
| **Domestic well site plan on ≤ 5 acres** | "If any water from a proposed well will be used for domestic purposes … on a parcel of land of five or fewer acres, the applicant shall submit a well site plan of the property with the notice of intention to drill. The site plan shall: 1. Include the county assessor's parcel identification number. 2. Show the proposed well location and the location of any septic tank or sewer system that is either located on the property or **within one hundred feet of the proposed well site**. 3. Show written approval by the county health authority that controls the installation of septic tanks" | § 45-596(F) |
| Variance | Where "parcel size, geology or location of improvements on the property prevents the well from being drilled" in compliance, a variance may be requested; the county or ADWR "may expressly require that a particular variance shall include certification by a registered professional engineer or geologist that the location of the well will not pose a health hazard" | § 45-596(G) |
| Drilling card | Within 15 days of a complete notice the director records it and "mail[s] a drilling card that authorizes the drilling of the well to the well driller" | § 45-596(D) |
| Completion | "The well shall be completed within one year after the date of the notice" | § 45-596(E) |
| Fee | $150, "except that a notice filed for a proposed well that will not be located within an active management area or an irrigation nonexpansion area, that will be used solely for domestic purposes … and that will have a pump with a maximum capacity of not more than thirty-five gallons per minute shall be accompanied by a filing fee of one hundred dollars" | § 45-596(L) |
| Reports | Driller's report within 30 days of completion; **owner's** completion report within 30 days after pump installation (equipment, 4-hour tested capacity, drawdown, static level) | § 45-600 |
| Open wells | A new owner reports any open well "within thirty days after a change of ownership" | § 45-593(D) |

### 6.9 Wells — construction rules, 12 A.A.C. 15, Art. 8 `[V]`

- **R12-15-811(A)(1)**: "only steel or thermoplastic casing"; casing "shall
  extend a minimum of one foot above ground level" (may terminate below grade
  with a pitless adaptor).
- **R12-15-811(B)(1) — surface seal**: "steel casing, one foot of which shall
  extend above ground level, and cement grout placed in one continuous
  application … **The minimum length of the steel casing shall be 20 feet.
  The minimum annular space between the casing and the borehole for placement
  of grout shall be one and one-half inches** … The minimum length of the
  surface seal shall be 20 feet." Hand-dug wells: watertight curbing to the
  static level, ≥ 6 in poured grout ((B)(2)).
- **R12-15-811(C)**: casing ≥ 4 in must have a watertight ½-in access port;
  (E) vents open downward and screened.
- **R12-15-821**: the Director "may require that further additional measures
  be taken, such as increasing the length of the surface seal or increasing
  the well's minimum distance from a potential source of contamination."
- **R12-15-816**: abandonment "only by a licensed well drilling contractor or
  single well licensee," after a notice of intent to abandon and an
  abandonment card; completion report within 30 days; 20-ft grout plug.
- **R12-15-818 — Well Location, verbatim**: "Except for monitor wells and
  piezometer wells, **no well shall be drilled within 100 feet of any septic
  tank system, sewage disposal area**, landfill, hazardous waste facility,
  storage area of hazardous materials or petroleum storage areas and tanks,
  unless authorized in writing by the Director." So the 100 ft is stated from
  both sides — ADEQ (A312(C) row 4, septic to well) and ADWR (well to
  septic) — and only ADWR's Director can waive its side, in writing. (An
  earlier draft of this bullet said Article 8 carried no number; see § 10.)
- **R12-15-807 — the single well licence is an exam, not a form**: the
  application lists the well location, ownership, the drill rig and its
  owner, the proposed design, "The names of any people who will be assisting
  the applicant … and whether the applicant will compensate them," and the
  applicant's experience; the Director offers the examination "no less than
  six times yearly"; passing grade **70 percent**; the licence authorises
  "one exempt well at the location specified" and "shall be valid for a
  period of one year." R12-15-803(B): no one but "a single well licensee or a
  bona fide employee of a well drilling contractor" may drill. R12-15-809: the
  notice of intention "shall be signed by the owner or lessee of the
  property." R12-15-810(A): drilling may start only with the drilling card
  "at the well site."

### 6.10 Who may install the septic system — R18-9-A309(C) `[V]`

The rule splits on system type, and the split is the answer to "can I put in
my own septic":

- **Conventional (everything under R18-9-E302)** — A309(C)(1): "If the entire
  on-site wastewater treatment facility, including treatment works and
  disposal works, will be permitted under R18-9-E302, the Director shall issue
  the Discharge Authorization if, as a part of the Request for Discharge
  Authorization: a. The site plan accurately reflects the final location and
  configuration of the components of the treatment and disposal works, and
  b. The applicant or the applicant's agent certifies … that the septic tank
  passed the watertightness test required by R18-9-A314(5)(d)." **No
  installer licence number is required.** Read with § 32-1121(A)(5) (the owner
  may "do the work themselves"), an owner-builder may install a conventional
  system, subject to the delegated county's inspection before backfill.
  Mohave County publishes an "On-Site Wastewater Application for
  Owner/Builders" (§ 3.1). `[V]`
- **Alternative (anything under R18-9-E303 to E323, alone or combined)** —
  A309(C)(2) requires, among other documents, "f. A Certificate of Completion
  signed by the current engineer or designer of record assuring that
  installation of the facility conforms to the design … and a regulatory
  representative, such as an inspector, may not act as an applicant's agent,
  nor authorize backfill before the current engineer or designer of record
  has verified proper installation of the system; **g. The name of the
  installation contractor and the Registrar of Contractor's license number
  issued to the installation contractor**; and h. A certification that any
  septic tank … passed the water-tightness test." An alternative system
  therefore needs a licensed installer and a designer of record; the
  owner-builder cannot be the installation contractor of record.

The site investigation is a licensed act in both cases (A310(H), § 6.4).

### 6.11 Do NOT encode

- **Building setbacks from lot lines** — county and municipal zoning; no
  statewide value.
- **A well-to-property-line distance** — none exists in Title 45 or 12 A.A.C.
  15 Art. 8. R12-15-818 fixes 100 ft to septic systems and contamination
  sources only; the property line is reached indirectly through ADEQ's
  50-ft septic-to-line rule on well-served lots (§ 6.1 row 2).
- **Any county's larger setbacks** — A312(C)(3) lets the agency impose them
  site by site; the tool prints the state table and a write-in line.
- **Flood, frost, snow, wind, seismic** — the locally adopted IRC Table
  R301.2 as amended; no statewide table.
- **Energy R-values** — § 3.5.
- **Sewer connection fees** — the $6,000 / $3,000 figures in § 6.5 are
  *thresholds in the rule*, not fees; print them as the rule's test only.

---

## 7. DELIBERATELY NOT PRINTED

| Item | Why |
|---|---|
| Permit, plan-review, impact or tap fee dollar figures | No state schedule; § 11-863(C) "reasonable fees," § 9-467(G)/§ 11-321(I) "reasonable costs." The kit prints the § 9-468/§ 11-323 itemised-list right for solar and tells the reader fee schedules are public. |
| Any review time in days for a **county** permit | § 11-1605(M)(2) carves residential-lot licences out of the time-frame statute. Printing a number would invent a right that does not exist. |
| A statewide IRC, NEC or IECC year | None is adopted statewide (§ 3). The map is printed with a retrieval date instead. |
| IECC climate zones and R-values | Not verified to a primary source in this pass; Maricopa County's energy chapter is voluntary and five counties have no energy code. |
| The state fire code edition | dffm.az.gov blocks both curl and the browser extension; § 37-1383 was read but not the DFFM rule. The kit says the state fire code exists and points to the fire district. |
| "Once per 24 months," "once per five years," "must live in it two years" | None is in § 32-1121. The five-year figure is Cochise's local opt-out limit and is printed only as that. |
| A homeowner workers'-compensation bright line | § 23-901(6)(b) is a two-part fact test; no statute exempts a homeowner by name. The kit prints the test and the § 23-902(D)/§ 23-961(N) paper. |
| Utility pre-energisation requirements (APS, SRP, TEP, UniSource, co-ops) | Service-requirement manuals not fetched. The kit tells the reader to get the utility's clearance rule in writing before framing. |
| Well depths, drilling costs, septic system costs | Unsourced in the guide; not the kit's business. |
| Phone numbers | House rule. The ADEQ NOI form and every county page carry them; the kit prints URLs and a write-in line. |
| Named installers, designers, third-party reviewers | § 9-470.01 lists are municipal; naming firms is an implied endorsement. |
| Which city or county requires an ROC-signed exemption verification under § 32-1169(A) | "May require" — not verified for any jurisdiction. The kit tells the reader to ask at the counter. |
| Apache and Santa Cruz county detail beyond code editions | Both county sites are Cloudflare-walled; editions were read from archived copies of the counties' own PDFs (March 2025 and May 2026) and are printed with that caveat. |
| ADEQ's fee schedule | azdeq.gov/SepticSewerFees unreachable; delegated county fees differ anyway. |

---

## 8. OPEN QUESTIONS

1. **State fire code edition and DFFM rule cite.** § 37-1383(A)(2) read; the
   adopted IFC edition (A.A.C. R4-36-…) not retrieved because dffm.az.gov is
   JavaScript-walled to curl, WebFetch and the browser extension's domain
   list. Needed only to correct guide line 47; not needed by the kit.
2. **ROC's own owner-builder page.** roc.az.gov/faq and
   /license-classifications were read in the browser; neither carries an
   owner-builder Q&A. The ROC's News page has an unlicensed-builder story
   mentioning an "owner-builder permit application." If an ROC owner-builder
   notice exists it was not found; the kit cites the statute.
3. **§ 9-470.01's reach for a one-off custom house.** The 15-working-day
   trigger presupposes approved construction documents; § 4.3's reading (the
   clock attaches after plan approval) is `[H]`. Confirm with a city ≥ 30,000
   before the kit promises anything beyond the statute's words.
4. **Whether any Arizona city licenses tradespeople by ordinance.** None of
   the twenty city sites read mentions one; Title 32 has no such chapter.
   Negative not proven for 91 municipalities.
5. **Utility clearance in no-code counties.** What APS/SRP/TEP/UniSource/the
   co-ops require before setting a meter where no building inspection
   exists (Greenlee; Cochise Option 2). Service-requirements manuals not
   fetched.
6. **Pima County**: adoption date of Ord. 2025-15 and effective date of the
   2024 IECC amendment set (Ord. 2026-6). **Tempe, Yuma city, Goodyear,
   Buckeye, Sierra Vista**: adopting ordinance numbers for the 2024 sets.
7. **Cochise County septic issuer** — not stated on the county pages read;
   the OBA says "Cochise County Environmental Health Department
   regulations."
8. **Apache and Santa Cruz county pages** — verify live once the Cloudflare
   wall allows; Apache's "2015 IRC / 2011 NEC" and "NOT VERIFIED" energy
   code are from an archived copy of the county's own FAQ.
9. **A.A.C. R18-1-525** (ADEQ licensing time frames) was read only as
   restated on ADEQ's NOI form DWS 402 (April 2025), not from the rule.
10. **Full text comparison of the 2023 onsite-rule amendment (29 A.A.R.
    1023, eff. 19 June 2023).** Table 1 of R18-9-A312(C) was compared line
    by line between the 2017 official compilation and the current text; the
    rest of Article 3 was read only in the current text. If the kit quotes
    E302 trench geometry, confirm it was not touched in 2023.
11. **Yuma County NEC** — county page posts 2020 NEC amendments; whether the
    2023 NEC came in with the City of Yuma's 2025 adoption (which the county
    adopts by reference under § 11-861(C)(1)) not verified.
12. **The § 32-1169(A) ROC-signed verification** — which counters ask for
    it. Unknown.
13. **§ 49-245(E), (H)** refer to general-permit rules "proposed after
    December 31, 2024" and "after September 26, 2025" — an ADEQ onsite-rule
    revision is in motion. Its status was not retrievable (azdeq.gov
    walled). See § 9.

---

## 9. KIT REVISION WATCH — ARIZONA TRIPWIRES

Add to `project-kit-revision-watch`:

1. **ADEQ onsite-rule rewrite.** § 49-245(E) and (H) (as read 3 September
   2026) anticipate revised general-permit rules "proposed after December
   31, 2024" and "proposed after September 26, 2025," with permittees to
   transition within 180 days of the effective date. When that rulemaking is
   final, R18-9-A312(C) Table 1, R18-9-A314 sizing and R18-9-E302 geometry
   — i.e., § 6 and the Site Plan Studio block — must be re-read. Watch the
   Arizona Administrative Register and ADEQ's onsite page.
2. **Cochise County 2024 codes effective 1 September 2026** (Res. 26-23).
   Now in force; the county FAQ still listed 2015 codes and the 2014 NEC on
   3 September 2026. Re-check the county's pages and whether the
   Owner-Builder Amendment text was re-adopted unchanged.
3. **Year-end 2026 transitions**: Coconino County accepts 2018-code plans
   "through 12/31/26"; Tempe accepts 2018/2017 through 31 December 2026 and
   mandates 2024/2023 from 1 January 2027. AZ.2's map rows change on 1
   January 2027.
4. **Phoenix 2023 NEC 210.8(F) Exception 2** — HVAC GFCI enforcement
   deferred to **1 March 2027**. Drop the note after that date.
5. **The 2018 hold-outs**: Maricopa County (the largest unincorporated
   population), Gilbert, Peoria, Flagstaff ("2024 Codes … being
   evaluated"), Kingman, Sierra Vista, Casa Grande, Pinal, Mohave, Navajo,
   La Paz (adopted 2018 in July 2026). A Maricopa County move to 2024 would
   change the largest single row.
6. **Pima County 2024 IECC** (Ord. 2026-6) — effective date unknown; the
   energy row for Pima flips when it lands.
7. **§ 32-1121 dual versions.** A future session law may reconcile the
   Ch. 140 / Ch. 145 texts; check azleg.gov's Title 32 TOC for a single
   entry. No kit change unless (A)(5) or (A)(6) wording moves.
8. **§ 9-470.01 and § 9-835** are recent and actively amended (the
   third-party review statute post-dates the 2024 session). Watch Title 9
   Ch. 7 Art. 4 and Art. 6.4 each session; the county carve-out in
   § 11-1605(M)(2) is the provision a future bill is most likely to remove.
9. **ADWR exempt-well statute** (§ 45-454) — the 100-ft municipal-provider
   rule and AMA restrictions are perennial legislative targets; re-read each
   session.
10. **Greenlee County** — a 2012 letter is the only source for "no code."
    A county that adopts zoning and then a code under § 11-861(A) would
    erase the kit's cleanest example; check the P&Z page annually.

---

## 10. LATE ADDENDUM

1. **§ 32-1169 reverses the "no statewide owner-builder statement" line.**
   § 2.3 and § 3.6 were written before § 32-1169 was retrieved and say no
   statewide owner-builder form exists. Correct statement: no statewide
   *form* exists, but § 32-1169(A) mandates the *content* of a signed
   exemption statement on every building-permit application, and (B) makes a
   false one unsworn falsification. § 5.11 is the controlling text; § 2.3's
   row now points there. The jurisdiction forms in § 3.6 are implementations
   of § 32-1169, not local inventions.
2. **The two azleg.gov versions of § 32-1121 are not word-for-word identical
   in (A)(5) and (A)(6)** as § 5.1 first said. A word-level diff on
   8 September 2026: (A)(5) differs only in "such **a** project" (Ch. 140
   text) versus "such project" (Ch. 145 text); (A)(6) differs only in
   "**shall** be included in all sales documents" versus "**must** be
   included"; (A)(11) is identical. No substantive difference; the § 5.1
   quotation follows the `/ars/32/01121.htm` text. The kit cites
   "§ 32-1121(A)(5)" without a version.
3. **§ 32-1162(A) retrieved** after § 5.10 was first drafted; § 5.10 now
   carries the two-year figure.
4. **R12-15-818 reverses the "no ADWR well-to-septic number" bullet.** § 6.9
   was first written from the Article 8 section list before R12-15-818 was
   read; the rule fixes **100 feet** from any septic tank system or sewage
   disposal area, waivable only in writing by the ADWR Director. § 6.9 and
   § 6.10 now carry the rule. The 100 ft is therefore stated by both ADEQ and
   ADWR, which is the pattern the tool wants.

---

## 11. VERIFIED URL SET (September 2026)

Status column: **200** = returned HTTP 200 to curl on 8 September 2026;
**wall** = returns 403 to curl and WebFetch but was read in a browser or by
a research subagent on 3 September 2026 (bot-wall, not a dead link). No
phone numbers are printed anywhere in the kit.

### Statutes and rules

| What | URL | Status |
|---|---|---|
| ★ § 32-1121 exemptions | `https://www.azleg.gov/ars/32/01121.htm` | 200 |
| ★ § 32-1169 permit-application statement | `https://www.azleg.gov/ars/32/01169.htm` | 200 |
| § 32-1101 definitions; § 32-1151; § 32-1158; § 32-1162; § 32-1164 | `https://www.azleg.gov/ars/32/01101.htm` etc. | 200 |
| ★ § 11-321 mandatory county permit | `https://www.azleg.gov/ars/11/00321.htm` | 200 |
| § 11-861 county codes; § 11-862; § 11-863; § 11-865; § 11-815 | `https://www.azleg.gov/ars/11/00861.htm` etc. | 200 |
| § 11-1604, 11-1605, 11-1606, 11-1609 (county bill of rights) | `https://www.azleg.gov/ars/11/01605.htm` etc. | 200 |
| § 9-801, 9-802, 9-806, 9-807, 9-808, 9-810, 9-810.01 | `https://www.azleg.gov/ars/9/00807.htm` etc. | 200 |
| ★ § 9-835 city licensing time frames; § 9-834; § 9-836; § 9-839 | `https://www.azleg.gov/ars/9/00835.htm` | 200 |
| ★ § 9-470.01 third-party review | `https://www.azleg.gov/ars/9/00470-01.htm` | 200 |
| § 9-467, 9-468 (building permits; solar) | `https://www.azleg.gov/ars/9/00467.htm` | 200 |
| § 33-981, 33-992.01, 33-1002 (liens) | `https://www.azleg.gov/ars/33/01002.htm` | 200 |
| § 23-901, 23-902, 23-961 (workers' comp) | `https://www.azleg.gov/ars/23/00902.htm` | 200 |
| § 45-454, 45-593–45-600 (wells) | `https://www.azleg.gov/ars/45/00454.htm`; `.../45/00596.htm` | 200 |
| § 49-107, 49-241, 49-245 (APP) | `https://www.azleg.gov/ars/49/00241.htm` | 200 |
| § 36-1681 pools; § 45-312 fixtures; § 28-8482 noise; § 34-451; § 37-1383; § 33-439 | `https://www.azleg.gov/ars/36/01681.htm` etc. | 200 |
| Title TOCs (spot dual versions) | `https://www.azleg.gov/arsDetail/?title=32` | 200 |
| ★ R18-9-A312 setbacks (LII reproduction) | `https://www.law.cornell.edu/regulations/arizona/Ariz-Admin-Code-SS-R18-9-A312` | 200 |
| R18-9-A301, A309, A310, A313, A314, A316, E302 | same pattern, `…-SS-R18-9-A314` | 200 |
| ★ R12-15-818 well location; Article 8 index | `https://www.law.cornell.edu/regulations/arizona/Ariz-Admin-Code-SS-R12-15-818`; `.../title-12/chapter-15/article-8` | 200 |
| Official A.A.C. 18 A.A.C. 9 PDF (Secretary of State) | `https://apps.azsos.gov/public_services/Title_18/18-09.pdf` | wall |
| Official compilation copy (Supp. 17-4) hosted by Cochise County | `https://www.cochise.az.gov/DocumentCenter/View/507/State-Sewage-Rules-PDF` | 200 |

### Agencies

| What | URL | Status |
|---|---|---|
| Registrar of Contractors — home, licence search | `https://roc.az.gov/` | wall |
| ROC licence classifications | `https://roc.az.gov/license-classifications` | wall |
| ADEQ onsite wastewater | `https://www.azdeq.gov/onsite-wastewater-treatment-facilities` | wall |
| ADWR well drilling | `https://www.azwater.gov/permitting-wells/well-drilling-arizona` | wall |
| ADEQ NOI form DWS 402 (April 2025), as posted by La Paz County | `https://www.co.la-paz.az.us/DocumentCenter/View/9258` | 200 |
| FEMA Flood Map Service Center | `https://msc.fema.gov/portal/home` | 200 |

### The two county opt-outs

| What | URL | Status |
|---|---|---|
| ★ Cochise Owner-Builder Amendment page | `https://www.cochise.az.gov/212/Owner-Builder-Amendment` | 200 |
| ★ Cochise Owner-Builder Amendment text (PDF) | `https://www.cochise.az.gov/DocumentCenter/View/24106/Amendment-to-the-Cochise-County-Building-Safety-Code-for-Rural-Residential-Owner-Built-Dwellings-and-Accessory-Structures-PDF` | 200 |
| Cochise Building Safety (2024 codes from 1 Sep 2026) | `https://www.cochise.az.gov/211/Building-Safety` | 200 |
| Coconino Alternative Methods & Materials Permit | `https://www.coconino.az.gov/2173/Alternative-Methods-and-Materials-Permit` | wall |
| ★ Greenlee "Building Codes – Load Stds" letter | `https://greenlee.az.gov/wp-content/uploads/2020/07/Building-Codes-and-Loading-Standards.pdf` | 200 |
| Greenlee Planning & Zoning | `https://greenlee.az.gov/ova_dep/planning-and-zoning/` | 200 |

### Counties — codes and septic

| County | Codes page | Septic page | Status |
|---|---|---|---|
| Maricopa | `https://www.maricopa.gov/2753/Adopted-Regulations`; addenda `https://www.maricopa.gov/DocumentCenter/View/5808/Local-Additions-and-Addenda-PDF` | `https://www.maricopa.gov/1631/Onsite-Wastewater-Septic-Systems` | 200 |
| Pima | `https://www.pima.gov/1038/Building-Permits-Resources` | `https://www.pima.gov/1086/On-Site-Wastewater-Treatment-Facilities` | 200 |
| Pinal | `https://www.pinal.gov/189/Building-Safety` | `https://www.pinal.gov/185/Wells-Septic` | 200 |
| Yavapai | `https://www.yavapaiaz.gov/Development-and-Permits/Codes-Ordinances` | `.../Development-Services/Environmental-Services-Unit` | wall |
| Mohave | `https://www.mohave.gov/departments/development-services/building-division/`; Ord. 2021-03 `https://www.mohave.gov/media/l4npv02v/2021-03-amended-thru-07-15-24.pdf` | owner-builder septic packet `https://www.mohave.gov/media/uo0js5ru/owner-builder-packet-6_2_24.pdf` | 200 |
| Coconino | `https://www.coconino.az.gov/2391/Building-Codes-Ordinances-Design-Criteri` | `https://www.coconino.az.gov/1156/Environmental-Quality` | wall |
| Navajo | `https://www.navajocountyaz.gov/289/Building-Information` | (Planning & Development Services) | 200 |
| Gila | `https://www.gilacountyaz.gov/government/community_development/building_safety/adopted_building_code.php` | (Community Development) | 200 |
| Graham | `https://www.graham.az.gov/277/Planning-Zoning` | `https://www.graham.az.gov/418/Septic-Wastewater` | wall |
| La Paz | Ord. 2026-01 `https://www.co.la-paz.az.us/DocumentCenter/View/9776` | ★ `https://www.co.la-paz.az.us/590/SANITATION-SEPTIC`; setback table `https://www.lapaz.gov/DocumentCenter/View/6687/Setback-Table-for-Onsite-Wastewater-System`; well waiver `https://www.co.la-paz.az.us/DocumentCenter/View/8684` | 200 |
| Yuma | `https://www.yumacountyaz.gov/government/development-services/laws-guidelines/building-safety-code-amendments` | (Environmental Programs) | wall |
| Apache, Santa Cruz | county sites Cloudflare-walled; archived copies of county PDFs used (§ 3.1) | — | wall |

### Cities (code pages read; owner-builder forms where named)

| City | URL | Status |
|---|---|---|
| Phoenix | `https://www.phoenix.gov/administration/departments/pdd/tools-resources/codes-ordinance/building-code.html` | 200 |
| Tucson (Owner/Builder Affidavit on the Residential Permits page) | `https://www.tucsonaz.gov/Departments/Planning-Development-Services/Codes/Building-Codes` | wall |
| Scottsdale | `https://www.scottsdaleaz.gov/codes-and-ordinances/building-codes` | 200 |
| Chandler | `https://www.chandleraz.gov/government/departments/development-services/building-safety-plan-review-permits-and-inspections` | 200 |
| Glendale | `https://www.glendaleaz.gov/Business/Building-Safety-Codes-Services/Building-Codes` | wall |
| Tempe | `https://www.tempe.gov/government/community-development/building-safety/building-codes-and-amendments` | wall |
| Flagstaff | `https://www.flagstaff.az.gov/5142/Building-Code` | 200 |
| Lake Havasu City (Owner/Builder Certification) | `https://www.lhcaz.gov/593/Codes`; `https://www.lhcaz.gov/DocumentCenter/View/1163/Owner---Builder-Certification-PDF` | 200 |
| Goodyear homeowner FAQ | `https://www.goodyearaz.gov/government/departments/engineering-development-services/development-services/homeowner-permit-faqs` | wall |

**Not printed**: Arizona 811 (DNS timed out twice on 8 September 2026 — verify
before printing); Industrial Commission of Arizona home page (403 to curl,
not read this pass).

---

## 12. LIVE GUIDE AUDIT — `src/app/permitting/state-guides/arizona/page.mdx`

Read in full (567 lines) on 3 September 2026. Line numbers are from `cat -n`.
The guide is better than most in the corpus on the exemption itself (it
already says "offering," "prima facie," and cites (A)(5) and (A)(6)); its
errors cluster in three places — the "no-permit counties" claim, the
unsourced dollar and day tables, and "varies locally" hedges on rules that
are statewide. No in-page anchors are proposed (the MDX pipeline has no
heading ids).

### 12.1 Wrong

| Line | Guide text (quoted) | Correction | Cite |
|---|---|---|---|
| 32 | "Building permit — Varies — Required in code jurisdictions; some rural unincorporated areas have no codes or permits" | A county building permit is mandatory statewide for construction over $1,000. What varies is whether the permit carries a building *code*. Greenlee County has no code and still issues the permit. | § 11-321(A); § 11-815(B); Greenlee County Engineer letter (§ 1.6) |
| 106 | "Arizona's contractor statutes do not impose a single statewide 'owner-builder declaration' form the way California does. Some local building departments require their own owner-builder affidavit" | Every permit application in Arizona must carry a signed statement of the licensing exemption claimed, naming every licensed general, mechanical, electrical and plumbing contractor to be used; a false one is unsworn falsification. The *form* is local; the *content* is statutory. | § 32-1169(A), (B); § 13-2704 |
| 152 | "Rural Counties (Cochise, Graham, La Paz) … (some counties require no permits in unincorporated areas)" | No county may waive the permit. Graham's own FAQ: "'dirt work' does not require a permit, everything else does." | § 11-321(A); Graham County FAQ |
| 59 | "Maricopa County (unincorporated), Tucson, Mesa, Flagstaff — Generally still on the 2018 I-Codes as of early 2026" | Tucson: 2024 IRC/2023 NEC effective 1 Jan 2026 (IECC 1 Jul 2026). Mesa: 2024 IRC/2023 NEC effective 8 Jan 2026. Maricopa County and Flagstaff remain on 2018. | Tucson Building Codes page; Mesa Ords. 5981/5982 (§ 3.2) |
| 60 | "Rural / unincorporated areas — Minimal codes, or none at all in some counties" | One county (Greenlee) has none; the rest run from the 2003 IRC (Graham) to the 2024 IRC (Pima, Yavapai, Coconino, Yuma, Cochise from 1 Sep 2026). | § 3.1 |
| 412 | "Pinal County … Some areas have no building codes" | Pinal's code applies "within the unincorporated areas of Pinal County, except as otherwise provided by statute." | PCDSC 6.05.020 (§ 3.1) |
| 424 | "Mohave County … Minimal regulations in many areas" | The Mohave County Building Safety Code applies to all unincorporated areas since Resolution 2007-249; the old partial "building overlay" survives only as an amnesty for pre-2008 structures. | Mohave Ord. 2021-03 § 1B, § 3G |
| 417 | "Cochise County … Minimal permitting in unincorporated areas" | Cochise runs a full 2024-code program; the Owner-Builder Amendment is an opt-out from plan review/inspections limited to parcels ≥ 4 acres in ≥ 4-acre zoning, once per five years, with a notice recorded against title and no CO on Option 2. | Cochise OBA Secs. 1, 2, 5, 6, 16 (§ 1.5) |
| 421 | "Lake Havard" | Lake Havasu City. | — |
| 123, 127 | "Workers' comp is not required for casual labor" | The exclusion requires employment that is *both* casual *and* "not in the usual course of the trade, business or occupation of the employer"; no statute exempts a homeowner by name. | § 23-901(6)(b); § 23-902(A) |
| 464 | "Q: Can I build without permits in Arizona? A: In some rural unincorporated areas, yes." | No. See line 32. | § 11-321(A) |
| 546 | "In some rural unincorporated counties there may be no building codes or permits required" | "no building codes" is true of one county; "or permits" is false everywhere. | § 11-321(A) |
| 459 | "County Health Departments: Septic permits (varies by county)" | The delegated agency is Development/Community Development Services in Pima, Pinal, Yavapai, Mohave, Coconino, Navajo, Gila, La Paz and Yuma; a health department in Maricopa (Environmental Services), Apache, Graham, Greenlee and Santa Cruz. | § 49-107; county pages (§ 3.1) |
| 450–452 | "(602) 542-1525 or (877) 692-9762" | Phone numbers — house rule. Delete. | — |
| 47 | "The main statewide exception is fire: Arizona has adopted a statewide edition of the International Fire Code through the State Fire Marshal" | The state fire code's exit and inspection provisions exclude "family dwellings that have fewer than five residential dwelling units," and enforcement is ceded to cities ≥ 100,000 with their own code; a house's fire rules come from the fire district's or county's adopted code. The real statewide exceptions are septic, wells, pool barriers, plumbing fixtures and the sprinkler-mandate ban. No edition should be named without the DFFM rule in hand. | § 37-1383(A)(2)(e), (5), (8); § 11-861(B); § 2.2 |

### 12.2 Hedges on rules that are statewide

| Line | Guide text | What is actually statewide | Cite |
|---|---|---|---|
| 18, 28–29, 108, 112, 534 | "the allowed scope varies by jurisdiction"; "Often yes … scope varies by jurisdiction — verify locally"; "(some cities limit homeowner electrical permits to specific tasks)" | The ROC chapter does not reach an owner improving the owner's own property at all; the statewide limit is that the house be "intended for occupancy solely by the owner" and not for sale or rent, which every AHJ site read applies as "no rentals." No city site read limits homeowner electrical permits "to specific tasks." | § 32-1101(A)(10)(b), (B); § 32-1121(A)(5); Chandler/Tucson/Goodyear pages (§ 3.6) |
| 18, 30, 100, 538 | one-year rule stated as a flat rule | Add: the presumption is expressly inapplicable "in an action against an owner-occupant as defined in section 33-1002" (recorded deed before construction + 30 days' residence in the following year), and "rent" includes compensation in "labor." | § 32-1121(A)(5); § 33-1002(A)(2) |
| 185–189 | "Counties 10–20 business days … Rural/No Code Areas: No review required" | Cities: posted time frames, one comprehensive request for corrections, 15-working-day denial notice, automatic fee refund, no mid-build changes (§ 9-835); 15 working days to third-party review in cities ≥ 30,000 (§ 9-470.01). Counties: **none of it** — residential-lot licences are carved out of § 11-1605 by subsection (M)(2); the only county clock is "at the earliest reasonable time" for inspections. | § 9-835(G), (K), (N); § 9-470.01; § 11-1605(M)(2); § 11-863(B) |
| 195 | "6–12 months without inspection (varies by jurisdiction)" | Unsourced; the only verified figure is Cochise's 36 months plus one 12-month extension. Delete the numbers. | Cochise OBA Sec. 12 |
| 396, 378 | "Rural/No Code Areas: No inspections required" | Building inspections, yes; Cochise's own page: "Zoning, floodplain, septic, well, and other non-building inspections remain required." | Cochise Owner Builder Amendment page |

### 12.3 Unsupported figures and generic content (delete or label)

| Lines | Content | Problem |
|---|---|---|
| 139–154 | Permit/plan-review dollar table by jurisdiction | No source; no state schedule exists (§ 11-863(C); § 9-467(G)). Greenlee: "at no cost." |
| 158–170 | "Well permit $100–$500"; "Septic permit $500–$1,200"; impact/tap fees | ADWR's notice fee is fixed by statute: $150, or $100 for a domestic ≤ 35 gpm well outside an AMA/INA (§ 45-596(L)); county site-plan approval fees are separate (La Paz: $100). Septic fees are county-set. Others unsourced. |
| 206–221 | "Typical Insulation Minimums (Zone 2B)" R-value table; "Air sealing 5 ACH" | No jurisdiction verified to these values; Maricopa County's energy chapter is voluntary; Gila's ordinance table differs; Prescott/Yavapai/Cochise use 2012 IECC, Yuma 2009, Sierra Vista 2006. Climate-zone map not verified here. Delete. |
| 226 | "Duct testing required in most jurisdictions" | Unsupported. |
| 70–76 | "Termite Protection: Required in most areas"; "Water Conservation: Landscape and plumbing requirements" | Unsourced. The verifiable statewide water rule is the fixture statute (§ 45-312); landscape rules are local. |
| 255–263, 280, 304, 313, 328, 341, 358–359, 372, 471, 494 | Every cost, savings and duration figure | Unsourced. |
| 325 | "Defensible space (30–100 feet clearance)" | WUI codes are optional per jurisdiction (§ 9-806; § 11-861(D)); no statewide distance. |
| 401–431 | County population figures | Unsourced; not needed. |
| 358 | "timeline: 4–8 weeks" (septic) | ADEQ's own posted clock for a 4.02 permit is 73 business days; delegated counties set their own. |

### 12.4 Material omissions (add)

1. **§ 32-1169** signed exemption statement on every permit application;
   naming licensed subs; ROC-signed verification on request; criminal
   penalty for a false statement.
2. **§ 11-321(A)** — permit mandatory everywhere; **Greenlee** no code;
   **Cochise** four-acre opt-out with recorded notice and no CO on Option 2;
   **Coconino** AMMP (≤ 600 sq ft).
3. **§ 9-835 / § 9-470.01 city clocks and the § 11-1605(M)(2) county
   carve-out**; the **§ 9-839 / § 11-1609 clarification letter** (30 days).
4. **§ 33-1002 owner-occupant lien shield** (record the deed first; no lien
   without a direct written contract) and **§ 33-992.01** 20-day notices.
5. **§ 32-1158** contract contents; **§ 32-1162(A)** two-year complaint
   window from occupancy; **§ 32-1132** recovery-fund eligibility for an
   occupying owner.
6. **§ 9-807 / § 11-861(E)** — no sprinkler mandate; **§ 36-1681** pool
   barrier; **§ 45-312** fixtures; **§ 9-467/§ 11-321** utility choice and
   no business-licence condition; **§ 28-8482** military-airport R-18/R-30
   rule; **§ 9-468/§ 11-323** solar permit limits; **§ 33-439** solar
   covenants void.
7. **Septic specifics**: 100-ft well setback and 50-ft property-line rule
   with the recorded neighbour waiver (R18-9-A312(C)); 100% reserve area;
   tank/flow table by bedrooms *and fixture count* (R18-9-A314); Construction
   Authorization two-year life (R18-9-A301(D)); site investigator must be a
   PE/geologist/sanitarian/certified (R18-9-A310(H)); transfer-of-ownership
   inspection within six months before sale (R18-9-A316).
8. **Well specifics**: exempt well ≤ 35 gpm; notice of intent; **owner may
   drill their own exempt well with a no-fee single well licence after an
   exam** (§ 45-595(D); R12-15-807); domestic site plan on ≤ 5 acres with
   county health sign-off (§ 45-596(F)); the **100-ft municipal-provider
   ban** in older AMAs (§ 45-454(C)); 100 ft from septic (R12-15-818);
   owner's completion report 30 days after the pump goes in (§ 45-600(B)).
9. **Phoenix's HVAC-GFCI enforcement deferral to 1 March 2027** and the
   2026 code rollovers (Coconino 2 Jun, La Paz 6 Aug, Cochise 1 Sep, Tempe
   1 Jul, Goodyear 23 Jun).
10. **Maricopa County's energy code is voluntary** — the largest county by
    population has no mandatory residential energy code in unincorporated
    areas.
