import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/ne-permit-kit' },
  title: 'Nebraska Owner-Builder Permit Kit — $34',
  description:
    'Nebraska permit kit: the 2018 code that binds your house even where no county inspects it, the electrical request that is now a felony to skip, the septic system you may not install and the well you may, and the energy code you enforce on yourself. 51 print-ready pages, every claim cited. $34 instant download.',
  keywords:
    'Nebraska owner builder permit, Nebraska building permit, Nebraska state building code 2018 IRC, Nebraska State Electrical Division homeowner permit, § 81-2121(5), § 71-6406, Nebraska septic registration Title 124, Nebraska well registration, radon resistant new construction Nebraska, Nebraska Energy Code',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const NE: KitContent = {
  slug: 'ne-permit-kit',
  heroSub:
    'Nebraska does not ask whether the code applies to your house — the statute says it does, whether or not anyone enforces it. The question is who can stop you, and on most rural parcels the answer is the power company, the septic installer, and you.',
  pageCount: 51,
  revision: 'September 2026',

  heroSheets: {
    front: {
      src: '/kits/ne/nek-hero-front.webp',
      alt: 'Nebraska Owner-Builder Permit Kit page quoting the statute that makes the state building code the legally applicable code regardless of whether the county, city, or village has provided for its administration or enforcement, above a table of what follows from that sentence',
    },
    back: {
      src: '/kits/ne/nek-hero-back.webp',
      alt: 'Kit page listing the five counties and fourteen cities that run their own electrical inspection programs under the State Electrical Division map, noting that everyone else is inspected by the state and that La Vista, Waverly and Boys Town are state-inspected despite the county around them',
    },
  },

  documents: [
    {
      no: 'NE.0',
      pages: '3 pages',
      title: 'Cover & How to Use',
      copy: 'A job-site cover with the two fields Nebraska actually makes you resolve — the building permit office, which may honestly be none, and the electrical inspection, which never is. Plus the one-page orientation.',
    },
    {
      no: 'NE.1',
      pages: '15 pages',
      title: 'What Binds You and Who Can Stop You',
      copy: 'Nebraska has no owner-builder exemption because it has nothing to be exempt from: no contractor license, no state permit, no state inspector for a house. So this walks the question that actually decides your build — the sentence that makes the 2018 code apply without a building department, the four state obligations that reach every parcel anyway, what you may do with your own hands trade by trade, and the registration act that governs everyone you hire.',
      thumb: '/kits/ne/nek-electrical.webp',
      caption: 'NE.1 What still applies to you, in the statute’s words',
      alt: 'Page 7 of NE.1: a table quoting the State Electrical Act on why a new house is inspected everywhere, the request for inspection due before work starts with its $250 late fee, and the certificate the owner must file with the utility before power is connected — above a boxed note that since July 18, 2026 failing to file is a Class IV felony while the Division’s own rules still say misdemeanor',
    },
    {
      no: 'NE.2',
      pages: '12 pages',
      title: 'Permit Application Checklist',
      copy: 'The paperwork that exists whether or not your county created a building permit: the code editions actually in force, the five NEC sections Nebraska holds at their 2017 text, the 2018 energy values for the one climate zone the whole state sits in, the radon standard and its two exemptions with the county list, the electrical fee schedule with a worked example, and the septic and well packages with their setback tables, sizing tables and fees.',
      thumb: '/kits/ne/nek-nec.webp',
      caption: 'NE.2 The 2023 NEC, with five sections held at 2017',
      alt: 'Page 3 of NE.2: the statute adopting the 2023 National Electrical Code quoted verbatim with its exception for five sections that stay on the 2017 edition, above a table naming each section — dwelling-unit GFCI locations, outdoor and basement receptacles, the service surge-protective device and the emergency disconnect — and a checklist for the editions the kit will not guess at',
    },
    {
      no: 'NE.3',
      pages: '8 pages',
      title: 'Inspection Sequence',
      copy: 'The one inspection track the statute fixes — electrical, with its one-week response clock, the rough-in that must come before drywall, the correction order of ten to seventeen days, and the five-month permit life — plus the septic and well registrations that stand in for every other inspection, the 2026 rule on virtual inspections that forbids self-inspection, and what to do where nobody is required to inspect you.',
      thumb: '/kits/ne/nek-sequence.webp',
      caption: 'NE.3 The electrical sequence, and three clocks on the permit',
      alt: 'Page 3 of NE.3: the final, correction and meter steps of the electrical inspection sequence with their statutory cites, above a boxed explanation of the three clocks on the permit — the request due before work starts with a felony behind it, the five-month void rule, and the two doorknob notices an inspector leaves before an owner’s file goes quiet',
    },
    {
      no: 'NE.4',
      pages: '8 pages',
      title: 'Where to File Directory',
      copy: 'Nebraska publishes one authoritative lookup — the State Electrical Division map of who inspects electrical at any address — and publishes nothing on which counties issue building permits, because no statute requires one to. So this is the map and how to read it, the three-question check you run yourself, the four state agencies and which does what, Lincoln and Sarpy County worked from their own documents, and the confirm-at-the-counter instruction for Omaha.',
    },
    {
      no: 'NE.5',
      pages: '5 pages',
      title: 'Forms & Documents Index',
      copy: 'Every document you will meet, named as the agency names it — and nine things Nebraska does not have, from a state building permit to an owner-builder affidavit, so nobody sells you one. Plus the one thing you may not do yourself, and the lien paper to keep.',
    },
  ],

  includes: [
    '51 print-ready pages across 6 documents, letter size',
    'Every Nebraska claim cited on the page it appears on',
    'Write-in lines for everything that varies by city or county',
    'A permit record, an inspection log and a confirmed-offices page for the job site',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things Nebraska law actually says that the standard advice gets wrong. Each takes about a minute to check.',

  highlights: [
    {
      icon: 'doc',
      label: 'The code binds without a permit',
      copy: 'Nebraska adopts the 2018 IRC and 2018 Uniform Plumbing Code by statute (Neb. Rev. Stat. § 71-6403(1)) and then says something almost no other state says: the state code “shall be the legally applicable code regardless of whether the county, city, or village has provided for the administration or enforcement” of it (§ 71-6406(7)). Local governments “may” run permits and inspections — nothing says they must, and no state agency may inspect a private house. Nor may a county run an older edition: a local code “shall not be deemed to conform” if it “includes a prior edition of any component” (§ 71-6406(3)(a)). A county still on the 2012 IRC is telling you something the statute forbids.',
    },
    {
      icon: 'bolt',
      label: 'Skipping the electrical request is a felony',
      copy: 'The homeowner exemption at § 81-2121(5) excuses you from the electrician’s license on your principal residence — and from nothing else. Every new single-family service is inspected (§ 81-2124(3)), the owner must file a request for inspection “at or before commencement” with a $250 delinquent fee for filing late (§ 81-2126), and the utility may not connect you “until there is filed with the electrical utility supplying power a certificate of the property owner” that inspection was requested (§ 81-2129). Then Laws 2026, LB889 rewrote the penalty: effective July 18, 2026, failing “to file a request for inspection when required” is a Class IV felony (§ 81-2143(1)(c)). The State Electrical Board’s own rules PDF, dated April 2024, still says misdemeanor.',
    },
    {
      icon: 'permit',
      label: 'Drill the well yourself; not the septic',
      copy: 'Published Nebraska guides have this backwards. On wells: “an individual may construct a water well or install and repair pumps and pumping equipment onsite on land owned by him or her and used by him or her … as his or her place of abode” (§ 46-1233(2)), to the Title 134 standards, registered within 60 days for $200 plus $25–$40 (§§ 46-602(1), 46-606(1)). On septic: no system “shall be sited, laid out, constructed … or inspected unless” the work “is carried out or supervised by” a certified professional, engineer or environmental health specialist (§ 81-15,248(1)) — and Title 124 ch. 9 § 004 requires that person to be “physically present at the site.” The professional, not you, registers it within 45 days for $140.',
    },
    {
      icon: 'check',
      label: 'Your code book is wrong in five places',
      copy: 'Nebraska is on the 2023 NEC, effective August 1, 2024 — current, not lagging. But § 81-2104(5) holds five sections at their 2017 text: 210.8(A), 210.8(A)(3) and 210.8(A)(5) — the dwelling-unit GFCI list, outdoor and basement receptacles — plus 230.67(A) surge protection and 230.85 the emergency disconnect. No AFCI section is on the list, whatever the guides say. And there is no state amendment table anywhere else: the Building Construction Act adopts the I-Codes by reference with named exclusions and nothing more, so the substance lives in local amendments. Lincoln, for one, is on the 2021 IRC and UPC — lawfully ahead of the state.',
    },
  ],

  sourceNote:
    'Every claim was read against its primary source in September 2026: the Nebraska Revised Statutes as the Legislature publishes them at nebraskalegislature.gov, including the Source and Effective Date lines on each section and the 2026 slip laws LB889 and LB441; DWEE’s Title 124 and Title 134 rule titles and its energy-code fact sheet; DHHS’s county radon determination; the State Electrical Division’s application form, rules, homeowner handout and inspection-jurisdiction map layer, which was queried feature by feature rather than read off a screenshot; Lincoln’s own code and homeowner-permit pages; and Sarpy County Resolution 2024-150.',

  faqs: [
    {
      question: 'Can you build your own house in Nebraska without a license?',
      answer:
        'Yes, and there is nothing to apply for. Nebraska issues no general contractor license. Its only statewide contractor law is the Contractor Registration Act, a $40 annual registration with the Department of Labor for people who work on property other than their own — and it says so directly: “Any person who performs work or has work performed on his or her own property … is not a contractor for purposes of the Contractor Registration Act” (Neb. Rev. Stat. § 48-2104(1)). That is why Nebraska has no owner-builder exemption: there is nothing to be exempt from. There is no frequency cap either, but building a house “to be held either for sale or rental” makes you a contractor under § 48-2103(3), and a house that is not your principal residence is outside the electrical homeowner exemption. Every trade you hire must be in the registry, which shows whether they carry workers’ compensation — the fact that decides your own exposure under § 48-116.',
    },
    {
      question: 'Do I need a building permit to build a house in Nebraska?',
      answer:
        'Only if your city or county created one, and many never did. Nebraska has no state building permit for a house and no statute requiring a county, city or village to issue one: § 71-6406(7) says a local government “may” adopt amendments for “inspections, appeals, permits, and fees,” and the state has no residential permit program at all. The same subsection then says the state building code “shall be the legally applicable code regardless of whether the county, city, or village has provided for the administration or enforcement” — so the 2018 IRC and UPC bind your house whether or not anyone inspects it. Two things survive even where no building code exists. In a zoned county, § 23-114.04 requires a zoning permit before construction of “any nonfarm building,” and that permit must show “sanitation, plumbing and sewage disposal”; building without one is a Class III misdemeanor. And no state list exists of which counties run programs, so the kit gives you the three-question check — county clerk, city clerk, and the State Electrical Division map — and a page to record the answers.',
    },
    {
      question: 'Can a homeowner do their own electrical work in Nebraska?',
      answer:
        'Yes, without a license, on your principal residence “if such residence is not larger than a single-family dwelling, or farm property” (§ 81-2121(5)). Read the exemption exactly: it excuses the license and nothing else. It does not say “without compensation” and it does not say you must personally do the work — those conditions appear in guides, not in the statute or the State Electrical Division’s handout. What the handout does require is a signed homeowner verification that you know the code and the Act. The inspection still applies: every new single-family service is inspected (§ 81-2124(3)), the request for inspection is due “at or before commencement” with the fees (§ 81-2126), and the power company may not connect you until you certify to it that inspection was requested (§ 81-2129). Fees on the March 27, 2026 form are $75 for a new service up to 400 amps plus $10 per branch circuit, with a $100 homeowner minimum; a 200-amp house with 30 circuits is $375. The online permitting system went live April 13, 2026. Failing to file the request has been a Class IV felony since July 18, 2026 (§ 81-2143(1)(c)).',
    },
    {
      question: 'Which building code does Nebraska use in 2026?',
      answer:
        'The 2018 editions, by statute, unchanged since a 2021 conforming amendment. Neb. Rev. Stat. § 71-6403(1) adopts the 2018 International Building Code, the 2018 International Residential Code “except section R313 and chapters 25 through 33,” the 2018 International Existing Building Code, and the 2018 Uniform Plumbing Code — the UPC, not the IPC and not the IRC plumbing chapters, which is why those chapters are excluded. Radon-resistant construction standards are folded in by § 71-6403(2). Under separate acts the electrical code is the 2023 NEC, effective August 1, 2024, with five sections held at their 2017 text (§ 81-2104(5)), and the energy code is the unamended 2018 IECC with the whole state in climate zone 5 (§ 81-1609(9)). A local government may adopt a newer edition and still conform — Lincoln is on the 2021 IRC, UPC, IMC and IEBC — but may not run an older one (§ 71-6406(3)(a)). Only the Legislature can change the editions; no 2021 or 2024 adoption bill had passed as of September 2026.',
    },
    {
      question: 'Can I install my own septic system or drill my own well in Nebraska?',
      answer:
        'Drill the well, yes. Install the septic system, no — and most published guides have the two backwards. Section 46-1233(2) lets “an individual … construct a water well or install and repair pumps and pumping equipment onsite on land owned by him or her and used by him or her for farming, ranching, or agricultural purposes or as his or her place of abode.” The exemption is from the driller’s license, not the construction standard, which is DWEE Title 134 chapter 4, effective June 28, 2026 (it replaced the old Title 178 chapter 12). You register the well within 60 days for $200 plus $25–$40 and keep the well log. The septic rule runs the other way: § 81-15,248(1) forbids any onsite wastewater system to be “sited, laid out, constructed … or inspected” unless the work is “carried out or supervised by” a certified professional, a Nebraska-licensed engineer or a registered environmental health specialist, and Title 124 chapter 9 § 004 requires that person to be “physically present at the site.” You may dig beside a Master Installer who stays on site; you may not build it alone. The professional registers the system within 45 days for $140. Setbacks are Title 124 Table 2.1: 100 feet from drainfield to a private well, 50 from the tank, 5 to a property line, and 10 feet to your foundation — rising to 30 feet if any part of the basement or footing sits lower than the system.',
    },
    {
      question: 'Does Nebraska require radon-resistant new construction?',
      answer:
        'Yes, statewide, by statute — with two exemptions the guides miss. Section 76-3504 requires radon-resistant new construction in every building “intended to be regularly occupied by people” built after September 1, 2019, and a local code that omits it does not conform (§ 71-6406(3)(b)). The statutory standard is shorter than IRC Appendix F: gasketed sump lids, a three-inch gas-tight vent pipe embedded in the subslab permeable material and run twelve inches above the roof and ten feet from openings, labels reading “Radon Reduction System,” and an electrical box in the attic for a future fan. There is no aggregate depth and no vapor retarder in the statute. Section 76-3505 exempts any project that “utilizes the design of an architect or professional engineer,” and any county whose average radon is below 2.7 pCi/L as determined by DHHS. DHHS’s January 2024 determination put 77 of 93 counties above the threshold; the fourteen below it are Blaine, Cherry, Dundy, Grant, Lincoln, Logan, Loup, McPherson, Merrick, Rock, Sheridan, Sioux, Thomas and Wheeler, with Arthur untested and Hall at exactly 2.7 — which is not “less than.” The list is redetermined annually. Radon is DHHS; onsite wastewater is DWEE.',
    },
  ],

  productDescription:
    'A 51-page print-ready permit kit for building your own home in Nebraska, in six documents. Covers the question that decides a Nebraska build — what binds your house and who can stop you — starting from the sentence at Neb. Rev. Stat. § 71-6406(7) that makes the 2018 IRC and UPC the legally applicable code whether or not any county administers it, and the four state obligations that reach every parcel anyway: the state electrical inspection enforced at the meter under §§ 81-2124, 81-2126 and 81-2129, with the Class IV felony LB889 added on July 18, 2026; the Nebraska Energy Code the owner-builder enforces on himself under § 81-1622; the septic registration a certified professional must make under § 81-15,248; and the well registration under § 46-602. Also the five NEC sections held at 2017 text, the radon standard and its two exemptions with DHHS’s county list, the Title 124 setback and sizing tables, the Title 134 well distances, the county zoning permit at § 23-114.04, the Contractor Registration Act, the lien protections of a “protected party,” and the State Electrical Division map of the five counties and fourteen cities that inspect their own electrical. Every claim is cited on the page it appears on and was verified against the Nebraska statutes, the agencies’ rule titles and forms, and the cities’ own documents in September 2026.',

  verifyNote:
    'Statutes, rules and code editions change, and three Nebraska answers moved in 2026 alone: the electrical penalty became a felony on July 18, the well standards moved to Title 134 on June 28, and the electrical fee schedule and online permit system changed in April. The radon county list is redetermined every year. Confirm each rule with the office that will handle your parcel — and where no office exists, with the statute page itself, which carries its own effective date. The kit prints its sources so you can.',

  binderLead:
    'The Owner-Builder Job Site Binder picks up where the permit kit stops — and in Nebraska, where most rural houses are never inspected by anyone but the electrical inspector and your own record is the only one that will exist, your paperwork matters more than usual. 367 pages of contracts, inspection forms, daily logs and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function NEPermitKit() {
  return <KitProductPage content={NE} />;
}
