import type { Metadata } from 'next';
import BinderCTA from '@/components/BinderCTA';
import TrackedLink from '@/components/TrackedLink';
import Icon, { type IconName } from '@/components/Icon';
import { generateProductSchema, generateFAQSchema, schemaToScriptTag } from '@/lib/schema';
import styles from '../product.module.css';

// filled in after /admin/api/provision-products creates the payment link
const STRIPE_CHECKOUT = 'https://buy.stripe.com/7sYeVd5W7gNhdE0eZ5fAc04';
const SITE_URL = 'https://build-your-house.com';
const PRICE = 34;

export const metadata: Metadata = {
  alternates: { canonical: '/shop/ga-permit-kit' },
  title: 'Georgia Owner-Builder Permit Kit — $34',
  description:
    'Every permit, form, and inspection Georgia requires of an owner-builder: the O.C.G.A. § 43-41-17 exemption walkthrough with the 24-month one-sale rule, permit application checklist, inspection sequence, and where-to-file directory. 32 print-ready pages with the statute citations on the page. $34 instant download.',
  keywords:
    'Georgia owner builder permit, can I build my own house in Georgia, Georgia owner builder law, Georgia owner builder exemption, GA building permit checklist, OCGA 43-41-17, Georgia inspection sequence, Georgia notice of commencement, Georgia blower door test, Georgia energy code',
  openGraph: {
    images: ['/binder/og-shop.jpg'],
  },
};

type KitDoc = {
  no: string;
  pages: string;
  title: string;
  copy: string;
  thumb?: string;
  caption?: string;
  alt?: string;
};

const DOCS: KitDoc[] = [
  {
    no: 'GA.0',
    pages: '3 pages',
    title: 'Cover & How to Use',
    copy:
      'What is in the kit, what order to work through it, and Georgia’s headline facts — the exemption, the $2,500 licensing threshold, the January 2026 code stack, the two mandatory energy tests, the septic gate, and the statewide-codes twist — each with its citation.',
  },
  {
    no: 'GA.1',
    pages: '7 pages',
    title: 'Owner-Builder Exemption Walkthrough',
    copy:
      'The exemption, plain: your own land, your own occupancy, not for sale or lease — O.C.G.A. § 43-41-17(h) quoted on the page. The 24-month one-sale rule that poisons the exemption, measured from the sold structure’s certificate of occupancy. The no-delegation rule, the carve-outs for hiring licensed subs, and § 43-14-13(d), which lets you self-perform the trades in your own dwelling.',
    thumb: '/binder/gak-exempt.webp',
    caption: 'GA.1 Exemption walkthrough',
    alt: 'Page GA.1, the Owner-Builder Exemption Walkthrough: the O.C.G.A. § 43-41-17(h) exemption conditions and the 24-month one-sale rule, with the statute text quoted on the page.',
  },
  {
    no: 'GA.2',
    pages: '10 pages',
    title: 'Permit Application Checklist',
    copy:
      'Everything the county or city wants in the packet, in the order they ask for it: site plan, plans, the septic construction permit that gates all site work on an unsewered lot, the land-disturbance question, the Notice of Commencement, and the GDOT driveway permit on a state route. Check the boxes and you have a complete application.',
    thumb: '/binder/gak-checklist.webp',
    caption: 'GA.2 Application checklist',
    alt: 'Page GA.2, the Permit Application Checklist: ruled checklist rows with checkboxes and a date column for each application document.',
  },
  {
    no: 'GA.3',
    pages: '5 pages',
    title: 'Inspection Sequence',
    copy:
      'Georgia deletes the IRC’s administration chapter, so no statewide inspection list exists. The kit prints the model ladder — footing through final, with the two energy-test gates and the septic final — plus blanks for your county’s actual required list, and what changes in a county that inspects nothing.',
    thumb: '/binder/gak-inspect.webp',
    caption: 'GA.3 Inspection sequence',
    alt: 'Page GA.3, the Inspection Sequence: the Georgia inspection ladder in call order with prerequisites and write-in rows for the county’s own list.',
  },
  {
    no: 'GA.4',
    pages: '4 pages',
    title: 'Where-to-File Directory',
    copy:
      'Which office handles which piece: the local building department where one exists, the county health department for septic, EPD for stormwater, the GDOT district office for a state-route driveway, and the clerk of superior court for the Notice of Commencement. Plus eleven of Georgia’s busiest permit counters, domains confirmed.',
  },
  {
    no: 'GA.5',
    pages: '3 pages',
    title: 'Forms & Documents Index',
    copy:
      'Every form referenced in the kit, with its official title and the office that issues it — including the county septic application, the NPDES Notice of Intent, and the Notice of Commencement contents list — so you can pull a current copy yourself.',
  },
];

const INCLUDES: string[] = [
  '32 print-ready pages across 6 documents, letter size',
  'The owner-builder exemption walkthrough (O.C.G.A. § 43-41-17(h)), including the 24-month one-sale rule',
  'A permit application checklist you can work straight through',
  'The inspection sequence, with blanks for your county’s own required list',
  'Where-to-file directory: building, septic, stormwater, driveway, and the superior court clerk',
  'Statute and code citations printed on the page, not linked away',
  'Lifetime access — re-download anytime with your purchase email',
];

const KNOWS: { icon: IconName; label: string; copy: string }[] = [
  {
    icon: 'doc',
    label: 'One sale in 24 months poisons the exemption — and the clock starts at the CO',
    copy:
      'Georgia lets you build your own house without a license, but § 43-41-17(h) carries a look-back most guides never mention: if you — or your family, firm, or corporation — sold a structure you built without a licensed contractor within the prior 24 months, measured from the date that structure’s certificate of occupancy issued, not the sale date, you cannot use the exemption for the next build. The statute then presumes the new building was never intended solely for your own occupancy. The kit walks the rule sentence by sentence with the statute on the page.',
  },
  {
    icon: 'permit',
    label: 'The code binds you even if your county has no permit office',
    copy:
      'Permits and inspections are a local-option power in Georgia (§ 8-2-26(a)(4)) — some counties run no building department at all. But the eight mandatory state minimum codes apply statewide with no local adoption required (§ 8-2-25(a)), and § 43-41-17(h) separately requires exempt owners to build in conformity with them. “No one checks” and “no rules apply” are different sentences, and your lender and insurer know the difference. The kit covers what to do in a no-inspection county.',
  },
  {
    icon: 'bolt',
    label: 'A 2024 IRC sitting on a 2015-era energy code — with two mandatory tests',
    copy:
      'On January 1, 2026 Georgia adopted the 2024 I-Codes and the 2023 NEC, but the energy code stayed the 2015 IECC with the Georgia Supplements and Amendments. Two performance tests are mandatory anyway: a blower door under 5 ACH50, and a duct-leakage test at or under 6 cfm25 per 100 square feet — waived only when the ducts and air handlers sit entirely inside the envelope — both run by a certified DET verifier whose signed report goes to the code official. Guides that quote the raw I-Code editions get the whole stack wrong. The kit prints Georgia’s numbers and cites the amendment packets.',
  },
  {
    icon: 'check',
    label: 'The Notice of Commencement is your lien screen — file it in 15 days or lose it',
    copy:
      'Within 15 days of work physically commencing, § 44-14-361.5 has the owner file a Notice of Commencement with the clerk of superior court and post a copy on the project site. Filing activates the notice-to-contractor screen that cuts off hidden remote lien claimants — and the statute says failing to file renders the whole protection inapplicable. Most owner-builder guides never mention it. The kit puts it in the checklist with the statutory contents list.',
  },
];

type Faq = { question: string; answer: string };

const FAQS: Faq[] = [
  {
    question: 'Can I build my own house in Georgia?',
    answer:
      'Yes. O.C.G.A. § 43-41-17(h) lets you construct a building on land you own, intended upon completion solely for occupancy by you and your family, firm, or corporation — not for use by the general public and not offered for sale or lease — acting as your own contractor, personally providing direct supervision and management of all work not performed by licensed contractors. No license, at any project cost. Two strings attach: you cannot delegate that supervision to anyone unlicensed, and all the work must still conform to the state minimum codes and any local permitting and inspection requirements. The kit walks the conditions one at a time with the statute quoted on the page.',
  },
  {
    question: 'Do I need a license to build my own house in Georgia?',
    answer:
      'No — and it is worth knowing what you are being exempted from. Georgia’s residential contractor licensing attaches at just $2,500 of work (§ 43-41-2(9)), one of the lowest thresholds in the country, and unlicensed contracting is a misdemeanor with a $500 minimum fine (§ 43-41-12). The § 43-41-17(h) exemption switches that off for a house on your own land, for your own occupancy. Separately, § 43-14-13(d) lets you self-perform the electrical, plumbing, HVAC, and low-voltage work in a dwelling you own or occupy — but that carve-out is personal to you: anyone you hire for those trades must hold the statewide license § 43-14-8 requires.',
  },
  {
    question: 'What is Georgia’s owner-builder law?',
    answer:
      'The whole thing lives in one subsection: O.C.G.A. § 43-41-17(h). It sets the conditions — your land, your occupancy, not for sale or lease — plus the one-sale-per-24-months rule, the no-delegation rule, and the sentence that keeps the codes and local permitting requirements binding on exempt owners. Unlike North Carolina, the statute requires no state affidavit, but many Georgia counties require their own notarized owner-builder affidavit as local practice, so ask yours. One honesty note the kit prints rather than hides: its statute quotes trace to an O.C.G.A. mirror current through March 28, 2024 — none of the 2024–2025 session laws is reported to have touched the exemption text, but confirm the current language before you rely on a single sentence.',
  },
  {
    question: 'Can I sell a house I built myself in Georgia?',
    answer:
      'Carefully — this is where the exemption bites. The house must be intended, upon completion, solely for your own occupancy (or your family’s, firm’s, or corporation’s) and not offered for sale or lease — a spec house never qualifies. And § 43-41-17(h) adds a look-back: if you sold or transferred a structure you built without a licensed contractor within the prior 24 months — measured from the date that structure’s certificate of occupancy issued — you cannot claim the exemption for the next build, and the statute presumes the new building was never intended solely for your occupancy. A sale by your family, firm, or corporation counts too. Georgia sets no fixed holding period after completion the way North Carolina’s 12-month rule does; it polices intent and the 24-month look-back. The kit prints exactly what the statute says and no more.',
  },
  {
    question: 'What building code is Georgia on?',
    answer:
      'As of January 1, 2026: the 2024 IRC with the 2026 Georgia Amendments for the house itself, alongside the 2024 IBC, IPC, IMC, IFGC, and ISPSC, and the 2023 NEC. The energy code is the odd one out — still the 2015 IECC with the Georgia Supplements and Amendments, untouched by the 2026 cycle. Two consequences follow. Georgia deletes the IRC’s plumbing, electrical, and energy parts, so trade work is inspected to the state IPC, NEC, and Georgia Energy Code, not IRC chapters. And two performance tests are mandatory: a blower door under 5 ACH50 and a duct-leakage test at or under 6 cfm25 per 100 square feet, both by a certified DET verifier. One relief: no fire sprinklers are required in one- and two-family dwellings (§ 8-2-4).',
  },
  {
    question: 'Do I need a permit if my county has no building department?',
    answer:
      'There may be no permit to pull — and the code still binds you. Permits and inspections are a power each city or county chooses to exercise (§ 8-2-26(a)(4)), and some exercise none of it. But the eight mandatory state minimum codes apply statewide with no local adoption required (§ 8-2-25(a)), and § 43-41-17(h) separately requires exempt owners to build in conformity with them. The state gates do not disappear either: on a septic lot, no physical development may begin until the county health department issues the septic construction permit (DPH Rule 511-3-1-.03(2)), and a driveway onto a state route needs GDOT’s permit before you touch the right-of-way. The kit’s first worksheet step is the call that settles who, if anyone, inspects your parcel.',
  },
];

const productSchema = generateProductSchema({
  name: 'Georgia Owner-Builder Permit Kit',
  description:
    'Georgia owner-builder permitting, start to finish: the O.C.G.A. § 43-41-17 exemption walkthrough with the 24-month one-sale rule, permit application checklist, inspection sequence, where-to-file directory, and forms index. 32 print-ready pages across 6 documents, with the statute and code citations printed on the page. Verified against O.C.G.A. sources, DCA amendment packets, DPH 511-3-1 septic rules, EPD, and GDOT regulations, August 2026.',
  image: `${SITE_URL}/binder/og-shop.jpg`,
  url: `${SITE_URL}/shop/ga-permit-kit`,
  price: PRICE,
  priceCurrency: 'USD',
  availability: 'InStock',
  brand: 'Build Your House',
  sku: 'ga-permit-kit',
});

const faqSchema = generateFAQSchema(FAQS);

export default function GAPermitKit() {
  return (
    <div className={styles.page}>
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(productSchema) }}
      />
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: schemaToScriptTag(faqSchema) }}
      />

      {/* ---------- HERO ---------- */}
      <section className={`${styles.hero} bp-band bp-grid`}>
        <span className={`${styles.crop} ${styles.tl}`} />
        <span className={`${styles.crop} ${styles.tr}`} />
        <span className={`${styles.crop} ${styles.bl}`} />
        <span className={`${styles.crop} ${styles.br}`} />
        <div className={styles.heroInner}>
          <div className={styles.heroGrid}>
            <div>
              <div className={`${styles.eyebrow} bp-eyebrow`}>
                Georgia · Permit Kit
              </div>
              <h1 className={styles.heroTitle}>Georgia Owner-Builder Permit Kit</h1>
              <p className={styles.heroSub}>
                Every permit, form, and inspection Georgia requires of an owner-builder — and
                the codes that bind you even in a county with no permit office. Verified against
                the statutes, citations printed on the page.
              </p>

              <div className={styles.dimstrip}>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Pages</span>
                  <span className={styles.v}>32</span>
                </div>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Documents</span>
                  <span className={styles.v}>06</span>
                </div>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Citations</span>
                  <span className={`${styles.v} ${styles.vText}`}>On-page</span>
                </div>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Price</span>
                  <span className={`${styles.v} ${styles.vAccent}`}>${PRICE}</span>
                </div>
              </div>

              <div className={styles.heroCtas}>
                <TrackedLink
                  href={STRIPE_CHECKOUT}
                  eventName="begin_checkout"
                  eventParams={{
                    currency: 'USD',
                    value: PRICE,
                    item_name: 'ga-permit-kit',
                    location: 'hero',
                  }}
                  className={styles.btnPrimary}
                >
                  Get the kit — ${PRICE}
                </TrackedLink>
                <TrackedLink
                  href="#contents"
                  eventName="shop_cta_click"
                  eventParams={{ location: 'gak_hero_see_inside', item_name: 'ga-permit-kit' }}
                  className={styles.btnGhost}
                >
                  See what&apos;s in it ↓
                </TrackedLink>
              </div>
              <p className={styles.heroFine}>
                One-time payment · Instant download · Part of the{' '}
                <TrackedLink
                  href="/shop"
                  eventName="shop_cta_click"
                  eventParams={{ location: 'gak_hero_family', context: 'ga-permit-kit' }}
                  className={styles.familyLink}
                >
                  Job Site Binder family
                </TrackedLink>
              </p>
            </div>

            <div className={styles.stack}>
              <img
                src="/binder/gak-checklist.webp"
                alt="A page of the Georgia permit application checklist stacked behind the exemption walkthrough."
                width={700}
                height={906}
                className={`${styles.sheet} ${styles.sheetDark} ${styles.stackBack}`}
              />
              <img
                src="/binder/gak-exempt.webp"
                alt="The Georgia owner-builder exemption walkthrough, page GA.1 of the permit kit."
                width={700}
                height={906}
                className={`${styles.sheet} ${styles.sheetDark} ${styles.stackFront}`}
              />
            </div>
          </div>
        </div>
      </section>

      {/* ---------- CONTENTS ---------- */}
      <section id="contents" className={`${styles.block} ${styles.anchor}`}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Contents</div>
              <h2 className={styles.secTitle}>Six documents, 32 pages</h2>
            </div>
            <div className={styles.secMeta}>
              Print-ready PDFs
              <br />
              Letter size
            </div>
          </div>

          <div className={styles.index}>
            {DOCS.map((d) => (
              <div key={d.no} className={styles.row}>
                <div className={styles.rowNo}>
                  {d.no}
                  <span className={styles.rowPages}>{d.pages}</span>
                </div>
                <div>
                  <h3 className={styles.rowTitle}>{d.title}</h3>
                  <p className={styles.rowCopy}>{d.copy}</p>
                </div>
                {d.thumb ? (
                  <figure className={styles.rowFig}>
                    <img
                      src={d.thumb}
                      alt={d.alt ?? ''}
                      width={700}
                      height={906}
                      loading="lazy"
                      className={styles.sheet}
                    />
                    <figcaption className={styles.sheetCap}>{d.caption}</figcaption>
                  </figure>
                ) : (
                  <span />
                )}
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ---------- WHAT THE KIT KNOWS ---------- */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Why it is worth $34</div>
              <h2 className={styles.secTitle}>
                What the kit knows that the internet doesn&apos;t
              </h2>
            </div>
            <div className={styles.secMeta}>
              Four examples
              <br />
              All checkable
            </div>
          </div>

          <p className={styles.lead}>
            Four things in this kit that most Georgia owner-builder advice gets wrong. Each one
            is checkable in a couple of minutes — which is the point of printing the citation.
          </p>

          <div className={styles.trust}>
            {KNOWS.map((k) => (
              <div key={k.label} className={styles.trustItem}>
                <Icon name={k.icon} size={26} className={styles.trustIco} />
                <div>
                  <p className={styles.trustLabel}>{k.label}</p>
                  <p className={styles.trustCopy}>{k.copy}</p>
                </div>
              </div>
            ))}
          </div>

          <p className={styles.trustSource}>
            Verified against O.C.G.A. sources, DCA amendment packets, DPH 511-3-1 septic rules,
            EPD, and GDOT regulations, August 2026 · Citations printed on each page
          </p>
        </div>
      </section>

      {/* ---------- ORDER ---------- */}
      <section id="purchase" className={`${styles.block} ${styles.anchor}`}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Order</div>
              <h2 className={styles.secTitle}>Get the permit kit</h2>
            </div>
            <div className={styles.secMeta}>
              One-time
              <br />
              Instant download
            </div>
          </div>

          <div className={styles.order}>
            <div className={styles.orderNo}>
              <span className="bp-sheet-no">GA Permit Kit</span>
              <span>Rev. August 2026</span>
            </div>

            <h3 className={styles.orderTitle}>
              The Georgia Owner-Builder Permit Kit
            </h3>

            <p className={`${styles.inclLabel} bp-mono-label`}>What you get</p>
            <ul className={styles.incl}>
              {INCLUDES.map((item) => (
                <li key={item}>{item}</li>
              ))}
            </ul>

            <div className={styles.priceRow}>
              <span className={styles.priceKey}>Price</span>
              <span className={styles.leader} aria-hidden="true" />
              <span className={styles.priceVal}>${PRICE}</span>
            </div>
            <div className={`${styles.orderDim} bp-dimline`}>
              One-time · Instant download
            </div>

            <TrackedLink
              href={STRIPE_CHECKOUT}
              eventName="begin_checkout"
              eventParams={{
                currency: 'USD',
                value: PRICE,
                item_name: 'ga-permit-kit',
                location: 'purchase_box',
              }}
              className={`${styles.btnPrimary} ${styles.orderCta}`}
            >
              Get the kit — ${PRICE}
            </TrackedLink>

            <div className={styles.smallprint}>
              <p className={styles.spItem}>
                <span className={styles.spKey}>Delivery</span>
                Instant download the moment payment clears.
              </p>
              <p className={styles.spItem}>
                <span className={styles.spKey}>Format</span>
                Print-ready PDFs, letter size. Print at home or at a copy shop.
              </p>
              <p className={styles.spItem}>
                <span className={styles.spKey}>Verify locally</span>
                Statutes and code editions change. Confirm each rule with your county or city —
                the kit prints its sources so you can.
              </p>
              <p className={styles.spItem}>
                <span className={styles.spKey}>Payment</span>${PRICE} one-time. No subscription,
                no renewal.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* ---------- FAQ ---------- */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Questions</div>
              <h2 className={styles.secTitle}>Frequently asked</h2>
            </div>
          </div>

          <div className={styles.faq}>
            {FAQS.map((f) => (
              <div key={f.question} className={styles.faqItem}>
                <h3 className={styles.faqQ}>{f.question}</h3>
                <p className={styles.faqA}>{f.answer}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* ---------- RELATED ---------- */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Related</div>
              <h2 className={styles.secTitle}>The free guide, and the other states</h2>
            </div>
            <div className={styles.secMeta}>
              One state each
              <br />
              Same format
            </div>
          </div>

          <div className={styles.smallprint}>
            <p className={styles.spItem}>
              <span className={styles.spKey}>Free guide</span>
              Start with the{' '}
              <TrackedLink
                href="/permitting/state-guides/georgia"
                eventName="shop_cta_click"
                eventParams={{ location: 'gak_related_guide', context: 'ga-permit-kit' }}
              >
                Georgia owner-builder guide
              </TrackedLink>{' '}
              — the free overview this kit turns into working paper.
            </p>
            <p className={styles.spItem}>
              <span className={styles.spKey}>North Carolina</span>
              Building across the line? The{' '}
              <TrackedLink
                href="/shop/nc-permit-kit"
                eventName="shop_cta_click"
                eventParams={{ location: 'gak_related', item_name: 'nc-permit-kit' }}
              >
                NC Permit Kit
              </TrackedLink>{' '}
              covers the same ground under North Carolina&apos;s statutes.
            </p>
            <p className={styles.spItem}>
              <span className={styles.spKey}>Texas</span>
              The{' '}
              <TrackedLink
                href="/shop/tx-permit-kit"
                eventName="shop_cta_click"
                eventParams={{ location: 'gak_related', item_name: 'tx-permit-kit' }}
              >
                TX Permit Kit
              </TrackedLink>
              , in the same six-document format.
            </p>
            <p className={styles.spItem}>
              <span className={styles.spKey}>Virginia</span>
              The{' '}
              <TrackedLink
                href="/shop/va-permit-kit"
                eventName="shop_cta_click"
                eventParams={{ location: 'gak_related', item_name: 'va-permit-kit' }}
              >
                VA Permit Kit
              </TrackedLink>
              , in the same six-document format.
            </p>
          </div>
        </div>
      </section>

      {/* ---------- CROSS-SELL ---------- */}
      <section className={styles.crossSell}>
        <div className={styles.wrap}>
          <BinderCTA
            context="ga-permit-kit"
            lead="The kit gets your permit. The binder runs the build — 367 pages of contracts, inspection forms, daily logs, and budget trackers covering every phase from footing to final, in the same print-and-go format."
          />
        </div>
      </section>
    </div>
  );
}
