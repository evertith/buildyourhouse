import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/ca-permit-kit' },
  title: 'California Owner-Builder Permit Kit — $34',
  description:
    'Every permit, form, and inspection California requires of an owner-builder: the B&P § 7044 exemption walkthrough, the statutory Owner-Builder Declaration, permit application checklist, inspection sequence, and where-to-file directory. 38 print-ready pages with the statute citations on the page. $34 instant download.',
  keywords:
    'California owner builder permit, B&P 7044 exemption, owner builder declaration California, CA building permit checklist, California inspection sequence, Title 24 owner builder',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

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
      pages: '11 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy:
        'Business and Professions Code § 7044 is four separate exemptions with different conditions, and picking the wrong one is how owner-builders get caught. This walks each branch, the Owner-Builder Declaration you sign under penalty of perjury, and the sale rule — including the conclusive presumption almost nobody prints.',
      thumb: '/kits/ca/cak-exempt.webp',
      caption: 'CA.1 Exemption walkthrough',
      alt: 'Page CA.1, the Owner-Builder Exemption Walkthrough: the four § 7044 branches set out in a table with the statutory conditions and the California code sections printed beside each.',
    },
    {
      no: 'CA.2',
      pages: '12 pages',
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

export default function CAPermitKit() {
  return <KitProductPage content={CA} />;
}
