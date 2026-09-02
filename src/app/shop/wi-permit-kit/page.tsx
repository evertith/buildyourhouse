import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/wi-permit-kit' },
  title: 'Wisconsin Owner-Builder Permit Kit — $34',
  description:
    'Wisconsin permit kit: the 2023 NEC that took effect on 1 September 2026, the two UDC zone maps numbered in opposite directions, the septic permit that must come before your building permit, and the four trade rules that are worded four different ways. 52 print-ready pages, every claim cited. $34 instant download.',
  keywords:
    'Wisconsin building permit, Wisconsin owner builder, Uniform Dwelling Code, UDC inspection agency, Wisconsin sanitary permit, POWTS permit Wisconsin, Wis. Stat. 101.654, Wisconsin homeowner electrical, NR 812 well separation, Wisconsin 2023 NEC',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const WI: KitContent = {
  slug: 'wi-permit-kit',
  heroSub:
    'Wisconsin has no permit-free town and no holding period on the owner exemption — but it does have two zone maps numbered backwards from each other, and a septic permit that has to come first.',
  pageCount: 52,
  revision: 'September 2026',

  heroSheets: {
    front: {
      src: '/kits/wi/wik-hero-front.webp',
      alt: 'Kit page setting the Uniform Dwelling Code roof-load zones against the energy zones in one table, showing Zone 1 as the northern 40 psf roof load but as the southern counties for insulation, above a worked example contrasting Vilas and Dane counties',
    },
    back: {
      src: '/kits/wi/wik-hero-back.webp',
      alt: 'Kit page quoting the rule that adopted the 2023 National Electrical Code effective 1 September 2026, above the table of standards the Uniform Dwelling Code adopts by reference',
    },
  },

  documents: [
    {
      no: 'WI.0',
      pages: '4 pages',
      title: 'Cover & How to Use',
      copy: 'A job-site cover with a “Who Enforces the UDC” line, because in Wisconsin that has four possible answers and none of them is “nobody”. Plus the orientation and the statute that reorders a rural build.',
    },
    {
      no: 'WI.1',
      pages: '11 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy: 'The one-sentence exemption, what it does not lift, and then the four trades — which are four separately worded rules. Includes the worker’s compensation triggers, the nine-part subcontractor test, and Wisconsin’s owner-milled lumber provision.',
      thumb: '/kits/wi/wik-exemption.webp',
      caption: 'WI.1 Four exemptions, four different tests',
      alt: 'Page 5 of WI.1: the tense-trap table setting the four Wisconsin trade exemptions side by side, showing the dwelling contractor and HVAC exemptions written as “resides or will reside” while the electrical exemption reads “owns and occupies”, above the callout explaining that the primitive rural hunting cabin exemption is grandfathered to structures built before 31 December 1997',
    },
    {
      no: 'WI.2',
      pages: '12 pages',
      title: 'Permit Application Checklist',
      copy: 'What to gather in the order Wisconsin makes you gather it — sanitary permit, then plans, then the uniform permit. Plus every code edition in force, the full prescriptive energy table, the frost rule, and three shot clocks.',
      thumb: '/kits/wi/wik-editions.webp',
      caption: 'WI.2 The code that changed this month',
      alt: 'Page 6 of WI.2: the callout quoting SPS 316.007(1)(a) adopting the 2023 National Electrical Code under CR 26-016 effective 1 September 2026 and explaining that the edition applying to a job turns on the permit application date, above the table of standards the Uniform Dwelling Code adopts by reference including ASCE 32-01, NFPA 54 and ICC 400-2012',
    },
    {
      no: 'WI.3',
      pages: '6 pages',
      title: 'Inspection Sequence',
      copy: 'The eight inspection types the code names, the three clocks that let you keep working or move in when the inspector does not show, the weather rules that stop a septic install, and a log.',
    },
    {
      no: 'WI.4',
      pages: '13 pages',
      title: 'Where to File Directory',
      copy: 'The two Department documents that resolve any parcel in the state — and almost nobody knows they exist. Plus the well and septic separation distances that decide where the house can actually go, the shoreland standards, and the floodplain rules.',
      thumb: '/kits/wi/wik-setbacks.webp',
      caption: 'WI.4 Where the well can go',
      alt: 'Page 7 of WI.4: the closing rows of the NR 812 Table A well separation distances, running from manure storage at 100 and 250 feet through quarries at 500 feet to landfills at 1,200 feet, above the callout explaining that properly abandoning an old drain field removes its 50-foot setback',
    },
    {
      no: 'WI.5',
      pages: '6 pages',
      title: 'Forms & Documents Index',
      copy: 'Every document you will meet, who produces it and where it goes — plus the twelve exemptions from the code, the two that are not really exemptions, and what to ask a subcontractor to show you.',
    },
  ],

  includes: [
    '52 print-ready pages across 6 documents, letter size',
    'Every Wisconsin claim cited on the page it appears on',
    'The NR 812 well separation distances and the SPS 383 septic setbacks in full',
    'A permit record and an inspection log for the job site',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things Wisconsin law actually says that the standard advice gets wrong. Each takes about a minute to check.',

  highlights: [
    {
      icon: 'bolt',
      label: 'Wisconsin left the 2017 NEC on 1 September 2026',
      copy: 'Every Wisconsin guide in circulation says the state is on the 2017 National Electrical Code. It stopped being true this month. SPS 316.007(1)(a) now adopts “NFPA 70 National Electrical Code, (NEC) – 2023,” by CR 26-016, Register June 2026 No. 846, effective 1 September 2026. Six editions of change arrived at once, and which one binds your job turns on your permit application date.',
    },
    {
      icon: 'doc',
      label: 'Two zone maps, numbered backwards from each other',
      copy: 'Figure 321.02 sets roof loads with Zone 1 as the north at 40 psf and Zone 2 as the south at 30 psf. SPS 322.31(1)(b) sets insulation with zone 2 as the 15 northern counties and zone 1 as everywhere else. The labels are inverted. Carry one number across and you under-frame a northern roof while under-insulating a northern wall — both wrong, in opposite directions.',
    },
    {
      icon: 'permit',
      label: 'No permit-free town, and no holding period',
      copy: 'If your municipality has not taken up enforcement, “the department shall provide inspection services and shall enforce this subchapter throughout” it (s. 101.651(3)(b)), and larger municipalities must contract for what they do not perform (s. 101.65(2)). But the owner exemption is one sentence with no strings: s. 101.654(1)(b) asks only that you “reside or will reside” in the dwelling. No holding period, no resale bar, no affidavit — the “two years” people cite is the continuing-education cycle for certified contractors.',
    },
    {
      icon: 'check',
      label: 'You may drill your own well. You may not install your own septic.',
      copy: 'NR 812.10(1)(a) exempts “an individual performing well drilling on real estate owned or leased by that individual” — though you must notify the Department before construction begins (s. 281.34(3)(a)). Septic is the reverse: the sanitary permit application cannot be completed without naming the master plumber responsible for the installation (SPS 383.21(2)(c)4.), and by statute that permit must be in hand before your building permit can issue (s. 145.195(1)).',
    },
  ],

  sourceNote:
    'Every claim was read against its primary source in September 2026: the Wisconsin Statutes and Administrative Code at docs.legis.wisconsin.gov, and the Department of Safety and Professional Services’ own delegation list, inspection map and owner brochure at dsps.wi.gov. Each table reproduced here was additionally rendered and read from the official PDF page, because the two-column code layout corrupts numbers in text extraction.',

  faqs: [
    {
      question: 'Can you build your own house in Wisconsin without a license?',
      answer:
        'Yes. Wisconsin licenses no residential general contractor. What it has instead is a credential attached to the permit — s. 101.654(1)(a) bars anyone from obtaining a building permit without a certificate of financial responsibility — and then exempts you from it in one sentence: “Paragraph (a) does not apply to an owner of a dwelling who resides or will reside in the dwelling and who applies for a building permit to perform work on that dwelling” (s. 101.654(1)(b)). The forward-looking “will reside” is deliberate and covers a house that does not exist yet. There is no holding period, no bar on selling afterward, no dollar cap and no affidavit — the full text of the statute and both administrative rules were read to confirm it. The exemption lifts the credential only: you still pull a permit, you still meet the code, and s. 101.66(1) names “every builder, designer, and owner” personally.',
    },
    {
      question: 'Do you need a building permit everywhere in Wisconsin?',
      answer:
        'Yes. Unlike Montana, Kentucky or Mississippi, Wisconsin has no gap. A city, village or town may take jurisdiction by ordinance; a municipality of 2,500 or fewer may instead ask its county; and if neither happens, “the department shall provide inspection services and shall enforce this subchapter throughout” that municipality (s. 101.651(3)(b)). Larger municipalities that do not inspect “shall contract with the department for those inspection services which the municipality does not perform” (s. 101.65(2)). The permit must be obtained “before any on-site construction, including excavation for a structure, may begin” (SPS 320.08(1)). What varies is who you call — and in a department-jurisdiction town that is a private registered UDC inspection agency, not a town hall.',
    },
    {
      question: 'Can a homeowner do their own electrical or plumbing work in Wisconsin?',
      answer:
        'This is the question Wisconsin answers least clearly, and the kit prints the texts rather than guessing. Both owner exemptions are written in the present tense: electrical covers “premises that the property owner owns and occupies as a residence” (s. 101.862(4)(a)) and plumbing covers work “in a one-family building owned and occupied by him or her as his or her home” (s. 145.06(4)(a)). Neither says “new construction,” and neither contains the forward-looking “or will reside” that the owner-builder exemption and the HVAC exemption both do — a real drafting asymmetry. One thing does settle the practical question on plumbing: SPS 320.09(9)(a)7. requires “the name and license number of the Wisconsin master plumber responsible for the installation of plumbing” to be entered on your permit at issuance. Note also that the plumbing exemption reaches a one-family building only, so it is unavailable on a duplex, and that both exemptions can be switched off by local ordinance. Ask your inspector in writing before you buy materials.',
    },
    {
      question: 'Can I install my own septic system or drill my own well in Wisconsin?',
      answer:
        'Septic, no. Well, yes. POWTS work is “plumbing” by statutory definition (s. 145.01(10)(a)2.), the homeowner plumbing exemption reaches work “in a one-family building” and a dispersal cell is not in the building, and the sanitary permit application must be accompanied by “documentation that the master plumber or the master plumber-restricted service who is to be responsible for the installation” (SPS 383.21(2)(c)4.). The soil evaluation is also credential-gated — only a certified soil tester may do it, and three soil profile evaluations are required with at least one dug as a full pit. Wells are the opposite: NR 812.10(1)(a) says a license “is not required for … an individual performing well drilling on real estate owned or leased by that individual.” You must notify the Department of Natural Resources before construction begins, all NR 812 construction standards still apply, and coliform and nitrate samples are required afterward by rule.',
    },
    {
      question: 'What building code does Wisconsin use in 2026?',
      answer:
        'The Uniform Dwelling Code, chs. SPS 320 to 325 — Wisconsin’s own code, not an adoption of the International Residential Code. Electrical changed on 1 September 2026: SPS 316.007(1)(a) now adopts the 2023 National Electrical Code, replacing the 2017 edition, under CR 26-016. Energy is SPS 322, which writes its own prescriptive tables rather than adopting the IECC — the only IECC reference is a note that the 2009 REScheck version meets the thermal envelope requirements. Fuel gas is NFPA 54, the National Fuel Gas Code, rather than the IFGC. Frost footings are “below the frost penetration level or at least 48 inches below adjacent grade, whichever is deeper,” expressly including landings and stoops (SPS 321.16). Wisconsin does not require sprinklers in a one- or two-family dwelling. Note that SPS 324 and SPS 325 are pointer chapters — electrical actually lives in ch. SPS 316 and plumbing in chs. SPS 381 to 387.',
    },
    {
      question: 'How do I find out who inspects my house in Wisconsin?',
      answer:
        'The Department publishes two documents that together resolve any parcel in the state, and almost nobody outside the trade knows they exist. First, the UDC Delegated Municipalities List — search it for your exact municipality, which in rural Wisconsin is a Town, not the city on your mailing address. If it is listed, that municipality issues your permit and does your inspections, and the list names the contact and the inspector under contract. If it is not listed, the UDC Permit and Inspection Map tells you whether to contact your county, the Department, or one of the named private inspection agencies working under state contract. Thirteen counties hold delegation, and one county is split between two agencies. Whoever it turns out to be, you are locked to them: “a person who obtains a Wisconsin uniform building permit from a registered UDC inspection agency shall retain the same agency to conduct the inspections for the project” (SPS 320.08(2)). Choose before you file.',
    },
  ],

  productDescription:
    'A 52-page print-ready permit kit for building your own home in Wisconsin, in six documents. Covers the s. 101.654(1)(b) owner exemption and its absence of any holding period, the four differently-worded trade exemptions and what each actually reaches, the four enforcement models and the two Department documents that identify yours, the 2023 National Electrical Code adoption effective 1 September 2026, the two Uniform Dwelling Code zone maps that are numbered in opposite directions, the sanitary permit that must precede the building permit by statute, and the NR 812 and SPS 383 separation distances reproduced in full. Every claim is cited on the page it appears on and was verified against the Wisconsin Statutes, the Wisconsin Administrative Code and the Department of Safety and Professional Services’ own documents in September 2026.',

  verifyNote:
    'Code editions change — Wisconsin’s electrical code changed on 1 September 2026, while this kit was being written. Confirm each rule with whoever enforces the Uniform Dwelling Code on your parcel, which may be your municipality, your county, the Department, or a private inspection agency under state contract, and confirm the septic side with your county. The kit prints its sources so you can.',

  binderLead:
    'The Owner-Builder Job Site Binder picks up where the permit kit stops — and in Wisconsin the permit is the beginning of a long supervised sequence, not the end of the paperwork. 367 pages of contracts, inspection forms, daily logs and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function WIPermitKit() {
  return <KitProductPage content={WI} />;
}
