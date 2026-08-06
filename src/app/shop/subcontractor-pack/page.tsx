import type { Metadata } from 'next';
import BinderCTA from '@/components/BinderCTA';
import CalloutBox from '@/components/CalloutBox';
import TrackedLink from '@/components/TrackedLink';
import { generateProductSchema, generateFAQSchema, schemaToScriptTag } from '@/lib/schema';
import styles from '../product.module.css';

const STRIPE_CHECKOUT = 'https://buy.stripe.com/7sY28rckvaoT1Vi7wDfAc02';
const SITE_URL = 'https://build-your-house.com';
const PRICE = 29;

export const metadata: Metadata = {
  alternates: { canonical: '/shop/subcontractor-pack' },
  title: 'Subcontractor Hiring Pack — Contracts & Vetting Forms, $29',
  description:
    'Hire subcontractors like a general contractor: interview scorecard, reference check script, hiring walkthrough, and the contract set — subcontractor agreement, change order, lien waivers, and draw schedule, with editable Word versions. 36 print-ready pages, $29 instant download.',
  keywords:
    'subcontractor agreement template, subcontractor interview questions, contractor reference check, lien waiver template, change order form, payment draw schedule, hiring subcontractors owner builder',
  openGraph: {
    images: ['/binder/og-shop.jpg'],
  },
};

type PackDoc = {
  no: string;
  pages: string;
  title: string;
  copy: string;
  note?: string;
  thumb?: string;
  caption?: string;
  alt?: string;
};

const DOCS: PackDoc[] = [
  {
    no: 'SH.1',
    pages: '4 pages',
    title: 'Interview Scorecard',
    copy:
      'The same questions for every sub, scored the same way, on one sheet. Licensing and insurance, crew size, current workload, who actually swings the hammer, and what happens when the schedule slips. Fill one out per bidder and the comparison makes itself.',
    thumb: '/binder/subpack-scorecard.webp',
    caption: 'SH.1 Interview scorecard',
    alt: 'Page SH.1, the Interview Scorecard: a ruled sheet of standard subcontractor interview questions with a score column and space for notes on each answer.',
  },
  {
    no: 'SH.2',
    pages: '3 pages',
    title: 'Reference Check Form',
    copy:
      'A script for the call most owner-builders skip. What to ask the last three customers, what to ask the supply house, and the two questions that get an honest answer about whether the crew finished on time.',
  },
  {
    no: 'SH.3',
    pages: '3 pages',
    title: 'Hiring Walkthrough',
    copy:
      'The order of operations: how many bids to get, what to send bidders so the numbers are comparable, when to verify the license and call the insurance carrier, and what to have signed before anyone starts.',
    thumb: '/binder/subpack-walkthrough.webp',
    caption: 'SH.3 Hiring walkthrough',
    alt: 'Page SH.3, the Hiring Walkthrough: the sequence for bidding and hiring a subcontractor laid out as numbered steps with the documents required at each one.',
  },
  {
    no: 'SH.4',
    pages: '3 pages',
    title: 'Red Flags & Walk-Away List',
    copy:
      'The answers that end the interview, and why each one predicts trouble. Printed so you can hand it to whoever is taking the call when you are not there.',
    thumb: '/binder/subpack-redflags.webp',
    caption: 'SH.4 Red flags',
    alt: 'Page SH.4, the Red Flags list: subcontractor warning signs printed one per row with a short explanation of the risk each one signals.',
  },
  {
    no: 'SH.5',
    pages: '9 pages',
    title: 'Subcontractor Agreement',
    copy:
      'The contract itself, with the blanks left where your scope, price, schedule, and payment terms go. Covers insurance requirements, cleanup, warranty, and what happens if the work fails inspection.',
    note: 'From the Job Site Binder · editable Word version included',
  },
  {
    no: 'SH.6',
    pages: '3 pages',
    title: 'Change Order Form',
    copy:
      'Price and schedule impact of a change, signed before the work happens. The document that keeps a verbal “while you’re in there” from becoming an invoice you did not agree to.',
    note: 'From the Job Site Binder · editable Word version included',
  },
  {
    no: 'SH.7',
    pages: '5 pages',
    title: 'Lien Waiver Templates',
    copy:
      'Conditional and unconditional waivers, partial and final. You exchange one for each payment, and they are how you prove at closing that nobody can still claim against your title.',
    note: 'From the Job Site Binder · editable Word version included',
  },
  {
    no: 'SH.8',
    pages: '4 pages',
    title: 'Payment Draw Schedule',
    copy:
      'Payments tied to completed, inspected work instead of the calendar — with the retainage line that gives you leverage on the punch list.',
    note: 'From the Job Site Binder · editable Word version included',
  },
];

const RED_FLAGS: { flag: string; why: string }[] = [
  {
    flag: 'No license number, or one that does not come back active.',
    why: 'Every state board has a free lookup. A sub who cannot give you the number to check has told you the answer.',
  },
  {
    flag: 'The certificate of insurance is always coming later.',
    why: 'You verify coverage by calling the carrier on the certificate, not by receiving a PDF. If it never arrives, their lapse becomes your liability.',
  },
  {
    flag: 'Wants a large deposit before any material is on site.',
    why: 'Some money up front is normal for materials. A big check against nothing delivered is how subs fund the job they are behind on.',
  },
  {
    flag: 'Will not put the scope in writing.',
    why: '“We will figure it out as we go” always resolves in their favor once your framing is open and their crew is the one standing in it.',
  },
  {
    flag: 'No references from the last twelve months.',
    why: 'Old references are a portfolio. Recent ones tell you how the crew is running right now, which is what you are actually buying.',
  },
  {
    flag: 'Cannot tell you who will be on your job.',
    why: 'You are hiring a crew, not a company. If the person bidding is not the person working, find out who is before you sign.',
  },
];

const INCLUDES: string[] = [
  '36 print-ready pages across 8 documents, letter size',
  'Interview scorecard and reference check script',
  'The hiring walkthrough: bid, verify, sign, in order',
  'Red flags and walk-away list',
  'Subcontractor agreement, change order, lien waivers, draw schedule',
  'Editable Word versions of all four contract documents',
  'Lifetime access — re-download anytime with your purchase email',
];

type Faq = { question: string; answer: string };

const FAQS: Faq[] = [
  {
    question: 'Is this included in the $97 Job Site Binder?',
    answer:
      'The four contract documents are, word for word — the subcontractor agreement, change order form, lien waivers, and draw schedule all come from the binder, with the same editable Word versions. The interview scorecard, reference check form, hiring walkthrough, and red-flag list are the hiring half. If you are going to buy the binder, buy the binder. Buy this pack if hiring subs is the only part you need help with right now.',
  },
  {
    question: 'Can I edit the contracts?',
    answer:
      'Yes. All four contract documents come as editable Word files alongside the print-ready PDFs, so you can drop in your project details, scope language, and payment terms. They open in Microsoft Word, Google Docs, or LibreOffice.',
  },
  {
    question: 'Will these contracts hold up in my state?',
    answer:
      'They are general-purpose construction documents of the kind used nationwide, and they are a far better starting point than a handshake or a one-line estimate. They are not legal advice. Lien waiver requirements in particular are state-specific — several states prescribe statutory waiver forms — so have a local construction attorney review the set before you use it on a real build.',
  },
  {
    question: 'How many subs can I use these for?',
    answer:
      'As many as your build needs. Print a scorecard for every bidder and a contract for every trade you hire. The license covers your own owner-builder project — please do not redistribute or resell the files.',
  },
];

const productSchema = generateProductSchema({
  name: 'Subcontractor Hiring Pack',
  description:
    'Hire subs like a GC: interview scorecard, reference check script, hiring walkthrough, and red-flag list, plus the subcontractor agreement, change order form, lien waivers, and payment draw schedule — print-ready PDFs with editable Word versions of all four contract documents. 36 pages across 8 documents.',
  image: `${SITE_URL}/binder/og-shop.jpg`,
  url: `${SITE_URL}/shop/subcontractor-pack`,
  price: PRICE,
  priceCurrency: 'USD',
  availability: 'InStock',
  brand: 'Build Your House',
  sku: 'sub-hiring-pack',
});

const faqSchema = generateFAQSchema(FAQS);

export default function SubcontractorPack() {
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
              <div className={`${styles.eyebrow} bp-eyebrow`}>Contracts &amp; Vetting</div>
              <h1 className={styles.heroTitle}>Subcontractor Hiring Pack</h1>
              <p className={styles.heroSub}>
                Hire subs like a GC: scorecard, reference script, and the contract set — with
                editable Word versions.
              </p>

              <div className={styles.dimstrip}>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Pages</span>
                  <span className={styles.v}>36</span>
                </div>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Documents</span>
                  <span className={styles.v}>08</span>
                </div>
                <div className={styles.dimcell}>
                  <span className={styles.k}>Editable</span>
                  <span className={styles.v}>04</span>
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
                    item_name: 'sub-hiring-pack',
                    location: 'hero',
                  }}
                  className={styles.btnPrimary}
                >
                  Get the pack — ${PRICE}
                </TrackedLink>
                <TrackedLink
                  href="#contents"
                  eventName="shop_cta_click"
                  eventParams={{ location: 'subpack_hero_see_inside', item_name: 'sub-hiring-pack' }}
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
                  eventParams={{ location: 'subpack_hero_family', context: 'sub-hiring-pack' }}
                  className={styles.familyLink}
                >
                  Job Site Binder family
                </TrackedLink>
              </p>
            </div>

            <div className={styles.stack}>
              <img
                src="/binder/subpack-walkthrough.webp"
                alt="A page of the hiring walkthrough stacked behind the interview scorecard."
                width={700}
                height={906}
                className={`${styles.sheet} ${styles.sheetDark} ${styles.stackBack}`}
              />
              <img
                src="/binder/subpack-scorecard.webp"
                alt="The subcontractor interview scorecard, page SH.1 of the hiring pack."
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
              <h2 className={styles.secTitle}>Eight documents, 36 pages</h2>
            </div>
            <div className={styles.secMeta}>
              Print-ready PDFs
              <br />4 editable Word files
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
                  {d.note ? <span className={styles.rowNote}>{d.note}</span> : null}
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

            {/* Makes the page column add up to 36 for anyone who checks. */}
            <div className={`${styles.row} ${styles.rowQuiet}`}>
              <div className={styles.rowNo}>
                FRONT MATTER
                <span className={styles.rowPages}>2 pages</span>
              </div>
              <p className={styles.rowQuietCopy}>Cover · how to use the pack · contents</p>
              <span />
            </div>
          </div>
        </div>
      </section>

      {/* ---------- WALK-AWAY LIST ---------- */}
      <section className={styles.block}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>The walk-away list</div>
              <h2 className={styles.secTitle}>Six answers that end the interview</h2>
            </div>
            <div className={styles.secMeta}>
              Page SH.4
              <br />
              Printed to hand over
            </div>
          </div>

          <p className={styles.lead}>
            Vetting is cheap and firing a sub mid-build is not. These are the answers that mean you
            keep looking — each one printed with the reason it predicts trouble, so the judgment
            call is not yours alone to remember.
          </p>

          <div className={styles.split}>
            <ul className={styles.flagList}>
              {RED_FLAGS.map((f) => (
                <li key={f.flag}>
                  <strong>{f.flag}</strong> {f.why}
                </li>
              ))}
            </ul>

            <figure className={styles.splitFig}>
              <img
                src="/binder/subpack-redflags.webp"
                alt="Full page SH.4 of the hiring pack: the subcontractor red-flag list, each warning sign printed with the risk it signals."
                width={700}
                height={906}
                loading="lazy"
                className={styles.sheet}
              />
              <figcaption className={styles.sheetCap}>SH.4 Red flags — full page</figcaption>
            </figure>
          </div>

          <CalloutBox type="info" title="If you are buying the binder, skip this pack">
            Every contract in this pack — the subcontractor agreement, change order form, lien
            waivers, and draw schedule — is already in the $97 Job Site Binder, with the same
            editable Word versions. Buy the pack if hiring subs is the only part you need. Buy the
            binder if you want the whole build covered; you would be paying twice for the contracts
            otherwise.
          </CalloutBox>
        </div>
      </section>

      {/* ---------- ORDER ---------- */}
      <section id="purchase" className={`${styles.block} ${styles.anchor}`}>
        <div className={styles.wrap}>
          <div className={styles.secHead}>
            <div>
              <div className={styles.secLabel}>Order</div>
              <h2 className={styles.secTitle}>Get the hiring pack</h2>
            </div>
            <div className={styles.secMeta}>
              One-time
              <br />
              Instant download
            </div>
          </div>

          <div className={styles.order}>
            <div className={styles.orderNo}>
              <span className="bp-sheet-no">Subcontractor Hiring Pack</span>
              <span>Rev. 2026</span>
            </div>

            <h3 className={styles.orderTitle}>The Subcontractor Hiring Pack</h3>

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
                item_name: 'sub-hiring-pack',
                location: 'purchase_box',
              }}
              className={`${styles.btnPrimary} ${styles.orderCta}`}
            >
              Get the pack — ${PRICE}
            </TrackedLink>

            <div className={styles.smallprint}>
              <p className={styles.spItem}>
                <span className={styles.spKey}>Delivery</span>
                Instant download the moment payment clears.
              </p>
              <p className={styles.spItem}>
                <span className={styles.spKey}>Format</span>
                Print-ready PDFs plus editable Word files for the four contracts.
              </p>
              <p className={styles.spItem}>
                <span className={styles.spKey}>Not legal advice</span>
                General-purpose construction documents. Have a local attorney review them before
                you use them on a real build.
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
            context="sub-hiring-pack"
            lead="Already know you'll want the whole system? The pack's contents are part of the binder's 367 pages — every contract here, plus the inspection forms, daily logs, budget trackers, and phase checklists for the rest of the build."
          />
        </div>
      </section>
    </div>
  );
}
