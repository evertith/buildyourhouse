import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/ak-permit-kit' },
  title: 'Alaska Owner-Builder Permit Kit — $34',
  description:
    'Every approval Alaska actually requires of an owner-builder — including the ones that apply where there is no building department: the AS 08.18.161(11) exemption walkthrough, the statewide smoke-alarm statute, the state plumbing code and its 2,500-population line, the where-to-file procedure, and the inspection and self-verification log. 56 print-ready pages with the statute citations on the page. $34 instant download.',
  keywords:
    'Alaska owner builder permit, AK building permit, Alaska owner builder exemption, AS 08.18.161, Alaska contractor registration, Mat-Su building permit, Alaska no building code, Alaska plumbing permit, Alaska smoke detector law',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const AK: KitContent = {
  slug: 'ak-permit-kit',
  heroSub:
    'Alaska is the easiest state in the country to get permission to build your own house, and the hardest one to prove you built it properly. This kit is about what still binds you when nobody is checking.',
  pageCount: 56,
  revision: 'August 2026',

  heroSheets: {
    front: {
      src: '/kits/ak/akk-exempt.webp',
      alt: 'Page 2 of AK.1, the Owner-Builder Exemption Walkthrough, showing the boxed quotation of AS 08.18.161(9) and why it does not cover a new house.',
    },
    back: {
      src: '/kits/ak/akk-directory.webp',
      alt: 'Page 2 of AK.4, the Where to File Directory, stacked behind the exemption walkthrough.',
    },
  },

  documents: [
    {
      no: 'AK.0',
      pages: '2 pages',
      title: 'Cover & How to Use',
      copy:
        'What is in the kit, what order to work it in, and why an Alaska kit has to answer a question the Lower 48 never asks.',
    },
    {
      no: 'AK.1',
      pages: '10 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy:
        'Which of Alaska’s twelve exemptions you actually build under — AS 08.18.161(9) is the remodel paragraph, (11) is the new-house one — the two-year rules attached to (11), and the three trade exclusions that live in two other chapters and are worded differently from each other.',
      thumb: '/kits/ak/akk-exempt.webp',
      caption: 'AK.1 Exemption walkthrough',
      alt: 'Page 2 of AK.1, the Owner-Builder Exemption Walkthrough: the boxed quotation of AS 08.18.161(9) showing the word "existing" that most summaries drop, above the full text of paragraph (11).',
    },
    {
      no: 'AK.2',
      pages: '20 pages',
      title: 'Permit Application Checklist',
      copy:
        'Both Alaska paths: the local-permit one, and the far commoner one where no government reviews your house. Built around the statewide floor — the smoke-alarm statute, the 2020 NEC, the 2018 UPC, the lead limits, DEC wastewater — that applies with no permit at all.',
      thumb: '/kits/ak/akk-checklist.webp',
      caption: 'AK.2 Application checklist',
      alt: 'Page 3 of AK.2, the Permit Application Checklist: the statewide smoke-alarm requirement explained above the statewide-floor checklist, with drawn checkboxes and columns for the date and evidence.',
    },
    {
      no: 'AK.3',
      pages: '7 pages',
      title: 'Inspection Sequence',
      copy:
        'Which parts of your house actually get inspected — three state regimes drawn on three different lines, none of them a borough boundary — the twelve-stage sequence, your rights when a state inspector does come, and the self-verification log for the stages nobody will ever look at.',
    },
    {
      no: 'AK.4',
      pages: '10 pages',
      title: 'Where to File Directory',
      copy:
        'Alaska publishes no jurisdiction list, so this is the five-question procedure that settles your parcel instead, plus the eleven offices that apply whether or not a building department exists, and a page to write down what you confirmed.',
      thumb: '/kits/ak/akk-directory.webp',
      caption: 'AK.4 Where-to-file directory',
      alt: 'Page 2 of AK.4, the Where to File Directory: the numbered table of the five questions that determine whether any government regulates your parcel, with why each one decides what happens next.',
    },
    {
      no: 'AK.5',
      pages: '7 pages',
      title: 'Forms & Documents Index',
      copy:
        'Every document you will meet and where it comes from — plus the seller-disclosure exemption for a first sale of a never-occupied house, and the build record you assemble in place of the certificate of occupancy most of Alaska never issues.',
    },
  ],

  includes: [
    '56 print-ready pages across 6 documents, letter size',
    'The owner-builder exemption walkthrough — AS 08.18.161(11), quoted in full',
    'The statewide rules that bind your house with no permit and no inspector',
    'A permit checklist for both paths, with and without a building department',
    'The borough-by-borough map of who issues permits — and the five questions behind it',
    'Inspection sequence plus a self-verification log for the unwatched stages',
    'Statute and regulation citations printed on the page, not linked away',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things in this kit that Alaska owner-builder advice gets wrong or leaves out entirely. Each is checkable at akleg.gov in about a minute — which is the point of printing the citation.',

  highlights: [
    {
      icon: 'doc',
      label: 'Almost everyone cites the wrong exemption paragraph',
      copy:
        'Search for the Alaska owner-builder exemption and you get AS 08.18.161 and a paraphrase of paragraph (9): “a person performing work on that person’s own property.” The statute actually reads “a person working on an existing structure on that person’s own property … and a person working on that person’s own existing residence.” Existing, twice. Paragraph (9) is the remodel paragraph. A new house is paragraph (11) — and (11) carries a one-building-every-two-years cap and a for-sale notice that (9) does not.',
    },
    {
      icon: 'permit',
      label: 'No building department, and a state plumbing inspector anyway',
      copy:
        'The state plumbing code applies to all new construction (AS 18.60.715(a)), and communities under 2,500 population are exempt from it (AS 18.60.735). At or above that line the code applies and the Department of Labor inspects — single-family houses included — in communities with no building department whatsoever. The trigger is population, not jurisdiction, which is why it blindsides people who checked only with their borough.',
    },
    {
      icon: 'bolt',
      label: 'The financier is the building official',
      copy:
        "Alaska has no building code for houses and enforces one anyway — through loan eligibility instead of a permit counter. By statute the Alaska Housing Finance Corporation may not lend on a home built after June 1992 without five named inspections, and 15 AAC 150.035 applies the 2018 IRC specifically to units not in a municipality with an approved building code. AHFC's amendments delete the code's own Administration and Enforcement chapter and its energy standard defines 'CODE OFFICIAL' as a representative of AHFC. Skip the inspections and the bill arrives at resale, as a destructive inspection with holes cut in your finished walls.",
    },
    {
      icon: 'check',
      label: 'One requirement reaches every dwelling in Alaska',
      copy:
        "The Fire Marshal's authority stops at four dwelling units and the adopted code excludes detached one-, two- and three-family dwellings outright. Yet AS 18.70.095(a) requires smoke detection devices 'in all dwelling units in the state,' installed as the fire marshal approves — and 13 AAC 50.030(b) permits battery-only alarms only in pre-1989 buildings or buildings with no commercial power. Violation is a class B misdemeanor, each 10 days a separate offense. It is the only Alaska construction requirement carrying a criminal penalty, and about a hundred dollars to satisfy.",
    },
  ],

  sourceNote:
    "Verified against the Alaska Statutes and Administrative Code at akleg.gov, each jurisdiction's own municipal code, and the Departments of Labor, Commerce, Environmental Conservation and Public Safety plus AHFC, August 2026 · Citations printed on each page",

  faqs: [
    {
      question: 'Do I need a license to build my own house in Alaska?',
      answer:
        'No. Alaska has no general contractor licensing examination at all — what it has is registration, and a person may not work as a contractor until the Department of Commerce, Community, and Economic Development issues a certificate of registration (AS 08.18.011(a)). Building your own house falls outside it, both because a "contractor" is defined as someone acting "in the pursuit of an independent business" (AS 08.18.171(4)) and because AS 08.18.161 exempts an owner acting as their own contractor. Which paragraph of AS 08.18.161 you rely on matters, though — see the next question.',
    },
    {
      question: 'What is the Alaska owner-builder exemption, exactly?',
      answer:
        'It depends on whether you are building something new. AS 08.18.161(9) covers "a person working on an existing structure on that person’s own property … and a person working on that person’s own existing residence" — that is the remodel and repair paragraph, and a bare lot has no existing structure on it. New construction is AS 08.18.161(11), which exempts "an owner who acts as the owner’s own contractor," expressly allows you to hire subcontractors, and imposes two conditions paragraph (9) does not: you are limited to one home, duplex, triplex, four-plex or commercial building every two years, and if you advertise or sell the structure during construction or within two years after construction begins you must file a notice with the department.',
    },
    {
      question: 'Can you build a house in Alaska without a permit?',
      answer:
        'In much of Alaska there is no building permit for the dwelling, because there is no statewide residential building code and many boroughs have adopted none. But "no building permit" is not "no requirements." Onsite wastewater is regulated statewide. Smoke and carbon monoxide alarms are required in every dwelling unit in the state by statute. The 2020 National Electrical Code and the 2018 Uniform Plumbing Code are the statewide minimums, and in a community of 2,500 or more the State of Alaska inspects your plumbing and gas piping. Zoning, driveway, floodplain and wetlands permits exist in boroughs with no building code at all.',
    },
    {
      question: 'Can a homeowner do their own electrical and plumbing in Alaska?',
      answer:
        'Largely yes, but under three separate exclusions in two different chapters, and they are not the same rule. Electrical is excluded for installation on residential property "owned by the installer or a member of the installer’s immediate family and not intended for sale at the time of making the installation" (AS 08.40.190(b)(3)) — two conditions. Mechanical is excluded for a single-family or two-family residence not intended for sale (AS 08.40.390(b)(3)) — with no ownership condition at all. Plumbing is the broadest and unconditional: "Nothing … prohibits a person from performing plumbing work on the person’s own property" (AS 18.60.715(c)). All three exclude you from the licence requirement only, never from the code.',
    },
    {
      question: 'Does Alaska have a statewide building code?',
      answer:
        'Not for houses, and the reason is statutory rather than a policy choice. The Department of Public Safety’s authority to set building standards runs only to buildings "used for residential purposes containing four or more dwelling units" (AS 18.70.080(a)(2)), and the code it adopts — the 2021 International Building Code, at 13 AAC 50.020 — revises its own scope section to exclude "Detached one-, two-, and three-family dwellings." Below four units, whether your house is reviewed depends entirely on what your borough or city has chosen to do, and boroughs and cities are separate governments with separate answers on the same map.',
    },
    {
      question: 'Can I install my own septic system in Alaska?',
      answer:
        'Yes, and the route is more permissive than most states. 18 AAC 72.400 bars anyone from installing a conventional onsite system unless they are a certified installer or an approved homeowner — but 18 AAC 72.410 makes you an approved homeowner after a DEC training course, an application and a $275 fee, good for one system in a one-year period on your own owner-occupied residence. You still need a registered engineer or a soils laboratory to classify the soils. Two things disqualify the shortcut entirely: ground known or suspected to contain permafrost, and a groundwater table within four feet of the surface. Inside the Municipality of Anchorage the rules are different again — a sealed engineer’s design is always required there.',
    },
    {
      question: 'Is there a time limit on selling a house I built for myself in Alaska?',
      answer:
        'There is no bar on selling, but there is a filing duty and a clock. Under AS 08.18.161(11), an owner who advertises or sells the structure during construction, or within two years after the period of construction begins, must file a notice on the department’s form stating they are not engaged in a contracting business — and once it is filed the department "shall investigate" (AS 08.18.116(b)). The clock starts earlier than people expect: the statute defines construction as beginning at the earlier of the day you start actual work and the day you enter into an agreement with anyone to provide labor, subcontracting or materials.',
    },
  ],

  productDescription:
    'Alaska owner-builder permitting, start to finish, in a state where most of the requirements do not arrive through a permit counter: the AS 08.18.161(11) exemption walkthrough, a permit checklist for both the local-permit and no-building-department paths, the inspection sequence and self-verification log, the five questions that establish who regulates your parcel, and the forms index. 56 print-ready pages across 6 documents with the statute and regulation citations printed on the page. Verified against the Alaska Statutes and Alaska Administrative Code at akleg.gov and the administering state agencies, August 2026.',

  verifyNote:
    'Statutes, regulations and code editions change, and in Alaska the thresholds that decide which rules reach your house — dwelling-unit counts and community population — move independently of any borough boundary. Confirm each rule with the office that will actually decide it, and the kit prints its sources so you can.',

  binderLead:
    'The kit gets you through the approvals — including the ones that apply where nobody issues a permit. The binder runs the build: 367 pages of contracts, inspection forms, daily logs and budget trackers covering every phase from footing to final, in the same print-and-go format. In Alaska that record does double duty, because it is what a lender, an insurer or a buyer will ask for in place of the certificate of occupancy you may never be issued.',
};

export default function AKPermitKit() {
  return <KitProductPage content={AK} />;
}
