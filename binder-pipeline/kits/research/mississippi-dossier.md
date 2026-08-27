# Mississippi Owner-Builder Dossier — research for the MS Permit Kit (six documents)

Compiled August 2026 for `binder-pipeline/kits/ms-permit-kit/`. Every claim
printed in the kit traces to a line in this file, and every line here traces to
a primary source that was actually fetched and read.

---

## PROVENANCE — what was read, and how

Mississippi is unusually hostile to automated statute research, and the routes
that work are not the obvious ones. Recording this because the next person to
revise this kit will otherwise repeat the dead ends.

### Sources that REFUSED access (do not retry)

| Source | Result |
|---|---|
| `law.justia.com` | 403 on sections; Cloudflare JS challenge on chapter indexes |
| `codes.findlaw.com` | 403 |
| `casetext.com` | 410 Gone |
| `mscode.com` | 403 |
| `legiscan.com` | 403 |
| `law.onecle.com` | 404 (no Mississippi coverage at the guessed path) |
| `sos.ms.gov/adminsearch` | 403 |
| `web.archive.org` | connection timeouts throughout |
| WebFetch against Justia | 403 (same block as curl — different infrastructure did not help) |
| `r.jina.ai` proxy in front of Justia | Worked for one researcher earlier in the session, then began returning the Cloudflare interstitial. Treat as unreliable rather than a solution. |
| `sos.ms.gov/publications-external-affairs/mississippi-law` | 403 (this is the route MID points at for the Secretary of State's unannotated code lookup) |

### Sources that WORKED

1. **`billstatus.ls.state.ms.us` — the Legislature's bill archive. This is the
   single most valuable Mississippi research asset and it is wide open.**
   - Session index, 2008 onward: `https://billstatus.ls.state.ms.us/<YEAR>/pdf/all_measures/allmsrs.xml`
     — XML, one `<MSRGROUP>` per bill carrying `<MEASURE>`, `<SHORTTITLE>`,
     `<MEASURELINK>` and the last `<ACTION>`. Grep `<SHORTTITLE>` by keyword and
     filter actions for "Approved by Governor" to find enacted law.
   - Session index, 2006–2007: same path but `/html/all_measures/allmsrs.htm`
     (the XML path 404s for those years).
   - Enrolled bill text, 2008 onward: `documents/<YEAR>/pdf/<CHAMBER>/<RANGE>/<BILL>SG.pdf`
     (SG = as sent to Governor). 2006–2007 use `/html/` and `.htm`.
   - Per-bill history: `https://billstatus.ls.state.ms.us/<YEAR>/pdf/history/<CHAMBER>/<BILL>.xml`
   - **Reading the enrolled bill is better than reading a codified section**,
     because the bill shows the effective date, the amendment history and the
     legislative title in one document.

2. **Agencies publish their own governing statute verbatim as PDFs**, and those
   sites are not blocked:
   - State Board of Contractors: `msboc.us` → Laws →
     `wp-content/uploads/2024/06/RESIDENTIAL-LAWS-AND-RULES-REVISED-2022-WEBSITE-VERSION.pdf`
     reproduces the whole of Title 73, Chapter 59 plus the Board's rules.
     A commercial counterpart exists at
     `wp-content/uploads/2022/02/COMMERCIAL-LAWS-AND-RULES-REVISED-2022.pdf`.
   - Dept of Health: `msdh.ms.gov` → Regulation → On-Site Wastewater → Laws and
     regulations → `msdhsite/_static/resources/4499.pdf` is the Individual
     On-site Wastewater Disposal System Law as reenacted.
   - Method: `curl` with a browser User-Agent, then `pdftotext -layout`.

3. **`legislature.ms.gov`** links the official free public code at
   `www.lexisnexis.com/hottopics/mscode/` (redirects to an `advance.lexis.com`
   container). It resolves 200 but is a JavaScript application, so it is not
   machine-readable — it is, however, the correct thing to cite to buyers as
   the official free source, and that is what the kit's `STATUTE_NOTE` does.

### Session-wide hazard encountered

The WebSearch budget (200 calls) was exhausted partway through by the four
parallel research sub-agents, after which no agent in the session could search.
All findings below were obtained with `curl` alone. **Two of the four research
sub-agents went idle without ever returning a report** — the failure mode
warned about in the brief — and were only recovered by messaging them. The
statutory spine of this kit was ultimately verified directly rather than by
sub-agent, which is why every citation below carries the document it came from.

---

## THE TRAPS — the verifiable facts that competing guides get wrong

Mississippi has three, and they are unusually good ones because each is a
single sentence of enacted text that contradicts the universal claim.

### TRAP 1 (headline) — "Mandatory on the coast" is not reliably true

**The universal claim.** Every guide, including build-your-house.com's own
state guide, says the Gulf Coast counties "are required to enforce" wind and
flood provisions — flatly, with no qualification.

**What the statute says.** The post-Katrina law is **House Bill 1406, 2006
Regular Session** (approved by the Governor 14 April 2006), Section 1, now
Miss. Code Ann. § 17-2-1. Subsection (1) does impose the mandate:

> The counties of Jackson, Harrison, Hancock, Stone and Pearl River, including
> all municipalities therein, shall enforce, on an emergency basis, all the
> wind and flood mitigation requirements prescribed by the 2003 International
> Residential Code and the 2003 International Building Code, as supplemented.

But subsection (4) hands it straight back:

> The provisions of this section shall go into effect thirty (30) days from the
> effective date of this act. However, **within sixty (60) days after the
> provisions of this section go into effect, the board of supervisors of a
> county and/or the governing authorities of any municipality within a county,
> upon resolution duly adopted and entered upon its minutes, may choose not to
> be subject to the code requirements imposed under this section.**

So the coastal mandate carried a **one-time 60-day opt-out** in 2006, available
separately to each county *and to each municipality within it*. Whether it
binds a given parcel today depends on a vote recorded in a minute book twenty
years ago.

**Also note subsection (2):** the emergency 2003 IRC/IBC wind and flood
requirements "shall remain in force until the county board of supervisors or
municipal governing authorities … adopts as minimum mandatory codes the latest
editions." In a coastal jurisdiction that never adopted, the operative wind
standard may still be the **2003** editions.

### TRAP 2 — The statewide opt-out was a 120-day window in 2014, not a standing choice

**The universal claim.** Guides describe Mississippi in the present tense —
"counties *can* opt out of the building code" — implying an ongoing option.

**What the statute says.** The statewide law is **Senate Bill 2378, 2014
Regular Session** (approved 17 March 2014, **effective August 1, 2014**).
Section 1(1) requires adoption:

> Except as provided in Section 17-2-1(1) and subsection (3) of this section, a
> county board of supervisors or municipal governing authority shall adopt and
> amend as minimum codes one (1) of the following as the State Uniform
> Construction Code…

Section 1(3) is the opt-out:

> **Within one hundred twenty (120) days after the provisions of this section
> go into effect**, the board of supervisors of a county and/or the governing
> authorities of any municipality within a county, upon resolution duly adopted
> and entered upon its minutes, may choose not to be subject to the code
> requirements imposed under this section.

Effective 1 Aug 2014 + 120 days ⇒ the window closed at the end of **November
2014** and has never reopened. **Confirmed by scanning every session index from
2008 to 2026: SB 2378 is the only enacted State Uniform Construction Code bill
in that entire period.** HB 679 (2014) was the identical House companion and
died in the Senate; SB 2663 (2017), HB 1142 (2021), HB 1272/1273 and SB 2045
(2023) all died in committee.

**Independently corroborated by the State**, which also supplies the exact
date. The State Fire Marshal's *Mississippi Uniform Building Codes* page
(`mid.ms.gov/sfmo/mississippi-uniform-building-codes/`, fetched August 2026)
says verbatim:

> Under Senate Bill 2378 of 2014, all counties and municipalities must enact
> uniform building codes unless they opt out prior to Nov. 30, 2014.

**And there is no published roster.** That MID page is a *data-collection form*
inviting jurisdictions to self-report their code policy; the Department
publishes no resulting list. Contrast the fire side, where § 45-11-101 does
impose an annual published-list duty — there is no parallel duty for building
codes. This is why MS.4 teaches the minute-book lookup instead of promising a
table.

**Codification note.** SB 2378 § 1 was codified into Title 17, Chapter 2. A
research agent reports the pinpoint as **§ 17-2-4** ("State Uniform
Construction Code; exemptions", Laws 2014 ch. 382 § 1), which is internally
plausible — it would explain why the codified §§ 17-2-7 and 17-2-9 now read
"Sections 17-2-1 through 17-2-5" alone, having dropped the enrolled bill's
trailing "and Section 1 of this act" as redundant once Section 1 landed inside
that range. **I could not confirm the pinpoint independently** (every code
mirror refused), so **the kit deliberately cites the bill and chapter rather
than the section number**: "Senate Bill 2378, 2014 Regular Session, Section 1,
effective August 1, 2014, codified in Miss. Code Ann. Title 17, Chapter 2."
Confirm § 17-2-4 before printing it in a future revision. Related caution from
the same report: do not quote the *enrolled* §§ 17-2-7/17-2-9 scope language as
current law, because the codified text differs.

**The consequence the kit sells:** the reader cannot change their code status
and cannot infer it. They must go and read a resolution. Which leads to —

### TRAP 3 — There is no single "Mississippi code edition," and the adopted code is a public record you can demand

**The universal claim.** "Mississippi adopted the 2021 IRC statewide effective
July 1, 2024, and the 2024 IRC effective May 18, 2026." (This is what the
site's own state guide says.)

**What the statute says.** SB 2378 § 1(1) lets a jurisdiction adopt "**one (1)
of the last three (3) adopted editions**" of the IBC or IRC. Miss. Code Ann.
§ 17-2-3(5), as amended by **HB 1385, 2011 Regular Session**, says the Building
Codes Council "shall adopt by reference and amend **only one (1) of the last
three (3) editions** … as **discretionary statewide minimum codes**."

Two things follow that no guide states:
- The correct answer to "what code is Mississippi on?" is **"which of three?
  ask your jurisdiction."** Neighboring counties can lawfully enforce different
  IRC editions on the same day.
- The word in the statute is **discretionary**. The Council sets a floor for
  jurisdictions that adopt; it does not impose a code on the state.

**The Council has adopted nothing — and this is now established.** A research
agent enumerated the Mississippi Insurance Department's complete adopted-
regulations index, including all sixteen chapters of 19 Miss. Admin. Code Part
7 (State Fire Marshal), where a Council code would legally have to be filed.
Keyword scan of that index returned **zero** hits for "Building Codes Council",
"Residential Code", "IRC", "Energy" and "National Electrical". Part 7's
chapters are electronic-protection licensing, the volunteer-firefighter tax
credit, modular/factory-built homes, MH bonding and installation inspection,
the Fire Prevention Code, and nine LP-gas/conveyance/first-responder chapters.
MID's 220-page sitemap and its own site search returned nothing either.

Phrase this carefully and do **not** write "abolished" or "repealed":
§ 17-2-3 is alive and unrepealed. The accurate statement, and the one the kit
prints, is that **the Council legally exists, its authority is statutorily
"discretionary," and it has published no adopted code** — so every statutory
reference to appendices "as adopted and amended by the Mississippi Building
Codes Council" points at an empty set. Two consequences worth printing, both of
which the kit states: **there is no statewide residential code edition**, and
there is **no statewide electrical or residential energy code for a site-built
house** — the NEC and the energy provisions reach a house only through
whichever IRC edition the local jurisdiction adopted. (Caveat carried from the
research: absence was verified within Title 19, where such a rule would live,
not across every title. High confidence, not absolute.)

**The mechanism nobody prints:** an adopted code is a filed public record.
Miss. Code Ann. § 19-5-9 (counties) requires the code to be "certified to by
the president and clerk of the board of supervisors and … filed as a permanent
record in the office of the clerk." § 21-19-25 (municipalities) requires it to
be "certified to by the mayor and clerk of the municipality, and … filed as a
permanent record in the office of the clerk," with published notice. So the
reader can walk into the chancery clerk's office and ask to see the filed code
and the 2014 resolution. **That is MS.4's central move and the kit's
differentiator.**

### Where the two bogus edition claims actually come from

Both figures in the existing state guide were traced to real Mississippi
adoptions that were then over-generalized. This is the most useful thing to
carry into the state-guide correction, because it explains the error rather
than merely contradicting it.

**"2021 IRC, effective July 1, 2024"** — the date is real, the code is not.
The State Fire Marshal's pages (`mid.ms.gov/sfmo/` and `/sfmo/fce/`) carry this
notice verbatim:

> *** NOTICE *** AS OF JULY 1, 2024, THE STATE OF MISSISSIPPI – OFFICE OF THE
> STATE FIRE MARSHAL HAS ADOPTED THE 2024 ADDITION [sic] OF THE INTERNATIONAL
> FIRE CODE (IFC) AND THE INTERNATIONAL BUILDING CODE (IBC).

That is the **Fire Marshal** adopting the 2024 **IFC and IBC**. The guide's
claim keeps the date and swaps in a residential code and a different year.

**"2024 IRC, effective May 2026"** — real, but modular homes only. 19 Miss.
Admin. Code Pt. 7, Ch. 3, *Uniform Standards Code for the Factory-Built Homes
Law as related to Modular Homes* (Reg. ME-2007-3, revised 1 July 2026, filed
22 May 2026). Rule 3.02.1 adopts, for **modular homes**, the 2024 editions of
the NEC, IBC, IRC, IMC, gas and plumbing codes, plus SSTD 10 or ASCE 7. So a
genuine statewide 2024-IRC-and-2024-NEC adoption does exist in Mississippi —
**under State Fire Marshal jurisdiction, for modular homes, and it does not
reach a site-built house.** (Defect noted: the same regulation's definitions
section still calls the IRC the 2006 edition, contradicting Rule 3.02.1(D). Do
not cite the definitions section.)

**Fire code scope, for completeness.** The Mississippi Fire Prevention Code
(19 Miss. Admin. Code Pt. 7 Ch. 7, effective 1 Jan 2025) uses a rolling "most
current edition" formula and is the statewide default for jurisdictions that
adopt none — but § 45-11-101's scope is state buildings, public assembly, and
buildings of 75 feet or more. **It does not reach one- and two-family
dwellings.** The code is statewide by default; the scope is not. Nothing in the
kit claims otherwise.

### Bonus finding — the sprinkler asymmetry

SB 2378 § 1(1)(b) adopts the IRC "with the exception of those provisions that
require the installation of a multipurpose residential fire protection
sprinkler system or any other fire sprinkler protection system in a new or
existing one- or two-family dwelling." § 17-2-3(7) separately bars the Council
from imposing one — **but expressly preserves local power**: "the county boards
of supervisors and municipal governing authorities may adopt, modify and
enforce codes adopted by the council, including the adoption of codes which
require the installation of fire protection sprinkler systems in any
structure." State: no. Your city: maybe.

### Bonus finding — the trade-license threshold is ZERO, not $10,000

Treated as a trap in MS.1 because it is the most consequential error in the
existing coverage. See the licensing section below.

---

## MS.0 — Cover summary facts

- Mississippi has a broad, unconditional-on-its-face owner-builder licensing
  exemption; no state building permit; and no code enforced at all across much
  of the state.
- Whether a code binds a parcel was fixed by resolutions in **2006** (coast,
  60-day window) and **2014** (statewide, 120-day window). Both closed.
- Cover carries a **"Code Status (see MS.4)"** field — the Mississippi analogue
  of Michigan's "Enforcing Agency" field.

---

## MS.1 — Licensing: the exemption, its limits, and who it does not cover

Source: Miss. Code Ann. Title 73, Chapter 59 (Residential Builders and
Remodelers), read in the Board's *Residential Builders Law 2022* booklet.

### The definitions that set the thresholds — § 73-59-1

- **(b) "Residential builder"** — "any corporation, partnership or individual
  who constructs a building or structure **for sale** for use by another as a
  residence or who, for a fixed price, commission, fee, wage or other
  compensation, undertakes … the construction, or superintending of the
  construction, of any building or structure which is not more than three (3)
  floors in height, **to be used by another as a residence**, when the total
  cost of the undertaking exceeds **Fifty Thousand Dollars ($50,000.00)**."
  → The $50,000 governs building **for another person**. It is not a cap on
  your own house. Building your own home fits neither prong.
- **(c) "Remodeler"** — improvements to an existing residence for compensation
  "when the total cost of the improvements exceeds **Ten Thousand Dollars
  ($10,000.00)**."
- **(h) "Construction manager"** — "any person or entity, **other than a
  residential builder, remodeler or owner**, who has a contract or agreement
  with the owner of the property …, **no matter if that owner himself is the
  general contractor or a holder of a building permit**."

### Who must be licensed — § 73-59-3(1)

(a) residential builders; (b) residential remodelers; (c) **construction
managers** contracting with the owner; (e) residential solar contractors; and —
the trap —

> **(d) Any subcontractor, of any tier, performing the following work or within
> the following trade, on any residential construction or residential
> improvement project, no matter the dollar amount of the construction or
> improvements: (i) Electrical; (ii) Plumbing; (iii) Mechanical; and/or (iv)
> Heating, ventilation and/or air conditioning**

**The $10,000 trade threshold repeated across the internet does not exist.** It
is § 73-59-1(c)'s *remodeler* figure, misapplied. The trade threshold is zero.
"Of any tier" additionally defeats the "my licensed GC subbed it out" defense.

### The exemptions — § 73-59-15

Seven paragraphs; four can reach an owner-builder:

- **(1)(b)** — "Any person who undertakes construction or improvement on his
  own residence, or who acts as his own general contractor in the performance
  of construction or improvement on his own residence." *No cost cap and no
  not-for-sale wording inside the paragraph itself.* **This is the exemption.**
- **(1)(c)** — building or acting as GC where the owner is "related to such
  person by consanguinity or direct affinity, and the property or improvement
  will not be for sale, rent, public use or public assembly."
- **(1)(d)** — "The owners of property who supervise, superintend, oversee,
  direct or in any manner assume charge of the construction … on such property
  for use by such owner and which will not be for sale, rent, public use or
  public assembly."
- **(1)(g)** — "Any person who constructs **two (2) single residences or less**
  within a period of one (1) year **in any county or municipality which does
  not require a building permit** or any local certification for such
  construction, provided that the person is not building the residences for
  sale." *Mississippi wrote a no-permit-jurisdiction exemption into its
  licensing law — evidence of how normal no-code counties are here.*

Also (a) agricultural buildings, buildings constructed as a community effort,
tenant houses; (e) and (f) licensed/COR-holding contractors.

### The cap — § 73-59-15(2), and why "calendar year" is wrong

> A person specified in subsection (1)(b) or (c) shall not make more than one
> (1) application for a permit to construct a single residence or shall not
> construct more than one (1) single residences **within a period of one (1)
> year**. There shall be a **rebuttable presumption** that such person intends
> to construct for the purpose of sale, lease, rent or any similar purpose if
> more than one (1) application is made … or if more than one (1) single
> residences is constructed within a period of one (1) year.

Three points the kit makes and others miss:
1. **"Within a period of one (1) year" is a rolling window, not a calendar
   year.** The state guide's "one dwelling per calendar year" is wrong, and
   wrong in the permissive direction (Dec + Jan would be two in one year).
2. **It applies to (1)(b) and (c) only.** Paragraph (d) is not in the list.
3. It is a **presumption**, not a bar — rebuttable with evidence of intent.
   The mechanism: being presumed to build for sale drops you into
   § 73-59-1(b)'s "for sale" prong, which requires a license.

### The permit counter — § 73-59-17

> The building official … of any municipality or county, **shall refuse to
> issue a permit** for any undertaking which would classify the applicant as a
> residential builder or remodeler under this chapter **unless the applicant
> has furnished evidence that he is either licensed as required by this chapter
> or exempt from the requirements of this chapter.** The building official …
> shall also **report to the board** the name and address of any person who, in
> his opinion, has violated this chapter…

The statute does not define what "evidence … that he is … exempt" looks like —
that is local, which is why the kit sends the reader to ask rather than
printing a form name.

### Penalties — § 73-59-9

- (1) misdemeanor; fine "not less than One Hundred Dollars ($100.00) and not
  more than Five Thousand Dollars ($5,000.00) or … imprison[ment] for not less
  than thirty (30) nor more than sixty (60) days in the county jail, or both."
- (2) an unlicensed party "may not bring any action, either at law or in
  equity, to enforce any contract for residential building or remodeling or to
  enforce a sales contract," and may recover only "actual documented expenses
  for labor, materials or both … shown by **clear and convincing evidence**."
- (3) the Board "shall have the authority to issue a citation and may stop
  work."

### Other Chapter 59 provisions worth knowing

- **§ 73-59-18** — residential contractors need a Dept of Revenue permit under
  § 27-65-27 to get a building permit, but "**a residential contractor is not a
  person building, repairing or renovating his or her own residence**." Does
  not reach an owner-builder.
- **§ 73-59-19** — a licensed residential builder may do commercial work up to
  7,500 sq ft without another license.
- **§ 73-59-1(a)** — the Board is the State Board of Contractors created in
  § 31-3-3 (Title 31 Ch. 3 is the separate *commercial* Certificate of
  Responsibility scheme; do not conflate).

### Owner doing their own trade work

Reading printed in MS.1: § 73-59-3(1)(d) reaches "any subcontractor, of any
tier" — an owner is not a subcontractor on their own house — and § 73-59-15(1)(b)
disapplies the whole **chapter** to a person building their own residence. So
**the State does not require an owner to be a licensed electrician to wire
their own home.** The kit then immediately sends the reader to check locally,
because counties (§ 19-5-9, unincorporated areas only) and municipalities
(§ 21-19-25) may adopt electrical, plumbing and gas codes with their own rules
on who may pull a permit and do the work.

---

## MS.2 — Applications: wastewater first, building permit maybe

The organizing insight of the kit: **in Mississippi the building permit is the
optional part; the wastewater approval is not.** The Individual On-site
Wastewater Disposal System Law sits in Title 41 (public health), so a county's
building-code status is irrelevant to it.

Source: Miss. Code Ann. §§ 41-67-1 et seq., read as reenacted by **HB 522,
2023 Regular Session**, cross-checked against the 2018 reenactment (HB 331).

### The two operative sentences — § 41-67-5

> (1) **No owner, lessee or developer shall construct or place** any mobile,
> modular or permanently constructed residence, building or facility, which may
> require the installation of an individual on-site wastewater disposal system,
> **without having first submitted a notice of intent to the department.**

Note the trigger: constructing or placing the **residence** — the duty lands at
the start of the project, not when the septic system goes in.

> (2) **No public utility supplying water shall make connection** to any
> dwelling, house, mobile home or residence **without the prior written
> approval of the department** certifying that the plan for the sewage
> treatment and disposal system … complies with this chapter. Connections of
> water utilities may be made during construction if the department has
> approved a plan … **and the owner of the property has agreed to have the
> system inspected and approved by the department before the use or occupancy
> of the property.**

**This is the enforcement mechanism that binds every parcel in Mississippi
regardless of building code**, and it is the kit's answer to "what still applies
if my county opted out."

### The two-acre exemption — § 41-67-6(7)

> Any lot or tract that is **two (2) acres or larger** shall be exempt from the
> requirements of this chapter and regulations of the department relating to
> approval of individual on-site wastewater disposal systems by the department,
> and shall be exempt from the provisions of Section 41-67-5(2), provided that:
> (a) All wastewater is contained on the lot or tract; (b) No watercourse, as
> defined in Section 51-3-3(h) … is impacted; and (c) **The person who
> installed the … system provides the department with a signed affidavit**
> attesting that the requirements of paragraphs (a) and (b) are met.

Three cumulative conditions. It exempts from *approval* and from the
water-connection bar — it does **not** by its terms exempt the § 41-67-5(1)
notice of intent, and MSDH's own process confirms this (the two-acre option
still runs steps 1–4).

### The clocks — § 41-67-7(1)

Approval required except per § 41-67-6(7); the department "must approve or
disapprove the request within five (5) working days"; must give written reasons
for disapproval; and "**if the department does not respond to the request
within ten (10) calendar days, the request … shall be deemed approved.**"

### Advanced systems — § 41-67-7(5)

The property owner, "if not a qualified homeowner maintenance provider, shall
keep a continuing maintenance agreement with a certified installer on all
advanced treatment systems **in perpetuity**." § 41-67-3 obliges the department
to train homeowners to become qualified maintenance providers, and "no fees
shall be charged to the homeowner for such training."

### The repealer — § 41-67-31

The chapter "shall stand repealed on **July 1, 2028**" (as extended by 2023
HB 522; the prior date was 1 July 2023, extended from 2018 HB 331). **Mississippi
reenacts this law on a roughly five-year cycle.** A revision of this kit after
mid-2028 must re-verify rather than assume. Session scan confirms HB 522 (2023)
is the most recent enacted reenactment.

### The process — MSDH Form 908

*Statement of Intent — Individual On-site Wastewater Disposal System (IOWDS):
New*, revision stamp 21-AUG-17. Filed with the legal description as it appears
in county records, a plot plan, and the fee; by email, by mail to PO Box 1700
Jackson, or online via the Department's wastewater application page.

Five steps: (1) application; (2) **site soil evaluation** by the local
environmentalist; (3) **permit/recommendation** — the form states this is
presented "to your water supply company to receive a water meter"; (4)
installation by a **certified installer**, who must contact the Department
**24 hours before starting work**; (5) **final approval** on the installer's
signed installation affidavit, plus the owner's maintenance affidavit for an
advanced treatment system.

Form 908 also carries a **non-residential water meter** option: if no IOWDS
will be installed and no residential wastewater generated, the property gets a
meter only — and if an operating IOWDS is later found, the meter is removed and
a fine of up to $10,000 may follow.

### Who else can require final approval

Form 908 asks the applicant to confirm final approval is not required by: the
board of supervisors (county ordinance), the water association/supplier, the
lending entity, a public utility authority, or another party (e.g. subdivision
agreements). MSDH publishes a *Map: County on-site wastewater disposal
ordinances* plus a list of "known final approval requiring entities" (FHA and
some sixteen named water associations, utility districts and cities), compiled
13 April 2021, carrying the Department's own caveat that the list "may or may
not be complete." **The kit prints the categories, not the roster** — see
deliberately-omitted, below.

---

## MS.3 — Inspections

There is **no statewide Mississippi inspection schedule**, because there is no
statewide inspection program. The sequence the kit prints is the one the IRC
produces, and a jurisdiction gets it only by adopting the IRC under SB 2378
§ 1(1) / § 17-2-3(5) — with the edition being any of the last three. The kit
says this explicitly rather than presenting the list as statutory.

The document is written twice over: an inspection log for readers whose
jurisdiction inspects, and a private-inspection procurement plan for readers
whose jurisdiction does not — framed around the three parties who still demand
evidence (lender draw inspections, builder's risk and wind insurers, future
buyer). **Where no code is enforced there is no certificate of occupancy**, and
the kit says so rather than implying one exists.

Mississippi-specific site conditions flagged: the whole state is in the IRC's
"very heavy" termite infestation region (plus Formosan termites on the coast);
expansive clay in central Mississippi, notably the Jackson metropolitan area;
and coastal wind/flood per § 17-2-1 subject to Trap 1.

---

## MS.4 — Establishing code status (the kit's differentiator)

The mechanism, all from enacted text:

- **§ 19-5-9** — a county may adopt building, plumbing, electrical, sanitary
  and related codes "within but not exceeding the provisions of the
  construction codes published by nationally recognized code groups," but those
  codes "**shall apply only to the unincorporated areas of the county**." The
  adopted code "shall be certified to by the president and clerk of the board
  of supervisors and shall be filed as a permanent record in the office of the
  clerk." Farm buildings excluded except as required by the Flood Disaster
  Protection Act of 1973. Utility-owned equipment excluded.
- **§ 21-19-25** — a municipality adopts by ordinance; the code is "certified
  to by the mayor and clerk of the municipality, and shall be filed as a
  permanent record in the office of the clerk"; notice of adoption published
  once in a newspaper or posted in three public places; and the code "shall not
  be in force for one (1) month after its passage, unless the municipal
  authorities in the ordinance authorize to the contrary." The section also
  carries the coastal command: "the governing authorities of each municipality
  in Jackson, Harrison, Hancock, Stone and Pearl River Counties shall enforce
  the requirements imposed under Section 1 of this act."
- **§ 17-2-5** (2008 HB 1465) — any county or municipality adopting codes after
  1 July 2008 shall adopt as minimum codes those established by the Building
  Codes Council; those that had adopted pre-2000 codes had until 1 July 2010 to
  come up to Council minimums; and enforcement is the adopting body's own.
  Also authorizes agreements with other governmental entities or **certified
  third-party providers** to issue permits and enforce.
- **§ 17-2-3** (2011 HB 1385) — the Council: 11 members appointed by
  professional associations, State Fire Marshal ex officio non-voting, quorum
  of four, two-thirds of those present to decide, meetings open to the public.

The reader's actual procedure, which is what MS.4 prints: establish whether the
parcel is inside a municipality (county tax assessor settles it from the parcel
number); ask the municipal clerk or the chancery clerk whether a code was
adopted and to see the filed copy; **ask specifically whether the board adopted
an opt-out resolution in 2014, or in 2006 on the coast**; get the answer in
writing; and if a code is enforced, ask which of the three permitted editions.

The second half of MS.4 lists the authorities that apply regardless of code
status: county health department (septic), floodplain administrator, E-911
addressing, county road department or MDOT, electric utility, water association
or rural water district, and zoning.

---

## MS.5 — Documents, and what needs no permit

Statewide-identity documents are only the MSDH ones (Form 908, site soil
evaluation, permit/recommendation, installation affidavit, maintenance
affidavit, final approval, two-acre exemption affidavit) plus Board of
Contractors license verification. Everything else is local and is described by
function rather than form number, because **Mississippi has no statewide
building permit application**.

### Structures exempt from the state construction code

- **§ 17-2-7** farm structures — a structure on a farm other than a residence
  or attached to one; barns, sheds, poultry houses, not public livestock areas;
  loses the exemption if converted to another use. **Conditional on an
  affidavit filed BEFORE constructing**, with "a statement of purpose or
  intended use," and the section "does not affect the authority of the
  governing body … to issue building permits before an affidavit … is filed."
- **§ 17-2-9(3)** hunting and fishing camps — "a private unattached outdoor
  recreational structure"; owner must file a **signed affidavit sworn** with
  the board of supervisors; must be "located in an unincorporated area of the
  county within, near or in close proximity to land upon which hunting or
  fishing activities legally may take place."
- **§ 17-2-9(4)** manufactured housing built to the federal standard.
- **§ 17-2-9(5)** **Pearl River County only** — no enforcement of provisions
  barring, or requiring permit approval for, salvage lumber or green cut timber
  "provided such timber is for personal use and is not for sale."
- **§ 17-2-9(1)–(2)** industrial/pipeline facilities by NAICS code; nonpublic
  fairgrounds and the Neshoba County Fairgrounds.
- **The limit on all of them:** § 17-2-7(5) and § 17-2-9(6), identically — "The
  provisions of this section shall not apply to any floodplain management
  ordinances or regulations necessary for eligibility for the National Flood
  Insurance Program," applying retroactively to permits granted before 22 May
  2012.
- SB 2378 § 1(5) separately excludes manufactured and mobile homes as defined
  in § 75-49-3 from the State Uniform Construction Code.

---

## CLAIMS MANIFEST — every state-specific claim printed, and its authority

| # | Claim | Authority | Doc |
|---|---|---|---|
| 1 | Chapter does not apply to a person building, or acting as own GC on, their own residence; no cost cap | § 73-59-15(1)(b) | MS.1 |
| 2 | Relative exemption (consanguinity/direct affinity, not for sale/rent/public) | § 73-59-15(1)(c) | MS.1 |
| 3 | Owner-in-charge exemption, not for sale/rent/public, not capped by (2) | § 73-59-15(1)(d) | MS.1 |
| 4 | Two residences a year where no building permit is required | § 73-59-15(1)(g) | MS.1, MS.3 |
| 5 | One permit application or residence "within a period of one (1) year" — rolling; rebuttable presumption of building for sale; applies to (1)(b),(c) only | § 73-59-15(2) | MS.1 |
| 6 | "Residential builder" = for sale for another, or for compensation for another over $50,000, ≤3 floors; "remodeler" = improvements over $10,000 | § 73-59-1(b),(c) | MS.1 |
| 7 | Electrical/plumbing/mechanical/HVAC subcontractors of any tier licensed "no matter the dollar amount" | § 73-59-3(1)(d) | MS.1, MS.2, MS.3 |
| 8 | Construction manager engaged by the owner must be licensed; definition excludes the owner by name | § 73-59-3(1)(c); § 73-59-1(h) | MS.1 |
| 9 | Building official shall refuse a permit absent evidence of license or exemption, and shall report | § 73-59-17 | MS.1, MS.2, MS.5 |
| 10 | Person building own residence is not a "residential contractor"; no DOR permit needed | § 73-59-18; § 27-65-27 | MS.1 |
| 11 | Misdemeanor $100–$5,000 and/or 30–60 days; no action to enforce contract; documented expenses by clear and convincing evidence; citation and stop work | § 73-59-9(1),(2),(3) | MS.1 |
| 12 | County codes only in unincorporated areas; adopted code certified and filed with the clerk | § 19-5-9 | MS.1, MS.4 |
| 13 | Municipal adoption by ordinance, certified and filed with the clerk, newspaper notice | § 21-19-25 | MS.1, MS.4 |
| 14 | Statewide code: adopt one of the last three adopted editions of IBC/IRC | SB 2378 (2014) § 1(1) | MS.3, MS.4 |
| 15 | 120-day statewide opt-out by resolution entered on minutes; effective 1 Aug 2014 | SB 2378 (2014) § 1(3) | MS.0, MS.4 |
| 16 | Residential fire sprinkler provisions excluded from the adopted IRC | SB 2378 (2014) § 1(1)(b) | MS.3, MS.4 |
| 17 | Council adopts one of last three editions as discretionary statewide minimum codes; barred from requiring sprinklers; local power to require them preserved | § 17-2-3(5),(7) (2011 HB 1385) | MS.3, MS.4 |
| 18 | Five named coastal counties enforce 2003 IRC/IBC wind and flood on an emergency basis | § 17-2-1 (2006 HB 1406) § 1(1) | MS.3, MS.4 |
| 19 | Coastal 60-day opt-out by resolution | HB 1406 (2006) § 1(4) | MS.4 |
| 20 | NFIP floodplain ordinances unaffected by the code exemptions | § 17-2-7(5); § 17-2-9(6) | MS.2, MS.4, MS.5 |
| 21 | Notice of intent required before constructing or placing the residence | § 41-67-5(1) | MS.2 |
| 22 | No public water utility may connect without prior written department approval; construction connection conditional on inspection before use or occupancy | § 41-67-5(2) | MS.2, MS.4 |
| 23 | Two-acre exemption from approval and from § 41-67-5(2), three conditions incl. installer's affidavit | § 41-67-6(7) | MS.2, MS.5 |
| 24 | Five working days to approve/disapprove; deemed approved after ten calendar days of silence | § 41-67-7(1) | MS.2 |
| 25 | Perpetual maintenance agreement for advanced treatment systems unless qualified homeowner maintenance provider | § 41-67-7(5) | MS.2, MS.5 |
| 26 | Wastewater chapter stands repealed 1 July 2028 unless reenacted | § 41-67-31 (2023 HB 522) | MS.2 |
| 27 | Farm structures exempt only on an affidavit filed before constructing | § 17-2-7(1),(3),(4) | MS.5 |
| 28 | Hunting/fishing camps exempt on sworn affidavit filed with board of supervisors; unincorporated areas | § 17-2-9(3) | MS.5 |
| 29 | Manufactured housing to federal standard; Pearl River salvage/green timber for personal use | § 17-2-9(4),(5) | MS.5 |
| 30 | MSDH five-step process and Form 908 identity | MSDH Form 908 (rev. 21-AUG-17) | MS.2, MS.5 |

---

## DELIBERATELY OMITTED — and why

| Omitted | Reason |
|---|---|
| **All MSDH fee amounts** (Form 908 shows a site-evaluation-plus-final-approval fee, a lower two-acre-exemption fee, and a later-final-approval fee) | The form's revision stamp is **2017**. A nine-year-old fee printed as current in a paid product is precisely the error class this kit exists to avoid. Structure printed, amount is a write-in. |
| **The MSDH roster of water associations / cities / utility districts requiring final approval** | Compiled **13 April 2021** and carries the Department's own caveat that it "may or may not be complete." The kit prints the five *categories* to ask about instead. |
| **Any per-jurisdiction permit fee, timeline, or code edition** | No statewide answer exists; the statute permits three editions concurrently. Write-in lines throughout. |
| **All phone numbers** | House standard. Every directory block carries a rule to write the number the reader confirmed. |
| **Named lists of which counties opted out in 2006/2014** | No official consolidated roster was located (see open questions). Printing a partial or inferred list would be worse than teaching the lookup, which is what MS.4 does. |
| **A claimed statewide IRC edition and effective date** | The "2021 IRC effective 1 July 2024 / 2024 IRC effective 18 May 2026" claim could not be verified against any adopting instrument, and the statutory structure (any of the last three editions, discretionary) contradicts the framing. See open questions. |
| **Deep links to any government page** | Government URLs rot. Domain plus navigation route throughout. |
| **`law.justia.com` as a reader-facing statute source** | Confirmed blocked. The kit sends buyers to legislature.ms.gov, msboc.us, msdh.ms.gov and billstatus.ls.state.ms.us, all verified reachable. |
| **Sealed-plans threshold for one- and two-family dwellings** | Not verified as a statewide rule; MS.2 asks the reader to confirm locally. |
| **Mississippi well permitting specifics** | MDEQ rules not verified to primary text in this pass; MS.4 names the agency and the kit makes no threshold claim. |
| **§ 83-75-1 windstorm-mitigation discount** | Cited by the state guide; not verified here. Not printed. |

---

## OPEN QUESTIONS — for the next revision

1. ~~Has the Building Codes Council adopted any edition?~~ **ANSWERED — no.**
   See the Council section under Trap 3. Remaining sliver: absence was verified
   within Title 19 of the Administrative Code, not across every title. If a
   future revision wants to state it absolutely, sweep the remaining titles.
   Also unresolved: whether the pinpoint codification of SB 2378 § 1 is
   § 17-2-4 (see the codification note under Trap 2) — confirm before printing
   a section number.
2. ~~Is there an official list of the 2006 and 2014 opt-outs?~~ **ANSWERED for
   2014 — no list exists.** MID's Fire Marshal page is a self-reporting form
   and the Department publishes nothing from it. Still open for **2006**: no
   coastal opt-out roster was sought or found. The Association of Supervisors
   or the Municipal League remain the best long shots. The minute-book method
   stays regardless.
3. **Per-jurisdiction verification.** No local permit offices were verified in
   this pass (the local-sampling sub-agent did not report before the kit was
   built). MS.4 was deliberately designed as a *method* rather than a directory,
   which is the more durable design for a state where the answer is
   parcel-specific — but a verified appendix of the ten largest offices, their
   stable domains, and whether each uses MyGovernmentOnline would still add
   value.
4. **What each permit office accepts as "evidence … that he is … exempt"**
   under § 73-59-17. If a common instrument exists (a widely-copied homeowner
   affidavit), naming it would be a strong addition to MS.1 and MS.5.
5. **Electric utility interconnection requirements in no-code counties** — what
   Entergy Mississippi, Mississippi Power, and the cooperatives require before
   setting a meter where no electrical inspector exists. Genuinely
   underdocumented; flagged in MS.2 and MS.4 as a question to ask.
6. **MDEQ domestic well permitting** — whether a household well needs a permit
   or only registration, and any capacity threshold.
7. **Re-verify the whole wastewater chapter after 1 July 2028** (§ 41-67-31).
8. **Mechanic's lien law** (§ 85-7-401 et seq., rewritten 2014) — not verified
   this pass and not printed; a one-paragraph warning would suit MS.1.

---

## FREE SOURCES (for buyers, all verified reachable August 2026)

- **legislature.ms.gov** → Mississippi Code — the official free public code.
  Title 73 Ch. 59 residential builders; Title 17 Ch. 2 building codes; Title 41
  Ch. 67 onsite wastewater; § 19-5-9 and § 21-19-25 county/municipal adoption.
- **msboc.us** → Laws — the whole residential law plus Board rules in one PDF,
  and the license search for verifying trade contractors.
- **msdh.ms.gov** → Regulation → On-Site Wastewater — the wastewater law, the
  regulations, Form 908, and the county-ordinance map.
- **billstatus.ls.state.ms.us** — every enacted bill, which is how the dates and
  the two opt-out windows in this kit were established.
