import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/la-permit-kit' },
  title: 'Louisiana Owner-Builder Permit Kit — $34',
  description:
    'Louisiana permit kit: the exemption statute that was repealed in 2022, the $50,000 threshold that replaced the $75,000 one everybody still quotes, the construction-code chapter that moved to a different Title of the Revised Statutes on 1 August 2026, and the filing date that locks your code edition. 47 print-ready pages, every claim cited. $34 instant download.',
  keywords:
    'Louisiana building permit, Louisiana owner builder, Louisiana owner builder exemption, R.S. 37:2157, affidavit claiming exemption from licensure, Louisiana Uniform Construction Code Commission, LUCCC, Louisiana parish building permit, Louisiana septic permit LHS-47, Louisiana freeboard ASCE 24',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const LA: KitContent = {
  slug: 'la-permit-kit',
  heroSub:
    'The statute every Louisiana guide cites for the owner-builder exemption was repealed in 2022 — and the whole construction-code chapter moved to a different Title of the Revised Statutes on 1 August 2026.',
  pageCount: 47,
  revision: 'September 2026',

  heroSheets: {
    front: {
      src: '/kits/la/lak-hero-front.webp',
      alt: 'Louisiana Owner-Builder Permit Kit page headed “Two things almost every Louisiana guide still prints, and both are wrong”, correcting the repealed exemption statute R.S. 37:2170 to R.S. 37:2157(A)(13) and the $75,000 licensing threshold to $50,000',
    },
    back: {
      src: '/kits/la/lak-hero-back.webp',
      alt: 'Kit page explaining that a Louisiana inspector inspects against the codes in force on the date of the original permit application, above a callout on the statute renumbering that took effect 1 August 2026',
    },
  },

  documents: [
    {
      no: 'LA.0',
      pages: '3 pages',
      title: 'Cover & How to Use',
      copy: 'A job-site cover with the two fields Louisiana actually makes you resolve — your parish, and separately the office that issues your permit, which may be the town instead. Plus the one-page orientation.',
    },
    {
      no: 'LA.1',
      pages: '13 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy: 'The exemption that exists, the one that was repealed, and the affidavit that turns one into a permit. Then the structural point no Louisiana guide makes: your position is set by three separate chapters of law, and the contractor exemption reaches only the first of them.',
      thumb: '/kits/la/lak-exemption.webp',
      caption: 'LA.1 The two corrections the rest of the internet has not made',
      alt: 'Page 1 of LA.1, with a callout headed “Two things almost every Louisiana guide still prints, and both are wrong” — that R.S. 37:2170 and 37:2171 were repealed by Acts 2022 No. 195 and the exemption now lives at R.S. 37:2157(A)(13), and that the licensing threshold is fifty thousand dollars rather than the widely quoted $75,000',
    },
    {
      no: 'LA.2',
      pages: '12 pages',
      title: 'Permit Application Checklist',
      copy: 'Every code edition in force with its effective date, the filing deadline that decides which edition binds your house for the life of the build, the freeboard answer most guides get backwards, the statewide minimum lot size for a septic system, and a permit record to fill in as each one issues.',
      thumb: '/kits/la/lak-checklist.webp',
      caption: 'LA.2 The freeboard rule, quoted from the amendment itself',
      alt: 'Page 4 of LA.2: the Louisiana amendment to 2021 IRC Section R322.1 quoted in a bordered callout, showing that local jurisdictions may adopt higher freeboard amounts but may not adopt amounts less than those required in ASCE 24-14, with the kit’s explanation that Louisiana sets a floor rather than leaving elevation entirely to parishes',
    },
    {
      no: 'LA.3',
      pages: '7 pages',
      title: 'Inspection Sequence',
      copy: 'Who inspects your house — parish staff, a regional planning commission, a contracted firm, or an inspector you hire yourself under the route the statute gives homeowners by name. Plus the pre-permit approvals that other offices sign before the permit office will look at your application, and an inspection log.',
    },
    {
      no: 'LA.4',
      pages: '7 pages',
      title: 'Where to File Directory',
      copy: 'Parish or town, and how to settle which. A directory of 37 parish permitting offices read off each parish government’s own site, the contracted firms and regional commissions that act as building official in several parishes, and a page to write down every office you confirmed.',
      thumb: '/kits/la/lak-directory.webp',
      caption: 'LA.4 The belief this document exists to kill',
      alt: 'Page 1 of LA.4, headed “There is no such thing as a no-permit parish”, with a callout reporting that all 64 Louisiana parish governments were run through the Uniform Construction Code Commission’s public jurisdiction registry and all 64 returned a credential number',
    },
    {
      no: 'LA.5',
      pages: '5 pages',
      title: 'Forms & Documents Index',
      copy: 'Every document you will be asked for, named as the office that issues it names it — LHS-47, SF-10ST, SF-11ST, FORM-A, FORM-B, DNR-GW-1S — plus the short list of things that need no permit, and the exclusions hidden inside those carve-outs.',
    },
  ],

  includes: [
    '47 print-ready pages across 6 documents, letter size',
    'Every Louisiana claim cited on the page it appears on',
    'Write-in lines for everything your parish or town decides',
    'A permit record and an inspection log for the job site',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things Louisiana law actually says that the standard advice gets wrong. Each takes about a minute to check.',

  highlights: [
    {
      icon: 'doc',
      label: 'The exemption statute everyone cites was repealed',
      copy: 'R.S. 37:2170 and 37:2171 were repealed by Acts 2022, No. 195 — quoting them to a permit clerk loses an argument you should win. The exemption now lives at R.S. 37:2157(A)(13), and it is written in management verbs: owners who “supervise, superintend, oversee, direct, or in any manner assume charge” of building their personal residence. That means you may hire and direct subcontractors, not merely swing a hammer. The same section proves it by contrast — (A)(15)(a) exempts an owner who “physically performs” home improvement work, and those words are absent from (13).',
    },
    {
      icon: 'permit',
      label: 'The threshold is $50,000, not $75,000',
      copy: 'The figure in wide circulation is stale. R.S. 37:2150.1(19)(a) and (4)(a)(ii) set it at fifty thousand dollars — Louisiana rewrote this chapter in 2022, 2024 and again in 2025. And project value is measured more broadly than people expect: it “includes the entire cost of the labor, materials, rentals, and all direct and indirect project expenses … regardless of who pays the costs or if they are donated” (R.S. 37:2150.1(3)). Buying your own materials does not get you under the line.',
    },
    {
      icon: 'check',
      label: 'The whole code chapter moved on 1 August 2026',
      copy: 'Acts 2026, No. 881 enacted R.S. 37:3727–3750 and, by Section 5, repealed R.S. 40:1730.21 through 1730.40.2 “in its entirety.” The Council became the Commission. Every code-adoption tracker, guide and parish handout still citing Title 40 is citing repealed law — and at the time of verification the Legislature’s own statute database had not reloaded either, still serving the repealed sections and returning nothing for a Title 37 lookup.',
    },
    {
      icon: 'bolt',
      label: 'Your filing date locks your code edition',
      copy: 'R.S. 37:3734: an inspector “shall conduct a building inspection using the requirements of the codes in effect for the locality on the date of the application for the original building permit.” The Commission publishes 1 January 2027 as the effective date for the 2024 I-Codes and the 2023 NEC. So an application filed before that line holds your house to the 2021 I-Codes and the 2020 NEC through a framing inspection that may not happen until 2028. The date you file is a design decision.',
    },
  ],

  sourceNote:
    'Every claim was read against its primary source in September 2026: the enrolled text of Acts 2026 No. 881, the Louisiana Revised Statutes at legis.la.gov, the Louisiana Administrative Code at doa.la.gov, the Uniform Construction Code Commission’s own compiled law-and-rules volume of 1 August 2026 and its construction-code history sheet, the State Licensing Board for Contractors’ exemption affidavit, the Department of Health’s on-site wastewater forms and applicant packet, and each parish government’s own permit page.',

  faqs: [
    {
      question: 'Can you build your own house in Louisiana without a contractor license?',
      answer:
        'Yes, on your own personal residence — and the exemption is broader than most states’ because it is written in management verbs. R.S. 37:2157(A)(13) exempts “owners of property who supervise, superintend, oversee, direct, or in any manner assume charge of the construction … of their personal residences,” so you may act as your own general contractor and hire licensed subs rather than doing the work with your own hands. Two conditions: you may not build more than one residence per year, with the year running from the date the certificate of occupancy issues, and you must file an affidavit of exemption to get the permit. Note that almost every guide still cites R.S. 37:2170 for this — that section was repealed by Acts 2022, No. 195.',
    },
    {
      question: 'What is the Louisiana owner-builder affidavit, and who gets it?',
      answer:
        'It is the Louisiana State Licensing Board for Contractors’ “Affidavit Claiming Exemption from Licensure” — notarized, carrying no form number but a revision date, and structured as eleven separate statements you initial individually. The form comes from the state board; the signed affidavit goes to your local parish or municipal permit official, not back to the board. R.S. 37:2160(C) requires it “prior to the issuance of a permit.” The reason your clerk insists is that R.S. 37:2160(B) forbids a local building department from issuing a permit to an unlicensed person at all, except for work requiring no license — the affidavit is how you prove you are in that carve-out. Watch out for the Church Owner/Builder Affidavit on the same forms page; confusingly, the words “Owner/Builder” are in the church form’s title and not in yours.',
    },
    {
      question: 'Is there a Louisiana parish where you can build without a permit?',
      answer:
        'No. R.S. 37:3737(A)(1) says all municipalities and parishes “shall enforce” the Uniform Construction Code and adds that “nothing in this Chapter allows any local government to avoid enforcement.” The older mechanism by which a parish could file an affidavit claiming exemption is gone from the operative text. We ran all 64 parish governments through the Commission’s public jurisdiction registry and all 64 returned a credential number. What varies is staffing, not authority — and where a parish counter is quiet, the statute names your route: homeowners exempted under R.S. 37:2157 “may establish agreements with private inspectors to conduct plan reviews, inspections, and enforce the State Uniform Construction Code,” provided that inspector is contracted with or registered to your jurisdiction.',
    },
    {
      question: 'Can a homeowner do their own plumbing and electrical work in Louisiana?',
      answer:
        'Plumbing on your own home, yes — but not by the mechanism people describe. There is no homeowner exemption in the plumbing licensing sections; R.S. 37:1367 requires the board’s license of any natural person doing the work and names no owner. The allowance is in the definitions instead, and is stronger for it: R.S. 37:1377(D) says that for purposes of the chapter “plumbing” does not include “(8) Work done by an individual on his own personal residence,” so the license requirement never attaches. Gas fitting has its own separate exemption at R.S. 37:1367(J)(2). Electrical is different again — Louisiana has no state journeyman or master electrician license at all. The state licenses the electrical contractor, the business selling the work; credentialing the individual is left to municipalities under R.S. 33:4782 and is optional even for them, with New Orleans expressly carved out. Ask your permit office whether a homeowner may pull the electrical permit where you are building.',
    },
    {
      question: 'Can I install my own septic system in Louisiana?',
      answer:
        'A conventional one, yes. LAC 51:XIII.705.A says an installer license “shall not be required … for an individual wishing to install an individual sewerage system, other than an individual mechanical plant, for his own private, personal use.” Three limits catch people. You must do the actual installation yourself, and the health department’s own form warns that “hiring an unlicensed person to perform any part of the installation … will not be allowed under this exception.” Nothing may be covered until a sanitarian has verified it. And an individual mechanical plant — the aerobic unit Louisiana leans on wherever soils and water tables defeat a conventional field — must be installed by a licensed installer. Water wells are the mirror image: LAC 56:I.307.A requires a licensed contractor for “all water wells, regardless of use or type,” so you may dig your own drainfield but you may not drill your own well.',
    },
    {
      question: 'Does Louisiana require freeboard above base flood elevation?',
      answer:
        'Yes, indirectly — and the two claims in circulation are both wrong. Louisiana does not write a number like “BFE plus one foot” into its code, but it does not leave elevation purely to parishes either. Its amendment to 2021 IRC Section R322.1 provides that local jurisdictions “shall have the authority to adopt higher freeboard amounts as needed (CRS, etc.) but shall not have the authority to adopt freeboard amounts less than those required in ASCE-24-14.” So ASCE 24-14 sets a statewide floor by reference, your parish may go above it and may not go below it, and the figure for your lot depends on your flood zone and flood design class. Ask your parish floodplain manager in writing for the required lowest-floor elevation, and ask separately whether the parish has adopted freeboard above the state floor.',
    },
  ],

  productDescription:
    'A 47-page print-ready permit kit for building your own home in Louisiana, in six documents. Covers the owner-builder exemption at R.S. 37:2157(A)(13) and the repealed statute most guides still cite, the LSLBC affidavit and the eleven statements you initial on it, the $50,000 threshold and how Louisiana measures project value, the three separate chapters of law that govern electrical, plumbing and septic work on your own house, every code edition in force with its effective date, the filing-date rule that locks your code edition for the life of the build, the ASCE 24-14 freeboard floor, the statewide minimum lot size for a septic system, and a directory of parish permitting offices read off each parish government’s own site. Every claim is cited on the page it appears on and was verified against the enrolled text of Acts 2026 No. 881, the Louisiana Revised Statutes, the Louisiana Administrative Code and the administering agencies’ own forms in September 2026.',

  verifyNote:
    'Louisiana rewrote its contractor chapter three times in four years and moved its entire construction-code chapter to a different Title of the Revised Statutes on 1 August 2026. Code editions turn over again on 1 January 2027. Confirm each rule with your parish or municipal permit office — and expect to meet the old citations, because most sources have not caught up. The kit prints its sources so you can check.',

  binderLead:
    'The Owner-Builder Job Site Binder picks up where the permit kit stops. In Louisiana the permit is the part with a clear answer; the twelve months after it are the part that needs a system. 367 pages of contracts, inspection forms, daily logs and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function LAPermitKit() {
  return <KitProductPage content={LA} />;
}
