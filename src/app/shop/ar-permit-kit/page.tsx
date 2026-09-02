import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/ar-permit-kit' },
  title: 'Arkansas Owner-Builder Permit Kit — $34',
  description:
    'Arkansas permit kit: the building permit most counties never created, the three trade exemptions that are three different tests, the 10-acre septic exemption missing from the rule book, and the 2026 NEC with Arkansas amendments. 40 print-ready pages, every claim cited. $34 instant download.',
  keywords:
    'Arkansas building permit, Arkansas owner builder, do I need a building permit in Arkansas, Arkansas Fire Prevention Code, Arkansas owner builder exemption, 17-25-513, Arkansas septic permit, Arkansas homeowner electrical exemption, Arkansas county building department',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const AR: KitContent = {
  slug: 'ar-permit-kit',
  heroSub:
    'Arkansas writes one building code for the whole state, forbids your county from adopting a different one — and then requires nobody to enforce it on your house.',
  pageCount: 40,
  revision: 'September 2026',

  heroSheets: {
    front: {
      src: '/kits/ar/ark-hero-front.webp',
      alt: 'Arkansas Owner-Builder Permit Kit page setting the electrical, plumbing and HVACR homeowner exemptions side by side in a three-column table, showing that one says "primary residence used as", one says "owned and occupied", and the HVACR one says "existing building or structure"',
    },
    back: {
      src: '/kits/ar/ark-hero-back.webp',
      alt: 'Kit page tabulating every Arkansas code edition in force, including the 2026 National Electrical Code, above a checklist for the two editions the kit deliberately refuses to guess at',
    },
  },

  documents: [
    {
      no: 'AR.0',
      pages: '3 pages',
      title: 'Cover & How to Use',
      copy: 'A job-site cover with the fields Arkansas actually makes you resolve, including a Local Building Department line with an explicit instruction to write NONE. Plus the one-page orientation.',
    },
    {
      no: 'AR.1',
      pages: '9 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy: 'The licensing exemption quoted in full, the definition by rule that makes it work for a house you do not live in yet, the four conditions people expect Arkansas to impose and it does not — and the three trade exemptions, which are three different tests. Read this first.',
      thumb: '/kits/ar/ark-exemption.webp',
      caption: 'AR.1 Three exemptions, three different tests',
      alt: 'Page 5 of AR.1: a three-column table setting the Arkansas electrical, plumbing and HVACR homeowner exemptions against each other, with the quoted statutory wording in the middle column and, in the right column, what each phrasing does to a house that is still under construction — noting the HVACR exemption reaches only an existing building',
    },
    {
      no: 'AR.2',
      pages: '10 pages',
      title: 'Permit Application Checklist',
      copy: 'What applies wherever you build, the septic sequence with its published fee table, the 10-acre exemption that lives only in the statute, every code edition in force, what Arkansas deleted from the residential code, and the 2026 NEC amendments that change what you wire.',
      thumb: '/kits/ar/ark-checklist.webp',
      caption: 'AR.2 The exemption that is missing from the rule book',
      alt: 'Page 4 of AR.2: the Arkansas septic plan-review fee table by conditioned square footage, above a bordered callout quoting the ten-acre, two-hundred-foot septic exemption from the statute and explaining that it is absent from the 2024 rule, so county health staff may be unfamiliar with it',
    },
    {
      no: 'AR.3',
      pages: '7 pages',
      title: 'Inspection Sequence',
      copy: 'Split into the approvals that happen wherever you build and the building inspections that happen only where somebody created a permit office. Includes the plumbing inspection Arkansas makes mandatory, the electrical one it makes optional, and an inspection log.',
    },
    {
      no: 'AR.4',
      pages: '6 pages',
      title: 'Where to File Directory',
      copy: 'Arkansas publishes no register of which jurisdictions issue building permits, so this document teaches the ten-minute method that settles it from your county’s own department list — plus the five counties where we ran it, and the offices that exist when no building department does.',
      thumb: '/kits/ar/ark-directory.webp',
      caption: 'AR.4 What the method returned',
      alt: 'Page 2 of AR.4: the closing steps of the ten-minute method for establishing whether a county issues building permits, above a table naming five Arkansas counties and reproducing each one’s published department list to show that none contains a building, planning or permits office',
    },
    {
      no: 'AR.5',
      pages: '5 pages',
      title: 'Forms & Documents Index',
      copy: 'Every document you will meet, named as the issuing office names it, plus the two lists that save the most money: what needs no permit even where permits exist, and what Arkansas never adopted — including the tiny-house appendix.',
    },
  ],

  includes: [
    '40 print-ready pages across 6 documents, letter size',
    'Every Arkansas claim cited on the page it appears on',
    'Write-in lines for everything that depends on your city or county',
    'A permit record, an inspection log and a where-to-file directory for the job site',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things Arkansas law actually says that the standard advice gets wrong. Each takes about a minute to check.',

  highlights: [
    {
      icon: 'permit',
      label: 'Your building permit may never have existed',
      copy: 'Arkansas adopts one code statewide and forbids local governments from adopting another — but nothing makes them enforce it. The code’s own text concedes the choice: jurisdictions may adopt it “should they choose to adopt” more stringent provisions (AFPC Vol. I § 101.2.2). Cities “may” require a permit (§ 14-56-202); counties act under a general services power in which “building codes” is not an enumerated service (§ 14-14-802). Of five counties we checked against their own published department lists, none had a building, planning or permits office.',
    },
    {
      icon: 'check',
      label: 'The three trade exemptions are three different tests',
      copy: 'Every guide says Arkansas lets you do your own electrical, plumbing and HVAC. Read the verbs. Electrical exempts work on “his or her primary residence,” defined as a dwelling “used as” your primary place of residence (§ 17-28-102(b), § 17-28-101(9)). Plumbing needs a building “owned and occupied” as your home (§ 17-38-302(1)). HVACR reaches only an “existing building or structure” (§ 17-33-102(b)(1)) — which on its face is not a house under construction. Two of the three are also expressly subject to local ordinance.',
    },
    {
      icon: 'doc',
      label: 'A septic exemption that is missing from the rule book',
      copy: 'Ark. Code Ann. § 14-236-104(c) exempts a system on a tract of ten acres or larger where the field line is at least 200 feet from every property line — the Department adds “including roads.” It is current law, and it appears nowhere in the 81-page 2024 onsite wastewater rule, so buyers never find it and county staff may not know it. The kit prints both conditions, the nuisance backstop that survives it, and the resale and financing reasons to permit anyway.',
    },
    {
      icon: 'bolt',
      label: 'Arkansas is on the 2026 NEC — with its own amendments',
      copy: 'Not an old edition: 17 CAR § 210-401 adopts NFPA 70, 2026. But it does not adopt it clean, and the changes land in your kitchen and laundry — AFCI and GFCI are not required on dwelling circuits over 130 volts except Articles 680 and 682, do not apply in laundry areas except within six feet of a sink, and do not apply to a refrigerator or microwave. Island and peninsula receptacles get their own Arkansas spacing rule.',
    },
  ],

  sourceNote:
    'Every claim was read against its primary source in September 2026: the Arkansas Code at arkleg.state.ar.us, the Code of Arkansas Rules at codeofarrules.arkansas.gov, the Arkansas Fire Prevention Code’s own adopted text, the Contractors Licensing Board and Board of Electrical Examiners statute books published by the Department of Labor and Licensing, and the Department of Health’s Rules Pertaining to Onsite Wastewater Systems effective 5 September 2024.',

  faqs: [
    {
      question: 'Do you need a building permit to build a house in Arkansas?',
      answer:
        'In much of the state, no. Arkansas has a statewide building code but no statewide building permit and no state residential inspection program. Cities “may” require a permit (Ark. Code Ann. § 14-56-202) and counties act under a general services power in which “building codes” is not among the enumerated services (§ 14-14-802(b)); the county planning subchapter enumerates “zoning, subdivision, setback, or entry control” ordinances and again omits building codes (§ 14-17-207(a)). Every verb is “may.” The code itself concedes the point, describing the Arkansas Fire Prevention Code as the only document available to local jurisdictions “should they choose to adopt” more stringent provisions. Arkansas publishes no register of which jurisdictions permit, so you have to establish it for your own parcel — the kit gives you the method.',
    },
    {
      question: 'Do I need a contractor license to build my own house in Arkansas?',
      answer:
        'No. Ark. Code Ann. § 17-25-513(1) exempts “a person who acts as a residential building contractor in the construction of his or her residence unless he or she builds more than one (1) residence during any calendar year.” The one-per-calendar-year cap is the only condition. “Own residence” is defined by rule to include “a residence constructed for the occupancy of the person who owns the property” (17 CAR § 295-101(6)), which is what makes it work for a house you do not live in yet. The exemption covers acting as your own general contractor, because the defined role expressly includes one who “assumes charge in a supervisory capacity or otherwise manages the construction” (§ 17-25-502(2)). There is no holding period, no not-for-sale window, no affidavit and no dollar limit — the $2,000 figure is a separate exemption for small jobs, and the $50,000 figure is the commercial threshold, which expressly excludes single-family residences.',
    },
    {
      question: 'Can a homeowner do their own electrical, plumbing and HVAC work in Arkansas?',
      answer:
        'All three exemptions exist, but they are worded differently and the differences matter for a house that is not finished. Electrical exempts work on “his or her primary residence,” defined as “an unattached single-family dwelling used as the person’s primary place of residence” (§ 17-28-102(b), § 17-28-101(9)) — present tense. Plumbing covers a building “owned and occupied by him or her as his or her home” (§ 17-38-302(1)). HVACR is narrowest: it reaches work “in an existing building or structure” (§ 17-33-102(b)(1)), which on its face is not new construction. Electrical and plumbing are also expressly subject to local ordinance, and a city or county “may by ordinance require a person, before doing electrical work on his or her primary residence, to demonstrate a technical competency” (§ 17-28-305(b)(2)). Ask each board in writing about your specific situation before you start.',
    },
    {
      question: 'Can I install my own septic system in Arkansas, and do I need a permit?',
      answer:
        'You may install it; you may not design it, and you do need the permit. Ark. Code Ann. § 14-236-102(b)(2) requires installer registration “with the individual homeowner retaining all rights to install and repair his system,” and “installer” is defined as someone who works for compensation for others. But Part I of the application “shall be completed by a Designated Representative” — a private licensed professional you hire (Rules Pertaining to Onsite Wastewater Systems § 4.10.1) — and the system “shall not be used until the Permit for Operation is issued” (§ 4.10.3). The permit comes from the Environmental Health Specialist at your county health unit, and state rule requires the approval “prior to construction of a building or residence” (§ 4.3). Plan-review fees run $30 to $150 by conditioned square footage. There is also a statutory exemption for a system on ten acres or more with every line at least 200 feet from every property line (§ 14-236-104(c)) — real, current, and absent from the rule book.',
    },
    {
      question: 'What building code and NEC edition does Arkansas use in 2026?',
      answer:
        'The Arkansas Fire Prevention Code, 2021 Edition, effective 1 January 2023 as state rule 015.01.22 Ark. Code R. 005. Volume III is the residential one — the 2021 International Residential Code with Arkansas amendments — and it applies to detached one- and two-family dwellings and townhouses up to three stories. Electrical is the 2026 National Electrical Code, adopted at 17 CAR § 210-401 with Arkansas amendments to the AFCI and GFCI requirements and to island and peninsula receptacles. What surprises people is how much Arkansas struck out of Volume III: IRC Chapter 11 energy, Chapter 24 fuel gas, Chapters 25–33 plumbing and Chapters 34–43 electrical are all deleted and replaced by pointers to separate Arkansas codes — and every appendix is deleted, so Arkansas has adopted no tiny-house, strawbale, cob or 3D-printed-construction appendix at state level.',
    },
    {
      question: 'If nobody inspects my house in Arkansas, does the building code still apply?',
      answer:
        'Yes. The Arkansas Fire Prevention Code is adopted statewide and Volume III reaches your dwelling by its own scope (§ R101.2). What is missing in a county with no building department is the inspection, not the standard, and not your liability for falling short of it. Three things also still bite regardless of your county: the onsite wastewater permit, the plumbing code — adopted as “minimum standards statewide in application… rural or urban” (§ 17-38-103), with permits and inspections mandatory wherever a water, sewer or gas utility system exists (§ 17-38-204(c)) — and the 2026 NEC as the performance standard for electrical work. Even the electrical exemption from routine inspection has a sting: a state inspector “may require electrical work to be exposed for inspection, including the removal of sheetrock” where the work was never subject to city inspection and there is evidence of serious violations (17 CAR § 210-1101(a)).',
    },
  ],

  productDescription:
    'A 40-page print-ready permit kit for building your own home in Arkansas, in six documents. Covers the owner-builder licensing exemption under Ark. Code Ann. § 17-25-513 and the rule that defines “own residence”, the local-option building permit and the method for establishing whether one exists on your parcel, the three trade homeowner exemptions and why their wording differs, the onsite wastewater permit sequence including the ten-acre statutory exemption, the current code editions including the 2026 NEC with Arkansas amendments, and what Arkansas deleted from the residential code. Every claim is cited on the page it appears on and was verified against the Arkansas Code, the Code of Arkansas Rules, the Arkansas Fire Prevention Code and the state licensing boards’ own publications in September 2026.',

  verifyNote:
    'Statutes, rules and code editions change, and in Arkansas the building permit itself depends on whether your city or county ever created one. Confirm each rule with the office that will actually handle your parcel — and with the Department of Health for the septic permit, which applies either way. The kit prints its sources so you can.',

  binderLead:
    'The Owner-Builder Job Site Binder picks up where the permit kit stops — and in Arkansas, where much of the state will never send an inspector, the binder is the record that nobody else is keeping. 367 pages of contracts, inspection forms, daily logs and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function ARPermitKit() {
  return <KitProductPage content={AR} />;
}
