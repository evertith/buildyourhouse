import type { Metadata } from 'next';
import BinderCTA from '@/components/BinderCTA';
import TrackedLink from '@/components/TrackedLink';
import Icon, { type IconName } from '@/components/Icon';
import { generateProductSchema, generateFAQSchema, schemaToScriptTag } from '@/lib/schema';
import styles from '../product.module.css';

const STRIPE_CHECKOUT = 'https://buy.stripe.com/7sYaEX3NZ40vgQc2cjfAc01';
const SITE_URL = 'https://build-your-house.com';
const PRICE = 34;

export const metadata: Metadata = {
  alternates: { canonical: '/shop/nc-permit-kit' },
  title: 'North Carolina Owner-Builder Permit Kit — $34',
  description:
    'Every permit, form, and inspection North Carolina requires of an owner-builder: the GC-license exemption walkthrough, NC permit application checklist, inspection sequence, and where-to-file directory. 27 print-ready pages with the statute citations on the page. $34 instant download.',
  keywords:
    'North Carolina owner builder permit, NC building permit checklist, NC owner builder exemption, North Carolina permit application, NC inspection sequence, NC lien agent',
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
    no: 'NC.0',
    pages: '2 pages',
    title: 'Cover & How to Use',
    copy:
      'What is in the kit, what order to work through it, and which documents you file versus which you keep on the truck.',
  },
  {
    no: 'NC.1',
    pages: '6 pages',
    title: 'Owner-Builder Exemption Walkthrough',
    copy:
      'The GC-license exemption, plain: what you must own, what you must occupy, and the twelve months you cannot sell, lease, or rent. Includes the Owner Exemption Affidavit you sign before the permit issues, with G.S. 87-1 and 87-14 cited on the page.',
    thumb: '/binder/nck-exempt.webp',
    caption: 'NC.1 Exemption walkthrough',
    alt: 'Page NC.1, the Owner-Builder Exemption Walkthrough: the license-exemption conditions listed with the North Carolina General Statute numbers printed beside each one.',
  },
  {
    no: 'NC.2',
    pages: '9 pages',
    title: 'Permit Application Checklist',
    copy:
      'Everything the county wants in the packet, in the order they ask for it: site plan, plans and specs, septic or sewer proof, lien agent designation, and the affidavit. Check the boxes and you have a complete application.',
    thumb: '/binder/nck-checklist.webp',
    caption: 'NC.2 Application checklist',
    alt: 'Page NC.2, the Permit Application Checklist: a ruled list of application documents with checkboxes and a column for the date each item was filed.',
  },
  {
    no: 'NC.3',
    pages: '5 pages',
    title: 'Inspection Sequence',
    copy:
      'Every inspection North Carolina calls for, in the order it is called, with what the inspector looks at and what has to be finished before you schedule it. Footing through final, including the trade inspections.',
    thumb: '/binder/nck-inspect.webp',
    caption: 'NC.3 Inspection sequence',
    alt: 'Page NC.3, the Inspection Sequence: North Carolina inspections listed in call order with the prerequisites for each and space to record the date passed.',
  },
  {
    no: 'NC.4',
    pages: '3 pages',
    title: 'Where-to-File Directory',
    copy:
      'Which office handles which piece: county building inspections, the environmental health department for septic, the electrical permit, and the lien agent filing. Who to call when the answer is not on the website.',
  },
  {
    no: 'NC.5',
    pages: '2 pages',
    title: 'Forms & Documents Index',
    copy:
      'Every form referenced in the kit, with its official name and the office that issues it, so you can pull a current copy yourself.',
  },
];

const INCLUDES: string[] = [
  '27 print-ready pages across 6 documents, letter size',
  'The owner-builder license exemption walkthrough (G.S. 87-1 and 87-14)',
  'A permit application checklist you can work straight through',
  'The full inspection sequence, in the order North Carolina calls it',
  'Where-to-file directory: building, electrical, septic, and lien agent',
  'Statute and code citations printed on the page, not linked away',
  'Lifetime access — re-download anytime with your purchase email',
];

const KNOWS: { icon: IconName; label: string; copy: string }[] = [
  {
    icon: 'doc',
    label: 'The lien agent threshold is $40,000 — not $30,000',
    copy:
      'North Carolina raised the project-cost trigger for designating a lien agent to $40,000, and a large number of owner-builder guides still print the old $30,000 figure. Either way a new house clears it, but the number matters when you are reading a form and deciding whether it applies to you. The kit uses the current threshold and cites the statute that sets it.',
  },
  {
    icon: 'bolt',
    label: 'Your house is wired under the 2017 NEC, not the 2020',
    copy:
      'North Carolina adopted the 2020 State Electrical Code but amended one- and two-family dwellings back out of it, so residential work is still inspected against the 2017 NEC. Guides that just report the state’s adopted edition get this backwards, and it changes real requirements. The kit says which edition applies to your house and tells you to confirm it with your inspections department.',
  },
  {
    icon: 'permit',
    label: 'The Construction Authorization is what unlocks the building permit',
    copy:
      'On a septic lot, the Improvement Permit is the first document — it says the soil will support a system. It is the Construction Authorization, issued after it, that the building inspector actually needs before a permit can be issued. Owner-builders routinely get the Improvement Permit, assume they are cleared, and lose weeks. The kit sequences both.',
  },
  {
    icon: 'check',
    label: 'You have to be at every inspection yourself',
    copy:
      'Under the owner exemption, the owner must be personally present for inspections unless the plans are sealed by an architect licensed under Chapter 83A — and an engineer’s seal does not satisfy it. You cannot send a sub or a spouse in your place. Plan your schedule around it before you break ground.',
  },
];

type Faq = { question: string; answer: string };

const FAQS: Faq[] = [
  {
    question: 'Do I need a contractor’s license to build my own house in North Carolina?',
    answer:
      'No. North Carolina exempts you from the general contractor license requirement for a home you own and will occupy as your primary residence, even though the project costs more than the $40,000 licensing threshold. You sign an Owner Exemption Affidavit before the permit is issued, and you cannot sell, lease, or rent the house for 12 months after completion. The kit walks the exemption conditions one at a time with the statute cited on the page.',
  },
  {
    question: 'How long does permitting take in North Carolina?',
    answer:
      'Plan review is the long pole, and it varies by county — commonly two to six weeks for a one- and two-family dwelling, longer in the fast-growing Piedmont counties. Septic adds its own clock: the soil evaluation and Improvement Permit come from environmental health before the Construction Authorization can issue. The kit lays out which clocks run in parallel and which have to run in order, so you can start the slow ones first.',
  },
  {
    question: 'Do I need a lien agent?',
    answer:
      'Yes, for new construction. North Carolina requires the owner to designate a lien agent for any improvement with a project cost of $40,000 or more, which a new house always clears. You designate through the state filing system and post the lien agent information at the job site. Doing it late is one of the more expensive owner-builder mistakes, because it affects who can claim against your title. The kit puts the designation in the permit checklist where it belongs.',
  },
  {
    question: 'Can someone else attend the inspections for me?',
    answer:
      'No. Building under the owner exemption, you must be personally present at inspections unless your plans are sealed by an architect licensed under North Carolina Chapter 83A. An engineer’s seal does not qualify, and a subcontractor standing in for you does not satisfy the requirement. If your work schedule cannot accommodate that, it is worth knowing before you apply rather than after.',
  },
];

const productSchema = generateProductSchema({
  name: 'North Carolina Owner-Builder Permit Kit',
  description:
    'North Carolina owner-builder permitting, start to finish: the GC-license exemption walkthrough, permit application checklist, inspection sequence, where-to-file directory, and forms index. 27 print-ready pages across 6 documents, with the statute and code citations printed on the page. Verified against ncleg.gov, NC OSFM, and NC DHHS sources, August 2026.',
  image: `${SITE_URL}/binder/og-shop.jpg`,
  url: `${SITE_URL}/shop/nc-permit-kit`,
  price: PRICE,
  priceCurrency: 'USD',
  availability: 'InStock',
  brand: 'Build Your House',
  sku: 'nc-permit-kit',
});

const faqSchema = generateFAQSchema(FAQS);

export default function NCPermitKit() {
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
                North Carolina · Permit Kit
              </div>
              <h1 className={styles.heroTitle}>North Carolina Owner-Builder Permit Kit</h1>
              <p className={styles.heroSub}>
                Every permit, form, and inspection North Carolina requires of an owner-builder —
                verified against the statutes, citations printed on the page.
              </p>

              <div className={styles.dimstrip}>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Pages</span>
                  <span className={styles.v}>27</span>
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
                    item_name: 'nc-permit-kit',
                    location: 'hero',
                  }}
                  className={styles.btnPrimary}
                >
                  Get the kit — ${PRICE}
                </TrackedLink>
                <TrackedLink
                  href="#contents"
                  eventName="shop_cta_click"
                  eventParams={{ location: 'nck_hero_see_inside', item_name: 'nc-permit-kit' }}
                  className={styles.btnGhost}
                >
                  See what&rsquo;s in it ↓
                </TrackedLink>
              </div>
              <p className={styles.heroFine}>
                One-time payment · Instant download · Part of the{' '}
                <TrackedLink
                  href="/shop"
                  eventName="shop_cta_click"
                  eventParams={{ location: 'nck_hero_family', context: 'nc-permit-kit' }}
                  className={styles.familyLink}
                >
                  Job Site Binder family
                </TrackedLink>
              </p>
            </div>

            <div className={styles.stack}>
              <img
                src="/binder/nck-checklist.webp"
                alt="A page of the NC permit application checklist stacked behind the exemption walkthrough."
                width={700}
                height={906}
                className={`${styles.sheet} ${styles.sheetDark} ${styles.stackBack}`}
              />
              <img
                src="/binder/nck-exempt.webp"
                alt="The North Carolina owner-builder exemption walkthrough, page NC.1 of the permit kit."
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
              <h2 className={styles.secTitle}>Six documents, 27 pages</h2>
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
                What the kit knows that the internet doesn&rsquo;t
              </h2>
            </div>
            <div className={styles.secMeta}>
              Four examples
              <br />
              All checkable
            </div>
          </div>

          <p className={styles.lead}>
            Four things in this kit that most North Carolina owner-builder advice gets wrong. Each
            one is checkable in a couple of minutes — which is the point of printing the citation.
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
            Verified against ncleg.gov, NC OSFM, and NC DHHS sources, August 2026 · Citations
            printed on each page
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
              <span className="bp-sheet-no">NC Permit Kit</span>
              <span>Rev. August 2026</span>
            </div>

            <h3 className={styles.orderTitle}>
              The North Carolina Owner-Builder Permit Kit
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
                item_name: 'nc-permit-kit',
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
                Statutes and code editions change. Confirm each rule with your county — the kit
                prints its sources so you can.
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

      {/* ---------- CROSS-SELL ---------- */}
      <section className={styles.crossSell}>
        <div className={styles.wrap}>
          <BinderCTA
            context="nc-permit-kit"
            lead="The kit gets your permit. The binder runs the build — 367 pages of contracts, inspection forms, daily logs, and budget trackers covering every phase from footing to final, in the same print-and-go format."
          />
        </div>
      </section>
    </div>
  );
}
