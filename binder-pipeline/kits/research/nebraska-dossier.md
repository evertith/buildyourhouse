# Nebraska Owner-Builder Permit Kit — Research Dossier

Kit 24 of the 50-state program (phase 5, with ID, AZ, NY). Compiled September
2026 for `binder-pipeline/kits/ne-permit-kit/` (NE.0–NE.5).

**Marking convention.** `[V]` = read in a primary source and quoted here.
`[H]` = secondary, inferred, or reasoned — not printed in the kit as a
citation. Anything unverifiable was deleted rather than softened.

**Primary sources used.**

| Source | What it is | Where |
|---|---|---|
| Neb. Rev. Stat. §§ 71-6401 to 71-6409 | Nebraska State Building Code (adopts IBC/IRC) | nebraskalegislature.gov/laws/statutes.php?statute=71-64xx |
| Neb. Rev. Stat. §§ 81-1608 to 81-1626 | Nebraska Energy Code | nebraskalegislature.gov |
| Neb. Rev. Stat. §§ 48-2101 to 48-2117 | Contractor Registration Act (Dept. of Labor) | nebraskalegislature.gov |
| Neb. Rev. Stat. §§ 81-2101 et seq. | State Electrical Act (State Electrical Division) | nebraskalegislature.gov |
| Neb. Rev. Stat. §§ 46-1201 et seq. | Water Well Standards and Contractors' Practice Act | nebraskalegislature.gov |
| Neb. Rev. Stat. §§ 46-602, 46-606 | Water well registration and fees (DWEE) | nebraskalegislature.gov |
| Neb. Rev. Stat. §§ 81-15,244 to 81-15,253 | Private Onsite Wastewater Treatment System Contractors Certification and System Registration Act | nebraskalegislature.gov |
| Neb. Rev. Stat. §§ 76-3501 to 76-3508 | Radon Resistant New Construction Act | nebraskalegislature.gov |
| Neb. Rev. Stat. §§ 18-132, 18-1901–1906, 23-114–23-114.05, 23-172, 14-419, 15-905 | City/county code adoption, plumbing boards, county zoning permits | nebraskalegislature.gov |
| Neb. Rev. Stat. §§ 52-125 et seq.; 48-106, 48-115, 48-116; 76-2,120; 76-2321 | Construction liens, workers' comp, seller disclosure, One-Call | nebraskalegislature.gov |
| Laws 2026, LB889 (slip law); LB441 (via § 71-6409) | 2026 amendments read in the bill text | nebraskalegislature.gov/FloorDocs/109/PDF/Slip/ |
| NDEE Title 124 (eff. 6-27-2022) + General Permit GTS220000 booklet (form 23-017 ver. 02.2026) | Onsite wastewater rules, Table 2.1 setbacks, septic sizing | dwee.nebraska.gov / dee.nebraska.gov PDFs |
| **DWEE Title 134 NAC ch. 1 and 4 (eff. 6-28-2026)** | Water well licensure and construction standards (**supersedes Title 178 ch. 12**) | dwee.nebraska.gov/sites/default/files/water/ |
| State Electrical Division pages, Board Rules (4-23-24), Application for State Electrical Inspection (3-27-26), Homeowner Handout (5-22-24), NSED GIS layer | Agency practice, fees, inspection jurisdictions | electrical.nebraska.gov; gis.ne.gov |
| DWEE energy-code page and Residential Energy Code Fact Sheet; Energy Impact Study 2018/2021 | Energy code practice, climate zone | dwee.nebraska.gov |
| DHHS report to the Legislature under § 76-3507 (Jan 1, 2024; data Oct 2018–Sep 2023); DHHS RRNC Requirements | County radon averages, exempt counties | nebraskalegislature.gov FloorDocs; dhhs.ne.gov |
| Dept. of Labor Contractor Registration page and search | Registration fee, registry | dol.nebraska.gov/conreg |
| City of Lincoln Building & Safety pages (codes; homeowner plumbing/mechanical/electrical) | Lincoln editions and homeowner conditions | lincoln.ne.gov |
| Sarpy County Resolution 2024-150 | Unincorporated Sarpy code editions | sarpy.gov DocumentCenter |

> **Fetching note for future revisions.** `nebraskalegislature.gov` serves
> every section as **HTML** at
> `https://nebraskalegislature.gov/laws/statutes.php?statute=71-6403` (a
> default curl works; a browser User-Agent was used anyway). Sections with a
> comma in the number use the comma literally: `statute=81-15,247`. Each page
> prints a **Source** line naming every session law that amended it and, when
> the amendment is recent, an **"Effective Date:"** line — this is the only
> reliable repeal/amendment tripwire, so always read it. The full chapter index
> (`browse-chapters.php?chapter=81`) is a 2.5 MB page that lists every section
> with "Repealed. Laws YYYY" where applicable — use it to find dead sections
> before citing. NDEE/DWEE rule titles are PDFs at
> `https://dwee.nebraska.gov/sites/default/files/titles/Title%20124%20Effective%2006-27-2022.pdf`
> (text extracts cleanly with `pdftotext -layout`). The old
> `www.nebraska.gov/nesos/rules-and-regs/...` paths **redirect to
> `rules.nebraska.gov`** and return an 803-byte HTML stub, not the PDF.
> `dee.ne.gov` does not resolve at all. State Electrical Division pages at
> `electrical.nebraska.gov` are Drupal HTML and return 200 to a plain curl;
> `/permits`, `/fees`, `/inspections` are 404 — the live paths are listed in
> § 11. **Omaha (`planning.omaha.gov`, `permits.cityofomaha.org`) and Douglas
> County (`dceservices.org`) are behind Akamai and returned 403 to curl, to
> WebFetch, and to a real Chrome session ("This service is not available in
> your region").** Nothing Omaha-specific in this dossier is verified from
> Omaha's own pages; see § 8. `lincoln.ne.gov` 403s curl but WebFetch works.
> Statute pages for LB-amended sections carry the **new** text plus an
> "Effective Date" line; the slip law is the only way to see what changed.

---

## 0. THE HEADLINE — WHAT MAKES THIS KIT DIFFERENT

Nebraska is the Kentucky pattern with a Montana-style electrical program
bolted on: **the code is mandatory everywhere and the building permit is
optional everywhere**, and what actually reaches a rural house is the **state
electrical inspector, the power company, and the septic installer's
certificate** — not a building official.

Seven findings carry the kit:

1. **The 2018 IRC (plus the 2018 UPC) is "the legally applicable code
   regardless of whether the county, city, or village has provided for the
   administration or enforcement."** `[V]` § 71-6406(7). No county may run an
   older edition (§ 71-6406(3)(a)). Nobody has to inspect. Nothing lets the
   state inspect a private house.
2. **A new house is state-inspected for electrical everywhere a local program
   does not exist, and the utility may not connect it without the owner's
   certificate that inspection was requested.** `[V]` §§ 81-2124(3), 81-2129.
   The homeowner exemption is a **licence** exemption only (§ 81-2121(5)).
3. **As of July 18, 2026, failing to file the electrical request for
   inspection is a Class IV felony** — LB889 raised it from a Class I
   misdemeanor. `[V]` § 81-2143(1)(c). The SED's own 2024 rules still say
   "misdemeanor."
4. **The energy code is enforced by the builder's own duty**: with no local
   energy code, "the prime contractor shall build … to the best of his or her
   knowledge, according to the Nebraska Energy Code," with a two-year
   post-occupancy correction window and a Class IV misdemeanor. `[V]`
   §§ 81-1622, 81-1625, 81-1626. An owner-builder is the "contractor"
   (§ 81-1609(2)).
5. **You may drill your own well on your own homestead; you may NOT install
   your own septic system.** `[V]` § 46-1233(2) versus § 81-15,248(1) and
   Title 124 ch. 9 § 004 ("physically present at the site").
6. **Radon-resistant construction is statewide by statute — except for any
   architect- or engineer-designed house and for 14 low-radon counties.**
   `[V]` § 76-3505(1)–(2); DHHS county table.
7. **The Contractor Registration Act is a $40 registration, not a licence,
   and an owner working on their own property "is not a contractor."** `[V]`
   § 48-2104(1). Every hired trade must be in the DOL registry, which shows
   whether they carry workers' comp — the fact that decides the owner's
   § 48-116 exposure.

Two hard numbers the kit prints with a retrieval date: **five counties and
fourteen cities** run their own electrical inspection programs (everyone else
is state-inspected; SED GIS layer, September 2026), and **77 of 93 counties**
exceed the 2.7 pCi/L radon threshold (DHHS, data through September 2023).

---

## 1. THE CENTRAL THESIS — WHO ENFORCES

### 1.1 The state building code is 2018 I-Codes plus the UPC, by statute `[V]`

**Neb. Rev. Stat. § 71-6403(1)**, verbatim: "There is hereby created the state
building code. The Legislature hereby adopts by reference: (a) The
International Building Code (IBC), 2018 edition, except section 101.4.3 and
chapter 29 … (b) The International Residential Code (IRC), 2018 edition,
**except section R313 and chapters 25 through 33**, published by the
International Code Council; (c) The International Existing Building Code, 2018
edition, except section 809 …; and (d) **The Uniform Plumbing Code, 2018
edition**, designated by the American National Standards Institute as an
American National Standard."

**§ 71-6403(2)**: those codes "and the minimum standards for radon resistant
new construction adopted under section 76-3504 shall constitute the state
building code except as amended pursuant to the Building Construction Act or
as otherwise authorized by state law."

Source line ends "Laws 2021, LB131, § 21" — **no edition change since 2021**.
Read September 2026. The 2018 editions are current.

Two things fall out of the text that the published guide gets wrong:

- **IRC chapters 25–33 are the IRC plumbing chapters.** They are excluded
  because Nebraska adopted the **2018 Uniform Plumbing Code (IAPMO), not the
  IPC and not the IRC plumbing chapters**, as the plumbing component of the
  state code. Where the state code applies, the plumbing standard is the UPC.
- **R313 (sprinklers) is excluded from the state code, but § 71-6406(2)(c)(iii)
  expressly lets a local government adopt it** and still "conform generally."
  There is **no statutory prohibition on a local residential sprinkler
  mandate** in this Act. See § 3.5.

### 1.2 Where the state code applies — § 71-6404(2) `[V]`

"The state building code shall be the building and construction standard
within the state and shall be applicable:
(a) To all buildings and structures owned by the state or any state agency;
(b) In each county, city, or village which elects to adopt the state building
code as its local building or construction code pursuant to section 71-6406;
and
(c) In each county, city, or village **which has not adopted a local building
or construction code pursuant to section 71-6406 within two years after an
update to the state building code**."

### 1.3 The local-option mechanism — § 71-6406 `[V]`

**§ 71-6406(1)(a)**: a county, city or village "may enact, administer, or
enforce a local building or construction code if or as long as" it "(i) Adopts
the state building code; or (ii) Adopts a building or construction code that
conforms generally with the state building code."

**§ 71-6406(1)(b)** — the default: "If a county, city, or village does not
adopt a code as authorized under subdivision (a) of this subsection within two
years after an update to the state building code, **the state building code
shall apply in the county, city, or village, except that such code shall not
apply to construction on a farm or for farm purposes.**"

**"Conforms generally"** (§ 71-6406(2)) is broad: a local code conforms if it
amends, modifies or deletes portions "to reduce unnecessary costs of
construction, increase safety, durability, or efficiency, establish best
building or construction practices … or address special local conditions"
(2)(a); adopts newer editions or appendices (2)(b); adopts R313 or IRC ch.
25–33 (2)(c)(iii); adopts a plumbing, electrical, fire or other standard code
under §§ 14-419, 15-905, 18-132 or 23-172 (2)(d); adopts a local energy code
under § 81-1618 (2)(e); or adopts RRNC standards meeting § 76-3504 (2)(f).

**A local code does NOT conform** (§ 71-6406(3)) if it "(a) Includes a prior
edition of any component … of the state building code; or (b) Does not
include minimum standards for radon resistant new construction that meet the
minimum standards adopted under section 76-3504." **A local government may
not lawfully run on the 2015 or 2012 IRC.** § 71-6406(5): "A county, city, or
village shall not adopt or enforce a local building or construction code other
than as provided by this section." § 71-6406(6): must "regularly update" —
adopt within two years of a state update.

### 1.4 The Nebraska inversion — the code binds whether or not anyone enforces it `[V]`

**§ 71-6406(7), last sentence, verbatim:** "Any local building or construction
code adopted under subdivision (1)(a) of this section **or the state building
code if applicable under subdivision (1)(b) of this section shall be the
legally applicable code regardless of whether the county, city, or village
has provided for the administration or enforcement of its local building or
construction code under this subsection.**"

The same subsection makes administration optional: a local government "may
adopt amendments for the proper administration and enforcement of its local
building or construction code including organization of enforcement,
qualifications of staff members, examination of plans, inspections, appeals,
permits, and fees" — *may*, not *shall*. **Nothing in the Building
Construction Act requires any county, city or village to issue building
permits or conduct inspections, and nothing gives any state agency authority
to do so for a private house.** § 71-6405(1) applies the code "regardless of
whether … [anyone] has provided for the administration or enforcement" only to
**state-owned** buildings; the state has no residential permit program.

**Result** (this is the kit's thesis, and it is the Kentucky pattern):
outside the cities and counties that chose to run a program, the 2018 IRC +
2018 UPC + RRNC standards are the law of your house, and **nobody issues a
permit, reviews a plan, or inspects** — with two statewide exceptions that
survive everywhere: the **state electrical inspection** (§ 3.3) and the
**energy code** (§ 3.4). Both are enforced by mechanisms that do not depend on a
county building department.

### 1.5 Farm exemption — statutory, and it means what it says `[V]`

§ 71-6406(1)(b): the state-code default "shall not apply to construction on a
farm or for farm purposes." § 71-6407: "Nothing in the Building Construction
Act shall be construed to authorize any state agency or political subdivision
to regulate the construction of farm buildings or other buildings or
structures when such regulation is otherwise prohibited by law."

The farm carve-out is written into the **default** path only. A county or
city that adopts its own code under (1)(a) is not, by this section, forbidden
from reaching farm construction — the limit for local zoning of farm
buildings lives in the county zoning statutes (see § 2.3). The words "on a
farm or for farm purposes" are not defined in the Act. **The kit prints the
exemption verbatim and tells the reader not to rely on it for a farmhouse
without the county's written agreement**, because a dwelling is a residence
first and a farm building second.

### 1.6 § 71-6409 — virtual inspections and the self-inspection bar (NEW, 2026) `[V]`

Laws 2026, LB441, § 2, **effective July 18, 2026**, added § 71-6409. It lets
any permitting entity "allow for virtual inspection by an authorized
inspector" of a one- or two-family dwelling under three stories and under
10,000 sq ft, conducted live with the permit holder, if "the individual
requesting or holding the building permit has provided the name of the
contractor who is licensed or registered in such state, county, city, or
village and who is completing the work to be virtually inspected."
Nonstructural reinspections may use video or photo documentation.

Two consequences for the owner-builder:

- **"Authorized inspector does not include an individual performing a
  self-performed inspection for the individual's own permit or building."**
  Whatever else a county offers, it may not let you inspect yourself.
- The virtual path is conditioned on naming a licensed/registered contractor
  "who is completing the work." Whether an owner doing the work personally can
  use it is not addressed by the text. See § 8, open question.

### 1.7 How many jurisdictions run a program — what can and cannot be counted

**Electrical — HARD NUMBER `[V]`.** The State Electrical Division publishes a
GIS layer of inspection jurisdictions (`NSED_Inspector_Programs`, queried
September 2026, 43 features). Every feature not listed below is "State of
Nebraska":

| Level | Own electrical inspection program (§ 81-2125) |
|---|---|
| **Counties (5 of 93)** | **Lancaster, Hall, Dodge, Douglas, Sarpy** |
| **Cities (14)** | Lincoln, Omaha, Bellevue, Papillion, Gretna, Ralston, Grand Island, Hastings, Kearney, Fremont, Norfolk, York, South Sioux City (also covering Jackson and Homer villages), Hickman |

Traps inside the metro: **La Vista** (Sarpy County) and **Waverly**
(Lancaster County) are explicitly **state**-inspected despite their
neighbours. The kit tells the reader to look the parcel up on the SED map
rather than assume from the county.

**Building permits — NO HARD NUMBER EXISTS `[V]` (verified absence).** No
state agency publishes which of the 93 counties issue building permits,
because no statute requires one to: § 71-6406(7) makes administration
optional, § 23-172 lets a county adopt a code by resolution, and § 23-114.04
lets a county require **zoning** permits for "any nonfarm building" whether or
not it has a building code. The Legislature's own conformity mechanism runs
through DWEE only for energy-chapter deletions (§ 71-6406(4)). The kit prints
the verification step instead of a number: (1) county clerk — is there a
resolution under § 23-172 adopting a building code, and a zoning resolution
under § 23-114 requiring permits? (2) if inside a city or its extraterritorial
zoning jurisdiction, the city clerk, because county codes "shall apply to all
of the county except within the limits of any incorporated city or village
and except within an unincorporated area where a city or village has been
granted zoning jurisdiction" (§ 23-172(5)). (3) the SED map for electrical.

### 1.8 The two big cities — Omaha and Lincoln

**Lincoln `[V]` (city's own pages, September 2026).** Building & Safety's
codes page lists: **IBC 2021, IRC 2021, UPC 2021, IMC 2021, NEC 2023, IECC
2018, IFGC 2021, IEBC 2021**, each "& Local Amendments" (in LMC Title 20–25
via encodeplus). Lincoln is therefore **ahead of the state code** — lawful
under § 71-6406(2)(b) ("any supplement, new edition"). Lincoln inspects its
own electrical (SED GIS: "City of Lincoln"; also Lancaster County). Homeowner
permits, verbatim from the plumbing, mechanical and electrical pages: "Only
the owner of the residence can apply for the permit." "You must presently
reside in the single-family dwelling or reside there after the construction
is complete." "The house cannot be in the process of being prepared for sale,
not a rental property, or for intended use for becoming a rental property."
"Permits are valid for 120 days from issuances." "The permit issued must be
inspected before any work is concealed and must also be inspected when the
installation of the work is completed." Electrical, Mechanical and Plumbing
permits "May only be issued to a licensed contractor or a homeowner for their
primary residence." Codes: LMC Title 23 (electricity, ch. 23.10), Title 24
(plumbing and sewers), Title 25 (heating). Building permit minimum fee $65
(homeowner page). Lincoln's plumbing board is optional by statute
(§ 18-1901(2), primary class "may").

**Omaha — statutory frame only `[V]`; city pages unreachable.** A city of the
metropolitan class **shall** have a plumbing board (§ 18-1901(1)) whose
plumbers are "licensed within such cities" (§ 18-1901(6)); the city may
regulate construction, "electric wiring, heating, plumbing, pipefitting" in
the city and its three-mile extraterritorial zoning jurisdiction, "except as
to construction on farms for farm purposes" (§ 14-419(1)–(2)); any building
code it adopts must conform under § 71-6406 (§ 14-419(4)). Omaha, Douglas
County and Ralston each run their own electrical inspection (SED GIS). **The
published guide's Omaha specifics — "Table 43-91," "plan review about 25%,"
"42-inch frost depth," "appointment with the Chief Electrical Inspector" — are
unverified and are not printed.** NE.4 lists Omaha's Planning Department
building-and-development page as the place to confirm the edition, fees and
homeowner conditions, and notes that the site is geo-restricted.

**Sarpy County (unincorporated) `[V]`** — Resolution 2024-150, adopted June 4,
2024, effective June 4, 2024: adopts the **2018 IBC, IRC, IPC, IMC, IFGC and
IECC** (ICC/ANSI A117.1-2009) for "the entire unincorporated area of Sarpy
County," replacing the 2012 codes, "as amended." Note **IPC, not UPC** —
allowed under § 71-6406(2)(d) via § 23-172. Sarpy County runs its own
electrical inspection (SED GIS); Bellevue, Papillion and Gretna run theirs;
**La Vista is state-inspected**.

---

## 2. SCOPE — WHAT IS OUTSIDE THE CODE

### 2.1 Statutory exclusions from the state building code `[V]`

- **Farm construction** — § 71-6406(1)(b) (default path only) and § 71-6407.
- **Manufactured homes and RVs** — § 71-6405(3): nothing in the Act applies to
  "manufactured homes or recreational vehicles regulated by the Uniform
  Standard Code for Manufactured Homes and Recreational Vehicles" (§ 71-4601
  et seq.) or "modular housing units regulated by the Nebraska Uniform
  Standards for Modular Housing Units Act" (§ 71-1555 et seq.). § 71-6407 adds
  the federal HUD-code preemption for manufactured homes.
- **IRC R313 and chapters 25–33** — carved out of the adopted text
  (§ 71-6403(1)(b)); plumbing is instead the 2018 UPC.
- **IBC 101.4.3 and chapter 29; IEBC § 809** — commercial-side carve-outs,
  listed for completeness.

### 2.2 No owner-builder exemption exists, because there is nothing to be exempt from `[V]`

The Building Construction Act contains no provision that treats a house built
by its owner differently, and Nebraska issues **no general contractor
license** — the Contractor Registration Act (§ 5.1) is a Department of Labor
**registration** for persons who do construction work *for others*. The
electrical homeowner exemption (§ 3.3, § 5.2) is the only owner-specific
provision in Nebraska law that reaches a house build.

### 2.3 Farm buildings under county zoning — and the farmhouse is NOT automatically exempt `[V]`

**§ 23-114.03**, verbatim: the county board may "regulate, restrict, or
prohibit the erection, construction, reconstruction, alteration, or use of
**nonfarm buildings** or structures." "**The county board may decide whether
buildings located on farmsteads used as residences shall be subject to such
county's zoning regulations and permit requirements.** For purposes of this
section and section 23-114.04, nonfarm buildings are all buildings except
those buildings utilized for agricultural purposes on a farmstead of twenty
acres or more which produces one thousand dollars or more of farm products
each year."

**§ 23-114.04(1)**: "The county board shall provide for enforcement of the
zoning regulations within its county by requiring the issuance of permits
prior to the erection, construction, reconstruction, alteration, repair, or
conversion of any nonfarm building or structure within a zoned area." (2): the
permit "shall not be issued unless the plans … including sanitation, plumbing
and sewage disposal, are filed in writing in the building inspector's office
and such plans fully conform to all zoning regulations." **§ 23-114.05**:
building "without having first obtained a permit" is a **Class III
misdemeanor**, each day a separate offense after notice.

Three consequences the kit prints:

1. The agricultural exemption is for buildings "utilized for agricultural
   purposes" on a **20-acre, $1,000-a-year** farmstead. A house is a
   residence; whether a farmstead residence needs a county permit is the
   **county's decision**, farm by farm. Ask the county in writing.
2. Even in a county with **no building code**, a **zoning permit** under
   § 23-114.04 may be required for the house and must show sanitation,
   plumbing and sewage disposal.
3. Cities regulate construction in their extraterritorial zoning jurisdiction
   (three miles for Omaha, § 14-419(1); Lincoln, § 15-905) "except as to
   construction on farms for farm purposes." A rural parcel near a city may
   be under city rules.

---

---

## 3. CODE EDITIONS AND AMENDMENTS

### 3.1 Editions in force `[V]` — 2018, by statute, unchanged since 2021

| Component | Edition | Carve-out | Cite |
|---|---|---|---|
| IRC | **2018** | R313; chapters 25–33 | § 71-6403(1)(b) |
| IBC | 2018 | § 101.4.3; ch. 29; §§ 305.2.3 and 310.4.1 modified to twelve-or-fewer | § 71-6403(1)(a) |
| IEBC | 2018 | § 809 | § 71-6403(1)(c) |
| **Uniform Plumbing Code** | **2018** | none stated | § 71-6403(1)(d) |
| RRNC minimum standards | per § 76-3504 | — | § 71-6403(2) |
| Energy | **2018 IECC** (separate act) | — | § 81-1609(9), § 81-1611 |
| Electrical | **2023 NEC** (separate act) | see § 3.3 | § 81-2104(5) |

**Amendment mechanism**: § 71-6403(2) says the code applies "except as amended
pursuant to the Building Construction Act or as otherwise authorized by state
law." The Act itself contains **no state amendment table** — there is no
Nebraska equivalent of Pennsylvania's § 403.21(a)(7). The only statutory
overlays are the refrigerant clause (§ 71-6408: no code provision may
prohibit an EPA-acceptable refrigerant under 42 U.S.C. 7671k as of 1 January
2023) and the RRNC standards. **Local amendments are where the substance
lives** (§ 71-6406(2)(a)), which is why Omaha and Lincoln differ from the
model code and each other.

**Update mechanism / tripwire**: editions are changed only by the Legislature
amending § 71-6403. The two-year local-adoption clock in §§ 71-6404(2)(c) and
71-6406(1)(b), (6) runs from "an update to the state building code." The last
update was 2019 (LB348/LB405, effective for the 2018 editions); the 2021
amendment (LB131) was a conforming change. **No 2021 or 2024 I-Code adoption
bill has passed as of September 2026** — verified by the Source line. Watch
the Legislature, not an agency.

### 3.2 Appendices and IRC chapter 11

The Act adopts the codes "by reference" with named exclusions and says nothing
about appendices. **No Nebraska statute adopts or excludes IRC appendices**;
whether Appendix F (radon) or any other appendix applies is therefore a local
question, except that RRNC is made mandatory by a separate statute
(§ 76-3504) and the local-code conformity test (§ 71-6406(3)(b)) — so the
radon result is the same everywhere regardless of Appendix F.

IRC chapter 11 (energy) is part of the adopted 2018 IRC. **§ 71-6406(4)**: a
local government "shall notify the Department of Water, Energy, and
Environment if it amends or modifies its local building or construction code
in such a way as to delete any portion of … chapter 11 of the 2018 edition of
the International Residential Code," within thirty days. The energy standard
that actually binds is the separate Nebraska Energy Code (§ 3.4), which the
2018 IRC ch. 11 mirrors.

### 3.3 ⚠ ELECTRICAL — the Nebraska trap is that the state inspects, the utility enforces, and the exemption is license-only `[V]`

**Edition — § 81-2104(5), verbatim:** the board "shall be governed by the
minimum standards set forth in the National Electrical Code issued and
adopted by the National Fire Protection Association beginning in the **2023
edition** of the National Electrical Code, Publication Number 70-2023,
**except that the minimum standards set forth in the 2017 edition of the
National Electrical Code shall apply for sections 210.8(A), 210.8(A)(3),
210.8(A)(5), 230.67(A), and 230.85.**"

What those five carve-backs mean for a house (the section numbers are the
NEC's own; the content description is `[H]` from general NEC knowledge and
the kit prints only the section numbers with "2017 text applies"):

| NEC section | Subject | Nebraska rule |
|---|---|---|
| 210.8(A) | dwelling-unit GFCI location list | 2017 list |
| 210.8(A)(3) | outdoor receptacles | 2017 text |
| 210.8(A)(5) | basement receptacles | 2017 text |
| 230.67(A) | service surge-protective device | 2017 (no such section — **not required**) |
| 230.85 | emergency disconnect at the service | 2017 (no such section — **not required**) |

Everything else is the 2023 NEC as published. **The SED's own page**
(`electrical.nebraska.gov/state-act-update-2023-code-adoption`): "Beginning
August 1st, 2024, the Nebraska State Electrical Division will be adopting the
NFPA 70 National Electric Code 2023." The kit prints **2023 NEC, effective
1 August 2024, § 81-2104(5)**, with the five-section 2017 carve-back.

**Who must be licensed — §§ 81-2106, 81-2108.** No person shall, **"for
another,"** plan, lay out, supervise, wire or install unless licensed as a
Class B electrical contractor, electrical contractor, Class A master, or (for
wiring) a journeyman employed by one. The words "for another" are the hinge.

**The homeowner exemption — § 81-2121(5), verbatim:** "Nothing in the State
Electrical Act shall be construed to: … (5) Prohibit an owner of property from
performing work on his or her principal residence, **if such residence is not
larger than a single-family dwelling**, or farm property, excluding commercial
or industrial installations or installations in public-use buildings or
facilities, **or require such owner to be licensed under the act**."

Read it exactly:

1. It is a **license** exemption. It says nothing about inspection or the
   permit. Inspection is governed by § 81-2124, separately.
2. "Principal residence … not larger than a single-family dwelling" — a
   duplex, a spec house, a rental, a second home are outside it. "Farm
   property" is a second, separate category.
3. It does **not** say "without compensation" and it does **not** say the
   owner must personally do the work. The published guide's "no compensation
   paid to or by another person" condition is **not in the statute** — see
   § 12. (The SED handout does require a signed "verification"; see below.)

> ⚠ **The SED handout misquotes its own statute.** The homeowner handout
> (`Homeowner Handout updated 5-22-24.rtf`) prints § 81-2121(5) as "performing
> work on his or her principal residence or/arm property" — dropping the
> "not larger than a single-family dwelling" limit and garbling "or farm."
> The statute controls. Print the statute.

**Inspection — § 81-2124, verbatim:** "(1) All new electrical installations
for commercial or industrial applications … and **any installation at the
request of the owner** shall be subject to the inspection and enforcement
provisions of the State Electrical Act. (2) All new electrical installations
for residential applications in excess of single-family residential
applications shall be subject to the inspection and enforcement provisions of
the act. **(3) All new electrical installations for single-family residential
applications requiring new electrical service equipment shall be subject to
the inspection and enforcement provisions of the act.**" A new house has new
service equipment. **A new house is inspected, everywhere, whoever wires it.**

**Where the state does NOT inspect — § 81-2125(1):** "State inspection shall
not apply within the jurisdiction of any county, city, or village which
provides by resolution or ordinance standards of electrical wiring … not less
than those prescribed by the board … and which further provides by resolution
or ordinance for the inspection of electrical installations within the limits
of such subdivision by a certified electrical inspector." Those subdivisions
must file their ordinances with the board (§ 81-2130) and may not charge a
state licensee a local license fee or exam (§ 81-2130). **The SED publishes a
GIS map of who inspects where** — see § 11. That map, not a phone call, is the
verification step.

**The request for inspection (the "permit") — § 81-2126, verbatim:** "At or
before commencement of any installation required to be inspected by the board,
**the licensee or owner making such installation shall submit to the board a
request for inspection**, on a form prescribed by the board, together with a
supervisory fee of fifty cents and the inspection fees required for such
installation. If the board becomes aware that a person has failed to file a
necessary request for inspection, the board shall send to such person a
written notification by certified mail to file such request within fourteen
days. **Any person filing a late request for inspection shall pay a
delinquent fee of two hundred fifty dollars.** Failure to file such request
within fourteen days shall result in submission of the matter to the county
attorney's office for action pursuant to section 81-2143." § 81-2135(2): fees
"shall be due and payable to the board at or before commencement of the
installation."

**The penalty — § 81-2143(1), as amended by Laws 2026, LB889, § 2, effective
July 18, 2026:** "It shall be a **Class IV felony** to knowingly and willfully
commit … (c) To fail to file a request for inspection when
required; (d) To interfere with or refuse entry to an inspector …; or (e) To
fail or neglect to comply with the act or any lawful rule, regulation, or
order of the board." Also (a) a false statement "in any … request for
inspection, certificate, or other … form" — which is what the homeowner
verification is.

> ⚠ **This penalty was a Class I misdemeanor until July 18, 2026.** LB889
> (approved by the Governor April 14, 2026; slip law read) struck "Class I
> misdemeanor" and inserted "Class IV felony," renumbered (1)–(5) as (a)–(e),
> and **added subsection (2)** (the family carve-out). The State Electrical
> Board Rules PDF dated 4-23-24 (Rule 13: "may be guilty of a misdemeanor under
> §81-2143") and any pre-2026 secondary source are now wrong. The kit prints
> the felony with the effective date.

**The meter chokepoint — § 81-2129, verbatim:** "No electrical installation
subject to inspection by the board shall be newly connected or reconnected for
use until there is filed with the electrical utility supplying power a
certificate of the property owner or licensed electrician directing the work
that inspection has been requested and that the conditions of the installation
are safe for energization. … **Any supplier may refuse service without
liability for such refusal until such conditions have been met.**" § 81-2133:
on inspection and approval "all liability upon any supplier of electrical
service for subsequent damage or loss arising from any installation shall be
terminated" — the utility's incentive to insist. The handout confirms
practice: "Temporary services WILL NOT be energized by the power company until
they receive authorization to do so from the State Electrical Inspector" and
for a new service "the State Electrical Division office will forward a copy to
the power supplier."

**The inspection clock — § 81-2134** (this is a genuine statutory
response-time, rare in this corpus): "(2) Where wiring is to be concealed, the
inspector must be notified within reasonable time to complete a rough-in
inspection prior to concealment, exclusive of Saturdays, Sundays, and
holidays. If wiring is concealed before rough-in inspection without adequate
notice having been given to the inspector, the person responsible for having
enclosed the wiring shall be responsible for all costs resulting from
uncovering and replacing the cover material. **(3) Inspections shall be made
within one week of the appropriate request.** When necessary, circuits may be
energized by the authorized installer prior to inspection but the installation
shall remain subject to condemnation and disconnection."

**Correction orders — § 81-2138:** for a non-dangerous defect the inspector
issues a correction order specifying "a date, not less than ten nor more than
seventeen calendar days from the date of the order, when a final inspection
shall be made"; uncorrected, a condemnation or disconnection order may follow.
Dangerous defects: immediate condemnation (§ 81-2136, unenergized) or
disconnection (§ 81-2137, energized). Appeal: §§ 81-2141–2142 (to the board,
via hearing officer).

**Inspection types the SED runs** (handout, `[V]` agency's own words):
Temporary Service; New Service; **Rough-In** ("must be approved by the
inspector before fiberglass insulation or drywall is installed"); **Final**;
Re-Inspection ("approximately fourteen working days to make the corrections").
Requests go to the inspector named on "the yellow wiring permit card"; each
inspector has a 24-hour voicemail line.

**The homeowner verification** (handout): "you will sign a verification so
stating" that you know the NEC and State Act requirements, "prior to a wiring
permit being issued to you." Form name: "Request for State Electrical
Inspection with Homeowner Verification." The online system launched **April
13, 2026** (Tyler Technologies platform); the handout still describes the
paper route to PO Box 95066, Lincoln. Homeowner permits in the new system
"must be linked by NSED Office Staff once you have registered an account."

**Family carve-out — § 81-2143(2)** `[V]`, printed for accuracy, **not as
permission**: "Subdivision (1)(b) of this section shall not be construed to
prohibit a person from performing electrical work for such person's parent,
stepparent, spouse, descendant, grandparent, brother, sister, cousin, uncle,
or aunt … without a license." This narrows only the **felony** for unlicensed
work "while claiming to have such license"; it does not amend § 81-2108's
license requirement, and the installation is still inspected under § 81-2124.
The kit does not tell a reader that a relative may wire the house. See § 8.

**Fees** — the handout's worked example is **pre-April-2026**: "The fee for a
200-amp service is $35.00 and each branch circuit (circuit-breaker) is $5.00
… $185.00." The SED announced "As of April 1, 2026 the permit fees have been
updated to reflect increases to some fees" and posted a new **Application for
State Electrical Inspection (rev. 3.27.26)**. Current schedule, read from that
form `[V]`:

| Item | Fee |
|---|---|
| NEW electrical service, 1–400 A | **$75** |
| Branch circuit or feeder (incl. extensions), each | **$10** |
| EXISTING service (regardless of size) | $50 |
| Reconnect | $75 |
| Approval notice (optional) | $6 |
| **Homeowner minimum permit fee** | **$100** |
| Minimum permit fee (general) | $50 |

Worked example for the kit (`[H]`, arithmetic on the `[V]` schedule): a new
house with a 200 A service and 30 branch circuits = $75 + 30 × $10 = **$310**.
Fees "WILL NOT BE REFUNDED OR TRANSFERRED" and are forfeited "IF APPLICATION
CONTAINS FALSE INFORMATION" (form text). The form's own fields: type of request
(Contractor / **Homeowner** / Utility Reconnect …), type of installation
(Single-Family Residence / other), description and location, owner, installer
and license, **power supplier name and address**, estimated completion date.

**Permit life** (State Electrical Board Rule 13, 4-23-24) `[V]`: void if work
not started within **five months** of issuance, or if no progress for five
consecutive months, after 14 days' written notice; extensions on "clear and
convincing proof of a practical hardship." Rule 13 also prescribes the
**doorknob-notice** procedure when an inspector cannot reach "a property owner
installing wiring pursuant to Sections 81-2121(5) and 81-2124" — two attempts,
then the application stays on file "subject to inspection."

**HVAC wiring is a licensed specialty** `[V]`: § 81-2102(17) "Special
electrician" includes "air conditioning and refrigeration installation" and
"well pump wiring"; the SED sells a "Heating/AC/Refrigeration" specialty
license. A homeowner wiring their own furnace or condenser is inside the
§ 81-2121(5) exemption; a hired HVAC installer wiring the unit is not, unless
so licensed. § 81-2121(7): a licensed pump installation contractor may wire
"pumps and pumping equipment at a water well location to the first control."

**Class B licenses are small-town only** `[V]`: § 81-2102(4)–(5) confine
Class B contractors and journeymen to residential work up to 400 A "in any
municipality which has a population of less than one hundred thousand" —
which excludes Omaha and Lincoln. Relevant when hiring: a Class B licensee
cannot lawfully wire a house inside either city.

### 3.4 Energy — the Nebraska Energy Code is the 2018 IECC, statewide, by statute `[V]`

| Rule | Text | Cite |
|---|---|---|
| Edition | "Nebraska Energy Code means the 2018 International Energy Conservation Code published by the International Code Council" | § 81-1609(9); adopted § 81-1611 |
| Applies to | "all new buildings, or renovations of or additions to any existing buildings, on which construction is initiated on or after **July 1, 2020**" | § 81-1614 |
| Residential building | "a building three stories or less that is used primarily as one or more dwelling units" | § 81-1609(5) |
| **Contractor** (the person the duties fall on) | "the person or entity responsible for the overall construction of any building" — **an owner-builder is the contractor** | § 81-1609(2) |
| Exemptions | <1 W/sq ft peak design energy; neither heated nor cooled; federally owned; manufactured home; modular unit; listed/eligible historic. **No exemption for a house, a farm dwelling, or an owner-built home.** | § 81-1615 |
| Local option | any county, city or village "may adopt and enforce a local energy code," deemed equivalent if it does not result in greater energy consumption; may set fees; may **waive a specific requirement when meeting it is not economically justified** after submitting its analysis to the department | § 81-1618 |
| Alternative standards | Director may by regulation approve equivalents "if the use of such alternative standards would not result in energy consumption greater than would result from the strict application of the Nebraska Energy Code" | § 81-1611 |
| Correction window | "within **two years** from the date a building is first occupied," the Director **or the local code authority** "may order the owner or prime contractor to take those actions necessary to bring the building into compliance"; owner keeps a civil action against the contractor/architect/engineer | § 81-1625 |
| Penalty | failure to comply, or directing another not to comply, is a **Class IV misdemeanor** | § 81-1626 |
| Inspection power | department and any local code authority may inspect "only after permission has been granted by the owner or occupant or after a warrant has been issued" | § 81-1617 |

**Enforcement where no local program exists — § 81-1622, verbatim** (this is
the Montana-style self-certification, and it is the answer to "who checks the
energy code in a county with no building department"):

> "Prior to the construction, renovation, or addition to any existing building
> after the dates specified in section 81-1614 the following requirements
> shall be met where a county, city, or village has not adopted a local energy
> code pursuant to section 81-1618: (1) When no architect or engineer is
> retained, **the prime contractor shall build or cause to be built, to the
> best of his or her knowledge, according to the Nebraska Energy Code**; and
> (2) When an architect or engineer is retained: (a) The architect or engineer
> shall place his or her state registration seal on all construction drawings
> which shall indicate that the design meets the Nebraska Energy Code and (b)
> the prime contractor responsible for the actual construction shall build or
> cause to be built in accordance with the construction documents prepared by
> the architect or engineer."

There is **no state energy permit, no state energy inspection on request of
the builder, and no certificate**. What exists: the department "may conduct
such inspections and investigations as are necessary" and **"a building owner
may submit a written request that the department undertake a
determination"** (§ 81-1616) — a post-construction complaint path, chargeable
at cost, appealable under the APA. The kit prints § 81-1622(1) as the
owner-builder's actual duty and § 81-1625's two-year window as the exposure.

**Prescriptive values `[V]`** — DWEE's Residential Energy Code Fact Sheet:
"The unamended 2018 IECC was adopted in Nebraska statewide on July 1, 2020."
Its quick-reference table: windows and doors U-0.30; skylights U-0.55; ceiling
R-49; wood-frame wall R-20 cavity or R-13+5; mass wall R-17 cavity / R-13
continuous; floor R-30; basement wall R-19 cavity / R-15 continuous;
slab-on-grade R-10 to 2 ft; crawl-space wall R-19 / R-15. Blower door
"less than 3 air changes per hour at 50 pascals." Duct leakage ≤ 4 CFM/100
sq ft (3 CFM without the air handler), not required when all ducts are inside
the thermal envelope. Whole-house mechanical ventilation required; Manual J
load calculations required. DWEE's compliance paths: REScheck or the
component table with no tradeoffs.

**Climate zone `[V]`** — DWEE's Energy Impact Study (2018 vs 2021 IECC): "The
climate zone map for Nebraska is unchanged between the 2018 and 2021 IECC,
both of which place **the entire state of Nebraska in a single climate zone
(5)**." The kit prints Zone 5 statewide on DWEE's authority.

**Enforcement where no local code, in DWEE's words `[V]`**: "If a local
jurisdiction has not adopted an energy code, the Nebraska Department of
Water, Energy, and Environment Planning and Aid Division will enforce the
code." Read with § 81-1622, "enforce" means the § 81-1616 determination on
request and the § 81-1625 order — not a permit or a routine inspection.

**Department**: "Department means the Department of Water, Energy, and
Environment" (§ 81-1609(1), as amended Laws 2025, LB317, § 452). The energy
office is DWEE; the former NDEE name persists on rule PDFs issued before 2025.
Energy-code page: `https://dwee.nebraska.gov/state-energy-information/energy-codes`
(HTTP 200, September 2026).

### 3.5 Fire sprinklers — no state mandate, no state prohibition `[V]`

§ 71-6403(1)(b) adopts the 2018 IRC "except section R313." § 71-6406(2)(c)(iii)
then lists "Section R313 or any portion of chapters 25 through 33 of the 2018
edition of the International Residential Code" among the things a local code
**may** adopt and still "conform generally." **Verified absence**: no section
of the Building Construction Act, of § 18-132, § 23-172, § 14-419 or § 15-905
forbids a local residential sprinkler requirement. The kit prints: no
statewide sprinkler requirement for one- and two-family dwellings; a city or
county may adopt R313; check the local amendments.

### 3.6 Radon — statewide by statute, with two exemptions the guide misses `[V]`

**§ 76-3504**: "Except as provided in section 76-3505, new construction built
after September 1, 2019, in the State of Nebraska that is intended to be
regularly occupied by people shall be built using radon resistant new
construction." § 71-6403(2) folds those minimum standards into the state
building code, and § 71-6406(3)(b) says a local code that lacks them does not
conform.

**The statutory minimum standards, verbatim list** (§ 76-3504(1)–(3)) — this
is what Nebraska requires, and it is **less** than IRC Appendix F:

- Sumps: a sump pit open to soil or terminating drain tile "shall be covered
  with a gasketed or otherwise sealed lid"; a suction-point sump lid "designed
  to accommodate the vent pipe"; a floor-drain sump lid "equipped with a
  trapped inlet."
- Passive subslab depressurization system in basement or slab-on-grade
  buildings: "A minimum three-inch diameter … ABS, PVC, or equivalent gas-tight
  pipe shall be embedded vertically into the subslab permeable material before
  the slab is cast. A 'T' fitting or equivalent method shall be used …" or
  inserted into an interior perimeter drain-tile loop or through a sealed sump
  cover; extended "up through the building floors and terminate at least
  twelve inches above the surface of the roof in a location at least ten feet
  away from any window or other opening … that is less than two feet below the
  exhaust point and ten feet from any window or other opening in adjoining or
  adjacent buildings"; separate vent pipes where interior footings divide the
  subslab material; every exposed interior vent pipe labelled "Radon Reduction
  System" on each floor and in accessible attics.
- Power source: "an electrical circuit terminated in an approved box shall be
  installed during construction in the attic or other anticipated location of
  vent pipe fans."

**Not in the statute** `[V]` (verified absence): any aggregate depth ("4
inches of clean aggregate"), any vapor retarder, any soil-gas membrane. Those
are IRC Appendix F practice. The kit prints the statute and labels the rest
as good practice.

**Exemptions — § 76-3505, verbatim**: "New construction after September 1,
2019, shall not be required to use radon resistant new construction if (1)
**the construction project utilizes the design of an architect or
professional engineer licensed under the Engineers and Architects Regulation
Act**, (2) the construction project is located in a county in which the
average radon concentration is less than two and seven-tenths picocuries per
liter of air as determined by the department pursuant to section 76-3507, or
(3) other than for any residential dwelling unit, a local building official
makes a determination …"

**The county list `[V]`** — DHHS report to the Clerk of the Legislature dated
January 1, 2024, under § 76-3507, pre-mitigation data October 1, 2018 to
September 30, 2023: **77 of 93 counties exceed 2.7 pCi/L**. Counties with an
average **below 2.7**: Blaine (0.5, one test), Cherry (2.0), Dundy (2.2),
Grant (1.9), Lincoln (2.5), Logan (1.8), Loup (2.3), McPherson (2.1), Merrick
(2.1), Rock (1.0), Sheridan (2.5), Sioux (1.9), Thomas (2.4), Wheeler (0.7).
**Arthur** had zero tests ("NA"); **Hall** averaged exactly 2.7 — neither
"less than" nor "exceeding," so the § 76-3505(2) exemption does not apply
there by its terms. The kit prints the 14 names with the data window and
tells the reader the list moves annually.

DHHS's own RRNC document repeats the exemptions: "if the project utilizes the
design of an architect or licensed engineer. Projects located in Zone 3
counties with a radon concentration of less than 2.7 pCi/l are exempt."
Department: DHHS (§ 76-3503(3)) — **radon is DHHS; onsite wastewater is
DWEE**; the guide has them backwards.

**Conversion**: a building contractor or sub "may convert a passive radon
mitigation system to an active" one without being a licensed mitigation
specialist, but "A radon mitigation specialist shall conduct any
postinstallation testing" (§ 76-3506).

**Reporting tripwire `[H]`**: a 2025 bill (LB376 § 41) reportedly removed the
annual report-to-the-Legislature language; the current § 76-3507 text read
September 2026 still requires DHHS to "compile the results … and identify
each county" annually. The public list is DHHS's "Average Radon Levels by
County" PDF (an image; not machine-readable). Re-check yearly.

---

## 4. PERMITS, CLOCKS AND INSPECTIONS

Nebraska has **no statewide building-permit statute for houses**: no state
application contents, no plan-review clock, no permit life, no inspection
list, no certificate of occupancy rule. Those exist only in local amendments
adopted under § 71-6406(7). What the state does fix is below.

| Item | Rule | Cite `[V]` |
|---|---|---|
| Building permit — who | local, optional; county zoning permit for "any nonfarm building" where zoned; city in its ETJ | §§ 71-6406(7), 23-114.04, 14-419, 15-905 |
| Plans a county zoning permit needs | "plans of and for the proposed erection … including sanitation, plumbing and sewage disposal" filed in the building inspector's office | § 23-114.04(2) |
| Self-inspection | never: "Authorized inspector does not include an individual performing a self-performed inspection for the individual's own permit or building" | § 71-6409(1)(a) |
| Virtual inspection | allowed for 1–2 family, <3 stories, <10,000 sq ft, live with the permit holder, if a licensed/registered contractor "who is completing the work" is named; photo/video for nonstructural reinspections | § 71-6409(2) (eff. 7-18-2026) |
| **Electrical request for inspection** | "At or before commencement," with fees; late = **$250** + 14-day certified-mail notice + county attorney | §§ 81-2126, 81-2135(2) |
| Electrical permit life | void if not started in **5 months** or no progress for 5 months, after 14 days' notice; extensions for hardship | Board Rule 13 |
| **Electrical rough-in** | notify "within reasonable time … prior to concealment"; cover without notice = you pay to uncover | § 81-2134(2) |
| **Electrical inspection clock** | "Inspections shall be made within **one week** of the appropriate request" | § 81-2134(3) |
| Electrical correction order | final inspection date **10–17 calendar days** out | § 81-2138 |
| Temporary service | separate application; "a minimum of five working days prior to the date energization is required"; inspector "may verbally authorize energization" | Board Rule 12 |
| **Power connection** | owner's certificate to the utility that inspection was requested and installation is safe; utility "may refuse service without liability" | § 81-2129 |
| Energizing before inspection | "circuits may be energized by the authorized installer prior to inspection but the installation shall remain subject to condemnation and disconnection" | § 81-2134(3) |
| Septic permit | Department permit before construction — general permit (owner covered if conditions met) or PE-stamped individual permit; installer must be certified/PE/REHS and on site | Title 124 ch. 3; § 81-15,248(1); ch. 9 § 004 |
| Septic registration | within **45 days** of completion by the professional; **$140** registration; late $150 (46–90 days) / $450 (91+) | § 81-15,248(2); Title 124 App. A |
| Individual septic construction permit fee | **$450** application | Title 124 App. A |
| Well registration | within **60 days**; **$200 + $25–40**; well log per § 46-1241 | §§ 46-602(1), 46-606(1), 46-1224(3) |
| Well variance | written request "at least 10 days prior" to construction, with "a scaled map showing the location of the well in relation to property lines, structures, utilities, and contamination sources" | Title 134 ch. 4 § 012.01 |
| One-Call | notice to the center "at least two full business days, but no more than ten business days, before commencing the excavation" | § 76-2321(1) |
| Energy | no permit, no certificate; builder self-compliance; DWEE determination on owner's written request; 2-year correction order | §§ 81-1622, 81-1616, 81-1625 |
| Contractor registration | $40/yr, DOL, 30 days to issue; owner exempt | §§ 48-2104(1), 48-2107, 48-2108 |

**Inspection sequence the kit can print as statutory (NE.3)**: electrical
**temporary service → rough-in → final** (§ 81-2134; handout), with the septic
professional's registration and the well registration as the two other
mandatory records. Every other inspection (footing, framing, insulation,
plumbing, mechanical, final/CO) is **local** and exists only where a program
does. NE.3 prints the local list as "typical where a program exists" and does
not attribute it to the state.

**Lincoln local clocks `[V]`** (city pages): homeowner trade permits valid
**120 days**; inspect before concealment and at completion.

---

---

## 5. LICENSING AND CONTRACTS

### 5.1 Contractor Registration Act — a registration, not a license, and the owner is outside it `[V]`

**§ 48-2104(1), verbatim:** "Before performing any construction work in
Nebraska, a contractor shall be registered with the department. … **Any person
who performs work or has work performed on his or her own property or any
person who earns less than five thousand dollars annually for construction
services is not a contractor for purposes of the Contractor Registration
Act.**"

That is the whole owner-builder answer: an owner building on their own
property is **not a contractor** and does not register. The Department of
Labor's registration page says the same in plain words: "A contractor is any
person or business … who engage in or arrange for work on real property
**other than their own property**."

| Rule | Text | Cite |
|---|---|---|
| Intent | "all contractors doing business in Nebraska be registered … It is not the intent of the Legislature to endorse the quality or performance of services provided by any individual contractor." | § 48-2102 |
| Contractor | anyone "engaged in the business of the construction … of buildings … including such construction … of such property **to be held either for sale or rental**" and "any subcontractor" and "any person who is providing or arranging for labor" | § 48-2103(3) |
| Fee | "not to exceed forty dollars," annual | § 48-2107; DOL: "annual fee increases to $40.00 effective August 1, 2026" |
| What registration proves | name/EIN, address, entity type, sales-tax election, **proof of workers' compensation insurance, self-insurance, or a signed statement that none is required** | § 48-2105 |
| Registration number | issued within 30 days; five digits + two-digit year | § 48-2108 |
| Revocation | automatic on lapse of workers' comp coverage | §§ 48-2109, 48-2110 |
| Penalty for the **contractor** | citation; administrative penalty ≤ $500 first violation, ≤ $5,000 subsequent | § 48-2114 |
| **Penalty for hiring an unregistered sub** | **None in the Act.** Every duty and every penalty attaches to the contractor. (Verified absence, §§ 48-2101–2117.) | — |
| Public database | DOL must publish, with each contractor's workers' comp status: insured / self-insured / **"sole proprietor with no employees and does not carry workers' compensation insurance"** | § 48-2117(3) |
| Not the state's endorsement | database presumption "solely for the purpose of establishing premiums" | § 48-2117(5) |

**Search**: `https://dol.nebraska.gov/conreg/Search` (HTTP 200). The kit's
sub-vetting step: every hired trade should appear here, and the entry tells
you whether they carry workers' comp — which matters because of § 48-116
(§ 5.5).

A spec builder (building "to be held … for sale") **is** a contractor under
§ 48-2103(3). The owner exemption is for one's own property; it is not a
"one house per year" rule — no frequency cap exists anywhere in the Act.

### 5.2 Electrical licensing and the homeowner right to wire

See § 3.3 in full. Summary for NE.1: licence exemption only (§ 81-2121(5));
inspection and request-for-inspection duties unchanged (§§ 81-2124(3),
81-2126); no utility connection without the owner's certificate (§ 81-2129);
Class IV felony for not filing (§ 81-2143(1)(c), from 18 July 2026).

### 5.3 Plumbing and HVAC — no state licence, and the UPC is the default everywhere `[V]`

**No Nebraska statute licenses plumbers or HVAC contractors at the state
level.** Verified by reading the full section indexes of Chapters 18, 38, 71
and 81 for "plumb," "heating," "HVAC," "air condition" and "mechanical
contractor": the only hits are the **municipal plumbing board** statutes
(§§ 18-1901–1906), the modular/manufactured-housing standards (§§ 71-1558,
71-1561, 71-4604) and the electrical "special electrician" licence (§ 81-2102(17)).

**Municipal plumbing boards — § 18-1901**: a city of the **metropolitan class
(Omaha) "shall"** have a plumbing board; a city of the **primary class
(Lincoln) "may"**; cities of the first and second class and villages "may."
§ 18-1901(6): the plumbers on the board "shall be licensed plumbers … licensed
within such cities." § 18-1906: the board adopts plumbing rules by ordinance
and "shall have power to compel the owner or contractor to first submit the
plans and specifications for plumbing … for approval." **Plumbing licences
are city licences, issued under city ordinances; there is no statewide
registry.**

**The default plumbing code is statutory, three times over:**

- § 71-6403(1)(d): the 2018 UPC is a component of the **state building code**.
- **§ 18-132(4)** (cities and villages): "If there is no ordinance adopting a
  plumbing code in effect in a city or village, the 2018 Uniform Plumbing Code
  … shall serve as the plumbing code for all the area within the jurisdiction
  of the city or village. **Nothing in this section shall be interpreted as
  creating an obligation for the city or village to inspect plumbing work.**"
- **§ 23-172(4), (6)** (counties): "If there is no county resolution adopting
  a plumbing code in effect for such county, the 2018 Uniform Plumbing Code …
  shall apply to all buildings" and "Nothing in this section shall be
  interpreted as creating an obligation for the county to inspect plumbing
  work."

So the plumbing standard for a Nebraska house is the **2018 UPC** unless the
city or county adopted something else — and the Legislature said, twice, that
nobody has to inspect it. Same Kentucky inversion, plumbing edition.

**HVAC**: no state mechanical licence or permit. The mechanical standard is
the 2018 IRC's own chapters 12–24 (part of the adopted IRC; only ch. 25–33
were excluded). The *electrical* side of an HVAC installation is a licensed
specialty (§ 81-2102(17)); see § 3.3.

### 5.4 Septic installers and well drillers

#### 5.4.1 Onsite wastewater — you may NOT install your own system `[V]`

**§ 81-15,248(1), verbatim:** "A private onsite wastewater treatment system
shall not be sited, laid out, constructed, closed, reconstructed, altered,
modified, repaired, inspected, or pumped unless the siting, layout,
construction, closure, reconstruction, alteration, modification, repair,
inspection, or pumping is carried out or supervised by either a certified
professional as required by the Private Onsite Wastewater Treatment System
Contractors Certification and System Registration Act, a professional
engineer licensed in Nebraska, or a registered environmental health
specialist registered in Nebraska."

There is **no owner exception** in the Act (§§ 81-15,245–253 read) and none
in Title 124. **Title 124 ch. 9 § 004** closes the "supervised" loophole:
"No person will engage in the siting, layout, construction … of a private
onsite wastewater system unless a Master Installer, a Journeyman Installer,
a professional engineer, or a registered environmental health specialist who
is responsible for such work **is physically present at the site** where such
work is being performed and is supervising the work." Ch. 9 § 001 defines
"direct supervision" the same way. An owner may dig alongside a Master
Installer who stays on site; an owner may not build the system alone.

| Rule | Text | Cite |
|---|---|---|
| Perc tests | only by a PE, REHS, or certified Inspector, Soil Evaluator, Master or Journeyman Installer | Title 124 ch. 2 § 012.01 |
| Registration | by the certified professional/PE/REHS "within **forty-five days** of completion"; fee $50 by statute until the fee schedule sets otherwise | § 81-15,248(2); ch. 10 |
| Late registration | initial late fee after 45 days; final late fee at 91+ days | ch. 10 § 003 |
| Owner gets a copy | professional "will provide a copy of the system registration form to the system owner" | ch. 10 § 004 |
| Local delegation | Director "by contract may delegate onsite wastewater treatment system inspection and registration to a governmental subdivision" with an at-least-as-stringent program | § 81-15,248(3) |
| Local stringency | "Nothing in this Title will prevent more stringent local requirements from being adopted." | ch. 2 § 014 |
| Penalty | civil penalty ≤ **$10,000 per violation per day** | § 81-15,253 |
| Reserve area | owner "will establish a reserve area sufficient in size" for a replacement system; setbacks apply to it | ch. 2 § 008 |
| Encroachment | "A person is not to construct or relocate a foundation, well, water line, surface water feature, or property line within the setback distances listed in Table 2.1" — PE letter needed for a variance | ch. 2 § 011 |
| Prohibited | cesspools, dry wells, leaching pits, seepage pits | ch. 2 § 003 |

**Permit structure** (Title 124 ch. 3): a system "is to be permitted by the
Department before any construction" (§ 002). Two routes: **General Permits**
(§ 003 — the owner "will be authorized to construct … under a general permit
if they meet the conditions of the permit," § 003.06) and individual
**Construction and Operating Permits** (§§ 004–006) whose plans "will be
prepared and properly stamped and signed by a Professional Engineer"
(§ 004.03). The Department publishes general permits for a **septic tank and
subsurface leach field, holding tank, wastewater lagoon, and mound system**
(Title 124 booklet, form 23-017 ver. 02.2026). A conventional house system
rides the general permit; an engineered system needs the individual permit.
The general permit's sizing rules are in § 6.5. **General-permit coverage
conditions** (GTS220000 § II.A) `[V]`: coverage "is granted to an owner of a
dwelling/non-dwelling facility who" submits, with the system registration, a
certification signed by the PE/REHS/certified professional, "an appropriately
scaled drawing of the onsite wastewater treatment system" and the percolation
or seepage test data. A pressure-dosed absorption system "is not covered under
this general permit" (§ III.K.21).

#### 5.4.2 Water wells — you MAY drill your own, on your own homestead `[V]`

**§ 46-1233(2), verbatim:** "A water well shall be constructed, pumps and
pumping equipment shall be installed and repaired onsite, and water wells
shall be decommissioned by a licensed contractor or supervisor or a person
working directly under the supervision of a licensed contractor or
supervisor, **except that an individual may construct a water well or install
and repair pumps and pumping equipment onsite on land owned by him or her
and used by him or her for farming, ranching, or agricultural purposes or as
his or her place of abode.**"

§ 46-1233(1): whoever constructs the well "shall do such work in accordance
with the rules and regulations developed under the Water Well Standards and
Contractors' Practice Act" — the owner exemption is from the **licence**, not
the **construction standard**.

| Rule | Text | Cite |
|---|---|---|
| Registration | every well completed on/after 1 July 2001 "shall be registered with the department … **within sixty days** after completion"; filed by "the licensed water well contractor … **or the owner of the water well if the owner constructed the water well**" | § 46-602(1) |
| Well log | "Any owner of a water well or a licensed water well contractor who engages in … constructing a water well shall keep and maintain an accurate well log" — 18 listed items | § 46-1241 |
| Fees | registration fee **$200** (§ 46-606(1)) **plus** the board's fee of **$25–$40** for a well designed to pump ≤ 50 gpm (§ 46-1224(3)) | §§ 46-606, 46-1224 |
| Department | "Department means the Department of Water, Energy, and Environment" | § 46-1207 |
| Pump wiring | a licensed pump installation contractor may wire "pumps and pumping equipment at a water well location to the first control" without an electrical licence | § 81-2121(7) |
| Discipline | licensee failing to file a registration or decommissioning notice is a ground for discipline | § 46-1235(8), (9) |

> ⚠ **The well construction standards have moved.** The lead cited "NDEE Title
> 178 Ch. 12." That chapter (178 NAC 12, effective 8/26/14, DHHS) is the old
> home. DWEE's Water Well Standards page (September 2026) now lists **Title 134
> NAC Chapters 1–5 (2026)**, with **Chapter 4 = "Regulations Governing Water
> Well Construction, Pump Installation and Water Well Decommissioning
> Standards."** § 6 uses Title 134 ch. 4; Title 178 ch. 12 is cited only as
> the superseded text. Title 134 ch. 4 (effective **June 28, 2026**) was read;
> its Chart 1 and Chart 2 are reproduced in § 6.3. Title 134 ch. 1 repeats the
> owner language ("by an individual on land owned by him or her and used by
> him or her for farming, ranching, or agricultural purposes or as his or her
> place of abode").

### 5.5 Workers' compensation and liens `[V]`

**Workers' compensation.** § 48-106(1): the Act applies to "every resident
employer in this state … who employs one or more employees **in the regular
trade, business, profession, or vocation of such employer**." § 48-115 (final
paragraph): "the terms employee and worker shall not be construed to include
any person whose employment is **not in the usual course of the trade,
business, profession, or occupation of his or her employer**." § 48-106(2)(b)
separately excludes "a household domestic servant in a private residence."
`[H]` An owner building their own home is not in the trade or business of
construction, so a directly hired day labourer is, on this text, outside the
Act — but the kit does **not** print that as a safe harbour, because a
tribunal decides "usual course" on facts, and the exposure if wrong is a Class
I misdemeanor plus personal liability (§ 48-145.01(1)).

**The statutory-employer trap and its cure — § 48-116**: any person "creating
or carrying into operation any scheme, artifice, or device to enable him or
her … to execute work without being responsible to the workers for the
provisions of the Nebraska Workers' Compensation Act shall be included in the
term employer" and is jointly and severally liable — **but** "This section …
shall not be construed as applying to an owner who lets a contract to a
contractor in good faith … if the owner … requires the contractor … to procure
a policy or policies of insurance from an insurance company licensed to write
such insurance in this state." **Kit rule: require a workers' comp certificate
(ACORD 25) from every contractor with employees, and check the DOL registry
flag for sole proprietors.** The DOL registry page: "All contractors with one
or more employees must provide a current Workers' Compensation Certificate of
Insurance (ACORD 25) with the Department of Labor listed as the certificate
holder."

**Construction liens — Nebraska Construction Lien Act, §§ 52-125 to 52-159.**
§ 52-137(1): a lien "does not attach and may not be enforced unless … not
later than **one hundred twenty days** after his or her final furnishing of
services or materials, he or she has recorded a lien." § 52-135(1): a claimant
"may give notice of the right to assert a lien to the contracting owner" —
with the mandatory warning "**If you did not contract with the person giving
this notice, any future payments you make in connection with this project may
subject you to double liability**" — and § 52-135(6): "This section shall
apply to a lien claimant only when the contracting owner is a protected
party." § 52-136(2), (5): as against a protected-party owner, a sub's lien is
capped at the lesser of its own unpaid amount or **the amount unpaid on the
prime contract when the notice arrives**; payments made in good faith before
notice are "properly made."

**"Protected party" — § 52-129(1)(a)** `[V]`: "An individual who contracts to
give a real estate security interest in, or to buy or to have improved,
residential real estate all or a part of which he or she occupies or intends
to occupy as a residence." **An owner-builder building their own home is a
protected party**, and "residential real estate" is "not more than four
dwelling units and no nonresidential uses" (§ 52-129(2)). Practical rule for
NE.5: keep every "notice of the right to assert a lien" received, stop paying
the prime contractor's unpaid balance to anyone else once a notice arrives,
and collect lien waivers with each payment.

**Seller disclosure — § 76-2,120.** Every seller of residential real property
gives the written disclosure statement (§ 76-2,120(2)), **except** — (6)(k) —
a transfer "Of newly constructed residential real property which has never
been occupied." An owner-builder who lives in the house and later sells is
inside the statute; the statement is "to the best of the seller's belief and
knowledge" and the seller is not liable for errors "not within the personal
knowledge of the seller" (§ 76-2,120(5), (8)).

---

## 6. SITE PLAN STUDIO EXTRACTION

Feeds `src/lib/siteplan/rules.ts`. All values `[V]`, read from **NDEE Title
124 ch. 2 Table 2.1** (effective June 27, 2022) and **DWEE Title 134 ch. 4
§ 001.03 Chart 1** (effective June 28, 2026). Units are feet.

> Framing note for the tool: Title 124 ch. 2 § 014: "Nothing in this Title
> will prevent more stringent local requirements from being adopted." Title
> 134 ch. 4 § 001: "These are minimum requirements. Local requirements may be
> more stringent." Delegated local programs exist (§ 81-15,248(3)). Present
> every number as a **state floor** the local health department or NRD may
> raise.

### 6.1 Title 124 Table 2.1 — Lagoon, Tank and Soil Absorption System Setbacks

| Feature | Tanks | Absorption / infiltrative / evaporative | Lagoons |
|---|---|---|---|
| Surface water | 50 | 50 | 50 |
| **Private drinking water wells** | **50** | **100** | 100 |
| Public non-community wells | 50 | 100 | 100 |
| Public community wells | 500 | 500 | 1,000 |
| Horizontal closed-loop geothermal wells | 25 | 25 | 25 |
| All other water wells | 50 | 100 | 100 |
| Water lines: pressure main/service, suction lines | 10 | 25 | 25 |
| **Property lines** | **5** | **5** | 50 |
| Trees | NA | NA | 50 |
| Parking area, driveway, sidewalk, impermeable surface | 5 | 5 | 50 |
| Foundation, Class 1 (any part *lower* than the system) | 15 | **30** | 100 |
| Foundation, Class 2 (foundation *higher* than the system; default) | 10 | 10 | 100 |
| Foundation, Class 3 (slab-on-grade, not living quarters) | 7 | 10 | 50 |
| Neighbor's foundation, Class 1 / 2 / 3 | 25 / 20 / 15 | 40 / 30 / 20 | 200 / 200 / 100 |

Table footnotes, verbatim in substance: Class 1 = "a basement, a non-basement
footing, swimming pool, or slab-on-grade living quarters where any portion of
the living quarters basement, footing, or slab is **lower in elevation** than
the onsite wastewater treatment system component"; Class 2 = the same
structures "**higher in elevation**" than the system, and "Any other
foundation that is not a Class 1 or Class 3"; Class 3 = "slab-on-grade
construction that is not used as living quarters." The water-well setback
"does not apply to a monitoring well." Some non-community public systems have
stricter Title 179 setbacks.

**Tool-encodable core seven** (governing = absorption column, tank in note):

| Core key | feet | Citation | Note |
|---|---|---|---|
| wellToSeptic (tank) | 50 | Title 124 ch. 2 Table 2.1 | tank to private drinking-water well; also Title 134 ch. 4 Chart 1, 50 ft "Any septic tank" — the two rules agree |
| wellToDrainfield | 100 | Title 124 ch. 2 Table 2.1; Title 134 ch. 4 Chart 1 | absorption system to private well; Chart 1 says 100 ft "Any septic lateral field (soil absorption system)" from the well side, and Chart 2 lets a driller go to 50–100 ft only with prior written DWEE approval and full-depth bentonite grout |
| wellToPropertyLine | null | — | **no state rule** — Title 134 ch. 4 Chart 1 has no property-line row (verified absence); only wells "under different ownership" carry distances (600 ft irrigation, 1,000 ft industrial/community), and those apply "only … to drilling industrial and irrigation wells" |
| septicToPropertyLine | 5 | Title 124 ch. 2 Table 2.1 | tank and absorption alike; lagoon 50 |
| septicToBuilding | 10 | Title 124 ch. 2 Table 2.1 | absorption to a Class 2 foundation; **30 ft if any part of the house is lower than the system (Class 1)**; tank 10 / 15 |
| septicToSurfaceWater | 50 | Title 124 ch. 2 Table 2.1 | tank, absorption and lagoon all 50 |
| wellToSurfaceWater | null | — | Title 134 ch. 4 Chart 1 has **no surface-water row** (verified absence); 10 ft "Any storm water way" and 10 ft "Any depression that could retain stagnant water" are the nearest rules |

### 6.2 Extra separations worth drawing

| Label | feet | Cite |
|---|---|---|
| Absorption area to a pressure water line or suction line | 25 | Title 124 Table 2.1 |
| Absorption area to driveway / parking / impermeable cover (also "within five feet horizontally" of a reserve area, GP § III.K.12) | 5 | Title 124 Table 2.1; GTS220000 |
| Absorption area to neighbour's foundation (Class 2) | 30 | Title 124 Table 2.1 |
| Well to any sewer line: pressurized or non-watertight / watertight | 50 / 10 | Title 134 ch. 4 Chart 1 |
| Well to wastewater lagoon, privy, cesspool, subsurface disposal system | 100 | Title 134 ch. 4 Chart 1 |
| Well to animal-waste structure or feeding-operation holding pens | 100 | Title 134 ch. 4 Chart 1 |
| Well to storm water way, frost-proof hydrant, well pit | 10 | Title 134 ch. 4 Chart 1 |
| Vertical: trench/bed bottom above seasonal high groundwater or barrier layer | 4 ft | GTS220000 § III.C, § III.K.1 |
| Undisturbed soil between trenches and between tank and nearest trench: slope <10% / 10–20% / >20% | 4 / 6 / 10 | GTS220000 § III.K.9 |

### 6.3 Well side — Title 134 ch. 4 Chart 1 (2026) versus Title 178 ch. 12 (2014)

The 2026 chart keeps every 2014 number and **splits "Any sewer line, 50"**
into pressurized sanitary 50 / non-watertight sanitary 50 / **watertight
sanitary 10** / storm 10, and adds the reserve area to the Chart 2 lateral-
field row. Chart 2 (50–100 ft to a lateral field, 25–50 ft to a tank) needs
(1) Chart 1 cannot be met, (2) prior written Department approval, (3)
full-length chip-bentonite grout, (4) protective silts/clays. Below Chart 2: a
declaratory ruling (§ 001.03(c), § 011).

### 6.4 Site disqualifiers and design rules — GTS220000 (septic tank + leach field general permit, June 27, 2022)

- **Percolation window**: "Soil is unsuitable for a soil absorption system if
  the percolation rate is faster than five minutes per inch or is slower than
  60 minutes per inch" (§ III.E.1, § III.J.1). Faster than 5 mpi is rescued
  by a 12-inch loamy-sand liner at 15–20 mpi and sized on the liner rate
  (§ III.J.2, § III.K.3); slower than 60 mpi "unless designed by a
  professional engineer and a construction permit is issued" (§ III.J.3) —
  i.e. off the general permit.
- **Groundwater**: seasonal high water table "at least four feet below the
  bottom of the infiltrative surface" (§ III.C).
- **Fill**: "Construction of a soil absorption system in fill is prohibited"
  except sand fill, or where the bottom 12 in. of the trench is in undisturbed
  native soil below the fill (§ III.J.4, § III.K.2).
- **Slope**: >3% requires drop-box or pressure distribution unless every
  trench bottom is at one elevation (§ III.K.13.b); trench spacing steps up at
  10% and 20% (§ III.K.9).
- **Trench limits**: gravity trench/bed ≤ 150 ft (§ III.K.5); trench 18–36 in.
  wide for pipe, ≤ 5 ft for chambers, wider = bed with Table 4 multiplier
  (1.25 up to 10 ft, 1.33 to 15 ft, 1.50 to 20 ft, >20 ft unacceptable);
  cover 8–36 in. (§ III.K.11); dosing required over 500 linear ft (§ III.K.20).
- **Reserve area** required and carries all setbacks (Title 124 ch. 2 § 008).
- **Perc tests only by** a PE, REHS, or certified Inspector / Soil Evaluator /
  Master or Journeyman Installer (Title 124 ch. 2 § 012.01).

### 6.5 Sizing numbers `[V]` — GTS220000

- **Design flow, Table 1**: "100 gallons per day plus 100 gallons per day per
  bedroom" — 1 br 200; 2 br 300; **3 br 400**; 4 br 500; 5 br 600; 6 br 700;
  7 br 800; 8 br 900; 9 br 1,000 gpd (§ III.B.3). A garage floor drain adds
  ≥ 100 gpd (§ III.L.3). Over 1,000 gpd is off the general permit.
- **Septic tank, Table 3** (minimum gallons; "In no case … less than 1,000"):

| Design flow (gpd) | no grinder / no large tub | grinder **or** large tub | grinder **and** large tub |
|---|---|---|---|
| 200 | 1,000 | 1,000 | 1,000 |
| 300 | 1,000 | 1,000 | 1,250 |
| **400 (3 br)** | **1,000** | **1,250** | **1,500** |
| 500 | 1,250 | 1,500 | 1,750 |
| 600 | 1,500 | 1,750 | 2,000 |
| 700 | 1,750 | 2,000 | 2,250 |
| 800 | 2,000 | 2,250 | 2,500 |
| 900 | 2,250 | 2,500 | 2,750 |
| 1,000 | 2,500 | 2,750 | 3,000 |

  "Large capacity tub" = working volume > 50 gallons. Single-compartment tank
  fed by a pump: +50% (§ III.H.3). Capacity is measured below the outlet
  invert (§ III.H.4).
- **Absorption trench bottom area, Table 5** (sq ft), by perc rate and flow:

| mpi | 200 | 300 | **400** | 500 | 600 | 700 | 800 | 900 | 1,000 gpd |
|---|---|---|---|---|---|---|---|---|---|
| <5 | liner, use 11–20 row | | | | | | | | |
| >5–10 | 165 | 330 | **495** | 660 | 825 | 990 | 1,155 | 1,320 | 1,485 |
| >10–20 | 210 | 420 | **630** | 840 | 1,050 | 1,260 | 1,470 | 1,680 | 1,890 |
| >20–30 | 250 | 500 | **750** | 1,000 | 1,250 | 1,500 | 1,750 | 2,000 | 2,250 |
| >30–40 | 275 | 550 | **825** | 1,100 | 1,375 | 1,650 | 1,925 | 2,200 | 2,475 |
| >40–50 | 330 | 660 | **990** | 1,320 | 1,650 | 1,980 | 2,310 | 2,640 | 2,970 |
| >50–60 | 350 | 700 | **1,050** | 1,400 | 1,750 | 2,100 | 2,450 | 2,800 | 3,150 |
| >60 | "Ineligible for general permit" | | | | | | | | |

  Formula for non-dwellings (§ III.K.19.b): sq ft = design flow × 0.20 ×
  √(perc rate). Beds: multiply by Table 4.
- **Holding tank** (holding-tank general permit): 1,000 gal for ≤ 2 bedrooms
  + 300 gal per additional bedroom, min "five times the daily flow but not
  less than 1,000 gallons" (Table 01: 3 br 1,300; 4 br 1,600; 5 br 1,900).

### 6.6 Do NOT encode

- **Building setbacks from lot lines** — county zoning (§ 23-114(2)(c)
  "building setback lines") or city zoning; no statewide value.
- **Frost depth, snow load, wind speed** — IRC Table R301.2 is filled in
  locally; no state table exists (verified absence in the Act). The guide's
  "42 inches Omaha" is unverified.
- **A well-to-property-line or well-to-surface-water distance** — none in
  Title 134 ch. 4.
- **Anything for a delegated-program county** (Lincoln-Lancaster, Douglas,
  Sarpy and others under § 81-15,248(3)) as if it were the ceiling — those
  programs may be stricter (Title 124 ch. 2 § 014).

**negativeFindings for the tool**:
- "You may drill your own well on land you own and use as your place of abode
  (§ 46-1233(2)), and you register it yourself within 60 days (§ 46-602(1)) —
  but you may NOT install your own septic system: a certified installer, PE or
  REHS must be physically present and supervising (§ 81-15,248(1); Title 124
  ch. 9 § 004)."
- "Perc faster than 5 min/inch fails without a 12-inch loamy-sand liner, and
  slower than 60 min/inch is off the general permit (GTS220000 § III.J)."
- "The house-to-drainfield distance triples — 10 ft to 30 ft — when any part
  of the basement or footing sits lower than the system (Title 124 Table 2.1
  Class 1)."
- "Title 134 ch. 4 (2026) has no well-to-property-line rule; the 600/1,000 ft
  rows apply only to irrigation and industrial wells."

---

## 7. DELIBERATELY NOT PRINTED

| Item | Why |
|---|---|
| Any building-permit fee, plan-review percentage, or tap fee | No state schedule exists; every local figure in the guide (Omaha "Table 43-91," "25%," Douglas "65%," $ ranges) is unverified. Omaha and Douglas sites are unreachable. |
| Omaha's code edition, frost depth, homeowner-permit procedure, "appointment with the Chief Electrical Inspector" | Omaha's pages geo-block; nothing verified. Statutory frame only (§ 1.8). |
| "42-inch frost depth" and any frost/snow/wind number | No statewide table; locally set in IRC Table R301.2. |
| A count of counties with building-permit programs | No primary source exists; the statute makes it optional and unreported (§ 1.7). |
| "You must personally do the wiring, without compensation" | Not in § 81-2121(5) and not in the SED handout. |
| "A few GFCI/AFCI sections remain on the 2017 NEC" | The five carve-backs are GFCI (210.8(A) list), surge protection (230.67(A)) and the emergency disconnect (230.85). No AFCI section. |
| "Nebraska Energy Code certificate" | No state certificate exists; § 81-1622 is self-compliance. (The IECC's own R401.3 posted certificate is a code requirement, not a state form.) |
| "4 inches of clean aggregate" and "vapor retarder" as RRNC law | Not in § 76-3504. |
| "53 of 93 counties in EPA Zone 1" / "statewide average well above 4" | Not from a Nebraska source; DHHS numbers (77 of 93 above 2.7) printed instead. |
| The family carve-out in § 81-2143(2) as permission | It narrows one felony; § 81-2108 still requires a licence "for another." |
| Workers'-comp "not required for an owner-builder" | Text of §§ 48-106, 48-115 supports it, but the kit prints the § 48-116 certificate rule, not a safe harbour. |
| Phone numbers | House rule. The SED GIS layer and Lincoln pages carry them; the kit points at the sources. |
| Class B electrical licensees' exact fee or exam | Irrelevant to the owner; only the <100,000-population limit matters. |
| Title 178 ch. 12 numbers as current | Superseded June 28, 2026 by Title 134 ch. 4. |

---

## 8. OPEN QUESTIONS

1. **Omaha.** Everything Omaha-specific must be verified from inside the US
   or by the owner in a browser: current code edition and ordinance, homeowner
   permit conditions, plumbing/mechanical licensing, fee table, whether the
   city or the SED issues a homeowner electrical permit inside city limits
   (SED GIS says "City of Omaha" inspects). NE.4 prints the URLs with a
   "geo-restricted; open in a normal browser" note.
2. **Douglas County Environmental Services** (unincorporated Douglas): same
   Akamai block. Its current code list and the guide's "65% plan review" are
   unverified.
3. **Building-permit programs by county** — no primary list. If the owner
   wants a number, the only honest path is a 93-clerk survey.
4. **§ 71-6409 and owner-builders**: the virtual-inspection option is
   conditioned on naming "the contractor who is licensed or registered … and
   who is completing the work." An owner doing their own work is neither. Not
   resolved by the text; the kit says "ask whether the county will extend it."
5. **§ 81-2143(2) family carve-out** — added 2026; whether it reaches
   § 81-2108's licence requirement or only the felony is untested.
6. **Radon county list currency** — the machine-readable list is the January
   2024 legislative report; DHHS's live PDF is an image. Confirm the current
   list before printing county names in a 2027 revision; LB376 (2025) may
   have changed the reporting duty.
7. **Whether a county zoning permit is demanded of a farmstead residence** is
   a county-by-county board decision (§ 23-114.03). No list exists.
8. **DWEE "Planning and Aid Division will enforce"** the energy code — the
   page says it; the statute gives only § 81-1616/1625 tools. No evidence of
   routine inspection was found.
9. **Hall County (2.7 pCi/L exactly)** — the statute's "less than" and
   "exceeds" leave 2.7 itself uncovered; treated as *not exempt*.

---

## 9. KIT REVISION WATCH — NEBRASKA TRIPWIRES

Add to `project-kit-revision-watch`:

1. **§ 71-6403 edition change.** Only the Legislature can move Nebraska off
   the 2018 I-Codes/UPC. Watch the Source line of § 71-6403 each session
   (January–April). A change restarts the two-year local clock
   (§ 71-6406(1)(b)) and rewrites NE.2. Lincoln already runs 2021.
2. **State Electrical Act.** Amended 2024 (LB144, LB716) and 2026 (LB889,
   LB1072). § 81-2104(5) (NEC edition + 2017 carve-backs) and § 81-2143
   (penalty, now felony) are the sections to re-read. SED fee form revised
   3-27-26; Board Rules PDF (4-23-24) is already stale on the penalty.
3. **Title 134** (wells) became effective **June 28, 2026** — first revision
   cycle will show whether DWEE re-issues chapters; Chart 1 numbers are the
   watch item. Title 178 ch. 12 must never be cited as current.
4. **Title 124 / general permits** — dated June 27, 2022; booklet form 23-017
   "ver. 02.2026." Watch the effective-date line on the GP header and
   Appendix A fees ($140 registration, $450 permit).
5. **Radon county list** — annual DHHS determination under § 76-3507; the 14
   sub-2.7 counties can change with five-year rolling data.
6. **SED inspection-jurisdiction GIS layer** — 5 counties / 14 cities as of
   September 2026; a city adopting an ordinance under § 81-2125 drops off the
   state list.
7. **DOL registration fee** — statutory cap $40 (§ 48-2107); hit the cap
   August 1, 2026. A cap increase would need a bill.
8. **§ 71-6409** virtual inspections (eff. 7-18-2026) — watch for a fix
   addressing owner-performed work.
9. **Sarpy County** adopts "every other code cycle" per its own resolution
   narrative — expect a 2024-code resolution around 2028; Lincoln likewise.

---

## 10. LATE ADDENDUM

*Reversals discovered after sections were written:*

1. **§ 3.3 was first written with "Class IV felony" on the strength of the
   current statute page alone; the LB889 slip law was then read and confirmed
   the felony is new (effective July 18, 2026) — the earlier state was a
   Class I misdemeanor.** The section was updated in place with the history
   rather than reversed.
2. **The lead's "NDEE Title 178 Ch. 12" for well standards is superseded**:
   DWEE Title 134 ch. 4, effective June 28, 2026, is current. § 5.4.2 and § 6
   were written against Title 134 from the start; Title 178 was read only for
   comparison.
3. **Omaha**: an early draft of § 1.8 intended to quote Omaha's own codes
   page; three fetch methods failed (geo-block). Nothing Omaha-specific is
   marked `[V]`.

4. **Build-pass corrections (September 8, 2026, kit builder).** (a) The
   § 3.3 worked fee example said $75 + 30 × $10 = **$310**; the arithmetic is
   **$375**, and NE.2 prints $375. The schedule itself ($75 new service
   1–400 A, $10 per branch circuit, $100 homeowner minimum) was re-read from
   the 3-27-26 application form and is unchanged. (b) The SED GIS layer
   (`NSED_Inspector_Programs`, re-read from the saved 43-feature export) also
   lists **Boys Town** (Douglas County) as "State of Nebraska" alongside La
   Vista and Waverly; NE.4 names all three as in-metro traps. (c) Lincoln's
   homeowner plumbing page (WebFetch, September 3, 2026) adds a fee the
   dossier omitted: homeowner trade permits carry "a minimum $35 fee" and
   "Additional inspection trips are $35"; the building-permit minimum remains
   "$65 and increases from there," with new homes "calculated based on the
   square footage with a $100 deposit." NE.4 prints all three as web-page
   figures. No other claim printed in the kit departs from this dossier.

---

## 11. VERIFIED URL SET (September 2026)

Every address below returned HTTP 200 to the method noted. **No phone
numbers; the kit prints a "write it in" line under each.**

### The ones that matter most

| What | URL | Method |
|---|---|---|
| ★ **SED inspection-jurisdiction map** (who inspects electrical at this address) | `https://gis.ne.gov/portal/apps/experiencebuilder/experience/?id=e398ff3b94424f08903b11183f80689b` | linked from SED page; data layer `https://gis.ne.gov/Enterprise/rest/services/NSED_Inspector_Programs/FeatureServer/0` (200) |
| ★ **SED homeowner handout** (page + RTF) | `https://electrical.nebraska.gov/homeowner-handout` | curl 200 |
| ★ **Application for State Electrical Inspection** (fees, 3-27-26) | `https://electrical.nebraska.gov/sites/default/files/doc/Application%20for%20Electrical%20Inspection%203.27.26_3.pdf` | curl 200 |
| ★ **DOL contractor registry search** | `https://dol.nebraska.gov/conreg/Search` (home: `https://dol.nebraska.gov/conreg`) | curl 200 |
| ★ **Title 124 booklet** (rules + general permits + forms) | `https://dee.nebraska.gov/sites/default/files/publications/23-017%20-%20Title%20124%20Onsite%20Wastewater%20Treatment%20Systems%20Booklet_0.pdf` | curl 200 |

### State Electrical Division

| What | URL |
|---|---|
| Home | `https://electrical.nebraska.gov/` |
| Statutes & rules (Act PDF rev. 6-26-2026; Board Rules 4-23-24) | `https://electrical.nebraska.gov/statutes-rules` |
| 2023 NEC adoption notice | `https://electrical.nebraska.gov/state-act-update-2023-code-adoption` |
| Online licensing & permitting system (live April 13, 2026) | `https://electrical.nebraska.gov/new-nsed-online-licensing-permitting-system-now-live` |
| April 1, 2026 fee notice | `https://electrical.nebraska.gov/april-1-2026-permit-fees-have-been-updated-reflect-increases-some-fees` |
| GIS mapping notice | `https://electrical.nebraska.gov/nsed-inspection-gis-mapping` |
| Licensing | `https://electrical.nebraska.gov/licensing` |

### DWEE — energy, onsite wastewater, wells

| What | URL |
|---|---|
| Energy codes page | `https://dwee.nebraska.gov/state-energy-information/energy-codes` |
| Residential Energy Code Fact Sheet (2018 IECC) | `https://dee.nebraska.gov/sites/default/files/energy/Website%20Nerbraska%20Residential%20Energy%20Code%20Fact%20Sheet.pdf` |
| Energy Impact Study 2018 vs 2021 (climate zone statement) | `https://dee.nebraska.gov/sites/default/files/energy/Energy%20Impact%20Study%20of%20the%202018%20IECC%20and%20the%202021%20IECC%20Energy%20Codes%20for%20Nebraska.pdf` |
| Title 124 rules PDF (6-27-2022) | `https://dwee.nebraska.gov/sites/default/files/titles/Title%20124%20Effective%2006-27-2022.pdf` |
| Water Well Standards statutes & regulations (Title 134 links) | `https://dwee.nebraska.gov/water-quality/groundwater/water-well-standards-and-contractors-licensing-program/water-well-standards-informational-brochures/water-well-standards` |
| Title 134 ch. 4 (well construction, 6-28-2026) | `https://dwee.nebraska.gov/sites/default/files/water/Title%20134%20NAC%204%202026-ADA.pdf` |
| Title 134 ch. 1 (licensure) | `https://dwee.nebraska.gov/sites/default/files/water/Title%20134%20NAC%201%202026-ADA.pdf` |

### Radon (DHHS)

| What | URL |
|---|---|
| Radon data page (county PDF, EPA map) | `https://dhhs.ne.gov/Pages/Radon-Data.aspx` |
| RRNC Requirements and Recommendations | `https://dhhs.ne.gov/Radon%20Documents/RRNC%20Requirements%20and%20Recommendations.pdf` |
| County averages report to the Legislature (Jan 1, 2024; machine-readable) | `https://nebraskalegislature.gov/FloorDocs/108/PDF/Agencies/Health_and_Human_Services__Department_of/713_20231227-153438.pdf` |

### Local

| What | URL | Note |
|---|---|---|
| Lincoln Building & Safety — codes | `https://www.lincoln.ne.gov/City/Departments/Building-Safety/Codes` | WebFetch 200; curl 403 |
| Lincoln homeowner building permits | `https://www.lincoln.ne.gov/City/Departments/PDS/Building-Safety/Homeowner-Building-Permits` | |
| Lincoln homeowner plumbing / mechanical / electrical | `.../Building-Safety/Plumbing/Homeowner-Plumbing-Projects`, `.../Mechanical/Homeowner-Mechanical-Projects`, `.../Electrical/Homeowner-Electrical-Projects` | |
| Lincoln permit portal | `https://permits.lincoln.ne.gov/CitizenAccess/` | |
| Sarpy County Planning & Building | `https://www.sarpy.gov/215/Planning-Building` | curl 200; portal `https://co-sarpy-ne.smartgovcommunity.com/Public/Home` |
| Sarpy Resolution 2024-150 | `https://www.sarpy.gov/DocumentCenter/View/6607/Resolution-2024-150` | |
| Omaha Planning — Building & Development Division | `https://planning.omaha.gov/building-and-development-division/` | **403 geo-block**; print with caveat |
| Omaha codes & amendments | `https://planning.omaha.gov/codes-amendments/` | **403 geo-block** |
| Douglas County Environmental Services permits | `https://www.dceservices.org/permits-and-inspections` | **403** |

### Statutes and everything else

| What | URL |
|---|---|
| Statute pattern | `https://nebraskalegislature.gov/laws/statutes.php?statute=71-6403` |
| Chapter index pattern | `https://nebraskalegislature.gov/laws/browse-chapters.php?chapter=71` |
| Slip laws | `https://nebraskalegislature.gov/FloorDocs/109/PDF/Slip/LB889.pdf` |
| Nebraska811 (One-Call) | statute § 76-2321; center site not fetched — print "Nebraska 811" with the two-business-day rule |
| FEMA Flood Map Service Center | `https://msc.fema.gov/portal/home` |

---

## 12. LIVE GUIDE AUDIT — `src/app/permitting/state-guides/nebraska/page.mdx`

Read in full (608 lines), September 2026. **No in-page anchors.** Format:
line → guide text (quoted) → correction → cite.

### 12.1 Wrong

| Line | Guide says | Correction | Cite |
|---|---|---|---|
| 33, 60, 555 | "2023 NEC … with some 2017 NEC carve-outs" / "a handful of GFCI/AFCI sections remain on the 2017 NEC" | The 2017 text applies to **210.8(A), 210.8(A)(3), 210.8(A)(5), 230.67(A) and 230.85** — GFCI list, outdoor and basement GFCI, service surge protection, emergency disconnect. **No AFCI section.** | § 81-2104(5) |
| 62 | "Plumbing & mechanical: Set by local code in jurisdictions that enforce one …; the IRC's own provisions apply where the state code governs" | IRC ch. 25–33 (plumbing) are **excluded**. The state plumbing code is the **2018 Uniform Plumbing Code**, and it is the default in every city/village and county without its own plumbing ordinance. Mechanical is IRC ch. 12–24. | § 71-6403(1)(b), (d); § 18-132(4); § 23-172(4) |
| 66 | "The Legislature has periodically updated specific chapters (for example, pulling energy provisions toward newer editions)" | No such amendments; § 71-6403 last touched 2021 (LB131, conforming). Delete. | § 71-6403 Source line |
| 127, 500, 559 | "You must personally do the wiring, with no compensation paid to or by another person" / "do the work yourself without pay" | Not in the statute or the SED handout. The exemption is from licensing; the conditions are principal residence, not larger than a single-family dwelling (or farm property), and the signed homeowner verification. | § 81-2121(5); handout |
| 119, 559 | Quotes § 81-2121(5) as "principal residence, if such residence is not larger than a single-family dwelling, or farm property..." — fine at 119; at 559 says "exempts an owner from licensing" — fine — but both omit that **inspection and the request for inspection still apply** and that not filing is now a **Class IV felony** | Add §§ 81-2124(3), 81-2126, 81-2129, 81-2143(1)(c) (eff. 7-18-2026) | |
| 129, 559 | "often in person — Omaha requires an appointment with the Chief Electrical Inspector" | Unverified (Omaha pages unreachable) and stale: SED's online system launched April 13, 2026; homeowner permits are linked by SED staff after account registration. | SED page |
| 189 | "State electrical permit … roughly $0.06/sq ft for new residential plus base fees" | Fees are **$75 for a new service 1–400 A + $10 per branch circuit; homeowner minimum $100** (3-27-26 form). | SED application form |
| 377, 508, 575 | RRNC "apply statewide — not just in EPA Zone 1, and not only where there's a local building department" / "required statewide" | **Two statutory exemptions**: any project "utiliz[ing] the design of an architect or professional engineer," and counties with average radon **< 2.7 pCi/L** (14 counties in DHHS's latest table). | § 76-3505(1)–(2); DHHS report |
| 383–384, 575 | "at least 4 inches of clean aggregate under the slab"; "A vapor retarder over the aggregate"; "4-inch sub-slab aggregate layer" | Not in the statute. § 76-3504 requires the ≥3-inch gas-tight pipe in "subslab permeable material," the sump lids, the roof termination/10-ft clearances, labels, and the attic junction box. Label aggregate depth and vapor retarder as practice. | § 76-3504 |
| 431 | "many systems require a registered professional" | **All** systems: no siting, layout, construction, repair or inspection unless "carried out or supervised by" a certified professional, PE or REHS who is **physically present**. An owner cannot self-install. | § 81-15,248(1); Title 124 ch. 9 § 004 |
| 445 | "Water wells must be constructed by a licensed Nebraska water-well contractor" | An individual **may** construct a well (and install the pump) "on land owned by him or her and used … as his or her place of abode," to the Title 134 standards, and registers it within 60 days. | § 46-1233(2); § 46-602(1) |
| 492 | "Nebraska DHHS (on-site wastewater) and DWEE (wells)" | Onsite wastewater is **DWEE** (Title 124; § 81-15,248 "department"). DHHS is **radon**. | § 76-3503(3); Title 124 |
| 163, 169 | "seller-disclosure obligations that follow the home for years after a sale" / "Owner-built homes don't have to be labeled as such" | § 76-2,120 applies at a sale of residential real property; a transfer "Of newly constructed residential real property which has never been occupied" is **exempt** ((6)(k)); liability is limited to the seller's personal knowledge ((8)). Rewrite. | § 76-2,120(6)(k), (8) |
| 298, 571 | "You may see older references to a Zone 4A sliver in the far southeast; under the 2018 IECC table Nebraska uses, the whole state is treated as Zone 5" | Keep Zone 5 (DWEE: "entire state … in a single climate zone (5)"); drop the 4A speculation. | DWEE Energy Impact Study |
| 294, 571 | "the state (… DWEE) is the backstop authority" | Precisely: with no local energy code the **prime contractor** (the owner-builder) "shall build … to the best of his or her knowledge, according to the Nebraska Energy Code"; DWEE acts on a written request or within two years of first occupancy. | §§ 81-1622, 81-1616, 81-1625 |
| 149 | "energy-code compliance documentation (e.g., a Nebraska Energy Code certificate)" | No state certificate exists. | § 81-1608–1626 (absence) |
| 551 | "build to the Nebraska State Building Code (the 2018 IRC)" in "Omaha, Lincoln, Bellevue, and most municipalities" | **Lincoln is on the 2021 IRC/UPC/IMC/IEBC, 2023 NEC, 2018 IECC.** | Lincoln codes page |
| 373, 575 | "53 of its 93 counties are in EPA Radon Zone 1"; "statewide indoor average runs well above the EPA's 4 pCi/L" | Not from a Nebraska source. DHHS: **77 of 93 counties exceed 2.7 pCi/L** (Oct 2018–Sep 2023). | DHHS § 76-3507 report |

### 12.2 Hedges on statewide rules (wrong kind of hedge)

| Line | Guide says | Why wrong | Cite |
|---|---|---|---|
| 58 | "Applies to: One- and two-family dwellings **where enforced**" | The code "shall be the legally applicable code regardless of whether the county, city, or village has provided for the administration or enforcement." | § 71-6406(7) |
| 85 | "the statewide energy code, the state electrical program, and the radon-construction requirement still apply **in principle**" | They apply by statute, and so does the IRC/UPC. Delete "in principle." | §§ 71-6406(7), 81-1614, 81-2124(3), 76-3504 |
| 141, 587 | "there may be no plumbing/HVAC permit at all" | True for the permit; but the **2018 UPC applies** to every building in an unincorporated county without a plumbing resolution. | § 23-172(4) |
| 112, 30 | "Cities and counties that enforce a building code allow homeowners to pull their own building permits on an owner-occupied primary residence" | Statewide generalisation from one city. Lincoln verified (owner; reside; not for sale/rental; 120-day permit). Say "Lincoln does; ask yours." | Lincoln pages |
| 94, 327–335, 461, 481, 524 | Frost depth "42 inches" Omaha; "~36–42" elsewhere | No state table; Omaha unverified. Replace with "IRC Table R301.2 is filled in by your jurisdiction — get the figure in writing." | § 71-6406(7); absence |
| 117, 502, 555 | "a few jurisdictions that run their own approved municipal/county electrical inspection programs" | **Five counties and fourteen cities** (SED GIS, Sept 2026); La Vista and Waverly are state-inspected. Point at the map. | § 81-2125; GIS layer |
| 152 | "jurisdictions that enforce a code may scrutinize repeated owner-builder permits that look like speculative building" | Unsupported. The real rule: a spec builder is a "contractor" under the Registration Act and outside the § 81-2121(5) principal-residence exemption. | § 48-2103(3); § 81-2121(5) |

### 12.3 Unverified figures to delete or label

Lines 184–249 (all permit/plan-review/tap-fee dollar figures and percentages),
259–264 (hidden-fee amounts), 280–286 (processing times, including Douglas
"15 days" and Lincoln "next business day"), 391 and 402 (radon and safe-room
costs, HMGP "up to 75%"), 425–427 and 439–441 (septic and well costs), 463
"$200–$400 well permit" (actual: $200 + $25–40 registration; no "permit"
for a domestic well). None traceable to a primary source; Omaha/Douglas
sources unreachable.

### 12.4 Material omissions

1. **Contractor Registration Act** — never mentioned. Owner exempt
   (§ 48-2104(1)); every hired trade must be registered ($40/yr); the DOL
   registry shows workers'-comp status; the owner's § 48-116 protection is to
   require the contractor's policy.
2. **§ 71-6406(3)(a)** — no local government may run a prior edition; and
   § 71-6406(7) — the code applies without enforcement.
3. **§ 71-6409 (2026)** — virtual inspections; **no self-inspection**.
4. **§ 81-2129** — no utility connection without the owner's certificate;
   § 81-2134(3) — inspections within one week; rough-in before concealment;
   § 81-2126 — $250 late fee; § 81-2143 — **Class IV felony from July 18,
   2026**; Board Rule 13 — 5-month permit life; homeowner minimum fee $100;
   SED online system (April 13, 2026).
5. **Title 124 Table 2.1 setbacks**, the **$140 registration / $450 permit**
   fees, the general-permit sizing tables, and the **owner-cannot-install**
   rule.
6. **Well**: owner-drill right, 60-day registration, $200 + $25–40, well log,
   Title 134 (2026) Chart 1 distances.
7. **County zoning permits** for nonfarm buildings (§ 23-114.04) and the
   county's discretion over farmstead residences (§ 23-114.03); city ETJ
   (§§ 14-419, 15-905).
8. **Sprinklers**: locals may adopt R313 (§ 71-6406(2)(c)(iii)).
9. **Energy**: § 81-1622 builder duty; § 81-1625 two-year order; § 81-1626
   Class IV misdemeanor; DWEE fact-sheet values (already matched) and Manual J
   / ventilation requirements.
10. **Liens**: 120-day recording (§ 52-137); owner-builder is a "protected
    party" (§ 52-129); notice-of-right-to-assert-lien warning (§ 52-135).
11. **One-Call**: two full business days (§ 76-2321).
12. **Sarpy County** unincorporated: 2018 codes by Resolution 2024-150 (IPC,
    not UPC); **Lincoln 2021** editions.
13. **Radon exemptions and the DHHS county list**; DHHS vs DWEE roles.
14. Class B electrical licensees cannot work in Omaha or Lincoln
    (§ 81-2102(4)–(5)) — relevant when hiring.
