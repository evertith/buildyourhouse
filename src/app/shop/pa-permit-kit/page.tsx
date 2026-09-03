import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/pa-permit-kit' },
  title: 'Pennsylvania Owner-Builder Permit Kit — $34',
  description:
    'Pennsylvania permit kit: who inspects your house in an opt-out municipality, the five inspections the statute requires, the appeal you do not have, wall bracing frozen at the 2006 IRC, and the energy table Pennsylvania rewrote. 40 print-ready pages, every claim cited. $34 instant download.',
  keywords:
    'Pennsylvania owner builder permit, PA Uniform Construction Code, UCC opt-out municipality, third party agency Pennsylvania, 34 Pa. Code 403.103, PA building permit inspections, HICPA new home, Pennsylvania building code 2021 IRC',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const PA: KitContent = {
  slug: 'pa-permit-kit',
  heroSub:
    'Pennsylvania does not ask whether the code applies to your house. It applies everywhere. The question is who is going to inspect it — and in 119 municipalities the answer is nobody, until you go and hire them.',
  pageCount: 40,
  revision: 'September 2026',

  heroSheets: {
    front: {
      src: '/kits/pa/pak-hero-front.webp',
      alt: 'Pennsylvania Owner-Builder Permit Kit page quoting the statute that lists the five inspections required on every one- and two-family dwelling, above a table explaining what each one covers',
    },
    back: {
      src: '/kits/pa/pak-hero-back.webp',
      alt: 'Kit page describing the Labor and Industry table of every Pennsylvania municipality, noting that 2,444 had opted in and 119 had opted out, and that the building code official column is blank on an opt-out row',
    },
  },

  documents: [
    {
      no: 'PA.0',
      pages: '3 pages',
      title: 'Cover & How to Use',
      copy: 'A job-site cover with the fields Pennsylvania actually makes you resolve — including a line for whoever is doing your plan review and inspections, because in a large number of municipalities that is a private company you have not hired yet. Plus the one-page orientation.',
    },
    {
      no: 'PA.1',
      pages: '8 pages',
      title: 'Who Inspects Your House',
      copy: 'Pennsylvania has no owner-builder exemption because it has no contractor license to be exempt from. So this walks the question that actually decides your build: the six ways a municipality can handle the code, what to do when it has chosen none of them, and the exclusions that are genuinely outside the code — including the recreational cabin, which has a seven-part test.',
      thumb: '/kits/pa/pak-enforcement.webp',
      caption: 'PA.1 The six ways a municipality handles the code',
      alt: 'Page 3 of PA.1: a numbered table of the six enforcement arrangements, from a municipality using its own employee through to one that elected not to administer the code at all, with a note that an agreement with Labor and Industry is available only for buildings other than one- and two-family dwellings',
    },
    {
      no: 'PA.2',
      pages: '9 pages',
      title: 'Permit Application Checklist',
      copy: 'What the regulation entitles the reviewer to demand, the fifteen-business-day clock and how a design professional’s certification cuts it to five, and the Pennsylvania amendments that make the code book on your desk wrong — wall bracing rolled back to 2006, a gypsum membrane under most engineered floors, and an energy table the Commonwealth rewrote rather than adopted.',
      thumb: '/kits/pa/pak-energy.webp',
      caption: 'PA.2 The energy table Pennsylvania wrote itself',
      alt: 'Page 5 of PA.2: Pennsylvania’s replacement Table R402.1.3 giving minimum insulation by climate zone — ceiling R-49 in all three zones, wood frame wall R-20 in zone 4 rising to R-23 in zone 5, and a blower door limit of 3.0 ACH50 across the whole Commonwealth — above a table of the ways Pennsylvania law differs from the printed 2021 IRC',
    },
    {
      no: 'PA.3',
      pages: '7 pages',
      title: 'Inspection Sequence',
      copy: 'The five inspections the statute names, in order, with the rule that the final one cannot pass until the other four have. The certificate of occupancy and its five-business-day clock. And the appeal you do not have if your municipality opted out — which is the other half of a bargain nobody explains.',
      thumb: '/kits/pa/pak-appeals.webp',
      caption: 'PA.3 The appeal you do not have',
      alt: 'Page 4 of PA.3: a boxed explanation chaining three provisions to show that no board of appeals exists in an opt-out municipality, that the right to appeal is expressly limited to municipalities which adopted an ordinance, and that the Industrial Board hears only Department decisions — concluding that you choose your inspector and give up the statutory right to appeal him',
    },
    {
      no: 'PA.4',
      pages: '7 pages',
      title: 'Where to File Directory',
      copy: 'Pennsylvania has roughly 2,560 municipalities and no central permit portal, so this is built around the one authoritative lookup that answers the central question for any parcel in the state — plus the offices that are not the building department, which is where the time actually goes.',
    },
    {
      no: 'PA.5',
      pages: '6 pages',
      title: 'Forms & Documents Index',
      copy: 'Every document you will meet, named as the office names it. Including the group that catches owner-builders: the paper nobody will ever ask you for, which exists only because acting as your own contractor removed the person who used to produce it.',
    },
  ],

  includes: [
    '40 print-ready pages across 6 documents, letter size',
    'Every Pennsylvania claim cited on the page it appears on',
    'Write-in lines for everything that varies by municipality',
    'A permit record, an inspection log and a confirmed-offices page for the job site',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things Pennsylvania law actually says that the standard advice gets wrong. Each takes about a minute to check.',

  highlights: [
    {
      icon: 'doc',
      label: 'Opting out moves the duty onto you',
      copy: 'The Uniform Construction Code applies to “all buildings in this Commonwealth” (35 P.S. § 7210.104(a)) and five inspections are required on every house. Where a municipality elected not to administer the code, 34 Pa. Code § 403.103(b) is explicit: “An applicant for a residential building permit shall obtain the services of a third-party agency certified in the appropriate categories.” Labor and Industry is not your fallback — § 403.103(g) gives the Department only non-residential work there. As of September 2026 L&I’s own table shows 119 of 2,563 municipalities in that position.',
    },
    {
      icon: 'check',
      label: 'Five inspections, not thirteen',
      copy: 'Published Pennsylvania advice prints a ten- to thirteen-item inspection list borrowed from a municipal handout. The statute names five: foundation; plumbing, mechanical and electrical; frame and masonry; wallboard; final — 35 P.S. § 7210.501(e)(1), repeated at 34 Pa. Code § 403.64(d) and (f). The same sentence adds the rule that matters: “The final inspection shall not be deemed approved until all previous inspections have been successfully completed and passed.” Your official may run more under § 403.64(e), but five is the floor — and in an opt-out municipality you are buying that list under contract, so its length is a price term.',
    },
    {
      icon: 'bolt',
      label: 'Your code book is wrong in four places',
      copy: 'Pennsylvania amends the model codes in two places, and one of them is the Act itself, where nobody looks. Wall bracing is excluded from the 2009 IRC “and any successor provisions” and enforced from the 2006 IRC instead (35 P.S. § 7210.304(i)). Most non-rated floor assemblies need a half-inch gypsum membrane underneath (§ 7210.304(h)). Three electrical sections — island countertops, tub and shower space, foyers — are struck from the 2021 IRC and replaced with 2018 and 2015 text. And appendices are not adopted at all (34 Pa. Code § 403.21(c)), so there is no radon requirement anywhere in the state.',
    },
    {
      icon: 'permit',
      label: 'Opt out and you lose the right to appeal',
      copy: 'This is the half of the bargain nobody mentions. A board of appeals is required only of a municipality that has adopted a UCC ordinance (34 Pa. Code § 403.121(a)), and § 403.63(i) grants the right to appeal only “in a municipality which has adopted an ordinance.” The Industrial Board hears appeals of Department decisions — and in an opt-out municipality your decision-maker is a private company. So there is no statutory forum at all. In an enforcing municipality, by contrast, the board must convene within 30 days and decide within five business days, and if it misses that “the appeal shall be deemed granted” (35 P.S. § 7210.501(c)(5)).',
    },
  ],

  sourceNote:
    'Every claim was read against its primary source in September 2026: the Pennsylvania Construction Code Act and the Home Improvement Consumer Protection Act at legis.state.pa.us, 34 Pa. Code Chapter 403 and 25 Pa. Code Chapter 73 at pacodeandbulletin.gov, and the Department of Labor and Industry’s own Uniform Construction Code pages — including the municipal elections table, which was parsed municipality by municipality rather than quoted second-hand.',

  faqs: [
    {
      question: 'Can you build your own house in Pennsylvania without a license?',
      answer:
        'Yes, and there is nothing to apply for. Pennsylvania issues no general contractor license of any kind — the Department of Labor and Industry states on its own contractor licensing page that “the Commonwealth of Pennsylvania currently has no licensure or certification requirements for most construction contractors (or their employees).” That is why Pennsylvania has no owner-builder exemption: there is nothing to be exempt from. The one state registration that touches residential work, the Home Improvement Consumer Protection Act, excludes your project twice over — 73 P.S. § 517.2 says the term home improvement “does not include … the construction of a new home,” and separately excludes “any work performed without compensation by the owner of the owner’s private residence.” You will still pull a UCC permit and pass five inspections.',
    },
    {
      question: 'What does it mean if my Pennsylvania township opted out of the UCC?',
      answer:
        'It means the township is not running a code enforcement program — not that the code stopped applying. The Uniform Construction Code still binds your house, and the five statutory inspections still have to happen. What changes is that the duty to find an inspector moves onto you: 34 Pa. Code § 403.103(b) provides that “an applicant for a residential building permit shall obtain the services of a third-party agency certified in the appropriate categories to conduct the plan review and inspections.” The agency does your plan review as well, so it has to be engaged before you build, not when you are ready for a footing inspection. Labor and Industry is not the fallback — under § 403.103(g) the Department picks up only buildings other than residential in an opt-out municipality. As of September 2026, L&I’s own municipal elections table showed 119 of 2,563 municipalities opted out, spread across 34 of the 67 counties, with no county entirely opted out.',
    },
    {
      question: 'How many inspections does Pennsylvania require on a new house?',
      answer:
        'Five, and they are named in the statute rather than left to local practice. 35 P.S. § 7210.501(e)(1) requires a foundation inspection; a plumbing, mechanical and electrical inspection; a frame and masonry inspection; a wallboard inspection; and a final inspection — and adds that “the final inspection shall not be deemed approved until all previous inspections have been successfully completed and passed.” 34 Pa. Code § 403.64(d) and (f) repeat the list for municipalities that administer the code. Your code official may conduct additional inspections under § 403.64(e), and many municipalities do, so a local list of ten or twelve items is normal and lawful — but five is the statewide floor, and the wallboard inspection is the one owner-builders forget because most states have no equivalent.',
    },
    {
      question: 'Which building code does Pennsylvania use in 2026?',
      answer:
        'The 2021 I-Codes, effective 1 January 2026, adopted by a regulation published at 55 Pa.B. 7701 amending 34 Pa. Code § 403.21. Be careful checking this: as this kit was compiled, L&I’s own Uniform Construction Code home page still described the 2018 series with an effective date of 14 February 2022 — the previous cycle. The regulation governs, not the web page. Three things the 2021 adoption does not bring with it: appendices are not adopted at all under § 403.21(c), so there is no radon-resistant construction requirement; wall bracing is excluded and enforced from the 2006 IRC under 35 P.S. § 7210.304(i); and residential fire sprinklers are excluded outright under § 7210.304(g). The 2024 code review cycle is open — comments reopened through 4 October 2026 — but no effective date exists, and the last cycle ran about 59 months from publication to effect.',
    },
    {
      question: 'Does Pennsylvania require a licensed electrician or plumber?',
      answer:
        'Not at state level — there is no statewide electrician, plumber or HVAC license. L&I puts it this way: “Some of Pennsylvania’s 2,562 municipalities have established local licensure or certification requirements for contractors or construction trades people,” typically for home improvement, electrical and plumbing contractors. There is no central registry to search, so the municipality is the only authority on its own rules. One statutory exception is worth knowing before you buy a lot: in Allegheny County, plumbing is carved out of the UCC entirely. 35 P.S. § 7210.501(a.1) bars a municipality in a county of the second class from administering and enforcing the plumbing provisions, and the county enforces its own plumbing code under the Local Health Administration Law instead — a separate permit, a separate inspector and a separate rulebook.',
    },
    {
      question: 'Which NEC does Pennsylvania use?',
      answer:
        'None, and that is the honest answer. The Pennsylvania UCC adopts no edition of NFPA 70 for residential work — the phrases “NFPA 70” and “National Electrical Code” do not appear in 34 Pa. Code Chapter 403 at all. Residential wiring is governed by Chapters 34 through 43 of the 2021 IRC, sections E3401 to E4304, which is why every Pennsylvania electrical amendment is written in E-section numbers. The trap is not a lagging edition but a carve-back: three sections are struck from the 2021 IRC and replaced with older text. Island and peninsula countertop receptacles (E3901.4.2) and bathtub and shower space (E4002.11) revert to the 2018 IRC, and foyers (E3901.11) revert to the 2015 IRC, further modified so the trigger reads six feet rather than three. Those are three of the most routinely inspected receptacle items, and a current code book will give the wrong answer on all three. Everything else in Chapters 34 to 43, including all AFCI and GFCI requirements and service sizing, is the 2021 IRC as published.',
    },
  ],

  productDescription:
    'A 40-page print-ready permit kit for building your own home in Pennsylvania, in six documents. Covers the question that decides a Pennsylvania build — who administers the Uniform Construction Code where you are building — including the case at 34 Pa. Code § 403.103(b) where the owner must hire a certified third-party agency himself, and the appeals gap that comes with it. Also the five inspections named at 35 P.S. § 7210.501(e)(1), the fifteen-business-day review clock and the certification that cuts it to five, the Pennsylvania amendments that override the printed 2021 IRC — wall bracing enforced from the 2006 edition, the floor membrane requirement, three electrical sections carried back to earlier editions, and the energy tables the Commonwealth rewrote — the Allegheny County plumbing carve-out, the recreational cabin exclusion and its seven-part test, and the septic isolation distances at 25 Pa. Code § 73.13. Every claim is cited on the page it appears on and was verified against the Pennsylvania statutes, the Pennsylvania Code and the Department of Labor and Industry’s own documents in September 2026.',

  verifyNote:
    'Statutes, regulations and code editions change, and two Pennsylvania answers are moving right now: the 2024 code review cycle is open, and the municipal opt-in/opt-out table is updated continuously — a municipality may switch on 180 days’ notice. Confirm each rule with the office that will handle your parcel, which in an opt-out municipality is the agency you hire rather than a township department. The kit prints its sources so you can.',

  binderLead:
    'The Owner-Builder Job Site Binder picks up where the permit kit stops — and in Pennsylvania, where a private agency may hold your inspection file and no single office holds the whole record, your own paperwork matters more than usual. 367 pages of contracts, inspection forms, daily logs and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function PAPermitKit() {
  return <KitProductPage content={PA} />;
}
