import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/tn-permit-kit' },
  title: 'Tennessee Owner-Builder Permit Kit — $34',
  description:
    'Tennessee permit kit: the three-way jurisdiction map and the opt-out that expires 180 days after the next election, the electrical permit that survives it, the 2017 NEC nobody expects, and the moment your own trades become prime contractors. 39 print-ready pages, every claim cited. $34 instant download.',
  keywords:
    'Tennessee owner builder permit, Tennessee building permit, owner builder exemption Tennessee, 62-6-103, Tennessee opt out county building code, SRBP Tennessee, Tennessee 2017 NEC, TDEC septic permit Tennessee',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const TN: KitContent = {
  slug: 'tn-permit-kit',
  heroSub:
    'Tennessee has one residential code and three different answers to who enforces it — and the answer for your county expires 180 days after its next election.',
  pageCount: 39,
  revision: 'September 2026',

  heroSheets: {
    front: {
      src: '/kits/tn/tnk-hero-front.webp',
      alt: 'Tennessee Owner-Builder Permit Kit page quoting the state licensing booklet line that bidding to a homeowner acting as their own general contractor makes a subcontractor a prime, above a table of the trades that need a state license at $25,000',
    },
    back: {
      src: '/kits/tn/tnk-hero-back.webp',
      alt: 'Kit page listing the code editions in force in Tennessee, with the electrical row reading 2017 National Electrical Code and a callout explaining that the state is two cycles behind',
    },
  },

  documents: [
    {
      no: 'TN.0',
      pages: '3 pages',
      title: 'Cover & How to Use',
      copy: 'A job-site cover with a field no other kit in this line has — Jurisdiction Status, because in Tennessee the answer is one of three published labels and everything else branches on it. Plus the one-page orientation.',
    },
    {
      no: 'TN.1',
      pages: '10 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy: 'How to find your jurisdiction’s status in five minutes, the exemption quoted in full, the two-year rule that is actually two different rules, and the definition that quietly turns every trade you hire into a prime contractor.',
      thumb: '/kits/tn/tnk-exemption.webp',
      caption: 'TN.1 The moment your subs become primes',
      alt: 'Page 5 of TN.1: a boxed quotation from the state contractor licensing booklet ending with the note that bidding to a homeowner acting as their own GC makes you a prime, followed by a table giving the licensing threshold for each trade — $25,000 for electrical, plumbing, mechanical and roofing, $100,000 for masonry, and $25,000 for any other trade bidding directly to the owner',
    },
    {
      no: 'TN.2',
      pages: '9 pages',
      title: 'Permit Application Checklist',
      copy: 'Every code edition in force including the 2017 NEC, the state fee schedule with the minimum cost per heated square foot that sets your fee, the septic package in order, the well filings, and the sinkhole rule that turns a drainage decision into an injection well.',
      thumb: '/kits/tn/tnk-checklist.webp',
      caption: 'TN.2 What is actually in force in Tennessee',
      alt: 'Page 2 of TN.2: a table of the codes binding a Tennessee house — 2018 International Residential Code, 2017 National Electrical Code, energy provisions reverted to the 2009 tables, plumbing and mechanical from the IRC rather than the 2021 IPC — above a callout headed that the 2017 NEC is the single most expensive assumption in Tennessee',
    },
    {
      no: 'TN.3',
      pages: '7 pages',
      title: 'Inspection Sequence',
      copy: 'Two inspection programs run over one Tennessee house and only one of them stops when your county opts out. The state sequence quoted from the rule, the separate electrical track, the insulation trap that depends on which product you bought, and a log.',
      thumb: '/kits/tn/tnk-inspections.webp',
      caption: 'TN.3 Two programs, one house',
      alt: 'Page 1 of TN.3: a table setting the three jurisdiction statuses against who performs the building inspections and who performs the electrical inspections, showing that the electrical column reads state in every row including the thirty-seven opt-out counties',
    },
    {
      no: 'TN.4',
      pages: '6 pages',
      title: 'Where to File Directory',
      copy: 'Tennessee publishes the answer — this shows you where the list lives, how to read it city-first, and the place where two official state pages contradict each other about which counties the state enforces.',
    },
    {
      no: 'TN.5',
      pages: '4 pages',
      title: 'Forms & Documents Index',
      copy: 'Every document you will meet, named as the agency names it, with what it costs. Plus what needs no permit at all, what Tennessee never asks for, and the one job you may not do yourself.',
    },
  ],

  includes: [
    '39 print-ready pages across 6 documents, letter size',
    'Every Tennessee claim cited on the page it appears on',
    'Write-in lines for everything that varies by jurisdiction',
    'A permit record, an inspection log and a confirmed-offices page for the job site',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things Tennessee law actually says that the standard advice gets wrong. Each takes about a minute to check.',

  highlights: [
    {
      icon: 'doc',
      label: 'The opt-out expires — it is not permanent',
      copy: 'Thirty-seven counties have opted out of the state residential code, and almost every guide treats that as settled. It is not. A resolution “shall expire one hundred eighty (180) days following the date of the election for the local legislative body next occurring following the adoption of the resolution.” If the incoming body does not pass it again, the State Fire Marshal resumes enforcement automatically. The rule requiring a jurisdiction to file “the date of the next election” when it opts out (0780-02-23-.14) exists precisely because of that sunset.',
    },
    {
      icon: 'bolt',
      label: 'Opting out does not end the electrical permit',
      copy: 'The building program rests on Title 68, Chapter 120; the electrical program on Title 68, Chapter 102. The opt-out is written against “the standards established pursuant to subsection (a)” — the building standards — and rule chapter 0780-02-01 contains no opt-out mechanism at all. Cross-checking the state’s electrical exempt list against the 37 residential opt-out counties returns zero overlap: every one of them is still inside the State Electrical Program, still buys a state permit, and still gets a rough-in and a final inspection.',
    },
    {
      icon: 'permit',
      label: 'Your exemption makes everyone else a prime',
      copy: 'Tennessee defines a prime contractor as “one who contracts directly with the owner.” Under a licensed builder, a framing or excavation sub bids to the contractor and needs no state license. When you are the general contractor they all bid to you — and the state’s own licensing booklet spells out the consequence: “Bidding to a homeowner acting as their own GC makes you a ‘Prime’.” So any single trade contract on your job at $25,000 or more needs a licensed contractor, including trades that would need none under a professional builder.',
    },
    {
      icon: 'check',
      label: 'The state is on the 2017 NEC, and no blower door',
      copy: 'Chapter 0780-02-01 was revised in July 2025 and still adopts the “National Electrical Code, 2017 edition,” with arc-fault protection made optional for bathrooms, laundry areas, garages and unfinished basements. Separately, Tennessee adopts the 2018 energy code and then amends its teeth back to 2009: the mandatory air-leakage test is replaced by a choice of a test or a visual inspection, duct testing is optional, and the insulation tables are the 2009 ones. Build to 2018 IECC R-values here and you are meeting a standard the state does not impose.',
    },
  ],

  sourceNote:
    'Every claim was read against its primary source in September 2026: the Secretary of State’s official rule chapters at publications.tnsosfiles.com — 0780-02-23 residential, 0780-02-01 electrical, 0400-48-01 septic, 0400-45-09 wells, 0400-45-06 underground injection — together with the State Fire Marshal’s own jurisdiction table, fee schedule and FAQs, the Board for Licensing Contractors’ rules as revised 18 November 2025, and TDEC’s own application form CN-0971.',

  faqs: [
    {
      question: 'Can you build your own house in Tennessee without a contractor license?',
      answer:
        'Yes. Tenn. Code Ann. § 62-6-103 exempts any person who owns property and constructs a single residence on it “for individual use, and not for resale, lease, rent or other similar purpose.” There is no dollar cap — the $25,000 threshold is what makes someone a contractor in the first place, and your own home is exempt at any value. You may also act as your own general contractor rather than only swinging your own hammer. Two conditions matter: the state permit rule defines a property owner’s permit as one for a dwelling “in which the owner intends to live upon completion,” and there is a two-year frequency limit that works differently in the statute than at the permit counter.',
    },
    {
      question: 'What is the Tennessee one-house-every-two-years rule?',
      answer:
        'It is two rules wearing the same number, and the difference decides what happens if you build two. In the statute it is a rebuttable presumption: there is a “rebuttable presumption that the person or firm intends to construct for the purpose of resale, lease, rent or any other similar purpose if more than one (1) application is made for a permit to construct a single residence or if more than one (1) single residence is constructed within a period of two (2) years.” Note it can be triggered by applications, not only finished houses — and it shifts the burden to you rather than barring you outright. At the permit counter it is a hard bar: rule 0780-02-23-.05(3) says “an individual may obtain only one (1) property owner’s permit within a twenty-four (24) month period.” That permit rule is the state program’s; an exempt jurisdiction applies its own.',
    },
    {
      question: 'Do all Tennessee counties require a building permit for a new home?',
      answer:
        'No, and the State Fire Marshal publishes the answer for every jurisdiction in the state. Each of the 95 counties and 378 municipalities is tagged EXEMPT (the local government runs its own building department), SRBP (the state enforces and you buy the permit at core.tn.gov), or OPT OUT (no residential building code is enforced at all). As of the table’s own currency date of 21 August 2026 that broke down as 50 counties exempt, 8 state-enforced and 37 opted out. Two things catch people: the unit is the jurisdiction rather than the county, so a city inside an opted-out county frequently has its own building department — Grundy County is opted out while Monteagle inside it is exempt — and an opt-out resolution expires 180 days after that legislative body’s next election unless the new body passes it again.',
    },
    {
      question: 'Do I still need an electrical permit in a Tennessee no-code county?',
      answer:
        'Yes, and this is the most expensive misunderstanding in Tennessee. The building code and the electrical code rest on different chapters of the law — Title 68, Chapter 120 for building and Title 68, Chapter 102 for electrical — and the opt-out provision is written only against the building standards. Rule chapter 0780-02-01 contains no opt-out mechanism at all and forbids any local government from adopting “less stringent electrical standards.” Cross-checking the state’s list of electrically exempt jurisdictions against the 37 residential opt-out counties returns zero overlap. So in every one of those counties you still buy a state electrical permit and still receive state electrical inspections, normally a rough-in and a final. A homeowner may do the work personally on a residential property owner’s electrical permit, but only one such permit is issued per twelve months — a different clock from the building permit’s twenty-four.',
    },
    {
      question: 'What building code does Tennessee use for new homes in 2026?',
      answer:
        'The state program adopts the 2018 International Residential Code with Appendix Q and ten Tennessee amendments, and the 2017 National Electrical Code — not the 2020 or 2023 edition. The electrical rule chapter was revised in July 2025 and still names the 2017 NEC, so this is a current document rather than a stale one, and it makes arc-fault protection optional for bathrooms, laundry areas, garages and unfinished basements. Energy is the part most people get wrong: Tennessee adopts the 2018 IECC or Chapter 11 of the 2018 IRC and then replaces the envelope tables and the testing provisions with the 2009 editions, so there is no mandatory blower door test and duct testing is expressly optional. Plumbing, mechanical and fuel gas come from the IRC’s own chapters, not from the 2021 IPC or IMC, which are adopted in a separate commercial rule. An exempt jurisdiction runs its own adopted code and need only stay within seven years of the current published edition, so a large city may be on something newer.',
    },
    {
      question: 'Who issues septic permits in Tennessee?',
      answer:
        'TDEC — the Department of Environment and Conservation, Division of Water Resources — not the county health department. The rule chapter’s own administrative history records that it was “renumbered from 1200-01-06,” the Health Department’s series, when it moved in 2013, so any guide still sending you to the health department is working from pre-2013 sources. You apply on form CN-0971 and mail it to the environmental field office shown on page 2 of the form, and the baseline cost for a conventional single-family system is $400 for the permit evaluation plus a required $100 construction inspection. Nine counties are contract counties served by their own environmental health office rather than a state field office — Shelby, Madison, Davidson, Williamson, Hamilton, Knox, Blount, Sevier and Jefferson. One sequencing trap worth knowing: in counties without a countywide building permit program, you must show the electrical inspector evidence that a septic application has been made before power is released.',
    },
  ],

  productDescription:
    'A 39-page print-ready permit kit for building your own home in Tennessee, in six documents. Covers the three-way jurisdiction map the State Fire Marshal publishes and the opt-out resolution that expires 180 days after the next local election, the electrical permit that survives that opt-out in all 37 no-code counties, the owner exemption at Tenn. Code Ann. § 62-6-103 and the two-year rule that is a rebuttable presumption in the statute and a hard bar at the permit counter, the definition that turns every trade you hire into a prime contractor at $25,000, the 2017 NEC and the energy provisions reverted to 2009 tables, the state fee schedule and the minimum cost per heated square foot that sets your fee, the TDEC septic sequence and its nine contract counties, the well filings and the licensed-driller requirement, and the karst rule that turns draining to a sinkhole into a regulated injection well. Every claim is cited on the page it appears on and was verified against the Secretary of State’s official rule chapters and the agencies’ own documents in September 2026.',

  verifyNote:
    'Statutes, rules and code editions change, and one Tennessee answer changes by design: an opt-out resolution expires 180 days after that legislative body’s next election, so the jurisdiction map churns. Re-check your status on the State Fire Marshal’s dated table before you file, not just before you buy the land, and confirm each rule with the office that will handle your parcel. The kit prints its sources so you can.',

  binderLead:
    'The Owner-Builder Job Site Binder picks up where the permit kit stops — and in Tennessee you may be running the job with no building inspector required to look at it, which makes your own records the only evidence there is. 367 pages of contracts, inspection forms, daily logs and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function TNPermitKit() {
  return <KitProductPage content={TN} />;
}
