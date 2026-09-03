import type { Metadata } from 'next';
import KitProductPage from '@/components/shop/KitProductPage';
import type { KitContent } from '@/lib/kit-content';

export const metadata: Metadata = {
  alternates: { canonical: '/shop/oh-permit-kit' },
  title: 'Ohio Owner-Builder Permit Kit — $34',
  description:
    'Ohio permit kit: the code section that excuses you from permits where no department is certified, the 23 counties with no residential certification anywhere, the 2023 NEC change almost every guide still prints as 2017, and the state trade licenses that do not reach your house. 51 print-ready pages, every claim cited. $34 instant download.',
  keywords:
    'Ohio owner builder permit, Residential Code of Ohio, RCO 101.5, Ohio building permit not required, certified residential building department Ohio, Ohio 2023 NEC, OCILB residential, Ohio septic permit OAC 3701-29',
  openGraph: { images: ['/binder/og-shop.jpg'] },
};

const OH: KitContent = {
  slug: 'oh-permit-kit',
  heroSub:
    'Ohio writes one residential code for the whole state, applies it to your house by its own terms — and then, in that same code, tells you when you do not have to file anything at all.',
  pageCount: 51,
  revision: 'September 2026',

  heroSheets: {
    front: {
      src: '/kits/oh/ohk-hero-front.webp',
      alt: 'Ohio Owner-Builder Permit Kit page quoting RCO section 101.5 beside Revised Code section 3791.04, showing that commercial plans fall back to the state when no local department is certified while residential plans go nowhere',
    },
    back: {
      src: '/kits/oh/ohk-hero-back.webp',
      alt: 'Kit page listing the Ohio code editions in force above a box explaining that the referenced electrical standard is printed as a redline reading seventy dash seventeen struck through and twenty-three inserted',
    },
  },

  documents: [
    {
      no: 'OH.0',
      pages: '3 pages',
      title: 'Cover & How to Use',
      copy: 'A job-site cover with the fields Ohio actually makes you resolve — including a building department line you may legitimately fill in as NONE, and a Local Health District line, because in rural Ohio that office matters more. Plus the one-page orientation.',
    },
    {
      no: 'OH.1',
      pages: '12 pages',
      title: 'Owner-Builder Exemption Walkthrough',
      copy: 'Why Ohio has no owner-builder exemption and does not need one, the four-link definition chain that puts your house outside the state trade licenses entirely, the two texts that decide whether anyone permits your parcel, and the lien rule that means you cannot be made to pay twice.',
      thumb: '/kits/oh/ohk-exemption.webp',
      caption: 'OH.1 The question that decides your build',
      alt: 'Page 4 of OH.1: a box quoting RCO section 101.5 and Revised Code section 3791.04(A)(1) side by side, showing that where no department is certified for nonresidential work plans go to the superintendent of industrial compliance, while where none is certified for residential work the owner is not required to make the submissions at all',
    },
    {
      no: 'OH.2',
      pages: '13 pages',
      title: 'Permit Application Checklist',
      copy: 'The approvals that apply wherever you build, every code edition actually in force, the eight Ohio amendments to the National Electrical Code, and the seven things Ohio changed in the residential code itself — including no sprinkler requirement, no radon provisions and no statewide frost depth.',
      thumb: '/kits/oh/ohk-checklist.webp',
      caption: 'OH.2 Why every source still says 2017',
      alt: 'Page 3 of OH.2: the table of code editions in force, above a box explaining that the Board of Building Standards files rules as redline PDFs so the National Electrical Code line prints as seventy dash seventeen struck through with twenty-three inserted, and that copying the line loses the strikethrough',
    },
    {
      no: 'OH.3',
      pages: '8 pages',
      title: 'Inspection Sequence',
      copy: 'Ohio names its inspections in the code and makes the official hand you the list. The one that happens before you move any dirt, the clause that makes framing wait for the trades, the four-day rule that lets you proceed anyway, and a log.',
    },
    {
      no: 'OH.4',
      pages: '8 pages',
      title: 'Where to File Directory',
      copy: 'Ohio publishes the answer to “does anybody permit my parcel?” as a searchable map. How to run it on your own address, what the statewide data shows, the 23 counties with no residential certification anywhere, and the offices that exist either way.',
      thumb: '/kits/oh/ohk-directory.webp',
      caption: 'OH.4 36 of 88 counties',
      alt: 'Page 2 of OH.4: a table counting residential against commercial certification across Ohio — 36 of 88 counties and 475 of 921 cities and villages residential-certified, against 64 and 656 commercial — above a paragraph explaining that the gap is the statutory asymmetry showing up in behavior',
    },
    {
      no: 'OH.5',
      pages: '7 pages',
      title: 'Forms & Documents Index',
      copy: 'Every document you will meet, named as the rules name it. The work Ohio exempts from approval outright, reproduced as the code lists it — including the four-part deck test — and the contract and lien paperwork that, as your own general contractor, has nobody to come from.',
    },
  ],

  includes: [
    '51 print-ready pages across 6 documents, letter size',
    'Every Ohio claim cited on the page it appears on',
    'Write-in lines for everything that varies by jurisdiction',
    'A permit record, an inspection log and a confirmed-offices page for the job site',
    'Lifetime access — re-download anytime with your purchase email',
  ],

  highlightsLead:
    'Four things Ohio law actually says that the standard advice gets wrong. Each takes about a minute to check.',

  highlights: [
    {
      icon: 'permit',
      label: 'The code itself tells you when to stop filing',
      copy: 'Most states leave you to infer that nobody enforces. Ohio writes it down twice. RCO section 101.5: where no building department “is certified by the Board of Building Standards for residential buildings… the owner is not required to make submission of construction documents, seek approvals, request inspections, or obtain certificates of occupancy.” And § 3791.04(A)(1) says the same in statute — with an asymmetry that gives the game away. If nobody local is certified for a warehouse, your plans go to the state. If nobody is certified for your house, they go nowhere. Ohio built a backstop for commercial work and deliberately did not build one for houses.',
    },
    {
      icon: 'doc',
      label: '23 counties have no residential certification at all',
      copy: 'Certification is applied for, not imposed — § 3781.10(E)(10) treats cities, townships and counties as identical voluntary applicants, and § 3781.10(E)(3) forbids the Board from requiring it of a department that does not enforce the residential code. Counted from the Board’s own published dataset in September 2026: 36 of 88 counties hold county-wide residential certification, and in 23 counties no county, municipality or township holds it anywhere. Meanwhile 64 counties are certified for commercial work — so a staffed building department with a counter is no answer to the residential question.',
    },
    {
      icon: 'bolt',
      label: 'Ohio moved to the 2023 NEC and almost nobody noticed',
      copy: 'The Board files rules as redline PDFs, so the referenced-standards line prints as “70—17 23” with the 17 struck through and 23 inserted. Copy that line and the strikethrough vanishes; what comes out is “1723,” which careful writers resolve to 2017. It has been the 2023 National Electrical Code since 15 April 2024 (OAC 4101:8-34-01 and 4101:8-44-01), incorporated whole with eight Ohio amendments — including one that turns the 2023 code’s mandatory whole-house surge protection into a conditional, and one exempting listed outdoor HVAC equipment from GFCI. The energy standard, on the facing page of the same rule, is unstruck and still the 2018 IECC.',
    },
    {
      icon: 'check',
      label: 'The state trade licenses do not reach your house',
      copy: 'Ohio licenses electrical, plumbing, HVAC, refrigeration and hydronics contractors — and none of it applies to a one-, two-, or three-family dwelling. Follow four definitions: § 4740.13(A) bars acting as “a type of contractor that this chapter licenses”; § 4740.01(A) names the five trades; § 4740.01(F) defines “construction project” to exclude “a residential building as defined in section 3781.06”; and § 3781.06(C)(9) defines that as a one-, two-, or three-family dwelling house. The licensing board says so itself: it regulates commercial contractors, and “all local building and health departments regulate residential contractors.” The rule you need is local, not state.',
    },
  ],

  sourceNote:
    'Every claim was read against its primary source in September 2026: the Ohio Revised Code and Ohio Administrative Code at codes.ohio.gov, including the Board of Building Standards’ own rule PDFs as filed with the Legislative Service Commission and read as rendered pages rather than extracted text; the Board’s published certified-jurisdiction dataset; the Ohio Department of Health’s sewage and private water chapters; and Ohio EPA’s construction stormwater general permit.',

  faqs: [
    {
      question: 'Can you build your own house in Ohio without a license?',
      answer:
        'Yes, and Ohio is unusual in that there is no licensing exemption to claim — because there is no license. Ohio issues no state general contractor or homebuilder license of any kind; its own advisory-committee statute at § 4740.14 refers to “general contractors” as a real trade while licensing none of them. That also means there is no state owner-builder affidavit, no exemption form, no annual cap on houses and no holding period, because those are conditions states attach to an exemption Ohio never needed to write. What you do still need is whatever your local jurisdiction requires: § 4740.12(B) expressly preserves local ordinances that regulate the trades or require registration of tradespersons, and cities commonly have both a general-contractor registration and a trade registration on top of it.',
    },
    {
      question: 'Do you need a building permit to build a house in Ohio?',
      answer:
        'Only if a building department certified for residential buildings has jurisdiction over your parcel — and in much of Ohio none does. The Residential Code of Ohio says so in its own text at section 101.5, and Revised Code § 3791.04(A)(1)(b) repeats it: where no certified residential department has jurisdiction, “the owner is not required to make the submissions.” Counted from the Board of Building Standards’ dataset in September 2026, 36 of Ohio’s 88 counties hold county-wide residential certification, and in 23 counties nothing inside the county holds it. But “no building permit” is not “no paperwork”: the sewage treatment system permit and the private water system permit come from your local health district under statewide rules, plumbing enforcement runs on its own statutory track, and zoning, floodplain and driveway permits are separate authorities again.',
    },
    {
      question: 'Do I need a licensed electrician or plumber for my own house in Ohio?',
      answer:
        'Not as a matter of state law, which surprises nearly everyone. Ohio’s five trade licenses reach only a “construction project,” and § 4740.01(F) defines that term to exclude “a residential building as defined in section 3781.06” — which § 3781.06(C)(9) defines as a one-, two-, or three-family dwelling house. The Ohio Construction Industry Licensing Board describes its own remit the same way: it regulates commercial contractors, and “all local building and health departments regulate residential contractors.” So the state license is a commercial license. Your city or township may absolutely still require its own registration or license for work on a house, and § 4740.12(B) preserves that power expressly — ask your jurisdiction and comply with what it says. Nothing here changes the code your wiring has to meet.',
    },
    {
      question: 'Which electrical code does Ohio use in 2026 — the 2017 or 2023 NEC?',
      answer:
        'The 2023 National Electrical Code, since 15 April 2024, and the widespread “2017” answer is a formatting artifact worth understanding. The Board of Building Standards publishes rules as PDFs of the amendment, with deleted text struck through and new text underlined on the same line, so the referenced-standards entry prints as “70—17 23” with the 17 crossed out. Any text extraction flattens that to “70—1723,” which reads as 2017 because 17 comes first. Read the rule as a rendered page — OAC 4101:8-44-01, page 31 — and the strikethrough is plain. Ohio incorporates NFPA 70 wholesale under OAC 4101:8-34-01 and applies eight amendments, notably rewriting the 2023 code’s mandatory whole-house surge protection to apply only “where provided” and exempting listed outdoor HVAC equipment from GFCI. On page 29 of the same rule the energy standard reads IECC—18 with no strikethrough, so residential energy is still the 2018 IECC.',
    },
    {
      question: 'What is the frost depth for footings in Ohio?',
      answer:
        'There is no statewide Ohio frost depth, and any source that gives you one is quoting something that is not in the code. The Residential Code of Ohio’s climatic design table leaves the frost-line cell blank on purpose — footnote b reads “The jurisdiction shall fill in the frost line depth column with the minimum depth of footing below finish grade,” and ground snow load and seismic design category are blank for the same reason. The only statewide floor is section 403.1.4: exterior footings not less than 12 inches below the undisturbed ground surface, then extended below whatever frost line your jurisdiction has filled in. Get that number from your building department in writing; where no department is certified there is no published figure and you should design to documented local practice. One trap worth knowing: the March 2024 Foundations amendment deleted the model code’s frost exemptions for freestanding accessory structures, so a detached pole barn needs frost-depth footings in Ohio.',
    },
    {
      question: 'Who issues septic and well permits in Ohio?',
      answer:
        'Your local board of health, statewide, whether or not any building department exists — which is why on a rural Ohio build the health district is the office that matters most. Sewage treatment systems run under OAC Chapter 3701-29, in force since 1 January 2015, and private water systems under OAC Chapter 3701-28, in force since 1 January 2020, and boards of health may adopt more stringent rules than the state floor. Two things owner-builders routinely get wrong: you cannot perform your own soil evaluation — it takes a certified soil scientist, an equivalently registered soil professional, or the district’s own registered sanitarian — and there is no blanket homeowner exemption for installing your own system. OAC 3701-29-03(H) lets the board waive the fee, the liability insurance and the surety bond for a registrant working on their own home, but the subject of that sentence is “the registered installer,” so you must register first, and the state testing requirement is not on the waiver list. Drilling your own well is similar: allowed, but only after registering with the Department of Health, and the surety bond still applies.',
    },
  ],

  productDescription:
    'A 51-page print-ready permit kit for building your own home in Ohio, in six documents. Covers the sentence in the Residential Code of Ohio that excuses an owner from plans, approvals, inspections and a certificate of occupancy where no certified residential building department has jurisdiction — and the statute that says the same thing while giving commercial work a state backstop houses never got; the Board of Building Standards’ address lookup and what its published data shows, including the 23 counties with no residential certification anywhere; the four-link definition chain that places a one-, two-, or three-family dwelling outside Ohio’s trade licenses; the move to the 2023 National Electrical Code and the redline formatting that keeps the 2017 answer in circulation; Ohio’s own amendments to the residential code, including no sprinkler requirement, no radon provisions, no statewide frost depth and a steeper stair than the model code allows; the sewage and private water permits that run through your health district regardless; and the lien rule that means an owner cannot be made to pay twice. Every claim is cited on the page it appears on and was verified against the Ohio Revised Code, the Ohio Administrative Code and the Board’s own filed rule text in September 2026.',

  verifyNote:
    'Statutes, rules and code editions change, and Ohio has one answer moving right now: the commercial building code and the plumbing code both advanced to 2021 model codes in October 2025 while the residential code remains on the 2018 IRC, so a new edition is plausible. Certification status also changes — a city, township or county can apply at any time, so re-run the Board of Building Standards lookup for your own address before each phase. Confirm each rule with the office that will handle your parcel: your building department if one is certified, and separately your health district for sewage and private water. The kit prints its sources so you can.',

  binderLead:
    'The Owner-Builder Job Site Binder picks up where the permit kit stops — and in Ohio, where a certified department may never look at your house, the record you keep is the only evidence the house was built to a standard. 367 pages of contracts, inspection forms, daily logs and budget trackers covering every phase from footing to final, in the same print-and-go format.',
};

export default function OHPermitKit() {
  return <KitProductPage content={OH} />;
}
