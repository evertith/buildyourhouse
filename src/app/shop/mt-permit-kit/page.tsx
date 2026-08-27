import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/mt-permit-kit' },
  title: 'Montana Owner-Builder Permit Kit — $34',
  description:
    'Montana says its building code does not apply to your house — then requires an electrical permit your power supplier cannot connect you without, and an energy certification you sign yourself. 53 print-ready pages with the MCA citations on the page. $34 instant download.',
  keywords:
    'Montana owner builder permit, Montana building permit not required, homeowner electrical permit Montana, MCA 37-68-103, MCA 50-60-102, Montana certified building code jurisdictions, Montana contractor license 2026, Montana exempt well 35 gpm, certificate of subdivision approval Montana, Montana 2020 NEC',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const MT: KitContent = {
  slug: 'mt-permit-kit',
  heroSub:
    'Montana writes one statewide building code and then says it does not apply to your house — and most of the state has no building permit at all. Here is what still binds you anyway, verified against the Montana Code Annotated with the citations printed on the page.',
  pageCount: 53,
  revision: 'August 2026',

  heroSheets: {
    front: {
      src: '/kits/mt/mtk-exemption.webp',
      alt: 'Page 6 of MT.1, the owner-builder exemption walkthrough: the table comparing three exemptions in MCA 37-68-103 showing the homeowner clause omits the word inspection.',
    },
    back: {
      src: '/kits/mt/mtk-directory.webp',
      alt: 'Page 2 of MT.4, the where-to-file directory: Montana certified building code programs sorted by which trades each one covers.',
    },
  },

  documents: [
    {
      no: 'MT.0',
      pages: '4 pages',
      title: 'Cover & How to Use',
      copy:
        'The Montana inversion on one page — no building permit, but a state electrical permit, an energy code you certify yourself, and a sanitation law that can stop the build — plus the four questions to answer before anything else applies.',
    },
    {
      no: 'MT.1',
      pages: '15 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy:
        'The construction contractor license that replaced registration on January 1, 2026, the building code that probably does not reach your house, and the three duties that survive. Includes the kit’s headline finding: the homeowner electrical exemption is a license exemption only, while the plumbing one reaches the permit — quoted verbatim with the MCA sections on the page.',
      thumb: '/kits/mt/mtk-exemption.webp',
      caption: 'MT.1 Exemption walkthrough',
      alt: 'Page 6 of MT.1, the owner-builder exemption walkthrough: MCA 37-68-103 quoted with a table showing the homeowner exemption covers the license but not the permit or inspection.',
    },
    {
      no: 'MT.2',
      pages: '15 pages',
      title: 'Permit Application Checklist',
      copy:
        'Sanitation approval, water, septic, and access first — because in Montana those decide whether the parcel can carry a house at all — then the building permit if one exists, then the electrical permit that exists either way. Opens with the statute that bars you from erecting or occupying a building without sanitation approval.',
      thumb: '/kits/mt/mtk-checklist.webp',
      caption: 'MT.2 Application checklist',
      alt: 'Page 1 of MT.2, the permit application checklist: MCA 76-4-121 quoted in full, the statute barring construction or occupancy without sanitation approval.',
    },
    {
      no: 'MT.3',
      pages: '8 pages',
      title: 'Inspection Sequence',
      copy:
        'Two completely different regimes on the same house — the full ladder inside a certified program, and the rural build where the only inspection is electrical. Includes the power-supplier release that is the real finish line, and the record you have to build yourself when no inspector is coming.',
    },
    {
      no: 'MT.4',
      pages: '6 pages',
      title: 'Where-to-File Directory',
      copy:
        'The department’s own list of certified local programs, sorted by which trades each one actually covers — the twenty-five that are building-only, and the county where electrical is the one thing that is not local — plus the state offices and a page to fill in your own.',
      thumb: '/kits/mt/mtk-directory.webp',
      caption: 'MT.4 Where to file',
      alt: 'Page 2 of MT.4, the where-to-file directory: Montana’s certified building code programs grouped by whether they cover all four trades, building only, or a partial set.',
    },
    {
      no: 'MT.5',
      pages: '5 pages',
      title: 'Forms & Documents Index',
      copy:
        'Every document you will actually meet — including the Homeowner Electrical Permit the state publishes for exactly this — which office issues it, and the ones people go looking for that Montana does not have.',
    },
  ],

  includes: [
    '53 print-ready pages across 6 documents, letter size',
    'The homeowner electrical and plumbing exemptions, quoted verbatim (MCA 37-68-103, 50-60-506, 37-69-102)',
    'The 2026 construction contractor license and its owner exemption — the statute most Montana guides still cite as repealed law',
    'The Montana amendments that change what you build — 30 psf minimum snow load, 4 ACH50 blower door, and the two places Montana softens the NEC',
    'A checklist that runs sanitation and water first, where Montana actually starts',
    'The state’s certified-jurisdiction list sorted by which trades each program covers',
    'The rule that ends "my buddy will help me wire it" — ARM 24.301.431(8), which no Montana guide prints',
    'Statute and rule citations printed on the page, not linked away',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things in this kit that most Montana owner-builder advice gets wrong — including two that were repealed or replaced in 2026. Each is checkable in about a minute, which is the whole argument for the price.',

  highlights: [
    {
      icon: 'permit',
      label: 'The building code does not apply — that is not the same as no rules',
      copy:
        'MCA 50-60-102(1)(a) says the state building code “does not apply to … residential buildings containing less than five dwelling units” unless your local legislative body adopted it, and 50-60-102(2) says the state “may not enforce” it. Not “applies but nobody inspects” — it does not reach your house. What still does: the electrical permit, the energy code, and all of Title 76 sanitation law. The kit sequences each one.',
    },
    {
      icon: 'bolt',
      label: 'Your electrical exemption covers the license, not the permit',
      copy:
        'MCA 37-68-103 says “licensing or inspection” at subsection (2) and “licensing and inspection” at (7)(a). For the homeowner, at (3)(a), it says only “does not require an individual to hold a license.” The permit and inspection survive — and they live in Title 50, which a Title 37 exemption cannot waive. Meanwhile the plumbing exemption at 50-60-506(4) does reach the permit. Same house, opposite answers.',
    },
    {
      icon: 'doc',
      label: 'Montana wires to the 2020 NEC — and amends it downward',
      copy:
        'The adopted National Electrical Code is the 2020 edition, effective June 11, 2022 — two editions behind the national cycle, in a state that lets you legally wire your own house. Then Montana amends it: ARM 24.301.401 removes 250-volt receptacles from the 210.8 GFCI requirement and deletes every reference to kitchens from the 210.12 AFCI requirement, making the state less stringent than the model code in both places. A national checklist will have you doing work Montana does not require; a 2023-edition habit will have you missing what it does. The kit prints the rule numbers.',
    },
    {
      icon: 'check',
      label: 'You may not even erect the building without sanitation approval',
      copy:
        'MCA 76-4-121 bars anyone from “erect[ing] any building or shelter … that requires facilities for the supply of water or disposal of sewage” — or occupying it — until a certificate of subdivision approval, a municipal service certification, or a properly quoted exemption exists. It sits outside the building-code chapter entirely, so “no building permit required” does not touch it. The kit shows you how to check a parcel from the recorded plat before you buy.',
    },
  ],

  sourceNote:
    'Verified against the Montana Code Annotated at mca.legmt.gov and the Department of Labor & Industry Building Codes Program, August 2026 · Citations printed on each page',

  faqs: [
    {
      question: 'Can you build your own house in Montana?',
      answer:
        'Yes, and Montana is one of the most permissive states for it. An owner working on the owner’s property is exempt from the construction contractor license "whether occupied by the owner or not" (MCA 37-45-104(13)) — the only condition is that you are not building it with the intention of promptly selling, and even that has a 12-month primary-residence escape. The state building code does not apply to a residential building of fewer than five dwelling units unless your local government adopted it. But an electrical permit, an energy certification, and county sanitation approval all still apply. The kit works each track.',
    },
    {
      question: 'Do you need a permit to build a house in Montana?',
      answer:
        'Across most of Montana by area, there is no building permit to apply for. MCA 50-60-102(1)(a) takes residential buildings of fewer than five dwelling units out of the state building code unless the local legislative body adopted it, and 50-60-102(2) says the state "may not enforce" it for them. Montana has 56 counties and only six county-level programs on the state’s certified list, two of them commercial-only. You will still need an electrical permit, a septic permit, sanitation approval on the parcel, and usually an address and approach permit.',
    },
    {
      question: 'Can a homeowner do their own electrical work in Montana?',
      answer:
        'Yes — but read the exemption carefully, because it is narrower than it looks. MCA 37-68-103(3)(a) says the chapter "does not require an individual to hold a license" for work on your own property maintained for your own use. It does not say inspection, and it does not say permit — while two neighboring subsections in the same section do say "licensing and inspection." So you still need the electrical permit and the inspection, and the state publishes a Homeowner Electrical Permit form for exactly this. One carve-out: grid-tied generator work, including grid-tied solar, is expressly not exempt (37-68-103(3)(b)).',
    },
    {
      question: 'Can a homeowner do their own plumbing in Montana?',
      answer:
        'Yes, and the statute is unusually broad: MCA 50-60-506(4) lets "the owner of residential property" install all sanitary plumbing and potable water supply piping "without a permit if the owner personally does the work" — no single-family limit and no occupancy condition in the statute itself. But do not stop at the statute. The administrative rule adds a condition the code does not contain: ARM 24.301.361(3) bars an owner permit where the residence is built on speculation of sale or rent and is not the owner’s primary residence in which they will reside, and ARM 24.301.431(3) does the same on the electrical side. Montana keeps a great deal of what governs your house in the rules rather than the code, which is why the kit prints both.',
    },
    {
      question: 'Does Montana require a contractor license?',
      answer:
        'As of January 1, 2026, yes — and this caught almost every Montana guide out. The old Construction Contractor Registration at MCA Title 39, chapter 9 was repealed and renumbered; the live chapter is Title 37, chapter 45, and 37-45-201(1) says no one may "engage in business as a construction contractor without a current license from the department." Owners working on their own property are exempt (37-45-104(13)). The reason it matters to you: engaging a contractor who is licensed on the date of the contract shields you from liability as an employer for workers’ compensation, unemployment insurance, and wages (37-45-202). Hire an unlicensed one and that shield never attaches.',
    },
    {
      question: 'My Montana county has no building department. Do I still need anything?',
      answer:
        'Yes, and the expensive ones are not building permits. MCA 76-4-121 says a person "may not … erect any building or shelter … that requires facilities for the supply of water or disposal of sewage" — or occupy it — until the parcel has sanitation approval or a properly recorded exemption. You will also need an electrical permit (no power supplier may energize without it, and doing so is a misdemeanor under 50-60-607); a county septic permit, which is separate from the sanitation certificate; a DNRC Notice of Intent on Form 602I, with a $400 fee, filed and authorized before you drill a well — new under House Bill 681, effective January 1, 2026; a 911 address; and a written energy certification you sign yourself under 50-60-802. The kit is organized around exactly this stack.',
    },
  ],

  productDescription:
    'Montana owner-builder permitting, start to finish: the exemption walkthrough (the 2026 construction contractor license, the building code that does not reach a house of fewer than five dwelling units, and the electrical permit, energy certification, and sanitation law that bind you anyway), the permit application checklist, the inspection sequence, the where-to-file directory built on the state’s own certified-jurisdiction list, and the forms index. 53 print-ready pages across 6 documents, with the MCA citations printed on the page. Verified against the Montana Code Annotated at mca.legmt.gov and the Department of Labor & Industry Building Codes Program, August 2026.',

  verifyNote:
    'Statutes and adopted code editions change, and in Montana almost everything turns on one question: whether your city or county appears on the state’s certified building-code jurisdiction list, and for which trades. Confirm that first, then confirm each permit with the office that will actually issue it. The kit prints its sources so you can.',

  binderLead:
    'The kit settles which permits exist for your parcel and which offices own them. The binder runs the build: 367 pages of contracts, inspection forms, daily logs, and budget trackers covering every phase from footing to final — and in a state where no building inspector may ever visit, that record is the only construction history your house will have.',
};

export default function MTPermitKit() {
  return <KitProductPage content={MT} />;
}
