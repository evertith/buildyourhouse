import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/ms-permit-kit' },
  title: 'Mississippi Owner-Builder Permit Kit — $34',
  description:
    'Every permit, form, and approval Mississippi requires of an owner-builder: the § 73-59-15 exemption walkthrough, how to find out whether any building code binds your parcel, the wastewater approval that applies even where none does, inspection sequence, and where-to-file directory. 36 print-ready pages with the statute citations on the page. $34 instant download.',
  keywords:
    'Mississippi owner builder permit, MS building permit checklist, Mississippi owner builder exemption, Miss Code 73-59-15, Mississippi no building code county, Mississippi septic permit, Mississippi residential builder license, Mississippi coastal wind code',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const MS: KitContent = {
  slug: 'ms-permit-kit',
  heroSub:
    'In Mississippi the first question is not where to file — it is whether any building code binds your parcel at all. That was decided by a vote in 2006 or 2014, and this kit shows you how to go and read it.',
  pageCount: 36,
  revision: 'August 2026',

  heroSheets: {
    front: {
      src: '/kits/ms/msk-exempt.webp',
      alt: 'The Mississippi owner-builder exemption walkthrough, page MS.1 of the permit kit.',
    },
    back: {
      src: '/kits/ms/msk-directory.webp',
      alt: 'A page of the Mississippi where-to-file directory stacked behind the exemption walkthrough.',
    },
  },

  documents: [
    {
      no: 'MS.0',
      pages: '2 pages',
      title: 'Cover & How to Use',
      copy:
        'What is in the kit and what order to work it — starting with why, in this state, establishing your code status comes before everything practical.',
    },
    {
      no: 'MS.1',
      pages: '9 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy:
        'The four separate exemptions in § 73-59-15 and how they differ, the twelve-month limit that is rolling rather than calendar, and the zero-dollar licensing rule that applies to every trade contractor you hire. Statute quoted and cited on the page.',
      thumb: '/kits/ms/msk-exempt.webp',
      caption: 'MS.1 Exemption walkthrough',
      alt: 'Page 2 of MS.1, the Owner-Builder Exemption Walkthrough: the table comparing the four Mississippi exemptions that can cover an owner-builder, with the statutory wording and the one-a-year limit beside each.',
    },
    {
      no: 'MS.2',
      pages: '7 pages',
      title: 'Permit Application Checklist',
      copy:
        'Built the way Mississippi actually works: the wastewater approval first, because it binds every parcel and locks your water meter, then the building permit if your parcel has one — and a full checklist of what still applies when it does not.',
      thumb: '/kits/ms/msk-checklist.webp',
      caption: 'MS.2 Application checklist',
      alt: 'Page 2 of MS.2, the Permit Application Checklist: the two statutory sentences governing onsite wastewater quoted in a bordered callout, above the five-step table of what the health department issues at each stage.',
    },
    {
      no: 'MS.3',
      pages: '6 pages',
      title: 'Inspection Sequence',
      copy:
        'The order inspections happen in and what each one checks, with dated fields to record them — plus, for the large part of Mississippi where nobody is coming, how to buy the same milestones privately and why your lender and insurer still want them.',
    },
    {
      no: 'MS.4',
      pages: '7 pages',
      title: 'Where to File Directory',
      copy:
        'How to establish whether any code binds your parcel, from public records you are entitled to see — the filed code and the opt-out resolution — plus the offices that apply regardless of your code status, and a page to write down what you confirmed.',
      thumb: '/kits/ms/msk-directory.webp',
      caption: 'MS.4 Where-to-file directory',
      alt: 'Page 2 of MS.4, the Where to File Directory: the checklist of four calls and one visit that establishes a parcel’s building-code status, quoting the county and municipal filing statutes.',
    },
    {
      no: 'MS.5',
      pages: '5 pages',
      title: 'Forms & Documents Index',
      copy:
        'Every document you will be handed or asked for, and where it comes from — plus the structures Mississippi exempts outright and the two affidavits that unlock them, one of which has to be filed before you build.',
    },
  ],

  includes: [
    '36 print-ready pages across 6 documents, letter size',
    'The owner-builder exemption walkthrough — all four exemptions in Miss. Code § 73-59-15',
    'How to establish whether a building code binds your parcel, from the filed public record',
    'The wastewater approval that applies statewide even where no code does, with the two-acre exemption',
    'Inspection sequence — and a private inspection plan for no-code parcels',
    'Where-to-file directory with the offices that apply regardless of code status',
    'Statute citations printed on the page, not linked away',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things in this kit that most Mississippi owner-builder advice gets wrong. Each one is checkable in a couple of minutes — which is the point of printing the citation.',

  highlights: [
    {
      icon: 'permit',
      label: 'Your code status was fixed by a vote in 2014',
      copy:
        "Guides describe Mississippi in the present tense — counties 'can' opt out of the building code. The statute gave a one-time window. SB 2378 took effect August 1, 2014 and allowed a county, or any municipality within it, 120 days to opt out 'upon resolution duly adopted and entered upon its minutes.' That closed in November 2014 and has never reopened — every building-code bill since has died in committee. You cannot change your parcel's status; you can only go and read the resolution, and this kit shows you where it is filed. The Fire Marshal's office puts the deadline in writing: counties and municipalities 'must enact uniform building codes unless they opt out prior to Nov. 30, 2014.' No roster of who did was ever published — so your county's minute book is the only record that governs.",
    },
    {
      icon: 'bolt',
      label: 'The trade-license threshold is zero, not $10,000',
      copy:
        "Search Mississippi trade licensing and you are told electrical, plumbing and HVAC need a state license 'over $10,000.' That figure is the remodeler threshold in § 73-59-1(c), about remodeling someone else's house. The trades have no threshold: § 73-59-3(1)(d) licenses subcontractors 'of any tier' doing electrical, plumbing, mechanical or HVAC 'no matter the dollar amount.' The electrician setting your temporary power pole for $700 needs a license, and your own exemption does not travel to anyone you pay.",
    },
    {
      icon: 'check',
      label: "The coast's mandatory wind code had a 60-day opt-out",
      copy:
        "Every guide states that the five Gulf Coast counties are required to enforce wind and flood provisions. The 2006 law that imposed it, HB 1406, gave each of those counties and each municipality inside them sixty days to opt out by resolution — in the same language as the 2014 window. So 'mandatory on the coast' is a claim to check rather than assume. The same section also leaves the emergency 2003 IRC and IBC provisions in force until a jurisdiction adopts the latest editions.",
    },
    {
      icon: 'doc',
      label: 'A rolling year, not a calendar year',
      copy:
        "Mississippi limits the owner-builder exemption to one residence, and the wording matters: § 73-59-15(2) says 'within a period of one (1) year' — a rolling twelve months measured from your last permit application or completed home. Guides that print 'one dwelling per calendar year' describe a rule Mississippi did not write, and the difference is real: under the calendar reading you could pull a permit in December and another in January. Under the statute that is two inside one year, and the rebuttable presumption that you are building for sale attaches.",
    },
  ],

  sourceNote:
    'Verified against the Mississippi Code, the enacted bills at billstatus.ls.state.ms.us, the State Board of Contractors’ published law and rules, and the Department of Health’s onsite wastewater law, August 2026 · Citations printed on each page',

  faqs: [
    {
      question: 'Do I need a license to build my own house in Mississippi?',
      answer:
        "No. Miss. Code § 73-59-15(1)(b) says the residential builders chapter 'shall not apply to … any person who undertakes construction or improvement on his own residence, or who acts as his own general contractor in the performance of construction or improvement on his own residence.' There is no cost cap, no square-footage limit and no state affidavit form. The $50,000 figure people quote defines who is a residential builder building for someone else — it is not a ceiling on your own house.",
    },
    {
      question: 'Can you build a house without a permit in Mississippi?',
      answer:
        "In much of the state, yes. Mississippi's statewide construction code law let every county and municipality opt out within 120 days of August 1, 2014, and many did. Mississippi's own licensing statute assumes it: § 73-59-15(1)(g) is an exemption written specifically for 'any county or municipality which does not require a building permit or any local certification.' But an opt-out is an opt-out of the building code only — the health department's wastewater approval, floodplain rules, road access and your utility's requirements all still apply.",
    },
    {
      question: 'Does Mississippi have a statewide building code?',
      answer:
        "Not in the way that phrase suggests. The Building Codes Council adopts codes as 'discretionary statewide minimum codes' under § 17-2-3(5), and both that section and the 2014 statewide law let a jurisdiction use 'one (1) of the last three (3) adopted editions' of the IBC or IRC. So there is no single Mississippi edition to look up — neighboring counties can lawfully enforce different editions of the IRC on the same day, and some enforce none at all. The adopted IRC also excludes the residential fire-sprinkler provisions, though a county or city may still require them.",
    },
    {
      question: 'Can a homeowner do their own electrical and plumbing in Mississippi?',
      answer:
        "As far as state law goes, yes. The trade licensing requirement in § 73-59-3(1)(d) is written for 'any subcontractor, of any tier' — you are not a subcontractor on your own house — and § 73-59-15(1)(b) disapplies the whole chapter to a person building their own residence. But the state is not the only government involved: counties may adopt electrical, plumbing and gas codes for their unincorporated areas under § 19-5-9, and municipalities under § 21-19-25, and a local code can set its own rules about who may pull a trade permit. Ask before you buy wire.",
    },
    {
      question: 'Do I need a septic permit before building in Mississippi?',
      answer:
        "Yes, and earlier than most people expect. Miss. Code § 41-67-5(1) says no owner 'shall construct or place' a residence that may require an onsite system 'without having first submitted a notice of intent to the department.' The trigger is building the house, not installing the septic system. And § 41-67-5(2) forbids any public water utility from connecting a dwelling 'without the prior written approval of the department' — which is why the health department's paperwork is what your water association asks to see before setting a meter. This applies statewide, regardless of your building-code status.",
    },
    {
      question: 'How many houses can I build under the Mississippi owner-builder exemption?',
      answer:
        "One in any rolling twelve months under the main exemption. Section 73-59-15(2) bars more than one permit application or one residence 'within a period of one (1) year' and creates a rebuttable presumption that a second means you are building for sale — which would require a license. Two wrinkles most guides miss: the cap names only paragraphs (1)(b) and (c), so the owner-in-charge exemption in (1)(d) is not subject to it by its terms; and in a jurisdiction that requires no building permit, (1)(g) allows two residences a year rather than one.",
    },
  ],

  productDescription:
    'Mississippi owner-builder permitting, start to finish: the § 73-59-15 exemption walkthrough, how to establish whether any building code binds your parcel, the wastewater approval that applies statewide even where none does, permit application checklist, inspection sequence, where-to-file directory, and forms index. 36 print-ready pages across 6 documents, with the statute citations printed on the page. Verified against the Mississippi Code, the enacted bills at billstatus.ls.state.ms.us, the State Board of Contractors and the Department of Health, August 2026.',

  verifyNote:
    'Statutes and code editions change, and in Mississippi the answer changes at the county line — and inside it, because a county code never reaches into a town. Confirm each rule with the office that will actually issue your permit, or with the clerk who holds the filed code if no office will, and the kit prints its sources so you can.',

  binderLead:
    'The kit settles whether you need a permit and gets you through it if you do. The binder runs the build: 367 pages of contracts, inspection forms, daily logs, and budget trackers covering every phase from footing to final, in the same print-and-go format — and it matters more here, because in a no-code county your own records are the only ones anyone will ever have.',
};

export default function MSPermitKit() {
  return <KitProductPage content={MS} />;
}
