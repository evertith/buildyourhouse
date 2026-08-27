import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/wa-permit-kit' },
  title: 'Washington Owner-Builder Permit Kit — $34',
  description:
    'Every permit, form, and inspection Washington requires of an owner-builder: the contractor-registration exemption walkthrough, permit application checklist, inspection sequence with the L&I electrical split, and where-to-file directory. 35 print-ready pages with the RCW and WAC citations on the page. $34 instant download.',
  keywords:
    'Washington owner builder permit, WA building permit checklist, RCW 18.27.090 exemption, L&I electrical permit, Washington energy code blower door, permit exempt well Washington',
  openGraph: {
    images: ['/binder/og-shop.jpg'],
  },
};

const WA: KitContent = {
  slug: 'wa-permit-kit',
  heroSub:
    'Washington splits one house across four permitting agencies — this kit tells you which counter you are standing at, with the RCW and WAC cited on every page.',
  pageCount: 35,
  revision: 'August 2026',

  heroSheets: {
    front: {
      src: '/kits/wa/wak-exempt.webp',
      alt: 'The Washington owner-builder exemption walkthrough, page WA.1 of the permit kit.',
    },
    back: {
      src: '/kits/wa/wak-checklist.webp',
      alt: 'A page of the WA permit application checklist stacked behind the exemption walkthrough.',
    },
  },

  documents: [
    {
      no: 'WA.0',
      pages: '3 pages',
      title: 'Cover & How to Use',
      copy:
        'What is in the kit, what order to work it, and why Washington sends you to more than one permit counter for a single house.',
    },
    {
      no: 'WA.1',
      pages: '7 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy:
        'Washington has no GC license — it has registration, and three separate exemptions with three different tests. Which one you are actually relying on, what the selling/demolishing/leasing carve-out means, and why the electrical exemption is stricter than the plumbing one. RCW 18.27.090, 19.28.261 and 18.106.150 cited on the page.',
      thumb: '/kits/wa/wak-exempt.webp',
      caption: 'WA.1 Exemption walkthrough',
      alt: 'Page WA.1, the Owner-Builder Exemption Walkthrough: the RCW 18.27.090(12) text quoted in full with its carve-out explained beside it.',
    },
    {
      no: 'WA.2',
      pages: '11 pages',
      title: 'Permit Application Checklist',
      copy:
        'The four gates state law puts on your application — proof of water, a complete filing, energy credits on the drawings, and the electrical permit that is not on this form. Plus the septic track, the current code editions, and the clocks the State puts on your reviewer.',
      thumb: '/kits/wa/wak-checklist.webp',
      caption: 'WA.2 Application checklist',
      alt: 'Page WA.2, the Permit Application Checklist: a ruled list of application items with checkboxes and columns for the date and who confirmed it.',
    },
    {
      no: 'WA.3',
      pages: '6 pages',
      title: 'Inspection Sequence',
      copy:
        'Fourteen inspections in call order with the agency named for each one — because your electrical rough-in is called to a different agency than your framing. Includes the three mandatory energy tests and a log with an agency column.',
      thumb: '/kits/wa/wak-inspect.webp',
      caption: 'WA.3 Inspection sequence',
      alt: 'Page WA.3, the Inspection Sequence: Washington inspections listed in call order with a column naming which agency inspects each one.',
    },
    {
      no: 'WA.4',
      pages: '5 pages',
      title: 'Where-to-File Directory',
      copy:
        'Four agencies, one house: building department, L&I or a city electrical program, your local health jurisdiction, and water. Verified domains for the high-volume counties, plus fill-in blocks for what you confirmed.',
    },
    {
      no: 'WA.5',
      pages: '3 pages',
      title: 'Forms & Documents Index',
      copy:
        'Every document you will meet, what it is, when it is needed, and which of the four agencies issues it — including the one nobody warns you about, the sales tax on every subcontractor invoice.',
    },
  ],

  includes: [
    '35 print-ready pages across 6 documents, letter size',
    'The contractor-registration exemption walkthrough (RCW 18.27.090, 19.28.261, 18.106.150)',
    'A permit application checklist you can work straight through',
    'The inspection sequence with the agency named for every call',
    'Where-to-file directory: building, L&I electrical, local health, water',
    'RCW and WAC citations printed on the page, not linked away',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things in this kit that most Washington owner-builder advice gets wrong. Each one is checkable in about a minute at app.leg.wa.gov — which is the point of printing the citation.',

  highlights: [
    {
      icon: 'bolt',
      label: 'Your electrical permit comes from the State, not the county',
      copy:
        'Washington hands electrical work to Labor & Industries under chapter 296-46B WAC, and RCW 19.28.101(1) lets only incorporated cities and towns run their own program — counties cannot. If your lot is in unincorporated county, your rough-in is inspected by the State, on a separate call, and nothing may be covered until that inspector approves it. The kit names the agency for every inspection in the sequence.',
    },
    {
      icon: 'doc',
      label: 'The 24-month electrical rule is not the rule for your house',
      copy:
        'Guides tell Washington owner-builders they must intend to occupy for 24 months to do their own electrical. Read where the sentence sits: RCW 19.28.261(1) exempts work on property you own, and the 24-month affidavit language is in the following sentence, which applies to a new residential building "intended for rent, sale, or lease." The kit quotes both and tells you to confirm with L&I.',
    },
    {
      icon: 'permit',
      label: 'The permit-exempt well is 950 gallons a day, not 5,000',
      copy:
        'RCW 90.44.050 does exempt 5,000 gallons a day — but in eight Puget Sound basins the 2018 streamflow law cut a new domestic connection to 950 gallons per day with a $500 fee at building permit, and to 3,000 in seven more. You also cannot get a building permit without evidence of water, and a water right application expressly does not count. The kit lists all fifteen basins by number and name.',
    },
    {
      icon: 'check',
      label: 'Three mandatory tests, and no visual alternative to any of them',
      copy:
        'Washington requires a blower door at 4.0 ACH50 under any compliance path, a duct leakage test, and verified ventilation airflow — each producing a signed report to the code official. The ceiling requirement is R-60, not the R-49 most summaries print, and the prescriptive table has a single column covering the whole state. The kit prints the table with its footnotes.',
    },
  ],

  sourceNote:
    'Verified against the RCW and WAC at app.leg.wa.gov, plus L&I, SBCC, Ecology, DOH and Revenue, August 2026 · Citations printed on each page',

  faqs: [
    {
      question: 'Can I build my own house in Washington without a contractor license?',
      answer:
        'Yes. Washington does not license general contractors at all — it registers them, and RCW 18.27.090(12) exempts an owner doing work on their own property or personal residence. The carve-out to watch: the exemption does not apply if the building is intended for sale, demolition, or leasing, and RCW 18.27.110(3) forfeits a permit obtained by falsifying an exemption. The kit walks all three exemptions — registration, electrical, and plumbing — because qualifying for one does not qualify you for the others.',
    },
    {
      question: 'Can I do my own electrical work in Washington?',
      answer:
        'Yes, on property you own — RCW 19.28.261(1). The widely repeated "you must intend to live there 24 months" condition actually sits in the next sentence of the statute, which applies to new residential buildings intended for rent, sale, or lease. What is true for everyone: the electrical permit comes from Labor & Industries (or your city, if it runs its own program — counties cannot), the work is inspected separately from your building inspections, and nothing may be covered until approved. The kit quotes the statute and tells you to confirm your reading with L&I.',
    },
    {
      question: 'Can I do my own plumbing in Washington?',
      answer:
        'Yes — RCW 18.106.150(1) exempts a homeowner doing plumbing in their own residence, and unlike the electrical exemption it carries no rent, sale, or lease condition. Medical gas piping is excluded, and the plumbing permit and inspections still apply through your local building department. The asymmetry between the two trades is one of the most misreported facts in Washington owner-builder advice, so the kit prints both statutes side by side.',
    },
    {
      question: 'What is the 950-gallon well rule?',
      answer:
        'RCW 90.44.050 exempts a domestic well drawing up to 5,000 gallons per day from the water-right permit requirement — but the 2018 streamflow restoration law overrode that baseline in fifteen named watersheds. In eight Puget Sound basins a new domestic connection is capped at 950 gallons per day annual average with a $500 fee collected at building permit; in seven more it is 3,000. And under RCW 19.27.097 you cannot get a building permit at all without evidence of adequate water — a pending water-right application expressly does not count. The kit lists every affected basin by number and name.',
    },
    {
      question: 'What inspections are required for a new house in Washington?',
      answer:
        'The building-side sequence runs from footing and foundation through framing, rough plumbing, and insulation to final — called to your local building department — while every electrical inspection is called separately to L&I or your city program. On top of those, the state energy code requires three tests with no visual alternative: a blower door at 4.0 air changes per hour, a duct-leakage test, and verified ventilation airflow, each producing a signed report. The kit lays out fourteen inspections in call order with the agency named for each.',
    },
    {
      question: 'How long does permitting take in Washington?',
      answer:
        'State law puts clocks on your reviewer: RCW 36.70B.070 gives the department 28 days to determine whether your application is complete (deemed complete on day 29 if they miss it), and RCW 36.70B.080 sets decision deadlines of 65, 100, or 170 days by permit type — with 10% and 20% fee refunds when they blow through them. Your application also vests to the rules in effect on the day it is complete (RCW 19.27.095), which is worth real money in a code-change year. The kit explains which clocks run in parallel and what starts each one.',
    },
  ],

  productDescription:
    'Washington owner-builder permitting, start to finish: the contractor-registration exemption walkthrough, permit application checklist, inspection sequence with the L&I electrical split named for every call, where-to-file directory, and forms index. 35 print-ready pages across 6 documents, with the RCW and WAC citations printed on the page. Verified against app.leg.wa.gov, L&I, SBCC, Ecology and DOH, August 2026.',

  verifyNote:
    'Statutes and code editions change, and Washington runs a three-year code cycle. Confirm each rule with the city or county building department that will issue your permit — and separately with L&I, or your city, for anything electrical. The kit prints its sources so you can.',

  binderLead:
    'The kit gets your permits. The binder runs the build — 367 pages of contracts, inspection forms, daily logs, and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function WAPermitKit() {
  return <KitProductPage content={WA} />;
}
