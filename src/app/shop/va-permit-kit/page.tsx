import type { Metadata } from 'next';
import BinderCTA from '@/components/BinderCTA';
import TrackedLink from '@/components/TrackedLink';
import Icon, { type IconName } from '@/components/Icon';
import { generateProductSchema, generateFAQSchema, schemaToScriptTag } from '@/lib/schema';
import styles from '../product.module.css';

// filled in after /admin/api/provision-products creates the payment link
const STRIPE_CHECKOUT = 'TODO_PAYMENT_LINK';
const SITE_URL = 'https://build-your-house.com';
const PRICE = 34;

export const metadata: Metadata = {
  alternates: { canonical: '/shop/va-permit-kit' },
  title: 'Virginia Owner-Builder Permit Kit — $34',
  description:
    'Every permit, form, and inspection Virginia requires of an owner-builder: the § 54.1-1101 license-exemption walkthrough, permit application checklist, USBC inspection sequence, and where-to-file directory. 31 print-ready pages with the statute citations on the page. $34 instant download.',
  keywords:
    'Virginia owner builder permit, VA building permit checklist, Virginia owner builder exemption, Virginia permit application, USBC inspection sequence, Virginia mechanics lien agent, VDOT entrance permit, VDH septic permit',
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
    no: 'VA.0',
    pages: '3 pages',
    title: 'Cover & How to Use',
    copy:
      'What is in the kit, what order to work through it, and the six Virginia headline facts — the exemption, the code edition, the lien agent line, the septic gate, the VDOT driveway permit, and the blower door — each with its citation.',
  },
  {
    no: 'VA.1',
    pages: '7 pages',
    title: 'Owner-Builder Exemption Walkthrough',
    copy:
      'The license exemption, plain: one primary residence, owned by you, for your own use, in any 24-month period — § 54.1-1101(A)(7) cited on the page. What you sign at the permit counter instead of a license number — the written statement supported by an affidavit that § 54.1-1111 requires — and the certificate-of-occupancy duty that follows you to closing.',
  },
  {
    no: 'VA.2',
    pages: '10 pages',
    title: 'Permit Application Checklist',
    copy:
      'Everything the locality wants in the packet, in the order they ask for it: site plan, plans (no architect seal required up to three stories), septic or sewer proof, the erosion agreement in lieu of a plan, the VDOT entrance permit, and the lien agent line. Check the boxes and you have a complete application.',
  },
  {
    no: 'VA.3',
    pages: '4 pages',
    title: 'Inspection Sequence',
    copy:
      'The seven statewide minimum inspections USBC § 113.3 calls for, quoted verbatim, in the order they are called — footing through final — with what has to be finished before you schedule each one, and where the blower-door and duct-test reports land.',
  },
  {
    no: 'VA.4',
    pages: '4 pages',
    title: 'Where-to-File Directory',
    copy:
      'Which counter handles which piece: the local building department, the local health department for septic and wells, the erosion and stormwater office, and the VDOT district for the driveway. Plus ten of Virginia’s busiest permit counters, with department names and domains confirmed.',
  },
  {
    no: 'VA.5',
    pages: '3 pages',
    title: 'Forms & Documents Index',
    copy:
      'Every form referenced in the kit, with its official title and the office that issues it — including the VDOT LUP-A and LUP-PE entrance forms and the VDH sewage and water application — so you can pull a current copy yourself.',
  },
];

const INCLUDES: string[] = [
  '31 print-ready pages across 6 documents, letter size',
  'The owner-builder license exemption walkthrough (§ 54.1-1101 and § 54.1-1111)',
  'A permit application checklist you can work straight through',
  'The full USBC inspection sequence, in the order Virginia calls it',
  'Where-to-file directory: building, septic and well, erosion, and the VDOT driveway',
  'Statute and code citations printed on the page, not linked away',
  'Lifetime access — re-download anytime with your purchase email',
];

const KNOWS: { icon: IconName; label: string; copy: string }[] = [
  {
    icon: 'doc',
    label: 'The lien agent line is optional — and it protects you, not them',
    copy:
      'Virginia puts a mechanics’ lien agent line on every one- and two-family dwelling permit — filled in only if you, the applicant, request it; otherwise the permit prints “None Designated” (§ 36-98.01). Most guides skip it because it is optional. Designate one anyway: § 43-4.01 then forces anyone who wants lien rights against your title to notify the agent within 30 days of first furnishing labor or materials, or the lien is limited to work performed after notice is finally given. The kit explains who can serve and where the line goes on the application.',
  },
  {
    icon: 'bolt',
    label: 'The blower door is mandatory — and Virginia’s number is 5, not 3',
    copy:
      'Every new Virginia dwelling gets a blower-door test — the visual-inspection alternative is gone — but Virginia amended the passing score to 5 ACH50, not the 3.0 the unamended 2021 IECC would demand. Guides that quote the raw I-Code make your target look stricter than it is. The kit prints the Virginia number, cites 13VAC5-63-264, and lists the seven categories of people allowed to run the test.',
  },
  {
    icon: 'permit',
    label: 'The septic office is on a 15-working-day shot clock — if you use the private lane',
    copy:
      'On an unsewered lot, septic approval gates the building permit. Wait in the general queue and you wait as long as it takes. Hire a licensed onsite soil evaluator — or a PE consulting one — and § 32.1-163.5 gives VDH 15 working days to act on a single-lot submission, or the design is deemed approved and the approval must issue. Most owner-builders never hear that the private lane exists. The kit sequences it.',
  },
  {
    icon: 'check',
    label: 'Your driveway probably needs a state permit before you cut it',
    copy:
      'Virginia is one of the few states where the state, not the county, maintains most roads outside cities. Unless you are in a city, a town that maintains its streets, or Henrico or Arlington, assume the road is VDOT’s — and no entrance may be constructed in the right-of-way until VDOT has approved the location and issued an entrance permit (24VAC30-73-60). The kit names the forms — LUP-A and LUP-PE — and puts them at the front of the checklist, where access belongs.',
  },
];

type Faq = { question: string; answer: string };

const FAQS: Faq[] = [
  {
    question: 'Can I build my own house in Virginia without a contractor’s license?',
    answer:
      'Yes. Code of Virginia § 54.1-1101(A)(7) exempts any person who performs or supervises the construction of no more than one primary residence owned by him and for his own use during any 24-month period. At the permit counter you sign a written statement, supported by an affidavit, that you are not subject to licensure — § 54.1-1111 forbids the building official to issue the permit without it. The exemption never waives the building code: § 54.1-1101(C) says exempt owners must still comply with the USBC, permits and inspections included. The kit walks the conditions one at a time with the statutes cited on the page.',
  },
  {
    question: 'Do I have to live in the house? Can I sell it afterward?',
    answer:
      'Virginia polices intent rather than a calendar. The exemption is for one primary residence built for your own use in any 24-month period — a house built to sell does not qualify — but the statute sets no fixed holding period after completion, unlike North Carolina’s 12-month rule. One string is attached: § 54.1-1101(B) requires an owner who used the exemption to obtain a certificate of occupancy before conveying the property to a third-party purchaser, unless the purchaser waives in writing, and violating it is a Class 1 misdemeanor. The kit prints exactly what the statute says and no more.',
  },
  {
    question: 'What inspections are required in Virginia?',
    answer:
      'USBC § 113.3 sets the statewide minimum, seven inspections: footing excavations and reinforcement before concrete is placed, foundation systems, preparatory work before concrete, structural members and fasteners before concealment, electrical, mechanical, and plumbing before concealment, energy conservation materials before concealment, and final. Nothing counts until it is inspected and approved (§ 113.1), and defective work must be corrected and reinspected before anything conceals it. The blower-door result and the signed duct-test report land at final. The kit lays the sequence out in call order with what has to be finished before you schedule each one.',
  },
  {
    question: 'Do I need a lien agent in Virginia?',
    answer:
      'No — and that is exactly why you should think about it. Virginia puts a mechanics’ lien agent line on every one- and two-family dwelling permit, filled in at the applicant’s option; if you skip it, the permit prints “None Designated” (§ 36-98.01). Designating one — an attorney, a title insurance company, or a financial institution (§ 43-1) — forces anyone who wants lien rights to notify the agent within 30 days of first furnishing labor or materials, or their lien is limited to work performed after notice is finally given (§ 43-4.01). It is one of the cheapest pieces of title protection an owner-builder can buy.',
  },
  {
    question: 'Can I do my own electrical, plumbing, and HVAC work?',
    answer:
      'The owner exemption in § 54.1-1101 switches off the entire licensing chapter, and Virginia defines a tradesman as someone who works for the general public for compensation (§ 54.1-1128) — an owner wiring his own primary residence is neither. That conclusion is a reading of two statutes together, not a sentence you can quote, so the kit prints both statutory bases and tells you to confirm with your building official before pulling the trade permits — some departments quiz owner applicants first. Either way, every trade still needs its permit and must pass its USBC inspection.',
  },
  {
    question: 'How long does permitting take in Virginia?',
    answer:
      'The USBC sets no fixed day-count for residential plan review — the official must act within a reasonable time (§ 110.1) — so the building permit itself is rarely the long pole. The state approvals are: VDH septic on an unsewered lot, which can hold up the building permit under USBC § 103.5 and runs on a 15-working-day clock if you use a private soil evaluator; the VDOT entrance permit for a driveway onto a state-maintained road; and land-disturbance approval before any dirt moves. The kit lays out which clocks run in parallel and which have to run in order, so you can start the slow ones first. Once issued, the permit is abandoned if work does not commence within six months.',
  },
];

const productSchema = generateProductSchema({
  name: 'Virginia Owner-Builder Permit Kit',
  description:
    'Virginia owner-builder permitting, start to finish: the § 54.1-1101 license-exemption walkthrough, permit application checklist, USBC inspection sequence, where-to-file directory, and forms index. 31 print-ready pages across 6 documents, with the statute and code citations printed on the page. Verified against law.lis.virginia.gov, DHCD/USBC, VDH, DEQ, and VDOT sources, August 2026.',
  image: `${SITE_URL}/binder/og-shop.jpg`,
  url: `${SITE_URL}/shop/va-permit-kit`,
  price: PRICE,
  priceCurrency: 'USD',
  availability: 'InStock',
  brand: 'Build Your House',
  sku: 'va-permit-kit',
});

const faqSchema = generateFAQSchema(FAQS);

export default function VAPermitKit() {
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
                Virginia · Permit Kit
              </div>
              <h1 className={styles.heroTitle}>Virginia Owner-Builder Permit Kit</h1>
              <p className={styles.heroSub}>
                Every permit, form, and inspection Virginia requires of an owner-builder —
                verified against the statutes, citations printed on the page.
              </p>

              <div className={styles.dimstrip}>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Pages</span>
                  <span className={styles.v}>31</span>
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
                    item_name: 'va-permit-kit',
                    location: 'hero',
                  }}
                  className={styles.btnPrimary}
                >
                  Get the kit — ${PRICE}
                </TrackedLink>
                <TrackedLink
                  href="#contents"
                  eventName="shop_cta_click"
                  eventParams={{ location: 'vak_hero_see_inside', item_name: 'va-permit-kit' }}
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
                  eventParams={{ location: 'vak_hero_family', context: 'va-permit-kit' }}
                  className={styles.familyLink}
                >
                  Job Site Binder family
                </TrackedLink>
              </p>
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
              <h2 className={styles.secTitle}>Six documents, 31 pages</h2>
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
            Four things in this kit that most Virginia owner-builder advice gets wrong. Each one
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
            Verified against law.lis.virginia.gov, DHCD/USBC, VDH, DEQ, and VDOT sources,
            August 2026 · Citations printed on each page
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
              <span className="bp-sheet-no">VA Permit Kit</span>
              <span>Rev. August 2026</span>
            </div>

            <h3 className={styles.orderTitle}>
              The Virginia Owner-Builder Permit Kit
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
                item_name: 'va-permit-kit',
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
                Statutes and code editions change. Confirm each rule with your locality — the
                kit prints its sources so you can.
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
                href="/permitting/state-guides/virginia"
                eventName="shop_cta_click"
                eventParams={{ location: 'vak_related_guide', context: 'va-permit-kit' }}
              >
                Virginia owner-builder guide
              </TrackedLink>{' '}
              — the free overview this kit turns into working paper.
            </p>
            <p className={styles.spItem}>
              <span className={styles.spKey}>North Carolina</span>
              Building across the line? The{' '}
              <TrackedLink
                href="/shop/nc-permit-kit"
                eventName="shop_cta_click"
                eventParams={{ location: 'vak_related', item_name: 'nc-permit-kit' }}
              >
                NC Permit Kit
              </TrackedLink>{' '}
              covers the same ground under North Carolina&apos;s statutes.
            </p>
            <p className={styles.spItem}>
              <span className={styles.spKey}>Georgia</span>
              The{' '}
              <TrackedLink
                href="/shop/ga-permit-kit"
                eventName="shop_cta_click"
                eventParams={{ location: 'vak_related', item_name: 'ga-permit-kit' }}
              >
                GA Permit Kit
              </TrackedLink>
              , in the same six-document format.
            </p>
            <p className={styles.spItem}>
              <span className={styles.spKey}>Texas</span>
              The{' '}
              <TrackedLink
                href="/shop/tx-permit-kit"
                eventName="shop_cta_click"
                eventParams={{ location: 'vak_related', item_name: 'tx-permit-kit' }}
              >
                TX Permit Kit
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
            context="va-permit-kit"
            lead="The kit gets your permit. The binder runs the build — 367 pages of contracts, inspection forms, daily logs, and budget trackers covering every phase from footing to final, in the same print-and-go format."
          />
        </div>
      </section>
    </div>
  );
}
