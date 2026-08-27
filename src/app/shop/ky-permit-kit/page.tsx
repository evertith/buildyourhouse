import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/ky-permit-kit' },
  title: 'Kentucky Owner-Builder Permit Kit — $34',
  description:
    'Kentucky permit kit: the building permit your county may not require, the three state permits that apply anyway, the 2023 NEC articles Kentucky has not switched on, and the two utilities that will not connect you. 39 print-ready pages, every claim cited. $34 instant download.',
  keywords:
    'Kentucky building permit, Kentucky owner builder, do I need a building permit in Kentucky, Kentucky state plumbing permit, Kentucky residential code, KRS 198B.060, Kentucky homeowner electrical permit, Kentucky county building inspector',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const KY: KitContent = {
  slug: 'ky-permit-kit',
  heroSub:
    'In roughly one Kentucky county in three, nobody will ever inspect your house — and you still cannot get power or water without two signatures.',
  pageCount: 39,
  revision: 'August 2026',

  heroSheets: {
    front: {
      src: '/kits/ky/kyk-hero-front.webp',
      alt: 'Kentucky Owner-Builder Permit Kit page quoting the statute and the code regulation that both make permits, inspections and certificates of occupancy optional for a single-family dwelling absent a local ordinance',
    },
    back: {
      src: '/kits/ky/kyk-hero-back.webp',
      alt: 'Kit page listing every Kentucky code edition in force above a callout on which 2023 NEC articles are enforceable and which remain delayed',
    },
  },

  documents: [
    {
      no: 'KY.0',
      pages: '3 pages',
      title: 'Cover & How to Use',
      copy: 'A job-site cover with the fields Kentucky actually makes you resolve, including a Local Building Department line with an explicit instruction to write NONE. Plus the one-page orientation.',
    },
    {
      no: 'KY.1',
      pages: '10 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy: 'There is no Kentucky state builder license to be exempt from — so this document answers the question that actually governs your build: does a building permit exist where you are building? Then the three trade exemptions, which are three different tests, and a qualification checklist.',
      thumb: '/kits/ky/kyk-exemption.webp',
      caption: 'KY.1 The sentence that decides your build',
      alt: 'Page 2 of KY.1, quoting KRS 198B.060(1) and 815 KAR 7:125 Section 2(2)(a) side by side, showing that permits, inspections and certificates of occupancy are not mandatory for a single-family residence unless a local ordinance requires them',
    },
    {
      no: 'KY.2',
      pages: '10 pages',
      title: 'Permit Application Checklist',
      copy: 'The septic permit that gates the state plumbing permit by statute, the workers compensation affidavit, every code edition in force, the NEC articles Kentucky still has not switched on, published state fees, and a permit record to fill in as each one issues.',
      thumb: '/kits/ky/kyk-checklist.webp',
      caption: 'KY.2 What is actually in force in Kentucky',
      alt: 'Page 6 of KY.2: the table of code editions in force in Kentucky — the 2023 NEC with delays still in force, the 2009 IECC, the 2015 IMC, NFPA 54 for fuel gas and Kentucky’s own plumbing code — above the callout explaining which delayed NEC articles became enforceable on 15 July 2026 and which remain unenforceable',
    },
    {
      no: 'KY.3',
      pages: '5 pages',
      title: 'Inspection Sequence',
      copy: 'Split into the approvals that happen wherever you build and the building inspections that happen only if your jurisdiction requires them. Includes the one statutory inspection clock Kentucky gives you, and an inspection log.',
    },
    {
      no: 'KY.4',
      pages: '6 pages',
      title: 'Where to File Directory',
      copy: 'How to find the per-county inspector sheet the state publishes and almost nobody knows about — it names your plumbing inspector, their office hours, your electrical inspector and your septic contact, and tells you whether a local building inspector exists at all.',
      thumb: '/kits/ky/kyk-directory.webp',
      caption: 'KY.4 The mistake this document exists to prevent',
      alt: 'Page 2 of KY.4: the callout reporting that of Kentucky’s 119 county inspector sheets, 25 print None for local building inspector, 6 leave the field empty and 10 carry no such line at all — 41 of 119 — with the caveat that the sheets are a contact list rather than a register of ordinances',
    },
    {
      no: 'KY.5',
      pages: '5 pages',
      title: 'Forms & Documents Index',
      copy: 'Every document you will meet, named as the Department names it, with what needs no permit at all — including the farmstead carve-out that is real but far narrower than people assume.',
    },
  ],

  includes: [
    '39 print-ready pages across 6 documents, letter size',
    'Every Kentucky claim cited on the page it appears on',
    'Write-in lines for everything that depends on your local ordinance',
    'A permit record and an inspection log for the job site',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things Kentucky law actually says that the standard advice gets wrong. Each takes about a minute to check.',

  highlights: [
    {
      icon: 'permit',
      label: 'Your building permit may not exist',
      copy: 'Permits, inspections and certificates of occupancy “shall not be mandatory for single-family residences unless a local government passes an ordinance” (KRS 198B.060(1)), and the code regulation repeats it (815 KAR 7:125 §2(2)(a)). The state is then barred from filling the gap: it “shall not preempt or assert jurisdiction for the enforcement of the code on single-family dwellings” (KRS 198B.060(4)(b)).',
    },
    {
      icon: 'check',
      label: 'Three state permits apply anyway',
      copy: 'The plumbing installation permit comes from the state and KRS Chapter 318 is in force “in all counties of the Commonwealth” (KRS 318.134(1)(a), 318.015(1)). An HVAC permit is required before an initial system in any building designed for human occupancy (KRS 198B.6671(1)). And your septic permit must accompany the plumbing application by statute (KRS 318.134(2)).',
    },
    {
      icon: 'bolt',
      label: 'The utilities are the real inspectors',
      copy: 'No utility may “initiate permanent electrical service to any new building” until a certified electrical inspector issues a final certificate of approval (KRS 198B.060(11)), and no public utility or water district may provide permanent water until the plumbing is installed and approved (KRS 318.165). In a no-ordinance county those two signatures are the enforcement.',
    },
    {
      icon: 'doc',
      label: 'Kentucky has not switched on all of the 2023 NEC',
      copy: 'Three delayed articles — 210.52(C), 230.67 and 314.27(C) — became enforceable on 15 July 2026, so guides written earlier are stale. But 210.8(A) and 210.8(D)(8)–(11) GFCI requirements “remain delayed and are not yet enforceable,” which is the half that changes what you install. Permits issued before 15 July 2026 are grandfathered.',
    },
  ],

  sourceNote:
    'Every claim was read against its primary source in August 2026: the Kentucky Revised Statutes and Administrative Regulations at apps.legislature.ky.gov, and the Department of Housing, Buildings and Construction’s own adopted-code list, NEC enforcement notices and all 119 county inspector sheets at dhbc.ky.gov.',

  faqs: [
    {
      question: 'Do you need a building permit to build a house in Kentucky?',
      answer:
        'Often, no. KRS 198B.060(1) says permits, inspections and certificates of occupancy “shall not be mandatory for single-family residences unless a local government passes an ordinance requiring inspections of single-family residences,” and 815 KAR 7:125 Section 2(2)(a) repeats it in the code regulation itself. The Department of Housing, Buildings and Construction cannot step in either — it “shall not preempt or assert jurisdiction for the enforcement of the code on single-family dwellings.” On the state’s own county inspector sheets, 25 counties print “None” for local building inspector, 6 leave the field empty and 10 more carry no such line at all — 41 of 119. Ask your city and your county; both answers matter.',
    },
    {
      question: 'Does the Kentucky Residential Code still apply if my county has no building permit?',
      answer:
        'Yes. The code is mandatory statewide and reaches your house by definition — KRS 198B.010(4) says “building” “also means single-family dwellings,” and KRS 198B.050(1) requires a mandatory Uniform State Building Code. What disappears in a county with no ordinance is the inspection, not the standard and not your liability. Kentucky also adds a specific cost to skipping the certificate of occupancy: under KRS 198B.130, an award against you in a code-violation claim “may also include reasonable attorney’s fees” if no certificate of occupancy was issued, for up to ten years after first occupation.',
    },
    {
      question: 'Can a homeowner do their own electrical work in Kentucky?',
      answer:
        'Yes, and the exemption is wider than almost every guide states. KRS 227A.030(3) reads in full: “Nothing in KRS 227A.010 to 227A.140 shall prohibit or interfere with the ability of a homeowner or farmer to install or repair electrical wiring on his or her real property.” There is no occupancy condition, no single-family limitation, no requirement that you personally perform the work and no affidavit — and farmers are named expressly. It exempts you from the license only, not from the certified electrical inspector’s final certificate of approval, which your power company needs before it can connect permanent service.',
    },
    {
      question: 'Do I need a state plumbing permit in Kentucky?',
      answer:
        'Yes, wherever you build. KRS 318.134(1)(a) bars anyone from constructing or altering plumbing “without first having procured a plumbing installation permit therefor from the department,” and KRS 318.015(1) puts the chapter “in full force and effect in all counties of the Commonwealth” — with one carve-out, farmsteads. A homeowner can hold the permit under 815 KAR 20:050 Section 2(1)(b) by filing an affidavit, performing all the work personally, and not having obtained another homeowner permit for a new home in the last five years. The fee is set in regulation: $50 base plus $14 per fixture, with five inspections included.',
    },
    {
      question: 'Is there a general contractor license in Kentucky?',
      answer:
        'No. Kentucky licenses trades, not builders — electricians and electrical contractors under KRS Chapter 227A, master and journeyman plumbers under KRS Chapter 318, and HVAC contractors and mechanics under KRS 198B.650 to 198B.689, plus elevator, boiler, fire sprinkler and manufactured-housing work. There is no state residential general contractor or home builder license, so acting as your own builder is not an exemption you claim; it is simply something you are allowed to do. Your city or county may still require a local business or contractor registration.',
    },
    {
      question: 'What building code does Kentucky use in 2026?',
      answer:
        'The 2018 Kentucky Residential Code, Third Edition (August 2024), based on the 2015 International Residential Code, effective 3 December 2024 under 815 KAR 7:125. Electrical is the 2023 NEC, but with Kentucky delays: 210.52(C), 230.67 and 314.27(C) became enforceable on 15 July 2026, while 210.8(A) and 210.8(D)(8)–(11) GFCI requirements remain delayed. Residential energy is the 2009 IECC, mechanical is the 2015 IMC, fuel gas is NFPA 54, the National Fuel Gas Code, rather than the IFGC — the Department’s documents conflict on the edition, so ask your inspector which one — and plumbing is Kentucky’s own State Plumbing Code at 815 KAR Chapter 20. Kentucky adopts neither the IPC nor the UPC.',
    },
  ],

  productDescription:
    'A 39-page print-ready permit kit for building your own home in Kentucky, in six documents. Covers the local-option building permit under KRS 198B.060, the three state permits that apply regardless, the homeowner electrical, plumbing and HVAC exemptions and their three different tests, the current code editions including Kentucky’s delayed 2023 NEC articles, and a per-county directory built from the Department of Housing, Buildings and Construction’s own inspector sheets. Every claim is cited on the page it appears on and was verified against the Kentucky Revised Statutes, the Kentucky Administrative Regulations and the Department’s own documents in August 2026.',

  verifyNote:
    'Statutes, regulations and code editions change, and in Kentucky the building permit itself depends on a local ordinance. Confirm each rule with your city and your county — and with the Department for the state plumbing and HVAC permits. The kit prints its sources so you can.',

  binderLead:
    'The Owner-Builder Job Site Binder picks up where the permit kit stops — because in Kentucky the permit may be the shortest part of the job. 367 pages of contracts, inspection forms, daily logs and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function KYPermitKit() {
  return <KitProductPage content={KY} />;
}
