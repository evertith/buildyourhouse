/**
 * Editorial lender directory for /financing.
 *
 * Facts verified against the lenders’ public pages in September 2026 — state
 * footprints and terms change, so entries describe what each lender
 * ADVERTISES and the page tells readers to verify. Nobody here pays us
 * today; if a sponsorship ever exists it runs through FEATURED_LENDER
 * below and renders with a visible "Sponsored" label (and rel="sponsored").
 *
 * RESPA note (see lender-outreach/target-lenders.md): keep placements
 * flat-fee advertising or compliance-approved lead-gen; never present a
 * listing as an endorsement in exchange for per-closing fees.
 */

export interface LenderEntry {
  id: string;
  name: string;
  kind: 'Owner-builder specialist' | 'Regional lender';
  url: string;
  /** Display string, hedged to what the lender advertises. */
  states: string;
  /** What they advertise, in our words — no endorsement. */
  notes: string;
}

export const LENDERS: LenderEntry[] = [
  {
    id: 'owner-builder-loans',
    name: 'Owner Builder Loans, LLC',
    kind: 'Owner-builder specialist',
    url: 'https://www.ownerbuilderloans.com/',
    states: 'AZ · CA · CO · FL · GA · MI · NC · SC · TX',
    notes:
    'Owner-builder construction loans are their entire business — no general contractor or project supervisor required. Advertises 12-month interest-only terms, unlimited draws with no draw fees, and land equity counting toward the down payment. Says construction loans are not available in every state it is licensed in, so confirm your state before you plan around it.',
  },
  {
    id: 'normandy',
    name: 'Normandy Corporation',
    kind: 'Owner-builder specialist',
    url: 'https://normandy.com/self-build-owner-build-loans/',
    states: 'CA · CT · DE · FL · IA · MA · MI · NC · NJ · NY · OR · RI · VA · WA',
    notes:
    'Licensed mortgage banker with a dedicated self-build / owner-build program for borrowers acting as their own GC — no site supervisor and no general contractor on the payroll. Advertises up to 90% loan-to-cost on conforming amounts, with jumbo programs up to 80%. The state list above is their owner-occupied footprint; they lend in more states for non-owner-occupied projects.',
  },
  {
    id: 'first-summit-bank',
    name: '1ST SUMMIT BANK',
    kind: 'Regional lender',
    url: 'https://www.1stsummit.bank/home/personal/loans/mortgages/',
    states: 'PA (Cambria, Somerset, Indiana, Westmoreland and Blair counties)',
    notes:
    'Johnstown-area bank that calls construction loans its specialty and says it will work with you “whether you are self-building or using a contractor” — the self-build path named in the same breath as the contractor one rather than buried in a footnote. Advertises an exclusive one-time closing on construction mortgages, with no second close and no repeat closing costs. Its own locations page puts all 17 community offices across five Pennsylvania counties, so confirm your lot falls inside that footprint before planning around it.',
  },
  {
    id: '802-credit-union',
    name: '802 Credit Union',
    kind: 'Regional lender',
    url: 'https://www.802cu.com/loans/mortgages/construction/',
    states: 'VT · NH',
    notes:
    'Vermont credit union that prices self-building as its own product: the construction loan table lists a "Self-Build" option sitting alongside a "with General Contractor" option, which is about as affirmative as a rate sheet gets — a lender that will not finance owner-builders does not build them a separate line item. Advertises interest-only payments for up to twelve months during construction and automatic conversion into a permanent mortgage with no second closing. Read the surrounding copy with clear eyes: the same page still tells you to "Work with a licensed, reputable builder", so expect to make your case for managing the build yourself. Membership required.',
  },
  {
    id: 'agcountry',
    name: 'AgCountry Farm Credit Services',
    kind: 'Regional lender',
    url: 'https://www.agcountry.com/financing/rural-home-loans',
    states: 'MN · ND · WI (parts of each)',
    notes:
    'Farm Credit association lending through the Rural 1st brand, whose home-loan FAQ answers the question directly: choosing a contractor is your decision, and with experience and well-documented plans "you can even be your own self-contractor" — footnoted as subject to restrictions, so treat it as a conversation to have early rather than a published program. Advertises construction-to-permanent financing in one package with no refinance at completion, and lets the land you are building on count toward the down payment rather than just the dwelling value. Serves parts of Minnesota, North Dakota and Wisconsin, so the county matters as much as the state.',
  },
  {
    id: 'america-first',
    name: 'America First Credit Union',
    kind: 'Regional lender',
    url: 'https://www.americafirst.com/loans/mortgage-loans/construction-lot-loans.html',
    states: 'AZ · ID · NV · NM · UT',
    notes:
    'Advertises "Contractor-Built" and "Self-Built" construction loans side by side, and the paperwork is where the difference shows: the contractor version asks for a builder contract and a copy of the builder’s license, while the self-built version asks for a "self-build qualification" instead. Self-built advertises up to 80% of acquisition cost on a nine-month term with extensions available; the contractor version advertises up to 95% on twelve months. Says the program is available in Arizona, Idaho, Nevada, New Mexico and Utah, and that this is member-direct lending only — so you join first and the credit union underwrites you directly.',
  },
  {
    id: 'andrew-johnson-bank',
    name: 'Andrew Johnson Bank',
    kind: 'Regional lender',
    url: 'https://www.andrewjohnsonbank.com/building-your-dream-home-what-you-need-to-know-about-construction-to-permanent-loans',
    states: 'TN (East Tennessee)',
    notes:
    'East Tennessee community bank whose construction-to-permanent FAQ answers the question most lenders dodge: "No approved-list requirement. You choose your contractor." It goes on to say the loan "may give you the flexibility to serve as your own contractor" — whether you are managing the project yourself or bringing in your own subcontractors. Advertises one closing with the rate locked before ground is broken, interest-only payments on what has been drawn, a build period usually structured at 12 months, land you already own counting toward equity, and loans reviewed and approved locally. Note the hedge — the page says "may" — so confirm owner-builder eligibility for your specific project before you plan around it.',
  },
  {
    id: 'bank-of-utah',
    name: 'Bank of Utah',
    kind: 'Regional lender',
    url: 'https://www.bankofutah.com/home-loans/loan-options/home-construction-loan',
    states: 'UT',
    notes:
    'Puts owner-builders in the opening sentence — its new-home construction loans are for "those of you working with a contractor and those of you building your own home as an owner-builder". Advertises no payments due during construction, with the interest drawn from an interest reserve account built into the loan, and keeps one loan officer on both the construction loan and the long-term mortgage so there is no handoff at completion. Down payment and loan-to-value requirements are tiered by the finished value of the house, so the leverage you are quoted depends on where your project lands in that table.',
  },
  {
    id: 'bath-state-bank',
    name: 'Bath State Bank',
    kind: 'Regional lender',
    url: 'https://www.bathstatebank.com/mortgage/construction',
    states: 'IN (southeastern)',
    notes:
    'Small southeastern Indiana bank that states it plainly: "We allow the borrower to act as their own general contractor." Advertises 12 months to build and complete the home, an unlimited number of draws, 80% loan-to-value, no minimum loan amount, and inspections completed by an in-house inspector rather than a third party. Its lending offices are in Bath, Liberty and West College Corner, so this is a genuinely local footprint.',
  },
  {
    id: 'beehive-fcu',
    name: 'Beehive Federal Credit Union',
    kind: 'Regional lender',
    url: 'https://beehive.org/construction/',
    states: 'ID (plus Logan, UT and Afton, WY)',
    notes:
    'Idaho credit union that lists "Owner-Builder Projects" among the things its construction loans are for, and says plainly that it offers "both traditional construction loans and owner-builder loans, so you can choose what fits your project and timeline". Financing is open to borrowers "working with a contractor or building on your own". Advertises a 12-month construction term with interest-only monthly payments, up to two draws a month, and a refund of some closing fees if the loan is paid off early. The owner-builder option is footnoted "for qualified members", so expect the credit union to want evidence you can run the job.',
  },
  {
    id: 'cfsbank',
    name: 'cfsbank',
    kind: 'Regional lender',
    url: 'https://cfsbank.bank/personal-banking/loans/new-construction-mortgage/',
    states: 'PA (southwestern — Washington, Fayette, Westmoreland and Butler county offices)',
    notes:
    'Community bank whose Owner Builder Mortgage opens with the line owner-builders are looking for: “You are your own contractor.” Advertises that lot and/or labor equity can count toward the down payment, twelve months to build, interest-only payments during construction, approved construction bills and invoices paid weekly, and a single closing rather than a construction loan you refinance later. The footprint is southwestern Pennsylvania only — every office it lists is in state.',
  },
  {
    id: 'compeer-home',
    name: 'Compeer Home (Compeer Financial)',
    kind: 'Regional lender',
    url: 'https://www.compeerhome.com/loans/construction-loans/',
    states: 'MN · WI · IL (144 rural counties)',
    notes:
    'Farm Credit cooperative that meets the question head on: "Not all lenders allow clients to serve as their own general contractor, but at Compeer Home, your rural home and land lending experts, we do." Advertises acting as your own general contractor as a headline way to control the budget, on a one-time-close construction-to-permanent loan — rate locked up front, interest charged only on funds drawn, and the loan converting automatically when the build finishes. The catch is geographic, not procedural: it lends across 144 counties in Minnesota, Wisconsin and Illinois and the whole program is aimed at rural and small-town property, so confirm your parcel is inside the footprint before you plan around it.',
  },
  {
    id: 'country-bank-ma',
    name: 'Country Bank',
    kind: 'Regional lender',
    url: 'https://www.countrybank.com/construction-loan/',
    states: 'MA',
    notes:
    'Massachusetts community bank that says it in one line — "Country Bank also allows you to be your own general contractor" — and then prices it in the footnote: up to 90% of appraised value if you use a licensed general contractor, up to 80% of final value if you are your own. Advertises interest-only payments during the first twelve months and a choice of fixed or adjustable rate. That ten-point leverage gap is the honest cost of self-contracting here, so build the down payment plan around the 80% number rather than the headline one.',
  },
  {
    id: 'country-living-loans',
    name: 'Country Living Loans (Farm Credit East)',
    kind: 'Regional lender',
    url: 'https://www.countrylivingloans.com/en/country-living-loans/home-construction-loans',
    states: 'CT · MA · ME · NH · NJ · NY · RI · VT',
    notes:
    'Farm Credit East’s country-home brand, and one of the few Farm Credit programs anywhere that answers the owner-builder question in writing: "We can work with a builder/general contractor for your home construction projects, or a self general contractor where you manage the project yourself." Advertises a single-closing construction-to-permanent loan for country homes, farms and land across eight Northeast states. One wrinkle worth knowing before you call: Farm Credit East’s own rural home lending page says nothing about who may build — the self-contracting language lives on the Country Living Loans site, so quote that page when you ask.',
  },
  {
    id: 'cu-hawaii-fcu',
    name: 'CU Hawaii Federal Credit Union',
    kind: 'Regional lender',
    url: 'https://www.cuhawaii.com/personal/home-real-estate-loans/construction-loan.html',
    states: 'HI (Island of Hawaiʻi)',
    notes:
    'Big Island credit union that prices owner-builders as a standing product rather than an exception: its construction loan table lists "Construction – Owner Builder" right next to "Construction – Contractor," and both are advertised at up to 80% loan-to-value, where investors get 70%. Advertises a one-year construction period with interest-only payments and staged draws as work is completed, converting to a 30-year first mortgage, plus a balloon variant running 180 months on a 360-month amortization. Membership is community-chartered to the Island of Hawaiʻi — you qualify by living, working, worshipping, volunteering or going to school there, and you keep it for life once you join.',
  },
  {
    id: 'farm-credit-virginias',
    name: 'Farm Credit of the Virginias',
    kind: 'Regional lender',
    url: 'https://www.farmcreditofvirginias.com/loans/construction-loans/',
    states: 'VA · WV',
    notes:
    'One of the few Farm Credit associations that puts owner-builders in writing — its construction page advertises allowances for owner and self-builds, with customer-managed builds carrying extra documentation and credit requirements. Interest-only during construction with scheduled draws and inspections, across a 96-county rural service area.',
  },
  {
    id: 'farm-credit-services-of-america',
    name: 'Farm Credit Services of America (Rural 1st)',
    kind: 'Regional lender',
    url: 'https://www.fcsamerica.com/financing/rural-home-loans',
    states: 'IA · NE · SD · WY',
    notes:
    'Farm Credit association whose Rural 1st home-loan FAQ answers the question without hedging: "Choosing a contractor is your decision, and Rural 1st will work with your choice. If you have experience and well-documented plans, you can even be your own self-contractor." That last sentence carries a "subject to restrictions" footnote, so ask what the restrictions are before you plan around it. Advertises construction-to-permanent in a single package with no refinance at completion, the land you are building on counting as equity toward the down payment, and a full year to finish rather than the six-month window it says many lenders impose. Serves rural borrowers from 42 offices across Iowa, Nebraska, South Dakota and Wyoming.',
  },
  {
    id: 'farmers-state-bank-oh',
    name: 'Farmers State Bank',
    kind: 'Regional lender',
    url: 'https://www.farmersstate-oh.com/home-mortgage-loans/construction',
    states: 'OH',
    notes:
    'Ohio community bank that names the product outright: "If you plan to build a residential home and act as the general contractor, you can use a self-build construction loan" — described as a specialty loan giving you greater control over the building process. Advertises an application process open at any hour, building plans and specifications reviewed during approval, and permanent financing applied for separately once construction finishes, so plan for a two-step close rather than a one-time close.',
  },
  {
    id: 'first-bank-of-manhattan',
    name: 'First Bank of Manhattan',
    kind: 'Regional lender',
    url: 'https://www.fnbmanhattan.com/personal/lending/construction-and-lot-loans',
    states: 'IL (Will County — Manhattan · New Lenox)',
    notes:
    'Small Will County bank whose construction page puts both paths on equal footing — "whether you decide to oversee the work yourself or hire a general contractor" — and then backs it up in the mechanics, describing draws issued by working with "you or your builder" and the title company. Advertises short-term fixed-rate construction loans with interest-only payments during the build, construction-to-permanent financing to save a second set of closing costs, and separate lot loans for undeveloped land you are not ready to build on yet. Two branches, so this is a local option rather than a statewide one.',
  },
  {
    id: 'first-farmers-bank-trust',
    name: 'First Farmers Bank & Trust',
    kind: 'Regional lender',
    url: 'https://www.ffbt.com/mortgage/apply-online',
    states: 'IN · IL',
    notes:
    'Indiana agricultural bank whose mortgage page advertises "owner and self-build construction options" alongside flexible loan amounts, straightforward disbursements and interest-only payments during the build — "There’s no place like home – especially when you’re the builder." Its footer gives the footprint as Indiana and Illinois, and it says mortgages are approved and serviced locally. The owner-build allowance is one line rather than a documented program, so get the requirements in writing early.',
  },
  {
    id: 'first-federal-kansas-city-barndo',
    name: 'First Federal Bank of Kansas City — Barndo Loan Program',
    kind: 'Regional lender',
    url: 'https://ffbkc.com/borrow/build-a-home/barndominium-financing/',
    states: 'Contiguous US (excludes AK · HI · NY)',
    notes:
    'A barndominium-only program with an unusually wide door: the bank advertises financing post-frame, steel-frame and stick-built barndo-style homes anywhere in the contiguous United States, and lists "acting as your own general contractor" as one of the ways to save on build cost — footnoted as available except in Texas. Advertises paying off an existing land loan, interest-only payments through the first 12 months, and living on site while you build. Two limits to be clear about: it only applies to barndo-style homes, and the bank\'s ordinary construction-to-permanent loan is a different, builder-based product limited to roughly 50 miles around Kansas City.',
  },
  {
    id: 'first-federal-lorain',
    name: 'First Federal Savings and Loan Association of Lorain',
    kind: 'Regional lender',
    url: 'https://www.fflorain.bank/personal/lending-products/construction-loan',
    states: 'OH (northern Ohio)',
    notes:
    'Northern Ohio thrift that leads its construction loan page with the heading "Act as your own General Contractor" — "You have the dream, the plan, and the ability." Advertises a single-close loan with one set of closing costs that converts automatically to permanent financing, fixed and adjustable rates, a six-draw schedule with additional draws available for a fee, lot equity counting toward the down payment, and lots up to 25 acres.',
  },
  {
    id: 'first-national-bank-alaska',
    name: 'First National Bank Alaska',
    kind: 'Regional lender',
    url: 'https://www.fnbalaska.com/personal/home-construction-loans/',
    states: 'AK',
    notes:
    'Statewide Alaska bank, in business since 1922, whose entire home-construction page is built around owner-builders — it defines the product as a loan “in which the borrower takes on the role of the home builder.” Advertises a builder’s resume, cost breakdown, construction schedule, spec sheet and supplier/subcontractor list as the documents that open the file, with a minimum 25% of total construction cost in cash or land equity plus a 10% contingency for overruns. Draws are released against percentage of completion with monthly site inspections, and the bank says it can pay your subs and suppliers directly. Note the Alaska-specific catch it states outright: every home has to meet AHFC’s New Construction Building and Energy Efficiency Requirements.',
  },
  {
    id: 'fulton-savings',
    name: 'Fulton Savings Bank',
    kind: 'Regional lender',
    url: 'https://www.fultonsavings.com/mortgage-loan-process/',
    states: 'NY (central — Oswego and Onondaga county offices)',
    notes:
    'Central New York savings bank that answers the question outright in its mortgage FAQ: “Can I get a construction loan and build my own home? YES … If you have the skills to build your home or act as the General Contractor you may do so.” Calls itself the local leader in self-build construction and renovation. Advertises rolling land and construction costs into a single loan with one closing, and draw schedules it describes as common-sense — worth asking about specifically, since draw rigidity is what usually bites owner-builders.',
  },
  {
    id: 'goldenwest',
    name: 'Goldenwest Credit Union',
    kind: 'Regional lender',
    url: 'https://www.gwcu.org/borrow/home-loans/construction-loans',
    states: 'UT · ID',
    notes:
    'Lists "Owner Builder or Contractor Builder" as a headline benefit and then splits the two into separate offers. The owner-builder side is aimed at borrowers who "can demonstrate qualified self-build experience" and advertises up to 85% financing with one-time-close and two-time-close options; the contractor side advertises up to 90%. You have to hand in an owner-builder letter setting out your building experience, so this is a program for someone with a track record rather than a first-timer. Branch network is concentrated in Utah with a handful of Idaho locations.',
  },
  {
    id: 'greenstone',
    name: 'GreenStone Farm Credit Services',
    kind: 'Regional lender',
    url: 'https://www.greenstonefcs.com/loans/home-land-loans/home-construction-loans/',
    states: 'MI · northeast WI',
    notes:
    'Farm Credit cooperative that says it plainly: "You can use a licensed builder, do it yourself, or opt for a combination of both." Advertises a one-time close with interest-only payments during the build rolling straight into the end mortgage, direct-deposit draws, and as little as 5% down with PMI. Builder’s risk insurance is required and the budget has to be adequate.',
  },
  {
    id: 'guardian-credit-union',
    name: 'Guardian Credit Union',
    kind: 'Regional lender',
    url: 'https://www.myguardiancu.com/home-loans/build/construction',
    states: 'AL (central)',
    notes:
    'The only Alabama lender found that answers the question at all. Its construction FAQ asks "Can I Use a Construction Loan for a Self-Build?" and answers "Yes, you can! We offer construction loans for self-build projects, but eligibility depends on your specific situation." Treat that as an opening, not a program — it is a conditional yes with no published owner-builder terms behind it, and another FAQ on the same page assumes "your builder will submit draw requests". Advertises up to 90% financing, a fixed rate with interest-only payments during construction, draws advanced after work is completed and inspected, and a 12-month term on most projects with extensions possible. Membership runs to central Alabama counties.',
  },
  {
    id: 'gulf-coast-bank-trust',
    name: 'Gulf Coast Bank & Trust',
    kind: 'Regional lender',
    url: 'https://www.gulfbank.com/construction-loans',
    states: 'LA',
    notes:
    'Advertises that "Self-build permitted (subject to additional approval and requirements.)" — but read which product that attaches to, because the same page says "Self-build/self-contract not allowed on OTC loans." Owner-builders are steered away from the one-time-close product and onto the two-close path, which advertises an 18-month required loan term and interest-only payments on drawn funds during construction. Advertises a staged draw schedule of typically five to seven disbursements, from foundation through framing, mechanicals, cabinetry and finishes to certificate of occupancy.',
  },
  {
    id: 'hawaii-central-fcu',
    name: 'Hawaii Central Federal Credit Union',
    kind: 'Regional lender',
    url: 'https://hawaiicentral.org/rates/construction-loans/',
    states: 'HI',
    notes:
    'Honolulu credit union that takes the question head-on: "Whether you already have a contractor lined up or plan to be your own contractor, our Construction Loans can fit your specific needs." It goes further than almost anyone else on this page — "although a bonded contractor is recommended, it is not required" — and names "Owner/Builder" alongside contractors as who it lends to. Advertises interest-only payments with accrued interest payable at each draw, a maximum credit line of $900,000 and up to 80% loan-to-value, on one- and two-year construction terms. Membership comes first, and the owner-builder language sits on a rates page rather than a product page, so confirm the program still reads that way when you call.',
  },
  {
    id: 'home-bank',
    name: 'Home Bank',
    kind: 'Regional lender',
    url: 'https://www.home24bank.com/personal/home-loans/construction.html',
    states: 'LA · MS · TX',
    notes:
    'Rare among community banks: it prices self-contracting as a published tier rather than treating it as an exception. Advertises "New Construction with Self-contracting - up to 80% LTV" directly alongside "New Construction with Builder contract - up to 90% LTV" — so acting as your own contractor is on the rate sheet, and it costs you ten points of leverage. Advertises a single closing, fixed or adjustable options with a possible rate reduction at completion if rates have fallen, and the appraised value of a lot you already own counting toward the equity requirement. The construction page does not break availability out by state, so confirm your market.',
  },
  {
    id: 'kalamazoo-county-state-bank',
    name: 'Kalamazoo County State Bank',
    kind: 'Regional lender',
    url: 'https://kcsbank.com/construction-loan/',
    states: 'MI (southwest)',
    notes:
    'Southwest Michigan community bank that lists "Self-Contracting Builds" as a construction loan use case and describes itself as one of the few banks financing owner-builders. Advertises letting you work with a builder, do some of the work yourself, or self-contract the entire project — including sweat equity on trades like drywall, electrical, plumbing, flooring and trim.',
  },
  {
    id: 'norway-savings-bank',
    name: 'Norway Savings Bank',
    kind: 'Regional lender',
    url: 'https://www.norwaysavings.bank/construction-land-loan/',
    states: 'ME · NH (Coos & Carroll counties)',
    notes:
    'The one Maine bank found that puts it in the feature list rather than the fine print: "Option to act as your own General Contractor," repeated in its own explainer, where it says you can "even act as your own general contractor if you wish." Advertises up to 85% of building acquisition cost or appraised value, whichever is less, and up to 12 months of construction phase sized deliberately to the Northern New England building season, with servicing kept local. Covers stick-built customs, modular and manufactured homes, seasonal and lake properties, and single-close construction-to-permanent. Worth knowing this is the exception in Maine, not the norm — several of its neighbors require an approved general contractor outright.',
  },
  {
    id: 'olympia-federal',
    name: 'Olympia Federal Savings',
    kind: 'Regional lender',
    url: 'https://www.olyfed.com/home/construction/',
    states: 'WA (South Sound)',
    notes:
    'South Sound mutual savings bank that advertises taking either kind of project — "whether you’re going to do it yourself or work with a builder". Advertises all-in-one construction-to-permanent financing closed up front so there is no refinance at completion, no risk-based pricing, and human underwriting rather than automated. Read the fine print on leverage: the advertised 95% loan-to-cost applies to owner-occupied homes built with a licensed contractor.',
  },
  {
    id: 'planters-bank-trust',
    name: 'Planters Bank & Trust',
    kind: 'Regional lender',
    url: 'https://www.plantersbankonline.com/lending/mortgages',
    states: 'KY · TN (Clarksville)',
    notes:
    'Kentucky community bank with four Clarksville, Tennessee branches whose mortgage page draws the distinction that matters: "If you are building your own home or employing a custom home builder, Planters Bank will help you set up a Construction Loan." Advertises a loan that runs through the construction period with draws taken for construction payments and payments that are often interest-only. It also offers Tennessee Housing Development Agency mortgages for property financed in Tennessee, which is useful corroboration that the Tennessee side of the footprint is real rather than incidental.',
  },
  {
    id: 'sherwood-community-bank',
    name: 'Sherwood Community Bank',
    kind: 'Regional lender',
    url: 'https://www.sherwoodbank.com/loans--mortgages/construction',
    states: 'MO (Cass County — Creighton · Harrisonville)',
    notes:
    'Two-branch bank south of Kansas City that names "owner-builder construction loan" outright as one of the construction programs it offers, alongside construction-only, renovation and rehab loans. The listing is a single line with no program detail behind it, so treat this as a door that is open rather than a program you can compare on paper — everything past the name has to come from the lender. Advertises the usual community-bank construction structure around it: roughly a 12-month term, periodic draws released against completed milestones, interest paid on drawn funds, and conversion to a permanent mortgage at completion.',
  },
  {
    id: 'spirit-of-alaska-fcu',
    name: 'Spirit of Alaska Federal Credit Union',
    kind: 'Regional lender',
    url: 'https://spiritofak.com/real-estate-loans/renovation-construction/',
    states: 'AK (Fairbanks area)',
    notes:
    'Fairbanks credit union that adopts the term as its own — it offers members the option to do the work themselves, "whom we term as owner-builders" — and spells out the choice plainly: "You can complete all the work yourself, hire a contractor, or do some of it and sub-contract out the rest." The same program covers buying land and building new, not only renovating. Advertises a construction program that opens in January and is designed around a one-year completion window because the Alaska building season is "a relatively small window," with draw requests accepted any day and draw checks processed twice a week, rolling into a fixed-rate mortgage at completion. It tells you to apply early in the year; on a one-season build, take that literally.',
  },
  {
    id: 'state-savings-bank-iowa',
    name: 'State Savings Bank',
    kind: 'Regional lender',
    url: 'https://www.ssb.bank/home-mortgage/home-construction-loans',
    states: 'IA (Baxter · West Des Moines)',
    notes:
    'Small central-Iowa bank whose construction FAQ asks and answers the question plainly: it "does allow individuals to work as their own GC as long as they have relevant construction experience," and says a resume or proof of previous houses built may be required. Read that gate honestly before you call — this is a bank that will finance a capable owner-builder, not a first-timer. Advertises interest-only payments on drawn funds, draws available up to twice a month, lien waivers and inspections at each draw, land equity counting toward the 20% down payment, and no second origination fee when the construction loan converts to permanent financing.',
  },
  {
    id: 'timberland-bank',
    name: 'Timberland Bank',
    kind: 'Regional lender',
    url: 'https://www.timberlandbank.com/lending/personal/construction-loan',
    states: 'WA',
    notes:
    'Washington community bank that advertises a named Owner-Builder program — "whether you hire a contractor or choose to build your own home" — with the owner-builder actively managing the project alongside a local lender. Advertises two-step construction financing at a maximum 80% loan-to-value, a 12-month construction term, interest-only payments during construction, and loan servicing kept in house.',
  },
  {
    id: 'tioga-state-bank',
    name: 'Tioga State Bank',
    kind: 'Regional lender',
    url: 'https://www.tiogabank.com/construction-loan-contact/',
    states: 'NY (Southern Tier — Owego, Vestal, Binghamton, Ithaca)',
    notes:
    'Southern Tier community bank that advertises “Allows you to do self builds” and says that “in some instances, we will allow you to be your own general contractor.” Read that hedge exactly as written — the option is advertised, but the bank reserves the call, so establish early which side of the line your project sits on. Advertises one closing with up to 12 months of interest-only payments during the construction period and terms up to 30 years, and says it finances stick-built, modular, prefabricated, log and manufactured homes.',
  },
  {
    id: 'union-bank-vt',
    name: 'Union Bank (Vermont)',
    kind: 'Regional lender',
    url: 'https://www.ublocal.com/personal/personal-loans/construction/',
    states: 'VT · northern NH',
    notes:
    'Vermont community bank lending across Vermont and northern New Hampshire that puts an experience test in writing rather than a contractor requirement: "Borrowers with suitable experience can act as the general contractor or perform some—or all—of the construction." Advertises no minimum draw amounts, funds usually available in 24 to 48 hours, invoices paid directly from a construction-loan checking account, and a twelve-month term with a possible four-month renewal. Its mortgage-side construction page describes a two-close structure — build first, then refinance into the permanent loan once the home is finished — with a minimum 10% down payment that can run as high as 40% depending on loan size and project.',
  },
  {
    id: 'utah-first',
    name: 'Utah First Credit Union',
    kind: 'Regional lender',
    url: 'https://utahfirst.com/construction-loans/',
    states: 'UT',
    notes:
    'Asks "Contractor or DIY? We Fund Both!" and means it — the page offers loan options "whether you’ve got a licensed builder managing the project or you’re calling the shots with a toolbelt and a timeline". The documentation list makes the owner-builder route explicit by asking for "proof you can build", which it defines as either a self-build qualification or a builder’s license, and it treats the builder contract as conditional on your actually using one. Advertises terms up to 18 months with 30-year amortization and a one-time-close option that bundles the construction loan and the mortgage into a single closing.',
  },
  {
    id: 'walden-savings',
    name: 'Walden Savings Bank',
    kind: 'Regional lender',
    url: 'https://waldensavings.bank/mortgage-loan/construction-loan',
    states: 'NY (Hudson Valley)',
    notes:
    'Hudson Valley mutual savings bank that lists “Allows you to be the general contractor” as a plain feature of its construction loan rather than an exception you have to negotiate for — its longer write-up puts it as “Act as Your Own General Contractor … the flexibility to manage your own build.” Advertises a one-time closing, a free rate lock held up front through the build, up to 85% financing of the completed home’s value, no points required, and a construction period of up to 12 months. Says first-time buyers qualify.',
  },
];

/**
 * Sponsored placement config — the on-site half of a signed lender deal.
 * null = no deal = the slot renders nothing. When a deal closes, fill this
 * in and the slot renders with a visible "Sponsored" label.
 */
export interface FeaturedLender {
  name: string;
  url: string;
  states: string;
  pitch: string; // one honest sentence, approved by the lender
}

export const FEATURED_LENDER: FeaturedLender | null = null;

export const LENDERS_VERIFIED = 'September 2026';
