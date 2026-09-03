import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/sc-permit-kit' },
  title: 'South Carolina Owner-Builder Permit Kit — $34',
  description:
    'South Carolina permit kit: the register-of-deeds notice that revokes your exemption if you skip it, the $500 threshold that decides who you may hire, the energy code set by statute instead of by the code council, and the beachfront setback measured in erosion rates. 55 print-ready pages, every claim cited. $34 instant download.',
  keywords:
    'South Carolina owner builder permit, SC building permit, owner builder exemption South Carolina, 40-59-260, SC register of deeds notice, South Carolina Residential Builders Commission, SC building codes council, SCDES septic permit',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const SC: KitContent = {
  slug: 'sc-permit-kit',
  heroSub:
    'South Carolina does not ask whether anyone will inspect your house — a statute already answered that. It asks which of the small obligations attached to your exemption you are going to forget.',
  pageCount: 55,
  revision: 'September 2026',

  heroSheets: {
    front: {
      src: '/kits/sc/sck-hero-front.webp',
      alt: 'South Carolina Owner-Builder Permit Kit page setting out three dollar thresholds side by side — $500 for a residential specialty contractor, $5,000 for a residential builder, and $10,000 for a general or mechanical contractor — each with the statute it comes from',
    },
    back: {
      src: '/kits/sc/sck-hero-back.webp',
      alt: 'Kit page listing the South Carolina code editions in force, showing the 2021 residential code beside a 2020 National Electrical Code and a 2009 energy standard set by statute rather than by the code council',
    },
  },

  documents: [
    {
      no: 'SC.0',
      pages: '3 pages',
      title: 'Cover & How to Use',
      copy: 'A job-site cover with the fields South Carolina actually makes you resolve — including a Register of Deeds line, because the office that indexes your owner-builder notice can revoke your exemption. Plus the one-page orientation.',
    },
    {
      no: 'SC.1',
      pages: '11 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy: 'The three conditions in § 40-59-260(A), the disclosure statement printed word for word, and the notice you file after the house is finished — the one whose omission the statute says revokes the exemption outright. Plus the three dollar thresholds, in two chapters, administered by two different boards.',
      thumb: '/kits/sc/sck-exemption.webp',
      caption: 'SC.1 Three thresholds, two chapters',
      alt: 'Page 6 of SC.1: a table setting $500 for a residential specialty contractor against $5,000 for a residential builder and $10,000 for a general or mechanical contractor, with the statutory sentence and the citation for each, above a note explaining that a fourth $5,000 figure is the bonding trigger and not a licensing one',
    },
    {
      no: 'SC.2',
      pages: '13 pages',
      title: 'Permit Application Checklist',
      copy: 'Every code edition in force and where the regulation says so, the 1 January 2027 rollover already on the calendar and why your permit date decides whether it reaches you, the energy standard the code council has no power to move, the termite amendment that bans foam plastic below grade, and where the wind maps actually live.',
      thumb: '/kits/sc/sck-checklist.webp',
      caption: 'SC.2 What is actually in force in South Carolina',
      alt: 'Page 1 of SC.2: the table of South Carolina code editions in force — the 2021 residential, building, plumbing, mechanical, fuel gas and fire codes, the 2020 National Electrical Code, and a 2009 energy standard — each row citing the article of Chapter 8 of the Code of Regulations that carries it',
    },
    {
      no: 'SC.3',
      pages: '13 pages',
      title: 'Inspection Sequence',
      copy: 'The approvals that sit upstream of your permit, the septic and well separations that decide whether your lot works at all, the beachfront lines that moved in July 2026, the inspection order, and the two closing acts most owner-builders treat as one.',
      thumb: '/kits/sc/sck-inspections.webp',
      caption: 'SC.3 The two lines, and what each side of them costs',
      alt: 'Page 3 of SC.3: a table explaining South Carolina beachfront jurisdiction — the baseline at the crest of the primary dune, the setback line at forty times the annual erosion rate and never less than twenty feet landward, and the difference between a no-fee written certification capped at 5,000 square feet of heated space and a permit carrying a $1,000 fee',
    },
    {
      no: 'SC.4',
      pages: '8 pages',
      title: 'Where to File Directory',
      copy: 'Twenty counties and fifteen municipalities with the office each one actually calls its own, the nine offices that are not your building department, and three dead ends still circulating — including a county domain that now belongs to somebody else entirely.',
    },
    {
      no: 'SC.5',
      pages: '7 pages',
      title: 'Forms & Documents Index',
      copy: 'Every document you will meet, named as the office names it. Plus the statewide statutory list of work that needs no permit and no credential at all — which South Carolina put in the licensing chapter, where nobody looks for it.',
    },
  ],

  includes: [
    '55 print-ready pages across 6 documents, letter size',
    'Every South Carolina claim cited on the page it appears on',
    'Write-in lines for everything that varies by county',
    'A permit record, an inspection log and a confirmed-offices page for the job site',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things South Carolina law actually says that the standard advice gets wrong. Each takes about a minute to check.',

  highlights: [
    {
      icon: 'doc',
      label: 'A filing after the build can revoke your exemption',
      copy: 'Section 40-59-260(E) requires the owner to “promptly file as a matter of public record a notice with the register of deeds, indexed under the owner’s name in the grantor’s index,” stating the structure “was constructed by the owner as an unlicensed builder.” Then: “Failure to do so revokes the statutory exemption.” No fine, no cure period, no deadline in days — the exemption you already built under simply stops having been yours. Subsection (D) obliges the permit office to hand you the forms when you sign, so ask for them at the counter. Several counties invert the timing and record it before the permit issues.',
    },
    {
      icon: 'permit',
      label: 'The number that matters is $500, not $5,000',
      copy: 'Every guide prints $5,000. That is the residential builder threshold at § 40-59-20(6) — the license you are exempt from. The number that decides whether the person you are paying is legal is $500, the residential specialty threshold at § 40-59-20(7), raised from $200 by 2022 Act No. 186. Chapter 11 general and mechanical contracting is a third number, $10,000, raised from $5,000 in 2023. And only three trades are licensed by examination — plumbers, electricians and HVAC; the other ten on the statutory list are registrations.',
    },
    {
      icon: 'bolt',
      label: 'The energy code is a statute, so the code council cannot move it',
      copy: 'South Carolina runs on the 2009 IECC, and the reason is not inertia. Regulation 8-1230 reads in full: “IRC Chapter 11 Energy Efficiency. The Building Codes Council does not adopt IRC Chapter 11.” What applies instead is § 6-10-30, the Energy Standard Act: “The 2009 edition of the International Energy Conservation Code is adopted as the Energy Standard.” That sentence was last changed by 2012 Act No. 143. Moving it takes an act of the General Assembly, not a code cycle — which also means no plan reviewer can move it on you.',
    },
    {
      icon: 'check',
      label: 'Nobody can honestly give you a wind speed by county',
      copy: 'The code sends you to “the previously published maps by the South Carolina Building Codes Council,” and § 6-9-105(C) says climatological boundaries must follow “major highways, waterbodies, or ridgelines” and that “political boundaries may not be used.” The maps are real and downloadable — the kit names the page — but they are hand-drawn contours where “interpolation between wind speed lines is determined by the AHJ,” they are keyed to an older code edition than the one they sit inside, and eleven counties have no map at all, including Greenville, Spartanburg and Anderson. For those the code names the ATC website, which went offline in 2026. The kit gives you the range for orientation, the working substitute, and a line for the number your official puts in writing.',
    },
  ],

  sourceNote:
    'Every claim was read against its primary source in September 2026: the S.C. Code of Laws and the S.C. Code of Regulations at scstatehouse.gov, the Department of Labor, Licensing and Regulation’s Residential Builders Commission and Building Codes Council material at llr.sc.gov, and the Department of Environmental Services’ own septic, well and coastal pages at des.sc.gov. The state’s code amendments are quoted from Chapter 8 of the Code of Regulations — where § 6-9-55 requires them to be promulgated — rather than from the Council’s own website, which still serves a scanned 2019 document for the previous code edition.',

  faqs: [
    {
      question: 'Can you build your own house in South Carolina without a contractor license?',
      answer:
        'Yes. S.C. Code § 40-59-260(A) says the licensing chapter “does not apply to an owner of residential property who improves the property” where three things hold: the owner does the work himself, with his own employees, or with licensed contractors and registered entities or individuals; the structure is intended for the owner’s sole occupancy or occupancy by the owner’s family and is not intended for sale or rent; and the general public does not have access to it. There is no square-footage cap and no limit on how often you may use it — read § 40-59-260 and § 40-11-360(5) end to end and no number of that kind appears in either. What the exemption does require is that you personally appear and sign the permit application, take a disclosure statement the statute prints in full, and afterwards file a notice at the register of deeds.',
    },
    {
      question: 'What is the South Carolina register of deeds notice, and what happens if I skip it?',
      answer:
        'It is the step almost every guide either omits or states without its consequence. Under § 40-59-260(E), an owner who has built under the exemption “must promptly file as a matter of public record a notice with the register of deeds, indexed under the owner’s name in the grantor’s index, stating that the residential building or structure was constructed by the owner as an unlicensed builder.” The next sentence is the whole point: “Failure to do so revokes the statutory exemption.” There is no fine and no cure period — the effect is that you retrospectively become someone who did residential building without a license, which § 40-59-30(A) makes a misdemeanor carrying $500 to $10,000 or not less than thirty days. The statute says “promptly” and gives no day count, and § 40-59-260(D) obliges the permitting agency to hand you the necessary forms at the moment you sign the application. Counties differ on timing: Greenville requires the disclosure notarized and recorded before submission, and Sumter requires recording before the permit issues.',
    },
    {
      question: 'Can a homeowner do their own electrical and plumbing work in South Carolina?',
      answer:
        'On your own home the state licensing statute does not stand in your way — § 40-59-260(A) removes Chapter 59 from an owner “who does the work himself,” and residential electrical, plumbing and HVAC are licensed inside that same chapter as specialty contractor licenses. The City of Aiken publishes the clearest local confirmation, stating that no license is required to do your own building, plumbing, electrical or mechanical work on your own house. But the exemption is a licensing exemption only: it does not waive the permit, the code or the inspection, and the disclosure you sign says your construction “must comply with all applicable laws, ordinances, building codes, and zoning regulations.” The practical gate is local — your building department decides what it will issue a homeowner trade permit for, and Charleston County, for one, bars homeowners from pulling permits for work on a manufactured home. Ask before you plan a schedule around it. Anyone you pay more than $500 for those trades must hold the license.',
    },
    {
      question: 'What is the South Carolina owner-builder two-year rule?',
      answer:
        'It is an evidence rule, not a ban on selling. Section 40-59-260(B) provides that “proof of the sale or rent or the offering for sale or rent of the structure by the owner-builder within two years after completion or issuance of a certificate or occupancy is prima facie evidence that the project was undertaken for the purpose of sale or rent, unless otherwise approved by the commission.” Four things people miss. Merely offering counts — you do not have to close. “Rent” is defined to include any arrangement where the owner receives compensation “in money, provisions, chattel, or labor from the occupancy,” so letting someone live there in exchange for work on the place is renting it. The window runs from completion or from the certificate of occupancy, which are usually different dates and the statute does not say which controls. And the escape clause — “unless otherwise approved by the commission” — is real but has no published procedure, form or fee, so raise it early and in writing if you can foresee needing it. The Chapter 11 twin at § 40-11-360(5) states the same presumption without the escape.',
    },
    {
      question: 'Who issues septic and well permits in South Carolina now that DHEC is gone?',
      answer:
        'Both come from the Department of Environmental Services (SCDES) at des.sc.gov — septic under Permits and Regulations, private wells under Programs, Bureau of Water, Residential Wells. The Department of Health and Environmental Control was abolished by 2023 Act No. 60 effective 1 July 2024, with environmental programs going to SCDES and public health to the Department of Public Health at dph.sc.gov. This matters practically because the old domain was not redirected — scdhec.gov serves nothing at all — and a surprising number of county websites still link septic guidance to it. One South Carolina answer is genuinely unusual: you may drill your own well. Regulation 61-44 defines a well driller to include owners constructing wells “on their own property for their own personal use only,” and exempts them from the state licensing and bonding requirements. You still need coverage under the general permit, which means filing a Notice of Intent — and the agency must answer within 48 hours excluding weekends and holidays, failing which coverage is deemed approved.',
    },
    {
      question: 'Which building code is in effect in South Carolina in 2026?',
      answer:
        'The 2021 suite, adopted by the Building Codes Council on 6 October 2021 with an implementation date for local jurisdictions of 1 January 2023: the 2021 IRC, IBC, IPC, IMC, IFGC and IFC, all as modified. Two rows do not follow the pattern and are the ones most often misreported. Electrical is the 2020 National Electrical Code, not a 2021 edition. And energy is the 2009 IECC, because the Council “does not adopt IRC Chapter 11” (Reg. 8-1230) and the Energy Standard is fixed by statute at § 6-10-30. The amendments themselves are codified in Chapter 8, Articles 8 through 14 of the Code of Regulations — § 6-9-55 requires anything affecting one- and two-family dwellings to be promulgated as a regulation before it can be enforced — and they are free to read. Do not use the PDF on the Council’s own Codes page: as of September 2026 the link named “Residential Code” serves a scanned copy of a May 2019 State Register document covering the 2018 IRC. And there is a date already on the calendar: on 26 August 2025 the Council adopted the 2024 I-Codes and the 2023 NEC with an implementation date of 1 January 2027. The energy standard does not move with them. Section 6-9-130(A) fixes your house to the codes in effect on the date your original building permit was issued, so a permit issued before 1 January 2027 keeps your whole build on the stack described here, however long it runs.',
    },
  ],

  productDescription:
    'A 55-page print-ready permit kit for building your own home in South Carolina, in six documents. Covers the owner-builder exemption at § 40-59-260 — its three conditions, the disclosure statement the statute prints in full, and the register-of-deeds notice whose omission the statute says revokes the exemption — plus the three dollar thresholds that decide who you may pay, the code editions actually in force and where the regulation says so, the energy standard set by statute rather than by the code council, the termite amendments that bar foam plastic below grade, the septic and well separation distances that decide whether a lot works, and the beachfront setback measured at forty times the annual erosion rate. Every claim is cited on the page it appears on and was verified against the S.C. Code of Laws, the S.C. Code of Regulations and the state agencies’ own material in September 2026.',

  verifyNote:
    'Statutes, regulations and code editions change, and South Carolina has two dates already on the calendar: the 2024 codes and the 2023 electrical code take effect 1 January 2027, and the beachfront jurisdictional lines are mid-cycle — Phase I took effect 24 July 2026 and Phase II, covering the greater Charleston beaches, runs through 2028. Confirm each rule with the office that will handle your parcel — your building department, and separately your septic, well and coastal offices. The kit prints its sources so you can.',

  binderLead:
    'The Owner-Builder Job Site Binder picks up where the permit kit stops. 367 pages of contracts, inspection forms, daily logs and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function SCPermitKit() {
  return <KitProductPage content={SC} />;
}
