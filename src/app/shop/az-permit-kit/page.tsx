import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/az-permit-kit' },
  title: 'Arizona Owner-Builder Permit Kit — $34',
  description:
    'Arizona permit kit: no statewide building code but a county building permit no board of supervisors may waive, the one no-code county and the two opt-out counties, the signed statement on every application that names your licensed subs, the one-year sale rule and the recorded deed that switches it off, the permit clocks that run against cities and not counties, and the septic and well rules that bind every lot. 49 print-ready pages, every claim cited. $34 instant download.',
  keywords:
    'Arizona owner builder permit, Arizona owner builder exemption ARS 32-1121, ARS 32-1169 owner builder statement, Arizona no building code county, Greenlee County no building code, Cochise County owner builder amendment, ARS 11-321 building permit, ARS 33-1002 owner occupant, Arizona septic setback R18-9-A312, ADWR single well license, Arizona 2024 IRC adoption by city',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const AZ: KitContent = {
  slug: 'az-permit-kit',
  heroSub:
    'Arizona adopts no statewide building code, and that one true fact gets turned into “no permit,” “no rules” and “varies locally.” None of those follow. A county building permit is mandatory by statute for any construction over $1,000, the statement you sign with it names every licensed contractor you will use, and the one-year sale rule has an off-switch written into the lien statute: record the deed, move in.',
  pageCount: 49,
  revision: 'September 2026',

  heroSheets: {
    front: {
      src: '/kits/az/azk-hero-front.webp',
      alt: 'Arizona Owner-Builder Permit Kit page quoting A.R.S. § 11-321(A), under which every board of supervisors shall require a building permit for construction exceeding $1,000, followed by a boxed quotation from the Greenlee County Engineer’s letter stating that the county has adopted no building codes, reviews no plans and inspects no construction, yet issues a building permit at no cost because Arizona law requires it',
    },
    back: {
      src: '/kits/az/azk-hero-back.webp',
      alt: 'Kit page quoting A.R.S. § 32-1169 in full — the signed statement every building-permit applicant must file, which for an exempt owner-builder must state the basis of the exemption and the name and license number of every general, mechanical, electrical or plumbing contractor to be employed, with a false statement being unsworn falsification — followed by four bullets on what that means at the counter',
    },
  },

  documents: [
    {
      no: 'AZ.0',
      pages: '3 pages',
      title: 'Cover & How to Use',
      copy: 'A job-site cover with two lines no other state needs — the IRC and NEC editions printed on your permit, because Arizona has no statewide edition of either, and the date your deed was recorded, which has to be earlier than every other date in the kit. And the one-page orientation.',
    },
    {
      no: 'AZ.1',
      pages: '13 pages',
      title: 'The Code Is Local, the Permit Is Not',
      copy: 'The statute that makes a county building permit mandatory everywhere, the one county with no code, and the two counties that let you opt out of inspection but not the permit. Then the exemption paragraph quoted whole and marked at its five moving parts, the owner-occupant status that switches off the one-year presumption and blocks subcontractor liens, who may lawfully help you, the statement you sign, the contract you are owed, and workers’ compensation without a bright line.',
      thumb: '/kits/az/azk-opt-outs.webp',
      caption: 'AZ.1 The two county opt-outs',
      alt: 'Page 4 of AZ.1: a two-column table comparing the Cochise County Owner-Builder Amendment on parcels of four acres or more with the Coconino County Alternative Methods and Materials Permit under 600 square feet — who qualifies, what plan review and inspections are skipped, what survives, the notice recorded against the title, and whether a certificate of occupancy issues',
    },
    {
      no: 'AZ.2',
      pages: '13 pages',
      title: 'Permit Application Checklist',
      copy: 'The IRC, NEC and energy editions actually in force in 15 counties and 20 cities as their own ordinances stated them on 3 September 2026, from the 2003 IRC to the 2024, with a confirm-at-the-counter rule for every cell that could not be closed. The rules that bind every lot regardless of code. The ADEQ septic package with its 100-foot well setback, 50-foot property-line rule and 100 percent reserve area, and the ADWR well package with the no-fee license that lets you drill your own.',
      thumb: '/kits/az/azk-editions.webp',
      caption: 'AZ.2 The county edition map',
      alt: 'Page 2 of AZ.2: a five-column table of Arizona counties from Pima to Gila listing the IRC edition, the NEC edition, the energy code and the adopting ordinance with its effective date for each — 2024 codes in Pima, Yavapai, Cochise and Coconino, 2018 in Pinal, Mohave and Navajo, 2015 in Apache and 2012 in Gila, with cells marked confirm where the county’s own source could not be read',
    },
    {
      no: 'AZ.3',
      pages: '8 pages',
      title: 'Inspection Sequence & Clocks',
      copy: 'The asymmetry nobody prints: a city house permit carries posted time frames, one comprehensive request for corrections, a 15-working-day denial notice, an automatic fee refund and a bar on mid-build plan changes, and a county house permit carries none of it — the county statute carves every residential lot out. The 15-working-day third-party review rule and its catch. The septic authorizations and their two-year life, the certificate of occupancy you may never get, and a log.',
      thumb: '/kits/az/azk-two-regimes.webp',
      caption: 'AZ.3 One house, two regimes',
      alt: 'Page 2 of AZ.3: a table headed “One house, two regimes” setting a city permit against a county permit row by row — review time frame, corrections, denial, refund, mid-build plan changes, inspections and what both owe you — with the county column reading none or no statutory limit at every clock, above the start of the A.R.S. § 9-835 city-clock table',
    },
    {
      no: 'AZ.4',
      pages: '6 pages',
      title: 'Where to File Directory',
      copy: 'All fifteen counties with their building-permit and ADEQ-delegated septic offices as their own sites name them, nine cities where the page was read, the two opt-out counters and the no-code county, the Registrar, ADEQ and ADWR, where the statutes and rules themselves live, the sequence in order, and a page to record every office you confirmed.',
    },
    {
      no: 'AZ.5',
      pages: '6 pages',
      title: 'Forms & Documents Index',
      copy: 'Every document you will meet, named as the statute or agency names it — the exemption statement and its twelve local names, the recorded deed, the twenty-day notices, the ADEQ Notice of Intent and its two authorizations, the ADWR notice and single well license — plus the thirty-day clarification letter that turns any “varies locally” into a dated written answer, what Arizona does not require, and what you may do yourself.',
    },
  ],

  includes: [
    '49 print-ready pages across 6 documents, letter size',
    'Every Arizona claim cited on the page it appears on',
    'The edition map for 15 counties and 20 cities, dated, with write-in lines for your ordinance',
    'A permit record, an inspection log, a clarification-letter template and a confirmed-offices page for the job site',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things Arizona law actually says that the standard advice gets wrong. Each takes about a minute to check.',

  highlights: [
    {
      icon: 'doc',
      label: 'No statewide code — and no county without a permit',
      copy: 'A county building code is optional: the board “may” adopt one and may exempt rural zones from it (A.R.S. § 11-861(A)). The permit is not. “The board of supervisors shall require a building permit for any construction of a building … exceeding a cost of $1,000” (§ 11-321(A)), and a copy of every permit goes to the county assessor and the Department of Revenue. Greenlee County, the one county with no code, says so in its own engineer’s letter: it reviews no plans and inspects nothing, and “Arizona Law requires the County to issue a building permit.” Cochise (parcels of four acres or more, once per five years) and Coconino (under 600 square feet) let you opt out of plan review and inspection — with a notice recorded against your title, and no certificate of occupancy on the no-inspection option.',
    },
    {
      icon: 'permit',
      label: 'The statement you sign is statutory, and a false one is a crime',
      copy: 'Arizona has no statewide owner-builder form, and every guide stops there. A.R.S. § 32-1169(A) requires each permit applicant to file a signed statement, and “if the applicant purports to be exempt from the licensing requirements of this chapter, the statement shall contain the basis of the asserted exemption and the name and license number of any general, mechanical, electrical or plumbing contractor who will be employed on the work.” The counter may demand the Registrar’s signature verifying the exemption. Subsection (B) makes a false statement unsworn falsification under § 13-2704. The affidavit, declaration or verification your city hands you is that section; the form is local, the content is not, and you need your licensed-sub list before you apply.',
    },
    {
      icon: 'check',
      label: 'Record the deed, move in — the one-year rule has an off-switch',
      copy: 'The exemption in A.R.S. § 32-1121(A)(5) makes a sale, a rental “or the offering for sale or rent” within a year of completion “prima facie evidence” you built to sell — rebuttable, and “rent” includes compensation in “labor,” so a helper living in the house is a tenant. Then the clause almost nobody reads: the presumption does not apply “in an action against an owner-occupant as defined in section 33-1002” — a natural person whose deed was “recorded with the county recorder” before construction started and who lives in the house at least thirty days in the year after. The same status blocks every lien “except by a person having executed in writing a contract directly with the owner-occupant” (§ 33-1002(B)). One recording date does both jobs, and nothing can fix it afterward.',
    },
    {
      icon: 'schedule',
      label: 'The permit clocks run against cities, not counties',
      copy: 'A city house permit carries a posted time frame, “one comprehensive written or electronic request for corrections,” a bar on denying a residential application without notice within fifteen working days, an automatic refund of every review fee if the city exceeds its time frame or its one request, and a bar on changing an approved plan mid-build (A.R.S. § 9-835). Cities of 30,000 or more must hand a single-family application to a third-party reviewer after fifteen working days (§ 9-470.01). The county statute removes all of it for any permit “necessary for the construction or development of a residential lot” (§ 11-1605(M)(2)); in unincorporated Arizona the only clock is inspections “at the earliest reasonable time” (§ 11-863(B)). Guides that show counties reviewing faster than cities have it backwards — and the one clock you can start yourself in a county is the § 11-1609 letter, answered in writing within thirty days.',
    },
  ],

  sourceNote:
    'Every claim was read against its primary source in September 2026: the Arizona Revised Statutes on the Legislature’s own site, one section per page; the Arizona Administrative Code section by section, cross-checked against the Secretary of State’s compilation; the Registrar of Contractors’ pages; ADEQ’s own Notice of Intent form; the Cochise County Owner-Builder Amendment and the Greenlee County Engineer’s letter from the counties’ own sites; and the adopting ordinances and code pages of 15 counties and 20 cities.',

  faqs: [
    {
      question: 'Can you build your own house in Arizona without a contractor license?',
      answer:
        'Yes. A.R.S. § 32-1121(A)(5) exempts “owners of property who improve such property or who build … structures … on such property and who do the work themselves, with their own employees or with duly licensed contractors,” if the house is “intended for occupancy solely by the owner” and “not intended for sale or for rent.” The definition of residential contractor expressly excludes “an owner making improvements to the owner’s property pursuant to section 32-1121, subsection A, paragraph 5” (§ 32-1101(A)(10)(b)). Three things come with it. On every building-permit application you file a signed statement of the exemption naming every licensed general, mechanical, electrical and plumbing contractor you will use, and a false statement is unsworn falsification (§ 32-1169). Selling, renting or offering the house within a year of completion is prima facie evidence you built to sell — unless you are an owner-occupant under § 33-1002, meaning your deed was recorded before construction and you live in the house thirty days in the following year. And your helpers must be wage employees or licensed contractors; the under-$1,000 casual-work exemption “does not apply … in any case in which the performance of the work requires a local building permit” (§ 32-1121(A)(14)).',
    },
    {
      question: 'Are there counties in Arizona where you do not need a building permit?',
      answer:
        'No. A.R.S. § 11-321(A) provides that, outside cities with their own permit ordinances, “the board of supervisors shall require a building permit for any construction of a building or an addition to a building exceeding a cost of $1,000.” What varies is whether the permit carries a building code. A county building code is optional under § 11-861(A), and Greenlee County has adopted none: its County Engineer’s posted letter says the county “does not review plans, does not inspect construction, or issue a Certificate of Occupancy,” and then, “With some exceptions, Arizona Law requires the County to issue a building permit. We issue a building permit at no cost when a Zoning Use Permit and Floodplain Permit are issued.” Two counties let a rural owner-builder opt out of plan review and inspection while keeping the permit: Cochise County’s Owner-Builder Amendment on parcels of at least four acres in four-acre zoning, usable once in every five years, with a notice recorded with the County Recorder and no certificate of occupancy on its no-inspection option; and Coconino County’s Alternative Methods and Materials Permit for dwellings of 600 square feet or less. Every statewide rule — the septic general permit, the well rules, the exemption statement — applies in all three exactly as it does in Phoenix.',
    },
    {
      question: 'Can a homeowner do their own electrical and plumbing work in Arizona?',
      answer:
        'At the state level, yes. Arizona licenses contractors, not tradespeople: “Only contractors as defined in this section are licensed and regulated by this chapter” (A.R.S. § 32-1101(B)), Title 32 has no chapter for electricians or plumbers as individuals, and an owner building under § 32-1121(A)(5) is expressly not a residential contractor. The local question is whether your city or county will issue you the trade permit, and every jurisdiction site read for this kit draws the same line: Chandler — “If you own a home that you lease or rent to others, a licensed contractor is required”; Tucson — “Rental units are considered commercial property and all commercial permits require a licensed contractor”; Goodyear — “If you own the house and live in it, you do not need to hire Licensed Contractors … If you own the house and rent it out, Licensed Contractors are required.” That is the statute’s “not intended … for rent,” applied at the counter. Two things you may not delegate to an unlicensed helper regardless: work “connecting to any supply of natural gas, propane or other petroleum or gaseous fuel,” and fire-safety wiring such as interconnected smoke alarms (§ 32-1121(D)). You may do those yourself.',
    },
    {
      question: 'Which building code does Arizona use in 2026?',
      answer:
        'None statewide. No state agency adopts a residential, energy or electrical code; each city and county enacts its own by reference in an adopting ordinance that must be “published in full” and filed with the clerk (A.R.S. § 9-802; § 11-864), and that ordinance — not the building department’s web page — is the authority for what binds your lot. As of 3 September 2026 the spread runs from the 2003 IRC in Graham County to the 2024 IRC in Pima, Yavapai, Coconino and Yuma counties and in Cochise from 1 September 2026, and in Phoenix, Tucson, Mesa, Chandler, Glendale, Tempe, Prescott, Yuma, Lake Havasu City, Surprise, Goodyear and Buckeye. Maricopa County, Pinal, Mohave, Navajo, La Paz, Gilbert, Peoria, Flagstaff, Sierra Vista, Kingman and Casa Grande remain on 2018. The electrical code runs from the 1999 or 2002 NEC in Graham County to the 2023, and Phoenix has deferred enforcement of the 2023 NEC’s HVAC-equipment GFCI rule to 1 March 2027. There is no statewide energy code at all: the state standard reaches public buildings only (§ 34-451), Maricopa County’s residential energy chapter is voluntary, and five counties have none. Transition rules are local too — Tempe accepts 2018 plans through 31 December 2026, Coconino County likewise — so get the grace-period sentence from your ordinance in writing before you choose an edition to design to.',
    },
    {
      question: 'How long does a building permit take in Arizona?',
      answer:
        'It depends on whether the counter is a city or a county, and the difference is statutory. A city “shall have in place an overall time frame during which the municipality will either grant or deny each type of license,” posted on its website; during review it “may make one comprehensive written or electronic request for corrections”; it may not deny a residential application unless it notified you within fifteen working days of submission that denial was possible; if it exceeds its time frame or its one request it “shall refund to the applicant all fees charged for reviewing and acting on the application,” automatically and unwaivably; and it may not change an approved plan while you build to it (A.R.S. § 9-835). In a city of 30,000 or more, a single-family permit application not acted on within fifteen working days may go to a third-party reviewer (§ 9-470.01) — though that clock does not start until the construction documents are approved. A county permit has none of this: § 11-1605(M)(2) exempts every license “necessary for the construction or development of a residential lot” from the county time-frame statute, and the only county clock on a house is inspections “at the earliest reasonable time” (§ 11-863(B)). What a county still owes you is a written clarification of any provision within thirty days of your written request (§ 11-1609). The kit prints the request as a template.',
    },
    {
      question: 'Can I install my own septic system or drill my own well in Arizona?',
      answer:
        'Both, with conditions, and both are state rules that apply in every county. Septic systems run on an ADEQ general Aquifer Protection Permit administered by a delegated county office. For a conventional system the Discharge Authorization issues on an accurate site plan and your certification that the tank passed the watertightness test — no installer license number is required (A.A.C. R18-9-A309(C)(1)) — so an owner who may do the work “themselves” under § 32-1121(A)(5) may install it, subject to the county’s inspection before backfill. An alternative system needs a licensed installation contractor’s ROC number and a designer’s certificate of completion (A309(C)(2)). What you may not do is the site investigation: only a registered engineer, geologist or sanitarian or a Department-certified investigator may (A310(H)). The setbacks that fix your footprint are 100 feet from any well, 50 feet from a property line on a well-served lot unless the neighbor records a waiver, and a reserve area equal to 100 percent of the primary field (R18-9-A312(C), (D)). Wells: an exempt well is one pumping 35 gallons a minute or less; you file a notice of intention to drill with ADWR first, with a county-health-approved site plan on parcels of five acres or less (§ 45-596(F)); and while a licensed driller normally drills, “a person who drills or modifies an exempt well on land owned by that person shall first obtain a single well license … No fee may be charged” (§ 45-595(D)). The license is an examination, passed at 70 percent, valid one year for one well (R12-15-807), and no well may be drilled within 100 feet of a septic system without the Director’s written authorization (R12-15-818).',
    },
  ],

  productDescription:
    'A 49-page print-ready permit kit for building your own home in Arizona, in six documents. Covers the fact that Arizona adopts no statewide building code and the statute that nonetheless makes a county building permit mandatory for any construction over $1,000, the one county with no code, the two counties that let a rural owner-builder opt out of plan review and inspection with a notice recorded against the title, the owner-builder exemption in A.R.S. § 32-1121(A)(5) quoted whole, the signed exemption statement every permit application must carry under § 32-1169 naming every licensed contractor to be used, the owner-occupant status under § 33-1002 that switches off the one-year sale presumption and blocks subcontractor liens, who may lawfully help you, contract contents and the two-year complaint window, the IRC, NEC and energy editions in force in 15 counties and 20 cities as of 3 September 2026, the statewide rules that bind every lot, the city permit clocks and refund under § 9-835 and the county carve-out in § 11-1605(M)(2), the ADEQ septic general permit with its setbacks, sizing and two authorizations, and the ADWR well rules including the no-fee single well license. Every claim is cited on the page it appears on and was verified against the Arizona Revised Statutes, the Arizona Administrative Code and the counties’ and cities’ own ordinances and pages in September 2026.',

  verifyNote:
    'Statutes, rules and code editions change, and several Arizona answers are moving: ADEQ has an onsite wastewater rulemaking in motion that will re-open the septic setback and sizing tables; Coconino County and Tempe stop accepting 2018-code plans on 31 December 2026; Phoenix’s HVAC-GFCI enforcement begins 1 March 2027; Maricopa County and ten other jurisdictions in the kit’s map are still on 2018 codes and may move. Confirm each rule with the office that will handle your parcel — the city inside its limits, the county outside — and ask for the adopting ordinance number. The kit prints its sources so you can.',

  binderLead:
    'The Owner-Builder Job Site Binder picks up where the permit kit stops — and in Arizona, where a no-code county or an opt-out permit will never produce a certificate of occupancy and the only record of the house may be the paper you kept, your own documentation matters more than usual. 367 pages of contracts, inspection forms, daily logs and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function AZPermitKit() {
  return <KitProductPage content={AZ} />;
}
