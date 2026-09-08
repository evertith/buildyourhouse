# New York Owner-Builder Permit Kit — Research Dossier

Kit 23 of the 50-state program. Compiled September 2026 for
`binder-pipeline/kits/ny-permit-kit/` (NY.0–NY.5).

**Scope.** New York State **outside New York City**. See § 0 for the
statutory basis of the exclusion.

**Marking convention.** `[V]` = read in a primary source and quoted here.
`[H]` = secondary, inferred, or reasoned — not printed in the kit as a
citation. Anything unverifiable was deleted rather than softened.

**Primary sources used.**

| Source | What it is | Where |
|---|---|---|
| Executive Law Art. 18, §§ 371, 372, 377, 378, 379, 380, 381, 382, 383 | Uniform Fire Prevention and Building Code Act | nysenate.gov/legislation/laws/EXC/A18 |
| Executive Law Art. 27, §§ 806, 809, 810 | Adirondack Park Agency Act (shoreline, permits, class A/B projects) | nysenate.gov/legislation/laws/EXC/806 etc. |
| 19 NYCRR Part 1202 (rule text, adopted 13 Dec 2022) | DOS enforcement in place of a local government | dos.ny.gov PDF `2022-12-2-rule-text-part-1202.pdf` |
| 19 NYCRR Part 1203 (rule text, adopted 29 Dec 2021, eff. 30 Dec 2022) | Minimum standards for administration and enforcement | dos.ny.gov PDF `2021-12-10-full-text-of-rule-part-1203.pdf` |
| 19 NYCRR Part 1205 (rule text 2023; § 1205.5(a) amended 2025) | Variance and appeals procedures | dos.ny.gov `2023-6-8-rule-text-part-1205`; `rule-text-part-1205-…` |
| 19 NYCRR Parts 1219–1229 (rule text, adopted 5 Dec 2025, eff. 31 Dec 2025) | The 2025 Uniform Code adoption, incl. Subpart 1229-2 | dos.ny.gov `rule-text-uniform-code-0` (PDF) |
| 19 NYCRR Part 1240 (rule text, adopted 5 Dec 2025) | 2025 Energy Code adoption, incl. § 1240.6 | dos.ny.gov `rule-text-part-1240-energy-code` (PDF) |
| 2025 Residential Code of New York State, Ch. 1, 3, 26, 34 | The adopted book (ICC free viewer) | codes.iccsafe.org/content/NYSRC2025P1 |
| 2025 ECCCNYS, Ch. 3 [RE], 4 [RE] | Residential energy provisions | codes.iccsafe.org/content/NYSECC2025P1 |
| DOS Code Outreach Program 2026-1; DOS "Administration and Enforcement of the Uniform Code" (rev. 2026); DOS Notice of Adoption page; DOS FAQ; Model Local Law; LG03; LG07; More Restrictive Standards bulletin 2021 | Division of Building Standards and Codes' own publications | dos.ny.gov |
| 10 NYCRR § 75.5; Appendix 75-A (eff. 16 Mar 2016) | Residential onsite wastewater | health.ny.gov / regs.health.ny.gov |
| 10 NYCRR Appendix 5-B (eff. 23 Nov 2005); DOH Fact Sheet #6 | Water well standards; CEO guidance | health.ny.gov |
| 10 NYCRR § 128-3.8 | NYC watershed septic rule | regs.health.ny.gov |
| General Municipal Law § 125; Workers' Compensation Law §§ 56, 57 | Building-permit workers' comp gate | nysenate.gov |
| WCB permit-requirements sheet; CE-200 overview page; CE-200 instructions | Board's own forms guidance | wcb.ny.gov |
| Education Law §§ 7209, 7306, 7307 | Stamped-plan exemptions | nysenate.gov |
| ECL §§ 15-1525, 15-1527 | Well driller registration; Long Island well permits | nysenate.gov |
| General Business Law §§ 770, 771; Lien Law § 71-a; Labor Law § 240 | Custom-home contract terms; escrow; scaffold law | nysenate.gov (structured reads) |
| Suffolk County Code § 563-16; Nassau Admin. Code § 21-11.1; Putnam County Code Ch. 135; Westchester § 863.312 | County home-improvement licensing | county-hosted PDFs |
| *Mulhern Gas Co. v. Mosley*, N.D.N.Y. Dkt. 75 (Stipulation and Order, 18 Nov 2025); 2d Cir. 25-2041 docket and 30 Jun 2026 opinion | All-electric suspension and clock | storage.courtlistener.com; courtlistener.com |

> **Fetching note for future revisions.** `nysenate.gov` and `dos.ny.gov`
> sit behind a **Cloudflare managed challenge that returns HTTP 403 to curl
> with any User-Agent**. What works: (1) the Chrome browser tools for
> nysenate.gov statute pages (`get_page_text` returns the full section
> verbatim) and for `codes.iccsafe.org` code-book chapters (use a JS
> `innerText` slice for anything past 50 KB — Chapter 3 of the RCNYS is
> 268 KB); (2) **WebFetch on a dos.ny.gov PDF URL saves the binary to the
> tool-results directory even though its summarizer cannot read it** — copy
> it out and run `pdftotext -layout`. That is how every 19 NYCRR rule text
> here was read. `health.ny.gov`, `regs.health.ny.gov`, `wcb.ny.gov`,
> `govt.westlaw.com`, `storage.courtlistener.com` and county PDF hosts all
> answer a plain curl. `ecode360.com` and `library.municode.com` block
> everything (curl, WebFetch and the browser's domain allow-list). Westlaw's
> NYCRR was **nine months stale** for Parts 1219–1229 in September 2026 —
> read the DOS rule-text PDFs instead. DOS's own document host is sometimes
> `yi.dos.ny.gov`.

---

## 0. THE HEADLINE — WHAT MAKES THIS KIT DIFFERENT

New York looks like Pennsylvania — one statewide code, local enforcement, no
state contractor license — and then diverges on every page. The permit is
gated by a **workers' compensation form**, not a license; the electrical
inspector is **whoever the town has approved**, not the building department;
the energy numbers are **New York's own** and stricter than the model code;
and the gas question has a **court-set clock** that runs out at the end of
this year.

Seven findings carry the kit:

1. **One code, three possible permit offices.** `[V]` Executive Law § 381(2)
   sends enforcement town → county → Department of State; the code itself
   never lapses (§§ 371(2)(c), 379(3), 383(1)). No town is code-free, and the
   first question is *which tier issues my permit*.
2. **The permit gate is General Municipal Law § 125.** `[V]` No town may
   issue a building permit without carrier proof of workers' comp and
   disability coverage (C-105.2 + DB-120.1 — "ACORD forms are not
   acceptable") **or** an affidavit of no employees — the job-specific
   **Form CE-200** "Apply as a Homeowner." Nobody else's owner-builder page
   mentions it.
3. **Electrical is a "special inspection" the AHJ must pre-approve.** `[V]`
   19 NYCRR § 1203.2(e)(4). The building official signs the CO only on a
   "final report of special inspections." There is no state list of
   agencies. And **[NY] E3401.2.1** lets an owner-occupied one-family
   dwelling have **no electrical system at all**.
4. **The all-electric prohibition is suspended by a stipulation whose clock
   started 2 September 2026.** `[V]` Mandate issued that day; 120 days =
   **31 December 2026** unless a certiorari petition (due ~24 November 2026)
   extends it. The trigger is the *substantially complete application*
   date, not the CO date (§ 1229-2.4).
5. **The energy tables are New York's, not the IECC's.** `[V]` Ceiling R-49
   (not R-60), windows U-0.27 (not 0.30), walls R-30 or 20&5ci, and
   **2.5 ACH50 in Zone 6** (3.0 in Zones 4–5). Ulster, Sullivan and Delaware
   are Zone 6.
6. **Stamped plans above 1,500 sq ft gross** — statewide, by Education Law
   §§ 7307(5) and 7209(7)(b), carried into the code by [NY] R106.6. `[V]`
7. **Radon is informational only, tiny houses are adopted, sprinklers start
   at three stories.** `[V]` 2025 RCNYS [NY] R101.2.1 and [NY] R309.2.

And one that cuts the other way: **an owner can appeal a code official to a
DOS regional board of review, decided in 60 days** (19 NYCRR § 1205.3(a)(2),
§ 1205.4(e)) — the statutory forum Pennsylvania's opt-out towns lack.

---

## 1. THE CENTRAL THESIS — WHO ENFORCES

### 1.1 One code, everywhere `[V]`

Executive Law § 371(2)(c): it is state policy to "Insure that the uniform
code be in full force and effect in every area of the state." § 383(1): the
article and the Uniform Code "shall supersede any other provision of a
general, special or local law, ordinance, administrative code, rule or
regulation inconsistent or in conflict therewith."

§ 379(3): "no municipality shall have the power to supersede, void, repeal or
make more or less restrictive any provisions of this article or of rules or
regulations made pursuant hereto." A municipality may adopt **more
restrictive** construction standards only by petitioning the State Fire
Prevention and Building Code Council, which must affirmatively approve them
(§ 379(1)–(2)); Nassau County has its own version of that power (§ 379(5)).
Zoning and other matters "as to which the uniform fire prevention and
building code does not provide" remain local (§ 379(3)).

**Consequence for the kit:** setbacks, lot coverage, height, driveway and
parkland fees are local; *construction* rules are not, except for
Council-approved more-restrictive local standards (DOS keeps a list — see
§ 11).

### 1.2 The NYC exclusion — statutory basis `[V]` — § 383(1)(c)

"[I]n cities with a population of over one million, the existing building and
fire prevention codes shall continue in full force and effect beyond January
one, nineteen hundred eighty-four unless the council … shall determine that
said local code provisions are less stringent than the uniform code." New
York City is the only such city. **Everything in this dossier is New York
State outside the five boroughs.** The kit says so once, in NY.0, citing
§ 383(1)(c), and does not attempt NYC.

### 1.3 Who administers — § 381(2), verbatim `[V]`

> "Except as may be provided in regulations of the secretary pursuant to
> subdivision one of this section, **every local government shall administer
> and enforce** the uniform fire prevention and building code and the state
> energy conservation construction code on and after the first day of
> January, nineteen hundred eighty-four, provided, however, that a local
> government may enact a local law prior to the first day of July in any year
> providing that it will not enforce such codes on and after the first day of
> January next succeeding. In such event **the county** in which said local
> government is situated shall administer and enforce such codes within such
> local government … unless the county shall have enacted a local law
> providing that it will not enforce such codes within that county. In such
> event **the secretary** in the place and stead of the local government
> shall, directly or by contract, administer and enforce the uniform code and
> the state energy conservation construction code. … Two or more local
> governments may provide for joint administration and enforcement … by
> agreement pursuant to article five-G of the general municipal law. Any local
> government may enter into agreement with the county … Local governments or
> counties may charge fees to defray the costs of administration and
> enforcement."

"Local government" is defined at § 372(11) as "a village, town (outside the
area of any incorporated village) or city." **A county is not a local
government under Article 18** — it is the first fallback.

So the three-tier ladder is statutory: **town/village/city → county → the
Department of State.** The word "opt out" appears nowhere in the statute; the
mechanism is a local law enacted before 1 July that the municipality "will
not enforce such codes" from the following 1 January. The code itself never
goes away (§§ 371(2)(c), 383(1)).

### 1.4 What happens in a state-enforced municipality `[V]` — 19 NYCRR Part 1202

Part 1202 (repealed and re-added, adopted 13 December 2022, effective 30
December 2022) is the procedure "in the circumstances in which the Secretary
of State, through the Department of State (the department), will administer
and enforce the Uniform Code and Energy Code in the place and stead of a
local government or county" (§ 1202.1(a)).

- § 1202.3(a): "No person shall commence any work for which a building permit
  is required without first having obtained a building permit **from the
  department**."
- § 1202.3(c): the application "shall be signed by the owner of the building
  or structure **and the owner of the real property**, if different."
- § 1202.3(c)(7): the application must include "the climatic and geographic
  design criteria as indicated in section 1202.12 of this Part."
- § 1202.1(c): DOS may contract inspections to a third party, and "the owner
  shall pay the associated fee prescribed by this Part, including but not
  limited to the fee associated with the third-party services."
- § 381(5)(a): once the county or the Secretary has taken over, the local
  government "shall not administer and enforce the uniform code, and shall
  not charge or collect fees."

**The kit's operating instruction:** the reader must first learn *which
tier* issues their permit. DOS is the AHJ in a small set of municipalities;
the county in others (and several counties run enforcement for many towns by
agreement). The verification step is to ask the town clerk whether the town
has a code enforcement program under Part 1203, and if not, whether the county
or DOS is the AHJ. *The list of state-enforced municipalities was not
retrievable in this session — see § 8.*

### 1.5 The minimum-standards floor `[V]` — § 381(1)

The Secretary "shall promulgate rules and regulations prescribing minimum
standards for administration and enforcement," which "shall address … (a)
frequency of mandatory inspections … (b) number and qualifications of staff,
including requirements that inspectors be certified … (c) required minimum
fees … (f) establishment of a procedure whereby any provision or requirement
of the uniform code may be varied or modified … Requests for a variance shall
be resolved within **sixty days** of the date of application unless a longer
period is required for good cause shown." Those rules are 19 NYCRR Part 1203
(§ 4 of this dossier) and Part 1205 (variances).

**Owner-occupied houses are not subject to periodic inspection** — § 381(1),
closing paragraph: "Nothing in the rules shall require or be construed to
require regular, periodic inspections of (A) owner-occupied one and
two-family dwellings … provided, however that this shall not be a limitation
on inspections conducted at the invitation of the owner or where conditions
on the premises threaten or present a hazard."

### 1.6 State supervision of the local program `[V]` — § 381(3)–(5)

If a local government fails to meet the minimum standards the Secretary may
order compliance, ask the Attorney General to sue, designate the county, or
take over directly (§ 381(4)). During a takeover the local government may not
charge fees (§ 381(5)(a)). This is the enforcement teeth behind Part 1203; it
also means a town that runs a sloppy program can lose it.

### 1.7 Remedies and penalties `[V]` — § 382

Every local government may "order in writing the remedying of any condition
… in violation of the uniform fire prevention and building code and … issue
appearance tickets" (§ 382(1)). A person who fails to comply with an order to
remedy, or "any owner, builder, architect, tenant, contractor, subcontractor,
construction superintendent or their agents or any other person taking part
or assisting in the construction of any building who shall knowingly violate"
the Uniform Code, "shall be punishable by a fine of not more than one thousand
dollars per day of violation, or imprisonment not exceeding one year, or
both" for the first 180 days, with escalating minimums thereafter (§ 382(2)).
A court "may order the removal of the building or an abatement of the
condition" (§ 382(3)).

**Kit note:** the owner-builder is expressly named in § 382(2) ("any owner,
builder"). There is no lesser penalty tier for a homeowner.

### 1.8 Appeals — the local law, not the statute `[H]`

Neither Article 18 nor Part 1203 requires a local board of appeals for code
official decisions (verified absence in both texts). Variances from the
Uniform Code itself go to DOS under Part 1205 (§ 381(1)(f), 60-day clock).
Whether a *local* appeal exists depends on the municipality's code
enforcement local law — the DOS model local law includes one, but a town may
have amended it. The kit tells the reader to check the local law.

---

## 2. SCOPE — WHAT IS OUTSIDE THE CODE

### 2.1 What "building" and "construction" mean `[V]` — § 372(3), (4)

"Building" is "a combination of any materials, whether portable or fixed,
having a roof, to form a structure affording shelter for persons, animals or
property," and includes factory manufactured homes and mobile homes; it
excludes a "temporary greenhouse" (§ 372(3), (17)). "Construction" includes
"the construction, reconstruction, alteration, conversion, repair,
installation of equipment or use of buildings" (§ 372(4)). "Equipment"
expressly includes "plumbing, heating, electrical, ventilating, air
conditioning, refrigerating equipment" (§ 372(7)). **Electrical work is
inside the Uniform Code by statutory definition.**

### 2.2 Which book applies to a house `[V]` — 19 NYCRR § 1220.2(a)

The 2025 RCNYS governs "detached one-family dwellings that are not more than
three stories above grade plane in height, and their accessory structures
that are not more than three stories above grade plane in height"; detached
two-family dwellings with separate egress; townhouses; bed-and-breakfast
dwellings; certain live/work units; and owner-occupied lodging houses with
five or fewer guestrooms and a P2904 sprinkler system. § 1220.2(d): an
applicant may elect the 2025 BCNYS instead, provided the whole building
complies with it.

"Story above grade plane" is defined in § 1219.2(a)(18) — a story whose
finished floor is entirely above grade plane, *or* whose ceiling is more than
6 ft above grade plane, more than 6 ft above finished ground for more than
50 % of the perimeter, or more than 12 ft above finished ground at any point.
A walk-out basement can count as a story.

### 2.3 Permit-exempt work is a local option, not a statewide list `[V]`

See § 4.2. Part 1203 lets the AHJ exempt eight categories (sheds ≤ 144 sq ft,
awnings, finish work, listed portable appliances, like-for-like equipment
replacement, non-structural repairs). Where DOS is the AHJ, Part 1202.3(b)
makes those same eight categories exempt outright. **There is no statewide
"no permit under X square feet" rule that binds a municipality.**

### 2.4 Agricultural buildings `[V]`

Defined in § 1219.2(a)(10) as a structure "to house farm equipment, farm
implements, poultry, livestock, hay, grain, or other horticultural products"
that "shall not be a place of human habitation." § 381(1) exempts
agricultural buildings from periodic inspection. Subpart 1229-2.5(a)(2)
exempts them from the fossil-fuel prohibition. There is **no** blanket
building-permit exemption for agricultural buildings in Part 1203 (verified
absence) — the RCNYS/BCNYS content that applies to them is a code-book
question the kit does not need.

### 2.5 No owner-builder exemption exists — because there is nothing to be exempt from `[V]`

Searched Executive Law Article 18, Part 1202 and Part 1203: no provision
treats a dwelling built by its owner differently from one built by a
contractor. New York has no state general contractor license (§ 5.1). The
DOS FAQ says, verbatim: "Issues regarding local laws, zoning, and licensing
of contractors or electricians are not handled by this Division."

What New York *does* have, and what every other state's owner-builder page
misses, is a **permit gate that is about employees, not licenses**: General
Municipal Law § 125 and Workers' Compensation Law § 57 (§ 5.2). That is the
New York equivalent of the exemption affidavit — it is filed on Form CE-200,
and the kit's NY.1 walks the reader through it.

### 2.6 The manufactured-home exception `[V]`

Executive Law § 379(1) and § 383(1)(c) both carve factory manufactured homes
out of local more-restrictive standards and out of the NYC carve-out. 19 NYCRR
Part 1210 governs manufactured-home installers; the DOS FAQ: "A person who
intends to own and occupy a manufactured home may apply for certification as
the installer of such manufactured home," and any homeowner-completed
component "shall be supervised and certified by an installer holding
certification issued pursuant to part 1210." Not a site-built house; noted so
NY.1 can send a manufactured-home buyer elsewhere.

---

## 3. CODE EDITIONS AND AMENDMENTS

### 3.1 Editions in force `[V]` — 2025 codes, effective 31 December 2025

DOS Notice of Adoption page (retrieved September 2026):

- **Amended Notice of Adoption – Rule Amending and Updating the Uniform
  Code**, 19 NYCRR Parts 1219–1229, adopted 5 December 2025, **effective
  31 December 2025**; rule text at `dos.ny.gov/rule-text-uniform-code-0`.
- **Amended Notice of Adoption – Rule Amending and Updating the Energy
  Code**, 19 NYCRR Part 1240, adopted 5 December 2025, **effective
  31 December 2025**; rule text at `dos.ny.gov/rule-text-part-1240-energy-code`.

The adopted rule text (PDF, "RULE TEXT (Uniform Code)") repeals Parts
1219–1229 and re-adds them. § 1219.2(a) defines the eight books, each
"(publication date: July 2025), published by the International Code Council,
Inc.": 2025 BCNYS, EBCNYS, FCNYS, FGCNYS, MCNYS, PCNYS, PMCNYS, **2025 RCNYS**.
DOS's own Code Outreach Program issue 2026-1 (3 February 2026): "NYS
specific code books which are based on the **2024 International Code
Council books** with New York modifications."

**Transition rule** `[V]`: DOS Notice of Adoption page: for the Uniform
Code, "a person shall have the option of complying with either the provisions
of the 2025 Uniform Code or the 2020 Uniform Code" during the period between
adoption and 31 December 2025; for the Energy Code, "There is no the
transition period" [sic]. The option period is now closed. Statutory basis:
Executive Law § 378(20)(b). The 2025 RCNYS itself, [NY] R102.6: "the
'effective date of this code' shall be deemed to be **December 31, 2025**."

**Which code applies to a permit applied for before 31 December 2025?**
*Not stated in any primary source read.* Neither Part 1203 nor the Notice
of Adoption carries a "permit applied for before X keeps the old code" rule
(verified absence). The only trigger language in the 2025 rules is the
fossil-fuel Subpart's "substantially complete building permit application
… submitted on or after December 31, 2025" (§ 1229-2.4(a)). The kit does not
print a grandfathering rule; a reader with a 2025 application in review must
ask the AHJ which edition it is reviewing against.

### 3.2 The code is the regulation, not the book `[V]`

DOS 2026-1, verbatim: "A common misconception among code users is that the
code is found solely in the 'code books.' The Uniform Code is contained in
state regulations, 19 NYCRR Parts 1219 through 1229, and the publications
incorporated by reference into those Parts … there are parts of the code
that are contained solely in the regulations. … The regulations must be
examined prior to reviewing the publications incorporated by reference."

The RCNYS's own [NY] R101.1.1 says the same. The kit therefore cites
**19 NYCRR § 1220.2** as the adoption and the 2025 RCNYS section for content.

> **⚠ Westlaw's NYCRR is stale.** `govt.westlaw.com/nycrr` Part 1220 still
> listed "s 1220.3 Changes to the text of the **2020** RCNYS" in September
> 2026, nine months after the 2025 rule took effect. Do not "verify" against
> Westlaw for Parts 1219–1229 or 1240 — use the DOS rule-text PDFs. `[V]`

### 3.3 New York's changes to the 2025 RCNYS — the regulatory list `[V]` — § 1220.2(e)

Short, and almost entirely bibliographic:

1. Chapter 2 definition of **permit** replaced: "[NY] PERMIT. An official
   document or certificate issued by the authority having jurisdiction that
   authorizes performance of a specified activity."
2. Chapter 44 referenced-standards corrections — ACI 318-19(22), ACI 332-20,
   AISI S230-19, **NDS-2024 with 2024 Supplement**, FEMA TB-2 and TB-11
   reverted to the **2008 and 2001** editions, MSS SP-58 reverted to 2018,
   pool standards with Addendum A, ASHRAE 34-2022 title fix; the federal
   pool-drain standard citation removed.
3. Appendix BA § BA113.3 relocated manufactured homes rewritten.
4. Appendix BO § BO103.1: a mislabeled definition replaced with "[NY]
   LOAD-BEARING ELEMENT."

Everything else "New York" is inside the book, marked **[NY]** section by
section. The kit's rule: **any RCNYS section printed with a [NY] tag is a
New York amendment; cite it as "2025 RCNYS § R___ [NY]".**

### 3.4 Chapter 1 of the 2025 RCNYS is entirely New York `[V]`

Every section of Chapter 1 carries the [NY] tag. Points the kit uses:

- **[NY] R101.2.1 Appendices**: adopted — "Appendix BA Manufactured Housing
  Used as Dwellings; Appendix BB Tiny Houses; Appendix BF Patio Covers;
  Appendix BO Existing Buildings and Structures." Then: "the following
  appendices are included **for informational purposes**: **Appendix BE
  Radon Control Methods**, BG Sound Transmission, BH Automatic Vehicular
  Gates, BI Light Straw-Clay, BJ Strawbale, BK Cob, BL Hemp-Lime, BM
  3D-Printing, BN Extended Wall Plate, CA–CG (gas piping, venting, water
  piping, nonsewered sanitation)."
  **Consequence: radon-resistant construction is NOT required by the
  Uniform Code.** A municipality could only require it via an Executive Law
  § 379 more-restrictive standard approved by the Code Council. **Appendix BB
  Tiny Houses IS adopted** — a genuine statewide path the guide never
  mentions. Strawbale/cob/hempcrete are informational only, so they run
  through R104.2.2 alternative-methods approval.
- **[NY] R104.2.2**: alternatives must be approved "in writing" by the
  building official; "Nothing in this code shall be construed as permitting
  any building official or any authority having jurisdiction to **waive,
  vary, modify, or otherwise alter** any provision … of the Uniform Code."
  The local official cannot grant a variance — only DOS under Part 1205.
- **[NY] R105.2**: exemptions exist only where "excluded from the permit
  requirement by the authority having jurisdiction's Code Enforcement
  Program, provided that Part 1203 allows" it. (Mirrors § 4.2.)
- **[NY] R106.1**: the AHJ "may waive the requirement for construction
  documents where a registered design professional is not required by law
  and where either the work to be done involves minor alterations or
  repairs, or where plans and specifications are determined by the
  authority having jurisdiction to not be necessary."
- **[NY] R106.2 Site plan**: "a site plan showing the size and location of
  new construction and existing structures on the site and distances from
  lot lines."
- **[NY] R106.6 Design professional**: "Construction documents shall be
  prepared by a registered design professional **when required by Article
  145 or Article 147 of the New York State Education Law**, by the stricter
  of Code Enforcement Program of the authority having jurisdiction or a Part
  1203—Compliant Code Enforcement Program, or by any other applicable law."
  → the 1,500 sq ft rule, § 5.4.
- **[NY] R109.1**: work stays "accessible and exposed until … inspected and
  accepted"; **[NY] R109.3**: the permit holder must notify when ready.
- **[NY] R110.1**: no occupancy without a CO where the local program requires
  one.
- **[NY] R112.1**: "An application for a variance or modification of any
  provision or requirement of Uniform Code shall be in accordance with the
  provisions of Part 1205. **An appeal of any order or determination, or the
  failure within a reasonable time to make an order or determination, of an
  administrative official** charged to enforce or purporting to enforce the
  Uniform Code may be made in accordance with the provisions of Part 1205."
  → see § 10 LATE ADDENDUM (this reverses § 1.8).
- **[NY] R113.1**: violations of Chapter 1 carry Executive Law § 382(2)
  penalties.
- **[NY] R115**: solid fuel-burning appliance, chimney or flue — separate
  permit, inspection and certificate of compliance before operation; fine
  ≤ $250 (Executive Law § 378(5-c)).

### 3.5 Climatic and geographic design criteria — filled in locally, by rule `[V]`

[NY] R301.2: "Additional criteria shall be established by the authority
having jurisdiction and set forth in Table R301.2." Footnotes: "(b) [NY] …
The authority having jurisdiction shall fill in the frost line depth column
with the minimum depth of footing below finish grade." "(d) [NY] The
authority having jurisdiction shall fill in this part of the table with the
wind speed from the ultimate design wind speeds map." "(o) [NY] The
authority having jurisdiction shall fill in this section … using the Ground
Snow Loads in Figure R301.2(3) in accordance with Section R301.2.3."

Where DOS is the AHJ, 19 NYCRR § 1202.12 puts the burden on the **owner** to
supply "ground snow load; wind design loads; seismic design category;
potential damage from weathering, frost, and termite; winter design
temperature; whether ice barrier underlayment is required; the air freezing
index; and the mean annual temperature," and if the town never set them, to
have a licensed architect or engineer establish them (§ 1202.12(b)).

**Consequence: there is no statewide frost depth.** The guide's "36 in / 42 in
/ 48 in" table is a set of local customs. The kit prints the rule and a
write-in line.

### 3.6 Snow — the number that forces an engineer `[V]`

**[NY] R301.2.3 Snow loads**, verbatim: "Ground snow loads shall be the
larger of those determined in accordance with Figure R301.2(3) and Figure
R302.2(4) [sic — the figure is R301.2(4)], or shall be determined in
accordance in with Section 1608 of the Building Code of New York State.
Wood-framed construction, cold-formed, steel-framed construction and masonry
and concrete construction, and structural insulated panel construction in
regions with allowable stress design ground snow loads, pg(asd), **70 pounds
per square foot** (3.35 kPa) or less, shall be in accordance with Chapters 5,
6 and 8. Buildings in regions with allowable stress design ground snow
loads, pg(asd), **greater than 70 pounds per square foot** (3.35 kPa) shall
be designed in accordance with accepted engineering practice."

Figure R301.2(4), Note 1, verbatim: "For sites at elevations above 1,000
feet (304.8 m), the ground snow load shown in Figure 301.2(4) shall be
increased from the mapped value by **2 psf** (0.096 kN/m2) for every **100
feet** (30.48 m) above 1,000 feet (304.8 m)." Figure R301.2(3) Note 1 points
to the ASCE 7 Hazard Tool geodatabase. Ground snow load is then the
**larger** of the two figures.

The BCNYS side: 19 NYCRR § 1221 amends "[NY] FIGURE 1608.2(5)—MINIMUM GROUND
SNOW LOADS FOR NEW YORK STATE" to add a Risk Category importance-factor note
(I 0.8, III 1.1, IV 1.2) — Risk Category II houses are unaffected.

**Kit correction of the guide:** the 70 psf ceiling is a *code* threshold in
R301.2.3, not a "Lewis County codes office" policy; the 2 psf/100 ft
surcharge is Note 1 to Figure R301.2(4); and the county list (Lewis, Oswego,
Jefferson, Hamilton, Herkimer, Essex) is unsourced — the kit prints the rule
and tells the reader to pull the two figures for the parcel.

### 3.7 Sprinklers, smoke and CO `[V]`

The 2025 RCNYS renumbered Chapter 3; the sprinkler section is **R309
Automatic Sprinkler Systems** (R313 is now Ceiling Height — do not cite
"R313" for sprinklers in New York).

- **[NY] R309.2 One- and two-family dwellings**, verbatim: "An automatic
  sprinkler system shall be installed in one- and two-family dwellings where
  such dwellings have a height of **three stories above grade plane**."
  Exceptions: additions/alterations to unsprinklered existing buildings
  (unless Appendix BO requires); manufactured homes. Design per P2904 or
  NFPA 13D.
- **[NY] R309.1 Townhouses**: required at three stories above grade plane,
  **or** "a height of less than three stories above grade plane and have a
  public water main available for connection."
- **Consequence:** a one- or two-story house (counting a walk-out basement
  that meets the § 1219.2(a)(18) "story above grade plane" test) needs no
  sprinkler. A three-story house does. The guide's "sprinkler stance" is
  simply absent; the kit prints R309.2.
- **[NY] R310 Smoke alarms**: "Smoke alarms and heat detection shall comply
  with NFPA 72, Section R310 and the manufacturer's installation
  instructions." [NY] R310.2.1: "Smoke alarms shall be provided in dwelling
  units. **Heat detection shall be provided in new attached garages**" —
  a New York addition.
- **[NY] R311 Carbon monoxide alarms**: "provided in accordance with Section
  915 of the Fire Code of New York State." Statutory floor: Executive Law
  § 378(5-a) (CO detector in every one- or two-family dwelling with
  fuel-burning appliances or an attached garage) and § 378(5-b) (smoke
  alarms; battery-operated permitted; **affidavit of compliance delivered at
  conveyance**, grantee has 10 days to object).

### 3.8 Flood `[V]`

[NY] R306.1: applies in "A Zones, shaded X Zones, B Zones, Coastal A Zones,
and V Zones" — the New York text sweeps **shaded X and B zones** into
flood-resistant construction, which the model code does not. R301.2.4:
floodways go to ASCE 24. Statutory root: Executive Law § 378(1-a) (post-Sandy
coastal standards). [NY] R106.1.4 lists what flood-zone drawings must show.

### 3.9 ⚠ ELECTRICAL — the New York trap `[V]`

**Edition.** The 2025 RCNYS Electrical Part header, verbatim: "This
Electrical Part (Chapters 34 through 43) is produced and copyrighted by the
National Fire Protection Association (NFPA) and is based on the **2023
National Electrical Code® (NEC®) (NFPA 70®—2023)**." E3401.2: "Electrical
systems, equipment or components not specifically covered in these chapters
shall comply with the applicable provisions of NFPA 70." So for a house the
kit cites **2025 RCNYS Chapters 34–43 (NEC 2023 basis)**. The guide's "the
exact NEC edition … vary" is wrong: it is fixed statewide by the adopted
book.

**Scope.** E3401.2: "Services within the scope of this code shall be limited
to 120/240-volt, 0- to 400-ampere, single-phase systems."

**The New York-only section — [NY] E3401.2.1 Owner-occupied one-family
dwellings**, verbatim: "Owner-occupied one-family dwellings and accessory
structures **shall not be required to be provided with electrical power,
wiring, devices and equipment**, unless expressly required by statute, local
law, ordinance, or other regulations. If an on-site electrical power system
is installed or used, all electrical wiring, devices and equipment in such
system shall comply with Part VIII—Electrical of this code." **An
owner-occupied off-grid house is lawful under the Uniform Code**; a rented
one is not. Nothing similar exists for plumbing. Highest-value single
sentence in the code for this site's audience.

**Who inspects — the trap.** E3403.2: "New electrical work … shall be
inspected by the building official." But 19 NYCRR § 1203.2(e)(4) classes
"electrical inspections" as **special inspections**, which are "not
considered to be building safety inspector enforcement activities," and an
AHJ "shall not accept or rely upon a special inspection unless the person
performing such special inspection (i) is a qualified person employed or
retained by **an agency that has been approved by the authority having
jurisdiction** and (ii) has been approved by the authority having
jurisdiction." In practice most New York building departments do not
employ an electrical inspector and instead accept certificates from
third-party electrical inspection agencies **they have approved**. The kit
prints the rule and the verification step: *ask the AHJ for its list of
approved electrical inspection agencies before wiring, and get the agency's
rough-in and final certificates into the CO file (§ 1203.3(d)(2)(ii),
"final report of special inspections").* **There is no state list of
approved electrical inspection agencies** (verified absence on DOS pages
read; DOS FAQ: licensing of electricians "not handled by this Division").

**Licensing.** No state electrician license exists (§ 5.1). Whether a
homeowner may do their own wiring is a *local licensing law* question, not a
Uniform Code question — Executive Law § 379(3) leaves matters "as to which
the uniform fire prevention and building code does not provide" to the
municipality.

### 3.10 Energy — 2025 ECCCNYS, and the numbers are New York's own `[V]`

19 NYCRR § 1240.4(a) incorporates the "2025 ECCCNYS Residential Provisions";
§ 1240.4 amends only Table R402.1.2 (crawl space wall U-factor typo, 0.55 →
0.055, Climate Zone 4) and clarifies R408.2.4 credits (DOS 2026-1). The book
itself carries New York values, tagged [NY]:

**Climate zones — [NY] Table R301.1(1), by county.** Zone 4: Bronx, Kings,
Nassau, New York, Queens, Richmond, Suffolk, Westchester. Zone 6: Chenango,
Clinton, Delaware, Essex, Franklin, Fulton, Hamilton, Herkimer, Jefferson,
Lewis, Madison, Montgomery, Oneida, Otsego, St. Lawrence, Sullivan, Ulster,
Warren. Zone 5: every other county (Albany, Allegany, Broome, Cattaraugus,
Cayuga, Chautauqua, Chemung, Columbia, Cortland, Dutchess, Erie, Genesee,
Greene, Livingston, Monroe, Niagara, Onondaga, Ontario, Orange, Orleans,
Oswego, Putnam, Rensselaer, Rockland, Saratoga, Schenectady, Schoharie,
Schuyler, Seneca, Steuben, Tioga, Tompkins, Washington, Wayne, Wyoming,
Yates). **Note Ulster, Sullivan and Delaware are Zone 6** — the guide's
"6A = Adirondacks/North Country/Tug Hill" misses the Catskills.

**[NY] Table R402.1.3 — insulation minimum R-values (identical in all three
zones):**

| Component | Zones 4, 5, 6 |
|---|---|
| Ceiling | R-49 |
| Insulation entirely above roof deck | R-30 ci |
| Wood-framed wall | R-30, or 20&5ci, or 13&10ci, or 0&20ci |
| Mass wall | 15/20 |
| Floor | R-30, or 19&7.5ci, or 20ci |
| Basement wall | 15ci, or 19, or 13&5ci |
| Unheated slab | R-10ci, 4 ft |
| Heated slab | R-10ci, 4 ft **and** R-10 full slab |
| Crawl space wall | 15ci, or 19, or 13&5ci |
| Vertical fenestration U | **0.27** (0.30 above 4,000 ft or in windborne-debris regions, Zones 5–6) |
| Skylight U | 0.50 |
| Glazed fenestration SHGC | 0.40 in Zones 4 and 5; NR in Zone 6 |

Footnote (e): "13&5" = R-13 cavity + R-5 continuous. Footnote (h): "30 or
19&7.5ci or 20ci."

**[NY] Table R402.1.2 — U-factors:** fenestration 0.27; skylight 0.50;
ceiling 0.026; wood-frame wall 0.045; floor 0.033; basement wall 0.050;
crawl space wall 0.055; unheated slab F 0.48; heated slab F 0.55.

**Ceiling stayed at R-49** (the 2024 IECC model is R-60 in Zones 5–6) and the
**window U-factor is 0.27** (the model code is 0.30). Both differ from the
guide.

**Air leakage — [NY] R402.5.1.3**, verbatim: "not greater than **3.0 air
changes per hour in Climate Zones 4 and 5**, or 0.19 cubic foot … of the
building thermal envelope area; and not greater than **2.5 air changes per
hour in Climate Zone 6**, or 0.16 cubic foot … of the building thermal
envelope area." Exception 2: buildings of 1,500 sq ft or less of conditioned
floor area may use 0.27 cfm/sq ft of enclosure area. Testing is mandatory
([NY] R402.5.1.2: "The building or each dwelling unit … shall be tested for
air leakage … Where required by the building official, testing shall be
conducted by an approved third party. A written report … shall be … provided
to the building official.") — and § 1203.3(d)(2)(iv) makes that report a CO
precondition.

**Compliance paths — [NY] R401.2**: Prescriptive (R401–R404 **and R408**
additional efficiency package), Simulated Building Performance (R405), or
Energy Rating Index (R406). **R401.3 certificate** must be posted at the
furnace/utility room listing R-values, U-factors, blower-door and duct-test
results, equipment efficiencies, and "The code edition under which the
structure was permitted, the compliance path used."

**NYStretch** `[V]`: NYSERDA's page in September 2026 still offered
**NYStretch-2020** and said only "NYSERDA plans to update NYStretch as energy
codes and technologies evolve." No 2025 NYStretch was found on NYSERDA's
site; no statewide list of adopting municipalities is published there. The
kit says: ask the AHJ whether it has adopted NYStretch and which edition;
print nothing else. The guide's "an updated NYStretch is being published to
pair with the 2025 code" is unverified.

### 3.11 The All-Electric Buildings Act — statute, rule, court, clock `[V]`

**Statute.** Executive Law § 378(19)(a) (Part RR, Chapter 56, Laws of 2023):
"the uniform code shall prohibit the installation of fossil-fuel equipment
and building systems, in any new building **not more than seven stories in
height**, except for a new commercial or industrial building greater than
one hundred thousand square feet in conditioned floor area, **on or after
December thirty-first, two thousand twenty-five**, and … in all new buildings
on or after December thirty-first, two thousand twenty-eight." Exemptions in
§ 378(19)(c): emergency/standby power; manufactured homes; listed commercial
uses. § 378(19)(f): grid-infeasibility exemption determined by the Public
Service Commission. Definition, § 378(19)(g)(i): equipment "that uses
fossil-fuel for combustion" and building systems "for the supply,
distribution, or delivery of fossil-fuel."

**Rule.** 19 NYCRR **Subpart 1229-2** (Uniform Code) and **§ 1240.6** (Energy
Code). § 1229-2.4(a)(1): prohibited in "buildings not more than seven stories
above grade plane in height … for which a **substantially complete building
permit application** for the initial construction of such building is
submitted on or after December 31, 2025." § 1229-2.3(20) defines
"substantially complete building permit application" as one that "includes
sufficient information and documentation required by the stricter of either
the authority having jurisdiction's Code Enforcement Program or … 19 NYCRR
Part 1203, such that the authority having jurisdiction can examine the
application." § 1229-2.5 exemptions: manufactured home; agricultural
building; critical infrastructure; hospital; emergency/standby power; the
**grid exemption** on "a written determination, issued by local utility …
indicating that new or expanded electric service cannot be reasonably
provided"; and a conditional list (car wash, commercial food establishment,
crematorium, fuel cell, laboratory, laundromat, manufacturing). **Nothing in
1229-2 exempts a single-family house, a wood stove, a propane range, or a
generator used for anything but emergency/standby power.**

**Court.** *Mulhern Gas Co. v. Mosley*, N.D.N.Y. 1:23-cv-01267 →
2d Cir. 25-2041 (consolidated with *Ass'n of Contracting Plumbers v. City of
New York*, 25-977). The **Stipulation and Order** signed by Judge Suddaby
**18 November 2025** (Dkt. 75), verbatim ¶ 2: "The effective date of 19
N.Y.C.R.R. § 1240.6 … and 19 N.Y.C.R.R. Subpart 1229-2 … is hereby
suspended, pending final disposition of the Plaintiffs' appeal in the Second
Circuit and the disposition of any petition for a writ of certiorari, if such
writ is timely sought." ¶ 4: "If no writ of certiorari is timely sought, this
suspension shall terminate automatically **120 days after the issuance of
the mandate** of the Second Circuit. Should a writ of certiorari be timely
sought by any party, and denied, then this suspension shall terminate
automatically on the 120th day after such denial. Should … the petition for a
writ of certiorari [be] granted, then this suspension shall terminate
automatically upon the 120th day following the sending down of the judgment
of the Supreme Court."

**Second Circuit decision**: 30 June 2026, affirmed (EPCA does not preempt).
**Docket 25-2041 (CourtListener, retrieved 3 September 2026)**: 7 July 2026
extension to file rehearing petition to 28 July 2026; **26 August 2026 —
"ORDER, denying petition for rehearing en banc"**; **2 September 2026 —
"JUDGMENT MANDATE, ISSUED."**

**Arithmetic the kit must print with its date-stamp:**
- Mandate issued 2 September 2026 → **120 days = 31 December 2026**. If no
  certiorari petition is filed, the prohibition becomes enforceable for
  substantially complete applications submitted on or after that date.
- A certiorari petition is due 90 days after the denial of rehearing
  (26 August 2026) → **on or about 24 November 2026**. If filed, the
  suspension continues until 120 days after denial, or 120 days after a
  Supreme Court judgment.
- **DOS status line (Notice of Adoption page, "Update on Recent Court
  Ruling – July 2, 2026")**: the provisions "continue to be suspended by
  Court Order and are neither effective nor enforceable." DOS "will continue
  to monitor the case and will provide updates accordingly."

**What the reader actually needs:** the trigger is the *date the
substantially complete application is submitted*, not the CO date. A house
whose complete application is in before the suspension lifts is outside the
prohibition regardless of when it is built (§ 1229-2.4(a)(1), and (b): the
prohibition does not apply "to buildings existing prior to the effective
date of the applicable prohibition"). This is the single most
time-sensitive instruction in the kit. Tripwire in § 9.

---

## 4. PERMITS, CLOCKS AND INSPECTIONS

Everything in this section is **19 NYCRR Part 1203** as repealed and re-added
by the rule adopted 29 December 2021, **effective 30 December 2022** (DOS
Notice of Adoption page; rule text PDF `2021-12-10-full-text-of-rule-part-1203.pdf`).
`[V]` throughout unless marked.

### 4.1 What Part 1203 is — and is not `[V]`

§ 1203.1(a): "Section 381 of the Executive Law directs the Secretary of State
to promulgate rules and regulations for administration of the New York State
Uniform Fire Prevention and Building Code and the New York State Energy
Conservation Construction Code."

§ 1203.2(a): "Every city, village, town, and county responsible for
administration and enforcement of either or both of the Codes shall establish
a code enforcement program to provide for such administration and enforcement
by **local law, ordinance, or other appropriate regulation**. Such code
enforcement program shall include the features and provisions described in
section 1203.3 of this Part."

§ 1203.3 lead-in: "Each authority having jurisdiction must provide for each of
the listed features through local law, ordinance, or appropriate regulation.
Such authority having jurisdiction **may adopt provisions for administration
and enforcement that are more stringent** than the minimum standards set forth
in this section."

**Kit framing:** Part 1203 is a *floor*, not the permit ordinance. The
reader's actual permit rules are in the municipality's local law (DOS
publishes a model local law that most towns copied). The kit prints the floor
with the citation, then tells the reader to pull the local law. Where the
floor is silent (fees, review clocks, inspector response), the kit says so
rather than inventing a number.

### 4.2 Building permit — required, with a permissive exemption list `[V]` — § 1203.3(a)(1)

"Each authority having jurisdiction shall include in its code enforcement
program provisions requiring building permits to be required for work that
must conform to either or both of the Codes." The AHJ **may** (not must)
exempt eight categories. The ones that touch a house build:

- (i) one-story detached structures accessory to one- or two-family dwellings
  or townhouses "used for tool and storage sheds, playhouses, or similar uses,
  provided the gross floor area **does not exceed 144 square feet**";
- (iii) window awnings on a one- or two-family dwelling;
- (v) "painting, wallpapering, tiling, carpeting, or other similar finish work";
- (vi) "installation of listed portable electrical, plumbing, heating,
  ventilation, or cooling equipment or appliances";
- (vii) like-for-like equipment replacement;
- (viii) repairs that do not affect the structural system, the means of egress
  or the fire protection system.

Gloss printed verbatim in the same paragraph: "An exemption from the
requirement to obtain a building permit **shall not be deemed an authorization
for work to be performed in violation** of either or both of the Codes."

**Trap:** the 144 sq ft shed exemption is *optional for the AHJ*. A town may
require a permit for a 100 sq ft shed. Print "up to 144 sq ft *if your
municipality adopted the exemption*."

### 4.3 What the application must contain `[V]` — § 1203.3(a)(2)

An application "shall include, but not be limited to":

1. description of the location, nature, extent, and scope of the work;
2. **tax map number** and street address;
3. occupancy classification;
4. where applicable, a **statement of special inspections**;
5. construction documents (drawings and/or specifications) per (a)(3);
6. additional submittal documents required by the Codes;
7. anything else the AHJ "may deem necessary."

### 4.4 What the drawings must show `[V]` — § 1203.3(a)(3)

Construction documents must be "drawn to scale on suitable material or in
electronic media" and, where applicable, show:

- location, nature, extent, scope;
- conformance with the Codes;
- "the location, construction, size, and character of all portions of the
  **means of egress**";
- "a representation of the **building thermal envelope**";
- structural information "including but not limited to **braced wall
  designs**; the size, section, and relative locations of structural members;
  design loads";
- structural, electrical, plumbing, mechanical, fire-protection and other
  service systems;
- "a **written statement indicating compliance with the Energy Code**";
- **the site plan**: "a site plan, drawn to scale and **drawn in accordance
  with an accurate boundary survey**, showing the size and location of new
  construction and existing structures and appurtenances on the site;
  distances from lot lines; the established street grades and the proposed
  finished grades; and, as applicable, flood hazard areas, floodways, and
  design flood elevations";
- **design-professional evidence**, (a)(3)(ix): "evidence that the documents
  were prepared by a licensed and registered architect in accordance with
  Article 147 of the New York State Education Law or a licensed and registered
  professional engineer in accordance with Article 145 of the New York State
  Education Law and practice guidelines, including but not limited to the
  design professional's seal … signed by the design professional … the design
  professional's registration expiration date, the design professional's firm
  name (if not a sole practitioner), and, if the documents are submitted by a
  professional engineering firm and not a sole practitioner professional
  engineer, the firm's Certificate of Authorization number."

**Owner-drawn plans — read (ix) carefully.** The list is prefaced "where
applicable," and (ix) is about *what the evidence looks like when a licensed
professional prepared the documents*. It does not itself say a house must be
designed by a licensed professional; that question is governed by the
Education Law exemptions (see § 5.4 below — open until verified). The kit must
not print "New York requires stamped plans for every house" on the strength
of § 1203.3(a)(3)(ix) alone.

### 4.5 Plan review, permit conditions, expiry `[V]` — § 1203.3(a)(4)–(8)

| Item | Rule | Cite |
|---|---|---|
| Plan examination | AHJ (or its § 1203.2(e)(2) contractor) "shall examine applications … to ascertain whether the proposed work is in conformance." Approved documents are stamped; one set retained, **one set returned "to be available at the work site"** | (a)(4) |
| Permit statement | Permit must state all work shall accord with the approved application, and must direct the holder to "notify the authority having jurisdiction **immediately in the event of changes** occurring during construction" | (a)(5) |
| **Expiration** | "building permits to be issued with a **specific expiration date**." AHJ "may provide that a building permit shall become invalid unless the work authorized is commenced within a specified period" | (a)(6) |
| Revocation | Permit issued in error, or work violating the Codes, "shall be revoked or suspended" until compliance is shown | (a)(7) |
| Display | Permit "visibly displayed at the worksite" until completion | (a)(8) |
| **Review clock** | **NONE.** No provision of Part 1203 sets a number of days for plan review. (verified absence) | — |
| **Fees** | Part 1203 sets **no fee and no maximum**. (Executive Law § 381(1) tells the Secretary to address "minimum fees" in the standards; the 2022 Part 1203 carries no fee schedule.) The municipality's local law and fee resolution govern. | — |

### 4.6 Inspections — the statewide minimum list `[V]` — § 1203.3(b)(1)

Inspections "shall include but not be limited to the following elements of
the construction process, where applicable":

1. "worksite **prior to the issuance of a permit**";
2. footing and foundation;
3. preparation for concrete slab;
4. framing;
5. "structural, **electrical**, plumbing, mechanical, fire-protection, and
   other similar service systems of the building";
6. fire resistant construction;
7. fire resistant penetrations;
8. "solid fuel-burning heating appliances, chimneys, flues, or gas vents";
9. **Energy Code** inspections "including but not limited to insulation,
   fenestration, **air leakage**, system controls, mechanical equipment size,
   and, where required, minimum fan efficiencies, programmable thermostats,
   energy recovery, whole-house ventilation, plumbing heat traps,
   high-performance lighting, and controls";
10. installation, connection and assembly of factory manufactured buildings
    and manufactured homes;
11. "a final inspection after all work authorized by the building permit has
    been completed."

**Remote inspections** are expressly allowed "when, at the discretion of the
authority having jurisdiction, the remote inspection can be performed to the
same level and quality as an in-person inspection." (b)(1).

**Duties on the permit holder** (b)(2): work "shall remain accessible and
exposed until inspected and accepted," and the holder must "notify the
authority having jurisdiction when construction work is ready for inspection."

**Duty on the inspector** (b)(3): after each inspection the AHJ "shall note
the work … to be satisfactory as completed, or the building permit holder
shall be notified as to the manner in which the work fails to comply …
**including a citation to the specific code provision or provisions that have
not been met**." Non-compliant work stays exposed until re-inspected.

**Inspector response time: NONE.** No provision of Part 1203 obliges the AHJ
to attend within any number of days. (verified absence)

**Kit consequence:** the guide's "10–14 inspections" list is a local
composite. The statewide floor is the eleven-element list above, which
already implies more than the five Pennsylvania requires — footing *and*
foundation, slab prep, framing, every service system, energy items
separately, and a pre-permit site visit. Print the list with the cite and
tell the reader the town's local law may add to it.

### 4.7 Special inspections and electrical — § 1203.2(e)(4) `[V]`

"'Special inspections' (as defined in the Uniform Code), including but not
limited to, **electrical inspections**, elevator inspections, welding
inspections, and smoke control system inspections are not considered to be
building safety inspector enforcement activities or code enforcement official
enforcement activities … However, an authority having jurisdiction **shall not
accept or rely upon a special inspection unless the person performing such
special inspection (i) is a qualified person employed or retained by an agency
that has been approved by the authority having jurisdiction and (ii) has been
approved by the authority having jurisdiction** as having the competence
necessary to inspect a particular type of construction requiring such special
inspection."

This is the regulatory root of the New York electrical-inspection trap (see
§ 3.x ⚠ ELECTRICAL): the building department's own inspector is not
necessarily the electrical inspector, and the electrical inspector must be
from an agency *the AHJ has approved*. The permit applicant cannot pick any
inspector.

### 4.8 Contracted-out enforcement `[V]` — § 1203.2(e)

An AHJ "may contract directly with an individual or business entity to
perform 'building safety inspector enforcement activities' or 'code
enforcement official enforcement activities' … on behalf of the authority
having jurisdiction," provided the contractor's people have qualifications
comparable to Part 1208 certification. So the person who reviews the plans
may be a private firm under contract — but the **permit still issues from
the municipality**, unlike Pennsylvania's opt-out model where the applicant
hires the agency.

### 4.9 Stop work orders `[V]` — § 1203.3(c)

Issued for work "contrary to provisions of either or both of the Codes, is
being conducted in a dangerous or unsafe manner, is being performed without
obtaining a required building permit, or when a building permit has been
issued in error." The order "shall state the reason for its issuance and the
conditions which must be satisfied before work will be allowed to resume."

### 4.10 Certificate of occupancy `[V]` — § 1203.3(d)

- (d)(1): "permission to use or occupy a building or structure … for which a
  building permit was previously issued … **shall be granted only by issuance
  of a certificate of occupancy or a certificate of compliance**," except a
  temporary CO under (d)(4).
- (d)(2): the AHJ may not issue the CO until it has (i) inspected and found
  compliance; (ii) where applicable, received the structural observations
  statement and/or **final report of special inspections**; (iii) where
  applicable, **flood hazard certifications**; (iv) where applicable, "each
  written statement of the results of tests performed to show compliance
  with the Energy Code" (this is where the blower-door result lands); (v)
  factory-built seals/data plates.
- (d)(3): the CO must carry the permit number and date, address and tax map
  number, portion covered, use and occupancy classification, construction
  type, assembly occupant load, "any special conditions imposed in connection
  with the issuance of the building permit," signature, issue date.
- (d)(4): **temporary CO** allowed before completion, "limited to a specified
  period of time," and only once the structure "may be occupied safely,"
  fire/smoke/CO/heat detection is "installed and operational," and "all
  required means of egress … have been provided."
- (d)(5): a CO issued in error or on incorrect information is suspended or
  revoked if deficiencies are not corrected within a specified period.
- **CO clock: NONE.** No day-count exists for issuing a CO. (verified absence)

### 4.11 Fees, appeals — what Part 1203 does not do

- **Fees**: not in Part 1203. Each municipality sets its own by local law or
  resolution. Do not print a number.
- **Appeals of a code official's decision**: Part 1203 contains no appeal
  board requirement (verified absence in the rule text). Variances from the
  Uniform Code and Energy Code themselves go to the Department of State under
  **19 NYCRR Part 1205** (Notice of Adoption page: "Uniform Code: Variance and
  Appeals Procedures," adopted 15 April 2025, effective 30 April 2025). The
  kit points readers to Part 1205 for a code variance and to the local law for
  anything about the official's conduct. *Part 1205 text not read in this
  session — the kit cites it only for existence and title, not for procedure.*

### 4.12 Order to remedy — the one statewide clock `[V]` — § 1203.5

§ 1203.5(c): "the time within which a person or entity served with an order
to remedy is required to comply with such order to remedy is hereby fixed at
**30 days** following the date of such order." § 1203.5(e): served personally
or by certified/registered mail "within five days of the date of the order";
mailed orders are deemed served on the mailing date. § 1203.5(f): the AHJ may
require corrective action to *begin* immediately. This is the clock Executive
Law § 382(2) refers to; missing it is what converts a violation into the
$1,000-per-day exposure.

---

## 5. LICENSING AND CONTRACTS

### 5.1 No state contractor, electrician or plumber license `[V]`

- DOS Division of Building Standards and Codes FAQ, verbatim: "Issues
  regarding local laws, zoning, and **licensing of contractors or
  electricians are not handled by this Division**." The same FAQ notes DOS's
  Division of Licensing Services licenses home inspectors and security/fire
  alarm installers — neither reaches a house build.
- Executive Law Article 18 contains no licensing provision (verified
  absence). Executive Law § 379(3) leaves licensing to municipalities as a
  matter "as to which the uniform fire prevention and building code does
  not provide"; DOS Legal Memorandum LG07: "municipalities are not
  prohibited from adopting or enacting building regulations pertaining to
  matters not addressed by the Uniform Code."
- **There is no statewide registry to search.** The kit tells the reader to
  ask the town clerk and county consumer-affairs office whether a local
  electrician, plumber or home-improvement license law exists.

### 5.2 ⚠ The permit gate nobody prints: GML § 125, WCL § 57, Form CE-200 `[V]`

**General Municipal Law § 125**, verbatim and complete:

> "No city, town or village shall issue a building permit without obtaining
> from the permit applicant either: 1. proof duly subscribed that workers'
> compensation insurance and disability benefits coverage issued by an
> insurance carrier in a form satisfactory to the chair of the workers'
> compensation board as provided for in section fifty-seven of the workers'
> compensation law is effective; or 2. **an affidavit that such permit
> applicant has not engaged an employer or any employees** as those terms are
> defined in section two of the workers' compensation law to perform work
> relating to such building permit."

**Workers' Compensation Law § 57(1)**: the head of any state or municipal
office "authorized or required by law to issue any permit for or in
connection with any work involving the employment of employees in a
hazardous employment … shall not issue such permit unless proof duly
subscribed by an insurance carrier is produced in a form satisfactory to the
chair, that compensation for all employees has been secured."

**The Board's forms** (WCB, "Requirements for businesses applying for
government permits, licenses, or contracts," BIZ-ContractREQs-fs-1-v12):
insured applicants produce **Form C-105.2** (workers' comp, from the carrier;
State Insurance Fund uses **U-26.3**) and **Form DB-120.1** (disability and
Paid Family Leave); "**ACORD forms are not acceptable** proof of New York
State workers' compensation coverage under WCL §57." Exempt applicants
obtain a **Certificate of Attestation of Exemption, Form CE-200**, "through
New York Business Express at businessexpress.ny.gov."

**CE-200 rules** (WCB exemption pages, verbatim):
- "Certificates are only valid for the specific license, permit or contract.
  **Certificates for building permits are job-specific and a separate
  certificate will be required for each building permit.**"
- Only "Entities operating in NY with no employees" (and out-of-state
  entities working wholly outside NY) may apply.
- The CE-200 "CAN NOT be used to show another business or that business's
  insurance carrier that coverage is not required."
- The Board's instruction sheet (WCB-Exemption-Instr-1-v3): "Under How to
  Apply: Select Apply as a Business, or Select **Apply as a Homeowner
  (applies to those obtaining permits to work on their residence)**." A
  NY.gov Business account is required; the certificate carries a number the
  building department can validate online.

**How the kit frames it (NY.1).** GML § 125 gives an owner-builder exactly
two doors: a carrier-issued C-105.2 + DB-120.1 (only if the owner actually
carries a policy), or the affidavit — which in practice is the CE-200
"homeowner" attestation that the applicant has "not engaged an employer or
any employees." An owner who hires *insured subcontractors* is not thereby
an employer of the subs' workers; an owner who hires individuals by the hour
to swing hammers may be. The kit prints the two doors, the forms, and the
job-specific rule, and tells the reader that whether day-labor makes them an
"employer" under WCL § 2 is a question for the Board or a lawyer — it does
not resolve it. **WCL § 56** (contractor liable for uninsured subcontractor's
injured employee) speaks of "a contractor," not an owner; the kit notes the
section exists and does not assert it reaches a homeowner.

### 5.3 Labor Law § 240 — the homeowner exemption turns on "direct or control" `[V]`

Labor Law § 240(1) imposes the scaffold/elevation duty on "All contractors
and owners and their agents, **except owners of one and two-family dwellings
who contract for but do not direct or control the work**." (Read on
nysenate.gov, September 2026.) **Kit statement:** an owner-builder who hires
trades and stays out of the means and methods is inside the exemption; an
owner-builder who supervises the framing crew from the deck may not be. The
kit prints the statutory phrase and nothing more — the case law on "direct
or control" is not summarized.

### 5.4 Stamped plans — the 1,500 sq ft rule `[V]`

**Education Law § 7307(5)** (architecture): "This article shall not apply to:
1. Farm buildings … nor to **residence buildings of gross area of fifteen
hundred square feet or less, not including garages, carports, porches,
cellars, or uninhabitable basements or attics**; or 2. Alterations, costing
… twenty thousand dollars or less, to any building or structure outside the
city of New York which do not involve changes affecting the structural
safety or public safety thereof."

**Education Law § 7209(7)(b)** (engineering): the same 1,500 sq ft residence
exclusion, and alterations "costing ten thousand dollars or less."

**§ 7307(1) / § 7209(1)**: no state, county, city, town or village official
"shall accept or approve any plans or specifications that are not stamped"
by a New York-licensed architect or engineer — except plans the articles do
not apply to.

**[NY] R106.6** ties the code to this: documents "shall be prepared by a
registered design professional **when required by Article 145 or Article 147
of the New York State Education Law**, by the stricter of Code Enforcement
Program of the authority having jurisdiction or a Part 1203—Compliant Code
Enforcement Program, or by any other applicable law."

**Kit statement:** a house of **more than 1,500 sq ft gross** (excluding
garage, carport, porches, cellar, uninhabitable basement/attic) needs
architect- or engineer-stamped drawings statewide. At or under 1,500 sq ft
the state law does not require a stamp, **but the local code enforcement
program may** (R106.6 "stricter of"), and any Part 1203 AHJ can still demand
"structural information including … braced wall designs" (§ 1203.3(a)(3)(v))
and engineered design where snow load exceeds 70 psf (R301.2.3). Education
Law § 7306(1)(c) separately confirms "Builders, or superintendents employed by
such builders" may supervise construction without an architect.

### 5.5 Home-improvement licensing counties — new construction is mostly outside `[V]`

The kit covers this in one paragraph because the county laws mostly exclude a
new house, but one state law reaches a custom home:

| Jurisdiction | Instrument read | New-home treatment `[V]` |
|---|---|---|
| **Suffolk** | Suffolk County Code § 563-16 (county PDF "CA-L01a") | "Home improvement contracting" … "shall not include **the construction of a new home** or work done by a contractor in compliance with a guaranty of completion on new residential property." Also excludes "work in the electrical and plumbing fields as defined by § 563-126" — Suffolk licenses those separately. |
| **Nassau** | Nassau County Administrative Code § 21-11.1(3) (local law text, county DocumentCenter) | "'Home Improvement' shall not include (a) **the construction of a new home building** or work done by a contractor in compliance with a guarantee of completion of a new building project." |
| **Putnam** | Putnam County Code Ch. 135 (county PDF), § 135-3(C) | Chapter does not apply to "(1) The sale or construction of a new home **other than a custom home** as defined in § 135-4"; "(3) **Work performed upon a residence by the owner**"; "(8) Plumbing, as defined in Chapter 190"; "(9) Electrical, as defined in Chapter 145" — Putnam licenses plumbers and electricians. |
| **Westchester** | Laws of Westchester County § 863.312 (reproduced in the county's own license application) | "Home improvement" = "repair, replacement, remodeling, installation, construction, alteration, conversion, modernization made to, in or upon a private residence …"; § 863.313: "No person shall … engage in the home improvement business within the county of Westchester … unless … licensed." **No express new-home exclusion in § 863.312**; the definition is broad enough to reach a contractor's work on a new house. Verify with the county before hiring. |
| **Rockland** | Rockland County Code Ch. 286 — **text not retrieved** (ecode360 blocked; county page 403) | Not verified. The kit says Rockland licenses home-improvement contractors and tells the reader to obtain the current chapter from the county. |

**None of the five reaches the owner working on their own house.** Putnam
says so expressly; the others define the licensee as a person conducting a
home-improvement *business* for an owner.

### 5.6 The state contract law that DOES reach a custom home — GBL Article 36-A and Lien Law § 71-a `[V]`

General Business Law § 770(3): "'Home improvement' shall also mean **the
construction of a custom home**." § 770(7): "custom home" is "a new single
family residence to be constructed on premises owned of record by the
purchaser at the time of contract, provided that such residence is intended
for residential occupancy by such purchaser." § 770(4): a home improvement
contract is one whose aggregate price exceeds **$500**. § 770(6): "owner"
includes "any person who purchases a custom home."

**GBL § 771(1)**: every such contract "shall be evidenced by a writing" and
contain, among other things — (a) contractor name, address, phone and
license number if any; (b) approximate start and substantial-completion
dates and whether completion is of the essence; (c) description of work and
materials and the agreed consideration; (d) a bold notice that an unpaid
contractor or subcontractor may file a mechanic's lien; (e) a notice that
the contractor must "deposit all payments received prior to completion" in
escrow or post "a bond, contract of indemnity or irrevocable letter of
credit" under **Lien Law § 71-a**; (f) any progress-payment schedule, with
amounts "bearing a reasonable relationship" to work performed; (h) the
owner's right to cancel "until midnight of the third business day"; (i)
the contractor's insurance disclosure. § 771(2): plain English, and a signed
copy to the owner before work begins.

**Lien Law § 71-a(4)**: payments received by a home improvement contractor
"prior to the substantial completion of work … shall be deposited within
five business days … in an escrow account," or the contractor may "post … a
bond or contract of indemnity … or an irrevocable letter of credit."

**Kit use (NY.5):** an owner-builder who contracts with a builder to erect
the whole house on the owner's lot is buying a *custom home*, and these
protections attach by statute. An owner who hires trades directly is
contracting for **home improvements** only if the work fits § 770(3) — new
construction by trade is not squarely "repair, replacement, remodeling …
of … residential property" and the kit does not claim it is. The § 771 list is
printed as the drafting benchmark for every trade contract regardless.
*Verified through structured reads of the statute pages on nysenate.gov;
verbatim quotations above are under 125 characters each because the fetch
tool would not return longer passages — a future revision should paste the
full § 771(1) text.*

### 5.7 Manufactured-home installers `[V]`

19 NYCRR Part 1210 certifies installers; DOS FAQ: an owner-occupant "may apply
for certification as the installer of such manufactured home." Not a
site-built house; one line in NY.1.

---

## 6. SITE PLAN STUDIO EXTRACTION

Feeds `src/lib/siteplan/rules.ts`. **All values `[V]`, quoted from 10 NYCRR
Appendix 75-A (effective 16 March 2016) and 10 NYCRR Appendix 5-B (effective
23 November 2005)**, retrieved September 2026. Units are feet.

> **Who administers.** 10 NYCRR § 75.5(a): individual onsite wastewater
> treatment systems "shall be designed and constructed in accordance with …
> Appendix 75-A." § 75.5(b): "Plans for the design of individual onsite
> wastewater treatment systems **shall be prepared directly by or under the
> supervision of a design professional**." § 75.5(c): alternative systems
> need prior review and approval by "the State or county health department
> official having jurisdiction," design-professional supervision of
> construction, and a post-construction certification. The 2025 RCNYS
> [NY] P2602.1.2 incorporates Appendix 75-A into the Uniform Code;
> [NY] P2602.1.1 incorporates Appendix 5-B for wells. **So the code official
> enforces both appendices, and the county health department (or the DOH
> district office in the 21 counties without a full-service health
> department) is the approver.** DOH Fact Sheet #6: "Approvals for deviations
> (e.g., 'specific waivers') from the standards can only be granted by the
> local health department (LHD i.e., county health department or NYS
> District Office) having jurisdiction."

### 6.1 App. 75-A Table 2 — separation distances from wastewater system components `[V]` — § 75-A.4(b)

| System component | Well or suction line (e)(g) | Stream, lake, watercourse (b) or wetland | Dwelling | Property line |
|---|---|---|---|---|
| House sewer (watertight joints) | 25 if cast iron sewer pipe, 50 otherwise | 25 | 3 | 10 |
| Septic tank or watertight ETU | **50** | 50 | 10 | 10 |
| Effluent line to distribution box | 50 | 50 | 10 | 10 |
| Distribution box | 100 | 100 | 20 | 10 |
| **Absorption field** (c)(d) | **100 (a)** | **100** | **20** | **10** |
| Seepage pit (d) | 150 (a) | 100 | 20 | 10 |
| Raised or mound system (c)(d) | 100 (a) | 100 | 20 | 10 |
| Intermittent sand filter (d) | 100 (a)(f) | 100 (f) | 20 | 10 |
| Non-waterborne, offsite residual disposal | 50 | 50 | 20 | 10 |
| Non-waterborne, onsite discharge | 100 | 50 | 20 | 10 |

Notes, verbatim: "(a) When wastewater treatment systems are located upgrade
and in the direct path of surface water drainage to a well, the closest part
of the treatment system shall be at least **200 feet** away from the well.
(b) Mean high water mark. (c) For all systems involving the placement of
fill material, separation distances are measured from the toe of the slope
of the fill. (d) Separation distances shall also be measured from the edge of
the designated additional usable area as described in Section 75-A.4(a)(5).
(e) The closest part of the wastewater treatment system shall be located at
least **10 feet from any water service line**. (f) When sand filters are
designed to be watertight … the separation distance can be reduced to 50
feet. (g) The listed water well separation distances from contaminant
sources **shall be increased by 50% whenever aquifer water enters the water
well at less than 50-feet below grade**."

**Tool framing:** the absorption field row governs a conventional layout;
the well-to-field 100 ft becomes **150 ft** for a shallow well (note g) and
**200 ft** when the field is upgradient in the drainage path (note a).
Wetlands ARE surface water here (unlike Pennsylvania).

### 6.2 App. 75-A — sizing `[V]`

- **Design flow** — § 75-A.3(b): "Designs for new construction shall be based
  upon a minimum daily flow of **110 gallons per day per bedroom**" (Table 1:
  post-1994 fixtures 110; pre-1994 130; pre-1980 150; waterless toilets 75
  graywater only). Not a 400-gpd base.
- **Septic tank** — § 75-A.6(a)(1), Table 3: 1–3 bedrooms **1,000 gal** (27
  sq ft liquid surface); 4 bedrooms 1,250 gal; 5 bedrooms 1,500 gal; 6
  bedrooms 1,750 gal; "+250 gallons and seven square feet of surface area for
  each additional bedroom. A garbage grinder shall be considered equivalent
  to an additional bedroom. … An expansion attic shall be considered as an
  additional bedroom."
- **Reserve area** — § 75-A.4(a)(5): "An additional useable area of **50
  percent** shall be set aside for future expansion or replacement whenever
  possible."
- **Water softener backwash** — § 75-A.3(a): normally excluded unless a
  separate subsurface discharge "250 feet from wells or water courses" is
  unavailable.

### 6.3 App. 75-A — site disqualifiers `[V]` — § 75-A.4(a)

- "(1) Areas lower than the **10 year flood level** are unacceptable for
  on-site systems. **Slopes greater than 15%** are also unacceptable."
- "(2) There must be at least **four feet of useable soil** available above
  rock, unsuitable soil, and high seasonal groundwater for the installation
  of a conventional absorption field system."
- "(3) Soils with very rapid percolation rates (**faster than one minute per
  inch**) are not suitable … unless the site is modified by blending."
- § 75-A.4(c)(2): "Highest groundwater level shall be at least **two feet
  below the proposed trench bottom**"; at least one test hole six feet deep.

### 6.4 App. 5-B Table 1 — separation distances to protect a water well `[V]`

| Contaminant source | Distance |
|---|---|
| Chemical storage sites not protected from the elements (salt, sand/salt) | 300 |
| Landfill, hazardous or radiological waste disposal area | 300 |
| Land application of municipal effluent/sludge; septage; liquid or solid manure; manure pile storage | 200 |
| Cesspools | 200 |
| Wastewater absorption systems in coarse gravel or in the direct path of drainage to a well | 200 |
| Fertilizer/pesticide mixing or clean-up areas; seepage pit; single-walled underground chemical/petroleum tanks | 150 |
| **Absorption field or bed** | **100** |
| Septic system components (non-watertight); intermittent sand filter without liner; privy pit; stormwater recharge from paved areas; cemeteries; barnyard, silo, animal pens | 100 |
| **Septic tank, aerobic unit, watertight effluent line to distribution box** | **50** |
| Sanitary or combined sewer; watertight privy vault; clear-water recharge basin | 50 |
| **Stream, lake, watercourse, drainage ditch, or wetland** | **25** |
| All known sources of contamination not shown | 100 |

Table 1 notes, verbatim: "The listed water well separation distances … shall
be increased by 50% whenever aquifer water enters the water well at less than
50 feet below grade." "Water wells shall not be located in a direct line of
flow from these items, nor in any contaminant plume." § 5-B.2(c): "A well
shall be located upgradient of any potential or known source of
contamination unless property boundaries, site topography, location of
structures and accessibility require a different location."

**App. 5-B carries no well-to-property-line distance and no well-to-dwelling
distance** (verified absence in Table 1) — encode as `unknown` with that
note.

### 6.5 Who may drill `[V]`

- ECL § 15-1525(1): "No person shall engage in **the business of** water well
  drilling in the state of New York without first obtaining a certificate of
  registration from the department." § 15-1525(3): completion report filed
  with DEC; "The water well driller shall provide a copy of such completion
  report to the water well owner." § 15-1525(5): on-site supervisor must have
  passed the NGWA exam. § 15-1525(6): local well-driller licensing laws are
  not preempted if "at least as comprehensive."
- **2025 RCNYS [NY] P2602.1.1**, verbatim: "Individual water supplies
  (private wells) **shall be installed by a well driller registered with the
  Department of Environmental Conservation** and be in compliance with the
  provisions of Appendix 5-B." **So under the Uniform Code an owner may not
  drill their own well** even though ECL § 15-1525 only regulates the
  "business" of drilling. The kit prints P2602.1.1.
- DEC registered-contractor search: `appfactory.dec.ny.gov/WaterWell/Contractor_Search`.
- Long Island: ECL § 15-1527 requires a DEC permit for wells in Kings,
  Queens, Nassau or Suffolk only where pumping capacity exceeds **45 gallons a
  minute** — ordinary house wells are below that; Nassau and Suffolk county
  sanitary codes govern them instead (not read).

### 6.6 Regional overlays that reach one house — flag, do not encode as statewide `[V]`

- **Adirondack Park** (Executive Law Article 27). § 810(2)(d)(1): in
  **Resource Management** areas, "Single family dwellings" are class B
  regional projects; § 809(2)(a): a class B project in a land use area not
  governed by an APA-approved local land use program needs an **APA permit
  before undertaking**. A single-family dwelling within one-eighth mile of
  wilderness/primitive/canoe forest preserve, or within 150 ft (Rural Use) /
  300 ft (Resource Management) of a state or federal highway, is also class B
  (§ 810(2)(c)(17), (d)(9)). § 809(1): a single family dwelling is a "minor
  project" — 45-day decision clock, deemed complete on receipt. **§ 806
  shoreline restrictions apply everywhere in the Park** regardless of APA
  jurisdiction: minimum setback of principal buildings from mean high-water
  mark **50 ft** (hamlet, moderate intensity), **75 ft** (low intensity,
  rural use), **100 ft** (resource management) (§ 806(1)(a)(2)); "the minimum
  setback of any on-site sewage drainage field or seepage pit shall be **one
  hundred feet** from the mean high-water mark in all land use areas"
  (§ 806(1)(b)); lot-width and tree-cutting rules in § 806(1)(a)(1), (3).
  Encode only with an "inside the Adirondack Park" gate.
- **New York City watershed** (10 NYCRR Part 128, effective 13 April 2005).
  § 128-3.8(a)(1): "The design, treatment, construction, maintenance and
  operation of new subsurface sewage treatment systems, and the plans
  therefor, require the review and approval of the Department" (NYC DEP).
  § 128-3.8(a)(5): "No part of any absorption field for a new conventional
  individual subsurface sewage treatment system … shall be located within
  the limiting distance of **100 feet of a watercourse or wetland or 300
  feet of a reservoir, reservoir stem or controlled lake**." Applies in the
  watershed towns of Delaware, Greene, Schoharie, Sullivan, Ulster (West of
  Hudson) and Putnam, Westchester, Dutchess (East of Hudson) — the parcel
  test is DEP's watershed map (`nyc.gov/site/dep/environment/regulations.page`).
  Encode only with an "inside the NYC watershed" gate.

### 6.7 Do NOT encode

- **Building setbacks from lot lines**: zoning, set by ~1,600 municipalities;
  no statewide value (Executive Law § 379(3)).
- **Frost depth**: filled in by the AHJ in Table R301.2 (§ 3.5). No statewide
  table.
- **Ground snow load**: parcel-specific from Figures R301.2(3)/(4) and the
  elevation surcharge; not a county table.
- **Any Long Island county sanitary-code number** (Suffolk Article 6 etc.):
  not read.
- **Well-to-property-line, well-to-house**: App. 5-B has none.

---

## 7. DELIBERATELY NOT PRINTED

| Item | Why |
|---|---|
| Permit fee dollar figures (Albany "$450", Bethlehem "$448", Long Island ranges) | Part 1203 sets no fee; the DOS model local law § 18 says "A fee schedule shall be established by resolution" of each legislative body. Any number is one town's number on one day. The kit prints the rule and a write-in line. |
| Recreation/parkland fee figures ("~$4,000 per unit") | Local, set under Town Law/Village Law subdivision provisions not read here. Not verified. |
| Processing-time tables ("1–4 weeks," "6–14 weeks") | No review clock exists in Part 1203 or Article 18 (verified absence). |
| Frost depth by region ("36/42/48 in") | Table R301.2 is filled in by the AHJ. No statewide value. |
| Ground snow load by county ("60–90 psf," "Lewis County 70 psf policy") | Parcel-specific; the 70 psf figure is the R301.2.3 engineering threshold, not a county policy. |
| An NEC year other than the one in the adopted book | The 2025 RCNYS Electrical Part is expressly NEC 2023-based; no local variation exists. |
| "3 ACH50" as a single statewide value | It is 3.0 in Zones 4–5 and **2.5 in Zone 6** — printed by zone instead. |
| Ceiling R-60 / window U-0.30 | New York's tables say R-49 and U-0.27. |
| "NYStretch 2025" | Not found on NYSERDA's site; 2020 edition is what is published. |
| A list of state-enforced (DOS-AHJ) municipalities | Not retrievable; DOS says only "a limited number." Verification step printed instead. |
| A list of approved third-party electrical inspection agencies | None exists at state level; approval is per-AHJ under § 1203.2(e)(4). |
| A radon-construction requirement | Appendix BE is expressly informational (R101.2.1). |
| Labor Law § 240 "strict liability" as a blanket owner-builder exposure | § 240(1) exempts "owners of one and two-family dwellings who contract for but do not direct or control the work"; the kit prints the phrase, not the guide's unqualified claim. § 241 not read. |
| Rockland County home-improvement definitions | Text not retrievable. |
| "October 28, 2026" as the all-electric start date | Secondary-source arithmetic from a mandate date that never happened; the mandate issued 2 September 2026. |
| Septic/well cost ranges | House rule; not verifiable. |
| Phone numbers | House rule. Several DOS and DOH documents carry them; the kit points at the page. |

---


## 8. OPEN QUESTIONS

1. **Which municipalities have DOS or the county as AHJ.** DOS's 2026 guide
   says the Department "enforces the Uniform Code and the Energy Code in the
   place of only a limited number of local governments." No list was found on
   dos.ny.gov. The kit's NY.4 tells the reader to ask the town clerk whether
   the town has a Part 1203 code enforcement local law. **Action: email
   codes@dos.ny.gov for the current list before the next revision.**
2. ~~Labor Law § 240 homeowner exemption~~ — **RESOLVED** (§ 5.3): § 240(1)
   read; exemption phrase verified. § 241(6) not read — same phrase is
   believed to appear there but is not asserted.
3. **Rockland County Chapter 286** — obtain the text from the county.
4. **Westchester § 863.312** — the definition has no new-home exclusion;
   confirm with the county's Consumer Protection department whether a
   contractor building a new house on an owner's lot must hold the license.
5. **Full text of GBL § 771(1)** — pasted from a verbatim read (the fetch tool
   capped quotations); the kit's NY.5 contract checklist should quote (d),
   (e) and (h) in full once retrieved.
6. **Suffolk/Nassau county sanitary codes** for wells and septic (Suffolk
   Article 6) — not read; NY.4 routes Long Island readers to the county
   health department.
7. **WCL § 2 "employer/employee" as applied to a homeowner hiring day
   labor** — a legal question the kit does not answer; the Board's CE-200
   homeowner path is printed as the procedure.
8. **Whether a certiorari petition is filed** in *Mulhern Gas* by ~24
   November 2026 — determines whether 31 December 2026 is the real
   all-electric start (§ 9, tripwire 1).
9. **19 NYCRR Part 1205 fee schedule** (November 2022 publication) — amount
   not retrieved; the kit says a fee applies and points at DOS Variances.
10. **DEC Part 602 / geothermal** — irrelevant to a house well except on Long
    Island open-loop systems; not pursued.

---


## 9. KIT REVISION WATCH — NEW YORK TRIPWIRES

Add to `project-kit-revision-watch`:

1. **All-electric clock.** Mandate issued 2 September 2026. **Certiorari
   deadline ≈ 24 November 2026.** If none is filed, Subpart 1229-2 / § 1240.6
   become enforceable **31 December 2026** for substantially complete
   applications submitted on or after that date. Watch DOS Notice of
   Adoption page ("Update on Recent Court Ruling") and CourtListener docket
   25-2041. NY.0, NY.1 and NY.2 all carry the date-stamped status box.
2. **Assembly bill A8996 (2025)** would let municipalities opt out of the
   electrification mandate (search result; bill text not read). If enacted,
   § 378(19) changes and the kit's all-electric box must be rebuilt.
3. **Part 1203 revision.** The 2022 rewrite still defines RCNYS as the 2020
   book (§ 1203.1(b)(13)); DOS will conform it. Watch the Notice of Adoption
   page for a new Part 1203 rule — the inspection list and exemption list
   could move.
4. **NYStretch 2025.** NYSERDA said an update is planned. When published,
   NY.2 energy page needs an overlay note; still local adoption only.
5. **2027 code cycle.** Executive Law § 378(20)(a): 90 days' notice minimum
   before any building-code change takes effect. Watch for the next Uniform
   Code update (historically ~5–6-year cycle: 2020 → 2025).
6. **Westlaw NYCRR lag.** Re-check Part 1220 on govt.westlaw.com; when it
   finally shows "2025 RCNYS," drop the stale-Westlaw warning.
7. **DOS FAQ wording** on fossil-fuel suspension — if DOS posts a "no longer
   suspended" update, the kit's status box flips.
8. **Part 1205 fee schedule** republication.

---


## 10. LATE ADDENDUM

**Addendum 1 — Appeals (reverses § 1.8 and the last row of § 4.11).** Written
before Part 1205 and 2025 RCNYS Chapter 1 were read. Both establish a
**statewide appeal route from a code official's decision**: 2025 RCNYS
[NY] R112.1: "An appeal of any order or determination, or the failure within
a reasonable time to make an order or determination, of an administrative
official charged to enforce or purporting to enforce the Uniform Code may be
made in accordance with the provisions of Part 1205." 19 NYCRR
§ 1205.3(a)(2): "Each regional board of review shall have the power to hear
and decide appeals. An appeal may be of any order or determination, relating
directly to the provisions of the Uniform Code, of an administrative official
authorized to enforce the Uniform Code, or the failure of an administrative
official to make such an order or determination within a reasonable amount
of time." Remedies include "sustaining, reversing, or modifying" the order,
or "directing that any orders, determinations, permits, or authorizations be
issued." § 1205.4(b): "Any person aggrieved may petition the regional board
of review for an appeal," on a DOS form with the § 1205.6 fee. § 1205.4(e):
"Petitions shall be decided within **60 days** of completeness unless a
longer period is required for good cause shown." Six regional boards, five
members each (architect, engineer, code-enforcement background, fire
background, businessperson/lawyer) — DOS 2026 guide. **Kit consequence:**
NY.1 and NY.3 print the Part 1205 appeal as the reader's remedy for a stalled
permit or a disputed inspection — a *better* position than Pennsylvania's
opt-out gap. Part 1203 itself still contains no local appeal board
requirement; that part of § 4.11 stands. Complaints about the official's
*conduct* (not the decision) go to DOS on the CEO/BSI complaint form
(`dos.ny.gov/code/complaints`).

**Addendum 2 — the "October 28, 2026" date.** Several trade-press sources
(Mondaq, Earthjustice, Spectrum) computed 120 days from the 30 June 2026
decision and printed 28 October 2026. The stipulation counts from the
**mandate**, and rehearing petitions delayed the mandate to 2 September 2026.
The correct no-certiorari date is **31 December 2026**. § 3.11 was written
after this was established; recorded here so nobody "corrects" it back.

**Addendum 3 — chapter numbering.** Early drafting notes referred to "R313"
for sprinklers (2020 RCNYS numbering). In the 2025 RCNYS the sprinkler
section is **R309**, smoke alarms **R310**, CO alarms **R311**, flood **R306**.
§ 3.7 was corrected before final write; any surviving "R313" reference in
kit copy is an error.

---

## 11. VERIFIED URL SET (September 2026)

Every address below returned HTTP 200 to curl, or (Cloudflare hosts marked
†) was read in full through the browser tools or WebFetch in this session.
**Never print a phone number; several of these pages carry them.**

### The three that matter most

| What | URL |
|---|---|
| ★ **DOS Notice of Adoption page** — current code editions, effective dates, and the all-electric "Update on Recent Court Ruling" status line | `https://dos.ny.gov/notice-adoption` † |
| ★ **WCB Certificate of Attestation of Exemption (CE-200) overview** — the permit gate; "Apply as a Homeowner" is on New York Business Express | `https://www.wcb.ny.gov/content/ebiz/wc_db_exemptions/requestExemptionOverview.jsp` and `https://businessexpress.ny.gov/` |
| ★ **2025 RCNYS, free viewer** (Chapter 1 administration, Chapter 3 design criteria, Chapter 26 wells/septic, Chapters 34–43 electrical) | `https://codes.iccsafe.org/content/NYSRC2025P1` |

### Department of State (all †)

| What | URL |
|---|---|
| Division of Building Standards and Codes home | `https://dos.ny.gov/building-standards-and-codes` |
| Local Government & State Agency Enforcement Programs (Part 1203 reporting, model local law) | `https://dos.ny.gov/code/local-government-state-agency-enforcement-programs` |
| Model Local Law establishing a code enforcement program (PDF) | `https://dos.ny.gov/model-local-laws` |
| Variances (start with a regional office) | `https://dos.ny.gov/code/variances` |
| Complaints about a code official (CEO/BSI form) or an AHJ | `https://dos.ny.gov/code/complaints` |
| FAQ (licensing not handled; fossil-fuel suspension status) | `https://dos.ny.gov/division-building-standards-and-codes-frequently-asked-questions` |
| Legal Memorandum LG03 (what elected officials need to know; opt-out mechanics) | `https://dos.ny.gov/legal-memorandum-lg03-nys-uniform-fire-prevention-and-building-code-what-elected-officials-need` |
| Legal Memorandum LG07 (the Uniform Code and local authority) | `https://dos.ny.gov/legal-memorandum-lg07-uniform-code-and-local-authority` |
| "Administration and Enforcement of the Uniform Code" guide, rev. 2026 (PDF) | `https://dos.ny.gov/system/files/documents/2026/02/administration-and-enforcement-of-the-uniform-code.pdf` |
| Code Outreach 2026-1, "NYCRR Changes to the 2025 Codes" (PDF) | `https://yi.dos.ny.gov/system/files/documents/2026/02/2026-1-nycrr-changes-to-the-2025-codes.pdf` |
| Rule text — 2025 Uniform Code, Parts 1219–1229 (PDF) | `https://dos.ny.gov/rule-text-uniform-code-0` |
| Rule text — 2025 Energy Code, Part 1240 (PDF) | `https://dos.ny.gov/rule-text-part-1240-energy-code` |
| Rule text — Part 1203 (PDF) | `https://dos.ny.gov/system/files/documents/2021/12/2021-12-10-full-text-of-rule-part-1203.pdf` |
| Rule text — Part 1202 (PDF) | `https://dos.ny.gov/system/files/documents/2022/12/2022-12-2-rule-text-part-1202.pdf` |
| Rule text — Part 1205 (2023 base; 2025 amendment) | `https://dos.ny.gov/2023-6-8-rule-text-part-1205`; `https://dos.ny.gov/rule-text-part-1205-uniform-code-variance-and-appeals-procedures` |
| More Restrictive Construction Standards bulletin (Exec. Law § 379) | `https://dos.ny.gov/system/files/documents/2021/05/2021-2018-03-more-restrictive-construction-standards_2020-update.pdf` |

### Statutes (nysenate.gov †)

```
https://www.nysenate.gov/legislation/laws/EXC/A18        Executive Law Art. 18 (§§ 370–383)
https://www.nysenate.gov/legislation/laws/EXC/378        § 378 (incl. subd. 19 all-electric, subd. 20 effective-date rule)
https://www.nysenate.gov/legislation/laws/EXC/381        § 381 (who enforces)
https://www.nysenate.gov/legislation/laws/EXC/383        § 383 (NYC carve-out, (1)(c))
https://www.nysenate.gov/legislation/laws/EXC/806        APA shoreline restrictions
https://www.nysenate.gov/legislation/laws/EXC/809        APA permits
https://www.nysenate.gov/legislation/laws/EXC/810        APA class A/B projects
https://www.nysenate.gov/legislation/laws/GMU/125        GML § 125 building permit / workers' comp
https://www.nysenate.gov/legislation/laws/WKC/57         WCL § 57
https://www.nysenate.gov/legislation/laws/EDN/7307       Ed. Law § 7307 (architecture; 1,500 sq ft)
https://www.nysenate.gov/legislation/laws/EDN/7209       Ed. Law § 7209 (engineering; 1,500 sq ft)
https://www.nysenate.gov/legislation/laws/ENV/15-1525    ECL § 15-1525 well drillers
https://www.nysenate.gov/legislation/laws/GBS/770        GBL § 770 (custom home)
https://www.nysenate.gov/legislation/laws/GBS/771        GBL § 771 (contract contents)
https://www.nysenate.gov/legislation/laws/LIE/71-A       Lien Law § 71-a (escrow)
https://www.nysenate.gov/legislation/laws/LAB/240        Labor Law § 240
```

### Health (septic, wells, radon)

| What | URL |
|---|---|
| 10 NYCRR Appendix 75-A (HTML) | `https://www.health.ny.gov/regulations/nycrr/title_10/part_75/appendix_75-a.htm` |
| 10 NYCRR Appendix 75-A (PDF, the text read here) | `https://www.health.ny.gov/environmental/water/drinking/docs/appendix_75a.pdf` |
| 10 NYCRR § 75.5 (design professional) | `https://regs.health.ny.gov/content/section-755-minimum-standards-individual-onsite-wastewater-treatment-systems` |
| DOH Residential Onsite Wastewater Treatment Systems Design Handbook (PDF) | `https://www.health.ny.gov/environmental/water/drinking/wastewater_treatment_systems/docs/design_handbook.pdf` |
| 10 NYCRR Appendix 5-B (HTML) | `https://www.health.ny.gov/regulations/nycrr/title_10/part_5/appendix_5b.htm` |
| DOH Fact Sheet #6 — wells, guidance for code officials | `https://www.health.ny.gov/environmental/water/drinking/regulations/fact_sheets/fs6_guidance_for_code_enforcement_officials.htm` |
| ★ County environmental health programs (who approves your septic/well) | `https://www.health.ny.gov/environmental/water/drinking/ctyadd1.htm` |
| DOH district offices (counties without a full-service health department) | `https://www.health.ny.gov/environmental/water/drinking/distphn.htm` |
| Interactive map of the above | `https://www.health.ny.gov/environmental/water/drinking/doh_pub_contacts_map.htm` |
| 10 NYCRR § 128-3.8 (NYC watershed septic) | `https://regs.health.ny.gov/content/section-128-38-subsurface-sewage-treatment-systems` |
| DOH radon program | `https://www.health.ny.gov/environmental/radon/` |

### Everything else

| What | URL |
|---|---|
| ★ DEC registered water well contractor search | `https://appfactory.dec.ny.gov/WaterWell/Contractor_Search` |
| DEC Water Well Consumer Protection Guide (PDF) | `https://extapps.dec.ny.gov/docs/water_pdf/wwpbrochur15.pdf` |
| WCB permit/license requirements sheet (forms C-105.2, DB-120.1, CE-200) | `https://www.wcb.ny.gov/content/main/Employers/requirements-businesses-applying-government-permits-licenses-contracts.pdf` |
| WCB CE-200 step-by-step (PDF) | `https://www.wcb.ny.gov/content/ebiz/wc_db_exemptions/How-to-Obtain-Certificate-of-Exemption.pdf` |
| Adirondack Park Agency — laws and permitting | `https://apa.ny.gov/permitting/laws.html` |
| NYC DEP watershed regulations and maps | `https://www.nyc.gov/site/dep/environment/regulations.page` |
| 2025 ECCCNYS free viewer | `https://codes.iccsafe.org/content/NYSECC2025P1` |
| NYSERDA NYStretch (2020 edition) | `https://www.nyserda.ny.gov/All-Programs/Clean-Resilient-Building-Codes/NYStretch-Energy-Code-2020` |
| ASCE 7 Hazard Tool (ground snow load geodatabase, Figure R301.2(3) Note 1) | `https://asce7hazardtool.online/` |
| FEMA Flood Map Service Center | `https://msc.fema.gov/portal/home` |
| *Mulhern Gas* — 2d Cir. docket (mandate, rehearing) | `https://www.courtlistener.com/docket/71197226/mulhern-gas-co-inc-v-mosley/` |
| *Mulhern Gas* — N.D.N.Y. docket; Stipulation and Order Dkt. 75 | `https://www.courtlistener.com/docket/67877190/mulhern-gas-co-inc-v-mosley/`; `https://storage.courtlistener.com/recap/gov.uscourts.nynd.140479/gov.uscourts.nynd.140479.75.0_1.pdf` |
| Suffolk County home-improvement law (§ 563) | `https://www.suffolkcountyny.gov/Portals/0/formsdocs/consumeraffairs/CA-L01a_Home_Improvement_License_Law.pdf` |
| Nassau County local law text (§ 21-11) | `https://www.nassaucountyny.gov/DocumentCenter/View/11095` |
| Putnam County Code Ch. 135 | `https://putnamcountyny.gov/images/Departments/Consumer_Affairs/PDF_Documents/homeimprovement/Chapter_135.pdf` |
| NYCRR (official compilation on Westlaw — **stale for Parts 1219–1229, 1240**) | `https://govt.westlaw.com/nycrr/Index` |

**Dead or blocked, do not print:** `ecode360.com` (Putnam/Rockland/Suffolk
chapters — 403 to every fetcher); `library.municode.com` (Westchester);
`dec.ny.gov/environmental-protection/water/water-quality/water-well-program`
(404 — the live page is `…/water-quantity/water-well-contractor-program`);
`wcb.ny.gov/content/main/Employers/certificate-attestation-exemption-ce-200.jsp`
(404); `www.ny.gov/services/certificates-attestation-exemption-ce-200` (403 to
curl; use the WCB page).

---

## 12. LIVE GUIDE AUDIT — `src/app/permitting/state-guides/new-york/page.mdx`

615 lines, "Last updated: May 2026." The MDX pipeline has no heading ids —
**never propose in-page anchors.** Line numbers are from the September 2026
read. NYC content (lines 89–91, 227–244, 494, 515, 566) is out of scope for
the kit and is not audited here except where a claim is plainly unverified.

### 12.1 Wrong

| Line | Guide text (quoted) | Correction | Cite |
|---|---|---|---|
| 64, 615 | "the exact NEC edition and any local electrical-license rule vary … Confirm the NEC edition with your building department" / "The exact NEC edition … vary by jurisdiction" | The edition does not vary. The 2025 RCNYS Electrical Part "is based on the 2023 National Electrical Code® (NEC®) (NFPA 70®—2023)"; anything not covered "shall comply with the applicable provisions of NFPA 70." Local *licensing* varies; the code does not. | 2025 RCNYS Ch. 34 header; E3401.2 |
| 296 | "Ceiling / attic insulation … R-49, R-49, **R-60**" | R-49 in all three zones. | [NY] Table R402.1.3 |
| 299 | "Windows (U-factor) U-0.30 max" (all zones) | **U-0.27**; 0.30 only above 4,000 ft or in windborne-debris regions, Zones 5–6. | [NY] Table R402.1.3 note g |
| 300 | "Air leakage … on the order of 3 ACH50" | 3.0 ACH in Zones 4–5; **2.5 ACH in Zone 6**; ≤1,500 sq ft may use 0.27 cfm/sq ft. | [NY] R402.5.1.3 |
| 298 | "Minimum wall cavity (R-value alternative) R-13 minimum" | No such row exists in the New York table. Delete. | [NY] Table R402.1.3 |
| 290 | "4A (New York City and Long Island), 5A (most of the state …), 6A (the Adirondacks, North Country, and Tug Hill). NYSERDA publishes a climate-zone-by-county table." | The county table is **in the code**, [NY] Table R301.1(1). Zone 4 includes **Westchester**. Zone 6 includes **Ulster, Sullivan, Delaware, Otsego, Chenango, Madison, Montgomery, Fulton, Herkimer, Oneida** as well as the North Country. | 2025 ECCCNYS [NY] Table R301.1(1) |
| 312, 586 | "starting January 1, 2026 … suspend the January 1, 2026 effective date until the Second Circuit Court of Appeals rules on the appeal" | Statute and rule date is **December 31, 2025** for a "substantially complete building permit application … submitted on or after" that date. The stipulation suspends until **120 days after the mandate** (or after certiorari disposition), not until the ruling. Second Circuit affirmed 30 June 2026; rehearing denied 26 August 2026; **mandate issued 2 September 2026 → 31 December 2026** absent a certiorari petition (due ~24 November 2026). DOS: still "neither effective nor enforceable" as of its 2 July 2026 update. | Exec. Law § 378(19); 19 NYCRR § 1229-2.4; Stip. & Order Dkt. 75 ¶¶ 2, 4; 2d Cir. 25-2041 docket |
| 393, 590 | "in Lewis County the codes office has stated the highest load they can approve as officials is 70 psf, and the 2025 code is pushing many properties above that" | 70 psf is the **statewide code threshold** in R301.2.3, above which "accepted engineering practice" (engineered design) is required. It is not a Lewis County policy. | 2025 RCNYS [NY] R301.2.3 |
| 97, 393 | "The code uses Figure 1608.2 ground-snow values" | For a house the RCNYS uses the larger of **Figures R301.2(3) and R301.2(4)** (or BCNYS § 1608). Figure 1608.2(5) is the BCNYS map. | [NY] R301.2.3 |
| 100, 367, 594 | "The radon appendix … is optional — individual towns must adopt it. Towns such as Caledonia, Lima, and Georgetown have." | Appendix BE is "included for informational purposes" — **not adopted**. A town cannot simply "adopt" it; under Executive Law § 379 a more-restrictive local standard takes effect only after the Code Council approves it. The three town names are unsourced — delete unless found on the Code Council's approved list. | [NY] R101.2.1; Exec. Law § 379(1)–(2) |
| 171 | "Labor Law §240/§241 ('Scaffold Law') imposes strict liability for gravity-related worker injuries, which is a real exposure if you pay laborers" | § 240(1) excepts "owners of one and two-family dwellings who contract for but do not direct or control the work." Print the exemption and the direct-or-control caveat. | Labor Law § 240(1) |
| 62 | "2025 Energy Conservation Construction Code of NYS (ECCCNYS) — 2024 IECC + ASHRAE 90.1-2022" | ASHRAE 90.1 is the commercial standard and irrelevant to a house; the edition claim was not verified (DOS documents refer to a "NYS ASHRAE 90.1-2025" with a replaced Appendix G). Delete the ASHRAE clause. | DOS 2026-1 |
| 99, 413 | "New York amended the code to require coastal communities to regulate the Coastal A Zone to the tougher VE-zone standards" | Not found in the 2025 RCNYS. What is verified: [NY] R306.1 applies flood-resistant construction in "A Zones, **shaded X Zones, B Zones**, Coastal A Zones, and V Zones," and floodways go to ASCE 24. Replace. | [NY] R306.1; Exec. Law § 378(1-a) |
| 420 | "where the basic design wind speed reaches 140 mph, impact-rated (or shuttered) glazing is required" | 140 mph is the "wind design required" threshold in a special wind region (R301.2.1.1). Opening protection applies in the windborne-debris zone the AHJ enters in Table R301.2 (R301.2.1.2, note m). Rewrite. | [NY] R301.2 note m; R301.2.1.1; R301.2.1.2 |

### 12.2 "Varies locally" hedges on rules that are statewide

| Line | Guide text | The statewide rule |
|---|---|---|
| 30 | "Can a homeowner pull their own permit — Yes in most upstate jurisdictions … (deed/affidavit/survey typical)" | Anyone may apply; the statewide gate is **GML § 125**: carrier proof of workers' comp and disability coverage **or** an affidavit of no employees (Form CE-200, "Apply as a Homeowner," job-specific). Plus the § 1203.3(a)(2)–(3) application contents (tax map number, site plan "drawn in accordance with an accurate boundary survey"). |
| 31, 152, 517, 570 | "Varies by locality … third-party electrical inspection (e.g., a NY electrical inspection agency) required" | Statewide: E3403.2 requires inspection of new electrical work; § 1203.2(e)(4) makes it a **special inspection** that the AHJ may accept only from an agency **it has approved**. Whether the *homeowner may do the wiring* is local licensing. Add [NY] E3401.2.1: an owner-occupied one-family dwelling need not have electrical service at all. |
| 337, 359 | "Standard New York inspection schedule (typical; exact list set locally)" / "Expect 10–14 inspections" | The floor is statewide: § 1203.3(b)(1) lists eleven elements (pre-permit site, footing and foundation, slab prep, framing, all service systems incl. electrical, fire-resistant construction, penetrations, solid-fuel appliances/chimneys, energy items, factory-built, final). Local law may add. |
| 328–330 | "Frost depth is a local call … 42–48 inches" | Correct that it is local — but the *reason* is [NY] Table R301.2 note b: "The authority having jurisdiction shall fill in the frost line depth column." Print the rule, delete the inch figures. |
| 264–280 | Processing-time tables | No review clock exists in Article 18 or Part 1203. What exists: a **Part 1205 appeal** to a regional board of review for "the failure of an administrative official to make an order or determination within a reasonable amount of time," decided within 60 days. |
| 306 | "an updated NYStretch is being published to pair with the 2025 code" | NYSERDA's page still offers NYStretch-2020 and says only that updates are "planned." Delete the town list and the "10–12%" figure; keep the concept with the NYSERDA link. |

### 12.3 Unsupported numbers (delete or source each to a dated fee schedule)

Lines 198–202 (Albany "$450," Bethlehem "$448/$748," county ranges); 208
("Town of Ulster … roughly $4,000 per new dwelling unit"); 218–221 (Long
Island fee ranges and "$62.50 CO fee"); 252–258 (tap fees, recreation fees,
septic/well/SWPPP/blower-door costs); 274–278 (weeks); 322–324 (frost inches);
365 (Zone 1 county list); 377, 594 ("$400–$900"); 397 ("60–90 psf … 20–30
psf"); 401 (PE county list); 438–441, 453–455 (septic and well costs); 519,
582 (fee restatements). Also line 39 "roughly 1,600 local governments" and
line 48/77 "a handful/a few rural towns" opt out — unsourced counts.

### 12.4 Third-party sources cited as authority (replace with primary)

- Line 146: nyeia.com (a private inspection agency) for "most municipalities
  allow anyone to perform electrical work" — delete the generalization; cite
  DOS FAQ, § 1203.2(e)(4), E3403.2.
- Line 111: Attorney General home-improvement fact sheet — replace with GBL
  §§ 770–771 and Lien Law § 71-a directly (and note "custom home" is inside
  GBL Article 36-A).
- Line 180: Property Condition Disclosure Act statements (2024 amendment,
  "$500 credit") — not verified this session; either verify RPL Art. 14 or
  cut. Add the verified conveyance rule instead: Executive Law § 378(5-b)(e)
  smoke-alarm affidavit at closing.

### 12.5 Material omissions

1. **GML § 125 / WCL § 57 / Form CE-200** — the actual permit gate.
2. **[NY] E3401.2.1** — owner-occupied one-family dwellings need no
   electrical system.
3. **Stamped plans above 1,500 sq ft gross** (Ed. Law §§ 7307(5), 7209(7)(b);
   [NY] R106.6).
4. **Part 1205 appeal** to a regional board of review, 60-day decision; DOS
   complaint forms for officials.
5. **§ 1203.5 30-day order to remedy** and **§ 382(2) $1,000/day** penalty
   naming "any owner, builder."
6. **[NY] R115** — separate permit and certificate of compliance for any
   solid-fuel appliance, chimney or flue before it may be operated.
7. **Appendix BB Tiny Houses is adopted**; strawbale/cob/hempcrete are
   informational (alternative-method approval, R104.2.2).
8. **[NY] R309.2** — sprinklers required only at three stories above grade
   plane; **[NY] R310.2.1** heat detection in new attached garages.
9. **10 NYCRR § 75.5(b)** — septic plans "shall be prepared directly by or
   under the supervision of a design professional"; Appendix 75-A Table 2
   distances and 110 gpd/bedroom; **[NY] P2602.1.1** — wells must be drilled
   by a DEC-registered driller (no DIY well), Appendix 5-B Table 1.
10. **APA § 806 shoreline setbacks** (50/75/100 ft; 100 ft for the leach
    field) and § 810 single-family-dwelling permit triggers; **NYC watershed
    § 128-3.8** (DEP approval; 100 ft/300 ft).
11. **GBL §§ 770–771 and Lien Law § 71-a** — a contractor building a custom
    home on the owner's lot owes a written contract with the § 771 contents
    and must escrow or bond payments.
12. **ECCCNYS R401.3 certificate** and the CO precondition of the written
    blower-door report (§ 1203.3(d)(2)(iv)).
13. **§ 381(1)**: no periodic inspections of owner-occupied one- and
    two-family dwellings.
14. **Executive Law § 383(1)(c)** as the statutory basis of the NYC
    carve-out (the guide says "home-rule authority").
15. **19 NYCRR Part 1202** — where DOS is the AHJ the application must be
    signed by the owner *and* the landowner, and the owner supplies the
    climatic design criteria (§ 1202.12).
16. The **2020→2025 option period closed 30 December 2025**; Westlaw's NYCRR
    is stale; the code is the regulation plus the book (DOS 2026-1).
