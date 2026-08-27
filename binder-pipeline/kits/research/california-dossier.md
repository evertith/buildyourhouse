# California Owner-Builder Permit Kit — research dossier

Primary-source research backing `gen_ca_0.py` … `gen_ca_5.py`.
Everything below was read from the source named, not from a summary.
Verified **August 2026**.

Fetch pattern used throughout for statute text (WebFetch garbles these pages):

```
curl -sL -A 'Mozilla/5.0' \
  'https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=BPC&sectionNum=7044.' \
  | python3 -c "import sys,html,re; t=sys.stdin.read(); \
      t=re.sub(r'<script.*?</script>','',t,flags=re.S); \
      t=re.sub(r'<style.*?</style>','',t,flags=re.S); \
      t=re.sub(r'<br[^>]*>','\n',t); t=re.sub(r'<[^>]+>',' ',t); \
      print(html.unescape(re.sub(r'[ \t]+',' ',t)))"
```

---

## 1. B&P § 7044 — the owner-builder exemption

Source: leginfo.legislature.ca.gov, lawCode=BPC sectionNum=7044.
**Amended by Stats. 2016, Ch. 714, Sec. 1 (SB 944). Effective January 1, 2017.**
Text current as of August 2026.

Four separate exemptions live in subdivision (a). They are *alternatives* —
you qualify under one of them, and each has its own conditions.

**§ 7044(a)(1) — build it yourself (or with your own employees)**

> "An owner who builds or improves a structure on his or her property,
> provided that both of the following conditions are met: (A) None of the
> improvements are intended or offered for sale. (B) The property owner
> personally performs all of the work or any work not performed by the owner
> is performed by the owner's employees with wages as their sole
> compensation."

Note "**employees with wages as their sole compensation**" — a helper paid a
share of the profit, or in trade, is not within this branch. And note this
branch has **no numeric cap** on structures.

**§ 7044(a)(2) — contract it out to licensed contractors**

> "(A) The owner directly contracts with licensees who are duly licensed to
> contract for the work of the respective trades involved in completing the
> project. (B) For projects involving single-family residential structures,
> no more than four of these structures are intended or offered for sale in a
> calendar year. **This subparagraph shall not apply if the owner contracts
> with a general contractor for the construction.**"

The four-structure cap sits *only* in this branch, and the final sentence
switches it off entirely when a licensed general contractor is used. Most
summaries report the cap without either qualification.

**§ 7044(a)(3) — improving your own principal residence**

> "A homeowner improving his or her principal place of residence or
> appurtenances thereto, provided that all of the following conditions exist:
> (A) The work is performed prior to sale. (B) The homeowner has actually
> resided in the residence for the 12 months prior to completion of the work.
> (C) The homeowner has not availed himself or herself of the exemption in
> this paragraph **on more than two structures more than once** during any
> three-year period."

This is a *remodel* branch, not a new-construction branch. It is the one that
carries the "resided for 12 months prior to completion" test — a test that
several guides wrongly attach to new construction.

**§ 7044(a)(4)** — nonprofit assisting an owner-builder in a mutual self-help
housing program (H&S § 50692(a), § 50078).

**§ 7044(b) — the two presumptions. This is the part that matters.**

> "(b) In all actions brought under this chapter, both of the following shall
> apply:
> (1) Except as provided in paragraph (2), proof of the sale or offering for
> sale of a structure by or for the owner-builder within one year after
> completion of the structure constitutes a **rebuttable presumption**
> affecting the burden of proof that the structure was undertaken for purposes
> of sale.
> (2) Proof of the sale or offering for sale of **five or more structures** by
> the owner-builder within one year after completion constitutes a
> **conclusive presumption** that the structures were undertaken for purposes
> of sale."

Two findings almost nobody prints:

* The one-year rule is triggered by **offering for sale**, not only by
  selling. Listing the house inside the year is enough.
* At five or more structures the presumption is **conclusive** — meaning it
  cannot be rebutted at all. Every summary that describes § 7044 says
  "rebuttable presumption" full stop and misses (b)(2).

---

## 2. H&S § 19825 — the statutory permit application (the kit's centrepiece)

Source: leginfo, lawCode=HSC sectionNum=19825.

This is the single most useful California find. § 19825(a) sets out the
**text of the permit application itself**, and requires every city and county
in California that issues building permits to use an application "in
substantially the same form." So an owner-builder in Modoc County and one in
San Diego sign materially the same declaration.

> "Every city, county, or city and county, whether general law or chartered,
> that requires the issuance of a permit as a condition precedent to the
> construction … shall require the execution of a permit application, in
> substantially the same form set forth under this subdivision, and require
> any individual who executes the Owner-Builder Declaration to **present
> documentation sufficient to identify the property owner** and, as necessary,
> **verify the signature** of the property owner."

The form contains, in order: Building Project Identification · Licensed
Contractor's Declaration · **Owner-Builder Declaration** · Workers'
Compensation Declaration · Declaration Regarding Construction Lending Agency
· owner certification block.

### The Owner-Builder Declaration — the sentence nobody reads

The declaration is affirmed **under penalty of perjury**, offers three
checkboxes (do the work yourself / employees; contract exclusively with
licensed contractors; other stated basis), and then closes with this
acknowledgment:

> "By my signature below I acknowledge that, **except for my personal
> residence in which I must have resided for at least one year prior to
> completion of the improvements covered by this permit, I cannot legally sell
> a structure that I have built as an owner-builder if it has not been
> constructed in its entirety by licensed contractors.**"

**This is California's trap** — see § 9 below.

### The Workers' Compensation Declaration

Three mutually exclusive options, affirmed under penalty of perjury: a
certificate of consent to self-insure (Lab. § 3700); a workers' comp policy
(carrier, policy number, expiry, agent); **or**

> "I certify that, in the performance of the work for which this permit is
> issued, I shall not employ any person in any manner so as to become subject
> to the workers' compensation laws of California, and agree that, if I should
> become subject to the workers' compensation provisions of Section 3700 of
> the Labor Code, I shall forthwith comply with those provisions."

Printed above it, in the statute, in capitals:

> "WARNING: FAILURE TO SECURE WORKERS' COMPENSATION COVERAGE IS UNLAWFUL, AND
> SHALL SUBJECT AN EMPLOYER TO CRIMINAL PENALTIES AND CIVIL FINES **UP TO ONE
> HUNDRED THOUSAND DOLLARS ($100,000)**, IN ADDITION TO THE COST OF
> COMPENSATION, DAMAGES AS PROVIDED FOR IN SECTION 3706 OF THE LABOR CODE,
> INTEREST, AND ATTORNEY'S FEES."

Note the interaction with § 7044(a)(1): that branch invites you to use "the
owner's employees," and the moment you do, the third checkbox becomes false
and you need a policy.

### § 19825(b) — someone else signing for you

> "When the Permit Application and the Owner-Builder Declaration have been
> executed by a person other than the property owner, prior to issuing the
> permit, the following shall be completed by the property owner and returned
> to the agency responsible for issuing the permit: AUTHORIZATION OF AGENT TO
> ACT ON PROPERTY OWNER'S BEHALF"

Unlike North Carolina (which forbids acting through an agent), California
provides a statutory agent-authorization form. Useful and widely unknown.

### Construction lending agency

The form carries a declaration naming any construction lending agency, citing
**Civil Code § 8172**.

---

## 3. B&P § 7031.5 — what the building department must collect

**Amended by Stats. 1977, Ch. 1052.**

> "Each county or city which requires the issuance of a permit … shall also
> require that each applicant for such a permit file as a condition precedent
> to the issuance of a permit a statement which he has prepared and signed
> stating that the applicant is licensed … or, **if the applicant is exempt
> from the provisions of this chapter, the basis for the alleged exemption.**
> Any violation of this section by any applicant for a permit shall be subject
> to a **civil penalty of not more than five hundred dollars ($500)**."

Precision point: **§ 7031.5 itself does not say "under penalty of perjury."**
The penalty-of-perjury language comes from the form text in H&S § 19825. Cite
§ 19825 for the oath and § 7031.5 for the duty and the $500 civil penalty.

---

## 4. B&P § 7048 — the "minor work" exemption (CURRENT TEXT — the $1,000 rule)

**Amended by Stats. 2025, Ch. 67, Sec. 12 (AB 1170). Effective January 1, 2026.**

> "(a) This chapter does not apply to a work or operation on one undertaking
> or project by one or more contracts if the aggregate contract price for
> labor, materials, and all other items is **less than one thousand dollars
> ($1,000)**, that work or operation being considered of casual, minor, or
> inconsequential nature, **and the work or operation does not require a
> building permit.**
> (b) This section does not apply in a case wherein the work of construction
> is only a part of a larger or major operation … or in which a division of
> the operation is made in contracts of amounts less than one thousand dollars
> ($1,000) for the purpose of evasion of this chapter or otherwise.
> (c) This section does not apply to a person who does either of the
> following: (1) Advertises or puts out a sign or card or other device that
> might indicate to the public that the person is a contractor … (2) **Employs
> another person to perform, or assist in performing, the work or operation.**"

**CITATION — CORRECTED.** An earlier draft of this dossier said AB 2622 was
"superseded." **That was wrong, and it was wrong in the shipped PDF until it was
caught.** The substance is entirely **AB 2622, Stats. 2024, Ch. 240, effective
January 1, 2025** — it raised the threshold from $500 to $1,000, added the "does
not require a building permit" condition, and added the (c)(2) no-employees
condition. The later line on the section, **Stats. 2025, Ch. 67 (AB 1170)**, is
the Legislative Counsel's annual *Maintenance of the codes* bill; its only change
to § 7048 was moving one comma. Independent corroboration: § 7027.2 — AB 2622's
other amended section, untouched by AB 1170 — still reads "(Amended by Stats.
2024, Ch. 240, Sec. 1. **(AB 2622) Effective January 1, 2025**.)"
**AB 2622 has no sunset.** Cite AB 2622 for the rule.

Four conditions, all of which must hold, and (b)/(c) are routinely omitted:
under $1,000 aggregate including materials; no building permit required;
not a slice of a larger project; and the person is working **alone** and does
not hold themselves out as a contractor.

---

## 5. B&P § 7031 — you can claw back what you paid an unlicensed person

**Amended by Stats. 2020, Ch. 312, Sec. 56 (SB 1474). Effective January 1, 2021.**

> "(a) … no person engaged in the business or acting in the capacity of a
> contractor, may bring or maintain any action, or recover in law or equity …
> for the collection of compensation for the performance of any act or
> contract where a license is required by this chapter without alleging that
> they were a duly licensed contractor at all times during the performance …
> **regardless of the merits of the cause of action** …
> (b) … a person who utilizes the services of an unlicensed contractor **may
> bring an action … to recover all compensation paid to the unlicensed
> contractor** for performance of any act or contract."

So the exposure runs the owner's way as well as against them: an unlicensed
contractor cannot sue you for payment, and you can sue to recover **all** of
what you already paid. § 7031(c) additionally voids any security interest
(e.g. a deed of trust) taken by an unlicensed contractor.

---

## 6. B&P § 7028 — unlicensed contracting is a misdemeanor

**Amended by Stats. 2014, Ch. 392, Sec. 3 (SB 315). Effective January 1, 2015.**

* First conviction: fine up to **$5,000**, or up to **six months** county
  jail, or both. (§ 7028(b))
* Second: mandatory fine, the greater of **20% of the contract price** or
  **$5,000**, plus not less than **90 days** county jail absent stated
  reasons. (§ 7028(c))
* Third or subsequent: **$5,000–$10,000** (or 20% of contract price if
  greater) and 90 days to one year. (§ 7028(d))
* Statute of limitations: **four years** from contract proposal, contract,
  completion, or abandonment, whichever is last. (§ 7028(g))
* **§ 7028(h):** "a person who utilized the services of the unlicensed person
  is a **victim of crime** and is eligible … for restitution for economic
  losses, **regardless of whether he or she had knowledge** that the person
  was unlicensed."

---

## 7. B&P § 7026 / § 7057 — what counts as contracting

**§ 7026** (Stats. 2001, Ch. 728): "Contractor" is "synonymous with builder"
and reaches anyone who undertakes to "construct, alter, repair, add to,
subtract from, improve, move, **wreck or demolish**" a structure, "or to do
any part thereof," including scaffolding and site clearing. Demolition and lot
clearing are contracting — relevant if you are clearing a site before you
build.

**§ 7057** (Stats. 2013, Ch. 377): a general building contractor's work
requires "at least two unrelated building trades or crafts." § 7057(c): a
general building contractor **may not** contract for a fire protection system
(§ 7026.12 / § 7026.13) or C-57 well drilling unless separately licensed or
subcontracting to the right licensee — which is why fire sprinklers and wells
come from their own specialty contractors.

---

## 8. H&S § 18938.6 — permit validity (AB 2913)

**Added by Stats. 2018, Ch. 655, Sec. 2 (AB 2913). Effective January 1, 2019.**

> "(a) Every permit shall remain valid for purposes of this part if the work
> on the site authorized by that permit is **commenced within 12 months after
> its issuance**, unless the permittee has abandoned the work authorized by
> the permit.
> (b) A permittee may request an extension of a permit. The building official
> may grant, in writing, one or more extensions of time for periods of **not
> more than 180 days per extension**. The permittee shall request an extension
> … in writing and demonstrate justifiable cause."

**CORRECTION for the live state guide:** § 18938.6 says *nothing* about
"an inspection every 180 days keeps the permit alive." The statutory test is
(i) commence within 12 months and (ii) do not abandon. The 180-day figure in
§ 18938.6 is the length of a **discretionary extension**, not a rolling
inspection clock. The rolling-inspection formulation belongs to the model code
provision as locally adopted, not to AB 2913.

**H&S § 18938.5** (amended by AB 130, Stats. 2025 Ch. 22, effective June 30,
2025) is a *different* rule: it fixes which building standards apply — those
"effective at the local level at the time an application for a building permit
is submitted." That is the statute that locks your code edition at
**application date**. It is not a permit-validity statute, and the live guide
cites it as one.

---

## 9. THE CALIFORNIA TRAP (the marketing hook)

**The declaration you sign is stricter than the statute everyone quotes.**

Every guide to California owner-building explains § 7044(b)(1): sell within a
year of completion and there is a *rebuttable presumption* you built for sale
— you carry the burden, but you can meet it. True, and it is the whole story
those guides tell.

But the document you actually sign, under penalty of perjury, at the permit
counter — whose text is fixed statewide by **H&S § 19825** — says something
materially different:

> "I cannot legally sell a structure that I have built as an owner-builder if
> it has not been constructed in its entirety by licensed contractors" —
> subject only to the carve-out for "my personal residence in which I must
> have resided for at least one year prior to completion of the improvements."

Three ways this differs from the § 7044 story:

1. It is framed as a **flat prohibition**, not a rebuttable presumption.
2. Its escape hatch is **residence for a year before completion of the
   improvements** — not "hold it a year after completion," which is what
   everyone believes the rule to be. Read literally, the year runs *before*
   completion, so a from-scratch new build on raw land cannot satisfy it at
   all.
3. It applies to any structure **not built entirely by licensed contractors** —
   which is precisely the § 7044(a)(1) owner-builder who did the work himself.

And § 7044(b)(2) — the **conclusive** presumption at five or more structures
in a year — is missing from essentially every online summary.

Practical framing for the kit: § 7044 is the law; the § 19825 declaration is
the sworn statement, and it is the sworn statement you are prosecuted on. If
resale inside a year is even possible, resolve it in writing before signing.

---

## 10. Corrections to flag in the live California state guide

`src/app/permitting/state-guides/california/page.mdx` — reported, not edited.
See the report for the full list.

---

## 11. Title 24 — the current edition, and the two renumberings

**The 2025 California Building Standards Code (Title 24) is the edition in
force. Effective January 1, 2026.** Confirmed on the California Energy Code
2025 adoption record: "Official title: 2025 California Energy Code, Title 24,
Part 6. Effective dates: **January 1, 2026 – Present**."

H&S § 18938.5(a) and CRC § 1.1.9 both fix which edition applies to *you*:

> § 1.1.9: "Only those standards approved by the California Building Standards
> Commission that are **effective at the time an application for building
> permit is submitted** shall apply to the plans and specifications for, and to
> the construction performed under, that permit."

So your code edition locks on your **application date**, not your permit date
or your start date. A submittal that slips across a cycle boundary moves your
whole project onto the new code.

### 11a. Model-code base years — read out of the code's OWN referenced standards

The decisive primary source is the California Residential Code's Chapter 44
(Referenced Standards), which names each standard with its edition. This is
better evidence than any agency summary.

| CRC edition | NFPA 70 (National Electrical Code) | NFPA 13D (residential sprinklers) |
|---|---|---|
| 2022 | **70—20** — the 2020 NEC | 13D—22 |
| 2025 | **70—23** — the 2023 NEC | 13D—25 |

Both quoted from the referenced-standards tables, each carrying the note
"* See California Electrical Code for amendments."

So the current **California Electrical Code is built on the 2023 NEC**. Buy the
2023 NEC, not the newest one on the shelf.

### 11b. Chapter 3 was renumbered in the 2025 edition — TRAP

The 2025 CRC reorganised Chapter 3. Two moves matter to a homebuilder:

* **Automatic sprinkler systems: R313 → R309.** In the 2022 CRC the
  requirement sat at R313.2; in the 2025 CRC it is **R309.2**. In the 2025 code
  R313 is now "Ceiling Height." Corroborated twice: the 2022 referenced-
  standards table points NFPA 13D at "R313.1.1, R313.2.1" while the 2025 table
  points the same standard at "**R309.1.1, R309.2.1**."
* Every online article, checklist and county handout citing "CRC R313" for
  sprinklers is now citing a section that says something else entirely.

### 11c. WUI construction moved OUT of the CRC into a new Part 7 — TRAP

2025 CRC § R337 is now only a signpost:

> "**User note:** Provisions for materials and construction methods for
> exterior wildfire exposure are now located in **Part 7, California
> Wildland-Urban Interface Code**. See Section R102.7, Wildland-Urban
> Interface. The provisions of Part 7, California Wildland-Urban Interface Code
> shall apply to buildings and structures built in the wildland-urban
> interface (WUI)."

California created a **new Part 7 of Title 24, the California Wildland-Urban
Interface Code**, in the 2025 edition. Part 7 had previously been vacant. Every
guide that sends you to "CBC Chapter 7A / CRC R337" is describing the old
arrangement.

### 11d. Other CALGreen-derived sections now sitting in CRC Chapter 3

R334 Construction Waste Reduction, Disposal and Recycling · R338 Electric
Vehicle · R340 Pollutant Control.

---

## 12. Fire sprinklers are required in EVERY new California home

2025 CRC **§ R309.2**, "One- and Two-Family Dwellings Automatic Sprinkler
Systems":

> "An automatic sprinkler system shall be installed in one- and two-family
> dwellings."

Exceptions are only: (1) additions or alterations to existing buildings not
already sprinklered; and (2) a detached Accessory Dwelling Unit as defined in
Government Code § 66313, not exceeding 1,200 square feet, on the same lot,
where the existing primary residence has no sprinklers.

**There is no exception for new construction, and none tied to fire hazard
zone.** Design and installation per NFPA 13D—25 or § R309.3 (§ R309.2.1).

This is the single most expensive surprise in the kit, and the live state guide
gets it wrong — it lists sprinklers as "often required" under the WUI section,
implying a fire-zone trigger. The trigger is simply "new dwelling."

Related: B&P § 7057(c) bars even a licensed general building contractor from
contracting for a fire protection system without the classification, so the
sprinkler system comes from its own C-16 specialist.

Note the ADU exception cites **Gov. Code § 66313**; the 2022 CRC cited
§ 65852.2 for the same definition. ADU law was recodified between editions.

---

## 13. Local amendments — CRC § 1.1.8 and § 1.1.8.1

> § 1.1.8: "the provisions of this code do not limit the authority of a city,
> county, or city and county governments to establish **more restrictive** and
> reasonably necessary differences … The effective date of amendments,
> additions or deletions to this code by a city, county, or city and county
> filed pursuant to Section 1.1.8.1 shall be **the date filed**. However, in no
> case shall the amendments … be effective any sooner than the effective date
> of this code."

> § 1.1.8.1: "The city, county, or city and county shall make **express
> findings** for each amendment, addition or deletion based upon **climatic,
> topographical or geological conditions** … [and] shall **file** the
> amendments, additions or deletions, and the findings **with the California
> Building Standards Commission**."

Fire-protection-district findings are ratified locally and filed with **HCD,
Division of Codes and Standards**. Exception to the findings requirement:
hazardous building ordinances and unreinforced-masonry mitigation programs.

Statutory backing: H&S § 17958, § 17958.5, § 17958.7 (State Housing Law),
§ 18941.5 (Building Standards Law), § 13869.7 (fire districts).

Two usable conclusions: local amendments may only be **more** restrictive, and
an amendment is not effective until it has been **filed**. If a requirement is
not in Title 24 and not in a filed local ordinance, ask which one it is under.

---

## 14. Permit validity — H&S § 18938.6, and what the live guide gets wrong

Covered at § 8 above. Short form: **commence within 12 months, do not abandon**;
extensions of up to 180 days each, in writing, for justifiable cause. There is
no statutory "an inspection every 180 days keeps it alive" rule in § 18938.6,
and § 18938.5 is a *which-edition-applies* statute, not a validity statute.

---

## 15. School facilities fees GATE the permit — Education Code § 17620

> § 17620(b): "A city or county … **shall not issue a building permit** for any
> construction absent **certification by the appropriate school district** that
> any fee, charge, dedication, or other requirement levied by the governing
> board of that school district has been complied with, or of the district's
> determination that the fee … does not apply to the construction."

> § 17620(c): if the district has specified the Gov. Code § 66007(a)
> restriction, subdivision (b) does not apply — but then the city or county
> "**shall not conduct a final inspection or issue a certificate of occupancy,
> whichever is later**," without that certification.

So it is a hard gate at one end or the other: either your permit or your
certificate of occupancy. § 17620(a)(1)(B) applies it to **new residential
construction**; (a)(1)(C) reaches other residential work only where the
increase in assessable space exceeds **500 square feet**.

Fee levels are set under **Gov. Code § 65995** and adjusted periodically by the
State Allocation Board. **Do not print a per-square-foot figure** — get the
current rate from the district in writing. (Amended by Stats. 2010, Ch. 541 —
AB 2048.)

---

## 16. Wells and septic

**Wells — Water Code § 13750.5** (Stats. 1996, Ch. 581):

> "No person shall undertake to dig, bore, or drill a water well … to deepen or
> reperforate such a well, or to abandon or destroy such a well, unless the
> person responsible for that construction … possesses a **C-57 Water Well
> Contractor's License**."

**No owner exception.** This is a sharp and useful contrast: § 7044 lets you
wire and plumb your own house, and Water Code § 13750.5 forbids you from
drilling your own well. Reinforced by B&P § 7057(c), which stops even a general
building contractor from taking C-57 work without the classification.

**Septic — the OWTS Policy.** The State Water Resources Control Board's "Water
Quality Control Policy for Siting, Design, Operation and Maintenance of Onsite
Wastewater Treatment Systems" was **adopted April 18, 2023** and **approved by
the Office of Administrative Law on September 26, 2023**
(waterboards.ca.gov/water_issues/programs/owts/). Local agencies implement it,
most through a **Local Agency Management Program (LAMP)** approved by the
Regional Water Quality Control Board; the Board publishes a LAMP contact list
and a public map tool for the Policy's Attachment 2 impaired areas.

---

## 17. Defensible space — two parallel regimes, both amended October 2025

Both amended by **Stats. 2025, Ch. 731 (AB 1455), effective October 13, 2025**.

* **PRC § 4291** — applies in the **State Responsibility Area**.
* **Gov. Code § 51182** — applies in a **Very High Fire Hazard Severity Zone
  designated by a local agency** under § 51179 (i.e. Local Responsibility Area).

Both require the same thing: "**Maintain defensible space of 100 feet** from
each side and from the front and rear of the structure, but not beyond the
property line," with "more intense fuel reductions … utilized between 5 and 30
feet around the structure, and an **ember-resistant zone being required within
5 feet** of the structure, based on regulations promulgated by the board."

### The pre-construction certification nobody mentions

Both § 4291(a)(5) and § 51182(a)(5) require, **before constructing a new
building** in the zone where a permit is required:

> "the owner shall obtain a **certification from the local building official
> that the dwelling or structure, as proposed to be built, complies with all
> applicable state and local building standards**, including those described in
> subdivision (b) of Section 51189, and shall provide a copy of the
> certification, upon request, to the insurer providing **course of
> construction** insurance … Upon completion … the owner shall obtain from the
> local building official a copy of the **final inspection report** that
> demonstrates that the dwelling or structure was constructed in compliance …
> and shall provide a copy of the report, upon request, to the property
> insurance carrier."

This is an owner-builder obligation with a direct insurance consequence, and it
is essentially absent from consumer guides.

### Zone 0 status — hedge carefully

PRC § 4291(g)(1): "The requirement for an ember-resistant zone … **shall not
take effect for new structures until the board updates the regulations** …
and the guidance document." (g)(2): for existing structures, three years after
the effective date for new structures. § 4291(h): CAL FIRE shall not change
inspection practices until the State Fire Marshal makes a written finding that
the Legislature has appropriated sufficient resources.

The statute points at the Board of Forestry's deadline in **Executive Order
N-18-25**. Whether the Board has adopted those regulations as of August 2026 is
the one open question — the kit must state the mechanism and tell the reader to
check current status with the Board of Forestry, not assert a compliance date.

---

## 18. Corrections to flag in the live California state guide

`src/app/permitting/state-guides/california/page.mdx` — **reported, not edited.**

**Wrong / unsupported**

1. **Fire sprinklers.** The guide lists sprinklers only under "Wildfire
   Protection (WUI Zones)" as "Fire sprinklers often required," implying a
   fire-zone trigger. CRC § R309.2 requires an automatic sprinkler system in
   **every new one- and two-family dwelling statewide**. This is the guide's
   most consequential error — it is a five-figure omission from a budget.
2. **CF-1R / CF-2R / CF-3R table.** The guide labels them "Registration form,"
   "Mechanical compliance," "Solar compliance." Those are not what the three
   documents are; the CF1R/CF2R/CF3R family is Certificate of Compliance /
   Installation / Verification. I could not open CEC primary text to confirm
   exact titles, so the kit omits them — but the guide's labels should not
   stand as written.
3. **Permit validity.** The guide says the permit "stays active as long as a
   required inspection is requested and approved within every 180-day window —
   each passed inspection resets the clock," citing AB 2913 and H&S
   §§ 18938.5/18938.6. **H&S § 18938.6 says no such thing.** Its test is
   commencement within 12 months plus no abandonment; its 180 days is the
   maximum length of a *discretionary extension*. And **§ 18938.5 is not a
   permit-validity statute at all** — it fixes which building standards apply.
4. ~~**AB 2622 as the current authority for § 7048.**~~ **RETRACTED — the guide
   is right.** AB 2622 (Stats. 2024, Ch. 240, eff. Jan 1 2025) *is* the
   substantive authority and has no sunset. The later AB 1170 line on the
   section is the annual maintenance-of-the-codes bill and moved a comma. The
   guide's "AB 2622 (2025)" is a slightly loose label for a 2024 bill operative
   in 2025, but the citation and the date are correct.
5. **§ 7044(a)(3) conditions misquoted.** The guide says "not used this
   exemption on more than two structures during any three-year period." The
   statute reads "on more than two structures **more than once** during any
   three-year period."
6. **Septic regulator.** "Regional Water Quality Control Board regulates" is
   the exception, not the rule — in most counties the permit comes from county
   environmental health under an approved LAMP.
7. **Well regulator.** "Department of Water Resources regulates" — DWR sets
   well standards; the permit is local. And the guide never mentions that
   **Water Code § 13750.5 requires a C-57 licensed driller with no owner
   exception**, which is a striking contrast to the DIY electrical it does
   cover.
8. **SMIP fee "$200-$600."** The Strong Motion Instrumentation Program fee for
   residential construction is a small per-valuation charge; a mid-hundreds
   figure for a single house looks wrong by an order of magnitude. Unverified —
   either source it or drop it.

**Stale / now superseded (the 2025 code took effect January 1, 2026)**

9. WUI construction is described as "CBC Chapter 7A / R337." Those provisions
   now live in the **new Title 24 Part 7, California Wildland-Urban Interface
   Code** (2025 CRC § R337 user note).
10. Any reference to sprinklers at **R313** is now the wrong section — it is
    **R309** in the 2025 edition.
11. Defensible space is given as a flat "100 feet of clearance (state law)"
    with no mention of the **two parallel statutes** (PRC § 4291 for the SRA,
    Gov. § 51182 for locally designated Very-High zones), the ember-resistant
    zone, or the **§ 4291(a)(5) pre-construction certification** the owner must
    obtain for the course-of-construction insurer.

17. **"Hire a HERS rater" is now stale.** As of January 1, 2026 the Home Energy
    Rating System Program no longer runs Energy Code compliance; field
    verification moved to the **Energy Code Compliance (ECC) Program** and the
    verifier is an **ECC-Rater**. Any 2026 guidance still saying HERS is wrong.
18. **WUI scope widened.** An emergency action extended the Wildland-Urban
    Interface Code beyond Very High: it now reaches all of the SRA regardless
    of zone class, plus LRA **High** and Very High.

**Missing, and worth adding**

12. **School facilities fees gate the building permit** (Ed. Code § 17620(b)).
    The guide lists school fees only as a dollar range under "Additional Fees"
    and never says the permit cannot issue without the district's certificate.
13. **H&S § 19825** — that the permit application and Owner-Builder Declaration
    are statutory and identical statewide, and the acknowledgment sentence in
    it that is stricter than § 7044 (see § 9 above).
14. **§ 7044(b)(2)'s conclusive presumption** at five or more structures.
15. **Workers' compensation has no employee-count floor in California**
    (Lab. § 3700), and the real threshold for a residential helper is
    **52 hours in the preceding 90 days** (Lab. § 3352(a)(8)). The guide's
    "workers' comp is strongly recommended" understates a statutory duty
    carrying civil fines up to $100,000 and loss of the exclusive remedy.
16. **§ 7031(b)** — the owner may recover **all** compensation paid to an
    unlicensed contractor, and § 7028(h) makes the hirer a crime victim.
19. **H&S § 19825(c)** — the Notice to Property Owner and its twelve initialed
    acknowledgments. A mandatory second document that gates the permit, and the
    guide does not mention it at all.
20. **B&P § 7044.01** — any licensed contractor, contractors' association,
    labor organization, affected consumer, DA or the AG may seek an injunction
    against a non-exempt owner-builder, without proving irreparable injury and
    with attorney's fees. A private enforcement channel the guide omits.
21. **Solar PV is mandatory** on new single-family (2025 Energy Code § 702.3.1,
    formerly § 150.1(c)14), with numeric exemptions at under 80 sq ft of
    solar-available roof and under 1.8 kWdc. The guide says "with exceptions"
    but never says what they are.
22. **Zone 0** — the Board of Forestry adopted the ember-resistant-zone
    regulations on **19 August 2026**, effective on filing (expected ~September
    2026). New buildings comply in full from the effective date, and new vs
    existing turns on permit application date.

**Editorial, not factual:** the cost tables (permit fees, impact fees, seismic
and Title 24 cost deltas, county-by-county examples) carry no sourcing. They
read as estimates. Either source them or label them as the author's estimates —
they are the least defensible content on the page.


---

## 19. Drafted site copy (for `src/app/shop/ca-permit-kit/page.tsx`)

Not applied — the shop page, `kits.ts`, R2 and Stripe are outside this task's
scope. Page renders for `heroSheets` / `thumb` do not exist yet; the paths below
follow the schema's convention for kits after the first four
(`/kits/<code>/*.webp`).

### kits.ts hook

```
hook: 'Sprinklers in every new home, the 2023 NEC, the declaration that is stricter than § 7044, and 52 hours that makes a helper your employee.',
```

### SEO metadata

```ts
export const metadata: Metadata = {
  alternates: { canonical: '/shop/ca-permit-kit' },
  title: 'California Owner-Builder Permit Kit — $34',
  description:
    'Every permit, form, and inspection California requires of an owner-builder: the B&P § 7044 exemption walkthrough, the statutory Owner-Builder Declaration, permit application checklist, inspection sequence, and where-to-file directory. 38 print-ready pages with the statute citations on the page. $34 instant download.',
  keywords:
    'California owner builder permit, B&P 7044 exemption, owner builder declaration California, CA building permit checklist, California inspection sequence, Title 24 owner builder',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};
```

### KitContent

```ts
const CA: KitContent = {
  slug: 'ca-permit-kit',
  heroSub:
    'Every permit, form, and inspection California requires of an owner-builder — verified against the statutes and the 2025 Title 24, citations printed on the page.',
  pageCount: 38,
  revision: 'August 2026',

  heroSheets: {
    front: {
      src: '/kits/ca/cak-exempt.webp',
      alt: 'The California owner-builder exemption walkthrough, page CA.1 of the permit kit.',
    },
    back: {
      src: '/kits/ca/cak-checklist.webp',
      alt: 'A page of the CA permit application checklist stacked behind the exemption walkthrough.',
    },
  },

  documents: [
    {
      no: 'CA.0',
      pages: '2 pages',
      title: 'Cover & How to Use',
      copy:
        'What is in the kit, what order to work through it, and which documents you file versus which you keep on the truck.',
    },
    {
      no: 'CA.1',
      pages: '9 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy:
        'Business and Professions Code § 7044 is four separate exemptions with different conditions, and picking the wrong one is how owner-builders get caught. This walks each branch, the Owner-Builder Declaration you sign under penalty of perjury, and the sale rule — including the conclusive presumption almost nobody prints.',
      thumb: '/kits/ca/cak-exempt.webp',
      caption: 'CA.1 Exemption walkthrough',
      alt: 'Page CA.1, the Owner-Builder Exemption Walkthrough: the four § 7044 branches set out in a table with the statutory conditions and the California code sections printed beside each.',
    },
    {
      no: 'CA.2',
      pages: '11 pages',
      title: 'Permit Application Checklist',
      copy:
        'Everything the counter wants, in the order they ask for it: the statutory application and its declarations, the school district certificate that gates your permit, Title 24 energy compliance, fire sprinklers, wildfire zone, septic and well, grading and stormwater. Check the boxes and you have a complete application.',
      thumb: '/kits/ca/cak-checklist.webp',
      caption: 'CA.2 Application checklist',
      alt: 'Page CA.2, the Permit Application Checklist: a ruled list of application documents with checkboxes and columns for the date each item was filed.',
    },
    {
      no: 'CA.3',
      pages: '6 pages',
      title: 'Inspection Sequence',
      copy:
        'Every inspection California calls for, in the order it is called, with what has to be finished before you schedule it — including the two California adds nobody expects: framing moisture content, and balcony waterproofing that may not be covered until it is inspected.',
      thumb: '/kits/ca/cak-inspect.webp',
      caption: 'CA.3 Inspection sequence',
      alt: 'Page CA.3, the Inspection Sequence: California inspections listed in call order with the prerequisites for each and space to record the date passed.',
    },
    {
      no: 'CA.4',
      pages: '4 pages',
      title: 'Where-to-File Directory',
      copy:
        'Which office handles which piece: city or county building, planning, county environmental health for septic and wells, the fire authority, the school district, and the regional water board. How to find each one for your parcel, and a page to write down what you confirmed.',
    },
    {
      no: 'CA.5',
      pages: '3 pages',
      title: 'Forms & Documents Index',
      copy:
        'Every document referenced in the kit, with what it is, when you need it, and the office it comes from, so you can pull a current copy yourself.',
    },
  ],

  includes: [
    '38 print-ready pages across 6 documents, letter size',
    'The B&P § 7044 exemption walkthrough — all four branches, not one',
    'A permit application checklist you can work straight through',
    'The full inspection sequence, in the order California calls it',
    'Where-to-file directory: building, environmental health, fire, school district',
    'Statute and code citations printed on the page, not linked away',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things in this kit that most California owner-builder advice gets wrong. Each one is checkable in a couple of minutes — which is the point of printing the citation.',

  highlights: [
    {
      icon: 'permit',
      label: 'Every new California home needs fire sprinklers',
      copy:
        'Guides list residential sprinklers under wildfire zones, as though a fire hazard designation triggered them. California Residential Code § R309.2 requires an automatic sprinkler system in every new one- and two-family dwelling, statewide, with no new-construction exception. It also moved: it was § R313.2 until the 2025 code renumbered Chapter 3 on January 1, 2026, so every checklist still citing R313 points at the wrong section. The kit gives the current number and tells you it drives your water service and pump sizing.',
    },
    {
      icon: 'bolt',
      label: 'Your house is wired to the 2023 NEC',
      copy:
        'California’s electrical code always trails the national one, and the cleanest proof is the Residential Code’s own referenced-standards table: the 2025 edition lists NFPA 70—23, where the 2022 edition listed 70—20. So the current California Electrical Code is built on the 2023 NEC with California amendments on top. Buy the 2023 book, not the newest one on the shelf — a newer NEC will disagree with your inspector in exactly the places that get red-tagged.',
    },
    {
      icon: 'doc',
      label: 'You sign two documents, and nobody mentions the second',
      copy:
        'Everyone explains § 7044(b): sell within a year and a rebuttable presumption arises. True — but the Owner-Builder Declaration you actually sign under penalty of perjury, whose wording Health and Safety Code § 19825 fixes for every city and county in California, is worded as a flat prohibition on selling a structure not built entirely by licensed contractors, with an escape hatch that runs backwards. And § 19825(c) requires a second document nobody warns you about: a Notice to Property Owner with twelve statements you must initial one at a time, on your building department’s own letterhead, signed and returned — “a permit shall not be issued unless the property owner complies with this section.” The kit prints both, and the four acknowledgments in the second one that are admissions about your own liability.',
    },
    {
      icon: 'check',
      label: '52 hours makes a helper your employee',
      copy:
        'California has no three-employee floor for workers’ compensation — Labor Code § 3700 reaches every employer. The exclusion for a residential helper in § 3352(a)(8) turns on either under 52 hours or not more than $100 in the 90 days before an injury, so on a house build the real line is 52 hours, about a week and a half. Get it wrong and you face civil fines up to $100,000 and an uncapped tort suit, because § 3706 strips the exclusive remedy. The kit prints the thresholds exactly.',
    },
  ],

  sourceNote:
    'Verified against leginfo.legislature.ca.gov, the 2025 California Building Standards Code, CAL FIRE and State Water Board sources, August 2026 · Citations printed on each page',

  faqs: [
    {
      question: 'Do I need a contractor’s license to build my own house in California?',
      answer:
        'No. Business and Professions Code § 7044 takes owners out of the Contractors State License Law entirely, at any project cost — California sets no dollar threshold above which an owner needs a licensed general contractor. What § 7044 actually contains is four separate exemptions with different conditions, and the one that fits a new build asks that none of the improvements are intended or offered for sale and that any work you do not do yourself is done by your own employees on wages. You claim it by signing an Owner-Builder Declaration under penalty of perjury when you pull the permit. The kit walks each branch with the statute cited on the page.',
    },
    {
      question: 'Can I sell a house I built as an owner-builder in California?',
      answer:
        'Carefully. Under § 7044(b)(1), selling or even offering for sale within one year of completion raises a rebuttable presumption that you built for sale — survivable with good records. At five or more structures within a year the presumption becomes conclusive, which cannot be rebutted at all. Separately, the declaration you sign at the counter says something stricter than the statute: that you cannot legally sell a structure built as an owner-builder unless it was constructed in its entirety by licensed contractors, excepting a personal residence you lived in for a year before completion. If resale inside a year is even possible, get your building department’s position in writing first.',
    },
    {
      question: 'Do I really need fire sprinklers in a new California house?',
      answer:
        'Yes. California Residential Code § R309.2 requires an automatic sprinkler system in every new one- and two-family dwelling, statewide. There is no exception for new construction and no fire-zone trigger — the only exceptions are additions to existing unsprinklered buildings and a small detached accessory dwelling unit. Design it in from the start, because it drives your water service size, your pressure, and on a well your tank and pump. Note also that even a licensed general contractor cannot contract for a fire protection system without the right classification, so it comes from a sprinkler specialist.',
    },
    {
      question: 'Can an owner-builder do their own electrical and plumbing in California?',
      answer:
        'Generally yes. The C-10, C-36 and C-20 classifications are classifications of contractor’s license, and § 7044 exempts you from the licensing chapter as a whole, so they govern the people you hire rather than the work you do yourself. Every trade still needs a permit and an inspection whoever performs it. Two jobs are different: fire sprinkler systems, and drilling a water well — Water Code § 13750.5 requires a C-57 licensed driller with no owner exception at all. Some jurisdictions also restrict owner self-performed work on the main service or gas piping, so ask before you plan the work.',
    },
    {
      question: 'What gates a California building permit besides the plans?',
      answer:
        'Three things people miss. The school district must certify that its facilities fee has been paid or does not apply — Education Code § 17620(b) forbids the city or county from issuing the permit without it, and the district is a separate office on separate hours. The application itself is a statutory form under Health and Safety Code § 19825, so you must present identification proving you are the owner on title, and anyone signing for you needs an Authorization of Agent returned before issuance. And your code edition locks on the date you submit, not the date you break ground. The kit puts all three at the front of the checklist.',
    },
    {
      question: 'Which building code edition applies to my project?',
      answer:
        'The 2025 California Building Standards Code took effect January 1, 2026, but the edition that governs your project is the one effective when your application was submitted — Health and Safety Code § 18938.5 and California Residential Code § 1.1.9 both say so. That is worth writing down, because a submittal that slips across a cycle boundary moves the whole job onto a new code. Your city or county may also amend Title 24, but only to make it more restrictive, only on express climatic, topographical or geological findings, and only once filed with the Building Standards Commission. If you are told something is required and it is not in Title 24, ask which filed amendment it is under.',
    },
  ],

  productDescription:
    'California owner-builder permitting, start to finish: the B&P § 7044 exemption walkthrough covering all four branches, the statutory Owner-Builder Declaration under H&S § 19825, permit application checklist, inspection sequence, where-to-file directory, and forms index. 38 print-ready pages across 6 documents, with the statute and code citations printed on the page. Verified against leginfo.legislature.ca.gov, the 2025 California Building Standards Code, CAL FIRE and State Water Board sources, August 2026.',

  verifyNote:
    'Statutes and code editions change, and California cities and counties amend Title 24 locally. Confirm each rule with the city or county building department that will issue your permit — the kit prints its sources so you can.',
};
```
