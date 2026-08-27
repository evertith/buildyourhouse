import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/co-permit-kit' },
  title: 'Colorado Owner-Builder Permit Kit — $34',
  description:
    'Colorado runs two permit systems over one house. The building permit is local — some counties require none. The electrical and plumbing permits are STATE permits, and the homeowner electrical exemption is conditioned on getting inspected. 37 print-ready pages with the C.R.S. citations on the page. $34 instant download.',
  keywords:
    'Colorado owner builder permit, Colorado building permit requirements, homeowner electrical permit Colorado, C.R.S. 12-115-116, state electrical permit Colorado, Colorado well permit 35 acres, counties with no building code Colorado, Colorado septic OWTS permit',
  openGraph: {
    images: ['/binder/og-shop.jpg'],
  },
};

const CO: KitContent = {
  slug: 'co-permit-kit',
  heroSub:
    'Two permit systems over one house: a building permit that is entirely local — and may not exist at all — and electrical and plumbing permits that come from the State. Verified against the Colorado Revised Statutes, citations printed on the page.',
  pageCount: 37,
  revision: 'August 2026',

  heroSheets: {
    front: {
      src: '/kits/co/cok-position.webp',
      alt: 'The Colorado owner-builder legal-position document, page CO.1 of the permit kit.',
    },
    back: {
      src: '/kits/co/cok-checklist.webp',
      alt: 'A page of the Colorado permit application checklist stacked behind the legal-position walkthrough.',
    },
  },

  documents: [
    {
      no: 'CO.0',
      pages: '4 pages',
      title: 'Cover & How to Use',
      copy:
        'The Colorado inversion in one page — no state building permit, but a state electrical permit — plus the four questions you have to answer before anything else in the kit applies.',
    },
    {
      no: 'CO.1',
      pages: '10 pages',
      title: "The Owner-Builder's Legal Position",
      copy:
        'No state contractor license, no statewide building code, and the two state trade permits that bind you anyway. Includes the condition hidden inside the homeowner electrical exemption, quoted verbatim with C.R.S. 12-115-116(2) on the page, and two verified local owner-builder regimes.',
      thumb: '/kits/co/cok-position.webp',
      caption: 'CO.1 Legal position',
      alt: 'Page CO.1, the owner-builder legal position: the Colorado homeowner electrical exemption quoted in full with the statute number printed beside it.',
    },
    {
      no: 'CO.2',
      pages: '9 pages',
      title: 'Permit Application Checklist',
      copy:
        'The land approvals that gate a Colorado build — well permit, septic, access — then the local building permit if one exists, then the state trade permits. In the order you actually have to work them.',
      thumb: '/kits/co/cok-checklist.webp',
      caption: 'CO.2 Application checklist',
      alt: 'Page CO.2, the permit application checklist: ruled checkboxes for the well permit, septic permit, and state trade permits with a column for the date each was filed.',
    },
    {
      no: 'CO.3',
      pages: '5 pages',
      title: 'Inspection Sequence',
      copy:
        'Four authorities can inspect one Colorado house and none of them talks to the others. How the state electrical and plumbing inspections work, where they slot into the local ladder, and a log for all of them.',
      thumb: '/kits/co/cok-inspect.webp',
      caption: 'CO.3 Inspection sequence',
      alt: 'Page CO.3, the inspection sequence: the typical inspection order with a column naming which authority owns each rung.',
    },
    {
      no: 'CO.4',
      pages: '6 pages',
      title: 'Where-to-File Directory',
      copy:
        "The Division's own published lists of which counties run their own electrical and plumbing programs — the ten counties where they differ — plus the state offices, and a page to fill in your own.",
    },
    {
      no: 'CO.5',
      pages: '3 pages',
      title: 'Forms & Documents Index',
      copy:
        'Every document you will actually meet, which office issues it, and the ones people go looking for that do not exist in Colorado at all.',
    },
  ],

  includes: [
    '37 print-ready pages across 6 documents, letter size',
    'The homeowner electrical and plumbing exemptions, quoted verbatim (C.R.S. 12-115-116, 12-155-118)',
    'A permit checklist that runs water and septic first, where Colorado actually starts',
    'The full inspection sequence, marked with which authority owns each step',
    "Where-to-file directory including DORA's published local-jurisdiction lists",
    'Statute and rule citations printed on the page, not linked away',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things in this kit that most Colorado owner-builder advice gets wrong. Each is checkable in about a minute — which is the whole argument for the price.',

  highlights: [
    {
      icon: 'bolt',
      label: 'The electrical exemption dies if you skip the inspection',
      copy:
        'C.R.S. 12-115-116(2) lets you do your own wiring “if all such electrical work … is inspected as provided in this article 115.” The word is “if.” Skip the permit and inspection and the exemption never applied to the work — leaving unlicensed electrical work, a class 2 misdemeanor. The plumbing exemption forty sections later carries no such condition. No general guide we have seen prints this.',
    },
    {
      icon: 'permit',
      label: 'No building permit does not mean no permit',
      copy:
        'A board of county commissioners is only “authorized to” adopt a building code, and the permit duty exists solely “after the adoption of the building code.” But the electrical and plumbing permits are state permits everywhere a local government does not run its own program — and no utility may connect permanent power without proof of final electrical approval. The kit sequences both tracks.',
    },
    {
      icon: 'doc',
      label: 'Colorado wires to the 2026 NEC and plumbs to 2021 codes',
      copy:
        'The State Electrical Board’s rule adopts the 2026 National Electrical Code effective August 1, 2026, while the Colorado Plumbing Code and Colorado Fuel Gas Code are built on 2021 model codes — two boards, one house, a five-year gap. Anything written before mid-2026 has the electrical edition wrong. The kit cites the rule numbers so you can check both yourself.',
    },
    {
      icon: 'check',
      label: 'Under 35 acres, your well is household use only',
      copy:
        'C.R.S. 37-92-602(3)(b)(II)(A) grants the no-injury presumption for a well used “solely for ordinary household purposes inside a single-family dwelling and … not … for irrigation” — or for the only well on a tract of thirty-five acres or more, which is where lawn, garden, and livestock use lives. People buy five-acre parcels planning an orchard and find out afterwards.',
    },
  ],

  sourceNote:
    'Verified against the official Colorado Revised Statutes 2026, the Code of Colorado Regulations, DORA, DFPC, and the Division of Water Resources, August 2026 · Citations printed on each page',

  faqs: [
    {
      question: 'Can you build your own house in Colorado?',
      answer:
        'Yes. No Colorado state agency issues a general contractor or home builder license, and there is no statewide residential building code — whether a building permit exists at all is decided by your county or municipality, and a few counties require none. But electrical and plumbing are licensed statewide, each installation in new construction requires a permit and an inspection, and where your local government does not run its own qualifying program those permits come from the State Electrical Board and the State Plumbing Board. The kit works both tracks.',
    },
    {
      question: 'Do you need a permit to build a house in Colorado?',
      answer:
        'There are two separate answers. A board of county commissioners is only “authorized to” adopt a building code (C.R.S. 30-28-201(1)), and the duty to get a building permit exists solely “after the adoption of the building code” (30-28-205(1)) — so in some unincorporated counties there is no building permit to apply for. The electrical and plumbing permits exist regardless, and both statutes require the permit and fee before work commences. The kit makes you settle each question separately, because the answers are independent.',
    },
    {
      question: 'Can a homeowner do their own electrical work in Colorado?',
      answer:
        'Yes, and you may pull the permit yourself — “qualified applicant” expressly includes “a homeowner performing work on the homeowner’s home” (C.R.S. 12-115-120(11)(c)). But read the exemption slowly: 12-115-116(2) applies “if all such electrical work … is inspected as provided in this article 115.” The exemption is conditioned on the inspection, and it goes away entirely if the property is developed for sale, lease, or rental. The kit prints the statute in full.',
    },
    {
      question: 'My county has no building code. Do I still need permits?',
      answer:
        'Yes. You will still need a state electrical permit and, in most counties, a state plumbing and gas piping permit; an on-site wastewater permit from your local public health agency; a well permit from the Division of Water Resources; and usually land-use approval and a driveway permit. And no utility may provide service without proof of final electrical approval (C.R.S. 12-115-120(1)(c)) — so an unapproved house does not get permanent power, however quiet your county is about building permits.',
    },
    {
      question: 'How long does a Colorado well permit take?',
      answer:
        'The Division of Water Resources states that review of a complete application may take up to 49 days, before a driller is even scheduled — which is why the kit runs water first rather than starting at the building department. Check the acreage rules before you buy land: under 35 acres a new exempt well is typically limited to household use inside the dwelling, with no outdoor irrigation, under C.R.S. 37-92-602(3)(b)(II)(A).',
    },
    {
      question: 'Who inspects my house in Colorado?',
      answer:
        'Up to four authorities under three different statutes, and none of them coordinates with the others: the local building inspector (if your jurisdiction adopted a code), the electrical inspector, the plumbing and gas inspector, and your local public health agency for septic. Ten Colorado counties run their own plumbing program but not an electrical one, so you can have a county plumbing inspector and a state electrical inspector on the same job. The kit gives you a log for all of them.',
    },
  ],

  productDescription:
    'Colorado owner-builder permitting, start to finish: the legal position (no state contractor license, no statewide building code — and the two state trade permits that bind you anyway), the permit application checklist, the inspection sequence, the where-to-file directory, and the forms index. 37 print-ready pages across 6 documents, with the C.R.S. and CCR citations printed on the page. Verified against the official Colorado Revised Statutes 2026, the Code of Colorado Regulations, DORA, and the Division of Water Resources, August 2026.',

  verifyNote:
    'Statutes and code editions change, and in Colorado almost everything is decided locally. Confirm each rule with your city or county building department — and confirm separately whether your electrical and plumbing permits come from them or from the State. The kit prints its sources so you can.',

  binderLead:
    'The kit gets your permits — all of them, from all the offices. The binder runs the build: 367 pages of contracts, inspection forms, daily logs, and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function COPermitKit() {
  return <KitProductPage content={CO} />;
}
