# Pennsylvania Owner-Builder Permit Kit — Research Dossier

Kit 18 of the 50-state program. Compiled September 2026 for
`binder-pipeline/kits/pa-permit-kit/` (PA.0–PA.5).

**Marking convention.** `[V]` = read in a primary source and quoted here.
`[H]` = secondary, inferred, or reasoned — not printed in the kit as a
citation. Anything unverifiable was deleted rather than softened.

**Primary sources used.**

| Source | What it is | Where |
|---|---|---|
| 35 P.S. §§ 7210.101 et seq. | Pennsylvania Construction Code Act (Act 45 of 1999) | legis.state.pa.us → palegis.us, Unconsolidated Statutes, 1999 Act 45 |
| 34 Pa. Code Ch. 401, 403 | UCC administration regulations | pacodeandbulletin.gov, Title 34 |
| 25 Pa. Code Ch. 73 | Standards for onlot sewage treatment facilities | pacodeandbulletin.gov, Title 25 |
| 73 P.S. §§ 517.1–517.19 | Home Improvement Consumer Protection Act (Act 132 of 2008) | palegis.us, 2008 Act 132 |
| PA L&I UCC pages | Opt-in/opt-out table, third-party agency list, licensing statement | pa.gov/agencies/dli |

> **Fetching note for future revisions.** `pa.gov` and `legis.state.pa.us`
> return **HTTP 403 to a default curl**. Pass a browser User-Agent. The Pa.
> Code site is fine without one. `pacodeandbulletin.gov` chapter TOC URLs
> return the **entire chapter text**, not just a table of contents, which
> makes them the fastest way to read a chapter:
> `https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/034/chapter403/chap403toc.html`

---

## 0. THE HEADLINE — WHAT MAKES THIS KIT DIFFERENT

Pennsylvania is the state where the standard owner-builder framing collapses,
because there is **no owner-builder exemption and nothing to be exempt from**.
Pennsylvania issues no general contractor license at all. So document 1 cannot
be an exemption walkthrough; it has to answer the question Pennsylvania
actually poses.

That question is **who inspects your house**, and it has a genuinely
surprising answer in 119 municipalities: *nobody, until you go and hire
them*.

Five findings carry the kit:

1. **The UCC applies statewide, and five inspections are required
   everywhere.** `[V]` No rural exception exists. The "opt-out = no
   inspections" belief is false.
2. **In an opt-out municipality the *permit applicant* must hire a certified
   third-party agency.** `[V]` 34 Pa. Code § 403.103(b), by name. L&I is not
   the fallback — it takes only non-residential work there.
3. **The required residential inspection list is FIVE items and it is in the
   statute.** `[V]` Not the 10–13 that circulating advice prints.
4. **An owner in an opt-out municipality has no statutory appeal.** `[V]`
   Verified by chaining three provisions. This is the strongest original
   finding in the kit and it cuts against the "opt-out is freedom" story.
5. **Pennsylvania amends the model codes in two places, and one amendment
   rolls wall bracing back to the 2006 IRC.** `[V]` Statutory, not
   regulatory, so it is invisible to anyone reading only 34 Pa. Code.

---

## 1. THE CENTRAL THESIS — WHO ENFORCES

### 1.1 Statewide application `[V]`

35 P.S. § 7210.104(a): "This act shall apply to the construction, alteration,
repair and occupancy of **all buildings in this Commonwealth**."

34 Pa. Code § 403.1(a)(1) repeats it for construction occurring on or after
9 April 2004.

### 1.2 The six enforcement paths `[V]`

35 P.S. § 7210.501(b) gives five ways for a municipality that adopted an
enforcing ordinance:

1. designate its own employee as municipal code official;
2. retain one or more code officials or **third-party agencies** to act on its
   behalf;
3. joint administration with other municipalities by intergovernmental
   agreement;
4. contract with another municipality (whose official then holds full
   authority);
5. **agreement with the Department — but expressly only for "structures other
   than one-family or two-family dwelling units and utility and miscellaneous
   use structures."**

Path 5 is the asymmetry that kills the common belief that "L&I handles it."
**L&I never reviews or inspects houses.**

The sixth case is the municipality that adopted no ordinance — § 7210.501(e).

### 1.3 Opt-out mechanics — the kit's thesis `[V]`

**34 Pa. Code § 403.103(b), verbatim:**

> "An applicant for a residential building permit shall obtain the services of
> a third-party agency certified in the appropriate categories to conduct the
> plan review and inspections under §§ 403.61—403.66 (relating to permit and
> inspection process for residential buildings)."

**35 P.S. § 7210.501(e)(1), verbatim** — the municipality's duty to tell you,
and the inspection list:

> "In municipalities which have not adopted an ordinance for the
> administration and enforcement of this act, it shall be the duty of the
> municipality to notify an applicant for a construction permit that it shall
> be the responsibility of the permit applicant of one-family or two-family
> dwelling units and utility and miscellaneous use structures to obtain the
> services of a construction code official or third-party agency with
> appropriate categories of certification to conduct the plan review and
> inspections. For one-family and two-family dwelling units and utility and
> miscellaneous use structures, all of the following five inspections shall be
> required: (i) Foundation inspection. (ii) Plumbing, mechanical and
> electrical inspection. (iii) Frame and masonry inspection. (iv) Wallboard
> inspection. (v) Final inspection. The final inspection shall not be deemed
> approved until all previous inspections have been successfully completed and
> passed."

**34 Pa. Code § 403.103(g)** `[V]`: for buildings **other than** residential,
the municipality notifies the applicant to obtain the Department's services.
That is the commercial half, and the reason the split is so widely
misreported.

**§ 403.103(e), (f)** `[V]`: the third-party agency retains copies of all final
inspection reports, and sends a copy of the final report to the property
owner, the builder, **and a lender designated by the builder**.

**L&I's own words, on its UCC home page** `[V]`:

> "If a municipality has 'OPTED-OUT,' the Department is responsible for all
> commercial code enforcement in that municipality." … "Certified third party
> agencies hired by property owners (or their contractors) enforce the
> residential requirements of the UCC in all opt-out municipalities."

### 1.4 How many have opted out — HARD NUMBER `[V]`

L&I publishes a live table of every municipality's election.

- Table (direct):
  `https://www.pa.gov/content/dam/copapwp-pagov/en/dli/documents/individuals/labor-management-relations/bois/documents/uccmun.htm`
- Landing page: L&I → UCC → Municipal Elections and Contact Information

Parsed row by row, September 2026: **2,563 rows — 2,444 OPT-IN (95.4%) and
119 OPT-OUT (4.6%)**. Opt-out rows carry a blank building code official,
consistent with there being nobody to call. **34 of 67 counties** contain at
least one opt-out municipality; no county is entirely opted out.
Concentrations: Crawford 13, Erie 12, Clinton 10, Westmoreland 10, Luzerne 8.

**Correction to L&I's own prose**: the narrative page says "Over 90% of
Pennsylvania's 2,562 municipalities" — its own table says 95.4% and 2,563
rows. Cite the table, and always with a retrieval date: a municipality may
change its election on 180 days' notice.

### 1.5 The opt-out appeals gap `[V]` — strongest original finding

Chain three provisions:

- **34 Pa. Code § 403.121(a)** — a board of appeals is required of a
  municipality that *has adopted* a UCC ordinance, or of municipalities party
  to a joint agreement. An opt-out municipality is neither.
- **34 Pa. Code § 403.63(i)** — a residential permit applicant may appeal "in a
  municipality which has adopted an ordinance for the administration and
  enforcement of the act." The qualifier is express.
- **34 Pa. Code § 403.141(d)–(e)** — the Industrial Board hears appeals of
  **Department** decisions. In an opt-out municipality the residential
  decision-maker is a private company.

**Result: no statutory forum exists to appeal a third-party agency's
residential code decision.** What remains is a written signed complaint to
L&I under § 403.104(a) / 35 P.S. § 7210.105(a), which can lead to
decertification — discipline of the official, not review of the decision.

Kit guidance: negotiate a second-review mechanism into the agency engagement
letter, because no statutory one exists.

### 1.6 In an enforcing municipality the appeal is excellent `[V]`

35 P.S. § 7210.501(c)(5): for a one- or two-family dwelling the board "shall
convene a hearing within 30 days," decide in writing within 5 business days
(10 in cities of the first class), and **"[i]f the board of appeals fails to
act within the time period under this paragraph, the appeal shall be deemed
granted."** Fee capped at actual notice, court-reporter and administrative
costs (§ 7210.501(c)(4)).

---

## 2. SCOPE — WHAT IS OUTSIDE THE CODE

### 2.1 Statutory exclusions `[V]` — 35 P.S. § 7210.104(b)

Agricultural buildings; utility and miscellaneous structures accessory to
detached one-family dwellings; repairs to residential buildings; alterations
making no structural change and no change to means of egress (expressly, "a
structural change does not include a minor framing change needed to replace
existing windows or doors"); aluminum/vinyl siding on existing buildings;
**recreational cabins**; certain temporary structures under 1,600 sq ft for
under 30 days; seasonal farm-product stands; livestock-auction structures.

34 Pa. Code § 403.1(b) adds: accessory carports, detached private garages,
greenhouses and sheds **under 1,000 sq ft** accessory to a detached one-family
dwelling; propane/LP gas installations; manufactured and industrialized
housing; **and construction of individual sewage disposal systems under
25 Pa. Code Ch. 73**.

### 2.2 The recreational cabin — the one real no-permit path `[V]`

35 P.S. § 7210.103 definition, all seven parts required. A structure which is:

1. utilized principally for recreational activity;
2. **not utilized as a domicile or residence for any individual for any time
   period**;
3. not utilized for commercial purposes;
4. not greater than two stories in height, excluding basement;
5. not utilized by the owner or any other person as a place of employment;
6. not a mailing address for bills and correspondence; and
7. not listed as an individual's place of residence on a tax return, driver's
   license, car registration or voter registration.

**Not self-executing** — § 7210.104(b)(7)(ii): the owner must file with the
municipality *either* an affidavit on the Department's prescribed form *or*
valid proof of insurance from an insurer authorized in Pennsylvania, stating
the structure meets the definition.

### 2.3 No owner-builder exemption exists `[V]`

Searched the Act and Chapter 403. There is no provision treating a dwelling
built by its owner differently. There is nothing to be exempt from: L&I's
Contractor Licensing page states, verbatim, **"The Commonwealth of
Pennsylvania currently has no licensure or certification requirements for most
construction contractors (or their employees)."**

---

## 3. CODE EDITIONS AND AMENDMENTS

### 3.1 Editions in force `[V]` — 2021 I-Codes, effective 1 January 2026

34 Pa. Code § 403.21(a) adopts the 2021 IBC, IMC, IFGC, IPC, IRC, IEBC, IECC,
International Performance Code, International Wildland-Urban Interface Code
and International Swimming Pool and Spa Code. Source note: "amended November
7, 2025, effective January 1, 2026, **55 Pa.B. 7701**."

> **⚠ L&I's own UCC home page is stale.** As of September 2026 it still
> described the **2018** I-Code series with an effective date of 14 February
> 2022. The regulation governs. Print this warning in the kit — a reader who
> "verifies" against the web page will be misled. `[V]`

Transition rule `[V]` — § 403.1(a)(2): work under a design or construction
contract executed before the amendment's effective date complies with the
codes in effect when that contract was signed.

**2024 cycle is OPEN** `[V]`: L&I's RAC page carries an active 2024 Code
Review Cycle with comments reopened through **4 October 2026**. The 2021 cycle
ran ~59 months from ICC publication to effect. **Do not print a projected 2024
effective date.** Tripwire — see § 9.

### 3.2 Appendices are NOT adopted `[V]` — § 403.21(c)

"Appendices to a code or standard listed in subsection (a) are not adopted in
the Uniform Construction Code except for the appendices and resource
information found in the 'International Existing Building Code of 2021' and
the appendices found in subsection (a)(12) and (13)" (IBC 2018 App. E; IBC 2009
App. H).

**Consequence: IRC Appendix F is not adopted, so the UCC imposes NO
radon-resistant construction requirement** — in the state with among the
highest indoor radon in the country. Verified negative; high-value kit
content.

### 3.3 Statutory amendments — 35 P.S. § 7210.304, Act 1 of 2011 `[V]`

These are invisible to anyone reading only the regulation.

| Subject | What Pennsylvania actually requires | Cite |
|---|---|---|
| **Wall bracing** | 2009 IRC R602.10—R602.12.1.6 "and any successor provisions" **excluded**; **2006 IRC R602.10—R602.11.3** is what applies | § 7210.304(i) |
| **Floor membrane** | Non-rated floor assemblies need ½-in gypsum wallboard, ⅝-in wood structural panel or equivalent on the underside. Exceptions: sprinklered space below; crawl space not used for storage or fuel-fired appliances; ≤80 sq ft per story unprotected if fireblocked at the perimeter; dimension lumber or SCL ≥ 2×10 nominal | § 7210.304(h) |
| **Sprinklers** | IRC R313.2 "and any successor triennial revisions" excluded. Builder must **offer** the option in writing at/before the purchase contract, with cost information and the Fire Commissioner's material | § 7210.304(g) |
| Log walls | Special energy treatment | § 7210.304(f) |
| Refrigerants | EPA-approved refrigerants permitted notwithstanding code prohibition; expires on adoption of the 2024-cycle regulation | § 7210.304(j) |

### 3.4 Regulatory amendments — § 403.21(a)(7) `[V]`

**Stairs** (§ 403.21(a)(7)(ii)) — more permissive than the model code: max riser
**8¼ in**; min tread **9 in**; riser variation ≤ ⅜ in within a flight; greatest
tread depth ≤ ⅜ in over the smallest; tread projection ≤ 1½ in with solid
risers; min 3 ft clear width; 6 ft 8 in headroom; handrails may project 3½ in
each side.

**Vapor retarder** (§ 403.21(a)(7)(iv)(E)) — R506.2.3 modified, striking "10 mil
… ASTM E1745 Class A" and inserting **"6 mil."**

**Excluded IRC provisions** (§ 403.21(a)(7)(iii)) include R311.7.4 (walkline),
R314.4 (smoke alarm interconnection), R325.5 (openness), R703.7 (exterior
plaster/stucco), R806.2 (minimum vent area), R1005.8 (insulation shield), and
a long list of energy sections. § 403.21(a)(7)(i) separately provides that
interconnected smoke alarms do not apply to one- and two-family dwellings
undergoing alterations, repairs or additions, where non-interconnected
battery-operated alarms are installed instead.

**Intermodal shipping containers** (§ 403.21(a)(7)(iv)(A)) — before permitting,
certified free from contaminants by a qualified third-party inspector approved
by the AHJ; penetrations beyond IBC § 3115 certified by a PA Registered Design
Professional.

### 3.5 ⚠ ELECTRICAL — the Pennsylvania trap `[V]`

**Pennsylvania adopts NO edition of NFPA 70 for residential work.** The strings
"NFPA 70" and "National Electrical Code" appear nowhere in 34 Pa. Code
Chapter 403. What governs is **IRC 2021 Chapters 34–43** (E3401–E4304).

The trap is not a lagging edition — it is a **three-section carve-back**:

| Provision | Status | What governs in PA |
|---|---|---|
| E3901.4.2 island/peninsula countertop | excluded | **2018 IRC** text |
| E4002.11 bathtub and shower space | excluded | **2018 IRC** text |
| E3901.11 foyers | excluded | **2015 IRC** text, modified "3 feet" → **"6 feet,"** min one receptacle |
| E4004.5 means of support | modified | 2021 text, "E3906.12" → "E3905.6.3" |

Everything else in Chapters 34–43 — **including all AFCI and GFCI
requirements and service sizing** — is the 2021 IRC as published.

**DO NOT print an NEC year as a Pennsylvania citation.** `[H]` The IRC 2021
electrical chapters correlate to the 2020 NEC by ordinary ICC/NFPA practice,
but no Pennsylvania source says so, and the kit must cite E-sections.

### 3.6 Energy — Pennsylvania replaced the tables `[V]`

§ 403.21(a)(9)(vi)(D) substitutes its own **Table R402.1.3**. Values for the
three Pennsylvania zones:

| Component | Zone 4 (exc. Marine) | Zone 5 | Zone 6 |
|---|---|---|---|
| Ceiling | R-49 | R-49 | R-49 |
| Wood frame wall | R-20, or 13+5 | R-23, or 13+7.5, or 20+3.8 | R-20+5, or 13+10 |
| Floor | R-19 | R-30 | R-30 |
| Basement wall | 10/13 | 15/19 | 15/19 |
| Crawl space wall | 10/13 | 15/19 | 15/19 |
| Slab | R-10, 2 ft | R-10, 4 ft or R-15, 3 ft | R-10, 4 ft |
| Fenestration U | 0.32 | 0.30 | 0.30 |
| Skylight U | 0.55 | 0.55 | 0.55 |
| Glazed SHGC | 0.40 | NR | NR |

Footnotes: "13+5" = R-13 cavity + R-5 continuous; "10/13" = R-10 continuous *or*
R-13 cavity; "15/19" may alternatively be R-13 cavity + R-5 continuous; a floor
may alternatively be insulated to fill the cavity at ≥ R-19.

**Ceiling stayed at R-49** — the unamended 2021 IECC would require R-60 in
these zones. **`[V]`**

**Air leakage: 3.0 ACH50.** Pennsylvania did **not** amend IECC R402.4.1.2, so
the 2021 requirement stands: 5 ACH in Climate Zones 1–2, **3 ACH in Climate
Zones 3 through 8** — which is all of Pennsylvania. Confirmed by the standard
reference design air-exchange row printed in the adopted tables. `[V]`

**Duct testing exceptions** (amended R403.3.5) `[V]`: no duct air-leakage test
where ducts and air handlers are entirely within the building thermal
envelope, or for ducts serving HRV/ERV units not integrated with the heating
or cooling ducts.

**Compliance paths** `[V]` — § 403.21(d)(1): REScheck, or **"Pennsylvania's
Alternative Residential Energy Provisions."**

**Climate zone is determined locally** `[V]` — § 403.103(d): the building code
official determines the climatic and geographic design criteria in IRC Table
R301.2(1). The kit therefore prints the table by zone and tells the reader to
confirm the zone, rather than printing a county map.

---

## 4. PERMITS, CLOCKS AND INSPECTIONS

Residential sections are **§§ 403.61–403.66**. The near-identical commercial
sections are §§ 403.41–403.48 — a very easy citation error, and one the
published state guide makes.

| Item | Rule | Cite `[V]` |
|---|---|---|
| Application contents | Construction documents, plans and specs, **all other permits or approvals**, site plan | § 403.62a(b), (e) |
| **Site plan** | "size and location of the new construction and existing structures on the site and the structures' distance from lot lines" | § 403.62a(e) |
| Flood data | Boundaries, zones, design flood elevation, proposed lowest floor incl. basement; Zone AO height above grade | § 403.62a(d) |
| Review clock | **15 business days**, or **5** with a licensed design professional's certification; else **deemed approved** | § 7210.502(a)(1), (3); § 403.63(a) |
| Other-permits list | Municipality "shall also provide a list of all other required permits" — and "will not be liable for the completeness of any list" | § 7210.502(a)(1) |
| Permit issuance | Issued "immediately upon receipt of all other required permits or approvals" once the plan is approved | § 7210.502(a)(1) |
| Permit life | Invalid if work not begun in **180 days**, or suspended/abandoned **180 days**; **max 5 years** | § 403.63(g) |
| Foundation-only permit | Permitted; no assurance the rest is approved | § 403.63(e) |
| Revisions | Require an additional plan review | § 403.63(j) |
| **Inspections** | Foundation; plumbing/mechanical/electrical; frame and masonry; wallboard; final | § 403.64(d), (f); § 7210.501(e)(1) |
| Additional inspections | Official "may conduct other inspections" | § 403.64(e) |
| **Inspector response time** | **NONE. No deadline exists anywhere.** | — (verified absence) |
| Certificate of occupancy | Required to occupy; **5 business days**, **10 in cities of the first class** | § 403.65(a), (b) |
| CO contents | Includes **the construction code edition applicable** and whether sprinklers are provided | § 403.65(b)(6), (7) |
| Fees | May be established, **no state maximum**; schedule must be public | § 401.2a(a), (b) |
| Conflict of interest | Code administrator may not review work in which he has a financial interest | § 7210.502(c) |
| HOP | Permit must carry notice an HOP is required; PennDOT has **60 days** or it is deemed issued | § 7210.502(b); § 403.63(d) |
| Alternatives | Official **"shall approve"** an equivalent alternative material, design or method; must accept the International Performance Code of 2021 as an alternative | § 403.103(c); § 403.44 |

**The no-inspector-clock finding** `[V]`: § 403.64(b) obliges the permit holder
to notify when work is ready, with no stated notice period; no provision of
the Act or Chapter 403 obliges the official to respond within any time. Every
"business days" deadline in the scheme attaches to permits, certificates or
appeals — never to attending an inspection. Kit frames this as the reason to
negotiate response times into a third-party agency contract.

---

## 5. LICENSING AND CONTRACTS

### 5.1 No state contractor license `[V]`

L&I Contractor Licensing page: "The Commonwealth of Pennsylvania currently has
no licensure or certification requirements for most construction contractors
(or their employees)." Narrow state programs exist for crane operators,
asbestos/lead abatement and manufactured-housing installers — none reaches a
house build.

### 5.2 Trade licensing is municipal `[V]`

Same page: "Some of Pennsylvania's 2,562 municipalities have established local
licensure or certification requirements for contractors or construction trades
people. Typically, these requirements pertain to home improvement contractors,
electrical contractors (or electricians), and plumbing contractors (or
plumbers)." **There is no statewide registry to search.**

### 5.3 ⚠ Allegheny County plumbing carve-out `[V]`

**35 P.S. § 7210.501(a.1)**: a municipality in a **county of the second class**
(Allegheny) "shall not administer and enforce plumbing code provisions" of its
UCC ordinance; the county retains authority to promulgate and enforce its own
plumbing code under the Local Health Administration Law.

**34 Pa. Code § 403.21(a)(6)(i)** repeats it: such a municipality "may not
administer and enforce the 'International Plumbing Code' adopted under this
chapter."

Practical effect: a separate permit, inspector and rulebook for plumbing, from
the county rather than the municipality.

### 5.4 HICPA does not reach a new house `[V]`

73 P.S. § 517.2, definition of "home improvement," paragraph (2):

> "The term does not include: **(i) The construction of a new home.** … (v) Any
> work performed without compensation by the owner of the owner's private
> residence or residential rental property."

"Contractor" excludes "a person for whom the total cash value of all of that
person's home improvements is less than **$5,000** during the previous taxable
year." Registration duty: § 517.3(a).

### 5.5 HICPA terms as a drafting benchmark `[V]`

Because the build is outside HICPA, none of its protections attach. The kit
prints them as terms to copy:

| Term | Requirement | Cite |
|---|---|---|
| Deposit cap | On a contract over $5,000, no more than **⅓ of the contract price**, plus designated special-order materials | § 517.9(10) |
| Liability insurance | Not less than **$50,000** personal injury and **$50,000** property damage; current amount stated in the contract | § 517.7(a)(11) |
| Time-and-materials | Written initial estimate before work starts; cost may not exceed **10%** above it without a signed change order | § 517.7(a)(8) |
| Change orders | Specifications "cannot be changed without a written change order signed by the owner and the contractor" | § 517.7(a)(7) |
| Named subs | Names and addresses of all subcontractors known at signing; a PO box is not an address | § 517.7(a)(10) |
| Dates; deposit shown | Approximate start and completion dates; down payment and special-order materials listed **separately** | § 517.7(a)(6), (9) |

Verification: OAG registration search at `hicsearch.attorneygeneral.gov`
(HTTP 200, September 2026); registration page at
`attorneygeneral.gov/businesses-and-organizations/home-improvement-contractor-registration/`.

---

## 6. SITE PLAN STUDIO EXTRACTION

Feeds `src/lib/siteplan/rules.ts`. **All values `[V]`, quoted from
25 Pa. Code § 73.13**, retrieved September 2026. Units are feet.

> Framing note for the tool: § 73.13(a) says these are minimums and "**[i]f
> conditions warrant, greater isolation distances may be required**." The tool
> must present them as regulatory minimums a Sewage Enforcement Officer may
> increase, never as approvals.

### 6.1 § 73.13(b) — treatment tanks, dosing tanks, lift pump tanks, filter tanks, chlorine contact/storage tanks

| Feature | Distance |
|---|---|
| Property line, easement or right-of-way | 10 |
| Occupied buildings, swimming pools and driveways | 10 |
| An individual water supply or water supply system suction line | **50** |
| Water supply line under pressure | 10 |
| Streams, lakes or other surface waters | 25 |
| A cistern used as a water supply | 25 |

### 6.2 § 73.13(c) — perimeter of the aggregate in the ABSORPTION AREA

| Feature | Distance |
|---|---|
| Property line, easement or right-of-way | 10 |
| Occupied buildings, swimming pools and driveways | 10 |
| An individual water supply or water supply system suction line | **100** |
| Water supply line under pressure | 10 |
| Streams, water courses, lakes, ponds or other surface water | 50 |
| Other active onlot systems | 5 |
| Surface drainageways | 10 |
| **Mine subsidence areas, mine bore holes or sink holes** | **100** |
| Rock outcrop or identified shallow pinnacle | 10 |
| Natural or manmade slope greater than 25% | 10 |
| A cistern used as a water supply | 25 |
| Detention basins, retention basins and stormwater seepage beds | 10 |

**Statutory gloss to carry into the tool** `[V]`: "for the purposes of this
chapter **wetlands are not surface waters**." Do not apply the 50-ft surface
water buffer to mapped wetlands under this rule.

### 6.3 § 73.13(d) — wetted perimeter of a SPRAY FIELD

| Feature | Distance |
|---|---|
| Property lines, easements or rights of way | 25 |
| Occupied buildings and swimming pools | **100** |
| An individual water supply or water supply suction line | 100 |
| A cistern used as a water supply | 25 |
| Water supply line under pressure | 10 |
| Streams, watercourses, lakes, ponds or other surface waters | 50 |
| Mine subsidence, boreholes, sinkholes | 100 |
| Roads or driveways | 25 |
| Unoccupied buildings | 25 |
| Rock outcrop | 25 |

### 6.4 § 73.12 — site suitability (hard disqualifiers) `[V]`

A site is **unsuitable and the permit shall be denied** where:

- slope of the proposed absorption area or spray field is **greater than 25%**;
- the area is a mapped **floodway** — and "[w]here there is no flood mapping, a
  floodway extends **50 feet from the top of the stream bank**" (not applicable
  to spray fields);
- one or more **rock outcrops** exist within the proposed absorption area;
- in limestone areas, **depressions left by earlier sinkholes** exist wholly or
  partly within the area.

Also: absorption areas may not be placed in or on **fill unless the fill has
been in place ≥ 4 years**, and must be sited only in or on **undisturbed
soils** (§ 73.12(b), (c)).

### 6.5 Sizing numbers `[V]`

- **Design flow** (§ 73.16(a)): "a minimum flow of **400 gpd** for all dwellings
  having three bedrooms or less… increased by **100 gpd for each bedroom over
  three**."
- **Absorption area** (§ 73.16(c), Table A): square feet of aggregate per gpd by
  average percolation rate. Perc **faster than 3.0 min/inch is Unsuitable**;
  3–5 min/inch is unsuitable for conventional systems but **1.50 sq ft/gpd for
  elevated sand mounds**; 6–15 min/inch is 1.19 sq ft/gpd conventional. Only
  the **bottom of the aggregate area** counts (§ 73.16(b)(1)).
- **Septic tank** (§ 73.62): "The minimum liquid septic tank capacity for any
  installation is **900 gallons**," sized from the same 400 gpd / +100 per
  bedroom basis.
- **Holding tank**: minimum **1,000 gallons** or three days' waste, whichever is
  larger.
- **Spray irrigation storage**: **2,000 gallons** for a three-bedroom dwelling,
  **+500 gallons** per additional bedroom.

### 6.6 Do NOT encode

- Any well **construction** standard — see § 8, open question.
- Building setbacks from lot lines: these are **zoning**, set by each of ~2,560
  municipalities, and have no statewide value.
- Frost depth and ground snow load: determined by the local code official under
  § 403.103(d). No statewide table verified.

---

## 7. DELIBERATELY NOT PRINTED

| Item | Why |
|---|---|
| Permit fee dollar figures | § 401.2a sets **no state maximum** and every municipality and agency sets its own. Any number is a guess. The kit tells the reader fee schedules are public by right and to compare. |
| Third-party agency fee ranges | Same, plus it is a competitive private market. |
| An NEC edition year | Pennsylvania adopts none. Printing "2020 NEC" would be a fabricated citation. |
| Projected 2024 I-Code effective date | Comment period still open October 2026; the 2021 cycle overran its statutory clock by ~5 months. |
| County-by-county climate zone map | § 403.103(d) gives that determination to the code official. |
| Frost depth / ground snow load tables | Not verified to any statewide authority. |
| Named third-party agencies | L&I's list carries its own caveat that entries are voluntarily supplied and may be out of date; naming firms would be an implied endorsement. The kit points at the list. |
| Mine subsidence acreage | See open questions — the widely repeated figure is facially impossible and DEP's own number could not be retrieved. |
| Phone numbers | House rule. The L&I table does carry BCO phone numbers; the kit points at the table instead. |
| Statutory-employer / workers' comp specifics | Pending licensing research at time of writing; not asserted without the statute in hand. |

---

## 8. OPEN QUESTIONS

1. **Mine subsidence acreage.** The published state guide claims "roughly 27
   million acres of undermined land." Pennsylvania's **total land area is
   about 28.6–28.8 million acres**, so the claim implies ~94% of the
   Commonwealth is undermined, which is facially false. DEP's Mine Subsidence
   Insurance pages could not be retrieved in this session (pa.gov redesign;
   legacy dep.pa.gov paths redirect to a landing page). **Action: source
   DEP's own figure before the guide is corrected; do not substitute a
   remembered number.**
2. **Current MSI premium and coverage limits.** Guide claims "$50/year for
   $50,000." Unverified.
3. ~~DEP on-lot sewage program URL~~ — **RESOLVED**, see § 11.
4. ~~PennDOT HOP page and form number~~ — **RESOLVED**, see § 11.
5. ~~DCED Municipal Statistics~~ — **RESOLVED, and the common URL is dead.**
   `munstats.pa.gov` **no longer resolves** (DNS failure, independently
   confirmed twice). The live host is **`apps.dced.pa.gov`**. Never print
   `munstats.pa.gov`.
6. **Private water well construction standards** — the hypothesis is that
   Pennsylvania has none statewide. Not independently confirmed here; the
   sewage/wells research agent did not return before the kit was built. PA.4
   therefore handles wells by telling the reader to ask the municipality
   whether a well ordinance exists and to specify construction terms in the
   driller's contract — which is correct whether or not a statewide standard
   exists, and asserts nothing unverified.
7. **Mechanics' liens and workers' compensation.** The licensing research
   agent did not return before the build. PA.5 therefore names lien waivers,
   certificates of insurance and workers' compensation evidence as documents
   to collect, with **no day counts, dollar thresholds or statutory-employer
   claims** — and tells the reader to confirm lien-waiver requirements with a
   Pennsylvania attorney. Nothing unverified was printed. **A future revision
   should add 49 P.S. § 1101 et seq. (Mechanics' Lien Law of 1963) detail and
   77 P.S. statutory-employer exposure once verified.**
7. **Whether R314.4's exclusion removes smoke-alarm interconnection for NEW
   dwellings** or only for alterations. § 403.21(a)(7)(iii)(B) excludes the
   section generally while (a)(7)(i) addresses alterations specifically. The
   kit states both and tells the reader to confirm with the official rather
   than resolving it.
8. **Philadelphia** as a city of the first class runs its own regime; the kit
   flags the 10-business-day CO clock and points readers to L&I of
   Philadelphia rather than attempting to document it.

---

## 9. KIT REVISION WATCH — PENNSYLVANIA TRIPWIRES

Add to `project-kit-revision-watch`:

1. **2024 I-Code cycle.** RAC comment period reopened through **4 October
   2026**. When the RAC report is adopted, § 403.21 changes wholesale and PA.2
   needs rebuilding. Watch the RAC page and the Pennsylvania Bulletin.
2. **The opt-out table changes continuously.** `uccmun.htm` carried a
   `Last-Modified` of the retrieval date. The 119/2,444 split will drift; the
   kit prints it with a retrieval date for this reason.
3. **L&I's UCC home page said "2018" while the regulation said 2021.** If L&I
   later corrects the page, the kit's warning should be softened or dropped.
4. **Act 45 amendments.** Five 2025 House bills to amend the act were listed
   on the act's page. None verified as enacted; watch for changes to
   § 7210.304 in particular, which is where the wall-bracing and floor-membrane
   rules live.
5. **Chapter 405 (elevators)** final regulation effective 20 December 2026 —
   irrelevant to houses, but evidence Title 34 is in motion.

---

## 10. LATE ADDENDUM

*Reserved for reversals discovered after the kit build. Nothing to date.*

---

## 11. VERIFIED URL SET (September 2026)

Every address below returned HTTP 200 when fetched. `pa.gov` and
`legis.state.pa.us` require a browser User-Agent.

### The two that matter most

| What | URL |
|---|---|
| ★ **L&I municipal UCC elections table** (opt-in/opt-out, by county, with the BCO named) | `https://www.pa.gov/content/dam/copapwp-pagov/en/dli/documents/individuals/labor-management-relations/bois/documents/uccmun.htm` |
| ★ **DCED Find Your Municipality** (address → municipality) | `https://apps.dced.pa.gov/Munstats-Public/FindMunicipality.aspx` |

> ⚠ `munstats.pa.gov` is **dead** (DNS failure). The live host is
> `apps.dced.pa.gov`. DCED's own caveat: "the geo-coding system used for
> address searches on this website is outside the control of DCED" — confirm
> rural and boundary-adjacent parcels with the county.

### Labor & Industry

| What | URL |
|---|---|
| UCC program home | `https://www.pa.gov/agencies/dli/programs-services/labor-management-relations/bureau-of-occupational-and-industrial-safety/uniform-construction-code-home` |
| Certified third-party agencies (buildings) | `.../bureau-of-occupational-and-industrial-safety/tpa-buildings` |
| Certified code officials search | `.../uniform-construction-code-home/certified-code-officials` |
| Contractor licensing statement | `.../uniform-construction-code-home/contractor-licensing` |
| UCC Review and Advisory Council (2024 cycle) | `.../uniform-construction-code-home/ucc-review-and-advisory-council` |

Agency-list markings: **R** = full residential approvals (what an
owner-builder needs), **C** = non-residential. L&I's caveat, worth quoting:
listings "are based on information voluntarily provided to the Department and
may not accurately reflect an agency's current complement."

### Sewage, wells, radon

| What | URL |
|---|---|
| DEP Act 537 Sewage Facilities Program (hub) | `https://www.pa.gov/agencies/dep/programs-and-services/water/clean-water/wastewater-management/act-537-sewage-facilities-program` |
| Sewage facilities planning (module component forms) | `.../act-537-sewage-facilities-program/sewage-facilities-planning` |
| ★ **Active SEOs by county** (live report) | `https://pacleanwateracademy.remote-learner.net/blocks/bcwseo/seoreport.php` |
| Homeowner: septic systems | `https://www.pa.gov/agencies/dep/residents/my-water/septic-systems` |
| Homeowner: private wells | `https://www.pa.gov/agencies/dep/residents/my-water/private-wells` |
| DEP eLibrary (forms live here) | `https://greenport.pa.gov/elibrary/` |
| DEP Permit Navigator | `https://www.ahs.dep.pa.gov/PermitNavigator/` |
| DEP radon division | `https://www.pa.gov/agencies/dep/programs-and-services/radiation-protection/radon-division` |

**Who issues the septic permit:** the **local agency** (normally the
township or borough) through its SEO — not DEP. 25 Pa. Code §§ 72.21(a),
72.24(a): application "shall be made by the owner… **to the local agency, on a
form provided by the Department**."

### Everything else

| What | URL |
|---|---|
| PennDOT Highway Occupancy Permit (apply) | `https://www.pa.gov/services/penndot/apply-for-a-penndot-highway-occupancy-permit` |
| PennDOT ePermitting (EPS) | `https://epermitting.penndot.pa.gov/EPS/home/home.jsp` |
| County conservation districts directory | `https://pacd.org/` |
| PA One Call | `https://www.pa1call.org/` |
| HICPA contractor search | `https://hicsearch.attorneygeneral.gov/` |
| HICPA registration | `https://www.attorneygeneral.gov/businesses-and-organizations/home-improvement-contractor-registration/` |
| Pa. Code (regulations) | `https://www.pacodeandbulletin.gov/` |
| Statutes | `https://www.legis.state.pa.us/` (redirects to `palegis.us`) |
| FEMA Flood Map Service Center | `https://msc.fema.gov/portal/home` |

**PennDOT driveway forms** `[V]`, DEP/PennDOT's own wording: "Form **M-950A**
… can be used to apply for a **minimum use driveway** permit. A minimum use
driveway is a residential or other driveway that is expected to be used by no
more than 25 vehicles per day… Form **M-945A** … can be used to apply for all
other types of HOPs." **An owner-builder is normally on the M-950A track.**

### Chapter TOC trick for future revisions

`pacodeandbulletin.gov` chapter-TOC URLs return the **entire chapter text**:

```
https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/034/chapter403/chap403toc.html
https://www.pacodeandbulletin.gov/Display/pacode?file=/secure/pacode/data/025/chapter73/chap73toc.html
```

Statutes, with a browser User-Agent:

```
https://www.legis.state.pa.us/WU01/LI/LI/US/HTM/1999/0/0045..HTM   (Act 45 of 1999, UCC)
https://www.legis.state.pa.us/WU01/LI/LI/US/HTM/2008/0/0132..HTM   (Act 132 of 2008, HICPA)
```
