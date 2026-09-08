import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/ny-permit-kit' },
  title: 'New York Owner-Builder Permit Kit — $34',
  description:
    'New York permit kit: which of three governments issues your permit, the workers’ compensation form that gates it, the electrical inspector your town must pre-approve, New York’s own energy values, and the court-set all-electric date. 45 print-ready pages, every claim cited. $34 instant download.',
  keywords:
    'New York owner builder permit, NYS Uniform Code, 19 NYCRR Part 1203, CE-200 building permit, General Municipal Law 125, New York building permit workers compensation, all electric buildings act suspended, New York stamped plans 1500 square feet, 2025 Residential Code of New York State',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const NY: KitContent = {
  slug: 'ny-permit-kit',
  heroSub:
    'New York has one code for every parcel outside New York City and three governments that might issue your permit. What gates it is not a license — it is a workers’ compensation form — and the gas question has a court-set date.',
  pageCount: 45,
  revision: 'September 2026',

  heroSheets: {
    front: {
      src: '/kits/ny/nyk-hero-front.webp',
      alt: 'New York Owner-Builder Permit Kit page quoting General Municipal Law § 125 in full — no city, town or village may issue a building permit without carrier proof of workers’ compensation coverage or an affidavit of no employees — above a table of the two doors and the Workers’ Compensation Board’s forms for each',
    },
    back: {
      src: '/kits/ny/nyk-hero-back.webp',
      alt: 'Kit page headed The All-Electric Provision, a dated status box setting out the application-date trigger, the 18 November 2025 stipulation suspending the rule, and the clock running from the Second Circuit mandate of 2 September 2026 to 31 December 2026',
    },
  },

  documents: [
    {
      no: 'NY.0',
      pages: '3 pages',
      title: 'Cover & How to Use',
      copy: 'A job-site cover with the field New York actually makes you resolve first — which of three governments issues your permit — and a one-line statement of the New York City carve-out. Plus the two-page orientation.',
    },
    {
      no: 'NY.1',
      pages: '9 pages',
      title: 'Who Enforces Your House',
      copy: 'New York has no owner-builder exemption because it has no contractor license to be exempt from. So this walks what actually decides your build: the statutory ladder from town to county to the Department of State, the workers’ compensation form no other guide prints, the 2025 code editions, and a dated status box on the all-electric rule with a check-before-you-file instruction.',
      thumb: '/kits/ny/nyk-ladder.webp',
      caption: 'NY.1 The three rungs of Executive Law § 381(2)',
      alt: 'Page 2 of NY.1: Executive Law § 381(2) quoted in a box, followed by a numbered table of the three permit offices — the town, village or city; the county; and the Department of State — with what each means for the applicant',
    },
    {
      no: 'NY.2',
      pages: '11 pages',
      title: 'Permit Application Checklist',
      copy: 'What the state rule entitles the reviewer to demand, the 1,500 square foot line above which plans must be stamped, the frost, snow and wind numbers your office writes into Table R301.2 itself, New York’s own energy values — R-49, U-0.27, and a blower-door limit that tightens in Zone 6 — the septic and well distances that fix where the house can sit, and the contract terms that attach by statute when you hire a builder for a custom home.',
      thumb: '/kits/ny/nyk-energy.webp',
      caption: 'NY.2 New York’s own energy table',
      alt: 'Page 6 of NY.2: New York’s Table R402.1.3 giving minimum insulation values identical in Zones 4, 5 and 6 — ceiling R-49, wood-frame wall R-30 or 20&5ci, window U-factor 0.27 — above a boxed quotation of the air-leakage rule, 3.0 air changes per hour in Zones 4 and 5 and 2.5 in Zone 6',
    },
    {
      no: 'NY.3',
      pages: '9 pages',
      title: 'Inspection Sequence',
      copy: 'The eleven inspection elements the state rule requires of every program, the electrical inspection your office may accept only from an agency it has approved, the written blower-door report the certificate of occupancy waits on, the 30-day order-to-remedy clock, and the appeal you do have — to a regional board of review that must decide in 60 days.',
      thumb: '/kits/ny/nyk-appeal.webp',
      caption: 'NY.3 The appeal you have',
      alt: 'Page 5 of NY.3: the penalty row of the enforcement table — a fine of not more than one thousand dollars per day of violation, naming any owner or builder — followed by the section on appeals, quoting [NY] R112.1 and 19 NYCRR § 1205.3(a)(2) on the regional board of review and its 60-day decision',
    },
    {
      no: 'NY.4',
      pages: '8 pages',
      title: 'Where to File Directory',
      copy: 'New York publishes no list of which government permits which parcel, so this is a method — one question to one clerk, in the statutory order — plus the county health department that approves septic and wells, the Adirondack Park and New York City watershed overlays, the five county home-improvement laws and which of them reach a new house, and the offices that exist whatever your rung.',
    },
    {
      no: 'NY.5',
      pages: '5 pages',
      title: 'Forms & Documents Index',
      copy: 'Every document you will meet, named as the agency names it — the CE-200, the carrier forms, the statement of special inspections, the agency certificates, the well completion report — plus what may need no permit if your office says so, what New York never asks for, and the two things you may not do yourself.',
    },
  ],

  includes: [
    '45 print-ready pages across 6 documents, letter size',
    'Every New York claim cited on the page it appears on',
    'Write-in lines for everything that varies by municipality',
    'A permit record, an inspection log and a confirmed-offices page for the job site',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things New York law actually says that the standard advice gets wrong. Each takes about a minute to check.',

  highlights: [
    {
      icon: 'doc',
      label: 'Your permit is gated by a workers’ compensation form',
      copy: 'General Municipal Law § 125 is one sentence: no city, town or village may issue a building permit without either carrier proof of workers’ compensation and disability coverage in a form satisfactory to the Workers’ Compensation Board, or “an affidavit that such permit applicant has not engaged an employer or any employees.” The Board’s forms are C-105.2 and DB-120.1 from your carrier — “ACORD forms are not acceptable” — or Form CE-200, the Certificate of Attestation of Exemption, applied for at New York Business Express under “Apply as a Homeowner.” It is job-specific: “a separate certificate will be required for each building permit.” No New York owner-builder guide prints this.',
    },
    {
      icon: 'bolt',
      label: 'The electrical inspector is whoever your town has approved',
      copy: '19 NYCRR § 1203.2(e)(4) classes electrical inspections as special inspections, and says an authority having jurisdiction “shall not accept or rely upon a special inspection unless the person performing such special inspection (i) is a qualified person employed or retained by an agency that has been approved by the authority having jurisdiction.” There is no state list. Most building departments employ no electrical inspector and accept certificates only from third-party agencies they have approved — and the certificate of occupancy waits on that agency’s “final report of special inspections” (§ 1203.3(d)(2)(ii)). The edition, by contrast, does not vary: the 2025 Residential Code’s Electrical Part “is based on the 2023 National Electrical Code.” And [NY] E3401.2.1 says an owner-occupied one-family dwelling need not have electrical service at all.',
    },
    {
      icon: 'check',
      label: 'The energy values are New York’s, not the model code’s',
      copy: 'Guides that copy the 2024 IECC print R-60 ceilings and U-0.30 windows. New York’s own Table R402.1.3 says R-49 in all three zones and U-0.27, and the air-leakage limit in [NY] R402.5.1.3 is 3.0 air changes per hour in Climate Zones 4 and 5 but 2.5 in Zone 6 — and Zone 6 includes Ulster, Sullivan and Delaware counties, not just the North Country. The blower door is mandatory, the written report goes to the building official, and § 1203.3(d)(2)(iv) makes it a certificate-of-occupancy precondition. Stamped plans, meanwhile, are a state rule, not a local one: above 1,500 square feet gross, by Education Law §§ 7307(5) and 7209(7)(b).',
    },
    {
      icon: 'permit',
      label: 'The all-electric date is 31 December 2026, not 28 October',
      copy: 'Executive Law § 378(19) and 19 NYCRR Subpart 1229-2 prohibit fossil-fuel equipment in new buildings for which a “substantially complete building permit application” is submitted on or after the effective date. A Stipulation and Order in Mulhern Gas Co. v. Mosley (18 November 2025) suspended the rule until 120 days after the Second Circuit’s mandate. The court affirmed on 30 June 2026, denied rehearing on 26 August 2026, and the mandate issued on 2 September 2026 — so the suspension ends 31 December 2026 unless a certiorari petition, due about 24 November 2026, extends it. The widely reported 28 October date counts from the decision; the stipulation counts from the mandate. The kit prints the box with the date it was checked and tells you to read the docket before you file.',
    },
  ],

  sourceNote:
    'Every claim was read against its primary source in September 2026: the Executive Law, General Municipal Law, Workers’ Compensation Law, Education Law and General Business Law at nysenate.gov; the Department of State’s own rule-text PDFs for 19 NYCRR Parts 1202, 1203, 1205, 1219–1229 and 1240; the 2025 Residential and Energy Codes of New York State in the ICC’s free viewer; the Health Department’s Appendices 75-A and 5-B; the Workers’ Compensation Board’s forms guidance; and the federal court docket in Mulhern Gas Co. v. Mosley — not the trade press that reported the wrong date.',

  faqs: [
    {
      question: 'Can you build your own house in New York without a license?',
      answer:
        'Yes, and there is nothing to apply for. New York issues no general contractor, electrician or plumber license at state level — the Department of State’s Division of Building Standards and Codes says on its own FAQ that “issues regarding local laws, zoning, and licensing of contractors or electricians are not handled by this Division,” and Executive Law Article 18 contains no licensing provision. That is why New York has no owner-builder exemption: there is nothing to be exempt from. Whether you may do your own wiring or plumbing is a local licensing question decided by your municipality under Executive Law § 379(3), and there is no statewide registry to search. What the state does gate is the permit itself, under General Municipal Law § 125 — carrier proof of workers’ compensation coverage or an affidavit of no employees, which for an owner-builder is Form CE-200 filed as a homeowner. This is New York State outside New York City; the five boroughs keep their own code under Executive Law § 383(1)(c).',
    },
    {
      question: 'Which office issues a building permit in New York State?',
      answer:
        'One of three, and the statute fixes the order. Executive Law § 381(2) provides that “every local government shall administer and enforce” the Uniform Code — a village, a town outside any village, or a city (§ 372(11)) — unless it enacted a local law before 1 July declining to enforce, in which case “the county … shall administer and enforce,” and if the county also declined, “the secretary in the place and stead of the local government” — the Department of State, under 19 NYCRR Part 1202. The code itself never lapses on any rung (§§ 371(2)(c), 383(1)); what changes is the office, the fee, the local law and the inspector. No list of which rung applies where is published, so the kit gives you the question to ask your clerk, in the statutory order, and a page to record the answer.',
    },
    {
      question: 'What is Form CE-200 and do I need it for a building permit?',
      answer:
        'Form CE-200 is the Workers’ Compensation Board’s Certificate of Attestation of Exemption, and it is the affidavit General Municipal Law § 125 lets you file instead of carrier proof of coverage — the sworn statement that you have “not engaged an employer or any employees” to do the permitted work. You apply through New York Business Express with a NY.gov Business account; the Board’s instruction sheet says to select “Apply as a Homeowner (applies to those obtaining permits to work on their residence).” Two rules bite. “Certificates for building permits are job-specific and a separate certificate will be required for each building permit,” so the house’s CE-200 does not cover a later permit for the garage. And the alternative door — Forms C-105.2 and DB-120.1 — must come from your carrier: “ACORD forms are not acceptable.” Whether paying day labor by the hour makes you an “employer” under Workers’ Compensation Law § 2 is a legal question the form does not answer; the kit says so and sends you to the Board or a lawyer.',
    },
    {
      question: 'Which building code does New York use in 2026?',
      answer:
        'The 2025 Uniform Code and 2025 Energy Code, adopted 5 December 2025 and effective 31 December 2025 (19 NYCRR Parts 1219–1229 and 1240). The eight code books are the 2025 editions “published by the International Code Council,” which the Department of State describes as based on the 2024 I-Codes with New York modifications; the option to build to the 2020 edition closed on the effective date, and no grandfathering rule for applications already in review was found. Two things to know. The code is the regulation plus the book, and the official NYCRR compilation on Westlaw was still showing the 2020 Residential Code nine months after the 2025 rule took effect — read the Department of State’s own rule-text PDFs instead. And the Electrical Part is fixed statewide: Chapters 34 through 43 of the 2025 Residential Code are “based on the 2023 National Electrical Code,” so the edition does not vary by town, whatever a local guide says.',
    },
    {
      question: 'Does New York require stamped plans for a house?',
      answer:
        'Above 1,500 square feet gross, yes, statewide. Education Law § 7307(5) says the architecture article does not apply to “residence buildings of gross area of fifteen hundred square feet or less, not including garages, carports, porches, cellars, or uninhabitable basements or attics,” and § 7209(7)(b) carries the same exclusion for engineering; above that line, § 7307(1) and § 7209(1) forbid any state, county, city, town or village official to “accept or approve any plans or specifications that are not stamped” by a New York-licensed architect or engineer. At or under 1,500 square feet the state does not require a stamp, but the 2025 Residential Code’s [NY] R106.6 hands the question to “the stricter of” your office’s code enforcement program, so ask. And any site with a ground snow load above 70 psf must be “designed in accordance with accepted engineering practice” under [NY] R301.2.3 — a code threshold, not a county policy — with 2 psf added to the mapped value for every 100 feet of elevation above 1,000 feet.',
    },
    {
      question: 'Is New York’s ban on gas in new homes in effect?',
      answer:
        'Not on the day this kit was compiled, and the date it could take effect is 31 December 2026 — not 28 October. Executive Law § 378(19) and 19 NYCRR Subpart 1229-2 reach new buildings for which a “substantially complete building permit application” is submitted on or after the effective date, which is the trigger that matters: a complete application in before the suspension lifts is outside the prohibition whenever the house is built. The rule is suspended by a Stipulation and Order in Mulhern Gas Co. v. Mosley signed 18 November 2025, which ends “120 days after the issuance of the mandate of the Second Circuit” if no certiorari petition is filed. The Second Circuit affirmed on 30 June 2026, denied rehearing en banc on 26 August 2026, and issued its mandate on 2 September 2026. A certiorari petition is due about 24 November 2026; if one is filed, the suspension runs to 120 days after its denial or after a Supreme Court judgment. Nothing in Subpart 1229-2 exempts a single-family house, a wood stove, a propane range or a generator used for anything but emergency or standby power. Read the Department of State’s Notice of Adoption page and the docket before you file.',
    },
  ],

  productDescription:
    'A 45-page print-ready permit kit for building your own home in New York State outside New York City, in six documents. Covers the question that decides a New York build — which of three governments issues your permit under Executive Law § 381(2) — and the permit gate no other guide prints, General Municipal Law § 125 and the job-specific Form CE-200. Also the electrical inspection your office may accept only from an agency it has approved (19 NYCRR § 1203.2(e)(4)), the 1,500 square foot stamped-plan rule, the frost, snow and wind numbers your office writes into Table R301.2, New York’s own energy values and the zone-dependent blower-door limit, the eleven inspection elements of § 1203.3(b)(1), the 30-day order to remedy and the $1,000-a-day penalty naming “any owner, builder,” the Part 1205 appeal decided in 60 days, the Appendix 75-A septic and Appendix 5-B well distances, the Adirondack Park and New York City watershed overlays, the five county home-improvement laws, and a dated status box on the all-electric rule with its court-set clock. Every claim is cited on the page it appears on and was verified against the statutes, the Department of State’s rule texts, the 2025 codes and the federal docket in September 2026.',

  verifyNote:
    'Statutes, regulations and code editions change, and one New York answer is moving right now: the all-electric suspension ends 31 December 2026 unless a certiorari petition due about 24 November 2026 extends it, and the Department of State updates its Notice of Adoption page when the status changes. Confirm each rule with the office that will handle your parcel — which may be your town, your county or the Department of State — and read the status box’s sources the week you file. The kit prints them so you can.',

  binderLead:
    'The Owner-Builder Job Site Binder picks up where the permit kit stops — and in New York, where the electrical certificate and the blower-door report come from people you hired and the certificate of occupancy waits on both, your own paperwork is the file the office reads from. 367 pages of contracts, inspection forms, daily logs and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function NYPermitKit() {
  return <KitProductPage content={NY} />;
}
