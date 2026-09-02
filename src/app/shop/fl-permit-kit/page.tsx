import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/fl-permit-kit' },
  title: 'Florida Owner-Builder Permit Kit — $34',
  description:
    'Florida permit kit: the two owner-builder exemptions with two different sale tests, the Notice of Commencement that gates your first inspection, the product approval number every window needs, and the septic permit that comes before your building permit. 45 print-ready pages, every claim cited. $34 instant download.',
  keywords:
    'Florida owner builder permit, Florida building permit, owner builder exemption Florida, 489.103(7), Notice of Commencement Florida, Florida product approval, Florida Building Code 8th Edition, Florida septic permit DEP',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const FL: KitContent = {
  slug: 'fl-permit-kit',
  heroSub:
    'Florida does not ask whether anyone will inspect your house. It asks how many separate offices have to say yes before the building department will even look at you.',
  pageCount: 45,
  revision: 'September 2026',

  heroSheets: {
    front: {
      src: '/kits/fl/flk-hero-front.webp',
      alt: 'Florida Owner-Builder Permit Kit page setting the Part I general contracting exemption beside the Part II electrical exemption, showing that one is triggered by the sale of any structure within a year and the other only by more than one',
    },
    back: {
      src: '/kits/fl/flk-hero-back.webp',
      alt: 'Kit page listing the Florida Building Code editions in force above a note explaining why the referenced electrical code reads as 2020 in one document and 2023 in another',
    },
  },

  documents: [
    {
      no: 'FL.0',
      pages: '3 pages',
      title: 'Cover & How to Use',
      copy: 'A job-site cover with the fields Florida actually makes you resolve — including a Clerk of Court line, because the office that records your Notice of Commencement is a permitting contact here. Plus the one-page orientation.',
    },
    {
      no: 'FL.1',
      pages: '10 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy: 'Florida gives you two exemptions, not one, in two different parts of the same chapter — and they do not say the same thing. The side-by-side comparison, all twelve paragraphs of the disclosure statement you sign, and the one place two Florida statutes openly contradict each other.',
      thumb: '/kits/fl/flk-exemption.webp',
      caption: 'FL.1 Two exemptions, two different sale tests',
      alt: 'Page 2 of FL.1: a table setting the Part I general contracting exemption against the Part II electrical exemption, showing that Part I is triggered by the sale of any such structure within a year and creates a presumption, while Part II is triggered only by more than one and is prima facie evidence',
    },
    {
      no: 'FL.2',
      pages: '10 pages',
      title: 'Permit Application Checklist',
      copy: 'Every code edition in force, the approval number every exterior window and door needs before it can be permitted, the wind test that catches inland lakefront lots, the blower door limit, and the statutory clock that discounts your permit fee by ten percent for every business day the county runs late.',
      thumb: '/kits/fl/flk-checklist.webp',
      caption: 'FL.2 What is actually in force in Florida',
      alt: 'Page 1 of FL.2: the table of code editions in force — the 8th Edition 2023 Florida Building Code based on the 2021 IRC, energy on the 2021 IECC, wind on ASCE 7-22, a separate Test Protocols volume for the High-Velocity Hurricane Zone — with the electrical row pointing to a note about the 2020 and 2023 editions of the NEC',
    },
    {
      no: 'FL.3',
      pages: '8 pages',
      title: 'Inspection Sequence',
      copy: 'Built around the gates rather than the list. The notice you record at the courthouse before anyone will inspect you, the septic approval that has to exist before your building permit does, the statewide inspection list, and a log.',
      thumb: '/kits/fl/flk-inspections.webp',
      caption: 'FL.3 The document that gates your first inspection',
      alt: 'Page 1 of FL.3, quoting the statute that bars the building department or a private provider from performing or approving inspections until a copy of the recorded Notice of Commencement is filed, above a table of the six things to get right including recording before work starts and the ninety-day window',
    },
    {
      no: 'FL.4',
      pages: '8 pages',
      title: 'Where to File Directory',
      copy: 'How to establish which of Florida’s 400-plus municipalities or 67 counties actually has your parcel, the filing order on a rural lot, which office issues your septic permit in 2026 — the answer is genuinely split — and the five water management districts.',
    },
    {
      no: 'FL.5',
      pages: '6 pages',
      title: 'Forms & Documents Index',
      copy: 'Every document you will meet, named as the agency names it. Plus the construction lien paperwork, which is yours now: as your own contractor, the documents that normally protect an owner have nobody to come from.',
    },
  ],

  includes: [
    '45 print-ready pages across 6 documents, letter size',
    'Every Florida claim cited on the page it appears on',
    'Write-in lines for everything that varies by county',
    'A permit record, an inspection log and a confirmed-offices page for the job site',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things Florida law actually says that the standard advice gets wrong. Each takes about a minute to check.',

  highlights: [
    {
      icon: 'permit',
      label: 'There are two exemptions, not one',
      copy: 'Chapter 489 is split. Part I licenses the thirteen contractor categories at § 489.105(3) — including plumbing, roofing and mechanical. Electrical is not among them; it sits in Part II. So the owner-builder exemption at § 489.103(7) cannot reach your wiring, and § 489.503(6) carries a second one. They do not match: Part I is tripped by the sale of “any such structure” within a year and “creates a presumption,” while Part II needs “more than one” and is “prima facie evidence.” Clearing one does not clear the other.',
    },
    {
      icon: 'check',
      label: 'A courthouse filing gates your first inspection',
      copy: 'The Notice of Commencement is recorded with the clerk of the circuit court, not the building department. Without a copy on file, “the issuing authority or a private provider performing inspection services may not perform or approve subsequent inspections” (§ 713.135(1)(e)1.). But the same statute bars the department from requiring it to issue the permit. Three different dollar thresholds apply — $2,500 to record, $5,000 to file, and a $15,000 HVAC carve-out — and they are not the same number.',
    },
    {
      icon: 'doc',
      label: 'Every exterior opening needs an approval number',
      copy: 'Florida approves products at the state level, and § 553.842(5) names the categories: “panel walls, exterior doors, roofing, skylights, windows, shutters, impact protective systems, and structural components.” At plan review you identify an FL number for each one. That makes it a purchasing constraint, not paperwork — a window with no Florida approval cannot be permitted here. The upside: statewide approval “shall preclude local jurisdictions from requiring further testing.”',
    },
    {
      icon: 'bolt',
      label: 'The county is on a clock, and late costs them',
      copy: 'Section 553.792 gives a local government 30 business days to review a residential permit on a structure under 7,500 square feet, and 5 business days to tell you what is missing — miss that and your application is automatically deemed complete. Run past the review deadline and the permit fee drops 10% for every business day late, rising to 20% on a second review. Almost no owner-builder starts this clock deliberately or notices when it is missed.',
    },
  ],

  sourceNote:
    'Every claim was read against its primary source in September 2026: the Florida Statutes at flsenate.gov, the Florida Administrative Code at flrules.org, and the Florida Building Commission’s own code editions, analyses of changes and product approval system at floridabuilding.org — plus the Department of Environmental Protection’s own county-by-county septic permitting pages.',

  faqs: [
    {
      question: 'Can you build your own house in Florida without a contractor license?',
      answer:
        'Yes. Section 489.103(7), Fla. Stat. exempts owners of property acting as their own contractor and “providing direct, onsite supervision themselves of all work not performed by licensed contractors” when building a one-family or two-family residence or a farm outbuilding for their own occupancy or use and not offered for sale or lease. There is no square-footage cap, no dollar cap and no frequency limit — the $75,000 figure in the statute applies to commercial buildings only. What the exemption does require is that you personally appear and sign the permit application, sign a twelve-paragraph disclosure statement, and satisfy the agency’s identity verification at issuance, which may be a driver license copy, a notarized signature, or another method it accepts.',
    },
    {
      question: 'Can a homeowner do their own electrical and plumbing work in Florida?',
      answer:
        'Yes, but under two different exemptions. Plumbing, mechanical, air-conditioning and roofing are all licensed inside Part I of chapter 489, and § 489.103 opens “This part does not apply to” owners acting as their own contractor — so when Part I stops applying to you, it stops applying for those trades. Electrical is licensed separately under Part II, which is why it needs its own exemption at § 489.503(6), with its own disclosure statement and its own limits. Either way you still pull permits and pass every inspection, and anyone you pay to perform a licensed trade must hold that license. Building departments vary in how readily they accept owner-performed trade work, so ask yours before you plan a schedule around it.',
    },
    {
      question: 'What is the Florida owner-builder one-year rule?',
      answer:
        'It is a hold-and-occupy rule, not a limit of one permit per year — and Florida actually has two different one-year clocks. Under § 489.103(7)(a)1., selling or leasing the structure within one year after completion “creates a presumption that the construction was undertaken for purposes of sale or lease,” which violates the exemption. The electrical exemption sets a different test: § 489.503(6)(a) is only triggered by selling or leasing more than one such structure within a year, and makes it prima facie evidence rather than a presumption. Separately, the workers’ compensation statute at § 440.02(10) runs its own one-year clock from the commencement of construction rather than from completion — so on a fourteen-month build those clocks expire months apart.',
    },
    {
      question: 'Do I need a Notice of Commencement in Florida?',
      answer:
        'For a house, yes, and the sequencing matters more than the form. You record it with the clerk of the circuit court before commencing work, post a certified copy or notarized statement at the site, and file a copy with the building department before the first inspection. Until that copy is filed, § 713.135(1)(e)1. bars the building department or a private provider from performing or approving inspections. Three thresholds apply and they are commonly conflated: recording is required above $2,500 (§ 713.02(5)), filing a copy with the department above $5,000, and § 713.135(1) does not reach an HVAC repair or replacement contract under $15,000. The notice is void if work does not start within 90 days of recording, and it expires one year after recording unless it says otherwise — payments you make after it expires are “improper payments” and can result in paying twice.',
    },
    {
      question: 'Who issues septic permits in Florida — the health department or DEP?',
      answer:
        'Both, depending on your county, which is why most guides get this wrong in one direction or the other. The onsite sewage program transferred from the Department of Health to the Department of Environmental Protection effective 1 July 2021 under the Clean Waterways Act (ch. 2020-150, Laws of Florida), but the transfer is being implemented county by county and is not finished. As of September 2026, DEP issues permits directly in 17 counties — Bay, Calhoun, Escambia, Franklin, Gadsden, Gulf, Holmes, Jackson, Jefferson, Leon, Liberty, Marion, Okaloosa, Santa Rosa, Wakulla, Walton and Washington — and in the other 50, including every major metro, you file with your county health department’s Environmental Health program. The rule chapter was renumbered from 64E-6 to 62-6, F.A.C. in the same move. One thing that does not vary: under § 381.0065(4) no building or plumbing permit may issue until you hold the septic construction permit, and occupancy cannot be authorized until final installation is approved.',
    },
    {
      question: 'Which Florida Building Code is in effect in 2026?',
      answer:
        'The 8th Edition (2023), effective 31 December 2023. The Residential volume is based on the 2021 IRC, the Energy Conservation volume on the 2021 IECC, and wind design moved to ASCE 7-22 in this edition. The 9th Edition (2026) exists only as a draft on the Commission’s own code menu, with a comment period still running in late 2026 and no published effective date — so treat any guide that gives you one with suspicion. The electrical answer is genuinely split: the 8th Edition as adopted referenced the 2020 NEC, and the Commission has since updated the referenced standard to the 2023 NEC using a fast-track power the Legislature gave it specifically for the electrical code. Ask your electrical plan reviewer which edition your permit is reviewed against, and write down what they say.',
    },
  ],

  productDescription:
    'A 45-page print-ready permit kit for building your own home in Florida, in six documents. Covers both owner-builder exemptions — the general contracting exemption at § 489.103(7) and the separate electrical exemption at § 489.503(6), which set different limits — the twelve-paragraph disclosure statement you sign in person, Florida Product Approval and the FL number every exterior opening needs, the windborne debris region that now reaches some inland lakefront lots, the Notice of Commencement that gates your first inspection, the statutory plan review clock and its fee reductions, the private provider alternative, and the county-by-county split in septic permitting. Every claim is cited on the page it appears on and was verified against the Florida Statutes, the Florida Administrative Code and the Florida Building Commission’s own documents in September 2026.',

  verifyNote:
    'Statutes, rules and code editions change, and Florida has two answers moving right now: the 9th Edition of the building code is in draft, and septic permitting is transferring to the Department of Environmental Protection county by county. Confirm each rule with the office that will handle your parcel — your building department, and separately your septic and well offices. The kit prints its sources so you can.',

  binderLead:
    'The Owner-Builder Job Site Binder picks up where the permit kit stops — and in Florida the permit is only the first of the offices you will deal with. 367 pages of contracts, inspection forms, daily logs and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function FLPermitKit() {
  return <KitProductPage content={FL} />;
}
