# Tennessee Owner-Builder Dossier — research for the TN Permit Kit (six documents)

Compiled September 2026 for kit 19 of the 50-state program. Every claim below is
tagged **[V]** (verified against a primary source, quoted) or **[H]** (hypothesis,
secondary source, or could not be verified). The kit prints only [V] material as
fact; [H] material is either printed with an explicit hedge or not printed at all.

Primary sources used throughout:
- **publications.tnsosfiles.com** — the Secretary of State's official compilation
  of rules, served as dated PDFs. This is the authoritative source for every rule
  chapter cited here. *Note: it returns HTTP 403 to curl without a browser
  User-Agent; set one when re-verifying.*
- **tn.gov/commerce/fire** — the State Fire Marshal's Office program pages.
- Tennessee Code Annotated, published under contract by LexisNexis.

---

## WARNING FOR FUTURE EDITORS — FIVE MINEFIELDS

1. **The opt-out is not permanent, and almost every guide on the internet says
   or implies it is.** A jurisdiction's opt-out resolution *expires 180 days
   after that legislative body's next election*. If the new body does not
   re-pass it, the State Fire Marshal resumes enforcement automatically. This is
   the single most under-reported fact about Tennessee residential code. It also
   means the jurisdiction list structurally churns — see minefield 5.

2. **The enforcement unit is the JURISDICTION, not the county.** A county
   resolution reaches only the unincorporated area — that limitation is on the
   face of the statute. Grundy County is OPT OUT; Monteagle, inside it, is
   EXEMPT. Franklin County is OPT OUT and *all seven* of its listed
   municipalities are EXEMPT. A county-level answer will be wrong for anyone
   inside a city.

3. **Opting out of the building code does NOT end the electrical permit.** The
   two programs rest on different chapters — Title 68 Chapter 120 for building,
   Title 68 Chapter 102 for electrical — and the opt-out statute is textually
   limited to the building standards. Verified empirically: zero overlap between
   the 37 residential opt-out counties and the electrical exempt list.

4. **Tennessee is on the 2017 NEC and the 2018 IRC**, both older than builders
   assume, and the energy provisions are amended back to *2009* tables. Do not
   write 2020/2023 NEC or 2018 IECC envelope numbers into this kit.

5. **The jurisdiction list is a living document with a printed currency date.**
   Re-pull it before every kit revision. A stale list is the most likely defect
   in this product.

---

## THE STRUCTURAL HEADLINE (the kit's thesis) — ONE CODE, THREE REGIMES, AND AN EXPIRY DATE

Tennessee adopts one state residential building code and then hands each
jurisdiction three ways to answer for it. The State Fire Marshal's Office
publishes the answer for every one of the state's 95 counties and 378
municipalities and tags each with one of three labels. [V]

Official legend, verbatim from the SFMO jurisdictions page:

> "Key
> **SRBP** - The jurisdiction will participate in the State Residential Building Program
> **EXEMPT** - The jurisdiction has received an exemption
> **OPT OUT** - The jurisdiction has passed a resolution opting out of the program"

| Status | What it means for a buyer | Counties | Municipalities |
|---|---|---|---|
| **EXEMPT** | Local building department enforces its own adopted code | 50 | 250 |
| **SRBP** | SFMO enforces; state permit, state contract inspectors | 8 | 79 |
| **OPT OUT** | **No residential building code enforcement at all** | 37 | 49 |
| | | **95** | **378** |

All 95 counties are accounted for, so the list is complete at county level. [V]

**Source:** https://www.tn.gov/commerce/fire/residential-permits/jurisdictions-inspectors.html
— page states its own currency: "This information is accurate as of 8/21/2026."
Accessed 2 September 2026, i.e. 12 days old at time of research. [V]

**INDEPENDENTLY RE-VERIFIED** by parsing the live page's HTML table directly
during kit assembly: 474 rows including the header, **95 county rows breaking
exactly 50 EXEMPT / 37 OPT OUT / 8 SRBP**. The counts above are confirmed. [V]

**Do not reproduce this table in the kit.** It carries inspector names, email
addresses and **phone numbers**, and the kit prints no phone numbers anywhere.
Print the county-level counts, the method, and the URL.

### ⚠ TWO OFFICIAL SFMO PAGES DISAGREE — VERIFIED, AND IT IS KIT CONTENT [V]

The SFMO publishes the SRBP county list in two places and they do not match:

| Page | SRBP counties listed |
|---|---|
| `residential-permits/jurisdictions-inspectors.html` (dated 8/21/2026) | **8** — Campbell, Chester, Giles, Hardeman, Hawkins, Lauderdale, Meigs, Smith |
| `residential-permits/fire-apply-for-a-residential-permit.html` (undated) | **7** — Chester, Giles, Hardeman, Hawkins, Lauderdale, Meigs, Smith |

**Campbell County is the difference.** It appears on the dated jurisdictions page
as SRBP *with a named assigned inspector*, and is absent from the apply page's
list entirely. Both pages were fetched and parsed directly on 2 September 2026.

**Resolution for the kit:** treat the dated `jurisdictions-inspectors` page as
authoritative — it carries a currency date, it is per-jurisdiction, and it names
the inspector. But *tell the buyer the two pages disagree*, because a Campbell
County owner reading the apply page would conclude no state permit exists for
them. The correct instruction is: check the dated list, then confirm with the
office before relying on it. This discrepancy is exactly the kind of thing the
kit exists to surface.

### The enabling statute and the opt-out mechanism

**Tenn. Code Ann. § 68-120-101**; implementing rules at **Chapter 0780-02-23**,
"One and Two Family Dwellings and Townhouses," effective **25 February 2024**. [V]

Key operative text (see SOURCING CAVEAT below):

> **(b)(1)(B)(i)** …the standards established pursuant to subsection (a) relative
> to one-family and two-family dwellings do not apply in any county or
> municipality in which the legislative body … **by a two-thirds (2/3) vote,
> adopts a resolution to exempt** the county or municipality … **provided,
> however, that any action by the county legislative body … shall be limited to
> the jurisdictional boundaries outside any municipality located within the
> county.**
>
> **(ii)(b)** A resolution … **shall expire one hundred eighty (180) days
> following the date of the election for the local legislative body next
> occurring following the adoption of the resolution**, but an earlier
> expiration date may be stated in the resolution.
>
> **(D)** …**the owner of a building … located in a county or municipality that
> has taken action pursuant to subdivision (b)(1)(B) may request that the state
> fire marshal inspect** the building … and … **the state fire marshal must
> issue documentation to the owner evidencing such.**

**SOURCING CAVEAT [V-secondary]:** the verbatim statutory transcription came from
FindLaw, not the official LexisNexis publication — the official publisher
redirects into an `advance.lexis.com` container that resisted scraping and Justia
returned an empty body. **Every operative element** (two-thirds vote, resolution
rather than referendum, 180-day post-election expiry, reversal, and the
(b)(1)(D) owner-requested inspection) **is independently corroborated by primary
SFMO pages and by the SFMO's own rules.** Confirm the block quote against the
official code before any future revision.

Independent primary corroboration, SFMO Residential Permit FAQs (page last
modified 25 February 2026), verbatim:

> "A city or county may opt out at any time. The law allows a city or county to
> opt out through the passage, **by a two-thirds vote, of a resolution** to
> exempt the city or county. **The opt out resolution expires 180 days following
> the date of the election for the city or county's legislative body.** If the
> subsequent legislative body does not vote to opt out prior to the expiration of
> the opt out resolution, **the SFMO will begin to enforce the residential
> building code requirements**…"

### The rule-level proof of the sunset

Rule **0780-02-23-.14**, verbatim — what a jurisdiction must file to opt out: [V]

> "Any local government opting out … shall submit to the Division the following:
> (1) A certified copy of the resolution opting out of these provisions;
> **(2) The date of the next election for the legislative body;** and
> (3) The name and mailing address of the person responsible by law for
> recordkeeping…"

Item (2) exists precisely *because* the opt-out expires. This is the rule-level
confirmation of the sunset, from a primary source. [V]

### Answers to the mechanism questions

| Question | Answer | Tag |
|---|---|---|
| Who votes? | County legislative body (unincorporated area only) or municipal legislative body | [V] |
| What majority? | **Two-thirds** | [V] |
| Referendum required? | **No** — a resolution suffices | [V] |
| Deadline to opt out? | **None** — "at any time" | [V] |
| Does it expire? | **Yes** — 180 days after that body's next election | [V] |
| Can they opt back in? | Yes, by resolution under (b)(1)(C); no supermajority stated for reversal | [V-secondary] |
| Townhouses in scope? | **UNRESOLVED — see open questions** | [H] |
| Additions? | Additions of 30+ sq ft of interior space are inside the program | [V] |

---

## CODE EDITIONS IN FORCE [V]

| Code | Edition | Rule chapter |
|---|---|---|
| Residential (IRC) | **2018 IRC + Appendix Q** | 0780-02-23-.02(1)(a) |
| Residential energy | **2018 IECC / IRC Ch. 11, amended back to 2009 tables** | 0780-02-23-.02(1)(b) |
| **Electrical (NEC)** | **2017 NEC**, effective 1 October 2018 | **0780-02-01**-.02(1) |

### THE ELECTRICAL TRAP — verbatim [V]

Rule 0780-02-01-.02(1), current version effective **14 July 2025** — so this is
not a stale document; the state simply has not moved off the 2017 NEC:

> "…shall be those prescribed in the **National Electrical Code, 2017 edition**,
> published by the National Fire Protection Association… **effective October 1,
> 2018**, except that:
> (a) Section 110.24, Available Fault Current shall be optional; and
> (b) **Arc Fault Circuit Interrupters (AFCIs) shall be optional for bathrooms,
> laundry areas, garages, unfinished basements**… and **for branch circuits
> dedicated to supplying refrigeration equipment**."

Corroborated by the SFMO electrical program page: "This section is responsible
for enforcing the provisions of the **2017 edition of the National Electric
Code**…" [V]

### Residential IRC amendments worth printing [V]

From rule 0780-02-23-.02(1)(a), verbatim list:
1. **R313 automatic fire sprinklers NOT mandatory**, per T.C.A. § 68-120-101(a)(8).
2. **Chapters 34–43 (electrical) deleted**; 0780-02-01 applies instead.
3. Figure R301.2(2) Seismic Design Categories replaced with the **2015 IRC**
   Site Class D figure. (Relevant — West Tennessee sits on the New Madrid zone.)
4. R314.6 smoke alarm power source amended to add Exception 3.
5. **Air-leakage testing replaced with the 2009 IRC Testing Option / Visual
   Inspection pair** — i.e. a choice, not a mandatory blower door.
6. **Duct testing and duct leakage are optional.**
7. **Insulation and fenestration tables replaced with the 2009 IRC tables.**
8. R402.4.4 Rooms Containing Fuel-Burning Appliances **deleted entirely**.

Also: smoke alarms "shall be no more than ten (10) years old from the date of
manufacture," and battery-only devices must use a 10-year sealed battery
(rule .15(3)). Appendix Q (tiny houses) **is** adopted. [V]

### THE ENERGY HEADLINE — no mandatory blower door [V]

Tennessee adopts the 2018 IECC/2018 IRC Ch. 11 on paper and then amends the
envelope and testing provisions back to 2009. Consequences:

1. The 2018 IECC's mandatory whole-house air leakage test **does not apply**. The
   2009 structure offers a **choice** of a testing option *or* a visual
   inspection option against a checklist.
2. **Duct testing is optional**, both the mandatory and prescriptive provisions.
3. The R-value / U-factor tables are the **2009** tables — meaningfully less
   demanding than 2018. Do not print 2018 IECC R-values in a Tennessee kit.
4. **No separate energy inspection** — rule .07(2)(c): "Energy efficiency
   inspections shall occur during the required inspections."
5. Path choice confirmed by SFMO FAQ: compliance may be met "through meeting the
   standards of **either Chapter 11 of the 2018 IRC or the 2018 edition of the
   International Energy Conservation Code**."

**Reverse error to avoid:** this analysis governs SRBP areas. An EXEMPT
jurisdiction is on *its own* adopted code, which may be newer and may require a
blower door. The kit must say so.

### The commercial chapter is a different rule — do not confuse them [V]

Chapter **0780-02-02** ("Codes and Standards", effective 17 April 2025) adopts
2021 editions of the IBC, IFGC, IMC, IPC, IPMC, IFC, IECC-commercial and IEBC.
**These do not govern a one- or two-family dwelling.** For a house under the
state program, plumbing / mechanical / fuel gas come from the **2018 IRC's own
chapters**, because 0780-02-23 adopts the 2018 IRC whole except Chapters 34–43.
Do not tell a homeowner they are building to the 2021 IPC. NFPA 101 is no longer
adopted at all.

---

## THE STATE RESIDENTIAL BUILDING PROGRAM (SRBP) — MECHANICS

Permits are bought through **CORE** (Comprehensive Online Regulatory and
Enforcement System) at **core.tn.gov**, or in person from a contracted Issuing
Agent, who "shall receive no more than fifteen dollars ($15.00) for each issued
permit," remitted *from* (not added to) the fee — rule .05(1). [V]

Inspections are "conducted by **deputy building inspectors appointed under
contract** with the Commissioner" (rule .07(1)). The SFMO runs 15 full-time state
inspectors and roughly 100 contracted Deputy Electrical and Deputy Building
Inspectors. **The jurisdictions page names the specific assigned inspector for
each county** — unusual and valuable. [V]

### Application contents — rule 0780-02-23-.05(4), verbatim [V]

> "(a) …an applicant shall complete a form prescribed by the Department
> containing at least the following information: 1. The location…; 2. A
> description of the work…; 3. The use and occupancy…; 4. The valuation of the
> project; 5. The square footage…; 6. The signature of the applicant; and 7. If
> applicable, a copy of the form issued by the appropriate municipal or county
> official stating the estimated tax liability…
> (b) …an applicant shall present: 1. Payment…; and 2. Licensure pursuant to
> T.C.A. Title 62, Chapter 6 (**proof of licensure is not required for a property
> owner purchasing the permit when the property owner is performing the work**).
> (c) …an applicant shall certify and have proof available, if requested, of:
> 1. **Availability of public sewer or a septic permit**; and 2. Any license or
> permit required by state law or local ordinance."

**No form number is published.** The rule says only "a form prescribed by the
Department"; the real path is the CORE workflow. **Do not invent a form number.** [V]

### FEE SCHEDULE — rule 0780-02-23-.08(1), verbatim [V]

| Total Construction Cost | Fee |
|---|---|
| $0.00 to $5,000 | $100 |
| $5,001 to $100,000 | $350 |
| $100,001 to $150,000 | $400 |
| $150,001 to $200,000 | $450 |
| $200,001 to $250,000 | $500 |
| $250,001 to $300,000 | $550 |
| $300,001 AND UP | $550 for the first $300,000; plus $50.00 for each additional $50,000 above $300,000 or fraction thereof |

Add-ons, verbatim: plumbing and mechanical inspection **$100**; slab inspection
other than monolith pours **$100**; prefabricated wall inspection **$100**;
re-inspection necessitated by more than one rejection **$100**; consultation
inspection or temporary certificate of occupancy **$100**. Beginning work before
obtaining the permit: **an additional 100% of the required permit fee for each
violation**. Duplicate permit if lost: **$10**. [V]

**Minimum valuation — the number that decides most buyers' fee.** SFMO fees page
(last modified 25 March 2026), verbatim footnotes:

> "* The cost of construction cannot be less than **$60.57 per heated square
> foot** of construction"
> "** An HVAC and Plumbing Inspection is required for all new construction"
> "*** Slab other than Monolith Pour Inspection is required when slab and footing
> are cast separately"

**FLAG:** $60.57/sq ft is a *website* figure, not a rule figure — the rule instead
says valuation shall not be less than ICC Building Valuation Data at a 0.60 cost
modifier. Reconcilable but not identical, and the website number will drift.
Date-stamp it in the kit. [V as of 25 March 2026]

Worked example: a 2,000 sq ft heated house → minimum valuation 2,000 × $60.57 =
**$121,140** → $100,001–$150,000 band → **$400** base + **$100** plumbing and
mechanical = **$500**, plus $100 more if the slab is a separate pour.

### Permit validity [V]

- Void if work not commenced within **180 days**; void if suspended or abandoned
  180 days; extensions of up to 180 days each on written request (rule .05(7)(a)).
- Expires **two years** from issue, or on issuance of the CO (rule .05(7)(b)).
- **Homeowner permit: one property owner's permit per 24 months** (rule .05(3),
  citing T.C.A. § 62-6-103).
- Permits are non-transferable; a change of contractor mid-build requires a **new
  permit**.

---

## INSPECTIONS [V]

Rule 0780-02-23-.07(2)(a), verbatim and in required order: foundations (monolith
slabs inspected as the footing); plumbing and mechanical before concealment;
frame; attached garages; prefabricated walls; fire renovations; final before
occupancy. Plus a **separate slab inspection** when not a monolith pour
(.07(2)(b)), and energy inspections folded into the others (.07(2)(c)).

Rule .07(4): "Inspections shall be conducted **in the order set out in paragraph
(2)**… Work shall not be done beyond the point indicated in each successive
inspection without first obtaining approval." [V]

**Practical count (SFMO FAQ):** "Three inspections will be required: the
foundation prior to pour, the rough-in/framing, and at final construction," plus
a fourth if the slab is a separate pour, plus plumbing and mechanical. [V]

### THE INSULATION TRAP — the highest-value scheduling item [V]

SFMO FAQ, verbatim: "**If batt or roll wall insulation is used, it must be in
place prior to requesting an inspection.** If a plastic vapor barrier is used, it
should be installed after the inspection. **If loose-fill or spray applied
insulation is used, the request should be made before it is installed**" — with a
manufacturer's product data sheet and installation certificate required.

Same inspection, opposite instructions depending on which product was bought.

### Turnaround, waiver, re-inspection [V]

- "**within three working days** of when the request is made… **except for footer
  inspections which are to be performed within one working day**."
- Any inspection may be waived on a letter from an **architect or engineer
  currently registered with the State of Tennessee** (rule .07(5)).
- **One free re-inspection per permit**; $100 for each one after.
- The **permit holder** books it — "Subcontractors should not schedule an
  inspection."

### Certificate of occupancy — rule .09 [V]

> "(1) A new one (1) or two (2) family dwelling, townhouse… **shall not be
> occupied until the Division has issued a certificate of occupancy.**
> (2) A certificate of occupancy shall be issued after the passage of all
> inspections required by this chapter **and passage of the final electrical
> inspection**."

---

## THE ELECTRICAL PROGRAM — AND THE KIT'S SECOND THESIS

### DOES THE ELECTRICAL PERMIT SURVIVE A BUILDING-CODE OPT-OUT? YES. [V]

Verifiable three ways:

1. **Textual.** § 68-120-101(b)(1)(B)(i) exempts a jurisdiction from "the
   standards established pursuant to **subsection (a)**" — the building
   construction safety standards. It does not reach Title 68 Chapter 102.
2. **Structural.** Rule 0780-02-01 contains no opt-out mechanism at all, and
   rule .17 forbids weakening it: "No city, county, town, municipal corporation,
   metropolitan government or political subdivision of this state shall adopt or
   enforce any ordinance prescribing **less stringent electrical standards** than
   those established hereunder…"
3. **Empirical.** Cross-checking the SFMO's Electrical Exempt Jurisdictions list
   against the 37 residential OPT OUT counties returns **zero overlap**. The only
   whole counties exempt from the state electrical program are **Hamilton** and
   **Shelby**, both of which are residentially EXEMPT, not opt-out.

**So in all 37 "no building code" counties a homeowner still buys a state
electrical permit and still receives state electrical inspections.** This is the
thing owner-builders in those counties get wrong most often.

SFMO states the separation plainly (Residential FAQ, verbatim): "The state
residential building permit is a building permit only. It is not: Grading or fill
approval / Determination of flood plain compliance / A septic or sewer permit; or
**An electrical permit** / Zoning approval." [V]

### Electrical mechanics [V]

- Rule .05(1): permit from "the **power distributor, local building official,
  Commissioner, or designee, or other issuing agent**…" Issuing agents may charge
  no more than **$5.00**, in addition to inspection fees.
- Rule .05(2)(a): "Any person may perform electrical work (for which an
  inspection is required) upon his/her own residence provided he/she first
  applies for and obtains a **residential property owner's electrical permit**."
  Extends to the applicant and immediate family; no unlicensed helpers.
  **One per 12-month period** — a *different clock* from the building permit's 24.
- Rule .05(6): an electrical **rejection requires buying a new permit** (unlike
  the building permit's one free re-inspection).
- Rule .04(10): no final electrical certificate "**if a building permit has not
  been obtained, if required**… or all inspections have not been performed."
- Rule .04(11): "electrical power shall be supplied to the building in order for
  the inspector to perform the final inspection."

### ELECTRICAL FEE SCHEDULE — rule 0780-02-01-.21, verbatim ceilings [V]

Final: 0–200 A **$35**; 201–400 A **$40**; 401–600 A **$50**; 601–1000 A **$90**;
1,001 A and above negotiable. Rough-in: **$35** at any capacity. Re-inspection:
**$35**. Dwelling unit heating/cooling system: **$35**. Consultation: **$50**.
Service release inspection (valid 45 days): based on capacity. Floating cabins:
**$150**.

Typical 200 A house: **$35 rough-in + $35 final = $70**, plus $35 if HVAC is
inspected, plus up to $5 issuing-agent fee per permit.

### Electrical exempt jurisdictions — NOT in the state program [V]

SFMO page last modified 22 May 2026. Each city entry qualified "(inside city
limits)":

- **East:** Athens, Bristol, Cleveland (incl. all of Cleveland Utilities
  district), Elizabethton, **all of Hamilton County** (incl. Chattanooga,
  Collegedale, East Ridge, Lakesite, Lookout Mountain, Signal Mountain, Soddy
  Daisy), Johnson City, Kingsport, Knoxville, Maryville, Morristown, Oak Ridge
- **Middle:** Clarksville, Cookeville, Franklin, Gallatin, Hendersonville,
  McMinnville, Mt. Juliet, Murfreesboro, Nashville/Davidson Co/Metro, Smyrna,
  Spring Hill
- **West:** Jackson, **all of Shelby County** (incl. Arlington, Bartlett,
  Collierville, Germantown, Lakeland, Memphis, Millington, Oakland)

### Public Chapter 177 (2021) — solar / generation interconnect [V]

If the build includes solar or any equipment delivering power to the grid: state
certified electrical inspector, lockable exterior load-breaking disconnect (or
approved alternative), utility notification before interconnection, and final
inspection at commissioning — only a service release is issued before then. Rapid
shutdown must be functional before final.

---

## WHAT SURVIVES AN OPT-OUT [V unless noted]

| Requirement | Survives? | Authority | Tag |
|---|---|---|---|
| State electrical permit + inspections | **YES** — zero overlap with the electrical exempt list | 0780-02-01; T.C.A. §§ 68-102-113/143/150 | **[V]** |
| Septic permit (TDEC) | **YES** — independent; the state building rule even requires proof of "public sewer or a septic permit" | 0400-48-01 | **[V]** |
| Voluntary SFMO inspection + CO on request | **YES** | § 68-120-101(b)(1)(D) | **[V]** |
| Local zoning / land use | **YES** — a code opt-out is not a zoning opt-out | SFMO FAQ | [V] separate; [H] on local content |
| Floodplain / NFIP | **YES** — separate local commitment | SFMO FAQ | [V] separate; **[H]** that every opt-out county participates |
| Contractor licensing | **YES** — statewide, independent of local code adoption | T.C.A. Title 62 Ch. 6 | **[V]** |
| E-911 addressing | Almost certainly | — | **[H] — NOT VERIFIED** |

**The single most useful sentence for a buyer in an opt-out county:** you do not
need a building permit, but you *do* need a state electrical permit, you *do* need
a septic permit if you are not on sewer, and you *can* voluntarily buy a state
building permit and get inspections and a CO. SFMO gives the commercial reason
(verbatim):

> "In addition, owners of one- or two-family dwellings **may now be able to access
> lenders and loan programs previously unavailable to them because those lenders
> or loan programs required a CO**."

---

## LICENSING AND THE OWNER-BUILDER EXEMPTION

### ⚠ SOURCING LIMITATION — READ BEFORE EDITING TN.1

**Tennessee does not publish its own code in machine-readable form.** The
official Tennessee Code Unannotated is hosted by LexisNexis behind a JavaScript
redirect and session-cookie wall; Justia, FindLaw, Casetext, public.law and the
Wayback Machine were all bot-blocked from the research environment.

Every § 62-6-xxx sentence quoted in the kit therefore comes from **published
Tennessee appellate opinions that quote the statute verbatim** (retrieved as the
courts' own PDFs), and every headline number is independently corroborated by
**2024–2026 agency documents** — the Board's rules revised 18 November 2025, the
SFMO rules revised 25 February 2024, and the SFMO's current FAQs.

**Consequence: the substance is solid; the subdivision numbering is not.** The
same exemption is cited as § 62-6-103(2)(A), § 62-6-103(a)(2)(A) and
§ 62-6-103(a)(2)(A & B) across different opinions. **The kit therefore cites at
SECTION level and quotes the sentence.** Do not add pinpoint subdivisions
without checking Lexis. An attempt to build an amendment check failed: the
General Assembly's bill search indexes captions, not TCA section numbers
("62-6-103" returns zero hits in every General Assembly from the 106th to the
114th while "contractor" returns hits).

### The threshold, and Tennessee's unusual bite [V-court + V-agency]

**Tenn. Code Ann. § 62-6-102** defines "contractor" to reach anyone who
"**undertakes to, attempts to or submits a price or bid or offers to** construct
… for which the total cost is **twenty-five thousand dollars ($25,000) or
more**." The license is required **to bid**, not merely to perform. Board rule
0680-01-.18 (unlawful bidding) backs it: an unlicensed bidder "shall [not] be
awarded any contract for the project … or [be] permitted to participate in any
re-bidding of the project."

Cost is measured **all-in**: rule 0680-01-.13(8) — "including all material and
labor furnished by or through another source other than the owner."

**§ 62-6-102 also defines a "prime contractor" as "one who contracts directly
with the owner."** That definition is the hinge of the whole kit.

| Rung | Threshold | Cite |
|---|---|---|
| Contractor's license (GC; and electrical, mechanical, plumbing, roofing subs) | **$25,000+** | § 62-6-102, § 62-6-103 |
| Masonry subcontractor | **$100,000+** | Rule 0680-01-.24(1) |
| Limited Licensed Electrician (LLE) | **under $25,000** | §§ 62-6-130 to -132 |
| Limited Licensed Plumber (LLP) | **under $25,000** | Title 62 Ch. 6 Part 4 |
| Home Improvement license (adopting counties only) | $3,000 to under $25,000 | §§ 62-6-501 et seq. |
| Limited Residential (BC-A/r) | projects to **$125,000** | Rule 0680-01-.29(1) |

**[H] correction to the research brief's premise:** the Home Improvement statute
does **not** appear to enumerate counties. Adoption is by county opt-in under
§ 62-6-516(b); TDCI publishes a nine-county list (Bradley, Davidson, Hamilton,
Haywood, Knox, Marion, Robertson, Rutherford, Shelby). Not printed in the kit.

### The exemption, verbatim [V-court]

> "[N]otwithstanding subdivision (a)(1), **any person, firm or church that owns
> property and constructs on the property single residences, farm buildings or
> other buildings for individual use, and not for resale, lease, rent or other
> similar purpose, is exempt from the requirements of this part.**"

Board rule **0680-01-.22**: "**Individual use shall mean use by persons other
than the general public.**" Board rule **0680-01-.26**: the exemption "does not
apply to construction pertaining to resale, lease, rent or other similar
purpose." [V]

### THE TWO-YEAR RULE — two mechanisms, and the kit prints both [V]

**Statutory (a rebuttable presumption):** there is a "rebuttable presumption that
the person or firm intends to construct for the purpose of resale, lease, rent or
any other similar purpose **if more than one (1) application is made for a permit
to construct a single residence or if more than one (1) single residence is
constructed within a period of two (2) years**."

Note it can be triggered by **applications**, not only finished houses. It shifts
the burden; it does not bar. In the leading case the owners rebutted it with
testimony — but they litigated for years to do it.

**At the permit counter (a hard bar):** rule 0780-02-23-.05(3) — "**an individual
may obtain only one (1) property owner's permit within a twenty-four (24) month
period.**" And rule .01(i) defines the permit as one for a dwelling "**in which
the owner intends to live upon completion**."

**Changing your mind mid-build:** a contractor is unlicensed for these purposes
if they do not hold a license "throughout the entire time contracting services
are performed," and the Court of Appeals has applied that to an owner-builder who
decided to sell part-way through. [V-court]

### Criminal exposure, and the carve-out that protects the owner [V-court]

Contracting unlicensed is a **Class A misdemeanor** (§ 62-6-120). But the penalty
"**shall not apply to a person who engages a contractor without a license for the
purpose of constructing a residence for the use of that person.**" The owner is
not the offender; the unlicensed contractor is. Separately, § 62-6-103(b) caps an
unlicensed contractor's recovery at "actual documented expenses … by clear and
convincing proof."

### THE PRIME TRAP — the kit's second thesis [V-agency]

TDCI's own licensing booklet: "Subcontractors: A contractor's license is NOT
required for all subcontractors, those bidding directly to a contractor and not
the owner … **Note: Bidding to a homeowner acting as their own GC makes you a
'Prime'.**"

Because § 62-6-102 defines a prime as one who contracts directly with the owner,
**an owner-builder converts every trade into a prime contractor** — so trades that
need no license under a professional builder need one at $25,000 when they bid to
you. And rule **0680-01-.27(3)** makes it misconduct for a licensed contractor to
pull a permit "for a job in which an unlicensed contractor is acting as the
general contractor," which closes the borrowed-license workaround. [V]

### Trades — what the owner may do [V unless noted]

- **Electrical: YES**, on a residential property owner's electrical permit
  (0780-02-01-.05(2)(a)) — **one per 12 months**, applicant and immediate family
  only, "shall not authorize assistance by any other person not duly licensed."
  Note the asymmetry with the building permit's 24 months.
- **Plumbing: YES.** TDCI's LLP application lists "Homeowner may perform plumbing
  on their own residence" among the § 62-6-406 exemptions. **[V-agency], not a
  statutory quote** — § 62-6-406's verbatim text could not be retrieved.
- **Mechanical / HVAC: UNRESOLVED [H].** No homeowner exemption text for
  mechanical work was found at all, and no below-$25,000 HVAC credential appears
  to exist (the Board licenses contractors, LLEs and LLPs, and nothing else).
  The kit reports the gap rather than filling it.

### Verifying a sub [V]

Rule 0680-01-.24(1) requires the sub to furnish "an active license with the
appropriate **name, classification, monetary limit, and expiration date**." Those
are the four fields. **verify.tn.gov** is the public license search;
**core.tn.gov** is the transactional permit system — different systems, widely
confused.

**The monetary limit is a free credit check.** Rule 0680-01-.13(1) sets it at the
**lesser of 10× net worth or 10× working capital**, so a $150,000 limit implies
roughly $15,000 of net worth or working capital. Limits from different
classifications **may not be combined** (.13(8)); tolerance is 10%, and none for
BC-A/r. **Caveat [V-agency]:** from 1 July 2026 the Board accepts a surety bond of
at least 50% of the requested limit instead of a CPA statement, so the inference
weakens for newer licenses. General liability floor is only **$100,000** for
limits up to $500,000 (rule 0680-06-.02(1)).

### Workers' compensation [V-agency + V-court]

Construction is the exception to the five-employee rule: businesses "in the
construction industry are required to have workers' compensation coverage for
everyone including the business owners." The **Exemption Registry** exempts the
business owner only — "Exempt owners are still required to have insurance
coverage for all of their employees, even if they have only one employee" — and a
registry filing can be disregarded where the filer is not genuinely a business
owner (a workers' comp court rejected one where "the only 'assets' … are [the
worker's] tools").

**[H] and flagged as such in the kit:** no Tennessee decision squarely holds
whether a residential owner-builder is a § 50-6-113 statutory employer. Case law
says an owner does not become a "contractor" merely by assuming GC
responsibilities, and the licensing definition requires "gain of whatever
nature" — but that is an inference across two titles. The kit's framing is
"collect the certificate anyway."

### Liens [V, 2007 enacted text]

**§ 66-11-146** is the owner-occupied carve-out and it cuts both ways:
- Hire a prime contractor → "a lien or right of lien upon such property **shall
  exist only in favor of a prime contractor**." Subs cannot lien your home.
- **Be** the prime → the lien exists "in favor of the prime contractor **and
  remote contractors in contractual privity with the prime contractor**." Your
  own trades **can** lien.
- Escape hatch: "**No lien … shall exist … from and after the date the prime
  contractor pays the remote contractor.**" Get waivers at every payment.

**§ 66-11-143 Notice of Completion:** recording it cuts unrecorded claimants to
**10 days** on a 1–4 family residence (30 elsewhere), and a notice recorded
**before** completion "is void and of no effect whatsoever."

**DELIBERATELY NOT PRINTED — § 66-11-145 Notice of Nonpayment.** As enacted in
2007 that section **excludes** one- to four-family residential, which is the
opposite of what most secondary sources say. Unresolved; the kit prints neither
version. Also not printed: "unlicensed contractors cannot lien," which appears
only in a demand letter quoted by a court, not in a holding.

---

## SEPTIC — TDEC, NOT THE HEALTH DEPARTMENT

**Primary source:** Rules of the Tennessee Department of Environment and
Conservation, Division of Water Resources, **Chapter 0400-48-01, "Regulations to
Govern Subsurface Sewage Disposal Systems."** Footer: "April, 2014 (Revised)."
Administrative history on every rule: *"Original rule filed June 20, 2013;
effective September 18, 2013. **Rule renumbered from 1200-01-06**."* [V]

**The renumbering IS the evidence of the transfer.** Chapter 1200 is the
Department of Health's rule series; 0400 is TDEC's. The same substantive
regulation that sat at 1200-01-06 now sits at 0400-48-01 under TDEC Division of
Water Resources. **Any guide that sends a Tennessee buyer to the county health
department for septic is working from pre-2013 sources.** [V]

Purpose, rule .01(1)(a), verbatim: "The purpose of these regulations is to provide
for the implementation of T.C.A. Title 68 Health, Safety and Environmental
Protection, Chapter 221 Water and Sewerage, Part 4 Subsurface Sewage Disposal
Systems." Authority: T.C.A. §§ 68-221-401 et seq. [V]

### Where you file [V]

Application form **CN-0971 (Rev. 04-25)**, "Application for Water Resources
Services," TDEC Division of Water Resources. Instruction 7, verbatim: "MAIL YOUR
APPLICATION AND FEE TO THE OFFICE ASSOCIATED WITH YOUR COUNTY SHOWN ON THE NEXT
PAGE."

Page 2 is the Environmental Field Office map. **Seven offices:** Jackson,
Nashville, Cookeville, Johnson City, Columbia, Chattanooga, Knoxville. (Map
revision stamp "Rev. 02/2025".)

### ⚠ SEVEN OR EIGHT FIELD OFFICES? BOTH, AND THE DIFFERENCE MATTERS [V]

TDEC's own field-office directory lists **eight** Environmental Field Offices —
the seven above **plus Memphis** (verified live on
`tn.gov/environment/contacts/field-offices.html`, 2 September 2026). But the
septic application form CN-0971 routes to only **seven**; Memphis is not on the
form's map.

The most likely explanation is that Shelby and its neighbors run septic through
a county health department rather than a TDEC field office, which is consistent
with the "Contract Counties" hatch on the same map — but **the chapter does not
say so and this is [H]**.

**Instruction for the kit, which is correct either way:** use the office map
printed on page 2 of the CN-0971 you are actually mailing, because that is the
map the form's own instruction points you to ("MAIL YOUR APPLICATION AND FEE TO
THE OFFICE ASSOCIATED WITH YOUR COUNTY SHOWN ON THE NEXT PAGE"). Do not print a
county-to-office table in the kit; print the instruction and the form number.

**Hardeman County is split and it is a genuine trap:** TDEC's directory assigns
its septic-related services to the **Jackson** office while Division of Water
Resources matters go through **Memphis**. [V from the TDEC directory]

### The eight offices and the counties each serves [V, from TDEC's directory]

Recorded here for reference; see the caveat above before printing any of it.

| Field Office | Counties served |
|---|---|
| Knoxville | Anderson, Blount, Campbell, Claiborne, Cocke, Grainger, Hamblen, Jefferson, Knox, Loudon, Monroe, Morgan, Roane, Scott, Sevier, Union |
| Chattanooga | Bledsoe, Bradley, Grundy, Hamilton, Marion, McMinn, Meigs, Polk, Rhea, Sequatchie |
| Johnson City | Carter, Greene, Hancock, Hawkins, Johnson, Sullivan, Unicoi, Washington |
| Nashville | Cheatham, Davidson, Dickson, Houston, Humphreys, Montgomery, Robertson, Rutherford, Stewart, Sumner, Trousdale, Williamson, Wilson |
| Columbia | Bedford, Coffee, Franklin, Giles, Hickman, Lawrence, Lewis, Lincoln, Marshall, Maury, Moore, Perry, Wayne |
| Cookeville | Cannon, Clay, Cumberland, DeKalb, Fentress, Jackson, Macon, Overton, Pickett, Putnam, Smith, Van Buren, Warren, White |
| Jackson | Benton, Carroll, Chester, Crockett, Decatur, Dyer, Gibson, Hardin, Haywood, Henderson, Henry, Lake, Lauderdale, Madison, McNairy, Obion, Weakley; **Hardeman (septic)** |
| Memphis | Fayette, Shelby, Tipton; **Hardeman (Division of Water Resources only)** |

Blount and Sevier counties run their own environmental health septic programs. [V]

### CONTRACT COUNTIES — nine, not the five everyone repeats [V]

Read directly off the CN-0971 (Rev. 04-25) page-2 map, rendered at 400 dpi and
inspected as an image. Contract counties carry a diagonal hatch fill and an
italic label; the legend key reads "*Contract Counties" with the matching swatch.

| Contract county | Division |
|---|---|
| Shelby | West |
| Madison | West |
| Davidson | Middle |
| Williamson | Middle |
| Hamilton | East |
| Knox | East |
| Blount | East |
| Sevier | East |
| Jefferson | East |

**The common street wisdom names Knox, Shelby, Hamilton, Davidson and Madison.
That is correct but INCOMPLETE — the current map adds Williamson, Blount, Sevier
and Jefferson. Anyone relying on the five-county version misroutes an
application in four counties.** [V]

**[H]** on the legal mechanism and on what "contract county" changes for the
applicant. The map proves the list; it does not say whether the county issues
under its own authority or issues TDEC's permit under contract, or whether the
fee differs. The kit's instruction — *if your county is one of these nine, the
county environmental health office is your counter, not the state field office* —
is supported by the form's own routing language plus the contract designation.

Corroborating mechanism, rule 0400-45-09-.10(1)(e) [V]: the well-program fee does
not apply in "any local jurisdiction which is authorized, **by private act or
pursuant to the provisions of an adopted 'home rule' charter**, to regulate the
location and construction of these wells." That private-act / home-rule route is
the obvious candidate for the septic contract counties too, though **[H]** that
it is the same mechanism.

### Who may run a percolation test — rule .05(8), verbatim [V]

> "Tests shall be conducted by an engineer or surveyor licensed in the State of
> Tennessee. An approved soil consultant or a registered professional
> environmentalist registered in the State of Tennessee may conduct percolation
> tests if they are not employed by a State, Regional, District, County or
> Municipal Department of Environment and Conservation."

### Sizing and capacity tables [V]

**Septic tank capacity, rule .08(1):** 2 bedrooms or less — 750 gal; 3 — 900 gal;
4 — 1000 gal; "For each additional bedroom, add two hundred fifty (250) gallons."
Tanks installed after 1 January 1991 must be two-compartment, inlet compartment
between 2/3 and 3/4 of total capacity (rule .09(1)).

**Disposal field sizing, Appendix II** — absorption area by percolation rate:

| Rate (mpi) | ft²/gallon | ft²/bedroom |
|---|---|---|
| 10 | 1.2 | 165 |
| 15 | 1.4 | 190 |
| 30 | 2.0 | 250 |
| 45 | 2.5 | 300 |
| 60 | 2.9 | 330 |
| 75 | 3.2 | 370 |
| 80 | 3.3 | 380 |
| 85 | 3.4 | 390 |
| 90 | 3.5 | 400 |
| 95 | 3.6 | 415 |
| 100 | 3.7 | 430 |
| 105 | 3.8 | 445 |

Notes, verbatim: "Round percolation rates to next highest increment of five (5)."
"Trenches of two (2) to three (3) feet in width are preferred." Wider trenches
carry multipliers: 4 ft ×1.33, 6 ft ×1.50, 8 ft ×1.60.

**The floor that overrides the table:** rule .07(1)(b), verbatim — "Where
percolation tests are conducted the size of the subsurface sewage disposal system
shall be determined by the rate found in Appendix II. **The minimum square
footage of trench bottom installed per bedroom shall be three hundred seventy
(370).**" So on the perc-test path, the Appendix II rows below 75 mpi do not
actually reduce the area below 370 ft²/bedroom. [V]

**Design flow:** Tennessee publishes no gpd-by-bedroom table for conventional
systems — the conventional path is ft² of trench bottom per bedroom. The only
express per-bedroom flow figure is rule .15(1), for **alternative** systems:
"one hundred fifty (150) gallons per bedroom per day." **[H]** that the same
150 gpd applies to conventional design. Thresholds that do apply: over **750 gpd**
is a "Large Conventional System" requiring a dosing system and engineer-designed
plans (.07(3)(c)); over **3,000 gpd** requires separate fields (.07(3)(c)2).

### Reserve area — Tennessee's 100% duplicate rule [V]

Rule .07(2), verbatim: "Where conventional subsurface sewage disposal systems are
installed, **sufficient additional area must be available for the expansion of the
disposal field in an amount large enough to install a secondary subsurface sewage
disposal field** as defined by these regulations."

Rule .03(2), "Lot Size," verbatim: "Lots shall be large enough to construct the
original subsurface sewage disposal system **and to provide an area for
duplication of that system**. The area(s) for both original and duplicate systems
shall meet the provisions of these rules and be of sufficient size to accommodate
a conventional subsurface sewage disposal system with thirty-six (36) inch wide
trenches except where alternative subsurface sewage disposal systems are utilized."

**Note the trap:** the reserve must be sized as if a *conventional* system were
going in it. You cannot shrink the reserve by planning to reuse gravelless pipe.
And the reserve must not be cut, filled or otherwise disturbed. [V]

### Minimum lot size [V]

Rule .03(3)(b)2, verbatim: "Where percolation tests are used… the minimum lot size
shall be **twenty thousand (20,000) square feet where a public water supply is
used** or a minimum of **twenty-five thousand (25,000) square feet where a private
water supply is used**."

≈0.46 acre on public water, ≈0.57 acre on a private well. **[H]** whether the same
minimum binds on the soil-map path — the rule states it only in the perc-test
subparagraph. The functional constraint on the soil-map path is .03(2): the lot
must fit system plus duplicate.

---

## SITE PLAN STUDIO EXTRACTION

Feeds `src/lib/siteplan/rules.ts`. **Source of truth for every distance in groups
A and B: Tenn. Comp. R. & Regs. 0400-48-01-.11(1).** Units: feet.

Lead-in text, verbatim: "The location of septic tank, dosing chamber, advanced
treatment system and disposal field shall be selected in accordance with the
following **minimum distances in feet**, bearing in mind that **local conditions
may require increased distances of separation**."

The table as printed in the rule:

| | Septic and Dosing Tanks and/or ATS | Disposal Field |
|---|---|---|
| Water Supply | 50 | 50 |
| Dwellings | 5 | 10 |
| Property Lines | 10 | 10 |
| Easements Boundaries | 10 | 10 |
| *Gullies, Ravines, Dry Stream Beds, Natural Drainageways, Sinkholes, Streams and Cut Banks | 15 | 25 |
| Water Lines | 10 | 10 |
| House to Tank Connections | -- | 10 |
| Septic and Dosing Tanks | -- | 5 |

Footnote, verbatim: "*These distances may increase or decrease as soil conditions
so warrant as determined by the Commissioner after a special investigation by an
approved soil consultant."

### A. From SEPTIC TANK / DOSING TANK / ATS

| feature | feet | rule cite | confidence |
|---|---|---|---|
| Water supply (well, spring, cistern — undifferentiated) | 50 | .11(1) | V |
| Dwelling | 5 | .11(1) | V |
| Property line | 10 | .11(1) | V |
| Easement boundary | 10 | .11(1) | V |
| Gully / ravine / dry stream bed / drainageway / **sinkhole** / stream / **cut bank** | 15 | .11(1), starred row | V — conditional |
| Water line | 10 | .11(1) | V |

### B. From DISPOSAL FIELD

| feature | feet | rule cite | confidence |
|---|---|---|---|
| Water supply (well, spring, cistern — undifferentiated) | 50 | .11(1) | V |
| Dwelling | 10 | .11(1) | V |
| Property line | 10 | .11(1) | V |
| Easement boundary | 10 | .11(1) | V |
| Gully / ravine / dry stream bed / drainageway / **sinkhole** / stream / **cut bank** | 25 | .11(1), starred row | V — conditional |
| Water line | 10 | .11(1) | V |
| House-to-tank connection (building sewer) | 10 | .11(1) | V |
| Septic / dosing tank | 5 | .11(1) | V |
| Adjacent trench wall (undisturbed earth between trenches) | 6 | .07(4)(d) | V |

### C. Mapping to the studio's core seven

| CoreSeparations field | feet | citation to print |
|---|---|---|
| `wellToSeptic` | 50 | 0400-48-01-.11(1) — "Water Supply" row, septic tank column |
| `wellToDrainfield` | 50 | 0400-48-01-.11(1) — "Water Supply" row, disposal field column |
| `wellToPropertyLine` | **null** | no state rule found in the septic chapter |
| `septicToPropertyLine` | 10 | 0400-48-01-.11(1) |
| `septicToBuilding` | 5 (tank) / 10 (field) | 0400-48-01-.11(1) — "Dwellings" row |
| `septicToSurfaceWater` | 15 (tank) / 25 (field) | 0400-48-01-.11(1), starred row — conditional |
| `wellToSurfaceWater` | **null** | no surface-water setback for wells found in either chapter |

### C2. The well-side table — 0400-45-09-.10(2), TABLE A [V]

"MINIMUM DISTANCES TO SEPARATE WATER WELLS FROM POTENTIAL SOURCES OF
CONTAMINATION." Lead-in, .10(2)(a): "The construction of a water well is
prohibited at other than a safe distance from any known potential source of
contamination."

| Source of contamination | Minimum distance |
|---|---|
| Animal pens or feed lots | 100 feet |
| Leaching pits; sewage lagoons | 200 feet |
| Pit privys *(rule's own spelling)* | 75 feet |
| Sewer lines | 50 feet |
| Sludge and septage disposal sites | 100 feet |
| **Septic tanks and drain fields** | **50 feet** |
| House to septic tank connections, if the line is tight | 10 feet |
| House to sewer line, if the line is tight | 10 feet |

**THE TWO CHAPTERS AGREE — checked explicitly.** Well-to-septic is **50 ft** in
all three places it is stated: the septic table's "Water Supply" row, the well
chapter's Table A, and the driller's completion report (0400-45-09-.15(2)(j)
requires the driller to confirm "the septic tank and field lines are located
**fifty (50) feet or greater** from the water well"). The tight building-sewer
line is 10 ft in both chapters. [V]

The well chapter **adds** coverage the septic chapter lacks (sewer lines 50 ft,
pit privies 75 ft, animal pens 100 ft, sludge/septage sites 100 ft, leaching pits
and sewage lagoons 200 ft) and adds a property-line rule the septic table has no
equivalent for.

### C3. ⚠ THE 25-FOOT TRAP — different well types, not different chapters [V]

Rule **0400-45-09-.17**(1)(a) sets much shorter distances for **closed-loop
geothermal boreholes** than Table A sets for water wells:

| Feature | Geothermal borehole (.17) | Water well (Table A, .10(2)) |
|---|---|---|
| Sewer line | 10 ft | 50 ft |
| **Septic tanks** | **25 ft** | **50 ft** |
| **Septic drain fields** | **25 ft** | **50 ft** |
| Springs | 100 ft | *(not listed)* |
| Water wells | 100 ft | *(not listed)* |

**A reader skimming chapter 0400-45-09 will find "25 feet from septic tanks" and
believe it governs their drinking-water well. It does not.** Note also that the
spring setback (100 ft) and the well-to-well setback (100 ft) appear **only** in
the geothermal table and cannot be cited as general water-well requirements.
Printed in TN.2 as an explicit warning.

### C4. Well property-line rule — graduated, and useful [V]

Rule 0400-45-09-.10(2)(d), verbatim: "**New wells shall not be located closer
than ten (10) feet from a property line.** New wells located from ten (10) feet
to twenty-five (25) feet from a property line shall require a minimum of
**thirty-five (35) feet of casing** installed below land surface with impervious
material such as cement grout or bentonite chips, tablets or bentonite grout
backfilled in the annular space to a depth of thirty-five feet."

Three tiers: **<10 ft prohibited; 10–25 ft allowed but triggers 35 ft of
cased-and-grouted construction; ≥25 ft normal.** Siting the well a few feet
further in can save a great deal of casing.

Other siting rules [V]: a well adjacent to a building must clear any projection
by **not less than 5 feet** (.10(2)(c)1); **new wells may not be constructed in
pits or basements** (.10(2)(c)2); in a flood-prone area the top of the watertight
casing must extend **not less than 2 feet above the 100-year flood plain**
(.10(2)(b)); wells closer than **50 feet** to a known source of pollution
**shall not be hydrofractured**.

### D. EXPLICIT NEGATIVE FINDINGS — `feet: null`, with a note. Do not invent numbers.

| feature | status |
|---|---|
| Public / community well, as distinct from private | **Not differentiated.** One "Water Supply" row at 50 ft. |
| Driveway, as a horizontal setback | **No setback.** Governed as a pipe-material spec (.07(4)(q)) plus a no-vehicular-traffic rule (.07(4)(s)). |
| Spring, as a numeric setback | **No standalone number.** Falls under "Water Supply" (50 ft) if it is the supply; otherwise an excluded area under .04(4)(b). |
| Cistern, as a numeric setback | **No standalone number.** Same treatment as spring. |
| Embankment | **Not a listed term.** "Cut Banks" is the analogous listed term, 15/25 ft. |
| Lake / pond / impoundment | **Not separately listed.** "Streams" is listed at 15/25 ft. |
| Foundation wall, as distinct from "Dwellings" | **Not separately listed.** Use the "Dwellings" row. |

### E. Non-setback site constraints

| constraint | value | rule cite | confidence |
|---|---|---|---|
| Depth to seasonal water table below field bottom | 4 ft | .04(2) | V — reducible where soil conditions provide adequate groundwater protection |
| Depth to rock below field trench bottom | 4 ft | .04(3)(a) | V — reducible where soil conditions warrant |
| Max slope, disposal field — presumed unsuitable above | 30% | .04(4)(d) | V — rebuttable |
| Max slope, disposal field — absolute | 50% | .04(4)(d) | V — hard |
| Acceptable soil absorption rate range | 10–75 min/in | .07(1)(a) | V |
| Below this rate a conventional system may not be used | 10 min/in | .04(4)(f) | V |
| Statutory ceiling with perc test | <106 min/in | .07(1)(d) / T.C.A. § 68-221-403(c)(1) | V quote, **H on reconciliation** with the 75 mpi sentence |
| Minimum lot size, public water | 20,000 sq ft | .03(3)(b)2 | V — stated for the perc-test path |
| Minimum lot size, private well | 25,000 sq ft | .03(3)(b)2 | V — stated for the perc-test path |
| Reserve area | 100% duplicate | .07(2), .03(2) | V |
| Min trench bottom per bedroom (perc-test path) | 370 sq ft | .07(1)(b) | V |
| Min undisturbed soil depth to qualify for perc test | 24 in | .03(3)(b)1(i) | V |
| Trench depth range | 24–48 in | .07(4)(u) | V |
| Ground cover over media | 12 min / 36 max in | .07(4)(o) | V |
| Design flow (alternative systems) | 150 gal/bedroom/day | .15(1) | V for alternative; **H if applied to conventional** |
| Large-system threshold (engineer required) | 750 gpd | .07(3)(c) | V |

### F. The sinkhole rules — distinctive Tennessee content

Rule .04(4)(b), verbatim: "Gullies, ravines, dry stream beds, natural drainage
ways, **sinkholes**, wells, springs, cisterns, streams and caves **shall be
excluded from consideration as usable areas** for subsurface sewage disposal
systems." [V]

Rule .04(4)(c), verbatim: "**Sinks** shall be considered unsuitable for subsurface
sewage disposal **unless** the following requirements are met: 1. Depth to rock
formations must be a minimum of four (4) feet from the surface of the ground and
trench depth shall not exceed thirty (30) inches. 2. Slopes must be thirty (30)
percent or less. 3. The area must not be subject to flooding. 4. All other site
suitability criteria must be met." [V]

**Internal tension worth flagging to the buyer:** .04(4)(b) excludes sinkholes
outright while .04(4)(c) gives conditions under which "sinks" may be used, and the
chapter does not define the difference between the two terms. **[H] on the
reconciliation** — most likely the sinkhole throat is excluded while the broader
closed depression is conditionally usable. Send this one to the field office
rather than resolving it on paper.

---

## WELLS — THE PERMIT SEQUENCE [V]

Chapter **0400-45-09**, "Water Well Licensing Regulations and Well Construction
Standards", footer "September, 2015 (Revised)", authority **Tenn. Code Ann.
§§ 69-10-101 et seq.** (Water Wells Act of 1963). Like the septic chapter,
**renumbered from the Health Department's 1200 series** (1200-04-09).

- **Licensed driller required.** Rule .10(1)(a) bars *any person* from
  constructing a well except in accordance with the Act and rules. TDEC's license
  page, verbatim and worth quoting to a buyer: "Tennessee licensed **general
  contractors, licensed electricians, and licensed plumbers ARE NOT permitted**
  to install or perform maintenance on water wells, water well pumps, or water
  well treatment systems unless they are also licensed by the TDEC, Division of
  Water Resources."
- **Notice of Intent BEFORE drilling**, filed by owner or driller, **$75** per
  property site; "**No well or borehole shall be drilled unless the driller has
  documentation that a Notice of Intent has been filed**" (.10(1)(c),(d)).
  **Expires 180 days** (.10(1)(h)). Fee waived if the same owner filed for the
  same property within the past five years (.10(1)(f)).
- **Report of Well Driller within 60 days** of completion (.15(1)), including the
  log, casing detail, static water level, **latitude and longitude to the nearest
  second**, and confirmation that septic is ≥50 ft away (.15(2)(j)).
- **Disinfection mandatory:** chlorine residual of at least **100 ppm**, standing
  **not less than 12 hours**, then pumped until the odor is gone (.12(1)).
- **Casing:** watertight from at least **19 feet below** land surface to **6
  inches above** it (.10(5)(a)). **Grout 3–10 ft is mandatory**; grouting the
  rest of the annulus is a departmental *recommendation* only (.10(6)(b)).
- **No homeowner exemption for drilling.** The rules carve out none. The owner's
  recognized role is filing the Notice of Intent — paperwork, not permission to
  dig. The one verified owner self-help is **abandoning a hand-dug well less than
  60 feet deep** (.16). **[H]** whether the statute itself contains an
  owner-drills-own-well exemption; the statute text was not read.

---

## KARST — AND THE UIC FINDING [V]

Tennessee's karst shows up in **three** separate programs. The septic rules treat
sinkholes as both a setback (15/25 ft, starred row) and a suitability problem
(excluded from usable area under .04(4)(b); "sinks" conditionally usable under
.04(4)(c)). Note the septic exclusion list expressly includes **caves**.

**The finding most Tennessee owner-builders have never heard**, from chapter
**0400-45-06, "Underground Injection Control"**, revised November 2024 (also
renumbered out of the 1200 series):

> "**Improved sinkhole**" means a naturally occurring karst depression **modified
> by man** in such a manner that the chemical, physical, biological,
> radiological, or bacteriological properties of the water or fluids moving into
> the subsurface through it have been or will be altered.

> "Injection well" means structure or device which is used for the emplacement of
> fluids into a subsurface stratum including… **(c) An improved sinkhole**; …
> (e) Modified recharge point.

Rule .06 lists among **Class V** wells: "(q) Modification of a recharge point or
the area where the recharge originates; and **(r) Improved sinkholes**." Rule
.07(1): "**all injection wells and activities must be authorized by permit or by
rule.**"

**Plain language for the kit:** route driveway runoff, roof drains or a graded
swale into a sinkhole and you have arguably created a Class V injection well.
Filling or grading around a sinkhole is not neutral earthwork in Tennessee.
Authorization-by-rule is available for many Class V wells (.14(2)), so this is
usually a conversation rather than a catastrophe — but one to have before the
excavator arrives. **[V]** on every quoted definition and the Class V listing;
**[H]** on the enforcement posture for a single residential lot. **No UIC fee is
printed** — rule .18's dollar figures were not extracted.

The same chapter defines a **septic system** as "a '**well**' that is used to
emplace sanitary waste below the surface" — which is why the septic chapter's
sinkhole exclusions and the UIC rules point the same way. [V]

---

## STORMWATER, ARAP AND A DATED TRIPWIRE [V]

- **Construction stormwater:** permit **TNR100000**, triggered by "the
  disturbance of **1 acre or more of total land area**." Most single-house lots
  stay under it; driveways, the septic field and its reserve, the well pad,
  staging and spoil are what push a rural build over.
- **⚠ DATED TRIPWIRE:** the outgoing CGP expired **30 September 2026**; the
  **2026 CGP took effect 1 October 2026** and runs to 30 September 2031. TDEC's
  own notice warned the forms would change on that date. Anyone breaking ground
  on or after 1 October 2026 is under the new permit. **Printed in TN.2.**
- **Reduced threshold in special/impaired/exceptional watersheds: [H] — NO
  NUMBER VERIFIED. Not printed.**
- **ARAP** (chapter 0400-40-07, authority Tenn. Code Ann. § 69-3-108): TDEC's own
  list of activities requiring one includes "**Road and utility crossings**" —
  that is the driveway culvert line item, stated by the agency itself. General
  Aquatic Resource Alteration Permits effective 15 May 2025 to 15 May 2030 cover
  routine crossings. A federal Corps § 404 permit and, near a TVA reservoir, a
  **TVA § 26a** approval may sit on top — TDEC names all three.

---

## OPEN QUESTIONS — for the next revision

1. **Townhouse scope discrepancy.** The statute's opt-out language speaks only of
   "one-family and two-family dwellings." Rule 0780-02-23-.14 describes opting out
   of provisions covering "one (1) and two (2) family dwellings, **townhouses** and
   additions thereto." Whether a townhouse in an opt-out jurisdiction is genuinely
   uncovered is unresolved. Low practical impact for most owner-builders; make no
   confident claim.
2. **Statute transcription is secondary.** Confirm the § 68-120-101(b) block quote
   against the official LexisNexis publication. Subsections (a) and (f) were
   obtained only as summaries, not verbatim.
3. **E-911 addressing not verified.** Needs a primary source before it goes in.
4. **NFIP participation not verified per county.** Do not assert per-county.
5. **Contract (delegated) septic counties** — the concept is verified from the
   CN-0971 map legend; the per-county list still needs extraction.
6. **The $60.57/sq ft minimum valuation will drift.** Re-check the SFMO fees page.
7. **EXEMPT jurisdictions' code editions are unknown and unknowable in bulk.** The
   statute requires only currency within seven years, so an EXEMPT city could be on
   anything from 2018 forward — and as of 2026 a 2018 code sits at the edge of that
   window.

---

## KIT REVISION WATCH — TRIPWIRES

1. **Fire Prevention rulemaking hearing scheduled 7 October 2026**
   (tn.gov/commerce/calendar/2026/10/7/fire-prevention-rulemaking-hearing.html).
   The page rendered with no body content so the subject could not be determined.
   Given that the commercial chapter moved to 2021 codes in April 2025 while the
   residential chapter is still on 2018 IRC / 2017 NEC, a residential or electrical
   update is plausible. **Re-check before and after 7 October 2026.**
2. **The jurisdiction list churns structurally.** Every opt-out resolution expires
   180 days after that body's next election. Re-pull
   `residential-permits/jurisdictions-inspectors.html` before every revision and
   compare counts (currently 50 EXEMPT / 8 SRBP / 37 OPT OUT counties).
3. **The $60.57/sq ft minimum construction cost** is a website figure and will move.
4. **2017 NEC.** Tennessee is two cycles behind; when it moves, TN.2 and TN.3 both
   change.

---

## DELIBERATELY NOT PRINTED — and why

| Claim | Why it is not in the kit |
|---|---|
| Notice of Nonpayment (§ 66-11-145) applying to a house | As enacted in 2007 the section **excludes** 1–4 family residential — the opposite of most secondary sources. Unresolved. |
| "Unlicensed contractors cannot lien in Tennessee" | Appears in a demand letter quoted by a court, not in a holding. The 2007 text carries no licensure condition. |
| "In the county of residence" as an exemption element | Appears in the permit's own important-notices text; no statutory support found. |
| The $2,500 out-of-state threshold's statutory basis | Real (it is on the Board's affidavit form) but no TCA section located. |
| A homeowner HVAC/mechanical exemption | No such text exists. The kit reports the gap. |
| Any per-county building permit fee | Only three fee bases in the state were verifiable. A wrong fee is worse than none. |
| A TVA § 26a URL or threshold | TVA returned HTTP 403 to every automated request. |
| A statewide E-911 addressing process | Administered county by county; no statewide document verified. |
| Sevier County post-wildfire construction rules | Searched; **no** such ordinance found on the county's own site. |
| A reduced stormwater threshold for special watersheds | Concept exists; no number verified. |
| A UIC fee | Rule 0400-45-06-.18's figures were not extracted. |
| A county-to-TDEC-field-office table | TDEC lists eight offices, CN-0971 routes to seven. The kit sends the reader to the map on the form instead. |
| The full 473-row jurisdiction table | It carries inspector names, emails and **phone numbers**; the kit prints no phone numbers. Counts, method and URL are printed instead. |
| A state building permit form number | The rule says only "a form prescribed by the Department"; permitting is now the CORE workflow. |
| 2018 IECC R-values | Tennessee replaced those tables with the 2009 ones. Printing 2018 numbers would be actively wrong. |

---

## LATE ADDENDUM

**Two discrepancies were resolved during kit assembly rather than during
research, by fetching and parsing the live pages directly.** Both are printed in
the kit as findings, because a buyer hitting either one would otherwise conclude
the kit was wrong.

1. **The SRBP county list differs between two official SFMO pages.** The dated
   jurisdictions-and-inspectors table lists **eight** counties including Campbell
   (with a named assigned inspector); the apply-for-a-residential-permit page
   lists **seven** and omits Campbell entirely. Verified by parsing both pages'
   markup on 2 September 2026. The kit prints the conflict, names the dated table
   as the better source, and tells the reader to confirm with the office rather
   than pick a winner.

2. **TDEC publishes eight Environmental Field Offices; CN-0971 routes to seven.**
   Memphis is on TDEC's directory and not on the form's map. Most likely because
   Shelby and its neighbors are contract counties, but the chapter does not say
   so. The kit prints the form's own routing instruction instead of a
   county-to-office table, which is correct either way.

**County counts independently re-verified during assembly:** the live
jurisdictions table parsed to 95 county rows breaking exactly **50 EXEMPT /
37 OPT OUT / 8 SRBP**, matching the research. [V]
