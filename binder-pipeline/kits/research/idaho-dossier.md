# Idaho Owner-Builder Permit Kit — Research Dossier

Kit 21 of the 50-state program. Compiled September 2026 for
`binder-pipeline/kits/id-permit-kit/` (ID.0–ID.5).

**Marking convention.** `[V]` = read in a primary source and quoted here.
`[H]` = secondary, inferred, or reasoned — not printed in the kit as a
citation. Anything unverifiable was deleted rather than softened.

**Primary sources used.**

| Source | What it is | Where |
|---|---|---|
| Idaho Code Title 39, ch. 41 (§§ 39-4101–39-4129) | Idaho Building Code Act | legislature.idaho.gov/statutesrules/idstat/Title39/T39CH41/ |
| Idaho Code § 39-9701 | Idaho Energy Conservation Code (2018 IECC pinned by statute; local preemption) | …/Title39/T39CH97/ |
| Idaho Code Title 54, ch. 52 (§§ 54-5201–54-5217) | Idaho Contractor Registration Act | …/Title54/T54CH52/ |
| Idaho Code Title 54, ch. 10 (§§ 54-1001–54-1019) | Electrical Contractors and Journeymen (2023 NEC adopted by statute) | …/Title54/T54CH10/ |
| Idaho Code Title 54, ch. 26 (§§ 54-2601–54-2630) | Plumbing and Plumbers | …/Title54/T54CH26/ |
| Idaho Code Title 54, ch. 50 (§§ 54-5001–54-5024) | Installation of HVAC Systems | …/Title54/T54CH50/ |
| Idaho Code §§ 42-111, 42-227, 42-235, 42-238 | Domestic-use definition; domestic wells exempt from water-right permit; drilling permit; driller licensing | …/Title42/ |
| Idaho Code §§ 55-2501–55-2508 | Property Condition Disclosure Act | …/Title55/T55CH25/ |
| Idaho Code § 72-212 | Workers' compensation exemptions | …/Title72/T72CH2/ |
| Idaho Code §§ 45-501, 45-507, 45-525 | Mechanics' liens; general-contractor disclosure | …/Title45/T45CH5/ |
| Idaho Code § 41-253 | International Fire Code adoption; 5-acre rural dwelling exemption from IFC water/access | …/Title41/T41CH2/ |
| IDAPA 24.39.30 | Rules of Building Safety (Building Code Rules) — IRC/IBC/IECC editions and Idaho amendments; DOPL fee table | adminrules.idaho.gov/rules/current/24/243930.pdf |
| IDAPA 24.39.10 | Rules of the Electrical Board — Idaho amendments to 2023 NEC; permits, fees | …/24/243910.pdf |
| IDAPA 24.39.20 | Rules Governing Plumbing — 2015 UPC adopted as Idaho State Plumbing Code; homeowner permits, fees | …/24/243920.pdf |
| IDAPA 24.39.70 | Rules Governing HVAC — 2018 IMC/IFGC/IRC Parts V–VI; homeowner permits, fees | …/24/243970.pdf |
| IDAPA 58.01.03 | DEQ Individual/Subsurface Sewage Disposal Rules — permit, installer registration, owner-install exemption, separation tables, sizing | adminrules.idaho.gov/rules/current/58/580103.pdf |
| IDAPA 37.03.09 | IDWR Well Construction Standards Rules — separation table, drilling permit, owner duties | …/37/370309.pdf |
| IDAPA 37.03.10 | IDWR Well Driller Licensing Rules | …/37/370310.pdf |
| DOPL program pages | Building, Electrical, Plumbing, HVAC, Contractor Registration; inspector-by-city list | dopl.idaho.gov/bld/, /ele/, /plb/, /hvac/, /con/ |
| Idaho Legislature bill lists 2023–2026 | Session-law chapter ↔ bill mapping (H0337=2023 ch. 244, H0266=2025 ch. 221, S1164=2025 ch. 272, H0585=2026 ch. 232, H0721=2026 ch. 277) | legislature.idaho.gov/sessioninfo/{year}/legislation/ |

> **Fetching note for future revisions.** `legislature.idaho.gov` serves
> every statute section at a predictable URL
> (`/statutesrules/idstat/Title54/T54CH10/SECT54-1016/`) and returned HTTP 200
> to curl with a browser User-Agent; each section prints a `History:` line
> naming every session law that amended it — the fastest way to catch a
> renumbering. `adminrules.idaho.gov` serves each IDAPA chapter as one PDF at
> `/rules/current/{title}/{chapter}.pdf` (e.g. `/24/243930.pdf`); the chapter
> index pages 404 but the PDFs are fine and `pdftotext -layout` extracts them
> cleanly, including the tables. Every rule paragraph carries an effective
> date in parentheses (`(7-1-24)`, `(4-4-25)`), which is how to tell what
> changed. `dopl.idaho.gov` is WordPress; the content lives inside `<main>`,
> so a naive HTML-stripper that drops nav returns nothing — extract the
> `<main>` element. The DOPL "FAQ" pages for building and contractors 404.

---

## 0. THE HEADLINE — WHAT MAKES THIS KIT DIFFERENT

Idaho is the state where **the building permit is optional but the trade
permits are not**, and where the exemptions everyone quotes are narrower on
paper than the DOPL web pages make them sound.

Idaho's Building Code Act does not impose a building permit on a private
house. It *authorizes* cities and counties to adopt and enforce a building
code (§ 39-4103(1), § 39-4116(1)), and the Division of Occupational and
Professional Licenses (DOPL) enforces the Act only for the buildings the Act
puts under the state — state-owned buildings, public schools, modular and
manufactured units (§ 39-4103(2), § 39-4116(7)). Where a county or city has
not adopted an ordinance, there is no residential building permit, no plan
review, no building inspection and no certificate of occupancy. **DOPL is not
the default building department for your house** — the published state guide
says it is, and that claim is false. `[V]`

But three permits survive that gap and each one is statewide:

1. **An electrical permit** — from DOPL wherever no city or county runs its
   own electrical program (§ 54-1001B), enforced at the meter: the power
   supplier "shall not connect with or energize any electrical installation
   … unless an inspection has been conducted and resulted as 'passed'"
   (§ 54-1005(3)). `[V]`
2. **A plumbing permit** — from DOPL wherever no local program exists
   (§ 54-2620(1)), including a homeowner doing his own work (§ 54-2620(2);
   IDAPA 24.39.20.500.01.b). `[V]`
3. **An HVAC permit** — "from the authority having jurisdiction," statewide
   (§ 54-5016(1)), which is DOPL where no local mechanical program exists.
   `[V]`

Plus the two land approvals that never depended on the building code: the
health-district septic installation permit (IDAPA 58.01.03.005) and the IDWR
well drilling permit (§ 42-235). `[V]`

Six findings carry the kit:

1. **No county or city may require a building permit that DOPL would issue
   for a house; "opt out" means nothing is issued.** The Act's permit
   section is two clauses: a permit "from the division" for buildings "coming
   under the purview of the division," and a permit "in accordance with the
   applicable ordinance" in "a local government jurisdiction enforcing
   building codes" (§ 39-4111(1)–(2)). A private house in a non-enforcing
   county is in neither clause. `[V]`
2. **The homeowner electrical exemption is a LICENSE exemption only**
   (§ 54-1016(2): "The licensing provisions of this chapter shall not apply
   to … any property owner performing noncommercial electrical work in the
   owner's primary or secondary residence or associated outbuildings"). The
   permit duty (§ 54-1005(4)) and the utility lock (§ 54-1005(3)) are
   untouched. `[V]`
3. **The plumbing and HVAC homeowner exemptions are broader than the
   electrical one and say nothing about "primary or secondary residence."**
   § 54-2602(1)(a) and § 54-5002(1)(a) exempt "any person who does
   [plumbing/HVAC] work in a single or duplex family dwelling … provided that
   such person owns or is a contract purchaser of the premises." No
   occupancy test, no not-for-sale clause, and a contract purchaser
   qualifies. The published guide's "not for sale, rent, or lease" language
   appears in no Idaho statute or rule that this research could find. `[V]`
4. **Idaho amends the 2023 NEC sharply downward for dwellings** — AFCI
   required only on bedroom circuits; the laundry-area, food-prep-area,
   250-volt, appliance-specific (dishwasher, range, oven, cooktop, dryer,
   microwave) and garage/accessory-building GFCI list items deleted (kitchens
   themselves stay GFCI); surge protection and the emergency disconnect made
   permissive (IDAPA 24.39.10.600.01). A
   homeowner wiring to the national book will over-build; one reading a
   2020-NEC video will miss Idaho's own island-receptacle rule. `[V]`
5. **The energy code is pinned to the 2018 IECC by statute, preempts every
   local energy rule, and Idaho's own Table R402.1.2 sets Climate Zone 5
   ceilings at R-38 and lets the permit holder choose a visual inspection in
   lieu of a blower-door test** (§ 39-9701; IDAPA 24.39.30.600.06). `[V]`
6. **Every inspection in Idaho now carries a statutory 48-business-hour
   clock with a self-help remedy**: if an inspection is not performed within
   48 business hours the permit holder may hire a qualified third-party
   inspector and is refunded the inspection fee (§ 39-4118, § 54-1004A,
   § 54-2626A, § 54-5020A — 2025 and 2026 session laws). For contrast, the
   Pennsylvania dossier's verified finding was that no inspector-response
   deadline exists anywhere in that scheme. `[V]`

And one trap: **the 2024 I-Code update was rejected by the Idaho House
Business Committee in February 2026**, so the 2018 IRC (with a 2020
Idaho-branded cover) remains in force with no successor scheduled. See § 9.

---

## 1. THE CENTRAL THESIS — WHO ENFORCES

### 1.1 The Act authorizes; it does not impose `[V]`

§ 39-4103(1): "This chapter authorizes the state division of occupational
and professional licenses and local governments to adopt and enforce building
codes pursuant to the provisions of this chapter."

§ 39-4104: "The administrator of the division … shall enforce the provisions
of this chapter that apply to the state. Local governments that adopt
building codes shall enforce all of the provisions of this chapter that
govern application by local governments."

§ 39-4103(2): the buildings expressly placed under DOPL are "all buildings
and other facilities owned by any state government agency or entity."
§ 39-4116(7): "The division shall retain jurisdiction for in-plant
inspections and installation standards for manufactured or mobile homes and
for in-plant inspections and enforcement of construction standards for
modular buildings and commercial coaches." § 39-4113(1): DOPL runs "a program
for plan reviews and permit issuance entirely within the division" for
buildings "within the scope of the division's jurisdiction pursuant to this
chapter."

**Nothing in the chapter places a privately owned one- or two-family
dwelling within the division's jurisdiction.** DOPL's own Building program
pages (September 2026) list plan-review and permit forms for "Building,"
"Manufactured Housing" and "Modular," and its inspector roster describes a
"Building/Industrial Safety Program" and a "Safety Program Specialist
(Industrial and School Safety)" — no residential inspection function.
`[V]` The DOPL inspector-by-city list (dated 5 August 2026) carries three
columns — **ELECTRICAL, HVAC, PLUMBING** — and no building column. `[V]`

**DOPL's own Plan Review Application form (revised 12 September 2023), verbatim** `[V]`:

> "The Division of Occupational and Professional Licenses is responsible for
> projects owned by the State of Idaho or any of its departments or agencies
> … **DOPL does NOT issue building permits for projects not owned by the
> State. Contact the local government for these projects.**"

That sentence, on the agency's own form, is the citation for the kit's
central correction. Print it.

### 1.2 The permit section, verbatim `[V]` — § 39-4111

> "(1) It shall be unlawful for any person to do … any construction … of any
> building, residence or structure, **coming under the purview of the
> division**, in the state of Idaho without first procuring a permit from
> the division …
> (2) It shall be unlawful for any person to do … any construction … of any
> building, residence or structure **in a local government jurisdiction
> enforcing building codes**, without first procuring a permit in accordance
> with the applicable ordinance or ordinances of the local government."

Read the two clauses together: a private house in a county that has not
adopted a building-code ordinance is outside both. That is the whole
"no-permit county" phenomenon, and it is statutory, not a gap in
enforcement.

§ 39-4111(3) is worth printing for anyone adding to an existing house: no
permit may require unaffected existing parts to be upgraded if they complied
when built, unless the jurisdiction proves "a specific substantial safety
hazard," and "the burden shall be upon the division or enforcing
jurisdiction to prove" it.

### 1.3 How a local government becomes an enforcing jurisdiction `[V]` — § 39-4116

- (1) "Local governments enforcing building codes shall do so only in
  compliance with the provisions of this section. Local governments that
  have not previously instituted and implemented a code enforcement program
  … may elect to implement a building code enforcement program by passing an
  ordinance evidencing the intent to do so. Local governments may contract
  with a public or private entity to administer their building code
  enforcement program."
- (2) An enforcing local government "shall, by ordinance effective January 1
  of the year following the adoption by the Idaho building code board, adopt
  … (a) International Building Code …; (b) Idaho residential code, parts
  I-III and IX; and (c) 2018 Idaho energy conservation code." "Local
  jurisdictions shall not adopt provisions … of subsequent versions of the
  International Residential Code or residential provisions of the
  International Energy Conservation Code … that have not been adopted by the
  Idaho building code board."
- (4) Local amendments must "establish at least an equivalent level of
  protection"; (4)(b) a local jurisdiction "shall not adopt any provision …
  that [has] been expressly rejected or exempted … by the Idaho building code
  board"; (4)(c) locals **may amend by ordinance** IRC "Part I,
  Administrative; Part II, Definitions; Part III … **Section R301, Design
  Criteria**; and Part IX, Appendices"; (4)(d) the rest of Part III only on a
  finding of "good cause for building or life safety," after a public hearing
  with 30 days' written notice to the § 39-4109(5) entities.
- (6) "**Permits shall be governed by the laws in effect at the time the
  permit application is received.**"

Consequence for the kit: **snow load, frost depth, wind, seismic and
flood-hazard design criteria are the one part of the structural code Idaho
hands to the county by name** (R301 is Design Criteria, and Table R301.2(1)
is the local design-criteria table). Everything else in Part III is
uniform unless a county has run the § 39-4116(4)(d) hearing process.

### 1.4 The three trade programs are state programs with a local opt-in `[V]`

**Electrical — § 54-1001B(1):** state inspection provisions "shall not
apply: (a) Within cities or counties that, by ordinance or building code,
prescribe the manner in which wires or equipment … shall be installed,
provided that the provisions of the Idaho electrical code are used as the
standard … and provided that actual inspections are made; or (b) Within
cities or counties that receive inspections from another city or county that
conducts inspections pursuant to paragraph (a)." (4): a city or county
choosing to run its own program gives DOPL 30 days' written notice. (5): if a
local program terminates, DOPL "shall provide electrical code enforcement
services in the jurisdiction for a minimum of one (1) year."

**Plumbing — § 54-2620(1):** unlawful to do any plumbing "in the state of
Idaho without first procuring a permit from the division … except: (a)
Within the boundaries of counties or incorporated cities … where such work
is regulated and enforced by an ordinance or code equivalent to this chapter
pursuant to … section 54-2601"; (b) within a city's 5-mile sewer-conversion
area under § 50-606. § 54-2601(2)–(8) mirror the electrical opt-in mechanics
(ordinance, 30 days' notice to DOPL, one-year DOPL backstop on termination).

**HVAC — § 54-5016(1):** on and after 1 January 2005, unlawful to install any
HVAC system "in any building, residence or structure in the state of Idaho
without first obtaining a permit from the authority having jurisdiction …
except that no permit shall be required to perform work related to repair
or maintenance of an existing HVAC system." § 54-5001: "Nothing in this
chapter shall require a local government to adopt or implement a mechanical
inspection program unless such local government chooses to do so by an
ordinance duly adopted." § 54-5005 (last paragraph): where a local
government has adopted mechanical codes, the state HVAC board's powers
"shall be limited to those … needed to enforce the requirements governing a
certificate of competency."

**Licensing, by contrast, is exclusively state** — § 54-1002(5) (electrical:
"no local jurisdiction shall have the authority to require additional
licensure or registration or to require payment of any fees"); § 54-5015(2)
(HVAC, same); § 54-2619 (plumbing: no local occupational-license fees from
state-certified plumbers "except those counties or cities that have
qualified plumbing inspectors"); § 54-5213(1) (contractors: after 1 January
2007 "no incorporated municipality, county … shall implement its own program
for the registration or licensure of construction contractors").

### 1.5 The permit enforced by the utility `[V]` — § 54-1005(3)–(4)

> "(3) Individuals, firms, cooperatives, corporations, or municipalities
> selling electricity, hereinafter known as the power supplier, shall not
> connect with or energize any electrical installation, coming under the
> provisions of this chapter, unless an inspection has been conducted and
> resulted as 'passed' by the administrator, covering the installation to be
> energized. Electrical installations approved by the board and addressed
> through administrative rule may be connected and energized by the power
> supplier after the purchase of an electrical permit by a **licensed
> electrical contractor**.
> (4) It shall be unlawful for any person … other than a power supplier to
> energize any electrical installation coming under the provisions of this
> chapter prior to the purchase of an electrical permit covering such
> installation."

The rule that implements the second sentence is **IDAPA 24.39.10.200.04**:
"At the request of a **licensed electrical contractor** and upon receipt of a
copy of an electrical permit, a power supply company may connect and energize
an electrical service, to the line side of the service disconnect, prior to a
passed inspection in the following situations: to preserve life or property
or to provide **temporary service for construction**."

**Kit consequence:** a homeowner on a homeowner electrical permit cannot get
temporary construction power energized ahead of a passed inspection — that
door is open only to a licensed contractor's permit. Print it in ID.3 as the
first decision on the electrical track.

"Cooperatives" are named — a rural electric co-op is bound.

### 1.6 Contractor registration numbers on the permit face `[V]` — § 54-5209

> "(1) … no building inspector or such other authority of any county,
> municipality or district charged with the duty of issuing building permits
> or other permits for construction of any type shall issue any permit
> without first requesting presentment of an Idaho contractor's registration
> number. Such registration number presented shall be conspicuously entered
> on the face of a permit so issued; provided however, a permit may be issued
> to a person otherwise exempt from the provisions of this chapter provided
> such permit shall conspicuously contain the phrase '**no contractor
> registration provided**' on the face of such permit. No authority charged
> with the duty of issuing such permit shall be required to verify that the
> person applying for such permit is exempt as provided in this chapter.
> (2) All building permits or other permits for construction of any type
> shall be posted at the construction site in such a manner that the
> conspicuous statements set forth in subsection (1) of this section are
> visible.
> (3) No person engaged in construction activities who is otherwise exempt
> as set forth in section 54-5205, Idaho Code, shall be required to have a
> contractor registration number."

This is the statutory root of the "owner-builder exemption declaration"
forms counties hand out. The form is local; the phrase on the permit face
and the posting duty are state law. `[V]`

### 1.7 Appeals `[V]`

§ 39-4107(2): the Building Code Board "shall function as a board of appeals
for the division as prescribed in the adopted building code" — i.e. for
buildings under DOPL — with decisions "in writing … within ten (10) working
days of the conclusion of a hearing," heard by a panel of at least three
members; the board "shall have no authority to waive any requirements of the
codes." § 39-4120: appeals to the board "by persons affected by any code,
rule, regulation or decision applicable to buildings **within the
jurisdiction of the division**," heard within 20 days of notice.

**For a house in an enforcing county the appeal body is local** — the IRC
Section R112 board of appeals as adopted (and amendable, being Part I) by
the local ordinance. Verified negative: no statute gives an owner in an
enforcing county a state-level appeal. `[V]` Trade decisions: the
electrical, plumbing and HVAC boards hear appeals of civil penalties
(§ 54-1006(5), § 54-2606(3)(f), § 54-5005(3)); the trade chapters are silent
on appeals of an inspector's correction notice, so ID.3 tells the reader to
ask the inspector's supervisor in writing and cites nothing.

### 1.8 Penalties `[V]`

| Statute | Offense | Penalty |
|---|---|---|
| § 39-4126 | Willful violation of the Building Code Act or adopted codes | Misdemeanor, ≤ $300 and/or ≤ 90 days; each building and each day a separate offense |
| § 54-1017 | Electrical: unlicensed work, or any violation of chapter or rules | Misdemeanor + civil penalty ≤ $3,000 per violation (rule: ≤ $1,000 per count, IDAPA 24.39.10.300); each day separate |
| § 54-2628 | Plumbing: work without certificate "or perform work without a permit" | Misdemeanor, $10–$300 and/or ≤ 30 days |
| § 54-5022 | HVAC: work without certificate or "without a permit" | Misdemeanor; civil penalty ≤ $1,000; each day separate |
| § 54-5017(4) | HVAC: failure to acquire, post and send permit | Double fee; triple fee on repeat within 12 months |
| § 54-5217 | Contracting without registration | Misdemeanor ≤ $1,000 and/or ≤ 6 months; **no right to sue for compensation** (§ 54-5217(2)); **lien rights waived** (§ 54-5208) |
| § 42-235 | Drilling a well without a drilling permit | Misdemeanor + § 42-1701B enforcement |

---

## 2. SCOPE — WHAT IS OUTSIDE THE CODE

### 2.1 Statutory exemptions from the Building Code Act `[V]`

§ 39-4103(4): industrial chemical-process and mineral-extraction equipment;
modular buildings built in Idaho for out-of-state sites.

§ 39-4116(5) — **agricultural buildings**, and the definition that keeps a
"barndominium" out of it: "Local governments shall exempt agricultural
buildings from the requirements of the codes enumerated in this chapter …
A county may issue permits for agricultural buildings to assure compliance
with road setbacks and utility easements, provided that the cost for such
permits shall not exceed the actual cost to the county of issuing the
permits." (a) lists livestock shelters, poultry buildings, barns, equipment
storage "used exclusively in agricultural operations," horticultural
structures, sheds "used as part of an agricultural operation," grain silos,
stables, and any structure "designed, constructed, and intended to house,
accommodate, or store farm implements, hay, grain, poultry, livestock, or
other horticultural products." (b): "'agricultural buildings' does not
include: (i) **A place of human habitation, which means a space in a
building for living, sleeping, or cooking.** Structures with bathrooms,
shower rooms, break rooms, locker rooms, storage or utility space, or other
similar areas are not considered places of human habitation; (ii) A place of
employment where agricultural products are processed …; or (iii) A place
used by the public." (c) (2025 ch. 40): "Counties shall not alter, amend,
deny, limit, or narrow the exemption … by … requiring size limitations …
maximum travel distances to exits … or requiring installation of automatic
sprinkler systems."

Parallel ag exemptions: § 54-2602(1)(b) (plumbing certificate not required
for farm buildings outside city limits unless on public water/sewer — "This
definition does not include a place for human habitation"); § 54-5002(1)(b)
(HVAC, same); § 54-5205(2)(g)–(h) (contractor registration: farmers and
ranchers; builders of § 39-4116-exempt ag buildings). **Plumbing permits
"shall not be required" for § 54-2602(1)(b) farm buildings**
(§ 54-2620(2)). No electrical parallel exists — § 54-1016 has no farm-building
exemption. `[V]` (verified absence)

### 2.2 The IRC's own permit exemptions, as amended `[V]` — IDAPA 24.39.30.600.03.b–c

Idaho keeps IRC R105.2's list (one-story detached accessory structures
≤ 200 sq ft, fences ≤ 7 ft, retaining walls ≤ 4 ft, sidewalks and driveways,
painting, decks ≤ 200 sq ft not more than 30 in above grade, etc.) and
amends two items: swimming pools are exempt up to **4 feet** deep (R105.2
item 7, "24 inches" replaced with "four (4) feet"), and adds "11. Flag
poles." These matter only in an enforcing jurisdiction; Part I is locally
amendable (§ 39-4116(4)(c)(i)), so print with the verification step.

IDAPA 24.39.30.500.02 (DOPL's own permits): "Plans are not required for
group U occupancies of Type V conventional light-frame wood construction."

### 2.3 Sprinklers — a statutory negative `[V]` — § 39-4116(3)

"All single family homes and multiple family dwellings up to two (2) units
are hereby exempted from the provisions of the International Fire Code, the
International Building Code and the Idaho residential code that require such
dwellings to have automatic fire sprinkler systems installed. Nothing in this
section shall prevent any person from voluntarily installing" one. Repeated
in rule: IRC R313.2 "Delete" (IDAPA 24.39.30.600.03.j). Townhouses: R313.1
exception rewritten so sprinklers are not required where two 1-hour walls or
a common 2-hour wall separates units (600.03.i).

### 2.4 Rural fire-code relief `[V]` — § 41-253(2)

"A detached single family dwelling, to be constructed upon lands of **five
(5) acres or more** outside an incorporated city and not within a designated
area of city impact, shall be exempt from the water supply and access
requirements of the adopted version of the International Fire Code unless a
county land use or subdivision ordinance requires such compliance." A county
may widen the exemption by ordinance after a hearing. The IFC edition is
whatever "later editions as may be … adopted by the state fire marshal"
(§ 41-253(1)) — not verified here; the kit cites the exemption, not an
edition.

### 2.5 EV infrastructure — a statutory prohibition `[V]` — § 39-4109B (2025)

"[N]either the state of Idaho nor any local government in Idaho shall adopt
any requirement that an electric vehicle (EV) charging station, a designated
EV parking space, an upgraded electrical conduit, or other infrastructure for
the purpose of EV charging station installation be included in a building
plan." Supersedes local ordinances.

### 2.6 What the owner-builder exemption does NOT reach

- **Septic:** any person installing a system needs an installation permit
  (IDAPA 58.01.03.005.01) — but an **installer's registration permit is not
  required for "owners installing their own standard or basic alternative
  system as described in the TGM"** (58.01.03.006.08.b). Complex systems
  (pressure distribution, sand mounds, ETPS, etc.) need a registered complex
  installer. `[V]`
- **Wells:** no owner-drilling exemption exists. § 42-238(2): "It shall be
  unlawful for any person to drill a well in Idaho, including wells excepted
  under sections 42-227 and 42-228, Idaho Code, without first complying with
  the provisions of this chapter." § 42-238(3): "a 'person' shall be defined
  as **any individual who drills or abandons any well for himself or
  another** in this state." IDAPA 37.03.09.025: "All persons constructing
  wells must comply with the requirements of Section 42-238, Idaho Code, and
  IDAPA 37.03.10, 'Well Driller Licensing Rules.'" `[V]` (Water *pump*
  wiring and the service line from pump to pressure tank have their own
  limited licenses — IDAPA 24.39.10.200.05.g; 24.39.20.100.04.e — which do
  not bar a homeowner working under the homeowner exemptions.)

---

## 3. CODE EDITIONS AND AMENDMENTS

### 3.1 Editions in force `[V]`

| Code | Edition | Where adopted | Notes |
|---|---|---|---|
| Idaho Residential Code | **2018 IRC Parts I, II, III and IX** with Idaho amendments | § 39-4109(1)(b); IDAPA 24.39.30.600.03 (rule text effective 7-1-24) | Parts IV–VIII "as they pertain to energy conservation, mechanical, fuel gas, plumbing and electrical" are excluded by statute. ICC sells this as the "2020 Idaho Residential Code" — same 2018 base. |
| Idaho Building Code | 2018 IBC + 2021 IBC mass-timber provisions | IDAPA 24.39.30.600.01–.02; § 39-4109A | Non-residential and 3+ family |
| International Existing Building Code | 2018 | IDAPA 24.39.30.600.04 | |
| Idaho Energy Conservation Code | **2018 IECC** (residential and commercial) with Idaho amendments | **§ 39-9701(1)** (statute); § 39-4109(1)(c); IDAPA 24.39.30.600.05–.06 | Statutorily pinned; see § 3.6 |
| Idaho Electrical Code | **2023 NEC** with Idaho amendments | **§ 54-1001** (statute, 2023 ch. 244 = H0337); IDAPA 24.39.10.600 (amendments effective 4-4-25) | See § 3.5 |
| Idaho State Plumbing Code | **2015 Uniform Plumbing Code**, Appendices A, B, C, D, E, G, I, J, K, L, with Idaho amendments | § 54-2601; IDAPA 24.39.20.600 (3-28-23) | Not the IPC |
| Idaho Mechanical Code | **2018 IMC** (App. A), **2018 IFGC** (App. A–D), **2018 IRC Parts V and VI** (App. A–D) | § 54-5001; IDAPA 24.39.70.600 (3-28-23) | |

**How editions change — and why the guide's "by statute" claim is half
right.** § 39-4109(1)(b): the IRC edition is whatever "version … adopted by
the Idaho building code board … through the negotiated rulemaking process";
(4): "Any edition of the building codes adopted by the board will take effect
on January 1 of the year following its adoption"; (5): two public hearings at
least 60 days apart with written notice to fourteen named organizations.
**The energy code is different**: § 39-4109(1)(c) and § 39-9701(1) fix "the
2018 Idaho energy conservation code … as amended … by the Idaho building code
board and **approved by the legislature**." And the NEC edition is set
directly in § 54-1001 (2023 NEC "is hereby adopted by the Idaho
legislature"). So: IRC/IBC by Board rule (subject to Idaho's legislative
rules review, which is what killed the 2026 update); IECC edition and NEC
edition by statute. `[V]`

**Amendment ceiling** — § 39-4109(3): "No amendments to the Idaho residential
building code shall be made by the Idaho building code board that provide for
standards that are more restrictive than those published by the
International Code Council." Every Idaho residential amendment loosens or
clarifies; none tightens. `[V]`

### 3.2 The rejected 2024 update `[V]`

**Docket 24-3930-2502** (Idaho Administrative Bulletin, 1 October 2025,
Vol. 25-10, p. 358 ff.): "The Division is proposing to incorporate by
reference the most recent editions of the International Codes, with
exceptions"; the proposed text struck "2018" and inserted "2024" for the IBC
and IECC and re-adopted the IRC on the 2024 edition. Public hearing 15
October 2025; the pending rule went to the 2026 Legislature.

**House Business Committee minutes, Tuesday 17 February 2026** `[V]`:

> "DOCKET NO. 24-3930-2502: Justin Touchstone, Trades Program Director, DOPL
> explained the board adopted the 2024 codes with amendments, citing safety,
> practicality and affordability as factors … MOTION: Rep. Thompson made a
> motion to reject Docket No. 24-3930-2502 due to the many concerns and
> questions regarding the proposed changes in addition to the incorporation
> by reference of the international code. Speaking to the motion, Rep. Crane
> (13) expressed his support of the motion, noting the need to create an
> Idaho Building Code. SUBSTITUTE MOTION: Rep. Berch made a substitute
> motion to HOLD Docket No. 24-3930-2502 in committee … Substitute motion
> failed by voice vote. [Original] Motion carried by voice vote. Reps. Berch
> and Cheatum requested to be recorded as voting NAY."

The committee's questions, as minuted, are a preview of what the next
attempt will fight over: "full house mechanical ventilation code, sealing of
registers and boots, recessed light fixtures … heat detector and
interconnected smoke alarm installation requirement in attached garages …
blower door test frequency."

**DOPL's Building statutes-and-rules page, September 2026** `[V]`: "These
boards are not currently engaged in rulemaking for 2026–2027. Existing rules
remain in effect." So: **2018 IRC/IBC/IEBC/IECC remain in force, the
current rule text carries 7-1-24 paragraph dates (fee Table 1-A 7-1-26), and
no successor edition is scheduled.** Print: "2018 edition; a 2024 update was
rejected by the Legislature's House Business Committee on 17 February 2026;
confirm the edition on your permit." Tripwire in § 9.

### 3.3 Idaho residential amendments that change what you build `[V]` — IDAPA 24.39.30.600.03

| Subject | Idaho text | Cite |
|---|---|---|
| Scope | R101.2 exception rewritten to bring owner-occupied lodging houses (≤ 5 guestrooms/10 occupants), small care facilities and ≤ 12-child day care within the IRC | 600.03.a |
| Windborne debris | R301.2.1.2 Protection of Openings — **deleted** | 600.03.d |
| Exterior wall fire separation | Table R302.1(1) replaced: walls need a 1-hour rating (both sides) only **< 3 ft** from the line; projections 1-hour underside/heavy timber/FRT ≥ 2 ft to < 3 ft; openings not allowed < 3 ft, 25 % max 3–5 ft, unlimited at 5 ft; footnotes drop the rating to 0 hours on eave undersides if fireblocked at the top plate and on rake overhangs without gable vents | 600.03.e |
| Garage separation | Table R302.6 replaced: **⅝-in Type X** on the garage side for the residence, attics, habitable rooms above and supporting structure; same for a garage < 3 ft from a dwelling on the same lot | 600.03.f |
| Floor fire protection | R302.13 — **deleted** (no membrane under I-joists) | 600.03.g |
| Ventilation | R303.4 replaced: "Dwelling units shall be provided with **whole-house mechanical ventilation** in accordance with Section M1505.4" — mandatory, not tied to an air-leakage threshold | 600.03.h |
| Sprinklers | R313.2 deleted; townhouse exception rewritten | 600.03.i–j |
| Alarms on alterations | R314.2.2 and R315.2.2 exception item 2 deleted | 600.03.k–l |
| Flood as-built elevation | R322.1.10 — deleted | 600.03.m |
| Footings | Tables R403, R403.1(1)–(3) deleted and replaced with Idaho **Table R403.1** (minimum width, in): 1-story light-frame 12 in at every soil value; 2-story 15/12/12/12 at 1,500/2,000/3,000/≥ 4,000 psf; 3-story 23/17/12/12; brick veneer and masonry columns as printed. R403.1.1 replaced: spread footings **≥ 6 in thick**, projections ≥ 2 in and ≤ footing thickness | 600.03.n–p |
| Wall bracing | R602.10 replaced: brace per R602.10, or R602.12 where applicable, "or the most current edition of **APA System Report SR-102** as an alternate method"; non-complying portions engineered under R301.1 | 600.03.q |

Not amended, therefore uniform statewide unless a county has used
§ 39-4116(4)(c)(iii): **R301.2 design criteria are locally set** (ground snow
load, frost depth, wind, seismic, weathering, ice-barrier, flood hazard,
termite). No statewide snow-load table or frost-depth figure exists in the
Act or the rule — verified absence across IDAPA 24.39.30. `[V]`

### 3.4 Plumbing amendments a house build hits `[V]` — IDAPA 24.39.20.600

- **Water service depth**: UPC 609.1 frost sentence replaced — "The cover
  must be not less than **forty-two (42) inches** below grade." (600.21) —
  the one statewide burial-depth number in Idaho.
- **Softener loop mandatory**: "All new one (1) and two (2) family residences
  built slab on grade or that will have a finished basement at the time of
  final inspection must have a pre-plumbed water softener loop. The kitchen
  sink must have one (1) hot soft line and one (1) cold soft line and one (1)
  cold hard line. Exterior cold hose bibbs intended for irrigation purposes
  must be piped with hard water." (600.26)
- Underground drainage/vent **≥ 2 in** (600.30); building sewer ≥ 4 in from
  the sewer connection to inside the foundation (600.39); cleanouts every
  50 ft in ≤ 2-in horizontal drains, full-size cleanout at the building
  drain/sewer junction (600.35).
- **Air admittance valves** allowed only in residential buildings, on island
  sinks in new construction, one floor each, never in attics/crawl spaces/
  outdoors/bathroom groups (600.46).
- Sidewall plumbing venting expressly acceptable on cabins and log homes
  (600.44.a).
- Dishwasher without air gap if the hose is looped to the countertop
  underside (600.43); water-hammer arrestors not required residentially
  (600.23); tracer wire not required where the pump wiring shares the
  water-line trench (600.19); frost-proof hose bibbs with integral backflow
  in freezing climates (600.15).
- Gray water: interior plumbing inspected by the plumbing AHJ; the exterior
  tank and irrigation by DEQ under IDAPA 58.01.03 (600.50).

### 3.5 ⚠ ELECTRICAL — the Idaho trap is a downward-amended 2023 NEC `[V]`

**Edition.** § 54-1001: "The 2023 National Electrical Code, NFPA 70, is
hereby adopted by the Idaho legislature. The 2023 National Electrical Code,
NFPA 70, together with any amendments, revisions, or modifications by the
Idaho electrical board through negotiated rulemaking shall collectively
constitute and be named the Idaho electrical code." Enacted by H0337, 2023
ch. 244. The Board's amendment paragraphs in IDAPA 24.39.10.600 carry the
rule effective date **(4-4-25)**.

**Amendments that change a house** — IDAPA 24.39.10.600.01:

| NEC 2023 section | Idaho action | Practical effect |
|---|---|---|
| 210.8(A) | "Delete reference to 250-volt receptacles" | Dwelling GFCI applies to 125-volt receptacles only |
| 210.8(A)(5) | Replaced: "Unfinished areas of basements" | Finished basement receptacles need no GFCI |
| 210.8(A)(6) | **Not amended** — "Kitchens" stays | Kitchen receptacles remain GFCI-protected |
| 210.8(A)(7) | **Deleted** (areas with sinks and permanent provisions for food/beverage preparation) | Wet bars, hobby rooms and other non-kitchen food-prep areas drop out |
| 210.8(A)(8) | Replaced: sinks "located in areas other than kitchens" within 6 ft of the sink edge | The sink rule is confined to non-kitchen sinks |
| 210.8(A)(11) | **Deleted** (laundry areas) | Laundry receptacles need no GFCI |
| 210.8(D) | In dwelling units, list items (7) dishwashers, (8) ranges, (9) wall ovens, (10) cooktops, (11) clothes dryers, (12) microwaves **deleted** | Appliance-specific GFCI not required |
| 210.8(F) | List items (1) garages at/below grade and (2) accessory buildings **deleted** | Outdoor outlets for garages/outbuildings not under 210.8(F) |
| **210.12(B)** | "Shall apply in full. Exception: In one- and two-family dwelling units, Arc-Fault Circuit-Interrupter Protection shall only apply to all branch circuits and outlets supplying **bedrooms**. All other locations in such units are exempt" | **AFCI = bedrooms only** |
| 210.52(C) | New item (4): island/peninsula receptacles "if installed" may be mounted ≤ 12 in below the countertop, not where the overhang exceeds 6 in | Island receptacles optional, below-counter allowed |
| 210.52(E)(3) | Balconies/decks/porches **≥ 20 sq ft** accessible from inside need one receptacle, ≤ 6½ ft above the surface | |
| 215.18, 225.42, 230.67 | Surge protection: for dwelling units a SPD "shall be **permitted**" — list item (1) deleted | **SPD not required** |
| 225.41, 230.85 | Emergency disconnect "shall be **permitted**" for one- and two-family dwellings; 230.85(C) deleted | **Outdoor emergency disconnect not required** |
| 314.27(C) | Second paragraph deleted | No ceiling-fan-rated box required at every habitable-room ceiling outlet |
| 334.10(3) | Replaced (NM cable concealment/thermal barrier; attics and underfloor "considered concealed") | |
| 334.15(C) | NM may be secured to the bottom edge of joists in crawl spaces ≤ 4.5 ft high | |
| 422.5(A)(7) | Dishwashers deleted from the GFCI appliance list | |
| 690.12 | Rapid-shutdown exemptions for detached PV-only structures and for off-grid buildings ≥ 1,000 ft from utility lines with 100-ft setbacks and a placard | Off-grid cabins |
| 706.5 / 706.15(B) | ESS listing not required for lead-acid batteries; off-grid disconnect at a readily accessible location | |

Also in 24.39.10.500.01.a.i: "No wiring or equipment may be concealed in any
manner from access or sight until the work has been inspected and approved
for cover by the electrical inspector."

**DO print "2023 NEC as amended by IDAPA 24.39.10" as the Idaho citation, and
print the AFCI/GFCI table.** A reader on a national code book will install
AFCI on every 120-V branch circuit, whole-house SPDs and an outdoor
emergency disconnect that Idaho does not require, and a reader on a stale
2017/2020 book will miss the Idaho-specific island rule. Either way the kit
must carry the table.

**Grid-tied renewables**: § 54-1016(2)(a): the homeowner licensing exemption
applies "except that homeowner installations of renewable power generation
connected to the community power grid shall be subject to a preplan review in
accordance with local jurisdictions' policies and procedures prior to the
purchase of a permit."

### 3.6 Energy — pinned by statute, preempting every county `[V]`

**§ 39-9701(1):** "On and after July 1, 2022, the Idaho state energy code
shall be the 2018 international energy conservation code, as amended,
revised, or modified by the Idaho building code board and approved by the
legislature."

**§ 39-9701(2) — the preemption:** "The provisions of this chapter preempt,
eliminate, and prohibit any cities, counties, incorporated or unincorporated
areas, special use districts, or any other local governmental entities of any
kind from adopting energy code or energy-related requirements through any
code, ordinance, process, policy, or guidance that differ from or are more
extensive than the requirements of the Idaho energy conservation code …"
(3): applies to local codes "adopted … prior to, on, or after July 1, 2022."

**Idaho's Table R402.1.2 (residential, IDAPA 24.39.30.600.06.b)** —
climate-zone rows 5 and 6 deleted and replaced:

| Component | Zone 5 | Zone 6 |
|---|---|---|
| Fenestration U-factor | 0.32 | 0.30 |
| Skylight U-factor | 0.55 | 0.55 |
| Glazed SHGC | NR | NR |
| **Ceiling** | **R-38** | **R-49** |
| Wood-frame wall | R-20, or 13+5 | R-22, or 13+5 |
| Mass wall | 13/17 | 15/20 |
| Floor | R-30 | R-30 |
| Basement wall | 15/19 | 15/19 |
| Slab R-value & depth | R-10, 2 ft | R-10, 4 ft |
| Crawl-space wall | 15/19 | 15/19 |

Equivalent U-factors (Table R402.1.4 as replaced, 600.06.d): Zone 5 ceiling
0.030, frame wall 0.060, floor 0.033; Zone 6 ceiling 0.026, frame wall 0.057.

**Air leakage — R402.4.1.2 exception (600.06.e):** "**Visual Inspection.**
The Permit Holder will determine at the time of permit application the
method of determining building envelope tightness. A visual inspection shall
be considered acceptable in lieu of testing when the items listed in Table
R402.4.1.1, applicable to the method of construction, are field verified."
**Idaho does not require a blower-door test; the choice is the permit
holder's and is made on the application.** The unamended ≤ 3 ACH50 figure
applies only if testing is chosen.

**Log homes** (600.06.f–g): new R402.6 with its own Table R402.6 — Zone 5:
8-in minimum average log, ceiling R-49, floor R-30, basement 10/13, slab
R-10 2 ft; Zone 6: 8-in log, R-49, R-30, 15/19, R-10 4 ft; or a 5-in log
with the high-efficiency-equipment path (90 % AFUE gas/propane, 84 % oil, or
15 SEER heat pump; zonal electric resistance as sole heat counts as
compliant). Compliance alternatives: R405 simulated performance or REScheck.

Conditioned-space definition excludes garages heated "for frost protection
or intermittent use" (600.06.a). Climate zones: the 2018 IECC Table
R301.1 assigns every Idaho county to Zone 5B or 6B; the county list is in the
model code, not in an Idaho amendment, so the kit prints "Zone 5 or 6 per
IECC Table R301.1 for your county" and does not reproduce the list.

### 3.7 Mechanical amendments `[V]` — IDAPA 24.39.70.600.03

New M1203.1: CO alarm required outside each sleeping area "where work
requiring a permit occurs in existing dwellings … where a fuel fired
appliance is installed"; M1401.3 and M1601.1 limited to "new, one- and
two-family dwellings"; dryer-duct support at 4-ft intervals with no
protruding fasteners; gas test ≥ 20 psig for 20 minutes (≥ 60 psig for
systems over 10 in w.c.); plastic flue-gas vent pipe tested at 5 psi for
15 minutes.

---

## 4. PERMITS, CLOCKS AND INSPECTIONS

### 4.1 Building permit (only in an enforcing jurisdiction) `[V]`

| Item | Rule | Cite |
|---|---|---|
| Whether one exists | Only "in a local government jurisdiction enforcing building codes" | § 39-4111(2) |
| Process document | Every local government that requires building permits "shall make available a document that describes in detail the requirements of its building permit process … on its website and in physical form upon request" | § 39-4117(1) (2025 ch. 272 = S1164) |
| **Completeness clock** | Incomplete residential application: written notice of what is missing within **10 business days** (20 commercial); after each submission the local government has 10 business days to determine completeness and must give written notice; completeness "shall not constitute approval" | § 39-4117(2)–(3) |
| Extension | Only by written agreement after the local government explains why | § 39-4117(4) |
| **Plan-review clock** | **None for a private house.** The 30-calendar-day initial-review clock applies to "public works" and public schools only | § 39-4113(2), (6) (verified limit) |
| Governing law | "Permits shall be governed by the laws in effect at the time the permit application is received" | § 39-4116(6) |
| Existing-building upgrades | No upgrade of unaffected compliant parts absent a proven "specific substantial safety hazard" | § 39-4111(3) |
| Registration on the face | Registration number, or "no contractor registration provided"; permit posted on site | § 54-5209 |
| Inspector credential | ICC certification; a residential-certified inspector "may only inspect structures regulated by the IRC" | § 39-4108 |
| **Inspection clock** | Not performed within **48 business hours** → permit holder may hire a § 39-4108-qualified third-party inspector, notify the jurisdiction, deliver the results, and be **refunded the inspection fee** | § 39-4118(1) (2025 ch. 221 = H0266) |
| Failure reason | Failed inspection with no reason given within **3 business days** → **10 % refund** of the inspection fee | § 39-4118(2) |
| Virtual re-inspections | Permitted at the jurisdiction's discretion after an in-person inspection; address verified on camera; not for structural on 3+ stories | § 39-4119 |
| Fees | Local: set by ordinance (no state cap in the Act for local programs). DOPL's own Table 1-A applies only to DOPL-issued permits: $695.63 for the first $100,000 of valuation + $3.92 per additional $1,000; plan review $100/hr, 40 %–65 % of the permit fee | § 39-4112; IDAPA 24.39.30.500.03 (7-1-26) |
| Permit life | **Not set by the Act.** IRC R105.5 (180 days) as adopted, and locally amendable (Part I) | — (verified absence) |
| Certificate of occupancy | IRC R110 as adopted, locally amendable (Part I); none exists where there is no program | — |

### 4.2 Electrical permit `[V]`

| Item | Rule | Cite |
|---|---|---|
| Who issues | DOPL, except in a city/county with its own § 54-1001B program | § 54-1001B; § 54-1005(1) |
| When | "All electrical permits shall be purchased before work is commenced. Payment of the total permit fee shall be made prior to a final inspection." | IDAPA 24.39.10.500.01.a |
| Homeowner eligibility | Licensing exemption for "any property owner performing noncommercial electrical work in the owner's primary or secondary residence or associated outbuildings or land associated with the entire property on which those buildings sit" | § 54-1016(2)(a) |
| **What the homeowner signs** | DOPL Homeowner Permit form (rev. 9/13/2022): "I certify that I am the owner of the residential property and **will personally perform the work** covered by this permit. I recognize this permit is only valid for work on a primary or secondary residence and associated outbuildings **not used for commercial purposes or rented by a tenant**." The identical certification appears on the plumbing and HVAC homeowner forms. It is an agency form condition, not a statute or rule — see § 5.2 note | DOPL ELE/PLB/HVAC Homeowner Permit Applications |
| **Temporary power** | Only "at the request of a licensed electrical contractor" may a utility energize before a passed inspection; a homeowner permit cannot get construction temp power ahead of inspection | IDAPA 24.39.10.200.04 |
| Online purchase | "Purchase your permit on-line HERE **based on location**" links to DOPL's ArcGIS jurisdiction map; the eTRAKiT portal at web.dbs.idaho.gov handles inspection requests (next-day requests until 7 p.m. MT) | DOPL ele-permits page; ele FAQ |
| "Associated buildings" | "All buildings, structures, and fixtures used for domestic purposes and in connection with the primary or secondary residence, such as garages, sheds, barns, or shops." | IDAPA 24.39.10.002.01 |
| Fee, new one-family dwelling | ≤ 1,500 sq ft living space **$130**; 1,501–2,500 **$195**; 2,501–3,500 **$260**; 3,501–4,500 **$325**; over 4,500 $325 + $65 per 1,000 sq ft. "Includes associated buildings with wiring being constructed on each property." | IDAPA 24.39.10.500.02.a.i |
| Existing dwelling | $65 per inspection | 500.02.a.ii |
| Reinspection | $65 (not ready, bad directions, uncorrected notice) | 500.04 |
| Plan check | $65 first hour, $65/hr after | 500.06 |
| Life | Expires **365 days** from purchase; renewal one year, $65 | 500.01.c |
| Transfer | To the owner if the contractor relationship ends; notarized consent; $45 | 500.01.d |
| Cover | Nothing concealed until inspected and approved for cover | 500.01.a.i |
| Energize | Utility may not energize before a passed inspection; contractor-only temporary power exception | § 54-1005(3); IDAPA 24.39.10.200.04 |
| Correction notice | Inspector "shall clearly indicate any and all violations to be corrected and specify a definite period of time" | § 54-1004 |
| Disconnect power | Administrator may de-energize or order disconnection "when such installation is found to be dangerous to life or property" | § 54-1004 |
| **48-hour rule** | Same third-party/refund remedy as building | § 54-1004A (2026 ch. 232 = H0585) |
| Combined permits | A DOPL plumbing or HVAC permit that "includes any part of an electrical installation" satisfies the electrical permit if fees are paid | § 54-1016(4); § 54-5016(2) |

### 4.3 Plumbing permit `[V]`

| Item | Rule | Cite |
|---|---|---|
| Who issues | DOPL except in a local program | § 54-2620(1) |
| Homeowner eligibility | Certificate not required for "any person who does plumbing work in a single or duplex family dwelling, including accessory buildings, quarters and grounds … provided that such person **owns or is a contract purchaser** of the premises"; permits "shall be issued … to a person excepted … pursuant to section 54-2602(1)(a)" | § 54-2602(1)(a); § 54-2620(2) |
| Homeowner must apply | "Homeowners making plumbing installations on their own premises under … 54-2602(1)(a) … must secure a plumbing permit by making application to the Division" | IDAPA 24.39.20.500.01.b |
| No permit needed | Clearing stoppages and repairing leaks with no rearrangement | § 54-2621 |
| Application | Description, location, ownership, occupancy and use; board "may require plans and specifications" | § 54-2622 |
| Fee, new 1–2 family | Same square-foot ladder as electrical: **$130 / $195 / $260 / $325** + $65 per extra 1,000 sq ft; "Includes all buildings with plumbing systems being constructed on each property" | IDAPA 24.39.20.500.02.a |
| Residential sewer/water service line | $65 per inspection | 500.02.b |
| Residential fire sprinkler | $65 or $4 per head | 500.02.b |
| Additional trips | $65/hr | 500.02.d |
| Life | 365 days from purchase **or last inspection**; renewal $65 | 500.01.c |
| **Required inspections** | **Groundwork** (tag on a vertical riser before cover) → **rough-in** (before concealment) → **final** (tag "at the approximate service entrance") | IDAPA 24.39.20.500.03; § 54-2625 |
| Notice to sewer cities | DOPL notifies cities that serve sewer outside their limits within 10 days of permits for sewer installations | § 54-2607(2) |
| **48-hour rule** | Third-party/refund remedy | § 54-2626A (2026 ch. 232) |

### 4.4 HVAC permit `[V]`

| Item | Rule | Cite |
|---|---|---|
| Who issues | "the authority having jurisdiction" — DOPL unless a local mechanical program | § 54-5016(1) |
| Homeowner eligibility | Certificate not required for "any person who installs or maintains [an HVAC] system in a single or duplex family dwelling, including accessory buildings … provided that such person owns or is a contract purchaser of the premises" | § 54-5002(1)(a) |
| Homeowner must apply | IDAPA 24.39.70.500.01.b | |
| No permit needed | "repair or maintenance of an existing HVAC system" | § 54-5016(1) |
| Fee, residential | Base **$100** + $30 first appliance (furnace, heat pump, A/C, boiler, mini-split, wood stove, gas fireplace …) + $15 each additional; exhaust/ventilation ducts $15 first + $5 each; gas piping $5 per appliance outlet; hydronic $5 per zone | IDAPA 24.39.70.500.02.a |
| **Manual J/S/D** | DOPL Homeowner HVAC fee worksheet: "Manual S, J, & D — **Review required** when installing the primary heating and/or cooling system in a NEW single or two-family dwelling — $25." On the form, not in the rule's fee table; the kit tells the reader to bring load/equipment/duct calculations to the permit | DOPL HVAC Homeowner Permit form |
| Life | 365 days from purchase or last inspection; renewal $65 (rule) — the statute's 90-day/180-day text at § 54-5017(3) is superseded "until fees are established by rule" | IDAPA 24.39.70.500.01.c; § 54-5017(2) |
| Inspection request | Permit holder "shall notify the division … at least one (1) day prior to the desired inspection, Sundays and holidays excluded" | § 54-5020(1) |
| Tags | Work-in-progress tag (groundwork, rough-in, anything to be concealed); final tag on the equipment | IDAPA 24.39.70.500.03; § 54-5019 |
| Reinspection after final | Fee "not to exceed the actual cost" | § 54-5020(1) |
| No permit penalty | Double fee; triple within 12 months | § 54-5017(4) |
| **48-hour rule** | Third-party/refund remedy | § 54-5020A (2026 ch. 232) |
| Refrigerant | Federal EPA § 608 — not an Idaho rule; the kit says "federal," cites nothing Idaho | `[H]` |

### 4.5 The inspection ladder — what is actually in a rule `[V]`

No Idaho statute enumerates the residential building-inspection sequence;
in an enforcing jurisdiction IRC R109 as adopted governs (foundation,
plumbing/mechanical/electrical rough, floodplain, frame and masonry, final;
locally amendable). The **trade** rungs are in rule: plumbing groundwork →
rough → final (IDAPA 24.39.20.500.03); HVAC work-in-progress → final
(24.39.70.500.03); electrical cover inspection → final
(24.39.10.500.01.a.i; § 54-1005(3)). Septic: test-hole/site inspection on
48 hours' notice, then final with as-built before any wastewater enters the
system (IDAPA 58.01.03.011.03, .05). Well: driller's report to IDWR within
30 days (§ 42-238(11)).

**The 48-hour rule, all four statutes, same text**: "If an inspection
requested by a permit holder is not performed within forty-eight (48)
business hours, such permit holder shall be authorized to hire a third-party
inspector to perform such inspection. The permit holder or third-party
inspector shall notify the division or local government … The permit holder
shall provide a copy of the results … [and] shall be refunded any fee, or
portion thereof, that the permit holder paid … for such inspection." The
third-party inspector must hold the same qualification as a state inspector
(§ 39-4108 ICC certification; § 54-1019 journeyman/master with 4 years;
§ 54-2627 certificate with 5 years; § 54-5021 board-certified). `[V]`

---

## 5. LICENSING AND CONTRACTS

### 5.1 Registration, not licensing `[V]`

§ 54-5202: the Act "provides for the registration of construction
contractors." § 54-5204(1): unlawful "to engage in the business of, or hold
himself out as, a contractor within this state without being registered."
§ 54-5203(3): "'Contractor' means: (a) Any person who in any capacity
undertakes, offers to undertake, purports to have the capacity to undertake,
or submits a bid to, or does himself or by or through others, perform
construction; or (b) A construction manager." No examination, no experience
test. Application requirements (§ 54-5210): SSN/EIN; owners; **workers'
compensation certificate or a statement why not required**; **general
liability with products/completed operations ≥ $300,000 single limit**;
type of construction; disciplinary history. Fee ≤ $150/year (§ 54-5210(2)).
Registration runs 2–5 years (§ 54-5211(1)).

### 5.2 The owner exemptions, verbatim `[V]` — § 54-5205(2)

Preamble: registration "shall not be required for the following, so long as
such person is not acting with the intent to evade this chapter and so long
as such person does not hold himself out as a registered contractor:"

> "(k) An owner who contracts for work to be performed by a registered
> contractor on his own property, provided however, this exemption shall not
> apply to an owner who, with the intent to evade this chapter, constructs a
> building, residence or other improvement on the owner's property with the
> intention and for the purpose of selling the improved property at any time
> during the construction or within twelve (12) months of completion of such
> construction;
> (l) An owner performing construction on the owner's personal residential
> real property, whether or not occupied by the owner, provided however, this
> exemption shall not apply to an owner **who is otherwise regulated by this
> chapter** who constructs a building, residence or other improvement on the
> owner's property with the intention and for the purpose of promptly
> selling the improved property, unless the owner has continuously occupied
> the property as the owner's primary residence for not less than twelve (12)
> months prior to the sale of such property;"

**Where "primary or secondary residence" and "not rented" actually live.**
The contractor exemption (l) says "personal residential real property,
whether or not occupied by the owner." The electrical licensing exemption
says "primary or secondary residence" (§ 54-1016(2)(a)). The plumbing and
HVAC certificate exemptions say "a single or duplex family dwelling … owns
or is a contract purchaser" (§ 54-2602(1)(a); § 54-5002(1)(a)) — no
residence test at all. The rules add nothing (24.39.20.500.01.b and
24.39.70.500.01.b simply say such homeowners "must secure a … permit"). The
"primary or secondary residence … not used for commercial purposes or
rented by a tenant" and "will personally perform the work" conditions are
the **DOPL homeowner permit form's certification** and the DOPL FAQ. The kit
prints all three layers and labels each — the Montana lesson, applied.
"Sale" and "lease" appear nowhere. `[V]`

Read precisely: (l) has **no occupancy requirement** ("whether or not
occupied by the owner"); its anti-flip proviso attaches only to an owner "who
is otherwise regulated by this chapter" (i.e. someone in the contracting
business) building "for the purpose of promptly selling"; (k) — hiring a
registered contractor — carries the intent-to-evade, sell-within-12-months
proviso. The published guide's "12-month rule is the trap for flippers"
callout collapses these into a single rule and drops the "otherwise
regulated" qualifier. Also useful: (f) casual/minor work under **$2,000**
aggregate, not part of a larger project; (p) "A person working on the
person's own residence, if the residence is owned by a person other than the
resident."

### 5.3 Why you hire registered subs — three statutory teeth `[V]`

- § 54-5204(2): "It shall be unlawful for a contractor to engage any other
  contractor who is required … to be registered … unless such other
  contractor furnishes satisfactory proof … that he is duly registered." (An
  exempt owner is not a "contractor," so this duty does not bind the owner —
  but the next two do the work.)
- § 54-5208: an unregistered contractor "shall be denied and shall be deemed
  to have conclusively waived any right to place a lien upon real property"
  — except subs, employees and suppliers who did not know.
- § 54-5217(2): an unregistered contractor "may [not] bring or maintain any
  action in any court of this state for the collection of compensation."
- § 54-5210(1)(e): every registrant carries **$300,000** GL including
  completed operations — "the name of the insurance company, the insured and
  policy number shall be made available only to persons or their insurers
  stating that they possess a claim against the contractor."

Trade contractors: electrical contractors must carry **$300,000** liability
(§ 54-1003A(1)); plumbing and HVAC contractors post a **$2,000** compliance
bond (§ 54-2606(3)(d); § 54-5007). Only journeyman/master/residential
electricians may do a contractor's work; apprentice ratio 1:6 residential
(§ 54-1010(3)). A "residential electrician" (4,000 hours + 2-year course)
may work only in "one (1) and two (2) family dwellings, townhouses, and
multi-family structures up to three (3) stories" (§ 54-1003A(3), (12)).

### 5.4 Mechanics' liens and the § 45-525 disclosure `[V]`

§ 45-501: every person performing labor or furnishing materials has a lien,
and "every contractor, subcontractor, architect, builder or any person having
charge of … the construction … shall be held to be the agent of the owner for
the purpose of this chapter." § 45-507: claim of lien filed with the county
recorder **within 90 days** after completion of labor/materials; a copy served
on the owner **within 5 business days** of filing (personal service or
certified mail); prevailing party recovers attorney's fees.

**§ 45-525 — the disclosure an owner-builder should demand from every
"general contractor" it hires for over $2,000**: before contracting, the
general contractor must give a signed disclosure that the homeowner may (a)
require lien waivers from subs at the owner's reasonable expense; (b)
receive proof of GL with completed operations and of workers' compensation;
(c) buy extended title insurance covering unfiled liens; (d) require a
surety bond up to the project value. Before final payment, a signed list of
every sub, supplier and equipment renter over $500 with a direct contract.
Failure is a Consumer Protection Act violation (§ 45-525(4)). An
owner-builder hiring trades directly is the "homeowner"; each trade
contractor with a direct contract over $2,000 is a "general contractor" for
this section (§ 45-525(5)(a)(i)). The kit prints the four rights as contract
terms.

### 5.5 Workers' compensation `[V]` — § 72-212

Exempt from coverage "unless coverage thereof is elected": "(2) Casual
employment," "(4) Employment of members of an employer's family dwelling in
his household if the employer is the owner of a sole proprietorship," and
"(6) Employment as the owner of a sole proprietorship." An owner-builder
paying day labor is not automatically inside (2). **"Casual employment" is
not defined in § 72-102** (verified: the definitions section has no entry);
the kit does not define it either and tells the reader to confirm with the
Industrial Commission before paying anyone by the hour. § 72-102(12)(a):
"Employer" "includes the owner or lessee of premises … who, by reason of
there being an independent contractor or for any other reason, is not the
direct employer of the workers there employed" — the statutory-employer
hook; print it as the reason to demand every trade's workers' compensation
certificate (which registered contractors must file, § 54-5210(1)(d)).

### 5.6 Property Condition Disclosure Act `[V]` — Title 55, ch. 25

§ 55-2504: any transfer of 1–4 unit residential property requires the
§ 55-2508 form. **§ 55-2505(12): exempt is "a transfer that involved newly
constructed residential real property that previously has not been
inhabited,** except that disclosure of annexation and city service status
shall be declared." So an owner-builder who sells before moving in files
only the three annexation questions; one who lives in the house and later
sells completes the whole form, including question 8: "Have any substantial
additions or alterations been made without a building permit?" and question
5's well and septic lines. The guide's sentence ("Owner-built homes don't
have to be labeled as such, but known defects, unpermitted work, and code
issues must be disclosed") is wrong for a never-inhabited new house.

---

## 6. SITE PLAN STUDIO EXTRACTION

Feeds `src/lib/siteplan/rules.ts`. All values `[V]`, quoted from
IDAPA 58.01.03 (DEQ septic rules, paragraphs effective 7-1-25) and
IDAPA 37.03.09 (IDWR well rules, 3-18-22 / 7-1-25). Units are feet. Idaho
has three separation tables — drainfield (58.01.03.008.01.d), septic tank
(58.01.03.007.18) and well (37.03.09.025.01.d) — and they agree at the
well/septic boundary from both sides.

> Framing note: 58.01.03.001.02 — where these rules conflict with any local
> zoning, building or health ordinance, "the provision that, in the
> Director's judgment, establishes the higher standard … prevails." The
> well rule adds: "Additional siting and separation distance requirements
> are set forth by the governing district health department" (37.03.09.025.
> 01.d preamble). The tool must present these as statewide minimums the
> health district may increase.

### 6.1 Drainfield separations — 58.01.03.008.01.d

| Feature of interest | Soil A | Soil B | Soil C |
|---|---|---|---|
| Public water supply | 100 | 100 | 100 |
| **All wells and other domestic water supplies** | **100** | 100 | 100 |
| Water distribution lines, not double-encased | 25 | 25 | 25 |
| Water distribution lines, double-encased | 10 | 10 | 10 |
| Permanent or intermittent surface water (other than canals/ditches) | **200** | **125** | **100** |
| Temporary surface water; irrigation canals and ditches | 50 | 50 | 50 |
| Downslope cut or scarp, impermeable layer above base | 75 | 50 | 50 |
| Downslope cut or scarp, impermeable layer below base | 50 | 25 | 25 |
| Building foundation — crawl space or slab | 10 | 10 | 10 |
| Building foundation — **basement** | **20** | 20 | 20 |
| Property line | 5 | 5 | 5 |

Soil groups (008.01.b): A = coarse to fine sand, loamy sand; B = very fine
sand, sandy loam, loam, silt loam, silt; C = clay loam, sandy clay loam,
silty clay loam. **Unsuitable**: gravel (> 10 mesh) at the coarse end;
sandy clay, silty clay, clay, high shrink/swell clays, organic mucks,
claypan/duripan/hardpan at the fine end.

### 6.2 Septic-tank separations — 58.01.03.007.18

| Feature of concern | Distance |
|---|---|
| Well, spring or suction line — public water | 100 |
| **Well, spring or suction line — other** | **50** |
| Water distribution line — public | 25 |
| Water distribution line — other | 10 |
| Permanent or intermittent surface water | 50 |
| Temporary surface water | 25 |
| Downslope cut or scarp | 10 |
| Dwelling foundation or building | 5 |
| Property line | 5 |
| Seasonal high water level, vertically from top of tank | 2 |

### 6.3 Well separations — 37.03.09.025.01.d (well owner must maintain: .036.04)

| Separation of well from | Distance |
|---|---|
| Existing public water supply well, separate ownership | 50 |
| Other existing well, separate ownership | 25 |
| **Septic drainfield** | **100** |
| **Septic tank** | **50** |
| Drainfield of a system > 2,500 gpd | 300 (less with site data) |
| Sewer main, pressurized, multiple sources | 100 |
| Sewer main, gravity, multiple sources | 50 |
| Secondary sewer line, pressure-tested, single residence | 25 |
| Effluent pipe | 50 |
| **Property line** | **5** |
| Permanent buildings other than well/plumbing houses | 10 |
| Above-ground chemical storage tanks | 20 |
| Permanent (> 6 months) or intermittent (> 2 months) surface water | 50 |
| Canals, ditches, laterals, temporary (< 2 months) surface water | 25 |

37.03.09.036.03: after the well exists, "The well owner must not construct
or allow construction of any permanent building, except for buildings to
house a well or plumbing apparatus, or both, closer than ten (10) feet from
an existing well." Casing must stand ≥ 12 in above finished grade
(.025.04; .036.02.b).

### 6.4 Site suitability — hard disqualifiers `[V]`

- **Slope**: a standard drainfield site "will not exceed twenty percent
  (20%)" (58.01.03.008.01.a); absorption beds not on slopes over 8 %
  (008.09.b).
- **Effective soil depth below the drainfield bottom** (008.01.c): to an
  impermeable layer 4 ft (all groups); to fractured bedrock/extremely
  permeable material 6/4/3 ft (A/B/C); to normal high groundwater 6/4/3 ft;
  to seasonal high groundwater 1 ft.
- **Replacement area**: "An acceptable site must be large enough to
  construct two (2) complete drainfields in which each are sized to receive
  one hundred percent (100%) of the design wastewater flow" (008.02.c); the
  replacement area "must be kept vacant, free of vehicular traffic, and free
  of any soil modification" (004.06). No driving or parking on the
  drainfield or replacement area (008.08.c, 008.10).
- **Public sewer**: the permit may be denied where "public or central
  wastewater treatment facilities are reasonably accessible" (005.05.c).

### 6.5 Sizing numbers `[V]`

- **Design flow** (58.01.03.007.09): single-family dwelling, 3 bedroom =
  **250 gpd**; "Add/subtract 50 gallons per day/bedroom."
- **Septic tank** (007.08.a): "Tanks serving single dwelling units. The
  minimum tank capacity is **one thousand (1,000) gallons**. For each
  bedroom over four (4) in a dwelling unit, add two hundred fifty (250)
  gallons."
- **Absorption area** (008.02.b): required area = design flow ÷ application
  rate; rates **1.0 / 0.5 / 0.2** gal per sq ft per day for soil groups
  A / B / C. (A 3-bedroom house on Group B soil: 250 ÷ 0.5 = 500 sq ft of
  trench bottom, twice, for the replacement area.)
- **Trench geometry** (008.03): laterals ≤ 100 ft; trench width 1–6 ft;
  depth 2–4 ft; total trench ≤ 1,500 sq ft; ≥ 6 ft undisturbed earth between
  trenches and between tank and trenches; aggregate ≥ 12 in total (≥ 2 in
  over, ≥ 6 in under the lateral); ≥ 12 in soil cover.

### 6.6 Do NOT encode

- **Building setbacks from lot lines.** These are zoning under the Local
  Land Use Planning Act, set by each of Idaho's 44 counties and ~200 cities;
  the state health rules give only 5 ft (tank, drainfield, well to the
  property line), which is a sanitation number, not a zoning setback.
- **Frost depth and ground snow load.** IRC R301.2 design criteria are
  expressly the county's to amend (§ 39-4116(4)(c)(iii)); no statewide value
  exists. The only statewide depth number is the **42-in** water-service
  burial depth in the plumbing code (IDAPA 24.39.20.600.21) — encode that
  one as a utility-trench note, not as frost depth.
- **Health-district additions.** Each of the seven districts may set larger
  separations; the tool must say "minimum, confirm with your district."
- **Well-to-septic beyond the table** — the 300-ft large-system row applies
  only to systems over 2,500 gpd.

---

## 7. DELIBERATELY NOT PRINTED

| Item | Why |
|---|---|
| Local building-permit fee figures, plan-review percentages, valuation-per-sq-ft factors (Boise, Nampa, Coeur d'Alene, Idaho Falls, Pocatello) | Every enforcing city and county sets its own by ordinance; none was verified in a primary source. The only citable table is DOPL's Table 1-A, and it applies only to DOPL-issued (state-building) permits. |
| DOPL Table 1-A as "the default" for houses | There is no default. DOPL does not issue residential building permits (DOPL Plan Review Application). |
| A list of which counties have no building department | No state agency publishes one; § 39-4116(1) lets any county adopt or contract for a program at any time. The kit prints the verification step: the § 39-4117(1) process document on the county website, or a written statement that no building ordinance has been adopted. |
| Which cities run their own electrical/plumbing/HVAC programs | Verified only that Boise (its own electrical, plumbing and mechanical fee schedules) and Coeur d'Alene (its own plumbing amendments) do. DOPL's inspector list is organized by city/ZIP and lists a state inspector for Boise ZIPs too, so it is not a jurisdiction roster. The kit points at DOPL's location-based permit map and says "ask the city building department first." |
| Processing-time estimates ("4–8 weeks") | No primary source; the only clocks in statute are § 39-4117's completeness clocks and the 48-business-hour inspection rule. |
| Ground snow load psf by county, frost depths by region, seismic design categories by city | All are IRC R301.2 design criteria that § 39-4116(4)(c)(iii) hands to the local jurisdiction; no statewide table exists in the Act or in IDAPA 24.39.30. The University of Idaho snow-load study is not referenced by any Idaho statute or rule. |
| "Case-study" snow-load counties (Ada, Kootenai, Bonneville, Blaine, Valley, Bonner) | Unverified county practice. |
| A 2018-IRC Idaho effective date ("January 1, 2021") | The Board's adoption date was not retrieved; § 39-4109(4) gives the mechanism (1 January after Board adoption) and § 39-9701 the energy pin (1 July 2022). Print the mechanism, not a remembered date. |
| A projected next-edition date | The 2024 update was rejected 17 February 2026; the Board is "not currently engaged in rulemaking for 2026–2027." |
| Septic and well cost ranges; snow-load engineering fees | Market figures, not rules. State minimum septic permit fee ($400 basic/complex; $300 tank-only; $40 renewal — IDAPA 58.01.14.110.04) and the $75 domestic drilling permit (§ 42-235) are printed instead. |
| Boise WUI "30-foot defensible space" figure | The city page verifies IR1 Class 1 ignition-resistant construction and a defensible-space section; the 30-ft distance was not found in the page text retrieved. |
| An IFC edition | § 41-253(1) delegates the edition to the state fire marshal; not verified here. The 5-acre exemption in § 41-253(2) is printed. |
| A definition of "casual employment" | Not in § 72-102. |
| Phone numbers | House rule. DOPL's inspector list and program pages carry them; the kit points at the list. |
| Named inspectors | The DOPL list names one per city per trade; they rotate. The kit prints the list URL and its revision date. |
| "Not for sale, rent, or lease" as a homeowner-permit rule | "Sale" and "lease" appear in no statute, rule or DOPL form. The form says "not used for commercial purposes or rented by a tenant." |

---

## 8. OPEN QUESTIONS

1. **IRC Part IX (Appendices).** § 39-4109(1)(a)(iii) and IDAPA 24.39.30.600.03
   adopt "Parts I, II, III, and IX" of the 2018 IRC. Part IX *is* the
   appendices (A–T, including F radon control and Q tiny houses), and
   § 39-4116(4)(c)(iv) lets a local jurisdiction amend Part IX by ordinance.
   IRC R102.5 says appendices apply only where specifically adopted. Whether
   adopting "Part IX" wholesale makes Appendix F or Q enforceable in an
   Idaho jurisdiction that has not spoken to them is not resolved by any
   source read here. Kit: ID.1 tells the reader to ask the building official
   in writing which IRC appendices the local ordinance adopted, and does not
   assert a radon or tiny-house rule either way.
2. **Board adoption date of the 2018 IRC.** Not retrieved (ICC's online
   preface page is script-rendered). Immaterial to a 2026 build; matters
   only for the guide's "effective January 1, 2021" sentence, which should be
   dropped rather than corrected.
3. **Which cities and counties run their own trade programs.** § 54-1001B(4)
   and § 54-2601(7) require 30 days' written notice to DOPL, so DOPL holds
   the list, but it publishes only the inspector-by-city schedule and the
   location-based permit map. Verified: Boise (all three trades) and Coeur
   d'Alene (plumbing). Canyon County's HVAC program transferred *to* DOPL on
   1 September 2023 (DOPL HVAC board news) — programs move in both
   directions.
4. **Whether local building programs enforce IRC R105.5 (180-day permit
   expiry) and R110 (certificate of occupancy) unamended.** Part I is
   locally amendable; the kit prints the model-code rule with "confirm."
5. **Health-district additions to the state separation tables.** IDAPA
   37.03.09.025.01.d says districts set "additional" siting requirements;
   none were read. ID.4 asks each district for its septic-permit checklist.
6. **DOPL eTRAKiT portal** (`web.dbs.idaho.gov/etrakit3/`) returned no
   response to automated fetch (likely bot-blocked); it is linked from every
   DOPL permit page. The kit prints the DOPL page, not the portal URL.
7. **Whether any Idaho utility requires a septic or address approval before
   energizing** — not researched; the statutory lock is the electrical
   inspection only (§ 54-1005(3)).

---

## 9. KIT REVISION WATCH — IDAHO TRIPWIRES

Add to `project-kit-revision-watch`:

1. **Next building-code docket.** The 2024 I-Code update (Docket
   24-3930-2502) was rejected by the House Business Committee on 17 February
   2026 with members calling for "an Idaho Building Code." DOPL says no
   rulemaking for 2026–2027. Watch `dopl.idaho.gov/bld/bld-statutes-and-rules/`
   ("Rule Changes Under Consideration") and the Administrative Bulletin for
   any 24-3930 docket; a new edition takes effect 1 January after Board
   adoption (§ 39-4109(4)) and only after surviving legislative review. If a
   bill creating a standalone "Idaho Building Code" appears, ID.2/ID.3
   rebuild.
2. **NEC amendments — Electrical Board public hearing 15 October 2026**
   (DOPL calendar). IDAPA 24.39.10.600 was last rewritten effective 4-4-25.
   Any change to the AFCI-bedrooms-only exception or the GFCI deletions
   changes the § 3.5 table.
3. **Energy code by statute.** § 39-9701 pins the 2018 IECC; only a bill
   moves it. Watch Title 39 ch. 97 each session.
4. **The inspector list rotates.** `BCRE-Inspector-list-with-schedule08052026.pdf`
   is dated 5 August 2026 and the filename changes with each revision; DOPL
   links it as "Inspector List with Schedule" from every trade page. Print
   the page, not the PDF path.
5. **Fee dockets.** Docket 24-3930-2501 (fees) produced the 7-1-26 Table 1-A;
   the Contractors Board moved to biennial registration 14 October 2025 with
   fees "effective July 1st, 2026" ($120 initial / $60 annual / $120
   biennial); the Factory Built Structures Board goes biennial 1 April 2026.
   Fee rows in ID.5 carry a date.
6. **2026 session bills that did NOT pass** and may return: H0768
   "Contractor registration, registration, discipline"; S1415 "State-certified
   private inspectors"; H0643 "Heat detection devices, building codes, local
   govt." Any of these would touch § 5.1, § 4.5 or § 3.3.
7. **Drought declaration** expires 31 December 2026 unless extended (IDWR
   drought page). It affects temporary water-right changes, not the domestic
   well exemption — but § 42-227(4) (2025) now requires a water-right permit
   for non-in-home use in new subdivisions inside moratorium or critical
   groundwater areas. Watch IDWR designations.
8. **Septic rules** — IDAPA 58.01.03 paragraphs are dated 7-1-25 (a fresh
   rewrite). Re-read the separation tables before any reprint.

---

## 10. LATE ADDENDUM

Two findings arrived after §§ 1–6 were first written and strengthened
rather than reversed them; recorded here so the build can see the change.

A. **§ 3.2 upgraded from `[H]` to `[V]`.** The first draft cited press
   coverage for the 2024-code rejection. The House Business Committee's own
   minutes of 17 February 2026 (retrieved from legislature.idaho.gov) and the
   Administrative Bulletin notice for Docket 24-3930-2502 (1 October 2025)
   now carry it.
B. **§ 1.1 gained the agency's own words.** DOPL's Plan Review Application
   states "DOPL does NOT issue building permits for projects not owned by the
   State. Contact the local government for these projects." The first draft
   proved the same point by statutory silence; the form quote is stronger and
   should lead in ID.1.
C. **The homeowner-form certification was located** ("will personally
   perform … not used for commercial purposes or rented by a tenant") and
   added to §§ 4.2 and 5.2. It changes nothing in the statute reading; it
   explains where the guide's "not for rent" language came from and confirms
   that "sale" and "lease" came from nowhere.

---

D. **Build pass, 8 September 2026 — nothing reversed; three additions.**
   Every `[V]` claim printed in ID.0–ID.5 was re-read against the saved
   primary source before printing (statute sections, IDAPA PDFs, DOPL
   forms, HBUS minutes) and none needed correcting. Recorded for the next
   revision:
   1. **Coeur d'Alene's Building Services page** (cdaid.org/building) says
      the team enforces "all applicable building, mechanical, accessibility,
      plumbing and housing codes" and lists the 2018 IMC among its adopted
      codes — so the city's local program likely covers mechanical as well
      as the plumbing verified in § 8.3. ID.4 prints the page's own words
      and tells the reader to ask the counter which trade permits the city
      issues itself; it does not assert an HVAC program.
   2. **DOPL has no regional permit offices.** Every homeowner form routes
      "all license applications, permit applications, fees, or forms to the
      Boise office," and inspectors are assigned by city and ZIP on the
      Inspector List. ID.4 describes DOPL as one office with inspectors by
      city; a kit brief that assumes "regional offices" is describing a
      structure DOPL does not publish.
   3. **The IDWR "Start Card"** — IDAPA 37.03.09.010.49 defines it as "an
      expedited drilling permit process for the construction of cold water,
      single-family residential wells." Printed in ID.2 and ID.5 as a
      definition only; the process itself was not read.

---

## 11. VERIFIED URL SET (September 2026)

Every address below returned HTTP 200 to curl with a browser User-Agent on
3 September 2026 unless marked.

### The four that matter most

| What | URL |
|---|---|
| ★ **DOPL location-based permit/jurisdiction map** ("Purchase your permit online HERE, based on location") | `https://idaho.maps.arcgis.com/apps/instant/sidebar/index.html?appid=c568d3c03d5f43f0841dcfa9c2a9537e` |
| ★ **DOPL Inspector List with Schedules** (electrical / HVAC / plumbing inspector by city and ZIP; dated 5 Aug 2026 — link from the trade pages, the filename changes) | `https://dopl.idaho.gov/wp-content/uploads/2025/09/BCRE-Inspector-list-with-schedule08052026.pdf` |
| ★ **DOPL public license/registration search** (contractor registration, electrical licenses, plumbing and HVAC certificates) | `https://edopl.idaho.gov/OnlineServices/?link=PubSearch` |
| ★ **Health districts by county** — Idaho Code § 39-408 | `https://legislature.idaho.gov/statutesrules/idstat/Title39/T39CH4/SECT39-408/` |

### Statutes (legislature.idaho.gov — pattern `/statutesrules/idstat/Title{T}/T{T}CH{C}/SECT{sec}/`)

| What | URL |
|---|---|
| Building Code Act, ch. 41 (index) | `https://legislature.idaho.gov/statutesrules/idstat/Title39/T39CH41/` |
| § 39-4111 permits; § 39-4116 local adoption; § 39-4117 timely review; § 39-4118 48-hour inspections | `…/Title39/T39CH41/SECT39-4111/`, `SECT39-4116/`, `SECT39-4117/`, `SECT39-4118/` |
| § 39-9701 energy code + preemption | `https://legislature.idaho.gov/statutesrules/idstat/Title39/T39CH97/SECT39-9701/` |
| Contractor Registration Act (index); § 54-5205 exemptions; § 54-5209 permit face | `https://legislature.idaho.gov/statutesrules/idstat/Title54/T54CH52/` |
| Electrical ch. 10; § 54-1001 (2023 NEC); § 54-1005 (utility lock); § 54-1016 (exemptions) | `https://legislature.idaho.gov/statutesrules/idstat/Title54/T54CH10/` |
| Plumbing ch. 26; § 54-2602 (owner exception); § 54-2620 (permits) | `https://legislature.idaho.gov/statutesrules/idstat/Title54/T54CH26/` |
| HVAC ch. 50; § 54-5002; § 54-5016 | `https://legislature.idaho.gov/statutesrules/idstat/Title54/T54CH50/` |
| Wells: § 42-227, § 42-235, § 42-238; § 42-111 | `https://legislature.idaho.gov/statutesrules/idstat/Title42/T42CH2/SECT42-235/` etc. |
| Property Condition Disclosure Act | `https://legislature.idaho.gov/statutesrules/idstat/Title55/T55CH25/` |
| § 45-525 general-contractor disclosures | `https://legislature.idaho.gov/statutesrules/idstat/Title45/T45CH5/SECT45-525/` |
| § 41-253 IFC 5-acre exemption | `https://legislature.idaho.gov/statutesrules/idstat/Title41/T41CH2/SECT41-253/` |
| Enrolled bills (effective-date clauses): H0337 (2023, NEC — eff. 1 Jul 2023); H0266 & S1164 (2025 — eff. 1 Jul 2025); H0585 & H0721 (2026 — eff. 1 Jul 2026); H0660 (2022, energy — eff. 1 Jul 2022) | `https://legislature.idaho.gov/wp-content/uploads/sessioninfo/{year}/legislation/{bill}.pdf` |
| House Business Committee minutes, 17 Feb 2026 (Docket 24-3930-2502 rejected) | `https://legislature.idaho.gov/wp-content/uploads/sessioninfo/2026/standingcommittees/260217_hbus_0130PM-Minutes.pdf` |

### Administrative rules (adminrules.idaho.gov — pattern `/rules/current/{title}/{chapter}.pdf`)

| What | URL |
|---|---|
| IDAPA 24.39.30 Building Code Rules | `https://adminrules.idaho.gov/rules/current/24/243930.pdf` |
| IDAPA 24.39.10 Electrical Board (NEC amendments, fees) | `https://adminrules.idaho.gov/rules/current/24/243910.pdf` |
| IDAPA 24.39.20 Plumbing (2015 UPC + amendments, fees) | `https://adminrules.idaho.gov/rules/current/24/243920.pdf` |
| IDAPA 24.39.70 HVAC (2018 IMC/IFGC, fees) | `https://adminrules.idaho.gov/rules/current/24/243970.pdf` |
| IDAPA 58.01.03 Septic rules | `https://adminrules.idaho.gov/rules/current/58/580103.pdf` |
| IDAPA 58.01.14 DEQ fees (septic permit minimums) | `https://adminrules.idaho.gov/rules/current/58/580114.pdf` |
| IDAPA 37.03.09 Well construction standards | `https://adminrules.idaho.gov/rules/current/37/370309.pdf` |
| IDAPA 37.03.10 Well driller licensing | `https://adminrules.idaho.gov/rules/current/37/370310.pdf` |
| Administrative Bulletin, Oct 2025 (Docket 24-3930-2502 proposed rule, p. 358) | `https://adminrules.idaho.gov/bulletin/2025/10.pdf` |

### DOPL

| What | URL |
|---|---|
| Building Code Board / Factory Built Structures | `https://dopl.idaho.gov/bld/` |
| Building statutes & rules + rulemaking history ("not currently engaged in rulemaking for 2026–2027") | `https://dopl.idaho.gov/bld/bld-statutes-and-rules/` |
| Plan Review and Permits (forms; the form that says DOPL does not issue non-state building permits) | `https://dopl.idaho.gov/bld/bld-plan-review-and-permits/` → `…/wp-content/uploads/2023/10/BLD-Plan-Review-Application-9-12-2023.pdf` |
| Electrical Board; FAQ; permits | `https://dopl.idaho.gov/ele/`, `…/ele/ele-faqs/`, `…/ele/ele-permits/` |
| Homeowner Electrical Permit Application | `https://dopl.idaho.gov/wp-content/uploads/2023/11/ELE-Home-Owner-Electrical-Permit-Application.pdf` |
| Plumbing Board; FAQ; permits (inspection codes 201 rough-in, 203 groundwork, 204 final) | `https://dopl.idaho.gov/plb/`, `…/plb/plb-faqs/`, `…/plb/plb-permits/` |
| Homeowner Plumbing Permit Application | `https://dopl.idaho.gov/wp-content/uploads/2023/11/PLB-Homeowner-Plumbing-Permit-Application.pdf` |
| HVAC Board; FAQ; permits (codes 701 rough-in, 704 final, 713 gas pressure) | `https://dopl.idaho.gov/hvac/`, `…/hvac/hvac-faqs/`, `…/hvac/hvac-permits/` |
| Homeowner HVAC Permit Application (Manual J/S/D review line) | `https://dopl.idaho.gov/wp-content/uploads/2023/10/HVAC-Home-Owner-Permit.pdf` |
| Contractors Board (registration; fees effective 1 Jul 2026) | `https://dopl.idaho.gov/con/` |
| eTRAKiT inspection-request portal (linked from DOPL; **no response to automated fetch**) | `https://web.dbs.idaho.gov/etrakit3/` |

### Septic, wells, other

| What | URL |
|---|---|
| DEQ septic program ("Idaho's seven public health districts administer these rules under a memorandum of understanding (MOU) with DEQ … issue septic system permits, inspect installations") | `https://www.deq.idaho.gov/water-quality/wastewater/septic-and-septage/` |
| Health districts: Panhandle (Dist. 1) · North Central (2) · Southwest (3) · Central (4) · South Central (5) · Southeastern (6) · Eastern (7) | `https://panhandlehealthdistrict.org/` · `https://idahopublichealth.com/` · `https://swdh.org/` · `https://cdh.idaho.gov/` · `https://phd5.idaho.gov/` · `https://siphidaho.org/` · `https://eiph.idaho.gov/` |
| IDWR wells ("Prior to drilling a well, the well owner or well driller must first obtain a drilling permit from IDWR. All wells must be constructed by a well driller with a valid license from IDWR.") | `https://idwr.idaho.gov/wells/`, `https://idwr.idaho.gov/wells/well-construction/` (licensed-driller search, well-log search) |
| IDWR drought declarations (2026 statewide) | `https://idwr.idaho.gov/legal-matters/drought-declarations/` |
| City of Boise building (own electrical/plumbing/mechanical fee schedules) | `https://www.cityofboise.org/departments/planning-and-development-services/building/` |
| City of Boise WUI overlay (IR1/IR2) | `https://www.cityofboise.org/departments/planning-and-development-services/planning/zoning/zoning-districts/wildland-urban-interface-overlay/` |
| Coeur d'Alene building (own plumbing amendments) | `https://www.cdaid.org/building` |
| ICC "2020 Idaho Residential Code" (2018 IRC base) | `https://codes.iccsafe.org/content/IDRC2020P1` |
| University of Idaho snow-load study (resource only; cited by no Idaho rule) | `https://www.lib.uidaho.edu/digital/idahosnow/` |

Dead or unusable: `https://idwr.idaho.gov/water-rights/domestic-water-use/` (404);
`https://dopl.idaho.gov/bld/bld-faqs/` and `/con/con-faqs/` (404 — the contractor
FAQ lives at `/con/con-faq/`); `https://dbs.idaho.gov/programs/building-program/`
(redirects to the DOPL home page; the legacy DBS statement is gone —
use the Plan Review Application form instead); `adminrules.idaho.gov/rules/current/24/`
index pages (404 — use the chapter PDFs).

---

## 12. LIVE GUIDE AUDIT — `src/app/permitting/state-guides/idaho/page.mdx`

Line numbers from `cat -n` of the 658-line file, September 2026. The MDX
pipeline has no heading ids; do not propose in-page anchors. Items are
grouped by severity: **A** = wrong on a statewide rule; **B** = unsupported
number or claim to delete; **C** = right but under-cited or hedged wrongly.

### A. Wrong on a statewide rule

| Line | Guide text (quoted) | Correction | Primary source |
|---|---|---|---|
| 20, 29, 48, 71, 79, 321, 542–543, 554, 621, 625, 658 | "Confirm whether your county/city enforces locally or whether DOPL is the building authority for your site" / "otherwise DOPL is the default building authority" / "**DOPL itself is the building authority** — it issues permits, reviews plans, and sends inspectors" / "Unincorporated areas in non-opted counties → DOPL Building Bureau is the default authority" / "DOPL-administered (non-opted counties) 2–5 weeks (plan review centralized through the state)" | **False.** DOPL issues no building permit for a private house. Where no city or county has adopted a building-code ordinance there is no residential building permit, plan review, building inspection or certificate of occupancy; the trade permits and the septic/well permits still apply. | § 39-4111(1)–(2); § 39-4103(2); § 39-4116(1), (7); DOPL Plan Review Application: "DOPL does NOT issue building permits for projects not owned by the State. Contact the local government for these projects." |
| 67 | "Idaho adopts code editions by **statute**, not just agency rulemaking — meaning a move to a newer IRC requires the Legislature to act" | Half wrong. The IRC/IBC edition is set by Building Code Board rule (effective 1 January after adoption). The **energy code edition** (2018 IECC) and the **NEC edition** (2023) are statutory. Board rules do face legislative review — which is how the 2024 update died on 17 Feb 2026. | § 39-4109(1)(b), (4); § 39-9701(1); § 54-1001; HBUS minutes 17 Feb 2026 |
| 30 | "Can a homeowner pull their own building permit — Yes for an owner-occupied residence (registration-exemption declaration typical)" | The contractor exemption applies "whether or not occupied by the owner." What the statute requires is the phrase "no contractor registration provided" on the permit face and posting on site; no issuing authority "shall be required to verify" the exemption. | § 54-5205(2)(l); § 54-5209(1)–(3) |
| 31, 148, 162, 556, 613, 617 | "not for commercial, sale, rent, or lease" / "not for property intended for sale, rent, or lease" / "not a flip or rental" | "Sale" and "lease" appear in no Idaho statute, rule or DOPL form. Statute: electrical licensing exemption = "noncommercial electrical work in the owner's primary or secondary residence or associated outbuildings"; plumbing and HVAC = "a single or duplex family dwelling … provided that such person owns or is a contract purchaser." DOPL form certification: "not used for commercial purposes or rented by a tenant" and "will personally perform the work." Print the three layers, labelled. | § 54-1016(2)(a); § 54-2602(1)(a); § 54-5002(1)(a); DOPL homeowner permit forms |
| 102 | "**Confirm locally**, but you generally won't be forced to sprinkler a single-family home" | Wrong hedge on a statewide rule. The exemption is statutory and binds local governments; R313.2 is deleted from the Idaho Residential Code. | § 39-4116(3); IDAPA 24.39.30.600.03.j |
| 120–125, 558, 609, 617 | "The exemption is lost only if you build with the intent to promptly sell — unless…" / "If you build and sell inside a year … you can lose the exemption" | Overstated. Subsection (l)'s proviso applies only to "an owner **who is otherwise regulated by this chapter**" building "for the purpose of promptly selling"; subsection (k)'s 12-month proviso requires "the intent to evade this chapter." Quote both provisos. | § 54-5205(2)(k), (l) |
| 143 | "Idaho Plumbing Board — journeyman/**master** and plumbing contractor licenses" | No master plumber exists in Idaho; classifications are contractor, journeyman, apprentice (and specialty equivalents), issued as certificates of competency. | § 54-2611 |
| 144 | "Idaho HVAC program — HVAC and **modular/mechanical** licenses" | HVAC certificates of competency: contractor, journeyman, apprentice, specialty (incl. specialty limited heating). "Modular/mechanical" is not a classification. | § 54-5009; § 54-5003 |
| 338–345 | Energy table: "Ceiling insulation R-49 / R-49"; "Wood-framed wall … R-20 + R-5 continuous (R-22 cavity option)" (Zone 6); "Floor R-30 / **R-38**"; "Windows U-0.30 max / U-0.30"; "Air leakage ≤3.0–5.0 ACH50 (per IECC; **verify locally**)" | Idaho replaced the rows. **Zone 5: ceiling R-38**, wall R-20 or 13+5, floor R-30, basement 15/19, slab R-10 2 ft, crawl 15/19, fenestration **U-0.32**. Zone 6: ceiling R-49, wall **R-22 or 13+5** (no R-20+5 option), floor **R-30**, slab R-10 4 ft, U-0.30. Air leakage: Idaho permits a **visual inspection in lieu of testing**, chosen by the permit holder at application; if tested the 2018 IECC figure for zones 3–8 is 3 ACH (5 ACH applies only to zones 1–2, none in Idaho). "Verify locally" is wrong: local governments are preempted from any energy requirement that differs from the state code. | IDAPA 24.39.30.600.06.b, .e; § 39-9701(2) |
| 347 | "Idaho's amendments tweak the base IECC — for example, **raising** required wall R-values in climate zone 6" | Idaho's Zone 6 wall row is "22 or 13+5" against the model code's "20+5 or 13+10" — a reduction, and by statute Idaho residential amendments may not be "more restrictive" than the ICC text. | IDAPA 24.39.30.600.06.b; § 39-4109(3) |
| 175, 181 | "Idaho applies seller-disclosure duties that survive the sale" / "Owner-built homes don't have to be labeled as such, but known defects, unpermitted work, and code issues must be disclosed" | A never-inhabited new house is **exempt** from the disclosure form except the three annexation/city-services questions. An owner who lives in the house and later sells completes the form, including "Have any substantial additions or alterations been made without a building permit?" | § 55-2505(12); § 55-2508 q. 8 |
| 219 | "State electrical permit (DOPL) $65 + $10 per branch circuit for additions/shops, or a square-footage fee for a new dwelling" | No per-circuit fee exists. New one-family dwelling: $130 (≤1,500 sq ft) / $195 / $260 / $325 (to 4,500) + $65 per 1,000 sq ft; existing dwelling $65 per inspection. | IDAPA 24.39.10.500.02.a |
| 195 | "DOPL's building fee schedule (**the default where a county hasn't adopted its own**)" | Table 1-A applies only to DOPL-issued permits (state buildings, schools, modular). There is no default for a house. The anchor values quoted are correct for Table 1-A (rows dated 7-1-26, not "January 1, 2025"). | IDAPA 24.39.30.500.03.b; § 39-4111 |
| 61 | "Electrical: 2023 NEC … adopted by the Idaho Electrical Board / DOPL" | Adopted by the **Legislature** (H0337, 2023 ch. 244, effective 1 July 2023); the Board amends it by rule. And the guide never mentions that Idaho amends the NEC downward (AFCI bedrooms only; kitchen/laundry/appliance GFCI items deleted; SPD and emergency disconnect permissive). | § 54-1001; IDAPA 24.39.10.600.01 |
| 60, 658 | "2018 IECC with Idaho amendments; **effective January 1, 2021**" | Unverified date. The statute pins the 2018 IECC "on and after July 1, 2022." Print the statute date or none. | § 39-9701(1); H0660 (2022) §4 |

### B. Unsupported numbers and claims — delete or replace

| Line | Guide text | Disposition |
|---|---|---|
| 39, 94, 402–421, 593, 633 | "several mountain counties require a site-specific engineered snow load"; "Ada, Kootenai, Bonneville, Blaine, Valley, and Bonner counties — the snow load is a **case-study** value"; "~20–25 psf in Boise … 140 psf … 200 psf"; the psf table; "several counties publish their own maps that supersede it" | No primary source. Replace with: ground snow load is an IRC R301.2 design criterion that § 39-4116(4)(c)(iii) lets each county set by ordinance; ask the building official for the adopted value or the required study; the University of Idaho study is a resource no Idaho rule cites. |
| 96, 427–444, 519, 524, 594 | Seismic Design Category by city; "Idaho-specific amendment … Seismic: Higher design categories" | Not an Idaho amendment; SDC is an R301.2 local design criterion. Delete the table; keep a one-line pointer to the USGS design maps and the local official. |
| 351–365, 503 | Frost-depth table by region; "24\" frost depth" | Local (R301.2). Keep the callout that frost depth is local; delete the numbers. The one statewide depth number is the **42-in** water-service burial depth (IDAPA 24.39.20.600.21). |
| 131 | "Most Idaho building departments require you to sign a contractor-registration exemption declaration … standard paperwork in counties like Kootenai and Shoshone" | County practice unverified. Replace with § 54-5209. |
| 213–286, 560, 629 | All city/county cost tables; "$993.75 for the first $100,000"; "$90/sq ft"; "10% of the building permit fee in the City of Coeur d'Alene"; resort-county totals | Unverified local figures. Replace with the DOPL trade-permit fee ladders (rule-cited) and "building permit: see the county's § 39-4117(1) process document and fee ordinance." |
| 191, 205, 243 | "plan-review fee that runs as high as 65%" | 40–65 % is DOPL's own rule for DOPL permits; local percentages are local. |
| 295 | "Snow-load engineering letter $500–$2,000" | Delete. |
| 296 | "Septic permit and site evaluation $300–$1,200 via your public health district" | Replace with the state minimum fee: $400 basic/complex system permit, $300 tank-only, $40 renewal; districts "may adopt different fees" and must publish them. IDAPA 58.01.14.110. |
| 312–324 | Processing-timeline table ("4–8 weeks" …) | Delete. Replace with the statutory clocks: 10 business days to notify an incomplete residential application and 10 business days per completeness review (§ 39-4117); no plan-review clock for houses; 48-business-hour inspection rule with third-party self-help (§ 39-4118, § 54-1004A, § 54-2626A, § 54-5020A). |
| 370–388 | 13-step inspection table | No statute enumerates it. Replace with IRC R109 as adopted (local) plus the rule-based trade rungs: plumbing groundwork → rough → final (IDAPA 24.39.20.500.03); HVAC work-in-progress → final (24.39.70.500.03); electrical cover → final (24.39.10.500.01.a.i); septic site inspection on 48 hours' notice and final with as-built before use (IDAPA 58.01.03.011). |
| 455 | Boise WUI "defensible-space fuel-modification distance of at least 30 feet"; "Ada County, Boise County, and others have parallel rules" | The city page verifies IR1 = Class 1 ignition-resistant construction and a defensible-space section; the 30-ft figure and the county parallels were not verified. |
| 469–487 | Septic and well cost tables | Market figures; keep only if labelled as estimates with no Idaho cite. |
| 172 | "workers' comp is required for paid employees in Idaho" | Hedge with § 72-212 exemptions (casual employment; household family members; sole proprietor) and note "casual employment" is undefined in § 72-102. |

### C. Right, but fix the citation or the hedge

| Line | Guide text | Fix |
|---|---|---|
| 20, 28, 552, 605 | "exempt under Idaho Code § 54-5205" | Cite subsection (2)(l) (and (k) for the hire-a-registered-contractor case). |
| 33, 58–63, 658 | Code editions | All correct: 2018 IRC (ICC "2020 Idaho Residential Code"), 2018 IBC, 2018 IECC, 2023 NEC, 2017 ISPC on the 2015 UPC (DOPL FAQ wording; the rule adopts the 2015 UPC), 2018 IMC/IFGC. Add citations: § 39-4109; IDAPA 24.39.30.600; § 54-1001; IDAPA 24.39.20.600; IDAPA 24.39.70.600. |
| 71, 80, 86, 392 | "Under § 39-4116, a city or county may adopt and run its own program"; "confirm your building authority and your trade authority separately" | Correct. Add: local trade programs require 30 days' written notice to DOPL and DOPL backstops a terminated program for one year (§ 54-1001B(4)–(5); § 54-2601(7)–(8)); Boise runs all three trades, Coeur d'Alene its own plumbing; use DOPL's location-based permit map. |
| 94, 364 | "Snow load: Determined locally"; "Frost depth is set by the local building official" | Correct; cite § 39-4116(4)(c)(iii) (R301 Design Criteria is locally amendable). |
| 95, 330 | "2018 IECC … climate zones 5B and 6B" | Correct; add § 39-9701 and the preemption. |
| 97, 100 | "sprinklers are not required statewide in single-family homes" | Correct; cite § 39-4116(3). Drop "confirm locally." |
| 98 | "Radon: Not a statewide mandate" | Keep as a hedge, but note the Part IX open question (§ 8.1) rather than asserting either way. |
| 154 | "renewable/solar grid-tie triggers a plans review" | Correct; cite § 54-1016(2)(a) ("preplan review in accordance with local jurisdictions' policies and procedures prior to the purchase of a permit"). |
| 156 | "refrigerant handling still needs EPA 608 certification" | Federal; say so and cite nothing Idaho. |
| 461 | Septic under IDAPA 58.01.03 via the seven health districts | Correct; cite § 39-408 for the districts and the DEQ page for the MOU. Add: permit required before any installation (005.01); owners may install their own standard or basic alternative system without an installer's registration (006.08.b); permit valid two years (005.08); no wastewater until the final inspection and as-built (011.05); two full drainfield areas required (008.02.c). |
| 478 | "Wells are permitted through IDWR … a domestic well is generally allowed" | Correct; add the $75 drilling permit before any drilling (§ 42-235), the licensed-driller requirement with no owner exemption (§ 42-238(2)–(3)), the domestic-use ceiling (13,000 gpd incl. ½ acre irrigation, § 42-111), and the 2025 subdivision/moratorium carve-out (§ 42-227(4)). |
| 492 | "Idaho declared a statewide drought emergency in 2026" | Correct (IDWR drought page); note it enables temporary water-right changes and expires at year-end unless extended; it does not change the domestic-well exemption. |
| 498 | Modular/manufactured under DOPL | Correct; cite § 39-4116(7). |
| 114 | "requires a person who contracts to construct for others to register" | The definition is broader ("undertakes … or does himself or by or through others, perform construction"); the owner exemptions are what carve the owner out. Cite § 54-5203(3). |

### D. Material omissions

1. **The utility lock** — power suppliers, including co-ops, may not energize
   before a passed DOPL inspection; only a licensed contractor's permit
   unlocks construction temp power (§ 54-1005(3); IDAPA 24.39.10.200.04).
2. **The 48-business-hour inspection rule** with the third-party self-help
   remedy and fee refund, across building, electrical, plumbing and HVAC
   (§ 39-4118; §§ 54-1004A, 54-2626A, 54-5020A), and the § 39-4117
   completeness clocks and mandatory published permit-process document.
3. **Idaho's downward NEC amendments** — AFCI bedrooms only; kitchen,
   laundry, appliance and garage/outbuilding GFCI items deleted; SPD and
   emergency disconnect permissive (IDAPA 24.39.10.600.01).
4. **Energy-code preemption** — no city or county may add any energy
   requirement (§ 39-9701(2)); **visual inspection in lieu of blower-door
   test** at the permit holder's election (IDAPA 24.39.30.600.06.e).
5. **The rejected 2024 code update** (HBUS 17 Feb 2026) and DOPL's "no
   rulemaking for 2026–2027."
6. **§ 54-5209** — "no contractor registration provided" on the permit face;
   posting; issuers need not verify.
7. **Teeth against unregistered subs** — no lien (§ 54-5208), no suit for
   payment (§ 54-5217(2)); registered contractors carry $300,000 GL
   (§ 54-5210(1)(e)); **§ 45-525 disclosure rights** (lien waivers, proof of
   insurance, surety bond, extended title insurance; sub/supplier list before
   final payment).
8. **Contract purchasers** qualify for the plumbing and HVAC homeowner
   exemptions (§ 54-2602(1)(a); § 54-5002(1)(a)).
9. **Agricultural-building exemption** and its "place of human habitation"
   definition (§ 39-4116(5)); no electrical parallel.
10. **5-acre rural exemption** from IFC water-supply and access requirements
    (§ 41-253(2)).
11. **Whole-house mechanical ventilation is mandatory** (R303.4 replaced,
    IDAPA 24.39.30.600.03.h); floor-membrane rule deleted (R302.13); Idaho
    footing table; APA SR-102 bracing alternate.
12. **Plumbing specifics**: 42-in water-service cover; mandatory softener
    loop on slab/finished-basement houses; 2-in minimum underground DWV;
    AAV limits (IDAPA 24.39.20.600.21, .26, .30, .46).
13. **Owner may install own standard septic system** (IDAPA
    58.01.03.006.08.b); **no owner may drill a well** (§ 42-238(3)).
14. **Separation tables** (drainfield, tank, well) and the 20 % slope /
    two-drainfield-area disqualifiers — the Site Plan Studio content.
15. **Manual J/S/D review** line on the DOPL homeowner HVAC form for new
    dwellings.
16. **EV-infrastructure prohibition** (§ 39-4109B) and the single-stair
    apartment section (§ 39-4109C) as evidence Title 39 ch. 41 is being
    amended every session.
