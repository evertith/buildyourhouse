import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/mi-permit-kit' },
  title: 'Michigan Owner-Builder Permit Kit — $34',
  description:
    'Every permit, form, and inspection Michigan requires of an owner-builder: the MCL 339.2403 exemption walkthrough, the four separate trade permits and who issues each, the permit application checklist, inspection sequence, and where-to-file directory. 36 print-ready pages with the statute citations on the page. $34 instant download.',
  keywords:
    'Michigan owner builder permit, MI building permit checklist, Michigan owner builder exemption, MCL 339.2403, Michigan enforcing agency, statewide jurisdiction list, Michigan homeowner electrical permit, Michigan 2015 residential code',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const MI: KitContent = {
  slug: 'mi-permit-kit',
  heroSub:
    "Michigan's hardest question is not what the rules are — it is who enforces them on your parcel. This kit answers it, per trade, with the statutes cited on the page.",
  pageCount: 36,
  revision: 'August 2026',

  heroSheets: {
    front: {
      src: '/kits/mi/mik-exempt.webp',
      alt: 'The Michigan owner-builder exemption walkthrough, page MI.1 of the permit kit.',
    },
    back: {
      src: '/kits/mi/mik-directory.webp',
      alt: 'A page of the Michigan where-to-file directory stacked behind the exemption walkthrough.',
    },
  },

  documents: [
    {
      no: 'MI.0',
      pages: '2 pages',
      title: 'Cover & How to Use',
      copy:
        'What is in the kit, what order to work through it, and why in this state the directory has to come before the checklist.',
    },
    {
      no: 'MI.1',
      pages: '8 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy:
        'The two statutes that exempt you, the three trade exemptions stacked on top, and what takes them away. No dollar threshold, no holding period, no not-for-sale window — with MCL 339.2401, 339.2403, 339.5737 and 339.601 cited on the page.',
      thumb: '/kits/mi/mik-exempt.webp',
      caption: 'MI.1 Exemption walkthrough',
      alt: 'Page MI.1, the Owner-Builder Exemption Walkthrough: the trade-by-trade exemption table with what each Michigan statute requires and the MCL citation beside each row.',
    },
    {
      no: 'MI.2',
      pages: '12 pages',
      title: 'Permit Application Checklist',
      copy:
        "Built around the five Environmental Control Approvals printed on the State's own application, plus the sealed-plans threshold, the code edition a court order froze, the soil-erosion permit that gates your building permit, and the State fee schedule.",
      thumb: '/kits/mi/mik-checklist.webp',
      caption: 'MI.2 Application checklist',
      alt: 'Page MI.2, the Permit Application Checklist: ruled checklist rows with checkboxes and columns for the date and who confirmed each item, beginning with which agency issues each of the four permits.',
    },
    {
      no: 'MI.3',
      pages: '5 pages',
      title: 'Inspection Sequence',
      copy:
        'The order Michigan calls inspections in, the one sequencing rule the State fixes by rule, and the five clocks that run against your enforcing agency.',
    },
    {
      no: 'MI.4',
      pages: '5 pages',
      title: 'Where to File Directory',
      copy:
        'How to read the Statewide Jurisdiction List for your exact township, per trade, plus the six other offices it does not cover and a page to write down what you confirmed.',
      thumb: '/kits/mi/mik-directory.webp',
      caption: 'MI.4 Where-to-file directory',
      alt: 'Page MI.4, the Where to File Directory: the step-by-step instructions for reading the Statewide Jurisdiction List for your parcel, with checkboxes for each step.',
    },
    {
      no: 'MI.5',
      pages: '4 pages',
      title: 'Forms & Documents Index',
      copy:
        "Every document you will meet, with the State's form number, and the work that needs no permit at all.",
    },
  ],

  includes: [
    '36 print-ready pages across 6 documents, letter size',
    'The owner-builder exemption walkthrough (MCL 339.2401 and 339.2403)',
    'Homeowner electrical, plumbing and mechanical exemptions — cited to live statute, not the repealed acts',
    "A permit application checklist built on the State's own approval block",
    "The inspection sequence, with Michigan's framing-after-rough-ins rule",
    'Where-to-file directory — per trade, because Michigan assigns them separately',
    'Statute and rule citations printed on the page, not linked away',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things in this kit that most Michigan owner-builder advice gets wrong. Each one is checkable in a couple of minutes — which is the point of printing the citation.',

  highlights: [
    {
      icon: 'doc',
      label: '3,500 sq ft counts habitable space only',
      copy:
        "Michigan exempts one- and two-family dwellings under 3,500 square feet of calculated floor area from the architect's seal. Almost nobody prints the definition: MCL 339.2012(2) counts habitable space only, and expressly excludes basements, garages, attics, bathrooms, closets, hallways and utility rooms. A house marketed at 4,200 square feet can sit comfortably under the threshold. Owner-builders buy sealed plan sets they never needed.",
    },
    {
      icon: 'permit',
      label: 'Your four permits may come from four different governments',
      copy:
        "Building, electrical, mechanical and plumbing are assigned separately, unit of government by unit of government, and the State is the default rather than the backstop — locals opt in by ordinance. Working through LARA's own list, 252 of Michigan's 1,824 units of government have at least one discipline assigned to a different agency than the others. The State is the plumbing enforcing agency for 264 units but the building agency for only 59.",
    },
    {
      icon: 'bolt',
      label: 'Michigan is still on the 2015 code, not the 2021',
      copy:
        "Michigan filed rule sets adopting the 2021 IRC and 2021 IECC residential provisions with a real effective date of August 29, 2025. On July 7, 2025 the Court of Claims froze both. LARA's own notice says the 2015 editions 'remain valid and in effect' — but the adopted-codes-by-state tables had already flipped Michigan to 2021. Buy the wrong book and your wall assemblies and air-sealing obligations are from a code that does not apply to you.",
    },
    {
      icon: 'check',
      label: 'Your city can switch off your electrical exemption',
      copy:
        "The three trade exemptions are not equally durable. A municipality that adopts a qualifying electrical ordinance displaces the whole article, and the statute's list of work such an ordinance may not require a license for — MCL 339.5733(2) — pointedly omits the homeowner exemption. Plumbing and mechanical are the opposite: local licensing is barred outright. No other Michigan guide states this asymmetry.",
    },
  ],

  sourceNote:
    'Verified against legislature.mi.gov, the Michigan Administrative Code, LARA Bureau of Construction Codes and EGLE, August 2026 · Citations printed on each page',

  faqs: [
    {
      question: "Do I need a builder's license to build my own house in Michigan?",
      answer:
        "No. Michigan's Occupational Code excludes you twice: a person who erects a residential structure 'for the person's own use and occupancy on the person's property' falls outside the definition of a residential builder (MCL 339.2401(a)(iii)), and there is a separate express exemption for 'an owner of property, with reference to a structure on the property for the owner's own use and occupancy' (MCL 339.2403(b)). Neither carries a project-cost threshold, a square-footage limit, or a holding period.",
    },
    {
      question: 'Can a homeowner do their own electrical, plumbing and HVAC in Michigan?',
      answer:
        'Yes, but under three separate exemptions with different tests, and they are narrower than most summaries suggest. Electrical is the widest, covering a single-family home and accompanying outbuildings you own and occupy or will occupy, provided you personally do the work. Plumbing covers your own plumbing, building sewer or private sewer — and, unusually, mentions no occupancy condition at all. Mechanical reaches only a heating or refrigerating system, requires you to install it personally, and requires you to affirm ownership and occupancy on the permit application itself.',
    },
    {
      question: 'Who issues my building permit — the township, the county, or the State?',
      answer:
        'It depends on your exact unit of government, and it is answered separately for each of the four trades. The State is the default: a local unit becomes the enforcing agency only by passing an ordinance and, since 1999, getting Construction Code Commission approval. LARA publishes the answer for every unit of government in Michigan in one free PDF, the Statewide Jurisdiction List, which is revised after every Commission meeting. The kit shows you how to read your row.',
    },
    {
      question: 'Is there a time limit on selling a house I built for myself in Michigan?',
      answer:
        "No. Michigan sets no holding period, no not-for-sale window, and no presumption that you lacked intent if you move out — the whole of Article 24 and all 154 sections of the Skilled Trades Regulation Act were searched for one. Michigan's test is your intent at the time you build. That cuts both ways: there is no safe-harbor date to wait out either, so a house you never meant to occupy needed the license from day one.",
    },
    {
      question: 'Which building code does Michigan use?',
      answer:
        "The 2015 Michigan Residential Code, based on the 2015 IRC, with residential energy under Part 10's adoption of the 2015 IECC. Michigan adopted 2021 editions of both with an effective date of August 29, 2025, but a July 7, 2025 stipulated order of the Court of Claims prevented LARA from implementing them, and LARA's own notice confirms the 2015 versions remain in effect. Confirm the edition with your enforcing agency before you draw, because this one can change by court order rather than legislative session.",
    },
    {
      question: 'Do I need an architect to design my own house in Michigan?',
      answer:
        "Usually not. Plans for a one- or two-family dwelling under 3,500 square feet of calculated floor area need no architect's or engineer's seal — and calculated floor area counts habitable space only, excluding basements, garages, bathrooms, closets, hallways and utility rooms. There is also a second exemption with no area limit at all, for an owner doing design work on a building on their own property for their own use. Do the arithmetic before you pay for a seal.",
    },
  ],

  productDescription:
    'Michigan owner-builder permitting, start to finish: the MCL 339.2403 exemption walkthrough, permit application checklist, inspection sequence, where-to-file directory, and forms index. 36 print-ready pages across 6 documents, with the statute and rule citations printed on the page. Verified against legislature.mi.gov, the Michigan Administrative Code, LARA Bureau of Construction Codes and EGLE, August 2026.',

  verifyNote:
    'Statutes, rules and code editions change, and in Michigan the agency that enforces them can change after any Construction Code Commission meeting. Confirm each rule with your enforcing agency — township, city, county, or the state Bureau of Construction Codes — and the kit prints its sources so you can.',

  binderLead:
    'The kit gets your permits — all four, from whichever governments issue them. The binder runs the build: 367 pages of contracts, inspection forms, daily logs, and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function MIPermitKit() {
  return <KitProductPage content={MI} />;
}
