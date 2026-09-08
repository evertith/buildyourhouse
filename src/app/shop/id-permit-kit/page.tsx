import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/id-permit-kit' },
  title: 'Idaho Owner-Builder Permit Kit — $34',
  description:
    'Idaho permit kit: the building permit your county may never have created, the three state trade permits that apply anyway and are enforced at the power meter, the homeowner permit that cannot get construction power, the 2023 NEC Idaho amended downward, and the 2024 code update the Legislature rejected. 43 print-ready pages, every claim cited. $34 instant download.',
  keywords:
    'Idaho owner builder permit, Idaho building permit no county building department, DOPL homeowner electrical permit, Idaho Code 54-5205 owner exemption, Idaho Code 54-1005 power supplier inspection, IDAPA 24.39.10, Idaho 2018 IRC, Idaho energy code 39-9701, Idaho septic permit health district, IDWR drilling permit',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const ID: KitContent = {
  slug: 'id-permit-kit',
  heroSub:
    'Idaho never put your house under a building permit. It let each city and county decide, and where yours has said nothing there is no permit, no plan review and no certificate of occupancy. What it did not leave to the county: three trade permits, and a power supplier that may not set your meter until a state inspector has passed the wiring.',
  pageCount: 43,
  revision: 'September 2026',

  heroSheets: {
    front: {
      src: '/kits/id/idk-hero-front.webp',
      alt: 'Idaho Owner-Builder Permit Kit page quoting the two clauses of Idaho Code section 39-4111, which require a building permit only for buildings under the state division or in a local jurisdiction enforcing building codes, followed by the DOPL form stating that DOPL does not issue building permits for projects not owned by the State',
    },
    back: {
      src: '/kits/id/idk-hero-back.webp',
      alt: 'Kit page quoting Idaho Code section 54-1005, which forbids any power supplier including cooperatives from energizing an installation until a state inspection has passed, above the rule that lets a utility energize temporary construction power only at the request of a licensed electrical contractor',
    },
  },

  documents: [
    {
      no: 'ID.0',
      pages: '3 pages',
      title: 'Cover & How to Use',
      copy: 'A job-site cover with two lines Idaho makes you answer separately — where the building permit comes from, which may honestly read NONE, and where the trade permits come from, which never does — plus a line for your public health district number. And the one-page orientation.',
    },
    {
      no: 'ID.1',
      pages: '11 pages',
      title: 'The Building Permit Is Optional, the Trade Permits Are Not',
      copy: 'The two-clause statute that puts a private house under a permit only where a local government has adopted an ordinance, and the DOPL form that says the state issues none. The five permits that survive that gap. The utility that may not energize until an inspection passes, and the temporary-power rule written for contractors only. Then the three owner exemptions, quoted at the words that decide arguments — because they are three different tests, and none of them says “not for sale, rent or lease.”',
      thumb: '/kits/id/idk-exemptions.webp',
      caption: 'ID.1 Three exemptions, three different tests',
      alt: 'Page 6 of ID.1: a three-row table quoting the contractor-registration exemption, which applies whether or not the owner occupies the house; the electrical licensing exemption, limited to a primary or secondary residence; and the plumbing and HVAC exemptions, which reach any owner or contract purchaser of a single or duplex family dwelling — followed by a box locating the “will personally perform” and “not rented by a tenant” conditions on the DOPL permit form rather than in any statute',
    },
    {
      no: 'ID.2',
      pages: '11 pages',
      title: 'Permit Application Checklist',
      copy: 'The code editions actually in force and the House committee minutes that rejected the 2024 update. The 2023 NEC as Idaho amended it downward — AFCI on bedroom circuits only, most of the new GFCI deleted, surge protection and the emergency disconnect made optional. The energy table Idaho wrote itself, pinned by statute so no county may add to it, with a visual inspection in place of a blower door. The trade fees as the rules set them, with a worked example. The septic and well packages in order.',
      thumb: '/kits/id/idk-nec.webp',
      caption: 'ID.2 The 2023 NEC, amended downward',
      alt: 'Page 3 of ID.2: a table of Idaho amendments to the 2023 National Electrical Code — arc-fault protection limited to bedrooms, the 250-volt, laundry, food-preparation and appliance GFCI items deleted, surge protection and the emergency disconnect made permissive, and island receptacles optional — with the rule citation and the practical effect of each',
    },
    {
      no: 'ID.3',
      pages: '7 pages',
      title: 'Inspection Sequence & Clocks',
      copy: 'The first decision, before the footings: three ways to get power on site when your homeowner permit cannot unlock the meter. Then the clocks — ten business days to tell you an application is incomplete, and the 48-business-hour inspection rule with its self-help remedy on all four tracks. The trade inspection ladders as the rules fix them, the building inspections as your ordinance adopted them, and a log with the column the clock runs from.',
      thumb: '/kits/id/idk-clocks.webp',
      caption: 'ID.3 The 48-business-hour rule',
      alt: 'Page 3 of ID.3: a boxed quotation of the Idaho statute authorizing a permit holder to hire a third-party inspector and be refunded the inspection fee when a requested inspection is not performed within 48 business hours, noting the identical text in the building, electrical, plumbing and HVAC chapters and their effective dates',
    },
    {
      no: 'ID.4',
      pages: '6 pages',
      title: 'Where to File Directory',
      copy: 'Idaho publishes no list of which counties enforce a building code, so this is the method the statute itself created, plus the offices that exist regardless: DOPL and its inspector schedule, the seven public health districts fixed county by county in statute, and IDWR for the well. Boise and Coeur d’Alene as worked examples of cities that run their own trade programs.',
    },
    {
      no: 'ID.5',
      pages: '5 pages',
      title: 'Forms & Documents Index',
      copy: 'Every document you will meet, named as the agency names it — the three DOPL homeowner permit applications and the certification printed on each, the septic installation permit and its as-built, the IDWR drilling permit — plus what needs no permit, what Idaho does not require, and the one thing you may not do yourself.',
    },
  ],

  includes: [
    '43 print-ready pages across 6 documents, letter size',
    'Every Idaho claim cited on the page it appears on',
    'Write-in lines for everything the county or the health district sets',
    'A permit record, an inspection log with a request-date column, and a confirmed-offices page for the job site',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things Idaho law actually says that the standard advice gets wrong. Each takes about a minute to check.',

  highlights: [
    {
      icon: 'doc',
      label: 'The state is not your building department',
      copy: 'Idaho Code § 39-4111 makes it unlawful to build without a permit in exactly two places: a building “coming under the purview of the division” and a building “in a local government jurisdiction enforcing building codes.” A private house in a county that has adopted no ordinance is in neither. DOPL’s own Plan Review Application says the rest: “DOPL does NOT issue building permits for projects not owned by the State. Contact the local government for these projects.” Where nobody has adopted a code there is no residential permit, plan review, inspection or certificate of occupancy — and no state office that will sell you one.',
    },
    {
      icon: 'bolt',
      label: 'The trade permits apply anyway, and the meter enforces them',
      copy: 'Three chapters of Title 54 never read the Building Code Act. Electrical (§ 54-1005), plumbing (§ 54-2620) and HVAC (§ 54-5016) permits are required statewide, from DOPL unless a city or county runs its own program, and a homeowner doing his own work buys them too. The electrical one is enforced at the meter: a power supplier, “cooperatives” named, “shall not connect with or energize any electrical installation … unless an inspection has been conducted and resulted as ‘passed.’” The one exception — temporary construction power before inspection — exists only “at the request of a licensed electrical contractor” (IDAPA 24.39.10.200.04). A homeowner permit does not open that door.',
    },
    {
      icon: 'check',
      label: 'Three exemptions, three tests, and no “sale or lease” rule',
      copy: 'The contractor-registration exemption covers an owner building on “personal residential real property, whether or not occupied by the owner” (§ 54-5205(2)(l)). The electrical exemption is from licensing only, for “noncommercial electrical work in the owner’s primary or secondary residence” (§ 54-1016(2)(a)); the permit and the passed inspection still apply. The plumbing and HVAC exemptions reach any person who “owns or is a contract purchaser” of a single or duplex family dwelling, with no residence test at all (§ 54-2602(1)(a); § 54-5002(1)(a)). “Not for sale, rent or lease” appears in none of them. What the DOPL form actually says is “will personally perform the work” and “not used for commercial purposes or rented by a tenant.”',
    },
    {
      icon: 'permit',
      label: 'Forty-eight business hours, then you may hire your own inspector',
      copy: 'Since 2025 and 2026 the same sentence sits in four statutes — § 39-4118 for building, §§ 54-1004A, 54-2626A and 54-5020A for the trades: if a requested inspection “is not performed within forty-eight (48) business hours,” the permit holder “shall be authorized to hire a third-party inspector” and “shall be refunded any fee” paid for that inspection. A failed inspection with no reason given within three business days earns a 10% refund. And a local government that requires building permits owes you a published process document and written notice within ten business days if your residential application is incomplete (§ 39-4117). Most states give you none of this. Idaho gives you all of it — but only if you log the date and time of every request.',
    },
  ],

  sourceNote:
    'Every claim was read against its primary source in September 2026: the Idaho Code on the Legislature’s own site, one section per page; the IDAPA rule chapters at adminrules.idaho.gov, each paragraph dated; DOPL’s own homeowner permit applications, Plan Review Application and program pages; the DEQ septic and IDWR well pages; and the House Business Committee’s minutes of 17 February 2026, which record the rejection of the 2024 code update.',

  faqs: [
    {
      question: 'Can you build your own house in Idaho without a contractor license?',
      answer:
        'Yes. Idaho registers contractors rather than licensing them — no examination, no experience test — and the Idaho Contractor Registration Act exempts “an owner performing construction on the owner’s personal residential real property, whether or not occupied by the owner” (Idaho Code § 54-5205(2)(l)). There is no occupancy requirement and no form to file with the state; where a building permit is issued, it must carry the phrase “no contractor registration provided” on its face and be posted at the site (§ 54-5209), and the issuing office “shall [not] be required to verify” your exemption. The anti-flip proviso in that subsection reaches only an owner “who is otherwise regulated by this chapter” — someone already in the contracting business — building for the purpose of promptly selling. What the exemption does not touch: the electrical, plumbing and HVAC permits, which you buy from DOPL on homeowner applications, and the inspections that come with them.',
    },
    {
      question: 'Do you need a building permit to build a house in Idaho?',
      answer:
        'Only if your city or county has adopted a building-code ordinance. Idaho Code § 39-4103(1) says the Building Code Act “authorizes” the state division and local governments to adopt and enforce building codes; it does not impose one. The permit section, § 39-4111, makes it unlawful to build without a permit for buildings “coming under the purview of the division” — state-owned buildings, schools, modular units — and for buildings “in a local government jurisdiction enforcing building codes.” A private house in a county with no ordinance is in neither clause. There is no state fallback: DOPL’s own Plan Review Application states that “DOPL does NOT issue building permits for projects not owned by the State.” Since 1 July 2025, any local government that requires building permits must publish “a document that describes in detail the requirements of its building permit process” on its website (§ 39-4117(1)) — the fastest way to tell whether yours is enforcing. Check the city first if you are inside city limits; a city’s ordinance and its county’s routinely differ.',
    },
    {
      question: 'Can a homeowner do their own electrical work in Idaho?',
      answer:
        'Yes, on a DOPL homeowner electrical permit — but read the exemption carefully, because it is narrower than the plumbing and HVAC ones and it is a licensing exemption only. Idaho Code § 54-1016(2)(a) provides that “the licensing provisions of this chapter shall not apply to … any property owner performing noncommercial electrical work in the owner’s primary or secondary residence or associated outbuildings.” The permit duty and the inspection are untouched. And by § 54-1005(3) your power supplier, rural cooperatives included, “shall not connect with or energize any electrical installation … unless an inspection has been conducted and resulted as ‘passed.’” The rule that lets a utility energize temporary construction power before inspection, IDAPA 24.39.10.200.04, works only “at the request of a licensed electrical contractor,” so an owner-builder on a homeowner permit decides before the footings whether a contractor pulls the temporary-service permit, the owner’s own service is inspected before the meter is set, or the job runs on a generator. Grid-tied solar needs a local preplan review before the permit. The permit itself is priced on living space — $130 up to 1,500 square feet, rising to $325 at 4,500 — and expires 365 days from purchase.',
    },
    {
      question: 'Which building code does Idaho use in 2026?',
      answer:
        'The 2018 International Residential Code, Parts I, II, III and IX, with Idaho amendments (IDAPA 24.39.30.600.03) — sold by ICC as the “2020 Idaho Residential Code” on the same 2018 base. Energy is the 2018 IECC, fixed in statute by Idaho Code § 39-9701 with Idaho’s own insulation table. Electrical is the 2023 NEC, adopted by the Legislature in § 54-1001 effective 1 July 2023 and amended downward by the Electrical Board. Plumbing is the 2015 Uniform Plumbing Code as the Idaho State Plumbing Code; mechanical is the 2018 IMC and IFGC. Residential fire sprinklers are exempted by statute (§ 39-4116(3)). The 2024 I-Codes were proposed in Docket 24-3930-2502, and on 17 February 2026 the House Business Committee voted to reject the docket, with one member “noting the need to create an Idaho Building Code.” DOPL’s statutes-and-rules page now reads “These boards are not currently engaged in rulemaking for 2026–2027,” so the 2018 editions remain in force with no successor scheduled. Ground snow load, frost depth and seismic category are not statewide numbers at all: IRC Section R301 design criteria are the county’s to amend (§ 39-4116(4)(c)(iii)).',
    },
    {
      question: 'What does the Idaho energy code require, and can my county add to it?',
      answer:
        'Idaho Code § 39-9701 makes the 2018 IECC, as amended by the Building Code Board, the state energy code and then preempts every local government from adopting any energy requirement “that differ[s] from or [is] more extensive than” it — so “verify locally” is the wrong instruction here. Idaho deleted the model code’s Climate Zone 5 and 6 rows and wrote its own (IDAPA 24.39.30.600.06): Zone 5 ceiling R-38, wood-frame wall R-20 or 13+5, floor R-30, fenestration U-0.32; Zone 6 ceiling R-49, wall R-22 or 13+5, U-0.30. Every Idaho county is Zone 5 or 6. A blower-door test is not required: Idaho adds a “Visual Inspection” exception under which “the Permit Holder will determine at the time of permit application the method of determining building envelope tightness,” and a visual inspection against the code’s checklist is acceptable in place of testing. The one thing Idaho requires that the model code makes conditional: R303.4 as replaced makes whole-house mechanical ventilation mandatory in every new dwelling.',
    },
    {
      question: 'Can I install my own septic system or drill my own well in Idaho?',
      answer:
        'Septic yes, well no. Septic systems are permitted by Idaho’s seven public health districts under DEQ’s rules, and no one may install a system “unless there is a valid installation permit” (IDAPA 58.01.03.005.01). The installer registration is separately excused for “owners installing their own standard or basic alternative system” (IDAPA 58.01.03.006.08.b); complex systems need a registered complex installer, and no system may receive wastewater until the district’s final inspection and as-built drawing (011.05). The site must hold two complete drainfields, the slope may not exceed 20%, and a drainfield sits at least 100 feet from a well. Wells are different. Idaho Code § 42-238(2) makes it unlawful “for any person to drill a well in Idaho … without first complying with the provisions of this chapter,” and subsection (3) defines “person” as “any individual who drills or abandons any well for himself or another.” The chapter then requires a driller’s license, an examination and a bond. Before drilling, the owner or driller obtains a $75 IDWR drilling permit (§ 42-235); a domestic well of up to 13,000 gallons a day needs no water right, except inside certain new subdivisions in moratorium or critical ground water areas (§ 42-227(4)).',
    },
  ],

  productDescription:
    'A 43-page print-ready permit kit for building your own home in Idaho, in six documents. Covers the question that decides an Idaho build — whether your city or county has adopted a building code at all — and the fact that DOPL issues no building permit for a house, so where nobody has adopted a code there is no permit, plan review or certificate of occupancy. Also the three state trade permits that apply everywhere regardless, the utility that may not energize until a state inspection passes, the temporary-power rule written only for licensed contractors, the three owner exemptions and their three different tests, the 2023 NEC as Idaho amended it downward, the energy table Idaho wrote and pinned by statute, the 2024 code update rejected in committee in February 2026, the ten-business-day completeness clock and the 48-business-hour inspection rule with its self-help remedy, the DOPL fee ladders, the health-district septic package with its separation distances, and the IDWR well permit. Every claim is cited on the page it appears on and was verified against the Idaho Code, the IDAPA rules and DOPL’s own forms and pages in September 2026.',

  verifyNote:
    'Statutes, rules and code editions change, and two Idaho answers are moving right now: the Building Code Board has no rulemaking scheduled for 2026–2027 after the 2024 update was rejected, but a bill creating a standalone Idaho building code has been called for in committee; and the Electrical Board holds a public hearing on its NEC amendments in October 2026. Trade programs also transfer between DOPL and cities in both directions. Confirm each rule with the office that will handle your parcel, which for the trades is DOPL unless its map says otherwise. The kit prints its sources so you can.',

  binderLead:
    'The Owner-Builder Job Site Binder picks up where the permit kit stops — and in Idaho, where a county with no building department will never issue a certificate of occupancy and the only record of the house may be the inspection tags you kept, your own paperwork matters more than usual. 367 pages of contracts, inspection forms, daily logs and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function IDPermitKit() {
  return <KitProductPage content={ID} />;
}
